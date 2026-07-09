# 0623. Add One Row to Tree

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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, nullptr);
        }
        std::queue<TreeNode*> q;
        q.push(root);
        int curDepth = 1;
        while (!q.empty() && curDepth < depth - 1) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ++curDepth;
        }
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            TreeNode* oldLeft = node->left;
            TreeNode* oldRight = node->right;
            node->left = new TreeNode(val);
            node->left->left = oldLeft;
            node->right = new TreeNode(val);
            node->right->right = oldRight;
        }
        return root;
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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }
        java.util.Queue<TreeNode> queue = new java.util.LinkedList<>();
        queue.offer(root);
        int currentDepth = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            if (currentDepth == depth - 1) {
                for (int i = 0; i < size; i++) {
                    TreeNode node = queue.poll();
                    TreeNode originalLeft = node.left;
                    TreeNode originalRight = node.right;
                    
                    node.left = new TreeNode(val);
                    node.left.left = originalLeft;
                    
                    node.right = new TreeNode(val);
                    node.right.right = originalRight;
                }
                break;
            } else {
                for (int i = 0; i < size; i++) {
                    TreeNode node = queue.poll();
                    if (node.left != null) queue.offer(node.left);
                    if (node.right != null) queue.offer(node.right);
                }
                currentDepth++;
            }
        }
        return root;
    }
}
```

## Python

```python
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :type depth: int
        :rtype: Optional[TreeNode]
        """
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        from collections import deque
        q = deque([root])
        cur_depth = 1
        while q and cur_depth < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            cur_depth += 1

        # now nodes in q are at depth-1
        while q:
            node = q.popleft()
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val)
            node.left.left = old_left
            node.right = TreeNode(val)
            node.right.right = old_right

        return root
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        
        q = collections.deque([root])
        current_depth = 1
        
        while q and current_depth < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            current_depth += 1
        
        # now nodes in q are at depth-1
        while q:
            node = q.popleft()
            old_left, old_right = node.left, node.right
            node.left = TreeNode(val)
            node.left.left = old_left
            node.right = TreeNode(val)
            node.right.right = old_right
        
        return root
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

struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if (depth == 1) {
        struct TreeNode* newRoot = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newRoot->val = val;
        newRoot->left = root;
        newRoot->right = NULL;
        return newRoot;
    }
    if (!root) return NULL;

    int capacity = 20005;                     // enough for given constraints
    struct TreeNode** q = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * capacity);
    int front = 0, back = 0;
    q[back++] = root;
    int curDepth = 1;

    while (curDepth < depth - 1) {
        int levelSize = back - front;
        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode* node = q[front++];
            if (node->left)  q[back++] = node->left;
            if (node->right) q[back++] = node->right;
        }
        ++curDepth;
    }

    while (front < back) {
        struct TreeNode* node = q[front++];
        struct TreeNode* oldLeft = node->left;
        struct TreeNode* oldRight = node->right;

        struct TreeNode* newLeft = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newLeft->val = val;
        newLeft->left = oldLeft;
        newLeft->right = NULL;

        struct TreeNode* newRight = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newRight->val = val;
        newRight->left = NULL;
        newRight->right = oldRight;

        node->left = newLeft;
        node->right = newRight;
    }

    free(q);
    return root;
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
    public TreeNode AddOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }

        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        int currentDepth = 1;

        while (queue.Count > 0 && currentDepth < depth - 1) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                var node = queue.Dequeue();
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            currentDepth++;
        }

        while (queue.Count > 0) {
            var node = queue.Dequeue();
            TreeNode oldLeft = node.left;
            TreeNode oldRight = node.right;
            node.left = new TreeNode(val, oldLeft, null);
            node.right = new TreeNode(val, null, oldRight);
        }

        return root;
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
 * @param {number} val
 * @param {number} depth
 * @return {TreeNode}
 */
var addOneRow = function(root, val, depth) {
    if (depth === 1) {
        const newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }
    
    let queue = [root];
    let currentDepth = 1;
    
    while (queue.length && currentDepth < depth - 1) {
        const nextLevel = [];
        for (const node of queue) {
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        queue = nextLevel;
        currentDepth++;
    }
    
    for (const node of queue) {
        const oldLeft = node.left;
        const oldRight = node.right;
        node.left = new TreeNode(val, oldLeft, null);
        node.right = new TreeNode(val, null, oldRight);
    }
    
    return root;
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

function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    if (!root) return null;
    if (depth === 1) {
        const newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }

    const dfs = (node: TreeNode | null, curDepth: number): void => {
        if (!node) return;
        if (curDepth === depth - 1) {
            const oldLeft = node.left;
            const oldRight = node.right;
            node.left = new TreeNode(val, oldLeft, null);
            node.right = new TreeNode(val, null, oldRight);
        } else {
            dfs(node.left, curDepth + 1);
            dfs(node.right, curDepth + 1);
        }
    };

    dfs(root, 1);
    return root;
}
```

## Php

```php
/ **
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
     * @param Integer $val
     * @param Integer $depth
     * @return TreeNode
     */
    function addOneRow($root, $val, $depth) {
        if ($depth == 1) {
            return new TreeNode($val, $root, null);
        }

        $queue = new SplQueue();
        $queue->enqueue([$root, 1]);

        while (!$queue->isEmpty()) {
            list($node, $d) = $queue->dequeue();

            if ($d == $depth - 1) {
                $oldLeft = $node->left;
                $oldRight = $node->right;

                $node->left = new TreeNode($val, $oldLeft, null);
                $node->right = new TreeNode($val, null, $oldRight);
            } else if ($d < $depth - 1) {
                if ($node->left !== null) {
                    $queue->enqueue([$node->left, $d + 1]);
                }
                if ($node->right !== null) {
                    $queue->enqueue([$node->right, $d + 1]);
                }
            }
        }

        return $root;
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
    func addOneRow(_ root: TreeNode?, _ val: Int, _ depth: Int) -> TreeNode? {
        guard let root = root else {
            return depth == 1 ? TreeNode(val) : nil
        }
        if depth == 1 {
            let newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        }
        var queue: [TreeNode] = [root]
        var currentDepth = 1
        while currentDepth < depth - 1 {
            var nextQueue: [TreeNode] = []
            for node in queue {
                if let left = node.left { nextQueue.append(left) }
                if let right = node.right { nextQueue.append(right) }
            }
            queue = nextQueue
            currentDepth += 1
        }
        for node in queue {
            let oldLeft = node.left
            let oldRight = node.right
            
            let leftNode = TreeNode(val)
            leftNode.left = oldLeft
            node.left = leftNode
            
            let rightNode = TreeNode(val)
            rightNode.right = oldRight
            node.right = rightNode
        }
        return root
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun addOneRow(root: TreeNode?, `val`: Int, depth: Int): TreeNode? {
        if (root == null) return null
        if (depth == 1) {
            val newRoot = TreeNode(`val`)
            newRoot.left = root
            return newRoot
        }
        val queue: java.util.ArrayDeque<TreeNode> = java.util.ArrayDeque()
        queue.add(root)
        var currentDepth = 1
        while (!queue.isEmpty()) {
            val size = queue.size
            if (currentDepth == depth - 1) {
                repeat(size) {
                    val node = queue.poll()
                    // Insert new left node
                    val oldLeft = node.left
                    node.left = TreeNode(`val`)
                    node.left?.left = oldLeft
                    // Insert new right node
                    val oldRight = node.right
                    node.right = TreeNode(`val`)
                    node.right?.right = oldRight
                }
                break
            } else {
                repeat(size) {
                    val node = queue.poll()
                    node.left?.let { queue.add(it) }
                    node.right?.let { queue.add(it) }
                }
                currentDepth++
            }
        }
        return root
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
  TreeNode? addOneRow(TreeNode? root, int val, int depth) {
    if (depth == 1) {
      return TreeNode(val, root, null);
    }
    if (root == null) {
      return null;
    }

    List<TreeNode> queue = [root];
    int currentDepth = 1;
    int index = 0;

    while (currentDepth < depth - 1) {
      int levelSize = queue.length - index;
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue[index++];
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      currentDepth++;
    }

    // Nodes from 'index' to end are at depth - 1
    for (int i = index; i < queue.length; i++) {
      TreeNode node = queue[i];
      TreeNode? oldLeft = node.left;
      TreeNode? oldRight = node.right;
      node.left = TreeNode(val, oldLeft, null);
      node.right = TreeNode(val, null, oldRight);
    }

    return root;
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
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if depth == 1 {
        return &TreeNode{Val: val, Left: root}
    }
    queue := []*TreeNode{root}
    curDepth := 1
    for curDepth < depth-1 {
        size := len(queue)
        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        curDepth++
    }
    for _, node := range queue {
        oldLeft := node.Left
        oldRight := node.Right
        node.Left = &TreeNode{Val: val, Left: oldLeft}
        node.Right = &TreeNode{Val: val, Right: oldRight}
    }
    return root
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

def add_one_row(root, val, depth)
  return TreeNode.new(val, root, nil) if depth == 1

  queue = [root]
  current_depth = 1

  while !queue.empty? && current_depth < depth - 1
    next_queue = []
    queue.each do |node|
      next_queue << node.left if node.left
      next_queue << node.right if node.right
    end
    queue = next_queue
    current_depth += 1
  end

  queue.each do |node|
    old_left = node.left
    old_right = node.right
    node.left = TreeNode.new(val, old_left, nil)
    node.right = TreeNode.new(val, nil, old_right)
  end

  root
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
    def addOneRow(root: TreeNode, `val`: Int, depth: Int): TreeNode = {
        if (depth == 1) {
            val newRoot = new TreeNode(`val`)
            newRoot.left = root
            return newRoot
        }

        def dfs(node: TreeNode, curDepth: Int): Unit = {
            if (node == null) return
            if (curDepth == depth - 1) {
                val oldLeft = node.left
                val oldRight = node.right

                val leftNode = new TreeNode(`val`)
                leftNode.left = oldLeft
                node.left = leftNode

                val rightNode = new TreeNode(`val`)
                rightNode.right = oldRight
                node.right = rightNode
            } else {
                dfs(node.left, curDepth + 1)
                dfs(node.right, curDepth + 1)
            }
        }

        dfs(root, 1)
        root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn add_one_row(root: Option<Rc<RefCell<TreeNode>>>, val: i32, depth: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if depth == 1 {
            return Some(Rc::new(RefCell::new(TreeNode {
                val,
                left: root,
                right: None,
            })));
        }

        let mut queue = std::collections::VecDeque::new();
        if let Some(r) = root.clone() {
            queue.push_back(r);
        }
        let mut current_depth = 1;

        while !queue.is_empty() {
            if current_depth == depth - 1 {
                for node_rc in queue.iter() {
                    let mut node = node_rc.borrow_mut();
                    let old_left = node.left.take();
                    let old_right = node.right.take();

                    let new_left = Rc::new(RefCell::new(TreeNode {
                        val,
                        left: old_left,
                        right: None,
                    }));
                    let new_right = Rc::new(RefCell::new(TreeNode {
                        val,
                        left: None,
                        right: old_right,
                    }));

                    node.left = Some(new_left);
                    node.right = Some(new_right);
                }
                break;
            } else {
                let level_size = queue.len();
                for _ in 0..level_size {
                    if let Some(node_rc) = queue.pop_front() {
                        let node_ref = node_rc.borrow();
                        if let Some(l) = node_ref.left.clone() {
                            queue.push_back(l);
                        }
                        if let Some(r) = node_ref.right.clone() {
                            queue.push_back(r);
                        }
                    }
                }
                current_depth += 1;
            }
        }

        root
    }
}
```

## Racket

```racket
(define/contract (add-one-row root val depth)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? (or/c tree-node? #f))
  (cond
    [(= depth 1)
     (let ((new-root (make-tree-node val)))
       (set-tree-node-left! new-root root)
       new-root)]
    [else
     (let recur ((node root) (cur 1))
       (when node
         (if (= (+ cur 1) depth)
             (let* ((left-old (tree-node-left node))
                    (right-old (tree-node-right node))
                    (left-new (make-tree-node val))
                    (right-new (make-tree-node val)))
               (set-tree-node-left! left-new left-old)
               (set-tree-node-right! right-new right-old)
               (set-tree-node-left! node left-new)
               (set-tree-node-right! node right-new))
             (begin
               (recur (tree-node-left node) (+ cur 1))
               (recur (tree-node-right node) (+ cur 1))))))
     root)))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec add_one_row(Root :: #tree_node{} | null, Val :: integer(), Depth :: integer()) -> #tree_node{} | null.
add_one_row(null, _, _) ->
    null;
add_one_row(Root, Val, 1) ->
    #tree_node{val = Val, left = Root, right = null};
add_one_row(Root, Val, Depth) when Depth > 1 ->
    add_one_row_helper(Root, Val, Depth).

-spec add_one_row_helper(Node :: #tree_node{} | null, integer(), integer()) -> #tree_node{} | null.
add_one_row_helper(null, _, _) ->
    null;
add_one_row_helper(Node, Val, 2) ->
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    NewLeft = #tree_node{val = Val, left = Left, right = null},
    NewRight = #tree_node{val = Val, left = null, right = Right},
    Node#tree_node{left = NewLeft, right = NewRight};
add_one_row_helper(Node, Val, Depth) ->
    UpdatedLeft = add_one_row_helper(Node#tree_node.left, Val, Depth - 1),
    UpdatedRight = add_one_row_helper(Node#tree_node.right, Val, Depth - 1),
    Node#tree_node{left = UpdatedLeft, right = UpdatedRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_one_row(root :: TreeNode.t | nil, val :: integer, depth :: integer) :: TreeNode.t | nil
  def add_one_row(root, val, depth) do
    cond do
      depth == 1 ->
        %TreeNode{val: val, left: root, right: nil}

      true ->
        insert(root, val, depth, 1)
    end
  end

  defp insert(nil, _val, _target_depth, _cur), do: nil

  defp insert(node, val, target_depth, cur) when cur == target_depth - 1 do
    new_left = %TreeNode{val: val, left: node.left, right: nil}
    new_right = %TreeNode{val: val, left: nil, right: node.right}
    %{node | left: new_left, right: new_right}
  end

  defp insert(node, val, target_depth, cur) do
    updated_left = insert(node.left, val, target_depth, cur + 1)
    updated_right = insert(node.right, val, target_depth, cur + 1)
    %{node | left: updated_left, right: updated_right}
  end
end
```
