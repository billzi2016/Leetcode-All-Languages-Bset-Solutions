# 2897. Apply Operations on Array to Maximize Sum of Squares

## Cpp

```cpp
class Solution {
public:
    int maxSum(std::vector<int>& nums, int k) {
        const int MAX_BIT = 31; // since nums[i] <= 1e9 < 2^30
        std::vector<int> cnt(MAX_BIT, 0);
        for (int x : nums) {
            for (int b = 0; b < MAX_BIT; ++b) {
                if (x & (1 << b)) ++cnt[b];
            }
        }
        int m = 0;
        for (int c : cnt) if (c > m) m = c;
        std::vector<long long> a(m, 0);
        for (int b = 0; b < MAX_BIT; ++b) {
            long long val = 1LL << b;
            int c = cnt[b];
            for (int i = 0; i < c; ++i) {
                a[i] += val;
            }
        }
        std::sort(a.begin(), a.end(), std::greater<long long>());
        const long long MOD = 1000000007LL;
        long long ans = 0;
        for (int i = 0; i < k && i < (int)a.size(); ++i) {
            long long v = a[i] % MOD;
            ans = (ans + v * v) % MOD;
        }
        // remaining selections contribute zero
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSum(java.util.List<Integer> nums, int k) {
        final long MOD = 1_000_000_007L;
        int n = nums.size();
        int[] bitCnt = new int[31];
        for (int val : nums) {
            for (int b = 0; b < 31; ++b) {
                if (((val >> b) & 1) == 1) {
                    bitCnt[b]++;
                }
            }
        }

        long[] constructed = new long[n];
        for (int i = 0; i < n; ++i) {
            long cur = 0L;
            for (int b = 0; b < 31; ++b) {
                if (bitCnt[b] > 0) {
                    cur |= (1L << b);
                    bitCnt[b]--;
                }
            }
            constructed[i] = cur;
        }

        java.util.Arrays.sort(constructed);
        long ans = 0L;
        for (int i = n - 1; i >= n - k && i >= 0; --i) {
            long v = constructed[i] % MOD;
            ans = (ans + v * v) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # count how many times each bit appears in the whole array
        cnt = [0] * 31  # since nums[i] <= 1e9 < 2^30
        for x in nums:
            b = 0
            while x:
                if x & 1:
                    cnt[b] += 1
                x >>= 1
                b += 1

        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(31):
                if cnt[b]:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD
        return ans
```

## Python3

```python
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        # count set bits at each position
        cnt = [0] * 31
        for x in nums:
            b = 0
            while x:
                if x & 1:
                    cnt[b] += 1
                x >>= 1
                b += 1
        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(31):
                if cnt[b]:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD
        return ans
```

## C

```c
int maxSum(int* nums, int numsSize, int k) {
    const int MOD = 1000000007;
    long long cnt[31] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        for (int b = 0; b < 31; ++b) {
            if (x & (1 << b)) cnt[b]++;
        }
    }
    long long ans = 0;
    for (int i = 0; i < k; ++i) {
        long long val = 0;
        for (int b = 0; b < 31; ++b) {
            if (cnt[b] > 0) {
                val |= (1LL << b);
                cnt[b]--;
            }
        }
        long long vmod = val % MOD;
        ans += (vmod * vmod) % MOD;
        if (ans >= MOD) ans -= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSum(IList<int> nums, int k) {
        const long MOD = 1000000007L;
        const int MAX_BIT = 31; // bits 0..30 sufficient for nums[i] <= 1e9
        long[] bitCount = new long[MAX_BIT];
        foreach (int num in nums) {
            int x = num;
            for (int b = 0; b < MAX_BIT; ++b) {
                if (((x >> b) & 1) == 1) bitCount[b]++;
            }
        }

        long[] top = new long[k];
        for (int b = MAX_BIT - 1; b >= 0; --b) {
            long cnt = bitCount[b];
            int limit = (int)Math.Min(cnt, k);
            long add = 1L << b;
            for (int i = 0; i < limit; ++i) {
                top[i] += add;
            }
        }

        long ans = 0;
        foreach (long val in top) {
            long v = val % MOD;
            ans = (ans + v * v) % MOD;
        }
        return (int)ans;
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
var maxSum = function(nums, k) {
    const n = nums.length;
    const cnt = new Array(31).fill(0);
    for (let i = 0; i < n; i++) {
        const val = nums[i];
        for (let b = 0; b < 31; b++) {
            if ((val >>> b) & 1) cnt[b]++;
        }
    }
    const arr = new Array(n).fill(0);
    for (let b = 0; b < 31; b++) {
        const c = cnt[b];
        if (c === 0) continue;
        const add = 1 << b;
        for (let i = 0; i < c; i++) {
            arr[i] += add;
        }
    }
    arr.sort((a, b) => b - a);
    const MOD = 1000000007n;
    let ans = 0n;
    for (let i = 0; i < k; i++) {
        const v = BigInt(arr[i]);
        ans = (ans + v * v) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function maxSum(nums: number[], k: number): number {
    const MOD = 1000000007n;
    const BIT = 31; // enough for nums[i] <= 1e9
    const cnt = new Array(BIT).fill(0);
    for (const num of nums) {
        let x = num;
        for (let b = 0; b < BIT; ++b) {
            if ((x & (1 << b)) !== 0) cnt[b]++;
        }
    }

    let ans = 0n;
    for (let i = 0; i < k; ++i) {
        let val = 0n;
        for (let b = 0; b < BIT; ++b) {
            if (cnt[b] > i) {
                val |= (1n << BigInt(b));
            }
        }
        ans = (ans + (val * val) % MOD) % MOD;
    }

    return Number(ans);
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
    function maxSum($nums, $k) {
        $cnt = array_fill(0, 31, 0);
        foreach ($nums as $num) {
            for ($b = 0; $b < 31; $b++) {
                if ((($num >> $b) & 1) === 1) {
                    $cnt[$b]++;
                }
            }
        }

        $mod = 1000000007;
        $ans = 0;

        for ($i = 0; $i < $k; $i++) {
            $val = 0;
            for ($b = 0; $b < 31; $b++) {
                if ($cnt[$b] > $i) {
                    $val |= (1 << $b);
                }
            }
            $vMod = $val % $mod;
            $sq = ($vMod * $vMod) % $mod;
            $ans = ($ans + $sq) % $mod;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        var bitCount = Array(repeating: 0, count: 31)
        for num in nums {
            var x = num
            var b = 0
            while x > 0 {
                if (x & 1) == 1 {
                    bitCount[b] += 1
                }
                b += 1
                x >>= 1
            }
        }
        var result: Int64 = 0
        for _ in 0..<k {
            var cur = 0
            for b in 0..<31 {
                if bitCount[b] > 0 {
                    cur |= (1 << b)
                    bitCount[b] -= 1
                }
            }
            let val = Int64(cur)
            result = (result + (val * val) % Int64(MOD)) % Int64(MOD)
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums: List<Int>, k: Int): Int {
        val cnt = IntArray(31)
        for (v in nums) {
            var x = v
            var i = 0
            while (x != 0) {
                if ((x and 1) == 1) cnt[i]++
                x = x ushr 1
                i++
            }
        }
        val MOD = 1_000_000_007L
        var ans = 0L
        repeat(k) {
            var cur = 0L
            for (i in 0..30) {
                if (cnt[i] > 0) {
                    cur += 1L shl i
                    cnt[i]--
                }
            }
            val sq = (cur % MOD) * (cur % MOD) % MOD
            ans = (ans + sq) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int maxSum(List<int> nums, int k) {
    int n = nums.length;
    // Count set bits for each position (0..30)
    List<int> bitCount = List.filled(31, 0);
    for (int num in nums) {
      int x = num;
      int b = 0;
      while (x > 0) {
        if ((x & 1) == 1) {
          bitCount[b]++;
        }
        x >>= 1;
        b++;
      }
    }

    // Build numbers by distributing bits greedily to the first positions
    List<int> vals = List.filled(n, 0);
    for (int b = 0; b < 31; ++b) {
      int mask = 1 << b;
      int cnt = bitCount[b];
      for (int i = 0; i < cnt; ++i) {
        vals[i] += mask;
      }
    }

    // The array is non‑increasing, so the first k elements are the largest
    int ans = 0;
    for (int i = 0; i < k; ++i) {
      int v = vals[i] % _mod;
      ans = (ans + (v * v) % _mod) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func maxSum(nums []int, k int) int {
	const MOD int64 = 1000000007
	// count bits up to 30 (since nums[i] <= 1e9 < 2^30)
	bitCnt := make([]int, 31)
	for _, v := range nums {
		x := v
		b := 0
		for x > 0 {
			if x&1 == 1 {
				bitCnt[b]++
			}
			x >>= 1
			b++
		}
	}
	var ans int64 = 0
	for i := 0; i < k; i++ {
		var cur int64 = 0
		for b := 0; b <= 30; b++ {
			if bitCnt[b] > 0 {
				cur |= 1 << b
				bitCnt[b]--
			}
		}
		curMod := cur % MOD
		ans = (ans + curMod*curMod) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def max_sum(nums, k)
  mod = 1_000_000_007
  cnt = Array.new(31, 0)

  nums.each do |num|
    bit = 0
    while num > 0
      cnt[bit] += 1 if (num & 1) == 1
      num >>= 1
      bit += 1
    end
  end

  result = 0
  k.times do
    cur = 0
    31.times do |b|
      if cnt[b] > 0
        cur |= (1 << b)
        cnt[b] -= 1
      end
    end
    result = (result + (cur * cur) % mod) % mod
  end

  result
end
```

## Scala

```scala
object Solution {
    def maxSum(nums: List[Int], k: Int): Int = {
        val MOD = 1000000007L
        val cnt = new Array[Int](31)
        for (num <- nums) {
            var x = num
            var b = 0
            while (b < 31) {
                if ((x & 1) == 1) cnt(b) += 1
                x >>= 1
                b += 1
            }
        }
        var ans = 0L
        var i = 0
        while (i < k) {
            var cur = 0L
            var b = 0
            while (b < 31) {
                if (cnt(b) > i) cur += (1L << b)
                b += 1
            }
            val sq = (cur % MOD) * (cur % MOD) % MOD
            ans = (ans + sq) % MOD
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i32; 31];
        for &num in nums.iter() {
            let x = num as u32;
            for b in 0..31 {
                if (x >> b) & 1 == 1 {
                    cnt[b] += 1;
                }
            }
        }

        let mut ans: i64 = 0;
        for _ in 0..k as usize {
            let mut cur: u64 = 0;
            for b in 0..31 {
                if cnt[b] > 0 {
                    cur |= 1u64 << b;
                    cnt[b] -= 1;
                }
            }
            let cur_mod = (cur % MOD as u64) as i64;
            ans = (ans + cur_mod * cur_mod % MOD) % MOD;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (max-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([cnt (make-vector 31 0)]
        [ans 0])
    ;; count bits in all numbers
    (for ([num nums])
      (let loop ((b 0))
        (when (< b 31)
          (when (not (= (bitwise-and num (arithmetic-shift 1 b)) 0))
            (vector-set! cnt b (+ (vector-ref cnt b) 1)))
          (loop (+ b 1)))))
    ;; construct k numbers greedily
    (for ([i (in-range k)])
      (let* ([cur
              (let loop ((b 0) (val 0))
                (if (= b 31)
                    val
                    (let ([c (vector-ref cnt b)])
                      (if (> c 0)
                          (begin
                            (vector-set! cnt b (- c 1))
                            (loop (+ b 1) (bitwise-ior val (arithmetic-shift 1 b))))
                          (loop (+ b 1) val)))))])
        (set! ans (modulo (+ ans (modulo (* cur cur) MOD)) MOD))))
    ans))
```

## Erlang

```erlang
-spec max_sum(Nums :: [integer()], K :: integer()) -> integer().
max_sum(Nums, K) ->
    Counts = count_bits(Nums),
    Mod = 1000000007,
    loop(0, K, Counts, Mod, 0).

%% Count set bits for positions 0..30
count_bits(Nums) ->
    count_bits(Nums, 30, []).

count_bits(_Nums, -1, Acc) -> lists:reverse(Acc);
count_bits(Nums, Bit, Acc) ->
    Mask = 1 bsl Bit,
    C = lists:foldl(fun(N, Sum) ->
                        if (N band Mask) =/= 0 -> Sum + 1; true -> Sum end
                    end, 0, Nums),
    count_bits(Nums, Bit - 1, [C | Acc]).

%% Compute value for the i‑th largest element
calc_val(Counts, I) ->
    calc_val(Counts, I, 0, 0).

calc_val([], _I, _Bit, Acc) -> Acc;
calc_val([C|Cs], I, Bit, Acc) ->
    NewAcc = if C > I -> Acc + (1 bsl Bit); true -> Acc end,
    calc_val(Cs, I, Bit + 1, NewAcc).

%% Tail‑recursive accumulation of the answer
loop(I, K, _Counts, _Mod, Acc) when I == K -> Acc;
loop(I, K, Counts, Mod, Acc) ->
    Val = calc_val(Counts, I),
    Square = (Val rem Mod) * (Val rem Mod) rem Mod,
    NewAcc = (Acc + Square) rem Mod,
    loop(I + 1, K, Counts, Mod, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec max_sum(nums :: [integer], k :: integer) :: integer
  def max_sum(nums, k) do
    mod = 1_000_000_007
    max_bit = 30

    cnt_array =
      Enum.reduce(nums, :array.new(max_bit + 1, default: 0), fn num, arr ->
        Enum.reduce(0..max_bit, arr, fn p, a ->
          if ((num >>> p) &&& 1) == 1 do
            cur = :array.get(p, a)
            :array.set(p, cur + 1, a)
          else
            a
          end
        end)
      end)

    Enum.reduce(0..k - 1, 0, fn i, acc ->
      val =
        Enum.reduce(0..max_bit, 0, fn p, v ->
          c = :array.get(p, cnt_array)

          if i < c do
            v + (1 <<< p)
          else
            v
          end
        end)

      (acc + rem(val * val, mod)) |> rem(mod)
    end)
  end
end
```
