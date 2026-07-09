# 1609. Even Odd Tree

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
    bool isEvenOddTree(TreeNode* root) {
        if (!root) return true;
        std::queue<TreeNode*> q;
        q.push(root);
        bool evenLevel = true; // level 0 is even
        while (!q.empty()) {
            int sz = q.size();
            long long prev = evenLevel ? LLONG_MIN : LLONG_MAX;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                int val = node->val;
                if (evenLevel) {
                    // values must be odd and strictly increasing
                    if ((val & 1) == 0) return false;
                    if (val <= prev) return false;
                } else {
                    // values must be even and strictly decreasing
                    if ((val & 1) == 1) return false;
                    if (val >= prev) return false;
                }
                prev = val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            evenLevel = !evenLevel;
        }
        return true;
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
    public boolean isEvenOddTree(TreeNode root) {
        if (root == null) return true;
        java.util.ArrayDeque<TreeNode> queue = new java.util.ArrayDeque<>();
        queue.add(root);
        boolean evenLevel = true; // level 0 is even
        while (!queue.isEmpty()) {
            int size = queue.size();
            int prev = evenLevel ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                int val = node.val;
                if (evenLevel) {
                    // values must be odd and strictly increasing
                    if ((val & 1) == 0 || val <= prev) return false;
                } else {
                    // values must be even and strictly decreasing
                    if ((val & 1) != 0 || val >= prev) return false;
                }
                prev = val;
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            evenLevel = !evenLevel;
        }
        return true;
    }
}
```

## Python

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        q = deque([root])
        even_level = True  # level 0 is even-indexed
        
        while q:
            size = len(q)
            prev = float('-inf') if even_level else float('inf')
            
            for _ in range(size):
                node = q.popleft()
                val = node.val
                
                if even_level:
                    # values must be odd and strictly increasing
                    if val % 2 == 0 or val <= prev:
                        return False
                else:
                    # values must be even and strictly decreasing
                    if val % 2 == 1 or val >= prev:
                        return False
                
                prev = val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            even_level = not even_level
        
        return True
```

## Python3

```python
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional['TreeNode']) -> bool:
        if not root:
            return True
        
        q = deque([root])
        even_level = True  # level 0 is even-indexed
        
        while q:
            size = len(q)
            prev = float('-inf') if even_level else float('inf')
            
            for _ in range(size):
                node = q.popleft()
                val = node.val
                
                if even_level:
                    # values must be odd and strictly increasing
                    if val % 2 == 0 or val <= prev:
                        return False
                else:
                    # values must be even and strictly decreasing
                    if val % 2 == 1 or val >= prev:
                        return False
                
                prev = val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            even_level = not even_level
        
        return True
```

## C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

bool isEvenOddTree(struct TreeNode* root) {
    if (!root) return true;

    // Maximum possible nodes as per constraints
    int maxNodes = 100000 + 5;
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * maxNodes);
    if (!queue) return false; // allocation failure, treat as false

    int front = 0, back = 0;
    queue[back++] = root;

    bool evenLevel = true; // level 0 is even
    while (front < back) {
        int levelSize = back - front;
        int prev = evenLevel ? INT_MIN : INT_MAX;

        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode *node = queue[front++];
            int val = node->val;

            if (evenLevel) {
                // Even-indexed level: values must be odd and strictly increasing
                if ((val % 2 == 0) || val <= prev) {
                    free(queue);
                    return false;
                }
            } else {
                // Odd-indexed level: values must be even and strictly decreasing
                if ((val % 2 != 0) || val >= prev) {
                    free(queue);
                    return false;
                }
            }
            prev = val;

            if (node->left) queue[back++] = node->left;
            if (node->right) queue[back++] = node->right;
        }
        evenLevel = !evenLevel;
    }

    free(queue);
    return true;
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
    public bool IsEvenOddTree(TreeNode root) {
        if (root == null) return true;
        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        int level = 0;
        while (queue.Count > 0) {
            int size = queue.Count;
            int prev = (level % 2 == 0) ? int.MinValue : int.MaxValue;
            for (int i = 0; i < size; i++) {
                var node = queue.Dequeue();
                if (level % 2 == 0) { // even level: odd values, strictly increasing
                    if ((node.val & 1) == 0 || node.val <= prev) return false;
                } else { // odd level: even values, strictly decreasing
                    if ((node.val & 1) == 1 || node.val >= prev) return false;
                }
                prev = node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            level++;
        }
        return true;
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
 * @return {boolean}
 */
var isEvenOddTree = function(root) {
    if (!root) return true;
    let queue = [root];
    let level = 0;
    
    while (queue.length) {
        const nextLevel = [];
        // set initial previous value based on level parity
        let prev = (level % 2 === 0) ? -Infinity : Infinity;
        
        for (const node of queue) {
            if (level % 2 === 0) { // even level: values must be odd and strictly increasing
                if ((node.val & 1) === 0 || node.val <= prev) return false;
            } else { // odd level: values must be even and strictly decreasing
                if ((node.val & 1) === 1 || node.val >= prev) return false;
            }
            prev = node.val;
            
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        
        queue = nextLevel;
        level++;
    }
    
    return true;
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

function isEvenOddTree(root: TreeNode | null): boolean {
    if (!root) return true;

    const queue: TreeNode[] = [root];
    let head = 0;
    let evenLevel = true; // level 0

    while (head < queue.length) {
        const levelSize = queue.length - head;
        let prev = evenLevel ? Number.NEGATIVE_INFINITY : Number.POSITIVE_INFINITY;

        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];
            const val = node.val;

            if (evenLevel) {
                // Even-indexed level: values must be odd and strictly increasing
                if ((val & 1) === 0 || val <= prev) return false;
            } else {
                // Odd-indexed level: values must be even and strictly decreasing
                if ((val & 1) === 1 || val >= prev) return false;
            }

            prev = val;

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        evenLevel = !evenLevel;
    }

    return true;
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
     * @return bool
     */
    function isEvenOddTree($root) {
        if ($root === null) {
            return true;
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $evenLevel = true; // level 0 is even

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $prev = $evenLevel ? PHP_INT_MIN : PHP_INT_MAX;

            for ($i = 0; $i < $size; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $val = $node->val;

                if ($evenLevel) {
                    // even-indexed level: values must be odd and strictly increasing
                    if (($val % 2 == 0) || $val <= $prev) {
                        return false;
                    }
                } else {
                    // odd-indexed level: values must be even and strictly decreasing
                    if (($val % 2 != 0) || $val >= $prev) {
                        return false;
                    }
                }

                $prev = $val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            $evenLevel = !$evenLevel;
        }

        return true;
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
    func isEvenOddTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        
        var queue: [TreeNode] = [root]
        var index = 0               // points to the current node to process
        var level = 0
        
        while index < queue.count {
            let size = queue.count - index   // nodes in the current level
            var prev: Int
            if level % 2 == 0 {
                prev = Int.min               // need strictly increasing
            } else {
                prev = Int.max               // need strictly decreasing
            }
            
            for _ in 0..<size {
                let node = queue[index]
                index += 1
                
                if level % 2 == 0 {          // even level: odd values, increasing
                    if node.val % 2 == 0 { return false }
                    if node.val <= prev { return false }
                } else {                     // odd level: even values, decreasing
                    if node.val % 2 != 0 { return false }
                    if node.val >= prev { return false }
                }
                
                prev = node.val
                
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            
            level += 1
        }
        
        return true
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
    fun isEvenOddTree(root: TreeNode?): Boolean {
        if (root == null) return true
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        var level = 0
        while (queue.isNotEmpty()) {
            val size = queue.size
            var prev = if (level % 2 == 0) Int.MIN_VALUE else Int.MAX_VALUE
            repeat(size) {
                val node = queue.removeFirst()
                val v = node.`val`
                if (level % 2 == 0) {
                    // even level: odd values, strictly increasing
                    if (v % 2 == 0 || v <= prev) return false
                } else {
                    // odd level: even values, strictly decreasing
                    if (v % 2 != 0 || v >= prev) return false
                }
                prev = v
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            level++
        }
        return true
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
  bool isEvenOddTree(TreeNode? root) {
    if (root == null) return true;

    List<TreeNode> queue = [root];
    int index = 0;
    bool evenLevel = true; // level 0 is even

    while (index < queue.length) {
      int levelSize = queue.length - index;
      int prev = evenLevel ? -1 : 1000001; // sentinel values

      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue[index++];
        int val = node.val;

        if (evenLevel) {
          // Even-indexed level: values must be odd and strictly increasing
          if (val % 2 == 0) return false;
          if (val <= prev) return false;
        } else {
          // Odd-indexed level: values must be even and strictly decreasing
          if (val % 2 != 0) return false;
          if (val >= prev) return false;
        }

        prev = val;

        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }

      evenLevel = !evenLevel; // move to next level
    }

    return true;
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
func isEvenOddTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	queue := []*TreeNode{root}
	evenLevel := true

	for len(queue) > 0 {
		levelSize := len(queue)
		if evenLevel {
			prev := -1 // values are >=1, so -1 works as initial minimum
			for i := 0; i < levelSize; i++ {
				node := queue[0]
				queue = queue[1:]

				if node.Val%2 == 0 || node.Val <= prev {
					return false
				}
				prev = node.Val

				if node.Left != nil {
					queue = append(queue, node.Left)
				}
				if node.Right != nil {
					queue = append(queue, node.Right)
				}
			}
		} else {
			maxInt := int(^uint(0) >> 1)
			prev := maxInt
			for i := 0; i < levelSize; i++ {
				node := queue[0]
				queue = queue[1:]

				if node.Val%2 == 1 || node.Val >= prev {
					return false
				}
				prev = node.Val

				if node.Left != nil {
					queue = append(queue, node.Left)
				}
				if node.Right != nil {
					queue = append(queue, node.Right)
				}
			}
		}
		evenLevel = !evenLevel
	}
	return true
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

def is_even_odd_tree(root)
  return true if root.nil?

  queue = [root]
  even_level = true

  until queue.empty?
    level_size = queue.size
    prev = even_level ? -1 : Float::INFINITY

    level_size.times do
      node = queue.shift
      val = node.val

      if even_level
        return false unless val.odd? && val > prev
      else
        return false unless val.even? && val < prev
      end

      prev = val
      queue << node.left if node.left
      queue << node.right if node.right
    end

    even_level = !even_level
  end

  true
end
```

## Scala

```scala
object Solution {
  def isEvenOddTree(root: TreeNode): Boolean = {
    import scala.collection.mutable.Queue

    val queue = Queue[TreeNode]()
    queue.enqueue(root)
    var level = 0

    while (queue.nonEmpty) {
      val size = queue.size
      var prev = if ((level & 1) == 0) Int.MinValue else Int.MaxValue

      for (_ <- 0 until size) {
        val node = queue.dequeue()

        // parity must be opposite to level parity
        if ((node.value & 1) == (level & 1)) return false

        if ((level & 1) == 0) { // even level: strictly increasing, odd values
          if (node.value <= prev) return false
        } else {               // odd level: strictly decreasing, even values
          if (node.value >= prev) return false
        }

        prev = node.value

        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
      level += 1
    }

    true
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn is_even_odd_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if root.is_none() {
            return true;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());
        let mut level = 0;

        while !queue.is_empty() {
            let size = queue.len();
            let mut prev = if level % 2 == 0 { i32::MIN } else { i32::MAX };

            for _ in 0..size {
                let node_rc = queue.pop_front().unwrap();
                let node_ref = node_rc.borrow();
                let val = node_ref.val;

                // parity and ordering checks
                if level % 2 == 0 {
                    // even level: values must be odd and strictly increasing
                    if val % 2 == 0 || val <= prev {
                        return false;
                    }
                } else {
                    // odd level: values must be even and strictly decreasing
                    if val % 2 != 0 || val >= prev {
                        return false;
                    }
                }

                prev = val;

                if let Some(left) = &node_ref.left {
                    queue.push_back(Rc::clone(left));
                }
                if let Some(right) = &node_ref.right {
                    queue.push_back(Rc::clone(right));
                }
            }

            level += 1;
        }

        true
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

(: is-even-odd-tree (-> (or/c tree-node? #f) boolean?))
(define (is-even-odd-tree root)
  (if (not root) #t
      (let odd?   (lambda (n) (= (modulo n 2) 1))
            even?  (lambda (n) (= (modulo n 2) 0)))
        (let bfs ((current-level (list root)) (even-level? #t))
          (cond
            [(null? current-level) #t]
            [else
             (let loop ((nodes current-level)
                        (prev (if even-level? -inf.0 +inf.0))
                        (next '()))
               (cond
                 [(null? nodes)
                  (bfs (reverse next) (not even-level?))]
                 [else
                  (define node (car nodes))
                  (define val  (tree-node-val node))
                  (if (if even-level?
                          (or (not (odd? val)) (<= val prev))
                          (or (not (even? val)) (>= val prev)))
                      #f
                      (let* ((left  (tree-node-left node))
                             (right (tree-node-right node))
                             (next-with-right (if right (cons right next) next))
                             (next-with-both (if left (cons left next-with-right) next-with-right)))
                        (loop (cdr nodes)
                              (if even-level? val prev)
                              next-with-both))))]))])))))
```

## Erlang

```erlang
-module(solution).
-export([is_even_odd_tree/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec is_even_odd_tree(Root :: #tree_node{} | null) -> boolean().
is_even_odd_tree(null) ->
    true;
is_even_odd_tree(Root) ->
    Q0 = queue:new(),
    Q1 = queue:in(Root, Q0),
    bfs(Q1, true).

bfs(Queue, _Even) when queue:is_empty(Queue) ->
    true;
bfs(Queue, Even) ->
    Size = queue:len(Queue),
    PrevInit = if Even -> 0; true -> 1000001 end,
    bfs_level(Size, Queue, Even, PrevInit).

bfs_level(0, Queue, Even, _Prev) ->
    bfs(Queue, not Even);
bfs_level(N, Queue, Even, Prev) ->
    case queue:out(Queue) of
        empty ->
            false;
        {value, Node, Q1} ->
            Val = Node#tree_node.val,
            Cond = if
                Even -> (Val rem 2 == 1) andalso (Val > Prev);
                true -> (Val rem 2 == 0) andalso (Val < Prev)
            end,
            case Cond of
                false -> false;
                true ->
                    Q2 = case Node#tree_node.left of
                        null -> Q1;
                        L -> queue:in(L, Q1)
                    end,
                    Q3 = case Node#tree_node.right of
                        null -> Q2;
                        R -> queue:in(R, Q2)
                    end,
                    bfs_level(N - 1, Q3, Even, Val)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_even_odd_tree(root :: TreeNode.t() | nil) :: boolean
  def is_even_odd_tree(nil), do: true

  def is_even_odd_tree(root) do
    bfs(:queue.from_list([root]), true)
  end

  defp bfs(queue, even_level) do
    if :queue.is_empty(queue) do
      true
    else
      size = :queue.len(queue)

      {next_queue, ok} = process_nodes(queue, size, even_level, nil, :queue.new())

      if ok, do: bfs(next_queue, not even_level), else: false
    end
  end

  defp process_nodes(_queue, 0, _even, _prev, children_q) do
    {children_q, true}
  end

  defp process_nodes(queue, remaining, even, prev, children_q) do
    case :queue.out(queue) do
      {:empty, _} ->
        {children_q, false}

      {{:value, node}, q_rest} ->
        cond do
          (even and rem(node.val, 2) == 0) or (!even and rem(node.val, 2) == 1) ->
            {children_q, false}

          not is_nil(prev) and ((even and node.val <= prev) or (!even and node.val >= prev)) ->
            {children_q, false}

          true ->
            children_q =
              case node.left do
                nil -> children_q
                l -> :queue.in(l, children_q)
              end

            children_q =
              case node.right do
                nil -> children_q
                r -> :queue.in(r, children_q)
              end

            process_nodes(q_rest, remaining - 1, even, node.val, children_q)
        end
    end
  end
end
```
