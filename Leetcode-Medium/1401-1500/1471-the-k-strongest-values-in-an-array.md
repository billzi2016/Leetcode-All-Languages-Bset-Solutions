# 1471. The k Strongest Values in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        int n = arr.size();
        int median = arr[(n - 1) / 2];
        vector<int> res;
        res.reserve(k);
        int left = 0, right = n - 1;
        while ((int)res.size() < k) {
            long long diffL = llabs((long long)arr[left] - median);
            long long diffR = llabs((long long)arr[right] - median);
            if (diffR > diffL) {
                res.push_back(arr[right--]);
            } else if (diffR < diffL) {
                res.push_back(arr[left++]);
            } else { // equal distance, take larger value
                res.push_back(arr[right--]);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] getStrongest(int[] arr, int k) {
        java.util.Arrays.sort(arr);
        int n = arr.length;
        int median = arr[(n - 1) / 2];
        int left = 0, right = n - 1;
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            if (Math.abs(arr[right] - median) >= Math.abs(arr[left] - median)) {
                result[i] = arr[right--];
            } else {
                result[i] = arr[left++];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        res = []
        l, r = 0, n - 1
        while len(res) < k:
            left_diff = abs(arr[l] - median)
            right_diff = abs(arr[r] - median)
            if right_diff > left_diff:
                res.append(arr[r])
                r -= 1
            elif right_diff < left_diff:
                res.append(arr[l])
                l += 1
            else:  # equal distance, pick larger value
                if arr[r] >= arr[l]:
                    res.append(arr[r])
                    r -= 1
                else:
                    res.append(arr[l])
                    l += 1
        return res
```

## Python3

```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        left, right = 0, n - 1
        res = []
        while len(res) < k:
            if (arr[right] - median) >= (median - arr[left]):
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
        return res
```

## C

```c
#include <stdlib.h>
#include <limits.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getStrongest(int* arr, int arrSize, int k, int* returnSize) {
    qsort(arr, arrSize, sizeof(int), cmp_int);
    
    int median = arr[(arrSize - 1) / 2];
    
    int *res = (int *)malloc(k * sizeof(int));
    int left = 0, right = arrSize - 1;
    int idx = 0;
    
    while (idx < k) {
        long long diffL = llabs((long long)arr[left] - median);
        long long diffR = llabs((long long)arr[right] - median);
        
        if (diffR > diffL) {
            res[idx++] = arr[right--];
        } else if (diffL > diffR) {
            res[idx++] = arr[left++];
        } else { // equal distance, pick larger value (right side)
            res[idx++] = arr[right--];
        }
    }
    
    *returnSize = k;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetStrongest(int[] arr, int k) {
        Array.Sort(arr);
        int n = arr.Length;
        int median = arr[(n - 1) / 2];
        List<int> result = new List<int>(k);
        int left = 0, right = n - 1;
        while (result.Count < k) {
            int dl = Math.Abs(arr[left] - median);
            int dr = Math.Abs(arr[right] - median);
            if (dl > dr) {
                result.Add(arr[left]);
                left++;
            } else if (dr > dl) {
                result.Add(arr[right]);
                right--;
            } else {
                // distances equal, pick larger value
                if (arr[left] > arr[right]) {
                    result.Add(arr[left]);
                    left++;
                } else {
                    result.Add(arr[right]);
                    right--;
                }
            }
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var getStrongest = function(arr, k) {
    const n = arr.length;
    arr.sort((a, b) => a - b);
    const midIdx = Math.floor((n - 1) / 2);
    const median = arr[midIdx];
    
    let left = 0, right = n - 1;
    const res = [];
    
    while (res.length < k) {
        const diffL = Math.abs(arr[left] - median);
        const diffR = Math.abs(arr[right] - median);
        
        if (diffR > diffL) {
            res.push(arr[right]);
            right--;
        } else if (diffR < diffL) {
            res.push(arr[left]);
            left++;
        } else { // equal distance, pick larger value
            if (arr[right] > arr[left]) {
                res.push(arr[right]);
                right--;
            } else {
                res.push(arr[left]);
                left++;
            }
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function getStrongest(arr: number[], k: number): number[] {
    const n = arr.length;
    arr.sort((a, b) => a - b);
    const median = arr[Math.floor((n - 1) / 2)];
    let left = 0, right = n - 1;
    const result: number[] = [];
    while (result.length < k) {
        const diffL = Math.abs(arr[left] - median);
        const diffR = Math.abs(arr[right] - median);
        if (diffR > diffL || (diffR === diffL && arr[right] > arr[left])) {
            result.push(arr[right]);
            right--;
        } else {
            result.push(arr[left]);
            left++;
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
     * @param Integer $k
     * @return Integer[]
     */
    function getStrongest($arr, $k) {
        sort($arr);
        $n = count($arr);
        $midIdx = intdiv($n - 1, 2);
        $median = $arr[$midIdx];
        $left = 0;
        $right = $n - 1;
        $res = [];
        $cnt = 0;
        while ($cnt < $k) {
            $distL = abs($arr[$left] - $median);
            $distR = abs($arr[$right] - $median);
            if ($distL > $distR) {
                $res[] = $arr[$left];
                $left++;
            } elseif ($distR > $distL) {
                $res[] = $arr[$right];
                $right--;
            } else {
                // equal distance, pick larger value (right side in sorted array)
                if ($arr[$right] >= $arr[$left]) {
                    $res[] = $arr[$right];
                    $right--;
                } else {
                    $res[] = $arr[$left];
                    $left++;
                }
            }
            $cnt++;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func getStrongest(_ arr: [Int], _ k: Int) -> [Int] {
        let sorted = arr.sorted()
        let n = sorted.count
        let median = sorted[(n - 1) / 2]
        var left = 0
        var right = n - 1
        var result = [Int]()
        while result.count < k {
            let diffLeft = abs(sorted[left] - median)
            let diffRight = abs(sorted[right] - median)
            if diffRight > diffLeft || (diffRight == diffLeft && sorted[right] > sorted[left]) {
                result.append(sorted[right])
                right -= 1
            } else {
                result.append(sorted[left])
                left += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getStrongest(arr: IntArray, k: Int): IntArray {
        val sorted = arr.clone()
        java.util.Arrays.sort(sorted)
        val n = sorted.size
        val median = sorted[(n - 1) / 2]
        var left = 0
        var right = n - 1
        val result = IntArray(k)
        var idx = 0
        while (idx < k) {
            val leftDist = kotlin.math.abs(sorted[left] - median)
            val rightDist = kotlin.math.abs(sorted[right] - median)
            if (leftDist > rightDist) {
                result[idx++] = sorted[left]
                left++
            } else {
                result[idx++] = sorted[right]
                right--
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> getStrongest(List<int> arr, int k) {
    arr.sort();
    int n = arr.length;
    int median = arr[(n - 1) ~/ 2];
    int left = 0, right = n - 1;
    List<int> result = [];
    while (result.length < k) {
      int leftDist = (arr[left] - median).abs();
      int rightDist = (arr[right] - median).abs();
      if (rightDist > leftDist) {
        result.add(arr[right]);
        right--;
      } else if (rightDist < leftDist) {
        result.add(arr[left]);
        left++;
      } else {
        // distances equal, pick the larger value
        if (arr[right] >= arr[left]) {
          result.add(arr[right]);
          right--;
        } else {
          result.add(arr[left]);
          left++;
        }
      }
    }
    return result;
  }
}
```

## Golang

```go
func getStrongest(arr []int, k int) []int {
    sort.Ints(arr)
    n := len(arr)
    median := arr[(n-1)/2]
    res := make([]int, 0, k)
    left, right := 0, n-1
    for len(res) < k {
        diffL := abs(arr[left] - median)
        diffR := abs(arr[right] - median)
        if diffR > diffL || (diffR == diffL && arr[right] > arr[left]) {
            res = append(res, arr[right])
            right--
        } else {
            res = append(res, arr[left])
            left++
        }
    }
    return res
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```

## Ruby

```ruby
def get_strongest(arr, k)
  sorted = arr.sort
  n = sorted.length
  m = sorted[(n - 1) / 2]
  left = 0
  right = n - 1
  result = []
  while result.size < k
    left_diff = (sorted[left] - m).abs
    right_diff = (sorted[right] - m).abs
    if right_diff > left_diff
      result << sorted[right]
      right -= 1
    elsif right_diff < left_diff
      result << sorted[left]
      left += 1
    else
      if sorted[right] > sorted[left]
        result << sorted[right]
        right -= 1
      else
        result << sorted[left]
        left += 1
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def getStrongest(arr: Array[Int], k: Int): Array[Int] = {
        val sorted = arr.sorted
        val n = sorted.length
        val median = sorted((n - 1) / 2)
        var left = 0
        var right = n - 1
        val result = scala.collection.mutable.ArrayBuffer[Int]()
        while (result.size < k) {
            val leftDiff = math.abs(sorted(left) - median)
            val rightDiff = math.abs(sorted(right) - median)
            if (rightDiff > leftDiff || (rightDiff == leftDiff && sorted(right) > sorted(left))) {
                result += sorted(right)
                right -= 1
            } else {
                result += sorted(left)
                left += 1
            }
        }
        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_strongest(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let mut v = arr.clone();
        v.sort();
        let n = v.len();
        let median = v[(n - 1) / 2];
        let mut left = 0usize;
        let mut right = n - 1;
        let mut res = Vec::with_capacity(k as usize);
        while res.len() < k as usize {
            let left_diff = (v[left] - median).abs();
            let right_diff = (v[right] - median).abs();
            if right_diff > left_diff || (right_diff == left_diff && v[right] > v[left]) {
                res.push(v[right]);
                if right == 0 {
                    break;
                }
                right -= 1;
            } else {
                res.push(v[left]);
                left += 1;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (get-strongest arr k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((sorted (sort arr <))
         (vec (list->vector sorted))
         (n (vector-length vec))
         (mid-index (quotient (- n 1) 2))
         (median (vector-ref vec mid-index)))
    (let loop ((l 0) (r (sub1 n)) (cnt 0) (acc '()))
      (if (= cnt k)
          (reverse acc)
          (let* ((dl (abs (- (vector-ref vec l) median)))
                 (dr (abs (- (vector-ref vec r) median))))
            (if (or (> dr dl)
                    (and (= dr dl)
                         (> (vector-ref vec r) (vector-ref vec l))))
                (loop l (sub1 r) (add1 cnt) (cons (vector-ref vec r) acc))
                (loop (add1 l) r (add1 cnt) (cons (vector-ref vec l) acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_strongest/2]).

-spec get_strongest(Arr :: [integer()], K :: integer()) -> [integer()].
get_strongest(Arr, K) ->
    Sorted = lists:sort(Arr),
    Tuple = list_to_tuple(Sorted),
    Len = tuple_size(Tuple),
    MidIdx = (Len - 1) div 2,
    Median = element(MidIdx + 1, Tuple),
    pick(K, 0, Len - 1, Tuple, Median, []).

pick(0, _Left, _Right, _Tuple, _Median, Acc) ->
    lists:reverse(Acc);
pick(K, Left, Right, Tuple, Median, Acc) when K > 0 ->
    LVal = element(Left + 1, Tuple),
    RVal = element(Right + 1, Tuple),
    DiffL = abs(LVal - Median),
    DiffR = abs(RVal - Median),
    case {DiffR > DiffL, DiffR < DiffL} of
        {true, _} ->
            pick(K - 1, Left, Right - 1, Tuple, Median, [RVal | Acc]);
        {false, true} ->
            pick(K - 1, Left + 1, Right, Tuple, Median, [LVal | Acc]);
        {false, false} -> % equal distances, choose larger value (RVal >= LVal)
            pick(K - 1, Left, Right - 1, Tuple, Median, [RVal | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_strongest(arr :: [integer], k :: integer) :: [integer]
  def get_strongest(arr, k) do
    sorted = Enum.sort(arr)
    n = length(sorted)
    median = Enum.at(sorted, div(n - 1, 2))
    collect(sorted, median, 0, n - 1, [], k)
  end

  defp collect(_sorted, _median, _l, _r, acc, k) when length(acc) == k do
    Enum.reverse(acc)
  end

  defp collect(sorted, median, l, r, acc, k) do
    left_val = Enum.at(sorted, l)
    right_val = Enum.at(sorted, r)

    diff_left = Kernel.abs(left_val - median)
    diff_right = Kernel.abs(right_val - median)

    cond do
      diff_right > diff_left ->
        collect(sorted, median, l, r - 1, [right_val | acc], k)

      diff_left > diff_right ->
        collect(sorted, median, l + 1, r, [left_val | acc], k)

      true ->
        if right_val >= left_val do
          collect(sorted, median, l, r - 1, [right_val | acc], k)
        else
          collect(sorted, median, l + 1, r, [left_val | acc], k)
        end
    end
  end
end
```
