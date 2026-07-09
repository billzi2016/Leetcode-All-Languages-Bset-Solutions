# 2620. Counter

## Javascript

```javascript
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let cur = n;
    return function() {
        return cur++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
```

## Typescript

```typescript
function createCounter(n: number): () => number {
    let current = n;
    return () => current++;
}

/** 
 * const counter = createCounter(10)
 * console.log(counter()) // 10
 * console.log(counter()) // 11
 * console.log(counter()) // 12
 */
```
