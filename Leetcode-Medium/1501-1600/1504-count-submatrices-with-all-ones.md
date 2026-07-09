# 1504. Count Submatrices With All Ones

## Cpp

```cpp
class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int m = mat.size();
        if (m == 0) return 0;
        int n = mat[0].size();
        vector<int> height(n, 0);
        long long ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1) height[j] += 1;
                else height[j] = 0;
            }
            for (int left = 0; left < n; ++left) {
                int minH = INT_MAX;
                for (int right = left; right < n; ++right) {
                    minH = std::min(minH, height[right]);
                    ans += minH;
                }
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numSubmat(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] height = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    height[i][j] = (i == 0 ? 1 : height[i - 1][j] + 1);
                }
            }
        }

        long total = 0;
        int[] sum = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();

        for (int i = 0; i < m; i++) {
            stack.clear();
            for (int j = 0; j < n; j++) {
                while (!stack.isEmpty() && height[i][stack.peek()] >= height[i][j]) {
                    stack.pop();
                }
                if (stack.isEmpty()) {
                    sum[j] = height[i][j] * (j + 1);
                } else {
                    int prev = stack.peek();
                    sum[j] = sum[prev] + height[i][j] * (j - prev);
                }
                total += sum[j];
                stack.push(j);
            }
        }

        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat:
            return 0
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            # update histogram heights
            for j in range(n):
                if mat[i][j]:
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []          # each element is (height, count)
            cur = 0             # number of submatrices ending at current column in this row
            for h in heights:
                cnt = 1
                while stack and stack[-1][0] >= h:
                    prev_h, prev_cnt = stack.pop()
                    cur -= (prev_h - h) * prev_cnt
                    cnt += prev_cnt
                cur += h
                stack.append((h, cnt))
                ans += cur
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            stack = []
            cur = 0
            for h in heights:
                cnt = 1
                while stack and stack[-1][0] >= h:
                    prev_h, prev_cnt = stack.pop()
                    cur -= prev_h * prev_cnt
                    cnt += prev_cnt
                stack.append((h, cnt))
                cur += h * cnt
                ans += cur
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int numSubmat(int** mat, int matSize, int* matColSize) {
    int m = matSize;
    if (m == 0) return 0;
    int n = matColSize[0];

    int **left = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        left[i] = (int *)calloc(n, sizeof(int));
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 1) {
                left[i][j] = (j > 0 ? left[i][j - 1] : 0) + 1;
            }
        }
    }

    long long ans = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 1) {
                int minWidth = INT_MAX;
                for (int k = i; k >= 0 && left[k][j] > 0; --k) {
                    if (left[k][j] < minWidth) minWidth = left[k][j];
                    ans += minWidth;
                }
            }
        }
    }

    for (int i = 0; i < m; ++i) free(left[i]);
    free(left);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSubmat(int[][] mat) {
        int m = mat.Length;
        int n = mat[0].Length;
        int[] heights = new int[n];
        long ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1) heights[j] += 1;
                else heights[j] = 0;
            }
            var stackHeight = new Stack<int>();
            var stackCount = new Stack<int>();
            long sum = 0;
            for (int j = 0; j < n; j++) {
                int cnt = 1;
                while (stackHeight.Count > 0 && stackHeight.Peek() >= heights[j]) {
                    int h = stackHeight.Pop();
                    int c = stackCount.Pop();
                    sum -= (long)(h - heights[j]) * c;
                    cnt += c;
                }
                stackHeight.Push(heights[j]);
                stackCount.Push(cnt);
                sum += heights[j];
                ans += sum;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSubmat = function(mat) {
    const m = mat.length, n = mat[0].length;
    const heights = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            heights[j] = mat[i][j] === 1 ? heights[j] + 1 : 0;
        }
        const stack = [];
        let sum = 0;
        for (let j = 0; j < n; ++j) {
            let cnt = 1;
            while (stack.length && stack[stack.length - 1].h >= heights[j]) {
                const top = stack.pop();
                cnt += top.c;
                sum -= top.h * top.c;
            }
            stack.push({ h: heights[j], c: cnt });
            sum += heights[j] * cnt;
            ans += sum;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numSubmat(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const heights = new Array(n).fill(0);
    let total = 0;

    for (let i = 0; i < m; i++) {
        // update histogram heights
        for (let j = 0; j < n; j++) {
            heights[j] = mat[i][j] === 1 ? heights[j] + 1 : 0;
        }

        const stack: number[] = [];          // indices with increasing heights
        const cntArr = new Array(n).fill(0); // count of subarrays where current height is minimum
        let sum = 0;                         // sum of contributions for current row

        for (let j = 0; j < n; j++) {
            let cnt = 1;
            while (stack.length && heights[stack[stack.length - 1]] >= heights[j]) {
                const idx = stack.pop()!;
                cnt += cntArr[idx];
                sum -= heights[idx] * cntArr[idx];
            }
            stack.push(j);
            cntArr[j] = cnt;
            sum += heights[j] * cnt;
            total += sum;
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSubmat($mat) {
        $m = count($mat);
        if ($m == 0) return 0;
        $n = count($mat[0]);
        $heights = array_fill(0, $n, 0);
        $ans = 0;

        for ($i = 0; $i < $m; $i++) {
            // update heights
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] == 1) {
                    $heights[$j] += 1;
                } else {
                    $heights[$j] = 0;
                }
            }

            // monotonic stack to count submatrices ending at row i
            $stack = [];          // each element: [height, count]
            $sum = 0;             // sum of contributions for current column

            for ($j = 0; $j < $n; $j++) {
                $cnt = 1;
                while (!empty($stack) && $stack[count($stack) - 1][0] >= $heights[$j]) {
                    $top = array_pop($stack);
                    $sum -= $top[0] * $top[1];
                    $cnt += $top[1];
                }
                $sum += $heights[$j] * $cnt;
                $ans += $sum;
                $stack[] = [$heights[$j], $cnt];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numSubmat(_ mat: [[Int]]) -> Int {
        let m = mat.count
        guard m > 0 else { return 0 }
        let n = mat[0].count
        var heights = Array(repeating: 0, count: n)
        var ans = 0
        
        for i in 0..<m {
            // update histogram heights
            for j in 0..<n {
                if mat[i][j] == 1 {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            
            var stack: [Int] = []
            var sum = 0
            for j in 0..<n {
                while let last = stack.last, heights[last] >= heights[j] {
                    let idx = stack.removeLast()
                    let left = stack.last ?? -1
                    // remove excess contributions caused by higher previous height
                    sum -= (heights[idx] - heights[j]) * (idx - left)
                }
                sum += heights[j]
                ans += sum
                stack.append(j)
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSubmat(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val height = IntArray(n)
        var total = 0L
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 1) {
                    height[j] += 1
                } else {
                    height[j] = 0
                }
            }
            val stack = java.util.ArrayDeque<Pair<Int, Int>>()
            var sum = 0L
            for (j in 0 until n) {
                var cnt = 1
                while (!stack.isEmpty() && stack.peekLast().first >= height[j]) {
                    val top = stack.removeLast()
                    sum -= top.first.toLong() * top.second
                    cnt += top.second
                }
                stack.addLast(Pair(height[j], cnt))
                sum += height[j].toLong() * cnt
                total += sum
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSubmat(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    List<int> heights = List.filled(n, 0);
    int ans = 0;

    for (int i = 0; i < m; i++) {
      // update heights
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 1) {
          heights[j] += 1;
        } else {
          heights[j] = 0;
        }
      }

      // monotonic stack to count submatrices ending at row i
      List<int> stackH = [];
      List<int> stackC = [];
      int sum = 0;

      for (int j = 0; j < n; j++) {
        int cnt = 1;
        while (stackH.isNotEmpty && stackH.last >= heights[j]) {
          int h = stackH.removeLast();
          int c = stackC.removeLast();
          sum -= h * c;
          cnt += c;
        }
        stackH.add(heights[j]);
        stackC.add(cnt);
        sum += heights[j] * cnt;
        ans += sum;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func numSubmat(mat [][]int) int {
	m := len(mat)
	if m == 0 {
		return 0
	}
	n := len(mat[0])
	heights := make([]int, n)
	res := 0

	type pair struct{ h, c int }

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}

		stack := []pair{}
		sumRow := 0
		for j := 0; j < n; j++ {
			if heights[j] == 0 {
				stack = nil
				sumRow = 0
				continue
			}
			cnt := 1
			for len(stack) > 0 && stack[len(stack)-1].h >= heights[j] {
				top := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				cnt += top.c
				sumRow -= top.h * top.c
			}
			stack = append(stack, pair{heights[j], cnt})
			sumRow += heights[j] * cnt
			res += sumRow
		}
	}
	return res
}
```

## Ruby

```ruby
def num_submat(mat)
  m = mat.size
  n = mat[0].size
  heights = Array.new(n, 0)
  ans = 0

  (0...m).each do |i|
    (0...n).each do |j|
      if mat[i][j] == 1
        heights[j] += 1
      else
        heights[j] = 0
      end
    end

    stack = []
    sum = 0
    (0...n).each do |j|
      cnt = 1
      while !stack.empty? && stack[-1][0] >= heights[j]
        h, c = stack.pop
        sum -= h * c
        cnt += c
      end
      stack << [heights[j], cnt]
      sum += heights[j] * cnt
      ans += sum
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numSubmat(mat: Array[Array[Int]]): Int = {
        val m = mat.length
        if (m == 0) return 0
        val n = mat(0).length
        val height = new Array[Int](n)
        var total: Long = 0L

        for (i <- 0 until m) {
            // update heights
            for (j <- 0 until n) {
                if (mat(i)(j) == 1) height(j) += 1 else height(j) = 0
            }

            val dp = new Array[Int](n)
            val stack = new java.util.ArrayDeque[Int]()

            for (j <- 0 until n) {
                while (!stack.isEmpty && height(stack.peek()) >= height(j)) {
                    stack.pop()
                }
                if (height(j) == 0) {
                    dp(j) = 0
                } else if (stack.isEmpty) {
                    dp(j) = height(j) * (j + 1)
                } else {
                    val prev = stack.peek()
                    dp(j) = dp(prev) + height(j) * (j - prev)
                }
                total += dp(j).toLong
                stack.push(j)
            }
        }

        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_submat(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        if m == 0 {
            return 0;
        }
        let n = mat[0].len();
        let mut heights = vec![0i32; n];
        let mut ans: i64 = 0;

        for i in 0..m {
            // update histogram heights
            for j in 0..n {
                if mat[i][j] == 1 {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }

            let mut stack: Vec<usize> = Vec::new();
            let mut sum = vec![0i64; n];

            for j in 0..n {
                while let Some(&last) = stack.last() {
                    if heights[last] >= heights[j] {
                        stack.pop();
                    } else {
                        break;
                    }
                }

                if stack.is_empty() {
                    sum[j] = (j as i64 + 1) * heights[j] as i64;
                } else {
                    let prev = *stack.last().unwrap();
                    sum[j] = sum[prev] + ((j - prev) as i64) * heights[j] as i64;
                }

                stack.push(j);
                ans += sum[j];
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (num-submat mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length mat))
         (n (if (= m 0) 0 (length (car mat))))
         (rows (list->vector (map list->vector mat)))
         (heights (make-vector n 0))
         (total 0))
    (for ([i (in-range m)])
      ;; update heights for current row
      (let ((row (vector-ref rows i)))
        (for ([j (in-range n)])
          (if (= (vector-ref row j) 1)
              (vector-set! heights j (+ 1 (vector-ref heights j)))
              (vector-set! heights j 0))))
      ;; count submatrices ending at this row using a monotonic stack
      (let* ((dp (make-vector n 0))
             (stack '()))
        (for ([j (in-range n)])
          (let ((h (vector-ref heights j)))
            (let loop ()
              (when (and (not (null? stack))
                         (>= (vector-ref heights (car stack)) h))
                (set! stack (cdr stack))
                (loop)))
            (if (null? stack)
                (vector-set! dp j (* h (+ j 1)))
                (let* ((prev (car stack))
                       (prev-sum (vector-ref dp prev))
                       (width (- j prev))
                       (sum (+ prev-sum (* h width))))
                  (vector-set! dp j sum)))
            (set! total (+ total (vector-ref dp j)))
            (set! stack (cons j stack))))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([num_submat/1]).

-spec num_submat(Mat :: [[integer()]]) -> integer().
num_submat([]) ->
    0;
num_submat([FirstRow|RestRows]) ->
    N = length(FirstRow),
    Heights0 = lists:duplicate(N, 0),
    process_rows([FirstRow|RestRows], Heights0, 0).

process_rows([], _Heights, Acc) ->
    Acc;
process_rows([Row|Rows], Heights, Acc) ->
    NewHeights = update_heights(Row, Heights),
    RowSum = row_sum(NewHeights),
    process_rows(Rows, NewHeights, Acc + RowSum).

update_heights(Row, Heights) ->
    lists:map(
        fun({R, H}) ->
            case R of
                1 -> H + 1;
                _ -> 0
            end
        end,
        lists:zip(Row, Heights)
    ).

row_sum(Heights) ->
    {_, _, Sum} = lists:foldl(
        fun(H, {Cur, Stack, Total}) ->
            {NewStack, NewCur, Cnt} = pop_higher(H, Stack, Cur, 1),
            NewCur2 = NewCur + H * Cnt,
            {NewCur2, [{H, Cnt}|NewStack], Total + NewCur2}
        end,
        {0, [], 0},
        Heights
    ),
    Sum.

pop_higher(_H, [], Cur, Cnt) ->
    {[], Cur, Cnt};
pop_higher(H, [{Ph, Pc} | Rest], Cur, Cnt) when Ph >= H ->
    NewCur = Cur - Ph * Pc,
    pop_higher(H, Rest, NewCur, Cnt + Pc);
pop_higher(_H, Stack, Cur, Cnt) ->
    {Stack, Cur, Cnt}.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_submat(mat :: [[integer]]) :: integer
  def num_submat(mat) do
    m = length(mat)
    n = if m == 0, do: 0, else: length(hd(mat))
    heights = List.duplicate(0, n)

    {ans, _} =
      Enum.reduce(0..(m - 1), {0, heights}, fn i, {total, hts} ->
        row = Enum.at(mat, i)
        new_heights = update_heights(row, hts, [])
        row_total = count_row(new_heights, n, 0, [], 0, 0)
        {total + row_total, new_heights}
      end)

    ans
  end

  # Update heights column‑wise based on current row values.
  defp update_heights([], [], acc), do: Enum.reverse(acc)

  defp update_heights([val | rest_vals], [h | rest_hs], acc) do
    new_h = if val == 1, do: h + 1, else: 0
    update_heights(rest_vals, rest_hs, [new_h | acc])
  end

  # Process a single row's histogram to count submatrices ending at this row.
  defp count_row(_heights, n, idx, _stack, _sum, ans) when idx == n, do: ans

  defp count_row(heights, n, idx, stack, sum, ans) do
    cur = Enum.at(heights, idx)
    {new_stack, cnt, new_sum} = pop_greater(stack, cur, 1, sum)
    sum2 = new_sum + cur * cnt
    ans2 = ans + sum2
    count_row(heights, n, idx + 1, [%{h: cur, cnt: cnt} | new_stack], sum2, ans2)
  end

  # Pop elements from the monotonic stack that are >= current height.
  defp pop_greater([], _cur_h, cnt, sum), do: {[], cnt, sum}

  defp pop_greater([%{h: h, cnt: c} = top | rest], cur_h, cnt, sum) when h >= cur_h do
    pop_greater(rest, cur_h, cnt + c, sum - h * c)
  end

  defp pop_greater(stack, _cur_h, cnt, sum), do: {stack, cnt, sum}
end
```
