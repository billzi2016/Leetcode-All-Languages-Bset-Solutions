# 0430. Flatten a Multilevel Doubly Linked List

## Cpp

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

#include <stack>

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) return nullptr;
        std::stack<Node*> st;
        st.push(head);
        Node* prev = nullptr;
        
        while (!st.empty()) {
            Node* cur = st.top();
            st.pop();
            
            if (prev) {
                prev->next = cur;
                cur->prev = prev;
            }
            
            // Push next first so that child is processed before next
            if (cur->next) st.push(cur->next);
            if (cur->child) {
                st.push(cur->child);
                cur->child = nullptr;
            }
            
            prev = cur;
        }
        return head;
    }
};
```

## Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public Node flatten(Node head) {
        if (head == null) return null;
        Deque<Node> stack = new ArrayDeque<>();
        Node curr = head;
        while (curr != null) {
            if (curr.child != null) {
                if (curr.next != null) {
                    stack.push(curr.next);
                }
                curr.next = curr.child;
                curr.next.prev = curr;
                curr.child = null;
            } else if (curr.next == null && !stack.isEmpty()) {
                Node nxt = stack.pop();
                curr.next = nxt;
                nxt.prev = curr;
            }
            curr = curr.next;
        }
        return head;
    }
}
```

## Python

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        dummy = Node(0, None, None, None)
        stack = [head]
        prev = dummy

        while stack:
            curr = stack.pop()
            # link current node with the previous one
            prev.next = curr
            curr.prev = prev

            # if there is a next node, push it first so that child nodes are processed before it
            if curr.next:
                stack.append(curr.next)

            # if there is a child, push it onto the stack and nullify the child pointer
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        # detach dummy node
        real_head = dummy.next
        if real_head:
            real_head.prev = None
        return real_head
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        stack = [head]
        prev = None

        while stack:
            node = stack.pop()

            if prev:
                prev.next = node
                node.prev = prev

            # If there is a next node, push it first so that child is processed before it.
            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None  # detach child after pushing

            prev = node

        return head
```

## Csharp

```csharp
/*
// Definition for a Node.
public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
}
*/

using System.Collections.Generic;

public class Solution {
    public Node Flatten(Node head) {
        if (head == null) return null;

        var stack = new Stack<Node>();
        stack.Push(head);
        Node prev = null;

        while (stack.Count > 0) {
            Node curr = stack.Pop();

            if (prev != null) {
                prev.next = curr;
                curr.prev = prev;
            }

            // If there is a next node, push it first so that child nodes are processed before it.
            if (curr.next != null) {
                stack.Push(curr.next);
            }

            // If there is a child, push it onto the stack and detach it.
            if (curr.child != null) {
                stack.Push(curr.child);
                curr.child = null;
            }

            prev = curr;
        }

        // Ensure the head's prev pointer is null (it may have been set during processing).
        head.prev = null;
        return head;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val,prev,next,child) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 *    this.child = child;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var flatten = function(head) {
    if (!head) return null;

    const dummy = new _Node(0, null, head, null);
    let prev = dummy;
    const stack = [head];

    while (stack.length) {
        const node = stack.pop();

        // link current node with previous
        prev.next = node;
        node.prev = prev;

        // if there is a next node, push it to stack (to be processed after child)
        if (node.next) {
            stack.push(node.next);
        }

        // if there is a child, push it and nullify the child pointer
        if (node.child) {
            stack.push(node.child);
            node.child = null;
        }

        prev = node;
    }

    // detach dummy head
    const realHead = dummy.next;
    if (realHead) realHead.prev = null;
    return realHead;
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     prev: _Node | null
 *     next: _Node | null
 *     child: _Node | null
 *     
 *     constructor(val?: number, prev? : _Node, next? : _Node, child? : _Node) {
 *         this.val = (val===undefined ? 0 : val);
 *         this.prev = (prev===undefined ? null : prev);
 *         this.next = (next===undefined ? null : next);
 *         this.child = (child===undefined ? null : child);
 *     }
 * }
 */

function flatten(head: _Node | null): _Node | null {
    if (!head) return null;

    const dummy = new _Node(0);
    let prev: _Node = dummy;
    const stack: (_Node)[] = [];
    stack.push(head);

    while (stack.length > 0) {
        const curr = stack.pop()!; // non-null

        // connect current node with the previous one
        prev.next = curr;
        curr.prev = prev;

        // if there is a next node, push it to process later
        if (curr.next) {
            stack.push(curr.next);
        }

        // if there is a child, push it to process before the next node
        if (curr.child) {
            stack.push(curr.child);
            curr.child = null; // clear child pointer as required
        }

        prev = curr;
    }

    // detach dummy head
    const realHead = dummy.next!;
    realHead.prev = null;
    return realHead;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $prev = null;
 *     public $next = null;
 *     public $child = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->prev = null;
 *         $this->next = null;
 *         $this->child = null;
 *     }
 * }
 */

class Solution {
    /**
     * @param Node $head
     * @return Node
     */
    function flatten($head) {
        if ($head === null) {
            return null;
        }

        $stack = [];
        $curr = $head;

        while ($curr !== null) {
            if ($curr->child !== null) {
                // If there is a next node, push it onto the stack
                if ($curr->next !== null) {
                    array_push($stack, $curr->next);
                }
                // Connect child as the next node
                $curr->next = $curr->child;
                $curr->next->prev = $curr;
                $curr->child = null;
            } elseif ($curr->next === null && !empty($stack)) {
                // No next node, pop from stack and continue
                $node = array_pop($stack);
                $curr->next = $node;
                $node->prev = $curr;
            }
            $curr = $curr->next;
        }

        return $head;
    }
}
```

## Swift

```swift
class Solution {
    func flatten(_ head: Node?) -> Node? {
        guard let head = head else { return nil }
        var stack: [Node] = []
        stack.append(head)
        var prev: Node? = nil
        
        while !stack.isEmpty {
            let node = stack.removeLast()
            
            if let next = node.next {
                stack.append(next)
            }
            if let child = node.child {
                stack.append(child)
                node.child = nil
            }
            
            if let p = prev {
                p.next = node
                node.prev = p
            } else {
                node.prev = nil
            }
            prev = node
        }
        
        return head
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var prev: Node? = null
 *     var next: Node? = null
 *     var child: Node? = null
 * }
 */
class Solution {
    fun flatten(root: Node?): Node? {
        if (root == null) return null
        val dummy = Node(0)
        var prev: Node = dummy
        val stack = java.util.ArrayDeque<Node>()
        stack.push(root)

        while (!stack.isEmpty()) {
            val curr = stack.pop()
            // link current node with the previous one
            prev.next = curr
            curr.prev = prev

            // if there is a next node, push it to process later
            if (curr.next != null) {
                stack.push(curr.next)
            }
            // if there is a child, push it first to flatten before the next node
            if (curr.child != null) {
                stack.push(curr.child)
                curr.child = null
            }

            prev = curr
        }

        // detach dummy head
        val head = dummy.next
        if (head != null) {
            head.prev = null
        }
        return head
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Prev *Node
 *     Next *Node
 *     Child *Node
 * }
 */

func flatten(root *Node) *Node {
	if root == nil {
		return nil
	}
	// Dummy head to simplify prev handling
	dummy := &Node{Val: 0, Next: root}
	root.Prev = dummy

	stack := []*Node{}
	cur := root

	for cur != nil {
		if cur.Child != nil {
			// If there is a next node, push it onto the stack for later processing
			if cur.Next != nil {
				stack = append(stack, cur.Next)
			}
			// Connect child as the next node
			cur.Next = cur.Child
			cur.Child.Prev = cur
			cur.Child = nil
		} else if cur.Next == nil && len(stack) > 0 {
			// No further nodes at this level, pop from stack
			next := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			cur.Next = next
			next.Prev = cur
		}
		cur = cur.Next
	}

	// Detach dummy head
	head := dummy.Next
	if head != nil {
		head.Prev = nil
	}
	return head
}
```

## Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :prev, :next, :child
#     def initialize(val=nil, prev=nil, next_=nil, child=nil)
#         @val = val
#         @prev = prev
#         @next = next_
#         @child = child
#     end
# end

def flatten(root)
  return nil unless root
  stack = [root]
  prev = nil
  until stack.empty?
    node = stack.pop
    if prev
      prev.next = node
      node.prev = prev
    end
    # push next first so that child is processed before it
    stack << node.next if node.next
    if node.child
      stack << node.child
      node.child = nil
    end
    prev = node
  end
  root
end
```

## Scala

```scala
/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var prev: Node = null
 *   var next: Node = null
 *   var child: Node = null
 * }
 */

object Solution {
  def flatten(head: Node): Node = {
    if (head == null) return null

    val stack = new java.util.ArrayDeque[Node]()
    var curr = head

    while (curr != null) {
      if (curr.child != null) {
        // If there is a next node, push it onto the stack
        if (curr.next != null) {
          stack.push(curr.next)
        }
        // Connect child as the next node
        val child = curr.child
        curr.next = child
        child.prev = curr
        curr.child = null
      } else if (curr.next == null && !stack.isEmpty) {
        // No next node, pop from stack and continue
        val nxt = stack.pop()
        curr.next = nxt
        nxt.prev = curr
      }
      curr = curr.next
    }

    head
  }
}
```
