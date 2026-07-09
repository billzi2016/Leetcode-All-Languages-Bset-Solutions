# 2568. Minimum Impossible OR

## Cpp

```cpp
class Solution {
public:
    int minImpossibleOR(vector<int>& nums) {
        const int MAX_BITS = 31; // enough for values up to 2^30
        vector<bool> has(MAX_BITS, false);
        for (int v : nums) {
            if ((v & (v - 1)) == 0) { // power of two
                int bit = __builtin_ctz(v); // position of the only set bit
                if (bit < MAX_BITS) has[bit] = true;
            }
        }
        for (int i = 0; i < MAX_BITS; ++i) {
            if (!has[i]) return 1 << i;
        }
        // All bits up to 30 are present, next power of two is 2^31 which fits in int
        return 1 << MAX_BITS;
    }
};
```

## Java

```java
class Solution {
    public int minImpossibleOR(int[] nums) {
        boolean[] have = new boolean[31];
        for (int v : nums) {
            if ((v & (v - 1)) == 0) { // power of two
                int bit = Integer.numberOfTrailingZeros(v);
                if (bit < 31) {
                    have[bit] = true;
                }
            }
        }
        for (int i = 0; i < 31; i++) {
            if (!have[i]) {
                return 1 << i;
            }
        }
        // According to constraints this case won't occur.
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def minImpossibleOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        present = set(nums)
        p = 1
        while True:
            if p not in present:
                return p
            p <<= 1
```

## Python3

```python
class Solution:
    def minImpossibleOR(self, nums):
        pure = set()
        for v in nums:
            # check if v is a power of two
            if v & (v - 1) == 0:
                pure.add(v)
        k = 0
        while True:
            candidate = 1 << k
            if candidate not in pure:
                return candidate
            k += 1
```

## C

```c
int minImpossibleOR(int* nums, int numsSize) {
    int present[31] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        if (x && (x & (x - 1)) == 0) {
            int bit = __builtin_ctz(x);
            if (bit < 31) present[bit] = 1;
        }
    }
    for (int i = 0; i < 31; ++i) {
        if (!present[i]) {
            return 1 << i;
        }
    }
    return 1 << 30; // fallback, should never be reached with given constraints
}
```

## Csharp

```csharp
public class Solution
{
    public int MinImpossibleOR(int[] nums)
    {
        var powerSet = new HashSet<int>();
        foreach (var v in nums)
        {
            if ((v & (v - 1)) == 0) // check if v is a power of two
                powerSet.Add(v);
        }

        for (int k = 0; ; k++)
        {
            long candidate = 1L << k;
            if (candidate > int.MaxValue)
                break;
            int val = (int)candidate;
            if (!powerSet.Contains(val))
                return val;
        }
        // Should never reach here given problem constraints
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minImpossibleOR = function(nums) {
    const powerSet = new Set();
    for (const v of nums) {
        // check if v is a power of two: only one bit set
        if ((v & (v - 1)) === 0) {
            powerSet.add(v);
        }
    }
    let p = 1;
    while (powerSet.has(p)) {
        p <<= 1;
    }
    return p;
};
```

## Typescript

```typescript
function minImpossibleOR(nums: number[]): number {
    const powers = new Set<number>();
    for (const v of nums) {
        if ((v & (v - 1)) === 0) {
            powers.add(v);
        }
    }
    let ans = 1;
    while (powers.has(ans)) {
        ans <<= 1;
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
    function minImpossibleOR($nums) {
        $powers = [];
        foreach ($nums as $num) {
            if (($num & ($num - 1)) == 0) { // check power of two
                $powers[$num] = true;
            }
        }
        $val = 1;
        while (true) {
            if (!isset($powers[$val])) {
                return $val;
            }
            $val <<= 1;
        }
    }
}
```

## Swift

```swift
class Solution {
    func minImpossibleOR(_ nums: [Int]) -> Int {
        var present = Set<Int>()
        for v in nums {
            present.insert(v)
        }
        var power = 1
        while present.contains(power) {
            power <<= 1
        }
        return power
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minImpossibleOR(nums: IntArray): Int {
        val set = HashSet<Int>(nums.size * 2)
        for (v in nums) {
            set.add(v)
        }
        var p = 1
        while (true) {
            if (!set.contains(p)) return p
            // Prevent overflow; given constraints, answer will be found before exceeding this.
            if (p > (1 shl 30)) break
            p = p shl 1
        }
        return p
    }
}
```

## Dart

```dart
class Solution {
  int minImpossibleOR(List<int> nums) {
    const int maxBits = 31;
    List<bool> have = List.filled(maxBits, false);
    for (int v in nums) {
      if ((v & (v - 1)) == 0) { // power of two
        int bit = v.bitLength - 1; // position of the set bit
        if (bit < maxBits) have[bit] = true;
      }
    }
    for (int i = 0;; i++) {
      if (i >= maxBits || !have[i]) return 1 << i;
    }
  }
}
```

## Golang

```go
import "math/bits"

func minImpossibleOR(nums []int) int {
    const maxBits = 31 // sufficient for nums[i] <= 1e9
    present := make([]bool, maxBits+1)
    for _, v := range nums {
        msb := bits.Len(uint(v)) - 1
        if msb >= 0 {
            present[msb] = true
        }
    }
    for i := 0; ; i++ {
        if i >= len(present) || !present[i] {
            return 1 << i
        }
    }
}
```

## Ruby

```ruby
def min_impossible_or(nums)
  present = {}
  nums.each { |v| present[v] = true }
  power = 1
  loop do
    return power unless present.key?(power)
    power <<= 1
  end
end
```

## Scala

```scala
object Solution {
    def minImpossibleOR(nums: Array[Int]): Int = {
        val present = new Array[Boolean](31)
        var idx = 0
        while (idx < nums.length) {
            val v = nums(idx)
            if ((v & (v - 1)) == 0) { // power of two
                val bit = Integer.numberOfTrailingZeros(v)
                present(bit) = true
            }
            idx += 1
        }
        var bit = 0
        while (bit < 31 && present(bit)) {
            bit += 1
        }
        1 << bit
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_impossible_or(nums: Vec<i32>) -> i32 {
        let mut present = [false; 31];
        for &x in nums.iter() {
            if x > 0 && (x & (x - 1)) == 0 {
                let k = x.trailing_zeros() as usize;
                if k < 31 {
                    present[k] = true;
                }
            }
        }
        for k in 0..31 {
            if !present[k] {
                return 1i32 << k;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (min-impossible-or nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([power-set (make-hash)])
    (for ([v nums])
      (when (and (> v 0) (= (bitwise-and v (sub1 v)) 0))
        (hash-set! power-set v #t)))
    (let loop ((k 0))
      (define candidate (arithmetic-shift 1 k))
      (if (hash-has-key? power-set candidate)
          (loop (+ k 1))
          candidate))))
```

## Erlang

```erlang
-spec min_impossible_or(Nums :: [integer()]) -> integer().
min_impossible_or(Nums) ->
    Set = build_set(Nums, #{}),
    find_missing(0, Set).

build_set([], Set) -> 
    Set;
build_set([H|T], Set) ->
    case (H band (H - 1)) of
        0 -> % H is a power of two
            build_set(T, maps:put(H, true, Set));
        _ ->
            build_set(T, Set)
    end.

find_missing(I, Set) ->
    Val = 1 bsl I,
    case maps:is_key(Val, Set) of
        true -> find_missing(I + 1, Set);
        false -> Val
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_impossible_or(nums :: [integer]) :: integer
  def min_impossible_or(nums) do
    import Bitwise

    powers =
      nums
      |> Enum.filter(fn x -> (x &&& (x - 1)) == 0 end)
      |> MapSet.new()

    i =
      Stream.iterate(0, &(&1 + 1))
      |> Enum.find(fn idx ->
        val = 1 <<< idx
        not MapSet.member?(powers, val)
      end)

    1 <<< i
  end
end
```
