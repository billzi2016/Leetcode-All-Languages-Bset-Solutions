# 0558. Logical OR of Two Binary Grids Represented as Quad-Trees

## Cpp

```cpp
/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight,
         Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* intersect(Node* quadTree1, Node* quadTree2) {
        if (quadTree1->isLeaf) {
            if (quadTree1->val) return new Node(true, true);
            else return quadTree2;
        }
        if (quadTree2->isLeaf) {
            if (quadTree2->val) return new Node(true, true);
            else return quadTree1;
        }
        
        Node* tl = intersect(quadTree1->topLeft,  quadTree2->topLeft);
        Node* tr = intersect(quadTree1->topRight, quadTree2->topRight);
        Node* bl = intersect(quadTree1->bottomLeft, quadTree2->bottomLeft);
        Node* br = intersect(quadTree1->bottomRight, quadTree2->bottomRight);
        
        if (tl->isLeaf && tr->isLeaf && bl->isLeaf && br->isLeaf &&
            tl->val == tr->val && tl->val == bl->val && tl->val == br->val) {
            return new Node(tl->val, true);
        }
        return new Node(false, false, tl, tr, bl, br);
    }
};
```

## Java

```java
class Solution {
    public Node intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1.isLeaf) {
            if (quadTree1.val) {
                return new Node(true, true, null, null, null, null);
            }
            return quadTree2;
        }
        if (quadTree2.isLeaf) {
            if (quadTree2.val) {
                return new Node(true, true, null, null, null, null);
            }
            return quadTree1;
        }

        Node topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
        Node topRight = intersect(quadTree1.topRight, quadTree2.topRight);
        Node bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
        Node bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);

        if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf &&
            topLeft.val == topRight.val && topLeft.val == bottomLeft.val && topLeft.val == bottomRight.val) {
            return new Node(topLeft.val, true, null, null, null, null);
        }
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}
```

## Python

```python
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        # If either node is a leaf
        if quadTree1.isLeaf:
            if quadTree1.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree1

        # Both are internal nodes; recurse on children
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # If all children are leaves with the same value, merge them
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            if tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True, None, None, None, None)

        return Node(False, False, tl, tr, bl, br)
```

## Python3

```python
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return Node(True, True, None, None, None, None)
            else:
                return quadTree1

        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and \
           tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True, None, None, None, None)
        else:
            return Node(False, False, tl, tr, bl, br)
```

## Csharp

```csharp
/*
// Definition for a QuadTree node.
public class Node {
    public bool val;
    public bool isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node(){}
    public Node(bool _val,bool _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
}
*/

public class Solution {
    public Node Intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1.isLeaf) {
            if (quadTree1.val) {
                // OR with anything yields true
                return new Node(true, true, null, null, null, null);
            }
            // false leaf: result is the other tree
            return quadTree2;
        }

        if (quadTree2.isLeaf) {
            if (quadTree2.val) {
                return new Node(true, true, null, null, null, null);
            }
            return quadTree1;
        }

        var tl = Intersect(quadTree1.topLeft,  quadTree2.topLeft);
        var tr = Intersect(quadTree1.topRight, quadTree2.topRight);
        var bl = Intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
        var br = Intersect(quadTree1.bottomRight, quadTree2.bottomRight);

        // If all children are leaves with the same value, merge them.
        if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
            tl.val == tr.val && tl.val == bl.val && tl.val == br.val) {
            return new Node(tl.val, true, null, null, null, null);
        }

        return new Node(false, false, tl, tr, bl, br);
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {Node} quadTree1
 * @param {Node} quadTree2
 * @return {Node}
 */
var intersect = function(quadTree1, quadTree2) {
    // If either node is a leaf
    if (quadTree1.isLeaf) {
        if (quadTree1.val) {
            // whole region becomes 1
            return new Node(true, true, null, null, null, null);
        }
        // quadTree1 is all 0s, result is quadTree2
        return quadTree2;
    }
    if (quadTree2.isLeaf) {
        if (quadTree2.val) {
            return new Node(true, true, null, null, null, null);
        }
        return quadTree1;
    }

    // Both are internal nodes: recurse on children
    const topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
    const topRight = intersect(quadTree1.topRight, quadTree2.topRight);
    const bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
    const bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);

    // If all children are leaves with the same value, merge them
    if (
        topLeft.isLeaf && topRight.isLeaf &&
        bottomLeft.isLeaf && bottomRight.isLeaf &&
        topLeft.val === topRight.val &&
        topLeft.val === bottomLeft.val &&
        topLeft.val === bottomRight.val
    ) {
        return new Node(topLeft.val, true, null, null, null, null);
    }

    // Otherwise, keep them as internal node
    return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
};
```

## Typescript

```typescript
/ **
 * Definition for _Node.
 * class _Node {
 *     val: boolean
 *     isLeaf: boolean
 *     topLeft: _Node | null
 * 	topRight: _Node | null
 * 	bottomLeft: _Node | null
 * 	bottomRight: _Node | null
 * 	constructor(val?: boolean, isLeaf?: boolean, topLeft?: _Node, topRight?: _Node, bottomLeft?: _Node, bottomRight?: _Node) {
 *         this.val = (val===undefined ? false : val)
 *         this.isLeaf = (isLeaf===undefined ? false : isLeaf)
 *         this.topLeft = (topLeft===undefined ? null : topLeft)
 *         this.topRight = (topRight===undefined ? null : topRight)
 *         this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
 *         this.bottomRight = (bottomRight===undefined ? null : bottomRight)
 *   }
 * }
 */

function intersect(quadTree1: _Node | null, quadTree2: _Node | null): _Node | null {
    if (!quadTree1) return quadTree2;
    if (!quadTree2) return quadTree1;

    // If either node is a leaf
    if (quadTree1.isLeaf) {
        if (quadTree1.val) {
            // true OR anything = true
            return new _Node(true, true);
        }
        // false OR other = other
        return quadTree2;
    }

    if (quadTree2.isLeaf) {
        if (quadTree2.val) {
            return new _Node(true, true);
        }
        return quadTree1;
    }

    const tl = intersect(quadTree1.topLeft, quadTree2.topLeft);
    const tr = intersect(quadTree1.topRight, quadTree2.topRight);
    const bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
    const br = intersect(quadTree1.bottomRight, quadTree2.bottomRight);

    // If all children are leaves with the same value, merge them
    if (
        tl && tr && bl && br &&
        tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
        tl.val === tr.val && tl.val === bl.val && tl.val === br.val
    ) {
        return new _Node(tl.val, true);
    }

    // Otherwise, create an internal node
    return new _Node(false, false, tl, tr, bl, br);
}
```

## Php

```php
class Solution {
    /**
     * @param Node $quadTree1
     * @param Node $quadTree2
     * @return Node
     */
    function intersect($quadTree1, $quadTree2) {
        if ($quadTree1->isLeaf) {
            if ($quadTree1->val) {
                return new Node(true, true);
            }
            return $quadTree2;
        }
        if ($quadTree2->isLeaf) {
            if ($quadTree2->val) {
                return new Node(true, true);
            }
            return $quadTree1;
        }

        $topLeft = $this->intersect($quadTree1->topLeft, $quadTree2->topLeft);
        $topRight = $this->intersect($quadTree1->topRight, $quadTree2->topRight);
        $bottomLeft = $this->intersect($quadTree1->bottomLeft, $quadTree2->bottomLeft);
        $bottomRight = $this->intersect($quadTree1->bottomRight, $quadTree2->bottomRight);

        if ($topLeft->isLeaf && $topRight->isLeaf && $bottomLeft->isLeaf && $bottomRight->isLeaf &&
            $topLeft->val == $topRight->val && $topLeft->val == $bottomLeft->val && $topLeft->val == $bottomRight->val) {
            return new Node($topLeft->val, true);
        }

        $node = new Node(false, false);
        $node->topLeft = $topLeft;
        $node->topRight = $topRight;
        $node->bottomLeft = $bottomLeft;
        $node->bottomRight = $bottomRight;
        return $node;
    }
}
```

## Swift

```swift
/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Bool
 *     public var isLeaf: Bool
 *     public var topLeft: Node?
 *     public var topRight: Node?
 *     public var bottomLeft: Node?
 *     public var bottomRight: Node?
 *     public init(_ val: Bool, _ isLeaf: Bool) {
 *         self.val = val
 *         self.isLeaf = isLeaf
 *         self.topLeft = nil
 *         self.topRight = nil
 *         self.bottomLeft = nil
 *         self.bottomRight = nil
 *     }
 * }
 */

class Solution {
    func intersect(_ quadTree1: Node?, _ quadTree2: Node?) -> Node? {
        guard let node1 = quadTree1, let node2 = quadTree2 else { return nil }
        
        // If either node is a leaf
        if node1.isLeaf {
            return node1.val ? Node(true, true) : node2
        }
        if node2.isLeaf {
            return node2.val ? Node(true, true) : node1
        }
        
        // Both are internal nodes; recurse on children
        let tl = intersect(node1.topLeft, node2.topLeft)
        let tr = intersect(node1.topRight, node2.topRight)
        let bl = intersect(node1.bottomLeft, node2.bottomLeft)
        let br = intersect(node1.bottomRight, node2.bottomRight)
        
        // If all children are leaves with the same value, merge them
        if let tl = tl, let tr = tr, let bl = bl, let br = br,
           tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
           tl.val == tr.val && tl.val == bl.val && tl.val == br.val {
            return Node(tl.val, true)
        }
        
        // Otherwise create an internal node
        let parent = Node(false, false)
        parent.topLeft = tl
        parent.topRight = tr
        parent.bottomLeft = bl
        parent.bottomRight = br
        return parent
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a QuadTree node.
 * class Node(var `val`: Boolean, var isLeaf: Boolean) {
 *     var topLeft: Node? = null
 *     var topRight: Node? = null
 *     var bottomLeft: Node? = null
 *     var bottomRight: Node? = null
 * }
 */
class Solution {
    fun intersect(quadTree1: Node?, quadTree2: Node?): Node? {
        if (quadTree1 == null) return quadTree2
        if (quadTree2 == null) return quadTree1

        // If either node is a leaf
        if (quadTree1.isLeaf) {
            return if (quadTree1.`val`) {
                Node(true, true)
            } else {
                quadTree2
            }
        }
        if (quadTree2.isLeaf) {
            return if (quadTree2.`val`) {
                Node(true, true)
            } else {
                quadTree1
            }
        }

        // Both are internal nodes; recurse on children
        val tl = intersect(quadTree1.topLeft, quadTree2.topLeft)
        val tr = intersect(quadTree1.topRight, quadTree2.topRight)
        val bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        val br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        // If all children are leaves with the same value, merge them
        if (tl != null && tr != null && bl != null && br != null &&
            tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
            tl.`val` == tr.`val` && tl.`val` == bl.`val` && tl.`val` == br.`val`
        ) {
            return Node(tl.`val`, true)
        }

        // Otherwise, create an internal node
        val node = Node(false, false)
        node.topLeft = tl
        node.topRight = tr
        node.bottomLeft = bl
        node.bottomRight = br
        return node
    }
}
```

## Golang

```go
/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func intersect(quadTree1 *Node, quadTree2 *Node) *Node {
    // If either node is a leaf
    if quadTree1.IsLeaf {
        if quadTree1.Val {
            // true overrides everything
            return &Node{Val: true, IsLeaf: true}
        }
        // false leaf => result is the other tree
        return quadTree2
    }
    if quadTree2.IsLeaf {
        if quadTree2.Val {
            return &Node{Val: true, IsLeaf: true}
        }
        return quadTree1
    }

    // Both are internal nodes; recurse on children
    tl := intersect(quadTree1.TopLeft, quadTree2.TopLeft)
    tr := intersect(quadTree1.TopRight, quadTree2.TopRight)
    bl := intersect(quadTree1.BottomLeft, quadTree2.BottomLeft)
    br := intersect(quadTree1.BottomRight, quadTree2.BottomRight)

    // If all children are leaves with the same value, merge them
    if tl.IsLeaf && tr.IsLeaf && bl.IsLeaf && br.IsLeaf &&
        tl.Val == tr.Val && tr.Val == bl.Val && bl.Val == br.Val {
        return &Node{Val: tl.Val, IsLeaf: true}
    }

    // Otherwise, create an internal node with these children
    return &Node{
        Val:         false,
        IsLeaf:      false,
        TopLeft:     tl,
        TopRight:    tr,
        BottomLeft:  bl,
        BottomRight: br,
    }
}
```

## Ruby

```ruby
def intersect(quadTree1, quadTree2)
  if quadTree1.isLeaf
    return quadTree1.val ? Node.new(true, true) : quadTree2
  end
  if quadTree2.isLeaf
    return quadTree2.val ? Node.new(true, true) : quadTree1
  end

  tl = intersect(quadTree1.topLeft, quadTree2.topLeft)
  tr = intersect(quadTree1.topRight, quadTree2.topRight)
  bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
  br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)

  if tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
     tl.val == tr.val && tl.val == bl.val && tl.val == br.val
    Node.new(tl.val, true)
  else
    Node.new(false, false, tl, tr, bl, br)
  end
end
```

## Scala

```scala
object Solution {
  def intersect(quadTree1: Node, quadTree2: Node): Node = {
    // If one of the nodes is a leaf
    if (quadTree1.isLeaf) {
      if (quadTree1.value) {
        return new Node(true, true)
      } else {
        return quadTree2
      }
    }
    if (quadTree2.isLeaf) {
      if (quadTree2.value) {
        return new Node(true, true)
      } else {
        return quadTree1
      }
    }

    // Both are internal nodes: recurse on children
    val tl = intersect(quadTree1.topLeft, quadTree2.topLeft)
    val tr = intersect(quadTree1.topRight, quadTree2.topRight)
    val bl = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
    val br = intersect(quadTree1.bottomRight, quadTree2.bottomRight)

    // If all children are leaves with the same value, merge them
    if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
        tl.value == tr.value && tr.value == bl.value && bl.value == br.value) {
      new Node(tl.value, true)
    } else {
      val node = new Node(false, false)
      node.topLeft = tl
      node.topRight = tr
      node.bottomLeft = bl
      node.bottomRight = br
      node
    }
  }
}
```
