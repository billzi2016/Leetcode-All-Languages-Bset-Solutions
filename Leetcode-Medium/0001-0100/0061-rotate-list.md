# 0061. Rotate List

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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        
        // Compute the length and get the tail node
        ListNode* tail = head;
        int len = 1;
        while (tail->next) {
            tail = tail->next;
            ++len;
        }
        
        k %= len;
        if (k == 0) return head;
        
        // Form a circular list
        tail->next = head;
        
        // Find the new tail: (len - k) steps from the start
        int stepsToNewTail = len - k;
        ListNode* newTail = head;
        for (int i = 1; i < stepsToNewTail; ++i) {
            newTail = newTail->next;
        }
        
        // Break the circle and set new head
        ListNode* newHead = newTail->next;
        newTail->next = nullptr;
        return newHead;
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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;
        
        // Compute the length and get the tail node
        ListNode tail = head;
        int len = 1;
        while (tail.next != null) {
            tail = tail.next;
            len++;
        }
        
        k %= len;
        if (k == 0) return head;
        
        // Form a circular list
        tail.next = head;
        
        // Find new tail: (len - k) steps from the start
        int stepsToNewTail = len - k;
        ListNode newTail = head;
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }
        
        // Break the circle
        ListNode newHead = newTail.next;
        newTail.next = null;
        return newHead;
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
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Compute the length and get the tail node.
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Find new tail: (length - k - 1)th node.
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        # Break the circle.
        new_tail.next = None
        tail.next = head

        return new_head
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Compute the length and get the tail node.
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Connect tail to head to form a circle.
        tail.next = head

        # Find new tail: (length - k) steps from the current head.
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
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
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next || k == 0) return head;

    // Compute length and get the tail node
    struct ListNode *tail = head;
    int len = 1;
    while (tail->next) {
        tail = tail->next;
        ++len;
    }

    // Form a circular list
    tail->next = head;

    k %= len;
    if (k == 0) {
        tail->next = NULL;
        return head;
    }

    int stepsToNewTail = len - k - 1;
    struct ListNode *newTail = head;
    for (int i = 0; i < stepsToNewTail; ++i) {
        newTail = newTail->next;
    }

    struct ListNode *newHead = newTail->next;
    newTail->next = NULL;

    return newHead;
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
    public ListNode RotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;

        // Compute the length and get the tail node
        ListNode tail = head;
        int len = 1;
        while (tail.next != null) {
            tail = tail.next;
            len++;
        }

        // Make it a circular list
        tail.next = head;

        k %= len;
        if (k == 0) {
            tail.next = null; // break the circle
            return head;
        }

        int stepsToNewTail = len - k;
        ListNode newTail = head;
        for (int i = 1; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null; // break the circle

        return newHead;
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
var rotateRight = function(head, k) {
    if (!head || k === 0) return head;
    
    // Compute the length and get the tail node.
    let len = 1;
    let tail = head;
    while (tail.next) {
        tail = tail.next;
        len++;
    }
    
    k %= len;
    if (k === 0) return head;
    
    // Form a circular list.
    tail.next = head;
    
    // Find the new tail: (len - k) steps from the current head.
    let stepsToNewTail = len - k;
    let newTail = head;
    for (let i = 1; i < stepsToNewTail; i++) {
        newTail = newTail.next;
    }
    
    // Break the circle and set the new head.
    const newHead = newTail.next;
    newTail.next = null;
    
    return newHead;
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

function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (!head || !head.next || k === 0) return head;

    // Compute the length and get the tail node
    let len = 1;
    let tail = head;
    while (tail.next) {
        tail = tail.next;
        len++;
    }

    k %= len;
    if (k === 0) return head;

    // Form a circular list
    tail.next = head;

    // Find the new tail: (len - k - 1) steps from the original head
    let stepsToNewTail = len - k - 1;
    let newTail = head;
    while (stepsToNewTail > 0) {
        newTail = newTail.next!;
        stepsToNewTail--;
    }

    const newHead = newTail.next!;
    newTail.next = null; // break the circle

    return newHead;
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
    function rotateRight($head, $k) {
        if ($head === null || $k == 0) {
            return $head;
        }

        // Compute the length and get the tail node.
        $len = 1;
        $tail = $head;
        while ($tail->next !== null) {
            $tail = $tail->next;
            $len++;
        }

        $k = $k % $len;
        if ($k == 0) {
            return $head;
        }

        // Find the new tail: (len - k - 1) steps from head.
        $stepsToNewTail = $len - $k - 1;
        $newTail = $head;
        for ($i = 0; $i < $stepsToNewTail; $i++) {
            $newTail = $newTail->next;
        }

        // Rewire pointers to rotate.
        $newHead = $newTail->next;
        $newTail->next = null;
        $tail->next = $head;

        return $newHead;
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
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head else { return nil }
        if k == 0 { return head }
        
        // Compute length and get tail
        var length = 1
        var tail = head
        while let next = tail.next {
            length += 1
            tail = next
        }
        
        let rotate = k % length
        if rotate == 0 { return head }
        
        // Find new tail: (length - rotate - 1) steps from head
        var stepsToNewTail = length - rotate - 1
        var newTail = head
        while stepsToNewTail > 0 {
            newTail = newTail.next!
            stepsToNewTail -= 1
        }
        
        let newHead = newTail.next
        newTail.next = nil
        tail.next = head
        
        return newHead
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
    fun rotateRight(head: ListNode?, k: Int): ListNode? {
        if (head == null || head.next == null || k == 0) return head

        // Compute length and get the tail node
        var length = 1
        var cur = head!!
        while (cur.next != null) {
            cur = cur.next!!
            length++
        }
        val tail = cur

        // Form a circular list
        tail.next = head

        val rotate = k % length
        if (rotate == 0) {
            tail.next = null
            return head
        }

        // Find new tail: (length - rotate) steps from the start
        var stepsToNewTail = length - rotate
        var newTail = head!!
        for (i in 1 until stepsToNewTail) {
            newTail = newTail.next!!
        }
        val newHead = newTail.next
        newTail.next = null

        return newHead
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
  ListNode? rotateRight(ListNode? head, int k) {
    if (head == null || head.next == null || k == 0) return head;

    // Compute length and get tail
    int len = 0;
    ListNode? cur = head;
    ListNode? tail;
    while (cur != null) {
      len++;
      if (cur.next == null) tail = cur;
      cur = cur.next;
    }

    k %= len;
    if (k == 0) return head;

    // Make it circular
    tail!.next = head;

    // Find new tail: (len - k - 1) steps from head
    int stepsToNewTail = len - k - 1;
    ListNode? newTail = head;
    for (int i = 0; i < stepsToNewTail; i++) {
      newTail = newTail!.next;
    }

    // New head is next of new tail
    ListNode? newHead = newTail!.next;
    // Break the circle
    newTail.next = null;

    return newHead;
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
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}
	
	// Compute the length and get the tail.
	length := 1
	tail := head
	for tail.Next != nil {
		tail = tail.Next
		length++
	}
	
	k %= length
	if k == 0 {
		return head
	}
	
	// Form a circular list.
	tail.Next = head
	
	// Find the new tail: (length - k - 1) steps from the start.
	stepsToNewTail := length - k - 1
	newTail := head
	for i := 0; i < stepsToNewTail; i++ {
		newTail = newTail.Next
	}
	
	newHead := newTail.Next
	newTail.Next = nil
	
	return newHead
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

def rotate_right(head, k)
  return nil if head.nil?
  # Compute length and get the tail node
  length = 1
  cur = head
  while cur.next
    cur = cur.next
    length += 1
  end
  tail = cur
  k %= length
  return head if k == 0

  steps_to_new_tail = length - k - 1
  new_tail = head
  steps_to_new_tail.times { new_tail = new_tail.next }

  new_head = new_tail.next
  new_tail.next = nil
  tail.next = head
  new_head
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
    def rotateRight(head: ListNode, k: Int): ListNode = {
        if (head == null || k == 0) return head

        // Compute the length and get the tail node
        var length = 1
        var tail = head
        while (tail.next != null) {
            tail = tail.next
            length += 1
        }

        val rot = k % length
        if (rot == 0) return head

        // Form a circular list
        tail.next = head

        // Find the new tail: (length - rot) steps from the original head
        var stepsToNewTail = length - rot
        var newTail = head
        for (_ <- 1 until stepsToNewTail) {
            newTail = newTail.next
        }

        val newHead = newTail.next
        newTail.next = null
        newHead
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rotate_right(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        // Empty list or no rotation needed
        if head.is_none() {
            return None;
        }

        // Compute the length of the list
        let mut len = 0usize;
        {
            let mut cur = &head;
            while let Some(node) = cur {
                len += 1;
                cur = &node.next;
            }
        }

        let k_usize = (k as usize) % len;
        if k_usize == 0 {
            return head;
        }

        // Number of nodes to keep before the new head
        let rotate = len - k_usize; // rotate >= 1 && rotate < len

        // Move to the node just before the new head
        let mut cur = &mut head;
        for _ in 0..rotate - 1 {
            cur = &mut cur.as_mut().unwrap().next;
        }

        // Detach the new head part
        let mut new_head = cur.as_mut().unwrap().next.take();

        // Connect the tail of the detached part to the original head segment
        if let Some(ref mut nh) = new_head {
            let mut tail = nh;
            while tail.next.is_some() {
                tail = tail.next.as_mut().unwrap();
            }
            tail.next = head;
        }

        new_head
    }
}
```

## Racket

```racket
(define/contract (rotate-right head k)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (if (or (not head) (zero? k))
      head
      (let* ((len-tail
              (let loop ((node head) (len 0) (tail #f))
                (if (not node)
                    (list len tail)
                    (loop (list-node-next node) (+ len 1) node))))
             (len (first len-tail))
             (tail (second len-tail)))
        (if (= len 0)
            head
            (let ((rot (modulo k len)))
              (if (= rot 0)
                  head
                  (let* ((steps (- len rot))
                         (new-tail
                          (let loop ((node head) (i steps))
                            (if (= i 1)
                                node
                                (loop (list-node-next node) (- i 1)))))
                         (new-head (list-node-next new-tail)))
                    (set-list-node-next! tail new-head)
                    (set-list-node-next! new-tail #f)
                    new-head)))))))
```

## Erlang

```erlang
-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec rotate_right(Head :: #list_node{} | null, K :: integer()) -> #list_node{} | null.
rotate_right(null, _K) ->
    null;
rotate_right(Head, K) ->
    Nodes = collect_nodes(Head, []),
    Len = length(Nodes),
    Rot = K rem Len,
    case Rot of
        0 -> Head;
        _ ->
            SplitPos = Len - Rot,
            {Front, Back} = lists:split(SplitPos, Nodes),
            NewNodes = Back ++ Front,
            build_list(NewNodes)
    end.

collect_nodes(null, Acc) ->
    lists:reverse(Acc);
collect_nodes(#list_node{val = V, next = N}, Acc) ->
    collect_nodes(N, [#list_node{val = V} | Acc]).

build_list([]) -> null;
build_list([#list_node{val = V} | Rest]) ->
    #list_node{val = V, next = build_list(Rest)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec rotate_right(head :: ListNode.t | nil, k :: integer) :: ListNode.t | nil
  def rotate_right(head, k) do
    vals = collect_vals(head, [])
    len = length(vals)

    cond do
      len == 0 -> nil
      k == 0 -> head
      true ->
        rot = rem(k, len)
        if rot == 0 do
          head
        else
          {front, back} = Enum.split(vals, len - rot)
          build_list(back ++ front)
        end
    end
  end

  defp collect_vals(nil, acc), do: Enum.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp build_list([]), do: nil

  defp build_list([h | t]) do
    %ListNode{val: h, next: build_list(t)}
  end
end
```
