# 0689. Maximum Sum of 3 Non-Overlapping Subarrays

## Cpp

```cpp
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int m = n - k + 1; // number of possible windows
        vector<long long> window(m);
        long long cur = 0;
        for (int i = 0; i < k; ++i) cur += nums[i];
        window[0] = cur;
        for (int i = 1; i < m; ++i) {
            cur += nums[i + k - 1] - nums[i - 1];
            window[i] = cur;
        }
        
        vector<int> left(m), right(m);
        // best index on the left up to i
        left[0] = 0;
        for (int i = 1; i < m; ++i) {
            if (window[i] > window[left[i - 1]]) left[i] = i;
            else left[i] = left[i - 1];
        }
        // best index on the right from i
        right[m - 1] = m - 1;
        for (int i = m - 2; i >= 0; --i) {
            if (window[i] >= window[right[i + 1]]) right[i] = i;
            else right[i] = right[i + 1];
        }
        
        long long bestSum = -1;
        vector<int> ans(3);
        for (int mid = k; mid <= m - k - 1; ++mid) {
            int l = left[mid - k];
            int r = right[mid + k];
            long long total = window[l] + window[mid] + window[r];
            if (total > bestSum) {
                bestSum = total;
                ans[0] = l;
                ans[1] = mid;
                ans[2] = r;
            } else if (total == bestSum) {
                // compare lexicographically
                if (l < ans[0] || (l == ans[0] && (mid < ans[1] || (mid == ans[1] && r < ans[2])))) {
                    ans[0] = l;
                    ans[1] = mid;
                    ans[2] = r;
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
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        // helper to get sum of subarray starting at i with length k
        java.util.function.IntUnaryOperator sum = i -> prefix[i + k] - prefix[i];

        int limit = n - k; // last start index for a window

        int[] left = new int[limit];
        int bestIdx = 0;
        for (int i = 0; i < limit; ++i) {
            if (sum.applyAsInt(i) > sum.applyAsInt(bestIdx)) {
                bestIdx = i;
            }
            left[i] = bestIdx;
        }

        int[] right = new int[limit];
        bestIdx = limit - 1;
        for (int i = limit - 1; i >= 0; --i) {
            if (sum.applyAsInt(i) >= sum.applyAsInt(bestIdx)) {
                bestIdx = i;
            }
            right[i] = bestIdx;
        }

        int[] ans = new int[3];
        int maxTotal = -1;

        for (int m = k; m <= n - 2 * k; ++m) {
            int l = left[m - k];
            int r = right[m + k];
            int total = sum.applyAsInt(l) + sum.applyAsInt(m) + sum.applyAsInt(r);
            if (total > maxTotal) {
                maxTotal = total;
                ans[0] = l;
                ans[1] = m;
                ans[2] = r;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        w_len = n - k + 1
        window_sum = [0] * w_len
        for i in range(w_len):
            window_sum[i] = pref[i + k] - pref[i]

        # left best index up to i
        left = [0] * w_len
        best_idx = 0
        for i in range(w_len):
            if window_sum[i] > window_sum[best_idx]:
                best_idx = i
            left[i] = best_idx

        # right best index from i to end
        right = [0] * w_len
        best_idx = w_len - 1
        for i in range(w_len - 1, -1, -1):
            if window_sum[i] >= window_sum[best_idx]:
                best_idx = i
            right[i] = best_idx

        max_total = -1
        ans = [0, 0, 0]
        # middle interval start index m
        for m in range(k, n - 2 * k + 1):
            l = left[m - k]
            r = right[m + k]
            total = window_sum[l] + window_sum[m] + window_sum[r]
            if total > max_total:
                max_total = total
                ans = [l, m, r]

        return ans
```

## Python3

```python
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # prefix sums
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        # window sums of length k
        w_len = n - k + 1
        w = [0] * w_len
        for i in range(w_len):
            w[i] = pre[i + k] - pre[i]

        # left best indices
        left = [0] * w_len
        best_idx = 0
        for i in range(w_len):
            if w[i] > w[best_idx]:
                best_idx = i
            left[i] = best_idx

        # right best indices
        right = [0] * w_len
        best_idx = w_len - 1
        for i in range(w_len - 1, -1, -1):
            if w[i] >= w[best_idx]:
                best_idx = i
            right[i] = best_idx

        max_total = -1
        ans = [0, 0, 0]
        # middle window start index
        for m in range(k, n - 2 * k + 1):
            l = left[m - k]
            r = right[m + k]
            total = w[l] + w[m] + w[r]
            if total > max_total:
                max_total = total
                ans = [l, m, r]

        return ans
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSumOfThreeSubarrays(int* nums, int numsSize, int k, int* returnSize){
    int n = numsSize;
    // prefix sums
    long long *pre = (long long*)malloc((n + 1) * sizeof(long long));
    pre[0] = 0;
    for (int i = 0; i < n; ++i)
        pre[i + 1] = pre[i] + nums[i];
    
    int limit = n - k + 1;               // number of possible windows
    int *left = (int*)malloc(limit * sizeof(int));
    int *right = (int*)malloc(limit * sizeof(int));
    
    // helper to get sum of window starting at i
    #define WIN_SUM(i) (pre[(i) + k] - pre[i])
    
    // left best indices
    int bestIdx = 0;
    left[0] = 0;
    for (int i = 1; i < limit; ++i){
        if (WIN_SUM(i) > WIN_SUM(bestIdx))
            bestIdx = i;
        left[i] = bestIdx;
    }
    
    // right best indices
    bestIdx = limit - 1;
    right[limit - 1] = bestIdx;
    for (int i = limit - 2; i >= 0; --i){
        if (WIN_SUM(i) >= WIN_SUM(bestIdx))
            bestIdx = i;
        right[i] = bestIdx;
    }
    
    long long maxTotal = -1;
    int ans0 = 0, ans1 = k, ans2 = 2 * k;
    
    for (int mid = k; mid <= n - 2 * k; ++mid){
        int l = left[mid - k];
        int r = right[mid + k];
        long long total = WIN_SUM(l) + WIN_SUM(mid) + WIN_SUM(r);
        if (total > maxTotal){
            maxTotal = total;
            ans0 = l;
            ans1 = mid;
            ans2 = r;
        }
    }
    
    free(pre);
    free(left);
    free(right);
    
    int *res = (int*)malloc(3 * sizeof(int));
    res[0] = ans0;
    res[1] = ans1;
    res[2] = ans2;
    *returnSize = 3;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MaxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.Length;
        int m = n - k + 1; // number of possible windows
        int[] windowSums = new int[m];
        
        // Compute sums of all windows of size k
        int sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        windowSums[0] = sum;
        for (int i = 1; i < m; i++) {
            sum += nums[i + k - 1] - nums[i - 1];
            windowSums[i] = sum;
        }
        
        // left[i]: best start index for a window in [0..i]
        int[] left = new int[m];
        left[0] = 0;
        for (int i = 1; i < m; i++) {
            if (windowSums[i] > windowSums[left[i - 1]]) {
                left[i] = i;
            } else {
                left[i] = left[i - 1];
            }
        }
        
        // right[i]: best start index for a window in [i..m-1]
        int[] right = new int[m];
        right[m - 1] = m - 1;
        for (int i = m - 2; i >= 0; i--) {
            if (windowSums[i] >= windowSums[right[i + 1]]) {
                right[i] = i;
            } else {
                right[i] = right[i + 1];
            }
        }
        
        int maxTotal = -1;
        int[] answer = new int[3];
        // middle window starts at mid
        for (int mid = k; mid <= n - 2 * k; mid++) {
            int lIdx = left[mid - k];
            int rIdx = right[mid + k];
            int total = windowSums[lIdx] + windowSums[mid] + windowSums[rIdx];
            if (total > maxTotal) {
                maxTotal = total;
                answer[0] = lIdx;
                answer[1] = mid;
                answer[2] = rIdx;
            }
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function(nums, k) {
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];

    const windowCount = n - k + 1;
    const sum = (i) => pref[i + k] - pref[i]; // sum of subarray starting at i

    // left[i]: best start index for a window in [0..i]
    const left = new Array(windowCount);
    let bestIdx = 0, bestSum = sum(0);
    left[0] = 0;
    for (let i = 1; i < windowCount; ++i) {
        const cur = sum(i);
        if (cur > bestSum) {
            bestSum = cur;
            bestIdx = i;
        }
        // keep earlier index when equal to ensure lexicographically smallest
        left[i] = bestIdx;
    }

    // right[i]: best start index for a window in [i..windowCount-1]
    const right = new Array(windowCount);
    bestIdx = windowCount - 1;
    bestSum = sum(bestIdx);
    right[bestIdx] = bestIdx;
    for (let i = windowCount - 2; i >= 0; --i) {
        const cur = sum(i);
        if (cur >= bestSum) { // >= to prefer earlier index on tie when scanning from left
            bestSum = cur;
            bestIdx = i;
        }
        right[i] = bestIdx;
    }

    let maxTotal = -1;
    const ans = [0, 0, 0];
    for (let m = k; m <= n - 2 * k; ++m) {
        const l = left[m - k];
        const r = right[m + k];
        const total = sum(l) + sum(m) + sum(r);
        if (total > maxTotal) {
            maxTotal = total;
            ans[0] = l;
            ans[1] = m;
            ans[2] = r;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxSumOfThreeSubarrays(nums: number[], k: number): number[] {
    const n = nums.length;
    const m = n - k + 1; // number of possible windows
    const windowSums = new Array(m).fill(0);
    // compute sums of all windows of size k
    let sum = 0;
    for (let i = 0; i < n; ++i) {
        sum += nums[i];
        if (i >= k) sum -= nums[i - k];
        if (i >= k - 1) windowSums[i - k + 1] = sum;
    }

    // left[i]: best window start index in [0..i]
    const left = new Array(m).fill(0);
    for (let i = 0; i < m; ++i) {
        if (i === 0) {
            left[i] = 0;
        } else {
            left[i] = windowSums[i] > windowSums[left[i - 1]] ? i : left[i - 1];
        }
    }

    // right[i]: best window start index in [i..m-1]
    const right = new Array(m).fill(0);
    for (let i = m - 1; i >= 0; --i) {
        if (i === m - 1) {
            right[i] = i;
        } else {
            // use >= to prefer earlier index when sums are equal
            right[i] = windowSums[i] >= windowSums[right[i + 1]] ? i : right[i + 1];
        }
    }

    let maxTotal = -Infinity;
    const answer = [0, 0, 0];

    // middle window start j must allow space for left and right windows
    for (let j = k; j <= m - k - 1; ++j) {
        const i = left[j - k];
        const l = right[j + k];
        const total = windowSums[i] + windowSums[j] + windowSums[l];
        if (total > maxTotal) {
            maxTotal = total;
            answer[0] = i;
            answer[1] = j;
            answer[2] = l;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSumOfThreeSubarrays($nums, $k) {
        $n = count($nums);
        // prefix sums
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }

        // left best start index up to each position
        $left = array_fill(0, $n, 0);
        $bestSum = $prefix[$k] - $prefix[0];
        $bestIdx = 0;
        for ($i = $k - 1; $i < $n; ++$i) {
            $currStart = $i - $k + 1;
            $currSum = $prefix[$i + 1] - $prefix[$currStart];
            if ($currSum > $bestSum) {
                $bestSum = $currSum;
                $bestIdx = $currStart;
            }
            $left[$i] = $bestIdx;
        }

        // right best start index from each position to the end
        $right = array_fill(0, $n, 0);
        $bestSum = $prefix[$n] - $prefix[$n - $k];
        $bestIdx = $n - $k;
        for ($i = $n - $k; $i >= 0; --$i) {
            $currSum = $prefix[$i + $k] - $prefix[$i];
            if ($currSum >= $bestSum) { // >= to keep earlier index on ties
                $bestSum = $currSum;
                $bestIdx = $i;
            }
            $right[$i] = $bestIdx;
        }

        $maxTotal = -1;
        $answer = [0, 0, 0];
        for ($mid = $k; $mid <= $n - 2 * $k; ++$mid) {
            $l = $left[$mid - 1];
            $r = $right[$mid + $k];
            $total = ($prefix[$l + $k] - $prefix[$l]) +
                     ($prefix[$mid + $k] - $prefix[$mid]) +
                     ($prefix[$r + $k] - $prefix[$r]);
            if ($total > $maxTotal) {
                $maxTotal = $total;
                $answer = [$l, $mid, $r];
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumOfThreeSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        let m = n - k + 1   // number of possible windows
        
        // Prefix sums
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + nums[i]
        }
        
        // Sum of each window of length k
        var windowSum = [Int](repeating: 0, count: m)
        for i in 0..<m {
            windowSum[i] = prefix[i + k] - prefix[i]
        }
        
        // leftBest[i]: start index of the best window in [0..i]
        var leftBest = [Int](repeating: 0, count: m)
        var bestIdx = 0
        for i in 0..<m {
            if windowSum[i] > windowSum[bestIdx] {
                bestIdx = i
            }
            leftBest[i] = bestIdx
        }
        
        // rightBest[i]: start index of the best window in [i..m-1]
        var rightBest = [Int](repeating: 0, count: m)
        bestIdx = m - 1
        for i in stride(from: m - 1, through: 0, by: -1) {
            if windowSum[i] >= windowSum[bestIdx] { // >= to keep earlier index on tie
                bestIdx = i
            }
            rightBest[i] = bestIdx
        }
        
        var maxTotal = -1
        var answer = [0, 0, 0]
        
        // middle window start j must allow space for left and right windows
        if m >= 3 * k {
            for j in k..<(m - k) {
                let i = leftBest[j - k]      // best left window before j
                let l = rightBest[j + k]     // best right window after j
                let total = windowSum[i] + windowSum[j] + windowSum[l]
                if total > maxTotal {
                    maxTotal = total
                    answer[0] = i
                    answer[1] = j
                    answer[2] = l
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumOfThreeSubarrays(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val m = n - k + 1 // number of possible windows
        val windowSums = IntArray(m)
        var sum = 0
        for (i in 0 until k) sum += nums[i]
        windowSums[0] = sum
        for (i in 1 until m) {
            sum += nums[i + k - 1] - nums[i - 1]
            windowSums[i] = sum
        }

        // left[i]: best start index for a window in [0..i]
        val left = IntArray(m)
        var bestIdx = 0
        for (i in 0 until m) {
            if (windowSums[i] > windowSums[bestIdx]) bestIdx = i
            // keep earlier index when equal, so no change
            left[i] = bestIdx
        }

        // right[i]: best start index for a window in [i..m-1]
        val right = IntArray(m)
        bestIdx = m - 1
        for (i in m - 1 downTo 0) {
            if (windowSums[i] >= windowSums[bestIdx]) bestIdx = i // >= to favor earlier index on ties
            right[i] = bestIdx
        }

        var maxTotal = -1
        val answer = IntArray(3)
        for (mid in k..n - 2 * k) {
            val l = left[mid - k]
            val r = right[mid + k]
            val total = windowSums[l] + windowSums[mid] + windowSums[r]
            if (total > maxTotal) {
                maxTotal = total
                answer[0] = l
                answer[1] = mid
                answer[2] = r
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxSumOfThreeSubarrays(List<int> nums, int k) {
    int n = nums.length;
    int m = n - k + 1; // number of possible windows
    List<int> windowSums = List.filled(m, 0);
    int sum = 0;
    for (int i = 0; i < k; i++) sum += nums[i];
    windowSums[0] = sum;
    for (int i = 1; i < m; i++) {
      sum += nums[i + k - 1] - nums[i - 1];
      windowSums[i] = sum;
    }

    List<int> left = List.filled(m, 0);
    left[0] = 0;
    for (int i = 1; i < m; i++) {
      if (windowSums[i] > windowSums[left[i - 1]]) {
        left[i] = i;
      } else {
        left[i] = left[i - 1];
      }
    }

    List<int> right = List.filled(m, 0);
    right[m - 1] = m - 1;
    for (int i = m - 2; i >= 0; i--) {
      if (windowSums[i] >= windowSums[right[i + 1]]) {
        right[i] = i;
      } else {
        right[i] = right[i + 1];
      }
    }

    int maxTotal = -1;
    List<int> ans = [0, k, 2 * k];
    for (int j = k; j <= m - k - 1; j++) {
      int iIdx = left[j - k];
      int rIdx = right[j + k];
      int total = windowSums[iIdx] + windowSums[j] + windowSums[rIdx];
      if (total > maxTotal) {
        maxTotal = total;
        ans = [iIdx, j, rIdx];
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxSumOfThreeSubarrays(nums []int, k int) []int {
    n := len(nums)
    // prefix sums
    pre := make([]int, n+1)
    for i := 0; i < n; i++ {
        pre[i+1] = pre[i] + nums[i]
    }

    // sums of all windows of length k
    m := n - k + 1
    w := make([]int, m)
    for i := 0; i < m; i++ {
        w[i] = pre[i+k] - pre[i]
    }

    // left[i]: best window index in [0..i]
    left := make([]int, m)
    bestIdx := 0
    for i := 0; i < m; i++ {
        if w[i] > w[bestIdx] {
            bestIdx = i
        }
        left[i] = bestIdx
    }

    // right[i]: best window index in [i..m-1]
    right := make([]int, m)
    bestIdx = m - 1
    for i := m - 1; i >= 0; i-- {
        if w[i] >= w[bestIdx] { // >= to keep lexicographically smallest
            bestIdx = i
        }
        right[i] = bestIdx
    }

    ans := []int{0, 0, 0}
    maxSum := -1

    // middle window start index ranges from k to n-2k inclusive
    for mid := k; mid <= n-2*k; mid++ {
        l := left[mid-k]
        r := right[mid+k]
        total := w[l] + w[mid] + w[r]
        if total > maxSum {
            maxSum = total
            ans[0], ans[1], ans[2] = l, mid, r
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_sum_of_three_subarrays(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }

  m = n - k + 1
  w = Array.new(m, 0)
  (0...m).each { |i| w[i] = pref[i + k] - pref[i] }

  left_best = Array.new(m, 0)
  best_idx = 0
  (0...m).each do |i|
    best_idx = i if w[i] > w[best_idx]
    left_best[i] = best_idx
  end

  right_best = Array.new(m, 0)
  best_idx = m - 1
  (m - 1).downto(0) do |i|
    best_idx = i if w[i] >= w[best_idx]
    right_best[i] = best_idx
  end

  max_total = -1
  ans = [0, k, 2 * k]

  (k..(n - 2 * k)).each do |mid|
    left = left_best[mid - k]
    right = right_best[mid + k]
    total = w[left] + w[mid] + w[right]
    if total > max_total
      max_total = total
      ans = [left, mid, right]
    elsif total == max_total
      cand = [left, mid, right]
      ans = cand if cand < ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxSumOfThreeSubarrays(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        // prefix sums for O(1) window sum queries
        val pref = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = pref(i) + nums(i).toLong
            i += 1
        }

        // sums of all windows of length k
        val wCount = n - k + 1
        val winSum = new Array[Long](wCount)
        i = 0
        while (i < wCount) {
            winSum(i) = pref(i + k) - pref(i)
            i += 1
        }

        // left best indices
        val leftIdx = new Array[Int](wCount)
        var bestLeft = 0
        var maxLeft = winSum(0)
        leftIdx(0) = 0
        i = 1
        while (i < wCount) {
            if (winSum(i) > maxLeft) {
                maxLeft = winSum(i)
                bestLeft = i
            }
            // keep earlier index on tie
            leftIdx(i) = bestLeft
            i += 1
        }

        // right best indices
        val rightIdx = new Array[Int](wCount)
        var bestRight = wCount - 1
        var maxRight = winSum(bestRight)
        rightIdx(bestRight) = bestRight
        i = wCount - 2
        while (i >= 0) {
            if (winSum(i) >= maxRight) { // >= to prefer smaller index on tie
                maxRight = winSum(i)
                bestRight = i
            }
            rightIdx(i) = bestRight
            i -= 1
        }

        var ans = Array(0, 0, 0)
        var maxTotal: Long = -1L
        var m = k
        while (m <= n - 2 * k) {
            val l = leftIdx(m - k)
            val r = rightIdx(m + k)
            val total = winSum(l) + winSum(m) + winSum(r)
            if (total > maxTotal) {
                maxTotal = total
                ans(0) = l
                ans(1) = m
                ans(2) = r
            }
            m += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_of_three_subarrays(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let m = n - k + 1; // number of possible windows

        // prefix sums
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }

        // sum of each window of length k
        let mut sums = vec![0i64; m];
        for i in 0..m {
            sums[i] = pref[i + k] - pref[i];
        }

        // left best indices
        let mut left = vec![0usize; m];
        left[0] = 0;
        for i in 1..m {
            if sums[i] > sums[left[i - 1]] {
                left[i] = i;
            } else {
                left[i] = left[i - 1];
            }
        }

        // right best indices
        let mut right = vec![0usize; m];
        right[m - 1] = m - 1;
        for i in (0..m - 1).rev() {
            if sums[i] >= sums[right[i + 1]] {
                right[i] = i;
            } else {
                right[i] = right[i + 1];
            }
        }

        let mut best_total = -1i64;
        let mut ans = [0usize; 3];

        // middle window start j
        for j in k..=m - k - 1 {
            let i_idx = left[j - k];
            let l_idx = right[j + k];
            let total = sums[i_idx] + sums[j] + sums[l_idx];
            if total > best_total {
                best_total = total;
                ans = [i_idx, j, l_idx];
            } else if total == best_total {
                let cand = (i_idx, j, l_idx);
                let cur = (ans[0], ans[1], ans[2]);
                if cand < cur {
                    ans = [i_idx, j, l_idx];
                }
            }
        }

        ans.iter().map(|&x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (max-sum-of-three-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([nums-vec (list->vector nums)]
         [n (vector-length nums-vec)])
    ;; prefix sums
    (let ([pref (make-vector (+ n 1) 0)])
      (for ([i (in-range n)])
        (vector-set! pref (add1 i)
                     (+ (vector-ref pref i) (vector-ref nums-vec i))))
      ;; window sums of length k
      (let* ([sum-len (- n k) ; last start index = n-k
             [sum-len (add1 sum-len)] ; number of windows
             [sums (make-vector sum-len 0)])
        (for ([i (in-range sum-len)])
          (vector-set! sums i
                       (- (vector-ref pref (+ i k))
                          (vector-ref pref i))))
        ;; best left indices
        (let ([left (make-vector sum-len 0)])
          (vector-set! left 0 0)
          (for ([i (in-range 1 sum-len)])
            (let* ([prev (vector-ref left (sub1 i))]
                   [prev-sum (vector-ref sums prev)]
                   [curr-sum (vector-ref sums i)])
              (if (> curr-sum prev-sum)
                  (vector-set! left i i)
                  (vector-set! left i prev))))
          ;; best right indices
          (let ([right (make-vector sum-len 0)])
            (vector-set! right (sub1 sum-len) (sub1 sum-len))
            (for ([i (in-range (- sum-len 2) -1 -1)]) ; descending
              (let* ([next (vector-ref right (add1 i))]
                     [next-sum (vector-ref sums next)]
                     [curr-sum (vector-ref sums i)])
                (if (>= curr-sum next-sum)
                    (vector-set! right i i)
                    (vector-set! right i next))))
            ;; iterate middle window
            (let ([best-total -1]
                  [ans (list 0 0 0)])
              (for ([mid (in-range k (add1 (- n (* 2 k))))])
                (let* ([left-idx (vector-ref left (- mid k))]
                       [right-idx (vector-ref right (+ mid k))]
                       [total (+ (vector-ref sums left-idx)
                                 (vector-ref sums mid)
                                 (vector-ref sums right-idx))])
                  (when (> total best-total)
                    (set! best-total total)
                    (set! ans (list left-idx mid right-idx)))))
              ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum_of_three_subarrays/2]).
-spec max_sum_of_three_subarrays(Nums :: [integer()], K :: integer()) -> [integer()].
max_sum_of_three_subarrays(Nums, K) ->
    N = length(Nums),
    Prefix = prefix_sums(Nums),
    WindowSums = window_sums(Prefix, N, K),
    M = N - K + 1,
    LeftBest = left_best(WindowSums, M),
    RightBest = right_best(WindowSums, M),
    MinMid = K,
    MaxMid = N - 2 * K,
    {_, Answer} = middle_loop(MinMid, MaxMid, WindowSums, LeftBest, RightBest, -1, []),
    Answer.

%% Prefix sums tuple of length N+1, element(Index+1) is sum of first Index elements
prefix_sums(Nums) ->
    {_, RevList} = lists:foldl(
        fun(X, {Acc, List}) ->
            New = Acc + X,
            {New, [New | List]}
        end,
        {0, []},
        Nums),
    PrefixRev = [0 | RevList],
    PrefixList = lists:reverse(PrefixRev),
    list_to_tuple(PrefixList).

%% Window sums tuple of length M = N-K+1
window_sums(Prefix, N, K) ->
    M = N - K + 1,
    build_window(0, M, Prefix, K, []).

build_window(I, M, _Prefix, _K, Acc) when I == M ->
    list_to_tuple(lists:reverse(Acc));
build_window(I, M, Prefix, K, Acc) ->
    Sum = element(I + K + 1, Prefix) - element(I + 1, Prefix),
    build_window(I + 1, M, Prefix, K, [Sum | Acc]).

%% LeftBest[i] = index of max window sum in [0..i]
left_best(WS, M) ->
    left_best_loop(0, M - 1, WS, 0, []).

left_best_loop(I, MaxI, _WS, _CurBestIdx, Acc) when I > MaxI ->
    list_to_tuple(lists:reverse(Acc));
left_best_loop(I, MaxI, WS, CurBestIdx, Acc) ->
    CurrSum = element(I + 1, WS),
    BestSum = element(CurBestIdx + 1, WS),
    NewBestIdx = if CurrSum > BestSum -> I; true -> CurBestIdx end,
    left_best_loop(I + 1, MaxI, WS, NewBestIdx, [NewBestIdx | Acc]).

%% RightBest[i] = index of max window sum in [i..M-1]; ties prefer earlier index
right_best(WS, M) ->
    right_best_loop(M - 1, M - 1, WS, []).

right_best_loop(I, _CurBestIdx, _WS, Acc) when I < 0 ->
    list_to_tuple(lists:reverse(Acc));
right_best_loop(I, CurBestIdx, WS, Acc) ->
    CurrSum = element(I + 1, WS),
    BestSum = element(CurBestIdx + 1, WS),
    NewBestIdx = if CurrSum >= BestSum -> I; true -> CurBestIdx end,
    right_best_loop(I - 1, NewBestIdx, WS, [NewBestIdx | Acc]).

%% Iterate middle start index and keep best total
middle_loop(Mid, MaxMid, _WS, _LB, _RB, CurBestTotal, CurAns) when Mid > MaxMid ->
    {CurBestTotal, CurAns};
middle_loop(Mid, MaxMid, WS, LB, RB, CurBestTotal, CurAns) ->
    LeftIdx = element((Mid - K) + 1, LB),
    RightIdx = element((Mid + K) + 1, RB),
    Sum = element(LeftIdx + 1, WS) + element(Mid + 1, WS) + element(RightIdx + 1, WS),
    {NewBestTotal, NewAns} =
        if Sum > CurBestTotal ->
                {Sum, [LeftIdx, Mid, RightIdx]};
           true -> {CurBestTotal, CurAns}
        end,
    middle_loop(Mid + 1, MaxMid, WS, LB, RB, NewBestTotal, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_of_three_subarrays(nums :: [integer], k :: integer) :: [integer]
  def max_sum_of_three_subarrays(nums, k) do
    n = length(nums)
    m = n - k + 1
    num_tup = List.to_tuple(nums)

    # Compute sums of all windows of size k
    first_sum =
      Enum.reduce(0..(k - 1), 0, fn i, acc -> acc + elem(num_tup, i) end)

    {_, rev_sums} =
      Enum.reduce(1..(m - 1), {first_sum, [first_sum]}, fn i, {prev, acc} ->
        new_sum = prev - elem(num_tup, i - 1) + elem(num_tup, i + k - 1)
        {new_sum, [new_sum | acc]}
      end)

    w_list = Enum.reverse(rev_sums)
    w = List.to_tuple(w_list)

    # left[i] = index of max window sum in w[0..i]
    {_, rev_left} =
      Enum.reduce(0..(m - 1), {0, []}, fn i, {best_idx, acc} ->
        best_idx = if elem(w, i) > elem(w, best_idx), do: i, else: best_idx
        {best_idx, [best_idx | acc]}
      end)

    left = List.to_tuple(Enum.reverse(rev_left))

    # right[i] = index of max window sum in w[i..m-1] (choose later index on ties)
    {_, rev_right} =
      Enum.reduce((m - 1)..0, {m - 1, []}, fn i, {best_idx, acc} ->
        best_idx = if elem(w, i) >= elem(w, best_idx), do: i, else: best_idx
        {best_idx, [best_idx | acc]}
      end)

    right = List.to_tuple(Enum.reverse(rev_right))

    # Iterate over middle window start position
    {_, ans} =
      Enum.reduce(k..(m - k - 1), {-1, {0, 0, 0}}, fn j, {best_total, ans} ->
        i_idx = elem(left, j - k)
        l_idx = elem(right, j + k)
        total = elem(w, i_idx) + elem(w, j) + elem(w, l_idx)

        {ans_i, ans_j, ans_l} = ans

        cond do
          total > best_total ->
            {total, {i_idx, j, l_idx}}

          total == best_total ->
            if i_idx < ans_i or (i_idx == ans_i and (j < ans_j or (j == ans_j and l_idx < ans_l))) do
              {best_total, {i_idx, j, l_idx}}
            else
              {best_total, ans}
            end

          true ->
            {best_total, ans}
        end
      end)

    [ans_i, ans_j, ans_l] = Tuple.to_list(ans)
    [ans_i, ans_j, ans_l]
  end
end
```
