# 0230. Kth Smallest Element in a BST

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
    int kthSmallest(TreeNode* root, int k) {
        std::stack<TreeNode*> st;
        while (true) {
            while (root) {
                st.push(root);
                root = root->left;
            }
            root = st.top();
            st.pop();
            if (--k == 0) return root->val;
            root = root->right;
        }
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
    public int kthSmallest(TreeNode root, int k) {
        java.util.ArrayDeque<TreeNode> stack = new java.util.ArrayDeque<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (--k == 0) {
                return curr.val;
            }
            curr = curr.right;
        }
        return -1; // Should never reach here given valid input
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
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right
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
int kthSmallest(struct TreeNode* root, int k) {
    // Stack to simulate recursion; size enough for max nodes (10^4)
    struct TreeNode *stack[10001];
    int top = -1;

    while (root != NULL || top != -1) {
        // Go as left as possible
        while (root != NULL) {
            stack[++top] = root;
            root = root->left;
        }
        // Process node
        root = stack[top--];
        if (--k == 0) {
            return root->val;
        }
        // Move to right subtree
        root = root->right;
    }
    // Should never reach here given valid input constraints
    return -1;
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
    public int KthSmallest(TreeNode root, int k) {
        var stack = new System.Collections.Generic.Stack<TreeNode>();
        TreeNode curr = root;
        while (curr != null || stack.Count > 0) {
            while (curr != null) {
                stack.Push(curr);
                curr = curr.left;
            }
            curr = stack.Pop();
            k--;
            if (k == 0) return curr.val;
            curr = curr.right;
        }
        // Should never reach here if input is valid
        return -1;
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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const stack = [];
    let node = root;
    while (true) {
        // Go to the leftmost node
        while (node !== null) {
            stack.push(node);
            node = node.left;
        }
        // Process node
        node = stack.pop();
        k--;
        if (k === 0) return node.val;
        // Move to right subtree
        node = node.right;
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

function kthSmallest(root: TreeNode | null, k: number): number {
    const stack: TreeNode[] = [];
    while (true) {
        while (root !== null) {
            stack.push(root);
            root = root.left;
        }
        root = stack.pop()!;
        if (--k === 0) return root.val;
        root = root.right;
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
     * @param Integer $k
     * @return Integer
     */
    function kthSmallest($root, $k) {
        $stack = [];
        while (true) {
            while ($root !== null) {
                $stack[] = $root;
                $root = $root->left;
            }
            $node = array_pop($stack);
            $k--;
            if ($k == 0) {
                return $node->val;
            }
            $root = $node->right;
        }
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
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        var stack = [TreeNode]()
        var node = root
        var remaining = k
        
        while true {
            while let cur = node {
                stack.append(cur)
                node = cur.left
            }
            let last = stack.removeLast()
            remaining -= 1
            if remaining == 0 {
                return last.val
            }
            node = last.right
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
    fun kthSmallest(root: TreeNode?, k: Int): Int {
        var count = 0
        val stack = java.util.ArrayDeque<TreeNode>()
        var node = root
        while (node != null || stack.isNotEmpty()) {
            while (node != null) {
                stack.push(node)
                node = node.left
            }
            node = stack.pop()
            count++
            if (count == k) return node.`val`
            node = node.right
        }
        // Should never reach here as per problem constraints
        return -1
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
  int kthSmallest(TreeNode? root, int k) {
    final List<TreeNode> stack = [];
    TreeNode? node = root;
    while (true) {
      while (node != null) {
        stack.add(node);
        node = node.left;
      }
      node = stack.removeLast();
      if (--k == 0) return node.val;
      node = node.right;
    }
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
func kthSmallest(root *TreeNode, k int) int {
    stack := []*TreeNode{}
    cur := root
    for cur != nil || len(stack) > 0 {
        for cur != nil {
            stack = append(stack, cur)
            cur = cur.Left
        }
        cur = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        k--
        if k == 0 {
            return cur.Val
        }
        cur = cur.Right
    }
    return -1 // unreachable given constraints
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

def kth_smallest(root, k)
  stack = []
  while !stack.empty? || root
    while root
      stack << root
      root = root.left
    end
    node = stack.pop
    k -= 1
    return node.val if k == 0
    root = node.right
  end
  nil
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
    def kthSmallest(root: TreeNode, k: Int): Int = {
        import scala.collection.mutable.Stack
        val stack = Stack[TreeNode]()
        var node = root
        var remaining = k

        while (stack.nonEmpty || node != null) {
            while (node != null) {
                stack.push(node)
                node = node.left
            }
            node = stack.pop()
            remaining -= 1
            if (remaining == 0) return node.value
            node = node.right
        }
        -1 // should never reach here given valid input
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut cur = root;
        let mut remaining = k;
        while !stack.is_empty() || cur.is_some() {
            while let Some(node_rc) = cur.clone() {
                stack.push(node_rc.clone());
                cur = node_rc.borrow().left.clone();
            }
            let node_rc = stack.pop().unwrap();
            remaining -= 1;
            if remaining == 0 {
                return node_rc.borrow().val;
            }
            cur = node_rc.borrow().right.clone();
        }
        // Given constraints, this line is never reached.
        -1
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (kth-smallest root k)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (let ((counter (box k))
        (ans #f))
    (define (inorder node)
      (when (and node (not ans))
        (inorder (tree-node-left node))
        (when (not ans)
          (set-box! counter (- (unbox counter) 1))
          (when (= (unbox counter) 0)
            (set! ans (tree-node-val node))))
        (when (and (not ans) (> (unbox counter) 0))
          (inorder (tree-node-right node)))))
    (inorder root)
    ans))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec kth_smallest(Root :: #tree_node{} | null, K :: integer()) -> integer().
kth_smallest(Root, K) ->
    case kth_smallest_helper(Root, K) of
        {found, Val} -> Val;
        _ -> erlang:error(badarg)
    end.

-spec kth_smallest_helper(Node :: #tree_node{} | null, K :: integer()) ->
          {found, integer()} | {continue, integer()}.
kth_smallest_helper(null, K) ->
    {continue, K};
kth_smallest_helper(#tree_node{val = V, left = L, right = R}, K) ->
    case kth_smallest_helper(L, K) of
        {found, Val} -> {found, Val};
        {continue, K1} ->
            if K1 == 1 ->
                    {found, V};
               true ->
                    kth_smallest_helper(R, K1 - 1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest(root :: TreeNode.t | nil, k :: integer) :: integer
  def kth_smallest(root, k) do
    traverse(root, [], k)
  end

  # Dive left as far as possible
  defp traverse(node, stack, k) when not is_nil(node) do
    traverse(node.left, [node | stack], k)
  end

  # No more left nodes; process the stack
  defp traverse(nil, [curr | rest], k) do
    new_k = k - 1
    if new_k == 0 do
      curr.val
    else
      traverse(curr.right, rest, new_k)
    end
  end

  # Fallback (should not occur with valid input)
  defp traverse(_, [], _), do: nil
end
```
