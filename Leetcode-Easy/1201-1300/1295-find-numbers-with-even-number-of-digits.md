# 1295. Find Numbers with Even Number of Digits

## Cpp

```cpp
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int cnt = 0;
        for (int x : nums) {
            if ((x >= 10 && x <= 99) ||
                (x >= 1000 && x <= 9999) ||
                x == 100000)
                ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if ((num >= 10 && num <= 99) ||
                (num >= 1000 && num <= 9999) ||
                num == 100000) {
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
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if (10 <= num < 100) or (1000 <= num < 10000) or num == 100000:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
```

## C

```c
int findNumbers(int* nums, int numsSize) {
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        int n = nums[i];
        if ((n >= 10 && n <= 99) || (n >= 1000 && n <= 9999) || n == 100000) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindNumbers(int[] nums)
    {
        int count = 0;
        foreach (int num in nums)
        {
            if ((num >= 10 && num <= 99) ||
                (num >= 1000 && num <= 9999) ||
                num == 100000)
            {
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
var findNumbers = function(nums) {
    let evenCount = 0;
    for (let num of nums) {
        let digits = 0;
        while (num > 0) {
            digits++;
            num = Math.trunc(num / 10);
        }
        if ((digits & 1) === 0) {
            evenCount++;
        }
    }
    return evenCount;
};
```

## Typescript

```typescript
function findNumbers(nums: number[]): number {
    let count = 0;
    for (const n of nums) {
        if ((n >= 10 && n < 100) || (n >= 1000 && n < 10000) || n === 100000) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNumbers($nums) {
        $evenCount = 0;
        foreach ($nums as $num) {
            // Convert to string and check length parity
            if ((strlen((string)$num) & 1) === 0) {
                $evenCount++;
            }
        }
        return $evenCount;
    }
}
```

## Swift

```swift
class Solution {
    func findNumbers(_ nums: [Int]) -> Int {
        var result = 0
        for num in nums {
            var n = num
            var digits = 0
            while n > 0 {
                digits += 1
                n /= 10
            }
            if digits % 2 == 0 {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findNumbers(nums: IntArray): Int {
        var count = 0
        for (num in nums) {
            when (num) {
                in 10..99, in 1000..9999, 100000 -> count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int findNumbers(List<int> nums) {
    int count = 0;
    for (int num in nums) {
      if ((num >= 10 && num <= 99) ||
          (num >= 1000 && num <= 9999) ||
          num == 100000) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func findNumbers(nums []int) int {
    count := 0
    for _, v := range nums {
        if (v >= 10 && v <= 99) || (v >= 1000 && v <= 9999) || v == 100000 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def find_numbers(nums)
  count = 0
  nums.each do |num|
    if (num >= 10 && num <= 99) || (num >= 1000 && num <= 9999) || num == 100000
      count += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def findNumbers(nums: Array[Int]): Int = {
        var count = 0
        for (num <- nums) {
            var n = num
            var digits = 0
            while (n > 0) {
                digits += 1
                n /= 10
            }
            if ((digits & 1) == 0) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut even_count = 0;
        for num in nums {
            let mut n = num;
            if n == 0 {
                // Zero has one digit (odd), skip counting
                continue;
            }
            let mut digits = 0;
            while n > 0 {
                digits += 1;
                n /= 10;
            }
            if digits % 2 == 0 {
                even_count += 1;
            }
        }
        even_count
    }
}
```

## Racket

```racket
(define/contract (find-numbers nums)
  (-> (listof exact-integer?) exact-integer?)
  (foldl (lambda (n acc)
           (+ acc (if (or (and (>= n 10) (<= n 99))
                         (and (>= n 1000) (<= n 9999))
                         (= n 100000))
                    1
                    0)))
         0
         nums))
```

## Erlang

```erlang
-spec find_numbers([integer()]) -> integer().
find_numbers(Nums) ->
    lists:foldl(
        fun(N, Acc) ->
            case N of
                _ when (N >= 10 andalso N =< 99) orelse (N >= 1000 andalso N =< 9999) orelse N == 100000 -> Acc + 1;
                _ -> Acc
            end
        end,
        0,
        Nums
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_numbers(nums :: [integer]) :: integer
  def find_numbers(nums) do
    Enum.count(nums, fn n ->
      (n >= 10 and n <= 99) or
        (n >= 1000 and n <= 9999) or
        n == 100_000
    end)
  end
end
```
