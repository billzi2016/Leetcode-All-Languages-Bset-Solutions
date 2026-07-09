# 2917. Find the K-or of an Array

## Cpp

```cpp
class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        int ans = 0;
        for (int bit = 0; bit < 31; ++bit) {
            int mask = 1 << bit;
            int cnt = 0;
            for (int x : nums) {
                if (x & mask) ++cnt;
                if (cnt >= k) break;
            }
            if (cnt >= k) ans |= mask;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findKOr(int[] nums, int k) {
        int result = 0;
        for (int bit = 0; bit < 31; bit++) {
            int mask = 1 << bit;
            int count = 0;
            for (int num : nums) {
                if ((num & mask) != 0) {
                    count++;
                }
            }
            if (count >= k) {
                result |= mask;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        for bit in range(32):  # considering non-negative ints < 2^31
            mask = 1 << bit
            cnt = sum(1 for x in nums if x & mask)
            if cnt >= k:
                result |= mask
        return result
```

## Python3

```python
from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit in range(31):  # numbers are < 2^31
            cnt = 0
            mask = 1 << bit
            for num in nums:
                if num & mask:
                    cnt += 1
                    if cnt >= k:  # early stop
                        result |= mask
                        break
        return result
```

## C

```c
int findKOr(int* nums, int numsSize, int k) {
    int result = 0;
    for (int bit = 0; bit < 31; ++bit) {
        int mask = 1 << bit;
        int cnt = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] & mask) {
                ++cnt;
                if (cnt >= k) break;
            }
        }
        if (cnt >= k) {
            result |= mask;
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int FindKOr(int[] nums, int k) {
        int result = 0;
        for (int bit = 0; bit < 31; ++bit) {
            int mask = 1 << bit;
            int count = 0;
            foreach (int num in nums) {
                if ((num & mask) != 0) {
                    count++;
                    if (count >= k) break; // early exit
                }
            }
            if (count >= k) {
                result |= mask;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKOr = function(nums, k) {
    let result = 0;
    for (let bit = 0; bit < 31; ++bit) {
        let count = 0;
        const mask = 1 << bit;
        for (const num of nums) {
            if ((num & mask) !== 0) {
                ++count;
                if (count >= k) break; // early exit
            }
        }
        if (count >= k) {
            result |= mask;
        }
    }
    return result;
};
```

## Typescript

```typescript
function findKOr(nums: number[], k: number): number {
    let result = 0;
    for (let bit = 0; bit < 31; bit++) {
        const mask = 1 << bit;
        let cnt = 0;
        for (const num of nums) {
            if ((num & mask) !== 0) cnt++;
            if (cnt >= k) break;
        }
        if (cnt >= k) result |= mask;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function findKOr($nums, $k) {
        $result = 0;
        // Since nums[i] < 2^31, bits 0..30 are enough.
        for ($bit = 0; $bit <= 30; $bit++) {
            $mask = 1 << $bit;
            $cnt = 0;
            foreach ($nums as $num) {
                if (($num & $mask) !== 0) {
                    $cnt++;
                }
            }
            if ($cnt >= $k) {
                $result |= $mask;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findKOr(_ nums: [Int], _ k: Int) -> Int {
        var result = 0
        for bit in 0..<32 {
            let mask = 1 << bit
            var count = 0
            for num in nums {
                if (num & mask) != 0 {
                    count += 1
                    if count >= k { break }
                }
            }
            if count >= k {
                result |= mask
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKOr(nums: IntArray, k: Int): Int {
        var result = 0
        for (bit in 0..30) {
            val mask = 1 shl bit
            var count = 0
            for (num in nums) {
                if ((num and mask) != 0) {
                    count++
                }
            }
            if (count >= k) {
                result = result or mask
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int findKOr(List<int> nums, int k) {
    int result = 0;
    for (int bit = 0; bit < 31; ++bit) {
      int mask = 1 << bit;
      int count = 0;
      for (int num in nums) {
        if ((num & mask) != 0) {
          count++;
          if (count >= k) break;
        }
      }
      if (count >= k) {
        result |= mask;
      }
    }
    return result;
  }
}
```

## Golang

```go
func findKOr(nums []int, k int) int {
    result := 0
    for bit := 0; bit < 31; bit++ {
        mask := 1 << bit
        count := 0
        for _, v := range nums {
            if v&mask != 0 {
                count++
                if count >= k {
                    result |= mask
                    break
                }
            }
        }
    }
    return result
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_k_or(nums, k)
  result = 0
  (0...31).each do |bit|
    count = 0
    mask = 1 << bit
    nums.each do |num|
      count += 1 if (num & mask) != 0
    end
    result |= mask if count >= k
  end
  result
end
```

## Scala

```scala
object Solution {
    def findKOr(nums: Array[Int], k: Int): Int = {
        var result = 0
        for (bit <- 0 until 32) {
            var count = 0
            var i = 0
            while (i < nums.length) {
                if (((nums(i) >> bit) & 1) == 1) count += 1
                i += 1
            }
            if (count >= k) result |= (1 << bit)
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_k_or(nums: Vec<i32>, k: i32) -> i32 {
        let mut result = 0i32;
        for bit in 0..31 {
            let mask = 1i32 << bit;
            let mut cnt = 0usize;
            for &num in &nums {
                if num & mask != 0 {
                    cnt += 1;
                }
            }
            if cnt >= k as usize {
                result |= mask;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-k-or nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ((ans 0))
    (for ([bit (in-range 32)])
      (define mask (arithmetic-shift 1 bit))
      (define cnt
        (for/sum ([x nums])
          (if (zero? (bitwise-and x mask)) 0 1)))
      (when (>= cnt k)
        (set! ans (bitwise-ior ans mask))))
    ans))
```

## Erlang

```erlang
-spec find_k_or(Nums :: [integer()], K :: integer()) -> integer().
find_k_or(Nums, K) ->
    find_k_or(Nums, K, 0, 0).

find_k_or(_Nums, _K, 32, Acc) ->
    Acc;
find_k_or(Nums, K, Bit, Acc) ->
    Mask = 1 bsl Bit,
    Count = count_bits(Nums, Mask, 0),
    NewAcc = if
        Count >= K -> Acc bor Mask;
        true -> Acc
    end,
    find_k_or(Nums, K, Bit + 1, NewAcc).

count_bits([], _Mask, C) ->
    C;
count_bits([H|T], Mask, C) ->
    NewC = case H band Mask of
        0 -> C;
        _ -> C + 1
    end,
    count_bits(T, Mask, NewC).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec find_k_or(nums :: [integer], k :: integer) :: integer
  def find_k_or(nums, k) do
    Enum.reduce(0..31, 0, fn bit, acc ->
      mask = 1 <<< bit
      cnt = Enum.count(nums, fn n -> (n &&& mask) != 0 end)
      if cnt >= k, do: acc ||| mask, else: acc
    end)
  end
end
```
