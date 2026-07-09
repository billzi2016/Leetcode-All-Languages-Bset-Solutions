# 2708. Maximum Strength of a Group

## Cpp

```cpp
class Solution {
public:
    long long maxStrength(vector<int>& nums) {
        vector<int> pos, neg;
        int zeroCnt = 0;
        for (int x : nums) {
            if (x > 0) pos.push_back(x);
            else if (x < 0) neg.push_back(x);
            else zeroCnt++;
        }
        sort(neg.begin(), neg.end()); // ascending, e.g., -9,-5,-1
        
        vector<long long> chosen;
        for (int p : pos) chosen.push_back(p);
        
        int nNeg = neg.size();
        if (nNeg % 2 == 0) {
            for (int v : neg) chosen.push_back(v);
        } else {
            if (!chosen.empty() || nNeg > 1) {
                // exclude the negative with smallest absolute value (closest to zero)
                for (int i = 0; i < nNeg - 1; ++i) chosen.push_back(neg[i]);
            }
            // else we cannot include any negative; will handle later
        }
        
        if (chosen.empty()) {
            if (zeroCnt > 0) return 0;
            // only one negative exists
            return (long long)neg[0];
        }
        
        long long prod = 1;
        for (long long v : chosen) prod *= v;
        return prod;
    }
};
```

## Java

```java
class Solution {
    public long maxStrength(int[] nums) {
        int n = nums.length;
        long best = Long.MIN_VALUE;
        int total = 1 << n;
        for (int mask = 1; mask < total; ++mask) {
            long prod = 1L;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    prod *= nums[i];
                }
            }
            if (prod > best) {
                best = prod;
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        best = None
        for mask in range(1, 1 << n):
            prod = 1
            m = mask
            i = 0
            while m:
                if m & 1:
                    prod *= nums[i]
                i += 1
                m >>= 1
            if best is None or prod > best:
                best = prod
        return best
```

## Python3

```python
class Solution:
    def maxStrength(self, nums):
        n = len(nums)
        best = None
        for mask in range(1, 1 << n):
            prod = 1
            i = 0
            m = mask
            while m:
                if m & 1:
                    prod *= nums[i]
                i += 1
                m >>= 1
            if best is None or prod > best:
                best = prod
        return best
```

## C

```c
#include <limits.h>

long long maxStrength(int* nums, int numsSize) {
    long long best = LLONG_MIN;
    int total = 1 << numsSize;
    for (int mask = 1; mask < total; ++mask) {
        long long prod = 1;
        for (int i = 0; i < numsSize; ++i) {
            if (mask & (1 << i)) {
                prod *= (long long)nums[i];
            }
        }
        if (prod > best) best = prod;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxStrength(int[] nums) {
        var positives = new System.Collections.Generic.List<int>();
        var negatives = new System.Collections.Generic.List<int>();

        foreach (int v in nums) {
            if (v > 0) positives.Add(v);
            else if (v < 0) negatives.Add(v);
        }

        long product = 1;
        int usedCount = 0;

        foreach (int p in positives) {
            product *= p;
            usedCount++;
        }

        negatives.Sort(); // ascending, more negative first
        int limit = negatives.Count;
        if (negatives.Count % 2 == 1) {
            // skip the negative with smallest absolute value (closest to zero)
            limit--;
        }
        for (int i = 0; i + 1 < limit; i += 2) {
            long pairProd = (long)negatives[i] * negatives[i + 1];
            product *= pairProd;
            usedCount += 2;
        }

        if (usedCount == 0) {
            int maxVal = nums[0];
            foreach (int v in nums) {
                if (v > maxVal) maxVal = v;
            }
            return maxVal;
        }

        return product;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxStrength = function(nums) {
    let posProduct = 1;
    let hasPos = false;
    const negs = [];
    
    for (const x of nums) {
        if (x > 0) {
            posProduct *= x;
            hasPos = true;
        } else if (x < 0) {
            negs.push(x);
        }
    }
    
    // Sort negatives to pair the most negative numbers together
    negs.sort((a, b) => a - b);
    
    let negProduct = 1;
    let usedNeg = false;
    for (let i = 0; i + 1 < negs.length; i += 2) {
        const pairProd = negs[i] * negs[i + 1];
        negProduct *= pairProd;
        usedNeg = true;
    }
    
    // If we couldn't pick any positive or a pair of negatives,
    // the best we can do is the maximum single element.
    if (!hasPos && !usedNeg) {
        return Math.max(...nums);
    }
    
    let result = 1;
    if (hasPos) result *= posProduct;
    if (usedNeg) result *= negProduct;
    return result;
};
```

## Typescript

```typescript
function maxStrength(nums: number[]): number {
    const n = nums.length;
    let best = -Infinity;
    const totalMasks = 1 << n;
    for (let mask = 1; mask < totalMasks; ++mask) {
        let prod = 1;
        for (let i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                prod *= nums[i];
            }
        }
        if (prod > best) best = prod;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxStrength($nums) {
        $negatives = [];
        $product = 1;
        $hasNonZero = false;
        $posCount = 0;
        foreach ($nums as $v) {
            if ($v == 0) continue;
            $hasNonZero = true;
            if ($v > 0) $posCount++;
            else $negatives[] = $v;
            $product *= $v;
        }

        // all zeros
        if (!$hasNonZero) return 0;

        $negCount = count($negatives);
        if ($negCount % 2 == 0) {
            return $product;
        }

        // odd number of negatives
        $removeNeg = max($negatives); // closest to zero (e.g., -1 > -5)

        // only one negative and no positives
        if ($negCount == 1 && $posCount == 0) {
            // if there is any zero, better to pick zero
            foreach ($nums as $v) {
                if ($v == 0) return 0;
            }
            return $removeNeg; // only element
        }

        // exclude the selected negative from product
        $product = (int)($product / $removeNeg);
        return $product;
    }
}
```

## Swift

```swift
class Solution {
    func maxStrength(_ nums: [Int]) -> Int {
        let n = nums.count
        var best = Int.min
        let totalMasks = 1 << n
        for mask in 1..<totalMasks {
            var product = 1
            for i in 0..<n where (mask & (1 << i)) != 0 {
                product *= nums[i]
            }
            if product > best {
                best = product
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxStrength(nums: IntArray): Long {
        val n = nums.size
        var best = Long.MIN_VALUE
        val totalMasks = 1 shl n
        for (mask in 1 until totalMasks) {
            var prod = 1L
            var idx = 0
            var m = mask
            while (m != 0) {
                if ((m and 1) == 1) {
                    prod *= nums[idx].toLong()
                }
                idx++
                m = m shr 1
            }
            if (prod > best) best = prod
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxStrength(List<int> nums) {
    List<int> positives = [];
    List<int> negatives = [];
    int zeroCount = 0;

    for (int x in nums) {
      if (x > 0) {
        positives.add(x);
      } else if (x < 0) {
        negatives.add(x);
      } else {
        zeroCount++;
      }
    }

    // Sort negatives to easily drop the one with smallest absolute value when needed
    negatives.sort(); // ascending, most negative first

    if (negatives.length.isOdd) {
      // Remove the negative closest to zero (last after sorting)
      negatives.removeLast();
    }

    // If no numbers are selected yet, we must pick the maximum single element
    if (positives.isEmpty && negatives.isEmpty) {
      int maxVal = nums[0];
      for (int v in nums) {
        if (v > maxVal) maxVal = v;
      }
      return maxVal;
    }

    int product = 1;
    for (int p in positives) product *= p;
    for (int n in negatives) product *= n;

    return product;
  }
}
```

## Golang

```go
func maxStrength(nums []int) int64 {
	n := len(nums)
	maxProd := int64(-1 << 63) // initialize to minimum int64
	for mask := 1; mask < (1 << n); mask++ {
		prod := int64(1)
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				prod *= int64(nums[i])
			}
		}
		if prod > maxProd {
			maxProd = prod
		}
	}
	return maxProd
}
```

## Ruby

```ruby
def max_strength(nums)
  n = nums.length
  max_prod = nil
  (1...(1 << n)).each do |mask|
    prod = 1
    i = 0
    while i < n
      if mask & (1 << i) != 0
        prod *= nums[i]
      end
      i += 1
    end
    max_prod = prod if max_prod.nil? || prod > max_prod
  end
  max_prod
end
```

## Scala

```scala
object Solution {
    def maxStrength(nums: Array[Int]): Long = {
        val n = nums.length
        var best: Long = Long.MinValue
        val totalMasks = 1 << n
        for (mask <- 1 until totalMasks) {
            var prod: Long = 1L
            var i = 0
            while (i < n) {
                if ((mask & (1 << i)) != 0) {
                    prod *= nums(i).toLong
                }
                i += 1
            }
            if (prod > best) best = prod
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_strength(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut best = i64::MIN;
        for mask in 1usize..(1usize << n) {
            let mut prod: i64 = 1;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    prod *= nums[i] as i64;
                }
            }
            if prod > best {
                best = prod;
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (max-strength nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (total (expt 2 n))
         (best (car nums)))
    (for ([mask (in-range 1 total)])
      (let ((prod 1))
        (for ([i (in-range n)])
          (when (not (= 0 (bitwise-and mask (arithmetic-shift 1 i))))
            (set! prod (* prod (list-ref nums i)))))
        (when (> prod best)
          (set! best prod))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([max_strength/1]).

-spec max_strength(Nums :: [integer()]) -> integer().
max_strength(Nums) ->
    N = length(Nums),
    Max = max_strength_masks(Nums, N, 1, undefined),
    Max.

max_strength_masks(_Nums, N, Mask, MaxAcc) when Mask >= (1 bsl N) ->
    MaxAcc;
max_strength_masks(Nums, N, Mask, MaxAcc) ->
    Prod = subset_product(Nums, Mask, 1),
    NewMax = case MaxAcc of
        undefined -> Prod;
        _ when Prod > MaxAcc -> Prod;
        _ -> MaxAcc
    end,
    max_strength_masks(Nums, N, Mask + 1, NewMax).

subset_product([], _Mask, Acc) ->
    Acc;
subset_product([H|T], Mask, Acc) ->
    case (Mask band 1) of
        1 -> subset_product(T, Mask bsr 1, Acc * H);
        0 -> subset_product(T, Mask bsr 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_strength(nums :: [integer]) :: integer
  def max_strength(nums) do
    n = length(nums)
    total_masks = 1 <<< n
    Enum.reduce(1..(total_masks - 1), nil, fn mask, current_max ->
      prod = compute_product(nums, mask)

      case current_max do
        nil -> prod
        _ when prod > current_max -> prod
        _ -> current_max
      end
    end)
  end

  defp compute_product(nums, mask) do
    Enum.reduce(Enum.with_index(nums), 1, fn {val, idx}, acc ->
      if (mask &&& (1 <<< idx)) != 0, do: acc * val, else: acc
    end)
  end
end
```
