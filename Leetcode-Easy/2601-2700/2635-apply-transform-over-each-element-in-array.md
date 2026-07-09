# 2635. Apply Transform Over Each Element in Array

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        res[i] = fn(arr[i], i);
    }
    return res;
};
```

## Typescript

```typescript
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const result: number[] = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        result[i] = fn(arr[i], i);
    }
    return result;
}
```
