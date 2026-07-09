# 0897. Increasing Order Search Tree

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
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode dummy(0);
        TreeNode* cur = &dummy;
        std::function<void(TreeNode*)> inorder = [&](TreeNode* node) {
            if (!node) return;
            inorder(node->left);
            cur->right = new TreeNode(node->val);
            cur = cur->right;
            inorder(node->right);
        };
        inorder(root);
        return dummy.right;
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
    private TreeNode cur;

    public TreeNode increasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode(0);
        cur = dummy;
        inorder(root);
        return dummy.right;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        // detach left child
        node.left = null;
        // attach to the right of current node
        cur.right = node;
        cur = node;
        inorder(node.right);
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
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(0)
        self.cur = dummy
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            # attach current node to the right of the last node in new tree
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
        
        inorder(root)
        return dummy.right
```

## Python3

```python
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        cur = dummy

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # detach left child
            node.left = None
            cur.right = node
            cur = node
            node = node.right

        return dummy.right
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

static void inorder(struct TreeNode* node, struct TreeNode** tail) {
    if (!node) return;
    inorder(node->left, tail);
    
    node->left = NULL;               // detach left child
    (*tail)->right = node;           // attach to the right of current tail
    *tail = node;                    // move tail forward
    
    inorder(node->right, tail);
}

struct TreeNode* increasingBST(struct TreeNode* root) {
    struct TreeNode dummy;
    dummy.left = dummy.right = NULL;
    
    struct TreeNode* tail = &dummy;
    inorder(root, &tail);
    
    return dummy.right;
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
    private TreeNode _prev;

    public TreeNode IncreasingBST(TreeNode root) {
        TreeNode dummy = new TreeNode(0);
        _prev = dummy;
        Inorder(root);
        return dummy.right;
    }

    private void Inorder(TreeNode node) {
        if (node == null) return;
        Inorder(node.left);
        // detach left child
        node.left = null;
        // link current node to the right of previous node
        _prev.right = node;
        _prev = node;
        Inorder(node.right);
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
 * @return {TreeNode}
 */
var increasingBST = function(root) {
    const dummy = new TreeNode(0);
    let prev = dummy;
    
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        // detach left child
        node.left = null;
        // attach to the right of previous node
        prev.right = node;
        prev = node;
        inorder(node.right);
    };
    
    inorder(root);
    return dummy.right;
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

function increasingBST(root: TreeNode | null): TreeNode | null {
    const dummy = new TreeNode(0);
    let cur = dummy;

    function inorder(node: TreeNode | null): void {
        if (!node) return;
        inorder(node.left);
        node.left = null;          // detach left child
        cur.right = node;          // attach to the right of current
        cur = node;                // move pointer
        inorder(node.right);
    }

    inorder(root);
    return dummy.right;
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
     * @return TreeNode
     */
    function increasingBST($root) {
        $dummy = new TreeNode(0);
        $prev = $dummy;
        $this->inorder($root, $prev);
        return $dummy->right;
    }

    private function inorder($node, &$prev) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left, $prev);
        $node->left = null;
        $prev->right = $node;
        $prev = $node;
        $this->inorder($node->right, $prev);
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
    func increasingBST(_ root: TreeNode?) -> TreeNode? {
        var dummy = TreeNode(0)
        var cur: TreeNode? = dummy
        
        func inorder(_ node: TreeNode?) {
            guard let n = node else { return }
            inorder(n.left)
            n.left = nil
            cur?.right = n
            cur = n
            inorder(n.right)
        }
        
        inorder(root)
        return dummy.right
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
    private var prev: TreeNode? = null
    private val dummy = TreeNode(0)

    fun increasingBST(root: TreeNode?): TreeNode? {
        prev = dummy
        inorder(root)
        return dummy.right
    }

    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        node.left = null
        prev?.right = node
        prev = node
        inorder(node.right)
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
  TreeNode? increasingBST(TreeNode? root) {
    final dummy = TreeNode(0);
    var prev = dummy;

    void inorder(TreeNode? node) {
      if (node == null) return;
      inorder(node.left);
      node.left = null;
      prev.right = node;
      prev = node;
      inorder(node.right);
    }

    inorder(root);
    return dummy.right;
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
func increasingBST(root *TreeNode) *TreeNode {
    dummy := &TreeNode{}
    cur := dummy

    var inorder func(node *TreeNode)
    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        inorder(node.Left)

        // detach left child and attach to the right of current node
        node.Left = nil
        cur.Right = node
        cur = node

        inorder(node.Right)
    }

    inorder(root)
    return dummy.Right
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

def increasing_bst(root)
  dummy = TreeNode.new(0)
  cur = dummy
  inorder = lambda do |node|
    return if node.nil?
    inorder.call(node.left)
    node.left = nil
    cur.right = node
    cur = node
    inorder.call(node.right)
  end
  inorder.call(root)
  dummy.right
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
    def increasingBST(root: TreeNode): TreeNode = {
        val dummy = new TreeNode(0)
        var prev = dummy

        def inorder(node: TreeNode): Unit = {
            if (node == null) return
            inorder(node.left)
            val right = node.right
            node.left = null
            prev.right = node
            prev = node
            inorder(right)
        }

        inorder(root)
        dummy.right
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

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
    pub fn increasing_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        // Collect values in inorder traversal
        fn inorder(node: Option<Rc<RefCell<TreeNode>>>, vals: &mut Vec<i32>) {
            if let Some(rc) = node {
                let left = rc.borrow().left.clone();
                inorder(left, vals);
                vals.push(rc.borrow().val);
                let right = rc.borrow().right.clone();
                inorder(right, vals);
            }
        }

        let mut values = Vec::new();
        inorder(root, &mut values);

        // Build new right-skewed tree
        let dummy = Rc::new(RefCell::new(TreeNode::new(0)));
        {
            let mut cur = dummy.clone();
            for v in values {
                let node = Rc::new(RefCell::new(TreeNode::new(v)));
                cur.borrow_mut().right = Some(node.clone());
                cur = node;
            }
        }
        dummy.borrow_mut().right.take()
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

(define/contract (increasing-bst root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (if (not root)
      #f
      (let* ((dummy (make-tree-node -1))
             (prev #f))
        (define (dfs node)
          (when node
            (dfs (tree-node-left node))
            ;; detach left child
            (set-tree-node-left! node #f)
            (if prev
                (begin
                  (set-tree-node-right! prev node)
                  (set! prev node))
                (begin
                  (set! prev node)
                  (set-tree-node-right! dummy node)))
            (dfs (tree-node-right node))))
        (dfs root)
        (tree-node-right dummy))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-export([increasing_bst/1]).

-spec increasing_bst(Root :: #tree_node{} | null) -> #tree_node{} | null.
increasing_bst(Root) ->
    Values = lists:reverse(inorder(Root, [])),
    build(Values).

inorder(null, Acc) -> Acc;
inorder(#tree_node{val=V,left=L,right=R}, Acc) ->
    Acc1 = inorder(L, Acc),
    Acc2 = [V|Acc1],
    inorder(R, Acc2).

build([]) -> null;
build([H|T]) ->
    #tree_node{val=H, left=null, right=build(T)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec increasing_bst(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def increasing_bst(root) do
    vals = inorder_vals(root)
    build(vals)
  end

  defp inorder_vals(nil), do: []
  defp inorder_vals(%TreeNode{left: l, right: r, val: v}) do
    inorder_vals(l) ++ [v] ++ inorder_vals(r)
  end

  defp build([]), do: nil
  defp build([h | t]) do
    %TreeNode{val: h, left: nil, right: build(t)}
  end
end
```
