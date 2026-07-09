# 2807. Insert Greatest Common Divisors in Linked List

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
#include <numeric>

class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* cur = head;
        while (cur && cur->next) {
            int g = std::gcd(cur->val, cur->next->val);
            ListNode* gcdNode = new ListNode(g);
            gcdNode->next = cur->next;
            cur->next = gcdNode;
            // Move to the original next node
            cur = gcdNode->next;
        }
        return head;
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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            ListNode nxt = cur.next;
            int g = gcd(cur.val, nxt.val);
            ListNode gcNode = new ListNode(g);
            cur.next = gcNode;
            gcNode.next = nxt;
            cur = nxt; // move to the next original node
        }
        return head;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        import math
        if not head or not head.next:
            return head

        cur = head
        while cur and cur.next:
            nxt = cur.next
            g = math.gcd(cur.val, nxt.val)
            gcd_node = ListNode(g)
            cur.next = gcd_node
            gcd_node.next = nxt
            cur = nxt
        return head
```

## Python3

```python
from typing import Optional
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            nxt = cur.next
            g = math.gcd(cur.val, nxt.val)
            new_node = ListNode(g)
            cur.next = new_node
            new_node.next = nxt
            cur = nxt
        return head
```

## C

```c
#include <stdlib.h>

static int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    if (!head || !head->next) return head;
    struct ListNode *cur = head;
    while (cur && cur->next) {
        int g = gcd(cur->val, cur->next->val);
        struct ListNode *newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = g;
        newNode->next = cur->next;
        cur->next = newNode;
        cur = newNode->next;  // advance to the original next node
    }
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
    public ListNode InsertGreatestCommonDivisors(ListNode head)
    {
        if (head == null || head.next == null)
            return head;

        ListNode cur = head;
        while (cur != null && cur.next != null)
        {
            int g = Gcd(cur.val, cur.next.val);
            ListNode gcdNode = new ListNode(g);
            ListNode nxt = cur.next;
            cur.next = gcdNode;
            gcdNode.next = nxt;

            cur = nxt; // move to the original next node
        }

        return head;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
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
var insertGreatestCommonDivisors = function(head) {
    if (!head || !head.next) return head;
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = b;
            b = a % b;
            a = t;
        }
        return a;
    };
    
    let cur = head;
    while (cur && cur.next) {
        const nxt = cur.next;
        const g = gcd(cur.val, nxt.val);
        const newNode = new ListNode(g);
        cur.next = newNode;
        newNode.next = nxt;
        cur = nxt;
    }
    
    return head;
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

function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;

    const gcd = (a: number, b: number): number => {
        let x = a, y = b;
        while (y !== 0) {
            const temp = x % y;
            x = y;
            y = temp;
        }
        return x;
    };

    let cur: ListNode | null = head;
    while (cur && cur.next) {
        const nxt = cur.next;
        const g = gcd(cur.val, nxt.val);
        const newNode = new ListNode(g, nxt);
        cur.next = newNode;
        cur = nxt; // move to the original next node
    }

    return head;
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
    function insertGreatestCommonDivisors($head) {
        if ($head === null || $head->next === null) {
            return $head;
        }

        $node = $head;
        while ($node !== null && $node->next !== null) {
            $nextNode = $node->next;
            $gcdVal = $this->gcd($node->val, $nextNode->val);
            $gcdNode = new ListNode($gcdVal);
            // Insert gcd node between $node and $nextNode
            $node->next = $gcdNode;
            $gcdNode->next = $nextNode;

            // Move to the next original pair
            $node = $nextNode;
        }

        return $head;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $b;
            $b = $a % $b;
            $a = $tmp;
        }
        return $a;
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
    func insertGreatestCommonDivisors(_ head: ListNode?) -> ListNode? {
        var current = head
        while let next = current?.next {
            let g = gcd(current!.val, next.val)
            let newNode = ListNode(g)
            current!.next = newNode
            newNode.next = next
            current = next
        }
        return head
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = y
            y = x % y
            x = temp
        }
        return x
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
    fun insertGreatestCommonDivisors(head: ListNode?): ListNode? {
        if (head == null || head.next == null) return head
        var cur = head
        while (cur?.next != null) {
            val nxt = cur.next!!
            val g = gcd(cur.`val`, nxt.`val`)
            val newNode = ListNode(g)
            cur.next = newNode
            newNode.next = nxt
            cur = nxt
        }
        return head
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
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
  ListNode? insertGreatestCommonDivisors(ListNode? head) {
    if (head == null || head.next == null) return head;

    var node1 = head;
    while (node1?.next != null) {
      var node2 = node1!.next!;
      int g = _gcd(node1.val, node2.val);
      var gcdNode = ListNode(g);
      // Insert the new node between node1 and node2
      node1.next = gcdNode;
      gcdNode.next = node2;

      // Move to the next original pair
      node1 = node2;
    }
    return head;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = b;
      b = a % b;
      a = t;
    }
    return a;
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
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	for cur := head; cur != nil && cur.Next != nil; {
		next := cur.Next
		g := gcd(cur.Val, next.Val)
		newNode := &ListNode{Val: g, Next: next}
		cur.Next = newNode
		cur = next
	}
	return head
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def insert_greatest_common_divisors(head)
  cur = head
  while cur && cur.next
    nxt = cur.next
    g = cur.val.gcd(nxt.val)
    gcd_node = ListNode.new(g)
    cur.next = gcd_node
    gcd_node.next = nxt
    cur = nxt
  end
  head
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
    def insertGreatestCommonDivisors(head: ListNode): ListNode = {
        if (head == null || head.next == null) return head

        var node1 = head
        var node2 = head.next

        while (node2 != null) {
            val g = gcd(node1.x, node2.x)
            val newNode = new ListNode(g)

            // insert newNode between node1 and node2
            node1.next = newNode
            newNode.next = node2

            // advance pointers to next original pair
            node1 = node2
            node2 = node2.next
        }

        head
    }

    private def gcd(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        if (x < 0) -x else x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn insert_greatest_common_divisors(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = b;
                b = a % b;
                a = t;
            }
            a
        }

        let mut head = head;
        let mut ptr = head.as_mut();
        while let Some(node) = ptr {
            if node.next.is_some() {
                let next_val = node.next.as_ref().unwrap().val;
                let g = gcd(node.val, next_val);
                let mut new_node = Box::new(ListNode { val: g, next: None });
                new_node.next = node.next.take();
                node.next = Some(new_node);
                let cur = node.next.as_mut().unwrap(); // the inserted node
                ptr = cur.next.as_mut(); // move to original second node
            } else {
                break;
            }
        }
        head
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
;; (struct list-node
;;   (val next) #:mutable #:transparent)

(define (gcd a b)
  (let loop ((a a) (b b))
    (if (= b 0)
        a
        (loop b (remainder a b)))))

(define/contract (insert-greatest-common-divisors head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (if (or (not head) (not (list-node-next head)))
      head
      (let ((curr head))
        (let loop ()
          (define nxt (list-node-next curr))
          (when nxt
            (define g (gcd (list-node-val curr) (list-node-val nxt)))
            (define newNode (make-list-node g))
            (set-list-node-next! curr newNode)
            (set-list-node-next! newNode nxt)
            (set! curr nxt)
            (loop)))
        head)))
```

## Erlang

```erlang
-module(solution).
-export([insert_greatest_common_divisors/1]).

%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec insert_greatest_common_divisors(Head :: #list_node{} | null) -> #list_node{} | null.
insert_greatest_common_divisors(null) ->
    null;
insert_greatest_common_divisors(Head = #list_node{}) ->
    case Head#list_node.next of
        null -> Head;
        _ -> process_pair(Head)
    end.

process_pair(#list_node{next=null}=Node) ->
    Node;
process_pair(Node = #list_node{val=V1, next=Node2}) when is_record(Node2, list_node) ->
    #list_node{val=V2} = Node2,
    G = gcd(V1, V2),
    ProcessedTail = process_pair(Node2),
    NewGcdNode = #list_node{val=G, next=ProcessedTail},
    Node#list_node{next=NewGcdNode}.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec insert_greatest_common_divisors(head :: ListNode.t() | nil) :: ListNode.t() | nil
  def insert_greatest_common_divisors(nil), do: nil
  def insert_greatest_common_divisors(head) do
    process(head)
  end

  defp process(%ListNode{val: v, next: nil}) do
    %ListNode{val: v, next: nil}
  end

  defp process(%ListNode{val: v, next: nxt}) do
    g = gcd(v, nxt.val)
    processed_next = process(nxt)

    %ListNode{
      val: v,
      next: %ListNode{
        val: g,
        next: processed_next
      }
    }
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
```
