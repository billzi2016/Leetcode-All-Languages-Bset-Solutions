# 0662. Maximum Width of Binary Tree

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
    int widthOfBinaryTree(TreeNode* root) {
        if (!root) return 0;
        using ull = unsigned long long;
        queue<pair<TreeNode*, ull>> q;
        q.emplace(root, 0);
        int maxWidth = 1;
        while (!q.empty()) {
            size_t sz = q.size();
            ull leftMost = q.front().second;
            ull rightMost = leftMost; // will be updated
            for (size_t i = 0; i < sz; ++i) {
                auto [node, idx] = q.front();
                q.pop();
                if (i == sz - 1) rightMost = idx;
                if (node->left)
                    q.emplace(node->left, idx * 2 + 1);
                if (node->right)
                    q.emplace(node->right, idx * 2 + 2);
            }
            int width = static_cast<int>(rightMost - leftMost + 1);
            maxWidth = max(maxWidth, width);
        }
        return maxWidth;
    }
};
```

## Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        long maxWidth = 1;
        java.util.Queue<TreeNode> nodeQueue = new java.util.ArrayDeque<>();
        java.util.Queue<Long> indexQueue = new java.util.ArrayDeque<>();
        nodeQueue.offer(root);
        indexQueue.offer(0L); // start with index 0
        while (!nodeQueue.isEmpty()) {
            int size = nodeQueue.size();
            long levelStart = indexQueue.peek(); // first index of this level (raw)
            long first = 0, last = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = nodeQueue.poll();
                long idx = indexQueue.poll() - levelStart; // normalize to avoid overflow
                if (i == 0) first = idx;
                if (i == size - 1) last = idx;
                if (node.left != null) {
                    nodeQueue.offer(node.left);
                    indexQueue.offer(idx * 2);
                }
                if (node.right != null) {
                    nodeQueue.offer(node.right);
                    indexQueue.offer(idx * 2 + 1);
                }
            }
            maxWidth = Math.max(maxWidth, last - first + 1);
        }
        return (int) maxWidth;
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
import collections

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        max_width = 0
        q = collections.deque([(root, 0)])
        while q:
            level_len = len(q)
            _, first_idx = q[0]
            for i in range(level_len):
                node, idx = q.popleft()
                # normalize to prevent large numbers
                cur_idx = idx - first_idx
                if i == level_len - 1:
                    last_idx = cur_idx
                if node.left:
                    q.append((node.left, 2 * cur_idx))
                if node.right:
                    q.append((node.right, 2 * cur_idx + 1))
            max_width = max(max_width, last_idx + 1)
        return max_width
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
import collections

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        q = collections.deque([(root, 0)])
        while q:
            level_len = len(q)
            _, first_idx = q[0]
            last_idx = first_idx
            for _ in range(level_len):
                node, idx = q.popleft()
                last_idx = idx
                if node.left:
                    q.append((node.left, idx * 2 + 1))
                if node.right:
                    q.append((node.right, idx * 2 + 2))
            max_width = max(max_width, last_idx - first_idx + 1)
        return max_width
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
int widthOfBinaryTree(struct TreeNode* root) {
    if (!root) return 0;

    int capacity = 6000; // sufficient for up to 3000 nodes
    struct TreeNode **nodeQueue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * capacity);
    unsigned long long *idxQueue = (unsigned long long *)malloc(sizeof(unsigned long long) * capacity);

    int head = 0, tail = 0;
    nodeQueue[tail] = root;
    idxQueue[tail++] = 1; // start index from 1

    unsigned long long maxWidth = 0;

    while (head < tail) {
        int levelSize = tail - head;
        unsigned long long levelStart = idxQueue[head];
        unsigned long long levelEnd   = idxQueue[head + levelSize - 1];
        unsigned long long width = levelEnd - levelStart + 1;
        if (width > maxWidth) maxWidth = width;

        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode *node = nodeQueue[head];
            unsigned long long curIdx = idxQueue[head] - levelStart; // normalize to prevent overflow
            head++;

            if (node->left) {
                nodeQueue[tail] = node->left;
                idxQueue[tail++] = 2 * curIdx + 1;
            }
            if (node->right) {
                nodeQueue[tail] = node->right;
                idxQueue[tail++] = 2 * curIdx + 2;
            }
        }
    }

    free(nodeQueue);
    free(idxQueue);
    return (int)maxWidth;
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
    public int WidthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;

        var queue = new Queue<(TreeNode node, ulong idx)>();
        queue.Enqueue((root, 0));
        ulong maxWidth = 1;

        while (queue.Count > 0) {
            int levelCount = queue.Count;
            ulong levelMin = queue.Peek().idx; // smallest index at this level for normalization
            ulong firstIdx = 0, lastIdx = 0;

            for (int i = 0; i < levelCount; i++) {
                var (node, idx) = queue.Dequeue();
                idx -= levelMin; // normalize to prevent overflow

                if (i == 0) firstIdx = idx;
                if (i == levelCount - 1) lastIdx = idx;

                if (node.left != null)
                    queue.Enqueue((node.left, 2 * idx + 1));
                if (node.right != null)
                    queue.Enqueue((node.right, 2 * idx + 2));
            }

            ulong width = lastIdx - firstIdx + 1;
            if (width > maxWidth) maxWidth = width;
        }

        return (int)maxWidth;
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
/**
 * @param {TreeNode} root
 * @return {number}
 */
var widthOfBinaryTree = function(root) {
    if (!root) return 0;
    let maxWidth = 0;
    const nodes = [root];
    const idxs = [0n]; // use BigInt to avoid overflow
    let head = 0;

    while (head < nodes.length) {
        const levelSize = nodes.length - head;
        const firstIdx = idxs[head];
        let lastIdx = firstIdx;

        for (let i = 0; i < levelSize; i++) {
            const node = nodes[head];
            const idx = idxs[head];
            if (i === levelSize - 1) lastIdx = idx;
            head++;

            if (node.left) {
                nodes.push(node.left);
                idxs.push(idx * 2n + 1n);
            }
            if (node.right) {
                nodes.push(node.right);
                idxs.push(idx * 2n + 2n);
            }
        }

        const width = Number(lastIdx - firstIdx + 1n);
        if (width > maxWidth) maxWidth = width;
    }

    return maxWidth;
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

function widthOfBinaryTree(root: TreeNode | null): number {
    if (!root) return 0;
    let maxWidth = 0;
    const queue: Array<[TreeNode, number]> = [[root, 0]];
    let head = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        const levelFirstIdx = queue[head][1];
        let first = 0, last = 0;

        for (let i = 0; i < levelSize; i++) {
            const [node, idx] = queue[head++];
            const curIdx = idx - levelFirstIdx; // normalize to prevent overflow
            if (i === 0) first = curIdx;
            if (i === levelSize - 1) last = curIdx;

            if (node.left) {
                queue.push([node.left, curIdx * 2]);
            }
            if (node.right) {
                queue.push([node.right, curIdx * 2 + 1]);
            }
        }

        const width = last - first + 1;
        if (width > maxWidth) maxWidth = width;
    }

    return maxWidth;
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
     * @return int
     */
    function widthOfBinaryTree($root) {
        if ($root === null) {
            return 0;
        }

        $queue = new SplQueue();
        // store [node, index]
        $queue->enqueue([$root, 0]);
        $maxWidth = 1;

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $firstIdx = null;
            $lastIdx = null;
            $offset = null; // index of first node in this level for normalization

            for ($i = 0; $i < $levelSize; $i++) {
                [$node, $idx] = $queue->dequeue();

                if ($i === 0) {
                    $offset = $idx;
                    $firstIdx = 0; // normalized
                }
                $curIdx = $idx - $offset;

                if ($i === $levelSize - 1) {
                    $lastIdx = $curIdx;
                }

                if ($node->left !== null) {
                    $queue->enqueue([$node->left, $curIdx * 2 + 1]);
                }
                if ($node->right !== null) {
                    $queue->enqueue([$node->right, $curIdx * 2 + 2]);
                }
            }

            // width of current level
            $width = $lastIdx - $firstIdx + 1;
            if ($width > $maxWidth) {
                $maxWidth = $width;
            }
        }

        return $maxWidth;
    }
}
```

## Swift

```swift
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
    func widthOfBinaryTree(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var queue: [(node: TreeNode, index: UInt64)] = [(root, 0)]
        var head = 0
        var maxWidth = 0
        
        while head < queue.count {
            let levelCount = queue.count - head
            let firstIdx = queue[head].index
            var lastIdx = firstIdx
            
            for _ in 0..<levelCount {
                let (node, idx) = queue[head]
                head += 1
                lastIdx = idx
                
                if let left = node.left {
                    queue.append((left, idx * 2))
                }
                if let right = node.right {
                    queue.append((right, idx * 2 + 1))
                }
            }
            
            let width = Int(lastIdx - firstIdx + 1)
            if width > maxWidth { maxWidth = width }
        }
        
        return maxWidth
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

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
    fun widthOfBinaryTree(root: TreeNode?): Int {
        if (root == null) return 0
        var maxWidth = 0L
        val queue: ArrayDeque<Pair<TreeNode, Long>> = ArrayDeque()
        queue.add(Pair(root, 0L))
        while (queue.isNotEmpty()) {
            val size = queue.size
            val levelStart = queue.peekFirst().second
            var firstIdx = 0L
            var lastIdx = 0L
            for (i in 0 until size) {
                val (node, idx) = queue.pollFirst()!!
                val curIdx = idx - levelStart
                if (i == 0) firstIdx = curIdx
                if (i == size - 1) lastIdx = curIdx
                node.left?.let { queue.add(Pair(it, curIdx * 2 + 1)) }
                node.right?.let { queue.add(Pair(it, curIdx * 2 + 2)) }
            }
            val width = lastIdx - firstIdx + 1
            if (width > maxWidth) maxWidth = width
        }
        return maxWidth.toInt()
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
import 'dart:collection';
import 'dart:math' as math;

class Solution {
  int widthOfBinaryTree(TreeNode? root) {
    if (root == null) return 0;
    final Queue<TreeNode> nodeQueue = Queue<TreeNode>();
    final Queue<int> indexQueue = Queue<int>();
    nodeQueue.addLast(root);
    indexQueue.addLast(0);
    int maxWidth = 1;

    while (nodeQueue.isNotEmpty) {
      final int levelSize = nodeQueue.length;
      final int firstIdx = indexQueue.first;
      final int lastIdx = indexQueue.last;
      maxWidth = math.max(maxWidth, lastIdx - firstIdx + 1);

      for (int i = 0; i < levelSize; i++) {
        final TreeNode node = nodeQueue.removeFirst();
        final int idx = indexQueue.removeFirst();

        if (node.left != null) {
          nodeQueue.addLast(node.left!);
          indexQueue.addLast(idx * 2);
        }
        if (node.right != null) {
          nodeQueue.addLast(node.right!);
          indexQueue.addLast(idx * 2 + 1);
        }
      }
    }

    return maxWidth;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func widthOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	type nodeInfo struct {
		node *TreeNode
		idx  uint64
	}
	queue := []nodeInfo{{root, 0}}
	maxWidth := 0

	for len(queue) > 0 {
		size := len(queue)
		firstIdx := queue[0].idx
		lastIdx := queue[size-1].idx
		if w := int(lastIdx - firstIdx + 1); w > maxWidth {
			maxWidth = w
		}
		nextQueue := make([]nodeInfo, 0, size*2)
		for i := 0; i < size; i++ {
			cur := queue[i]
			relIdx := cur.idx - firstIdx // normalize to prevent overflow
			if cur.node.Left != nil {
				nextQueue = append(nextQueue, nodeInfo{cur.node.Left, relIdx * 2})
			}
			if cur.node.Right != nil {
				nextQueue = append(nextQueue, nodeInfo{cur.node.Right, relIdx*2 + 1})
			}
		}
		queue = nextQueue
	}
	return maxWidth
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

def width_of_binary_tree(root)
  return 0 unless root
  queue = [[root, 0]]
  front = 0
  max_width = 0

  while front < queue.size
    level_size = queue.size - front
    level_min = queue[front][1]
    first = nil
    last = nil

    level_size.times do
      node, idx = queue[front]
      front += 1
      cur_idx = idx - level_min
      first = cur_idx if first.nil?
      last = cur_idx

      if node.left
        queue << [node.left, 2 * cur_idx + 1]
      end
      if node.right
        queue << [node.right, 2 * cur_idx + 2]
      end
    end

    width = last - first + 1
    max_width = width if width > max_width
  end

  max_width
end
```

## Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
import scala.collection.mutable

object Solution {
  def widthOfBinaryTree(root: TreeNode): Int = {
    if (root == null) return 0
    val q = mutable.Queue[(TreeNode, Long)]()
    q.enqueue((root, 0L))
    var maxWidth: Long = 0L

    while (q.nonEmpty) {
      val levelSize = q.size
      val levelOffset = q.head._2 // index of first node in this level
      var firstIdx: Long = 0L
      var lastIdx: Long = 0L

      for (i <- 0 until levelSize) {
        val (node, idx) = q.dequeue()
        val normIdx = idx - levelOffset
        if (i == 0) firstIdx = normIdx
        if (i == levelSize - 1) lastIdx = normIdx

        if (node.left != null)  q.enqueue((node.left, normIdx * 2))
        if (node.right != null) q.enqueue((node.right, normIdx * 2 + 1))
      }

      maxWidth = math.max(maxWidth, lastIdx - firstIdx + 1)
    }

    maxWidth.toInt
  }
}
```

## Rust

```rust
use std::cell::RefCell;
use std::rc::Rc;
use std::collections::VecDeque;

impl Solution {
    pub fn width_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut max_width: u64 = 0;
        let mut queue: VecDeque<(Rc<RefCell<TreeNode>>, u64)> = VecDeque::new();
        queue.push_back((root.unwrap(), 0));

        while !queue.is_empty() {
            let level_len = queue.len();
            let level_start = queue.front().unwrap().1; // index of first node in this level
            let mut first: u64 = 0;
            let mut last: u64 = 0;

            for i in 0..level_len {
                let (node_rc, idx) = queue.pop_front().unwrap();
                let cur_idx = idx - level_start; // normalize to prevent overflow

                if i == 0 { first = cur_idx; }
                if i == level_len - 1 { last = cur_idx; }

                let left_opt = node_rc.borrow().left.clone();
                if let Some(left) = left_opt {
                    queue.push_back((left, cur_idx * 2 + 1));
                }
                let right_opt = node_rc.borrow().right.clone();
                if let Some(right) = right_opt {
                    queue.push_back((right, cur_idx * 2 + 2));
                }
            }

            let width = last - first + 1;
            if width > max_width {
                max_width = width;
            }
        }

        max_width as i32
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

(define/contract (width-of-binary-tree root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let loop ((curr (list (cons root 0))) (maxw 1))
        (if (null? curr)
            maxw
            (let* ((first-idx (cdr (car curr)))
                   (last-idx (cdr (car (reverse curr))))
                   (width (+ (- last-idx first-idx) 1))
                   (new-max (if (> width maxw) width maxw))
                   ;; build next level list with positional indices
                   (next
                    (let build ((lst curr) (acc '()))
                      (if (null? lst)
                          (reverse acc)
                          (let* ((pair (car lst))
                                 (node (car pair))
                                 (idx (cdr pair))
                                 (left (tree-node-left node))
                                 (right (tree-node-right node))
                                 (acc1 (if left
                                           (cons (cons left (+ (* 2 idx) 1)) acc)
                                           acc))
                                 (acc2 (if right
                                           (cons (cons right (+ (* 2 idx) 2)) acc1)
                                           acc1)))
                            (build (cdr lst) acc2))))))
              (loop next new-max))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec width_of_binary_tree(Root :: #tree_node{} | null) -> integer().
width_of_binary_tree(null) ->
    0;
width_of_binary_tree(Root) ->
    bfs([{Root, 1}], 0).

bfs([], Max) ->
    Max;
bfs(LevelQueue, Max) ->
    [{_, FirstIdx} | _] = LevelQueue,
    {_, LastIdx} = lists:last(LevelQueue),
    Width = LastIdx - FirstIdx + 1,
    NewMax = erlang:max(Max, Width),
    NextQueue = build_next(LevelQueue, []),
    bfs(NextQueue, NewMax).

build_next([], Acc) ->
    lists:reverse(Acc);
build_next([{Node, Id} | Rest], Acc) ->
    #tree_node{left = Left, right = Right} = Node,
    Acc1 = case Left of
        null -> Acc;
        _ -> [{Left, Id * 2} | Acc]
    end,
    Acc2 = case Right of
        null -> Acc1;
        _ -> [{Right, Id * 2 + 1} | Acc1]
    end,
    build_next(Rest, Acc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec width_of_binary_tree(root :: TreeNode.t() | nil) :: integer
  def width_of_binary_tree(nil), do: 0

  def width_of_binary_tree(root) do
    bfs([{root, 0}], 0)
  end

  defp bfs([], max_width), do: max_width

  defp bfs(queue, max_width) do
    first_idx = elem(List.first(queue), 1)
    last_idx = elem(List.last(queue), 1)
    width = last_idx - first_idx + 1
    new_max = if width > max_width, do: width, else: max_width

    next_queue =
      queue
      |> Enum.reduce([], fn {node, idx}, acc ->
        acc =
          case node.left do
            nil -> acc
            left -> [{left, idx * 2} | acc]
          end

        case node.right do
          nil -> acc
          right -> [{right, idx * 2 + 1} | acc]
        end
      end)
      |> Enum.reverse()

    bfs(next_queue, new_max)
  end
end
```
