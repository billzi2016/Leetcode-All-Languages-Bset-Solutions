# 0445. Add Two Numbers II

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        std::vector<int> s1, s2;
        while (l1) { s1.push_back(l1->val); l1 = l1->next; }
        while (l2) { s2.push_back(l2->val); l2 = l2->next; }
        
        int i = (int)s1.size() - 1;
        int j = (int)s2.size() - 1;
        int carry = 0;
        ListNode* head = nullptr;
        
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += s1[i--];
            if (j >= 0) sum += s2[j--];
            ListNode* node = new ListNode(sum % 10);
            node->next = head;
            head = node;
            carry = sum / 10;
        }
        return head;
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Deque<Integer> s1 = new ArrayDeque<>();
        Deque<Integer> s2 = new ArrayDeque<>();
        
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        
        ListNode head = null;
        int carry = 0;
        while (!s1.isEmpty() || !s2.isEmpty() || carry != 0) {
            int sum = carry;
            if (!s1.isEmpty()) sum += s1.pop();
            if (!s2.isEmpty()) sum += s2.pop();
            
            ListNode node = new ListNode(sum % 10);
            node.next = head;
            head = node;
            carry = sum / 10;
        }
        
        return head;
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry:
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10

        return head
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional['ListNode'], l2: Optional['ListNode']) -> Optional['ListNode']:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry:
            total = carry
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10

        return head
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
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int s1[101], top1 = 0;
    while (l1) {
        s1[top1++] = l1->val;
        l1 = l1->next;
    }
    
    int s2[101], top2 = 0;
    while (l2) {
        s2[top2++] = l2->val;
        l2 = l2->next;
    }
    
    int carry = 0;
    struct ListNode* head = NULL;
    
    while (top1 > 0 || top2 > 0 || carry) {
        int sum = carry;
        if (top1 > 0) sum += s1[--top1];
        if (top2 > 0) sum += s2[--top2];
        
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = head;
        head = node;
        carry = sum / 10;
    }
    
    return head;
}
```

## Csharp

```csharp
using System.Collections.Generic;

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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        Stack<int> s1 = new Stack<int>();
        Stack<int> s2 = new Stack<int>();
        
        while (l1 != null) {
            s1.Push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.Push(l2.val);
            l2 = l2.next;
        }
        
        int carry = 0;
        ListNode head = null;
        while (s1.Count > 0 || s2.Count > 0 || carry > 0) {
            int sum = carry;
            if (s1.Count > 0) sum += s1.Pop();
            if (s2.Count > 0) sum += s2.Pop();
            
            ListNode node = new ListNode(sum % 10);
            node.next = head;
            head = node;
            carry = sum / 10;
        }
        
        return head;
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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    const s1 = [], s2 = [];
    while (l1) {
        s1.push(l1.val);
        l1 = l1.next;
    }
    while (l2) {
        s2.push(l2.val);
        l2 = l2.next;
    }
    let carry = 0;
    let head = null;
    while (s1.length || s2.length || carry) {
        const sum = (s1.pop() || 0) + (s2.pop() || 0) + carry;
        const node = new ListNode(sum % 10);
        node.next = head;
        head = node;
        carry = Math.floor(sum / 10);
    }
    return head;
};
```

## Typescript

```typescript
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const s1: number[] = [];
    const s2: number[] = [];

    while (l1) {
        s1.push(l1.val);
        l1 = l1.next;
    }
    while (l2) {
        s2.push(l2.val);
        l2 = l2.next;
    }

    let carry = 0;
    let head: ListNode | null = null;

    while (s1.length > 0 || s2.length > 0 || carry !== 0) {
        let sum = carry;
        if (s1.length > 0) sum += s1.pop()!;
        if (s2.length > 0) sum += s2.pop()!;

        const node = new ListNode(sum % 10);
        node.next = head;
        head = node;
        carry = Math.floor(sum / 10);
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
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $s1 = [];
        $s2 = [];

        while ($l1 !== null) {
            $s1[] = $l1->val;
            $l1 = $l1->next;
        }

        while ($l2 !== null) {
            $s2[] = $l2->val;
            $l2 = $l2->next;
        }

        $carry = 0;
        $head = null;

        while (!empty($s1) || !empty($s2) || $carry > 0) {
            $sum = $carry;
            if (!empty($s1)) {
                $sum += array_pop($s1);
            }
            if (!empty($s2)) {
                $sum += array_pop($s2);
            }

            $node = new ListNode($sum % 10);
            $node->next = $head;
            $head = $node;

            $carry = intdiv($sum, 10);
        }

        return $head;
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
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var s1 = [Int]()
        var s2 = [Int]()
        var p = l1
        while let node = p {
            s1.append(node.val)
            p = node.next
        }
        var q = l2
        while let node = q {
            s2.append(node.val)
            q = node.next
        }
        
        var carry = 0
        var head: ListNode? = nil
        
        while !s1.isEmpty || !s2.isEmpty {
            let x = s1.popLast() ?? 0
            let y = s2.popLast() ?? 0
            let sum = x + y + carry
            let node = ListNode(sum % 10)
            node.next = head
            head = node
            carry = sum / 10
        }
        
        if carry > 0 {
            let node = ListNode(carry)
            node.next = head
            head = node
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
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val s1 = ArrayDeque<Int>()
        val s2 = ArrayDeque<Int>()
        var p1 = l1
        while (p1 != null) {
            s1.push(p1.`val`)
            p1 = p1.next
        }
        var p2 = l2
        while (p2 != null) {
            s2.push(p2.`val`)
            p2 = p2.next
        }

        var carry = 0
        var head: ListNode? = null
        while (!s1.isEmpty() || !s2.isEmpty() || carry != 0) {
            var sum = carry
            if (!s1.isEmpty()) sum += s1.pop()
            if (!s2.isEmpty()) sum += s2.pop()
            val node = ListNode(sum % 10)
            node.next = head
            head = node
            carry = sum / 10
        }
        return head
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
  ListNode? addTwoNumbers(ListNode? l1, ListNode? l2) {
    final List<int> s1 = [];
    final List<int> s2 = [];

    while (l1 != null) {
      s1.add(l1.val);
      l1 = l1.next;
    }
    while (l2 != null) {
      s2.add(l2.val);
      l2 = l2.next;
    }

    int carry = 0;
    ListNode? head;

    while (s1.isNotEmpty || s2.isNotEmpty || carry != 0) {
      int sum = carry;
      if (s1.isNotEmpty) sum += s1.removeLast();
      if (s2.isNotEmpty) sum += s2.removeLast();

      final node = ListNode(sum % 10);
      node.next = head;
      head = node;

      carry = sum ~/ 10;
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
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var s1 []int
    for cur := l1; cur != nil; cur = cur.Next {
        s1 = append(s1, cur.Val)
    }
    var s2 []int
    for cur := l2; cur != nil; cur = cur.Next {
        s2 = append(s2, cur.Val)
    }

    carry := 0
    var head *ListNode

    for len(s1) > 0 || len(s2) > 0 || carry > 0 {
        sum := carry
        if len(s1) > 0 {
            sum += s1[len(s1)-1]
            s1 = s1[:len(s1)-1]
        }
        if len(s2) > 0 {
            sum += s2[len(s2)-1]
            s2 = s2[:len(s2)-1]
        }
        node := &ListNode{
            Val:  sum % 10,
            Next: head,
        }
        head = node
        carry = sum / 10
    }

    return head
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

def add_two_numbers(l1, l2)
  s1 = []
  while l1
    s1 << l1.val
    l1 = l1.next
  end

  s2 = []
  while l2
    s2 << l2.val
    l2 = l2.next
  end

  carry = 0
  head = nil

  while !s1.empty? || !s2.empty? || carry != 0
    sum = carry
    sum += s1.pop unless s1.empty?
    sum += s2.pop unless s2.empty?

    node = ListNode.new(sum % 10)
    node.next = head
    head = node

    carry = sum / 10
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
import scala.collection.mutable.Stack

object Solution {
  def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
    val s1 = Stack[Int]()
    val s2 = Stack[Int]()

    var p = l1
    while (p != null) {
      s1.push(p.x)
      p = p.next
    }

    var q = l2
    while (q != null) {
      s2.push(q.x)
      q = q.next
    }

    var carry = 0
    var head: ListNode = null

    while (s1.nonEmpty || s2.nonEmpty) {
      val a = if (s1.isEmpty) 0 else s1.pop()
      val b = if (s2.isEmpty) 0 else s2.pop()
      val sum = a + b + carry
      val node = new ListNode(sum % 10)
      node.next = head
      head = node
      carry = sum / 10
    }

    if (carry > 0) {
      val node = new ListNode(carry)
      node.next = head
      head = node
    }

    head
  }
}
```

## Rust

```rust
impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut s1 = Vec::new();
        let mut s2 = Vec::new();

        let mut cur = &l1;
        while let Some(node) = cur {
            s1.push(node.val);
            cur = &node.next;
        }

        let mut cur = &l2;
        while let Some(node) = cur {
            s2.push(node.val);
            cur = &node.next;
        }

        let mut carry = 0;
        let mut head: Option<Box<ListNode>> = None;

        while !s1.is_empty() || !s2.is_empty() || carry != 0 {
            let mut sum = carry;
            if let Some(v) = s1.pop() {
                sum += v;
            }
            if let Some(v) = s2.pop() {
                sum += v;
            }

            let new_node = ListNode {
                val: sum % 10,
                next: head,
            };
            head = Some(Box::new(new_node));
            carry = sum / 10;
        }

        head
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
(struct list-node
  (val next) #:mutable #:transparent)

(define (make-list-node [val 0])
  (list-node val #f))

(: add-two-numbers (-> (or/c list-node? #false)
                       (or/c list-node? #false)
                       (or/c list-node? #false)))
(define (add-two-numbers l1 l2)
  ;; Build a stack (list) of values from head to tail; top will be least‑significant digit.
  (define (build-stack lst)
    (let recur ((node lst) (stk '()))
      (if (not node)
          stk
          (recur (list-node-next node) (cons (list-node-val node) stk)))))
  (define s1 (build-stack l1))
  (define s2 (build-stack l2))

  ;; Process stacks, creating result list by prepending nodes.
  (let loop ((st1 s1) (st2 s2) (carry 0) (ans #f))
    (if (and (null? st1) (null? st2) (= carry 0))
        ans
        (let* ((sum carry)
               (sum (if (null? st1) sum (+ sum (car st1))))
               (next-st1 (if (null? st1) '() (cdr st1)))
               (sum (if (null? st2) sum (+ sum (car st2))))
               (next-st2 (if (null? st2) '() (cdr st2)))
               (digit (modulo sum 10))
               (new-carry (quotient sum 10))
               (node (list-node digit ans))) ; prepend new node
          (loop next-st1 next-st2 new-carry node)))))

;; Provide the contract for the function as required by LeetCode.
(provide add-two-numbers)
```

## Erlang

```erlang
%% Definition for singly-linked list.
-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec add_two_numbers(L1 :: #list_node{} | null, L2 :: #list_node{} | null) -> #list_node{} | null.
add_two_numbers(L1, L2) ->
    S1 = collect_vals(L1, []),
    S2 = collect_vals(L2, []),
    add_stack(S1, S2, 0, null).

collect_vals(null, Acc) -> Acc;
collect_vals(Node, Acc) ->
    collect_vals(Node#list_node.next, [Node#list_node.val | Acc]).

add_stack([], [], 0, Result) -> Result;
add_stack(S1, S2, Carry, Result) ->
    {V1, Rest1} = case S1 of
        [] -> {0, []};
        [H|T] -> {H, T}
    end,
    {V2, Rest2} = case S2 of
        [] -> {0, []};
        [H|T] -> {H, T}
    end,
    Sum = V1 + V2 + Carry,
    Digit = Sum rem 10,
    NewCarry = Sum div 10,
    NewNode = #list_node{val = Digit, next = Result},
    add_stack(Rest1, Rest2, NewCarry, NewNode).
```

## Elixir

```elixir
defmodule Solution do
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def add_two_numbers(l1, l2) do
    s1 = build_stack(l1, [])
    s2 = build_stack(l2, [])
    do_add(s1, s2, 0, nil)
  end

  defp build_stack(nil, acc), do: acc
  defp build_stack(%ListNode{val: v, next: nxt}, acc) do
    build_stack(nxt, [v | acc])
  end

  defp do_add([], [], 0, acc), do: acc
  defp do_add(s1, s2, carry, acc) do
    {sum1, ns1} = case s1 do
      [] -> {carry, []}
      [h | t] -> {carry + h, t}
    end

    {sum2, ns2} = case s2 do
      [] -> {sum1, []}
      [h | t] -> {sum1 + h, t}
    end

    node_val = rem(sum2, 10)
    new_carry = div(sum2, 10)

    new_node = %ListNode{val: node_val, next: acc}
    do_add(ns1, ns2, new_carry, new_node)
  end
end
```
