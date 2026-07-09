# 0116. Populating Next Right Pointers in Each Node

## Cpp

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        Node* levelStart = root;
        while (levelStart->left) {
            Node* cur = levelStart;
            while (cur) {
                cur->left->next = cur->right;
                if (cur->next) {
                    cur->right->next = cur->next->left;
                }
                cur = cur->next;
            }
            levelStart = levelStart->left;
        }
        return root;
    }
};
```

## Java

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Node levelStart = root;
        while (levelStart.left != null) {
            Node cur = levelStart;
            while (cur != null) {
                // Connect left child to right child
                cur.left.next = cur.right;
                // Connect right child to next node's left child, if exists
                if (cur.next != null) {
                    cur.right.next = cur.next.left;
                }
                cur = cur.next;
            }
            levelStart = levelStart.left;
        }
        return root;
    }
}
```

## Python

```python
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        # Start with the leftmost node of each level
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # Connect left child to right child
                head.left.next = head.right
                # Connect right child to next subtree's left child, if exists
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
```

## Python3

```python
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
```

## C

```c
/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *left;
 *     struct Node *right;
 *     struct Node *next;
 * };
 */

struct Node* connect(struct Node* root) {
    if (!root) return NULL;
    struct Node *leftmost = root;
    while (leftmost->left) {
        struct Node *head = leftmost;
        while (head) {
            head->left->next = head->right;
            if (head->next)
                head->right->next = head->next->left;
            head = head->next;
        }
        leftmost = leftmost->left;
    }
    return root;
}
```

## Csharp

```csharp
/*
// Definition for a Node.
public class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}
*/

public class Solution {
    public Node Connect(Node root) {
        if (root == null) return null;

        Node levelStart = root;
        while (levelStart.left != null) {
            Node cur = levelStart;
            while (cur != null) {
                // connect left child to right child
                cur.left.next = cur.right;
                // connect right child to next node's left child, if exists
                if (cur.next != null) {
                    cur.right.next = cur.next.left;
                }
                cur = cur.next;
            }
            levelStart = levelStart.left;
        }

        return root;
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a _Node.
 * function _Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {_Node} root
 * @return {_Node}
 */
var connect = function(root) {
    if (!root) return null;
    let leftmost = root;
    while (leftmost.left) {
        let head = leftmost;
        while (head) {
            head.left.next = head.right;
            if (head.next) {
                head.right.next = head.next.left;
            }
            head = head.next;
        }
        leftmost = leftmost.left;
    }
    return root;
};
```

## Typescript

```typescript
/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     left: _Node | null
 *     right: _Node | null
 *     next: _Node | null
 *     constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function connect(root: _Node | null): _Node | null {
    if (!root) return null;
    let level: _Node | null = root;
    while (level.left) {
        let cur: _Node | null = level;
        while (cur) {
            // connect left child to right child
            cur.left!.next = cur.right;
            // connect right child to next node's left child if exists
            if (cur.next) {
                cur.right!.next = cur.next.left;
            }
            cur = cur.next;
        }
        level = level.left;
    }
    return root;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val = 0;
 *     public $left = null;
 *     public $right = null;
 *     public $next = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->left = null;
 *         $this->right = null;
 *         $this->next = null;
 *     }
 * }
 */

class Solution {
    /**
     * @param Node $root
     * @return Node
     */
    public function connect($root) {
        if ($root === null) {
            return $root;
        }

        $leftmost = $root;
        while ($leftmost->left !== null) {
            $head = $leftmost;
            while ($head !== null) {
                // Connect left child to right child
                $head->left->next = $head->right;

                // Connect right child to the next node's left child, if it exists
                if ($head->next !== null) {
                    $head->right->next = $head->next->left;
                }

                $head = $head->next;
            }
            $leftmost = $leftmost->left;
        }

        return $root;
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var left: Node?
 *     public var right: Node?
 *	   public var next: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func connect(_ root: Node?) -> Node? {
        var levelStart = root
        while let start = levelStart {
            var current: Node? = start
            while let node = current {
                if let left = node.left, let right = node.right {
                    left.next = right
                    if let nextNode = node.next {
                        right.next = nextNode.left
                    }
                }
                current = node.next
            }
            levelStart = start.left
        }
        return root
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun connect(root: Node?): Node? {
        var levelStart = root
        while (levelStart?.left != null) {
            var cur = levelStart
            while (cur != null) {
                cur.left?.next = cur.right
                if (cur.next != null) {
                    cur.right?.next = cur.next!!.left
                }
                cur = cur.next
            }
            levelStart = levelStart.left
        }
        return root
    }
}
```

## Golang

```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	for leftmost := root; leftmost.Left != nil; leftmost = leftmost.Left {
		cur := leftmost
		for cur != nil {
			cur.Left.Next = cur.Right
			if cur.Next != nil {
				cur.Right.Next = cur.Next.Left
			}
			cur = cur.Next
		}
	}
	return root
}
```

## Ruby

```ruby
# Definition for Node.
# class Node
#     attr_accessor :val, :left, :right, :next
#     def initialize(val)
#         @val = val
#         @left, @right, @next = nil, nil, nil
#     end
# end

# @param {Node} root
# @return {Node}
def connect(root)
  return nil unless root
  leftmost = root
  while leftmost.left
    head = leftmost
    while head
      head.left.next = head.right
      head.right.next = head.next.left if head.next
      head = head.next
    end
    leftmost = leftmost.left
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
 *   var left: Node = null
 *   var right: Node = null
 *   var next: Node = null
 * }
 */
object Solution {
  def connect(root: Node): Node = {
    if (root == null) return null

    var levelStart = root
    while (levelStart.left != null) {
      var cur = levelStart
      while (cur != null) {
        // Connect left child to right child
        cur.left.next = cur.right
        // Connect right child to next node's left child, if exists
        if (cur.next != null) {
          cur.right.next = cur.next.left
        }
        cur = cur.next
      }
      levelStart = levelStart.left
    }

    root
  }
}
```
