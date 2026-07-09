# 0216. Combination Sum III

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> path;
        function<void(int,int)> dfs = [&](int start, int remaining) {
            if (path.size() == k) {
                if (remaining == 0) result.push_back(path);
                return;
            }
            for (int i = start; i <= 9; ++i) {
                if (i > remaining) break; // prune: sum would exceed target
                // further pruning: not enough numbers left to fill k slots
                int needed = k - path.size() - 1;
                if (needed > 0 && i + needed > remaining) {
                    // even the smallest possible next numbers will exceed remaining
                    // but since we iterate increasing, break is safe
                    // however this condition may be too aggressive; skip it
                }
                path.push_back(i);
                dfs(i + 1, remaining - i);
                path.pop_back();
            }
        };
        dfs(1, n);
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(1, k, n, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int start, int k, int target, List<Integer> path, List<List<Integer>> res) {
        if (k == 0 && target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (k <= 0 || target <= 0) {
            return;
        }
        // Prune: the smallest possible sum with remaining numbers
        int minPossible = 0;
        for (int i = start; i < start + k && i <= 9; i++) {
            minPossible += i;
        }
        if (minPossible > target) return;
        // Prune: the largest possible sum with remaining numbers
        int maxPossible = 0;
        for (int i = 9; i >= start && (9 - i + 1) <= k; i--) {
            maxPossible += i;
        }
        if (maxPossible < target) return;

        for (int i = start; i <= 9; i++) {
            path.add(i);
            backtrack(i + 1, k - 1, target - i, path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return
            for i in range(start, 10):
                # prune if sum would exceed target
                if total + i > n:
                    break
                # prune if not enough numbers left to fill the combination
                if len(path) + (9 - i + 1) < k:
                    continue
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res: List[List[int]] = []

        def backtrack(start: int, path: List[int], total: int):
            if len(path) == k:
                if total == n:
                    res.append(path.copy())
                return
            # prune if not enough numbers left or sum already too large
            remaining_needed = k - len(path)
            max_possible_sum = sum(range(9, 9 - remaining_needed, -1))
            min_possible_sum = sum(range(start, start + remaining_needed))
            if total + min_possible_sum > n or total + max_possible_sum < n:
                return

            for num in range(start, 10):
                if total + num > n:
                    break
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()

        backtrack(1, [], 0)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int **res;
    int *colSizes;
    int count;
    int capacity;
    int k;
    int n;
    int path[9];
} Context;

static void backtrack(Context *ctx, int start, int depth, int sum) {
    if (depth == ctx->k) {
        if (sum == ctx->n) {
            if (ctx->count == ctx->capacity) {
                ctx->capacity *= 2;
                ctx->res = realloc(ctx->res, ctx->capacity * sizeof(int*));
                ctx->colSizes = realloc(ctx->colSizes, ctx->capacity * sizeof(int));
            }
            int *comb = malloc(ctx->k * sizeof(int));
            memcpy(comb, ctx->path, ctx->k * sizeof(int));
            ctx->res[ctx->count] = comb;
            ctx->colSizes[ctx->count] = ctx->k;
            ctx->count++;
        }
        return;
    }

    for (int i = start; i <= 9; ++i) {
        if (sum + i > ctx->n) break;               // prune: sum would exceed target
        ctx->path[depth] = i;
        backtrack(ctx, i + 1, depth + 1, sum + i);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes) {
    Context ctx;
    ctx.k = k;
    ctx.n = n;
    ctx.count = 0;
    ctx.capacity = 200;                     // sufficient for all possible combinations
    ctx.res = malloc(ctx.capacity * sizeof(int*));
    ctx.colSizes = malloc(ctx.capacity * sizeof(int));

    backtrack(&ctx, 1, 0, 0);

    *returnSize = ctx.count;
    if (ctx.count == 0) {
        free(ctx.res);
        free(ctx.colSizes);
        *returnColumnSizes = NULL;
        return NULL;
    }

    // shrink to exact size
    ctx.res = realloc(ctx.res, ctx.count * sizeof(int*));
    ctx.colSizes = realloc(ctx.colSizes, ctx.count * sizeof(int));

    *returnColumnSizes = ctx.colSizes;
    return ctx.res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        var results = new List<IList<int>>();
        var path = new List<int>();

        void Dfs(int start, int remainingCount, int target) {
            if (remainingCount == 0) {
                if (target == 0) results.Add(new List<int>(path));
                return;
            }

            for (int i = start; i <= 9; i++) {
                if (i > target) break; // further numbers will only be larger
                path.Add(i);
                Dfs(i + 1, remainingCount - 1, target - i);
                path.RemoveAt(path.Count - 1);
            }
        }

        Dfs(1, k, n);
        return results;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    const result = [];
    const backtrack = (start, combo, sum) => {
        if (combo.length === k) {
            if (sum === n) result.push([...combo]);
            return;
        }
        for (let i = start; i <= 9; i++) {
            if (sum + i > n) break; // prune since further numbers are larger
            combo.push(i);
            backtrack(i + 1, combo, sum + i);
            combo.pop();
        }
    };
    backtrack(1, [], 0);
    return result;
};
```

## Typescript

```typescript
function combinationSum3(k: number, n: number): number[][] {
    const res: number[][] = [];
    const path: number[] = [];

    function dfs(start: number, kLeft: number, target: number) {
        if (kLeft === 0 && target === 0) {
            res.push(path.slice());
            return;
        }
        if (kLeft === 0 || target <= 0) return;

        for (let i = start; i <= 9; i++) {
            // prune: smallest possible sum with remaining numbers
            const minSum = kLeft * i + (kLeft * (kLeft - 1)) / 2;
            if (minSum > target) break;
            // prune: largest possible sum exceeds target? optional, not needed

            path.push(i);
            dfs(i + 1, kLeft - 1, target - i);
            path.pop();
        }
    }

    dfs(1, k, n);
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer[][]
     */
    function combinationSum3($k, $n) {
        $result = [];
        $path = [];

        $dfs = function($start, $remainingK, $remainingSum) use (&$dfs, &$result, &$path) {
            if ($remainingK == 0) {
                if ($remainingSum == 0) {
                    $result[] = $path;
                }
                return;
            }

            // Prune: not enough numbers left or sum too large/small
            for ($i = $start; $i <= 9; $i++) {
                if ($i > $remainingSum) break; // further numbers will only be larger

                $path[] = $i;
                $dfs($i + 1, $remainingK - 1, $remainingSum - $i);
                array_pop($path);
            }
        };

        $dfs(1, $k, $n);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        var result = [[Int]]()
        
        func backtrack(_ start: Int, _ path: [Int], _ sum: Int) {
            if path.count == k {
                if sum == n {
                    result.append(path)
                }
                return
            }
            if sum >= n { return }
            for i in start...9 {
                let newSum = sum + i
                if newSum > n { break }
                backtrack(i + 1, path + [i], newSum)
            }
        }
        
        backtrack(1, [], 0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()
        fun backtrack(start: Int, kLeft: Int, target: Int) {
            if (kLeft == 0 && target == 0) {
                result.add(ArrayList(path))
                return
            }
            if (kLeft == 0 || target <= 0) return
            for (i in start..9) {
                // Prune if i is larger than remaining target
                if (i > target) break
                path.add(i)
                backtrack(i + 1, kLeft - 1, target - i)
                path.removeAt(path.size - 1)
            }
        }
        backtrack(1, k, n)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> combinationSum3(int k, int n) {
    final List<List<int>> result = [];

    void backtrack(int start, List<int> path, int sum) {
      if (path.length == k) {
        if (sum == n) {
          result.add(List.from(path));
        }
        return;
      }

      for (int i = start; i <= 9; i++) {
        final int newSum = sum + i;
        if (newSum > n) break; // further numbers will only increase the sum
        path.add(i);
        backtrack(i + 1, path, newSum);
        path.removeLast();
      }
    }

    backtrack(1, [], 0);
    return result;
  }
}
```

## Golang

```go
func combinationSum3(k int, n int) [][]int {
	var res [][]int
	var path []int

	var dfs func(start, cnt, sum int)
	dfs = func(start, cnt, sum int) {
		if cnt == k && sum == n {
			tmp := make([]int, k)
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		if cnt >= k || sum >= n {
			return
		}
		for i := start; i <= 9; i++ {
			path = append(path, i)
			dfs(i+1, cnt+1, sum+i)
			path = path[:len(path)-1]
		}
	}

	dfs(1, 0, 0)
	return res
}
```

## Ruby

```ruby
def combination_sum3(k, n)
  result = []
  dfs = nil
  dfs = lambda do |start, path, cur_sum|
    if path.size == k
      result << path.clone if cur_sum == n
      return
    end
    (start..9).each do |num|
      break if cur_sum + num > n
      path << num
      dfs.call(num + 1, path, cur_sum + num)
      path.pop
    end
  end
  dfs.call(1, [], 0)
  result
end
```

## Scala

```scala
object Solution {
    def combinationSum3(k: Int, n: Int): List[List[Int]] = {
        import scala.collection.mutable.ListBuffer
        val result = ListBuffer[List[Int]]()

        def dfs(start: Int, kLeft: Int, sumLeft: Int, path: List[Int]): Unit = {
            if (kLeft == 0 && sumLeft == 0) {
                result += path
                return
            }
            if (kLeft <= 0 || sumLeft <= 0) return

            var i = start
            while (i <= 9) {
                if (i > sumLeft) return
                dfs(i + 1, kLeft - 1, sumLeft - i, path :+ i)
                i += 1
            }
        }

        dfs(1, k, n, List())
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        let mut path = Vec::new();

        fn dfs(start: i32, k_left: i32, target: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            if k_left == 0 && target == 0 {
                res.push(path.clone());
                return;
            }
            if k_left <= 0 || target <= 0 {
                return;
            }
            for i in start..=9 {
                if i > target {
                    break;
                }
                path.push(i);
                dfs(i + 1, k_left - 1, target - i, path, res);
                path.pop();
            }
        }

        dfs(1, k, n, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (combination-sum3 k n)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)))
  (letrec ((search
            (lambda (start remaining target path)
              (cond [(= remaining 0) (if (= target 0) (list (reverse path)) '())]
                    [(or (< target 0) (> start 9)) '()]
                    [else
                     (apply append
                            (for/list ([i (in-range start 10)]
                                       #:when (<= i target))
                              (search (+ i 1) (- remaining 1) (- target i) (cons i path))))]))))
    (search 1 k n '())))
```

## Erlang

```erlang
-module(solution).
-export([combination_sum3/2]).

-spec combination_sum3(K :: integer(), N :: integer()) -> [[integer()]].
combination_sum3(K, N) ->
    Result = dfs(1, K, N, [], []),
    lists:reverse(Result).

dfs(_Start, 0, 0, Curr, Acc) ->
    [lists:reverse(Curr) | Acc];
dfs(Start, KRem, SumRem, Curr, Acc) when KRem > 0, SumRem > 0, Start =< 9 ->
    WithInclude = dfs(Start + 1, KRem - 1, SumRem - Start, [Start | Curr], Acc),
    dfs(Start + 1, KRem, SumRem, Curr, WithInclude);
dfs(_Start, _KRem, _SumRem, _Curr, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec combination_sum3(k :: integer, n :: integer) :: [[integer]]
  def combination_sum3(k, n) do
    backtrack(1, k, n, [])
  end

  defp backtrack(_start, 0, 0, path), do: [Enum.reverse(path)]

  defp backtrack(start, k, n, _path) when start > 9 or k < 0 or n < 0,
    do: []

  defp backtrack(start, k, n, path) do
    Enum.flat_map(start..9, fn i ->
      backtrack(i + 1, k - 1, n - i, [i | path])
    end)
  end
end
```
