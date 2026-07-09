# 2455. Average Value of Even Numbers That Are Divisible by Three

## Cpp

```cpp
class Solution {
public:
    int averageValue(vector<int>& nums) {
        long long sum = 0;
        int cnt = 0;
        for (int x : nums) {
            if (x % 6 == 0) {
                sum += x;
                ++cnt;
            }
        }
        return cnt ? static_cast<int>(sum / cnt) : 0;
    }
};
```

## Java

```java
class Solution {
    public int averageValue(int[] nums) {
        int sum = 0;
        int count = 0;
        for (int num : nums) {
            if (num % 6 == 0) { // divisible by both 2 and 3
                sum += num;
                count++;
            }
        }
        return count == 0 ? 0 : sum / count;
    }
}
```

## Python

```python
class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cnt = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                cnt += 1
        return total // cnt if cnt else 0
```

## Python3

```python
from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        cnt = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                cnt += 1
        return total // cnt if cnt else 0
```

## C

```c
int averageValue(int* nums, int numsSize) {
    int sum = 0;
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % 6 == 0) {
            sum += nums[i];
            ++count;
        }
    }
    return count ? sum / count : 0;
}
```

## Csharp

```csharp
public class Solution {
    public int AverageValue(int[] nums) {
        int sum = 0;
        int cnt = 0;
        foreach (int num in nums) {
            if (num % 6 == 0) {
                sum += num;
                cnt++;
            }
        }
        return cnt == 0 ? 0 : sum / cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let sum = 0;
    let count = 0;
    for (const num of nums) {
        if (num % 6 === 0) {
            sum += num;
            count++;
        }
    }
    return count === 0 ? 0 : Math.floor(sum / count);
};
```

## Typescript

```typescript
function averageValue(nums: number[]): number {
    let sum = 0;
    let count = 0;
    for (const num of nums) {
        if (num % 6 === 0) {
            sum += num;
            count++;
        }
    }
    return count === 0 ? 0 : Math.floor(sum / count);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function averageValue($nums) {
        $sum = 0;
        $count = 0;
        foreach ($nums as $num) {
            if ($num % 6 === 0) {
                $sum += $num;
                $count++;
            }
        }
        if ($count === 0) {
            return 0;
        }
        return intdiv($sum, $count);
    }
}
```

## Swift

```swift
class Solution {
    func averageValue(_ nums: [Int]) -> Int {
        var sum = 0
        var count = 0
        for num in nums {
            if num % 6 == 0 {
                sum += num
                count += 1
            }
        }
        return count == 0 ? 0 : sum / count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun averageValue(nums: IntArray): Int {
        var sum = 0
        var count = 0
        for (num in nums) {
            if (num % 6 == 0) {
                sum += num
                count++
            }
        }
        return if (count == 0) 0 else sum / count
    }
}
```

## Dart

```dart
class Solution {
  int averageValue(List<int> nums) {
    int sum = 0;
    int cnt = 0;
    for (int num in nums) {
      if (num % 6 == 0) {
        sum += num;
        cnt++;
      }
    }
    return cnt == 0 ? 0 : sum ~/ cnt;
  }
}
```

## Golang

```go
func averageValue(nums []int) int {
    sum, cnt := 0, 0
    for _, v := range nums {
        if v%6 == 0 {
            sum += v
            cnt++
        }
    }
    if cnt == 0 {
        return 0
    }
    return sum / cnt
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def average_value(nums)
  sum = 0
  cnt = 0
  nums.each do |num|
    if num % 6 == 0
      sum += num
      cnt += 1
    end
  end
  cnt.zero? ? 0 : sum / cnt
end
```

## Scala

```scala
object Solution {
    def averageValue(nums: Array[Int]): Int = {
        var sum = 0
        var count = 0
        for (num <- nums) {
            if (num % 6 == 0) {
                sum += num
                count += 1
            }
        }
        if (count == 0) 0 else sum / count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn average_value(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        let mut count = 0;
        for &num in nums.iter() {
            if num % 6 == 0 {
                sum += num;
                count += 1;
            }
        }
        if count == 0 { 0 } else { sum / count }
    }
}
```

## Racket

```racket
(define/contract (average-value nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((filtered (filter (lambda (x) (zero? (modulo x 6))) nums))
         (cnt (length filtered)))
    (if (= cnt 0)
        0
        (quotient (apply + filtered) cnt))))
```

## Erlang

```erlang
-module(solution).
-export([average_value/1]).

-spec average_value(Nums :: [integer()]) -> integer().
average_value(Nums) ->
    Filtered = [N || N <- Nums, N rem 6 =:= 0],
    case length(Filtered) of
        0 -> 0;
        Count ->
            Sum = lists:sum(Filtered),
            Sum div Count
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec average_value(nums :: [integer]) :: integer
  def average_value(nums) do
    {sum, count} =
      Enum.reduce(nums, {0, 0}, fn x, {s, c} ->
        if rem(x, 6) == 0 do
          {s + x, c + 1}
        else
          {s, c}
        end
      end)

    if count == 0, do: 0, else: div(sum, count)
  end
end
```
