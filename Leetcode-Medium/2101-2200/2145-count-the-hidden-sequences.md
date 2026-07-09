# 2145. Count the Hidden Sequences

## Cpp

```cpp
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long cur = 0;
        long long mn = 0, mx = 0;
        for (int d : differences) {
            cur += d;
            if (cur < mn) mn = cur;
            if (cur > mx) mx = cur;
        }
        long long neededRange = mx - mn;
        long long allowedRange = (long long)upper - lower;
        if (neededRange > allowedRange) return 0;
        return (int)(allowedRange - neededRange + 1);
    }
};
```

## Java

```java
class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        long cur = 0;
        long min = 0, max = 0;
        for (int d : differences) {
            cur += d;
            if (cur < min) min = cur;
            if (cur > max) max = cur;
        }
        long range = max - min;
        long total = (long) upper - lower;
        long ans = total - range + 1;
        return ans < 0 ? 0 : (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        cur = 0
        minv = maxv = 0
        for d in differences:
            cur += d
            if cur < minv:
                minv = cur
            elif cur > maxv:
                maxv = cur
        diff_range = maxv - minv
        total_range = upper - lower
        if diff_range > total_range:
            return 0
        return total_range - diff_range + 1
```

## Python3

```python
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = 0
        mn = mx = 0
        for d in differences:
            cur += d
            if cur < mn:
                mn = cur
            elif cur > mx:
                mx = cur
        range_seq = mx - mn
        total_range = upper - lower
        ans = total_range - range_seq + 1
        return ans if ans > 0 else 0
```

## C

```c
#include <stddef.h>

int numberOfArrays(int* differences, int differencesSize, int lower, int upper) {
    long long cur = 0;
    long long minVal = 0, maxVal = 0;
    for (int i = 0; i < differencesSize; ++i) {
        cur += differences[i];
        if (cur < minVal) minVal = cur;
        if (cur > maxVal) maxVal = cur;
    }
    long long range = maxVal - minVal;
    long long totalRange = (long long)upper - (long long)lower;
    if (range > totalRange) return 0;
    return (int)(totalRange - range + 1);
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfArrays(int[] differences, int lower, int upper) {
        long cur = 0;
        long min = 0, max = 0;
        foreach (int d in differences) {
            cur += d;
            if (cur < min) min = cur;
            else if (cur > max) max = cur;
        }
        long needed = max - min;
        long totalRange = (long)upper - lower;
        long ans = totalRange - needed + 1;
        return ans > 0 ? (int)ans : 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} differences
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var numberOfArrays = function(differences, lower, upper) {
    let cur = 0;
    let minVal = 0;
    let maxVal = 0;
    for (const d of differences) {
        cur += d;
        if (cur < minVal) minVal = cur;
        else if (cur > maxVal) maxVal = cur;
    }
    const range = maxVal - minVal;
    const total = upper - lower;
    if (range > total) return 0;
    return total - range + 1;
};
```

## Typescript

```typescript
function numberOfArrays(differences: number[], lower: number, upper: number): number {
    let cur = 0;
    let minVal = 0;
    let maxVal = 0;
    for (const d of differences) {
        cur += d;
        if (cur < minVal) minVal = cur;
        else if (cur > maxVal) maxVal = cur;
    }
    const neededRange = maxVal - minVal;
    const totalRange = upper - lower;
    const ans = totalRange - neededRange + 1;
    return ans > 0 ? ans : 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $differences
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function numberOfArrays($differences, $lower, $upper) {
        $cur = 0;
        $minVal = 0;
        $maxVal = 0;
        foreach ($differences as $d) {
            $cur += $d;
            if ($cur < $minVal) {
                $minVal = $cur;
            } elseif ($cur > $maxVal) {
                $maxVal = $cur;
            }
        }
        $range = $maxVal - $minVal;
        $totalRange = $upper - $lower;
        if ($range > $totalRange) {
            return 0;
        }
        return $totalRange - $range + 1;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfArrays(_ differences: [Int], _ lower: Int, _ upper: Int) -> Int {
        var cur = 0
        var minVal = 0
        var maxVal = 0
        for d in differences {
            cur += d
            if cur < minVal { minVal = cur }
            if cur > maxVal { maxVal = cur }
        }
        let range = maxVal - minVal
        let total = upper - lower + 1
        let ans = total - range
        return ans > 0 ? ans : 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfArrays(differences: IntArray, lower: Int, upper: Int): Int {
        var cur = 0L
        var minPref = 0L
        var maxPref = 0L
        for (d in differences) {
            cur += d.toLong()
            if (cur < minPref) minPref = cur
            if (cur > maxPref) maxPref = cur
        }
        val range = maxPref - minPref
        val totalRange = upper.toLong() - lower.toLong()
        val possible = totalRange - range + 1
        return if (possible > 0) possible.toInt() else 0
    }
}
```

## Dart

```dart
class Solution {
  int numberOfArrays(List<int> differences, int lower, int upper) {
    int cur = 0;
    int minVal = 0;
    int maxVal = 0;
    for (int d in differences) {
      cur += d;
      if (cur < minVal) minVal = cur;
      if (cur > maxVal) maxVal = cur;
    }
    int range = maxVal - minVal;
    int total = upper - lower + 1 - range;
    return total > 0 ? total : 0;
  }
}
```

## Golang

```go
func numberOfArrays(differences []int, lower int, upper int) int {
    cur := 0
    minV, maxV := 0, 0
    for _, d := range differences {
        cur += d
        if cur < minV {
            minV = cur
        }
        if cur > maxV {
            maxV = cur
        }
    }
    seqRange := maxV - minV
    totalRange := upper - lower
    ans := totalRange - seqRange + 1
    if ans < 0 {
        ans = 0
    }
    return ans
}
```

## Ruby

```ruby
def number_of_arrays(differences, lower, upper)
  cur = 0
  min_val = 0
  max_val = 0
  differences.each do |d|
    cur += d
    min_val = cur if cur < min_val
    max_val = cur if cur > max_val
  end
  needed_range = max_val - min_val
  total_range = upper - lower
  ans = total_range - needed_range + 1
  ans > 0 ? ans : 0
end
```

## Scala

```scala
object Solution {
    def numberOfArrays(differences: Array[Int], lower: Int, upper: Int): Int = {
        var cur: Long = 0L
        var minVal: Long = 0L
        var maxVal: Long = 0L
        for (d <- differences) {
            cur += d.toLong
            if (cur < minVal) minVal = cur
            if (cur > maxVal) maxVal = cur
        }
        val needed = maxVal - minVal
        val totalRange = upper.toLong - lower.toLong
        if (needed > totalRange) 0
        else ((totalRange - needed + 1).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_arrays(differences: Vec<i32>, lower: i32, upper: i32) -> i32 {
        let mut pref: i64 = 0;
        let mut min_pref: i64 = 0;
        let mut max_pref: i64 = 0;
        for d in differences.iter() {
            pref += *d as i64;
            if pref < min_pref {
                min_pref = pref;
            }
            if pref > max_pref {
                max_pref = pref;
            }
        }
        let range = (upper - lower) as i64;
        let needed = max_pref - min_pref;
        let mut ans = range - needed + 1;
        if ans < 0 {
            ans = 0;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-arrays differences lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let loop ((lst differences) (cur 0) (mn 0) (mx 0))
    (if (null? lst)
        (let* ((range (- mx mn))
               (total (+ (- upper lower) 1))
               (ans (- total range)))
          (if (< ans 0) 0 ans))
        (let* ((newcur (+ cur (car lst)))
               (newmn (min mn newcur))
               (newmx (max mx newcur)))
          (loop (cdr lst) newcur newmn newmx)))))
```

## Erlang

```erlang
-spec number_of_arrays([integer()], integer(), integer()) -> integer().
number_of_arrays(Differences, Lower, Upper) ->
    {_, Min, Max} = lists:foldl(
        fun(Diff, {Cur, MinAcc, MaxAcc}) ->
            NewCur = Cur + Diff,
            NewMin = if NewCur < MinAcc -> NewCur; true -> MinAcc end,
            NewMax = if NewCur > MaxAcc -> NewCur; true -> MaxAcc end,
            {NewCur, NewMin, NewMax}
        end,
        {0, 0, 0},
        Differences),
    Range = Max - Min,
    Ans = Upper - Lower - Range + 1,
    case Ans of
        N when N < 0 -> 0;
        _ -> Ans
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_arrays(differences :: [integer], lower :: integer, upper :: integer) :: integer
  def number_of_arrays(differences, lower, upper) do
    {min_val, max_val, _cur} =
      Enum.reduce(differences, {0, 0, 0}, fn d, {min_acc, max_acc, cur} ->
        new_cur = cur + d
        new_min = if new_cur < min_acc, do: new_cur, else: min_acc
        new_max = if new_cur > max_acc, do: new_cur, else: max_acc
        {new_min, new_max, new_cur}
      end)

    needed_range = max_val - min_val
    total_range = upper - lower

    if needed_range > total_range do
      0
    else
      total_range - needed_range + 1
    end
  end
end
```
