# 0173. Binary Search Tree Iterator

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
 * /
class BSTIterator {
    std::stack<TreeNode*> st;
    
    void pushLeft(TreeNode* node) {
        while (node) {
            st.push(node);
            node = node->left;
        }
    }
public:
    BSTIterator(TreeNode* root) {
        pushLeft(root);
    }
    
    int next() {
        TreeNode* cur = st.top();
        st.pop();
        int val = cur->val;
        if (cur->right) pushLeft(cur->right);
        return val;
    }
    
    bool hasNext() {
        return !st.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
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
class BSTIterator {
    private final java.util.Deque<TreeNode> stack = new java.util.ArrayDeque<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root);
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode node = stack.pop();
        if (node.right != null) {
            pushLeft(node.right);
        }
        return node.val;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    private void pushLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
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

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest element
        node = self.stack.pop()
        val = node.val
        # If there is a right subtree, process its leftmost branch
        if node.right:
            self._push_left_branch(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
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

typedef struct {
    struct TreeNode **stack;
    int top;
    int capacity;
} BSTIterator;

static void push(BSTIterator *it, struct TreeNode *node) {
    if (it->top == it->capacity) {
        int newCap = it->capacity ? it->capacity * 2 : 128;
        it->stack = realloc(it->stack, newCap * sizeof(struct TreeNode *));
        it->capacity = newCap;
    }
    it->stack[it->top++] = node;
}

static struct TreeNode *pop(BSTIterator *it) {
    return it->stack[--it->top];
}

/** @brief Initialize your data structure here. */
BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator *it = malloc(sizeof(BSTIterator));
    it->stack = NULL;
    it->top = 0;
    it->capacity = 0;

    struct TreeNode *cur = root;
    while (cur) {
        push(it, cur);
        cur = cur->left;
    }
    return it;
}

/** @brief Returns the next smallest number. */
int bSTIteratorNext(BSTIterator* obj) {
    struct TreeNode *node = pop(obj);
    int val = node->val;

    if (node->right) {
        struct TreeNode *cur = node->right;
        while (cur) {
            push(obj, cur);
            cur = cur->left;
        }
    }
    return val;
}

/** @brief Returns whether we have a next smallest number. */
bool bSTIteratorHasNext(BSTIterator* obj) {
    return obj->top > 0;
}

/** @brief Deallocate memory. */
void bSTIteratorFree(BSTIterator* obj) {
    if (obj) {
        free(obj->stack);
        free(obj);
    }
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
public class BSTIterator
{
    private readonly Stack<TreeNode> _stack = new Stack<TreeNode>();

    public BSTIterator(TreeNode root)
    {
        PushLeft(root);
    }

    /** @return the next smallest number */
    public int Next()
    {
        TreeNode node = _stack.Pop();
        int result = node.val;
        if (node.right != null)
        {
            PushLeft(node.right);
        }
        return result;
    }

    /** @return whether we have a next smallest number */
    public bool HasNext()
    {
        return _stack.Count > 0;
    }

    private void PushLeft(TreeNode node)
    {
        while (node != null)
        {
            _stack.Push(node);
            node = node.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
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
var BSTIterator = function(root) {
    this.stack = [];
    let node = root;
    while (node) {
        this.stack.push(node);
        node = node.left;
    }
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function() {
    const node = this.stack.pop();
    const val = node.val;
    if (node.right) {
        let cur = node.right;
        while (cur) {
            this.stack.push(cur);
            cur = cur.left;
        }
    }
    return val;
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function() {
    return this.stack.length > 0;
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

class BSTIterator {
    private stack: TreeNode[] = [];

    constructor(root: TreeNode | null) {
        this.pushLeft(root);
    }

    private pushLeft(node: TreeNode | null): void {
        while (node !== null) {
            this.stack.push(node);
            node = node.left;
        }
    }

    next(): number {
        const node = this.stack.pop()!;
        if (node.right !== null) {
            this.pushLeft(node.right);
        }
        return node.val;
    }

    hasNext(): boolean {
        return this.stack.length > 0;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
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
class BSTIterator {
    /**
     * @var TreeNode[]
     */
    private $stack;

    /**
     * @param TreeNode $root
     */
    function __construct($root) {
        $this->stack = [];
        $this->pushLeft($root);
    }

    /**
     * Push all left descendants of a node onto the stack.
     *
     * @param TreeNode|null $node
     */
    private function pushLeft($node) {
        while ($node !== null) {
            $this->stack[] = $node;
            $node = $node->left;
        }
    }

    /**
     * @return Integer
     */
    function next() {
        $node = array_pop($this->stack);
        $val = $node->val;
        if ($node->right !== null) {
            $this->pushLeft($node->right);
        }
        return $val;
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return !empty($this->stack);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * $obj = new BSTIterator($root);
 * $ret_1 = $obj->next();
 * $ret_2 = $obj->hasNext();
 */
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

class BSTIterator {
    private var stack: [TreeNode] = []
    
    init(_ root: TreeNode?) {
        pushLeft(root)
    }
    
    private func pushLeft(_ node: TreeNode?) {
        var cur = node
        while let n = cur {
            stack.append(n)
            cur = n.left
        }
    }
    
    /** @return the next smallest number */
    func next() -> Int {
        let node = stack.removeLast()
        if let right = node.right {
            pushLeft(right)
        }
        return node.val
    }
    
    /** @return whether we have a next smallest number */
    func hasNext() -> Bool {
        return !stack.isEmpty
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator(root)
 * let ret_1: Int = obj.next()
 * let ret_2: Bool = obj.hasNext()
 */
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
class BSTIterator(root: TreeNode?) {

    private val stack = java.util.ArrayDeque<TreeNode>()

    init {
        pushLeft(root)
    }

    private fun pushLeft(node: TreeNode?) {
        var cur = node
        while (cur != null) {
            stack.push(cur)
            cur = cur.left
        }
    }

    /** @return the next smallest number */
    fun next(): Int {
        val node = stack.pop()
        if (node.right != null) {
            pushLeft(node.right)
        }
        return node.`val`
    }

    /** @return whether we have a next smallest number */
    fun hasNext(): Boolean {
        return stack.isNotEmpty()
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
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
class BSTIterator {
  final List<TreeNode> _stack = [];

  BSTIterator(TreeNode? root) {
    _pushLeft(root);
  }

  void _pushLeft(TreeNode? node) {
    while (node != null) {
      _stack.add(node);
      node = node.left;
    }
  }

  int next() {
    final TreeNode node = _stack.removeLast();
    if (node.right != null) {
      _pushLeft(node.right);
    }
    return node.val;
  }

  bool hasNext() => _stack.isNotEmpty;
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = BSTIterator(root);
 * int param1 = obj.next();
 * bool param2 = obj.hasNext();
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
type BSTIterator struct {
    stack []*TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
    it := BSTIterator{}
    for root != nil {
        it.stack = append(it.stack, root)
        root = root.Left
    }
    return it
}

func (this *BSTIterator) Next() int {
    n := len(this.stack) - 1
    node := this.stack[n]
    this.stack = this.stack[:n] // pop

    if node.Right != nil {
        cur := node.Right
        for cur != nil {
            this.stack = append(this.stack, cur)
            cur = cur.Left
        }
    }
    return node.Val
}

func (this *BSTIterator) HasNext() bool {
    return len(this.stack) > 0
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
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

class BSTIterator
  # Initialize the iterator with the root of the BST.
  #
  # @param {TreeNode} root
  def initialize(root)
    @stack = []
    push_left_branch(root)
  end

  # @return {Integer} the next smallest number
  def next()
    node = @stack.pop
    val = node.val
    push_left_branch(node.right) if node.right
    val
  end

  # @return {Boolean} true if there exists a next smallest number
  def has_next()
    !@stack.empty?
  end

  private

  # Push all left descendants of the given node onto the stack.
  #
  # @param {TreeNode} node
  def push_left_branch(node)
    while node
      @stack << node
      node = node.left
    end
  end
end

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator.new(root)
# param_1 = obj.next()
# param_2 = obj.has_next()
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
class BSTIterator(_root: TreeNode) {

  private val stack = new scala.collection.mutable.Stack[TreeNode]()

  private def pushLeft(node: TreeNode): Unit = {
    var cur = node
    while (cur != null) {
      stack.push(cur)
      cur = cur.left
    }
  }

  // Initialize the stack with the leftmost path from root
  if (_root != null) pushLeft(_root)

  def next(): Int = {
    val node = stack.pop()
    if (node.right != null) pushLeft(node.right)
    node.value
  }

  def hasNext(): Boolean = stack.nonEmpty
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * val obj = new BSTIterator(root)
 * val param_1 = obj.next()
 * val param_2 = obj.hasNext()
 */
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

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

struct BSTIterator {
    stack: RefCell<Vec<Rc<RefCell<TreeNode>>>>,
}

impl BSTIterator {

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let iter = BSTIterator { stack: RefCell::new(Vec::new()) };
        iter.push_left(root);
        iter
    }
    
    fn next(&self) -> i32 {
        // Pop the smallest node
        let mut stack_ref = self.stack.borrow_mut();
        let node_rc = stack_ref.pop().expect("next called without a next element");
        let node = node_rc.borrow();
        let val = node.val;
        let right_child = node.right.clone();
        drop(stack_ref); // Release mutable borrow before recursive push
        self.push_left(right_child);
        val
    }
    
    fn has_next(&self) -> bool {
        !self.stack.borrow().is_empty()
    }
}

impl BSTIterator {
    fn push_left(&self, mut node_opt: Option<Rc<RefCell<TreeNode>>>) {
        while let Some(node_rc) = node_opt {
            self.stack.borrow_mut().push(Rc::clone(&node_rc));
            node_opt = node_rc.borrow().left.clone();
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * let obj = BSTIterator::new(root);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */
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

(define bst-iterator%
  (class object%
    (init-field root)
    (field [stack '()])

    ;; Push all left descendants of node onto the stack
    (define (push-left node)
      (let loop ((n node) (s stack))
        (if n
            (loop (tree-node-left n) (cons n s))
            (set! stack s))))

    ;; Initialize the iterator by pushing leftmost path from root
    (begin
      (push-left root))

    (define/public (next)
      (let ((node (car stack)))
        (set! stack (cdr stack))
        (when (tree-node-right node)
          (push-left (tree-node-right node)))
        (tree-node-val node)))

    (define/public (has-next)
      (not (null? stack)))

    (super-new)))
```

## Erlang

```erlang
-module(solution).
-export([bst_iterator_init_/1,
         bst_iterator_next/0,
         bst_iterator_has_next/0]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-define(STACK_KEY, bst_iterator_stack).

%% Initialize the iterator with the root of BST.
-spec bst_iterator_init_(Root :: #tree_node{} | null) -> any().
bst_iterator_init_(Root) ->
    Stack = push_left(Root, []),
    put(?STACK_KEY, Stack).

%% Return the next smallest number in the BST.
-spec bst_iterator_next() -> integer().
bst_iterator_next() ->
    case get(?STACK_KEY) of
        [] ->
            erlang:error(no_next);
        [Top | Rest] ->
            Value = Top#tree_node.val,
            NewStack =
                case Top#tree_node.right of
                    null -> Rest;
                    Right -> push_left(Right, Rest)
                end,
            put(?STACK_KEY, NewStack),
            Value
    end.

%% Return true if there exists a next smallest number.
-spec bst_iterator_has_next() -> boolean().
bst_iterator_has_next() ->
    case get(?STACK_KEY) of
        [] -> false;
        _  -> true
    end.

%% Helper: push all left descendants of Node onto Accumulator stack.
-spec push_left(Node :: #tree_node{} | null, Acc :: [#tree_node{}]) -> [#tree_node{}].
push_left(null, Acc) ->
    Acc;
push_left(Node, Acc) ->
    push_left(Node#tree_node.left, [Node | Acc]).
```

## Elixir

```elixir
defmodule BSTIterator do
  @spec init_(root :: TreeNode.t() | nil) :: any
  def init_(root) do
    stack = left_path([], root)
    Process.put(:bst_iter_stack, stack)
    :ok
  end

  @spec next() :: integer
  def next() do
    [node | rest] = Process.get(:bst_iter_stack, [])
    new_stack = left_path(rest, node.right)
    Process.put(:bst_iter_stack, new_stack)
    node.val
  end

  @spec has_next() :: boolean
  def has_next() do
    case Process.get(:bst_iter_stack, []) do
      [] -> false
      _ -> true
    end
  end

  defp left_path(stack, nil), do: stack

  defp left_path(stack, %TreeNode{} = node) do
    left_path([node | stack], node.left)
  end
end
```
