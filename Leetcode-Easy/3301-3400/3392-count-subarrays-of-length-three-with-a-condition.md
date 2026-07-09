# 3392. Count Subarrays of Length Three With a Condition

## Cpp

```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 1; i + 1 < n; ++i) {
            if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
                ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countSubarrays(int[] nums) {
        int count = 0;
        for (int i = 1; i < nums.length - 1; i++) {
            if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
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
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]):
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]):
                ans += 1
        return ans
```

## C

```c
int countSubarrays(int* nums, int numsSize) {
    int count = 0;
    for (int i = 1; i + 1 < numsSize; ++i) {
        if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountSubarrays(int[] nums) {
        int count = 0;
        for (int i = 1; i < nums.Length - 1; i++) {
            if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function(nums) {
    let count = 0;
    for (let i = 1; i < nums.length - 1; ++i) {
        if (nums[i] === 2 * (nums[i - 1] + nums[i + 1])) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countSubarrays(nums: number[]): number {
    let ans = 0;
    for (let i = 1; i + 1 < nums.length; ++i) {
        if (nums[i] === 2 * (nums[i - 1] + nums[i + 1])) {
            ans++;
        }
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
    function countSubarrays($nums) {
        $n = count($nums);
        $cnt = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i] == 2 * ($nums[$i - 1] + $nums[$i + 1])) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int]) -> Int {
        var count = 0
        let n = nums.count
        if n < 3 { return 0 }
        for i in 1..<(n - 1) {
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]) {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray): Int {
        var count = 0
        for (i in 1 until nums.size - 1) {
            if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countSubarrays(List<int> nums) {
    int ans = 0;
    for (int i = 1; i < nums.length - 1; ++i) {
      if (nums[i] == 2 * (nums[i - 1] + nums[i + 1])) {
        ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countSubarrays(nums []int) int {
    cnt := 0
    for i := 1; i+1 < len(nums); i++ {
        if nums[i] == 2*(nums[i-1]+nums[i+1]) {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_subarrays(nums)
  count = 0
  (1...nums.length - 1).each do |i|
    count += 1 if nums[i] == (nums[i - 1] + nums[i + 1]) * 2
  end
  count
end
```

## Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int]): Int = {
        var count = 0
        for (i <- 1 until nums.length - 1) {
            if (nums(i) == 2 * (nums(i - 1) + nums(i + 1))) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut cnt = 0;
        for i in 1..n - 1 {
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]) {
                cnt += 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i 1) (cnt 0))
      (if (> i (- n 2))
          cnt
          (loop (+ i 1)
                (if (= (vector-ref v i)
                       (* 2 (+ (vector-ref v (- i 1))
                               (vector-ref v (+ i 1)))))
                    (+ cnt 1)
                    cnt))))))
```

## Erlang

```erlang
-spec count_subarrays(Nums :: [integer()]) -> integer().
count_subarrays(Nums) ->
    count_subarrays(Nums, 0).

count_subarrays([A,B,C|Rest], Acc) ->
    NewAcc = case B =:= 2 * (A + C) of
                true -> Acc + 1;
                false -> Acc
            end,
    count_subarrays([B,C|Rest], NewAcc);
count_subarrays(_, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer]) :: integer
  def count_subarrays(nums) do
    len = length(nums)

    Enum.reduce(1..(len - 2), 0, fn i, acc ->
      a = Enum.at(nums, i - 1)
      b = Enum.at(nums, i)
      c = Enum.at(nums, i + 1)

      if b == 2 * (a + c) do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
