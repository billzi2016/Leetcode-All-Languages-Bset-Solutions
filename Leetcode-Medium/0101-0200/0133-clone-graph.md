# 0133. Clone Graph

## Cpp

```cpp
#include <unordered_map>
#include <vector>
#include <functional>

/*
// Definition for a Node.
class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() : val(0), neighbors(std::vector<Node*>()) {}
    Node(int _val) : val(_val), neighbors(std::vector<Node*>()) {}
    Node(int _val, std::vector<Node*> _neighbors) : val(_val), neighbors(_neighbors) {}
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        std::unordered_map<Node*, Node*> cloned;
        std::function<Node*(Node*)> dfs = [&](Node* cur) -> Node* {
            if (cloned.count(cur)) return cloned[cur];
            Node* copy = new Node(cur->val);
            cloned[cur] = copy;
            for (Node* nb : cur->neighbors) {
                copy->neighbors.push_back(dfs(nb));
            }
            return copy;
        };
        return dfs(node);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        Map<Node, Node> clones = new HashMap<>();
        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);
        clones.put(node, new Node(node.val));
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            for (Node nei : cur.neighbors) {
                if (!clones.containsKey(nei)) {
                    clones.put(nei, new Node(nei.val));
                    queue.offer(nei);
                }
                clones.get(cur).neighbors.add(clones.get(nei));
            }
        }
        return clones.get(node);
    }
}
```

## Python

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        from collections import deque

        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])

        return old_to_new[node]
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {node: Node(node.val)}
        q = deque([node])
        
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numNeighbors;
 *     struct Node** neighbors;
 * };
 */

struct Node *cloneGraph(struct Node *s) {
    if (s == NULL) return NULL;

    struct Node *map[101];
    memset(map, 0, sizeof(map));

    /* Clone the starting node */
    struct Node *startClone = malloc(sizeof(struct Node));
    startClone->val = s->val;
    startClone->numNeighbors = s->numNeighbors;
    if (s->numNeighbors > 0) {
        startClone->neighbors = malloc(s->numNeighbors * sizeof(struct Node *));
        for (int i = 0; i < s->numNeighbors; ++i) startClone->neighbors[i] = NULL;
    } else {
        startClone->neighbors = NULL;
    }
    map[s->val] = startClone;

    struct Node *queue[101];
    int front = 0, back = 0;
    queue[back++] = s;

    while (front < back) {
        struct Node *node = queue[front++];
        struct Node *cloneNode = map[node->val];

        for (int i = 0; i < node->numNeighbors; ++i) {
            struct Node *nbr = node->neighbors[i];
            if (!map[nbr->val]) {
                /* Clone neighbor */
                struct Node *nbrClone = malloc(sizeof(struct Node));
                nbrClone->val = nbr->val;
                nbrClone->numNeighbors = nbr->numNeighbors;
                if (nbr->numNeighbors > 0) {
                    nbrClone->neighbors = malloc(nbr->numNeighbors * sizeof(struct Node *));
                    for (int k = 0; k < nbr->numNeighbors; ++k) nbrClone->neighbors[k] = NULL;
                } else {
                    nbrClone->neighbors = NULL;
                }
                map[nbr->val] = nbrClone;
                queue[back++] = nbr;
            }
            cloneNode->neighbors[i] = map[nbr->val];
        }
    }

    return startClone;
}
```

## Csharp

```csharp
using System.Collections.Generic;

/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> neighbors;

    public Node() {
        val = 0;
        neighbors = new List<Node>();
    }

    public Node(int _val) {
        val = _val;
        neighbors = new List<Node>();
    }

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

public class Solution {
    public Node CloneGraph(Node node) {
        if (node == null) return null;

        var cloneMap = new Dictionary<Node, Node>();
        var queue = new Queue<Node>();

        queue.Enqueue(node);
        cloneMap[node] = new Node(node.val);

        while (queue.Count > 0) {
            var current = queue.Dequeue();
            foreach (var neighbor in current.neighbors) {
                if (!cloneMap.ContainsKey(neighbor)) {
                    cloneMap[neighbor] = new Node(neighbor.val);
                    queue.Enqueue(neighbor);
                }
                cloneMap[current].neighbors.Add(cloneMap[neighbor]);
            }
        }

        return cloneMap[node];
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;
    
    const map = new Map(); // original node -> cloned node
    const queue = [node];
    map.set(node, new Node(node.val));
    
    while (queue.length) {
        const cur = queue.shift();
        for (const nei of cur.neighbors) {
            if (!map.has(nei)) {
                map.set(nei, new Node(nei.val));
                queue.push(nei);
            }
            map.get(cur).neighbors.push(map.get(nei));
        }
    }
    
    return map.get(node);
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 * 
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 * 
 */

function cloneGraph(node: _Node | null): _Node | null {
    if (!node) return null;
    const visited = new Map<_Node, _Node>();
    
    const dfs = (n: _Node): _Node => {
        if (visited.has(n)) return visited.get(n)!;
        const copy = new _Node(n.val);
        visited.set(n, copy);
        for (const nei of n.neighbors) {
            copy.neighbors.push(dfs(nei));
        }
        return copy;
    };
    
    return dfs(node);
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $neighbors = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->neighbors = array();
 *     }
 * }
 */

class Solution {
    /**
     * @param Node $node
     * @return Node
     */
    function cloneGraph($node) {
        if ($node === null) {
            return null;
        }

        $map = new SplObjectStorage(); // original node => cloned node
        $queue = [$node];

        $cloneRoot = new Node($node->val);
        $map[$node] = $cloneRoot;

        while (!empty($queue)) {
            $curr = array_shift($queue);
            foreach ($curr->neighbors as $nbr) {
                if (!$map->contains($nbr)) {
                    $clonedNbr = new Node($nbr->val);
                    $map[$nbr] = $clonedNbr;
                    $queue[] = $nbr;
                }
                // Append the cloned neighbor to the cloned current node's neighbors
                $map[$curr]->neighbors[] = $map[$nbr];
            }
        }

        return $cloneRoot;
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var neighbors: [Node?]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.neighbors = []
 *     }
 * }
 */

class Solution {
    func cloneGraph(_ node: Node?) -> Node? {
        guard let start = node else { return nil }
        var visited = [ObjectIdentifier: Node]()
        
        func dfs(_ n: Node) -> Node {
            let key = ObjectIdentifier(n)
            if let cloned = visited[key] {
                return cloned
            }
            let copy = Node(n.val)
            visited[key] = copy
            for neighbor in n.neighbors {
                if let nb = neighbor {
                    copy.neighbors.append(dfs(nb))
                } else {
                    copy.neighbors.append(nil)
                }
            }
            return copy
        }
        
        return dfs(start)
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var neighbors: ArrayList<Node?> = ArrayList<Node?>()
 * }
 */
class Solution {
    fun cloneGraph(node: Node?): Node? {
        if (node == null) return null
        val map = HashMap<Node, Node>()
        val queue: java.util.ArrayDeque<Node> = java.util.ArrayDeque()
        queue.add(node)
        map[node] = Node(node.`val`)
        while (!queue.isEmpty()) {
            val cur = queue.poll()
            for (nbr in cur.neighbors) {
                if (nbr == null) continue
                if (!map.containsKey(nbr)) {
                    map[nbr] = Node(nbr.`val`)
                    queue.add(nbr)
                }
                map[cur]?.neighbors?.add(map[nbr])
            }
        }
        return map[node]
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}
	cloneMap := make(map[*Node]*Node)
	queue := []*Node{node}
	cloneMap[node] = &Node{Val: node.Val}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		for _, nb := range cur.Neighbors {
			if _, exists := cloneMap[nb]; !exists {
				cloneMap[nb] = &Node{Val: nb.Val}
				queue = append(queue, nb)
			}
			cloneMap[cur].Neighbors = append(cloneMap[cur].Neighbors, cloneMap[nb])
		}
	}
	return cloneMap[node]
}
```

## Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :neighbors
#     def initialize(val = 0, neighbors = nil)
#         @val = val
#         neighbors = [] if neighbors.nil?
#         @neighbors = neighbors
#     end
# end

def cloneGraph(node)
  return nil if node.nil?

  cloned = {}
  queue = [node]
  cloned[node] = Node.new(node.val, [])

  until queue.empty?
    cur = queue.shift
    cur.neighbors.each do |nbr|
      unless cloned.key?(nbr)
        cloned[nbr] = Node.new(nbr.val, [])
        queue << nbr
      end
      cloned[cur].neighbors << cloned[nbr]
    end
  end

  cloned[node]
end
```

## Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var neighbors: List[Node] = List()
 * }
 */

object Solution {
  def cloneGraph(graph: Node): Node = {
    if (graph == null) return null

    import scala.collection.mutable.{Map, Queue}

    val nodeMap = Map.empty[Node, Node]
    val startCopy = new Node(graph.value)
    nodeMap.put(graph, startCopy)

    val q = Queue[Node]()
    q.enqueue(graph)

    while (q.nonEmpty) {
      val cur = q.dequeue()
      for (nbr <- cur.neighbors) {
        if (!nodeMap.contains(nbr)) {
          val nbrCopy = new Node(nbr.value)
          nodeMap.put(nbr, nbrCopy)
          q.enqueue(nbr)
        }
        // Append the cloned neighbor to the cloned current node's neighbors list
        val curClone = nodeMap(cur)
        curClone.neighbors = curClone.neighbors :+ nodeMap(nbr)
      }
    }

    startCopy
  }
}
```
