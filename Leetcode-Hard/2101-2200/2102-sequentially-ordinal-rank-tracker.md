# 2102. Sequentially Ordinal Rank Tracker

## Cpp

```cpp
class SORTracker {
public:
    struct Item {
        std::string name;
        int score;
    };
    
    // left: max-heap where top is the worst among the best (k+1) items
    struct LeftCmp {
        bool operator()(const Item& a, const Item& b) const {
            if (a.score != b.score) return a.score > b.score;          // higher score = better -> lower priority
            return a.name < b.name;                                    // lexicographically smaller = better -> lower priority
        }
    };
    
    // right: min-heap where top is the best among the rest
    struct RightCmp {
        bool operator()(const Item& a, const Item& b) const {
            if (a.score != b.score) return a.score < b.score;          // lower score = worse -> lower priority
            return a.name > b.name;                                    // larger name = worse -> lower priority
        }
    };
    
    std::priority_queue<Item, std::vector<Item>, LeftCmp> left;
    std::priority_queue<Item, std::vector<Item>, RightCmp> right;
    int getCount = 0;
    
    SORTracker() {
        
    }
    
    void add(std::string name, int score) {
        Item it{std::move(name), score};
        left.push(it);
        if ((int)left.size() > getCount + 1) {
            Item moved = left.top(); left.pop();
            right.push(moved);
        }
    }
    
    std::string get() {
        std::string ans = left.top().name;
        // move the next best from right to left
        ++getCount;
        if (!right.empty()) {
            Item moved = right.top(); right.pop();
            left.push(moved);
        }
        return ans;
    }
};

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker* obj = new SORTracker();
 * obj->add(name,score);
 * string param_2 = obj->get();
 */
```

## Java

```java
class SORTracker {
    private static class Location {
        String name;
        int score;
        Location(String name, int score) {
            this.name = name;
            this.score = score;
        }
    }

    // Comparator for best-first ordering (higher score, then lexicographically smaller name)
    private final java.util.Comparator<Location> bestFirst = (a, b) -> {
        if (a.score != b.score) return Integer.compare(b.score, a.score);
        return a.name.compareTo(b.name);
    };
    // Comparator for left heap: worst among the kept best locations should be at the head
    private final java.util.Comparator<Location> worstFirst = (a, b) -> {
        if (a.score != b.score) return Integer.compare(a.score, b.score); // lower score is worse
        return b.name.compareTo(a.name); // lexicographically larger name is worse
    };

    private final java.util.PriorityQueue<Location> left;   // max-heap of best k+1 items (worst at top)
    private final java.util.PriorityQueue<Location> right;  // min-heap of the rest (best at top)

    private int getCalls = 0;

    public SORTracker() {
        left = new java.util.PriorityQueue<>(worstFirst);
        right = new java.util.PriorityQueue<>(bestFirst);
    }

    public void add(String name, int score) {
        Location loc = new Location(name, score);
        left.add(loc);
        if (left.size() > getCalls + 1) {
            // Move the worst among current best to the right heap
            right.add(left.poll());
        }
    }

    public String get() {
        // The top of left is the (getCalls+1)-th best location
        Location ans = left.peek();
        String result = ans.name;
        // Prepare for next get call
        getCalls++;
        if (!right.isEmpty()) {
            left.add(right.poll());
        }
        return result;
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = new SORTracker();
 * obj.add(name,score);
 * String param_2 = obj.get();
 */
```

## Python

```python
import heapq

class _WorseFirst:
    __slots__ = ('name', 'score')
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score          # lower score is worse
        return self.name > other.name                # larger name is worse

class _BetterFirst:
    __slots__ = ('name', 'score')
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        if self.score != other.score:
            return self.score > other.score          # higher score is better
        return self.name < other.name                # smaller name is better

class SORTracker(object):

    def __init__(self):
        self.k = 0                     # number of get() calls already made
        self.left = []                 # max-heap (worst among top k+1 at root)
        self.right = []                # min-heap (best among the rest at root)

    def add(self, name, score):
        heapq.heappush(self.left, _WorseFirst(name, score))
        if len(self.left) > self.k + 1:
            worst = heapq.heappop(self.left)
            heapq.heappush(self.right, _BetterFirst(worst.name, worst.score))

    def get(self):
        # ensure left holds exactly k+1 best items
        if self.right:
            best = heapq.heappop(self.right)
            heapq.heappush(self.left, _WorseFirst(best.name, best.score))
        result = self.left[0].name
        self.k += 1
        return result
```

## Python3

```python
import heapq

class _Node:
    __slots__ = ('score', 'name')
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name
    # In left heap we want the *worst* element to be at the top.
    # Define ordering so that a "worse" node is considered smaller.
    def __lt__(self, other: '._Node') -> bool:
        if self.score != other.score:
            return self.score < other.score          # lower score => worse
        return self.name > other.name                # lexicographically larger => worse

class SORTracker:

    def __init__(self):
        self.left = []      # max‑heap of best k+1 items (implemented as min‑heap with reversed order)
        self.right = []     # min‑heap of the rest, ordered by (-score, name) so smallest is best
        self.k = 0          # number of get() calls performed

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.left, _Node(score, name))
        if len(self.left) > self.k + 1:
            worst = heapq.heappop(self.left)
            heapq.heappush(self.right, (-worst.score, worst.name))

    def get(self) -> str:
        self.k += 1
        if self.right:
            sc_neg, nm = heapq.heappop(self.right)
            heapq.heappush(self.left, _Node(-sc_neg, nm))
        return self.left[0].name
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Item {
    char *name;
    int score;
} Item;

typedef struct Heap {
    Item **data;
    int size;
    int capacity;
    int (*cmp)(Item *, Item *);
} Heap;

static int better(Item *a, Item *b) { // a is higher priority (better)
    if (a->score != b->score) return a->score > b->score;
    return strcmp(a->name, b->name) < 0;
}

static int worse(Item *a, Item *b) { // a is higher priority (worse)
    if (a->score != b->score) return a->score < b->score;
    return strcmp(a->name, b->name) > 0;
}

static Heap* heapCreate(int capacity, int (*cmp)(Item *, Item *)) {
    Heap *h = (Heap *)malloc(sizeof(Heap));
    h->data = (Item **)malloc(sizeof(Item *) * capacity);
    h->size = 0;
    h->capacity = capacity;
    h->cmp = cmp;
    return h;
}

static void heapSwap(Item **a, Item **b) {
    Item *tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Heap *h, Item *item) {
    if (h->size == h->capacity) {
        h->capacity <<= 1;
        h->data = (Item **)realloc(h->data, sizeof(Item *) * h->capacity);
    }
    int i = h->size++;
    h->data[i] = item;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (h->cmp(h->data[i], h->data[p])) {
            heapSwap(&h->data[i], &h->data[p]);
            i = p;
        } else break;
    }
}

static Item* heapTop(Heap *h) {
    return h->size ? h->data[0] : NULL;
}

static Item* heapPop(Heap *h) {
    if (h->size == 0) return NULL;
    Item *ret = h->data[0];
    h->size--;
    if (h->size) {
        h->data[0] = h->data[h->size];
        int i = 0;
        while (1) {
            int l = (i << 1) + 1, r = l + 1, best = i;
            if (l < h->size && h->cmp(h->data[l], h->data[best])) best = l;
            if (r < h->size && h->cmp(h->data[r], h->data[best])) best = r;
            if (best != i) {
                heapSwap(&h->data[i], &h->data[best]);
                i = best;
            } else break;
        }
    }
    return ret;
}

static void heapFree(Heap *h) {
    for (int i = 0; i < h->size; ++i) {
        free(h->data[i]->name);
        free(h->data[i]);
    }
    free(h->data);
    free(h);
}

/* SORTracker definition */
typedef struct {
    Heap *left;   // max-heap with worse comparator
    Heap *right;  // min-heap with better comparator
    int getCount;
} SORTracker;

SORTracker* sORTrackerCreate() {
    SORTracker *obj = (SORTracker *)malloc(sizeof(SORTracker));
    obj->left = heapCreate(64, worse);
    obj->right = heapCreate(64, better);
    obj->getCount = 0;
    return obj;
}

void sORTrackerAdd(SORTracker* obj, char* name, int score) {
    Item *it = (Item *)malloc(sizeof(Item));
    it->name = strdup(name);
    it->score = score;

    heapPush(obj->left, it);
    if (obj->left->size > obj->getCount + 1) {
        Item *move = heapPop(obj->left);
        heapPush(obj->right, move);
    }
}

char* sORTrackerGet(SORTracker* obj) {
    Item *top = heapTop(obj->left);
    char *ans = strdup(top->name);
    obj->getCount++;

    if (obj->right->size > 0) {
        Item *move = heapPop(obj->right);
        heapPush(obj->left, move);
    }
    return ans;
}

void sORTrackerFree(SORTracker* obj) {
    heapFree(obj->left);
    heapFree(obj->right);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class SORTracker
{
    private class Location
    {
        public string Name;
        public int Score;
    }

    private class LeftComparer : IComparer<Location>
    {
        // Order by ascending score, then descending name (worse first)
        public int Compare(Location a, Location b)
        {
            int cmp = a.Score.CompareTo(b.Score);
            if (cmp != 0) return cmp;
            // larger name is considered smaller (worse)
            return string.Compare(b.Name, a.Name, StringComparison.Ordinal);
        }
    }

    private class RightComparer : IComparer<Location>
    {
        // Order by descending score, then ascending name (better first)
        public int Compare(Location a, Location b)
        {
            int cmp = b.Score.CompareTo(a.Score); // higher score -> smaller
            if (cmp != 0) return cmp;
            return string.Compare(a.Name, b.Name, StringComparison.Ordinal);
        }
    }

    private readonly PriorityQueue<Location, Location> left;   // contains best k+1 items, worst among them at top
    private readonly PriorityQueue<Location, Location> right;  // contains the rest, best among them at top
    private int getCalls;

    public SORTracker()
    {
        left = new PriorityQueue<Location, Location>(new LeftComparer());
        right = new PriorityQueue<Location, Location>(new RightComparer());
        getCalls = 0;
    }

    public void Add(string name, int score)
    {
        var loc = new Location { Name = name, Score = score };
        left.Enqueue(loc, loc);
        if (left.Count > getCalls + 1)
        {
            var moved = left.Dequeue();
            right.Enqueue(moved, moved);
        }
    }

    public string Get()
    {
        // The current answer is the worst among the best (k+1) items
        string ans = left.Peek().Name;
        getCalls++;
        if (right.Count > 0)
        {
            var moved = right.Dequeue();
            left.Enqueue(moved, moved);
        }
        return ans;
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = new SORTracker();
 * obj.Add(name,score);
 * string param_2 = obj.Get();
 */
```

## Javascript

```javascript
var Heap = function(compare) {
    this.data = [];
    this.compare = compare; // returns true if a has higher priority than b
};

Heap.prototype.size = function() {
    return this.data.length;
};

Heap.prototype.peek = function() {
    return this.data[0];
};

Heap.prototype.push = function(item) {
    var arr = this.data;
    arr.push(item);
    var i = arr.length - 1;
    while (i > 0) {
        var p = (i - 1) >> 1;
        if (this.compare(arr[p], arr[i])) break; // parent has higher priority
        var tmp = arr[p];
        arr[p] = arr[i];
        arr[i] = tmp;
        i = p;
    }
};

Heap.prototype.pop = function() {
    var arr = this.data;
    if (arr.length === 0) return undefined;
    var top = arr[0];
    var last = arr.pop();
    if (arr.length > 0) {
        arr[0] = last;
        var n = arr.length;
        var i = 0;
        while (true) {
            var l = i * 2 + 1,
                r = l + 1,
                best = i;
            if (l < n && this.compare(arr[l], arr[best])) best = l;
            if (r < n && this.compare(arr[r], arr[best])) best = r;
            if (best === i) break;
            var tmp = arr[i];
            arr[i] = arr[best];
            arr[best] = tmp;
            i = best;
        }
    }
    return top;
};

var SORTracker = function() {
    // comparator for left heap: worse element has higher priority (root is worst among top)
    var worseComp = function(a, b) {
        if (a.score !== b.score) return a.score < b.score; // lower score is worse
        return a.name > b.name; // lexicographically larger name is worse
    };
    // comparator for right heap: better element has higher priority (root is best among rest)
    var betterComp = function(a, b) {
        if (a.score !== b.score) return a.score > b.score; // higher score is better
        return a.name < b.name; // lexicographically smaller name is better
    };
    this.left = new Heap(worseComp);   // holds top k+1 items, root = (k+1)-th best
    this.right = new Heap(betterComp); // holds the rest
    this.k = 0; // number of get() calls performed so far
};

SORTracker.prototype.add = function(name, score) {
    var node = { name: name, score: score };
    this.left.push(node);
    if (this.left.size() > this.k + 1) {
        var moved = this.left.pop();
        this.right.push(moved);
    }
};

SORTracker.prototype.get = function() {
    var ansNode = this.left.peek(); // current (k+1)-th best
    this.k += 1;
    if (this.right.size() > 0) {
        var moved = this.right.pop(); // next best from the rest
        this.left.push(moved);
    }
    return ansNode.name;
};
```

## Typescript

```typescript
class Heap<T> {
    private data: T[] = [];
    private compare: (a: T, b: T) => boolean; // true if a has higher priority than b

    constructor(compare: (a: T, b: T) => boolean) {
        this.compare = compare;
    }

    size(): number {
        return this.data.length;
    }

    peek(): T | undefined {
        return this.data[0];
    }

    push(item: T): void {
        this.data.push(item);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): T | undefined {
        if (this.data.length === 0) return undefined;
        const top = this.data[0];
        const last = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = last;
            this.bubbleDown(0);
        }
        return top;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parent = (index - 1) >> 1;
            if (!this.compare(this.data[index], this.data[parent])) break;
            [this.data[index], this.data[parent]] = [this.data[parent], this.data[index]];
            index = parent;
        }
    }

    private bubbleDown(index: number): void {
        const n = this.data.length;
        while (true) {
            let left = index * 2 + 1;
            let right = left + 1;
            let best = index;

            if (left < n && this.compare(this.data[left], \`this.data[best]\`)) {
                best = left;
            }
            if (right < n && this.compare(this.data[right], this.data[best])) {
                best = right;
            }
            if (best === index) break;
            [this.data[index], this.data[best]] = [this.data[best], \`this.data[index]\`];
            index = best;
        }
    }
}

interface Location {
    name: string;
    score: number;
}

class SORTracker {
    private left: Heap<Location>;   // max-heap where root is the worst among top (k+1)
    private right: Heap<Location>;  // min-heap where root is the best among the rest
    private k: number;              // number of get() calls performed

    constructor() {
        const worse = (a: Location, b: Location) => {
            if (a.score !== b.score) return a.score < b.score;
            return a.name > b.name;
        };
        const better = (a: Location, b: Location) => {
            if (a.score !== b.score) return a.score > b.score;
            return a.name < b.name;
        };
        this.left = new Heap<Location>(worse);   // root = worst among stored
        this.right = new Heap<Location>(better); // root = best among stored
        this.k = 0;
    }

    add(name: string, score: number): void {
        const loc: Location = { name, score };
        this.left.push(loc);
        if (this.left.size() > this.k + 1) {
            const moved = this.left.pop()!;
            this.right.push(moved);
        }
    }

    get(): string {
        const ans = this.left.peek()!.name;
        this.k++;
        if (this.right.size() > 0) {
            const moved = this.right.pop()!;
            this.left.push(moved);
        }
        return ans;
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * var obj = new SORTracker()
 * obj.add(name,score)
 * var param_2 = obj.get()
 */
```

## Php

```php
class SORTracker {
    private $left;   // Max-heap: worst among the best (k+1) items at top
    private $right;  // Min-heap: best among the rest at top
    private $k = 0;  // number of get() calls performed

    function __construct() {
        $this->left = new class extends SplMaxHeap {
            protected function compare($a, $b) {
                if ($a['score'] === $b['score']) {
                    return strcmp($a['name'], $b['name']);
                }
                // higher score is better => smaller; thus larger (worse) has lower score
                return $b['score'] - $a['score'];
            }
        };
        $this->right = new class extends SplMinHeap {
            protected function compare($a, $b) {
                if ($a['score'] === $b['score']) {
                    return strcmp($a['name'], $b['name']);
                }
                // higher score is better => smaller
                return $b['score'] - $a['score'];
            }
        };
    }

    /**
     * @param String $name
     * @param Integer $score
     * @return NULL
     */
    function add($name, $score) {
        $node = ['name' => $name, 'score' => $score];
        $this->left->insert($node);
        if ($this->left->count() > $this->k + 1) {
            $move = $this->left->extract(); // worst among current best
            $this->right->insert($move);
        }
    }

    /**
     * @return String
     */
    function get() {
        $ansNode = $this->left->top();
        $result = $ansNode['name'];
        $this->k++;
        if (!$this->right->isEmpty()) {
            $move = $this->right->extract(); // best among the rest
            $this->left->insert($move);
        }
        return $result;
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * $obj = new SORTracker();
 * $obj->add($name, $score);
 * $ret_2 = $obj->get();
 */
```

## Swift

```swift
class SORTracker {
    private struct Location {
        let name: String
        let score: Int
    }
    
    private struct Heap<T> {
        var elements: [T] = []
        let areSorted: (T, T) -> Bool   // returns true if first has higher priority
        
        init(sort: @escaping (T, T) -> Bool) {
            self.areSorted = sort
        }
        
        var isEmpty: Bool { elements.isEmpty }
        var count: Int { elements.count }
        func peek() -> T? { elements.first }
        
        mutating func push(_ value: T) {
            elements.append(value)
            siftUp(elements.count - 1)
        }
        
        mutating func pop() -> T? {
            guard !elements.isEmpty else { return nil }
            if elements.count == 1 {
                return elements.removeLast()
            } else {
                let top = elements[0]
                elements[0] = elements.removeLast()
                siftDown(0)
                return top
            }
        }
        
        private mutating func siftUp(_ index: Int) {
            var child = index
            var parent = (child - 1) / 2
            while child > 0 && areSorted(elements[child], elements[parent]) {
                elements.swapAt(child, parent)
                child = parent
                parent = (child - 1) / 2
            }
        }
        
        private mutating func siftDown(_ index: Int) {
            var parent = index
            while true {
                let left = parent * 2 + 1
                let right = left + 1
                var candidate = parent
                if left < elements.count && areSorted(elements[left], elements[candidate]) {
                    candidate = left
                }
                if right < elements.count && areSorted(elements[right], elements[candidate]) {
                    candidate = right
                }
                if candidate == parent { break }
                elements.swapAt(parent, candidate)
                parent = candidate
            }
        }
    }
    
    private var left: Heap<Location>
    private var right: Heap<Location>
    private var getCount: Int = 0
    
    init() {
        // Left heap: max-heap where "worse" location has higher priority (root is worst among best)
        left = Heap(sort: { a, b in
            if a.score != b.score {
                return a.score < b.score   // smaller score => worse
            }
            return a.name > b.name         // lexicographically larger name => worse
        })
        // Right heap: min-heap where "better" location has higher priority (root is best among rest)
        right = Heap(sort: { a, b in
            if a.score != b.score {
                return a.score > b.score   // larger score => better
            }
            return a.name < b.name         // lexicographically smaller name => better
        })
    }
    
    func add(_ name: String, _ score: Int) {
        let loc = Location(name: name, score: score)
        left.push(loc)
        if left.count > getCount + 1 {
            if let moved = left.pop() {
                right.push(moved)
            }
        }
    }
    
    func get() -> String {
        guard let best = left.peek() else { return "" }
        // Move the next best from right to left, if any
        if let candidate = right.pop() {
            left.push(candidate)
        }
        getCount += 1
        return best.name
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * let obj = SORTracker()
 * obj.add(name, score)
 * let ret_2: String = obj.get()
 */
```

## Kotlin

```kotlin
class SORTracker() {
    private data class Location(val name: String, val score: Int)

    // left heap: worst among the best (k+1) items at the top
    private val left = java.util.PriorityQueue<Location>(Comparator { a, b ->
        if (a.score != b.score) a.score - b.score else b.name.compareTo(a.name)
    })
    // right heap: best among the rest at the top
    private val right = java.util.PriorityQueue<Location>(Comparator { a, b ->
        if (a.score != b.score) b.score - a.score else a.name.compareTo(b.name)
    })

    private var getCount = 0

    fun add(name: String, score: Int) {
        val loc = Location(name, score)
        left.add(loc)
        if (left.size > getCount + 1) {
            right.add(left.poll())
        }
    }

    fun get(): String {
        val result = left.peek()!!.name
        getCount++
        if (right.isNotEmpty()) {
            left.add(right.poll())
        }
        return result
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * var obj = SORTracker()
 * obj.add(name,score)
 * var param_2 = obj.get()
 */
```

## Dart

```dart
class Item {
  String name;
  int score;
  Item(this.name, this.score);
}

int compareItems(Item a, Item b) {
  if (a.score != b.score) return b.score - a.score; // higher score is better
  return a.name.compareTo(b.name); // lexicographically smaller is better
}

class BinaryHeap {
  final List<Item> _data = [];
  final bool Function(Item a, Item b) _higherPriority;
  BinaryHeap(this._higherPriority);
  int get size => _data.length;
  bool get isEmpty => _data.isEmpty;
  void push(Item x) {
    _data.add(x);
    _siftUp(_data.length - 1);
  }
  Item pop() {
    final top = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return top;
  }
  Item peek() => _data[0];
  void _siftUp(int i) {
    while (i > 0) {
      final p = (i - 1) >> 1;
      if (!_higherPriority(_data[i], _data[p])) break;
      final tmp = _data[i];
      _data[i] = _data[p];
      _data[p] = tmp;
      i = p;
    }
  }

  void _siftDown(int i) {
    final n = _data.length;
    while (true) {
      int best = i;
      final l = i * 2 + 1;
      final r = l + 1;
      if (l < n && _higherPriority(_data[l], _data[best])) best = l;
      if (r < n && _higherPriority(_data[r], _data[best])) best = r;
      if (best == i) break;
      final tmp = _data[i];
      _data[i] = _data[best];
      _data[best] = tmp;
      i = best;
    }
  }
}

class SORTracker {
  int _getCalls = 0;
  late final BinaryHeap _left; // worst among top k+1 at root
  late final BinaryHeap _right; // best among the rest at root

  SORTracker() {
    _left = BinaryHeap((a, b) => compareItems(a, b) > 0);
    _right = BinaryHeap((a, b) => compareItems(a, b) < 0);
  }

  void add(String name, int score) {
    final item = Item(name, score);
    _left.push(item);
    if (_left.size > _getCalls + 1) {
      final moved = _left.pop(); // worst among current top
      _right.push(moved);
    }
  }

  String get() {
    final ans = _left.peek().name;
    _getCalls++;
    if (!_right.isEmpty) {
      final moved = _right.pop(); // best among the rest
      _left.push(moved);
    }
    return ans;
  }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = SORTracker();
 * obj.add(name,score);
 * String param2 = obj.get();
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type Item struct {
	name  string
	score int
}

// left heap: min-heap where the top is the worst among the best items
type LeftHeap []Item

func (h LeftHeap) Len() int { return len(h) }
func (h LeftHeap) Less(i, j int) bool {
	a, b := h[i], h[j]
	if a.score != b.score {
		return a.score < b.score // lower score is worse
	}
	return a.name > b.name // lexicographically larger name is worse
}
func (h LeftHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *LeftHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *LeftHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// right heap: max-heap where the top is the best among the remaining items
type RightHeap []Item

func (h RightHeap) Len() int { return len(h) }
func (h RightHeap) Less(i, j int) bool {
	a, b := h[i], h[j]
	if a.score != b.score {
		return a.score > b.score // higher score is better
	}
	return a.name < b.name // lexicographically smaller name is better
}
func (h RightHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *RightHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *RightHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

type SORTracker struct {
	left  LeftHeap
	right RightHeap
	k     int // number of times Get has been called
}

/** Initialize your data structure here. */
func Constructor() SORTracker {
	tracker := SORTracker{
		left:  make(LeftHeap, 0),
		right: make(RightHeap, 0),
		k:     0,
	}
	heap.Init(&tracker.left)
	heap.Init(&tracker.right)
	return tracker
}

/** Add a new location. */
func (this *SORTracker) Add(name string, score int) {
	it := Item{name: name, score: score}
	heap.Push(&this.left, it)
	if this.left.Len() > this.k+1 {
		worst := heap.Pop(&this.left).(Item)
		heap.Push(&this.right, worst)
	}
}

/** Return the current k-th best location (0-indexed). */
func (this *SORTracker) Get() string {
	ans := this.left[0].name
	this.k++
	if this.right.Len() > 0 {
		best := heap.Pop(&this.right).(Item)
		heap.Push(&this.left, best)
	}
	return ans
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(name,score);
 * param_2 := obj.Get();
 */
```

## Ruby

```ruby
class Heap
  def initialize(&comp)
    @data = []
    @comp = comp # returns true if a should be above b
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

class SORTracker
  def initialize()
    # left: max-heap where the top is the worst among the current best (k+1) items
    @left = Heap.new do |a, b|
      if a[1] != b[1]
        a[1] < b[1]          # lower score is worse
      else
        a[0] > b[0]          # lexicographically larger name is worse
      end
    end

    # right: min-heap where the top is the best among the remaining items
    @right = Heap.new do |a, b|
      if a[1] != b[1]
        a[1] > b[1]          # higher score is better
      else
        a[0] < b[0]          # lexicographically smaller name is better
      end
    end

    @get_cnt = 0
  end

=begin
    :type name: String
    :type score: Integer
    :rtype: Void
=end
  def add(name, score)
    item = [name, score]
    @left.push(item)
    if @left.size > @get_cnt + 1
      @right.push(@left.pop)
    end
  end

=begin
    :rtype: String
=end
  def get()
    ans_item = @left.peek
    @get_cnt += 1
    unless @right.empty?
      @left.push(@right.pop)
    end
    ans_item[0]
  end
end

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker.new()
# obj.add(name, score)
# param_2 = obj.get()
```

## Scala

```scala
import scala.collection.mutable.PriorityQueue

class SORTracker() {

  private case class Loc(name: String, score: Int)

  private def isBetter(a: Loc, b: Loc): Boolean = {
    if (a.score != b.score) a.score > b.score
    else a.name < b.name
  }

  // Ordering where worse location is considered larger (for left heap)
  private implicit val worstOrdering: Ordering[Loc] = Ordering.fromLessThan[Loc] { (a, b) =>
    if (a.score != b.score) a.score < b.score
    else a.name > b.name
  }

  // Ordering where better location is considered larger (for right heap)
  private implicit val bestOrdering: Ordering[Loc] = Ordering.fromLessThan[Loc] { (a, b) =>
    if (a.score != b.score) a.score > b.score
    else a.name < b.name
  }

  // left holds the top k+1 locations; its head is the worst among them
  private val left: PriorityQueue[Loc] = new PriorityQueue[Loc]()(worstOrdering)
  // right holds the remaining locations; its head is the best among them
  private val right: PriorityQueue[Loc] = new PriorityQueue[Loc]()(bestOrdering)

  private var getCount: Int = 0

  def add(name: String, score: Int): Unit = {
    val loc = Loc(name, score)
    if (left.isEmpty) {
      left.enqueue(loc)
    } else {
      // Compare with the worst among current top k+1
      if (isBetter(loc, left.head)) {
        left.enqueue(loc)
        // Move the new worst from left to right to keep size = getCount + 1
        val moved = left.dequeue()
        right.enqueue(moved)
      } else {
        right.enqueue(loc)
      }
    }
  }

  def get(): String = {
    val result = left.head.name
    getCount += 1
    // After increasing getCount, we need one more element in left
    if (right.nonEmpty) {
      val moved = right.dequeue()
      left.enqueue(moved)
    }
    result
  }

}

/**
 * Your SORTracker object will be instantiated and called as such:
 * val obj = new SORTracker()
 * obj.add(name,score)
 * val param_2 = obj.get()
 */
```

## Rust

```rust
use std::cmp::{Ord, Ordering, Reverse};
use std::collections::BinaryHeap;

#[derive(Clone)]
struct Item {
    score: i32,
    name: String,
}

impl PartialEq for Item {
    fn eq(&self, other: &Self) -> bool {
        self.score == other.score && self.name == other.name
    }
}
impl Eq for Item {}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        match self.score.cmp(&other.score) {
            Ordering::Equal => other.name.cmp(&self.name), // smaller name is better (greater)
            ord => ord,
        }
    }
}

struct SORTracker {
    left: BinaryHeap<Reverse<Item>>, // worst among the best k+1 items at top
    right: BinaryHeap<Item>,         // best among the rest at top
    k: usize,                        // number of get() calls performed
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SORTracker {
    fn new() -> Self {
        SORTracker {
            left: BinaryHeap::new(),
            right: BinaryHeap::new(),
            k: 0,
        }
    }

    fn add(&mut self, name: String, score: i32) {
        let item = Item { score, name };
        self.left.push(Reverse(item));
        if self.left.len() > self.k + 1 {
            // move the worst among current best set to right heap
            if let Some(Reverse(moved)) = self.left.pop() {
                self.right.push(moved);
            }
        }
    }

    fn get(&mut self) -> String {
        // after this call we need k+2 items in left (since k will be incremented)
        self.k += 1;
        if let Some(best_rest) = self.right.pop() {
            self.left.push(Reverse(best_rest));
        }
        // top of left is the worst among the best k+1 items, i.e., the kth best overall
        let rev = self.left.peek().unwrap();
        rev.0.name.clone()
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * let mut obj = SORTracker::new();
 * obj.add(name, score);
 * let ret_2: String = obj.get();
 */
```

## Racket

```racket
(require data/heap)

(define (worse? a b)
  (let* ([sa (first a)] [na (second a)]
         [sb (first b)] [nb (second b)])
    (or (< sa sb)
        (and (= sa sb) (string>? na nb)))))

(define (better? a b)
  (let* ([sa (first a)] [na (second a)]
         [sb (first b)] [nb (second b)])
    (or (> sa sb)
        (and (= sa sb) (string<? na nb)))))

(define sor-tracker%
  (class object%
    (super-new)

    (field [k 0]
           [left (make-heap worse?)]
           [right (make-heap better?)])

    ; add : string? exact-integer? -> void?
    (define/public (add name score)
      (define item (list score name))
      (heap-insert! left item)
      (when (> (heap-size left) (+ k 1))
        (define moved (heap-pop! left))
        (heap-insert! right moved)))

    ; get : -> string?
    (define/public (get)
      (define result-name (second (heap-peek left)))
      (set! k (+ k 1))
      (when (> (heap-size right) 0)
        (define moved (heap-pop! right))
        (heap-insert! left moved))
      result-name)))
```

## Erlang

```erlang
-spec sor_tracker_init_() -> any().
sor_tracker_init_() ->
    put(left, #{data => undefined, sz => 0}),
    put(right, #{data => undefined, sz => 0}),
    put(k, 0).

-spec sor_tracker_add(Name :: unicode:unicode_binary(), Score :: integer()) -> any().
sor_tracker_add(Name, Score) ->
    Elem = {Score, Name},
    K = get(k),
    Left0 = get(left),
    NewLeft = heap_push(Left0, Elem, fun worse/2),
    case maps:get(sz, NewLeft) > K + 1 of
        true ->
            {Top, L2} = heap_pop(NewLeft, fun worse/2),
            Right0 = get(right),
            NewRight = heap_push(Right0, Top, fun better/2),
            put(left, L2),
            put(right, NewRight);
        false ->
            put(left, NewLeft)
    end.

-spec sor_tracker_get() -> unicode:unicode_binary().
sor_tracker_get() ->
    K = get(k),
    Left = get(left),
    {Score, Name} = heap_peek(Left),
    Answer = Name,
    NewK = K + 1,
    put(k, NewK),
    case maps:get(sz, Left) < NewK + 1 of
        true ->
            Right = get(right),
            {TopR, NewRight} = heap_pop(Right, fun better/2),
            L2 = heap_push(Left, TopR, fun worse/2),
            put(left, L2),
            put(right, NewRight);
        false -> ok
    end,
    Answer.

%% Comparator: returns true if A is "greater" (i.e., worse) than B
worse({S1,N1}, {S2,N2}) ->
    case S1 =:= S2 of
        true -> N1 > N2;
        false -> S1 < S2
    end.

%% Comparator for right heap: returns true if A is "greater" (i.e., better) than B
better({S1,N1}, {S2,N2}) ->
    case S1 =:= S2 of
        true -> N1 < N2;
        false -> S1 > S2
    end.

heap_peek(HeapMap) ->
    Sz = maps:get(sz, HeapMap),
    Data = maps:get(data, HeapMap),
    element(1, Data).

heap_push(HeapMap, Elem, Comp) ->
    Sz = maps:get(sz, HeapMap),
    Data = maps:get(data, HeapMap, undefined),
    NewSz = Sz + 1,
    NewData =
        case Data of
            undefined -> erlang:make_tuple(NewSz, undefined);
            _ when tuple_size(Data) < NewSz -> erlang:append_element(Data, undefined);
            _ -> Data
        end,
    UpdatedData = setelement(NewSz, NewData, Elem),
    heapify_up(#{data => UpdatedData, sz => NewSz}, NewSz, Comp).

heap_pop(HeapMap, Comp) ->
    Sz = maps:get(sz, HeapMap),
    Data = maps:get(data, HeapMap),
    Top = element(1, Data),
    case Sz of
        1 -> {Top, #{data => undefined, sz => 0}};
        _ ->
            LastElem = element(Sz, Data),
            TmpData = setelement(1, Data, LastElem),
            NewHeapTmp = #{data => TmpData, sz => Sz - 1},
            NewHeap = heapify_down(NewHeapTmp, 1, Comp),
            {Top, NewHeap}
    end.

heapify_up(HeapMap, Index, Comp) when Index =< 1 ->
    HeapMap;
heapify_up(HeapMap, Index, Comp) ->
    ParentIdx = Index div 2,
    Data = maps:get(data, HeapMap),
    Elem = element(Index, Data),
    ParentElem = element(ParentIdx, Data),
    case Comp(Elem, ParentElem) of
        true ->
            Swapped1 = setelement(Index, Data, ParentElem),
            Swapped2 = setelement(ParentIdx, Swapped1, Elem),
            heapify_up(HeapMap#{data => Swapped2}, ParentIdx, Comp);
        false -> HeapMap
    end.

heapify_down(HeapMap, Index, Comp) ->
    Sz = maps:get(sz, HeapMap),
    Data = maps:get(data, HeapMap),
    Left = Index * 2,
    Right = Left + 1,
    if
        Left > Sz ->
            HeapMap;
        true ->
            LargerIdx =
                case Right =< Sz of
                    true ->
                        LeftElem = element(Left, Data),
                        RightElem = element(Right, Data),
                        case Comp(RightElem, LeftElem) of
                            true -> Right;
                            false -> Left
                        end;
                    false -> Left
                end,
            CurrElem = element(Index, Data),
            ChildElem = element(LargerIdx, Data),
            case Comp(ChildElem, CurrElem) of
                true ->
                    Swapped1 = setelement(Index, Data, ChildElem),
                    Swapped2 = setelement(LargerIdx, Swapped1, CurrElem),
                    heapify_down(HeapMap#{data => Swapped2}, LargerIdx, Comp);
                false -> HeapMap
            end
    end.
```

## Elixir

```elixir
defmodule SORTracker do
  defmodule Heap do
    @type t :: %{data: list(), cmp: (any, any -> boolean)}

    @spec new((any, any -> boolean)) :: t()
    def new(cmp) when is_function(cmp, 2), do: %{data: [], cmp: cmp}

    @spec size(t()) :: non_neg_integer()
    def size(%{data: d}), do: length(d)

    @spec peek(t()) :: any | nil
    def peek(%{data: []}), do: nil
    def peek(%{data: [root | _]}), do: root

    @spec push(t(), any) :: t()
    def push(%{data: d, cmp: cmp} = heap, item) do
      d = d ++ [item]
      idx = length(d) - 1
      {d, _} = bubble_up(d, idx, cmp)
      %{heap | data: d}
    end

    @spec pop(t()) :: {any, t()}
    def pop(%{data: []} = heap), do: {nil, heap}
    def pop(%{data: [_root] , cmp: cmp} = heap) do
      {Enum.at(heap.data, 0), %{heap | data: []}}
    end
    def pop(%{data: d, cmp: cmp} = heap) do
      root = Enum.at(d, 0)
      last = List.last(d)
      d = List.replace_at(d, 0, last)
      d = :lists.sublist(d, length(d) - 1)
      {d, _} = bubble_down(d, 0, cmp)
      {root, %{heap | data: d}}
    end

    defp parent(idx), do: div(idx - 1, 2)

    defp left_child(idx), do: idx * 2 + 1
    defp right_child(idx), do: idx * 2 + 2

    defp bubble_up(d, 0, _cmp), do: {d, 0}
    defp bubble_up(d, idx, cmp) do
      p = parent(idx)
      if cmp.(Enum.at(d, idx), Enum.at(d, p)) do
        d = swap(d, idx, p)
        bubble_up(d, p, cmp)
      else
        {d, idx}
      end
    end

    defp bubble_down(d, idx, cmp) do
      l = left_child(idx)
      r = right_child(idx)
      size = length(d)

      largest =
        cond do
          l < size and cmp.(Enum.at(d, l), Enum.at(d, idx)) -> l
          true -> idx
        end

      largest =
        if r < size and cmp.(Enum.at(d, r), Enum.at(d, largest)) do
          r
        else
          largest
        end

      if largest != idx do
        d = swap(d, idx, largest)
        bubble_down(d, largest, cmp)
      else
        {d, idx}
      end
    end

    defp swap(list, i, j) do
      vi = Enum.at(list, i)
      vj = Enum.at(list, j)
      list
      |> List.replace_at(i, vj)
      |> List.replace_at(j, vi)
    end
  end

  @spec init_() :: any()
  def init_() do
    left_cmp = fn a, b -> worse?(a, b) end
    right_cmp = fn a, b -> better?(a, b) end

    state = %{
      left: Heap.new(left_cmp),
      right: Heap.new(right_cmp),
      k: 0
    }

    Process.put(:sor_state, state)
  end

  @spec add(name :: String.t(), score :: integer) :: any()
  def add(name, score) do
    state = Process.get(:sor_state)

    item = %{name: name, score: score}
    left = Heap.push(state.left, item)

    {left, right} =
      if Heap.size(left) > state.k + 1 do
        {worst, new_left} = Heap.pop(left)
        {new_left, Heap.push(state.right, worst)}
      else
        {left, state.right}
      end

    Process.put(:sor_state, %{state | left: left, right: right})
  end

  @spec get() :: String.t()
  def get() do
    state = Process.get(:sor_state)

    {top, new_left} = Heap.pop(state.left)
    result = top.name

    {new_left, new_right, new_k} =
      if Heap.size(state.right) > 0 do
        {best, new_right} = Heap.pop(state.right)
        {Heap.push(new_left, best), new_right, state.k + 1}
      else
        {new_left, state.right, state.k + 1}
      end

    Process.put(:sor_state, %{left: new_left, right: new_right, k: new_k})
    result
  end

  # Helper comparison functions
  defp better?(%{score: s1, name: n1}, %{score: s2, name: n2}) do
    if s1 != s2, do: s1 > s2, else: n1 < n2
  end

  defp worse?(a, b), do: not better?(a, b)
end
```
