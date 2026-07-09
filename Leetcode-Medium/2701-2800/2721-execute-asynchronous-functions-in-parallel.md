# 2721. Execute Asynchronous Functions in Parallel

## Javascript

```javascript
/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const total = functions.length;
        if (total === 0) {
            resolve([]);
            return;
        }
        const results = new Array(total);
        let resolvedCount = 0;

        for (let i = 0; i < total; i++) {
            try {
                const p = functions[i]();
                Promise.resolve(p).then(value => {
                    results[i] = value;
                    resolvedCount++;
                    if (resolvedCount === total) {
                        resolve(results);
                    }
                }).catch(err => reject(err));
            } catch (err) {
                reject(err);
                break;
            }
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
```

## Typescript

```typescript
type Fn<T> = () => Promise<T>;

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
    return new Promise<T[]>((resolve, reject) => {
        const len = functions.length;
        if (len === 0) {
            resolve([]);
            return;
        }
        const results = new Array<T>(len);
        let resolvedCount = 0;

        functions.forEach((fn, index) => {
            try {
                const p = fn();
                p.then(value => {
                    results[index] = value;
                    resolvedCount++;
                    if (resolvedCount === len) {
                        resolve(results);
                    }
                }).catch(err => {
                    reject(err);
                });
            } catch (err) {
                reject(err);
            }
        });
    });
}

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
```
