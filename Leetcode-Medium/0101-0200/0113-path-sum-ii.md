# 0113. Path Sum II

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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> current;
        dfs(root, targetSum, current, result);
        return result;
    }
private:
    void dfs(TreeNode* node, int remain, vector<int>& path, vector<vector<int>>& res) {
        if (!node) return;
        path.push_back(node->val);
        remain -= node->val;
        if (!node->left && !node->right && remain == 0) {
            res.push_back(path);
        } else {
            dfs(node->left, remain, path, res);
            dfs(node->right, remain, path, res);
        }
        path.pop_back();
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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        dfs(root, targetSum, new ArrayList<>(), result);
        return result;
    }

    private void dfs(TreeNode node, int remaining, List<Integer> path, List<List<Integer>> result) {
        if (node == null) return;

        path.add(node.val);
        remaining -= node.val;

        // Check leaf
        if (node.left == null && node.right == null && remaining == 0) {
            result.add(new ArrayList<>(path));
        } else {
            dfs(node.left, remaining, path, result);
            dfs(node.right, remaining, path, result);
        }

        // backtrack
        path.remove(path.size() - 1);
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
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def dfs(node, remaining):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                res.append(list(path))
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()

        dfs(root, targetSum)
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res: List[List[int]] = []
        if not root:
            return res
        
        def dfs(node: TreeNode, cur_sum: int, path: List[int]) -> None:
            cur_sum += node.val
            path.append(node.val)
            
            # leaf check
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    res.append(path.copy())
            else:
                if node.left:
                    dfs(node.left, cur_sum, path)
                if node.right:
                    dfs(node.right, cur_sum, path)
            path.pop()
        
        dfs(root, 0, [])
        return res
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

struct Result {
    int **paths;
    int *colSizes;
    int size;
    int cap;
};

static void dfs(struct TreeNode* node, int remain, int *path, int depth, struct Result *res) {
    if (!node) return;
    path[depth] = node->val;
    int newRemain = remain - node->val;

    if (!node->left && !node->right) { // leaf
        if (newRemain == 0) {
            if (res->size == res->cap) {
                res->cap = res->cap ? res->cap * 2 : 1;
                res->paths = realloc(res->paths, sizeof(int*) * res->cap);
                res->colSizes = realloc(res->colSizes, sizeof(int) * res->cap);
            }
            int *copy = malloc(sizeof(int) * (depth + 1));
            memcpy(copy, path, sizeof(int) * (depth + 1));
            res->paths[res->size] = copy;
            res->colSizes[res->size] = depth + 1;
            res->size++;
        }
        return;
    }

    dfs(node->left, newRemain, path, depth + 1, res);
    dfs(node->right, newRemain, path, depth + 1, res);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pathSum(struct TreeNode* root, int targetSum, int* returnSize, int*** returnColumnSizes) {
    // Adjust signature to match problem statement
    (void)returnColumnSizes; // placeholder to avoid unused warning if not needed
    struct Result res;
    res.paths = NULL;
    res.colSizes = NULL;
    res.size = 0;
    res.cap = 0;

    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int maxDepth = 5000; // as per constraints
    int *stack = malloc(sizeof(int) * maxDepth);
    dfs(root, targetSum, stack, 0, &res);
    free(stack);

    *returnSize = res.size;
    *returnColumnSizes = res.colSizes;
    return res.paths;
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
    private IList<IList<int>> result;
    private List<int> path;
    private int target;

    public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
        result = new List<IList<int>>();
        path = new List<int>();
        target = targetSum;
        DFS(root, 0);
        return result;
    }

    private void DFS(TreeNode node, int currentSum) {
        if (node == null) return;

        path.Add(node.val);
        currentSum += node.val;

        if (node.left == null && node.right == null) {
            if (currentSum == target) {
                result.Add(new List<int>(path));
            }
        } else {
            DFS(node.left, currentSum);
            DFS(node.right, currentSum);
        }

        path.RemoveAt(path.Count - 1);
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
 * @param {number} targetSum
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
    const result = [];
    const path = [];

    function dfs(node, remaining) {
        if (!node) return;
        path.push(node.val);
        remaining -= node.val;

        if (!node.left && !node.right && remaining === 0) {
            result.push([...path]);
        } else {
            dfs(node.left, remaining);
            dfs(node.right, remaining);
        }

        path.pop();
    }

    dfs(root, targetSum);
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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    const result: number[][] = [];
    const path: number[] = [];

    function dfs(node: TreeNode | null, remaining: number): void {
        if (!node) return;
        path.push(node.val);
        remaining -= node.val;

        if (!node.left && !node.right && remaining === 0) {
            result.push([...path]);
        } else {
            dfs(node.left, remaining);
            dfs(node.right, remaining);
        }

        path.pop();
    }

    dfs(root, targetSum);
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
     * @param Integer $targetSum
     * @return Integer[][]
     */
    function pathSum($root, $targetSum) {
        $result = [];
        $path = [];
        $this->dfs($root, $targetSum, $path, $result);
        return $result;
    }

    private function dfs($node, $remaining, &$path, &$result) {
        if ($node === null) {
            return;
        }
        $path[] = $node->val;
        $remaining -= $node->val;

        if ($node->left === null && $node->right === null) {
            if ($remaining == 0) {
                $result[] = $path;
            }
        } else {
            if ($node->left !== null) {
                $this->dfs($node->left, $remaining, $path, $result);
            }
            if ($node->right !== null) {
                $this->dfs($node->right, $remaining, $path, $result);
            }
        }

        array_pop($path);
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
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> [[Int]] {
        var result = [[Int]]()
        var path = [Int]()
        
        func dfs(_ node: TreeNode?, _ remaining: Int) {
            guard let node = node else { return }
            path.append(node.val)
            
            if node.left == nil && node.right == nil && remaining == node.val {
                result.append(path)
            } else {
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)
            }
            
            path.removeLast()
        }
        
        dfs(root, targetSum)
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
    fun pathSum(root: TreeNode?, targetSum: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()
        fun dfs(node: TreeNode?, remain: Int) {
            if (node == null) return
            path.add(node.`val`)
            val newRemain = remain - node.`val`
            if (node.left == null && node.right == null && newRemain == 0) {
                result.add(ArrayList(path))
            } else {
                dfs(node.left, newRemain)
                dfs(node.right, newRemain)
            }
            path.removeAt(path.size - 1)
        }
        dfs(root, targetSum)
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
  List<List<int>> pathSum(TreeNode? root, int targetSum) {
    final List<List<int>> result = [];
    final List<int> path = [];

    void dfs(TreeNode? node, int remaining) {
      if (node == null) return;
      path.add(node.val);
      if (node.left == null && node.right == null && remaining == node.val) {
        result.add(List.from(path));
      } else {
        dfs(node.left, remaining - node.val);
        dfs(node.right, remaining - node.val);
      }
      path.removeLast();
    }

    dfs(root, targetSum);
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
func pathSum(root *TreeNode, targetSum int) [][]int {
	var result [][]int
	var dfs func(node *TreeNode, remaining int, path []int)
	dfs = func(node *TreeNode, remaining int, path []int) {
		if node == nil {
			return
		}
		path = append(path, node.Val)
		if node.Left == nil && node.Right == nil && node.Val == remaining {
			tmp := make([]int, len(path))
			copy(tmp, path)
			result = append(result, tmp)
			return
		}
		dfs(node.Left, remaining-node.Val, path)
		dfs(node.Right, remaining-node.Val, path)
	}
	dfs(root, targetSum, []int{})
	return result
}
```

## Ruby

```ruby
def path_sum(root, target_sum)
  result = []
  dfs = lambda do |node, remaining, path|
    return unless node
    path << node.val
    new_remaining = remaining - node.val
    if node.left.nil? && node.right.nil? && new_remaining == 0
      result << path.clone
    else
      dfs.call(node.left, new_remaining, path)
      dfs.call(node.right, new_remaining, path)
    end
    path.pop
  end
  dfs.call(root, target_sum, [])
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
    def pathSum(root: TreeNode, targetSum: Int): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val currentPath = scala.collection.mutable.ArrayBuffer[Int]()

        def dfs(node: TreeNode, remaining: Int): Unit = {
            if (node == null) return
            currentPath.append(node.value)
            val newRemaining = remaining - node.value

            if (node.left == null && node.right == null) {
                if (newRemaining == 0) {
                    result += currentPath.toList
                }
            } else {
                dfs(node.left, newRemaining)
                dfs(node.right, newRemaining)
            }

            currentPath.remove(currentPath.size - 1)
        }

        dfs(root, targetSum)
        result.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> Vec<Vec<i32>> {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>,
               remain: i32,
               path: &mut Vec<i32>,
               out: &mut Vec<Vec<i32>>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                let val = n.val;
                path.push(val);
                let new_remain = remain - val;
                if n.left.is_none() && n.right.is_none() {
                    if new_remain == 0 {
                        out.push(path.clone());
                    }
                } else {
                    dfs(&n.left, new_remain, path, out);
                    dfs(&n.right, new_remain, path, out);
                }
                path.pop();
            }
        }

        let mut result = Vec::new();
        let mut cur_path = Vec::new();
        dfs(&root, target_sum, &mut cur_path, &mut result);
        result
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (path-sum root targetSum)
  (-> (or/c tree-node? #f) exact-integer? (listof (listof exact-integer?)))
  (letrec ((dfs
            (lambda (node remaining path)
              (if (not node)
                  '()
                  (let* ((new-remaining (- remaining (tree-node-val node)))
                         (new-path (cons (tree-node-val node) path)))
                    (if (and (not (tree-node-left node))
                             (not (tree-node-right node))) ; leaf
                        (if (= new-remaining 0)
                            (list (reverse new-path))
                            '())
                        (append (dfs (tree-node-left node) new-remaining new-path)
                                (dfs (tree-node-right node) new-remaining new-path))))))))
    (dfs root targetSum '())))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec path_sum(Root :: #tree_node{} | null, TargetSum :: integer()) -> [[integer()]].
path_sum(null, _Target) ->
    [];
path_sum(Root, TargetSum) ->
    Res = traverse(Root, TargetSum, [], []),
    lists:reverse(Res).

traverse(null, _Remain, _PathAcc, Acc) ->
    Acc;
traverse(#tree_node{val = Val, left = Left, right = Right}, Remain, PathAcc, Acc) ->
    NewPath = [Val | PathAcc],
    NewRemain = Remain - Val,
    case {Left == null, Right == null} of
        {true, true} ->
            if NewRemain == 0 ->
                    [lists:reverse(NewPath) | Acc];
               true -> Acc
            end;
        _ ->
            Acc1 = traverse(Left, NewRemain, NewPath, Acc),
            traverse(Right, NewRemain, NewPath, Acc1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec path_sum(root :: TreeNode.t | nil, target_sum :: integer) :: [[integer]]
  def path_sum(nil, _target_sum), do: []

  def path_sum(root, target_sum) do
    dfs(root, target_sum, [], [])
    |> Enum.reverse()
  end

  defp dfs(nil, _rem, _path, acc), do: acc

  defp dfs(%TreeNode{val: v, left: l, right: r}, rem, path, acc) do
    new_rem = rem - v
    new_path = [v | path]

    if l == nil and r == nil do
      if new_rem == 0 do
        [[Enum.reverse(new_path)] | acc]
      else
        acc
      end
    else
      acc1 = dfs(l, new_rem, new_path, acc)
      dfs(r, new_rem, new_path, acc1)
    end
  end
end
```
