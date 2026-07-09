# 0998. Maximum Binary Tree II

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
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        if (val > root->val) {
            TreeNode* node = new TreeNode(val);
            node->left = root;
            return node;
        }
        root->right = insertIntoMaxTree(root->right, val);
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
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        if (val > root.val) {
            TreeNode node = new TreeNode(val);
            node.left = root;
            return node;
        }
        root.right = insertIntoMaxTree(root.right, val);
        return root;
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
    def insertIntoMaxTree(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            return TreeNode(val, left=root)
        root.right = self.insertIntoMaxTree(root.right, val)
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
    def insertIntoMaxTree(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        cur = root
        while cur.right and cur.right.val > val:
            cur = cur.right
        node = TreeNode(val)
        node.left = cur.right
        cur.right = node
        return root
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* insertIntoMaxTree(struct TreeNode* root, int val) {
    if (root == NULL) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = node->right = NULL;
        return node;
    }
    if (val > root->val) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = root;
        node->right = NULL;
        return node;
    } else {
        root->right = insertIntoMaxTree(root->right, val);
        return root;
    }
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
    public TreeNode InsertIntoMaxTree(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        if (val > root.val) {
            var newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }
        root.right = InsertIntoMaxTree(root.right, val);
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
 * @return {TreeNode}
 */
var insertIntoMaxTree = function(root, val) {
    if (!root) return new TreeNode(val);
    if (val > root.val) {
        const node = new TreeNode(val);
        node.left = root;
        return node;
    }
    root.right = insertIntoMaxTree(root.right, val);
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

function insertIntoMaxTree(root: TreeNode | null, val: number): TreeNode | null {
    if (!root) return new TreeNode(val);
    if (val > root.val) {
        const node = new TreeNode(val);
        node.left = root;
        return node;
    }
    root.right = insertIntoMaxTree(root.right, val);
    return root;
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
     * @param Integer $val
     * @return TreeNode
     */
    function insertIntoMaxTree($root, $val) {
        if ($root === null) {
            return new TreeNode($val);
        }
        if ($val > $root->val) {
            $new = new TreeNode($val);
            $new->left = $root;
            return $new;
        }
        $root->right = $this->insertIntoMaxTree($root->right, $val);
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
    func insertIntoMaxTree(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        guard let node = root else { return TreeNode(val) }
        if val > node.val {
            let newRoot = TreeNode(val)
            newRoot.left = node
            return newRoot
        } else {
            node.right = insertIntoMaxTree(node.right, val)
            return node
        }
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
    fun insertIntoMaxTree(root: TreeNode?, `val`: Int): TreeNode? {
        if (root == null) return TreeNode(`val`)
        if (`val` > root.`val`) {
            val newRoot = TreeNode(`val`)
            newRoot.left = root
            return newRoot
        }
        root.right = insertIntoMaxTree(root.right, `val`)
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
  TreeNode? insertIntoMaxTree(TreeNode? root, int val) {
    if (root == null) {
      return TreeNode(val);
    }
    if (val > root.val) {
      return TreeNode(val, root, null);
    }
    root.right = insertIntoMaxTree(root.right, val);
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
func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return &TreeNode{Val: val}
    }
    if val > root.Val {
        // New node becomes the new root with the existing tree as its left child.
        return &TreeNode{
            Val:  val,
            Left: root,
        }
    }
    // Otherwise, insert into the right subtree.
    root.Right = insertIntoMaxTree(root.Right, val)
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

def insert_into_max_tree(root, val)
  return TreeNode.new(val) if root.nil?
  if val > root.val
    new_root = TreeNode.new(val)
    new_root.left = root
    new_root
  else
    root.right = insert_into_max_tree(root.right, val)
    root
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
    def insertIntoMaxTree(root: TreeNode, `val`: Int): TreeNode = {
        if (root == null) return new TreeNode(`val`)
        if (`val` > root.value) {
            val node = new TreeNode(`val`)
            node.left = root
            node
        } else {
            root.right = insertIntoMaxTree(root.right, `val`)
            root
        }
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn insert_into_max_tree(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            None => Some(Rc::new(RefCell::new(TreeNode::new(val)))),
            Some(node_rc) => {
                if node_rc.borrow().val < val {
                    let mut new_node = TreeNode::new(val);
                    new_node.left = Some(node_rc.clone());
                    Some(Rc::new(RefCell::new(new_node)))
                } else {
                    let right_child = node_rc.borrow().right.clone();
                    let new_right = Self::insert_into_max_tree(right_child, val);
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
(define/contract (insert-into-max-tree root val)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (if (not root)
      (make-tree-node val)
      (if (> val (tree-node-val root))
          (let ([new (make-tree-node val)])
            (set-tree-node-left! new root)
            new)
          (begin
            (set-tree-node-right! root (insert-into-max-tree (tree-node-right root) val))
            root))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec insert_into_max_tree(Root :: #tree_node{} | null, Val :: integer()) -> #tree_node{} | null.
insert_into_max_tree(null, Val) ->
    #tree_node{val = Val, left = null, right = null};
insert_into_max_tree(Root = #tree_node{val = V}, Val) when Val > V ->
    #tree_node{val = Val, left = Root, right = null};
insert_into_max_tree(Node = #tree_node{right = R}, Val) ->
    NewRight = insert_into_max_tree(R, Val),
    Node#tree_node{right = NewRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec insert_into_max_tree(root :: TreeNode.t() | nil, val :: integer) :: TreeNode.t() | nil
  def insert_into_max_tree(nil, val), do: %TreeNode{val: val}

  def insert_into_max_tree(%TreeNode{val: v} = node, val) when val > v do
    %TreeNode{val: val, left: node, right: nil}
  end

  def insert_into_max_tree(%TreeNode{} = node, val) do
    new_right = insert_into_max_tree(node.right, val)
    %{node | right: new_right}
  end
end
```
