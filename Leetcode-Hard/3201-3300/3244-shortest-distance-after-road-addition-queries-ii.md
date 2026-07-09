# 3244. Shortest Distance After Road Addition Queries II

## Cpp

```cpp
class Solution {
public:
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        long long saved = 0;                     // total edges saved by shortcuts
        map<int,int> intervals;                  // key: start u , value: end v of active shortcuts
        vector<int> ans;
        ans.reserve(queries.size());
        
        for (const auto& q : queries) {
            int u = q[0], v = q[1];
            
            // Check if there is an existing interval that already covers [u, v]
            bool covered = false;
            auto it = intervals.lower_bound(u);
            if (it != intervals.begin()) {
                auto prev = std::prev(it);
                if (prev->second >= v) {
                    covered = true;
                }
            }
            
            if (!covered) {
                // Remove all intervals completely inside [u, v]
                while (true) {
                    it = intervals.lower_bound(u);
                    if (it == intervals.end() || it->first > v) break;
                    // due to non‑crossing property, it->second <= v
                    saved -= (long long)(it->second - it->first - 1);
                    it = intervals.erase(it);   // erase returns iterator to next element
                }
                // Insert the new interval
                intervals[u] = v;
                saved += (long long)(v - u - 1);
            }
            
            ans.push_back((int)((n - 1) - saved));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        int m = queries.length;
        int[] answer = new int[m];
        java.util.TreeMap<Integer, Integer> map = new java.util.TreeMap<>();
        long saved = 0; // total number of edges skipped by current shortcuts

        for (int i = 0; i < m; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            java.util.Map.Entry<Integer, Integer> floor = map.floorEntry(u);
            if (floor != null && floor.getValue() >= v) {
                // new road is completely covered by an existing one; no effect
            } else {
                // remove all intervals that start inside [u, v]
                java.util.NavigableMap<Integer, Integer> sub = map.subMap(u, true, v, true);
                java.util.List<Integer> toRemove = new java.util.ArrayList<>();
                for (java.util.Map.Entry<Integer, Integer> e : sub.entrySet()) {
                    saved -= (long) (e.getValue() - e.getKey() - 1);
                    toRemove.add(e.getKey());
                }
                for (int key : toRemove) {
                    map.remove(key);
                }
                // add the new interval
                map.put(u, v);
                saved += (long) (v - u - 1);
            }

            answer[i] = (int) ((n - 1) - saved);
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from bisect import bisect_left

        starts = []               # sorted list of interval start points
        end_map = {}              # start -> end
        saved = 0                 # total edges saved by current shortcuts
        res = []

        for u, v in queries:
            # find position to insert based on start
            idx = bisect_left(starts, u)

            # check if covered by previous interval
            covered = False
            if idx > 0:
                prev_start = starts[idx - 1]
                prev_end = end_map[prev_start]
                if prev_end >= v:   # existing interval fully covers [u,v]
                    covered = True

            if not covered:
                # remove all intervals that are strictly inside [u, v]
                # start from idx (first start >= u)
                while idx < len(starts):
                    s = starts[idx]
                    e = end_map[s]
                    if s > v:   # beyond the new interval
                        break
                    # since intervals do not cross, e <= v holds here
                    saved -= (e - s - 1)
                    del end_map[s]
                    starts.pop(idx)   # keep idx same as list shifts left

                # insert the new interval
                starts.insert(idx, u)
                end_map[u] = v
                saved += (v - u - 1)

            res.append((n - 1) - saved)

        return res
```

## Python3

```python
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries):
        nxt = [i + 1 for i in range(n)]  # nxt[n-1] = n (sentinel)
        size = n
        ans = []
        for u, v in queries:
            cur = nxt[u]
            while cur < v:
                size -= 1
                nxt[u] = nxt[cur]
                cur = nxt[u]
            ans.append(size - 1)
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct Node {
    int l, r;
    unsigned int pri;
    long long sum;               // total saved steps in subtree
    struct Node *left, *right;
} Node;

static Node *pool;
static int poolIdx;

/* Update aggregate information of a node */
static void update(Node *n) {
    if (!n) return;
    long long leftSum = n->left ? n->left->sum : 0;
    long long rightSum = n->right ? n->right->sum : 0;
    n->sum = (long long)n->r - n->l - 1 + leftSum + rightSum;
}

/* Split treap by key (node.l < key goes to *a, otherwise to *b) */
static void split(Node *root, int key, Node **a, Node **b) {
    if (!root) {
        *a = *b = NULL;
        return;
    }
    if (root->l < key) {
        split(root->right, key, &root->right, b);
        *a = root;
        update(*a);
    } else {
        split(root->left, key, a, &root->left);
        *b = root;
        update(*b);
    }
}

/* Merge two treaps where all keys in a are < keys in b */
static Node *merge(Node *a, Node *b) {
    if (!a || !b) return a ? a : b;
    if (a->pri > b->pri) {
        a->right = merge(a->right, b);
        update(a);
        return a;
    } else {
        b->left = merge(a, b->left);
        update(b);
        return b;
    }
}

/* Simple xorshift RNG */
static unsigned int rng() {
    static unsigned int x = 2463534242U;
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shortestDistanceAfterQueries(int n, int** queries, int queriesSize,
                                 int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    pool = (Node *)malloc(sizeof(Node) * (queriesSize + 5));
    poolIdx = 0;

    Node *root = NULL;
    long long totalSaved = 0;   // sum of (r-l-1) for chosen shortcuts

    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int v = queries[i][1];

        Node *left, *midRight;
        split(root, u, &left, &midRight);
        Node *mid, *right;
        split(midRight, v, &mid, &right);

        long long midSum = mid ? mid->sum : 0;
        long long newWeight = (long long)v - u - 1;

        if (newWeight > midSum) {
            totalSaved = totalSaved - midSum + newWeight;
            Node *node = &pool[poolIdx++];
            node->l = u;
            node->r = v;
            node->pri = rng();
            node->left = node->right = NULL;
            node->sum = newWeight;
            root = merge(left, merge(node, right));
        } else {
            root = merge(left, merge(mid, right));
        }

        ans[i] = (int)((long long)n - 1 - totalSaved);
    }

    free(pool);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ShortestDistanceAfterQueries(int n, int[][] queries) {
        int m = queries.Length;
        int[] answer = new int[m];
        long saved = 0; // total edges saved by shortcuts

        var starts = new SortedSet<int>();          // stores start points of active shortcuts
        var endMap = new Dictionary<int, int>();    // maps start -> end for active shortcuts

        for (int i = 0; i < m; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            bool redundant = false;

            // Find the greatest start <= u to see if it contains [u, v]
            var predView = starts.GetViewBetween(int.MinValue, u);
            if (predView.Count > 0) {
                int predStart = predView.Max;
                int predEnd = endMap[predStart];
                if (predEnd >= v) {
                    redundant = true; // already covered by a larger shortcut
                }
            }

            if (!redundant) {
                // Remove all shortcuts fully inside [u, v]
                var innerView = starts.GetViewBetween(u, v - 1);
                var toRemove = new List<int>();
                foreach (int s in innerView) {
                    int e = endMap[s];
                    if (e <= v) {
                        saved -= (e - s - 1);
                        toRemove.Add(s);
                    }
                }
                foreach (int s in toRemove) {
                    starts.Remove(s);
                    endMap.Remove(s);
                }

                // Add the new shortcut
                starts.Add(u);
                endMap[u] = v;
                saved += (v - u - 1);
            }

            answer[i] = (n - 1) - (int)saved;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var shortestDistanceAfterQueries = function(n, queries) {
    // Treap node definition
    function Node(key, end) {
        this.key = key;          // start of interval
        this.end = end;          // end of interval
        this.prio = Math.random();
        this.left = null;
        this.right = null;
    }

    // Rotate right
    function rotateRight(y) {
        const x = y.left;
        y.left = x.right;
        x.right = y;
        return x;
    }
    // Rotate left
    function rotateLeft(x) {
        const y = x.right;
        x.right = y.left;
        y.left = x;
        return y;
    }

    // Insert node into treap
    function insert(root, node) {
        if (!root) return node;
        if (node.key < root.key) {
            root.left = insert(root.left, node);
            if (root.left.prio < root.prio) root = rotateRight(root);
        } else {
            root.right = insert(root.right, node);
            if (root.right.prio < root.prio) root = rotateLeft(root);
        }
        return root;
    }

    // Merge two treaps where all keys in a < keys in b
    function merge(a, b) {
        if (!a) return b;
        if (!b) return a;
        if (a.prio < b.prio) {
            a.right = merge(a.right, b);
            return a;
        } else {
            b.left = merge(a, b.left);
            return b;
        }
    }

    // Erase node with given key
    function erase(root, key) {
        if (!root) return null;
        if (key < root.key) {
            root.left = erase(root.left, key);
        } else if (key > root.key) {
            root.right = erase(root.right, key);
        } else {
            // delete this node
            return merge(root.left, root.right);
        }
        return root;
    }

    // Find node with smallest key >= given key
    function lowerBound(root, key) {
        let res = null;
        while (root) {
            if (root.key >= key) {
                res = root;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return res;
    }

    // Find node with largest key <= given key
    function predecessor(root, key) {
        let res = null;
        while (root) {
            if (root.key <= key) {
                res = root;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return res;
    }

    let root = null;          // treap of effective intervals
    let savedSum = 0;         // total saved steps by current intervals
    const ans = [];

    for (const [u, v] of queries) {
        // Check if new interval is already covered by an existing one
        const pred = predecessor(root, u);
        if (!(pred && pred.end >= v)) {
            // Remove all intervals strictly inside [u, v)
            let node = lowerBound(root, u);
            while (node && node.key < v) {
                savedSum -= (node.end - node.key - 1);
                root = erase(root, node.key);
                node = lowerBound(root, u);
            }
            // Insert the new interval
            const save = v - u - 1;
            savedSum += save;
            const newNode = new Node(u, v);
            root = insert(root, newNode);
        }
        ans.push((n - 1) - savedSum);
    }

    return ans;
};
```

## Typescript

```typescript
function shortestDistanceAfterQueries(n: number, queries: number[][]): number[] {
    class Node {
        key: number;
        val: number;
        pri: number;
        left: Node | null = null;
        right: Node | null = null;
        constructor(key: number, val: number) {
            this.key = key;
            this.val = val;
            this.pri = Math.random();
        }
    }

    class Treap {
        root: Node | null = null;

        rotateRight(y: Node): Node {
            const x = y.left!;
            y.left = x.right;
            x.right = y;
            return x;
        }

        rotateLeft(x: Node): Node {
            const y = x.right!;
            x.right = y.left;
            y.left = x;
            return y;
        }

        _insert(node: Node | null, key: number, val: number): Node {
            if (!node) return new Node(key, val);
            if (key < node.key) {
                node.left = this._insert(node.left, key, val);
                if (node.left!.pri < node.pri) node = this.rotateRight(node);
            } else {
                node.right = this._insert(node.right, key, val);
                if (node.right!.pri < node.pri) node = this.rotateLeft(node);
            }
            return node;
        }

        insert(key: number, val: number): void {
            this.root = this._insert(this.root, key, val);
        }

        _erase(node: Node | null, key: number): Node | null {
            if (!node) return null;
            if (key < node.key) {
                node.left = this._erase(node.left, key);
            } else if (key > node.key) {
                node.right = this._erase(node.right, key);
            } else {
                // node to delete
                if (!node.left && !node.right) return null;
                if (!node.left) return node.right;
                if (!node.right) return node.left;
                if (node.left.pri < node.right.pri) {
                    node = this.rotateRight(node);
                    node.right = this._erase(node.right, key);
                } else {
                    node = this.rotateLeft(node);
                    node.left = this._erase(node.left, key);
                }
            }
            return node;
        }

        erase(key: number): void {
            this.root = this._erase(this.root, key);
        }

        predecessor(key: number): Node | null {
            let cur = this.root;
            let pred: Node | null = null;
            while (cur) {
                if (cur.key <= key) {
                    pred = cur;
                    cur = cur.right;
                } else {
                    cur = cur.left;
                }
            }
            return pred;
        }

        successor(key: number): Node | null {
            let cur = this.root;
            let succ: Node | null = null;
            while (cur) {
                if (cur.key > key) {
                    succ = cur;
                    cur = cur.left;
                } else {
                    cur = cur.right;
                }
            }
            return succ;
        }

        // get node by exact key
        find(key: number): Node | null {
            let cur = this.root;
            while (cur) {
                if (key === cur.key) return cur;
                cur = key < cur.key ? cur.left : cur.right;
            }
            return null;
        }
    }

    const treap = new Treap();
    let saved = 0; // total reduction
    const ans: number[] = [];

    for (const [u, v] of queries) {
        const pred = treap.predecessor(u);
        if (pred && pred.val >= v) {
            // new interval is fully covered, ignore
        } else {
            // remove intervals strictly inside [u,v]
            let cur = treap.successor(u);
            while (cur && cur.key < v && cur.val <= v) {
                saved -= (cur.val - cur.key - 1);
                const delKey = cur.key;
                // move to next before deletion
                cur = treap.successor(delKey);
                treap.erase(delKey);
            }
            // insert new interval
            treap.insert(u, v);
            saved += (v - u - 1);
        }
        ans.push((n - 1) - saved);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function shortestDistanceAfterQueries($n, $queries) {
        // DSU parent array for "next not deleted" nodes
        $parent = [];
        for ($i = 0; $i <= $n; $i++) {
            $parent[$i] = $i;
        }

        // Find with path compression (recursive closure)
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        $cnt = $n; // current number of nodes in the shortest path
        $ans = [];

        foreach ($queries as $q) {
            [$u, $v] = $q;
            $x = $find($u + 1);
            while ($x < $v) {
                // remove node x from the path
                $cnt--;
                $parent[$x] = $find($x + 1); // union with next
                $x = $find($x); // move to next not-deleted node
            }
            $ans[] = $cnt - 1; // distance equals remaining nodes minus one
        }

        return $ans;
    }
}
```

## Swift

```swift
import Foundation

class TreapNode {
    var key: Int
    var val: Int
    var priority: UInt32
    var left: TreapNode?
    var right: TreapNode?
    var size: Int = 1
    
    init(key: Int, val: Int) {
        self.key = key
        self.val = val
        self.priority = arc4random()
    }
}

func nodeSize(_ node: TreapNode?) -> Int {
    return node?.size ?? 0
}

func update(_ node: TreapNode?) {
    if let n = node {
        n.size = 1 + nodeSize(n.left) + nodeSize(n.right)
    }
}

// split by key, left contains keys < key, right contains keys >= key
func split(_ root: TreapNode?, _ key: Int) -> (TreapNode?, TreapNode?) {
    guard let r = root else { return (nil, nil) }
    if r.key < key {
        let (l2, r2) = split(r.right, key)
        r.right = l2
        update(r)
        return (r, r2)
    } else {
        let (l1, r1) = split(r.left, key)
        r.left = r1
        update(r)
        return (l1, r)
    }
}

// merge two treaps where all keys in left < keys in right
func merge(_ left: TreapNode?, _ right: TreapNode?) -> TreapNode? {
    if left == nil { return right }
    if right == nil { return left }
    if left!.priority < right!.priority {
        left!.right = merge(left!.right, right)
        update(left)
        return left
    } else {
        right!.left = merge(left, right!.left)
        update(right)
        return right
    }
}

// predecessor: max node with key < given key
func predecessor(_ root: TreapNode?, _ key: Int) -> TreapNode? {
    var cur = root
    var pred: TreapNode? = nil
    while let node = cur {
        if node.key < key {
            pred = node
            cur = node.right
        } else {
            cur = node.left
        }
    }
    return pred
}

class Solution {
    func shortestDistanceAfterQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var parent = Array(0...n)               // DSU for edges 0..n-2, sentinel at n-1
        var answer = n - 1                      // initial distance
        var result = [Int]()
        var root: TreapNode? = nil              // treap storing active shortcuts
        
        func findEdge(_ x: Int) -> Int {
            var v = x
            while parent[v] != v {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }
        
        for q in queries {
            let l = q[0]
            let r = q[1]
            
            // Remove unit edges inside [l, r)
            var i = findEdge(l)
            while i < r {
                answer -= 1
                parent[i] = i + 1
                i = findEdge(i)
            }
            
            // Check if new shortcut is already covered by an existing one
            if let pred = predecessor(root, l), pred.val >= r {
                result.append(answer)
                continue
            }
            
            // Split treap to isolate intervals with start in [l, r)
            let (leftPart, rest) = split(root, l)
            let (midPart, rightPart) = split(rest, r)
            let removedCount = nodeSize(midPart)
            
            // Insert the new shortcut
            let newNode = TreapNode(key: l, val: r)
            root = merge(merge(leftPart, newNode), rightPart)
            
            // Update answer: replace removed shortcuts with one new shortcut
            answer = answer - removedCount + 1
            
            result.append(answer)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.TreeMap

class Solution {
    fun shortestDistanceAfterQueries(n: Int, queries: Array<IntArray>): IntArray {
        val intervals = TreeMap<Int, Int>()
        var saved = 0L
        val answer = IntArray(queries.size)
        for (i in queries.indices) {
            val u = queries[i][0]
            val v = queries[i][1]

            // If an existing interval already covers [u, v], ignore this query.
            val floor = intervals.floorEntry(u)
            var needInsert = true
            if (floor != null && floor.value >= v) {
                needInsert = false
            }

            if (needInsert) {
                // Remove all intervals completely inside [u, v].
                val sub = intervals.subMap(u, false, v, false)
                val toRemove = ArrayList<Int>(sub.size)
                for ((start, end) in sub.entries) {
                    saved -= (end - start - 1).toLong()
                    toRemove.add(start)
                }
                for (key in toRemove) {
                    intervals.remove(key)
                }

                // Insert the new interval.
                intervals[u] = v
                saved += (v - u - 1).toLong()
            }

            answer[i] = (n - 1 - saved).toInt()
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class _Node {
  int key; // start of interval
  int val; // end of interval
  int pr;
  _Node? left, right;
  _Node(this.key, this.val) : pr = Random().nextInt(1 << 30);
}

_Node? _rotateRight(_Node y) {
  final x = y.left!;
  y.left = x.right;
  x.right = y;
  return x;
}

_Node? _rotateLeft(_Node x) {
  final y = x.right!;
  x.right = y.left;
  y.left = x;
  return y;
}

_Node _insert(_Node? root, int key, int val) {
  if (root == null) return _Node(key, val);
  if (key < root.key) {
    root.left = _insert(root.left, key, val);
    if (root.left!.pr > root.pr) {
      root = _rotateRight(root)!;
    }
  } else {
    root.right = _insert(root.right, key, val);
    if (root.right!.pr > root.pr) {
      root = _rotateLeft(root)!;
    }
  }
  return root;
}

_Node? _erase(_Node? root, int key) {
  if (root == null) return null;
  if (key < root.key) {
    root.left = _erase(root.left, key);
  } else if (key > root.key) {
    root.right = _erase(root.right, key);
  } else {
    // remove this node
    if (root.left == null) return root.right;
    if (root.right == null) return root.left;
    if (root.left!.pr > root.right!.pr) {
      root = _rotateRight(root)!;
      root.right = _erase(root.right, key);
    } else {
      root = _rotateLeft(root)!;
      root.left = _erase(root.left, key);
    }
  }
  return root;
}

_Node? _lowerBound(_Node? root, int key) {
  _Node? res;
  while (root != null) {
    if (root.key >= key) {
      res = root;
      root = root.left;
    } else {
      root = root.right;
    }
  }
  return res;
}

_Node? _predecessor(_Node? root, int key) {
  _Node? res;
  while (root != null) {
    if (root.key < key) {
      res = root;
      root = root.right;
    } else {
      root = root.left;
    }
  }
  return res;
}

class Solution {
  List<int> shortestDistanceAfterQueries(int n, List<List<int>> queries) {
    int totalReduction = 0; // sum of (end - start - 1) for active intervals
    _Node? root;
    final List<int> ans = [];

    for (final q in queries) {
      final int l = q[0];
      final int r = q[1];

      bool contained = false;

      // check predecessor interval that might contain [l, r]
      final pred = _predecessor(root, l);
      if (pred != null && pred.val >= r) {
        contained = true;
      } else {
        // also check interval starting exactly at l
        final cur = _lowerBound(root, l);
        if (cur != null && cur.key == l && cur.val >= r) {
          contained = true;
        }
      }

      if (!contained) {
        // remove all intervals fully inside [l, r]
        while (true) {
          final node = _lowerBound(root, l);
          if (node == null || node.val > r) break; // no more inner intervals
          totalReduction -= (node.val - node.key - 1);
          root = _erase(root, node.key);
        }
        // insert the new interval
        root = _insert(root, l, r);
        totalReduction += (r - l - 1);
      }

      ans.add((n - 1) - totalReduction);
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type node struct {
	key   int
	end   int
	prio  uint32
	left  *node
	right *node
	sum   int64 // total saved in subtree
}

func weight(n *node) int64 {
	if n == nil {
		return 0
	}
	return int64(n.end-n.key-1)
}

func update(n *node) {
	if n == nil {
		return
	}
	n.sum = weight(n)
	if n.left != nil {
		n.sum += n.left.sum
	}
	if n.right != nil {
		n.sum += n.right.sum
	}
}

// split returns (lessThanKey, greaterOrEqualKey)
func split(root *node, key int) (*node, *node) {
	if root == nil {
		return nil, nil
	}
	if key <= root.key {
		l, r := split(root.left, key)
		root.left = r
		update(root)
		return l, root
	}
	l, r := split(root.right, key)
	root.right = l
	update(root)
	return root, r
}

func merge(a, b *node) *node {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.prio < b.prio {
		a.right = merge(a.right, b)
		update(a)
		return a
	}
	b.left = merge(a, b.left)
	update(b)
	return b
}

func maxNode(root *node) *node {
	if root == nil {
		return nil
	}
	for root.right != nil {
		root = root.right
	}
	return root
}

func minNode(root *node) *node {
	if root == nil {
		return nil
	}
	for root.left != nil {
		root = root.left
	}
	return root
}

var rng = rand.New(rand.NewSource(time.Now().UnixNano()))

func newNode(l, r int) *node {
	n := &node{
		key:  l,
		end:  r,
		prio: rng.Uint32(),
	}
	update(n)
	return n
}

func sumSub(root *node) int64 {
	if root == nil {
		return 0
	}
	return root.sum
}

func shortestDistanceAfterQueries(n int, queries [][]int) []int {
	ans := make([]int, len(queries))
	var root *node
	var totalSaved int64 = 0

	for i, q := range queries {
		u, v := q[0], q[1]

		left, right := split(root, u)

		// check predecessor interval that might contain [u,v]
		contained := false
		if pred := maxNode(left); pred != nil && pred.end >= v {
			contained = true
		}
		// also check interval starting exactly at u in the right part
		if !contained && right != nil {
			if mn := minNode(right); mn != nil && mn.key == u && mn.end >= v {
				contained = true
			}
		}

		if contained {
			root = merge(left, right)
		} else {
			mid, newRight := split(right, v) // mid: intervals with start in [u,v)
			totalSaved -= sumSub(mid)

			w := int64(v - u - 1)
			totalSaved += w

			newInterval := newNode(u, v)
			root = merge(merge(left, newInterval), newRight)
		}

		ans[i] = (n - 1) - int(totalSaved)
	}
	return ans
}
```

## Ruby

```ruby
class SegTree
  def initialize(n, inf)
    @size = 1
    while @size < n
      @size <<= 1
    end
    @inf = inf
    @tree = Array.new(@size * 2, inf)
  end

  def point_update(pos, val)
    i = pos + @size
    if val < @tree[i]
      @tree[i] = val
      i >>= 1
      while i > 0
        left = @tree[i << 1]
        right = @tree[(i << 1) + 1]
        newv = left < right ? left : right
        break if newv == @tree[i]
        @tree[i] = newv
        i >>= 1
      end
    end
  end

  def range_min(l, r)
    l += @size
    r += @size
    res = @inf
    while l <= r
      if (l & 1) == 1
        v = @tree[l]
        res = v < res ? v : res
        l += 1
      end
      if (r & 1) == 0
        v = @tree[r]
        res = v < res ? v : res
        r -= 1
      end
      l >>= 1
      r >>= 1
    end
    res
  end
end

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  inf = (1 << 60)
  seg = SegTree.new(n, inf)
  seg.point_update(n - 1, n - 1) # initial chain line

  answers = []
  queries.each do |u, v|
    min_c_v = seg.range_min(v, n - 1)
    dp_v = min_c_v - v
    cand = 1 + dp_v

    min_c_u = seg.range_min(u, n - 1)
    dp_u = min_c_u - u

    if cand < dp_u
      new_c = cand + u
      seg.point_update(u, new_c)
    end

    answers << seg.range_min(0, n - 1) # distance from 0 is minC - 0
  end

  answers
end
```

## Scala

```scala
import java.util.{TreeMap => JTreeMap}

object Solution {
  def shortestDistanceAfterQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val map = new JTreeMap[Int, Int]()
    var i = 0
    while (i < n - 1) {
      map.put(i, i + 1)
      i += 1
    }
    var dist = n - 1
    val ans = new Array[Int](queries.length)
    var idx = 0
    while (idx < queries.length) {
      val u = queries(idx)(0)
      val v = queries(idx)(1)

      // interval containing u
      var curStart = map.floorKey(u)
      var removed = 0
      while (curStart < v) {
        val curEnd = map.get(curStart)
        removed += curEnd - curStart
        map.remove(curStart)
        curStart = curEnd
      }

      // add new shortcut
      map.put(u, v)

      dist = dist - (removed - 1)
      ans(idx) = dist

      idx += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::collections::BTreeSet;
use std::ops::Bound::{Excluded, Included};

struct Fenwick {
    n: usize,
    bit: Vec<i32>,
}
impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, bit: vec![0; n + 2] }
    }
    fn add(&mut self, mut idx: usize, delta: i32) {
        // internal index is 1‑based
        idx += 1;
        while idx <= self.n + 1 {
            self.bit[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i32 {
        // inclusive prefix sum [0..=idx]
        idx += 1;
        let mut res = 0;
        while idx > 0 {
            res += self.bit[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n_usize = n as usize;
        // set of positions that are starts of intervals in the current optimal path
        let mut starts: BTreeSet<usize> = (0..=n_usize - 1).collect();
        let mut bit = Fenwick::new(n_usize);
        for i in 0..n_usize {
            bit.add(i, 1);
        }

        let mut ans = n - 1;
        let mut res = Vec::with_capacity(queries.len());

        for q in queries {
            let u = q[0] as usize;
            let v = q[1] as usize;

            // number of starts strictly greater than u and <= v
            let cnt = (bit.sum(v) - bit.sum(u)) as i32;

            if cnt > 1 {
                ans -= cnt - 1;
                // ensure u and v are present in the set
                if !starts.contains(&u) {
                    starts.insert(u);
                    bit.add(u, 1);
                }
                if !starts.contains(&v) {
                    starts.insert(v);
                    bit.add(v, 1);
                }
                // remove all interior starts (u < x < v)
                let to_remove: Vec<usize> = starts.range((Excluded(u), Excluded(v))).cloned().collect();
                for x in to_remove {
                    starts.remove(&x);
                    bit.add(x, -1);
                }
            }

            res.push(ans);
        }

        res
    }
}
```

## Racket

```racket
(define INF 1000000000000)

;; Binary Indexed Tree for prefix minimum
(define (make-bit n)
  (let ((tree (make-vector (+ n 2) INF)))
    (define (update idx val)
      (let loop ((i (+ idx 1))) ; convert to 1‑based inside
        (when (<= i (+ n 1))
          (vector-set! tree i (min (vector-ref tree i) val))
          (loop (+ i (bitwise-and (- i) i))))))
    (define (query idx)
      (let loop ((i (+ idx 1)) (res INF))
        (if (= i 0)
            res
            (loop (- i (bitwise-and (- i) i)) (min res (vector-ref tree i))))))
    (values update query)))

;; shortest-distance-after-queries implementation
(define (shortest-distance-after-queries n queries)
  (let* ((size n)
         ;; adjacency list for added edges
         (adj (make-vector n '()))
         ;; best offset per exact target, initialized to INF
         (best (make-vector n INF))
         ;; BIT for prefix minima of offsets
         (values (make-bit size))
         (bit-update (car values))
         (bit-query (cadr values))
         ;; queue for BFS propagation
         (queue (make-vector (+ (* 2 (length queries)) 10) -1))
         (qhead 0)
         (qtail 0)
         (answers '()))
    (define (enqueue x)
      (vector-set! queue qtail x)
      (set! qtail (+ qtail 1)))
    (define (dequeue)
      (let ((x (vector-ref queue qhead)))
        (set! qhead (+ qhead 1))
        x))
    (define (queue-empty?) (= qhead qtail))
    ;; helper to get current distance of node i
    (define (dist i)
      (let* ((pref (bit-query i))
             (minB (if (< pref 0) pref 0)))
        (+ i minB)))
    ;; process propagation queue
    (define (process-queue)
      (let loop ()
        (unless (queue-empty?)
          (let ((x (dequeue)))
            (let ((dx (dist x)))
              (for-each
               (lambda (w)
                 (let ((b (+ dx 1 (- w)))) ; b = dist[x] + 1 - w
                   (when (< b (vector-ref best w))
                     (vector-set! best w b)
                     (bit-update w b)
                     (enqueue w))))
               (vector-ref adj x)))
            (loop)))))
    ;; main loop over queries
    (for-each
     (lambda (qr)
       (let* ((u (list-ref qr 0))
              (v (list-ref qr 1)))
         ;; add edge to adjacency
         (vector-set! adj u (cons v (vector-ref adj u)))
         ;; try to improve target using current distance of u
         (let ((b (+ (dist u) 1 (- v)))) ; b = dist[u] + 1 - v
           (when (< b (vector-ref best v))
             (vector-set! best v b)
             (bit-update v b)
             (enqueue v)))
         ;; propagate improvements
         (process-queue)
         ;; compute answer for n-1
         (let* ((pref (bit-query (- n 1)))
                (minB (if (< pref 0) pref 0))
                (ans (+ (- n 1) minB)))
           (set! answers (cons ans answers)))))
     queries)
    (reverse answers)))
```

## Erlang

```erlang
-spec shortest_distance_after_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
shortest_distance_after_queries(N, Queries) ->
    Size = 4 * N + 5,
    EmptyLazy = array:new(Size, {default,0}),
    {FinalLazy, RevAns} = lists:foldl(
        fun([U,V], {LazyAcc, AnsAcc}) ->
            Weight = V - U - 1,
            BestU = point_query(U, 1, 0, N-1, LazyAcc),
            Candidate = BestU + Weight,
            CurV = point_query(V, 1, 0, N-1, LazyAcc),
            NewLazy = if
                Candidate > CurV ->
                    range_chmax(V, N-1, Candidate, 1, 0, N-1, LazyAcc);
                true -> LazyAcc
            end,
            Shortest = (N-1) - point_query(N-1, 1, 0, N-1, NewLazy),
            {NewLazy, [Shortest | AnsAcc]}
        end,
        {EmptyLazy, []},
        Queries),
    lists:reverse(RevAns).

%% range chmax on interval [L,R] with value Val
range_chmax(L, R, Val, Id, LNode, RNode, Lazy) ->
    if
        R < LNode orelse L > RNode ->
            Lazy;
        L =< LNode andalso RNode =< R ->
            Old = array:get(Id, Lazy),
            New = max(Old, Val),
            array:set(Id, New, Lazy);
        true ->
            Mid = (LNode + RNode) div 2,
            Lazy1 = range_chmax(L, R, Val, Id*2, LNode, Mid, Lazy),
            Lazy2 = range_chmax(L, R, Val, Id*2+1, Mid+1, RNode, Lazy1),
            Lazy2
    end.

%% point query at position Pos, returns maximum value applied on the path
point_query(Pos, Id, LNode, RNode, Lazy) ->
    Cur = array:get(Id, Lazy),
    if
        LNode == RNode ->
            Cur;
        true ->
            Mid = (LNode + RNode) div 2,
            ChildVal = if
                Pos =< Mid ->
                    point_query(Pos, Id*2, LNode, Mid, Lazy);
                true ->
                    point_query(Pos, Id*2+1, Mid+1, RNode, Lazy)
            end,
            max(Cur, ChildVal)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_distance_after_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def shortest_distance_after_queries(n, queries) do
    size = pow2_ceil(n)
    tree = :array.new(2 * size, default: 0)

    {answers_rev, _final_tree} =
      Enum.reduce(queries, {[], tree}, fn [u, v], {acc, tr} ->
        dp_u = u + prefix_min(tr, 0, u, size)
        cur_dp_v = v + prefix_min(tr, 0, v, size)
        cand_dp_v = dp_u + 1

        tr =
          if cand_dp_v < cur_dp_v do
            new_val = cand_dp_v - v
            point_update(tr, v, new_val, size)
          else
            tr
          end

        ans = (n - 1) + prefix_min(tr, 0, n - 1, size)
        {[ans | acc], tr}
      end)

    Enum.reverse(answers_rev)
  end

  # smallest power of two >= n
  defp pow2_ceil(n), do: pow2_ceil(n, 1)
  defp pow2_ceil(n, s) when s >= n, do: s
  defp pow2_ceil(n, s), do: pow2_ceil(n, s * 2)

  # point update: set leaf idx to min(old, val) and propagate up
  defp point_update(tree, idx, val, size) do
    pos = idx + size
    old = :array.get(pos, tree)

    if val < old do
      tree = :array.set(pos, val, tree)
      propagate_up(tree, div(pos, 2))
    else
      tree
    end
  end

  defp propagate_up(tree, 0), do: tree
  defp propagate_up(tree, pos) do
    left = :array.get(pos * 2, tree)
    right = :array.get(pos * 2 + 1, tree)
    new_min = if left < right, do: left, else: right
    old = :array.get(pos, tree)

    tree =
      if new_min != old do
        :array.set(pos, new_min, tree)
      else
        tree
      end

    propagate_up(tree, div(pos, 2))
  end

  # minimum value in range [l, r] (inclusive) using iterative segment tree query
  defp prefix_min(tree, l, r, size) do
    left = l + size
    right = r + size
    query_loop(tree, left, right, 1_000_000_000)
  end

  defp query_loop(_tree, left, right, acc) when left > right, do: acc

  defp query_loop(tree, left, right, acc) do
    {acc, left, right} =
      if rem(left, 2) == 1 do
        {min(acc, :array.get(left, tree)), left + 1, right}
      else
        {acc, left, right}
      end

    {acc, left, right} =
      if rem(right, 2) == 0 do
        {min(acc, :array.get(right, tree)), left, right - 1}
      else
        {acc, left, right}
      end

    query_loop(tree, div(left, 2), div(right, 2), acc)
  end
end
```
