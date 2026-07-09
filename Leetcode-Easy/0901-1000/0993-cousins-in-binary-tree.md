# 0993. Cousins in Binary Tree

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
    bool isCousins(TreeNode* root, int x, int y) {
        if (!root) return false;
        queue<pair<TreeNode*, TreeNode*>> q; // node, parent
        q.push({root, nullptr});
        
        while (!q.empty()) {
            int sz = q.size();
            bool foundX = false, foundY = false;
            TreeNode* parentX = nullptr;
            TreeNode* parentY = nullptr;
            
            for (int i = 0; i < sz; ++i) {
                auto [node, parent] = q.front(); q.pop();
                
                if (node->val == x) { foundX = true; parentX = parent; }
                if (node->val == y) { foundY = true; parentY = parent; }
                
                if (node->left)  q.push({node->left, node});
                if (node->right) q.push({node->right, node});
            }
            
            if (foundX && foundY) {
                return parentX != parentY;
            }
            if (foundX || foundY) {
                // Found only one at this depth -> cannot be cousins
                return false;
            }
        }
        return false;
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
    public boolean isCousins(TreeNode root, int x, int y) {
        if (root == null) return false;
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<TreeNode> parentQueue = new LinkedList<>();
        nodeQueue.add(root);
        parentQueue.add(null); // root has no parent

        int depth = 0;
        int xDepth = -1, yDepth = -1;
        int xParent = -2, yParent = -2; // distinct sentinel values

        while (!nodeQueue.isEmpty()) {
            int size = nodeQueue.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = nodeQueue.poll();
                TreeNode par = parentQueue.poll();

                if (cur.val == x) {
                    xDepth = depth;
                    xParent = (par == null ? -1 : par.val);
                }
                if (cur.val == y) {
                    yDepth = depth;
                    yParent = (par == null ? -1 : par.val);
                }

                if (cur.left != null) {
                    nodeQueue.add(cur.left);
                    parentQueue.add(cur);
                }
                if (cur.right != null) {
                    nodeQueue.add(cur.right);
                    parentQueue.add(cur);
                }
            }

            // after processing the whole level, check if both found
            if (xDepth != -1 && yDepth != -1) {
                return xDepth == yDepth && xParent != yParent;
            }
            depth++;
        }
        return false;
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
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        from collections import deque

        if not root:
            return False

        q = deque()
        q.append((root, None, 0))  # node, parent, depth

        px = py = None
        dx = dy = -1

        while q:
            node, parent, depth = q.popleft()

            if node.val == x:
                px, dx = parent, depth
            elif node.val == y:
                py, dy = parent, depth

            # If both found, can stop early
            if px is not None and py is not None:
                break

            if node.left:
                q.append((node.left, node, depth + 1))
            if node.right:
                q.append((node.right, node, depth + 1))

        return dx == dy and px != py
```

## Python3

```python
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        from collections import deque
        queue = deque([(root, None, 0)])  # node, parent, depth
        info = {}
        
        while queue and len(info) < 2:
            node, parent, depth = queue.popleft()
            if node.val == x or node.val == y:
                info[node.val] = (parent, depth)
                if len(info) == 2:
                    break
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        if x in info and y in info:
            parent_x, depth_x = info[x]
            parent_y, depth_y = info[y]
            return depth_x == depth_y and parent_x != parent_y
        return False
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
static void dfs(struct TreeNode* node, struct TreeNode* parent, int depth,
                int target, int *foundDepth, struct TreeNode **foundParent) {
    if (!node) return;
    if (node->val == target) {
        *foundDepth = depth;
        *foundParent = parent;
        return;
    }
    dfs(node->left, node, depth + 1, target, foundDepth, foundParent);
    dfs(node->right, node, depth + 1, target, foundDepth, foundParent);
}

bool isCousins(struct TreeNode* root, int x, int y) {
    int depthX = -1, depthY = -1;
    struct TreeNode *parentX = NULL, *parentY = NULL;
    dfs(root, NULL, 0, x, &depthX, &parentX);
    dfs(root, NULL, 0, y, &depthY, &parentY);
    return (depthX == depthY && parentX != parentY);
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
    public bool IsCousins(TreeNode root, int x, int y) {
        if (root == null) return false;
        
        var queue = new Queue<(TreeNode node, TreeNode parent)>();
        queue.Enqueue((root, null));
        
        int depthX = -1, depthY = -1;
        TreeNode parentX = null, parentY = null;
        int depth = 0;
        
        while (queue.Count > 0 && (depthX == -1 || depthY == -1)) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                var (node, parent) = queue.Dequeue();
                
                if (node.val == x) {
                    depthX = depth;
                    parentX = parent;
                } else if (node.val == y) {
                    depthY = depth;
                    parentY = parent;
                }
                
                if (node.left != null) queue.Enqueue((node.left, node));
                if (node.right != null) queue.Enqueue((node.right, node));
            }
            depth++;
        }
        
        return depthX == depthY && parentX != parentY;
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
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    if (!root) return false;
    const queue = [[root, null]]; // [node, parent]
    
    while (queue.length) {
        const levelSize = queue.length;
        let xParent = null, yParent = null;
        
        for (let i = 0; i < levelSize; i++) {
            const [node, parent] = queue.shift();
            
            if (node.val === x) xParent = parent;
            if (node.val === y) yParent = parent;
            
            if (node.left) queue.push([node.left, node]);
            if (node.right) queue.push([node.right, node]);
        }
        
        if (xParent && yParent) {
            return xParent !== yParent;
        }
        if ((xParent && !yParent) || (!xParent && yParent)) {
            // Found only one at this depth
            return false;
        }
    }
    
    return false;
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

function isCousins(root: TreeNode | null, x: number, y: number): boolean {
    if (!root) return false;

    let xParent: TreeNode | null = null;
    let yParent: TreeNode | null = null;
    let xDepth = -1;
    let yDepth = -1;

    const queue: Array<{node: TreeNode, parent: TreeNode | null, depth: number}> = [{node: root, parent: null, depth: 0}];
    let idx = 0;

    while (idx < queue.length) {
        const {node, parent, depth} = queue[idx++];
        if (node.val === x) {
            xParent = parent;
            xDepth = depth;
        } else if (node.val === y) {
            yParent = parent;
            yDepth = depth;
        }

        if (xDepth !== -1 && yDepth !== -1) break;

        if (node.left) queue.push({node: node.left, parent: node, depth: depth + 1});
        if (node.right) queue.push({node: node.right, parent: node, depth: depth + 1});
    }

    return xDepth === yDepth && xParent !== yParent;
}
```

## Php

```php
<?php
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
     * @param Integer $x
     * @param Integer $y
     * @return Boolean
     */
    function isCousins($root, $x, $y) {
        if ($root === null) return false;
        $queue = new SplQueue();
        $queue->enqueue([$root, null]); // node and its parent

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $parentX = null;
            $parentY = null;

            for ($i = 0; $i < $size; $i++) {
                [$node, $parent] = $queue->dequeue();

                if ($node->val === $x) $parentX = $parent;
                if ($node->val === $y) $parentY = $parent;

                if ($node->left !== null) {
                    $queue->enqueue([$node->left, $node]);
                }
                if ($node->right !== null) {
                    $queue->enqueue([$node->right, $node]);
                }
            }

            if ($parentX !== null && $parentY !== null) {
                return $parentX !== $parentY;
            }
            if (($parentX !== null) xor ($parentY !== null)) {
                // found one but not the other at this depth
                return false;
            }
        }

        return false;
    }
}
?>
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
    func isCousins(_ root: TreeNode?, _ x: Int, _ y: Int) -> Bool {
        guard let root = root else { return false }
        var queue: [(node: TreeNode, parent: TreeNode?)] = [(root, nil)]
        
        while !queue.isEmpty {
            var nextLevel: [(node: TreeNode, parent: TreeNode?)] = []
            var xParent: TreeNode? = nil
            var yParent: TreeNode? = nil
            
            for (node, parent) in queue {
                if node.val == x { xParent = parent }
                if node.val == y { yParent = parent }
                
                if let left = node.left {
                    nextLevel.append((left, node))
                }
                if let right = node.right {
                    nextLevel.append((right, node))
                }
            }
            
            if let xp = xParent, let yp = yParent {
                return xp !== yp
            }
            // Found only one at this depth -> cannot be cousins
            if (xParent != nil) != (yParent != nil) {
                return false
            }
            
            queue = nextLevel
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isCousins(root: TreeNode?, x: Int, y: Int): Boolean {
        if (root == null) return false
        var xParent: TreeNode? = null
        var yParent: TreeNode? = null
        var xDepth = -1
        var yDepth = -1
        val queue: ArrayDeque<Pair<TreeNode, Int>> = ArrayDeque()
        queue.add(Pair(root, 0))
        while (queue.isNotEmpty()) {
            val (node, depth) = queue.removeFirst()
            node.left?.let {
                if (it.`val` == x) {
                    xParent = node
                    xDepth = depth + 1
                } else if (it.`val` == y) {
                    yParent = node
                    yDepth = depth + 1
                }
                queue.add(Pair(it, depth + 1))
            }
            node.right?.let {
                if (it.`val` == x) {
                    xParent = node
                    xDepth = depth + 1
                } else if (it.`val` == y) {
                    yParent = node
                    yDepth = depth + 1
                }
                queue.add(Pair(it, depth + 1))
            }
            if (xDepth != -1 && yDepth != -1) break
        }
        return xDepth == yDepth && xParent !== yParent
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
  bool isCousins(TreeNode? root, int x, int y) {
    if (root == null) return false;

    class _Info {
      TreeNode node;
      TreeNode? parent;
      int depth;
      _Info(this.node, this.parent, this.depth);
    }

    Queue<_Info> q = Queue();
    q.add(_Info(root, null, 0));

    TreeNode? xParent;
    TreeNode? yParent;
    int? xDepth;
    int? yDepth;

    while (q.isNotEmpty) {
      var cur = q.removeFirst();

      if (cur.node.val == x) {
        xParent = cur.parent;
        xDepth = cur.depth;
      }
      if (cur.node.val == y) {
        yParent = cur.parent;
        yDepth = cur.depth;
      }

      if (xDepth != null && yDepth != null) break;

      if (cur.node.left != null) {
        q.add(_Info(cur.node.left!, cur.node, cur.depth + 1));
      }
      if (cur.node.right != null) {
        q.add(_Info(cur.node.right!, cur.node, cur.depth + 1));
      }
    }

    return xDepth == yDepth && xParent != null && yParent != null && xParent!.val != yParent!.val;
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
func isCousins(root *TreeNode, x int, y int) bool {
	if root == nil {
		return false
	}
	type nodeInfo struct {
		node   *TreeNode
		parent *TreeNode
	}
	queue := []nodeInfo{{root, nil}}
	var xParent, yParent *TreeNode
	xDepth, yDepth := -1, -1
	depth := 0

	for len(queue) > 0 {
		levelSize := len(queue)
		for i := 0; i < levelSize; i++ {
			cur := queue[0]
			queue = queue[1:]

			if cur.node.Val == x {
				xParent = cur.parent
				xDepth = depth
			}
			if cur.node.Val == y {
				yParent = cur.parent
				yDepth = depth
			}

			if cur.node.Left != nil {
				queue = append(queue, nodeInfo{cur.node.Left, cur.node})
			}
			if cur.node.Right != nil {
				queue = append(queue, nodeInfo{cur.node.Right, cur.node})
			}
		}
		if xParent != nil && yParent != nil {
			return xDepth == yDepth && xParent != yParent
		}
		depth++
	}
	return false
}
```

## Ruby

```ruby
def is_cousins(root, x, y)
  return false unless root
  queue = [[root, nil]]
  while !queue.empty?
    level_size = queue.size
    x_parent = nil
    y_parent = nil
    level_size.times do
      node, parent = queue.shift
      if node.val == x
        x_parent = parent
      elsif node.val == y
        y_parent = parent
      end
      queue << [node.left, node] if node.left
      queue << [node.right, node] if node.right
    end
    return false if (x_parent && !y_parent) || (!x_parent && y_parent)
    return x_parent != y_parent if x_parent && y_parent
  end
  false
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
    def isCousins(root: TreeNode, x: Int, y: Int): Boolean = {
        if (root == null) return false
        import scala.collection.mutable.Queue
        val q = Queue[(TreeNode, TreeNode)]()
        q.enqueue((root, null))
        while (q.nonEmpty) {
            var parentX: TreeNode = null
            var parentY: TreeNode = null
            val levelSize = q.size
            for (_ <- 0 until levelSize) {
                val (node, parent) = q.dequeue()
                if (node.value == x) parentX = parent
                else if (node.value == y) parentY = parent
                if (node.left != null) q.enqueue((node.left, node))
                if (node.right != null) q.enqueue((node.right, node))
            }
            if (parentX != null && parentY != null) {
                return parentX ne parentY
            } else if (parentX != null || parentY != null) {
                return false
            }
        }
        false
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

impl Solution {
    pub fn is_cousins(root: Option<Rc<RefCell<TreeNode>>>, x: i32, y: i32) -> bool {
        if root.is_none() {
            return false;
        }
        let mut queue = VecDeque::new();
        // (node_option, parent_value_option, depth)
        queue.push_back((root.clone(), None, 0usize));
        let mut x_info: Option<(usize, Option<i32>)> = None;
        let mut y_info: Option<(usize, Option<i32>)> = None;

        while let Some((node_opt, parent_val, depth)) = queue.pop_front() {
            if let Some(node_rc) = node_opt {
                let node_ref = node_rc.borrow();
                let val = node_ref.val;
                if val == x {
                    x_info = Some((depth, parent_val));
                }
                if val == y {
                    y_info = Some((depth, parent_val));
                }
                if x_info.is_some() && y_info.is_some() {
                    break;
                }
                if let Some(left) = node_ref.left.clone() {
                    queue.push_back((Some(left), Some(val), depth + 1));
                }
                if let Some(right) = node_ref.right.clone() {
                    queue.push_back((Some(right), Some(val), depth + 1));
                }
            }
        }

        match (x_info, y_info) {
            (Some((dx, px)), Some((dy, py))) => dx == dy && px != py,
            _ => false,
        }
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

(define/contract (is-cousins root x y)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? boolean?)
  (let ((dx #f) (px #f) (dy #f) (py #f))
    (define (dfs node depth parent)
      (when node
        (cond [(= (tree-node-val node) x)
               (set! dx depth)
               (set! px parent)]
              [(= (tree-node-val node) y)
               (set! dy depth)
               (set! py parent)])
        (dfs (tree-node-left node) (+ depth 1) node)
        (dfs (tree-node-right node) (+ depth 1) node)))
    (dfs root 0 #f)
    (and dx dy (= dx dy) (not (eq? px py)))))
```

## Erlang

```erlang
-module(solution).
-export([is_cousins/3]).

%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec is_cousins(Root :: #tree_node{} | null, X :: integer(), Y :: integer()) -> boolean().
is_cousins(Root, X, Y) ->
    case {find(Root, X, null, 0), find(Root, Y, null, 0)} of
        {{found, Dx, Px}, {found, Dy, Py}} when Dx =:= Dy, Px =/= Py -> true;
        _ -> false
    end.

%% Helper: locate Target value, returning {found, Depth, Parent} or not_found.
-spec find(Root :: #tree_node{} | null,
           Target :: integer(),
           Parent :: #tree_node{} | null,
           Depth :: non_neg_integer()) ->
          {found, non_neg_integer(), #tree_node{} | null} | not_found.
find(null, _Target, _Parent, _Depth) ->
    not_found;
find(#tree_node{val = Val, left = L, right = R}=Node, Target, Parent, Depth) ->
    if
        Val =:= Target ->
            {found, Depth, Parent};
        true ->
            case find(L, Target, Node, Depth + 1) of
                not_found -> find(R, Target, Node, Depth + 1);
                Res -> Res
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_cousins(root :: TreeNode.t | nil, x :: integer, y :: integer) :: boolean
  def is_cousins(root, x, y) do
    bfs([{root, nil}], x, y)
  end

  defp bfs([], _x, _y), do: false

  defp bfs(queue, x, y) do
    {found_x_parent, found_y_parent, next_queue} =
      Enum.reduce(queue, {nil, nil, []}, fn {node, parent}, {fx, fy, nq} ->
        # gather children for the next level
        children =
          case node do
            %TreeNode{left: l, right: r} -> [{l, node}, {r, node}]
          end

        new_nq = nq ++ Enum.filter(children, fn {c, _} -> not is_nil(c) end)

        cond do
          node.val == x -> {parent, fy, new_nq}
          node.val == y -> {fx, parent, new_nq}
          true -> {fx, fy, new_nq}
        end
      end)

    cond do
      # both found at the same depth
      not is_nil(found_x_parent) and not is_nil(found_y_parent) ->
        found_x_parent != found_y_parent

      # only one found at this depth => depths differ
      (not is_nil(found_x_parent)) xor (not is_nil(found_y_parent)) ->
        false

      # none found, continue to next level
      true ->
        bfs(next_queue, x, y)
    end
  end
end
```
