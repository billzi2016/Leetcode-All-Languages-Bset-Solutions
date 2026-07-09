# 0106. Construct Binary Tree from Inorder and Postorder Traversal

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
    TreeNode* buildTree(std::vector<int>& inorder, std::vector<int>& postorder) {
        if (inorder.empty()) return nullptr;
        unordered_map<int,int> pos;
        for (int i = 0; i < (int)inorder.size(); ++i) pos[inorder[i]] = i;
        return build(inorder, 0, inorder.size() - 1,
                     postorder, 0, postorder.size() - 1, pos);
    }
private:
    TreeNode* build(const std::vector<int>& inorder, int inL, int inR,
                    const std::vector<int>& postorder, int postL, int postR,
                    const unordered_map<int,int>& pos) {
        if (inL > inR || postL > postR) return nullptr;
        int rootVal = postorder[postR];
        TreeNode* node = new TreeNode(rootVal);
        int idx = pos.at(rootVal);
        int leftSize = idx - inL;
        node->left  = build(inorder, inL, idx - 1,
                            postorder, postL, postL + leftSize - 1, pos);
        node->right = build(inorder, idx + 1, inR,
                            postorder, postL + leftSize, postR - 1, pos);
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
    private Map<Integer, Integer> inorderIndexMap;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        return build(0, inorder.length - 1, 0, postorder.length - 1, inorder, postorder);
    }

    private TreeNode build(int inStart, int inEnd,
                           int postStart, int postEnd,
                           int[] inorder, int[] postorder) {
        if (inStart > inEnd || postStart > postEnd) {
            return null;
        }
        int rootVal = postorder[postEnd];
        TreeNode root = new TreeNode(rootVal);
        int inorderRootIdx = inorderIndexMap.get(rootVal);
        int leftSize = inorderRootIdx - inStart;

        root.left = build(inStart, inorderRootIdx - 1,
                          postStart, postStart + leftSize - 1,
                          inorder, postorder);
        root.right = build(inorderRootIdx + 1, inEnd,
                           postStart + leftSize, postEnd - 1,
                           inorder, postorder);
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            index = idx_map[root_val]
            # Build right subtree first because we are consuming postorder from the end
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root

        return helper(0, len(inorder) - 1)
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int, post_left: int, post_right: int) -> Optional[TreeNode]:
            if in_left > in_right or post_left > post_right:
                return None
            
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            inorder_root_idx = idx_map[root_val]
            left_tree_size = inorder_root_idx - in_left
            
            root.left = helper(in_left, inorder_root_idx - 1,
                               post_left, post_left + left_tree_size - 1)
            root.right = helper(inorder_root_idx + 1, in_right,
                                post_left + left_tree_size, post_right - 1)
            return root
        
        n = len(inorder)
        return helper(0, n - 1, 0, n - 1)
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

static struct TreeNode* build(int inStart, int inEnd,
                              int postStart, int postEnd,
                              const int *inorder, const int *postorder) {
    if (inStart > inEnd || postStart > postEnd) return NULL;
    
    int rootVal = postorder[postEnd];
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = rootVal;
    node->left = node->right = NULL;
    
    int idx = idxMap[rootVal + OFFSET];
    int leftSize = idx - inStart;
    
    node->left = build(inStart, idx - 1,
                       postStart, postStart + leftSize - 1,
                       inorder, postorder);
    node->right = build(idx + 1, inEnd,
                        postStart + leftSize, postEnd - 1,
                        inorder, postorder);
    return node;
}

struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    memset(idxMap, -1, sizeof(idxMap));
    for (int i = 0; i < inorderSize; ++i) {
        idxMap[inorder[i] + OFFSET] = i;
    }
    return build(0, inorderSize - 1, 0, postorderSize - 1, inorder, postorder);
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
public class Solution {
    private Dictionary<int, int> inorderIndex;
    private int[] postorder;

    public TreeNode BuildTree(int[] inorder, int[] postorder) {
        inorderIndex = new Dictionary<int, int>(inorder.Length);
        for (int i = 0; i < inorder.Length; i++) {
            inorderIndex[inorder[i]] = i;
        }
        this.postorder = postorder;
        return Build(0, inorder.Length - 1, 0, postorder.Length - 1);
    }

    private TreeNode Build(int inLeft, int inRight, int postLeft, int postRight) {
        if (inLeft > inRight || postLeft > postRight) {
            return null;
        }

        int rootVal = postorder[postRight];
        TreeNode root = new TreeNode(rootVal);

        int idx = inorderIndex[rootVal];
        int leftSize = idx - inLeft;

        root.left = Build(inLeft, idx - 1, postLeft, postLeft + leftSize - 1);
        root.right = Build(idx + 1, inRight, postLeft + leftSize, postRight - 1);

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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    const idxMap = new Map();
    for (let i = 0; i < inorder.length; i++) {
        idxMap.set(inorder[i], i);
    }

    function helper(inLeft, inRight, postLeft, postRight) {
        if (inLeft > inRight) return null;
        const rootVal = postorder[postRight];
        const root = new TreeNode(rootVal);
        const inorderRootIdx = idxMap.get(rootVal);
        const leftSize = inorderRootIdx - inLeft;

        root.left = helper(inLeft, inorderRootIdx - 1, postLeft, postLeft + leftSize - 1);
        root.right = helper(inorderRootIdx + 1, inRight, postLeft + leftSize, postRight - 1);
        return root;
    }

    return helper(0, inorder.length - 1, 0, postorder.length - 1);
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

function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    const n = inorder.length;
    if (n === 0) return null;

    const idxMap = new Map<number, number>();
    for (let i = 0; i < n; i++) {
        idxMap.set(inorder[i], i);
    }

    let postIdx = n - 1;

    function helper(left: number, right: number): TreeNode | null {
        if (left > right) return null;
        const rootVal = postorder[postIdx--];
        const root = new TreeNode(rootVal);
        const inorderIdx = idxMap.get(rootVal)!;
        // Build right subtree first because we are consuming postorder from the end
        root.right = helper(inorderIdx + 1, right);
        root.left = helper(left, inorderIdx - 1);
        return root;
    }

    return helper(0, n - 1);
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
     * @param Integer[] $inorder
     * @param Integer[] $postorder
     * @return TreeNode|null
     */
    function buildTree($inorder, $postorder) {
        $n = count($inorder);
        if ($n == 0) return null;

        // map value to its index in inorder for O(1) lookup
        $idxMap = [];
        foreach ($inorder as $i => $val) {
            $idxMap[$val] = $i;
        }

        // recursive builder using closure
        $build = function($inLeft, $inRight, &$postIdx) use (&$build, $postorder, $idxMap) {
            if ($inLeft > $inRight) {
                return null;
            }
            $rootVal = $postorder[$postIdx];
            $postIdx--;

            $node = new TreeNode($rootVal);
            $index = $idxMap[$rootVal];

            // Build right subtree first because we are consuming postorder from the end
            $node->right = $build($index + 1, $inRight, $postIdx);
            $node->left  = $build($inLeft, $index - 1, $postIdx);

            return $node;
        };

        $postIdx = $n - 1;
        return $build(0, $n - 1, $postIdx);
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
    func buildTree(_ inorder: [Int], _ postorder: [Int]) -> TreeNode? {
        guard !inorder.isEmpty else { return nil }
        var indexMap = [Int: Int]()
        for (i, v) in inorder.enumerated() {
            indexMap[v] = i
        }
        var postIdx = postorder.count - 1
        
        func helper(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right { return nil }
            let rootVal = postorder[postIdx]
            postIdx -= 1
            let node = TreeNode(rootVal)
            let inorderIdx = indexMap[rootVal]!
            // Build right subtree first because we are consuming postorder from the end
            node.right = helper(inorderIdx + 1, right)
            node.left = helper(left, inorderIdx - 1)
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
    fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
        if (inorder.isEmpty()) return null
        val indexMap = HashMap<Int, Int>(inorder.size)
        for (i in inorder.indices) {
            indexMap[inorder[i]] = i
        }

        fun build(inLeft: Int, inRight: Int, postLeft: Int, postRight: Int): TreeNode? {
            if (inLeft > inRight || postLeft > postRight) return null
            val rootVal = postorder[postRight]
            val root = TreeNode(rootVal)
            val inorderRootIdx = indexMap[rootVal]!!
            val leftSize = inorderRootIdx - inLeft
            root.left = build(inLeft, inorderRootIdx - 1, postLeft, postLeft + leftSize - 1)
            root.right = build(inorderRootIdx + 1, inRight, postLeft + leftSize, postRight - 1)
            return root
        }

        return build(0, inorder.size - 1, 0, postorder.size - 1)
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
  late Map<int, int> _inorderIndex;

  TreeNode? buildTree(List<int> inorder, List<int> postorder) {
    final n = inorder.length;
    _inorderIndex = {};
    for (int i = 0; i < n; ++i) {
      _inorderIndex[inorder[i]] = i;
    }
    return _build(inorder, 0, n, postorder, 0, n);
  }

  TreeNode? _build(List<int> inorder, int inStart, int inEnd,
      List<int> postorder, int postStart, int postEnd) {
    if (inStart >= inEnd || postStart >= postEnd) return null;

    final rootVal = postorder[postEnd - 1];
    final root = TreeNode(rootVal);
    final idx = _inorderIndex[rootVal]!;

    final leftSize = idx - inStart;
    root.left = _build(inorder, inStart, idx,
        postorder, postStart, postStart + leftSize);
    root.right = _build(inorder, idx + 1, inEnd,
        postorder, postStart + leftSize, postEnd - 1);

    return root;
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
func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 || len(postorder) == 0 {
		return nil
	}
	idxMap := make(map[int]int, len(inorder))
	for i, v := range inorder {
		idxMap[v] = i
	}
	var helper func(inL, inR, postL, postR int) *TreeNode
	helper = func(inL, inR, postL, postR int) *TreeNode {
		if inL > inR || postL > postR {
			return nil
		}
		rootVal := postorder[postR]
		rootIdx := idxMap[rootVal]
		leftSize := rootIdx - inL

		node := &TreeNode{Val: rootVal}
		node.Left = helper(inL, rootIdx-1, postL, postL+leftSize-1)
		node.Right = helper(rootIdx+1, inR, postL+leftSize, postR-1)
		return node
	}
	return helper(0, len(inorder)-1, 0, len(postorder)-1)
}
```

## Ruby

```ruby
def build_tree(inorder, postorder)
  index_map = {}
  inorder.each_with_index { |val, i| index_map[val] = i }
  @post_idx = postorder.length - 1

  build = lambda do |left, right|
    return nil if left > right
    root_val = postorder[@post_idx]
    @post_idx -= 1
    root = TreeNode.new(root_val)
    inorder_root_index = index_map[root_val]
    root.right = build.call(inorder_root_index + 1, right)
    root.left = build.call(left, inorder_root_index - 1)
    root
  end

  build.call(0, inorder.length - 1)
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
    def buildTree(inorder: Array[Int], postorder: Array[Int]): TreeNode = {
        if (inorder.isEmpty) return null

        val idxMap: Map[Int, Int] = inorder.zipWithIndex.toMap

        def helper(inStart: Int, inEnd: Int, postStart: Int, postEnd: Int): TreeNode = {
            if (inStart > inEnd || postStart > postEnd) return null

            val rootVal = postorder(postEnd)
            val root = new TreeNode(rootVal)

            val idx = idxMap(rootVal)
            val leftSize = idx - inStart

            root.left = helper(inStart, idx - 1, postStart, postStart + leftSize - 1)
            root.right = helper(idx + 1, inEnd, postStart + leftSize, postEnd - 1)

            root
        }

        helper(0, inorder.length - 1, 0, postorder.length - 1)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn build_tree(inorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut idx_map = HashMap::new();
        for (i, &v) in inorder.iter().enumerate() {
            idx_map.insert(v, i);
        }
        fn build(
            in_start: usize,
            in_end: usize,
            post_start: usize,
            post_end: usize,
            inorder: &[i32],
            postorder: &[i32],
            map: &HashMap<i32, usize>,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if in_start >= in_end || post_start >= post_end {
                return None;
            }
            let root_val = postorder[post_end - 1];
            let root_idx = *map.get(&root_val).unwrap();
            let left_len = root_idx - in_start;

            let left = build(
                in_start,
                root_idx,
                post_start,
                post_start + left_len,
                inorder,
                postorder,
                map,
            );
            let right = build(
                root_idx + 1,
                in_end,
                post_start + left_len,
                post_end - 1,
                inorder,
                postorder,
                map,
            );

            Some(Rc::new(RefCell::new(TreeNode {
                val: root_val,
                left,
                right,
            })))
        }

        let n = inorder.len();
        build(0, n, 0, n, &inorder, &postorder, &idx_map)
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

(define/contract (build-tree inorder postorder)
  (-> (listof exact-integer?) (listof exact-integer?) (or/c tree-node? #f))
  (let* ([n (length inorder)]
         [in-vec (list->vector inorder)]
         [post-vec (list->vector postorder)]
         [idx-hash (make-hash)])
    (for ([i (in-range n)])
      (hash-set! idx-hash (vector-ref in-vec i) i))
    (define (helper i-start i-end p-start p-end)
      (if (>= i-start i-end)
          #f
          (let* ([root-val (vector-ref post-vec (- p-end 1))]
                 [node (make-tree-node root-val)]
                 [in-index (hash-ref idx-hash root-val)])
            (define left-size (- in-index i-start))
            (set-tree-node-left! node
                                 (helper i-start in-index p-start (+ p-start left-size)))
            (set-tree-node-right! node
                                  (helper (+ in-index 1) i-end (+ p-start left-size) (- p-end 1)))
            node)))
    (helper 0 n 0 n)))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                      left = null  :: 'null' | #tree_node{},
                      right = null :: 'null' | #tree_node{}}).

-spec build_tree(Inorder :: [integer()], Postorder :: [integer()]) -> #tree_node{} | null.
build_tree(Inorder, Postorder) ->
    InMap = build_map(Inorder, 0, #{}),
    PostTuple = list_to_tuple(Postorder),
    Len = length(Inorder),
    build(0, Len - 1, 0, Len - 1, InMap, PostTuple).

-spec build_map([integer()], integer(), map()) -> map().
build_map([], _Idx, Map) ->
    Map;
build_map([H|T], Idx, Map) ->
    NewMap = maps:put(H, Idx, Map),
    build_map(T, Idx + 1, NewMap).

-spec build(integer(), integer(), integer(), integer(), map(), tuple()) -> #tree_node{} | null.
build(InL, InR, _PostL, _PostR, _InMap, _PostTuple) when InL > InR ->
    null;
build(_InL, _InR, PostL, PostR, InMap, PostTuple) when PostL > PostR ->
    null;
build(InL, InR, PostL, PostR, InMap, PostTuple) ->
    RootVal = element(PostR + 1, PostTuple),
    Index = maps:get(RootVal, InMap),
    LeftSize = Index - InL,
    RightSize = InR - Index,
    LeftNode = build(InL, Index - 1, PostL, PostL + LeftSize - 1, InMap, PostTuple),
    RightNode = build(Index + 1, InR, PostL + LeftSize, PostR - 1, InMap, PostTuple),
    #tree_node{val = RootVal, left = LeftNode, right = RightNode}.
```

## Elixir

```elixir
defmodule Solution do
  @spec build_tree(inorder :: [integer], postorder :: [integer]) :: TreeNode.t | nil
  def build_tree(inorder, postorder) do
    idx_map = for {val, idx} <- Enum.with_index(inorder), into: %{}, do: {val, idx}
    in_t = List.to_tuple(inorder)
    post_t = List.to_tuple(postorder)

    build(in_t, post_t, idx_map, 0, tuple_size(in_t), 0, tuple_size(post_t))
  end

  defp build(_in_t, _post_t, _idx_map, in_start, in_end, _post_start, _post_end)
       when in_start >= in_end do
    nil
  end

  defp build(in_t, post_t, idx_map, in_start, in_end, post_start, post_end) do
    root_val = elem(post_t, post_end - 1)
    idx = Map.fetch!(idx_map, root_val)

    left_len = idx - in_start

    left =
      build(in_t, post_t, idx_map, in_start, idx, post_start, post_start + left_len)

    right =
      build(in_t, post_t, idx_map, idx + 1, in_end, post_start + left_len, post_end - 1)

    %TreeNode{val: root_val, left: left, right: right}
  end
end
```
