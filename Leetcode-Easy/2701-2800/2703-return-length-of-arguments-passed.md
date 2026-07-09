# 2703. Return Length of Arguments Passed

## Javascript

```javascript
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
```

## Typescript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    return args.length;
}

/**
 * argumentsLength(1, 2, 3); // 3
 */
```
