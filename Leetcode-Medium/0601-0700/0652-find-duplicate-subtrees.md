# 0652. Find Duplicate Subtrees

## Cpp

```cpp
/ **
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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        unordered_map<string,int> cnt;
        vector<TreeNode*> ans;
        function<string(TreeNode*)> dfs = [&](TreeNode* node)->string{
            if (!node) return "#";
            string left = dfs(node->left);
            string right = dfs(node->right);
            string key = to_string(node->val) + "," + left + "," + right;
            int c = ++cnt[key];
            if (c == 2) ans.push_back(node);
            return key;
        };
        dfs(root);
        return ans;
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
    private final Map<String, Integer> countMap = new HashMap<>();
    private final List<TreeNode> duplicates = new ArrayList<>();

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        serialize(root);
        return duplicates;
    }

    private String serialize(TreeNode node) {
        if (node == null) {
            return "#";
        }
        String leftSerial = serialize(node.left);
        String rightSerial = serialize(node.right);
        String serial = node.val + "," + leftSerial + "," + rightSerial;

        int cnt = countMap.getOrDefault(serial, 0);
        if (cnt == 1) { // second time we see this subtree
            duplicates.add(node);
        }
        countMap.put(serial, cnt + 1);
        return serial;
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
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        from collections import defaultdict
        serial_count = defaultdict(int)
        duplicates = []

        def traverse(node):
            if not node:
                return "#"
            left_serial = traverse(node.left)
            right_serial = traverse(node.right)
            serial = "{},{},{}".format(node.val, left_serial, right_serial)
            cnt = serial_count[serial]
            if cnt == 1:  # second occurrence
                duplicates.append(node)
            serial_count[serial] = cnt + 1
            return serial

        traverse(root)
        return duplicates
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = {}          # maps (val,left_id,right_id) -> unique id
        count = {}          # maps unique id -> occurrence count
        duplicates = []     # result list

        def dfs(node):
            if not node:
                return 0  # use 0 as the sentinel id for null
            left_id = dfs(node.left)
            right_id = dfs(node.right)
            key = (node.val, left_id, right_id)
            uid = trees.get(key)
            if uid is None:
                uid = len(trees) + 1
                trees[key] = uid
            cnt = count.get(uid, 0)
            if cnt == 1:          # second time we see this subtree
                duplicates.append(node)
            count[uid] = cnt + 1
            return uid

        dfs(root)
        return duplicates
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

/* hash table entry */
struct Entry {
    int val;
    int leftId;
    int rightId;
    int id;          /* unique subtree identifier */
    int cnt;         /* occurrence count */
    struct Entry *next;
};

#define HASH_SIZE 20011   /* a prime larger than expected node count */

static struct Entry **table;      /* hash table buckets */
static int nextId;                /* next available subtree id (0 reserved for NULL) */
static struct TreeNode **ans;     /* result array */
static int ansSize;               /* number of results stored */
static int ansCap;                /* capacity of result array */

/* simple hash function for a triple (val,left,right) */
static unsigned int hashKey(int val, int leftId, int rightId) {
    unsigned int h = (unsigned int)(val + 0x9e3779b9);
    h ^= (unsigned int)leftId + 0x9e3779b9 + (h << 6) + (h >> 2);
    h ^= (unsigned int)rightId + 0x9e3779b9 + (h << 6) + (h >> 2);
    return h;
}

/* ensure result array has space */
static void pushResult(struct TreeNode *node) {
    if (ansSize == ansCap) {
        ansCap = ansCap ? ansCap * 2 : 16;
        ans = (struct TreeNode **)realloc(ans, ansCap * sizeof(struct TreeNode *));
    }
    ans[ansSize++] = node;
}

/* post-order traversal returning subtree id */
static int dfs(struct TreeNode *node) {
    if (!node) return 0;   /* id 0 represents NULL */

    int leftId = dfs(node->left);
    int rightId = dfs(node->right);

    unsigned int h = hashKey(node->val, leftId, rightId);
    int idx = h % HASH_SIZE;
    struct Entry *e = table[idx];
    while (e) {
        if (e->val == node->val && e->leftId == leftId && e->rightId == rightId)
            break;
        e = e->next;
    }
    if (!e) {   /* first time seeing this subtree shape */
        e = (struct Entry *)malloc(sizeof(struct Entry));
        e->val = node->val;
        e->leftId = leftId;
        e->rightId = rightId;
        e->id = ++nextId;
        e->cnt = 1;
        e->next = table[idx];
        table[idx] = e;
    } else {
        e->cnt++;
        if (e->cnt == 2)   /* record only once when duplicate is confirmed */
            pushResult(node);
    }
    return e->id;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** findDuplicateSubtrees(struct TreeNode* root, int* returnSize){
    /* initialise globals */
    table = (struct Entry **)calloc(HASH_SIZE, sizeof(struct Entry *));
    nextId = 0;
    ans = NULL;
    ansSize = 0;
    ansCap = 0;

    dfs(root);

    free(table);   /* entries themselves are not freed as LeetCode does not require it */

    *returnSize = ansSize;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Text;

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
public class Solution {
    public IList<TreeNode> FindDuplicateSubtrees(TreeNode root) {
        var countMap = new Dictionary<string, int>();
        var result = new List<TreeNode>();
        Serialize(root, countMap, result);
        return result;
    }

    private string Serialize(TreeNode node, Dictionary<string, int> map, List<TreeNode> res) {
        if (node == null) {
            return "#";
        }
        string left = Serialize(node.left, map, res);
        string right = Serialize(node.right, map, res);
        var sb = new StringBuilder();
        sb.Append(node.val).Append(',').Append(left).Append(',').Append(right);
        string key = sb.ToString();

        if (map.TryGetValue(key, out int cnt)) {
            if (cnt == 1) {
                res.Add(node);
            }
            map[key] = cnt + 1;
        } else {
            map[key] = 1;
        }

        return key;
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
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    const map = new Map(); // serialization -> count
    const res = [];
    
    function dfs(node) {
        if (!node) return '#';
        const left = dfs(node.left);
        const right = dfs(node.right);
        const serial = `${node.val},${left},${right}`;
        const cnt = map.get(serial) || 0;
        if (cnt === 1) { // second occurrence
            res.push(node);
        }
        map.set(serial, cnt + 1);
        return serial;
    }
    
    dfs(root);
    return res;
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

function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    const countMap = new Map<string, number>();
    const result: TreeNode[] = [];

    function serialize(node: TreeNode | null): string {
        if (node === null) return '#';
        const leftSerial = serialize(node.left);
        const rightSerial = serialize(node.right);
        const serial = `${node.val},${leftSerial},${rightSerial}`;
        const cnt = countMap.get(serial) ?? 0;
        if (cnt === 1) {
            result.push(node);
        }
        countMap.set(serial, cnt + 1);
        return serial;
    }

    serialize(root);
    return result;
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
     * @return TreeNode[]
     */
    function findDuplicateSubtrees($root) {
        $map = [];
        $result = [];

        $dfs = function ($node) use (&$dfs, &$map, &$result) {
            if ($node === null) {
                return '#';
            }
            $leftSerial = $dfs($node->left);
            $rightSerial = $dfs($node->right);
            $serial = $node->val . ',' . $leftSerial . ',' . $rightSerial;

            if (isset($map[$serial])) {
                $map[$serial] += 1;
            } else {
                $map[$serial] = 1;
            }

            if ($map[$serial] === 2) { // add only once when duplicate is first detected
                $result[] = $node;
            }
            return $serial;
        };

        $dfs($root);
        return $result;
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
    func findDuplicateSubtrees(_ root: TreeNode?) -> [TreeNode?] {
        var countMap = [String:Int]()
        var duplicates = [TreeNode?]()
        
        func serialize(_ node: TreeNode?) -> String {
            guard let n = node else { return "#" }
            let leftKey = serialize(n.left)
            let rightKey = serialize(n.right)
            let key = "\(n.val),\(leftKey),\(rightKey)"
            
            if let cnt = countMap[key] {
                if cnt == 1 {
                    duplicates.append(node)
                }
                countMap[key] = cnt + 1
            } else {
                countMap[key] = 1
            }
            return key
        }
        
        _ = serialize(root)
        return duplicates
    }
}
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
class Solution {
    fun findDuplicateSubtrees(root: TreeNode?): List<TreeNode?> {
        val countMap = HashMap<String, Int>()
        val result = mutableListOf<TreeNode?>()
        
        fun serialize(node: TreeNode?): String {
            if (node == null) return "#"
            val leftSerial = serialize(node.left)
            val rightSerial = serialize(node.right)
            val key = "${node.`val`},$leftSerial,$rightSerial"
            countMap[key] = countMap.getOrDefault(key, 0) + 1
            if (countMap[key] == 2) {
                result.add(node)
            }
            return key
        }
        
        serialize(root)
        return result
    }
}
```

## Dart

```dart
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  final Map<String, int> _freq = {};
  final List<TreeNode?> _result = [];

  List<TreeNode?> findDuplicateSubtrees(TreeNode? root) {
    _traverse(root);
    return _result;
  }

  String _traverse(TreeNode? node) {
    if (node == null) return '#';
    final left = _traverse(node.left);
    final right = _traverse(node.right);
    final key = '${node.val},$left,$right';
    final count = (_freq[key] ?? 0) + 1;
    _freq[key] = count;
    if (count == 2) {
      _result.add(node);
    }
    return key;
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
import "fmt"

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	m := make(map[string]int)
	var res []*TreeNode

	var dfs func(*TreeNode) string
	dfs = func(node *TreeNode) string {
		if node == nil {
			return "#"
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		key := fmt.Sprintf("%d,%s,%s", node.Val, left, right)
		m[key]++
		if m[key] == 2 {
			res = append(res, node)
		}
		return key
	}

	dfs(root)
	return res
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

def find_duplicate_subtrees(root)
  counts = Hash.new(0)
  result = []

  serialize = nil
  serialize = ->(node) {
    return "#" if node.nil?
    left_key = serialize.call(node.left)
    right_key = serialize.call(node.right)
    key = "#{node.val},#{left_key},#{right_key}"
    counts[key] += 1
    result << node if counts[key] == 2
    key
  }

  serialize.call(root)
  result
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
  import scala.collection.mutable

  def findDuplicateSubtrees(root: TreeNode): List[TreeNode] = {
    val count = mutable.Map[String, Int]()
    val duplicates = mutable.ListBuffer[TreeNode]()

    def serialize(node: TreeNode): String = {
      if (node == null) "#"
      else {
        val leftSer = serialize(node.left)
        val rightSer = serialize(node.right)
        val key = s"${node.value},$leftSer,$rightSer"
        count(key) = count.getOrElse(key, 0) + 1
        if (count(key) == 2) duplicates += node
        key
      }
    }

    serialize(root)
    duplicates.toList
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

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

impl Solution {
    pub fn find_duplicate_subtrees(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut map: HashMap<String, i32> = HashMap::new();
        let mut result: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();
        Self::traverse(&root, &mut map, &mut result);
        result
    }

    fn traverse(
        node: &Option<Rc<RefCell<TreeNode>>>,
        map: &mut HashMap<String, i32>,
        result: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> String {
        if let Some(rc_node) = node {
            let (val, left_child, right_child) = {
                let n = rc_node.borrow();
                (n.val, n.left.clone(), n.right.clone())
            };
            let left_serial = Self::traverse(&left_child, map, result);
            let right_serial = Self::traverse(&right_child, map, result);
            let serial = format!("{},{},{}", val, left_serial, right_serial);
            let count = map.entry(serial.clone()).or_insert(0);
            *count += 1;
            if *count == 2 {
                result.push(Some(Rc::clone(rc_node)));
            }
            serial
        } else {
            "#".to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (find-duplicate-subtrees root)
  (-> (or/c tree-node? #f) (listof (or/c tree-node? #f)))
  (let* ([counts (make-hash)]
         [result '()])
    (define (traverse node)
      (if (not node)
          "#"
          (let* ([left-serial (traverse (tree-node-left node))]
                 [right-serial (traverse (tree-node-right node))]
                 [serial (format "~a,~a,~a" (tree-node-val node) left-serial right-serial)])
            (define cnt (hash-ref counts serial 0))
            (when (= cnt 1)
              (set! result (cons node result)))
            (hash-set! counts serial (+ cnt 1))
            serial)))
    (traverse root)
    (reverse result)))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-export([find_duplicate_subtrees/1]).

-spec find_duplicate_subtrees(Root :: #tree_node{} | null) -> [#tree_node{} | null].
find_duplicate_subtrees(Root) ->
    case Root of
        null -> [];
        _ ->
            {_Ser, _Map, Res} = traverse(Root, #{}),
            Res
    end.

traverse(null, Map) ->
    {"#", Map, []};
traverse(Node, Map) when is_record(Node, tree_node) ->
    {LSer, Map1, LRes} = traverse(Node#tree_node.left, Map),
    {RSer, Map2, RRes} = traverse(Node#tree_node.right, Map1),
    Serial = integer_to_list(Node#tree_node.val) ++ "," ++ LSer ++ "," ++ RSer,
    Count = maps:get(Serial, Map2, 0) + 1,
    NewMap = maps:put(Serial, Count, Map2),
    Res =
        case Count of
            2 -> [Node] ++ LRes ++ RRes;
            _ -> LRes ++ RRes
        end,
    {Serial, NewMap, Res}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_duplicate_subtrees(root :: TreeNode.t | nil) :: [TreeNode.t | nil]
  def find_duplicate_subtrees(nil), do: []

  def find_duplicate_subtrees(root) do
    {_ser, {_freq, dup}} = dfs(root, {%{}, []})
    Enum.reverse(dup)
  end

  defp dfs(nil, acc), do: {"#", acc}

  defp dfs(%TreeNode{val: v, left: l, right: r} = node, {freq, dup}) do
    {ls, {freq1, dup1}} = dfs(l, {freq, dup})
    {rs, {freq2, dup2}} = dfs(r, {freq1, dup1})

    ser = Integer.to_string(v) <> "," <> ls <> "," <> rs
    cnt = Map.get(freq2, ser, 0)
    freq3 = Map.put(freq2, ser, cnt + 1)
    dup3 = if cnt == 1, do: [node | dup2], else: dup2

    {ser, {freq3, dup3}}
  end
end
```
