# 0147. Insertion Sort List

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
    ListNode* insertionSortList(ListNode* head) {
        if (!head) return nullptr;
        ListNode dummy(0);
        ListNode* cur = head;
        while (cur) {
            ListNode* nxt = cur->next;  // store next node
            ListNode* prev = &dummy;
            while (prev->next && prev->next->val < cur->val) {
                prev = prev->next;
            }
            cur->next = prev->next;
            prev->next = cur;
            cur = nxt;
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
    public ListNode insertionSortList(ListNode head) {
        if (head == null) return null;
        ListNode dummy = new ListNode(0);
        ListNode cur = head;
        while (cur != null) {
            ListNode prev = dummy;
            // Find the right place to insert cur
            while (prev.next != null && prev.next.val < cur.val) {
                prev = prev.next;
            }
            ListNode nextTemp = cur.next; // store next node
            // Insert cur between prev and prev.next
            cur.next = prev.next;
            prev.next = cur;
            // Move to the next node in original list
            cur = nextTemp;
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
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)  # pseudo-head for the sorted list
        curr = head

        while curr:
            # Find the right place to insert curr in the sorted part.
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            nxt = curr.next  # store next node to process

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move to the next node in the original list.
            curr = nxt

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
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(float('-inf'))
        cur = head
        while cur:
            prev = dummy
            # Find the right place to insert cur
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            nxt = cur.next
            # Insert cur between prev and prev.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
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
struct ListNode* insertionSortList(struct ListNode* head) {
    if (!head || !head->next) return head;
    
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = NULL;
    
    while (head) {
        struct ListNode* next = head->next;
        struct ListNode* prev = &dummy;
        
        while (prev->next && prev->next->val < head->val) {
            prev = prev->next;
        }
        
        head->next = prev->next;
        prev->next = head;
        head = next;
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
    public ListNode InsertionSortList(ListNode head) {
        if (head == null) return null;

        var dummy = new ListNode(0);
        var cur = head;

        while (cur != null) {
            // Find the correct position to insert cur
            var prev = dummy;
            while (prev.next != null && prev.next.val < cur.val) {
                prev = prev.next;
            }

            // Insert cur between prev and prev.next
            var nextTemp = cur.next;
            cur.next = prev.next;
            prev.next = cur;

            // Move to the next node in the original list
            cur = nextTemp;
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
var insertionSortList = function(head) {
    if (!head || !head.next) return head;
    
    const dummy = new ListNode(0);
    let cur = head;
    
    while (cur) {
        // Find the right place to insert cur in the sorted part.
        let prev = dummy;
        while (prev.next && prev.next.val < cur.val) {
            prev = prev.next;
        }
        
        // Insert cur between prev and prev.next
        const nextTemp = cur.next;
        cur.next = prev.next;
        prev.next = cur;
        cur = nextTemp;
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

function insertionSortList(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let cur = head;
    while (cur) {
        // Find the correct position to insert cur
        let prev = dummy;
        while (prev.next && prev.next.val < cur.val) {
            prev = prev.next;
        }
        const nextTemp = cur.next; // store next node
        // Insert cur between prev and prev.next
        cur.next = prev.next;
        prev.next = cur;
        // Move to the next node in original list
        cur = nextTemp;
    }
    return dummy.next;
};
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
    function insertionSortList($head) {
        if ($head === null) {
            return null;
        }

        $dummy = new ListNode(0);
        $current = $head;

        while ($current !== null) {
            $nextNode = $current->next; // preserve next node

            // Find the correct position to insert current node
            $prev = $dummy;
            while ($prev->next !== null && $prev->next->val < $current->val) {
                $prev = $prev->next;
            }

            // Insert between prev and prev->next
            $current->next = $prev->next;
            $prev->next = $current;

            // Move to the next node in original list
            $current = $nextNode;
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
    func insertionSortList(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        var current = head
        while let node = current {
            let nextNode = node.next
            var prev = dummy
            while let nxt = prev.next, nxt.val < node.val {
                prev = nxt
            }
            node.next = prev.next
            prev.next = node
            current = nextNode
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
    fun insertionSortList(head: ListNode?): ListNode? {
        if (head == null) return null
        val dummy = ListNode(0)
        var cur = head
        while (cur != null) {
            var prev = dummy
            // Find the right place to insert cur
            while (prev.next != null && prev.next!!.`val` < cur.`val`) {
                prev = prev.next!!
            }
            val nextTemp = cur.next
            // Insert cur between prev and prev.next
            cur.next = prev.next
            prev.next = cur
            cur = nextTemp
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
  ListNode? insertionSortList(ListNode? head) {
    if (head == null) return null;

    final dummy = ListNode(0);
    var cur = head;

    while (cur != null) {
      // Keep reference to the next node before re-linking
      final nextTemp = cur.next;

      // Find the correct position to insert cur in the sorted part
      var prev = dummy;
      while (prev.next != null && prev.next!.val < cur.val) {
        prev = prev.next!;
      }

      // Insert cur between prev and prev.next
      cur.next = prev.next;
      prev.next = cur;

      // Move to the next node in the original list
      cur = nextTemp;
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
func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	dummy := &ListNode{0, nil}
	cur := head
	for cur != nil {
		prev := dummy
		for prev.Next != nil && prev.Next.Val < cur.Val {
			prev = prev.Next
		}
		nextTemp := cur.Next
		cur.Next = prev.Next
		prev.Next = cur
		cur = nextTemp
	}
	return dummy.Next
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

def insertion_sort_list(head)
  return head if head.nil? || head.next.nil?

  dummy = ListNode.new(0)
  cur = head

  while cur
    prev = dummy
    # Find the right place to insert cur
    while prev.next && prev.next.val < cur.val
      prev = prev.next
    end

    nxt = cur.next
    cur.next = prev.next
    prev.next = cur
    cur = nxt
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
    def insertionSortList(head: ListNode): ListNode = {
        if (head == null) return null
        val dummy = new ListNode(0)
        var cur = head
        while (cur != null) {
            val next = cur.next
            var prev = dummy
            while (prev.next != null && prev.next.x < cur.x) {
                prev = prev.next
            }
            cur.next = prev.next
            prev.next = cur
            cur = next
        }
        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn insertion_sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: None });
        let mut cur = head;
        while let Some(mut node) = cur {
            let next = node.next.take();
            let mut prev = &mut dummy;
            while let Some(ref nxt) = prev.next {
                if nxt.val < node.val {
                    prev = prev.next.as_mut().unwrap();
                } else {
                    break;
                }
            }
            node.next = prev.next.take();
            prev.next = Some(node);
            cur = next;
        }
        dummy.next
    }
}
```

## Racket

```racket
(define/contract (insertion-sort-list head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (not head)
      #f
      (let ([dummy (make-list-node 0)])
        (set-list-node-next! dummy #f)
        (let loop ((curr head))
          (when curr
            (define next (list-node-next curr))
            ;; insert `curr` into the sorted part
            (let insert ((prev dummy) (node (list-node-next dummy)))
              (if (and node (< (list-node-val node) (list-node-val curr)))
                  (insert node (list-node-next node))
                  (begin
                    (set-list-node-next! prev curr)
                    (set-list-node-next! curr node))))
            (loop next)))
        (list-node-next dummy))))
```

## Erlang

```erlang
-module(solution).
-export([insertion_sort_list/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec insertion_sort_list(Head :: #list_node{} | null) -> #list_node{} | null.
insertion_sort_list(Head) ->
    sort(Head, null).

%% internal recursive sorting
sort(null, Sorted) -> Sorted;
sort(Node, Sorted) ->
    Next = Node#list_node.next,
    Detached = Node#list_node{next=null},
    NewSorted = insert(Detached, Sorted),
    sort(Next, NewSorted).

%% insert a node into sorted list and return new head
insert(Node, null) ->
    Node#list_node{next=null};
insert(Node, Head = #list_node{val=HVal}=H) ->
    if
        Node#list_node.val =< HVal ->
            Node#list_node{next=Head};
        true ->
            NewNext = insert(Node, H#list_node.next),
            H#list_node{next=NewNext}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec insertion_sort_list(head :: ListNode.t | nil) :: ListNode.t | nil
  def insertion_sort_list(head) do
    vals = collect_vals(head, [])
    sorted = Enum.sort(vals)
    build_list(sorted)
  end

  defp collect_vals(nil, acc), do: :lists.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp build_list([]), do: nil

  defp build_list([h | t]) do
    %ListNode{val: h, next: build_list(t)}
  end
end
```
