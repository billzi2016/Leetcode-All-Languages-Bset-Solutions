# 1862. Sum of Floored Pairs

## Cpp

```cpp
class Solution {
public:
    int sumOfFlooredPairs(vector<int>& nums) {
        const int MOD = 1'000'000'007;
        int maxA = 0;
        for (int x : nums) if (x > maxA) maxA = x;
        vector<int> cnt(maxA + 1, 0);
        for (int x : nums) ++cnt[x];
        vector<int> pref(maxA + 1, 0);
        for (int i = 1; i <= maxA; ++i) {
            pref[i] = pref[i - 1] + cnt[i];
        }
        long long ans = 0;
        for (int v = 1; v <= maxA; ++v) {
            if (!cnt[v]) continue;
            int k = 1;
            for (int start = v; start <= maxA; ++k, start += v) {
                int l = start;
                int r = min(start + v - 1, maxA);
                long long rangeCount = pref[r] - pref[l - 1];
                if (rangeCount == 0) continue;
                ans = (ans + (long long)cnt[v] * k % MOD * (rangeCount % MOD)) % MOD;
            }
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int sumOfFlooredPairs(int[] nums) {
        int max = 0;
        for (int v : nums) if (v > max) max = v;
        int[] freq = new int[max + 1];
        for (int v : nums) freq[v]++;
        long[] pref = new long[max + 1];
        pref[0] = freq[0];
        for (int i = 1; i <= max; i++) {
            pref[i] = pref[i - 1] + freq[i];
        }
        long ans = 0;
        for (int v = 1; v <= max; v++) {
            if (freq[v] == 0) continue;
            for (int multiple = v; multiple <= max; multiple += v) {
                int high = Math.min(max, multiple + v - 1);
                long cnt = pref[high] - (multiple > 0 ? pref[multiple - 1] : 0);
                if (cnt == 0) continue;
                long k = multiple / v;
                ans = (ans + ((long) freq[v] * cnt % MOD) * k) % MOD;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfFlooredPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        pref = [0] * (max_val + 1)
        s = 0
        for i in range(max_val + 1):
            s += freq[i]
            pref[i] = s

        ans = 0
        for v in range(1, max_val + 1):
            fv = freq[v]
            if not fv:
                continue
            limit = max_val // v
            for k in range(1, limit + 1):
                low = k * v
                high = min((k + 1) * v - 1, max_val)
                cnt = pref[high] - (pref[low - 1] if low > 0 else 0)
                if cnt:
                    ans = (ans + fv * cnt * k) % MOD
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        pref = [0] * (max_val + 1)
        cur = 0
        for i in range(max_val + 1):
            cur += freq[i]
            pref[i] = cur

        ans = 0
        for v in range(1, max_val + 1):
            fv = freq[v]
            if fv == 0:
                continue
            for m in range(v, max_val + 1, v):
                l = m
                r = min(m + v - 1, max_val)
                cnt = pref[r] - (pref[l - 1] if l > 0 else 0)
                if cnt == 0:
                    continue
                q = m // v
                ans = (ans + fv * cnt % MOD * q) % MOD

        return ans % MOD
```

## C

```c
#include <string.h>

int sumOfFlooredPairs(int* nums, int numsSize) {
    const int MOD = 1000000007;
    int maxV = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxV) maxV = nums[i];

    static int freq[100001];
    memset(freq, 0, (maxV + 1) * sizeof(int));
    for (int i = 0; i < numsSize; ++i)
        ++freq[nums[i]];

    static int pref[100001];
    pref[0] = 0;
    for (int i = 1; i <= maxV; ++i)
        pref[i] = pref[i - 1] + freq[i];

    long long ans = 0;
    for (int d = 1; d <= maxV; ++d) {
        if (!freq[d]) continue;
        int fd = freq[d];
        for (int k = 1; k * d <= maxV; ++k) {
            int l = k * d;
            int r = (k + 1) * d - 1;
            if (r > maxV) r = maxV;
            int cnt = pref[r] - pref[l - 1];
            if (!cnt) continue;
            long long add = ((long long)fd * cnt) % MOD;
            add = (add * k) % MOD;
            ans += add;
            if (ans >= MOD) ans -= MOD;
        }
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int SumOfFlooredPairs(int[] nums) {
        int n = nums.Length;
        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        int[] freq = new int[maxVal + 1];
        foreach (int v in nums) freq[v]++;

        long[] pref = new long[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            pref[i] = pref[i - 1] + freq[i];
        }

        long ans = 0;
        for (int a = 1; a <= maxVal; a++) {
            int fa = freq[a];
            if (fa == 0) continue;
            for (int k = 1; k * a <= maxVal; k++) {
                int left = k * a;
                int right = Math.Min((k + 1) * a - 1, maxVal);
                long cnt = pref[right] - pref[left - 1];
                if (cnt == 0) continue;
                long add = ((long)fa * cnt) % MOD;
                add = (add * k) % MOD;
                ans += add;
                if (ans >= MOD) ans -= MOD;
            }
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfFlooredPairs = function(nums) {
    const MOD = 1000000007;
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;

    const freq = new Array(maxVal + 1).fill(0);
    for (const v of nums) freq[v]++;

    const pref = new Array(maxVal + 1).fill(0);
    let sum = 0;
    for (let i = 1; i <= maxVal; ++i) {
        sum += freq[i];
        pref[i] = sum;
    }

    let ans = 0;
    for (let d = 1; d <= maxVal; ++d) {
        const fd = freq[d];
        if (!fd) continue;
        let q = 1;
        for (let left = d; left <= maxVal; left += d, ++q) {
            const right = Math.min(left + d - 1, maxVal);
            const cnt = pref[right] - pref[left - 1];
            if (!cnt) continue;
            const contrib = (q * cnt) % MOD;
            ans = (ans + fd * contrib) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function sumOfFlooredPairs(nums: number[]): number {
    const MOD = 1_000_000_007;
    const n = nums.length;
    let maxVal = 0;
    for (let v of nums) if (v > maxVal) maxVal = v;

    const freq = new Uint32Array(maxVal + 2);
    for (let v of nums) freq[v]++;

    const prefix = new Uint32Array(maxVal + 2);
    for (let i = 1; i <= maxVal; ++i) {
        prefix[i] = prefix[i - 1] + freq[i];
    }

    let ans = 0;
    for (let v = 1; v <= maxVal; ++v) {
        const fv = freq[v];
        if (fv === 0) continue;
        let k = 1;
        for (let mult = v; mult <= maxVal; mult += v, ++k) {
            const l = mult;
            const r = Math.min(mult + v - 1, maxVal);
            const cnt = prefix[r] - (l > 1 ? prefix[l - 1] : 0);
            if (cnt === 0) continue;
            const add = ((fv * cnt) % MOD) * k % MOD;
            ans += add;
            if (ans >= MOD) ans -= MOD;
        }
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
    function sumOfFlooredPairs($nums) {
        $MOD = 1000000007;
        $maxVal = max($nums);
        $freq = array_fill(0, $maxVal + 1, 0);
        foreach ($nums as $v) {
            $freq[$v]++;
        }

        // prefix sums of frequencies
        $pref = array_fill(0, $maxVal + 1, 0);
        for ($i = 1; $i <= $maxVal; $i++) {
            $pref[$i] = $pref[$i - 1] + $freq[$i];
        }

        $ans = 0;
        for ($v = 1; $v <= $maxVal; $v++) {
            if ($freq[$v] == 0) continue;
            $fv = $freq[$v];
            // iterate over multiples of v
            for ($k = 1, $l = $v; $l <= $maxVal; $k++, $l += $v) {
                $r = $l + $v - 1;
                if ($r > $maxVal) $r = $maxVal;
                $cnt = $pref[$r] - $pref[$l - 1];
                if ($cnt == 0) continue;
                // contribution: fv * cnt * k
                $add = ($fv % $MOD) * ($cnt % $MOD) % $MOD;
                $add = $add * ($k % $MOD) % $MOD;
                $ans += $add;
                if ($ans >= $MOD) $ans -= $MOD;
            }
        }

        return $ans % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfFlooredPairs(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        guard let maxVal = nums.max() else { return 0 }
        var freq = [Int](repeating: 0, count: maxVal + 1)
        for v in nums {
            freq[v] += 1
        }
        var pref = [Int](repeating: 0, count: maxVal + 1)
        var running = 0
        for i in 0...maxVal {
            running += freq[i]
            pref[i] = running
        }
        var ans: Int64 = 0
        for v in 1...maxVal where freq[v] > 0 {
            var multiple = v
            while multiple <= maxVal {
                let k = multiple / v
                let left = multiple
                let right = min(multiple + v - 1, maxVal)
                let cntInRange = pref[right] - (left > 0 ? pref[left - 1] : 0)
                if cntInRange > 0 {
                    let add = (Int64(freq[v]) * Int64(cntInRange) % Int64(MOD)) * Int64(k) % Int64(MOD)
                    ans += add
                    if ans >= Int64(MOD) { ans %= Int64(MOD) }
                }
                multiple += v
            }
        }
        return Int(ans % Int64(MOD))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfFlooredPairs(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        var maxVal = 0
        for (num in nums) if (num > maxVal) maxVal = num
        val freq = IntArray(maxVal + 1)
        for (num in nums) freq[num]++
        val pref = LongArray(maxVal + 1)
        var acc = 0L
        for (i in 0..maxVal) {
            acc += freq[i].toLong()
            pref[i] = acc
        }
        var ans = 0L
        for (v in 1..maxVal) {
            val fv = freq[v]
            if (fv == 0) continue
            var multiple = v
            while (multiple <= maxVal) {
                val l = multiple
                val r = kotlin.math.min(multiple + v - 1, maxVal)
                val cnt = pref[r] - if (l > 0) pref[l - 1] else 0L
                val q = (multiple / v).toLong()
                ans += fv.toLong() * cnt % MOD * q % MOD
                if (ans >= MOD) ans %= MOD
                multiple += v
            }
        }
        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumOfFlooredPairs(List<int> nums) {
    const int MOD = 1000000007;
    int maxVal = 0;
    for (var v in nums) {
      if (v > maxVal) maxVal = v;
    }
    List<int> freq = List.filled(maxVal + 1, 0);
    for (var v in nums) {
      freq[v]++;
    }

    // prefix sum of frequencies
    List<int> pref = List.filled(maxVal + 1, 0);
    int running = 0;
    for (int i = 0; i <= maxVal; i++) {
      running += freq[i];
      pref[i] = running;
    }

    int ans = 0;

    for (int x = 1; x <= maxVal; x++) {
      if (freq[x] == 0) continue;
      int mult = x;
      int k = 1;
      while (mult <= maxVal) {
        int l = mult;
        int r = mult + x - 1;
        if (r > maxVal) r = maxVal;
        int cnt = pref[r] - pref[l - 1];
        if (cnt != 0) {
          int add = ((freq[x] * cnt) % MOD);
          add = (add * k) % MOD;
          ans += add;
          if (ans >= MOD) ans -= MOD;
        }
        mult += x;
        k++;
      }
    }

    return ans % MOD;
  }
}
```

## Golang

```go
func sumOfFlooredPairs(nums []int) int {
	const MOD int64 = 1000000007
	maxV := 0
	for _, v := range nums {
		if v > maxV {
			maxV = v
		}
	}
	freq := make([]int64, maxV+2)
	for _, v := range nums {
		freq[v]++
	}
	prefix := make([]int64, maxV+2)
	for i := 1; i <= maxV; i++ {
		prefix[i] = prefix[i-1] + freq[i]
	}

	var ans int64
	for d := 1; d <= maxV; d++ {
		if freq[d] == 0 {
			continue
		}
		fd := freq[d] % MOD
		for k := 1; k*d <= maxV; k++ {
			l := k * d
			r := (k+1)*d - 1
			if r > maxV {
				r = maxV
			}
			cnt := prefix[r] - prefix[l-1]
			ans = (ans + fd*int64(k)%MOD*(cnt%MOD)) % MOD
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def sum_of_floored_pairs(nums)
  mod = 1_000_000_007
  max_val = nums.max
  freq = Array.new(max_val + 1, 0)
  nums.each { |v| freq[v] += 1 }

  pref = Array.new(max_val + 1, 0)
  (1..max_val).each do |i|
    pref[i] = pref[i - 1] + freq[i]
  end

  ans = 0
  (1..max_val).each do |x|
    next if freq[x].zero?
    k = 1
    while (l = x * k) <= max_val
      r = [x * (k + 1) - 1, max_val].min
      cnt = pref[r] - pref[l - 1]
      unless cnt.zero?
        ans += freq[x] * cnt % mod * k
        ans %= mod
      end
      k += 1
    end
  end

  ans % mod
end
```

## Scala

```scala
object Solution {
    def sumOfFlooredPairs(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        if (nums.isEmpty) return 0
        val maxVal = nums.max
        val freq = new Array[Int](maxVal + 1)
        for (x <- nums) freq(x) += 1

        val prefix = new Array[Long](maxVal + 1)
        var acc: Long = 0L
        var i = 1
        while (i <= maxVal) {
            acc += freq(i)
            prefix(i) = acc
            i += 1
        }

        var ans: Long = 0L
        var v = 1
        while (v <= maxVal) {
            val fv = freq(v)
            if (fv > 0) {
                var k = 1
                while (k * v <= maxVal) {
                    val l = k * v
                    val r = math.min(l + v - 1, maxVal)
                    val cntInRange = prefix(r) - (if (l > 1) prefix(l - 1) else 0L)
                    if (cntInRange != 0) {
                        ans += fv.toLong * cntInRange % MOD * k % MOD
                        if (ans >= MOD) ans %= MOD
                    }
                    k += 1
                }
            }
            v += 1
        }

        (ans % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_floored_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut cnt = vec![0i64; max_val + 1];
        for &x in &nums {
            cnt[x as usize] += 1;
        }
        // prefix sums of counts
        let mut pref = vec![0i64; max_val + 1];
        pref[0] = cnt[0];
        for i in 1..=max_val {
            pref[i] = pref[i - 1] + cnt[i];
        }

        let mut ans: i64 = 0;
        for v in 1..=max_val {
            let cv = cnt[v];
            if cv == 0 {
                continue;
            }
            let mut m = v;
            while m <= max_val {
                let k = (m / v) as i64;
                let l = m;
                let r = std::cmp::min(m + v - 1, max_val);
                let cnt_range = pref[r] - if l > 0 { pref[l - 1] } else { 0 };
                let add = cv % MOD * (cnt_range % MOD) % MOD * (k % MOD) % MOD;
                ans += add;
                if ans >= MOD {
                    ans -= MOD;
                }
                m += v;
            }
        }

        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (sum-of-floored-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((maxV (apply max nums))
         (freq (make-vector (add1 maxV) 0)))
    ;; count frequencies
    (for ([x nums])
      (vector-set! freq x (+ (vector-ref freq x) 1)))
    ;; prefix sums of frequencies
    (define pref (make-vector (add1 maxV) 0))
    (let loop ((i 1) (acc 0))
      (when (<= i maxV)
        (vector-set! pref i (+ acc (vector-ref freq i)))
        (loop (add1 i) (vector-ref pref i))))
    ;; compute answer
    (define ans 0)
    (for ([a (in-range 1 (add1 maxV))])
      (let ((fa (vector-ref freq a)))
        (when (> fa 0)
          (for ([m (in-range a (add1 maxV) a)])
            (let* ((l m)
                   (r (min (+ m a -1) maxV))
                   (cnt (- (vector-ref pref r)
                           (if (= l 1) 0 (vector-ref pref (sub1 l))))))
              (when (> cnt 0)
                (let ((k (quotient m a)))
                  (set! ans (modulo (+ ans (* fa cnt k)) MOD)))))))))
    ans)))
```

## Erlang

```erlang
-export([sum_of_floored_pairs/1]).

-spec sum_of_floored_pairs([integer()]) -> integer().
sum_of_floored_pairs(Nums) ->
    Mod = 1000000007,
    MaxV = lists:max(Nums),

    %% frequency array
    Freq0 = array:new(MaxV + 1, {default, 0}),
    Freq = lists:foldl(
        fun(N, Arr) ->
            C = array:get(N, Arr),
            array:set(N, C + 1, Arr)
        end,
        Freq0,
        Nums),

    %% prefix sum array
    {_, Pref} = lists:foldl(
        fun(I, {Sum, Arr}) ->
            NewSum = Sum + array:get(I, Freq),
            {NewSum, array:set(I, NewSum, Arr)}
        end,
        {0, array:new(MaxV + 1, {default, 0})},
        lists:seq(1, MaxV)),

    loop_d(1, MaxV, Freq, Pref, Mod, 0).

loop_d(D, MaxV, _Freq, _Pref, _Mod, Acc) when D > MaxV ->
    Acc;
loop_d(D, MaxV, Freq, Pref, Mod, Acc) ->
    FD = array:get(D, Freq),
    NewAcc =
        if
            FD == 0 -> Acc;
            true -> loop_k(D, D, MaxV, D, FD, Pref, Mod, Acc)
        end,
    loop_d(D + 1, MaxV, Freq, Pref, Mod, NewAcc).

loop_k(_Step, K, MaxV, _D, _FD, _Pref, _Mod, Acc) when K > MaxV ->
    Acc;
loop_k(Step, K, MaxV, D, FD, Pref, Mod, Acc) ->
    Lo = K,
    Hi = erlang:min(K + Step - 1, MaxV),
    PrefHi = array:get(Hi, Pref),
    PrefLoMinus1 =
        if
            Lo > 1 -> array:get(Lo - 1, Pref);
            true -> 0
        end,
    Cnt = PrefHi - PrefLoMinus1,
    Q = K div D,
    Contribution = ((Cnt rem Mod) * (FD rem Mod)) rem Mod,
    Contribution2 = (Contribution * (Q rem Mod)) rem Mod,
    NewAcc = (Acc + Contribution2) rem Mod,
    loop_k(Step, K + Step, MaxV, D, FD, Pref, Mod, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_floored_pairs(nums :: [integer]) :: integer
  def sum_of_floored_pairs(nums) do
    mod = 1_000_000_007
    max_v = Enum.max(nums)

    freq_map =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    freq_arr =
      0..max_v
      |> Enum.map(fn i -> Map.get(freq_map, i, 0) end)
      |> :array.from_list()

    pref_arr =
      Enum.reduce(0..max_v, {0, []}, fn i, {sum, acc} ->
        cnt = :array.get(i, freq_arr)
        new_sum = sum + cnt
        {new_sum, [new_sum | acc]}
      end)
      |> elem(1)
      |> Enum.reverse()
      |> :array.from_list()

    ans =
      Enum.reduce(1..max_v, 0, fn v, acc_outer ->
        cnt_v = :array.get(v, freq_arr)

        if cnt_v == 0 do
          acc_outer
        else
          max_k = div(max_v, v)

          Enum.reduce(1..max_k, acc_outer, fn k, acc_inner ->
            l = k * v
            r = min((k + 1) * v - 1, max_v)
            total =
              :array.get(r, pref_arr) -
                (if l > 0, do: :array.get(l - 1, pref_arr), else: 0)

            add = rem(cnt_v * total * k, mod)
            new_acc = acc_inner + add
            if new_acc >= mod, do: new_acc - mod, else: new_acc
          end)
        end
      end)

    ans
  end
end
```
