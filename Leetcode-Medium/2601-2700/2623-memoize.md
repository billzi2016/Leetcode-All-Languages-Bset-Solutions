# 2623. Memoize

## Javascript

```javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn.apply(this, args);
        cache.set(key, result);
        return result;
    };
}
```

## Typescript

```typescript
type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache = new Map<string, number>()
    return function(...args: number[]): number {
        const key = JSON.stringify(args)
        if (cache.has(key)) {
            return cache.get(key)!
        }
        const result = fn(...args)
        cache.set(key, result)
        return result
    }
}
```
