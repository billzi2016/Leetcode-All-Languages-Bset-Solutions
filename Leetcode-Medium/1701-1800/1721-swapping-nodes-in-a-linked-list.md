# 1721. Swapping Nodes in a Linked List

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
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        if (!head) return nullptr;
        ListNode* first = head;
        for (int i = 1; i < k; ++i) {
            first = first->next;
        }
        ListNode* second = head;
        ListNode* cur = first->next;
        while (cur) {
            cur = cur->next;
            second = second->next;
        }
        int tmp = first->val;
        first->val = second->val;
        second->val = tmp;
        return head;
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
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        if (head == null) return null;
        
        // Find kth node from the start
        ListNode first = head;
        for (int i = 1; i < k; i++) {
            first = first.next;
        }
        
        // Use two-pointer technique to find kth node from the end
        ListNode second = head;
        ListNode fast = first;
        while (fast.next != null) {
            fast = fast.next;
            second = second.next;
        }
        
        // Swap values
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
        
        return head;
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
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Find kth node from the start
        first = head
        for _ in range(k - 1):
            first = first.next

        # Use two-pointer technique to find kth node from the end
        second = head
        cur = first
        while cur.next:
            cur = cur.next
            second = second.next

        # Swap their values
        first.val, second.val = second.val, first.val
        return head
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Find kth node from the start
        first = head
        for _ in range(k - 1):
            first = first.next
        
        # Use two-pointer technique to find kth node from the end
        second = head
        fast = first
        while fast.next:
            fast = fast.next
            second = second.next
        
        # Swap values
        first.val, second.val = second.val, first.val
        return head
```

## C

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    if (!head) return NULL;
    
    // Find kth node from the beginning
    struct ListNode *first = head;
    for (int i = 1; i < k && first; ++i) {
        first = first->next;
    }
    
    // Find kth node from the end using two-pointer technique
    struct ListNode *second = head;
    struct ListNode *temp = first;
    while (temp->next != NULL) {
        temp = temp->next;
        second = second->next;
    }
    
    // Swap their values
    int tmpVal = first->val;
    first->val = second->val;
    second->val = tmpVal;
    
    return head;
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
public class Solution {
    public ListNode SwapNodes(ListNode head, int k) {
        if (head == null) return null;

        // Find kth node from the start
        ListNode first = head;
        for (int i = 1; i < k; i++) {
            first = first.next;
        }

        // Use two-pointer technique to find kth node from the end
        ListNode fast = first.next;   // start after the kth node
        ListNode second = head;
        while (fast != null) {
            fast = fast.next;
            second = second.next;
        }

        // Swap values
        int temp = first.val;
        first.val = second.val;
        second.val = temp;

        return head;
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
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    // Find kth node from the start
    let first = head;
    for (let i = 1; i < k; i++) {
        first = first.next;
    }
    
    // Use two-pointer technique to find kth node from the end
    let fast = first;
    let second = head;
    while (fast.next !== null) {
        fast = fast.next;
        second = second.next;
    }
    
    // Swap values of the two nodes
    const temp = first.val;
    first.val = second.val;
    second.val = temp;
    
    return head;
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

function swapNodes(head: ListNode | null, k: number): ListNode | null {
    if (!head) return null;

    // Find kth node from the start
    let first: ListNode | null = head;
    for (let i = 1; i < k && first; i++) {
        first = first.next;
    }

    // Use two-pointer technique to find kth node from the end
    let second: ListNode | null = head;
    let fast: ListNode | null = first ? first.next : null;
    while (fast) {
        fast = fast.next;
        second = second!.next;
    }

    // Swap values of the two nodes
    if (first && second) {
        const tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }

    return head;
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
class Solution {

    /**
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function swapNodes($head, $k) {
        if ($head === null) return null;

        // Find kth node from the start
        $first = $head;
        for ($i = 1; $i < $k; $i++) {
            $first = $first->next;
        }

        // Use two-pointer technique to find kth node from the end
        $second = $head;
        $curr = $first;
        while ($curr->next !== null) {
            $curr = $curr->next;
            $second = $second->next;
        }

        // Swap values
        $tmp = $first->val;
        $first->val = $second->val;
        $second->val = $tmp;

        return $head;
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
class Solution {
    func swapNodes(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head else { return nil }
        var first: ListNode? = head
        for _ in 1..<k {
            first = first?.next
        }
        var fast = first?.next
        var second: ListNode? = head
        while fast != nil {
            fast = fast?.next
            second = second?.next
        }
        // Swap values
        let temp = first!.val
        first!.val = second!.val
        second!.val = temp
        return head
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun swapNodes(head: ListNode?, k: Int): ListNode? {
        if (head == null) return null

        // Find kth node from the start
        var first = head
        for (i in 1 until k) {
            first = first!!.next
        }
        val nodeFromStart = first!!

        // Find kth node from the end using two-pointer technique
        var second = head
        var temp = first
        while (temp?.next != null) {
            temp = temp.next
            second = second!!.next
        }
        val nodeFromEnd = second!!

        // Swap their values
        val tmp = nodeFromStart.`val`
        nodeFromStart.`val` = nodeFromEnd.`val`
        nodeFromEnd.`val` = tmp

        return head
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
class Solution {
  ListNode? swapNodes(ListNode? head, int k) {
    if (head == null) return null;

    // Find kth node from the start
    ListNode? kthFromStart = head;
    for (int i = 1; i < k; i++) {
      kthFromStart = kthFromStart!.next;
    }

    // Use two-pointer technique to find kth node from the end
    ListNode? fast = kthFromStart;
    ListNode? slow = head;
    while (fast!.next != null) {
      fast = fast.next;
      slow = slow!.next;
    }
    ListNode? kthFromEnd = slow;

    // Swap their values
    int temp = kthFromStart!.val;
    kthFromStart.val = kthFromEnd!.val;
    kthFromEnd.val = temp;

    return head;
  }
}
```

## Golang

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val  int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
	if head == nil {
		return nil
	}
	// Find kth node from the start
	first := head
	for i := 1; i < k; i++ {
		first = first.Next
	}
	// Use two-pointer to find kth node from the end
	second := head
	fast := first
	for fast.Next != nil {
		fast = fast.Next
		second = second.Next
	}
	// Swap values
	first.Val, second.Val = second.Val, first.Val
	return head
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
# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def swap_nodes(head, k)
  # Find the kth node from the start
  first = head
  (k - 1).times { first = first.next }

  # Use two-pointer technique to find the kth node from the end
  fast = first
  second = head
  while fast.next
    fast = fast.next
    second = second.next
  end

  # Swap their values
  first.val, second.val = second.val, first.val
  head
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
object Solution {
    def swapNodes(head: ListNode, k: Int): ListNode = {
        // Find kth node from the start
        var first = head
        for (_ <- 1 until k) {
            first = first.next
        }

        // Use two-pointer technique to find kth node from the end
        var fast = first
        var second = head
        while (fast.next != null) {
            fast = fast.next
            second = second.next
        }

        // Swap their values
        val tmp = first.x
        first.x = second.x
        second.x = tmp

        head
    }
}
```

## Rust

```rust
use std::mem;

impl Solution {
    pub fn swap_nodes(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        // Compute the length of the list
        let mut len = 0usize;
        {
            let mut cur = &head;
            while let Some(node) = cur {
                len += 1;
                cur = &node.next;
            }
        }

        let left_idx = k as usize;               // 1‑based index from start
        let right_idx = len - (k as usize) + 1;   // corresponding index from end

        let mut left_ptr: *mut ListNode = std::ptr::null_mut();
        let mut right_ptr: *mut ListNode = std::ptr::null_mut();

        // Locate the two nodes
        {
            let mut idx = 1usize;
            let mut cur = &mut head;
            while let Some(node) = cur {
                if idx == left_idx {
                    left_ptr = node.as_mut() as *mut ListNode;
                }
                if idx == right_idx {
                    right_ptr = node.as_mut() as *mut ListNode;
                }
                cur = &mut node.next;
                idx += 1;
            }
        }

        // Swap their values
        unsafe {
            mem::swap(&mut (*left_ptr).val, &mut (*right_ptr).val);
        }

        head
    }
}
```

## Racket

```racket
#|
; Definition for singly-linked list:
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (swap-nodes head k)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (if (not head)
      head
      (let* ([node1
              (let loop ((node head) (i 1))
                (if (= i k)
                    node
                    (loop (list-node-next node) (+ i 1))))]
             [slow head]
             [fast node1])
        (let move ()
          (when (list-node-next fast)
            (set! fast (list-node-next fast))
            (set! slow (list-node-next slow))
            (move)))
        (let ([node2 slow])
          (let ([tmp (list-node-val node1)])
            (set-list-node-val! node1 (list-node-val node2))
            (set-list-node-val! node2 tmp))
          head))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec swap_nodes(Head :: #list_node{} | null, K :: integer()) -> #list_node{} | null.
swap_nodes(null, _K) ->
    null;
swap_nodes(Head, K) ->
    Len = list_len(Head, 0),
    Pos2 = Len - K + 1,
    {ValK, ValPos2} = get_vals(Head, K, Pos2, 1, undefined, undefined),
    rebuild(Head, K, Pos2, ValK, ValPos2, 1).

list_len(null, Acc) -> Acc;
list_len(Node, Acc) ->
    list_len(Node#list_node.next, Acc + 1).

get_vals(null, _K, _Pos2, _Idx, V1, V2) ->
    {V1, V2};
get_vals(Node, K, Pos2, Idx, V1, V2) ->
    Val = Node#list_node.val,
    NewV1 = case Idx of
                K -> Val;
                _ -> V1
            end,
    NewV2 = case Idx of
                Pos2 -> Val;
                _ -> V2
            end,
    get_vals(Node#list_node.next, K, Pos2, Idx + 1, NewV1, NewV2).

rebuild(null, _K, _Pos2, _ValK, _ValPos2, _Idx) ->
    null;
rebuild(Node, K, Pos2, ValK, ValPos2, Idx) ->
    NewVal = case Idx of
                K -> ValPos2;
                Pos2 -> ValK;
                _ -> Node#list_node.val
            end,
    #list_node{
        val = NewVal,
        next = rebuild(Node#list_node.next, K, Pos2, ValK, ValPos2, Idx + 1)
    }.
```

## Elixir

```elixir
defmodule ListNode do
  @type t :: %__MODULE__{
          val: integer,
          next: ListNode.t() | nil
        }
  defstruct val: 0, next: nil
end

defmodule Solution do
  @spec swap_nodes(head :: ListNode.t() | nil, k :: integer) :: ListNode.t() | nil
  def swap_nodes(head, k) do
    vals = collect_vals(head, [])
    len = length(vals)

    i = k - 1
    j = len - k

    val_i = Enum.at(vals, i)
    val_j = Enum.at(vals, j)

    vals = List.replace_at(vals, i, val_j)
    vals = List.replace_at(vals, j, val_i)

    build_list(vals)
  end

  defp collect_vals(nil, acc), do: Enum.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp build_list(vals) do
    Enum.reduce(Enum.reverse(vals), nil, fn v, acc ->
      %ListNode{val: v, next: acc}
    end)
  end
end
```
