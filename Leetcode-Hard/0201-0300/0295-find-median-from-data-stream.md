# 0295. Find Median from Data Stream

## Cpp

```cpp
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {}
    
    void addNum(int num) {
        if (low.empty() || num <= low.top()) {
            low.push(num);
        } else {
            high.push(num);
        }
        // Balance the heaps so that their sizes differ at most by 1
        if (low.size() > high.size() + 1) {
            high.push(low.top());
            low.pop();
        } else if (high.size() > low.size() + 1) {
            low.push(high.top());
            high.pop();
        }
    }
    
    double findMedian() {
        if (low.size() == high.size()) {
            return (static_cast<double>(low.top()) + static_cast<double>(high.top())) / 2.0;
        } else if (low.size() > high.size()) {
            return static_cast<double>(low.top());
        } else {
            return static_cast<double>(high.top());
        }
    }

private:
    std::priority_queue<int> low; // max-heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> high; // min-heap
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

## Java

```java
import java.util.Collections;
import java.util.PriorityQueue;

class MedianFinder {
    private PriorityQueue<Integer> maxHeap; // lower half
    private PriorityQueue<Integer> minHeap; // upper half

    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
            maxHeap.offer(num);
        } else {
            minHeap.offer(num);
        }
        // Rebalance heaps
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.offer(maxHeap.poll());
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.offer(minHeap.poll());
        }
    }

    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) {
            return ((double) maxHeap.peek() + (double) minHeap.peek()) / 2.0;
        } else {
            return (double) maxHeap.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

## Python

```python
import heapq

class MedianFinder(object):
    def __init__(self):
        self.small = []  # max-heap (as negatives)
        self.large = []  # min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Balance the heaps so that len(small) >= len(large) and difference <= 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

## Python3

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (as negatives)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Rebalance heaps to maintain size property
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *lower;      // max-heap
    int lowerSize;
    int lowerCap;
    int *upper;      // min-heap
    int upperSize;
    int upperCap;
} MedianFinder;

/* ---------- Max Heap (lower) helpers ---------- */
static void lowerSwap(int *a, int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}
static void lowerHeapifyUp(MedianFinder *obj, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (obj->lower[parent] >= obj->lower[idx]) break;
        lowerSwap(obj->lower, parent, idx);
        idx = parent;
    }
}
static void lowerHeapifyDown(MedianFinder *obj, int idx) {
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int largest = idx;

        if (left < obj->lowerSize && obj->lower[left] > obj->lower[largest])
            largest = left;
        if (right < obj->lowerSize && obj->lower[right] > obj->lower[largest])
            largest = right;
        if (largest == idx) break;

        lowerSwap(obj->lower, idx, largest);
        idx = largest;
    }
}
static void lowerPush(MedianFinder *obj, int val) {
    if (obj->lowerSize == obj->lowerCap) {
        obj->lowerCap = obj->lowerCap ? obj->lowerCap * 2 : 4;
        obj->lower = realloc(obj->lower, obj->lowerCap * sizeof(int));
    }
    obj->lower[obj->lowerSize] = val;
    lowerHeapifyUp(obj, obj->lowerSize);
    obj->lowerSize++;
}
static int lowerTop(MedianFinder *obj) {
    return obj->lower[0];
}
static int lowerPop(MedianFinder *obj) {
    int top = obj->lower[0];
    obj->lowerSize--;
    if (obj->lowerSize > 0) {
        obj->lower[0] = obj->lower[obj->lowerSize];
        lowerHeapifyDown(obj, 0);
    }
    return top;
}

/* ---------- Min Heap (upper) helpers ---------- */
static void upperSwap(int *a, int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}
static void upperHeapifyUp(MedianFinder *obj, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (obj->upper[parent] <= obj->upper[idx]) break;
        upperSwap(obj->upper, parent, idx);
        idx = parent;
    }
}
static void upperHeapifyDown(MedianFinder *obj, int idx) {
    while (1) {
        int left = (idx << 1) + 1;
        int right = left + 1;
        int smallest = idx;

        if (left < obj->upperSize && obj->upper[left] < obj->upper[smallest])
            smallest = left;
        if (right < obj->upperSize && obj->upper[right] < obj->upper[smallest])
            smallest = right;
        if (smallest == idx) break;

        upperSwap(obj->upper, idx, smallest);
        idx = smallest;
    }
}
static void upperPush(MedianFinder *obj, int val) {
    if (obj->upperSize == obj->upperCap) {
        obj->upperCap = obj->upperCap ? obj->upperCap * 2 : 4;
        obj->upper = realloc(obj->upper, obj->upperCap * sizeof(int));
    }
    obj->upper[obj->upperSize] = val;
    upperHeapifyUp(obj, obj->upperSize);
    obj->upperSize++;
}
static int upperTop(MedianFinder *obj) {
    return obj->upper[0];
}
static int upperPop(MedianFinder *obj) {
    int top = obj->upper[0];
    obj->upperSize--;
    if (obj->upperSize > 0) {
        obj->upper[0] = obj->upper[obj->upperSize];
        upperHeapifyDown(obj, 0);
    }
    return top;
}

/* ---------- MedianFinder API ---------- */
MedianFinder* medianFinderCreate() {
    MedianFinder *obj = malloc(sizeof(MedianFinder));
    obj->lower = NULL;   obj->lowerSize = 0; obj->lowerCap = 0;
    obj->upper = NULL;   obj->upperSize = 0; obj->upperCap = 0;
    return obj;
}

void medianFinderAddNum(MedianFinder* obj, int num) {
    if (obj->lowerSize == 0 || num <= lowerTop(obj)) {
        lowerPush(obj, num);
    } else {
        upperPush(obj, num);
    }

    // Balance heaps: ensure lowerSize >= upperSize and diff <= 1
    if (obj->lowerSize > obj->upperSize + 1) {
        int moved = lowerPop(obj);
        upperPush(obj, moved);
    } else if (obj->upperSize > obj->lowerSize) {
        int moved = upperPop(obj);
        lowerPush(obj, moved);
    }
}

double medianFinderFindMedian(MedianFinder* obj) {
    if (obj->lowerSize > obj->upperSize) {
        return (double)lowerTop(obj);
    } else {
        return ((double)lowerTop(obj) + (double)upperTop(obj)) / 2.0;
    }
}

void medianFinderFree(MedianFinder* obj) {
    free(obj->lower);
    free(obj->upper);
    free(obj);
}
```

## Csharp

```csharp
public class MedianFinder {
    private readonly Heap _maxHeap; // lower half
    private readonly Heap _minHeap; // upper half

    public MedianFinder() {
        _maxHeap = new Heap(isMin: false);
        _minHeap = new Heap(isMin: true);
    }
    
    public void AddNum(int num) {
        if (_maxHeap.Count == 0 || num <= _maxHeap.Peek())
            _maxHeap.Push(num);
        else
            _minHeap.Push(num);
        
        // Rebalance heaps to maintain size property
        if (_maxHeap.Count > _minHeap.Count + 1) {
            _minHeap.Push(_maxHeap.Pop());
        } else if (_minHeap.Count > _maxHeap.Count) {
            _maxHeap.Push(_minHeap.Pop());
        }
    }
    
    public double FindMedian() {
        if ((_maxHeap.Count + _minHeap.Count) % 2 == 1)
            return _maxHeap.Peek();
        return (_maxHeap.Peek() + _minHeap.Peek()) / 2.0;
    }

    // Simple binary heap implementation
    private class Heap {
        private readonly List<int> _data = new List<int>();
        private readonly bool _isMin; // true for min-heap, false for max-heap

        public Heap(bool isMin) {
            _isMin = isMin;
        }

        public int Count => _data.Count;

        public void Push(int val) {
            _data.Add(val);
            int idx = _data.Count - 1;
            while (idx > 0) {
                int parent = (idx - 1) / 2;
                if (Compare(_data[idx], _data[parent])) {
                    Swap(idx, parent);
                    idx = parent;
                } else break;
            }
        }

        public int Pop() {
            int root = _data[0];
            int lastIdx = _data.Count - 1;
            _data[0] = _data[lastIdx];
            _data.RemoveAt(lastIdx);
            HeapifyDown(0);
            return root;
        }

        public int Peek() => _data[0];

        private void HeapifyDown(int idx) {
            int n = _data.Count;
            while (true) {
                int left = idx * 2 + 1;
                int right = idx * 2 + 2;
                int target = idx;

                if (left < n && Compare(_data[left], _data[target]))
                    target = left;
                if (right < n && Compare(_data[right], _data[target]))
                    target = right;

                if (target == idx) break;
                Swap(idx, target);
                idx = target;
            }
        }

        // Returns true if a should be above b according to heap type
        private bool Compare(int a, int b) {
            return _isMin ? a < b : a > b;
        }

        private void Swap(int i, int j) {
            int tmp = _data[i];
            _data[i] = _data[j];
            _data[j] = tmp;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */
```

## Javascript

```javascript
var Heap = function(compare) {
    this.data = [];
    this.compare = compare;
};

Heap.prototype.size = function() {
    return this.data.length;
};

Heap.prototype.peek = function() {
    return this.data[0];
};

Heap.prototype.push = function(val) {
    this.data.push(val);
    this._siftUp(this.size() - 1);
};

Heap.prototype.pop = function() {
    if (this.size() === 0) return undefined;
    var top = this.data[0];
    var end = this.data.pop();
    if (this.size() > 0) {
        this.data[0] = end;
        this._siftDown(0);
    }
    return top;
};

Heap.prototype._parent = function(i) {
    return ((i - 1) >> 1);
};

Heap.prototype._left = function(i) {
    return i * 2 + 1;
};

Heap.prototype._right = function(i) {
    return i * 2 + 2;
};

Heap.prototype._siftUp = function(i) {
    while (i > 0) {
        var p = this._parent(i);
        if (this.compare(this.data[i], this.data[p]) < 0) {
            var tmp = this.data[i];
            this.data[i] = this.data[p];
            this.data[p] = tmp;
            i = p;
        } else break;
    }
};

Heap.prototype._siftDown = function(i) {
    var n = this.size();
    while (true) {
        var l = this._left(i), r = this._right(i), best = i;
        if (l < n && this.compare(this.data[l], this.data[best]) < 0) best = l;
        if (r < n && this.compare(this.data[r], this.data[best]) < 0) best = r;
        if (best !== i) {
            var tmp = this.data[i];
            this.data[i] = this.data[best];
            this.data[best] = tmp;
            i = best;
        } else break;
    }
};

var MedianFinder = function() {
    // max-heap for lower half
    this.maxHeap = new Heap(function(a, b) { return b - a; });
    // min-heap for upper half
    this.minHeap = new Heap(function(a, b) { return a - b; });
};

MedianFinder.prototype.addNum = function(num) {
    if (this.maxHeap.size() === 0 || num <= this.maxHeap.peek()) {
        this.maxHeap.push(num);
    } else {
        this.minHeap.push(num);
    }
    // balance sizes
    if (this.maxHeap.size() > this.minHeap.size() + 1) {
        this.minHeap.push(this.maxHeap.pop());
    } else if (this.minHeap.size() > this.maxHeap.size()) {
        this.maxHeap.push(this.minHeap.pop());
    }
};

MedianFinder.prototype.findMedian = function() {
    if (this.maxHeap.size() > this.minHeap.size()) {
        return this.maxHeap.peek();
    } else {
        return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
    }
};
```

## Typescript

```typescript
class Heap {
    private data: number[];
    private compare: (a: number, b: number) => boolean;

    constructor(compare: (a: number, b: number) => boolean) {
        this.data = [];
        this.compare = compare;
    }

    size(): number {
        return this.data.length;
    }

    peek(): number | undefined {
        return this.data[0];
    }

    push(val: number): void {
        this.data.push(val);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): number | undefined {
        if (this.data.length === 0) return undefined;
        const top = this.data[0];
        const end = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = end;
            this.bubbleDown(0);
        }
        return top;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parent = (index - 1) >> 1;
            if (this.compare(this.data[index], this.data[parent])) {
                [this.data[index], this.data[parent]] = [this.data[parent], this.data[index]];
                index = parent;
            } else break;
        }
    }

    private bubbleDown(index: number): void {
        const length = this.data.length;
        while (true) {
            let left = index * 2 + 1;
            let right = index * 2 + 2;
            let smallest = index;

            if (left < length && this.compare(this.data[left], this.data[smallest])) {
                smallest = left;
            }
            if (right < length && this.compare(this.data[right], this.data[smallest])) {
                smallest = right;
            }
            if (smallest !== index) {
                [this.data[index], this.data[smallest]] = [this.data[smallest], this.data[index]];
                index = smallest;
            } else break;
        }
    }
}

class MedianFinder {
    private low: Heap;   // max-heap
    private high: Heap;  // min-heap

    constructor() {
        this.low = new Heap((a, b) => a > b);
        this.high = new Heap((a, b) => a < b);
    }

    addNum(num: number): void {
        if (this.low.size() === 0 || num <= (this.low.peek() as number)) {
            this.low.push(num);
        } else {
            this.high.push(num);
        }

        // Balance the heaps
        if (this.low.size() > this.high.size() + 1) {
            const moved = this.low.pop()!;
            this.high.push(moved);
        } else if (this.high.size() > this.low.size()) {
            const moved = this.high.pop()!;
            this.low.push(moved);
        }
    }

    findMedian(): number {
        if (this.low.size() > this.high.size()) {
            return this.low.peek() as number;
        } else {
            return ((this.low.peek() as number) + (this.high.peek() as number)) / 2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

## Php

```php
class MedianFinder {
    /**
     * @var SplMaxHeap
     */
    private $low;
    /**
     * @var SplMinHeap
     */
    private $high;

    /**
     */
    function __construct() {
        $this->low = new SplMaxHeap(); // max-heap for lower half
        $this->high = new SplMinHeap(); // min-heap for upper half
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function addNum($num) {
        if ($this->low->isEmpty() || $num <= $this->low->top()) {
            $this->low->insert($num);
        } else {
            $this->high->insert($num);
        }

        // Rebalance heaps to ensure size difference is at most 1
        if ($this->low->count() > $this->high->count() + 1) {
            $this->high->insert($this->low->extract());
        } elseif ($this->high->count() > $this->low->count() + 1) {
            $this->low->insert($this->high->extract());
        }
    }

    /**
     * @return Float
     */
    function findMedian() {
        if ($this->low->count() == $this->high->count()) {
            return ($this->low->top() + $this->high->top()) / 2.0;
        } elseif ($this->low->count() > $this->high->count()) {
            return (float)$this->low->top();
        } else {
            return (float)$this->high->top();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * $obj = new MedianFinder();
 * $obj->addNum($num);
 * $ret_2 = $obj->findMedian();
 */
```

## Swift

```swift
class MedianFinder {
    private var lower: Heap // Max-heap
    private var higher: Heap // Min-heap

    init() {
        lower = Heap(sort: >)
        higher = Heap(sort: <)
    }
    
    func addNum(_ num: Int) {
        if lower.isEmpty || num <= (lower.peek ?? num) {
            lower.insert(num)
        } else {
            higher.insert(num)
        }
        
        // Rebalance heaps
        if lower.count > higher.count + 1 {
            if let moved = lower.remove() {
                higher.insert(moved)
            }
        } else if higher.count > lower.count {
            if let moved = higher.remove() {
                lower.insert(moved)
            }
        }
    }
    
    func findMedian() -> Double {
        if lower.count > higher.count {
            return Double(lower.peek!)
        } else {
            return (Double(lower.peek!) + Double(higher.peek!)) / 2.0
        }
    }
}

struct Heap {
    private var elements: [Int] = []
    private let sort: (Int, Int) -> Bool
    
    init(sort: @escaping (Int, Int) -> Bool) {
        self.sort = sort
    }
    
    var isEmpty: Bool { elements.isEmpty }
    var count: Int { elements.count }
    var peek: Int? { elements.first }
    
    mutating func insert(_ value: Int) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func remove() -> Int? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let root = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return root
        }
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && sort(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            
            if left < elements.count && sort(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && sort(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder()
 * obj.addNum(num)
 * let ret_2: Double = obj.findMedian()
 */
```

## Kotlin

```kotlin
import java.util.PriorityQueue

class MedianFinder() {

    private val lower = PriorityQueue<Int>(compareByDescending { it }) // max-heap
    private val higher = PriorityQueue<Int>() // min-heap

    fun addNum(num: Int) {
        if (lower.isEmpty() || num <= lower.peek()) {
            lower.offer(num)
        } else {
            higher.offer(num)
        }
        // Rebalance heaps to maintain size property
        if (lower.size > higher.size + 1) {
            higher.offer(lower.poll())
        } else if (higher.size > lower.size) {
            lower.offer(higher.poll())
        }
    }

    fun findMedian(): Double {
        return if (lower.size == higher.size) {
            (lower.peek().toLong() + higher.peek().toLong()) / 2.0
        } else {
            lower.peek().toDouble()
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

## Dart

```dart
class Heap {
  List<int> _data = [];
  bool Function(int a, int b) _compare; // true if a should be before b

  Heap(this._compare);

  int get size => _data.length;
  bool get isEmpty => _data.isEmpty;

  int top() => _data[0];

  void push(int val) {
    _data.add(val);
    _siftUp(_data.length - 1);
  }

  int pop() {
    if (_data.length == 1) return _data.removeLast();
    final root = _data[0];
    _data[0] = _data.removeLast();
    _siftDown(0);
    return root;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (_compare(_data[idx], _data[parent])) {
        final tmp = _data[idx];
        _data[idx] = _data[parent];
        _data[parent] = tmp;
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    int n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int best = idx;

      if (left < n && _compare(_data[left], _data[best])) best = left;
      if (right < n && _compare(_data[right], _data[best])) best = right;

      if (best != idx) {
        final tmp = _data[idx];
        _data[idx] = _data[best];
        _data[best] = tmp;
        idx = best;
      } else {
        break;
      }
    }
  }
}

class MedianFinder {
  late Heap _maxHeap; // lower half (max-heap)
  late Heap _minHeap; // higher half (min-heap)

  MedianFinder() {
    _maxHeap = Heap((a, b) => a > b);
    _minHeap = Heap((a, b) => a < b);
  }

  void addNum(int num) {
    if (_maxHeap.isEmpty || num <= _maxHeap.top()) {
      _maxHeap.push(num);
    } else {
      _minHeap.push(num);
    }
    // Balance the heaps
    if (_maxHeap.size > _minHeap.size + 1) {
      _minHeap.push(_maxHeap.pop());
    } else if (_minHeap.size > _maxHeap.size) {
      _maxHeap.push(_minHeap.pop());
    }
  }

  double findMedian() {
    if ((_maxHeap.size + _minHeap.size) % 2 == 1) {
      return _maxHeap.top().toDouble();
    } else {
      return (_maxHeap.top() + _minHeap.top()) / 2.0;
    }
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = MedianFinder();
 * obj.addNum(num);
 * double param2 = obj.findMedian();
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } // min-heap
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MedianFinder struct {
	maxHeap *MaxHeap // lower half
	minHeap *MinHeap // upper half
}

/** initialize your data structure here. */
func Constructor() MedianFinder {
	mh := &MaxHeap{}
	heap.Init(mh)
	nh := &MinHeap{}
	heap.Init(nh)
	return MedianFinder{
		maxHeap: mh,
		minHeap: nh,
	}
}

func (this *MedianFinder) AddNum(num int) {
	if this.maxHeap.Len() == 0 || num <= (*this.maxHeap)[0] {
		heap.Push(this.maxHeap, num)
	} else {
		heap.Push(this.minHeap, num)
	}
	// Rebalance
	if this.maxHeap.Len() > this.minHeap.Len()+1 {
		val := heap.Pop(this.maxHeap).(int)
		heap.Push(this.minHeap, val)
	} else if this.minHeap.Len() > this.maxHeap.Len()+1 {
		val := heap.Pop(this.minHeap).(int)
		heap.Push(this.maxHeap, val)
	}
}

func (this *MedianFinder) FindMedian() float64 {
	total := this.maxHeap.Len() + this.minHeap.Len()
	if total%2 == 1 {
		if this.maxHeap.Len() > this.minHeap.Len() {
			return float64((*this.maxHeap)[0])
		}
		return float64((*this.minHeap)[0])
	}
	a := (*this.maxHeap)[0]
	b := (*this.minHeap)[0]
	return (float64(a) + float64(b)) / 2.0
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
```

## Ruby

```ruby
class Heap
  def initialize(&comp)
    @data = []
    @comp = comp || ->(a, b) { a < b } # default min-heap
  end

  def size
    @data.size
  end

  def empty?
    @data.empty?
  end

  def peek
    @data[0]
  end

  def push(val)
    @data << val
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    top
  end

  private

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break unless @comp.call(@data[idx], @data[parent])
      @data[idx], @data[parent] = @data[parent], @data[idx]
      idx = parent
    end
  end

  def sift_down(idx)
    n = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      best = idx
      if left < n && @comp.call(@data[left], @data[best])
        best = left
      end
      if right < n && @comp.call(@data[right], @data[best])
        best = right
      end
      break if best == idx
      @data[idx], @data[best] = @data[best], @data[idx]
      idx = best
    end
  end
end

class MedianFinder
  def initialize()
    # max-heap for lower half
    @lower = Heap.new { |a, b| a > b }
    # min-heap for upper half
    @higher = Heap.new
  end

=begin
    :type num: Integer
    :rtype: Void
=end
  def add_num(num)
    if @lower.empty? || num <= @lower.peek
      @lower.push(num)
    else
      @higher.push(num)
    end

    # Balance the heaps so that size difference is at most 1 and lower has >= higher
    if @lower.size > @higher.size + 1
      @higher.push(@lower.pop)
    elsif @higher.size > @lower.size
      @lower.push(@higher.pop)
    end
  end

=begin
    :rtype: Float
=end
  def find_median()
    if @lower.size > @higher.size
      @lower.peek.to_f
    else
      (@lower.peek + @higher.peek) / 2.0
    end
  end
end
```

## Scala

```scala
class MedianFinder() {

  private val lower = new java.util.PriorityQueue[Int](java.util.Collections.reverseOrder())
  private val higher = new java.util.PriorityQueue[Int]()

  def addNum(num: Int): Unit = {
    if (lower.isEmpty || num <= lower.peek()) {
      lower.offer(num)
    } else {
      higher.offer(num)
    }

    // Rebalance the heaps to maintain size property
    if (lower.size() > higher.size() + 1) {
      higher.offer(lower.poll())
    } else if (higher.size() > lower.size()) {
      lower.offer(higher.poll())
    }
  }

  def findMedian(): Double = {
    if (lower.size() == higher.size()) {
      (lower.peek().toDouble + higher.peek().toDouble) / 2.0
    } else {
      lower.peek().toDouble
    }
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * val obj = new MedianFinder()
 * obj.addNum(num)
 * val param_2 = obj.findMedian()
 */
```

## Rust

```rust
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct MedianFinder {
    low: BinaryHeap<i32>,               // max-heap
    high: BinaryHeap<Reverse<i32>>,     // min-heap
}

impl MedianFinder {

    fn new() -> Self {
        MedianFinder {
            low: BinaryHeap::new(),
            high: BinaryHeap::new(),
        }
    }
    
    fn add_num(&mut self, num: i32) {
        if self.low.peek().map_or(true, |&x| num <= x) {
            self.low.push(num);
        } else {
            self.high.push(Reverse(num));
        }

        // Balance the heaps so that low.len() >= high.len()
        if self.low.len() > self.high.len() + 1 {
            if let Some(val) = self.low.pop() {
                self.high.push(Reverse(val));
            }
        } else if self.high.len() > self.low.len() {
            if let Some(Reverse(val)) = self.high.pop() {
                self.low.push(val);
            }
        }
    }
    
    fn find_median(&self) -> f64 {
        if self.low.len() > self.high.len() {
            *self.low.peek().unwrap() as f64
        } else {
            let a = *self.low.peek().unwrap() as f64;
            let b = self.high.peek().unwrap().0 as f64;
            (a + b) / 2.0
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let mut obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */
```

## Racket

```racket
#lang racket

(require racket/heap)

(define median-finder%
  (class object%
    (super-new)

    (field [lower (make-heap >)]
           [upper (make-heap <)]
           [size-lower 0]
           [size-upper 0])

    ; add-num : exact-integer? -> void?
    (define/public (add-num num)
      (if (or (heap-empty? lower) (<= num (heap-peek lower)))
          (begin
            (heap-add! lower num)
            (set! size-lower (+ size-lower 1)))
          (begin
            (heap-add! upper num)
            (set! size-upper (+ size-upper 1))))
      ;; rebalance heaps if necessary
      (cond
        [(> (- size-lower size-upper) 1)
         (define moved (heap-remove-min! lower))
         (set! size-lower (- size-lower 1))
         (heap-add! upper moved)
         (set! size-upper (+ size-upper 1))]
        [(> (- size-upper size-lower) 1)
         (define moved (heap-remove-min! upper))
         (set! size-upper (- size-upper 1))
         (heap-add! lower moved)
         (set! size-lower (+ size-lower 1))]))

    ; find-median : -> flonum?
    (define/public (find-median)
      (cond
        [(= size-lower size-upper)
         (/ (+ (heap-peek lower) (heap-peek upper)) 2.0)]
        [(> size-lower size-upper)
         (exact->inexact (heap-peek lower))]
        [else
         (exact->inexact (heap-peek upper))]))
    ))
```

## Erlang

```erlang
-spec median_finder_init_() -> any().
median_finder_init_() ->
    put({?MODULE, state}, []).

-spec median_finder_add_num(Num :: integer()) -> any().
median_finder_add_num(Num) ->
    List = get({?MODULE, state}),
    NewList = insert_sorted(List, Num),
    put({?MODULE, state}, NewList).

-spec median_finder_find_median() -> float().
median_finder_find_median() ->
    List = get({?MODULE, state}),
    Len = length(List),
    case Len rem 2 of
        1 ->
            Index = Len div 2 + 1,
            lists:nth(Index, List) * 1.0;
        0 ->
            Index1 = Len div 2,
            Index2 = Index1 + 1,
            A = lists:nth(Index1, List),
            B = lists:nth(Index2, List),
            (A + B) / 2
    end.

%% helper function to insert a number into a sorted list
insert_sorted([], Num) ->
    [Num];
insert_sorted([H|T] = List, Num) when Num =< H ->
    [Num | List];
insert_sorted([H|T], Num) ->
    [H | insert_sorted(T, Num)].
```

## Elixir

```elixir
defmodule MaxHeap do
  def new(), do: {0, :array.new()}

  def size({sz, _}), do: sz

  def peek({0, _}), do: nil
  def peek({_, arr}) do
    :array.get(1, arr)
  end

  def push({sz, arr}, val) do
    idx = sz + 1
    arr = :array.set(idx, val, arr)
    arr = heapify_up(arr, idx)
    {idx, arr}
  end

  def pop({0, _} = heap), do: {nil, heap}
  def pop({sz, arr}) do
    top = :array.get(1, arr)
    last = :array.get(sz, arr)
    arr = :array.set(1, last, arr)
    arr = heapify_down(arr, 1, sz - 1)
    {top, {sz - 1, arr}}
  end

  defp heapify_up(arr, i) when i > 1 do
    parent = div(i, 2)
    val_i = :array.get(i, arr)
    val_p = :array.get(parent, arr)

    if val_i > val_p do
      arr = :array.set(i, val_p, arr)
      arr = :array.set(parent, val_i, arr)
      heapify_up(arr, parent)
    else
      arr
    end
  end

  defp heapify_up(arr, _), do: arr

  defp heapify_down(arr, i, size) do
    left = i * 2
    right = left + 1
    largest = i

    if left <= size and :array.get(left, arr) > :array.get(largest, arr) do
      largest = left
    end

    if right <= size and :array.get(right, arr) > :array.get(largest, arr) do
      largest = right
    end

    if largest != i do
      val_i = :array.get(i, arr)
      val_l = :array.get(largest, arr)

      arr = :array.set(i, val_l, arr)
      arr = :array.set(largest, val_i, arr)

      heapify_down(arr, largest, size)
    else
      arr
    end
  end
end

defmodule MinHeap do
  def new(), do: {0, :array.new()}

  def size({sz, _}), do: sz

  def peek({0, _}), do: nil
  def peek({_, arr}) do
    :array.get(1, arr)
  end

  def push({sz, arr}, val) do
    idx = sz + 1
    arr = :array.set(idx, val, arr)
    arr = heapify_up(arr, idx)
    {idx, arr}
  end

  def pop({0, _} = heap), do: {nil, heap}
  def pop({sz, arr}) do
    top = :array.get(1, arr)
    last = :array.get(sz, arr)
    arr = :array.set(1, last, arr)
    arr = heapify_down(arr, 1, sz - 1)
    {top, {sz - 1, arr}}
  end

  defp heapify_up(arr, i) when i > 1 do
    parent = div(i, 2)
    val_i = :array.get(i, arr)
    val_p = :array.get(parent, arr)

    if val_i < val_p do
      arr = :array.set(i, val_p, arr)
      arr = :array.set(parent, val_i, arr)
      heapify_up(arr, parent)
    else
      arr
    end
  end

  defp heapify_up(arr, _), do: arr

  defp heapify_down(arr, i, size) do
    left = i * 2
    right = left + 1
    smallest = i

    if left <= size and :array.get(left, arr) < :array.get(smallest, arr) do
      smallest = left
    end

    if right <= size and :array.get(right, arr) < :array.get(smallest, arr) do
      smallest = right
    end

    if smallest != i do
      val_i = :array.get(i, arr)
      val_s = :array.get(smallest, arr)

      arr = :array.set(i, val_s, arr)
      arr = :array.set(smallest, val_i, arr)

      heapify_down(arr, smallest, size)
    else
      arr
    end
  end
end

defmodule MedianFinder do
  @agent_name __MODULE__

  def init_() do
    case Process.whereis(@agent_name) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    Agent.start_link(fn -> %{max: MaxHeap.new(), min: MinHeap.new()} end, name: @agent_name)
    :ok
  end

  def add_num(num) do
    Agent.update(@agent_name, fn state ->
      max_heap = state.max
      min_heap = state.min

      max_top = MaxHeap.peek(max_heap)

      cond do
        max_top == nil or num <= max_top ->
          max_heap = MaxHeap.push(max_heap, num)
          %{max: max_heap, min: min_heap}
        true ->
          min_heap = MinHeap.push(min_heap, num)
          %{max: max_heap, min: min_heap}
      end
    end)

    # rebalance after insertion
    Agent.update(@agent_name, fn state ->
      max_heap = state.max
      min_heap = state.min

      {max_sz, _} = max_heap
      {min_sz, _} = min_heap

      cond do
        max_sz > min_sz + 1 ->
          {top, max_heap} = MaxHeap.pop(max_heap)
          min_heap = MinHeap.push(min_heap, top)
          %{max: max_heap, min: min_heap}
        min_sz > max_sz ->
          {top, min_heap} = MinHeap.pop(min_heap)
          max_heap = MaxHeap.push(max_heap, top)
          %{max: max_heap, min: min_heap}
        true ->
          %{max: max_heap, min: min_heap}
      end
    end)
  end

  def find_median() do
    state = Agent.get(@agent_name, & &1)

    {max_sz, _} = state.max
    {min_sz, _} = state.min

    if rem(max_sz + min_sz, 2) == 1 do
      MaxHeap.peek(state.max) * 1.0
    else
      (MaxHeap.peek(state.max) + MinHeap.peek(state.min)) / 2.0
    end
  end
end
```
