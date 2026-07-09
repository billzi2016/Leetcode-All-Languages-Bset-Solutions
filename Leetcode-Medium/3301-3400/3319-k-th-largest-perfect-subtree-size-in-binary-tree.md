# 3319. K-th Largest Perfect Subtree Size in Binary Tree

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
    struct Info {
        bool perfect;
        int height; // height from node to leaves (leaf = 0)
        int size;   // number of nodes in the subtree
    };
    
    vector<int> sizes;
    
    Info dfs(TreeNode* node) {
        if (!node) return {false, -1, 0};
        
        auto leftInfo = dfs(node->left);
        auto rightInfo = dfs(node->right);
        
        bool perfect = false;
        int height = 0, sz = 0;
        
        // leaf case
        if (!node->left && !node->right) {
            perfect = true;
            height = 0;
            sz = 1;
        }
        // internal node must have both children and their subtrees perfect with equal height
        else if (node->left && node->right && leftInfo.perfect && rightInfo.perfect &&
                 leftInfo.height == rightInfo.height) {
            perfect = true;
            height = leftInfo.height + 1;
            sz = leftInfo.size + rightInfo.size + 1;
        }
        
        if (perfect) sizes.push_back(sz);
        return {perfect, height, sz};
    }
    
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        dfs(root);
        sort(sizes.begin(), sizes.end(), greater<int>());
        if ((int)sizes.size() < k) return -1;
        return sizes[k-1];
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
    public int kthLargestPerfectSubtree(TreeNode root, int k) {
        List<Integer> sizes = new ArrayList<>();
        dfs(root, sizes);
        Collections.sort(sizes, Collections.reverseOrder());
        return (k <= sizes.size()) ? sizes.get(k - 1) : -1;
    }

    // Returns the height of a perfect subtree rooted at node,
    // or -1 if the subtree is not perfect.
    private int dfs(TreeNode node, List<Integer> sizes) {
        if (node == null) return -1;
        if (node.left == null && node.right == null) {
            sizes.add(1);
            return 0; // height of a leaf
        }
        int leftH = dfs(node.left, sizes);
        int rightH = dfs(node.right, sizes);
        if (leftH == -1 || rightH == -1) return -1;
        if (leftH != rightH) return -1;

        int curHeight = leftH + 1; // height of current perfect subtree
        int size = (1 << (curHeight + 1)) - 1; // nodes = 2^{h+1} - 1
        sizes.add(size);
        return curHeight;
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
    def kthLargestPerfectSubtree(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        perfect_sizes = []

        def dfs(node):
            if not node:
                # Null subtree is not considered a perfect binary tree for this problem
                return (False, -1, 0)  # is_perfect, height, size
            left_perf, left_h, left_sz = dfs(node.left)
            right_perf, right_h, right_sz = dfs(node.right)

            # Leaf node case
            if not node.left and not node.right:
                perfect_sizes.append(1)
                return (True, 0, 1)

            # Internal node must have both children present and be perfect with equal height
            if left_perf and right_perf and left_h == right_h:
                sz = left_sz + right_sz + 1
                h = left_h + 1
                perfect_sizes.append(sz)
                return (True, h, sz)

            # Not a perfect subtree
            return (False, -1, 0)

        dfs(root)

        if len(perfect_sizes) < k:
            return -1
        perfect_sizes.sort(reverse=True)
        return perfect_sizes[k-1]
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
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_sizes = []

        def dfs(node):
            if not node:
                # Empty tree is considered perfect with height -1 and size 0
                return True, -1, 0
            left_perf, left_h, left_sz = dfs(node.left)
            right_perf, right_h, right_sz = dfs(node.right)

            if left_perf and right_perf and left_h == right_h:
                h = left_h + 1
                sz = left_sz + right_sz + 1
                perfect_sizes.append(sz)
                return True, h, sz
            else:
                # Not a perfect subtree; height/size are irrelevant for ancestors
                return False, 0, 0

        dfs(root)

        if len(perfect_sizes) < k:
            return -1
        perfect_sizes.sort(reverse=True)
        return perfect_sizes[k - 1]
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

static int cmp_desc(const void *a, const void *b) {
    return *(int *)b - *(int *)a;
}

/* Returns height of perfect subtree rooted at node,
   or -1 if not perfect. Collects sizes in the array. */
static int dfs(struct TreeNode *node, int *sizes, int *cnt) {
    if (!node) return -1;
    if (!node->left && !node->right) {
        sizes[(*cnt)++] = 1;               // leaf is a perfect subtree of size 1
        return 0;                          // height 0
    }
    int leftH = dfs(node->left, sizes, cnt);
    int rightH = dfs(node->right, sizes, cnt);
    if (leftH != -1 && rightH != -1 && leftH == rightH) {
        int h = leftH + 1;
        int size = (1 << (h + 1)) - 1;     // nodes in a perfect binary tree of height h
        sizes[(*cnt)++] = size;
        return h;
    }
    return -1;                             // not a perfect subtree
}

int kthLargestPerfectSubtree(struct TreeNode* root, int k) {
    int sizes[2005];
    int cnt = 0;
    dfs(root, sizes, &cnt);
    if (cnt < k) return -1;
    qsort(sizes, cnt, sizeof(int), cmp_desc);
    return sizes[k - 1];
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
    public int KthLargestPerfectSubtree(TreeNode root, int k) {
        List<int> sizes = new List<int>();
        Dfs(root, sizes);
        if (sizes.Count < k) return -1;
        sizes.Sort((a, b) => b.CompareTo(a));
        return sizes[k - 1];
    }

    private (bool isPerfect, int height, int size) Dfs(TreeNode node, List<int> sizes) {
        if (node == null) return (false, 0, 0);
        if (node.left == null && node.right == null) {
            sizes.Add(1);
            return (true, 1, 1);
        }

        var left = Dfs(node.left, sizes);
        var right = Dfs(node.right, sizes);

        if (left.isPerfect && right.isPerfect && left.height == right.height) {
            int height = left.height + 1;
            int size = left.size + right.size + 1;
            sizes.Add(size);
            return (true, height, size);
        }

        return (false, 0, 0);
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
 * @param {number} k
 * @return {number}
 */
var kthLargestPerfectSubtree = function(root, k) {
    const sizes = [];
    
    function dfs(node) {
        if (!node) return { isPerfect: true, height: 0, size: 0 };
        
        const left = dfs(node.left);
        const right = dfs(node.right);
        
        // leaf node forms a perfect subtree of size 1
        if (!node.left && !node.right) {
            sizes.push(1);
            return { isPerfect: true, height: 1, size: 1 };
        }
        
        // internal node must have both children and their subtrees must be perfect with equal heights
        if (node.left && node.right && left.isPerfect && right.isPerfect && left.height === right.height) {
            const sz = left.size + right.size + 1; // also equals 2 * left.size + 1
            sizes.push(sz);
            return { isPerfect: true, height: left.height + 1, size: sz };
        }
        
        // not a perfect subtree rooted at this node
        return { isPerfect: false, height: 0, size: 0 };
    }
    
    dfs(root);
    
    sizes.sort((a, b) => b - a); // descending order
    
    return k <= sizes.length ? sizes[k - 1] : -1;
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

function kthLargestPerfectSubtree(root: TreeNode | null, k: number): number {
    const sizes: number[] = [];

    function dfs(node: TreeNode | null): { perfect: boolean; height: number } {
        if (!node) return { perfect: true, height: -1 };
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left.perfect && right.perfect && left.height === right.height) {
            const h = left.height + 1;
            // size of a perfect binary tree with height h is 2^(h+1)-1
            const size = (1 << (h + 1)) - 1;
            sizes.push(size);
            return { perfect: true, height: h };
        }
        return { perfect: false, height: 0 };
    }

    dfs(root);

    sizes.sort((a, b) => b - a);
    return k <= sizes.length ? sizes[k - 1] : -1;
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
     * @param Integer $k
     * @return Integer
     */
    function kthLargestPerfectSubtree($root, $k) {
        $sizes = [];
        $this->dfs($root, $sizes);
        rsort($sizes); // descending order
        if (count($sizes) < $k) {
            return -1;
        }
        return $sizes[$k - 1];
    }

    /**
     * @param TreeNode|null $node
     * @param array &$sizes
     * @return array [bool $isPerfect, int $height, int $size]
     */
    private function dfs($node, &$sizes) {
        if ($node === null) {
            // An empty subtree is considered perfect with height -1 and size 0.
            return [true, -1, 0];
        }

        list($leftPerfect, $leftHeight, $leftSize) = $this->dfs($node->left, $sizes);
        list($rightPerfect, $rightHeight, $rightSize) = $this->dfs($node->right, $sizes);

        $isPerfect = $leftPerfect && $rightPerfect && ($leftHeight === $rightHeight);
        if ($isPerfect) {
            $height = $leftHeight + 1;
            $size   = $leftSize + $rightSize + 1;
            $sizes[] = $size;
            return [$isPerfect, $height, $size];
        } else {
            // Height and size are irrelevant when not perfect.
            return [false, 0, 0];
        }
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
    func kthLargestPerfectSubtree(_ root: TreeNode?, _ k: Int) -> Int {
        var sizes = [Int]()
        
        func dfs(_ node: TreeNode?) -> (isPerfect: Bool, height: Int, size: Int) {
            guard let n = node else { return (true, 0, 0) }
            let left = dfs(n.left)
            let right = dfs(n.right)
            
            if left.isPerfect && right.isPerfect && left.height == right.height {
                let h = left.height + 1
                let sz = left.size + right.size + 1
                sizes.append(sz)
                return (true, h, sz)
            } else {
                return (false, 0, 0)
            }
        }
        
        _ = dfs(root)
        if k > sizes.count { return -1 }
        sizes.sort(by: >)
        return sizes[k - 1]
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
    fun kthLargestPerfectSubtree(root: TreeNode?, k: Int): Int {
        val sizes = mutableListOf<Int>()
        fun dfs(node: TreeNode?): Pair<Boolean, Int> {
            if (node == null) return true to -1  // empty subtree is perfect with height -1
            val left = dfs(node.left)
            val right = dfs(node.right)

            var isPerfect = false
            var height = 0
            if (left.first && right.first && left.second == right.second) {
                isPerfect = true
                height = left.second + 1
                // size of a perfect binary tree with given height: 2^(height+1) - 1
                val size = (1 shl (height + 1)) - 1
                sizes.add(size)
            }
            return isPerfect to height
        }

        dfs(root)

        if (sizes.size < k) return -1
        sizes.sortDescending()
        return sizes[k - 1]
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
  int kthLargestPerfectSubtree(TreeNode? root, int k) {
    List<int> sizes = [];

    int? dfs(TreeNode? node) {
      if (node == null) return null;

      // Recurse first to gather perfect subtrees in children
      int? leftH = dfs(node.left);
      int? rightH = dfs(node.right);

      // Leaf node forms a perfect subtree of size 1
      if (node.left == null && node.right == null) {
        sizes.add(1);
        return 0;
      }

      // Node is perfect if both children are perfect and have same height
      if (leftH != null && rightH != null && leftH == rightH) {
        int h = leftH + 1; // height of current subtree
        int sz = (1 << (h + 1)) - 1; // size = 2^{h+1} - 1
        sizes.add(sz);
        return h;
      }

      // Not a perfect subtree
      return null;
    }

    dfs(root);

    sizes.sort((a, b) => b.compareTo(a));
    if (k - 1 < sizes.length) {
      return sizes[k - 1];
    }
    return -1;
  }
}
```

## Golang

```go
import "sort"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthLargestPerfectSubtree(root *TreeNode, k int) int {
	var sizes []int
	var dfs func(*TreeNode) (int, bool)
	dfs = func(node *TreeNode) (int, bool) {
		if node == nil {
			return -1, true // empty subtree is perfect with height -1
		}
		lh, lp := dfs(node.Left)
		rh, rp := dfs(node.Right)
		if lp && rp && lh == rh {
			h := lh + 1
			size := (1 << (h + 1)) - 1
			sizes = append(sizes, size)
			return h, true
		}
		return 0, false
	}
	dfs(root)

	sort.Slice(sizes, func(i, j int) bool { return sizes[i] > sizes[j] })
	if k <= len(sizes) {
		return sizes[k-1]
	}
	return -1
}
```

## Ruby

```ruby
def kth_largest_perfect_subtree(root, k)
  sizes = []
  dfs = nil
  dfs = ->(node) do
    return [true, 0, -1] if node.nil?

    left_perf, left_sz, left_h = dfs.call(node.left)
    right_perf, right_sz, right_h = dfs.call(node.right)

    if left_perf && right_perf && left_h == right_h
      sz = left_sz + right_sz + 1
      h = left_h + 1
      sizes << sz
      [true, sz, h]
    else
      [false, 0, 0]
    end
  end

  dfs.call(root)
  return -1 if k > sizes.length
  sizes.sort.reverse[k - 1]
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
    def kthLargestPerfectSubtree(root: TreeNode, k: Int): Int = {
        import scala.collection.mutable.ArrayBuffer

        val sizes = ArrayBuffer[Int]()

        def dfs(node: TreeNode): (Boolean, Int, Int) = {
            if (node == null) return (true, -1, 0) // empty subtree considered perfect with height -1
            val (lp, lh, ls) = dfs(node.left)
            val (rp, rh, rs) = dfs(node.right)

            if (lp && rp && lh == rh) {
                val h = lh + 1
                val sz = ls + rs + 1
                sizes += sz
                (true, h, sz)
            } else {
                (false, 0, 0)
            }
        }

        dfs(root)

        if (sizes.isEmpty) return -1
        val sorted = sizes.sorted(Ordering[Int].reverse)
        if (k <= sorted.length) sorted(k - 1) else -1
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

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

pub struct Solution;

impl Solution {
    pub fn kth_largest_perfect_subtree(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut sizes = Vec::new();
        Self::dfs(&root, &mut sizes);
        if k as usize == 0 {
            return -1;
        }
        sizes.sort_unstable_by(|a, b| b.cmp(a));
        let idx = (k - 1) as usize;
        if idx < sizes.len() {
            sizes[idx]
        } else {
            -1
        }
    }

    // Returns (is_perfect, height, size)
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, sizes: &mut Vec<i32>) -> (bool, i32, i32) {
        match node {
            None => (true, -1, 0), // empty subtree is perfect with height -1
            Some(rc) => {
                let left = rc.borrow().left.clone();
                let right = rc.borrow().right.clone();

                let (l_perf, l_h, l_sz) = Self::dfs(&left, sizes);
                let (r_perf, r_h, r_sz) = Self::dfs(&right, sizes);

                if l_perf && r_perf && l_h == r_h {
                    let height = l_h + 1;
                    let size = l_sz + r_sz + 1;
                    sizes.push(size);
                    (true, height, size)
                } else {
                    (false, 0, 0)
                }
            }
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

(define/contract (kth-largest-perfect-subtree root k)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (let ([sizes '()]) ; list of sizes of perfect subtrees
    (define (dfs node)
      (if (not node)
          (values #t -1 0)               ; empty subtree: perfect, height -1, size 0
          (let-values ([(lp lh ls) (dfs (tree-node-left node))]
                       [(rp rh rs) (dfs (tree-node-right node))])
            (if (and lp rp (= lh rh))
                (let* ([h (+ lh 1)]
                       [sz (+ ls rs 1)])
                  (set! sizes (cons sz sizes))
                  (values #t h sz))
                (values #f 0 0)))))
    (dfs root)
    (define sorted (sort sizes >))
    (if (< (length sorted) k)
        -1
        (list-ref sorted (- k 1)))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec kth_largest_perfect_subtree(Root :: #tree_node{} | null, K :: integer()) -> integer().
kth_largest_perfect_subtree(null, _K) ->
    -1;
kth_largest_perfect_subtree(Root, K) when K > 0 ->
    {_Perf, _H, _S, Sizes} = traverse(Root, []),
    SortedDesc = lists:reverse(lists:sort(Sizes)),
    case length(SortedDesc) >= K of
        true -> lists:nth(K, SortedDesc);
        false -> -1
    end.

-spec traverse(Node :: #tree_node{} | null, Acc :: [integer()]) ->
          {boolean(), integer(), integer(), [integer()]}.
traverse(null, Acc) ->
    {false, 0, 0, Acc};
traverse(Node, Acc) ->
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    case {Left, Right} of
        {null, null} ->
            NewAcc = [1 | Acc],
            {true, 1, 1, NewAcc};
        _ ->
            {LPerf, LH, LS, Acc1} = traverse(Left, Acc),
            {RPerf, RH, RS, Acc2} = traverse(Right, Acc1),
            if LPerf andalso RPerf andalso LH =:= RH ->
                    Size = LS + RS + 1,
                    Height = LH + 1,
                    NewAcc = [Size | Acc2],
                    {true, Height, Size, NewAcc};
               true ->
                    {false, 0, 0, Acc2}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_largest_perfect_subtree(root :: TreeNode.t() | nil, k :: integer) :: integer
  def kth_largest_perfect_subtree(root, k) do
    {_perf, _depth, _size, sizes} = dfs(root)

    sorted = Enum.sort(sizes, &>=/2)

    case Enum.at(sorted, k - 1) do
      nil -> -1
      v -> v
    end
  end

  defp dfs(nil), do: {true, -1, 0, []}

  defp dfs(%TreeNode{left: left, right: right}) do
    {lp, ld, ls, llist} = dfs(left)
    {rp, rd, rs, rlist} = dfs(right)

    combined = llist ++ rlist

    if lp and rp and ld == rd do
      depth = ld + 1
      size = ls + rs + 1
      {true, depth, size, [size | combined]}
    else
      {false, nil, nil, combined}
    end
  end
end
```
