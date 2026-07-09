# 3495. Minimum Operations to Make Array Elements Zero

## Cpp

```cpp
class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        vector<long long> pow4;
        pow4.push_back(1LL); // 4^0
        while (pow4.back() <= 1000000000LL) {
            pow4.push_back(pow4.back() * 4LL);
        }
        // ensure one extra element for upper bound
        if (pow4.back() <= 1000000000LL) pow4.push_back(pow4.back()*4LL);
        
        long long total = 0;
        for (const auto& q : queries) {
            long long l = q[0];
            long long r = q[1];
            long long sumSteps = 0;
            // iterate over possible k values
            for (int k = 1; ; ++k) {
                if (k >= (int)pow4.size()) break;
                long long left = max(l, pow4[k-1]);
                if (left > r) break;
                long long right = min(r, pow4[k] - 1);
                if (right < left) continue;
                long long cnt = right - left + 1;
                sumSteps += cnt * k;
            }
            int maxStep = upper_bound(pow4.begin(), pow4.end(), r) - pow4.begin(); // steps for r
            long long ops = max<long long>(maxStep, (sumSteps + 1) / 2);
            total += ops;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public long minOperations(int[][] queries) {
        long total = 0L;
        for (int[] q : queries) {
            int l = q[0];
            int r = q[1];
            long sum = 0L;
            long curPow = 1L; // 4^k
            int k = 0;
            while (curPow <= r) {
                long nextPow = curPow * 4L;
                long start = Math.max((long) l, curPow);
                long end = Math.min((long) r, nextPow - 1);
                if (start <= end) {
                    sum += (end - start + 1) * (k + 1);
                }
                curPow = nextPow;
                k++;
            }
            // maximum operations needed for a single number in the range
            int maxF = 0;
            long temp = r;
            while (temp > 0) {
                temp /= 4;
                maxF++;
            }
            long ops = Math.max(maxF, (sum + 1) / 2);
            total += ops;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: int
        """
        # precompute powers of 4 up to >1e9
        pow4 = [1]
        while pow4[-1] <= 10**9:
            pow4.append(pow4[-1] * 4)
        # add a sentinel large value for easier interval handling
        pow4.append(10**18)

        total_sum = 0
        for l, r in queries:
            total_steps = 0
            # iterate over intervals defined by powers of 4
            for i in range(len(pow4) - 1):
                start = pow4[i]
                end = pow4[i + 1] - 1
                if start > r or end < l:
                    continue
                cnt = min(r, end) - max(l, start) + 1
                total_steps += (i + 1) * cnt
            ops = (total_steps + 1) // 2  # ceil division by 2
            total_sum += ops
        return total_sum
```

## Python3

```python
class Solution:
    def minOperations(self, queries):
        # precompute powers of 4 up to >1e9
        pows = [1]
        while pows[-1] <= 10**9:
            pows.append(pows[-1] * 4)

        def total_up_to(N: int) -> int:
            if N <= 0:
                return 0
            total = 0
            # iterate over intervals defined by powers of 4
            for k in range(len(pows) - 1):
                start = pows[k]
                if start > N:
                    break
                end = min(N, pows[k + 1] - 1)
                cnt_len = end - start + 1
                total += (k + 1) * cnt_len
            return total

        ans = 0
        for l, r in queries:
            total = total_up_to(r) - total_up_to(l - 1)
            max_cnt = 0
            # find floor(log4(r))
            # binary search over pows
            lo, hi = 0, len(pows) - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if pows[mid] <= r:
                    lo = mid
                else:
                    hi = mid - 1
            max_cnt = lo + 1  # because cnt = k+1 where k=log4 floor
            ops = (total + 1) // 2
            ans += max(max_cnt, ops)
        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

long long minOperations(int** queries, int queriesSize, int* queriesColSize) {
    // precompute powers of 4 up to >1e9
    vector<long long> pow4;
    long long p = 1;
    while (p <= 1000000000LL) {
        pow4.push_back(p);
        if (p > LLONG_MAX / 4) break;
        p *= 4;
    }
    // prefix sum function: Σ_{x=1}^{n} (floor(log4(x)) + 1)
    auto prefix = [&](long long n) -> long long {
        if (n <= 0) return 0LL;
        long long sum = 0;
        for (size_t k = 0; k < pow4.size(); ++k) {
            long long start = pow4[k];
            if (n < start) break;
            long long next = (k + 1 < pow4.size()) ? pow4[k + 1] : LLONG_MAX;
            long long end = min(n, next - 1);
            long long cnt = end - start + 1;
            sum += cnt * (static_cast<long long>(k) + 1);
        }
        return sum;
    };
    
    long long total = 0;
    for (int i = 0; i < queriesSize; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        long long steps = prefix(r) - prefix(static_cast<long long>(l) - 1);
        total += (steps + 1) / 2; // ceil(steps/2)
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long MinOperations(int[][] queries) {
        // Precompute powers of 4 up to exceed the maximum possible r (1e9)
        long[] pow = new long[20];
        pow[0] = 1;
        for (int i = 1; i < pow.Length; i++) {
            pow[i] = pow[i - 1] * 4;
        }

        long total = 0;
        foreach (var q in queries) {
            long l = q[0];
            long r = q[1];

            long sum = 0;
            int maxS = 0;

            for (int k = 0; ; k++) {
                if (k >= pow.Length) break;
                long blockStart = pow[k];
                if (blockStart > r) break;

                long blockEnd = (k + 1 < pow.Length) ? pow[k + 1] - 1 : long.MaxValue;
                long left = Math.Max(l, blockStart);
                long right = Math.Min(r, blockEnd);

                if (left <= right) {
                    long cnt = right - left + 1;
                    int s = k + 1; // floor(log4(x)) + 1 for this block
                    sum += cnt * s;
                    maxS = s; // blocks are processed in increasing order, so last valid s is the maximum
                }
            }

            long ops = Math.Max((long)maxS, (sum + 1) / 2);
            total += ops;
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} queries
 * @return {number}
 */
var minOperations = function(queries) {
    // precompute powers of 4 up to >1e9
    const pow4 = [1];
    while (pow4[pow4.length - 1] <= 1e9) {
        pow4.push(pow4[pow4.length - 1] * 4);
    }
    const m = pow4.length; // includes last power > limit

    // helper: sum of depths from 1 to n
    function sumDepthUpTo(n) {
        if (n <= 0) return 0;
        let total = 0;
        for (let k = 0; k < m - 1 && pow4[k] <= n; ++k) {
            const start = pow4[k];
            const end = Math.min(pow4[k + 1] - 1, n);
            const cnt = end - start + 1;
            total += cnt * (k + 1); // depth = k+1
        }
        return total;
    }

    // helper: depth of a single number x (floor(log4(x)) + 1)
    function depthOf(x) {
        // binary search in pow4 to find largest power <= x
        let lo = 0, hi = m - 1;
        while (lo < hi) {
            const mid = Math.floor((lo + hi + 1) / 2);
            if (pow4[mid] <= x) lo = mid;
            else hi = mid - 1;
        }
        return lo + 1; // because pow4[0]=1 corresponds to depth 1
    }

    let answerSum = 0;

    for (const [l, r] of queries) {
        const totalWork = sumDepthUpTo(r) - sumDepthUpTo(l - 1);
        const maxDepth = depthOf(r);
        const ops = Math.max(maxDepth, Math.floor((totalWork + 1) / 2));
        answerSum += ops;
    }

    return answerSum;
};
```

## Typescript

```typescript
function minOperations(queries: number[][]): number {
    // precompute powers of 4 up to exceed 1e9
    const pow4: number[] = [];
    let v = 1;
    while (v <= 1_000_000_000) {
        pow4.push(v);
        v *= 4;
    }
    // sentinel for easier handling of the last interval
    pow4.push(Number.MAX_SAFE_INTEGER);

    let total = 0;

    for (const [lOrig, rOrig] of queries) {
        const l = lOrig;
        const r = rOrig;
        let sumOps = 0;
        let maxK = 0; // floor(log4(r))

        // iterate over intervals where floor(log4(x)) is constant
        for (let k = 0; pow4[k] <= r; ++k) {
            const left = Math.max(l, pow4[k]);
            const right = Math.min(r, pow4[k + 1] - 1);
            if (left <= right) {
                const cnt = right - left + 1;
                sumOps += (k + 1) * cnt; // ops for this segment
            }
            if (pow4[k + 1] <= r) maxK = k + 1;
        }

        const maxOps = maxK + 1; // floor(log4(r)) + 1
        const needed = Math.max(Math.floor((sumOps + 1) / 2), maxOps);
        total += needed;
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $queries
     * @return Integer
     */
    function minOperations($queries) {
        // precompute powers of 4 up to a value larger than max possible r (1e9)
        $pow4 = [1];
        while (end($pow4) <= 2000000000) { // safe upper bound
            $pow4[] = end($pow4) * 4;
        }
        $nPow = count($pow4);
        $answer = 0;

        foreach ($queries as $qr) {
            $l = $qr[0];
            $r = $qr[1];

            // total steps needed for all numbers in [l, r]
            $total = 0;
            $cur = $l;
            while ($cur <= $r) {
                // find k such that pow4[k] <= cur < pow4[k+1]
                $k = 0;
                while ($k + 1 < $nPow && $pow4[$k + 1] <= $cur) {
                    $k++;
                }
                $segmentEnd = min($r, $pow4[$k + 1] - 1);
                $cnt = $segmentEnd - $cur + 1;
                $total += $cnt * ($k + 1); // each number in this segment needs (k+1) "/4" ops
                $cur = $segmentEnd + 1;
            }

            // steps needed for the maximum element r
            $kR = 0;
            while ($kR + 1 < $nPow && $pow4[$kR + 1] <= $r) {
                $kR++;
            }
            $maxHeight = $kR + 1;

            // minimal operations: max(maxHeight, ceil(total/2))
            $ops = max($maxHeight, intdiv($total + 1, 2));
            $answer += $ops;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ queries: [[Int]]) -> Int {
        var totalResult: Int64 = 0
        for q in queries {
            let l = Int64(q[0])
            let r = Int64(q[1])
            let count = r - l + 1
            let steps = count + (prefix(r) - prefix(l - 1))
            let ops = (steps + 1) / 2
            totalResult += ops
        }
        return Int(totalResult)
    }
    
    private func prefix(_ n: Int64) -> Int64 {
        if n <= 0 { return 0 }
        var sum: Int64 = 0
        var power: Int64 = 1          // 4^0
        var exp: Int64 = 0            // current exponent
        
        while power <= n {
            let nextPower = power * 4
            let end = min(n, nextPower - 1)
            let cnt = end - power + 1
            sum += exp * cnt
            exp += 1
            power = nextPower
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(queries: Array<IntArray>): Long {
        // Precompute powers of 4 up to > 1e9
        val powers = mutableListOf<Long>()
        var p = 1L
        while (p <= 1_000_000_000L) {
            powers.add(p)
            p *= 4L
        }

        fun prefix(n: Long): Long {
            if (n <= 0L) return 0L
            var sum = 0L
            var idx = 0
            while (idx < powers.size && powers[idx] <= n) {
                val start = powers[idx]
                val nextPower = if (idx + 1 < powers.size) powers[idx + 1] else Long.MAX_VALUE
                val end = minOf(n, nextPower - 1)
                val cnt = end - start + 1
                sum += cnt * (idx + 1).toLong()
                idx++
            }
            return sum
        }

        var answer = 0L
        for (q in queries) {
            val l = q[0].toLong()
            val r = q[1].toLong()

            // max depth needed for the largest number r
            var idx = 0
            while (idx + 1 < powers.size && powers[idx + 1] <= r) idx++
            val maxDepth = (idx + 1).toLong()

            val totalSteps = prefix(r) - prefix(l - 1)
            val opsNeeded = kotlin.math.max(maxDepth, (totalSteps + 1) / 2)
            answer += opsNeeded
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  static const List<int> _pow = [
    1,
    4,
    16,
    64,
    256,
    1024,
    4096,
    16384,
    65536,
    262144,
    1048576,
    4194304,
    16777216,
    67108864,
    268435456,
    1073741824,
    4294967296
  ];

  int _maxK(int x) {
    int k = 0;
    while (k + 1 < _pow.length && _pow[k + 1] <= x) {
      k++;
    }
    return k;
  }

  int minOperations(List<List<int>> queries) {
    int total = 0;
    for (var q in queries) {
      int l = q[0];
      int r = q[1];

      int maxK = _maxK(r);
      int maxOps = maxK + 1;

      int sumOps = 0;
      for (int k = 0; k <= maxK; k++) {
        int left = l > _pow[k] ? l : _pow[k];
        int rightBound = _pow[k + 1] - 1;
        int right = r < rightBound ? r : rightBound;
        if (left <= right) {
          int cnt = right - left + 1;
          sumOps += (k + 1) * cnt;
        }
      }

      int need = (sumOps + 1) >> 1; // ceil(sumOps / 2)
      total += need > maxOps ? need : maxOps;
    }
    return total;
  }
}
```

## Golang

```go
func minOperations(queries [][]int) int64 {
	type void struct{}
	// precompute powers of 4 up to exceed maximum possible r (1e9)
	var pow []int64
	pow = append(pow, 1)
	for {
		next := pow[len(pow)-1] * 4
		pow = append(pow, next)
		if next > 1_000_000_000 {
			break
		}
	}

	maxInt64 := func(a, b int64) int64 {
		if a > b {
			return a
		}
		return b
	}
	minInt64 := func(a, b int64) int64 {
		if a < b {
			return a
		}
		return b
	}

	var total int64
	for _, q := range queries {
		l := int64(q[0])
		r := int64(q[1])

		var sumK int64
		var maxK int64

		for t := 0; ; t++ {
			start := pow[t]
			if start > r {
				break
			}
			end := pow[t+1] - 1
			if end > r {
				end = r
			}
			lo := maxInt64(l, start)
			hi := minInt64(r, end)
			if lo <= hi {
				cnt := hi - lo + 1
				k := int64(t + 1) // k = floor(log4(x)) + 1
				sumK += cnt * k
				if k > maxK {
					maxK = k
				}
			}
		}

		ops := maxK
		half := (sumK + 1) / 2
		if half > ops {
			ops = half
		}
		total += ops
	}
	return total
}
```

## Ruby

```ruby
def min_operations(queries)
  max_r = 0
  queries.each { |l, r| max_r = r if r > max_r }

  powers = [1]
  while powers[-1] <= max_r
    powers << powers[-1] * 4
  end

  total = 0
  queries.each do |l, r|
    sum = 0
    (0...powers.length - 1).each do |i|
      left = [l, powers[i]].max
      right = [r, powers[i + 1] - 1].min
      next if left > right

      len = right - left + 1
      sum += len * (i + 1)
    end
    ops = (sum + 1) / 2
    total += ops
  end

  total
end
```

## Scala

```scala
object Solution {
    def minOperations(queries: Array[Array[Int]]): Long = {
        val maxVal = 1000000000L
        val powers = scala.collection.mutable.ArrayBuffer.empty[Long]
        var p = 1L
        while (p <= maxVal) {
            powers += p
            if (p > Long.MaxValue / 4) {
                // avoid overflow, break after adding current power
                p = Long.MaxValue
            } else {
                p *= 4
            }
        }
        powers += Long.MaxValue // sentinel for the last interval

        var result: Long = 0L
        for (qr <- queries) {
            val l = qr(0).toLong
            val r = qr(1).toLong
            var total: Long = 0L
            var maxK = 0
            var idx = 0
            while (idx < powers.length - 1 && powers(idx) <= r) {
                val segStart = math.max(l, powers(idx))
                val segEnd = math.min(r, powers(idx + 1) - 1)
                if (segStart <= segEnd) {
                    val cnt = segEnd - segStart + 1L
                    val k = idx + 1 // floor(log4(x)) = idx, so operations needed = idx+1
                    total += cnt * k
                    if (k > maxK) maxK = k
                }
                idx += 1
            }
            val ops = math.max(maxK, (total + 1) / 2)
            result += ops
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(queries: Vec<Vec<i32>>) -> i64 {
        fn prefix_sum(n: i64) -> i64 {
            if n <= 0 {
                return 0;
            }
            let mut sum = 0i64;
            let mut pow = 1i64; // 4^0
            let mut k = 0i64;   // current exponent
            while pow <= n {
                let next_pow = pow * 4;
                let end = if n < next_pow - 1 { n } else { next_pow - 1 };
                let cnt = end - pow + 1;
                sum += cnt * (k + 1);
                pow = next_pow;
                k += 1;
            }
            sum
        }

        let mut total: i64 = 0;
        for q in queries {
            let l = q[0] as i64;
            let r = q[1] as i64;
            let s = prefix_sum(r) - if l > 1 { prefix_sum(l - 1) } else { 0 };
            total += (s + 1) / 2;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (min-operations queries)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((max-r 1000000000)                         ; upper bound from constraints
         ;; generate powers of 4 up to > max-r, keep the extra one for interval ends
         (pow-list (let loop ([p 0] [val 1] [acc '()])
                     (if (> val (* 4 max-r))
                         (reverse acc)
                         (loop (+ p 1) (* val 4) (cons val acc)))))
         (pow-vec (list->vector pow-list))
         (limit (- (vector-length pow-vec) 1)))    ; last index that has a following power
    (let ((total 0))
      (for ([q queries])
        (define l (first q))
        (define r (second q))
        (define S 0)
        (define M 0)
        (for ([i (in-range limit)])
          (define low-bound (vector-ref pow-vec i))
          (define high-bound (sub1 (vector-ref pow-vec (+ i 1))))
          (when (and (<= low-bound r) (>= high-bound l))
            (define lo (max l low-bound))
            (define hi (min r high-bound))
            (when (<= lo hi)
              (define cnt (+ 1 (- hi lo)))      ; number of integers with this k
              (define k (+ i 1))                ; operations needed for each such integer
              (set! S (+ S (* cnt k)))
              (when (> k M) (set! M k)))))
        (define ans (max (quotient (+ S 1) 2) M))
        (set! total (+ total ans)))
      total)))
```

## Erlang

```erlang
-spec min_operations(Queries :: [[integer()]]) -> integer().
min_operations(Queries) ->
    Intervals = build_intervals(),
    lists:foldl(fun([L,R], Acc) ->
        Total = sum_f(L, R, Intervals),
        MaxNeed = needed(R, Intervals),
        Ops = max(MaxNeed, (Total + 1) div 2),
        Acc + Ops
    end, 0, Queries).

build_intervals() ->
    build_intervals(0, 1, []).

build_intervals(_K, Start, Acc) when Start > 1000000000 ->
    lists:reverse(Acc);
build_intervals(K, Start, Acc) ->
    End = erlang:min(Start * 4 - 1, 1000000000),
    Val = K + 1,
    build_intervals(K + 1, Start * 4, [{Start, End, Val} | Acc]).

sum_f(_L, _R, []) -> 0;
sum_f(L, R, [{S, E, V} | Rest]) ->
    if
        R < S -> 0;
        L > E -> sum_f(L, R, Rest);
        true ->
            OverlapStart = erlang:max(L, S),
            OverlapEnd   = erlang:min(R, E),
            Count = OverlapEnd - OverlapStart + 1,
            Count * V + sum_f(L, R, Rest)
    end.

needed(_R, []) -> 0;
needed(R, [{S, E, V} | Rest]) ->
    if
        R >= S, R =< E -> V;
        true -> needed(R, Rest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(queries :: [[integer]]) :: integer
  def min_operations(queries) do
    Enum.reduce(queries, 0, fn [l, r], acc ->
      diff = prefix(r) - prefix(l - 1)
      ops = div(diff + 1, 2)
      acc + ops
    end)
  end

  defp prefix(n) when n <= 0, do: 0
  defp prefix(n), do: sum_prefix(n, 0, 1, 0)

  defp sum_prefix(limit, k, pow, acc) do
    if pow > limit do
      acc
    else
      next_pow = pow * 4
      cnt = min(limit, next_pow - 1) - pow + 1
      new_acc = acc + cnt * (k + 1)
      sum_prefix(limit, k + 1, next_pow, new_acc)
    end
  end
end
```
