# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

## Cpp

```cpp
/ **
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        return dfs(original, cloned, target);
    }
private:
    TreeNode* dfs(TreeNode* o, TreeNode* c, TreeNode* target) {
        if (!o) return nullptr;
        if (o == target) return c;
        TreeNode* leftRes = dfs(o->left, c->left, target);
        if (leftRes) return leftRes;
        return dfs(o->right, c->right, target);
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
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        if (original == null) {
            return null;
        }
        if (original == target) {
            return cloned;
        }
        TreeNode leftResult = getTargetCopy(original.left, cloned.left, target);
        if (leftResult != null) {
            return leftResult;
        }
        return getTargetCopy(original.right, cloned.right, target);
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        stack = [(original, cloned)]
        while stack:
            o_node, c_node = stack.pop()
            if o_node is target:
                return c_node
            if o_node.right:
                stack.append((o_node.right, c_node.right))
            if o_node.left:
                stack.append((o_node.left, c_node.left))
        return None
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def getTargetCopy(self, original: 'TreeNode', cloned: 'TreeNode', target: 'TreeNode') -> 'TreeNode':
        queue = deque([(original, cloned)])
        while queue:
            o_node, c_node = queue.popleft()
            if o_node is target:
                return c_node
            if o_node.left:
                queue.append((o_node.left, c_node.left))
            if o_node.right:
                queue.append((o_node.right, c_node.right))
        return None
```

## Csharp

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode GetTargetCopy(TreeNode original, TreeNode cloned, TreeNode target) {
        if (original == null) return null;
        if (original == target) return cloned;
        
        var leftResult = GetTargetCopy(original.left, cloned.left, target);
        if (leftResult != null) return leftResult;
        
        return GetTargetCopy(original.right, cloned.right, target);
    }
}
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 *
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */
var getTargetCopy = function(original, cloned, target) {
    const dfs = (o, c) => {
        if (!o) return null;
        if (o === target) return c;
        const leftRes = dfs(o.left, c.left);
        if (leftRes) return leftRes;
        return dfs(o.right, c.right);
    };
    return dfs(original, cloned);
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

function getTargetCopy(original: TreeNode | null, cloned: TreeNode | null, target: TreeNode | null): TreeNode | null {
    if (!original || !cloned) return null;
    if (original === target) return cloned;

    const leftResult = getTargetCopy(original.left, cloned.left, target);
    if (leftResult !== null) return leftResult;

    return getTargetCopy(original.right, cloned.right, target);
}
```
