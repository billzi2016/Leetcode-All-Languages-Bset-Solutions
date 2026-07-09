# 0098. Validate Binary Search Tree

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
    bool isValidBST(TreeNode* root) {
        return validate(root, LLONG_MIN, LLONG_MAX);
    }
private:
    bool validate(TreeNode* node, long long low, long long high) {
        if (!node) return true;
        if (node->val <= low || node->val >= high) return false;
        return validate(node->left, low, node->val) && 
               validate(node->right, node->val, high);
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
    public boolean isValidBST(TreeNode root) {
        return validate(root, null, null);
    }

    private boolean validate(TreeNode node, Long lower, Long upper) {
        if (node == null) {
            return true;
        }
        long val = node.val;
        if ((lower != null && val <= lower) || (upper != null && val >= upper)) {
            return false;
        }
        return validate(node.left, lower, val) && validate(node.right, val, upper);
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
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, low, high):
            if not node:
                return True
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        return helper(root, None, None)
```

## Python3

```python
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            return dfs(node.left, low, val) and dfs(node.right, val, high)
        return dfs(root, float('-inf'), float('inf'))
```

## C

```c
#include <stdbool.h>
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
static bool validate(struct TreeNode* node, long long low, long long high) {
    if (!node) return true;
    if (node->val <= low || node->val >= high) return false;
    return validate(node->left, low, node->val) && 
           validate(node->right, node->val, high);
}

bool isValidBST(struct TreeNode* root) {
    return validate(root, LLONG_MIN, LLONG_MAX);
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
    public bool IsValidBST(TreeNode root) {
        return Validate(root, long.MinValue, long.MaxValue);
    }

    private bool Validate(TreeNode node, long low, long high) {
        if (node == null) return true;
        if (node.val <= low || node.val >= high) return false;
        return Validate(node.left, low, node.val) && Validate(node.right, node.val, high);
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
var isValidBST = function(root) {
    const validate = (node, lower, upper) => {
        if (!node) return true;
        const val = node.val;
        if (val <= lower || val >= upper) return false;
        return validate(node.left, lower, val) && validate(node.right, val, upper);
    };
    return validate(root, -Infinity, Infinity);
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

function isValidBST(root: TreeNode | null): boolean {
    const validate = (node: TreeNode | null, low: number, high: number): boolean => {
        if (!node) return true;
        if (node.val <= low || node.val >= high) return false;
        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    };
    return validate(root, -Infinity, Infinity);
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
    function isValidBST($root) {
        return $this->validate($root, null, null);
    }

    private function validate($node, $low, $high) {
        if ($node === null) {
            return true;
        }
        if (($low !== null && $node->val <= $low) || ($high !== null && $node->val >= $high)) {
            return false;
        }
        return $this->validate($node->left, $low, $node->val) &&
               $this->validate($node->right, $node->val, $high);
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
    func isValidBST(_ root: TreeNode?) -> Bool {
        return validate(root, lower: nil, upper: nil)
    }
    
    private func validate(_ node: TreeNode?, lower: Int64?, upper: Int64?) -> Bool {
        guard let n = node else { return true }
        let val = Int64(n.val)
        if let low = lower, val <= low { return false }
        if let high = upper, val >= high { return false }
        return validate(n.left, lower: lower, upper: val) && validate(n.right, lower: val, upper: upper)
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
    fun isValidBST(root: TreeNode?): Boolean {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE)
    }

    private fun validate(node: TreeNode?, low: Long, high: Long): Boolean {
        if (node == null) return true
        val v = node.`val`.toLong()
        if (v <= low || v >= high) return false
        return validate(node.left, low, v) && validate(node.right, v, high)
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
  bool isValidBST(TreeNode? root) {
    return _validate(root, null, null);
  }

  bool _validate(TreeNode? node, int? low, int? high) {
    if (node == null) return true;
    if ((low != null && node.val <= low) || (high != null && node.val >= high)) {
      return false;
    }
    return _validate(node.left, low, node.val) &&
           _validate(node.right, node.val, high);
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
func isValidBST(root *TreeNode) bool {
	var helper func(node *TreeNode, low, high *int) bool
	helper = func(node *TreeNode, low, high *int) bool {
		if node == nil {
			return true
		}
		if low != nil && node.Val <= *low {
			return false
		}
		if high != nil && node.Val >= *high {
			return false
		}
		if !helper(node.Left, low, &node.Val) {
			return false
		}
		if !helper(node.Right, &node.Val, high) {
			return false
		}
		return true
	}
	return helper(root, nil, nil)
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

def is_valid_bst(root)
  validate = lambda do |node, low, high|
    return true if node.nil?
    return false if (!low.nil? && node.val <= low) || (!high.nil? && node.val >= high)
    validate.call(node.left, low, node.val) && validate.call(node.right, node.val, high)
  end
  validate.call(root, nil, nil)
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
    def isValidBST(root: TreeNode): Boolean = {
        def validate(node: TreeNode, low: Long, high: Long): Boolean = {
            if (node == null) true
            else {
                val v = node.value.toLong
                if (v <= low || v >= high) false
                else validate(node.left, low, v) && validate(node.right, v, high)
            }
        }
        validate(root, Long.MinValue, Long.MaxValue)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn helper(node: Option<&Rc<RefCell<TreeNode>>>, min: i64, max: i64) -> bool {
            match node {
                None => true,
                Some(rc) => {
                    let n = rc.borrow();
                    let val = n.val as i64;
                    if val <= min || val >= max {
                        return false;
                    }
                    helper(n.left.as_ref(), min, val) && helper(n.right.as_ref(), val, max)
                }
            }
        }
        helper(root.as_ref(), i64::MIN, i64::MAX)
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

(define/contract (is-valid-bst root)
  (-> (or/c tree-node? #f) boolean?)
  (letrec ((valid?
            (lambda (node low high)
              (if (not node)
                  #t
                  (let* ((val (tree-node-val node))
                         (low-ok (or (not low) (< low val)))
                         (high-ok (or (not high) (> high val))))
                    (and low-ok high-ok
                         (valid? (tree-node-left node) low val)
                         (valid? (tree-node-right node) val high)))))))
    (valid? root #f #f)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec is_valid_bst(Root :: #tree_node{} | null) -> boolean().
is_valid_bst(Root) ->
    validate(Root, undefined, undefined).

validate(null, _Min, _Max) ->
    true;
validate(Node, Min, Max) ->
    Val = Node#tree_node.val,
    case (if Min =:= undefined -> true; true -> Val > Min end) andalso
         (if Max =:= undefined -> true; true -> Val < Max end) of
        false -> false;
        true ->
            Left = Node#tree_node.left,
            Right = Node#tree_node.right,
            validate(Left, Min, Val) andalso validate(Right, Val, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid_bst(root :: TreeNode.t() | nil) :: boolean()
  def is_valid_bst(root) do
    valid?(root, nil, nil)
  end

  defp valid?(nil, _min, _max), do: true

  defp valid?(%TreeNode{val: v, left: l, right: r}, min, max) do
    cond do
      not is_nil(min) and v <= min -> false
      not is_nil(max) and v >= max -> false
      true -> valid?(l, min, v) and valid?(r, v, max)
    end
  end
end
```
