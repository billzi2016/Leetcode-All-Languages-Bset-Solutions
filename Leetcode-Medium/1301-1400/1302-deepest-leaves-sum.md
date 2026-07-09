# 1302. Deepest Leaves Sum

## Cpp

```cpp
/ **
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
    int deepestLeavesSum(TreeNode* root) {
        if (!root) return 0;
        std::queue<TreeNode*> q;
        q.push(root);
        int levelSum = 0;
        while (!q.empty()) {
            int sz = q.size();
            levelSum = 0; // reset for current level
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                levelSum += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return levelSum;
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
    public int deepestLeavesSum(TreeNode root) {
        if (root == null) return 0;
        java.util.Queue<TreeNode> queue = new java.util.LinkedList<>();
        queue.offer(root);
        int sum = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            sum = 0; // reset for current level
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return sum;
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
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        q = collections.deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level_sum
```

## Python3

```python
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level_sum
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
static void dfs(struct TreeNode* node, int depth, int* maxDepth, long long* sum) {
    if (!node) return;
    if (depth > *maxDepth) {
        *maxDepth = depth;
        *sum = node->val;
    } else if (depth == *maxDepth) {
        *sum += node->val;
    }
    dfs(node->left, depth + 1, maxDepth, sum);
    dfs(node->right, depth + 1, maxDepth, sum);
}

int deepestLeavesSum(struct TreeNode* root) {
    int maxDepth = -1;
    long long sum = 0;
    dfs(root, 0, &maxDepth, &sum);
    return (int)sum;
}
```

## Csharp

```csharp
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
    public int DeepestLeavesSum(TreeNode root) {
        if (root == null) return 0;
        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        int levelSum = 0;
        while (queue.Count > 0) {
            int size = queue.Count;
            levelSum = 0;
            for (int i = 0; i < size; i++) {
                var node = queue.Dequeue();
                levelSum += node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
        }
        return levelSum;
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
var deepestLeavesSum = function(root) {
    if (!root) return 0;
    const queue = [root];
    let idx = 0;
    let sum = 0;
    while (idx < queue.length) {
        const levelSize = queue.length - idx;
        sum = 0;
        for (let i = 0; i < levelSize; i++) {
            const node = queue[idx++];
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
    return sum;
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

function deepestLeavesSum(root: TreeNode | null): number {
    if (!root) return 0;
    let queue: TreeNode[] = [root];
    let sum = 0;
    while (queue.length) {
        const levelSize = queue.length;
        sum = 0; // reset for current level
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
    return sum;
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
     * @return Integer
     */
    function deepestLeavesSum($root) {
        if ($root === null) {
            return 0;
        }
        $queue = new SplQueue();
        $queue->enqueue($root);
        $sum = 0;
        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $sum = 0; // reset sum for current level
            for ($i = 0; $i < $levelSize; $i++) {
                $node = $queue->dequeue();
                $sum += $node->val;
                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }
        }
        return $sum;
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
    func deepestLeavesSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var queue: [TreeNode] = [root]
        var result = 0
        
        while !queue.isEmpty {
            var nextLevel: [TreeNode] = []
            var levelSum = 0
            for node in queue {
                levelSum += node.val
                if let left = node.left { nextLevel.append(left) }
                if let right = node.right { nextLevel.append(right) }
            }
            result = levelSum
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
    fun deepestLeavesSum(root: TreeNode?): Int {
        if (root == null) return 0
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        var levelSum = 0
        while (queue.isNotEmpty()) {
            val size = queue.size
            levelSum = 0
            repeat(size) {
                val node = queue.removeFirst()
                levelSum += node.`val`
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
        }
        return levelSum
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
  int deepestLeavesSum(TreeNode? root) {
    if (root == null) return 0;
    final Queue<TreeNode> q = Queue<TreeNode>();
    q.add(root);
    int levelSum = 0;
    while (q.isNotEmpty) {
      int size = q.length;
      levelSum = 0;
      for (int i = 0; i < size; ++i) {
        final node = q.removeFirst();
        levelSum += node.val;
        if (node.left != null) q.add(node.left!);
        if (node.right != null) q.add(node.right!);
      }
    }
    return levelSum;
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
func deepestLeavesSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	var sum int
	for len(queue) > 0 {
		levelSize := len(queue)
		sum = 0
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return sum
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

def deepest_leaves_sum(root)
  return 0 unless root
  queue = [root]
  last_level_sum = 0
  until queue.empty?
    level_size = queue.size
    current_sum = 0
    level_size.times do
      node = queue.shift
      current_sum += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    last_level_sum = current_sum
  end
  last_level_sum
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
    def deepestLeavesSum(root: TreeNode): Int = {
        import scala.collection.mutable.Queue
        val q = Queue[TreeNode]()
        q.enqueue(root)
        var sum = 0
        while (q.nonEmpty) {
            val levelSize = q.size
            sum = 0
            for (_ <- 0 until levelSize) {
                val node = q.dequeue()
                sum += node.value
                if (node.left != null) q.enqueue(node.left)
                if (node.right != null) q.enqueue(node.right)
            }
        }
        sum
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut queue = std::collections::VecDeque::new();
        if let Some(node) = root {
            queue.push_back(node);
        } else {
            return 0;
        }
        let mut sum = 0;
        while !queue.is_empty() {
            let level_size = queue.len();
            sum = 0;
            for _ in 0..level_size {
                if let Some(rc_node) = queue.pop_front() {
                    let node_ref = rc_node.borrow();
                    sum += node_ref.val;
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
        }
        sum
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

(define/contract (deepest-leaves-sum root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec
      ((max-depth
        (lambda (node)
          (if (not node)
              -1
              (+ 1 (max (max-depth (tree-node-left node))
                        (max-depth (tree-node-right node)))))))
       (sum-at-depth
        (lambda (node d)
          (if (not node)
              0
              (if (= d 0)
                  (tree-node-val node)
                  (+ (sum-at-depth (tree-node-left node) (- d 1))
                     (sum-at-depth (tree-node-right node) (- d 1))))))))
    (let ((md (max-depth root)))
      (sum-at-depth root md))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec deepest_leaves_sum(Root :: #tree_node{} | null) -> integer().
deepest_leaves_sum(null) ->
    0;
deepest_leaves_sum(Root) ->
    Depth = max_depth(Root),
    sum_deep(Root, Depth, 1).

max_depth(null) ->
    0;
max_depth(#tree_node{left = L, right = R}) ->
    1 + erlang:max(max_depth(L), max_depth(R)).

sum_deep(null, _TargetDepth, _CurrDepth) ->
    0;
sum_deep(#tree_node{val = V, left = L, right = R}, TargetDepth, CurrDepth) ->
    NewDepth = CurrDepth + 1,
    case CurrDepth of
        TargetDepth ->
            V + sum_deep(L, TargetDepth, NewDepth) + sum_deep(R, TargetDepth, NewDepth);
        _ ->
            sum_deep(L, TargetDepth, NewDepth) + sum_deep(R, TargetDepth, NewDepth)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec deepest_leaves_sum(root :: TreeNode.t() | nil) :: integer
  def deepest_leaves_sum(nil), do: 0
  def deepest_leaves_sum(root) do
    bfs([root])
  end

  defp bfs(nodes) do
    sum = Enum.reduce(nodes, 0, fn n, acc -> acc + n.val end)

    children =
      nodes
      |> Enum.flat_map(fn n ->
        [n.left, n.right]
        |> Enum.filter(& &1)
      end)

    if children == [] do
      sum
    else
      bfs(children)
    end
  end
end
```
