# 0092. Reverse Linked List II

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;
        ListNode dummy(0);
        dummy.next = head;
        ListNode* pre = &dummy;
        for (int i = 1; i < left; ++i) {
            pre = pre->next;
        }
        ListNode* cur = pre->next;
        ListNode* then = cur->next;
        for (int i = 0; i < right - left; ++i) {
            cur->next = then->next;
            then->next = pre->next;
            pre->next = then;
            then = cur->next;
        }
        return dummy.next;
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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        // Move prev to the node before position left
        for (int i = 1; i < left; i++) {
            prev = prev.next;
        }
        
        // Start reversing from 'curr' which is at position left
        ListNode curr = prev.next;
        for (int i = 0; i < right - left; i++) {
            ListNode next = curr.next;
            // Detach next
            curr.next = next.next;
            // Move next to the front of the sublist
            next.next = prev.next;
            prev.next = next;
        }
        
        return dummy.next;
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
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # Move `pre` to the node immediately before the sublist to reverse
        for _ in range(left - 1):
            pre = pre.next

        # `cur` will point to the first node of the sublist that will be reversed
        cur = pre.next

        # Iteratively reverse the nodes between left and right
        for _ in range(right - left):
            nxt = cur.next          # Node to be moved to front of the sublist
            cur.next = nxt.next    # Remove `nxt` from its current position
            nxt.next = pre.next    # Insert `nxt` after `pre`
            pre.next = nxt

        return dummy.next
```

## Python3

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node immediately before the sublist to reverse
        for _ in range(left - 1):
            prev = prev.next
        
        # `curr` will point to the first node of the sublist
        curr = prev.next
        
        # Iteratively reverse the nodes within [left, right]
        for _ in range(right - left):
            nxt = curr.next          # Node to be moved to front of sublist
            curr.next = nxt.next    # Remove `nxt` from its current position
            nxt.next = prev.next    # Insert `nxt` after `prev`
            prev.next = nxt
        
        return dummy.next
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
struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (!head || left == right) return head;

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;

    for (int i = 1; i < left; ++i) {
        prev = prev->next;
    }

    struct ListNode *curr = prev->next;
    struct ListNode *next;

    for (int i = 0; i < right - left; ++i) {
        next = curr->next;
        curr->next = next->next;
        next->next = prev->next;
        prev->next = next;
    }

    return dummy.next;
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
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;

        var dummy = new ListNode(0, head);
        var prev = dummy;

        // Move prev to the node before position left
        for (int i = 1; i < left; i++) {
            prev = prev.next;
        }

        var curr = prev.next; // Node at position left

        // Reverse nodes between left and right
        for (int i = 0; i < right - left; i++) {
            var next = curr.next;
            curr.next = next.next;
            next.next = prev.next;
            prev.next = next;
        }

        return dummy.next;
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (!head || left === right) return head;
    
    const dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    
    // Move `prev` to the node before position `left`
    for (let i = 1; i < left; i++) {
        prev = prev.next;
    }
    
    // `curr` points to the first node that will be reversed
    let curr = prev.next;
    
    // Iteratively reverse nodes between left and right
    for (let i = 0; i < right - left; i++) {
        const nxt = curr.next;
        curr.next = nxt.next;
        nxt.next = prev.next;
        prev.next = nxt;
    }
    
    return dummy.next;
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

function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    if (!head || left === right) return head;

    const dummy = new ListNode(0);
    dummy.next = head;
    let prev: ListNode | null = dummy;

    // Move `prev` to the node immediately before position `left`
    for (let i = 1; i < left; i++) {
        if (prev) prev = prev.next!;
    }

    // `curr` points to the first node of the sublist to be reversed
    let curr: ListNode | null = prev!.next;

    // Iteratively reverse nodes between left and right
    for (let i = 0; i < right - left; i++) {
        const next: ListNode = curr!.next!;          // node to relocate
        curr!.next = next.next;                     // detach `next`
        next.next = prev!.next;                     // insert `next` after `prev`
        prev!.next = next;
    }

    return dummy.next;
}
```

## Php

```php
/ **
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
     * @param Integer $left
     * @param Integer $right
     * @return ListNode
     */
    function reverseBetween($head, $left, $right) {
        if ($left == $right || $head === null) {
            return $head;
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;

        // Move `prev` to the node immediately before the sublist to reverse
        $prev = $dummy;
        for ($i = 1; $i < $left; $i++) {
            $prev = $prev->next;
        }

        // `curr` points to the first node of the sublist
        $curr = $prev->next;

        // Iteratively reverse the sublist using head insertion technique
        for ($i = 0; $i < $right - $left; $i++) {
            $temp = $curr->next;
            $curr->next = $temp->next;
            $temp->next = $prev->next;
            $prev->next = $temp;
        }

        return $dummy->next;
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
    func reverseBetween(_ head: ListNode?, _ left: Int, _ right: Int) -> ListNode? {
        if left == right || head == nil { return head }
        
        let dummy = ListNode(0)
        dummy.next = head
        
        var prev: ListNode? = dummy
        for _ in 1..<left {
            prev = prev!.next
        }
        
        var curr = prev!.next
        // Reverse the sublist [left, right]
        for _ in 0..<(right - left) {
            let next = curr!.next!
            curr!.next = next.next
            next.next = prev!.next
            prev!.next = next
        }
        
        return dummy.next
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
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        if (head == null) return null
        val dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        for (i in 1 until left) {
            prev = prev?.next
        }
        val start = prev?.next
        var then = start?.next

        for (i in 0 until right - left) {
            if (start == null || then == null) break
            start.next = then.next
            then.next = prev?.next
            prev?.next = then
            then = start.next
        }
        return dummy.next
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
  ListNode? reverseBetween(ListNode? head, int left, int right) {
    if (head == null || left == right) return head;

    // Dummy node to simplify edge cases where reversal starts at head
    final dummy = ListNode(0, head);
    ListNode? prev = dummy;

    // Move `prev` to the node immediately before the sublist to reverse
    for (int i = 1; i < left; ++i) {
      prev = prev!.next;
    }

    // `curr` points to the first node of the sublist that will be reversed
    ListNode? curr = prev!.next;

    // Perform standard in‑place reversal between left and right
    for (int i = 0; i < right - left; ++i) {
      final next = curr!.next;
      curr.next = next!.next;
      next.next = prev!.next;
      prev.next = next;
    }

    return dummy.next;
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
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || left == right {
		return head
	}
	dummy := &ListNode{Next: head}
	prev := dummy
	for i := 1; i < left; i++ {
		prev = prev.Next
	}
	curr := prev.Next
	for i := 0; i < right-left; i++ {
		next := curr.Next
		curr.Next = next.Next
		next.Next = prev.Next
		prev.Next = next
	}
	return dummy.Next
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

def reverse_between(head, left, right)
  return head if head.nil? || left == right

  dummy = ListNode.new(0)
  dummy.next = head
  prev = dummy

  (left - 1).times { prev = prev.next }

  curr = prev.next
  (right - left).times do
    nxt = curr.next
    curr.next = nxt.next
    nxt.next = prev.next
    prev.next = nxt
  end

  dummy.next
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
    def reverseBetween(head: ListNode, left: Int, right: Int): ListNode = {
        if (head == null) return null
        val dummy = new ListNode(0)
        dummy.next = head
        var prev: ListNode = dummy
        for (_ <- 1 until left) {
            prev = prev.next
        }
        var curr = prev.next
        for (_ <- 0 until (right - left)) {
            val next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        }
        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
        // Dummy node to simplify edge cases
        let mut dummy = Some(Box::new(ListNode { val: 0, next: head }));
        // prev will point to the node before the sublist to reverse
        let mut prev = &mut dummy;
        for _ in 0..(left - 1) {
            prev = &mut prev.as_mut().unwrap().next;
        }

        // curr points to the first node of the sublist
        let mut curr = prev.as_mut().unwrap().next.take();

        // Reverse the sublist [left, right]
        let mut rev: Option<Box<ListNode>> = None;
        let mut count = right - left + 1;
        while count > 0 {
            if let Some(mut node) = curr {
                let next = node.next.take();
                node.next = rev;
                rev = Some(node);
                curr = next;
            }
            count -= 1;
        }

        // Connect the tail of the reversed sublist to the remaining part
        if let Some(ref mut rev_head) = rev {
            let mut tail = rev_head.as_mut();
            while tail.next.is_some() {
                tail = tail.next.as_mut().unwrap();
            }
            tail.next = curr;
        }

        // Attach the reversed sublist back to the list
        prev.as_mut().unwrap().next = rev;

        // Return the new head (skip dummy)
        dummy.unwrap().next
    }
}
```

## Racket

```racket
(define/contract (reverse-between head left right)
  (-> (or/c list-node? #f) exact-integer? exact-integer? (or/c list-node? #f))
  (if (or (not head) (= left right))
      head
      (let* ([dummy (make-list-node 0)])
        (set-list-node-next! dummy head)
        (let loop-prev ((i 1) (prev dummy))
          (if (< i left)
              (loop-prev (+ i 1) (list-node-next prev))
              (let* ([start (list-node-next prev)]
                     [curr start])
                (let loop-reverse ((i 0))
                  (when (< i (- right left))
                    (let* ([temp (list-node-next curr)])
                      (set-list-node-next! curr (list-node-next temp))
                      (set-list-node-next! temp (list-node-next prev))
                      (set-list-node-next! prev temp)
                      (loop-reverse (+ i 1)))))
                (list-node-next dummy)))))))
```

## Erlang

```erlang
-module(solution).
-export([reverse_between/3]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec reverse_between(Head :: #list_node{} | null, Left :: integer(), Right :: integer()) -> #list_node{} | null.
reverse_between(Head, Left, Right) ->
    Values = to_list(Head),
    {Prefix, Rest} = lists:split(Left - 1, Values),
    Len = Right - Left + 1,
    {Mid, Suffix} = lists:split(Len, Rest),
    NewValues = Prefix ++ lists:reverse(Mid) ++ Suffix,
    from_list(NewValues).

to_list(null) -> [];
to_list(#list_node{val = V, next = N}) ->
    [V | to_list(N)].

from_list([]) -> null;
from_list([H|T]) ->
    #list_node{val = H, next = from_list(T)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_between(head :: ListNode.t | nil, left :: integer, right :: integer) :: ListNode.t | nil
  def reverse_between(head, left, right) do
    vals = collect_vals(head, [])
    if left == right do
      head
    else
      prefix = Enum.take(vals, left - 1)
      middle = vals |> Enum.slice(left - 1, right - left + 1) |> Enum.reverse()
      suffix = Enum.drop(vals, right)
      build_list(prefix ++ middle ++ suffix)
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
