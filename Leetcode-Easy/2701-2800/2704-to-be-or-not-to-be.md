# 2704. To Be Or Not To Be

## Javascript

```javascript
/**
 * @param {*} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function (expected) {
            if (val === expected) {
                return true;
            }
            throw "Not Equal";
        },
        notToBe: function (unexpected) {
            if (val !== unexpected) {
                return true;
            }
            throw "Equal";
        }
    };
};
```

## Typescript

```typescript
type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (other: any) => {
            if (val === other) {
                return true;
            }
            throw "Not Equal";
        },
        notToBe: (other: any) => {
            if (val !== other) {
                return true;
            }
            throw "Equal";
        }
    };
}
```
