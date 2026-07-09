# 3158. Find the XOR of Numbers Which Appear Twice

## Cpp

```cpp
class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        int result = 0;
        int count[51] = {0};
        for (int num : nums) {
            ++count[num];
            if (count[num] == 2) {
                result ^= num;
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        java.util.HashSet<Integer> dup = new java.util.HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) {
                dup.add(num);
            }
        }
        int ans = 0;
        for (int v : dup) {
            ans ^= v;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = 0
        for num, cnt in freq.items():
            if cnt == 2:
                result ^= num
        return result
```

## Python3

```python
from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = 0
        for num, cnt in freq.items():
            if cnt == 2:
                result ^= num
        return result
```

## C

```c
int duplicateNumbersXOR(int* nums, int numsSize) {
    int count[51] = {0};
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= 1 && nums[i] <= 50)
            ++count[nums[i]];
    }
    int result = 0;
    for (int v = 1; v <= 50; ++v) {
        if (count[v] == 2)
            result ^= v;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int DuplicateNumbersXOR(int[] nums) {
        var seen = new HashSet<int>();
        int xorResult = 0;
        foreach (int num in nums) {
            if (seen.Contains(num)) {
                xorResult ^= num; // second occurrence
            } else {
                seen.Add(num);
            }
        }
        return xorResult;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var duplicateNumbersXOR = function(nums) {
    const seen = new Set();
    let xorResult = 0;
    for (const num of nums) {
        if (seen.has(num)) {
            xorResult ^= num;
        } else {
            seen.add(num);
        }
    }
    return xorResult;
};
```

## Typescript

```typescript
function duplicateNumbersXOR(nums: number[]): number {
    const seen = new Set<number>();
    let xorResult = 0;
    for (const num of nums) {
        if (seen.has(num)) {
            xorResult ^= num;
        } else {
            seen.add(num);
        }
    }
    return xorResult;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function duplicateNumbersXOR($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }

        $xor = 0;
        foreach ($freq as $num => $count) {
            if ($count == 2) {
                $xor ^= $num;
            }
        }

        return $xor;
    }
}
```

## Swift

```swift
class Solution {
    func duplicateNumbersXOR(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var result = 0
        for num in nums {
            if seen.contains(num) {
                result ^= num
            } else {
                seen.insert(num)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun duplicateNumbersXOR(nums: IntArray): Int {
        val seen = HashSet<Int>()
        var result = 0
        for (num in nums) {
            if (!seen.add(num)) {
                result = result xor num
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int duplicateNumbersXOR(List<int> nums) {
    int result = 0;
    final Set<int> seen = {};
    for (final num in nums) {
      if (seen.contains(num)) {
        result ^= num;
      } else {
        seen.add(num);
      }
    }
    return result;
  }
}
```

## Golang

```go
func duplicateNumbersXOR(nums []int) int {
    freq := make([]int, 51)
    for _, v := range nums {
        freq[v]++
    }
    xor := 0
    for num, cnt := range freq {
        if cnt == 2 {
            xor ^= num
        }
    }
    return xor
}
```

## Ruby

```ruby
def duplicate_numbers_xor(nums)
  counts = Hash.new(0)
  nums.each { |num| counts[num] += 1 }
  result = 0
  counts.each do |num, cnt|
    result ^= num if cnt == 2
  end
  result
end
```

## Scala

```scala
object Solution {
    def duplicateNumbersXOR(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        var result = 0
        for (num <- nums) {
            if (seen.contains(num)) {
                result ^= num
            } else {
                seen.add(num)
            }
        }
        result
    }
}
```

## Rust

```rust
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let mut xor_val = 0;
        for &num in nums.iter() {
            if !seen.insert(num) {
                xor_val ^= num;
            }
        }
        xor_val
    }
}
```

## Racket

```racket
(define/contract (duplicate-numbers-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for ([x nums])
      (hash-update! freq x add1 0))
    (let loop ((keys (hash-keys freq)) (acc 0))
      (if (null? keys)
          acc
          (let* ([k (car keys)]
                 [cnt (hash-ref freq k)])
            (loop (cdr keys) (if (= cnt 2) (bitwise-xor acc k) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([duplicate_numbers_xor/1]).

duplicate_numbers_xor(Nums) ->
    Freq = lists:foldl(
        fun(N, M) ->
            maps:update_with(N,
                             fun(C) -> C + 1 end,
                             1,
                             M)
        end,
        #{},
        Nums),
    maps:fold(
        fun(Key, Count, Acc) ->
            case Count of
                2 -> Acc bxor Key;
                _ -> Acc
            end
        end,
        0,
        Freq).
```

## Elixir

```elixir
defmodule Solution do
  @spec duplicate_numbers_xor(nums :: [integer]) :: integer
  def duplicate_numbers_xor(nums) do
    nums
    |> Enum.frequencies()
    |> Enum.reduce(0, fn {num, cnt}, acc ->
      if cnt == 2, do: Bitwise.bxor(acc, num), else: acc
    end)
  end
end
```
