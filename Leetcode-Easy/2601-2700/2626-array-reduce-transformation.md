# 2626. Array Reduce Transformation

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let res = init;
    for (let i = 0; i < nums.length; i++) {
        res = fn(res, nums[i]);
    }
    return res;
};
```

## Typescript

```typescript
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let res = init;
    for (let i = 0; i < nums.length; i++) {
        res = fn(res, nums[i]);
    }
    return res;
}
```
