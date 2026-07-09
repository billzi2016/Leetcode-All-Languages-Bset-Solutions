# 0450. Delete Node in a BST

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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            // Node to be deleted found
            if (!root->left) {
                TreeNode* r = root->right;
                delete root;
                return r;
            }
            if (!root->right) {
                TreeNode* l = root->left;
                delete root;
                return l;
            }
            // Both children exist: find inorder successor (min in right subtree)
            TreeNode* succ = root->right;
            while (succ->left) succ = succ->left;
            root->val = succ->val;
            root->right = deleteNode(root->right, succ->val);
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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else { // found node to delete
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            // both children exist: replace with inorder successor
            TreeNode succ = getMin(root.right);
            root.val = succ.val;
            root.right = deleteNode(root.right, succ.val);
        }
        return root;
    }

    private TreeNode getMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node;
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
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Both children exist: find inorder successor (min in right subtree)
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
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
    def deleteNode(self, root: Optional['TreeNode'], key: int) -> Optional['TreeNode']:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Both children exist: find inorder successor (smallest in right subtree)
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
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

static struct TreeNode* findMin(struct TreeNode* node) {
    while (node && node->left)
        node = node->left;
    return node;
}

struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    if (!root) return NULL;

    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else { // found node to delete
        if (!root->left) {
            struct TreeNode* rightChild = root->right;
            free(root);
            return rightChild;
        } else if (!root->right) {
            struct TreeNode* leftChild = root->left;
            free(root);
            return leftChild;
        } else {
            // Node with two children: replace with inorder successor
            struct TreeNode* succ = findMin(root->right);
            root->val = succ->val;
            root->right = deleteNode(root->right, succ->val);
        }
    }
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
    public TreeNode DeleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = DeleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = DeleteNode(root.right, key);
        } else {
            // Node to delete found
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            // Both children exist: find inorder successor (min in right subtree)
            TreeNode succ = GetMin(root.right);
            root.val = succ.val;
            // Delete the successor node from right subtree
            root.right = DeleteNode(root.right, succ.val);
        }
        return root;
    }

    private TreeNode GetMin(TreeNode node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
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
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(root, key) {
    if (!root) return null;
    
    if (key < root.val) {
        root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
    } else { // found node to delete
        if (!root.left) return root.right;
        if (!root.right) return root.left;
        
        // both children exist: find inorder successor (min in right subtree)
        let succ = root.right;
        while (succ.left) succ = succ.left;
        root.val = succ.val;
        // delete the successor node from right subtree
        root.right = deleteNode(root.right, succ.val);
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

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if (!root) return null;

    if (key < root.val) {
        root.left = deleteNode(root.left, key);
        return root;
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key);
        return root;
    } else {
        // Node to be deleted found
        if (!root.left) return root.right;
        if (!root.right) return root.left;

        // Find inorder successor (minimum in right subtree)
        let succ: TreeNode = root.right;
        while (succ.left) {
            succ = succ.left;
        }
        // Replace root's value with successor's value
        root.val = succ.val;
        // Delete the successor node from right subtree
        root.right = deleteNode(root.right, succ.val);
        return root;
    }
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
     * @param Integer $key
     * @return TreeNode
     */
    function deleteNode($root, $key) {
        if ($root === null) {
            return null;
        }

        if ($key < $root->val) {
            $root->left = $this->deleteNode($root->left, $key);
        } elseif ($key > $root->val) {
            $root->right = $this->deleteNode($root->right, $key);
        } else { // found node to delete
            if ($root->left === null) {
                return $root->right;
            }
            if ($root->right === null) {
                return $root->left;
            }

            // Find the minimum node in right subtree (successor)
            $succ = $root->right;
            while ($succ->left !== null) {
                $succ = $succ->left;
            }
            // Replace current node's value with successor's value
            $root->val = $succ->val;
            // Delete the successor node from right subtree
            $root->right = $this->deleteNode($root->right, $succ->val);
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
    func deleteNode(_ root: TreeNode?, _ key: Int) -> TreeNode? {
        guard let node = root else { return nil }
        if key < node.val {
            node.left = deleteNode(node.left, key)
        } else if key > node.val {
            node.right = deleteNode(node.right, key)
        } else {
            // Node to be deleted found
            if node.left == nil {
                return node.right
            } else if node.right == nil {
                return node.left
            } else {
                // Find inorder successor (minimum in right subtree)
                var succ = node.right!
                while let leftChild = succ.left {
                    succ = leftChild
                }
                node.val = succ.val
                node.right = deleteNode(node.right, succ.val)
            }
        }
        return node
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
    fun deleteNode(root: TreeNode?, key: Int): TreeNode? {
        if (root == null) return null
        when {
            key < root.`val` -> {
                root.left = deleteNode(root.left, key)
            }
            key > root.`val` -> {
                root.right = deleteNode(root.right, key)
            }
            else -> { // found the node to delete
                if (root.left == null) return root.right
                if (root.right == null) return root.left
                // both children exist: replace with inorder successor
                val minNode = getMin(root.right!!)
                root.`val` = minNode.`val`
                root.right = deleteNode(root.right, minNode.`val`)
            }
        }
        return root
    }

    private fun getMin(node: TreeNode): TreeNode {
        var cur = node
        while (cur.left != null) {
            cur = cur.left!!
        }
        return cur
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
  TreeNode? deleteNode(TreeNode? root, int key) {
    if (root == null) return null;

    if (key < root.val) {
      root.left = deleteNode(root.left, key);
    } else if (key > root.val) {
      root.right = deleteNode(root.right, key);
    } else {
      // Node to be deleted found
      if (root.left == null) return root.right;
      if (root.right == null) return root.left;

      // Both children exist: replace with inorder successor
      TreeNode succ = _minValueNode(root.right!);
      root.val = succ.val;
      root.right = deleteNode(root.right, succ.val);
    }
    return root;
  }

  TreeNode _minValueNode(TreeNode node) {
    while (node.left != null) {
      node = node.left!;
    }
    return node;
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
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }
    if key < root.Val {
        root.Left = deleteNode(root.Left, key)
    } else if key > root.Val {
        root.Right = deleteNode(root.Right, key)
    } else {
        // Node to be deleted found
        if root.Left == nil {
            return root.Right
        }
        if root.Right == nil {
            return root.Left
        }
        // Find inorder successor (smallest in the right subtree)
        succ := root.Right
        for succ.Left != nil {
            succ = succ.Left
        }
        // Replace root's value with successor's value
        root.Val = succ.Val
        // Delete the successor node from right subtree
        root.Right = deleteNode(root.Right, succ.Val)
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

def delete_node(root, key)
  return nil if root.nil?

  if key < root.val
    root.left = delete_node(root.left, key)
  elsif key > root.val
    root.right = delete_node(root.right, key)
  else
    # Node with only one child or no child
    return root.right if root.left.nil?
    return root.left if root.right.nil?

    # Node with two children: Get the inorder successor (smallest in the right subtree)
    succ = root.right
    succ = succ.left while succ.left

    # Copy the inorder successor's value to this node and delete the successor
    root.val = succ.val
    root.right = delete_node(root.right, succ.val)
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
    def deleteNode(root: TreeNode, key: Int): TreeNode = {
        if (root == null) return null

        if (key < root.value) {
            root.left = deleteNode(root.left, key)
        } else if (key > root.value) {
            root.right = deleteNode(root.right, key)
        } else {
            // Node to be deleted found
            if (root.left == null) return root.right
            if (root.right == null) return root.left

            // Find inorder successor (minimum in right subtree)
            var succ = root.right
            while (succ.left != null) {
                succ = succ.left
            }
            // Replace root's value with successor's value
            root.value = succ.value
            // Delete the successor node from right subtree
            root.right = deleteNode(root.right, succ.value)
        }
        root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution;

impl Solution {
    fn find_min(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut cur = node.clone();
        while let Some(rc) = cur {
            if rc.borrow().left.is_none() {
                return rc.borrow().val;
            }
            cur = rc.borrow().left.clone();
        }
        unreachable!()
    }

    pub fn delete_node(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            None => None,
            Some(node_rc) => {
                let node_val = node_rc.borrow().val;
                if key < node_val {
                    let left = node_rc.borrow().left.clone();
                    let new_left = Self::delete_node(left, key);
                    node_rc.borrow_mut().left = new_left;
                    Some(node_rc)
                } else if key > node_val {
                    let right = node_rc.borrow().right.clone();
                    let new_right = Self::delete_node(right, key);
                    node_rc.borrow_mut().right = new_right;
                    Some(node_rc)
                } else {
                    // Node to delete found
                    let left_opt = node_rc.borrow().left.clone();
                    let right_opt = node_rc.borrow().right.clone();

                    if left_opt.is_none() {
                        return right_opt;
                    }
                    if right_opt.is_none() {
                        return left_opt;
                    }

                    // Both children exist: replace with inorder successor
                    let min_val = Self::find_min(&right_opt);
                    node_rc.borrow_mut().val = min_val;
                    let new_right = Self::delete_node(right_opt, min_val);
                    node_rc.borrow_mut().right = new_right;
                    Some(node_rc)
                }
            }
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

;; helper: find the minimum node in a BST subtree
(define (find-min node)
  (let loop ((n node))
    (if (tree-node-left n)
        (loop (tree-node-left n))
        n)))

;; delete a node with given key from BST
(define/contract (delete-node root key)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (cond
    [(not root) #f]
    [(< key (tree-node-val root))
     (set-tree-node-left! root (delete-node (tree-node-left root) key))
     root]
    [(> key (tree-node-val root))
     (set-tree-node-right! root (delete-node (tree-node-right root) key))
     root]
    [else
     (let ([left  (tree-node-left root)]
           [right (tree-node-right root)])
       (cond
         [(and left right)
          (let ([succ (find-min right)])
            (set-tree-node-val! root (tree-node-val succ))
            (set-tree-node-right! root (delete-node right (tree-node-val succ)))
            root)]
         [left  left]
         [right right]
         [else  #f]))]))
```

## Erlang

```erlang
-module(solution).
-export([delete_node/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec delete_node(Root :: #tree_node{} | null, Key :: integer()) -> #tree_node{} | null.
delete_node(null, _Key) ->
    null;
delete_node(Node = #tree_node{}, Key) ->
    case Node of
        #tree_node{val=V,left=L,right=R} when Key < V ->
            NewLeft = delete_node(L, Key),
            Node#tree_node{left=NewLeft};
        #tree_node{val=V,left=L,right=R} when Key > V ->
            NewRight = delete_node(R, Key),
            Node#tree_node{right=NewRight};
        #tree_node{val=_V,left=L,right=R} -> % Key == V
            case {L,R} of
                {null,null} -> null;
                {null,_} -> R;
                {_,null} -> L;
                _ ->
                    MinVal = find_min(R),
                    NewRight = delete_node(R, MinVal),
                    Node#tree_node{val=MinVal,right=NewRight}
            end
    end.

-spec find_min(Node :: #tree_node{}) -> integer().
find_min(#tree_node{val=V,left=null}) ->
    V;
find_min(#tree_node{left=L}) ->
    find_min(L).
```

## Elixir

```elixir
defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec delete_node(root :: TreeNode.t() | nil, key :: integer) :: TreeNode.t() | nil
  def delete_node(nil, _key), do: nil

  def delete_node(%TreeNode{val: v, left: l, right: r} = node, key) when key < v do
    %TreeNode{node | left: delete_node(l, key)}
  end

  def delete_node(%TreeNode{val: v, left: l, right: r} = node, key) when key > v do
    %TreeNode{node | right: delete_node(r, key)}
  end

  def delete_node(%TreeNode{left: nil, right: r}, _key), do: r
  def delete_node(%TreeNode{right: nil, left: l}, _key), do: l

  def delete_node(%TreeNode{val: _, left: l, right: r} = node, _key) do
    {succ_val, new_right} = extract_min(r)
    %TreeNode{val: succ_val, left: l, right: new_right}
  end

  defp extract_min(%TreeNode{val: v, left: nil, right: r}) do
    {v, r}
  end

  defp extract_min(%TreeNode{left: l} = node) do
    {min_val, new_left} = extract_min(l)
    {min_val, %TreeNode{node | left: new_left}}
  end
end
```
