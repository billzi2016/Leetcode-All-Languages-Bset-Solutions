# 1019. Next Greater Node In Linked List

## Cpp

```cpp
#include <vector>
#include <stack>
using namespace std;

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
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> vals;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next)
            vals.push_back(cur->val);
        
        int n = vals.size();
        vector<int> ans(n, 0);
        stack<int> st; // store indices
        
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && vals[i] > vals[st.top()]) {
                ans[st.top()] = vals[i];
                st.pop();
            }
            st.push(i);
        }
        return ans;
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
    public int[] nextLargerNodes(ListNode head) {
        if (head == null) return new int[0];
        java.util.List<Integer> values = new java.util.ArrayList<>();
        for (ListNode node = head; node != null; node = node.next) {
            values.add(node.val);
        }
        int n = values.size();
        int[] answer = new int[n];
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>(); // store indices
        for (int i = 0; i < n; i++) {
            int cur = values.get(i);
            while (!stack.isEmpty() && cur > values.get(stack.peek())) {
                answer[stack.pop()] = cur;
            }
            stack.push(i);
        }
        return answer;
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
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # Collect values from the linked list.
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        n = len(vals)
        ans = [0] * n
        stack = []  # stores indices with decreasing values

        for i, v in enumerate(vals):
            while stack and v > vals[stack[-1]]:
                idx = stack.pop()
                ans[idx] = v
            stack.append(i)

        return ans
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def nextLargerNodes(self, head: Optional['ListNode']) -> List[int]:
        if not head:
            return []
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        ans = [0] * len(values)
        stack = []  # stores indices with decreasing values
        for i, val in enumerate(values):
            while stack and val > values[stack[-1]]:
                idx = stack.pop()
                ans[idx] = val
            stack.append(i)
        return ans
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextLargerNodes(struct ListNode* head, int* returnSize) {
    // First pass: collect values into an array
    int capacity = 1024;
    int *vals = (int *)malloc(capacity * sizeof(int));
    int n = 0;
    struct ListNode *cur = head;
    while (cur) {
        if (n == capacity) {
            capacity <<= 1;
            vals = (int *)realloc(vals, capacity * sizeof(int));
        }
        vals[n++] = cur->val;
        cur = cur->next;
    }

    // Prepare answer array initialized to 0
    int *ans = (int *)calloc(n, sizeof(int));

    // Monotonic decreasing stack storing indices
    int *stack = (int *)malloc(n * sizeof(int));
    int top = -1;

    for (int i = 0; i < n; ++i) {
        while (top >= 0 && vals[i] > vals[stack[top]]) {
            ans[stack[top]] = vals[i];
            --top;
        }
        stack[++top] = i;
    }

    free(vals);
    free(stack);

    *returnSize = n;
    return ans;
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
    public int[] NextLargerNodes(ListNode head) {
        if (head == null) return new int[0];
        
        var values = new List<int>();
        for (var node = head; node != null; node = node.next)
            values.Add(node.val);
        
        int n = values.Count;
        int[] answer = new int[n];
        var stack = new Stack<int>(); // stores indices
        
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && values[i] > values[stack.Peek()]) {
                int idx = stack.Pop();
                answer[idx] = values[i];
            }
            stack.Push(i);
        }
        
        // Remaining indices in stack already have default value 0.
        return answer;
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
 * @return {number[]}
 */
var nextLargerNodes = function(head) {
    const values = [];
    for (let node = head; node !== null; node = node.next) {
        values.push(node.val);
    }
    const n = values.length;
    const answer = new Array(n).fill(0);
    const stack = []; // store indices with decreasing values
    for (let i = 0; i < n; ++i) {
        while (stack.length && values[i] > values[stack[stack.length - 1]]) {
            const idx = stack.pop();
            answer[idx] = values[i];
        }
        stack.push(i);
    }
    return answer;
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

function nextLargerNodes(head: ListNode | null): number[] {
    const values: number[] = [];
    for (let cur = head; cur !== null; cur = cur.next) {
        values.push(cur.val);
    }

    const n = values.length;
    const answer = new Array<number>(n).fill(0);
    const stack: number[] = []; // indices with decreasing values

    for (let i = 0; i < n; i++) {
        while (stack.length && values[i] > values[stack[stack.length - 1]]) {
            const idx = stack.pop()!;
            answer[idx] = values[i];
        }
        stack.push(i);
    }

    return answer;
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
     * @return int[]
     */
    function nextLargerNodes($head) {
        // Collect values from the linked list into an array.
        $values = [];
        while ($head !== null) {
            $values[] = $head->val;
            $head = $head->next;
        }

        $n = count($values);
        $result = array_fill(0, $n, 0);
        $stack = []; // stack of indices with decreasing values

        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $values[$i] > $values[$stack[count($stack) - 1]]) {
                $idx = array_pop($stack);
                $result[$idx] = $values[$i];
            }
            $stack[] = $i;
        }

        return $result;
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
    func nextLargerNodes(_ head: ListNode?) -> [Int] {
        var values = [Int]()
        var node = head
        while let cur = node {
            values.append(cur.val)
            node = cur.next
        }
        
        let n = values.count
        if n == 0 { return [] }
        var answer = Array(repeating: 0, count: n)
        var stack = [Int]() // indices with decreasing values
        
        for i in 0..<n {
            while let last = stack.last, values[i] > values[last] {
                let idx = stack.removeLast()
                answer[idx] = values[i]
            }
            stack.append(i)
        }
        
        return answer
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
    fun nextLargerNodes(head: ListNode?): IntArray {
        val values = mutableListOf<Int>()
        var node = head
        while (node != null) {
            values.add(node.`val`)
            node = node.next
        }
        val n = values.size
        val ans = IntArray(n)
        val stack = java.util.ArrayDeque<Int>() // store indices in decreasing order of value
        for (i in 0 until n) {
            while (!stack.isEmpty() && values[i] > values[stack.peekLast()]) {
                val idx = stack.removeLast()
                ans[idx] = values[i]
            }
            stack.addLast(i)
        }
        return ans
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
  List<int> nextLargerNodes(ListNode? head) {
    if (head == null) return [];

    // Collect node values.
    final List<int> vals = [];
    for (var cur = head; cur != null; cur = cur.next) {
      vals.add(cur.val);
    }

    final int n = vals.length;
    final List<int> ans = List.filled(n, 0);
    final List<int> stack = []; // stores indices with decreasing values

    for (int i = 0; i < n; ++i) {
      while (stack.isNotEmpty && vals[i] > vals[stack.last]) {
        ans[stack.removeLast()] = vals[i];
      }
      stack.add(i);
    }

    return ans;
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
func nextLargerNodes(head *ListNode) []int {
	if head == nil {
		return []int{}
	}
	// Collect node values into a slice.
	vals := []int{}
	for cur := head; cur != nil; cur = cur.Next {
		vals = append(vals, cur.Val)
	}

	n := len(vals)
	ans := make([]int, n)
	stack := []int{} // indices of nodes with decreasing values

	for i, v := range vals {
		// Resolve previous smaller values.
		for len(stack) > 0 && v > vals[stack[len(stack)-1]] {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[idx] = v
		}
		stack = append(stack, i)
	}
	return ans
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

def next_larger_nodes(head)
  values = []
  node = head
  while node
    values << node.val
    node = node.next
  end

  n = values.size
  answer = Array.new(n, 0)
  stack = [] # store indices with decreasing values

  values.each_with_index do |val, i|
    while !stack.empty? && val > values[stack[-1]]
      idx = stack.pop
      answer[idx] = val
    end
    stack << i
  end

  answer
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
    def nextLargerNodes(head: ListNode): Array[Int] = {
        if (head == null) return Array.emptyIntArray

        val values = scala.collection.mutable.ArrayBuffer[Int]()
        var cur = head
        while (cur != null) {
            values += cur.x
            cur = cur.next
        }

        val n = values.length
        val answer = new Array[Int](n)
        val stack = scala.collection.mutable.Stack[Int]() // store indices

        for (i <- 0 until n) {
            while (stack.nonEmpty && values(i) > values(stack.top)) {
                answer(stack.pop()) = values(i)
            }
            stack.push(i)
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn next_larger_nodes(head: Option<Box<ListNode>>) -> Vec<i32> {
        // Collect node values into a vector for random access.
        let mut vals = Vec::new();
        let mut cur = &head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = &node.next;
        }

        let n = vals.len();
        let mut answer = vec![0; n];
        let mut stack: Vec<usize> = Vec::new(); // indices with decreasing values

        for i in 0..n {
            while let Some(&last) = stack.last() {
                if vals[i] > vals[last] {
                    answer[last] = vals[i];
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        answer
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
;; (struct list-node
;;   (val next) #:mutable #:transparent)

(define/contract (next-larger-nodes head)
  (-> (or/c list-node? #f) (listof exact-integer?))
  (if (not head)
      '()
      (let* ((vals
              (let loop ((node head) (acc '()))
                (if node
                    (loop (list-node-next node)
                          (cons (list-node-val node) acc))
                    (reverse acc))))
             (vec (list->vector vals))
             (n   (vector-length vec))
             (ans (make-vector n 0)))
        (letrec ((pop-while
                  (lambda (cur s)
                    (if (and (pair? s)
                             (> cur (vector-ref vec (car s))))
                        (begin
                          (vector-set! ans (car s) cur)
                          (pop-while cur (cdr s)))
                        s)))
                 (iter
                  (lambda (i stk)
                    (when (< i n)
                      (let* ((cur (vector-ref vec i))
                             (new-stk (pop-while cur stk)))
                        (iter (+ i 1) (cons i new-stk)))))))
          (iter 0 '())
          (vector->list ans)))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec next_larger_nodes(Head :: #list_node{} | null) -> [integer()].
next_larger_nodes(Head) ->
    ValuesRev = collect_vals(Head, []),
    Values = lists:reverse(ValuesRev),
    N = length(Values),
    Answer0 = array:from_list(lists:duplicate(N, 0)),
    {Answer, _Stack} = process(Values, 0, Answer0, []),
    array:to_list(Answer).

collect_vals(null, Acc) -> Acc;
collect_vals(#list_node{val = V, next = Next}, Acc) ->
    collect_vals(Next, [V | Acc]).

process([], _Idx, AnswerArr, Stack) ->
    {AnswerArr, Stack};
process([Val | Rest], Idx, AnswerArr, Stack) ->
    {Ans1, Stack1} = pop_greater(Val, AnswerArr, Stack),
    process(Rest, Idx + 1, Ans1, [{Idx, Val} | Stack1]).

pop_greater(_Val, AnswerArr, []) -> {AnswerArr, []};
pop_greater(Val, AnswerArr, [{TopIdx, TopVal} = _Top | Rest]) when Val > TopVal ->
    UpdatedAns = array:set(TopIdx, Val, AnswerArr),
    pop_greater(Val, UpdatedAns, Rest);
pop_greater(_Val, AnswerArr, Stack) -> {AnswerArr, Stack}.
```

## Elixir

```elixir
defmodule Solution do
  @spec next_larger_nodes(head :: ListNode.t | nil) :: [integer]
  def next_larger_nodes(head) do
    vals = collect_vals(head, [])
    values = Enum.reverse(vals)
    len = length(values)

    if len == 0 do
      []
    else
      tuple = List.to_tuple(values)
      answer_arr = :array.new(len, default: 0)
      final_arr = process(0, len, tuple, [], answer_arr)
      array_to_list(final_arr, len)
    end
  end

  defp collect_vals(nil, acc), do: acc
  defp collect_vals(%{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  defp process(i, len, _tuple, stack, answer) when i == len, do: answer

  defp process(i, len, tuple, stack, answer) do
    cur = elem(tuple, i)
    {new_stack, new_answer} = pop_and_update(stack, answer, cur, tuple)
    process(i + 1, len, tuple, [i | new_stack], new_answer)
  end

  defp pop_and_update([], answer, _cur, _tuple), do: {[], answer}
  defp pop_and_update([top | rest] = stack, answer, cur, tuple) do
    top_val = elem(tuple, top)

    if cur > top_val do
      updated_answer = :array.set(top, cur, answer)
      pop_and_update(rest, updated_answer, cur, tuple)
    else
      {stack, answer}
    end
  end

  defp array_to_list(arr, len) do
    Enum.map(0..len - 1, fn i -> :array.get(i, arr) end)
  end
end
```
