# 1172. Dinner Plate Stacks

## Cpp

```cpp
class DinnerPlates {
public:
    DinnerPlates(int capacity) : cap(capacity) {}
    
    void push(int val) {
        // Find the leftmost stack with available space
        while (!avail.empty()) {
            int idx = avail.top();
            if (idx < (int)stacks.size() && (int)stacks[idx].size() < cap) break;
            avail.pop(); // stale entry
        }
        int idx;
        if (avail.empty()) {
            idx = stacks.size();
            stacks.emplace_back();
        } else {
            idx = avail.top();
            avail.pop();
        }
        stacks[idx].push_back(val);
        // This stack now has at least one plate
        nonempty.push(idx);
        // If it still has space, put back into avail
        if ((int)stacks[idx].size() < cap) {
            avail.push(idx);
        }
    }
    
    int pop() {
        while (!nonempty.empty()) {
            int idx = nonempty.top();
            if (idx < (int)stacks.size() && !stacks[idx].empty()) break;
            nonempty.pop(); // stale entry
        }
        if (nonempty.empty()) return -1;
        int idx = nonempty.top();
        int val = stacks[idx].back();
        stacks[idx].pop_back();
        // This stack now has space
        avail.push(idx);
        // If still not empty, keep it in nonempty heap for future pops
        if (!stacks[idx].empty()) {
            nonempty.push(idx);
        }
        // Trim trailing empty stacks to keep size minimal
        while (!stacks.empty() && stacks.back().empty()) {
            stacks.pop_back();
        }
        return val;
    }
    
    int popAtStack(int index) {
        if (index >= (int)stacks.size() || stacks[index].empty()) return -1;
        int val = stacks[index].back();
        stacks[index].pop_back();
        // This stack now has space
        avail.push(index);
        // If still not empty, keep it in nonempty heap
        if (!stacks[index].empty()) {
            nonempty.push(index);
        }
        // Trim trailing empty stacks
        while (!stacks.empty() && stacks.back().empty()) {
            stacks.pop_back();
        }
        return val;
    }

private:
    int cap;
    std::vector<std::vector<int>> stacks;
    std::priority_queue<int, std::vector<int>, std::greater<int>> avail; // min-heap for available space
    std::priority_queue<int> nonempty; // max-heap for non-empty stacks
};
```

## Java

```java
import java.util.*;

class DinnerPlates {
    private final int capacity;
    private final List<Deque<Integer>> stacks;
    private final TreeSet<Integer> nonEmpty; // indices with at least one plate
    private final TreeSet<Integer> hasSpace; // indices with size < capacity

    public DinnerPlates(int capacity) {
        this.capacity = capacity;
        this.stacks = new ArrayList<>();
        this.nonEmpty = new TreeSet<>();
        this.hasSpace = new TreeSet<>();
    }

    public void push(int val) {
        int idx;
        if (!hasSpace.isEmpty()) {
            idx = hasSpace.first();
        } else {
            idx = stacks.size();
            stacks.add(new ArrayDeque<>());
        }
        Deque<Integer> stack = stacks.get(idx);
        stack.push(val);

        // update structures
        nonEmpty.add(idx);
        if (stack.size() == capacity) {
            hasSpace.remove(idx);
        } else {
            hasSpace.add(idx);
        }
    }

    public int pop() {
        if (nonEmpty.isEmpty()) return -1;
        int idx = nonEmpty.last();
        Deque<Integer> stack = stacks.get(idx);
        int val = stack.pop();

        // update structures
        if (stack.isEmpty()) {
            nonEmpty.remove(idx);
        }
        hasSpace.add(idx); // now has space (including empty)

        return val;
    }

    public int popAtStack(int index) {
        if (index >= stacks.size()) return -1;
        Deque<Integer> stack = stacks.get(index);
        if (stack.isEmpty()) return -1;

        int val = stack.pop();

        // update structures
        if (stack.isEmpty()) {
            nonEmpty.remove(index);
        } else {
            nonEmpty.add(index); // still non-empty, ensure present
        }
        hasSpace.add(index); // now has space

        return val;
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = new DinnerPlates(capacity);
 * obj.push(val);
 * int param_2 = obj.pop();
 * int param_3 = obj.popAtStack(index);
 */
```

## Python

```python
import heapq

class DinnerPlates(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = []          # list of stacks (each a list)
        self.available = []       # min-heap of indices with free space
        self.nonempty = []        # max-heap (store -index) of non‑empty stacks

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Find leftmost stack that has room
        while self.available:
            idx = self.available[0]
            if idx < len(self.stacks) and len(self.stacks[idx]) < self.capacity:
                break
            heapq.heappop(self.available)   # stale entry
        if not self.available:
            idx = len(self.stacks)
            self.stacks.append([])
        else:
            idx = heapq.heappop(self.available)

        self.stacks[idx].append(val)

        # If still has room, put back into available heap
        if len(self.stacks[idx]) < self.capacity:
            heapq.heappush(self.available, idx)

        # Mark as non‑empty for pop()
        heapq.heappush(self.nonempty, -idx)

    def pop(self):
        """
        :rtype: int
        """
        while self.nonempty:
            idx = -self.nonempty[0]
            if idx < len(self.stacks) and self.stacks[idx]:
                break
            heapq.heappop(self.nonempty)   # stale entry
        if not self.nonempty:
            return -1

        idx = -heapq.heappop(self.nonempty)
        val = self.stacks[idx].pop()

        # If still non‑empty, keep it in the heap for future pops
        if self.stacks[idx]:
            heapq.heappush(self.nonempty, -idx)

        # This stack now has free space
        heapq.heappush(self.available, idx)

        # Remove trailing empty stacks to keep length minimal
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        # Stack now has free space
        heapq.heappush(self.available, index)

        if self.stacks[index]:
            heapq.heappush(self.nonempty, -index)

        # Clean up trailing empty stacks if needed
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val
```

## Python3

```python
import heapq

class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []               # list of lists
        self.available = []            # min-heap of indices with free space
        self.nonempty = []             # max-heap (store -index) of non‑empty stacks

    def push(self, val: int) -> None:
        # clean up unavailable entries
        while self.available:
            idx = self.available[0]
            if idx < len(self.stacks) and len(self.stacks[idx]) < self.capacity:
                break
            heapq.heappop(self.available)

        if not self.available:
            idx = len(self.stacks)
            self.stacks.append([])
        else:
            idx = heapq.heappop(self.available)

        self.stacks[idx].append(val)
        heapq.heappush(self.nonempty, -idx)

    def pop(self) -> int:
        # find rightmost non‑empty stack
        while self.nonempty:
            idx = -self.nonempty[0]
            if idx < len(self.stacks) and self.stacks[idx]:
                break
            heapq.heappop(self.nonempty)

        if not self.nonempty:
            return -1

        idx = -heapq.heappop(self.nonempty)
        val = self.stacks[idx].pop()

        # stack still has plates -> keep it in nonempty heap
        if self.stacks[idx]:
            heapq.heappush(self.nonempty, -idx)

        # now this index has free space
        heapq.heappush(self.available, idx)

        # trim trailing empty stacks to keep length accurate
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()
        heapq.heappush(self.available, index)

        if self.stacks[index]:
            heapq.heappush(self.nonempty, -index)
        else:
            # trim trailing empties if this was at the end
            while self.stacks and not self.stacks[-1]:
                self.stacks.pop()

        return val
```

## C

```c
typedef struct {
    int *data;
    int top; // current size
} Stack;

typedef struct {
    int capacity;

    Stack **stacks;
    int stacksSize;
    int stacksCap;

    int *minHeapArr;
    int minHeapSize;
    int minHeapCap;

    int *maxHeapArr;
    int maxHeapSize;
    int maxHeapCap;
} DinnerPlates;

/* ---------- heap utilities ---------- */
static void minHeapSwap(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}
static void maxHeapSwap(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}

/* ensure capacity for dynamic arrays */
static void ensureMinHeapCap(DinnerPlates *obj) {
    if (obj->minHeapSize < obj->minHeapCap) return;
    int newCap = obj->minHeapCap ? obj->minHeapCap * 2 : 4;
    obj->minHeapArr = realloc(obj->minHeapArr, newCap * sizeof(int));
    obj->minHeapCap = newCap;
}
static void ensureMaxHeapCap(DinnerPlates *obj) {
    if (obj->maxHeapSize < obj->maxHeapCap) return;
    int newCap = obj->maxHeapCap ? obj->maxHeapCap * 2 : 4;
    obj->maxHeapArr = realloc(obj->maxHeapArr, newCap * sizeof(int));
    obj->maxHeapCap = newCap;
}
static void ensureStacksCap(DinnerPlates *obj) {
    if (obj->stacksSize < obj->stacksCap) return;
    int newCap = obj->stacksCap ? obj->stacksCap * 2 : 4;
    obj->stacks = realloc(obj->stacks, newCap * sizeof(Stack*));
    obj->stacksCap = newCap;
}

/* min-heap push */
static void minHeapPush(DinnerPlates *obj, int val) {
    ensureMinHeapCap(obj);
    int i = obj->minHeapSize++;
    obj->minHeapArr[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (obj->minHeapArr[p] <= obj->minHeapArr[i]) break;
        minHeapSwap(&obj->minHeapArr[p], &obj->minHeapArr[i]);
        i = p;
    }
}

/* max-heap push */
static void maxHeapPush(DinnerPlates *obj, int val) {
    ensureMaxHeapCap(obj);
    int i = obj->maxHeapSize++;
    obj->maxHeapArr[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (obj->maxHeapArr[p] >= obj->maxHeapArr[i]) break;
        maxHeapSwap(&obj->maxHeapArr[p], &obj->maxHeapArr[i]);
        i = p;
    }
}

/* min-heap pop top */
static int minHeapPop(DinnerPlates *obj) {
    if (obj->minHeapSize == 0) return -1;
    int top = obj->minHeapArr[0];
    obj->minHeapArr[0] = obj->minHeapArr[--obj->minHeapSize];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, smallest = i;
        if (l < obj->minHeapSize && obj->minHeapArr[l] < obj->minHeapArr[smallest]) smallest = l;
        if (r < obj->minHeapSize && obj->minHeapArr[r] < obj->minHeapArr[smallest]) smallest = r;
        if (smallest == i) break;
        minHeapSwap(&obj->minHeapArr[i], &obj->minHeapArr[smallest]);
        i = smallest;
    }
    return top;
}

/* max-heap pop top */
static int maxHeapPop(DinnerPlates *obj) {
    if (obj->maxHeapSize == 0) return -1;
    int top = obj->maxHeapArr[0];
    obj->maxHeapArr[0] = obj->maxHeapArr[--obj->maxHeapSize];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, largest = i;
        if (l < obj->maxHeapSize && obj->maxHeapArr[l] > obj->maxHeapArr[largest]) largest = l;
        if (r < obj->maxHeapSize && obj->maxHeapArr[r] > obj->maxHeapArr[largest]) largest = r;
        if (largest == i) break;
        maxHeapSwap(&obj->maxHeapArr[i], &obj->maxHeapArr[largest]);
        i = largest;
    }
    return top;
}

/* peek functions */
static int minHeapPeek(DinnerPlates *obj) {
    if (obj->minHeapSize == 0) return -1;
    return obj->minHeapArr[0];
}
static int maxHeapPeek(DinnerPlates *obj) {
    if (obj->maxHeapSize == 0) return -1;
    return obj->maxHeapArr[0];
}

/* ---------- core operations ---------- */
DinnerPlates* dinnerPlatesCreate(int capacity) {
    DinnerPlates *obj = malloc(sizeof(DinnerPlates));
    obj->capacity = capacity;

    obj->stacks = NULL;
    obj->stacksSize = 0;
    obj->stacksCap = 0;

    obj->minHeapArr = NULL;
    obj->minHeapSize = 0;
    obj->minHeapCap = 0;

    obj->maxHeapArr = NULL;
    obj->maxHeapSize = 0;
    obj->maxHeapCap = 0;
    return obj;
}

static Stack* createStack(int capacity) {
    Stack *s = malloc(sizeof(Stack));
    s->data = malloc(capacity * sizeof(int));
    s->top = 0;
    return s;
}

/* clean up invalid entries on top of min-heap */
static void cleanMinHeap(DinnerPlates *obj) {
    while (obj->minHeapSize > 0) {
        int idx = minHeapPeek(obj);
        if (idx >= obj->stacksSize) { minHeapPop(obj); continue; }
        Stack *s = obj->stacks[idx];
        if (!s || s->top == obj->capacity) { minHeapPop(obj); continue; }
        break;
    }
}

/* clean up invalid entries on top of max-heap */
static void cleanMaxHeap(DinnerPlates *obj) {
    while (obj->maxHeapSize > 0) {
        int idx = maxHeapPeek(obj);
        if (idx >= obj->stacksSize) { maxHeapPop(obj); continue; }
        Stack *s = obj->stacks[idx];
        if (!s || s->top == 0) { maxHeapPop(obj); continue; }
        break;
    }
}

void dinnerPlatesPush(DinnerPlates* obj, int val) {
    cleanMinHeap(obj);
    int idx;
    if (obj->minHeapSize == 0) {
        /* need a new stack */
        idx = obj->stacksSize;
        ensureStacksCap(obj);
        obj->stacks[obj->stacksSize++] = createStack(obj->capacity);
    } else {
        idx = minHeapPeek(obj);
    }
    Stack *s = obj->stacks[idx];
    s->data[s->top++] = val;

    /* after push, if stack still not full, keep it in min-heap (duplicate ok) */
    if (s->top < obj->capacity) {
        minHeapPush(obj, idx);
    } else {
        /* now full; will be removed lazily */
    }
    maxHeapPush(obj, idx);
}

int dinnerPlatesPop(DinnerPlates* obj) {
    cleanMaxHeap(obj);
    if (obj->maxHeapSize == 0) return -1;
    int idx = maxHeapPeek(obj);
    Stack *s = obj->stacks[idx];
    int val = s->data[--s->top];

    /* after pop, this stack has space */
    minHeapPush(obj, idx);
    if (s->top > 0) {
        maxHeapPush(obj, idx); // still non‑empty; duplicate ok
    }
    return val;
}

int dinnerPlatesPopAtStack(DinnerPlates* obj, int index) {
    if (index < 0 || index >= obj->stacksSize) return -1;
    Stack *s = obj->stacks[index];
    if (!s || s->top == 0) return -1;
    int val = s->data[--s->top];

    minHeapPush(obj, index);
    if (s->top > 0) {
        maxHeapPush(obj, index);
    }
    return val;
}

void dinnerPlatesFree(DinnerPlates* obj) {
    for (int i = 0; i < obj->stacksSize; ++i) {
        if (obj->stacks[i]) {
            free(obj->stacks[i]->data);
            free(obj->stacks[i]);
        }
    }
    free(obj->stacks);
    free(obj->minHeapArr);
    free(obj->maxHeapArr);
    free(obj);
}

/**
 * Your DinnerPlates struct will be instantiated and called as such:
 * DinnerPlates* obj = dinnerPlatesCreate(capacity);
 * dinnerPlatesPush(obj, val);
 *
 * int param_2 = dinnerPlatesPop(obj);
 *
 * int param_3 = dinnerPlatesPopAtStack(obj, index);
 *
 * dinnerPlatesFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class DinnerPlates
{
    private readonly int _capacity;
    private readonly List<Stack<int>> _stacks;
    private readonly PriorityQueue<int, int> _minHeap; // indices with available space (min index)
    private readonly PriorityQueue<int, int> _maxHeap; // indices with plates (max index via negative priority)

    public DinnerPlates(int capacity)
    {
        _capacity = capacity;
        _stacks = new List<Stack<int>>();
        _minHeap = new PriorityQueue<int, int>();
        _maxHeap = new PriorityQueue<int, int>();
    }

    public void Push(int val)
    {
        // Clean up min-heap to find a valid stack with space
        while (_minHeap.Count > 0)
        {
            int idx = _minHeap.Peek();
            if (idx < _stacks.Count && _stacks[idx].Count < _capacity)
                break;
            _minHeap.Dequeue(); // discard invalid entry
        }

        int targetIdx;
        if (_minHeap.Count == 0)
        {
            // Need a new stack at the end
            targetIdx = _stacks.Count;
            var newStack = new Stack<int>();
            _stacks.Add(newStack);
        }
        else
        {
            targetIdx = _minHeap.Dequeue();
        }

        _stacks[targetIdx].Push(val);

        // This stack now has at least one plate
        _maxHeap.Enqueue(targetIdx, -targetIdx);

        // If it still has space, put back into min-heap
        if (_stacks[targetIdx].Count < _capacity)
        {
            _minHeap.Enqueue(targetIdx, targetIdx);
        }
    }

    public int Pop()
    {
        // Find rightmost non‑empty stack
        while (_maxHeap.Count > 0)
        {
            int idx = _maxHeap.Peek();
            if (idx < _stacks.Count && _stacks[idx].Count > 0)
                break;
            _maxHeap.Dequeue(); // discard invalid entry
        }

        if (_maxHeap.Count == 0)
            return -1;

        int targetIdx = _maxHeap.Dequeue();
        int val = _stacks[targetIdx].Pop();

        // This stack now has space
        _minHeap.Enqueue(targetIdx, targetIdx);

        // If still non‑empty, keep it in max-heap for future pops
        if (_stacks[targetIdx].Count > 0)
            _maxHeap.Enqueue(targetIdx, -targetIdx);

        return val;
    }

    public int PopAtStack(int index)
    {
        if (index >= _stacks.Count || _stacks[index].Count == 0)
            return -1;

        int val = _stacks[index].Pop();

        // Stack now has space
        _minHeap.Enqueue(index, index);

        // If still non‑empty, ensure it's represented in max-heap
        if (_stacks[index].Count > 0)
            _maxHeap.Enqueue(index, -index);

        return val;
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = new DinnerPlates(capacity);
 * obj.Push(val);
 * int param_2 = obj.Pop();
 * int param_3 = obj.PopAtStack(index);
 */
```

## Javascript

```javascript
/**
 * @param {number} capacity
 */
var DinnerPlates = function (capacity) {
    this.capacity = capacity;
    this.stacks = []; // array of arrays

    // Min-heap for indices with available space
    this.pushHeap = new Heap((a, b) => a < b);
    // Max-heap for indices that are non‑empty
    this.popHeap = new Heap((a, b) => a > b);
};

/** 
 * @param {number} val
 * @return {void}
 */
DinnerPlates.prototype.push = function (val) {
    // Clean up invalid entries in pushHeap
    while (
        this.pushHeap.size() > 0 &&
        (this.pushHeap.peek() >= this.stacks.length ||
            this.stacks[this.pushHeap.peek()].length >= this.capacity)
    ) {
        this.pushHeap.pop();
    }

    let idx;
    if (this.pushHeap.size() > 0) {
        // Use the leftmost stack with space
        idx = this.pushHeap.pop();
    } else {
        // Need a new stack at the end
        idx = this.stacks.length;
        this.stacks.push([]);
    }

    // Ensure the stack exists
    if (!this.stacks[idx]) this.stacks[idx] = [];

    this.stacks[idx].push(val);

    // If after push the stack still has space, put it back into pushHeap
    if (this.stacks[idx].length < this.capacity) {
        this.pushHeap.push(idx);
    }

    // This stack is now non‑empty, add to popHeap
    this.popHeap.push(idx);
};

/**
 * @return {number}
 */
DinnerPlates.prototype.pop = function () {
    // Clean up invalid entries in popHeap
    while (
        this.popHeap.size() > 0 &&
        (this.popHeap.peek() >= this.stacks.length ||
            this.stacks[this.popHeap.peek()].length === 0)
    ) {
        this.popHeap.pop();
    }

    if (this.popHeap.size() === 0) return -1;

    const idx = this.popHeap.peek();
    const val = this.stacks[idx].pop();

    // After pop, the stack has space again
    this.pushHeap.push(idx);

    // If it became empty, remove from popHeap lazily next call
    if (this.stacks[idx].length === 0) {
        this.popHeap.pop();
    }

    return val;
};

/** 
 * @param {number} index
 * @return {number}
 */
DinnerPlates.prototype.popAtStack = function (index) {
    if (
        index >= this.stacks.length ||
        !this.stacks[index] ||
        this.stacks[index].length === 0
    ) {
        return -1;
    }

    const val = this.stacks[index].pop();

    // Stack now has space
    this.pushHeap.push(index);

    // If still non‑empty, ensure it's in popHeap for future pops
    if (this.stacks[index].length > 0) {
        this.popHeap.push(index);
    }

    return val;
};

/**
 * Simple binary heap implementation with custom comparator.
 */
class Heap {
    /**
     * @param {(a:any,b:any)=>boolean} compare - returns true if a should be before b
     */
    constructor(compare) {
        this.data = [];
        this.compare = compare;
    }
    size() {
        return this.data.length;
    }
    peek() {
        return this.data[0];
    }
    push(value) {
        const a = this.data;
        a.push(value);
        let i = a.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.compare(a[i], a[p])) {
                [a[i], a[p]] = [a[p], a[i]];
                i = p;
            } else break;
        }
    }
    pop() {
        const a = this.data;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop();
        if (a.length > 0) {
            a[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1,
                    r = l + 1,
                    best = i;
                if (l < a.length && this.compare(a[l], a[best])) best = l;
                if (r < a.length && this.compare(a[r], a[best])) best = r;
                if (best !== i) {
                    [a[i], a[best]] = [a[best], a[i]];
                    i = best;
                } else break;
            }
        }
        return top;
    }
}

/** 
 * Your DinnerPlates object will be instantiated and called as such:
 * var obj = new DinnerPlates(capacity)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAtStack(index)
 */
```

## Typescript

```typescript
class MinHeap {
    private heap: number[] = [];
    push(val: number): void {
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1);
    }
    pop(): number | undefined {
        if (this.heap.length === 0) return undefined;
        const min = this.heap[0];
        const end = this.heap.pop()!;
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.bubbleDown(0);
        }
        return min;
    }
    peek(): number | undefined {
        return this.heap[0];
    }
    size(): number {
        return this.heap.length;
    }
    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this.heap[parent] <= this.heap[idx]) break;
            [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
            idx = parent;
        }
    }
    private bubbleDown(idx: number): void {
        const length = this.heap.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = idx * 2 + 2;
            let smallest = idx;
            if (left < length && this.heap[left] < this.heap[smallest]) smallest = left;
            if (right < length && this.heap[right] < this.heap[smallest]) smallest = right;
            if (smallest === idx) break;
            [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
            idx = smallest;
        }
    }
}

class DinnerPlates {
    private capacity: number;
    private stacks: number[][] = [];
    private available: MinHeap = new MinHeap(); // indices with space
    private rightmostNonEmpty: number = -1;

    constructor(capacity: number) {
        this.capacity = capacity;
    }

    push(val: number): void {
        // Clean up heap top if it points to a full stack or non‑existent
        while (this.available.size() > 0) {
            const idx = this.available.peek()!;
            if (idx < this.stacks.length && this.stacks[idx].length < this.capacity) break;
            this.available.pop();
        }

        let idx: number;
        if (this.available.size() === 0) {
            // need a new stack at the end
            idx = this.stacks.length;
            this.stacks.push([]);
        } else {
            idx = this.available.pop()!;
        }

        if (!this.stacks[idx]) this.stacks[idx] = [];
        this.stacks[idx].push(val);

        if (this.stacks[idx].length < this.capacity) {
            // still has space, put back into heap
            this.available.push(idx);
        }
        if (idx > this.rightmostNonEmpty) this.rightmostNonEmpty = idx;
    }

    pop(): number {
        while (this.rightmostNonEmpty >= 0 &&
               (this.rightmostNonEmpty >= this.stacks.length ||
                this.stacks[this.rightmostNonEmpty].length === 0)) {
            this.rightmostNonEmpty--;
        }
        if (this.rightmostNonEmpty < 0) return -1;

        const idx = this.rightmostNonEmpty;
        const val = this.stacks[idx].pop()!; // guaranteed non‑empty

        // After pop, if stack now has space, it becomes a candidate for future pushes
        if (this.stacks[idx].length === this.capacity - 1) {
            this.available.push(idx);
        }
        // If the stack became empty, rightmostNonEmpty will be adjusted in next call
        return val;
    }

    popAtStack(index: number): number {
        if (index >= this.stacks.length || !this.stacks[index] || this.stacks[index].length === 0) {
            return -1;
        }
        const val = this.stacks[index].pop()!;

        // If it was full before popping, now has space
        if (this.stacks[index].length === this.capacity - 1) {
            this.available.push(index);
        }

        // Adjust rightmostNonEmpty if needed
        if (index === this.rightmostNonEmpty && this.stacks[index].length === 0) {
            while (this.rightmostNonEmpty >= 0 &&
                   (this.rightmostNonEmpty >= this.stacks.length ||
                    this.stacks[this.rightmostNonEmpty].length === 0)) {
                this.rightmostNonEmpty--;
            }
        }

        return val;
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * var obj = new DinnerPlates(capacity)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAtStack(index)
 */
```

## Php

```php
class DinnerPlates {
    private $capacity;
    private $stacks = [];
    private $minHeap;
    private $maxHeap;

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
        $this->minHeap = new SplMinHeap(); // indices with available space
        $this->maxHeap = new SplMaxHeap(); // indices with at least one plate
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        while (true) {
            if ($this->minHeap->isEmpty()) {
                $idx = count($this->stacks);
                break;
            }
            $idx = $this->minHeap->extract();
            if (!isset($this->stacks[$idx])) {
                $this->stacks[$idx] = [];
            }
            if (count($this->stacks[$idx]) < $this->capacity) {
                break;
            }
            // stale entry, continue
        }

        // ensure stack exists
        if (!isset($this->stacks[$idx])) {
            $this->stacks[$idx] = [];
        }

        $this->stacks[$idx][] = $val;

        // if it was empty before push, now non-empty -> add to maxHeap
        if (count($this->stacks[$idx]) == 1) {
            $this->maxHeap->insert($idx);
        }

        // if still has space after push, keep index in minHeap for future pushes
        if (count($this->stacks[$idx]) < $this->capacity) {
            $this->minHeap->insert($idx);
        }
    }

    /**
     * @return Integer
     */
    function pop() {
        while (!$this->maxHeap->isEmpty()) {
            $idx = $this->maxHeap->extract();
            if (isset($this->stacks[$idx]) && !empty($this->stacks[$idx])) {
                $val = array_pop($this->stacks[$idx]);

                // after pop, this stack now has space
                $this->minHeap->insert($idx);

                // if still non-empty, re-insert into maxHeap
                if (!empty($this->stacks[$idx])) {
                    $this->maxHeap->insert($idx);
                }
                return $val;
            }
            // stale entry, continue
        }
        return -1;
    }

    /**
     * @param Integer $index
     * @return Integer
     */
    function popAtStack($index) {
        if (!isset($this->stacks[$index]) || empty($this->stacks[$index])) {
            return -1;
        }
        $val = array_pop($this->stacks[$index]);

        // this stack now has space
        $this->minHeap->insert($index);

        // if still non-empty, keep it in maxHeap for future pops
        if (!empty($this->stacks[$index])) {
            $this->maxHeap->insert($index);
        }
        return $val;
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * $obj = new DinnerPlates($capacity);
 * $obj->push($val);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->popAtStack($index);
 */
```

## Swift

```swift
class Heap {
    private var elements: [Int] = []
    private let priorityFunction: (Int, Int) -> Bool
    
    init(_ priorityFunction: @escaping (Int, Int) -> Bool) {
        self.priorityFunction = priorityFunction
    }
    
    func peek() -> Int? {
        return elements.first
    }
    
    func push(_ value: Int) {
        elements.append(value)
        siftUp(elements.count - 1)
    }
    
    func pop() -> Int? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        }
        let top = elements[0]
        elements[0] = elements.removeLast()
        siftDown(0)
        return top
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && priorityFunction(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { break }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class DinnerPlates {
    private let capacity: Int
    private var stacks: [[Int]] = []
    private var minHeap: Heap   // indices with available space (not full)
    private var maxHeap: Heap   // indices that are non‑empty
    
    init(_ capacity: Int) {
        self.capacity = capacity
        self.minHeap = Heap { $0 < $1 }   // min‑heap
        self.maxHeap = Heap { $0 > $1 }   // max‑heap
    }
    
    func push(_ val: Int) {
        // Clean up stale entries in minHeap
        while let idx = minHeap.peek() {
            if idx >= stacks.count || stacks[idx].count == capacity {
                _ = minHeap.pop()
            } else {
                break
            }
        }
        
        var index: Int
        if let idx = minHeap.peek() {
            index = idx
            _ = minHeap.pop()
        } else {
            index = stacks.count
            stacks.append([])
        }
        
        stacks[index].append(val)
        
        // If still has space, put back into minHeap
        if stacks[index].count < capacity {
            minHeap.push(index)
        }
        // Stack is now non‑empty
        maxHeap.push(index)
    }
    
    func pop() -> Int {
        // Clean up stale entries in maxHeap
        while let idx = maxHeap.peek() {
            if idx >= stacks.count || stacks[idx].isEmpty {
                _ = maxHeap.pop()
            } else {
                break
            }
        }
        
        guard let idx = maxHeap.pop() else { return -1 }
        let val = stacks[idx].removeLast()
        
        // If still non‑empty, keep it in maxHeap
        if !stacks[idx].isEmpty {
            maxHeap.push(idx)
        }
        // It now has space
        if stacks[idx].count < capacity {
            minHeap.push(idx)
        }
        return val
    }
    
    func popAtStack(_ index: Int) -> Int {
        if index >= stacks.count || stacks[index].isEmpty {
            return -1
        }
        let val = stacks[index].removeLast()
        
        // After removal, this stack has space
        if stacks[index].count < capacity {
            minHeap.push(index)
        }
        // If still non‑empty, ensure it's in maxHeap
        if !stacks[index].isEmpty {
            maxHeap.push(index)
        }
        return val
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * let obj = DinnerPlates(capacity)
 * obj.push(val)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.popAtStack(index)
 */
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class DinnerPlates(capacity: Int) {
    private val cap = capacity
    private val stacks = mutableListOf<MutableList<Int>>()
    private val pushHeap = PriorityQueue<Int>() // min-heap of indices with available space
    private val popHeap = PriorityQueue<Int>(compareByDescending { it }) // max-heap of non‑empty stack indices

    fun push(`val`: Int) {
        // Remove stale entries where the stack is already full
        while (true) {
            val idx = pushHeap.peek() ?: break
            if (idx < stacks.size && stacks[idx].size >= cap) {
                pushHeap.poll()
            } else {
                break
            }
        }

        if (pushHeap.isEmpty()) {
            // Need a new stack at the end
            val idx = stacks.size
            val newStack = mutableListOf<Int>()
            newStack.add(`val`)
            stacks.add(newStack)
            if (newStack.size < cap) pushHeap.offer(idx)
            popHeap.offer(idx)
        } else {
            val idx = pushHeap.peek()!!
            val stack = stacks[idx]
            stack.add(`val`)
            if (stack.size == cap) {
                // Now full, remove from available heap
                pushHeap.poll()
            }
            popHeap.offer(idx)
        }
    }

    fun pop(): Int {
        while (true) {
            val idx = popHeap.peek() ?: return -1
            if (idx >= stacks.size) {
                popHeap.poll()
                continue
            }
            val stack = stacks[idx]
            if (stack.isEmpty()) {
                popHeap.poll()
                continue
            }
            // Pop from the rightmost non‑empty stack
            val value = stack.removeAt(stack.lastIndex)
            if (stack.size == cap - 1) {
                pushHeap.offer(idx)
            }
            return value
        }
    }

    fun popAtStack(index: Int): Int {
        if (index >= stacks.size) return -1
        val stack = stacks[index]
        if (stack.isEmpty()) return -1
        val value = stack.removeAt(stack.lastIndex)
        if (stack.size == cap - 1) {
            pushHeap.offer(index)
        }
        return value
    }
}
```

## Dart

```dart
class PriorityQueue {
  final List<int> _heap = [];
  final bool Function(int a, int b) _comp; // true if a has higher priority than b

  PriorityQueue(this._comp);

  bool get isEmpty => _heap.isEmpty;

  void push(int x) {
    _heap.add(x);
    _siftUp(_heap.length - 1);
  }

  int peek() => _heap[0];

  int pop() {
    final int res = _heap[0];
    final int last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return res;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final int parent = (idx - 1) >> 1;
      if (_comp(_heap[idx], _heap[parent])) {
        final int tmp = _heap[idx];
        _heap[idx] = _heap[parent];
        _heap[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    final int n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int best = idx;
      if (left < n && _comp(_heap[left], _heap[best])) best = left;
      if (right < n && _comp(_heap[right], _heap[best])) best = right;
      if (best != idx) {
        final int tmp = _heap[idx];
        _heap[idx] = _heap[best];
        _heap[best] = tmp;
        idx = best;
      } else {
        break;
      }
    }
  }
}

class DinnerPlates {
  final int capacity;
  final List<List<int>> _stacks = [];
  final PriorityQueue _leftHeap;   // min-heap for indices with available space
  final PriorityQueue _rightHeap;  // max-heap for indices with plates

  DinnerPlates(this.capacity)
      : _leftHeap = PriorityQueue((a, b) => a < b),
        _rightHeap = PriorityQueue((a, b) => a > b);

  void push(int val) {
    // Find the leftmost stack that is not full.
    while (!_leftHeap.isEmpty) {
      final int idx = _leftHeap.peek();
      if (idx < _stacks.length && _stacks[idx].length < capacity) break;
      _leftHeap.pop(); // discard invalid entry
    }

    int idx;
    if (_leftHeap.isEmpty) {
      idx = _stacks.length;
      _stacks.add([]);
    } else {
      idx = _leftHeap.pop();
    }

    // Ensure the stack exists.
    while (idx >= _stacks.length) {
      _stacks.add([]);
    }

    _stacks[idx].add(val);

    // If after pushing the stack is still not full, keep it in left heap.
    if (_stacks[idx].length < capacity) {
      _leftHeap.push(idx);
    }

    // This stack now has at least one plate.
    _rightHeap.push(idx);
  }

  int pop() {
    while (!_rightHeap.isEmpty) {
      final int idx = _rightHeap.peek();
      if (idx < _stacks.length && _stacks[idx].isNotEmpty) break;
      _rightHeap.pop(); // discard invalid entry
    }

    if (_rightHeap.isEmpty) return -1;

    final int idx = _rightHeap.pop();
    final int val = _stacks[idx].removeLast();

    // If the stack still has plates, keep it in right heap.
    if (_stacks[idx].isNotEmpty) {
      _rightHeap.push(idx);
    }

    // It now has free space.
    _leftHeap.push(idx);
    return val;
  }

  int popAtStack(int index) {
    if (index >= _stacks.length || _stacks[index].isEmpty) return -1;

    final int val = _stacks[index].removeLast();

    // After removal, this stack has free space.
    _leftHeap.push(index);

    // If it still contains plates, ensure it's reachable for future pops.
    if (_stacks[index].isNotEmpty) {
      _rightHeap.push(index);
    }

    return val;
  }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = DinnerPlates(capacity);
 * obj.push(val);
 * int param2 = obj.pop();
 * int param3 = obj.popAtStack(index);
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // larger first
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type DinnerPlates struct {
	capacity int
	stacks   [][]int
	minIdx   MinHeap // leftmost stack with space
	maxIdx   MaxHeap // rightmost non‑empty stack
}

/** Initialize your data structure here. */
func Constructor(capacity int) DinnerPlates {
	dp := DinnerPlates{
		capacity: capacity,
	}
	heap.Init(&dp.minIdx)
	heap.Init(&dp.maxIdx)
	return dp
}

func (this *DinnerPlates) Push(val int) {
	for {
		if this.minIdx.Len() == 0 {
			idx := len(this.stacks)
			this.stacks = append(this.stacks, []int{})
			this.stacks[idx] = append(this.stacks[idx], val)
			if len(this.stacks[idx]) < this.capacity {
				heap.Push(&this.minIdx, idx)
			}
			heap.Push(&this.maxIdx, idx)
			return
		}
		idx := heap.Pop(&this.minIdx).(int)
		if idx < len(this.stacks) && len(this.stacks[idx]) < this.capacity {
			this.stacks[idx] = append(this.stacks[idx], val)
			if len(this.stacks[idx]) < this.capacity {
				heap.Push(&this.minIdx, idx)
			}
			heap.Push(&this.maxIdx, idx)
			return
		}
		// otherwise discard and continue
	}
}

func (this *DinnerPlates) Pop() int {
	for this.maxIdx.Len() > 0 {
		idx := heap.Pop(&this.maxIdx).(int)
		if idx < len(this.stacks) && len(this.stacks[idx]) > 0 {
			n := len(this.stacks[idx])
			val := this.stacks[idx][n-1]
			this.stacks[idx] = this.stacks[idx][:n-1]

			if len(this.stacks[idx]) > 0 {
				heap.Push(&this.maxIdx, idx)
			}
			if len(this.stacks[idx]) < this.capacity {
				heap.Push(&this.minIdx, idx)
			}
			return val
		}
	}
	return -1
}

func (this *DinnerPlates) PopAtStack(index int) int {
	if index >= len(this.stacks) || len(this.stacks[index]) == 0 {
		return -1
	}
	n := len(this.stacks[index])
	val := this.stacks[index][n-1]
	this.stacks[index] = this.stacks[index][:n-1]

	if len(this.stacks[index]) > 0 {
		heap.Push(&this.maxIdx, index)
	}
	if len(this.stacks[index]) < this.capacity {
		heap.Push(&this.minIdx, index)
	}
	return val
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * obj.Push(val);
 * param_2 := obj.Pop();
 * param_3 := obj.PopAtStack(index);
 */
```

## Ruby

```ruby
class MinHeap
  def initialize
    @data = []
  end

  def push(x)
    i = @data.size
    @data << x
    while i > 0
      p = (i - 1) / 2
      break if @data[p] <= @data[i]
      @data[p], @data[i] = @data[i], @data[p]
      i = p
    end
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      i = 0
      size = @data.size
      loop do
        l = i * 2 + 1
        r = i * 2 + 2
        smallest = i
        smallest = l if l < size && @data[l] < @data[smallest]
        smallest = r if r < size && @data[r] < @data[smallest]
        break if smallest == i
        @data[i], @data[smallest] = @data[smallest], @data[i]
        i = smallest
      end
    end
    top
  end

  def peek
    @data[0]
  end

  def empty?
    @data.empty?
  end
end

class DinnerPlates
  # :type capacity: Integer
  def initialize(capacity)
    @capacity = capacity
    @stacks = []
    @available = MinHeap.new          # indices with space (< capacity)
    @nonempty = MinHeap.new           # store negative indices for max-heap behavior
  end

  # :type val: Integer
  # :rtype: Void
  def push(val)
    # Find leftmost stack that has room
    while !@available.empty?
      idx = @available.peek
      if idx < @stacks.size && @stacks[idx].size < @capacity
        break
      else
        @available.pop
      end
    end

    if @available.empty?
      idx = @stacks.size
      @stacks << []
    else
      idx = @available.peek
      @available.pop
    end

    @stacks[idx] << val

    # If still not full, it remains available
    @available.push(idx) if @stacks[idx].size < @capacity

    # Mark as non‑empty for pop()
    @nonempty.push(-idx)
  end

  # :rtype: Integer
  def pop()
    # Find rightmost non‑empty stack
    while !@nonempty.empty?
      idx = -@nonempty.peek
      if idx < @stacks.size && !@stacks[idx].empty?
        break
      else
        @nonempty.pop
      end
    end

    return -1 if @nonempty.empty?

    idx = -@nonempty.peek
    val = @stacks[idx].pop

    # After popping, this stack may have space again
    @available.push(idx) if @stacks[idx].size < @capacity

    val
  end

  # :type index: Integer
  # :rtype: Integer
  def pop_at_stack(index)
    return -1 if index >= @stacks.size || @stacks[index].nil? || @stacks[index].empty?
    val = @stacks[index].pop
    @available.push(index) if @stacks[index].size < @capacity
    # No need to update nonempty heap; stale entries are cleaned lazily
    val
  end
end
```

## Scala

```scala
import java.util.{PriorityQueue, Collections}
import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

class DinnerPlates(_capacity: Int) {

  private val capacity = _capacity
  private val stacks = ArrayBuffer.empty[ArrayDeque[Int]]

  // min-heap for leftmost stack that is not full
  private val pushHeap = new PriorityQueue[Int]()
  // max-heap for rightmost non‑empty stack
  private val popHeap = new PriorityQueue[Int](Collections.reverseOrder[Int]())

  def push(`val`: Int): Unit = {
    var idx = -1
    while (pushHeap.nonEmpty) {
      val cand = pushHeap.peek()
      if (cand < stacks.size && stacks(cand).size < capacity) {
        idx = cand
        // keep it for later use, will poll after confirming
        // but we need to remove it now to avoid duplicate stale entries later
        pushHeap.poll()
        // break loop with valid idx
        break
      } else {
        pushHeap.poll() // discard stale index
      }
    }

    if (idx == -1) {
      // no existing non‑full stack, create a new one at the end
      idx = stacks.size
      stacks.append(ArrayDeque.empty[Int])
    }

    val st = stacks(idx)
    st.append(`val`)

    // after push, if still not full, make it available for future pushes
    if (st.size < capacity) {
      pushHeap.offer(idx)
    }
    // stack is now non‑empty, ensure it's in pop heap
    popHeap.offer(idx)
  }

  def pop(): Int = {
    while (popHeap.nonEmpty) {
      val idx = popHeap.peek()
      if (idx < stacks.size && stacks(idx).nonEmpty) {
        val st = stacks(idx)
        val res = st.removeLast()
        // after removal, if stack becomes non‑full, add to push heap
        if (st.size < capacity) {
          pushHeap.offer(idx)
        }
        // if still non‑empty, keep it in pop heap for future pops
        if (st.nonEmpty) {
          popHeap.offer(idx)
        }
        popHeap.poll() // remove the used entry
        return res
      } else {
        popHeap.poll()
      }
    }
    -1
  }

  def popAtStack(index: Int): Int = {
    if (index >= stacks.size) return -1
    val st = stacks(index)
    if (st.isEmpty) return -1
    val res = st.removeLast()
    // after removal, stack may become non‑full
    if (st.size < capacity) {
      pushHeap.offer(index)
    }
    // if still non‑empty, keep it in pop heap
    if (st.nonEmpty) {
      popHeap.offer(index)
    }
    res
  }

  // Helper to break out of while loop when needed
  private def break = throw new RuntimeException("break")
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct DinnerPlates {
    capacity: usize,
    stacks: Vec<Vec<i32>>,
    push_heap: BinaryHeap<Reverse<usize>>, // min-heap of indices with available space
    pop_heap: BinaryHeap<usize>,           // max-heap of non‑empty stack indices
}

impl DinnerPlates {
    fn new(capacity: i32) -> Self {
        DinnerPlates {
            capacity: capacity as usize,
            stacks: Vec::new(),
            push_heap: BinaryHeap::new(),
            pop_heap: BinaryHeap::new(),
        }
    }

    fn clean_push_heap(&mut self) {
        while let Some(&Reverse(idx)) = self.push_heap.peek() {
            if idx < self.stacks.len() && self.stacks[idx].len() < self.capacity {
                break;
            }
            self.push_heap.pop();
        }
    }

    fn clean_pop_heap(&mut self) {
        while let Some(&idx) = self.pop_heap.peek() {
            if idx < self.stacks.len() && !self.stacks[idx].is_empty() {
                break;
            }
            self.pop_heap.pop();
        }
    }

    fn push(&mut self, val: i32) {
        self.clean_push_heap();

        let idx = if let Some(Reverse(i)) = self.push_heap.pop() {
            i
        } else {
            let i = self.stacks.len();
            self.stacks.push(Vec::new());
            i
        };

        if idx >= self.stacks.len() {
            self.stacks.resize(idx + 1, Vec::new());
        }

        self.stacks[idx].push(val);

        if self.stacks[idx].len() < self.capacity {
            self.push_heap.push(Reverse(idx));
        }
        self.pop_heap.push(idx);
    }

    fn pop(&mut self) -> i32 {
        self.clean_pop_heap();

        if let Some(idx) = self.pop_heap.pop() {
            let val = self.stacks[idx].pop().unwrap();

            if !self.stacks[idx].is_empty() {
                self.pop_heap.push(idx);
            }
            self.push_heap.push(Reverse(idx));

            while let Some(last) = self.stacks.last() {
                if last.is_empty() {
                    self.stacks.pop();
                } else {
                    break;
                }
            }

            val
        } else {
            -1
        }
    }

    fn pop_at_stack(&mut self, index: i32) -> i32 {
        let idx = index as usize;
        if idx >= self.stacks.len() || self.stacks[idx].is_empty() {
            return -1;
        }

        let val = self.stacks[idx].pop().unwrap();
        self.push_heap.push(Reverse(idx));

        if !self.stacks[idx].is_empty() {
            self.pop_heap.push(idx);
        }

        while let Some(last) = self.stacks.last() {
            if last.is_empty() {
                self.stacks.pop();
            } else {
                break;
            }
        }

        val
    }
}

/*
Your DinnerPlates object will be instantiated and called as such:
let mut obj = DinnerPlates::new(capacity);
obj.push(val);
let ret_2 = obj.pop();
let ret_3 = obj.pop_at_stack(index);
*/
```

## Racket

```racket
(require racket/heap)

(struct stack (vec size) #:mutable)

(define dinner-plates%
  (class object%
    (super-new)
    
    ; capacity : exact-integer?
    (init-field
      capacity)
    
    ; internal state
    (define stacks (make-hash))          ; index -> stack struct
    (define avail (make-heap <))         ; min‑heap of indices with free space
    (define nonempty (make-heap >))      ; max‑heap of indices that are non‑empty
    (define max-index -1)                ; highest index created so far
    
    ;; get existing stack or create a new one at index i
    (define (get-or-create i)
      (hash-ref stacks i
                (lambda ()
                  (define s (stack (make-vector capacity) 0))
                  (hash-set! stacks i s)
                  s)))
    
    ;; push : exact-integer? -> void?
    (define/public (push val)
      (let loop ()
        (if (heap-empty? avail)
            ; no existing stack with space → create a new one
            (begin
              (set! max-index (+ max-index 1))
              (define i max-index)
              (define s (get-or-create i))
              (vector-set! (stack-vec s) (stack-size s) val)
              (set-stack-size! s (+ (stack-size s) 1))
              ; if still not full, it remains a candidate for future pushes
              (when (< (stack-size s) capacity)
                (heap-add! avail i))
              (heap-add! nonempty i))
            ; there is at least one index with potential space
            (let* ([i (heap-min avail)]
                   [s (hash-ref stacks i #f)])
              (cond
                [(and s (< (stack-size s) capacity))
                 ; use this stack
                 (heap-remove-min! avail)
                 (vector-set! (stack-vec s) (stack-size s) val)
                 (set-stack-size! s (+ (stack-size s) 1))
                 (when (< (stack-size s) capacity)
                   (heap-add! avail i))   ; still has room
                 (heap-add! nonempty i)]
                [else
                 ; stale entry – remove and continue searching
                 (heap-remove-min! avail)
                 (loop)]))))))

    ;; pop : -> exact-integer?
    (define/public (pop)
      (let loop ()
        (if (heap-empty? nonempty)
            -1
            (let* ([i (heap-min nonempty)]
                   [s (hash-ref stacks i #f)])
              (cond
                [(or (not s) (= (stack-size s) 0))
                 (heap-remove-min! nonempty)
                 (loop)]
                [else
                 (define val (vector-ref (stack-vec s) (- (stack-size s) 1)))
                 (set-stack-size! s (- (stack-size s) 1))
                 ; if it now has a free slot, make it available for pushes
                 (when (= (stack-size s) (- capacity 1))
                   (heap-add! avail i))
                 val])))))

    ;; pop-at-stack : exact-integer? -> exact-integer?
    (define/public (pop-at-stack index)
      (let ([s (hash-ref stacks index #f)])
        (if (or (not s) (= (stack-size s) 0))
            -1
            (begin
              (define val (vector-ref (stack-vec s) (- (stack-size s) 1)))
              (set-stack-size! s (- (stack-size s) 1))
              ; if it now has a free slot, add to avail heap
              (when (= (stack-size s) (- capacity 1))
                (heap-add! avail index))
              val))))))
```

## Erlang

```erlang
-module(dinnerplates).
-export([dinner_plates_init_/1,
         dinner_plates_push/1,
         dinner_plates_pop/0,
         dinner_plates_pop_at_stack/1]).

%% Initialization
-spec dinner_plates_init_(Capacity :: integer()) -> any().
dinner_plates_init_(Capacity) ->
    put(capacity, Capacity),
    put(stacks, #{}),
    put(left, gb_sets:new()),
    put(right, gb_sets:new()),
    put(next, 0).

%% Push operation
-spec dinner_plates_push(Val :: integer()) -> any().
dinner_plates_push(Val) ->
    Capacity = get(capacity),
    Stacks   = get(stacks),
    LeftSet  = get(left),
    RightSet = get(right),
    NextIdx  = get(next),

    {IdxOpt, CleanLeft} = find_left(Capacity, Stacks, LeftSet),

    case IdxOpt of
        undefined ->
            %% create a new stack at NextIdx
            NewStacks   = maps:put(NextIdx, {1, [Val]}, Stacks),
            NewRight    = gb_sets:add(-NextIdx, RightSet),
            NewLeft     = if Capacity > 1 -> gb_sets:add(NextIdx, CleanLeft);
                           true          -> CleanLeft
                        end,
            put(stacks, NewStacks),
            put(right, NewRight),
            put(left, NewLeft),
            put(next, NextIdx + 1);
        Idx ->
            {Size, List} = maps:get(Idx, Stacks),
            NewSize      = Size + 1,
            NewList      = [Val | List],
            UpdatedStacks= maps:put(Idx, {NewSize, NewList}, Stacks),

            UpdatedLeft = if NewSize == Capacity -> gb_sets:delete(Idx, CleanLeft);
                             true               -> CleanLeft
                          end,
            UpdatedRight = gb_sets:add(-Idx, RightSet),

            put(stacks, UpdatedStacks),
            put(left, UpdatedLeft),
            put(right, UpdatedRight)
    end.

%% Pop operation (rightmost non‑empty stack)
-spec dinner_plates_pop() -> integer().
dinner_plates_pop() ->
    Stacks   = get(stacks),
    RightSet = get(right),

    case find_right(Stacks, RightSet) of
        {undefined, _} ->
            -1;
        {Idx, CleanRight} ->
            {Size, List} = maps:get(Idx, Stacks),
            [Val | Rest] = List,
            NewSize      = Size - 1,

            NewStacks = if NewSize == 0 -> maps:remove(Idx, Stacks);
                           true       -> maps:put(Idx, {NewSize, Rest}, Stacks)
                        end,

            UpdatedLeft  = gb_sets:add(Idx, get(left)),
            UpdatedRight = case NewSize of
                               0 -> CleanRight;               % stack became empty, do not re‑add
                               _ -> gb_sets:add(-Idx, CleanRight) % still non‑empty
                           end,

            put(stacks, NewStacks),
            put(left, UpdatedLeft),
            put(right, UpdatedRight),

            Val
    end.

%% Pop at a specific stack index
-spec dinner_plates_pop_at_stack(Index :: integer()) -> integer().
dinner_plates_pop_at_stack(Index) ->
    Stacks = get(stacks),
    case maps:get(Index, Stacks, {0, []}) of
        {0, _} ->
            -1;
        {Size, List} ->
            [Val | Rest] = List,
            NewSize = Size - 1,

            NewStacks = if NewSize == 0 -> maps:remove(Index, Stacks);
                           true       -> maps:put(Index, {NewSize, Rest}, Stacks)
                        end,

            %% left set always gets the index because it now has free space
            UpdatedLeft = gb_sets:add(Index, get(left)),

            %% right set should contain the index only if still non‑empty
            RightSet    = get(right),
            UpdatedRight = case NewSize of
                               0 -> gb_sets:delete(-Index, RightSet);
                               _ -> gb_sets:add(-Index, RightSet)
                           end,

            put(stacks, NewStacks),
            put(left, UpdatedLeft),
            put(right, UpdatedRight),

            Val
    end.

%% Helper: find the leftmost stack that is not full
find_left(_Capacity, _Stacks, LeftSet) when gb_sets:is_empty(LeftSet) ->
    {undefined, LeftSet};
find_left(Capacity, Stacks, LeftSet) ->
    {Idx, _} = gb_sets:smallest(LeftSet),
    case maps:get(Idx, Stacks, {0, []}) of
        {Size, _} when Size < Capacity ->
            {Idx, LeftSet};
        _ ->
            NewLeft = gb_sets:delete(Idx, LeftSet),
            find_left(Capacity, Stacks, NewLeft)
    end.

%% Helper: find the rightmost non‑empty stack
find_right(_Stacks, RightSet) when gb_sets:is_empty(RightSet) ->
    {undefined, RightSet};
find_right(Stacks, RightSet) ->
    {NegIdx, _} = gb_sets:smallest(RightSet),
    Idx = -NegIdx,
    case maps:get(Idx, Stacks, {0, []}) of
        {Size, _} when Size > 0 ->
            NewRight = gb_sets:delete(NegIdx, RightSet),
            {Idx, NewRight};
        _ ->
            NewRight = gb_sets:delete(NegIdx, RightSet),
            find_right(Stacks, NewRight)
    end.
```

## Elixir

```elixir
defmodule DinnerPlates do
  @spec init_(capacity :: integer) :: any
  def init_(capacity) do
    state = %{
      cap: capacity,
      stacks: %{},                     # idx => {list, size}
      avail: :gb_trees.empty(),       # indices with space (< cap)
      max_idx: -1
    }

    Process.put({__MODULE__, :state}, state)
    nil
  end

  @spec push(val :: integer) :: any
  def push(val) do
    state = Process.get({__MODULE__, :state})
    {idx, avail_tree} =
      if :gb_trees.is_empty(state.avail) do
        {state.max_idx + 1, state.avail}
      else
        {{i, _}, _} = :gb_trees.smallest(state.avail)
        {i, state.avail}
      end

    {list, size} = Map.get(state.stacks, idx, {[], 0})
    new_stack = {[val | list], size + 1}
    new_stacks = Map.put(state.stacks, idx, new_stack)

    # update avail tree
    new_avail =
      cond do
        new_stack |> elem(1) == state.cap ->
          case :gb_trees.lookup(idx, state.avail) do
            {:value, _} -> :gb_trees.delete_any(idx, state.avail)
            :none -> state.avail
          end

        true ->
          case :gb_trees.lookup(idx, state.avail) do
            {:value, _} -> state.avail
            :none -> :gb_trees.enter(idx, true, state.avail)
          end
      end

    new_max = if idx > state.max_idx, do: idx, else: state.max_idx

    Process.put({__MODULE__, :state}, %{state | stacks: new_stacks, avail: new_avail, max_idx: new_max})
    nil
  end

  @spec pop() :: integer
  def pop() do
    state = Process.get({__MODULE__, :state})
    {value, new_state} = pop_from(state.max_idx, state)
    Process.put({__MODULE__, :state}, new_state)
    value
  end

  @spec pop_at_stack(index :: integer) :: integer
  def pop_at_stack(index) do
    state = Process.get({__MODULE__, :state})
    case Map.get(state.stacks, index) do
      nil ->
        -1

      {[], _} ->
        -1

      {[top | rest], size} ->
        new_size = size - 1
        new_stacks =
          if new_size == 0 do
            Map.delete(state.stacks, index)
          else
            Map.put(state.stacks, index, {rest, new_size})
          end

        # ensure index is in avail (has space now)
        new_avail =
          case :gb_trees.lookup(index, state.avail) do
            {:value, _} -> state.avail
            :none -> :gb_trees.enter(index, true, state.avail)
          end

        # adjust max_idx if needed
        new_max =
          if index == state.max_idx and new_size == 0 do
            find_new_max(state.max_idx - 1, new_stacks)
          else
            state.max_idx
          end

        Process.put({__MODULE__, :state}, %{state | stacks: new_stacks, avail: new_avail, max_idx: new_max})
        top
    end
  end

  # Helper to pop from a given index moving left if empty
  defp pop_from(-1, state), do: {-1, state}

  defp pop_from(idx, state) do
    case Map.get(state.stacks, idx) do
      nil ->
        # empty slot, move left
        new_state = %{state | stacks: Map.delete(state.stacks, idx)}
        new_avail =
          case :gb_trees.lookup(idx, state.avail) do
            {:value, _} -> :gb_trees.delete_any(idx, state.avail)
            :none -> state.avail
          end

        pop_from(idx - 1, %{new_state | avail: new_avail, max_idx: idx - 1})

      {[], _} ->
        # should not happen, treat as empty
        pop_from(idx - 1, state)

      {[top | rest], size} ->
        new_size = size - 1

        new_stacks =
          if new_size == 0 do
            Map.delete(state.stacks, idx)
          else
            Map.put(state.stacks, idx, {rest, new_size})
          end

        # ensure idx is in avail (has space now)
        new_avail =
          case :gb_trees.lookup(idx, state.avail) do
            {:value, _} -> state.avail
            :none -> :gb_trees.enter(idx, true, state.avail)
          end

        final_max = if new_size == 0, do: idx - 1, else: state.max_idx
        {top, %{state | stacks: new_stacks, avail: new_avail, max_idx: final_max}}
    end
  end

  # Find the next non‑empty stack index moving leftwards
  defp find_new_max(-1, _stacks), do: -1

  defp find_new_max(idx, stacks) do
    case Map.get(stacks, idx) do
      nil -> find_new_max(idx - 1, stacks)
      {[], _} -> find_new_max(idx - 1, stacks)
      _ -> idx
    end
  end
end
```
