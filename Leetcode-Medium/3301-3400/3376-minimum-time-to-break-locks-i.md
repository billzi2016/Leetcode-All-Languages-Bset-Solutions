# 3376. Minimum Time to Break Locks I

## Cpp

```cpp
class Solution {
public:
    int findMinimumTime(vector<int>& strength, int k) {
        return *max_element(strength.begin(), strength.end());
    }
};
```

## Java

```java
class Solution {
    public int findMinimumTime(List<Integer> strength, int k) {
        int n = strength.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = strength.get(i);
        int best = Integer.MAX_VALUE;
        // generate all permutations
        boolean[] used = new boolean[n];
        int[] perm = new int[n];
        java.util.ArrayDeque<int[]> stack = new java.util.ArrayDeque<>();
        stack.push(new int[]{0, 0}); // depth, current extra time (charges)
        while (!stack.isEmpty()) {
            int[] state = stack.pop();
            int depth = state[0];
            int extra = state[1];
            if (depth == n) {
                best = Math.min(best, n + extra);
                continue;
            }
            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    used[i] = true;
                    perm[depth] = arr[i];
                    int need = arr[i] - k * depth;
                    int newExtra = Math.max(extra, need);
                    stack.push(new int[]{depth + 1, newExtra});
                    used[i] = false;
                }
            }
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def findMinimumTime(self, strength, k):
        """
        :type strength: List[int]
        :type k: int
        :rtype: int
        """
        from itertools import permutations
        n = len(strength)
        best = float('inf')
        for perm in permutations(strength):
            total = 0
            power = 1
            for s in perm:
                total += (s + power - 1) // power
                if total >= best:  # prune
                    break
                power += k
            if total < best:
                best = total
        return best
```

## Python3

```python
class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        return max(strength)
```

## C

```c
int findMinimumTime(int* strength, int strengthSize, int k) {
    int n = strengthSize;
    int totalMask = 1 << n;
    const int INF = 0x3f3f3f3f;
    int *dp = (int*)malloc(totalMask * sizeof(int));
    for (int i = 0; i < totalMask; ++i) dp[i] = INF;
    dp[0] = 0;
    for (int mask = 0; mask < totalMask; ++mask) {
        int cnt = __builtin_popcount(mask);
        if (dp[mask] == INF) continue;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) {
                int need = strength[i] - k * cnt;
                if (need < 0) need = 0;
                int nxt = mask | (1 << i);
                if (dp[mask] + need < dp[nxt]) {
                    dp[nxt] = dp[mask] + need;
                }
            }
        }
    }
    int ans = dp[totalMask - 1];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int FindMinimumTime(IList<int> strength, int k) {
        int n = strength.Count;
        int totalMask = (1 << n) - 1;
        long INF = long.MaxValue / 4;
        long[] dp = new long[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = INF;
        dp[0] = 0;

        for (int mask = 0; mask <= totalMask; mask++) {
            if (dp[mask] == INF) continue;
            int broken = BitCount(mask);
            long power = 1L + (long)broken * k;
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << j)) != 0) continue;
                long cost = (strength[j] + power - 1) / power;
                int nextMask = mask | (1 << j);
                long newVal = dp[mask] + cost;
                if (newVal < dp[nextMask]) dp[nextMask] = newVal;
            }
        }

        return (int)dp[totalMask];
    }

    private int BitCount(int x) {
        int cnt = 0;
        while (x != 0) {
            cnt += x & 1;
            x >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} strength
 * @param {number} k
 * @return {number}
 */
var findMinimumTime = function(strength, k) {
    let maxVal = 0;
    for (let v of strength) {
        if (v > maxVal) maxVal = v;
    }
    return maxVal;
};
```

## Typescript

```typescript
function findMinimumTime(strength: number[], k: number): number {
    strength.sort((a, b) => b - a);
    let result = 0;
    for (let i = 0; i < strength.length; ++i) {
        const cur = strength[i] - i * k;
        if (cur > result) result = cur;
    }
    return Math.max(result, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $strength
     * @param Integer $k
     * @return Integer
     */
    function findMinimumTime($strength, $k) {
        $n = count($strength);
        $size = 1 << $n;
        $dp = array_fill(0, $size, PHP_INT_MAX);
        $dp[0] = 0;

        for ($mask = 0; $mask < $size; $mask++) {
            $curTime = $dp[$mask];
            if ($curTime === PHP_INT_MAX) continue;
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) != 0) continue;
                $remaining = $strength[$i] - $curTime * $k;
                if ($remaining < 0) $remaining = 0;
                $newTime = $curTime + $remaining;
                $nextMask = $mask | (1 << $i);
                if ($newTime < $dp[$nextMask]) {
                    $dp[$nextMask] = $newTime;
                }
            }
        }

        return $dp[$size - 1];
    }
}
```

## Swift

```swift
class Solution {
    func findMinimumTime(_ strength: [Int], _ k: Int) -> Int {
        let workers = k + 1
        var jobs = strength.sorted(by: >)
        var loads = Array(repeating: 0, count: workers)
        var best = Int.max
        
        func dfs(_ idx: Int) {
            if idx == jobs.count {
                if let cur = loads.max(), cur < best {
                    best = cur
                }
                return
            }
            // prune if current max already not better than best
            if let curMax = loads.max(), curMax >= best { return }
            
            var seen = Set<Int>()
            for i in 0..<workers {
                if seen.contains(loads[i]) { continue }   // skip symmetric states
                seen.insert(loads[i])
                
                loads[i] += jobs[idx]
                if loads[i] < best {
                    dfs(idx + 1)
                }
                loads[i] -= jobs[idx]
                
                // If this worker was empty before placing the job, no need to try other empty workers
                if loads[i] == 0 { break }
            }
        }
        
        dfs(0)
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinimumTime(strength: List<Int>, k: Int): Int {
        var sum = 0L
        for (v in strength) sum += v.toLong()
        var t = 0L
        while (t * (t + 1) / 2 < sum) {
            t++
        }
        return t.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int findMinimumTime(List<int> strength, int k) {
    int n = strength.length;
    int fullMask = (1 << n) - 1;
    const int INF = 1 << 60;
    List<int> dp = List.filled(1 << n, INF);
    dp[0] = 0;

    for (int mask = 0; mask <= fullMask; ++mask) {
      int curTime = dp[mask];
      if (curTime == INF) continue;
      // damage at the next minute
      int baseDamage = 1 + curTime * k;
      for (int i = 0; i < n; ++i) {
        if ((mask & (1 << i)) != 0) continue;
        int need = strength[i];
        int minutes = 0;
        int sum = 0;
        while (sum < need) {
          // damage during this minute
          int dmgThisMinute = baseDamage + minutes * k;
          sum += dmgThisMinute;
          minutes++;
        }
        int nextMask = mask | (1 << i);
        dp[nextMask] = dp[nextMask] < curTime + minutes ? dp[nextMask] : curTime + minutes;
      }
    }

    return dp[fullMask];
  }
}
```

## Golang

```go
func findMinimumTime(strength []int, k int) int {
    n := len(strength)
    maxStrength := 0
    for _, v := range strength {
        if v > maxStrength {
            maxStrength = v
        }
    }
    minByCapacity := (n + k - 1) / k
    if maxStrength > minByCapacity {
        return maxStrength
    }
    return minByCapacity
}
```

## Ruby

```ruby
def find_minimum_time(strength, k)
  n = strength.length
  total_masks = 1 << n
  popcnt = Array.new(total_masks, 0)
  (1...total_masks).each { |i| popcnt[i] = popcnt[i >> 1] + (i & 1) }

  dp = Array.new(total_masks, Float::INFINITY)
  dp[0] = 0

  (0...total_masks).each do |mask|
    cnt = popcnt[mask]
    denom = k + cnt
    n.times do |j|
      next if (mask & (1 << j)) != 0
      cost = (strength[j] + denom - 1) / denom
      new_mask = mask | (1 << j)
      val = dp[mask] + cost
      dp[new_mask] = val if val < dp[new_mask]
    end
  end

  dp[total_masks - 1].to_i
end
```

## Scala

```scala
object Solution {
    def findMinimumTime(strength: List[Int], k: Int): Int = {
        if (strength.isEmpty) 0 else strength.max
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_minimum_time(strength: Vec<i32>, k: i32) -> i32 {
        let n = strength.len();
        let mut order: Vec<usize> = (0..n).collect();
        let mut best: i64 = i64::MAX;

        fn backtrack(
            pos: usize,
            order: &mut [usize],
            strengths: &[i32],
            k: i32,
            cur: i64,
            best: &mut i64,
        ) {
            if pos == order.len() {
                if cur < *best {
                    *best = cur;
                }
                return;
            }
            for i in pos..order.len() {
                order.swap(pos, i);
                let s = strengths[order[pos]] as i64;
                let dmg = 1 + (pos as i32) * k;
                let add = (s + dmg as i64 - 1) / dmg as i64; // ceil division
                backtrack(pos + 1, order, strengths, k, cur + add, best);
                order.swap(pos, i);
            }
        }

        backtrack(0, &mut order, &strength, k, 0, &mut best);
        best as i32
    }
}
```

## Racket

```racket
(define/contract (find-minimum-time strength k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length strength))
         (arr (list->vector strength))
         (best (box +inf.0)))
    (define (dfs mask pos curmax)
      (if (= pos n)
          (when (< curmax (unbox best)) (set-box! best curmax))
          (for ([i (in-range n)])
            (when (= 0 (bitwise-and mask (arithmetic-shift 1 i)))
              (let* ((val (- (vector-ref arr i) (* pos k)))
                     (newmax (if (> val curmax) val curmax)))
                (when (< newmax (unbox best))
                  (dfs (bitwise-ior mask (arithmetic-shift 1 i)) (+ pos 1) newmax)))))))
    (dfs 0 0 -inf.0)
    (let ((ans (unbox best)))
      (if (< ans 0) 0 (exact-floor ans)))))
```

## Erlang

```erlang
-spec find_minimum_time(Strength :: [integer()], _K :: integer()) -> integer().
find_minimum_time(Strength, _K) ->
    lists:max(Strength).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_minimum_time(strength :: [integer], k :: integer) :: integer
  def find_minimum_time(strength, k) do
    {minute, _count} =
      strength
      |> Enum.sort()
      |> Enum.reduce({0, 0}, fn s, {min, cnt} ->
        if cnt == k or min < s do
          new_min = max(min + 1, s)
          {new_min, 1}
        else
          {min, cnt + 1}
        end
      end)

    minute
  end
end
```
