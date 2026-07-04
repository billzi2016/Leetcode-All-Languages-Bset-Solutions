# 0203. Remove Linked List Elements

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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        while (prev->next) {
            if (prev->next->val == val) {
                ListNode* toDelete = prev->next;
                prev->next = toDelete->next;
                // optional delete to avoid memory leak in environments that track it
                // delete toDelete;
            } else {
                prev = prev->next;
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
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        while (prev.next != null) {
            if (prev.next.val == val) {
                prev.next = prev.next.next;
            } else {
                prev = prev.next;
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
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
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
    def removeElements(self, head: Optional['ListNode'], val: int) -> Optional['ListNode']:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
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
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;
    
    while (prev->next) {
        if (prev->next->val == val) {
            struct ListNode *tmp = prev->next;
            prev->next = tmp->next;
            free(tmp);
        } else {
            prev = prev->next;
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
    public ListNode RemoveElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0, head);
        ListNode cur = dummy;
        while (cur.next != null) {
            if (cur.next.val == val) {
                cur.next = cur.next.next;
            } else {
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
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    const dummy = new ListNode(0);
    dummy.next = head;
    let cur = dummy;
    while (cur.next !== null) {
        if (cur.next.val === val) {
            cur.next = cur.next.next;
        } else {
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

function removeElements(head: ListNode | null, val: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let prev: ListNode | null = dummy;
    while (prev && prev.next) {
        if (prev.next.val === val) {
            prev.next = prev.next.next;
        } else {
            prev = prev.next;
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
     * @param Integer $val
     * @return ListNode
     */
    function removeElements($head, $val) {
        $dummy = new ListNode(0);
        $dummy->next = $head;
        $prev = $dummy;
        while ($prev->next !== null) {
            if ($prev->next->val == $val) {
                $prev->next = $prev->next->next;
            } else {
                $prev = $prev->next;
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
    func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        
        while let curr = prev?.next {
            if curr.val == val {
                prev?.next = curr.next
            } else {
                prev = curr
            }
        }
        
        return dummy.next
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
    fun removeElements(head: ListNode?, `val`: Int): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var prev: ListNode? = dummy
        var curr = head
        while (curr != null) {
            if (curr.`val` == `val`) {
                prev?.next = curr.next
            } else {
                prev = curr
            }
            curr = curr.next
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
  ListNode? removeElements(ListNode? head, int val) {
    var dummy = ListNode(0, head);
    var prev = dummy;
    while (prev.next != null) {
      if (prev.next!.val == val) {
        prev.next = prev.next!.next;
      } else {
        prev = prev.next!;
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
func removeElements(head *ListNode, val int) *ListNode {
    dummy := &ListNode{Next: head}
    cur := dummy
    for cur.Next != nil {
        if cur.Next.Val == val {
            cur.Next = cur.Next.Next
        } else {
            cur = cur.Next
        }
    }
    return dummy.Next
}
```

## Ruby

```ruby
def remove_elements(head, val)
  dummy = ListNode.new(0)
  dummy.next = head
  current = dummy
  while current && current.next
    if current.next.val == val
      current.next = current.next.next
    else
      current = current.next
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
    def removeElements(head: ListNode, `val`: Int): ListNode = {
        val dummy = new ListNode(0)
        dummy.next = head
        var prev = dummy
        while (prev != null && prev.next != null) {
            if (prev.next.x == `val`) {
                prev.next = prev.next.next
            } else {
                prev = prev.next
            }
        }
        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut cur = &mut dummy;
        while let Some(ref mut nxt) = cur.next {
            if nxt.val == val {
                cur.next = nxt.next.take();
            } else {
                cur = cur.next.as_mut().unwrap();
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
(struct list-node
  (val next) #:mutable #:transparent)

(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (remove-elements head val)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (let ([dummy (make-list-node 0)])
    (set-list-node-next! dummy head)
    (let recur ([prev dummy] [curr head])
      (if (not curr)
          (list-node-next dummy)
          (if (= (list-node-val curr) val)
              (begin
                (set-list-node-next! prev (list-node-next curr))
                (recur prev (list-node-next curr)))
              (recur curr (list-node-next curr)))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec remove_elements(Head :: #list_node{} | null, Val :: integer()) -> #list_node{} | null.
remove_elements(null, _Val) ->
    null;
remove_elements(#list_node{val=Val, next=Next}, Val) ->
    remove_elements(Next, Val);
remove_elements(Node=#list_node{next=Next}, Val) ->
    Node#list_node{next = remove_elements(Next, Val)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_elements(head :: ListNode.t | nil, val :: integer) :: ListNode.t | nil
  def remove_elements(nil, _val), do: nil

  def remove_elements(%ListNode{val: v, next: nxt} = node, val) do
    filtered_next = remove_elements(nxt, val)

    if v == val do
      filtered_next
    else
      %ListNode{node | next: filtered_next}
    end
  end
end
```
