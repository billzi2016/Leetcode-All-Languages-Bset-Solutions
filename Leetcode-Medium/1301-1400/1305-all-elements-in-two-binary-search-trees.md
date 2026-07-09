# 1305. All Elements in Two Binary Search Trees

## Cpp

```cpp
/ **
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
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> a, b;
        inorder(root1, a);
        inorder(root2, b);
        vector<int> res;
        res.reserve(a.size() + b.size());
        size_t i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a[i] <= b[j]) res.push_back(a[i++]);
            else res.push_back(b[j++]);
        }
        while (i < a.size()) res.push_back(a[i++]);
        while (j < b.size()) res.push_back(b[j++]);
        return res;
    }
private:
    void inorder(TreeNode* node, vector<int>& vec) {
        if (!node) return;
        inorder(node->left, vec);
        vec.push_back(node->val);
        inorder(node->right, vec);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        inorder(root1, list1);
        inorder(root2, list2);
        
        List<Integer> merged = new ArrayList<>(list1.size() + list2.size());
        int i = 0, j = 0;
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) <= list2.get(j)) {
                merged.add(list1.get(i++));
            } else {
                merged.add(list2.get(j++));
            }
        }
        while (i < list1.size()) {
            merged.add(list1.get(i++));
        }
        while (j < list2.size()) {
            merged.add(list2.get(j++));
        }
        return merged;
    }
    
    private void inorder(TreeNode node, List<Integer> list) {
        if (node == null) return;
        inorder(node.left, list);
        list.add(node.val);
        inorder(node.right, list);
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
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder(root):
            res, stack = [], []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                node = stack.pop()
                res.append(node.val)
                root = node.right
            return res

        list1 = inorder(root1) if root1 else []
        list2 = inorder(root2) if root2 else []

        # Merge two sorted lists
        i, j = 0, 0
        merged = []
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        if i < len(list1):
            merged.extend(list1[i:])
        if j < len(list2):
            merged.extend(list2[j:])

        return merged
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def getAllElements(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> List[int]:
        def inorder(root: Optional['TreeNode']):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                node = stack.pop()
                yield node.val
                root = node.right

        gen1, gen2 = inorder(root1), inorder(root2)
        val1 = next(gen1, None)
        val2 = next(gen2, None)

        merged: List[int] = []
        while val1 is not None or val2 is not None:
            if val2 is None or (val1 is not None and val1 <= val2):
                merged.append(val1)  # type: ignore
                val1 = next(gen1, None)
            else:
                merged.append(val2)  # type: ignore
                val2 = next(gen2, None)

        return merged
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
#include <stdlib.h>

static int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

static void inorderFill(struct TreeNode* root, int *arr, int *idx) {
    if (!root) return;
    inorderFill(root->left, arr, idx);
    arr[(*idx)++] = root->val;
    inorderFill(root->right, arr, idx);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize){
    int n1 = countNodes(root1);
    int n2 = countNodes(root2);
    int total = n1 + n2;
    *returnSize = total;

    int *arr1 = NULL, *arr2 = NULL;
    if (n1 > 0) arr1 = (int*)malloc(sizeof(int) * n1);
    if (n2 > 0) arr2 = (int*)malloc(sizeof(int) * n2);

    int idx = 0;
    if (n1 > 0) inorderFill(root1, arr1, &idx);
    idx = 0;
    if (n2 > 0) inorderFill(root2, arr2, &idx);

    int *res = (int*)malloc(sizeof(int) * total);
    int i = 0, j = 0, k = 0;
    while (i < n1 && j < n2) {
        if (arr1[i] <= arr2[j]) res[k++] = arr1[i++];
        else res[k++] = arr2[j++];
    }
    while (i < n1) res[k++] = arr1[i++];
    while (j < n2) res[k++] = arr2[j++];

    if (arr1) free(arr1);
    if (arr2) free(arr2);
    return res;
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
    public IList<int> GetAllElements(TreeNode root1, TreeNode root2) {
        var list1 = new List<int>();
        var list2 = new List<int>();
        Inorder(root1, list1);
        Inorder(root2, list2);

        var merged = new List<int>(list1.Count + list2.Count);
        int i = 0, j = 0;
        while (i < list1.Count && j < list2.Count) {
            if (list1[i] < list2[j]) {
                merged.Add(list1[i++]);
            } else {
                merged.Add(list2[j++]);
            }
        }
        while (i < list1.Count) merged.Add(list1[i++]);
        while (j < list2.Count) merged.Add(list2[j++]);

        return merged;
    }

    private void Inorder(TreeNode node, List<int> result) {
        if (node == null) return;
        Inorder(node.left, result);
        result.Add(node.val);
        Inorder(node.right, result);
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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function(root1, root2) {
    const inorder = (node, arr) => {
        if (!node) return;
        inorder(node.left, arr);
        arr.push(node.val);
        inorder(node.right, arr);
    };
    
    const list1 = [];
    const list2 = [];
    inorder(root1, list1);
    inorder(root2, list2);
    
    const merged = [];
    let i = 0, j = 0;
    while (i < list1.length && j < list2.length) {
        if (list1[i] <= list2[j]) {
            merged.push(list1[i++]);
        } else {
            merged.push(list2[j++]);
        }
    }
    while (i < list1.length) merged.push(list1[i++]);
    while (j < list2.length) merged.push(list2[j++]);
    
    return merged;
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

function getAllElements(root1: TreeNode | null, root2: TreeNode | null): number[] {
    const list1: number[] = [];
    const list2: number[] = [];

    const inorder = (node: TreeNode | null, arr: number[]): void => {
        if (!node) return;
        inorder(node.left, arr);
        arr.push(node.val);
        inorder(node.right, arr);
    };

    inorder(root1, list1);
    inorder(root2, list2);

    const merged: number[] = [];
    let i = 0, j = 0;
    while (i < list1.length && j < list2.length) {
        if (list1[i] <= list2[j]) {
            merged.push(list1[i++]);
        } else {
            merged.push(list2[j++]);
        }
    }
    while (i < list1.length) merged.push(list1[i++]);
    while (j < list2.length) merged.push(list2[j++]);

    return merged;
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
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Integer[]
     */
    function getAllElements($root1, $root2) {
        $list1 = [];
        $list2 = [];
        $this->inorder($root1, $list1);
        $this->inorder($root2, $list2);

        $i = 0;
        $j = 0;
        $merged = [];

        $n1 = count($list1);
        $n2 = count($list2);

        while ($i < $n1 && $j < $n2) {
            if ($list1[$i] <= $list2[$j]) {
                $merged[] = $list1[$i];
                $i++;
            } else {
                $merged[] = $list2[$j];
                $j++;
            }
        }

        while ($i < $n1) {
            $merged[] = $list1[$i++];
        }
        while ($j < $n2) {
            $merged[] = $list2[$j++];
        }

        return $merged;
    }

    private function inorder($node, &$arr) {
        if ($node === null) {
            return;
        }
        $this->inorder($node->left, $arr);
        $arr[] = $node->val;
        $this->inorder($node->right, $arr);
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
    func getAllElements(_ root1: TreeNode?, _ root2: TreeNode?) -> [Int] {
        var list1 = [Int]()
        var list2 = [Int]()
        inorder(root1, &list1)
        inorder(root2, &list2)
        return merge(list1, list2)
    }
    
    private func inorder(_ node: TreeNode?, _ result: inout [Int]) {
        guard let n = node else { return }
        inorder(n.left, &result)
        result.append(n.val)
        inorder(n.right, &result)
    }
    
    private func merge(_ a: [Int], _ b: [Int]) -> [Int] {
        var i = 0, j = 0
        var merged = [Int]()
        merged.reserveCapacity(a.count + b.count)
        while i < a.count && j < b.count {
            if a[i] <= b[j] {
                merged.append(a[i])
                i += 1
            } else {
                merged.append(b[j])
                j += 1
            }
        }
        while i < a.count {
            merged.append(a[i])
            i += 1
        }
        while j < b.count {
            merged.append(b[j])
            j += 1
        }
        return merged
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
    fun getAllElements(root1: TreeNode?, root2: TreeNode?): List<Int> {
        val list1 = mutableListOf<Int>()
        val list2 = mutableListOf<Int>()
        inorder(root1, list1)
        inorder(root2, list2)

        val merged = mutableListOf<Int>()
        var i = 0
        var j = 0
        while (i < list1.size && j < list2.size) {
            if (list1[i] <= list2[j]) {
                merged.add(list1[i])
                i++
            } else {
                merged.add(list2[j])
                j++
            }
        }
        while (i < list1.size) {
            merged.add(list1[i])
            i++
        }
        while (j < list2.size) {
            merged.add(list2[j])
            j++
        }
        return merged
    }

    private fun inorder(node: TreeNode?, list: MutableList<Int>) {
        if (node == null) return
        inorder(node.left, list)
        list.add(node.`val`)
        inorder(node.right, list)
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
  List<int> getAllElements(TreeNode? root1, TreeNode? root2) {
    final List<int> list1 = [];
    final List<int> list2 = [];

    void inorder(TreeNode? node, List<int> out) {
      if (node == null) return;
      inorder(node.left, out);
      out.add(node.val);
      inorder(node.right, out);
    }

    inorder(root1, list1);
    inorder(root2, list2);

    final List<int> merged = [];
    int i = 0, j = 0;
    while (i < list1.length && j < list2.length) {
      if (list1[i] <= list2[j]) {
        merged.add(list1[i]);
        i++;
      } else {
        merged.add(list2[j]);
        j++;
      }
    }
    while (i < list1.length) {
      merged.add(list1[i]);
      i++;
    }
    while (j < list2.length) {
      merged.add(list2[j]);
      j++;
    }

    return merged;
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
func inorder(node *TreeNode, out *[]int) {
    if node == nil {
        return
    }
    inorder(node.Left, out)
    *out = append(*out, node.Val)
    inorder(node.Right, out)
}

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
    var list1, list2 []int
    inorder(root1, &list1)
    inorder(root2, &list2)

    merged := make([]int, 0, len(list1)+len(list2))
    i, j := 0, 0
    for i < len(list1) && j < len(list2) {
        if list1[i] <= list2[j] {
            merged = append(merged, list1[i])
            i++
        } else {
            merged = append(merged, list2[j])
            j++
        }
    }
    for i < len(list1) {
        merged = append(merged, list1[i])
        i++
    }
    for j < len(list2) {
        merged = append(merged, list2[j])
        j++
    }
    return merged
}
```

## Ruby

```ruby
def get_all_elements(root1, root2)
  list1 = []
  list2 = []

  inorder = lambda do |node, arr|
    return if node.nil?
    inorder.call(node.left, arr)
    arr << node.val
    inorder.call(node.right, arr)
  end

  inorder.call(root1, list1)
  inorder.call(root2, list2)

  merged = []
  i = 0
  j = 0
  while i < list1.size && j < list2.size
    if list1[i] <= list2[j]
      merged << list1[i]
      i += 1
    else
      merged << list2[j]
      j += 1
    end
  end

  while i < list1.size
    merged << list1[i]
    i += 1
  end

  while j < list2.size
    merged << list2[j]
    j += 1
  end

  merged
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
  import scala.collection.mutable.ListBuffer

  private def inorder(node: TreeNode, buf: ListBuffer[Int]): Unit = {
    if (node != null) {
      inorder(node.left, buf)
      buf += node.value
      inorder(node.right, buf)
    }
  }

  def getAllElements(root1: TreeNode, root2: TreeNode): List[Int] = {
    val list1 = ListBuffer.empty[Int]
    val list2 = ListBuffer.empty[Int]

    inorder(root1, list1)
    inorder(root2, list2)

    val merged = ListBuffer.empty[Int]
    var i = 0
    var j = 0

    while (i < list1.size && j < list2.size) {
      if (list1(i) <= list2(j)) {
        merged += list1(i)
        i += 1
      } else {
        merged += list2(j)
        j += 1
      }
    }

    while (i < list1.size) {
      merged += list1(i)
      i += 1
    }
    while (j < list2.size) {
      merged += list2(j)
      j += 1
    }

    merged.toList
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn get_all_elements(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn inorder(root: &Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
            let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
            let mut cur = root.clone();
            while cur.is_some() || !stack.is_empty() {
                while let Some(node_rc) = cur {
                    stack.push(node_rc.clone());
                    cur = node_rc.borrow().left.clone();
                }
                if let Some(node_rc) = stack.pop() {
                    out.push(node_rc.borrow().val);
                    cur = node_rc.borrow().right.clone();
                }
            }
        }

        let mut v1 = Vec::new();
        inorder(&root1, &mut v1);
        let mut v2 = Vec::new();
        inorder(&root2, &mut v2);

        let mut i = 0;
        let mut j = 0;
        let mut res = Vec::with_capacity(v1.len() + v2.len());
        while i < v1.len() && j < v2.len() {
            if v1[i] <= v2[j] {
                res.push(v1[i]);
                i += 1;
            } else {
                res.push(v2[j]);
                j += 1;
            }
        }
        if i < v1.len() {
            res.extend_from_slice(&v1[i..]);
        }
        if j < v2.len() {
            res.extend_from_slice(&v2[j..]);
        }
        res
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

(define/contract (get-all-elements root1 root2)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) (listof exact-integer?))
  (letrec
      ([inorder
        (lambda (node)
          (if (not node)
              '()
              (append (inorder (tree-node-left node))
                      (list (tree-node-val node))
                      (inorder (tree-node-right node)))))]

       [merge
        (lambda (l1 l2)
          (cond [(null? l1) l2]
                [(null? l2) l1]
                [else (let ([h1 (car l1)] [h2 (car l2)])
                        (if (<= h1 h2)
                            (cons h1 (merge (cdr l1) l2))
                            (cons h2 (merge l1 (cdr l2))))))])])
    (merge (inorder root1) (inorder root2))))
```

## Erlang

```erlang
-module(solution).
-export([get_all_elements/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec get_all_elements(Root1 :: #tree_node{} | null, Root2 :: #tree_node{} | null) -> [integer()].
get_all_elements(Root1, Root2) ->
    List1 = inorder(Root1),
    List2 = inorder(Root2),
    merge(List1, List2).

%% In-order traversal producing a sorted list
inorder(null) ->
    [];
inorder(#tree_node{val = V, left = L, right = R}) ->
    inorder(L) ++ [V] ++ inorder(R).

%% Merge two sorted lists
merge([], L) -> L;
merge(L, []) -> L;
merge([H1|T1]=L1, [H2|T2]=L2) when H1 =< H2 ->
    [H1 | merge(T1, L2)];
merge([_H1|_T1]=L1, [_H2|_T2]=L2) ->
    [H2 | merge(L1, T2)]
    where
        H2 = hd(L2).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_all_elements(root1 :: TreeNode.t | nil, root2 :: TreeNode.t | nil) :: [integer]
  def get_all_elements(root1, root2) do
    list1 = inorder(root1)
    list2 = inorder(root2)
    merge(list1, list2)
  end

  defp inorder(nil), do: []
  defp inorder(node) do
    inorder_rev(node, [])
  end

  defp inorder_rev(nil, acc), do: acc
  defp inorder_rev(%TreeNode{val: v, left: l, right: r}, acc) do
    acc = inorder_rev(r, acc)
    acc = [v | acc]
    inorder_rev(l, acc)
  end

  defp merge([], b), do: b
  defp merge(a, []), do: a
  defp merge([h1 | t1] = a, [h2 | _] = b) when h1 <= h2 do
    [h1 | merge(t1, b)]
  end
  defp merge(a, [h2 | t2]) do
    [h2 | merge(a, t2)]
  end
end
```
