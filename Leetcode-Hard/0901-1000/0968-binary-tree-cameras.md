# 0968. Binary Tree Cameras

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
    int minCameraCover(TreeNode* root) {
        int cameras = 0;
        // 0: not covered, 1: has camera, 2: covered without camera
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 2; // null nodes are considered covered
            int left = dfs(node->left);
            int right = dfs(node->right);
            
            if (left == 0 || right == 0) { // any child is not covered, place camera here
                ++cameras;
                return 1; // this node has a camera
            }
            if (left == 1 || right == 1) {
                return 2; // child has camera, so this node is covered
            }
            return 0; // this node is not covered
        };
        
        int rootState = dfs(root);
        if (rootState == 0) ++cameras;
        return cameras;
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
    private int cameras = 0;

    public int minCameraCover(TreeNode root) {
        if (dfs(root) == 2) {
            cameras++;
        }
        return cameras;
    }

    // State: 0 -> has camera, 1 -> covered without camera, 2 -> not covered
    private int dfs(TreeNode node) {
        if (node == null) {
            return 1; // Null nodes are considered covered.
        }
        int left = dfs(node.left);
        int right = dfs(node.right);

        if (left == 2 || right == 2) {
            cameras++;
            return 0; // Place camera at this node.
        }

        if (left == 0 || right == 0) {
            return 1; // This node is covered by a child's camera.
        }

        return 2; // This node needs to be covered by its parent.
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
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.cameras = 0

        def dfs(node):
            if not node:
                # Null nodes are considered covered without a camera.
                return 1
            left = dfs(node.left)
            right = dfs(node.right)

            # If any child is not covered, place a camera at this node.
            if left == 0 or right == 0:
                self.cameras += 1
                return 2  # This node has a camera.

            # If any child has a camera, this node is covered.
            if left == 2 or right == 2:
                return 1  # Covered, no camera needed here.

            # Otherwise, this node is not covered.
            return 0

        root_state = dfs(root)
        if root_state == 0:  # Root is not covered; need an extra camera.
            self.cameras += 1
        return self.cameras
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0

        def dfs(node: Optional[TreeNode]) -> int:
            # Return states:
            # 0 -> node is not covered
            # 1 -> node is covered, no camera here
            # 2 -> node has a camera
            if not node:
                return 1  # Null nodes are considered covered

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 2

            if left == 2 or right == 2:
                return 1

            return 0

        root_state = dfs(root)
        if root_state == 0:
            self.cameras += 1
        return self.cameras
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
static int dfs(struct TreeNode* node, int *cnt) {
    if (!node) return 1; // null nodes are considered covered

    int left = dfs(node->left, cnt);
    int right = dfs(node->right, cnt);

    // If any child is not covered, place camera here
    if (left == 0 || right == 0) {
        (*cnt)++;
        return 2; // this node has a camera
    }

    // If any child has a camera, this node is covered
    if (left == 2 || right == 2) {
        return 1; // covered without camera
    }

    // Children are covered but no camera among them
    return 0; // not covered
}

int minCameraCover(struct TreeNode* root) {
    int cameras = 0;
    if (dfs(root, &cameras) == 0) { // root is not covered
        cameras++;
    }
    return cameras;
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
public class Solution
{
    private int cameras;

    public int MinCameraCover(TreeNode root)
    {
        cameras = 0;
        if (Dfs(root) == 0)
            cameras++;
        return cameras;
    }

    // Returns state:
    // 0 -> node is not covered,
    // 1 -> node is covered without a camera,
    // 2 -> node has a camera.
    private int Dfs(TreeNode node)
    {
        if (node == null)
            return 1; // Null nodes are considered covered.

        int left = Dfs(node.left);
        int right = Dfs(node.right);

        if (left == 0 || right == 0)
        {
            cameras++;
            return 2; // Place camera at this node.
        }

        if (left == 2 || right == 2)
        {
            return 1; // This node is covered by child's camera.
        }

        return 0; // Not covered and no camera placed.
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
var minCameraCover = function(root) {
    let cameras = 0;
    
    const dfs = (node) => {
        if (!node) return 1; // Null nodes are considered covered.
        
        const left = dfs(node.left);
        const right = dfs(node.right);
        
        // If any child is not covered, place camera at current node.
        if (left === 0 || right === 0) {
            cameras++;
            return 2; // Node has a camera.
        }
        
        // If any child has a camera, this node is covered.
        if (left === 2 || right === 2) {
            return 1; // Covered without camera.
        }
        
        // Otherwise, this node is not covered.
        return 0;
    };
    
    if (dfs(root) === 0) cameras++;
    return cameras;
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

function minCameraCover(root: TreeNode | null): number {
    const INF = 1e9;
    if (!root) return 0;

    function dfs(node: TreeNode | null): [number, number, number] {
        if (!node) return [0, 0, INF]; // [not covered, covered w/o cam, has cam]

        const left = dfs(node.left);
        const right = dfs(node.right);

        // Place a camera at this node
        const s2 = 1 + Math.min(left[0], left[1], left[2]) + Math.min(right[0], right[1], right[2]);

        // Node is not covered, children must be covered without cameras
        const s0 = left[1] + right[1];

        // Node is covered without a camera: at least one child has a camera
        const minLeft12 = Math.min(left[1], left[2]);
        const minRight12 = Math.min(right[1], right[2]);
        let s1 = INF;
        s1 = Math.min(s1, left[2] + minRight12);   // left child has a camera
        s1 = Math.min(s1, right[2] + minLeft12);   // right child has a camera

        return [s0, s1, s2];
    }

    const [_, coveredWithoutCam, withCam] = dfs(root);
    return Math.min(coveredWithoutCam, withCam);
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
     * @var int
     */
    private $cameras = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function minCameraCover($root) {
        $state = $this->dfs($root);
        if ($state == 0) {
            $this->cameras++;
        }
        return $this->cameras;
    }

    /**
     * @param TreeNode|null $node
     * @return int 0: not covered, 1: has camera, 2: covered without camera
     */
    private function dfs($node) {
        if ($node === null) {
            return 2; // Null nodes are considered covered.
        }

        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);

        // If any child is not covered, place camera at current node.
        if ($left == 0 || $right == 0) {
            $this->cameras++;
            return 1; // Has camera
        }

        // If any child has a camera, this node is covered.
        if ($left == 1 || $right == 1) {
            return 2; // Covered without camera
        }

        // Otherwise, this node is not covered.
        return 0;
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
    func minCameraCover(_ root: TreeNode?) -> Int {
        let INF = 1_000_000
        
        func dfs(_ node: TreeNode?) -> (Int, Int, Int) {
            guard let n = node else { return (0, 0, INF) }
            let left = dfs(n.left)
            let right = dfs(n.right)
            
            // State 2: place camera at this node
            let s2 = 1 + min(left.0, min(left.1, left.2)) + min(right.0, min(right.1, right.2))
            // State 0: node not covered, children must be covered without cameras
            let s0 = left.1 + right.1
            // State 1: node is covered without camera here; at least one child has a camera
            var s1 = INF
            s1 = min(s1, left.2 + min(right.1, right.2))
            s1 = min(s1, right.2 + min(left.1, left.2))
            
            return (s0, s1, s2)
        }
        
        let result = dfs(root)
        // root must be covered either by a camera on it or by its children
        return min(result.1, result.2)
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
    private var cameras = 0

    fun minCameraCover(root: TreeNode?): Int {
        if (dfs(root) == 0) cameras++
        return cameras
    }

    // Returns state of the node:
    // 0 -> not covered, needs a camera from parent
    // 1 -> has a camera
    // 2 -> covered without a camera
    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 2
        val left = dfs(node.left)
        val right = dfs(node.right)

        if (left == 0 || right == 0) {
            cameras++
            return 1
        }
        if (left == 1 || right == 1) {
            return 2
        }
        return 0
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
  int _cameras = 0;

  int minCameraCover(TreeNode? root) {
    _cameras = 0;
    int state = _dfs(root);
    if (state == 0) _cameras++;
    return _cameras;
  }

  int _dfs(TreeNode? node) {
    if (node == null) return 1; // null nodes are considered covered
    int left = _dfs(node.left);
    int right = _dfs(node.right);

    if (left == 0 || right == 0) {
      _cameras++;
      return 2; // place camera here
    }
    if (left == 2 || right == 2) {
      return 1; // covered by child camera
    }
    return 0; // not covered
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
func minCameraCover(root *TreeNode) int {
    cameras := 0
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 1 // null nodes are considered covered
        }
        left := dfs(node.Left)
        right := dfs(node.Right)

        if left == 2 || right == 2 {
            cameras++
            return 0 // place camera at this node
        }
        if left == 0 || right == 0 {
            return 1 // this node is covered by child's camera
        }
        return 2 // this node needs a camera
    }

    if dfs(root) == 2 {
        cameras++
    }
    return cameras
}
```

## Ruby

```ruby
def min_camera_cover(root)
  INF = 1 << 30
  dfs = nil
  dfs = ->(node) do
    return [INF, 0, 0] if node.nil?
    left = dfs.call(node.left)
    right = dfs.call(node.right)

    s0 = 1 + [left[0], left[1], left[2]].min + [right[0], right[1], right[2]].min
    s2 = left[1] + right[1]
    opt1 = left[0] + [right[0], right[1]].min
    opt2 = right[0] + [left[0], left[1]].min
    s1 = [opt1, opt2].min

    [s0, s1, s2]
  end

  res = dfs.call(root)
  [res[0], res[1]].min
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
    def minCameraCover(root: TreeNode): Int = {
        var cameras = 0

        // State definitions:
        // 0 -> this node needs a camera (not covered)
        // 1 -> this node is covered, no camera here
        // 2 -> this node has a camera
        def dfs(node: TreeNode): Int = {
            if (node == null) return 1 // null nodes are considered covered

            val leftState = dfs(node.left)
            val rightState = dfs(node.right)

            if (leftState == 0 || rightState == 0) {
                cameras += 1
                2 // place camera at current node
            } else if (leftState == 2 || rightState == 2) {
                1 // covered by child camera
            } else {
                0 // not covered, no camera here
            }
        }

        if (dfs(root) == 0) cameras += 1
        cameras
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution {}

impl Solution {
    pub fn min_camera_cover(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        const INF: i32 = 1_000_000;
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32, i32) {
            match node {
                None => (0, 0, INF),
                Some(rc) => {
                    let left = dfs(rc.borrow().left.clone());
                    let right = dfs(rc.borrow().right.clone());

                    // Place a camera at this node
                    let s2 = 1 + left.0.min(left.1).min(left.2)
                               + right.0.min(right.1).min(right.2);

                    // Node is not covered, children must be covered without cameras here
                    let s0 = left.1 + right.1;

                    // Node is covered without a camera; at least one child has a camera
                    let mut s1 = INF;
                    // left child has camera
                    s1 = s1.min(left.2 + right.1.min(right.2));
                    // right child has camera
                    s1 = s1.min(right.2 + left.1.min(left.2));

                    (s0, s1, s2)
                }
            }
        }

        let res = dfs(root);
        std::cmp::min(res.1, res.2)
    }
}

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
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

(define/contract (min-camera-cover root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ([camera-count (box 0)])
    (define (dfs node)
      (if (not node)
          2 ; null nodes are considered covered
          (let* ((left-state  (dfs (tree-node-left node)))
                 (right-state (dfs (tree-node-right node))))
            (cond
              [(or (= left-state 0) (= right-state 0))
               (set-box! camera-count (+ (unbox camera-count) 1))
               1]                                   ; place a camera here
              [(or (= left-state 1) (= right-state 1))
               2]                                   ; this node is covered
              [else
               0]))))                              ; not covered
    (let ([root-state (dfs root)])
      (when (= root-state 0)
        (set-box! camera-count (+ (unbox camera-count) 1)))
      (unbox camera-count))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                     left = null :: 'null' | #tree_node{},
                     right = null :: 'null' | #tree_node{}}).

-define(INF, 2000).

-spec min_camera_cover(Root :: #tree_node{} | null) -> integer().
min_camera_cover(Root) ->
    {_, S1, S2} = dfs(Root),
    erlang:min(S1, S2).

dfs(null) ->
    {?INF, 0, ?INF};
dfs(#tree_node{left = Left, right = Right}) ->
    {L0, L1, L2} = dfs(Left),
    {R0, R1, R2} = dfs(Right),

    MinL = erlang:min(L0, erlang:min(L1, L2)),
    MinR = erlang:min(R0, erlang:min(R1, R2)),

    S2 = 1 + MinL + MinR,
    S0 = erlang:min(L1, L2) + erlang:min(R1, R2),
    S1 = erlang:min(L2 + MinR, R2 + MinL),

    {S0, S1, S2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_camera_cover(root :: TreeNode.t() | nil) :: integer
  def min_camera_cover(root) do
    {state, cameras} = dfs(root)
    if state == 0, do: cameras + 1, else: cameras
  end

  defp dfs(nil), do: {1, 0}

  defp dfs(%TreeNode{left: left, right: right}) do
    {ls, lc} = dfs(left)
    {rs, rc} = dfs(right)
    cam = lc + rc

    cond do
      ls == 0 or rs == 0 ->
        {2, cam + 1}
      ls == 2 or rs == 2 ->
        {1, cam}
      true ->
        {0, cam}
    end
  end
end
```
