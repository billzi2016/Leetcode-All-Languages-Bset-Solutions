# 3164. Find the Number of Good Pairs II

## Cpp

```cpp
class Solution {
public:
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        const int MAXV = 1000000;
        vector<int> freq(MAXV + 1, 0);
        for (int v : nums2) {
            ++freq[v];
        }
        long long ans = 0;
        for (int a : nums1) {
            if (a % k != 0) continue;
            int x = a / k;
            for (int d = 1; (long long)d * d <= x; ++d) {
                if (x % d == 0) {
                    ans += freq[d];
                    int other = x / d;
                    if (other != d) ans += freq[other];
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        int max = 0;
        for (int v : nums1) {
            if (v > max) max = v;
        }
        int[] cnt1 = new int[max + 1];
        for (int v : nums1) {
            cnt1[v]++;
        }

        int[] freqT = new int[max + 1];
        for (int v2 : nums2) {
            long t = (long) v2 * k;
            if (t <= max) {
                freqT[(int) t]++;
            }
        }

        long ans = 0L;
        for (int d = 1; d <= max; d++) {
            int f = freqT[d];
            if (f == 0) continue;
            for (int m = d; m <= max; m += d) {
                int c = cnt1[m];
                if (c != 0) {
                    ans += (long) c * f;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        if not nums1 or not nums2:
            return 0

        max_val = max(nums1)
        cnt1 = [0] * (max_val + 1)
        for v in nums1:
            cnt1[v] += 1

        from collections import Counter
        cnt2 = Counter(nums2)

        ans = 0
        for d, cd in cnt2.items():
            step = d * k
            if step > max_val:
                continue
            total = 0
            # sum frequencies of nums1 that are multiples of step
            for m in range(step, max_val + 1, step):
                total += cnt1[m]
            ans += cd * total

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if not nums1 or not nums2:
            return 0

        max_num2 = max(nums2)
        max_y = 0
        for x in nums1:
            if x % k == 0:
                y = x // k
                if y > max_y:
                    max_y = y

        limit = max(max_num2, max_y)

        freq = [0] * (limit + 1)
        for v in nums2:
            if v <= limit:
                freq[v] += 1

        div_cnt = [0] * (limit + 1)
        for d in range(1, limit + 1):
            cnt_d = freq[d]
            if cnt_d:
                for m in range(d, limit + 1, d):
                    div_cnt[m] += cnt_d

        ans = 0
        for x in nums1:
            if x % k == 0:
                y = x // k
                if y <= limit:
                    ans += div_cnt[y]

        return ans
```

## C

```c
#include <stdlib.h>
#include <math.h>

long long numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    if (nums1Size == 0 || nums2Size == 0) return 0;
    
    int maxV = 0;
    for (int i = 0; i < nums1Size; ++i) {
        if (nums1[i] > maxV) maxV = nums1[i];
    }
    
    int *freq = (int *)calloc((size_t)maxV + 1, sizeof(int));
    if (!freq) return 0; // allocation failure guard
    
    for (int i = 0; i < nums2Size; ++i) {
        long long prod = (long long)nums2[i] * k;
        if (prod <= maxV) {
            freq[(int)prod] += 1;
        }
    }
    
    long long ans = 0;
    for (int i = 0; i < nums1Size; ++i) {
        int v = nums1[i];
        int limit = (int)sqrt((double)v);
        for (int d = 1; d <= limit; ++d) {
            if (v % d == 0) {
                int d1 = d;
                int d2 = v / d;
                ans += freq[d1];
                if (d2 != d1) ans += freq[d2];
            }
        }
    }
    
    free(freq);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long NumberOfPairs(int[] nums1, int[] nums2, int k) {
        var freq = new Dictionary<int, int>();
        foreach (var x in nums2) {
            if (freq.ContainsKey(x)) freq[x]++; else freq[x] = 1;
        }

        long ans = 0;
        foreach (var v in nums1) {
            int limit = (int)Math.Sqrt(v);
            for (int d = 1; d <= limit; ++d) {
                if (v % d != 0) continue;

                // divisor d
                if (d % k == 0) {
                    int t = d / k;
                    if (freq.TryGetValue(t, out int cnt)) ans += cnt;
                }

                int other = v / d;
                if (other != d) {
                    if (other % k == 0) {
                        int t = other / k;
                        if (freq.TryGetValue(t, out int cnt2)) ans += cnt2;
                    }
                }
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, k) {
    const MAX_VAL = 1000000; // based on constraints
    
    // frequency of each value in nums2
    const freq = new Uint32Array(MAX_VAL + 1);
    for (let v of nums2) {
        if (v <= MAX_VAL) freq[v]++; // all values satisfy this bound
    }
    
    // divisorSum[t] = total count of numbers in nums2 that divide t
    const divisorSum = new Uint32Array(MAX_VAL + 1);
    for (let d = 1; d <= MAX_VAL; ++d) {
        const cnt = freq[d];
        if (cnt === 0) continue;
        for (let m = d; m <= MAX_VAL; m += d) {
            divisorSum[m] += cnt;
        }
    }
    
    let ans = 0;
    for (let x of nums1) {
        if (x % k !== 0) continue;
        const t = x / k; // guaranteed integer
        if (t <= MAX_VAL) ans += divisorSum[t];
    }
    
    return ans;
};
```

## Typescript

```typescript
function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    const maxV = Math.max(...nums1);
    const freqProd = new Uint32Array(maxV + 1);
    for (const x of nums2) {
        const p = x * k;
        if (p <= maxV) freqProd[p]++;
    }
    const memo = new Map<number, number>();
    let ans = 0;
    for (const v of nums1) {
        let sum = memo.get(v);
        if (sum === undefined) {
            let total = 0;
            const limit = Math.floor(Math.sqrt(v));
            for (let d = 1; d <= limit; ++d) {
                if (v % d === 0) {
                    const d2 = v / d;
                    if (freqProd[d] !== 0) total += freqProd[d];
                    if (d2 !== d && freqProd[d2] !== 0) total += freqProd[d2];
                }
            }
            memo.set(v, total);
            sum = total;
        }
        ans += sum;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function numberOfPairs($nums1, $nums2, $k) {
        // Find maximum value in nums1 to limit the multiple enumeration
        $maxV = 0;
        foreach ($nums1 as $v) {
            if ($v > $maxV) {
                $maxV = $v;
            }
        }

        // Frequency of each value in nums1
        $cnt1 = [];
        foreach ($nums1 as $v) {
            if (!isset($cnt1[$v])) {
                $cnt1[$v] = 0;
            }
            $cnt1[$v]++;
        }

        // Frequency of each value in nums2
        $freq2 = [];
        foreach ($nums2 as $d) {
            if (!isset($freq2[$d])) {
                $freq2[$d] = 0;
            }
            $freq2[$d]++;
        }

        $ans = 0;

        // For each distinct divisor from nums2, add contributions of its multiples in nums1
        foreach ($freq2 as $d => $f) {
            $step = $d * $k;               // required divisor for nums1 elements
            if ($step > $maxV) {
                continue;
            }
            for ($multiple = $step; $multiple <= $maxV; $multiple += $step) {
                if (isset($cnt1[$multiple])) {
                    $ans += $f * $cnt1[$multiple];
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var freq = [Int:Int]()
        for val in nums2 {
            let prod = val * k
            freq[prod, default: 0] += 1
        }
        var ans = 0
        for v in nums1 {
            var d = 1
            while d * d <= v {
                if v % d == 0 {
                    if let cnt = freq[d] {
                        ans += cnt
                    }
                    let other = v / d
                    if other != d, let cnt2 = freq[other] {
                        ans += cnt2
                    }
                }
                d += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Long {
        var maxA = 0
        for (v in nums1) if (v > maxA) maxA = v
        val limit = maxA / k
        if (limit == 0) return 0L

        val cntB = IntArray(limit + 1)
        for (b in nums2) {
            if (b <= limit) cntB[b]++
        }

        val divCount = IntArray(limit + 1)
        for (b in 1..limit) {
            val f = cntB[b]
            if (f == 0) continue
            var multiple = b
            while (multiple <= limit) {
                divCount[multiple] += f
                multiple += b
            }
        }

        var ans = 0L
        for (a in nums1) {
            if (a % k != 0) continue
            val x = a / k
            if (x <= limit) ans += divCount[x].toLong()
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPairs(List<int> nums1, List<int> nums2, int k) {
    // Find maximum value in nums2 for frequency array size
    int maxNum2 = 0;
    for (int v in nums2) {
      if (v > maxNum2) maxNum2 = v;
    }

    // Determine the largest x = nums1[i] / k where division is exact
    int maxX = 0;
    for (int v in nums1) {
      if (v % k == 0) {
        int x = v ~/ k;
        if (x > maxX) maxX = x;
      }
    }

    // If no element of nums1 is divisible by k, answer is zero
    if (maxX == 0) return 0;

    // Frequency of each value in nums2
    List<int> freq = List.filled(maxNum2 + 1, 0);
    for (int v in nums2) {
      freq[v]++;
    }

    // cntDivisible[x] = total count of nums2 values that divide x
    List<int> cntDivisible = List.filled(maxX + 1, 0);

    int limit = maxNum2 < maxX ? maxNum2 : maxX;
    for (int t = 1; t <= limit; ++t) {
      int f = freq[t];
      if (f == 0) continue;
      for (int m = t; m <= maxX; m += t) {
        cntDivisible[m] += f;
      }
    }

    // Accumulate answer using precomputed divisor counts
    int ans = 0;
    for (int v in nums1) {
      if (v % k == 0) {
        int x = v ~/ k;
        ans += cntDivisible[x];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfPairs(nums1 []int, nums2 []int, k int) int64 {
    maxV := 0
    for _, v := range nums1 {
        if v > maxV {
            maxV = v
        }
    }
    for _, v := range nums2 {
        if v > maxV {
            maxV = v
        }
    }

    cnt := make([]int, maxV+1)
    for _, v := range nums2 {
        cnt[v]++
    }

    maxX := maxV / k
    if maxX == 0 {
        maxX = 1
    }
    divisorSum := make([]int64, maxX+1)

    for t := 1; t <= maxV; t++ {
        c := cnt[t]
        if c == 0 {
            continue
        }
        for m := t; m <= maxX; m += t {
            divisorSum[m] += int64(c)
        }
    }

    var ans int64
    for _, v := range nums1 {
        if v%k != 0 {
            continue
        }
        x := v / k
        if x <= maxX {
            ans += divisorSum[x]
        }
    }
    return ans
}
```

## Ruby

```ruby
def number_of_pairs(nums1, nums2, k)
  max_t = 0
  nums1.each do |v|
    if v % k == 0
      t = v / k
      max_t = t if t > max_t
    end
  end
  return 0 if max_t == 0

  freq = Array.new(max_t + 1, 0)
  nums2.each do |v|
    next if v > max_t
    freq[v] += 1
  end

  cnt = Array.new(max_t + 1, 0)
  d = 1
  while d <= max_t
    f = freq[d]
    if f > 0
      m = d
      while m <= max_t
        cnt[m] += f
        m += d
      end
    end
    d += 1
  end

  ans = 0
  nums1.each do |v|
    next unless v % k == 0
    t = v / k
    ans += cnt[t]
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
        val MAX_VAL = 1000000
        val cnt = new Array[Int](MAX_VAL + 1)
        for (v <- nums2) {
            cnt(v) += 1
        }
        var ans: Long = 0L
        for (v <- nums1) {
            var d = 1
            val limit = math.sqrt(v).toInt
            while (d <= limit) {
                if (v % d == 0) {
                    // divisor d
                    var t = d
                    if (t % k == 0) {
                        val x = t / k
                        ans += cnt(x)
                    }
                    val other = v / d
                    if (other != d) {
                        t = other
                        if (t % k == 0) {
                            val x = t / k
                            ans += cnt(x)
                        }
                    }
                }
                d += 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        if nums1.is_empty() || nums2.is_empty() {
            return 0;
        }
        let max_num1 = *nums1.iter().max().unwrap() as usize;
        let max_num2 = *nums2.iter().max().unwrap() as usize;
        let k_usize = k as usize;
        if k_usize == 0 {
            return 0;
        }
        let max_x = max_num1 / k_usize;
        if max_x == 0 {
            return 0;
        }

        // frequency of each value in nums2
        let mut freq = vec![0i64; max_num2 + 1];
        for &v in nums2.iter() {
            freq[v as usize] += 1;
        }

        // sum_div[x] = total count of divisors of x that appear in nums2
        let mut sum_div = vec![0i64; max_x + 1];
        for d in 1..=max_num2 {
            let cnt = freq[d];
            if cnt == 0 {
                continue;
            }
            let mut m = d;
            while m <= max_x {
                sum_div[m] += cnt;
                m += d;
            }
        }

        // accumulate answer
        let mut ans: i64 = 0;
        for &t in nums1.iter() {
            if t % k == 0 {
                let x = (t / k) as usize;
                ans += sum_div[x];
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/math)

(define/contract (number-of-pairs nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([freq (make-hash)])
    ;; frequency of each value in nums2
    (for ([b nums2])
      (hash-set! freq b (+ 1 (hash-ref freq b 0))))
    (define total 0)
    (for ([a nums1])
      (when (= (remainder a k) 0)
        (let* ([c (quotient a k)]
               [limit (exact-floor (sqrt c))])
          (for ([i (in-range 1 (add1 limit))])
            (when (= (remainder c i) 0)
              (define d i)
              (define e (/ c i))
              (set! total (+ total (hash-ref freq d 0)))
              (unless (= d e)
                (set! total (+ total (hash-ref freq e 0)))))))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([number_of_pairs/3]).

-spec number_of_pairs(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
number_of_pairs(Nums1, Nums2, K) ->
    TMap = build_tmap(Nums2, K, #{}),
    total_pairs(Nums1, TMap, 0).

build_tmap([], _K, Map) -> Map;
build_tmap([B|Rest], K, Map) ->
    T = B * K,
    Count = maps:get(T, Map, 0),
    NewMap = maps:put(T, Count + 1, Map),
    build_tmap(Rest, K, NewMap).

total_pairs([], _Map, Acc) -> Acc;
total_pairs([A|Rest], Map, Acc) ->
    SumA = count_divisors(A, Map, 0),
    total_pairs(Rest, Map, Acc + SumA).

count_divisors(A, Map, Acc) ->
    Max = trunc(math:sqrt(A)),
    count_divisors_loop(1, Max, A, Map, Acc).

count_divisors_loop(I, Max, _A, _Map, Acc) when I > Max -> Acc;
count_divisors_loop(I, Max, A, Map, Acc) ->
    case A rem I of
        0 ->
            D1 = I,
            D2 = A div I,
            C1 = maps:get(D1, Map, 0),
            NewAcc = Acc + C1,
            FinalAcc = if D2 =/= D1 -> NewAcc + maps:get(D2, Map, 0);
                         true       -> NewAcc
                      end,
            count_divisors_loop(I + 1, Max, A, Map, FinalAcc);
        _ ->
            count_divisors_loop(I + 1, Max, A, Map, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def number_of_pairs(nums1, nums2, k) do
    max_val = Enum.max(nums1)

    freq_t =
      Enum.reduce(nums2, %{}, fn x, acc ->
        t = x * k

        if t <= max_val do
          Map.update(acc, t, 1, &(&1 + 1))
        else
          acc
        end
      end)

    Enum.reduce(nums1, 0, fn v, total ->
      limit = :math.sqrt(v) |> trunc()
      total + count_divisors(v, limit, freq_t)
    end)
  end

  defp count_divisors(v, limit, freq_t) do
    1..limit
    |> Enum.reduce(0, fn i, acc ->
      if rem(v, i) == 0 do
        d1 = i
        d2 = div(v, i)

        add1 = Map.get(freq_t, d1, 0)
        add2 = if d2 != d1, do: Map.get(freq_t, d2, 0), else: 0

        acc + add1 + add2
      else
        acc
      end
    end)
  end
end
```
