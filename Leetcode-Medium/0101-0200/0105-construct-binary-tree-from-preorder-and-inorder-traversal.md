# 0105. Construct Binary Tree from Preorder and Inorder Traversal

## Cpp

```cpp
#include <unordered_map>
using namespace std;

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int,int> pos;
        for (int i = 0; i < (int)inorder.size(); ++i) pos[inorder[i]] = i;
        int preIdx = 0;
        function<TreeNode*(int,int)> dfs = [&](int l, int r) -> TreeNode* {
            if (l > r) return nullptr;
            int val = preorder[preIdx++];
            TreeNode* node = new TreeNode(val);
            int idx = pos[val];
            node->left = dfs(l, idx - 1);
            node->right = dfs(idx + 1, r);
            return node;
        };
        return dfs(0, (int)inorder.size() - 1);
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
    private int[] preorder;
    private int preIdx;
    private java.util.Map<Integer, Integer> inorderIndexMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length != inorder.length) {
            return null;
        }
        this.preorder = preorder;
        this.preIdx = 0;
        this.inorderIndexMap = new java.util.HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        return buildSubTree(0, inorder.length - 1);
    }

    private TreeNode buildSubTree(int leftInorderIdx, int rightInorderIdx) {
        if (leftInorderIdx > rightInorderIdx) {
            return null;
        }
        int rootVal = preorder[preIdx++];
        TreeNode root = new TreeNode(rootVal);
        int inorderRootIdx = inorderIndexMap.get(rootVal);
        root.left = buildSubTree(leftInorderIdx, inorderRootIdx - 1);
        root.right = buildSubTree(inorderRootIdx + 1, rightInorderIdx);
        return root;
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            inorder_index = idx_map[root_val]
            root.left = helper(left, inorder_index - 1)
            root.right = helper(inorder_index + 1, right)
            return root

        return helper(0, len(inorder) - 1)
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)

            # Build left and right subtrees
            root.left = array_to_tree(left, idx_map[root_val] - 1)
            root.right = array_to_tree(idx_map[root_val] + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define OFFSET 3000
static int idxMap[6001];

static struct TreeNode* build(int* preorder, int preStart, int inStart, int len) {
    if (len == 0) return NULL;
    
    int rootVal = preorder[preStart];
    int inRootIdx = idxMap[rootVal + OFFSET];
    int leftLen = inRootIdx - inStart;
    int rightLen = len - leftLen - 1;
    
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = rootVal;
    node->left = build(preorder, preStart + 1, inStart, leftLen);
    node->right = build(preorder, preStart + 1 + leftLen, inRootIdx + 1, rightLen);
    return node;
}

struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    memset(idxMap, -1, sizeof(idxMap));
    for (int i = 0; i < inorderSize; ++i) {
        idxMap[inorder[i] + OFFSET] = i;
    }
    return build(preorder, 0, 0, preorderSize);
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
    private Dictionary<int, int> inorderIndex;
    private int[] preorderArr;
    private int[] inorderArr;

    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        preorderArr = preorder;
        inorderArr = inorder;
        inorderIndex = new Dictionary<int, int>(inorder.Length);
        for (int i = 0; i < inorder.Length; i++) {
            inorderIndex[inorder[i]] = i;
        }
        return Build(0, preorder.Length - 1, 0, inorder.Length - 1);
    }

    private TreeNode Build(int preStart, int preEnd, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) {
            return null;
        }
        int rootVal = preorderArr[preStart];
        TreeNode root = new TreeNode(rootVal);
        int idxInorder = inorderIndex[rootVal];
        int leftSize = idxInorder - inStart;

        root.left = Build(preStart + 1, preStart + leftSize, inStart, idxInorder - 1);
        root.right = Build(preStart + leftSize + 1, preEnd, idxInorder + 1, inEnd);

        return root;
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    const idxMap = new Map();
    for (let i = 0; i < inorder.length; i++) {
        idxMap.set(inorder[i], i);
    }
    let preIdx = 0;
    function helper(left, right) {
        if (left > right) return null;
        const rootVal = preorder[preIdx++];
        const root = new TreeNode(rootVal);
        const inorderIdx = idxMap.get(rootVal);
        root.left = helper(left, inorderIdx - 1);
        root.right = helper(inorderIdx + 1, right);
        return root;
    }
    return helper(0, inorder.length - 1);
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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (!preorder.length || !inorder.length) return null;

    const idxMap = new Map<number, number>();
    for (let i = 0; i < inorder.length; i++) {
        idxMap.set(inorder[i], i);
    }

    let preIdx = 0;

    function helper(left: number, right: number): TreeNode | null {
        if (left > right) return null;

        const rootVal = preorder[preIdx++];
        const root = new TreeNode(rootVal);

        const inorderIndex = idxMap.get(rootVal)!;
        root.left = helper(left, inorderIndex - 1);
        root.right = helper(inorderIndex + 1, right);

        return root;
    }

    return helper(0, inorder.length - 1);
}
```

## Php

```php
/ **
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
     * @param Integer[] $preorder
     * @param Integer[] $inorder
     * @return TreeNode
     */
    function buildTree($preorder, $inorder) {
        $n = count($inorder);
        if ($n == 0) return null;

        // map value to its index in inorder array for O(1) lookups
        $idxMap = [];
        foreach ($inorder as $i => $val) {
            $idxMap[$val] = $i;
        }

        $preIdx = 0;

        $build = function($left, $right) use (&$preorder, &$idxMap, &$preIdx, &$build) {
            if ($left > $right) {
                return null;
            }

            // root value from preorder traversal
            $rootVal = $preorder[$preIdx++];
            $root = new TreeNode($rootVal);

            // split inorder array
            $inRootIdx = $idxMap[$rootVal];

            // recursively build left and right subtrees
            $root->left  = $build($left, $inRootIdx - 1);
            $root->right = $build($inRootIdx + 1, $right);

            return $root;
        };

        return $build(0, $n - 1);
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
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        var indexMap = [Int:Int]()
        for (i, v) in inorder.enumerated() {
            indexMap[v] = i
        }
        var preIdx = 0
        
        func helper(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right { return nil }
            let rootVal = preorder[preIdx]
            preIdx += 1
            let node = TreeNode(rootVal)
            let inorderIdx = indexMap[rootVal]!
            node.left = helper(left, inorderIdx - 1)
            node.right = helper(inorderIdx + 1, right)
            return node
        }
        
        return helper(0, inorder.count - 1)
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
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        if (preorder.isEmpty()) return null
        val indexMap = HashMap<Int, Int>()
        for (i in inorder.indices) {
            indexMap[inorder[i]] = i
        }
        var preIdx = 0
        fun helper(inLeft: Int, inRight: Int): TreeNode? {
            if (inLeft > inRight) return null
            val rootVal = preorder[preIdx++]
            val root = TreeNode(rootVal)
            val inorderRootIndex = indexMap[rootVal]!!
            root.left = helper(inLeft, inorderRootIndex - 1)
            root.right = helper(inorderRootIndex + 1, inRight)
            return root
        }
        return helper(0, inorder.size - 1)
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
  int _preIdx = 0;
  late Map<int, int> _inMap;

  TreeNode? buildTree(List<int> preorder, List<int> inorder) {
    _preIdx = 0;
    _inMap = {for (int i = 0; i < inorder.length; i++) inorder[i]: i};
    return _build(preorder, 0, inorder.length - 1);
  }

  TreeNode? _build(List<int> preorder, int left, int right) {
    if (left > right) return null;
    int rootVal = preorder[_preIdx++];
    TreeNode node = TreeNode(rootVal);
    int idx = _inMap[rootVal]!;
    node.left = _build(preorder, left, idx - 1);
    node.right = _build(preorder, idx + 1, right);
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
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	idxMap := make(map[int]int, len(inorder))
	for i, v := range inorder {
		idxMap[v] = i
	}
	var helper func(pStart, pEnd, iStart, iEnd int) *TreeNode
	helper = func(pStart, pEnd, iStart, iEnd int) *TreeNode {
		if pStart > pEnd || iStart > iEnd {
			return nil
		}
		rootVal := preorder[pStart]
		inIdx := idxMap[rootVal]
		leftSize := inIdx - iStart

		node := &TreeNode{Val: rootVal}
		node.Left = helper(pStart+1, pStart+leftSize, iStart, inIdx-1)
		node.Right = helper(pStart+leftSize+1, pEnd, inIdx+1, iEnd)
		return node
	}
	return helper(0, len(preorder)-1, 0, len(inorder)-1)
}
```

## Ruby

```ruby
def build_tree(preorder, inorder)
  index_map = {}
  inorder.each_with_index { |val, i| index_map[val] = i }
  pre_idx = 0

  construct = lambda do |left, right|
    return nil if left > right
    root_val = preorder[pre_idx]
    pre_idx += 1
    root = TreeNode.new(root_val)
    inorder_idx = index_map[root_val]

    root.left = construct.call(left, inorder_idx - 1)
    root.right = construct.call(inorder_idx + 1, right)

    root
  end

  construct.call(0, inorder.length - 1)
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
  def buildTree(preorder: Array[Int], inorder: Array[Int]): TreeNode = {
    import scala.collection.mutable

    val idxMap = mutable.Map[Int, Int]()
    for (i <- inorder.indices) idxMap(inorder(i)) = i

    var preIdx = 0
    def helper(left: Int, right: Int): TreeNode = {
      if (left > right) return null
      val rootVal = preorder(preIdx)
      preIdx += 1
      val root = new TreeNode(rootVal)
      val inorderIdx = idxMap(rootVal)
      root.left = helper(left, inorderIdx - 1)
      root.right = helper(inorderIdx + 1, right)
      root
    }

    if (preorder.isEmpty) null else helper(0, inorder.length - 1)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

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

impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.is_empty() {
            return None;
        }
        let mut idx_map = HashMap::new();
        for (i, &v) in inorder.iter().enumerate() {
            idx_map.insert(v, i);
        }
        fn helper(
            left: i32,
            right: i32,
            preorder: &Vec<i32>,
            idx_map: &HashMap<i32, usize>,
            pre_idx: &mut usize,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if left > right {
                return None;
            }
            let root_val = preorder[*pre_idx];
            *pre_idx += 1;
            let node = Rc::new(RefCell::new(TreeNode::new(root_val)));
            let inorder_idx = idx_map[&root_val] as i32;
            let left_child = helper(left, inorder_idx - 1, preorder, idx_map, pre_idx);
            let right_child = helper(inorder_idx + 1, right, preorder, idx_map, pre_idx);
            {
                let mut n = node.borrow_mut();
                n.left = left_child;
                n.right = right_child;
            }
            Some(node)
        }

        let mut pre_idx = 0usize;
        helper(0, inorder.len() as i32 - 1, &preorder, &idx_map, &mut pre_idx)
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

(define/contract (build-tree preorder inorder)
  (-> (listof exact-integer?) (listof exact-integer?) (or/c tree-node? #f))
  (let* ((n (length preorder))
         (pre-vec (list->vector preorder))
         (in-vec (list->vector inorder))
         (idx-map (make-hash)))
    (for ([i (in-range n)])
      (hash-set! idx-map (vector-ref in-vec i) i))
    (define (helper preL preR inL inR)
      (if (> preL preR)
          #f
          (let* ((root-val (vector-ref pre-vec preL))
                 (inIdx (hash-ref idx-map root-val))
                 (leftSize (- inIdx inL))
                 (node (make-tree-node root-val)))
            (set-tree-node-left! node (helper (+ preL 1) (+ preL leftSize) inL (- inIdx 1)))
            (set-tree-node-right! node (helper (+ preL leftSize 1) preR (+ inIdx 1) inR))
            node)))
    (if (= n 0)
        #f
        (helper 0 (- n 1) 0 (- n 1)))))
```

## Erlang

```erlang
-module(solution).
-export([build_tree/2]).

-record(tree_node, {
    val = 0 :: integer(),
    left = null :: 'null' | #tree_node{},
    right = null :: 'null' | #tree_node{}
}).

-spec build_tree(Preorder :: [integer()], Inorder :: [integer()]) -> #tree_node{} | null.
build_tree(Preorder, Inorder) ->
    IndexMap = maps:from_list(lists:zip(Inorder, lists:seq(0, length(Inorder) - 1))),
    {Tree, _} = build(Preorder, 0, length(Inorder) - 1, IndexMap),
    Tree.

build(PreList, InStart, InEnd, _) when InStart > InEnd ->
    {null, PreList};
build([], _, _, _) ->
    {null, []};
build([RootVal | RestPre], InStart, InEnd, IndexMap) ->
    Pos = maps:get(RootVal, IndexMap),
    {LeftTree, AfterLeft} = build(RestPre, InStart, Pos - 1, IndexMap),
    {RightTree, AfterRight} = build(AfterLeft, Pos + 1, InEnd, IndexMap),
    Node = #tree_node{val = RootVal, left = LeftTree, right = RightTree},
    {Node, AfterRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec build_tree(preorder :: [integer], inorder :: [integer]) :: TreeNode.t() | nil
  def build_tree(preorder, inorder) do
    index_map = Enum.with_index(inorder) |> Map.new(fn {val, idx} -> {val, idx} end)
    pre_tuple = List.to_tuple(preorder)
    build(pre_tuple, 0, tuple_size(pre_tuple), 0, length(inorder), index_map)
  end

  defp build(_pre, pre_start, pre_end, _in_start, _in_end, _map) when pre_start >= pre_end,
    do: nil

  defp build(pre, pre_start, pre_end, in_start, in_end, map) do
    root_val = elem(pre, pre_start)
    root_idx_inorder = Map.fetch!(map, root_val)
    left_size = root_idx_inorder - in_start

    left =
      build(
        pre,
        pre_start + 1,
        pre_start + 1 + left_size,
        in_start,
        root_idx_inorder,
        map
      )

    right =
      build(
        pre,
        pre_start + 1 + left_size,
        pre_end,
        root_idx_inorder + 1,
        in_end,
        map
      )

    %TreeNode{val: root_val, left: left, right: right}
  end
end
```
