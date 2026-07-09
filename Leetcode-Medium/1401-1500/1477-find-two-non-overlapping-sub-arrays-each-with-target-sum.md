# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

## Cpp

```cpp
class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        const int INF = n + 5;
        vector<int> bestEnd(n, INF), bestStart(n, INF);
        
        long long sum = 0;
        int left = 0;
        for (int right = 0; right < n; ++right) {
            sum += arr[right];
            while (sum > target && left <= right) {
                sum -= arr[left++];
            }
            if (sum == target) {
                int len = right - left + 1;
                bestEnd[right] = min(bestEnd[right], len);
                bestStart[left] = min(bestStart[left], len);
            }
        }
        
        vector<int> pref(n, INF), suff(n, INF);
        for (int i = 0; i < n; ++i) {
            if (i == 0) pref[i] = bestEnd[i];
            else pref[i] = min(pref[i-1], bestEnd[i]);
        }
        for (int i = n - 1; i >= 0; --i) {
            if (i == n - 1) suff[i] = bestStart[i];
            else suff[i] = min(suff[i+1], bestStart[i]);
        }
        
        int ans = INF;
        for (int i = 0; i < n - 1; ++i) {
            if (pref[i] != INF && suff[i + 1] != INF) {
                ans = min(ans, pref[i] + suff[i + 1]);
            }
        }
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int INF = Integer.MAX_VALUE / 2;
        int[] best = new int[n];
        Arrays.fill(best, INF);
        int sum = 0, left = 0;
        int answer = INF;

        for (int right = 0; right < n; ++right) {
            sum += arr[right];
            while (sum > target && left <= right) {
                sum -= arr[left++];
            }
            if (sum == target) {
                int len = right - left + 1;
                if (left > 0 && best[left - 1] != INF) {
                    answer = Math.min(answer, len + best[left - 1]);
                }
                best[right] = Math.min(best[right], len);
            }
            if (right > 0) {
                best[right] = Math.min(best[right], best[right - 1]);
            }
        }
        return answer == INF ? -1 : answer;
    }
}
```

## Python

```python
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = 10**9

        best_start = [INF] * n   # minimal length of subarray starting at i with sum == target
        best_end = [INF] * n     # minimal length of subarray ending at i with sum == target

        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target and left <= right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                length = right - left + 1
                if best_start[left] > length:
                    best_start[left] = length
                if best_end[right] > length:
                    best_end[right] = length

        # prefix minima of best_end
        pref = [INF] * n
        pref[0] = best_end[0]
        for i in range(1, n):
            pref[i] = min(pref[i-1], best_end[i])

        # suffix minima of best_start
        suff = [INF] * n
        suff[-1] = best_start[-1]
        for i in range(n-2, -1, -1):
            suff[i] = min(suff[i+1], best_start[i])

        ans = INF
        for i in range(n-1):
            if pref[i] < INF and suff[i+1] < INF:
                ans = min(ans, pref[i] + suff[i+1])

        return -1 if ans == INF else ans
```

## Python3

```python
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        # prefix[i]: minimal length of a subarray with sum=target that ends at or before i
        prefix = [INF] * n
        left = 0
        cur_sum = 0
        best_len = INF
        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target and left <= right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                length = right - left + 1
                best_len = min(best_len, length)
            prefix[right] = best_len

        # start_len[i]: length of subarray starting at i with sum=target (or INF)
        start_len = [INF] * n
        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += arr[right]
            while cur_sum > target and left <= right:
                cur_sum -= arr[left]
                left += 1
            if cur_sum == target:
                start_len[left] = right - left + 1

        # suffix[i]: minimal length of a subarray with sum=target that starts at or after i
        suffix = [INF] * n
        best_len = INF
        for i in range(n - 1, -1, -1):
            if start_len[i] != INF:
                best_len = min(best_len, start_len[i])
            suffix[i] = best_len

        ans = INF
        for i in range(n - 1):
            if prefix[i] != INF and suffix[i + 1] != INF:
                ans = min(ans, prefix[i] + suffix[i + 1])

        return -1 if ans == INF else ans
```

## C

```c
int minSumOfLengths(int* arr, int arrSize, int target) {
    if (arrSize < 2) return -1;
    const int INF = arrSize + 5;

    int *lenStart = (int*)malloc(sizeof(int) * arrSize);
    int *lenEnd   = (int*)malloc(sizeof(int) * arrSize);
    for (int i = 0; i < arrSize; ++i) {
        lenStart[i] = INF;
        lenEnd[i]   = INF;
    }

    long long sum = 0;
    int left = 0;
    for (int right = 0; right < arrSize; ++right) {
        sum += arr[right];
        while (sum > target && left <= right) {
            sum -= arr[left];
            ++left;
        }
        if (sum == target) {
            int len = right - left + 1;
            if (len < lenStart[left]) lenStart[left] = len;
            if (len < lenEnd[right])   lenEnd[right]   = len;
        }
    }

    int *prefixMin = (int*)malloc(sizeof(int) * arrSize);
    int cur = INF;
    for (int i = 0; i < arrSize; ++i) {
        if (lenEnd[i] < cur) cur = lenEnd[i];
        prefixMin[i] = cur;
    }

    int *suffixMin = (int*)malloc(sizeof(int) * arrSize);
    cur = INF;
    for (int i = arrSize - 1; i >= 0; --i) {
        if (lenStart[i] < cur) cur = lenStart[i];
        suffixMin[i] = cur;
    }

    int answer = INF;
    for (int i = 0; i < arrSize - 1; ++i) {
        if (prefixMin[i] < INF && suffixMin[i + 1] < INF) {
            int total = prefixMin[i] + suffixMin[i + 1];
            if (total < answer) answer = total;
        }
    }

    free(lenStart);
    free(lenEnd);
    free(prefixMin);
    free(suffixMin);

    return (answer == INF) ? -1 : answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSumOfLengths(int[] arr, int target) {
        int n = arr.Length;
        const int INF = int.MaxValue / 2;
        int[] best = new int[n];
        for (int i = 0; i < n; ++i) best[i] = INF;

        int left = 0, sum = 0;
        int ans = INF;

        for (int right = 0; right < n; ++right) {
            sum += arr[right];

            while (sum > target && left <= right) {
                sum -= arr[left];
                left++;
            }

            if (sum == target) {
                int len = right - left + 1;
                if (left > 0 && best[left - 1] != INF) {
                    ans = Math.Min(ans, best[left - 1] + len);
                }
                if (right == 0) {
                    best[right] = len;
                } else {
                    best[right] = Math.Min(best[right - 1], len);
                }
            } else {
                if (right > 0) {
                    best[right] = best[right - 1];
                }
            }
        }

        return ans == INF ? -1 : ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var minSumOfLengths = function(arr, target) {
    const n = arr.length;
    const INF = 1e9; // larger than any possible answer (max length sum <= 2*10^5)
    
    const endMin = new Array(n).fill(INF);   // minimal length of subarray ending at i with sum == target
    const startMin = new Array(n).fill(INF); // minimal length of subarray starting at i with sum == target
    
    let sum = 0, left = 0;
    for (let right = 0; right < n; ++right) {
        sum += arr[right];
        while (sum > target && left <= right) {
            sum -= arr[left];
            ++left;
        }
        if (sum === target) {
            const len = right - left + 1;
            endMin[right] = Math.min(endMin[right], len);
            startMin[left] = Math.min(startMin[left], len);
        }
    }
    
    // prefix minima of endMin
    const pref = new Array(n).fill(INF);
    for (let i = 0; i < n; ++i) {
        pref[i] = i === 0 ? endMin[i] : Math.min(pref[i - 1], endMin[i]);
    }
    
    // suffix minima of startMin
    const suff = new Array(n).fill(INF);
    for (let i = n - 1; i >= 0; --i) {
        suff[i] = i === n - 1 ? startMin[i] : Math.min(suff[i + 1], startMin[i]);
    }
    
    let ans = INF;
    for (let i = 0; i < n - 1; ++i) {
        if (pref[i] < INF && suff[i + 1] < INF) {
            ans = Math.min(ans, pref[i] + suff[i + 1]);
        }
    }
    
    return ans === INF ? -1 : ans;
};
```

## Typescript

```typescript
function minSumOfLengths(arr: number[], target: number): number {
    const n = arr.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const best: number[] = new Array(n).fill(INF);
    let left = 0;
    let sum = 0;
    let answer = INF;

    for (let right = 0; right < n; ++right) {
        sum += arr[right];
        while (sum > target && left <= right) {
            sum -= arr[left];
            left++;
        }
        if (sum === target) {
            const len = right - left + 1;
            if (left > 0 && best[left - 1] !== INF) {
                answer = Math.min(answer, best[left - 1] + len);
            }
            best[right] = len;
        }
        if (right > 0) {
            best[right] = Math.min(best[right], best[right - 1]);
        }
    }

    return answer === INF ? -1 : answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function minSumOfLengths($arr, $target) {
        $n = count($arr);
        if ($n == 0) return -1;
        $INF = $n + 5; // larger than any possible length

        // prefix[i]: minimal length of a subarray with sum=target that ends at or before i
        $prefix = array_fill(0, $n, $INF);
        $best = $INF;
        $sum = 0;
        $left = 0;
        for ($right = 0; $right < $n; $right++) {
            $sum += $arr[$right];
            while ($sum > $target && $left <= $right) {
                $sum -= $arr[$left];
                $left++;
            }
            if ($sum == $target) {
                $currLen = $right - $left + 1;
                if ($currLen < $best) {
                    $best = $currLen;
                }
            }
            $prefix[$right] = $best;
        }

        // suffix[i]: minimal length of a subarray with sum=target that starts at or after i
        $suffix = array_fill(0, $n, $INF);
        $best = $INF;
        $sum = 0;
        $right = $n - 1;
        for ($left = $n - 1; $left >= 0; $left--) {
            $sum += $arr[$left];
            while ($sum > $target && $right >= $left) {
                $sum -= $arr[$right];
                $right--;
            }
            if ($sum == $target) {
                $currLen = $right - $left + 1;
                if ($currLen < $best) {
                    $best = $currLen;
                }
            }
            $suffix[$left] = $best;
        }

        $ans = $INF;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($prefix[$i] < $INF && $suffix[$i + 1] < $INF) {
                $total = $prefix[$i] + $suffix[$i + 1];
                if ($total < $ans) {
                    $ans = $total;
                }
            }
        }

        return $ans == $INF ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSumOfLengths(_ arr: [Int], _ target: Int) -> Int {
        let n = arr.count
        var pref = Array(repeating: Int.max, count: n)
        var best = Int.max
        var left = 0
        var sum = 0
        
        // Prefix minima: best length of subarray ending at or before each index
        for right in 0..<n {
            sum += arr[right]
            while sum > target && left <= right {
                sum -= arr[left]
                left += 1
            }
            if sum == target {
                let len = right - left + 1
                if len < best { best = len }
            }
            pref[right] = best
        }
        
        // Record minimal length for subarrays starting at each index
        var startLen = Array(repeating: Int.max, count: n)
        left = 0
        sum = 0
        for right in 0..<n {
            sum += arr[right]
            while sum > target && left <= right {
                sum -= arr[left]
                left += 1
            }
            if sum == target {
                let len = right - left + 1
                if len < startLen[left] { startLen[left] = len }
            }
        }
        
        // Suffix minima: best length of subarray starting at or after each index
        var suffixMin = Array(repeating: Int.max, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffixMin[i] = min(suffixMin[i + 1], startLen[i])
        }
        
        // Combine prefix and suffix to find answer
        var ans = Int.max
        if n >= 2 {
            for i in 0..<(n - 1) {
                let leftBest = pref[i]
                let rightBest = suffixMin[i + 1]
                if leftBest != Int.max && rightBest != Int.max {
                    let total = leftBest + rightBest
                    if total < ans { ans = total }
                }
            }
        }
        
        return ans == Int.max ? -1 : ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        val n = arr.size
        val INF = 1_000_000_007
        val endLen = IntArray(n) { INF }
        val startIdx = IntArray(n) { -1 }

        var left = 0
        var sum = 0L
        for (right in 0 until n) {
            sum += arr[right].toLong()
            while (sum > target && left <= right) {
                sum -= arr[left].toLong()
                left++
            }
            if (sum == target.toLong()) {
                val len = right - left + 1
                endLen[right] = len
                startIdx[right] = left
            }
        }

        val pref = IntArray(n) { INF }
        for (i in 0 until n) {
            pref[i] = if (i == 0) endLen[i] else kotlin.math.min(pref[i - 1], endLen[i])
        }

        var ans = INF
        for (right in 0 until n) {
            val len = endLen[right]
            if (len != INF) {
                val start = startIdx[right]
                if (start > 0 && pref[start - 1] != INF) {
                    ans = kotlin.math.min(ans, len + pref[start - 1])
                }
            }
        }

        return if (ans == INF) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minSumOfLengths(List<int> arr, int target) {
    int n = arr.length;
    const int INF = 1 << 60;

    // Minimum length of a subarray ending at each index with sum == target
    List<int> bestEnd = List.filled(n, INF);
    int sum = 0;
    int left = 0;
    for (int right = 0; right < n; ++right) {
      sum += arr[right];
      while (sum > target && left <= right) {
        sum -= arr[left];
        left++;
      }
      if (sum == target) {
        bestEnd[right] = right - left + 1;
      }
    }

    // Prefix minima of bestEnd
    List<int> pref = List.filled(n, INF);
    for (int i = 0; i < n; ++i) {
      if (i == 0) {
        pref[i] = bestEnd[i];
      } else {
        pref[i] = pref[i - 1] < bestEnd[i] ? pref[i - 1] : bestEnd[i];
      }
    }

    // Minimum length of a subarray starting at each index with sum == target
    List<int> bestStart = List.filled(n, INF);
    sum = 0;
    int rightPtr = n - 1;
    for (int l = n - 1; l >= 0; --l) {
      sum += arr[l];
      while (sum > target && rightPtr >= l) {
        sum -= arr[rightPtr];
        rightPtr--;
      }
      if (sum == target) {
        bestStart[l] = rightPtr - l + 1;
      }
    }

    // Suffix minima of bestStart
    List<int> suff = List.filled(n, INF);
    for (int i = n - 1; i >= 0; --i) {
      if (i == n - 1) {
        suff[i] = bestStart[i];
      } else {
        suff[i] = suff[i + 1] < bestStart[i] ? suff[i + 1] : bestStart[i];
      }
    }

    int ans = INF;
    for (int i = 0; i < n - 1; ++i) {
      if (pref[i] != INF && suff[i + 1] != INF) {
        int total = pref[i] + suff[i + 1];
        if (total < ans) ans = total;
      }
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minSumOfLengths(arr []int, target int) int {
    n := len(arr)
    const INF = int(^uint(0) >> 1)

    // bestLeft[i]: minimum length of a subarray with sum=target that ends at or before i
    bestLeft := make([]int, n)
    best := INF
    left, sum := 0, 0
    for right := 0; right < n; right++ {
        sum += arr[right]
        for sum > target && left <= right {
            sum -= arr[left]
            left++
        }
        if sum == target {
            curLen := right - left + 1
            if curLen < best {
                best = curLen
            }
        }
        bestLeft[right] = best
    }

    // bestRight[i]: minimum length of a subarray with sum=target that starts at or after i
    bestRight := make([]int, n)
    best = INF
    rightIdx := n - 1
    sum = 0
    for leftIdx := n - 1; leftIdx >= 0; leftIdx-- {
        sum += arr[leftIdx]
        for sum > target && rightIdx >= leftIdx {
            sum -= arr[rightIdx]
            rightIdx--
        }
        if sum == target {
            curLen := rightIdx - leftIdx + 1
            if curLen < best {
                best = curLen
            }
        }
        bestRight[leftIdx] = best
    }

    ans := INF
    for i := 0; i < n-1; i++ {
        if bestLeft[i] != INF && bestRight[i+1] != INF {
            total := bestLeft[i] + bestRight[i+1]
            if total < ans {
                ans = total
            }
        }
    }

    if ans == INF {
        return -1
    }
    return ans
}
```

## Ruby

```ruby
def min_sum_of_lengths(arr, target)
  n = arr.length
  inf = 1 << 60

  best_end = Array.new(n, inf)   # minimal length of subarray ending at i with sum == target
  best_start = Array.new(n, inf) # minimal length of subarray starting at i with sum == target

  left = 0
  sum = 0
  arr.each_with_index do |val, right|
    sum += val
    while sum > target && left <= right
      sum -= arr[left]
      left += 1
    end
    if sum == target
      len = right - left + 1
      best_end[right] = len if len < best_end[right]
      best_start[left] = len if len < best_start[left]
    end
  end

  pref = Array.new(n, inf)
  (0...n).each do |i|
    pref[i] = i.zero? ? best_end[i] : [pref[i - 1], best_end[i]].min
  end

  suff = Array.new(n, inf)
  (n - 1).downto(0) do |i|
    suff[i] = i == n - 1 ? best_start[i] : [suff[i + 1], best_start[i]].min
  end

  ans = inf
  (0...n - 1).each do |i|
    if pref[i] < inf && suff[i + 1] < inf
      total = pref[i] + suff[i + 1]
      ans = total if total < ans
    end
  end

  ans == inf ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minSumOfLengths(arr: Array[Int], target: Int): Int = {
        val n = arr.length
        val INF = Int.MaxValue / 2
        val bestEnd = Array.fill(n)(INF)
        val bestStart = Array.fill(n)(INF)

        var left = 0
        var sum: Long = 0L
        val t = target.toLong

        for (right <- 0 until n) {
            sum += arr(right).toLong
            while (sum > t && left <= right) {
                sum -= arr(left).toLong
                left += 1
            }
            if (sum == t) {
                val len = right - left + 1
                if (len < bestEnd(right)) bestEnd(right) = len
                if (len < bestStart(left)) bestStart(left) = len
            }
        }

        val prefix = Array.fill(n)(INF)
        var cur = INF
        for (i <- 0 until n) {
            if (bestEnd(i) < cur) cur = bestEnd(i)
            prefix(i) = cur
        }

        val suffix = Array.fill(n)(INF)
        cur = INF
        for (i <- (n - 1) to 0 by -1) {
            if (bestStart(i) < cur) cur = bestStart(i)
            suffix(i) = cur
        }

        var ans = INF
        for (i <- 0 until n - 1) {
            val leftLen = prefix(i)
            val rightLen = suffix(i + 1)
            if (leftLen < INF && rightLen < INF) {
                val total = leftLen + rightLen
                if (total < ans) ans = total
            }
        }

        if (ans == INF) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_sum_of_lengths(arr: Vec<i32>, target: i32) -> i32 {
        let n = arr.len();
        if n < 2 {
            return -1;
        }
        const INF_USIZE: usize = usize::MAX / 4;

        let mut best_end = vec![INF_USIZE; n];
        let mut best_start = vec![INF_USIZE; n];

        let mut sum: i64 = 0;
        let mut left: usize = 0;
        for right in 0..n {
            sum += arr[right] as i64;
            while left <= right && sum > target as i64 {
                sum -= arr[left] as i64;
                left += 1;
            }
            if sum == target as i64 {
                let len = right - left + 1;
                if len < best_end[right] {
                    best_end[right] = len;
                }
                if len < best_start[left] {
                    best_start[left] = len;
                }
            }
        }

        // prefix minimum lengths ending at or before i
        let mut prefix = vec![INF_USIZE; n];
        for i in 0..n {
            if i == 0 {
                prefix[i] = best_end[i];
            } else {
                prefix[i] = std::cmp::min(prefix[i - 1], best_end[i]);
            }
        }

        // suffix minimum lengths starting at or after i
        let mut suffix = vec![INF_USIZE; n];
        for i in (0..n).rev() {
            if i == n - 1 {
                suffix[i] = best_start[i];
            } else {
                suffix[i] = std::cmp::min(suffix[i + 1], best_start[i]);
            }
        }

        let mut answer = INF_USIZE;
        for i in 0..n - 1 {
            if prefix[i] != INF_USIZE && suffix[i + 1] != INF_USIZE {
                answer = std::cmp::min(answer, prefix[i] + suffix[i + 1]);
            }
        }

        if answer == INF_USIZE {
            -1
        } else {
            answer as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-sum-of-lengths arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector arr)]
         [n (vector-length v)]
         [INF 1000000000])
    (if (< n 2)
        -1
        (begin
          ;; best length of subarray ending at each index
          (define best-end (make-vector n INF))
          (let loop ((r 0) (l 0) (sum 0))
            (when (< r n)
              (set! sum (+ sum (vector-ref v r)))
              (let shrink ((l l) (sum sum))
                (if (and (> sum target) (<= l r))
                    (shrink (+ l 1) (- sum (vector-ref v l)))
                    (begin
                      (when (= sum target)
                        (let ([len (+ 1 (- r l))])
                          (when (< len (vector-ref best-end r))
                            (vector-set! best-end r len))))
                      (loop (+ r 1) l sum)))))
          ;; prefix minima
          (define pref (make-vector n INF))
          (for ([i (in-range n)])
            (let ([cur (vector-ref best-end i)])
              (if (= i 0)
                  (vector-set! pref i cur)
                  (let ([prev (vector-ref pref (- i 1))])
                    (vector-set! pref i (min prev cur))))))
          ;; best length of subarray starting at each index
          (define best-start (make-vector n INF))
          (let loop ((l (sub1 n)) (r (sub1 n)) (sum 0))
            (when (>= l 0)
              (set! sum (+ sum (vector-ref v l)))
              (let shrink ((r r) (sum sum))
                (if (and (> sum target) (>= r l))
                    (shrink (- r 1) (- sum (vector-ref v r)))
                    (begin
                      (when (= sum target)
                        (let ([len (+ 1 (- r l))])
                          (when (< len (vector-ref best-start l))
                            (vector-set! best-start l len))))
                      (loop (- l 1) r sum)))))
          ;; suffix minima
          (define suff (make-vector n INF))
          (for ([i (in-range (sub1 n) -1 -1)])
            (let ([cur (vector-ref best-start i)])
              (if (= i (sub1 n))
                  (vector-set! suff i cur)
                  (let ([next (vector-ref suff (+ i 1))])
                    (vector-set! suff i (min next cur))))))
          ;; combine
          (define ans INF)
          (for ([i (in-range (sub1 n))]) ; split between i and i+1
            (let ([left (vector-ref pref i)]
                  [right (vector-ref suff (+ i 1))])
              (when (and (< left INF) (< right INF))
                (set! ans (min ans (+ left right))))))
          (if (= ans INF) -1 ans))))))
```

## Erlang

```erlang
-module(solution).
-export([min_sum_of_lengths/2]).

-define(INF, 1073741824). % large enough (2^30)

min_sum_of_lengths(Arr, Target) ->
    N = length(Arr),
    case N < 2 of
        true -> -1;
        false ->
            ValArray = array:from_list(Arr),
            EndLen = array:new(N, {default, ?INF}),
            StartLen = array:new(N, {default, ?INF}),
            {EndLen1, StartLen1} = find_subarrays(ValArray, N, Target, 0, 0, EndLen, StartLen),
            PrefixMin = build_prefix_min(EndLen1, N),
            SuffixMin = build_suffix_min(StartLen1, N),
            Best = compute_best(PrefixMin, SuffixMin, N),
            case Best of
                ?INF -> -1;
                _ -> Best
            end
    end.

find_subarrays(_ValArray, N, _Target, R, _L, EndLen, StartLen) when R >= N ->
    {EndLen, StartLen};
find_subarrays(ValArray, N, Target, R, L, EndLen, StartLen) ->
    ValR = array:get(R, ValArray),
    Sum0 = get_sum(R, L, ValArray), % placeholder not used
    % We'll maintain sum via recursion parameters to avoid recomputation.
    {NewL, NewSum, UpdatedEnd, UpdatedStart} =
        slide_window(ValArray, Target, R, L, 0, EndLen, StartLen),
    find_subarrays(ValArray, N, Target, R + 1, NewL, UpdatedEnd, UpdatedStart).

% To avoid recomputing sum each call, we use an accumulator approach.
% However Erlang recursion makes it easier to pass current sum.
% We'll rewrite with accumulator.

find_subarrays(ValArray, N, Target) ->
    find_subarrays(ValArray, N, Target, 0, 0, 0, 
        array:new(N, {default, ?INF}), 
        array:new(N, {default, ?INF})).

find_subarrays(_ValArray, N, _Target, R, _L, _Sum, EndLen, StartLen) when R >= N ->
    {EndLen, StartLen};
find_subarrays(ValArray, N, Target, R, L, Sum, EndLen, StartLen) ->
    ValR = array:get(R, ValArray),
    Sum1 = Sum + ValR,
    {L2, Sum2} = shrink(L, Sum1, Target, ValArray, R),
    % after shrinking, check for target sum
    case Sum2 == Target of
        true ->
            Len = R - L2 + 1,
            PrevEnd = array:get(R, EndLen),
            NewEnd = if Len < PrevEnd -> Len; true -> PrevEnd end,
            UpdatedEnd = array:set(R, NewEnd, EndLen),
            PrevStart = array:get(L2, StartLen),
            NewStart = if Len < PrevStart -> Len; true -> PrevStart end,
            UpdatedStart = array:set(L2, NewStart, StartLen);
        false ->
            UpdatedEnd = EndLen,
            UpdatedStart = StartLen
    end,
    find_subarrays(ValArray, N, Target, R + 1, L2, Sum2, UpdatedEnd, UpdatedStart).

shrink(L, Sum, Target, ValArray, R) when Sum > Target, L =< R ->
    ValL = array:get(L, ValArray),
    shrink(L + 1, Sum - ValL, Target, ValArray, R);
shrink(L, Sum, _Target, _ValArray, _R) ->
    {L, Sum}.

build_prefix_min(EndLen, N) ->
    build_prefix_min(0, ?INF, EndLen, array:new(N, {default, ?INF}), N).

build_prefix_min(I, PrevMin, EndLen, Acc, N) when I >= N ->
    Acc;
build_prefix_min(I, PrevMin, EndLen, Acc, N) ->
    Curr = array:get(I, EndLen),
    Min = if Curr < PrevMin -> Curr; true -> PrevMin end,
    NewAcc = array:set(I, Min, Acc),
    build_prefix_min(I + 1, Min, EndLen, NewAcc, N).

build_suffix_min(StartLen, N) ->
    build_suffix_min(N - 1, ?INF, StartLen, array:new(N, {default, ?INF}), N).

build_suffix_min(I, NextMin, StartLen, Acc, N) when I < 0 ->
    Acc;
build_suffix_min(I, NextMin, StartLen, Acc, N) ->
    Curr = array:get(I, StartLen),
    Min = if Curr < NextMin -> Curr; true -> NextMin end,
    NewAcc = array:set(I, Min, Acc),
    build_suffix_min(I - 1, Min, StartLen, NewAcc, N).

compute_best(PrefixMin, SuffixMin, N) ->
    compute_best(0, ?INF, PrefixMin, SuffixMin, N).

compute_best(I, Best, _PrefixMin, _SuffixMin, N) when I >= N - 1 ->
    Best;
compute_best(I, Best, PrefixMin, SuffixMin, N) ->
    Left = array:get(I, PrefixMin),
    Right = array:get(I + 1, SuffixMin),
    NewBest = if Left < ?INF, Right < ?INF, (Left + Right) < Best -> Left + Right;
                 true -> Best end,
    compute_best(I + 1, NewBest, PrefixMin, SuffixMin, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_sum_of_lengths(arr :: [integer], target :: integer) :: integer
  def min_sum_of_lengths(arr, target) do
    n = length(arr)
    inf = 1_000_000_0

    dp = :array.new(n, default: inf)

    {_, _, ans, _} =
      Enum.with_index(arr)
      |> Enum.reduce({dp, 0, 0, inf}, fn {val, right}, {dp_acc, left, sum, best_ans} ->
        sum = sum + val

        {left, sum} =
          if sum > target do
            shrink(left, sum, arr, target, right)
          else
            {left, sum}
          end

        prev_best = if right == 0, do: inf, else: :array.get(right - 1, dp_acc)

        if sum == target do
          len = right - left + 1

          best_ans =
            if left > 0 do
              left_best = :array.get(left - 1, dp_acc)
              if left_best != inf, do: min(best_ans, left_best + len), else: best_ans
            else
              best_ans
            end

          cur_best = min(prev_best, len)
          dp_new = :array.set(right, cur_best, dp_acc)
          {dp_new, left, sum, best_ans}
        else
          dp_new = :array.set(right, prev_best, dp_acc)
          {dp_new, left, sum, best_ans}
        end
      end)

    if ans == inf, do: -1, else: ans
  end

  defp shrink(left, sum, arr, target, right) do
    if sum > target && left <= right do
      shrink(left + 1, sum - Enum.at(arr, left), arr, target, right)
    else
      {left, sum}
    end
  end
end
```
