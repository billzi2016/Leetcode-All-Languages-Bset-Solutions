# 2487. Remove Nodes From Linked List

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
    // Helper to reverse a singly linked list
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) {
            ListNode* nxt = head->next;
            head->next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }

    ListNode* removeNodes(ListNode* head) {
        if (!head) return nullptr;

        // Step 1: reverse the list
        ListNode* rev = reverseList(head);

        // Step 2: delete nodes that are smaller than a previously seen maximum
        int maxVal = -1;                     // values are >= 1, so -1 works as initial sentinel
        ListNode dummy(0);
        dummy.next = rev;
        ListNode* prev = &dummy;

        while (prev->next) {
            if (prev->next->val < maxVal) {
                // remove the node
                ListNode* del = prev->next;
                prev->next = del->next;
                // optional: delete del; // not required for LeetCode judging
            } else {
                maxVal = prev->next->val;
                prev = prev->next;
            }
        }

        // Step 3: reverse again to restore original order (now filtered)
        return reverseList(dummy.next);
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
    public ListNode removeNodes(ListNode head) {
        // Reverse the list to process from original right to left
        head = reverse(head);
        
        int max = Integer.MIN_VALUE;
        ListNode curr = head;
        ListNode prev = null;
        
        while (curr != null) {
            if (curr.val >= max) {
                max = curr.val;
                prev = curr;
                curr = curr.next;
            } else {
                // Remove current node
                if (prev != null) {
                    prev.next = curr.next;
                }
                ListNode toDelete = curr;
                curr = curr.next;
                // Optional: clean up reference
                toDelete.next = null;
            }
        }
        
        // Reverse again to restore original order with deletions applied
        return reverse(head);
    }
    
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode nextTmp = head.next;
            head.next = prev;
            prev = head;
            head = nextTmp;
        }
        return prev;
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
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Helper to reverse a linked list in-place.
        def reverse(node):
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        # Reverse the original list to process from right to left.
        rev = reverse(head)

        max_val = -float('inf')
        cur = rev
        prev = None
        while cur:
            if cur.val >= max_val:
                max_val = cur.val
                prev = cur
                cur = cur.next
            else:
                # Skip the current node.
                if prev:
                    prev.next = cur.next
                cur = cur.next

        # Reverse again to restore original order (now filtered).
        return reverse(rev)
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
    def removeNodes(self, head: Optional['ListNode']) -> Optional['ListNode']:
        # Helper to reverse a singly linked list
        def reverse(node: Optional['ListNode']) -> Optional['ListNode']:
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        # Reverse the list to process from original right to left
        head = reverse(head)

        max_val = 0  # values are >=1 per constraints
        cur = head
        prev = None
        while cur:
            if cur.val < max_val:
                # Remove current node
                prev.next = cur.next
                cur = cur.next
            else:
                max_val = cur.val
                prev = cur
                cur = cur.next

        # Reverse again to restore original order (now filtered)
        return reverse(head)
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
static struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL, *curr = head, *next;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

struct ListNode* removeNodes(struct ListNode* head) {
    if (!head) return NULL;

    /* Reverse the list */
    head = reverseList(head);

    int maxVal = -1;  // values are >= 1
    struct ListNode *curr = head, *prev = NULL;
    while (curr) {
        if (curr->val < maxVal) {
            /* Delete current node */
            struct ListNode* del = curr;
            if (prev)
                prev->next = curr->next;
            else
                head = curr->next;  // not expected to happen due to init maxVal
            curr = curr->next;
            /* optional free: */ 
            // free(del);
        } else {
            maxVal = curr->val;
            prev = curr;
            curr = curr->next;
        }
    }

    /* Reverse back to original order */
    head = reverseList(head);
    return head;
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
    private ListNode Reverse(ListNode head)
    {
        ListNode prev = null;
        while (head != null)
        {
            ListNode nxt = head.next;
            head.next = prev;
            prev = head;
            head = nxt;
        }
        return prev;
    }

    public ListNode RemoveNodes(ListNode head)
    {
        // Reverse the list to process from right to left
        head = Reverse(head);

        int maxVal = int.MinValue;
        ListNode cur = head;
        ListNode prev = null;

        while (cur != null)
        {
            if (cur.val >= maxVal)
            {
                maxVal = cur.val;
                prev = cur;
                cur = cur.next;
            }
            else
            {
                // Delete current node
                prev.next = cur.next;
                cur = prev.next;
            }
        }

        // Reverse again to restore original order (now filtered)
        return Reverse(head);
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
var removeNodes = function(head) {
    // Helper to reverse a singly linked list
    const reverseList = (node) => {
        let prev = null;
        while (node) {
            const nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    };
    
    // Reverse the original list
    head = reverseList(head);
    
    // Remove nodes that are smaller than a previously seen maximum
    let maxVal = -Infinity;
    let cur = head;
    let prev = null;
    while (cur) {
        if (cur.val >= maxVal) {
            maxVal = cur.val;
            prev = cur;
            cur = cur.next;
        } else {
            // Delete cur
            if (prev) {
                prev.next = cur.next;
            }
            const nxt = cur.next;
            cur.next = null; // optional cleanup
            cur = nxt;
        }
    }
    
    // Reverse again to restore required order
    return reverseList(head);
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

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    while (head !== null) {
        const nxt = head.next;
        head.next = prev;
        prev = head;
        head = nxt;
    }
    return prev;
}

function removeNodes(head: ListNode | null): ListNode | null {
    // Reverse the list to process from right to left
    let rev = reverseList(head);
    let maxVal = -Infinity;
    let newHead: ListNode | null = null;

    while (rev !== null) {
        if (rev.val >= maxVal) {
            maxVal = rev.val;
            const nxt = rev.next;
            // Prepend to the result list
            rev.next = newHead;
            newHead = rev;
            rev = nxt;
        } else {
            // Skip this node
            rev = rev.next;
        }
    }

    return newHead;
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
    public function removeNodes($head) {
        // Reverse the list to process from right to left
        $head = $this->reverseList($head);

        $max = PHP_INT_MIN;
        $prev = null;
        $curr = $head;

        while ($curr !== null) {
            if ($curr->val < $max) {
                // Remove current node
                $prev->next = $curr->next;
                $temp = $curr;
                $curr = $curr->next;
                $temp->next = null; // clean up reference
            } else {
                $max = $curr->val;
                $prev = $curr;
                $curr = $curr->next;
            }
        }

        // Reverse again to restore original order (now filtered)
        return $this->reverseList($head);
    }

    /**
     * @param ListNode $head
     * @return ListNode
     */
    private function reverseList($head) {
        $prev = null;
        $curr = $head;

        while ($curr !== null) {
            $nextTemp = $curr->next;
            $curr->next = $prev;
            $prev = $curr;
            $curr = $nextTemp;
        }

        return $prev;
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
    func removeNodes(_ head: ListNode?) -> ListNode? {
        // Reverse the list
        var revHead = reverse(head)
        
        var maxVal = Int.min
        var prev: ListNode? = nil
        var curr = revHead
        
        while let node = curr {
            if node.val >= maxVal {
                maxVal = node.val
                prev = node
                curr = node.next
            } else {
                // Skip the current node
                prev?.next = node.next
                curr = node.next
            }
        }
        
        // Reverse again to restore original order (now filtered)
        return reverse(revHead)
    }
    
    private func reverse(_ head: ListNode?) -> ListNode? {
        var prev: ListNode? = nil
        var curr = head
        while let node = curr {
            let nextTemp = node.next
            node.next = prev
            prev = node
            curr = nextTemp
        }
        return prev
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeNodes(head: ListNode?): ListNode? {
        var revHead = reverse(head)
        var maxVal = Int.MIN_VALUE
        var cur = revHead
        var prev: ListNode? = null
        while (cur != null) {
            if (cur.`val` < maxVal) {
                val nxt = cur.next
                if (prev != null) {
                    prev!!.next = nxt
                } else {
                    revHead = nxt
                }
                cur = nxt
            } else {
                maxVal = cur.`val`
                prev = cur
                cur = cur.next
            }
        }
        return reverse(revHead)
    }

    private fun reverse(head: ListNode?): ListNode? {
        var prev: ListNode? = null
        var curr = head
        while (curr != null) {
            val nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        }
        return prev
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
  ListNode? _reverse(ListNode? head) {
    ListNode? prev = null;
    var curr = head;
    while (curr != null) {
      var nxt = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nxt;
    }
    return prev;
  }

  ListNode? removeNodes(ListNode? head) {
    if (head == null) return null;

    // Reverse the list to process from right to left.
    head = _reverse(head);

    int maxVal = -1; // values are >= 1, so this works as initial minimum.
    ListNode? keptPrev;
    var curr = head;

    while (curr != null) {
      if (curr.val >= maxVal) {
        maxVal = curr.val;
        keptPrev = curr;
        curr = curr.next;
      } else {
        // Remove current node.
        var nxt = curr.next;
        if (keptPrev != null) {
          keptPrev.next = nxt;
        }
        curr = nxt;
      }
    }

    // Reverse again to restore original order with deletions applied.
    return _reverse(head);
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
func removeNodes(head *ListNode) *ListNode {
	// Reverse the list
	var prev *ListNode
	cur := head
	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	reversed := prev

	// Remove nodes that are smaller than a previously seen maximum
	maxVal := 0
	var keptPrev *ListNode
	cur = reversed
	for cur != nil {
		next := cur.Next
		if cur.Val < maxVal {
			if keptPrev != nil {
				keptPrev.Next = next
			}
		} else {
			maxVal = cur.Val
			keptPrev = cur
		}
		cur = next
	}

	// Reverse again to restore original order (now filtered)
	prev = nil
	cur = reversed
	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
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

def reverse(head)
  prev = nil
  cur = head
  while cur
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  end
  prev
end

# @param {ListNode} head
# @return {ListNode}
def remove_nodes(head)
  return nil unless head

  # Reverse the list to process from right to left
  head = reverse(head)

  max_val = -Float::INFINITY
  prev = nil
  cur = head

  while cur
    if cur.val < max_val
      # Delete current node
      prev.next = cur.next if prev
      cur = cur.next
    else
      max_val = cur.val
      prev = cur
      cur = cur.next
    end
  end

  # Reverse again to restore original order (now filtered)
  reverse(head)
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
    def removeNodes(head: ListNode): ListNode = {
        // Helper to reverse a singly linked list
        def reverse(node: ListNode): ListNode = {
            var prev: ListNode = null
            var cur = node
            while (cur != null) {
                val nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            }
            prev
        }

        // Reverse the list to process from right to left
        var revHead = reverse(head)

        var maxVal = Int.MinValue
        var curr = revHead
        var prev: ListNode = null

        while (curr != null) {
            if (curr.x >= maxVal) {
                maxVal = curr.x
                prev = curr
                curr = curr.next
            } else {
                // Delete current node
                val toDelete = curr
                if (prev != null) {
                    prev.next = curr.next
                }
                curr = curr.next
                // Optional cleanup
                toDelete.next = null
            }
        }

        // Reverse again to restore original order with deletions applied
        reverse(revHead)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn reverse(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
            let mut prev = None;
            while let Some(mut node) = head {
                let next = node.next.take();
                node.next = prev;
                prev = Some(node);
                head = next;
            }
            prev
        }

        // Reverse the original list.
        let rev = reverse(head);

        // Traverse reversed list, keep nodes that are >= max seen so far,
        // and build the resulting list in correct order by prepending.
        let mut max_val = i32::MIN;
        let mut dummy = Box::new(ListNode { val: 0, next: None });
        let mut cur_opt = rev;

        while let Some(mut node) = cur_opt {
            let next = node.next.take();
            if node.val >= max_val {
                max_val = node.val;
                node.next = dummy.next.take();
                dummy.next = Some(node);
            }
            // else node is dropped
            cur_opt = next;
        }

        dummy.next
    }
}
```

## Racket

```racket
(define (reverse-list head)
  (let loop ((prev #f) (curr head))
    (if (not curr)
        prev
        (let ((next (list-node-next curr)))
          (set-list-node-next! curr prev)
          (loop curr next)))))

(define/contract (remove-nodes head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (not head)
      #f
      (let* ((rev (reverse-list head))
             (dummy (make-list-node)))
        (set-list-node-next! dummy rev)
        (let loop ((prev dummy) (cur rev) (max -inf.0))
          (if (not cur)
              (reverse-list (list-node-next dummy))
              (let ((next (list-node-next cur))
                    (val  (list-node-val cur)))
                (if (>= val max)
                    (begin
                      (set! max val)
                      (loop cur next max))
                    (begin
                      (set-list-node-next! prev next)
                      (loop prev next max)))))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_nodes/1]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec remove_nodes(Head :: #list_node{} | null) -> #list_node{} | null.
remove_nodes(null) ->
    null;
remove_nodes(Head) ->
    Rev = reverse_list(Head),
    filter_keep(Rev, 0, null).

%% Reverse the linked list
-spec reverse_list(#list_node{} | null) -> #list_node{} | null.
reverse_list(Head) ->
    rev_acc(Head, null).

-spec rev_acc(#list_node{} | null, #list_node{} | null) -> #list_node{} | null.
rev_acc(null, Acc) ->
    Acc;
rev_acc(Node, Acc) ->
    Next = Node#list_node.next,
    NewNode = Node#list_node{next = Acc},
    rev_acc(Next, NewNode).

%% Keep nodes whose value is >= max seen so far while traversing
-spec filter_keep(#list_node{} | null, integer(), #list_node{} | null) -> #list_node{} | null.
filter_keep(null, _Max, Acc) ->
    Acc;
filter_keep(Node, Max, Acc) ->
    Val = Node#list_node.val,
    Next = Node#list_node.next,
    if
        Val >= Max ->
            NewAcc = Node#list_node{next = Acc},
            filter_keep(Next, Val, NewAcc);
        true ->
            filter_keep(Next, Max, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_nodes(head :: ListNode.t | nil) :: ListNode.t | nil
  def remove_nodes(head) do
    rev = reverse(head)
    build_filtered(rev, nil, 0)
  end

  # Reverse the linked list.
  defp reverse(head), do: reverse(head, nil)

  defp reverse(nil, acc), do: acc

  defp reverse(%ListNode{val: v, next: nxt}, acc) do
    reverse(nxt, %ListNode{val: v, next: acc})
  end

  # Traverse the reversed list, keeping nodes whose value is >= max seen so far.
  # Prepend kept nodes to the result to obtain the final order.
  defp build_filtered(nil, result, _max), do: result

  defp build_filtered(%ListNode{val: v, next: nxt}, result, max) do
    if v >= max do
      new_node = %ListNode{val: v, next: result}
      build_filtered(nxt, new_node, v)
    else
      build_filtered(nxt, result, max)
    end
  end
end
```
