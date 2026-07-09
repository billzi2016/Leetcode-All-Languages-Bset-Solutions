# 2715. Timeout Cancellation

## Javascript

```javascript
/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);
    return function cancelFn() {
        clearTimeout(timerId);
    };
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
    const timer = setTimeout(() => {
        fn(...args);
    }, t);
    return () => clearTimeout(timer);
}
```
