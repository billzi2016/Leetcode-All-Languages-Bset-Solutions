# 1028. Recover a Tree From Preorder Traversal

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
    TreeNode* recoverFromPreorder(string traversal) {
        vector<TreeNode*> levelNodes;
        TreeNode* root = nullptr;
        int i = 0, n = traversal.size();
        while (i < n) {
            int depth = 0;
            while (i < n && traversal[i] == '-') {
                ++depth;
                ++i;
            }
            int val = 0;
            while (i < n && isdigit(traversal[i])) {
                val = val * 10 + (traversal[i] - '0');
                ++i;
            }
            TreeNode* node = new TreeNode(val);
            if (depth == 0) {
                root = node;
            } else {
                TreeNode* parent = levelNodes[depth - 1];
                if (!parent->left)
                    parent->left = node;
                else
                    parent->right = node;
            }
            if ((int)levelNodes.size() <= depth)
                levelNodes.push_back(node);
            else
                levelNodes[depth] = node;
        }
        return root;
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
    public TreeNode recoverFromPreorder(String traversal) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        int i = 0, n = traversal.length();
        while (i < n) {
            int depth = 0;
            while (i < n && traversal.charAt(i) == '-') {
                depth++;
                i++;
            }
            int val = 0;
            while (i < n && Character.isDigit(traversal.charAt(i))) {
                val = val * 10 + (traversal.charAt(i) - '0');
                i++;
            }
            TreeNode node = new TreeNode(val);
            // Ensure stack size matches the current depth
            while (stack.size() > depth) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                TreeNode parent = stack.peek();
                if (parent.left == null) {
                    parent.left = node;
                } else {
                    parent.right = node;
                }
            }
            stack.push(node);
        }
        // The bottom of the stack is the root
        while (stack.size() > 1) {
            stack.pop();
        }
        return stack.peek();
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
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        i, n = 0, len(traversal)
        stack = []
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + ord(traversal[i]) - 48
                i += 1
            node = TreeNode(val)
            # Adjust stack to current depth
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0] if stack else None
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
    def recoverFromPreorder(self, traversal: str) -> Optional['TreeNode']:
        stack = []
        i = 0
        n = len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            node = TreeNode(val)
            # Adjust stack to current depth
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0] if stack else None
```

## C

```c
#include <stdlib.h>
#include <ctype.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* recoverFromPreorder(char* traversal) {
    struct TreeNode* stack[1005];
    int sz = 0;
    char *s = traversal;
    
    while (*s) {
        int depth = 0;
        while (*s == '-') {
            depth++;
            s++;
        }
        int val = 0;
        while (*s && isdigit(*s)) {
            val = val * 10 + (*s - '0');
            s++;
        }
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = val;
        node->left = node->right = NULL;
        
        while (sz > depth) {
            sz--; // pop
        }
        if (sz > 0) {
            struct TreeNode* parent = stack[sz - 1];
            if (!parent->left)
                parent->left = node;
            else
                parent->right = node;
        }
        stack[sz++] = node;
    }
    
    return stack[0];
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
    public TreeNode RecoverFromPreorder(string traversal) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        int i = 0;
        TreeNode root = null;

        while (i < traversal.Length) {
            int depth = 0;
            while (i < traversal.Length && traversal[i] == '-') {
                depth++;
                i++;
            }

            int val = 0;
            while (i < traversal.Length && char.IsDigit(traversal[i])) {
                val = val * 10 + (traversal[i] - '0');
                i++;
            }

            TreeNode node = new TreeNode(val);

            if (depth == 0) {
                root = node;
            } else {
                while (stack.Count > depth) {
                    stack.Pop();
                }
                TreeNode parent = stack.Peek();
                if (parent.left == null) {
                    parent.left = node;
                } else {
                    parent.right = node;
                }
            }

            stack.Push(node);
        }

        return root;
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
 * @param {string} traversal
 * @return {TreeNode}
 */
var recoverFromPreorder = function(traversal) {
    const stack = [];
    let i = 0;
    const n = traversal.length;
    while (i < n) {
        // count dashes to get depth
        let depth = 0;
        while (i < n && traversal[i] === '-') {
            depth++;
            i++;
        }
        // parse number value
        let val = 0;
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9') {
            val = val * 10 + (traversal.charCodeAt(i) - 48);
            i++;
        }
        const node = new TreeNode(val);
        // adjust stack to current depth
        while (stack.length > depth) {
            stack.pop();
        }
        if (stack.length > 0) {
            const parent = stack[stack.length - 1];
            if (!parent.left) {
                parent.left = node;
            } else {
                parent.right = node;
            }
        }
        stack.push(node);
    }
    return stack[0] || null;
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

function recoverFromPreorder(traversal: string): TreeNode | null {
    const n = traversal.length;
    let i = 0;
    const stack: TreeNode[] = [];

    while (i < n) {
        // count dashes to determine depth
        let depth = 0;
        while (i < n && traversal[i] === '-') {
            depth++;
            i++;
        }

        // parse node value
        let val = 0;
        while (i < n && traversal[i] >= '0' && traversal[i] <= '9') {
            val = val * 10 + (traversal.charCodeAt(i) - 48);
            i++;
        }

        const node = new TreeNode(val);

        // adjust stack to current depth
        while (stack.length > depth) {
            stack.pop();
        }

        if (stack.length > 0) {
            const parent = stack[stack.length - 1];
            if (!parent.left) {
                parent.left = node;
            } else {
                parent.right = node;
            }
        }

        stack.push(node);
    }

    return stack.length ? stack[0] : null;
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
     * @param String $traversal
     * @return TreeNode
     */
    function recoverFromPreorder($traversal) {
        $n = strlen($traversal);
        $i = 0;
        $stack = [];

        while ($i < $n) {
            // count dashes to determine depth
            $depth = 0;
            while ($i < $n && $traversal[$i] === '-') {
                $depth++;
                $i++;
            }

            // parse node value
            $value = 0;
            while ($i < $n && ctype_digit($traversal[$i])) {
                $value = $value * 10 + intval($traversal[$i]);
                $i++;
            }

            $node = new TreeNode($value);

            // adjust stack to current depth
            while (count($stack) > $depth) {
                array_pop($stack);
            }

            // attach node to its parent if exists
            if (!empty($stack)) {
                $parent = $stack[count($stack) - 1];
                if ($parent->left === null) {
                    $parent->left = $node;
                } else {
                    $parent->right = $node;
                }
            }

            // push current node onto stack
            $stack[] = $node;
        }

        // root is the first element in the stack
        return $stack[0];
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
    func recoverFromPreorder(_ traversal: String) -> TreeNode? {
        let chars = Array(traversal)
        var index = 0
        var stack = [TreeNode]()
        
        while index < chars.count {
            // count dashes to determine depth
            var depth = 0
            while index < chars.count && chars[index] == "-" {
                depth += 1
                index += 1
            }
            
            // parse node value
            var value = 0
            while index < chars.count && chars[index].isNumber {
                if let digit = Int(String(chars[index])) {
                    value = value * 10 + digit
                }
                index += 1
            }
            
            let node = TreeNode(value)
            
            // ensure stack size matches depth (parent is at depth-1)
            while stack.count > depth {
                stack.removeLast()
            }
            
            if let parent = stack.last {
                if parent.left == nil {
                    parent.left = node
                } else {
                    parent.right = node
                }
            }
            
            stack.append(node)
        }
        
        return stack.first
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
    fun recoverFromPreorder(traversal: String): TreeNode? {
        val stack = mutableListOf<TreeNode>()
        var i = 0
        val n = traversal.length
        while (i < n) {
            var depth = 0
            while (i < n && traversal[i] == '-') {
                depth++
                i++
            }
            var value = 0
            while (i < n && traversal[i].isDigit()) {
                value = value * 10 + (traversal[i] - '0')
                i++
            }
            val node = TreeNode(value)
            while (stack.size > depth) {
                stack.removeAt(stack.lastIndex)
            }
            if (stack.isNotEmpty()) {
                val parent = stack[stack.lastIndex]
                if (parent.left == null) {
                    parent.left = node
                } else {
                    parent.right = node
                }
            }
            stack.add(node)
        }
        return if (stack.isNotEmpty()) stack[0] else null
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
  TreeNode? recoverFromPreorder(String traversal) {
    List<TreeNode> stack = [];
    int i = 0;
    while (i < traversal.length) {
      // Count depth indicated by dashes
      int depth = 0;
      while (i < traversal.length && traversal[i] == '-') {
        depth++;
        i++;
      }
      // Parse node value
      int val = 0;
      while (i < traversal.length &&
          traversal.codeUnitAt(i) >= 48 &&
          traversal.codeUnitAt(i) <= 57) {
        val = val * 10 + (traversal.codeUnitAt(i) - 48);
        i++;
      }
      TreeNode node = TreeNode(val);
      // Adjust stack to current depth
      while (stack.length > depth) {
        stack.removeLast();
      }
      // Attach to parent if exists
      if (stack.isNotEmpty) {
        TreeNode parent = stack.last;
        if (parent.left == null) {
          parent.left = node;
        } else {
          parent.right = node;
        }
      }
      stack.add(node);
    }
    return stack.isNotEmpty ? stack[0] : null;
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
func recoverFromPreorder(traversal string) *TreeNode {
    n := len(traversal)
    stack := []*TreeNode{}
    i := 0
    for i < n {
        depth := 0
        for i < n && traversal[i] == '-' {
            depth++
            i++
        }
        val := 0
        for i < n && traversal[i] >= '0' && traversal[i] <= '9' {
            val = val*10 + int(traversal[i]-'0')
            i++
        }
        node := &TreeNode{Val: val}
        // Ensure stack size matches current depth
        for len(stack) > depth {
            stack = stack[:len(stack)-1]
        }
        if len(stack) > 0 {
            parent := stack[len(stack)-1]
            if parent.Left == nil {
                parent.Left = node
            } else {
                parent.Right = node
            }
        }
        stack = append(stack, node)
    }
    return stack[0]
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

def recover_from_preorder(traversal)
  i = 0
  n = traversal.length
  stack = []

  while i < n
    depth = 0
    while i < n && traversal[i] == '-'
      depth += 1
      i += 1
    end

    val = 0
    while i < n && traversal[i] >= '0' && traversal[i] <= '9'
      val = val * 10 + (traversal[i].ord - 48)
      i += 1
    end

    node = TreeNode.new(val)

    while stack.length > depth
      stack.pop
    end

    unless stack.empty?
      parent = stack[-1]
      if parent.left.nil?
        parent.left = node
      else
        parent.right = node
      end
    end

    stack << node
  end

  stack[0]
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
    def recoverFromPreorder(traversal: String): TreeNode = {
        import scala.collection.mutable.Stack

        val n = traversal.length
        var i = 0
        val stack = Stack[TreeNode]()

        while (i < n) {
            // count dashes to determine depth
            var depth = 0
            while (i < n && traversal.charAt(i) == '-') {
                depth += 1
                i += 1
            }
            // parse node value
            var num = 0
            while (i < n && traversal.charAt(i).isDigit) {
                num = num * 10 + (traversal.charAt(i) - '0')
                i += 1
            }

            val node = new TreeNode(num)

            // ensure stack size matches current depth
            while (stack.size > depth) {
                stack.pop()
            }

            if (stack.nonEmpty) {
                val parent = stack.top
                if (parent.left == null) parent.left = node else parent.right = node
            }

            stack.push(node)
        }

        // root is the bottom-most element in the stack
        while (stack.size > 1) stack.pop()
        stack.top
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

impl Solution {
    pub fn recover_from_preorder(traversal: String) -> Option<Rc<RefCell<TreeNode>>> {
        let bytes = traversal.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;
        let mut levels: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();
        let mut root: Option<Rc<RefCell<TreeNode>>> = None;

        while i < n {
            // count dashes to determine depth
            let mut depth = 0usize;
            while i < n && bytes[i] == b'-' {
                depth += 1;
                i += 1;
            }
            // parse node value
            let mut val: i32 = 0;
            while i < n && bytes[i].is_ascii_digit() {
                val = val * 10 + (bytes[i] - b'0') as i32;
                i += 1;
            }

            let node = Rc::new(RefCell::new(TreeNode::new(val)));

            if depth == 0 {
                root = Some(node.clone());
            } else {
                // parent is the last node at depth-1
                let parent_rc = levels[depth - 1].as_ref().unwrap().clone();
                let mut parent = parent_rc.borrow_mut();
                if parent.left.is_none() {
                    parent.left = Some(node.clone());
                } else {
                    parent.right = Some(node.clone());
                }
            }

            // ensure the levels vector can hold current depth
            while levels.len() <= depth {
                levels.push(None);
            }
            levels[depth] = Some(node);
        }

        root
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

(define/contract (recover-from-preorder traversal)
  (-> string? (or/c tree-node? #f))
  (let* ((len (string-length traversal))
         ;; maximum possible depth is number of nodes, which ≤1000 per constraints
         (levels (make-vector 1000 #f)))
    (let loop ((i 0))
      (when (< i len)
        ;; count dashes to get depth
        (define depth
          (let count-dash ((j i) (cnt 0))
            (if (and (< j len) (char=? (string-ref traversal j) #\-))
                (count-dash (+ j 1) (+ cnt 1))
                cnt)))
        (set! i (+ i depth))
        ;; parse number
        (define-values (num next-i)
          (let parse-num ((j i) (val 0))
            (if (and (< j len) (char-numeric? (string-ref traversal j)))
                (parse-num (+ j 1)
                           (+ (* val 10)
                              (- (char->integer (string-ref traversal j))
                                 (char->integer #\0))))
                (values val j))))
        (set! i next-i)
        ;; create node
        (define node (make-tree-node num))
        (vector-set! levels depth node)
        (when (> depth 0)
          (let ((parent (vector-ref levels (- depth 1))))
            (if (not (tree-node-left parent))
                (set-tree-node-left! parent node)
                (set-tree-node-right! parent node))))
        (loop i)))
    (vector-ref levels 0)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec recover_from_preorder(Traversal :: unicode:unicode_binary()) -> #tree_node{} | null.
recover_from_preorder(Traversal) ->
    Bin = unicode:characters_to_binary(Traversal),
    Levels = parse(Bin, []),
    case Levels of
        [] -> null;
        [Root|_] -> Root
    end.

%% Parse the binary string, building a list where index = depth and value = node.
parse(<<>>, Levels) ->
    Levels;
parse(Bin, Levels) ->
    {Depth, Rest1} = count_dashes(Bin),
    {Value, Rest2} = read_number(Rest1),
    Node0 = #tree_node{val = Value},
    UpdatedLevels =
        case Depth of
            0 ->
                add_or_replace(Levels, 0, Node0);
            _ ->
                Parent = get_at(Depth - 1, Levels),
                UpdatedParent =
                    case Parent#tree_node.left of
                        null -> Parent#tree_node{left = Node0};
                        _    -> Parent#tree_node{right = Node0}
                    end,
                TempLevels = set_at(Depth - 1, UpdatedParent, Levels),
                add_or_replace(TempLevels, Depth, Node0)
        end,
    parse(Rest2, UpdatedLevels).

%% Count leading dashes to determine depth.
count_dashes(Bin) -> count_dashes(Bin, 0).
count_dashes(<<$-, Rest/binary>>, Acc) ->
    count_dashes(Rest, Acc + 1);
count_dashes(Rest, Acc) ->
    {Acc, Rest}.

%% Read consecutive digits to obtain node value.
read_number(Bin) -> read_number(Bin, 0).
read_number(<<Digit, Rest/binary>>, Acc) when Digit >= $0, Digit =< $9 ->
    NewAcc = Acc * 10 + (Digit - $0),
    read_number(Rest, NewAcc);
read_number(Rest, Acc) ->
    {Acc, Rest}.

%% Retrieve element at zero‑based Index from list.
get_at(Index, List) ->
    lists:nth(Index + 1, List).

%% Replace element at Index with Elem; assumes Index < length(List).
set_at(0, Elem, [_|Tail]) ->
    [Elem | Tail];
set_at(N, Elem, [H|Tail]) when N > 0 ->
    [H | set_at(N - 1, Elem, Tail)];
set_at(_, Elem, []) -> % should not happen for valid input
    [Elem].

%% Add Elem at Index if list is shorter; otherwise replace.
add_or_replace(Levels, Index, Elem) ->
    Len = length(Levels),
    case Index < Len of
        true  -> set_at(Index, Elem, Levels);
        false -> Levels ++ [Elem]
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
  @spec recover_from_preorder(traversal :: String.t()) :: TreeNode.t() | nil
  def recover_from_preorder(traversal) do
    chars = String.to_charlist(traversal)
    n = length(chars)

    {root, _} = build(chars, 0, 0, n)
    root
  end

  # Recursive builder: returns {node_or_nil, next_index}
  defp build(_chars, i, _depth, n) when i >= n, do: {nil, i}

  defp build(chars, i, depth, n) do
    {dash_cnt, j} = count_dashes(chars, i, 0, n)

    if dash_cnt != depth do
      # No node at this depth; backtrack without consuming characters
      {nil, i}
    else
      {val, k} = parse_number(chars, j, 0, n)
      node = %TreeNode{val: val}

      {left_child, l} = build(chars, k, depth + 1, n)
      node = %{node | left: left_child}

      {right_child, m} = build(chars, l, depth + 1, n)
      node = %{node | right: right_child}

      {node, m}
    end
  end

  defp count_dashes(_chars, i, acc, n) when i >= n, do: {acc, i}

  defp count_dashes(chars, i, acc, n) do
    case Enum.at(chars, i) do
      ?- -> count_dashes(chars, i + 1, acc + 1, n)
      _ -> {acc, i}
    end
  end

  defp parse_number(_chars, i, acc, n) when i >= n, do: {acc, i}

  defp parse_number(chars, i, acc, n) do
    case Enum.at(chars, i) do
      c when c >= ?0 and c <= ?9 ->
        parse_number(chars, i + 1, acc * 10 + (c - ?0), n)

      _ ->
        {acc, i}
    end
  end
end
```
