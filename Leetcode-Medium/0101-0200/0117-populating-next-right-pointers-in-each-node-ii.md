# 0117. Populating Next Right Pointers in Each Node II

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
        Node* cur = root;
        while (cur) {
            Node dummy(0);
            Node* tail = &dummy;
            for (Node* node = cur; node; node = node->next) {
                if (node->left) {
                    tail->next = node->left;
                    tail = tail->next;
                }
                if (node->right) {
                    tail->next = node->right;
                    tail = tail->next;
                }
            }
            cur = dummy.next;
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
        Node levelHead = root;
        while (levelHead != null) {
            Node dummy = new Node(0);
            Node tail = dummy;
            for (Node cur = levelHead; cur != null; cur = cur.next) {
                if (cur.left != null) {
                    tail.next = cur.left;
                    tail = tail.next;
                }
                if (cur.right != null) {
                    tail.next = cur.right;
                    tail = tail.next;
                }
            }
            levelHead = dummy.next;
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

        # Start with the head of the current level
        curr = root
        while curr:
            # Dummy node that helps build the next level's linked list
            dummy = Node(0)
            tail = dummy

            # Iterate over nodes in the current level using next pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next  # move to next node in current level

            # Move to the first node of the next level
            curr = dummy.next

        return root
```

## Python3

```python
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            dummy = Node(0)
            tail = dummy
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
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
    
    struct Node *head = root;  // start node of current level
    
    while (head) {
        struct Node dummy;      // temporary dummy node for the next level
        dummy.next = NULL;
        struct Node *prev = &dummy;
        
        for (struct Node *curr = head; curr != NULL; curr = curr->next) {
            if (curr->left) {
                prev->next = curr->left;
                prev = prev->next;
            }
            if (curr->right) {
                prev->next = curr->right;
                prev = prev->next;
            }
        }
        
        head = dummy.next;  // move to the first node of next level
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

        Node levelStart = root; // start node of current level

        while (levelStart != null) {
            Node dummy = new Node(0); // dummy head for the next level
            Node tail = dummy;        // tail to build next level's linked list
            Node curr = levelStart;

            while (curr != null) {
                if (curr.left != null) {
                    tail.next = curr.left;
                    tail = tail.next;
                }
                if (curr.right != null) {
                    tail.next = curr.right;
                    tail = tail.next;
                }
                curr = curr.next; // move within current level using already established next pointers
            }

            // Move to the first node of the next level
            levelStart = dummy.next;
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
    let levelHead = root;
    while (levelHead) {
        const dummy = new _Node(0);
        let tail = dummy;
        for (let node = levelHead; node !== null; node = node.next) {
            if (node.left) {
                tail.next = node.left;
                tail = tail.next;
            }
            if (node.right) {
                tail.next = node.right;
                tail = tail.next;
            }
        }
        levelHead = dummy.next;
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
 *
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
    let levelHead: _Node | null = root;

    while (levelHead) {
        const dummy = new _Node(0);
        let tail: _Node = dummy;

        for (let node: _Node | null = levelHead; node !== null; node = node.next) {
            if (node.left) {
                tail.next = node.left;
                tail = tail.next!;
            }
            if (node.right) {
                tail.next = node.right;
                tail = tail.next!;
            }
        }

        levelHead = dummy.next;
    }

    return root;
}
```

## Php

```php
/**
 * Definition for a Node.
 * class Node {
 *     public $val;
 *     public $left;
 *     public $right;
 *     public $next;
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
            return null;
        }

        $curr = $root;
        while ($curr !== null) {
            $dummy = new Node(0);
            $tail = $dummy;

            while ($curr !== null) {
                if ($curr->left !== null) {
                    $tail->next = $curr->left;
                    $tail = $tail->next;
                }
                if ($curr->right !== null) {
                    $tail->next = $curr->right;
                    $tail = $tail->next;
                }
                $curr = $curr->next;
            }

            $curr = $dummy->next;
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
        while let head = levelStart {
            let dummy = Node(0)
            var tail: Node? = dummy
            var curr: Node? = head
            while let node = curr {
                if let left = node.left {
                    tail?.next = left
                    tail = left
                }
                if let right = node.right {
                    tail?.next = right
                    tail = right
                }
                curr = node.next
            }
            levelStart = dummy.next
        }
        return root
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var left: Node? = null
 *     var right: Node? = null
 *     var next: Node? = null
 * }
 */
class Solution {
    fun connect(root: Node?): Node? {
        var levelHead = root
        val dummy = Node(0)
        while (levelHead != null) {
            var curr = dummy
            var node = levelHead
            while (node != null) {
                if (node.left != null) {
                    curr.next = node.left
                    curr = curr.next!!
                }
                if (node.right != null) {
                    curr.next = node.right
                    curr = curr.next!!
                }
                node = node.next
            }
            levelHead = dummy.next
            dummy.next = null
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
	cur := root
	var nextLevelHead, prev *Node

	for cur != nil {
		for cur != nil {
			if cur.Left != nil {
				if prev != nil {
					prev.Next = cur.Left
				} else {
					nextLevelHead = cur.Left
				}
				prev = cur.Left
			}
			if cur.Right != nil {
				if prev != nil {
					prev.Next = cur.Right
				} else {
					nextLevelHead = cur.Right
				}
				prev = cur.Right
			}
			cur = cur.Next
		}
		cur = nextLevelHead
		nextLevelHead, prev = nil, nil
	}
	return root
}
```

## Ruby

```ruby
# Definition for a Node.
# class Node
#     attr_accessor :val, :left, :right, :next
#     def initialize(val)
#         @val = val
#         @left, @right, @next = nil, nil, nil
#     end
# end

def connect(root)
  head = root
  while head
    dummy = Node.new(0)
    tail = dummy
    node = head
    while node
      if node.left
        tail.next = node.left
        tail = tail.next
      end
      if node.right
        tail.next = node.right
        tail = tail.next
      end
      node = node.next
    end
    head = dummy.next
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

        var levelStart: Node = root

        while (levelStart != null) {
            val dummy = new Node(0)
            var tail: Node = dummy
            var cur: Node = levelStart

            while (cur != null) {
                if (cur.left != null) {
                    tail.next = cur.left
                    tail = tail.next
                }
                if (cur.right != null) {
                    tail.next = cur.right
                    tail = tail.next
                }
                cur = cur.next
            }

            levelStart = dummy.next
        }

        root
    }
}
```
