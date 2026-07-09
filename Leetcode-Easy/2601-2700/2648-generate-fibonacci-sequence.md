# 2648. Generate Fibonacci Sequence

## Javascript

```javascript
/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        const next = a + b;
        a = b;
        b = next;
    }
};
```

## Typescript

```typescript
function* fibGenerator(): Generator<number, any, number> {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}
```
