# 1031. Maximum Sum of Two Non-Overlapping Subarrays

## Cpp

```cpp
class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        auto getSum = [&](int l, int r) { return pref[r] - pref[l]; }; // [l,r)
        
        vector<int> sumFirst(n - firstLen + 1);
        for (int i = 0; i <= n - firstLen; ++i) sumFirst[i] = getSum(i, i + firstLen);
        vector<int> sumSecond(n - secondLen + 1);
        for (int i = 0; i <= n - secondLen; ++i) sumSecond[i] = getSum(i, i + secondLen);
        
        auto compute = [&](const vector<int>& a, int lenA,
                           const vector<int>& b, int lenB) {
            int best = INT_MIN;
            int ans = 0;
            int i = 0; // index for a
            for (int j = 0; j < (int)b.size(); ++j) {
                while (i <= j - lenA && i < (int)a.size()) {
                    best = max(best, a[i]);
                    ++i;
                }
                if (best != INT_MIN) ans = max(ans, best + b[j]);
            }
            return ans;
        };
        
        int res1 = compute(sumFirst, firstLen, sumSecond, secondLen);
        int res2 = compute(sumSecond, secondLen, sumFirst, firstLen);
        return max(res1, res2);
    }
};
```

## Java

```java
class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        return Math.max(maxSum(nums, firstLen, secondLen), maxSum(nums, secondLen, firstLen));
    }
    
    private int maxSum(int[] nums, int L, int M) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        // max sum of length L subarray ending at or before each index
        int[] leftMax = new int[n];
        int curL = 0;
        for (int i = L - 1; i < n; i++) {
            curL = prefix[i + 1] - prefix[i + 1 - L];
            if (i == L - 1) {
                leftMax[i] = curL;
            } else {
                leftMax[i] = Math.max(leftMax[i - 1], curL);
            }
        }
        // fill earlier positions with 0 (won't be used)
        for (int i = 0; i < L - 1; i++) {
            leftMax[i] = 0;
        }
        
        // max sum of length M subarray starting at or after each index
        int[] rightMax = new int[n];
        int curM = 0;
        for (int i = n - M; i >= 0; i--) {
            curM = prefix[i + M] - prefix[i];
            if (i == n - M) {
                rightMax[i] = curM;
            } else {
                rightMax[i] = Math.max(rightMax[i + 1], curM);
            }
        }
        // fill later positions with 0 (won't be used)
        for (int i = n - M + 1; i < n; i++) {
            rightMax[i] = 0;
        }
        
        int ans = 0;
        // L subarray ends at i, M subarray starts after i
        for (int i = L - 1; i <= n - M - 1; i++) {
            ans = Math.max(ans, leftMax[i] + rightMax[i + 1]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def max_sum(L, M):
            # max sum where L-length subarray appears before M-length subarray
            sumL = [0] * n
            for i in range(L - 1, n):
                sumL[i] = prefix[i + 1] - prefix[i + 1 - L]

            maxL = [0] * n
            cur = 0
            for i in range(n):
                if i >= L - 1:
                    cur = max(cur, sumL[i])
                maxL[i] = cur

            best = 0
            for j in range(L + M - 1, n):
                sumM = prefix[j + 1] - prefix[j + 1 - M]
                total = maxL[j - M] + sumM
                if total > best:
                    best = total
            return best

        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))
```

## Python3

```python
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        def window_sums(L: int) -> List[int]:
            return [prefix[i + L] - prefix[i] for i in range(n - L + 1)]

        sum_first = window_sums(firstLen)
        sum_second = window_sums(secondLen)

        ans = 0

        # first subarray before second
        max_first = 0
        for start_second in range(firstLen, n - secondLen + 1):
            max_first = max(max_first, sum_first[start_second - firstLen])
            ans = max(ans, max_first + sum_second[start_second])

        # second subarray before first
        max_second = 0
        for start_first in range(secondLen, n - firstLen + 1):
            max_second = max(max_second, sum_second[start_first - secondLen])
            ans = max(ans, max_second + sum_first[start_first])

        return ans
```

## C

```c
int maxSumTwoNoOverlap(int* nums, int numsSize, int firstLen, int secondLen) {
    // Prefix sum array
    int *prefix = (int *)malloc((numsSize + 1) * sizeof(int));
    prefix[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    // Helper lambda simulated with a static inline function
    int compute(int L, int M) {
        int *left = (int *)malloc(numsSize * sizeof(int));
        int *right = (int *)malloc(numsSize * sizeof(int));

        // left[i]: max sum of an L-length subarray ending at or before i
        for (int i = 0; i < numsSize; ++i) {
            if (i >= L - 1) {
                int cur = prefix[i + 1] - prefix[i + 1 - L];
                if (i == L - 1)
                    left[i] = cur;
                else
                    left[i] = left[i - 1] > cur ? left[i - 1] : cur;
            } else {
                left[i] = 0; // not enough elements yet
            }
        }

        // right[i]: max sum of an M-length subarray starting at or after i
        for (int i = numsSize - 1; i >= 0; --i) {
            if (i + M <= numsSize) {
                int cur = prefix[i + M] - prefix[i];
                if (i == numsSize - M)
                    right[i] = cur;
                else
                    right[i] = right[i + 1] > cur ? right[i + 1] : cur;
            } else {
                right[i] = 0; // not enough elements remaining
            }
        }

        int best = 0;
        for (int i = L - 1; i <= numsSize - M - 1; ++i) {
            int total = left[i] + right[i + 1];
            if (total > best) best = total;
        }

        free(left);
        free(right);
        return best;
    }

    int ans1 = compute(firstLen, secondLen);
    int ans2 = compute(secondLen, firstLen);
    int result = ans1 > ans2 ? ans1 : ans2;

    free(prefix);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        return Math.Max(Helper(nums, firstLen, secondLen), Helper(nums, secondLen, firstLen));
    }

    private int Helper(int[] nums, int L, int M) {
        int n = nums.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];

        int lenL = n - L + 1;
        int[] sumL = new int[lenL];
        for (int i = 0; i < lenL; i++) {
            sumL[i] = pref[i + L] - pref[i];
        }

        int lenM = n - M + 1;
        int[] sumM = new int[lenM];
        for (int i = 0; i < lenM; i++) {
            sumM[i] = pref[i + M] - pref[i];
        }

        int[] maxMSuffix = new int[lenM];
        for (int i = lenM - 1; i >= 0; i--) {
            if (i == lenM - 1) maxMSuffix[i] = sumM[i];
            else maxMSuffix[i] = Math.Max(maxMSuffix[i + 1], sumM[i]);
        }

        int ans = 0;
        for (int i = 0; i < lenL; i++) {
            int startM = i + L;
            if (startM <= n - M) {
                int bestM = maxMSuffix[startM];
                ans = Math.Max(ans, sumL[i] + bestM);
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} firstLen
 * @param {number} secondLen
 * @return {number}
 */
var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    
    const maxWithOrder = (lenA, lenB) => {
        // sum of subarray length lenA ending at each index
        const sumA = new Array(n).fill(0);
        for (let i = lenA - 1; i < n; ++i) {
            sumA[i] = prefix[i + 1] - prefix[i + 1 - lenA];
        }
        // sum of subarray length lenB ending at each index
        const sumB = new Array(n).fill(0);
        for (let i = lenB - 1; i < n; ++i) {
            sumB[i] = prefix[i + 1] - prefix[i + 1 - lenB];
        }
        // best A up to each index
        const bestA = new Array(n).fill(0);
        let curBest = 0;
        for (let i = 0; i < n; ++i) {
            if (i >= lenA - 1) {
                curBest = Math.max(curBest, sumA[i]);
            }
            bestA[i] = curBest;
        }
        // combine B after A
        let ans = 0;
        for (let j = lenB - 1; j < n; ++j) {
            const leftIdx = j - lenB; // last index where A can end
            if (leftIdx >= 0) {
                ans = Math.max(ans, sumB[j] + bestA[leftIdx]);
            }
        }
        return ans;
    };
    
    return Math.max(
        maxWithOrder(firstLen, secondLen),
        maxWithOrder(secondLen, firstLen)
    );
};
```

## Typescript

```typescript
function maxSumTwoNoOverlap(nums: number[], firstLen: number, secondLen: number): number {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];

    const sumFirst = new Array(n - firstLen + 1);
    for (let i = 0; i <= n - firstLen; ++i) {
        sumFirst[i] = pref[i + firstLen] - pref[i];
    }
    const sumSecond = new Array(n - secondLen + 1);
    for (let i = 0; i <= n - secondLen; ++i) {
        sumSecond[i] = pref[i + secondLen] - pref[i];
    }

    let ans = 0;

    // firstLen subarray before secondLen subarray
    let maxFirst = -Infinity;
    for (let i = 0; i <= n - secondLen; ++i) {
        if (i - firstLen >= 0) {
            maxFirst = Math.max(maxFirst, sumFirst[i - firstLen]);
        }
        if (maxFirst !== -Infinity) {
            ans = Math.max(ans, maxFirst + sumSecond[i]);
        }
    }

    // secondLen subarray before firstLen subarray
    let maxSecond = -Infinity;
    for (let i = 0; i <= n - firstLen; ++i) {
        if (i - secondLen >= 0) {
            maxSecond = Math.max(maxSecond, sumSecond[i - secondLen]);
        }
        if (maxSecond !== -Infinity) {
            ans = Math.max(ans, maxSecond + sumFirst[i]);
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
     * @param Integer $firstLen
     * @param Integer $secondLen
     * @return Integer
     */
    function maxSumTwoNoOverlap($nums, $firstLen, $secondLen) {
        $n = count($nums);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }

        $ans = 0;

        // firstLen before secondLen
        $maxFirst = 0;
        for ($i = $firstLen; $i + $secondLen <= $n; $i++) {
            $sumFirst = $prefix[$i] - $prefix[$i - $firstLen];
            if ($sumFirst > $maxFirst) {
                $maxFirst = $sumFirst;
            }
            $sumSecond = $prefix[$i + $secondLen] - $prefix[$i];
            $total = $maxFirst + $sumSecond;
            if ($total > $ans) {
                $ans = $total;
            }
        }

        // secondLen before firstLen
        $maxSecond = 0;
        for ($i = $secondLen; $i + $firstLen <= $n; $i++) {
            $sumSecond = $prefix[$i] - $prefix[$i - $secondLen];
            if ($sumSecond > $maxSecond) {
                $maxSecond = $sumSecond;
            }
            $sumFirst = $prefix[$i + $firstLen] - $prefix[$i];
            $total = $maxSecond + $sumFirst;
            if ($total > $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumTwoNoOverlap(_ nums: [Int], _ firstLen: Int, _ secondLen: Int) -> Int {
        func maxSum(_ arr: [Int], _ L: Int, _ M: Int) -> Int {
            let n = arr.count
            var prefix = [Int](repeating: 0, count: n + 1)
            for i in 0..<n {
                prefix[i + 1] = prefix[i] + arr[i]
            }
            var maxL = 0
            var result = 0
            // start index of M-length subarray
            if n < L + M { return 0 }
            for i in L...(n - M) {
                let sumL = prefix[i] - prefix[i - L]
                if sumL > maxL { maxL = sumL }
                let sumM = prefix[i + M] - prefix[i]
                let total = maxL + sumM
                if total > result { result = total }
            }
            return result
        }
        
        let option1 = maxSum(nums, firstLen, secondLen)
        let option2 = maxSum(nums, secondLen, firstLen)
        return max(option1, option2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumTwoNoOverlap(nums: IntArray, firstLen: Int, secondLen: Int): Int {
        val n = nums.size
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + nums[i]
        }

        fun maxSum(lenA: Int, lenB: Int): Int {
            val leftMax = IntArray(n)
            var cur = prefix[lenA] - prefix[0]
            var best = cur
            leftMax[lenA - 1] = best
            for (i in lenA until n) {
                cur = prefix[i + 1] - prefix[i + 1 - lenA]
                if (cur > best) best = cur
                leftMax[i] = best
            }
            var ans = 0
            for (startB in lenA..n - lenB) {
                val sumB = prefix[startB + lenB] - prefix[startB]
                val candidate = leftMax[startB - 1] + sumB
                if (candidate > ans) ans = candidate
            }
            return ans
        }

        val option1 = maxSum(firstLen, secondLen)
        val option2 = maxSum(secondLen, firstLen)
        return kotlin.math.max(option1, option2)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxSumTwoNoOverlap(List<int> nums, int firstLen, int secondLen) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }

    int helper(int lenA, int lenB) {
      int maxA = 0;
      int result = 0;
      for (int i = lenA; i + lenB <= n; ++i) {
        int sumA = prefix[i] - prefix[i - lenA];
        if (sumA > maxA) maxA = sumA;
        int sumB = prefix[i + lenB] - prefix[i];
        int total = maxA + sumB;
        if (total > result) result = total;
      }
      return result;
    }

    int ans1 = helper(firstLen, secondLen);
    int ans2 = helper(secondLen, firstLen);
    return max(ans1, ans2);
  }
}
```

## Golang

```go
func maxSumTwoNoOverlap(nums []int, firstLen int, secondLen int) int {
	n := len(nums)
	prefix := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + nums[i]
	}
	getSum := func(start, length int) int {
		return prefix[start+length] - prefix[start]
	}

	maxTotal := 0

	// firstLen before secondLen
	maxFirst := 0
	for i := firstLen; i+secondLen <= n; i++ {
		curFirst := getSum(i-firstLen, firstLen)
		if curFirst > maxFirst {
			maxFirst = curFirst
		}
		curSecond := getSum(i, secondLen)
		if total := maxFirst + curSecond; total > maxTotal {
			maxTotal = total
		}
	}

	// secondLen before firstLen
	maxSecond := 0
	for i := secondLen; i+firstLen <= n; i++ {
		curSecond := getSum(i-secondLen, secondLen)
		if curSecond > maxSecond {
			maxSecond = curSecond
		}
		curFirst := getSum(i, firstLen)
		if total := maxSecond + curFirst; total > maxTotal {
			maxTotal = total
		}
	}

	return maxTotal
}
```

## Ruby

```ruby
def max_sum_two_no_overlap(nums, first_len, second_len)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }

  compute = lambda do |l, r|
    best_l = Array.new(n, 0)
    max_sofar = 0
    (l - 1...n).each do |i|
      sum_l = prefix[i + 1] - prefix[i + 1 - l]
      max_sofar = [max_sofar, sum_l].max
      best_l[i] = max_sofar
    end

    result = 0
    (r - 1...n).each do |j|
      sum_r = prefix[j + 1] - prefix[j + 1 - r]
      idx = j - r
      next if idx < 0
      total = best_l[idx] + sum_r
      result = [result, total].max
    end
    result
  end

  ans1 = compute.call(first_len, second_len)
  ans2 = compute.call(second_len, first_len)
  [ans1, ans2].max
end
```

## Scala

```scala
object Solution {
    def maxSumTwoNoOverlap(nums: Array[Int], firstLen: Int, secondLen: Int): Int = {
        val n = nums.length
        val pref = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = pref(i) + nums(i)
            i += 1
        }

        def maxSum(lenA: Int, lenB: Int): Int = {
            var maxA = 0
            var best = 0
            var startB = lenA
            while (startB <= n - lenB) {
                val sumA = pref(startB) - pref(startB - lenA)
                if (sumA > maxA) maxA = sumA
                val sumB = pref(startB + lenB) - pref(startB)
                val cand = maxA + sumB
                if (cand > best) best = cand
                startB += 1
            }
            best
        }

        math.max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_two_no_overlap(nums: Vec<i32>, first_len: i32, second_len: i32) -> i32 {
        let n = nums.len();
        let fl = first_len as usize;
        let sl = second_len as usize;

        // Prefix sums for O(1) window sum queries
        let mut pre = vec![0i64; n + 1];
        for i in 0..n {
            pre[i + 1] = pre[i] + nums[i] as i64;
        }

        // Sums of all windows with length first_len
        let mut sum_first = Vec::with_capacity(n - fl + 1);
        for i in 0..=n - fl {
            sum_first.push(pre[i + fl] - pre[i]);
        }
        // Sums of all windows with length second_len
        let mut sum_second = Vec::with_capacity(n - sl + 1);
        for i in 0..=n - sl {
            sum_second.push(pre[i + sl] - pre[i]);
        }

        let mut ans: i64 = 0;

        if !sum_first.is_empty() && !sum_second.is_empty() {
            // first_len window before second_len window
            let mut pref_max_first = vec![0i64; sum_first.len()];
            for (i, &v) in sum_first.iter().enumerate() {
                pref_max_first[i] = if i == 0 { v } else { pref_max_first[i - 1].max(v) };
            }
            for j in 0..sum_second.len() {
                if j >= fl {
                    let cand = pref_max_first[j - fl] + sum_second[j];
                    if cand > ans {
                        ans = cand;
                    }
                }
            }

            // second_len window before first_len window
            let mut pref_max_second = vec![0i64; sum_second.len()];
            for (i, &v) in sum_second.iter().enumerate() {
                pref_max_second[i] = if i == 0 { v } else { pref_max_second[i - 1].max(v) };
            }
            for i in 0..sum_first.len() {
                if i >= sl {
                    let cand = pref_max_second[i - sl] + sum_first[i];
                    if cand > ans {
                        ans = cand;
                    }
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-sum-two-no-overlap nums firstLen secondLen)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         ;; prefix sums
         (pref (make-vector (+ n 1) 0)))
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1)
                   (+ (vector-ref pref i) (vector-ref v i))))
    (define (window-sums len)
      (for/list ([s (in-range 0 (+ 1 (- n len)))])
        (- (vector-ref pref (+ s len))
           (vector-ref pref s))))
    (define sumA-vec (list->vector (window-sums firstLen)))
    (define sumB-vec (list->vector (window-sums secondLen)))
    (define lenA (vector-length sumA-vec))
    (define lenB (vector-length sumB-vec))
    ;; suffix max for B
    (define suffixMaxB (make-vector lenB 0))
    (let loop ((i (- lenB 1)) (mx -1))
      (when (>= i 0)
        (let ((val (vector-ref sumB-vec i)))
          (when (> val mx) (set! mx val))
          (vector-set! suffixMaxB i mx)
          (loop (- i 1) mx))))
    ;; suffix max for A
    (define suffixMaxA (make-vector lenA 0))
    (let loop ((i (- lenA 1)) (mx -1))
      (when (>= i 0)
        (let ((val (vector-ref sumA-vec i)))
          (when (> val mx) (set! mx val))
          (vector-set! suffixMaxA i mx)
          (loop (- i 1) mx))))
    (define best 0)
    ;; firstLen subarray before secondLen subarray
    (for ([i (in-range lenA)])
      (let ((idx (+ i firstLen))) ; start index for second subarray
        (when (< idx lenB)
          (let ((cand (+ (vector-ref sumA-vec i)
                         (vector-ref suffixMaxB idx))))
            (when (> cand best) (set! best cand))))))
    ;; secondLen subarray before firstLen subarray
    (for ([j (in-range lenB)])
      (let ((idx (+ j secondLen))) ; start index for first subarray
        (when (< idx lenA)
          (let ((cand (+ (vector-ref sumB-vec j)
                         (vector-ref suffixMaxA idx))))
            (when (> cand best) (set! best cand))))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([max_sum_two_no_overlap/3]).

-spec max_sum_two_no_overlap(Nums :: [integer()], FirstLen :: integer(), SecondLen :: integer()) -> integer().
max_sum_two_no_overlap(Nums, FirstLen, SecondLen) ->
    N = length(Nums),
    Pref = list_to_tuple(prefix_sums(Nums)),
    Res1 = helper(N, FirstLen, SecondLen, Pref),
    Res2 = helper(N, SecondLen, FirstLen, Pref),
    erlang:max(Res1, Res2).

prefix_sums(List) -> prefix_sums(List, 0, [0]).
prefix_sums([], _Acc, AccList) -> lists:reverse(AccList);
prefix_sums([H|T], Acc, AccList) ->
    New = Acc + H,
    prefix_sums(T, New, [New|AccList]).

helper(N, L1, L2, Pref) ->
    LeftRev = build_left(0, N, L1, Pref, 0, []),
    Left = lists:reverse(LeftRev),
    Right = build_right(N-1, N, L2, Pref, 0, []),
    compute_max_split(L1-1, N - L2 - 1, Left, Right, 0).

build_left(I, N, L, Pref, MaxSoFar, Acc) when I == N ->
    Acc;
build_left(I, N, L, Pref, MaxSoFar, Acc) ->
    NewMax =
        if I >= L-1 ->
                Start = I - L + 1,
                CurSum = element(Start+L+1, Pref) - element(Start+1, Pref),
                erlang:max(MaxSoFar, CurSum);
           true -> MaxSoFar
        end,
    build_left(I+1, N, L, Pref, NewMax, [NewMax|Acc]).

build_right(I, N, L, Pref, MaxSoFar, Acc) when I < 0 ->
    Acc;
build_right(I, N, L, Pref, MaxSoFar, Acc) ->
    NewMax =
        if I =< N - L ->
                CurSum = element(I+L+1, Pref) - element(I+1, Pref),
                erlang:max(MaxSoFar, CurSum);
           true -> MaxSoFar
        end,
    build_right(I-1, N, L, Pref, NewMax, [NewMax|Acc]).

compute_max_split(Start, End, _Left, _Right, Max) when Start > End ->
    Max;
compute_max_split(I, End, Left, Right, Max) ->
    LeftVal = lists:nth(I+1, Left),
    RightVal = lists:nth(I+2, Right),
    NewMax = erlang:max(Max, LeftVal + RightVal),
    compute_max_split(I+1, End, Left, Right, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_two_no_overlap(nums :: [integer], first_len :: integer, second_len :: integer) :: integer
  def max_sum_two_no_overlap(nums, first_len, second_len) do
    n = length(nums)

    # prefix sums
    pref =
      Enum.reduce(nums, [0], fn x, acc ->
        [hd(acc) + x | acc]
      end)
      |> Enum.reverse()

    sum_range = fn i, len ->
      Enum.at(pref, i + len) - Enum.at(pref, i)
    end

    # sums of subarrays with given lengths
    sums_l =
      for i <- 0..(n - first_len), do: sum_range.(i, first_len)

    sums_m =
      for i <- 0..(n - second_len), do: sum_range.(i, second_len)

    # left max of M-length subarrays up to each index
    {_, left_max_rev} =
      Enum.reduce(sums_m, {-1_000_000_000, []}, fn val, {cur_max, acc} ->
        new_max = if val > cur_max, do: val, else: cur_max
        {new_max, [new_max | acc]}
      end)

    left_max = Enum.reverse(left_max_rev)

    # right max of M-length subarrays from each index to the end
    {_, right_max_rev} =
      Enum.reduce(Enum.reverse(sums_m), {-1_000_000_000, []}, fn val, {cur_max, acc} ->
        new_max = if val > cur_max, do: val, else: cur_max
        {new_max, [new_max | acc]}
      end)

    right_max = Enum.reverse(right_max_rev)

    m_len = length(sums_m)

    # evaluate all positions of the first subarray
    Enum.reduce(0..(length(sums_l) - 1), 0, fn i, best ->
      l_sum = Enum.at(sums_l, i)
      best =
        if i + first_len <= m_len - 1 do
          total = l_sum + Enum.at(right_max, i + first_len)
          if total > best, do: total, else: best
        else
          best
        end

      best =
        if i >= second_len do
          total = l_sum + Enum.at(left_max, i - second_len)
          if total > best, do: total, else: best
        else
          best
        end

      best
    end)
  end
end
```
