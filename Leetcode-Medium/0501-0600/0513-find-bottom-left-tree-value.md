# 0513. Find Bottom Left Tree Value

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
    int findBottomLeftValue(TreeNode* root) {
        maxDepth = -1;
        bottomLeftVal = 0;
        dfs(root, 0);
        return bottomLeftVal;
    }
private:
    int maxDepth;
    int bottomLeftVal;
    
    void dfs(TreeNode* node, int depth) {
        if (!node) return;
        if (depth > maxDepth) {
            maxDepth = depth;
            bottomLeftVal = node->val;
        }
        dfs(node->left, depth + 1);
        dfs(node->right, depth + 1);
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
    private int maxDepth = -1;
    private int bottomLeftValue;

    public int findBottomLeftValue(TreeNode root) {
        dfs(root, 0);
        return bottomLeftValue;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        if (depth > maxDepth) {
            maxDepth = depth;
            bottomLeftValue = node.val;
        }
        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
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
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_depth = -1
        bottom_left = None

        def dfs(node, depth):
            nonlocal max_depth, bottom_left
            if not node:
                return
            # first time we reach this depth -> leftmost node at that level
            if depth > max_depth:
                max_depth = depth
                bottom_left = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return bottom_left
```

## Python3

```python
import collections
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional['TreeNode']) -> int:
        queue = collections.deque([root])
        node = None
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
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

static int maxDepth;
static int bottomLeftVal;

static void dfs(struct TreeNode* node, int depth) {
    if (!node) return;
    if (depth > maxDepth) {
        maxDepth = depth;
        bottomLeftVal = node->val;
    }
    dfs(node->left, depth + 1);
    dfs(node->right, depth + 1);
}

int findBottomLeftValue(struct TreeNode* root) {
    maxDepth = -1;
    bottomLeftVal = 0;
    dfs(root, 0);
    return bottomLeftVal;
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
    private int maxDepth = -1;
    private int bottomLeftValue;

    public int FindBottomLeftValue(TreeNode root)
    {
        DFS(root, 0);
        return bottomLeftValue;
    }

    private void DFS(TreeNode node, int depth)
    {
        if (node == null) return;

        // First time we reach this depth, it's the leftmost node at that level
        if (depth > maxDepth)
        {
            maxDepth = depth;
            bottomLeftValue = node.val;
        }

        DFS(node.left, depth + 1);
        DFS(node.right, depth + 1);
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
 * @return {number}
 */
var findBottomLeftValue = function(root) {
    let maxDepth = -1;
    let bottomLeft = 0;
    
    const dfs = (node, depth) => {
        if (!node) return;
        // first node encountered at this depth is the leftmost
        if (depth > maxDepth) {
            maxDepth = depth;
            bottomLeft = node.val;
        }
        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
    };
    
    dfs(root, 0);
    return bottomLeft;
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

function findBottomLeftValue(root: TreeNode | null): number {
    if (!root) return 0;
    const queue: TreeNode[] = [root];
    let node: TreeNode = root;
    for (let i = 0; i < queue.length; i++) {
        node = queue[i];
        // enqueue right child first, then left child
        if (node.right) queue.push(node.right);
        if (node.left) queue.push(node.left);
    }
    return node.val;
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
     * @return int
     */
    function findBottomLeftValue($root) {
        $queue = new SplQueue();
        $queue->enqueue($root);
        $node = null;
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            if ($node->right !== null) {
                $queue->enqueue($node->right);
            }
            if ($node->left !== null) {
                $queue->enqueue($node->left);
            }
        }
        return $node->val;
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
    func findBottomLeftValue(_ root: TreeNode?) -> Int {
        var maxDepth = -1
        var bottomLeft = 0
        
        func dfs(_ node: TreeNode?, _ depth: Int) {
            guard let node = node else { return }
            if depth > maxDepth {
                maxDepth = depth
                bottomLeft = node.val
            }
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        }
        
        dfs(root, 0)
        return bottomLeft
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findBottomLeftValue(root: TreeNode?): Int {
        var maxDepth = -1
        var result = 0

        fun dfs(node: TreeNode?, depth: Int) {
            if (node == null) return
            if (depth > maxDepth) {
                maxDepth = depth
                result = node.`val`
            }
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        }

        dfs(root, 0)
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
  int findBottomLeftValue(TreeNode? root) {
    int maxDepth = -1;
    int leftmost = 0;

    void dfs(TreeNode? node, int depth) {
      if (node == null) return;
      if (depth > maxDepth) {
        maxDepth = depth;
        leftmost = node.val;
      }
      dfs(node.left, depth + 1);
      dfs(node.right, depth + 1);
    }

    dfs(root, 0);
    return leftmost;
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
func findBottomLeftValue(root *TreeNode) int {
    maxDepth := -1
    result := 0

    var dfs func(node *TreeNode, depth int)
    dfs = func(node *TreeNode, depth int) {
        if node == nil {
            return
        }
        if depth > maxDepth {
            maxDepth = depth
            result = node.Val
        }
        dfs(node.Left, depth+1)
        dfs(node.Right, depth+1)
    }

    dfs(root, 0)
    return result
}
```

## Ruby

```ruby
def find_bottom_left_value(root)
  max_depth = -1
  result = nil

  dfs = lambda do |node, depth|
    return if node.nil?
    if depth > max_depth
      max_depth = depth
      result = node.val
    end
    dfs.call(node.left, depth + 1)
    dfs.call(node.right, depth + 1)
  end

  dfs.call(root, 0)
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
  def findBottomLeftValue(root: TreeNode): Int = {
    var maxDepth = -1
    var answer = 0

    def dfs(node: TreeNode, depth: Int): Unit = {
      if (node == null) return
      if (depth > maxDepth) {
        maxDepth = depth
        answer = node.value
      }
      dfs(node.left, depth + 1)
      dfs(node.right, depth + 1)
    }

    dfs(root, 0)
    answer
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, depth: usize, max_depth: &mut usize, ans: &mut i32) {
            if let Some(rc_node) = node {
                let n = rc_node.borrow();
                if depth > *max_depth {
                    *max_depth = depth;
                    *ans = n.val;
                }
                dfs(&n.left, depth + 1, max_depth, ans);
                dfs(&n.right, depth + 1, max_depth, ans);
            }
        }

        let root_ref = root.as_ref().unwrap();
        let mut answer = root_ref.borrow().val;
        let mut max_depth = 0usize;
        dfs(&root, 0, &mut max_depth, &mut answer);
        answer
    }
}
```

## Racket

```racket
(define/contract (find-bottom-left-value root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((max-depth -1)
        (result 0))
    (define (dfs node depth)
      (when node
        (when (> depth max-depth)
          (set! max-depth depth)
          (set! result (tree-node-val node)))
        (dfs (tree-node-left node) (+ depth 1))
        (dfs (tree-node-right node) (+ depth 1))))
    (dfs root 0)
    result))
```

## Erlang

```erlang
-spec find_bottom_left_value(Root :: #tree_node{} | null) -> integer().
find_bottom_left_value(null) ->
    0;
find_bottom_left_value(Root) ->
    {_Depth, Value} = dfs(Root, 0, -1, 0),
    Value.

dfs(null, _Depth, MaxDepth, BottomVal) ->
    {MaxDepth, BottomVal};
dfs(Node, Depth, MaxDepth, BottomVal) ->
    case Depth > MaxDepth of
        true ->
            NewMax = Depth,
            NewVal = Node#tree_node.val;
        false ->
            NewMax = MaxDepth,
            NewVal = BottomVal
    end,
    {AfterLeftMax, AfterLeftVal} = dfs(Node#tree_node.left, Depth + 1, NewMax, NewVal),
    dfs(Node#tree_node.right, Depth + 1, AfterLeftMax, AfterLeftVal).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_bottom_left_value(root :: TreeNode.t() | nil) :: integer
  def find_bottom_left_value(nil), do: 0

  def find_bottom_left_value(root) do
    {_depth, value} = dfs(root, 0, {-1, nil})
    value
  end

  defp dfs(nil, _depth, acc), do: acc

  defp dfs(%TreeNode{val: v, left: l, right: r}, depth, {max_depth, ans}) do
    {new_max, new_ans} =
      if depth > max_depth do
        {depth, v}
      else
        {max_depth, ans}
      end

    acc_left = dfs(l, depth + 1, {new_max, new_ans})
    dfs(r, depth + 1, acc_left)
  end
end
```
