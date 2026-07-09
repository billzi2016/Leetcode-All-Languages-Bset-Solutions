# 1361. Validate Binary Tree Nodes

## Cpp

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        vector<int> indegree(n, 0);
        for (int i = 0; i < n; ++i) {
            int l = leftChild[i];
            if (l != -1) {
                if (++indegree[l] > 1) return false;
            }
            int r = rightChild[i];
            if (r != -1) {
                if (++indegree[r] > 1) return false;
            }
        }
        int root = -1, rootsCount = 0;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) {
                ++rootsCount;
                root = i;
            }
        }
        if (rootsCount != 1) return false;
        vector<char> visited(n, 0);
        queue<int> q;
        q.push(root);
        visited[root] = 1;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            int l = leftChild[node];
            if (l != -1) {
                if (visited[l]) return false;
                visited[l] = 1;
                q.push(l);
            }
            int r = rightChild[node];
            if (r != -1) {
                if (visited[r]) return false;
                visited[r] = 1;
                q.push(r);
            }
        }
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] indegree = new int[n];
        for (int i = 0; i < n; i++) {
            int l = leftChild[i];
            if (l != -1) {
                indegree[l]++;
                if (indegree[l] > 1) return false;
            }
            int r = rightChild[i];
            if (r != -1) {
                indegree[r]++;
                if (indegree[r] > 1) return false;
            }
        }

        int root = -1;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                if (root != -1) return false; // multiple roots
                root = i;
            }
        }
        if (root == -1) return false; // no root

        boolean[] visited = new boolean[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(root);
        visited[root] = true;
        int count = 0;

        while (!stack.isEmpty()) {
            int node = stack.pop();
            count++;

            int l = leftChild[node];
            if (l != -1) {
                if (visited[l]) return false;
                visited[l] = true;
                stack.push(l);
            }

            int r = rightChild[node];
            if (r != -1) {
                if (visited[r]) return false;
                visited[r] = true;
                stack.push(r);
            }
        }

        return count == n;
    }
}
```

## Python

```python
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        indeg = [0] * n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l != -1:
                indeg[l] += 1
                if indeg[l] > 1:
                    return False
            if r != -1:
                indeg[r] += 1
                if indeg[r] > 1:
                    return False

        roots = [i for i in range(n) if indeg[i] == 0]
        if len(roots) != 1:
            return False
        root = roots[0]

        stack = [root]
        visited = set([root])
        while stack:
            node = stack.pop()
            for child in (leftChild[node], rightChild[node]):
                if child == -1:
                    continue
                if child in visited:
                    return False
                visited.add(child)
                stack.append(child)

        return len(visited) == n
```

## Python3

```python
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indeg = [0] * n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l != -1:
                indeg[l] += 1
                if indeg[l] > 1:
                    return False
            if r != -1:
                indeg[r] += 1
                if indeg[r] > 1:
                    return False

        roots = [i for i in range(n) if indeg[i] == 0]
        if len(roots) != 1:
            return False
        root = roots[0]

        visited = [False] * n
        stack = [root]
        visited[root] = True
        while stack:
            node = stack.pop()
            for child in (leftChild[node], rightChild[node]):
                if child == -1:
                    continue
                if visited[child]:
                    return False
                visited[child] = True
                stack.append(child)

        return all(visited)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool validateBinaryTreeNodes(int n, int* leftChild, int leftChildSize, int* rightChild, int rightChildSize) {
    if (n == 0) return false;
    
    int *indeg = (int *)calloc(n, sizeof(int));
    if (!indeg) return false; // allocation failure
    
    for (int i = 0; i < n; ++i) {
        int lc = leftChild[i];
        if (lc != -1) {
            indeg[lc]++;
            if (indeg[lc] > 1) {
                free(indeg);
                return false;
            }
        }
        int rc = rightChild[i];
        if (rc != -1) {
            indeg[rc]++;
            if (indeg[rc] > 1) {
                free(indeg);
                return false;
            }
        }
    }
    
    int root = -1, roots = 0;
    for (int i = 0; i < n; ++i) {
        if (indeg[i] == 0) {
            root = i;
            roots++;
        }
    }
    free(indeg);
    if (roots != 1) return false;
    
    bool *visited = (bool *)calloc(n, sizeof(bool));
    if (!visited) return false;
    
    int *stack = (int *)malloc(n * sizeof(int));
    if (!stack) {
        free(visited);
        return false;
    }
    
    int top = 0;
    stack[top++] = root;
    visited[root] = true;
    int count = 1;
    
    while (top > 0) {
        int node = stack[--top];
        int children[2] = { leftChild[node], rightChild[node] };
        for (int k = 0; k < 2; ++k) {
            int child = children[k];
            if (child == -1) continue;
            if (visited[child]) {
                free(visited);
                free(stack);
                return false;
            }
            visited[child] = true;
            stack[top++] = child;
            count++;
        }
    }
    
    free(visited);
    free(stack);
    return count == n;
}
```

## Csharp

```csharp
public class Solution {
    public bool ValidateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] indeg = new int[n];
        for (int i = 0; i < n; i++) {
            if (leftChild[i] != -1) {
                indeg[leftChild[i]]++;
                if (indeg[leftChild[i]] > 1) return false;
            }
            if (rightChild[i] != -1) {
                indeg[rightChild[i]]++;
                if (indeg[rightChild[i]] > 1) return false;
            }
        }

        int root = -1;
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                if (root != -1) return false; // multiple roots
                root = i;
            }
        }
        if (root == -1) return false;

        bool[] visited = new bool[n];
        var stack = new System.Collections.Generic.Stack<int>();
        stack.Push(root);
        visited[root] = true;

        while (stack.Count > 0) {
            int node = stack.Pop();
            int left = leftChild[node];
            if (left != -1) {
                if (visited[left]) return false;
                visited[left] = true;
                stack.Push(left);
            }
            int right = rightChild[node];
            if (right != -1) {
                if (visited[right]) return false;
                visited[right] = true;
                stack.Push(right);
            }
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} leftChild
 * @param {number[]} rightChild
 * @return {boolean}
 */
var validateBinaryTreeNodes = function(n, leftChild, rightChild) {
    const indegree = new Array(n).fill(0);
    
    for (let i = 0; i < n; i++) {
        const l = leftChild[i];
        const r = rightChild[i];
        if (l !== -1) {
            indegree[l]++;
            if (indegree[l] > 1) return false; // multiple parents
        }
        if (r !== -1) {
            indegree[r]++;
            if (indegree[r] > 1) return false;
        }
    }
    
    let root = -1, rootsCount = 0;
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            root = i;
            rootsCount++;
        } else if (indegree[i] > 1) {
            return false;
        }
    }
    
    if (rootsCount !== 1) return false;
    
    const visited = new Array(n).fill(false);
    const stack = [root];
    visited[root] = true;
    let visitedCount = 0;
    
    while (stack.length) {
        const node = stack.pop();
        visitedCount++;
        const children = [leftChild[node], rightChild[node]];
        for (const child of children) {
            if (child === -1) continue;
            if (visited[child]) return false; // cycle or multiple parents
            visited[child] = true;
            stack.push(child);
        }
    }
    
    return visitedCount === n;
};
```

## Typescript

```typescript
function validateBinaryTreeNodes(n: number, leftChild: number[], rightChild: number[]): boolean {
    const indegree = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        const l = leftChild[i];
        if (l !== -1) {
            indegree[l]++;
            if (indegree[l] > 1) return false;
        }
        const r = rightChild[i];
        if (r !== -1) {
            indegree[r]++;
            if (indegree[r] > 1) return false;
        }
    }

    let root = -1;
    for (let i = 0; i < n; i++) {
        if (indegree[i] === 0) {
            if (root !== -1) return false; // multiple roots
            root = i;
        } else if (indegree[i] !== 1) {
            return false; // should be exactly one parent
        }
    }

    if (root === -1) return false;

    const visited = new Array(n).fill(false);
    const stack: number[] = [root];
    visited[root] = true;

    while (stack.length) {
        const node = stack.pop()!;
        const l = leftChild[node];
        if (l !== -1) {
            if (visited[l]) return false;
            visited[l] = true;
            stack.push(l);
        }
        const r = rightChild[node];
        if (r !== -1) {
            if (visited[r]) return false;
            visited[r] = true;
            stack.push(r);
        }
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $leftChild
     * @param Integer[] $rightChild
     * @return Boolean
     */
    function validateBinaryTreeNodes($n, $leftChild, $rightChild) {
        // Compute indegrees and ensure no node has more than one parent
        $indeg = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $lc = $leftChild[$i];
            if ($lc != -1) {
                $indeg[$lc]++;
                if ($indeg[$lc] > 1) {
                    return false;
                }
            }
            $rc = $rightChild[$i];
            if ($rc != -1) {
                $indeg[$rc]++;
                if ($indeg[$rc] > 1) {
                    return false;
                }
            }
        }

        // Find the root (exactly one node with indegree 0)
        $root = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) {
                if ($root != -1) { // more than one root
                    return false;
                }
                $root = $i;
            }
        }
        if ($root == -1) {
            return false; // no root found
        }

        // DFS to check connectivity and cycles
        $visited = array_fill(0, $n, false);
        $stack = [$root];
        $visited[$root] = true;

        while (!empty($stack)) {
            $node = array_pop($stack);

            $lc = $leftChild[$node];
            if ($lc != -1) {
                if ($visited[$lc]) {
                    return false; // cycle or multiple parents detected during traversal
                }
                $visited[$lc] = true;
                $stack[] = $lc;
            }

            $rc = $rightChild[$node];
            if ($rc != -1) {
                if ($visited[$rc]) {
                    return false;
                }
                $visited[$rc] = true;
                $stack[] = $rc;
            }
        }

        // Ensure all nodes were visited (connected)
        foreach ($visited as $v) {
            if (!$v) {
                return false;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func validateBinaryTreeNodes(_ n: Int, _ leftChild: [Int], _ rightChild: [Int]) -> Bool {
        if n == 0 { return true }
        var indegree = Array(repeating: 0, count: n)
        
        for i in 0..<n {
            let l = leftChild[i]
            if l != -1 {
                indegree[l] += 1
                if indegree[l] > 1 { return false }
            }
            let r = rightChild[i]
            if r != -1 {
                indegree[r] += 1
                if indegree[r] > 1 { return false }
            }
        }
        
        var root = -1
        for i in 0..<n {
            if indegree[i] == 0 {
                if root != -1 { // more than one root
                    return false
                }
                root = i
            } else if indegree[i] > 1 {
                return false
            }
        }
        
        if root == -1 { return false }
        
        var visited = Array(repeating: false, count: n)
        var stack = [Int]()
        stack.append(root)
        visited[root] = true
        
        while !stack.isEmpty {
            let node = stack.removeLast()
            let l = leftChild[node]
            if l != -1 {
                if visited[l] { return false }
                visited[l] = true
                stack.append(l)
            }
            let r = rightChild[node]
            if r != -1 {
                if visited[r] { return false }
                visited[r] = true
                stack.append(r)
            }
        }
        
        for v in visited where !v {
            return false
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validateBinaryTreeNodes(n: Int, leftChild: IntArray, rightChild: IntArray): Boolean {
        val indeg = IntArray(n)
        for (i in 0 until n) {
            val l = leftChild[i]
            if (l != -1) indeg[l]++
            val r = rightChild[i]
            if (r != -1) indeg[r]++
        }
        var root = -1
        for (i in 0 until n) {
            when {
                indeg[i] == 0 -> {
                    if (root != -1) return false // multiple roots
                    root = i
                }
                indeg[i] > 1 -> return false // node has more than one parent
            }
        }
        if (root == -1) return false

        val visited = BooleanArray(n)
        val queue: ArrayDeque<Int> = ArrayDeque()
        queue.add(root)
        visited[root] = true
        var count = 0

        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            count++
            val l = leftChild[node]
            if (l != -1) {
                if (visited[l]) return false
                visited[l] = true
                queue.add(l)
            }
            val r = rightChild[node]
            if (r != -1) {
                if (visited[r]) return false
                visited[r] = true
                queue.add(r)
            }
        }
        return count == n
    }
}
```

## Dart

```dart
class Solution {
  bool validateBinaryTreeNodes(int n, List<int> leftChild, List<int> rightChild) {
    // Compute indegrees for each node.
    List<int> indegree = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int l = leftChild[i];
      if (l != -1) {
        indegree[l]++;
        if (indegree[l] > 1) return false;
      }
      int r = rightChild[i];
      if (r != -1) {
        indegree[r]++;
        if (indegree[r] > 1) return false;
      }
    }

    // Find the unique root (node with indegree 0).
    int root = -1;
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        if (root != -1) return false; // more than one root
        root = i;
      }
    }
    if (root == -1) return false; // no root found

    // DFS traversal to ensure connectivity and detect cycles.
    List<int> stack = [root];
    List<bool> visited = List.filled(n, false);
    visited[root] = true;
    int visitedCount = 0;

    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      visitedCount++;

      int l = leftChild[node];
      if (l != -1) {
        if (visited[l]) return false; // cycle or multiple parents
        visited[l] = true;
        stack.add(l);
      }

      int r = rightChild[node];
      if (r != -1) {
        if (visited[r]) return false;
        visited[r] = true;
        stack.add(r);
      }
    }

    return visitedCount == n;
  }
}
```

## Golang

```go
func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
	if n == 0 {
		return true
	}
	indeg := make([]int, n)
	for i := 0; i < n; i++ {
		if leftChild[i] != -1 {
			if leftChild[i] < 0 || leftChild[i] >= n {
				return false
			}
			indeg[leftChild[i]]++
			if indeg[leftChild[i]] > 1 {
				return false
			}
		}
		if rightChild[i] != -1 {
			if rightChild[i] < 0 || rightChild[i] >= n {
				return false
			}
			indeg[rightChild[i]]++
			if indeg[rightChild[i]] > 1 {
				return false
			}
		}
	}

	root := -1
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			if root != -1 { // more than one root
				return false
			}
			root = i
		}
	}
	if root == -1 { // no root
		return false
	}

	visited := make([]bool, n)
	stack := []int{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if visited[node] {
			return false // cycle detected
		}
		visited[node] = true

		left := leftChild[node]
		if left != -1 {
			if visited[left] {
				return false
			}
			stack = append(stack, left)
		}
		right := rightChild[node]
		if right != -1 {
			if visited[right] {
				return false
			}
			stack = append(stack, right)
		}
	}

	for i := 0; i < n; i++ {
		if !visited[i] {
			return false // disconnected node
		}
	}
	return true
}
```

## Ruby

```ruby
def validate_binary_tree_nodes(n, left_child, right_child)
  indegree = Array.new(n, 0)

  n.times do |i|
    lc = left_child[i]
    rc = right_child[i]
    indegree[lc] += 1 if lc != -1
    indegree[rc] += 1 if rc != -1
  end

  root = nil
  roots_count = 0
  n.times do |i|
    if indegree[i] == 0
      root = i
      roots_count += 1
    elsif indegree[i] > 1
      return false
    end
  end

  return false unless roots_count == 1

  visited = Array.new(n, false)
  stack = [root]

  until stack.empty?
    node = stack.pop
    return false if visited[node]
    visited[node] = true

    lc = left_child[node]
    rc = right_child[node]

    if lc != -1
      return false if visited[lc]
      stack << lc
    end
    if rc != -1
      return false if visited[rc]
      stack << rc
    end
  end

  visited.all?
end
```

## Scala

```scala
object Solution {
  def validateBinaryTreeNodes(n: Int, leftChild: Array[Int], rightChild: Array[Int]): Boolean = {
    val indeg = new Array[Int](n)
    for (i <- 0 until n) {
      val l = leftChild(i)
      if (l != -1) {
        indeg(l) += 1
        if (indeg(l) > 1) return false
      }
      val r = rightChild(i)
      if (r != -1) {
        indeg(r) += 1
        if (indeg(r) > 1) return false
      }
    }

    var root = -1
    var rootsCount = 0
    for (i <- 0 until n) {
      if (indeg(i) == 0) {
        root = i
        rootsCount += 1
      }
    }
    if (rootsCount != 1) return false

    val visited = new Array[Boolean](n)
    val stack = new java.util.ArrayDeque[Int]()
    stack.push(root)
    visited(root) = true
    var visitedCount = 0

    while (!stack.isEmpty) {
      val node = stack.pop()
      visitedCount += 1

      val l = leftChild(node)
      if (l != -1) {
        if (visited(l)) return false
        visited(l) = true
        stack.push(l)
      }

      val r = rightChild(node)
      if (r != -1) {
        if (visited(r)) return false
        visited(r) = true
        stack.push(r)
      }
    }

    visitedCount == n
  }
}
```

## Rust

```rust
impl Solution {
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        let n = n as usize;
        if left_child.len() != n || right_child.len() != n {
            return false;
        }

        // indegree to detect multiple parents
        let mut indegree = vec![0usize; n];
        for i in 0..n {
            let lc = left_child[i];
            if lc != -1 {
                let c = lc as usize;
                indegree[c] += 1;
                if indegree[c] > 1 {
                    return false;
                }
            }
            let rc = right_child[i];
            if rc != -1 {
                let c = rc as usize;
                indegree[c] += 1;
                if indegree[c] > 1 {
                    return false;
                }
            }
        }

        // find the unique root
        let roots: Vec<usize> = (0..n).filter(|&i| indegree[i] == 0).collect();
        if roots.len() != 1 {
            return false;
        }
        let root = roots[0];

        // DFS traversal to check connectivity and cycles
        let mut visited = vec![false; n];
        let mut stack = Vec::new();
        stack.push(root);
        while let Some(node) = stack.pop() {
            if visited[node] {
                return false;
            }
            visited[node] = true;

            let lc = left_child[node];
            if lc != -1 {
                let c = lc as usize;
                if visited[c] {
                    return false;
                }
                stack.push(c);
            }

            let rc = right_child[node];
            if rc != -1 {
                let c = rc as usize;
                if visited[c] {
                    return false;
                }
                stack.push(c);
            }
        }

        // all nodes must be visited
        visited.iter().all(|&v| v)
    }
}
```

## Racket

```racket
(define/contract (validate-binary-tree-nodes n leftChild rightChild)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) boolean?)
  (let* ([lvec (list->vector leftChild)]
         [rvec (list->vector rightChild)]
         [indeg (make-vector n 0)])
    ;; compute indegrees and check for multiple parents
    (for ([i (in-range n)])
      (for ([child (in-list (list (vector-ref lvec i) (vector-ref rvec i)))])
        (when (not (= child -1))
          (let* ([prev (vector-ref indeg child)]
                 [new (+ prev 1)])
            (vector-set! indeg child new)
            (when (> new 1)
              (return #f))))))
    ;; find root
    (define roots '())
    (for ([i (in-range n)])
      (when (= (vector-ref indeg i) 0)
        (set! roots (cons i roots))))
    (if (not (= (length roots) 1))
        #f
        (let* ([root (car roots)]
               [visited (make-vector n #f)])
          (vector-set! visited root #t)
          (let loop ((stack (list root)) (cnt 1) (valid #t))
            (cond
              [(or (null? stack) (not valid)) (and valid (= cnt n))]
              [else
               (define node (car stack))
               (define rest (cdr stack))
               (define new-stack rest)
               (define new-cnt cnt)
               (define still-valid valid)
               (for ([child (in-list (list (vector-ref lvec node) (vector-ref rvec node)))])
                 (when (not (= child -1))
                   (if (vector-ref visited child)
                       (set! still-valid #f)
                       (begin
                         (vector-set! visited child #t)
                         (set! new-cnt (+ new-cnt 1))
                         (set! new-stack (cons child new-stack))))))
               (loop new-stack new-cnt still-valid)]))))))
```

## Erlang

```erlang
-spec validate_binary_tree_nodes(N :: integer(), LeftChild :: [integer()], RightChild :: [integer()]) -> boolean().
validate_binary_tree_nodes(N, LeftChild, RightChild) ->
    Indegrees = build_indegrees(LeftChild, RightChild),
    case check_indegrees(Indegrees) of
        false -> false;
        true ->
            RootCandidates = [I || I <- lists:seq(0, N - 1), maps:get(I, Indegrees, 0) == 0],
            case length(RootCandidates) of
                1 ->
                    Root = hd(RootCandidates),
                    case traverse(N, LeftChild, RightChild, Root) of
                        {ok, Count} -> Count == N;
                        error -> false
                    end;
                _ -> false
            end
    end.

build_indegrees(LeftChild, RightChild) ->
    lists:foldl(fun(I, Acc) ->
        L = lists:nth(I + 1, LeftChild),
        R = lists:nth(I + 1, RightChild),
        Acc1 = if L =/= -1 -> maps:update_with(L, fun(V) -> V + 1 end, 1, Acc); true -> Acc end,
        if R =/= -1 -> maps:update_with(R, fun(V) -> V + 1 end, 1, Acc1); true -> Acc1 end
    end, #{}, lists:seq(0, length(LeftChild) - 1)).

check_indegrees(Map) ->
    Values = maps:values(Map),
    lists:all(fun(V) -> V =< 1 end, Values).

traverse(_N, LeftChild, RightChild, Root) ->
    traverse_loop([Root], #{Root => true}, LeftChild, RightChild).

traverse_loop([], Visited, _LeftChild, _RightChild) ->
    {ok, maps:size(Visited)};
traverse_loop([Node | RestStack], Visited, LeftChild, RightChild) ->
    L = lists:nth(Node + 1, LeftChild),
    R = lists:nth(Node + 1, RightChild),
    case process_child(L, RestStack, Visited) of
        error -> error;
        {Stack1, Vis1} ->
            case process_child(R, Stack1, Vis1) of
                error -> error;
                {Stack2, Vis2} ->
                    traverse_loop(Stack2, Vis2, LeftChild, RightChild)
            end
    end.

process_child(-1, Stack, Visited) ->
    {Stack, Visited};
process_child(Child, Stack, Visited) ->
    case maps:is_key(Child, Visited) of
        true -> error;
        false -> {[Child | Stack], maps:put(Child, true, Visited)}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec validate_binary_tree_nodes(n :: integer, left_child :: [integer], right_child :: [integer]) :: boolean
  def validate_binary_tree_nodes(n, left_child, right_child) do
    left_t = List.to_tuple(left_child)
    right_t = List.to_tuple(right_child)

    indeg_map =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        left = elem(left_t, i)
        acc = if left != -1, do: Map.update(acc, left, 1, &(&1 + 1)), else: acc

        right = elem(right_t, i)
        if right != -1, do: Map.update(acc, right, 1, &(&1 + 1)), else: acc
      end)

    roots =
      Enum.filter(0..(n - 1), fn i ->
        Map.get(indeg_map, i, 0) == 0
      end)

    case roots do
      [root] -> traverse(root, n, left_t, right_t)
      _ -> false
    end
  end

  defp traverse(root, n, left_t, right_t) do
    case dfs([root], MapSet.new(), left_t, right_t) do
      {:ok, visited} -> MapSet.size(visited) == n
      :error -> false
    end
  end

  defp dfs([], visited, _left_t, _right_t), do: {:ok, visited}

  defp dfs([node | rest], visited, left_t, right_t) do
    if MapSet.member?(visited, node) do
      :error
    else
      visited = MapSet.put(visited, node)

      left = elem(left_t, node)
      right = elem(right_t, node)

      stack =
        rest
        |> (fn s -> if left != -1, do: [left | s], else: s end).()
        |> (fn s -> if right != -1, do: [right | s], else: s end).()

      dfs(stack, visited, left_t, right_t)
    end
  end
end
```
