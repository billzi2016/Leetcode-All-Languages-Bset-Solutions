# 0927. Three Equal Parts

## Cpp

```cpp
class Solution {
public:
    vector<int> threeEqualParts(vector<int>& arr) {
        int n = arr.size();
        int ones = 0;
        for (int bit : arr) if (bit == 1) ++ones;
        if (ones == 0) return {0, n - 2};
        if (ones % 3 != 0) return {-1, -1};
        int k = ones / 3;
        int first = -1, second = -1, third = -1;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (arr[i] == 1) {
                if (cnt == 0) first = i;
                else if (cnt == k) second = i;
                else if (cnt == 2 * k) third = i;
                ++cnt;
            }
        }
        int len = n - third; // length of the suffix pattern
        // Verify that the three parts are equal
        for (int i = 0; i < len; ++i) {
            if (arr[first + i] != arr[second + i] || arr[first + i] != arr[third + i])
                return {-1, -1};
        }
        int i = first + len - 1;
        int j = second + len;
        return {i, j};
    }
};
```

## Java

```java
class Solution {
    public int[] threeEqualParts(int[] arr) {
        int n = arr.length;
        int totalOnes = 0;
        for (int bit : arr) {
            if (bit == 1) totalOnes++;
        }
        if (totalOnes == 0) return new int[]{0, n - 1};
        if (totalOnes % 3 != 0) return new int[]{-1, -1};

        int k = totalOnes / 3;
        int first = -1, second = -1, third = -1;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 1) {
                count++;
                if (count == 1) first = i;
                else if (count == k + 1) second = i;
                else if (count == 2 * k + 1) third = i;
            }
        }

        int len = n - third; // length of the suffix pattern
        for (int i = 0; i < len; i++) {
            if (arr[first + i] != arr[second + i] || arr[first + i] != arr[third + i]) {
                return new int[]{-1, -1};
            }
        }

        int iIdx = first + len - 1;
        int jIdx = second + len;
        return new int[]{iIdx, jIdx};
    }
}
```

## Python

```python
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        total_ones = sum(arr)
        n = len(arr)
        if total_ones == 0:
            return [0, n - 1]
        if total_ones % 3 != 0:
            return [-1, -1]

        k = total_ones // 3
        first = second = third = -1
        count = 0
        for i, bit in enumerate(arr):
            if bit == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        # Align the three parts
        while third < n:
            if arr[first] != arr[second] or arr[second] != arr[third]:
                return [-1, -1]
            first += 1
            second += 1
            third += 1

        return [first - 1, second]
```

## Python3

```python
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        total_ones = sum(arr)
        if total_ones == 0:
            return [0, n - 1]
        if total_ones % 3 != 0:
            return [-1, -1]

        k = total_ones // 3
        first = second = third = -1
        cnt = 0
        for i, bit in enumerate(arr):
            if bit == 1:
                cnt += 1
                if cnt == 1:
                    first = i
                elif cnt == k + 1:
                    second = i
                elif cnt == 2 * k + 1:
                    third = i

        # Compare the three parts
        while third < n and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1

        if third == n:
            return [first - 1, second]
        else:
            return [-1, -1]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* threeEqualParts(int* arr, int arrSize, int* returnSize) {
    int totalOnes = 0;
    for (int i = 0; i < arrSize; ++i)
        totalOnes += arr[i];
    
    int* ans = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    if (totalOnes == 0) {
        ans[0] = 0;
        ans[1] = arrSize - 1;
        return ans;
    }
    
    if (totalOnes % 3 != 0) {
        ans[0] = -1;
        ans[1] = -1;
        return ans;
    }
    
    int k = totalOnes / 3;
    int first1 = -1, second1 = -1, third1 = -1;
    int cnt = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (arr[i] == 1) {
            if (cnt == 0) first1 = i;
            else if (cnt == k) second1 = i;
            else if (cnt == 2 * k) third1 = i;
            cnt++;
        }
    }
    
    // Compare the three parts
    while (third1 < arrSize) {
        if (arr[first1] != arr[second1] || arr[first1] != arr[third1]) {
            ans[0] = -1;
            ans[1] = -1;
            return ans;
        }
        first1++;
        second1++;
        third1++;
    }
    
    // Successful split
    ans[0] = first1 - 1;   // end index of first part
    ans[1] = second1;      // start index of third part
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ThreeEqualParts(int[] arr)
    {
        int n = arr.Length;
        int totalOnes = 0;
        foreach (int bit in arr)
            if (bit == 1) totalOnes++;

        if (totalOnes == 0)
            return new int[] { 0, n - 1 };

        if (totalOnes % 3 != 0)
            return new int[] { -1, -1 };

        int k = totalOnes / 3;
        int first = -1, second = -1, third = -1;
        int count = 0;

        for (int i = 0; i < n; i++)
        {
            if (arr[i] == 1)
            {
                count++;
                if (count == 1) first = i;
                else if (count == k + 1) second = i;
                else if (count == 2 * k + 1) third = i;
            }
        }

        while (third < n && arr[first] == arr[second] && arr[second] == arr[third])
        {
            first++;
            second++;
            third++;
        }

        if (third == n)
            return new int[] { first - 1, second };
        else
            return new int[] { -1, -1 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var threeEqualParts = function(arr) {
    const n = arr.length;
    let totalOnes = 0;
    for (const v of arr) if (v === 1) totalOnes++;
    
    // If there are no ones, any split works.
    if (totalOnes === 0) return [0, n - 1];
    // Must be divisible by 3.
    if (totalOnes % 3 !== 0) return [-1, -1];
    
    const k = totalOnes / 3;
    let first = -1, second = -1, third = -1;
    let cnt = 0;
    for (let i = 0; i < n; ++i) {
        if (arr[i] === 1) {
            ++cnt;
            if (cnt === 1) first = i;
            else if (cnt === k + 1) second = i;
            else if (cnt === 2 * k + 1) third = i;
        }
    }
    
    const len = n - third; // length of the suffix pattern
    
    // Verify that the three parts have identical patterns.
    for (let i = 0; i < len; ++i) {
        if (arr[first + i] !== arr[second + i] || arr[first + i] !== arr[third + i]) {
            return [-1, -1];
        }
    }
    
    const iIdx = first + len - 1;
    const jIdx = second + len;
    
    // Ensure indices are valid (jIdx must be < n)
    if (jIdx < n) return [iIdx, jIdx];
    return [-1, -1];
};
```

## Typescript

```typescript
function threeEqualParts(arr: number[]): number[] {
    const n = arr.length;
    let totalOnes = 0;
    for (const v of arr) if (v === 1) totalOnes++;
    
    if (totalOnes === 0) return [0, n - 1];
    if (totalOnes % 3 !== 0) return [-1, -1];
    
    const k = totalOnes / 3;
    let first = -1, second = -1, third = -1;
    let cnt = 0;
    for (let i = 0; i < n; i++) {
        if (arr[i] === 1) {
            cnt++;
            if (cnt === 1) first = i;
            else if (cnt === k + 1) second = i;
            else if (cnt === 2 * k + 1) third = i;
        }
    }
    
    while (third < n && arr[first] === arr[second] && arr[second] === arr[third]) {
        first++;
        second++;
        third++;
    }
    
    if (third !== n) return [-1, -1];
    
    const i = first - 1;
    const j = second;
    return [i, j];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function threeEqualParts($arr) {
        $n = count($arr);
        $totalOnes = array_sum($arr);
        if ($totalOnes == 0) {
            return [0, $n - 2];
        }
        if ($totalOnes % 3 != 0) {
            return [-1, -1];
        }

        $k = intdiv($totalOnes, 3);
        $first = $second = $third = -1;
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($arr[$i] == 1) {
                $cnt++;
                if ($cnt == 1) {
                    $first = $i;
                } elseif ($cnt == $k + 1) {
                    $second = $i;
                } elseif ($cnt == 2 * $k + 1) {
                    $third = $i;
                }
            }
        }

        // length of the pattern that must be identical in all three parts
        $len = $n - $third;

        // verify that the three segments are equal
        for ($i = 0; $i < $len; $i++) {
            if ($arr[$first + $i] != $arr[$second + $i] || $arr[$first + $i] != $arr[$third + $i]) {
                return [-1, -1];
            }
        }

        // ensure there are enough zeros between the parts
        if ($first + $len > $second || $second + $len > $third) {
            return [-1, -1];
        }

        return [$first + $len - 1, $second + $len];
    }
}
```

## Swift

```swift
class Solution {
    func threeEqualParts(_ arr: [Int]) -> [Int] {
        let n = arr.count
        var totalOnes = 0
        for v in arr where v == 1 { totalOnes += 1 }
        if totalOnes == 0 {
            return [0, n - 1]
        }
        if totalOnes % 3 != 0 {
            return [-1, -1]
        }
        let k = totalOnes / 3
        var first = -1, second = -1, third = -1
        var count = 0
        for i in 0..<n {
            if arr[i] == 1 {
                count += 1
                if count == 1 { first = i }
                else if count == k + 1 { second = i }
                else if count == 2 * k + 1 { third = i }
            }
        }
        var i1 = first, i2 = second, i3 = third
        while i3 < n {
            if arr[i1] != arr[i2] || arr[i2] != arr[i3] {
                return [-1, -1]
            }
            i1 += 1
            i2 += 1
            i3 += 1
        }
        return [i1 - 1, i2]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun threeEqualParts(arr: IntArray): IntArray {
        val n = arr.size
        var totalOnes = 0
        for (v in arr) if (v == 1) totalOnes++
        if (totalOnes == 0) return intArrayOf(0, n - 2)
        if (totalOnes % 3 != 0) return intArrayOf(-1, -1)

        val k = totalOnes / 3
        var first = -1
        var second = -1
        var third = -1
        var cnt = 0
        for (i in 0 until n) {
            if (arr[i] == 1) {
                cnt++
                when (cnt) {
                    1 -> first = i
                    k + 1 -> second = i
                    2 * k + 1 -> third = i
                }
            }
        }

        var i = first
        var j = second
        var l = third
        while (l < n) {
            if (arr[i] != arr[j] || arr[j] != arr[l]) return intArrayOf(-1, -1)
            i++; j++; l++
        }
        // i-1 is the end index of first part, j is the start index of third part
        return intArrayOf(i - 1, j)
    }
}
```

## Dart

```dart
class Solution {
  List<int> threeEqualParts(List<int> arr) {
    int n = arr.length;
    int totalOnes = 0;
    for (int v in arr) {
      if (v == 1) totalOnes++;
    }
    if (totalOnes == 0) return [0, n - 1];
    if (totalOnes % 3 != 0) return [-1, -1];

    int k = totalOnes ~/ 3;
    int first = -1, second = -1, third = -1;
    int count = 0;
    for (int i = 0; i < n; i++) {
      if (arr[i] == 1) {
        if (count == 0) first = i;
        else if (count == k) second = i;
        else if (count == 2 * k) third = i;
        count++;
      }
    }

    while (third < n && arr[first] == arr[second] && arr[second] == arr[third]) {
      first++;
      second++;
      third++;
    }

    if (third != n) return [-1, -1];

    int i = first - 1;
    int j = second;
    return [i, j];
  }
}
```

## Golang

```go
func threeEqualParts(arr []int) []int {
    n := len(arr)
    totalOnes := 0
    for _, v := range arr {
        if v == 1 {
            totalOnes++
        }
    }
    if totalOnes == 0 {
        return []int{0, n - 1}
    }
    if totalOnes%3 != 0 {
        return []int{-1, -1}
    }
    k := totalOnes / 3
    cnt := 0
    var i1, i2, i3 int
    for idx, v := range arr {
        if v == 1 {
            cnt++
            if cnt == 1 {
                i1 = idx
            } else if cnt == k+1 {
                i2 = idx
            } else if cnt == 2*k+1 {
                i3 = idx
            }
        }
    }
    for i3 < n && arr[i1] == arr[i2] && arr[i2] == arr[i3] {
        i1++
        i2++
        i3++
    }
    if i3 == n {
        return []int{i1 - 1, i2}
    }
    return []int{-1, -1}
}
```

## Ruby

```ruby
def three_equal_parts(arr)
  n = arr.length
  total = arr.sum
  return [0, n - 1] if total == 0
  return [-1, -1] if total % 3 != 0

  k = total / 3
  first = second = third = nil
  count = 0

  arr.each_with_index do |bit, i|
    next unless bit == 1
    count += 1
    case count
    when 1
      first = i
    when k + 1
      second = i
    when 2 * k + 1
      third = i
      break
    end
  end

  while third < n && arr[first] == arr[second] && arr[second] == arr[third]
    first += 1
    second += 1
    third += 1
  end

  if third == n
    [first - 1, second]
  else
    [-1, -1]
  end
end
```

## Scala

```scala
object Solution {
    def threeEqualParts(arr: Array[Int]): Array[Int] = {
        val totalOnes = arr.count(_ == 1)
        if (totalOnes == 0) return Array(0, arr.length - 1)
        if (totalOnes % 3 != 0) return Array(-1, -1)

        val k = totalOnes / 3
        var first = -1
        var second = -1
        var third = -1
        var cnt = 0

        for (i <- arr.indices) {
            if (arr(i) == 1) {
                if (cnt == 0) first = i
                else if (cnt == k) second = i
                else if (cnt == 2 * k) third = i
                cnt += 1
            }
        }

        val len = arr.length - third // length of the pattern to match

        if (first + len > second || second + len > third) return Array(-1, -1)

        for (i <- 0 until len) {
            if (arr(first + i) != arr(second + i) || arr(first + i) != arr(third + i)) {
                return Array(-1, -1)
            }
        }

        Array(first + len - 1, second + len)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn three_equal_parts(arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        let total_ones = arr.iter().filter(|&&x| x == 1).count();

        if total_ones == 0 {
            return vec![0, (n - 1) as i32];
        }
        if total_ones % 3 != 0 {
            return vec![-1, -1];
        }

        let k = total_ones / 3;
        let mut first_one: Option<usize> = None;
        let mut second_one: Option<usize> = None;
        let mut third_one: Option<usize> = None;
        let mut cnt = 0;

        for (i, &v) in arr.iter().enumerate() {
            if v == 1 {
                cnt += 1;
                if cnt == 1 {
                    first_one = Some(i);
                } else if cnt == k + 1 {
                    second_one = Some(i);
                } else if cnt == 2 * k + 1 {
                    third_one = Some(i);
                }
            }
        }

        let f = first_one.unwrap();
        let s = second_one.unwrap();
        let t = third_one.unwrap();

        // Length of the pattern that must be identical in all three parts
        let tail_len = n - t;

        if f + tail_len > s || s + tail_len > t {
            return vec![-1, -1];
        }

        for offset in 0..tail_len {
            let a = arr[f + offset];
            let b = arr[s + offset];
            let c = arr[t + offset];
            if a != b || b != c {
                return vec![-1, -1];
            }
        }

        let i = (f + tail_len - 1) as i32;
        let j = (s + tail_len) as i32;
        vec![i, j]
    }
}
```

## Racket

```racket
(define/contract (three-equal-parts arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector arr))
         (n (vector-length v))
         (total-ones (for/sum ([i (in-range n)]) (vector-ref v i))))
    (cond
      [(= total-ones 0) (list 0 (- n 1))]
      [(not (= (remainder total-ones 3) 0)) (list -1 -1)]
      [else
       (let* ((k (quotient total-ones 3))
              (indices
                (let loop ((i 0) (cnt 0) (f -1) (s -1) (t -1))
                  (if (= i n)
                      (values f s t)
                      (let ((val (vector-ref v i)))
                        (if (= val 1)
                            (let ((newcnt (+ cnt 1)))
                              (cond
                                [(= newcnt 1) (loop (+ i 1) newcnt i s t)]
                                [(= newcnt (+ k 1)) (loop (+ i 1) newcnt f i t)]
                                [(= newcnt (+ (* 2 k) 1)) (loop (+ i 1) newcnt f s i)]
                                [else (loop (+ i 1) newcnt f s t)]))
                            (loop (+ i 1) cnt f s t)))))))
         (let-values ([(first1 second1 third1) indices])
           (let loop ((f first1) (s second1) (t third1))
             (if (= t n)
                 (list (- f 1) s)
                 (if (and (= (vector-ref v f) (vector-ref v s))
                          (= (vector-ref v s) (vector-ref v t)))
                     (loop (+ f 1) (+ s 1) (+ t 1))
                     (list -1 -1))))))])))
```

## Erlang

```erlang
-module(solution).
-export([three_equal_parts/1]).

three_equal_parts(Arr) ->
    N = length(Arr),
    OnesPos = ones_positions(Arr, 0),
    TotalOnes = length(OnesPos),
    case TotalOnes of
        0 -> [0, N - 1];
        _ when TotalOnes rem 3 =/= 0 -> [-1, -1];
        _ ->
            K = TotalOnes div 3,
            Idx1 = lists:nth(1, OnesPos),
            Idx2 = lists:nth(K + 1, OnesPos),
            Idx3 = lists:nth(2 * K + 1, OnesPos),
            Tuple = list_to_tuple(Arr),
            Len = N - Idx3,
            case compare_suffix(Tuple, Idx1, Idx2, Idx3, Len) of
                true ->
                    I = Idx1 + Len - 1,
                    J = Idx2 + Len,
                    [I, J];
                false -> [-1, -1]
            end
    end.

ones_positions([], _Idx) -> [];
ones_positions([H | T], Idx) ->
    Rest = ones_positions(T, Idx + 1),
    case H of
        1 -> [Idx | Rest];
        _ -> Rest
    end.

compare_suffix(_Tuple, _I1, _I2, _I3, 0) -> true;
compare_suffix(Tuple, I1, I2, I3, Rem) ->
    E1 = element(I1 + 1, Tuple),
    E2 = element(I2 + 1, Tuple),
    E3 = element(I3 + 1, Tuple),
    if
        E1 =:= E2, E2 =:= E3 ->
            compare_suffix(Tuple, I1 + 1, I2 + 1, I3 + 1, Rem - 1);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec three_equal_parts(arr :: [integer]) :: [integer]
  def three_equal_parts(arr) do
    n = length(arr)
    total_ones = Enum.count(arr, fn x -> x == 1 end)

    cond do
      total_ones == 0 ->
        [0, n - 1]

      rem(total_ones, 3) != 0 ->
        [-1, -1]

      true ->
        k = div(total_ones, 3)
        tuple = List.to_tuple(arr)

        {first_idx, second_idx, third_idx} =
          Enum.reduce(Enum.with_index(arr), {nil, nil, nil, 0}, fn
            {val, idx}, {f, s, t, cnt} ->
              if val == 1 do
                cnt = cnt + 1

                cond do
                  cnt == 1 -> {idx, f, s, cnt}
                  cnt == k + 1 -> {f, idx, s, cnt}
                  cnt == 2 * k + 1 -> {f, s, idx, cnt}
                  true -> {f, s, t, cnt}
                end
              else
                {f, s, t, cnt}
              end
          end)
          |> (fn {f, s, t, _cnt} -> {f, s, t} end).()

        pattern_len = n - third_idx

        equal =
          Enum.reduce_while(0..(pattern_len - 1), true, fn offset, _acc ->
            a = elem(tuple, first_idx + offset)
            b = elem(tuple, second_idx + offset)
            c = elem(tuple, third_idx + offset)

            if a == b and b == c do
              {:cont, true}
            else
              {:halt, false}
            end
          end)

        if equal do
          i = first_idx + pattern_len - 1
          j = second_idx + pattern_len
          [i, j]
        else
          [-1, -1]
        end
    end
  end
end
```
