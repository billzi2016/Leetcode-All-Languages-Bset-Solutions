# 0107. Binary Tree Level Order Traversal II

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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (!root) return {};
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> res;
        while (!q.empty()) {
            int sz = q.size();
            vector<int> level;
            level.reserve(sz);
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            res.push_back(std::move(level));
        }
        reverse(res.begin(), res.end());
        return res;
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> result = new LinkedList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>(size);
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.addFirst(level);
        }
        return result;
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
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_vals)
        return result[::-1]
```

## Python3

```python
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result[::-1]
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
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrderBottom(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    const int MAX_NODES = 2000;               // per constraints
    struct TreeNode **queue = malloc(MAX_NODES * sizeof(struct TreeNode*));
    int front = 0, rear = 0;
    queue[rear++] = root;

    // temporary storage for each level (top-down)
    int **levelsVals = malloc(MAX_NODES * sizeof(int*));
    int *colSizesTmp = malloc(MAX_NODES * sizeof(int));
    int levelsCount = 0;

    while (front < rear) {
        int sz = rear - front;                 // nodes in current level
        int *vals = malloc(sz * sizeof(int));
        for (int i = 0; i < sz; ++i) {
            struct TreeNode *node = queue[front++];
            vals[i] = node->val;
            if (node->left)  queue[rear++] = node->left;
            if (node->right) queue[rear++] = node->right;
        }
        levelsVals[levelsCount] = vals;
        colSizesTmp[levelsCount] = sz;
        ++levelsCount;
    }

    // prepare bottom-up result
    int **result = malloc(levelsCount * sizeof(int*));
    int *colSizesRes = malloc(levelsCount * sizeof(int));
    for (int i = 0; i < levelsCount; ++i) {
        result[i] = levelsVals[levelsCount - 1 - i];
        colSizesRes[i] = colSizesTmp[levelsCount - 1 - i];
    }

    // clean up temporary structures
    free(levelsVals);
    free(colSizesTmp);
    free(queue);

    *returnSize = levelsCount;
    *returnColumnSizes = colSizesRes;
    return result;
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
    public IList<IList<int>> LevelOrderBottom(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) return result;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            var level = new List<int>(levelSize);
            for (int i = 0; i < levelSize; i++) {
                var node = queue.Dequeue();
                level.Add(node.val);
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            result.Add(level);
        }

        result.Reverse();
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
var levelOrderBottom = function(root) {
    if (!root) return [];
    const queue = [root];
    const result = [];
    let head = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head;
        const level = [];
        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];
            level.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.unshift(level); // prepend to get bottom-up order
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

function levelOrderBottom(root: TreeNode | null): number[][] {
    if (!root) return [];
    const result: number[][] = [];
    const queue: TreeNode[] = [root];
    
    while (queue.length > 0) {
        const size = queue.length;
        const level: number[] = [];
        for (let i = 0; i < size; i++) {
            const node = queue.shift()!;
            level.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(level);
    }
    
    return result.reverse();
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
    function levelOrderBottom($root) {
        if ($root === null) {
            return [];
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $level = [];

            for ($i = 0; $i < $size; $i++) {
                $node = $queue->dequeue();
                $level[] = $node->val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            array_unshift($result, $level); // prepend to achieve bottom‑up order
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
    func levelOrderBottom(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        var queue: [TreeNode] = [root]
        var result: [[Int]] = []
        
        while !queue.isEmpty {
            var levelVals: [Int] = []
            var nextQueue: [TreeNode] = []
            
            for node in queue {
                levelVals.append(node.val)
                if let left = node.left { nextQueue.append(left) }
                if let right = node.right { nextQueue.append(right) }
            }
            
            result.append(levelVals)
            queue = nextQueue
        }
        
        return result.reversed()
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
    fun levelOrderBottom(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()
        val result = mutableListOf<MutableList<Int>>()
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            val level = mutableListOf<Int>()
            repeat(levelSize) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            result.add(0, level) // prepend to achieve bottom‑up order
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

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
  List<List<int>> levelOrderBottom(TreeNode? root) {
    if (root == null) return [];
    final Queue<TreeNode> queue = Queue<TreeNode>();
    queue.add(root);
    final List<List<int>> result = [];

    while (queue.isNotEmpty) {
      int size = queue.length;
      final List<int> level = <int>[];
      for (int i = 0; i < size; i++) {
        final TreeNode node = queue.removeFirst();
        level.add(node.val);
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      result.add(level);
    }

    return result.reversed.toList();
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
func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		level := make([]int, 0, size)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			level = append(level, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, level)
	}
	// reverse result for bottom-up order
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return result
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

def level_order_bottom(root)
  return [] unless root
  queue = [root]
  result = []
  until queue.empty?
    level = []
    size = queue.size
    size.times do
      node = queue.shift
      level << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << level
  end
  result.reverse
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
    import scala.collection.mutable.{Queue, ListBuffer}
    
    def levelOrderBottom(root: TreeNode): List[List[Int]] = {
        if (root == null) return Nil
        val q: Queue[TreeNode] = Queue(root)
        var result: List[List[Int]] = Nil
        
        while (q.nonEmpty) {
            val size = q.size
            val levelBuf = new ListBuffer[Int]()
            for (_ <- 0 until size) {
                val node = q.dequeue()
                levelBuf += node.value
                if (node.left != null) q.enqueue(node.left)
                if (node.right != null) q.enqueue(node.right)
            }
            result = levelBuf.toList :: result   // prepend to achieve bottom‑up order
        }
        result
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        if root.is_none() {
            return res;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        while !queue.is_empty() {
            let level_len = queue.len();
            let mut level = Vec::with_capacity(level_len);
            for _ in 0..level_len {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    level.push(node_ref.val);
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
            res.push(level);
        }

        res.reverse();
        res
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

(define/contract (level-order-bottom root)
  (-> (or/c tree-node? #f) (listof (listof exact-integer?)))
  (if (not root)
      '()
      (letrec ((collect-children
                (lambda (nodes)
                  (if (null? nodes)
                      '()
                      (apply append
                             (for/list ((node nodes))
                               (filter identity
                                       (list (tree-node-left node)
                                             (tree-node-right node)))))))))
        (let loop ((curr (list root)) (acc '()))
          (if (null? curr)
              (reverse acc)
              (let* ((vals (map tree-node-val curr))
                     (next (collect-children curr)))
                (loop next (cons vals acc))))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec level_order_bottom(Root :: #tree_node{} | null) -> [[integer()]].
level_order_bottom(null) ->
    [];
level_order_bottom(Root) ->
    Levels = bfs([Root], []),
    lists:reverse(Levels).

bfs([], Acc) ->
    Acc;
bfs(CurrentLevel, Acc) ->
    Values = [Node#tree_node.val || Node <- CurrentLevel],
    NextLevel = collect_children(CurrentLevel, []),
    bfs(NextLevel, [Values | Acc]).

collect_children([], Acc) ->
    Acc;
collect_children([Node|Rest], Acc) ->
    Acc1 = case Node#tree_node.left of
               null -> Acc;
               L -> Acc ++ [L]
           end,
    Acc2 = case Node#tree_node.right of
               null -> Acc1;
               R -> Acc1 ++ [R]
           end,
    collect_children(Rest, Acc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec level_order_bottom(root :: TreeNode.t | nil) :: [[integer]]
  def level_order_bottom(root) do
    root
    |> traverse(0, [])
    |> Enum.reverse()
  end

  defp traverse(nil, _depth, acc), do: acc

  defp traverse(%TreeNode{val: v, left: l, right: r}, depth, acc) do
    acc =
      if length(acc) == depth do
        acc ++ [[]]
      else
        acc
      end

    updated = List.update_at(acc, depth, fn lst -> lst ++ [v] end)

    acc_left = traverse(l, depth + 1, updated)
    traverse(r, depth + 1, acc_left)
  end
end
```
