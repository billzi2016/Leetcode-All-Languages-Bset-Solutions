# 0701. Insert into a Binary Search Tree

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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);
        TreeNode* cur = root;
        while (true) {
            if (val < cur->val) {
                if (cur->left) {
                    cur = cur->left;
                } else {
                    cur->left = new TreeNode(val);
                    break;
                }
            } else { // val > cur->val, guaranteed not equal
                if (cur->right) {
                    cur = cur->right;
                } else {
                    cur->right = new TreeNode(val);
                    break;
                }
            }
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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        TreeNode cur = root;
        while (true) {
            if (val < cur.val) {
                if (cur.left == null) {
                    cur.left = new TreeNode(val);
                    break;
                } else {
                    cur = cur.left;
                }
            } else { // val > cur.val, guaranteed not equal
                if (cur.right == null) {
                    cur.right = new TreeNode(val);
                    break;
                } else {
                    cur = cur.right;
                }
            }
        }
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
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:  # val > node.val (guaranteed distinct)
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
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
    def insertIntoBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
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
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    if (root == NULL) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = node->right = NULL;
        return node;
    }
    
    struct TreeNode* cur = root;
    while (1) {
        if (val < cur->val) {
            if (cur->left) {
                cur = cur->left;
            } else {
                cur->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                cur->left->val = val;
                cur->left->left = cur->left->right = NULL;
                break;
            }
        } else { // val > cur->val, guaranteed not equal
            if (cur->right) {
                cur = cur->right;
            } else {
                cur->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                cur->right->val = val;
                cur->right->left = cur->right->right = NULL;
                break;
            }
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
    public TreeNode InsertIntoBST(TreeNode root, int val) {
        if (root == null) {
            return new TreeNode(val);
        }
        if (val < root.val) {
            root.left = InsertIntoBST(root.left, val);
        } else {
            root.right = InsertIntoBST(root.right, val);
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
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    if (!root) return new TreeNode(val);
    let node = root;
    while (true) {
        if (val < node.val) {
            if (node.left) {
                node = node.left;
            } else {
                node.left = new TreeNode(val);
                break;
            }
        } else { // val > node.val
            if (node.right) {
                node = node.right;
            } else {
                node.right = new TreeNode(val);
                break;
            }
        }
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

function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    if (root === null) {
        return new TreeNode(val);
    }
    if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    } else {
        root.right = insertIntoBST(root.right, val);
    }
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
    function insertIntoBST($root, $val) {
        if ($root === null) {
            return new TreeNode($val);
        }
        $node = $root;
        while (true) {
            if ($val < $node->val) {
                if ($node->left === null) {
                    $node->left = new TreeNode($val);
                    break;
                } else {
                    $node = $node->left;
                }
            } else { // $val > $node->val
                if ($node->right === null) {
                    $node->right = new TreeNode($val);
                    break;
                } else {
                    $node = $node->right;
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
    func insertIntoBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        guard let root = root else { return TreeNode(val) }
        var node = root
        while true {
            if val < node.val {
                if let left = node.left {
                    node = left
                } else {
                    node.left = TreeNode(val)
                    break
                }
            } else {
                if let right = node.right {
                    node = right
                } else {
                    node.right = TreeNode(val)
                    break
                }
            }
        }
        return root
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
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {
        if (root == null) return TreeNode(`val`)
        var node = root
        while (true) {
            if (`val` < node.`val`) {
                if (node.left == null) {
                    node.left = TreeNode(`val`)
                    break
                } else {
                    node = node.left!!
                }
            } else {
                if (node.right == null) {
                    node.right = TreeNode(`val`)
                    break
                } else {
                    node = node.right!!
                }
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
  TreeNode? insertIntoBST(TreeNode? root, int val) {
    if (root == null) {
      return TreeNode(val);
    }
    if (val < root.val) {
      root.left = insertIntoBST(root.left, val);
    } else {
      root.right = insertIntoBST(root.right, val);
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
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return &TreeNode{Val: val}
    }
    cur := root
    for {
        if val < cur.Val {
            if cur.Left == nil {
                cur.Left = &TreeNode{Val: val}
                break
            }
            cur = cur.Left
        } else {
            if cur.Right == nil {
                cur.Right = &TreeNode{Val: val}
                break
            }
            cur = cur.Right
        }
    }
    return root
}
```

## Ruby

```ruby
def insert_into_bst(root, val)
  return TreeNode.new(val) if root.nil?
  node = root
  loop do
    if val < node.val
      if node.left.nil?
        node.left = TreeNode.new(val)
        break
      else
        node = node.left
      end
    else
      if node.right.nil?
        node.right = TreeNode.new(val)
        break
      else
        node = node.right
      end
    end
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
    def insertIntoBST(root: TreeNode, `val`: Int): TreeNode = {
        if (root == null) return new TreeNode(`val`)
        if (`val` < root.value) {
            root.left = insertIntoBST(root.left, `val`)
        } else {
            root.right = insertIntoBST(root.right, `val`)
        }
        root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn insert_into_bst(root: Option<Rc<RefCell<TreeNode>>>, val: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() {
            return Some(Rc::new(RefCell::new(TreeNode::new(val))));
        }
        let mut cur = root.clone().unwrap();
        loop {
            let mut node = cur.borrow_mut();
            if val < node.val {
                if let Some(left) = &node.left {
                    let next = Rc::clone(left);
                    drop(node);
                    cur = next;
                } else {
                    node.left = Some(Rc::new(RefCell::new(TreeNode::new(val))));
                    break;
                }
            } else {
                if let Some(right) = &node.right {
                    let next = Rc::clone(right);
                    drop(node);
                    cur = next;
                } else {
                    node.right = Some(Rc::new(RefCell::new(TreeNode::new(val))));
                    break;
                }
            }
        }
        root
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

(define/contract (insert-into-bst root val)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (if (not root)
      (make-tree-node val)
      (let loop ((node root))
        (cond
          [(< val (tree-node-val node))
           (if (tree-node-left node)
               (loop (tree-node-left node))
               (begin
                 (set-tree-node-left! node (make-tree-node val))
                 root))]
          [(> val (tree-node-val node))
           (if (tree-node-right node)
               (loop (tree-node-right node))
               (begin
                 (set-tree-node-right! node (make-tree-node val))
                 root))]
          [else ; equal case shouldn't happen per problem guarantee
           root]))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                      left = null :: 'null' | #tree_node{},
                      right = null :: 'null' | #tree_node{}}).

-spec insert_into_bst(Root :: #tree_node{} | null, Val :: integer()) -> #tree_node{} | null.
insert_into_bst(null, Val) ->
    #tree_node{val = Val};
insert_into_bst(Root, Val) ->
    case Val < Root#tree_node.val of
        true ->
            NewLeft = insert_into_bst(Root#tree_node.left, Val),
            Root#tree_node{left = NewLeft};
        false ->
            NewRight = insert_into_bst(Root#tree_node.right, Val),
            Root#tree_node{right = NewRight}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec insert_into_bst(root :: TreeNode.t() | nil, val :: integer) :: TreeNode.t() | nil
  def insert_into_bst(nil, val), do: %TreeNode{val: val}

  def insert_into_bst(%TreeNode{val: v} = node, val) when val < v do
    %{node | left: insert_into_bst(node.left, val)}
  end

  def insert_into_bst(%TreeNode{} = node, val) do
    %{node | right: insert_into_bst(node.right, val)}
  end
end
```
