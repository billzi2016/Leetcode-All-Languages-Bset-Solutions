# 3578. Count Partitions With Max-Min Difference at Most K

## Cpp

```cpp
class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        const int MOD = 1000000007;
        int n = nums.size();
        vector<long long> dp(n), pref(n);
        deque<int> minD, maxD;
        int l = 0;
        for (int i = 0; i < n; ++i) {
            while (!minD.empty() && nums[i] <= nums[minD.back()]) minD.pop_back();
            minD.push_back(i);
            while (!maxD.empty() && nums[i] >= nums[maxD.back()]) maxD.pop_back();
            maxD.push_back(i);
            while (!minD.empty() && !maxD.empty() && (long long)nums[maxD.front()] - (long long)nums[minD.front()] > k) {
                if (minD.front() == l) minD.pop_front();
                if (maxD.front() == l) maxD.pop_front();
                ++l;
            }
            long long total = 0;
            if (l == 0) {
                total = 1; // dp[-1]
                if (i - 1 >= 0) total = (total + pref[i - 1]) % MOD;
            } else {
                int leftIdx = l - 2;
                long long sub = (leftIdx >= 0 ? pref[leftIdx] : 0);
                total = (pref[i - 1] - sub + MOD) % MOD;
            }
            dp[i] = total;
            pref[i] = ((i > 0 ? pref[i - 1] : 0) + dp[i]) % MOD;
        }
        return (int)dp[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int countPartitions(int[] nums, int k) {
        int n = nums.length;
        final long MOD = 1_000_000_007L;
        long[] dp = new long[n + 1];
        long[] pref = new long[n + 1];
        dp[0] = 1;
        pref[0] = 1;

        java.util.Deque<Integer> maxDeque = new java.util.ArrayDeque<>();
        java.util.Deque<Integer> minDeque = new java.util.ArrayDeque<>();

        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] <= nums[right]) {
                maxDeque.pollLast();
            }
            maxDeque.addLast(right);
            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] >= nums[right]) {
                minDeque.pollLast();
            }
            minDeque.addLast(right);

            while (left <= right &&
                   (long) nums[maxDeque.peekFirst()] - (long) nums[minDeque.peekFirst()] > k) {
                if (maxDeque.peekFirst() == left) maxDeque.pollFirst();
                if (minDeque.peekFirst() == left) minDeque.pollFirst();
                left++;
            }

            int l = left;
            long sum = pref[right];
            if (l > 0) {
                sum = (sum - pref[l - 1]) % MOD;
                if (sum < 0) sum += MOD;
            }
            dp[right + 1] = sum;
            pref[right + 1] = (pref[right] + dp[right + 1]) % MOD;
        }

        return (int) (dp[n] % MOD);
    }
}
```

## Python

```python
import collections

class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        pref = [0] * (n + 1)   # prefix sums of dp
        pref[0] = 1            # dp[0] = 1

        maxdq = collections.deque()
        mindq = collections.deque()
        l = 0
        dp_i = 0

        for i in range(n):
            # add current index to deques
            while maxdq and nums[maxdq[-1]] <= nums[i]:
                maxdq.pop()
            maxdq.append(i)
            while mindq and nums[mindq[-1]] >= nums[i]:
                mindq.pop()
            mindq.append(i)

            # shrink window until condition satisfied
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq[0] == l:
                    maxdq.popleft()
                if mindq[0] == l:
                    mindq.popleft()
                l += 1

            # dp for prefix ending at i (i+1 elements)
            left_sum = pref[l - 1] if l > 0 else 0
            dp_i = (pref[i] - left_sum) % MOD
            pref[i + 1] = (pref[i] + dp_i) % MOD

        return dp_i % MOD
```

## Python3

```python
class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)      # dp[i]: ways for first i elements
        pref = [0] * (n + 1)    # prefix sums of dp
        dp[0] = 1
        pref[0] = 1

        from collections import deque
        maxdq = deque()
        mindq = deque()
        left = 0

        for right in range(n):
            # maintain decreasing max deque
            while maxdq and nums[maxdq[-1]] <= nums[right]:
                maxdq.pop()
            maxdq.append(right)
            # maintain increasing min deque
            while mindq and nums[mindq[-1]] >= nums[right]:
                mindq.pop()
            mindq.append(right)

            # shrink window until condition satisfied
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq[0] == left:
                    maxdq.popleft()
                if mindq[0] == left:
                    mindq.popleft()
                left += 1

            # sum dp[left .. right]
            total = pref[right]
            if left > 0:
                total = (total - pref[left - 1]) % MOD
            dp[right + 1] = total
            pref[right + 1] = (pref[right] + dp[right + 1]) % MOD

        return dp[n] % MOD
```

## C

```c
#include <stdlib.h>

int countPartitions(int* nums, int numsSize, int k) {
    const int MOD = 1000000007;
    int n = numsSize;
    
    long long *dp = (long long*)malloc((n + 1) * sizeof(long long));
    long long *pref = (long long*)malloc((n + 1) * sizeof(long long));
    dp[0] = 1;
    pref[0] = 1;
    
    int *minD = (int*)malloc((n + 5) * sizeof(int));
    int *maxD = (int*)malloc((n + 5) * sizeof(int));
    int minHead = 0, minTail = -1;
    int maxHead = 0, maxTail = -1;
    
    int left = 1; // 1‑based index of window start
    
    for (int i = 1; i <= n; ++i) {
        int val = nums[i - 1];
        
        while (minTail >= minHead && nums[minD[minTail] - 1] >= val) minTail--;
        minD[++minTail] = i;
        
        while (maxTail >= maxHead && nums[maxD[maxTail] - 1] <= val) maxTail--;
        maxD[++maxTail] = i;
        
        while (left <= i) {
            int curMin = nums[minD[minHead] - 1];
            int curMax = nums[maxD[maxHead] - 1];
            if ((long long)curMax - curMin <= k) break;
            if (minD[minHead] == left) ++minHead;
            if (maxD[maxHead] == left) ++maxHead;
            ++left;
        }
        
        long long sum = pref[i - 1];
        if (left > 1) {
            sum -= pref[left - 2];
            if (sum < 0) sum += MOD;
        }
        dp[i] = sum % MOD;
        pref[i] = (pref[i - 1] + dp[i]) % MOD;
    }
    
    int result = (int)(dp[n] % MOD);
    free(dp);
    free(pref);
    free(minD);
    free(maxD);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPartitions(int[] nums, int k) {
        const int MOD = 1000000007;
        int n = nums.Length;
        long[] dp = new long[n + 1];
        long[] pref = new long[n + 1];
        dp[0] = 1;
        pref[0] = 1;

        var maxDeque = new System.Collections.Generic.LinkedList<int>();
        var minDeque = new System.Collections.Generic.LinkedList<int>();
        int left = 0;

        for (int i = 0; i < n; i++) {
            while (maxDeque.Count > 0 && nums[maxDeque.Last.Value] <= nums[i])
                maxDeque.RemoveLast();
            maxDeque.AddLast(i);
            while (minDeque.Count > 0 && nums[minDeque.Last.Value] >= nums[i])
                minDeque.RemoveLast();
            minDeque.AddLast(i);

            while (nums[maxDeque.First.Value] - nums[minDeque.First.Value] > k) {
                if (maxDeque.First.Value == left) maxDeque.RemoveFirst();
                if (minDeque.First.Value == left) minDeque.RemoveFirst();
                left++;
            }

            long sum = pref[i];
            if (left > 0) {
                sum = (sum - pref[left - 1]) % MOD;
                if (sum < 0) sum += MOD;
            }
            dp[i + 1] = sum;
            pref[i + 1] = (pref[i] + dp[i + 1]) % MOD;
        }

        return (int)(dp[n] % MOD);
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
var countPartitions = function(nums, k) {
    const n = nums.length;
    const MOD = 1000000007;

    const dp = new Array(n);
    const pref = new Array(n); // prefix sums of dp

    const minDeque = [];
    const maxDeque = [];
    let minFront = 0, maxFront = 0;
    let left = 0; // current window left bound

    for (let i = 0; i < n; ++i) {
        // maintain monotonic increasing deque for minimum
        while (minDeque.length > minFront && nums[minDeque[minDeque.length - 1]] >= nums[i]) {
            minDeque.pop();
        }
        minDeque.push(i);
        // maintain monotonic decreasing deque for maximum
        while (maxDeque.length > maxFront && nums[maxDeque[maxDeque.length - 1]] <= nums[i]) {
            maxDeque.pop();
        }
        maxDeque.push(i);

        // shrink window until condition satisfied
        while (nums[maxDeque[maxFront]] - nums[minDeque[minFront]] > k) {
            ++left;
            if (minDeque[minFront] < left) ++minFront;
            if (maxDeque[maxFront] < left) ++maxFront;
        }

        let curDp;
        if (left === 0) {
            const prevSum = i > 0 ? pref[i - 1] : 0;
            curDp = (1 + prevSum) % MOD; // include dp[-1] = 1
        } else {
            const leftMinus2 = left - 2;
            const sub = leftMinus2 >= 0 ? pref[leftMinus2] : 0;
            curDp = (pref[i - 1] - sub + MOD) % MOD;
        }

        dp[i] = curDp;
        pref[i] = ((i > 0 ? pref[i - 1] : 0) + curDp) % MOD;
    }

    return dp[n - 1];
};
```

## Typescript

```typescript
function countPartitions(nums: number[], k: number): number {
    const MOD = 1000000007;
    const n = nums.length;
    const dp = new Array(n + 1).fill(0);
    const pref = new Array(n + 1).fill(0);
    dp[0] = 1;
    pref[0] = 1;

    let left = 0;
    const minDeque: number[] = [];
    const maxDeque: number[] = [];
    let minHead = 0, maxHead = 0;

    for (let i = 0; i < n; i++) {
        while (minDeque.length > minHead && nums[minDeque[minDeque.length - 1]] >= nums[i]) {
            minDeque.pop();
        }
        minDeque.push(i);
        while (maxDeque.length > maxHead && nums[maxDeque[maxDeque.length - 1]] <= nums[i]) {
            maxDeque.pop();
        }
        maxDeque.push(i);

        while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > k) {
            if (minDeque[minHead] === left) minHead++;
            if (maxDeque[maxHead] === left) maxHead++;
            left++;
        }

        const total = pref[i];
        const subtract = left > 0 ? pref[left - 1] : 0;
        let val = total - subtract;
        if (val < 0) val += MOD;
        dp[i + 1] = val % MOD;

        pref[i + 1] = (pref[i] + dp[i + 1]) % MOD;
    }

    return dp[n];
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
    function countPartitions($nums, $k) {
        $mod = 1000000007;
        $n = count($nums);
        // dp[i]: ways for first i elements (prefix length i)
        $dp = array_fill(0, $n + 1, 0);
        // pref[i]: sum of dp[0..i-1]
        $pref = array_fill(0, $n + 2, 0);
        $dp[0] = 1;
        $pref[1] = 1;

        $maxDeque = [];
        $minDeque = [];
        $maxFront = 0;
        $minFront = 0;
        $left = 0;

        for ($right = 0; $right < $n; $right++) {
            // maintain decreasing max deque
            while (count($maxDeque) > $maxFront && $nums[$maxDeque[count($maxDeque) - 1]] <= $nums[$right]) {
                array_pop($maxDeque);
            }
            $maxDeque[] = $right;

            // maintain increasing min deque
            while (count($minDeque) > $minFront && $nums[$minDeque[count($minDeque) - 1]] >= $nums[$right]) {
                array_pop($minDeque);
            }
            $minDeque[] = $right;

            // shrink left until window is valid
            while (true) {
                $maxIdx = $maxDeque[$maxFront];
                $minIdx = $minDeque[$minFront];
                if ($nums[$maxIdx] - $nums[$minIdx] <= $k) {
                    break;
                }
                if ($maxIdx == $left) {
                    $maxFront++;
                }
                if ($minIdx == $left) {
                    $minFront++;
                }
                $left++;
            }

            // dp for prefix length right+1
            $sum = $pref[$right + 1] - $pref[$left];
            $sum %= $mod;
            if ($sum < 0) {
                $sum += $mod;
            }
            $dp[$right + 1] = $sum;
            $pref[$right + 2] = ($pref[$right + 1] + $dp[$right + 1]) % $mod;
        }

        return $dp[$n] % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        var dp = Array(repeating: 0, count: n + 1)
        var pref = Array(repeating: 0, count: n + 1)
        dp[0] = 1
        pref[0] = 1
        
        var maxDeque = [Int]()
        var minDeque = [Int]()
        var maxHead = 0
        var minHead = 0
        var left = 0
        
        for r in 0..<n {
            // maintain decreasing deque for maximum
            while let last = maxDeque.last, nums[last] < nums[r] {
                maxDeque.removeLast()
            }
            maxDeque.append(r)
            // maintain increasing deque for minimum
            while let last = minDeque.last, nums[last] > nums[r] {
                minDeque.removeLast()
            }
            minDeque.append(r)
            
            // shrink window until condition satisfied
            while maxHead < maxDeque.count && minHead < minDeque.count &&
                    (nums[maxDeque[maxHead]] - nums[minDeque[minHead]]) > k {
                if maxDeque[maxHead] == left { maxHead += 1 }
                if minDeque[minHead] == left { minHead += 1 }
                left += 1
            }
            
            let i = r + 1
            var sum = pref[i - 1]
            if left > 0 {
                sum -= pref[left - 1]
                sum %= MOD
                if sum < 0 { sum += MOD }
            } else {
                sum %= MOD
            }
            dp[i] = sum
            pref[i] = (pref[i - 1] + dp[i]) % MOD
        }
        
        return dp[n] % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        val mod = 1_000_000_007L
        val n = nums.size
        val dp = LongArray(n)
        val pref = LongArray(n)

        val maxDeque = java.util.ArrayDeque<Int>()
        val minDeque = java.util.ArrayDeque<Int>()
        var left = 0

        for (i in 0 until n) {
            while (maxDeque.isNotEmpty() && nums[maxDeque.peekLast()] <= nums[i]) {
                maxDeque.pollLast()
            }
            maxDeque.addLast(i)

            while (minDeque.isNotEmpty() && nums[minDeque.peekLast()] >= nums[i]) {
                minDeque.pollLast()
            }
            minDeque.addLast(i)

            while (nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()] > k) {
                if (maxDeque.peekFirst() == left) maxDeque.pollFirst()
                if (minDeque.peekFirst() == left) minDeque.pollFirst()
                left++
            }

            val totalPrev = if (i == 0) 0L else pref[i - 1]
            val dpVal: Long = if (left == 0) {
                (1L + totalPrev) % mod
            } else {
                val subtract = if (left >= 2) pref[left - 2] else 0L
                var v = totalPrev - subtract
                v %= mod
                if (v < 0) v += mod
                v
            }
            dp[i] = dpVal
            pref[i] = (totalPrev + dpVal) % mod
        }

        return dp[n - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countPartitions(List<int> nums, int k) {
    int n = nums.length;
    List<int> dp = List.filled(n, 0);
    List<int> pref = List.filled(n, 0);

    // Deques storing indices
    List<int> maxDeque = [];
    List<int> minDeque = [];
    int maxHead = 0;
    int minHead = 0;

    int left = 0;

    for (int i = 0; i < n; ++i) {
      // maintain decreasing deque for maximum
      while (maxDeque.length > maxHead && nums[maxDeque.last] <= nums[i]) {
        maxDeque.removeLast();
      }
      maxDeque.add(i);

      // maintain increasing deque for minimum
      while (minDeque.length > minHead && nums[minDeque.last] >= nums[i]) {
        minDeque.removeLast();
      }
      minDeque.add(i);

      // shrink window until condition satisfied
      while (nums[maxDeque[maxHead]] - nums[minDeque[minHead]] > k) {
        if (maxDeque[maxHead] == left) maxHead++;
        if (minDeque[minHead] == left) minHead++;
        left++;
      }

      int sum;
      if (left == 0) {
        int prevPref = i > 0 ? pref[i - 1] : 0;
        sum = (1 + prevPref) % _MOD;
      } else {
        int prevPref = i > 0 ? pref[i - 1] : 0;
        int sub = left - 2 >= 0 ? pref[left - 2] : 0;
        sum = (prevPref - sub) % _MOD;
        if (sum < 0) sum += _MOD;
      }

      dp[i] = sum;
      pref[i] = ((i > 0 ? pref[i - 1] : 0) + dp[i]) % _MOD;
    }

    return dp[n - 1];
  }
}
```

## Golang

```go
func countPartitions(nums []int, k int) int {
	const MOD = 1000000007
	n := len(nums)
	dp := make([]int, n)
	pref := make([]int, n)

	maxDeque := make([]int, 0)
	minDeque := make([]int, 0)
	left := 0

	for i := 0; i < n; i++ {
		// maintain decreasing max deque
		for len(maxDeque) > 0 && nums[maxDeque[len(maxDeque)-1]] <= nums[i] {
			maxDeque = maxDeque[:len(maxDeque)-1]
		}
		maxDeque = append(maxDeque, i)

		// maintain increasing min deque
		for len(minDeque) > 0 && nums[minDeque[len(minDeque)-1]] >= nums[i] {
			minDeque = minDeque[:len(minDeque)-1]
		}
		minDeque = append(minDeque, i)

		// shrink window until valid
		for len(maxDeque) > 0 && len(minDeque) > 0 && nums[maxDeque[0]]-nums[minDeque[0]] > k {
			if maxDeque[0] == left {
				maxDeque = maxDeque[1:]
			}
			if minDeque[0] == left {
				minDeque = minDeque[1:]
			}
			left++
		}

		var sum int
		if i > 0 {
			sum = pref[i-1]
		} else {
			sum = 0
		}

		if left == 0 {
			sum = (sum + 1) % MOD // empty prefix case
		} else {
			if left >= 2 {
				sub := pref[left-2]
				sum -= sub
				if sum < 0 {
					sum += MOD
				}
			}
			// when left == 1, no subtraction needed
		}

		dp[i] = sum % MOD
		if i == 0 {
			pref[i] = dp[i]
		} else {
			pref[i] = (pref[i-1] + dp[i]) % MOD
		}
	}
	return dp[n-1] % MOD
}
```

## Ruby

```ruby
def count_partitions(nums, k)
  mod = 1_000_000_007
  n = nums.length

  dp = Array.new(n + 1, 0)
  pref = Array.new(n + 1, 0)
  dp[0] = 1
  pref[0] = 1

  max_deque = []
  min_deque = []
  max_head = 0
  min_head = 0
  left = 0

  (0...n).each do |i|
    while max_head < max_deque.length && nums[max_deque[-1]] <= nums[i]
      max_deque.pop
    end
    max_deque << i

    while min_head < min_deque.length && nums[min_deque[-1]] >= nums[i]
      min_deque.pop
    end
    min_deque << i

    while nums[max_deque[max_head]] - nums[min_deque[min_head]] > k
      if max_deque[max_head] == left
        max_head += 1
      end
      if min_deque[min_head] == left
        min_head += 1
      end
      left += 1
    end

    sum = pref[i]
    sum -= pref[left - 1] if left > 0
    sum %= mod
    sum += mod if sum < 0

    dp[i + 1] = sum
    pref[i + 1] = (pref[i] + dp[i + 1]) % mod
  end

  dp[n] % mod
end
```

## Scala

```scala
object Solution {
    def countPartitions(nums: Array[Int], k: Int): Int = {
        val MOD = 1000000007L
        val n = nums.length
        val dp = new Array[Long](n)
        val pre = new Array[Long](n)

        import java.util.ArrayDeque

        val maxDQ = new ArrayDeque[Int]()
        val minDQ = new ArrayDeque[Int]()

        var left = 0

        for (i <- 0 until n) {
            while (!maxDQ.isEmpty && nums(maxDQ.peekLast()) <= nums(i)) {
                maxDQ.pollLast()
            }
            maxDQ.addLast(i)

            while (!minDQ.isEmpty && nums(minDQ.peekLast()) >= nums(i)) {
                minDQ.pollLast()
            }
            minDQ.addLast(i)

            while (!maxDQ.isEmpty && !minDQ.isEmpty &&
                   (nums(maxDQ.peekFirst()).toLong - nums(minDQ.peekFirst()).toLong > k.toLong)) {
                if (maxDQ.peekFirst() == left) maxDQ.pollFirst()
                if (minDQ.peekFirst() == left) minDQ.pollFirst()
                left += 1
            }

            val prePrev = if (i > 0) pre(i - 1) else 0L
            var sum = prePrev
            if (left > 0) {
                val sub = if (left >= 2) pre(left - 2) else 0L
                sum = (sum - sub + MOD) % MOD
            } else {
                sum = (sum + 1) % MOD
            }
            dp(i) = sum
            pre(i) = (prePrev + dp(i)) % MOD
        }

        dp(n - 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut dp = vec![0i64; n + 1];
        let mut pref = vec![0i64; n + 1];
        dp[0] = 1;
        pref[0] = 1;

        use std::collections::VecDeque;
        let mut min_deque: VecDeque<usize> = VecDeque::new();
        let mut max_deque: VecDeque<usize> = VecDeque::new();

        let mut l: usize = 0;

        for r in 0..n {
            // maintain monotonic queues
            while let Some(&idx) = min_deque.back() {
                if nums[idx] > nums[r] {
                    min_deque.pop_back();
                } else {
                    break;
                }
            }
            min_deque.push_back(r);
            while let Some(&idx) = max_deque.back() {
                if nums[idx] < nums[r] {
                    max_deque.pop_back();
                } else {
                    break;
                }
            }
            max_deque.push_back(r);

            // shrink window until condition holds
            loop {
                let cur_max = nums[*max_deque.front().unwrap()] as i64;
                let cur_min = nums[*min_deque.front().unwrap()] as i64;
                if cur_max - cur_min <= k as i64 {
                    break;
                }
                if let Some(&front) = min_deque.front() {
                    if front == l {
                        min_deque.pop_front();
                    }
                }
                if let Some(&front) = max_deque.front() {
                    if front == l {
                        max_deque.pop_front();
                    }
                }
                l += 1;
            }

            // dp transition using prefix sums
            let pref_l_minus_1 = if l == 0 { 0 } else { pref[l - 1] };
            let mut val = (pref[r] - pref_l_minus_1) % MOD;
            if val < 0 {
                val += MOD;
            }
            dp[r + 1] = val;
            pref[r + 1] = (pref[r] + val) % MOD;
        }

        dp[n] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-partitions nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (dp (make-vector n 0))
         (pref (make-vector n 0))
         (min-deq (make-vector n 0))
         (max-deq (make-vector n 0))
         (left 0)
         (min-head 0) (min-tail 0)
         (max-head 0) (max-tail 0))
    (let loop ((i 0))
      (when (< i n)
        (define cur (vector-ref arr i))
        ;; update min deque (increasing)
        (let rec ((mh min-head) (mt min-tail))
          (if (and (< mh mt)
                   (>= (vector-ref arr (vector-ref min-deq (- mt 1))) cur))
              (begin
                (set! min-tail (- mt 1))
                (rec mh (- mt 1)))
              (begin
                (vector-set! min-deq min-tail i)
                (set! min-tail (+ min-tail 1)))))
        ;; update max deque (decreasing)
        (let rec ((mh max-head) (mt max-tail))
          (if (and (< mh mt)
                   (<= (vector-ref arr (vector-ref max-deq (- mt 1))) cur))
              (begin
                (set! max-tail (- mt 1))
                (rec mh (- mt 1)))
              (begin
                (vector-set! max-deq max-tail i)
                (set! max-tail (+ max-tail 1)))))
        ;; shrink left while invalid
        (let shrink ()
          (when (> (- (vector-ref arr (vector-ref max-deq max-head))
                     (vector-ref arr (vector-ref min-deq min-head))) k)
            (when (= (vector-ref min-deq min-head) left)
              (set! min-head (+ min-head 1)))
            (when (= (vector-ref max-deq max-head) left)
              (set! max-head (+ max-head 1)))
            (set! left (+ left 1))
            (shrink)))
        ;; compute dp[i]
        (define dp-i
          (if (= left 0)
              (let ((prev (if (= i 0) 0 (vector-ref pref (- i 1)))))
                (modulo (+ 1 prev) MOD))
              (let* ((l left)
                     (pre-i-1 (if (= i 0) 0 (vector-ref pref (- i 1))))
                     (pre-l-2 (if (= l 1) 0 (vector-ref pref (- l 2))))
                     (diff (modulo (- pre-i-1 pre-l-2) MOD)))
                diff)))
        (vector-set! dp i dp-i)
        ;; update prefix sum
        (let ((prev-pref (if (= i 0) 0 (vector-ref pref (- i 1)))))
          (vector-set! pref i (modulo (+ prev-pref dp-i) MOD)))
        (loop (+ i 1))))
    (vector-ref dp (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([count_partitions/2]).

-define(MOD, 1000000007).

%% Public API
-spec count_partitions(Nums :: [integer()], K :: integer()) -> integer().
count_partitions(Nums, K) ->
    MaxD0 = new_deque(),
    MinD0 = new_deque(),
    DPQ0  = push_back(new_deque(), 1),   % dp[0] = 1
    CurSum0 = 1,
    Left0 = 0,
    loop(Nums, 0, K, MaxD0, MinD0, DPQ0, CurSum0, Left0).

%% Main loop over the array
loop([], _Idx, _K, _MaxD, _MinD, _DPQ, _CurSum, _Left) ->
    %% The answer is the last dp value stored at the back of DPQ
    case peek_back(_DPQ) of
        undefined -> 0;
        {_Idx, Val} -> Val rem ?MOD
    end;

loop([Val|Rest], Idx, K, MaxD, MinD, DPQ, CurSum, Left) ->
    %% Insert current element into monotonic deques
    MaxD1 = push_max(MaxD, {Idx, Val}),
    MinD1 = push_min(MinD, {Idx, Val}),

    %% Shrink window while condition violated
    {Left2, MaxD2, MinD2, DPQ2, CurSum2} =
        shrink_window(K, Left, MaxD1, MinD1, DPQ, CurSum),

    %% dp for prefix ending at Idx (i.e., dp[Idx+1]) is current sum
    NewDP = CurSum2 rem ?MOD,

    %% Add new dp to structures
    DPQ3  = push_back(DPQ2, {Idx + 1, NewDP}),
    CurSum3 = (CurSum2 + NewDP) rem ?MOD,

    loop(Rest, Idx + 1, K, MaxD2, MinD2, DPQ3, CurSum3, Left2).

%% Shrink window until max-min <= K
shrink_window(K, Left, MaxD, MinD, DPQ, CurSum) ->
    case {peek_front(MaxD), peek_front(MinD)} of
        {{_, MaxVal}, {_, MinVal}} when MaxVal - MinVal =< K ->
            {Left, MaxD, MinD, DPQ, CurSum};
        _ ->
            %% Remove leftmost index from deques if present
            MaxD1 = maybe_pop_front(MaxD, Left),
            MinD1 = maybe_pop_front(MinD, Left),

            %% Pop dp value corresponding to 'Left' from DPQ front
            {FrontDP, DPQ1} = pop_front(DPQ),
            CurSum1 = (CurSum - FrontDP + ?MOD) rem ?MOD,
            shrink_window(K, Left + 1, MaxD1, MinD1, DPQ1, CurSum1)
    end.

%% Helper to conditionally pop front element if its index matches Left
maybe_pop_front(D, Index) ->
    case peek_front(D) of
        {Idx, _Val} when Idx =:= Index -> 
            {_, D1} = pop_front(D),
            D1;
        _ -> D
    end.

%% Monotonic max deque push (decreasing values)
push_max(D, Elem = {_Idx, Val}) ->
    case peek_back(D) of
        undefined -> ok;
        {_BIdx, BVal} when BVal < Val ->
            {_, D1} = pop_back(D),
            return push_max(D1, Elem);
        _ -> ok
    end,
    push_back(D, Elem).

%% Monotonic min deque push (increasing values)
push_min(D, Elem = {_Idx, Val}) ->
    case peek_back(D) of
        undefined -> ok;
        {_BIdx, BVal} when BVal > Val ->
            {_, D1} = pop_back(D),
            return push_min(D1, Elem);
        _ -> ok
    end,
    push_back(D, Elem).

%% Deque implementation using two lists (front and back)
new_deque() ->
    #{front => [], back => []}.

push_back(D, Elem) ->
    Back = maps:get(back, D),
    D#{back => [Elem | Back]}.

peek_front(D) ->
    case maps:get(front, D) of
        [H|_] -> H;
        [] ->
            case lists:reverse(maps:get(back, D)) of
                [] -> undefined;
                [H2|_] -> H2
            end
    end.

pop_front(D) ->
    case maps:get(front, D) of
        [H|T] ->
            {H, D#{front => T}};
        [] ->
            Back = maps:get(back, D),
            Rev = lists:reverse(Back),
            case Rev of
                [] -> error;
                [H2|T2] ->
                    {H2, #{front => T2, back => []}}
            end
    end.

peek_back(D) ->
    case maps:get(back, D) of
        [H|_] -> H;
        [] ->
            case lists:reverse(maps:get(front, D)) of
                [] -> undefined;
                [H2|_] -> H2
            end
    end.

pop_back(D) ->
    case maps:get(back, D) of
        [_|_] = B ->
            {hd(B), D#{back => tl(B)}};
        [] ->
            Front = maps:get(front, D),
            RevF = lists:reverse(Front),
            case RevF of
                [] -> error;
                [H|T] ->
                    {H, #{front => [], back => T}}
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec count_partitions(nums :: [integer], k :: integer) :: integer
  def count_partitions(nums, k) do
    mod = 1_000_000_007
    n = length(nums)

    nums_arr = :array.from_list(nums)

    # dp[0] = 1, pref[0] = 1
    dp_arr = :array.set(0, 1, :array.new(n + 1, default: 0))
    pref_arr = :array.set(0, 1, :array.new(n + 1, default: 0))

    max_q = :queue.new()
    min_q = :queue.new()
    left = 0

    {_, _, _, final_dp, _} =
      Enum.reduce(0..(n - 1), {max_q, min_q, left, dp_arr, pref_arr}, fn i,
                                                                      {mq, miq, l, dpa, pfa} ->
        # maintain max deque (decreasing values)
        mq = pop_back_while(mq, i, fn new, old -> new > old end, nums_arr)
        mq = :queue.in(i, mq)

        # maintain min deque (increasing values)
        miq = pop_back_while(miq, i, fn new, old -> new < old end, nums_arr)
        miq = :queue.in(i, miq)

        {l, mq, miq} = adjust_left(l, mq, miq, k, nums_arr)

        pref_i = :array.get(i, pfa)
        sub =
          if l > 0 do
            :array.get(l - 1, pfa)
          else
            0
          end

        val = pref_i - sub
        val = rem(val, mod)
        val = if val < 0, do: val + mod, else: val

        dp_idx = i + 1
        dpa = :array.set(dp_idx, val, dpa)

        new_pref = rem(pref_i + val, mod)
        pfa = :array.set(dp_idx, new_pref, pfa)

        {mq, miq, l, dpa, pfa}
      end)

    :array.get(n, final_dp)
  end

  # Pop from the back while cmp.(new_val, last_val) is true
  defp pop_back_while(q, idx, cmp, nums_arr) do
    case :queue.peek_r(q) do
      {:value, last_idx} ->
        new_val = :array.get(idx, nums_arr)
        last_val = :array.get(last_idx, nums_arr)

        if cmp.(new_val, last_val) do
          {{:value, _}, q2} = :queue.out_r(q)
          pop_back_while(q2, idx, cmp, nums_arr)
        else
          q
        end

      :empty ->
        q
    end
  end

  # Adjust left pointer to keep window valid
  defp adjust_left(left, max_q, min_q, k, nums_arr) do
    case {:queue.peek(max_q), :queue.peek(min_q)} do
      {{:value, max_idx}, {:value, min_idx}} ->
        max_val = :array.get(max_idx, nums_arr)
        min_val = :array.get(min_idx, nums_arr)

        if max_val - min_val > k do
          {max_q, min_q} =
            if max_idx == left do
              {{:value, _}, mq2} = :queue.out(max_q)
              {mq2, min_q}
            else
              {max_q, min_q}
            end

          {max_q, min_q} =
            if min_idx == left do
              {{:value, _}, miq2} = :queue.out(min_q)
              {max_q, miq2}
            else
              {max_q, min_q}
            end

          adjust_left(left + 1, max_q, min_q, k, nums_arr)
        else
          {left, max_q, min_q}
        end

      _ ->
        {left, max_q, min_q}
    end
  end
end
```
