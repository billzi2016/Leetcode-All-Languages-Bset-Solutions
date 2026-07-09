# 0109. Convert Sorted List to Binary Search Tree

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    ListNode* cur;
    
    int getLength(ListNode* head) {
        int len = 0;
        while (head) {
            ++len;
            head = head->next;
        }
        return len;
    }
    
    TreeNode* buildBST(int l, int r) {
        if (l > r) return nullptr;
        int mid = l + (r - l) / 2;
        TreeNode* leftChild = buildBST(l, mid - 1);
        TreeNode* node = new TreeNode(cur->val);
        cur = cur->next;
        node->left = leftChild;
        node->right = buildBST(mid + 1, r);
        return node;
    }
    
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int n = getLength(head);
        cur = head;
        return buildBST(0, n - 1);
    }
};
```

## Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    private ListNode current;

    public TreeNode sortedListToBST(ListNode head) {
        int size = 0;
        for (ListNode node = head; node != null; node = node.next) {
            size++;
        }
        current = head;
        return buildTree(0, size - 1);
    }

    private TreeNode buildTree(int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = left + (right - left) / 2;

        TreeNode leftChild = buildTree(left, mid - 1);

        TreeNode root = new TreeNode(current.val);
        current = current.next;

        root.left = leftChild;
        root.right = buildTree(mid + 1, right);
        return root;
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Compute the length of the linked list
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        self.current = head  # pointer that moves forward during inorder construction

        def build(l, r):
            if l >= r:
                return None
            mid = (l + r) // 2

            # Build left subtree
            left_child = build(l, mid)

            # Root node corresponds to current list node
            root_val = self.current.val
            root = TreeNode(root_val)
            root.left = left_child

            # Move to next list node
            self.current = self.current.next

            # Build right subtree
            root.right = build(mid + 1, r)

            return root

        return build(0, size)
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        # Compute the length of the linked list
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        # Use a closure to build BST in inorder fashion
        self.curr = head

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            left_child = build(l, mid - 1)
            root = TreeNode(self.curr.val)
            root.left = left_child
            self.curr = self.curr.next
            root.right = build(mid + 1, r)
            return root

        return build(0, size - 1)
```

## C

```c
#include <stdlib.h>

static struct ListNode *list_ptr;

static struct TreeNode* build(int left, int right) {
    if (left > right) return NULL;
    int mid = left + (right - left) / 2;
    
    struct TreeNode *left_child = build(left, mid - 1);
    
    struct TreeNode *node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = list_ptr->val;
    node->left = left_child;
    
    list_ptr = list_ptr->next;
    
    node->right = build(mid + 1, right);
    return node;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* sortedListToBST(struct ListNode* head) {
    int len = 0;
    struct ListNode *p = head;
    while (p) {
        ++len;
        p = p->next;
    }
    
    list_ptr = head;
    if (len == 0) return NULL;
    return build(0, len - 1);
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
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
    private ListNode _current;

    public TreeNode SortedListToBST(ListNode head) {
        int size = 0;
        for (var node = head; node != null; node = node.next) size++;
        _current = head;
        return BuildTree(0, size - 1);
    }

    private TreeNode BuildTree(int left, int right) {
        if (left > right) return null;

        int mid = left + (right - left) / 2;

        // Build left subtree
        TreeNode leftChild = BuildTree(left, mid - 1);

        // Root node corresponds to current list node
        TreeNode root = new TreeNode(_current.val);
        _current = _current.next;
        root.left = leftChild;

        // Build right subtree
        root.right = BuildTree(mid + 1, right);

        return root;
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    // Get the length of the linked list
    let size = 0;
    for (let node = head; node !== null; node = node.next) {
        size++;
    }
    
    let current = head;
    
    const buildTree = (l, r) => {
        if (l >= r) return null;
        const mid = Math.floor((l + r) / 2);
        
        // Build left subtree
        const left = buildTree(l, mid);
        
        // Root node corresponds to current list node
        const root = new TreeNode(current.val);
        root.left = left;
        current = current.next;
        
        // Build right subtree
        root.right = buildTree(mid + 1, r);
        return root;
    };
    
    return buildTree(0, size);
};
```

## Typescript

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

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

function sortedListToBST(head: ListNode | null): TreeNode | null {
    // Compute the length of the linked list
    let size = 0;
    for (let node = head; node !== null; node = node.next) {
        size++;
    }

    let current: ListNode | null = head;

    const build = (l: number, r: number): TreeNode | null => {
        if (l >= r) return null;
        const mid = Math.floor((l + r) / 2);
        // Build left subtree
        const left = build(l, mid);

        // Root node corresponds to current list node
        if (current === null) return null; // safety check
        const root = new TreeNode(current.val);
        root.left = left;

        // Move to next list node
        current = current.next;

        // Build right subtree
        root.right = build(mid + 1, r);
        return root;
    };

    return build(0, size);
}
```

## Php

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
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

    /** @var ListNode|null */
    private $current;

    /**
     * @param ListNode $head
     * @return TreeNode|null
     */
    function sortedListToBST($head) {
        // compute length of list
        $len = 0;
        $node = $head;
        while ($node !== null) {
            $len++;
            $node = $node->next;
        }
        $this->current = $head;
        return $this->buildTree(0, $len - 1);
    }

    /**
     * @param int $l left index (inclusive)
     * @param int $r right index (inclusive)
     * @return TreeNode|null
     */
    private function buildTree($l, $r) {
        if ($l > $r) {
            return null;
        }
        $mid = intdiv($l + $r, 2);
        // Build left subtree
        $left = $this->buildTree($l, $mid - 1);

        // Root node corresponds to current list node
        $rootVal = $this->current !== null ? $this->current->val : 0;
        $root = new TreeNode($rootVal);
        $root->left = $left;

        // Move to next list node
        $this->current = $this->current !== null ? $this->current->next : null;

        // Build right subtree
        $root->right = $this->buildTree($mid + 1, $r);
        return $root;
    }
}
```

## Swift

```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
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
    func sortedListToBST(_ head: ListNode?) -> TreeNode? {
        var size = 0
        var node = head
        while node != nil {
            size += 1
            node = node?.next
        }
        
        var current = head
        
        func build(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right { return nil }
            let mid = (left + right) / 2
            
            // Build left subtree
            let leftChild = build(left, mid - 1)
            
            // Root node from current list node
            guard let val = current?.val else { return nil }
            let root = TreeNode(val)
            root.left = leftChild
            
            // Move to next list node
            current = current?.next
            
            // Build right subtree
            root.right = build(mid + 1, right)
            
            return root
        }
        
        return build(0, size - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortedListToBST(head: ListNode?): TreeNode? {
        var size = 0
        var p = head
        while (p != null) {
            size++
            p = p.next
        }
        var current = head

        fun build(l: Int, r: Int): TreeNode? {
            if (l > r) return null
            val mid = l + (r - l) / 2
            val left = build(l, mid - 1)
            val nodeVal = current!!.`val`
            val root = TreeNode(nodeVal)
            current = current?.next
            root.left = left
            root.right = build(mid + 1, r)
            return root
        }

        return if (size == 0) null else build(0, size - 1)
    }
}
```

## Dart

```dart
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
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
  TreeNode? sortedListToBST(ListNode? head) {
    // Compute the length of the linked list
    int size = 0;
    ListNode? node = head;
    while (node != null) {
      size++;
      node = node.next;
    }

    ListNode? current = head;

    TreeNode? build(int left, int right) {
      if (left > right) return null;
      int mid = left + ((right - left) >> 1);

      // Build left subtree
      TreeNode? leftChild = build(left, mid - 1);

      // Root node corresponds to current list node
      TreeNode root = TreeNode(current!.val);
      current = current.next;

      // Build right subtree
      TreeNode? rightChild = build(mid + 1, right);

      root.left = leftChild;
      root.right = rightChild;
      return root;
    }

    return build(0, size - 1);
  }
}
```

## Golang

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedListToBST(head *ListNode) *TreeNode {
    // Compute the length of the list
    size := 0
    for n := head; n != nil; n = n.Next {
        size++
    }

    curr := head

    var build func(int, int) *TreeNode
    build = func(l, r int) *TreeNode {
        if l > r {
            return nil
        }
        mid := (l + r) / 2

        // Build left subtree
        left := build(l, mid-1)

        // Root node corresponds to current list node
        root := &TreeNode{Val: curr.Val}
        curr = curr.Next

        // Attach left subtree and build right subtree
        root.Left = left
        root.Right = build(mid+1, r)
        return root
    }

    return build(0, size-1)
}
```

## Ruby

```ruby
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def sorted_list_to_bst(head)
  # Compute the length of the list
  size = 0
  node = head
  while node
    size += 1
    node = node.next
  end

  list_head = head

  build = nil
  build = ->(l, r) do
    return nil if l > r
    mid = (l + r) / 2

    left_child = build.call(l, mid - 1)

    root_val = list_head.val
    root = TreeNode.new(root_val)
    list_head = list_head.next

    right_child = build.call(mid + 1, r)

    root.left = left_child
    root.right = right_child
    root
  end

  build.call(0, size - 1)
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def sortedListToBST(head: ListNode): TreeNode = {
        // Compute the length of the list
        var size = 0
        var node = head
        while (node != null) {
            size += 1
            node = node.next
        }

        if (size == 0) return null

        var current: ListNode = head

        def build(l: Int, r: Int): TreeNode = {
            if (l > r) return null
            val mid = l + (r - l) / 2
            // Build left subtree
            val left = build(l, mid - 1)
            // Root node corresponds to current list node
            val root = new TreeNode(current.x)
            current = current.next
            // Build right subtree
            val right = build(mid + 1, r)
            root.left = left
            root.right = right
            root
        }

        build(0, size - 1)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
        // Collect values from the linked list into a vector.
        let mut vals = Vec::new();
        let mut cur = head.as_ref();
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next.as_ref();
        }

        fn build(slice: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if slice.is_empty() {
                return None;
            }
            let mid = slice.len() / 2;
            let left = build(&slice[..mid]);
            let right = build(&slice[mid + 1..]);
            Some(Rc::new(RefCell::new(TreeNode {
                val: slice[mid],
                left,
                right,
            })))
        }

        build(&vals)
    }
}
```

## Racket

```racket
; Definition for singly-linked list:
#|
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

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

(define/contract (sorted-list-to-bst head)
  (-> (or/c list-node? #f) (or/c tree-node? #f))
  (let* ((len
          (let loop ((node head) (cnt 0))
            (if node
                (loop (list-node-next node) (+ cnt 1))
                cnt)))
         (cur (box head)))
    (define (build l r)
      (if (> l r)
          #f
          (let* ((mid (quotient (+ l r) 2))
                 (left (build l (- mid 1)))
                 (node-val (list-node-val (unbox cur)))
                 (root (make-tree-node node-val))
                 (_ (set-box! cur (list-node-next (unbox cur))))
                 (right (build (+ mid 1) r)))
            (set-tree-node-left! root left)
            (set-tree-node-right! root right)
            root)))
    (if (= len 0)
        #f
        (build 0 (- len 1)))))
```

## Erlang

```erlang
-module(solution).
-export([sorted_list_to_bst/1]).

-spec sorted_list_to_bst(Head :: #list_node{} | null) -> #tree_node{} | null.
sorted_list_to_bst(null) ->
    null;
sorted_list_to_bst(Head) ->
    Len = list_len(Head),
    {Tree, _} = build_tree(Len, Head),
    Tree.

list_len(null) ->
    0;
list_len(#list_node{next=Next}) ->
    1 + list_len(Next).

build_tree(0, List) ->
    {null, List};
build_tree(N, List) when N > 0 ->
    LeftSize = N div 2,
    RightSize = N - LeftSize - 1,
    {LeftTree, RestAfterLeft} = build_tree(LeftSize, List),
    case RestAfterLeft of
        null ->
            {null, null};
        #list_node{val=Val, next=NextNode} ->
            {RightTree, RestAfterRight} = build_tree(RightSize, NextNode),
            Root = #tree_node{val=Val, left=LeftTree, right=RightTree},
            {Root, RestAfterRight}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sorted_list_to_bst(head :: ListNode.t() | nil) :: TreeNode.t() | nil
  def sorted_list_to_bst(head) do
    len = list_len(head)
    {root, _} = build(0, len - 1, head)
    root
  end

  defp list_len(nil), do: 0
  defp list_len(%ListNode{next: nxt}), do: 1 + list_len(nxt)

  defp build(l, r, node) when l > r, do: {nil, node}
  defp build(l, r, node) do
    mid = div(l + r, 2)
    {left, after_left} = build(l, mid - 1, node)

    %ListNode{val: val, next: nxt} = after_left
    root = %TreeNode{val: val, left: left}

    {right, rest} = build(mid + 1, r, nxt)
    root = %{root | right: right}
    {root, rest}
  end
end
```
