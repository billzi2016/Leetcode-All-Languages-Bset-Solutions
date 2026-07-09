# 0082. Remove Duplicates from Sorted List II

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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        
        while (head) {
            if (head->next && head->val == head->next->val) {
                int dupVal = head->val;
                while (head && head->val == dupVal) {
                    ListNode* tmp = head;
                    head = head->next;
                    // optional: delete tmp;
                }
                prev->next = head;
            } else {
                prev = head;
                head = head->next;
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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        ListNode cur = head;
        while (cur != null) {
            if (cur.next != null && cur.val == cur.next.val) {
                int dupVal = cur.val;
                while (cur != null && cur.val == dupVal) {
                    cur = cur.next;
                }
                prev.next = cur;
            } else {
                prev = cur;
                cur = cur.next;
            }
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
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                while cur and cur.val == dup_val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next

        return dummy.next
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
    def deleteDuplicates(self, head: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                while cur and cur.val == dup_val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

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
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;
    struct ListNode *cur = head;
    
    while (cur) {
        if (cur->next && cur->val == cur->next->val) {
            int dupVal = cur->val;
            while (cur && cur->val == dupVal) {
                struct ListNode* tmp = cur;
                cur = cur->next;
                // optional: free(tmp);
            }
            prev->next = cur;
        } else {
            prev = cur;
            cur = cur->next;
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
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        var dummy = new ListNode(0, head);
        var prev = dummy;
        var cur = head;

        while (cur != null) {
            if (cur.next != null && cur.val == cur.next.val) {
                int dupVal = cur.val;
                while (cur != null && cur.val == dupVal) {
                    cur = cur.next;
                }
                prev.next = cur;
            } else {
                prev = cur;
                cur = cur.next;
            }
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
var deleteDuplicates = function(head) {
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let cur = head;
    
    while (cur !== null) {
        if (cur.next !== null && cur.val === cur.next.val) {
            // Skip all nodes with this value
            const dupVal = cur.val;
            while (cur !== null && cur.val === dupVal) {
                cur = cur.next;
            }
            prev.next = cur; // link past duplicates
        } else {
            // No duplicate for current node
            prev = cur;
            cur = cur.next;
        }
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

function deleteDuplicates(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let prev: ListNode = dummy;
    let cur = head;

    while (cur) {
        if (cur.next && cur.val === cur.next.val) {
            const dupVal = cur.val;
            while (cur && cur.val === dupVal) {
                cur = cur.next;
            }
            prev.next = cur;
        } else {
            prev = cur;
            cur = cur.next;
        }
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
    function deleteDuplicates($head) {
        $dummy = new ListNode(0, $head);
        $prev = $dummy;
        $curr = $head;

        while ($curr !== null) {
            if ($curr->next !== null && $curr->val === $curr->next->val) {
                // Skip all nodes with this duplicate value
                $dupVal = $curr->val;
                while ($curr !== null && $curr->val === $dupVal) {
                    $curr = $curr->next;
                }
                $prev->next = $curr; // link past the duplicates
            } else {
                // Current node is distinct, move prev forward
                $prev = $curr;
                $curr = $curr->next;
            }
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
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        var cur = head
        
        while cur != nil {
            if let nxt = cur!.next, cur!.val == nxt.val {
                let dupVal = cur!.val
                while cur != nil && cur!.val == dupVal {
                    cur = cur!.next
                }
                prev?.next = cur
            } else {
                prev = cur
                cur = cur!.next
            }
        }
        
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
    fun deleteDuplicates(head: ListNode?): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        var cur = head

        while (cur != null) {
            if (cur.next != null && cur.`val` == cur.next!!.`val`) {
                // Skip all nodes with this value
                val dupVal = cur.`val`
                while (cur != null && cur.`val` == dupVal) {
                    cur = cur.next
                }
                prev?.next = cur
            } else {
                // No duplicate, move prev forward
                prev = cur
                cur = cur.next
            }
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
  ListNode? deleteDuplicates(ListNode? head) {
    // Dummy node to handle edge cases easily
    final dummy = ListNode(0);
    dummy.next = head;

    ListNode? prev = dummy; // The last node known to be distinct
    ListNode? cur = head;   // Iterator

    while (cur != null) {
      if (cur.next != null && cur.val == cur.next!.val) {
        // Found a duplicate sequence, skip all nodes with this value
        final dupVal = cur.val;
        while (cur != null && cur.val == dupVal) {
          cur = cur.next;
        }
        // Link previous distinct node to the next new value
        prev!.next = cur;
      } else {
        // Current node is distinct, move prev forward
        prev = cur;
        cur = cur.next;
      }
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
func deleteDuplicates(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy
    cur := head

    for cur != nil {
        if cur.Next != nil && cur.Val == cur.Next.Val {
            dupVal := cur.Val
            for cur != nil && cur.Val == dupVal {
                cur = cur.Next
            }
            prev.Next = cur
        } else {
            prev = cur
            cur = cur.Next
        }
    }

    return dummy.Next
}
```

## Ruby

```ruby
def delete_duplicates(head)
  dummy = ListNode.new(0, head)
  prev = dummy
  cur = head
  while cur
    if cur.next && cur.val == cur.next.val
      dup_val = cur.val
      while cur && cur.val == dup_val
        cur = cur.next
      end
      prev.next = cur
    else
      prev = cur
      cur = cur.next
    end
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
    def deleteDuplicates(head: ListNode): ListNode = {
        val dummy = new ListNode(0)
        dummy.next = head
        var prev = dummy
        var cur = head

        while (cur != null) {
            if (cur.next != null && cur.x == cur.next.x) {
                val dupVal = cur.x
                while (cur != null && cur.x == dupVal) {
                    cur = cur.next
                }
                prev.next = cur
            } else {
                prev = cur
                cur = cur.next
            }
        }

        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: None });
        let mut tail = &mut dummy;
        let mut cur = head;

        while let Some(mut node) = cur {
            if let Some(ref next_node) = node.next {
                if node.val == next_node.val {
                    // duplicate value found; skip all nodes with this value
                    let dup_val = node.val;
                    cur = node.next.take(); // move past the first duplicate
                    while let Some(mut nxt) = cur {
                        if nxt.val == dup_val {
                            cur = nxt.next.take();
                        } else {
                            break;
                        }
                    }
                } else {
                    // unique node, attach to result list
                    tail.next = Some(Box::new(ListNode { val: node.val, next: None }));
                    tail = tail.next.as_mut().unwrap();
                    cur = node.next.take();
                }
            } else {
                // last node and it's unique
                tail.next = Some(Box::new(ListNode { val: node.val, next: None }));
                tail = tail.next.as_mut().unwrap();
                break;
            }
        }

        dummy.next
    }
}
```

## Racket

```racket
; Definition for singly-linked list:
#|
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (delete-duplicates head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (let ((dummy (make-list-node 0)))
    (set-list-node-next! dummy head)
    (let loop ((prev dummy) (cur head))
      (cond
        [(not cur) (list-node-next dummy)]
        [(and (list-node-next cur)
              (= (list-node-val cur) (list-node-val (list-node-next cur))))
         ;; Skip all nodes with this duplicate value
         (let skip ((node cur))
           (let ((next (list-node-next node)))
             (if (and next (= (list-node-val node) (list-node-val next)))
                 (skip next)
                 (begin
                   (set-list-node-next! prev (list-node-next node))
                   (loop prev (list-node-next node))))))]
        [else
         (loop cur (list-node-next cur))]))))
```

## Erlang

```erlang
-spec delete_duplicates(Head :: #list_node{} | null) -> #list_node{} | null.
delete_duplicates(Head) ->
    process(Head).

process(null) ->
    null;
process(#list_node{val = V, next = Next}) ->
    case Next of
        #list_node{val = V2} when V2 =:= V ->
            Rest = skip_same(Next, V),
            process(Rest);
        _ ->
            NewNext = process(Next),
            #list_node{val = V, next = NewNext}
    end.

skip_same(null, _) ->
    null;
skip_same(#list_node{val = V, next = N}, Val) when V =:= Val ->
    skip_same(N, Val);
skip_same(Node, _) ->
    Node.
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_duplicates(head :: ListNode.t | nil) :: ListNode.t | nil
  def delete_duplicates(head) do
    vals = collect_distinct_vals(head, [])
    build_list(vals)
  end

  defp collect_distinct_vals(nil, acc), do: Enum.reverse(acc)

  defp collect_distinct_vals(%ListNode{val: v, next: nxt}, acc) do
    if nxt != nil && v == nxt.val do
      # skip all nodes with this duplicate value
      next_node = skip_duplicates(nxt, v)
      collect_distinct_vals(next_node, acc)
    else
      collect_distinct_vals(nxt, [v | acc])
    end
  end

  defp skip_duplicates(nil, _val), do: nil

  defp skip_duplicates(%ListNode{val: v, next: nxt} = node, val) do
    if v == val do
      skip_duplicates(nxt, val)
    else
      node
    end
  end

  defp build_list([]), do: nil
  defp build_list([h | t]), do: %ListNode{val: h, next: build_list(t)}
end
```
