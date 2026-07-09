# 3566. Partition Array into Two Equal Product Subsets

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkEqualPartitions(vector<int>& nums, long long target) {
        int n = nums.size();
        __int128 total = 1;
        for (int x : nums) total *= (__int128)x;
        __int128 need = (__int128)target * (__int128)target;
        if (total != need) return false;

        int fullMask = (1 << n) - 1;
        for (int mask = 1; mask < fullMask; ++mask) {
            if (mask == fullMask) continue; // whole set, not allowed
            __int128 prod = 1;
            bool over = false;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    prod *= (__int128)nums[i];
                    if (prod > target) { // early stop
                        over = true;
                        break;
                    }
                }
            }
            if (!over && prod == target) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkEqualPartitions(int[] nums, long target) {
        int n = nums.length;
        java.math.BigInteger total = java.math.BigInteger.ONE;
        for (int v : nums) {
            total = total.multiply(java.math.BigInteger.valueOf(v));
        }
        java.math.BigInteger t = java.math.BigInteger.valueOf(target);
        if (!total.equals(t.multiply(t))) return false;

        int limit = 1 << n;
        for (int mask = 1; mask < limit - 1; ++mask) {
            long prod = 1L;
            boolean exceed = false;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    int val = nums[i];
                    if (prod > target / val) {
                        exceed = true;
                        break;
                    }
                    prod *= val;
                }
            }
            if (!exceed && prod == target) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        total = 1
        for v in nums:
            total *= v
        if total != target * target:
            return False

        n = len(nums)
        # iterate all non-empty proper subsets
        for mask in range(1, (1 << n) - 1):
            prod = 1
            ok = True
            for i in range(n):
                if mask >> i & 1:
                    prod *= nums[i]
                    if prod > target:   # early stop, all numbers positive
                        ok = False
                        break
            if ok and prod == target:
                return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total = 1
        for v in nums:
            total *= v
        if total != target * target:
            return False

        n = len(nums)
        # iterate all non‑empty proper subsets
        limit = (1 << n) - 1
        for mask in range(1, limit):
            if mask == limit:  # skip full set
                continue
            prod_val = 1
            overflow = False
            for i in range(n):
                if mask >> i & 1:
                    prod_val *= nums[i]
                    if prod_val > target:
                        overflow = True
                        break
            if not overflow and prod_val == target:
                return True
        return False
```

## C

```c
#include <stdbool.h>
#include <stddef.h>

bool checkEqualPartitions(int* nums, int numsSize, long long target) {
    __int128 total = 1;
    for (int i = 0; i < numsSize; ++i) {
        total *= (__int128)nums[i];
    }
    __int128 need = (__int128)target * (__int128)target;
    if (total != need) return false;

    int n = numsSize;
    int limit = 1 << n;
    for (int mask = 1; mask < limit - 1; ++mask) {
        __int128 prod = 1;
        bool exceeded = false;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                prod *= (__int128)nums[i];
                if (prod > target) { // cannot match target
                    exceeded = true;
                    break;
                }
            }
        }
        if (!exceeded && prod == target) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckEqualPartitions(int[] nums, long target) {
        int n = nums.Length;
        var totalProduct = new System.Numerics.BigInteger(1);
        foreach (int v in nums) totalProduct *= v;

        var t = new System.Numerics.BigInteger(target);
        if (totalProduct != t * t) return false; // necessary condition

        int limit = 1 << n;
        for (int mask = 1; mask < limit - 1; ++mask) { // exclude empty and full
            long prod = 1;
            bool exceeded = false;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    int val = nums[i];
                    if (prod > target / val) { // would exceed target
                        exceeded = true;
                        break;
                    }
                    prod *= val;
                }
            }
            if (!exceeded && prod == target) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var checkEqualPartitions = function(nums, target) {
    const n = nums.length;
    const bigNums = nums.map(v => BigInt(v));
    const bigTarget = BigInt(target);
    const totalProd = bigNums.reduce((acc, v) => acc * v, 1n);
    if (totalProd !== bigTarget * bigTarget) return false;

    const fullMask = (1 << n) - 1;
    // iterate over all non‑empty proper subsets
    for (let mask = 1; mask < fullMask; ++mask) {
        // skip the whole set
        if (mask === fullMask) continue;
        let prod = 1n;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                prod *= bigNums[i];
                if (prod > bigTarget) break; // early stop
            }
        }
        if (prod === bigTarget) return true;
    }
    return false;
};
```

## Typescript

```typescript
function checkEqualPartitions(nums: number[], target: number): boolean {
    const n = nums.length;
    const bigTarget = BigInt(target);
    let totalProd = 1n;
    for (const v of nums) totalProd *= BigInt(v);
    if (totalProd !== bigTarget * bigTarget) return false;

    const limit = 1 << n;
    for (let mask = 1; mask < limit - 1; ++mask) {
        let prod = 1n;
        for (let i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                prod *= BigInt(nums[i]);
                if (prod > bigTarget) break;
            }
        }
        if (prod === bigTarget) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function checkEqualPartitions($nums, $target) {
        $n = count($nums);
        $limit = 1 << $n;
        for ($mask = 1; $mask < $limit - 1; $mask++) {
            $prod = 1;
            // product of subset defined by mask
            for ($i = 0; $i < $n; $i++) {
                if ($mask & (1 << $i)) {
                    $prod *= $nums[$i];
                    if ($prod > $target) {
                        break;
                    }
                }
            }
            if ($prod !== $target) {
                continue;
            }
            // product of complement subset
            $comp = 1;
            for ($i = 0; $i < $n; $i++) {
                if (!($mask & (1 << $i))) {
                    $comp *= $nums[$i];
                    if ($comp > $target) {
                        break;
                    }
                }
            }
            if ($comp === $target) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkEqualPartitions(_ nums: [Int], _ target: Int) -> Bool {
        let n = nums.count
        if n < 2 { return false }
        let t = UInt64(target)
        let totalMasks = 1 << n
        // iterate over all non‑empty proper subsets
        for mask in 1..<(totalMasks - 1) {
            var prod: UInt64 = 1
            var exceeded = false
            for i in 0..<n where (mask >> i) & 1 == 1 {
                prod *= UInt64(nums[i])
                if prod > t { exceeded = true; break }
            }
            if exceeded || prod != t { continue }
            // complement product
            var comp: UInt64 = 1
            exceeded = false
            for i in 0..<n where (mask >> i) & 1 == 0 {
                comp *= UInt64(nums[i])
                if comp > t { exceeded = true; break }
            }
            if !exceeded && comp == t {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkEqualPartitions(nums: IntArray, target: Long): Boolean {
        val n = nums.size
        // Compute total product using BigInteger to avoid overflow
        var total = java.math.BigInteger.ONE
        for (v in nums) {
            total = total.multiply(java.math.BigInteger.valueOf(v.toLong()))
        }
        val tBig = java.math.BigInteger.valueOf(target)
        if (!total.equals(tBig.multiply(tBig))) return false

        // Enumerate all non‑empty proper subsets
        val limit = 1 shl n
        for (mask in 1 until limit - 1) {
            var prod = 1L
            var exceeded = false
            for (i in 0 until n) {
                if ((mask and (1 shl i)) != 0) {
                    val v = nums[i].toLong()
                    // If multiplication would exceed target, break early
                    if (prod > target / v) {
                        exceeded = true
                        break
                    }
                    prod *= v
                }
            }
            if (!exceeded && prod == target) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool checkEqualPartitions(List<int> nums, int target) {
    int n = nums.length;
    int totalProduct = 1;
    for (int v in nums) {
      totalProduct *= v;
    }
    if (totalProduct != target * target) return false;

    int limit = 1 << n;
    for (int mask = 1; mask < limit - 1; ++mask) {
      int prod = 1;
      bool exceed = false;
      for (int i = 0; i < n; ++i) {
        if ((mask >> i) & 1 == 1) {
          prod *= nums[i];
          if (prod > target) {
            exceed = true;
            break;
          }
        }
      }
      if (!exceed && prod == target) return true;
    }
    return false;
  }
}
```

## Golang

```go
import "math/big"

func checkEqualPartitions(nums []int, target int64) bool {
	n := len(nums)

	// Compute total product using big integers
	total := big.NewInt(1)
	for _, v := range nums {
		total.Mul(total, big.NewInt(int64(v)))
	}
	tBig := big.NewInt(target)
	targetSq := new(big.Int).Mul(tBig, tBig)
	if total.Cmp(targetSq) != 0 {
		return false
	}

	var dfs func(idx int, prod int64, cnt int) bool
	dfs = func(idx int, prod int64, cnt int) bool {
		if idx == n {
			return prod == target && cnt > 0 && cnt < n
		}
		v := int64(nums[idx])

		// Include current number if it doesn't exceed target
		if prod <= target/v {
			if dfs(idx+1, prod*v, cnt+1) {
				return true
			}
		}
		// Exclude current number
		if dfs(idx+1, prod, cnt) {
			return true
		}
		return false
	}

	return dfs(0, 1, 0)
}
```

## Ruby

```ruby
def check_equal_partitions(nums, target)
  n = nums.length
  total = 1
  nums.each { |x| total *= x }
  return false unless total == target * target

  limit = (1 << n) - 1
  (1...limit).each do |mask|
    prod = 1
    (0...n).each do |i|
      if mask & (1 << i) != 0
        prod *= nums[i]
        break if prod > target
      end
    end
    next unless prod == target

    # ensure complement is non‑empty (mask not full)
    return true if mask != limit
  end
  false
end
```

## Scala

```scala
object Solution {
  def checkEqualPartitions(nums: Array[Int], target: Long): Boolean = {
    val n = nums.length
    // Verify total product equals target^2 using BigInt to avoid overflow
    var total = BigInt(1)
    for (v <- nums) total *= v
    if (total != BigInt(target) * target) return false

    val fullMask = (1 << n) - 1
    var mask = 1
    while (mask < fullMask) {
      var prod: Long = 1L
      var valid = true
      var i = 0
      while (i < n && valid) {
        if ((mask >> i & 1) == 1) {
          val v = nums(i).toLong
          if (prod > target / v) {
            valid = false // product would exceed target
          } else {
            prod *= v
          }
        }
        i += 1
      }
      if (valid && prod == target) return true
      mask += 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn check_equal_partitions(nums: Vec<i32>, target: i64) -> bool {
        let n = nums.len();
        if n < 2 {
            return false;
        }
        // total product of all numbers
        let mut total: u128 = 1;
        for &v in &nums {
            total *= v as u128;
        }
        let t = target as u128;
        // both subsets must multiply to target, so total must be target^2
        if total != t * t {
            return false;
        }

        // enumerate non‑empty proper subsets
        let limit = 1usize << n;
        for mask in 1..limit - 1 {
            let mut prod: u128 = 1;
            let mut overflow = false;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    prod *= nums[i] as u128;
                    if prod > t {
                        overflow = true;
                        break;
                    }
                }
            }
            if !overflow && prod == t {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (check-equal-partitions nums target)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((n (length nums))
         (total (apply * nums))
         (target-sq (* target target)))
    (if (not (= total target-sq))
        #false
        (let loop ((mask 1) (full (- (expt 2 n) 1))) ; full mask value
          (cond [(>= mask full) #false]
                [else
                 (let ((prod
                        (let inner ((i 0) (p 1))
                          (if (= i n)
                              p
                              (inner (+ i 1)
                                     (if (bitwise-bit-set? mask i)
                                         (* p (list-ref nums i))
                                         p))))))
                   (if (= prod target)
                       #true
                       (loop (+ mask 1) full))))])))
```

## Erlang

```erlang
-module(solution).
-export([check_equal_partitions/2]).

-spec check_equal_partitions(Nums :: [integer()], Target :: integer()) -> boolean().
check_equal_partitions(Nums, Target) ->
    TotalProd = lists:foldl(fun(X, Acc) -> X * Acc end, 1, Nums),
    case TotalProd == Target * Target of
        false -> false;
        true ->
            N = length(Nums),
            MaxMask = (1 bsl N) - 1,
            find_subset(Nums, N, Target, 1, MaxMask - 1)
    end.

find_subset(_Nums, _N, _Target, Mask, Limit) when Mask > Limit -> false;
find_subset(Nums, N, Target, Mask, Limit) ->
    Prod = subset_product(Nums, Mask, 0, 1),
    if
        Prod == Target -> true;
        true -> find_subset(Nums, N, Target, Mask + 1, Limit)
    end.

subset_product([], _Mask, _Pos, Acc) -> Acc;
subset_product([H|T], Mask, Pos, Acc) ->
    case (Mask band (1 bsl Pos)) of
        0 -> subset_product(T, Mask, Pos + 1, Acc);
        _ -> subset_product(T, Mask, Pos + 1, H * Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec check_equal_partitions(nums :: [integer], target :: integer) :: boolean
  def check_equal_partitions(nums, target) do
    total = Enum.reduce(nums, 1, &*/2)

    if total != target * target do
      false
    else
      n = length(nums)
      max_mask = (1 <<< n) - 1

      1..(max_mask - 1)
      |> Enum.any?(fn mask ->
        subset_product(mask, nums, target) == target
      end)
    end
  end

  defp subset_product(mask, nums, limit) do
    Enum.reduce_while(Enum.with_index(nums), 1, fn {val, idx}, acc ->
      if (mask &&& (1 <<< idx)) != 0 do
        new = acc * val
        if new > limit, do: {:halt, new}, else: {:cont, new}
      else
        {:cont, acc}
      end
    end)
  end
end
```
