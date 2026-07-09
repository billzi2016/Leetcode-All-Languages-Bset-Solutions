# 2181. Merge Nodes in Between Zeros

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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* cur = head->next;          // start after leading zero
        ListNode* prev = head;               // will build result list using dummy head
        
        while (cur) {
            int sum = 0;
            while (cur && cur->val != 0) {   // accumulate until next zero
                sum += cur->val;
                cur = cur->next;
            }
            // create node for the summed block
            ListNode* node = new ListNode(sum);
            prev->next = node;
            prev = node;
            
            if (cur) cur = cur->next;        // skip the zero delimiter
        }
        prev->next = nullptr;                // terminate the list
        return head->next;                   // first summed node
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
    public ListNode mergeNodes(ListNode head) {
        // Dummy node to build the result list
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        // Start after the leading zero
        ListNode cur = head.next;
        while (cur != null) {
            int sum = 0;
            // Accumulate values until the next zero
            while (cur != null && cur.val != 0) {
                sum += cur.val;
                cur = cur.next;
            }
            // cur is now at a zero node (or null, which shouldn't happen per constraints)
            tail.next = new ListNode(sum);
            tail = tail.next;
            
            // Move past the zero to start next segment
            if (cur != null) {
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
```

## Python

```python
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        tail = dummy
        cur = head.next  # skip the leading zero

        while cur:
            block_sum = 0
            while cur and cur.val != 0:
                block_sum += cur.val
                cur = cur.next
            # cur is at a zero node (or None if list ended, which shouldn't happen per constraints)
            tail.next = ListNode(block_sum)
            tail = tail.next
            if cur:
                cur = cur.next  # move past the zero to start next block

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
    def mergeNodes(self, head: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0)
        tail = dummy
        cur_sum = 0
        node = head.next  # skip the leading zero
        
        while node:
            if node.val == 0:
                tail.next = ListNode(cur_sum)
                tail = tail.next
                cur_sum = 0
            else:
                cur_sum += node.val
            node = node.next
        
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
struct ListNode* mergeNodes(struct ListNode* head) {
    if (!head) return NULL;

    struct ListNode *node = head->next;          // start after leading zero
    struct ListNode *newHead = NULL;             // head of result list
    struct ListNode *prevResult = NULL;          // last node in result list
    struct ListNode *write = NULL;               // node that will store current block sum
    int sum = 0;

    while (node) {
        if (node->val == 0) {                    // end of a block
            if (write != NULL) {
                write->val = sum;                // store the accumulated sum
                if (newHead == NULL) {
                    newHead = write;
                } else {
                    prevResult->next = write;
                }
                prevResult = write;
                write = NULL;
                sum = 0;
            }
        } else {                                 // inside a block
            sum += node->val;
            if (write == NULL) {
                write = node;                    // first node of this block becomes the sum node
            }
        }
        node = node->next;
    }

    if (prevResult) {
        prevResult->next = NULL;                 // terminate the list
    }

    return newHead;
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
    public ListNode MergeNodes(ListNode head) {
        // Dummy node to build the result list
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        int sum = 0;
        ListNode cur = head.next; // skip leading zero

        while (cur != null) {
            if (cur.val == 0) {
                // End of a segment, create node with accumulated sum
                tail.next = new ListNode(sum);
                tail = tail.next;
                sum = 0;
            } else {
                sum += cur.val;
            }
            cur = cur.next;
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
var mergeNodes = function(head) {
    // Skip the leading zero node.
    let cur = head.next;
    const dummy = new ListNode(0);
    let tail = dummy;
    let sum = 0;
    
    while (cur !== null) {
        if (cur.val === 0) {
            // End of a segment: create a node with the accumulated sum.
            tail.next = new ListNode(sum);
            tail = tail.next;
            sum = 0; // reset for next segment
        } else {
            sum += cur.val;
        }
        cur = cur.next;
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

function mergeNodes(head: ListNode | null): ListNode | null {
    if (!head) return null;
    
    const dummy = new ListNode(0);
    let tail = dummy;
    let cur = head.next; // skip the leading zero
    
    while (cur) {
        let sum = 0;
        while (cur && cur.val !== 0) {
            sum += cur.val;
            cur = cur.next!;
        }
        // cur is at a zero node (or null after last block)
        tail.next = new ListNode(sum);
        tail = tail.next;
        if (cur) {
            cur = cur.next; // move past the zero to start next segment
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
    function mergeNodes($head) {
        // Pointer to the zero node preceding the current block
        $writePrev = $head;
        // Pointer used to traverse nodes and compute sums
        $ptr = $head->next;

        while ($ptr !== null) {
            $sum = 0;
            // Accumulate values until the next zero is encountered
            while ($ptr !== null && $ptr->val != 0) {
                $sum += $ptr->val;
                $ptr = $ptr->next;
            }

            // $writePrev->next is the first node of the block; store the sum there
            $writePrev->next->val = $sum;

            // Link this summed node to the start of the next block (if any)
            $writePrev->next->next = ($ptr !== null) ? $ptr->next : null;

            // Move write pointer forward to the node we just updated
            $writePrev = $writePrev->next;

            // Skip the zero that terminated the current block
            if ($ptr !== null) {
                $ptr = $ptr->next;
            }
        }

        // The list now starts after the initial dummy zero
        return $head->next;
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
    func mergeNodes(_ head: ListNode?) -> ListNode? {
        var cur = head?.next          // skip the leading zero
        let dummy = ListNode(0)
        var tail = dummy
        
        while let start = cur {
            var sum = 0
            var ptr = start
            // accumulate until we hit a zero node
            while ptr.val != 0 {
                sum += ptr.val
                if let nxt = ptr.next {
                    ptr = nxt
                } else { break }
            }
            // create merged node
            tail.next = ListNode(sum)
            tail = tail.next!
            // move to the node after the zero delimiter
            cur = ptr.next
        }
        
        return dummy.next
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeNodes(head: ListNode?): ListNode? {
        var modify = head?.next
        var cur = modify
        while (cur != null) {
            var sum = 0
            while (cur != null && cur.`val` != 0) {
                sum += cur.`val`
                cur = cur.next
            }
            // cur is at a zero node (or null, but per constraints it's a zero)
            modify?.`val` = sum
            modify?.next = cur?.next
            modify = modify?.next
            cur = cur?.next
        }
        return head?.next
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
  ListNode? mergeNodes(ListNode? head) {
    if (head == null) return null;
    ListNode? curZero = head;
    while (curZero != null && curZero.next != null) {
      int sum = 0;
      ListNode? runner = curZero.next;
      while (runner != null && runner.val != 0) {
        sum += runner.val;
        runner = runner.next;
      }
      // runner is the zero that ends the current segment
      curZero.val = sum;
      curZero.next = runner?.next; // skip zeros and intermediate nodes
      curZero = curZero.next; // move to start of next segment
    }
    return head;
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
func mergeNodes(head *ListNode) *ListNode {
    dummy := &ListNode{}
    tail := dummy
    cur := head.Next

    for cur != nil {
        sum := 0
        for cur != nil && cur.Val != 0 {
            sum += cur.Val
            cur = cur.Next
        }
        tail.Next = &ListNode{Val: sum}
        tail = tail.Next
        if cur != nil {
            cur = cur.Next
        }
    }
    return dummy.Next
}
```

## Ruby

```ruby
def merge_nodes(head)
  cur = head.next
  dummy = ListNode.new(0)
  tail = dummy
  sum = 0
  while cur
    if cur.val == 0
      tail.next = ListNode.new(sum)
      tail = tail.next
      sum = 0
    else
      sum += cur.val
    end
    cur = cur.next
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
    def mergeNodes(head: ListNode): ListNode = {
        var cur = head.next          // skip leading zero
        val dummy = new ListNode(0)
        var tail = dummy

        while (cur != null) {
            var sum = 0
            while (cur != null && cur.x != 0) {
                sum += cur.x
                cur = cur.next
            }
            // cur is at a zero node (or null after the last block)
            tail.next = new ListNode(sum)
            tail = tail.next
            if (cur != null) cur = cur.next   // skip the zero delimiter
        }

        dummy.next
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_nodes(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Skip the leading zero node.
        let mut cur = head.as_ref().and_then(|node| node.next.as_ref());
        let mut sum = 0;
        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;

        while let Some(node) = cur {
            if node.val == 0 {
                // End of a segment: create a new node with the accumulated sum.
                tail.next = Some(Box::new(ListNode::new(sum)));
                tail = tail.next.as_mut().unwrap();
                sum = 0;
            } else {
                sum += node.val;
            }
            cur = node.next.as_ref();
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

(define/contract (merge-nodes head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (not head)
      #f
      (let ([dummy (make-list-node 0)])
        (let loop ((cur (list-node-next head)) (tail dummy))
          (if (not cur)
              (list-node-next dummy)
              (let sum-loop ((node cur) (s 0))
                (if (and node (not (= (list-node-val node) 0)))
                    (sum-loop (list-node-next node) (+ s (list-node-val node)))
                    (let ((newnode (make-list-node s)))
                      (set-list-node-next! tail newnode)
                      (let ((next-cur (if node (list-node-next node) #f)))
                        (loop next-cur newnode))))))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec merge_nodes(Head :: #list_node{} | null) -> #list_node{} | null.
merge_nodes(null) ->
    null;
merge_nodes(Head) ->
    Sums = collect_sums(Head#list_node.next, 0, []),
    build_list(Sums).

collect_sums(null, _Acc, Acc) ->
    lists:reverse(Acc);
collect_sums(Node, Acc, AccList) ->
    case Node#list_node.val of
        0 ->
            NewAcc = [Acc | AccList],
            collect_sums(Node#list_node.next, 0, NewAcc);
        V when is_integer(V) ->
            collect_sums(Node#list_node.next, Acc + V, AccList)
    end.

build_list([]) -> null;
build_list([H|T]) ->
    #list_node{val = H, next = build_list(T)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec merge_nodes(head :: ListNode.t | nil) :: ListNode.t | nil
  def merge_nodes(nil), do: nil

  def merge_nodes(%ListNode{next: next_node}) do
    sums = collect_sums(next_node, [], 0)
    build_list(sums)
  end

  defp collect_sums(nil, acc, _cur), do: Enum.reverse(acc)

  defp collect_sums(%ListNode{val: v, next: nxt}, acc, cur) do
    if v == 0 do
      # End of a block; store the accumulated sum.
      collect_sums(nxt, [cur | acc], 0)
    else
      collect_sums(nxt, acc, cur + v)
    end
  end

  defp build_list([]), do: nil

  defp build_list([h | t]) do
    %ListNode{val: h, next: build_list(t)}
  end
end
```
