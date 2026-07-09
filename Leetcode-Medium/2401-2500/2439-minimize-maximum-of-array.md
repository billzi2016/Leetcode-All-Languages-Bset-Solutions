# 2439. Minimize Maximum of Array

## Cpp

```cpp
class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        long long sum = 0;
        long long ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            sum += nums[i];
            long long cur = (sum + i) / (i + 1); // ceil division
            if (cur > ans) ans = cur;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int minimizeArrayValue(int[] nums) {
        long sum = 0;
        long answer = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            long cur = (sum + i) / (i + 1); // ceil division of prefix average
            if (cur > answer) {
                answer = cur;
            }
        }
        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        prefix_sum = 0
        for i, v in enumerate(nums):
            prefix_sum += v
            # ceiling of average = (sum + length - 1) // length
            cur = (prefix_sum + i) // (i + 1)
            if cur > max_val:
                max_val = cur
        return max_val
```

## Python3

```python
from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        ans = 0
        for i, v in enumerate(nums):
            total += v
            cur = (total + i) // (i + 1)  # ceil division
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
int minimizeArrayValue(int* nums, int numsSize) {
    long long prefixSum = 0;
    long long answer = 0;
    for (int i = 0; i < numsSize; ++i) {
        prefixSum += nums[i];
        long long cur = (prefixSum + i) / (i + 1); // ceiling division
        if (cur > answer) answer = cur;
    }
    return (int)answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimizeArrayValue(int[] nums) {
        long sum = 0;
        long answer = 0;
        for (int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            long cur = (sum + i) / (i + 1); // ceil division
            if (cur > answer) answer = cur;
        }
        return (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeArrayValue = function(nums) {
    let maxVal = 0;
    let prefixSum = 0;
    for (let i = 0; i < nums.length; ++i) {
        prefixSum += nums[i];
        // ceil(prefixSum / (i + 1)) using integer arithmetic
        const cur = Math.floor((prefixSum + i) / (i + 1));
        if (cur > maxVal) maxVal = cur;
    }
    return maxVal;
};
```

## Typescript

```typescript
function minimizeArrayValue(nums: number[]): number {
    let sum = 0;
    let answer = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        // ceil division of sum / (i + 1)
        const cur = Math.floor((sum + i) / (i + 1));
        if (cur > answer) answer = cur;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimizeArrayValue($nums) {
        $sum = 0;
        $ans = 0;
        foreach ($nums as $i => $val) {
            $sum += $val;
            // ceil division of sum / (i+1)
            $candidate = intdiv($sum + $i, $i + 1);
            if ($candidate > $ans) {
                $ans = $candidate;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeArrayValue(_ nums: [Int]) -> Int {
        var sum: Int64 = 0
        var answer: Int64 = 0
        for (index, value) in nums.enumerated() {
            sum += Int64(value)
            let i = Int64(index)
            // ceil division of sum / (i+1)
            let cur = (sum + i) / (i + 1)
            if cur > answer {
                answer = cur
            }
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeArrayValue(nums: IntArray): Int {
        var sum = 0L
        var ans = 0L
        for (i in nums.indices) {
            sum += nums[i].toLong()
            val len = i + 1L
            val cur = (sum + len - 1) / len // ceil of average
            if (cur > ans) ans = cur
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimizeArrayValue(List<int> nums) {
    int sum = 0;
    int answer = 0;
    for (int i = 0; i < nums.length; ++i) {
      sum += nums[i];
      int cur = ((sum + i) ~/ (i + 1));
      if (cur > answer) answer = cur;
    }
    return answer;
  }
}
```

## Golang

```go
func minimizeArrayValue(nums []int) int {
    var sum int64
    ans := 0
    for i, v := range nums {
        sum += int64(v)
        cur := int((sum + int64(i)) / int64(i+1))
        if cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimize_array_value(nums)
  max_val = 0
  sum = 0
  nums.each_with_index do |v, i|
    sum += v
    k = i + 1
    cur = (sum + k - 1) / k
    max_val = cur if cur > max_val
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def minimizeArrayValue(nums: Array[Int]): Int = {
        var sum: Long = 0L
        var ans: Long = 0L
        for (i <- nums.indices) {
            sum += nums(i).toLong
            val avgCeil = (sum + i) / (i + 1)
            if (avgCeil > ans) ans = avgCeil
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        let mut sum: i64 = 0;
        let mut ans: i64 = 0;
        for (i, &v) in nums.iter().enumerate() {
            sum += v as i64;
            let len = (i + 1) as i64;
            let cur = (sum + len - 1) / len; // ceil division
            if cur > ans {
                ans = cur;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (minimize-array-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums)))
    (let loop ((i -1) (pref-sum 0) (best 0))
      (if (= i (sub1 n))
          best
          (let* ((next-i (+ i 1))
                 (new-sum (+ pref-sum (list-ref nums next-i)))
                 (candidate (quotient (+ new-sum next-i) (+ next-i 1)))) ; ceil division
            (loop next-i new-sum (max best candidate)))))))
```

## Erlang

```erlang
-spec minimize_array_value(Nums :: [integer()]) -> integer().
minimize_array_value(Nums) ->
    {_,Ans} = lists:foldl(
        fun({Num,Idx},{Sum,CurMax}) ->
            NewSum = Sum + Num,
            Needed = (NewSum + Idx) div (Idx + 1),
            {NewSum, erlang:max(CurMax, Needed)}
        end,
        {0,0},
        lists:zip(Nums, lists:seq(0, length(Nums) - 1))
    ),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_array_value(nums :: [integer]) :: integer
  def minimize_array_value(nums) do
    {max_val, _} =
      Enum.reduce(Enum.with_index(nums), {0, 0}, fn {val, idx}, {cur_max, sum} ->
        new_sum = sum + val
        len = idx + 1
        needed = div(new_sum + len - 1, len)  # ceil division
        {max(cur_max, needed), new_sum}
      end)

    max_val
  end
end
```
