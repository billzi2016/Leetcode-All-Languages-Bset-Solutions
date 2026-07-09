# 0199. Binary Tree Right Side View

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                if (i == sz - 1) result.push_back(node->val); // rightmost at this level
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) {
                    result.add(node.val);
                }
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
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
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import deque
        q = deque([root])
        view = []
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == level_size - 1:
                    view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return view
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
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        view = []
        queue = [root]
        while queue:
            view.append(queue[-1].val)
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        return view
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rightSideView(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (!root) return NULL;

    /* Maximum number of nodes is 100, allocate a bit more for safety */
    const int MAXN = 200;
    int* result = (int*)malloc(sizeof(int) * MAXN);
    struct TreeNode** queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * MAXN);

    int front = 0, rear = 0;
    queue[rear++] = root;

    while (front < rear) {
        int levelSize = rear - front;          // number of nodes at current level
        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode* node = queue[front++];
            if (i == levelSize - 1) {           // rightmost node of this level
                result[*returnSize] = node->val;
                (*returnSize)++;
            }
            if (node->left)  queue[rear++] = node->left;
            if (node->right) queue[rear++] = node->right;
        }
    }

    free(queue);
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
using System.Collections.Generic;

public class Solution {
    public IList<int> RightSideView(TreeNode root) {
        var result = new List<int>();
        if (root == null) return result;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                if (i == levelSize - 1) {
                    result.Add(node.val);
                }
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
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
 * @return {number[]}
 */
var rightSideView = function(root) {
    if (!root) return [];
    const result = [];
    const queue = [root];
    
    while (queue.length) {
        const levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            if (i === levelSize - 1) result.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
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

function rightSideView(root: TreeNode | null): number[] {
    const view: number[] = [];
    if (!root) return view;
    const queue: TreeNode[] = [root];
    while (queue.length) {
        const levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift()!;
            if (i === levelSize - 1) view.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }
    return view;
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
     * @return Integer[]
     */
    function rightSideView($root) {
        if ($root === null) {
            return [];
        }

        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();

                if ($i === $levelSize - 1) {
                    $result[] = $node->val;
                }

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }
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
    func rightSideView(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }
        var result: [Int] = []
        var queue: [TreeNode] = [root]
        var index = 0
        
        while index < queue.count {
            let levelSize = queue.count - index
            for i in 0..<levelSize {
                let node = queue[index]
                index += 1
                if i == levelSize - 1 {
                    result.append(node.val)
                }
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
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
    fun rightSideView(root: TreeNode?): List<Int> {
        val res = mutableListOf<Int>()
        if (root == null) return res
        val q: ArrayDeque<TreeNode> = ArrayDeque()
        q.add(root)
        while (q.isNotEmpty()) {
            var node: TreeNode? = null
            repeat(q.size) {
                node = q.removeFirst()
                node?.left?.let { q.add(it) }
                node?.right?.let { q.add(it) }
            }
            res.add(node!!.`val`)
        }
        return res
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
  List<int> rightSideView(TreeNode? root) {
    if (root == null) return [];
    List<int> result = [];
    List<TreeNode?> queue = [root];
    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeAt(0)!;
        if (i == levelSize - 1) result.add(node.val);
        if (node.left != null) queue.add(node.left);
        if (node.right != null) queue.add(node.right);
      }
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
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	var result []int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			if i == levelSize-1 {
				result = append(result, node.Val)
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
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

def right_side_view(root)
  return [] unless root
  view = []
  level = [root]
  until level.empty?
    view << level[-1].val
    next_level = []
    level.each do |node|
      next_level << node.left if node.left
      next_level << node.right if node.right
    end
    level = next_level
  end
  view
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
  def rightSideView(root: TreeNode): List[Int] = {
    if (root == null) return Nil
    val res = scala.collection.mutable.ListBuffer[Int]()
    val q = new java.util.ArrayDeque[TreeNode]()
    q.add(root)
    while (!q.isEmpty) {
      val size = q.size()
      for (i <- 0 until size) {
        val node = q.poll()
        if (i == size - 1) res += node.value
        if (node.left != null) q.add(node.left)
        if (node.right != null) q.add(node.right)
      }
    }
    res.toList
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result = Vec::new();
        if root.is_none() {
            return result;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        while !queue.is_empty() {
            let level_size = queue.len();
            for i in 0..level_size {
                let node_rc = queue.pop_front().unwrap();
                let node_ref = node_rc.borrow();

                if i == level_size - 1 {
                    result.push(node_ref.val);
                }
                if let Some(left) = &node_ref.left {
                    queue.push_back(Rc::clone(left));
                }
                if let Some(right) = &node_ref.right {
                    queue.push_back(Rc::clone(right));
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (right-side-view root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (if (not root)
      '()
      (let loop ((level (list root)) (acc '()))
        (if (null? level)
            (reverse acc)
            (let* ((rightmost-val (tree-node-val (car (reverse level))))
                   (next-level
                    (apply append
                           (map (lambda (node)
                                  (filter identity
                                          (list (tree-node-left node) (tree-node-right node))))
                                level))))
              (loop next-level (cons rightmost-val acc)))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec right_side_view(Root :: #tree_node{} | null) -> [integer()].
right_side_view(null) ->
    [];
right_side_view(Root) ->
    bfs([Root], []).

bfs([], Res) ->
    lists:reverse(Res);
bfs(LevelNodes, Acc) ->
    Values = [Node#tree_node.val || Node <- LevelNodes],
    LastVal = lists:last(Values),
    NextLevel = lists:flatmap(
        fun(Node) ->
            LeftChildren = case Node#tree_node.left of
                               null -> [];
                               L -> [L]
                           end,
            RightChildren = case Node#tree_node.right of
                                null -> [];
                                R -> [R]
                            end,
            LeftChildren ++ RightChildren
        end, LevelNodes),
    bfs(NextLevel, [LastVal | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec right_side_view(root :: TreeNode.t | nil) :: [integer]
  def right_side_view(nil), do: []

  def right_side_view(root) do
    root
    |> dfs(0, %{})
    |> Enum.sort_by(fn {depth, _} -> depth end)
    |> Enum.map(fn {_depth, val} -> val end)
  end

  defp dfs(nil, _depth, acc), do: acc

  defp dfs(%TreeNode{val: v, left: l, right: r}, depth, acc) do
    acc = if Map.has_key?(acc, depth), do: acc, else: Map.put(acc, depth, v)
    acc = dfs(r, depth + 1, acc)
    dfs(l, depth + 1, acc)
  end
end
```
