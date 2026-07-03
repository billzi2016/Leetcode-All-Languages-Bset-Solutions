# 0101. Symmetric Tree

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
    bool isSymmetric(TreeNode* root) {
        return isMirror(root, root);
    }
private:
    bool isMirror(TreeNode* a, TreeNode* b) {
        if (!a && !b) return true;
        if (!a || !b) return false;
        return (a->val == b->val)
            && isMirror(a->left, b->right)
            && isMirror(a->right, b->left);
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
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    private boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null || t2 == null) return false;
        if (t1.val != t2.val) return false;
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);
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
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)
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
    def isSymmetric(self, root):
        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right)
```

## C

```c
#include <stdbool.h>

static bool isMirror(struct TreeNode* a, struct TreeNode* b) {
    if (!a && !b) return true;
    if (!a || !b) return false;
    if (a->val != b->val) return false;
    return isMirror(a->left, b->right) && isMirror(a->right, b->left);
}

bool isSymmetric(struct TreeNode* root) {
    if (!root) return true;
    return isMirror(root->left, root->right);
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
    public bool IsSymmetric(TreeNode root) {
        if (root == null) return true;
        return IsMirror(root.left, root.right);
    }

    private bool IsMirror(TreeNode left, TreeNode right) {
        if (left == null && right == null) return true;
        if (left == null || right == null) return false;
        if (left.val != right.val) return false;
        return IsMirror(left.left, right.right) && IsMirror(left.right, right.left);
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
var isSymmetric = function(root) {
    if (!root) return true;
    
    const isMirror = (t1, t2) => {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        if (t1.val !== t2.val) return false;
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left);
    };
    
    return isMirror(root.left, root.right);
};
```

## Typescript

```typescript
function isSymmetric(root: TreeNode | null): boolean {
    if (!root) return true;
    const isMirror = (a: TreeNode | null, b: TreeNode | null): boolean => {
        if (!a && !b) return true;
        if (!a || !b) return false;
        if (a.val !== b.val) return false;
        return isMirror(a.left, b.right) && isMirror(a.right, b.left);
    };
    return isMirror(root.left, root.right);
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
     * @return bool
     */
    function isSymmetric($root) {
        if ($root === null) {
            return true;
        }
        return $this->isMirror($root->left, $root->right);
    }

    /**
     * @param TreeNode|null $t1
     * @param TreeNode|null $t2
     * @return bool
     */
    private function isMirror($t1, $t2) {
        if ($t1 === null && $t2 === null) {
            return true;
        }
        if ($t1 === null || $t2 === null) {
            return false;
        }
        if ($t1->val !== $t2->val) {
            return false;
        }
        return $this->isMirror($t1->left, $t2->right) && $this->isMirror($t1->right, $t2->left);
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
    func isSymmetric(_ root: TreeNode?) -> Bool {
        return isMirror(root, root)
    }

    private func isMirror(_ t1: TreeNode?, _ t2: TreeNode?) -> Bool {
        if t1 == nil && t2 == nil { return true }
        if t1 == nil || t2 == nil { return false }
        if t1!.val != t2!.val { return false }
        return isMirror(t1!.left, t2!.right) && isMirror(t1!.right, t2!.left)
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
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) return true
        return isMirror(root.left, root.right)
    }

    private fun isMirror(t1: TreeNode?, t2: TreeNode?): Boolean {
        if (t1 == null && t2 == null) return true
        if (t1 == null || t2 == null) return false
        if (t1.`val` != t2.`val`) return false
        return isMirror(t1.left, t2.right) && isMirror(t1.right, t2.left)
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
  bool isSymmetric(TreeNode? root) {
    return _isMirror(root, root);
  }

  bool _isMirror(TreeNode? t1, TreeNode? t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    if (t1.val != t2.val) return false;
    return _isMirror(t1.left, t2.right) && _isMirror(t1.right, t2.left);
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
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	var isMirror func(a, b *TreeNode) bool
	isMirror = func(a, b *TreeNode) bool {
		if a == nil && b == nil {
			return true
		}
		if a == nil || b == nil {
			return false
		}
		if a.Val != b.Val {
			return false
		}
		return isMirror(a.Left, b.Right) && isMirror(a.Right, b.Left)
	}
	return isMirror(root.Left, root.Right)
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

def is_symmetric(root)
  return true if root.nil?
  queue = [[root.left, root.right]]
  until queue.empty?
    left, right = queue.shift
    if left.nil? && right.nil?
      next
    elsif left.nil? || right.nil?
      return false
    elsif left.val != right.val
      return false
    else
      queue << [left.left, right.right]
      queue << [left.right, right.left]
    end
  end
  true
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
    def isSymmetric(root: TreeNode): Boolean = {
        if (root == null) true
        else isMirror(root.left, root.right)
    }

    private def isMirror(left: TreeNode, right: TreeNode): Boolean = {
        if (left == null && right == null) true
        else if (left == null || right == null) false
        else left.value == right.value &&
             isMirror(left.left, right.right) &&
             isMirror(left.right, right.left)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::is_mirror(root.clone(), root)
    }

    fn is_mirror(
        left: Option<Rc<RefCell<TreeNode>>>,
        right: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (left, right) {
            (None, None) => true,
            (Some(l), Some(r)) => {
                let l_ref = l.borrow();
                let r_ref = r.borrow();
                l_ref.val == r_ref.val
                    && Self::is_mirror(l_ref.left.clone(), r_ref.right.clone())
                    && Self::is_mirror(l_ref.right.clone(), r_ref.left.clone())
            }
            _ => false,
        }
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

(define/contract (is-symmetric root)
  (-> (or/c tree-node? #f) boolean?)
  (if (not root)
      #t
      (letrec ((mirror?
                (lambda (t1 t2)
                  (cond
                    [(and (not t1) (not t2)) #t]
                    [(or (not t1) (not t2))   #f]
                    [else
                     (and (= (tree-node-val t1) (tree-node-val t2))
                          (mirror? (tree-node-left t1)  (tree-node-right t2))
                          (mirror? (tree-node-right t1) (tree-node-left t2)))]))))
        (mirror? (tree-node-left root) (tree-node-right root)))))
```

## Erlang

```erlang
-spec is_symmetric(Root :: #tree_node{} | null) -> boolean().
is_symmetric(Root) ->
    case Root of
        null -> true;
        #tree_node{} = Node -> is_mirror(Node#tree_node.left, Node#tree_node.right)
    end.

%% helper function to compare two subtrees for mirror symmetry
-spec is_mirror(A :: #tree_node{} | null, B :: #tree_node{} | null) -> boolean().
is_mirror(null, null) ->
    true;
is_mirror(#tree_node{val = V1, left = L1, right = R1},
          #tree_node{val = V2, left = L2, right = R2}) when V1 =:= V2 ->
    is_mirror(L1, R2) andalso is_mirror(R1, L2);
is_mirror(_, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_symmetric(root :: TreeNode.t | nil) :: boolean
  def is_symmetric(nil), do: true

  def is_symmetric(%TreeNode{left: left, right: right}) do
    mirror?(left, right)
  end

  defp mirror?(nil, nil), do: true

  defp mirror?(
         %TreeNode{val: v1, left: l1, right: r1},
         %TreeNode{val: v2, left: l2, right: r2}
       )
       when v1 == v2 do
    mirror?(l1, r2) and mirror?(r1, l2)
  end

  defp mirror?(_, _), do: false
end
```
