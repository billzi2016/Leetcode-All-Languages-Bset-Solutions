# 1013. Partition Array Into Three Parts With Equal Sum

## Cpp

```cpp
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        long long total = 0;
        for (int num : arr) total += num;
        if (total % 3 != 0) return false;
        long long target = total / 3;
        long long sum = 0;
        int count = 0;
        // we need at least two cuts before the last element
        for (size_t i = 0; i < arr.size(); ++i) {
            sum += arr[i];
            if (sum == target) {
                ++count;
                sum = 0;
                if (count == 2 && i < arr.size() - 1) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        long total = 0;
        for (int num : arr) total += num;
        if (total % 3 != 0) return false;
        long target = total / 3;
        long sum = 0;
        int count = 0;
        // Find first two partitions; the third is guaranteed by remaining elements
        for (int i = 0; i < arr.length - 1; i++) {
            sum += arr[i];
            if (sum == target) {
                count++;
                sum = 0;
                if (count == 2) return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        cnt = 0
        n = len(arr)
        for i in range(n - 1):  # ensure at least one element remains for the third part
            cur += arr[i]
            if cur == target:
                cnt += 1
                cur = 0
                if cnt == 2:
                    return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        parts = 0
        # stop before last element to ensure third part non‑empty
        for i in range(len(arr) - 1):
            cur += arr[i]
            if cur == target:
                parts += 1
                cur = 0
                if parts == 2:
                    return True
        return False
```

## C

```c
#include <stdbool.h>

bool canThreePartsEqualSum(int* arr, int arrSize) {
    long long total = 0;
    for (int i = 0; i < arrSize; ++i) {
        total += arr[i];
    }
    if (total % 3 != 0) return false;
    long long target = total / 3;
    long long sum = 0;
    int partsFound = 0;
    for (int i = 0; i < arrSize - 1; ++i) {
        sum += arr[i];
        if (sum == target) {
            ++partsFound;
            sum = 0;
            if (partsFound == 2) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanThreePartsEqualSum(int[] arr) {
        long total = 0;
        foreach (int num in arr) total += num;
        if (total % 3 != 0) return false;
        long target = total / 3;
        long sum = 0;
        int count = 0;
        // we need to find first two parts; the third is guaranteed by remaining elements
        for (int i = 0; i < arr.Length - 1; i++) {
            sum += arr[i];
            if (sum == target) {
                count++;
                sum = 0;
                if (count == 2) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canThreePartsEqualSum = function(arr) {
    const total = arr.reduce((s, v) => s + v, 0);
    if (total % 3 !== 0) return false;
    const target = total / 3;
    let sum = 0, parts = 0;
    // stop before the last element to ensure third part is non‑empty
    for (let i = 0; i < arr.length - 1; ++i) {
        sum += arr[i];
        if (sum === target) {
            parts++;
            sum = 0;
            if (parts === 2) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function canThreePartsEqualSum(arr: number[]): boolean {
    const total = arr.reduce((a, b) => a + b, 0);
    if (total % 3 !== 0) return false;
    const part = total / 3;

    let sum = 0;
    let i = -1;
    for (let idx = 0; idx < arr.length; idx++) {
        sum += arr[idx];
        if (sum === part) {
            i = idx;
            break;
        }
    }
    if (i === -1) return false;

    sum = 0;
    for (let j = i + 1; j < arr.length; j++) {
        sum += arr[j];
        if (sum === part && j < arr.length - 1) {
            return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canThreePartsEqualSum($arr) {
        $total = array_sum($arr);
        if ($total % 3 !== 0) {
            return false;
        }
        $target = intdiv($total, 3);
        $sum = 0;
        $count = 0;
        $n = count($arr);
        for ($i = 0; $i < $n - 1; $i++) {
            $sum += $arr[$i];
            if ($sum == $target) {
                $count++;
                $sum = 0;
                if ($count == 2) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canThreePartsEqualSum(_ arr: [Int]) -> Bool {
        let total = arr.reduce(0, +)
        if total % 3 != 0 { return false }
        let target = total / 3
        var sum = 0
        var partsFound = 0
        
        for i in 0..<arr.count {
            sum += arr[i]
            if sum == target {
                partsFound += 1
                sum = 0
                if partsFound == 2 && i < arr.count - 1 {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canThreePartsEqualSum(arr: IntArray): Boolean {
        val total = arr.sum()
        if (total % 3 != 0) return false
        val target = total / 3
        var sum = 0
        var partsFound = 0
        for (i in arr.indices) {
            sum += arr[i]
            if (sum == target) {
                partsFound++
                sum = 0
                if (partsFound == 2 && i < arr.lastIndex) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canThreePartsEqualSum(List<int> arr) {
    int total = 0;
    for (var num in arr) total += num;
    if (total % 3 != 0) return false;
    int target = total ~/ 3;
    int sum = 0, count = 0;
    // iterate up to second last element
    for (int i = 0; i < arr.length - 1; i++) {
      sum += arr[i];
      if (sum == target) {
        count++;
        sum = 0;
        if (count == 2) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func canThreePartsEqualSum(arr []int) bool {
    total := 0
    for _, v := range arr {
        total += v
    }
    if total%3 != 0 {
        return false
    }
    target := total / 3
    sum, parts := 0, 0
    // iterate up to len(arr)-1 to ensure the third part is non‑empty
    for i := 0; i < len(arr)-1; i++ {
        sum += arr[i]
        if sum == target {
            parts++
            sum = 0
        }
    }
    return parts >= 2
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def can_three_parts_equal_sum(arr)
  total = arr.sum
  return false unless total % 3 == 0
  target = total / 3
  prefix = 0
  count = 0
  n = arr.length
  arr.each_with_index do |val, idx|
    prefix += val
    if prefix == target && idx < n - 1
      count += 1
      return true if count >= 2
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def canThreePartsEqualSum(arr: Array[Int]): Boolean = {
        val total = arr.foldLeft(0L)(_ + _)
        if (total % 3 != 0) return false
        val target = total / 3
        var cur = 0L
        var parts = 0
        for (i <- 0 until arr.length - 1) {
            cur += arr(i).toLong
            if (cur == target) {
                parts += 1
                cur = 0L
                if (parts == 2) return true
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_three_parts_equal_sum(arr: Vec<i32>) -> bool {
        let total: i64 = arr.iter().map(|&x| x as i64).sum();
        if total % 3 != 0 {
            return false;
        }
        let target = total / 3;
        let mut cur = 0i64;
        let mut count = 0;
        for (i, &val) in arr.iter().enumerate() {
            cur += val as i64;
            if cur == target {
                count += 1;
                cur = 0;
                if count == 2 && i < arr.len() - 1 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (can-three-parts-equal-sum arr)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length arr))
         (total (apply + arr)))
    (if (not (= (remainder total 3) 0))
        #false
        (let ((target (/ total 3)))
          (letrec ((iter
                    (lambda (lst idx cum found-first)
                      (cond
                        [(null? lst) #false]
                        [else
                         (let* ((new-cum (+ cum (car lst)))
                                (new-idx (+ idx 1))
                                (found-first2 (if (and (not found-first)
                                                       (= new-cum target)
                                                       (<= new-idx (- n 3)))
                                                   #true
                                                   found-first)))
                           (cond
                             [(and found-first2
                                   (= new-cum (* 2 target))
                                   (<= new-idx (- n 2))) #true]
                             [else (iter (cdr lst) new-idx new-cum found-first2)]))])))
            (iter arr -1 0 #false))))))
```

## Erlang

```erlang
-module(solution).
-export([can_three_parts_equal_sum/1]).

-spec can_three_parts_equal_sum(Arr :: [integer()]) -> boolean().
can_three_parts_equal_sum(Arr) ->
    Total = lists:sum(Arr),
    case Total rem 3 of
        0 ->
            Target = Total div 3,
            can_partition(Arr, Target, 0, false);
        _ -> false
    end.

-spec can_partition([integer()], integer(), integer(), boolean()) -> boolean().
can_partition([], _, _, _) -> false;
can_partition([H|T], Target, CumSum, FirstFound) ->
    NewCum = CumSum + H,
    case {NewCum, FirstFound, T} of
        {Target, false, _} ->
            can_partition(T, Target, NewCum, true);
        {Sum, true, Rest} when Sum =:= 2*Target, Rest =/= [] ->
            true;
        _ ->
            can_partition(T, Target, NewCum, FirstFound)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_three_parts_equal_sum(arr :: [integer]) :: boolean
  def can_three_parts_equal_sum(arr) do
    total = Enum.sum(arr)

    if rem(total, 3) != 0 do
      false
    else
      target = div(total, 3)
      n = length(arr)

      {_sum, count} =
        Enum.reduce(Enum.with_index(arr), {0, 0}, fn {val, idx}, {sum, cnt} ->
          new_sum = sum + val

          new_cnt =
            if new_sum == target and idx < n - 1 do
              cnt + 1
            else
              cnt
            end

          {new_sum, new_cnt}
        end)

      count >= 2
    end
  end
end
```
