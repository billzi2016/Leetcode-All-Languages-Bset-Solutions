# 0655. Print Binary Tree

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
    vector<vector<string>> printTree(TreeNode* root) {
        int height = getHeight(root);
        int cols = (1 << height) - 1;
        vector<vector<string>> res(height, vector<string>(cols, ""));
        fill(res, root, 0, 0, cols - 1);
        return res;
    }
private:
    int getHeight(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
    
    void fill(vector<vector<string>>& mat, TreeNode* node, int row, int left, int right) {
        if (!node || left > right) return;
        int mid = left + (right - left) / 2;
        mat[row][mid] = to_string(node->val);
        fill(mat, node->left, row + 1, left, mid - 1);
        fill(mat, node->right, row + 1, mid + 1, right);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        int rows = height;
        int cols = (1 << height) - 1; // 2^height - 1
        
        List<List<String>> res = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            List<String> row = new ArrayList<>(Collections.nCopies(cols, ""));
            res.add(row);
        }
        
        fill(root, 0, 0, cols - 1, res);
        return res;
    }
    
    private int getHeight(TreeNode node) {
        if (node == null) return 0;
        return Math.max(getHeight(node.left), getHeight(node.right)) + 1;
    }
    
    private void fill(TreeNode node, int r, int left, int right, List<List<String>> res) {
        if (node == null) return;
        int mid = (left + right) / 2;
        res.get(r).set(mid, Integer.toString(node.val));
        fill(node.left, r + 1, left, mid - 1, res);
        fill(node.right, r + 1, mid + 1, right, res);
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
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        # Compute tree height
        def get_height(node):
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            return max(left_h, right_h) + 1

        height = get_height(root)
        width = (1 << height) - 1  # 2^height - 1

        # Initialize result matrix with empty strings
        res = [[""] * width for _ in range(height)]

        # Fill the matrix recursively
        def dfs(node, r, left, right):
            if not node or left > right:
                return
            mid = (left + right) // 2
            res[r][mid] = str(node.val)
            dfs(node.left, r + 1, left, mid - 1)
            dfs(node.right, r + 1, mid + 1, right)

        dfs(root, 0, 0, width - 1)
        return res
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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if not root:
            return []
        
        # Compute tree height
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)
        width = (1 << height) - 1  # 2^height - 1
        
        # Initialize matrix with empty strings
        res = [["" for _ in range(width)] for _ in range(height)]
        
        # Fill the matrix recursively
        def dfs(node, r, left, right):
            if not node or left > right:
                return
            mid = (left + right) // 2
            res[r][mid] = str(node.val)
            dfs(node.left, r + 1, left, mid - 1)
            dfs(node.right, r + 1, mid + 1, right)
        
        dfs(root, 0, 0, width - 1)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Compute the height of the tree */
static int getHeight(struct TreeNode* root) {
    if (!root) return 0;
    int lh = getHeight(root->left);
    int rh = getHeight(root->right);
    return (lh > rh ? lh : rh) + 1;
}

/* Fill the matrix with node values */
static void fill(struct TreeNode* node, char*** res, int row, int left, int right) {
    if (!node || left > right) return;
    int mid = (left + right) / 2;

    /* replace empty string with node value */
    free(res[row][mid]);
    char buf[12];
    sprintf(buf, "%d", node->val);
    size_t len = strlen(buf);
    res[row][mid] = (char*)malloc(len + 1);
    strcpy(res[row][mid], buf);

    fill(node->left,  res, row + 1, left, mid - 1);
    fill(node->right, res, row + 1, mid + 1, right);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** printTree(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    int h = getHeight(root);
    int rows = h;
    int cols = (1 << h) - 1;   // 2^h - 1

    char*** res = (char***)malloc(rows * sizeof(char**));
    int* colSizes = (int*)malloc(rows * sizeof(int));

    for (int i = 0; i < rows; ++i) {
        res[i] = (char**)malloc(cols * sizeof(char*));
        colSizes[i] = cols;
        for (int j = 0; j < cols; ++j) {
            res[i][j] = (char*)malloc(1);
            res[i][j][0] = '\0';
        }
    }

    fill(root, res, 0, 0, cols - 1);

    *returnSize = rows;
    *returnColumnSizes = colSizes;
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
    public IList<IList<string>> PrintTree(TreeNode root) {
        int height = GetHeight(root);
        int rows = height;
        int cols = (1 << height) - 1; // 2^height - 1
        
        var res = new List<IList<string>>(rows);
        for (int i = 0; i < rows; i++) {
            var row = new List<string>(cols);
            for (int j = 0; j < cols; j++) row.Add("");
            res.Add(row);
        }
        
        Fill(root, 0, 0, cols - 1, res);
        return res;
    }
    
    private int GetHeight(TreeNode node) {
        if (node == null) return 0;
        return 1 + Math.Max(GetHeight(node.left), GetHeight(node.right));
    }
    
    private void Fill(TreeNode node, int r, int left, int right, IList<IList<string>> res) {
        if (node == null || left > right) return;
        int mid = (left + right) / 2;
        res[r][mid] = node.val.ToString();
        Fill(node.left, r + 1, left, mid - 1, res);
        Fill(node.right, r + 1, mid + 1, right, res);
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
 * @return {string[][]}
 */
var printTree = function(root) {
    const getHeight = (node) => {
        if (!node) return 0;
        return 1 + Math.max(getHeight(node.left), getHeight(node.right));
    };
    
    const height = getHeight(root);
    const rows = height;
    const cols = Math.pow(2, height) - 1;
    
    // Initialize matrix with empty strings
    const res = Array.from({ length: rows }, () => Array(cols).fill(""));
    
    const dfs = (node, r, left, right) => {
        if (!node || left > right) return;
        const mid = Math.floor((left + right) / 2);
        res[r][mid] = node.val.toString();
        dfs(node.left, r + 1, left, mid - 1);
        dfs(node.right, r + 1, mid + 1, right);
    };
    
    dfs(root, 0, 0, cols - 1);
    return res;
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

function printTree(root: TreeNode | null): string[][] {
    if (!root) return [];

    const height = getHeight(root);
    const rows = height;
    const cols = Math.pow(2, height) - 1;

    const res: string[][] = Array.from({ length: rows }, () => Array(cols).fill(""));

    fill(res, root, 0, 0, cols - 1);
    return res;
}

function getHeight(node: TreeNode | null): number {
    if (!node) return 0;
    return 1 + Math.max(getHeight(node.left), getHeight(node.right));
}

function fill(
    matrix: string[][],
    node: TreeNode | null,
    depth: number,
    left: number,
    right: number
): void {
    if (!node || left > right) return;
    const mid = Math.floor((left + right) / 2);
    matrix[depth][mid] = node.val.toString();
    fill(matrix, node.left, depth + 1, left, mid - 1);
    fill(matrix, node.right, depth + 1, mid + 1, right);
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
     * @return string[][]
     */
    function printTree($root) {
        $height = $this->getHeight($root);
        $rows = $height;
        $cols = (int)pow(2, $height) - 1;
        $res = array_fill(0, $rows, array_fill(0, $cols, ""));
        
        $dfs = function($node, $row, $left, $right) use (&$res, &$dfs) {
            if ($node === null) return;
            $mid = intdiv($left + $right, 2);
            $res[$row][$mid] = (string)$node->val;
            if ($node->left !== null) {
                $dfs($node->left, $row + 1, $left, $mid - 1);
            }
            if ($node->right !== null) {
                $dfs($node->right, $row + 1, $mid + 1, $right);
            }
        };
        
        $dfs($root, 0, 0, $cols - 1);
        return $res;
    }

    private function getHeight($node) {
        if ($node === null) return 0;
        $left = $this->getHeight($node->left);
        $right = $this->getHeight($node->right);
        return max($left, $right) + 1;
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
    func printTree(_ root: TreeNode?) -> [[String]] {
        let height = getHeight(root)
        let rows = height
        let cols = (1 << height) - 1
        var result = Array(repeating: Array(repeating: "", count: cols), count: rows)
        fill(root, 0, 0, cols - 1, &result)
        return result
    }
    
    private func getHeight(_ node: TreeNode?) -> Int {
        guard let n = node else { return 0 }
        return max(getHeight(n.left), getHeight(n.right)) + 1
    }
    
    private func fill(_ node: TreeNode?, _ row: Int, _ left: Int, _ right: Int, _ res: inout [[String]]) {
        guard let n = node else { return }
        let mid = (left + right) / 2
        res[row][mid] = String(n.val)
        fill(n.left, row + 1, left, mid - 1, &res)
        fill(n.right, row + 1, mid + 1, right, &res)
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
    fun printTree(root: TreeNode?): List<List<String>> {
        if (root == null) return emptyList()
        val height = getHeight(root)
        val rows = height
        val cols = (1 shl height) - 1
        val res = MutableList(rows) { MutableList(cols) { "" } }
        fill(res, root, 0, 0, cols - 1)
        return res
    }

    private fun getHeight(node: TreeNode?): Int {
        if (node == null) return 0
        val leftH = getHeight(node.left)
        val rightH = getHeight(node.right)
        return maxOf(leftH, rightH) + 1
    }

    private fun fill(
        res: MutableList<MutableList<String>>,
        node: TreeNode?,
        row: Int,
        left: Int,
        right: Int
    ) {
        if (node == null || left > right) return
        val mid = (left + right) / 2
        res[row][mid] = node.`val`.toString()
        fill(res, node.left, row + 1, left, mid - 1)
        fill(res, node.right, row + 1, mid + 1, right)
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
  List<List<String>> printTree(TreeNode? root) {
    if (root == null) return [];

    int getHeight(TreeNode? node) {
      if (node == null) return -1;
      int left = getHeight(node.left);
      int right = getHeight(node.right);
      return 1 + (left > right ? left : right);
    }

    final int height = getHeight(root);
    final int rows = height + 1;
    final int cols = (1 << (height + 1)) - 1;

    List<List<String>> res =
        List.generate(rows, (_) => List.filled(cols, ""));

    void fill(TreeNode? node, int r, int c) {
      if (node == null) return;
      res[r][c] = node.val.toString();
      if (r == height) return; // leaf level, no children to place
      int offset = 1 << (height - r - 1);
      if (node.left != null) fill(node.left, r + 1, c - offset);
      if (node.right != null) fill(node.right, r + 1, c + offset);
    }

    int startCol = (cols - 1) ~/ 2;
    fill(root, 0, startCol);
    return res;
  }
}
```

## Golang

```go
package main

import "strconv"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func printTree(root *TreeNode) [][]string {
	if root == nil {
		return [][]string{}
	}
	var heightFunc func(*TreeNode) int
	heightFunc = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		lh := heightFunc(node.Left)
		rh := heightFunc(node.Right)
		if lh > rh {
			return lh + 1
		}
		return rh + 1
	}
	h := heightFunc(root)
	w := (1 << h) - 1

	res := make([][]string, h)
	for i := range res {
		res[i] = make([]string, w)
	}

	var fill func(node *TreeNode, r, left, right int)
	fill = func(node *TreeNode, r, left, right int) {
		if node == nil || left > right {
			return
		}
		mid := (left + right) / 2
		res[r][mid] = strconv.Itoa(node.Val)
		fill(node.Left, r+1, left, mid-1)
		fill(node.Right, r+1, mid+1, right)
	}

	fill(root, 0, 0, w-1)
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

def print_tree(root)
  # Compute the height of the tree (root at depth 0)
  height = lambda do |node|
    return -1 unless node
    [height.call(node.left), height.call(node.right)].max + 1
  end
  h = height.call(root)

  rows = h + 1
  cols = (1 << (h + 1)) - 1
  res = Array.new(rows) { Array.new(cols, "") }

  dfs = lambda do |node, r, left, right|
    return unless node
    mid = (left + right) / 2
    res[r][mid] = node.val.to_s
    dfs.call(node.left, r + 1, left, mid - 1)
    dfs.call(node.right, r + 1, mid + 1, right)
  end

  dfs.call(root, 0, 0, cols - 1)
  res
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
    def printTree(root: TreeNode): List[List[String]] = {
        // compute tree height (0-indexed)
        def getHeight(node: TreeNode): Int = {
            if (node == null) -1
            else Math.max(getHeight(node.left), getHeight(node.right)) + 1
        }
        val h = getHeight(root)
        val rows = h + 1
        val cols = (1 << (h + 1)) - 1

        // initialize matrix with empty strings
        val res = Array.ofDim[String](rows, cols)
        var i = 0
        while (i < rows) {
            var j = 0
            while (j < cols) {
                res(i)(j) = ""
                j += 1
            }
            i += 1
        }

        // fill matrix using DFS
        def dfs(node: TreeNode, r: Int, left: Int, right: Int): Unit = {
            if (node == null) return
            val mid = (left + right) / 2
            res(r)(mid) = node.value.toString
            dfs(node.left, r + 1, left, mid - 1)
            dfs(node.right, r + 1, mid + 1, right)
        }

        dfs(root, 0, 0, cols - 1)

        // convert to List[List[String]]
        res.map(_.toList).toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn print_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<String>> {
        fn height(node: &Option<Rc<RefCell<TreeNode>>>) -> usize {
            if let Some(rc) = node {
                let n = rc.borrow();
                1 + std::cmp::max(height(&n.left), height(&n.right))
            } else {
                0
            }
        }

        let h = height(&root);
        let rows = h;
        let cols = (1usize << h) - 1;
        let mut res: Vec<Vec<String>> = vec![vec![String::new(); cols]; rows];

        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            row: usize,
            left: usize,
            right: usize,
            board: &mut Vec<Vec<String>>,
        ) {
            if let Some(rc) = node {
                let n = rc.borrow();
                let mid = (left + right) / 2;
                board[row][mid] = n.val.to_string();
                dfs(&n.left, row + 1, left, mid.saturating_sub(1), board);
                dfs(&n.right, row + 1, mid + 1, right, board);
            }
        }

        if h > 0 {
            dfs(&root, 0, 0, cols - 1, &mut res);
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

;; helper: compute height of the tree
(define (tree-height node)
  (if node
      (+ 1 (max (tree-height (tree-node-left node))
                (tree-height (tree-node-right node))))
      0))

;; helper: recursively place values into matrix
(define (fill! mat node r left right)
  (when node
    (let* ((mid (quotient (+ left right) 2))
           (rowvec (vector-ref mat r)))
      (vector-set! rowvec mid (number->string (tree-node-val node)))
      (fill! mat (tree-node-left node) (+ r 1) left (- mid 1))
      (fill! mat (tree-node-right node) (+ r 1) (+ mid 1) right))))

(define/contract (print-tree root)
  (-> (or/c tree-node? #f) (listof (listof string?)))
  (let* ((h (tree-height root))
         (n (- (arithmetic-shift 1 h) 1)) ; 2^h - 1
         (mat (make-vector h)))
    ;; initialize matrix with empty strings
    (for ([i (in-range h)])
      (vector-set! mat i (make-vector n "")))
    ;; fill values
    (fill! mat root 0 0 (- n 1))
    ;; convert to list of lists
    (let loop ((r 0) (acc '()))
      (if (= r h)
          (reverse acc)
          (loop (+ r 1)
                (cons (vector->list (vector-ref mat r)) acc))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec print_tree(Root :: #tree_node{} | null) -> [[unicode:unicode_binary()]].
print_tree(null) ->
    [];
print_tree(Root) ->
    Height = tree_height(Root),
    Width = (1 bsl Height) - 1,
    PosMap = fill(Root, 0, 0, Width-1, #{}),
    [build_row(RowIdx, Width, PosMap) || RowIdx <- lists:seq(0, Height-1)].

tree_height(null) -> 0;
tree_height(Node) ->
    LeftH = tree_height(Node#tree_node.left),
    RightH = tree_height(Node#tree_node.right),
    1 + max(LeftH, RightH).

fill(null, _Row, _L, _R, Map) -> Map;
fill(Node, Row, L, R, Map) ->
    Mid = (L + R) div 2,
    ValBin = integer_to_binary(Node#tree_node.val),
    NewMap = maps:put({Row,Mid}, ValBin, Map),
    Map1 = fill(Node#tree_node.left, Row+1, L, Mid-1, NewMap),
    fill(Node#tree_node.right, Row+1, Mid+1, R, Map1).

build_row(RowIdx, Width, PosMap) ->
    [maps:get({RowIdx,Col}, PosMap, <<"">>) || Col <- lists:seq(0, Width-1)].
```

## Elixir

```elixir
defmodule Solution do
  @spec print_tree(root :: TreeNode.t | nil) :: [[String.t]]
  def print_tree(root) do
    h = height(root)
    rows = h
    cols = (1 <<< h) - 1

    empty_row = List.duplicate("", cols)

    matrix =
      for _ <- 0..rows - 1, do: empty_row

    root_col = div(cols, 2)

    offset =
      if h >= 2 do
        1 <<< (h - 2)
      else
        0
      end

    fill(matrix, root, 0, root_col, offset)
  end

  defp height(nil), do: 0

  defp height(%TreeNode{left: l, right: r}) do
    1 + max(height(l), height(r))
  end

  defp fill(matrix, nil, _row, _col, _offset), do: matrix

  defp fill(matrix, %TreeNode{val: v, left: l, right: r}, row, col, offset) do
    updated =
      List.update_at(matrix, row, fn line ->
        List.update_at(line, col, fn _ -> Integer.to_string(v) end)
      end)

    if offset == 0 do
      updated
    else
      new_offset = div(offset, 2)
      left_col = col - offset
      right_col = col + offset

      after_left = fill(updated, l, row + 1, left_col, new_offset)
      fill(after_left, r, row + 1, right_col, new_offset)
    end
  end
end
```
