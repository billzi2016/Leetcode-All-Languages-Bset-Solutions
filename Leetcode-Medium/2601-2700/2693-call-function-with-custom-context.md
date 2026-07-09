# 2693. Call Function with Custom Context

## Javascript

```javascript
/**
 * @param {Object} context
 * @param {...any} args
 * @return {*}
 */
Function.prototype.callPolyfill = function (context, ...args) {
    // Ensure the context is an object (wrap primitives)
    const ctx = Object(context);
    const fnKey = Symbol('fn');
    ctx[fnKey] = this;
    const result = ctx[fnKey](...args);
    delete ctx[fnKey];
    return result;
};
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

interface Function {
    callPolyfill(context: Record<string, JSONValue>, ...args: JSONValue[]): JSONValue;
}

Function.prototype.callPolyfill = function (context: Record<string, JSONValue>, ...args: JSONValue[]): JSONValue {
    const tempKey = Symbol();
    // @ts-ignore
    context[tempKey] = this;
    // @ts-ignore
    const result = context[tempKey](...args);
    delete (context as any)[tempKey];
    return result as JSONValue;
};

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
```
