# 2809. Minimum Time to Make Array Sum At Most x

## Cpp

```cpp
class Solution {
public:
    int minimumTime(vector<int>& nums1, vector<int>& nums2, int x) {
        int n = nums1.size();
        vector<pair<int,int>> a(n);
        for (int i = 0; i < n; ++i) a[i] = {nums2[i], nums1[i]};
        sort(a.begin(), a.end()); // sort by nums2 ascending
        
        long long sum1 = 0, sum2 = 0;
        for (int v : nums1) sum1 += v;
        for (int v : nums2) sum2 += v;
        
        const long long NEG = -(1LL<<60);
        vector<vector<long long>> dp(n+1, vector<long long>(n+1, NEG));
        dp[0][0] = 0;
        for (int i = 1; i <= n; ++i) {
            int b = a[i-1].first; // nums2
            int a1 = a[i-1].second; // nums1
            dp[i][0] = 0;
            for (int j = 1; j <= i; ++j) {
                long long notTake = dp[i-1][j];
                long long take = dp[i-1][j-1];
                if (take != NEG) {
                    take += (long long)b * j + a1;
                }
                dp[i][j] = max(notTake, take);
            }
        }
        
        for (int t = 0; t <= n; ++t) {
            long long reduction = dp[n][t];
            if (reduction == NEG) continue;
            long long cur = sum1 + sum2 * t - reduction;
            if (cur <= x) return t;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumTime(java.util.List<Integer> nums1, java.util.List<Integer> nums2, int x) {
        int n = nums1.size();
        long[] a = new long[n];
        long[] b = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = nums1.get(i);
            b[i] = nums2.get(i);
        }
        // sort by b ascending
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        java.util.Arrays.sort(idx, (i, j) -> Long.compare(b[i], b[j]));
        long[] aSorted = new long[n];
        long[] bSorted = new long[n];
        for (int i = 0; i < n; i++) {
            aSorted[i] = a[idx[i]];
            bSorted[i] = b[idx[i]];
        }
        long sumA = 0, sumB = 0;
        for (int i = 0; i < n; i++) {
            sumA += a[i];
            sumB += b[i];
        }
        long NEG = Long.MIN_VALUE / 4;
        long[][] dp = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) java.util.Arrays.fill(dp[i], NEG);
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i][0] = 0;
            for (int j = 1; j <= i; j++) {
                long skip = dp[i - 1][j];
                long takePrev = dp[i - 1][j - 1];
                long take = NEG;
                if (takePrev != NEG) {
                    take = takePrev + aSorted[i - 1] + (long) j * bSorted[i - 1];
                }
                dp[i][j] = Math.max(skip, take);
            }
        }
        for (int t = 0; t <= n; t++) {
            long reduction = dp[n][t];
            if (reduction == NEG) continue;
            long total = sumA + (long) t * sumB - reduction;
            if (total <= x) return t;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTime(self, nums1, nums2, x):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums1)
        # Pair and sort by nums2 ascending
        paired = sorted(zip(nums2, nums1))
        sorted_nums2 = [p[0] for p in paired]
        sorted_nums1 = [p[1] for p in paired]

        # dp[i][j]: max reduction using j operations among first i elements
        INF_NEG = -10**18
        dp = [[INF_NEG] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            a2 = sorted_nums2[i - 1]
            a1 = sorted_nums1[i - 1]
            dp[i][0] = 0
            for j in range(1, i + 1):
                # not take this element
                best = dp[i - 1][j]
                # take it as the j-th operation (time=j)
                cand = dp[i - 1][j - 1] + a2 * j + a1
                if cand > best:
                    best = cand
                dp[i][j] = best

        total_nums1 = sum(nums1)
        total_nums2 = sum(nums2)

        for t in range(0, n + 1):
            reduction = dp[n][t]
            if total_nums1 + t * total_nums2 - reduction <= x:
                return t
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        pairs = sorted(zip(nums1, nums2), key=lambda p: p[1])
        total_nums1 = sum(nums1)
        total_nums2 = sum(nums2)

        NEG_INF = -10**18
        dp = [NEG_INF] * (n + 1)
        dp[0] = 0

        for a, b in pairs:
            for j in range(n, 0, -1):
                if dp[j - 1] != NEG_INF:
                    val = dp[j - 1] + b * j + a
                    if val > dp[j]:
                        dp[j] = val

        for t in range(n + 1):
            if dp[t] == NEG_INF:
                continue
            current_sum = total_nums1 + t * total_nums2 - dp[t]
            if current_sum <= x:
                return t
        return -1
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int b; // nums1
    int a; // nums2
} Pair;

static int cmpPair(const void *p1, const void *p2) {
    const Pair *x = (const Pair *)p1;
    const Pair *y = (const Pair *)p2;
    return x->a - y->a;
}

int minimumTime(int* nums1, int nums1Size, int* nums2, int nums2Size, int x) {
    int n = nums1Size;
    Pair *arr = (Pair *)malloc(n * sizeof(Pair));
    long long sum1 = 0, sum2 = 0;
    for (int i = 0; i < n; ++i) {
        arr[i].a = nums2[i];
        arr[i].b = nums1[i];
        sum1 += nums1[i];
        sum2 += nums2[i];
    }
    qsort(arr, n, sizeof(Pair), cmpPair);

    int dim = n + 1;
    long long NEG = -(1LL << 60);
    long long *dp = (long long *)malloc(dim * dim * sizeof(long long));
    for (int i = 0; i < dim * dim; ++i) dp[i] = NEG;
    dp[0] = 0; // dp[0][0]

    for (int i = 1; i <= n; ++i) {
        int idx = i - 1;
        for (int j = 0; j <= i; ++j) {
            long long notTake = dp[(i - 1) * dim + j];
            long long take = NEG;
            if (j > 0) {
                long long prev = dp[(i - 1) * dim + (j - 1)];
                if (prev != NEG) {
                    take = prev + (long long)arr[idx].b + (long long)arr[idx].a * j;
                }
            }
            dp[i * dim + j] = notTake > take ? notTake : take;
        }
    }

    int answer = -1;
    for (int t = 0; t <= n; ++t) {
        long long reduction = dp[n * dim + t];
        if (reduction == NEG) continue;
        long long curSum = sum1 + sum2 * t - reduction;
        if (curSum <= x) {
            answer = t;
            break;
        }
    }

    free(arr);
    free(dp);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumTime(IList<int> nums1, IList<int> nums2, int x) {
        int n = nums1.Count;
        var pairs = new List<(int a, int b)>(n);
        long sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += nums1[i];
            sum2 += nums2[i];
            pairs.Add((nums1[i], nums2[i]));
        }
        pairs.Sort((p1, p2) => p1.b.CompareTo(p2.b));

        long[,] dp = new long[n + 1, n + 1];
        const long NEG_INF = long.MinValue / 4;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) dp[i, j] = NEG_INF;
            dp[i, 0] = 0;
        }

        for (int i = 1; i <= n; i++) {
            int a = pairs[i - 1].a;
            int b = pairs[i - 1].b;
            for (int j = 1; j <= i; j++) {
                long notTake = dp[i - 1, j];
                long take = dp[i - 1, j - 1] + (long)b * j + a;
                dp[i, j] = Math.Max(notTake, take);
            }
        }

        for (int t = 0; t <= n; t++) {
            long reduction = dp[n, t];
            if (reduction == NEG_INF) continue;
            long total = sum1 + sum2 * t - reduction;
            if (total <= x) return t;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} x
 * @return {number}
 */
var minimumTime = function(nums1, nums2, x) {
    const n = nums1.length;
    // Pair and sort by nums2 ascending
    const pairs = [];
    for (let i = 0; i < n; ++i) {
        pairs.push([nums1[i], nums2[i]]);
    }
    pairs.sort((a, b) => a[1] - b[1]); // compare nums2

    const sumNums1 = nums1.reduce((s, v) => s + v, 0);
    const sumNums2 = nums2.reduce((s, v) => s + v, 0);

    // dp[j] = max reduction using j operations processed so far
    const dp = new Array(n + 1).fill(-Infinity);
    dp[0] = 0;

    for (let idx = 0; idx < n; ++idx) {
        const a = pairs[idx][0];
        const b = pairs[idx][1];
        // update in descending order to avoid reuse within same iteration
        for (let j = idx + 1; j >= 1; --j) {
            if (dp[j - 1] !== -Infinity) {
                const candidate = dp[j - 1] + b * j + a;
                if (candidate > dp[j]) dp[j] = candidate;
            }
        }
    }

    for (let t = 0; t <= n; ++t) {
        const reduction = dp[t];
        // reduction is always defined (dp[0]=0, others computed)
        const curSum = sumNums1 + sumNums2 * t - reduction;
        if (curSum <= x) return t;
    }
    return -1;
};
```

## Typescript

```typescript
function minimumTime(nums1: number[], nums2: number[], x: number): number {
    const n = nums1.length;
    let sumNums1 = 0, sumNums2 = 0;
    const pairs: { a: number; b: number }[] = [];
    for (let i = 0; i < n; i++) {
        sumNums1 += nums1[i];
        sumNums2 += nums2[i];
        pairs.push({ a: nums1[i], b: nums2[i] });
    }
    pairs.sort((p, q) => p.b - q.b);
    const dp = new Array(n + 1).fill(-Infinity);
    dp[0] = 0;
    for (let i = 0; i < n; i++) {
        const { a, b } = pairs[i];
        for (let j = i + 1; j >= 1; j--) {
            const cand = dp[j - 1] + a + b * j;
            if (cand > dp[j]) dp[j] = cand;
        }
    }
    for (let t = 0; t <= n; t++) {
        const cur = sumNums1 + sumNums2 * t - dp[t];
        if (cur <= x) return t;
    }
    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $x
     * @return Integer
     */
    function minimumTime($nums1, $nums2, $x) {
        $n = count($nums1);
        // Pair and sort by nums2 ascending
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = [$nums1[$i], $nums2[$i]];
        }
        usort($pairs, function($a, $b) {
            if ($a[1] == $b[1]) return 0;
            return ($a[1] < $b[1]) ? -1 : 1;
        });
        $sortedNums1 = [];
        $sortedNums2 = [];
        foreach ($pairs as $p) {
            $sortedNums1[] = $p[0];
            $sortedNums2[] = $p[1];
        }
        $sum1 = array_sum($nums1);
        $sum2 = array_sum($nums2);
        // DP: dp[j] = max reduction using j operations
        $negInf = -PHP_INT_MAX;
        $dp = array_fill(0, $n + 1, $negInf);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            // iterate j descending
            for ($j = $i + 1; $j >= 1; $j--) {
                if ($dp[$j - 1] != $negInf) {
                    $candidate = $dp[$j - 1] + $sortedNums2[$i] * $j + $sortedNums1[$i];
                    if ($candidate > $dp[$j]) {
                        $dp[$j] = $candidate;
                    }
                }
            }
        }
        for ($t = 0; $t <= $n; $t++) {
            $total = $sum1 + $t * $sum2 - $dp[$t];
            if ($total <= $x) {
                return $t;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTime(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Int {
        let n = nums1.count
        var pairs = [(Int, Int)]()
        for i in 0..<n {
            pairs.append((nums1[i], nums2[i]))
        }
        // Sort by nums2 ascending
        pairs.sort { $0.1 < $1.1 }
        
        let sumNums1 = nums1.reduce(0, +)
        let sumNums2 = nums2.reduce(0, +)
        
        // dp[j] = max reduction using j operations after processing some elements
        var dp = Array(repeating: Int.min / 4, count: n + 1)
        dp[0] = 0
        
        for (a, b) in pairs {
            var j = n
            while j >= 1 {
                let prev = dp[j - 1]
                if prev > Int.min / 4 {
                    let candidate = prev + a + b * j
                    if candidate > dp[j] {
                        dp[j] = candidate
                    }
                }
                j -= 1
            }
        }
        
        for t in 0...n {
            let reduction = dp[t]
            if reduction <= Int.min / 4 { continue }
            let finalSum = sumNums1 + t * sumNums2 - reduction
            if finalSum <= x {
                return t
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTime(nums1: List<Int>, nums2: List<Int>, x: Int): Int {
        val n = nums1.size
        // Pair (nums2, nums1) and sort by nums2 ascending
        val pairs = (0 until n).map { i -> Pair(nums2[i], nums1[i]) }.sortedBy { it.first }
        var sum1 = 0L
        var sum2 = 0L
        for (v in nums1) sum1 += v.toLong()
        for (v in nums2) sum2 += v.toLong()

        val INF_NEG = Long.MIN_VALUE / 4
        val dp = LongArray(n + 1) { INF_NEG }
        dp[0] = 0L

        for ((idx, p) in pairs.withIndex()) {
            val b = p.first.toLong()
            val a = p.second.toLong()
            var j = idx + 1
            while (j >= 1) {
                if (dp[j - 1] != INF_NEG) {
                    val cand = dp[j - 1] + b * j + a
                    if (cand > dp[j]) dp[j] = cand
                }
                j--
            }
        }

        for (t in 0..n) {
            val reduced = dp[t]
            if (reduced == INF_NEG) continue
            val total = sum1 + sum2 * t - reduced
            if (total <= x.toLong()) return t
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minimumTime(List<int> nums1, List<int> nums2, int x) {
    int n = nums1.length;
    // Pair and sort by nums2 ascending
    List<List<int>> pairs = List.generate(n, (i) => [nums2[i], nums1[i]]);
    pairs.sort((a, b) => a[0].compareTo(b[0]));
    List<int> sortedNums2 = List.filled(n, 0);
    List<int> sortedNums1 = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      sortedNums2[i] = pairs[i][0];
      sortedNums1[i] = pairs[i][1];
    }

    int totalSum1 = nums1.reduce((a, b) => a + b);
    int totalSum2 = nums2.reduce((a, b) => a + b);

    // dp[i][j]: max reduction using j operations among first i elements
    List<List<int>> dp = List.generate(n + 1,
        (_) => List.filled(n + 1, -1));
    dp[0][0] = 0;

    for (int i = 1; i <= n; ++i) {
      int curNum2 = sortedNums2[i - 1];
      int curNum1 = sortedNums1[i - 1];
      for (int j = 0; j <= i; ++j) {
        int best = dp[i - 1][j]; // not take this element
        if (j > 0 && dp[i - 1][j - 1] != -1) {
          int candidate = dp[i - 1][j - 1] + curNum2 * j + curNum1;
          if (candidate > best) best = candidate;
        }
        dp[i][j] = best;
      }
    }

    for (int t = 0; t <= n; ++t) {
      int reduction = dp[n][t];
      if (reduction == -1) continue;
      int finalSum = totalSum1 + totalSum2 * t - reduction;
      if (finalSum <= x) return t;
    }
    return -1;
  }
}
```

## Golang

```go
func minimumTime(nums1 []int, nums2 []int, x int) int {
	type pair struct{ a, b int }
	n := len(nums1)
	pairs := make([]pair, n)
	var sumA, sumB int64
	for i := 0; i < n; i++ {
		pairs[i] = pair{a: nums1[i], b: nums2[i]}
		sumA += int64(nums1[i])
		sumB += int64(nums2[i])
	}
	// sort by nums2 (b) ascending
	sort.Slice(pairs, func(i, j int) bool { return pairs[i].b < pairs[j].b })

	const neg = int64(-1 << 60)
	// dp[i][j] = max reduction using first i elements with exactly j operations
	dp := make([][]int64, n+1)
	for i := range dp {
		dp[i] = make([]int64, n+1)
		for j := range dp[i] {
			dp[i][j] = neg
		}
	}
	dp[0][0] = 0

	for i := 1; i <= n; i++ {
		a := int64(pairs[i-1].a)
		b := int64(pairs[i-1].b)
		for j := 0; j <= i; j++ {
			// not take this element
			if dp[i-1][j] > dp[i][j] {
				dp[i][j] = dp[i-1][j]
			}
			// take this element as the j-th operation
			if j > 0 && dp[i-1][j-1] != neg {
				val := dp[i-1][j-1] + b*int64(j) + a
				if val > dp[i][j] {
					dp[i][j] = val
				}
			}
		}
	}

	for t := 0; t <= n; t++ {
		total := sumA + sumB*int64(t) - dp[n][t]
		if total <= int64(x) {
			return t
		}
	}
	return -1
}
```

## Ruby

```ruby
def minimum_time(nums1, nums2, x)
  n = nums1.length
  pairs = nums1.zip(nums2).sort_by { |_, b| b }

  total_nums1 = nums1.sum
  total_nums2 = nums2.sum

  neg_inf = -10**18
  dp = Array.new(n + 1, neg_inf)
  dp[0] = 0

  pairs.each do |a, b|
    # update in reverse to avoid reuse within same iteration
    (n).downto(1) do |j|
      prev = dp[j - 1]
      next if prev == neg_inf
      val = prev + b * j + a
      dp[j] = val if val > dp[j]
    end
  end

  (0..n).each do |t|
    next if dp[t] == neg_inf
    current_sum = total_nums1 + total_nums2 * t - dp[t]
    return t if current_sum <= x
  end

  -1
end
```

## Scala

```scala
object Solution {
  def minimumTime(nums1: List[Int], nums2: List[Int], x: Int): Int = {
    val n = nums1.length
    // Pair and sort by nums2 ascending
    val paired = (nums1 zip nums2).sortBy(_._2)
    val a = paired.map(_._1.toLong).toArray
    val b = paired.map(_._2.toLong).toArray

    // dp[i][j] = max reduction using j operations among first i elements
    val INF_NEG = Long.MinValue / 4
    val dp = Array.ofDim[Long](n + 1, n + 1)
    for (i <- 0 to n; j <- 0 to n) dp(i)(j) = INF_NEG
    dp(0)(0) = 0L

    for (i <- 1 to n) {
      dp(i)(0) = 0L
      val v1 = a(i - 1)
      val v2 = b(i - 1)
      var j = 1
      while (j <= i) {
        val take = dp(i - 1)(j - 1) + v1 + v2 * j
        val notTake = dp(i - 1)(j)
        dp(i)(j) = if (take > notTake) take else notTake
        j += 1
      }
    }

    val sum1 = nums1.map(_.toLong).sum
    val sum2 = nums2.map(_.toLong).sum

    var t = 0
    while (t <= n) {
      val reduction = dp(n)(t)
      if (reduction > INF_NEG) {
        val curSum = sum1 + sum2 * t - reduction
        if (curSum <= x) return t
      }
      t += 1
    }
    -1
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time(nums1: Vec<i32>, nums2: Vec<i32>, x: i32) -> i32 {
        let n = nums1.len();
        // Pair (nums2, nums1) and sort by nums2 ascending
        let mut pairs: Vec<(i64, i64)> = (0..n)
            .map(|i| (nums2[i] as i64, nums1[i] as i64))
            .collect();
        pairs.sort_by_key(|k| k.0);

        let total_nums1: i64 = nums1.iter().map(|&v| v as i64).sum();
        let total_nums2: i64 = nums2.iter().map(|&v| v as i64).sum();

        // dp[j] = max reduction using exactly j operations
        let mut dp = vec![i64::MIN / 4; n + 1];
        dp[0] = 0;
        for (idx, &(b, a)) in pairs.iter().enumerate() {
            // iterate j backwards to avoid reuse within same iteration
            for j in (1..=idx + 1).rev() {
                let candidate = dp[j - 1] + a + b * (j as i64);
                if candidate > dp[j] {
                    dp[j] = candidate;
                }
            }
        }

        for t in 0..=n {
            let reduced = dp[t];
            // reduced is always defined because we can pick any t distinct indices
            let total = total_nums1 + (t as i64) * total_nums2 - reduced;
            if total <= x as i64 {
                return t as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-time nums1 nums2 x)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums1))
         (pairs (map vector nums1 nums2))
         (sorted (sort pairs (lambda (a b) (< (vector-ref a 1) (vector-ref b 1)))))
         (total1 (apply + nums1))
         (total2 (apply + nums2))
         (neg-inf -1000000000000)
         (dp (make-vector (add1 n) neg-inf)))
    (vector-set! dp 0 0)
    (let loop ((idx 0) (rest sorted))
      (if (null? rest)
          (let find ((t 0))
            (cond [(> t n) -1]
                  [else
                   (let* ((reduced (vector-ref dp t))
                          (sum (+ total1 (* total2 t) (- reduced))))
                     (if (<= sum x)
                         t
                         (find (add1 t))))]))
          (let* ((pair (car rest))
                 (a (vector-ref pair 0))
                 (b (vector-ref pair 1)))
            (for ([j (in-range (add1 idx) 0 -1)])
              (let* ((prev (vector-ref dp (sub1 j)))
                     (cand (+ prev (+ (* b j) a))))
                (when (> cand (vector-ref dp j))
                  (vector-set! dp j cand))))
            (loop (add1 idx) (cdr rest)))))))
```

## Erlang

```erlang
-spec minimum_time(Nums1 :: [integer()], Nums2 :: [integer()], X :: integer()) -> integer().
minimum_time(Nums1, Nums2, X) ->
    N = length(Nums1),
    TotalA = lists:sum(Nums1),
    TotalB = lists:sum(Nums2),

    % Pair and sort by nums2 ascending
    Pairs = lists:keysort(1, lists:zip(Nums2, Nums1)),

    % Initialize dp tuple: size N+1, dp[0]=0, others = very negative
    NegInf = -1000000000,
    InitDp = erlang:make_tuple(N + 1, NegInf),
    Dp = setelement(1, InitDp, 0),

    % Process each element updating DP
    FinalDp = process_elements(Pairs, 1, N, Dp),

    % Find minimal t satisfying condition
    find_min(0, N, TotalA, TotalB, X, FinalDp).

% Recursive processing of sorted pairs
process_elements([], _Idx, _N, Dp) ->
    Dp;
process_elements([{B, A} | Rest], Idx, N, Dp0) ->
    Dp1 = update_j(Idx, B, A, Dp0),
    process_elements(Rest, Idx + 1, N, Dp1).

% Update DP for current element, iterating j from Idx down to 1
update_j(0, _B, _A, Dp) ->
    Dp;
update_j(J, B, A, Dp) ->
    Prev = element(J, Dp),          % dp[j-1]
    Curr = element(J + 1, Dp),      % dp[j] before update
    Cand = Prev + B * J + A,
    NewVal = if Cand > Curr -> Cand; true -> Curr end,
    Dp1 = setelement(J + 1, Dp, NewVal),
    update_j(J - 1, B, A, Dp1).

% Find minimal t such that remaining sum <= X
find_min(T, N, TotalA, TotalB, X, Dp) when T =< N ->
    Reduction = element(T + 1, Dp),          % dp[t]
    Remaining = TotalA + TotalB * T - Reduction,
    if Remaining =< X -> T;
       true -> find_min(T + 1, N, TotalA, TotalB, X, Dp)
    end;
find_min(_, _, _, _, _, _) ->
    -1.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time(nums1 :: [integer], nums2 :: [integer], x :: integer) :: integer
  def minimum_time(nums1, nums2, x) do
    n = length(nums1)

    pairs =
      Enum.zip(nums1, nums2)
      |> Enum.sort_by(fn {_a, b} -> b end)

    sorted_nums1 = Enum.map(pairs, fn {a, _b} -> a end)
    sorted_nums2 = Enum.map(pairs, fn {_a, b} -> b end)

    neg_inf = -10_000_000_000_000
    prev = :array.new(n + 1, default: neg_inf) |> :array.set(0, 0)

    {dp_last, _} =
      Enum.zip(sorted_nums1, sorted_nums2)
      |> Enum.with_index()
      |> Enum.reduce({prev, 0}, fn {{a, b}, i}, {prev_arr, _cnt} ->
        cur = :array.new(n + 1, default: neg_inf)

        max_j = i + 1

        cur =
          Enum.reduce(0..max_j, cur, fn j, acc ->
            without = :array.get(j, prev_arr)

            with =
              if j > 0 do
                base = :array.get(j - 1, prev_arr)

                if base == neg_inf do
                  neg_inf
                else
                  base + a + b * j
                end
              else
                neg_inf
              end

            best = if without > with, do: without, else: with
            :array.set(j, best, acc)
          end)

        {cur, i + 1}
      end)

    # best reduction achievable with up to t operations
    best_up_to =
      0..n
      |> Enum.map_reduce(neg_inf, fn t, best ->
        val = :array.get(t, dp_last)
        new_best = if val > best, do: val, else: best
        {new_best, new_best}
      end)
      |> elem(0)

    sum1 = Enum.sum(nums1)
    sum2 = Enum.sum(nums2)

    answer =
      0..n
      |> Enum.find(fn t ->
        total = sum1 + sum2 * t - Enum.at(best_up_to, t)
        total <= x
      end)

    case answer do
      nil -> -1
      v -> v
    end
  end
end
```
