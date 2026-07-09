# 0103. Binary Tree Zigzag Level Order Traversal

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        while (!q.empty()) {
            int sz = q.size();
            vector<int> level(sz);
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                int idx = leftToRight ? i : (sz - 1 - i);
                level[idx] = node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans.emplace_back(std::move(level));
            leftToRight = !leftToRight;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;
        while (!queue.isEmpty()) {
            int size = queue.size();
            Deque<Integer> level = new LinkedList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (leftToRight) {
                    level.addLast(node.val);
                } else {
                    level.addFirst(node.val);
                }
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(new ArrayList<>(level));
            leftToRight = !leftToRight;
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
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        q = deque([root])
        res = []
        left_to_right = True
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
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right
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
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result: List[List[int]] = []
        nodes = deque([root])
        left_to_right = True
        while nodes:
            level_size = len(nodes)
            level: List[int] = []
            for _ in range(level_size):
                if left_to_right:
                    node = nodes.popleft()
                    level.append(node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                else:
                    node = nodes.pop()
                    level.append(node.val)
                    # add children in reverse order to the front
                    if node.right:
                        nodes.appendleft(node.right)
                    if node.left:
                        nodes.appendleft(node.left)
            result.append(level)
            left_to_right = not left_to_right
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
int** zigzagLevelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int maxNodes = 2000; // per constraints
    struct TreeNode **queue = (struct TreeNode **)malloc(maxNodes * sizeof(struct TreeNode *));
    int front = 0, rear = 0;
    queue[rear++] = root;

    int capacityLevels = 100;
    int** result = (int **)malloc(capacityLevels * sizeof(int *));
    int* colSizes = (int *)malloc(capacityLevels * sizeof(int));

    int level = 0;
    while (front < rear) {
        int levelSize = rear - front;
        int* vals = (int *)malloc(levelSize * sizeof(int));

        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode* node = queue[front++];
            vals[i] = node->val;
            if (node->left)  queue[rear++] = node->left;
            if (node->right) queue[rear++] = node->right;
        }

        if (level % 2 == 1) {
            for (int i = 0, j = levelSize - 1; i < j; ++i, --j) {
                int tmp = vals[i];
                vals[i] = vals[j];
                vals[j] = tmp;
            }
        }

        if (level >= capacityLevels) {
            capacityLevels <<= 1;
            result = (int **)realloc(result, capacityLevels * sizeof(int *));
            colSizes = (int *)realloc(colSizes, capacityLevels * sizeof(int));
        }

        result[level] = vals;
        colSizes[level] = levelSize;
        ++level;
    }

    free(queue);
    *returnSize = level;
    *returnColumnSizes = colSizes;
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
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) return result;

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        bool leftToRight = true;

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            var level = new List<int>(levelSize);

            for (int i = 0; i < levelSize; i++) {
                var node = queue.Dequeue();
                level.Add(node.val);
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }

            if (!leftToRight) {
                level.Reverse();
            }
            result.Add(level);
            leftToRight = !leftToRight;
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
var zigzagLevelOrder = function(root) {
    if (!root) return [];
    const result = [];
    const queue = [root];
    let leftToRight = true;
    
    while (queue.length) {
        const size = queue.length;
        const level = new Array(size);
        for (let i = 0; i < size; i++) {
            const node = queue.shift();
            // place value according to current direction
            const index = leftToRight ? i : (size - 1 - i);
            level[index] = node.val;
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(level);
        leftToRight = !leftToRight;
    }
    
    return result;
};
```

## Typescript

```typescript
function zigzagLevelOrder(root: TreeNode | null): number[][] {
    if (!root) return [];
    const result: number[][] = [];
    const queue: (TreeNode | null)[] = [root];
    let leftToRight = true;

    while (queue.length > 0) {
        const levelSize = queue.length;
        const levelVals: number[] = [];

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            levelVals.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        if (!leftToRight) levelVals.reverse();
        result.push(levelVals);
        leftToRight = !leftToRight;
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
    function zigzagLevelOrder($root) {
        if ($root === null) {
            return [];
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];
        $leftToRight = true;

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

            if (!$leftToRight) {
                $level = array_reverse($level);
            }

            $result[] = $level;
            $leftToRight = !$leftToRight;
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
    func zigzagLevelOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        var result = [[Int]]()
        var queue = [TreeNode]()
        queue.append(root)
        var head = 0
        var leftToRight = true
        
        while head < queue.count {
            let levelSize = queue.count - head
            var levelVals = [Int]()
            for _ in 0..<levelSize {
                let node = queue[head]
                head += 1
                levelVals.append(node.val)
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            if !leftToRight {
                levelVals.reverse()
            }
            result.append(levelVals)
            leftToRight.toggle()
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
    fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()
        val result = mutableListOf<List<Int>>()
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        var leftToRight = true
        while (queue.isNotEmpty()) {
            val size = queue.size
            val level = IntArray(size)
            for (i in 0 until size) {
                val node = queue.removeFirst()
                val idx = if (leftToRight) i else size - 1 - i
                level[idx] = node.`val`
                node.left?.let { queue.addLast(it) }
                node.right?.let { queue.addLast(it) }
            }
            result.add(level.toList())
            leftToRight = !leftToRight
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
  List<List<int>> zigzagLevelOrder(TreeNode? root) {
    if (root == null) return [];
    Queue<TreeNode> queue = Queue();
    queue.add(root);
    bool leftToRight = true;
    List<List<int>> result = [];

    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      List<int> level = [];
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeFirst();
        level.add(node.val);
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      if (!leftToRight) {
        level = level.reversed.toList();
      }
      result.add(level);
      leftToRight = !leftToRight;
    }

    return result;
  }
}
```

## Golang

```go
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*TreeNode{root}
	leftToRight := true

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

		if !leftToRight {
			for i, j := 0, len(level)-1; i < j; i, j = i+1, j-1 {
				level[i], level[j] = level[j], level[i]
			}
		}
		result = append(result, level)
		leftToRight = !leftToRight
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

def zigzag_level_order(root)
  return [] unless root
  result = []
  queue = [root]
  left_to_right = true
  until queue.empty?
    level_size = queue.size
    level_vals = []
    level_size.times do
      node = queue.shift
      if left_to_right
        level_vals << node.val
      else
        level_vals.unshift(node.val)
      end
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << level_vals
    left_to_right = !left_to_right
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
    def zigzagLevelOrder(root: TreeNode): List[List[Int]] = {
        if (root == null) return Nil

        val queue = scala.collection.mutable.Queue[TreeNode]()
        queue.enqueue(root)

        var leftToRight = true
        val result = scala.collection.mutable.ListBuffer[List[Int]]()

        while (queue.nonEmpty) {
            val levelSize = queue.size
            val levelVals = scala.collection.mutable.ArrayBuffer[Int]()

            for (_ <- 0 until levelSize) {
                val node = queue.dequeue()
                levelVals += node.value
                if (node.left != null) queue.enqueue(node.left)
                if (node.right != null) queue.enqueue(node.right)
            }

            val ordered = if (leftToRight) levelVals.toList else levelVals.reverse.toList
            result += ordered
            leftToRight = !leftToRight
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
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        if root.is_none() {
            return result;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());
        let mut left_to_right = true;
        while !queue.is_empty() {
            let level_len = queue.len();
            let mut level_vals = Vec::with_capacity(level_len);
            for _ in 0..level_len {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    level_vals.push(node_ref.val);
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
            if !left_to_right {
                level_vals.reverse();
            }
            result.push(level_vals);
            left_to_right = !left_to_right;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (zigzag-level-order root)
  (-> (or/c tree-node? #f) (listof (listof exact-integer?)))
  (if (not root)
      '()
      (let loop ((current (list root))
                 (ltr #t)
                 (acc '()))
        (if (null? current)
            (reverse acc)
            (let* ((vals (map tree-node-val current))
                   (ordered (if ltr vals (reverse vals)))
                   (next
                     (for/list ([node current]
                                [child (in-list (list (tree-node-left node) (tree-node-right node)))]
                                #:when child)
                       child)))
              (loop next (not ltr) (cons ordered acc)))))))
```

## Erlang

```erlang
-spec zigzag_level_order(Root :: #tree_node{} | null) -> [[integer()]].
zigzag_level_order(null) ->
    [];
zigzag_level_order(Root) ->
    bfs([Root], true, []).

bfs([], _LeftToRight, Acc) ->
    lists:reverse(Acc);
bfs(LevelNodes, LeftToRight, Acc) ->
    Values = [Node#tree_node.val || Node <- LevelNodes],
    OrderedValues = case LeftToRight of
        true -> Values;
        false -> lists:reverse(Values)
    end,
    Children = [Child ||
                Node <- LevelNodes,
                Child <- [Node#tree_node.left, Node#tree_node.right],
                Child =/= null],
    bfs(Children, not LeftToRight, [OrderedValues | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec zigzag_level_order(root :: TreeNode.t | nil) :: [[integer]]
  def zigzag_level_order(nil), do: []

  def zigzag_level_order(root) do
    bfs(:queue.from_list([root]), true, [])
    |> Enum.reverse()
  end

  defp bfs(queue, left_to_right, acc) do
    if :queue.is_empty(queue) do
      acc
    else
      size = :queue.len(queue)
      {vals, next_queue} = get_level(queue, size, [], [])
      vals = if left_to_right, do: vals, else: Enum.reverse(vals)
      bfs(next_queue, not left_to_right, [vals | acc])
    end
  end

  defp get_level(queue, 0, vals_acc, new_q) do
    {Enum.reverse(vals_acc), new_q}
  end

  defp get_level(queue, n, vals_acc, new_q) do
    {{:value, node}, q1} = :queue.out(queue)

    new_q2 =
      case node.left do
        nil -> new_q
        l -> :queue.in(l, new_q)
      end

    new_q3 =
      case node.right do
        nil -> new_q2
        r -> :queue.in(r, new_q2)
      end

    get_level(q1, n - 1, [node.val | vals_acc], new_q3)
  end
end
```
