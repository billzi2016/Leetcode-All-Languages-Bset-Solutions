# 2151. Maximum Good People Based on Statements

## Cpp

```cpp
class Solution {
public:
    int maximumGood(vector<vector<int>>& statements) {
        int n = statements.size();
        int best = 0;
        int totalMasks = 1 << n;
        for (int mask = 0; mask < totalMasks; ++mask) {
            bool ok = true;
            for (int i = 0; i < n && ok; ++i) {
                if ((mask >> i) & 1) { // person i is good
                    for (int j = 0; j < n; ++j) {
                        int s = statements[i][j];
                        if (s == 2) continue;
                        bool jGood = (mask >> j) & 1;
                        if ((s == 1 && !jGood) || (s == 0 && jGood)) {
                            ok = false;
                            break;
                        }
                    }
                }
            }
            if (ok) {
                int cnt = __builtin_popcount(mask);
                best = max(best, cnt);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maximumGood(int[][] statements) {
        int n = statements.length;
        int maxGood = 0;
        int totalMasks = 1 << n;
        for (int mask = 0; mask < totalMasks; mask++) {
            boolean valid = true;
            for (int i = 0; i < n && valid; i++) {
                if ((mask & (1 << i)) == 0) continue; // person i is bad, no constraints
                for (int j = 0; j < n; j++) {
                    int stmt = statements[i][j];
                    if (stmt == 2) continue;
                    boolean jGood = (mask & (1 << j)) != 0;
                    if ((stmt == 1 && !jGood) || (stmt == 0 && jGood)) {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                int goodCount = Integer.bitCount(mask);
                if (goodCount > maxGood) maxGood = goodCount;
            }
        }
        return maxGood;
    }
}
```

## Python

```python
class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        max_good = 0
        for mask in range(1 << n):
            valid = True
            # check each person assumed good
            for i in range(n):
                if not (mask >> i) & 1:
                    continue
                for j in range(n):
                    s = statements[i][j]
                    if s == 2:
                        continue
                    if s == 1 and ((mask >> j) & 1) == 0:
                        valid = False
                        break
                    if s == 0 and ((mask >> j) & 1) == 1:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                good_cnt = bin(mask).count("1")
                if good_cnt > max_good:
                    max_good = good_cnt
        return max_good
```

## Python3

```python
from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        for mask in range(1 << n):
            valid = True
            # check consistency for each person assumed good
            for i in range(n):
                if (mask >> i) & 1:
                    row = statements[i]
                    for j in range(n):
                        s = row[j]
                        if s == 2:
                            continue
                        if s == 1 and not ((mask >> j) & 1):
                            valid = False
                            break
                        if s == 0 and ((mask >> j) & 1):
                            valid = False
                            break
                if not valid:
                    break
            if valid:
                good_cnt = mask.bit_count()
                if good_cnt > max_good:
                    max_good = good_cnt
        return max_good
```

## C

```c
int maximumGood(int** statements, int statementsSize, int* statementsColSize) {
    int n = statementsSize;
    int max_good = 0;
    int total_masks = 1 << n;
    for (int mask = 0; mask < total_masks; ++mask) {
        int valid = 1;
        for (int i = 0; i < n && valid; ++i) {
            if ((mask >> i) & 1) { // person i is good
                for (int j = 0; j < n; ++j) {
                    int stmt = statements[i][j];
                    if (stmt == 2) continue;
                    int isGoodJ = (mask >> j) & 1;
                    if ((stmt == 1 && !isGoodJ) || (stmt == 0 && isGoodJ)) {
                        valid = 0;
                        break;
                    }
                }
            }
        }
        if (valid) {
            int cnt = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i) & 1) ++cnt;
            }
            if (cnt > max_good) max_good = cnt;
        }
    }
    return max_good;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumGood(int[][] statements)
    {
        int n = statements.Length;
        int maxGood = 0;

        int totalMasks = 1 << n;
        for (int mask = 0; mask < totalMasks; ++mask)
        {
            bool ok = true;
            for (int i = 0; i < n && ok; ++i)
            {
                if (((mask >> i) & 1) == 1) // person i is good
                {
                    for (int j = 0; j < n; ++j)
                    {
                        int s = statements[i][j];
                        if (s == 2) continue; // no statement / self

                        bool jGood = ((mask >> j) & 1) == 1;
                        if (s == 1 && !jGood) { ok = false; break; } // said good but actually bad
                        if (s == 0 && jGood) { ok = false; break; }   // said bad but actually good
                    }
                }
            }

            if (ok)
            {
                int cnt = CountBits(mask);
                if (cnt > maxGood) maxGood = cnt;
            }
        }

        return maxGood;
    }

    private int CountBits(int x)
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
 * @param {number[][]} statements
 * @return {number}
 */
var maximumGood = function(statements) {
    const n = statements.length;
    const totalMasks = 1 << n;
    let best = 0;

    for (let mask = 0; mask < totalMasks; ++mask) {
        let valid = true;
        // verify all good people statements
        for (let i = 0; i < n && valid; ++i) {
            if ((mask >> i) & 1) { // person i is good
                for (let j = 0; j < n; ++j) {
                    const stmt = statements[i][j];
                    if (stmt === 2) continue; // no info about self or neutral
                    const isGoodJ = (mask >> j) & 1;
                    if ((stmt === 1 && !isGoodJ) || (stmt === 0 && isGoodJ)) {
                        valid = false;
                        break;
                    }
                }
            }
        }
        if (valid) {
            // count bits in mask
            let cnt = 0, m = mask;
            while (m) {
                cnt += m & 1;
                m >>= 1;
            }
            if (cnt > best) best = cnt;
        }
    }

    return best;
};
```

## Typescript

```typescript
function maximumGood(statements: number[][]): number {
    const n = statements.length;
    let maxGood = 0;

    const popcount = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    const totalMasks = 1 << n;
    for (let mask = 0; mask < totalMasks; ++mask) {
        let valid = true;

        for (let i = 0; i < n && valid; ++i) {
            if ((mask >> i) & 1) { // person i is good
                for (let j = 0; j < n; ++j) {
                    const stmt = statements[i][j];
                    if (stmt === 2) continue; // self statement, ignore
                    if (stmt === 1 && ((mask >> j) & 1) === 0) { // says j good but j is bad
                        valid = false;
                        break;
                    }
                    if (stmt === 0 && ((mask >> j) & 1) === 1) { // says j bad but j is good
                        valid = false;
                        break;
                    }
                }
            }
        }

        if (valid) {
            const cnt = popcount(mask);
            if (cnt > maxGood) maxGood = cnt;
        }
    }

    return maxGood;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $statements
     * @return Integer
     */
    function maximumGood($statements) {
        $n = count($statements);
        $maxGood = 0;
        $totalMasks = 1 << $n;

        for ($mask = 0; $mask < $totalMasks; $mask++) {
            $valid = true;

            // Verify statements of all people assumed to be good in this mask
            for ($i = 0; $i < $n && $valid; $i++) {
                if ((($mask >> $i) & 1) === 1) { // person i is good
                    for ($j = 0; $j < $n; $j++) {
                        $stmt = $statements[$i][$j];
                        if ($stmt == 2) continue; // no statement

                        $isGoodJ = (($mask >> $j) & 1) === 1;
                        if ($stmt == 1 && !$isGoodJ) { // says good but actually bad
                            $valid = false;
                            break;
                        }
                        if ($stmt == 0 && $isGoodJ) { // says bad but actually good
                            $valid = false;
                            break;
                        }
                    }
                }
            }

            if ($valid) {
                // count number of set bits (good people)
                $cnt = 0;
                $temp = $mask;
                while ($temp) {
                    $cnt += $temp & 1;
                    $temp >>= 1;
                }
                if ($cnt > $maxGood) {
                    $maxGood = $cnt;
                }
            }
        }

        return $maxGood;
    }
}
```

## Swift

```swift
class Solution {
    func maximumGood(_ statements: [[Int]]) -> Int {
        let n = statements.count
        var best = 0
        let totalMasks = 1 << n
        
        for mask in 0..<totalMasks {
            var valid = true
            // Check each person assumed to be good
            for i in 0..<n where ((mask >> i) & 1) == 1 {
                for j in 0..<n {
                    let stmt = statements[i][j]
                    if stmt == 2 { continue }   // no statement
                    let isGoodJ = ((mask >> j) & 1) == 1
                    if (stmt == 1 && !isGoodJ) || (stmt == 0 && isGoodJ) {
                        valid = false
                        break
                    }
                }
                if !valid { break }
            }
            if valid {
                best = max(best, mask.nonzeroBitCount)
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumGood(statements: Array<IntArray>): Int {
        val n = statements.size
        var maxGood = 0
        val totalMasks = 1 shl n
        for (mask in 0 until totalMasks) {
            var valid = true
            // check each person assumed good
            for (i in 0 until n) {
                if ((mask shr i) and 1 == 1) { // person i is good
                    for (j in 0 until n) {
                        val s = statements[i][j]
                        if (s == 2) continue
                        val expectedGood = s == 1
                        val actualGood = ((mask shr j) and 1) == 1
                        if (expectedGood != actualGood) {
                            valid = false
                            break
                        }
                    }
                    if (!valid) break
                }
            }
            if (valid) {
                val goodCount = Integer.bitCount(mask)
                if (goodCount > maxGood) maxGood = goodCount
            }
        }
        return maxGood
    }
}
```

## Dart

```dart
class Solution {
  int maximumGood(List<List<int>> statements) {
    int n = statements.length;
    int maxGood = 0;
    int totalMasks = 1 << n;

    for (int mask = 0; mask < totalMasks; ++mask) {
      bool valid = true;
      for (int i = 0; i < n && valid; ++i) {
        if ((mask & (1 << i)) != 0) { // person i is good
          for (int j = 0; j < n; ++j) {
            int s = statements[i][j];
            if (s == 2) continue; // no statement about self or irrelevant
            bool jGood = (mask & (1 << j)) != 0;
            if ((s == 1 && !jGood) || (s == 0 && jGood)) {
              valid = false;
              break;
            }
          }
        }
      }
      if (valid) {
        int cnt = _popCount(mask);
        if (cnt > maxGood) maxGood = cnt;
      }
    }

    return maxGood;
  }

  int _popCount(int x) {
    int count = 0;
    while (x != 0) {
      count += x & 1;
      x >>= 1;
    }
    return count;
  }
}
```

## Golang

```go
package main

import "math/bits"

func maximumGood(statements [][]int) int {
	n := len(statements)
	maxGood := 0
	total := 1 << n
	for mask := 0; mask < total; mask++ {
		if isValid(mask, statements, n) {
			cnt := bits.OnesCount(uint(mask))
			if cnt > maxGood {
				maxGood = cnt
			}
		}
	}
	return maxGood
}

func isValid(mask int, statements [][]int, n int) bool {
	for i := 0; i < n; i++ {
		if (mask>>i)&1 == 1 { // person i is good
			for j := 0; j < n; j++ {
				s := statements[i][j]
				if s == 2 {
					continue
				}
				if s == 1 && ((mask>>j)&1) == 0 {
					return false
				}
				if s == 0 && ((mask>>j)&1) == 1 {
					return false
				}
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def maximum_good(statements)
  n = statements.size
  max_good = 0
  total_masks = 1 << n

  (0...total_masks).each do |mask|
    valid = true
    n.times do |i|
      next if (mask & (1 << i)).zero? # person i is bad, no need to check their statements
      n.times do |j|
        s = statements[i][j]
        next if s == 2
        if s == 1 && (mask & (1 << j)).zero?
          valid = false
          break
        elsif s == 0 && (mask & (1 << j)) != 0
          valid = false
          break
        end
      end
      break unless valid
    end

    if valid
      good_cnt = mask.to_s(2).count('1')
      max_good = good_cnt if good_cnt > max_good
    end
  end

  max_good
end
```

## Scala

```scala
object Solution {
    def maximumGood(statements: Array[Array[Int]]): Int = {
        val n = statements.length
        var best = 0
        val total = 1 << n

        for (mask <- 0 until total) {
            var valid = true
            var i = 0
            while (i < n && valid) {
                if (((mask >> i) & 1) == 1) { // person i is good
                    var j = 0
                    while (j < n && valid) {
                        statements(i)(j) match {
                            case 0 => if (((mask >> j) & 1) == 1) valid = false
                            case 1 => if (((mask >> j) & 1) == 0) valid = false
                            case _ => // ignore 2
                        }
                        j += 1
                    }
                }
                i += 1
            }

            if (valid) {
                val cnt = Integer.bitCount(mask)
                if (cnt > best) best = cnt
            }
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_good(statements: Vec<Vec<i32>>) -> i32 {
        let n = statements.len();
        let mut best = 0i32;
        let total_masks = 1usize << n;
        for mask in 0..total_masks {
            let mut valid = true;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    // person i is good, their statements must be truthful
                    for j in 0..n {
                        match statements[i][j] {
                            0 => {
                                // says j is bad
                                if (mask >> j) & 1 == 1 {
                                    valid = false;
                                    break;
                                }
                            }
                            1 => {
                                // says j is good
                                if (mask >> j) & 1 == 0 {
                                    valid = false;
                                    break;
                                }
                            }
                            _ => {}
                        }
                    }
                }
                if !valid {
                    break;
                }
            }
            if valid {
                let cnt = mask.count_ones() as i32;
                if cnt > best {
                    best = cnt;
                }
            }
        }
        best
    }
}
```

## Racket

```racket
#lang racket
(require racket/bitwise)

(define/contract (maximum-good statements)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length statements))
         (total (expt 2 n)))
    (let max-good ((mask 0) (best 0))
      (if (= mask total)
          best
          (let ((valid?
                 (for/and ([i (in-range n)])
                   (if (= (bitwise-and (arithmetic-shift mask (- i)) 1) 1)
                       (for/and ([j (in-range n)])
                         (let ((val (list-ref (list-ref statements i) j)))
                           (or (= val 2)
                               (= (bitwise-and (arithmetic-shift mask (- j)) 1) val))))
                       #t))))
            (max-good (+ mask 1)
                      (if valid?
                          (max best (bitwise-bit-count mask))
                          best)))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_good/1]).

-spec maximum_good(Statements :: [[integer()]]) -> integer().
maximum_good(Statements) ->
    N = length(Statements),
    MaxMask = (1 bsl N) - 1,
    max_good_loop(0, MaxMask, Statements, 0).

max_good_loop(Mask, MaxMask, _Stmts, CurrentMax) when Mask > MaxMask ->
    CurrentMax;
max_good_loop(Mask, MaxMask, Stmts, CurrentMax) ->
    case is_valid(Mask, Stmts) of
        true ->
            Count = bit_count(Mask),
            NewMax = if Count > CurrentMax -> Count; true -> CurrentMax end,
            max_good_loop(Mask + 1, MaxMask, Stmts, NewMax);
        false ->
            max_good_loop(Mask + 1, MaxMask, Stmts, CurrentMax)
    end.

is_valid(Mask, Statements) ->
    N = length(Statements),
    is_valid_mask(0, N, Mask, Statements).

is_valid_mask(I, N, _Mask, _Stmts) when I == N ->
    true;
is_valid_mask(I, N, Mask, Stmts) ->
    case (Mask bsr I) band 1 of
        1 -> % person i is good, statements must match
            Row = lists:nth(I + 1, Stmts),
            case check_row(Row, 0, Mask) of
                true -> is_valid_mask(I + 1, N, Mask, Stmts);
                false -> false
            end;
        0 ->
            % bad person, no constraints
            is_valid_mask(I + 1, N, Mask, Stmts)
    end.

check_row(Row, J, _Mask) when J == length(Row) ->
    true;
check_row(Row, J, Mask) ->
    Val = lists:nth(J + 1, Row),
    case Val of
        2 -> % no statement about self or irrelevant
            check_row(Row, J + 1, Mask);
        _ ->
            Expected = Val,
            Actual = (Mask bsr J) band 1,
            if Expected == Actual ->
                    check_row(Row, J + 1, Mask);
               true ->
                    false
            end
    end.

bit_count(0) -> 0;
bit_count(N) -> (N band 1) + bit_count(N bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec maximum_good(statements :: [[integer]]) :: integer
  def maximum_good(statements) do
    n = length(statements)

    Enum.reduce(0..<(1 <<< n), 0, fn mask, best ->
      if valid?(mask, statements, n) do
        cnt = bit_count(mask)
        if cnt > best, do: cnt, else: best
      else
        best
      end
    end)
  end

  defp valid?(mask, statements, n) do
    Enum.reduce_while(0..(n - 1), true, fn i, _ ->
      if ((mask >>> i) &&& 1) == 1 do
        row = Enum.at(statements, i)

        consistent =
          Enum.reduce_while(0..(n - 1), true, fn j, _ ->
            s = Enum.at(row, j)

            cond do
              s == 2 -> {:cont, true}
              s == 1 and ((mask >>> j) &&& 1) == 0 -> {:halt, false}
              s == 0 and ((mask >>> j) &&& 1) == 1 -> {:halt, false}
              true -> {:cont, true}
            end
          end)

        if consistent, do: {:cont, true}, else: {:halt, false}
      else
        {:cont, true}
      end
    end) == true
  end

  defp bit_count(mask), do: count_bits(mask, 0)

  defp count_bits(0, acc), do: acc
  defp count_bits(m, acc), do: count_bits(m &&& (m - 1), acc + 1)
end
```
