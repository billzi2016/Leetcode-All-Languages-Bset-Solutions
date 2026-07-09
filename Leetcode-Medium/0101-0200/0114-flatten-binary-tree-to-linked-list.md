# 0114. Flatten Binary Tree to Linked List

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
    TreeNode* prev = nullptr;
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        flatten(root->right);
        flatten(root->left);
        root->right = prev;
        root->left = nullptr;
        prev = root;
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
    private TreeNode prev = null;
    
    public void flatten(TreeNode root) {
        if (root == null) return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
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
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                # Store original right subtree
                temp_right = node.right
                # Move left subtree to the right
                node.right = node.left
                node.left = None
                # Connect the original right subtree after the left tail
                left_tail.right = temp_right

            # Return the rightmost node after flattening this subtree
            return right_tail or left_tail or node

        dfs(root)
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
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None

        def dfs(node):
            nonlocal prev
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            node.left = None
            prev = node

        dfs(root)
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
void flatten(struct TreeNode* root) {
    struct TreeNode *curr = root;
    while (curr) {
        if (curr->left) {
            // Find the rightmost node of left subtree
            struct TreeNode *prev = curr->left;
            while (prev->right) {
                prev = prev->right;
            }
            // Connect the original right subtree to the rightmost node
            prev->right = curr->right;
            // Move left subtree to the right
            curr->right = curr->left;
            curr->left = NULL;
        }
        curr = curr->right;
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
public class Solution
{
    public void Flatten(TreeNode root)
    {
        FlattenTree(root);
    }

    private TreeNode FlattenTree(TreeNode node)
    {
        if (node == null) return null;

        // Recursively flatten left and right subtrees
        TreeNode leftTail = FlattenTree(node.left);
        TreeNode rightTail = FlattenTree(node.right);

        // If there is a left subtree, we splice it between the node and the right subtree
        if (leftTail != null)
        {
            leftTail.right = node.right;
            node.right = node.left;
            node.left = null;
        }

        // Return the tail of the flattened tree rooted at 'node'
        return rightTail ?? leftTail ?? node;
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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    if (!root) return;
    const stack = [root];
    let prev = null;
    while (stack.length) {
        const node = stack.pop();
        if (prev) {
            prev.right = node;
            prev.left = null;
        }
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
        prev = node;
    }
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

/**
 Do not return anything, modify root in-place instead.
 */
function flatten(root: TreeNode | null): void {
    if (!root) return;
    const stack: TreeNode[] = [];
    stack.push(root);
    while (stack.length) {
        const node = stack.pop()!;
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
        if (stack.length) {
            node.right = stack[stack.length - 1];
        } else {
            node.right = null;
        }
        node.left = null;
    }
};
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
     * @var TreeNode|null
     */
    private $prev = null;

    /**
     * @param TreeNode $root
     * @return NULL
     */
    function flatten($root) {
        $this->prev = null;
        $this->dfs($root);
    }

    /**
     * @param TreeNode|null $node
     */
    private function dfs($node) {
        if ($node === null) {
            return;
        }
        // Process right subtree first, then left subtree (reverse preorder)
        $this->dfs($node->right);
        $this->dfs($node->left);

        // Rewire current node's pointers
        $node->right = $this->prev;
        $node->left = null;

        // Update prev to current node
        $this->prev = $node;
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
    func flatten(_ root: TreeNode?) {
        var prev: TreeNode? = nil
        
        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            node.left = nil
            prev = node
        }
        
        dfs(root)
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
    fun flatten(root: TreeNode?): Unit {
        flattenTree(root)
    }

    private fun flattenTree(node: TreeNode?): TreeNode? {
        if (node == null) return null
        if (node.left == null && node.right == null) return node

        val leftTail = flattenTree(node.left)
        val rightTail = flattenTree(node.right)

        if (leftTail != null) {
            leftTail.right = node.right
            node.right = node.left
            node.left = null
        }

        return rightTail ?: leftTail
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
  TreeNode? _prev;

  void flatten(TreeNode? root) {
    _prev = null;
    _dfs(root);
  }

  void _dfs(TreeNode? node) {
    if (node == null) return;
    _dfs(node.right);
    _dfs(node.left);
    node.right = _prev;
    node.left = null;
    _prev = node;
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
func flatten(root *TreeNode) {
    var prev *TreeNode
    var dfs func(*TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        dfs(node.Right)
        dfs(node.Left)
        node.Right = prev
        node.Left = nil
        prev = node
    }
    dfs(root)
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

def flatten(root)
  @prev = nil
  dfs = lambda do |node|
    return if node.nil?
    dfs.call(node.right)
    dfs.call(node.left)
    node.right = @prev
    node.left = nil
    @prev = node
  end
  dfs.call(root)
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
    def flatten(root: TreeNode): Unit = {
        var prev: TreeNode = null
        def dfs(node: TreeNode): Unit = {
            if (node == null) return
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            node.left = null
            prev = node
        }
        dfs(root)
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

pub struct Solution;

impl Solution {
    pub fn flatten(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
            match node {
                Some(rc_node) => {
                    // Detach left and right children
                    let left_opt = rc_node.borrow_mut().left.take();
                    let right_opt = rc_node.borrow_mut().right.take();

                    // Recursively flatten subtrees
                    let left_tail = dfs(left_opt.clone());
                    let right_tail = dfs(right_opt.clone());

                    // Rewire pointers: left subtree becomes the right child
                    if let Some(l) = left_opt {
                        rc_node.borrow_mut().right = Some(l.clone());
                        if let Some(lt) = left_tail {
                            lt.borrow_mut().right = right_opt;
                        }
                    } else {
                        rc_node.borrow_mut().right = right_opt;
                    }

                    // Return the tail of the flattened subtree
                    if right_tail.is_some() {
                        right_tail
                    } else if left_tail.is_some() {
                        left_tail
                    } else {
                        Some(rc_node)
                    }
                }
                None => None,
            }
        }

        let _ = dfs(root.clone());
    }
}
```

## Racket

```racket
(define/contract (flatten root)
  (-> (or/c tree-node? #f) void?)
  (define prev (box #f))
  (letrec ((dfs (lambda (node)
                  (when node
                    (dfs (tree-node-right node))
                    (dfs (tree-node-left node))
                    (set-tree-node-right! node (unbox prev))
                    (set-tree-node-left! node #f)
                    (set-box! prev node)))))
    (dfs root)))
```
