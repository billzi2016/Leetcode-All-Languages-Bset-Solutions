# 0144. Binary Tree Preorder Traversal

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (!root) return ans;
        stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top();
            st.pop();
            ans.push_back(node->val);
            if (node->right) st.push(node->right);
            if (node->left)  st.push(node->left);
        }
        return ans;
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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            result.add(node.val);
            if (node.right != null) stack.push(node.right);
            if (node.left != null) stack.push(node.left);
        }
        return result;
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
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            # push right first so that left is processed next
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return output
```

## Python3

```python
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (root == NULL) {
        return NULL;
    }
    
    /* Maximum number of nodes is 100 as per constraints */
    int capacity = 100;
    int *result = (int *)malloc(capacity * sizeof(int));
    struct TreeNode **stack = (struct TreeNode **)malloc(capacity * sizeof(struct TreeNode*));
    
    int top = -1;
    stack[++top] = root;
    
    while (top >= 0) {
        struct TreeNode *node = stack[top--];
        result[(*returnSize)++] = node->val;
        
        if (node->right != NULL) {
            stack[++top] = node->right;
        }
        if (node->left != NULL) {
            stack[++top] = node->left;
        }
    }
    
    free(stack);
    return result;
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
    public IList<int> PreorderTraversal(TreeNode root) {
        var result = new List<int>();
        if (root == null) return result;
        var stack = new Stack<TreeNode>();
        stack.Push(root);
        while (stack.Count > 0) {
            var node = stack.Pop();
            result.Add(node.val);
            if (node.right != null) stack.Push(node.right);
            if (node.left != null) stack.Push(node.left);
        }
        return result;
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
 * @return {number[]}
 */
var preorderTraversal = function(root) {
    const result = [];
    if (!root) return result;
    const stack = [root];
    while (stack.length) {
        const node = stack.pop();
        result.push(node.val);
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
    }
    return result;
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

function preorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    if (!root) return result;
    const stack: TreeNode[] = [root];
    while (stack.length) {
        const node = stack.pop()!;
        result.push(node.val);
        if (node.right) stack.push(node.right);
        if (node.left) stack.push(node.left);
    }
    return result;
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
     * @return Integer[]
     */
    function preorderTraversal($root) {
        $result = [];
        if ($root === null) {
            return $result;
        }

        $stack = [$root];
        while (!empty($stack)) {
            $node = array_pop($stack);
            $result[] = $node->val;

            // push right first so that left is processed first
            if ($node->right !== null) {
                $stack[] = $node->right;
            }
            if ($node->left !== null) {
                $stack[] = $node->left;
            }
        }

        return $result;
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
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        guard let root = root else { return result }
        var stack: [TreeNode] = [root]
        while !stack.isEmpty {
            let node = stack.removeLast()
            result.append(node.val)
            if let right = node.right {
                stack.append(right)
            }
            if let left = node.left {
                stack.append(left)
            }
        }
        return result
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
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        if (root == null) return result
        val stack = java.util.ArrayDeque<TreeNode>()
        stack.push(root)
        while (!stack.isEmpty()) {
            val node = stack.pop()
            result.add(node.`val`)
            node.right?.let { stack.push(it) }
            node.left?.let { stack.push(it) }
        }
        return result
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
  List<int> preorderTraversal(TreeNode? root) {
    if (root == null) return [];
    final List<int> result = [];
    final List<TreeNode> stack = [root];
    while (stack.isNotEmpty) {
      final node = stack.removeLast();
      result.add(node.val);
      if (node.right != null) stack.add(node.right!);
      if (node.left != null) stack.add(node.left!);
    }
    return result;
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
func preorderTraversal(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    stack := []*TreeNode{root}
    result := make([]int, 0, 100)
    for len(stack) > 0 {
        // pop last element
        n := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        result = append(result, n.Val)
        if n.Right != nil {
            stack = append(stack, n.Right)
        }
        if n.Left != nil {
            stack = append(stack, n.Left)
        }
    }
    return result
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

def preorder_traversal(root)
  return [] if root.nil?
  stack = [root]
  result = []
  until stack.empty?
    node = stack.pop
    result << node.val
    stack << node.right if node.right
    stack << node.left if node.left
  end
  result
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
    def preorderTraversal(root: TreeNode): List[Int] = {
        if (root == null) return Nil
        val stack = new scala.collection.mutable.Stack[TreeNode]()
        val result = scala.collection.mutable.ListBuffer[Int]()
        stack.push(root)
        while (stack.nonEmpty) {
            val node = stack.pop()
            result += node.value
            if (node.right != null) stack.push(node.right)
            if (node.left != null)  stack.push(node.left)
        }
        result.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn preorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        let mut stack = Vec::new();

        if let Some(node) = root {
            stack.push(node);
        }

        while let Some(rc_node) = stack.pop() {
            let node = rc_node.borrow();
            result.push(node.val);
            if let Some(ref right) = node.right {
                stack.push(Rc::clone(right));
            }
            if let Some(ref left) = node.left {
                stack.push(Rc::clone(left));
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (preorder-traversal root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (if (not root)
      '()
      (let loop ((stack (list root)) (acc '()))
        (if (null? stack)
            (reverse acc)
            (let* ((node (car stack))
                   (rest (cdr stack))
                   (val (tree-node-val node))
                   (left (tree-node-left node))
                   (right (tree-node-right node))
                   (new-stack
                     (let ((s (if right (cons right rest) rest)))
                       (if left (cons left s) s))))
              (loop new-stack (cons val acc)))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec preorder_traversal(Root :: #tree_node{} | null) -> [integer()].
preorder_traversal(null) ->
    [];
preorder_traversal(Root) ->
    preorder_iter([Root], []).

preorder_iter([], Acc) ->
    lists:reverse(Acc);
preorder_iter([#tree_node{val = V, left = L, right = R} | Stack], Acc) ->
    NewStack = case R of
        null -> Stack;
        _ -> [R | Stack]
    end,
    NewStack2 = case L of
        null -> NewStack;
        _ -> [L | NewStack]
    end,
    preorder_iter(NewStack2, [V | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec preorder_traversal(root :: TreeNode.t | nil) :: [integer]
  def preorder_traversal(nil), do: []
  def preorder_traversal(root) do
    traverse([root], [])
  end

  defp traverse([], acc), do: Enum.reverse(acc)
  defp traverse([nil | rest], acc), do: traverse(rest, acc)

  defp traverse([%TreeNode{val: v, left: l, right: r} | rest], acc) do
    new_stack =
      (if r != nil, do: [r], else: []) ++
      (if l != nil, do: [l], else: []) ++
      rest

    traverse(new_stack, [v | acc])
  end
end
```
