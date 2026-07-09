# 2641. Cousins in Binary Tree II

## Cpp

```cpp
#include <bits/stdc++.h>
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
class Solution {
public:
    TreeNode* replaceValueInTree(TreeNode* root) {
        if (!root) return nullptr;
        
        // First BFS to compute sum of each level
        vector<long long> levelSum;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            long long curSum = 0;
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                curSum += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            levelSum.push_back(curSum);
        }
        
        // Second BFS to update values
        queue<TreeNode*> q2;
        q2.push(root);
        root->val = 0;               // root has no cousins
        int depth = 1;                // children are at depth 1
        
        while (!q2.empty()) {
            int sz = q2.size();
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q2.front(); q2.pop();
                
                long long siblingSum = 0;
                if (node->left) siblingSum += node->left->val;
                if (node->right) siblingSum += node->right->val;
                
                if (node->left) {
                    node->left->val = static_cast<int>(levelSum[depth] - siblingSum);
                    q2.push(node->left);
                }
                if (node->right) {
                    node->right->val = static_cast<int>(levelSum[depth] - siblingSum);
                    q2.push(node->right);
                }
            }
            ++depth;
        }
        
        return root;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public TreeNode replaceValueInTree(TreeNode root) {
        if (root == null) return null;

        // First pass: compute sum of values at each level
        List<Long> levelSums = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                sum += node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            levelSums.add(sum);
        }

        // Second pass: update each node's value to the sum of its cousins
        queue.clear();
        queue.offer(root);
        root.val = 0; // root has no cousins
        int levelIdx = 1; // start from children level

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();

                long siblingSum = 0;
                if (node.left != null) siblingSum += node.left.val;
                if (node.right != null) siblingSum += node.right.val;

                if (node.left != null) {
                    int newVal = (int) (levelSums.get(levelIdx) - siblingSum);
                    node.left.val = newVal;
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    int newVal = (int) (levelSums.get(levelIdx) - siblingSum);
                    node.right.val = newVal;
                    queue.offer(node.right);
                }
            }
            levelIdx++;
        }

        return root;
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
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        # First pass: compute sum of values at each level.
        level_sums = []
        queue = [root]
        while queue:
            next_queue = []
            lvl_sum = 0
            for node in queue:
                lvl_sum += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            level_sums.append(lvl_sum)
            queue = next_queue

        # Second pass: update each node's value to sum of cousins.
        root.val = 0  # root has no cousins
        queue = [root]
        depth = 1  # children are at level 1
        while queue:
            next_queue = []
            for parent in queue:
                left, right = parent.left, parent.right
                sibling_sum = 0
                if left:
                    sibling_sum += left.val
                if right:
                    sibling_sum += right.val

                if left:
                    left.val = level_sums[depth] - sibling_sum
                    next_queue.append(left)
                if right:
                    right.val = level_sums[depth] - sibling_sum
                    next_queue.append(right)

            queue = next_queue
            depth += 1

        return root
```

## Python3

```python
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # First pass: compute sum of values at each level
        level_sums = []
        q = deque([root])
        while q:
            lvl_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                lvl_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(lvl_sum)

        # Second pass: update each node's value to sum of cousins
        root.val = 0
        q = deque([root])
        lvl = 1  # children are at this level
        while q and lvl < len(level_sums):
            for _ in range(len(q)):
                parent = q.popleft()
                sibling_sum = (parent.left.val if parent.left else 0) + \
                              (parent.right.val if parent.right else 0)

                if parent.left:
                    parent.left.val = level_sums[lvl] - sibling_sum
                    q.append(parent.left)
                if parent.right:
                    parent.right.val = level_sums[lvl] - sibling_sum
                    q.append(parent.right)
            lvl += 1

        return root
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
struct TreeNode* replaceValueInTree(struct TreeNode* root) {
    if (!root) return NULL;

    /* ---------- First BFS: compute level sums ---------- */
    int queueCap = 1024;
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * queueCap);
    int front = 0, back = 0;
    queue[back++] = root;

    int levelCap = 128;
    long long *levelSums = (long long *)malloc(sizeof(long long) * levelCap);
    int levelCount = 0;

    while (front < back) {
        int sz = back - front;
        long long sum = 0;
        for (int i = 0; i < sz; ++i) {
            struct TreeNode *node = queue[front++];
            sum += node->val;
            if (node->left) {
                if (back == queueCap) {
                    queueCap <<= 1;
                    queue = (struct TreeNode **)realloc(queue, sizeof(struct TreeNode *) * queueCap);
                }
                queue[back++] = node->left;
            }
            if (node->right) {
                if (back == queueCap) {
                    queueCap <<= 1;
                    queue = (struct TreeNode **)realloc(queue, sizeof(struct TreeNode *) * queueCap);
                }
                queue[back++] = node->right;
            }
        }
        if (levelCount == levelCap) {
            levelCap <<= 1;
            levelSums = (long long *)realloc(levelSums, sizeof(long long) * levelCap);
        }
        levelSums[levelCount++] = sum;
    }

    int totalNodes = back;   // number of nodes visited

    /* ---------- Second BFS: update node values ---------- */
    front = 0;
    back = 0;
    queue[back++] = root;
    root->val = 0;               // root has no cousins
    int levelIdx = 1;            // start from children level

    while (front < back) {
        int sz = back - front;
        for (int i = 0; i < sz; ++i) {
            struct TreeNode *node = queue[front++];
            long long childSum = 0;
            if (node->left) childSum += node->left->val;
            if (node->right) childSum += node->right->val;

            if (node->left) {
                node->left->val = (int)(levelSums[levelIdx] - childSum);
                queue[back++] = node->left;
            }
            if (node->right) {
                node->right->val = (int)(levelSums[levelIdx] - childSum);
                queue[back++] = node->right;
            }
        }
        ++levelIdx;
    }

    free(queue);
    free(levelSums);
    return root;
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
    public TreeNode ReplaceValueInTree(TreeNode root) {
        if (root == null) return null;

        // First pass: compute sum of values at each level.
        var levelSums = new System.Collections.Generic.List<long>();
        var queue = new System.Collections.Generic.Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            int sz = queue.Count;
            long sum = 0;
            for (int i = 0; i < sz; i++) {
                var node = queue.Dequeue();
                sum += node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            levelSums.Add(sum);
        }

        // Second pass: update each node's value to the sum of its cousins.
        var q2 = new System.Collections.Generic.Queue<TreeNode>();
        q2.Enqueue(root);
        root.val = 0; // root has no cousins
        int levelIdx = 1; // children are at level 1

        while (q2.Count > 0) {
            int sz = q2.Count;
            for (int i = 0; i < sz; i++) {
                var node = q2.Dequeue();
                long siblingSum = 0;
                if (node.left != null) siblingSum += node.left.val;
                if (node.right != null) siblingSum += node.right.val;

                if (node.left != null) {
                    node.left.val = (int)(levelSums[levelIdx] - siblingSum);
                    q2.Enqueue(node.left);
                }
                if (node.right != null) {
                    node.right.val = (int)(levelSums[levelIdx] - siblingSum);
                    q2.Enqueue(node.right);
                }
            }
            levelIdx++;
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
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var replaceValueInTree = function(root) {
    if (!root) return root;
    
    // First pass: compute sum of values at each level.
    const levelSums = [];
    let queue = [root];
    while (queue.length) {
        const nextLevel = [];
        let sum = 0;
        for (const node of queue) {
            sum += node.val;
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        levelSums.push(sum);
        queue = nextLevel;
    }
    
    // Second pass: replace each node's value with cousin sum.
    let level = 1; // start from children of root
    queue = [root];
    root.val = 0; // root has no cousins
    while (level < levelSums.length) {
        const nextLevel = [];
        for (const node of queue) {
            const leftVal = node.left ? node.left.val : 0;
            const rightVal = node.right ? node.right.val : 0;
            const siblingSum = leftVal + rightVal;
            
            if (node.left) {
                node.left.val = levelSums[level] - siblingSum;
                nextLevel.push(node.left);
            }
            if (node.right) {
                node.right.val = levelSums[level] - siblingSum;
                nextLevel.push(node.right);
            }
        }
        queue = nextLevel;
        level++;
    }
    
    return root;
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

function replaceValueInTree(root: TreeNode | null): TreeNode | null {
    if (!root) return root;

    // First pass: compute sum of values at each level
    const levelSums: number[] = [];
    let queue: TreeNode[] = [root];
    while (queue.length) {
        let nextLevel: TreeNode[] = [];
        let sum = 0;
        for (const node of queue) {
            sum += node.val;
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        levelSums.push(sum);
        queue = nextLevel;
    }

    // Second pass: update each node's value to cousin sum
    root.val = 0; // root has no cousins
    queue = [root];
    let level = 0;
    while (queue.length) {
        const nextLevel: TreeNode[] = [];
        for (const node of queue) {
            const siblingSum = (node.left?.val ?? 0) + (node.right?.val ?? 0);
            if (node.left) {
                node.left.val = levelSums[level + 1] - siblingSum;
                nextLevel.push(node.left);
            }
            if (node.right) {
                node.right.val = levelSums[level + 1] - siblingSum;
                nextLevel.push(node.right);
            }
        }
        queue = nextLevel;
        level++;
    }

    return root;
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
     * @return TreeNode
     */
    function replaceValueInTree($root) {
        if ($root === null) {
            return null;
        }

        // First pass: compute sum of values at each level.
        $queue = new SplQueue();
        $queue->enqueue($root);
        $levelSums = [];

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $sum = 0;
            for ($i = 0; $i < $size; $i++) {
                $node = $queue->dequeue();
                $sum += $node->val;
                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }
            $levelSums[] = $sum;
        }

        // Second pass: update each node's value to sum of cousins.
        $queue2 = new SplQueue();
        $queue2->enqueue($root);
        $root->val = 0; // root has no cousins
        $level = 1;

        while (!$queue2->isEmpty()) {
            $size = $queue2->count();
            for ($i = 0; $i < $size; $i++) {
                $node = $queue2->dequeue();

                $childrenSum = 0;
                if ($node->left !== null) {
                    $childrenSum += $node->left->val;
                }
                if ($node->right !== null) {
                    $childrenSum += $node->right->val;
                }

                if ($node->left !== null) {
                    $node->left->val = $levelSums[$level] - $childrenSum;
                    $queue2->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $node->right->val = $levelSums[$level] - $childrenSum;
                    $queue2->enqueue($node->right);
                }
            }
            $level++;
        }

        return $root;
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
    func replaceValueInTree(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else { return nil }
        
        // First BFS to compute sum of each level
        var levelSums = [Int]()
        var queue = [TreeNode]()
        queue.append(root)
        var idx = 0
        while idx < queue.count {
            let levelSize = queue.count - idx
            var sum = 0
            for _ in 0..<levelSize {
                let node = queue[idx]
                idx += 1
                sum += node.val
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            levelSums.append(sum)
        }
        
        // Second BFS to replace values with cousin sums
        root.val = 0
        var q2 = [TreeNode]()
        q2.append(root)
        var idx2 = 0
        var level = 0
        while idx2 < q2.count {
            let levelSize = q2.count - idx2
            for _ in 0..<levelSize {
                let node = q2[idx2]
                idx2 += 1
                
                // original values of children before they are overwritten
                let leftVal = node.left?.val ?? 0
                let rightVal = node.right?.val ?? 0
                let siblingSum = leftVal + rightVal
                
                if let left = node.left {
                    left.val = levelSums[level + 1] - siblingSum
                    q2.append(left)
                }
                if let right = node.right {
                    right.val = levelSums[level + 1] - siblingSum
                    q2.append(right)
                }
            }
            level += 1
        }
        
        return root
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
    fun replaceValueInTree(root: TreeNode?): TreeNode? {
        if (root == null) return null

        // First BFS to compute sum of values at each level
        val levelSums = mutableListOf<Long>()
        var queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        while (queue.isNotEmpty()) {
            var levelSum = 0L
            val size = queue.size
            repeat(size) {
                val node = queue.removeFirst()
                levelSum += node.`val`.toLong()
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            levelSums.add(levelSum)
        }

        // Second BFS to replace values with cousin sums
        queue = ArrayDeque()
        queue.add(root)
        root.`val` = 0   // root has no cousins
        var levelIdx = 1
        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val node = queue.removeFirst()
                val leftChild = node.left
                val rightChild = node.right
                val siblingSum = (leftChild?.`val` ?: 0) + (rightChild?.`val` ?: 0)
                if (leftChild != null) {
                    leftChild.`val` = (levelSums[levelIdx] - siblingSum).toInt()
                    queue.add(leftChild)
                }
                if (rightChild != null) {
                    rightChild.`val` = (levelSums[levelIdx] - siblingSum).toInt()
                    queue.add(rightChild)
                }
            }
            levelIdx++
        }

        return root
    }
}
```

## Dart

```dart
import 'dart:collection';

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
  TreeNode? replaceValueInTree(TreeNode? root) {
    if (root == null) return null;

    // First pass: compute sum of values at each level.
    List<int> levelSums = [];
    Queue<TreeNode> queue = Queue();
    queue.add(root);
    while (queue.isNotEmpty) {
      int size = queue.length;
      int sum = 0;
      for (int i = 0; i < size; i++) {
        TreeNode node = queue.removeFirst();
        sum += node.val;
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      levelSums.add(sum);
    }

    // Second pass: update each node's value to the sum of its cousins.
    queue.clear();
    queue.add(root);
    root.val = 0; // root has no cousins
    int levelIdx = 1; // children are at level 1

    while (queue.isNotEmpty) {
      int size = queue.length;
      for (int i = 0; i < size; i++) {
        TreeNode node = queue.removeFirst();

        int leftVal = node.left?.val ?? 0;
        int rightVal = node.right?.val ?? 0;
        int siblingSum = leftVal + rightVal;

        if (node.left != null) {
          node.left!.val = levelSums[levelIdx] - siblingSum;
          queue.add(node.left!);
        }
        if (node.right != null) {
          node.right!.val = levelSums[levelIdx] - siblingSum;
          queue.add(node.right!);
        }
      }
      levelIdx++;
    }

    return root;
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
func replaceValueInTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	// First pass: compute sum of values at each level.
	var levelSums []int
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		size := len(queue)
		sum := 0
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		levelSums = append(levelSums, sum)
	}

	// Second pass: update each node's value to the sum of its cousins.
	root.Val = 0
	queue = []*TreeNode{root}
	level := 1 // children are at level 1
	for len(queue) > 0 && level < len(levelSums) {
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]

			siblingSum := 0
			if node.Left != nil {
				siblingSum += node.Left.Val
			}
			if node.Right != nil {
				siblingSum += node.Right.Val
			}

			if node.Left != nil {
				node.Left.Val = levelSums[level] - siblingSum
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				node.Right.Val = levelSums[level] - siblingSum
				queue = append(queue, node.Right)
			}
		}
		level++
	}

	return root
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

def replace_value_in_tree(root)
  return nil unless root

  # First pass: compute sum of values at each level.
  level_sums = []
  queue = [root]
  front = 0
  while front < queue.size
    level_sum = 0
    level_end = queue.size
    while front < level_end
      node = queue[front]
      front += 1
      level_sum += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    level_sums << level_sum
  end

  # Second pass: update each node's value to sum of its cousins.
  root.val = 0
  queue = [root]
  front = 0
  level_index = 1
  while front < queue.size
    level_end = queue.size
    while front < level_end
      node = queue[front]
      front += 1

      sibling_sum = 0
      sibling_sum += node.left.val if node.left
      sibling_sum += node.right.val if node.right

      if node.left
        node.left.val = level_sums[level_index] - sibling_sum
        queue << node.left
      end
      if node.right
        node.right.val = level_sums[level_index] - sibling_sum
        queue << node.right
      end
    end
    level_index += 1
  end

  root
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
  def replaceValueInTree(root: TreeNode): TreeNode = {
    if (root == null) return null

    // First pass: compute sum of values at each level
    val levelSums = scala.collection.mutable.ArrayBuffer[Int]()
    val queue1 = scala.collection.mutable.Queue[TreeNode]()
    queue1.enqueue(root)
    while (queue1.nonEmpty) {
      val sz = queue1.size
      var sum: Long = 0L
      for (_ <- 0 until sz) {
        val node = queue1.dequeue()
        sum += node.value
        if (node.left != null) queue1.enqueue(node.left)
        if (node.right != null) queue1.enqueue(node.right)
      }
      levelSums.append(sum.toInt)
    }

    // Second pass: update each node's value to the sum of its cousins
    val queue2 = scala.collection.mutable.Queue[TreeNode]()
    queue2.enqueue(root)
    root.value = 0                     // root has no cousins
    var level = 1                      // children are at level 1
    while (queue2.nonEmpty) {
      val sz = queue2.size
      for (_ <- 0 until sz) {
        val node = queue2.dequeue()
        var siblingSum = 0
        if (node.left != null) siblingSum += node.left.value
        if (node.right != null) siblingSum += node.right.value

        if (node.left != null) {
          node.left.value = levelSums(level) - siblingSum
          queue2.enqueue(node.left)
        }
        if (node.right != null) {
          node.right.value = levelSums(level) - siblingSum
          queue2.enqueue(node.right)
        }
      }
      level += 1
    }

    root
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

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
    pub fn replace_value_in_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() {
            return None;
        }
        // First pass: compute sum of values at each level.
        let mut level_sums: Vec<i64> = Vec::new();
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.as_ref().unwrap().clone());

        while !queue.is_empty() {
            let sz = queue.len();
            let mut sum: i64 = 0;
            for _ in 0..sz {
                let node = queue.pop_front().unwrap();
                sum += node.borrow().val as i64;
                if let Some(left) = node.borrow().left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.borrow().right.clone() {
                    queue.push_back(right);
                }
            }
            level_sums.push(sum);
        }

        // Second pass: update each node's value to sum of cousins.
        let root_rc = root.unwrap();
        {
            let mut r = root_rc.borrow_mut();
            r.val = 0;
        }
        let mut q2: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        q2.push_back(root_rc.clone());

        let mut depth: usize = 1; // children are at this depth
        while !q2.is_empty() && depth < level_sums.len() {
            let sz = q2.len();
            for _ in 0..sz {
                let node = q2.pop_front().unwrap();

                let left_opt = node.borrow().left.clone();
                let right_opt = node.borrow().right.clone();

                let left_val = if let Some(ref l) = left_opt { l.borrow().val as i64 } else { 0 };
                let right_val = if let Some(ref r) = right_opt { r.borrow().val as i64 } else { 0 };
                let sibling_sum = left_val + right_val;

                if let Some(l) = left_opt {
                    l.borrow_mut().val = (level_sums[depth] - sibling_sum) as i32;
                    q2.push_back(l);
                }
                if let Some(r) = right_opt {
                    r.borrow_mut().val = (level_sums[depth] - sibling_sum) as i32;
                    q2.push_back(r);
                }
            }
            depth += 1;
        }

        Some(root_rc)
    }
}
```

## Racket

```racket
(define/contract (replace-value-in-tree root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (if (not root) 
      #f
      (letrec ((collect-level-sums
                (lambda (r)
                  (let loop ((nodes (list r)) (sums '()))
                    (if (null? nodes)
                        (reverse sums)
                        (let* ((sum (apply + (map tree-node-val nodes)))
                               (children (foldl
                                          (lambda (node acc)
                                            (let ((l (tree-node-left node))
                                                  (r (tree-node-right node)))
                                              (if l (cons l acc) acc)
                                              (if r (cons r acc) acc)))
                                          '()
                                          nodes)))
                          (loop (reverse children) (cons sum sums))))))))
        (define level-sums (collect-level-sums root))
        ;; root has no cousins
        (set-tree-node-val! root 0)
        (let loop ((queue (list root)) (lvl 1))
          (if (null? queue)
              root
              (let* ((level-sum (if (< lvl (length level-sums))
                                    (list-ref level-sums lvl)
                                    0))
                     (next '()))
                (for-each
                 (lambda (node)
                   (define left  (tree-node-left node))
                   (define right (tree-node-right node))
                   (when (or left right)
                     (define sibling-sum (+ (if left (tree-node-val left) 0)
                                            (if right (tree-node-val right) 0)))
                     (when left
                       (set-tree-node-val! left (- level-sum sibling-sum))
                       (set! next (cons left next)))
                     (when right
                       (set-tree-node-val! right (- level-sum sibling-sum))
                       (set! next (cons right next)))))
                 queue)
                (if (null? next)
                    root
                    (loop (reverse next) (+ lvl 1)))))))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                     left = null :: 'null' | #tree_node{},
                     right = null :: 'null' | #tree_node{}}).

-spec replace_value_in_tree(Root :: #tree_node{} | null) -> #tree_node{} | null.
replace_value_in_tree(Root) ->
    case Root of
        null -> null;
        _ ->
            LevelSums = compute_level_sums(Root),
            NewRoot0 = Root#tree_node{val = 0},
            process_node(NewRoot0, 0, LevelSums)
    end.

%% Compute sum of values at each depth using BFS.
-spec compute_level_sums(Root :: #tree_node{}) -> map().
compute_level_sums(Root) ->
    Q0 = queue:new(),
    Q1 = queue:in({Root, 0}, Q0),
    compute_loop(Q1, #{}).

-spec compute_loop(queue:queue(), map()) -> map().
compute_loop(Queue, Sums) ->
    case queue:out(Queue) of
        {empty, _} ->
            Sums;
        {{value, {Node, Depth}}, RestQueue} ->
            Val = Node#tree_node.val,
            NewSums = maps:update_with(
                Depth,
                fun(Prev) -> Prev + Val end,
                fun() -> Val end,
                Sums),
            Q2 = case Node#tree_node.left of
                    null -> RestQueue;
                    L -> queue:in({L, Depth + 1}, RestQueue)
                 end,
            Q3 = case Node#tree_node.right of
                    null -> Q2;
                    R -> queue:in({R, Depth + 1}, Q2)
                 end,
            compute_loop(Q3, NewSums)
    end.

%% Recursively update node values using precomputed level sums.
-spec process_node(Node :: #tree_node{}, Depth :: non_neg_integer(), map()) -> #tree_node{}.
process_node(Node, Depth, LevelSums) ->
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,

    LeftVal = case Left of
                  null -> 0;
                  L -> L#tree_node.val
              end,
    RightVal = case Right of
                   null -> 0;
                   R -> R#tree_node.val
               end,
    SiblingSum = LeftVal + RightVal,
    LevelNext = Depth + 1,
    LevelSumNext = maps:get(LevelNext, LevelSums, 0),

    NewLeft = case Left of
                  null -> null;
                  L ->
                      NewVal = LevelSumNext - SiblingSum,
                      UpdatedL = L#tree_node{val = NewVal},
                      process_node(UpdatedL, LevelNext, LevelSums)
              end,

    NewRight = case Right of
                   null -> null;
                   R ->
                       NewVal = LevelSumNext - SiblingSum,
                       UpdatedR = R#tree_node{val = NewVal},
                       process_node(UpdatedR, LevelNext, LevelSums)
               end,

    Node#tree_node{left = NewLeft, right = NewRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec replace_value_in_tree(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def replace_value_in_tree(nil), do: nil

  def replace_value_in_tree(root) do
    level_sums = collect_level_sums(root, 0, %{})
    replace_nodes(root, 0, level_sums)
  end

  defp collect_level_sums(nil, _depth, acc), do: acc

  defp collect_level_sums(%TreeNode{val: v, left: l, right: r}, depth, acc) do
    acc1 = Map.update(acc, depth, v, &(&1 + v))
    acc2 = collect_level_sums(l, depth + 1, acc1)
    collect_level_sums(r, depth + 1, acc2)
  end

  defp replace_nodes(nil, _depth, _level_sums), do: nil

  defp replace_nodes(%TreeNode{left: l, right: r} = node, depth, level_sums) do
    left_val = if l, do: l.val, else: 0
    right_val = if r, do: r.val, else: 0
    sibling_sum = left_val + right_val

    new_val =
      if depth == 0 do
        0
      else
        Map.get(level_sums, depth, 0) - sibling_sum
      end

    new_left = replace_nodes(l, depth + 1, level_sums)
    new_right = replace_nodes(r, depth + 1, level_sums)

    %TreeNode{val: new_val, left: new_left, right: new_right}
  end
end
```
