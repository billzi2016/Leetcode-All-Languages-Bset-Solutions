# 1261. Find Elements in a Contaminated Binary Tree

## Cpp

```cpp
#include <unordered_set>
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
class FindElements {
    unordered_set<int> seen;
    
    void dfs(TreeNode* node, long long val) {
        if (!node) return;
        node->val = (int)val;          // optional restoration
        seen.insert((int)val);
        if (node->left)  dfs(node->left,  val * 2 + 1);
        if (node->right) dfs(node->right, val * 2 + 2);
    }
public:
    FindElements(TreeNode* root) {
        if (root) dfs(root, 0);
    }
    
    bool find(int target) {
        return seen.find(target) != seen.end();
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */
```

## Java

```java
import java.util.HashSet;
import java.util.Set;

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
class FindElements {
    private final Set<Integer> values = new HashSet<>();

    public FindElements(TreeNode root) {
        if (root != null) {
            recover(root, 0);
        }
    }

    private void recover(TreeNode node, int val) {
        if (node == null) return;
        node.val = val;
        values.add(val);
        recover(node.left, val * 2 + 1);
        recover(node.right, val * 2 + 2);
    }

    public boolean find(int target) {
        return values.contains(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.seen = set()
        if root:
            self._dfs(root, 0)

    def _dfs(self, node, val):
        if not node:
            return
        node.val = val
        self.seen.add(val)
        if node.left:
            self._dfs(node.left, val * 2 + 1)
        if node.right:
            self._dfs(node.right, val * 2 + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen
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

class FindElements:
    def __init__(self, root: Optional['TreeNode']):
        self.seen = set()
        if root is not None:
            self._dfs(root, 0)

    def _dfs(self, node: 'TreeNode', val: int):
        self.seen.add(val)
        if node.left:
            self._dfs(node.left, val * 2 + 1)
        if node.right:
            self._dfs(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.seen
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

#define MAX_VAL (1 << 21)  // 2,097,152

typedef struct {
    char *present;  // bitmap of recovered values
} FindElements;

static void dfs(struct TreeNode* node, int val, char *present) {
    if (!node) return;
    present[val] = 1;
    if (node->left)
        dfs(node->left, val * 2 + 1, present);
    if (node->right)
        dfs(node->right, val * 2 + 2, present);
}

FindElements* findElementsCreate(struct TreeNode* root) {
    FindElements *obj = (FindElements *)malloc(sizeof(FindElements));
    obj->present = (char *)calloc(MAX_VAL, sizeof(char));
    if (root)
        dfs(root, 0, obj->present);
    return obj;
}

bool findElementsFind(FindElements* obj, int target) {
    if (!obj || target < 0 || target >= MAX_VAL) return false;
    return obj->present[target] != 0;
}

void findElementsFree(FindElements* obj) {
    if (obj) {
        free(obj->present);
        free(obj);
    }
}

/**
 * Your FindElements struct will be instantiated and called as such:
 * FindElements* obj = findElementsCreate(root);
 * bool param_1 = findElementsFind(obj, target);
 * 
 * findElementsFree(obj);
 */
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
public class FindElements {
    private HashSet<int> _values = new HashSet<int>();

    public FindElements(TreeNode root) {
        if (root != null) {
            Recover(root, 0);
        }
    }

    private void Recover(TreeNode node, int val) {
        _values.Add(val);
        if (node.left != null) {
            Recover(node.left, val * 2 + 1);
        }
        if (node.right != null) {
            Recover(node.right, val * 2 + 2);
        }
    }

    public bool Find(int target) {
        return _values.Contains(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * bool param_1 = obj.Find(target);
 */
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
 */
var FindElements = function(root) {
    this.values = new Set();
    
    const dfs = (node, val) => {
        if (!node) return;
        node.val = val;
        this.values.add(val);
        if (node.left) dfs(node.left, 2 * val + 1);
        if (node.right) dfs(node.right, 2 * val + 2);
    };
    
    if (root) dfs(root, 0);
};

/** 
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function(target) {
    return this.values.has(target);
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

class FindElements {
    private seen: Set<number>;

    constructor(root: TreeNode | null) {
        this.seen = new Set();
        if (root !== null) {
            const dfs = (node: TreeNode, val: number): void => {
                node.val = val;
                this.seen.add(val);
                if (node.left) dfs(node.left, 2 * val + 1);
                if (node.right) dfs(node.right, 2 * val + 2);
            };
            dfs(root, 0);
        }
    }

    find(target: number): boolean {
        return this.seen.has(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */
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
class FindElements {
    /**
     * @var array<int,bool>
     */
    private $values = [];

    /**
     * @param TreeNode $root
     */
    public function __construct($root) {
        if ($root === null) {
            return;
        }
        $this->dfs($root, 0);
    }

    /**
     * Depth‑first traversal to recover node values.
     *
     * @param TreeNode $node
     * @param int $val
     */
    private function dfs($node, $val) {
        if ($node === null) {
            return;
        }
        $node->val = $val;
        $this->values[$val] = true;

        if ($node->left !== null) {
            $this->dfs($node->left, $val * 2 + 1);
        }
        if ($node->right !== null) {
            $this->dfs($node->right, $val * 2 + 2);
        }
    }

    /**
     * @param int $target
     * @return bool
     */
    public function find($target) {
        return isset($this->values[$target]);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * $obj = new FindElements($root);
 * $ret_1 = $obj->find($target);
 */
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

class FindElements {
    private var seen = Set<Int>()
    
    init(_ root: TreeNode?) {
        if let node = root {
            dfs(node, 0)
        }
    }
    
    private func dfs(_ node: TreeNode?, _ value: Int) {
        guard let n = node else { return }
        seen.insert(value)
        if let left = n.left {
            dfs(left, value * 2 + 1)
        }
        if let right = n.right {
            dfs(right, value * 2 + 2)
        }
    }
    
    func find(_ target: Int) -> Bool {
        return seen.contains(target)
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * let obj = FindElements(root)
 * let ret_1: Bool = obj.find(target)
 */
```

## Kotlin

```kotlin
class FindElements(root: TreeNode?) {
    private val values = HashSet<Int>()

    init {
        if (root != null) {
            dfs(root, 0)
        }
    }

    private fun dfs(node: TreeNode?, value: Int) {
        if (node == null) return
        node.`val` = value
        values.add(value)
        dfs(node.left, value * 2 + 1)
        dfs(node.right, value * 2 + 2)
    }

    fun find(target: Int): Boolean {
        return values.contains(target)
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
class FindElements {
  final Set<int> _values = {};

  FindElements(TreeNode? root) {
    if (root != null) {
      _dfs(root, 0);
    }
  }

  void _dfs(TreeNode node, int val) {
    _values.add(val);
    if (node.left != null) {
      _dfs(node.left!, val * 2 + 1);
    }
    if (node.right != null) {
      _dfs(node.right!, val * 2 + 2);
    }
  }

  bool find(int target) => _values.contains(target);
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = FindElements(root);
 * bool param1 = obj.find(target);
 */
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
type FindElements struct {
    seen map[int]struct{}
}

func Constructor(root *TreeNode) FindElements {
    fe := FindElements{seen: make(map[int]struct{})}
    var dfs func(node *TreeNode, val int)
    dfs = func(node *TreeNode, val int) {
        if node == nil {
            return
        }
        fe.seen[val] = struct{}{}
        if node.Left != nil {
            dfs(node.Left, 2*val+1)
        }
        if node.Right != nil {
            dfs(node.Right, 2*val+2)
        }
    }
    if root != nil {
        dfs(root, 0)
    }
    return fe
}

func (this *FindElements) Find(target int) bool {
    _, ok := this.seen[target]
    return ok
}

/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */
```

## Ruby

```ruby
require 'set'

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

class FindElements
  def initialize(root)
    @values = Set.new
    recover(root, 0) if root
  end

  def find(target)
    @values.include?(target)
  end

  private

  def recover(node, val)
    return unless node
    node.val = val
    @values.add(val)
    recover(node.left, val * 2 + 1) if node.left
    recover(node.right, val * 2 + 2) if node.right
  end
end
```

## Scala

```scala
import scala.collection.mutable

/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
class FindElements(_root: TreeNode) {

  private val seen: mutable.HashSet[Int] = mutable.HashSet.empty

  if (_root != null) {
    def dfs(node: TreeNode, v: Int): Unit = {
      node.value = v
      seen += v
      if (node.left != null) dfs(node.left, v * 2 + 1)
      if (node.right != null) dfs(node.right, v * 2 + 2)
    }
    dfs(_root, 0)
  }

  def find(target: Int): Boolean = seen.contains(target)
}

/**
 * Your FindElements object will be instantiated and called as such:
 * val obj = new FindElements(root)
 * val param_1 = obj.find(target)
 */
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashSet;

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

struct FindElements {
    set: HashSet<i32>,
}

impl FindElements {
    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut set = HashSet::new();
        Self::dfs(root, 0, &mut set);
        FindElements { set }
    }

    fn dfs(node_opt: Option<Rc<RefCell<TreeNode>>>, val: i32, set: &mut HashSet<i32>) {
        if let Some(rc_node) = node_opt {
            set.insert(val);
            let left = rc_node.borrow().left.clone();
            let right = rc_node.borrow().right.clone();
            Self::dfs(left, 2 * val + 1, set);
            Self::dfs(right, 2 * val + 2, set);
        }
    }

    fn find(&self, target: i32) -> bool {
        self.set.contains(&target)
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * let obj = FindElements::new(root);
 * let ret_1: bool = obj.find(target);
 */
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

(define find-elements%
  (class object%
    (super-new)
    
    ;; root : (or/c tree-node? #f)
    (init-field root)
    
    ;; vals : hash table used as a set of recovered values
    (field [vals (make-hash)])
    
    ;; Recover the original values using DFS and store them in `vals`
    (let dfs ((node root) (val 0))
      (when node
        (set-tree-node-val! node val)
        (hash-set! vals val #t)
        (dfs (tree-node-left node) (+ (* 2 val) 1))
        (dfs (tree-node-right node) (+ (* 2 val) 2))))
    
    ;; find : exact-integer? -> boolean?
    (define/public (find target)
      (hash-has-key? vals target))))
```

## Erlang

```erlang
-module(solution).
-export([find_elements_init_/1, find_elements_find/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec find_elements_init_(Root :: #tree_node{} | null) -> any().
find_elements_init_(Root) ->
    Seen = recover(Root),
    put(seen, Seen),
    ok.

-spec find_elements_find(Target :: integer()) -> boolean().
find_elements_find(Target) ->
    case get(seen) of
        undefined -> false;
        Seen -> maps:is_key(Target, Seen)
    end.

recover(null) -> #{};
recover(Node) when is_record(Node, tree_node) ->
    dfs(Node, 0, #{}).

dfs(null, _Val, Map) -> Map;
dfs(#tree_node{left=Left,right=Right}=Node, Val, Map) ->
    Map1 = maps:put(Val, true, Map),
    Map2 = dfs(Left, Val*2 + 1, Map1),
    dfs(Right, Val*2 + 2, Map2).
```

## Elixir

```elixir
defmodule FindElements do
  @spec init_(root :: TreeNode.t() | nil) :: :ok
  def init_(root) do
    set =
      case root do
        nil -> MapSet.new()
        _ -> dfs(root, 0, MapSet.new())
      end

    Process.put(:find_elements_set, set)
    :ok
  end

  @spec find(target :: integer) :: boolean
  def find(target) do
    set = Process.get(:find_elements_set, MapSet.new())
    MapSet.member?(set, target)
  end

  defp dfs(nil, _val, set), do: set

  defp dfs(node, val, set) do
    set = MapSet.put(set, val)

    set =
      case node.left do
        nil -> set
        left -> dfs(left, val * 2 + 1, set)
      end

    case node.right do
      nil -> set
      right -> dfs(right, val * 2 + 2, set)
    end
  end
end
```
