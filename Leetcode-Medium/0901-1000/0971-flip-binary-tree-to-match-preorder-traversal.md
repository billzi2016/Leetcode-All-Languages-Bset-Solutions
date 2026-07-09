# 0971. Flip Binary Tree To Match Preorder Traversal

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
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        idx = 0;
        ok = true;
        dfs(root, voyage);
        if (!ok) return {-1};
        return flips;
    }
private:
    int idx;
    bool ok;
    vector<int> flips;
    
    void dfs(TreeNode* node, const vector<int>& voyage) {
        if (!node || !ok) return;
        if (node->val != voyage[idx]) {
            ok = false;
            return;
        }
        ++idx;
        // If left child exists and does not match next expected value, we need to flip
        if (node->left && idx < (int)voyage.size() && node->left->val != voyage[idx]) {
            flips.push_back(node->val);
            // traverse right first then left
            dfs(node->right, voyage);
            dfs(node->left, voyage);
        } else {
            // normal order: left then right
            dfs(node->left, voyage);
            dfs(node->right, voyage);
        }
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int idx;
    private List<Integer> flips;
    private int[] voyage;
    private boolean ok = true;

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        this.idx = 0;
        this.flips = new ArrayList<>();
        this.voyage = voyage;
        dfs(root);
        if (!ok) {
            return Collections.singletonList(-1);
        }
        return flips;
    }

    private void dfs(TreeNode node) {
        if (!ok || node == null) {
            return;
        }
        if (node.val != voyage[idx++]) {
            ok = false;
            return;
        }
        // If left child exists and does not match the next expected value, we need to flip.
        if (node.left != null && idx < voyage.length && node.left.val != voyage[idx]) {
            flips.add(node.val);
            dfs(node.right);
            dfs(node.left);
        } else {
            dfs(node.left);
            dfs(node.right);
        }
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
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: Optional[TreeNode]
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.idx = 0
        self.voyage = voyage
        self.flips = []

        def dfs(node):
            if not node:
                return True
            # current node must match the expected value
            if self.idx >= len(self.voyage) or node.val != self.voyage[self.idx]:
                return False
            self.idx += 1

            # decide whether to flip based on next expected value
            if node.left and self.idx < len(self.voyage) and node.left.val != self.voyage[self.idx]:
                # need to flip this node
                self.flips.append(node.val)
                # traverse right first, then left
                if not dfs(node.right):
                    return False
                if not dfs(node.left):
                    return False
            else:
                # normal order: left then right
                if not dfs(node.left):
                    return False
                if not dfs(node.right):
                    return False
            return True

        if dfs(root):
            return self.flips
        else:
            return [-1]
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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.idx = 0
        self.res = []
        self.failed = False

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if self.idx >= len(voyage) or node.val != voyage[self.idx]:
                self.failed = True
                return False
            self.idx += 1

            # If left child exists and does not match the next expected value, flip.
            if node.left and self.idx < len(voyage) and node.left.val != voyage[self.idx]:
                self.res.append(node.val)
                # traverse right first then left (as if flipped)
                if not dfs(node.right):
                    return False
                if not dfs(node.left):
                    return False
            else:
                if not dfs(node.left):
                    return False
                if not dfs(node.right):
                    return False
            return True

        dfs(root)
        return [-1] if self.failed else self.res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static int *g_voyage;
static int g_n;
static int g_idx;
static int *g_res;
static int g_resCount;

static bool dfs(struct TreeNode* node) {
    if (!node) return true;
    if (g_idx >= g_n || node->val != g_voyage[g_idx]) return false;
    g_idx++;

    if (node->left && g_idx < g_n && node->left->val != g_voyage[g_idx]) {
        // need to flip this node
        g_res[g_resCount++] = node->val;
        if (!dfs(node->right)) return false;
        if (!dfs(node->left)) return false;
    } else {
        if (!dfs(node->left)) return false;
        if (!dfs(node->right)) return false;
    }
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* flipMatchVoyage(struct TreeNode* root, int* voyage, int voyageSize, int* returnSize) {
    g_voyage = voyage;
    g_n = voyageSize;
    g_idx = 0;
    g_resCount = 0;
    g_res = (int*)malloc(voyageSize * sizeof(int));

    if (!dfs(root)) {
        free(g_res);
        int* ans = (int*)malloc(sizeof(int));
        ans[0] = -1;
        *returnSize = 1;
        return ans;
    }

    *returnSize = g_resCount;
    return g_res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> FlipMatchVoyage(TreeNode root, int[] voyage) {
        var result = new List<int>();
        int index = 0;
        bool dfs(TreeNode node) {
            if (node == null) return true;
            if (index >= voyage.Length || node.val != voyage[index]) return false;
            index++;
            // If left child exists and does not match the next expected value, we need to flip.
            if (node.left != null && index < voyage.Length && node.left.val != voyage[index]) {
                result.Add(node.val);
                // Traverse right first then left after flipping.
                if (!dfs(node.right)) return false;
                if (!dfs(node.left)) return false;
            } else {
                if (!dfs(node.left)) return false;
                if (!dfs(node.right)) return false;
            }
            return true;
        }

        if (!dfs(root)) {
            return new List<int> { -1 };
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
 * @param {number[]} voyage
 * @return {number[]}
 */
var flipMatchVoyage = function(root, voyage) {
    let idx = 0;
    const flips = [];
    let possible = true;

    function dfs(node) {
        if (!node || !possible) return;
        if (node.val !== voyage[idx]) {
            possible = false;
            return;
        }
        idx++;
        // decide order based on next expected value
        if (
            node.left &&
            idx < voyage.length &&
            node.left.val !== voyage[idx]
        ) {
            flips.push(node.val);
            dfs(node.right);
            dfs(node.left);
        } else {
            dfs(node.left);
            dfs(node.right);
        }
    }

    dfs(root);
    return possible ? flips : [-1];
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

function flipMatchVoyage(root: TreeNode | null, voyage: number[]): number[] {
    const result: number[] = [];
    let idx = 0;
    let possible = true;

    function dfs(node: TreeNode | null): void {
        if (!node || !possible) return;
        if (node.val !== voyage[idx]) {
            possible = false;
            return;
        }
        idx++;

        // Determine if we need to flip at this node
        if (
            node.left &&
            idx < voyage.length &&
            node.left.val !== voyage[idx]
        ) {
            // Flip required: record and traverse right then left
            result.push(node.val);
            dfs(node.right);
            dfs(node.left);
        } else {
            dfs(node.left);
            dfs(node.right);
        }
    }

    dfs(root);
    return possible ? result : [-1];
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
    private int $idx = 0;
    private array $voyage = [];
    private array $flips = [];

    /**
     * @param TreeNode $root
     * @param Integer[] $voyage
     * @return Integer[]
     */
    function flipMatchVoyage($root, $voyage) {
        $this->idx = 0;
        $this->voyage = $voyage;
        $this->flips = [];

        if ($this->dfs($root)) {
            return $this->flips;
        }
        return [-1];
    }

    private function dfs($node): bool {
        if ($node === null) {
            return true;
        }
        $n = count($this->voyage);
        if ($this->idx >= $n || $node->val !== $this->voyage[$this->idx]) {
            return false;
        }
        $this->idx++;

        // Determine if we need to flip at this node
        if (
            $node->left !== null &&
            $this->idx < $n &&
            $node->left->val !== $this->voyage[$this->idx]
        ) {
            $this->flips[] = $node->val;
            // Traverse right first, then left
            if (!$this->dfs($node->right)) return false;
            if (!$this->dfs($node->left)) return false;
        } else {
            // Normal preorder: left then right
            if (!$this->dfs($node->left)) return false;
            if (!$this->dfs($node->right)) return false;
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
    private var idx = 0
    private var result = [Int]()
    private var voyage = [Int]()
    private var possible = true

    func flipMatchVoyage(_ root: TreeNode?, _ voyage: [Int]) -> [Int] {
        self.idx = 0
        self.result.removeAll()
        self.voyage = voyage
        self.possible = true
        dfs(root)
        return possible ? result : [-1]
    }

    private func dfs(_ node: TreeNode?) {
        guard let node = node else { return }
        if idx >= voyage.count || node.val != voyage[idx] {
            possible = false
            return
        }
        idx += 1

        // Determine if a flip is needed
        if let left = node.left,
           idx < voyage.count,
           left.val != voyage[idx] {
            result.append(node.val)
            dfs(node.right)
            dfs(node.left)
        } else {
            dfs(node.left)
            dfs(node.right)
        }
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
    fun flipMatchVoyage(root: TreeNode?, voyage: IntArray): List<Int> {
        val flips = mutableListOf<Int>()
        var idx = 0

        fun dfs(node: TreeNode?): Boolean {
            if (node == null) return true
            if (idx >= voyage.size || node.`val` != voyage[idx]) return false
            idx++

            // If left child exists and does not match the next expected value, we need to flip.
            if (node.left != null && idx < voyage.size && node.left!!.`val` != voyage[idx]) {
                flips.add(node.`val`)
                // Traverse right subtree first after flip.
                if (!dfs(node.right)) return false
                if (!dfs(node.left)) return false
            } else {
                if (!dfs(node.left)) return false
                if (!dfs(node.right)) return false
            }
            return true
        }

        return if (dfs(root)) flips else listOf(-1)
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
  int _idx = 0;
  bool _possible = true;
  List<int> _flipped = [];

  void _dfs(TreeNode? node, List<int> voyage) {
    if (node == null || !_possible) return;
    if (_idx >= voyage.length || node.val != voyage[_idx]) {
      _possible = false;
      return;
    }
    _idx++;
    // If left child exists and its value doesn't match the next expected voyage value,
    // we need to flip this node.
    if (node.left != null && _idx < voyage.length && node.left!.val != voyage[_idx]) {
      _flipped.add(node.val);
      _dfs(node.right, voyage);
      _dfs(node.left, voyage);
    } else {
      _dfs(node.left, voyage);
      _dfs(node.right, voyage);
    }
  }

  List<int> flipMatchVoyage(TreeNode? root, List<int> voyage) {
    _idx = 0;
    _possible = true;
    _flipped.clear();
    _dfs(root, voyage);
    return _possible ? _flipped : [-1];
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
func flipMatchVoyage(root *TreeNode, voyage []int) []int {
	var res []int
	idx := 0

	var dfs func(node *TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		if idx >= len(voyage) || node.Val != voyage[idx] {
			return false
		}
		idx++

		// If left child exists and does not match the next expected value, flip.
		if node.Left != nil && idx < len(voyage) && node.Left.Val != voyage[idx] {
			res = append(res, node.Val)
			if !dfs(node.Right) {
				return false
			}
			if !dfs(node.Left) {
				return false
			}
		} else {
			if !dfs(node.Left) {
				return false
			}
			if !dfs(node.Right) {
				return false
			}
		}
		return true
	}

	if dfs(root) {
		return res
	}
	return []int{-1}
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

def flip_match_voyage(root, voyage)
  @idx = 0
  @voyage = voyage
  @flips = []
  @possible = true

  dfs = lambda do |node|
    return if node.nil? || !@possible
    if node.val != @voyage[@idx]
      @possible = false
      return
    end
    @idx += 1

    if node.left && @idx < @voyage.size && node.left.val != @voyage[@idx]
      @flips << node.val
      dfs.call(node.right)
      dfs.call(node.left)
    else
      dfs.call(node.left)
      dfs.call(node.right)
    end
  end

  dfs.call(root)

  @possible ? @flips : [-1]
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
  import scala.collection.mutable.ListBuffer

  def flipMatchVoyage(root: TreeNode, voyage: Array[Int]): List[Int] = {
    val n = voyage.length
    var idx = 0
    val flips = ListBuffer[Int]()

    def dfs(node: TreeNode): Boolean = {
      if (node == null) return true
      if (idx >= n || node.value != voyage(idx)) return false
      idx += 1

      // Determine if we need to flip at this node
      if (node.left != null && idx < n && node.left.value != voyage(idx)) {
        // Flip required: visit right then left
        flips += node.value
        if (!dfs(node.right)) return false
        if (!dfs(node.left)) return false
      } else {
        // Normal order: left then right
        if (!dfs(node.left)) return false
        if (!dfs(node.right)) return false
      }
      true
    }

    if (dfs(root) && idx == n) flips.toList else List(-1)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

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
        TreeNode { val, left: None, right: None }
    }
}

pub struct Solution;

impl Solution {
    pub fn flip_match_voyage(root: Option<Rc<RefCell<TreeNode>>>, voyage: Vec<i32>) -> Vec<i32> {
        fn dfs(
            node_opt: Option<Rc<RefCell<TreeNode>>>,
            voyage: &Vec<i32>,
            idx: &mut usize,
            flips: &mut Vec<i32>,
        ) -> bool {
            if let Some(rc_node) = node_opt {
                let node_ref = rc_node.borrow();
                if *idx >= voyage.len() || node_ref.val != voyage[*idx] {
                    return false;
                }
                *idx += 1;

                // Determine if we need to flip
                if let Some(left_rc) = &node_ref.left {
                    if *idx < voyage.len() && left_rc.borrow().val != voyage[*idx] {
                        // Flip required
                        flips.push(node_ref.val);
                        // Visit right first, then left
                        if !dfs(node_ref.right.clone(), voyage, idx, flips) {
                            return false;
                        }
                        if !dfs(Some(left_rc.clone()), voyage, idx, flips) {
                            return false;
                        }
                        return true;
                    }
                }

                // Normal order: left then right
                if !dfs(node_ref.left.clone(), voyage, idx, flips) {
                    return false;
                }
                if !dfs(node_ref.right.clone(), voyage, idx, flips) {
                    return false;
                }
            }
            true
        }

        let mut idx = 0usize;
        let mut flips = Vec::new();
        if dfs(root, &voyage, &mut idx, &mut flips) {
            flips
        } else {
            vec![-1]
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

(define/contract (flip-match-voyage root voyage)
  (-> (or/c tree-node? #f) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length voyage))
         (idx (box 0))
         (flips '()))
    (define (dfs node)
      (if (not node)
          #t
          (let ((pos (unbox idx)))
            (if (>= pos n)
                #f
                (let ((expected (list-ref voyage pos)))
                  (if (not (= (tree-node-val node) expected))
                      #f
                      (begin
                        (set-box! idx (+ pos 1))
                        (define left (tree-node-left node))
                        (define right (tree-node-right node))
                        (cond
                          [(and left right)
                           (let ((next-pos (unbox idx)))
                             (if (>= next-pos n)
                                 #f
                                 (let ((next-expected (list-ref voyage next-pos)))
                                   (cond
                                     [(= (tree-node-val left) next-expected)
                                      (and (dfs left) (dfs right))]
                                     [(= (tree-node-val right) next-expected)
                                      (set! flips (cons (tree-node-val node) flips))
                                      (and (dfs right) (dfs left))]
                                     [else #f])))))]
                          [else
                           (and (dfs left) (dfs right))]))))))))
    (if (dfs root)
        (reverse flips)
        (list -1))))
```

## Erlang

```erlang
-module(solution).
-export([flip_match_voyage/2]).

-record(tree_node, {
    val = 0 :: integer(),
    left = null :: 'null' | #tree_node{},
    right = null :: 'null' | #tree_node{}
}).

%% Helper to get element at zero‑based Index
get(Index, List) ->
    lists:nth(Index + 1, List).

%% Depth‑first traversal that records flips
dfs(null, _Voyage, Index) ->
    {Index, [], ok};
dfs(Node, Voyage, Index) ->
    Val = Node#tree_node.val,
    Expected = get(Index, Voyage),
    if
        Val =/= Expected ->
            {Index, [], error};
        true ->
            Index1 = Index + 1,
            Left = Node#tree_node.left,
            Right = Node#tree_node.right,
            case {Left, Right} of
                {null, null} ->
                    {Index1, [], ok};
                {null, R} when R =/= null ->
                    NextExp = get(Index1, Voyage),
                    if
                        (R#tree_node.val) =:= NextExp ->
                            dfs(R, Voyage, Index1);
                        true ->
                            {Index1, [], error}
                    end;
                {L, null} when L =/= null ->
                    NextExp = get(Index1, Voyage),
                    if
                        (L#tree_node.val) =:= NextExp ->
                            dfs(L, Voyage, Index1);
                        true ->
                            {Index1, [], error}
                    end;
                {L, R} ->
                    NextExp = get(Index1, Voyage),
                    case L#tree_node.val of
                        NextExp ->
                            %% No flip needed: left then right
                            {Idx2, FlipsL, ResL} = dfs(L, Voyage, Index1),
                            case ResL of
                                error -> {Idx2, [], error};
                                ok ->
                                    {Idx3, FlipsR, ResR} = dfs(R, Voyage, Idx2),
                                    case ResR of
                                        error -> {Idx3, [], error};
                                        ok -> {Idx3, FlipsL ++ FlipsR, ok}
                                    end
                            end;
                        _ ->
                            %% Try flip: right must match next expected value
                            case R#tree_node.val of
                                NextExp ->
                                    {Idx2, FlipsR, ResR} = dfs(R, Voyage, Index1),
                                    case ResR of
                                        error -> {Idx2, [], error};
                                        ok ->
                                            {Idx3, FlipsL, ResL} = dfs(L, Voyage, Idx2),
                                            case ResL of
                                                error -> {Idx3, [], error};
                                                ok -> {Idx3, [Val] ++ FlipsR ++ FlipsL, ok}
                                            end
                                    end;
                                _ ->
                                    {Index1, [], error}
                            end
                    end
            end
    end.

-spec flip_match_voyage(Root :: #tree_node{} | null, Voyage :: [integer()]) -> [integer()].
flip_match_voyage(Root, Voyage) ->
    case dfs(Root, Voyage, 0) of
        {_Idx, Flips, ok} -> Flips;
        _ -> [-1]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec flip_match_voyage(root :: TreeNode.t | nil, voyage :: [integer]) :: [integer]
  def flip_match_voyage(root, voyage) do
    case dfs(root, voyage, []) do
      {:ok, [], flips} -> Enum.reverse(flips)
      _ -> [-1]
    end
  end

  # When node is nil, just return the remaining voyage unchanged.
  defp dfs(nil, voyage, flips), do: {:ok, voyage, flips}

  # Mismatch when we still have a node but no more expected values.
  defp dfs(_node, [], _flips), do: :error

  defp dfs(%TreeNode{val: v, left: l, right: r} = node, [expected | rest] = voyage, flips) do
    if v != expected do
      :error
    else
      case {l, r} do
        {nil, nil} ->
          {:ok, rest, flips}

        {left, nil} ->
          dfs(left, rest, flips)

        {nil, right} ->
          dfs(right, rest, flips)

        {left, right} ->
          case rest do
            [] ->
              :error

            [next_expected | _] ->
              if left.val != next_expected do
                # need to flip; right must match the expected value
                if right.val == next_expected do
                  new_flips = [v | flips]

                  with {:ok, after_right, flips2} <- dfs(right, rest, new_flips),
                       {:ok, after_left, flips3} <- dfs(left, after_right, flips2) do
                    {:ok, after_left, flips3}
                  else
                    _ -> :error
                  end
                else
                  :error
                end
              else
                # no flip needed; traverse left then right
                with {:ok, after_left, flips2} <- dfs(left, rest, flips),
                     {:ok, after_right, flips3} <- dfs(right, after_left, flips2) do
                  {:ok, after_right, flips3}
                else
                  _ -> :error
                end
              end
          end
      end
    end
  end
end
```
