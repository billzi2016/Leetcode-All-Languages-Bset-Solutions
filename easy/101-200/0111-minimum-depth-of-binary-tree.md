# 0111. Minimum Depth of Binary Tree

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
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        std::queue<TreeNode*> q;
        q.push(root);
        int depth = 0;
        while (!q.empty()) {
            ++depth;
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                if (!node->left && !node->right) return depth;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return depth; // never reached
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
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        if (root.left == null) return 1 + right;
        if (root.right == null) return 1 + left;
        return 1 + Math.min(left, right);
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
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return 0
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
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
int minDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    if (!root->left && !root->right) return 1;
    if (!root->left) return 1 + minDepth(root->right);
    if (!root->right) return 1 + minDepth(root->left);
    int left = minDepth(root->left);
    int right = minDepth(root->right);
    return 1 + (left < right ? left : right);
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
    public int MinDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        if (root.left == null) return 1 + MinDepth(root.right);
        if (root.right == null) return 1 + MinDepth(root.left);
        int leftDepth = MinDepth(root.left);
        int rightDepth = MinDepth(root.right);
        return 1 + (leftDepth < rightDepth ? leftDepth : rightDepth);
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
var minDepth = function(root) {
    if (!root) return 0;
    // If one of the subtrees is missing, we must consider the depth of the other subtree.
    if (!root.left && !root.right) return 1;
    if (!root.left) return minDepth(root.right) + 1;
    if (!root.right) return minDepth(root.left) + 1;
    return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
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

function minDepth(root: TreeNode | null): number {
    if (!root) return 0;
    const queue: Array<{node: TreeNode, depth: number}> = [{ node: root, depth: 1 }];
    let idx = 0;
    while (idx < queue.length) {
        const { node, depth } = queue[idx++];
        if (!node.left && !node.right) return depth;
        if (node.left) queue.push({ node: node.left, depth: depth + 1 });
        if (node.right) queue.push({ node: node.right, depth: depth + 1 });
    }
    return 0;
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
    function minDepth($root) {
        if ($root === null) {
            return 0;
        }

        $queue = new SplQueue();
        $queue->enqueue([$root, 1]);

        while (!$queue->isEmpty()) {
            [$node, $depth] = $queue->dequeue();

            if ($node->left === null && $node->right === null) {
                return $depth;
            }

            if ($node->left !== null) {
                $queue->enqueue([$node->left, $depth + 1]);
            }
            if ($node->right !== null) {
                $queue->enqueue([$node->right, $depth + 1]);
            }
        }

        return 0;
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
    func minDepth(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var queue: [TreeNode] = [root]
        var index = 0
        var depth = 1
        
        while index < queue.count {
            let levelCount = queue.count - index
            for _ in 0..<levelCount {
                let node = queue[index]
                index += 1
                if node.left == nil && node.right == nil {
                    return depth
                }
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            depth += 1
        }
        return depth
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
    fun minDepth(root: TreeNode?): Int {
        if (root == null) return 0
        val queue: ArrayDeque<Pair<TreeNode, Int>> = ArrayDeque()
        queue.add(Pair(root, 1))
        while (queue.isNotEmpty()) {
            val (node, depth) = queue.poll()
            if (node.left == null && node.right == null) {
                return depth
            }
            node.left?.let { queue.add(Pair(it, depth + 1)) }
            node.right?.let { queue.add(Pair(it, depth + 1)) }
        }
        return 0
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
  int minDepth(TreeNode? root) {
    if (root == null) return 0;
    List<TreeNode> queue = [root];
    int depth = 0;
    int index = 0;

    while (index < queue.length) {
      int levelCount = queue.length - index;
      depth++;
      for (int i = 0; i < levelCount; i++) {
        TreeNode node = queue[index++];
        if (node.left == null && node.right == null) {
          return depth;
        }
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
    }
    return depth;
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
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := minDepth(root.Left)
	right := minDepth(root.Right)

	if root.Left == nil && root.Right == nil {
		return 1
	}
	if root.Left == nil {
		return right + 1
	}
	if root.Right == nil {
		return left + 1
	}
	if left < right {
		return left + 1
	}
	return right + 1
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

def min_depth(root)
  return 0 if root.nil?
  queue = [[root, 1]]
  until queue.empty?
    node, depth = queue.shift
    return depth if node.left.nil? && node.right.nil?
    queue << [node.left, depth + 1] if node.left
    queue << [node.right, depth + 1] if node.right
  end
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
    def minDepth(root: TreeNode): Int = {
        if (root == null) return 0
        val queue = scala.collection.mutable.Queue[(TreeNode, Int)]()
        queue.enqueue((root, 1))
        while (queue.nonEmpty) {
            val (node, depth) = queue.dequeue()
            if (node.left == null && node.right == null) return depth
            if (node.left != null) queue.enqueue((node.left, depth + 1))
            if (node.right != null) queue.enqueue((node.right, depth + 1))
        }
        0
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

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

impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut queue: VecDeque<(Rc<RefCell<TreeNode>>, i32)> = VecDeque::new();
        queue.push_back((root.unwrap(), 1));
        while let Some((node_rc, depth)) = queue.pop_front() {
            let node_ref = node_rc.borrow();
            let left = node_ref.left.clone();
            let right = node_ref.right.clone();
            if left.is_none() && right.is_none() {
                return depth;
            }
            if let Some(l) = left {
                queue.push_back((l, depth + 1));
            }
            if let Some(r) = right {
                queue.push_back((r, depth + 1));
            }
        }
        0
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (min-depth root)
  (-> (or/c tree-node? #f) exact-integer?)
  (cond
    [(not root) 0]
    [else
     (let ([left (tree-node-left root)]
           [right (tree-node-right root)])
       (cond
         [(and (not left) (not right)) 1]
         [(not left) (+ 1 (min-depth right))]
         [(not right) (+ 1 (min-depth left))]
         [else (+ 1 (min (min-depth left) (min-depth right)))]))]))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec min_depth(Root :: #tree_node{} | null) -> integer().
min_depth(null) ->
    0;
min_depth(Root) ->
    L = min_depth(Root#tree_node.left),
    R = min_depth(Root#tree_node.right),
    if
        L == 0 orelse R == 0 ->
            erlang:max(L, R) + 1;
        true ->
            erlang:min(L, R) + 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_depth(root :: TreeNode.t() | nil) :: integer
  def min_depth(root) do
    case root do
      nil -> 0
      _ ->
        bfs(:queue.in({root, 1}, :queue.new()))
    end
  end

  defp bfs(queue) do
    case :queue.out(queue) do
      {:empty, _} ->
        0

      {{:value, {node, depth}}, q} ->
        if node.left == nil and node.right == nil do
          depth
        else
          q1 = if node.left != nil, do: :queue.in({node.left, depth + 1}, q), else: q
          q2 = if node.right != nil, do: :queue.in({node.right, depth + 1}, q1), else: q1
          bfs(q2)
        end
    end
  end
end
```
