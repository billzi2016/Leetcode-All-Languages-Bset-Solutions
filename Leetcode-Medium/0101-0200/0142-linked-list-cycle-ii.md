# 0142. Linked List Cycle II

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return nullptr;
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                // cycle detected
                ListNode *ptr1 = head;
                ListNode *ptr2 = slow;
                while (ptr1 != ptr2) {
                    ptr1 = ptr1->next;
                    ptr2 = ptr2->next;
                }
                return ptr1;
            }
        }
        return nullptr; // no cycle
    }
};
```

## Java

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return null;
        ListNode slow = head, fast = head;
        boolean hasCycle = false;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        if (!hasCycle) return null;
        ListNode ptr1 = head, ptr2 = slow;
        while (ptr1 != ptr2) {
            ptr1 = ptr1.next;
            ptr2 = ptr2.next;
        }
        return ptr1;
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # Cycle detected, find entry point
                ptr1 = head
                ptr2 = slow
                while ptr1 is not ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1

        return None
```

## Python3

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                ptr1, ptr2 = head, slow
                while ptr1 is not ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1

        return None
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
struct ListNode *detectCycle(struct ListNode *head) {
    if (!head || !head->next) return NULL;

    struct ListNode *slow = head;
    struct ListNode *fast = head;

    // Find meeting point, if any
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            // Cycle detected; find entry point
            struct ListNode *ptr1 = head;
            struct ListNode *ptr2 = slow;
            while (ptr1 != ptr2) {
                ptr1 = ptr1->next;
                ptr2 = ptr2->next;
            }
            return ptr1;
        }
    }

    // No cycle
    return NULL;
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode DetectCycle(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode slow = head;
        ListNode fast = head;

        // Find meeting point, if any
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                // Cycle detected; find entry point
                ListNode ptr1 = head;
                ListNode ptr2 = slow;
                while (ptr1 != ptr2) {
                    ptr1 = ptr1.next;
                    ptr2 = ptr2.next;
                }
                return ptr1;
            }
        }

        // No cycle
        return null;
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    if (!head || !head.next) return null;

    let slow = head, fast = head;
    // Find meeting point
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) {
            // Cycle detected, find entry
            let ptr1 = head;
            let ptr2 = slow;
            while (ptr1 !== ptr2) {
                ptr1 = ptr1.next;
                ptr2 = ptr2.next;
            }
            return ptr1;
        }
    }
    // No cycle
    return null;
};
```

## Typescript

```typescript
function detectCycle(head: ListNode | null): ListNode | null {
    if (!head) return null;
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    // Find meeting point
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
        if (slow === fast) {
            // Cycle detected, find entry
            let ptr1: ListNode | null = head;
            let ptr2: ListNode | null = slow;
            while (ptr1 !== ptr2) {
                ptr1 = ptr1!.next;
                ptr2 = ptr2!.next;
            }
            return ptr1;
        }
    }

    // No cycle
    return null;
}
```

## Php

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {
    /**
     * @param ListNode $head
     * @return ListNode|null
     */
    function detectCycle($head) {
        if ($head === null || $head->next === null) {
            return null;
        }
        $slow = $head;
        $fast = $head;
        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
            if ($slow === $fast) { // cycle detected
                $ptr1 = $head;
                $ptr2 = $slow;
                while ($ptr1 !== $ptr2) {
                    $ptr1 = $ptr1->next;
                    $ptr2 = $ptr2->next;
                }
                return $ptr1;
            }
        }
        return null; // no cycle
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
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func detectCycle(_ head: ListNode?) -> ListNode? {
        var slow = head
        var fast = head
        
        while fast != nil && fast!.next != nil {
            slow = slow?.next
            fast = fast!.next!.next
            
            if slow === fast {
                var ptr1 = head
                var ptr2 = slow
                while ptr1 !== ptr2 {
                    ptr1 = ptr1?.next
                    ptr2 = ptr2?.next
                }
                return ptr1
            }
        }
        return nil
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
    fun detectCycle(head: ListNode?): ListNode? {
        if (head == null) return null

        var slow: ListNode? = head
        var fast: ListNode? = head

        // Find meeting point, if any
        while (fast?.next != null) {
            slow = slow?.next
            fast = fast.next?.next
            if (slow === fast) {
                // Cycle detected; find entry point
                var ptr1: ListNode? = head
                var ptr2: ListNode? = slow
                while (ptr1 !== ptr2) {
                    ptr1 = ptr1?.next
                    ptr2 = ptr2?.next
                }
                return ptr1
            }
        }

        // No cycle
        return null
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
func detectCycle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    // Phase 1: Determine whether a cycle exists
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast {
            // Cycle detected; now find the entry point
            ptr1 := head
            ptr2 := slow
            for ptr1 != ptr2 {
                ptr1 = ptr1.Next
                ptr2 = ptr2.Next
            }
            return ptr1
        }
    }

    // No cycle found
    return nil
}
```

## Ruby

```ruby
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

def detectCycle(head)
  slow = head
  fast = head

  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
    if slow == fast
      ptr = head
      while ptr != slow
        ptr = ptr.next
        slow = slow.next
      end
      return ptr
    end
  end

  nil
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */

object Solution {
    def detectCycle(head: ListNode): ListNode = {
        if (head == null) return null

        var slow: ListNode = head
        var fast: ListNode = head
        var hasCycle = false

        while (fast != null && fast.next != null) {
            slow = slow.next
            fast = fast.next.next
            if (slow eq fast) {
                hasCycle = true
                // break out of loop
                fast = null // use to exit loop condition
            }
        }

        if (!hasCycle) return null

        var ptr1: ListNode = head
        var ptr2: ListNode = slow
        while (ptr1 ne ptr2) {
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        }
        ptr1
    }
}
```
