# 1080. Insufficient Nodes in Root to Leaf Paths

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
    long long lim;
    const long long NEG_INF = LLONG_MIN / 4;
    
public:
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        lim = limit;
        if (!root) return nullptr;
        long long maxSum = dfs(root);
        if (maxSum < lim) {
            deleteSubtree(root);
            return nullptr;
        }
        return root;
    }
    
private:
    long long dfs(TreeNode* node) {
        if (!node) return NEG_INF;
        long long leftMax = dfs(node->left);
        long long rightMax = dfs(node->right);
        
        if (node->left && node->val + leftMax < lim) {
            deleteSubtree(node->left);
            node->left = nullptr;
        }
        if (node->right && node->val + rightMax < lim) {
            deleteSubtree(node->right);
            node->right = nullptr;
        }
        
        if (!node->left && !node->right) {
            return node->val;
        } else {
            long long childMax = NEG_INF;
            if (node->left) childMax = std::max(childMax, leftMax);
            if (node->right) childMax = std::max(childMax, rightMax);
            return node->val + childMax;
        }
    }
    
    void deleteSubtree(TreeNode* node) {
        if (!node) return;
        deleteSubtree(node->left);
        deleteSubtree(node->right);
        delete node;
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
    public TreeNode sufficientSubset(TreeNode root, int limit) {
        long maxSum = dfs(root, limit);
        return maxSum == Long.MIN_VALUE ? null : root;
    }

    private long dfs(TreeNode node, int limit) {
        if (node == null) {
            return Long.MIN_VALUE;
        }
        // Leaf case
        if (node.left == null && node.right == null) {
            return node.val >= limit ? node.val : Long.MIN_VALUE;
        }

        long leftMax = dfs(node.left, limit);
        long rightMax = dfs(node.right, limit);

        if (leftMax == Long.MIN_VALUE) {
            node.left = null;
        }
        if (rightMax == Long.MIN_VALUE) {
            node.right = null;
        }

        long childBest = Math.max(leftMax, rightMax);
        // If both children are removed, treat this node as a leaf
        if (childBest == Long.MIN_VALUE) {
            return node.val >= limit ? node.val : Long.MIN_VALUE;
        }

        long maxPathSum = node.val + childBest;
        return maxPathSum >= limit ? maxPathSum : Long.MIN_VALUE;
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
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return None

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # prune left child if insufficient
            if node.left:
                if left_max is None or left_max + node.val < limit:
                    node.left = None
            # prune right child if insufficient
            if node.right:
                if right_max is None or right_max + node.val < limit:
                    node.right = None

            # after pruning, check if this becomes a leaf
            if not node.left and not node.right:
                return node.val if node.val >= limit else None

            # compute max sum from this node to any remaining leaf
            candidates = []
            if node.left:
                candidates.append(left_max)
            if node.right:
                candidates.append(right_max)
            max_child = max(candidates)  # at least one child remains
            return node.val + max_child

        keep_root = dfs(root)
        return root if keep_root is not None else None
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
    def sufficientSubset(self, root, limit: int):
        def dfs(node, cur_sum):
            if not node:
                return None
            new_sum = cur_sum + node.val
            # Process children
            node.left = dfs(node.left, new_sum)
            node.right = dfs(node.right, new_sum)
            # If leaf after pruning or original leaf
            if not node.left and not node.right:
                if new_sum < limit:
                    return None
            return node

        return dfs(root, 0)
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
static struct TreeNode* prune(struct TreeNode* node, long long curSum, int limit) {
    if (!node) return NULL;
    long long newSum = curSum + node->val;
    node->left  = prune(node->left,  newSum, limit);
    node->right = prune(node->right, newSum, limit);
    if (!node->left && !node->right) {
        if (newSum < limit) return NULL;
    }
    return node;
}

struct TreeNode* sufficientSubset(struct TreeNode* root, int limit) {
    return prune(root, 0LL, limit);
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
    public TreeNode SufficientSubset(TreeNode root, int limit) {
        return Prune(root, 0L, limit);
    }

    private TreeNode Prune(TreeNode node, long accSum, int limit) {
        if (node == null) return null;
        long curSum = accSum + node.val;

        node.left = Prune(node.left, curSum, limit);
        node.right = Prune(node.right, curSum, limit);

        // If both children are removed, this becomes a leaf.
        if (node.left == null && node.right == null) {
            if (curSum < limit) return null;
        }
        return node;
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
 * @param {number} limit
 * @return {TreeNode}
 */
var sufficientSubset = function(root, limit) {
    const dfs = (node) => {
        if (!node) return -Infinity;
        let leftMax = dfs(node.left);
        let rightMax = dfs(node.right);
        
        // prune left child if insufficient
        if (node.left && node.val + leftMax < limit) {
            node.left = null;
            leftMax = -Infinity;
        }
        // prune right child if insufficient
        if (node.right && node.val + rightMax < limit) {
            node.right = null;
            rightMax = -Infinity;
        }
        
        const maxChild = Math.max(leftMax, rightMax);
        // leaf case
        if (maxChild === -Infinity) return node.val;
        return node.val + maxChild;
    };
    
    const maxSum = dfs(root);
    return maxSum >= limit ? root : null;
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

function sufficientSubset(root: TreeNode | null, limit: number): TreeNode | null {
    function dfs(node: TreeNode | null, sum: number): TreeNode | null {
        if (!node) return null;
        const newSum = sum + node.val;
        // If leaf node
        if (!node.left && !node.right) {
            return newSum >= limit ? node : null;
        }
        node.left = dfs(node.left, newSum);
        node.right = dfs(node.right, newSum);
        // After pruning children, if both are gone, treat as leaf
        if (!node.left && !node.right) {
            return newSum >= limit ? node : null;
        }
        return node;
    }
    return dfs(root, 0);
}
```

## Php

```php
<?php
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
     * @param Integer $limit
     * @return TreeNode
     */
    function sufficientSubset($root, $limit) {
        [$newRoot, $_] = $this->dfs($root, $limit);
        return $newRoot;
    }

    private function dfs($node, $limit) {
        if ($node === null) {
            return [null, PHP_INT_MIN];
        }
        // Process left and right subtrees
        [$leftNode, $leftMax] = $this->dfs($node->left, $limit);
        [$rightNode, $rightMax] = $this->dfs($node->right, $limit);
        $node->left = $leftNode;
        $node->right = $rightNode;

        // Determine maximum sum from this node to any leaf
        if ($node->left === null && $node->right === null) {
            $maxPath = $node->val;
        } else {
            $maxChild = max($leftMax, $rightMax);
            $maxPath = $node->val + $maxChild;
        }

        // Prune node if insufficient
        if ($maxPath < $limit) {
            return [null, $maxPath];
        }
        return [$node, $maxPath];
    }
}
?>
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
    func sufficientSubset(_ root: TreeNode?, _ limit: Int) -> TreeNode? {
        func dfs(_ node: TreeNode?, _ acc: Int) -> TreeNode? {
            guard let n = node else { return nil }
            let leftPruned = dfs(n.left, acc + n.val)
            let rightPruned = dfs(n.right, acc + n.val)
            n.left = leftPruned
            n.right = rightPruned
            // If after pruning both children are gone, this becomes a leaf.
            if n.left == nil && n.right == nil {
                if acc + n.val < limit {
                    return nil
                }
            }
            return n
        }
        return dfs(root, 0)
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
    fun sufficientSubset(root: TreeNode?, limit: Int): TreeNode? {
        fun dfs(node: TreeNode?, sum: Long): TreeNode? {
            if (node == null) return null
            val newSum = sum + node.`val`.toLong()
            // leaf node
            if (node.left == null && node.right == null) {
                return if (newSum < limit) null else node
            }
            node.left = dfs(node.left, newSum)
            node.right = dfs(node.right, newSum)
            // prune current node if both children are removed
            return if (node.left == null && node.right == null) null else node
        }
        return dfs(root, 0L)
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
  TreeNode? sufficientSubset(TreeNode? root, int limit) {
    TreeNode? dfs(TreeNode? node, int curSum) {
      if (node == null) return null;
      int newSum = curSum + node.val;
      node.left = dfs(node.left, newSum);
      node.right = dfs(node.right, newSum);
      if (node.left == null && node.right == null) {
        if (newSum < limit) return null;
      }
      return node;
    }

    return dfs(root, 0);
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
func sufficientSubset(root *TreeNode, limit int) *TreeNode {
    const negInf = -1 << 60
    var dfs func(*TreeNode) (*TreeNode, int)
    dfs = func(node *TreeNode) (*TreeNode, int) {
        if node == nil {
            return nil, negInf
        }
        // Leaf case (original leaf)
        if node.Left == nil && node.Right == nil {
            if node.Val < limit {
                return nil, node.Val
            }
            return node, node.Val
        }

        leftNode, leftMax := dfs(node.Left)
        rightNode, rightMax := dfs(node.Right)

        node.Left = leftNode
        node.Right = rightNode

        maxChild := leftMax
        if rightMax > maxChild {
            maxChild = rightMax
        }

        var best int
        if maxChild == negInf { // both children removed, becomes leaf
            best = node.Val
        } else {
            best = node.Val + maxChild
        }

        if best < limit {
            return nil, best
        }
        return node, best
    }

    res, _ := dfs(root)
    return res
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

def sufficient_subset(root, limit)
  prune = ->(node, acc) do
    return nil unless node
    total = acc + node.val
    node.left = prune.call(node.left, total)
    node.right = prune.call(node.right, total)
    if node.left.nil? && node.right.nil?
      return nil if total < limit
    end
    node
  end

  prune.call(root, 0)
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
    def sufficientSubset(root: TreeNode, limit: Int): TreeNode = {
        def dfs(node: TreeNode, acc: Long): TreeNode = {
            if (node == null) return null
            val newAcc = acc + node.value.toLong
            node.left = dfs(node.left, newAcc)
            node.right = dfs(node.right, newAcc)
            if (node.left == null && node.right == null && newAcc < limit) null else node
        }
        dfs(root, 0L)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sufficient_subset(root: Option<Rc<RefCell<TreeNode>>>, limit: i32) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, cur_sum: i64, limit: i64) -> Option<Rc<RefCell<TreeNode>>> {
            match node {
                Some(rc_node) => {
                    let mut n = rc_node.borrow_mut();
                    let new_sum = cur_sum + n.val as i64;

                    let left_child = n.left.take();
                    let right_child = n.right.take();

                    let pruned_left = dfs(left_child, new_sum, limit);
                    let pruned_right = dfs(right_child, new_sum, limit);

                    n.left = pruned_left;
                    n.right = pruned_right;

                    if n.left.is_none() && n.right.is_none() && new_sum < limit {
                        None
                    } else {
                        Some(rc_node)
                    }
                }
                None => None,
            }
        }

        dfs(root, 0, limit as i64)
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

(define/contract (sufficient-subset root limit)
  (-> (or/c tree-node? #f) exact-integer? (or/c tree-node? #f))
  (letrec ((dfs
            (lambda (node acc)
              (if (not node)
                  #f
                  (let* ((new-acc (+ acc (tree-node-val node)))
                         (left-pruned (dfs (tree-node-left node) new-acc))
                         (right-pruned (dfs (tree-node-right node) new-acc)))
                    (set-tree-node-left! node left-pruned)
                    (set-tree-node-right! node right-pruned)
                    (if (and (not left-pruned) (not right-pruned))
                        (if (>= new-acc limit) node #f)
                        node))))))
    (dfs root 0)))
```

## Erlang

```erlang
-module(solution).
-export([sufficient_subset/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec sufficient_subset(Root :: #tree_node{} | null, Limit :: integer()) -> #tree_node{} | null.
sufficient_subset(Root, Limit) ->
    prune(Root, 0, Limit).

prune(null, _, _) -> 
    null;
prune(#tree_node{val = V, left = L, right = R} = Node, Sum, Limit) ->
    NewSum = Sum + V,
    PrunedLeft = prune(L, NewSum, Limit),
    PrunedRight = prune(R, NewSum, Limit),
    case {PrunedLeft, PrunedRight} of
        {null, null} ->
            if NewSum >= Limit ->
                    Node#tree_node{left = null, right = null};
               true -> 
                    null
            end;
        _ ->
            Node#tree_node{left = PrunedLeft, right = PrunedRight}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sufficient_subset(root :: TreeNode.t | nil, limit :: integer) :: TreeNode.t | nil
  def sufficient_subset(root, limit) do
    prune(root, 0, limit)
  end

  defp prune(nil, _cur_sum, _limit), do: nil

  defp prune(%TreeNode{val: v, left: l, right: r} = node, cur_sum, limit) do
    new_sum = cur_sum + v
    left_pruned = prune(l, new_sum, limit)
    right_pruned = prune(r, new_sum, limit)

    pruned_node = %TreeNode{node | left: left_pruned, right: right_pruned}

    if pruned_node.left == nil and pruned_node.right == nil and new_sum < limit do
      nil
    else
      pruned_node
    end
  end
end
```
