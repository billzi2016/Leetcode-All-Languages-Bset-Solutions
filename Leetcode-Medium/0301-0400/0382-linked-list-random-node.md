# 0382. Linked List Random Node

## Cpp

```cpp
#include <cstdlib>
#include <chrono>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    ListNode* head_;
public:
    Solution(ListNode* head) : head_(head) {
        srand(static_cast<unsigned>(std::chrono::high_resolution_clock::now().time_since_epoch().count()));
    }
    
    int getRandom() {
        int result = 0;
        ListNode* cur = head_;
        int n = 0;
        while (cur) {
            ++n;
            if (rand() % n == 0) {
                result = cur->val;
            }
            cur = cur->next;
        }
        return result;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
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
import java.util.Random;

class Solution {
    private final ListNode head;
    private final Random rand;

    public Solution(ListNode head) {
        this.head = head;
        this.rand = new Random();
    }

    public int getRandom() {
        int result = -1;
        ListNode node = head;
        int i = 0;
        while (node != null) {
            i++;
            // rand.nextInt(i) returns a value in [0, i-1]
            if (rand.nextInt(i) == 0) {
                result = node.val;
            }
            node = node.next;
        }
        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```

## Python

```python
import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        node = self.head
        result = None
        i = 0
        while node:
            i += 1
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next
        return result
```

## Python3

```python
from typing import Optional
import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: Optional['ListNode']):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        result = None
        i = 0
        while node:
            i += 1
            if random.randint(1, i) == i:
                result = node.val
            node = node.next
        return result
```

## C

```c
#include <stdlib.h>
#include <time.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct {
    struct ListNode* head;
} Solution;

Solution* solutionCreate(struct ListNode* head) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->head = head;
    /* Seed the random number generator once */
    static int seeded = 0;
    if (!seeded) {
        srand((unsigned)time(NULL));
        seeded = 1;
    }
    return obj;
}

int solutionGetRandom(Solution* obj) {
    int result = -1;
    struct ListNode* node = obj->head;
    int i = 0;
    while (node) {
        if (rand() % (i + 1) == 0) {
            result = node->val;
        }
        node = node->next;
        ++i;
    }
    return result;
}

void solutionFree(Solution* obj) {
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(head);
 * int param_1 = solutionGetRandom(obj);
 * solutionFree(obj);
 */
```

## Csharp

```csharp
using System;

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
    private readonly ListNode _head;
    private readonly Random _rand;

    public Solution(ListNode head)
    {
        _head = head;
        _rand = new Random();
    }

    public int GetRandom()
    {
        int result = _head.val;
        ListNode node = _head.next;
        int i = 2; // current index (1-based)

        while (node != null)
        {
            // With probability 1/i, replace the result with current node's value
            if (_rand.Next(i) == 0)
                result = node.val;

            node = node.next;
            i++;
        }

        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.GetRandom();
 */
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
 */
var Solution = function(head) {
    this.head = head;
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    let result = null;
    let node = this.head;
    let i = 1;
    while (node !== null) {
        // With probability 1/i, replace the result with current node's value
        if (Math.floor(Math.random() * i) === 0) {
            result = node.val;
        }
        node = node.next;
        i++;
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

class Solution {
    private head: ListNode | null;
    constructor(head: ListNode | null) {
        this.head = head;
    }

    getRandom(): number {
        let result = 0;
        let node = this.head;
        let i = 0;
        while (node !== null) {
            i++;
            if (Math.random() < 1 / i) {
                result = node.val;
            }
            node = node.next;
        }
        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
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
     * @var ListNode
     */
    private $head;

    /**
     * @param ListNode $head
     */
    function __construct($head) {
        $this->head = $head;
    }

    /**
     * @return integer
     */
    function getRandom() {
        $node = $this->head;
        $result = null;
        $i = 0;
        while ($node !== null) {
            $i++;
            // Reservoir sampling: replace result with current node's value with probability 1/i
            if (mt_rand(1, $i) === 1) {
                $result = $node->val;
            }
            $node = $node->next;
        }
        return $result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = new Solution($head);
 * $ret_1 = $obj->getRandom();
 */
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
    private var head: ListNode?
    
    init(_ head: ListNode?) {
        self.head = head
    }
    
    func getRandom() -> Int {
        var result = 0
        var node = head
        var i = 1
        while let current = node {
            if Int.random(in: 1...i) == 1 {
                result = current.val
            }
            i += 1
            node = current.next
        }
        return result
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(head)
 * let ret_1: Int = obj.getRandom()
 */
```

## Kotlin

```kotlin
/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution(head: ListNode?) {

    private val head: ListNode? = head
    private val rand = java.util.Random()

    fun getRandom(): Int {
        var result = 0
        var node = head
        var i = 1
        while (node != null) {
            if (rand.nextInt(i) == 0) {
                result = node.`val`
            }
            node = node.next
            i++
        }
        return result
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(head)
 * var param_1 = obj.getRandom()
 */
```

## Dart

```dart
import 'dart:math';

/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  final ListNode? _head;
  final Random _rand = Random();

  Solution(ListNode? head) : _head = head;

  int getRandom() {
    int result = 0;
    int i = 0;
    for (ListNode? node = _head; node != null; node = node.next) {
      i++;
      if (_rand.nextInt(i) == 0) {
        result = node.val;
      }
    }
    return result;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(head);
 * int param1 = obj.getRandom();
 */
```

## Golang

```go
import (
	"math/rand"
	"time"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type Solution struct {
	head *ListNode
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func Constructor(head *ListNode) Solution {
	return Solution{head: head}
}

func (this *Solution) GetRandom() int {
	var result int
	curr := this.head
	i := 1
	for curr != nil {
		if rand.Intn(i) == 0 {
			result = curr.Val
		}
		curr = curr.Next
		i++
	}
	return result
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
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
class Solution

=begin
    :type head: ListNode
=end
    def initialize(head)
        @head = head
    end


=begin
    :rtype: Integer
=end
    def get_random()
        cur = @head
        result = nil
        i = 0
        while cur
            i += 1
            # rand(i) returns integer in [0, i-1]; select when it is 0
            result = cur.val if rand(i) == 0
            cur = cur.next
        end
        result
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(head)
# param_1 = obj.get_random()
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
class Solution(_head: ListNode) {

  private val head: ListNode = _head
  private val rand = new java.util.Random()

  def getRandom(): Int = {
    var result = 0
    var node = head
    var i = 1
    while (node != null) {
      if (rand.nextInt(i) == 0) {
        result = node.x
      }
      node = node.next
      i += 1
    }
    result
  }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(head)
 * val param_1 = obj.getRandom()
 */
```

## Rust

```rust
extern crate rand;
use rand::Rng;

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

struct Solution {
    vals: Vec<i32>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(head: Option<Box<ListNode>>) -> Self {
        let mut vals = Vec::new();
        let mut cur = &head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = &node.next;
        }
        Solution { vals }
    }
    
    fn get_random(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let idx = rng.gen_range(0..self.vals.len());
        self.vals[idx]
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(head);
 * let ret_1: i32 = obj.get_random();
 */
```

## Racket

```racket
; Definition for singly-linked list:
#|
; val : integer?
; next : (or/c list-node? #f)
(struct list-node
  (val next) #:mutable #:transparent)

; constructor
(define (make-list-node [val 0])
  (list-node val #f))
|#

(define solution%
  (class object%
    (super-new)
    
    ; head : (or/c list-node? #f)
    (init-field head)
    
    ; get-random : -> exact-integer?
    (define/public (get-random)
      (let loop ((node head) (i 0) (result #f))
        (if (not node)
            result
            (let* ((new-i (+ i 1))
                   (new-result (if (= (random new-i) 0)
                                   (list-node-val node)
                                   result)))
              (loop (list-node-next node) new-i new-result)))))))
```

## Erlang

```erlang
-module(solution).
-export([solution_init_/1, solution_get_random/0]).

%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec solution_init_(Head :: #list_node{} | null) -> any().
solution_init_(Head) ->
    put(head, Head),
    Seed = {erlang:phash2(self()), erlang:unique_integer([positive]), erlang:system_time()},
    rand:seed(exsplus, Seed).

-spec solution_get_random() -> integer().
solution_get_random() ->
    Head = get(head),
    reservoir(Head, 0, 0).

reservoir(null, _Count, Result) ->
    Result;
reservoir(Node, Count, Result) ->
    NewCount = Count + 1,
    NewResult =
        case rand:uniform(NewCount) of
            1 -> Node#list_node.val;
            _ -> Result
        end,
    reservoir(Node#list_node.next, NewCount, NewResult).
```

## Elixir

```elixir
defmodule ListNode do
  @type t :: %__MODULE__{
          val: integer,
          next: ListNode.t() | nil
        }
  defstruct val: 0, next: nil
end

defmodule Solution do
  @spec init_(head :: ListNode.t() | nil) :: any
  def init_(head) do
    vals = collect(head, [])
    Process.put(:list_vals, vals)
  end

  @spec get_random() :: integer
  def get_random() do
    vals = Process.get(:list_vals, [])
    len = length(vals)
    idx = :rand.uniform(len) - 1
    Enum.at(vals, idx)
  end

  defp collect(nil, acc), do: Enum.reverse(acc)

  defp collect(%ListNode{val: v, next: nxt}, acc) do
    collect(nxt, [v | acc])
  end
end
```
