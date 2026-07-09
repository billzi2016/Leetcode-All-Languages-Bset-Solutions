# 2672. Number of Adjacent Elements With the Same Color

## Cpp

```cpp
class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        vector<int> colors(n, 0);
        vector<int> answer;
        answer.reserve(queries.size());
        int same = 0;
        for (const auto& q : queries) {
            int idx = q[0];
            int col = q[1];
            // Remove contributions of the old color at idx
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx - 1] == colors[idx]) --same;
                if (idx + 1 < n && colors[idx + 1] == colors[idx]) --same;
            }
            // Apply new color
            colors[idx] = col;
            // Add contributions of the new color at idx
            if (idx > 0 && colors[idx - 1] == col) ++same;
            if (idx + 1 < n && colors[idx + 1] == col) ++same;
            answer.push_back(same);
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] colorTheArray(int n, int[][] queries) {
        int[] colors = new int[n];
        int[] result = new int[queries.length];
        int sameCount = 0;
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][0];
            int col = queries[i][1];

            // Remove contributions of the old color at idx
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx - 1] == colors[idx]) sameCount--;
                if (idx < n - 1 && colors[idx + 1] == colors[idx]) sameCount--;
            }

            // Apply new color
            colors[idx] = col;

            // Add contributions of the new color at idx
            if (idx > 0 && colors[idx - 1] == col) sameCount++;
            if (idx < n - 1 && colors[idx + 1] == col) sameCount++;

            result[i] = sameCount;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        colors = [0] * n
        same_adjacent = 0
        res = []
        for idx, col in queries:
            old = colors[idx]
            if old != 0:
                if idx > 0 and colors[idx - 1] == old:
                    same_adjacent -= 1
                if idx < n - 1 and colors[idx + 1] == old:
                    same_adjacent -= 1
            colors[idx] = col
            if col != 0:
                if idx > 0 and colors[idx - 1] == col:
                    same_adjacent += 1
                if idx < n - 1 and colors[idx + 1] == col:
                    same_adjacent += 1
            res.append(same_adjacent)
        return res
```

## Python3

```python
class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        colors = [0] * n
        ans = 0
        res = []
        for idx, col in queries:
            # Remove contributions of the old color at idx
            old = colors[idx]
            if old != 0:
                if idx > 0 and colors[idx - 1] == old:
                    ans -= 1
                if idx + 1 < n and colors[idx + 1] == old:
                    ans -= 1
            # Apply new color
            colors[idx] = col
            # Add contributions of the new color at idx
            if col != 0:
                if idx > 0 and colors[idx - 1] == col:
                    ans += 1
                if idx + 1 < n and colors[idx + 1] == col:
                    ans += 1
            res.append(ans)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* colorTheArray(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int *colors = (int*)calloc(n, sizeof(int));
    int *result = (int*)malloc(queriesSize * sizeof(int));
    int sameCount = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int idx = queries[i][0];
        int col = queries[i][1];

        if (colors[idx] != 0) {
            if (idx > 0 && colors[idx - 1] == colors[idx]) sameCount--;
            if (idx + 1 < n && colors[idx + 1] == colors[idx]) sameCount--;
        }

        colors[idx] = col;

        if (col != 0) {
            if (idx > 0 && colors[idx - 1] == col) sameCount++;
            if (idx + 1 < n && colors[idx + 1] == col) sameCount++;
        }

        result[i] = sameCount;
    }

    free(colors);
    *returnSize = queriesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ColorTheArray(int n, int[][] queries) {
        int[] colors = new int[n];
        int ans = 0;
        int m = queries.Length;
        int[] result = new int[m];
        for (int i = 0; i < m; i++) {
            int idx = queries[i][0];
            int col = queries[i][1];
            int old = colors[idx];
            if (old != 0) {
                if (idx > 0 && colors[idx - 1] == old) ans--;
                if (idx < n - 1 && colors[idx + 1] == old) ans--;
            }
            colors[idx] = col;
            if (col != 0) {
                if (idx > 0 && colors[idx - 1] == col) ans++;
                if (idx < n - 1 && colors[idx + 1] == col) ans++;
            }
            result[i] = ans;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var colorTheArray = function(n, queries) {
    const colors = new Array(n).fill(0);
    let sameCount = 0;
    const result = [];
    
    for (const [idx, col] of queries) {
        // Remove contributions from the old color
        if (colors[idx] !== 0) {
            if (idx > 0 && colors[idx - 1] === colors[idx]) sameCount--;
            if (idx < n - 1 && colors[idx + 1] === colors[idx]) sameCount--;
        }
        
        // Apply new color
        colors[idx] = col;
        
        // Add contributions from the new color
        if (col !== 0) {
            if (idx > 0 && colors[idx - 1] === col) sameCount++;
            if (idx < n - 1 && colors[idx + 1] === col) sameCount++;
        }
        
        result.push(sameCount);
    }
    
    return result;
};
```

## Typescript

```typescript
function colorTheArray(n: number, queries: number[][]): number[] {
    const colors = new Array<number>(n).fill(0);
    let same = 0;
    const result: number[] = [];

    for (const [idx, col] of queries) {
        const old = colors[idx];

        if (old !== 0) {
            if (idx > 0 && colors[idx - 1] === old) same--;
            if (idx < n - 1 && colors[idx + 1] === old) same--;
        }

        colors[idx] = col;

        if (col !== 0) {
            if (idx > 0 && colors[idx - 1] === col) same++;
            if (idx < n - 1 && colors[idx + 1] === col) same++;
        }

        result.push(same);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function colorTheArray($n, $queries) {
        $colors = array_fill(0, $n, 0);
        $ans = [];
        $cur = 0;
        foreach ($queries as $q) {
            [$idx, $col] = $q;
            $old = $colors[$idx];
            if ($old != 0) {
                if ($idx > 0 && $colors[$idx - 1] == $old) {
                    $cur--;
                }
                if ($idx < $n - 1 && $colors[$idx + 1] == $old) {
                    $cur--;
                }
            }
            $colors[$idx] = $col;
            if ($col != 0) {
                if ($idx > 0 && $colors[$idx - 1] == $col) {
                    $cur++;
                }
                if ($idx < $n - 1 && $colors[$idx + 1] == $col) {
                    $cur++;
                }
            }
            $ans[] = $cur;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func colorTheArray(_ n: Int, _ queries: [[Int]]) -> [Int] {
        var colors = Array(repeating: 0, count: n)
        var sameCount = 0
        var result = [Int]()
        result.reserveCapacity(queries.count)
        
        for q in queries {
            let idx = q[0]
            let newColor = q[1]
            
            // Remove contributions of the old color
            let oldColor = colors[idx]
            if oldColor != 0 {
                if idx > 0 && colors[idx - 1] == oldColor {
                    sameCount -= 1
                }
                if idx < n - 1 && colors[idx + 1] == oldColor {
                    sameCount -= 1
                }
            }
            
            // Apply new color
            colors[idx] = newColor
            
            // Add contributions of the new color
            if newColor != 0 {
                if idx > 0 && colors[idx - 1] == newColor {
                    sameCount += 1
                }
                if idx < n - 1 && colors[idx + 1] == newColor {
                    sameCount += 1
                }
            }
            
            result.append(sameCount)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun colorTheArray(n: Int, queries: Array<IntArray>): IntArray {
        val colors = IntArray(n)
        var sameCount = 0
        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val idx = queries[i][0]
            val newColor = queries[i][1]

            // Check left neighbor
            if (idx > 0) {
                if (colors[idx] != 0 && colors[idx] == colors[idx - 1]) sameCount--
                if (newColor != 0 && newColor == colors[idx - 1]) sameCount++
            }
            // Check right neighbor
            if (idx < n - 1) {
                if (colors[idx] != 0 && colors[idx] == colors[idx + 1]) sameCount--
                if (newColor != 0 && newColor == colors[idx + 1]) sameCount++
            }

            colors[idx] = newColor
            result[i] = sameCount
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> colorTheArray(int n, List<List<int>> queries) {
    List<int> colors = List.filled(n, 0);
    int count = 0;
    List<int> result = [];
    for (var query in queries) {
      int idx = query[0];
      int newColor = query[1];
      int oldColor = colors[idx];

      if (oldColor != 0) {
        if (idx > 0 && colors[idx - 1] == oldColor) count--;
        if (idx < n - 1 && colors[idx + 1] == oldColor) count--;
      }

      colors[idx] = newColor;

      if (newColor != 0) {
        if (idx > 0 && colors[idx - 1] == newColor) count++;
        if (idx < n - 1 && colors[idx + 1] == newColor) count++;
      }

      result.add(count);
    }
    return result;
  }
}
```

## Golang

```go
func colorTheArray(n int, queries [][]int) []int {
	colors := make([]int, n)
	ans := 0
	result := make([]int, len(queries))

	for i, q := range queries {
		idx, col := q[0], q[1]

		if idx > 0 && colors[idx] != 0 && colors[idx] == colors[idx-1] {
			ans--
		}
		if idx+1 < n && colors[idx] != 0 && colors[idx] == colors[idx+1] {
			ans--
		}

		colors[idx] = col

		if idx > 0 && colors[idx] != 0 && colors[idx] == colors[idx-1] {
			ans++
		}
		if idx+1 < n && colors[idx] != 0 && colors[idx] == colors[idx+1] {
			ans++
		}

		result[i] = ans
	}
	return result
}
```

## Ruby

```ruby
def color_the_array(n, queries)
  colors = Array.new(n, 0)
  cnt = 0
  result = []

  queries.each do |idx, col|
    old = colors[idx]

    if idx > 0 && old != 0 && colors[idx - 1] == old
      cnt -= 1
    end
    if idx < n - 1 && old != 0 && colors[idx + 1] == old
      cnt -= 1
    end

    colors[idx] = col

    if idx > 0 && colors[idx - 1] == col
      cnt += 1
    end
    if idx < n - 1 && colors[idx + 1] == col
      cnt += 1
    end

    result << cnt
  end

  result
end
```

## Scala

```scala
object Solution {
    def colorTheArray(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        val colors = Array.fill[Int](n)(0)
        var same = 0
        val result = new Array[Int](queries.length)

        for (i <- queries.indices) {
            val idx = queries(i)(0)
            val col = queries(i)(1)

            // Remove previous contributions
            if (idx > 0 && colors(idx) != 0 && colors(idx) == colors(idx - 1)) same -= 1
            if (idx < n - 1 && colors(idx) != 0 && colors(idx) == colors(idx + 1)) same -= 1

            // Apply new color
            colors(idx) = col

            // Add new contributions
            if (idx > 0 && colors(idx) != 0 && colors(idx) == colors(idx - 1)) same += 1
            if (idx < n - 1 && colors(idx) != 0 && colors(idx) == colors(idx + 1)) same += 1

            result(i) = same
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn color_the_array(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut colors = vec![0i32; n];
        let mut cur = 0i32;
        let mut res = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let idx = q[0] as usize;
            let new_color = q[1];

            if idx > 0 && colors[idx] == colors[idx - 1] {
                cur -= 1;
            }
            if idx + 1 < n && colors[idx] == colors[idx + 1] {
                cur -= 1;
            }

            colors[idx] = new_color;

            if idx > 0 && colors[idx] == colors[idx - 1] {
                cur += 1;
            }
            if idx + 1 < n && colors[idx] == colors[idx + 1] {
                cur += 1;
            }

            res.push(cur);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (color-the-array n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([arr (make-vector n 0)]
         [ans 0]
         [res '()])
    (for ([q queries])
      (define idx (first q))
      (define col (second q))
      (define old (vector-ref arr idx))
      ;; remove contributions of the old color
      (when (> idx 0)
        (when (= (vector-ref arr (- idx 1)) old)
          (set! ans (- ans 1))))
      (when (< idx (sub1 n))
        (when (= (vector-ref arr (+ idx 1)) old)
          (set! ans (- ans 1))))
      ;; recolor the element
      (vector-set! arr idx col)
      ;; add contributions of the new color
      (when (> idx 0)
        (when (= (vector-ref arr (- idx 1)) col)
          (set! ans (+ ans 1))))
      (when (< idx (sub1 n))
        (when (= (vector-ref arr (+ idx 1)) col)
          (set! ans (+ ans 1))))
      (set! res (cons ans res)))
    (reverse res)))
```

## Erlang

```erlang
-spec color_the_array(N :: integer(), Queries :: [[integer()]]) -> [integer()].
color_the_array(N, Queries) ->
    Arr0 = array:new(N, {default, 0}),
    process_queries(Queries, N, Arr0, 0, []).

process_queries([], _N, _Arr, _Count, Acc) ->
    lists:reverse(Acc);
process_queries([[Idx, Color]|Rest], N, Arr, Count, Acc) ->
    Old = array:get(Idx, Arr),
    Count1 =
        if Idx > 0 ->
                Left = array:get(Idx-1, Arr),
                C0 = case Old == Left of true -> Count - 1; false -> Count end,
                case Color == Left of true -> C0 + 1; false -> C0 end;
           true -> Count
        end,
    Count2 =
        if Idx < N-1 ->
                Right = array:get(Idx+1, Arr),
                C0 = case Old == Right of true -> Count1 - 1; false -> Count1 end,
                case Color == Right of true -> C0 + 1; false -> C0 end;
           true -> Count1
        end,
    NewArr = array:set(Idx, Color, Arr),
    process_queries(Rest, N, NewArr, Count2, [Count2|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec color_the_array(n :: integer, queries :: [[integer]]) :: [integer]
  def color_the_array(n, queries) do
    {_cnt, _colors, rev_res} =
      Enum.reduce(queries, {0, %{}, []}, fn [idx, col], {cnt, colors, acc} ->
        old = Map.get(colors, idx, 0)

        cnt =
          if idx > 0 and old != 0 and Map.get(colors, idx - 1, 0) == old do
            cnt - 1
          else
            cnt
          end

        cnt =
          if idx < n - 1 and old != 0 and Map.get(colors, idx + 1, 0) == old do
            cnt - 1
          else
            cnt
          end

        colors = Map.put(colors, idx, col)

        cnt =
          if idx > 0 and Map.get(colors, idx - 1, 0) == col do
            cnt + 1
          else
            cnt
          end

        cnt =
          if idx < n - 1 and Map.get(colors, idx + 1, 0) == col do
            cnt + 1
          else
            cnt
          end

        {cnt, colors, [cnt | acc]}
      end)

    Enum.reverse(rev_res)
  end
end
```
