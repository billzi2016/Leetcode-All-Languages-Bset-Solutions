# 2705. Compact Object

## Javascript

```javascript
/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    const dfs = (val) => {
        // Remove falsy primitives (false, 0, "", null, undefined, NaN)
        if (!val) return undefined;

        if (Array.isArray(val)) {
            const res = [];
            for (const item of val) {
                const processed = dfs(item);
                if (processed !== undefined) {
                    res.push(processed);
                }
            }
            return res;
        }

        if (typeof val === 'object') { // non‑null object
            const res = {};
            for (const key in val) {
                if (Object.prototype.hasOwnProperty.call(val, key)) {
                    const processed = dfs(val[key]);
                    if (processed !== undefined) {
                        res[key] = processed;
                    }
                }
            }
            return res;
        }

        // Truthy primitive
        return val;
    };

    return dfs(obj);
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    const dfs = (value: JSONValue): any => {
        if (value === null) return undefined;

        if (Array.isArray(value)) {
            const res: JSONValue[] = [];
            for (const item of value) {
                if (item === null) continue;
                if (typeof item === 'object') {
                    const processed = dfs(item);
                    if (processed !== undefined) res.push(processed);
                } else {
                    if (Boolean(item)) res.push(item);
                }
            }
            return res;
        }

        if (typeof value === 'object') {
            const res: Record<string, JSONValue> = {};
            for (const [k, v] of Object.entries(value as any)) {
                if (v === null) continue;
                if (typeof v === 'object') {
                    const processed = dfs(v);
                    if (processed !== undefined) res[k] = processed;
                } else {
                    if (Boolean(v)) res[k] = v;
                }
            }
            return res;
        }

        // primitive
        return Boolean(value) ? value : undefined;
    };

    const result = dfs(obj as any);
    return result as Obj;
}
```
