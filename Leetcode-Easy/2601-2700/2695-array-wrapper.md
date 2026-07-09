# 2695. Array Wrapper

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums || [];
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((acc, cur) => acc + cur, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return JSON.stringify(this.nums);
}
```

## Typescript

```typescript
class ArrayWrapper {
    private nums: number[];
    
    constructor(nums: number[]) {
        this.nums = nums;
    }
    
    valueOf(): number {
        return this.nums.reduce((sum, val) => sum + val, 0);
    }
    
    toString(): string {
        return JSON.stringify(this.nums);
    }
}
```
