# 1200. Minimum Absolute Difference

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int minDiff = INT_MAX;
        for (size_t i = 1; i < arr.size(); ++i) {
            minDiff = min(minDiff, arr[i] - arr[i-1]);
        }
        vector<vector<int>> result;
        for (size_t i = 1; i < arr.size(); ++i) {
            if (arr[i] - arr[i-1] == minDiff) {
                result.push_back({arr[i-1], arr[i]});
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<java.util.List<Integer>> minimumAbsDifference(int[] arr) {
        java.util.Arrays.sort(arr);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 1; i < arr.length; i++) {
            int diff = arr[i] - arr[i - 1];
            if (diff < minDiff) {
                minDiff = diff;
            }
        }
        java.util.List<java.util.List<Integer>> result = new java.util.ArrayList<>();
        for (int i = 1; i < arr.length; i++) {
            int diff = arr[i] - arr[i - 1];
            if (diff == minDiff) {
                java.util.List<Integer> pair = new java.util.ArrayList<>(2);
                pair.add(arr[i - 1]);
                pair.add(arr[i]);
                result.add(pair);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        return result
```

## Python3

```python
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result: List[List[int]] = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])
        return result
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int*** returnColumnSizes) {
    qsort(arr, (size_t)arrSize, sizeof(int), cmp_int);
    
    int minDiff = INT_MAX;
    for (int i = 0; i < arrSize - 1; ++i) {
        int diff = arr[i + 1] - arr[i];
        if (diff < minDiff) minDiff = diff;
    }
    
    int maxPairs = arrSize - 1;
    int **result = (int **)malloc(maxPairs * sizeof(int *));
    int *colSizes = (int *)malloc(maxPairs * sizeof(int));
    
    int count = 0;
    for (int i = 0; i < arrSize - 1; ++i) {
        int diff = arr[i + 1] - arr[i];
        if (diff == minDiff) {
            int *pair = (int *)malloc(2 * sizeof(int));
            pair[0] = arr[i];
            pair[1] = arr[i + 1];
            result[count] = pair;
            colSizes[count] = 2;
            ++count;
        }
    }
    
    *returnSize = count;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);
        var result = new List<IList<int>>();
        int minDiff = int.MaxValue;
        for (int i = 1; i < arr.Length; i++) {
            int diff = arr[i] - arr[i - 1];
            if (diff < minDiff) {
                minDiff = diff;
                result.Clear();
                result.Add(new List<int> { arr[i - 1], arr[i] });
            } else if (diff == minDiff) {
                result.Add(new List<int> { arr[i - 1], arr[i] });
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    arr.sort((a, b) => a - b);
    let minDiff = Infinity;
    for (let i = 1; i < arr.length; i++) {
        const diff = arr[i] - arr[i - 1];
        if (diff < minDiff) minDiff = diff;
    }
    const result = [];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] === minDiff) {
            result.push([arr[i - 1], arr[i]]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b);
    let minDiff = Number.MAX_SAFE_INTEGER;
    for (let i = 1; i < arr.length; i++) {
        const diff = arr[i] - arr[i - 1];
        if (diff < minDiff) minDiff = diff;
    }
    const result: number[][] = [];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] === minDiff) {
            result.push([arr[i - 1], arr[i]]);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[][]
     */
    function minimumAbsDifference($arr) {
        sort($arr, SORT_NUMERIC);
        $n = count($arr);
        $minDiff = PHP_INT_MAX;
        for ($i = 1; $i < $n; $i++) {
            $diff = $arr[$i] - $arr[$i - 1];
            if ($diff < $minDiff) {
                $minDiff = $diff;
            }
        }
        $result = [];
        for ($i = 1; $i < $n; $i++) {
            if ($arr[$i] - $arr[$i - 1] == $minDiff) {
                $result[] = [$arr[$i - 1], $arr[$i]];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minimumAbsDifference(_ arr: [Int]) -> [[Int]] {
        let sorted = arr.sorted()
        var minDiff = Int.max
        for i in 1..<sorted.count {
            let diff = sorted[i] - sorted[i - 1]
            if diff < minDiff {
                minDiff = diff
            }
        }
        var result: [[Int]] = []
        for i in 1..<sorted.count {
            if sorted[i] - sorted[i - 1] == minDiff {
                result.append([sorted[i - 1], sorted[i]])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumAbsDifference(arr: IntArray): List<List<Int>> {
        arr.sort()
        var minDiff = Int.MAX_VALUE
        for (i in 0 until arr.size - 1) {
            val diff = arr[i + 1] - arr[i]
            if (diff < minDiff) minDiff = diff
        }
        val result = mutableListOf<List<Int>>()
        for (i in 0 until arr.size - 1) {
            if (arr[i + 1] - arr[i] == minDiff) {
                result.add(listOf(arr[i], arr[i + 1]))
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> minimumAbsDifference(List<int> arr) {
    arr.sort();
    int minDiff = (arr[1] - arr[0]).abs();
    for (int i = 2; i < arr.length; i++) {
      int diff = (arr[i] - arr[i - 1]).abs();
      if (diff < minDiff) {
        minDiff = diff;
      }
    }
    List<List<int>> result = [];
    for (int i = 1; i < arr.length; i++) {
      if ((arr[i] - arr[i - 1]).abs() == minDiff) {
        result.add([arr[i - 1], arr[i]]);
      }
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func minimumAbsDifference(arr []int) [][]int {
    sort.Ints(arr)
    minDiff := int(^uint(0) >> 1)
    for i := 1; i < len(arr); i++ {
        diff := arr[i] - arr[i-1]
        if diff < minDiff {
            minDiff = diff
        }
    }
    res := make([][]int, 0)
    for i := 1; i < len(arr); i++ {
        if arr[i]-arr[i-1] == minDiff {
            res = append(res, []int{arr[i-1], arr[i]})
        }
    }
    return res
}
```

## Ruby

```ruby
def minimum_abs_difference(arr)
  arr.sort!
  min_diff = Float::INFINITY
  (1...arr.length).each do |i|
    diff = arr[i] - arr[i - 1]
    min_diff = diff if diff < min_diff
  end
  result = []
  (1...arr.length).each do |i|
    diff = arr[i] - arr[i - 1]
    result << [arr[i - 1], arr[i]] if diff == min_diff
  end
  result
end
```

## Scala

```scala
object Solution {
    def minimumAbsDifference(arr: Array[Int]): List[List[Int]] = {
        val sorted = arr.sorted
        var minDiff = Int.MaxValue
        for (i <- 1 until sorted.length) {
            val diff = sorted(i) - sorted(i - 1)
            if (diff < minDiff) minDiff = diff
        }
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        for (i <- 1 until sorted.length) {
            if (sorted(i) - sorted(i - 1) == minDiff) {
                result += List(sorted(i - 1), sorted(i))
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
        arr.sort_unstable();
        let mut min_diff = i32::MAX;
        for i in 1..arr.len() {
            let diff = arr[i] - arr[i - 1];
            if diff < min_diff {
                min_diff = diff;
            }
        }
        let mut result = Vec::new();
        for i in 1..arr.len() {
            if arr[i] - arr[i - 1] == min_diff {
                result.push(vec![arr[i - 1], arr[i]]);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (minimum-abs-difference arr)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((sorted (sort arr <))
         (n (length sorted)))
    (if (< n 2)
        '()
        (let ((mindiff
               (for/fold ([md (abs (- (list-ref sorted 1) (list-ref sorted 0)))])
                         ([i (in-range 2 n)])
                 (let* ((a (list-ref sorted (- i 1)))
                        (b (list-ref sorted i))
                        (d (abs (- b a))))
                   (if (< d md) d md)))))
          (for/list ([i (in-range 1 n)]
                     #:when (= (abs (- (list-ref sorted i)
                                       (list-ref sorted (- i 1)))) mindiff))
            (list (list-ref sorted (- i 1)) (list-ref sorted i)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_abs_difference/1]).

-spec minimum_abs_difference(Arr :: [integer()]) -> [[integer()]].
minimum_abs_difference(Arr) ->
    Sorted = lists:sort(Arr),
    MinDiff = find_min_diff(Sorted, 1000000000),
    collect_pairs(Sorted, MinDiff).

find_min_diff([_], Min) -> Min;
find_min_diff([A,B|Rest], Min) ->
    Diff = abs(B - A),
    NewMin = if Diff < Min -> Diff; true -> Min end,
    find_min_diff([B|Rest], NewMin).

collect_pairs([_], _Diff) -> [];
collect_pairs([A,B|Rest], Diff) ->
    case abs(B - A) of
        D when D =:= Diff -> [[A,B] | collect_pairs([B|Rest], Diff)];
        _ -> collect_pairs([B|Rest], Diff)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_abs_difference(arr :: [integer]) :: [[integer]]
  def minimum_abs_difference(arr) do
    sorted = Enum.sort(arr)
    len = length(sorted)

    pairs =
      for i <- 0..(len - 2) do
        a = Enum.at(sorted, i)
        b = Enum.at(sorted, i + 1)
        {b - a, [a, b]}
      end

    min_diff = pairs |> Enum.map(fn {d, _} -> d end) |> Enum.min()

    pairs
    |> Enum.filter(fn {d, _} -> d == min_diff end)
    |> Enum.map(fn {_, pair} -> pair end)
  end
end
```
