# 0919. Complete Binary Tree Inserter

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
class CBTInserter {
private:
    TreeNode* root_;
    std::queue<TreeNode*> candidates_;
public:
    CBTInserter(TreeNode* root) : root_(root) {
        std::queue<TreeNode*> bfs;
        bfs.push(root_);
        while (!bfs.empty()) {
            TreeNode* node = bfs.front();
            bfs.pop();
            if (node->left) bfs.push(node->left);
            if (node->right) bfs.push(node->right);
            if (!(node->left && node->right)) {
                candidates_.push(node);
            }
        }
    }
    
    int insert(int val) {
        TreeNode* child = new TreeNode(val);
        TreeNode* parent = candidates_.front();
        if (!parent->left) {
            parent->left = child;
        } else {
            parent->right = child;
            candidates_.pop(); // parent now has two children
        }
        candidates_.push(child); // new node may receive future children
        return parent->val;
    }
    
    TreeNode* get_root() {
        return root_;
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(val);
 * TreeNode* param_2 = obj->get_root();
 */
```

## Java

```java
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
class CBTInserter {
    private final TreeNode root;
    private final java.util.Queue<TreeNode> candidates;

    public CBTInserter(TreeNode root) {
        this.root = root;
        this.candidates = new java.util.LinkedList<>();
        java.util.Queue<TreeNode> bfs = new java.util.LinkedList<>();
        bfs.offer(root);
        while (!bfs.isEmpty()) {
            TreeNode node = bfs.poll();
            if (node.left != null) bfs.offer(node.left);
            if (node.right != null) bfs.offer(node.right);
            if (node.left == null || node.right == null) {
                candidates.offer(node);
            }
        }
    }

    public int insert(int val) {
        TreeNode parent = candidates.peek();
        TreeNode child = new TreeNode(val);
        if (parent.left == null) {
            parent.left = child;
        } else {
            parent.right = child;
            candidates.poll(); // parent now has two children
        }
        candidates.offer(child); // new node may receive future children
        return parent.val;
    }

    public TreeNode get_root() {
        return root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(val);
 * TreeNode param_2 = obj.get_root();
 */
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.root = root
        self.candidates = collections.deque()
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.candidates.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        new_node = TreeNode(val)
        parent = self.candidates[0]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.candidates.popleft()
        self.candidates.append(new_node)
        return parent.val

    def get_root(self):
        """
        :rtype: Optional[TreeNode]
        """
        return self.root
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

class CBTInserter:
    def __init__(self, root: Optional['TreeNode']):
        self.root = root
        self.q = deque()
        if not root:
            return
        bfs = deque([root])
        while bfs:
            node = bfs.popleft()
            if not node.left or not node.right:
                self.q.append(node)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.q[0]
        new_node = TreeNode(val)
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.q.popleft()
        self.q.append(new_node)
        return parent.val

    def get_root(self) -> Optional['TreeNode']:
        return self.root
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

typedef struct {
    struct TreeNode* root;
    struct TreeNode** q;   // candidate queue
    int front;             // index of current parent
    int back;              // next insertion position
    int cap;               // capacity of q
} CBTInserter;

CBTInserter* cBTInserterCreate(struct TreeNode* root) {
    CBTInserter* obj = (CBTInserter*)malloc(sizeof(CBTInserter));
    obj->root = root;
    obj->cap = 20000;                     // initial capacity, enough for constraints
    obj->q = (struct TreeNode**)malloc(obj->cap * sizeof(struct TreeNode*));
    obj->front = 0;
    obj->back = 0;

    // BFS to populate candidate queue
    struct TreeNode** bfs = (struct TreeNode**)malloc(obj->cap * sizeof(struct TreeNode*));
    int b_front = 0, b_back = 0;
    bfs[b_back++] = root;
    while (b_front < b_back) {
        struct TreeNode* node = bfs[b_front++];
        if (node->left) bfs[b_back++] = node->left;
        if (node->right) bfs[b_back++] = node->right;
        if (!(node->left && node->right)) {
            obj->q[obj->back++] = node;
        }
    }
    free(bfs);
    return obj;
}

int cBTInserterInsert(CBTInserter* obj, int val) {
    struct TreeNode* parent = obj->q[obj->front];
    struct TreeNode* child = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    child->val = val;
    child->left = NULL;
    child->right = NULL;

    if (!parent->left) {
        parent->left = child;
    } else {
        parent->right = child;
        obj->front++;  // parent now has two children
    }

    // ensure capacity for new candidate
    if (obj->back >= obj->cap) {
        int newCap = obj->cap * 2;
        obj->q = (struct TreeNode**)realloc(obj->q, newCap * sizeof(struct TreeNode*));
        obj->cap = newCap;
    }
    obj->q[obj->back++] = child;

    return parent->val;
}

struct TreeNode* cBTInserterGet_root(CBTInserter* obj) {
    return obj->root;
}

void cBTInserterFree(CBTInserter* obj) {
    if (obj) {
        free(obj->q);
        free(obj);
    }
}

/**
 * Your CBTInserter struct will be instantiated and called as such:
 * CBTInserter* obj = cBTInserterCreate(root);
 * int param_1 = cBTInserterInsert(obj, val);
 *
 * struct TreeNode* param_2 = cBTInserterGet_root(obj);
 *
 * cBTInserterFree(obj);
 */
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
public class CBTInserter
{
    private readonly TreeNode _root;
    private readonly Queue<TreeNode> _candidates;

    public CBTInserter(TreeNode root)
    {
        _root = root;
        _candidates = new Queue<TreeNode>();
        var bfs = new Queue<TreeNode>();
        bfs.Enqueue(root);
        while (bfs.Count > 0)
        {
            var node = bfs.Dequeue();
            if (node.left != null) bfs.Enqueue(node.left);
            if (node.right != null) bfs.Enqueue(node.right);
            if (node.left == null || node.right == null)
                _candidates.Enqueue(node);
        }
    }

    public int Insert(int val)
    {
        var parent = _candidates.Peek();
        var child = new TreeNode(val);
        if (parent.left == null)
        {
            parent.left = child;
        }
        else
        {
            parent.right = child;
            // parent now has two children, remove it from candidates
            _candidates.Dequeue();
        }
        // the new node may receive future children
        _candidates.Enqueue(child);
        return parent.val;
    }

    public TreeNode Get_root()
    {
        return _root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.Insert(val);
 * TreeNode param_2 = obj.Get_root();
 */
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
 */
var CBTInserter = function(root) {
    this.root = root;
    this.candidates = [];
    const bfsQueue = [root];
    while (bfsQueue.length) {
        const node = bfsQueue.shift();
        if (!node.left || !node.right) {
            this.candidates.push(node);
        }
        if (node.left) bfsQueue.push(node.left);
        if (node.right) bfsQueue.push(node.right);
    }
};

/** 
 * @param {number} val
 * @return {number}
 */
CBTInserter.prototype.insert = function(val) {
    const newNode = new TreeNode(val);
    const parent = this.candidates[0];
    if (!parent.left) {
        parent.left = newNode;
    } else {
        parent.right = newNode;
        // parent now has two children, remove it from candidates
        this.candidates.shift();
    }
    // new node may receive future children
    this.candidates.push(newNode);
    return parent.val;
};

/**
 * @return {TreeNode}
 */
CBTInserter.prototype.get_root = function() {
    return this.root;
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

class CBTInserter {
    private root: TreeNode | null;
    private queue: TreeNode[];
    private idx: number;

    constructor(root: TreeNode | null) {
        this.root = root;
        this.queue = [];
        this.idx = 0;
        if (!root) return;
        const bfs: TreeNode[] = [root];
        while (bfs.length) {
            const node = bfs.shift()!;
            if (!node.left || !node.right) {
                this.queue.push(node);
            }
            if (node.left) bfs.push(node.left);
            if (node.right) bfs.push(node.right);
        }
    }

    insert(val: number): number {
        const parent = this.queue[this.idx];
        const newNode = new TreeNode(val);
        if (!parent.left) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
            this.idx++;
        }
        this.queue.push(newNode);
        return parent.val;
    }

    get_root(): TreeNode | null {
        return this.root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(val)
 * var param_2 = obj.get_root()
 */
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
class CBTInserter {
    private $root;
    private $queue; // SplQueue of nodes with missing children

    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        $this->root = $root;
        $this->queue = new SplQueue();

        $bfs = new SplQueue();
        $bfs->enqueue($root);
        while (!$bfs->isEmpty()) {
            $node = $bfs->dequeue();
            if ($node->left !== null) {
                $bfs->enqueue($node->left);
            }
            if ($node->right !== null) {
                $bfs->enqueue($node->right);
            }
            // If node is missing a child, add to queue
            if (!($node->left && $node->right)) {
                $this->queue->enqueue($node);
            }
        }
    }

    /**
     * @param Integer $val
     * @return Integer
     */
    function insert($val) {
        $newNode = new TreeNode($val);
        $parent = $this->queue->top(); // node with the smallest index that has a missing child

        if ($parent->left === null) {
            $parent->left = $newNode;
        } else {
            $parent->right = $newNode;
            // parent now has two children, remove it from queue
            $this->queue->dequeue();
        }

        // new node may receive future children
        $this->queue->enqueue($newNode);
        return $parent->val;
    }

    /**
     * @return TreeNode
     */
    function get_root() {
        return $this->root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * $obj = new CBTInserter($root);
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->get_root();
 */
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

class CBTInserter {
    private var root: TreeNode?
    private var candidates: [TreeNode] = []
    private var idx: Int = 0

    init(_ root: TreeNode?) {
        self.root = root
        var bfs: [TreeNode] = []
        if let r = root {
            bfs.append(r)
        }
        var i = 0
        while i < bfs.count {
            let node = bfs[i]
            i += 1
            if node.left == nil || node.right == nil {
                candidates.append(node)
            }
            if let left = node.left {
                bfs.append(left)
            }
            if let right = node.right {
                bfs.append(right)
            }
        }
    }

    func insert(_ val: Int) -> Int {
        // Ensure idx points to a node that still has a missing child
        while idx < candidates.count && candidates[idx].left != nil && candidates[idx].right != nil {
            idx += 1
        }
        let parent = candidates[idx]
        let newNode = TreeNode(val)
        if parent.left == nil {
            parent.left = newNode
        } else {
            parent.right = newNode
        }
        candidates.append(newNode)
        return parent.val
    }

    func get_root() -> TreeNode? {
        return root
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * let obj = CBTInserter(root)
 * let ret_1: Int = obj.insert(val)
 * let ret_2: TreeNode? = obj.get_root()
 */
```

## Kotlin

```kotlin
import java.util.ArrayDeque

/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class CBTInserter(root: TreeNode?) {

    private val root: TreeNode? = root
    private val deque: ArrayDeque<TreeNode> = ArrayDeque()

    init {
        if (root != null) {
            val bfs: ArrayDeque<TreeNode> = ArrayDeque()
            bfs.add(root)
            while (!bfs.isEmpty()) {
                val node = bfs.poll()
                if (node.left == null || node.right == null) {
                    deque.add(node)
                }
                node.left?.let { bfs.add(it) }
                node.right?.let { bfs.add(it) }
            }
        }
    }

    fun insert(`val`: Int): Int {
        val newNode = TreeNode(`val`)
        val parent = deque.peek()
        if (parent != null) {
            if (parent.left == null) {
                parent.left = newNode
            } else {
                parent.right = newNode
                deque.poll() // parent now has two children
            }
            deque.add(newNode)
            return parent.`val`
        }
        // Should not reach here as per problem constraints
        return -1
    }

    fun get_root(): TreeNode? {
        return root
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = CBTInserter(root)
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.get_root()
 */
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
class CBTInserter {
  TreeNode? _root;
  final Queue<TreeNode> _candidates = Queue<TreeNode>();

  CBTInserter(TreeNode? root) {
    _root = root;
    if (root == null) return;
    final Queue<TreeNode> bfs = Queue<TreeNode>();
    bfs.add(root);
    while (bfs.isNotEmpty) {
      TreeNode node = bfs.removeFirst();
      if (node.left != null) bfs.add(node.left!);
      if (node.right != null) bfs.add(node.right!);
      if (node.left == null || node.right == null) {
        _candidates.add(node);
      }
    }
  }

  int insert(int val) {
    TreeNode parent = _candidates.first;
    TreeNode child = TreeNode(val);
    if (parent.left == null) {
      parent.left = child;
    } else {
      parent.right = child;
      // parent now has two children, remove it from candidates
      _candidates.removeFirst();
    }
    // new node may receive future children
    _candidates.add(child);
    return parent.val;
  }

  TreeNode? get_root() {
    return _root;
  }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = CBTInserter(root);
 * int param1 = obj.insert(val);
 * TreeNode? param2 = obj.get_root();
 */
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
type CBTInserter struct {
	root  *TreeNode
	queue []*TreeNode // nodes with missing children, in BFS order
	idx   int         // points to the first node in queue that can receive a child
}

func Constructor(root *TreeNode) CBTInserter {
	q := []*TreeNode{}
	bfs := []*TreeNode{root}
	for len(bfs) > 0 {
		node := bfs[0]
		bfs = bfs[1:]

		if node.Left != nil {
			bfs = append(bfs, node.Left)
		}
		if node.Right != nil {
			bfs = append(bfs, node.Right)
		}
		if node.Left == nil || node.Right == nil {
			q = append(q, node)
		}
	}
	return CBTInserter{root: root, queue: q, idx: 0}
}

func (this *CBTInserter) Insert(val int) int {
	newNode := &TreeNode{Val: val}
	parent := this.queue[this.idx]

	if parent.Left == nil {
		parent.Left = newNode
	} else {
		parent.Right = newNode
		this.idx++
	}
	this.queue = append(this.queue, newNode)
	return parent.Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(val);
 * param_2 := obj.Get_root();
 */
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

class CBTInserter
  def initialize(root)
    @root = root
    @queue = []
    bfs = [root]
    i = 0
    while i < bfs.length
      node = bfs[i]
      i += 1
      if node.left
        bfs << node.left
      end
      if node.right
        bfs << node.right
      end
      if node.left.nil? || node.right.nil?
        @queue << node
      end
    end
  end

  def insert(val)
    parent = @queue.first
    new_node = TreeNode.new(val)
    if parent.left.nil?
      parent.left = new_node
    else
      parent.right = new_node
      @queue.shift
    end
    @queue << new_node
    parent.val
  end

  def get_root
    @root
  end
end
```

## Scala

```scala
import scala.collection.mutable.Queue

/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
class CBTInserter(_root: TreeNode) {

  private val root: TreeNode = _root
  private val candidates: Queue[TreeNode] = Queue()

  // Initialize the candidate queue with nodes that have less than two children
  {
    val bfs: Queue[TreeNode] = Queue()
    bfs.enqueue(root)
    while (bfs.nonEmpty) {
      val node = bfs.dequeue()
      if (node.left != null) bfs.enqueue(node.left)
      if (node.right != null) bfs.enqueue(node.right)
      if (node.left == null || node.right == null) candidates.enqueue(node)
    }
  }

  def insert(`val`: Int): Int = {
    val parent = candidates.head
    val newNode = new TreeNode(`val`)
    if (parent.left == null) {
      parent.left = newNode
    } else {
      parent.right = newNode
      // Parent now has two children, remove it from candidates
      candidates.dequeue()
    }
    // New node may receive future children
    candidates.enqueue(newNode)
    parent.value
  }

  def get_root(): TreeNode = root
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * val obj = new CBTInserter(root)
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.get_root()
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::rc::Rc;
use std::collections::VecDeque;

/// Definition for a binary tree node.
/// #[derive(Debug, PartialEq, Eq)]
/// pub struct TreeNode {
///   pub val: i32,
///   pub left: Option<Rc<RefCell<TreeNode>>>,
///   pub right: Option<Rc<RefCell<TreeNode>>>,
/// }
///
/// impl TreeNode {
///   #[inline]
///   pub fn new(val: i32) -> Self {
///     TreeNode {
///       val,
///       left: None,
///       right: None
///     }
///   }
/// }

pub struct CBTInserter {
    root: Option<Rc<RefCell<TreeNode>>>,
    deque: VecDeque<Rc<RefCell<TreeNode>>>,
}

impl CBTInserter {
    pub fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut deque = VecDeque::new();
        if let Some(r) = root.clone() {
            let mut bfs = VecDeque::new();
            bfs.push_back(r.clone());
            while let Some(node) = bfs.pop_front() {
                let left_opt = node.borrow().left.clone();
                let right_opt = node.borrow().right.clone();

                if left_opt.is_none() || right_opt.is_none() {
                    deque.push_back(node.clone());
                }
                if let Some(l) = left_opt {
                    bfs.push_back(l);
                }
                if let Some(r) = right_opt {
                    bfs.push_back(r);
                }
            }
        }
        CBTInserter { root, deque }
    }

    pub fn insert(&mut self, val: i32) -> i32 {
        // parent is always at front
        let parent_rc = self.deque.front().unwrap().clone();
        let new_node = Rc::new(RefCell::new(TreeNode::new(val)));

        {
            let mut parent_ref = parent_rc.borrow_mut();
            if parent_ref.left.is_none() {
                parent_ref.left = Some(new_node.clone());
            } else {
                parent_ref.right = Some(new_node.clone());
                // parent now has two children, remove it from deque
                self.deque.pop_front();
            }
        }

        // new node may receive future children
        self.deque.push_back(new_node);
        parent_rc.borrow().val
    }

    pub fn get_root(&self) -> Option<Rc<RefCell<TreeNode>>> {
        self.root.clone()
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(define cbt-inserter%
  (class object%
    (init-field root)

    ;; internal queue to store incomplete nodes in BFS order
    (define front '())
    (define rear '())

    (define (ensure-front)
      (when (null? front)
        (set! front (reverse rear))
        (set! rear '())))

    (define (queue-empty?) (and (null? front) (null? rear)))

    (define (queue-peek)
      (ensure-front)
      (car front))

    (define (dequeue!)
      (ensure-front)
      (let ((elem (car front)))
        (set! front (cdr front))
        elem))

    (define (enqueue! x)
      (set! rear (cons x rear)))

    ;; preprocessing: BFS to populate queue with nodes that have <2 children
    (when root
      (let bfs ((lst (list root)))
        (unless (null? lst)
          (define node (car lst))
          (when (or (not (tree-node-left node)) (not (tree-node-right node)))
            (enqueue! node))
          (define children
            (filter identity (list (tree-node-left node) (tree-node-right node))))
          (bfs (append (cdr lst) children)))))

    ;; insert a new value into the CBT and return parent value
    (define/public (insert val)
      (define newnode (make-tree-node val))
      (define parent (queue-peek))
      (if (not (tree-node-left parent))
          (set-tree-node-left! parent newnode)
          (begin
            (set-tree-node-right! parent newnode)
            (dequeue!))) ; parent now has two children, remove it
      (enqueue! newnode)
      (tree-node-val parent))

    ;; return the root of the tree
    (define/public (get_root) root)

    (super-new)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec cbt_inserter_init_(Root :: #tree_node{} | null) -> any().
cbt_inserter_init_(Root) ->
    Arr = tree_to_array(Root),
    put(arr, Arr).

-spec cbt_inserter_insert(Val :: integer()) -> integer().
cbt_inserter_insert(Val) ->
    Arr = get(arr),
    N = length(Arr),
    ParentIdx = (N - 1) div 2,
    ParentVal = lists:nth(ParentIdx + 1, Arr),
    NewArr = Arr ++ [Val],
    put(arr, NewArr),
    ParentVal.

-spec cbt_inserter_get_root() -> #tree_node{} | null.
cbt_inserter_get_root() ->
    Arr = get(arr),
    build_tree(Arr, 0).

%% Helper: convert tree to level-order array (list of values)
tree_to_array(null) -> [];
tree_to_array(Root) ->
    bfs([Root], []).

bfs([], Acc) ->
    lists:reverse(Acc);
bfs([null | Rest], Acc) ->
    bfs(Rest, Acc);
bfs([Node | Rest], Acc) ->
    Val = Node#tree_node.val,
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    NewQueue = Rest ++ (case Left of null -> []; _ -> [Left] end)
                     ++ (case Right of null -> []; _ -> [Right] end),
    bfs(NewQueue, [Val | Acc]).

%% Helper: build tree from level-order array
build_tree(Arr, Index) ->
    Len = length(Arr),
    if
        Index >= Len -> null;
        true ->
            Val = lists:nth(Index + 1, Arr),
            Left = build_tree(Arr, 2 * Index + 1),
            Right = build_tree(Arr, 2 * Index + 2),
            #tree_node{val = Val, left = Left, right = Right}
    end.
```

## Elixir

```elixir
defmodule CBTInserter do
  @spec init_(root :: TreeNode.t | nil) :: any
  def init_(root) do
    vals = bfs_collect(root)
    Process.put(:cbt_vals, vals)
  end

  @spec insert(val :: integer) :: integer
  def insert(val) do
    vals = Process.get(:cbt_vals, [])
    parent_idx = div(length(vals) - 1, 2)
    parent_val = Enum.at(vals, parent_idx)
    Process.put(:cbt_vals, vals ++ [val])
    parent_val
  end

  @spec get_root() :: TreeNode.t | nil
  def get_root() do
    vals = Process.get(:cbt_vals, [])
    build_tree(vals, 0)
  end

  # Helper to collect node values in level-order
  defp bfs_collect(nil), do: []

  defp bfs_collect(root) do
    queue = :queue.from_list([root])
    traverse(queue, [])
  end

  defp traverse(q, acc) do
    case :queue.out(q) do
      {:empty, _} ->
        Enum.reverse(acc)

      {{:value, node}, q2} ->
        acc1 = [node.val | acc]
        q3 =
          if node.left != nil do
            :queue.in(node.left, q2)
          else
            q2
          end

        q4 =
          if node.right != nil do
            :queue.in(node.right, q3)
          else
            q3
          end

        traverse(q4, acc1)
    end
  end

  # Helper to build tree from level-order list
  defp build_tree(vals, idx) when idx >= length(vals), do: nil

  defp build_tree(vals, idx) do
    left = build_tree(vals, 2 * idx + 1)
    right = build_tree(vals, 2 * idx + 2)

    %TreeNode{
      val: Enum.at(vals, idx),
      left: left,
      right: right
    }
  end
end
```
