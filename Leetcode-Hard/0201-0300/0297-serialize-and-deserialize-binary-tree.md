# 0297. Serialize and Deserialize Binary Tree

## Cpp

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        string s;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (node) {
                s += to_string(node->val) + ',';
                q.push(node->left);
                q.push(node->right);
            } else {
                s += "#,";
            }
        }
        if (!s.empty()) s.pop_back(); // remove trailing comma
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        vector<string> vals;
        string token;
        stringstream ss(data);
        while (getline(ss, token, ',')) {
            vals.push_back(token);
        }
        int i = 0;
        TreeNode* root = new TreeNode(stoi(vals[i++]));
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty() && i < (int)vals.size()) {
            TreeNode* node = q.front(); q.pop();
            // left child
            if (vals[i] != "#") {
                TreeNode* leftNode = new TreeNode(stoi(vals[i]));
                node->left = leftNode;
                q.push(leftNode);
            }
            ++i;
            if (i >= (int)vals.size()) break;
            // right child
            if (vals[i] != "#") {
                TreeNode* rightNode = new TreeNode(stoi(vals[i]));
                node->right = rightNode;
                q.push(rightNode);
            }
            ++i;
        }
        return root;
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
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        build(root, sb);
        if (sb.length() > 0) {
            sb.setLength(sb.length() - 1); // remove trailing comma
        }
        return sb.toString();
    }

    private void build(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("null,");
            return;
        }
        sb.append(node.val).append(',');
        build(node.left, sb);
        build(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null || data.isEmpty()) {
            return null;
        }
        String[] nodes = data.split(",");
        int[] idx = new int[1];
        return buildTree(nodes, idx);
    }

    private TreeNode buildTree(String[] nodes, int[] idx) {
        if (idx[0] >= nodes.length) {
            return null;
        }
        String val = nodes[idx[0]++];
        if ("null".equals(val)) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = buildTree(nodes, idx);
        node.right = buildTree(nodes, idx);
        return node;
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ''
        from collections import deque
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node:
                vals.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                vals.append('#')
        # Remove trailing null markers to shorten the string
        while vals and vals[-1] == '#':
            vals.pop()
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        from collections import deque
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            # left child
            if vals[i] != '#':
                left = TreeNode(int(vals[i]))
                node.left = left
                q.append(left)
            i += 1
            if i >= len(vals):
                break
            # right child
            if vals[i] != '#':
                right = TreeNode(int(vals[i]))
                node.right = right
                q.append(right)
            i += 1
        return root
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ''
        from collections import deque
        q = deque([root])
        parts = []
        while q:
            node = q.popleft()
            if node:
                parts.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                parts.append('#')
        # Remove trailing null markers to shorten the string
        while parts and parts[-1] == '#':
            parts.pop()
        return ','.join(parts)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        vals = data.split(',')
        from collections import deque
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            # left child
            if vals[i] != '#':
                left = TreeNode(int(vals[i]))
                node.left = left
                q.append(left)
            i += 1
            if i >= len(vals):
                break
            # right child
            if vals[i] != '#':
                right = TreeNode(int(vals[i]))
                node.right = right
                q.append(right)
            i += 1
        return root
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct StringBuilder {
    char *buf;
    int len;
    int cap;
};

static void sb_init(struct StringBuilder *sb) {
    sb->cap = 1024;
    sb->len = 0;
    sb->buf = (char *)malloc(sb->cap);
    sb->buf[0] = '\0';
}

static void sb_append(struct StringBuilder *sb, const char *s, int slen) {
    if (sb->len + slen >= sb->cap) {
        while (sb->len + slen >= sb->cap) sb->cap <<= 1;
        sb->buf = (char *)realloc(sb->buf, sb->cap);
    }
    memcpy(sb->buf + sb->len, s, slen);
    sb->len += slen;
    sb->buf[sb->len] = '\0';
}

static void preorder(struct TreeNode *node, struct StringBuilder *sb) {
    if (!node) {
        sb_append(sb, "#,", 2);
        return;
    }
    char numbuf[16];
    int n = snprintf(numbuf, sizeof(numbuf), "%d", node->val);
    sb_append(sb, numbuf, n);
    sb_append(sb, ",", 1);
    preorder(node->left, sb);
    preorder(node->right, sb);
}

/** Encodes a tree to a single string. */
char* serialize(struct TreeNode* root) {
    struct StringBuilder sb;
    sb_init(&sb);
    preorder(root, &sb);
    return sb.buf;  // caller is responsible for freeing
}

/* Helper for deserialization */
static struct TreeNode* build(char **ptr) {
    if (**ptr == '\0') return NULL;
    char *comma = strchr(*ptr, ',');
    if (!comma) return NULL;  // malformed input
    int len = (int)(comma - *ptr);
    if (len == 1 && (*ptr)[0] == '#') {
        *ptr = comma + 1;
        return NULL;
    }
    char numbuf[16];
    memcpy(numbuf, *ptr, len);
    numbuf[len] = '\0';
    int val = atoi(numbuf);
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = val;
    *ptr = comma + 1;          // advance past current token
    node->left = build(ptr);   // construct left subtree
    node->right = build(ptr);  // construct right subtree
    return node;
}

/** Decodes your encoded data to tree. */
struct TreeNode* deserialize(char* data) {
    char *p = data;
    return build(&p);
}

// Your functions will be called as such:
// char* data = serialize(root);
// struct TreeNode* newRoot = deserialize(data);
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public string serialize(TreeNode root) {
        if (root == null) return "";
        var sb = new StringBuilder();
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            var node = queue.Dequeue();
            if (node == null) {
                sb.Append("null,");
            } else {
                sb.Append(node.val).Append(',');
                queue.Enqueue(node.left);
                queue.Enqueue(node.right);
            }
        }
        // Remove trailing comma
        if (sb.Length > 0) sb.Length--;
        return sb.ToString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data) {
        if (string.IsNullOrEmpty(data)) return null;
        var vals = data.Split(',');
        int index = 0;
        TreeNode root = new TreeNode(int.Parse(vals[index++]));
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0 && index < vals.Length) {
            var node = queue.Dequeue();
            // left child
            if (index < vals.Length) {
                string leftVal = vals[index++];
                if (leftVal != "null") {
                    TreeNode leftNode = new TreeNode(int.Parse(leftVal));
                    node.left = leftNode;
                    queue.Enqueue(leftNode);
                }
            }
            // right child
            if (index < vals.Length) {
                string rightVal = vals[index++];
                if (rightVal != "null") {
                    TreeNode rightNode = new TreeNode(int.Parse(rightVal));
                    node.right = rightNode;
                    queue.Enqueue(rightNode);
                }
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    if (!root) return '';
    const vals = [];
    const dfs = (node) => {
        if (!node) {
            vals.push('null');
            return;
        }
        vals.push(String(node.val));
        dfs(node.left);
        dfs(node.right);
    };
    dfs(root);
    return vals.join(',');
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if (!data) return null;
    const arr = data.split(',');
    let idx = 0;
    const build = () => {
        if (arr[idx] === 'null') {
            idx++;
            return null;
        }
        const node = new TreeNode(parseInt(arr[idx++], 10));
        node.left = build();
        node.right = build();
        return node;
    };
    return build();
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
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

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
    if (!root) return "";
    const queue: (TreeNode | null)[] = [root];
    const parts: string[] = [];
    while (queue.length) {
        const node = queue.shift()!;
        if (node) {
            parts.push(String(node.val));
            queue.push(node.left);
            queue.push(node.right);
        } else {
            parts.push("null");
        }
    }
    // Remove trailing nulls to keep the string concise
    while (parts.length && parts[parts.length - 1] === "null") {
        parts.pop();
    }
    return parts.join(",");
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    if (!data) return null;
    const vals = data.split(",");
    const root = new TreeNode(parseInt(vals[0], 10));
    const queue: TreeNode[] = [root];
    let idx = 1;
    while (idx < vals.length) {
        const parent = queue.shift()!;
        // left child
        if (idx < vals.length) {
            const val = vals[idx++];
            if (val !== "null") {
                const leftNode = new TreeNode(parseInt(val, 10));
                parent.left = leftNode;
                queue.push(leftNode);
            }
        }
        // right child
        if (idx < vals.length) {
            const val = vals[idx++];
            if (val !== "null") {
                const rightNode = new TreeNode(parseInt(val, 10));
                parent.right = rightNode;
                queue.push(rightNode);
            }
        }
    }
    return root;
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```

## Php

```php
<?php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */

class Codec {
    function __construct() {
        // No initialization required
    }

    /**
     * @param TreeNode|null $root
     * @return string
     */
    function serialize($root) {
        if ($root === null) {
            return '';
        }
        $queue = new SplQueue();
        $queue->enqueue($root);
        $result = [];

        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            if ($node !== null) {
                $result[] = (string)$node->val;
                $queue->enqueue($node->left);
                $queue->enqueue($node->right);
            } else {
                $result[] = 'null';
            }
        }

        // Trim trailing nulls to keep the string compact
        while (!empty($result) && end($result) === 'null') {
            array_pop($result);
        }

        return implode(',', $result);
    }

    /**
     * @param string $data
     * @return TreeNode|null
     */
    function deserialize($data) {
        if ($data === '' ) {
            return null;
        }
        $vals = explode(',', $data);
        $n = count($vals);
        $rootVal = intval($vals[0]);
        $root = new TreeNode($rootVal);
        $queue = new SplQueue();
        $queue->enqueue($root);
        $i = 1;

        while (!$queue->isEmpty() && $i < $n) {
            $node = $queue->dequeue();

            // left child
            if ($i < $n) {
                if ($vals[$i] !== 'null') {
                    $leftNode = new TreeNode(intval($vals[$i]));
                    $node->left = $leftNode;
                    $queue->enqueue($leftNode);
                }
                $i++;
            }

            // right child
            if ($i < $n) {
                if ($vals[$i] !== 'null') {
                    $rightNode = new TreeNode(intval($vals[$i]));
                    $node->right = $rightNode;
                    $queue->enqueue($rightNode);
                }
                $i++;
            }
        }

        return $root;
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * $ser = new Codec();
 * $deser = new Codec();
 * $data = $ser->serialize($root);
 * $ans = $deser->deserialize($data);
 */
?>
```

## Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Codec {
    func serialize(_ root: TreeNode?) -> String {
        var parts = [String]()
        func preorder(_ node: TreeNode?) {
            guard let n = node else {
                parts.append("null")
                return
            }
            parts.append(String(n.val))
            preorder(n.left)
            preorder(n.right)
        }
        preorder(root)
        // If the tree is empty, return an empty string
        return parts.isEmpty ? "" : parts.joined(separator: ",")
    }
    
    func deserialize(_ data: String) -> TreeNode? {
        if data.isEmpty { return nil }
        var values = data.split(separator: ",").map { String($0) }
        var index = 0
        
        func build() -> TreeNode? {
            if index >= values.count { return nil }
            let val = values[index]
            index += 1
            if val == "null" {
                return nil
            } else {
                let node = TreeNode(Int(val)!)
                node.left = build()
                node.right = build()
                return node
            }
        }
        
        return build()
    }
}

// Your Codec object will be instantiated and called as such:
// var ser = Codec()
// var deser = Codec()
// deser.deserialize(ser.serialize(root))
```

## Kotlin

```kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

import java.util.ArrayDeque

class Codec() {

    // Encodes a tree to a single string.
    fun serialize(root: TreeNode?): String {
        if (root == null) return ""
        val sb = StringBuilder()
        val q: ArrayDeque<TreeNode?> = ArrayDeque()
        q.add(root)
        while (!q.isEmpty()) {
            val node = q.poll()
            if (node == null) {
                sb.append("null,")
                continue
            }
            sb.append(node.`val`).append(',')
            q.add(node.left)
            q.add(node.right)
        }
        // Trim trailing "null"s to keep the string compact
        val parts = sb.toString().split(",")
        var i = parts.size - 1
        while (i >= 0 && (parts[i].isEmpty() || parts[i] == "null")) {
            i--
        }
        return if (i < 0) "" else parts.subList(0, i + 1).joinToString(",")
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        if (data.isEmpty()) return null
        val vals = data.split(",")
        val root = TreeNode(vals[0].toInt())
        val q: ArrayDeque<TreeNode> = ArrayDeque()
        q.add(root)
        var idx = 1
        while (!q.isEmpty() && idx < vals.size) {
            val node = q.poll()
            // left child
            if (idx < vals.size) {
                val leftVal = vals[idx++]
                if (leftVal != "null") {
                    val leftNode = TreeNode(leftVal.toInt())
                    node.left = leftNode
                    q.add(leftNode)
                }
            }
            // right child
            if (idx < vals.size) {
                val rightVal = vals[idx++]
                if (rightVal != "null") {
                    val rightNode = TreeNode(rightVal.toInt())
                    node.right = rightNode
                    q.add(rightNode)
                }
            }
        }
        return root
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var ser = Codec()
 * var deser = Codec()
 * var data = ser.serialize(root)
 * var ans = deser.deserialize(data)
 */
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	var sb []string
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node != nil {
			sb = append(sb, strconv.Itoa(node.Val))
			queue = append(queue, node.Left)
			queue = append(queue, node.Right)
		} else {
			sb = append(sb, "null")
		}
	}
	// Trim trailing nulls to keep the string concise
	i := len(sb) - 1
	for i >= 0 && sb[i] == "null" {
		i--
	}
	sb = sb[:i+1]
	return strings.Join(sb, ",")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	if data == "" {
		return nil
	}
	vals := strings.Split(data, ",")
	rootVal, _ := strconv.Atoi(vals[0])
	root := &TreeNode{Val: rootVal}
	queue := []*TreeNode{root}
	idx := 1
	for len(queue) > 0 && idx < len(vals) {
		node := queue[0]
		queue = queue[1:]

		// left child
		if vals[idx] != "null" {
			v, _ := strconv.Atoi(vals[idx])
			left := &TreeNode{Val: v}
			node.Left = left
			queue = append(queue, left)
		}
		idx++
		if idx >= len(vals) {
			break
		}

		// right child
		if vals[idx] != "null" {
			v, _ := strconv.Atoi(vals[idx])
			right := &TreeNode{Val: v}
			node.Right = right
			queue = append(queue, right)
		}
		idx++
	}
	return root
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

def serialize(root)
  return "" if root.nil?
  queue = [root]
  vals = []
  until queue.empty?
    node = queue.shift
    if node
      vals << node.val.to_s
      queue << node.left
      queue << node.right
    else
      vals << "null"
    end
  end
  # Remove trailing nulls to shorten the string
  while vals.last == "null"
    vals.pop
  end
  vals.join(',')
end

def deserialize(data)
  return nil if data.nil? || data.empty?
  parts = data.split(',')
  root = TreeNode.new(parts[0].to_i)
  queue = [root]
  i = 1
  while !queue.empty? && i < parts.length
    parent = queue.shift
    # left child
    if parts[i] != "null"
      left_node = TreeNode.new(parts[i].to_i)
      parent.left = left_node
      queue << left_node
    end
    i += 1
    break if i >= parts.length
    # right child
    if parts[i] != "null"
      right_node = TreeNode.new(parts[i].to_i)
      parent.right = right_node
      queue << right_node
    end
    i += 1
  end
  root
end

# Your functions will be called as such:
# deserialize(serialize(data))
```

## Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

import scala.collection.mutable.Queue

class Codec {
  // Encodes a tree to a single string.
  def serialize(root: TreeNode): String = {
    if (root == null) return ""
    val sb = new StringBuilder
    val q = Queue[TreeNode]()
    q.enqueue(root)
    while (q.nonEmpty) {
      val node = q.dequeue()
      if (node != null) {
        sb.append(node.value).append(',')
        q.enqueue(node.left)
        q.enqueue(node.right)
      } else {
        sb.append("#,")
      }
    }
    // Remove trailing comma
    if (sb.nonEmpty) sb.setLength(sb.length - 1)
    sb.toString()
  }

  // Decodes your encoded data to tree.
  def deserialize(data: String): TreeNode = {
    if (data == null || data.isEmpty) return null
    val vals = data.split(",")
    val root = new TreeNode(vals(0).toInt)
    val q = Queue[TreeNode]()
    q.enqueue(root)
    var i = 1
    while (i < vals.length) {
      val parent = q.dequeue()
      // left child
      if (vals(i) != "#") {
        val leftNode = new TreeNode(vals(i).toInt)
        parent.left = leftNode
        q.enqueue(leftNode)
      }
      i += 1
      if (i >= vals.length) return root
      // right child
      if (vals(i) != "#") {
        val rightNode = new TreeNode(vals(i).toInt)
        parent.right = rightNode
        q.enqueue(rightNode)
      }
      i += 1
    }
    root
  }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var ser = new Codec()
 * var deser = new Codec()
 * val s = ser.serialize(root)
 * val ans = deser.deserialize(s)
 */
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

struct Codec {}

impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<String>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                out.push(n.val.to_string());
                dfs(&n.left, out);
                dfs(&n.right, out);
            } else {
                out.push("#".to_string());
            }
        }

        let mut parts = Vec::new();
        dfs(&root, &mut parts);
        parts.join(",")
    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        let tokens: Vec<&str> = data.split(',').collect();

        fn build(tokens: &[&str], idx: &mut usize) -> Option<Rc<RefCell<TreeNode>>> {
            if *idx >= tokens.len() {
                return None;
            }
            let token = tokens[*idx];
            *idx += 1;
            if token == "#" {
                None
            } else {
                let val: i32 = token.parse().unwrap();
                let node = Rc::new(RefCell::new(TreeNode::new(val)));
                let left = build(tokens, idx);
                let right = build(tokens, idx);
                node.borrow_mut().left = left;
                node.borrow_mut().right = right;
                Some(node)
            }
        }

        let mut index = 0;
        build(&tokens, &mut index)
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */
```
