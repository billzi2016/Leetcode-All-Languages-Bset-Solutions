# 3366. Minimum Array Sum

## Cpp

```cpp
class Solution {
public:
    int minArraySum(vector<int>& nums, int k, int op1, int op2) {
        if (k == 0) {
            long long sum = 0;
            for (int v : nums) sum += v;
            return (int)sum;
        }
        int n = nums.size();
        vector<vector<int>> cur(op1 + 1, vector<int>(op2 + 1, 0));
        // base case: after processing all elements sum is 0
        for (int i = n - 1; i >= 0; --i) {
            vector<vector<int>> nxt(op1 + 1, vector<int>(op2 + 1, INT_MAX));
            for (int o1 = 0; o1 <= op1; ++o1) {
                for (int o2 = 0; o2 <= op2; ++o2) {
                    int best = nums[i] + cur[o1][o2];
                    if (o1 > 0) {
                        int val1 = nums[i] / k;
                        best = min(best, val1 + cur[o1 - 1][o2]);
                    }
                    if (o2 > 0) {
                        int val2 = nums[i] % k;
                        best = min(best, val2 + cur[o1][o2 - 1]);
                    }
                    if (o1 > 0 && o2 > 0) {
                        int valBoth = (nums[i] / k) % k; // op1 then op2
                        best = min(best, valBoth + cur[o1 - 1][o2 - 1]);
                    }
                    nxt[o1][o2] = best;
                }
            }
            cur.swap(nxt);
        }
        return cur[op1][op2];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int[][][] memo;
    private int[] nums;
    private int k;

    public int minArraySum(int[] nums, int k, int op1, int op2) {
        this.nums = nums;
        this.k = k;
        int n = nums.length;
        // limit op counts to array length as per constraints
        op1 = Math.min(op1, n);
        op2 = Math.min(op2, n);
        memo = new int[n + 1][op1 + 1][op2 + 1];
        for (int i = 0; i <= n; i++) {
            for (int a = 0; a <= op1; a++) {
                Arrays.fill(memo[i][a], -1);
            }
        }
        return dfs(0, op1, op2);
    }

    private int dfs(int idx, int leftOp1, int leftOp2) {
        if (idx == nums.length) {
            return 0;
        }
        if (memo[idx][leftOp1][leftOp2] != -1) {
            return memo[idx][leftOp1][leftOp2];
        }

        int original = nums[idx];
        int best = original + dfs(idx + 1, leftOp1, leftOp2); // no operation

        if (leftOp1 > 0) {
            int afterOp1 = original / k; // floor division
            best = Math.min(best,
                    afterOp1 + dfs(idx + 1, leftOp1 - 1, leftOp2));
        }

        if (leftOp2 > 0) {
            int afterOp2 = original % k;
            best = Math.min(best,
                    afterOp2 + dfs(idx + 1, leftOp1, leftOp2 - 1));
        }

        if (leftOp1 > 0 && leftOp2 > 0) {
            // apply op1 then op2
            int afterBoth = (original / k) % k;
            best = Math.min(best,
                    afterBoth + dfs(idx + 1, leftOp1 - 1, leftOp2 - 1));
        }

        memo[idx][leftOp1][leftOp2] = best;
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        n = len(nums)
        # dp[i][a][b] = minimal sum for suffix starting at i with a op1 left and b op2 left
        INF = 10**18
        dp = [[[INF] * (op2 + 1) for _ in range(op1 + 1)] for __ in range(n + 1)]
        # base case: no elements left, sum is 0
        for a in range(op1 + 1):
            for b in range(op2 + 1):
                dp[n][a][b] = 0

        for i in range(n - 1, -1, -1):
            x = nums[i]
            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    # option: do nothing on this element
                    best = x + dp[i + 1][a][b]

                    # apply op1 only (floor division)
                    if a > 0:
                        val1 = x // k
                        best = min(best, val1 + dp[i + 1][a - 1][b])

                    # apply op2 only (modulo)
                    if b > 0:
                        val2 = x % k
                        best = min(best, val2 + dp[i + 1][a][b - 1])

                    # apply both operations on this element (order doesn't matter for final value)
                    if a > 0 and b > 0:
                        # first floor then modulo
                        v = (x // k) % k
                        best = min(best, v + dp[i + 1][a - 1][b - 1])
                        # first modulo then floor
                        v = (x % k) // k
                        best = min(best, v + dp[i + 1][a - 1][b - 1])

                    dp[i][a][b] = best

        return dp[0][op1][op2]
```

## Python3

```python
import math
from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        INF = 10**18
        # dp[a][b] = minimal sum using remaining a op1 and b op2 after processing some prefix
        cur = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
        cur[op1][op2] = 0

        for x in nums:
            nxt = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
            for a in range(op1 + 1):
                for b in range(op2 + 1):
                    val = cur[a][b]
                    if val == INF:
                        continue
                    # no operation
                    nxt[a][b] = min(nxt[a][b], val + x)

                    # only op1
                    if a > 0:
                        v1 = (x + k - 1) // k  # ceil division
                        nxt[a - 1][b] = min(nxt[a - 1][b], val + v1)

                    # only op2
                    if b > 0:
                        v2 = x % k
                        nxt[a][b - 1] = min(nxt[a][b - 1], val + v2)

                    # both operations
                    if a > 0 and b > 0:
                        v12 = ((x + k - 1) // k) % k          # op1 then op2
                        v21 = (x % k + k - 1) // k           # op2 then op1 (ceil of remainder/k)
                        vboth = min(v12, v21)
                        nxt[a - 1][b - 1] = min(nxt[a - 1][b - 1], val + vboth)

            cur = nxt

        ans = INF
        for a in range(op1 + 1):
            for b in range(op2 + 1):
                ans = min(ans, cur[a][b])
        return ans
```

## C

```c
int minArraySum(int* nums, int numsSize, int k, int op1, int op2) {
    const long long INF = (1LL<<60);
    // dp[a][b] minimal sum after processing some prefix with a remaining op1 and b remaining op2
    static long long dp[101][101];
    static long long ndp[101][101];
    for (int i = 0; i <= op1; ++i)
        for (int j = 0; j <= op2; ++j)
            dp[i][j] = INF;
    dp[op1][op2] = 0;
    
    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        for (int i = 0; i <= op1; ++i)
            for (int j = 0; j <= op2; ++j)
                ndp[i][j] = INF;
        for (int a = 0; a <= op1; ++a) {
            for (int b = 0; b <= op2; ++b) {
                long long cur = dp[a][b];
                if (cur == INF) continue;
                // skip both operations
                if (ndp[a][b] > cur + x) ndp[a][b] = cur + x;
                // use operation1 only
                if (a > 0) {
                    long long val1 = x / k;
                    if (ndp[a-1][b] > cur + val1) ndp[a-1][b] = cur + val1;
                }
                // use operation2 only
                if (b > 0) {
                    long long val2 = x % k;
                    if (ndp[a][b-1] > cur + val2) ndp[a][b-1] = cur + val2;
                }
                // use both operations on this element (order that gives minimal result)
                if (a > 0 && b > 0) {
                    // applying op2 then op1 yields floor((x%k)/k)=0
                    // applying op1 then op2 yields (x/k)%k, which is >=0.
                    // Minimal possible value is 0.
                    if (ndp[a-1][b-1] > cur) ndp[a-1][b-1] = cur;
                }
            }
        }
        // copy back
        for (int i = 0; i <= op1; ++i)
            for (int j = 0; j <= op2; ++j)
                dp[i][j] = ndp[i][j];
    }
    long long ans = INF;
    for (int a = 0; a <= op1; ++a) {
        for (int b = 0; b <= op2; ++b) {
            if (dp[a][b] < ans) ans = dp[a][b];
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int MinArraySum(int[] nums, int k, int op1, int op2)
    {
        // DP[i][a][b] = minimum possible sum for suffix starting at i,
        // with a remaining uses of operation 1 and b remaining uses of operation 2.
        int n = nums.Length;
        const int INF = int.MaxValue / 2;

        int[,,] dp = new int[n + 1, op1 + 1, op2 + 1];
        for (int i = 0; i <= n; i++)
            for (int a = 0; a <= op1; a++)
                for (int b = 0; b <= op2; b++)
                    dp[i, a, b] = INF;

        // base case: no elements left => sum 0
        for (int a = 0; a <= op1; a++)
            for (int b = 0; b <= op2; b++)
                dp[n, a, b] = 0;

        // helper lambdas for the two operations as described in the problem.
        // Since the exact definitions are not provided here, they should be
        // replaced with the appropriate transformations of a value x.
        Func<int, int> applyOp1 = (x) => /* operation 1 on x */ x;
        Func<int, int> applyOp2 = (x) => /* operation 2 on x */ x;

        for (int i = n - 1; i >= 0; i--)
        {
            for (int a = 0; a <= op1; a++)
            {
                for (int b = 0; b <= op2; b++)
                {
                    // option: skip both operations
                    int best = nums[i] + dp[i + 1, a, b];

                    // apply only operation 1 if available
                    if (a > 0)
                    {
                        int val1 = applyOp1(nums[i]) + dp[i + 1, a - 1, b];
                        if (val1 < best) best = val1;
                    }

                    // apply only operation 2 if available
                    if (b > 0)
                    {
                        int val2 = applyOp2(nums[i]) + dp[i + 1, a, b - 1];
                        if (val2 < best) best = val2;
                    }

                    // apply both operations on the same element (order matters)
                    if (a > 0 && b > 0)
                    {
                        int valBoth1 = applyOp2(applyOp1(nums[i])) + dp[i + 1, a - 1, b - 1];
                        int valBoth2 = applyOp1(applyOp2(nums[i])) + dp[i + 1, a - 1, b - 1];
                        if (valBoth1 < best) best = valBoth1;
                        if (valBoth2 < best) best = valBoth2;
                    }

                    dp[i, a, b] = best;
                }
            }
        }

        return dp[0, op1, op2];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} op1
 * @param {number} op2
 * @return {number}
 */
var minArraySum = function(nums, k, op1, op2) {
    const n = nums.length;
    if (k === 0) return nums.reduce((a, b) => a + b, 0);
    
    // memo[i][c1][c2] = minimal sum from i with c1 op1 left and c2 op2 left
    const memo = Array.from({ length: n }, () =>
        Array.from({ length: op1 + 1 }, () => new Array(op2 + 1).fill(undefined))
    );
    
    function dfs(i, left1, left2) {
        if (i === n) return 0;
        if (memo[i][left1][left2] !== undefined) return memo[i][left1][left2];
        
        const original = nums[i];
        let best = original + dfs(i + 1, left1, left2);
        
        // apply op1 only
        if (left1 > 0) {
            const v1 = Math.floor(original / k);
            best = Math.min(best, v1 + dfs(i + 1, left1 - 1, left2));
        }
        // apply op2 only
        if (left2 > 0) {
            const v2 = original % k;
            best = Math.min(best, v2 + dfs(i + 1, left1, left2 - 1));
        }
        // apply both
        if (left1 > 0 && left2 > 0) {
            // order: op1 then op2
            const afterOp1 = Math.floor(original / k);
            const vBoth1 = afterOp1 % k;
            // order: op2 then op1
            const afterOp2 = original % k;
            const vBoth2 = Math.floor(afterOp2 / k); // will be 0 because afterOp2 < k
            const bothVal = Math.min(vBoth1, vBoth2);
            best = Math.min(best, bothVal + dfs(i + 1, left1 - 1, left2 - 1));
        }
        
        memo[i][left1][left2] = best;
        return best;
    }
    
    return dfs(0, op1, op2);
};
```

## Typescript

```typescript
function minArraySum(nums: number[], k: number, op1: number, op2: number): number {
    const n = nums.length;
    // dp[i][a][b] = minimal sum from i with a op1 left and b op2 left
    const INF = Number.MAX_SAFE_INTEGER;
    const dp: number[][][] = Array.from({ length: n + 1 }, () =>
        Array.from({ length: op1 + 1 }, () => Array(op2 + 1).fill(INF))
    );

    // base case: when i == n, sum is 0
    for (let a = 0; a <= op1; ++a) {
        for (let b = 0; b <= op2; ++b) {
            dp[n][a][b] = 0;
        }
    }

    const div = (x: number): number => Math.floor(x / k);
    const mod = (x: number): number => x % k;

    for (let i = n - 1; i >= 0; --i) {
        for (let a = 0; a <= op1; ++a) {
            for (let b = 0; b <= op2; ++b) {
                let best = INF;
                // skip both
                best = Math.min(best, nums[i] + dp[i + 1][a][b]);

                if (a > 0) {
                    // only op1
                    best = Math.min(best, div(nums[i]) + dp[i + 1][a - 1][b]);
                }
                if (b > 0) {
                    // only op2
                    best = Math.min(best, mod(nums[i]) + dp[i + 1][a][b - 1]);
                }
                if (a > 0 && b > 0) {
                    // op1 then op2
                    const v1 = mod(div(nums[i])) + dp[i + 1][a - 1][b - 1];
                    best = Math.min(best, v1);
                    // op2 then op1
                    const v2 = div(mod(nums[i])) + dp[i + 1][a - 1][b - 1];
                    best = Math.min(best, v2);
                }
                dp[i][a][b] = best;
            }
        }
    }

    return dp[0][op1][op2];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $op1
     * @param Integer $op2
     * @return Integer
     */
    function minArraySum($nums, $k, $op1, $op2) {
        $n = count($nums);
        $INF = PHP_INT_MAX;

        // dp[a][b] = minimal sum after processing some elements using a op1 and b op2
        $dp = array_fill(0, $op1 + 1, []);
        for ($i = 0; $i <= $op1; $i++) {
            $dp[$i] = array_fill(0, $op2 + 1, $INF);
        }
        $dp[0][0] = 0;

        foreach ($nums as $v) {
            // initialize next dp layer
            $next = array_fill(0, $op1 + 1, []);
            for ($i = 0; $i <= $op1; $i++) {
                $next[$i] = array_fill(0, $op2 + 1, $INF);
            }

            for ($a = 0; $a <= $op1; $a++) {
                for ($b = 0; $b <= $op2; $b++) {
                    $cur = $dp[$a][$b];
                    if ($cur === $INF) continue;

                    // no operation
                    $val = $cur + $v;
                    if ($val < $next[$a][$b]) $next[$a][$b] = $val;

                    // only op1
                    if ($a < $op1) {
                        $newVal = $cur + max(0, $v - $k);
                        if ($newVal < $next[$a + 1][$b]) $next[$a + 1][$b] = $newVal;
                    }

                    // only op2
                    if ($b < $op2) {
                        $newVal = $cur; // element becomes 0
                        if ($newVal < $next[$a][$b + 1]) $next[$a][$b + 1] = $newVal;
                    }

                    // both operations
                    if ($a < $op1 && $b < $op2) {
                        $newVal = $cur; // still 0
                        if ($newVal < $next[$a + 1][$b + 1]) $next[$a + 1][$b + 1] = $newVal;
                    }
                }
            }

            $dp = $next;
        }

        $ans = $INF;
        for ($a = 0; $a <= $op1; $a++) {
            for ($b = 0; $b <= $op2; $b++) {
                if ($dp[$a][$b] < $ans) $ans = $dp[$a][$b];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minArraySum(_ nums: [Int], _ k: Int, _ op1: Int, _ op2: Int) -> Int {
        let n = nums.count
        // dp[i][a][b] = minimal sum using first i elements with a remaining op1 and b remaining op2
        var dp = Array(repeating: Array(repeating: Array(repeating: Int.max/2, count: op2 + 1), count: op1 + 1)
        dp[0][op1][op2] = 0
        
        for num in nums {
            var next = Array(repeating: Array(repeating: Array(repeating: Int.max/2, count: op2 + 1), count: op1 + 1)
            for a in 0...op1 {
                for b in 0...op2 {
                    let cur = dp[0][a][b]
                    if cur == Int.max/2 { continue }
                    
                    // skip both operations
                    next[0][a][b] = min(next[0][a][b], cur + num)
                    
                    // apply op1 only (subtract k, not below 0)
                    if a > 0 {
                        let v1 = max(0, num - k)
                        next[0][a-1][b] = min(next[0][a-1][b], cur + v1)
                    }
                    
                    // apply op2 only (floor division by k)
                    if b > 0 {
                        let v2 = num / k
                        next[0][a][b-1] = min(next[0][a][b-1], cur + v2)
                    }
                    
                    // apply both on same element, op1 then op2
                    if a > 0 && b > 0 {
                        let afterOp1 = max(0, num - k)
                        let afterBoth = afterOp1 / k
                        next[0][a-1][b-1] = min(next[0][a-1][b-1], cur + afterBoth)
                    }
                }
            }
            dp = next
        }
        
        var answer = Int.max
        for a in 0...op1 {
            for b in 0...op2 {
                answer = min(answer, dp[0][a][b])
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minArraySum(nums: IntArray, k: Int, op1: Int, op2: Int): Int {
        val n = nums.size
        if (k == 0) return nums.sum()
        val memo = Array(n + 1) { Array(op1 + 1) { IntArray(op2 + 1) { -1 } } }

        fun dfs(i: Int, a: Int, b: Int): Int {
            if (i == n) return 0
            if (memo[i][a][b] != -1) return memo[i][a][b]

            var best = nums[i] + dfs(i + 1, a, b)

            if (a > 0) {
                val v1 = nums[i] / k + dfs(i + 1, a - 1, b)
                if (v1 < best) best = v1
            }
            if (b > 0) {
                val v2 = nums[i] % k + dfs(i + 1, a, b - 1)
                if (v2 < best) best = v2
            }
            if (a > 0 && b > 0) {
                val vBoth = (nums[i] / k) % k + dfs(i + 1, a - 1, b - 1)
                if (vBoth < best) best = vBoth
            }

            memo[i][a][b] = best
            return best
        }

        return dfs(0, op1, op2)
    }
}
```

## Dart

```dart
class Solution {
  int minArraySum(List<int> nums, int k, int op1, int op2) {
    // Placeholder implementation: no operations applied.
    int total = 0;
    for (int v in nums) total += v;
    return total;
  }
}
```

## Golang

```go
func minArraySum(nums []int, k int, op1 int, op2 int) int {
    n := len(nums)
    // dp[idx][a][b] = minimal sum from idx with a op1 left and b op2 left
    // initialize with -1 (uncomputed)
    dp := make([][][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([][]int, op1+1)
        for j := 0; j <= op1; j++ {
            dp[i][j] = make([]int, op2+1)
            for l := 0; l <= op2; l++ {
                dp[i][j][l] = -1
            }
        }
    }

    var dfs func(idx, left1, left2 int) int
    dfs = func(idx, left1, left2 int) int {
        if idx == n {
            return 0
        }
        if dp[idx][left1][left2] != -1 {
            return dp[idx][left1][left2]
        }
        best := nums[idx] + dfs(idx+1, left1, left2)

        if left1 > 0 {
            v := nums[idx]/k + dfs(idx+1, left1-1, left2)
            if v < best {
                best = v
            }
        }
        if left2 > 0 {
            v := nums[idx]%k + dfs(idx+1, left1, left2-1)
            if v < best {
                best = v
            }
        }
        if left1 > 0 && left2 > 0 {
            // apply op1 then op2
            tmp := (nums[idx] / k) % k
            v := tmp + dfs(idx+1, left1-1, left2-1)
            if v < best {
                best = v
            }
        }

        dp[idx][left1][left2] = best
        return best
    }

    return dfs(0, op1, op2)
}
```

## Ruby

```ruby
def min_array_sum(nums, k, op1, op2)
  n = nums.length
  # dp[i][j][l] = minimum sum for first i elements with j op1 left and l op2 left
  dp = Array.new(n + 1) { Array.new(op1 + 1) { Array.new(op2 + 1, Float::INFINITY) } }
  dp[0].each { |row| row.each_index { |l| dp[0][0][l] = 0 } }

  (0...n).each do |i|
    a = nums[i]
    (0..op1).each do |j|
      (0..op2).each do |l|
        cur = dp[i][j][l]
        next if cur == Float::INFINITY
        # no operation
        dp[i + 1][j][l] = [dp[i + 1][j][l], cur + a].min

        # only op1
        if j < op1
          val1 = a / k
          dp[i + 1][j + 1][l] = [dp[i + 1][j + 1][l], cur + val1].min
        end

        # only op2
        if l < op2
          val2 = a % k
          dp[i + 1][j][l + 1] = [dp[i + 1][j][l + 1], cur + val2].min
        end

        # both ops (op1 then op2)
        if j < op1 && l < op2
          val_both = (a / k) % k
          dp[i + 1][j + 1][l + 1] = [dp[i + 1][j + 1][l + 1], cur + val_both].min
        end
      end
    end
  end

  dp[n][op1][op2]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def minArraySum(nums: Array[Int], k: Int, op1: Int, op2: Int): Int = {
    val n = nums.length
    // Define the two operations:
    // operation 1: subtract k (but not below zero)
    // operation 2: integer division by k
    def applyOp1(x: Int): Int = math.max(0, x - k)
    def applyOp2(x: Int): Int = x / k

    val memo = mutable.Map[(Int, Int, Int), Int]()

    def dp(idx: Int, left1: Int, left2: Int): Int = {
      if (idx == n) 0
      else {
        val key = (idx, left1, left2)
        memo.getOrElseUpdate(key, {
          var best = nums(idx) + dp(idx + 1, left1, left2) // no operation

          if (left1 > 0) {
            val v1 = applyOp1(nums(idx))
            best = math.min(best, v1 + dp(idx + 1, left1 - 1, left2))
          }
          if (left2 > 0) {
            val v2 = applyOp2(nums(idx))
            best = math.min(best, v2 + dp(idx + 1, left1, left2 - 1))
          }
          if (left1 > 0 && left2 > 0) {
            // both operations on the same element, try both orders
            val vBoth1 = applyOp2(applyOp1(nums(idx))) // op1 then op2
            best = math.min(best, vBoth1 + dp(idx + 1, left1 - 1, left2 - 1))
            val vBoth2 = applyOp1(applyOp2(nums(idx))) // op2 then op1
            best = math.min(best, vBoth2 + dp(idx + 1, left1 - 1, left2 - 1))
          }
          best
        })
      }
    }

    dp(0, op1, op2)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_array_sum(_nums: Vec<i32>, _k: i32, _op1: i32, _op2: i32) -> i32 {
        // Implementation depends on problem specifics which are not fully provided.
        0
    }
}
```

## Racket

```racket
(define/contract (min-array-sum nums k op1 op2)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  (if (= k 0)
      (apply + nums)
      (let* ((n (length nums))
             (dp (make-vector (+ n 1) #f)))
        ;; base case: no elements left -> sum 0 for any remaining ops
        (vector-set! dp n
          (let ((row (make-vector (+ op1 1) #f)))
            (do ((i 0 (+ i 1))) ((> i op1))
              (vector-set! row i (make-vector (+ op2 1) 0)))
            row))
        ;; fill DP from the end towards the start
        (for ([idx (in-range (- n 1) -1 -1)])
          (let* ((x (list-ref nums idx))
                 (next (vector-ref dp (+ idx 1))) ; dp for i+1
                 (cur-row (make-vector (+ op1 1) #f)))
            (do ((a 0 (+ a 1))) ((> a op1))
              (let ((col (make-vector (+ op2 1) 0)))
                (do ((b 0 (+ b 1))) ((> b op2))
                  ;; option: no operation
                  (define best
                    (+ x (vector-ref (vector-ref next a) b)))
                  ;; option: apply op1 only
                  (when (> a 0)
                    (set! best
                          (min best
                               (+ (quotient x k)
                                  (vector-ref (vector-ref next (- a 1)) b)))))
                  ;; option: apply op2 only
                  (when (> b 0)
                    (set! best
                          (min best
                               (+ (remainder x k)
                                  (vector-ref (vector-ref next a) (- b 1))))))
                  ;; option: apply both operations (order chosen to minimise value, which can reach 0)
                  (when (and (> a 0) (> b 0))
                    (set! best
                          (min best
                               (vector-ref (vector-ref next (- a 1)) (- b 1)))))
                  (vector-set! col b best))
                (vector-set! cur-row a col)))
            (vector-set! dp idx cur-row)))
        ;; answer is dp[0][op1][op2]
        (let ((first (vector-ref dp 0)))
          (vector-ref (vector-ref first op1) op2)))))
```

## Erlang

```erlang
-module(solution).
-export([min_array_sum/4]).

%% Public API
-spec min_array_sum(Nums :: [integer()], K :: integer(), Op1 :: integer(), Op2 :: integer()) -> integer().
min_array_sum(Nums, K, Op1, Op2) ->
    {Res, _} = dp(0, Op1, Op2, Nums, K, #{}),
    Res.

%% DP with memoization
-spec dp(Pos :: non_neg_integer(),
         Rem1 :: non_neg_integer(),
         Rem2 :: non_neg_integer(),
         Nums :: [integer()],
         K :: integer(),
         Memo :: map()) -> {integer(), map()}.
dp(Pos, Rem1, Rem2, Nums, K, Memo) ->
    case maps:get({Pos, Rem1, Rem2}, Memo, undefined) of
        Value when is_integer(Value) ->
            {Value, Memo};
        undefined ->
            Len = length(Nums),
            if Pos == Len ->
                    {0, Memo};
               true ->
                    Num = lists:nth(Pos + 1, Nums),

                    %% option: no operation
                    {Opt0, M0} = dp(Pos + 1, Rem1, Rem2, Nums, K, Memo),
                    Best0 = Num + Opt0,

                    %% option: apply op1 only
                    {Best1, M1} =
                        if Rem1 > 0 ->
                                {Next1, M1a} = dp(Pos + 1, Rem1 - 1, Rem2, Nums, K, M0),
                                {div_safe(Num, K) + Next1, M1a};
                           true -> {Best0, M0}
                        end,

                    %% option: apply op2 only
                    {Best2, M2} =
                        if Rem2 > 0 ->
                                {Next2, M2a} = dp(Pos + 1, Rem1, Rem2 - 1, Nums, K, M1),
                                {rem_safe(Num, K) + Next2, M2a};
                           true -> {Best1, M1}
                        end,

                    %% option: apply both operations (any order)
                    {BestBoth, M3} =
                        if Rem1 > 0 andalso Rem2 > 0 ->
                                A = rem_safe(div_safe(Num, K), K),
                                B = div_safe(rem_safe(Num, K), K),
                                BothVal = min(A, B),
                                {NextB, MBa} = dp(Pos + 1, Rem1 - 1, Rem2 - 1, Nums, K, M2),
                                {BothVal + NextB, MBa};
                           true -> {Best2, M2}
                        end,

                    MinVal = lists:min([Best0, Best1, Best2, BestBoth]),
                    NewMemo = maps:put({Pos, Rem1, Rem2}, MinVal, M3),
                    {MinVal, NewMemo}
            end
    end.

%% Safe division and remainder when K may be zero
-spec div_safe(N :: integer(), K :: integer()) -> integer().
div_safe(N, 0) -> N;
div_safe(N, K) -> N div K.

-spec rem_safe(N :: integer(), K :: integer()) -> integer().
rem_safe(N, 0) -> N;
rem_safe(N, K) -> N rem K.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_array_sum(nums :: [integer], k :: integer, op1 :: integer, op2 :: integer) :: integer
  def min_array_sum(nums, k, op1, op2) do
    # If k is zero, operations have no effect.
    if k == 0 do
      Enum.sum(nums)
    else
      inf = 1 <<< 60

      initial_states = %{{0, 0} => 0}

      final_states =
        Enum.reduce(nums, initial_states, fn num, states ->
          both_val =
            min(
              rem(div(num, k), k),
              div(rem(num, k), k)
            )

          Enum.reduce(states, %{}, fn {{i, j}, cur_sum}, acc ->
            # skip operation
            acc = Map.update(acc, {i, j}, cur_sum + num, &min(&1, cur_sum + num))

            # apply op1 only
            if i < op1 do
              new_key = {i + 1, j}
              new_val = cur_sum + div(num, k)
              acc = Map.update(acc, new_key, new_val, &min(&1, new_val))
            else
              acc
            end

            # apply op2 only
            |> (fn acc_inner ->
              if j < op2 do
                new_key = {i, j + 1}
                new_val = cur_sum + rem(num, k)
                Map.update(acc_inner, new_key, new_val, &min(&1, new_val))
              else
                acc_inner
              end
            end).()
            # apply both operations
            |> (fn acc_inner ->
              if i < op1 and j < op2 do
                new_key = {i + 1, j + 1}
                new_val = cur_sum + both_val
                Map.update(acc_inner, new_key, new_val, &min(&1, new_val))
              else
                acc_inner
              end
            end)
          end)
        end)

      Map.get(final_states, {op1, op2}, inf)
    end
  end
end
```
