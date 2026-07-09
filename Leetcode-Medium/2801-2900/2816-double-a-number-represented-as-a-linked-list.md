# 2816. Double a Number Represented as a Linked List

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) {
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }

    ListNode* doubleIt(ListNode* head) {
        // Reverse to process from least significant digit
        ListNode* rev = reverseList(head);
        int carry = 0;
        ListNode* cur = rev;
        ListNode* prev = nullptr;
        while (cur) {
            int sum = cur->val * 2 + carry;
            cur->val = sum % 10;
            carry = sum / 10;
            prev = cur;
            cur = cur->next;
        }
        if (carry > 0) {
            prev->next = new ListNode(carry);
        }
        // Reverse back to original order
        return reverseList(rev);
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
    public ListNode doubleIt(ListNode head) {
        // Reverse the list to process from least significant digit
        ListNode rev = reverse(head);
        ListNode cur = rev;
        ListNode prev = null;
        int carry = 0;
        while (cur != null) {
            int sum = cur.val * 2 + carry;
            cur.val = sum % 10;
            carry = sum / 10;
            prev = cur;
            cur = cur.next;
        }
        if (carry > 0) {
            prev.next = new ListNode(carry);
        }
        // Reverse back to original order
        return reverse(rev);
    }

    private ListNode reverse(ListNode node) {
        ListNode prev = null;
        while (node != null) {
            ListNode nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    }
}
```

## Python

```python
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        # Reverse the list
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        rev_head = prev

        # Double each digit with carry propagation
        carry = 0
        cur = rev_head
        prev = None
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            prev = cur
            cur = cur.next

        if carry:
            prev.next = ListNode(carry)

        # Reverse back to original order
        prev = None
        cur = rev_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
```

## Python3

```python
from typing import Optional

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list to process from least significant digit
        rev_head = self._reverse(head)
        carry = 0
        cur = rev_head
        while cur:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            if not cur.next and carry:
                cur.next = ListNode(carry)
                break
            cur = cur.next
        # Reverse back to original order
        return self._reverse(rev_head)

    def _reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev
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
static struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL, *curr = head, *next;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

struct ListNode* doubleIt(struct ListNode* head) {
    if (!head) return NULL;

    struct ListNode *rev = reverseList(head);
    struct ListNode *cur = rev, *prev = NULL;
    int carry = 0;

    while (cur) {
        int sum = cur->val * 2 + carry;
        cur->val = sum % 10;
        carry = sum / 10;
        prev = cur;
        cur = cur->next;
    }

    if (carry) {
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = carry;
        node->next = NULL;
        prev->next = node;
    }

    rev = reverseList(rev);
    return rev;
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
    private ListNode Reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }

    public ListNode DoubleIt(ListNode head) {
        // Reverse to process from least significant digit
        head = Reverse(head);
        int carry = 0;
        ListNode cur = head, prev = null;

        while (cur != null) {
            int sum = cur.val * 2 + carry;
            cur.val = sum % 10;
            carry = sum / 10;
            prev = cur;
            cur = cur.next;
        }

        if (carry > 0) {
            prev.next = new ListNode(carry);
        }

        // Reverse back to original order
        return Reverse(head);
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
var doubleIt = function(head) {
    // reverse the list
    const reverse = (node) => {
        let prev = null;
        while (node) {
            const nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    };
    
    let rev = reverse(head);
    let cur = rev;
    let carry = 0;
    let prev = null;
    
    while (cur) {
        const sum = cur.val * 2 + carry;
        cur.val = sum % 10;
        carry = Math.floor(sum / 10);
        prev = cur;
        cur = cur.next;
    }
    
    if (carry > 0) {
        prev.next = new ListNode(carry);
    }
    
    return reverse(rev);
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

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let curr = head;
    while (curr) {
        const nxt = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}

function doubleIt(head: ListNode | null): ListNode | null {
    if (!head) return null;

    // Reverse to process from least significant digit
    let rev = reverseList(head);

    let carry = 0;
    let cur = rev;
    let prev: ListNode | null = null;

    while (cur) {
        const sum = cur.val * 2 + carry;
        cur.val = sum % 10;
        carry = Math.floor(sum / 10);
        prev = cur;
        cur = cur.next;
    }

    if (carry > 0 && prev) {
        prev.next = new ListNode(carry);
    }

    // Reverse back to original order
    return reverseList(rev);
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
     * @return ListNode
     */
    function doubleIt($head) {
        // Reverse the list to process from least significant digit
        $head = $this->reverseList($head);
        
        $carry = 0;
        $prev = null;
        $curr = $head;
        while ($curr !== null) {
            $sum = $curr->val * 2 + $carry;
            $curr->val = $sum % 10;
            $carry = intdiv($sum, 10);
            $prev = $curr;
            $curr = $curr->next;
        }
        
        // If there's remaining carry, append a new node
        if ($carry > 0) {
            $prev->next = new ListNode($carry);
        }
        
        // Reverse back to original order
        return $this->reverseList($head);
    }
    
    /**
     * @param ListNode $head
     * @return ListNode
     */
    private function reverseList($head) {
        $prev = null;
        $curr = $head;
        while ($curr !== null) {
            $next = $curr->next;
            $curr->next = $prev;
            $prev = $curr;
            $curr = $next;
        }
        return $prev;
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
    func doubleIt(_ head: ListNode?) -> ListNode? {
        guard let reversedHead = reverse(head) else { return nil }
        var carry = 0
        var curr: ListNode? = reversedHead
        var prev: ListNode? = nil
        
        while let node = curr {
            let total = node.val * 2 + carry
            node.val = total % 10
            carry = total / 10
            prev = node
            curr = node.next
        }
        
        if carry > 0 {
            prev?.next = ListNode(carry)
        }
        
        return reverse(reversedHead)
    }
    
    private func reverse(_ head: ListNode?) -> ListNode? {
        var prev: ListNode? = nil
        var curr = head
        while let node = curr {
            let nextTemp = node.next
            node.next = prev
            prev = node
            curr = nextTemp
        }
        return prev
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
    fun doubleIt(head: ListNode?): ListNode? {
        // Reverse the list to process from least significant digit
        var revHead = reverse(head)
        var cur = revHead
        var carry = 0
        var prev: ListNode? = null

        while (cur != null) {
            val sum = cur.`val` * 2 + carry
            cur.`val` = sum % 10
            carry = sum / 10
            prev = cur
            cur = cur.next
        }

        if (carry > 0) {
            prev?.next = ListNode(carry)
        }

        // Reverse back to original order and return
        return reverse(revHead)
    }

    private fun reverse(node: ListNode?): ListNode? {
        var prev: ListNode? = null
        var curr = node
        while (curr != null) {
            val next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        }
        return prev
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
  ListNode? _reverse(ListNode? head) {
    ListNode? prev;
    while (head != null) {
      ListNode? nxt = head.next;
      head.next = prev;
      prev = head;
      head = nxt;
    }
    return prev;
  }

  ListNode? doubleIt(ListNode? head) {
    if (head == null) return null;

    // Reverse to start from least significant digit.
    ListNode? rev = _reverse(head);
    ListNode? cur = rev;
    ListNode? prev;
    int carry = 0;

    while (cur != null) {
      int sum = cur.val * 2 + carry;
      cur.val = sum % 10;
      carry = sum ~/ 10;
      prev = cur;
      cur = cur.next;
    }

    if (carry > 0) {
      // Append new most‑significant digit.
      prev!.next = ListNode(carry);
    }

    // Restore original order.
    return _reverse(rev);
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
func reverse(head *ListNode) *ListNode {
    var prev *ListNode
    cur := head
    for cur != nil {
        nxt := cur.Next
        cur.Next = prev
        prev = cur
        cur = nxt
    }
    return prev
}

func doubleIt(head *ListNode) *ListNode {
    // Reverse the list to process from least significant digit.
    rev := reverse(head)

    carry := 0
    var prev *ListNode
    cur := rev
    for cur != nil {
        sum := cur.Val*2 + carry
        cur.Val = sum % 10
        carry = sum / 10
        prev = cur
        cur = cur.Next
    }

    // If there's remaining carry, append a new node.
    if carry > 0 {
        prev.Next = &ListNode{Val: carry}
    }

    // Reverse back to original order and return.
    return reverse(rev)
}
```

## Ruby

```ruby
def reverse(node)
  prev = nil
  cur = node
  while cur
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  end
  prev
end

def double_it(head)
  rev = reverse(head)

  carry = 0
  prev = nil
  cur = rev
  while cur
    sum = cur.val * 2 + carry
    cur.val = sum % 10
    carry = sum / 10
    prev = cur
    cur = cur.next
  end

  if carry > 0
    prev.next = ListNode.new(carry)
  end

  reverse(rev)
end
```

## Scala

```scala
object Solution {
  private def reverse(head: ListNode): ListNode = {
    var prev: ListNode = null
    var cur = head
    while (cur != null) {
      val nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
    }
    prev
  }

  def doubleIt(head: ListNode): ListNode = {
    var rev = reverse(head)
    var carry = 0
    var curr = rev
    var prev: ListNode = null

    while (curr != null) {
      val sum = curr.x * 2 + carry
      curr.x = sum % 10
      carry = sum / 10
      prev = curr
      curr = curr.next
    }

    if (carry > 0) {
      prev.next = new ListNode(carry)
    }

    reverse(rev)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn double_it(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Reverse the list
        let mut prev: Option<Box<ListNode>> = None;
        let mut cur = head;
        while let Some(mut node) = cur {
            let next = node.next.take();
            node.next = prev;
            prev = Some(node);
            cur = next;
        }

        // Process doubled values with carry, rebuilding list in correct order
        let mut rev_head = prev;
        let mut carry: i32 = 0;
        let mut processed: Option<Box<ListNode>> = None;

        while let Some(mut node) = rev_head {
            let sum = node.val * 2 + carry;
            node.val = sum % 10;
            carry = sum / 10;

            let next = node.next.take(); // original next (already reversed)
            node.next = processed;       // prepend to result list
            processed = Some(node);
            rev_head = next;
        }

        if carry > 0 {
            let mut new_node = Box::new(ListNode::new(carry));
            new_node.next = processed;
            processed = Some(new_node);
        }

        processed
    }
}
```

## Racket

```racket
#lang racket

; Definition for singly-linked list:
;|
(struct list-node
  (val next) #:mutable #:transparent)

(define (make-list-node [val 0])
  (list-node val #f))
|#

;; reverse a linked list in place, return new head
(define (reverse-list head)
  (let loop ((prev #f) (curr head))
    (if (not curr)
        prev
        (let ((next (list-node-next curr)))
          (set-list-node-next! curr prev)
          (loop curr next)))))

;; double the number represented by the linked list
(define/contract (double-it head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (not head)
      #f
      (let* ((rev (reverse-list head))
             ;; process nodes, handling carry; also keep last processed node
             (values (call-with-values
                       (lambda ()
                         (let loop ((curr rev) (carry 0) (prev #f))
                           (if (not curr)
                               (values carry prev)
                               (let* ((sum (+ (* 2 (list-node-val curr)) carry))
                                      (new-val (modulo sum 10))
                                      (new-carry (quotient sum 10)))
                                 (set-list-node-val! curr new-val)
                                 (loop (list-node-next curr) new-carry curr)))))
                       (lambda (final-carry last-node)
                         (values final-carry last-node))))
             (final-carry (car values))
             (last-node (cadr values)))
        ;; if there is remaining carry, append a new node
        (when (> final-carry 0)
          (let ((new-node (make-list-node final-carry)))
            (set-list-node-next! last-node new-node)))
        ;; reverse back to original order and return
        (reverse-list rev))))
```

## Erlang

```erlang
-module(solution).
-export([double_it/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec double_it(Head :: #list_node{} | null) -> #list_node{} | null.
double_it(null) ->
    null;
double_it(Head) ->
    {NewHead, Carry} = double_it_helper(Head),
    case Carry of
        0 -> NewHead;
        _ -> #list_node{val = Carry, next = NewHead}
    end.

-spec double_it_helper(Node :: #list_node{} | null) -> {#list_node{} | null, integer()}.
double_it_helper(null) ->
    {null, 0};
double_it_helper(Node) ->
    Next = Node#list_node.next,
    {NewNext, CarryFromNext} = double_it_helper(Next),
    Total = Node#list_node.val * 2 + CarryFromNext,
    NewVal = Total rem 10,
    CarryOut = Total div 10,
    {#list_node{val = NewVal, next = NewNext}, CarryOut}.
```

## Elixir

```elixir
defmodule Solution do
  @spec double_it(head :: ListNode.t | nil) :: ListNode.t | nil
  def double_it(head) do
    vals = collect_vals(head, [])
    {new_head, _} = build(vals, nil, 0)
    new_head
  end

  defp collect_vals(nil, acc), do: acc

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp build([], tail, carry) when carry > 0 do
    {%ListNode{val: carry, next: tail}, 0}
  end

  defp build([], tail, _carry), do: {tail, 0}

  defp build([v | rest], tail, carry) do
    sum = v * 2 + carry
    node_val = rem(sum, 10)
    new_carry = div(sum, 10)
    new_node = %ListNode{val: node_val, next: tail}
    build(rest, new_node, new_carry)
  end
end
```
