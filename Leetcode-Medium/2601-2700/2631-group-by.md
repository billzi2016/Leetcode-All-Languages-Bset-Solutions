# 2631. Group By

## Javascript

```javascript
/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const groups = Object.create(null);
    for (let i = 0; i < this.length; i++) {
        const key = fn(this[i], i, this);
        if (!Object.prototype.hasOwnProperty.call(groups, key)) {
            groups[key] = [];
        }
        groups[key].push(this[i]);
    }
    return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
```

## Typescript

```typescript
interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>
}

Array.prototype.groupBy = function<T>(this: T[], fn: (item: T) => string): Record<string, T[]> {
    const result: Record<string, T[]> = {};
    for (const item of this) {
        const key = fn(item);
        if (!(key in result)) {
            result[key] = [];
        }
        result[key].push(item);
    }
    return result;
};
```
