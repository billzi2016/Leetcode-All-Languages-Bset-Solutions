# 0138. Copy List with Random Pointer

## Cpp

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        
        // 1. Interweave copied nodes with original nodes
        for (Node* cur = head; cur; cur = cur->next->next) {
            Node* copy = new Node(cur->val);
            copy->next = cur->next;
            cur->next = copy;
        }
        
        // 2. Assign random pointers to copied nodes
        for (Node* cur = head; cur; cur = cur->next->next) {
            if (cur->random)
                cur->next->random = cur->random->next;
            else
                cur->next->random = nullptr;
        }
        
        // 3. Separate the interleaved lists into original and copied lists
        Node* dummy = new Node(0);
        Node* copyCur = dummy;
        for (Node* cur = head; cur; ) {
            Node* copy = cur->next;
            copyCur->next = copy;
            copyCur = copy;
            
            cur->next = copy->next;
            cur = cur->next;
        }
        
        return dummy->next;
    }
};
```

## Java

```java
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;

        // 1. Interleave copied nodes with original nodes
        Node cur = head;
        while (cur != null) {
            Node copy = new Node(cur.val);
            copy.next = cur.next;
            cur.next = copy;
            cur = copy.next;
        }

        // 2. Assign random pointers for the copies
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        // 3. Separate the copied list from the interleaved list
        Node dummy = new Node(0);
        Node copyCur = dummy;
        cur = head;
        while (cur != null) {
            Node copy = cur.next;
            // restore original next
            cur.next = copy.next;
            // append copy to result list
            copyCur.next = copy;
            copyCur = copyCur.next;

            cur = cur.next;
        }

        return dummy.next;
    }
}
```

## Python

```python
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # First pass: interleave copied nodes with original nodes
        cur = head
        while cur:
            copy_node = Node(cur.val)
            copy_node.next = cur.next
            cur.next = copy_node
            cur = copy_node.next

        # Second pass: assign random pointers for the copies
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Third pass: separate the copied list from the original list
        cur_original = head
        copy_head = head.next
        cur_copy = copy_head
        while cur_original:
            cur_original.next = cur_original.next.next
            if cur_copy.next:
                cur_copy.next = cur_copy.next.next
            else:
                cur_copy.next = None
            cur_original = cur_original.next
            cur_copy = cur_copy.next

        return copy_head
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Interleave copied nodes with original nodes.
        cur = head
        while cur:
            nxt = cur.next
            copy_node = Node(cur.val)
            cur.next = copy_node
            copy_node.next = nxt
            cur = nxt

        # 2. Assign random pointers for the copied nodes.
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 3. Separate the interleaved list into original and copied lists.
        cur = head
        copy_head = head.next
        while cur:
            copy_node = cur.next
            nxt = copy_node.next
            cur.next = nxt
            copy_node.next = nxt.next if nxt else None
            cur = nxt

        return copy_head
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *next;
 *     struct Node *random;
 * };
 */

struct Node* copyRandomList(struct Node* head) {
    if (!head) return NULL;

    // First pass: create copied nodes interleaved with original nodes
    struct Node* cur = head;
    while (cur) {
        struct Node* copy = (struct Node*)malloc(sizeof(struct Node));
        copy->val = cur->val;
        copy->next = cur->next;
        copy->random = NULL;
        cur->next = copy;
        cur = copy->next;
    }

    // Second pass: assign random pointers for the copied nodes
    cur = head;
    while (cur) {
        if (cur->random)
            cur->next->random = cur->random->next;
        else
            cur->next->random = NULL;
        cur = cur->next->next;
    }

    // Third pass: separate the interleaved lists into original and copied lists
    struct Node dummy;          // temporary dummy node for the new list
    dummy.next = NULL;
    struct Node* copyPrev = &dummy;

    cur = head;
    while (cur) {
        struct Node* copy = cur->next;
        cur->next = copy->next;           // restore original next pointer
        copyPrev->next = copy;            // append copy to new list
        copyPrev = copy;
        cur = cur->next;
    }

    return dummy.next;
}
```

## Csharp

```csharp
/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node CopyRandomList(Node head) {
        if (head == null) return null;

        // 1. Interleave copied nodes with original nodes
        Node cur = head;
        while (cur != null) {
            Node copy = new Node(cur.val);
            copy.next = cur.next;
            cur.next = copy;
            cur = copy.next;
        }

        // 2. Assign random pointers for the copies
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        // 3. Separate the copied list from the interleaved list
        Node dummyHead = new Node(0);
        Node copyCur = dummyHead;
        cur = head;
        while (cur != null) {
            Node copy = cur.next;
            // restore original next
            cur.next = copy.next;
            // append copy to result list
            copyCur.next = copy;
            copyCur = copyCur.next;

            cur = cur.next;
        }

        return dummyHead.next;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {
    if (!head) return null;

    // 1. Interweave copied nodes with original nodes
    let cur = head;
    while (cur) {
        const copy = new _Node(cur.val, null, null);
        copy.next = cur.next;
        cur.next = copy;
        cur = copy.next;
    }

    // 2. Assign random pointers for the copies
    cur = head;
    while (cur) {
        if (cur.random) {
            cur.next.random = cur.random.next;
        }
        cur = cur.next.next;
    }

    // 3. Separate the copied list from the original list
    const pseudoHead = new _Node(0, null, null);
    let copyIter = pseudoHead;
    cur = head;
    while (cur) {
        const copy = cur.next;
        copyIter.next = copy;
        copyIter = copy;

        // restore original next pointer
        cur.next = copy.next;
        cur = cur.next;
    }

    return pseudoHead.next;
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     next: _Node | null
 *     random: _Node | null
 *
 *     constructor(val?: number, next?: _Node, random?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */

function copyRandomList(head: _Node | null): _Node | null {
    if (!head) return null;

    // 1. Interleave copied nodes with original nodes
    let cur: _Node | null = head;
    while (cur) {
        const copy = new _Node(cur.val);
        copy.next = cur.next;
        cur.next = copy;
        cur = copy.next;
    }

    // 2. Assign random pointers for the copies
    cur = head;
    while (cur) {
        if (cur.random) {
            cur.next!.random = cur.random.next;
        } else {
            cur.next!.random = null;
        }
        cur = cur.next!.next;
    }

    // 3. Separate the copied list from the interleaved list
    const pseudoHead = new _Node(0);
    let copyCur: _Node | null = pseudoHead;
    cur = head;
    while (cur) {
        const copy = cur.next!;
        // restore original next pointer
        cur.next = copy.next;
        // append copy to the result list
        copyCur!.next = copy;
        copyCur = copy;
        cur = cur.next;
    }

    return pseudoHead.next;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $next = null;
 *     public $random = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->next = null;
 *         $this->random = null;
 *     }
 * }
 */

class Solution {
    /**
     * @param Node $head
     * @return Node
     */
    function copyRandomList($head) {
        if ($head === null) {
            return null;
        }

        // 1. Clone nodes and interweave with original list
        $curr = $head;
        while ($curr !== null) {
            $clone = new Node($curr->val);
            $clone->next = $curr->next;
            $curr->next = $clone;
            $curr = $clone->next;
        }

        // 2. Assign random pointers for cloned nodes
        $curr = $head;
        while ($curr !== null) {
            if ($curr->random !== null) {
                $curr->next->random = $curr->random->next;
            }
            $curr = $curr->next->next;
        }

        // 3. Separate the cloned list from the original list
        $orig = $head;
        $cloneHead = $head->next;
        while ($orig !== null) {
            $clone = $orig->next;
            $orig->next = $clone->next;
            if ($clone->next !== null) {
                $clone->next = $clone->next->next;
            }
            $orig = $orig->next;
        }

        return $cloneHead;
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var next: Node?
 *     public var random: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *         self.random = nil
 *     }
 * }
 */

class Solution {
    func copyRandomList(_ head: Node?) -> Node? {
        guard let _ = head else { return nil }
        
        // 1. Interleave copied nodes with original nodes
        var cur = head
        while let node = cur {
            let copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            cur = copy.next
        }
        
        // 2. Assign random pointers for the copies
        cur = head
        while let node = cur {
            if let rand = node.random {
                node.next?.random = rand.next
            }
            cur = node.next?.next
        }
        
        // 3. Separate the copied list from the interleaved list
        let dummy = Node(0)
        var copyCur: Node? = dummy
        cur = head
        while let node = cur {
            let copy = node.next!
            // restore original next pointer
            node.next = copy.next
            // append copy to new list
            copyCur?.next = copy
            copyCur = copy
            cur = node.next
        }
        
        return dummy.next
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var next: Node? = null
 *     var random: Node? = null
 * }
 */
class Solution {
    fun copyRandomList(head: Node?): Node? {
        if (head == null) return null

        // 1. Interweave copied nodes with original nodes
        var cur = head
        while (cur != null) {
            val copy = Node(cur.`val`)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next
        }

        // 2. Assign random pointers for the copies
        cur = head
        while (cur != null) {
            if (cur.random != null) {
                cur.next!!.random = cur.random!!.next
            }
            cur = cur.next!!.next
        }

        // 3. Separate the copied list from the original list
        val pseudoHead = Node(0)
        var copyIter: Node? = pseudoHead
        cur = head
        while (cur != null) {
            val copy = cur.next!!
            copyIter?.next = copy
            copyIter = copy

            // restore original next pointer
            cur.next = copy.next
            cur = cur.next
        }

        return pseudoHead.next
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	// 1. Interleave copied nodes with original nodes.
	for cur := head; cur != nil; {
		copyNode := &Node{Val: cur.Val}
		copyNode.Next = cur.Next
		cur.Next = copyNode
		cur = copyNode.Next
	}
	// 2. Assign random pointers for the copied nodes.
	for cur := head; cur != nil; cur = cur.Next.Next {
		if cur.Random != nil {
			cur.Next.Random = cur.Random.Next
		} else {
			cur.Next.Random = nil
		}
	}
	// 3. Separate the interleaved list into original and copied lists.
	dummy := &Node{}
	copyIter := dummy
	for cur := head; cur != nil; {
		copyNode := cur.Next
		copyIter.Next = copyNode
		copyIter = copyNode

		cur.Next = copyNode.Next
		cur = cur.Next
	}
	return dummy.Next
}
```

## Ruby

```ruby
# Definition for Node.
# class Node
#   attr_accessor :val, :next, :random
#   def initialize(val = 0)
#     @val = val
#     @next = nil
#     @random = nil
#   end
# end

def copyRandomList(head)
  return nil if head.nil?

  # First pass: interleave copied nodes with original nodes
  cur = head
  while cur
    copy = Node.new(cur.val)
    copy.next = cur.next
    cur.next = copy
    cur = copy.next
  end

  # Second pass: assign random pointers for the copies
  cur = head
  while cur
    copy = cur.next
    copy.random = cur.random ? cur.random.next : nil
    cur = copy.next
  end

  # Third pass: separate the interleaved lists
  dummy = Node.new(0)
  copy_cur = dummy
  cur = head
  while cur
    copy = cur.next
    next_orig = copy.next

    # restore original list's next pointer
    cur.next = next_orig

    # append copy to new list
    copy_cur.next = copy
    copy_cur = copy

    cur = next_orig
  end

  dummy.next
end
```

## Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var next: Node = null
 *   var random: Node = null
 * }
 */

object Solution {
  def copyRandomList(head: Node): Node = {
    if (head == null) return null

    // Step 1: Interleave copied nodes with original nodes
    var cur = head
    while (cur != null) {
      val copy = new Node(cur.value)
      copy.next = cur.next
      cur.next = copy
      cur = copy.next
    }

    // Step 2: Assign random pointers for the copied nodes
    cur = head
    while (cur != null) {
      if (cur.random != null) {
        cur.next.random = cur.random.next
      }
      cur = cur.next.next
    }

    // Step 3: Separate the interleaved list into original and copied lists
    var oldNode = head
    val newHead = head.next
    while (oldNode != null) {
      val copyNode = oldNode.next
      oldNode.next = copyNode.next
      if (copyNode.next != null) {
        copyNode.next = copyNode.next.next
      }
      oldNode = oldNode.next
    }

    newHead
  }
}
```
