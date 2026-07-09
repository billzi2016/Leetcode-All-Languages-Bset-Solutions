# 0449. Serialize and Deserialize BST

## Cpp

```cpp
/ **
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <bits/stdc++.h>
using namespace std;

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        string res;
        function<void(TreeNode*)> preorder = [&](TreeNode* node) {
            if (!node) return;
            res += to_string(node->val);
            res.push_back(' ');
            preorder(node->left);
            preorder(node->right);
        };
        preorder(root);
        if (!res.empty() && res.back() == ' ') res.pop_back();
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        vector<int> vals;
        stringstream ss(data);
        int x;
        while (ss >> x) vals.push_back(x);
        size_t idx = 0;
        function<TreeNode*(long long, long long)> build = [&](long long lo, long long hi) -> TreeNode* {
            if (idx == vals.size()) return nullptr;
            int val = vals[idx];
            if (val < lo || val > hi) return nullptr;
            ++idx;
            TreeNode* node = new TreeNode(val);
            node->left = build(lo, (long long)val - 1);
            node->right = build((long long)val + 1, hi);
            return node;
        };
        return build(LLONG_MIN, LLONG_MAX);
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
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        // remove trailing space
        sb.setLength(sb.length() - 1);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if (node == null) return;
        sb.append(node.val).append(' ');
        buildString(node.left, sb);
        buildString(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null || data.isEmpty()) return null;
        String[] parts = data.split(" ");
        int n = parts.length;
        preorder = new int[n];
        for (int i = 0; i < n; i++) {
            preorder[i] = Integer.parseInt(parts[i]);
        }
        index = 0;
        return buildTree(Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private int[] preorder;
    private int index;

    private TreeNode buildTree(long lower, long upper) {
        if (index >= preorder.length) return null;
        int val = preorder[index];
        if (val < lower || val > upper) return null;
        index++;
        TreeNode node = new TreeNode(val);
        node.left = buildTree(lower, val - 1L);
        node.right = buildTree(val + 1L, upper);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
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
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = list(map(int, data.split(',')))
        self.idx = 0

        def build(lower, upper):
            if self.idx == len(vals):
                return None
            val = vals[self.idx]
            if not (lower < val < upper):
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float('-inf'), float('inf'))
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        nums = list(map(int, data.split()))
        self.idx = 0
        sys.setrecursionlimit(20000)
        def build(lower, upper):
            if self.idx == len(nums):
                return None
            val = nums[self.idx]
            if not (lower < val < upper):
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node
        return build(float('-inf'), float('inf'))
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <ctype.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Helper to perform preorder traversal and write into buffer */
static void preorder(struct TreeNode *node, char **buf) {
    if (!node) return;
    int len = sprintf(*buf, "%d ", node->val);
    *buf += len;
    preorder(node->left, buf);
    preorder(node->right, buf);
}

/** Encodes a tree to a single string. */
char* serialize(struct TreeNode* root) {
    /* Allocate enough space: max 10^4 nodes, each up to 5 digits + sign + space */
    size_t capacity = 120000;               // generous upper bound
    char *buf = (char *)malloc(capacity);
    if (!buf) return NULL;
    char *ptr = buf;

    preorder(root, &ptr);

    if (ptr != buf) {
        *(ptr - 1) = '\0';   /* replace trailing space with null terminator */
    } else {
        *ptr = '\0';
    }
    return buf;
}

/* Helper to rebuild BST from preorder array using bounds */
static struct TreeNode* buildBST(int *pre, int n, int *idx, long long low, long long high) {
    if (*idx >= n) return NULL;
    int val = pre[*idx];
    if (val < low || val > high) return NULL;

    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = val;
    (*idx)++;

    node->left  = buildBST(pre, n, idx, low, (long long)val - 1);
    node->right = buildBST(pre, n, idx, (long long)val + 1, high);
    return node;
}

/** Decodes your encoded data to tree. */
struct TreeNode* deserialize(char* data) {
    if (!data || *data == '\0') return NULL;

    int max_nodes = 10000;
    int *vals = (int *)malloc(sizeof(int) * max_nodes);
    int count = 0;

    char *p = data;
    while (*p) {
        while (*p && isspace((unsigned char)*p)) p++;
        if (!*p) break;
        long val = strtol(p, &p, 10);
        vals[count++] = (int)val;
    }

    int idx = 0;
    struct TreeNode *root = buildBST(vals, count, &idx, LLONG_MIN, LLONG_MAX);
    free(vals);
    return root;
}

/* The functions will be used as:
   char* data = serialize(root);
   struct TreeNode* tree = deserialize(data);
*/
```

## Csharp

```csharp
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
        var sb = new System.Text.StringBuilder();
        void Preorder(TreeNode node) {
            if (node == null) return;
            sb.Append(node.val).Append(' ');
            Preorder(node.left);
            Preorder(node.right);
        }
        Preorder(root);
        // Remove trailing space if any
        if (sb.Length > 0) sb.Length--;
        return sb.ToString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data) {
        if (string.IsNullOrEmpty(data)) return null;
        var parts = data.Split(' ', System.StringSplitOptions.RemoveEmptyEntries);
        int[] vals = new int[parts.Length];
        for (int i = 0; i < parts.Length; i++) vals[i] = int.Parse(parts[i]);
        int index = 0;

        TreeNode Build(long lower, long upper) {
            if (index == vals.Length) return null;
            int val = vals[index];
            if (val <= lower || val >= upper) return null;
            index++;
            var node = new TreeNode(val);
            node.left = Build(lower, val);
            node.right = Build(val, upper);
            return node;
        }

        return Build(long.MinValue, long.MaxValue);
    }
}
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
    const vals = [];
    const preorder = (node) => {
        if (!node) return;
        vals.push(node.val);
        preorder(node.left);
        preorder(node.right);
    };
    preorder(root);
    return vals.join(' ');
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if (!data) return null;
    const nums = data.split(' ').map(Number);
    let idx = 0;
    const build = (lower, upper) => {
        if (idx === nums.length) return null;
        const val = nums[idx];
        if (val < lower || val > upper) return null;
        idx++;
        const node = new TreeNode(val);
        node.left = build(lower, val);
        node.right = build(val, upper);
        return node;
    };
    return build(-Infinity, Infinity);
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
    const vals: number[] = [];
    const preorder = (node: TreeNode | null) => {
        if (!node) return;
        vals.push(node.val);
        preorder(node.left);
        preorder(node.right);
    };
    preorder(root);
    return vals.join(',');
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    if (!data) return null;
    const nums = data.split(',').map(Number);
    let idx = 0;

    const build = (lower: number, upper: number): TreeNode | null => {
        if (idx >= nums.length) return null;
        const val = nums[idx];
        if (val < lower || val > upper) return null;
        idx++;
        const node = new TreeNode(val);
        node.left = build(lower, val);
        node.right = build(val, upper);
        return node;
    };

    return build(Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY);
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
```

## Php

```php
/ **
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
        
    }

    /**
     * @param TreeNode $root
     * @return string
     */
    function serialize($root) {
        $vals = [];
        $this->preorder($root, $vals);
        return implode(',', $vals);
    }
    
    private function preorder($node, &$vals) {
        if ($node === null) {
            return;
        }
        $vals[] = $node->val;
        $this->preorder($node->left, $vals);
        $this->preorder($node->right, $vals);
    }

    /**
     * @param string $data
     * @return TreeNode|null
     */
    function deserialize($data) {
        if (strlen($data) === 0) {
            return null;
        }
        $vals = explode(',', $data);
        $index = 0;
        return $this->buildTree($vals, $index, PHP_INT_MIN, PHP_INT_MAX);
    }
    
    private function buildTree(&$vals, &$i, $lower, $upper) {
        if ($i >= count($vals)) {
            return null;
        }
        $val = intval($vals[$i]);
        if ($val < $lower || $val > $upper) {
            return null;
        }
        $i++;
        $node = new TreeNode($val);
        $node->left  = $this->buildTree($vals, $i, $lower, $val - 1);
        $node->right = $this->buildTree($vals, $i, $val + 1, $upper);
        return $node;
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * $ser = new Codec();
 * $tree = $ser->serialize($param_1);
 * $deser = new Codec();
 * $ret = $deser->deserialize($tree);
 * return $ret;
 */
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
    // Encodes a tree to a single string.
    func serialize(_ root: TreeNode?) -> String {
        var parts = [String]()
        func preorder(_ node: TreeNode?) {
            guard let n = node else { return }
            parts.append(String(n.val))
            preorder(n.left)
            preorder(n.right)
        }
        preorder(root)
        return parts.joined(separator: " ")
    }
    
    // Decodes your encoded data to tree.
    func deserialize(_ data: String) -> TreeNode? {
        if data.isEmpty { return nil }
        let values = data.split(separator: " ").compactMap { Int($0) }
        var index = 0
        
        func build(_ lower: Int, _ upper: Int) -> TreeNode? {
            if index >= values.count { return nil }
            let val = values[index]
            if val < lower || val > upper { return nil }
            index += 1
            let node = TreeNode(val)
            node.left = build(lower, val - 1)
            node.right = build(val + 1, upper)
            return node
        }
        
        return build(Int.min, Int.max)
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let ser = Codec()
 * let deser = Codec()
 * let tree: String = ser.serialize(root)
 * let ans = deser.deserialize(tree)
 * return ans
 */
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

class Codec() {
    // Encodes a tree to a single string.
    fun serialize(root: TreeNode?): String {
        val sb = StringBuilder()
        fun preorder(node: TreeNode?) {
            if (node == null) return
            sb.append(node.`val`).append(' ')
            preorder(node.left)
            preorder(node.right)
        }
        preorder(root)
        if (sb.isNotEmpty()) sb.setLength(sb.length - 1) // remove trailing space
        return sb.toString()
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        if (data.isEmpty()) return null
        val values = data.split(' ').map { it.toInt() }
        var idx = 0

        fun build(lower: Long, upper: Long): TreeNode? {
            if (idx >= values.size) return null
            val v = values[idx].toLong()
            if (v < lower || v > upper) return null
            idx++
            val node = TreeNode(v.toInt())
            node.left = build(lower, v - 1)
            node.right = build(v + 1, upper)
            return node
        }

        return build(Long.MIN_VALUE, Long.MAX_VALUE)
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

type Codec struct{}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (c *Codec) serialize(root *TreeNode) string {
	var sb strings.Builder
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		sb.WriteString(strconv.Itoa(node.Val))
		sb.WriteByte(' ')
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return strings.TrimSpace(sb.String())
}

// Deserializes your encoded data to tree.
func (c *Codec) deserialize(data string) *TreeNode {
	if len(data) == 0 {
		return nil
	}
	parts := strings.Split(data, " ")
	vals := make([]int, len(parts))
	for i, p := range parts {
		v, _ := strconv.Atoi(p)
		vals[i] = v
	}

	const (
		maxInt = int(^uint(0) >> 1)
		minInt = -maxInt - 1
	)

	idx := 0
	var build func(int, int) *TreeNode
	build = func(lower, upper int) *TreeNode {
		if idx >= len(vals) {
			return nil
		}
		val := vals[idx]
		if val <= lower || val >= upper {
			return nil
		}
		idx++
		node := &TreeNode{Val: val}
		node.Left = build(lower, val)
		node.Right = build(val, upper)
		return node
	}

	return build(minInt, maxInt)
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor()
 * deser := Constructor()
 * data := ser.serialize(root)
 * ans := deser.deserialize(data)
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
  return '' if root.nil?
  vals = []
  stack = [root]
  while !stack.empty?
    node = stack.pop
    next if node.nil?
    vals << node.val
    stack << node.right if node.right
    stack << node.left if node.left
  end
  vals.join(' ')
end

def deserialize(data)
  return nil if data.nil? || data.empty?
  vals = data.split.map(&:to_i)
  idx = 0
  build = lambda do |lower, upper|
    return nil if idx >= vals.size
    val = vals[idx]
    return nil if val <= lower || val >= upper
    idx += 1
    node = TreeNode.new(val)
    node.left = build.call(lower, val)
    node.right = build.call(val, upper)
    node
  end
  build.call(-Float::INFINITY, Float::INFINITY)
end
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

class Codec {
  // Encodes a tree to a single string.
  def serialize(root: TreeNode): String = {
    val sb = new StringBuilder
    def preorder(node: TreeNode): Unit = {
      if (node == null) return
      sb.append(node.value).append(' ')
      preorder(node.left)
      preorder(node.right)
    }
    preorder(root)
    sb.toString.trim
  }

  // Decodes your encoded data to tree.
  def deserialize(data: String): TreeNode = {
    if (data.isEmpty) return null
    val vals = data.split(" ").map(_.toInt)
    var idx = 0

    def build(lower: Long, upper: Long): TreeNode = {
      if (idx >= vals.length) return null
      val v = vals(idx).toLong
      if (v < lower || v > upper) return null
      idx += 1
      val node = new TreeNode(v.toInt)
      node.left = build(lower, v - 1)
      node.right = build(v + 1, upper)
      node
    }

    build(Long.MinValue, Long.MaxValue)
  }
}

/**
 * Your Codec object will be instantiated and called as such:
 * val ser = new Codec()
 * val deser = new Codec()
 * val tree: String = ser.serialize(root)
 * val ans = deser.deserialize(tree)
 * return ans
 */
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

/// Definition for a binary tree node.
/// #[derive(Debug, PartialEq, Eq)]
/// pub struct TreeNode {
///   pub val: i32,
///   pub left: Option<Rc<RefCell<TreeNode>>>,
///   pub right: Option<Rc<RefCell<TreeNode>>>,
/// }
///
/// impl TreeNode {
///   #[inline]
///   pub fn new(val: i32) -> Self {
///     TreeNode {
///       val,
///       left: None,
///       right: None
///     }
///   }
/// }

struct Codec {}

impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        fn preorder(node: &Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<String>) {
            if let Some(rc) = node {
                let n = rc.borrow();
                out.push(n.val.to_string());
                preorder(&n.left, out);
                preorder(&n.right, out);
            }
        }

        let mut vals = Vec::new();
        preorder(&root, &mut vals);
        vals.join(" ")
    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        if data.is_empty() {
            return None;
        }
        let nums: Vec<i32> = data
            .split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();

        fn build(
            min: i64,
            max: i64,
            idx: &mut usize,
            nums: &Vec<i32>,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if *idx >= nums.len() {
                return None;
            }
            let val = nums[*idx] as i64;
            if !(min < val && val < max) {
                return None;
            }
            *idx += 1;
            let node = Rc::new(RefCell::new(TreeNode::new(val as i32)));
            {
                let left = build(min, val, idx, nums);
                node.borrow_mut().left = left;
                let right = build(val, max, idx, nums);
                node.borrow_mut().right = right;
            }
            Some(node)
        }

        let mut index = 0usize;
        build(i64::MIN, i64::MAX, &mut index, &nums)
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */
```
