# 2789. Largest Element in an Array after Merge Operations

## Cpp

```cpp
class Solution {
public:
    long long maxArrayValue(vector<int>& nums) {
        long long cur = nums.back();
        long long ans = cur;
        for (int i = (int)nums.size() - 2; i >= 0; --i) {
            if (nums[i] <= cur) {
                cur += nums[i];
            } else {
                cur = nums[i];
            }
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxArrayValue(int[] nums) {
        int n = nums.length;
        long cur = nums[n - 1];
        long ans = cur;
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] <= cur) {
                cur += nums[i];
            } else {
                ans = Math.max(ans, cur);
                cur = nums[i];
            }
        }
        ans = Math.max(ans, cur);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur = nums[-1]
        ans = cur
        for i in range(n - 2, -1, -1):
            if nums[i] <= cur:
                cur += nums[i]
            else:
                ans = max(ans, cur)
                cur = nums[i]
        return max(ans, cur)
```

## Python3

```python
from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        cur = nums[-1]
        ans = cur
        for x in reversed(nums[:-1]):
            if x <= cur:
                cur += x
            else:
                cur = x
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
long long maxArrayValue(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    long long cur = nums[numsSize - 1];
    long long ans = cur;
    for (int i = numsSize - 2; i >= 0; --i) {
        if ((long long)nums[i] <= cur) {
            cur += nums[i];
        } else {
            if (cur > ans) ans = cur;
            cur = nums[i];
        }
    }
    if (cur > ans) ans = cur;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxArrayValue(int[] nums) {
        int n = nums.Length;
        long cur = nums[n - 1];
        long ans = cur;
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] <= cur) {
                cur += nums[i];
            } else {
                if (cur > ans) ans = cur;
                cur = nums[i];
            }
        }
        if (cur > ans) ans = cur;
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxArrayValue = function(nums) {
    const n = nums.length;
    let cur = nums[n - 1];
    let ans = cur;
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] <= cur) {
            cur += nums[i];
        } else {
            if (cur > ans) ans = cur;
            cur = nums[i];
        }
    }
    return Math.max(ans, cur);
};
```

## Typescript

```typescript
function maxArrayValue(nums: number[]): number {
    let n = nums.length;
    if (n === 0) return 0;
    let cur = nums[n - 1];
    let ans = cur;
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] <= cur) {
            cur += nums[i];
        } else {
            cur = nums[i];
        }
        if (cur > ans) ans = cur;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxArrayValue($nums) {
        $n = count($nums);
        $cur = $nums[$n - 1];
        $ans = $cur;
        for ($i = $n - 2; $i >= 0; --$i) {
            if ($nums[$i] <= $cur) {
                $cur += $nums[$i];
            } else {
                $cur = $nums[$i];
            }
            if ($cur > $ans) {
                $ans = $cur;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxArrayValue(_ nums: [Int]) -> Int {
        var cur = nums.last!
        var ans = cur
        if nums.count == 1 { return ans }
        for i in stride(from: nums.count - 2, through: 0, by: -1) {
            if nums[i] <= cur {
                cur += nums[i]
            } else {
                cur = nums[i]
            }
            if cur > ans {
                ans = cur
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxArrayValue(nums: IntArray): Long {
        val n = nums.size
        var cur = nums[n - 1].toLong()
        var ans = cur
        for (i in n - 2 downTo 0) {
            if (nums[i].toLong() <= cur) {
                cur += nums[i]
            } else {
                cur = nums[i].toLong()
            }
            if (cur > ans) ans = cur
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxArrayValue(List<int> nums) {
    int n = nums.length;
    int cur = nums[n - 1];
    int ans = cur;
    for (int i = n - 2; i >= 0; --i) {
      if (nums[i] <= cur) {
        cur += nums[i];
      } else {
        cur = nums[i];
      }
      if (cur > ans) ans = cur;
    }
    return ans;
  }
}
```

## Golang

```go
func maxArrayValue(nums []int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }
    cur := int64(nums[n-1])
    ans := cur
    for i := n - 2; i >= 0; i-- {
        v := int64(nums[i])
        if v <= cur {
            cur += v
        } else {
            cur = v
        }
        if cur > ans {
            ans = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_array_value(nums)
  cur = nums[-1]
  ans = cur
  (nums.length - 2).downto(0) do |i|
    if nums[i] <= cur
      cur += nums[i]
    else
      cur = nums[i]
    end
    ans = cur if cur > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxArrayValue(nums: Array[Int]): Long = {
        val n = nums.length
        var cur: Long = nums(n - 1).toLong
        var ans: Long = cur
        var i = n - 2
        while (i >= 0) {
            val v = nums(i).toLong
            if (v <= cur) {
                cur += v
            } else {
                cur = v
            }
            if (cur > ans) ans = cur
            i -= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_array_value(nums: Vec<i32>) -> i64 {
        let mut cur = *nums.last().unwrap() as i64;
        let mut ans = cur;
        for &v in nums.iter().rev().skip(1) {
            let x = v as i64;
            if x <= cur {
                cur += x;
            } else {
                cur = x;
            }
            if cur > ans {
                ans = cur;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-array-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (if (= n 0)
        0
        (let loop ((i (- n 2))
                   (cur (vector-ref v (- n 1)))
                   (ans (vector-ref v (- n 1))))
          (if (< i 0)
              ans
              (let* ((val (vector-ref v i))
                     (new-cur (if (<= val cur) (+ cur val) val))
                     (new-ans (max ans new-cur)))
                (loop (- i 1) new-cur new-ans)))))))
```

## Erlang

```erlang
-spec max_array_value(Nums :: [integer()]) -> integer().
max_array_value(Nums) ->
    Rev = lists:reverse(Nums),
    case Rev of
        [] -> 0;
        [First|Rest] ->
            process(Rest, First, First)
    end.

process([], _Cur, Max) ->
    Max;
process([X|Xs], Cur, Max) ->
    if X =< Cur ->
            NewCur = X + Cur,
            NewMax = erlang:max(NewCur, Max),
            process(Xs, NewCur, NewMax);
       true ->
            NewCur = X,
            NewMax = erlang:max(NewCur, Max),
            process(Xs, NewCur, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_array_value(nums :: [integer]) :: integer
  def max_array_value(nums) do
    [last | rest] = Enum.reverse(nums)

    {_cur, answer} =
      Enum.reduce(rest, {last, last}, fn x, {cur, ans} ->
        new_cur = if x <= cur, do: cur + x, else: x
        new_ans = max(ans, new_cur)
        {new_cur, new_ans}
      end)

    answer
  end
end
```
