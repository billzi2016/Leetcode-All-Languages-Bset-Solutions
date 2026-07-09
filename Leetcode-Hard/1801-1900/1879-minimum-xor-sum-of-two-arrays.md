# 1879. Minimum XOR Sum of Two Arrays

## Cpp

```cpp
class Solution {
public:
    int minimumXORSum(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int totalMask = 1 << n;
        const int INF = 1e9;
        vector<int> dp(totalMask, INF);
        dp[0] = 0;
        for (int mask = 0; mask < totalMask; ++mask) {
            int i = __builtin_popcount((unsigned)mask); // index in nums1
            if (i >= n) continue;
            int cur = dp[mask];
            if (cur == INF) continue;
            for (int j = 0; j < n; ++j) {
                if (!(mask & (1 << j))) {
                    int newMask = mask | (1 << j);
                    int val = cur + (nums1[i] ^ nums2[j]);
                    if (val < dp[newMask]) dp[newMask] = val;
                }
            }
        }
        return dp[totalMask - 1];
    }
};
```

## Java

```java
class Solution {
    public int minimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int totalMasks = 1 << n;
        int INF = Integer.MAX_VALUE / 2;
        int[] dp = new int[totalMasks];
        for (int i = 0; i < totalMasks; i++) {
            dp[i] = INF;
        }
        dp[0] = 0;
        for (int mask = 0; mask < totalMasks; mask++) {
            int i = Integer.bitCount(mask); // index in nums1 to assign next
            if (i >= n) continue;
            int cur = dp[mask];
            if (cur == INF) continue;
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) == 0) {
                    int newMask = mask | (1 << j);
                    int val = cur + (nums1[i] ^ nums2[j]);
                    if (val < dp[newMask]) {
                        dp[newMask] = val;
                    }
                }
            }
        }
        return dp[totalMasks - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        size = 1 << n
        INF = float('inf')
        dp = [INF] * size
        dp[0] = 0
        for mask in range(size):
            i = bin(mask).count('1')  # index in nums1 to match next
            if i >= n:
                continue
            cur = dp[mask]
            for j in range(n):
                if not (mask >> j) & 1:
                    new_mask = mask | (1 << j)
                    val = cur + (nums1[i] ^ nums2[j])
                    if val < dp[new_mask]:
                        dp[new_mask] = val
        return dp[-1]
```

## Python3

```python
from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = 1 << n
        INF = 10 ** 9
        dp = [INF] * m
        dp[0] = 0
        for mask in range(m):
            i = bin(mask).count("1")  # index in nums1 to match next
            if i >= n:
                continue
            cur = dp[mask]
            for j in range(n):
                if not (mask >> j) & 1:
                    new_mask = mask | (1 << j)
                    val = cur + (nums1[i] ^ nums2[j])
                    if val < dp[new_mask]:
                        dp[new_mask] = val
        return dp[-1]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimumXORSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;
    int totalMask = 1 << n;
    int *dp = (int *)malloc(totalMask * sizeof(int));
    for (int i = 0; i < totalMask; ++i) dp[i] = INT_MAX;
    dp[0] = 0;

    for (int mask = 0; mask < totalMask; ++mask) {
        int i = __builtin_popcount((unsigned)mask);
        if (i >= n) continue;
        int cur = dp[mask];
        if (cur == INT_MAX) continue;
        for (int j = 0; j < n; ++j) {
            if (!(mask & (1 << j))) {
                int newMask = mask | (1 << j);
                int val = cur + (nums1[i] ^ nums2[j]);
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    int ans = dp[totalMask - 1];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumXORSum(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int size = 1 << n;
        int[] dp = new int[size];
        const int INF = int.MaxValue / 2;
        for (int i = 0; i < size; i++) dp[i] = INF;
        dp[0] = 0;

        int[] popcnt = new int[size];
        for (int mask = 1; mask < size; mask++) {
            popcnt[mask] = popcnt[mask >> 1] + (mask & 1);
        }

        for (int mask = 0; mask < size; mask++) {
            int i = popcnt[mask]; // index in nums1 to match next
            if (i >= n) continue;
            int cur = dp[mask];
            if (cur == INF) continue;
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) != 0) continue;
                int newMask = mask | (1 << j);
                int val = cur + (nums1[i] ^ nums2[j]);
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }

        return dp[size - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumXORSum = function(nums1, nums2) {
    const n = nums1.length;
    const total = 1 << n;
    const dp = new Array(total).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;

    // precompute popcount for all masks
    const popcnt = new Uint8Array(total);
    for (let mask = 1; mask < total; ++mask) {
        popcnt[mask] = popcnt[mask >> 1] + (mask & 1);
    }

    for (let mask = 0; mask < total; ++mask) {
        const i = popcnt[mask]; // index in nums1 to match next
        if (i >= n) continue;
        const cur = dp[mask];
        for (let j = 0; j < n; ++j) {
            if ((mask & (1 << j)) === 0) {
                const newMask = mask | (1 << j);
                const val = cur + (nums1[i] ^ nums2[j]);
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[total - 1];
};
```

## Typescript

```typescript
function minimumXORSum(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const total = 1 << n;
    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array<number>(total).fill(INF);
    dp[0] = 0;

    const countBits = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    for (let mask = 0; mask < total; mask++) {
        const i = countBits(mask); // index in nums1 to match next
        if (i >= n) continue;
        const cur = dp[mask];
        if (cur === INF) continue;
        for (let j = 0; j < n; j++) {
            if ((mask & (1 << j)) === 0) {
                const newMask = mask | (1 << j);
                const val = cur + (nums1[i] ^ nums2[j]);
                if (val < dp[newMask]) dp[newMask] = val;
            }
        }
    }

    return dp[total - 1];
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minimumXORSum($nums1, $nums2) {
        $n = count($nums1);
        $size = 1 << $n;
        $dp = array_fill(0, $size, PHP_INT_MAX);
        $dp[0] = 0;

        // precompute popcount for all masks
        $bitsCount = array_fill(0, $size, 0);
        for ($mask = 1; $mask < $size; $mask++) {
            $bitsCount[$mask] = $bitsCount[$mask >> 1] + ($mask & 1);
        }

        for ($mask = 0; $mask < $size; $mask++) {
            $i = $bitsCount[$mask]; // index in nums1
            if ($i >= $n) continue;
            $cur = $dp[$mask];
            if ($cur === PHP_INT_MAX) continue;
            for ($j = 0; $j < $n; $j++) {
                if (($mask & (1 << $j)) == 0) {
                    $newMask = $mask | (1 << $j);
                    $val = $cur + ($nums1[$i] ^ $nums2[$j]);
                    if ($val < $dp[$newMask]) {
                        $dp[$newMask] = $val;
                    }
                }
            }
        }

        return $dp[$size - 1];
    }
}
?>
```

## Swift

```swift
class Solution {
    func minimumXORSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        let totalMask = 1 << n
        var dp = Array(repeating: Int.max, count: totalMask)
        dp[0] = 0
        
        for mask in 0..<totalMask {
            let i = mask.nonzeroBitCount
            if i >= n { continue }
            let current = dp[mask]
            if current == Int.max { continue }
            for j in 0..<n where (mask & (1 << j)) == 0 {
                let newMask = mask | (1 << j)
                let val = current + (nums1[i] ^ nums2[j])
                if val < dp[newMask] {
                    dp[newMask] = val
                }
            }
        }
        
        return dp[totalMask - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumXORSum(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val total = 1 shl n
        val INF = Int.MAX_VALUE / 4
        val dp = IntArray(total) { INF }
        dp[0] = 0
        for (mask in 0 until total) {
            val i = Integer.bitCount(mask)
            if (i >= n) continue
            val cur = dp[mask]
            if (cur == INF) continue
            for (j in 0 until n) {
                if ((mask and (1 shl j)) == 0) {
                    val newMask = mask or (1 shl j)
                    val value = cur + (nums1[i] xor nums2[j])
                    if (value < dp[newMask]) dp[newMask] = value
                }
            }
        }
        return dp[total - 1]
    }
}
```

## Dart

```dart
class Solution {
  int minimumXORSum(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    int size = 1 << n;
    const int INF = 0x3FFFFFFFFFFFFFFF; // sufficiently large
    List<int> dp = List.filled(size, INF);
    dp[0] = 0;

    for (int mask = 0; mask < size; ++mask) {
      int i = _popCount(mask);
      if (i >= n) continue;
      int base = dp[mask];
      for (int j = 0; j < n; ++j) {
        if ((mask & (1 << j)) == 0) {
          int newMask = mask | (1 << j);
          int val = base + (nums1[i] ^ nums2[j]);
          if (val < dp[newMask]) dp[newMask] = val;
        }
      }
    }

    return dp[size - 1];
  }

  int _popCount(int x) {
    int count = 0;
    while (x != 0) {
      x &= x - 1;
      count++;
    }
    return count;
  }
}
```

## Golang

```go
import "math/bits"

func minimumXORSum(nums1 []int, nums2 []int) int {
	n := len(nums1)
	size := 1 << n
	const INF = int(^uint(0) >> 1)

	dp := make([]int, size)
	for i := 0; i < size; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for mask := 0; mask < size; mask++ {
		i := bits.OnesCount(uint(mask))
		if i >= n {
			continue
		}
		cur := dp[mask]
		if cur == INF {
			continue
		}
		for j := 0; j < n; j++ {
			if (mask>>j)&1 == 0 {
				newMask := mask | (1 << j)
				val := cur + (nums1[i] ^ nums2[j])
				if val < dp[newMask] {
					dp[newMask] = val
				}
			}
		}
	}
	return dp[size-1]
}
```

## Ruby

```ruby
def minimum_xor_sum(nums1, nums2)
  n = nums1.length
  total_masks = 1 << n
  # precompute popcount for each mask
  popcnt = Array.new(total_masks, 0)
  (1...total_masks).each do |m|
    popcnt[m] = popcnt[m >> 1] + (m & 1)
  end

  INF = 1 << 60
  dp = Array.new(total_masks, INF)
  dp[0] = 0

  (0...total_masks).each do |mask|
    i = popcnt[mask] # index in nums1 to assign next
    next if i >= n
    cur = dp[mask]
    (0...n).each do |j|
      bit = 1 << j
      next if (mask & bit) != 0
      new_mask = mask | bit
      val = cur + (nums1[i] ^ nums2[j])
      dp[new_mask] = val if val < dp[new_mask]
    end
  end

  dp[total_masks - 1]
end
```

## Scala

```scala
object Solution {
    def minimumXORSum(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        val size = 1 << n
        val INF = Int.MaxValue / 2
        val dp = Array.fill(size)(INF)
        dp(0) = 0
        for (mask <- 0 until size) {
            val i = Integer.bitCount(mask)
            if (i < n) {
                var j = 0
                while (j < n) {
                    if ((mask & (1 << j)) == 0) {
                        val newMask = mask | (1 << j)
                        val cost = dp(mask) + (nums1(i) ^ nums2(j))
                        if (cost < dp(newMask)) dp(newMask) = cost
                    }
                    j += 1
                }
            }
        }
        dp(size - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_xor_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let size = 1usize << n;
        let mut dp = vec![i32::MAX; size];
        dp[0] = 0;
        for mask in 0..size {
            let i = mask.count_ones() as usize;
            if i >= n { continue; }
            let cur = dp[mask];
            if cur == i32::MAX { continue; }
            for j in 0..n {
                if (mask & (1 << j)) == 0 {
                    let new_mask = mask | (1 << j);
                    let val = cur + (nums1[i] ^ nums2[j]);
                    if val < dp[new_mask] {
                        dp[new_mask] = val;
                    }
                }
            }
        }
        dp[size - 1]
    }
}
```

## Racket

```racket
(define/contract (minimum-xor-sum nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums1))
         (size (arithmetic-shift 1 n))          ; 2^n
         (INF (arithmetic-shift 1 60))          ; large sentinel
         (dp (make-vector size INF))
         (v1 (list->vector nums1))
         (v2 (list->vector nums2)))
    (vector-set! dp 0 0)
    (for ([mask (in-range size)])
      (let ((i (bitwise-bit-count mask))
            (cur (vector-ref dp mask)))
        (when (< cur INF)                     ; reachable state
          (for ([j (in-range n)])
            (when (= 0 (bitwise-and mask (arithmetic-shift 1 j))) ; j not used yet
              (let* ((new-mask (bitwise-ior mask (arithmetic-shift 1 j)))
                     (val (+ cur (bitwise-xor (vector-ref v1 i) (vector-ref v2 j)))))
                (when (< val (vector-ref dp new-mask))
                  (vector-set! dp new-mask val))))))))
    (vector-ref dp (sub1 size))))
```

## Erlang

```erlang
-spec minimum_xor_sum(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
minimum_xor_sum(Nums1, Nums2) ->
    N = length(Nums1),
    N1T = list_to_tuple(Nums1),
    N2T = list_to_tuple(Nums2),
    INF = 1 bsl 60,
    DP0 = #{0 => 0},
    FinalDP = loop(0, N, N1T, N2T, INF, DP0),
    maps:get((1 bsl N) - 1, FinalDP).

loop(I, N, _N1T, _N2T, _INF, DP) when I == N ->
    DP;
loop(I, N, N1T, N2T, INF, DP) ->
    Num1Val = element(I + 1, N1T),
    NDp = maps:fold(
        fun(Mask, Val, Acc) ->
            lists:foldl(
                fun(J, AAcc) ->
                    Bit = 1 bsl J,
                    case (Mask band Bit) of
                        0 ->
                            NewMask = Mask bor Bit,
                            Num2Val = element(J + 1, N2T),
                            Cost = Val + erlang:bxor(Num1Val, Num2Val),
                            Prev = maps:get(NewMask, AAcc, INF),
                            if Cost < Prev -> maps:put(NewMask, Cost, AAcc);
                               true       -> AAcc
                            end;
                        _ ->
                            AAcc
                    end
                end,
                Acc,
                lists:seq(0, N - 1)
            )
        end,
        #{},
        DP),
    loop(I + 1, N, N1T, N2T, INF, NDp).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_xor_sum(nums1 :: [integer], nums2 :: [integer]) :: integer
  def minimum_xor_sum(nums1, nums2) do
    import Bitwise

    n = length(nums1)
    total_masks = 1 <<< n
    a1 = List.to_tuple(nums1)
    a2 = List.to_tuple(nums2)
    inf = 1 <<< 60

    dp0 = %{0 => 0}

    dp_final =
      Enum.reduce(0..total_masks - 1, dp0, fn mask, dp_acc ->
        cur = Map.get(dp_acc, mask, inf)
        i = popcount(mask)

        if i < n do
          Enum.reduce(0..n - 1, dp_acc, fn j, dp_inner ->
            bit = 1 <<< j

            if (mask &&& bit) == 0 do
              new_mask = mask ||| bit
              val = cur + (elem(a1, i) ^^^ elem(a2, j))
              old = Map.get(dp_inner, new_mask, inf)

              if val < old do
                Map.put(dp_inner, new_mask, val)
              else
                dp_inner
              end
            else
              dp_inner
            end
          end)
        else
          dp_acc
        end
      end)

    Map.get(dp_final, total_masks - 1)
  end

  defp popcount(0), do: 0
  defp popcount(x) do
    1 + popcount(Bitwise.band(x, x - 1))
  end
end
```
