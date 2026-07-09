# 0077. Combinations

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> cur;
        cur.reserve(k);
        function<void(int)> dfs = [&](int start) {
            if ((int)cur.size() == k) {
                res.push_back(cur);
                return;
            }
            // prune: need enough remaining numbers to fill cur
            for (int i = start; i <= n - (k - cur.size()) + 1; ++i) {
                cur.push_back(i);
                dfs(i + 1);
                cur.pop_back();
            }
        };
        dfs(1);
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (k == 0 || n < k) return res;
        Deque<Integer> path = new ArrayDeque<>();
        backtrack(1, n, k, path, res);
        return res;
    }

    private void backtrack(int start, int n, int k, Deque<Integer> path, List<List<Integer>> res) {
        if (path.size() == k) {
            res.add(new ArrayList<>(path));
            return;
        }
        // Prune: need enough remaining numbers to fill the combination
        for (int i = start; i <= n - (k - path.size()) + 1; i++) {
            path.addLast(i);
            backtrack(i + 1, n, k, path, res);
            path.removeLast();
        }
    }
}
```

## Python

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        comb = []

        def backtrack(start):
            if len(comb) == k:
                result.append(comb[:])
                return
            # prune: not enough numbers left to fill the combination
            for i in range(start, n + 1):
                if n - i + 1 < k - len(comb):
                    break
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: List[List[int]] = []
        comb: List[int] = []

        def backtrack(start: int) -> None:
            if len(comb) == k:
                res.append(comb.copy())
                return
            # prune: ensure enough numbers remain to fill the combination
            for i in range(start, n - (k - len(comb)) + 2):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()

        backtrack(1)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void dfs(int start, int n, int k, int *comb, int depth,
                int **res, int *colSizes, int *idx) {
    if (depth == k) {
        int *tmp = (int *)malloc(k * sizeof(int));
        memcpy(tmp, comb, k * sizeof(int));
        res[*idx] = tmp;
        colSizes[*idx] = k;
        (*idx)++;
        return;
    }
    for (int i = start; i <= n - (k - depth) + 1; ++i) {
        comb[depth] = i;
        dfs(i + 1, n, k, comb, depth + 1, res, colSizes, idx);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {
    // compute total number of combinations C(n,k)
    long long cap = 1;
    int kk = k;
    if (kk > n - kk) kk = n - kk;          // use smaller side
    for (int i = 1; i <= kk; ++i) {
        cap = cap * (n - kk + i) / i;
    }
    size_t total = (size_t)cap;

    int **res = (int **)malloc(total * sizeof(int *));
    int *colSizes = (int *)malloc(total * sizeof(int));

    int *comb = (int *)malloc(k * sizeof(int));
    int idx = 0;
    dfs(1, n, k, comb, 0, res, colSizes, &idx);

    free(comb);
    *returnSize = idx;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<IList<int>> Combine(int n, int k)
    {
        var result = new List<IList<int>>();
        if (k == 0 || n < k) return result;
        Backtrack(1, new List<int>());
        return result;

        void Backtrack(int start, List<int> path)
        {
            if (path.Count == k)
            {
                result.Add(new List<int>(path));
                return;
            }

            // Prune: need enough remaining numbers to fill the combination
            for (int i = start; i <= n - (k - path.Count) + 1; i++)
            {
                path.Add(i);
                Backtrack(i + 1, path);
                path.RemoveAt(path.Count - 1);
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    const result = [];
    const path = [];

    const backtrack = (start) => {
        if (path.length === k) {
            result.push([...path]);
            return;
        }
        // Prune: ensure enough numbers remain to fill the combination
        for (let i = start; i <= n - (k - path.length) + 1; i++) {
            path.push(i);
            backtrack(i + 1);
            path.pop();
        }
    };

    backtrack(1);
    return result;
};
```

## Typescript

```typescript
function combine(n: number, k: number): number[][] {
    const result: number[][] = [];
    const combo: number[] = [];

    function backtrack(start: number) {
        if (combo.length === k) {
            result.push([...combo]);
            return;
        }
        // Prune branches where not enough numbers remain
        for (let i = start; i <= n - (k - combo.length) + 1; i++) {
            combo.push(i);
            backtrack(i + 1);
            combo.pop();
        }
    }

    backtrack(1);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[][]
     */
    function combine($n, $k) {
        $result = [];

        $backtrack = function($start, $path) use (&$backtrack, &$result, $n, $k) {
            if (count($path) === $k) {
                $result[] = $path;
                return;
            }

            // Prune: need enough remaining numbers to fill the combination
            $remainingNeeded = $k - count($path);
            for ($i = $start; $i <= $n - $remainingNeeded + 1; $i++) {
                $path[] = $i;
                $backtrack($i + 1, $path);
                array_pop($path);
            }
        };

        $backtrack(1, []);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        var result = [[Int]]()
        var path = [Int]()
        
        func backtrack(_ start: Int) {
            if path.count == k {
                result.append(path)
                return
            }
            var i = start
            while i <= n {
                // Prune branches that cannot fill the remaining slots
                if n - i + 1 < k - path.count { break }
                path.append(i)
                backtrack(i + 1)
                path.removeLast()
                i += 1
            }
        }
        
        backtrack(1)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val current = mutableListOf<Int>()
        fun backtrack(start: Int) {
            if (current.size == k) {
                result.add(ArrayList(current))
                return
            }
            for (i in start..n - (k - current.size) + 1) {
                current.add(i)
                backtrack(i + 1)
                current.removeAt(current.lastIndex)
            }
        }
        backtrack(1)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> combine(int n, int k) {
    final List<List<int>> result = [];
    final List<int> path = [];

    void backtrack(int start) {
      if (path.length == k) {
        result.add(List.from(path));
        return;
      }
      // Prune: need enough remaining numbers to fill the combination
      for (int i = start; i <= n - (k - path.length) + 1; i++) {
        path.add(i);
        backtrack(i + 1);
        path.removeLast();
      }
    }

    backtrack(1);
    return result;
  }
}
```

## Golang

```go
func combine(n int, k int) [][]int {
	var res [][]int
	var path []int

	var backtrack func(start int)
	backtrack = func(start int) {
		if len(path) == k {
			tmp := make([]int, k)
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		// prune: ensure enough remaining numbers to fill the combination
		for i := start; i <= n-(k-len(path))+1; i++ {
			path = append(path, i)
			backtrack(i + 1)
			path = path[:len(path)-1]
		}
	}

	backtrack(1)
	return res
}
```

## Ruby

```ruby
def combine(n, k)
  results = []
  combo = []

  dfs = lambda do |start|
    if combo.size == k
      results << combo.clone
      return
    end
    (start..n).each do |i|
      # prune if not enough numbers left to fill the combination
      break if n - i + 1 < k - combo.size
      combo << i
      dfs.call(i + 1)
      combo.pop
    end
  end

  dfs.call(1)
  results
end
```

## Scala

```scala
object Solution {
    def combine(n: Int, k: Int): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        val current = scala.collection.mutable.ArrayBuffer[Int]()

        def backtrack(start: Int): Unit = {
            if (current.size == k) {
                result += current.toList
                return
            }
            var i = start
            // prune: need enough remaining numbers to fill the combination
            while (i <= n - (k - current.size) + 1) {
                current.append(i)
                backtrack(i + 1)
                current.remove(current.size - 1)
                i += 1
            }
        }

        backtrack(1)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        fn backtrack(start: i32, n: i32, k: usize, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            if path.len() == k {
                res.push(path.clone());
                return;
            }
            for i in start..=n {
                // Prune branches where remaining numbers are insufficient
                let needed = k - path.len();
                let available = (n - i + 1) as usize;
                if available < needed {
                    break;
                }
                path.push(i);
                backtrack(i + 1, n, k, path, res);
                path.pop();
            }
        }

        let mut result = Vec::new();
        if k == 0 || n < k {
            return result;
        }
        let mut current = Vec::with_capacity(k as usize);
        backtrack(1, n, k as usize, &mut current, &mut result);
        result
    }
}
```

## Racket

```racket
(define/contract (combine n k)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)))
  (letrec ((choose
            (lambda (start k)
              (cond [(= k 0) (list '())]
                    [(> start n) '()]
                    [else
                     (append
                       (map (lambda (comb) (cons start comb))
                            (choose (+ start 1) (- k 1)))
                       (choose (+ start 1) k))]))))
    (choose 1 k)))
```

## Erlang

```erlang
-export([combine/2]).
-spec combine(N :: integer(), K :: integer()) -> [[integer()]].
combine(N, K) ->
    comb(1, N, K).

comb(_Start, _N, 0) -> [[]];
comb(Start, N, K) when Start > N; K < 0 -> [];
comb(Start, N, K) when K > N - Start + 1 -> [];
comb(Start, N, K) ->
    With = [ [Start | Rest] || Rest <- comb(Start + 1, N, K - 1) ],
    Without = comb(Start + 1, N, K),
    With ++ Without.
```

## Elixir

```elixir
defmodule Solution do
  @spec combine(n :: integer, k :: integer) :: [[integer]]
  def combine(n, k) do
    backtrack(1, n, k, [], [])
    |> Enum.reverse()
  end

  defp backtrack(_start, _n, 0, path, acc) do
    [Enum.reverse(path) | acc]
  end

  defp backtrack(start, n, k, path, acc) when start > n do
    acc
  end

  defp backtrack(start, n, k, path, acc) do
    max = n - k + 1
    Enum.reduce_while(start..max, acc, fn i, a ->
      new_path = [i | path]
      a2 = backtrack(i + 1, n, k - 1, new_path, a)
      {:cont, a2}
    end)
  end
end
```
