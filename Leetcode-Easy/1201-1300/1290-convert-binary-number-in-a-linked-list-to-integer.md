# 1290. Convert Binary Number in a Linked List to Integer

## Cpp

```cpp
/ **
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
    int getDecimalValue(ListNode* head) {
        int result = 0;
        while (head) {
            result = (result << 1) | head->val;
            head = head->next;
        }
        return result;
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
    public int getDecimalValue(ListNode head) {
        int result = 0;
        while (head != null) {
            result = (result << 1) | head.val;
            head = head.next;
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
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num
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
    def getDecimalValue(self, head: Optional['ListNode']) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num
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
int getDecimalValue(struct ListNode* head) {
    int result = 0;
    while (head) {
        result = (result << 1) | head->val;
        head = head->next;
    }
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
    public int GetDecimalValue(ListNode head) {
        int result = 0;
        while (head != null) {
            result = (result << 1) | head.val;
            head = head.next;
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
 * @return {number}
 */
var getDecimalValue = function(head) {
    let num = 0;
    while (head !== null) {
        num = (num << 1) | head.val;
        head = head.next;
    }
    return num;
};
```

## Typescript

```typescript
function getDecimalValue(head: ListNode | null): number {
    let num = 0;
    while (head !== null) {
        num = (num << 1) | head.val;
        head = head.next;
    }
    return num;
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
     * @return int
     */
    function getDecimalValue($head) {
        $num = 0;
        while ($head !== null) {
            $num = ($num << 1) | $head->val;
            $head = $head->next;
        }
        return $num;
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
    func getDecimalValue(_ head: ListNode?) -> Int {
        var result = 0
        var node = head
        while let current = node {
            result = (result << 1) | current.val
            node = current.next
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getDecimalValue(head: ListNode?): Int {
        var result = 0
        var current = head
        while (current != null) {
            result = (result shl 1) or current.`val`
            current = current.next
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
  int getDecimalValue(ListNode? head) {
    int result = 0;
    while (head != null) {
      result = (result << 1) | head.val;
      head = head.next;
    }
    return result;
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
func getDecimalValue(head *ListNode) int {
    result := 0
    for ; head != nil; head = head.Next {
        result = (result << 1) | head.Val
    }
    return result
}
```

## Ruby

```ruby
def get_decimal_value(head)
  num = 0
  while head
    num = (num << 1) | head.val
    head = head.next
  end
  num
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
    def getDecimalValue(head: ListNode): Int = {
        var result = 0
        var node = head
        while (node != null) {
            result = (result << 1) | node.x
            node = node.next
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut result = 0i32;
        let mut cur = head.as_ref();
        while let Some(node) = cur {
            result = (result << 1) | node.val;
            cur = node.next.as_ref();
        }
        result
    }
}
```

## Racket

```racket
(define/contract (get-decimal-value head)
  (-> (or/c list-node? #f) exact-integer?)
  (let loop ((node head) (acc 0))
    (if (not node)
        acc
        (loop (list-node-next node)
              (+ (arithmetic-shift acc 1) (list-node-val node))))))
```

## Erlang

```erlang
%% Definition for singly-linked list.
%%
%% -record(list_node, {val = 0 :: integer(),
%%                     next = null :: 'null' | #list_node{}}).

-spec get_decimal_value(Head :: #list_node{} | null) -> integer().
get_decimal_value(Head) ->
    get_decimal_value(Head, 0).

get_decimal_value(null, Acc) ->
    Acc;
get_decimal_value(#list_node{val = Val, next = Next}, Acc) ->
    NewAcc = (Acc bsl 1) bor Val,
    get_decimal_value(Next, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec get_decimal_value(head :: ListNode.t | nil) :: integer
  def get_decimal_value(head) do
    traverse(head, 0)
  end

  defp traverse(nil, acc), do: acc

  defp traverse(%ListNode{val: v, next: nxt}, acc) do
    traverse(nxt, (acc <<< 1) ||| v)
  end
end
```
