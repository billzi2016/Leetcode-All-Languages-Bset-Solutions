# 0987. Vertical Order Traversal of a Binary Tree

## Cpp

```cpp
#include <bits/stdc++.h>
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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<tuple<int,int,int>> nodes; // col, row, value
        function<void(TreeNode*,int,int)> dfs = [&](TreeNode* node, int row, int col){
            if (!node) return;
            nodes.emplace_back(col, row, node->val);
            dfs(node->left, row + 1, col - 1);
            dfs(node->right, row + 1, col + 1);
        };
        dfs(root, 0, 0);
        sort(nodes.begin(), nodes.end(), [](const auto& a, const auto& b){
            if (get<0>(a) != get<0>(b)) return get<0>(a) < get<0>(b); // col
            if (get<1>(a) != get<1>(b)) return get<1>(a) < get<1>(b); // row
            return get<2>(a) < get<2>(b); // value
        });
        vector<vector<int>> ans;
        int prevCol = INT_MIN;
        for (auto& t : nodes) {
            int col = get<0>(t);
            int val = get<2>(t);
            if (col != prevCol) {
                ans.emplace_back();
                prevCol = col;
            }
            ans.back().push_back(val);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<int[]> nodes = new ArrayList<>();
        dfs(root, 0, 0, nodes);
        Collections.sort(nodes, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]); // column
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]); // row
            return Integer.compare(a[2], b[2]);                 // value
        });
        List<List<Integer>> result = new ArrayList<>();
        int prevCol = Integer.MIN_VALUE;
        for (int[] n : nodes) {
            int col = n[0];
            int val = n[2];
            if (col != prevCol) {
                result.add(new ArrayList<>());
                prevCol = col;
            }
            result.get(result.size() - 1).add(val);
        }
        return result;
    }

    private void dfs(TreeNode node, int row, int col, List<int[]> nodes) {
        if (node == null) return;
        nodes.add(new int[]{col, row, node.val});
        dfs(node.left, row + 1, col - 1, nodes);
        dfs(node.right, row + 1, col + 1, nodes);
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
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        nodes = []  # list of (col, row, val)
        
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        # sort by column, then row, then value
        nodes.sort()
        
        from collections import defaultdict
        cols = defaultdict(list)
        for c, r, v in nodes:
            cols[c].append(v)
        
        result = []
        for col in sorted(cols.keys()):
            result.append(cols[col])
        return result
```

## Python3

```python
from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)  # col -> list of (row, value)

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if not node:
                return
            nodes[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(nodes.keys()):
            column_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in column_nodes])
        return result
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
struct NodeInfo {
    int col;
    int row;
    int val;
};

static void dfs(struct TreeNode* root, int row, int col,
                struct NodeInfo** arr, int* size, int* cap) {
    if (!root) return;
    if (*size == *cap) {
        *cap = (*cap == 0) ? 128 : (*cap * 2);
        *arr = realloc(*arr, (*cap) * sizeof(struct NodeInfo));
    }
    (*arr)[(*size)++] = (struct NodeInfo){col, row, root->val};
    dfs(root->left, row + 1, col - 1, arr, size, cap);
    dfs(root->right, row + 1, col + 1, arr, size, cap);
}

static int cmpNode(const void* a, const void* b) {
    const struct NodeInfo* x = (const struct NodeInfo*)a;
    const struct NodeInfo* y = (const struct NodeInfo*)b;
    if (x->col != y->col) return x->col - y->col;
    if (x->row != y->row) return x->row - y->row;
    return x->val - y->val;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** verticalTraversal(struct TreeNode* root, int* returnSize, int*** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    struct NodeInfo* nodes = NULL;
    int sz = 0, cap = 0;
    dfs(root, 0, 0, &nodes, &sz, &cap);

    qsort(nodes, sz, sizeof(struct NodeInfo), cmpNode);

    // Count distinct columns
    int groups = 0;
    for (int i = 0; i < sz; ++i) {
        if (i == 0 || nodes[i].col != nodes[i - 1].col)
            groups++;
    }

    int* colSizes = malloc(groups * sizeof(int));
    memset(colSizes, 0, groups * sizeof(int));

    // Compute sizes per column
    int g = -1;
    for (int i = 0; i < sz; ++i) {
        if (i == 0 || nodes[i].col != nodes[i - 1].col)
            g++;
        colSizes[g]++;
    }

    int** ans = malloc(groups * sizeof(int*));
    for (int i = 0; i < groups; ++i) {
        ans[i] = malloc(colSizes[i] * sizeof(int));
    }

    // Fill answer
    int* pos = calloc(groups, sizeof(int));
    g = -1;
    for (int i = 0; i < sz; ++i) {
        if (i == 0 || nodes[i].col != nodes[i - 1].col)
            g++;
        ans[g][pos[g]++] = nodes[i].val;
    }

    free(pos);
    free(nodes);

    *returnSize = groups;
    *returnColumnSizes = &colSizes;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> VerticalTraversal(TreeNode root) {
        var map = new Dictionary<int, List<(int row, int val)>>();

        void DFS(TreeNode node, int row, int col) {
            if (node == null) return;
            if (!map.ContainsKey(col)) map[col] = new List<(int, int)>();
            map[col].Add((row, node.val));
            DFS(node.left, row + 1, col - 1);
            DFS(node.right, row + 1, col + 1);
        }

        DFS(root, 0, 0);

        var cols = new List<int>(map.Keys);
        cols.Sort();

        IList<IList<int>> result = new List<IList<int>>();
        foreach (int c in cols) {
            var list = map[c];
            list.Sort((a, b) => {
                int cmp = a.row.CompareTo(b.row);
                return cmp != 0 ? cmp : a.val.CompareTo(b.val);
            });
            var columnVals = new List<int>();
            foreach (var p in list) columnVals.Add(p.val);
            result.Add(columnVals);
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
 * @return {number[][]}
 */
var verticalTraversal = function(root) {
    const nodes = [];
    const dfs = (node, row, col) => {
        if (!node) return;
        nodes.push([col, row, node.val]);
        dfs(node.left, row + 1, col - 1);
        dfs(node.right, row + 1, col + 1);
    };
    dfs(root, 0, 0);
    
    nodes.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];      // column
        if (a[1] !== b[1]) return a[1] - b[1];      // row
        return a[2] - b[2];                         // value
    });
    
    const result = [];
    let prevCol = null;
    for (const [col, , val] of nodes) {
        if (col !== prevCol) {
            result.push([]);
            prevCol = col;
        }
        result[result.length - 1].push(val);
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

function verticalTraversal(root: TreeNode | null): number[][] {
    if (!root) return [];

    // Collect nodes as [col, row, value]
    const nodes: Array<[number, number, number]> = [];
    const queue: Array<{ node: TreeNode; col: number; row: number }> = [{ node: root, col: 0, row: 0 }];

    while (queue.length) {
        const { node, col, row } = queue.shift()!;
        nodes.push([col, row, node.val]);
        if (node.left) queue.push({ node: node.left, col: col - 1, row: row + 1 });
        if (node.right) queue.push({ node: node.right, col: col + 1, row: row + 1 });
    }

    // Sort by column, then row, then value
    nodes.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[2] - b[2];
    });

    const result: number[][] = [];
    let prevCol = Number.NEGATIVE_INFINITY;

    for (const [col, , val] of nodes) {
        if (col !== prevCol) {
            result.push([]);
            prevCol = col;
        }
        result[result.length - 1].push(val);
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
     * @return Integer[][]
     */
    function verticalTraversal($root) {
        if ($root === null) {
            return [];
        }

        // Collect (col, row, value) for each node using DFS
        $nodes = [];
        $stack = [[$root, 0, 0]]; // each element: [node, row, col]

        while (!empty($stack)) {
            [$node, $row, $col] = array_pop($stack);
            $nodes[] = [$col, $row, $node->val];

            if ($node->right !== null) {
                $stack[] = [$node->right, $row + 1, $col + 1];
            }
            if ($node->left !== null) {
                $stack[] = [$node->left, $row + 1, $col - 1];
            }
        }

        // Sort by column, then row, then value
        usort($nodes, function($a, $b) {
            if ($a[0] != $b[0]) return $a[0] <=> $b[0];
            if ($a[1] != $b[1]) return $a[1] <=> $b[1];
            return $a[2] <=> $b[2];
        });

        // Group values by column
        $result = [];
        $prevCol = null;
        foreach ($nodes as $entry) {
            [$col, $row, $val] = $entry;
            if ($col !== $prevCol) {
                $result[] = [];
                $prevCol = $col;
            }
            $result[count($result) - 1][] = $val;
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
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        var nodes = [(col: Int, row: Int, val: Int)]()
        
        func dfs(_ node: TreeNode?, _ row: Int, _ col: Int) {
            guard let n = node else { return }
            nodes.append((col, row, n.val))
            dfs(n.left, row + 1, col - 1)
            dfs(n.right, row + 1, col + 1)
        }
        
        dfs(root, 0, 0)
        
        nodes.sort {
            if $0.col != $1.col { return $0.col < $1.col }
            if $0.row != $1.row { return $0.row < $1.row }
            return $0.val < $1.val
        }
        
        var result = [[Int]]()
        var currentCol: Int? = nil
        var columnVals = [Int]()
        
        for node in nodes {
            if currentCol == nil || node.col != currentCol! {
                if let _ = currentCol {
                    result.append(columnVals)
                }
                columnVals = []
                currentCol = node.col
            }
            columnVals.append(node.val)
        }
        if !columnVals.isEmpty {
            result.append(columnVals)
        }
        
        return result
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
    fun verticalTraversal(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()
        data class NodeInfo(val col: Int, val row: Int, val value: Int)
        val nodes = mutableListOf<NodeInfo>()
        fun dfs(node: TreeNode?, row: Int, col: Int) {
            if (node == null) return
            nodes.add(NodeInfo(col, row, node.`val`))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        }
        dfs(root, 0, 0)
        nodes.sortWith(compareBy<NodeInfo> { it.col }.thenBy { it.row }.thenBy { it.value })
        val columnMap = linkedMapOf<Int, MutableList<Int>>()
        for (info in nodes) {
            columnMap.getOrPut(info.col) { mutableListOf() }.add(info.value)
        }
        return columnMap.values.map { it.toList() }
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
class _Triple {
  int col;
  int row;
  int val;
  _Triple(this.col, this.row, this.val);
}

class Solution {
  List<List<int>> verticalTraversal(TreeNode? root) {
    if (root == null) return [];
    final List<_Triple> nodes = [];

    void dfs(TreeNode? node, int row, int col) {
      if (node == null) return;
      nodes.add(_Triple(col, row, node.val));
      dfs(node.left, row + 1, col - 1);
      dfs(node.right, row + 1, col + 1);
    }

    dfs(root, 0, 0);

    nodes.sort((a, b) {
      if (a.col != b.col) return a.col.compareTo(b.col);
      if (a.row != b.row) return a.row.compareTo(b.row);
      return a.val.compareTo(b.val);
    });

    final List<List<int>> result = [];
    int? prevCol;
    for (final t in nodes) {
      if (prevCol == null || t.col != prevCol) {
        result.add([]);
        prevCol = t.col;
      }
      result.last.add(t.val);
    }

    return result;
  }
}
```

## Golang

```go
package main

import "sort"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func verticalTraversal(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	type info struct{ val, row, col int }
	var nodes []info

	var dfs func(node *TreeNode, row, col int)
	dfs = func(node *TreeNode, row, col int) {
		if node == nil {
			return
		}
		nodes = append(nodes, info{node.Val, row, col})
		dfs(node.Left, row+1, col-1)
		dfs(node.Right, row+1, col+1)
	}
	dfs(root, 0, 0)

	sort.Slice(nodes, func(i, j int) bool {
		if nodes[i].col != nodes[j].col {
			return nodes[i].col < nodes[j].col
		}
		if nodes[i].row != nodes[j].row {
			return nodes[i].row < nodes[j].row
		}
		return nodes[i].val < nodes[j].val
	})

	var res [][]int
	curCol := 0
	for idx, n := range nodes {
		if idx == 0 || n.col != curCol {
			res = append(res, []int{n.val})
			curCol = n.col
		} else {
			res[len(res)-1] = append(res[len(res)-1], n.val)
		}
	}
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

def vertical_traversal(root)
  return [] unless root

  nodes = []
  queue = [[root, 0, 0]] # node, row, col
  i = 0
  while i < queue.length
    node, row, col = queue[i]
    nodes << [col, row, node.val]
    if node.left
      queue << [node.left, row + 1, col - 1]
    end
    if node.right
      queue << [node.right, row + 1, col + 1]
    end
    i += 1
  end

  nodes.sort_by! { |col, row, val| [col, row, val] }

  result = []
  current_col = nil
  nodes.each do |col, _row, val|
    if col != current_col
      result << []
      current_col = col
    end
    result[-1] << val
  end

  result
end
```

## Scala

```scala
object Solution {
    def verticalTraversal(root: TreeNode): List[List[Int]] = {
        if (root == null) return Nil

        case class Info(col: Int, row: Int, value: Int)

        val nodes = scala.collection.mutable.ArrayBuffer[Info]()
        val queue = scala.collection.mutable.Queue[(TreeNode, Int, Int)]()
        queue.enqueue((root, 0, 0))

        while (queue.nonEmpty) {
            val (node, col, row) = queue.dequeue()
            nodes += Info(col, row, node.value)
            if (node.left != null) queue.enqueue((node.left, col - 1, row + 1))
            if (node.right != null) queue.enqueue((node.right, col + 1, row + 1))
        }

        val sorted = nodes.sortBy(info => (info.col, info.row, info.value))

        val map = scala.collection.mutable.LinkedHashMap[Int, scala.collection.mutable.ListBuffer[Int]]()
        for (info <- sorted) {
            val list = map.getOrElseUpdate(info.col, scala.collection.mutable.ListBuffer[Int]())
            list += info.value
        }

        map.values.map(_.toList).toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn vertical_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        if root.is_none() {
            return vec![];
        }
        let mut entries: Vec<(i32, i32, i32)> = Vec::new();
        let mut queue: VecDeque<(Rc<RefCell<TreeNode>>, i32, i32)> = VecDeque::new();
        queue.push_back((root.unwrap(), 0, 0));
        while let Some((node_rc, row, col)) = queue.pop_front() {
            let node_ref = node_rc.borrow();
            entries.push((col, row, node_ref.val));
            if let Some(left) = &node_ref.left {
                queue.push_back((Rc::clone(left), row + 1, col - 1));
            }
            if let Some(right) = &node_ref.right {
                queue.push_back((Rc::clone(right), row + 1, col + 1));
            }
        }
        entries.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else {
                a.2.cmp(&b.2)
            }
        });
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut current_col: Option<i32> = None;
        for (col, _row, val) in entries {
            if Some(col) != current_col {
                result.push(Vec::new());
                current_col = Some(col);
            }
            if let Some(last) = result.last_mut() {
                last.push(val);
            }
        }
        result
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

(define/contract (vertical-traversal root)
  (-> (or/c tree-node? #f) (listof (listof exact-integer?)))
  (if (not root)
      '()
      (letrec
          ((traverse
            (lambda (node col row acc)
              (if (not node)
                  acc
                  (let* ((new-acc (cons (list col row (tree-node-val node)) acc))
                         (left-acc (traverse (tree-node-left node) (- col 1) (+ row 1) new-acc)))
                    (traverse (tree-node-right node) (+ col 1) (+ row 1) left-acc))))))
        (let* ((triples (traverse root 0 0 '()))
               (sorted
                (sort triples
                      (lambda (a b)
                        (cond [(< (first a) (first b)) #t]
                              [(> (first a) (first b)) #f]
                              [else (let ((ra (second a)) (rb (second b)))
                                      (if (< ra rb) #t
                                          (if (> ra rb) #f
                                              (< (third a) (third b)))))]))))
               (grouped
                (let loop ((lst sorted)
                           (current-col #f)
                           (curr '())
                           (res '()))
                  (cond [(null? lst)
                         (reverse (if (null? curr) res (cons (reverse curr) res)))]
                        [else
                         (define col (first (car lst)))
                         (define val (third (car lst)))
                         (if (or (not current-col) (= col current-col))
                             (loop (cdr lst) col (cons val curr) res)
                             (loop (cdr lst) col (list val) (cons (reverse curr) res)))]))))
          grouped))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec vertical_traversal(Root :: #tree_node{} | null) -> [[integer()]].
vertical_traversal(Root) when Root =:= null ->
    [];
vertical_traversal(Root) ->
    Queue0 = queue:new(),
    Queue1 = queue:in({Root, 0, 0}, Queue0),
    Entries = bfs(Queue1, []),
    Sorted = lists:sort(Entries),                     % {Col, Row, Val}
    Map = group_entries(Sorted, #{}),
    Cols = lists:sort(maps:keys(Map)),
    [maps:get(C, Map) || C <- Cols].

bfs(Queue, Acc) ->
    case queue:out(Queue) of
        {{value, {Node, Row, Col}}, Q1} ->
            #tree_node{val = Val, left = Left, right = Right} = Node,
            NewAcc = [{Col, Row, Val} | Acc],
            Q2 = maybe_in(Left, Row + 1, Col - 1, Q1),
            Q3 = maybe_in(Right, Row + 1, Col + 1, Q2),
            bfs(Q3, NewAcc);
        {empty, _} ->
            lists:reverse(Acc)
    end.

maybe_in(null, _, _, Q) -> Q;
maybe_in(Node, R, C, Q) -> queue:in({Node, R, C}, Q).

group_entries([], Map) -> Map;
group_entries([{Col, _Row, Val} | Rest], Map) ->
    Prev = maps:get(Col, Map, []),
    UpdatedMap = maps:put(Col, Prev ++ [Val], Map),
    group_entries(Rest, UpdatedMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec vertical_traversal(root :: TreeNode.t | nil) :: [[integer]]
  def vertical_traversal(nil), do: []

  def vertical_traversal(root) do
    nodes = traverse(root, 0, 0, [])
    grouped = Enum.group_by(nodes, fn {col, _row, _val} -> col end)

    grouped
    |> Map.keys()
    |> Enum.sort()
    |> Enum.map(fn col ->
      grouped[col]
      |> Enum.sort_by(fn {_c, row, val} -> {row, val} end)
      |> Enum.map(fn {_c, _r, v} -> v end)
    end)
  end

  defp traverse(nil, _row, _col, acc), do: acc

  defp traverse(%TreeNode{val: v, left: l, right: r}, row, col, acc) do
    acc = [{col, row, v} | acc]
    acc = traverse(l, row + 1, col - 1, acc)
    traverse(r, row + 1, col + 1, acc)
  end
end
```
