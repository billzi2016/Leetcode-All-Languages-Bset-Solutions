# 2965. Find Missing and Repeated Values

## Cpp

```cpp
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        long long total = 1LL * n * n;
        long long sum = 0, sqrSum = 0;
        for (auto& row : grid) {
            for (int val : row) {
                sum += val;
                sqrSum += 1LL * val * val;
            }
        }
        long long expectedSum = total * (total + 1) / 2;
        long long expectedSq = total * (total + 1) * (2 * total + 1) / 6;
        long long diff = sum - expectedSum;               // repeat - missing
        long long diffSq = sqrSum - expectedSq;           // repeat^2 - missing^2
        long long sum_xy = diffSq / diff;                // repeat + missing
        long long repeat = (diff + sum_xy) / 2;
        long long missing = sum_xy - repeat;
        return {(int)repeat, (int)missing};
    }
};
```

## Java

```java
class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        long total = (long) n * n;

        long expectedSum = total * (total + 1) / 2;
        long expectedSqSum = total * (total + 1) * (2 * total + 1) / 6;

        long sum = 0;
        long sqSum = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                sum += val;
                sqSum += (long) val * val;
            }
        }

        long diff = sum - expectedSum;          // repeated - missing
        long sqDiff = sqSum - expectedSqSum;    // repeated^2 - missing^2

        long repeat = (sqDiff / diff + diff) / 2;
        long missing = repeat - diff;

        return new int[]{(int) repeat, (int) missing};
    }
}
```

## Python

```python
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        total = n * n
        seen = set()
        repeat = -1
        actual_sum = 0

        for row in grid:
            for val in row:
                actual_sum += val
                if val in seen:
                    repeat = val
                else:
                    seen.add(val)

        expected_sum = total * (total + 1) // 2
        missing = expected_sum - (actual_sum - repeat)
        return [repeat, missing]
```

## Python3

```python
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = {}
        repeat = -1
        for row in grid:
            for val in row:
                if val in seen:
                    repeat = val
                else:
                    seen[val] = 1
        total = n * n
        missing = -1
        for num in range(1, total + 1):
            if num not in seen:
                missing = num
                break
        return [repeat, missing]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingAndRepeatedValues(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    long long actualSum = 0;
    long long actualSqSum = 0;
    
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < gridColSize[i]; ++j) {
            int val = grid[i][j];
            actualSum += val;
            actualSqSum += (long long)val * val;
        }
    }
    
    long long n = gridSize;
    long long total = n * n;                     // total numbers expected
    long long expectedSum = total * (total + 1) / 2;
    long long expectedSqSum = total * (total + 1) * (2 * total + 1) / 6;
    
    long long sumDiff = actualSum - expectedSum;          // repeat - missing
    long long sqrDiff = actualSqSum - expectedSqSum;      // repeat^2 - missing^2
    
    long long repeat = (sqrDiff / sumDiff + sumDiff) / 2;
    long long missing = repeat - sumDiff;
    
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = (int)repeat;
    ans[1] = (int)missing;
    *returnSize = 2;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindMissingAndRepeatedValues(int[][] grid) {
        int n = grid.Length;
        long total = (long)n * n;
        long expectedSum = total * (total + 1) / 2;
        long expectedSqSum = total * (total + 1) * (2 * total + 1) / 6;

        long sum = 0, sqSum = 0;
        for (int i = 0; i < n; i++) {
            int[] row = grid[i];
            for (int j = 0; j < n; j++) {
                long val = row[j];
                sum += val;
                sqSum += val * val;
            }
        }

        long diff = sum - expectedSum;          // repeated - missing
        long sqDiff = sqSum - expectedSqSum;    // repeated^2 - missing^2

        long sumXY = sqDiff / diff;             // repeated + missing

        int repeat = (int)((sumXY + diff) / 2);
        int missing = (int)((sumXY - diff) / 2);

        return new int[] { repeat, missing };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    const n = grid.length;
    const total = n * n;
    let sum = 0;
    let sqrSum = 0;
    for (let i = 0; i < n; ++i) {
        const row = grid[i];
        for (let j = 0; j < n; ++j) {
            const val = row[j];
            sum += val;
            sqrSum += val * val;
        }
    }
    const expectedSum = total * (total + 1) / 2;
    const expectedSqSum = total * (total + 1) * (2 * total + 1) / 6;
    
    const diff = sum - expectedSum;               // repeat - missing
    const sqDiff = sqrSum - expectedSqSum;        // repeat^2 - missing^2
    
    const sumXY = sqDiff / diff;                  // repeat + missing
    const repeat = (diff + sumXY) / 2;
    const missing = sumXY - repeat;
    
    return [repeat, missing];
};
```

## Typescript

```typescript
function findMissingAndRepeatedValues(grid: number[][]): number[] {
    const n = grid.length;
    const total = n * n;

    let sum = 0;
    let sqrSum = 0;

    for (let i = 0; i < n; i++) {
        const row = grid[i];
        for (let j = 0; j < n; j++) {
            const val = row[j];
            sum += val;
            sqrSum += val * val;
        }
    }

    const expectedSum = total * (total + 1) / 2;
    const expectedSqSum = total * (total + 1) * (2 * total + 1) / 6;

    const diff = sum - expectedSum;               // repeated - missing
    const sqDiff = sqrSum - expectedSqSum;         // repeated^2 - missing^2

    const sumXY = sqDiff / diff;                  // repeated + missing

    const repeated = (sumXY + diff) / 2;
    const missing = sumXY - repeated;

    return [repeated, missing];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[]
     */
    function findMissingAndRepeatedValues($grid) {
        $n = count($grid);
        $total = $n * $n;

        $sum = 0;
        $sqSum = 0;

        foreach ($grid as $row) {
            foreach ($row as $val) {
                $sum += $val;
                $sqSum += $val * $val;
            }
        }

        $expectedSum = intdiv($total * ($total + 1), 2);
        $expectedSqSum = intdiv($total * ($total + 1) * (2 * $total + 1), 6);

        $diff = $sum - $expectedSum;               // repeated - missing
        $sqDiff = $sqSum - $expectedSqSum;         // repeated^2 - missing^2

        // (repeated + missing) = sqDiff / diff
        $sumVals = intdiv($sqDiff, $diff);

        $repeat = intdiv($sumVals + $diff, 2);
        $missing = intdiv($sumVals - $diff, 2);

        return [$repeat, $missing];
    }
}
```

## Swift

```swift
class Solution {
    func findMissingAndRepeatedValues(_ grid: [[Int]]) -> [Int] {
        let n = grid.count
        let total = n * n
        var freq = [Int](repeating: 0, count: total + 1)
        
        for row in grid {
            for val in row {
                if val >= 1 && val <= total {
                    freq[val] += 1
                }
            }
        }
        
        var repeatVal = -1
        var missingVal = -1
        
        for i in 1...total {
            if freq[i] == 2 {
                repeatVal = i
            } else if freq[i] == 0 {
                missingVal = i
            }
        }
        
        return [repeatVal, missingVal]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMissingAndRepeatedValues(grid: Array<IntArray>): IntArray {
        val n = grid.size
        val total = n * n
        var sum = 0L
        var sqSum = 0L
        for (i in 0 until n) {
            val row = grid[i]
            for (j in 0 until n) {
                val v = row[j].toLong()
                sum += v
                sqSum += v * v
            }
        }
        val expectedSum = total.toLong() * (total + 1) / 2
        val expectedSqSum = total.toLong() * (total + 1) * (2L * total + 1) / 6
        val diff = sum - expectedSum          // repeated - missing
        val sqDiff = sqSum - expectedSqSum    // repeated^2 - missing^2
        val sumXY = sqDiff / diff            // repeated + missing
        val repeat = ((sumXY + diff) / 2).toInt()
        val missing = ((sumXY - diff) / 2).toInt()
        return intArrayOf(repeat, missing)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findMissingAndRepeatedValues(List<List<int>> grid) {
    int n = grid.length;
    int total = n * n;

    int sum = 0;
    int sqSum = 0;
    for (var row in grid) {
      for (int val in row) {
        sum += val;
        sqSum += val * val;
      }
    }

    int expectedSum = total * (total + 1) ~/ 2;
    int expectedSqSum = total * (total + 1) * (2 * total + 1) ~/ 6;

    int diff = sum - expectedSum; // repeated - missing
    int sqDiff = sqSum - expectedSqSum; // repeated^2 - missing^2

    int sumXY = sqDiff ~/ diff; // repeated + missing

    int repeated = (sumXY + diff) ~/ 2;
    int missing = repeated - diff;

    return [repeated, missing];
  }
}
```

## Golang

```go
package main

func findMissingAndRepeatedValues(grid [][]int) []int {
	n := len(grid)
	total := n * n

	var sum, sqSum int64
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			v := int64(grid[i][j])
			sum += v
			sqSum += v * v
		}
	}

	total64 := int64(total)
	expectedSum := total64 * (total64 + 1) / 2
	expectedSqSum := total64 * (total64 + 1) * (2*total64 + 1) / 6

	diff := sum - expectedSum          // repeated - missing
	sqDiff := sqSum - expectedSqSum    // repeated^2 - missing^2

	repeat := (sqDiff/diff + diff) / 2
	missing := repeat - diff

	return []int{int(repeat), int(missing)}
}
```

## Ruby

```ruby
def find_missing_and_repeated_values(grid)
  n = grid.length
  total = n * n
  freq = Array.new(total + 1, 0)
  repeat = -1
  missing = -1

  grid.each do |row|
    row.each do |val|
      if freq[val] == 1
        repeat = val
      end
      freq[val] += 1
    end
  end

  (1..total).each do |i|
    if freq[i] == 0
      missing = i
      break
    end
  end

  [repeat, missing]
end
```

## Scala

```scala
object Solution {
    def findMissingAndRepeatedValues(grid: Array[Array[Int]]): Array[Int] = {
        val n = grid.length
        var sum: Long = 0L
        var sqSum: Long = 0L
        var i = 0
        while (i < n) {
            val row = grid(i)
            var j = 0
            while (j < n) {
                val v = row(j).toLong
                sum += v
                sqSum += v * v
                j += 1
            }
            i += 1
        }
        val total: Long = n.toLong * n
        val expectedSum: Long = total * (total + 1) / 2
        val expectedSqSum: Long = total * (total + 1) * (2 * total + 1) / 6
        val diff: Long = sum - expectedSum          // repeated - missing
        val sqDiff: Long = sqSum - expectedSqSum    // repeated^2 - missing^2
        val repeatLong: Long = (sqDiff / diff + diff) / 2
        val missingLong: Long = repeatLong - diff
        Array(repeatLong.toInt, missingLong.toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len() as i64;
        let total = n * n;

        let mut sum: i64 = 0;
        let mut sq_sum: i64 = 0;
        for row in &grid {
            for &val in row {
                let v = val as i64;
                sum += v;
                sq_sum += v * v;
            }
        }

        let expected_sum = total * (total + 1) / 2;
        let expected_sq_sum = total * (total + 1) * (2 * total + 1) / 6;

        let diff = sum - expected_sum; // repeated - missing
        let sq_diff = sq_sum - expected_sq_sum; // repeated^2 - missing^2

        let repeat = ((sq_diff / diff) + diff) / 2;
        let missing = repeat - diff;

        vec![repeat as i32, missing as i32]
    }
}
```

## Racket

```racket
(define/contract (find-missing-and-repeated-values grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length grid))
         (total (* n n))
         (expected-sum (/ (* total (+ total 1)) 2))
         (expected-square-sum
          (/ (* total (+ total 1) (+ (* 2 total) 1)) 6)))
    (let-values ([(actual-sum actual-sq)
                  (for/fold ([sum 0] [sq 0]) ([row grid])
                    (for/fold ([sum sum] [sq sq]) ([v row])
                      (values (+ sum v) (+ sq (* v v)))) )])
      (let* ((diff (- actual-sum expected-sum))
             (square-diff (- actual-sq expected-square-sum))
             (repeat (/ (+ (/ square-diff diff) diff) 2))
             (missing (/ (- (/ square-diff diff) diff) 2)))
        (list repeat missing)))))
```

## Erlang

```erlang
-module(solution).
-export([find_missing_and_repeated_values/1]).

-spec find_missing_and_repeated_values(Grid :: [[integer()]]) -> [integer()].
find_missing_and_repeated_values(Grid) ->
    N = length(Grid),
    Total = N * N,
    FreqMap = build_freq_map(Grid, #{}),
    {Repeat, Missing} = find_vals(1, Total, FreqMap, undefined, undefined),
    [Repeat, Missing].

build_freq_map([], Map) -> Map;
build_freq_map([Row|Rest], Map) ->
    NewMap = lists:foldl(fun (Num, Acc) ->
        Count = maps:get(Num, Acc, 0),
        maps:put(Num, Count + 1, Acc)
    end, Map, Row),
    build_freq_map(Rest, NewMap).

find_vals(Cur, Max, _Map, Repeat, Missing) when Cur > Max ->
    {Repeat, Missing};
find_vals(Cur, Max, Map, RepeatAcc, MissingAcc) ->
    case maps:find(Cur, Map) of
        error -> % missing number
            find_vals(Cur + 1, Max, Map, RepeatAcc, Cur);
        {ok, 2} -> % repeated number
            find_vals(Cur + 1, Max, Map, Cur, MissingAcc);
        _ ->
            find_vals(Cur + 1, Max, Map, RepeatAcc, MissingAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_missing_and_repeated_values(grid :: [[integer]]) :: [integer]
  def find_missing_and_repeated_values(grid) do
    n = length(grid)
    total = n * n

    {sum, sqr_sum} =
      Enum.reduce(grid, {0, 0}, fn row, {s, ss} ->
        Enum.reduce(row, {s, ss}, fn val, {s2, ss2} ->
          {s2 + val, ss2 + val * val}
        end)
      end)

    expected_sum = div(total * (total + 1), 2)
    expected_sqrsum = div(total * (total + 1) * (2 * total + 1), 6)

    sum_diff = sum - expected_sum
    sqr_diff = sqr_sum - expected_sqrsum

    repeat_plus_missing = div(sqr_diff, sum_diff)
    repeat = div(repeat_plus_missing + sum_diff, 2)
    missing = repeat_plus_missing - repeat

    [repeat, missing]
  end
end
```
