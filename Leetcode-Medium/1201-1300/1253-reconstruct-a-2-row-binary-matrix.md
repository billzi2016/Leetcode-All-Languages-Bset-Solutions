# 1253. Reconstruct a 2-Row Binary Matrix

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
        int n = colsum.size();
        vector<vector<int>> res(2, vector<int>(n, 0));
        // First handle columns with sum 2
        for (int i = 0; i < n; ++i) {
            if (colsum[i] == 2) {
                if (upper <= 0 || lower <= 0) return {};
                res[0][i] = 1;
                res[1][i] = 1;
                --upper;
                --lower;
            }
        }
        // Then handle columns with sum 1
        for (int i = 0; i < n; ++i) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    res[0][i] = 1;
                    --upper;
                } else if (lower > 0) {
                    res[1][i] = 1;
                    --lower;
                } else {
                    return {};
                }
            }
        }
        // Verify all counts used up
        if (upper != 0 || lower != 0) return {};
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        int n = colsum.length;
        int[] top = new int[n];
        int[] bottom = new int[n];

        // Handle columns with sum 2 and 0
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 2) {
                top[i] = 1;
                bottom[i] = 1;
                upper--;
                lower--;
            }
        }

        if (upper < 0 || lower < 0) {
            return new ArrayList<>();
        }

        // Handle columns with sum 1
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    bottom[i] = 0;
                    upper--;
                } else if (lower > 0) {
                    top[i] = 0;
                    bottom[i] = 1;
                    lower--;
                } else {
                    return new ArrayList<>();
                }
            }
        }

        if (upper != 0 || lower != 0) {
            return new ArrayList<>();
        }

        List<List<Integer>> result = new ArrayList<>(2);
        List<Integer> rowTop = new ArrayList<>(n);
        List<Integer> rowBottom = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            rowTop.add(top[i]);
            rowBottom.add(bottom[i]);
        }
        result.add(rowTop);
        result.add(rowBottom);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n

        # First handle columns with sum 2
        for i, v in enumerate(colsum):
            if v == 2:
                top[i] = 1
                bottom[i] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []

        # Then handle columns with sum 1
        for i, v in enumerate(colsum):
            if v == 1:
                if upper > 0:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1

        # Validate remaining counts
        if upper != 0 or lower != 0:
            return []

        return [top, bottom]
```

## Python3

```python
from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        top = [0] * n
        bottom = [0] * n

        # Handle columns with sum 2
        for i, v in enumerate(colsum):
            if v == 2:
                top[i] = 1
                bottom[i] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []

        # Handle columns with sum 1
        for i, v in enumerate(colsum):
            if v == 1:
                if upper > 0:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1

        if upper != 0 or lower != 0:
            return []

        return [top, bottom]
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** reconstructMatrix(int upper, int lower, int* colsum, int colsumSize, int* returnSize, int** returnColumnSizes) {
    int n = colsumSize;
    // Allocate result matrix
    int **ans = (int **)malloc(2 * sizeof(int *));
    if (!ans) return NULL;
    ans[0] = (int *)calloc(n, sizeof(int));
    ans[1] = (int *)calloc(n, sizeof(int));
    if (!ans[0] || !ans[1]) {
        free(ans[0]);
        free(ans[1]);
        free(ans);
        return NULL;
    }

    // First pass: handle colsum == 2 and 0
    for (int i = 0; i < n; ++i) {
        if (colsum[i] == 2) {
            ans[0][i] = 1;
            ans[1][i] = 1;
            upper--;
            lower--;
        }
    }

    // If counts already invalid, clean up
    if (upper < 0 || lower < 0) {
        free(ans[0]);
        free(ans[1]);
        free(ans);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Second pass: handle colsum == 1
    for (int i = 0; i < n; ++i) {
        if (colsum[i] == 1) {
            if (upper > 0) {
                ans[0][i] = 1;
                upper--;
            } else {
                ans[1][i] = 1;
                lower--;
            }
        }
    }

    // Final validation
    if (upper != 0 || lower != 0) {
        free(ans[0]);
        free(ans[1]);
        free(ans);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Prepare return values
    *returnSize = 2;
    *returnColumnSizes = (int *)malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = n;
    (*returnColumnSizes)[1] = n;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> ReconstructMatrix(int upper, int lower, int[] colsum) {
        int n = colsum.Length;
        int[] top = new int[n];
        int[] bottom = new int[n];

        // Handle columns with sum 2
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 2) {
                top[i] = 1;
                bottom[i] = 1;
                upper--;
                lower--;
                if (upper < 0 || lower < 0) {
                    return new List<IList<int>>();
                }
            }
        }

        // Handle columns with sum 1
        for (int i = 0; i < n; i++) {
            if (colsum[i] == 1) {
                if (upper > 0) {
                    top[i] = 1;
                    upper--;
                } else {
                    bottom[i] = 1;
                    lower--;
                }
                if (upper < 0 || lower < 0) {
                    return new List<IList<int>>();
                }
            }
        }

        // Verify all sums satisfied
        if (upper != 0 || lower != 0) {
            return new List<IList<int>>();
        }

        var result = new List<IList<int>>(2);
        result.Add(top.ToList());
        result.Add(bottom.ToList());
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} upper
 * @param {number} lower
 * @param {number[]} colsum
 * @return {number[][]}
 */
var reconstructMatrix = function(upper, lower, colsum) {
    const n = colsum.length;
    const top = new Array(n).fill(0);
    const bottom = new Array(n).fill(0);
    
    // First handle columns with sum 2
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 2) {
            top[i] = 1;
            bottom[i] = 1;
            upper--;
            lower--;
        }
    }
    
    // If counts become negative, impossible
    if (upper < 0 || lower < 0) return [];
    
    // Then handle columns with sum 1
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 1) {
            if (upper > 0) {
                top[i] = 1;
                bottom[i] = 0;
                upper--;
            } else {
                top[i] = 0;
                bottom[i] = 1;
                lower--;
            }
        }
    }
    
    // Final validation
    if (upper !== 0 || lower !== 0) return [];
    
    return [top, bottom];
};
```

## Typescript

```typescript
function reconstructMatrix(upper: number, lower: number, colsum: number[]): number[][] {
    const n = colsum.length;
    const top = new Array<number>(n).fill(0);
    const bottom = new Array<number>(n).fill(0);

    // Handle columns with sum 2 first
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 2) {
            if (upper === 0 || lower === 0) return [];
            top[i] = 1;
            bottom[i] = 1;
            upper--;
            lower--;
        }
    }

    // Handle columns with sum 1
    for (let i = 0; i < n; i++) {
        if (colsum[i] === 1) {
            if (upper > 0) {
                top[i] = 1;
                bottom[i] = 0;
                upper--;
            } else if (lower > 0) {
                top[i] = 0;
                bottom[i] = 1;
                lower--;
            } else {
                return [];
            }
        }
    }

    // If any remaining counts, impossible
    if (upper !== 0 || lower !== 0) return [];

    return [top, bottom];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $upper
     * @param Integer $lower
     * @param Integer[] $colsum
     * @return Integer[][]
     */
    function reconstructMatrix($upper, $lower, $colsum) {
        $n = count($colsum);
        $top = array_fill(0, $n, 0);
        $bottom = array_fill(0, $n, 0);

        // Handle columns with sum 2
        for ($i = 0; $i < $n; $i++) {
            if ($colsum[$i] == 2) {
                $top[$i] = 1;
                $bottom[$i] = 1;
                $upper--;
                $lower--;
            }
        }

        // If counts become negative, impossible
        if ($upper < 0 || $lower < 0) {
            return [];
        }

        // Handle columns with sum 1
        for ($i = 0; $i < $n; $i++) {
            if ($colsum[$i] == 1) {
                if ($upper > 0) {
                    $top[$i] = 1;
                    $upper--;
                } else {
                    $bottom[$i] = 1;
                    $lower--;
                }
            }
        }

        // Verify all counts satisfied
        if ($upper === 0 && $lower === 0) {
            return [$top, $bottom];
        }

        return [];
    }
}
```

## Swift

```swift
class Solution {
    func reconstructMatrix(_ upper: Int, _ lower: Int, _ colsum: [Int]) -> [[Int]] {
        var up = upper
        var low = lower
        let n = colsum.count
        var top = Array(repeating: 0, count: n)
        var bottom = Array(repeating: 0, count: n)
        
        // First handle columns with sum == 2
        for i in 0..<n {
            if colsum[i] == 2 {
                top[i] = 1
                bottom[i] = 1
                up -= 1
                low -= 1
                if up < 0 || low < 0 { return [] }
            }
        }
        
        // Then handle columns with sum == 1
        for i in 0..<n {
            if colsum[i] == 1 {
                if up > 0 {
                    top[i] = 1
                    up -= 1
                } else if low > 0 {
                    bottom[i] = 1
                    low -= 1
                } else {
                    return []
                }
            }
        }
        
        // Validate remaining counts
        if up != 0 || low != 0 { return [] }
        return [top, bottom]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reconstructMatrix(upper: Int, lower: Int, colsum: IntArray): List<List<Int>> {
        var up = upper
        var low = lower
        val n = colsum.size
        val top = IntArray(n)
        val bottom = IntArray(n)

        // Handle columns with sum 2 or 0 first
        for (i in 0 until n) {
            when (colsum[i]) {
                2 -> {
                    if (up == 0 || low == 0) return emptyList()
                    top[i] = 1
                    bottom[i] = 1
                    up--
                    low--
                }
                0 -> {
                    // both remain 0
                }
            }
        }

        // Handle columns with sum 1
        for (i in 0 until n) {
            if (colsum[i] == 1) {
                when {
                    up > 0 -> {
                        top[i] = 1
                        bottom[i] = 0
                        up--
                    }
                    low > 0 -> {
                        top[i] = 0
                        bottom[i] = 1
                        low--
                    }
                    else -> return emptyList()
                }
            }
        }

        if (up != 0 || low != 0) return emptyList()

        val rowTop = mutableListOf<Int>()
        val rowBottom = mutableListOf<Int>()
        for (i in 0 until n) {
            rowTop.add(top[i])
            rowBottom.add(bottom[i])
        }
        return listOf(rowTop, rowBottom)
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> reconstructMatrix(int upper, int lower, List<int> colsum) {
    int n = colsum.length;
    List<int> top = List.filled(n, 0);
    List<int> bottom = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      if (colsum[i] == 2) {
        top[i] = 1;
        bottom[i] = 1;
        upper--;
        lower--;
        if (upper < 0 || lower < 0) {
          return <List<int>>[];
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (colsum[i] == 1) {
        if (upper > 0) {
          top[i] = 1;
          upper--;
        } else if (lower > 0) {
          bottom[i] = 1;
          lower--;
        } else {
          return <List<int>>[];
        }
      }
    }

    if (upper == 0 && lower == 0) {
      return [top, bottom];
    }
    return <List<int>>[];
  }
}
```

## Golang

```go
func reconstructMatrix(upper int, lower int, colsum []int) [][]int {
	n := len(colsum)
	top := make([]int, n)
	bottom := make([]int, n)

	for i, v := range colsum {
		if v == 2 {
			top[i] = 1
			bottom[i] = 1
			upper--
			lower--
		}
	}

	if upper < 0 || lower < 0 {
		return [][]int{}
	}

	for i, v := range colsum {
		if v == 1 {
			if upper > 0 {
				top[i] = 1
				upper--
			} else if lower > 0 {
				bottom[i] = 1
				lower--
			} else {
				return [][]int{}
			}
		}
	}

	if upper != 0 || lower != 0 {
		return [][]int{}
	}
	return [][]int{top, bottom}
}
```

## Ruby

```ruby
def reconstruct_matrix(upper, lower, colsum)
  n = colsum.length
  upper_row = Array.new(n, 0)
  lower_row = Array.new(n, 0)

  colsum.each_with_index do |c, i|
    if c == 2
      return [] if upper <= 0 || lower <= 0
      upper_row[i] = 1
      lower_row[i] = 1
      upper -= 1
      lower -= 1
    end
  end

  colsum.each_with_index do |c, i|
    next unless c == 1
    if upper > 0
      upper_row[i] = 1
      lower_row[i] = 0
      upper -= 1
    elsif lower > 0
      upper_row[i] = 0
      lower_row[i] = 1
      lower -= 1
    else
      return []
    end
  end

  (upper == 0 && lower == 0) ? [upper_row, lower_row] : []
end
```

## Scala

```scala
object Solution {
    def reconstructMatrix(upper: Int, lower: Int, colsum: Array[Int]): List[List[Int]] = {
        val n = colsum.length
        val top = Array.fill(n)(0)
        val bottom = Array.fill(n)(0)
        var up = upper
        var low = lower

        // Handle columns with sum 2
        for (i <- 0 until n) {
            if (colsum(i) == 2) {
                top(i) = 1
                bottom(i) = 1
                up -= 1
                low -= 1
            }
        }

        if (up < 0 || low < 0) return List()

        // Handle columns with sum 1
        for (i <- 0 until n) {
            if (colsum(i) == 1) {
                if (up > 0) {
                    top(i) = 1
                    up -= 1
                } else {
                    bottom(i) = 1
                    low -= 1
                }
            }
        }

        if (up == 0 && low == 0) List(top.toList, bottom.toList) else List()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reconstruct_matrix(upper: i32, lower: i32, colsum: Vec<i32>) -> Vec<Vec<i32>> {
        let n = colsum.len();
        let mut top = vec![0i32; n];
        let mut bottom = vec![0i32; n];
        let mut up = upper;
        let mut low = lower;

        // Handle columns with sum 2
        for (i, &c) in colsum.iter().enumerate() {
            if c == 2 {
                top[i] = 1;
                bottom[i] = 1;
                up -= 1;
                low -= 1;
            }
        }

        if up < 0 || low < 0 {
            return vec![];
        }

        // Handle columns with sum 1
        for (i, &c) in colsum.iter().enumerate() {
            if c == 1 {
                if up > 0 {
                    top[i] = 1;
                    up -= 1;
                } else {
                    bottom[i] = 1;
                    low -= 1;
                }
            }
        }

        if up == 0 && low == 0 {
            vec![top, bottom]
        } else {
            vec![]
        }
    }
}
```

## Racket

```racket
(define/contract (reconstruct-matrix upper lower colsum)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((n (length colsum))
         (row0 (make-vector n 0))
         (row1 (make-vector n 0)))
    (let loop ((i 0) (up upper) (low lower) (cs colsum))
      (if (null? cs)
          (if (and (= up 0) (= low 0))
              (list (vector->list row0) (vector->list row1))
              '())
          (let ((c (car cs)))
            (cond
              [(= c 2)
               (vector-set! row0 i 1)
               (vector-set! row1 i 1)
               (loop (+ i 1) (- up 1) (- low 1) (cdr cs))]
              [(= c 0)
               (vector-set! row0 i 0)
               (vector-set! row1 i 0)
               (loop (+ i 1) up low (cdr cs))]
              [else ; c == 1
               (if (> up 0)
                   (begin
                     (vector-set! row0 i 1)
                     (vector-set! row1 i 0)
                     (loop (+ i 1) (- up 1) low (cdr cs)))
                   (if (> low 0)
                       (begin
                         (vector-set! row0 i 0)
                         (vector-set! row1 i 1)
                         (loop (+ i 1) up (- low 1) (cdr cs)))
                       (loop (+ i 1) -1 -1 (cdr cs))))]))))))
```

## Erlang

```erlang
-spec reconstruct_matrix(Upper :: integer(), Lower :: integer(), Colsum :: [integer()]) -> [[integer()]].
reconstruct_matrix(Upper, Lower, Colsum) ->
    case process(Colsum, Upper, Lower, [], []) of
        {ok, URev, LRev} ->
            UpperRow = lists:reverse(URev),
            LowerRow = lists:reverse(LRev),
            [UpperRow, LowerRow];
        error -> []
    end.

process([], 0, 0, UAcc, LAcc) ->
    {ok, UAcc, LAcc};
process([], _, _, _UAcc, _LAcc) ->
    error;
process([C|Rest], Upper, Lower, UAcc, LAcc) when C =:= 2 ->
    if Upper > 0 andalso Lower > 0 ->
            process(Rest, Upper-1, Lower-1, [1|UAcc], [1|LAcc]);
       true -> error
    end;
process([C|Rest], Upper, Lower, UAcc, LAcc) when C =:= 0 ->
    process(Rest, Upper, Lower, [0|UAcc], [0|LAcc]);
process([C|Rest], Upper, Lower, UAcc, LAcc) when C =:= 1 ->
    if Upper > 0 ->
            process(Rest, Upper-1, Lower, [1|UAcc], [0|LAcc]);
       true ->
            if Lower > 0 ->
                    process(Rest, Upper, Lower-1, [0|UAcc], [1|LAcc]);
               true -> error
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reconstruct_matrix(upper :: integer, lower :: integer, colsum :: [integer]) :: [[integer]]
  def reconstruct_matrix(upper, lower, colsum) do
    {row0_rev, row1_rev, up_rem, low_rem} =
      Enum.reduce(colsum, {[], [], upper, lower}, fn val, {r0, r1, up, lo} ->
        case val do
          2 ->
            {[1 | r0], [1 | r1], up - 1, lo - 1}

          0 ->
            {[0 | r0], [0 | r1], up, lo}

          1 ->
            if up > 0 do
              {[1 | r0], [0 | r1], up - 1, lo}
            else
              {[0 | r0], [1 | r1], up, lo - 1}
            end
        end
      end)

    if up_rem == 0 and low_rem == 0 do
      [Enum.reverse(row0_rev), Enum.reverse(row1_rev)]
    else
      []
    end
  end
end
```
