# 1382. Balance a Binary Search Tree

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
    TreeNode* balanceBST(TreeNode* root) {
        if (!root) return nullptr;
        vector<int> vals;
        inorder(root, vals);
        return build(vals, 0, (int)vals.size() - 1);
    }
private:
    void inorder(TreeNode* node, vector<int>& vals) {
        if (!node) return;
        inorder(node->left, vals);
        vals.push_back(node->val);
        inorder(node->right, vals);
    }
    
    TreeNode* build(const vector<int>& vals, int l, int r) {
        if (l > r) return nullptr;
        int m = l + (r - l) / 2;
        TreeNode* node = new TreeNode(vals[m]);
        node->left = build(vals, l, m - 1);
        node->right = build(vals, m + 1, r);
        return node;
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
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        inorder(root, vals);
        return build(vals, 0, vals.size() - 1);
    }

    private void inorder(TreeNode node, List<Integer> vals) {
        if (node == null) return;
        inorder(node.left, vals);
        vals.add(node.val);
        inorder(node.right, vals);
    }

    private TreeNode build(List<Integer> vals, int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(vals.get(mid));
        node.left = build(vals, left, mid - 1);
        node.right = build(vals, mid + 1, right);
        return node;
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
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Inorder traversal to collect node values in sorted order
        vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)

        # Build balanced BST from sorted values
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(vals[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(vals) - 1)
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node: Optional[TreeNode], vals: List[int]) -> None:
            if not node:
                return
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)

        def build(vals: List[int], lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(vals[mid])
            node.left = build(vals, lo, mid - 1)
            node.right = build(vals, mid + 1, hi)
            return node

        values: List[int] = []
        inorder(root, values)
        return build(values, 0, len(values) - 1)
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

static int *vals = NULL;
static int valsSize = 0;
static int valsCap = 0;

static void inorder(struct TreeNode* node) {
    if (!node) return;
    inorder(node->left);
    if (valsSize == valsCap) {
        valsCap = valsCap ? valsCap * 2 : 256;
        vals = realloc(vals, valsCap * sizeof(int));
    }
    vals[valsSize++] = node->val;
    inorder(node->right);
}

static struct TreeNode* build(int l, int r) {
    if (l > r) return NULL;
    int m = l + (r - l) / 2;
    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = vals[m];
    root->left = build(l, m - 1);
    root->right = build(m + 1, r);
    return root;
}

struct TreeNode* balanceBST(struct TreeNode* root) {
    if (!root) return NULL;
    inorder(root);
    struct TreeNode* balanced = build(0, valsSize - 1);
    free(vals);
    vals = NULL;
    valsSize = valsCap = 0;
    return balanced;
}
```

## Csharp

```csharp
using System.Collections.Generic;

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
    private List<int> inorderValues = new List<int>();

    public TreeNode BalanceBST(TreeNode root)
    {
        if (root == null) return null;

        Inorder(root);
        return BuildBalanced(0, inorderValues.Count - 1);
    }

    private void Inorder(TreeNode node)
    {
        if (node == null) return;
        Inorder(node.left);
        inorderValues.Add(node.val);
        Inorder(node.right);
    }

    private TreeNode BuildBalanced(int left, int right)
    {
        if (left > right) return null;

        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(inorderValues[mid]);
        node.left = BuildBalanced(left, mid - 1);
        node.right = BuildBalanced(mid + 1, right);
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
 * @return {TreeNode}
 */
var balanceBST = function(root) {
    const vals = [];
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        vals.push(node.val);
        inorder(node.right);
    };
    inorder(root);
    
    const build = (l, r) => {
        if (l > r) return null;
        const m = Math.floor((l + r) / 2);
        const node = new TreeNode(vals[m]);
        node.left = build(l, m - 1);
        node.right = build(m + 1, r);
        return node;
    };
    
    return build(0, vals.length - 1);
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

function balanceBST(root: TreeNode | null): TreeNode | null {
    const values: number[] = [];

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);
        values.push(node.val);
        inorder(node.right);
    };

    inorder(root);

    const build = (l: number, r: number): TreeNode | null => {
        if (l > r) return null;
        const m = Math.floor((l + r) / 2);
        const node = new TreeNode(values[m]);
        node.left = build(l, m - 1);
        node.right = build(m + 1, r);
        return node;
    };

    return build(0, values.length - 1);
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
     * @return TreeNode
     */
    function balanceBST($root) {
        $vals = [];
        $this->inorder($root, $vals);
        return $this->buildBalanced($vals, 0, count($vals) - 1);
    }

    private function inorder($node, &$arr) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left, $arr);
        $arr[] = $node->val;
        $this->inorder($node->right, $arr);
    }

    private function buildBalanced(&$arr, $l, $r) {
        if ($l > $r) {
            return null;
        }
        $mid = intdiv($l + $r, 2);
        $newNode = new TreeNode($arr[$mid]);
        $newNode->left = $this->buildBalanced($arr, $l, $mid - 1);
        $newNode->right = $this->buildBalanced($arr, $mid + 1, $r);
        return $newNode;
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
    func balanceBST(_ root: TreeNode?) -> TreeNode? {
        var values = [Int]()
        inorder(root, &values)
        return build(values, 0, values.count - 1)
    }
    
    private func inorder(_ node: TreeNode?, _ arr: inout [Int]) {
        guard let n = node else { return }
        inorder(n.left, &arr)
        arr.append(n.val)
        inorder(n.right, &arr)
    }
    
    private func build(_ arr: [Int], _ left: Int, _ right: Int) -> TreeNode? {
        if left > right { return nil }
        let mid = (left + right) / 2
        let node = TreeNode(arr[mid])
        node.left = build(arr, left, mid - 1)
        node.right = build(arr, mid + 1, right)
        return node
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
    fun balanceBST(root: TreeNode?): TreeNode? {
        val values = mutableListOf<Int>()
        inorder(root, values)
        return build(values, 0, values.size - 1)
    }

    private fun inorder(node: TreeNode?, list: MutableList<Int>) {
        if (node == null) return
        inorder(node.left, list)
        list.add(node.`val`)
        inorder(node.right, list)
    }

    private fun build(list: List<Int>, left: Int, right: Int): TreeNode? {
        if (left > right) return null
        val mid = (left + right) / 2
        val node = TreeNode(list[mid])
        node.left = build(list, left, mid - 1)
        node.right = build(list, mid + 1, right)
        return node
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
  TreeNode? balanceBST(TreeNode? root) {
    final List<int> vals = [];

    void inorder(TreeNode? node) {
      if (node == null) return;
      inorder(node.left);
      vals.add(node.val);
      inorder(node.right);
    }

    inorder(root);

    TreeNode? build(int l, int r) {
      if (l > r) return null;
      final int m = (l + r) >> 1;
      final TreeNode node = TreeNode(vals[m]);
      node.left = build(l, m - 1);
      node.right = build(m + 1, r);
      return node;
    }

    return build(0, vals.length - 1);
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

func balanceBST(root *TreeNode) *TreeNode {
    var vals []int
    inorder(root, &vals)
    return build(vals, 0, len(vals)-1)
}

func inorder(node *TreeNode, out *[]int) {
    if node == nil {
        return
    }
    inorder(node.Left, out)
    *out = append(*out, node.Val)
    inorder(node.Right, out)
}

func build(nums []int, l, r int) *TreeNode {
    if l > r {
        return nil
    }
    mid := (l + r) / 2
    n := &TreeNode{Val: nums[mid]}
    n.Left = build(nums, l, mid-1)
    n.Right = build(nums, mid+1, r)
    return n
}
```

## Ruby

```ruby
def balance_bst(root)
  # Inorder traversal to collect values in sorted order
  vals = []
  stack = []
  node = root
  while node || !stack.empty?
    while node
      stack << node
      node = node.left
    end
    node = stack.pop
    vals << node.val
    node = node.right
  end

  # Recursive construction of balanced BST from sorted values
  build = lambda do |l, r|
    return nil if l > r
    m = (l + r) / 2
    new_node = TreeNode.new(vals[m])
    new_node.left = build.call(l, m - 1)
    new_node.right = build.call(m + 1, r)
    new_node
  end

  build.call(0, vals.size - 1)
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer

/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def balanceBST(root: TreeNode): TreeNode = {
    val vals = ListBuffer[Int]()

    def inorder(node: TreeNode): Unit = {
      if (node == null) return
      inorder(node.left)
      vals += node.value
      inorder(node.right)
    }

    inorder(root)

    def build(l: Int, r: Int): TreeNode = {
      if (l > r) return null
      val mid = l + (r - l) / 2
      val node = new TreeNode(vals(mid))
      node.left = build(l, mid - 1)
      node.right = build(mid + 1, r)
      node
    }

    build(0, vals.length - 1)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, vals: &mut Vec<i32>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                inorder(&n.left, vals);
                vals.push(n.val);
                inorder(&n.right, vals);
            }
        }

        fn build(vals: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if vals.is_empty() {
                return None;
            }
            let mid = vals.len() / 2;
            let node = Rc::new(RefCell::new(TreeNode::new(vals[mid])));
            node.borrow_mut().left = build(&vals[..mid]);
            node.borrow_mut().right = build(&vals[mid + 1..]);
            Some(node)
        }

        let mut vals = Vec::new();
        inorder(&root, &mut vals);
        build(&vals)
    }
}
```

## Racket

```racket
#lang racket

; Definition for a binary tree node.
#|
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(require racket/list)

;; Helper: collect BST values in sorted order using reverse inorder traversal.
(: inorder-collect (-> (or/c tree-node? #f) (listof integer?) (listof integer?)))
(define (inorder-collect node acc)
  (if (not node)
      acc
      (let ((acc1 (inorder-collect (tree-node-right node) acc))
            (acc2 (cons (tree-node-val node) acc1)))
        (inorder-collect (tree-node-left node) acc2))))

;; Helper: build a balanced BST from a sorted vector of values.
(: build-balanced (-> (vectorof integer?) Integer Integer (or/c tree-node? #f)))
(define (build-balanced vec l r)
  (if (>= l r)
      #f
      (let* ((mid (+ l (quotient (- r l) 2)))
             (node (make-tree-node (vector-ref vec mid))))
        (set-tree-node-left! node (build-balanced vec l mid))
        (set-tree-node-right! node (build-balanced vec (add1 mid) r))
        node)))

;; Main function
(define/contract (balance-bst root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (let* ((vals (inorder-collect root '()))
         (vec (list->vector vals)))
    (build-balanced vec 0 (vector-length vec))))
```

## Erlang

```erlang
-module(solution).
-export([balance_bst/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec balance_bst(Root :: #tree_node{} | null) -> #tree_node{} | null.
balance_bst(Root) ->
    Values = inorder(Root),
    N = length(Values),
    {Tree, _} = build_balanced(N, Values),
    Tree.

inorder(null) ->
    [];
inorder(#tree_node{left = L, right = R, val = V}) ->
    inorder(L) ++ [V] ++ inorder(R).

build_balanced(0, List) ->
    {null, List};
build_balanced(N, List) when N > 0 ->
    LeftSize = N div 2,
    RightSize = N - LeftSize - 1,
    {LeftTree, [RootVal | Rest1]} = build_balanced(LeftSize, List),
    {RightTree, Rest2} = build_balanced(RightSize, Rest1),
    {#tree_node{val = RootVal, left = LeftTree, right = RightTree}, Rest2}.
```

## Elixir

```elixir
defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec balance_bst(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def balance_bst(root) do
    vals = inorder(root, []) |> Enum.reverse()
    {tree, _} = build_balanced(vals, length(vals))
    tree
  end

  defp inorder(nil, acc), do: acc

  defp inorder(%TreeNode{val: v, left: l, right: r}, acc) do
    acc = inorder(l, acc)
    acc = [v | acc]
    inorder(r, acc)
  end

  defp build_balanced(list, 0), do: {nil, list}

  defp build_balanced(list, n) when n > 0 do
    left_n = div(n, 2)
    {left_tree, rest1} = build_balanced(list, left_n)

    [root_val | rest2] = rest1

    right_n = n - left_n - 1
    {right_tree, rest3} = build_balanced(rest2, right_n)

    {%TreeNode{val: root_val, left: left_tree, right: right_tree}, rest3}
  end
end
```
