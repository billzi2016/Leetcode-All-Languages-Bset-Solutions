# 0872. Leaf-Similar Trees

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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1, leaves2;
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        return leaves1 == leaves2;
    }
private:
    void dfs(TreeNode* node, vector<int>& leaves) {
        if (!node) return;
        if (!node->left && !node->right) {
            leaves.push_back(node->val);
            return;
        }
        dfs(node->left, leaves);
        dfs(node->right, leaves);
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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList<>();
        List<Integer> leaves2 = new ArrayList<>();
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        return leaves1.equals(leaves2);
    }
    
    private void dfs(TreeNode node, List<Integer> leaves) {
        if (node == null) {
            return;
        }
        if (node.left == null && node.right == null) {
            leaves.add(node.val);
        } else {
            dfs(node.left, leaves);
            dfs(node.right, leaves);
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
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            dfs(node.left, leaves)
            dfs(node.right, leaves)

        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
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
#include <stdbool.h>

static void dfs(struct TreeNode* node, int *leaves, int *cnt) {
    if (!node) return;
    if (!node->left && !node->right) {
        leaves[(*cnt)++] = node->val;
        return;
    }
    dfs(node->left, leaves, cnt);
    dfs(node->right, leaves, cnt);
}

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2) {
    int leaves1[200];
    int leaves2[200];
    int sz1 = 0, sz2 = 0;
    
    dfs(root1, leaves1, &sz1);
    dfs(root2, leaves2, &sz2);
    
    if (sz1 != sz2) return false;
    for (int i = 0; i < sz1; ++i) {
        if (leaves1[i] != leaves2[i]) return false;
    }
    return true;
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
    public bool LeafSimilar(TreeNode root1, TreeNode root2)
    {
        var leaves1 = new List<int>();
        var leaves2 = new List<int>();
        CollectLeaves(root1, leaves1);
        CollectLeaves(root2, leaves2);
        if (leaves1.Count != leaves2.Count) return false;
        for (int i = 0; i < leaves1.Count; i++)
        {
            if (leaves1[i] != leaves2[i]) return false;
        }
        return true;
    }

    private void CollectLeaves(TreeNode node, List<int> leaves)
    {
        if (node == null) return;
        if (node.left == null && node.right == null)
        {
            leaves.Add(node.val);
            return;
        }
        CollectLeaves(node.left, leaves);
        CollectLeaves(node.right, leaves);
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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    const leaves1 = [];
    const leaves2 = [];

    const dfs = (node, arr) => {
        if (!node) return;
        if (!node.left && !node.right) {
            arr.push(node.val);
            return;
        }
        dfs(node.left, arr);
        dfs(node.right, arr);
    };

    dfs(root1, leaves1);
    dfs(root2, leaves2);

    if (leaves1.length !== leaves2.length) return false;
    for (let i = 0; i < leaves1.length; ++i) {
        if (leaves1[i] !== leaves2[i]) return false;
    }
    return true;
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

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    const leaves1: number[] = [];
    const leaves2: number[] = [];

    const dfs = (node: TreeNode | null, out: number[]) => {
        if (!node) return;
        if (!node.left && !node.right) {
            out.push(node.val);
        } else {
            dfs(node.left, out);
            dfs(node.right, out);
        }
    };

    dfs(root1, leaves1);
    dfs(root2, leaves2);

    if (leaves1.length !== leaves2.length) return false;
    for (let i = 0; i < leaves1.length; ++i) {
        if (leaves1[i] !== leaves2[i]) return false;
    }
    return true;
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
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return bool
     */
    function leafSimilar($root1, $root2) {
        $leaves1 = [];
        $leaves2 = [];
        $this->dfs($root1, $leaves1);
        $this->dfs($root2, $leaves2);
        return $leaves1 == $leaves2;
    }

    private function dfs($node, &$arr) {
        if ($node === null) {
            return;
        }
        if ($node->left === null && $node->right === null) {
            $arr[] = $node->val;
            return;
        }
        $this->dfs($node->left, $arr);
        $this->dfs($node->right, $arr);
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
    func leafSimilar(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        var leaves1 = [Int]()
        var leaves2 = [Int]()
        dfs(root1, &leaves1)
        dfs(root2, &leaves2)
        return leaves1 == leaves2
    }
    
    private func dfs(_ node: TreeNode?, _ result: inout [Int]) {
        guard let n = node else { return }
        if n.left == nil && n.right == nil {
            result.append(n.val)
        } else {
            dfs(n.left, &result)
            dfs(n.right, &result)
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
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        val leaves1 = mutableListOf<Int>()
        val leaves2 = mutableListOf<Int>()
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
    }

    private fun dfs(node: TreeNode?, list: MutableList<Int>) {
        if (node == null) return
        if (node.left == null && node.right == null) {
            list.add(node.`val`)
        } else {
            dfs(node.left, list)
            dfs(node.right, list)
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
  bool leafSimilar(TreeNode? root1, TreeNode? root2) {
    List<int> leaves1 = [];
    List<int> leaves2 = [];
    _dfs(root1, leaves1);
    _dfs(root2, leaves2);
    if (leaves1.length != leaves2.length) return false;
    for (int i = 0; i < leaves1.length; i++) {
      if (leaves1[i] != leaves2[i]) return false;
    }
    return true;
  }

  void _dfs(TreeNode? node, List<int> leaves) {
    if (node == null) return;
    if (node.left == null && node.right == null) {
      leaves.add(node.val);
      return;
    }
    _dfs(node.left, leaves);
    _dfs(node.right, leaves);
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
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leaves1 := []int{}
	leaves2 := []int{}
	
	var dfs func(node *TreeNode, out *[]int)
	dfs = func(node *TreeNode, out *[]int) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil {
			*out = append(*out, node.Val)
			return
		}
		dfs(node.Left, out)
		dfs(node.Right, out)
	}
	
	dfs(root1, &leaves1)
	dfs(root2, &leaves2)
	
	if len(leaves1) != len(leaves2) {
		return false
	}
	for i := range leaves1 {
		if leaves1[i] != leaves2[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def leaf_similar(root1, root2)
  leaves1 = []
  leaves2 = []

  dfs = lambda do |node, arr|
    return if node.nil?
    if node.left.nil? && node.right.nil?
      arr << node.val
    else
      dfs.call(node.left, arr)
      dfs.call(node.right, arr)
    end
  end

  dfs.call(root1, leaves1)
  dfs.call(root2, leaves2)

  leaves1 == leaves2
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

  private def dfs(node: TreeNode, leaves: ListBuffer[Int]): Unit = {
    if (node == null) return
    if (node.left == null && node.right == null) {
      leaves += node.value
    } else {
      dfs(node.left, leaves)
      dfs(node.right, leaves)
    }
  }

  def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {
    val leaves1 = ListBuffer[Int]()
    val leaves2 = ListBuffer[Int]()
    dfs(root1, leaves1)
    dfs(root2, leaves2)
    leaves1 == leaves2
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, leaves: &mut Vec<i32>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                if n.left.is_none() && n.right.is_none() {
                    leaves.push(n.val);
                } else {
                    dfs(&n.left, leaves);
                    dfs(&n.right, leaves);
                }
            }
        }

        let mut leaves1 = Vec::new();
        let mut leaves2 = Vec::new();
        dfs(&root1, &mut leaves1);
        dfs(&root2, &mut leaves2);
        leaves1 == leaves2
    }
}
```

## Racket

```racket
(define (collect node)
  (cond [(not node) '()]
        [(and (not (tree-node-left node)) (not (tree-node-right node)))
         (list (tree-node-val node))]
        [else
         (append (collect (tree-node-left node))
                 (collect (tree-node-right node)))]))

(define/contract (leaf-similar root1 root2)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) boolean?)
  (let ([leaves1 (collect root1)]
        [leaves2 (collect root2)])
    (equal? leaves1 leaves2)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec leaf_similar(Root1 :: #tree_node{} | null, Root2 :: #tree_node{} | null) -> boolean().
leaf_similar(Root1, Root2) ->
    leaf_seq(Root1) =:= leaf_seq(Root2).

leaf_seq(Root) ->
    lists:reverse(dfs(Root, [])).

dfs(null, Acc) ->
    Acc;
dfs(Node, Acc) when is_record(Node, tree_node) ->
    case {Node#tree_node.left, Node#tree_node.right} of
        {null, null} ->
            [Node#tree_node.val | Acc];
        _ ->
            Acc1 = dfs(Node#tree_node.left, Acc),
            dfs(Node#tree_node.right, Acc1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec leaf_similar(root1 :: TreeNode.t() | nil, root2 :: TreeNode.t() | nil) :: boolean()
  def leaf_similar(root1, root2) do
    get_leaves(root1) == get_leaves(root2)
  end

  defp get_leaves(nil), do: []

  defp get_leaves(root) do
    root
    |> collect([])
    |> Enum.reverse()
  end

  defp collect(nil, acc), do: acc

  defp collect(%TreeNode{left: nil, right: nil, val: v}, acc), do: [v | acc]

  defp collect(%TreeNode{left: l, right: r}, acc) do
    acc = collect(r, acc)
    collect(l, acc)
  end
end
```
