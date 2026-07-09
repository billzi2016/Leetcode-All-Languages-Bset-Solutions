# 2667. Create Hello World Function

## Javascript

```javascript
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
```

## Typescript

```typescript
function createHelloWorld() {
    return function (..._args: any[]): string {
        return "Hello World";
    };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
```
