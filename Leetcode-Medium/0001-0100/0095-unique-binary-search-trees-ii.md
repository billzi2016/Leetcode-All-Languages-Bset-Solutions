# 0095. Unique Binary Search Trees II

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
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        unordered_map<long long, vector<TreeNode*>> memo;
        return build(1, n, memo);
    }
private:
    vector<TreeNode*> build(int start, int end,
                            unordered_map<long long, vector<TreeNode*>>& memo) {
        long long key = (static_cast<long long>(start) << 32) | static_cast<unsigned int>(end);
        if (memo.find(key) != memo.end()) return memo[key];
        vector<TreeNode*> res;
        if (start > end) {
            res.push_back(nullptr);
            memo[key] = res;
            return res;
        }
        for (int i = start; i <= end; ++i) {
            vector<TreeNode*> leftTrees  = build(start, i - 1, memo);
            vector<TreeNode*> rightTrees = build(i + 1, end, memo);
            for (TreeNode* l : leftTrees) {
                for (TreeNode* r : rightTrees) {
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        memo[key] = res;
        return res;
    }
};
```

## Java

```java
import java.util.*;

public class Solution {
    private Map<String, List<TreeNode>> memo = new HashMap<>();

    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new ArrayList<>();
        return generate(1, n);
    }

    private List<TreeNode> generate(int start, int end) {
        String key = start + "," + end;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        List<TreeNode> res = new ArrayList<>();
        if (start > end) {
            res.add(null);
            memo.put(key, res);
            return res;
        }

        for (int i = start; i <= end; i++) {
            List<TreeNode> leftTrees = generate(start, i - 1);
            List<TreeNode> rightTrees = generate(i + 1, end);
            for (TreeNode left : leftTrees) {
                for (TreeNode right : rightTrees) {
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    res.add(root);
                }
            }
        }

        memo.put(key, res);
        return res;
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        memo = {}
        
        def build(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            
            trees = []
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        node = TreeNode(root_val)
                        node.left = left
                        node.right = right
                        trees.append(node)
            memo[(start, end)] = trees
            return trees
        
        return build(1, n)
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
    def generateTrees(self, n: int) -> List[Optional['TreeNode']]:
        if n == 0:
            return []
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def build(start: int, end: int):
            trees = []
            if start > end:
                trees.append(None)
                return tuple(trees)  # cache needs hashable
            
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return tuple(trees)  # store as immutable for caching
        
        result = list(build(1, n))
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    struct TreeNode **trees;
    int size;
} Result;

static Result *memo[9][9];  // n <= 8

static Result* gen(int start, int end) {
    if (start > end) {
        Result *res = (Result *)malloc(sizeof(Result));
        res->size = 1;
        res->trees = (struct TreeNode **)malloc(sizeof(struct TreeNode *));
        res->trees[0] = NULL;
        return res;
    }
    if (memo[start][end])
        return memo[start][end];

    int cap = 256;
    struct TreeNode **list = (struct TreeNode **)malloc(cap * sizeof(struct TreeNode *));
    int cnt = 0;

    for (int i = start; i <= end; ++i) {
        Result *leftRes = gen(start, i - 1);
        Result *rightRes = gen(i + 1, end);
        for (int l = 0; l < leftRes->size; ++l) {
            for (int r = 0; r < rightRes->size; ++r) {
                struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
                root->val = i;
                root->left = leftRes->trees[l];
                root->right = rightRes->trees[r];

                if (cnt >= cap) {
                    cap <<= 1;
                    list = (struct TreeNode **)realloc(list, cap * sizeof(struct TreeNode *));
                }
                list[cnt++] = root;
            }
        }
    }

    Result *res = (Result *)malloc(sizeof(Result));
    res->size = cnt;
    res->trees = list;
    memo[start][end] = res;
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** generateTrees(int n, int* returnSize) {
    // reset memo for safety
    for (int i = 0; i <= 8; ++i)
        for (int j = 0; j <= 8; ++j)
            memo[i][j] = NULL;

    if (n == 0) {
        *returnSize = 0;
        return NULL;
    }

    Result *res = gen(1, n);
    struct TreeNode **ans = (struct TreeNode **)malloc(res->size * sizeof(struct TreeNode *));
    for (int i = 0; i < res->size; ++i)
        ans[i] = res->trees[i];
    *returnSize = res->size;
    return ans;
}
```

## Csharp

```csharp
using System;
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
    private IDictionary<(int, int), IList<TreeNode>> memo = new Dictionary<(int, int), IList<TreeNode>>();

    public IList<TreeNode> GenerateTrees(int n) {
        if (n == 0) return new List<TreeNode>();
        return Build(1, n);
    }

    private IList<TreeNode> Build(int start, int end) {
        var key = (start, end);
        if (memo.ContainsKey(key)) return memo[key];

        var result = new List<TreeNode>();

        if (start > end) {
            result.Add(null);
            memo[key] = result;
            return result;
        }

        for (int i = start; i <= end; i++) {
            var leftTrees = Build(start, i - 1);
            var rightTrees = Build(i + 1, end);

            foreach (var left in leftTrees) {
                foreach (var right in rightTrees) {
                    var root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    result.Add(root);
                }
            }
        }

        memo[key] = result;
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
var generateTrees = function(n) {
    if (n === 0) return [];
    
    const memo = new Map();
    
    const build = (start, end) => {
        const key = `${start},${end}`;
        if (memo.has(key)) return memo.get(key);
        
        const res = [];
        if (start > end) {
            res.push(null);
            memo.set(key, res);
            return res;
        }
        
        for (let rootVal = start; rootVal <= end; ++rootVal) {
            const leftTrees = build(start, rootVal - 1);
            const rightTrees = build(rootVal + 1, end);
            
            for (const left of leftTrees) {
                for (const right of rightTrees) {
                    const node = new TreeNode(rootVal);
                    node.left = left;
                    node.right = right;
                    res.push(node);
                }
            }
        }
        
        memo.set(key, res);
        return res;
    };
    
    return build(1, n);
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

function generateTrees(n: number): Array<TreeNode | null> {
    if (n === 0) return [];

    const memo = new Map<string, Array<TreeNode | null>>();

    function build(start: number, end: number): Array<TreeNode | null> {
        const key = `${start},${end}`;
        if (memo.has(key)) return memo.get(key)!;

        const res: Array<TreeNode | null> = [];

        if (start > end) {
            res.push(null);
            memo.set(key, res);
            return res;
        }

        for (let i = start; i <= end; i++) {
            const leftTrees = build(start, i - 1);
            const rightTrees = build(i + 1, end);

            for (const left of leftTrees) {
                for (const right of rightTrees) {
                    const root = new TreeNode(i, left, right);
                    res.push(root);
                }
            }
        }

        memo.set(key, res);
        return res;
    }

    return build(1, n);
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
     * @param Integer $n
     * @return TreeNode[]
     */
    function generateTrees($n) {
        if ($n == 0) {
            return [];
        }
        $memo = [];
        return $this->build(1, $n, $memo);
    }

    private function build($start, $end, &$memo) {
        $key = $start . ',' . $end;
        if (isset($memo[$key])) {
            return $memo[$key];
        }
        $result = [];

        if ($start > $end) {
            // Empty tree
            $result[] = null;
            $memo[$key] = $result;
            return $result;
        }

        for ($i = $start; $i <= $end; $i++) {
            $leftTrees  = $this->build($start, $i - 1, $memo);
            $rightTrees = $this->build($i + 1, $end, $memo);

            foreach ($leftTrees as $left) {
                foreach ($rightTrees as $right) {
                    $root = new TreeNode($i);
                    $root->left = $left;
                    $root->right = $right;
                    $result[] = $root;
                }
            }
        }

        $memo[$key] = $result;
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
    private var memo = [String:[TreeNode?]]()
    
    func generateTrees(_ n: Int) -> [TreeNode?] {
        if n == 0 { return [] }
        return build(1, n)
    }
    
    private func build(_ start: Int, _ end: Int) -> [TreeNode?] {
        let key = "\(start)-\(end)"
        if let cached = memo[key] {
            return cached
        }
        
        var result = [TreeNode?]()
        if start > end {
            result.append(nil)
            memo[key] = result
            return result
        }
        
        for rootVal in start...end {
            let leftTrees = build(start, rootVal - 1)
            let rightTrees = build(rootVal + 1, end)
            
            for left in leftTrees {
                for right in rightTrees {
                    let node = TreeNode(rootVal)
                    node.left = left
                    node.right = right
                    result.append(node)
                }
            }
        }
        
        memo[key] = result
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
    fun generateTrees(n: Int): List<TreeNode?> {
        if (n == 0) return emptyList()
        val memo = HashMap<Pair<Int, Int>, List<TreeNode?>>()

        fun build(start: Int, end: Int): List<TreeNode?> {
            if (start > end) return listOf(null)
            val key = Pair(start, end)
            memo[key]?.let { return it }

            val res = mutableListOf<TreeNode?>()
            for (rootVal in start..end) {
                val leftTrees = build(start, rootVal - 1)
                val rightTrees = build(rootVal + 1, end)
                for (left in leftTrees) {
                    for (right in rightTrees) {
                        val root = TreeNode(rootVal)
                        root.left = left
                        root.right = right
                        res.add(root)
                    }
                }
            }
            memo[key] = res
            return res
        }

        return build(1, n)
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
  List<TreeNode?> generateTrees(int n) {
    if (n == 0) return [];
    final Map<String, List<TreeNode?>> memo = {};
    return _generate(1, n, memo);
  }

  List<TreeNode?> _generate(int start, int end, Map<String, List<TreeNode?>> memo) {
    final String key = '$start,$end';
    if (memo.containsKey(key)) {
      return memo[key]!;
    }
    final List<TreeNode?> res = [];
    if (start > end) {
      res.add(null);
      memo[key] = res;
      return res;
    }
    for (int i = start; i <= end; i++) {
      final List<TreeNode?> leftTrees = _generate(start, i - 1, memo);
      final List<TreeNode?> rightTrees = _generate(i + 1, end, memo);
      for (final TreeNode? l in leftTrees) {
        for (final TreeNode? r in rightTrees) {
          final TreeNode node = TreeNode(i);
          node.left = l;
          node.right = r;
          res.add(node);
        }
      }
    }
    memo[key] = res;
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
type pair struct{ start, end int }

var memo map[pair][]*TreeNode

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return []*TreeNode{}
	}
	memo = make(map[pair][]*TreeNode)
	return build(1, n)
}

func build(start, end int) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}
	key := pair{start, end}
	if v, ok := memo[key]; ok {
		return v
	}
	var res []*TreeNode
	for i := start; i <= end; i++ {
		leftTrees := build(start, i-1)
		rightTrees := build(i+1, end)
		for _, l := range leftTrees {
			for _, r := range rightTrees {
				node := &TreeNode{Val: i, Left: l, Right: r}
				res = append(res, node)
			}
		}
	}
	memo[key] = res
	return res
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

def generate_trees(n)
  return [] if n == 0
  memo = {}

  build = nil
  build = lambda do |start_idx, end_idx|
    key = [start_idx, end_idx]
    return memo[key] if memo.key?(key)

    trees = []
    if start_idx > end_idx
      trees << nil
    else
      (start_idx..end_idx).each do |root_val|
        left_subtrees  = build.call(start_idx, root_val - 1)
        right_subtrees = build.call(root_val + 1, end_idx)

        left_subtrees.each do |left|
          right_subtrees.each do |right|
            node = TreeNode.new(root_val)
            node.left = left
            node.right = right
            trees << node
          end
        end
      end
    end

    memo[key] = trees
  end

  build.call(1, n)
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
  def generateTrees(n: Int): List[TreeNode] = {
    if (n == 0) return Nil

    val memo = scala.collection.mutable.Map[(Int, Int), List[TreeNode]]()

    def build(start: Int, end: Int): List[TreeNode] = {
      if (start > end) return List(null)

      memo.get((start, end)) match {
        case Some(cached) => cached
        case None =>
          var result = List.empty[TreeNode]
          for (i <- start to end) {
            val leftTrees  = build(start, i - 1)
            val rightTrees = build(i + 1, end)
            for (l <- leftTrees; r <- rightTrees) {
              val root = new TreeNode(i)
              root.left = l
              root.right = r
              result = root :: result
            }
          }
          memo((start, end)) = result
          result
      }
    }

    build(1, n)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

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
    pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if n == 0 {
            return vec![];
        }
        let mut memo: HashMap<(i32, i32), Vec<Option<Rc<RefCell<TreeNode>>>>> = HashMap::new();
        Self::generate(1, n, &mut memo)
    }

    fn generate(
        start: i32,
        end: i32,
        memo: &mut HashMap<(i32, i32), Vec<Option<Rc<RefCell<TreeNode>>>>>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        if start > end {
            return vec![None];
        }
        if let Some(cached) = memo.get(&(start, end)) {
            return cached.clone();
        }

        let mut result: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();

        for root_val in start..=end {
            let left_subtrees = Self::generate(start, root_val - 1, memo);
            let right_subtrees = Self::generate(root_val + 1, end, memo);

            for left in &left_subtrees {
                for right in &right_subtrees {
                    let node = Rc::new(RefCell::new(TreeNode::new(root_val)));
                    if let Some(ref l) = left {
                        node.borrow_mut().left = Some(Rc::clone(l));
                    }
                    if let Some(ref r) = right {
                        node.borrow_mut().right = Some(Rc::clone(r));
                    }
                    result.push(Some(node));
                }
            }
        }

        memo.insert((start, end), result.clone());
        result
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

;; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

(define/contract (generate-trees n)
  (-> exact-integer? (listof (or/c tree-node? #f)))
  (if (= n 0)
      '()
      (let ([memo (make-hash)])
        (define (all start end)
          (cond [(> start end) (list #f)]
                [else
                 (define key (cons start end))
                 (if (hash-has-key? memo key)
                     (hash-ref memo key)
                     (let ([res '()])
                       (for ([root-val (in-range start (+ end 1))])
                         (define left-list (all start (- root-val 1)))
                         (define right-list (all (+ root-val 1) end))
                         (for ([l left-list])
                           (for ([r right-list])
                             (define node (make-tree-node root-val))
                             (set-tree-node-left! node l)
                             (set-tree-node-right! node r)
                             (set! res (cons node res)))))
                       (define result (reverse res))
                       (hash-set! memo key result)
                       result)))])
        (all 1 n))))
```

## Erlang

```erlang
-module(solution).
-export([generate_trees/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec generate_trees(N :: integer()) -> [#tree_node{} | null].
generate_trees(0) ->
    [];
generate_trees(N) when N > 0 ->
    all_possible(1, N).

all_possible(Start, End) when Start > End ->
    [null];
all_possible(Start, End) ->
    lists:foldl(fun(I, Acc) ->
        Lefts = all_possible(Start, I - 1),
        Rights = all_possible(I + 1, End),
        Trees = [#tree_node{val = I, left = L, right = R} || L <- Lefts, R <- Rights],
        Trees ++ Acc
    end, [], lists:seq(Start, End)).
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_trees(n :: integer) :: [TreeNode.t() | nil]
  def generate_trees(0), do: []
  def generate_trees(n) when n > 0 do
    build(1, n)
  end

  defp build(start, finish) when start > finish, do: [nil]

  defp build(start, finish) do
    Enum.flat_map(start..finish, fn i ->
      left = build(start, i - 1)
      right = build(i + 1, finish)

      for l <- left, r <- right do
        %TreeNode{val: i, left: l, right: r}
      end
    end)
  end
end
```
