# 2627. Debounce

## Javascript

```javascript
/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timer;
    return function(...args) {
        const context = this;
        clearTimeout(timer);
        timer = setTimeout(() => {
            fn.apply(context, args);
        }, t);
    };
};
```

## Typescript

```typescript
type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let timer: NodeJS.Timeout | null = null;
    return function(...args: number[]) {
        if (timer !== null) clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    };
}
```
