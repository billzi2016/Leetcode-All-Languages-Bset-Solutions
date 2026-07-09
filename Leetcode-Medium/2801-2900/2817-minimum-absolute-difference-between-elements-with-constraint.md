# 2817. Minimum Absolute Difference Between Elements With Constraint

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x) {
        multiset<long long> s;
        int n = nums.size();
        int ans = INT_MAX;
        for (int j = 0; j < n; ++j) {
            if (j - x >= 0) {
                s.insert(nums[j - x]);
            }
            if (!s.empty()) {
                auto it = s.lower_bound(nums[j]);
                if (it != s.end())
                    ans = min(ans, (int)llabs(*it - nums[j]));
                if (it != s.begin()) {
                    --it;
                    ans = min(ans, (int)llabs(*it - nums[j]));
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minAbsoluteDifference(java.util.List<Integer> nums, int x) {
        java.util.TreeSet<Integer> set = new java.util.TreeSet<>();
        int n = nums.size();
        int answer = Integer.MAX_VALUE;
        for (int j = x; j < n; ++j) {
            // add the element that is exactly x positions before j
            set.add(nums.get(j - x));
            int val = nums.get(j);
            Integer floor = set.floor(val);
            if (floor != null) {
                answer = Math.min(answer, Math.abs(val - floor));
            }
            Integer ceil = set.ceiling(val);
            if (ceil != null) {
                answer = Math.min(answer, Math.abs(val - ceil));
            }
        }
        return answer;
    }
}
```

## Python

```python
import random

class TreapNode:
    __slots__ = ('key', 'prio', 'cnt', 'left', 'right')
    def __init__(self, key):
        self.key = key
        self.prio = random.randint(1, 1 << 30)
        self.cnt = 1
        self.left = None
        self.right = None

def rotate_right(p):
    q = p.left
    p.left = q.right
    q.right = p
    return q

def rotate_left(p):
    q = p.right
    p.right = q.left
    q.left = p
    return q

def insert(root, key):
    if root is None:
        return TreapNode(key)
    if key == root.key:
        root.cnt += 1
        return root
    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.prio < root.prio:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key)
        if root.right.prio < root.prio:
            root = rotate_left(root)
    return root

def lower_bound(root, key):
    res = None
    while root:
        if root.key >= key:
            res = root
            root = root.left
        else:
            root = root.right
    return res

def predecessor(root, key):
    res = None
    while root:
        if root.key < key:
            res = root
            root = root.right
        else:
            root = root.left
    return res

class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        INF = 10 ** 18
        ans = INF
        root = None
        n = len(nums)
        for j in range(x, n):
            # insert element that becomes eligible
            root = insert(root, nums[j - x])
            val = nums[j]
            node_ge = lower_bound(root, val)
            if node_ge:
                diff = node_ge.key - val
                if diff < 0:
                    diff = -diff
                if diff < ans:
                    ans = diff
            node_lt = predecessor(root, val)
            if node_lt:
                diff = val - node_lt.key
                if diff < 0:
                    diff = -diff
                if diff < ans:
                    ans = diff
        return ans
```

## Python3

```python
import random
from typing import List

class _Node:
    __slots__ = ("key", "prio", "left", "right")
    def __init__(self, key):
        self.key = key
        self.prio = random.random()
        self.left = None
        self.right = None

def _split(root, key):
    if not root:
        return (None, None)
    if root.key < key:
        l, r = _split(root.right, key)
        root.right = l
        return (root, r)
    else:
        l, r = _split(root.left, key)
        root.left = r
        return (l, root)

def _merge(a, b):
    if not a or not b:
        return a or b
    if a.prio < b.prio:
        a.right = _merge(a.right, b)
        return a
    else:
        b.left = _merge(a, b.left)
        return b

class _Treap:
    __slots__ = ("root",)
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = _Node(key)
        left, right = _split(self.root, key)
        self.root = _merge(_merge(left, node), right)

    def lower_bound(self, val):
        cur = self.root
        ans = None
        while cur:
            if cur.key >= val:
                ans = cur.key
                cur = cur.left
            else:
                cur = cur.right
        return ans

    def predecessor(self, val):
        cur = self.root
        ans = None
        while cur:
            if cur.key < val:
                ans = cur.key
                cur = cur.right
            else:
                cur = cur.left
        return ans

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        treap = _Treap()
        best = 2_000_000_000  # larger than any possible difference
        n = len(nums)
        for j in range(x, n):
            treap.insert(nums[j - x])
            v = nums[j]
            lb = treap.lower_bound(v)
            if lb is not None:
                diff = abs(lb - v)
                if diff < best:
                    best = diff
            pred = treap.predecessor(v)
            if pred is not None:
                diff = abs(pred - v)
                if diff < best:
                    best = diff
        return best
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct Node {
    int key;
    unsigned priority;
    int cnt;
    struct Node *left, *right;
} Node;

/* Xorshift RNG */
static unsigned rng_state = 2463534242U;
static unsigned next_rand() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 17;
    rng_state ^= rng_state << 5;
    return rng_state;
}

/* Rotations */
static Node* rotateRight(Node* y) {
    Node* x = y->left;
    y->left = x->right;
    x->right = y;
    return x;
}
static Node* rotateLeft(Node* x) {
    Node* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

/* Insert */
static Node* treapInsert(Node* root, int key) {
    if (!root) {
        Node* node = (Node*)malloc(sizeof(Node));
        node->key = key;
        node->priority = next_rand();
        node->cnt = 1;
        node->left = node->right = NULL;
        return node;
    }
    if (key == root->key) {
        root->cnt++;
        return root;
    } else if (key < root->key) {
        root->left = treapInsert(root->left, key);
        if (root->left->priority > root->priority)
            root = rotateRight(root);
    } else {
        root->right = treapInsert(root->right, key);
        if (root->right->priority > root->priority)
            root = rotateLeft(root);
    }
    return root;
}

/* Lower bound: first node with key >= val */
static Node* lowerBound(Node* root, int val) {
    Node* res = NULL;
    while (root) {
        if (root->key >= val) {
            res = root;
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return res;
}

/* Predecessor: max node with key < val */
static Node* predecessor(Node* root, int val) {
    Node* res = NULL;
    while (root) {
        if (root->key < val) {
            res = root;
            root = root->right;
        } else {
            root = root->left;
        }
    }
    return res;
}

int minAbsoluteDifference(int* nums, int numsSize, int x) {
    Node* treap = NULL;
    int answer = INT_MAX;

    for (int j = x; j < numsSize; ++j) {
        treap = treapInsert(treap, nums[j - x]);

        Node* succ = lowerBound(treap, nums[j]);
        if (succ) {
            int diff = succ->key - nums[j];
            if (diff < 0) diff = -diff;
            if (diff < answer) answer = diff;
        }

        Node* pred = predecessor(treap, nums[j]);
        if (pred) {
            int diff = pred->key - nums[j];
            if (diff < 0) diff = -diff;
            if (diff < answer) answer = diff;
        }
    }

    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinAbsoluteDifference(IList<int> nums, int x) {
        var set = new SortedSet<int>();
        int ans = int.MaxValue;
        for (int j = x; j < nums.Count; ++j) {
            // Add the element that becomes eligible
            set.Add(nums[j - x]);
            int cur = nums[j];
            
            // Find smallest element >= cur
            var ceilView = set.GetViewBetween(cur, int.MaxValue);
            if (ceilView.Count > 0) {
                ans = Math.Min(ans, Math.Abs(ceilView.Min - cur));
            }
            
            // Find largest element <= cur
            var floorView = set.GetViewBetween(int.MinValue, cur);
            if (floorView.Count > 0) {
                ans = Math.Min(ans, Math.Abs(floorView.Max - cur));
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minAbsoluteDifference = function(nums, x) {
    // Treap node definition
    function Node(key) {
        this.key = key;
        this.pri = Math.random();
        this.cnt = 1;          // count of duplicates
        this.left = null;
        this.right = null;
    }

    // Right rotation
    function rotateRight(y) {
        const x = y.left;
        y.left = x.right;
        x.right = y;
        return x;
    }

    // Left rotation
    function rotateLeft(x) {
        const y = x.right;
        x.right = y.left;
        y.left = x;
        return y;
    }

    // Insert key into treap rooted at root, returns new root
    function insert(root, key) {
        if (root === null) return new Node(key);
        if (key < root.key) {
            root.left = insert(root.left, key);
            if (root.left.pri > root.pri) {
                root = rotateRight(root);
            }
        } else if (key > root.key) {
            root.right = insert(root.right, key);
            if (root.right.pri > root.pri) {
                root = rotateLeft(root);
            }
        } else {
            // duplicate
            root.cnt++;
        }
        return root;
    }

    // Find node with smallest key >= target
    function lowerBound(root, target) {
        let cur = root;
        let candidate = null;
        while (cur !== null) {
            if (cur.key >= target) {
                candidate = cur;
                cur = cur.left;
            } else {
                cur = cur.right;
            }
        }
        return candidate;
    }

    // Find node with largest key < target
    function predecessor(root, target) {
        let cur = root;
        let candidate = null;
        while (cur !== null) {
            if (cur.key < target) {
                candidate = cur;
                cur = cur.right;
            } else {
                cur = cur.left;
            }
        }
        return candidate;
    }

    let ans = Infinity;
    let treapRoot = null;

    for (let j = 0; j < nums.length; ++j) {
        if (j - x >= 0) {
            treapRoot = insert(treapRoot, nums[j - x]);
        }
        if (treapRoot !== null) {
            const val = nums[j];
            const lbNode = lowerBound(treapRoot, val);
            if (lbNode !== null) {
                ans = Math.min(ans, Math.abs(lbNode.key - val));
            }
            const predNode = predecessor(treapRoot, val);
            if (predNode !== null) {
                ans = Math.min(ans, Math.abs(predNode.key - val));
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function minAbsoluteDifference(nums: number[], x: number): number {
    if (x === 0) {
        const sorted = nums.slice().sort((a, b) => a - b);
        let best = Infinity;
        for (let i = 1; i < sorted.length; ++i) {
            const diff = Math.abs(sorted[i] - sorted[i - 1]);
            if (diff < best) best = diff;
        }
        return best;
    }

    class Node {
        key: number;
        prio: number;
        left: Node | null = null;
        right: Node | null = null;
        constructor(key: number) {
            this.key = key;
            // 31-bit random priority
            this.prio = (Math.random() * 0x7fffffff) | 0;
        }
    }

    function rotateRight(y: Node): Node {
        const x = y.left!;
        y.left = x.right;
        x.right = y;
        return x;
    }

    function rotateLeft(x: Node): Node {
        const y = x.right!;
        x.right = y.left;
        y.left = x;
        return y;
    }

    function insert(root: Node | null, key: number): Node {
        if (!root) return new Node(key);
        if (key < root.key) {
            root.left = insert(root.left, key);
            if (root.left.prio > root.prio) root = rotateRight(root);
        } else {
            root.right = insert(root.right, key);
            if (root.right.prio > root.prio) root = rotateLeft(root);
        }
        return root;
    }

    function lowerBound(root: Node | null, key: number): number | undefined {
        let ans: number | undefined;
        while (root) {
            if (root.key >= key) {
                ans = root.key;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return ans;
    }

    function predecessor(root: Node | null, key: number): number | undefined {
        let ans: number | undefined;
        while (root) {
            if (root.key < key) {
                ans = root.key;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return ans;
    }

    let treap: Node | null = null;
    let best = Infinity;

    for (let j = 0; j < nums.length; ++j) {
        if (j - x >= 0) {
            treap = insert(treap, nums[j - x]);
        }
        if (treap) {
            const val = nums[j];
            const lb = lowerBound(treap, val);
            if (lb !== undefined) {
                const diff = Math.abs(lb - val);
                if (diff < best) best = diff;
            }
            const pred = predecessor(treap, val);
            if (pred !== undefined) {
                const diff = Math.abs(pred - val);
                if (diff < best) best = diff;
            }
        }
    }

    return best;
}
```

## Php

```php
class BIT {
    public int $size;
    public array $tree;

    public function __construct(int $n) {
        $this->size = $n;
        $this->tree = array_fill(0, $n + 2, 0);
    }

    public function add(int $i, int $delta): void {
        for (; $i <= $this->size; $i += $i & -$i) {
            $this->tree[$i] += $delta;
        }
    }

    public function prefixSum(int $i): int {
        $sum = 0;
        for (; $i > 0; $i -= $i & -$i) {
            $sum += $this->tree[$i];
        }
        return $sum;
    }

    // returns smallest index such that prefix sum >= k (k >= 1)
    public function findKth(int $k): int {
        $idx = 0;
        $bitMask = 1;
        while (($bitMask << 1) <= $this->size) {
            $bitMask <<= 1;
        }
        for ($d = $bitMask; $d > 0; $d >>= 1) {
            $next = $idx + $d;
            if ($next <= $this->size && $this->tree[$next] < $k) {
                $k -= $this->tree[$next];
                $idx = $next;
            }
        }
        return $idx + 1;
    }
}

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function minAbsoluteDifference($nums, $x) {
        $n = count($nums);
        if ($x == 0) {
            $sorted = $nums;
            sort($sorted);
            $ans = PHP_INT_MAX;
            for ($i = 1; $i < $n; $i++) {
                $diff = $sorted[$i] - $sorted[$i - 1];
                if ($diff < $ans) {
                    $ans = $diff;
                    if ($ans == 0) break;
                }
            }
            return $ans;
        }

        // coordinate compression
        $vals = $nums;
        sort($vals);
        $unique = array_values(array_unique($vals));
        $map = [];
        foreach ($unique as $idx => $val) {
            $map[$val] = $idx + 1; // 1‑based index for BIT
        }

        $bit = new BIT(count($unique));
        $ans = PHP_INT_MAX;

        for ($j = $x; $j < $n; $j++) {
            // insert element at position j - x
            $valInsert = $nums[$j - $x];
            $idxInsert = $map[$valInsert];
            $bit->add($idxInsert, 1);

            $target = $nums[$j];
            $idxTarget = $map[$target];

            // predecessor (largest <= target)
            $cntLe = $bit->prefixSum($idxTarget);
            if ($cntLe > 0) {
                $predIdx = $bit->findKth($cntLe);
                $diff = abs($unique[$predIdx - 1] - $target);
                if ($diff < $ans) $ans = $diff;
            }

            // successor (smallest >= target)
            $total = $bit->prefixSum($bit->size);
            $cntLt = $bit->prefixSum($idxTarget - 1);
            if ($cntLt < $total) {
                $succIdx = $bit->findKth($cntLt + 1);
                $diff = abs($unique[$succIdx - 1] - $target);
                if ($diff < $ans) $ans = $diff;
            }

            if ($ans == 0) break; // early exit
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minAbsoluteDifference(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var tree = AVLTree()
        var answer = Int.max

        for j in x..<n {
            let idxToAdd = j - x
            tree.insert(nums[idxToAdd])
            if let diff = tree.nearestDiff(to: nums[j]) {
                if diff < answer { answer = diff }
                if answer == 0 { return 0 }
            }
        }
        return answer
    }
}

private class AVLTree {
    private class Node {
        var key: Int
        var cnt: Int
        var height: Int
        var left: Node?
        var right: Node?

        init(_ key: Int) {
            self.key = key
            self.cnt = 1
            self.height = 1
        }
    }

    private var root: Node?

    func insert(_ key: Int) {
        root = insert(root, key)
    }

    private func insert(_ node: Node?, _ key: Int) -> Node? {
        guard let node = node else { return Node(key) }

        if key == node.key {
            node.cnt += 1
        } else if key < node.key {
            node.left = insert(node.left, key)
        } else {
            node.right = insert(node.right, key)
        }

        updateHeight(node)
        return balance(node)
    }

    private func height(_ node: Node?) -> Int {
        return node?.height ?? 0
    }

    private func updateHeight(_ node: Node) {
        node.height = max(height(node.left), height(node.right)) + 1
    }

    private func getBalance(_ node: Node) -> Int {
        return height(node.left) - height(node.right)
    }

    private func rotateRight(_ y: Node) -> Node {
        let x = y.left!
        let t2 = x.right

        x.right = y
        y.left = t2

        updateHeight(y)
        updateHeight(x)

        return x
    }

    private func rotateLeft(_ x: Node) -> Node {
        let y = x.right!
        let t2 = y.left

        y.left = x
        x.right = t2

        updateHeight(x)
        updateHeight(y)

        return y
    }

    private func balance(_ node: Node) -> Node {
        let bf = getBalance(node)

        // Left Left
        if bf > 1 && getBalance(node.left!) >= 0 {
            return rotateRight(node)
        }
        // Left Right
        if bf > 1 && getBalance(node.left!) < 0 {
            node.left = rotateLeft(node.left!)
            return rotateRight(node)
        }
        // Right Right
        if bf < -1 && getBalance(node.right!) <= 0 {
            return rotateLeft(node)
        }
        // Right Left
        if bf < -1 && getBalance(node.right!) > 0 {
            node.right = rotateRight(node.right!)
            return rotateLeft(node)
        }

        return node
    }

    func nearestDiff(to target: Int) -> Int? {
        guard let _ = root else { return nil }
        var best = Int.max

        if let lb = lowerBound(root, target) {
            best = min(best, abs(lb - target))
        }
        if let pred = predecessor(root, target) {
            best = min(best, abs(pred - target))
        }

        return best == Int.max ? nil : best
    }

    private func lowerBound(_ node: Node?, _ target: Int) -> Int? {
        var current = node
        var result: Int? = nil
        while let cur = current {
            if cur.key >= target {
                result = cur.key
                current = cur.left
            } else {
                current = cur.right
            }
        }
        return result
    }

    private func predecessor(_ node: Node?, _ target: Int) -> Int? {
        var current = node
        var result: Int? = nil
        while let cur = current {
            if cur.key < target {
                result = cur.key
                current = cur.right
            } else {
                current = cur.left
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet
import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun minAbsoluteDifference(nums: List<Int>, x: Int): Int {
        val n = nums.size
        val set = TreeSet<Int>()
        var ans = Int.MAX_VALUE
        for (j in 0 until n) {
            if (j - x >= 0) {
                set.add(nums[j - x])
            }
            if (!set.isEmpty()) {
                val target = nums[j]
                set.floor(target)?.let { ans = min(ans, abs(target - it)) }
                set.ceiling(target)?.let { ans = min(ans, abs(it - target)) }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';
import 'dart:math';

class BIT {
  final List<int> _tree;
  final int n;
  BIT(this.n) : _tree = List.filled(n + 2, 0);

  void add(int idx, int delta) {
    for (int i = idx; i <= n; i += i & -i) {
      _tree[i] += delta;
    }
  }

  int sum(int idx) {
    int res = 0;
    for (int i = idx; i > 0; i -= i & -i) {
      res += _tree[i];
    }
    return res;
  }

  // returns smallest index such that prefix sum >= k (k >= 1)
  int kth(int k) {
    int idx = 0;
    int bitMask = 1;
    while ((bitMask << 1) <= n) bitMask <<= 1;
    for (int step = bitMask; step > 0; step >>= 1) {
      int next = idx + step;
      if (next <= n && _tree[next] < k) {
        idx = next;
        k -= _tree[next];
      }
    }
    return idx + 1;
  }
}

class Solution {
  int minAbsoluteDifference(List<int> nums, int x) {
    int n = nums.length;
    // coordinate compression
    List<int> sortedVals = List.from(nums);
    sortedVals.sort();
    sortedVals = sortedVals.toSet().toList(); // unique
    Map<int, int> rank = {};
    for (int i = 0; i < sortedVals.length; ++i) {
      rank[sortedVals[i]] = i + 1; // 1-indexed for BIT
    }

    BIT bit = BIT(sortedVals.length);
    int answer = 1 << 60;

    for (int j = x; j < n; ++j) {
      // insert nums[j - x] into the multiset
      int idxToAdd = j - x;
      int valAdd = nums[idxToAdd];
      bit.add(rank[valAdd]!, 1);

      int curVal = nums[j];
      int r = rank[curVal]!;

      // predecessor (largest <= curVal that is strictly less)
      int cntPre = bit.sum(r - 1);
      if (cntPre > 0) {
        int predIdx = bit.kth(cntPre);
        int predVal = sortedVals[predIdx - 1];
        answer = min(answer, (curVal - predVal).abs());
      }

      // successor (smallest >= curVal that is strictly greater)
      int cntLe = bit.sum(r); // count of values <= curVal
      int total = bit.sum(bit.n);
      if (cntLe < total) {
        int succIdx = bit.kth(cntLe + 1);
        int succVal = sortedVals[succIdx - 1];
        answer = min(answer, (succVal - curVal).abs());
      }
    }

    return answer;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"math/rand"
	"time"
)

type node struct {
	key      int
	priority uint32
	left     *node
	right    *node
	cnt      int
}

func newNode(key int) *node {
	return &node{
		key:      key,
		priority: rand.Uint32(),
		cnt:      1,
	}
}

// rotate right
func rotateRight(p *node) *node {
	q := p.left
	p.left = q.right
	q.right = p
	return q
}

// rotate left
func rotateLeft(p *node) *node {
	q := p.right
	p.right = q.left
	q.left = p
	return q
}

func insert(root *node, key int) *node {
	if root == nil {
		return newNode(key)
	}
	if key < root.key {
		root.left = insert(root.left, key)
		if root.left.priority > root.priority {
			root = rotateRight(root)
		}
	} else if key > root.key {
		root.right = insert(root.right, key)
		if root.right.priority > root.priority {
			root = rotateLeft(root)
		}
	} else {
		root.cnt++
	}
	return root
}

// lowerBound returns the node with smallest key >= target
func lowerBound(root *node, target int) *node {
	var res *node
	for root != nil {
		if root.key >= target {
			res = root
			root = root.left
		} else {
			root = root.right
		}
	}
	return res
}

// predecessor returns the node with largest key <= target
func predecessor(root *node, target int) *node {
	var res *node
	for root != nil {
		if root.key <= target {
			res = root
			root = root.right
		} else {
			root = root.left
		}
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func minAbsoluteDifference(nums []int, x int) int {
	rand.Seed(time.Now().UnixNano())
	var root *node
	ans := math.MaxInt64

	for j := x; j < len(nums); j++ {
		// insert element that becomes eligible
		root = insert(root, nums[j-x])

		val := nums[j]

		if lb := lowerBound(root, val); lb != nil {
			if d := abs(lb.key - val); d < ans {
				ans = d
				if ans == 0 {
					return 0
				}
			}
		}
		if pred := predecessor(root, val); pred != nil {
			if d := abs(pred.key - val); d < ans {
				ans = d
				if ans == 0 {
					return 0
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
class Fenwick
  def initialize(n)
    @n = n
    @tree = Array.new(n + 2, 0)
  end

  def add(i, delta)
    while i <= @n
      @tree[i] += delta
      i += i & -i
    end
  end

  def sum(i)
    res = 0
    while i > 0
      res += @tree[i]
      i -= i & -i
    end
    res
  end

  # returns smallest index such that prefix sum >= k (k >= 1)
  def kth(k)
    idx = 0
    bitmask = 1 << (Math.log2(@n).to_i + 1)
    while bitmask > 0
      next_idx = idx + bitmask
      if next_idx <= @n && @tree[next_idx] < k
        idx = next_idx
        k -= @tree[next_idx]
      end
      bitmask >>= 1
    end
    idx + 1
  end
end

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_absolute_difference(nums, x)
  n = nums.length
  # coordinate compression
  vals = nums.uniq.sort
  index = {}
  vals.each_with_index { |v, i| index[v] = i + 1 } # 1‑based

  bit = Fenwick.new(vals.size)

  ans = (1 << 62) # sufficiently large
  set_size = 0

  (x...n).each do |j|
    # insert element that becomes eligible
    add_val = nums[j - x]
    bit.add(index[add_val], 1)
    set_size += 1

    target = nums[j]
    idx_target = index[target]

    # predecessor (largest <= target)
    cnt_le = bit.sum(idx_target)
    if cnt_le > 0
      pred_idx = bit.kth(cnt_le)
      diff = (target - vals[pred_idx - 1]).abs
      ans = diff if diff < ans
    end

    # successor (smallest >= target)
    cnt_lt = bit.sum(idx_target - 1)
    if cnt_lt < set_size
      succ_idx = bit.kth(cnt_lt + 1)
      diff = (vals[succ_idx - 1] - target).abs
      ans = diff if diff < ans
    end

    return 0 if ans == 0
  end

  ans.to_i
end
```

## Scala

```scala
import java.util.TreeSet

object Solution {
  def minAbsoluteDifference(nums: List[Int], x: Int): Int = {
    val arr = nums.toArray
    val n = arr.length
    var ans = Int.MaxValue
    val set = new TreeSet[Integer]()
    for (j <- x until n) {
      set.add(arr(j - x))
      val cur = arr(j)
      val floor = set.floor(cur)
      if (floor != null) ans = math.min(ans, math.abs(cur - floor))
      val ceil = set.ceiling(cur)
      if (ceil != null) ans = math.min(ans, math.abs(ceil - cur))
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::BTreeMap;

impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>, x: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut map: BTreeMap<i32, i32> = BTreeMap::new();
        let mut ans: i64 = i64::MAX;
        let x_usize = x as usize;

        for j in x_usize..n {
            // Insert the element that is exactly x positions before j
            let val = nums[j - x_usize];
            *map.entry(val).or_insert(0) += 1;

            let target = nums[j];

            // Find successor (first >= target)
            if let Some((&succ_val, _)) = map.range(target..).next() {
                let diff = (succ_val as i64 - target as i64).abs();
                if diff < ans {
                    ans = diff;
                }
            }

            // Find predecessor (last <= target)
            if let Some((&pred_val, _)) = map.range(..=target).next_back() {
                let diff = (pred_val as i64 - target as i64).abs();
                if diff < ans {
                    ans = diff;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/random)

(struct node (key prio left right) #:transparent)

(define (rand-prio) (random most-positive-fixnum))

(define (rotate-right y)
  (let* ([x (node-left y)]
         [t2 (node-right x)])
    (make-node (node-key x) (node-prio x) (node-left x)
               (make-node (node-key y) (node-prio y) t2 (node-right y)))))

(define (rotate-left x)
  (let* ([y (node-right x)]
         [t2 (node-left y)])
    (make-node (node-key y) (node-prio y)
               (make-node (node-key x) (node-prio x) (node-left x) t2)
               (node-right y))))

(define (treap-insert root key)
  (if (not root)
      (make-node key (rand-prio) #f #f)
      (let ([k (node-key root)])
        (cond [(< key k)
               (let ([new-left (treap-insert (node-left root) key)])
                 (define new-root (make-node k (node-prio root) new-left (node-right root)))
                 (if (> (node-prio new-left) (node-prio root))
                     (rotate-right new-root)
                     new-root))]
              [(> key k)
               (let ([new-right (treap-insert (node-right root) key)])
                 (define new-root (make-node k (node-prio root) (node-left root) new-right))
                 (if (> (node-prio new-right) (node-prio root))
                     (rotate-left new-root)
                     new-root))]
              [else ; duplicate, insert to left
               (let ([new-left (treap-insert (node-left root) key)])
                 (define new-root (make-node k (node-prio root) new-left (node-right root)))
                 (if (> (node-prio new-left) (node-prio root))
                     (rotate-right new-root)
                     new-root))]))))

(define (treap-lower-bound root target)
  (let loop ([node root] [candidate #f])
    (if (not node)
        candidate
        (let ([k (node-key node)])
          (if (>= k target)
              (loop (node-left node) k)
              (loop (node-right node) candidate))))))

(define (treap-predecessor root target)
  (let loop ([node root] [candidate #f])
    (if (not node)
        candidate
        (let ([k (node-key node)])
          (if (< k target)
              (loop (node-right node) k)
              (loop (node-left node) candidate))))))

(define/contract (min-absolute-difference nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [inf 10000000000]
         [best (box inf)]
         [root (box #f)])
    (for ([j (in-range x n)])
      (set-box! root (treap-insert (unbox root) (list-ref nums (- j x))))
      (define val (list-ref nums j))
      (define succ (treap-lower-bound (unbox root) val))
      (when succ
        (let ([diff (abs (- val succ))])
          (when (< diff (unbox best)) (set-box! best diff))))
      (define pred (treap-predecessor (unbox root) val))
      (when pred
        (let ([diff (abs (- val pred))])
          (when (< diff (unbox best)) (set-box! best diff)))))
    (unbox best)))
```

## Erlang

```erlang
-spec min_absolute_difference([integer()], integer()) -> integer().
min_absolute_difference(Nums, X) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    MaxInt = 1 bsl 60,
    loop(0, Len, Tuple, X, gb_trees:empty(), MaxInt).

loop(Index, Len, _Tuple, _X, _Tree, MinDiff) when Index == Len ->
    MinDiff;
loop(Index, Len, Tuple, X, Tree, MinDiff) ->
    Tree1 = case Index - X of
                I when I >= 0 ->
                    ValInsert = erlang:element(I + 1, Tuple),
                    insert_if_not_exists(Tree, ValInsert);
                _ -> Tree
            end,
    CurrVal = erlang:element(Index + 1, Tuple),
    Diff = nearest_diff(Tree1, CurrVal),
    NewMin = if Diff < MinDiff -> Diff; true -> MinDiff end,
    loop(Index + 1, Len, Tuple, X, Tree1, NewMin).

insert_if_not_exists(Tree, Val) ->
    case gb_trees:is_defined(Val, Tree) of
        true -> Tree;
        false -> gb_trees:insert(Val, true, Tree)
    end.

nearest_diff(Tree, Val) ->
    case gb_trees:is_empty(Tree) of
        true -> 1 bsl 60;
        false ->
            Iter = gb_trees:iterator_from(Val, Tree),
            Diff1 = case gb_trees:next(Iter) of
                        {Key, _V, _Next} -> erlang:abs(Key - Val);
                        none -> 1 bsl 60
                    end,
            Diff2 = case gb_trees:prev(Iter) of
                        {Key, _V, _Prev} -> erlang:abs(Key - Val);
                        none -> 1 bsl 60
                    end,
            if Diff1 < Diff2 -> Diff1; true -> Diff2 end
    end.
```

## Elixir

```elixir
defmodule Treap do
  def insert(nil, key), do: %{key: key, prio: :rand.uniform(), cnt: 1, left: nil, right: nil}
  def insert(node = %{key: k, cnt: c, left: l, right: r, prio: p}, key) do
    cond do
      key == k ->
        %{node | cnt: c + 1}

      key < k ->
        new_left = insert(l, key)
        node2 = %{node | left: new_left}
        if new_left.prio > p, do: rotate_right(node2), else: node2

      true ->
        new_right = insert(r, key)
        node2 = %{node | right: new_right}
        if new_right.prio > p, do: rotate_left(node2), else: node2
    end
  end

  defp rotate_right(%{key: k, left: %{key: lk, prio: lp, cnt: lc, left: ll, right: lr}, right: r, cnt: c, prio: p}) do
    %{key: lk, prio: lp, cnt: lc,
      left: ll,
      right: %{key: k, prio: p, cnt: c, left: lr, right: r}}
  end

  defp rotate_left(%{key: k, right: %{key: rk, prio: rp, cnt: rc, left: rl, right: rr}, left: l, cnt: c, prio: p}) do
    %{key: rk, prio: rp, cnt: rc,
      left: %{key: k, prio: p, cnt: c, left: l, right: rl},
      right: rr}
  end

  def floor(nil, _), do: nil
  def floor(%{key: k, left: l, right: r} = node, key) do
    cond do
      k == key -> k
      k < key ->
        case floor(r, key) do
          nil -> k
          v when v > k -> v
          v -> v
        end
      true -> # k > key
        floor(l, key)
    end
  end

  def ceil(nil, _), do: nil
  def ceil(%{key: k, left: l, right: r} = node, key) do
    cond do
      k == key -> k
      k > key ->
        case ceil(l, key) do
          nil -> k
          v when v < k -> v
          _ -> k
        end
      true -> # k < key
        ceil(r, key)
    end
  end
end

defmodule Solution do
  @spec min_absolute_difference(nums :: [integer], x :: integer) :: integer
  def min_absolute_difference(nums, x) do
    arr = List.to_tuple(nums)
    n = tuple_size(arr)

    {_, ans} =
      Enum.reduce(0..(n - 1), {nil, :infinity}, fn j, {root, best} ->
        root =
          if j >= x do
            val = elem(arr, j - x)
            Treap.insert(root, val)
          else
            root
          end

        best =
          if j >= x do
            cur = elem(arr, j)

            floor = Treap.floor(root, cur)
            ceil = Treap.ceil(root, cur)

            diffs =
              [floor, ceil]
              |> Enum.filter(& &1)
              |> Enum.map(fn v -> abs(v - cur) end)

            min_diff = if diffs == [], do: best, else: Enum.min(diffs)

            if min_diff < best, do: min_diff, else: best
          else
            best
          end

        {root, best}
      end)

    ans
  end
end
```
