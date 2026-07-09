# 2034. Stock Price Fluctuation

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class StockPrice {
    unordered_map<int, int> priceAt;
    priority_queue<pair<int,int>> maxHeap; // (price, timestamp)
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap; // (price, timestamp)
    int latestTimestamp = 0;
public:
    StockPrice() {}
    
    void update(int timestamp, int price) {
        priceAt[timestamp] = price;
        maxHeap.emplace(price, timestamp);
        minHeap.emplace(price, timestamp);
        if (timestamp > latestTimestamp) latestTimestamp = timestamp;
    }
    
    int current() {
        return priceAt[latestTimestamp];
    }
    
    int maximum() {
        while (!maxHeap.empty()) {
            auto [p, t] = maxHeap.top();
            if (priceAt[t] == p) return p;
            maxHeap.pop();
        }
        return -1; // unreachable per constraints
    }
    
    int minimum() {
        while (!minHeap.empty()) {
            auto [p, t] = minHeap.top();
            if (priceAt[t] == p) return p;
            minHeap.pop();
        }
        return -1; // unreachable per constraints
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
```

## Java

```java
class StockPrice {
    private java.util.Map<Integer, Integer> tsToPrice;
    private java.util.TreeMap<Integer, Integer> priceCount;
    private int latestTimestamp;

    public StockPrice() {
        tsToPrice = new java.util.HashMap<>();
        priceCount = new java.util.TreeMap<>();
        latestTimestamp = 0;
    }

    public void update(int timestamp, int price) {
        if (timestamp > latestTimestamp) {
            latestTimestamp = timestamp;
        }
        Integer oldPrice = tsToPrice.get(timestamp);
        if (oldPrice != null) {
            int cnt = priceCount.get(oldPrice);
            if (cnt == 1) {
                priceCount.remove(oldPrice);
            } else {
                priceCount.put(oldPrice, cnt - 1);
            }
        }
        tsToPrice.put(timestamp, price);
        priceCount.put(price, priceCount.getOrDefault(price, 0) + 1);
    }

    public int current() {
        return tsToPrice.get(latestTimestamp);
    }

    public int maximum() {
        return priceCount.lastKey();
    }

    public int minimum() {
        return priceCount.firstKey();
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
```

## Python

```python
import heapq

class StockPrice(object):
    def __init__(self):
        self.prices = {}
        self.max_heap = []
        self.min_heap = []
        self.latest_ts = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        self.prices[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        if timestamp > self.latest_ts:
            self.latest_ts = timestamp

    def current(self):
        """
        :rtype: int
        """
        return self.prices[self.latest_ts]

    def maximum(self):
        """
        :rtype: int
        """
        while True:
            neg_price, ts = self.max_heap[0]
            price = -neg_price
            if self.prices.get(ts) == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self):
        """
        :rtype: int
        """
        while True:
            price, ts = self.min_heap[0]
            if self.prices.get(ts) == price:
                return price
            heapq.heappop(self.min_heap)
```

## Python3

```python
import heapq

class StockPrice:
    def __init__(self):
        self.prices = {}
        self.latest_ts = 0
        self.max_heap = []  # (-price, timestamp)
        self.min_heap = []  # (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        if timestamp > self.latest_ts:
            self.latest_ts = timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.latest_ts]

    def maximum(self) -> int:
        while True:
            neg_price, ts = self.max_heap[0]
            price = -neg_price
            if self.prices.get(ts) == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, ts = self.min_heap[0]
            if self.prices.get(ts) == price:
                return price
            heapq.heappop(self.min_heap)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int price;
    int timestamp;
} HeapNode;

typedef struct {
    int *keys;
    int *vals;
    char *used;
    int cap;
    int mask;
    HeapNode *maxHeap;
    HeapNode *minHeap;
    int maxSize;
    int minSize;
    int latestTimestamp;
} StockPrice;

/* hash map helpers */
static int hashGet(StockPrice *obj, int key) {
    unsigned int idx = ((unsigned int)key * 2654435761u) & obj->mask;
    while (obj->used[idx]) {
        if (obj->keys[idx] == key) return obj->vals[idx];
        idx = (idx + 1) & obj->mask;
    }
    return -1;  // not found
}

static void hashSet(StockPrice *obj, int key, int value) {
    unsigned int idx = ((unsigned int)key * 2654435761u) & obj->mask;
    while (obj->used[idx]) {
        if (obj->keys[idx] == key) {
            obj->vals[idx] = value;
            return;
        }
        idx = (idx + 1) & obj->mask;
    }
    obj->used[idx] = 1;
    obj->keys[idx] = key;
    obj->vals[idx] = value;
}

/* max-heap helpers */
static void maxHeapPush(StockPrice *obj, int price, int timestamp) {
    int i = ++obj->maxSize;
    obj->maxHeap[i].price = price;
    obj->maxHeap[i].timestamp = timestamp;
    while (i > 1) {
        int p = i >> 1;
        if (obj->maxHeap[p].price >= obj->maxHeap[i].price) break;
        HeapNode tmp = obj->maxHeap[p];
        obj->maxHeap[p] = obj->maxHeap[i];
        obj->maxHeap[i] = tmp;
        i = p;
    }
}

/* min-heap helpers */
static void minHeapPush(StockPrice *obj, int price, int timestamp) {
    int i = ++obj->minSize;
    obj->minHeap[i].price = price;
    obj->minHeap[i].timestamp = timestamp;
    while (i > 1) {
        int p = i >> 1;
        if (obj->minHeap[p].price <= obj->minHeap[i].price) break;
        HeapNode tmp = obj->minHeap[p];
        obj->minHeap[p] = obj->minHeap[i];
        obj->minHeap[i] = tmp;
        i = p;
    }
}

/* heap cleanup for max */
static void cleanMaxHeap(StockPrice *obj) {
    while (obj->maxSize > 0) {
        HeapNode top = obj->maxHeap[1];
        int cur = hashGet(obj, top.timestamp);
        if (cur == top.price) break;
        /* remove outdated top */
        obj->maxHeap[1] = obj->maxHeap[obj->maxSize--];
        int i = 1;
        while (1) {
            int l = i << 1, r = l + 1, largest = i;
            if (l <= obj->maxSize && obj->maxHeap[l].price > obj->maxHeap[largest].price)
                largest = l;
            if (r <= obj->maxSize && obj->maxHeap[r].price > obj->maxHeap[largest].price)
                largest = r;
            if (largest == i) break;
            HeapNode tmp = obj->maxHeap[i];
            obj->maxHeap[i] = obj->maxHeap[largest];
            obj->maxHeap[largest] = tmp;
            i = largest;
        }
    }
}

/* heap cleanup for min */
static void cleanMinHeap(StockPrice *obj) {
    while (obj->minSize > 0) {
        HeapNode top = obj->minHeap[1];
        int cur = hashGet(obj, top.timestamp);
        if (cur == top.price) break;
        /* remove outdated top */
        obj->minHeap[1] = obj->minHeap[obj->minSize--];
        int i = 1;
        while (1) {
            int l = i << 1, r = l + 1, smallest = i;
            if (l <= obj->minSize && obj->minHeap[l].price < obj->minHeap[smallest].price)
                smallest = l;
            if (r <= obj->minSize && obj->minHeap[r].price < obj->minHeap[smallest].price)
                smallest = r;
            if (smallest == i) break;
            HeapNode tmp = obj->minHeap[i];
            obj->minHeap[i] = obj->minHeap[smallest];
            obj->minHeap[smallest] = tmp;
            i = smallest;
        }
    }
}

/* API implementations */
StockPrice* stockPriceCreate() {
    const int HASH_CAP = 262144; // power of two > 2 * 1e5
    StockPrice *obj = (StockPrice *)malloc(sizeof(StockPrice));
    obj->cap = HASH_CAP;
    obj->mask = HASH_CAP - 1;
    obj->keys = (int *)malloc(HASH_CAP * sizeof(int));
    obj->vals = (int *)malloc(HASH_CAP * sizeof(int));
    obj->used = (char *)calloc(HASH_CAP, sizeof(char));

    int heapCap = 200005; // enough for all pushes
    obj->maxHeap = (HeapNode *)malloc((heapCap) * sizeof(HeapNode));
    obj->minHeap = (HeapNode *)malloc((heapCap) * sizeof(HeapNode));
    obj->maxSize = 0;
    obj->minSize = 0;
    obj->latestTimestamp = -1;
    return obj;
}

void stockPriceUpdate(StockPrice* obj, int timestamp, int price) {
    hashSet(obj, timestamp, price);
    maxHeapPush(obj, price, timestamp);
    minHeapPush(obj, price, timestamp);
    if (timestamp > obj->latestTimestamp) obj->latestTimestamp = timestamp;
}

int stockPriceCurrent(StockPrice* obj) {
    return hashGet(obj, obj->latestTimestamp);
}

int stockPriceMaximum(StockPrice* obj) {
    cleanMaxHeap(obj);
    return obj->maxHeap[1].price;
}

int stockPriceMinimum(StockPrice* obj) {
    cleanMinHeap(obj);
    return obj->minHeap[1].price;
}

void stockPriceFree(StockPrice* obj) {
    free(obj->keys);
    free(obj->vals);
    free(obj->used);
    free(obj->maxHeap);
    free(obj->minHeap);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class StockPrice {
    private readonly Dictionary<int, int> _timestampToPrice;
    private int _latestTimestamp;
    private readonly PriorityQueue<(int price, int timestamp), int> _minHeap;
    private readonly PriorityQueue<(int price, int timestamp), int> _maxHeap;

    public StockPrice() {
        _timestampToPrice = new Dictionary<int, int>();
        _latestTimestamp = 0;
        _minHeap = new PriorityQueue<(int, int), int>();
        _maxHeap = new PriorityQueue<(int, int), int>();
    }

    public void Update(int timestamp, int price) {
        _timestampToPrice[timestamp] = price;
        if (timestamp > _latestTimestamp) {
            _latestTimestamp = timestamp;
        }
        _minHeap.Enqueue((price, timestamp), price);
        _maxHeap.Enqueue((price, timestamp), -price);
    }

    public int Current() {
        return _timestampToPrice[_latestTimestamp];
    }

    public int Maximum() {
        while (true) {
            var top = _maxHeap.Peek();
            if (_timestampToPrice.TryGetValue(top.timestamp, out int curPrice) && curPrice == top.price) {
                return top.price;
            }
            _maxHeap.Dequeue();
        }
    }

    public int Minimum() {
        while (true) {
            var top = _minHeap.Peek();
            if (_timestampToPrice.TryGetValue(top.timestamp, out int curPrice) && curPrice == top.price) {
                return top.price;
            }
            _minHeap.Dequeue();
        }
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.Update(timestamp,price);
 * int param_2 = obj.Current();
 * int param_3 = obj.Maximum();
 * int param_4 = obj.Minimum();
 */
```

## Javascript

```javascript
var Heap = /** @class */ (function () {
    function Heap(compare) {
        this.data = [];
        this.compare = compare;
    }
    Heap.prototype.size = function () {
        return this.data.length;
    };
    Heap.prototype.peek = function () {
        return this.data[0];
    };
    Heap.prototype.push = function (item) {
        var arr = this.data;
        arr.push(item);
        this._siftUp(arr.length - 1);
    };
    Heap.prototype.pop = function () {
        var arr = this.data;
        if (arr.length === 0)
            return undefined;
        var top = arr[0];
        var last = arr.pop();
        if (arr.length > 0) {
            arr[0] = last;
            this._siftDown(0);
        }
        return top;
    };
    Heap.prototype._siftUp = function (idx) {
        var arr = this.data, compare = this.compare;
        while (idx > 0) {
            var parent = (idx - 1) >> 1;
            if (compare(arr[parent], arr[idx]))
                break;
            var tmp = arr[parent];
            arr[parent] = arr[idx];
            arr[idx] = tmp;
            idx = parent;
        }
    };
    Heap.prototype._siftDown = function (idx) {
        var arr = this.data, compare = this.compare;
        var n = arr.length;
        while (true) {
            var left = idx * 2 + 1;
            var right = left + 1;
            var best = idx;
            if (left < n && !compare(arr[best], arr[left]))
                best = left;
            if (right < n && !compare(arr[best], arr[right]))
                best = right;
            if (best === idx)
                break;
            var tmp = arr[idx];
            arr[idx] = arr[best];
            arr[best] = tmp;
            idx = best;
        }
    };
    return Heap;
}());
var StockPrice = function () {
    this.timeToPrice = new Map();
    this.latestTimestamp = 0;
    // max-heap: higher price first
    this.maxHeap = new Heap(function (a, b) { return a[0] >= b[0]; });
    // min-heap: lower price first
    this.minHeap = new Heap(function (a, b) { return a[0] <= b[0]; });
};
StockPrice.prototype.update = function (timestamp, price) {
    this.timeToPrice.set(timestamp, price);
    if (timestamp > this.latestTimestamp)
        this.latestTimestamp = timestamp;
    this.maxHeap.push([price, timestamp]);
    this.minHeap.push([price, timestamp]);
};
StockPrice.prototype.current = function () {
    return this.timeToPrice.get(this.latestTimestamp);
};
StockPrice.prototype.maximum = function () {
    while (true) {
        var top = this.maxHeap.peek();
        if (!top)
            break;
        var price = top[0], ts = top[1];
        if (this.timeToPrice.get(ts) === price)
            return price;
        this.maxHeap.pop();
    }
};
StockPrice.prototype.minimum = function () {
    while (true) {
        var top = this.minHeap.peek();
        if (!top)
            break;
        var price = top[0], ts = top[1];
        if (this.timeToPrice.get(ts) === price)
            return price;
        this.minHeap.pop();
    }
};
```

## Typescript

```typescript
class Heap {
    private data: [number, number][] = [];
    private cmp: (a: [number, number], b: [number, number]) => boolean;

    constructor(cmp: (a: [number, number], b: [number, number]) => boolean) {
        this.cmp = cmp;
    }

    peek(): [number, number] | undefined {
        return this.data[0];
    }

    push(item: [number, number]): void {
        const arr = this.data;
        arr.push(item);
        let i = arr.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.cmp(arr[p], arr[i])) break; // parent has higher priority
            [arr[p], arr[i]] = [arr[i], arr[p]];
            i = p;
        }
    }

    pop(): [number, number] | undefined {
        const arr = this.data;
        if (arr.length === 0) return undefined;
        const top = arr[0];
        const last = arr.pop()!;
        if (arr.length > 0) {
            arr[0] = last;
            let i = 0;
            const n = arr.length;
            while (true) {
                let left = i * 2 + 1;
                let right = i * 2 + 2;
                let best = i;
                if (left < n && this.cmp(arr[left], arr[best])) best = left;
                if (right < n && this.cmp(arr[right], arr[best])) best = right;
                if (best === i) break;
                [arr[i], arr[best]] = [arr[best], arr[i]];
                i = best;
            }
        }
        return top;
    }

    size(): number {
        return this.data.length;
    }
}

class StockPrice {
    private tsToPrice: Map<number, number>;
    private maxHeap: Heap;
    private minHeap: Heap;
    private latestTimestamp: number;

    constructor() {
        this.tsToPrice = new Map();
        // Max-heap: higher price has higher priority
        this.maxHeap = new Heap((a, b) => a[0] > b[0]);
        // Min-heap: lower price has higher priority
        this.minHeap = new Heap((a, b) => a[0] < b[0]);
        this.latestTimestamp = -1;
    }

    update(timestamp: number, price: number): void {
        this.tsToPrice.set(timestamp, price);
        if (timestamp > this.latestTimestamp) {
            this.latestTimestamp = timestamp;
        }
        this.maxHeap.push([price, timestamp]);
        this.minHeap.push([price, timestamp]);
    }

    current(): number {
        return this.tsToPrice.get(this.latestTimestamp)!;
    }

    maximum(): number {
        while (true) {
            const top = this.maxHeap.peek();
            if (!top) break; // should not happen
            const [p, t] = top;
            if (this.tsToPrice.get(t) === p) {
                return p;
            }
            this.maxHeap.pop(); // discard stale entry
        }
        return -1;
    }

    minimum(): number {
        while (true) {
            const top = this.minHeap.peek();
            if (!top) break; // should not happen
            const [p, t] = top;
            if (this.tsToPrice.get(t) === p) {
                return p;
            }
            this.minHeap.pop(); // discard stale entry
        }
        return -1;
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = new StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
```

## Php

```php
class StockPrice {
    private $prices;
    private $latestTimestamp;
    private $maxHeap;
    private $minHeap;

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->prices = [];
        $this->latestTimestamp = 0;
        $this->maxHeap = new SplPriorityQueue();
        $this->maxHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $this->minHeap = new SplPriorityQueue();
        $this->minHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
    }

    /**
     * @param Integer $timestamp
     * @param Integer $price
     * @return NULL
     */
    function update($timestamp, $price) {
        $this->prices[$timestamp] = $price;
        if ($timestamp > $this->latestTimestamp) {
            $this->latestTimestamp = $timestamp;
        }
        // max-heap: priority = price
        $this->maxHeap->insert([$timestamp, $price], $price);
        // min-heap: use negative price as priority to simulate min-heap
        $this->minHeap->insert([$timestamp, $price], -$price);
    }

    /**
     * @return Integer
     */
    function current() {
        return $this->prices[$this->latestTimestamp];
    }

    /**
     * @return Integer
     */
    function maximum() {
        while (true) {
            $top = $this->maxHeap->top(); // [$timestamp, $price]
            [$ts, $p] = $top;
            if (isset($this->prices[$ts]) && $this->prices[$ts] === $p) {
                return $p;
            }
            $this->maxHeap->extract(); // discard stale entry
        }
    }

    /**
     * @return Integer
     */
    function minimum() {
        while (true) {
            $top = $this->minHeap->top(); // [$timestamp, $price]
            [$ts, $p] = $top;
            if (isset($this->prices[$ts]) && $this->prices[$ts] === $p) {
                return $p;
            }
            $this->minHeap->extract(); // discard stale entry
        }
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * $obj = new StockPrice();
 * $obj->update($timestamp, $price);
 * $ret_2 = $obj->current();
 * $ret_3 = $obj->maximum();
 * $ret_4 = $obj->minimum();
 */
```

## Swift

```swift
class StockPrice {
    private var priceAtTimestamp: [Int: Int] = [:]
    private var latestTimestamp: Int = 0

    private struct HeapElement {
        let price: Int
        let timestamp: Int
    }

    private struct Heap {
        var elements: [HeapElement] = []
        let areSorted: (HeapElement, HeapElement) -> Bool   // true if first has higher priority

        init(_ areSorted: @escaping (HeapElement, HeapElement) -> Bool) {
            self.areSorted = areSorted
        }

        mutating func push(_ value: HeapElement) {
            elements.append(value)
            siftUp(from: elements.count - 1)
        }

        mutating func pop() -> HeapElement? {
            guard !elements.isEmpty else { return nil }
            if elements.count == 1 {
                return elements.removeLast()
            }
            let top = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return top
        }

        func peek() -> HeapElement? {
            return elements.first
        }

        private mutating func siftUp(from index: Int) {
            var childIdx = index
            var parentIdx = (childIdx - 1) / 2
            while childIdx > 0 && areSorted(elements[childIdx], elements[parentIdx]) {
                elements.swapAt(childIdx, parentIdx)
                childIdx = parentIdx
                parentIdx = (childIdx - 1) / 2
            }
        }

        private mutating func siftDown(from index: Int) {
            var parentIdx = index
            while true {
                let leftIdx = parentIdx * 2 + 1
                let rightIdx = leftIdx + 1
                var candidateIdx = parentIdx

                if leftIdx < elements.count && areSorted(elements[leftIdx], elements[candidateIdx]) {
                    candidateIdx = leftIdx
                }
                if rightIdx < elements.count && areSorted(elements[rightIdx], elements[candidateIdx]) {
                    candidateIdx = rightIdx
                }
                if candidateIdx == parentIdx { return }
                elements.swapAt(parentIdx, candidateIdx)
                parentIdx = candidateIdx
            }
        }
    }

    private var maxHeap: Heap
    private var minHeap: Heap

    init() {
        maxHeap = Heap({ $0.price > $1.price })
        minHeap = Heap({ $0.price < $1.price })
    }

    func update(_ timestamp: Int, _ price: Int) {
        priceAtTimestamp[timestamp] = price
        if timestamp > latestTimestamp { latestTimestamp = timestamp }
        let element = HeapElement(price: price, timestamp: timestamp)
        maxHeap.push(element)
        minHeap.push(element)
    }

    func current() -> Int {
        return priceAtTimestamp[latestTimestamp]!
    }

    func maximum() -> Int {
        while let top = maxHeap.peek(),
              priceAtTimestamp[top.timestamp] != top.price {
            _ = maxHeap.pop()
        }
        return maxHeap.peek()!.price
    }

    func minimum() -> Int {
        while let top = minHeap.peek(),
              priceAtTimestamp[top.timestamp] != top.price {
            _ = minHeap.pop()
        }
        return minHeap.peek()!.price
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice()
 * obj.update(timestamp, price)
 * let ret_2: Int = obj.current()
 * let ret_3: Int = obj.maximum()
 * let ret_4: Int = obj.minimum()
 */
```

## Kotlin

```kotlin
class StockPrice() {
    private val tsMap = HashMap<Int, Int>()
    private val priceCount = java.util.TreeMap<Int, Int>()
    private var latestTs = 0

    fun update(timestamp: Int, price: Int) {
        val oldPrice = tsMap.put(timestamp, price)
        if (oldPrice != null) {
            val cnt = priceCount[oldPrice]!!
            if (cnt == 1) priceCount.remove(oldPrice) else priceCount[oldPrice] = cnt - 1
        }
        priceCount[price] = (priceCount[price] ?: 0) + 1
        if (timestamp > latestTs) {
            latestTs = timestamp
        }
    }

    fun current(): Int {
        return tsMap[latestTs]!!
    }

    fun maximum(): Int {
        return priceCount.lastKey()
    }

    fun minimum(): Int {
        return priceCount.firstKey()
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
```

## Dart

```dart
import 'dart:collection';

class StockPrice {
  final Map<int, int> _timestampToPrice = {};
  int _latestTimestamp = 0;
  final PriorityQueue<List<int>> _maxHeap;
  final PriorityQueue<List<int>> _minHeap;

  StockPrice()
      : _maxHeap = PriorityQueue<List<int>>((a, b) => b[0].compareTo(a[0])),
        _minHeap = PriorityQueue<List<int>>((a, b) => a[0].compareTo(b[0])) {}

  void update(int timestamp, int price) {
    _timestampToPrice[timestamp] = price;
    if (timestamp > _latestTimestamp) {
      _latestTimestamp = timestamp;
    }
    _maxHeap.add([price, timestamp]);
    _minHeap.add([price, timestamp]);
  }

  int current() {
    return _timestampToPrice[_latestTimestamp]!;
  }

  int maximum() {
    while (true) {
      final top = _maxHeap.first;
      if (_timestampToPrice[top[1]] == top[0]) {
        return top[0];
      }
      _maxHeap.removeFirst();
    }
  }

  int minimum() {
    while (true) {
      final top = _minHeap.first;
      if (_timestampToPrice[top[1]] == top[0]) {
        return top[0];
      }
      _minHeap.removeFirst();
    }
  }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = StockPrice();
 * obj.update(timestamp,price);
 * int param2 = obj.current();
 * int param3 = obj.maximum();
 * int param4 = obj.minimum();
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type Item struct {
	price int
	ts    int
}

/* Max Heap */
type MaxHeap []Item

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	if h[i].price == h[j].price {
		return h[i].ts > h[j].ts
	}
	return h[i].price > h[j].price
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

/* Min Heap */
type MinHeap []Item

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].price == h[j].price {
		return h[i].ts < h[j].ts
	}
	return h[i].price < h[j].price
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

/* StockPrice */
type StockPrice struct {
	prices   map[int]int
	maxH     MaxHeap
	minH     MinHeap
	latestTs int
}

func Constructor() StockPrice {
	sp := StockPrice{
		prices: make(map[int]int),
		maxH:   MaxHeap{},
		minH:   MinHeap{},
	}
	heap.Init(&sp.maxH)
	heap.Init(&sp.minH)
	return sp
}

func (this *StockPrice) Update(timestamp int, price int) {
	this.prices[timestamp] = price
	if timestamp > this.latestTs {
		this.latestTs = timestamp
	}
	heap.Push(&this.maxH, Item{price: price, ts: timestamp})
	heap.Push(&this.minH, Item{price: price, ts: timestamp})
}

func (this *StockPrice) Current() int {
	return this.prices[this.latestTs]
}

func (this *StockPrice) Maximum() int {
	for {
		top := this.maxH[0]
		if cur, ok := this.prices[top.ts]; ok && cur == top.price {
			return top.price
		}
		heap.Pop(&this.maxH)
	}
}

func (this *StockPrice) Minimum() int {
	for {
		top := this.minH[0]
		if cur, ok := this.prices[top.ts]; ok && cur == top.price {
			return top.price
		}
		heap.Pop(&this.minH)
	}
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */
```

## Ruby

```ruby
class StockPrice
  def initialize
    @price_at = {}          # timestamp => price
    @max_heap = []          # max-heap of [price, timestamp]
    @min_heap = []          # min-heap of [price, timestamp]
    @latest_ts = 0
  end

=begin
  :type timestamp: Integer
  :type price: Integer
  :rtype: Void
=end
  def update(timestamp, price)
    @price_at[timestamp] = price
    push_max([price, timestamp])
    push_min([price, timestamp])
    @latest_ts = timestamp if timestamp > @latest_ts
  end

=begin
  :rtype: Integer
=end
  def current
    @price_at[@latest_ts]
  end

=begin
  :rtype: Integer
=end
  def maximum
    loop do
      price, ts = @max_heap[0]
      return price if @price_at[ts] == price
      pop_max
    end
  end

=begin
  :rtype: Integer
=end
  def minimum
    loop do
      price, ts = @min_heap[0]
      return price if @price_at[ts] == price
      pop_min
    end
  end

  private

  # max-heap operations
  def push_max(item)
    @max_heap << item
    sift_up_max(@max_heap.size - 1)
  end

  def pop_max
    heap = @max_heap
    return if heap.empty?
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      sift_down_max(0)
    end
  end

  def sift_up_max(idx)
    heap = @max_heap
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent][0] >= heap[idx][0]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  def sift_down_max(idx)
    heap = @max_heap
    size = heap.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      largest = left if left < size && heap[left][0] > heap[largest][0]
      largest = right if right < size && heap[right][0] > heap[largest][0]
      break if largest == idx
      heap[largest], heap[idx] = heap[idx], heap[largest]
      idx = largest
    end
  end

  # min-heap operations
  def push_min(item)
    @min_heap << item
    sift_up_min(@min_heap.size - 1)
  end

  def pop_min
    heap = @min_heap
    return if heap.empty?
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      sift_down_min(0)
    end
  end

  def sift_up_min(idx)
    heap = @min_heap
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent][0] <= heap[idx][0]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  def sift_down_min(idx)
    heap = @min_heap
    size = heap.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      smallest = left if left < size && heap[left][0] < heap[smallest][0]
      smallest = right if right < size && heap[right][0] < heap[smallest][0]
      break if smallest == idx
      heap[smallest], heap[idx] = heap[idx], heap[smallest]
      idx = smallest
    end
  end
end
```

## Scala

```scala
import java.util.{PriorityQueue, Comparator}
import scala.collection.mutable

class StockPrice() {

  private case class Node(price: Int, ts: Int)

  private val priceMap = mutable.Map[Int, Int]()
  private var latestTimestamp = 0

  private val maxHeap = new PriorityQueue[Node](new Comparator[Node] {
    override def compare(a: Node, b: Node): Int = Integer.compare(b.price, a.price) // higher price first
  })

  private val minHeap = new PriorityQueue[Node](new Comparator[Node] {
    override def compare(a: Node, b: Node): Int = Integer.compare(a.price, b.price) // lower price first
  })

  def update(timestamp: Int, price: Int): Unit = {
    priceMap.put(timestamp, price)
    if (timestamp > latestTimestamp) latestTimestamp = timestamp
    maxHeap.offer(Node(price, timestamp))
    minHeap.offer(Node(price, timestamp))
  }

  def current(): Int = {
    priceMap(latestTimestamp)
  }

  def maximum(): Int = {
    while (true) {
      val node = maxHeap.peek()
      if (node != null && priceMap.getOrElse(node.ts, -1) == node.price) return node.price
      maxHeap.poll()
    }
    0 // unreachable
  }

  def minimum(): Int = {
    while (true) {
      val node = minHeap.peek()
      if (node != null && priceMap.getOrElse(node.ts, -1) == node.price) return node.price
      minHeap.poll()
    }
    0 // unreachable
  }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * val obj = new StockPrice()
 * obj.update(timestamp,price)
 * val param_2 = obj.current()
 * val param_3 = obj.maximum()
 * val param_4 = obj.minimum()
 */
```

## Rust

```rust
use std::collections::{HashMap, BTreeMap};

struct StockPrice {
    ts_price: HashMap<i32, i32>,
    price_counts: BTreeMap<i32, i32>,
    latest_ts: i32,
}

impl StockPrice {
    fn new() -> Self {
        StockPrice {
            ts_price: HashMap::new(),
            price_counts: BTreeMap::new(),
            latest_ts: 0,
        }
    }

    fn update(&mut self, timestamp: i32, price: i32) {
        if timestamp > self.latest_ts {
            self.latest_ts = timestamp;
        }
        if let Some(&old_price) = self.ts_price.get(&timestamp) {
            if let Some(cnt) = self.price_counts.get_mut(&old_price) {
                *cnt -= 1;
                if *cnt == 0 {
                    self.price_counts.remove(&old_price);
                }
            }
        }
        *self.price_counts.entry(price).or_insert(0) += 1;
        self.ts_price.insert(timestamp, price);
    }

    fn current(&self) -> i32 {
        *self.ts_price.get(&self.latest_ts).unwrap()
    }

    fn maximum(&self) -> i32 {
        *self.price_counts.iter().next_back().unwrap().0
    }

    fn minimum(&self) -> i32 {
        *self.price_counts.iter().next().unwrap().0
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let mut obj = StockPrice::new();
 * obj.update(timestamp, price);
 * let ret_2: i32 = obj.current();
 * let ret_3: i32 = obj.maximum();
 * let ret_4: i32 = obj.minimum();
 */
```

## Racket

```racket
(require racket/base)
(require data/heap)

(define stock-price%
  (class object%
    (super-new)

    ; fields
    (define latest-ts 0)
    (define ts->price (make-hash))
    (define max-heap (make-heap (lambda (a b) (> (car a) (car b)))))
    (define min-heap (make-heap (lambda (a b) (< (car a) (car b)))))

    ; update : exact-integer? exact-integer? -> void?
    (define/public (update timestamp price)
      (when (> timestamp latest-ts)
        (set! latest-ts timestamp))
      (hash-set! ts->price timestamp price)
      (heap-add! max-heap (list price timestamp))
      (heap-add! min-heap (list price timestamp)))

    ; current : -> exact-integer?
    (define/public (current)
      (hash-ref ts->price latest-ts))

    ; maximum : -> exact-integer?
    (define/public (maximum)
      (let loop ()
        (define top (heap-peek max-heap))
        (if (and top
                 (= (hash-ref ts->price (cadr top) #f) (car top)))
            (car top)
            (begin
              (heap-remove-min! max-heap)
              (loop)))))

    ; minimum : -> exact-integer?
    (define/public (minimum)
      (let loop ()
        (define top (heap-peek min-heap))
        (if (and top
                 (= (hash-ref ts->price (cadr top) #f) (car top)))
            (car top)
            (begin
              (heap-remove-min! min-heap)
              (loop))))))
```
```

## Erlang

```erlang
-module(stock_price).
-export([stock_price_init_/0,
         stock_price_update/2,
         stock_price_current/0,
         stock_price_maximum/0,
         stock_price_minimum/0]).

-spec stock_price_init_() -> any().
stock_price_init_() ->
    State = #{ts_map => #{},
              price_tree => gb_trees:empty(),
              latest_ts => 0},
    put(stock_price_state, State).

-spec stock_price_update(Timestamp :: integer(), Price :: integer()) -> any().
stock_price_update(Timestamp, Price) ->
    State = get(stock_price_state),
    TsMap = maps:get(ts_map, State),
    PriceTree = maps:get(price_tree, State),
    LatestTs = maps:get(latest_ts, State),

    % handle possible old price
    {PriceTree1, _} =
        case maps:find(Timestamp, TsMap) of
            {ok, OldPrice} ->
                {dec_price_count(OldPrice, PriceTree), true};
            error ->
                {PriceTree, false}
        end,

    % add new price
    PriceTree2 = inc_price_count(Price, PriceTree1),

    NewTsMap = maps:put(Timestamp, Price, TsMap),
    NewLatestTs = if Timestamp > LatestTs -> Timestamp; true -> LatestTs end,
    NewState = State#{ts_map => NewTsMap,
                      price_tree => PriceTree2,
                      latest_ts => NewLatestTs},
    put(stock_price_state, NewState).

-spec stock_price_current() -> integer().
stock_price_current() ->
    State = get(stock_price_state),
    LatestTs = maps:get(latest_ts, State),
    TsMap = maps:get(ts_map, State),
    maps:get(LatestTs, TsMap).

-spec stock_price_maximum() -> integer().
stock_price_maximum() ->
    State = get(stock_price_state),
    PriceTree = maps:get(price_tree, State),
    {Price, _Count} = gb_trees:largest(PriceTree),
    Price.

-spec stock_price_minimum() -> integer().
stock_price_minimum() ->
    State = get(stock_price_state),
    PriceTree = maps:get(price_tree, State),
    {Price, _Count} = gb_trees:smallest(PriceTree),
    Price.

%% Helper functions
inc_price_count(Price, Tree) ->
    case gb_trees:lookup(Price, Tree) of
        {value, Count} -> gb_trees:update(Price, Count + 1, Tree);
        none -> gb_trees:insert(Price, 1, Tree)
    end.

dec_price_count(Price, Tree) ->
    case gb_trees:lookup(Price, Tree) of
        {value, Count} when Count > 1 ->
            gb_trees:update(Price, Count - 1, Tree);
        {value, 1} ->
            gb_trees:delete(Price, Tree)
    end.
```

## Elixir

```elixir
defmodule StockPrice do
  @spec init_() :: any
  def init_() do
    state = %{
      ts_to_price: %{},
      price_tree: :gb_trees.empty(),
      latest_ts: 0
    }

    Process.put(:stock_state, state)
  end

  @spec update(timestamp :: integer, price :: integer) :: any
  def update(timestamp, price) do
    state = Process.get(:stock_state)

    old_price = Map.get(state.ts_to_price, timestamp)

    new_ts_map = Map.put(state.ts_to_price, timestamp, price)

    tree_after_removal =
      if old_price != nil do
        dec_tree(state.price_tree, old_price)
      else
        state.price_tree
      end

    new_tree = inc_tree(tree_after_removal, price)

    new_latest_ts =
      if timestamp > state.latest_ts do
        timestamp
      else
        state.latest_ts
      end

    new_state = %{
      ts_to_price: new_ts_map,
      price_tree: new_tree,
      latest_ts: new_latest_ts
    }

    Process.put(:stock_state, new_state)
  end

  @spec current() :: integer
  def current() do
    state = Process.get(:stock_state)
    Map.fetch!(state.ts_to_price, state.latest_ts)
  end

  @spec maximum() :: integer
  def maximum() do
    state = Process.get(:stock_state)
    {price, _cnt} = :gb_trees.maximum(state.price_tree)
    price
  end

  @spec minimum() :: integer
  def minimum() do
    state = Process.get(:stock_state)
    {price, _cnt} = :gb_trees.minimum(state.price_tree)
    price
  end

  # Helper functions for managing the price multiset using gb_trees
  defp inc_tree(tree, price) do
    case :gb_trees.lookup(price, tree) do
      {:value, cnt} -> :gb_trees.update(price, cnt + 1, tree)
      :none -> :gb_trees.insert(price, 1, tree)
    end
  end

  defp dec_tree(tree, price) do
    case :gb_trees.lookup(price, tree) do
      {:value, 1} -> :gb_trees.delete(price, tree)
      {:value, cnt} -> :gb_trees.update(price, cnt - 1, tree)
      :none -> tree
    end
  end
end
```
