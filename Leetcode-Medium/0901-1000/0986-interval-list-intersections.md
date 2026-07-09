# 0986. Interval List Intersections

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> res;
        int i = 0, j = 0;
        while (i < (int)firstList.size() && j < (int)secondList.size()) {
            int start = max(firstList[i][0], secondList[j][0]);
            int end = min(firstList[i][1], secondList[j][1]);
            if (start <= end) {
                res.push_back({start, end});
            }
            if (firstList[i][1] < secondList[j][1]) {
                ++i;
            } else {
                ++j;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0, j = 0;
        java.util.List<int[]> res = new java.util.ArrayList<>();
        while (i < firstList.length && j < secondList.length) {
            int start1 = firstList[i][0], end1 = firstList[i][1];
            int start2 = secondList[j][0], end2 = secondList[j][1];
            int lo = Math.max(start1, start2);
            int hi = Math.min(end1, end2);
            if (lo <= hi) {
                res.add(new int[]{lo, hi});
            }
            // Move the pointer with the smaller endpoint
            if (end1 < end2) {
                i++;
            } else {
                j++;
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}
```

## Python

```python
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Find overlap, if any
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start <= end:
                res.append([start, end])

            # Move the pointer with the smaller endpoint
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        intersections: List[List[int]] = []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                intersections.append([start, end])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return intersections
```

## C

```c
#include <stdlib.h>

static inline int max(int a, int b) { return a > b ? a : b; }
static inline int min(int a, int b) { return a < b ? a : b; }

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** intervalIntersection(int** firstList, int firstListSize, int* firstListColSize,
                           int** secondList, int secondListSize, int* secondListColSize,
                           int* returnSize, int** returnColumnSizes) {
    int maxPossible = firstListSize + secondListSize;
    int** result = (int**)malloc(sizeof(int*) * maxPossible);
    int* colSizes = (int*)malloc(sizeof(int) * maxPossible);
    
    int i = 0, j = 0, k = 0;
    while (i < firstListSize && j < secondListSize) {
        int start1 = firstList[i][0];
        int end1   = firstList[i][1];
        int start2 = secondList[j][0];
        int end2   = secondList[j][1];
        
        int interStart = max(start1, start2);
        int interEnd   = min(end1, end2);
        if (interStart <= interEnd) {
            int* interval = (int*)malloc(2 * sizeof(int));
            interval[0] = interStart;
            interval[1] = interEnd;
            result[k] = interval;
            colSizes[k] = 2;
            ++k;
        }
        
        if (end1 < end2) {
            ++i;
        } else {
            ++j;
        }
    }
    
    *returnSize = k;
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] IntervalIntersection(int[][] firstList, int[][] secondList) {
        var result = new List<int[]>();
        int i = 0, j = 0;
        while (i < firstList.Length && j < secondList.Length) {
            int start = Math.Max(firstList[i][0], secondList[j][0]);
            int end = Math.Min(firstList[i][1], secondList[j][1]);
            if (start <= end) {
                result.Add(new int[] { start, end });
            }
            if (firstList[i][1] < secondList[j][1]) {
                i++;
            } else {
                j++;
            }
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function(firstList, secondList) {
    const res = [];
    let i = 0, j = 0;
    while (i < firstList.length && j < secondList.length) {
        const [aStart, aEnd] = firstList[i];
        const [bStart, bEnd] = secondList[j];
        
        // Find overlap
        const start = Math.max(aStart, bStart);
        const end = Math.min(aEnd, bEnd);
        if (start <= end) {
            res.push([start, end]);
        }
        
        // Move the pointer with the smaller endpoint
        if (aEnd < bEnd) {
            i++;
        } else {
            j++;
        }
    }
    return res;
};
```

## Typescript

```typescript
function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {
    const result: number[][] = [];
    let i = 0, j = 0;
    while (i < firstList.length && j < secondList.length) {
        const [aStart, aEnd] = firstList[i];
        const [bStart, bEnd] = secondList[j];
        const start = Math.max(aStart, bStart);
        const end = Math.min(aEnd, bEnd);
        if (start <= end) {
            result.push([start, end]);
        }
        if (aEnd < bEnd) {
            i++;
        } else {
            j++;
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $firstList
     * @param Integer[][] $secondList
     * @return Integer[][]
     */
    function intervalIntersection($firstList, $secondList) {
        $i = 0;
        $j = 0;
        $res = [];
        $n = count($firstList);
        $m = count($secondList);
        while ($i < $n && $j < $m) {
            $aStart = $firstList[$i][0];
            $aEnd   = $firstList[$i][1];
            $bStart = $secondList[$j][0];
            $bEnd   = $secondList[$j][1];

            $start = max($aStart, $bStart);
            $end   = min($aEnd, $bEnd);
            if ($start <= $end) {
                $res[] = [$start, $end];
            }

            if ($aEnd < $bEnd) {
                $i++;
            } else {
                $j++;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func intervalIntersection(_ firstList: [[Int]], _ secondList: [[Int]]) -> [[Int]] {
        var i = 0
        var j = 0
        var result: [[Int]] = []
        
        while i < firstList.count && j < secondList.count {
            let aStart = firstList[i][0]
            let aEnd = firstList[i][1]
            let bStart = secondList[j][0]
            let bEnd = secondList[j][1]
            
            let startMax = max(aStart, bStart)
            let endMin = min(aEnd, bEnd)
            
            if startMax <= endMin {
                result.append([startMax, endMin])
            }
            
            if aEnd < bEnd {
                i += 1
            } else {
                j += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun intervalIntersection(firstList: Array<IntArray>, secondList: Array<IntArray>): Array<IntArray> {
        val result = mutableListOf<IntArray>()
        var i = 0
        var j = 0
        while (i < firstList.size && j < secondList.size) {
            val aStart = firstList[i][0]
            val aEnd = firstList[i][1]
            val bStart = secondList[j][0]
            val bEnd = secondList[j][1]

            val start = maxOf(aStart, bStart)
            val end = minOf(aEnd, bEnd)

            if (start <= end) {
                result.add(intArrayOf(start, end))
            }

            if (aEnd < bEnd) {
                i++
            } else {
                j++
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> intervalIntersection(List<List<int>> firstList, List<List<int>> secondList) {
    int i = 0, j = 0;
    List<List<int>> result = [];
    while (i < firstList.length && j < secondList.length) {
      int start1 = firstList[i][0];
      int end1 = firstList[i][1];
      int start2 = secondList[j][0];
      int end2 = secondList[j][1];

      int lo = start1 > start2 ? start1 : start2;
      int hi = end1 < end2 ? end1 : end2;

      if (lo <= hi) {
        result.add([lo, hi]);
      }

      if (end1 < end2) {
        i++;
      } else {
        j++;
      }
    }
    return result;
  }
}
```

## Golang

```go
func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
    i, j := 0, 0
    res := make([][]int, 0)
    for i < len(firstList) && j < len(secondList) {
        aStart, aEnd := firstList[i][0], firstList[i][1]
        bStart, bEnd := secondList[j][0], secondList[j][1]

        // Find overlap
        start := aStart
        if bStart > start {
            start = bStart
        }
        end := aEnd
        if bEnd < end {
            end = bEnd
        }

        if start <= end {
            res = append(res, []int{start, end})
        }

        // Move the pointer with the smaller endpoint
        if aEnd < bEnd {
            i++
        } else {
            j++
        }
    }
    return res
}
```

## Ruby

```ruby
def interval_intersection(first_list, second_list)
  i = 0
  j = 0
  result = []

  while i < first_list.length && j < second_list.length
    a_start, a_end = first_list[i]
    b_start, b_end = second_list[j]

    start_max = [a_start, b_start].max
    end_min   = [a_end, b_end].min

    result << [start_max, end_min] if start_max <= end_min

    if a_end < b_end
      i += 1
    else
      j += 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def intervalIntersection(firstList: Array[Array[Int]], secondList: Array[Array[Int]]): Array[Array[Int]] = {
    val res = scala.collection.mutable.ListBuffer.empty[Array[Int]]
    var i = 0
    var j = 0
    while (i < firstList.length && j < secondList.length) {
      val start1 = firstList(i)(0)
      val end1   = firstList(i)(1)
      val start2 = secondList(j)(0)
      val end2   = secondList(j)(1)

      val lo = math.max(start1, start2)
      val hi = math.min(end1, end2)
      if (lo <= hi) {
        res += Array(lo, hi)
      }

      if (end1 < end2) i += 1 else j += 1
    }
    res.toArray
  }
}
```

## Rust

```rust
impl Solution {
    pub fn interval_intersection(first_list: Vec<Vec<i32>>, second_list: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i = 0;
        let mut j = 0;
        let mut result: Vec<Vec<i32>> = Vec::new();
        while i < first_list.len() && j < second_list.len() {
            let a_start = first_list[i][0];
            let a_end = first_list[i][1];
            let b_start = second_list[j][0];
            let b_end = second_list[j][1];

            let start = std::cmp::max(a_start, b_start);
            let end = std::cmp::min(a_end, b_end);

            if start <= end {
                result.push(vec![start, end]);
            }

            if a_end < b_end {
                i += 1;
            } else {
                j += 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (interval-intersection firstList secondList)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let loop ((i firstList) (j secondList) (acc '()))
    (cond
      [(or (null? i) (null? j)) (reverse acc)]
      [else
       (define a (car i))
       (define b (car j))
       (define start (max (first a) (first b)))
       (define end   (min (second a) (second b)))
       (define new-acc (if (<= start end)
                           (cons (list start end) acc)
                           acc))
       (cond
         [(< (second a) (second b)) (loop (cdr i) j new-acc)]
         [(> (second a) (second b)) (loop i (cdr j) new-acc)]
         [else (loop (cdr i) (cdr j) new-acc)])])))
```

## Erlang

```erlang
-module(solution).
-export([interval_intersection/2]).

-spec interval_intersection(FirstList :: [[integer()]], SecondList :: [[integer()]]) -> [[integer()]].
interval_intersection(FirstList, SecondList) ->
    loop(FirstList, SecondList, []).

loop([], _, Acc) -> lists:reverse(Acc);
loop(_, [], Acc) -> lists:reverse(Acc);
loop([[AStart, AEnd] | Rest1] = L1, [[BStart, BEnd] | Rest2] = L2, Acc) ->
    Start = erlang:max(AStart, BStart),
    End   = erlang:min(AEnd, BEnd),
    NewAcc = if
        Start =< End -> [[Start, End] | Acc];
        true        -> Acc
    end,
    if
        AEnd < BEnd -> loop(Rest1, L2, NewAcc);
        BEnd < AEnd -> loop(L1, Rest2, NewAcc);
        true       -> loop(Rest1, Rest2, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec interval_intersection(first_list :: [[integer]], second_list :: [[integer]]) :: [[integer]]
  def interval_intersection(first_list, second_list) do
    intersect(first_list, second_list, [])
    |> Enum.reverse()
  end

  defp intersect([], _, acc), do: acc
  defp intersect(_, [], acc), do: acc

  defp intersect([[a_start, a_end] | as], [[b_start, b_end] | bs], acc) do
    s = max(a_start, b_start)
    e = min(a_end, b_end)

    new_acc =
      if s <= e do
        [[s, e] | acc]
      else
        acc
      end

    cond do
      a_end < b_end ->
        intersect(as, [[b_start, b_end] | bs], new_acc)

      b_end < a_end ->
        intersect([[a_start, a_end] | as], bs, new_acc)

      true ->
        intersect(as, bs, new_acc)
    end
  end
end
```
