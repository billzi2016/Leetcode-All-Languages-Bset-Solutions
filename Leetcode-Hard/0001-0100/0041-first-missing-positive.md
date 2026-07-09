# 0041. First Missing Positive

## Cpp

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ) {
            int val = nums[i];
            if (val > 0 && val <= n && nums[val - 1] != val) {
                swap(nums[i], nums[val - 1]);
            } else {
                ++i;
            }
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
};
```

## Java

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; ) {
            int correctIdx = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= n && nums[i] != nums[correctIdx]) {
                int temp = nums[i];
                nums[i] = nums[correctIdx];
                nums[correctIdx] = temp;
            } else {
                i++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return n + 1;
    }
}
```

## Python

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for idx, val in enumerate(nums):
            if val != idx + 1:
                return idx + 1
        return n + 1
```

## Python3

```python
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            v = nums[i]
            if 1 <= v <= n and nums[v - 1] != v:
                nums[i], nums[v - 1] = nums[v - 1], nums[i]
            else:
                i += 1
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1
        return n + 1
```

## C

```c
int firstMissingPositive(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        while (nums[i] >= 1 && nums[i] <= numsSize && nums[nums[i] - 1] != nums[i]) {
            int correctIdx = nums[i] - 1;
            int temp = nums[correctIdx];
            nums[correctIdx] = nums[i];
            nums[i] = temp;
        }
    }
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != i + 1) return i + 1;
    }
    return numsSize + 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int FirstMissingPositive(int[] nums)
    {
        int n = nums.Length;
        for (int i = 0; i < n;)
        {
            int correctIdx = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= n && nums[i] != nums[correctIdx])
            {
                int temp = nums[i];
                nums[i] = nums[correctIdx];
                nums[correctIdx] = temp;
            }
            else
            {
                i++;
            }
        }

        for (int i = 0; i < n; i++)
        {
            if (nums[i] != i + 1)
                return i + 1;
        }

        return n + 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        while (
            nums[i] > 0 &&
            nums[i] <= n &&
            nums[nums[i] - 1] !== nums[i]
        ) {
            const correctIdx = nums[i] - 1;
            // swap nums[i] and nums[correctIdx]
            const temp = nums[i];
            nums[i] = nums[correctIdx];
            nums[correctIdx] = temp;
        }
    }
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) {
            return i + 1;
        }
    }
    return n + 1;
};
```

## Typescript

```typescript
function firstMissingPositive(nums: number[]): number {
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        while (
            nums[i] > 0 &&
            nums[i] <= n &&
            nums[nums[i] - 1] !== nums[i]
        ) {
            const correctIdx = nums[i] - 1;
            [nums[i], nums[correctIdx]] = [nums[correctIdx], nums[i]];
        }
    }
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) {
            return i + 1;
        }
    }
    return n + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            while (
                $nums[$i] > 0 &&
                $nums[$i] <= $n &&
                $nums[$i] != $nums[$nums[$i] - 1]
            ) {
                $correctIdx = $nums[$i] - 1;
                // swap $nums[$i] and $nums[$correctIdx]
                $temp = $nums[$i];
                $nums[$i] = $nums[$correctIdx];
                $nums[$correctIdx] = $temp;
            }
        }

        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] != $i + 1) {
                return $i + 1;
            }
        }

        return $n + 1;
    }
}
```

## Swift

```swift
class Solution {
    func firstMissingPositive(_ nums: [Int]) -> Int {
        var a = nums
        let n = a.count
        var i = 0
        while i < n {
            let val = a[i]
            if val > 0 && val <= n && a[val - 1] != val {
                a.swapAt(i, val - 1)
            } else {
                i += 1
            }
        }
        for (idx, value) in a.enumerated() {
            if value != idx + 1 {
                return idx + 1
            }
        }
        return n + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun firstMissingPositive(nums: IntArray): Int {
        val n = nums.size
        var i = 0
        while (i < n) {
            val cur = nums[i]
            if (cur > 0 && cur <= n && nums[cur - 1] != cur) {
                // swap nums[i] with nums[cur - 1]
                val temp = nums[cur - 1]
                nums[cur - 1] = cur
                nums[i] = temp
            } else {
                i++
            }
        }
        for (j in 0 until n) {
            if (nums[j] != j + 1) return j + 1
        }
        return n + 1
    }
}
```

## Dart

```dart
class Solution {
  int firstMissingPositive(List<int> nums) {
    int n = nums.length;
    for (int i = 0; i < n;) {
      int val = nums[i];
      int correctIdx = val - 1;
      if (val > 0 && val <= n && nums[i] != nums[correctIdx]) {
        // swap nums[i] with nums[correctIdx]
        int temp = nums[i];
        nums[i] = nums[correctIdx];
        nums[correctIdx] = temp;
      } else {
        i++;
      }
    }

    for (int i = 0; i < n; i++) {
      if (nums[i] != i + 1) {
        return i + 1;
      }
    }
    return n + 1;
  }
}
```

## Golang

```go
func firstMissingPositive(nums []int) int {
    n := len(nums)
    for i := 0; i < n; {
        v := nums[i]
        if v > 0 && v <= n && nums[v-1] != v {
            nums[i], nums[v-1] = nums[v-1], nums[i]
        } else {
            i++
        }
    }
    for i := 0; i < n; i++ {
        if nums[i] != i+1 {
            return i + 1
        }
    }
    return n + 1
}
```

## Ruby

```ruby
def first_missing_positive(nums)
  n = nums.length
  i = 0
  while i < n
    val = nums[i]
    if val > 0 && val <= n && nums[val - 1] != val
      nums[i], nums[val - 1] = nums[val - 1], nums[i]
    else
      i += 1
    end
  end

  (0...n).each do |idx|
    return idx + 1 if nums[idx] != idx + 1
  end
  n + 1
end
```

## Scala

```scala
object Solution {
  def firstMissingPositive(nums: Array[Int]): Int = {
    val n = nums.length
    var i = 0
    while (i < n) {
      val v = nums(i)
      if (v > 0 && v <= n && nums(v - 1) != v) {
        val tmp = nums(v - 1)
        nums(v - 1) = v
        nums(i) = tmp
      } else {
        i += 1
      }
    }
    var j = 0
    while (j < n) {
      if (nums(j) != j + 1) return j + 1
      j += 1
    }
    n + 1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        for i in 0..n {
            while nums[i] > 0 && (nums[i] as usize) <= n {
                let correct_idx = (nums[i] - 1) as usize;
                if nums[correct_idx] == nums[i] {
                    break;
                }
                nums.swap(i, correct_idx);
            }
        }

        for i in 0..n {
            if nums[i] != (i as i32 + 1) {
                return i as i32 + 1;
            }
        }
        n as i32 + 1
    }
}
```

## Racket

```racket
(define/contract (first-missing-positive nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    ;; Cycle sort in‑place
    (let loop ((i 0))
      (when (< i n)
        (let ((val (vector-ref v i)))
          (if (and (> val 0) (<= val n)
                   (not (= val (vector-ref v (- val 1)))))
              (begin
                (let* ((target-index (- val 1))
                       (temp val))
                  (vector-set! v i (vector-ref v target-index))
                  (vector-set! v target-index temp)
                  (loop i))) ; re‑check the new value at position i
              (loop (+ i 1))))))
    ;; Find first missing positive
    (let search ((i 0))
      (if (= i n)
          (+ n 1)
          (if (= (vector-ref v i) (+ i 1))
              (search (+ i 1))
              (+ i 1))))))
```

## Erlang

```erlang
-module(solution).
-export([first_missing_positive/1]).

-spec first_missing_positive(Nums :: [integer()]) -> integer().
first_missing_positive(Nums) ->
    Len = length(Nums),
    Max = Len + 1,
    Set = build_set(Nums, Max, #{}),
    find_missing(1, Max, Set).

build_set([], _Max, Acc) -> Acc;
build_set([H|T], Max, Acc) when H > 0, H =< Max ->
    build_set(T, Max, maps:put(H, true, Acc));
build_set([_|T], Max, Acc) ->
    build_set(T, Max, Acc).

find_missing(I, Max, Set) when I =< Max ->
    case maps:is_key(I, Set) of
        true -> find_missing(I + 1, Max, Set);
        false -> I
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec first_missing_positive(nums :: [integer]) :: integer
  def first_missing_positive(nums) do
    n = length(nums)

    set =
      Enum.reduce(nums, MapSet.new(), fn x, acc ->
        if x > 0 and x <= n do
          MapSet.put(acc, x)
        else
          acc
        end
      end)

    missing = Enum.find(1..n, fn i -> not MapSet.member?(set, i) end)

    case missing do
      nil -> n + 1
      val -> val
    end
  end
end
```
