# 2665. Counter II

## Javascript

```javascript
/**
 * @param {integer} init
 * @return {{increment: Function, decrement: Function, reset: Function}}
 */
var createCounter = function(init) {
    let current = init;
    return {
        increment: () => ++current,
        decrement: () => --current,
        reset: () => (current = init)
    };
};
```

## Typescript

```typescript
type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let current = init;
    const start = init;
    return {
        increment: () => {
            current += 1;
            return current;
        },
        decrement: () => {
            current -= 1;
            return current;
        },
        reset: () => {
            current = start;
            return current;
        }
    };
}
```
