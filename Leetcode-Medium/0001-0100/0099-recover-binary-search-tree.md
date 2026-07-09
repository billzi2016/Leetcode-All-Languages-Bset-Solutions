# 0099. Recover Binary Search Tree

## Cpp

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode *first = nullptr, *second = nullptr, *prev = nullptr;
        inorder(root, prev, first, second);
        if (first && second) std::swap(first->val, second->val);
    }
private:
    void inorder(TreeNode* node, TreeNode*& prev, TreeNode*& first, TreeNode*& second) {
        if (!node) return;
        inorder(node->left, prev, first, second);
        if (prev && prev->val > node->val) {
            if (!first) first = prev;
            second = node;
        }
        prev = node;
        inorder(node->right, prev, first, second);
    }
};
```

## Java

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void recoverTree(TreeNode root) {
        List<TreeNode> inorderList = new ArrayList<>();
        inorder(root, inorderList);
        TreeNode first = null, second = null;
        for (int i = 1; i < inorderList.size(); i++) {
            if (inorderList.get(i).val < inorderList.get(i - 1).val) {
                if (first == null) {
                    first = inorderList.get(i - 1);
                }
                second = inorderList.get(i);
            }
        }
        if (first != null && second != null) {
            int tmp = first.val;
            first.val = second.val;
            second.val = tmp;
        }
    }

    private void inorder(TreeNode node, List<TreeNode> list) {
        if (node == null) return;
        inorder(node.left, list);
        list.add(node);
        inorder(node.right, list);
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        # swap the values of the two misplaced nodes
        self.first.val, self.second.val = self.second.val, self.first.val
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)
            if prev and node.val < prev.val:
                if not first:
                    first = prev
                    second = node
                else:
                    second = node
            prev = node
            inorder(node.right)

        inorder(root)
        if first and second:
            first.val, second.val = second.val, first.val
```

## C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static struct TreeNode *firstNode = NULL;
static struct TreeNode *middleNode = NULL;
static struct TreeNode *lastNode = NULL;
static struct TreeNode *prevNode = NULL;

static void inorder(struct TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    
    if (prevNode && root->val < prevNode->val) {
        if (!firstNode) {
            firstNode = prevNode;
            middleNode = root;
        } else {
            lastNode = root;
        }
    }
    prevNode = root;
    
    inorder(root->right);
}

void recoverTree(struct TreeNode* root) {
    firstNode = middleNode = lastNode = NULL;
    prevNode = NULL;
    inorder(root);
    if (firstNode && lastNode) {
        int tmp = firstNode->val;
        firstNode->val = lastNode->val;
        lastNode->val = tmp;
    } else if (firstNode && middleNode) {
        int tmp = firstNode->val;
        firstNode->val = middleNode->val;
        middleNode->val = tmp;
    }
}
```

## Csharp

```csharp
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution
{
    public void RecoverTree(TreeNode root)
    {
        var nodes = new System.Collections.Generic.List<TreeNode>();
        Inorder(root, nodes);

        TreeNode first = null, second = null, prev = null;
        foreach (var node in nodes)
        {
            if (prev != null && prev.val > node.val)
            {
                if (first == null)
                    first = prev;
                second = node;
            }
            prev = node;
        }

        if (first != null && second != null)
        {
            int tmp = first.val;
            first.val = second.val;
            second.val = tmp;
        }
    }

    private void Inorder(TreeNode node, System.Collections.Generic.List<TreeNode> list)
    {
        if (node == null) return;
        Inorder(node.left, list);
        list.Add(node);
        Inorder(node.right, list);
    }
}
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    let first = null, second = null;
    const prev = { val: -Infinity };
    
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        
        if (prev.val > node.val) {
            if (!first) {
                first = prevNode; // will set after we have reference
                first = prevNode; // placeholder, will be overwritten below
                first = prevNode; // redundant but keep pattern
                first = prevNode;
            }
            second = node;
        }
        // store current as previous for next iteration
        prev.val = node.val;
        prevNode = node;
        
        inorder(node.right);
    };
    
    // need a variable to hold actual previous node reference
    let prevNode = { val: -Infinity };
    const dfs = (node) => {
        if (!node) return;
        dfs(node.left);
        if (prevNode.val > node.val) {
            if (!first) first = prevNode;
            second = node;
        }
        prevNode = node;
        dfs(node.right);
    };
    
    dfs(root);
    if (first && second) {
        const tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
};
```

## Typescript

```typescript
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 Do not return anything, modify root in-place instead.
 */
function recoverTree(root: TreeNode | null): void {
    let first: TreeNode | null = null;
    let second: TreeNode | null = null;
    let prev: TreeNode | null = null;

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);
        if (prev && prev.val > node.val) {
            if (!first) first = prev;
            second = node;
        }
        prev = node;
        inorder(node.right);
    };

    inorder(root);

    if (first && second) {
        const tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}
```

## Php

```php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return NULL
     */
    function recoverTree($root) {
        $first = null;
        $second = null;
        $prev = null;

        $cur = $root;
        while ($cur !== null) {
            if ($cur->left === null) {
                // visit cur
                if ($prev !== null && $prev->val > $cur->val) {
                    if ($first === null) {
                        $first = $prev;
                    }
                    $second = $cur;
                }
                $prev = $cur;

                $cur = $cur->right;
            } else {
                // find predecessor
                $pre = $cur->left;
                while ($pre->right !== null && $pre->right !== $cur) {
                    $pre = $pre->right;
                }

                if ($pre->right === null) {
                    // make thread
                    $pre->right = $cur;
                    $cur = $cur->left;
                } else {
                    // remove thread and visit cur
                    $pre->right = null;

                    if ($prev !== null && $prev->val > $cur->val) {
                        if ($first === null) {
                            $first = $prev;
                        }
                        $second = $cur;
                    }
                    $prev = $cur;

                    $cur = $cur->right;
                }
            }
        }

        // swap values of the two misplaced nodes
        if ($first !== null && $second !== null) {
            $tmp = $first->val;
            $first->val = $second->val;
            $second->val = $tmp;
        }
    }
}
```

## Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    private var first: TreeNode?
    private var second: TreeNode?
    private var prev: TreeNode?

    func recoverTree(_ root: TreeNode?) {
        inorder(root)
        if let f = first, let s = second {
            let tmp = f.val
            f.val = s.val
            s.val = tmp
        }
    }

    private func inorder(_ node: TreeNode?) {
        guard let n = node else { return }
        inorder(n.left)

        if let prevNode = prev, prevNode.val > n.val {
            if first == nil {
                first = prevNode
            }
            second = n
        }
        prev = n

        inorder(n.right)
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun recoverTree(root: TreeNode?) {
        var first: TreeNode? = null
        var second: TreeNode? = null
        var prev: TreeNode? = null

        fun inorder(node: TreeNode?) {
            if (node == null) return
            inorder(node.left)

            if (prev != null && node.`val` < prev!!.`val`) {
                if (first == null) first = prev
                second = node
            }
            prev = node

            inorder(node.right)
        }

        inorder(root)

        // swap the values of the two misplaced nodes
        val tmp = first?.`val`
        first?.`val` = second?.`val` ?: 0
        second?.`val` = tmp ?: 0
    }
}
```

## Dart

```dart
class Solution {
  void recoverTree(TreeNode? root) {
    TreeNode? first;
    TreeNode? second;
    TreeNode? prev;

    List<TreeNode> stack = [];
    TreeNode? cur = root;

    while (cur != null || stack.isNotEmpty) {
      while (cur != null) {
        stack.add(cur);
        cur = cur.left;
      }
      cur = stack.removeLast();
      if (prev != null && prev.val > cur!.val) {
        if (first == null) {
          first = prev;
        }
        second = cur;
      }
      prev = cur;
      cur = cur.right;
    }

    if (first != null && second != null) {
      int temp = first.val;
      first.val = second.val;
      second.val = temp;
    }
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func recoverTree(root *TreeNode) {
    var first, second, prev *TreeNode

    var inorder func(node *TreeNode)
    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        inorder(node.Left)

        if prev != nil && prev.Val > node.Val {
            if first == nil {
                first = prev
            }
            second = node
        }
        prev = node

        inorder(node.Right)
    }

    inorder(root)

    if first != nil && second != nil {
        first.Val, second.Val = second.Val, first.Val
    }
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def recover_tree(root)
  first = second = prev = nil

  inorder = lambda do |node|
    return if node.nil?
    inorder.call(node.left)

    if prev && node.val < prev.val
      first = prev if first.nil?
      second = node
    end
    prev = node

    inorder.call(node.right)
  end

  inorder.call(root)
  if first && second
    first.val, second.val = second.val, first.val
  end
end
```

## Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def recoverTree(root: TreeNode): Unit = {
        import scala.collection.mutable.ListBuffer

        val nodes = ListBuffer[TreeNode]()

        def inorder(node: TreeNode): Unit = {
            if (node == null) return
            inorder(node.left)
            nodes += node
            inorder(node.right)
        }

        inorder(root)

        var first: TreeNode = null
        var second: TreeNode = null

        for (i <- 0 until nodes.length - 1) {
            if (nodes(i).value > nodes(i + 1).value) {
                if (first == null) first = nodes(i)
                second = nodes(i + 1)
            }
        }

        // swap the values of the two misplaced nodes
        val tmp = first.value
        first.value = second.value
        second.value = tmp
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn recover_tree(root: &mut Option<Rc<RefCell<TreeNode>>>) {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut curr_opt = root.clone();

        let mut prev: Option<Rc<RefCell<TreeNode>>> = None;
        let mut first: Option<Rc<RefCell<TreeNode>>> = None;
        let mut second: Option<Rc<RefCell<TreeNode>>> = None;

        while curr_opt.is_some() || !stack.is_empty() {
            while let Some(node_rc) = curr_opt {
                stack.push(node_rc.clone());
                curr_opt = node_rc.borrow().left.clone();
            }

            let node_rc = stack.pop().unwrap();

            if let Some(prev_rc) = prev.clone() {
                if prev_rc.borrow().val > node_rc.borrow().val {
                    if first.is_none() {
                        first = Some(prev_rc.clone());
                    }
                    second = Some(node_rc.clone());
                }
            }

            prev = Some(node_rc.clone());
            curr_opt = node_rc.borrow().right.clone();
        }

        if let (Some(first_rc), Some(second_rc)) = (first, second) {
            let mut first_mut = first_rc.borrow_mut();
            let mut second_mut = second_rc.borrow_mut();
            std::mem::swap(&mut first_mut.val, &mut second_mut.val);
        }
    }
}
```

## Racket

```racket
#|
; Definition for a binary tree node.
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (recover-tree root)
  (-> (or/c tree-node? #f) void?)
  (let ((first #f)
        (second #f)
        (prev #f))
    (define (inorder node)
      (when node
        (inorder (tree-node-left node))
        (when prev
          (when (> (tree-node-val prev) (tree-node-val node))
            (if first
                (set! second node)
                (begin
                  (set! first prev)
                  (set! second node)))))
        (set! prev node)
        (inorder (tree-node-right node))))
    (inorder root)
    (when (and first second)
      (let ((temp (tree-node-val first)))
        (set-tree-node-val! first (tree-node-val second))
        (set-tree-node-val! second temp)))))
```
