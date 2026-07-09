# 0889. Construct Binary Tree from Preorder and Postorder Traversal

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
    vector<int> pre, post;
    unordered_map<int,int> idxInPost;
    
    TreeNode* build(int preL, int preR, int postL, int postR){
        if (preL > preR) return nullptr;
        TreeNode* root = new TreeNode(pre[preL]);
        if (preL == preR) return root;
        
        int leftRootVal = pre[preL + 1];
        int leftRootIdxPost = idxInPost[leftRootVal];
        int leftSize = leftRootIdxPost - postL + 1;
        
        root->left = build(preL + 1, preL + leftSize, postL, leftRootIdxPost);
        root->right = build(preL + leftSize + 1, preR, leftRootIdxPost + 1, postR - 1);
        return root;
    }
    
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        pre = preorder;
        post = postorder;
        for (int i = 0; i < (int)post.size(); ++i) {
            idxInPost[post[i]] = i;
        }
        return build(0, (int)pre.size() - 1, 0, (int)post.size() - 1);
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
    private int[] postorder;
    private java.util.Map<Integer, Integer> postIndexMap;

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        this.preorder = preorder;
        this.postorder = postorder;
        this.postIndexMap = new java.util.HashMap<>();
        for (int i = 0; i < postorder.length; i++) {
            postIndexMap.put(postorder[i], i);
        }
        return build(0, preorder.length - 1, 0, postorder.length - 1);
    }

    private TreeNode build(int preStart, int preEnd, int postStart, int postEnd) {
        if (preStart > preEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        if (preStart == preEnd) {
            return root;
        }

        // The next element in preorder is the left child root.
        int leftRootVal = preorder[preStart + 1];
        int leftRootIdxInPost = postIndexMap.get(leftRootVal);
        int leftSize = leftRootIdxInPost - postStart + 1;

        root.left = build(preStart + 1, preStart + leftSize,
                          postStart, leftRootIdxInPost);

        root.right = build(preStart + leftSize + 1, preEnd,
                           leftRootIdxInPost + 1, postEnd - 1);
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
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.pre_idx = 0
        self.post_idx = 0

        def build():
            root_val = preorder[self.pre_idx]
            node = TreeNode(root_val)
            self.pre_idx += 1

            if node.val != postorder[self.post_idx]:
                node.left = build()
            if node.val != postorder[self.post_idx]:
                node.right = build()

            self.post_idx += 1
            return node

        return build()
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_in_post = {val: i for i, val in enumerate(postorder)}
        
        def build(pre_start: int, pre_end: int, post_start: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            
            left_root_val = preorder[pre_start + 1]
            left_root_idx = index_in_post[left_root_val]
            left_size = left_root_idx - post_start + 1
            
            root.left = build(pre_start + 1, pre_start + left_size, post_start)
            root.right = build(pre_start + left_size + 1, pre_end, left_root_idx + 1)
            return root
        
        n = len(preorder)
        return build(0, n - 1, 0)
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
static struct TreeNode* build(int preStart, int preEnd, int postStart,
                              int* preorder, int* pos) {
    if (preStart > preEnd) return NULL;

    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = preorder[preStart];
    root->left = root->right = NULL;

    if (preStart == preEnd) return root;

    int leftRootVal = preorder[preStart + 1];
    int leftRootIdxInPost = pos[leftRootVal];
    int leftSize = leftRootIdxInPost - postStart + 1;

    root->left = build(preStart + 1, preStart + leftSize,
                       postStart, preorder, pos);
    root->right = build(preStart + leftSize + 1, preEnd,
                        leftRootIdxInPost + 1, preorder, pos);

    return root;
}

struct TreeNode* constructFromPrePost(int* preorder, int preorderSize,
                                      int* postorder, int postorderSize) {
    int* pos = (int*)malloc((preorderSize + 1) * sizeof(int));
    for (int i = 0; i < postorderSize; ++i) {
        pos[postorder[i]] = i;
    }

    struct TreeNode* root = build(0, preorderSize - 1, 0, preorder, pos);
    free(pos);
    return root;
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
    public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder) {
        int n = preorder.Length;
        var posInPost = new Dictionary<int, int>(n);
        for (int i = 0; i < n; i++) {
            posInPost[postorder[i]] = i;
        }
        return Build(0, n - 1, 0, preorder, posInPost);
    }

    private TreeNode Build(int preStart, int preEnd, int postStart, int[] preorder, Dictionary<int, int> posInPost) {
        if (preStart > preEnd) return null;
        var root = new TreeNode(preorder[preStart]);
        if (preStart == preEnd) return root;

        int leftRootVal = preorder[preStart + 1];
        int leftRootIdxInPost = posInPost[leftRootVal];
        int leftSize = leftRootIdxInPost - postStart + 1;

        root.left = Build(preStart + 1, preStart + leftSize, postStart, preorder, posInPost);
        root.right = Build(preStart + leftSize + 1, preEnd, leftRootIdxInPost + 1, preorder, posInPost);
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
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var constructFromPrePost = function(preorder, postorder) {
    const n = preorder.length;
    const pos = new Array(n + 1);
    for (let i = 0; i < n; ++i) {
        pos[postorder[i]] = i;
    }

    function build(preL, preR, postL) {
        if (preL > preR) return null;
        const root = new TreeNode(preorder[preL]);
        if (preL === preR) return root;

        const leftRootVal = preorder[preL + 1];
        const leftSize = pos[leftRootVal] - postL + 1;

        root.left = build(preL + 1, preL + leftSize, postL);
        root.right = build(preL + leftSize + 1, preR, postL + leftSize);
        return root;
    }

    return build(0, n - 1, 0);
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

function constructFromPrePost(preorder: number[], postorder: number[]): TreeNode | null {
    const n = preorder.length;
    if (n === 0) return null;

    const idxMap = new Map<number, number>();
    for (let i = 0; i < n; ++i) {
        idxMap.set(postorder[i], i);
    }

    function build(preStart: number, preEnd: number, postStart: number): TreeNode | null {
        if (preStart > preEnd) return null;
        const root = new TreeNode(preorder[preStart]);
        if (preStart === preEnd) return root;

        const leftRootVal = preorder[preStart + 1];
        const leftRootIdxInPost = idxMap.get(leftRootVal)!;
        const leftSize = leftRootIdxInPost - postStart + 1;

        root.left = build(preStart + 1, preStart + leftSize, postStart);
        root.right = build(preStart + leftSize + 1, preEnd, leftRootIdxInPost + 1);
        return root;
    }

    return build(0, n - 1, 0);
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
     * @param Integer[] $preorder
     * @param Integer[] $postorder
     * @return TreeNode|null
     */
    function constructFromPrePost($preorder, $postorder) {
        $n = count($preorder);
        if ($n == 0) return null;
        $pos = [];
        foreach ($postorder as $i => $val) {
            $pos[$val] = $i;
        }
        return $this->build($preorder, 0, $n - 1, $postorder, 0, $pos);
    }

    private function build(&$pre, $preStart, $preEnd, &$post, $postStart, &$pos) {
        if ($preStart > $preEnd) return null;
        $root = new TreeNode($pre[$preStart]);
        if ($preStart == $preEnd) {
            return $root;
        }
        $leftRootVal = $pre[$preStart + 1];
        $leftSize = $pos[$leftRootVal] - $postStart + 1;

        $root->left = $this->build($pre, $preStart + 1, $preStart + $leftSize, $post, $postStart, $pos);
        $root->right = $this->build($pre, $preStart + $leftSize + 1, $preEnd, $post, $postStart + $leftSize, $pos);
        return $root;
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
    private var preorder: [Int] = []
    private var postIndexMap: [Int:Int] = [:]
    
    func constructFromPrePost(_ preorder: [Int], _ postorder: [Int]) -> TreeNode? {
        self.preorder = preorder
        for (i, v) in postorder.enumerated() {
            postIndexMap[v] = i
        }
        return build(preStart: 0, preEnd: preorder.count - 1, postStart: 0)
    }
    
    private func build(preStart: Int, preEnd: Int, postStart: Int) -> TreeNode? {
        if preStart > preEnd { return nil }
        let root = TreeNode(preorder[preStart])
        if preStart == preEnd { return root }
        
        let leftRootVal = preorder[preStart + 1]
        guard let leftRootIdx = postIndexMap[leftRootVal] else { return root }
        let leftSize = leftRootIdx - postStart + 1
        
        root.left = build(preStart: preStart + 1,
                          preEnd: preStart + leftSize,
                          postStart: postStart)
        root.right = build(preStart: preStart + leftSize + 1,
                           preEnd: preEnd,
                           postStart: postStart + leftSize)
        return root
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
    private lateinit var preorder: IntArray
    private lateinit var postIndexMap: IntArray

    fun constructFromPrePost(preorder: IntArray, postorder: IntArray): TreeNode? {
        this.preorder = preorder
        val n = preorder.size
        postIndexMap = IntArray(n + 1)
        for (i in postorder.indices) {
            postIndexMap[postorder[i]] = i
        }
        return build(0, n - 1, 0)
    }

    private fun build(preStart: Int, preEnd: Int, postStart: Int): TreeNode? {
        if (preStart > preEnd) return null
        val root = TreeNode(preorder[preStart])
        if (preStart == preEnd) return root

        val leftRootVal = preorder[preStart + 1]
        val leftRootIdxInPost = postIndexMap[leftRootVal]
        val leftSize = leftRootIdxInPost - postStart + 1

        root.left = build(preStart + 1, preStart + leftSize, postStart)
        root.right = build(preStart + leftSize + 1, preEnd, leftRootIdxInPost + 1)

        return root
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
  TreeNode? constructFromPrePost(List<int> preorder, List<int> postorder) {
    final Map<int, int> idx = {};
    for (int i = 0; i < postorder.length; ++i) {
      idx[postorder[i]] = i;
    }

    TreeNode? build(int preStart, int preEnd, int postStart) {
      if (preStart > preEnd) return null;
      final root = TreeNode(preorder[preStart]);
      if (preStart == preEnd) return root;

      final leftRootVal = preorder[preStart + 1];
      final leftSize = idx[leftRootVal]! - postStart + 1;

      root.left = build(preStart + 1, preStart + leftSize, postStart);
      root.right = build(preStart + leftSize + 1, preEnd, postStart + leftSize);
      return root;
    }

    return build(0, preorder.length - 1, 0);
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
func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
    // map each value to its index in postorder for O(1) lookups
    idx := make(map[int]int, len(postorder))
    for i, v := range postorder {
        idx[v] = i
    }

    var build func(preStart, preEnd, postStart int) *TreeNode
    build = func(preStart, preEnd, postStart int) *TreeNode {
        if preStart > preEnd {
            return nil
        }
        root := &TreeNode{Val: preorder[preStart]}
        if preStart == preEnd {
            return root
        }

        // The next element in preorder is the left child root
        leftRootVal := preorder[preStart+1]
        leftRootIdx := idx[leftRootVal]

        // Number of nodes in left subtree
        leftSize := leftRootIdx - postStart + 1

        root.Left = build(preStart+1, preStart+leftSize, postStart)
        root.Right = build(preStart+leftSize+1, preEnd, leftRootIdx+1)

        return root
    }

    return build(0, len(preorder)-1, 0)
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

def construct_from_pre_post(preorder, postorder)
  n = preorder.length
  index_in_post = {}
  postorder.each_with_index { |v, i| index_in_post[v] = i }

  build = lambda do |pre_l, pre_r, post_l|
    return nil if pre_l > pre_r

    root = TreeNode.new(preorder[pre_l])
    return root if pre_l == pre_r

    left_root_val = preorder[pre_l + 1]
    left_size = index_in_post[left_root_val] - post_l + 1

    root.left = build.call(pre_l + 1, pre_l + left_size, post_l)
    root.right = build.call(pre_l + left_size + 1, pre_r, post_l + left_size)

    root
  end

  build.call(0, n - 1, 0)
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
    def constructFromPrePost(preorder: Array[Int], postorder: Array[Int]): TreeNode = {
        val n = preorder.length
        if (n == 0) return null

        // map value -> index in postorder for O(1) lookups
        val idxInPost = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            idxInPost(postorder(i)) = i
            i += 1
        }

        def helper(preStart: Int, preEnd: Int, postStart: Int): TreeNode = {
            if (preStart > preEnd) return null
            if (preStart == preEnd) return new TreeNode(preorder(preStart))

            val leftRootVal = preorder(preStart + 1)
            val leftRootIdx = idxInPost(leftRootVal)
            val leftSize = leftRootIdx - postStart + 1

            val root = new TreeNode(preorder(preStart))
            root.left = helper(preStart + 1, preStart + leftSize, postStart)
            root.right = helper(preStart + leftSize + 1, preEnd, leftRootIdx + 1)
            root
        }

        helper(0, n - 1, 0)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn construct_from_pre_post(preorder: Vec<i32>, postorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        let n = preorder.len();
        if n == 0 {
            return None;
        }
        let mut idx_map = HashMap::with_capacity(n);
        for (i, &v) in postorder.iter().enumerate() {
            idx_map.insert(v, i);
        }
        Self::build(0, n - 1, 0, &preorder, &idx_map)
    }

    fn build(
        pre_start: usize,
        pre_end: usize,
        post_start: usize,
        preorder: &[i32],
        idx_map: &HashMap<i32, usize>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        if pre_start > pre_end {
            return None;
        }
        let root_val = preorder[pre_start];
        let node = Rc::new(RefCell::new(TreeNode::new(root_val)));
        if pre_start == pre_end {
            return Some(node);
        }

        // The next element in preorder is the left child's root.
        let left_root_val = preorder[pre_start + 1];
        let left_root_post_idx = *idx_map.get(&left_root_val).unwrap();
        let left_size = left_root_post_idx - post_start + 1;

        node.borrow_mut().left = Self::build(
            pre_start + 1,
            pre_start + left_size,
            post_start,
            preorder,
            idx_map,
        );
        node.borrow_mut().right = Self::build(
            pre_start + left_size + 1,
            pre_end,
            left_root_post_idx + 1,
            preorder,
            idx_map,
        );

        Some(node)
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(: construct-from-pre-post (-> (listof exact-integer?) (listof exact-integer?) (or/c tree-node? #f)))
(define (construct-from-pre-post preorder postorder)
  (let* ([n (length preorder)]
         [pre-vec (list->vector preorder)]
         [post-vec (list->vector postorder)]
         ;; build a hash table mapping value -> index in postorder
         [pos-hash (make-hash)])
    (for ([i (in-range n)])
      (hash-set! pos-hash (vector-ref post-vec i) i))
    (define (build pre-start pre-end post-start post-end)
      (if (> pre-start pre-end)
          #f
          (let* ([root-val (vector-ref pre-vec pre-start)]
                 [node (make-tree-node root-val)])
            (if (= pre-start pre-end)
                node
                (let* ([left-root-val (vector-ref pre-vec (+ pre-start 1))]
                       [left-root-pos (hash-ref pos-hash left-root-val)]
                       [left-size (+ (- left-root-pos post-start) 1)])
                  (set-tree-node-left!
                   node
                   (build (+ pre-start 1)
                          (+ pre-start left-size)
                          post-start
                          left-root-pos))
                  (set-tree-node-right!
                   node
                   (build (+ pre-start left-size 1)
                          pre-end
                          (+ left-root-pos 1)
                          (- post-end 1)))
                  node)))))
    (if (= n 0) #f (build 0 (sub1 n) 0 (sub1 n)))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                     left = null  :: 'null' | #tree_node{},
                     right = null :: 'null' | #tree_node{}}).

-spec construct_from_pre_post(Preorder :: [integer()], Postorder :: [integer()]) -> #tree_node{} | null.
construct_from_pre_post(Preorder, Postorder) ->
    PreTuple = list_to_tuple(Preorder),
    IndexMap = build_index_map(Postorder, 0, #{}),
    helper(0, tuple_size(PreTuple) - 1, 0, PreTuple, IndexMap).

-spec build_index_map([integer()], integer(), map()) -> map().
build_index_map([], _Idx, Map) ->
    Map;
build_index_map([V | Rest], Idx, Map) ->
    NewMap = maps:put(V, Idx, Map),
    build_index_map(Rest, Idx + 1, NewMap).

-spec helper(integer(), integer(), integer(), tuple(), map()) -> #tree_node{} | null.
helper(PreStart, PreEnd, _PostStart, _PreTuple, _IndexMap) when PreStart > PreEnd ->
    null;
helper(PreStart, PreEnd, _PostStart, PreTuple, _IndexMap) when PreStart == PreEnd ->
    Val = element(PreStart + 1, PreTuple),
    #tree_node{val = Val, left = null, right = null};
helper(PreStart, PreEnd, PostStart, PreTuple, IndexMap) ->
    RootVal   = element(PreStart + 1, PreTuple),
    LeftRootVal = element(PreStart + 2, PreTuple),
    LeftRootPos = maps:get(LeftRootVal, IndexMap),
    NumLeft = LeftRootPos - PostStart + 1,
    Left  = helper(PreStart + 1, PreStart + NumLeft, PostStart, PreTuple, IndexMap),
    Right = helper(PreStart + NumLeft + 1, PreEnd, PostStart + NumLeft, PreTuple, IndexMap),
    #tree_node{val = RootVal, left = Left, right = Right}.
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_from_pre_post([integer], [integer]) :: TreeNode.t() | nil
  def construct_from_pre_post([], _), do: nil

  def construct_from_pre_post(preorder, postorder) do
    pre = List.to_tuple(preorder)

    idx_map =
      postorder
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, v, i) end)

    n = tuple_size(pre)
    build(pre, idx_map, 0, n - 1, 0)
  end

  defp build(_pre, _idx_map, pre_s, pre_e, _post_s) when pre_s > pre_e do
    nil
  end

  defp build(pre, idx_map, pre_s, pre_e, post_s) do
    root_val = elem(pre, pre_s)
    node = %TreeNode{val: root_val}

    if pre_s == pre_e do
      node
    else
      left_root_val = elem(pre, pre_s + 1)
      left_root_idx = Map.fetch!(idx_map, left_root_val)
      left_size = left_root_idx - post_s + 1

      left_child =
        build(pre, idx_map, pre_s + 1, pre_s + left_size, post_s)

      right_child =
        build(pre, idx_map, pre_s + left_size + 1, pre_e, post_s + left_size)

      %TreeNode{node | left: left_child, right: right_child}
    end
  end
end
```
