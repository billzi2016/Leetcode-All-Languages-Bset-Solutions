# 0863. All Nodes Distance K in Binary Tree

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
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<TreeNode*, TreeNode*> parent;
        function<void(TreeNode*, TreeNode*)> dfs = [&](TreeNode* node, TreeNode* par){
            if (!node) return;
            parent[node] = par;
            dfs(node->left, node);
            dfs(node->right, node);
        };
        dfs(root, nullptr);
        
        unordered_set<TreeNode*> visited;
        queue<pair<TreeNode*, int>> q;
        q.push({target, 0});
        visited.insert(target);
        vector<int> ans;
        
        while (!q.empty()) {
            auto [node, dist] = q.front(); q.pop();
            if (dist == k) {
                ans.push_back(node->val);
            } else if (dist < k) {
                if (node->left && !visited.count(node->left)) {
                    visited.insert(node->left);
                    q.push({node->left, dist + 1});
                }
                if (node->right && !visited.count(node->right)) {
                    visited.insert(node->right);
                    q.push({node->right, dist + 1});
                }
                TreeNode* p = parent[node];
                if (p && !visited.count(p)) {
                    visited.insert(p);
                    q.push({p, dist + 1});
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

public class Solution {
    /**
     * Definition for a binary tree node.
     */
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    private void buildParentMap(TreeNode node, TreeNode parent, Map<TreeNode, TreeNode> map) {
        if (node == null) return;
        map.put(node, parent);
        buildParentMap(node.left, node, map);
        buildParentMap(node.right, node, map);
    }

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        buildParentMap(root, null, parent);

        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> visited = new HashSet<>();

        queue.offer(target);
        visited.add(target);
        int dist = 0;

        while (!queue.isEmpty()) {
            if (dist == k) break;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = queue.poll();
                TreeNode p = parent.get(cur);
                if (p != null && visited.add(p)) queue.offer(p);
                if (cur.left != null && visited.add(cur.left)) queue.offer(cur.left);
                if (cur.right != null && visited.add(cur.right)) queue.offer(cur.right);
            }
            dist++;
        }

        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            result.add(queue.poll().val);
        }
        return result;
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
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        # Build parent pointers for each node
        parent = {}
        stack = [(root, None)]
        while stack:
            node, par = stack.pop()
            if not node:
                continue
            parent[node] = par
            stack.append((node.left, node))
            stack.append((node.right, node))

        # BFS from target
        from collections import deque
        q = deque([(target, 0)])
        visited = {target}
        res = []
        while q:
            node, d = q.popleft()
            if d == k:
                res.append(node.val)
            elif d < k:
                for nxt in (node.left, node.right, parent.get(node)):
                    if nxt and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d + 1))
        return res
```

## Python3

```python
from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> List[int]:
        if not root:
            return []
        
        # Build parent pointers for each node.
        parent = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # BFS from target.
        visited = {target}
        q = deque([target])
        dist = 0
        
        while q and dist < k:
            for _ in range(len(q)):
                cur = q.popleft()
                for nxt in (cur.left, cur.right, parent.get(cur)):
                    if nxt and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            dist += 1
        
        return [node.val for node in q]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static void dfs(struct TreeNode* node, struct TreeNode* parent,
                struct TreeNode** parMap) {
    if (!node) return;
    parMap[node->val] = parent;
    dfs(node->left, node, parMap);
    dfs(node->right, node, parMap);
}

int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize) {
    // map from node value to its parent pointer (values are unique and <= 500)
    struct TreeNode* parent[501] = {0};
    dfs(root, NULL, parent);
    
    bool visited[501] = {false};
    typedef struct {
        struct TreeNode* node;
        int dist;
    } QueueItem;
    
    // maximum possible nodes is 500
    QueueItem queue[600];
    int head = 0, tail = 0;
    
    queue[tail++] = (QueueItem){target, 0};
    visited[target->val] = true;
    
    int* result = (int*)malloc(sizeof(int) * 500);
    int cnt = 0;
    
    while (head < tail) {
        QueueItem cur = queue[head++];
        if (cur.dist == k) {
            result[cnt++] = cur.node->val;
            continue; // do not expand further from this node
        }
        struct TreeNode* neighbors[3];
        int ncnt = 0;
        if (cur.node->left)  neighbors[ncnt++] = cur.node->left;
        if (cur.node->right) neighbors[ncnt++] = cur.node->right;
        struct TreeNode* p = parent[cur.node->val];
        if (p)               neighbors[ncnt++] = p;
        for (int i = 0; i < ncnt; ++i) {
            struct TreeNode* nxt = neighbors[i];
            if (!visited[nxt->val]) {
                visited[nxt->val] = true;
                queue[tail++] = (QueueItem){nxt, cur.dist + 1};
            }
        }
    }
    
    *returnSize = cnt;
    return result;
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
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public IList<int> DistanceK(TreeNode root, TreeNode target, int k) {
        var parent = new Dictionary<TreeNode, TreeNode>();
        void Dfs(TreeNode node, TreeNode par) {
            if (node == null) return;
            parent[node] = par;
            Dfs(node.left, node);
            Dfs(node.right, node);
        }
        Dfs(root, null);

        var result = new List<int>();
        var queue = new Queue<(TreeNode node, int dist)>();
        var visited = new HashSet<TreeNode>();

        queue.Enqueue((target, 0));
        visited.Add(target);

        while (queue.Count > 0) {
            var (node, dist) = queue.Dequeue();
            if (dist == k) {
                result.Add(node.val);
            } else if (dist < k) {
                TreeNode[] neighbors = { node.left, node.right, parent[node] };
                foreach (var nb in neighbors) {
                    if (nb != null && !visited.Contains(nb)) {
                        visited.Add(nb);
                        queue.Enqueue((nb, dist + 1));
                    }
                }
            }
        }

        return result;
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
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */
var distanceK = function(root, target, k) {
    const parentMap = new Map();
    
    // DFS to record each node's parent
    const dfs = (node, parent) => {
        if (!node) return;
        if (parent) parentMap.set(node, parent);
        dfs(node.left, node);
        dfs(node.right, node);
    };
    dfs(root, null);
    
    const result = [];
    const visited = new Set();
    const queue = [[target, 0]];
    visited.add(target);
    
    while (queue.length) {
        const [node, dist] = queue.shift();
        if (dist === k) {
            result.push(node.val);
            continue; // nodes at this distance are collected; no need to go deeper from them
        }
        if (dist > k) break;
        
        const neighbors = [];
        if (node.left) neighbors.push(node.left);
        if (node.right) neighbors.push(node.right);
        const parent = parentMap.get(node);
        if (parent) neighbors.push(parent);
        
        for (const nb of neighbors) {
            if (!visited.has(nb)) {
                visited.add(nb);
                queue.push([nb, dist + 1]);
            }
        }
    }
    
    return result;
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

function distanceK(root: TreeNode | null, target: TreeNode | null, k: number): number[] {
    if (!root || !target) return [];

    const parentMap = new Map<TreeNode, TreeNode | null>();

    const dfs = (node: TreeNode | null, parent: TreeNode | null): void => {
        if (!node) return;
        parentMap.set(node, parent);
        dfs(node.left, node);
        dfs(node.right, node);
    };
    dfs(root, null);

    const result: number[] = [];
    const visited = new Set<TreeNode>();
    const queue: [TreeNode, number][] = [];

    visited.add(target);
    queue.push([target, 0]);

    while (queue.length) {
        const [node, dist] = queue.shift()!;
        if (dist === k) {
            result.push(node.val);
            continue;
        }
        const neighbors: (TreeNode | null)[] = [
            node.left,
            node.right,
            parentMap.get(node) ?? null
        ];
        for (const nb of neighbors) {
            if (nb && !visited.has(nb)) {
                visited.add(nb);
                queue.push([nb, dist + 1]);
            }
        }
    }

    return result;
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
 *     function __construct($value) { $this->val = $value; }
 * }
 */
class Solution {
    /**
     * @param TreeNode $root
     * @param TreeNode $target
     * @param Integer $k
     * @return Integer[]
     */
    function distanceK($root, $target, $k) {
        if ($root === null) return [];

        // Build adjacency list graph: node value => array of neighbor values
        $graph = [];
        $this->buildGraph($root, $graph);

        $start = $target->val;
        if ($k == 0) return [$start];

        $queue = new SplQueue();
        $visited = [];

        $queue->enqueue([$start, 0]);
        $visited[$start] = true;

        while (!$queue->isEmpty()) {
            list($nodeVal, $dist) = $queue->dequeue();

            if ($dist == $k) {
                // collect this node and all remaining nodes at same distance
                $result = [$nodeVal];
                while (!$queue->isEmpty()) {
                    $next = $queue->dequeue();
                    $result[] = $next[0];
                }
                return $result;
            }

            if (!isset($graph[$nodeVal])) continue;

            foreach ($graph[$nodeVal] as $nei) {
                if (!isset($visited[$nei])) {
                    $visited[$nei] = true;
                    $queue->enqueue([$nei, $dist + 1]);
                }
            }
        }

        return [];
    }

    private function buildGraph($node, &$graph) {
        if ($node === null) return;

        $val = $node->val;
        if (!isset($graph[$val])) $graph[$val] = [];

        if ($node->left !== null) {
            $lVal = $node->left->val;
            $graph[$val][] = $lVal;
            if (!isset($graph[$lVal])) $graph[$lVal] = [];
            $graph[$lVal][] = $val;
            $this->buildGraph($node->left, $graph);
        }

        if ($node->right !== null) {
            $rVal = $node->right->val;
            $graph[$val][] = $rVal;
            if (!isset($graph[$rVal])) $graph[$rVal] = [];
            $graph[$rVal][] = $val;
            $this->buildGraph($node->right, $graph);
        }
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
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        guard let root = root, let target = target else { return [] }
        var graph = [ObjectIdentifier: [TreeNode]]()
        
        func addEdge(_ a: TreeNode, _ b: TreeNode) {
            let idA = ObjectIdentifier(a)
            graph[idA, default: []].append(b)
            let idB = ObjectIdentifier(b)
            graph[idB, default: []].append(a)
        }
        
        func dfs(_ node: TreeNode?, _ parent: TreeNode?) {
            guard let node = node else { return }
            if let p = parent {
                addEdge(node, p)
            }
            dfs(node.left, node)
            dfs(node.right, node)
        }
        
        dfs(root, nil)
        
        var result = [Int]()
        var visited = Set<ObjectIdentifier>()
        var queue: [(TreeNode, Int)] = []
        queue.append((target, 0))
        visited.insert(ObjectIdentifier(target))
        
        while !queue.isEmpty {
            let (node, dist) = queue.removeFirst()
            if dist == k {
                result.append(node.val)
            } else if dist < k {
                for neighbor in graph[ObjectIdentifier(node), default: []] {
                    let nid = ObjectIdentifier(neighbor)
                    if !visited.contains(nid) {
                        visited.insert(nid)
                        queue.append((neighbor, dist + 1))
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): List<Int> {
        val parentMap = HashMap<TreeNode, TreeNode?>()
        fun build(node: TreeNode?, parent: TreeNode?) {
            if (node == null) return
            parentMap[node] = parent
            build(node.left, node)
            build(node.right, node)
        }
        build(root, null)

        val visited = HashSet<TreeNode>()
        val queue: ArrayDeque<Pair<TreeNode, Int>> = ArrayDeque()
        if (target != null) {
            queue.add(Pair(target, 0))
            visited.add(target)
        }

        val result = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val (node, dist) = queue.removeFirst()
            if (dist == k) {
                result.add(node.`val`)
            } else if (dist < k) {
                node.left?.let {
                    if (visited.add(it)) queue.add(Pair(it, dist + 1))
                }
                node.right?.let {
                    if (visited.add(it)) queue.add(Pair(it, dist + 1))
                }
                parentMap[node]?.let { p ->
                    if (p != null && visited.add(p)) {
                        queue.add(Pair(p, dist + 1))
                    }
                }
            }
        }
        return result
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
func distanceK(root *TreeNode, target *TreeNode, k int) []int {
    parent := make(map[*TreeNode]*TreeNode)
    var dfs func(node *TreeNode)
    dfs = func(node *TreeNode) {
        if node == nil {
            return
        }
        if node.Left != nil {
            parent[node.Left] = node
            dfs(node.Left)
        }
        if node.Right != nil {
            parent[node.Right] = node
            dfs(node.Right)
        }
    }
    dfs(root)

    visited := make(map[*TreeNode]bool)
    queue := []*TreeNode{target}
    visited[target] = true
    dist := 0

    for len(queue) > 0 && dist < k {
        size := len(queue)
        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]

            if node.Left != nil && !visited[node.Left] {
                visited[node.Left] = true
                queue = append(queue, node.Left)
            }
            if node.Right != nil && !visited[node.Right] {
                visited[node.Right] = true
                queue = append(queue, node.Right)
            }
            if p, ok := parent[node]; ok && !visited[p] {
                visited[p] = true
                queue = append(queue, p)
            }
        }
        dist++
    }

    var res []int
    for _, node := range queue {
        res = append(res, node.Val)
    }
    return res
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

def distance_k(root, target, k)
  parent = {}
  stack = [[root, nil]]
  until stack.empty?
    node, par = stack.pop
    next if node.nil?
    parent[node] = par
    stack << [node.left, node]
    stack << [node.right, node]
  end

  queue = [[target, 0]]
  visited = { target => true }
  result = []

  until queue.empty?
    node, dist = queue.shift
    if dist == k
      result << node.val
    elsif dist < k
      [node.left, node.right, parent[node]].each do |nbr|
        next if nbr.nil? || visited[nbr]
        visited[nbr] = true
        queue << [nbr, dist + 1]
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{Queue, Set, Map, ListBuffer}
  def distanceK(root: TreeNode, target: TreeNode, k: Int): List[Int] = {
    val adj: Map[TreeNode, ListBuffer[TreeNode]] = Map()

    def addEdge(a: TreeNode, b: TreeNode): Unit = {
      adj.getOrElseUpdate(a, ListBuffer()) += b
    }

    def dfs(node: TreeNode): Unit = {
      if (node == null) return
      if (!adj.contains(node)) adj(node) = ListBuffer()
      if (node.left != null) {
        addEdge(node, node.left)
        addEdge(node.left, node)
        dfs(node.left)
      }
      if (node.right != null) {
        addEdge(node, node.right)
        addEdge(node.right, node)
        dfs(node.right)
      }
    }

    dfs(root)

    val visited: Set[TreeNode] = Set()
    val q: Queue[(TreeNode, Int)] = Queue()
    q.enqueue((target, 0))
    visited += target
    val res = ListBuffer[Int]()

    while (q.nonEmpty) {
      val (cur, d) = q.dequeue()
      if (d == k) {
        res += cur.value
      } else if (d < k) {
        for (nb <- adj.getOrElse(cur, ListBuffer())) {
          if (!visited.contains(nb)) {
            visited += nb
            q.enqueue((nb, d + 1))
          }
        }
      }
    }

    res.toList
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque, HashSet};

impl Solution {
    pub fn distance_k(root: Option<Rc<RefCell<TreeNode>>>, target: Option<Rc<RefCell<TreeNode>>>, k: i32) -> Vec<i32> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();

        fn build(node: &Option<Rc<RefCell<TreeNode>>>, graph: &mut HashMap<i32, Vec<i32>>) {
            if let Some(rc_node) = node {
                let val = rc_node.borrow().val;
                if let Some(left_rc) = &rc_node.borrow().left {
                    let left_val = left_rc.borrow().val;
                    graph.entry(val).or_default().push(left_val);
                    graph.entry(left_val).or_default().push(val);
                    build(&Some(Rc::clone(left_rc)), graph);
                }
                if let Some(right_rc) = &rc_node.borrow().right {
                    let right_val = right_rc.borrow().val;
                    graph.entry(val).or_default().push(right_val);
                    graph.entry(right_val).or_default().push(val);
                    build(&Some(Rc::clone(right_rc)), graph);
                }
            }
        }

        build(&root, &mut graph);

        let target_val = target.as_ref().unwrap().borrow().val;
        let mut visited: HashSet<i32> = HashSet::new();
        let mut queue: VecDeque<(i32, i32)> = VecDeque::new(); // (node value, distance)
        visited.insert(target_val);
        queue.push_back((target_val, 0));

        let mut result = Vec::new();

        while let Some((node_val, dist)) = queue.pop_front() {
            if dist == k {
                result.push(node_val);
                continue;
            }
            if let Some(neighbors) = graph.get(&node_val) {
                for &nbr in neighbors {
                    if visited.insert(nbr) {
                        queue.push_back((nbr, dist + 1));
                    }
                }
            }
        }

        result
    }
}
```
