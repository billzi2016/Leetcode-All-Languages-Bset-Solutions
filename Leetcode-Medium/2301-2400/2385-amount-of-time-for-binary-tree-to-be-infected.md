# 2385. Amount of Time for Binary Tree to Be Infected

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
    int amountOfTime(TreeNode* root, int start) {
        if (!root) return 0;
        unordered_map<int, vector<int>> adj;
        // Build undirected graph
        function<void(TreeNode*, TreeNode*)> dfs = [&](TreeNode* node, TreeNode* parent){
            if (!node) return;
            if (parent) {
                adj[node->val].push_back(parent->val);
                adj[parent->val].push_back(node->val);
            }
            if (node->left) dfs(node->left, node);
            if (node->right) dfs(node->right, node);
        };
        dfs(root, nullptr);
        
        // BFS from start
        queue<int> q;
        unordered_set<int> visited;
        q.push(start);
        visited.insert(start);
        int minutes = -1;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; ++i) {
                int cur = q.front(); q.pop();
                for (int nb : adj[cur]) {
                    if (!visited.count(nb)) {
                        visited.insert(nb);
                        q.push(nb);
                    }
                }
            }
            ++minutes;
        }
        return minutes;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int amountOfTime(TreeNode root, int start) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(root, null, graph);
        
        Queue<Integer> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        queue.offer(start);
        visited.add(start);
        int minutes = -1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int node = queue.poll();
                for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
                    if (visited.add(neighbor)) {
                        queue.offer(neighbor);
                    }
                }
            }
            minutes++;
        }
        return minutes;
    }
    
    private void buildGraph(TreeNode node, TreeNode parent, Map<Integer, List<Integer>> graph) {
        if (node == null) return;
        graph.computeIfAbsent(node.val, k -> new ArrayList<>());
        if (parent != null) {
            graph.get(node.val).add(parent.val);
            graph.get(parent.val).add(node.val);
        }
        buildGraph(node.left, node, graph);
        buildGraph(node.right, node, graph);
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
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        from collections import deque

        # Build undirected graph representation of the tree
        adj = {}
        stack = [(root, None)]
        while stack:
            node, parent_val = stack.pop()
            if not node:
                continue
            val = node.val
            if val not in adj:
                adj[val] = []
            if parent_val is not None:
                adj[val].append(parent_val)
                adj[parent_val].append(val)
            if node.left:
                stack.append((node.left, val))
            if node.right:
                stack.append((node.right, val))

        # BFS from the start node to find the farthest distance
        q = deque([start])
        visited = {start}
        minutes = -1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for nb in adj.get(cur, []):
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            minutes += 1

        return minutes
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
    def amountOfTime(self, root: Optional['TreeNode'], start: int) -> int:
        if not root:
            return 0

        graph = {}

        # Build undirected graph using DFS recursion
        import sys
        sys.setrecursionlimit(200000)

        def build(node, parent):
            if not node:
                return
            val = node.val
            if val not in graph:
                graph[val] = []
            if parent is not None:
                pval = parent.val
                graph[val].append(pval)
                graph[pval].append(val)
            build(node.left, node)
            build(node.right, node)

        build(root, None)

        # BFS from start to find max distance
        visited = set([start])
        q = deque([start])
        minutes = -1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for nb in graph.get(cur, []):
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            minutes += 1

        return minutes
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

static int maxDist;

static int dfs(struct TreeNode* node, int start) {
    if (!node) return 0;                     // empty subtree
    int left = dfs(node->left, start);
    int right = dfs(node->right, start);

    if (node->val == start) {                // found the start node
        maxDist = left > right ? left : right;
        return -1;                           // mark presence of start with negative depth
    }

    if (left >= 0 && right >= 0) {           // start not in this subtree
        int curDepth = (left > right ? left : right) + 1;
        return curDepth;
    } else {                                 // one side contains the start node
        int dist = (left < 0 ? -left : left) + (right < 0 ? -right : right);
        if (dist > maxDist) maxDist = dist;
        int curDepth = (left < right ? left : right) - 1; // propagate negative distance upward
        return curDepth;
    }
}

int amountOfTime(struct TreeNode* root, int start) {
    maxDist = 0;
    dfs(root, start);
    return maxDist;
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
    private void BuildGraph(TreeNode node, TreeNode parent, Dictionary<int, List<int>> graph) {
        if (node == null) return;

        if (!graph.ContainsKey(node.val))
            graph[node.val] = new List<int>();

        if (parent != null) {
            // ensure parent entry exists
            if (!graph.ContainsKey(parent.val))
                graph[parent.val] = new List<int>();
            graph[node.val].Add(parent.val);
            graph[parent.val].Add(node.val);
        }

        BuildGraph(node.left, node, graph);
        BuildGraph(node.right, node, graph);
    }

    public int AmountOfTime(TreeNode root, int start) {
        var graph = new Dictionary<int, List<int>>();
        BuildGraph(root, null, graph);

        var queue = new Queue<int>();
        var visited = new HashSet<int>();

        queue.Enqueue(start);
        visited.Add(start);

        int minutes = -1;
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                int cur = queue.Dequeue();
                foreach (var nb in graph[cur]) {
                    if (!visited.Contains(nb)) {
                        visited.Add(nb);
                        queue.Enqueue(nb);
                    }
                }
            }
            minutes++;
        }

        return minutes;
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
 * @param {number} start
 * @return {number}
 */
var amountOfTime = function(root, start) {
    if (!root) return 0;
    
    // Build undirected graph using adjacency list
    const adj = new Map(); // val -> array of neighbor vals
    
    const stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (!adj.has(node.val)) adj.set(node.val, []);
        
        if (node.left) {
            // ensure entries exist
            if (!adj.has(node.left.val)) adj.set(node.left.val, []);
            adj.get(node.val).push(node.left.val);
            adj.get(node.left.val).push(node.val);
            stack.push(node.left);
        }
        if (node.right) {
            if (!adj.has(node.right.val)) adj.set(node.right.val, []);
            adj.get(node.val).push(node.right.val);
            adj.get(node.right.val).push(node.val);
            stack.push(node.right);
        }
    }
    
    // BFS from start node to find max distance
    const visited = new Set();
    const queue = [start];
    visited.add(start);
    let minutes = -1;
    for (let idx = 0; idx < queue.length;) {
        const levelSize = queue.length - idx;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[idx++];
            const neighbors = adj.get(cur) || [];
            for (const nb of neighbors) {
                if (!visited.has(nb)) {
                    visited.add(nb);
                    queue.push(nb);
                }
            }
        }
        minutes++;
    }
    
    return minutes;
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

function amountOfTime(root: TreeNode | null, start: number): number {
    if (!root) return 0;

    // Build undirected graph representation of the tree
    const adj = new Map<number, number[]>();
    const stack: [TreeNode, TreeNode | null][] = [[root, null]];
    while (stack.length) {
        const [node, parent] = stack.pop()!;
        if (!adj.has(node.val)) adj.set(node.val, []);
        if (parent) {
            adj.get(node.val)!.push(parent.val);
            adj.get(parent.val)!.push(node.val);
        }
        if (node.left) stack.push([node.left, node]);
        if (node.right) stack.push([node.right, node]);
    }

    // BFS from start to find maximum distance
    const visited = new Set<number>();
    const dist = new Map<number, number>();
    const queue: number[] = [];

    visited.add(start);
    dist.set(start, 0);
    queue.push(start);

    let maxDist = 0;
    let idx = 0;
    while (idx < queue.length) {
        const cur = queue[idx++];
        const curDist = dist.get(cur)!;
        const neighbors = adj.get(cur) ?? [];
        for (const nb of neighbors) {
            if (!visited.has(nb)) {
                visited.add(nb);
                const nd = curDist + 1;
                dist.set(nb, nd);
                maxDist = Math.max(maxDist, nd);
                queue.push(nb);
            }
        }
    }

    return maxDist;
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
    private $graph = [];

    /**
     * @param TreeNode $root
     * @param Integer $start
     * @return Integer
     */
    function amountOfTime($root, $start) {
        if ($root === null) return 0;
        $this->buildGraph($root, null);
        $queue = new SplQueue();
        $queue->enqueue([$start, 0]);
        $visited = [];
        $visited[$start] = true;
        $maxDist = 0;

        while (!$queue->isEmpty()) {
            [$nodeVal, $dist] = $queue->dequeue();
            if ($dist > $maxDist) $maxDist = $dist;
            if (!isset($this->graph[$nodeVal])) continue;
            foreach ($this->graph[$nodeVal] as $nei) {
                if (!isset($visited[$nei])) {
                    $visited[$nei] = true;
                    $queue->enqueue([$nei, $dist + 1]);
                }
            }
        }

        return $maxDist;
    }

    private function buildGraph($node, $parent) {
        if ($node === null) return;
        $val = $node->val;
        if (!isset($this->graph[$val])) $this->graph[$val] = [];

        if ($parent !== null) {
            $pVal = $parent->val;
            // add edge both ways
            $this->graph[$val][] = $pVal;
            $this->graph[$pVal][] = $val;
        }

        $this->buildGraph($node->left, $node);
        $this->buildGraph($node->right, $node);
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
    func amountOfTime(_ root: TreeNode?, _ start: Int) -> Int {
        guard let root = root else { return 0 }
        
        // Build undirected graph from the binary tree
        var graph = [Int: [Int]]()
        func addEdge(_ u: Int, _ v: Int) {
            graph[u, default: []].append(v)
            graph[v, default: []].append(u)
        }
        
        var stack: [TreeNode] = [root]
        while let node = stack.popLast() {
            if let left = node.left {
                addEdge(node.val, left.val)
                stack.append(left)
            }
            if let right = node.right {
                addEdge(node.val, right.val)
                stack.append(right)
            }
        }
        
        // BFS from start node to find maximum distance
        var visited = Set<Int>()
        var queue: [Int] = []
        var head = 0
        
        visited.insert(start)
        queue.append(start)
        var minutes = -1
        
        while head < queue.count {
            let levelSize = queue.count - head
            for _ in 0..<levelSize {
                let cur = queue[head]
                head += 1
                if let neighbors = graph[cur] {
                    for nb in neighbors where !visited.contains(nb) {
                        visited.insert(nb)
                        queue.append(nb)
                    }
                }
            }
            minutes += 1
        }
        
        return minutes
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
    fun amountOfTime(root: TreeNode?, start: Int): Int {
        if (root == null) return 0

        val adj = HashMap<Int, MutableList<Int>>()

        fun build(node: TreeNode?, parent: Int?) {
            if (node == null) return
            val v = node.`val`
            adj.getOrPut(v) { mutableListOf() }
            if (parent != null) {
                adj[v]!!.add(parent)
                adj[parent]!!.add(v)
            }
            build(node.left, v)
            build(node.right, v)
        }

        build(root, null)

        val visited = HashSet<Int>()
        val queue: ArrayDeque<Int> = ArrayDeque()
        queue.add(start)
        visited.add(start)

        var minutes = -1
        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) {
                val cur = queue.removeFirst()
                for (nbr in adj[cur]!!) {
                    if (!visited.contains(nbr)) {
                        visited.add(nbr)
                        queue.addLast(nbr)
                    }
                }
            }
            minutes++
        }

        return minutes
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
  int amountOfTime(TreeNode? root, int start) {
    if (root == null) return 0;

    // Build undirected graph from the binary tree.
    final Map<int, List<int>> adj = {};
    final Queue<TreeNode> q = Queue();
    q.add(root);
    while (q.isNotEmpty) {
      final node = q.removeFirst();
      adj.putIfAbsent(node.val, () => []);
      if (node.left != null) {
        adj[node.val]!.add(node.left!.val);
        adj.putIfAbsent(node.left!.val, () => []).add(node.val);
        q.add(node.left!);
      }
      if (node.right != null) {
        adj[node.val]!.add(node.right!.val);
        adj.putIfAbsent(node.right!.val, () => []).add(node.val);
        q.add(node.right!);
      }
    }

    // BFS from start node to find maximum distance.
    final Set<int> visited = {start};
    final Queue<int> bfs = Queue();
    bfs.add(start);
    int minutes = -1;
    while (bfs.isNotEmpty) {
      int levelSize = bfs.length;
      for (int i = 0; i < levelSize; i++) {
        int cur = bfs.removeFirst();
        for (int nb in adj[cur] ?? []) {
          if (!visited.contains(nb)) {
            visited.add(nb);
            bfs.add(nb);
          }
        }
      }
      minutes++;
    }

    return minutes;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
func amountOfTime(root *TreeNode, start int) int {
	if root == nil {
		return 0
	}
	graph := make(map[int][]int)
	var build func(node *TreeNode, parent int)
	build = func(node *TreeNode, parent int) {
		if node == nil {
			return
		}
		if _, ok := graph[node.Val]; !ok {
			graph[node.Val] = []int{}
		}
		if parent != -1 {
			graph[node.Val] = append(graph[node.Val], parent)
			graph[parent] = append(graph[parent], node.Val)
		}
		build(node.Left, node.Val)
		build(node.Right, node.Val)
	}
	build(root, -1)

	queue := []int{start}
	visited := map[int]bool{start: true}
	minutes := -1
	for len(queue) > 0 {
		levelSize := len(queue)
		for i := 0; i < levelSize; i++ {
			cur := queue[0]
			queue = queue[1:]
			for _, nb := range graph[cur] {
				if !visited[nb] {
					visited[nb] = true
					queue = append(queue, nb)
				}
			}
		}
		minutes++
	}
	return minutes
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

def amount_of_time(root, start)
  graph = Hash.new { |h, k| h[k] = [] }

  build = lambda do |node, parent|
    return unless node
    if parent
      graph[node.val] << parent.val
      graph[parent.val] << node.val
    end
    build.call(node.left, node) if node.left
    build.call(node.right, node) if node.right
  end

  build.call(root, nil)

  visited = {}
  queue = [[start, 0]]
  visited[start] = true
  max_dist = 0

  until queue.empty?
    cur, dist = queue.shift
    max_dist = dist if dist > max_dist
    graph[cur].each do |nbr|
      next if visited[nbr]
      visited[nbr] = true
      queue << [nbr, dist + 1]
    end
  end

  max_dist
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
  def amountOfTime(root: TreeNode, start: Int): Int = {
    import scala.collection.mutable.{HashMap, HashSet}
    // Map each node value to its parent node
    val parent = new HashMap[Int, TreeNode]()
    var startNode: TreeNode = null

    // Iterative DFS to fill parent map and locate the start node
    val stack = new java.util.ArrayDeque[TreeNode]()
    stack.push(root)
    while (!stack.isEmpty) {
      val node = stack.pop()
      if (node.value == start) startNode = node
      if (node.left != null) {
        parent(node.left.value) = node
        stack.push(node.left)
      }
      if (node.right != null) {
        parent(node.right.value) = node
        stack.push(node.right)
      }
    }

    // BFS from the start node to compute the maximum distance
    val visited = new HashSet[Int]()
    val queue = new java.util.ArrayDeque[TreeNode]()
    queue.offer(startNode)
    visited.add(startNode.value)

    var minutes = -1
    while (!queue.isEmpty) {
      val levelSize = queue.size()
      for (_ <- 0 until levelSize) {
        val cur = queue.poll()
        // left child
        if (cur.left != null && !visited.contains(cur.left.value)) {
          visited.add(cur.left.value)
          queue.offer(cur.left)
        }
        // right child
        if (cur.right != null && !visited.contains(cur.right.value)) {
          visited.add(cur.right.value)
          queue.offer(cur.right)
        }
        // parent
        parent.get(cur.value).foreach { p =>
          if (!visited.contains(p.value)) {
            visited.add(p.value)
            queue.offer(p)
          }
        }
      }
      minutes += 1
    }

    minutes
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque, HashSet};

impl Solution {
    pub fn amount_of_time(root: Option<Rc<RefCell<TreeNode>>>, start: i32) -> i32 {
        // Build undirected graph from the binary tree
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut stack: Vec<(Rc<RefCell<TreeNode>>, Option<i32>)> = Vec::new();

        if let Some(rc) = root {
            stack.push((rc, None));
        }

        while let Some((node_rc, parent_opt)) = stack.pop() {
            let node_ref = node_rc.borrow();
            let val = node_ref.val;
            graph.entry(val).or_insert(Vec::new());

            if let Some(p) = parent_opt {
                graph.get_mut(&val).unwrap().push(p);
                graph.get_mut(&p).unwrap().push(val);
            }

            if let Some(left_rc) = node_ref.left.clone() {
                stack.push((left_rc, Some(val)));
            }
            if let Some(right_rc) = node_ref.right.clone() {
                stack.push((right_rc, Some(val)));
            }
        }

        // BFS from the start node to find the farthest distance
        let mut visited: HashSet<i32> = HashSet::new();
        let mut queue: VecDeque<i32> = VecDeque::new();

        visited.insert(start);
        queue.push_back(start);

        let mut minutes: i32 = -1;
        while !queue.is_empty() {
            let level_size = queue.len();
            for _ in 0..level_size {
                if let Some(node) = queue.pop_front() {
                    if let Some(neighs) = graph.get(&node) {
                        for &nb in neighs {
                            if visited.insert(nb) {
                                queue.push_back(nb);
                            }
                        }
                    }
                }
            }
            minutes += 1;
        }

        minutes
    }
}
```

## Racket

```racket
(require racket/queue)

; Definition for a binary tree node.
#|
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define (add-edge! adj u v)
  (hash-update! adj u (lambda (lst) (cons v lst)) (list))
  (hash-update! adj v (lambda (lst) (cons u lst)) (list)))

(define/contract (amount-of-time root start)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (if (not root)
      0
      (let* ((adj (make-hash))
             (build
               (letrec ((b (lambda (node)
                             (when node
                               (define val (tree-node-val node))
                               (define l (tree-node-left node))
                               (define r (tree-node-right node))
                               (when l
                                 (add-edge! adj val (tree-node-val l))
                                 (b l))
                               (when r
                                 (add-edge! adj val (tree-node-val r))
                                 (b r))))))
                 b)))
        (build root)
        (let* ((visited (make-hash))
               (q (make-queue)))
          (hash-set! visited start #t)
          (enqueue! q start)
          (let loop ((minutes -1))
            (if (queue-empty? q)
                minutes
                (let ((level-size (queue-length q)))
                  (for ([i (in-range level-size)])
                    (define cur (dequeue! q))
                    (for ([nbr (hash-ref adj cur '())])
                      (unless (hash-has-key? visited nbr)
                        (hash-set! visited nbr #t)
                        (enqueue! q nbr))))
                  (loop (+ minutes 1)))))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec amount_of_time(Root :: #tree_node{} | null, Start :: integer()) -> integer().
amount_of_time(Root, Start) ->
    Graph = build(Root, undefined, #{}),
    bfs(Graph, Start).

%% Build undirected adjacency list from the binary tree.
build(null, _Parent, Map) ->
    Map;
build(Node, Parent, Map) ->
    Val = Node#tree_node.val,
    %% Ensure entry for current node exists
    Map1 = case maps:is_key(Val, Map) of
               true -> Map;
               false -> maps:put(Val, [], Map)
           end,
    {Map2, _} =
        case Parent of
            undefined ->
                {Map1, ok};
            _ ->
                AdjP = maps:get(Parent, Map1, []),
                AdjV = maps:get(Val, Map1, []),
                M1 = maps:put(Parent, [Val | AdjP], Map1),
                M2 = maps:put(Val, [Parent | AdjV], M1),
                {M2, ok}
        end,
    MapL = build(Node#tree_node.left, Val, Map2),
    build(Node#tree_node.right, Val, MapL).

%% Breadth‑first search to find the farthest distance from start.
bfs(Graph, Start) ->
    Q0 = queue:in(Start, queue:new()),
    Visited0 = #{Start => true},
    bfs_loop(Q0, Visited0, Graph, 0).

bfs_loop(Queue, _Visited, _Graph, Minutes) when queue:is_empty(Queue) ->
    Minutes - 1;   %% subtract the extra increment after last level
bfs_loop(Queue, Visited, Graph, Minutes) ->
    LevelCount = queue:len(Queue),
    {NewQueue, NewVisited} = process_level(LevelCount, Queue, Visited, Graph,
                                           queue:new(), Visited),
    bfs_loop(NewQueue, NewVisited, Graph, Minutes + 1).

%% Process all nodes of the current BFS level.
process_level(0, _OldQ, Visited, _Graph, AccQ, AccV) ->
    {AccQ, AccV};
process_level(N, OldQ, Visited, Graph, AccQ, AccV) ->
    {{value, Node}, RestQ} = queue:out(OldQ),
    Neighs = maps:get(Node, Graph, []),
    {QAfterNei, VAfterNei} =
        lists:foldl(fun(Nei, {QAcc, VAcc}) ->
                            case maps:is_key(Nei, VAcc) of
                                true -> {QAcc, VAcc};
                                false -> {queue:in(Nei, QAcc), VAcc#{Nei => true}}
                            end
                    end,
                    {AccQ, AccV},
                    Neighs),
    process_level(N - 1, RestQ, Visited, Graph, QAfterNei, VAfterNei).
```

## Elixir

```elixir
defmodule Solution do
  @spec amount_of_time(root :: TreeNode.t() | nil, start :: integer) :: integer
  def amount_of_time(nil, _start), do: 0

  def amount_of_time(root, start) do
    graph = build_graph(root, nil, %{})
    bfs(:queue.from_list([{start, 0}]), MapSet.new([start]), 0, graph)
  end

  # Build undirected adjacency list for the tree
  defp build_graph(nil, _parent, graph), do: graph

  defp build_graph(%TreeNode{val: v, left: l, right: r}, parent, graph) do
    graph = Map.put_new(graph, v, [])

    graph =
      if parent != nil do
        add_edge(graph, v, parent)
      else
        graph
      end

    graph
    |> build_graph(l, v)
    |> build_graph(r, v)
  end

  defp add_edge(g, a, b) do
    g = Map.update!(g, a, fn lst -> [b | lst] end)
    Map.update!(g, b, fn lst -> [a | lst] end)
  end

  # Breadth‑first search to find the farthest distance from start
  defp bfs(queue, visited, max_dist, graph) do
    case :queue.out(queue) do
      {:empty, _} ->
        max_dist

      {{:value, {node, dist}}, q} ->
        new_max = if dist > max_dist, do: dist, else: max_dist

        {new_queue, new_visited} =
          Enum.reduce(Map.get(graph, node, []), {q, visited}, fn neighbor,
                                                                {acc_q, acc_vis} ->
            if MapSet.member?(acc_vis, neighbor) do
              {acc_q, acc_vis}
            else
              {
                :queue.in({neighbor, dist + 1}, acc_q),
                MapSet.put(acc_vis, neighbor)
              }
            end
          end)

        bfs(new_queue, new_visited, new_max, graph)
    end
  end
end
```
