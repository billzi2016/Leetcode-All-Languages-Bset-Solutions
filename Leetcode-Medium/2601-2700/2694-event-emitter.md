# 2694. Event Emitter

## Javascript

```javascript
class EventEmitter {
    constructor() {
        this.events = Object.create(null);
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        const listeners = this.events[eventName];
        const entry = { callback };
        listeners.push(entry);

        return {
            unsubscribe: () => {
                const idx = listeners.indexOf(entry);
                if (idx !== -1) {
                    listeners.splice(idx, 1);
                }
            },
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const listeners = this.events[eventName];
        if (!listeners || listeners.length === 0) return [];

        // Use a shallow copy in case callbacks modify the list during iteration
        const snapshot = listeners.slice();
        const results = [];
        for (const { callback } of snapshot) {
            results.push(callback(...args));
        }
        return results;
    }
}
```

## Typescript

```typescript
type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
};

type Listener = {
    callback: Callback;
    active: boolean;
};

class EventEmitter {
    private events: Map<string, Listener[]> = new Map();

    subscribe(eventName: string, callback: Callback): Subscription {
        const listener: Listener = { callback, active: true };
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);
        }
        this.events.get(eventName)!.push(listener);

        return {
            unsubscribe: () => {
                // Mark inactive and remove from the list
                listener.active = false;
                const arr = this.events.get(eventName);
                if (arr) {
                    const idx = arr.indexOf(listener);
                    if (idx !== -1) {
                        arr.splice(idx, 1);
                    }
                    if (arr.length === 0) {
                        this.events.delete(eventName);
                    }
                }
            }
        };
    }

    emit(eventName: string, args: any[] = []): any[] {
        const listeners = this.events.get(eventName);
        if (!listeners) return [];
        const results: any[] = [];
        // Use a snapshot to avoid issues if callbacks modify subscriptions
        for (const listener of [...listeners]) {
            if (listener.active) {
                results.push(listener.callback(...args));
            }
        }
        return results;
    }
}
```
