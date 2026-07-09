# 1110. Delete Nodes And Return Forest

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
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> delSet(to_delete.begin(), to_delete.end());
        vector<TreeNode*> forest;
        function<TreeNode*(TreeNode*, bool)> dfs = [&](TreeNode* node, bool isRoot) -> TreeNode* {
            if (!node) return nullptr;
            bool deleted = delSet.count(node->val);
            if (isRoot && !deleted) forest.push_back(node);
            node->left = dfs(node->left, deleted);
            node->right = dfs(node->right, deleted);
            return deleted ? nullptr : node;
        };
        dfs(root, true);
        return forest;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> deleteSet = new HashSet<>();
        for (int v : to_delete) deleteSet.add(v);
        List<TreeNode> forest = new ArrayList<>();
        root = dfs(root, deleteSet, forest);
        if (root != null) forest.add(root);
        return forest;
    }
    
    private TreeNode dfs(TreeNode node, Set<Integer> deleteSet, List<TreeNode> forest) {
        if (node == null) return null;
        node.left = dfs(node.left, deleteSet, forest);
        node.right = dfs(node.right, deleteSet, forest);
        if (deleteSet.contains(node.val)) {
            if (node.left != null) forest.add(node.left);
            if (node.right != null) forest.add(node.right);
            return null;
        }
        return node;
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
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        delete_set = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node

        root = dfs(root)
        if root:
            forest.append(root)
        return forest
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
    def delNodes(self, root: Optional['TreeNode'], to_delete: List[int]) -> List['TreeNode']:
        delete_set = set(to_delete)
        forest: List['TreeNode'] = []

        def dfs(node: Optional['TreeNode']) -> Optional['TreeNode']:
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node

        root = dfs(root)
        if root:
            forest.append(root)
        return forest
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Helper function: postorder traversal, returns the possibly new subtree root */
static struct TreeNode* dfs(struct TreeNode* node, int del[], struct TreeNode** forest, int* idx) {
    if (!node) return NULL;
    
    node->left = dfs(node->left, del, forest, idx);
    node->right = dfs(node->right, del, forest, idx);
    
    if (del[node->val]) {
        if (node->left)  forest[(*idx)++] = node->left;
        if (node->right) forest[(*idx)++] = node->right;
        return NULL;   // delete this node
    }
    return node;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** delNodes(struct TreeNode* root, int* to_delete, int to_deleteSize, int* returnSize){
    int del[1001] = {0};
    for (int i = 0; i < to_deleteSize; ++i) {
        if (to_delete[i] >= 0 && to_delete[i] <= 1000)
            del[to_delete[i]] = 1;
    }
    
    /* Allocate maximum possible size (number of nodes ≤ 1000) */
    struct TreeNode** forest = malloc(sizeof(struct TreeNode*) * 1001);
    int idx = 0;
    
    root = dfs(root, del, forest, &idx);
    if (root) {
        forest[idx++] = root;
    }
    
    *returnSize = idx;
    return forest;
}
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
public class Solution {
    private HashSet<int> toDeleteSet;
    private IList<TreeNode> forest;

    public IList<TreeNode> DelNodes(TreeNode root, int[] to_delete) {
        toDeleteSet = new HashSet<int>(to_delete);
        forest = new List<TreeNode>();
        TreeNode newRoot = Dfs(root);
        if (newRoot != null) {
            forest.Add(newRoot);
        }
        return forest;
    }

    private TreeNode Dfs(TreeNode node) {
        if (node == null) return null;

        node.left = Dfs(node.left);
        node.right = Dfs(node.right);

        if (toDeleteSet.Contains(node.val)) {
            if (node.left != null) forest.Add(node.left);
            if (node.right != null) forest.Add(node.right);
            return null;
        }

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
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const delSet = new Set(to_delete);
    const forest = [];

    const dfs = (node) => {
        if (!node) return null;
        node.left = dfs(node.left);
        node.right = dfs(node.right);
        if (delSet.has(node.val)) {
            if (node.left) forest.push(node.left);
            if (node.right) forest.push(node.right);
            return null;
        }
        return node;
    };

    const newRoot = dfs(root);
    if (newRoot) forest.push(newRoot);
    return forest;
};
```

## Typescript

```typescript
function delNodes(root: TreeNode | null, to_delete: number[]): Array<TreeNode | null> {
    const deleteSet = new Set(to_delete);
    const forest: TreeNode[] = [];

    function dfs(node: TreeNode | null, isRoot: boolean): TreeNode | null {
        if (!node) return null;
        const deleted = deleteSet.has(node.val);
        if (isRoot && !deleted) {
            forest.push(node);
        }
        node.left = dfs(node.left, deleted);
        node.right = dfs(node.right, deleted);
        return deleted ? null : node;
    }

    dfs(root, true);
    return forest;
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
     * @param Integer[] $to_delete
     * @return TreeNode[]
     */
    function delNodes($root, $to_delete) {
        $delSet = array_flip($to_delete);
        $forest = [];
        $this->dfs($root, true, $delSet, $forest);
        return $forest;
    }

    private function dfs($node, $isRoot, &$delSet, &$forest) {
        if ($node === null) {
            return null;
        }
        $toDelete = isset($delSet[$node->val]);
        if ($isRoot && !$toDelete) {
            $forest[] = $node;
        }
        $node->left  = $this->dfs($node->left,  $toDelete, $delSet, $forest);
        $node->right = $this->dfs($node->right, $toDelete, $delSet, $forest);
        return $toDelete ? null : $node;
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
    func delNodes(_ root: TreeNode?, _ to_delete: [Int]) -> [TreeNode?] {
        var deleteSet = Set(to_delete)
        var forest = [TreeNode]()
        
        func dfs(_ node: TreeNode?) -> TreeNode? {
            guard let node = node else { return nil }
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if deleteSet.contains(node.val) {
                if let left = node.left {
                    forest.append(left)
                }
                if let right = node.right {
                    forest.append(right)
                }
                return nil
            } else {
                return node
            }
        }
        
        if let newRoot = dfs(root) {
            forest.append(newRoot)
        }
        
        return forest.map { $0 as TreeNode? }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun delNodes(root: TreeNode?, to_delete: IntArray): List<TreeNode?> {
        val deleteSet = to_delete.toHashSet()
        val forest = mutableListOf<TreeNode?>()

        fun dfs(node: TreeNode?): TreeNode? {
            if (node == null) return null
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if (deleteSet.contains(node.`val`)) {
                if (node.left != null) forest.add(node.left)
                if (node.right != null) forest.add(node.right)
                return null
            }
            return node
        }

        val newRoot = dfs(root)
        if (newRoot != null) forest.add(newRoot)

        return forest
    }
}
```

## Golang

```go
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	delSet := make(map[int]bool, len(to_delete))
	for _, v := range to_delete {
		delSet[v] = true
	}
	var forest []*TreeNode

	var dfs func(*TreeNode) *TreeNode
	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		node.Left = dfs(node.Left)
		node.Right = dfs(node.Right)

		if delSet[node.Val] {
			if node.Left != nil {
				forest = append(forest, node.Left)
			}
			if node.Right != nil {
				forest = append(forest, node.Right)
			}
			return nil
		}
		return node
	}

	root = dfs(root)
	if root != nil {
		forest = append(forest, root)
	}
	return forest
}
```

## Ruby

```ruby
require 'set'

def del_nodes(root, to_delete)
  delete_set = Set.new(to_delete)
  forest = []

  dfs = lambda do |node|
    return nil unless node
    node.left = dfs.call(node.left)
    node.right = dfs.call(node.right)

    if delete_set.include?(node.val)
      forest << node.left if node.left
      forest << node.right if node.right
      nil
    else
      node
    end
  end

  root = dfs.call(root)
  forest << root if root
  forest
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

    def delNodes(root: TreeNode, to_delete: Array[Int]): List[TreeNode] = {
        if (root == null) return Nil

        val deleteSet = to_delete.toSet
        val forest = ListBuffer.empty[TreeNode]

        def dfs(node: TreeNode): TreeNode = {
            if (node == null) return null
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if (deleteSet.contains(node.value)) {
                if (node.left != null) forest += node.left
                if (node.right != null) forest += node.right
                null
            } else {
                node
            }
        }

        val newRoot = dfs(root)
        if (newRoot != null) forest += newRoot

        forest.toList
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashSet;

impl Solution {
    pub fn del_nodes(root: Option<Rc<RefCell<TreeNode>>>, to_delete: Vec<i32>) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let delete_set: HashSet<i32> = to_delete.into_iter().collect();
        let mut forest: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();

        fn dfs(
            node: Option<Rc<RefCell<TreeNode>>>,
            set: &HashSet<i32>,
            forest: &mut Vec<Option<Rc<RefCell<TreeNode>>>>
        ) -> Option<Rc<RefCell<TreeNode>>> {
            match node {
                Some(rc_node) => {
                    // Detach children
                    let left_child;
                    let right_child;
                    {
                        let mut nb = rc_node.borrow_mut();
                        left_child = nb.left.take();
                        right_child = nb.right.take();
                    }

                    let new_left = dfs(left_child, set, forest);
                    let new_right = dfs(right_child, set, forest);

                    // Reattach processed children
                    {
                        let mut nb = rc_node.borrow_mut();
                        nb.left = new_left.clone();
                        nb.right = new_right.clone();
                    }

                    if set.contains(&rc_node.borrow().val) {
                        if let Some(l) = new_left { forest.push(Some(l)); }
                        if let Some(r) = new_right { forest.push(Some(r)); }
                        None
                    } else {
                        Some(rc_node)
                    }
                },
                None => None,
            }
        }

        let new_root = dfs(root, &delete_set, &mut forest);
        if let Some(r) = new_root {
            forest.push(Some(r));
        }
        forest
    }
}
```

## Racket

```racket
(define/contract (del-nodes root to_delete)
  (-> (or/c tree-node? #f) (listof exact-integer?) (listof (or/c tree-node? #f)))
  (if (not root)
      '()
      (let* ((del-set (make-hash))
             (_ (for ([v to_delete]) (hash-set! del-set v #t)))
             (forest '()))
        (define (dfs node)
          (if (not node)
              #f
              (let* ((new-left  (dfs (tree-node-left node)))
                     (new-right (dfs (tree-node-right node))))
                (set-tree-node-left! node new-left)
                (set-tree-node-right! node new-right)
                (if (hash-has-key? del-set (tree-node-val node))
                    (begin
                      (when new-left  (set! forest (cons new-left forest)))
                      (when new-right (set! forest (cons new-right forest)))
                      #f)
                    node))))
        (define new-root (dfs root))
        (when (and new-root (not (hash-has-key? del-set (tree-node-val new-root))))
          (set! forest (cons new-root forest)))
        (reverse forest))))
```
