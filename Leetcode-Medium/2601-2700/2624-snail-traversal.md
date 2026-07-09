# 2624. Snail Traversal

## Javascript

```javascript
/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    const total = this.length;
    if (rowsCount <= 0 || colsCount <= 0 || rowsCount * colsCount !== total) return [];
    const result = Array.from({ length: rowsCount }, () => new Array(colsCount));
    for (let i = 0; i < total; ++i) {
        const col = Math.floor(i / rowsCount);
        const row = (col % 2 === 0) ? (i % rowsCount) : (rowsCount - 1 - (i % rowsCount));
        result[row][col] = this[i];
    }
    return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
```

## Typescript

```typescript
interface Array<T> {
    snail(rowsCount: number, colsCount: number): number[][];
}

Array.prototype.snail = function(rowsCount: number, colsCount: number): number[][] {
    const nums = this as unknown as number[];
    if (rowsCount * colsCount !== nums.length) return [];

    const result: number[][] = Array.from({ length: rowsCount }, () => new Array<number>(colsCount));

    for (let i = 0; i < nums.length; ++i) {
        const col = Math.floor(i / rowsCount);
        const row = (col % 2 === 0) ? (i % rowsCount) : (rowsCount - 1 - (i % rowsCount));
        result[row][col] = nums[i];
    }

    return result;
};
```
