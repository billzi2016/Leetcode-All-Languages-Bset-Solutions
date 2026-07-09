# 0024. Swap Nodes in Pairs

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
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        while (prev->next && prev->next->next) {
            ListNode* first = prev->next;
            ListNode* second = first->next;
            // swap
            first->next = second->next;
            second->next = first;
            prev->next = second;
            // move prev forward
            prev = first;
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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;

            // Perform swap
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Move prev pointer forward for next pair
            prev = first;
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
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            # swap the pair
            prev.next = second
            first.next = second.next
            second.next = first
            # move prev to the next pair start
            prev = first
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
    def swapPairs(self, head: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            # Move prev pointer two nodes ahead
            prev = first
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
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;

    while (prev->next && prev->next->next) {
        struct ListNode *first = prev->next;
        struct ListNode *second = first->next;

        // Perform swap
        first->next = second->next;
        second->next = first;
        prev->next = second;

        // Move prev to the next pair's previous node
        prev = first;
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
    public ListNode SwapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;

            // Perform swap
            first.next = second.next;
            second.next = first;
            prev.next = second;

            // Move prev pointer forward for next pair
            prev = first;
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
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    
    while (prev.next && prev.next.next) {
        const first = prev.next;
        const second = first.next;
        
        // Swap
        first.next = second.next;
        second.next = first;
        prev.next = second;
        
        // Move to next pair
        prev = first;
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

function swapPairs(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let prev = dummy;

    while (prev.next && prev.next.next) {
        const first = prev.next;
        const second = first.next!; // guaranteed not null

        // swap
        first.next = second.next;
        second.next = first;
        prev.next = second;

        // move prev two nodes ahead
        prev = first;
    }

    return dummy.next;
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
     * @param ListNode|null $head
     * @return ListNode|null
     */
    function swapPairs($head) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;
        $prev = $dummy;

        while ($prev->next !== null && $prev->next->next !== null) {
            $first = $prev->next;
            $second = $first->next;

            // Swapping
            $first->next = $second->next;
            $second->next = $first;
            $prev->next = $second;

            // Move prev pointer forward for next pair
            $prev = $first;
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
    func swapPairs(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        
        while let first = prev?.next, let second = first.next {
            // Nodes after the pair
            let nextPair = second.next
            
            // Swap
            prev?.next = second
            second.next = first
            first.next = nextPair
            
            // Move prev to the end of the swapped pair
            prev = first
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
    fun swapPairs(head: ListNode?): ListNode? {
        if (head == null || head.next == null) return head
        val second = head.next
        head.next = swapPairs(second?.next)
        second?.next = head
        return second
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
  ListNode? swapPairs(ListNode? head) {
    var dummy = ListNode(0, head);
    var prev = dummy;
    while (prev.next != null && prev.next!.next != null) {
      var first = prev.next!;
      var second = first.next!;

      // Perform the swap
      first.next = second.next;
      second.next = first;
      prev.next = second;

      // Move prev pointer forward for next pair
      prev = first;
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
func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy

    for prev.Next != nil && prev.Next.Next != nil {
        first := prev.Next
        second := first.Next

        // Swapping
        first.Next = second.Next
        second.Next = first
        prev.Next = second

        // Move prev two nodes ahead
        prev = first
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

def swap_pairs(head)
  return head unless head && head.next
  new_head = head.next
  head.next = swap_pairs(new_head.next)
  new_head.next = head
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
    def swapPairs(head: ListNode): ListNode = {
        if (head == null || head.next == null) return head
        val second = head.next
        head.next = swapPairs(second.next)
        second.next = head
        second
    }
}
```

## Rust

```rust
impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match head {
            None => None,
            Some(mut first) => {
                if let Some(mut second) = first.next.take() {
                    // Detach the rest of the list after the second node
                    let remaining = second.next.take();
                    // Recursively swap the remaining part
                    first.next = Self::swap_pairs(remaining);
                    // Place first after second
                    second.next = Some(first);
                    Some(second)
                } else {
                    // Only one node left, no swap needed
                    Some(first)
                }
            }
        }
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

(define/contract (swap-pairs head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (cond
    [(or (not head) (not (list-node-next head))) head]
    [else
     (let* ([first head]
            [second (list-node-next first)]
            [rest (list-node-next second)])
       (set-list-node-next! first (swap-pairs rest))
       (set-list-node-next! second first)
       second)]))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec swap_pairs(Head :: #list_node{} | null) -> #list_node{} | null.
swap_pairs(null) ->
    null;
swap_pairs(#list_node{next = null}=Node) ->
    Node;
swap_pairs(#list_node{val = V1, next = #list_node{val = V2, next = Rest}}) ->
    SwappedRest = swap_pairs(Rest),
    #list_node{
        val = V2,
        next = #list_node{
            val = V1,
            next = SwappedRest
        }
    }.
```

## Elixir

```elixir
defmodule Solution do
  @spec swap_pairs(head :: ListNode.t() | nil) :: ListNode.t() | nil
  def swap_pairs(nil), do: nil

  def swap_pairs(%ListNode{next: nil} = node), do: node

  def swap_pairs(%ListNode{
        val: v1,
        next: %ListNode{val: v2, next: nxt}
      }) do
    %ListNode{
      val: v2,
      next: %ListNode{
        val: v1,
        next: swap_pairs(nxt)
      }
    }
  end
end
```
