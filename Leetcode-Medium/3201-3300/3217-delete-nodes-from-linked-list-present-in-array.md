# 3217. Delete Nodes From Linked List Present in Array

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
    ListNode* modifiedList(std::vector<int>& nums, ListNode* head) {
        std::unordered_set<int> toRemove(nums.begin(), nums.end());
        
        // Remove leading nodes that need deletion
        while (head && toRemove.count(head->val)) {
            ListNode* del = head;
            head = head->next;
            delete del;
        }
        
        // If all nodes were removed (shouldn't happen per constraints)
        if (!head) return nullptr;
        
        ListNode* cur = head;
        while (cur && cur->next) {
            if (toRemove.count(cur->next->val)) {
                ListNode* del = cur->next;
                cur->next = del->next;
                delete del;
            } else {
                cur = cur->next;
            }
        }
        return head;
    }
};
```

## Java

```java
import java.util.HashSet;
import java.util.Set;

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
    public ListNode modifiedList(int[] nums, ListNode head) {
        Set<Integer> toRemove = new HashSet<>();
        for (int v : nums) {
            toRemove.add(v);
        }
        while (head != null && toRemove.contains(head.val)) {
            head = head.next;
        }
        if (head == null) {
            return null;
        }
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            if (toRemove.contains(cur.next.val)) {
                cur.next = cur.next.next;
            } else {
                cur = cur.next;
            }
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
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        remove_set = set(nums)
        # Remove leading nodes that need to be deleted
        while head and head.val in remove_set:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val in remove_set:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
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
    def modifiedList(self, nums: List[int], head: Optional['ListNode']) -> Optional['ListNode']:
        remove_set = set(nums)
        # Remove leading nodes that need to be deleted
        while head and head.val in remove_set:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val in remove_set:
                cur.next = cur.next.next
            else:
                cur = cur.next
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
struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    // Values are in range [1, 100000]
    const int MAX_VAL = 100000;
    char *toRemove = (char *)calloc(MAX_VAL + 1, sizeof(char));
    if (!toRemove) return head; // allocation failure fallback

    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (v >= 1 && v <= MAX_VAL)
            toRemove[v] = 1;
    }

    // Skip leading nodes that need removal
    while (head && toRemove[head->val]) {
        struct ListNode *tmp = head;
        head = head->next;
        free(tmp);
    }

    struct ListNode *cur = head;
    while (cur && cur->next) {
        if (toRemove[cur->next->val]) {
            struct ListNode *tmp = cur->next;
            cur->next = tmp->next;
            free(tmp);
        } else {
            cur = cur->next;
        }
    }

    free(toRemove);
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
    public ListNode ModifiedList(int[] nums, ListNode head) {
        var toRemove = new HashSet<int>(nums);
        
        // Remove leading nodes that need deletion
        while (head != null && toRemove.Contains(head.val)) {
            head = head.next;
        }
        
        if (head == null) return null;
        
        var current = head;
        while (current != null && current.next != null) {
            if (toRemove.Contains(current.next.val)) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
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
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    const removeSet = new Set(nums);
    
    // Remove leading nodes that need to be deleted
    while (head && removeSet.has(head.val)) {
        head = head.next;
    }
    
    let cur = head;
    while (cur && cur.next) {
        if (removeSet.has(cur.next.val)) {
            cur.next = cur.next.next;
        } else {
            cur = cur.next;
        }
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

function modifiedList(nums: number[], head: ListNode | null): ListNode | null {
    const removeSet = new Set<number>(nums);
    
    // Remove leading nodes that need to be deleted
    while (head && removeSet.has(head.val)) {
        head = head.next;
    }
    
    let cur = head;
    while (cur && cur.next) {
        if (removeSet.has(cur.next.val)) {
            cur.next = cur.next.next; // skip the node
        } else {
            cur = cur.next;
        }
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
     * @param Integer[] $nums
     * @param ListNode $head
     * @return ListNode|null
     */
    function modifiedList($nums, $head) {
        // Build a hash set of values to remove
        $remove = [];
        foreach ($nums as $v) {
            $remove[$v] = true;
        }

        // Skip leading nodes that need removal
        while ($head !== null && isset($remove[$head->val])) {
            $head = $head->next;
        }

        if ($head === null) {
            return null;
        }

        // Traverse the rest of the list and unlink unwanted nodes
        $curr = $head;
        while ($curr !== null && $curr->next !== null) {
            if (isset($remove[$curr->next->val])) {
                $curr->next = $curr->next->next;
            } else {
                $curr = $curr->next;
            }
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
    func modifiedList(_ nums: [Int], _ head: ListNode?) -> ListNode? {
        var removeSet = Set<Int>(nums)
        var newHead = head
        while let node = newHead, removeSet.contains(node.val) {
            newHead = node.next
        }
        guard var current = newHead else { return nil }
        while let nextNode = current.next {
            if removeSet.contains(nextNode.val) {
                current.next = nextNode.next
            } else {
                current = nextNode
            }
        }
        return newHead
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun modifiedList(nums: IntArray, head: ListNode?): ListNode? {
        val toRemove = HashSet<Int>(nums.size)
        for (v in nums) {
            toRemove.add(v)
        }

        var newHead = head
        while (newHead != null && toRemove.contains(newHead.`val`)) {
            newHead = newHead.next
        }
        if (newHead == null) return null

        var cur = newHead
        while (cur.next != null) {
            if (toRemove.contains(cur.next!!.`val`)) {
                cur.next = cur.next!!.next
            } else {
                cur = cur.next!!
            }
        }
        return newHead
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
  ListNode? modifiedList(List<int> nums, ListNode? head) {
    final Set<int> toRemove = nums.toSet();

    // Remove leading nodes that need deletion
    while (head != null && toRemove.contains(head.val)) {
      head = head.next;
    }

    if (head == null) return null;

    ListNode? cur = head;
    while (cur?.next != null) {
      if (toRemove.contains(cur!.next!.val)) {
        cur.next = cur.next!.next; // skip the node to be removed
      } else {
        cur = cur.next!;
      }
    }

    return head;
  }
}
```

## Golang

```go
func modifiedList(nums []int, head *ListNode) *ListNode {
	// Build a set of values to remove.
	toRemove := make(map[int]struct{}, len(nums))
	for _, v := range nums {
		toRemove[v] = struct{}{}
	}

	// Skip leading nodes that need removal.
	for head != nil {
		if _, ok := toRemove[head.Val]; ok {
			head = head.Next
		} else {
			break
		}
	}

	// Traverse the rest of the list and unlink nodes as needed.
	cur := head
	for cur != nil && cur.Next != nil {
		if _, ok := toRemove[cur.Next.Val]; ok {
			cur.Next = cur.Next.Next
		} else {
			cur = cur.Next
		}
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

def modified_list(nums, head)
  remove_set = {}
  nums.each { |v| remove_set[v] = true }

  while head && remove_set[head.val]
    head = head.next
  end

  cur = head
  while cur && cur.next
    if remove_set[cur.next.val]
      cur.next = cur.next.next
    else
      cur = cur.next
    end
  end

  head
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def modifiedList(nums: Array[Int], head: ListNode): ListNode = {
    val toRemove = mutable.HashSet[Int]()
    var idx = 0
    while (idx < nums.length) {
      toRemove.add(nums(idx))
      idx += 1
    }

    var newHead = head
    while (newHead != null && toRemove.contains(newHead.x)) {
      newHead = newHead.next
    }
    if (newHead == null) return null

    var cur = newHead
    while (cur != null && cur.next != null) {
      if (toRemove.contains(cur.next.x)) {
        cur.next = cur.next.next
      } else {
        cur = cur.next
      }
    }

    newHead
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn modified_list(nums: Vec<i32>, head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let remove_set: HashSet<i32> = nums.into_iter().collect();

        // Remove leading nodes that need to be deleted
        let mut new_head = head;
        while let Some(node) = new_head {
            if remove_set.contains(&node.val) {
                new_head = node.next;
            } else {
                new_head = Some(node);
                break;
            }
        }

        // If all nodes were removed
        let mut cur = match new_head {
            Some(ref mut h) => h,
            None => return None,
        };

        // Traverse and remove interior nodes
        loop {
            match cur.next.take() {
                Some(mut nxt) => {
                    if remove_set.contains(&nxt.val) {
                        // Skip the node to be removed
                        cur.next = nxt.next.take();
                        // stay on current node
                    } else {
                        // Keep the node and move forward
                        let next_ref = &mut nxt;
                        cur.next = Some(nxt);
                        cur = cur.next.as_mut().unwrap();
                    }
                }
                None => break,
            }
        }

        new_head
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
(struct list-node (val next) #:mutable #:transparent)

(define/contract (modified-list nums head)
  (-> (listof exact-integer?) (or/c list-node? #f) (or/c list-node? #f))
  (let ([remove-set (make-hash)])
    (for-each (lambda (n) (hash-set! remove-set n #t)) nums)

    ;; Skip leading nodes that need to be removed
    (define new-head
      (let loop ((h head))
        (if (and h (hash-has-key? remove-set (list-node-val h)))
            (loop (list-node-next h))
            h)))

    ;; Remove interior nodes
    (when new-head
      (let loop ((cur new-head))
        (define nxt (list-node-next cur))
        (when nxt
          (if (hash-has-key? remove-set (list-node-val nxt))
              (begin
                (set-list-node-next! cur (list-node-next nxt))
                (loop cur)) ; stay on cur after removal
              (loop nxt)))))

    new-head))
```

## Erlang

```erlang
-record(list_node, {val = 0 :: integer(),
                     next = null :: 'null' | #list_node{}}).

-export([modified_list/2]).

-spec modified_list(Nums :: [integer()], Head :: #list_node{} | null) -> #list_node{} | null.
modified_list(Nums, Head) ->
    RemoveMap = maps:from_list([{N, true} || N <- Nums]),
    NewHead = skip_head(Head, RemoveMap),
    case NewHead of
        null -> null;
        _ -> rebuild(NewHead, RemoveMap)
    end.

skip_head(null, _) -> 
    null;
skip_head(Node, Map) when maps:is_key(Node#list_node.val, Map) ->
    skip_head(Node#list_node.next, Map);
skip_head(Node, _) ->
    Node.

rebuild(Node, Map) ->
    Next = Node#list_node.next,
    case Next of
        null -> 
            Node;
        _ ->
            if maps:is_key(Next#list_node.val, Map) ->
                    % skip the next node
                    NewNode = Node#list_node{next = Next#list_node.next},
                    rebuild(NewNode, Map);
               true ->
                    UpdatedNext = rebuild(Next, Map),
                    Node#list_node{next = UpdatedNext}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec modified_list(nums :: [integer], head :: ListNode.t | nil) :: ListNode.t | nil
  def modified_list(nums, head) do
    set = MapSet.new(nums)

    rev_head =
      Enum.reduce_while(
        Stream.unfold(head, fn
          nil -> nil
          node -> {node, node.next}
        end),
        nil,
        fn node, acc ->
          if MapSet.member?(set, node.val) do
            {:cont, acc}
          else
            {:cont, %ListNode{val: node.val, next: acc}}
          end
        end
      )

    Enum.reduce_while(
      Stream.unfold(rev_head, fn
        nil -> nil
        node -> {node, node.next}
      end),
      nil,
      fn node, acc ->
        {:cont, %ListNode{val: node.val, next: acc}}
      end
    )
  end
end
```
