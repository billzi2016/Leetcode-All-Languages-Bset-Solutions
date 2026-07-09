# 2649. Nested Array Generator

## Javascript

```javascript
/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function* (arr) {
    const stack = [{ arr, idx: 0 }];
    while (stack.length) {
        const frame = stack[stack.length - 1];
        if (frame.idx >= frame.arr.length) {
            stack.pop();
            continue;
        }
        const val = frame.arr[frame.idx++];
        if (Array.isArray(val)) {
            stack.push({ arr: val, idx: 0 });
        } else {
            yield val;
        }
    }
};
```

## Typescript

```typescript
type MultidimensionalArray = (MultidimensionalArray | number)[];

function* inorderTraversal(arr: MultidimensionalArray): Generator<number, void, unknown> {
    for (const el of arr) {
        if (Array.isArray(el)) {
            yield* inorderTraversal(el);
        } else {
            yield el;
        }
    }
}
```
