# 0988. Smallest String Starting From Leaf

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
    string smallestFromLeaf(TreeNode* root) {
        if (!root) return "";
        string best = "~"; // larger than any possible answer
        string path;
        dfs(root, path, best);
        return best;
    }
private:
    void dfs(TreeNode* node, string& path, string& best) {
        if (!node) return;
        path.push_back(char('a' + node->val));
        if (!node->left && !node->right) {
            string cand = path;
            reverse(cand.begin(), cand.end());
            if (cand < best) best = cand;
        }
        dfs(node->left, path, best);
        dfs(node->right, path, best);
        path.pop_back();
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
    public String smallestFromLeaf(TreeNode root) {
        return dfs(root);
    }

    private String dfs(TreeNode node) {
        if (node == null) {
            return null;
        }
        String left = dfs(node.left);
        String right = dfs(node.right);

        char curChar = (char) ('a' + node.val);

        // Leaf node
        if (left == null && right == null) {
            return String.valueOf(curChar);
        }

        String bestChild;
        if (left == null) {
            bestChild = right;
        } else if (right == null) {
            bestChild = left;
        } else {
            bestChild = left.compareTo(right) <= 0 ? left : right;
        }

        // Append current character at the end to build leaf-to-root string
        return bestChild + curChar;
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
    def smallestFromLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if not root:
            return ""
        import sys
        sys.setrecursionlimit(10000)
        best = [None]  # use list to allow modification in nested scope
        path = []

        def dfs(node):
            if not node:
                return
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:  # leaf
                cand = ''.join(reversed(path))
                if best[0] is None or cand < best[0]:
                    best[0] = cand
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return best[0]
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root):
        self.best = None

        def dfs(node, path):
            if not node:
                return
            # add current character (from root towards leaf)
            path.append(chr(ord('a') + node.val))
            # if leaf, evaluate string from leaf to root
            if not node.left and not node.right:
                s = ''.join(reversed(path))
                if self.best is None or s < self.best:
                    self.best = s
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            # backtrack
            path.pop()

        dfs(root, [])
        return self.best
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char *best = NULL;

static void dfs(struct TreeNode* node, char *buf, int depth) {
    if (!node) return;
    buf[depth] = (char)('a' + node->val);
    if (!node->left && !node->right) {
        int len = depth + 1;
        char *cand = (char*)malloc(len + 1);
        for (int i = 0; i < len; ++i)
            cand[i] = buf[len - 1 - i];
        cand[len] = '\0';
        if (!best || strcmp(cand, best) < 0) {
            free(best);
            best = cand;
        } else {
            free(cand);
        }
    } else {
        dfs(node->left, buf, depth + 1);
        dfs(node->right, buf, depth + 1);
    }
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
char* smallestFromLeaf(struct TreeNode* root) {
    if (best) { free(best); best = NULL; }
    char path[8505];
    dfs(root, path, 0);
    return best ? best : "";
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
    private string best;

    public string SmallestFromLeaf(TreeNode root) {
        if (root == null) return "";
        var path = new System.Text.StringBuilder();
        Dfs(root, path);
        return best ?? "";
    }

    private void Dfs(TreeNode node, System.Text.StringBuilder path) {
        if (node == null) return;

        // Append current character (from root towards leaf)
        path.Append((char)('a' + node.val));

        // If leaf, evaluate the string formed from leaf to root
        if (node.left == null && node.right == null) {
            // Build reversed string
            int len = path.Length;
            char[] rev = new char[len];
            for (int i = 0; i < len; i++) {
                rev[i] = path[len - 1 - i];
            }
            string candidate = new string(rev);
            if (best == null || string.Compare(candidate, best) < 0) {
                best = candidate;
            }
        } else {
            Dfs(node.left, path);
            Dfs(node.right, path);
        }

        // Backtrack
        path.Length--;
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
 * @return {string}
 */
var smallestFromLeaf = function(root) {
    let best = null;
    const dfs = (node, path) => {
        if (!node) return;
        // add current character
        path.push(String.fromCharCode(97 + node.val));
        if (!node.left && !node.right) {
            // leaf: construct string from leaf to root
            const candidate = path.slice().reverse().join('');
            if (best === null || candidate < best) {
                best = candidate;
            }
        } else {
            dfs(node.left, path);
            dfs(node.right, path);
        }
        // backtrack
        path.pop();
    };
    dfs(root, []);
    return best;
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

function smallestFromLeaf(root: TreeNode | null): string {
    if (!root) return "";
    let best = "~"; // character after 'z' in ASCII, ensures any valid string is smaller

    const dfs = (node: TreeNode | null, cur: string): void => {
        if (!node) return;
        const next = String.fromCharCode(97 + node.val) + cur; // prepend current char
        if (!node.left && !node.right) { // leaf
            if (next < best) best = next;
        }
        dfs(node.left, next);
        dfs(node.right, next);
    };

    dfs(root, "");
    return best === "~" ? "" : best;
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
     * @return string
     */
    function smallestFromLeaf($root) {
        $best = null;
        $dfs = function($node, $path) use (&$best, &$dfs) {
            if ($node === null) {
                return;
            }
            $char = chr(ord('a') + $node->val);
            $newPath = $char . $path;
            if ($node->left === null && $node->right === null) {
                if ($best === null || strcmp($newPath, $best) < 0) {
                    $best = $newPath;
                }
            } else {
                if ($node->left !== null) {
                    $dfs($node->left, $newPath);
                }
                if ($node->right !== null) {
                    $dfs($node->right, $newPath);
                }
            }
        };
        $dfs($root, "");
        return $best;
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
    func smallestFromLeaf(_ root: TreeNode?) -> String {
        var best: String? = nil
        var path = [Character]()
        
        func dfs(_ node: TreeNode?) {
            guard let node = node else { return }
            let ch = Character(UnicodeScalar(node.val + 97)!)
            path.append(ch)
            
            if node.left == nil && node.right == nil {
                let candidate = String(path.reversed())
                if best == nil || candidate < best! {
                    best = candidate
                }
            } else {
                dfs(node.left)
                dfs(node.right)
            }
            path.removeLast()
        }
        
        dfs(root)
        return best ?? ""
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
    fun smallestFromLeaf(root: TreeNode?): String {
        return dfs(root) ?: ""
    }

    private fun dfs(node: TreeNode?): String? {
        if (node == null) return null

        val left = dfs(node.left)
        val right = dfs(node.right)

        // Leaf node
        if (left == null && right == null) {
            return ('a'.code + node.`val`).toChar().toString()
        }

        var best: String? = null
        if (left != null) best = left
        if (right != null) {
            if (best == null || right < best) best = right
        }

        // Append current character at the end to build leaf->root string
        return best!! + ('a'.code + node.`val`).toChar()
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
  String smallestFromLeaf(TreeNode? root) {
    if (root == null) return '';
    String? best;
    final List<int> path = [];

    void dfs(TreeNode? node) {
      if (node == null) return;
      path.add(node.val);
      if (node.left == null && node.right == null) {
        final sb = StringBuffer();
        for (int i = path.length - 1; i >= 0; --i) {
          sb.writeCharCode(path[i] + 97);
        }
        final candidate = sb.toString();
        if (best == null || candidate.compareTo(best!) < 0) {
          best = candidate;
        }
      } else {
        dfs(node.left);
        dfs(node.right);
      }
      path.removeLast();
    }

    dfs(root);
    return best ?? '';
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
var result string

func smallestFromLeaf(root *TreeNode) string {
    result = ""
    dfs(root, nil)
    return result
}

func dfs(node *TreeNode, path []byte) {
    if node == nil {
        return
    }
    // Append current character (from root towards leaf)
    path = append(path, byte('a'+node.Val))
    if node.Left == nil && node.Right == nil {
        // Leaf: construct string from leaf to root by reversing the path
        n := len(path)
        rev := make([]byte, n)
        for i := 0; i < n; i++ {
            rev[i] = path[n-1-i]
        }
        s := string(rev)
        if result == "" || s < result {
            result = s
        }
        return
    }
    dfs(node.Left, path)
    dfs(node.Right, path)
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

def smallest_from_leaf(root)
  smallest = nil
  dfs = lambda do |node, path|
    return if node.nil?
    new_path = (('a'.ord + node.val).chr) + path
    if node.left.nil? && node.right.nil?
      smallest = new_path if smallest.nil? || new_path < smallest
    else
      dfs.call(node.left, new_path)
      dfs.call(node.right, new_path)
    end
  end
  dfs.call(root, "")
  smallest
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
    def smallestFromLeaf(root: TreeNode): String = {
        var best = ""
        def dfs(node: TreeNode, cur: String): Unit = {
            if (node == null) return
            val newStr = (('a' + node.value).toChar) + cur
            if (node.left == null && node.right == null) {
                if (best.isEmpty || newStr < best) best = newStr
            } else {
                dfs(node.left, newStr)
                dfs(node.right, newStr)
            }
        }
        dfs(root, "")
        best
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, path: &mut Vec<u8>, best: &mut Option<String>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                path.push((n.val as u8) + b'a');
                if n.left.is_none() && n.right.is_none() {
                    let cand: String = path.iter().rev().map(|&c| c as char).collect();
                    match best {
                        None => *best = Some(cand),
                        Some(cur) => {
                            if cand < *cur {
                                *cur = cand;
                            }
                        }
                    }
                } else {
                    dfs(&n.left, path, best);
                    dfs(&n.right, path, best);
                }
                path.pop();
            }
        }

        let mut best: Option<String> = None;
        let mut path: Vec<u8> = Vec::new();
        dfs(&root, &mut path, &mut best);
        best.unwrap_or_default()
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define/contract (smallest-from-leaf root)
  (-> (or/c tree-node? #f) string?)
  (if (not root)
      ""
      (let ([best (box #f)])
        (define (dfs node path)
          (when node
            (let* ((c (integer->char (+ (tree-node-val node) 97)))
                   (new-path (cons c path)))
              (if (and (not (tree-node-left node))
                       (not (tree-node-right node)))
                  (let ([candidate (list->string (reverse new-path))])
                    (when (or (not (unbox best))
                              (string<? candidate (unbox best)))
                      (set-box! best candidate)))
                  (begin
                    (dfs (tree-node-left node) new-path)
                    (dfs (tree-node-right node) new-path))))))

        (dfs root '())
        (unbox best))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_from_leaf/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec smallest_from_leaf(Root :: #tree_node{} | null) -> unicode:unicode_binary().
smallest_from_leaf(null) ->
    <<>>;
smallest_from_leaf(Root) ->
    case dfs(Root, [], undefined) of
        undefined -> <<>>;
        Bin -> Bin
    end.

dfs(null, _Acc, Best) ->
    Best;
dfs(Node, Acc, Best) when is_record(Node, tree_node) ->
    Char = $a + Node#tree_node.val,
    NewAcc = [Char | Acc],
    case {Node#tree_node.left, Node#tree_node.right} of
        {null, null} -> % leaf node
            CurrBin = list_to_binary(NewAcc),
            case Best of
                undefined -> CurrBin;
                _ when CurrBin < Best -> CurrBin;
                _ -> Best
            end;
        _ ->
            Best1 = case Node#tree_node.left of
                        null -> Best;
                        Left -> dfs(Left, NewAcc, Best)
                    end,
            Best2 = case Node#tree_node.right of
                        null -> Best1;
                        Right -> dfs(Right, NewAcc, Best1)
                    end,
            Best2
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_from_leaf(root :: TreeNode.t | nil) :: String.t
  def smallest_from_leaf(nil), do: ""

  def smallest_from_leaf(root) do
    dfs(root)
  end

  defp dfs(nil), do: nil

  defp dfs(%TreeNode{val: v, left: l, right: r}) do
    left_str = dfs(l)
    right_str = dfs(r)

    cur_char = <<v + ?a>>

    cond do
      left_str == nil and right_str == nil ->
        cur_char

      left_str == nil ->
        cur_char <> right_str

      right_str == nil ->
        cur_char <> left_str

      true ->
        s1 = cur_char <> left_str
        s2 = cur_char <> right_str

        case String.compare(s1, s2) do
          :lt -> s1
          _ -> s2
        end
    end
  end
end
```
