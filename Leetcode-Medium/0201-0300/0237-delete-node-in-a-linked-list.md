# 0237. Delete Node in a Linked List

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode* nxt = node->next;
        node->val = nxt->val;
        node->next = nxt->next;
        // Optional: delete nxt; // not required by problem
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
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // Since the node to be deleted is not the tail,
        // we can copy the value from its next node and bypass it.
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## Python3

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
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
void deleteNode(struct ListNode* node) {
    if (!node || !node->next) return;  // safety check, though problem guarantees non-tail
    struct ListNode* nxt = node->next;
    node->val = nxt->val;
    node->next = nxt->next;
    /* Optional: free the removed node to avoid memory leak */
    // free(nxt);
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void DeleteNode(ListNode node) {
        if (node == null || node.next == null) return;
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void}
 */
var deleteNode = function(node) {
    if (!node || !node.next) return;
    node.val = node.next.val;
    node.next = node.next.next;
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

/**
 * Do not return anything, modify it in-place instead.
 */
function deleteNode(node: ListNode | null): void {
    if (node && node.next) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```

## Php

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {
    /**
     * @param ListNode $node
     * @return void
     */
    function deleteNode($node) {
        if ($node === null || $node->next === null) {
            return;
        }
        $node->val = $node->next->val;
        $node->next = $node->next->next;
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
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func deleteNode(_ node: ListNode?) {
        guard let node = node, let next = node.next else { return }
        node.val = next.val
        node.next = next.next
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
    fun deleteNode(node: ListNode?) {
        if (node == null) return
        val nxt = node.next ?: return
        node.`val` = nxt.`val`
        node.next = nxt.next
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
func deleteNode(node *ListNode) {
    if node == nil || node.Next == nil {
        return
    }
    node.Val = node.Next.Val
    node.Next = node.Next.Next
}
```

## Ruby

```ruby
def delete_node(node)
  return if node.nil? || node.next.nil?
  node.val = node.next.val
  node.next = node.next.next
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(var _x: Int = 0) {
 *   var next: ListNode = null
 *   var x: Int = _x
 * }
 */

object Solution {
    def deleteNode(node: ListNode): Unit = {
        val nxt = node.next
        if (nxt != null) {
            node.x = nxt.x
            node.next = nxt.next
        }
    }
}
```
