# 1325. Delete Leaves With a Given Value

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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if (!root) return nullptr;
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);
        if (!root->left && !root->right && root->val == target) {
            delete root;
            return nullptr;
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
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root == null) return null;
        root.left = removeLeafNodes(root.left, target);
        root.right = removeLeafNodes(root.right, target);
        if (root.val == target && root.left == null && root.right == null) {
            return null;
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
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # Recursively process left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If current node is a leaf and its value equals target, delete it
        if not root.left and not root.right and root.val == target:
            return None

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
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Recursively process left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If current node is a leaf with the target value, delete it
        if not root.left and not root.right and root.val == target:
            return None

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
struct TreeNode* removeLeafNodes(struct TreeNode* root, int target) {
    if (root == NULL) return NULL;
    
    root->left = removeLeafNodes(root->left, target);
    root->right = removeLeafNodes(root->right, target);
    
    if (root->left == NULL && root->right == NULL && root->val == target) {
        return NULL;
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
    public TreeNode RemoveLeafNodes(TreeNode root, int target) {
        if (root == null) return null;

        root.left = RemoveLeafNodes(root.left, target);
        root.right = RemoveLeafNodes(root.right, target);

        if (root.val == target && root.left == null && root.right == null)
            return null;
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
 * @param {number} target
 * @return {TreeNode}
 */
var removeLeafNodes = function(root, target) {
    if (!root) return null;
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (!root.left && !root.right && root.val === target) {
        return null;
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

function removeLeafNodes(root: TreeNode | null, target: number): TreeNode | null {
    if (!root) return null;
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (!root.left && !root.right && root.val === target) {
        return null;
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
     * @param Integer $target
     * @return TreeNode
     */
    function removeLeafNodes($root, $target) {
        if ($root === null) {
            return null;
        }
        $root->left = $this->removeLeafNodes($root->left, $target);
        $root->right = $this->removeLeafNodes($root->right, $target);
        if ($root->left === null && $root->right === null && $root->val == $target) {
            return null;
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
    func removeLeafNodes(_ root: TreeNode?, _ target: Int) -> TreeNode? {
        guard let node = root else { return nil }
        node.left = removeLeafNodes(node.left, target)
        node.right = removeLeafNodes(node.right, target)
        if node.left == nil && node.right == nil && node.val == target {
            return nil
        }
        return node
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
    fun removeLeafNodes(root: TreeNode?, target: Int): TreeNode? {
        if (root == null) return null
        root.left = removeLeafNodes(root.left, target)
        root.right = removeLeafNodes(root.right, target)
        return if (root.left == null && root.right == null && root.`val` == target) {
            null
        } else {
            root
        }
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
  TreeNode? removeLeafNodes(TreeNode? root, int target) {
    if (root == null) return null;
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (root.left == null && root.right == null && root.val == target) {
      return null;
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
func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    if root == nil {
        return nil
    }
    root.Left = removeLeafNodes(root.Left, target)
    root.Right = removeLeafNodes(root.Right, target)
    if root.Left == nil && root.Right == nil && root.Val == target {
        return nil
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

def remove_leaf_nodes(root, target)
  return nil if root.nil?
  root.left = remove_leaf_nodes(root.left, target)
  root.right = remove_leaf_nodes(root.right, target)
  if root.left.nil? && root.right.nil? && root.val == target
    nil
  else
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
    def removeLeafNodes(root: TreeNode, target: Int): TreeNode = {
        if (root == null) return null

        root.left = removeLeafNodes(root.left, target)
        root.right = removeLeafNodes(root.right, target)

        if (root.left == null && root.right == null && root.value == target) null
        else root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn remove_leaf_nodes(root: Option<Rc<RefCell<TreeNode>>>, target: i32) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, target: i32) -> Option<Rc<RefCell<TreeNode>>> {
            match node {
                None => None,
                Some(rc_node) => {
                    // Process left subtree
                    let left_processed = {
                        let left = rc_node.borrow().left.clone();
                        dfs(left, target)
                    };
                    // Process right subtree
                    let right_processed = {
                        let right = rc_node.borrow().right.clone();
                        dfs(right, target)
                    };
                    // Update children after processing
                    {
                        let mut node_mut = rc_node.borrow_mut();
                        node_mut.left = left_processed;
                        node_mut.right = right_processed;
                    }
                    // Determine if current node became a leaf with the target value
                    let is_leaf = {
                        let n = rc_node.borrow();
                        n.left.is_none() && n.right.is_none()
                    };
                    if is_leaf && rc_node.borrow().val == target {
                        None
                    } else {
                        Some(rc_node)
                    }
                }
            }
        }

        dfs(root, target)
    }
}
```

## Racket

```racket
(define/contract (remove-leaf-nodes root target)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (if (not root)
      #f
      (begin
        (set-tree-node-left! root (remove-leaf-nodes (tree-node-left root) target))
        (set-tree-node-right! root (remove-leaf-nodes (tree-node-right root) target))
        (if (and (eq? (tree-node-left root) #f)
                 (eq? (tree-node-right root) #f)
                 (= (tree-node-val root) target))
            #f
            root))))
```

## Erlang

```erlang
-module(solution).
-export([remove_leaf_nodes/2]).

-spec remove_leaf_nodes(Root :: #tree_node{} | null, Target :: integer()) -> #tree_node{} | null.
remove_leaf_nodes(null, _Target) ->
    null;
remove_leaf_nodes(Root, Target) ->
    Left  = remove_leaf_nodes(Root#tree_node.left, Target),
    Right = remove_leaf_nodes(Root#tree_node.right, Target),
    UpdatedRoot = Root#tree_node{left = Left, right = Right},
    case {UpdatedRoot#tree_node.left, UpdatedRoot#tree_node.right, UpdatedRoot#tree_node.val} of
        {null, null, Target} -> null;
        _ -> UpdatedRoot
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_leaf_nodes(root :: TreeNode.t | nil, target :: integer) :: TreeNode.t | nil
  def remove_leaf_nodes(nil, _target), do: nil

  def remove_leaf_nodes(%TreeNode{} = node, target) do
    left = remove_leaf_nodes(node.left, target)
    right = remove_leaf_nodes(node.right, target)

    if left == nil and right == nil and node.val == target do
      nil
    else
      %TreeNode{node | left: left, right: right}
    end
  end
end
```
