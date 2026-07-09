# 0982. Triples with Bitwise AND Equal To Zero

## Cpp

```cpp
class Solution {
public:
    int countTriplets(vector<int>& nums) {
        const int B = 16;
        const int MAX = 1 << B;
        vector<int> cnt(MAX, 0);
        for (int x : nums) ++cnt[x];
        
        // sup[mask] = sum_{superset of mask} cnt[superset]
        vector<long long> sup(MAX);
        for (int m = 0; m < MAX; ++m) sup[m] = cnt[m];
        for (int i = 0; i < B; ++i) {
            for (int m = 0; m < MAX; ++m) {
                if ((m & (1 << i)) == 0)
                    sup[m] += sup[m | (1 << i)];
            }
        }
        
        // exact[mask] = number of ordered pairs with AND exactly mask
        vector<long long> exact(MAX);
        for (int m = 0; m < MAX; ++m) exact[m] = sup[m] * sup[m];
        for (int i = 0; i < B; ++i) {
            for (int m = 0; m < MAX; ++m) {
                if ((m & (1 << i)) == 0)
                    exact[m] -= exact[m | (1 << i)];
            }
        }
        
        // dp[mask] = sum_{sub ⊆ mask} exact[sub]
        vector<long long> dp = exact;
        for (int i = 0; i < B; ++i) {
            for (int m = 0; m < MAX; ++m) {
                if (m & (1 << i))
                    dp[m] += dp[m ^ (1 << i)];
            }
        }
        
        long long ans = 0;
        int fullMask = MAX - 1;
        for (int m = 0; m < MAX; ++m) {
            if (!cnt[m]) continue;
            int comp = (~m) & fullMask;
            ans += (long long)cnt[m] * dp[comp];
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countTriplets(int[] nums) {
        final int BITS = 16;
        final int SIZE = 1 << BITS;
        int[] freq = new int[SIZE];
        for (int num : nums) {
            freq[num]++;
        }
        // SOS DP to compute dp[mask] = sum of frequencies of submasks of mask
        int[] dp = freq.clone();
        for (int i = 0; i < BITS; i++) {
            for (int mask = 0; mask < SIZE; mask++) {
                if ((mask & (1 << i)) != 0) {
                    dp[mask] += dp[mask ^ (1 << i)];
                }
            }
        }
        long ans = 0;
        int n = nums.length;
        int fullMask = SIZE - 1;
        for (int i = 0; i < n; i++) {
            int a = nums[i];
            for (int j = 0; j < n; j++) {
                int b = nums[j];
                int and = a & b;
                int complement = (~and) & fullMask;
                ans += dp[complement];
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_BITS = 16
        MAX_MASK = (1 << MAX_BITS) - 1

        # frequency of each value
        cnt = [0] * (MAX_MASK + 1)
        for v in nums:
            cnt[v] += 1

        # SOS DP: f[mask] = sum_{submask ⊆ mask} cnt[submask]
        f = cnt[:]
        for i in range(MAX_BITS):
            bit = 1 << i
            for mask in range(MAX_MASK + 1):
                if mask & bit:
                    f[mask] += f[mask ^ bit]

        ans = 0
        n = len(nums)
        for i in range(n):
            vi = nums[i]
            for j in range(n):
                and_val = vi & nums[j]
                complement = MAX_MASK ^ and_val
                ans += f[complement]
        return ans
```

## Python3

```python
class Solution:
    def countTriplets(self, nums):
        MAX_BITS = 16
        MAX_MASK = (1 << MAX_BITS) - 1

        freq = [0] * (MAX_MASK + 1)
        for v in nums:
            freq[v] += 1

        # dp[mask] = sum of frequencies of all submasks of mask
        dp = freq[:]
        for i in range(MAX_BITS):
            bit = 1 << i
            for mask in range(MAX_MASK + 1):
                if mask & bit:
                    dp[mask] += dp[mask ^ bit]

        masks = [m for m, f in enumerate(freq) if f]
        ans = 0
        for a in masks:
            fa = freq[a]
            for b in masks:
                fb = freq[b]
                complement = (~(a & b)) & MAX_MASK
                ans += fa * fb * dp[complement]

        return ans
```

## C

```c
#include <stddef.h>

int countTriplets(int* nums, int numsSize) {
    const int BITS = 16;
    const int MAXMASK = 1 << BITS;
    static int cnt[1 << 16];
    static int supcnt[1 << 16];

    for (int i = 0; i < MAXMASK; ++i) cnt[i] = 0;
    for (int i = 0; i < numsSize; ++i) {
        cnt[nums[i]]++;
    }

    for (int mask = 0; mask < MAXMASK; ++mask) supcnt[mask] = cnt[mask];

    for (int bit = 0; bit < BITS; ++bit) {
        for (int mask = 0; mask < MAXMASK; ++mask) {
            if (mask & (1 << bit)) {
                supcnt[mask] += supcnt[mask ^ (1 << bit)];
            }
        }
    }

    long long ans = 0;
    int fullMask = MAXMASK - 1;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < numsSize; ++j) {
            int andVal = nums[i] & nums[j];
            int complement = (~andVal) & fullMask;
            ans += supcnt[complement];
        }
    }

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountTriplets(int[] nums) {
        const int BITS = 16;
        int size = 1 << BITS;
        int[] cnt = new int[size];
        foreach (int x in nums) cnt[x]++;

        int[] dp = new int[size];
        Array.Copy(cnt, dp, size);
        for (int i = 0; i < BITS; i++) {
            for (int mask = 0; mask < size; mask++) {
                if ((mask & (1 << i)) != 0) {
                    dp[mask] += dp[mask ^ (1 << i)];
                }
            }
        }

        long ans = 0;
        for (int a = 0; a < size; a++) {
            if (cnt[a] == 0) continue;
            for (int b = 0; b < size; b++) {
                if (cnt[b] == 0) continue;
                int mask = (~(a & b)) & (size - 1);
                ans += (long)cnt[a] * cnt[b] * dp[mask];
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countTriplets = function(nums) {
    const MAX_BITS = 16;
    const SIZE = 1 << MAX_BITS; // 65536
    const ALL_MASK = SIZE - 1;
    const n = nums.length;

    // Count ordered pairs (i, j) by their AND result
    const pairCnt = new Uint32Array(SIZE);
    for (let i = 0; i < n; ++i) {
        const a = nums[i];
        for (let j = 0; j < n; ++j) {
            const mask = a & nums[j];
            pairCnt[mask]++;
        }
    }

    // SOS DP: dp[mask] = sum of pairCnt[sub] for all sub ⊆ mask
    const dp = new Float64Array(SIZE);
    for (let i = 0; i < SIZE; ++i) {
        dp[i] = pairCnt[i];
    }
    for (let bit = 0; bit < MAX_BITS; ++bit) {
        const step = 1 << bit;
        for (let mask = 0; mask < SIZE; ++mask) {
            if (mask & step) {
                dp[mask] += dp[mask ^ step];
            }
        }
    }

    // For each k, add number of pairs whose AND is subset of complement of nums[k]
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const comp = (~nums[i]) & ALL_MASK;
        ans += dp[comp];
    }
    return ans;
};
```

## Typescript

```typescript
function countTriplets(nums: number[]): number {
    const MAX = 1 << 16;
    const cnt = new Uint32Array(MAX);
    for (const v of nums) cnt[v]++;

    // sup[mask]: count of numbers that are supermasks of mask
    const sup = new Uint32Array(MAX);
    sup.set(cnt);
    for (let bit = 0; bit < 16; ++bit) {
        for (let mask = 0; mask < MAX; ++mask) {
            if ((mask & (1 << bit)) === 0) {
                sup[mask] += sup[mask | (1 << bit)];
            }
        }
    }

    // pairExact[mask]: ordered pairs whose AND equals exactly mask
    const pair = new Float64Array(MAX);
    for (let i = 0; i < MAX; ++i) {
        const s = sup[i];
        pair[i] = s * s;
    }
    for (let bit = 0; bit < 16; ++bit) {
        for (let mask = 0; mask < MAX; ++mask) {
            if ((mask & (1 << bit)) === 0) {
                pair[mask] -= pair[mask | (1 << bit)];
            }
        }
    }

    // zero[mask]: count of numbers whose bits are subset of mask
    const zero = new Uint32Array(MAX);
    zero.set(cnt);
    for (let bit = 0; bit < 16; ++bit) {
        for (let mask = 0; mask < MAX; ++mask) {
            if ((mask & (1 << bit)) !== 0) {
                zero[mask] += zero[mask ^ (1 << bit)];
            }
        }
    }

    let ans = 0;
    const fullMask = MAX - 1;
    for (let mask = 0; mask < MAX; ++mask) {
        const complement = (~mask) & fullMask;
        ans += pair[mask] * zero[complement];
    }
    return Math.trunc(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countTriplets($nums) {
        $MAX_BITS = 16;
        $SIZE = 1 << $MAX_BITS;
        $cnt = array_fill(0, $SIZE, 0);
        foreach ($nums as $v) {
            $cnt[$v]++;
        }

        // submask sums: sub[mask] = sum_{s subset of mask} cnt[s]
        $sub = $cnt;
        for ($i = 0; $i < $MAX_BITS; $i++) {
            $bit = 1 << $i;
            for ($mask = 0; $mask < $SIZE; $mask++) {
                if ($mask & $bit) {
                    $sub[$mask] += $sub[$mask ^ $bit];
                }
            }
        }

        $ans = 0;
        $n = count($nums);
        $fullMask = $SIZE - 1;
        for ($i = 0; $i < $n; $i++) {
            $a = $nums[$i];
            for ($j = 0; $j < $n; $j++) {
                $andVal = $a & $nums[$j];
                $comp = (~$andVal) & $fullMask;
                $ans += $sub[$comp];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countTriplets(_ nums: [Int]) -> Int {
        let maxMask = 1 << 16
        var freq = [Int](repeating: 0, count: maxMask)
        for v in nums {
            freq[v] += 1
        }
        // SOS DP to compute sum over subsets
        var dp = freq
        for i in 0..<16 {
            let bit = 1 << i
            for mask in 0..<maxMask {
                if (mask & bit) != 0 {
                    dp[mask] += dp[mask ^ bit]
                }
            }
        }
        var result: Int64 = 0
        for a in nums {
            for b in nums {
                let m = a & b
                let complement = (~m) & (maxMask - 1)
                result += Int64(dp[complement])
            }
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countTriplets(nums: IntArray): Int {
        val MAX = 1 shl 16
        val freq = IntArray(MAX)
        for (v in nums) {
            freq[v]++
        }
        val dp = freq.clone()
        for (i in 0 until 16) {
            for (mask in 0 until MAX) {
                if ((mask and (1 shl i)) != 0) {
                    dp[mask] += dp[mask xor (1 shl i)]
                }
            }
        }
        val values = mutableListOf<Int>()
        for (i in 0 until MAX) {
            if (freq[i] > 0) values.add(i)
        }
        var ans = 0L
        val fullMask = MAX - 1
        for (a in values) {
            val fa = freq[a].toLong()
            for (b in values) {
                val fb = freq[b].toLong()
                val andVal = a and b
                val complement = fullMask xor andVal
                val cntC = dp[complement].toLong()
                ans += fa * fb * cntC
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countTriplets(List<int> nums) {
    const int MAX_BITS = 16;
    const int SIZE = 1 << MAX_BITS;
    const int MASK = SIZE - 1;

    // frequency of each value
    List<int> freq = List.filled(SIZE, 0);
    for (int x in nums) {
      freq[x]++;
    }

    // dp[mask] = number of elements that are submasks of mask
    List<int> dp = List.from(freq);
    for (int i = 0; i < MAX_BITS; i++) {
      int bit = 1 << i;
      for (int mask = 0; mask < SIZE; mask++) {
        if ((mask & bit) != 0) {
          dp[mask] += dp[mask ^ bit];
        }
      }
    }

    int ans = 0;
    for (int a in nums) {
      for (int b in nums) {
        int v = a & b;
        int complement = (~v) & MASK;
        ans += dp[complement];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countTriplets(nums []int) int {
	const MAX = 1 << 16
	freq := make([]int, MAX)
	for _, v := range nums {
		freq[v]++
	}
	dp := make([]int, MAX)
	copy(dp, freq)
	for i := 0; i < 16; i++ {
		bit := 1 << i
		for mask := 0; mask < MAX; mask++ {
			if mask&bit != 0 {
				dp[mask] += dp[mask^bit]
			}
		}
	}
	vals := make([]int, 0)
	for v, f := range freq {
		if f > 0 {
			vals = append(vals, v)
		}
	}
	var ans int64
	maskAll := MAX - 1
	for _, a := range vals {
		fa := freq[a]
		for _, b := range vals {
			fb := freq[b]
			pair := int64(fa) * int64(fb)
			m := ^(a & b) & maskAll
			ans += pair * int64(dp[m])
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def count_triplets(nums)
  max_bits = 16
  size = 1 << max_bits
  freq = Array.new(size, 0)
  nums.each { |v| freq[v] += 1 }

  f = freq.clone
  (0...max_bits).each do |i|
    (0...size).each do |mask|
      if (mask & (1 << i)).zero?
        f[mask] += f[mask | (1 << i)]
      end
    end
  end

  g = Array.new(size, 0)
  (0...size).each { |mask| g[mask] = f[mask] * f[mask] }

  pair_exact = g.clone
  (0...max_bits).each do |i|
    (0...size).each do |mask|
      if (mask & (1 << i)).zero?
        pair_exact[mask] -= pair_exact[mask | (1 << i)]
      end
    end
  end

  total = 0
  all_mask = size - 1
  (0...size).each do |c|
    cnt = freq[c]
    next if cnt.zero?
    complement = all_mask ^ c
    total += cnt * pair_exact[complement]
  end

  total
end
```

## Scala

```scala
object Solution {
    def countTriplets(nums: Array[Int]): Int = {
        val MAX = 1 << 16
        val freq = new Array[Int](MAX)
        for (v <- nums) {
            freq(v) += 1
        }
        // SOS DP to compute sum over submasks
        val dp = freq.clone()
        var i = 0
        while (i < 16) {
            var mask = 0
            while (mask < MAX) {
                if ((mask & (1 << i)) != 0) {
                    dp(mask) += dp(mask ^ (1 << i))
                }
                mask += 1
            }
            i += 1
        }

        var ans: Long = 0L
        val n = nums.length
        var aIdx = 0
        while (aIdx < n) {
            val a = nums(aIdx)
            var bIdx = 0
            while (bIdx < n) {
                val mask = a & nums(bIdx)
                val complement = (~mask) & (MAX - 1)
                ans += dp(complement)
                bIdx += 1
            }
            aIdx += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_triplets(nums: Vec<i32>) -> i32 {
        const BITS: usize = 16;
        let size = 1usize << BITS;
        let mut cnt = vec![0i32; size];
        for &v in &nums {
            cnt[v as usize] += 1;
        }
        // SOS DP to compute sum over subsets
        let mut f = cnt.clone();
        for i in 0..BITS {
            for mask in 0..size {
                if (mask & (1 << i)) != 0 {
                    let without = mask ^ (1 << i);
                    f[mask] += f[without];
                }
            }
        }

        let full_mask = size - 1;
        let mut ans: i64 = 0;
        for &a in &nums {
            for &b in &nums {
                let and = (a & b) as usize;
                let comp = (!and) & full_mask;
                ans += f[comp] as i64;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((bits 16)
         (size (arithmetic-shift 1 bits))
         (mask-all (sub1 size))                     ; all 16 bits set
         (freq (make-vector size 0)))
    ;; frequency of each value
    (for ([v (in-list nums)])
      (vector-set! freq v (+ (vector-ref freq v) 1)))
    ;; SOS DP: g[mask] = sum_{submask ⊆ mask} freq[submask]
    (let ((g (vector-copy freq)))
      (for ([b (in-range bits)])
        (let ((bit (arithmetic-shift 1 b)))
          (for ([m (in-range size)])
            (when (positive? (bitwise-and m bit))
              (let* ((without (bitwise-xor m bit))
                     (new-val (+ (vector-ref g m) (vector-ref g without))))
                (vector-set! g m new-val))))))
      ;; count triples
      (let* ((arr (list->vector nums))
             (n (vector-length arr)))
        (let loop ((i 0) (ans 0))
          (if (= i n)
              ans
              (let inner-loop ((j 0) (partial ans))
                (if (= j n)
                    (loop (+ i 1) partial)
                    (let* ((x (bitwise-and (vector-ref arr i) (vector-ref arr j)))
                           (comp (bitwise-and (lognot x) mask-all))
                           (add (vector-ref g comp)))
                      (inner-loop (+ j 1) (+ partial add)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_triplets/1]).

-define(BITS, 16).
-define(SIZE, 1 bsl ?BITS).

count_triplets(Nums) ->
    All = (1 bsl ?BITS) - 1,
    % Build frequency array
    Cnt0 = array:new(?SIZE, {default,0}),
    Cnt = lists:foldl(fun(N, Acc) ->
                Old = array:get(N, Acc),
                array:set(N, Old + 1, Acc)
            end, Cnt0, Nums),

    % SOS DP over supersets to compute supcnt[mask] = sum_{x superset mask} cnt[x]
    SupCnt = supdp(0, ?BITS, Cnt),

    % Count triples
    lists:foldl(fun(A, AccA) ->
        lists:foldl(fun(B, AccB) ->
            Mask = band(A, B),
            Complement = bxor(Mask, All),
            CountC = array:get(Complement, SupCnt),
            AccB + CountC
        end, AccA, Nums)
    end, 0, Nums).

% supdp(BitIdx, MaxBits, Array) -> Array after processing bits [BitIdx..MaxBits-1]
supdp(BitIdx, MaxBits, Arr) when BitIdx < MaxBits ->
    Arr2 = supdp_mask(0, ?SIZE, BitIdx, Arr),
    supdp(BitIdx + 1, MaxBits, Arr2);
supdp(_, _, Arr) -> Arr.

% supdp_mask(Index, Size, Bit, Array) updates entries where bit is not set
supdp_mask(Index, Size, Bit, Arr) when Index < Size ->
    case (Index band (1 bsl Bit)) of
        0 ->
            Val = array:get(Index, Arr),
            AddVal = array:get(Index bor (1 bsl Bit), Arr),
            NewArr = array:set(Index, Val + AddVal, Arr),
            supdp_mask(Index + 1, Size, Bit, NewArr);
        _ ->
            supdp_mask(Index + 1, Size, Bit, Arr)
    end;
supdp_mask(_, _, _, Arr) -> Arr.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_triplets(nums :: [integer]) :: integer
  def count_triplets(nums) do
    size = 1 <<< 16
    table = :ets.new(:pair_counts, [:set, :private])

    for a <- nums do
      for b <- nums do
        mask = a &&& b
        :ets.update_counter(table, mask, {2, 1}, {mask, 0})
      end
    end

    dp =
      Enum.reduce(0..size - 1, :array.new(size, default: 0), fn i, acc ->
        case :ets.lookup(table, i) do
          [{^i, val}] -> :array.set(i, val, acc)
          [] -> acc
        end
      end)

    dp =
      Enum.reduce(0..15, dp, fn bit, arr ->
        step = 1 <<< bit

        Enum.reduce(0..size - 1, arr, fn mask, a2 ->
          if (mask &&& step) != 0 do
            val = :array.get(mask, a2)
            add = :array.get(mask ^^^ step, a2)
            :array.set(mask, val + add, a2)
          else
            a2
          end
        end)
      end)

    Enum.reduce(nums, 0, fn x, acc ->
      complement = (size - 1) ^^^ x
      acc + :array.get(complement, dp)
    end)
  end
end
```
