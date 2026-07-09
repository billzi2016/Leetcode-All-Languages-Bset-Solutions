# 2196. Create Binary Tree From Descriptions

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
    TreeNode* createBinaryTree(std::vector<std::vector<int>>& descriptions) {
        std::unordered_map<int, TreeNode*> nodeMap;
        std::unordered_set<int> children;
        
        for (const auto& d : descriptions) {
            int parentVal = d[0];
            int childVal  = d[1];
            int isLeft    = d[2];
            
            if (!nodeMap.count(parentVal)) {
                nodeMap[parentVal] = new TreeNode(parentVal);
            }
            if (!nodeMap.count(childVal)) {
                nodeMap[childVal] = new TreeNode(childVal);
            }
            
            if (isLeft) {
                nodeMap[parentVal]->left = nodeMap[childVal];
            } else {
                nodeMap[parentVal]->right = nodeMap[childVal];
            }
            children.insert(childVal);
        }
        
        for (const auto& kv : nodeMap) {
            if (!children.count(kv.first)) {
                return kv.second;
            }
        }
        return nullptr; // Should never reach here per problem constraints
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodeMap = new HashMap<>();
        Set<Integer> children = new HashSet<>();

        for (int[] d : descriptions) {
            int parentVal = d[0];
            int childVal = d[1];
            boolean isLeft = d[2] == 1;

            TreeNode parentNode = nodeMap.computeIfAbsent(parentVal, v -> new TreeNode(v));
            TreeNode childNode = nodeMap.computeIfAbsent(childVal, v -> new TreeNode(v));

            if (isLeft) {
                parentNode.left = childNode;
            } else {
                parentNode.right = childNode;
            }

            children.add(childVal);
        }

        for (int val : nodeMap.keySet()) {
            if (!children.contains(val)) {
                return nodeMap.get(val);
            }
        }
        return null; // Should never reach here as per problem constraints
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
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        node_map = {}
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)
            
            parent_node = node_map[parent_val]
            child_node = node_map[child_val]
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child_val)
        
        for val, node in node_map.items():
            if val not in children:
                return node
        
        return None
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)
            
            parent_node = node_map[parent_val]
            child_node = node_map[child_val]
            
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child_val)
        
        for val, node in node_map.items():
            if val not in children:
                return node
        return None
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
static struct TreeNode* newNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct TreeNode* createBinaryTree(int** descriptions, int descriptionsSize, int* descriptionsColSize) {
    const int MAX_VAL = 100000;               // per constraints
    struct TreeNode **nodeArr = (struct TreeNode**)calloc(MAX_VAL + 1, sizeof(struct TreeNode*));
    char *isChild = (char*)calloc(MAX_VAL + 1, sizeof(char));

    for (int i = 0; i < descriptionsSize; ++i) {
        int parent = descriptions[i][0];
        int child  = descriptions[i][1];
        int isLeft = descriptions[i][2];

        if (!nodeArr[parent])
            nodeArr[parent] = newNode(parent);
        if (!nodeArr[child])
            nodeArr[child] = newNode(child);

        if (isLeft)
            nodeArr[parent]->left = nodeArr[child];
        else
            nodeArr[parent]->right = nodeArr[child];

        isChild[child] = 1;
    }

    struct TreeNode* root = NULL;
    for (int i = 0; i <= MAX_VAL; ++i) {
        if (nodeArr[i] && !isChild[i]) {
            root = nodeArr[i];
            break;
        }
    }

    free(nodeArr);
    free(isChild);
    return root;
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
    public TreeNode CreateBinaryTree(int[][] descriptions) {
        var nodeMap = new Dictionary<int, TreeNode>();
        var children = new HashSet<int>();

        foreach (var d in descriptions) {
            int parentVal = d[0];
            int childVal = d[1];
            int isLeft = d[2];

            if (!nodeMap.TryGetValue(parentVal, out var parentNode)) {
                parentNode = new TreeNode(parentVal);
                nodeMap[parentVal] = parentNode;
            }

            if (!nodeMap.TryGetValue(childVal, out var childNode)) {
                childNode = new TreeNode(childVal);
                nodeMap[childVal] = childNode;
            }

            if (isLeft == 1) {
                parentNode.left = childNode;
            } else {
                parentNode.right = childNode;
            }

            children.Add(childVal);
        }

        foreach (var kvp in nodeMap) {
            if (!children.Contains(kvp.Key)) {
                return kvp.Value;
            }
        }

        return null; // Should never reach here as per problem constraints
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
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
    const nodeMap = new Map(); // value -> TreeNode
    const children = new Set();

    for (const [parentVal, childVal, isLeft] of descriptions) {
        if (!nodeMap.has(parentVal)) {
            nodeMap.set(parentVal, new TreeNode(parentVal));
        }
        if (!nodeMap.has(childVal)) {
            nodeMap.set(childVal, new TreeNode(childVal));
        }

        const parentNode = nodeMap.get(parentVal);
        const childNode = nodeMap.get(childVal);

        if (isLeft === 1) {
            parentNode.left = childNode;
        } else {
            parentNode.right = childNode;
        }
        children.add(childVal);
    }

    // Find root: a node that never appears as a child
    for (const [val, node] of nodeMap.entries()) {
        if (!children.has(val)) {
            return node;
        }
    }
    return null; // should not happen per problem constraints
};
```

## Typescript

```typescript
function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const nodes = new Map<number, TreeNode>();
    const children = new Set<number>();

    for (const [parentVal, childVal, isLeft] of descriptions) {
        let parentNode = nodes.get(parentVal);
        if (!parentNode) {
            parentNode = new TreeNode(parentVal);
            nodes.set(parentVal, parentNode);
        }
        let childNode = nodes.get(childVal);
        if (!childNode) {
            childNode = new TreeNode(childVal);
            nodes.set(childVal, childNode);
        }
        if (isLeft === 1) {
            parentNode.left = childNode;
        } else {
            parentNode.right = childNode;
        }
        children.add(childVal);
    }

    for (const [val, node] of nodes.entries()) {
        if (!children.has(val)) {
            return node;
        }
    }
    return null;
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
     * @param Integer[][] $descriptions
     * @return TreeNode
     */
    function createBinaryTree($descriptions) {
        $nodeMap = [];   // value => TreeNode
        $children = [];  // set of child values

        foreach ($descriptions as $desc) {
            [$parentVal, $childVal, $isLeft] = $desc;

            if (!isset($nodeMap[$parentVal])) {
                $nodeMap[$parentVal] = new TreeNode($parentVal);
            }
            if (!isset($nodeMap[$childVal])) {
                $nodeMap[$childVal] = new TreeNode($childVal);
            }

            $parentNode = $nodeMap[$parentVal];
            $childNode  = $nodeMap[$childVal];

            if ($isLeft == 1) {
                $parentNode->left = $childNode;
            } else {
                $parentNode->right = $childNode;
            }

            $children[$childVal] = true;
        }

        foreach ($nodeMap as $val => $node) {
            if (!isset($children[$val])) {
                return $node; // root found
            }
        }

        return null; // should never happen per problem constraints
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
    func createBinaryTree(_ descriptions: [[Int]]) -> TreeNode? {
        var nodeMap = [Int: TreeNode]()
        var childSet = Set<Int>()
        
        for desc in descriptions {
            let parentVal = desc[0]
            let childVal = desc[1]
            let isLeft = desc[2] == 1
            
            let parentNode: TreeNode
            if let existing = nodeMap[parentVal] {
                parentNode = existing
            } else {
                parentNode = TreeNode(parentVal)
                nodeMap[parentVal] = parentNode
            }
            
            let childNode: TreeNode
            if let existing = nodeMap[childVal] {
                childNode = existing
            } else {
                childNode = TreeNode(childVal)
                nodeMap[childVal] = childNode
            }
            
            if isLeft {
                parentNode.left = childNode
            } else {
                parentNode.right = childNode
            }
            
            childSet.insert(childVal)
        }
        
        for (val, node) in nodeMap where !childSet.contains(val) {
            return node
        }
        return nil
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
    fun createBinaryTree(descriptions: Array<IntArray>): TreeNode? {
        val nodeMap = HashMap<Int, TreeNode>()
        val children = HashSet<Int>()

        for (desc in descriptions) {
            val parentVal = desc[0]
            val childVal = desc[1]
            val isLeft = desc[2] == 1

            val parentNode = nodeMap.getOrPut(parentVal) { TreeNode(parentVal) }
            val childNode = nodeMap.getOrPut(childVal) { TreeNode(childVal) }

            if (isLeft) {
                parentNode.left = childNode
            } else {
                parentNode.right = childNode
            }

            children.add(childVal)
        }

        for ((value, node) in nodeMap) {
            if (!children.contains(value)) {
                return node
            }
        }
        return null
    }
}
```

## Dart

```dart
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
  TreeNode? createBinaryTree(List<List<int>> descriptions) {
    final Map<int, TreeNode> nodeMap = {};
    final Set<int> children = {};

    for (final desc in descriptions) {
      final int parentVal = desc[0];
      final int childVal = desc[1];
      final int isLeft = desc[2];

      final TreeNode parentNode =
          nodeMap.putIfAbsent(parentVal, () => TreeNode(parentVal));
      final TreeNode childNode =
          nodeMap.putIfAbsent(childVal, () => TreeNode(childVal));

      if (isLeft == 1) {
        parentNode.left = childNode;
      } else {
        parentNode.right = childNode;
      }

      children.add(childVal);
    }

    for (final entry in nodeMap.entries) {
      if (!children.contains(entry.key)) {
        return entry.value;
      }
    }
    return null; // Should never happen per problem constraints
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
func createBinaryTree(descriptions [][]int) *TreeNode {
    nodeMap := make(map[int]*TreeNode)
    children := make(map[int]bool)

    for _, d := range descriptions {
        parentVal, childVal, isLeft := d[0], d[1], d[2]

        parentNode, ok := nodeMap[parentVal]
        if !ok {
            parentNode = &TreeNode{Val: parentVal}
            nodeMap[parentVal] = parentNode
        }

        childNode, ok := nodeMap[childVal]
        if !ok {
            childNode = &TreeNode{Val: childVal}
            nodeMap[childVal] = childNode
        }

        if isLeft == 1 {
            parentNode.Left = childNode
        } else {
            parentNode.Right = childNode
        }
        children[childVal] = true
    }

    var root *TreeNode
    for val, node := range nodeMap {
        if !children[val] {
            root = node
            break
        }
    }
    return root
}
```

## Ruby

```ruby
require 'set'

def create_binary_tree(descriptions)
  node_map = {}
  children = Set.new

  descriptions.each do |parent_val, child_val, is_left|
    parent_node = (node_map[parent_val] ||= TreeNode.new(parent_val))
    child_node  = (node_map[child_val]  ||= TreeNode.new(child_val))

    if is_left == 1
      parent_node.left = child_node
    else
      parent_node.right = child_node
    end

    children.add(child_val)
  end

  root_val = node_map.keys.find { |val| !children.include?(val) }
  node_map[root_val]
end
```

## Scala

```scala
object Solution {
  def createBinaryTree(descriptions: Array[Array[Int]]): TreeNode = {
    import scala.collection.mutable.{HashMap, HashSet}
    val nodeMap = HashMap[Int, TreeNode]()
    val childSet = HashSet[Int]()

    for (desc <- descriptions) {
      val parentVal = desc(0)
      val childVal = desc(1)
      val isLeft = desc(2) == 1

      val parentNode = nodeMap.getOrElseUpdate(parentVal, new TreeNode(parentVal))
      val childNode = nodeMap.getOrElseUpdate(childVal, new TreeNode(childVal))

      if (isLeft) parentNode.left = childNode else parentNode.right = childNode
      childSet.add(childVal)
    }

    val rootVal = nodeMap.keys.find(v => !childSet.contains(v)).get
    nodeMap(rootVal)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut children: HashSet<i32> = HashSet::new();

        for desc in descriptions.iter() {
            let parent_val = desc[0];
            let child_val = desc[1];
            let is_left = desc[2] == 1;

            let parent_node = nodes
                .entry(parent_val)
                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(parent_val))))
                .clone();
            let child_node = nodes
                .entry(child_val)
                .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(child_val))))
                .clone();

            if is_left {
                parent_node.borrow_mut().left = Some(child_node.clone());
            } else {
                parent_node.borrow_mut().right = Some(child_node.clone());
            }

            children.insert(child_val);
        }

        // Find the root (node that never appears as a child)
        let root_val = *nodes
            .keys()
            .find(|&&v| !children.contains(&v))
            .unwrap();

        nodes.get(&root_val).cloned()
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

(define/contract (create-binary-tree descriptions)
  (-> (listof (listof exact-integer?)) (or/c tree-node? #f))
  (let ((node-map (make-hash))
        (children-set (make-hash)))
    ;; helper to obtain existing node or create a new one
    (define (get-or-create val)
      (if (hash-has-key? node-map val)
          (hash-ref node-map val)
          (let ((n (make-tree-node val)))
            (hash-set! node-map val n)
            n)))
    ;; build the tree connections
    (for ([desc descriptions])
      (match desc
        [(list parent child isLeft)
         (define parent-node (get-or-create parent))
         (define child-node  (get-or-create child))
         (if (= isLeft 1)
             (set-tree-node-left!  parent-node child-node)
             (set-tree-node-right! parent-node child-node))
         (hash-set! children-set child #t)]))
    ;; locate the root (node never appearing as a child)
    (let ((root #f))
      (for ([k (in-hash-keys node-map)])
        (when (and (not root) (not (hash-has-key? children-set k)))
          (set! root (hash-ref node-map k))))
      root)))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                     left = null :: 'null' | #tree_node{},
                     right = null :: 'null' | #tree_node{}}).

-spec create_binary_tree(Descriptions :: [[integer()]]) -> #tree_node{} | null.
create_binary_tree(Descriptions) ->
    {NodeMap, ChildSet} =
        lists:foldl(
          fun([Parent, Child, IsLeft], {M0, C0}) ->
                  M1 = case maps:is_key(Parent, M0) of
                           true -> M0;
                           false -> maps:put(Parent, #tree_node{val = Parent}, M0)
                       end,
                  M2 = case maps:is_key(Child, M1) of
                           true -> M1;
                           false -> maps:put(Child, #tree_node{val = Child}, M1)
                       end,
                  ParentNode = maps:get(Parent, M2),
                  ChildNode  = maps:get(Child, M2),
                  UpdatedParent =
                      if IsLeft == 1 ->
                              ParentNode#tree_node{left = ChildNode};
                         true ->
                              ParentNode#tree_node{right = ChildNode}
                      end,
                  M3 = maps:put(Parent, UpdatedParent, M2),
                  {M3, maps:put(Child, true, C0)}
          end,
          {maps:new(), maps:new()},
          Descriptions),

    RootVals = [V || V <- maps:keys(NodeMap), not maps:is_key(V, ChildSet)],
    case RootVals of
        [RootVal | _] -> maps:get(RootVal, NodeMap);
        [] -> null
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec create_binary_tree(descriptions :: [[integer]]) :: TreeNode.t() | nil
  def create_binary_tree(descriptions) do
    {node_map, children_set} =
      Enum.reduce(descriptions, {%{}, MapSet.new()}, fn [parent_val, child_val, is_left], {nm, cs} ->
        parent_node = Map.get(nm, parent_val, %TreeNode{val: parent_val})
        child_node = Map.get(nm, child_val, %TreeNode{val: child_val})

        updated_parent =
          if is_left == 1 do
            %{parent_node | left: child_node}
          else
            %{parent_node | right: child_node}
          end

        nm2 = nm |> Map.put(parent_val, updated_parent) |> Map.put(child_val, child_node)
        cs2 = MapSet.put(cs, child_val)

        {nm2, cs2}
      end)

    root_key =
      Enum.find(Map.keys(node_map), fn k -> not MapSet.member?(children_set, k) end)

    case root_key do
      nil -> nil
      _ -> Map.get(node_map, root_key)
    end
  end
end
```
