# 2622. Cache With Time Limit

## Javascript

```javascript
var TimeLimitedCache = function() {
    this.cache = new Map(); // key -> {value, timeout}
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existed = this.cache.has(key);
    if (existed) {
        clearTimeout(this.cache.get(key).timeout);
    }
    const timeout = setTimeout(() => {
        this.cache.delete(key);
    }, duration);
    this.cache.set(key, { value, timeout });
    return existed;
};

TimeLimitedCache.prototype.get = function(key) {
    const entry = this.cache.get(key);
    return entry ? entry.value : -1;
};

TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};
```

## Typescript

```typescript
class TimeLimitedCache {
    private cache: Map<number, { value: number; timer: ReturnType<typeof setTimeout> }>;

    constructor() {
        this.cache = new Map();
    }

    set(key: number, value: number, duration: number): boolean {
        const existed = this.cache.has(key);
        if (existed) {
            clearTimeout(this.cache.get(key)!.timer);
        }
        const timer = setTimeout(() => {
            this.cache.delete(key);
        }, duration);
        this.cache.set(key, { value, timer });
        return existed;
    }

    get(key: number): number {
        const entry = this.cache.get(key);
        return entry ? entry.value : -1;
    }

    count(): number {
        return this.cache.size;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
```
