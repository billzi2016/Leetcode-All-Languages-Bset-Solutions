# 2724. Sort By

## Javascript

```javascript
/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    // Create a shallow copy to avoid mutating the original array,
    // then sort based on the numeric value returned by fn.
    return arr.slice().sort((a, b) => fn(a) - fn(b));
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (value: JSONValue) => number;

function sortBy(arr: JSONValue[], fn: Fn): JSONValue[] {
    return arr.slice().sort((a, b) => fn(a) - fn(b));
}
```
