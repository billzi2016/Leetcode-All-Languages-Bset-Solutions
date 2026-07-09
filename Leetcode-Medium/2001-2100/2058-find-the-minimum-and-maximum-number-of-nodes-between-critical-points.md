# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (!head || !head->next) return {-1, -1};
        
        int index = 0; // position of current node
        ListNode* prev = nullptr;
        ListNode* curr = head;
        // advance to second node for checking (needs both prev and next)
        prev = curr;
        curr = curr->next;
        ++index; // now at position 1
        
        int firstCrit = -1;
        int prevCrit = -1;
        int minDist = INT_MAX;
        
        while (curr && curr->next) {
            // curr has both prev and next
            if ((prev->val < curr->val && curr->val > curr->next->val) ||
                (prev->val > curr->val && curr->val < curr->next->val)) {
                if (firstCrit == -1) {
                    firstCrit = prevCrit = index;
                } else {
                    minDist = min(minDist, index - prevCrit);
                    prevCrit = index;
                }
            }
            // move forward
            prev = curr;
            curr = curr->next;
            ++index;
        }
        
        if (firstCrit == -1 || minDist == INT_MAX) return {-1, -1};
        int maxDist = prevCrit - firstCrit;
        return {minDist, maxDist};
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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null) {
            return new int[]{-1, -1};
        }

        ListNode prev = head;
        ListNode curr = head.next;
        int pos = 1; // position of 'curr' (0‑based indexing)

        Integer firstCritical = null;
        Integer prevCritical = null;
        int minDist = Integer.MAX_VALUE;

        while (curr != null && curr.next != null) {
            boolean isMax = curr.val > prev.val && curr.val > curr.next.val;
            boolean isMin = curr.val < prev.val && curr.val < curr.next.val;
            if (isMax || isMin) { // critical point
                if (firstCritical == null) {
                    firstCritical = pos;
                    prevCritical = pos;
                } else {
                    minDist = Math.min(minDist, pos - prevCritical);
                    prevCritical = pos;
                }
            }

            // advance pointers
            prev = curr;
            curr = curr.next;
            pos++;
        }

        if (firstCritical == null || firstCritical.equals(prevCritical)) {
            return new int[]{-1, -1};
        }

        int maxDist = prevCritical - firstCritical;
        return new int[]{minDist, maxDist};
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
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next:
            return [-1, -1]

        prev = head
        curr = head.next
        idx = 1  # position of curr (0-based indexing)

        first_crit = -1
        prev_crit = -1
        min_dist = float('inf')

        while curr and curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first_crit == -1:
                    first_crit = idx
                    prev_crit = idx
                else:
                    min_dist = min(min_dist, idx - prev_crit)
                    prev_crit = idx
            # advance pointers
            prev = curr
            curr = nxt
            idx += 1

        if first_crit == -1 or first_crit == prev_crit:
            return [-1, -1]

        max_dist = prev_crit - first_crit
        return [min_dist, max_dist]
```

## Python3

```python
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional['ListNode']) -> List[int]:
        if not head or not head.next:
            return [-1, -1]

        prev = head
        curr = head.next
        idx = 1  # index of curr (0-based)

        first_cp = -1      # index of first critical point
        last_cp = -1       # index of most recent critical point
        min_dist = float('inf')
        cp_count = 0

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                cp_count += 1
                if first_cp == -1:
                    first_cp = idx
                    last_cp = idx
                else:
                    min_dist = min(min_dist, idx - last_cp)
                    last_cp = idx
            # move forward
            prev = curr
            curr = curr.next
            idx += 1

        if cp_count < 2:
            return [-1, -1]

        max_dist = last_cp - first_cp
        return [min_dist, max_dist]
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
    int *ans = (int*)malloc(2 * sizeof(int));
    ans[0] = -1;
    ans[1] = -1;
    *returnSize = 2;

    if (!head || !head->next) return ans;

    struct ListNode *prev = head;
    struct ListNode *curr = head->next;
    int idx = 1;                     // position of curr (0‑based)
    int firstCrit = -1;              // index of first critical point
    int prevCrit = -1;               // index of previous critical point
    int minDist = INT_MAX;
    int critCount = 0;

    while (curr && curr->next) {
        struct ListNode *next = curr->next;
        if ((curr->val > prev->val && curr->val > next->val) ||
            (curr->val < prev->val && curr->val < next->val)) {
            // critical point found at idx
            if (critCount == 0) {
                firstCrit = idx;
                prevCrit = idx;
            } else {
                int dist = idx - prevCrit;
                if (dist < minDist) minDist = dist;
                prevCrit = idx;
            }
            critCount++;
        }
        // advance pointers
        prev = curr;
        curr = next;
        idx++;
    }

    if (critCount >= 2) {
        ans[0] = minDist;
        ans[1] = prevCrit - firstCrit;   // max distance between first and last critical points
    }

    return ans;
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
    public int[] NodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null) return new int[] { -1, -1 };

        ListNode prev = head;
        ListNode curr = head.next;
        int idx = 1; // position of 'curr' (0-based indexing)

        int firstCriticalIdx = -1;
        int prevCriticalIdx = -1;
        int minDist = int.MaxValue;

        while (curr != null && curr.next != null) {
            bool isPeak = curr.val > prev.val && curr.val > curr.next.val;
            bool isValley = curr.val < prev.val && curr.val < curr.next.val;

            if (isPeak || isValley) {
                if (firstCriticalIdx == -1) {
                    firstCriticalIdx = idx;
                    prevCriticalIdx = idx;
                } else {
                    minDist = Math.Min(minDist, idx - prevCriticalIdx);
                    prevCriticalIdx = idx;
                }
            }

            // advance pointers
            prev = curr;
            curr = curr.next;
            idx++;
        }

        if (firstCriticalIdx == -1 || firstCriticalIdx == prevCriticalIdx) {
            return new int[] { -1, -1 };
        }

        int maxDist = prevCriticalIdx - firstCriticalIdx;
        return new int[] { minDist, maxDist };
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
var nodesBetweenCriticalPoints = function(head) {
    if (!head || !head.next) return [-1, -1];
    
    let prev = head;
    let curr = head.next;
    let idx = 1; // position of curr
    
    const INF = Number.MAX_SAFE_INTEGER;
    let minDist = INF;
    let firstCriticalIdx = -1;
    let prevCriticalIdx = -1;
    
    while (curr && curr.next) {
        const next = curr.next;
        const isMax = curr.val > prev.val && curr.val > next.val;
        const isMin = curr.val < prev.val && curr.val < next.val;
        
        if (isMax || isMin) {
            if (firstCriticalIdx === -1) {
                firstCriticalIdx = idx;
                prevCriticalIdx = idx;
            } else {
                minDist = Math.min(minDist, idx - prevCriticalIdx);
                prevCriticalIdx = idx;
            }
        }
        
        // move forward
        prev = curr;
        curr = next;
        idx++;
    }
    
    if (firstCriticalIdx === -1 || minDist === INF) {
        return [-1, -1];
    }
    
    const maxDist = prevCriticalIdx - firstCriticalIdx;
    return [minDist, maxDist];
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

function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    if (!head || !head.next) return [-1, -1];

    let prev = head;
    let curr = head.next;
    let idx = 1; // position of curr

    let firstCrit = -1;
    let prevCrit = -1;
    let lastCrit = -1;
    let minDist = Number.MAX_SAFE_INTEGER;

    while (curr && curr.next) {
        const isMax = curr.val > prev.val && curr.val > curr.next!.val;
        const isMin = curr.val < prev.val && curr.val < curr.next!.val;
        if (isMax || isMin) {
            if (firstCrit === -1) {
                firstCrit = idx;
                prevCrit = idx;
                lastCrit = idx;
            } else {
                minDist = Math.min(minDist, idx - prevCrit);
                prevCrit = idx;
                lastCrit = idx;
            }
        }
        prev = curr;
        curr = curr.next;
        idx++;
    }

    if (firstCrit === -1 || firstCrit === lastCrit) return [-1, -1];

    const maxDist = lastCrit - firstCrit;
    return [minDist, maxDist];
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
     * @return Integer[]
     */
    function nodesBetweenCriticalPoints($head) {
        if ($head === null || $head->next === null) {
            return [-1, -1];
        }

        $prev = $head;
        $curr = $head->next;
        $index = 2; // position of $curr (1-indexed)

        $firstCritical = -1;
        $lastCritical = -1;
        $minDist = PHP_INT_MAX;

        while ($curr !== null && $curr->next !== null) {
            $isCritical = false;
            if (($curr->val > $prev->val && $curr->val > $curr->next->val) ||
                ($curr->val < $prev->val && $curr->val < $curr->next->val)) {
                $isCritical = true;
            }

            if ($isCritical) {
                if ($firstCritical == -1) {
                    $firstCritical = $index;
                    $lastCritical = $index;
                } else {
                    $dist = $index - $lastCritical;
                    if ($dist < $minDist) {
                        $minDist = $dist;
                    }
                    $lastCritical = $index;
                }
            }

            // move forward
            $prev = $curr;
            $curr = $curr->next;
            $index++;
        }

        if ($firstCritical != -1 && $firstCritical != $lastCritical) {
            $maxDist = $lastCritical - $firstCritical;
            return [$minDist, $maxDist];
        }

        return [-1, -1];
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
    func nodesBetweenCriticalPoints(_ head: ListNode?) -> [Int] {
        guard let head = head else { return [-1, -1] }
        var prev: ListNode? = head
        var curr: ListNode? = head.next
        var index = 1               // position of `curr` (head is at 0)
        
        var firstCriticalIdx: Int? = nil
        var previousCriticalIdx: Int? = nil
        var minDist = Int.max
        
        while let current = curr, let nextNode = current.next {
            let isMax = current.val > prev!.val && current.val > nextNode.val
            let isMin = current.val < prev!.val && current.val < nextNode.val
            if isMax || isMin {
                if firstCriticalIdx == nil {
                    firstCriticalIdx = index
                    previousCriticalIdx = index
                } else {
                    let dist = index - previousCriticalIdx!
                    if dist < minDist { minDist = dist }
                    previousCriticalIdx = index
                }
            }
            // advance pointers
            prev = curr
            curr = curr?.next
            index += 1
        }
        
        guard let first = firstCriticalIdx,
              let last = previousCriticalIdx,
              first != last else {
            return [-1, -1]
        }
        
        let maxDist = last - first
        return [minDist, maxDist]
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
    fun nodesBetweenCriticalPoints(head: ListNode?): IntArray {
        if (head == null || head.next == null) return intArrayOf(-1, -1)

        var prev = head
        var curr = head.next!!
        var index = 1 // position of curr (0-based for head)

        var firstCrit = -1
        var lastCrit = -1
        var prevCrit = -1
        var minDist = Int.MAX_VALUE

        while (curr.next != null) {
            val nextNode = curr.next!!

            val isCritical = (curr.`val` > prev.`val` && curr.`val` > nextNode.`val`) ||
                             (curr.`val` < prev.`val` && curr.`val` < nextNode.`val`)

            if (isCritical) {
                if (firstCrit == -1) {
                    firstCrit = index
                    prevCrit = index
                } else {
                    minDist = kotlin.math.min(minDist, index - prevCrit)
                    prevCrit = index
                }
                lastCrit = index
            }

            // advance pointers
            prev = curr
            curr = nextNode
            index++
        }

        if (minDist == Int.MAX_VALUE) return intArrayOf(-1, -1)

        val maxDist = lastCrit - firstCrit
        return intArrayOf(minDist, maxDist)
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
  List<int> nodesBetweenCriticalPoints(ListNode? head) {
    if (head == null || head.next == null) return [-1, -1];

    ListNode? prev = head;
    ListNode? curr = head.next;
    int idx = 1; // position of curr (0‑based indexing)

    int firstCriticalIdx = -1;
    int prevCriticalIdx = -1;
    int minDist = 0x7fffffff;

    while (curr != null && curr.next != null) {
      bool isCritical = false;
      if ((curr.val > prev!.val && curr.val > curr.next!.val) ||
          (curr.val < prev.val && curr.val < curr.next!.val)) {
        isCritical = true;
      }

      if (isCritical) {
        if (firstCriticalIdx == -1) {
          firstCriticalIdx = idx;
          prevCriticalIdx = idx;
        } else {
          int dist = idx - prevCriticalIdx;
          if (dist < minDist) minDist = dist;
          prevCriticalIdx = idx;
        }
      }

      // advance pointers
      prev = curr;
      curr = curr.next;
      idx++;
    }

    // Need at least two critical points
    if (firstCriticalIdx == -1 || firstCriticalIdx == prevCriticalIdx) {
      return [-1, -1];
    }

    int maxDist = prevCriticalIdx - firstCriticalIdx;
    return [minDist, maxDist];
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
func nodesBetweenCriticalPoints(head *ListNode) []int {
	if head == nil || head.Next == nil {
		return []int{-1, -1}
	}

	prev := head
	curr := head.Next
	idx := 1 // position of curr (0‑based for head)

	firstCritIdx := -1
	prevCritIdx := -1
	minDist := int(^uint(0) >> 1) // max int

	for curr != nil && curr.Next != nil {
		if (curr.Val > prev.Val && curr.Val > curr.Next.Val) ||
			(curr.Val < prev.Val && curr.Val < curr.Next.Val) {

			if firstCritIdx == -1 {
				firstCritIdx = idx
				prevCritIdx = idx
			} else {
				dist := idx - prevCritIdx
				if dist < minDist {
					minDist = dist
				}
				prevCritIdx = idx
			}
		}
		prev = curr
		curr = curr.Next
		idx++
	}

	if firstCritIdx == -1 || firstCritIdx == prevCritIdx {
		return []int{-1, -1}
	}
	maxDist := prevCritIdx - firstCritIdx
	return []int{minDist, maxDist}
}
```

## Ruby

```ruby
def nodes_between_critical_points(head)
  return [-1, -1] if head.nil? || head.next.nil?

  prev = head
  cur = head.next
  idx = 1

  first_cp = nil
  last_cp = nil
  prev_cp = nil
  min_dist = Float::INFINITY

  while cur && cur.next
    is_max = cur.val > prev.val && cur.val > cur.next.val
    is_min = cur.val < prev.val && cur.val < cur.next.val
    if is_max || is_min
      if first_cp.nil?
        first_cp = idx
        prev_cp = idx
      else
        dist = idx - prev_cp
        min_dist = [min_dist, dist].min
        prev_cp = idx
      end
      last_cp = idx
    end

    prev = cur
    cur = cur.next
    idx += 1
  end

  if first_cp.nil? || first_cp == last_cp
    [-1, -1]
  else
    max_dist = last_cp - first_cp
    [min_dist.to_i, max_dist]
  end
end
```

## Scala

```scala
object Solution {
  def nodesBetweenCriticalPoints(head: ListNode): Array[Int] = {
    if (head == null || head.next == null) return Array(-1, -1)

    var prev = head
    var curr = head.next
    var idx = 1 // index of curr node

    var firstCrit = -1
    var prevCrit = -1
    var minDist = Int.MaxValue

    while (curr != null && curr.next != null) {
      val isMax = curr.x > prev.x && curr.x > curr.next.x
      val isMin = curr.x < prev.x && curr.x < curr.next.x
      if (isMax || isMin) {
        if (firstCrit == -1) {
          firstCrit = idx
          prevCrit = idx
        } else {
          minDist = math.min(minDist, idx - prevCrit)
          prevCrit = idx
        }
      }
      prev = curr
      curr = curr.next
      idx += 1
    }

    if (minDist == Int.MaxValue) Array(-1, -1)
    else {
      val maxDist = prevCrit - firstCrit
      Array(minDist, maxDist)
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        // Need at least three nodes to have a critical point
        let mut prev_opt = head.as_ref();
        let mut curr_opt = prev_opt.and_then(|node| node.next.as_ref());
        let mut next_opt = curr_opt.and_then(|node| node.next.as_ref());

        if next_opt.is_none() {
            return vec![-1, -1];
        }

        let mut idx: usize = 1; // index of `curr_opt` (0‑based)
        let mut first_cp: Option<usize> = None;
        let mut prev_cp: Option<usize> = None;
        let mut min_dist: usize = usize::MAX;

        while let (Some(p), Some(c), Some(n)) = (prev_opt, curr_opt, next_opt) {
            // check if current node is a critical point
            if (c.val > p.val && c.val > n.val) || (c.val < p.val && c.val < n.val) {
                match first_cp {
                    None => {
                        first_cp = Some(idx);
                        prev_cp = Some(idx);
                    }
                    Some(_) => {
                        let pc = prev_cp.unwrap();
                        if idx - pc < min_dist {
                            min_dist = idx - pc;
                        }
                        prev_cp = Some(idx);
                    }
                }
            }

            // advance the three pointers
            prev_opt = curr_opt;
            curr_opt = next_opt;
            next_opt = n.next.as_ref();
            idx += 1;
        }

        if let (Some(first), Some(last)) = (first_cp, prev_cp) {
            if min_dist == usize::MAX {
                // only one critical point
                vec![-1, -1]
            } else {
                let max_dist = last - first;
                vec![min_dist as i32, max_dist as i32]
            }
        } else {
            vec![-1, -1]
        }
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
(struct list-node (val next) #:mutable #:transparent)

(define/contract (nodes-between-critical-points head)
  (-> (or/c list-node? #f) (listof exact-integer?))
  (if (or (not head) (not (list-node-next head)))
      (list -1 -1)
      (let loop ((prev head)
                 (cur (list-node-next head))
                 (idx 1)                     ; index of cur (0‑based for first node)
                 (first #f)                  ; index of first critical point
                 (prev-crit #f)              ; index of previous critical point
                 (last #f)                   ; index of last critical point seen
                 (min-dist 1000000000)       ; large initial value
                 (cnt 0))                    ; number of critical points found
        (if (or (not cur) (not (list-node-next cur)))
            (if (< cnt 2)
                (list -1 -1)
                (list min-dist (- last first)))
            (let* ((next (list-node-next cur))
                   (val (list-node-val cur))
                   (prev-val (list-node-val prev))
                   (next-val (list-node-val next))
                   (is-crit (or (and (> val prev-val) (> val next-val))
                                (and (< val prev-val) (< val next-val)))))
              (if is-crit
                  (let* ((new-first (if first idx first))
                         (new-min (if prev-crit
                                      (min min-dist (- idx prev-crit))
                                      min-dist))
                         (new-prev-crit idx)
                         (new-last idx)
                         (new-cnt (+ cnt 1)))
                    (loop cur next (+ idx 1) new-first new-prev-crit new-last new-min new-cnt))
                  (loop cur next (+ idx 1) first prev-crit last min-dist cnt))))))))
```

## Erlang

```erlang
-module(solution).
-export([nodes_between_critical_points/1]).

-define(INF, 1000000000).

-record(list_node, {val = 0 :: integer(),
                   next = null :: 'null' | #list_node{}}).

-spec nodes_between_critical_points(Head :: #list_node{} | null) -> [integer()].
nodes_between_critical_points(null) ->
    [-1, -1];
nodes_between_critical_points(#list_node{next = null}) ->
    [-1, -1];
nodes_between_critical_points(Head) ->
    PrevNode = Head,
    CurrNode = Head#list_node.next,
    loop(CurrNode, PrevNode, 2, undefined, undefined, undefined, 0, ?INF).

loop(null, _Prev, _Idx, FirstPos, _PrevCrit, LastPos, Count, MinDist) ->
    finalize(FirstPos, LastPos, Count, MinDist);
loop(#list_node{next = null} = _CurrNode, _Prev, _Idx, FirstPos, _PrevCrit, LastPos, Count, MinDist) ->
    finalize(FirstPos, LastPos, Count, MinDist);
loop(CurrNode, PrevNode, Idx,
     FirstPos, PrevCritPos, LastPos, Count, MinDist) ->
    #list_node{val = CurrVal, next = NextNode} = CurrNode,
    PrevVal = PrevNode#list_node.val,
    NextVal = NextNode#list_node.val,
    IsCritical = (CurrVal > PrevVal andalso CurrVal > NextVal) orelse
                 (CurrVal < PrevVal andalso CurrVal < NextVal),
    case IsCritical of
        true ->
            NewCount = Count + 1,
            case Count of
                0 ->
                    loop(NextNode, CurrNode, Idx+1,
                         Idx, Idx, Idx, NewCount, MinDist);
                _ ->
                    Dist = Idx - PrevCritPos,
                    NewMin = if Dist < MinDist -> Dist; true -> MinDist end,
                    loop(NextNode, CurrNode, Idx+1,
                         FirstPos, Idx, Idx, NewCount, NewMin)
            end;
        false ->
            loop(NextNode, CurrNode, Idx+1,
                 FirstPos, PrevCritPos, LastPos, Count, MinDist)
    end.

finalize(undefined, _LastPos, _Count, _MinDist) ->
    [-1, -1];
finalize(_FirstPos, _LastPos, Count, _MinDist) when Count < 2 ->
    [-1, -1];
finalize(FirstPos, LastPos, _Count, MinDist) ->
    [MinDist, LastPos - FirstPos].
```

## Elixir

```elixir
defmodule Solution do
  @spec nodes_between_critical_points(head :: ListNode.t() | nil) :: [integer]
  def nodes_between_critical_points(head) do
    case head do
      nil -> [-1, -1]
      %ListNode{next: nil} -> [-1, -1]
      _ ->
        prev = head
        cur = head.next
        {first_idx, last_idx, min_dist} = traverse(prev, cur, 1, nil, nil, :infinity)

        if first_idx != nil and last_idx != first_idx do
          max_dist = last_idx - first_idx
          [min_dist, max_dist]
        else
          [-1, -1]
        end
    end
  end

  defp traverse(_prev, nil, _idx, first_idx, last_idx, min_dist), do: {first_idx, last_idx, min_dist}
  defp traverse(prev, %ListNode{next: nil} = cur, idx, first_idx, last_idx, min_dist) do
    # cur is the last node; cannot be critical, stop traversal
    {first_idx, last_idx, min_dist}
  end

  defp traverse(prev, %ListNode{val: c_val, next: nxt} = cur, idx, first_idx, last_idx, min_dist) do
    crit? =
      (c_val > prev.val and c_val > nxt.val) or
        (c_val < prev.val and c_val < nxt.val)

    {new_first, new_last, new_min} =
      if crit? do
        cond do
          first_idx == nil ->
            {idx, idx, min_dist}
          true ->
            updated_min = Kernel.min(min_dist, idx - last_idx)
            {first_idx, idx, updated_min}
        end
      else
        {first_idx, last_idx, min_dist}
      end

    traverse(cur, nxt, idx + 1, new_first, new_last, new_min)
  end
end
```
