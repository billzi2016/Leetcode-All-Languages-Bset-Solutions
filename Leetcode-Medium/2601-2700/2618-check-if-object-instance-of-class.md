# 2618. Check if Object Instance of Class

## Javascript

```javascript
/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    // Validate inputs
    if (obj === null || obj === undefined) return false;
    if (typeof classFunction !== 'function' || classFunction.prototype === undefined) return false;

    // Wrap primitives to their object equivalents
    var current = Object(obj);

    // Traverse prototype chain
    while (true) {
        var proto = Object.getPrototypeOf(current);
        if (!proto) break;
        if (proto === classFunction.prototype) return true;
        current = proto;
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
```

## Typescript

```typescript
function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj == null || typeof classFunction !== 'function') return false;
    const targetProto = classFunction.prototype;
    if (targetProto === undefined) return false;

    let proto: any;
    if (typeof obj !== 'object' && typeof obj !== 'function') {
        // primitive value, wrap to get its prototype chain
        proto = Object.getPrototypeOf(Object(obj));
    } else {
        proto = Object.getPrototypeOf(obj);
    }

    while (proto) {
        if (proto === targetProto) return true;
        proto = Object.getPrototypeOf(proto);
    }
    return false;
}

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
```
