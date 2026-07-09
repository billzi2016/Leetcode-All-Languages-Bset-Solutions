# 3513. Number of Unique XOR Triplets I

## Cpp

```cpp
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 1;
        if (n == 2) return 2;
        int msb = 31 - __builtin_clz(n); // floor(log2(n))
        return 1 << (msb + 1);
    }
};
```

## Java

```java
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        int n = nums.length;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int msb = 31 - Integer.numberOfLeadingZeros(n);
        return 1 << (msb + 1);
    }
}
```

## Python

```python
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        msb = n.bit_length() - 1
        return 1 << (msb + 1)
```

## Python3

```python
from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        msb = n.bit_length() - 1
        return 1 << (msb + 1)
```

## C

```c
int uniqueXorTriplets(int* nums, int numsSize) {
    int n = numsSize;
    if (n == 1) return 1;
    if (n == 2) return 2;
    int msb = 31 - __builtin_clz(n); // floor(log2(n))
    return 1 << (msb + 1);
}
```

## Csharp

```csharp
public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        int n = nums.Length;
        if (n <= 2) return n;
        int bits = 0;
        while ((1 << bits) <= n) bits++;
        return 1 << bits;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var uniqueXorTriplets = function(nums) {
    const n = nums.length;
    if (n === 1) return 1;
    if (n === 2) return 2;
    // most significant bit index (0‑based)
    const msb = 31 - Math.clz32(n);
    return 1 << (msb + 1);
};
```

## Typescript

```typescript
function uniqueXorTriplets(nums: number[]): number {
    const n = nums.length;
    if (n === 1) return 1;
    if (n === 2) return 2;
    const msb = Math.floor(Math.log2(n));
    return 1 << (msb + 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function uniqueXorTriplets($nums) {
        $n = count($nums);
        if ($n == 1) return 1;
        if ($n == 2) return 2;

        // find most significant bit position (0‑based)
        $msb = 0;
        $temp = $n;
        while ($temp > 1) {
            $temp >>= 1;
            $msb++;
        }
        // all values from 0 to 2^{msb+1}-1 are reachable
        return 1 << ($msb + 1);
    }
}
```

## Swift

```swift
class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 1 { return 1 }
        if n == 2 { return 2 }
        var x = n
        var msb = 0
        while x > 1 {
            x >>= 1
            msb += 1
        }
        return 1 << (msb + 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        val n = nums.size
        return when (n) {
            1 -> 1
            2 -> 2
            else -> {
                val msb = 31 - Integer.numberOfLeadingZeros(n)
                1 shl (msb + 1)
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  int uniqueXorTriplets(List<int> nums) {
    int n = nums.length;
    if (n == 1) return 1;
    if (n == 2) return 2;
    int msb = n.bitLength - 1; // floor(log2(n))
    return 1 << (msb + 1);
  }
}
```

## Golang

```go
import "math/bits"

func uniqueXorTriplets(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	msb := bits.Len(uint(n)) - 1
	return 1 << (msb + 1)
}
```

## Ruby

```ruby
def unique_xor_triplets(nums)
  n = nums.length
  return 1 if n == 1
  return 2 if n == 2
  1 << n.bit_length
end
```

## Scala

```scala
object Solution {
    def uniqueXorTriplets(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 1) return 1
        if (n == 2) return 2
        val msb = 31 - Integer.numberOfLeadingZeros(n)
        1 << (msb + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len() as u32;
        if n <= 2 {
            use std::collections::HashSet;
            let mut set = HashSet::new();
            for i in 0..n {
                for j in i..n {
                    for k in j..n {
                        let val = nums[i as usize] ^ nums[j as usize] ^ nums[k as usize];
                        set.insert(val);
                    }
                }
            }
            return set.len() as i32;
        }
        // n >= 3
        let msb = 31 - n.leading_zeros(); // position of most significant bit (0‑based)
        let ans = 1u32 << (msb + 1);
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (unique-xor-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length nums)))
    (cond
      [(= n 1) 1]
      [(= n 2) 2]
      [else
       (arithmetic-shift 1 (integer-length n))])))
```

## Erlang

```erlang
-module(solution).
-export([unique_xor_triplets/1]).

-spec unique_xor_triplets(Nums :: [integer()]) -> integer().
unique_xor_triplets(Nums) ->
    N = length(Nums),
    case N of
        0 -> 0;
        1 -> 1;
        2 -> 2;
        _ -> next_power_of_two(N + 1)
    end.

next_power_of_two(Limit) when Limit =< 1 -> 1;
next_power_of_two(Limit) ->
    next_power_of_two(1, Limit).

next_power_of_two(Power, Limit) when Power >= Limit -> Power;
next_power_of_two(Power, Limit) -> next_power_of_two(Power bsl 1, Limit).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_xor_triplets(nums :: [integer]) :: integer
  def unique_xor_triplets(nums) do
    n = length(nums)

    cond do
      n == 1 -> 1
      n == 2 -> 2
      true ->
        msb = floor_log2(n)
        1 <<< (msb + 1)
    end
  end

  defp floor_log2(x) when x > 0 do
    :math.floor(:math.log2(x)) |> trunc()
  end
end
```
