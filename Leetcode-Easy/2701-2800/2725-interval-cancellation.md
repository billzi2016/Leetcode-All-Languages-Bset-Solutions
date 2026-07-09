# 2725. Interval Cancellation

## Javascript

```javascript
/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Call immediately
    fn(...args);
    // Schedule repeated calls
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);
    // Return cancel function
    return function() {
        clearInterval(intervalId);
    };
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
    fn(...args);
    const id = setInterval(() => fn(...args), t);
    return () => clearInterval(id as any);
}
```
