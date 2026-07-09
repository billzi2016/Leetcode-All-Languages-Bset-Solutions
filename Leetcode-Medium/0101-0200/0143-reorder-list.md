# 0143. Reorder List

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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;
        
        // Find middle of the list
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Split and reverse second half
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* prev = nullptr;
        while (second) {
            ListNode* nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }
        
        // Merge two halves
        ListNode* first = head;
        second = prev;
        while (second) {
            ListNode* tmp1 = first->next;
            ListNode* tmp2 = second->next;
            first->next = second;
            second->next = tmp1;
            first = tmp1;
            second = tmp2;
        }
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
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // Find the middle of the list
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Split and reverse the second half
        ListNode second = slow.next;
        slow.next = null;
        ListNode prev = null;
        while (second != null) {
            ListNode nxt = second.next;
            second.next = prev;
            prev = second;
            second = nxt;
        }
        second = prev; // head of reversed second half

        // Merge the two halves
        ListNode first = head;
        while (second != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;

            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2;
        }
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
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split and reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev
        
        # Merge two halves alternately
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reorderList(self, head: Optional['ListNode']) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split and reverse the second half
        second = slow.next
        slow.next = None  # terminate first half
        
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev  # head of reversed second half
        
        # Merge two halves alternately
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
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
void reorderList(struct ListNode* head) {
    if (!head || !head->next) return;

    // Find middle of the list
    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Split and reverse second half
    struct ListNode *second = slow->next;
    slow->next = NULL;

    struct ListNode *prev = NULL, *curr = second, *tmp;
    while (curr) {
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }
    // 'prev' is the head of reversed second half
    second = prev;

    // Merge two halves alternately
    struct ListNode *first = head;
    while (second) {
        struct ListNode *tmp1 = first->next;
        struct ListNode *tmp2 = second->next;

        first->next = second;
        second->next = tmp1;

        first = tmp1;
        second = tmp2;
    }
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
    public void ReorderList(ListNode head) {
        if (head == null || head.next == null) return;

        // Find middle of the list
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse second half
        ListNode prev = null;
        ListNode curr = slow.next;
        while (curr != null) {
            ListNode nextTmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTmp;
        }
        // Cut the first half
        slow.next = null;

        // Merge two halves
        ListNode first = head;
        ListNode second = prev;
        while (second != null) {
            ListNode tmp1 = first.next;
            ListNode tmp2 = second.next;

            first.next = second;
            second.next = tmp1;

            first = tmp1;
            second = tmp2;
        }
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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if (!head || !head.next) return;
    
    // Find the middle of the list (end of first half)
    let slow = head, fast = head.next;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Split and reverse second half
    let second = slow.next;
    slow.next = null;
    let prev = null;
    while (second) {
        const nxt = second.next;
        second.next = prev;
        prev = second;
        second = nxt;
    }
    second = prev; // head of reversed second half
    
    // Merge two halves alternately
    let first = head;
    while (second) {
        const tmp1 = first.next;
        const tmp2 = second.next;
        
        first.next = second;
        second.next = tmp1;
        
        first = tmp1;
        second = tmp2;
    }
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

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    if (!head || !head.next) return;

    // Find the middle of the list (end of first half)
    let slow: ListNode = head;
    let fast: ListNode | null = head.next;
    while (fast && fast.next) {
        slow = slow.next!;
        fast = fast.next.next;
    }

    // Split and reverse the second half
    let second: ListNode | null = slow.next;
    slow.next = null;

    let prev: ListNode | null = null;
    let curr: ListNode | null = second;
    while (curr) {
        const nextTmp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTmp;
    }

    // Merge the two halves
    let first: ListNode | null = head;
    let secondRev: ListNode | null = prev;
    while (secondRev) {
        const tmp1 = first!.next;
        const tmp2 = secondRev.next;

        first!.next = secondRev;
        secondRev.next = tmp1;

        first = tmp1!;
        secondRev = tmp2;
    }
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
     * @return NULL
     */
    function reorderList($head) {
        if ($head === null || $head->next === null) {
            return;
        }

        // Find middle of the list
        $slow = $head;
        $fast = $head;
        while ($fast->next !== null && $fast->next->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        // Split and reverse second half
        $second = $slow->next;
        $slow->next = null;

        $prev = null;
        while ($second !== null) {
            $tmp = $second->next;
            $second->next = $prev;
            $prev = $second;
            $second = $tmp;
        }
        $second = $prev; // head of reversed second half

        // Merge two halves
        $first = $head;
        while ($second !== null) {
            $tmp1 = $first->next;
            $tmp2 = $second->next;

            $first->next = $second;
            $second->next = $tmp1;

            $first = $tmp1;
            $second = $tmp2;
        }
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
    func reorderList(_ head: ListNode?) {
        guard let head = head, head.next != nil else { return }
        
        // Find the middle of the list
        var slow: ListNode? = head
        var fast: ListNode? = head
        while fast?.next != nil && fast?.next?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }
        
        // Split and reverse the second half
        var second = slow?.next
        slow?.next = nil
        var prev: ListNode? = nil
        while let curr = second {
            let nextTmp = curr.next
            curr.next = prev
            prev = curr
            second = nextTmp
        }
        
        // Merge the two halves
        var first: ListNode? = head
        var secondRev: ListNode? = prev
        while secondRev != nil {
            let tmp1 = first?.next
            let tmp2 = secondRev?.next
            
            first?.next = secondRev
            secondRev?.next = tmp1
            
            first = tmp1
            secondRev = tmp2
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reorderList(head: ListNode?) {
        if (head == null || head.next == null) return

        // Find the middle of the list
        var slow = head
        var fast = head
        while (fast?.next != null && fast.next?.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }

        // Split and reverse the second half
        var second = slow!!.next
        slow.next = null

        var prev: ListNode? = null
        var curr = second
        while (curr != null) {
            val nextTmp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTmp
        }

        // Merge the two halves
        var first = head
        var secondRev = prev
        while (secondRev != null) {
            val tmp1 = first!!.next
            val tmp2 = secondRev.next

            first.next = secondRev
            secondRev.next = tmp1

            first = tmp1
            secondRev = tmp2
        }
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
  void reorderList(ListNode? head) {
    if (head == null || head.next == null) return;

    // Find the middle of the list
    ListNode? slow = head;
    ListNode? fast = head;
    while (fast?.next != null && fast!.next!.next != null) {
      slow = slow!.next;
      fast = fast.next!.next;
    }

    // Split and reverse the second half
    ListNode? second = slow!.next;
    slow.next = null;

    ListNode? prev = null;
    while (second != null) {
      ListNode? nextTmp = second.next;
      second.next = prev;
      prev = second;
      second = nextTmp;
    }

    // Merge the two halves
    ListNode? first = head;
    ListNode? secondRev = prev;
    while (secondRev != null) {
      ListNode? tmp1 = first!.next;
      ListNode? tmp2 = secondRev.next;

      first.next = secondRev;
      secondRev.next = tmp1;

      first = tmp1;
      secondRev = tmp2;
    }
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
func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}
	// Find the middle of the list
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// Split and reverse the second half
	second := slow.Next
	slow.Next = nil

	var prev *ListNode
	curr := second
	for curr != nil {
		nextTmp := curr.Next
		curr.Next = prev
		prev = curr
		curr = nextTmp
	}

	// Merge the two halves
	first, secondRev := head, prev
	for secondRev != nil {
		tmp1 := first.Next
		tmp2 := secondRev.Next

		first.Next = secondRev
		secondRev.Next = tmp1

		first = tmp1
		secondRev = tmp2
	}
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

def reorder_list(head)
  return if head.nil? || head.next.nil?

  # Find the middle of the list (end of first half)
  slow = head
  fast = head.next
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  # Split and reverse the second half
  second = slow.next
  slow.next = nil

  prev = nil
  cur = second
  while cur
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  end
  second = prev

  # Merge two halves alternately
  first = head
  while second
    tmp1 = first.next
    tmp2 = second.next

    first.next = second
    second.next = tmp1

    first = tmp1
    second = tmp2
  end
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
  def reorderList(head: ListNode): Unit = {
    if (head == null || head.next == null) return

    // Find middle and split the list into two halves
    var slow: ListNode = head
    var fast: ListNode = head
    var prev: ListNode = null
    while (fast != null && fast.next != null) {
      prev = slow
      slow = slow.next
      fast = fast.next.next
    }
    if (prev != null) prev.next = null

    // Reverse the second half
    var prevNode: ListNode = null
    var curr: ListNode = slow
    while (curr != null) {
      val nextTmp = curr.next
      curr.next = prevNode
      prevNode = curr
      curr = nextTmp
    }

    // Merge the two halves alternately
    var first: ListNode = head
    var second: ListNode = prevNode
    while (second != null) {
      val tmp1 = first.next
      val tmp2 = second.next

      first.next = second
      if (tmp1 == null) return
      second.next = tmp1

      first = tmp1
      second = tmp2
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        // Extract all nodes into a vector, taking ownership.
        let mut nodes: Vec<Option<Box<ListNode>>> = Vec::new();
        while let Some(mut node) = head.take() {
            let next = node.next.take(); // detach the rest of the list
            nodes.push(Some(node));
            *head = next;
        }

        let n = nodes.len();
        if n <= 1 {
            // Reattach the single node (or empty) and return.
            if n == 1 {
                *head = nodes[0].take();
            }
            return;
        }

        // Build the reordered list using the collected nodes.
        let mut dummy: Option<Box<ListNode>> = None;
        let mut tail = &mut dummy;

        let mut i = 0usize;
        let mut j = n - 1;
        while i < j {
            // Take node from the front.
            let left_node = nodes[i].take().unwrap();
            *tail = Some(left_node);
            tail = &mut tail.as_mut().unwrap().next;

            // Take node from the back.
            let right_node = nodes[j].take().unwrap();
            *tail = Some(right_node);
            tail = &mut tail.as_mut().unwrap().next;

            i += 1;
            if j == 0 { break; } // safeguard, though shouldn't happen here
            j -= 1;
        }

        // If there is a middle node left (odd length), attach it.
        if i == j {
            let mid_node = nodes[i].take().unwrap();
            *tail = Some(mid_node);
            tail = &mut tail.as_mut().unwrap().next;
        }

        // Terminate the list.
        *tail = None;

        // Set the head to the newly built reordered list.
        *head = dummy;
    }
}
```

## Racket

```racket
; Definition for singly-linked list:
#|
(struct list-node
  (val next) #:mutable #:transparent)
|#

(define/contract (reorder-list head)
  (-> (or/c list-node? #f) void?)
  (when (and head (list-node-next head))
    ;; find middle of the list
    (define middle head)
    (define fast (list-node-next head))
    (let loop ()
      (if (and fast (list-node-next fast))
          (begin
            (set! middle (list-node-next middle))
            (set! fast (list-node-next (list-node-next fast)))
            (loop))
          (void)))
    ;; split the list into two halves
    (define second (list-node-next middle))
    (set-list-node-next! middle #f)
    ;; reverse the second half
    (define prev #f)
    (let rev ((curr second))
      (when curr
        (define nxt (list-node-next curr))
        (set-list-node-next! curr prev)
        (set! prev curr)
        (rev nxt)))
    (define second-rev prev)
    ;; merge the two halves alternately
    (define first head)
    (let merge ((f first) (s second-rev))
      (when s
        (define tmp1 (list-node-next f))
        (define tmp2 (list-node-next s))
        (set-list-node-next! f s)
        (set-list-node-next! s tmp1)
        (merge tmp1 tmp2)))
    (void)))
```
