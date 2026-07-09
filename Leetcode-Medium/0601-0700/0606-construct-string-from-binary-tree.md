# 0606. Construct String from Binary Tree

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
    string tree2str(TreeNode* root) {
        return build(root);
    }
private:
    string build(TreeNode* node) {
        if (!node) return "";
        string res = to_string(node->val);
        if (node->left || node->right) {
            // left subtree
            if (node->left) {
                res += "(" + build(node->left) + ")";
            } else {
                // need empty parentheses when right child exists
                res += "()";
            }
            // right subtree
            if (node->right) {
                res += "(" + build(node->right) + ")";
            }
        }
        return res;
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
    public String tree2str(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        build(root, sb);
        return sb.toString();
    }

    private void build(TreeNode node, StringBuilder sb) {
        sb.append(node.val);
        if (node.left != null) {
            sb.append('(');
            build(node.left, sb);
            sb.append(')');
        } else if (node.right != null) { // need empty parentheses for missing left child
            sb.append("()");
        }
        if (node.right != null) {
            sb.append('(');
            build(node.right, sb);
            sb.append(')');
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
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ''
            res = str(node.val)
            # Process left child; include parentheses if left exists or right exists
            if node.left or node.right:
                res += '(' + dfs(node.left) + ')'
            # Process right child only if it exists
            if node.right:
                res += '(' + dfs(node.right) + ')'
            return res

        return dfs(root)
```

## Python3

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = str(root.val)
        if root.left or root.right:
            # Left child (or empty placeholder if only right exists)
            if root.left:
                s += "(" + self.tree2str(root.left) + ")"
            else:
                s += "()"
            # Right child
            if root.right:
                s += "(" + self.tree2str(root.right) + ")"
        return s
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
#include <stdlib.h>
#include <stdio.h>

static int numDigits(int x) {
    if (x == 0) return 1;
    int cnt = 0;
    if (x < 0) { cnt++; x = -x; }
    while (x) { cnt++; x /= 10; }
    return cnt;
}

static int calcLen(struct TreeNode* node) {
    if (!node) return 0;
    int len = numDigits(node->val);
    if (node->left || node->right) {
        len += 2;                     // '(' and ')'
        if (node->left) len += calcLen(node->left);
    }
    if (node->right) {
        len += 2;
        len += calcLen(node->right);
    }
    return len;
}

static void buildStr(struct TreeNode* node, char **p) {
    if (!node) return;
    int n = sprintf(*p, "%d", node->val);
    *p += n;
    if (node->left || node->right) {
        **p = '('; (*p)++;
        if (node->left) buildStr(node->left, p);
        **p = ')'; (*p)++;
    }
    if (node->right) {
        **p = '('; (*p)++;
        buildStr(node->right, p);
        **p = ')'; (*p)++;
    }
}

char* tree2str(struct TreeNode* root) {
    if (!root) {
        char *empty = (char*)malloc(1);
        if (empty) empty[0] = '\0';
        return empty;
    }
    int len = calcLen(root);
    char *buf = (char*)malloc(len + 1);
    char *ptr = buf;
    buildStr(root, &ptr);
    *ptr = '\0';
    return buf;
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
using System.Text;

public class Solution {
    public string Tree2str(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        Build(root, sb);
        return sb.ToString();
    }

    private void Build(TreeNode node, StringBuilder sb) {
        sb.Append(node.val);
        // If there is at least one child, we need to process left parentheses
        if (node.left != null || node.right != null) {
            sb.Append('(');
            if (node.left != null) {
                Build(node.left, sb);
            }
            sb.Append(')');
            if (node.right != null) {
                sb.Append('(');
                Build(node.right, sb);
                sb.Append(')');
            }
        }
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
var tree2str = function(root) {
    const dfs = (node) => {
        if (!node) return "";
        let s = "" + node.val;
        if (node.left || node.right) {
            // left child
            if (node.left) {
                s += "(" + dfs(node.left) + ")";
            } else {
                s += "()";
            }
            // right child
            if (node.right) {
                s += "(" + dfs(node.right) + ")";
            }
        }
        return s;
    };
    return dfs(root);
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

function tree2str(root: TreeNode | null): string {
    if (!root) return "";
    
    const dfs = (node: TreeNode | null): string => {
        if (!node) return "";
        let s = "" + node.val;
        // If there is at least one child, we need to handle parentheses
        if (node.left || node.right) {
            if (node.left) {
                s += "(" + dfs(node.left) + ")";
            } else {
                // left child missing but right exists -> empty ()
                s += "()";
            }
            if (node.right) {
                s += "(" + dfs(node.right) + ")";
            }
        }
        return s;
    };
    
    return dfs(root);
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
    function tree2str($root) {
        if ($root === null) {
            return "";
        }

        $result = (string)$root->val;

        // If there is a left child or we need to represent an empty left because right exists
        if ($root->left !== null || $root->right !== null) {
            if ($root->left !== null) {
                $result .= '(' . $this->tree2str($root->left) . ')';
            } else {
                // left is null but right exists, need empty parentheses
                $result .= '()';
            }

            if ($root->right !== null) {
                $result .= '(' . $this->tree2str($root->right) . ')';
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
    func tree2str(_ root: TreeNode?) -> String {
        guard let node = root else { return "" }
        var result = "\(node.val)"
        if node.left == nil && node.right == nil {
            // leaf node, nothing to add
        } else if node.right == nil {
            // only left child exists
            result += "(\(tree2str(node.left)))"
        } else {
            // right child exists (left may be nil)
            result += "(\(tree2str(node.left)))"
            result += "(\(tree2str(node.right)))"
        }
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
    fun tree2str(root: TreeNode?): String {
        if (root == null) return ""
        val sb = StringBuilder()
        build(root, sb)
        return sb.toString()
    }

    private fun build(node: TreeNode?, sb: StringBuilder) {
        if (node == null) return
        sb.append(node.`val`)
        if (node.left == null && node.right == null) return

        // left subtree (may be empty)
        sb.append('(')
        if (node.left != null) build(node.left, sb)
        sb.append(')')

        // right subtree (only if exists)
        if (node.right != null) {
            sb.append('(')
            build(node.right, sb)
            sb.append(')')
        }
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
  String tree2str(TreeNode? root) {
    if (root == null) return '';
    // Leaf node
    if (root.left == null && root.right == null) {
      return '${root.val}';
    }

    String leftPart = '';
    if (root.left != null) {
      leftPart = '(${tree2str(root.left)})';
    } else if (root.right != null) {
      // Need empty parentheses when left child is missing but right exists
      leftPart = '()';
    }

    String rightPart = '';
    if (root.right != null) {
      rightPart = '(${tree2str(root.right)})';
    }

    return '${root.val}$leftPart$rightPart';
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func tree2str(root *TreeNode) string {
	var sb strings.Builder
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		sb.WriteString(strconv.Itoa(node.Val))
		if node.Left != nil || node.Right != nil {
			sb.WriteByte('(')
			if node.Left != nil {
				dfs(node.Left)
			}
			sb.WriteByte(')')
			if node.Right != nil {
				sb.WriteByte('(')
				dfs(node.Right)
				sb.WriteByte(')')
			}
		}
	}
	dfs(root)
	return sb.String()
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

def tree2str(root)
  return "" if root.nil?
  result = root.val.to_s
  if root.left || root.right
    if root.left
      result << "(" + tree2str(root.left) + ")"
    else
      result << "()"
    end
    if root.right
      result << "(" + tree2str(root.right) + ")"
    end
  end
  result
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
    def tree2str(root: TreeNode): String = {
        if (root == null) return ""
        val sb = new StringBuilder

        def dfs(node: TreeNode): Unit = {
            if (node == null) return
            sb.append(node.value)
            if (node.left != null || node.right != null) {
                // left child (may be empty)
                sb.append('(')
                if (node.left != null) dfs(node.left)
                sb.append(')')
                // right child (only if exists)
                if (node.right != null) {
                    sb.append('(')
                    dfs(node.right)
                    sb.append(')')
                }
            }
        }

        dfs(root)
        sb.toString()
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn tree2str(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: Rc<RefCell<TreeNode>>) -> String {
            let n = node.borrow();
            let val_str = n.val.to_string();
            match (n.left.clone(), n.right.clone()) {
                (None, None) => val_str,
                (Some(l), None) => format!("{}({})", val_str, dfs(l)),
                (None, Some(r)) => format!("{}()({})", val_str, dfs(r)),
                (Some(l), Some(r)) => format!("{}({})({})", val_str, dfs(l), dfs(r)),
            }
        }

        if let Some(node) = root {
            dfs(node)
        } else {
            String::new()
        }
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define/contract (tree2str root)
  (-> (or/c tree-node? #f) string?)
  (letrec ((helper
            (lambda (node)
              (if (not node)
                  ""
                  (let* ((v (number->string (tree-node-val node)))
                         (l (tree-node-left node))
                         (r (tree-node-right node))
                         (left-part
                          (cond [(and (not l) (not r)) ""]
                                [l (string-append "(" (helper l) ")")]
                                [else "()"]))
                         (right-part (if r (string-append "(" (helper r) ")") "")))
                    (string-append v left-part right-part))))))
    (helper root)))
```

## Erlang

```erlang
-module(solution).
-export([tree2str/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec tree2str(Root :: #tree_node{} | null) -> unicode:unicode_binary().
tree2str(Root) ->
    list_to_binary(build(Root)).

build(null) ->
    "";
build(#tree_node{val = V, left = L, right = R}) ->
    ValStr = integer_to_list(V),
    case {L, R} of
        {null, null} -> 
            ValStr;
        {_, null} -> 
            ValStr ++ "(" ++ build(L) ++ ")";
        {null, _} -> 
            ValStr ++ "()" ++ "(" ++ build(R) ++ ")";
        _ -> 
            ValStr ++ "(" ++ build(L) ++ ")" ++ "(" ++ build(R) ++ ")"
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec tree2str(root :: TreeNode.t | nil) :: String.t
  def tree2str(root) do
    build(root)
  end

  defp build(nil), do: ""

  defp build(%TreeNode{val: v, left: l, right: r}) do
    s = Integer.to_string(v)

    case {l, r} do
      {nil, nil} ->
        s

      {_left, nil} ->
        s <> "(" <> build(l) <> ")"

      {nil, _right} ->
        s <> "()" <> "(" <> build(r) <> ")"

      {_left, _right} ->
        s <> "(" <> build(l) <> ")" <> "(" <> build(r) <> ")"
    end
  end
end
```
