# 2727. Is Object Empty

## Javascript

```javascript
/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }
    // For plain objects, check own enumerable keys
    return Object.keys(obj).length === 0;
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[];

function isEmpty(obj: Obj): boolean {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }
    // For plain objects
    return Object.keys(obj as Record<string, unknown>).length === 0;
}
```
