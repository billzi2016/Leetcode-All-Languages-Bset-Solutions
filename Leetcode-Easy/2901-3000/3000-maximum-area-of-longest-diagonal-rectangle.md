# 3000. Maximum Area of Longest Diagonal Rectangle

## Cpp

```cpp
class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        long long maxDiagSq = -1;
        int maxArea = 0;
        for (const auto& dim : dimensions) {
            int l = dim[0];
            int w = dim[1];
            long long diagSq = 1LL * l * l + 1LL * w * w;
            int area = l * w;
            if (diagSq > maxDiagSq) {
                maxDiagSq = diagSq;
                maxArea = area;
            } else if (diagSq == maxDiagSq && area > maxArea) {
                maxArea = area;
            }
        }
        return maxArea;
    }
};
```

## Java

```java
class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxDiagSq = -1;
        int maxArea = 0;
        for (int[] dim : dimensions) {
            int l = dim[0];
            int w = dim[1];
            int diagSq = l * l + w * w;
            int area = l * w;
            if (diagSq > maxDiagSq) {
                maxDiagSq = diagSq;
                maxArea = area;
            } else if (diagSq == maxDiagSq && area > maxArea) {
                maxArea = area;
            }
        }
        return maxArea;
    }
}
```

## Python

```python
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag = -1
        max_area = 0
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            elif diag_sq == max_diag and area > max_area:
                max_area = area
        return max_area
```

## Python3

```python
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = -1
        max_area = 0
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            elif diag_sq == max_diag and area > max_area:
                max_area = area
        return max_area
```

## C

```c
int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    long long maxDiagSq = -1;
    int bestArea = 0;
    for (int i = 0; i < dimensionsSize; ++i) {
        int length = dimensions[i][0];
        int width = dimensions[i][1];
        long long diagSq = (long long)length * length + (long long)width * width;
        int area = length * width;
        if (diagSq > maxDiagSq) {
            maxDiagSq = diagSq;
            bestArea = area;
        } else if (diagSq == maxDiagSq && area > bestArea) {
            bestArea = area;
        }
    }
    return bestArea;
}
```

## Csharp

```csharp
public class Solution {
    public int AreaOfMaxDiagonal(int[][] dimensions) {
        int maxDiagSq = -1;
        int maxArea = 0;
        foreach (var dim in dimensions) {
            int length = dim[0];
            int width = dim[1];
            int diagSq = length * length + width * width;
            int area = length * width;
            if (diagSq > maxDiagSq) {
                maxDiagSq = diagSq;
                maxArea = area;
            } else if (diagSq == maxDiagSq && area > maxArea) {
                maxArea = area;
            }
        }
        return maxArea;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
    let maxDiagSq = -1;
    let maxArea = 0;
    for (const [len, wid] of dimensions) {
        const diagSq = len * len + wid * wid;
        const area = len * wid;
        if (diagSq > maxDiagSq) {
            maxDiagSq = diagSq;
            maxArea = area;
        } else if (diagSq === maxDiagSq && area > maxArea) {
            maxArea = area;
        }
    }
    return maxArea;
};
```

## Typescript

```typescript
function areaOfMaxDiagonal(dimensions: number[][]): number {
    let maxDiagSq = -1;
    let maxArea = 0;
    for (const [len, wid] of dimensions) {
        const diagSq = len * len + wid * wid;
        const area = len * wid;
        if (diagSq > maxDiagSq) {
            maxDiagSq = diagSq;
            maxArea = area;
        } else if (diagSq === maxDiagSq && area > maxArea) {
            maxArea = area;
        }
    }
    return maxArea;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $dimensions
     * @return Integer
     */
    function areaOfMaxDiagonal($dimensions) {
        $maxDiag = -1;
        $maxArea = 0;
        foreach ($dimensions as $dim) {
            $l = $dim[0];
            $w = $dim[1];
            $diagSq = $l * $l + $w * $w;
            $area = $l * $w;
            if ($diagSq > $maxDiag) {
                $maxDiag = $diagSq;
                $maxArea = $area;
            } elseif ($diagSq == $maxDiag && $area > $maxArea) {
                $maxArea = $area;
            }
        }
        return $maxArea;
    }
}
```

## Swift

```swift
class Solution {
    func areaOfMaxDiagonal(_ dimensions: [[Int]]) -> Int {
        var maxDiag = -1
        var maxArea = 0
        for dim in dimensions {
            let length = dim[0]
            let width = dim[1]
            let diagSq = length * length + width * width
            let area = length * width
            if diagSq > maxDiag {
                maxDiag = diagSq
                maxArea = area
            } else if diagSq == maxDiag && area > maxArea {
                maxArea = area
            }
        }
        return maxArea
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areaOfMaxDiagonal(dimensions: Array<IntArray>): Int {
        var maxDiag = -1L
        var maxArea = 0
        for (dim in dimensions) {
            val l = dim[0]
            val w = dim[1]
            val diag = l.toLong() * l + w.toLong() * w
            val area = l * w
            if (diag > maxDiag) {
                maxDiag = diag
                maxArea = area
            } else if (diag == maxDiag && area > maxArea) {
                maxArea = area
            }
        }
        return maxArea
    }
}
```

## Dart

```dart
class Solution {
  int areaOfMaxDiagonal(List<List<int>> dimensions) {
    int maxDiagSq = -1;
    int maxArea = 0;
    for (var dim in dimensions) {
      int length = dim[0];
      int width = dim[1];
      int diagSq = length * length + width * width;
      int area = length * width;
      if (diagSq > maxDiagSq) {
        maxDiagSq = diagSq;
        maxArea = area;
      } else if (diagSq == maxDiagSq && area > maxArea) {
        maxArea = area;
      }
    }
    return maxArea;
  }
}
```

## Golang

```go
func areaOfMaxDiagonal(dimensions [][]int) int {
	maxDiag := -1
	maxArea := 0
	for _, d := range dimensions {
		l, w := d[0], d[1]
		diagSq := l*l + w*w
		area := l * w
		if diagSq > maxDiag || (diagSq == maxDiag && area > maxArea) {
			maxDiag = diagSq
			maxArea = area
		}
	}
	return maxArea
}
```

## Ruby

```ruby
def area_of_max_diagonal(dimensions)
  max_diag = -1
  max_area = 0
  dimensions.each do |len, wid|
    diag_sq = len * len + wid * wid
    area = len * wid
    if diag_sq > max_diag || (diag_sq == max_diag && area > max_area)
      max_diag = diag_sq
      max_area = area
    end
  end
  max_area
end
```

## Scala

```scala
object Solution {
    def areaOfMaxDiagonal(dimensions: Array[Array[Int]]): Int = {
        var maxDiagSq: Long = -1L
        var maxArea: Int = 0
        for (dim <- dimensions) {
            val l = dim(0).toLong
            val w = dim(1).toLong
            val diagSq = l * l + w * w
            val area = (l * w).toInt
            if (diagSq > maxDiagSq) {
                maxDiagSq = diagSq
                maxArea = area
            } else if (diagSq == maxDiagSq && area > maxArea) {
                maxArea = area
            }
        }
        maxArea
    }
}
```

## Rust

```rust
impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        let mut best_diag: i64 = -1;
        let mut best_area: i32 = 0;
        for dim in dimensions.iter() {
            let l = dim[0] as i64;
            let w = dim[1] as i64;
            let diag_sq = l * l + w * w;
            let area = (l * w) as i32;
            if diag_sq > best_diag {
                best_diag = diag_sq;
                best_area = area;
            } else if diag_sq == best_diag && area > best_area {
                best_area = area;
            }
        }
        best_area
    }
}
```

## Racket

```racket
(define/contract (area-of-max-diagonal dimensions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let loop ((lst dimensions) (best-diag -1) (best-area 0))
    (if (null? lst)
        best-area
        (let* ((pair (car lst))
               (l (first pair))
               (w (second pair))
               (diag (+ (* l l) (* w w)))
               (area (* l w)))
          (cond [(> diag best-diag) (loop (cdr lst) diag area)]
                [(and (= diag best-diag) (> area best-area)) (loop (cdr lst) best-diag area)]
                [else (loop (cdr lst) best-diag best-area)])))))
```

## Erlang

```erlang
-spec area_of_max_diagonal(Dimensions :: [[integer()]]) -> integer().
area_of_max_diagonal(Dimensions) ->
    {_, MaxArea} = lists:foldl(
        fun([L, W], {MaxD, MaxA}) ->
            D = L * L + W * W,
            A = L * W,
            case D > MaxD of
                true -> {D, A};
                false ->
                    case D == MaxD andalso A > MaxA of
                        true -> {MaxD, A};
                        false -> {MaxD, MaxA}
                    end
            end
        end,
        {0, 0},
        Dimensions),
    MaxArea.
```

## Elixir

```elixir
defmodule Solution do
  @spec area_of_max_diagonal(dimensions :: [[integer]]) :: integer
  def area_of_max_diagonal(dimensions) do
    {_, max_area} =
      Enum.reduce(dimensions, {0, 0}, fn [l, w], {max_diag_sq, max_area} ->
        diag_sq = l * l + w * w
        area = l * w

        cond do
          diag_sq > max_diag_sq -> {diag_sq, area}
          diag_sq == max_diag_sq and area > max_area -> {max_diag_sq, area}
          true -> {max_diag_sq, max_area}
        end
      end)

    max_area
  end
end
```
