# 2458. Height of Binary Tree After Subtree Removal Queries

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
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        unordered_map<TreeNode*, int> height;
        int maxVal = 0;
        function<int(TreeNode*)> dfsHeight = [&](TreeNode* node) -> int {
            if (!node) return -1;               // leaf's child contributes -1
            maxVal = max(maxVal, node->val);
            int lh = dfsHeight(node->left);
            int rh = dfsHeight(node->right);
            int cur = max(lh, rh) + 1;
            height[node] = cur;
            return cur;
        };
        dfsHeight(root);

        vector<int> answer(maxVal + 1, 0);
        function<void(TreeNode*, int, int)> dfsAns = [&](TreeNode* node, int depth, int up) {
            if (!node) return;
            answer[node->val] = up;
            int lh = node->left ? height[node->left] : -1;
            int rh = node->right ? height[node->right] : -1;

            if (node->left) {
                int viaSibling = depth + 1 + rh;          // path through right sibling
                int childUp = max(up, viaSibling);
                dfsAns(node->left, depth + 1, childUp);
            }
            if (node->right) {
                int viaSibling = depth + 1 + lh;          // path through left sibling
                int childUp = max(up, viaSibling);
                dfsAns(node->right, depth + 1, childUp);
            }
        };
        dfsAns(root, 0, -1);   // root has no external path

        vector<int> res;
        res.reserve(queries.size());
        for (int q : queries) {
            res.push_back(answer[q]);
        }
        return res;
    }
};
```

## Java

```java
/ **
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
 * /
class Solution {
    private int[] down;
    private int[] depth;
    private int[] ans;

    public int[] treeQueries(TreeNode root, int[] queries) {
        // constraints: 1 <= val <= n <= 100000
        int maxSize = 100005;
        down = new int[maxSize];
        depth = new int[maxSize];
        ans = new int[maxSize];

        dfsDown(root, 0);          // compute subtree heights and depths
        dfsAns(root, -1);          // propagate answers for each node

        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; ++i) {
            res[i] = ans[queries[i]];
        }
        return res;
    }

    private int dfsDown(TreeNode node, int d) {
        if (node == null) return -1;          // height of empty subtree
        depth[node.val] = d;
        int leftH = dfsDown(node.left, d + 1);
        int rightH = dfsDown(node.right, d + 1);
        int h = Math.max(leftH, rightH) + 1;
        down[node.val] = h;
        return h;
    }

    private void dfsAns(TreeNode node, int up) {
        if (node == null) return;
        ans[node.val] = up;

        // process left child
        if (node.left != null) {
            int siblingHeight = (node.right != null) ? down[node.right.val] : -1;
            int best = Math.max(up, depth[node.val]);               // path ending at parent
            if (siblingHeight != -1) {
                best = Math.max(best, depth[node.val] + 1 + siblingHeight);
            }
            dfsAns(node.left, best);
        }

        // process right child
        if (node.right != null) {
            int siblingHeight = (node.left != null) ? down[node.left.val] : -1;
            int best = Math.max(up, depth[node.val]);
            if (siblingHeight != -1) {
                best = Math.max(best, depth[node.val] + 1 + siblingHeight);
            }
            dfsAns(node.right, best);
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
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(300000)

        n_estimate = 100005  # upper bound for allocation
        down = [0] * (n_estimate)      # subtree height
        depth = [0] * (n_estimate)     # depth from root
        ans = [0] * (n_estimate)       # answer for each node value

        def dfs1(node, d):
            if not node:
                return -1  # height of empty subtree
            depth[node.val] = d
            lh = dfs1(node.left, d + 1)
            rh = dfs1(node.right, d + 1)
            h = 1 + max(lh, rh)
            down[node.val] = h
            return h

        def dfs2(node, best_up):
            if not node:
                return
            ans[node.val] = best_up
            left = node.left
            right = node.right
            left_h = down[left.val] if left else -1
            right_h = down[right.val] if right else -1

            if left:
                cand = depth[node.val] + 1 + (right_h)
                new_best = best_up if best_up > cand else cand
                dfs2(left, new_best)

            if right:
                cand = depth[node.val] + 1 + (left_h)
                new_best = best_up if best_up > cand else cand
                dfs2(right, new_best)

        dfs1(root, 0)
        dfs2(root, -1)   # root has no external path

        return [ans[q] for q in queries]
```

## Python3

```python
import sys
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional['TreeNode'], queries: List[int]) -> List[int]:
        sys.setrecursionlimit(200000)

        # First pass: compute height of each subtree.
        height = {}
        def dfs_height(node):
            if not node:
                return -1
            lh = dfs_height(node.left)
            rh = dfs_height(node.right)
            h = max(lh, rh) + 1
            height[node.val] = h
            return h

        dfs_height(root)

        # Second pass: propagate the best possible height after removing each node.
        answer = {}
        def dfs_ans(node, depth, best):
            if not node:
                return
            answer[node.val] = best
            left, right = node.left, node.right
            lh = height[left.val] if left else -1
            rh = height[right.val] if right else -1

            if left:
                sibling_contrib = depth + 1 + rh if right else float('-inf')
                new_best = best if best > sibling_contrib else sibling_contrib
                dfs_ans(left, depth + 1, new_best)

            if right:
                sibling_contrib = depth + 1 + lh if left else float('-inf')
                new_best = best if best > sibling_contrib else sibling_contrib
                dfs_ans(right, depth + 1, new_best)

        # For the root, removing it would leave an empty tree (height 0), which serves as base.
        dfs_ans(root, 0, 0)

        return [answer[q] for q in queries]
```

## C

```c
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Helper to count nodes */
static int countNodes(struct TreeNode* node) {
    if (!node) return 0;
    return 1 + countNodes(node->left) + countNodes(node->right);
}

/* DFS that fills preorder order, depths, idx and subtree sizes */
static int dfsFill(struct TreeNode* node, int depth,
                   int *order, int *depthArr, int *idx, int *subSize, int *pos) {
    if (!node) return 0;
    int curPos = (*pos);
    order[curPos] = node->val;
    depthArr[curPos] = depth;
    idx[node->val] = curPos;
    (*pos)++;
    int leftSize = dfsFill(node->left, depth + 1, order, depthArr, idx, subSize, pos);
    int rightSize = dfsFill(node->right, depth + 1, order, depthArr, idx, subSize, pos);
    int total = 1 + leftSize + rightSize;
    subSize[node->val] = total;
    return total;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* treeQueries(struct TreeNode* root, int* queries, int queriesSize, int* returnSize) {
    int n = countNodes(root);
    int *order = (int*)malloc(n * sizeof(int));
    int *depthArr = (int*)malloc(n * sizeof(int));
    int *pref = (int*)malloc(n * sizeof(int));
    int *suff = (int*)malloc(n * sizeof(int));
    int *idx = (int*)calloc((n + 2), sizeof(int));      // value -> preorder index
    int *subSize = (int*)calloc((n + 2), sizeof(int));  // value -> subtree size

    int pos = 0;
    dfsFill(root, 0, order, depthArr, idx, subSize, &pos);

    /* prefix max depths */
    pref[0] = depthArr[0];
    for (int i = 1; i < n; ++i) {
        pref[i] = pref[i - 1] > depthArr[i] ? pref[i - 1] : depthArr[i];
    }
    /* suffix max depths */
    suff[n - 1] = depthArr[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        suff[i] = suff[i + 1] > depthArr[i] ? suff[i + 1] : depthArr[i];
    }

    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int v = queries[i];
        int l = idx[v];
        int r = l + subSize[v] - 1;
        int leftMax = (l > 0) ? pref[l - 1] : -1;
        int rightMax = (r + 1 < n) ? suff[r + 1] : -1;
        int res = leftMax > rightMax ? leftMax : rightMax;
        if (res < 0) res = 0;   // should not happen as root is never removed
        ans[i] = res;
    }

    free(order);
    free(depthArr);
    free(pref);
    free(suff);
    free(idx);
    free(subSize);

    *returnSize = queriesSize;
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
    public int[] TreeQueries(TreeNode root, int[] queries) {
        // Dictionaries to store depth from root and down heights
        var depth = new Dictionary<int, int>();
        var down = new Dictionary<int, int>();
        var answer = new Dictionary<int, int>();

        // First iterative post-order traversal to compute depths and down heights
        var stack = new Stack<(TreeNode node, bool visited)>();
        stack.Push((root, false));
        depth[root.val] = 0;

        while (stack.Count > 0) {
            var (node, visited) = stack.Pop();
            if (!visited) {
                // Pre-order part
                stack.Push((node, true)); // will process after children
                if (node.left != null) {
                    depth[node.left.val] = depth[node.val] + 1;
                    stack.Push((node.left, false));
                }
                if (node.right != null) {
                    depth[node.right.val] = depth[node.val] + 1;
                    stack.Push((node.right, false));
                }
            } else {
                // Post-order part: compute down height
                int leftH = node.left != null ? down[node.left.val] : -1;
                int rightH = node.right != null ? down[node.right.val] : -1;
                down[node.val] = Math.Max(leftH, rightH) + 1; // leaf gets 0
            }
        }

        // Second traversal to propagate best height outside each subtree
        var stack2 = new Stack<(TreeNode node, int upBest)>();
        stack2.Push((root, -1)); // root has no external part

        while (stack2.Count > 0) {
            var (node, upBest) = stack2.Pop();
            answer[node.val] = upBest;

            int leftH = node.left != null ? down[node.left.val] : -1;
            int rightH = node.right != null ? down[node.right.val] : -1;
            int depthNode = depth[node.val];

            if (node.left != null) {
                int best = Math.Max(upBest, depthNode);
                if (node.right != null)
                    best = Math.Max(best, depthNode + 1 + rightH);
                stack2.Push((node.left, best));
            }
            if (node.right != null) {
                int best = Math.Max(upBest, depthNode);
                if (node.left != null)
                    best = Math.Max(best, depthNode + 1 + leftH);
                stack2.Push((node.right, best));
            }
        }

        // Build result for queries
        int[] res = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            res[i] = answer[queries[i]];
        }
        return res;
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
 * @param {number[]} queries
 * @return {number[]}
 */
var treeQueries = function(root, queries) {
    // First pass: collect depth and order for post‑order height computation
    const stack = [{node: root, d: 0}];
    const order = [];
    let maxVal = 0;
    const depth = []; // index by node value
    while (stack.length) {
        const {node, d} = stack.pop();
        depth[node.val] = d;
        if (node.val > maxVal) maxVal = node.val;
        order.push(node);
        if (node.right) stack.push({node: node.right, d: d + 1});
        if (node.left)  stack.push({node: node.left,  d: d + 1});
    }

    // Height of subtree rooted at each node
    const height = new Array(maxVal + 1).fill(0);
    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        const leftH  = node.left  ? height[node.left.val]  + 1 : 0;
        const rightH = node.right ? height[node.right.val] + 1 : 0;
        height[node.val] = Math.max(leftH, rightH);
    }

    // Second pass: compute answer for each node (max distance from root to any leaf not in its subtree)
    const ansNode = new Array(maxVal + 1).fill(0);
    const stack2 = [{node: root, bestAbove: 0}];
    while (stack2.length) {
        const {node, bestAbove} = stack2.pop();
        ansNode[node.val] = bestAbove;
        const leftH  = node.left  ? height[node.left.val]  + 1 : 0;
        const rightH = node.right ? height[node.right.val] + 1 : 0;

        if (node.left) {
            const newBest = Math.max(bestAbove, depth[node.val] + rightH);
            stack2.push({node: node.left, bestAbove: newBest});
        }
        if (node.right) {
            const newBest = Math.max(bestAbove, depth[node.val] + leftH);
            stack2.push({node: node.right, bestAbove: newBest});
        }
    }

    // Answer queries
    const res = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        res[i] = ansNode[queries[i]];
    }
    return res;
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

function treeQueries(root: TreeNode | null, queries: number[]): number[] {
    if (!root) return [];

    const down = new Map<number, number>();   // height of subtree rooted at node
    const depth = new Map<number, number>();  // depth from root (edges)
    const answer = new Map<number, number>(); // result for each node

    // First DFS: compute depth and subtree heights
    function dfsDown(node: TreeNode | null, d: number): number {
        if (!node) return -1; // height of empty subtree
        depth.set(node.val, d);
        const leftH = dfsDown(node.left, d + 1);
        const rightH = dfsDown(node.right, d + 1);
        const h = Math.max(leftH, rightH) + 1;
        down.set(node.val, h);
        return h;
    }

    dfsDown(root, 0);

    // Second DFS: compute answer for each node using information from ancestors
    function dfsAns(node: TreeNode | null, bestAbove: number): void {
        if (!node) return;
        answer.set(node.val, bestAbove);
        const curDepth = depth.get(node.val)!;

        if (node.left) {
            const siblingContrib = node.right !== null
                ? curDepth + 1 + down.get(node.right!.val)!
                : Number.NEGATIVE_INFINITY;
            const bestForLeft = Math.max(bestAbove, curDepth, siblingContrib);
            dfsAns(node.left, bestForLeft);
        }
        if (node.right) {
            const siblingContrib = node.left !== null
                ? curDepth + 1 + down.get(node.left!.val)!
                : Number.NEGATIVE_INFINITY;
            const bestForRight = Math.max(bestAbove, curDepth, siblingContrib);
            dfsAns(node.right, bestForRight);
        }
    }

    // root has no nodes outside its subtree
    dfsAns(root, -1);

    const res: number[] = [];
    for (const q of queries) {
        res.push(answer.get(q)!);
    }
    return res;
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
    private $height = [];
    private $leftChild = [];
    private $rightChild = [];
    private $answer = [];

    private function computeHeight($node) {
        if ($node === null) {
            return -1; // height of empty subtree
        }
        $lh = $this->computeHeight($node->left);
        $rh = $this->computeHeight($node->right);
        $val = $node->val;
        $this->height[$val] = max($lh, $rh) + 1;
        $this->leftChild[$val] = $node->left ? $node->left->val : null;
        $this->rightChild[$val] = $node->right ? $node->right->val : null;
        return $this->height[$val];
    }

    private function computeUp($node, $up) {
        if ($node === null) {
            return;
        }
        $val = $node->val;
        $this->answer[$val] = $up;

        $l = $this->leftChild[$val];
        $r = $this->rightChild[$val];

        // Process left child
        if ($l !== null) {
            $siblingContribution = ($r !== null) ? $this->height[$r] + 1 : PHP_INT_MIN;
            $newUp = max($up, $siblingContribution);
            $this->computeUp($node->left, $newUp);
        }
        // Process right child
        if ($r !== null) {
            $siblingContribution = ($l !== null) ? $this->height[$l] + 1 : PHP_INT_MIN;
            $newUp = max($up, $siblingContribution);
            $this->computeUp($node->right, $newUp);
        }
    }

    /**
     * @param TreeNode $root
     * @param Integer[] $queries
     * @return Integer[]
     */
    function treeQueries($root, $queries) {
        $this->height = [];
        $this->leftChild = [];
        $this->rightChild = [];
        $this->answer = [];

        $this->computeHeight($root);
        // For the root, there is no ancestor path, so up value is 0 (the root itself)
        $this->computeUp($root, 0);

        $res = [];
        foreach ($queries as $q) {
            $res[] = $this->answer[$q];
        }
        return $res;
    }
}
?>
```

## Swift

```swift
/ **
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
    func treeQueries(_ root: TreeNode?, _ queries: [Int]) -> [Int] {
        guard let root = root else { return [] }
        var height = [Int:Int]()          // max distance from node down to a leaf (edges)
        var answer = [Int:Int]()          // result for each node
        
        func dfsHeight(_ node: TreeNode?) -> Int {
            guard let n = node else { return -1 }   // empty child contributes -1 so leaf gets 0
            let leftH = dfsHeight(n.left)
            let rightH = dfsHeight(n.right)
            let h = max(leftH, rightH) + 1
            height[n.val] = h
            return h
        }
        
        _ = dfsHeight(root)
        
        func dfsPass(_ node: TreeNode?, _ depth: Int, _ upDist: Int) {
            guard let n = node else { return }
            // upDist is the maximum distance from root to any leaf that does NOT lie in n's subtree
            answer[n.val] = upDist
            
            let leftH = n.left != nil ? height[n.left!.val]! : -1
            let rightH = n.right != nil ? height[n.right!.val]! : -1
            
            if let leftNode = n.left {
                var viaSibling = -1
                if rightH != -1 {
                    // depth of parent + edge to sibling + height down sibling
                    viaSibling = depth + 1 + rightH
                }
                // ancestors (including the parent itself) can be the deepest leaf after removal
                let fromAncestors = max(upDist, depth)
                let newUp = max(fromAncestors, viaSibling)
                dfsPass(leftNode, depth + 1, newUp)
            }
            
            if let rightNode = n.right {
                var viaSibling = -1
                if leftH != -1 {
                    viaSibling = depth + 1 + leftH
                }
                let fromAncestors = max(upDist, depth)
                let newUp = max(fromAncestors, viaSibling)
                dfsPass(rightNode, depth + 1, newUp)
            }
        }
        
        // root has no nodes outside its subtree, use -1 as sentinel
        dfsPass(root, 0, -1)
        
        var result = [Int]()
        for q in queries {
            if let val = answer[q] {
                result.append(val)
            } else {
                result.append(0)   // should not happen per constraints
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
/****
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun treeQueries(root: TreeNode?, queries: IntArray): IntArray {
        if (root == null) return IntArray(0)

        // First pass to find maximum node value (n)
        var maxVal = 0
        fun dfsFind(node: TreeNode?) {
            if (node == null) return
            if (node.`val` > maxVal) maxVal = node.`val`
            dfsFind(node.left)
            dfsFind(node.right)
        }
        dfsFind(root)

        val n = maxVal
        val down = IntArray(n + 1) { -1 }   // height of subtree rooted at i
        val up = IntArray(n + 1) { -2 }     // height from root to deepest leaf not in subtree i

        // Compute down heights (post-order)
        fun dfsDown(node: TreeNode?) {
            if (node == null) return
            dfsDown(node.left)
            dfsDown(node.right)
            val leftH = node.left?.let { down[it.`val`] } ?: -1
            val rightH = node.right?.let { down[it.`val`] } ?: -1
            down[node.`val`] = maxOf(leftH, rightH) + 1
        }
        dfsDown(root)

        // Compute up heights (pre-order)
        up[root!!.`val`] = -1   // root has no ancestors
        fun dfsUp(node: TreeNode?) {
            if (node == null) return
            val v = node.`val`

            node.left?.let { left ->
                var best = up[v]
                val siblingHeight = node.right?.let { down[it.`val`] } ?: -1
                best = maxOf(best, siblingHeight)
                up[left.`val`] = best + 1
                dfsUp(left)
            }

            node.right?.let { right ->
                var best = up[v]
                val siblingHeight = node.left?.let { down[it.`val`] } ?: -1
                best = maxOf(best, siblingHeight)
                up[right.`val`] = best + 1
                dfsUp(right)
            }
        }
        dfsUp(root)

        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            ans[i] = up[queries[i]]
        }
        return ans
    }
}
```

## Dart

```dart
/ **
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  List<int> treeQueries(TreeNode? root, List<int> queries) {
    if (root == null) return [];

    // Find maximum node value to size arrays.
    int maxVal = 0;
    List<TreeNode> stack = [root];
    while (stack.isNotEmpty) {
      TreeNode node = stack.removeLast();
      if (node.val > maxVal) maxVal = node.val;
      if (node.left != null) stack.add(node.left!);
      if (node.right != null) stack.add(node.right!);
    }

    int size = maxVal + 1;
    List<int> depth = List.filled(size, 0);
    List<int> height = List.filled(size, -1);
    List<int> answer = List.filled(size, -1);

    // Compute depths (preorder).
    List<List<dynamic>> stDepth = [
      [root, 0]
    ];
    while (stDepth.isNotEmpty) {
      var pair = stDepth.removeLast();
      TreeNode node = pair[0];
      int d = pair[1];
      depth[node.val] = d;
      if (node.left != null) stDepth.add([node.left!, d + 1]);
      if (node.right != null) stDepth.add([node.right!, d + 1]);
    }

    // Compute heights using postorder via order list.
    List<TreeNode> order = [];
    List<TreeNode> stOrder = [root];
    while (stOrder.isNotEmpty) {
      TreeNode node = stOrder.removeLast();
      order.add(node);
      if (node.left != null) stOrder.add(node.left!);
      if (node.right != null) stOrder.add(node.right!);
    }
    for (int i = order.length - 1; i >= 0; --i) {
      TreeNode node = order[i];
      int leftH = node.left != null ? height[node.left!.val] : -1;
      int rightH = node.right != null ? height[node.right!.val] : -1;
      height[node.val] = 1 + (leftH > rightH ? leftH : rightH);
    }

    // Propagate the best height from outside each subtree.
    List<List<dynamic>> stAns = [
      [root, -1]
    ];
    while (stAns.isNotEmpty) {
      var pair = stAns.removeLast();
      TreeNode node = pair[0];
      int up = pair[1];
      answer[node.val] = up;

      if (node.left != null) {
        int siblingHeight =
            node.right != null ? height[node.right!.val] : -1;
        int cand = siblingHeight >= 0
            ? depth[node.val] + 1 + siblingHeight
            : -1;
        int childUp = up > cand ? up : cand;
        stAns.add([node.left!, childUp]);
      }
      if (node.right != null) {
        int siblingHeight =
            node.left != null ? height[node.left!.val] : -1;
        int cand = siblingHeight >= 0
            ? depth[node.val] + 1 + siblingHeight
            : -1;
        int childUp = up > cand ? up : cand;
        stAns.add([node.right!, childUp]);
      }
    }

    List<int> res = [];
    for (int q in queries) {
      res.add(answer[q]);
    }
    return res;
  }
}
```

## Golang

```go
/ **
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 * /
func treeQueries(root *TreeNode, queries []int) []int {
    // maps to store depth, height of subtree and answer (up value)
    depth := make(map[int]int)
    height := make(map[int]int)
    up := make(map[int]int)

    var dfsHeight func(node *TreeNode) int
    dfsHeight = func(node *TreeNode) int {
        if node == nil {
            return -1 // so leaf gets height 0
        }
        lh := dfsHeight(node.Left)
        rh := dfsHeight(node.Right)
        h := max(lh, rh) + 1
        height[node.Val] = h
        return h
    }

    var dfsDepth func(node *TreeNode, d int)
    dfsDepth = func(node *TreeNode, d int) {
        if node == nil {
            return
        }
        depth[node.Val] = d
        dfsDepth(node.Left, d+1)
        dfsDepth(node.Right, d+1)
    }

    var dfsUp func(node *TreeNode)
    dfsUp = func(node *TreeNode) {
        if node == nil {
            return
        }
        // best candidate from ancestors (including the parent itself)
        base := up[node.Val]
        if depth[node.Val] > base {
            base = depth[node.Val]
        }

        if node.Left != nil {
            siblingBest := -1
            if node.Right != nil {
                siblingBest = depth[node.Val] + 1 + height[node.Right.Val]
            }
            childUp := base
            if siblingBest > childUp {
                childUp = siblingBest
            }
            up[node.Left.Val] = childUp
            dfsUp(node.Left)
        }

        if node.Right != nil {
            siblingBest := -1
            if node.Left != nil {
                siblingBest = depth[node.Val] + 1 + height[node.Left.Val]
            }
            childUp := base
            if siblingBest > childUp {
                childUp = siblingBest
            }
            up[node.Right.Val] = childUp
            dfsUp(node.Right)
        }
    }

    // compute heights and depths
    dfsHeight(root)
    dfsDepth(root, 0)

    // root has no nodes outside its subtree
    up[root.Val] = -1
    dfsUp(root)

    ans := make([]int, len(queries))
    for i, v := range queries {
        ans[i] = up[v]
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#   attr_accessor :val, :left, :right
#   def initialize(val = 0, left = nil, right = nil)
#     @val = val
#     @left = left
#     @right = right
#   end
# end

def tree_queries(root, queries)
  return [] unless root

  start_idx = {}
  depths = []
  order = []
  parent = {}

  stack = [[root, 0]]
  idx = 0
  while !stack.empty?
    node, d = stack.pop
    start_idx[node.val] = idx
    depths << d
    order << node.val
    idx += 1

    if node.right
      parent[node.right.val] = node.val
      stack << [node.right, d + 1]
    end
    if node.left
      parent[node.left.val] = node.val
      stack << [node.left, d + 1]
    end
  end

  size = Hash.new(0)
  order.reverse_each do |v|
    size[v] += 1
    p = parent[v]
    size[p] += size[v] if p
  end

  n = depths.size
  pref_max = Array.new(n, -1)
  cur = -1
  depths.each_with_index do |d, i|
    cur = d if d > cur
    pref_max[i] = cur
  end

  suff_max = Array.new(n, -1)
  cur = -1
  (n - 1).downto(0) do |i|
    d = depths[i]
    cur = d if d > cur
    suff_max[i] = cur
  end

  result = []
  queries.each do |v|
    l = start_idx[v]
    r = l + size[v] - 1
    left_best = l > 0 ? pref_max[l - 1] : -1
    right_best = r + 1 < n ? suff_max[r + 1] : -1
    result << (left_best > right_best ? left_best : right_best)
  end

  result
end
```

## Scala

```scala
/****
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def treeQueries(root: TreeNode, queries: Array[Int]): Array[Int] = {
    // constraints guarantee node values are in [1, n] with n <= 100000
    val maxSize = 100005
    val depth = new Array[Int](maxSize)
    val subHeight = new Array[Int](maxSize)   // height of subtree rooted at node (edges to deepest leaf)
    val best1 = new Array[Int](maxSize)       // largest child subtree height
    val best2 = new Array[Int](maxSize)       // second largest child subtree height

    def dfs(node: TreeNode, d: Int): Unit = {
      if (node == null) return
      depth(node.value) = d
      var leftH = -1
      var rightH = -1
      if (node.left != null) {
        dfs(node.left, d + 1)
        leftH = subHeight(node.left.value)
      }
      if (node.right != null) {
        dfs(node.right, d + 1)
        rightH = subHeight(node.right.value)
      }
      val maxChild = Math.max(leftH, rightH)
      subHeight(node.value) = if (maxChild == -1) 0 else maxChild + 1

      var first = -1
      var second = -1
      def consider(v: Int): Unit = {
        if (v > first) { second = first; first = v }
        else if (v > second) { second = v }
      }
      if (leftH != -1) consider(leftH)
      if (rightH != -1) consider(rightH)
      best1(node.value) = first
      best2(node.value) = second
    }

    dfs(root, 0)

    val answer = new Array[Int](maxSize)

    def dfs2(node: TreeNode, upVal: Int): Unit = {
      if (node == null) return
      answer(node.value) = upVal

      // process left child
      if (node.left != null) {
        val child = node.left
        var siblingBest = best1(node.value)
        val childSub = subHeight(child.value)
        if (siblingBest == childSub) siblingBest = best2(node.value)

        var cand = upVal
        if (siblingBest != -1) {
          val candidate = depth(child.value) + siblingBest
          if (candidate > cand) cand = candidate
        }
        dfs2(child, cand)
      }

      // process right child
      if (node.right != null) {
        val child = node.right
        var siblingBest = best1(node.value)
        val childSub = subHeight(child.value)
        if (siblingBest == childSub) siblingBest = best2(node.value)

        var cand = upVal
        if (siblingBest != -1) {
          val candidate = depth(child.value) + siblingBest
          if (candidate > cand) cand = candidate
        }
        dfs2(child, cand)
      }
    }

    dfs2(root, 0)

    queries.map(q => answer(q))
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
    pub fn tree_queries(root: Option<Rc<RefCell<TreeNode>>>, queries: Vec<i32>) -> Vec<i32> {
        // Helper DFS to record preorder depths, entry indices and subtree sizes.
        fn dfs(
            node: Rc<RefCell<TreeNode>>,
            depth: i32,
            order: &mut Vec<i32>,
            tin: &mut HashMap<i32, usize>,
            sz: &mut HashMap<i32, usize>,
        ) -> usize {
            let val = node.borrow().val;
            tin.insert(val, order.len());
            order.push(depth);
            let left_sz = if let Some(left) = node.borrow().left.clone() {
                dfs(left, depth + 1, order, tin, sz)
            } else {
                0
            };
            let right_sz = if let Some(right) = node.borrow().right.clone() {
                dfs(right, depth + 1, order, tin, sz)
            } else {
                0
            };
            let total = 1 + left_sz + right_sz;
            sz.insert(val, total);
            total
        }

        // Empty tree edge case (should not happen per constraints).
        if root.is_none() {
            return vec![];
        }

        let mut order: Vec<i32> = Vec::new();          // depths in preorder
        let mut tin: HashMap<i32, usize> = HashMap::new(); // node value -> entry index
        let mut sz: HashMap<i32, usize> = HashMap::new();  // node value -> subtree size

        dfs(root.unwrap(), 0, &mut order, &mut tin, &mut sz);

        let n = order.len();
        // Prefix maximum depths.
        let mut pref = vec![i32::MIN; n];
        for i in 0..n {
            if i == 0 {
                pref[i] = order[i];
            } else {
                pref[i] = pref[i - 1].max(order[i]);
            }
        }
        // Suffix maximum depths.
        let mut suff = vec![i32::MIN; n];
        for i in (0..n).rev() {
            if i == n - 1 {
                suff[i] = order[i];
            } else {
                suff[i] = suff[i + 1].max(order[i]);
            }
        }

        let mut ans: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries {
            let start = *tin.get(&q).unwrap();
            let size_sub = *sz.get(&q).unwrap();
            let end = start + size_sub - 1;

            let left_max = if start == 0 { i32::MIN } else { pref[start - 1] };
            let right_max = if end + 1 >= n { i32::MIN } else { suff[end + 1] };

            ans.push(left_max.max(right_max));
        }

        ans
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

(define/contract (tree-queries root queries)
  (-> (or/c tree-node? #f) (listof exact-integer?) (listof exact-integer?))
  (if (not root)
      (make-list (length queries) 0)
      (let ((heights (make-hash))   ; node val -> height (edges)
            (upVals (make-hash)))   ; node val -> answer after removal
        (define (post-order node)
          (if (not node)
              -1
              (let* ((lh (post-order (tree-node-left node)))
                     (rh (post-order (tree-node-right node)))
                     (h (+ 1 (max lh rh))))
                (hash-set! heights (tree-node-val node) h)
                h)))
        (define (top-down node depth up)
          (when node
            (let ((val (tree-node-val node))
                  (left (tree-node-left node))
                  (right (tree-node-right node)))
              (hash-set! upVals val up)
              (let* ((lh (if left (hash-ref heights (tree-node-val left) -1) -1))
                     (rh (if right (hash-ref heights (tree-node-val right) -1) -1)))
                (when left
                  (let* ((siblingHeight rh)
                         (candidate (if (= siblingHeight -1)
                                        depth
                                        (+ depth 1 siblingHeight)))
                         (childUp (max up candidate)))
                    (top-down left (+ depth 1) childUp)))
                (when right
                  (let* ((siblingHeight lh)
                         (candidate (if (= siblingHeight -1)
                                        depth
                                        (+ depth 1 siblingHeight)))
                         (childUp (max up candidate)))
                    (top-down right (+ depth 1) childUp)))))))
        (post-order root)
        (top-down root 0 -1)
        (map (lambda (q) (hash-ref upVals q -1)) queries))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec tree_queries(Root :: #tree_node{} | null, Queries :: [integer()]) -> [integer()].
tree_queries(null, _Queries) ->
    [];
tree_queries(Root, Queries) ->
    % DFS to compute depth, subtree height and per‑depth top two values
    {_, NodeDepthMap, NodeHeightMap, FirstMap, SecondMap, MaxDepth} =
        dfs(Root, 0,
            #{},   % node -> depth
            #{},   % node -> height
            #{},   % depth -> first max (depth+height)
            #{},   % depth -> second max
            -1),   % current maximum depth

    % Build arrays (lists) for depths 0..MaxDepth
    Depths = lists:seq(0, MaxDepth),
    FirstVals  = [maps:get(D, FirstMap, -1)  || D <- Depths],
    SecondVals = [maps:get(D, SecondMap, -1) || D <- Depths],

    % Prefix max of first values
    {PrefixList, _} =
        lists:mapfoldl(fun(Val, Prev) ->
                           New = erlang:max(Prev, Val),
                           {New, New}
                       end,
                       -1,
                       FirstVals),

    % Suffix max of first values
    RevFirstVals = lists:reverse(FirstVals),
    {RevSuffixList, _} =
        lists:mapfoldl(fun(Val, Prev) ->
                           New = erlang:max(Prev, Val),
                           {New, New}
                       end,
                       -1,
                       RevFirstVals),
    SuffixList = lists:reverse(RevSuffixList),

    % Convert prefix/suffix to maps for O(1) access
    PrefixMap = maps:from_list(lists:zip(Depths, PrefixList)),
    SuffixMap = maps:from_list(lists:zip(Depths, SuffixList)),

    % Answer each query
    lists:map(
      fun(Q) ->
          D   = maps:get(Q, NodeDepthMap),
          H   = maps:get(Q, NodeHeightMap),
          Val = D + H,
          First  = maps:get(D, FirstMap, -1),
          Second = maps:get(D, SecondMap, -1),

          Candidate = if Val == First -> Second; true -> First end,

          LeftMax  = if D > 0      -> maps:get(D-1, PrefixMap, -1);
                       true       -> -1
                    end,
          RightMax = if D < MaxDepth -> maps:get(D+1, SuffixMap, -1);
                        true        -> -1
                     end,
          MaxOther = erlang:max(LeftMax, RightMax),

          erlang:max(Candidate, MaxOther)
      end,
      Queries).

% -------------------------------------------------------------------
% dfs(Node, Depth, NodeDepthMap, NodeHeightMap, FirstMap, SecondMap, MaxDepth) ->
%   returns {Height, UpdatedNodeDepthMap, UpdatedNodeHeightMap,
%            UpdatedFirstMap, UpdatedSecondMap, UpdatedMaxDepth}
% -------------------------------------------------------------------
dfs(null, _Depth, ND, NH, FM, SM, MD) ->
    {-1, ND, NH, FM, SM, MD};
dfs(Node, Depth, ND, NH, FM, SM, MD) ->
    Val   = Node#tree_node.val,
    Left  = Node#tree_node.left,
    Right = Node#tree_node.right,

    {LH, ND1, NH1, FM1, SM1, MD1} = dfs(Left, Depth+1, ND, NH, FM, SM, MD),
    {RH, ND2, NH2, FM2, SM2, MD2} = dfs(Right, Depth+1, ND1, NH1, FM1, SM1, MD1),

    H = erlang:max(LH, RH) + 1,
    ND3 = maps:put(Val, Depth, ND2),
    NH3 = maps:put(Val, H,     NH2),

    Sum = Depth + H,
    {First, Second} =
        case maps:find(Depth, FM2) of
            error -> {-1, -1};
            {ok, F} -> {F, maps:get(Depth, SM2)}
        end,

    {NewFirst, NewSecond} =
        if Sum > First ->
                {Sum, First};
           Sum > Second ->
                {First, Sum};
           true ->
                {First, Second}
        end,

    FM3 = maps:put(Depth, NewFirst,  FM2),
    SM3 = maps:put(Depth, NewSecond, SM2),

    NewMD = if Depth > MD2 -> Depth; true -> MD2 end,
    {H, ND3, NH3, FM3, SM3, NewMD}.
```

## Elixir

```elixir
defmodule Solution do
  @spec tree_queries(root :: TreeNode.t | nil, queries :: [integer]) :: [integer]
  def tree_queries(root, queries) do
    {depth_map, down_map} = compute_maps(root)
    ans_map = compute_answers(root, depth_map, down_map)

    Enum.map(queries, fn q -> Map.get(ans_map, q) end)
  end

  # Compute depth (distance from root) and down (height of subtree) for each node.
  defp compute_maps(nil), do: {%{}, %{}}
  defp compute_maps(root) do
    depth = %{root.val => 0}
    down = %{}
    stack = [{root, false}]

    {final_depth, final_down} = postorder_loop(stack, depth, down)
    {final_depth, final_down}
  end

  defp postorder_loop([], depth, down), do: {depth, down}

  defp postorder_loop([{nil, _} | rest], depth, down) do
    postorder_loop(rest, depth, down)
  end

  defp postorder_loop([{node, visited} | rest], depth, down) do
    if visited do
      left_down =
        case node.left do
          nil -> -1
          l -> Map.get(down, l.val)
        end

      right_down =
        case node.right do
          nil -> -1
          r -> Map.get(down, r.val)
        end

      d = max(left_down, right_down) + 1
      down2 = Map.put(down, node.val, d)
      postorder_loop(rest, depth, down2)
    else
      # push node back as visited
      stack = [{node, true} | rest]

      # process right child first (order doesn't matter)
      {depth_r, stack_r} =
        case node.right do
          nil -> {depth, stack}
          r ->
            d = Map.get(depth, node.val) + 1
            {Map.put(depth, r.val, d), [{r, false} | stack]}
        end

      # then left child
      {depth_l, stack_l} =
        case node.left do
          nil -> {depth_r, stack_r}
          l ->
            d = Map.get(depth_r, node.val) + 1
            {Map.put(depth_r, l.val, d), [{l, false} | stack_r]}
        end

      postorder_loop(stack_l, depth_l, down)
    end
  end

  # Compute answer for each node: height after removing its subtree.
  defp compute_answers(nil, _depth_map, _down_map), do: %{}
  defp compute_answers(root, depth_map, down_map) do
    ans = %{}
    stack = [{root, -1}]
    compute_loop(stack, depth_map, down_map, ans)
  end

  defp compute_loop([], _depth, _down, ans), do: ans

  defp compute_loop([{nil, _} | rest], depth, down, ans) do
    compute_loop(rest, depth, down, ans)
  end

  defp compute_loop([{node, from_parent} | rest], depth, down, ans) do
    # store answer (ensure non‑negative)
    ans2 = Map.put(ans, node.val, max(from_parent, 0))

    left = node.left
    right = node.right
    depth_node = Map.get(depth, node.val)

    left_sib_down =
      case right do
        nil -> -1
        r -> Map.get(down, r.val)
      end

    right_sib_down =
      case left do
        nil -> -1
        l -> Map.get(down, l.val)
      end

    stack2 = rest

    # push left child if exists
    stack2 =
      if left != nil do
        candidate = depth_node + 1 + left_sib_down
        child_from = max(from_parent, candidate)
        [{left, child_from} | stack2]
      else
        stack2
      end

    # push right child if exists
    stack2 =
      if right != nil do
        candidate = depth_node + 1 + right_sib_down
        child_from = max(from_parent, candidate)
        [{right, child_from} | stack2]
      else
        stack2
      end

    compute_loop(stack2, depth, down, ans2)
  end
end
```
