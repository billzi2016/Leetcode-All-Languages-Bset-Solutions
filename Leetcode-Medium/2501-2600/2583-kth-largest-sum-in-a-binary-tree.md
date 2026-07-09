# 2583. Kth Largest Sum in a Binary Tree

## Cpp

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        if (!root) return -1;
        std::queue<TreeNode*> q;
        q.push(root);
        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> minHeap;
        
        while (!q.empty()) {
            int sz = q.size();
            long long sum = 0;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                sum += static_cast<long long>(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            minHeap.push(sum);
            if ((int)minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        return (int)minHeap.size() < k ? -1 : minHeap.top();
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long kthLargestLevelSum(TreeNode root, int k) {
        if (root == null) return -1;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        PriorityQueue<Long> minHeap = new PriorityQueue<>(k);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            long sum = 0L;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            minHeap.offer(sum);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        return minHeap.size() < k ? -1 : minHeap.peek();
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if not root:
            return -1

        from collections import deque
        import heapq

        q = deque([root])
        minheap = []

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heapq.heappush(minheap, level_sum)
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0] if len(minheap) == k else -1
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq
from typing import Optional

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        q = deque([root])
        min_heap = []
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0] if len(min_heap) == k else -1
```

## C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>

static void heapSwap(long long *a, long long *b) {
    long long tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(long long *heap, int *sz, long long val) {
    (*sz)++;
    heap[*sz] = val;
    int i = *sz;
    while (i > 1 && heap[i] < heap[i >> 1]) {
        heapSwap(&heap[i], &heap[i >> 1]);
        i >>= 1;
    }
}

static void heapPopMin(long long *heap, int *sz) {
    if (*sz == 0) return;
    heap[1] = heap[*sz];
    (*sz)--;
    int i = 1;
    while (i << 1 <= *sz) {
        int child = i << 1;
        if (child + 1 <= *sz && heap[child + 1] < heap[child])
            child++;
        if (heap[i] <= heap[child]) break;
        heapSwap(&heap[i], &heap[child]);
        i = child;
    }
}

long long kthLargestLevelSum(struct TreeNode* root, int k) {
    if (!root) return -1;

    // Queue for BFS
    int maxNodes = 100005;               // per constraints n <= 1e5
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * (maxNodes + 5));
    int front = 0, back = 0;
    queue[back++] = root;

    // Min-heap of size at most k
    long long *heap = (long long *)malloc(sizeof(long long) * (k + 2));
    int heapSize = 0;

    while (front < back) {
        int levelCount = back - front;
        long long sum = 0;
        for (int i = 0; i < levelCount; ++i) {
            struct TreeNode *node = queue[front++];
            sum += node->val;
            if (node->left)  queue[back++] = node->left;
            if (node->right) queue[back++] = node->right;
        }
        heapPush(heap, &heapSize, sum);
        if (heapSize > k) {
            heapPopMin(heap, &heapSize);
        }
    }

    long long result = -1;
    if (heapSize == k) {
        result = heap[1];   // smallest among the top k => kth largest overall
    }

    free(queue);
    free(heap);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public long KthLargestLevelSum(TreeNode root, int k) {
        if (root == null) return -1;

        var bfsQueue = new Queue<TreeNode>();
        bfsQueue.Enqueue(root);

        var minHeap = new PriorityQueue<long, long>(); // element, priority

        while (bfsQueue.Count > 0) {
            int levelSize = bfsQueue.Count;
            long sum = 0;
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = bfsQueue.Dequeue();
                sum += node.val;
                if (node.left != null) bfsQueue.Enqueue(node.left);
                if (node.right != null) bfsQueue.Enqueue(node.right);
            }
            minHeap.Enqueue(sum, sum);
            if (minHeap.Count > k) {
                minHeap.Dequeue(); // discard smallest
            }
        }

        return minHeap.Count < k ? -1 : minHeap.Peek();
    }
}
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/* Min-heap for numbers */
class MinHeap {
    constructor() {
        this.heap = [];
    }
    size() {
        return this.heap.length;
    }
    peek() {
        return this.heap[0];
    }
    push(val) {
        const h = this.heap;
        h.push(val);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p] <= h[i]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    }
    pop() {
        const h = this.heap;
        if (h.length === 0) return undefined;
        const root = h[0];
        const last = h.pop();
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1,
                    r = l + 1,
                    smallest = i;
                if (l < h.length && h[l] < h[smallest]) smallest = l;
                if (r < h.length && h[r] < h[smallest]) smallest = r;
                if (smallest === i) break;
                [h[i], h[smallest]] = [h[smallest], h[i]];
                i = smallest;
            }
        }
        return root;
    }
}

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthLargestLevelSum = function (root, k) {
    if (!root) return -1;

    const heap = new MinHeap();
    const queue = [root];
    let head = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        let sum = 0;
        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        heap.push(sum);
        if (heap.size() > k) heap.pop(); // keep only k largest sums
    }

    return heap.size() < k ? -1 : heap.peek();
};
```

## Typescript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function kthLargestLevelSum(root: TreeNode | null, k: number): number {
    if (!root) return -1;
    const queue: (TreeNode | null)[] = [root];
    let head = 0;
    const levelSums: number[] = [];

    while (head < queue.length) {
        const size = queue.length - head; // nodes at current level
        let sum = 0;
        for (let i = 0; i < size; i++) {
            const node = queue[head++];
            if (!node) continue;
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        levelSums.push(sum);
    }

    if (levelSums.length < k) return -1;
    levelSums.sort((a, b) => b - a); // descending
    return levelSums[k - 1];
}
```

## Php

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @param Integer $k
     * @return Integer
     */
    function kthLargestLevelSum($root, $k) {
        if ($root === null) {
            return -1;
        }

        $queue = new SplQueue();
        $queue->enqueue($root);

        $minHeap = new SplMinHeap();

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $sum = 0;

            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $sum += $node->val;
                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            $minHeap->insert($sum);
            if ($minHeap->count() > $k) {
                $minHeap->extract(); // remove smallest to keep only k largest sums
            }
        }

        if ($minHeap->count() < $k) {
            return -1;
        }

        return $minHeap->top();
    }
}
```

## Swift

```swift
struct MinHeap {
    private var data: [Int] = []
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Int? {
        guard !data.isEmpty else { return nil }
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return result
    }
    
    func peek() -> Int? {
        return data.first
    }
    
    var count: Int {
        return data.count
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if data[child] < data[parent] {
                data.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left] < data[smallest] {
                smallest = left
            }
            if right < data.count && data[right] < data[smallest] {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func kthLargestLevelSum(_ root: TreeNode?, _ k: Int) -> Int {
        guard let root = root else { return -1 }
        var queue: [TreeNode] = [root]
        var index = 0
        var heap = MinHeap()
        
        while index < queue.count {
            let levelSize = queue.count - index
            var sum = 0
            for _ in 0..<levelSize {
                let node = queue[index]
                index += 1
                sum += node.val
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            heap.push(sum)
            if heap.count > k {
                _ = heap.pop()
            }
        }
        
        return heap.count < k ? -1 : (heap.peek() ?? -1)
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun kthLargestLevelSum(root: TreeNode?, k: Int): Long {
        if (root == null) return -1L
        val queue: java.util.ArrayDeque<TreeNode> = java.util.ArrayDeque()
        queue.add(root)
        val minHeap = java.util.PriorityQueue<Long>()
        while (queue.isNotEmpty()) {
            var levelSize = queue.size
            var sum = 0L
            repeat(levelSize) {
                val node = queue.removeFirst()
                sum += node.`val`.toLong()
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            minHeap.offer(sum)
            if (minHeap.size > k) {
                minHeap.poll()
            }
        }
        return if (minHeap.size < k) -1L else minHeap.peek()
    }
}
```

## Dart

```dart
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  int kthLargestLevelSum(TreeNode? root, int k) {
    if (root == null) return -1;

    List<TreeNode> queue = [root];
    int front = 0;
    List<int> levelSums = [];

    while (front < queue.length) {
      int levelSize = queue.length - front;
      int sum = 0;
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue[front++];
        sum += node.val;
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      levelSums.add(sum);
    }

    if (levelSums.length < k) return -1;

    levelSums.sort((a, b) => b.compareTo(a)); // descending
    return levelSums[k - 1];
  }
}
```

## Golang

```go
import "container/heap"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

type int64MinHeap []int64

func (h int64MinHeap) Len() int           { return len(h) }
func (h int64MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h int64MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *int64MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int64))
}

func (h *int64MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kthLargestLevelSum(root *TreeNode, k int) int64 {
	if root == nil {
		return -1
	}
	queue := []*TreeNode{root}
	h := &int64MinHeap{}
	heap.Init(h)

	for len(queue) > 0 {
		n := len(queue)
		var sum int64
		next := make([]*TreeNode, 0, n*2)
		for i := 0; i < n; i++ {
			node := queue[i]
			sum += int64(node.Val)
			if node.Left != nil {
				next = append(next, node.Left)
			}
			if node.Right != nil {
				next = append(next, node.Right)
			}
		}
		if h.Len() < k {
			heap.Push(h, sum)
		} else if sum > (*h)[0] {
			heap.Pop(h)
			heap.Push(h, sum)
		}
		queue = next
	}

	if h.Len() < k {
		return -1
	}
	return (*h)[0]
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def kth_largest_level_sum(root, k)
  return -1 unless root

  sums = []
  queue = [root]
  head = 0

  while head < queue.length
    level_size = queue.length - head
    level_sum = 0
    level_size.times do
      node = queue[head]
      head += 1
      level_sum += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    sums << level_sum
  end

  return -1 if sums.length < k
  sums.sort!
  sums[-k]
end
```

## Scala

```scala
object Solution {
    def kthLargestLevelSum(root: TreeNode, k: Int): Long = {
        if (root == null) return -1L
        val queue = new java.util.ArrayDeque[TreeNode]()
        queue.offer(root)
        val minHeap = new java.util.PriorityQueue[Long]()
        while (!queue.isEmpty) {
            var levelSize = queue.size()
            var sum: Long = 0L
            var i = 0
            while (i < levelSize) {
                val node = queue.poll()
                sum += node.value.toLong
                if (node.left != null) queue.offer(node.left)
                if (node.right != null) queue.offer(node.right)
                i += 1
            }
            minHeap.offer(sum)
            if (minHeap.size() > k) {
                minHeap.poll()
            }
        }
        if (minHeap.size() < k) -1L else minHeap.peek()
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{VecDeque, BinaryHeap};
use std::cmp::Reverse;

impl Solution {
    pub fn kth_largest_level_sum(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i64 {
        if root.is_none() {
            return -1;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        let k_usize = k as usize;

        while !queue.is_empty() {
            let level_len = queue.len();
            let mut sum: i64 = 0;
            for _ in 0..level_len {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    sum += node_ref.val as i64;
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
            heap.push(Reverse(sum));
            if heap.len() > k_usize {
                heap.pop();
            }
        }

        if heap.len() < k_usize {
            -1
        } else {
            heap.peek().unwrap().0
        }
    }
}
```

## Racket

```racket
#|
; Definition for a binary tree node.
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(require racket/list)

(define/contract (kth-largest-level-sum root k)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (if (not root)
      -1
      (let loop ((queue (list root)) (sums '()))
        (if (null? queue)
            (let* ((sorted (sort sums >)))
              (if (< (length sorted) k) -1 (list-ref sorted (- k 1))))
            (let* ((level-size (length queue))
                   (process-level
                    (let loop2 ((i 0) (q queue) (sum 0) (next '()))
                      (if (= i level-size)
                          (values sum (reverse next))
                          (let* ((node (car q))
                                 (val (tree-node-val node))
                                 (new-sum (+ sum val))
                                 (left (tree-node-left node))
                                 (right (tree-node-right node))
                                 (next2 (if left (cons left next) next))
                                 (next3 (if right (cons right next2) next2)))
                            (loop2 (add1 i) (cdr q) new-sum next3))))))
              (call-with-values process-level
                (lambda (level-sum next-queue)
                  (loop next-queue (cons level-sum sums)))))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec kth_largest_level_sum(Root :: #tree_node{} | null, K :: integer()) -> integer().
kth_largest_level_sum(null, _K) ->
    -1;
kth_largest_level_sum(_Root, K) when K =< 0 ->
    -1;
kth_largest_level_sum(Root, K) ->
    LevelSums = bfs(queue:in(Root, queue:new()), []),
    case length(LevelSums) < K of
        true -> -1;
        false ->
            Sorted = lists:sort(fun(A, B) -> A > B end, LevelSums),
            lists:nth(K, Sorted)
    end.

bfs(Q, Acc) ->
    case queue:is_empty(Q) of
        true -> lists:reverse(Acc);
        false ->
            {Sum, NextQ} = process_level(Q, 0, queue:new()),
            bfs(NextQ, [Sum | Acc])
    end.

process_level(Q, SumAcc, NextQ) ->
    case queue:out(Q) of
        {empty, _} ->
            {SumAcc, NextQ};
        {{value, Node}, RestQ} ->
            NewSum = SumAcc + Node#tree_node.val,
            Q1 = maybe_in(Node#tree_node.left, NextQ),
            Q2 = maybe_in(Node#tree_node.right, Q1),
            process_level(RestQ, NewSum, Q2)
    end.

maybe_in(null, Q) -> Q;
maybe_in(Node, Q) -> queue:in(Node, Q).
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_largest_level_sum(root :: TreeNode.t() | nil, k :: integer) :: integer
  def kth_largest_level_sum(root, k) do
    if root == nil do
      -1
    else
      sums = bfs([root], [])
      if length(sums) < k do
        -1
      else
        sums
        |> Enum.sort(&>=/2)
        |> Enum.at(k - 1)
      end
    end
  end

  defp bfs([], acc), do: Enum.reverse(acc)

  defp bfs(nodes, acc) do
    sum = Enum.reduce(nodes, 0, fn %TreeNode{val: v}, s -> s + v end)

    next_nodes =
      Enum.flat_map(nodes, fn %TreeNode{left: l, right: r} ->
        [l, r] |> Enum.filter(& &1)
      end)

    bfs(next_nodes, [sum | acc])
  end
end
```
