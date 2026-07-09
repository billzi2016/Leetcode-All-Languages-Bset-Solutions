# 0817. Linked List Components

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
    int numComponents(ListNode* head, std::vector<int>& nums) {
        std::unordered_set<int> s(nums.begin(), nums.end());
        int components = 0;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next) {
            if (s.count(cur->val) && (cur->next == nullptr || !s.count(cur->next->val))) {
                ++components;
            }
        }
        return components;
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
    public int numComponents(ListNode head, int[] nums) {
        java.util.Set<Integer> set = new java.util.HashSet<>();
        for (int v : nums) set.add(v);
        int components = 0;
        ListNode cur = head;
        while (cur != null) {
            if (set.contains(cur.val) && (cur.next == null || !set.contains(cur.next.val))) {
                components++;
            }
            cur = cur.next;
        }
        return components;
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
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        target = set(nums)
        count = 0
        node = head
        while node:
            if node.val in target and (node.next is None or node.next.val not in target):
                count += 1
            node = node.next
        return count
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: 'Optional[ListNode]', nums: List[int]) -> int:
        target = set(nums)
        count = 0
        node = head
        while node:
            if node.val in target and (node.next is None or node.next.val not in target):
                count += 1
            node = node.next
        return count
```

## C

```c
#include <stdbool.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int numComponents(struct ListNode* head, int* nums, int numsSize) {
    bool present[10001] = {false};
    for (int i = 0; i < numsSize; ++i) {
        present[nums[i]] = true;
    }
    
    int count = 0;
    struct ListNode* cur = head;
    while (cur) {
        if (present[cur->val]) {
            if (!cur->next || !present[cur->next->val]) {
                ++count;
            }
        }
        cur = cur->next;
    }
    return count;
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
    public int NumComponents(ListNode head, int[] nums) {
        var set = new HashSet<int>(nums);
        int components = 0;
        var node = head;
        while (node != null) {
            if (set.Contains(node.val) && (node.next == null || !set.Contains(node.next.val))) {
                components++;
            }
            node = node.next;
        }
        return components;
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
 * @param {number[]} nums
 * @return {number}
 */
var numComponents = function(head, nums) {
    const set = new Set(nums);
    let count = 0;
    for (let node = head; node !== null; node = node.next) {
        if (set.has(node.val) && (!node.next || !set.has(node.next.val))) {
            count++;
        }
    }
    return count;
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

function numComponents(head: ListNode | null, nums: number[]): number {
    const set = new Set(nums);
    let count = 0;
    let node = head;
    while (node) {
        if (set.has(node.val) && (!node.next || !set.has(node.next.val))) {
            count++;
        }
        node = node.next;
    }
    return count;
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
     * @param Integer[] $nums
     * @return Integer
     */
    function numComponents($head, $nums) {
        // Create a hash set for quick lookup of nums values
        $set = array_flip($nums);
        $count = 0;
        $curr = $head;
        while ($curr !== null) {
            if (isset($set[$curr->val])) {
                // If next node is not in the set or does not exist, this ends a component
                if ($curr->next === null || !isset($set[$curr->next->val])) {
                    $count++;
                }
            }
            $curr = $curr->next;
        }
        return $count;
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
    func numComponents(_ head: ListNode?, _ nums: [Int]) -> Int {
        let set = Set(nums)
        var count = 0
        var node = head
        while let cur = node {
            if set.contains(cur.val) && (cur.next == nil || !set.contains(cur.next!.val)) {
                count += 1
            }
            node = cur.next
        }
        return count
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
    fun numComponents(head: ListNode?, nums: IntArray): Int {
        if (head == null) return 0
        val set = HashSet<Int>()
        for (num in nums) set.add(num)

        var count = 0
        var node = head
        while (node != null) {
            if (set.contains(node.`val`) && (node.next == null || !set.contains(node.next!!.`val`))) {
                count++
            }
            node = node.next
        }
        return count
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
  int numComponents(ListNode? head, List<int> nums) {
    final Set<int> set = nums.toSet();
    int count = 0;
    var node = head;
    while (node != null) {
      if (set.contains(node.val) &&
          (node.next == null || !set.contains(node.next!.val))) {
        count++;
      }
      node = node.next;
    }
    return count;
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
func numComponents(head *ListNode, nums []int) int {
    set := make(map[int]bool, len(nums))
    for _, v := range nums {
        set[v] = true
    }

    count := 0
    for cur := head; cur != nil; cur = cur.Next {
        if set[cur.Val] && (cur.Next == nil || !set[cur.Next.Val]) {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def num_components(head, nums)
  in_set = {}
  nums.each { |v| in_set[v] = true }
  count = 0
  cur = head
  while cur
    if in_set[cur.val] && (cur.next.nil? || !in_set[cur.next.val])
      count += 1
    end
    cur = cur.next
  end
  count
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
    def numComponents(head: ListNode, nums: Array[Int]): Int = {
        val set = nums.toSet
        var count = 0
        var cur = head
        while (cur != null) {
            if (set.contains(cur.x) && (cur.next == null || !set.contains(cur.next.x))) {
                count += 1
            }
            cur = cur.next
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashSet;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

impl Solution {
    pub fn num_components(head: Option<Box<ListNode>>, nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut count = 0;
        let mut cur = &head;
        while let Some(node) = cur {
            if set.contains(&node.val) {
                let next_in_set = node
                    .next
                    .as_ref()
                    .map_or(false, |next_node| set.contains(&next_node.val));
                if !next_in_set {
                    count += 1;
                }
            }
            cur = &node.next;
        }
        count as i32
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

(define/contract (num-components head nums)
  (-> (or/c list-node? #f) (listof exact-integer?) exact-integer?)
  (let ([s (make-hash)])
    (for ([x nums]) (hash-set! s x #t))
    (let loop ((node head) (cnt 0))
      (if (not node)
          cnt
          (let* ([val (list-node-val node)]
                 [next (list-node-next node)]
                 [in? (hash-has-key? s val)])
            (if in?
                (if (or (not next)
                        (not (hash-has-key? s (list-node-val next))))
                    (loop next (+ cnt 1))
                    (loop next cnt))
                (loop next cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([num_components/2]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec num_components(Head :: #list_node{} | null, Nums :: [integer()]) -> integer().
num_components(Head, Nums) ->
    Set = lists:foldl(fun(X, Acc) -> maps:put(X, true, Acc) end, #{}, Nums),
    count(Head, Set, 0).

count(null, _Set, Acc) -> Acc;
count(Node, Set, Acc) ->
    Val = Node#list_node.val,
    Next = Node#list_node.next,
    case maps:is_key(Val, Set) of
        true ->
            End =
                case Next of
                    null -> true;
                    #list_node{val = NextVal} ->
                        not maps:is_key(NextVal, Set)
                end,
            NewAcc = if End -> Acc + 1; true -> Acc end,
            count(Next, Set, NewAcc);
        false ->
            count(Next, Set, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_components(head :: ListNode.t() | nil, nums :: [integer]) :: integer
  def num_components(head, nums) do
    set = MapSet.new(nums)
    count_components(head, set, 0)
  end

  defp count_components(nil, _set, cnt), do: cnt

  defp count_components(%ListNode{val: v, next: nxt} = node, set, cnt) do
    if MapSet.member?(set, v) and (nxt == nil or not MapSet.member?(set, nxt.val)) do
      count_components(nxt, set, cnt + 1)
    else
      count_components(nxt, set, cnt)
    end
  end
end
```
