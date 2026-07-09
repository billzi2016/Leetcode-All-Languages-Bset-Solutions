# 2650. Design Cancellable Function

## Javascript

```javascript
var cancellable = function(generator) {
    let finished = false;
    let cancelled = false;
    let active = false; // waiting for current yielded promise
    let resolveOuter, rejectOuter;
    const outerPromise = new Promise((res, rej) => {
        resolveOuter = res;
        rejectOuter = rej;
    });

    function step(method, arg) {
        if (finished) return;
        let result;
        try {
            result = method === 'next' ? generator.next(arg) : generator.throw(arg);
        } catch (e) {
            finished = true;
            rejectOuter(e);
            return;
        }
        const { value, done } = result;
        if (done) {
            finished = true;
            resolveOuter(value);
            return;
        }
        active = true;
        Promise.resolve(value).then(
            v => {
                if (!active) return;
                active = false;
                step('next', v);
            },
            err => {
                if (!active) return;
                active = false;
                step('throw', err);
            }
        );
    }

    // start execution
    step('next');

    function cancel() {
        if (finished || cancelled) return;
        cancelled = true;
        active = false; // ignore pending promise callbacks
        try {
            step('throw', "Cancelled");
        } catch (_) {}
    }

    return [cancel, outerPromise];
};
```

## Typescript

```typescript
function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {
    let resolveFn!: (value: T) => void;
    let rejectFn!: (reason: any) => void;
    const outer = new Promise<T>((resolve, reject) => {
        resolveFn = resolve;
        rejectFn = reject;
    });

    let step = 0; // version counter for current awaiting promise
    let finished = false;

    function finish() {
        finished = true;
        step = -1;
    }

    function handle(iterResult: IteratorResult<Promise<any>, T>) {
        if (finished) return;
        if (iterResult.done) {
            resolveFn(iterResult.value);
            finish();
            return;
        }
        const promise = iterResult.value;
        const myStep = ++step; // capture version for this wait
        promise.then(
            (val) => {
                if (myStep !== step) return; // cancelled during wait
                try {
                    handle(generator.next(val));
                } catch (e) {
                    rejectFn(e);
                    finish();
                }
            },
            (err) => {
                if (myStep !== step) return;
                try {
                    handle(generator.throw(err));
                } catch (e) {
                    rejectFn(e);
                    finish();
                }
            }
        );
    }

    // start execution
    try {
        handle(generator.next());
    } catch (e) {
        rejectFn(e);
        finish();
    }

    function cancel() {
        if (finished) return;
        ++step; // invalidate any pending promise callbacks
        try {
            const iterResult = generator.throw("Cancelled");
            handle(iterResult);
        } catch (e) {
            rejectFn(e);
            finish();
        }
    }

    return [cancel, outer];
}

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
```
