# 2997. Minimum Number of Operations to Make Array XOR Equal to K

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int totalXor = 0;
        for (int num : nums) totalXor ^= num;
        int diff = totalXor ^ k;
        return __builtin_popcount(diff);
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums, int k) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        return Integer.bitCount(xor ^ k);
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num
        diff = xor_all ^ k
        # Use built‑in bit_count if available (Python 3.8+), otherwise fallback to bin count.
        return diff.bit_count() if hasattr(int, "bit_count") else bin(diff).count('1')
```

## Python3

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        return (total_xor ^ k).bit_count()
```

## C

```c
int minOperations(int* nums, int numsSize, int k) {
    int xorAll = 0;
    for (int i = 0; i < numsSize; ++i) {
        xorAll ^= nums[i];
    }
    int diff = xorAll ^ k;
    return __builtin_popcount(diff);
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(int[] nums, int k)
    {
        int xor = 0;
        foreach (int num in nums)
        {
            xor ^= num;
        }
        int diff = xor ^ k;
        int count = 0;
        while (diff != 0)
        {
            count += diff & 1;
            diff >>= 1;
        }
        return count;
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
var minOperations = function(nums, k) {
    let totalXor = 0;
    for (const num of nums) {
        totalXor ^= num;
    }
    let diff = totalXor ^ k;
    let operations = 0;
    while (diff !== 0) {
        operations++;
        diff &= diff - 1; // clear the lowest set bit
    }
    return operations;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    let totalXor = 0;
    for (const num of nums) {
        totalXor ^= num;
    }
    let diff = totalXor ^ k;
    let operations = 0;
    while (diff !== 0) {
        operations += diff & 1;
        diff >>>= 1;
    }
    return operations;
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
    function minOperations($nums, $k) {
        $xor = 0;
        foreach ($nums as $num) {
            $xor ^= $num;
        }
        $diff = $xor ^ $k;
        $cnt = 0;
        while ($diff) {
            $cnt++;
            $diff &= $diff - 1; // clear lowest set bit
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var xorAll = 0
        for num in nums {
            xorAll ^= num
        }
        let diff = xorAll ^ k
        return diff.nonzeroBitCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        var xorAll = 0
        for (num in nums) {
            xorAll = xorAll xor num
        }
        val diff = xorAll xor k
        return Integer.bitCount(diff)
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    int xor = 0;
    for (var v in nums) {
      xor ^= v;
    }
    int diff = xor ^ k;
    int cnt = 0;
    while (diff != 0) {
      cnt += diff & 1;
      diff >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
package main

import "math/bits"

func minOperations(nums []int, k int) int {
	xor := 0
	for _, v := range nums {
		xor ^= v
	}
	return bits.OnesCount(uint(xor ^ k))
}
```

## Ruby

```ruby
def min_operations(nums, k)
  xor_sum = 0
  nums.each { |num| xor_sum ^= num }
  (xor_sum ^ k).to_s(2).count('1')
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        var xorAll = 0
        var i = 0
        while (i < nums.length) {
            xorAll ^= nums(i)
            i += 1
        }
        Integer.bitCount(xorAll ^ k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut xor = 0i32;
        for v in nums {
            xor ^= v;
        }
        (xor ^ k).count_ones() as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((xs nums) (xor 0))
    (if (null? xs)
        (bitwise-bit-count (bitwise-xor xor k))
        (loop (cdr xs) (bitwise-xor xor (car xs))))))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    XorAll = lists:foldl(fun(X, Acc) -> X bxor Acc end, 0, Nums),
    Diff = XorAll bxor K,
    count_bits(Diff).

count_bits(N) when N =:= 0 -> 0;
count_bits(N) ->
    count_bits(N band (N - 1)) + 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    xor_all = Enum.reduce(nums, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
    diff = Bitwise.bxor(xor_all, k)
    popcount(diff)
  end

  defp popcount(0), do: 0
  defp popcount(n) do
    Bitwise.band(n, 1) + popcount(Bitwise.bsr(n, 1))
  end
end
```
