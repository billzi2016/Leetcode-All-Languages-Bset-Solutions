# 0023. Merge k Sorted Lists

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
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        struct Compare {
            bool operator()(ListNode* a, ListNode* b) const {
                return a->val > b->val;
            }
        };
        
        std::priority_queue<ListNode*, std::vector<ListNode*>, Compare> minHeap;
        for (auto node : lists) {
            if (node) minHeap.push(node);
        }
        
        ListNode dummy(0);
        ListNode* tail = &dummy;
        
        while (!minHeap.empty()) {
            ListNode* cur = minHeap.top();
            minHeap.pop();
            tail->next = cur;
            tail = tail->next;
            if (cur->next) {
                minHeap.push(cur->next);
            }
        }
        
        return dummy.next;
    }
};
```

## Java

```java
import java.util.PriorityQueue;

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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (!pq.isEmpty()) {
            ListNode cur = pq.poll();
            tail.next = cur;
            tail = tail.next;
            if (cur.next != null) {
                pq.offer(cur.next);
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
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        # Initialize heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
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

static void heapSwap(struct ListNode **a, struct ListNode **b) {
    struct ListNode *tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(struct ListNode **heap, int *size, struct ListNode *node) {
    int i = (*size);
    heap[i] = node;
    (*size)++;
    while (i > 0) {
        int parent = (i - 1) >> 1;
        if (heap[parent]->val <= heap[i]->val) break;
        heapSwap(&heap[parent], &heap[i]);
        i = parent;
    }
}

static struct ListNode *heapPop(struct ListNode **heap, int *size) {
    if (*size == 0) return NULL;
    struct ListNode *top = heap[0];
    (*size)--;
    heap[0] = heap[*size];
    int i = 0;
    while (1) {
        int left = (i << 1) + 1;
        int right = left + 1;
        int smallest = i;
        if (left < *size && heap[left]->val < heap[smallest]->val)
            smallest = left;
        if (right < *size && heap[right]->val < heap[smallest]->val)
            smallest = right;
        if (smallest == i) break;
        heapSwap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return top;
}

/**
 * Merge k sorted linked lists and return it as one sorted list.
 */
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize == 0) return NULL;

    struct ListNode **heap = (struct ListNode **)malloc(sizeof(struct ListNode *) * listsSize);
    int heapSize = 0;

    for (int i = 0; i < listsSize; ++i) {
        if (lists[i] != NULL) {
            heapPush(heap, &heapSize, lists[i]);
        }
    }

    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode *tail = &dummy;

    while (heapSize > 0) {
        struct ListNode *node = heapPop(heap, &heapSize);
        tail->next = node;
        tail = node;
        if (node->next != NULL) {
            heapPush(heap, &heapSize, node->next);
        }
    }

    free(heap);
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
    public ListNode MergeKLists(ListNode[] lists) {
        if (lists == null || lists.Length == 0) return null;

        var pq = new PriorityQueue<ListNode, int>();
        foreach (var node in lists) {
            if (node != null) {
                pq.Enqueue(node, node.val);
            }
        }

        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        while (pq.Count > 0) {
            var smallest = pq.Dequeue();
            tail.next = smallest;
            tail = tail.next;
            if (smallest.next != null) {
                pq.Enqueue(smallest.next, smallest.next.val);
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
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
        }
        push(node) {
            const h = this.heap;
            h.push(node);
            let idx = h.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (h[parent].val <= h[idx].val) break;
                [h[parent], h[idx]] = [h[idx], h[parent]];
                idx = parent;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return null;
            const min = h[0];
            const end = h.pop();
            if (h.length > 0) {
                h[0] = end;
                this._bubbleDown(0);
            }
            return min;
        }
        _bubbleDown(idx) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && h[left].val < h[smallest].val) smallest = left;
                if (right < n && h[right].val < h[smallest].val) smallest = right;
                if (smallest === idx) break;
                [h[idx], h[smallest]] = [h[smallest], h[idx]];
                idx = smallest;
            }
        }
    }

    const heap = new MinHeap();
    for (const node of lists) {
        if (node !== null) heap.push(node);
    }

    const dummy = new ListNode(0);
    let tail = dummy;

    while (heap.size() > 0) {
        const smallest = heap.pop();
        tail.next = smallest;
        tail = tail.next;
        if (smallest.next !== null) heap.push(smallest.next);
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

class MinHeap {
    private data: ListNode[] = [];

    size(): number {
        return this.data.length;
    }

    push(node: ListNode): void {
        this.data.push(node);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): ListNode | undefined {
        if (this.data.length === 0) return undefined;
        const min = this.data[0];
        const end = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = end;
            this.bubbleDown(0);
        }
        return min;
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this.data[parent].val <= this.data[idx].val) break;
            this.swap(parent, idx);
            idx = parent;
        }
    }

    private bubbleDown(idx: number): void {
        const length = this.data.length;
        while (true) {
            let smallest = idx;
            const left = idx * 2 + 1;
            const right = left + 1;

            if (left < length && this.data[left].val < this.data[smallest].val) {
                smallest = left;
            }
            if (right < length && this.data[right].val < this.data[smallest].val) {
                smallest = right;
            }
            if (smallest === idx) break;
            this.swap(idx, smallest);
            idx = smallest;
        }
    }

    private swap(i: number, j: number): void {
        const temp = this.data[i];
        this.data[i] = this.data[j];
        this.data[j] = temp;
    }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const heap = new MinHeap();
    for (const node of lists) {
        if (node) heap.push(node);
    }

    const dummy = new ListNode(0);
    let tail = dummy;

    while (heap.size() > 0) {
        const minNode = heap.pop()!;
        tail.next = minNode;
        tail = tail.next;
        if (minNode.next) heap.push(minNode.next);
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
     * @param ListNode[] $lists
     * @return ListNode|null
     */
    function mergeKLists($lists) {
        $heap = new SplPriorityQueue();
        // We only need the node data when extracting
        $heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        foreach ($lists as $node) {
            if ($node !== null) {
                // Use negative value as priority to simulate a min-heap
                $heap->insert($node, -$node->val);
            }
        }

        $dummy = new ListNode(0);
        $curr = $dummy;

        while (!$heap->isEmpty()) {
            /** @var ListNode $node */
            $node = $heap->extract(); // node with smallest value
            $curr->next = $node;
            $curr = $curr->next;

            if ($node->next !== null) {
                $heap->insert($node->next, -$node->next->val);
            }
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
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        var heap = MinHeap()
        for node in lists {
            if let n = node {
                heap.push(n)
            }
        }
        let dummy = ListNode(0)
        var tail = dummy
        while let smallest = heap.pop() {
            tail.next = smallest
            tail = smallest
            if let next = smallest.next {
                heap.push(next)
            }
        }
        return dummy.next
    }
}

struct MinHeap {
    private var data: [ListNode] = []
    
    mutating func push(_ node: ListNode) {
        data.append(node)
        var idx = data.count - 1
        while idx > 0 {
            let parent = (idx - 1) / 2
            if data[idx].val < data[parent].val {
                data.swapAt(idx, parent)
                idx = parent
            } else { break }
        }
    }
    
    mutating func pop() -> ListNode? {
        guard !data.isEmpty else { return nil }
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            var idx = 0
            while true {
                let left = idx * 2 + 1
                let right = left + 1
                var smallest = idx
                if left < data.count && data[left].val < data[smallest].val {
                    smallest = left
                }
                if right < data.count && data[right].val < data[smallest].val {
                    smallest = right
                }
                if smallest == idx { break }
                data.swapAt(idx, smallest)
                idx = smallest
            }
        }
        return result
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
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        val pq = java.util.PriorityQueue<ListNode>(compareBy { it.`val` })
        for (node in lists) {
            if (node != null) {
                pq.add(node)
            }
        }
        val dummy = ListNode(0)
        var tail: ListNode = dummy
        while (pq.isNotEmpty()) {
            val node = pq.poll()
            tail.next = node
            tail = tail.next!!
            if (node.next != null) {
                pq.add(node.next)
            }
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
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class _MinHeap {
  final List<ListNode> _heap = [];

  bool get isEmpty => _heap.isEmpty;

  void add(ListNode node) {
    _heap.add(node);
    _siftUp(_heap.length - 1);
  }

  ListNode removeMin() {
    final min = _heap.first;
    final last = _heap.removeLast();
    if (_heap.isNotEmpty) {
      _heap[0] = last;
      _siftDown(0);
    }
    return min;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_heap[parent].val <= _heap[idx].val) break;
      _swap(parent, idx);
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    final n = _heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _heap[left].val < _heap[smallest].val) {
        smallest = left;
      }
      if (right < n && _heap[right].val < _heap[smallest].val) {
        smallest = right;
      }
      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final tmp = _heap[i];
    _heap[i] = _heap[j];
    _heap[j] = tmp;
  }
}

class Solution {
  ListNode? mergeKLists(List<ListNode?> lists) {
    final heap = _MinHeap();
    for (var node in lists) {
      if (node != null) heap.add(node);
    }

    final dummy = ListNode(0);
    var tail = dummy;

    while (!heap.isEmpty) {
      final minNode = heap.removeMin();
      tail.next = minNode;
      tail = tail.next!;

      if (minNode.next != null) {
        heap.add(minNode.next!);
      }
    }

    return dummy.next;
  }
}
```

## Golang

```go
import "container/heap"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type nodeHeap []*ListNode

func (h nodeHeap) Len() int { return len(h) }
func (h nodeHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h nodeHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *nodeHeap) Push(x interface{}) {
	*h = append(*h, x.(*ListNode))
}
func (h *nodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	node := old[n-1]
	*h = old[:n-1]
	return node
}

func mergeKLists(lists []*ListNode) *ListNode {
	var h nodeHeap
	heap.Init(&h)

	for _, node := range lists {
		if node != nil {
			heap.Push(&h, node)
		}
	}

	dummy := &ListNode{}
	cur := dummy

	for h.Len() > 0 {
		minNode := heap.Pop(&h).(*ListNode)
		cur.Next = minNode
		cur = cur.Next
		if minNode.Next != nil {
			heap.Push(&h, minNode.Next)
		}
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

def merge_two_lists(l1, l2)
  dummy = ListNode.new(0)
  tail = dummy
  while l1 && l2
    if l1.val < l2.val
      tail.next = l1
      l1 = l1.next
    else
      tail.next = l2
      l2 = l2.next
    end
    tail = tail.next
  end
  tail.next = l1 || l2
  dummy.next
end

def merge_k_lists(lists)
  return nil if lists.empty?
  n = lists.length
  interval = 1
  while interval < n
    (0...n).step(interval * 2) do |i|
      j = i + interval
      if j < n
        lists[i] = merge_two_lists(lists[i], lists[j])
      end
    end
    interval <<= 1
  end
  lists[0]
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
  def mergeKLists(lists: Array[ListNode]): ListNode = {
    import java.util.PriorityQueue

    val pq = new PriorityQueue[ListNode]((a: ListNode, b: ListNode) => Integer.compare(a.x, b.x))
    for (node <- lists if node != null) {
      pq.offer(node)
    }

    val dummy = new ListNode(0)
    var tail = dummy

    while (!pq.isEmpty) {
      val cur = pq.poll()
      tail.next = cur
      tail = tail.next
      if (cur.next != null) {
        pq.offer(cur.next)
      }
    }

    dummy.next
  }
}
```

## Rust

```rust
use std::cmp::Ordering;
use std::collections::BinaryHeap;

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

struct HeapNode {
    val: i32,
    node: Box<ListNode>,
}

impl PartialEq for HeapNode {
    fn eq(&self, other: &Self) -> bool {
        self.val == other.val
    }
}
impl Eq for HeapNode {}

impl PartialOrd for HeapNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(other.val.cmp(&self.val)) // reverse for min-heap
    }
}
impl Ord for HeapNode {
    fn cmp(&self, other: &Self) -> Ordering {
        other.val.cmp(&self.val) // reverse for min-heap
    }
}

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        let mut heap = BinaryHeap::new();

        for opt in lists.into_iter() {
            if let Some(node) = opt {
                heap.push(HeapNode { val: node.val, node });
            }
        }

        let mut dummy = Box::new(ListNode::new(0));
        let mut cur = &mut dummy.next;

        while let Some(mut smallest) = heap.pop() {
            // detach the next pointer
            let next_opt = smallest.node.next.take();

            // attach smallest node to result list
            *cur = Some(smallest.node);
            cur = &mut cur.as_mut().unwrap().next;

            if let Some(next_node) = next_opt {
                heap.push(HeapNode { val: next_node.val, node: next_node });
            }
        }

        dummy.next
    }
}
```

## Racket

```racket
(define (merge-two l1 l2)
  (cond
    [(not l1) l2]
    [(not l2) l1]
    [else
     (if (<= (list-node-val l1) (list-node-val l2))
         (begin
           (set-list-node-next! l1 (merge-two (list-node-next l1) l2))
           l1)
         (begin
           (set-list-node-next! l2 (merge-two l1 (list-node-next l2)))
           l2))]))

(define (pair-merge lst)
  (cond
    [(empty? lst) '()]
    [(empty? (cdr lst)) (list (car lst))]
    [else (cons (merge-two (car lst) (cadr lst))
                (pair-merge (cddr lst)))]))

(define/contract (merge-k-lists lists)
  (-> (listof (or/c list-node? #f)) (or/c list-node? #f))
  (let recur ((lst lists))
    (cond
      [(empty? lst) #f]
      [(null? (cdr lst)) (car lst)]
      [else (recur (pair-merge lst))])))
```

## Erlang

```erlang
-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-spec merge_k_lists(Lists :: [#list_node{} | null]) -> #list_node{} | null.
merge_k_lists([]) ->
    null;
merge_k_lists(Lists) ->
    merge_pairs(Lists).

%% Merge all lists pairwise until one remains
merge_pairs([L]) ->
    L;
merge_pairs(Lists) ->
    Merged = merge_pairwise(Lists, []),
    merge_pairs(Merged).

%% Merge adjacent pairs and collect results in Acc (reversed)
merge_pairwise([], Acc) ->
    lists:reverse(Acc);
merge_pairwise([L], Acc) ->
    lists:reverse([L | Acc]);
merge_pairwise([L1, L2 | Rest], Acc) ->
    M = merge_two(L1, L2),
    merge_pairwise(Rest, [M | Acc]).

%% Merge two sorted linked lists
-spec merge_two(#list_node{} | null, #list_node{} | null) -> #list_node{} | null.
merge_two(null, L) -> L;
merge_two(L, null) -> L;
merge_two(L1 = #list_node{val = V1, next = N1},
          L2 = #list_node{val = V2, next = N2}) ->
    if
        V1 =< V2 ->
            L1#list_node{next = merge_two(N1, L2)};
        true ->
            L2#list_node{next = merge_two(L1, N2)}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec merge_k_lists(lists :: [ListNode.t() | nil]) :: ListNode.t() | nil
  def merge_k_lists(lists) do
    case lists do
      [] -> nil
      _ ->
        merged = merge_until_one(lists)
        hd(merged)
    end
  end

  defp merge_until_one([single]), do: [single]
  defp merge_until_one(lists) do
    merged = merge_pairs(lists)
    merge_until_one(merged)
  end

  defp merge_pairs([]), do: []
  defp merge_pairs([l]), do: [l]
  defp merge_pairs([l1, l2 | rest]) do
    [merge_two(l1, l2) | merge_pairs(rest)]
  end

  defp merge_two(nil, l), do: l
  defp merge_two(l, nil), do: l
  defp merge_two(%ListNode{val: v1, next: n1} = node1, %ListNode{val: v2, next: n2} = node2) do
    if v1 <= v2 do
      %ListNode{val: v1, next: merge_two(n1, node2)}
    else
      %ListNode{val: v2, next: merge_two(node1, n2)}
    end
  end
end
```
