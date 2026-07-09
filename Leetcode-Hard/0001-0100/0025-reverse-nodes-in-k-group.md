# 0025. Reverse Nodes in k-Group

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prevGroupEnd = &dummy;

        while (true) {
            // Find the kth node from prevGroupEnd
            ListNode* kth = prevGroupEnd;
            for (int i = 0; i < k && kth; ++i) {
                kth = kth->next;
            }
            if (!kth) break; // not enough nodes

            ListNode* groupStart = prevGroupEnd->next;
            ListNode* nextGroupStart = kth->next;

            // Reverse the group
            ListNode* prev = nextGroupStart;
            ListNode* cur = groupStart;
            while (cur != nextGroupStart) {
                ListNode* tmp = cur->next;
                cur->next = prev;
                prev = cur;
                cur = tmp;
            }

            // Connect reversed group with previous part
            prevGroupEnd->next = kth;   // kth is now the head of reversed group
            prevGroupEnd = groupStart;  // groupStart becomes the tail after reversal
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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode groupPrev = dummy;

        while (true) {
            // Find the kth node from groupPrev
            ListNode kth = groupPrev;
            for (int i = 0; i < k && kth != null; i++) {
                kth = kth.next;
            }
            if (kth == null) break; // not enough nodes

            ListNode groupNext = kth.next;
            // Reverse the group
            ListNode prev = groupNext;
            ListNode cur = groupPrev.next;
            while (cur != groupNext) {
                ListNode nxt = cur.next;
                cur.next = prev;
                prev = cur;
                cur = nxt;
            }

            // Connect reversed group with previous part
            ListNode temp = groupPrev.next; // will become the tail after reversal
            groupPrev.next = kth;
            groupPrev = temp;
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
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head

        # Helper to get the kth node from current (inclusive)
        def get_kth(node, steps):
            while node and steps > 0:
                node = node.next
                steps -= 1
            return node

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Reconnect reversed group with previous part
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            # reverse the group
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        # unreachable code
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
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (head == NULL || k <= 1) return head;

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;

    while (1) {
        // Check there are at least k nodes ahead
        struct ListNode *node = prev;
        for (int i = 0; i < k && node != NULL; ++i) {
            node = node->next;
        }
        if (node == NULL) break; // fewer than k nodes left

        // Reverse k nodes
        struct ListNode *curr = prev->next;
        struct ListNode *nxt = curr->next;
        for (int i = 1; i < k; ++i) {
            curr->next = nxt->next;
            nxt->next = prev->next;
            prev->next = nxt;
            nxt = curr->next;
        }
        // Move prev to the tail of the reversed segment
        prev = curr;
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
    public ListNode ReverseKGroup(ListNode head, int k) {
        if (head == null || k == 1) return head;

        var dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;

        while (true) {
            // Find the kth node from pre
            ListNode end = pre;
            for (int i = 0; i < k && end != null; i++) {
                end = end.next;
            }
            if (end == null) break; // not enough nodes

            ListNode start = pre.next;
            ListNode nextGroup = end.next;

            // Reverse [start, end]
            ListNode prev = nextGroup;
            ListNode curr = start;
            while (curr != nextGroup) {
                ListNode tmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = tmp;
            }

            // Connect reversed group with previous part
            pre.next = end;
            pre = start; // start is now the tail of the reversed group
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
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    if (!head || k === 1) return head;
    
    const dummy = new ListNode(0);
    dummy.next = head;
    let groupPrev = dummy;
    
    while (true) {
        // Find the kth node from groupPrev
        let kth = groupPrev;
        for (let i = 0; i < k && kth; i++) {
            kth = kth.next;
        }
        if (!kth) break; // not enough nodes
        
        const groupNext = kth.next;
        
        // Reverse the group
        let prev = groupNext;
        let curr = groupPrev.next;
        while (curr !== groupNext) {
            const tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        
        // Reconnect reversed group with previous part
        const tail = groupPrev.next; // original head becomes tail after reversal
        groupPrev.next = kth;        // kth is new head of the reversed group
        groupPrev = tail;            // move groupPrev to the tail for next iteration
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

function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (!head || k === 1) return head;

    const dummy = new ListNode(0);
    dummy.next = head;
    let prevGroupTail: ListNode = dummy;

    while (true) {
        // Find the kth node from prevGroupTail
        let kth: ListNode | null = prevGroupTail;
        for (let i = 0; i < k && kth !== null; i++) {
            kth = kth.next;
        }
        if (!kth) break; // Not enough nodes left

        const groupStart = prevGroupTail.next!;
        let prev: ListNode | null = null;
        let curr: ListNode | null = groupStart;

        // Reverse k nodes
        for (let i = 0; i < k && curr !== null; i++) {
            const nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }

        // Connect reversed group with the rest of the list
        prevGroupTail.next = prev;          // prev is new head of this group
        groupStart.next = curr;             // curr is the node after the group

        // Move prevGroupTail to the end of the reversed group for next iteration
        prevGroupTail = groupStart;
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
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function reverseKGroup($head, $k) {
        if ($k == 1 || $head === null) {
            return $head;
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;
        $groupPrev = $dummy;

        while (true) {
            // Find the kth node from groupPrev
            $kth = $groupPrev;
            for ($i = 0; $i < $k && $kth !== null; $i++) {
                $kth = $kth->next;
            }
            if ($kth === null) {
                break; // Not enough nodes left to reverse
            }

            $groupNext = $kth->next;

            // Reverse the group
            $prev = $groupNext;
            $curr = $groupPrev->next;
            while ($curr !== $groupNext) {
                $tmp = $curr->next;
                $curr->next = $prev;
                $prev = $curr;
                $curr = $tmp;
            }

            // Connect reversed group with previous part
            $temp = $groupPrev->next; // old head becomes tail after reversal
            $groupPrev->next = $kth;  // $kth is now the new head of the reversed group
            $groupPrev = $temp;       // Move groupPrev to the tail for next iteration
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
    func reverseKGroup(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head, k > 1 else { return head }
        let dummy = ListNode(0, head)
        var groupPrev: ListNode? = dummy

        while true {
            // Find the kth node from groupPrev
            var kth = groupPrev
            for _ in 0..<k {
                kth = kth?.next
                if kth == nil {
                    return dummy.next
                }
            }

            let groupNext = kth!.next

            // Reverse nodes between groupPrev.next and kth (inclusive)
            var prev: ListNode? = groupNext
            var curr = groupPrev?.next

            while curr !== groupNext {
                let nxt = curr?.next
                curr?.next = prev
                prev = curr
                curr = nxt
            }

            // Connect reversed part with previous part
            let temp = groupPrev?.next   // old start, now tail after reversal
            groupPrev?.next = kth        // kth is new head of the reversed segment
            groupPrev = temp             // move groupPrev to the tail for next iteration
        }
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
    fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
        if (head == null || k == 1) return head
        val dummy = ListNode(0)
        dummy.next = head
        var groupPrev: ListNode? = dummy

        while (true) {
            val kth = getKth(groupPrev, k) ?: break
            val groupNext = kth.next

            // reverse the group
            var prev: ListNode? = groupNext
            var curr = groupPrev!!.next
            while (curr !== groupNext) {
                val tmp = curr!!.next
                curr.next = prev
                prev = curr
                curr = tmp
            }

            val tail = groupPrev!!.next // original head becomes tail after reversal
            groupPrev!!.next = kth
            groupPrev = tail
        }
        return dummy.next
    }

    private fun getKth(start: ListNode?, k: Int): ListNode? {
        var cur = start
        var i = 0
        while (i < k && cur != null) {
            cur = cur!!.next
            i++
        }
        return cur
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
  ListNode? reverseKGroup(ListNode? head, int k) {
    if (head == null || k == 1) return head;

    // Dummy node to simplify edge handling
    final dummy = ListNode(0, head);
    ListNode? prevGroup = dummy;

    while (true) {
      // Check if there are at least k nodes ahead
      ListNode? kth = prevGroup;
      for (int i = 0; i < k && kth != null; ++i) {
        kth = kth!.next;
      }
      if (kth == null) break; // Not enough nodes

      // Nodes to be reversed: from prevGroup.next up to kth
      final nextGroupStart = kth!.next;

      // Reverse the segment
      ListNode? prev = nextGroupStart;
      ListNode? cur = prevGroup!.next;
      while (cur != nextGroupStart) {
        final tmp = cur!.next;
        cur.next = prev;
        prev = cur;
        cur = tmp;
      }

      // Connect reversed segment with previous part
      final tail = prevGroup.next; // original start becomes the tail after reversal
      prevGroup.next = kth; // kth is now the head of reversed segment (prev)
      prevGroup = tail; // move prevGroup to the end of the reversed segment for next iteration
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
func reverseKGroup(head *ListNode, k int) *ListNode {
	if k <= 1 || head == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	prevGroup := dummy

	for {
		// Find the kth node from prevGroup
		kth := prevGroup
		for i := 0; i < k && kth != nil; i++ {
			kth = kth.Next
		}
		if kth == nil { // not enough nodes left
			break
		}
		groupNext := kth.Next

		// Reverse the group
		prev, curr := groupNext, prevGroup.Next
		for curr != groupNext {
			tmp := curr.Next
			curr.Next = prev
			prev = curr
			curr = tmp
		}

		// Connect reversed group with previous part
		newHead := prevGroup.Next // original head becomes tail after reversal
		prevGroup.Next = kth
		prevGroup = newHead
	}
	return dummy.Next
}
```

## Ruby

```ruby
def reverse_k_group(head, k)
  return head if head.nil? || k == 1

  dummy = ListNode.new(0)
  dummy.next = head
  group_prev = dummy

  loop do
    kth = group_prev
    k.times do
      kth = kth.next
      break unless kth
    end
    break unless kth

    group_next = kth.next
    prev = group_next
    cur = group_prev.next

    while cur != group_next
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
    end

    tmp = group_prev.next
    group_prev.next = kth
    group_prev = tmp
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
    def reverseKGroup(head: ListNode, k: Int): ListNode = {
        if (head == null || k == 1) return head

        val dummy = new ListNode(0)
        dummy.next = head
        var groupPrev: ListNode = dummy

        while (true) {
            // Find the kth node from groupPrev
            var kth: ListNode = groupPrev
            var i = 0
            while (i < k && kth != null) {
                kth = kth.next
                i += 1
            }
            if (kth == null) return dummy.next

            val groupNext = kth.next

            // Reverse the group
            var prev: ListNode = groupNext
            var curr: ListNode = groupPrev.next
            while (curr != groupNext) {
                val tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            }

            // Reconnect with previous part
            val newGroupHead = kth
            val newGroupTail = groupPrev.next

            groupPrev.next = newGroupHead
            groupPrev = newGroupTail
        }
        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_k_group(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        if k <= 1 {
            return head;
        }
        let k = k as usize;

        // Dummy node to simplify edge handling
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        // Raw pointer to the dummy node
        let mut prev: *mut ListNode = &mut *dummy;

        unsafe {
            loop {
                // Find the k-th node from prev
                let mut kth = prev;
                for _ in 0..k {
                    if (*kth).next.is_none() {
                        return dummy.next;
                    }
                    kth = (*kth)
                        .next
                        .as_deref_mut()
                        .unwrap() as *mut ListNode;
                }

                // Detach the part after the k-th node
                let mut next_group = (*kth).next.take();

                // Start reversing the k nodes
                let mut cur_opt = (*prev).next.take(); // first node of the group
                let mut prev_rev: Option<Box<ListNode>> = next_group;
                let mut tail_ptr: *mut ListNode = std::ptr::null_mut();

                for i in 0..k {
                    if let Some(mut cur) = cur_opt {
                        let nxt = cur.next.take();
                        cur.next = prev_rev;
                        prev_rev = Some(cur);
                        if i == 0 {
                            // This node becomes the tail after reversal
                            tail_ptr = &mut **prev_rev.as_mut().unwrap() as *mut ListNode;
                        }
                        cur_opt = nxt;
                    }
                }

                // Connect reversed group with previous part
                (*prev).next = prev_rev;

                // Move prev to the tail of the reversed group for next iteration
                prev = tail_ptr;
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

;; helper: return the k-th node starting from `node` (1-indexed), or #f if not enough nodes
(define (get-kth node k)
  (let loop ((curr node) (i 1))
    (if (or (not curr) (> i k))
        #f
        (if (= i k)
            curr
            (loop (list-node-next curr) (+ i 1))))))

;; main function
(define/contract (reverse-k-group head k)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (if (not head)
      #f
      (let* ((dummy (make-list-node 0))
             (prev dummy))
        (set-list-node-next! dummy head)
        (let outer ()
          (define start (list-node-next prev))
          (define kth (and start (get-kth start k)))
          (if (not kth)
              (void) ; not enough nodes left
              (begin
                (define next-group (list-node-next kth))
                ;; reverse exactly k nodes
                (let rev ((cur start) (prev2 next-group) (cnt 0))
                  (when (< cnt k)
                    (define temp (list-node-next cur))
                    (set-list-node-next! cur prev2)
                    (rev temp cur (+ cnt 1))))
                ;; reconnect reversed segment
                (set-list-node-next! prev kth)
                ;; move `prev` to the tail of the reversed segment (original start)
                (set! prev start)
                (outer))))
        (list-node-next dummy))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec reverse_k_group(Head :: #list_node{} | null, K :: integer()) -> #list_node{} | null.
reverse_k_group(null, _) ->
    null;
reverse_k_group(Head, K) when K =< 1 ->
    Head;
reverse_k_group(Head, K) ->
    case split(Head, K) of
        {true, Rest} ->
            ProcessedRest = reverse_k_group(Rest, K),
            reverse_k_nodes(Head, K, ProcessedRest);
        {false, _} ->
            Head
    end.

-spec split(Node :: #list_node{} | null, K :: integer()) -> {boolean(), #list_node{} | null}.
split(Node, 0) ->
    {true, Node};
split(null, _) ->
    {false, null};
split(#list_node{next = Next}, N) when N > 0 ->
    split(Next, N - 1).

-spec reverse_k_nodes(Node :: #list_node{} | null, K :: integer(), Prev :: #list_node{} | null) -> #list_node{} | null.
reverse_k_nodes(_, 0, Prev) ->
    Prev;
reverse_k_nodes(#list_node{val = Val, next = Next}, K, Prev) ->
    NewNode = #list_node{val = Val, next = Prev},
    reverse_k_nodes(Next, K - 1, NewNode).
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_k_group(head :: ListNode.t() | nil, k :: integer) :: ListNode.t() | nil
  def reverse_k_group(head, k) do
    if enough?(head, k) do
      {new_head, new_tail, rest} = reverse_first_k(head, k)
      %ListNode{new_tail | next: reverse_k_group(rest, k)}
      new_head
    else
      head
    end
  end

  defp enough?(_, 0), do: true
  defp enough?(nil, _k), do: false
  defp enough?(%ListNode{next: nxt}, k) when k > 0 do
    enough?(nxt, k - 1)
  end

  defp reverse_first_k(head, k) do
    rev(head, k, nil, nil)
  end

  defp rev(current, 0, prev, tail) do
    {prev, tail, current}
  end

  defp rev(%ListNode{val: v, next: nxt}, k, prev, nil) when k > 0 do
    new_node = %ListNode{val: v, next: prev}
    rev(nxt, k - 1, new_node, new_node)
  end

  defp rev(%ListNode{val: v, next: nxt}, k, prev, tail) when k > 0 do
    new_node = %ListNode{val: v, next: prev}
    rev(nxt, k - 1, new_node, tail)
  end
end
```
