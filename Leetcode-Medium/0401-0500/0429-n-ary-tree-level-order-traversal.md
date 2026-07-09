# 0429. N-ary Tree Level Order Traversal

## Cpp

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    std::vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, std::vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    std::vector<std::vector<int>> levelOrder(Node* root) {
        if (!root) return {};
        std::vector<std::vector<int>> result;
        std::queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            std::vector<int> level;
            level.reserve(sz);
            for (int i = 0; i < sz; ++i) {
                Node* node = q.front(); q.pop();
                level.push_back(node->val);
                for (Node* child : node->children) {
                    if (child) q.push(child);
                }
            }
            result.emplace_back(std::move(level));
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>(size);
            for (int i = 0; i < size; i++) {
                Node node = queue.poll();
                level.add(node.val);
                if (node.children != null) {
                    for (Node child : node.children) {
                        if (child != null) {
                            queue.offer(child);
                        }
                    }
                }
            }
            result.add(level);
        }
        return result;
    }
}
```

## Python

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(level_vals)
        return result
```

## Python3

```python
from typing import List, Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result: List[List[int]] = []
        queue = collections.deque([root])
        while queue:
            level_size = len(queue)
            current_level: List[int] = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(current_level)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrder(struct Node* root, int* returnSize, int** returnColumnSizes) {
    if (root == NULL) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    const int MAX_NODES = 10005;               // per constraints
    struct Node **queue = (struct Node **)malloc(MAX_NODES * sizeof(struct Node *));
    int front = 0, back = 0;

    queue[back++] = root;

    int **result = (int **)malloc(MAX_NODES * sizeof(int *));
    int *colSizes = (int *)malloc(MAX_NODES * sizeof(int));
    int levelCount = 0;

    while (front < back) {
        int levelSize = back - front;
        int *levelVals = (int *)malloc(levelSize * sizeof(int));

        for (int i = 0; i < levelSize; ++i) {
            struct Node *node = queue[front++];
            levelVals[i] = node->val;

            for (int j = 0; j < node->numChildren; ++j) {
                queue[back++] = node->children[j];
            }
        }

        result[levelCount] = levelVals;
        colSizes[levelCount] = levelSize;
        ++levelCount;
    }

    free(queue);
    *returnSize = levelCount;
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, IList<Node> _children) {
        val = _val;
        children = _children;
    }
}
*/

public class Solution {
    public IList<IList<int>> LevelOrder(Node root) {
        var result = new List<IList<int>>();
        if (root == null) return result;

        var queue = new Queue<Node>();
        queue.Enqueue(root);

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            var currentLevel = new List<int>(levelSize);
            for (int i = 0; i < levelSize; i++) {
                Node node = queue.Dequeue();
                currentLevel.Add(node.val);
                if (node.children != null) {
                    foreach (var child in node.children) {
                        if (child != null) {
                            queue.Enqueue(child);
                        }
                    }
                }
            }
            result.Add(currentLevel);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (!root) return [];
    const result = [];
    let queue = [root];
    
    while (queue.length) {
        const nextQueue = [];
        const levelVals = [];
        
        for (const node of queue) {
            levelVals.push(node.val);
            if (node.children && node.children.length) {
                for (const child of node.children) {
                    if (child) nextQueue.push(child);
                }
            }
        }
        
        result.push(levelVals);
        queue = nextQueue;
    }
    
    return result;
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     children: _Node[]
 *     
 *     constructor(v: number) {
 *         this.val = v;
 *         this.children = [];
 *     }
 * }
 */

function levelOrder(root: _Node | null): number[][] {
    const res: number[][] = [];
    if (!root) return res;

    let queue: _Node[] = [root];

    while (queue.length > 0) {
        const nextLevel: _Node[] = [];
        const levelVals: number[] = [];

        for (const node of queue) {
            levelVals.push(node.val);
            if (node.children && node.children.length > 0) {
                for (const child of node.children) {
                    nextLevel.push(child);
                }
            }
        }

        res.push(levelVals);
        queue = nextLevel;
    }

    return res;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $children = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->children = array();
 *     }
 * }
 */
class Solution {
    /**
     * @param Node $root
     * @return integer[][]
     */
    function levelOrder($root) {
        if ($root === null) {
            return [];
        }
        $result = [];
        $queue = new SplQueue();
        $queue->enqueue($root);
        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $level = [];
            for ($i = 0; $i < $size; $i++) {
                $node = $queue->dequeue();
                $level[] = $node->val;
                if (!empty($node->children)) {
                    foreach ($node->children as $child) {
                        if ($child !== null) {
                            $queue->enqueue($child);
                        }
                    }
                }
            }
            $result[] = $level;
        }
        return $result;
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var children: [Node]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.children = []
 *     }
 * }
 */

class Solution {
    func levelOrder(_ root: Node?) -> [[Int]] {
        guard let root = root else { return [] }
        var result: [[Int]] = []
        var queue: [Node] = [root]
        var index = 0
        
        while index < queue.count {
            let levelCount = queue.count - index
            var currentLevel: [Int] = []
            for _ in 0..<levelCount {
                let node = queue[index]
                index += 1
                currentLevel.append(node.val)
                queue.append(contentsOf: node.children)
            }
            result.append(currentLevel)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun levelOrder(root: Node?): List<List<Int>> {
        if (root == null) return emptyList()
        val result = mutableListOf<MutableList<Int>>()
        val queue: ArrayDeque<Node> = ArrayDeque()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val size = queue.size
            val level = mutableListOf<Int>()
            repeat(size) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                for (child in node.children) {
                    if (child != null) {
                        queue.add(child)
                    }
                }
            }
            result.add(level)
        }
        return result
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
	if root == nil {
		return [][]int{}
	}
	var result [][]int
	queue := []*Node{root}
	for len(queue) > 0 {
		levelSize := len(queue)
		levelVals := make([]int, 0, levelSize)
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]
			levelVals = append(levelVals, node.Val)
			if len(node.Children) > 0 {
				queue = append(queue, node.Children...)
			}
		}
		result = append(result, levelVals)
	}
	return result
}
```

## Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :children
#     def initialize(val)
#         @val = val
#         @children = []
#     end
# end

def level_order(root)
  return [] if root.nil?
  result = []
  queue = [root]
  until queue.empty?
    level_size = queue.size
    current_level = []
    level_size.times do
      node = queue.shift
      current_level << node.val
      node.children.each { |child| queue << child }
    end
    result << current_level
  end
  result
end
```

## Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var children: List[Node] = List()
 * }
 */

object Solution {
  def levelOrder(root: Node): List[List[Int]] = {
    if (root == null) return Nil

    val result = scala.collection.mutable.ListBuffer[List[Int]]()
    val queue = scala.collection.mutable.Queue[Node]()
    queue.enqueue(root)

    while (queue.nonEmpty) {
      val size = queue.size
      val level = scala.collection.mutable.ListBuffer[Int]()

      for (_ <- 0 until size) {
        val node = queue.dequeue()
        level += node.value
        if (node.children != null) {
          node.children.foreach(queue.enqueue(_))
        }
      }

      result += level.toList
    }

    result.toList
  }
}
```
