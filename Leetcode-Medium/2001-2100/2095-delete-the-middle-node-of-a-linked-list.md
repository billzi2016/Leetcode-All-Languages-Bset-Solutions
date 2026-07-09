# 2095. Delete the Middle Node of a Linked List

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
    ListNode* deleteMiddle(ListNode* head) {
        if (!head || !head->next) return nullptr;
        ListNode dummy(0, head);
        ListNode* slow = &dummy;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        // slow is node before the middle
        ListNode* toDelete = slow->next;
        slow->next = toDelete->next;
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
    public ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }
        // 'slow' is the middle node, remove it
        prev.next = slow.next;
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
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Remove the middle node
        prev.next = slow.next
        return head
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
    def deleteMiddle(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return None
        
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        prev.next = slow.next
        return head
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
struct ListNode* deleteMiddle(struct ListNode* head) {
    if (!head || !head->next) return NULL;

    struct ListNode *slow = head, *fast = head, *prev = NULL;

    while (fast && fast->next) {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    prev->next = slow->next;
    free(slow);
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
    public ListNode DeleteMiddle(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }

        // 'slow' is the middle node, remove it
        prev.next = slow.next;
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
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (!head || !head.next) return null;
    let slow = head, fast = head;
    let prev = null;
    while (fast && fast.next) {
        fast = fast.next.next;
        prev = slow;
        slow = slow.next;
    }
    // Remove the middle node
    prev.next = slow.next;
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

function deleteMiddle(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return null;

    let slow: ListNode = head;
    let fast: ListNode | null = head;
    let prev: ListNode | null = null;

    while (fast && fast.next) {
        fast = fast.next.next;
        prev = slow;
        slow = slow.next!;
    }

    // Remove the middle node
    if (prev) {
        prev.next = slow.next;
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
     * @return ListNode|null
     */
    function deleteMiddle($head) {
        if ($head === null || $head->next === null) {
            return null;
        }

        $slow = $head;
        $fast = $head;
        $prev = null;

        while ($fast !== null && $fast->next !== null) {
            $fast = $fast->next->next;
            $prev = $slow;
            $slow = $slow->next;
        }

        // Remove the middle node
        if ($prev !== null) {
            $prev->next = $slow->next;
        } else {
            return null; // This case occurs only when list has one element, already handled above.
        }

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
    func deleteMiddle(_ head: ListNode?) -> ListNode? {
        guard let head = head else { return nil }
        if head.next == nil {
            return nil
        }

        let dummy = ListNode(0, head)
        var slow: ListNode? = dummy
        var fast: ListNode? = dummy

        while fast?.next != nil && fast?.next?.next != nil {
            fast = fast?.next?.next
            slow = slow?.next
        }

        // Remove the middle node
        slow?.next = slow?.next?.next

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
    fun deleteMiddle(head: ListNode?): ListNode? {
        if (head == null) return null
        val dummy = ListNode(0)
        dummy.next = head
        var slow: ListNode = dummy
        var fast: ListNode? = head

        while (fast != null && fast.next != null) {
            fast = fast.next?.next
            slow = slow.next!!
        }

        // Delete the middle node
        slow.next = slow.next?.next
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
  ListNode? deleteMiddle(ListNode? head) {
    if (head == null || head.next == null) return null;

    ListNode? prev;
    ListNode? slow = head;
    ListNode? fast = head;

    while (fast != null && fast.next != null) {
      prev = slow;
      slow = slow!.next;
      fast = fast.next!.next;
    }

    // Remove the middle node
    prev!.next = slow!.next;

    return head;
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
func deleteMiddle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }
    dummy := &ListNode{Next: head}
    prev, slow, fast := dummy, head, head

    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        prev = slow
        slow = slow.Next
    }

    // Delete the middle node
    prev.Next = slow.Next
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

def delete_middle(head)
  return nil if head.nil? || head.next.nil?

  slow = head
  fast = head
  prev = nil

  while fast && fast.next
    fast = fast.next.next
    prev = slow
    slow = slow.next
  end

  # Remove the middle node
  prev.next = slow.next
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
    def deleteMiddle(head: ListNode): ListNode = {
        if (head == null || head.next == null) return null

        var slow: ListNode = head
        var fast: ListNode = head
        var prev: ListNode = null

        while (fast != null && fast.next != null) {
            fast = fast.next.next
            prev = slow
            slow = slow.next
        }

        // Remove the middle node
        if (prev != null) {
            prev.next = slow.next
        }
        head
    }
}
```

## Rust

```rust
impl Solution {
    pub fn delete_middle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // If list has 0 or 1 node, result is empty
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return None;
        }

        // First pass: compute length
        let mut len = 0usize;
        let mut cur = &head;
        while let Some(node) = cur {
            len += 1;
            cur = &node.next;
        }

        let mid = len / 2; // index of node to delete

        // Second pass: remove the middle node using a dummy head
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        {
            let mut prev = &mut dummy;
            for _ in 0..mid {
                prev = prev.next.as_mut().unwrap();
            }
            // `prev` is the node before the middle one
            if let Some(mut mid_node) = prev.next.take() {
                prev.next = mid_node.next.take();
            }
        }
        dummy.next
    }
}
```

## Racket

```racket
(define/contract (delete-middle head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (cond
    [(not head) #f]
    [(not (list-node-next head)) ; only one node
     #f]
    [else
     (let loop ((slow head) (fast head) (prev #f))
       (if (or (not fast) (not (list-node-next fast)))
           (begin
             (set-list-node-next! prev (list-node-next slow))
             head)
           (let* ([next-fast (list-node-next fast)]
                  [fast2 (if next-fast (list-node-next next-fast) #f)])
             (loop (list-node-next slow) fast2 slow))))]))
```

## Erlang

```erlang
-module(solution).
-export([delete_middle/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec delete_middle(Head :: #list_node{} | null) -> #list_node{} | null.
delete_middle(Head) ->
    case Head of
        null -> null;
        _ ->
            Len = length_list(Head, 0),
            MidIdx = Len div 2,
            delete_at_index(Head, MidIdx)
    end.

length_list(null, Acc) -> Acc;
length_list(#list_node{next = Next}, Acc) ->
    length_list(Next, Acc + 1).

delete_at_index(Node, 0) ->
    case Node of
        null -> null;
        #list_node{next = Next} -> Next
    end;
delete_at_index(null, _) -> null;
delete_at_index(#list_node{} = Node, Index) when Index > 0 ->
    NewNext = delete_at_index(Node#list_node.next, Index - 1),
    Node#list_node{next = NewNext}.
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_middle(head :: ListNode.t() | nil) :: ListNode.t() | nil
  def delete_middle(nil), do: nil

  def delete_middle(head) do
    len = length_of(head, 0)

    if len == 1 do
      nil
    else
      mid = div(len, 2)
      rev = build_rev(head, 0, mid, nil)
      reverse_iter(rev, nil)
    end
  end

  defp length_of(nil, acc), do: acc
  defp length_of(%ListNode{next: nxt}, acc), do: length_of(nxt, acc + 1)

  defp build_rev(nil, _idx, _mid, acc), do: acc

  defp build_rev(%ListNode{val: v, next: nxt}, idx, mid, acc) do
    if idx == mid do
      build_rev(nxt, idx + 1, mid, acc)
    else
      new_node = %ListNode{val: v, next: acc}
      build_rev(nxt, idx + 1, mid, new_node)
    end
  end

  defp reverse_iter(nil, acc), do: acc

  defp reverse_iter(%ListNode{val: v, next: nxt}, acc) do
    node = %ListNode{val: v, next: acc}
    reverse_iter(nxt, node)
  end
end
```
