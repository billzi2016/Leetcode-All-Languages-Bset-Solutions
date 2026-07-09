# 2625. Flatten Deeply Nested Array

## Javascript

```javascript
/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];
    function dfs(subArr, depth) {
        for (const el of subArr) {
            if (Array.isArray(el) && depth < n) {
                dfs(el, depth + 1);
            } else {
                result.push(el);
            }
        }
    }
    dfs(arr, 0);
    return result;
};
```

## Typescript

```typescript
type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr: MultiDimensionalArray, n: number): MultiDimensionalArray {
    const result: MultiDimensionalArray = [];
    const dfs = (subArr: MultiDimensionalArray, depth: number): void => {
        for (const el of subArr) {
            if (Array.isArray(el)) {
                if (depth < n) {
                    dfs(el as MultiDimensionalArray, depth + 1);
                } else {
                    result.push(el as MultiDimensionalArray);
                }
            } else {
                result.push(el as number);
            }
        }
    };
    dfs(arr, 0);
    return result;
};
```
