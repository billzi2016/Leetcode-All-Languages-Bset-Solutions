# 2637. Promise Time Limit

## Javascript

```javascript
/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise((resolve, reject) => {
            let settled = false;
            const timer = setTimeout(() => {
                if (!settled) {
                    settled = true;
                    reject("Time Limit Exceeded");
                }
            }, t);
            Promise.resolve()
                .then(() => fn(...args))
                .then(value => {
                    if (settled) return;
                    settled = true;
                    clearTimeout(timer);
                    resolve(value);
                })
                .catch(err => {
                    if (settled) return;
                    settled = true;
                    clearTimeout(timer);
                    reject(err);
                });
        });
    };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
```

## Typescript

```typescript
type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    return async function(...args: any[]): Promise<any> {
        return new Promise((resolve, reject) => {
            const timer = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);

            let promise: Promise<any>;
            try {
                promise = fn(...args);
            } catch (err) {
                clearTimeout(timer);
                reject(err);
                return;
            }

            promise
                .then((value) => {
                    clearTimeout(timer);
                    resolve(value);
                })
                .catch((error) => {
                    clearTimeout(timer);
                    reject(error);
                });
        });
    };
}

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
```
