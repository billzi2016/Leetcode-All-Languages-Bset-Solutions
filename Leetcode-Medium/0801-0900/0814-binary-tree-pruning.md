# 0814. Binary Tree Pruning

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
    TreeNode* pruneTree(TreeNode* root) {
        if (!containsOne(root)) return nullptr;
        return root;
    }
private:
    // Returns true if the subtree rooted at node contains a 1.
    bool containsOne(TreeNode* node) {
        if (!node) return false;
        bool leftHas = containsOne(node->left);
        bool rightHas = containsOne(node->right);
        if (!leftHas) node->left = nullptr;
        if (!rightHas) node->right = nullptr;
        return node->val == 1 || leftHas || rightHas;
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
    public TreeNode pruneTree(TreeNode root) {
        return containsOne(root) ? root : null;
    }

    private boolean containsOne(TreeNode node) {
        if (node == null) {
            return false;
        }
        boolean leftHasOne = containsOne(node.left);
        boolean rightHasOne = containsOne(node.right);

        if (!leftHasOne) {
            node.left = null;
        }
        if (!rightHasOne) {
            node.right = null;
        }

        return node.val == 1 || leftHasOne || rightHasOne;
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
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            # If current node is 0 and both children are pruned, prune this node.
            if node.val == 0 and not node.left and not node.right:
                return None
            return node

        return dfs(root)
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
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
static int containsOne(struct TreeNode* node) {
    if (!node) return 0;
    int leftHas = containsOne(node->left);
    int rightHas = containsOne(node->right);
    if (!leftHas) node->left = NULL;
    if (!rightHas) node->right = NULL;
    return node->val == 1 || leftHas || rightHas;
}

struct TreeNode* pruneTree(struct TreeNode* root) {
    if (!root) return NULL;
    return containsOne(root) ? root : NULL;
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
    public TreeNode PruneTree(TreeNode root) {
        if (root == null) return null;
        bool keep = ContainsOne(root);
        return keep ? root : null;
    }

    private bool ContainsOne(TreeNode node) {
        if (node == null) return false;

        bool leftHasOne = ContainsOne(node.left);
        bool rightHasOne = ContainsOne(node.right);

        if (!leftHasOne) node.left = null;
        if (!rightHasOne) node.right = null;

        return node.val == 1 || leftHasOne || rightHasOne;
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
var pruneTree = function(root) {
    const dfs = (node) => {
        if (!node) return null;
        node.left = dfs(node.left);
        node.right = dfs(node.right);
        if (node.val === 0 && !node.left && !node.right) {
            return null;
        }
        return node;
    };
    return dfs(root);
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

function pruneTree(root: TreeNode | null): TreeNode | null {
    const dfs = (node: TreeNode | null): boolean => {
        if (!node) return false;
        const leftHasOne = dfs(node.left);
        const rightHasOne = dfs(node.right);
        if (!leftHasOne) node.left = null;
        if (!rightHasOne) node.right = null;
        return node.val === 1 || leftHasOne || rightHasOne;
    };
    return dfs(root) ? root : null;
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
     * @param TreeNode|null $root
     * @return TreeNode|null
     */
    function pruneTree($root) {
        if ($root === null) {
            return null;
        }

        $root->left = $this->pruneTree($root->left);
        $root->right = $this->pruneTree($root->right);

        if ($root->val == 0 && $root->left === null && $root->right === null) {
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
    func pruneTree(_ root: TreeNode?) -> TreeNode? {
        func containsOne(_ node: TreeNode?) -> Bool {
            guard let node = node else { return false }
            let leftHas = containsOne(node.left)
            if !leftHas { node.left = nil }
            let rightHas = containsOne(node.right)
            if !rightHas { node.right = nil }
            return node.val == 1 || leftHas || rightHas
        }
        return containsOne(root) ? root : nil
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
    fun pruneTree(root: TreeNode?): TreeNode? {
        if (root == null) return null
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
        return if (root.`val` == 0 && root.left == null && root.right == null) null else root
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
  TreeNode? pruneTree(TreeNode? root) {
    return _prune(root);
  }

  TreeNode? _prune(TreeNode? node) {
    if (node == null) return null;
    node.left = _prune(node.left);
    node.right = _prune(node.right);
    if (node.val == 0 && node.left == null && node.right == null) {
      return null;
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
func pruneTree(root *TreeNode) *TreeNode {
    var dfs func(*TreeNode) bool
    dfs = func(node *TreeNode) bool {
        if node == nil {
            return false
        }
        leftHasOne := dfs(node.Left)
        rightHasOne := dfs(node.Right)

        if !leftHasOne {
            node.Left = nil
        }
        if !rightHasOne {
            node.Right = nil
        }

        return node.Val == 1 || leftHasOne || rightHasOne
    }

    if dfs(root) {
        return root
    }
    return nil
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

def prune_tree(root)
  return nil if root.nil?
  root.left = prune_tree(root.left)
  root.right = prune_tree(root.right)
  return nil if root.val == 0 && root.left.nil? && root.right.nil?
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
    def pruneTree(root: TreeNode): TreeNode = {
        def dfs(node: TreeNode): TreeNode = {
            if (node == null) return null
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if (node.value == 0 && node.left == null && node.right == null) null else node
        }
        dfs(root)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn prune_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: &mut Option<Rc<RefCell<TreeNode>>>) -> bool {
            if let Some(rc) = node {
                // Recurse on children
                let left_has_one;
                let right_has_one;
                {
                    let mut n = rc.borrow_mut();
                    left_has_one = dfs(&mut n.left);
                    right_has_one = dfs(&mut n.right);
                    if !left_has_one { n.left = None; }
                    if !right_has_one { n.right = None; }
                }
                // Determine if this subtree contains a 1
                let has_one = rc.borrow().val == 1 || left_has_one || right_has_one;
                if !has_one {
                    *node = None;
                }
                has_one
            } else {
                false
            }
        }

        let mut root_opt = root;
        dfs(&mut root_opt);
        root_opt
    }
}
```

## Racket

```racket
(define/contract (prune-tree root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (letrec ((dfs
            (lambda (node)
              (if (not node)
                  #f
                  (let* ((new-left (dfs (tree-node-left node)))
                         (new-right (dfs (tree-node-right node))))
                    (set-tree-node-left! node new-left)
                    (set-tree-node-right! node new-right)
                    (if (or (= (tree-node-val node) 1) new-left new-right)
                        node
                        #f))))))
    (dfs root)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec prune_tree(Root :: #tree_node{} | null) -> #tree_node{} | null.
prune_tree(null) ->
    null;
prune_tree(Node) when is_record(Node, tree_node) ->
    PrunedLeft  = prune_tree(Node#tree_node.left),
    PrunedRight = prune_tree(Node#tree_node.right),
    case {Node#tree_node.val, PrunedLeft, PrunedRight} of
        {0, null, null} -> 
            null;
        _ ->
            Node#tree_node{left = PrunedLeft, right = PrunedRight}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec prune_tree(root :: TreeNode.t() | nil) :: TreeNode.t() | nil
  def prune_tree(nil), do: nil

  def prune_tree(%TreeNode{val: v, left: l, right: r} = node) do
    left_pruned = prune_tree(l)
    right_pruned = prune_tree(r)

    if v == 0 and left_pruned == nil and right_pruned == nil do
      nil
    else
      %TreeNode{node | left: left_pruned, right: right_pruned}
    end
  end
end
```
