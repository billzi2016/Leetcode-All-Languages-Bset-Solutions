# 0039. Combination Sum

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> cur;
        function<void(int,int)> dfs = [&](int start, int remain) {
            if (remain == 0) {
                res.push_back(cur);
                return;
            }
            for (int i = start; i < (int)candidates.size(); ++i) {
                int val = candidates[i];
                if (val > remain) break;
                cur.push_back(val);
                dfs(i, remain - val); // can reuse same element
                cur.pop_back();
            }
        };
        dfs(0, target);
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, 0, target, new ArrayList<>(), res);
        return res;
    }
    
    private void backtrack(int[] cand, int start, int remain, List<Integer> path, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < cand.length && cand[i] <= remain; i++) {
            path.add(cand[i]);
            backtrack(cand, i, remain - cand[i], path, res);
            path.remove(path.size() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        comb = []

        def backtrack(start, remain):
            if remain == 0:
                res.append(list(comb))
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remain:
                    break
                comb.append(val)
                backtrack(i, remain - val)  # can reuse same element
                comb.pop()

        backtrack(0, target)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > remaining:
                    break
                comb.append(val)
                backtrack(i, remaining - val)  # can reuse same element
                comb.pop()

        backtrack(0, target)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void dfs(int *candidates, int candidatesSize, int startIdx, int target,
                int *path, int curLen, int **result, int *colSizes, int *returnSize) {
    if (target == 0) {
        int *comb = (int *)malloc(sizeof(int) * curLen);
        memcpy(comb, path, sizeof(int) * curLen);
        result[*returnSize] = comb;
        colSizes[*returnSize] = curLen;
        (*returnSize)++;
        return;
    }
    for (int i = startIdx; i < candidatesSize; ++i) {
        int val = candidates[i];
        if (val > target) continue;
        path[curLen] = val;
        dfs(candidates, candidatesSize, i, target - val, path, curLen + 1,
            result, colSizes, returnSize);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    const int MAX_COMB = 150;
    int **result = (int **)malloc(sizeof(int *) * MAX_COMB);
    int *colSizes = (int *)malloc(sizeof(int) * MAX_COMB);
    int path[40];   // target <= 40, min candidate >=2, so length won't exceed 20, 40 is safe
    *returnSize = 0;

    dfs(candidates, candidatesSize, 0, target, path, 0, result, colSizes, returnSize);

    if (*returnSize == 0) {
        free(result);
        free(colSizes);
        *returnColumnSizes = NULL;
        return NULL;
    }

    result = (int **)realloc(result, sizeof(int *) * (*returnSize));
    colSizes = (int *)realloc(colSizes, sizeof(int) * (*returnSize));
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        Array.Sort(candidates);
        var results = new List<IList<int>>();
        var current = new List<int>();
        Backtrack(0, target);
        return results;

        void Backtrack(int start, int remaining) {
            if (remaining == 0) {
                results.Add(new List<int>(current));
                return;
            }
            for (int i = start; i < candidates.Length && candidates[i] <= remaining; i++) {
                current.Add(candidates[i]);
                Backtrack(i, remaining - candidates[i]); // can reuse same element
                current.RemoveAt(current.Count - 1);
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const res = [];
    // sort to help pruning
    candidates.sort((a, b) => a - b);
    
    const backtrack = (start, remain, path) => {
        if (remain === 0) {
            res.push([...path]);
            return;
        }
        for (let i = start; i < candidates.length; i++) {
            const cur = candidates[i];
            if (cur > remain) break; // cannot exceed target
            path.push(cur);
            backtrack(i, remain - cur, path); // can reuse same element
            path.pop();
        }
    };
    
    backtrack(0, target, []);
    return res;
};
```

## Typescript

```typescript
function combinationSum(candidates: number[], target: number): number[][] {
    const res: number[][] = [];
    if (!candidates || candidates.length === 0) return res;
    candidates.sort((a, b) => a - b);
    
    const backtrack = (remain: number, combo: number[], start: number) => {
        if (remain === 0) {
            res.push([...combo]);
            return;
        }
        for (let i = start; i < candidates.length; i++) {
            const cur = candidates[i];
            if (cur > remain) break;
            combo.push(cur);
            backtrack(remain - cur, combo, i); // reuse same element
            combo.pop();
        }
    };
    
    backtrack(target, [], 0);
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum($candidates, $target) {
        sort($candidates);
        $result = [];
        $path = [];
        $this->dfs($candidates, $target, 0, $path, $result);
        return $result;
    }

    private function dfs($candidates, $remain, $start, &$path, &$result) {
        if ($remain == 0) {
            $result[] = $path;
            return;
        }
        $n = count($candidates);
        for ($i = $start; $i < $n; $i++) {
            $val = $candidates[$i];
            if ($val > $remain) break;
            $path[] = $val;
            $this->dfs($candidates, $remain - $val, $i, $path, $result);
            array_pop($path);
        }
    }
}
```

## Swift

```swift
class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        let sorted = candidates.sorted()
        var result = [[Int]]()
        var path = [Int]()
        
        func backtrack(_ start: Int, _ remaining: Int) {
            if remaining == 0 {
                result.append(path)
                return
            }
            for i in start..<sorted.count {
                let val = sorted[i]
                if val > remaining { break }
                path.append(val)
                backtrack(i, remaining - val)
                path.removeLast()
            }
        }
        
        backtrack(0, target)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {
        val sorted = candidates.sorted()
        val res = mutableListOf<List<Int>>()
        val path = mutableListOf<Int>()
        fun dfs(start: Int, remain: Int) {
            if (remain == 0) {
                res.add(ArrayList(path))
                return
            }
            for (i in start until sorted.size) {
                val cur = sorted[i]
                if (cur > remain) break
                path.add(cur)
                dfs(i, remain - cur)
                path.removeAt(path.size - 1)
            }
        }
        dfs(0, target)
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> combinationSum(List<int> candidates, int target) {
    candidates.sort();
    List<List<int>> result = [];
    List<int> path = [];

    void dfs(int start, int remaining) {
      if (remaining == 0) {
        result.add(List.from(path));
        return;
      }
      for (int i = start; i < candidates.length; i++) {
        int val = candidates[i];
        if (val > remaining) break;
        path.add(val);
        dfs(i, remaining - val);
        path.removeLast();
      }
    }

    dfs(0, target);
    return result;
  }
}
```

## Golang

```go
package main

import "sort"

func combinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	var res [][]int
	var cur []int
	var dfs func(start, remain int)
	dfs = func(start, remain int) {
		if remain == 0 {
			tmp := make([]int, len(cur))
			copy(tmp, cur)
			res = append(res, tmp)
			return
		}
		for i := start; i < len(candidates); i++ {
			val := candidates[i]
			if val > remain {
				break
			}
			cur = append(cur, val)
			dfs(i, remain-val)
			cur = cur[:len(cur)-1]
		}
	}
	dfs(0, target)
	return res
}
```

## Ruby

```ruby
def combination_sum(candidates, target)
  candidates.sort!
  results = []

  dfs = nil
  dfs = lambda do |start_idx, path, remain|
    if remain == 0
      results << path.clone
      return
    end

    (start_idx...candidates.length).each do |i|
      val = candidates[i]
      break if val > remain
      path << val
      dfs.call(i, path, remain - val)
      path.pop
    end
  end

  dfs.call(0, [], target)
  results
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, ListBuffer}

object Solution {
  def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {
    val sorted = candidates.sorted
    val res = ListBuffer[List[Int]]()
    val path = ArrayBuffer[Int]()

    def backtrack(start: Int, remain: Int): Unit = {
      if (remain == 0) {
        res += path.toList
        return
      }
      var i = start
      while (i < sorted.length && sorted(i) <= remain) {
        path.append(sorted(i))
        backtrack(i, remain - sorted(i))
        path.remove(path.size - 1)
        i += 1
      }
    }

    backtrack(0, target)
    res.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut cand = candidates;
        cand.sort_unstable();
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut path: Vec<i32> = Vec::new();

        fn dfs(
            start: usize,
            remain: i32,
            cand: &Vec<i32>,
            path: &mut Vec<i32>,
            res: &mut Vec<Vec<i32>>,
        ) {
            if remain == 0 {
                res.push(path.clone());
                return;
            }
            for i in start..cand.len() {
                let v = cand[i];
                if v > remain {
                    break;
                }
                path.push(v);
                dfs(i, remain - v, cand, path, res);
                path.pop();
            }
        }

        dfs(0, target, &cand, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (combination-sum candidates target)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  (let* ([sorted (sort candidates <)])
    (letrec
        ((dfs
           (lambda (start rem path)
             (cond [(zero? rem) (list (reverse path))]
                   [else
                    (let loop ((i start) (acc '()))
                      (if (>= i (length sorted))
                          acc
                          (let* ([c (list-ref sorted i)])
                            (if (> c rem)
                                acc
                                (let ((next (dfs i (- rem c) (cons c path))))
                                  (loop (+ i 1) (append acc next)))))))])))
      (dfs 0 target '()))))
```

## Erlang

```erlang
-spec combination_sum([integer()], integer()) -> [[integer()]].
combination_sum(Candidates, Target) ->
    Sorted = lists:sort(Candidates),
    Result = dfs(Sorted, Target, 0, [], []),
    lists:reverse(Result).

dfs(_Cand, 0, _Idx, Curr, Acc) ->
    [lists:reverse(Curr) | Acc];
dfs(Cand, Target, Idx, _Curr, Acc) when Target < 0; Idx >= length(Cand) ->
    Acc;
dfs(Cand, Target, Idx, Curr, Acc) ->
    Candidate = lists:nth(Idx + 1, Cand),
    Acc1 = dfs(Cand, Target - Candidate, Idx, [Candidate | Curr], Acc),
    dfs(Cand, Target, Idx + 1, Curr, Acc1).
```

## Elixir

```elixir
defmodule Solution do
  @spec combination_sum(candidates :: [integer], target :: integer) :: [[integer]]
  def combination_sum(candidates, target) do
    sorted = Enum.sort(candidates)
    dfs(sorted, target, 0, [], [])
    |> Enum.reverse()
  end

  defp dfs(_cands, 0, _idx, path, acc) do
    [Enum.reverse(path) | acc]
  end

  defp dfs(_cands, target, _idx, _path, acc) when target < 0 do
    acc
  end

  defp dfs(cands, target, idx, path, acc) do
    if idx >= length(cands) do
      acc
    else
      c = Enum.at(cands, idx)

      acc1 =
        if c <= target do
          dfs(cands, target - c, idx, [c | path], acc)
        else
          acc
        end

      dfs(cands, target, idx + 1, path, acc1)
    end
  end
end
```
