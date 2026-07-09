# 0086. Partition List

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
    ListNode* partition(ListNode* head, int x) {
        ListNode lessDummy(0), greaterDummy(0);
        ListNode *less = &lessDummy, *greater = &greaterDummy;
        
        while (head) {
            if (head->val < x) {
                less->next = head;
                less = less->next;
            } else {
                greater->next = head;
                greater = greater->next;
            }
            head = head->next;
        }
        // Terminate the greater list
        greater->next = nullptr;
        // Connect less list with greater list
        less->next = greaterDummy.next;
        
        return lessDummy.next;
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
    public ListNode partition(ListNode head, int x) {
        ListNode lessDummy = new ListNode(0);
        ListNode greaterDummy = new ListNode(0);
        ListNode less = lessDummy;
        ListNode greater = greaterDummy;
        
        while (head != null) {
            if (head.val < x) {
                less.next = head;
                less = less.next;
            } else {
                greater.next = head;
                greater = greater.next;
            }
            head = head.next;
        }
        
        // Terminate the greater list to avoid cycles.
        greater.next = null;
        // Connect less list with greater list.
        less.next = greaterDummy.next;
        
        return lessDummy.next;
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
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_ptr, greater_ptr = less_dummy, greater_dummy

        cur = head
        while cur:
            nxt = cur.next  # preserve next node
            if cur.val < x:
                less_ptr.next = cur
                less_ptr = less_ptr.next
                less_ptr.next = None
            else:
                greater_ptr.next = cur
                greater_ptr = greater_ptr.next
                greater_ptr.next = None
            cur = nxt

        # connect partitions
        less_ptr.next = greater_dummy.next
        return less_dummy.next
```

## Python3

```python
from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less = less_dummy
        greater = greater_dummy
        cur = head
        while cur:
            nxt = cur.next
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur.next = None
            cur = nxt
        less.next = greater_dummy.next
        return less_dummy.next
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
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode less_dummy = {0, NULL};
    struct ListNode greater_dummy = {0, NULL};
    struct ListNode *less_tail = &less_dummy;
    struct ListNode *greater_tail = &greater_dummy;

    while (head) {
        struct ListNode* next = head->next;
        head->next = NULL;  // detach current node
        if (head->val < x) {
            less_tail->next = head;
            less_tail = less_tail->next;
        } else {
            greater_tail->next = head;
            greater_tail = greater_tail->next;
        }
        head = next;
    }

    less_tail->next = greater_dummy.next;
    return less_dummy.next;
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
    public ListNode Partition(ListNode head, int x) {
        ListNode lessDummy = new ListNode(0);
        ListNode greaterDummy = new ListNode(0);
        ListNode less = lessDummy;
        ListNode greater = greaterDummy;

        while (head != null) {
            if (head.val < x) {
                less.next = head;
                less = less.next;
            } else {
                greater.next = head;
                greater = greater.next;
            }
            head = head.next;
        }

        // Terminate the greater list.
        greater.next = null;
        // Connect less list with greater list.
        less.next = greaterDummy.next;

        return lessDummy.next;
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    const beforeHead = new ListNode(0);
    const afterHead = new ListNode(0);
    let before = beforeHead;
    let after = afterHead;
    
    while (head !== null) {
        if (head.val < x) {
            before.next = head;
            before = before.next;
        } else {
            after.next = head;
            after = after.next;
        }
        head = head.next;
    }
    
    after.next = null; // terminate the list
    before.next = afterHead.next;
    return beforeHead.next;
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

function partition(head: ListNode | null, x: number): ListNode | null {
    const lessDummy = new ListNode(0);
    const greaterDummy = new ListNode(0);
    let lessTail = lessDummy;
    let greaterTail = greaterDummy;
    let cur = head;

    while (cur) {
        if (cur.val < x) {
            lessTail.next = cur;
            lessTail = lessTail.next;
        } else {
            greaterTail.next = cur;
            greaterTail = greaterTail.next;
        }
        cur = cur.next;
    }

    // Terminate the greater list to avoid potential cycles
    greaterTail.next = null;
    // Connect less list with greater list
    lessTail.next = greaterDummy.next;

    return lessDummy.next;
}
```

## Php

```php
<?php
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
     * @param integer $x
     * @return ListNode
     */
    function partition($head, $x) {
        $lessDummy   = new ListNode(0);
        $greaterDummy = new ListNode(0);
        $lessTail    = $lessDummy;
        $greaterTail = $greaterDummy;

        $curr = $head;
        while ($curr !== null) {
            $next = $curr->next;
            $curr->next = null; // detach node
            if ($curr->val < $x) {
                $lessTail->next = $curr;
                $lessTail = $curr;
            } else {
                $greaterTail->next = $curr;
                $greaterTail = $curr;
            }
            $curr = $next;
        }

        // concatenate the two partitions
        $lessTail->next = $greaterDummy->next;

        return $lessDummy->next;
    }
}
?>
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
    func partition(_ head: ListNode?, _ x: Int) -> ListNode? {
        let lessDummy = ListNode(0)
        var lessTail: ListNode? = lessDummy
        let greaterDummy = ListNode(0)
        var greaterTail: ListNode? = greaterDummy
        
        var current = head
        while let node = current {
            if node.val < x {
                lessTail?.next = node
                lessTail = lessTail?.next
            } else {
                greaterTail?.next = node
                greaterTail = greaterTail?.next
            }
            current = node.next
        }
        
        // Terminate the greater list to avoid cycles.
        greaterTail?.next = nil
        // Connect less list with greater/equal list.
        lessTail?.next = greaterDummy.next
        
        return lessDummy.next
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
    fun partition(head: ListNode?, x: Int): ListNode? {
        val lessDummy = ListNode(0)
        var lessTail: ListNode = lessDummy
        val greaterDummy = ListNode(0)
        var greaterTail: ListNode = greaterDummy

        var cur = head
        while (cur != null) {
            val nextNode = cur.next
            cur.next = null
            if (cur.`val` < x) {
                lessTail.next = cur
                lessTail = cur
            } else {
                greaterTail.next = cur
                greaterTail = cur
            }
            cur = nextNode
        }

        // Connect the two partitions
        lessTail.next = greaterDummy.next

        return lessDummy.next
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
  ListNode? partition(ListNode? head, int x) {
    var lessDummy = ListNode(0);
    var greaterDummy = ListNode(0);
    var less = lessDummy;
    var greater = greaterDummy;
    var curr = head;

    while (curr != null) {
      if (curr.val < x) {
        less.next = curr;
        less = less.next!;
      } else {
        greater.next = curr;
        greater = greater.next!;
      }
      curr = curr.next;
    }

    // Terminate the greater list to avoid cycles.
    greater.next = null;
    // Connect less list with greater/equal list.
    less.next = greaterDummy.next;

    return lessDummy.next;
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
func partition(head *ListNode, x int) *ListNode {
	lessDummy := &ListNode{}
	greaterDummy := &ListNode{}
	lessPtr, greaterPtr := lessDummy, greaterDummy

	for cur := head; cur != nil; cur = cur.Next {
		if cur.Val < x {
			lessPtr.Next = cur
			lessPtr = lessPtr.Next
		} else {
			greaterPtr.Next = cur
			greaterPtr = greaterPtr.Next
		}
	}

	greaterPtr.Next = nil
	lessPtr.Next = greaterDummy.Next

	return lessDummy.Next
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

def partition(head, x)
  less_dummy = ListNode.new(0)
  greater_dummy = ListNode.new(0)

  less = less_dummy
  greater = greater_dummy

  cur = head
  while cur
    if cur.val < x
      less.next = cur
      less = less.next
    else
      greater.next = cur
      greater = greater.next
    end
    cur = cur.next
  end

  # Terminate the greater list to avoid cycles.
  greater.next = nil
  # Connect the two partitions.
  less.next = greater_dummy.next

  less_dummy.next
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
    def partition(head: ListNode, x: Int): ListNode = {
        val lessDummy = new ListNode(0)
        val greaterDummy = new ListNode(0)
        var lessTail = lessDummy
        var greaterTail = greaterDummy

        var cur = head
        while (cur != null) {
            val nextNode = cur.next
            cur.next = null
            if (cur.x < x) {
                lessTail.next = cur
                lessTail = cur
            } else {
                greaterTail.next = cur
                greaterTail = cur
            }
            cur = nextNode
        }

        lessTail.next = greaterDummy.next
        lessDummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut less_dummy = Box::new(ListNode { val: 0, next: None });
        let mut greater_dummy = Box::new(ListNode { val: 0, next: None });

        // tails for the two partitions
        let mut less_tail: &mut Box<ListNode> = &mut less_dummy;
        let mut greater_tail: &mut Box<ListNode> = &mut greater_dummy;

        let mut current = head;
        while let Some(mut node) = current {
            current = node.next.take(); // detach the rest of the list
            if node.val < x {
                less_tail.next = Some(node);
                less_tail = less_tail.next.as_mut().unwrap();
            } else {
                greater_tail.next = Some(node);
                greater_tail = greater_tail.next.as_mut().unwrap();
            }
        }

        // concatenate the two partitions
        less_tail.next = greater_dummy.next;
        less_dummy.next
    }
}
```

## Racket

```racket
(define/contract (partition head x)
  (-> (or/c list-node? #f) exact-integer? (or/c list-node? #f))
  (if (not head)
      #f
      (let ([less-dummy   (make-list-node 0)]
            [greater-dummy (make-list-node 0)])
        (let loop ((curr head)
                   (less-tail less-dummy)
                   (greater-tail greater-dummy))
          (if (not curr)
              (begin
                (set-list-node-next! less-tail (list-node-next greater-dummy))
                (list-node-next less-dummy))
              (let ([next (list-node-next curr)])
                (set-list-node-next! curr #f)
                (if (< (list-node-val curr) x)
                    (begin
                      (set-list-node-next! less-tail curr)
                      (loop next (list-node-next less-tail) greater-tail))
                    (begin
                      (set-list-node-next! greater-tail curr)
                      (loop next less-tail (list-node-next greater-tail))))))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec partition(Head :: #list_node{} | null, X :: integer()) -> #list_node{} | null.
partition(Head, X) ->
    {LessRev, GreaterRev} = split(Head, X, [], []),
    Less = lists:reverse(LessRev),
    Greater = lists:reverse(GreaterRev),
    build_list(Less ++ Greater).

-spec split(#list_node{} | null, integer(), [integer()], [integer()]) -> {[integer()], [integer()]}.
split(null, _X, LessAcc, GreaterAcc) ->
    {LessAcc, GreaterAcc};
split(#list_node{val = Val, next = Next}, X, LessAcc, GreaterAcc) ->
    if
        Val < X ->
            split(Next, X, [Val | LessAcc], GreaterAcc);
        true ->
            split(Next, X, LessAcc, [Val | GreaterAcc])
    end.

-spec build_list([integer()]) -> #list_node{} | null.
build_list([]) -> null;
build_list([H | T]) -> #list_node{val = H, next = build_list(T)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec partition(head :: ListNode.t | nil, x :: integer) :: ListNode.t | nil
  def partition(head, x) do
    {less_vals, greater_vals} = collect_vals(head, [], [], x)
    vals = Enum.reverse(less_vals) ++ Enum.reverse(greater_vals)
    build_list(vals)
  end

  defp collect_vals(nil, less_acc, greater_acc, _x), do: {less_acc, greater_acc}
  defp collect_vals(%ListNode{val: v, next: nxt}, less_acc, greater_acc, x) do
    if v < x do
      collect_vals(nxt, [v | less_acc], greater_acc, x)
    else
      collect_vals(nxt, less_acc, [v | greater_acc], x)
    end
  end

  defp build_list([]), do: nil
  defp build_list([h | t]) do
    %ListNode{val: h, next: build_list(t)}
  end
end
```
