# 1932. Merge BSTs to Create Single BST

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
    unordered_map<int, TreeNode*> mp;
    
    bool dfs(TreeNode* node, long long low, long long high) {
        if (!node) return true;
        if (node->val <= low || node->val >= high) return false;
        // leaf that can be merged
        if (!node->left && !node->right) {
            auto it = mp.find(node->val);
            if (it != mp.end()) {
                TreeNode* sub = it->second;
                // attach its children
                node->left = sub->left;
                node->right = sub->right;
                mp.erase(it);
            }
        }
        return dfs(node->left, low, node->val) && dfs(node->right, node->val, high);
    }
    
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        mp.clear();
        unordered_set<int> leafVals;
        for (TreeNode* t : trees) {
            mp[t->val] = t;
            if (t->left) leafVals.insert(t->left->val);
            if (t->right) leafVals.insert(t->right->val);
        }
        // find unique root not appearing as any leaf
        TreeNode* candidate = nullptr;
        for (TreeNode* t : trees) {
            if (!leafVals.count(t->val)) {
                if (candidate) return nullptr; // more than one possible root
                candidate = t;
            }
        }
        if (!candidate) return nullptr;
        // remove candidate from map to avoid self-merge
        mp.erase(candidate->val);
        if (!dfs(candidate, LLONG_MIN, LLONG_MAX)) return nullptr;
        // all trees must be merged
        if (!mp.empty()) return nullptr;
        return candidate;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public TreeNode canMerge(List<TreeNode> trees) {
        Map<Integer, TreeNode> rootMap = new HashMap<>();
        Set<Integer> leafVals = new HashSet<>();

        for (TreeNode t : trees) {
            rootMap.put(t.val, t);
            if (t.left != null) leafVals.add(t.left.val);
            if (t.right != null) leafVals.add(t.right.val);
        }

        TreeNode root = null;
        int candidates = 0;
        for (TreeNode t : trees) {
            if (!leafVals.contains(t.val)) {
                root = t;
                candidates++;
            }
        }
        if (candidates != 1) return null;

        // remove the chosen root from map; it should not be merged into another tree
        rootMap.remove(root.val);

        boolean[] ok = new boolean[]{true};
        TreeNode mergedRoot = dfs(root, Long.MIN_VALUE, Long.MAX_VALUE, rootMap, ok);
        if (!ok[0] || !rootMap.isEmpty()) return null;
        return mergedRoot;
    }

    private TreeNode dfs(TreeNode node, long min, long max,
                         Map<Integer, TreeNode> map, boolean[] ok) {
        if (node == null) return null;
        if (node.val <= min || node.val >= max) {
            ok[0] = false;
            return null;
        }

        // If this node is a leaf and there exists another tree with the same root value,
        // merge that tree here.
        if (node.left == null && node.right == null && map.containsKey(node.val)) {
            TreeNode mergeTree = map.get(node.val);
            map.remove(node.val);
            node = new TreeNode(mergeTree.val, mergeTree.left, mergeTree.right);
        }

        node.left = dfs(node.left, min, node.val, map, ok);
        node.right = dfs(node.right, node.val, max, map, ok);
        return node;
    }
}

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
```

## Python

```python
import sys

sys.setrecursionlimit(10 ** 6)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """
        # map root value -> tree node
        roots = {tree.val: tree for tree in trees}
        leaf_vals = set()
        for tree in trees:
            if tree.left:
                leaf_vals.add(tree.left.val)
            if tree.right:
                leaf_vals.add(tree.right.val)

        # candidate final root: a root whose value never appears as a leaf
        candidates = [val for val in roots if val not in leaf_vals]
        if len(candidates) != 1:
            return None

        root_val = candidates[0]
        root = roots.pop(root_val)

        def dfs(node, low, high):
            if not node:
                return None
            if not (low < node.val < high):
                raise ValueError
            # if leaf and can be merged
            if node.left is None and node.right is None and node.val in roots:
                node = roots.pop(node.val)
            node.left = dfs(node.left, low, node.val)
            node.right = dfs(node.right, node.val, high)
            return node

        try:
            root = dfs(root, -float('inf'), float('inf'))
        except ValueError:
            return None

        if roots:  # some trees couldn't be merged
            return None
        return root
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
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # map root value to its tree node
        roots = {tree.val: tree for tree in trees}
        leaf_vals = set()
        for tree in trees:
            if tree.left:
                leaf_vals.add(tree.left.val)
            if tree.right:
                leaf_vals.add(tree.right.val)

        # find the unique final root (not appearing as any leaf)
        candidates = [val for val in roots if val not in leaf_vals]
        if len(candidates) != 1:
            return None
        final_root_val = candidates[0]
        root = roots.pop(final_root_val)

        # merge recursively
        def dfs(node: TreeNode) -> bool:
            if not node:
                return True
            # left child
            if node.left:
                lv = node.left.val
                if lv in roots:
                    subtree = roots.pop(lv)
                    node.left = subtree
                if not dfs(node.left):
                    return False
            # right child
            if node.right:
                rv = node.right.val
                if rv in roots:
                    subtree = roots.pop(rv)
                    node.right = subtree
                if not dfs(node.right):
                    return False
            return True

        if not dfs(root):
            return None
        if roots:  # some trees couldn't be merged
            return None

        # validate BST property using bounds
        def is_valid(node: TreeNode, low: int, high: int) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)

        return root if is_valid(root, float('-inf'), float('inf')) else None
```

## C

```c
/****
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#include <stddef.h>
#include <string.h>
#include <limits.h>

#define MAXV 50000

static struct TreeNode* rootMap[MAXV + 1];
static int cntVals[MAXV + 1];

/* forward declaration */
static int dfsMerge(struct TreeNode **pnode, long long low, long long high);

struct TreeNode* canMerge(struct TreeNode** trees, int treesSize){
    if (treesSize == 0) return NULL;

    memset(rootMap, 0, sizeof(rootMap));
    memset(cntVals, 0, sizeof(cntVals));

    /* record roots and count occurrences of every value */
    for (int i = 0; i < treesSize; ++i) {
        struct TreeNode *root = trees[i];
        rootMap[root->val] = root;
        cntVals[root->val]++;

        if (root->left) {
            cntVals[root->left->val]++;
        }
        if (root->right) {
            cntVals[root->right->val]++;
        }
    }

    /* find the unique final root (value appears only once) */
    struct TreeNode *finalRoot = NULL;
    int candidates = 0;
    for (int i = 0; i < treesSize; ++i) {
        if (cntVals[trees[i]->val] == 1) {
            finalRoot = trees[i];
            ++candidates;
        }
    }
    if (candidates != 1) return NULL;

    /* mark the chosen root as used */
    rootMap[finalRoot->val] = NULL;

    /* merge recursively while validating BST property */
    if (!dfsMerge(&finalRoot, LLONG_MIN, LLONG_MAX)) return NULL;

    /* ensure all other roots have been merged */
    for (int i = 0; i < treesSize; ++i) {
        if (rootMap[trees[i]->val] != NULL) return NULL;
    }

    return finalRoot;
}

/* Recursive merge and BST validation.
   Returns 1 if subtree rooted at *pnode is a valid BST after merges,
   otherwise returns 0. */
static int dfsMerge(struct TreeNode **pnode, long long low, long long high){
    struct TreeNode *node = *pnode;
    if (!node) return 1;

    int v = node->val;
    if (v <= low || v >= high) return 0;

    /* If leaf and there exists an unused tree whose root matches this value,
       replace the leaf with that whole subtree. */
    if (!node->left && !node->right) {
        struct TreeNode *other = rootMap[v];
        if (other != NULL) {               /* found a tree to merge */
            rootMap[v] = NULL;              /* mark as used */
            *pnode = other;                 /* replace leaf with the subtree */
            node = other;
            v = node->val;                  /* same value, bounds unchanged */
        }
    }

    return dfsMerge(&(node->left), low, v) && dfsMerge(&(node->right), v, high);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public TreeNode CanMerge(IList<TreeNode> trees) {
        int n = trees.Count;
        var rootMap = new Dictionary<int, TreeNode>();
        var leafVals = new HashSet<int>();
        long totalNodes = 0;

        foreach (var root in trees) {
            rootMap[root.val] = root;
            if (root.left != null) leafVals.Add(root.left.val);
            if (root.right != null) leafVals.Add(root.right.val);

            // count nodes (each tree has at most 3 nodes)
            var stack = new Stack<TreeNode>();
            stack.Push(root);
            while (stack.Count > 0) {
                var node = stack.Pop();
                totalNodes++;
                if (node.left != null) stack.Push(node.left);
                if (node.right != null) stack.Push(node.right);
            }
        }

        // find the unique root that is not a leaf value
        int candidateRootVal = -1;
        int candidates = 0;
        foreach (var kv in rootMap) {
            if (!leafVals.Contains(kv.Key)) {
                candidateRootVal = kv.Key;
                candidates++;
            }
        }
        if (candidates != 1) return null;

        // start merging from the chosen root
        TreeNode finalRoot = rootMap[candidateRootVal];
        rootMap.Remove(candidateRootVal);

        finalRoot = Merge(finalRoot, rootMap);
        if (rootMap.Count > 0) return null; // some trees couldn't be merged

        // validate BST and node count
        long prev = long.MinValue;
        int visited = 0;
        var st = new Stack<TreeNode>();
        TreeNode cur = finalRoot;
        while (st.Count > 0 || cur != null) {
            while (cur != null) {
                st.Push(cur);
                cur = cur.left;
            }
            cur = st.Pop();
            if (cur.val <= prev) return null;
            prev = cur.val;
            visited++;
            cur = cur.right;
        }

        return visited == totalNodes ? finalRoot : null;
    }

    private TreeNode Merge(TreeNode node, Dictionary<int, TreeNode> map) {
        if (node == null) return null;

        // If leaf and there exists a tree with same root value
        if (node.left == null && node.right == null && map.TryGetValue(node.val, out var sub)) {
            map.Remove(node.val);
            sub.left = Merge(sub.left, map);
            sub.right = Merge(sub.right, map);
            return sub;
        }

        node.left = Merge(node.left, map);
        node.right = Merge(node.right, map);
        return node;
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
 * @param {TreeNode[]} trees
 * @return {TreeNode}
 */
var canMerge = function(trees) {
    const rootMap = new Map(); // val -> root node
    const leafVals = new Set();

    for (const t of trees) {
        rootMap.set(t.val, t);
        if (t.left) leafVals.add(t.left.val);
        if (t.right) leafVals.add(t.right.val);
    }

    // find the unique root that is not a leaf in any other tree
    let finalRoot = null;
    for (const t of trees) {
        if (!leafVals.has(t.val)) {
            if (finalRoot) return null; // more than one candidate
            finalRoot = t;
        }
    }
    if (!finalRoot) return null;

    // remove the chosen root from map so it won't be merged into itself
    rootMap.delete(finalRoot.val);

    const dfs = (node, low, high) => {
        if (!node) return true;
        if (node.val <= low || node.val >= high) return false;

        // If leaf and its value matches a remaining root, merge it
        if (!node.left && !node.right && rootMap.has(node.val)) {
            const sub = rootMap.get(node.val);
            node.left = sub.left;
            node.right = sub.right;
            rootMap.delete(node.val);
        }

        return dfs(node.left, low, node.val) && dfs(node.right, node.val, high);
    };

    if (!dfs(finalRoot, -Infinity, Infinity)) return null;
    // all other trees must have been merged
    if (rootMap.size !== 0) return null;

    return finalRoot;
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

function canMerge(trees: Array<TreeNode | null>): TreeNode | null {
    const rootMap = new Map<number, TreeNode>();
    const leafCount = new Map<number, number>();

    // map each tree's root
    for (const t of trees) {
        if (t) rootMap.set(t.val, t);
    }

    // count leaf occurrences
    for (const t of trees) {
        if (!t) continue;
        if (t.left) {
            leafCount.set(t.left.val, (leafCount.get(t.left.val) ?? 0) + 1);
        }
        if (t.right) {
            leafCount.set(t.right.val, (leafCount.get(t.right.val) ?? 0) + 1);
        }
    }

    // early impossible check: a root appearing as leaf more than once
    for (const [val, cnt] of leafCount.entries()) {
        if (cnt > 1 && rootMap.has(val)) return null;
    }

    // find the unique root that is not any leaf
    let finalRoot: TreeNode | null = null;
    for (const [val, node] of rootMap.entries()) {
        if (!leafCount.has(val)) {
            if (finalRoot) return null; // more than one candidate
            finalRoot = node;
        }
    }
    if (!finalRoot) return null;

    const attachSubtree = (parent: TreeNode, side: 'left' | 'right') => {
        const child = parent[side];
        if (child && rootMap.has(child.val)) {
            const sub = rootMap.get(child.val)!;
            parent[side] = sub;
            rootMap.delete(sub.val);
        }
    };

    const dfs = (node: TreeNode | null, low: number, high: number): boolean => {
        if (!node) return true;
        if (node.val <= low || node.val >= high) return false;

        // merge possible subtrees at current leaves
        attachSubtree(node, 'left');
        attachSubtree(node, 'right');

        return dfs(node.left, low, node.val) && dfs(node.right, node.val, high);
    };

    const valid = dfs(finalRoot, -Infinity, Infinity);
    if (!valid || rootMap.size > 0) return null;
    return finalRoot;
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
     * @param TreeNode[] $trees
     * @return TreeNode|null
     */
    function canMerge($trees) {
        // Map root value to its tree node
        $rootMap = [];
        foreach ($trees as $t) {
            $rootMap[$t->val] = $t;
        }

        // Count occurrences of leaf values across all trees
        $leafCount = [];
        foreach ($trees as $t) {
            if ($t->left !== null) {
                $leafCount[$t->left->val] = ($leafCount[$t->left->val] ?? 0) + 1;
            }
            if ($t->right !== null) {
                $leafCount[$t->right->val] = ($leafCount[$t->right->val] ?? 0) + 1;
            }
        }

        // Find the root that does not appear as any leaf
        $candidateRoot = null;
        foreach ($trees as $t) {
            if (!isset($leafCount[$t->val])) {
                $candidateRoot = $t;
                break;
            }
        }

        if ($candidateRoot === null) {
            return null;
        }

        // Remove the chosen root from map to avoid merging it into itself
        unset($rootMap[$candidateRoot->val]);

        // Depth‑first validation and merging with bounds
        $dfs = function($node, $low, $high) use (&$dfs, &$rootMap) {
            if ($node === null) {
                return true;
            }
            $val = $node->val;
            if ($val <= $low || $val >= $high) {
                return false;
            }

            // If leaf matches another tree's root, merge it
            if ($node->left === null && $node->right === null && isset($rootMap[$val])) {
                $sub = $rootMap[$val];
                unset($rootMap[$val]);
                $node->left  = $sub->left;
                $node->right = $sub->right;
            }

            return $dfs($node->left, $low, $val) && $dfs($node->right, $val, $high);
        };

        $valid = $dfs($candidateRoot, PHP_INT_MIN, PHP_INT_MAX);

        // All trees must be merged and the final structure must be a BST
        if ($valid && empty($rootMap)) {
            return $candidateRoot;
        }
        return null;
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
    func canMerge(_ trees: [TreeNode?]) -> TreeNode? {
        var rootMap = [Int: TreeNode]()
        var leafCount = [Int: Int]()
        var roots = [TreeNode]()
        
        // Collect roots and leaf occurrences
        for opt in trees {
            guard let node = opt else { continue }
            roots.append(node)
            rootMap[node.val] = node
            if let l = node.left {
                leafCount[l.val, default: 0] += 1
            }
            if let r = node.right {
                leafCount[r.val, default: 0] += 1
            }
        }
        
        // Find the unique root that never appears as a leaf
        var finalRoot: TreeNode? = nil
        for r in roots {
            if leafCount[r.val] == nil {
                if finalRoot != nil { return nil } // multiple candidates
                finalRoot = r
            }
        }
        guard let root = finalRoot else { return nil }
        
        // Remove the chosen final root from map so we only merge others
        rootMap.removeValue(forKey: root.val)
        
        // Recursive DFS to validate BST property and perform merges
        func dfs(_ node: TreeNode?, _ low: Int, _ high: Int) -> Bool {
            guard let n = node else { return true }
            if n.val <= low || n.val >= high { return false }
            
            // If leaf, try to merge a tree whose root matches this value
            if n.left == nil && n.right == nil {
                if let sub = rootMap[n.val] {
                    n.left = sub.left
                    n.right = sub.right
                    rootMap.removeValue(forKey: n.val)
                }
            }
            
            return dfs(n.left, low, n.val) && dfs(n.right, n.val, high)
        }
        
        if !dfs(root, Int.min, Int.max) { return nil }
        // All other trees must have been merged
        return rootMap.isEmpty ? root : nil
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
    fun canMerge(trees: List<TreeNode?>): TreeNode? {
        val rootMap = HashMap<Int, TreeNode>()
        val leafCount = HashMap<Int, Int>()

        for (t in trees) {
            if (t == null) continue
            rootMap[t.`val`] = t
            t.left?.let { leafCount[it.`val`] = leafCount.getOrDefault(it.`val`, 0) + 1 }
            t.right?.let { leafCount[it.`val`] = leafCount.getOrDefault(it.`val`, 0) + 1 }
        }

        var finalRoot: TreeNode? = null
        for (t in trees) {
            if (t == null) continue
            if (!leafCount.containsKey(t.`val`)) {
                if (finalRoot != null) return null   // more than one possible root
                finalRoot = t
            }
        }

        if (finalRoot == null) return null

        // remove the chosen root from map so we don't try to merge it into itself
        rootMap.remove(finalRoot.`val`)

        fun merge(node: TreeNode) {
            node.left?.let { leftChild ->
                if (rootMap.containsKey(leftChild.`val`) && leftChild.left == null && leftChild.right == null) {
                    val sub = rootMap.remove(leftChild.`val`)!!
                    node.left = sub
                    merge(sub)
                } else {
                    merge(leftChild)
                }
            }
            node.right?.let { rightChild ->
                if (rootMap.containsKey(rightChild.`val`) && rightChild.left == null && rightChild.right == null) {
                    val sub = rootMap.remove(rightChild.`val`)!!
                    node.right = sub
                    merge(sub)
                } else {
                    merge(rightChild)
                }
            }
        }

        merge(finalRoot)

        if (rootMap.isNotEmpty()) return null   // some trees couldn't be merged

        fun isValid(node: TreeNode?, low: Long, high: Long): Boolean {
            if (node == null) return true
            val v = node.`val`.toLong()
            if (v <= low || v >= high) return false
            return isValid(node.left, low, v) && isValid(node.right, v, high)
        }

        return if (isValid(finalRoot, Long.MIN_VALUE, Long.MAX_VALUE)) finalRoot else null
    }
}
```

## Golang

```go
type LeafInfo struct {
	parent *TreeNode
	isLeft bool
}

func canMerge(trees []*TreeNode) *TreeNode {
	roots := make(map[int]*TreeNode)
	leafMap := make(map[int]LeafInfo)

	// map roots
	for _, r := range trees {
		roots[r.Val] = r
	}

	// collect initial leaves (excluding root itself)
	var collectLeaves func(node, parent *TreeNode, isLeft bool)
	collectLeaves = func(node, parent *TreeNode, isLeft bool) {
		if node == nil {
			return
		}
		if node.Left == nil && node.Right == nil {
			leafMap[node.Val] = LeafInfo{parent: parent, isLeft: isLeft}
			return
		}
		collectLeaves(node.Left, node, true)
		collectLeaves(node.Right, node, false)
	}
	for _, r := range trees {
		if r.Left != nil {
			collectLeaves(r.Left, r, true)
		}
		if r.Right != nil {
			collectLeaves(r.Right, r, false)
		}
	}

	// iterative merging
	for {
		merged := false
		for leafVal, info := range leafMap {
			childRoot, ok := roots[leafVal]
			if !ok || info.parent == nil {
				continue
			}
			// attach childRoot to the leaf position
			if info.isLeft {
				info.parent.Left = childRoot
			} else {
				info.parent.Right = childRoot
			}
			delete(roots, leafVal)
			delete(leafMap, leafVal)

			// add new leaves from the attached subtree
			if childRoot.Left != nil {
				collectLeaves(childRoot.Left, childRoot, true)
			}
			if childRoot.Right != nil {
				collectLeaves(childRoot.Right, childRoot, false)
			}
			merged = true
		}
		if !merged {
			break
		}
	}

	if len(roots) != 1 {
		return nil
	}
	var finalRoot *TreeNode
	for _, r := range roots {
		finalRoot = r
		break
	}

	// validate BST
	var validate func(node *TreeNode, low, high int64) bool
	validate = func(node *TreeNode, low, high int64) bool {
		if node == nil {
			return true
		}
		val := int64(node.Val)
		if val <= low || val >= high {
			return false
		}
		return validate(node.Left, low, val) && validate(node.Right, val, high)
	}
	if !validate(finalRoot, -1<<63, 1<<63-1) {
		return nil
	}
	return finalRoot
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

def can_merge(trees)
  root_map = {}
  leaf_counts = Hash.new(0)

  trees.each do |root|
    root_map[root.val] = root
    leaf_counts[root.left.val] += 1 if root.left
    leaf_counts[root.right.val] += 1 if root.right
  end

  start_root_val = nil
  root_map.each_key do |val|
    next unless leaf_counts[val].zero?
    return nil if start_root_val # more than one possible root
    start_root_val = val
  end
  return nil unless start_root_val

  start_root = root_map.delete(start_root_val)

  valid = lambda do |node, low, high|
    return true if node.nil?
    v = node.val
    return false unless v > low && v < high

    if node.left
      if node.left.left.nil? && node.left.right.nil? && root_map.key?(node.left.val)
        node.left = root_map.delete(node.left.val)
      end
      return false unless valid.call(node.left, low, v)
    end

    if node.right
      if node.right.left.nil? && node.right.right.nil? && root_map.key?(node.right.val)
        node.right = root_map.delete(node.right.val)
      end
      return false unless valid.call(node.right, v, high)
    end
    true
  end

  success = valid.call(start_root, -Float::INFINITY, Float::INFINITY) && root_map.empty?
  success ? start_root : nil
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
object Solution {
  def canMerge(trees: List[TreeNode]): TreeNode = {
    if (trees.isEmpty) return null

    val rootMap = mutable.Map[Int, TreeNode]()
    val leafVals = mutable.Set[Int]()

    // populate maps and leaf set
    for (root <- trees) {
      rootMap(root.value) = root
      if (root.left != null) leafVals += root.left.value
      if (root.right != null) leafVals += root.right.value
    }

    // find the unique root that is not a leaf value
    val candidates = rootMap.keys.filter(k => !leafVals.contains(k)).toSeq
    if (candidates.length != 1) return null

    var finalRoot = rootMap(candidates.head)
    rootMap.remove(finalRoot.value)

    // merge trees using stack DFS
    val stack = mutable.Stack[TreeNode]()
    stack.push(finalRoot)

    while (stack.nonEmpty) {
      val cur = stack.pop()

      // left child
      var left = cur.left
      if (left != null && left.left == null && left.right == null && rootMap.contains(left.value)) {
        val sub = rootMap(left.value)
        rootMap.remove(left.value)
        cur.left = sub
        left = sub
      }
      if (cur.left != null) stack.push(cur.left)

      // right child
      var right = cur.right
      if (right != null && right.left == null && right.right == null && rootMap.contains(right.value)) {
        val sub = rootMap(right.value)
        rootMap.remove(right.value)
        cur.right = sub
        right = sub
      }
      if (cur.right != null) stack.push(cur.right)
    }

    // all roots must be merged
    if (rootMap.nonEmpty) return null

    // validate BST via inorder traversal (strictly increasing values)
    var prev: Option[Int] = None
    val inStack = mutable.Stack[TreeNode]()
    var node: TreeNode = finalRoot
    while (node != null || inStack.nonEmpty) {
      while (node != null) {
        inStack.push(node)
        node = node.left
      }
      val cur = inStack.pop()
      if (prev.isDefined && cur.value <= prev.get) return null
      prev = Some(cur.value)
      node = cur.right
    }

    finalRoot
  }
}
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

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

pub struct Solution;

impl Solution {
    pub fn can_merge(trees: Vec<Option<Rc<RefCell<TreeNode>>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut root_map: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut leaf_counts: HashMap<i32, i32> = HashMap::new();

        for opt in &trees {
            if let Some(rc) = opt {
                let val = rc.borrow().val;
                root_map.insert(val, Rc::clone(rc));
                if let Some(l) = &rc.borrow().left {
                    *leaf_counts.entry(l.borrow().val).or_insert(0) += 1;
                }
                if let Some(r) = &rc.borrow().right {
                    *leaf_counts.entry(r.borrow().val).or_insert(0) += 1;
                }
            }
        }

        // find the unique root that is not a leaf in any tree
        let mut final_root_val: Option<i32> = None;
        for (&val, _) in &root_map {
            if !leaf_counts.contains_key(&val) {
                if final_root_val.is_some() {
                    return None; // multiple possible roots
                }
                final_root_val = Some(val);
            }
        }
        let root_val = match final_root_val {
            Some(v) => v,
            None => return None,
        };

        let mut root = root_map.remove(&root_val).unwrap();

        if !Self::dfs(Rc::clone(&root), i32::MIN, i32::MAX, &mut root_map) {
            return None;
        }

        // all trees must be merged
        if !root_map.is_empty() {
            return None;
        }
        Some(root)
    }

    fn dfs(
        node: Rc<RefCell<TreeNode>>,
        low: i32,
        high: i32,
        map: &mut HashMap<i32, Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let val = node.borrow().val;
        if !(low < val && val < high) {
            return false;
        }

        // process left child
        {
            let left_opt = node.borrow_mut().left.take();
            if let Some(left_rc) = left_opt {
                let lval = left_rc.borrow().val;
                if left_rc.borrow().left.is_none()
                    && left_rc.borrow().right.is_none()
                    && map.contains_key(&lval)
                {
                    // merge subtree rooted at lval
                    let merged = map.remove(&lval).unwrap();
                    if !Self::dfs(Rc::clone(&merged), low, val, map) {
                        return false;
                    }
                    node.borrow_mut().left = Some(merged);
                } else {
                    if !Self::dfs(Rc::clone(&left_rc), low, val, map) {
                        return false;
                    }
                    node.borrow_mut().left = Some(left_rc);
                }
            }
        }

        // process right child
        {
            let right_opt = node.borrow_mut().right.take();
            if let Some(right_rc) = right_opt {
                let rval = right_rc.borrow().val;
                if right_rc.borrow().left.is_none()
                    && right_rc.borrow().right.is_none()
                    && map.contains_key(&rval)
                {
                    // merge subtree rooted at rval
                    let merged = map.remove(&rval).unwrap();
                    if !Self::dfs(Rc::clone(&merged), val, high, map) {
                        return false;
                    }
                    node.borrow_mut().right = Some(merged);
                } else {
                    if !Self::dfs(Rc::clone(&right_rc), val, high, map) {
                        return false;
                    }
                    node.borrow_mut().right = Some(right_rc);
                }
            }
        }

        true
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

(define/contract (can-merge trees)
  (-> (listof (or/c tree-node? #f)) (or/c tree-node? #f))
  (let ((root-hash (make-hash))
        (leaf-count (make-hash)))
    ;; populate root map and leaf counts
    (for ([t trees])
      (when t
        (hash-set! root-hash (tree-node-val t) t)
        (let recur ((node t))
          (when node
            (define l (tree-node-left node))
            (define r (tree-node-right node))
            (if (and (not l) (not r))
                (let ((cnt (hash-ref leaf-count (tree-node-val node) 0)))
                  (hash-set! leaf-count (tree-node-val node) (+ cnt 1)))
                (begin
                  (recur l)
                  (recur r)))))))
    ;; check duplicate leaves
    (define dup #f)
    (for ([k (in-hash-keys leaf-count)])
      (when (> (hash-ref leaf-count k) 1)
        (set! dup #t)))
    (if dup
        #f
        (let ((candidates '()))
          (for ([k (in-hash-keys root-hash)])
            (unless (hash-has-key? leaf-count k)
              (set! candidates (cons k candidates))))
          (if (= (length candidates) 1)
              (let* ((root-val (car candidates))
                     (root (hash-ref root-hash root-val)))
                (hash-remove! root-hash root-val)
                (define (merge node low high)
                  (if (not node)
                      #t
                      (let ((val (tree-node-val node)))
                        (if (or (<= val low) (>= val high))
                            #f
                            (let ((left (tree-node-left node))
                                  (right (tree-node-right node)))
                              (if (and (not left) (not right)
                                       (hash-has-key? root-hash val))
                                  (let ((sub (hash-ref root-hash val)))
                                    (hash-remove! root-hash val)
                                    (set-tree-node-val! node (tree-node-val sub))
                                    (set-tree-node-left! node (tree-node-left sub))
                                    (set-tree-node-right! node (tree-node-right sub))
                                    (and (merge (tree-node-left node) low val)
                                         (merge (tree-node-right node) val high)))
                                  (and (merge left low val)
                                       (merge right val high))))))))
                (if (and (merge root -inf.0 +inf.0)
                         (hash-empty? root-hash))
                    root
                    #f))
              #f)))))
```
