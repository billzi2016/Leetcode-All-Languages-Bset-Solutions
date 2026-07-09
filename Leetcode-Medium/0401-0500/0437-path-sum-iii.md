# 0437. Path Sum III

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
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long,int> prefixCount;
        prefixCount[0] = 1; // empty path
        long long curSum = 0;
        int result = 0;
        dfs(root, targetSum, curSum, prefixCount, result);
        return result;
    }
private:
    void dfs(TreeNode* node, int target, long long curSum,
             unordered_map<long long,int>& cnt, int& res) {
        if (!node) return;
        curSum += node->val;
        long long need = curSum - target;
        auto it = cnt.find(need);
        if (it != cnt.end()) res += it->second;
        ++cnt[curSum];
        dfs(node->left, target, curSum, cnt, res);
        dfs(node->right, target, curSum, cnt, res);
        // backtrack
        if (--cnt[curSum] == 0) cnt.erase(curSum);
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
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0L, 1);
        return dfs(root, 0L, targetSum, prefixCount);
    }

    private int dfs(TreeNode node, long curSum, int target, Map<Long, Integer> map) {
        if (node == null) {
            return 0;
        }
        curSum += node.val;
        int count = map.getOrDefault(curSum - target, 0);
        map.put(curSum, map.getOrDefault(curSum, 0) + 1);
        count += dfs(node.left, curSum, target, map);
        count += dfs(node.right, curSum, target, map);
        map.put(curSum, map.get(curSum) - 1); // backtrack
        return count;
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
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict

        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty path has sum 0

        def dfs(node, cur_sum):
            if not node:
                return 0
            cur_sum += node.val
            total = prefix_counts.get(cur_sum - targetSum, 0)

            prefix_counts[cur_sum] += 1
            total += dfs(node.left, cur_sum)
            total += dfs(node.right, cur_sum)
            prefix_counts[cur_sum] -= 1  # backtrack

            return total

        return dfs(root, 0)
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty path has sum 0
        
        def dfs(node, cur_sum):
            if not node:
                return 0
            cur_sum += node.val
            total = prefix_counts[cur_sum - targetSum]
            prefix_counts[cur_sum] += 1
            total += dfs(node.left, cur_sum)
            total += dfs(node.right, cur_sum)
            prefix_counts[cur_sum] -= 1
            return total
        
        return dfs(root, 0)
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
static int dfs(struct TreeNode* node, long long curSum, int target,
               long long *prefix, int depth) {
    if (!node) return 0;
    curSum += (long long)node->val;
    int cnt = 0;
    if (curSum == target) cnt++;
    for (int i = 0; i < depth; ++i) {
        if (curSum - prefix[i] == target) cnt++;
    }
    prefix[depth] = curSum;
    cnt += dfs(node->left, curSum, target, prefix, depth + 1);
    cnt += dfs(node->right, curSum, target, prefix, depth + 1);
    return cnt;
}

int pathSum(struct TreeNode* root, int targetSum) {
    if (!root) return 0;
    long long prefix[1005]; // max nodes per constraints
    return dfs(root, 0LL, targetSum, prefix, 0);
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
public class Solution {
    public int PathSum(TreeNode root, int targetSum) {
        var prefixCount = new Dictionary<long, int>();
        prefixCount[0] = 1; // empty path has sum 0
        return Dfs(root, 0L, targetSum, prefixCount);
    }

    private int Dfs(TreeNode node, long curSum, int target, Dictionary<long, int> map) {
        if (node == null) return 0;

        int result = 0;
        curSum += node.val;

        long need = curSum - target;
        if (map.TryGetValue(need, out var cnt)) {
            result += cnt;
        }

        // add current sum to map
        if (map.ContainsKey(curSum))
            map[curSum] = map[curSum] + 1;
        else
            map[curSum] = 1;

        result += Dfs(node.left, curSum, target, map);
        result += Dfs(node.right, curSum, target, map);

        // backtrack: remove current sum count
        if (map[curSum] == 1)
            map.Remove(curSum);
        else
            map[curSum] = map[curSum] - 1;

        return result;
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
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    const prefixCount = new Map();
    // base case: empty path sum = 0 occurs once
    prefixCount.set(0, 1);
    let result = 0;
    
    function dfs(node, currSum) {
        if (!node) return;
        currSum += node.val;
        
        // paths ending at current node with required sum
        const need = currSum - targetSum;
        result += prefixCount.get(need) || 0;
        
        // record current prefix sum
        prefixCount.set(currSum, (prefixCount.get(currSum) || 0) + 1);
        
        dfs(node.left, currSum);
        dfs(node.right, currSum);
        
        // backtrack: remove current prefix sum count
        const cnt = prefixCount.get(currSum);
        if (cnt === 1) {
            prefixCount.delete(currSum);
        } else {
            prefixCount.set(currSum, cnt - 1);
        }
    }
    
    dfs(root, 0);
    return result;
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

function pathSum(root: TreeNode | null, targetSum: number): number {
    const prefixCount = new Map<number, number>();
    prefixCount.set(0, 1);
    let result = 0;

    function dfs(node: TreeNode | null, curSum: number): void {
        if (!node) return;
        curSum += node.val;

        const need = curSum - targetSum;
        if (prefixCount.has(need)) {
            result += prefixCount.get(need)!;
        }

        prefixCount.set(curSum, (prefixCount.get(curSum) ?? 0) + 1);
        dfs(node.left, curSum);
        dfs(node.right, curSum);

        const cnt = prefixCount.get(curSum)! - 1;
        if (cnt === 0) {
            prefixCount.delete(curSum);
        } else {
            prefixCount.set(curSum, cnt);
        }
    }

    dfs(root, 0);
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
    private int $ans = 0;

    /**
     * @param TreeNode $root
     * @param Integer $targetSum
     * @return Integer
     */
    function pathSum($root, $targetSum) {
        $prefix = [0 => 1];
        $this->dfs($root, 0, $targetSum, $prefix);
        return $this->ans;
    }

    private function dfs($node, int $currSum, int $target, array &$map): void {
        if ($node === null) {
            return;
        }
        $currSum += $node->val;
        $need = $currSum - $target;
        if (isset($map[$need])) {
            $this->ans += $map[$need];
        }

        if (!isset($map[$currSum])) {
            $map[$currSum] = 0;
        }
        $map[$currSum]++;

        $this->dfs($node->left, $currSum, $target, $map);
        $this->dfs($node->right, $currSum, $target, $map);

        $map[$currSum]--;
        if ($map[$currSum] === 0) {
            unset($map[$currSum]);
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
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> Int {
        var prefixCount = [Int: Int]()
        prefixCount[0] = 1
        var result = 0
        
        func dfs(_ node: TreeNode?, _ currentSum: Int) {
            guard let node = node else { return }
            let newSum = currentSum + node.val
            
            if let cnt = prefixCount[newSum - targetSum] {
                result += cnt
            }
            
            prefixCount[newSum, default: 0] += 1
            dfs(node.left, newSum)
            dfs(node.right, newSum)
            
            // backtrack
            if let cnt = prefixCount[newSum] {
                if cnt == 1 {
                    prefixCount.removeValue(forKey: newSum)
                } else {
                    prefixCount[newSum] = cnt - 1
                }
            }
        }
        
        dfs(root, 0)
        return result
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
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        var result = 0
        val prefixCount = HashMap<Long, Int>()
        prefixCount[0L] = 1

        fun dfs(node: TreeNode?, curSum: Long) {
            if (node == null) return
            val newSum = curSum + node.`val`.toLong()
            result += prefixCount.getOrDefault(newSum - targetSum.toLong(), 0)
            prefixCount[newSum] = prefixCount.getOrDefault(newSum, 0) + 1

            dfs(node.left, newSum)
            dfs(node.right, newSum)

            val cnt = prefixCount[newSum]!! - 1
            if (cnt == 0) {
                prefixCount.remove(newSum)
            } else {
                prefixCount[newSum] = cnt
            }
        }

        dfs(root, 0L)
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
  int pathSum(TreeNode? root, int targetSum) {
    final Map<int, int> prefixCount = {0: 1};
    int result = 0;

    void dfs(TreeNode? node, int currSum) {
      if (node == null) return;
      final int newSum = currSum + node.val;
      result += prefixCount[newSum - targetSum] ?? 0;
      prefixCount[newSum] = (prefixCount[newSum] ?? 0) + 1;

      dfs(node.left, newSum);
      dfs(node.right, newSum);

      // backtrack
      final int count = prefixCount[newSum]! - 1;
      if (count == 0) {
        prefixCount.remove(newSum);
      } else {
        prefixCount[newSum] = count;
      }
    }

    dfs(root, 0);
    return result;
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
func pathSum(root *TreeNode, targetSum int) int {
    prefix := map[int]int{0: 1}
    var dfs func(node *TreeNode, cur int) int
    dfs = func(node *TreeNode, cur int) int {
        if node == nil {
            return 0
        }
        cur += node.Val
        count := prefix[cur-targetSum]
        prefix[cur]++
        count += dfs(node.Left, cur)
        count += dfs(node.Right, cur)
        prefix[cur]--
        return count
    }
    return dfs(root, 0)
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

def path_sum(root, target_sum)
  prefix = Hash.new(0)
  prefix[0] = 1

  dfs = nil
  dfs = ->(node, cur) do
    return 0 unless node
    cur += node.val
    count = prefix[cur - target_sum]
    prefix[cur] += 1
    count += dfs.call(node.left, cur)
    count += dfs.call(node.right, cur)
    prefix[cur] -= 1
    count
  end

  dfs.call(root, 0)
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

  def pathSum(root: TreeNode, targetSum: Int): Int = {
    val prefix = mutable.Map[Long, Int]().withDefaultValue(0)
    prefix.put(0L, 1)
    dfs(root, 0L, targetSum.toLong, prefix)
  }

  private def dfs(node: TreeNode, curSum: Long, target: Long,
                  prefix: mutable.Map[Long, Int]): Int = {
    if (node == null) return 0
    val newSum = curSum + node.value
    var count = prefix.getOrElse(newSum - target, 0)

    // add current sum to map
    prefix.update(newSum, prefix.getOrElse(newSum, 0) + 1)

    count += dfs(node.left, newSum, target, prefix)
    count += dfs(node.right, newSum, target, prefix)

    // backtrack: remove current sum count
    val updated = prefix(newSum) - 1
    if (updated == 0) prefix.remove(newSum) else prefix.update(newSum, updated)

    count
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> i32 {
        fn dfs(
            node: &Option<Rc<RefCell<TreeNode>>>,
            cur_sum: i64,
            target: i64,
            map: &mut HashMap<i64, i32>,
            count: &mut i32,
        ) {
            if let Some(rc) = node {
                let n = rc.borrow();
                let new_sum = cur_sum + n.val as i64;

                if let Some(c) = map.get(&(new_sum - target)) {
                    *count += *c;
                }

                *map.entry(new_sum).or_insert(0) += 1;

                dfs(&n.left, new_sum, target, map, count);
                dfs(&n.right, new_sum, target, map, count);

                if let Some(entry) = map.get_mut(&new_sum) {
                    *entry -= 1;
                }
            }
        }

        let mut count = 0;
        let mut prefix: HashMap<i64, i32> = HashMap::new();
        prefix.insert(0, 1);
        dfs(&root, 0, target_sum as i64, &mut prefix, &mut count);
        count
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (path-sum root targetSum)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (let ((prefix (make-hash)))               ; sum -> count
    (hash-set! prefix 0 1)                  ; empty path
    (define (dfs node cur-sum)
      (if (not node)
          0
          (let* ((new-sum (+ cur-sum (tree-node-val node)))
                 (paths-here (hash-ref prefix (- new-sum targetSum) 0))
                 (_ (hash-set! prefix new-sum (+ (hash-ref prefix new-sum 0) 1)))
                 (left-count (dfs (tree-node-left node) new-sum))
                 (right-count (dfs (tree-node-right node) new-sum))
                 (_ (hash-set! prefix new-sum (- (hash-ref prefix new-sum) 1))))
            (+ paths-here left-count right-count)))))
    (dfs root 0)))
```

## Erlang

```erlang
-module(solution).
-export([path_sum/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec path_sum(Root :: #tree_node{} | null, TargetSum :: integer()) -> integer().
path_sum(Root, TargetSum) ->
    Map0 = #{0 => 1},
    dfs(Root, 0, TargetSum, Map0).

dfs(null, _Curr, _Target, _Map) -> 0;
dfs(Node, Curr, Target, Map) ->
    NewCurr = Curr + Node#tree_node.val,
    PathsHere = maps:get(NewCurr - Target, Map, 0),
    UpdatedMap = maps:update_with(NewCurr,
                                  fun(Count) -> Count + 1 end,
                                  1,
                                  Map),
    LeftCnt = dfs(Node#tree_node.left, NewCurr, Target, UpdatedMap),
    RightCnt = dfs(Node#tree_node.right, NewCurr, Target, UpdatedMap),
    PathsHere + LeftCnt + RightCnt.
```

## Elixir

```elixir
defmodule Solution do
  @spec path_sum(root :: TreeNode.t | nil, target_sum :: integer) :: integer
  def path_sum(root, target_sum) do
    dfs(root, 0, target_sum, %{})
  end

  defp dfs(nil, _cur_sum, _target, _map), do: 0

  defp dfs(%TreeNode{val: v, left: l, right: r}, cur_sum, target, map) do
    new_sum = cur_sum + v

    cnt =
      Map.get(map, new_sum - target, 0)
      |> Kernel.+(if new_sum == target, do: 1, else: 0)

    map2 = Map.update(map, new_sum, 1, &(&1 + 1))

    left_cnt = dfs(l, new_sum, target, map2)
    right_cnt = dfs(r, new_sum, target, map2)

    cnt + left_cnt + right_cnt
  end
end
```
