# 2074. Reverse Nodes in Even Length Groups

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
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        if (!head) return nullptr;
        ListNode dummy(0, head);
        ListNode* prevTail = &dummy;   // node before current group
        ListNode* cur = head;
        int groupSize = 1;
        
        while (cur) {
            // Determine actual length of this group
            int cnt = 0;
            ListNode* temp = cur;
            while (cnt < groupSize && temp) {
                ++cnt;
                temp = temp->next;   // temp points to node after the group
            }
            
            if (cnt % 2 == 0) { // need to reverse this even-length group
                ListNode* prev = temp;      // will become next of reversed tail
                ListNode* node = cur;
                for (int i = 0; i < cnt; ++i) {
                    ListNode* nxt = node->next;
                    node->next = prev;
                    prev = node;
                    node = nxt;
                }
                // Connect previous part with new head of reversed segment
                prevTail->next = prev;
                // After reversal, cur becomes the tail of this group
                prevTail = cur;
            } else { // odd length, keep order
                // Move prevTail to the last node of this group
                prevTail = cur;
                for (int i = 1; i < cnt; ++i) {
                    prevTail = prevTail->next;
                }
            }
            
            // Prepare for next iteration
            cur = temp;
            ++groupSize;
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
    public ListNode reverseEvenLengthGroups(ListNode head) {
        if (head == null) return null;
        ListNode dummy = new ListNode(0, head);
        ListNode prevGroupTail = dummy;
        ListNode cur = head;
        int groupSize = 1;

        while (cur != null) {
            // Determine actual size of the current group
            int cnt = 0;
            ListNode temp = cur;
            while (temp != null && cnt < groupSize) {
                temp = temp.next;
                cnt++;
            }

            if ((cnt & 1) == 0) { // even length, reverse this segment
                ListNode prev = null;
                ListNode node = cur;
                for (int i = 0; i < cnt; i++) {
                    ListNode nxt = node.next;
                    node.next = prev;
                    prev = node;
                    node = nxt;
                }
                // Connect reversed part with surrounding nodes
                prevGroupTail.next = prev;      // new head of this group
                cur.next = temp;               // original head becomes tail
                // Move pointers for next iteration
                prevGroupTail = cur;
                cur = temp;
            } else { // odd length, keep order
                for (int i = 0; i < cnt; i++) {
                    prevGroupTail = cur;
                    cur = cur.next;
                }
            }

            groupSize++;
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
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        # helper to reverse first k nodes starting at node 'start'
        def reverse_k(start, k):
            prev = None
            cur = start
            while k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            # prev is new head, start is new tail
            return prev, start

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy   # node before current group
        curr = head
        group_len = 1

        while curr:
            cnt = 0
            group_start = curr
            # traverse up to group_len nodes or until list ends
            while cnt < group_len and curr:
                cnt += 1
                curr = curr.next   # curr will be the first node of next group after loop

            if cnt % 2 == 0:
                # reverse this even-length group
                new_head, new_tail = reverse_k(group_start, cnt)
                prev_group_tail.next = new_head
                new_tail.next = curr
                prev_group_tail = new_tail
            else:
                # no reversal; move prev_group_tail to the last node of this group
                for _ in range(cnt):
                    prev_group_tail = prev_group_tail.next

            group_len += 1

        return dummy.next
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
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy  # tail of the processed part
        curr = head
        group_size = 1

        while curr:
            # Determine actual size of this group
            cnt = 0
            node = curr
            while node and cnt < group_size:
                node = node.next
                cnt += 1
            next_group_head = node  # start of the following group

            if cnt % 2 == 0:  # need to reverse
                # Reverse cnt nodes starting at curr
                rev_head, rev_tail = self._reverse_sublist(curr, cnt)
                prev_group_tail.next = rev_head
                rev_tail.next = next_group_head
                # Update pointers for next iteration
                prev_group_tail = rev_tail
                curr = next_group_head
            else:
                # No reversal; just move prev_group_tail to the last node of this group
                for _ in range(cnt):
                    prev_group_tail = curr
                    curr = curr.next
                # curr is already at next_group_head
            group_size += 1

        return dummy.next

    def _reverse_sublist(self, head: ListNode, k: int):
        """Reverse first k nodes of list starting at head.
        Returns (new_head, new_tail)."""
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # prev is new head, original head becomes tail
        return prev, head
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
struct ListNode* reverseEvenLengthGroups(struct ListNode* head) {
    if (!head) return NULL;
    
    // Dummy node to simplify connections
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prevGroupTail = &dummy;   // node before current group
    struct ListNode *curr = head;              // first node of current group
    
    int groupSize = 1;
    
    while (curr) {
        // Determine actual size of this group and the node after the group
        struct ListNode *groupEnd = curr;
        int cnt = 0;
        while (cnt < groupSize && groupEnd) {
            groupEnd = groupEnd->next;
            cnt++;
        }
        
        if (cnt % 2 == 0) { // need to reverse this even-length group
            struct ListNode *prev = NULL;
            struct ListNode *node = curr;
            for (int i = 0; i < cnt; ++i) {
                struct ListNode *nextTmp = node->next;
                node->next = prev;
                prev = node;
                node = nextTmp;
            }
            // 'prev' is new head of reversed segment, 'curr' becomes its tail
            prevGroupTail->next = prev;   // connect previous part to new head
            curr->next = groupEnd;        // connect tail to the rest of list
            
            // Move pointers forward for next iteration
            prevGroupTail = curr;
            curr = groupEnd;
        } else { // odd length, keep order
            for (int i = 0; i < cnt; ++i) {
                prevGroupTail = curr;
                curr = curr->next;
            }
        }
        
        ++groupSize;
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
    public ListNode ReverseEvenLengthGroups(ListNode head) {
        if (head == null) return null;

        ListNode dummy = new ListNode(0, head);
        ListNode prevGroupTail = dummy; // node before the current group
        int groupSize = 1;

        while (head != null) {
            // Determine actual length of this group
            int count = 0;
            ListNode cur = head;
            while (cur != null && count < groupSize) {
                cur = cur.next;
                count++;
            }

            if ((count & 1) == 0) { // even length, reverse the segment
                ListNode prev = null;
                ListNode node = head;
                for (int i = 0; i < count; i++) {
                    ListNode nxt = node.next;
                    node.next = prev;
                    prev = node;
                    node = nxt;
                }
                // Connect reversed part with surrounding nodes
                prevGroupTail.next = prev;      // new head of this group
                head.next = node;               // original head is now tail
                // Move pointers forward for next iteration
                prevGroupTail = head;
                head = node;
            } else { // odd length, keep order
                for (int i = 0; i < count; i++) {
                    prevGroupTail = head;
                    head = head.next;
                }
            }

            groupSize++;
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
var reverseEvenLengthGroups = function(head) {
    if (!head) return null;
    const dummy = new ListNode(0, head);
    let prevGroupTail = dummy; // tail of the processed part
    let curr = head;           // start of current group
    let groupSize = 1;

    while (curr) {
        // Determine actual length of this group
        let count = 0;
        let node = curr;
        while (node && count < groupSize) {
            node = node.next;
            count++;
        }

        if (count % 2 === 0) { // need to reverse
            // Reverse 'count' nodes starting at curr
            let prev = null;
            let cur = curr;
            for (let i = 0; i < count; i++) {
                const nxt = cur.next;
                cur.next = prev;
                prev = cur;
                cur = nxt;
            }
            // Connect reversed segment with surrounding parts
            prevGroupTail.next = prev;   // prev is new head of this segment
            curr.next = cur;             // curr (original head) becomes tail
            // Move pointers for next iteration
            prevGroupTail = curr;
            curr = cur;
        } else {
            // No reversal, just skip the group
            for (let i = 0; i < count; i++) {
                prevGroupTail = curr;
                curr = curr.next;
            }
        }

        groupSize++;
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

function reverseEvenLengthGroups(head: ListNode | null): ListNode | null {
    if (!head) return null;
    const dummy = new ListNode(0, head);
    let prevGroupTail: ListNode = dummy;
    let current: ListNode | null = head;
    let groupSize = 1;

    while (current) {
        // Determine actual size of this group
        let cnt = 0;
        let node = current;
        while (node && cnt < groupSize) {
            node = node.next;
            cnt++;
        }
        const nextGroupStart = node; // may be null

        if (cnt % 2 === 0) {
            // Reverse the even-length group
            let prev: ListNode | null = null;
            let cur: ListNode | null = current;
            for (let i = 0; i < cnt; i++) {
                const nxt = cur!.next;
                cur!.next = prev;
                prev = cur!;
                cur = nxt;
            }
            // Connect reversed segment with surrounding parts
            prevGroupTail.next = prev;
            current!.next = nextGroupStart;

            // Move pointers forward for next iteration
            prevGroupTail = current!;
            current = nextGroupStart;
        } else {
            // No reversal; just advance pointers through the group
            for (let i = 0; i < cnt; i++) {
                prevGroupTail = current!;
                current = current!.next;
            }
        }

        groupSize++;
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
     * @return ListNode
     */
    function reverseEvenLengthGroups($head) {
        if ($head === null) return null;

        $dummy = new ListNode(0, $head);
        $prevGroupTail = $dummy;
        $curr = $head;
        $groupSize = 1;

        while ($curr !== null) {
            // Determine actual size of the current group
            $cnt = 0;
            $temp = $curr;
            while ($temp !== null && $cnt < $groupSize) {
                $cnt++;
                $temp = $temp->next;
            }

            if ($cnt % 2 == 0) { // even length, reverse this group
                $prev = null;
                $node = $curr;
                for ($i = 0; $i < $cnt; $i++) {
                    $nextNode = $node->next;
                    $node->next = $prev;
                    $prev = $node;
                    $node = $nextNode;
                }
                // Connect reversed group with surrounding parts
                $prevGroupTail->next = $prev;   // new head of this group
                $curr->next = $node;            // $curr is now the tail after reversal
                $prevGroupTail = $curr;         // move tail pointer to end of this group
            } else { // odd length, keep order
                for ($i = 1; $i < $cnt; $i++) {
                    $curr = $curr->next;
                }
                $prevGroupTail = $curr;
                $node = $curr->next;
            }

            // Move to the next group
            $curr = $node ?? null;
            $groupSize++;
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
    func reverseEvenLengthGroups(_ head: ListNode?) -> ListNode? {
        guard let head = head else { return nil }
        var newHead: ListNode? = head
        var prevTail: ListNode? = nil          // tail of the previous processed group
        var curr: ListNode? = head             // start node of current group
        var groupSize = 1
        
        while let start = curr {
            var count = 0
            var node: ListNode? = start
            var lastInGroup: ListNode? = nil
            
            // Determine actual size of this group and its last node
            while count < groupSize && node != nil {
                count += 1
                lastInGroup = node
                node = node!.next
            }
            
            let nextGroupHead = node   // first node of the following group (may be nil)
            
            if count % 2 == 0 {
                // Reverse this even-length segment
                var prev: ListNode? = nextGroupHead
                var cur: ListNode? = start
                for _ in 0..<count {
                    let nxt = cur!.next
                    cur!.next = prev
                    prev = cur
                    cur = nxt
                }
                // Connect with previous part
                if let pTail = prevTail {
                    pTail.next = prev
                } else {
                    newHead = prev
                }
                // After reversal, start becomes the tail of this segment
                prevTail = start
            } else {
                // No reversal; just move prevTail to the last node of this odd group
                if prevTail == nil {
                    newHead = start
                }
                prevTail = lastInGroup
            }
            
            // Move to next group
            curr = nextGroupHead
            groupSize += 1
        }
        
        return newHead
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
    fun reverseEvenLengthGroups(head: ListNode?): ListNode? {
        if (head == null) return null
        val dummy = ListNode(0)
        dummy.next = head
        var prevGroupTail: ListNode = dummy
        var curr: ListNode? = head
        var groupSize = 1

        while (curr != null) {
            // Determine actual size of the current group
            var count = 0
            var temp = curr
            while (temp != null && count < groupSize) {
                count++
                temp = temp.next
            }

            if (count % 2 == 0) {
                // Reverse this even-length group
                val groupHead = curr
                var prev: ListNode? = null
                var node = curr
                for (i in 0 until count) {
                    val nextNode = node!!.next
                    node.next = prev
                    prev = node
                    node = nextNode
                }
                // Connect reversed part with surrounding nodes
                prevGroupTail.next = prev          // new head of the group
                groupHead!!.next = node            // node is the first after the group
                prevGroupTail = groupHead           // update tail for next iteration
                curr = node                         // move to next group's start
            } else {
                // Keep order, just advance pointers
                for (i in 0 until count) {
                    prevGroupTail = curr!!
                    curr = curr!!.next
                }
            }

            groupSize++
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
  ListNode? reverseEvenLengthGroups(ListNode? head) {
    if (head == null) return null;

    // Dummy node to simplify connections
    final dummy = ListNode(0, head);
    ListNode? prevGroupTail = dummy;
    ListNode? current = head;
    int groupSize = 1;

    while (current != null) {
      // Determine actual size of this group
      int cnt = 0;
      ListNode? temp = current;
      while (temp != null && cnt < groupSize) {
        cnt++;
        temp = temp.next;
      }

      if (cnt % 2 == 0) {
        // Reverse the group in place
        ListNode? prev = null;
        ListNode? node = current;
        for (int i = 0; i < cnt; i++) {
          final nextNode = node!.next;
          node.next = prev;
          prev = node;
          node = nextNode;
        }
        // Connect reversed segment
        prevGroupTail!.next = prev;
        // 'current' is now the tail of the reversed segment
        current!.next = node;
        // Update pointers for next iteration
        prevGroupTail = current;
        current = node;
      } else {
        // No reversal; just move pointers to the end of this group
        for (int i = 0; i < cnt; i++) {
          prevGroupTail = current!;
          current = current!.next;
        }
      }

      groupSize++;
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
func reverseEvenLengthGroups(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy
    curr := head
    groupSize := 1

    for curr != nil {
        // Determine actual length of the current group
        cnt := 0
        temp := curr
        for cnt < groupSize && temp != nil {
            cnt++
            temp = temp.Next
        }

        if cnt%2 == 0 {
            // Reverse this even-length group
            newHead, newTail := reverseSegment(curr, cnt)
            prev.Next = newHead
            newTail.Next = temp
            prev = newTail
            curr = temp
        } else {
            // Skip this odd-length group without reversing
            for i := 0; i < cnt; i++ {
                prev = curr
                curr = curr.Next
            }
        }

        groupSize++
    }

    return dummy.Next
}

// reverseSegment reverses k nodes starting from start and returns the new head and tail.
func reverseSegment(start *ListNode, k int) (*ListNode, *ListNode) {
    var prev *ListNode
    cur := start
    for i := 0; i < k; i++ {
        nxt := cur.Next
        cur.Next = prev
        prev = cur
        cur = nxt
    }
    // prev is the new head after reversal, start becomes the tail.
    return prev, start
}
```

## Ruby

```ruby
def reverse_even_length_groups(head)
  return nil unless head
  dummy = ListNode.new(0)
  dummy.next = head
  prev_group_tail = dummy
  curr = head
  group_size = 1

  while curr
    cnt = 0
    node = curr
    while node && cnt < group_size
      node = node.next
      cnt += 1
    end
    next_head = node

    if cnt.even?
      prev = nil
      cur = curr
      i = 0
      while i < cnt
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        i += 1
      end
      new_head = prev
      new_tail = curr
    else
      new_head = curr
      new_tail = curr
      (cnt - 1).times { new_tail = new_tail.next }
    end

    prev_group_tail.next = new_head
    new_tail.next = next_head

    prev_group_tail = new_tail
    curr = next_head
    group_size += 1
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
    def reverseEvenLengthGroups(head: ListNode): ListNode = {
        val dummy = new ListNode(0)
        dummy.next = head
        var prev: ListNode = dummy
        var curr: ListNode = head
        var groupSize = 1

        while (curr != null) {
            // Determine actual size of the current group
            var cnt = 0
            var tail: ListNode = null
            var node = curr
            while (cnt < groupSize && node != null) {
                cnt += 1
                tail = node
                node = node.next
            }
            val nextGroupStart = node

            if (cnt % 2 == 0) {
                // Reverse the even-length group [curr, tail]
                var prevNode: ListNode = null
                var curNode: ListNode = curr
                var i = 0
                while (i < cnt) {
                    val nxt = curNode.next
                    curNode.next = prevNode
                    prevNode = curNode
                    curNode = nxt
                    i += 1
                }
                // Connect reversed segment back to the list
                prev.next = prevNode          // new head of this segment
                curr.next = nextGroupStart    // original head becomes tail
                prev = curr                   // move prev to the tail of reversed segment
            } else {
                // No reversal needed; just advance prev to the group's tail
                prev = tail
            }

            // Prepare for next group
            curr = nextGroupStart
            groupSize += 1
        }

        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reverse_even_length_groups(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Collect node values.
        let mut vals = Vec::new();
        let mut cur = head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = node.next;
        }

        // Process groups, reversing even‑length ones.
        let n = vals.len();
        let mut idx = 0usize;
        let mut group_len = 1usize;
        while idx < n {
            let remaining = n - idx;
            let cur_len = if remaining >= group_len { group_len } else { remaining };
            if cur_len % 2 == 0 {
                vals[idx..idx + cur_len].reverse();
            }
            idx += cur_len;
            group_len += 1;
        }

        // Rebuild the linked list from the reordered values.
        let mut new_head: Option<Box<ListNode>> = None;
        for &v in vals.iter().rev() {
            let mut node = Box::new(ListNode::new(v));
            node.next = new_head;
            new_head = Some(node);
        }
        new_head
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

(define/contract (reverse-even-length-groups head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (let loop ((prev #f)               ; node before current group
             (curr head)            ; first node of current group
             (group-size 1)         ; expected size of this group
             (new-head head))       ; possibly updated head of the whole list
    (if (not curr)
        new-head
        ;; determine actual length of this group and start of next group
        (let-values (((len next-start)
                      (let get ((node curr) (cnt 0))
                        (if (or (>= cnt group-size) (not node))
                            (values cnt node)
                            (get (list-node-next node) (+ cnt 1))))))
          (if (= (remainder len 2) 0)               ; even length → reverse
              (let ((rev-head                     ; head after reversal
                     (let rev ((prev #f) (node curr) (cnt len))
                       (if (= cnt 0)
                           prev
                           (let ((next (list-node-next node)))
                             (set-list-node-next! node prev)
                             (rev node next (- cnt 1)))))))
                ;; connect previous part with reversed segment
                (if prev
                    (set-list-node-next! prev rev-head)
                    (set! new-head rev-head))
                ;; curr is now the tail of the reversed segment
                (set-list-node-next! curr next-start)
                (loop curr next-start (+ group-size 1) new-head))
              ;; odd length → keep order, just move pointers
              (let ((tail                         ; last node of this group
                     (let find-tail ((node curr) (i 1))
                       (if (= i len)
                           node
                           (find-tail (list-node-next node) (+ i 1))))))
                (loop tail next-start (+ group-size 1) new-head)))))))
```

## Erlang

```erlang
-module(solution).
-export([reverse_even_length_groups/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec reverse_even_length_groups(Head :: #list_node{} | null) -> #list_node{} | null.
reverse_even_length_groups(Head) ->
    {NewHead, _} = solve(Head, 1),
    NewHead.

%% Process groups recursively, returning head and tail of the processed segment.
solve(null, _) ->
    {null, null};
solve(Curr, Size) ->
    {GroupNodes, NextNode} = collect_nodes(Curr, Size, []),
    Len = length(GroupNodes),
    Processed = if Len rem 2 == 0 -> lists:reverse(GroupNodes);
                true -> GroupNodes
               end,
    {RestHead, RestTail} = solve(NextNode, Size + 1),
    {GroupHead, GroupTail} = build_chain_with_next(Processed, RestHead),
    OverallTail = case RestTail of
        null -> GroupTail;
        _ -> RestTail
    end,
    {GroupHead, OverallTail}.

%% Collect up to Count nodes starting from Node.
collect_nodes(null, _, Acc) ->
    {lists:reverse(Acc), null};
collect_nodes(Node, 0, Acc) ->
    {lists:reverse(Acc), Node};
collect_nodes(Node, Count, Acc) when Count > 0 ->
    collect_nodes(Node#list_node.next, Count - 1, [Node | Acc]).

%% Build a linked list from Nodes (in order) whose last node points to Next.
build_chain_with_next(Nodes, Next) ->
    {Head, Tail} = lists:foldr(
        fun(NodeRec, {AccHead, AccTail}) ->
            NewNode = #list_node{val = NodeRec#list_node.val, next = AccHead},
            case AccTail of
                null -> {NewNode, NewNode};
                _    -> {NewNode, AccTail}
            end
        end,
        {Next, null},
        Nodes),
    {Head, Tail}.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_even_length_groups(head :: ListNode.t | nil) :: ListNode.t | nil
  def reverse_even_length_groups(nil), do: nil

  def reverse_even_length_groups(head) do
    vals = to_vals(head)
    processed = process(vals, 1, [])
    build_list(processed)
  end

  # Convert linked list to a list of values
  defp to_vals(head) do
    collect(head, []) |> Enum.reverse()
  end

  defp collect(nil, acc), do: acc

  defp collect(%ListNode{val: v, next: nxt}, acc) do
    collect(nxt, [v | acc])
  end

  # Process groups, reversing even-length ones
  defp process([], _group_len, acc_rev), do: Enum.reverse(acc_rev)

  defp process(vals, group_len, acc_rev) do
    {group, rest} = take_group(vals, group_len, [])
    new_group = if rem(length(group), 2) == 0, do: Enum.reverse(group), else: group

    new_acc =
      Enum.reduce(Enum.reverse(new_group), acc_rev, fn x, a -> [x | a] end)

    process(rest, group_len + 1, new_acc)
  end

  # Take up to k elements from the list
  defp take_group(list, 0, acc), do: {Enum.reverse(acc), list}
  defp take_group([], _k, acc), do: {Enum.reverse(acc), []}

  defp take_group([h | t], k, acc) when k > 0 do
    take_group(t, k - 1, [h | acc])
  end

  # Build linked list from a list of values
  defp build_list(vals) do
    Enum.reduce(Enum.reverse(vals), nil, fn v, acc ->
      %ListNode{val: v, next: acc}
    end)
  end
end
```
