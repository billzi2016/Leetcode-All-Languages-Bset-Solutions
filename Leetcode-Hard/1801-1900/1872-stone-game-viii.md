# 1872. Stone Game VIII

## Cpp

```cpp
class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();
        vector<long long> pref(n);
        pref[0] = stones[0];
        for (int i = 1; i < n; ++i) pref[i] = pref[i-1] + stones[i];
        long long best = pref[n-1]; // total sum
        for (int i = n - 2; i >= 1; --i) {
            best = max(pref[i] - best, best);
        }
        return (int)best;
    }
};
```

## Java

```java
class Solution {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        long[] pref = new long[n];
        pref[0] = stones[0];
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + stones[i];
        }
        // dp[i] for i in [1, n], with dp[n]=0
        long[] dp = new long[n + 1];
        dp[n] = 0;
        long best = Long.MIN_VALUE;
        for (int i = n - 1; i >= 1; --i) {
            long cand = pref[i] - dp[i + 1];
            if (cand > best) best = cand;
            dp[i] = best;
        }
        long answer = Long.MIN_VALUE;
        for (int j = 1; j < n; ++j) {
            long val = pref[j] - dp[j + 1];
            if (val > answer) answer = val;
        }
        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        # prefix sums
        pref = [0] * n
        cur = 0
        for i, v in enumerate(stones):
            cur += v
            pref[i] = cur
        total = cur

        # suffix sums
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = stones[i] + suff[i + 1]

        dp = [0] * (n + 1)   # dp[i]: best difference for player to move when suffix starts at i
        best = -10**18
        for i in range(n - 1, -1, -1):
            cand = total - suff[i + 1] - dp[i + 1]
            if cand > best:
                best = cand
            dp[i] = best

        ans = -10**18
        for j in range(1, n):
            val = pref[j] - dp[j + 1]
            if val > ans:
                ans = val
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * n
        cur = 0
        for i, v in enumerate(stones):
            cur += v
            prefix[i] = cur

        dp = [0] * n          # dp[n-1] stays 0
        best = -10**18        # max of (prefix[j] - dp[j]) for j > i
        for i in range(n - 2, -1, -1):
            cand = prefix[i + 1] - dp[i + 1]
            if cand > best:
                best = cand
            dp[i] = best

        return dp[0]
```

## C

```c
int stoneGameVIII(int* stones, int stonesSize){
    long long *pref = (long long*)malloc(sizeof(long long) * stonesSize);
    long long sum = 0;
    for (int i = 0; i < stonesSize; ++i){
        sum += stones[i];
        pref[i] = sum;
    }
    long long suffixMax = pref[stonesSize - 1]; // dp[n-1] = 0, so pref[n-1] - 0
    long long answer = suffixMax;
    for (int i = stonesSize - 2; i >= 0; --i){
        if (i == 0) answer = suffixMax;          // result before processing i=0
        long long v = pref[i] - suffixMax;       // pref[i] - dp[i]
        if (v > suffixMax) suffixMax = v;
    }
    free(pref);
    return (int)answer;
}
```

## Csharp

```csharp
public class Solution {
    public int StoneGameVIII(int[] stones) {
        int n = stones.Length;
        long[] pre = new long[n];
        pre[0] = stones[0];
        for (int i = 1; i < n; i++) {
            pre[i] = pre[i - 1] + stones[i];
        }

        long[] dp = new long[n];
        dp[n - 1] = 0;
        long best = pre[n - 1]; // when i = n-2, only j = n-1 is possible
        dp[n - 2] = best;

        for (int i = n - 3; i >= 0; --i) {
            long cand = pre[i + 1] - dp[i + 1];
            if (cand > best) best = cand;
            dp[i] = best;
        }

        return (int)dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVIII = function(stones) {
    const n = stones.length;
    const pref = new Array(n);
    pref[0] = stones[0];
    for (let i = 1; i < n; ++i) {
        pref[i] = pref[i - 1] + stones[i];
    }
    const total = pref[n - 1];
    let ans = total; // take all stones
    for (let i = 1; i <= n - 2; ++i) {
        const cand = pref[i] - total;
        if (cand > ans) ans = cand;
    }
    return ans;
};
```

## Typescript

```typescript
function stoneGameVIII(stones: number[]): number {
    const n = stones.length;
    const prefix = new Array<number>(n);
    let sum = 0;
    for (let i = 0; i < n; ++i) {
        sum += stones[i];
        prefix[i] = sum;
    }
    if (n === 2) return prefix[1];

    let ans = prefix[n - 1]; // taking all stones at once
    let minPref = prefix[n - 1];
    for (let i = n - 2; i >= 1; --i) {
        const candidate = prefix[i] - minPref;
        if (candidate > ans) ans = candidate;
        if (prefix[i] < minPref) minPref = prefix[i];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVIII($stones) {
        $n = count($stones);
        $pref = [];
        $sum = 0;
        for ($i = 0; $i < $n; $i++) {
            $sum += $stones[$i];
            $pref[$i] = $sum;
        }

        // dp[i] = optimal difference when the game state starts at index i
        $dp = array_fill(0, $n + 1, 0);
        $maxSuffix = PHP_INT_MIN;

        for ($i = $n - 1; $i >= 0; $i--) {
            $candidate = $pref[$i] - $dp[$i + 1];
            if ($candidate > $maxSuffix) {
                $maxSuffix = $candidate;
            }
            $dp[$i] = $maxSuffix;
        }

        // The answer corresponds to dp[1], as the first move must remove at least two stones
        return $dp[1];
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameVIII(_ stones: [Int]) -> Int {
        let n = stones.count
        var prefix = [Int](repeating: 0, count: n)
        var sum = 0
        for i in 0..<n {
            sum += stones[i]
            prefix[i] = sum
        }
        
        // dp[n-1] = 0
        var dpNext = 0          // represents dp[i+1] during iteration
        var best = Int.min
        var answer = 0
        
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                let cand = prefix[i + 1] - dpNext
                if cand > best { best = cand }
                dpNext = best      // now dpNext holds dp[i]
            }
            answer = dpNext        // dp[0]
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameVIII(stones: IntArray): Int {
        val n = stones.size
        val prefix = LongArray(n)
        var sum = 0L
        for (i in 0 until n) {
            sum += stones[i].toLong()
            prefix[i] = sum
        }
        var best = prefix[n - 1] // dp[n-1] = 0, so pref[n-1] - 0
        var dpCurrent = 0L
        for (i in n - 2 downTo 0) {
            dpCurrent = best
            val candidate = prefix[i] - dpCurrent
            if (candidate > best) {
                best = candidate
            }
        }
        return dpCurrent.toInt()
    }
}
```

## Golang

```go
func stoneGameVIII(stones []int) int {
    n := len(stones)
    prefix := make([]int, n)
    sum := 0
    for i, v := range stones {
        sum += v
        prefix[i] = sum
    }

    dpNext := 0 // corresponds to dp[n]
    maxDiff := -(1 << 60)

    for i := n - 1; i >= 1; i-- {
        cand := prefix[i] - dpNext
        if cand > maxDiff {
            maxDiff = cand
        }
        dpNext = maxDiff
    }
    return dpNext
}
```

## Ruby

```ruby
def stone_game_viii(stones)
  n = stones.length
  prefix = Array.new(n)
  sum = 0
  stones.each_with_index do |v, i|
    sum += v
    prefix[i] = sum
  end

  dp_next = 0 # dp[n]
  i = n - 1
  while i >= 1
    if i == n - 1
      cur = prefix[i] - dp_next
    else
      take = prefix[i] - dp_next
      cur = take > dp_next ? take : dp_next
    end
    dp_next = cur
    i -= 1
  end

  dp_next
end
```

## Scala

```scala
object Solution {
    def stoneGameVIII(stones: Array[Int]): Int = {
        val n = stones.length
        val pref = new Array[Long](n)
        var sum: Long = 0L
        var i = 0
        while (i < n) {
            sum += stones(i).toLong
            pref(i) = sum
            i += 1
        }
        val dp = new Array[Long](n + 1)
        dp(n) = 0L
        dp(n - 1) = pref(n - 1)
        var best: Long = dp(n - 1)
        i = n - 2
        while (i >= 0) {
            dp(i) = best
            val candidate = pref(i) - dp(i + 1)
            if (candidate > best) best = candidate
            i -= 1
        }
        dp(0).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_viii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        // prefix sums as i64
        let mut pre = vec![0i64; n];
        let mut sum = 0i64;
        for (i, &v) in stones.iter().enumerate() {
            sum += v as i64;
            pre[i] = sum;
        }
        // dp[i] = max_{j >= i} (pre[j] - dp[j+1]), dp[n]=0
        let mut dp = vec![0i64; n + 1];
        let mut best = i64::MIN;
        for i in (0..n).rev() {
            let cand = pre[i] - dp[i + 1];
            if cand > best {
                best = cand;
            }
            dp[i] = best;
        }
        // Alice must take at least two stones initially, so answer is dp[1]
        dp[1] as i32
    }
}
```

## Racket

```racket
(define/contract (stone-game-viii stones)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length stones))
         (pref (make-vector n))
         (sum 0))
    (for ([i (in-range n)])
      (set! sum (+ sum (list-ref stones i)))
      (vector-set! pref i sum))
    (define best -inf.0)
    (define next-dp 0) ; dp[i+1], initially dp[n-1] = 0
    (for ([i (in-range (- n 2) -1 -1)]) ; i from n-2 down to 0
      (let ((candidate (- (vector-ref pref (+ i 1)) next-dp)))
        (when (> candidate best)
          (set! best candidate))
        (set! next-dp best))) ; dp[i] becomes best for the next iteration
    next-dp))
```
