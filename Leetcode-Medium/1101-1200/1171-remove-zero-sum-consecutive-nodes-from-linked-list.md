# 1171. Remove Zero Sum Consecutive Nodes from Linked List

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
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;
        unordered_map<int, ListNode*> prefixMap;
        int sum = 0;
        // First pass: record the last node for each prefix sum
        for (ListNode* cur = &dummy; cur != nullptr; cur = cur->next) {
            sum += cur->val;
            prefixMap[sum] = cur;
        }
        // Second pass: skip zero-sum sequences
        sum = 0;
        for (ListNode* cur = &dummy; cur != nullptr; cur = cur->next) {
            sum += cur->val;
            ListNode* last = prefixMap[sum];
            if (cur->next != last->next) {
                cur->next = last->next;
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
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        java.util.Map<Integer, ListNode> prefixMap = new java.util.HashMap<>();
        int sum = 0;
        for (ListNode cur = dummy; cur != null; cur = cur.next) {
            sum += cur.val;
            prefixMap.put(sum, cur);
        }
        sum = 0;
        for (ListNode cur = dummy; cur != null; cur = cur.next) {
            sum += cur.val;
            ListNode last = prefixMap.get(sum);
            if (last != cur) {
                cur.next = last.next;
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
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        # First pass: record the last occurrence of each prefix sum
        prefix_sum = 0
        sum_to_node = {0: dummy}
        cur = dummy
        while cur:
            prefix_sum += cur.val
            sum_to_node[prefix_sum] = cur
            cur = cur.next

        # Second pass: skip zero-sum sequences using the recorded nodes
        prefix_sum = 0
        cur = dummy
        while cur:
            prefix_sum += cur.val
            # Jump to the node after the last occurrence of this sum
            cur.next = sum_to_node[prefix_sum].next
            cur = cur.next

        return dummy.next
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
    def removeZeroSumSublists(self, head: Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0)
        dummy.next = head

        # First pass: record the last occurrence of each prefix sum.
        prefix_sum_to_node = {}
        cur = dummy
        prefix = 0
        while cur:
            prefix += cur.val
            prefix_sum_to_node[prefix] = cur
            cur = cur.next

        # Second pass: skip nodes that are part of zero-sum sequences.
        cur = dummy
        prefix = 0
        while cur:
            prefix += cur.val
            # The node stored for this prefix sum is the farthest node with same sum.
            # Skip all intermediate nodes.
            cur.next = prefix_sum_to_node[prefix].next
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
#include <stdlib.h>

#define HASH_SIZE 2003

struct MapEntry {
    int key;
    struct ListNode *val;
    struct MapEntry *next;
};

static struct MapEntry *hashTable[HASH_SIZE];

static int hashFunc(int key) {
    int h = key % HASH_SIZE;
    if (h < 0) h += HASH_SIZE;
    return h;
}

static void hashmapClear(void) {
    for (int i = 0; i < HASH_SIZE; ++i) {
        struct MapEntry *e = hashTable[i];
        while (e) {
            struct MapEntry *tmp = e;
            e = e->next;
            free(tmp);
        }
        hashTable[i] = NULL;
    }
}

static void hashmapPut(int key, struct ListNode *val) {
    int idx = hashFunc(key);
    struct MapEntry *e = hashTable[idx];
    while (e) {
        if (e->key == key) {
            e->val = val;
            return;
        }
        e = e->next;
    }
    struct MapEntry *newE = (struct MapEntry *)malloc(sizeof(struct MapEntry));
    newE->key = key;
    newE->val = val;
    newE->next = hashTable[idx];
    hashTable[idx] = newE;
}

static struct ListNode *hashmapGet(int key) {
    int idx = hashFunc(key);
    struct MapEntry *e = hashTable[idx];
    while (e) {
        if (e->key == key) return e->val;
        e = e->next;
    }
    return NULL;
}

struct ListNode* removeZeroSumSublists(struct ListNode* head) {
    hashmapClear();  // ensure table is empty for each call
    
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;
    
    int prefix = 0;
    struct ListNode *cur = &dummy;
    while (cur) {
        prefix += cur->val;
        hashmapPut(prefix, cur);
        cur = cur->next;
    }
    
    prefix = 0;
    cur = &dummy;
    while (cur) {
        prefix += cur->val;
        struct ListNode *node = hashmapGet(prefix);
        if (node && node->next != cur->next) {
            cur->next = node->next;
        }
        cur = cur->next;
    }
    
    // optional cleanup
    hashmapClear();
    
    return dummy.next;
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
    public ListNode RemoveZeroSumSublists(ListNode head) {
        var dummy = new ListNode(0);
        dummy.next = head;
        var sumToNode = new Dictionary<int, ListNode>();
        int sum = 0;
        for (var node = dummy; node != null; node = node.next) {
            sum += node.val;
            sumToNode[sum] = node; // keep the last occurrence of this prefix sum
        }
        sum = 0;
        for (var node = dummy; node != null; node = node.next) {
            sum += node.val;
            var lastNode = sumToNode[sum];
            if (node.next != lastNode.next) {
                node.next = lastNode.next; // skip zero-sum subsequence
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
var removeZeroSumSublists = function(head) {
    const dummy = new ListNode(0);
    dummy.next = head;
    
    // First pass: record the last occurrence of each prefix sum.
    let sum = 0;
    const sumToNode = new Map();
    sumToNode.set(0, dummy);
    for (let node = dummy; node !== null; node = node.next) {
        sum += node.val;
        sumToNode.set(sum, node);
    }
    
    // Second pass: skip zero-sum sequences.
    sum = 0;
    for (let node = dummy; node !== null; node = node.next) {
        sum += node.val;
        const lastNode = sumToNode.get(sum);
        if (node.next !== lastNode.next) {
            node.next = lastNode.next;
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

function removeZeroSumSublists(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    const sumToNode = new Map<number, ListNode>();
    let sum = 0;
    for (let cur: ListNode | null = dummy; cur !== null; cur = cur.next) {
        sum += cur.val;
        sumToNode.set(sum, cur);
    }
    sum = 0;
    for (let cur: ListNode | null = dummy; cur !== null; cur = cur.next) {
        sum += cur.val;
        const node = sumToNode.get(sum)!;
        cur.next = node.next;
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
    function removeZeroSumSublists($head) {
        // Dummy node to handle deletions at the head
        $dummy = new ListNode(0);
        $dummy->next = $head;

        // First pass: record the last occurrence of each prefix sum
        $prefixSum = 0;
        $node = $dummy;
        $sumToNode = [];
        while ($node !== null) {
            $prefixSum += $node->val;
            $sumToNode[$prefixSum] = $node; // store latest node with this sum
            $node = $node->next;
        }

        // Second pass: skip zero-sum sequences using the recorded nodes
        $prefixSum = 0;
        $node = $dummy;
        while ($node !== null) {
            $prefixSum += $node->val;
            $lastNode = $sumToNode[$prefixSum];
            if ($lastNode !== $node) {
                // Bypass all nodes between current node and lastNode
                $node->next = $lastNode->next;
            }
            $node = $node->next;
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
    func removeZeroSumSublists(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        
        var prefix = 0
        var sumToNode = [Int: ListNode]()
        var node: ListNode? = dummy
        
        // First pass: record the last occurrence of each prefix sum
        while let cur = node {
            prefix += cur.val
            sumToNode[prefix] = cur
            node = cur.next
        }
        
        // Second pass: skip zero-sum sequences
        prefix = 0
        node = dummy
        while let cur = node {
            prefix += cur.val
            if let last = sumToNode[prefix] {
                cur.next = last.next
            }
            node = cur.next
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
    fun removeZeroSumSublists(head: ListNode?): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        val prefixMap = HashMap<Int, ListNode>()
        var sum = 0
        var cur: ListNode? = dummy
        while (cur != null) {
            sum += cur.`val`
            prefixMap[sum] = cur
            cur = cur.next
        }
        sum = 0
        cur = dummy
        while (cur != null) {
            sum += cur.`val`
            val node = prefixMap[sum]
            if (node != null) {
                cur.next = node.next
            }
            cur = cur.next
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
  ListNode? removeZeroSumSublists(ListNode? head) {
    var dummy = ListNode(0);
    dummy.next = head;

    // First pass: record the last node for each prefix sum.
    var prefixMap = <int, ListNode>{};
    int sum = 0;
    for (var node = dummy; node != null; node = node.next) {
      sum += node.val;
      prefixMap[sum] = node;
    }

    // Second pass: skip zero-sum sequences.
    sum = 0;
    for (var node = dummy; node != null; node = node.next) {
      sum += node.val;
      var lastNode = prefixMap[sum];
      if (lastNode != null && !identical(lastNode, node)) {
        node.next = lastNode.next;
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
 *     Val  int
 *     Next *ListNode
 * }
 */
func removeZeroSumSublists(head *ListNode) *ListNode {
    dummy := &ListNode{Val: 0, Next: head}
    prefixSumToNode := make(map[int]*ListNode)

    sum := 0
    for cur := dummy; cur != nil; cur = cur.Next {
        sum += cur.Val
        prefixSumToNode[sum] = cur
    }

    sum = 0
    for cur := dummy; cur != nil; cur = cur.Next {
        sum += cur.Val
        if node, ok := prefixSumToNode[sum]; ok {
            cur.Next = node.Next
        }
    }

    return dummy.Next
}
```

## Ruby

```ruby
def remove_zero_sum_sublists(head)
  dummy = ListNode.new(0)
  dummy.next = head
  sum = 0
  prefix_map = {}

  node = dummy
  while node
    sum += node.val
    prefix_map[sum] = node
    node = node.next
  end

  sum = 0
  node = dummy
  while node
    sum += node.val
    node.next = prefix_map[sum].next if prefix_map[sum]
    node = node.next
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
    def removeZeroSumSublists(head: ListNode): ListNode = {
        val dummy = new ListNode(0)
        dummy.next = head

        import scala.collection.mutable.HashMap
        val prefixMap = HashMap[Int, ListNode]()

        var sum = 0
        var cur: ListNode = dummy
        while (cur != null) {
            sum += cur.x
            prefixMap(sum) = cur
            cur = cur.next
        }

        sum = 0
        cur = dummy
        while (cur != null) {
            sum += cur.x
            val node = prefixMap(sum)
            // skip all nodes between cur and node
            cur.next = node.next
            cur = cur.next
        }

        dummy.next
    }
}
```

## Rust

```rust
use std::collections::HashMap;

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

pub struct Solution;

impl Solution {
    pub fn remove_zero_sum_sublists(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Dummy node to simplify edge cases
        let mut dummy = Box::new(ListNode { val: 0, next: head });
        let mut prefix_sum: i64 = 0;
        let mut map: HashMap<i64, *mut ListNode> = HashMap::new();
        // Store sum 0 at dummy
        map.insert(0, &mut *dummy as *mut _);

        // First pass: record the last occurrence of each prefix sum
        unsafe {
            let mut cur: *mut ListNode = &mut *dummy;
            while let Some(ref mut nxt) = (*cur).next {
                prefix_sum += nxt.val as i64;
                map.insert(prefix_sum, &mut **nxt as *mut _);
                cur = &mut **nxt as *mut _;
            }
        }

        // Second pass: skip zero-sum sequences using the recorded nodes
        let mut sum2: i64 = 0;
        unsafe {
            let mut cur: *mut ListNode = &mut *dummy;
            while let Some(ref mut nxt) = (*cur).next {
                sum2 += nxt.val as i64;
                if let Some(&last_node) = map.get(&sum2) {
                    // Skip nodes between cur and last_node (inclusive of those after cur up to last_node)
                    (*cur).next = (*last_node).next.take();
                }
                match (*cur).next.as_deref_mut() {
                    Some(node_ref) => cur = node_ref as *mut ListNode,
                    None => break,
                }
            }
        }

        dummy.next
    }
}
```

## Racket

```racket
#|
; Definition for singly-linked list:
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (remove-zero-sum-sublists head)
  (-> (or/c list-node? #f) (or/c list-node? #f))
  (let* ((dummy (make-list-node 0))
         (_ (set-list-node-next! dummy head)))
    ;; First pass: record the last occurrence of each prefix sum
    (define mp (make-hash))
    (hash-set! mp 0 dummy)
    (let loop ((cur head) (s 0))
      (when cur
        (set! s (+ s (list-node-val cur)))
        (hash-set! mp s cur)
        (loop (list-node-next cur) s)))
    ;; Second pass: skip zero-sum sequences using the map
    (let loop2 ((cur dummy) (s 0))
      (when cur
        (set! s (+ s (list-node-val cur)))
        (define node (hash-ref mp s))
        (set-list-node-next! cur (list-node-next node))
        (loop2 (list-node-next cur) s)))
    (list-node-next dummy)))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec remove_zero_sum_sublists(Head :: #list_node{} | null) -> #list_node{} | null.
remove_zero_sum_sublists(Head) ->
    Dummy = #list_node{val = 0, next = Head},
    Map = first_pass(Dummy, 0, #{ }),
    rebuild(Dummy#list_node.next, 0, Map).

first_pass(Node, Sum, Map) when Node =/= null ->
    NewSum = Sum + Node#list_node.val,
    UpdatedMap = maps:put(NewSum, Node, Map),
    case Node#list_node.next of
        null -> UpdatedMap;
        Next -> first_pass(Next, NewSum, UpdatedMap)
    end;
first_pass(null, _Sum, Map) ->
    Map.

rebuild(Node, Sum, Map) when Node =/= null ->
    NewSum = Sum + Node#list_node.val,
    LastNode = maps:get(NewSum, Map),
    NextNode = LastNode#list_node.next,
    #list_node{
        val = Node#list_node.val,
        next = rebuild(NextNode, NewSum, Map)
    };
rebuild(null, _Sum, _Map) ->
    null.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_zero_sum_sublists(head :: ListNode.t() | nil) :: ListNode.t() | nil
  def remove_zero_sum_sublists(head) do
    vals = collect_vals(head, [])
    cleaned = clean(vals)
    build_list(cleaned)
  end

  # Convert linked list to a list of values (preserving order)
  defp collect_vals(nil, acc), do: Enum.reverse(acc)

  defp collect_vals(%ListNode{val: v, next: nxt}, acc) do
    collect_vals(nxt, [v | acc])
  end

  # Repeatedly remove any zero‑sum consecutive subarray until none remain
  defp clean(vals) do
    remover = fn remover, list ->
      case remove_once(list) do
        {true, new_list} -> remover.(remover, new_list)
        {false, _} -> list
      end
    end

    remover.(remover, vals)
  end

  # Remove the first zero‑sum subarray found (if any)
  defp remove_once(list) do
    {found, _, result} =
      Enum.reduce_while(Enum.with_index(list), {%{0 => -1}, 0, false, list}, fn
        {value, idx},
        {prefix_map, sum, _found, orig_list} = acc ->
          new_sum = sum + value

          if Map.has_key?(prefix_map, new_sum) do
            start_idx = prefix_map[new_sum] + 1
            end_idx = idx

            left = Enum.slice(orig_list, 0, start_idx)
            right = Enum.slice(orig_list, end_idx + 1, length(orig_list) - end_idx - 1)

            {:halt, {nil, nil, true, left ++ right}}
          else
            {:cont,
             {Map.put(prefix_map, new_sum, idx), new_sum, false, orig_list}}
          end
      end)

    case found do
      true -> {true, result}
      false -> {false, list}
    end
  end

  # Build a linked list from a list of values
  defp build_list([]), do: nil

  defp build_list(vals) do
    Enum.reduce(Enum.reverse(vals), nil, fn v, acc ->
      %ListNode{val: v, next: acc}
    end)
  end
end
```
