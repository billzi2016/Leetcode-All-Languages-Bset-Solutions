# 0725. Split Linked List in Parts

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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        // Count total nodes
        int n = 0;
        for (ListNode* cur = head; cur != nullptr; cur = cur->next) ++n;
        
        int base = n / k;          // minimum size of each part
        int extra = n % k;         // first 'extra' parts have one more node
        
        vector<ListNode*> ans(k, nullptr);
        ListNode* curr = head;
        for (int i = 0; i < k; ++i) {
            ans[i] = curr;
            int partSize = base + (i < extra ? 1 : 0);
            ListNode* prev = nullptr;
            for (int j = 0; j < partSize && curr != nullptr; ++j) {
                prev = curr;
                curr = curr->next;
            }
            if (prev) prev->next = nullptr;
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
    public ListNode[] splitListToParts(ListNode head, int k) {
        // First pass: compute total length of the list
        int length = 0;
        ListNode node = head;
        while (node != null) {
            length++;
            node = node.next;
        }
        
        int baseSize = length / k;          // minimum nodes per part
        int extra = length % k;             // first 'extra' parts get one more node
        
        ListNode[] result = new ListNode[k];
        ListNode current = head;
        
        for (int i = 0; i < k; i++) {
            result[i] = current;
            int partSize = baseSize + (i < extra ? 1 : 0);
            
            // Advance to the last node of this part
            for (int j = 0; j < partSize - 1 && current != null; j++) {
                current = current.next;
            }
            
            // Cut the list if needed and move to next part's head
            if (current != null) {
                ListNode nextPart = current.next;
                current.next = null;
                current = nextPart;
            }
        }
        
        return result;
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
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        # Count total nodes
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        base, extra = divmod(n, k)
        result = [None] * k
        cur = head

        for i in range(k):
            result[i] = cur
            part_len = base + (1 if i < extra else 0)
            # advance to the last node of this part
            for _ in range(part_len - 1):
                if cur:
                    cur = cur.next
            # cut the list if needed
            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt

        return result
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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Compute total length of the list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        base, extra = divmod(n, k)
        result: List[Optional[ListNode]] = [None] * k
        cur = head
        
        for i in range(k):
            result[i] = cur
            part_len = base + (1 if i < extra else 0)
            # Advance to the last node of this part
            for _ in range(part_len - 1):
                if cur:
                    cur = cur.next
            # Cut the list if needed
            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt
        
        return result
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
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize) {
    // Count total nodes
    int n = 0;
    struct ListNode* cur = head;
    while (cur) {
        ++n;
        cur = cur->next;
    }
    
    int base = n / k;          // minimum size of each part
    int extra = n % k;         // first 'extra' parts have one more node
    
    struct ListNode** result = malloc(sizeof(struct ListNode*) * k);
    cur = head;
    
    for (int i = 0; i < k; ++i) {
        result[i] = cur;
        int partSize = base + (i < extra ? 1 : 0);
        struct ListNode* prev = NULL;
        for (int j = 0; j < partSize; ++j) {
            if (!cur) break;
            prev = cur;
            cur = cur->next;
        }
        if (prev) {
            prev->next = NULL;
        }
    }
    
    *returnSize = k;
    return result;
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
    public ListNode[] SplitListToParts(ListNode head, int k) {
        // Count total nodes in the list
        int total = 0;
        var node = head;
        while (node != null) {
            total++;
            node = node.next;
        }

        int baseSize = total / k;          // Minimum size of each part
        int extra = total % k;             // First 'extra' parts have one more node

        ListNode[] result = new ListNode[k];
        var current = head;

        for (int i = 0; i < k; i++) {
            result[i] = current;
            int partSize = baseSize + (i < extra ? 1 : 0);

            // Move to the last node of this part
            for (int j = 0; j < partSize - 1 && current != null; j++) {
                current = current.next;
            }

            // Cut the list if needed and move to next part's head
            if (current != null) {
                var nextPart = current.next;
                current.next = null;
                current = nextPart;
            }
        }

        return result;
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
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    // Count total nodes
    let length = 0;
    let node = head;
    while (node) {
        length++;
        node = node.next;
    }
    
    const baseSize = Math.floor(length / k);
    let extra = length % k; // first 'extra' parts get an extra node
    
    const result = new Array(k).fill(null);
    let current = head;
    
    for (let i = 0; i < k; i++) {
        result[i] = current;
        let partSize = baseSize + (extra > 0 ? 1 : 0);
        if (extra > 0) extra--;
        
        // Move to the last node of this part
        for (let j = 0; j < partSize - 1 && current; j++) {
            current = current.next;
        }
        
        // Cut the list if needed
        if (current) {
            const nextPart = current.next;
            current.next = null;
            current = nextPart;
        }
    }
    
    return result;
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

function splitListToParts(head: ListNode | null, k: number): Array<ListNode | null> {
    // Count total nodes
    let length = 0;
    let node = head;
    while (node) {
        length++;
        node = node.next;
    }

    const baseSize = Math.floor(length / k);
    let extra = length % k; // first 'extra' parts get an additional node

    const result: Array<ListNode | null> = new Array(k).fill(null);
    let current = head;

    for (let i = 0; i < k; i++) {
        result[i] = current;
        let partSize = baseSize + (extra > 0 ? 1 : 0);
        if (extra > 0) extra--;

        // advance to the last node of this part
        for (let j = 0; j < partSize - 1 && current; j++) {
            current = current!.next;
        }

        // cut the list if needed
        if (current) {
            const nextPart = current.next;
            current.next = null;
            current = nextPart;
        }
    }

    return result;
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
     * @param Integer $k
     * @return ListNode[]
     */
    function splitListToParts($head, $k) {
        // Count total nodes
        $count = 0;
        $node = $head;
        while ($node !== null) {
            $count++;
            $node = $node->next;
        }

        $baseSize = intdiv($count, $k);
        $extra = $count % $k; // first $extra parts get one extra node

        $result = array_fill(0, $k, null);
        $current = $head;

        for ($i = 0; $i < $k; $i++) {
            $result[$i] = $current;
            $partSize = $baseSize + ($extra > 0 ? 1 : 0);
            if ($extra > 0) {
                $extra--;
            }

            $prev = null;
            for ($j = 0; $j < $partSize && $current !== null; $j++) {
                $prev = $current;
                $current = $current->next;
            }
            if ($prev !== null) {
                // cut the list
                $prev->next = null;
            }
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
    func splitListToParts(_ head: ListNode?, _ k: Int) -> [ListNode?] {
        var length = 0
        var node = head
        while node != nil {
            length += 1
            node = node!.next
        }
        
        let baseSize = length / k
        var extra = length % k
        
        var result = [ListNode?](repeating: nil, count: k)
        var current = head
        
        for i in 0..<k {
            let partHead = current
            var partSize = baseSize + (extra > 0 ? 1 : 0)
            if extra > 0 { extra -= 1 }
            
            var prev: ListNode? = nil
            for _ in 0..<partSize {
                prev = current
                current = current?.next
            }
            // Cut the list to end this part
            prev?.next = nil
            
            result[i] = partHead
        }
        
        return result
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
    fun splitListToParts(head: ListNode?, k: Int): Array<ListNode?> {
        // Count total nodes
        var n = 0
        var cur = head
        while (cur != null) {
            n++
            cur = cur.next
        }

        val baseSize = n / k
        var extra = n % k

        val result = arrayOfNulls<ListNode>(k)
        var current = head

        for (i in 0 until k) {
            result[i] = current
            var partSize = baseSize + if (extra > 0) 1 else 0
            if (extra > 0) extra--

            var prev: ListNode? = null
            repeat(partSize) {
                prev = current
                current = current?.next
            }
            // Cut the list if needed
            prev?.next = null
        }

        return result
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
  List<ListNode?> splitListToParts(ListNode? head, int k) {
    // Count total nodes
    int n = 0;
    for (var cur = head; cur != null; cur = cur.next) {
      n++;
    }

    int baseSize = n ~/ k;
    int extra = n % k;

    List<ListNode?> ans = List.filled(k, null);
    ListNode? current = head;

    for (int i = 0; i < k; i++) {
      int partSize = baseSize + (i < extra ? 1 : 0);
      if (partSize == 0) {
        ans[i] = null;
        continue;
      }

      ans[i] = current;
      // Move to the last node of this part
      for (int j = 1; j < partSize; j++) {
        current = current!.next;
      }
      // Cut the list
      var nextPartHead = current!.next;
      current.next = null;
      current = nextPartHead;
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
func splitListToParts(head *ListNode, k int) []*ListNode {
    // Count total nodes
    n := 0
    for cur := head; cur != nil; cur = cur.Next {
        n++
    }

    baseSize := n / k
    extra := n % k

    result := make([]*ListNode, k)
    cur := head

    for i := 0; i < k; i++ {
        result[i] = cur
        partSize := baseSize
        if extra > 0 {
            partSize++
            extra--
        }

        var prev *ListNode
        for j := 0; j < partSize && cur != nil; j++ {
            prev = cur
            cur = cur.Next
        }
        if prev != nil {
            prev.Next = nil
        }
    }

    return result
}
```

## Ruby

```ruby
def split_list_to_parts(head, k)
  # Count total nodes
  n = 0
  node = head
  while node
    n += 1
    node = node.next
  end

  base = n / k
  extra = n % k
  parts = Array.new(k)

  cur = head
  (0...k).each do |i|
    parts[i] = cur
    size = base + (extra > 0 ? 1 : 0)
    extra -= 1 if extra > 0

    prev = nil
    size.times do
      break unless cur
      prev = cur
      cur = cur.next
    end
    prev.next = nil if prev
  end

  parts
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
    def splitListToParts(head: ListNode, k: Int): Array[ListNode] = {
        // Compute total length of the list
        var len = 0
        var node = head
        while (node != null) {
            len += 1
            node = node.next
        }

        val baseSize = len / k
        var extra = len % k

        val result = new Array[ListNode](k)
        var cur = head

        for (i <- 0 until k) {
            val partHead = cur
            var partSize = baseSize + (if (extra > 0) 1 else 0)
            if (extra > 0) extra -= 1

            // Advance to the last node of this part
            var j = 0
            while (j < partSize - 1 && cur != null) {
                cur = cur.next
                j += 1
            }

            // Cut the list if needed
            if (cur != null) {
                val nextPart = cur.next
                cur.next = null
                cur = nextPart
            }

            result(i) = partHead
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn split_list_to_parts(head: Option<Box<ListNode>>, k: i32) -> Vec<Option<Box<ListNode>>> {
        // Compute total length of the list
        let mut len = 0usize;
        let mut ptr = &head;
        while let Some(node) = ptr {
            len += 1;
            ptr = &node.next;
        }

        let k_usize = k as usize;
        let base = len / k_usize;
        let extra = len % k_usize;

        let mut result: Vec<Option<Box<ListNode>>> = Vec::with_capacity(k_usize);
        let mut current = head;

        for i in 0..k_usize {
            let size = base + if i < extra { 1 } else { 0 };
            if size == 0 {
                result.push(None);
                continue;
            }

            // Take the head of this part
            let mut part_head = std::mem::take(&mut current);
            // Find the tail (the node after which we will cut)
            let mut tail = &mut part_head;
            for _ in 0..size - 1 {
                if let Some(node) = tail {
                    tail = &mut node.next;
                }
            }
            // Detach the rest of the list
            current = std::mem::take(tail);
            result.push(part_head);
        }

        result
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
#|
(struct list-node
  (val next) #:mutable #:transparent)

(define (make-list-node [val 0])
  (list-node val #f))
|#

(define/contract (split-list-to-parts head k)
  (-> (or/c list-node? #f) exact-integer? (listof (or/c list-node? #f)))
  (let* ((len
          (let loop ((node head) (cnt 0))
            (if node
                (loop (list-node-next node) (+ cnt 1))
                cnt)))
         (base (quotient len k))
         (extra (remainder len k))
         (res (make-vector k #f)))
    ;; helper to process each part
    (let loop-parts ((i 0) (cur head))
      (if (< i k)
          (let* ((size (+ base (if (< i extra) 1 0))))
            (if (= size 0)
                (begin
                  (vector-set! res i #f)
                  (loop-parts (+ i 1) cur))
                (let walk ((steps (- size 1)) (prev cur) (next (list-node-next cur)))
                  (if (= steps 0)
                      (begin
                        (set-list-node-next! prev #f)
                        (vector-set! res i cur)
                        (loop-parts (+ i 1) next))
                      (walk (- steps 1) next (and next (list-node-next next)))))))
          (void)))
    (vector->list res)))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec split_list_to_parts(Head :: #list_node{} | null, K :: integer()) -> [#list_node{} | null].
split_list_to_parts(Head, K) ->
    Len = count_len(Head),
    Base = Len div K,
    Rem  = Len rem K,
    build_parts(Head, K, Base, Rem).

%% Count the number of nodes in the list.
count_len(null) -> 0;
count_len(#list_node{next = Next}) -> 1 + count_len(Next).

%% Build the resulting list of parts.
build_parts(_Current, 0, _Base, _Rem) ->
    [];
build_parts(Current, PartsLeft, Base, Rem) ->
    PartSize = Base + (if Rem > 0 -> 1; true -> 0 end),
    NewRem   = if Rem > 0 -> Rem - 1; true -> Rem end,
    {PartHead, NextCurrent} = take_part(Current, PartSize),
    [PartHead | build_parts(NextCurrent, PartsLeft - 1, Base, NewRem)].

%% Take Size nodes from Source, constructing a new list.
take_part(Source, 0) ->
    {null, Source};
take_part(null, _Size) ->
    {null, null};
take_part(#list_node{val = V, next = NextSrc}, Size) when Size > 0 ->
    {RestHead, RestTail} = take_part(NextSrc, Size - 1),
    NewNode = #list_node{val = V, next = RestHead},
    {NewNode, RestTail}.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_list_to_parts(head :: ListNode.t() | nil, k :: integer) :: [ListNode.t() | nil]
  def split_list_to_parts(head, k) do
    total_len = list_length(head)
    base_size = div(total_len, k)
    extra = rem(total_len, k)

    {parts, _} =
      Enum.map_reduce(0..(k - 1), head, fn idx, cur_head ->
        part_size = base_size + if idx < extra, do: 1, else: 0
        {part_head, next_head} = take_nodes(cur_head, part_size)
        {part_head, next_head}
      end)

    parts
  end

  defp list_length(nil), do: 0
  defp list_length(%ListNode{next: nxt}), do: 1 + list_length(nxt)

  defp take_nodes(head, 0), do: {nil, head}
  defp take_nodes(nil, _n), do: {nil, nil}
  defp take_nodes(%ListNode{val: v, next: nxt} = node, n) when n > 0 do
    {next_part, rest_head} = take_nodes(nxt, n - 1)
    new_node = %ListNode{val: v, next: next_part}
    {new_node, rest_head}
  end
end
```
