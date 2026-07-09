# 0894. All Possible Full Binary Trees

## Cpp

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

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
    unordered_map<int, vector<TreeNode*>> memo;
    
    vector<TreeNode*> build(int n) {
        if (memo.count(n)) return memo[n];
        vector<TreeNode*> res;
        if (n == 1) {
            res.push_back(new TreeNode(0));
        } else {
            for (int left = 1; left < n; left += 2) {
                int right = n - 1 - left;
                const auto& leftTrees = build(left);
                const auto& rightTrees = build(right);
                for (TreeNode* l : leftTrees) {
                    for (TreeNode* r : rightTrees) {
                        TreeNode* root = new TreeNode(0);
                        root->left = l;
                        root->right = r;
                        res.push_back(root);
                    }
                }
            }
        }
        memo[n] = res;
        return res;
    }
    
public:
    vector<TreeNode*> allPossibleFBT(int n) {
        if (n % 2 == 0) return {};
        return build(n);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private Map<Integer, List<TreeNode>> memo = new HashMap<>();

    public List<TreeNode> allPossibleFBT(int n) {
        if (n % 2 == 0) return new ArrayList<>();
        return generate(n);
    }

    private List<TreeNode> generate(int n) {
        if (memo.containsKey(n)) return memo.get(n);
        List<TreeNode> result = new ArrayList<>();
        if (n == 1) {
            result.add(new TreeNode(0));
        } else {
            for (int left = 1; left <= n - 2; left += 2) {
                int right = n - 1 - left;
                List<TreeNode> leftTrees = generate(left);
                List<TreeNode> rightTrees = generate(right);
                for (TreeNode l : leftTrees) {
                    for (TreeNode r : rightTrees) {
                        result.add(new TreeNode(0, l, r));
                    }
                }
            }
        }
        memo.put(n, result);
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
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n % 2 == 0:
            return []
        memo = {1: [TreeNode(0)]}

        def helper(nodes):
            if nodes in memo:
                return memo[nodes]
            trees = []
            for left_cnt in range(1, nodes, 2):
                right_cnt = nodes - 1 - left_cnt
                for left in helper(left_cnt):
                    for right in helper(right_cnt):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        trees.append(root)
            memo[nodes] = trees
            return trees

        return helper(n)
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
    def allPossibleFBT(self, n: int) -> List[Optional['TreeNode']]:
        if n % 2 == 0:
            return []
        
        from functools import lru_cache
        
        @lru_cache(None)
        def helper(nodes: int) -> List[Optional['TreeNode']]:
            if nodes == 1:
                return [TreeNode(0)]
            result = []
            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes
                left_subtrees = helper(left_nodes)
                right_subtrees = helper(right_nodes)
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        result.append(root)
            return result
        
        return helper(n)
```

## C

```c
#include <stdlib.h>

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct List {
    struct TreeNode **arr;
    int size;
};

/* Memoization table for n up to 20 (inclusive). */
static struct List memo[21];

/* Clone a binary tree. */
static struct TreeNode* clone(struct TreeNode* root) {
    if (!root) return NULL;
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = root->val;
    node->left = clone(root->left);
    node->right = clone(root->right);
    return node;
}

/* Recursive helper that returns all full binary trees with n nodes. */
static struct List allPossibleFBTRec(int n) {
    if (memo[n].size != -1) {
        return memo[n];
    }

    struct List result;
    result.size = 0;
    result.arr = NULL;

    if (n % 2 == 0) {               /* No full binary tree with even nodes */
        memo[n] = result;
        return result;
    }

    if (n == 1) {                   /* Base case: single node tree */
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = 0;
        node->left = NULL;
        node->right = NULL;

        result.arr = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        result.arr[0] = node;
        result.size = 1;

        memo[n] = result;
        return result;
    }

    for (int leftNodes = 1; leftNodes <= n - 2; leftNodes += 2) {
        int rightNodes = n - 1 - leftNodes;
        struct List leftList = allPossibleFBTRec(leftNodes);
        struct List rightList = allPossibleFBTRec(rightNodes);

        for (int i = 0; i < leftList.size; ++i) {
            for (int j = 0; j < rightList.size; ++j) {
                struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                root->val = 0;
                root->left = clone(leftList.arr[i]);
                root->right = clone(rightList.arr[j]);

                result.arr = (struct TreeNode**)realloc(result.arr,
                                 sizeof(struct TreeNode*) * (result.size + 1));
                result.arr[result.size++] = root;
            }
        }
    }

    memo[n] = result;
    return result;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** allPossibleFBT(int n, int* returnSize) {
    static int initialized = 0;
    if (!initialized) {
        for (int i = 0; i <= 20; ++i) {
            memo[i].size = -1;
            memo[i].arr = NULL;
        }
        initialized = 1;
    }

    struct List ans = allPossibleFBTRec(n);
    *returnSize = ans.size;
    return ans.arr;
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
    private readonly Dictionary<int, List<TreeNode>> memo = new Dictionary<int, List<TreeNode>>();

    public IList<TreeNode> AllPossibleFBT(int n) {
        if (n % 2 == 0) return new List<TreeNode>();
        return Helper(n);
    }

    private List<TreeNode> Helper(int n) {
        if (memo.ContainsKey(n)) return memo[n];

        var result = new List<TreeNode>();

        if (n == 1) {
            result.Add(new TreeNode(0));
        } else {
            for (int leftCount = 1; leftCount < n; leftCount += 2) {
                int rightCount = n - 1 - leftCount;
                var leftTrees = Helper(leftCount);
                var rightTrees = Helper(rightCount);

                foreach (var left in leftTrees) {
                    foreach (var right in rightTrees) {
                        var root = new TreeNode(0, left, right);
                        result.Add(root);
                    }
                }
            }
        }

        memo[n] = result;
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
 * @param {number} n
 * @return {TreeNode[]}
 */
var allPossibleFBT = function(n) {
    if (n % 2 === 0) return [];
    const memo = new Map();
    const build = (nodes) => {
        if (memo.has(nodes)) return memo.get(nodes);
        const res = [];
        if (nodes === 1) {
            res.push(new TreeNode(0));
        } else {
            for (let leftCount = 1; leftCount < nodes; leftCount += 2) {
                const rightCount = nodes - 1 - leftCount;
                const leftTrees = build(leftCount);
                const rightTrees = build(rightCount);
                for (const l of leftTrees) {
                    for (const r of rightTrees) {
                        const root = new TreeNode(0);
                        root.left = l;
                        root.right = r;
                        res.push(root);
                    }
                }
            }
        }
        memo.set(nodes, res);
        return res;
    };
    return build(n);
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

function allPossibleFBT(n: number): Array<TreeNode | null> {
    const memo = new Map<number, TreeNode[]>();

    function build(nodes: number): TreeNode[] {
        if (memo.has(nodes)) return memo.get(nodes)!;

        const result: TreeNode[] = [];

        if (nodes === 1) {
            result.push(new TreeNode(0));
        } else if (nodes % 2 === 1) { // only odd counts can form full binary trees
            for (let leftSize = 1; leftSize < nodes; leftSize += 2) {
                const rightSize = nodes - 1 - leftSize;
                const leftTrees = build(leftSize);
                const rightTrees = build(rightSize);

                for (const l of leftTrees) {
                    for (const r of rightTrees) {
                        const root = new TreeNode(0);
                        root.left = l;
                        root.right = r;
                        result.push(root);
                    }
                }
            }
        }

        memo.set(nodes, result);
        return result;
    }

    if (n % 2 === 0) return [];
    return build(n);
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
     * @var array<int, TreeNode[]>
     */
    private static $memo = [];

    /**
     * @param Integer $n
     * @return TreeNode[]
     */
    function allPossibleFBT($n) {
        if ($n % 2 == 0) {
            return [];
        }
        if (isset(self::$memo[$n])) {
            return self::$memo[$n];
        }
        if ($n == 1) {
            $single = new TreeNode(0);
            self::$memo[1] = [$single];
            return self::$memo[1];
        }

        $result = [];
        for ($leftNodes = 1; $leftNodes < $n; $leftNodes += 2) {
            $rightNodes = $n - 1 - $leftNodes;
            $leftTrees = $this->allPossibleFBT($leftNodes);
            $rightTrees = $this->allPossibleFBT($rightNodes);
            foreach ($leftTrees as $l) {
                foreach ($rightTrees as $r) {
                    $root = new TreeNode(0, $l, $r);
                    $result[] = $root;
                }
            }
        }

        self::$memo[$n] = $result;
        return $result;
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
    private var memo = [Int: [TreeNode]]()
    
    func allPossibleFBT(_ n: Int) -> [TreeNode?] {
        guard n % 2 == 1 else { return [] }
        return helper(n).map { $0 as TreeNode? }
    }
    
    private func helper(_ n: Int) -> [TreeNode] {
        if let cached = memo[n] {
            return cached
        }
        
        var result = [TreeNode]()
        if n == 1 {
            result.append(TreeNode(0))
        } else {
            for leftCount in stride(from: 1, through: n - 2, by: 2) {
                let rightCount = n - 1 - leftCount
                let leftTrees = helper(leftCount)
                let rightTrees = helper(rightCount)
                
                for l in leftTrees {
                    for r in rightTrees {
                        let root = TreeNode(0, l, r)
                        result.append(root)
                    }
                }
            }
        }
        
        memo[n] = result
        return result
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
    private val memo = HashMap<Int, List<TreeNode?>>()

    fun allPossibleFBT(n: Int): List<TreeNode?> {
        if (n % 2 == 0) return emptyList()
        return dfs(n)
    }

    private fun dfs(nodes: Int): List<TreeNode?> {
        memo[nodes]?.let { return it }
        val result = mutableListOf<TreeNode?>()
        if (nodes == 1) {
            result.add(TreeNode(0))
        } else {
            var leftSize = 1
            while (leftSize < nodes) {
                val rightSize = nodes - 1 - leftSize
                val leftTrees = dfs(leftSize)
                val rightTrees = dfs(rightSize)
                for (l in leftTrees) {
                    for (r in rightTrees) {
                        val root = TreeNode(0)
                        root.left = l
                        root.right = r
                        result.add(root)
                    }
                }
                leftSize += 2
            }
        }
        memo[nodes] = result
        return result
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
  final Map<int, List<TreeNode?>> _memo = {};

  List<TreeNode?> allPossibleFBT(int n) {
    if (n % 2 == 0) return [];
    return _allPossibleFBT(n);
  }

  List<TreeNode?> _allPossibleFBT(int n) {
    if (_memo.containsKey(n)) return _memo[n]!;

    final List<TreeNode?> res = [];

    if (n == 1) {
      res.add(TreeNode(0));
    } else {
      for (int leftNodes = 1; leftNodes < n; leftNodes += 2) {
        int rightNodes = n - 1 - leftNodes;
        final List<TreeNode?> leftList = _allPossibleFBT(leftNodes);
        final List<TreeNode?> rightList = _allPossibleFBT(rightNodes);

        for (final TreeNode? l in leftList) {
          for (final TreeNode? r in rightList) {
            final TreeNode root = TreeNode(0);
            root.left = l;
            root.right = r;
            res.add(root);
          }
        }
      }
    }

    _memo[n] = res;
    return res;
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

var memo = map[int][]*TreeNode{
	1: {{Val: 0}},
}

func allPossibleFBT(n int) []*TreeNode {
	if n%2 == 0 {
		return []*TreeNode{}
	}
	return helper(n)
}

func helper(n int) []*TreeNode {
	if res, ok := memo[n]; ok {
		return res
	}
	var ans []*TreeNode
	for leftCount := 1; leftCount < n; leftCount += 2 {
		rightCount := n - 1 - leftCount
		leftTrees := helper(leftCount)
		rightTrees := helper(rightCount)
		for _, l := range leftTrees {
			for _, r := range rightTrees {
				root := &TreeNode{Val: 0, Left: l, Right: r}
				ans = append(ans, root)
			}
		}
	}
	memo[n] = ans
	return ans
}
```

## Ruby

```ruby
def all_possible_fbt(n)
  @memo ||= {}
  return [] if n.even?
  return @memo[n] if @memo.key?(n)

  result = []
  if n == 1
    result << TreeNode.new(0)
  else
    (1...n).step(2) do |left|
      right = n - 1 - left
      left_trees = all_possible_fbt(left)
      right_trees = all_possible_fbt(right)
      left_trees.each do |l|
        right_trees.each do |r|
          root = TreeNode.new(0)
          root.left = l
          root.right = r
          result << root
        end
      end
    end
  end

  @memo[n] = result
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
  import scala.collection.mutable.{Map => MutableMap, ListBuffer}

  private val memo: MutableMap[Int, List[TreeNode]] = MutableMap(
    1 -> List(new TreeNode(0))
  )

  def allPossibleFBT(n: Int): List[TreeNode] = {
    if (n % 2 == 0) return Nil
    helper(n)
  }

  private def helper(n: Int): List[TreeNode] = {
    memo.getOrElseUpdate(n, {
      val res = ListBuffer[TreeNode]()
      for (i <- 1 until n by 2) {
        val leftList  = helper(i)
        val rightList = helper(n - i - 1)
        for (l <- leftList; r <- rightList) {
          val root = new TreeNode(0)
          root.left = l
          root.right = r
          res += root
        }
      }
      res.toList
    })
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn all_possible_fbt(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if n % 2 == 0 {
            return vec![];
        }
        let mut memo: HashMap<i32, Vec<Option<Rc<RefCell<TreeNode>>>>> = HashMap::new();
        Self::helper(n, &mut memo)
    }

    fn helper(
        n: i32,
        memo: &mut HashMap<i32, Vec<Option<Rc<RefCell<TreeNode>>>>>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if let Some(v) = memo.get(&n) {
            return v.clone();
        }
        let mut res = Vec::new();
        if n == 1 {
            res.push(Some(Rc::new(RefCell::new(TreeNode::new(0)))));
        } else {
            for left_nodes in (1..n).step_by(2) {
                let right_nodes = n - 1 - left_nodes;
                let left_trees = Self::helper(left_nodes, memo);
                let right_trees = Self::helper(right_nodes, memo);
                for l in &left_trees {
                    for r in &right_trees {
                        let node = TreeNode {
                            val: 0,
                            left: l.clone(),
                            right: r.clone(),
                        };
                        res.push(Some(Rc::new(RefCell::new(node))));
                    }
                }
            }
        }
        memo.insert(n, res.clone());
        res
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

;; Memoization table
(define memo (make-hash))

(: compute (-> exact-integer? (listof (or/c tree-node? #f))))
(define (compute n)
  (if (= n 1)
      (list (make-tree-node))
      (let ((result '()))
        (for ([i (in-range 1 n 2)])
          (let* ([left-list  (all-possible-fbt i)]
                 [right-list (all-possible-fbt (- n i 1))])
            (for* ([l left-list] [r right-list])
              (define root (make-tree-node))
              (set-tree-node-left!  root l)
              (set-tree-node-right! root r)
              (set! result (cons root result)))))
        (reverse result))))

(: all-possible-fbt (-> exact-integer? (listof (or/c tree-node? #f))))
(define (all-possible-fbt n)
  (if (odd? n)
      (hash-ref! memo n (lambda () (compute n)))
      '()))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                      left = null :: 'null' | #tree_node{},
                      right = null :: 'null' | #tree_node{}}).

-spec all_possible_fbt(N :: integer()) -> [#tree_node{}].
all_possible_fbt(N) ->
    case N rem 2 of
        0 -> [];
        _ -> all_possible_fbt_memo(N)
    end.

%% memoized helper using process dictionary
all_possible_fbt_memo(1) ->
    [#tree_node{}];
all_possible_fbt_memo(N) ->
    case get(N) of
        undefined ->
            Res = lists:foldl(
                fun(I, Acc) ->
                    LeftCount = I,
                    RightCount = N - I - 1,
                    LeftTrees = all_possible_fbt_memo(LeftCount),
                    RightTrees = all_possible_fbt_memo(RightCount),
                    Combined = [#tree_node{left=L, right=R} || L <- LeftTrees, R <- RightTrees],
                    Acc ++ Combined
                end,
                [],
                lists:seq(1, N - 2, 2)
            ),
            put(N, Res),
            Res;
        Trees -> Trees
    end.
```

## Elixir

```elixir
defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec all_possible_fbt(n :: integer) :: [TreeNode.t() | nil]
  def all_possible_fbt(n) when rem(n, 2) == 1 do
    generate(n)
  end

  def all_possible_fbt(_n), do: []

  defp generate(1), do: [%TreeNode{}]

  defp generate(n) do
    1..(n - 2)
    |> Enum.flat_map(fn i ->
      if rem(i, 2) == 1 do
        left_trees = generate(i)
        right_trees = generate(n - 1 - i)

        for l <- left_trees, r <- right_trees do
          %TreeNode{val: 0, left: l, right: r}
        end
      else
        []
      end
    end)
  end
end
```
