# 1385. Find the Distance Value Between Two Arrays

## Cpp

```cpp
class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int cnt = 0;
        for (int x : arr1) {
            auto it = lower_bound(arr2.begin(), arr2.end(), x - d);
            bool ok = true;
            if (it != arr2.end() && *it <= x + d) ok = false;
            if (ok) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int[] sorted = arr2.clone();
        java.util.Arrays.sort(sorted);
        int count = 0;
        for (int val : arr1) {
            int idx = java.util.Arrays.binarySearch(sorted, val);
            if (idx < 0) {
                idx = -idx - 1; // insertion point
            }
            boolean ok = true;
            if (idx < sorted.length && Math.abs((long)sorted[idx] - val) <= d) {
                ok = false;
            }
            if (idx - 1 >= 0 && Math.abs((long)sorted[idx - 1] - val) <= d) {
                ok = false;
            }
            if (ok) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        import bisect
        arr2.sort()
        count = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            ok = True
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                ok = False
            if idx > 0 and abs(arr2[idx-1] - x) <= d:
                ok = False
            if ok:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for a in arr1:
            i = bisect.bisect_left(arr2, a)
            ok = True
            if i < len(arr2) and abs(arr2[i] - a) <= d:
                ok = False
            if i > 0 and abs(arr2[i - 1] - a) <= d:
                ok = False
            if ok:
                cnt += 1
        return cnt
```

## C

```c
#include <stdlib.h>
#include <math.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size, int d) {
    if (arr2Size == 0) return arr1Size;
    qsort(arr2, arr2Size, sizeof(int), cmp_int);
    
    int count = 0;
    for (int i = 0; i < arr1Size; ++i) {
        int val = arr1[i];
        // lower_bound: first index with arr2[idx] >= val
        int left = 0, right = arr2Size;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr2[mid] < val)
                left = mid + 1;
            else
                right = mid;
        }
        int idx = left;
        int ok = 1;
        if (idx < arr2Size && abs(arr2[idx] - val) <= d) ok = 0;
        if (idx > 0 && abs(arr2[idx - 1] - val) <= d) ok = 0;
        if (ok) ++count;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindTheDistanceValue(int[] arr1, int[] arr2, int d)
    {
        Array.Sort(arr2);
        int count = 0;
        foreach (int x in arr1)
        {
            int idx = Array.BinarySearch(arr2, x);
            bool ok = true;
            if (idx >= 0)
            {
                // exact match -> distance <= d
                ok = false;
            }
            else
            {
                int insertPos = ~idx; // bitwise complement gives insertion point
                // check right neighbor
                if (insertPos < arr2.Length && Math.Abs(arr2[insertPos] - x) <= d)
                    ok = false;
                // check left neighbor
                if (insertPos > 0 && Math.Abs(arr2[insertPos - 1] - x) <= d)
                    ok = false;
            }
            if (ok) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    arr2.sort((a, b) => a - b);
    let result = 0;
    for (const x of arr1) {
        // lower bound binary search
        let left = 0, right = arr2.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr2[mid] < x) left = mid + 1;
            else right = mid;
        }
        let ok = true;
        if (left < arr2.length && Math.abs(arr2[left] - x) <= d) ok = false;
        if (left - 1 >= 0 && Math.abs(arr2[left - 1] - x) <= d) ok = false;
        if (ok) result++;
    }
    return result;
};
```

## Typescript

```typescript
function findTheDistanceValue(arr1: number[], arr2: number[], d: number): number {
    // Sort arr2 for binary searching
    arr2.sort((a, b) => a - b);
    const n = arr2.length;
    let count = 0;

    for (const val of arr1) {
        // Find the first index where arr2[idx] >= val - d
        let left = 0, right = n; // exclusive upper bound
        const targetLow = val - d;
        while (left < right) {
            const mid = left + ((right - left) >> 1);
            if (arr2[mid] < targetLow) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // After binary search, left is the lower bound index
        let ok = true;
        if (left < n && Math.abs(arr2[left] - val) <= d) {
            ok = false;
        } else if (left > 0 && Math.abs(arr2[left - 1] - val) <= d) {
            // Check previous element in case lower bound overshoots
            ok = false;
        }

        if (ok) count++;
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @param Integer $d
     * @return Integer
     */
    function findTheDistanceValue($arr1, $arr2, $d) {
        sort($arr2);
        $cnt = 0;
        $n2 = count($arr2);
        foreach ($arr1 as $a) {
            $pos = $this->lowerBound($arr2, $a);
            $ok = true;
            if ($pos < $n2 && abs($arr2[$pos] - $a) <= $d) {
                $ok = false;
            }
            if ($pos > 0 && abs($arr2[$pos - 1] - $a) <= $d) {
                $ok = false;
            }
            if ($ok) {
                $cnt++;
            }
        }
        return $cnt;
    }

    private function lowerBound($arr, $target) {
        $left = 0;
        $right = count($arr);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($arr[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func findTheDistanceValue(_ arr1: [Int], _ arr2: [Int], _ d: Int) -> Int {
        let sortedArr2 = arr2.sorted()
        var result = 0
        
        for value in arr1 {
            // Find the first index where element >= value - d
            var left = 0
            var right = sortedArr2.count
            while left < right {
                let mid = (left + right) / 2
                if sortedArr2[mid] < value - d {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            
            var isValid = true
            // Check the element at found index
            if left < sortedArr2.count && abs(sortedArr2[left] - value) <= d {
                isValid = false
            }
            // Check the previous element, which could be closer
            if left > 0 && abs(sortedArr2[left - 1] - value) <= d {
                isValid = false
            }
            
            if isValid {
                result += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
        val sorted = arr2.sortedArray()
        var result = 0
        for (value in arr1) {
            var idx = java.util.Arrays.binarySearch(sorted, value)
            if (idx < 0) idx = -idx - 1
            var ok = true
            if (idx < sorted.size && kotlin.math.abs(sorted[idx] - value) <= d) ok = false
            if (idx > 0 && kotlin.math.abs(sorted[idx - 1] - value) <= d) ok = false
            if (ok) result++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int findTheDistanceValue(List<int> arr1, List<int> arr2, int d) {
    arr2.sort();
    int count = 0;
    for (int a in arr1) {
      int idx = _lowerBound(arr2, a - d);
      bool ok = true;
      if (idx < arr2.length && (arr2[idx] - a).abs() <= d) {
        ok = false;
      } else if (idx > 0 && (arr2[idx - 1] - a).abs() <= d) {
        ok = false;
      }
      if (ok) count++;
    }
    return count;
  }

  int _lowerBound(List<int> list, int target) {
    int left = 0, right = list.length;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (list[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
package main

import "sort"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	sort.Ints(arr2)
	count := 0
	for _, v := range arr1 {
		left, right := v-d, v+d
		i := sort.Search(len(arr2), func(i int) bool { return arr2[i] >= left })
		ok := true
		if i < len(arr2) && arr2[i] <= right {
			ok = false
		}
		if i > 0 && arr2[i-1] >= left && arr2[i-1] <= right {
			ok = false
		}
		if ok {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def find_the_distance_value(arr1, arr2, d)
  arr2.sort!
  count = 0
  arr1.each do |x|
    lower = x - d
    upper = x + d
    l = 0
    r = arr2.length
    while l < r
      m = (l + r) / 2
      if arr2[m] < lower
        l = m + 1
      else
        r = m
      end
    end
    count += 1 if l == arr2.length || arr2[l] > upper
  end
  count
end
```

## Scala

```scala
object Solution {
    def findTheDistanceValue(arr1: Array[Int], arr2: Array[Int], d: Int): Int = {
        val sorted = arr2.sorted
        var result = 0

        for (a <- arr1) {
            // lower bound for a - d
            var lo = 0
            var hi = sorted.length
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (sorted(mid) < a - d) lo = mid + 1 else hi = mid
            }

            var ok = true
            if (lo < sorted.length && Math.abs(sorted(lo) - a) <= d) ok = false
            if (ok && lo > 0 && Math.abs(sorted(lo - 1) - a) <= d) ok = false

            if (ok) result += 1
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        let mut sorted_arr2 = arr2.clone();
        sorted_arr2.sort_unstable();
        let n = sorted_arr2.len();
        let mut count = 0;
        for &x in &arr1 {
            match sorted_arr2.binary_search(&x) {
                Ok(_) => continue, // exact match -> distance 0 <= d
                Err(pos) => {
                    let mut min_diff = i32::MAX;
                    if pos < n {
                        min_diff = (sorted_arr2[pos] - x).abs();
                    }
                    if pos > 0 {
                        let diff = (sorted_arr2[pos - 1] - x).abs();
                        if diff < min_diff {
                            min_diff = diff;
                        }
                    }
                    if min_diff > d {
                        count += 1;
                    }
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (find-the-distance-value arr1 arr2 d)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ([lst arr1] [cnt 0])
    (if (null? lst)
        cnt
        (let* ([x (car lst)]
               [ok (for/and ([y arr2]) (> (abs (- x y)) d))])
          (loop (cdr lst) (+ cnt (if ok 1 0)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_the_distance_value/3]).

-spec find_the_distance_value(Arr1 :: [integer()], Arr2 :: [integer()], D :: integer()) -> integer().
find_the_distance_value(Arr1, Arr2, D) ->
    Sorted = lists:sort(Arr2),
    Tuple = list_to_tuple(Sorted),
    N = tuple_size(Tuple),
    count_good(Arr1, Tuple, N, D, 0).

count_good([], _Tuple, _N, _D, Acc) -> Acc;
count_good([X|Rest], Tuple, N, D, Acc) ->
    Lower = lower_bound(Tuple, N, X - D),
    case Lower of
        L when L == N ->
            count_good(Rest, Tuple, N, D, Acc + 1);
        _ ->
            Val = element(Lower + 1, Tuple),
            if
                Val =< X + D -> % there exists an element within distance D
                    count_good(Rest, Tuple, N, D, Acc);
                true ->
                    count_good(Rest, Tuple, N, D, Acc + 1)
            end
    end.

lower_bound(Tuple, N, Target) ->
    lower_bound(Tuple, Target, 0, N).

lower_bound(_Tuple, _Target, Low, High) when Low >= High -> Low;
lower_bound(Tuple, Target, Low, High) ->
    Mid = (Low + High) div 2,
    Val = element(Mid + 1, Tuple),
    if
        Val < Target ->
            lower_bound(Tuple, Target, Mid + 1, High);
        true ->
            lower_bound(Tuple, Target, Low, Mid)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_distance_value(arr1 :: [integer], arr2 :: [integer], d :: integer) :: integer
  def find_the_distance_value(arr1, arr2, d) do
    sorted = Enum.sort(arr2)

    Enum.reduce(arr1, 0, fn x, acc ->
      if has_close?(sorted, x, d) do
        acc
      else
        acc + 1
      end
    end)
  end

  defp has_close?(arr, x, d) do
    low = lower_bound(arr, x - d)

    cond do
      low < length(arr) and abs(x - Enum.at(arr, low)) <= d -> true
      low > 0 and abs(x - Enum.at(arr, low - 1)) <= d -> true
      true -> false
    end
  end

  defp lower_bound(arr, target) do
    do_lower_bound(arr, target, 0, length(arr))
  end

  defp do_lower_bound(_arr, _target, lo, hi) when lo >= hi, do: lo

  defp do_lower_bound(arr, target, lo, hi) do
    mid = div(lo + hi, 2)

    if Enum.at(arr, mid) < target do
      do_lower_bound(arr, target, mid + 1, hi)
    else
      do_lower_bound(arr, target, lo, mid)
    end
  end
end
```
