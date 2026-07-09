# 1161. Maximum Level Sum of a Binary Tree

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
    int maxLevelSum(TreeNode* root) {
        if (!root) return 0;
        std::queue<TreeNode*> q;
        q.push(root);
        long long maxSum = LLONG_MIN;
        int answer = 1;
        int level = 0;
        while (!q.empty()) {
            ++level;
            long long sum = 0;
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                sum += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            if (sum > maxSum) {
                maxSum = sum;
                answer = level;
            }
        }
        return answer;
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
    public int maxLevelSum(TreeNode root) {
        java.util.Queue<TreeNode> queue = new java.util.ArrayDeque<>();
        queue.offer(root);
        long maxSum = Long.MIN_VALUE;
        int answerLevel = 1;
        int currentLevel = 0;

        while (!queue.isEmpty()) {
            currentLevel++;
            int size = queue.size();
            long levelSum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                levelSum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            if (levelSum > maxSum) {
                maxSum = levelSum;
                answerLevel = currentLevel;
            }
        }

        return answerLevel;
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
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque

        if not root:
            return 0

        q = deque([root])
        level = 0
        max_sum = float('-inf')
        answer = 1

        while q:
            level += 1
            cur_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                answer = level

        return answer
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_sum = float('-inf')
        answer = 1
        level = 0
        
        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
                
        return answer
```

## C

```c
#include <stdlib.h>
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxLevelSum(struct TreeNode* root) {
    if (!root) return 0;

    int capacity = 10005;                     // enough for given constraints
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * capacity);
    int front = 0, rear = 0;
    queue[rear++] = root;

    long long maxSum = LLONG_MIN;
    int answerLevel = 1;
    int currentLevel = 0;

    while (front < rear) {
        ++currentLevel;
        int levelSize = rear - front;
        long long sum = 0;
        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode *node = queue[front++];
            sum += node->val;
            if (node->left)  queue[rear++] = node->left;
            if (node->right) queue[rear++] = node->right;
        }
        if (sum > maxSum) {
            maxSum = sum;
            answerLevel = currentLevel;
        }
    }

    free(queue);
    return answerLevel;
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
    public int MaxLevelSum(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        long maxSum = long.MinValue;
        int answerLevel = 1;
        int currentLevel = 0;

        while (queue.Count > 0) {
            currentLevel++;
            int levelSize = queue.Count;
            long levelSum = 0;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                levelSum += node.val;

                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }

            if (levelSum > maxSum) {
                maxSum = levelSum;
                answerLevel = currentLevel;
            }
        }

        return answerLevel;
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
 * @return {number}
 */
var maxLevelSum = function(root) {
    if (!root) return 0;
    let maxSum = -Infinity;
    let answer = 1;
    let level = 0;
    let queue = [root];
    
    while (queue.length > 0) {
        level++;
        let sum = 0;
        const nextLevel = [];
        for (const node of queue) {
            sum += node.val;
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        if (sum > maxSum) {
            maxSum = sum;
            answer = level;
        }
        queue = nextLevel;
    }
    
    return answer;
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

function maxLevelSum(root: TreeNode | null): number {
    if (!root) return 0;
    let maxSum = -Infinity;
    let answer = 1;
    const queue: TreeNode[] = [root];
    let level = 0;

    while (queue.length > 0) {
        level++;
        const size = queue.length;
        let sum = 0;
        for (let i = 0; i < size; i++) {
            const node = queue.shift()!;
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        if (sum > maxSum) {
            maxSum = sum;
            answer = level;
        }
    }

    return answer;
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
     * @return Integer
     */
    function maxLevelSum($root) {
        if ($root === null) {
            return 0;
        }

        $queue = new SplQueue();
        $queue->enqueue($root);

        $maxSum = PHP_INT_MIN;
        $answer = 1;
        $level = 0;

        while (!$queue->isEmpty()) {
            $level++;
            $size = $queue->count();
            $sum = 0;

            for ($i = 0; $i < $size; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $sum += $node->val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            if ($sum > $maxSum) {
                $maxSum = $sum;
                $answer = $level;
            }
        }

        return $answer;
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
    func maxLevelSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var queue: [TreeNode] = [root]
        var index = 0               // points to the current front of the queue
        var level = 0
        var maxSum = Int.min
        var answer = 1
        
        while index < queue.count {
            level += 1
            let levelSize = queue.count - index   // nodes at the current level
            var sum = 0
            for _ in 0..<levelSize {
                let node = queue[index]
                index += 1
                sum += node.val
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            if sum > maxSum {
                maxSum = sum
                answer = level
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun maxLevelSum(root: TreeNode?): Int {
        if (root == null) return 0
        val queue = ArrayDeque<TreeNode>()
        queue.addLast(root)
        var level = 0
        var answer = 1
        var maxSum = Long.MIN_VALUE

        while (queue.isNotEmpty()) {
            level++
            var sum = 0L
            repeat(queue.size) {
                val node = queue.removeFirst()
                sum += node.`val`.toLong()
                node.left?.let { queue.addLast(it) }
                node.right?.let { queue.addLast(it) }
            }
            if (sum > maxSum) {
                maxSum = sum
                answer = level
            }
        }
        return answer
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
  int maxLevelSum(TreeNode? root) {
    if (root == null) return 0;

    List<TreeNode> queue = [root];
    int idx = 0;          // points to the current node in the queue
    int level = 0;
    int answer = 1;
    int maxSum = root.val;

    while (idx < queue.length) {
      level++;
      int nodesInLevel = queue.length - idx;
      int sum = 0;

      for (int i = 0; i < nodesInLevel; i++) {
        TreeNode node = queue[idx++];
        sum += node.val;
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }

      if (sum > maxSum) {
        maxSum = sum;
        answer = level;
      }
    }

    return answer;
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
func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	maxSum := root.Val
	ans := 1
	level := 0

	for len(queue) > 0 {
		level++
		sum := 0
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if sum > maxSum {
			maxSum = sum
			ans = level
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_level_sum(root)
  return 0 unless root
  queue = [root]
  level = 0
  max_sum = -(1 << 60)
  answer = 1
  until queue.empty?
    level += 1
    sum = 0
    size = queue.size
    size.times do
      node = queue.shift
      sum += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    if sum > max_sum
      max_sum = sum
      answer = level
    end
  end
  answer
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
    def maxLevelSum(root: TreeNode): Int = {
        import scala.collection.mutable.Queue
        val q = Queue[TreeNode]()
        q.enqueue(root)
        var level = 0
        var maxSum: Long = Long.MinValue
        var answer = 1

        while (q.nonEmpty) {
            level += 1
            var sum: Long = 0L
            val size = q.size
            for (_ <- 0 until size) {
                val node = q.dequeue()
                sum += node.value
                if (node.left != null) q.enqueue(node.left)
                if (node.right != null) q.enqueue(node.right)
            }
            if (sum > maxSum) {
                maxSum = sum
                answer = level
            }
        }
        answer
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        let mut level = 0i32;
        let mut ans = 1i32;
        let mut max_sum: i64 = i64::MIN;

        while !queue.is_empty() {
            level += 1;
            let size = queue.len();
            let mut sum: i64 = 0;
            for _ in 0..size {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    sum += node_ref.val as i64;
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }
            if sum > max_sum {
                max_sum = sum;
                ans = level;
            }
        }

        ans
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

(define/contract (max-level-sum root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let loop ((level 1)
                 (nodes (list root))
                 (best-level 1)
                 (best-sum (tree-node-val root)))
        (if (null? nodes)
            best-level
            (let* ((level-sum (foldl (lambda (node acc) (+ acc (tree-node-val node))) 0 nodes))
                   (children (foldl (lambda (node acc)
                                      (let ((left (tree-node-left node))
                                            (right (tree-node-right node)))
                                        (if left (cons left acc) acc)
                                        (if right (cons right acc) acc)))
                                    '()
                                    nodes))
                   (new-best-sum (if (> level-sum best-sum) level-sum best-sum))
                   (new-best-level (if (> level-sum best-sum) level best-level)))
              (loop (+ level 1)
                    (reverse children)
                    new-best-level
                    new-best-sum))))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec max_level_sum(Root :: #tree_node{} | null) -> integer().
max_level_sum(null) ->
    0;
max_level_sum(Root) ->
    bfs(0, [Root], -1000000000000, 0).

bfs(_Level, [], _MaxSum, Ans) ->
    Ans;
bfs(Level, Queue, MaxSum, Ans) ->
    {Sum, ChildrenRev} = process_nodes(Queue, 0, []),
    NewLevel = Level + 1,
    {NewMax, NewAns} =
        if Sum > MaxSum -> {Sum, NewLevel};
           true         -> {MaxSum, Ans}
        end,
    bfs(NewLevel, lists:reverse(ChildrenRev), NewMax, NewAns).

process_nodes([], SumAcc, ChildrenAcc) ->
    {SumAcc, ChildrenAcc};
process_nodes([Node | Rest], SumAcc, ChildrenAcc) ->
    case Node of
        null ->
            process_nodes(Rest, SumAcc, ChildrenAcc);
        #tree_node{} = T ->
            NewSum = SumAcc + T#tree_node.val,
            ChildAcc1 = case T#tree_node.left of
                            null -> ChildrenAcc;
                            L    -> [L | ChildrenAcc]
                        end,
            ChildAcc2 = case T#tree_node.right of
                            null -> ChildAcc1;
                            R    -> [R | ChildAcc1]
                        end,
            process_nodes(Rest, NewSum, ChildAcc2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_level_sum(root :: TreeNode.t() | nil) :: integer
  def max_level_sum(nil), do: 0

  def max_level_sum(root) do
    bfs([root], 1, root.val, 1)
  end

  defp bfs([], _level, _max_sum, ans), do: ans

  defp bfs(nodes, level, max_sum, ans) do
    sum =
      Enum.reduce(nodes, 0, fn %TreeNode{val: v}, acc ->
        acc + v
      end)

    {new_max, new_ans} =
      if sum > max_sum do
        {sum, level}
      else
        {max_sum, ans}
      end

    next_nodes =
      nodes
      |> Enum.flat_map(fn %TreeNode{left: l, right: r} ->
        [l, r] |> Enum.filter(& &1)
      end)

    bfs(next_nodes, level + 1, new_max, new_ans)
  end
end
```
