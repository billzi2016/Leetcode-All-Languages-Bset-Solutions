# 0328. Odd Even Linked List

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
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;
        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;
        
        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            
            even.next = odd.next;
            even = even.next;
        }
        
        odd.next = evenHead;
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
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
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
    def oddEvenList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return head
        
        odd = head
        even_head = even = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
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
struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head || !head->next)
        return head;

    struct ListNode *odd = head;
    struct ListNode *even = head->next;
    struct ListNode *evenHead = even;

    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;

        even->next = odd->next;
        even = even->next;
    }

    odd->next = evenHead;
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
    public ListNode OddEvenList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;

            even.next = odd.next;
            even = even.next;
        }

        odd.next = evenHead;
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
var oddEvenList = function(head) {
    if (!head || !head.next) return head;
    
    let odd = head;
    let even = head.next;
    const evenHead = even;
    
    while (even && even.next) {
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
    }
    
    odd.next = evenHead;
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

function oddEvenList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;

    let odd: ListNode = head;
    let even: ListNode = head.next;
    const evenHead: ListNode = even;

    while (even && even.next) {
        odd.next = even.next;
        odd = odd.next;

        even.next = odd.next;
        even = even.next;
    }

    odd.next = evenHead;
    return head;
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
     * @return ListNode
     */
    function oddEvenList($head) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $odd = $head;
        $even = $head->next;
        $evenHead = $even;

        while ($even !== null && $even->next !== null) {
            // link next odd
            $odd->next = $even->next;
            $odd = $odd->next;

            // link next even
            $even->next = $odd->next;
            $even = $even->next;
        }

        // attach even list after odd list
        $odd->next = $evenHead;

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
    func oddEvenList(_ head: ListNode?) -> ListNode? {
        guard let head = head else { return nil }
        guard let second = head.next else { return head }
        
        var odd: ListNode? = head
        var evenHead: ListNode? = second
        var even: ListNode? = second
        
        while let nextOdd = even?.next {
            // link current odd to the next odd node
            odd?.next = nextOdd
            odd = nextOdd
            
            // link current even to the next even node
            even?.next = odd?.next
            even = even?.next
        }
        
        odd?.next = evenHead
        return head
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
    fun oddEvenList(head: ListNode?): ListNode? {
        if (head == null) return null

        var odd: ListNode? = head
        val evenHead: ListNode? = head.next
        var even: ListNode? = evenHead

        while (even != null && even.next != null) {
            // link next odd node
            odd!!.next = even.next
            odd = odd!!.next

            // link next even node
            even.next = odd!!.next
            even = even.next
        }

        // attach even list after odd list
        odd!!.next = evenHead
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
  ListNode? oddEvenList(ListNode? head) {
    if (head == null || head.next == null) return head;

    ListNode? odd = head;
    ListNode? even = head.next;
    ListNode? evenHead = even;

    while (even != null && even.next != null) {
      odd!.next = even.next;
      odd = odd!.next;

      even!.next = odd!.next;
      even = even!.next;
    }

    odd!.next = evenHead;
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
func oddEvenList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    odd := head
    even := head.Next
    evenHead := even

    for even != nil && even.Next != nil {
        odd.Next = even.Next
        odd = odd.Next
        even.Next = odd.Next
        even = even.Next
    }

    odd.Next = evenHead
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

def odd_even_list(head)
  return head if head.nil? || head.next.nil?

  odd = head
  even = head.next
  even_head = even

  while even && even.next
    odd.next = even.next
    odd = odd.next

    even.next = odd.next
    even = even.next
  end

  odd.next = even_head
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
    def oddEvenList(head: ListNode): ListNode = {
        if (head == null) return null
        var odd: ListNode = head
        var even: ListNode = head.next
        val evenHead: ListNode = even

        while (even != null && even.next != null) {
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        }

        odd.next = evenHead
        head
    }
}
```

## Rust

```rust
impl Solution {
    pub fn odd_even_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Empty or single node list.
        let mut odd = match head.as_mut() {
            Some(node) => node,
            None => return None,
        };
        // Detach the even sublist.
        let mut even_head = odd.next.take();
        if even_head.is_none() {
            return head;
        }
        let mut even = even_head.as_mut().unwrap();

        while even.next.is_some() {
            // Move next odd node after current odd.
            let mut next_odd = even.next.take().unwrap();
            odd.next = Some(next_odd);
            odd = odd.next.as_mut().unwrap();

            // Move following even node after current even, if it exists.
            if odd.next.is_some() {
                let mut next_even = odd.next.take().unwrap();
                even.next = Some(next_even);
                even = even.next.as_mut().unwrap();
            } else {
                even.next = None;
                break;
            }
        }

        // Append the even list after the odd list.
        odd.next = even_head;

        head
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
;; (struct list-node (val next) #:mutable #:transparent)

(define/contract (odd-even-list head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (or (not head) (not (list-node-next head)))
      head
      (let* ((odd head)
             (even (list-node-next head))
             (even-head even))
        (let loop ()
          (when (and even (list-node-next even))
            ;; link odd to the next odd node
            (set-list-node-next! odd (list-node-next even))
            (set! odd (list-node-next odd)) ; advance odd

            ;; link even to the next even node
            (set-list-node-next! even (list-node-next odd))
            (set! even (list-node-next even))

            (loop)))
        (set-list-node-next! odd even-head)
        head)))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec odd_even_list(Head :: #list_node{} | null) -> #list_node{} | null.
odd_even_list(null) ->
    null;
odd_even_list(Head) ->
    Values = to_vals(Head, []),
    {OddVals, EvenVals} = split_vals(Values, true, [], []),
    from_vals(OddVals ++ EvenVals).

to_vals(null, Acc) -> lists:reverse(Acc);
to_vals(#list_node{val = V, next = N}, Acc) ->
    to_vals(N, [V | Acc]).

split_vals([], _IsOdd, O, E) ->
    {lists:reverse(O), lists:reverse(E)};
split_vals([X | Xs], true, O, E) ->
    split_vals(Xs, false, [X | O], E);
split_vals([X | Xs], false, O, E) ->
    split_vals(Xs, true, O, [X | E]).

from_vals([]) -> null;
from_vals([V | Vs]) ->
    #list_node{val = V, next = from_vals(Vs)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec odd_even_list(head :: ListNode.t | nil) :: ListNode.t | nil
  def odd_even_list(head) do
    {odd_vals, even_vals} = collect(head, true, [], [])
    vals = Enum.reverse(odd_vals) ++ Enum.reverse(even_vals)
    build(vals)
  end

  defp collect(nil, _is_odd, odds, evens), do: {odds, evens}

  defp collect(%ListNode{val: v, next: nxt}, true, odds, evens) do
    collect(nxt, false, [v | odds], evens)
  end

  defp collect(%ListNode{val: v, next: nxt}, false, odds, evens) do
    collect(nxt, true, odds, [v | evens])
  end

  defp build([]), do: nil

  defp build([h | t]) do
    %ListNode{val: h, next: build(t)}
  end
end
```
