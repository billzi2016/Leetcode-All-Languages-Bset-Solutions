# 1669. Merge In Between Linked Lists

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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        // Find node just before position a
        ListNode* prevA = list1;
        for (int i = 0; i < a - 1; ++i) {
            prevA = prevA->next;
        }
        
        // Find node at position b
        ListNode* nodeB = list1;
        for (int i = 0; i < b; ++i) {
            nodeB = nodeB->next;
        }
        ListNode* afterB = nodeB->next;
        
        // Connect prevA to head of list2
        prevA->next = list2;
        
        // Find tail of list2
        ListNode* tail2 = list2;
        while (tail2->next) {
            tail2 = tail2->next;
        }
        // Connect tail of list2 to afterB
        tail2->next = afterB;
        
        return list1;
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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        // Find node just before position a
        ListNode prevA = list1;
        for (int i = 0; i < a - 1; i++) {
            prevA = prevA.next;
        }
        
        // Find node at position b and the node after it
        ListNode curB = list1;
        for (int i = 0; i < b; i++) {
            curB = curB.next;
        }
        ListNode afterB = curB.next;
        
        // Connect prevA to head of list2
        prevA.next = list2;
        
        // Find tail of list2
        ListNode tail2 = list2;
        while (tail2.next != null) {
            tail2 = tail2.next;
        }
        
        // Connect tail of list2 to afterB
        tail2.next = afterB;
        
        return list1;
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
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # Find node just before position a
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        # Find node just after position b
        cur = list1
        for _ in range(b):
            cur = cur.next
        post = cur.next

        # Connect prev to head of list2
        prev.next = list2

        # Find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Connect tail to the remainder of list1
        tail.next = post

        return list1
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        # Find node just before position a
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        # Find node at position b
        cur = list1
        for _ in range(b):
            cur = cur.next

        # Connect the part before a to list2
        prev.next = list2

        # Find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # Connect tail of list2 to the part after b
        tail.next = cur.next

        return list1
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

struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){
    struct ListNode *prevA = NULL;   // node at index a-1
    struct ListNode *endB = NULL;    // node at index b
    struct ListNode *cur = list1;
    
    for (int i = 0; i < b; ++i) {
        if (i == a - 1)
            prevA = cur;
        cur = cur->next;
    }
    endB = cur; // cur is now at index b
    
    // Connect node before a to head of list2
    prevA->next = list2;
    
    // Find tail of list2
    struct ListNode *tail = list2;
    while (tail->next != NULL) {
        tail = tail->next;
    }
    
    // Connect tail of list2 to node after b
    tail->next = endB->next;
    
    return list1;
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
    public ListNode MergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        // Find the node just before index a (prevA) and the node at index b (nodeB)
        ListNode prevA = null;
        ListNode nodeB = null;
        ListNode cur = list1;
        int idx = 0;
        while (cur != null && idx <= b) {
            if (idx == a - 1) {
                prevA = cur;
            }
            if (idx == b) {
                nodeB = cur;
                break;
            }
            cur = cur.next;
            idx++;
        }

        // Connect prevA to the head of list2
        prevA.next = list2;

        // Find tail of list2
        ListNode tail = list2;
        while (tail.next != null) {
            tail = tail.next;
        }

        // Connect tail of list2 to the node after b
        tail.next = nodeB.next;

        return list1;
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
 * @param {ListNode} list1
 * @param {number} a
 * @param {number} b
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeInBetween = function(list1, a, b, list2) {
    // Find node before position a and node at position b
    let prevA = null;
    let nodeB = null;
    let cur = list1;
    for (let i = 0; i <= b; ++i) {
        if (i === a - 1) prevA = cur;
        if (i === b) nodeB = cur;
        cur = cur.next;
    }
    
    // Connect prevA to head of list2
    prevA.next = list2;
    
    // Find tail of list2
    let tail = list2;
    while (tail.next !== null) {
        tail = tail.next;
    }
    
    // Connect tail to the node after b
    tail.next = nodeB.next;
    
    return list1;
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

function mergeInBetween(list1: ListNode | null, a: number, b: number, list2: ListNode | null): ListNode | null {
    if (!list1) return list2;

    // Dummy node simplifies edge cases where a == 0
    const dummy = new ListNode(0, list1);
    let prevA: ListNode | null = dummy;

    // Move to the (a-1)-th node (prevA)
    for (let i = 0; i < a; i++) {
        if (prevA) prevA = prevA.next!;
    }

    // Find the b-th node
    let cur: ListNode | null = prevA;
    for (let i = a; i <= b; i++) {
        if (cur) cur = cur.next!;
    }

    const postB: ListNode | null = cur ? cur.next : null;

    // Connect (a-1)-th node to list2
    if (prevA) prevA.next = list2;

    // Find tail of list2 and connect it to postB
    let tail = list2;
    if (tail) {
        while (tail.next) {
            tail = tail.next;
        }
        tail.next = postB;
    } else {
        // If list2 is empty, just link prevA directly to postB
        if (prevA) prevA.next = postB;
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
     * @param ListNode $list1
     * @param Integer $a
     * @param Integer $b
     * @param ListNode $list2
     * @return ListNode
     */
    function mergeInBetween($list1, $a, $b, $list2) {
        // Find node just before position a (index a-1)
        $prev = $list1;
        for ($i = 0; $i < $a - 1; $i++) {
            $prev = $prev->next;
        }

        // Find node at position b
        $curr = $prev;
        for ($i = $a - 1; $i <= $b; $i++) {
            $curr = $curr->next;
        }
        // $curr is now the node after index b (i.e., b+1)
        $afterB = $curr;

        // Connect prev to list2
        $prev->next = $list2;

        // Find tail of list2
        $tail = $list2;
        while ($tail->next !== null) {
            $tail = $tail->next;
        }

        // Connect tail of list2 to the remainder of list1
        $tail->next = $afterB;

        return $list1;
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
    func mergeInBetween(_ list1: ListNode?, _ a: Int, _ b: Int, _ list2: ListNode?) -> ListNode? {
        guard let head = list1 else { return list2 }
        
        var prevA: ListNode? = nil
        var cur: ListNode? = head
        var idx = 0
        
        // Move to node at index a, keeping track of node before it (prevA)
        while idx < a {
            prevA = cur
            cur = cur!.next
            idx += 1
        }
        
        // Continue moving until we reach the node after index b
        while idx <= b {
            cur = cur!.next
            idx += 1
        }
        let postB = cur   // node at position b+1
        
        // Connect prevA to list2
        prevA?.next = list2
        
        // Find tail of list2 and connect it to postB
        var tail = list2
        if tail != nil {
            while tail!.next != nil {
                tail = tail!.next
            }
            tail!.next = postB
        }
        
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
    fun mergeInBetween(list1: ListNode?, a: Int, b: Int, list2: ListNode?): ListNode? {
        if (list1 == null) return list2

        // Find node just before position a (index a-1)
        var prevA = list1
        for (i in 0 until a - 1) {
            prevA = prevA!!.next!!
        }

        // Find the node after position b
        var postB = prevA.next
        for (i in a..b) {
            postB = postB?.next
        }

        // Connect prevA to list2
        prevA.next = list2

        // Attach the tail of list2 to postB
        var tail = list2
        if (tail != null) {
            while (tail!!.next != null) {
                tail = tail.next
            }
            tail!!.next = postB
        } else {
            // If list2 is empty, just link prevA directly to postB
            prevA.next = postB
        }

        return list1
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
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	// Find node just before position a
	prev := list1
	for i := 0; i < a-1; i++ {
		prev = prev.Next
	}
	// Find node at position b and the node after it
	cur := list1
	for i := 0; i < b; i++ {
		cur = cur.Next
	}
	afterB := cur.Next

	// Connect prev to head of list2
	prev.Next = list2

	// Find tail of list2
	tail := list2
	for tail.Next != nil {
		tail = tail.Next
	}

	// Connect tail of list2 to the remainder of list1
	tail.Next = afterB

	return list1
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

def merge_in_between(list1, a, b, list2)
  # Find node just before position a (prev) and node at position a (curr)
  prev = nil
  curr = list1
  i = 0
  while i < a
    prev = curr
    curr = curr.next
    i += 1
  end

  # Find node at position b
  node_b = curr
  j = a
  while j < b
    node_b = node_b.next
    j += 1
  end
  after = node_b.next

  # Connect prev to list2
  prev.next = list2

  # Find tail of list2
  tail = list2
  while tail.next
    tail = tail.next
  end

  # Connect tail to the remainder of list1
  tail.next = after

  list1
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
    def mergeInBetween(list1: ListNode, a: Int, b: Int, list2: ListNode): ListNode = {
        var idx = 0
        var cur: ListNode = list1
        var prevA: ListNode = null
        var nodeB: ListNode = null

        while (idx <= b) {
            if (idx == a - 1) prevA = cur
            if (idx == b) nodeB = cur
            cur = cur.next
            idx += 1
        }

        // Connect the part before 'a' to list2
        prevA.next = list2

        // Find tail of list2
        var tail: ListNode = list2
        while (tail.next != null) {
            tail = tail.next
        }

        // Connect tail of list2 to the part after 'b'
        tail.next = nodeB.next

        list1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_in_between(
        list1: Option<Box<ListNode>>,
        a: i32,
        b: i32,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut head = list1;
        let mut list2_opt = list2;

        // Find the node before position a and the node at position b
        {
            // prev will point to the (a-1)th node
            let mut prev = &mut head;
            for _ in 0..(a as usize - 1) {
                prev = &mut prev.as_mut().unwrap().next;
            }

            // end will point to the b-th node
            let mut end = &mut head;
            for _ in 0..b as usize {
                end = &mut end.as_mut().unwrap().next;
            }

            // The part after b
            let after = end.as_mut().unwrap().next.take();

            // Splice list2 into list1
            let start_node = prev.as_mut().unwrap();
            start_node.next = list2_opt;

            // Connect the tail of list2 to the 'after' segment
            let mut tail = &mut start_node.next;
            while let Some(ref mut node) = tail {
                if node.next.is_none() {
                    node.next = after;
                    break;
                }
                tail = &mut node.next;
            }
        }

        head
    }
}
```
