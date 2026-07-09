# 2619. Array Prototype Last

## Javascript

```javascript
/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    return this.length ? this[this.length - 1] : -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
```

## Typescript

```typescript
interface Array<T> {
    last(): T | -1;
}

Array.prototype.last = function(this: any[]) {
    return this.length ? this[this.length - 1] : -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
```
