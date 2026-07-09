# 2096. Step-By-Step Directions From a Binary Tree Node to Another

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
    bool dfs(TreeNode* node, int target, std::string& path) {
        if (!node) return false;
        if (node->val == target) return true;
        path.push_back('L');
        if (dfs(node->left, target, path)) return true;
        path.pop_back();
        path.push_back('R');
        if (dfs(node->right, target, path)) return true;
        path.pop_back();
        return false;
    }
    
    std::string getDirections(TreeNode* root, int startValue, int destValue) {
        std::string startPath, destPath;
        dfs(root, startValue, startPath);
        dfs(root, destValue, destPath);
        
        size_t i = 0;
        while (i < startPath.size() && i < destPath.size() && startPath[i] == destPath[i]) {
            ++i;
        }
        std::string result(startPath.size() - i, 'U');
        result += destPath.substr(i);
        return result;
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
    public String getDirections(TreeNode root, int startValue, int destValue) {
        StringBuilder pathToStart = new StringBuilder();
        StringBuilder pathToDest = new StringBuilder();
        dfs(root, startValue, pathToStart);
        dfs(root, destValue, pathToDest);
        String sPath = pathToStart.toString();
        String dPath = pathToDest.toString();

        int i = 0;
        while (i < sPath.length() && i < dPath.length() && sPath.charAt(i) == dPath.charAt(i)) {
            i++;
        }

        StringBuilder result = new StringBuilder();
        for (int j = i; j < sPath.length(); j++) {
            result.append('U');
        }
        result.append(dPath.substring(i));
        return result.toString();
    }

    private boolean dfs(TreeNode node, int target, StringBuilder path) {
        if (node == null) return false;
        if (node.val == target) return true;

        // try left
        path.append('L');
        if (dfs(node.left, target, path)) return true;
        path.deleteCharAt(path.length() - 1);

        // try right
        path.append('R');
        if (dfs(node.right, target, path)) return true;
        path.deleteCharAt(path.length() - 1);
        return false;
    }
}
```

## Python

```python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        sys.setrecursionlimit(200000)

        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if dfs(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right, target, path):
                return True
            path.pop()
            return False

        start_path = []
        dest_path = []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        up_moves = 'U' * (len(start_path) - i)
        down_moves = ''.join(dest_path[i:])
        return up_moves + down_moves
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
from typing import Optional, List

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        sys.setrecursionlimit(10**6)

        def dfs(node: Optional[TreeNode], target: int, path: List[str]) -> bool:
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if dfs(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right, target, path):
                return True
            path.pop()
            return False

        start_path: List[str] = []
        dest_path: List[str] = []
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        up_moves = 'U' * (len(start_path) - i)
        down_moves = ''.join(dest_path[i:])
        return up_moves + down_moves
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static int dfs(struct TreeNode* node, int target, char *path, int *pos) {
    if (!node) return 0;
    if (node->val == target) return 1;

    path[*pos] = 'L';
    (*pos)++;
    if (dfs(node->left, target, path, pos)) return 1;
    (*pos)--; // backtrack

    path[*pos] = 'R';
    (*pos)++;
    if (dfs(node->right, target, path, pos)) return 1;
    (*pos)--; // backtrack

    return 0;
}

char* getDirections(struct TreeNode* root, int startValue, int destValue) {
    /* Maximum possible depth is number of nodes (<=100000). Allocate a bit more. */
    int maxDepth = 200005;
    char *startPath = (char*)malloc(maxDepth);
    char *destPath  = (char*)malloc(maxDepth);

    int startLen = 0, destLen = 0;
    dfs(root, startValue, startPath, &startLen);
    dfs(root, destValue,  destPath,  &destLen);

    int i = 0;
    while (i < startLen && i < destLen && startPath[i] == destPath[i]) {
        ++i;
    }

    int resultLen = (startLen - i) + (destLen - i);
    char *result = (char*)malloc(resultLen + 1);
    int idx = 0;

    for (int j = i; j < startLen; ++j) {
        result[idx++] = 'U';
    }
    for (int j = i; j < destLen; ++j) {
        result[idx++] = destPath[j];
    }
    result[idx] = '\0';

    free(startPath);
    free(destPath);
    return result;
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
    private bool FindPath(TreeNode node, int target, List<char> path) {
        if (node == null) return false;
        if (node.val == target) return true;

        path.Add('L');
        if (FindPath(node.left, target, path)) return true;
        path.RemoveAt(path.Count - 1);

        path.Add('R');
        if (FindPath(node.right, target, path)) return true;
        path.RemoveAt(path.Count - 1);

        return false;
    }

    public string GetDirections(TreeNode root, int startValue, int destValue) {
        var startPath = new List<char>();
        var destPath = new List<char>();

        FindPath(root, startValue, startPath);
        FindPath(root, destValue, destPath);

        int i = 0;
        while (i < startPath.Count && i < destPath.Count && startPath[i] == destPath[i]) {
            i++;
        }

        var sb = new StringBuilder();
        for (int j = i; j < startPath.Count; ++j) {
            sb.Append('U');
        }
        for (int j = i; j < destPath.Count; ++j) {
            sb.Append(destPath[j]);
        }

        return sb.ToString();
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
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) {
    const findPath = (node, target, path) => {
        if (!node) return false;
        if (node.val === target) return true;
        // try left
        path.push('L');
        if (findPath(node.left, target, path)) return true;
        path.pop();
        // try right
        path.push('R');
        if (findPath(node.right, target, path)) return true;
        path.pop();
        return false;
    };
    
    const startPath = [];
    const destPath = [];
    findPath(root, startValue, startPath);
    findPath(root, destValue, destPath);
    
    let i = 0;
    while (i < startPath.length && i < destPath.length && startPath[i] === destPath[i]) {
        i++;
    }
    
    const upMoves = 'U'.repeat(startPath.length - i);
    const downMoves = destPath.slice(i).join('');
    return upMoves + downMoves;
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

function getDirections(root: TreeNode | null, startValue: number, destValue: number): string {
    const startPath: string[] = [];
    const destPath: string[] = [];

    function findPath(node: TreeNode | null, target: number, path: string[]): boolean {
        if (!node) return false;
        if (node.val === target) return true;

        path.push('L');
        if (findPath(node.left, target, path)) return true;
        path.pop();

        path.push('R');
        if (findPath(node.right, target, path)) return true;
        path.pop();

        return false;
    }

    findPath(root, startValue, startPath);
    findPath(root, destValue, destPath);

    let i = 0;
    while (
        i < startPath.length &&
        i < destPath.length &&
        startPath[i] === destPath[i]
    ) {
        i++;
    }

    const upMoves = 'U'.repeat(startPath.length - i);
    const downMoves = destPath.slice(i).join('');
    return upMoves + downMoves;
}
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
     * @param Integer $startValue
     * @param Integer $destValue
     * @return String
     */
    function getDirections($root, $startValue, $destValue) {
        $pathStart = [];
        $pathDest = [];

        $this->dfs($root, $startValue, $pathStart);
        $this->dfs($root, $destValue, $pathDest);

        $i = 0;
        $lenS = count($pathStart);
        $lenD = count($pathDest);
        while ($i < $lenS && $i < $lenD && $pathStart[$i] === $pathDest[$i]) {
            $i++;
        }

        $up = str_repeat('U', $lenS - $i);
        $down = implode('', array_slice($pathDest, $i));

        return $up . $down;
    }

    /**
     * Depth‑first search to record path from root to target.
     *
     * @param TreeNode|null $node
     * @param int $target
     * @param array &$path  // mutable list of directions ('L' or 'R')
     * @return bool          // true if target found in this subtree
     */
    private function dfs($node, $target, &$path) {
        if ($node === null) {
            return false;
        }
        if ($node->val === $target) {
            return true;
        }

        // try left child
        $path[] = 'L';
        if ($this->dfs($node->left, $target, $path)) {
            return true;
        }
        array_pop($path);

        // try right child
        $path[] = 'R';
        if ($this->dfs($node->right, $target, $path)) {
            return true;
        }
        array_pop($path);

        return false;
    }
}
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
    func getDirections(_ root: TreeNode?, _ startValue: Int, _ destValue: Int) -> String {
        var startPath = [Character]()
        var destPath = [Character]()
        _ = findPath(root, startValue, &startPath)
        _ = findPath(root, destValue, &destPath)
        
        var i = 0
        while i < startPath.count && i < destPath.count && startPath[i] == destPath[i] {
            i += 1
        }
        
        let upCount = startPath.count - i
        var result = [Character]()
        for _ in 0..<upCount {
            result.append("U")
        }
        if i < destPath.count {
            result.append(contentsOf: destPath[i...])
        }
        return String(result)
    }
    
    private func findPath(_ node: TreeNode?, _ target: Int, _ path: inout [Character]) -> Bool {
        guard let node = node else { return false }
        if node.val == target {
            return true
        }
        // Explore left child
        path.append("L")
        if findPath(node.left, target, &path) {
            return true
        }
        path.removeLast()
        // Explore right child
        path.append("R")
        if findPath(node.right, target, &path) {
            return true
        }
        path.removeLast()
        return false
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
    fun getDirections(root: TreeNode?, startValue: Int, destValue: Int): String {
        if (root == null) return ""
        val pathToStart = StringBuilder()
        val pathToDest = StringBuilder()
        findPath(root, startValue, pathToStart)
        findPath(root, destValue, pathToDest)

        var i = 0
        while (i < pathToStart.length && i < pathToDest.length &&
            pathToStart[i] == pathToDest[i]) {
            i++
        }

        val result = StringBuilder()
        repeat(pathToStart.length - i) { result.append('U') }
        result.append(pathToDest.substring(i))
        return result.toString()
    }

    private fun findPath(node: TreeNode?, target: Int, path: StringBuilder): Boolean {
        if (node == null) return false
        if (node.`val` == target) return true

        // try left
        path.append('L')
        if (findPath(node.left, target, path)) return true
        path.setLength(path.length - 1)

        // try right
        path.append('R')
        if (findPath(node.right, target, path)) return true
        path.setLength(path.length - 1)

        return false
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
  String getDirections(TreeNode? root, int startValue, int destValue) {
    // Helper DFS to record path from root to target.
    bool dfs(TreeNode? node, int target, StringBuffer path) {
      if (node == null) return false;
      if (node.val == target) return true;

      // Try left child
      path.write('L');
      if (dfs(node.left, target, path)) return true;
      path.length = path.length - 1; // backtrack

      // Try right child
      path.write('R');
      if (dfs(node.right, target, path)) return true;
      path.length = path.length - 1; // backtrack

      return false;
    }

    StringBuffer startBuf = StringBuffer();
    StringBuffer destBuf = StringBuffer();

    dfs(root, startValue, startBuf);
    dfs(root, destValue, destBuf);

    String startPath = startBuf.toString();
    String destPath = destBuf.toString();

    int i = 0;
    while (i < startPath.length &&
        i < destPath.length &&
        startPath[i] == destPath[i]) {
      i++;
    }

    StringBuffer result = StringBuffer();

    // Add 'U' for each step moving up from start to LCA
    for (int j = 0; j < startPath.length - i; ++j) {
      result.write('U');
    }
    // Append the remaining part of dest path after LCA
    if (i < destPath.length) {
      result.write(destPath.substring(i));
    }

    return result.toString();
  }
}
```

## Golang

```go
import "strings"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getDirections(root *TreeNode, startValue int, destValue int) string {
	var startPath []byte
	dfsFindPath(root, startValue, &startPath)
	var destPath []byte
	dfsFindPath(root, destValue, &destPath)

	// find common prefix length
	i := 0
	for i < len(startPath) && i < len(destPath) && startPath[i] == destPath[i] {
		i++
	}

	var sb strings.Builder
	// move up from start to LCA
	for j := i; j < len(startPath); j++ {
		sb.WriteByte('U')
	}
	// then follow path from LCA to destination
	sb.Write(destPath[i:])
	return sb.String()
}

// dfsFindPath records the path from root to target using 'L' and 'R'.
func dfsFindPath(node *TreeNode, target int, path *[]byte) bool {
	if node == nil {
		return false
	}
	if node.Val == target {
		return true
	}
	// try left child
	*path = append(*path, 'L')
	if dfsFindPath(node.Left, target, path) {
		return true
	}
	*path = (*path)[:len(*path)-1]

	// try right child
	*path = append(*path, 'R')
	if dfsFindPath(node.Right, target, path) {
		return true
	}
	*path = (*path)[:len(*path)-1]
	return false
}
```

## Ruby

```ruby
def find_path(node, target, path)
  return false unless node
  return true if node.val == target

  path << 'L'
  if find_path(node.left, target, path)
    return true
  end
  path.pop

  path << 'R'
  if find_path(node.right, target, path)
    return true
  end
  path.pop

  false
end

def get_directions(root, start_value, dest_value)
  start_path = []
  dest_path = []

  find_path(root, start_value, start_path)
  find_path(root, dest_value, dest_path)

  i = 0
  while i < start_path.length && i < dest_path.length && start_path[i] == dest_path[i]
    i += 1
  end

  up_moves = 'U' * (start_path.length - i)
  down_moves = dest_path[i..-1]&.join('') || ''

  up_moves + down_moves
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
    def getDirections(root: TreeNode, startValue: Int, destValue: Int): String = {
        def dfs(node: TreeNode, target: Int, path: StringBuilder): Boolean = {
            if (node == null) false
            else if (node.value == target) true
            else {
                path.append('L')
                if (dfs(node.left, target, path)) return true
                path.setLength(path.length - 1)
                path.append('R')
                if (dfs(node.right, target, path)) return true
                path.setLength(path.length - 1)
                false
            }
        }

        val startPathBuilder = new StringBuilder
        dfs(root, startValue, startPathBuilder)
        val destPathBuilder = new StringBuilder
        dfs(root, destValue, destPathBuilder)

        val startPath = startPathBuilder.toString()
        val destPath = destPathBuilder.toString()

        var i = 0
        while (i < startPath.length && i < destPath.length && startPath.charAt(i) == destPath.charAt(i)) {
            i += 1
        }

        val result = new StringBuilder
        for (_ <- 0 until (startPath.length - i)) result.append('U')
        result.append(destPath.substring(i))
        result.toString()
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode { val, left: None, right: None }
    }
}

pub struct Solution;

impl Solution {
    pub fn get_directions(root: Option<Rc<RefCell<TreeNode>>>, start_value: i32, dest_value: i32) -> String {
        fn dfs(node: Option<&Rc<RefCell<TreeNode>>>, target: i32, path: &mut String) -> bool {
            if let Some(rc) = node {
                let n = rc.borrow();
                if n.val == target {
                    return true;
                }
                // go left
                path.push('L');
                if dfs(n.left.as_ref(), target, path) {
                    return true;
                }
                path.pop();

                // go right
                path.push('R');
                if dfs(n.right.as_ref(), target, path) {
                    return true;
                }
                path.pop();
            }
            false
        }

        let mut start_path = String::new();
        let mut dest_path = String::new();

        dfs(root.as_ref(), start_value, &mut start_path);
        dfs(root.as_ref(), dest_value, &mut dest_path);

        // find common prefix length
        let bytes_start = start_path.as_bytes();
        let bytes_dest = dest_path.as_bytes();
        let mut i = 0;
        while i < bytes_start.len()
            && i < bytes_dest.len()
            && bytes_start[i] == bytes_dest[i]
        {
            i += 1;
        }

        let up_moves = "U".repeat(start_path.len() - i);
        let down_moves = &dest_path[i..];
        format!("{}{}", up_moves, down_moves)
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
;; (struct tree-node
;;   (val left right) #:mutable #:transparent)

(define (dfs node target)
  (cond [(not node) #f]
        [(= (tree-node-val node) target) ""]
        [else
         (let ([left (dfs (tree-node-left node) target)])
           (if left
               (string-append "L" left)
               (let ([right (dfs (tree-node-right node) target)])
                 (if right
                     (string-append "R" right)
                     #f))))]))

(define/contract (get-directions root startValue destValue)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? string?)
  (let* ([start-path (dfs root startValue)]
         [dest-path (dfs root destValue)])
    (unless (and start-path dest-path)
      (error "Start or destination value not found in the tree"))
    (define len-start (string-length start-path))
    (define len-dest (string-length dest-path))
    (define common
      (let loop ((i 0))
        (if (or (= i len-start) (= i len-dest)
                (not (char=? (string-ref start-path i) (string-ref dest-path i))))
            i
            (loop (+ i 1)))))
    (define up-count (- len-start common))
    (string-append (make-string up-count #\U)
                   (substring dest-path common))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                     left = null  :: 'null' | #tree_node{},
                     right = null :: 'null' | #tree_node{}}).

-export([get_directions/3]).

-spec get_directions(Root :: #tree_node{} | null,
                     StartValue :: integer(),
                     DestValue :: integer()) -> unicode:unicode_binary().
get_directions(Root, StartValue, DestValue) ->
    {true, StartPath} = find_path(Root, StartValue),
    {true, DestPath}   = find_path(Root, DestValue),

    CommonLen = common_prefix_len(StartPath, DestPath, 0),

    UpCount = length(StartPath) - CommonLen,
    Ups = lists:duplicate(UpCount, $U),

    RestDest = lists:nthtail(CommonLen, DestPath),
    ResultList = Ups ++ RestDest,
    list_to_binary(ResultList).

%% find_path/2 returns {true, Path} where Path is a list of characters from root to target
-spec find_path(#tree_node{} | null, integer()) -> {boolean(), [integer()]}.
find_path(Node, Target) ->
    case find_path(Node, Target, []) of
        false -> {false, []};
        {true, P} -> {true, P}
    end.

-spec find_path(#tree_node{} | null, integer(), [integer()]) -> false | {true, [integer()]}.
find_path(null, _Target, _Acc) ->
    false;
find_path(#tree_node{val = Val, left = L, right = R}, Target, Acc) ->
    if
        Val =:= Target ->
            {true, lists:reverse(Acc)};
        true ->
            case find_path(L, Target, [$L | Acc]) of
                false ->
                    case find_path(R, Target, [$R | Acc]) of
                        false -> false;
                        Res -> Res
                    end;
                Res -> Res
            end
    end.

-spec common_prefix_len([integer()], [integer()], integer()) -> integer().
common_prefix_len([], _B, Len) -> Len;
common_prefix_len(_A, [], Len) -> Len;
common_prefix_len([H|T1], [H|T2], Len) ->
    common_prefix_len(T1, T2, Len + 1);
common_prefix_len(_, _, Len) -> Len.
```

## Elixir

```elixir
defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule Solution do
  @spec get_directions(root :: TreeNode.t() | nil, start_value :: integer, dest_value :: integer) :: String.t()
  def get_directions(root, start_value, dest_value) do
    start_path = find_path(root, start_value, [])
    dest_path = find_path(root, dest_value, [])

    common_len = common_prefix_len(start_path, dest_path)

    up_moves = String.duplicate("U", length(start_path) - common_len)
    down_moves = Enum.join(Enum.drop(dest_path, common_len))

    up_moves <> down_moves
  end

  defp find_path(nil, _target, _acc), do: nil

  defp find_path(%TreeNode{val: v} = node, target, acc) when v == target,
    do: Enum.reverse(acc)

  defp find_path(node, target, acc) do
    case find_path(node.left, target, ["L" | acc]) do
      nil -> find_path(node.right, target, ["R" | acc])
      path -> path
    end
  end

  defp common_prefix_len([h1 | t1], [h2 | t2]) when h1 == h2,
    do: 1 + common_prefix_len(t1, t2)

  defp common_prefix_len(_, _), do: 0
end
```
