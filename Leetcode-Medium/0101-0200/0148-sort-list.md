# 0148. Sort List

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
    // split the list starting at head into first n nodes and return the head of the rest
    ListNode* split(ListNode* head, int n) {
        while (n > 1 && head) {
            head = head->next;
            --n;
        }
        if (!head) return nullptr;
        ListNode* second = head->next;
        head->next = nullptr;
        return second;
    }

    // merge two sorted lists, return new head and set tail to the last node
    ListNode* merge(ListNode* l1, ListNode* l2, ListNode*& tail) {
        ListNode dummy(0);
        ListNode* cur = &dummy;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 ? l1 : l2;
        while (cur->next) cur = cur->next; // move to the end
        tail = cur;
        return dummy.next;
    }

    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;

        // compute length
        int n = 0;
        for (ListNode* p = head; p; p = p->next) ++n;

        ListNode dummy(0);
        dummy.next = head;
        for (int step = 1; step < n; step <<= 1) {
            ListNode* prev = &dummy;
            ListNode* cur = dummy.next;
            while (cur) {
                ListNode* left = cur;
                ListNode* right = split(left, step);
                cur = split(right, step);
                ListNode* mergedTail = nullptr;
                prev->next = merge(left, right, mergedTail);
                prev = mergedTail;
            }
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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        // compute length
        int n = 0;
        for (ListNode cur = head; cur != null; cur = cur.next) n++;
        ListNode dummy = new ListNode(0);
        for (int step = 1; step < n; step <<= 1) {
            ListNode tail = dummy;
            ListNode cur = head;
            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, step);
                cur = split(right, step);
                ListNode[] merged = merge(left, right);
                tail.next = merged[0];
                tail = merged[1];
            }
            head = dummy.next;
        }
        return head;
    }

    // Split the list after n nodes and return the start of the next part.
    private ListNode split(ListNode head, int n) {
        if (head == null) return null;
        for (int i = 1; i < n && head.next != null; i++) {
            head = head.next;
        }
        ListNode second = head.next;
        head.next = null;
        return second;
    }

    // Merge two sorted lists and return [mergedHead, mergedTail].
    private ListNode[] merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode p = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        p.next = (l1 != null) ? l1 : l2;
        while (p.next != null) {
            p = p.next;
        }
        return new ListNode[]{dummy.next, p};
    }
}
```

## Python

```python
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # compute length of list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        step = 1

        def split(start, size):
            if not start:
                return None
            cur = start
            for _ in range(1, size):
                if cur.next:
                    cur = cur.next
                else:
                    break
            nxt = cur.next
            cur.next = None
            return nxt

        def merge(l1, l2):
            dummy_merge = ListNode(0)
            tail = dummy_merge
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return dummy_merge.next, tail

        while step < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = split(left, step)
                curr = split(right, step)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            step <<= 1

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
    def sortList(self, head):
        if not head or not head.next:
            return head

        # get length of list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        def split(start, sz):
            """cut first sz nodes from start, return next sublist head"""
            if not start:
                return None
            cur = start
            for i in range(sz - 1):
                if cur.next:
                    cur = cur.next
                else:
                    break
            nxt = cur.next
            cur.next = None
            return nxt

        def merge(l1, l2):
            """merge two sorted lists, return (head, tail)"""
            dummy_merge = ListNode(0)
            p = dummy_merge
            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 if l1 else l2
            # advance to tail
            while p.next:
                p = p.next
            return dummy_merge.next, p

        while size < length:
            prev = dummy
            curr = dummy.next
            while curr:
                left = curr
                right = split(left, size)
                curr = split(right, size)
                merged_head, merged_tail = merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1

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

static struct ListNode* mergeLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode* p = &dummy;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            p->next = l1;
            l1 = l1->next;
        } else {
            p->next = l2;
            l2 = l2->next;
        }
        p = p->next;
    }
    p->next = (l1 ? l1 : l2);
    return dummy.next;
}

/* Cut the list after n nodes and return the head of the next part */
static struct ListNode* split(struct ListNode* head, int n) {
    while (--n && head) {
        head = head->next;
    }
    if (!head) return NULL;
    struct ListNode* second = head->next;
    head->next = NULL;
    return second;
}

struct ListNode* sortList(struct ListNode* head) {
    if (!head || !head->next) return head;

    /* compute length */
    int length = 0;
    for (struct ListNode* p = head; p; p = p->next) ++length;

    struct ListNode dummy;
    dummy.next = head;

    for (int step = 1; step < length; step <<= 1) {
        struct ListNode* cur = dummy.next;
        struct ListNode* tail = &dummy;

        while (cur) {
            struct ListNode* left = cur;
            struct ListNode* right = split(left, step);
            cur = split(right, step);   /* next start */

            tail->next = mergeLists(left, right);
            while (tail->next) tail = tail->next;
        }
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
public class Solution
{
    public ListNode SortList(ListNode head)
    {
        if (head == null || head.next == null) return head;

        // compute length
        int n = 0;
        var node = head;
        while (node != null)
        {
            n++;
            node = node.next;
        }

        var dummy = new ListNode(0, head);
        for (int step = 1; step < n; step <<= 1)
        {
            var prev = dummy;
            var curr = dummy.next;
            while (curr != null)
            {
                var left = curr;
                var right = Split(left, step);
                curr = Split(right, step);

                var mergedHead = Merge(left, right, out ListNode mergedTail);
                prev.next = mergedHead;
                prev = mergedTail;
            }
        }

        return dummy.next;
    }

    private ListNode Split(ListNode head, int size)
    {
        for (int i = 1; head != null && i < size; i++)
            head = head.next;

        if (head == null) return null;

        var second = head.next;
        head.next = null;
        return second;
    }

    private ListNode Merge(ListNode l1, ListNode l2, out ListNode tail)
    {
        var dummy = new ListNode(0);
        var p = dummy;
        while (l1 != null && l2 != null)
        {
            if (l1.val < l2.val)
            {
                p.next = l1;
                l1 = l1.next;
            }
            else
            {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }

        p.next = l1 ?? l2;

        while (p.next != null)
            p = p.next;

        tail = p;
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
var sortList = function(head) {
    if (!head || !head.next) return head;
    
    // compute length of list
    let len = 0;
    for (let node = head; node; node = node.next) len++;
    
    const dummy = new ListNode(0);
    dummy.next = head;
    
    for (let step = 1; step < len; step <<= 1) {
        let cur = dummy.next;
        let tail = dummy;
        while (cur) {
            const left = cur;
            const right = split(left, step);
            cur = split(right, step);
            const merged = merge(left, right);
            tail.next = merged[0];
            tail = merged[1];
        }
    }
    
    return dummy.next;
};

function split(head, size) {
    if (!head) return null;
    let cur = head;
    for (let i = 1; i < size && cur.next; i++) {
        cur = cur.next;
    }
    const next = cur.next;
    cur.next = null;
    return next;
}

function merge(l1, l2) {
    const dummy = new ListNode(0);
    let p = dummy;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            p.next = l1;
            l1 = l1.next;
        } else {
            p.next = l2;
            l2 = l2.next;
        }
        p = p.next;
    }
    p.next = l1 ? l1 : l2;
    while (p.next) p = p.next;
    return [dummy.next, p];
}
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

function sortList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;

    // Get length of list
    let length = 0;
    for (let node = head; node; node = node.next) length++;

    const dummy = new ListNode(0, head);

    // Split the list after 'size' nodes and return the next part's head
    const split = (start: ListNode | null, size: number): ListNode | null => {
        if (!start) return null;
        let cur: ListNode | null = start;
        for (let i = 1; i < size && cur.next; i++) {
            cur = cur.next;
        }
        const next = cur.next;
        cur.next = null;
        return next;
    };

    // Merge two sorted lists, attach after 'prev', and return the tail node
    const merge = (l1: ListNode | null, l2: ListNode | null, prev: ListNode): ListNode => {
        let cur = prev;
        while (l1 && l2) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next!;
        }
        cur.next = l1 ? l1 : l2;
        while (cur.next) cur = cur.next;
        return cur;
    };

    for (let step = 1; step < length; step <<= 1) {
        let prev = dummy;
        let curr = dummy.next;

        while (curr) {
            const left = curr;
            const right = split(left, step);
            curr = split(right, step);
            prev = merge(left, right, prev);
        }
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
     * @param ListNode|null $head
     * @return ListNode|null
     */
    function sortList($head) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        // split the list into two halves
        $mid = $this->getMid($head);
        $left = $this->sortList($head);
        $right = $this->sortList($mid);

        // merge sorted halves
        return $this->merge($left, $right);
    }

    /**
     * @param ListNode|null $head
     * @return ListNode|null  start of second half
     */
    private function getMid($head) {
        $slow = $head;
        $fast = $head;
        $prev = null;

        while ($fast !== null && $fast->next !== null) {
            $prev = $slow;
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        // cut the list
        if ($prev !== null) {
            $prev->next = null;
        }
        return $slow;
    }

    /**
     * @param ListNode|null $l1
     * @param ListNode|null $l2
     * @return ListNode|null
     */
    private function merge($l1, $l2) {
        $dummy = new ListNode(0);
        $tail = $dummy;

        while ($l1 !== null && $l2 !== null) {
            if ($l1->val <= $l2->val) {
                $tail->next = $l1;
                $l1 = $l1->next;
            } else {
                $tail->next = $l2;
                $l2 = $l2->next;
            }
            $tail = $tail->next;
        }

        if ($l1 !== null) {
            $tail->next = $l1;
        } elseif ($l2 !== null) {
            $tail->next = $l2;
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
    func sortList(_ head: ListNode?) -> ListNode? {
        guard head != nil else { return nil }
        
        // Compute length of list
        var length = 0
        var node = head
        while node != nil {
            length += 1
            node = node!.next
        }
        
        let dummyHead = ListNode(0)
        dummyHead.next = head
        
        var step = 1
        while step < length {
            var prev: ListNode? = dummyHead
            var curr = dummyHead.next
            
            while curr != nil {
                let left = curr
                let right = split(left, step)
                curr = split(right, step)   // start of next pair
                
                let merged = merge(left, right)
                prev?.next = merged.head
                prev = merged.tail
            }
            step <<= 1
        }
        
        return dummyHead.next
    }
    
    private func split(_ head: ListNode?, _ n: Int) -> ListNode? {
        var i = 1
        var node = head
        while i < n && node?.next != nil {
            node = node!.next
            i += 1
        }
        let next = node?.next
        node?.next = nil
        return next
    }
    
    private func merge(_ l1: ListNode?, _ l2: ListNode?) -> (head: ListNode?, tail: ListNode?) {
        var dummy = ListNode(0)
        var p: ListNode? = dummy
        var a = l1
        var b = l2
        
        while a != nil && b != nil {
            if a!.val < b!.val {
                p?.next = a
                a = a!.next
            } else {
                p?.next = b
                b = b!.next
            }
            p = p?.next
        }
        
        if a != nil { p?.next = a } else { p?.next = b }
        
        // Move to the tail of merged list
        while p?.next != nil {
            p = p?.next
        }
        return (dummy.next, p)
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
    fun sortList(head: ListNode?): ListNode? {
        if (head?.next == null) return head

        // Find middle using slow and fast pointers
        var prev: ListNode? = null
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            prev = slow
            slow = slow!!.next
            fast = fast.next?.next
        }
        // Split the list into two halves
        prev?.next = null

        val left = sortList(head)
        val right = sortList(slow)

        return merge(left, right)
    }

    private fun merge(l1: ListNode?, l2: ListNode?): ListNode? {
        val dummy = ListNode(0)
        var tail: ListNode = dummy
        var a = l1
        var b = l2

        while (a != null && b != null) {
            if (a.`val` <= b.`val`) {
                tail.next = a
                a = a.next
            } else {
                tail.next = b
                b = b.next
            }
            tail = tail.next!!
        }

        tail.next = a ?: b
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
  ListNode? sortList(ListNode? head) {
    if (head == null || head.next == null) return head;

    // Find the middle of the list
    ListNode? slow = head;
    ListNode? fast = head;
    ListNode? prev;
    while (fast != null && fast.next != null) {
      prev = slow;
      slow = slow!.next;
      fast = fast.next!.next;
    }

    // Split the list into two halves
    prev!.next = null;

    // Recursively sort each half
    ListNode? left = sortList(head);
    ListNode? right = sortList(slow);

    // Merge sorted halves
    return _merge(left, right);
  }

  ListNode? _merge(ListNode? l1, ListNode? l2) {
    ListNode dummy = ListNode(0);
    ListNode tail = dummy;

    while (l1 != null && l2 != null) {
      if (l1.val < l2.val) {
        tail.next = l1;
        l1 = l1.next;
      } else {
        tail.next = l2;
        l2 = l2.next;
      }
      tail = tail.next!;
    }

    tail.next = l1 ?? l2;
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
func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	// compute length
	n := 0
	for cur := head; cur != nil; cur = cur.Next {
		n++
	}
	dummy := &ListNode{Next: head}
	size := 1
	for size < n {
		prev, curr := dummy, dummy.Next
		for curr != nil {
			left := curr
			right := split(left, size)
			curr = split(right, size)
			mergedHead, mergedTail := merge(left, right)
			prev.Next = mergedHead
			prev = mergedTail
		}
		size <<= 1
	}
	return dummy.Next
}

// split the list after 'size' nodes and return the head of the second part.
func split(head *ListNode, size int) *ListNode {
	if head == nil {
		return nil
	}
	for i := 1; i < size && head.Next != nil; i++ {
		head = head.Next
	}
	second := head.Next
	head.Next = nil
	return second
}

// merge two sorted lists and return both the head and tail of the merged list.
func merge(l1, l2 *ListNode) (*ListNode, *ListNode) {
	dummy := &ListNode{}
	tail := dummy
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			tail.Next = l1
			l1 = l1.Next
		} else {
			tail.Next = l2
			l2 = l2.Next
		}
		tail = tail.Next
	}
	if l1 != nil {
		tail.Next = l1
	} else {
		tail.Next = l2
	}
	// advance to the end to get the tail
	for tail.Next != nil {
		tail = tail.Next
	}
	return dummy.Next, tail
}
```

## Ruby

```ruby
def sort_list(head)
  return head if !head || !head.next

  # Compute length of list
  len = 0
  node = head
  while node
    len += 1
    node = node.next
  end

  dummy = ListNode.new(0, head)

  split = lambda do |start, size|
    i = 1
    while start && i < size
      start = start.next
      i += 1
    end
    return nil unless start
    nxt = start.next
    start.next = nil
    nxt
  end

  merge = lambda do |l1, l2|
    dummy_merge = ListNode.new(0)
    tail = dummy_merge
    while l1 && l2
      if l1.val < l2.val
        tail.next = l1
        l1 = l1.next
      else
        tail.next = l2
        l2 = l2.next
      end
      tail = tail.next
    end
    tail.next = l1 ? l1 : l2
    while tail.next
      tail = tail.next
    end
    [dummy_merge.next, tail]
  end

  step = 1
  while step < len
    prev = dummy
    curr = dummy.next
    while curr
      left = curr
      right = split.call(left, step)
      next_start = split.call(right, step)

      merged_head, merged_tail = merge.call(left, right)
      prev.next = merged_head
      prev = merged_tail

      curr = next_start
    end
    step <<= 1
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
  def sortList(head: ListNode): ListNode = {
    if (head == null || head.next == null) return head

    // Find middle of the list
    var slow = head
    var fast = head
    var prev: ListNode = null
    while (fast != null && fast.next != null) {
      prev = slow
      slow = slow.next
      fast = fast.next.next
    }
    // Split the list into two halves
    if (prev != null) prev.next = null

    val left = sortList(head)
    val right = sortList(slow)

    merge(left, right)
  }

  private def merge(l1: ListNode, l2: ListNode): ListNode = {
    val dummy = new ListNode(0)
    var tail = dummy
    var a = l1
    var b = l2
    while (a != null && b != null) {
      if (a.x < b.x) {
        tail.next = a
        a = a.next
      } else {
        tail.next = b
        b = b.next
      }
      tail = tail.next
    }
    if (a != null) tail.next = a else tail.next = b
    dummy.next
  }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        Self::sort(head)
    }

    fn sort(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return head;
        }
        let (left, right) = Self::split(head);
        let left_sorted = Self::sort(left);
        let right_sorted = Self::sort(right);
        Self::merge(left_sorted, right_sorted)
    }

    fn split(mut head: Option<Box<ListNode>>) -> (Option<Box<ListNode>>, Option<Box<ListNode>>) {
        if head.is_none() || head.as_ref().unwrap().next.is_none() {
            return (head, None);
        }
        let mut slow = &mut head;
        let mut fast = &mut head;

        while fast.as_ref().unwrap().next.is_some()
            && fast
                .as_ref()
                .unwrap()
                .next
                .as_ref()
                .unwrap()
                .next
                .is_some()
        {
            fast = &mut fast.as_mut().unwrap().next.as_mut().unwrap().next;
            slow = &mut slow.as_mut().unwrap().next;
        }

        let mid = slow.as_mut().unwrap().next.take();
        (head, mid)
    }

    fn merge(mut l1: Option<Box<ListNode>>, mut l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: None });
        let mut tail = &mut dummy;
        while l1.is_some() && l2.is_some() {
            if l1.as_ref().unwrap().val < l2.as_ref().unwrap().val {
                let mut node = l1.unwrap();
                l1 = node.next.take();
                tail.next = Some(node);
            } else {
                let mut node = l2.unwrap();
                l2 = node.next.take();
                tail.next = Some(node);
            }
            tail = tail.next.as_mut().unwrap();
        }
        if l1.is_some() {
            tail.next = l1;
        } else if l2.is_some() {
            tail.next = l2;
        }
        dummy.next
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

;; helper: find middle node (end of first half)
(define (find-mid head)
  (let loop ((slow head) (fast (list-node-next head)))
    (if (or (not fast) (not (list-node-next fast)))
        slow
        (loop (list-node-next slow) (list-node-next (list-node-next fast))))))

;; helper: merge two sorted lists, return new head
(define (merge l1 l2)
  (let ((dummy (make-list-node 0))
        (tail #f))
    (set! tail dummy)
    (let loop ()
      (cond [(not l1) (set-list-node-next! tail l2)]
            [(not l2) (set-list-node-next! tail l1)]
            [else
             (if (<= (list-node-val l1) (list-node-val l2))
                 (begin
                   (set-list-node-next! tail l1)
                   (set! tail l1)
                   (set! l1 (list-node-next l1)))
                 (begin
                   (set-list-node-next! tail l2)
                   (set! tail l2)
                   (set! l2 (list-node-next l2))))
             (loop)]))
    (list-node-next dummy)))

;; main function
(define/contract (sort-list head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (or (not head) (not (list-node-next head)))
      head
      (let* ((mid (find-mid head))
             (right (list-node-next mid)))
        (set-list-node-next! mid #f)
        (merge (sort-list head) (sort-list right)))))
```

## Erlang

```erlang
-spec sort_list(Head :: #list_node{} | null) -> #list_node{} | null.
sort_list(Head) ->
    SortedVals = lists:sort(to_vals(Head)),
    from_vals(SortedVals).

to_vals(null) -> [];
to_vals(Node) when is_record(Node, list_node) ->
    [Node#list_node.val | to_vals(Node#list_node.next)].

from_vals([]) -> null;
from_vals([H|T]) ->
    #list_node{val = H, next = from_vals(T)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_list(head :: ListNode.t | nil) :: ListNode.t | nil
  def sort_list(head) do
    values = collect_vals(head, [])
    case Enum.sort(values) do
      [] -> nil
      sorted -> build(sorted)
    end
  end

  defp collect_vals(nil, acc), do: :lists.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp build(vals) do
    Enum.reduce(Enum.reverse(vals), nil, fn v, acc ->
      %ListNode{val: v, next: acc}
    end)
  end
end
```
