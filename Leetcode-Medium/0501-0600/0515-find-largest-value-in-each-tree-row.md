# 0515. Find Largest Value in Each Tree Row

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
    vector<int> largestValues(TreeNode* root) {
        if (!root) return {};
        vector<int> ans;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            int curMax = INT_MIN;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                if (node->val > curMax) curMax = node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans.push_back(curMax);
        }
        return ans;
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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.val > max) max = node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            ans.add(max);
        }
        return ans;
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
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import deque
        q = deque([root])
        res = []
        while q:
            level_max = -10**9  # smaller than any possible node value
            for _ in range(len(q)):
                node = q.popleft()
                if node.val > level_max:
                    level_max = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_max)
        return res
```

## Python3

```python
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result: List[int] = []
        queue = deque([root])
        while queue:
            level_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val > level_max:
                    level_max = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result
```

## C

```c
#include <stdlib.h>
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* largestValues(struct TreeNode* root, int* returnSize) {
    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }
    
    // Maximum possible nodes as per constraints
    const int MAX_NODES = 10005;
    
    // Queue for BFS
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * MAX_NODES);
    int head = 0, tail = 0;
    queue[tail++] = root;
    
    // Result array (at most one entry per level)
    int *ans = (int *)malloc(sizeof(int) * MAX_NODES);
    int levels = 0;
    
    while (head < tail) {
        int sz = tail - head;          // nodes in current level
        int curMax = INT_MIN;
        for (int i = 0; i < sz; ++i) {
            struct TreeNode *node = queue[head++];
            if (node->val > curMax) curMax = node->val;
            if (node->left)  queue[tail++] = node->left;
            if (node->right) queue[tail++] = node->right;
        }
        ans[levels++] = curMax;
    }
    
    free(queue);
    *returnSize = levels;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> LargestValues(TreeNode root) {
        var result = new List<int>();
        if (root == null) return result;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            int levelCount = queue.Count;
            int maxVal = int.MinValue;
            for (int i = 0; i < levelCount; i++) {
                var node = queue.Dequeue();
                if (node.val > maxVal) maxVal = node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            result.Add(maxVal);
        }
        return result;
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
 * @return {number[]}
 */
var largestValues = function(root) {
    if (!root) return [];
    const ans = [];
    const queue = [root];
    
    while (queue.length) {
        const levelSize = queue.length;
        let maxVal = -Infinity;
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            if (node.val > maxVal) maxVal = node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        ans.push(maxVal);
    }
    
    return ans;
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

function largestValues(root: TreeNode | null): number[] {
    if (!root) return [];
    const result: number[] = [];
    const queue: TreeNode[] = [root];
    let head = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head;
        let maxVal = Number.NEGATIVE_INFINITY;
        for (let i = 0; i < levelSize; ++i) {
            const node = queue[head++];
            if (node.val > maxVal) maxVal = node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(maxVal);
    }
    return result;
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
     * @return Integer[]
     */
    function largestValues($root) {
        if ($root === null) {
            return [];
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $maxVal = PHP_INT_MIN;

            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();

                if ($node->val > $maxVal) {
                    $maxVal = $node->val;
                }

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            $result[] = $maxVal;
        }

        return $result;
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
    func largestValues(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }
        var result: [Int] = []
        var queue: [TreeNode] = [root]
        
        while !queue.isEmpty {
            var nextLevel: [TreeNode] = []
            var maxVal = Int.min
            for node in queue {
                if node.val > maxVal { maxVal = node.val }
                if let left = node.left { nextLevel.append(left) }
                if let right = node.right { nextLevel.append(right) }
            }
            result.append(maxVal)
            queue = nextLevel
        }
        
        return result
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
    fun largestValues(root: TreeNode?): List<Int> {
        if (root == null) return emptyList()
        val result = mutableListOf<Int>()
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.addLast(root)
        while (queue.isNotEmpty()) {
            var levelMax = Int.MIN_VALUE
            repeat(queue.size) {
                val node = queue.removeFirst()
                if (node.`val` > levelMax) levelMax = node.`val`
                node.left?.let { queue.addLast(it) }
                node.right?.let { queue.addLast(it) }
            }
            result.add(levelMax)
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

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
  List<int> largestValues(TreeNode? root) {
    if (root == null) return [];
    final List<int> ans = [];
    final Queue<TreeNode> queue = Queue<TreeNode>();
    queue.add(root);
    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      int maxVal = -2147483648; // Minimum possible node value
      for (int i = 0; i < levelSize; i++) {
        final TreeNode node = queue.removeFirst();
        if (node.val > maxVal) maxVal = node.val;
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      ans.add(maxVal);
    }
    return ans;
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
func largestValues(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	ans := []int{}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		maxVal := queue[0].Val
		for i := 0; i < levelSize; i++ {
			node := queue[i]
			if node.Val > maxVal {
				maxVal = node.Val
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		ans = append(ans, maxVal)
		queue = queue[levelSize:]
	}
	return ans
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

def largest_values(root)
  return [] unless root
  result = []
  queue = [root]
  head = 0
  while head < queue.size
    level_size = queue.size - head
    max_val = -Float::INFINITY
    level_size.times do
      node = queue[head]
      head += 1
      max_val = node.val if node.val > max_val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << max_val
  end
  result
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
object Solution {
    def largestValues(root: TreeNode): List[Int] = {
        if (root == null) return Nil
        import scala.collection.mutable.{Queue, ListBuffer}
        val queue = Queue[TreeNode]()
        queue.enqueue(root)
        val result = ListBuffer[Int]()
        while (queue.nonEmpty) {
            var maxVal = Int.MinValue
            val levelSize = queue.size
            for (_ <- 0 until levelSize) {
                val node = queue.dequeue()
                if (node.value > maxVal) maxVal = node.value
                if (node.left != null) queue.enqueue(node.left)
                if (node.right != null) queue.enqueue(node.right)
            }
            result += maxVal
        }
        result.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution;

impl Solution {
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut queue = std::collections::VecDeque::new();

        if let Some(node) = root {
            queue.push_back(node);
        } else {
            return result;
        }

        while !queue.is_empty() {
            let level_len = queue.len();
            let mut max_val = i32::MIN;
            for _ in 0..level_len {
                let rc_node = queue.pop_front().unwrap();
                let node_ref = rc_node.borrow();
                if node_ref.val > max_val {
                    max_val = node_ref.val;
                }
                if let Some(left) = &node_ref.left {
                    queue.push_back(Rc::clone(left));
                }
                if let Some(right) = &node_ref.right {
                    queue.push_back(Rc::clone(right));
                }
            }
            result.push(max_val);
        }

        result
    }
}

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
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

(define/contract (largest-values root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (if (not root)
      '()
      (let loop ((level (list root)) (acc '()))
        (if (null? level)
            (reverse acc)
            (let* ((vals (map tree-node-val level))
                   (maxv (apply max vals))
                   (children
                    (apply append
                           (map (lambda (node)
                                  (let ((l (tree-node-left node))
                                        (r (tree-node-right node)))
                                    (cond [(and l r) (list l r)]
                                          [l (list l)]
                                          [r (list r)]
                                          [else '()])))
                                level))))
              (loop children (cons maxv acc)))))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-export([largest_values/1]).

-spec largest_values(Root :: #tree_node{} | null) -> [integer()].
largest_values(null) ->
    [];
largest_values(Root) ->
    bfs([Root]).

bfs([]) ->
    [];
bfs(Nodes) ->
    InitialMax = (hd(Nodes))#tree_node.val,
    {LevelMax, ChildrenRev} = lists:foldl(
        fun(Node, {CurMax, Acc}) ->
            Val = Node#tree_node.val,
            NewMax = erlang:max(CurMax, Val),
            Acc1 = case Node#tree_node.left of
                null -> Acc;
                L -> [L | Acc]
            end,
            Acc2 = case Node#tree_node.right of
                null -> Acc1;
                R -> [R | Acc1]
            end,
            {NewMax, Acc2}
        end,
        {InitialMax, []},
        Nodes),
    NextLevel = lists:reverse(ChildrenRev),
    [LevelMax | bfs(NextLevel)].
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_values(root :: TreeNode.t | nil) :: [integer]
  def largest_values(nil), do: []

  def largest_values(root) do
    bfs([root], [])
  end

  defp bfs([], acc), do: Enum.reverse(acc)

  defp bfs(current_level, acc) do
    {max_val, next_level} =
      Enum.reduce(current_level, {nil, []}, fn node, {cur_max, nxt} ->
        cur_max =
          case cur_max do
            nil -> node.val
            _ when node.val > cur_max -> node.val
            _ -> cur_max
          end

        nxt = if node.left, do: [node.left | nxt], else: nxt
        nxt = if node.right, do: [node.right | nxt], else: nxt
        {cur_max, nxt}
      end)

    bfs(Enum.reverse(next_level), [max_val | acc])
  end
end
```
