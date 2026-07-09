# 2666. Allow One Function Call

## Javascript

```javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called = false;
    return function(...args) {
        if (!called) {
            called = true;
            return fn.apply(this, args);
        }
        // subsequent calls do nothing (undefined)
    };
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let called = false;
    return function (...args: JSONValue[]): JSONValue | undefined {
        if (called) return undefined;
        called = true;
        return (fn as (...a: any[]) => any)(...args);
    };
}
```
