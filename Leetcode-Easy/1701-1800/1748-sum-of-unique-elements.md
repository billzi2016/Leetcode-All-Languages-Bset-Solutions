# 1748. Sum of Unique Elements

## Cpp

```cpp
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int cnt[101] = {0};
        for (int x : nums) ++cnt[x];
        int sum = 0;
        for (int x : nums) {
            if (cnt[x] == 1) sum += x;
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int sumOfUnique(int[] nums) {
        int[] freq = new int[101];
        for (int num : nums) {
            freq[num]++;
        }
        int sum = 0;
        for (int i = 1; i <= 100; i++) {
            if (freq[i] == 1) {
                sum += i;
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        total = 0
        for num, count in freq.items():
            if count == 1:
                total += num
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sum(num for num, count in freq.items() if count == 1)
```

## C

```c
int sumOfUnique(int* nums, int numsSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]]++;
    }
    int sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (freq[nums[i]] == 1) {
            sum += nums[i];
        }
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution
{
    public int SumOfUnique(int[] nums)
    {
        var freq = new int[101];
        foreach (var num in nums)
        {
            freq[num]++;
        }

        int sum = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (freq[i] == 1)
                sum += i;
        }
        return sum;
    }
}
```

## Javascript

```javascript
var sumOfUnique = function(nums) {
    const freq = new Map();
    for (const n of nums) {
        freq.set(n, (freq.get(n) || 0) + 1);
    }
    let sum = 0;
    for (const [num, cnt] of freq.entries()) {
        if (cnt === 1) sum += num;
    }
    return sum;
};
```

## Typescript

```typescript
function sumOfUnique(nums: number[]): number {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    let total = 0;
    for (const [num, count] of freq.entries()) {
        if (count === 1) total += num;
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
    function sumOfUnique($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }
        $sum = 0;
        foreach ($freq as $value => $count) {
            if ($count === 1) {
                $sum += $value;
            }
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfUnique(_ nums: [Int]) -> Int {
        var frequency = [Int: Int]()
        for num in nums {
            frequency[num, default: 0] += 1
        }
        var result = 0
        for (num, count) in frequency where count == 1 {
            result += num
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfUnique(nums: IntArray): Int {
        val count = IntArray(101)
        for (num in nums) {
            count[num]++
        }
        var sum = 0
        for (num in nums) {
            if (count[num] == 1) sum += num
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int sumOfUnique(List<int> nums) {
    final Map<int, int> freq = {};
    for (final num in nums) {
      freq[num] = (freq[num] ?? 0) + 1;
    }
    int sum = 0;
    freq.forEach((key, value) {
      if (value == 1) sum += key;
    });
    return sum;
  }
}
```

## Golang

```go
func sumOfUnique(nums []int) int {
    freq := make(map[int]int, len(nums))
    for _, v := range nums {
        freq[v]++
    }
    sum := 0
    for v, c := range freq {
        if c == 1 {
            sum += v
        }
    }
    return sum
}
```

## Ruby

```ruby
def sum_of_unique(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  sum = 0
  freq.each { |num, count| sum += num if count == 1 }
  sum
end
```

## Scala

```scala
object Solution {
  def sumOfUnique(nums: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
    for (x <- nums) freq(x) += 1
    var sum = 0
    for ((num, count) <- freq if count == 1) sum += num
    sum
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        freq.into_iter()
            .filter(|(_, cnt)| cnt == 1)
            .map(|(val, _)| val)
            .sum()
    }
}
```

## Racket

```racket
(define/contract (sum-of-unique nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for ([n nums])
      (hash-update! freq n (lambda (v) (+ v 1)) 0))
    (for/sum ([kv (in-hash freq)]
              #:when (= (cdr kv) 1))
      (car kv))))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_unique/1]).

-spec sum_of_unique(Nums :: [integer()]) -> integer().
sum_of_unique(Nums) ->
    Freq = lists:foldl(fun(N, M) ->
                case maps:is_key(N, M) of
                    true -> maps:update_with(N, fun(C) -> C + 1 end, M);
                    false -> maps:put(N, 1, M)
                end
            end, #{}, Nums),
    maps:fold(fun(K, V, Sum) ->
                case V of
                    1 -> Sum + K;
                    _ -> Sum
                end
              end, 0, Freq).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_unique(nums :: [integer]) :: integer
  def sum_of_unique(nums) do
    nums
    |> Enum.frequencies()
    |> Enum.filter(fn {_k, v} -> v == 1 end)
    |> Enum.map(fn {k, _v} -> k end)
    |> Enum.sum()
  end
end
```
