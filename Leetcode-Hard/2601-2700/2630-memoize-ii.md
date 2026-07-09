# 2630. Memoize II

## Javascript

```javascript
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const ROOT = new Map();
    const RESULT = Symbol('result');
    return function(...args) {
        let node = ROOT;
        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }
            node = node.get(arg);
        }
        if (node.has(RESULT)) {
            return node.get(RESULT);
        }
        const res = fn.apply(this, args);
        node.set(RESULT, res);
        return res;
    };
}
```

## Typescript

```typescript
type Fn = (...params: any[]) => any;

function memoize(fn: Fn): Fn {
    const RESULT = Symbol('result');
    const root = new Map<any, any>();

    return function (this: any, ...args: any[]): any {
        let node = root;
        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }
            node = node.get(arg);
        }
        if (node.has(RESULT)) {
            return node.get(RESULT);
        }
        const result = fn.apply(this, args);
        node.set(RESULT, result);
        return result;
    };
}
```
