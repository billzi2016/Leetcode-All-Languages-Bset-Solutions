# 2629. Function Composition

## Javascript

```javascript
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        let result = x;
        for (let i = functions.length - 1; i >= 0; --i) {
            result = functions[i](result);
        }
        return result;
    };
};
```

## Typescript

```typescript
type F = (x: number) => number;

function compose(functions: F[]): F {
    return function(x: number): number {
        let result = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            result = functions[i](result);
        }
        return result;
    };
}

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
```
