# 0102. Binary Tree Level Order Traversal

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
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
            result.emplace_back(std::move(level));
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>(size);
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
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
    def levelOrder(self, root):
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
        return result
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_len = len(queue)
            level_vals = []
            for _ in range(level_len):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_vals)
        return result
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
int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    const int MAX_NODES = 2000;               // per problem constraints
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * MAX_NODES);
    int head = 0, tail = 0;
    queue[tail++] = root;
    
    int** result = (int **)malloc(sizeof(int *) * MAX_NODES);
    *returnColumnSizes = (int *)malloc(sizeof(int) * MAX_NODES);
    
    int level = 0;
    while (head < tail) {
        int sz = tail - head;                 // number of nodes at current level
        (*returnColumnSizes)[level] = sz;
        result[level] = (int *)malloc(sizeof(int) * sz);
        
        for (int i = 0; i < sz; ++i) {
            struct TreeNode *node = queue[head++];
            result[level][i] = node->val;
            if (node->left)  queue[tail++] = node->left;
            if (node->right) queue[tail++] = node->right;
        }
        level++;
    }
    
    free(queue);
    *returnSize = level;
    return result;
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
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) return result;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            var currentLevel = new List<int>(levelSize);
            for (int i = 0; i < levelSize; i++) {
                var node = queue.Dequeue();
                currentLevel.Add(node.val);
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            result.Add(currentLevel);
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
var levelOrder = function(root) {
    if (!root) return [];
    const result = [];
    const queue = [root];
    
    while (queue.length) {
        const levelSize = queue.length;
        const currentLevel = [];
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            currentLevel.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(currentLevel);
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

function levelOrder(root: TreeNode | null): number[][] {
    const result: number[][] = [];
    if (!root) return result;
    
    const queue: TreeNode[] = [root];
    
    while (queue.length > 0) {
        const levelSize = queue.length;
        const currentLevel: number[] = [];
        
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            currentLevel.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        result.push(currentLevel);
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
     * @return integer[][]
     */
    function levelOrder($root) {
        if ($root === null) {
            return [];
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $currentLevel = [];

            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $currentLevel[] = $node->val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            $result[] = $currentLevel;
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
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        var result = [[Int]]()
        var queue = [TreeNode]()
        var index = 0
        queue.append(root)
        
        while index < queue.count {
            let levelSize = queue.count - index
            var currentLevel = [Int]()
            for _ in 0..<levelSize {
                let node = queue[index]
                index += 1
                currentLevel.append(node.val)
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            result.append(currentLevel)
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
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()
        val result = mutableListOf<List<Int>>()
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val size = queue.size
            val level = mutableListOf<Int>()
            repeat(size) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            result.add(level)
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
  List<List<int>> levelOrder(TreeNode? root) {
    if (root == null) return [];
    List<List<int>> result = [];
    Queue<TreeNode> queue = Queue();
    queue.add(root);
    while (queue.isNotEmpty) {
      int size = queue.length;
      List<int> level = [];
      for (int i = 0; i < size; i++) {
        TreeNode node = queue.removeFirst();
        level.add(node.val);
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      result.add(level);
    }
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
func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		levelVals := make([]int, 0, levelSize)
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			levelVals = append(levelVals, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		result = append(result, levelVals)
	}
	return result
}
```

## Ruby

```ruby
def level_order(root)
  return [] unless root
  result = []
  queue = [root]
  until queue.empty?
    level_size = queue.size
    level = []
    level_size.times do
      node = queue.shift
      level << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << level
  end
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
    def levelOrder(root: TreeNode): List[List[Int]] = {
        if (root == null) return List.empty[List[Int]]
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val queue = scala.collection.mutable.Queue[TreeNode]()
        queue.enqueue(root)
        while (queue.nonEmpty) {
            val levelSize = queue.size
            val levelVals = scala.collection.mutable.ArrayBuffer[Int]()
            for (_ <- 0 until levelSize) {
                val node = queue.dequeue()
                levelVals += node.value
                if (node.left != null) queue.enqueue(node.left)
                if (node.right != null) queue.enqueue(node.right)
            }
            result += levelVals.toList
        }
        result.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut queue = VecDeque::new();

        if let Some(node) = root {
            queue.push_back(node);
        } else {
            return result;
        }

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut level = Vec::with_capacity(level_size);

            for _ in 0..level_size {
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

            result.push(level);
        }

        result
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

(define/contract (level-order root)
  (-> (or/c tree-node? #f) (listof (listof exact-integer?)))
  (if (not root)
      '()
      (let loop ((nodes (list root)) (result '()))
        (if (null? nodes)
            (reverse result)
            (let* ((vals (map tree-node-val nodes))
                   (children
                    (apply append
                           (map (lambda (n)
                                  (filter identity
                                          (list (tree-node-left n) (tree-node-right n))))
                                nodes))))
              (loop children (cons vals result)))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec level_order(Root :: #tree_node{} | null) -> [[integer()]].
level_order(null) ->
    [];
level_order(Root) ->
    bfs([Root], []).

bfs([], Acc) ->
    lists:reverse(Acc);
bfs(LevelNodes, Acc) ->
    Values = [Node#tree_node.val || Node <- LevelNodes],
    NextLevel = collect_children(LevelNodes),
    bfs(NextLevel, [Values | Acc]).

collect_children([]) -> [];
collect_children([Node|Rest]) ->
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    case {Left, Right} of
        {null, null} ->
            collect_children(Rest);
        {L, null} when L =/= null ->
            [L | collect_children(Rest)];
        {null, R} when R =/= null ->
            [R | collect_children(Rest)];
        {L, R} ->
            [L, R | collect_children(Rest)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec level_order(root :: TreeNode.t | nil) :: [[integer]]
  def level_order(nil), do: []

  def level_order(root) do
    bfs(:queue.from_list([root]), [])
  end

  defp bfs(queue, result) do
    if :queue.is_empty(queue) do
      Enum.reverse(result)
    else
      {level_vals, next_queue} = process_level(queue, [], :queue.new())
      bfs(next_queue, [Enum.reverse(level_vals) | result])
    end
  end

  defp process_level(queue, vals_acc, next_q) do
    case :queue.out(queue) do
      {:empty, _} ->
        {vals_acc, next_q}

      {{:value, node}, rest_queue} ->
        vals_acc = [node.val | vals_acc]

        next_q =
          case node.left do
            nil -> next_q
            left -> :queue.in(left, next_q)
          end

        next_q =
          case node.right do
            nil -> next_q
            right -> :queue.in(right, next_q)
          end

        process_level(rest_queue, vals_acc, next_q)
    end
  end
end
```
