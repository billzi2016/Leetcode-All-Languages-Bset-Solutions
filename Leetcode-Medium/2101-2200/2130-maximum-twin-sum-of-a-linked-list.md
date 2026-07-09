# 2130. Maximum Twin Sum of a Linked List

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
    int pairSum(ListNode* head) {
        if (!head) return 0;
        // Find start of second half
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        // Reverse second half
        ListNode* prev = nullptr;
        ListNode* curr = slow;
        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        // Compute max twin sum
        int maxSum = 0;
        ListNode* p1 = head;
        ListNode* p2 = prev; // head of reversed second half
        while (p2) {
            int sum = p1->val + p2->val;
            if (sum > maxSum) maxSum = sum;
            p1 = p1->next;
            p2 = p2->next;
        }
        // Optional: restore original list (not required for answer)
        // Reverse second half back
        curr = prev;
        prev = nullptr;
        while (curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        // Reconnect if needed (head's next should point to restored part)
        // Since we don't keep a pointer to the node before slow, and list is even,
        // the original connection can be re-established by traversing to middle again.
        // This step is omitted as LeetCode does not require list restoration.

        return maxSum;
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
    public int pairSum(ListNode head) {
        if (head == null) return 0;
        
        // Find start of second half
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Reverse second half
        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        
        // Compute max twin sum
        int maxSum = 0;
        ListNode p1 = head, p2 = prev;
        while (p2 != null) {
            int sum = p1.val + p2.val;
            if (sum > maxSum) maxSum = sum;
            p1 = p1.next;
            p2 = p2.next;
        }
        
        // Optional: restore the list (not required for answer)
        // Reverse again to restore original order
        curr = prev;
        prev = null;
        while (curr != null) {
            ListNode nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        
        return maxSum;
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
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Find start of second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compute max twin sum
        max_sum = 0
        p1, p2 = head, prev
        while p2:
            s = p1.val + p2.val
            if s > max_sum:
                max_sum = s
            p1 = p1.next
            p2 = p2.next

        # (Optional) Restore list - omitted as not required
        return max_sum
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
    def pairSum(self, head: Optional['ListNode']) -> int:
        # Find start of second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Compute max twin sum
        max_sum = 0
        p1, p2 = head, prev
        while p2:
            max_sum = max(max_sum, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next

        # (Optional) Restore the list - not required for answer
        return max_sum
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
int pairSum(struct ListNode* head) {
    // Find the start of second half using slow and fast pointers
    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Reverse the second half
    struct ListNode *prev = NULL, *curr = slow, *tmp;
    while (curr) {
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }
    
    // Compute maximum twin sum
    int maxSum = 0;
    struct ListNode *p1 = head, *p2 = prev;
    while (p2) {
        int sum = p1->val + p2->val;
        if (sum > maxSum) maxSum = sum;
        p1 = p1->next;
        p2 = p2->next;
    }
    
    return maxSum;
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
    public int PairSum(ListNode head) {
        if (head == null) return 0;

        // Find middle of the list
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse second half starting from 'slow'
        ListNode prev = null;
        ListNode curr = slow;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        // 'prev' is now the head of reversed second half

        int maxSum = 0;
        ListNode firstPtr = head;
        ListNode secondPtr = prev;
        while (secondPtr != null) {
            int sum = firstPtr.val + secondPtr.val;
            if (sum > maxSum) maxSum = sum;
            firstPtr = firstPtr.next;
            secondPtr = secondPtr.next;
        }

        // Optional: restore the original list order (not required for answer)
        // Reverse again to restore
        curr = prev;
        prev = null;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }

        return maxSum;
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
 * @return {number}
 */
var pairSum = function(head) {
    // Find the start of second half using slow/fast pointers
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Reverse the second half in-place
    let prev = null;
    let curr = slow;
    while (curr) {
        const nxt = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nxt;
    }
    
    // Compute maximum twin sum
    let maxSum = 0;
    let p1 = head, p2 = prev;
    while (p2) {
        const sum = p1.val + p2.val;
        if (sum > maxSum) maxSum = sum;
        p1 = p1.next;
        p2 = p2.next;
    }
    
    // (Optional) Restore the list by reversing again – omitted as not required
    
    return maxSum;
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

function pairSum(head: ListNode | null): number {
    if (!head) return 0;

    // Find start of second half
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;
    while (fast && fast.next) {
        slow = slow!.next!;
        fast = fast.next.next!;
    }

    // Reverse second half
    const reverse = (node: ListNode | null): ListNode | null => {
        let prev: ListNode | null = null;
        let curr: ListNode | null = node;
        while (curr) {
            const nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    };
    const secondHalfReversed = reverse(slow);

    // Compute max twin sum
    let p1: ListNode | null = head;
    let p2: ListNode | null = secondHalfReversed;
    let maxSum = 0;
    while (p2) {
        const curSum = p1!.val + p2.val;
        if (curSum > maxSum) maxSum = curSum;
        p1 = p1!.next;
        p2 = p2.next;
    }

    // Optional: restore original list (not required for answer)
    // reverse(secondHalfReversed);

    return maxSum;
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
     * @return int
     */
    function pairSum($head) {
        // Find start of second half
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        // Reverse second half
        $second = $this->reverseList($slow);
        $first = $head;

        $maxSum = 0;
        while ($second !== null) {
            $currSum = $first->val + $second->val;
            if ($currSum > $maxSum) {
                $maxSum = $currSum;
            }
            $first = $first->next;
            $second = $second->next;
        }

        return $maxSum;
    }

    /**
     * @param ListNode|null $head
     * @return ListNode|null
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
class Solution {
    func pairSum(_ head: ListNode?) -> Int {
        guard var slow = head, var fast = head else { return 0 }
        // Find the start of the second half
        while fast != nil && fast!.next != nil {
            slow = slow!.next!
            fast = fast!.next!.next
        }
        // Reverse the second half
        let reversedSecond = reverse(slow)
        var firstPtr = head
        var secondPtr = reversedSecond
        var maxSum = 0
        while let node1 = firstPtr, let node2 = secondPtr {
            let sum = node1.val + node2.val
            if sum > maxSum { maxSum = sum }
            firstPtr = node1.next
            secondPtr = node2.next
        }
        // Optional: restore the list (not required for answer)
        _ = reverse(reversedSecond)
        return maxSum
    }

    private func reverse(_ head: ListNode?) -> ListNode? {
        var prev: ListNode? = nil
        var curr = head
        while let node = curr {
            let nextTmp = node.next
            node.next = prev
            prev = node
            curr = nextTmp
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
    fun pairSum(head: ListNode?): Int {
        if (head == null) return 0

        // Find start of second half
        var slow: ListNode? = head
        var fast: ListNode? = head
        while (fast != null && fast.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }

        // Reverse second half
        var prev: ListNode? = null
        var curr = slow
        while (curr != null) {
            val nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        }

        // Compute max twin sum
        var first = head
        var second = prev
        var maxSum = 0
        while (second != null) {
            val sum = (first?.`val` ?: 0) + second.`val`
            if (sum > maxSum) maxSum = sum
            first = first?.next
            second = second.next
        }

        // Optional: restore list (not required for answer)

        return maxSum
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
  int pairSum(ListNode? head) {
    if (head == null) return 0;

    // Find the start of second half
    ListNode? slow = head;
    ListNode? fast = head;
    while (fast != null && fast.next != null) {
      slow = slow!.next;
      fast = fast.next!.next;
    }

    // Reverse second half
    ListNode? prev = null;
    ListNode? curr = slow;
    while (curr != null) {
      ListNode? nxt = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nxt;
    }

    // Compute max twin sum
    int maxSum = 0;
    ListNode? p1 = head;
    ListNode? p2 = prev;
    while (p2 != null) {
      int sum = p1!.val + p2.val;
      if (sum > maxSum) maxSum = sum;
      p1 = p1.next;
      p2 = p2.next;
    }

    return maxSum;
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
func pairSum(head *ListNode) int {
	// Find the start of second half using slow and fast pointers
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// Reverse the second half
	second := reverse(slow)

	maxSum := 0
	p1, p2 := head, second
	for p2 != nil {
		if s := p1.Val + p2.Val; s > maxSum {
			maxSum = s
		}
		p1 = p1.Next
		p2 = p2.Next
	}

	// Optional: restore the original list (not required for answer)
	// reverse(second)

	return maxSum
}

// Helper to reverse a linked list and return new head
func reverse(head *ListNode) *ListNode {
	var prev *ListNode
	curr := head
	for curr != nil {
		next := curr.Next
		curr.Next = prev
		prev = curr
		curr = next
	}
	return prev
}
```

## Ruby

```ruby
def pair_sum(head)
  # Find the start of the second half using slow and fast pointers
  slow = head
  fast = head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  # Reverse the second half of the list
  prev = nil
  curr = slow
  while curr
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  end

  # Compute maximum twin sum
  max_sum = 0
  p1 = head
  p2 = prev
  while p2
    s = p1.val + p2.val
    max_sum = s if s > max_sum
    p1 = p1.next
    p2 = p2.next
  end

  max_sum
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
    def pairSum(head: ListNode): Int = {
        // Find the start of second half using slow and fast pointers
        var slow: ListNode = head
        var fast: ListNode = head
        while (fast != null && fast.next != null) {
            slow = slow.next
            fast = fast.next.next
        }

        // Reverse the second half
        var prev: ListNode = null
        var curr: ListNode = slow
        while (curr != null) {
            val next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        }

        // Compute maximum twin sum
        var p1: ListNode = head
        var p2: ListNode = prev
        var maxSum = 0
        while (p2 != null) {
            val sum = p1.x + p2.x
            if (sum > maxSum) maxSum = sum
            p1 = p1.next
            p2 = p2.next
        }

        // Return the result (restoring list is unnecessary for this problem)
        maxSum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let mut vals = Vec::new();
        let mut cur = &head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = &node.next;
        }
        let n = vals.len();
        let mut max_sum = 0;
        for i in 0..n / 2 {
            let s = vals[i] + vals[n - 1 - i];
            if s > max_sum {
                max_sum = s;
            }
        }
        max_sum
    }
}
```

## Racket

```racket
; Definition for singly-linked list:
#|
(struct list-node
  (val next) #:mutable #:transparent)

(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (pair-sum head)
  (-> (or/c list-node? #f) exact-integer?)
  (if (not head)
      0
      (let ()
        ;; Find the start of the second half
        (define slow head)
        (define fast head)
        (let loop ()
          (when (and fast (list-node-next fast))
            (set! slow (list-node-next slow))
            (set! fast (list-node-next (list-node-next fast)))
            (loop)))
        ;; Reverse the second half
        (define prev #f)
        (define curr slow)
        (let rev ()
          (when curr
            (define next (list-node-next curr))
            (set-list-node-next! curr prev)
            (set! prev curr)
            (set! curr next)
            (rev)))
        (define second-head prev)
        ;; Compute maximum twin sum
        (define p1 head)
        (define p2 second-head)
        (define max-sum 0)
        (let comp ()
          (when (and p1 p2)
            (define s (+ (list-node-val p1) (list-node-val p2)))
            (when (> s max-sum) (set! max-sum s))
            (set! p1 (list-node-next p1))
            (set! p2 (list-node-next p2))
            (comp)))
        max-sum)))
```

## Erlang

```erlang
-module(solution).
-export([pair_sum/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec pair_sum(Head :: #list_node{} | null) -> integer().
pair_sum(null) ->
    0;
pair_sum(Head) ->
    SecondHalfStart = find_second_half_start(Head),
    RevSecond = reverse_list(SecondHalfStart),
    max_twin_sum(Head, RevSecond, 0).

%% Find the start node of the second half (index n/2)
find_second_half_start(Head) ->
    find_middle(Head, Head).

find_middle(Slow, Fast) ->
    case {Fast, next(Fast)} of
        {null, _} -> Slow;
        {_, null} -> Slow;
        {_ , _} ->
            NextSlow = next(Slow),
            NextFast = next(next(Fast)),
            find_middle(NextSlow, NextFast)
    end.

next(null) -> null;
next(#list_node{} = Node) -> Node#list_node.next.

%% Reverse a linked list and return the new head
reverse_list(Head) ->
    rev(Head, null).

rev(null, Acc) -> Acc;
rev(Node, Acc) ->
    Next = next(Node),
    NewNode = Node#list_node{next=Acc},
    rev(Next, NewNode).

%% Compute maximum twin sum using two pointers
max_twin_sum(_P1, null, Max) -> Max;
max_twin_sum(P1, P2, MaxSoFar) ->
    Sum = P1#list_node.val + P2#list_node.val,
    NewMax = if Sum > MaxSoFar -> Sum; true -> MaxSoFar end,
    max_twin_sum(next(P1), next(P2), NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec pair_sum(head :: ListNode.t | nil) :: integer
  def pair_sum(head) do
    {_prev, second_half_start} = find_mid(nil, head, head)
    rev = reverse_list(second_half_start, nil)
    max_twin_sum(head, rev, 0)
  end

  defp find_mid(prev, slow, fast) do
    case fast do
      nil ->
        {prev, slow}

      %ListNode{next: nil} ->
        {prev, slow}

      %ListNode{next: %ListNode{} = f_next} ->
        find_mid(slow, slow.next, f_next.next)
    end
  end

  defp reverse_list(nil, acc), do: acc

  defp reverse_list(%ListNode{val: v, next: nxt}, acc) do
    new_node = %ListNode{val: v, next: acc}
    reverse_list(nxt, new_node)
  end

  defp max_twin_sum(_first, nil, current_max), do: current_max

  defp max_twin_sum(%ListNode{val: v1, next: nxt1}, %ListNode{val: v2, next: nxt2}, current_max) do
    sum = v1 + v2
    new_max = if sum > current_max, do: sum, else: current_max
    max_twin_sum(nxt1, nxt2, new_max)
  end
end
```
