# 1947. Maximum Compatibility Score Sum

## Cpp

```cpp
class Solution {
public:
    int maxCompatibilitySum(vector<vector<int>>& students, vector<vector<int>>& mentors) {
        int m = students.size();
        int n = students[0].size();
        vector<vector<int>> score(m, vector<int>(m, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                int cnt = 0;
                for (int k = 0; k < n; ++k) {
                    if (students[i][k] == mentors[j][k]) ++cnt;
                }
                score[i][j] = cnt;
            }
        }
        vector<int> dp(1 << m, -1);
        function<int(int)> dfs = [&](int mask) -> int {
            int i = __builtin_popcount((unsigned)mask);
            if (i == m) return 0;
            int &res = dp[mask];
            if (res != -1) return res;
            res = 0;
            for (int j = 0; j < m; ++j) {
                if (!(mask & (1 << j))) {
                    res = max(res, score[i][j] + dfs(mask | (1 << j)));
                }
            }
            return res;
        };
        return dfs(0);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxCompatibilitySum(int[][] students, int[][] mentors) {
        int m = students.length;
        int n = students[0].length;
        int[][] score = new int[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                int cnt = 0;
                for (int k = 0; k < n; k++) {
                    if (students[i][k] == mentors[j][k]) cnt++;
                }
                score[i][j] = cnt;
            }
        }

        int size = 1 << m;
        int[] dp = new int[size];
        Arrays.fill(dp, -1);
        dp[0] = 0;

        for (int mask = 0; mask < size; mask++) {
            int i = Integer.bitCount(mask); // number of students already assigned
            if (i >= m) continue;
            for (int j = 0; j < m; j++) {
                if ((mask & (1 << j)) == 0) {
                    int newMask = mask | (1 << j);
                    dp[newMask] = Math.max(dp[newMask], dp[mask] + score[i][j]);
                }
            }
        }

        return dp[size - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        m = len(students)
        # precompute compatibility scores
        scores = [[sum(1 for a, b in zip(students[i], mentors[j]) if a == b) 
                   for j in range(m)] for i in range(m)]
        
        dp = [-1] * (1 << m)
        dp[0] = 0
        
        for mask in range(1 << m):
            k = bin(mask).count('1')  # number of students already assigned
            if k >= m:
                continue
            cur = dp[mask]
            for j in range(m):
                if not (mask >> j) & 1:
                    nmask = mask | (1 << j)
                    val = cur + scores[k][j]
                    if val > dp[nmask]:
                        dp[nmask] = val
        
        return dp[(1 << m) - 1]
```

## Python3

```python
from typing import List

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        # Precompute compatibility scores
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            s = students[i]
            for j in range(m):
                cnt = 0
                t = mentors[j]
                for k in range(len(s)):
                    if s[k] == t[k]:
                        cnt += 1
                score[i][j] = cnt

        dp = [-1] * (1 << m)
        dp[0] = 0
        for mask in range(1 << m):
            i = mask.bit_count()  # number of students already assigned
            if i >= m or dp[mask] < 0:
                continue
            cur = dp[mask]
            for j in range(m):
                if not (mask >> j) & 1:
                    new_mask = mask | (1 << j)
                    val = cur + score[i][j]
                    if val > dp[new_mask]:
                        dp[new_mask] = val
        return dp[(1 << m) - 1]
```

## C

```c
#include <limits.h>

int maxCompatibilitySum(int** students, int studentsSize, int* studentsColSize,
                        int** mentors, int mentorsSize, int* mentorsColSize) {
    int n = studentsColSize[0];
    int m = studentsSize;  // same as mentorsSize

    int scores[8][8];
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            int cnt = 0;
            for (int k = 0; k < n; ++k) {
                if (students[i][k] == mentors[j][k]) ++cnt;
            }
            scores[i][j] = cnt;
        }
    }

    int totalMask = 1 << m;
    int dp[256];
    for (int mask = 0; mask < totalMask; ++mask) dp[mask] = INT_MIN / 2;
    dp[0] = 0;

    for (int mask = 0; mask < totalMask; ++mask) {
        if (dp[mask] <= INT_MIN / 4) continue;
        int i = __builtin_popcount(mask);  // next student index
        if (i >= m) continue;
        for (int j = 0; j < m; ++j) {
            if (!(mask & (1 << j))) {
                int newMask = mask | (1 << j);
                int val = dp[mask] + scores[i][j];
                if (val > dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[totalMask - 1];
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxCompatibilitySum(int[][] students, int[][] mentors)
    {
        int m = students.Length;
        int n = students[0].Length;

        // Precompute compatibility scores between each student and mentor
        int[,] score = new int[m, m];
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < m; j++)
            {
                int cnt = 0;
                for (int k = 0; k < n; k++)
                {
                    if (students[i][k] == mentors[j][k])
                        cnt++;
                }
                score[i, j] = cnt;
            }
        }

        int totalMask = 1 << m;
        int[] dp = new int[totalMask];
        for (int mask = 0; mask < totalMask; mask++)
        {
            int studentIdx = BitCount(mask); // number of already assigned students
            if (studentIdx >= m) continue;

            for (int mentor = 0; mentor < m; mentor++)
            {
                if ((mask & (1 << mentor)) == 0)
                {
                    int newMask = mask | (1 << mentor);
                    dp[newMask] = Math.Max(dp[newMask], dp[mask] + score[studentIdx, mentor]);
                }
            }
        }

        return dp[totalMask - 1];
    }

    private int BitCount(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} students
 * @param {number[][]} mentors
 * @return {number}
 */
var maxCompatibilitySum = function(students, mentors) {
    const m = students.length;
    const n = students[0].length;
    const scores = Array.from({ length: m }, () => Array(m).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            let cnt = 0;
            for (let k = 0; k < n; k++) {
                if (students[i][k] === mentors[j][k]) cnt++;
            }
            scores[i][j] = cnt;
        }
    }

    const size = 1 << m;
    const dp = new Array(size).fill(-Infinity);
    dp[0] = 0;

    const bitCount = (x) => {
        let c = 0;
        while (x) {
            x &= x - 1;
            c++;
        }
        return c;
    };

    for (let mask = 0; mask < size; mask++) {
        const i = bitCount(mask); // number of students already assigned
        if (i >= m) continue;
        for (let j = 0; j < m; j++) {
            if ((mask & (1 << j)) === 0) {
                const newMask = mask | (1 << j);
                dp[newMask] = Math.max(dp[newMask], dp[mask] + scores[i][j]);
            }
        }
    }

    return dp[size - 1];
};
```

## Typescript

```typescript
function maxCompatibilitySum(students: number[][], mentors: number[][]): number {
    const m = students.length;
    const n = students[0].length;
    const score: number[][] = Array.from({ length: m }, () => new Array(m).fill(0));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            let cnt = 0;
            for (let k = 0; k < n; k++) {
                if (students[i][k] === mentors[j][k]) cnt++;
            }
            score[i][j] = cnt;
        }
    }

    const totalMask = 1 << m;
    const dp = new Array(totalMask).fill(-Infinity);
    dp[0] = 0;

    const bits = new Array(totalMask).fill(0);
    for (let mask = 1; mask < totalMask; mask++) {
        bits[mask] = bits[mask >> 1] + (mask & 1);
    }

    for (let mask = 0; mask < totalMask; mask++) {
        const i = bits[mask];
        if (i >= m) continue;
        for (let j = 0; j < m; j++) {
            if ((mask & (1 << j)) === 0) {
                const newMask = mask | (1 << j);
                dp[newMask] = Math.max(dp[newMask], dp[mask] + score[i][j]);
            }
        }
    }

    return dp[totalMask - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $students
     * @param Integer[][] $mentors
     * @return Integer
     */
    function maxCompatibilitySum($students, $mentors) {
        $m = count($students);
        $n = count($students[0]);

        // Precompute compatibility scores
        $score = array_fill(0, $m, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $cnt = 0;
                for ($k = 0; $k < $n; $k++) {
                    if ($students[$i][$k] == $mentors[$j][$k]) {
                        $cnt++;
                    }
                }
                $score[$i][$j] = $cnt;
            }
        }

        $size = 1 << $m;
        $dp = array_fill(0, $size, -1);
        $dp[0] = 0;

        for ($mask = 0; $mask < $size; $mask++) {
            // number of assigned students equals bits set in mask
            $i = 0;
            $temp = $mask;
            while ($temp) {
                $i += $temp & 1;
                $temp >>= 1;
            }
            if ($i >= $m) continue;

            for ($j = 0; $j < $m; $j++) {
                if ((($mask >> $j) & 1) == 0) {
                    $newMask = $mask | (1 << $j);
                    $val = $dp[$mask] + $score[$i][$j];
                    if ($val > $dp[$newMask]) {
                        $dp[$newMask] = $val;
                    }
                }
            }
        }

        return $dp[$size - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxCompatibilitySum(_ students: [[Int]], _ mentors: [[Int]]) -> Int {
        let m = students.count
        var score = Array(repeating: Array(repeating: 0, count: m), count: m)
        for i in 0..<m {
            for j in 0..<m {
                var cnt = 0
                for k in 0..<students[i].count {
                    if students[i][k] == mentors[j][k] {
                        cnt += 1
                    }
                }
                score[i][j] = cnt
            }
        }
        
        let totalMask = 1 << m
        var dp = Array(repeating: -1, count: totalMask)
        
        func dfs(_ mask: Int) -> Int {
            if mask == totalMask - 1 { return 0 }
            if dp[mask] != -1 { return dp[mask] }
            let i = mask.nonzeroBitCount
            var best = 0
            for j in 0..<m where (mask & (1 << j)) == 0 {
                let val = score[i][j] + dfs(mask | (1 << j))
                if val > best { best = val }
            }
            dp[mask] = best
            return best
        }
        
        return dfs(0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCompatibilitySum(students: Array<IntArray>, mentors: Array<IntArray>): Int {
        val m = students.size
        val n = students[0].size
        val score = Array(m) { IntArray(m) }
        for (i in 0 until m) {
            for (j in 0 until m) {
                var cnt = 0
                for (k in 0 until n) {
                    if (students[i][k] == mentors[j][k]) cnt++
                }
                score[i][j] = cnt
            }
        }
        val totalMask = 1 shl m
        val dp = IntArray(totalMask) { -1 }
        dp[0] = 0
        for (mask in 0 until totalMask) {
            if (dp[mask] == -1) continue
            val i = Integer.bitCount(mask)
            if (i >= m) continue
            for (j in 0 until m) {
                if ((mask and (1 shl j)) == 0) {
                    val newMask = mask or (1 shl j)
                    dp[newMask] = maxOf(dp[newMask], dp[mask] + score[i][j])
                }
            }
        }
        return dp[totalMask - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxCompatibilitySum(List<List<int>> students, List<List<int>> mentors) {
    int m = students.length;
    int n = students[0].length;

    // Precompute compatibility scores between each student and mentor
    List<List<int>> score = List.generate(m, (_) => List.filled(m, 0));
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < m; ++j) {
        int cnt = 0;
        for (int k = 0; k < n; ++k) {
          if (students[i][k] == mentors[j][k]) cnt++;
        }
        score[i][j] = cnt;
      }
    }

    int size = 1 << m;
    List<int> dp = List.filled(size, -1);
    dp[0] = 0;

    for (int mask = 0; mask < size; ++mask) {
      if (dp[mask] < 0) continue;
      int i = _popCount(mask); // number of students already assigned
      if (i >= m) continue;
      for (int j = 0; j < m; ++j) {
        if ((mask & (1 << j)) == 0) {
          int newMask = mask | (1 << j);
          int val = dp[mask] + score[i][j];
          if (val > dp[newMask]) dp[newMask] = val;
        }
      }
    }

    return dp[size - 1];
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x != 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
func maxCompatibilitySum(students [][]int, mentors [][]int) int {
	m := len(students)
	// precompute compatibility scores
	score := make([][]int, m)
	for i := 0; i < m; i++ {
		score[i] = make([]int, m)
		for j := 0; j < m; j++ {
			cnt := 0
			for k := 0; k < len(students[0]); k++ {
				if students[i][k] == mentors[j][k] {
					cnt++
				}
			}
			score[i][j] = cnt
		}
	}

	size := 1 << m
	dp := make([]int, size)
	for i := range dp {
		dp[i] = -1
	}
	var dfs func(int, int) int
	dfs = func(i, mask int) int {
		if i == m {
			return 0
		}
		if dp[mask] != -1 {
			return dp[mask]
		}
		best := 0
		for j := 0; j < m; j++ {
			if (mask>>j)&1 == 0 {
				val := score[i][j] + dfs(i+1, mask|1<<j)
				if val > best {
					best = val
				}
			}
		}
		dp[mask] = best
		return best
	}

	return dfs(0, 0)
}
```

## Ruby

```ruby
def max_compatibility_sum(students, mentors)
  m = students.length
  n = students[0].length

  # Precompute compatibility scores between each student and mentor
  scores = Array.new(m) { Array.new(m, 0) }
  (0...m).each do |i|
    (0...m).each do |j|
      cnt = 0
      (0...n).each do |k|
        cnt += 1 if students[i][k] == mentors[j][k]
      end
      scores[i][j] = cnt
    end
  end

  total_masks = 1 << m
  dp = Array.new(total_masks, -1)
  dp[0] = 0

  (0...total_masks).each do |mask|
    next if dp[mask] < 0
    i = mask.to_s(2).count('1') # number of already assigned students
    next if i >= m
    (0...m).each do |j|
      next if (mask & (1 << j)) != 0
      new_mask = mask | (1 << j)
      val = dp[mask] + scores[i][j]
      dp[new_mask] = val if val > dp[new_mask]
    end
  end

  dp[total_masks - 1]
end
```

## Scala

```scala
object Solution {
    def maxCompatibilitySum(students: Array[Array[Int]], mentors: Array[Array[Int]]): Int = {
        val m = students.length
        val n = students(0).length
        val score = Array.ofDim[Int](m, m)
        var i = 0
        while (i < m) {
            var j = 0
            while (j < m) {
                var cnt = 0
                var k = 0
                while (k < n) {
                    if (students(i)(k) == mentors(j)(k)) cnt += 1
                    k += 1
                }
                score(i)(j) = cnt
                j += 1
            }
            i += 1
        }

        val totalMask = (1 << m) - 1
        val dp = Array.fill(1 << m)(Int.MinValue)
        dp(0) = 0

        var mask = 0
        while (mask <= totalMask) {
            val assigned = Integer.bitCount(mask)
            if (assigned < m && dp(mask) != Int.MinValue) {
                var mentorIdx = 0
                while (mentorIdx < m) {
                    if ((mask & (1 << mentorIdx)) == 0) {
                        val newMask = mask | (1 << mentorIdx)
                        val newScore = dp(mask) + score(assigned)(mentorIdx)
                        if (newScore > dp(newMask)) dp(newMask) = newScore
                    }
                    mentorIdx += 1
                }
            }
            mask += 1
        }

        dp(totalMask)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_compatibility_sum(students: Vec<Vec<i32>>, mentors: Vec<Vec<i32>>) -> i32 {
        let m = students.len();
        let n = students[0].len();

        // Precompute compatibility scores between each student and mentor
        let mut score = vec![vec![0i32; m]; m];
        for i in 0..m {
            for j in 0..m {
                let mut cnt = 0;
                for k in 0..n {
                    if students[i][k] == mentors[j][k] {
                        cnt += 1;
                    }
                }
                score[i][j] = cnt as i32;
            }
        }

        // DP over subsets of mentors
        let size = 1usize << m;
        let mut dp = vec![-1i32; size];
        dp[0] = 0;

        for mask in 0..size {
            if dp[mask] < 0 { continue; }
            let student_idx = mask.count_ones() as usize; // next student to assign
            if student_idx >= m { continue; }

            for mentor in 0..m {
                if (mask & (1 << mentor)) == 0 {
                    let new_mask = mask | (1 << mentor);
                    let val = dp[mask] + score[student_idx][mentor];
                    if val > dp[new_mask] {
                        dp[new_mask] = val;
                    }
                }
            }
        }

        dp[size - 1]
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-compatibility-sum students mentors)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let* ((m (length students))
         (scores (make-vector m)))
    ;; compute compatibility scores matrix
    (for ([i (in-range m)])
      (let ((row (make-vector m)))
        (for ([j (in-range m)])
          (define cnt
            (for/sum ([a (list-ref students i)]
                      [b (list-ref mentors j)]) (if (= a b) 1 0)))
          (vector-set! row j cnt))
        (vector-set! scores i row)))
    (define full-mask (sub1 (arithmetic-shift 1 m)))
    (define memo (make-vector (add1 full-mask) #f))
    (define (dfs mask)
      (if (= mask full-mask)
          0
          (let ((cached (vector-ref memo mask)))
            (if (not (eq? cached #f))
                cached
                (let* ((i (bitwise-bit-count mask))
                       (best
                         (let loop ((j 0) (cur-best -1))
                           (if (= j m)
                               cur-best
                               (if (zero? (bitwise-and mask (arithmetic-shift 1 j)))
                                   (let ((val (+ (vector-ref (vector-ref scores i) j)
                                                 (dfs (bitwise-ior mask (arithmetic-shift 1 j))))))
                                     (loop (+ j 1) (max cur-best val)))
                                   (loop (+ j 1) cur-best)))) ))
                  (vector-set! memo mask best)
                  best))))))
    (dfs 0)))
```

## Erlang

```erlang
-spec max_compatibility_sum(Students :: [[integer()]], Mentors :: [[integer()]]) -> integer().
max_compatibility_sum(Students, Mentors) ->
    M = length(Students),
    Scores = compute_scores(Students, Mentors),
    MaxMask = (1 bsl M) - 1,
    DP0 = maps:put(0, 0, #{}),
    DP = dp_iterate(0, MaxMask, Scores, DP0, M),
    maps:get(MaxMask, DP).

compute_scores(Students, Mentors) ->
    Rows = [ [compatibility(S, Mt) || Mt <- Mentors] || S <- Students],
    TupleRows = [list_to_tuple(R) || R <- Rows],
    list_to_tuple(TupleRows).

compatibility(Student, Mentor) ->
    lists:foldl(fun({S,M}, Acc) -> if S =:= M -> Acc+1; true -> Acc end end,
                0,
                lists:zip(Student, Mentor)).

dp_iterate(CurMask, MaxMask, _Scores, DP, _M) when CurMask > MaxMask ->
    DP;
dp_iterate(CurMask, MaxMask, Scores, DP, M) ->
    case maps:find(CurMask, DP) of
        error ->
            dp_iterate(CurMask+1, MaxMask, Scores, DP, M);
        {ok, CurVal} ->
            StudentIdx = popcount(CurMask),
            NewDP = assign_mentor(StudentIdx, CurMask, Scores, CurVal, DP, M),
            dp_iterate(CurMask+1, MaxMask, Scores, NewDP, M)
    end.

assign_mentor(StudentIdx, Mask, Scores, CurVal, DP, M) ->
    lists:foldl(fun(J, AccDP) ->
        case (Mask band (1 bsl J)) of
            0 ->
                NewMask = Mask bor (1 bsl J),
                Score = element(J+1, element(StudentIdx+1, Scores)),
                Prev = maps:get(NewMask, AccDP, -1),
                NewVal = CurVal + Score,
                if NewVal > Prev -> maps:put(NewMask, NewVal, AccDP);
                   true -> AccDP
                end;
            _ ->
                AccDP
        end
    end, DP, lists:seq(0, M-1)).

popcount(0) -> 0;
popcount(N) -> (N band 1) + popcount(N bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_compatibility_sum(students :: [[integer]], mentors :: [[integer]]) :: integer
  def max_compatibility_sum(students, mentors) do
    m = length(students)

    scores =
      for s <- students do
        for t <- mentors do
          Enum.zip(s, t)
          |> Enum.count(fn {a, b} -> a == b end)
        end
      end

    {ans, _} = dfs(0, 0, m, scores, %{})
    ans
  end

  defp dfs(mask, idx, m, scores, memo) do
    case Map.fetch(memo, mask) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if idx == m do
          {0, Map.put(memo, mask, 0)}
        else
          {best, new_memo} =
            Enum.reduce(0..(m - 1), {-1_000_000, memo}, fn j, {cur_best, cur_mem} ->
              if (mask &&& (1 <<< j)) == 0 do
                {sub_val, sub_mem} = dfs(mask ||| (1 <<< j), idx + 1, m, scores, cur_mem)
                total = Enum.at(Enum.at(scores, idx), j) + sub_val

                if total > cur_best do
                  {total, sub_mem}
                else
                  {cur_best, sub_mem}
                end
              else
                {cur_best, cur_mem}
              end
            end)

          final_memo = Map.put(new_memo, mask, best)
          {best, final_memo}
        end
    end
  end
end
```
