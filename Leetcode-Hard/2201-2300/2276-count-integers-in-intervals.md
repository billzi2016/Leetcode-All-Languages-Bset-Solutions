# 2276. Count Integers in Intervals

## Cpp

```cpp
class CountIntervals {
public:
    CountIntervals() : total(0) {}
    
    void add(int left, int right) {
        int L = left;
        int R = right;
        // Find first interval with start >= L
        auto it = intervals.lower_bound(L);
        // Check previous interval for possible overlap/touch
        if (it != intervals.begin()) {
            auto prev = std::prev(it);
            if ((long long)prev->second >= (long long)L - 1) {
                L = std::min(L, prev->first);
                R = std::max(R, prev->second);
                total -= (long long)(prev->second - prev->first + 1);
                intervals.erase(prev);
            }
        }
        // Merge all overlapping/touching intervals starting from it
        it = intervals.lower_bound(L);
        while (it != intervals.end() && (long long)it->first <= (long long)R + 1) {
            L = std::min(L, it->first);
            R = std::max(R, it->second);
            total -= (long long)(it->second - it->first + 1);
            auto eraseIt = it++;
            intervals.erase(eraseIt);
        }
        // Insert the merged interval
        intervals[L] = R;
        total += (long long)(R - L + 1);
    }
    
    int count() {
        return (int)total;
    }
private:
    std::map<int, int> intervals; // start -> end, non‑overlapping
    long long total;
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */
```

## Java

```java
class CountIntervals {
    private final java.util.TreeMap<Integer, Integer> intervals;
    private long total;

    public CountIntervals() {
        intervals = new java.util.TreeMap<>();
        total = 0L;
    }

    public void add(int left, int right) {
        int start = left;
        int end = right;

        // Merge with the interval that may overlap on the left
        java.util.Map.Entry<Integer, Integer> lower = intervals.floorEntry(start);
        if (lower != null && lower.getValue() >= start - 1) {
            start = Math.min(start, lower.getKey());
            end = Math.max(end, lower.getValue());
            total -= (long) lower.getValue() - lower.getKey() + 1;
            intervals.remove(lower.getKey());
        }

        // Merge with all overlapping/adjacent intervals on the right
        java.util.Map.Entry<Integer, Integer> entry = intervals.ceilingEntry(start);
        while (entry != null && entry.getKey() <= end + 1) {
            start = Math.min(start, entry.getKey());
            end = Math.max(end, entry.getValue());
            total -= (long) entry.getValue() - entry.getKey() + 1;
            intervals.remove(entry.getKey());
            entry = intervals.ceilingEntry(start);
        }

        // Insert the merged interval
        intervals.put(start, end);
        total += (long) end - start + 1;
    }

    public int count() {
        return (int) total;
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = new CountIntervals();
 * obj.add(left,right);
 * int param_2 = obj.count();
 */
```

## Python

```python
import bisect

class CountIntervals(object):
    def __init__(self):
        self.intervals = []  # each element is [left, right]
        self.total = 0

    def add(self, left, right):
        new_l, new_r = left, right
        i = bisect.bisect_left(self.intervals, [left, -float('inf')])

        # Merge with previous intervals that overlap
        while i > 0 and self.intervals[i - 1][1] >= new_l:
            prev = self.intervals.pop(i - 1)
            self.total -= (prev[1] - prev[0] + 1)
            new_l = min(new_l, prev[0])
            new_r = max(new_r, prev[1])
            i -= 1

        # Merge with following intervals that overlap
        while i < len(self.intervals) and self.intervals[i][0] <= new_r:
            cur = self.intervals.pop(i)
            self.total -= (cur[1] - cur[0] + 1)
            new_l = min(new_l, cur[0])
            new_r = max(new_r, cur[1])

        # Insert the merged interval
        self.intervals.insert(i, [new_l, new_r])
        self.total += (new_r - new_l + 1)

    def count(self):
        return self.total
```

## Python3

```python
import bisect

class CountIntervals:
    def __init__(self):
        self.intervals = []          # list of [left, right], non‑overlapping & sorted
        self.total = 0               # total count of covered integers

    def add(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.intervals, [left, -float('inf')])
        start, end = left, right

        # merge with intervals on the left that overlap or touch
        j = i - 1
        while j >= 0 and self.intervals[j][1] + 1 >= start:
            s, e = self.intervals[j]
            start = min(start, s)
            end = max(end, e)
            self.total -= (e - s + 1)
            del self.intervals[j]
            i -= 1
            j -= 1

        # merge with intervals on the right that overlap or touch
        while i < len(self.intervals) and self.intervals[i][0] - 1 <= end:
            s, e = self.intervals[i]
            start = min(start, s)
            end = max(end, e)
            self.total -= (e - s + 1)
            del self.intervals[i]

        # insert the merged interval
        self.intervals.insert(i, [start, end])
        self.total += (end - start + 1)

    def count(self) -> int:
        return self.total
```

## C

```c
#include <stdlib.h>
#include <time.h>

typedef struct Node {
    int l;
    int r;
    unsigned pri;
    struct Node *left, *right;
} Node;

typedef struct {
    Node* root;
    long long total;
} CountIntervals;

/* Treap utilities */
static Node* newNode(int l, int r) {
    Node* n = (Node*)malloc(sizeof(Node));
    n->l = l;
    n->r = r;
    n->pri = ((unsigned)rand() << 16) ^ (unsigned)rand();
    n->left = n->right = NULL;
    return n;
}

static void split(Node* root, int key, Node** left, Node** right) {
    if (!root) {
        *left = *right = NULL;
    } else if (root->l < key) {
        split(root->right, key, &root->right, right);
        *left = root;
    } else {
        split(root->left, key, left, &root->left);
        *right = root;
    }
}

static Node* merge(Node* left, Node* right) {
    if (!left || !right) return left ? left : right;
    if (left->pri > right->pri) {
        left->right = merge(left->right, right);
        return left;
    } else {
        right->left = merge(left, right->left);
        return right;
    }
}

static void freeTree(Node* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

/* Traverse to collect min left, max right and total length */
static void traverse(Node* root, int* minL, int* maxR, long long* sum) {
    if (!root) return;
    if (root->l < *minL) *minL = root->l;
    if (root->r > *maxR) *maxR = root->r;
    *sum += (long long)(root->r - root->l + 1);
    traverse(root->left, minL, maxR, sum);
    traverse(root->right, minL, maxR, sum);
}

/* API implementations */
CountIntervals* countIntervalsCreate() {
    static int seeded = 0;
    if (!seeded) {
        srand((unsigned)time(NULL));
        seeded = 1;
    }
    CountIntervals* obj = (CountIntervals*)malloc(sizeof(CountIntervals));
    obj->root = NULL;
    obj->total = 0;
    return obj;
}

void countIntervalsAdd(CountIntervals* obj, int L, int R) {
    Node *leftPart, *midRight, *rightPart;
    split(obj->root, L, &leftPart, &midRight);

    /* Check possible overlap with the rightmost interval in leftPart */
    if (leftPart) {
        Node* cur = leftPart;
        while (cur->right) cur = cur->right;
        if (cur->r >= L) {
            Node *a, *b;
            split(leftPart, cur->l, &a, &b);
            Node *c, *d;
            split(b, cur->l + 1, &c, &d);   // c is the overlapping node
            obj->total -= (long long)(cur->r - cur->l + 1);
            freeTree(c);
            leftPart = a;
            if (cur->l < L) L = cur->l;
            if (cur->r > R) R = cur->r;
        }
    }

    /* Split intervals that start within [L, R] */
    split(midRight, R + 1, &midRight, &rightPart);
    if (midRight) {
        int minL = L, maxR = R;
        long long sum = 0;
        traverse(midRight, &minL, &maxR, &sum);
        obj->total -= sum;
        freeTree(midRight);
        L = minL;
        R = maxR;
    }

    Node* newNodeInterval = newNode(L, R);
    obj->total += (long long)(R - L + 1);

    Node* merged = merge(leftPart, newNodeInterval);
    obj->root = merge(merged, rightPart);
}

int countIntervalsCount(CountIntervals* obj) {
    return (int)obj->total;
}

void countIntervalsFree(CountIntervals* obj) {
    if (!obj) return;
    freeTree(obj->root);
    free(obj);
}

/**
 * Your CountIntervals struct will be instantiated and called as such:
 * CountIntervals* obj = countIntervalsCreate();
 * countIntervalsAdd(obj, left, right);
 *
 * int param_2 = countIntervalsCount(obj);
 *
 * countIntervalsFree(obj);
 */
```

## Csharp

```csharp
public class CountIntervals {
    private class Node {
        public int l, r;
        public int pri;
        public Node left, right;
        public Node(int l, int r) {
            this.l = l;
            this.r = r;
            pri = _rand.Next();
        }
    }

    private static readonly Random _rand = new Random();

    private Node _root;
    private long _total;

    public CountIntervals() {
        _root = null;
        _total = 0;
    }

    public void Add(int left, int right) {
        int newL = left, newR = right;

        // Split by left: nodes with start < left go to leftTree
        Split(_root, left, out Node leftTree, out Node rest);

        // Check predecessor interval in leftTree
        if (leftTree != null) {
            Node pred = GetMax(leftTree);
            if (pred.r >= left) {
                newL = Math.Min(newL, pred.l);
                newR = Math.Max(newR, pred.r);
                _total -= (long)(pred.r - pred.l + 1);
                leftTree = Delete(leftTree, pred.l);
            }
        }

        // Split rest by right+1: nodes with start in [left, right] go to midTree
        Split(rest, right + 1, out Node midTree, out Node rightTree);

        if (midTree != null) {
            var stack = new System.Collections.Generic.Stack<Node>();
            Node cur = midTree;
            while (cur != null || stack.Count > 0) {
                while (cur != null) {
                    stack.Push(cur);
                    cur = cur.left;
                }
                Node node = stack.Pop();
                newL = Math.Min(newL, node.l);
                newR = Math.Max(newR, node.r);
                _total -= (long)(node.r - node.l + 1);
                cur = node.right;
            }
        }

        // Insert merged interval
        Node merged = new Node(newL, newR);
        _total += (long)(newR - newL + 1);

        _root = Merge(leftTree, merged);
        _root = Merge(_root, rightTree);
    }

    public int Count() {
        return (int)_total;
    }

    // Treap split: left keys < key, right keys >= key
    private static void Split(Node cur, int key, out Node left, out Node right) {
        if (cur == null) {
            left = right = null;
            return;
        }
        if (cur.l < key) {
            Split(cur.right, key, out Node ltemp, out right);
            cur.right = ltemp;
            left = cur;
        } else {
            Split(cur.left, key, out left, out Node rtemp);
            cur.left = rtemp;
            right = cur;
        }
    }

    private static Node Merge(Node a, Node b) {
        if (a == null) return b;
        if (b == null) return a;
        if (a.pri > b.pri) {
            a.right = Merge(a.right, b);
            return a;
        } else {
            b.left = Merge(a, b.left);
            return b;
        }
    }

    private static Node Delete(Node cur, int key) {
        if (cur == null) return null;
        if (key < cur.l) {
            cur.left = Delete(cur.left, key);
            return cur;
        } else if (key > cur.l) {
            cur.right = Delete(cur.right, key);
            return cur;
        } else {
            return Merge(cur.left, cur.right);
        }
    }

    private static Node GetMax(Node node) {
        while (node.right != null) node = node.right;
        return node;
    }
}
```

## Javascript

```javascript
var CountIntervals = function() {
    this.intervals = []; // sorted by start
    this.total = 0;
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
CountIntervals.prototype.add = function(left, right) {
    const intervals = this.intervals;
    // binary search for first interval with start >= left
    let lo = 0, hi = intervals.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (intervals[mid][0] < left) lo = mid + 1;
        else hi = mid;
    }
    let startIdx = lo;
    // check previous interval for overlap
    if (startIdx - 1 >= 0 && intervals[startIdx - 1][1] >= left) {
        startIdx--;
    }
    let endIdx = startIdx;
    // expand forward while overlapping with right
    while (endIdx < intervals.length && intervals[endIdx][0] <= right) {
        endIdx++;
    }
    // merge intervals in [startIdx, endIdx)
    let newL = left, newR = right;
    for (let i = startIdx; i < endIdx; i++) {
        const iv = intervals[i];
        newL = Math.min(newL, iv[0]);
        newR = Math.max(newR, iv[1]);
        this.total -= (iv[1] - iv[0] + 1);
    }
    // replace the overlapped range with the merged interval
    intervals.splice(startIdx, endIdx - startIdx, [newL, newR]);
    this.total += (newR - newL + 1);
};

/**
 * @return {number}
 */
CountIntervals.prototype.count = function() {
    return this.total;
};
```

## Typescript

```typescript
class Node {
    key: number;
    l: number;
    r: number;
    prio: number;
    left: Node | null = null;
    right: Node | null = null;
    constructor(key: number, l: number, r: number) {
        this.key = key;
        this.l = l;
        this.r = r;
        this.prio = Math.random();
    }
}
function split(root: Node | null, key: number): [Node | null, Node | null] {
    if (!root) return [null, null];
    if (key < root.key) {
        const [l, r] = split(root.left, key);
        root.left = r;
        return [l, root];
    } else {
        const [l, r] = split(root.right, key);
        root.right = l;
        return [root, r];
    }
}
function merge(a: Node | null, b: Node | null): Node | null {
    if (!a) return b;
    if (!b) return a;
    if (a.prio > b.prio) {
        a.right = merge(a.right, b);
        return a;
    } else {
        b.left = merge(a, b.left);
        return b;
    }
}
function insert(root: Node | null, node: Node): Node {
    if (!root) return node;
    if (node.prio > root.prio) {
        const [l, r] = split(root, node.key);
        node.left = l;
        node.right = r;
        return node;
    } else if (node.key < root.key) {
        root.left = insert(root.left, node);
    } else {
        root.right = insert(root.right, node);
    }
    return root;
}
function erase(root: Node | null, key: number): Node | null {
    if (!root) return null;
    if (key < root.key) {
        root.left = erase(root.left, key);
        return root;
    } else if (key > root.key) {
        root.right = erase(root.right, key);
        return root;
    } else {
        return merge(root.left, root.right);
    }
}
function lowerBound(root: Node | null, key: number): Node | null {
    let cur = root;
    let ans: Node | null = null;
    while (cur) {
        if (cur.key >= key) {
            ans = cur;
            cur = cur.left;
        } else {
            cur = cur.right;
        }
    }
    return ans;
}
function predecessor(root: Node | null, key: number): Node | null {
    let cur = root;
    let ans: Node | null = null;
    while (cur) {
        if (cur.key <= key) {
            ans = cur;
            cur = cur.right;
        } else {
            cur = cur.left;
        }
    }
    return ans;
}
function successor(root: Node | null, key: number): Node | null {
    let cur = root;
    let ans: Node | null = null;
    while (cur) {
        if (cur.key > key) {
            ans = cur;
            cur = cur.left;
        } else {
            cur = cur.right;
        }
    }
    return ans;
}
class CountIntervals {
    private root: Node | null = null;
    private total: number = 0;

    constructor() {}

    add(left: number, right: number): void {
        let newL = left;
        let newR = right;

        // Check predecessor for overlap
        const pred = predecessor(this.root, left);
        if (pred && pred.r >= left) {
            newL = Math.min(newL, pred.l);
            newR = Math.max(newR, pred.r);
            this.total -= pred.r - pred.l + 1;
            this.root = erase(this.root, pred.key);
        }

        // Merge all overlapping successors
        let node = lowerBound(this.root, left);
        while (node && node.l <= newR) {
            newL = Math.min(newL, node.l);
            newR = Math.max(newR, node.r);
            this.total -= node.r - node.l + 1;
            const next = successor(this.root, node.key);
            this.root = erase(this.root, node.key);
            node = next;
        }

        // Insert merged interval
        const newNode = new Node(newL, newL, newR);
        this.root = insert(this.root, newNode);
        this.total += newR - newL + 1;
    }

    count(): number {
        return this.total;
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * var obj = new CountIntervals()
 * obj.add(left,right)
 * var param_2 = obj.count()
 */
```

## Php

```php
class CountIntervals {
    private $intervals;
    private $total;

    function __construct() {
        $this->intervals = [];
        $this->total = 0;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function add($left, $right) {
        // Find first interval with start >= left using binary search
        $n = count($this->intervals);
        $lo = 0;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->intervals[$mid][0] < $left) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        $i = $lo; // insertion position

        $newL = $left;
        $newR = $right;
        $removeStart = $i;

        // Check previous interval for overlap
        if ($i > 0 && $this->intervals[$i - 1][1] >= $left) {
            $removeStart = $i - 1;
        }

        $removedLen = 0;
        $idx = $removeStart;
        $cnt = count($this->intervals);
        while ($idx < $cnt) {
            $cur = $this->intervals[$idx];
            if ($cur[0] > $newR) {
                break; // no more overlap
            }
            // Overlapping interval
            $removedLen += $cur[1] - $cur[0] + 1;
            if ($cur[0] < $newL) $newL = $cur[0];
            if ($cur[1] > $newR) $newR = $cur[1];
            $idx++;
        }
        $removeCount = $idx - $removeStart;

        // Replace overlapped intervals with the merged one
        array_splice($this->intervals, $removeStart, $removeCount, [[$newL, $newR]]);

        // Update total count
        $this->total = $this->total - $removedLen + ($newR - $newL + 1);
    }

    /**
     * @return Integer
     */
    function count() {
        return $this->total;
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * $obj = new CountIntervals();
 * $obj->add($left, $right);
 * $ret_2 = $obj->count();
 */
```

## Swift

```swift
class CountIntervals {
    private class Node {
        var l: Int
        var r: Int
        var pri: Int
        var left: Node?
        var right: Node?
        init(_ l: Int, _ r: Int) {
            self.l = l
            self.r = r
            self.pri = Int.random(in: Int.min...Int.max)
        }
    }
    
    private var root: Node?
    private var total = 0
    
    init() {}
    
    func add(_ left: Int, _ right: Int) {
        var newL = left
        var newR = right
        
        // split by left
        var (t1, t2) = split(root, left)
        
        // check predecessor interval that may overlap
        if let pred = getMax(t1), pred.r >= left {
            newL = min(newL, pred.l)
            newR = max(newR, pred.r)
            total -= (pred.r - pred.l + 1)
            t1 = erase(t1, pred.l)
        }
        
        // split right part by right+1
        var (tMid, t3) = split(t2, right + 1)
        
        // merge intervals inside tMid
        if let minNode = getMin(tMid) {
            newL = min(newL, minNode.l)
        }
        if let maxNode = getMax(tMid) {
            newR = max(newR, maxNode.r)
        }
        func subtract(_ node: Node?) {
            guard let node = node else { return }
            total -= (node.r - node.l + 1)
            subtract(node.left)
            subtract(node.right)
        }
        subtract(tMid)
        
        // create merged interval
        let newNode = Node(newL, newR)
        total += (newR - newL + 1)
        
        var merged = merge(t1, newNode)
        merged = merge(merged, t3)
        root = merged
    }
    
    func count() -> Int {
        return total
    }
    
    // Treap operations
    
    private func split(_ node: Node?, _ key: Int) -> (Node?, Node?) {
        guard let node = node else { return (nil, nil) }
        if node.l < key {
            let (a, b) = split(node.right, key)
            node.right = a
            return (node, b)
        } else {
            let (a, b) = split(node.left, key)
            node.left = b
            return (a, node)
        }
    }
    
    private func merge(_ left: Node?, _ right: Node?) -> Node? {
        guard let left = left else { return right }
        guard let right = right else { return left }
        if left.pri > right.pri {
            left.right = merge(left.right, right)
            return left
        } else {
            right.left = merge(left, right.left)
            return right
        }
    }
    
    private func erase(_ node: Node?, _ key: Int) -> Node? {
        guard let node = node else { return nil }
        if key < node.l {
            node.left = erase(node.left, key)
            return node
        } else if key > node.l {
            node.right = erase(node.right, key)
            return node
        } else {
            return merge(node.left, node.right)
        }
    }
    
    private func getMax(_ node: Node?) -> Node? {
        var cur = node
        while let right = cur?.right {
            cur = right
        }
        return cur
    }
    
    private func getMin(_ node: Node?) -> Node? {
        var cur = node
        while let left = cur?.left {
            cur = left
        }
        return cur
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * let obj = CountIntervals()
 * obj.add(left, right)
 * let ret_2: Int = obj.count()
 */
```

## Kotlin

```kotlin
import java.util.TreeMap
import kotlin.math.max
import kotlin.math.min

class CountIntervals() {
    private val intervals = TreeMap<Int, Int>()
    private var total: Long = 0

    fun add(left: Int, right: Int) {
        var l = left
        var r = right

        // Merge with the interval that may start before 'l' and overlap
        val lower = intervals.floorEntry(l)
        if (lower != null && lower.value >= l) {
            l = min(lower.key, l)
            r = max(lower.value, r)
            total -= (lower.value - lower.key + 1).toLong()
            intervals.remove(lower.key)
        }

        // Merge with all overlapping intervals that start at or after 'l'
        var entry = intervals.ceilingEntry(l)
        while (entry != null && entry.key <= r) {
            l = min(entry.key, l)
            r = max(entry.value, r)
            total -= (entry.value - entry.key + 1).toLong()
            intervals.remove(entry.key)
            entry = intervals.ceilingEntry(l)
        }

        intervals[l] = r
        total += (r - l + 1).toLong()
    }

    fun count(): Int {
        return total.toInt()
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * var obj = CountIntervals()
 * obj.add(left,right)
 * var param_2 = obj.count()
 */
```

## Dart

```dart
class Interval {
  int left;
  int right;
  Interval(this.left, this.right);
}

class CountIntervals {
  final List<Interval> _intervals = [];
  int _total = 0;

  CountIntervals();

  void add(int left, int right) {
    // Find insertion point for 'left' using binary search.
    int idx = _lowerBound(left);
    int newLeft = left;
    int newRight = right;
    int removeStart = idx;
    // Check overlap with previous interval.
    if (idx > 0 && _intervals[idx - 1].right >= left) {
      Interval prev = _intervals[idx - 1];
      newLeft = prev.left < newLeft ? prev.left : newLeft;
      newRight = prev.right > newRight ? prev.right : newRight;
      _total -= (prev.right - prev.left + 1);
      removeStart = idx - 1;
    }
    // Merge all following overlapping intervals.
    int i = idx;
    while (i < _intervals.length && _intervals[i].left <= newRight) {
      Interval cur = _intervals[i];
      if (cur.left < newLeft) newLeft = cur.left;
      if (cur.right > newRight) newRight = cur.right;
      _total -= (cur.right - cur.left + 1);
      i++;
    }
    // Remove overlapped intervals.
    if (removeStart < i) {
      _intervals.removeRange(removeStart, i);
    }
    // Insert the merged interval.
    _intervals.insert(removeStart, Interval(newLeft, newRight));
    _total += (newRight - newLeft + 1);
  }

  int count() => _total;

  int _lowerBound(int target) {
    int lo = 0;
    int hi = _intervals.length;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (_intervals[mid].left < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals obj = CountIntervals();
 * obj.add(left,right);
 * int param2 = obj.count();
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type node struct {
	l, r    int
	left    *node
	right   *node
	priority uint32
}

func rotateRight(y *node) *node {
	x := y.left
	y.left = x.right
	x.right = y
	return x
}

func rotateLeft(x *node) *node {
	y := x.right
	x.right = y.left
	y.left = x
	return y
}

func insert(root, nd *node) *node {
	if root == nil {
		return nd
	}
	if nd.l < root.l {
		root.left = insert(root.left, nd)
		if root.left.priority < root.priority {
			root = rotateRight(root)
		}
	} else {
		root.right = insert(root.right, nd)
		if root.right.priority < root.priority {
			root = rotateLeft(root)
		}
	}
	return root
}

func merge(a, b *node) *node {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.priority < b.priority {
		a.right = merge(a.right, b)
		return a
	}
	b.left = merge(a, b.left)
	return b
}

func deleteNode(root *node, key int) *node {
	if root == nil {
		return nil
	}
	if key < root.l {
		root.left = deleteNode(root.left, key)
	} else if key > root.l {
		root.right = deleteNode(root.right, key)
	} else {
		return merge(root.left, root.right)
	}
	return root
}

func lowerBound(root *node, key int) *node {
	var res *node
	for root != nil {
		if root.l >= key {
			res = root
			root = root.left
		} else {
			root = root.right
		}
	}
	return res
}

func predecessor(root *node, key int) *node {
	var res *node
	for root != nil {
		if root.l <= key {
			res = root
			root = root.right
		} else {
			root = root.left
		}
	}
	return res
}

func successor(root *node, key int) *node {
	var res *node
	for root != nil {
		if root.l > key {
			res = root
			root = root.left
		} else {
			root = root.right
		}
	}
	return res
}

type CountIntervals struct {
	root  *node
	total int64
	rng   *rand.Rand
}

func Constructor() CountIntervals {
	src := rand.NewSource(time.Now().UnixNano())
	return CountIntervals{
		root: nil,
		total: 0,
		rng: rand.New(src),
	}
}

func min(a, b int) int {
	if a < b { return a }
	return b
}
func max(a, b int) int {
	if a > b { return a }
	return b
}

func (this *CountIntervals) Add(left int, right int)  {
	newL, newR := left, right

	// Check predecessor for possible overlap
	pred := predecessor(this.root, left)
	if pred != nil && pred.r >= left {
		newL = min(newL, pred.l)
		newR = max(newR, pred.r)
		this.total -= int64(pred.r - pred.l + 1)
		this.root = deleteNode(this.root, pred.l)
	}

	// Merge all overlapping intervals starting from lower bound
	cur := lowerBound(this.root, left)
	for cur != nil && cur.l <= newR {
		nextKey := cur.l
		newL = min(newL, cur.l)
		newR = max(newR, cur.r)
		this.total -= int64(cur.r - cur.l + 1)
		this.root = deleteNode(this.root, cur.l)
		cur = successor(this.root, nextKey)
	}

	// Insert merged interval
	nd := &node{
		l: newL,
		r: newR,
		priority: this.rng.Uint32(),
	}
	this.root = insert(this.root, nd)
	this.total += int64(newR - newL + 1)
}

func (this *CountIntervals) Count() int {
	return int(this.total)
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(left,right);
 * param_2 := obj.Count();
 */
```

## Ruby

```ruby
class CountIntervals
  def initialize()
    @intervals = []
    @total = 0
  end

=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
  def add(left, right)
    idx = lower_bound(@intervals, left)
    start_idx = idx
    if idx > 0 && @intervals[idx - 1][1] >= left - 1
      start_idx = idx - 1
    end

    new_l = left
    new_r = right
    removed = 0
    i = start_idx
    while i < @intervals.length && @intervals[i][0] <= right + 1
      new_l = [new_l, @intervals[i][0]].min
      new_r = [new_r, @intervals[i][1]].max
      removed += (@intervals[i][1] - @intervals[i][0] + 1)
      i += 1
    end

    if i > start_idx
      @intervals.slice!(start_idx, i - start_idx)
    end
    @intervals.insert(start_idx, [new_l, new_r])
    added = new_r - new_l + 1
    @total += added - removed
  end

=begin
    :rtype: Integer
=end
  def count()
    @total
  end

  private

  def lower_bound(arr, target)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid][0] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end
```

## Scala

```scala
import java.util.TreeMap
import java.util.Map.Entry

class CountIntervals() {

  private val intervals = new TreeMap[Long, Long]()
  private var total: Long = 0L

  def add(left: Int, right: Int): Unit = {
    var l = left.toLong
    var r = right.toLong

    // Merge with interval that may start before l
    var entry = intervals.floorEntry(l)
    if (entry != null && entry.getValue >= l - 1) {
      l = Math.min(l, entry.getKey)
      r = Math.max(r, entry.getValue)
      total -= (entry.getValue - entry.getKey + 1)
      intervals.remove(entry.getKey)
    }

    // Merge with all intervals that start within the new range
    entry = intervals.ceilingEntry(l)
    while (entry != null && entry.getKey <= r + 1) {
      l = Math.min(l, entry.getKey)
      r = Math.max(r, entry.getValue)
      total -= (entry.getValue - entry.getKey + 1)
      val next = intervals.higherEntry(entry.getKey)
      intervals.remove(entry.getKey)
      entry = next
    }

    // Insert merged interval
    intervals.put(l, r)
    total += (r - l + 1)
  }

  def count(): Int = {
    total.toInt
  }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * val obj = new CountIntervals()
 * obj.add(left,right)
 * val param_2 = obj.count()
 */
```

## Rust

```rust
use std::cell::{Cell, RefCell};
use std::collections::BTreeMap;
use std::ops::Bound::{Included, Unbounded};

struct CountIntervals {
    intervals: RefCell<BTreeMap<i32, i32>>,
    total: Cell<i64>,
}

impl CountIntervals {
    fn new() -> Self {
        CountIntervals {
            intervals: RefCell::new(BTreeMap::new()),
            total: Cell::new(0),
        }
    }

    fn add(&self, left: i32, right: i32) {
        let mut map = self.intervals.borrow_mut();
        let mut new_left = left as i64;
        let mut new_right = right as i64;
        let mut remove_keys: Vec<i32> = Vec::new();

        // Check possible overlapping interval that starts before `left`
        if let Some((&s, &e)) = map.range((Unbounded, Included(&left))).next_back() {
            if e >= left && s < left {
                new_left = new_left.min(s as i64);
                new_right = new_right.max(e as i64);
                remove_keys.push(s);
            }
        }

        // Collect keys of intervals that start within [left, right]
        let candidate_keys: Vec<i32> = map
            .range((Included(&left), Included(&i32::MAX)))
            .map(|(&k, _)| k)
            .collect();

        for s in candidate_keys {
            if let Some(&e) = map.get(&s) {
                if s > right {
                    break;
                }
                // Overlap guaranteed because start <= right and e >= left (otherwise it wouldn't be overlapping)
                new_left = new_left.min(s as i64);
                new_right = new_right.max(e as i64);
                remove_keys.push(s);
            }
        }

        // Update total by removing lengths of overlapped intervals
        let mut total_val = self.total.get();
        for &k in &remove_keys {
            if let Some(&e) = map.get(&k) {
                total_val -= (e as i64 - k as i64 + 1);
            }
        }

        // Remove the old intervals
        for k in remove_keys.iter() {
            map.remove(k);
        }

        // Insert merged interval and update total
        let nl = new_left as i32;
        let nr = new_right as i32;
        map.insert(nl, nr);
        total_val += (nr as i64 - nl as i64 + 1);
        self.total.set(total_val);
    }

    fn count(&self) -> i32 {
        self.total.get() as i32
    }
}

/**
 * Your CountIntervals object will be instantiated and called as such:
 * let obj = CountIntervals::new();
 * obj.add(left, right);
 * let ret_2: i32 = obj.count();
 */
```

## Racket

```racket
(define count-intervals%
  (class object%
    (super-new)
    ;; internal fields
    (define root #f)          ; treap root
    (define total 0)          ; total covered integers

    ;; node structure for treap
    (struct:node (key end priority left right) #:transparent)

    ;; helper to create a node
    (define (make-node k e p l r)
      (node k e p l r))

    ;; split treap into (< key) and (>= key)
    (define (split t key)
      (if (not t)
          (values #f #f)
          (let ((k (node-key t)))
            (if (< k key)
                (let-values ([(l r) (split (node-right t) key)])
                  (values (make-node k (node-end t) (node-priority t) (node-left t) l) r))
                (let-values ([(l r) (split (node-left t) key)])
                  (values l (make-node k (node-end t) (node-priority t) r (node-right t))))))))

    ;; merge two treaps where all keys in a < keys in b
    (define (merge a b)
      (cond [(not a) b]
            [(not b) a]
            [else (if (< (node-priority a) (node-priority b))
                      (make-node (node-key a) (node-end a) (node-priority a)
                                 (node-left a)
                                 (merge (node-right a) b))
                      (make-node (node-key b) (node-end b) (node-priority b)
                                 (merge a (node-left b))
                                 (node-right b)))]))

    ;; find node with maximum key in treap
    (define (max-node t)
      (if (not t) #f
          (let loop ((cur t))
            (if (node-right cur)
                (loop (node-right cur))
                cur))))

    ;; collect total length and maximal end value from a subtree
    (define (collect-info t)
      (if (not t)
          (values 0 -inf.0)
          (let-values ([(lenL maxL) (collect-info (node-left t))]
                       [(lenR maxR) (collect-info (node-right t))])
            (define cur-len (+ (- (node-end t) (node-key t)) 1))
            (values (+ lenL cur-len lenR)
                    (max (node-end t) (max maxL maxR))))))

    ;; public methods
    (define/public (add left right)
      (let* ((L left) (R right))
        ;; split root into parts < L and >= L
        (define-values (left-part right-part) (split root L))

        ;; check predecessor in left-part for possible overlap/adjacency
        (let ((pred (max-node left-part)))
          (when pred
            (when (>= (node-end pred) (- L 1))
              ;; merge with predecessor
              (set! L (min L (node-key pred)))
              (set! R (max R (node-end pred)))
              ;; subtract its contribution from total
              (set! total (- total (+ (- (node-end pred) (node-key pred)) 1)))
              ;; remove predecessor node from left-part
              (define-values (less tmp) (split left-part (node-key pred))) ; less < pred.key, tmp >= pred.key
              (define-values (_ new-left) (split tmp (+ (node-key pred) 1))) ; _ is pred node
              (set! left-part new-left))))

        ;; split right-part at R+1 to isolate overlapping intervals
        (define splitKey (+ R 1))
        (define-values (mid right-rest) (split right-part splitKey))

        ;; process all intervals in mid (they overlap)
        (when mid
          (let-values ([(lenMid maxEndMid) (collect-info mid)])
            (set! total (- total lenMid))
            (set! R (max R maxEndMid))))

        ;; create merged interval node
        (define new-node (make-node L R (random) #f #f))
        (set! total (+ total (+ (- R L) 1)))

        ;; merge back all parts
        (set! root (merge (merge left-part new-node) right-rest))))

    (define/public (count)
      total)))
```

## Erlang

```erlang
-module(count_intervals).
-export([count_intervals_init_/0,
         count_intervals_add/2,
         count_intervals_count/0]).

-spec count_intervals_init_() -> any().
count_intervals_init_() ->
    Tab = ets:new(count_intervals_table, [ordered_set, private]),
    erlang:put(count_intervals_tab, Tab),
    erlang:put(count_intervals_total, 0),
    ok.

-spec count_intervals_add(Left :: integer(), Right :: integer()) -> any().
count_intervals_add(Left, Right) ->
    Tab = erlang:get(count_intervals_tab),
    Total0 = erlang:get(count_intervals_total),
    {NewL, NewR, NewTotal} = merge_intervals(Left, Right, Tab, Total0),
    ets:insert(Tab, {NewL, NewR}),
    erlang:put(count_intervals_total, NewTotal + (NewR - NewL + 1)),
    ok.

-spec count_intervals_count() -> integer().
count_intervals_count() ->
    erlang:get(count_intervals_total).

%% internal helpers

merge_intervals(L, R, Tab, Total) ->
    case find_overlap(L, R, Tab) of
        none ->
            {L, R, Total};
        {S, E} ->
            ets:delete(Tab, S),
            NewTotal = Total - (E - S + 1),
            NewL = if S < L -> S; true -> L end,
            NewR = if E > R -> E; true -> R end,
            merge_intervals(NewL, NewR, Tab, NewTotal)
    end.

find_overlap(L, R, Tab) ->
    case ets:prev(Tab, L) of
        '$end_of_table' ->
            find_next_overlap(L, R, Tab);
        {S, E} when E >= L - 1 ->
            {S, E};
        _Other ->
            find_next_overlap(L, R, Tab)
    end.

find_next_overlap(_L, R, Tab) ->
    case ets:next(Tab, _L - 1) of
        '$end_of_table' -> none;
        {S, E} = Obj when S =< R + 1 -> {S, E};
        _Other -> none
    end.
```

## Elixir

```elixir
defmodule CountIntervals do
  defmodule Node do
    defstruct [:key, :l, :r, :prio, :left, :right, :sum]
  end

  @spec init_() :: any
  def init_() do
    Process.put(:ci_tree, nil)
    :ok
  end

  @spec add(left :: integer, right :: integer) :: any
  def add(left, right) do
    tree = Process.get(:ci_tree)

    {left_part, rest} = split(tree, left - 1)
    {left_clean, new_l} = merge_left(left_part, left)

    {mid, right_part} = split(rest, right + 1)

    # Determine merged right bound from mid intervals
    new_r =
      case get_min_and_max_end(mid) do
        nil -> right
        {_min_start, max_end} -> max(right, max_end)
      end

    # Merge any further right intervals that become adjacent after expansion
    {right_clean, final_r} = merge_right(right_part, new_r)

    node = %Node{
      key: new_l,
      l: new_l,
      r: final_r,
      prio: :rand.uniform(1_000_000_000),
      left: nil,
      right: nil,
      sum: final_r - new_l + 1
    }

    new_tree = merge(merge(left_clean, node), right_clean)
    Process.put(:ci_tree, new_tree)
    :ok
  end

  @spec count() :: integer
  def count() do
    case Process.get(:ci_tree) do
      nil -> 0
      t -> t.sum
    end
  end

  # ---------- Treap helpers ----------
  defp sum(nil), do: 0
  defp sum(%Node{sum: s}), do: s

  defp update(nil), do: nil
  defp update(node) do
    %{node | sum: (node.r - node.l + 1) + sum(node.left) + sum(node.right)}
  end

  # split by key, left contains keys <= key
  defp split(nil, _key), do: {nil, nil}
  defp split(%Node{key: k} = root, key) when k <= key do
    {l1, r1} = split(root.right, key)
    new_root = %{root | right: l1} |> update()
    {new_root, r1}
  end
  defp split(%Node{} = root, key) do
    {l1, r1} = split(root.left, key)
    new_root = %{root | left: r1} |> update()
    {l1, new_root}
  end

  # merge two trees where all keys in a <= keys in b
  defp merge(nil, b), do: b
  defp merge(a, nil), do: a
  defp merge(%Node{prio: pa} = a, %Node{prio: pb} = b) when pa < pb do
    new_right = merge(a.right, b)
    %{a | right: new_right} |> update()
  end
  defp merge(a, %Node{} = b) do
    new_left = merge(a, b.left)
    %{b | left: new_left} |> update()
  end

  # erase node with given key
  defp erase(nil, _key), do: nil
  defp erase(%Node{key: k} = root, key) when key < k do
    new_left = erase(root.left, key)
    %{root | left: new_left} |> update()
  end
  defp erase(%Node{key: k} = root, key) when key > k do
    new_right = erase(root.right, key)
    %{root | right: new_right} |> update()
  end
  defp erase(%Node{} = root, _key), do: merge(root.left, root.right)

  # get max (rightmost) node
  defp get_max(nil), do: nil
  defp get_max(%Node{right: nil} = node), do: node
  defp get_max(%Node{right: r}), do: get_max(r)

  # get min (leftmost) node
  defp get_min(nil), do: nil
  defp get_min(%Node{left: nil} = node), do: node
  defp get_min(%Node{left: l}), do: get_min(l)

  # merge left side overlapping intervals recursively
  defp merge_left(tree, cur_l) do
    case get_max(tree) do
      nil -> {tree, cur_l}
      %Node{l: l_node, r: r_node} = node ->
        if r_node >= cur_l - 1 do
          new_l = min(l_node, cur_l)
          tree_without = erase(tree, node.key)
          merge_left(tree_without, new_l)
        else
          {tree, cur_l}
        end
    end
  end

  # merge right side overlapping intervals recursively
  defp merge_right(tree, cur_r) do
    case get_min(tree) do
      nil -> {tree, cur_r}
      %Node{l: l_node, r: r_node} = node ->
        if l_node <= cur_r + 1 do
          new_r = max(cur_r, r_node)
          tree_without = erase(tree, node.key)
          merge_right(tree_without, new_r)
        else
          {tree, cur_r}
        end
    end
  end

  # get min start and max end from a subtree (or nil)
  defp get_min_and_max_end(nil), do: nil
  defp get_min_and_max_end(tree) do
    min_node = get_min(tree)
    max_node = get_max(tree)
    {min_node.l, max_node.r}
  end
end
```
