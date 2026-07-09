# 1448. Count Good Nodes in Binary Tree

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
    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        int count = 0;
        std::stack<std::pair<TreeNode*, int>> st;
        st.emplace(root, root->val);
        while (!st.empty()) {
            auto [node, curMax] = st.top();
            st.pop();
            if (node->val >= curMax) {
                ++count;
                curMax = node->val;
            }
            if (node->right) st.emplace(node->right, curMax);
            if (node->left)  st.emplace(node->left,  curMax);
        }
        return count;
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
    private int goodCount;

    public int goodNodes(TreeNode root) {
        goodCount = 0;
        dfs(root, root.val);
        return goodCount;
    }

    private void dfs(TreeNode node, int currentMax) {
        if (node == null) {
            return;
        }
        if (node.val >= currentMax) {
            goodCount++;
            currentMax = node.val;
        }
        dfs(node.left, currentMax);
        dfs(node.right, currentMax);
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
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        stack = [(root, root.val)]
        while stack:
            node, cur_max = stack.pop()
            if node.val >= cur_max:
                count += 1
            new_max = max(cur_max, node.val)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        return count
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
    def goodNodes(self, root: 'TreeNode') -> int:
        count = 0
        stack = [(root, root.val)]
        while stack:
            node, cur_max = stack.pop()
            if node.val >= cur_max:
                count += 1
                new_max = node.val
            else:
                new_max = cur_max
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        return count
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

static int dfs(struct TreeNode* node, int curMax) {
    if (!node) return 0;
    int isGood = (node->val >= curMax) ? 1 : 0;
    int newMax = (node->val > curMax) ? node->val : curMax;
    return isGood + dfs(node->left, newMax) + dfs(node->right, newMax);
}

int goodNodes(struct TreeNode* root){
    if (!root) return 0;
    return dfs(root, root->val);
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
    public int GoodNodes(TreeNode root) {
        if (root == null) return 0;

        int count = 0;
        var stack = new Stack<(TreeNode node, int maxSoFar)>();
        stack.Push((root, root.val));

        while (stack.Count > 0)
        {
            var (node, curMax) = stack.Pop();

            if (node.val >= curMax)
                count++;

            int newMax = Math.Max(curMax, node.val);

            if (node.left != null)
                stack.Push((node.left, newMax));
            if (node.right != null)
                stack.Push((node.right, newMax));
        }

        return count;
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
var goodNodes = function(root) {
    if (!root) return 0;
    let count = 0;
    const stack = [[root, root.val]];
    while (stack.length) {
        const [node, maxSoFar] = stack.pop();
        if (!node) continue;
        if (node.val >= maxSoFar) count++;
        const newMax = Math.max(maxSoFar, node.val);
        if (node.right) stack.push([node.right, newMax]);
        if (node.left)  stack.push([node.left, newMax]);
    }
    return count;
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

function goodNodes(root: TreeNode | null): number {
    if (!root) return 0;
    let count = 0;
    const stack: [TreeNode, number][] = [[root, root.val]];
    while (stack.length) {
        const [node, curMax] = stack.pop()!;
        if (node.val >= curMax) count++;
        const newMax = Math.max(curMax, node.val);
        if (node.left) stack.push([node.left, newMax]);
        if (node.right) stack.push([node.right, newMax]);
    }
    return count;
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
     * @return Integer
     */
    function goodNodes($root) {
        if ($root === null) {
            return 0;
        }
        $count = 0;
        $stack = [[$root, $root->val]];
        while (!empty($stack)) {
            [$node, $maxSoFar] = array_pop($stack);
            if ($node->val >= $maxSoFar) {
                $count++;
                $newMax = $node->val;
            } else {
                $newMax = $maxSoFar;
            }
            if ($node->right !== null) {
                $stack[] = [$node->right, $newMax];
            }
            if ($node->left !== null) {
                $stack[] = [$node->left, $newMax];
            }
        }
        return $count;
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
    func goodNodes(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }
        return dfs(node, node.val)
    }
    
    private func dfs(_ node: TreeNode?, _ currentMax: Int) -> Int {
        guard let n = node else { return 0 }
        var count = 0
        if n.val >= currentMax {
            count += 1
        }
        let newMax = max(currentMax, n.val)
        count += dfs(n.left, newMax)
        count += dfs(n.right, newMax)
        return count
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
    fun goodNodes(root: TreeNode?): Int {
        if (root == null) return 0
        var count = 0
        val stack = java.util.ArrayDeque<Pair<TreeNode, Int>>()
        stack.push(Pair(root, root.`val`))
        while (!stack.isEmpty()) {
            val (node, maxSoFar) = stack.pop()
            if (node.`val` >= maxSoFar) count++
            val newMax = kotlin.math.max(maxSoFar, node.`val`)
            node.left?.let { stack.push(Pair(it, newMax)) }
            node.right?.let { stack.push(Pair(it, newMax)) }
        }
        return count
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
func goodNodes(root *TreeNode) int {
    if root == nil {
        return 0
    }
    var dfs func(node *TreeNode, maxSoFar int) int
    dfs = func(node *TreeNode, maxSoFar int) int {
        if node == nil {
            return 0
        }
        count := 0
        if node.Val >= maxSoFar {
            count = 1
            maxSoFar = node.Val
        }
        return count + dfs(node.Left, maxSoFar) + dfs(node.Right, maxSoFar)
    }
    return dfs(root, root.Val)
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

def good_nodes(root)
  return 0 unless root
  count = 0
  stack = [[root, root.val]]
  until stack.empty?
    node, cur_max = stack.pop
    count += 1 if node.val >= cur_max
    new_max = [cur_max, node.val].max
    stack << [node.right, new_max] if node.right
    stack << [node.left, new_max] if node.left
  end
  count
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
    def goodNodes(root: TreeNode): Int = {
        if (root == null) return 0
        var count = 0
        val stack = new java.util.ArrayDeque[(TreeNode, Int)]()
        stack.push((root, root.value))
        while (!stack.isEmpty) {
            val (node, maxSoFar) = stack.pop()
            if (node != null) {
                if (node.value >= maxSoFar) count += 1
                val newMax = Math.max(maxSoFar, node.value)
                if (node.left != null) stack.push((node.left, newMax))
                if (node.right != null) stack.push((node.right, newMax))
            }
        }
        count
    }
}
```

## Rust

```rust
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
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut count = 0i32;
        let mut stack: Vec<(Rc<RefCell<TreeNode>>, i32)> = Vec::new();
        let rc_root = root.unwrap();
        stack.push((rc_root, i32::MIN));
        while let Some((node_rc, cur_max)) = stack.pop() {
            let node_ref = node_rc.borrow();
            let val = node_ref.val;
            if val >= cur_max {
                count += 1;
            }
            let new_max = std::cmp::max(cur_max, val);
            if let Some(left) = &node_ref.left {
                stack.push((Rc::clone(left), new_max));
            }
            if let Some(right) = &node_ref.right {
                stack.push((Rc::clone(right), new_max));
            }
        }
        count
    }
}
```
