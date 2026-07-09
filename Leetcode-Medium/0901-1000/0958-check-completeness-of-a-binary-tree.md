# 0958. Check Completeness of a Binary Tree

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
    bool isCompleteTree(TreeNode* root) {
        if (!root) return true;
        std::queue<TreeNode*> q;
        q.push(root);
        bool end = false;
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (!node) {
                end = true;
            } else {
                if (end) return false;
                q.push(node->left);
                q.push(node->right);
            }
        }
        return true;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean end = false;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) {
                end = true;
            } else {
                if (end) return false;
                queue.offer(node.left);
                queue.offer(node.right);
            }
        }
        return true;
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
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([root])
        end = False
        while q:
            node = q.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
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
    def isCompleteTree(self, root: Optional['TreeNode']) -> bool:
        if not root:
            return True
        q = deque([root])
        end = False
        while q:
            node = q.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
```

## C

```c
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isCompleteTree(struct TreeNode* root) {
    if (!root) return true;
    struct TreeNode* q[300];
    int front = 0, rear = 0;
    q[rear++] = root;
    bool seenNull = false;
    while (front < rear) {
        struct TreeNode* node = q[front++];
        if (node == NULL) {
            seenNull = true;
        } else {
            if (seenNull) return false;
            q[rear++] = node->left;
            q[rear++] = node->right;
        }
    }
    return true;
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
    public bool IsCompleteTree(TreeNode root) {
        if (root == null) return true;
        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        bool end = false;
        while (queue.Count > 0) {
            var node = queue.Dequeue();
            if (node == null) {
                end = true;
            } else {
                if (end) return false;
                queue.Enqueue(node.left);
                queue.Enqueue(node.right);
            }
        }
        return true;
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
 * @return {boolean}
 */
var isCompleteTree = function(root) {
    if (!root) return true;
    const queue = [root];
    let i = 0;
    let end = false;
    while (i < queue.length) {
        const node = queue[i++];
        if (node === null) {
            end = true;
        } else {
            if (end) return false;
            queue.push(node.left);
            queue.push(node.right);
        }
    }
    return true;
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

function isCompleteTree(root: TreeNode | null): boolean {
    if (!root) return true;
    const queue: Array<TreeNode | null> = [root];
    let end = false;

    while (queue.length) {
        const node = queue.shift()!;
        if (node === null) {
            end = true;
        } else {
            if (end) return false;
            queue.push(node.left);
            queue.push(node.right);
        }
    }

    return true;
}
```

## Php

```php
<?php
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
     * @return bool
     */
    function isCompleteTree($root) {
        if ($root === null) {
            return true;
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $end = false;

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();

            if ($node === null) {
                $end = true;
            } else {
                if ($end) {
                    return false;
                }
                $queue->enqueue($node->left);
                $queue->enqueue($node->right);
            }
        }

        return true;
    }
}
?>
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
    func isCompleteTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        var queue: [TreeNode?] = [root]
        var index = 0
        var seenNil = false
        
        while index < queue.count {
            let node = queue[index]
            index += 1
            
            if let current = node {
                if seenNil { return false }
                queue.append(current.left)
                queue.append(current.right)
            } else {
                seenNil = true
            }
        }
        return true
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
    fun isCompleteTree(root: TreeNode?): Boolean {
        if (root == null) return true
        val queue = ArrayDeque<TreeNode?>()
        queue.add(root)
        var end = false
        while (queue.isNotEmpty()) {
            val node = queue.poll()
            if (node == null) {
                end = true
            } else {
                if (end) return false
                queue.add(node.left)
                queue.add(node.right)
            }
        }
        return true
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
  bool isCompleteTree(TreeNode? root) {
    if (root == null) return true;
    List<TreeNode?> queue = [root];
    int idx = 0;
    bool end = false;

    while (idx < queue.length) {
      TreeNode? node = queue[idx++];
      if (node == null) {
        end = true;
      } else {
        if (end) return false;
        queue.add(node.left);
        queue.add(node.right);
      }
    }
    return true;
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
func isCompleteTree(root *TreeNode) bool {
    if root == nil {
        return true
    }
    queue := []*TreeNode{root}
    end := false
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        if node == nil {
            end = true
        } else {
            if end {
                return false
            }
            queue = append(queue, node.Left)
            queue = append(queue, node.Right)
        }
    }
    return true
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

def is_complete_tree(root)
  return true if root.nil?
  queue = [root]
  end_seen = false
  until queue.empty?
    node = queue.shift
    if node
      return false if end_seen
      queue << node.left
      queue << node.right
    else
      end_seen = true
    end
  end
  true
end
```

## Scala

```scala
import scala.collection.mutable

/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def isCompleteTree(root: TreeNode): Boolean = {
    if (root == null) return true
    val queue = mutable.Queue[TreeNode]()
    queue.enqueue(root)
    var end = false
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      if (node == null) {
        end = true
      } else {
        if (end) return false
        queue.enqueue(node.left)
        queue.enqueue(node.right)
      }
    }
    true
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
    pub fn is_complete_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if root.is_none() {
            return true;
        }
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
        queue.push_back(root);
        let mut seen_null = false;

        while let Some(node_opt) = queue.pop_front() {
            match node_opt {
                None => {
                    seen_null = true;
                }
                Some(node_rc) => {
                    if seen_null {
                        return false;
                    }
                    let node_ref = node_rc.borrow();
                    queue.push_back(node_ref.left.clone());
                    queue.push_back(node_ref.right.clone());
                }
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (is-complete-tree root)
  (-> (or/c tree-node? #f) boolean?)
  (let loop ((queue (list root)) (found-null? #f))
    (cond
      [(null? queue) #t]
      [else
       (define node (car queue))
       (define rest (cdr queue))
       (if (not node)
           (loop rest #t)
           (if found-null?
               #f
               (loop (append rest (list (tree-node-left node)
                                         (tree-node-right node)))
                     #f)))])))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec is_complete_tree(Root :: #tree_node{} | null) -> boolean().
is_complete_tree(Root) ->
    case Root of
        null -> true;
        _ -> bfs([Root], false)
    end.

bfs([], _) -> true;
bfs([Node|Rest], SeenNull) ->
    case Node of
        null ->
            bfs(Rest, true);
        #tree_node{} = N ->
            if SeenNull ->
                false;
               true ->
                NewQueue = Rest ++ [N#tree_node.left, N#tree_node.right],
                bfs(NewQueue, SeenNull)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_complete_tree(root :: TreeNode.t | nil) :: boolean
  def is_complete_tree(nil), do: true

  def is_complete_tree(root) do
    bfs([root], false)
  end

  defp bfs([], _seen_nil), do: true

  # Encounter a nil node; from now on any non‑nil means not complete.
  defp bfs([nil | rest], _seen_nil) do
    bfs(rest, true)
  end

  # Already saw a nil and now see a real node → not complete.
  defp bfs([%TreeNode{} | _rest], true), do: false

  # Normal processing when no prior nil encountered.
  defp bfs([%TreeNode{left: left, right: right} | rest], false) do
    bfs(rest ++ [left, right], false)
  end
end
```
