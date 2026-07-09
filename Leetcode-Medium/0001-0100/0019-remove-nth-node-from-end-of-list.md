# 0019. Remove Nth Node From End of List

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* first = &dummy;
        ListNode* second = &dummy;
        for (int i = 0; i <= n; ++i) {
            first = first->next;
        }
        while (first) {
            first = first->next;
            second = second->next;
        }
        ListNode* toDelete = second->next;
        second->next = second->next->next;
        delete toDelete;
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode first = dummy;
        ListNode second = dummy;
        for (int i = 0; i <= n; i++) {
            first = first.next;
        }
        while (first != null) {
            first = first.next;
            second = second.next;
        }
        second.next = second.next.next;
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead to maintain a gap of n between first and second
        for _ in range(n + 1):
            first = first.next

        # Advance both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

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
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move first ahead by n+1 steps to maintain a gap of n between first and second
        for _ in range(n + 1):
            if first:
                first = first.next
        
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from end
        if second.next:
            second.next = second.next.next
        
        return dummy.next
```

## C

```c
#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *first = &dummy, *second = &dummy;

    for (int i = 0; i <= n; ++i) {
        first = first->next;
    }

    while (first != NULL) {
        first = first->next;
        second = second->next;
    }

    struct ListNode* toDelete = second->next;
    second->next = second->next->next;
    free(toDelete);

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
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        var dummy = new ListNode(0, head);
        var first = dummy;
        var second = dummy;

        // Move first pointer n+1 steps ahead to maintain a gap of n between first and second
        for (int i = 0; i <= n; i++) {
            first = first.next;
        }

        // Move both pointers until first reaches the end
        while (first != null) {
            first = first.next;
            second = second.next;
        }

        // Remove the nth node from end
        second.next = second.next.next;

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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0, head);
    let first = dummy;
    let second = dummy;
    
    // Move second ahead by n+1 steps to maintain a gap of n between first and second
    for (let i = 0; i <= n; i++) {
        second = second.next;
    }
    
    // Move both pointers until second reaches the end
    while (second !== null) {
        first = first.next;
        second = second.next;
    }
    
    // Remove the target node
    first.next = first.next.next;
    
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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let first: ListNode | null = dummy;
    // Move first pointer n+1 steps ahead
    for (let i = 0; i <= n; i++) {
        first = first!.next;
    }
    let second: ListNode | null = dummy;
    while (first) {
        first = first.next;
        second = second!.next!;
    }
    // Remove the target node
    second!.next = second!.next!.next;
    return dummy.next;
}
```

## Php

```php
/**
 * Definition for singly-linked list.
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
     * @param int $n
     * @return ListNode|null
     */
    function removeNthFromEnd($head, $n) {
        $dummy = new ListNode(0);
        $dummy->next = $head;
        $first = $dummy;
        $second = $dummy;

        // Move first pointer n+1 steps ahead to maintain a gap of n between first and second
        for ($i = 0; $i <= $n; $i++) {
            $first = $first->next;
        }

        // Move both pointers until first reaches the end
        while ($first !== null) {
            $first = $first->next;
            $second = $second->next;
        }

        // Delete the target node
        $second->next = $second->next->next;

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
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        let dummy = ListNode(0, head)
        var first: ListNode? = dummy
        var second: ListNode? = dummy
        
        for _ in 0..<(n + 1) {
            first = first?.next
        }
        
        while first != nil {
            first = first?.next
            second = second?.next
        }
        
        second?.next = second?.next?.next
        return dummy.next
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var first: ListNode? = dummy
        var second: ListNode? = dummy

        repeat(n + 1) { first = first?.next }

        while (first != null) {
            first = first?.next
            second = second?.next
        }

        second?.next = second?.next?.next
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
  ListNode? removeNthFromEnd(ListNode? head, int n) {
    // Dummy node simplifies edge cases (e.g., removing the head)
    final dummy = ListNode(0, head);
    ListNode? first = dummy;
    ListNode? second = dummy;

    // Move 'first' ahead by n+1 steps to maintain a gap of n between first and second
    for (int i = 0; i <= n; i++) {
      first = first?.next;
    }

    // Advance both pointers until 'first' reaches the end
    while (first != null) {
      first = first.next;
      second = second!.next;
    }

    // Remove the target node
    second!.next = second.next?.next;

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
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{Next: head}
    first, second := dummy, dummy

    // Move first ahead by n+1 steps to maintain a gap of n between first and second
    for i := 0; i <= n; i++ {
        if first != nil {
            first = first.Next
        }
    }

    // Advance both pointers until first reaches the end
    for first != nil {
        first = first.Next
        second = second.Next
    }

    // Remove the target node
    if second.Next != nil {
        second.Next = second.Next.Next
    }

    return dummy.Next
}
```

## Ruby

```ruby
def remove_nth_from_end(head, n)
  dummy = ListNode.new(0, head)
  first = dummy
  second = dummy

  (n + 1).times { first = first.next }

  while first
    first = first.next
    second = second.next
  end

  second.next = second.next.next
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
    def removeNthFromEnd(head: ListNode, n: Int): ListNode = {
        val dummy = new ListNode(0)
        dummy.next = head
        var first: ListNode = dummy
        var second: ListNode = dummy

        // Move first pointer n+1 steps ahead to maintain a gap of n between first and second
        for (_ <- 0 to n) {
            first = first.next
        }

        // Advance both pointers until first reaches the end
        while (first != null) {
            first = first.next
            second = second.next
        }

        // Remove the target node
        second.next = second.next.next

        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        // First pass: compute the length of the list
        let mut len = 0usize;
        let mut cur = &head;
        while let Some(node) = cur {
            len += 1;
            cur = &node.next;
        }

        // Position of node to remove from the start (0‑based)
        let target = len - n as usize;

        // Dummy head simplifies removal, especially at the front
        let mut dummy = ListNode { val: 0, next: head };
        {
            let mut prev = &mut dummy;
            for _ in 0..target {
                prev = prev.next.as_mut().unwrap();
            }
            // Remove the target node
            if let Some(mut to_delete) = prev.next.take() {
                prev.next = to_delete.next.take();
            }
        }
        dummy.next
    }
}
```

## Racket

```racket
(define/contract (remove-nth-from-end head n)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (let* ((dummy (make-list-node 0)))
    (set-list-node-next! dummy head)
    (let* ((first dummy)
           (second dummy))
      ;; advance `first` n+1 steps ahead
      (for ([i (in-range (+ n 1))])
        (set! first (list-node-next first)))
      ;; move both pointers until `first` reaches the end
      (let loop ()
        (when first
          (set! first (list-node-next first))
          (set! second (list-node-next second))
          (loop)))
      ;; remove the target node
      (define to-delete (list-node-next second))
      (when to-delete
        (set-list-node-next! second (list-node-next to-delete)))
      ;; return new head
      (list-node-next dummy))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec remove_nth_from_end(Head :: #list_node{} | null, N :: integer()) -> #list_node{} | null.
remove_nth_from_end(Head, N) ->
    {NewHead, _} = remove_helper(Head, N),
    NewHead.

remove_helper(null, _) ->
    {null, 0};
remove_helper(#list_node{val=_, next=Next}=Node, N) ->
    {NewNext, Count} = remove_helper(Next, N),
    CurrCount = Count + 1,
    case CurrCount of
        N -> {NewNext, CurrCount};
        _ -> {Node#list_node{next=NewNext}, CurrCount}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_nth_from_end(head :: ListNode.t() | nil, n :: integer) :: ListNode.t() | nil
  def remove_nth_from_end(head, n) do
    {new_head, _} = remove_helper(head, n)
    new_head
  end

  defp remove_helper(nil, _n), do: {nil, 0}

  defp remove_helper(%ListNode{next: nxt}=node, n) do
    {next_node, idx} = remove_helper(nxt, n)
    cur_idx = idx + 1

    if cur_idx == n do
      {next_node, cur_idx}
    else
      {%ListNode{node | next: next_node}, cur_idx}
    end
  end
end
```
