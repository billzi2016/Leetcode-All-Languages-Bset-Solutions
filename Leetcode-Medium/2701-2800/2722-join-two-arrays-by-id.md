# 2722. Join Two Arrays by ID

## Javascript

```javascript
/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const map = new Map();
    for (const obj of arr1) {
        map.set(obj.id, { ...obj });
    }
    for (const obj of arr2) {
        if (map.has(obj.id)) {
            const merged = { ...map.get(obj.id), ...obj };
            map.set(obj.id, merged);
        } else {
            map.set(obj.id, { ...obj });
        }
    }
    const result = Array.from(map.values());
    result.sort((a, b) => a.id - b.id);
    return result;
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    const map = new Map<number, any>();

    for (const obj of arr1) {
        // store a shallow copy to avoid mutating original objects
        map.set(obj.id, { ...obj });
    }

    for (const obj of arr2) {
        if (map.has(obj.id)) {
            const existing = map.get(obj.id);
            Object.assign(existing, obj); // properties from arr2 override
        } else {
            map.set(obj.id, { ...obj });
        }
    }

    const result: ArrayType[] = Array.from(map.values());
    result.sort((a, b) => a.id - b.id);
    return result;
}
```
