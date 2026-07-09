# 2348. Number of Zero-Filled Subarrays

## Cpp

```cpp
class Solution {
public:
    long long zeroFilledSubarray(std::vector<int>& nums) {
        long long ans = 0;
        long long cur = 0;
        for (int x : nums) {
            if (x == 0) {
                ++cur;
                ans += cur;
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long result = 0;
        long consecutive = 0;
        for (int num : nums) {
            if (num == 0) {
                consecutive++;
                result += consecutive;
            } else {
                consecutive = 0;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        consecutive = 0
        for v in nums:
            if v == 0:
                consecutive += 1
                total += consecutive
            else:
                consecutive = 0
        return total
```

## Python3

```python
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for v in nums:
            if v == 0:
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans
```

## C

```c
long long zeroFilledSubarray(int* nums, int numsSize) {
    long long ans = 0;
    long long cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 0) {
            ++cur;
            ans += cur;
        } else {
            cur = 0;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long ZeroFilledSubarray(int[] nums)
    {
        long total = 0;
        long consecutiveZeros = 0;
        foreach (int num in nums)
        {
            if (num == 0)
            {
                consecutiveZeros++;
                total += consecutiveZeros;
            }
            else
            {
                consecutiveZeros = 0;
            }
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let count = 0;
    let result = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            count += 1;
            result += count;
        } else {
            count = 0;
        }
    }
    return result;
};
```

## Typescript

```typescript
function zeroFilledSubarray(nums: number[]): number {
    let total = 0;
    let consecutiveZeros = 0;
    for (const num of nums) {
        if (num === 0) {
            consecutiveZeros++;
            total += consecutiveZeros;
        } else {
            consecutiveZeros = 0;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function zeroFilledSubarray($nums) {
        $cnt = 0;
        $ans = 0;
        foreach ($nums as $v) {
            if ($v == 0) {
                $cnt++;
                $ans += $cnt;
            } else {
                $cnt = 0;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func zeroFilledSubarray(_ nums: [Int]) -> Int {
        var consecutiveZeros = 0
        var total: Int64 = 0
        for num in nums {
            if num == 0 {
                consecutiveZeros += 1
                total += Int64(consecutiveZeros)
            } else {
                consecutiveZeros = 0
            }
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun zeroFilledSubarray(nums: IntArray): Long {
        var total = 0L
        var consecutive = 0L
        for (num in nums) {
            if (num == 0) {
                consecutive++
                total += consecutive
            } else {
                consecutive = 0L
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int zeroFilledSubarray(List<int> nums) {
    int count = 0;
    int result = 0;
    for (int num in nums) {
      if (num == 0) {
        count++;
        result += count;
      } else {
        count = 0;
      }
    }
    return result;
  }
}
```

## Golang

```go
func zeroFilledSubarray(nums []int) int64 {
	var ans int64
	cnt := 0
	for _, v := range nums {
		if v == 0 {
			cnt++
			ans += int64(cnt)
		} else {
			cnt = 0
		}
	}
	return ans
}
```

## Ruby

```ruby
def zero_filled_subarray(nums)
  total = 0
  consecutive = 0
  nums.each do |x|
    if x == 0
      consecutive += 1
      total += consecutive
    else
      consecutive = 0
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def zeroFilledSubarray(nums: Array[Int]): Long = {
        var total: Long = 0L
        var consecutive: Long = 0L
        for (num <- nums) {
            if (num == 0) {
                consecutive += 1
                total += consecutive
            } else {
                consecutive = 0L
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {
        let mut consecutive = 0i64;
        let mut total = 0i64;
        for &num in nums.iter() {
            if num == 0 {
                consecutive += 1;
            } else {
                consecutive = 0;
            }
            total += consecutive;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (zero-filled-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (cnt 0) (ans 0))
    (if (null? lst)
        ans
        (let* ((x (car lst))
               (new-cnt (if (= x 0) (+ cnt 1) 0))
               (new-ans (+ ans new-cnt)))
          (loop (cdr lst) new-cnt new-ans)))))
```

## Erlang

```erlang
-spec zero_filled_subarray(Nums :: [integer()]) -> integer().
zero_filled_subarray(Nums) ->
    {Total, _} = lists:foldl(
        fun(Elem, {Sum, Cur}) ->
            case Elem of
                0 -> NewCur = Cur + 1,
                     {Sum + NewCur, NewCur};
                _ -> {Sum, 0}
            end
        end,
        {0, 0},
        Nums),
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec zero_filled_subarray(nums :: [integer]) :: integer
  def zero_filled_subarray(nums) do
    {result, _} =
      Enum.reduce(nums, {0, 0}, fn x, {acc, cur} ->
        if x == 0 do
          new_cur = cur + 1
          {acc + new_cur, new_cur}
        else
          {acc, 0}
        end
      end)

    result
  end
end
```
