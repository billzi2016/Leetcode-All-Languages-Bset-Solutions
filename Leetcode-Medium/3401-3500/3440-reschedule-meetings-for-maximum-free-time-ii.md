# 3440. Reschedule Meetings for Maximum Free Time II

## Cpp

```cpp
class Solution {
public:
    int maxFreeTime(int eventTime, vector<int>& startTime, vector<int>& endTime) {
        int n = startTime.size();
        using ll = long long;
        vector<ll> gaps(n + 1);
        gaps[0] = (ll)startTime[0]; // before first meeting
        for (int i = 1; i < n; ++i) {
            gaps[i] = (ll)startTime[i] - endTime[i - 1];
        }
        gaps[n] = (ll)eventTime - endTime[n - 1]; // after last meeting

        vector<ll> prefMax(n + 1), suffMax(n + 1);
        prefMax[0] = gaps[0];
        for (int i = 1; i <= n; ++i) {
            prefMax[i] = max(prefMax[i - 1], gaps[i]);
        }
        suffMax[n] = gaps[n];
        for (int i = n - 1; i >= 0; --i) {
            suffMax[i] = max(suffMax[i + 1], gaps[i]);
        }

        ll ans = 0;
        // baseline: existing maximum gap without moving any meeting
        for (ll g : gaps) ans = max(ans, g);

        for (int i = 0; i < n; ++i) {
            ll dur = (ll)endTime[i] - startTime[i];
            ll leftBoundary = (i == 0 ? 0LL : endTime[i - 1]);
            ll rightBoundary = (i == n - 1 ? eventTime : startTime[i + 1]);

            // Case 2: merge adjacent free slots, meeting stays within merged region
            ll cand2 = (rightBoundary - leftBoundary) - dur;
            ans = max(ans, cand2);

            // Determine maximum non‑adjacent gap size
            int leftGapIdx = i;       // gap before meeting i
            int rightGapIdx = i + 1;  // gap after meeting i

            ll maxNonAdj = 0;
            if (leftGapIdx - 1 >= 0) {
                maxNonAdj = max(maxNonAdj, prefMax[leftGapIdx - 1]);
            }
            if (rightGapIdx + 1 <= n) {
                maxNonAdj = max(maxNonAdj, suffMax[rightGapIdx + 1]);
            }

            // Case 1: move meeting into a separate gap of sufficient size
            if (maxNonAdj >= dur) {
                ll cand1 = rightBoundary - leftBoundary;
                ans = max(ans, cand1);
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        int n = startTime.length;
        long[] gaps = new long[n + 1];
        // gap before first meeting
        gaps[0] = startTime[0];
        // gaps between meetings
        for (int i = 1; i < n; i++) {
            gaps[i] = (long) startTime[i] - endTime[i - 1];
        }
        // gap after last meeting
        gaps[n] = (long) eventTime - endTime[n - 1];

        long[] prefixMax = new long[n + 1];
        prefixMax[0] = gaps[0];
        for (int i = 1; i <= n; i++) {
            prefixMax[i] = Math.max(prefixMax[i - 1], gaps[i]);
        }

        long[] suffixMax = new long[n + 1];
        suffixMax[n] = gaps[n];
        for (int i = n - 1; i >= 0; i--) {
            suffixMax[i] = Math.max(suffixMax[i + 1], gaps[i]);
        }

        long best = 0;
        for (int i = 0; i < n; i++) {
            long dur = (long) endTime[i] - startTime[i];
            long left = (i == 0) ? 0L : endTime[i - 1];
            long right = (i == n - 1) ? eventTime : startTime[i + 1];

            // Case 2: merge adjacent free slots after removing meeting i
            long case2 = right - left - dur;
            if (case2 > best) best = case2;

            // Check if there exists a non‑adjacent gap large enough for the meeting
            boolean canCase1 = false;
            if (i > 0 && prefixMax[i - 1] >= dur) {
                canCase1 = true;
            }
            if (i + 2 <= n && suffixMax[i + 2] >= dur) {
                canCase1 = true;
            }

            if (canCase1) {
                long case1 = right - left; // the whole merged interval becomes free
                if (case1 > best) best = case1;
            }
        }
        return (int) best;
    }
}
```

## Python

```python
class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        # gaps G[0..n]: before first, between meetings, after last
        G = [0] * (n + 1)
        G[0] = startTime[0]                     # gap before first meeting
        for i in range(n - 1):
            G[i + 1] = startTime[i + 1] - endTime[i]   # between i and i+1
        G[n] = eventTime - endTime[-1]          # after last meeting

        # original maximum free interval
        ans = max(G)

        # prefix max of gaps
        pref = [0] * (n + 1)
        pref[0] = G[0]
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] if pref[i - 1] > G[i] else G[i]

        # suffix max of gaps
        suff = [0] * (n + 1)
        suff[n] = G[n]
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] if suff[i + 1] > G[i] else G[i]

        for i in range(n):
            dur = endTime[i] - startTime[i]
            left_gap = G[i]
            right_gap = G[i + 1]

            # case 2: merge adjacent gaps
            best = left_gap + right_gap

            # case 1 from left side (non‑adjacent gap)
            if i >= 2:
                max_left_nonadj = pref[i - 2]
                if dur <= max_left_nonadj:
                    cand = left_gap + dur + right_gap
                    if cand > best:
                        best = cand

            # case 1 from right side (non‑adjacent gap)
            if i + 2 <= n:
                max_right_nonadj = suff[i + 2]
                if dur <= max_right_nonadj:
                    cand = left_gap + dur + right_gap
                    if cand > best:
                        best = cand

            if best > ans:
                ans = best

        return ans
```

## Python3

```python
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        # durations of meetings
        dur = [endTime[i] - startTime[i] for i in range(n)]
        # gaps between meetings, including before first and after last
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]  # before first meeting
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[-1]  # after last meeting

        # original maximum free interval (no move)
        ans = max(gaps)

        # prefix and suffix maximums of gaps
        pref_max = [0] * (n + 1)
        pref_max[0] = gaps[0]
        for i in range(1, n + 1):
            pref_max[i] = pref_max[i - 1] if pref_max[i - 1] > gaps[i] else gaps[i]

        suff_max = [0] * (n + 1)
        suff_max[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            suff_max[i] = suff_max[i + 1] if suff_max[i + 1] > gaps[i] else gaps[i]

        for i in range(n):
            left_i = endTime[i - 1] if i > 0 else 0
            right_i = startTime[i + 1] if i < n - 1 else eventTime
            combined_len = right_i - left_i
            d = dur[i]

            # maximum non‑adjacent gap size
            max_left = pref_max[i - 1] if i - 1 >= 0 else 0
            max_right = suff_max[i + 2] if i + 2 <= n else 0
            max_non_adjacent = max_left if max_left > max_right else max_right

            if d <= max_non_adjacent:
                cand = combined_len          # case 1
            else:
                cand = combined_len - d      # case 2
            if cand > ans:
                ans = cand

        return ans
```

## C

```c
#include <stdlib.h>

int maxFreeTime(int eventTime, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    int n = startTimeSize;
    long long *gap = (long long *)malloc((n + 1) * sizeof(long long));
    if (!gap) return 0;

    gap[0] = (long long)startTime[0];                     // before first meeting
    for (int i = 1; i < n; ++i)
        gap[i] = (long long)startTime[i] - endTime[i - 1];
    gap[n] = (long long)eventTime - endTime[n - 1];       // after last meeting

    long long ans = 0;
    for (int i = 0; i <= n; ++i)
        if (gap[i] > ans) ans = gap[i];                  // current maximum free interval

    // Case 2: merge adjacent gaps while the moved meeting stays within them
    for (int i = 0; i < n; ++i) {
        long long merged = gap[i] + gap[i + 1];
        if (merged > ans) ans = merged;
    }

    // Left-to-right pass for Case 1 using a previous non‑adjacent gap
    long long bestLeftGap = 0;
    for (int i = 0; i < n; ++i) {
        long long dur = (long long)endTime[i] - startTime[i];
        if (dur <= bestLeftGap) {
            long long total = gap[i] + dur + gap[i + 1];
            if (total > ans) ans = total;
        }
        if (gap[i] > bestLeftGap) bestLeftGap = gap[i];
    }

    // Right-to-left pass for Case 1 using a later non‑adjacent gap
    long long bestRightGap = 0;
    for (int i = n - 1; i >= 0; --i) {
        long long dur = (long long)endTime[i] - startTime[i];
        if (dur <= bestRightGap) {
            long long total = gap[i] + dur + gap[i + 1];
            if (total > ans) ans = total;
        }
        if (gap[i + 1] > bestRightGap) bestRightGap = gap[i + 1];
    }

    free(gap);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        int n = startTime.Length;
        long[] gaps = new long[n + 1];
        // gap before first meeting
        gaps[0] = startTime[0];
        for (int i = 1; i < n; i++) {
            gaps[i] = (long)startTime[i] - endTime[i - 1];
        }
        // gap after last meeting
        gaps[n] = (long)eventTime - endTime[n - 1];

        long maxGap = 0;
        foreach (var g in gaps) if (g > maxGap) maxGap = g;

        long ans = maxGap;

        // Precompute left_i, right_i, duration for each meeting
        long[] left = new long[n];
        long[] right = new long[n];
        long[] dur = new long[n];

        for (int i = 0; i < n; i++) {
            dur[i] = (long)endTime[i] - startTime[i];
            left[i] = (i == 0) ? 0L : endTime[i - 1];
            right[i] = (i == n - 1) ? eventTime : startTime[i + 1];

            long candidate2 = right[i] - left[i] - dur[i];
            if (candidate2 > ans) ans = candidate2;
        }

        // Left to right pass
        long t1 = long.MinValue;
        for (int i = 0; i < n; i++) {
            if (dur[i] <= t1) {
                long cand = right[i] - left[i];
                if (cand > ans) ans = cand;
            }
            // gap before meeting i becomes non‑adjacent for future meetings
            t1 = Math.Max(t1, gaps[i]);
        }

        // Right to left pass
        long t2 = long.MinValue;
        for (int i = n - 1; i >= 0; i--) {
            if (dur[i] <= t2) {
                long cand = right[i] - left[i];
                if (cand > ans) ans = cand;
            }
            // gap after meeting i becomes non‑adjacent for earlier meetings
            t2 = Math.Max(t2, gaps[i + 1]);
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} eventTime
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @return {number}
 */
var maxFreeTime = function(eventTime, startTime, endTime) {
    const n = startTime.length;
    const gaps = new Array(n + 1);
    // gap before first meeting
    gaps[0] = startTime[0];
    // gaps between meetings
    for (let i = 1; i < n; ++i) {
        gaps[i] = startTime[i] - endTime[i - 1];
    }
    // gap after last meeting
    gaps[n] = eventTime - endTime[n - 1];

    let ans = 0;
    for (let g of gaps) if (g > ans) ans = g;

    const prefMax = new Array(n + 1);
    prefMax[0] = gaps[0];
    for (let i = 1; i <= n; ++i) {
        prefMax[i] = Math.max(prefMax[i - 1], gaps[i]);
    }

    const suffMax = new Array(n + 1);
    suffMax[n] = gaps[n];
    for (let i = n - 1; i >= 0; --i) {
        suffMax[i] = Math.max(suffMax[i + 1], gaps[i]);
    }

    for (let i = 0; i < n; ++i) {
        const dur = endTime[i] - startTime[i];
        const leftGap = gaps[i];
        const rightGap = gaps[i + 1];

        // Case 2: merge adjacent free slots
        const merged = leftGap + rightGap;
        if (merged > ans) ans = merged;

        // Find the largest non‑adjacent gap
        let maxNonAdj = 0;
        if (i - 2 >= 0) maxNonAdj = Math.max(maxNonAdj, prefMax[i - 2]);
        if (i + 2 <= n) maxNonAdj = Math.max(maxNonAdj, suffMax[i + 2]);

        // Case 1: move meeting into a separate gap
        if (maxNonAdj >= dur) {
            const newFree = leftGap + dur + rightGap; // equals right_i - left_i
            if (newFree > ans) ans = newFree;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxFreeTime(eventTime: number, startTime: number[], endTime: number[]): number {
    const n = startTime.length;
    const gaps = new Array<number>(n + 1);
    // gap before first meeting
    gaps[0] = startTime[0];
    for (let i = 0; i < n - 1; ++i) {
        gaps[i + 1] = startTime[i + 1] - endTime[i];
    }
    // gap after last meeting
    gaps[n] = eventTime - endTime[n - 1];

    let ans = 0;
    for (const g of gaps) if (g > ans) ans = g;

    // Case 2: merge adjacent free slots by removing the meeting
    for (let i = 0; i < n; ++i) {
        const left = i === 0 ? 0 : endTime[i - 1];
        const right = i === n - 1 ? eventTime : startTime[i + 1];
        const dur = endTime[i] - startTime[i];
        const merged = right - left - dur; // equals gaps[i] + gaps[i+1]
        if (merged > ans) ans = merged;
    }

    // Left-to-right pass for Case 1 (move to a non‑adjacent earlier gap)
    let maxLeftGap = 0;
    for (let i = 0; i < n; ++i) {
        const left = i === 0 ? 0 : endTime[i - 1];
        const right = i === n - 1 ? eventTime : startTime[i + 1];
        const dur = endTime[i] - startTime[i];
        if (dur <= maxLeftGap) {
            const cand = right - left;
            if (cand > ans) ans = cand;
        }
        // gap[i] becomes non‑adjacent for future meetings
        if (gaps[i] > maxLeftGap) maxLeftGap = gaps[i];
    }

    // Right-to-left pass for Case 1 (move to a non‑adjacent later gap)
    let maxRightGap = 0;
    for (let i = n - 1; i >= 0; --i) {
        const left = i === 0 ? 0 : endTime[i - 1];
        const right = i === n - 1 ? eventTime : startTime[i + 1];
        const dur = endTime[i] - startTime[i];
        if (dur <= maxRightGap) {
            const cand = right - left;
            if (cand > ans) ans = cand;
        }
        // gap[i+1] becomes non‑adjacent for earlier meetings
        if (gaps[i + 1] > maxRightGap) maxRightGap = gaps[i + 1];
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $eventTime
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @return Integer
     */
    function maxFreeTime($eventTime, $startTime, $endTime) {
        $n = count($startTime);
        // gaps between meetings, including leading and trailing gaps
        $gaps = [];
        $gaps[0] = $startTime[0]; // leading gap
        for ($i = 1; $i < $n; $i++) {
            $gaps[$i] = $startTime[$i] - $endTime[$i - 1];
        }
        $gaps[$n] = $eventTime - $endTime[$n - 1]; // trailing gap
        $m = $n; // last index of gaps

        // prefix max of gaps
        $pref = [];
        $curMax = 0;
        for ($i = 0; $i <= $m; $i++) {
            if ($gaps[$i] > $curMax) $curMax = $gaps[$i];
            $pref[$i] = $curMax;
        }
        // suffix max of gaps
        $suff = [];
        $curMax = 0;
        for ($i = $m; $i >= 0; $i--) {
            if ($gaps[$i] > $curMax) $curMax = $gaps[$i];
            $suff[$i] = $curMax;
        }

        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $duration = $endTime[$i] - $startTime[$i];
            $left = ($i == 0) ? 0 : $endTime[$i - 1];
            $right = ($i == $n - 1) ? $eventTime : $startTime[$i + 1];

            // Case 2: move within adjacent interval, merging gaps
            $candidate = $right - $left - $duration;
            if ($candidate > $ans) $ans = $candidate;

            // Find maximum non‑adjacent gap length
            $maxNonAdj = 0;
            $idxLeft = $i - 2;               // gaps before the left adjacent gap
            if ($idxLeft >= 0) {
                $maxNonAdj = $pref[$idxLeft];
            }
            $idxRight = $i + 2;              // gaps after the right adjacent gap
            if ($idxRight <= $m) {
                $val = $suff[$idxRight];
                if ($val > $maxNonAdj) $maxNonAdj = $val;
            }

            // Case 1: move to a non‑adjacent free slot
            if ($maxNonAdj >= $duration) {
                $candidate = $right - $left; // whole interval becomes free
                if ($candidate > $ans) $ans = $candidate;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxFreeTime(_ eventTime: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        if n == 0 { return eventTime }
        var gaps = [Int](repeating: 0, count: n + 1)
        gaps[0] = startTime[0]
        for i in 1..<n {
            gaps[i] = startTime[i] - endTime[i - 1]
        }
        gaps[n] = eventTime - endTime[n - 1]
        
        var answer = gaps.max() ?? 0
        
        // Case 2: merge adjacent free slots and subtract meeting duration
        for i in 0..<n {
            let leftEnd = (i == 0) ? 0 : endTime[i - 1]
            let rightStart = (i == n - 1) ? eventTime : startTime[i + 1]
            let dur = endTime[i] - startTime[i]
            let cand = (rightStart - leftEnd) - dur
            if cand > answer { answer = cand }
        }
        
        // Case 1: move meeting into a non‑adjacent free slot (left side)
        var maxLeftGap = -1
        for i in 0..<n {
            let dur = endTime[i] - startTime[i]
            let leftEnd = (i == 0) ? 0 : endTime[i - 1]
            let rightStart = (i == n - 1) ? eventTime : startTime[i + 1]
            if maxLeftGap >= dur {
                let cand = rightStart - leftEnd
                if cand > answer { answer = cand }
            }
            if i >= 1 {
                // gap[i-1] becomes non‑adjacent for future meetings
                maxLeftGap = max(maxLeftGap, gaps[i - 1])
            }
        }
        
        // Case 1: move meeting into a non‑adjacent free slot (right side)
        var maxRightGap = -1
        for i in stride(from: n - 1, through: 0, by: -1) {
            let dur = endTime[i] - startTime[i]
            let leftEnd = (i == 0) ? 0 : endTime[i - 1]
            let rightStart = (i == n - 1) ? eventTime : startTime[i + 1]
            if maxRightGap >= dur {
                let cand = rightStart - leftEnd
                if cand > answer { answer = cand }
            }
            // gap[i+1] becomes non‑adjacent for earlier meetings
            maxRightGap = max(maxRightGap, gaps[i + 1])
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFreeTime(eventTime: Int, startTime: IntArray, endTime: IntArray): Int {
        val n = startTime.size
        val gaps = IntArray(n + 1)
        gaps[0] = startTime[0]
        for (i in 1 until n) {
            gaps[i] = startTime[i] - endTime[i - 1]
        }
        gaps[n] = eventTime - endTime[n - 1]

        var ans = 0
        // existing maximum gap
        for (g in gaps) if (g > ans) ans = g

        // case 2: merge adjacent free slots after moving meeting elsewhere
        for (i in 0 until n) {
            val cand = gaps[i] + gaps[i + 1]
            if (cand > ans) ans = cand
        }

        // left to right pass for case 1
        var maxLeftGap = 0
        for (i in 0 until n) {
            val dur = endTime[i] - startTime[i]
            if (dur <= maxLeftGap) {
                val cand = gaps[i] + gaps[i + 1] + dur
                if (cand > ans) ans = cand
            }
            if (gaps[i] > maxLeftGap) maxLeftGap = gaps[i]
        }

        // right to left pass for case 1
        var maxRightGap = 0
        for (i in n - 1 downTo 0) {
            val dur = endTime[i] - startTime[i]
            if (dur <= maxRightGap) {
                val cand = gaps[i] + gaps[i + 1] + dur
                if (cand > ans) ans = cand
            }
            if (gaps[i + 1] > maxRightGap) maxRightGap = gaps[i + 1]
        }

        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxFreeTime(int eventTime, List<int> startTime, List<int> endTime) {
    int n = startTime.length;
    // gaps between meetings and at the ends
    List<int> gaps = List.filled(n + 1, 0);
    gaps[0] = startTime[0];
    for (int i = 1; i < n; ++i) {
      gaps[i] = startTime[i] - endTime[i - 1];
    }
    gaps[n] = eventTime - endTime[n - 1];

    // prefix max of gaps
    List<int> pref = List.filled(n + 1, 0);
    pref[0] = gaps[0];
    for (int i = 1; i <= n; ++i) {
      pref[i] = max(pref[i - 1], gaps[i]);
    }

    // suffix max of gaps
    List<int> suff = List.filled(n + 1, 0);
    suff[n] = gaps[n];
    for (int i = n - 1; i >= 0; --i) {
      suff[i] = max(suff[i + 1], gaps[i]);
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int leftGap = gaps[i];
      int rightGap = gaps[i + 1];
      int dur = endTime[i] - startTime[i];

      // Case 2: merge adjacent free slots after moving meeting elsewhere
      ans = max(ans, leftGap + rightGap);

      // Case 1: move meeting into a non‑adjacent gap on the left
      if (i >= 2 && dur <= pref[i - 2]) {
        ans = max(ans, leftGap + dur + rightGap);
      }
      // Case 1: move meeting into a non‑adjacent gap on the right
      if (i + 2 <= n && dur <= suff[i + 2]) {
        ans = max(ans, leftGap + dur + rightGap);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
    n := len(startTime)
    // gaps between meetings, including before first and after last
    gaps := make([]int, n+1)
    gaps[0] = startTime[0]
    for i := 1; i < n; i++ {
        gaps[i] = startTime[i] - endTime[i-1]
    }
    gaps[n] = eventTime - endTime[n-1]

    // prefix max of gaps
    pref := make([]int, n+1)
    curMax := 0
    for i := 0; i <= n; i++ {
        if gaps[i] > curMax {
            curMax = gaps[i]
        }
        pref[i] = curMax
    }

    // suffix max of gaps
    suff := make([]int, n+2) // extra element to avoid bounds check
    curMax = 0
    for i := n; i >= 0; i-- {
        if gaps[i] > curMax {
            curMax = gaps[i]
        }
        suff[i] = curMax
    }

    ans := 0
    for _, g := range gaps {
        if g > ans {
            ans = g
        }
    }

    for i := 0; i < n; i++ {
        dur := endTime[i] - startTime[i]

        // move into left adjacent gap
        if gaps[i] >= dur {
            cand := gaps[i+1] + dur
            if cand > ans {
                ans = cand
            }
        }
        // move into right adjacent gap
        if gaps[i+1] >= dur {
            cand := gaps[i] + dur
            if cand > ans {
                ans = cand
            }
        }

        // check for any non‑adjacent gap large enough
        leftMax := -1
        if i-2 >= 0 {
            leftMax = pref[i-2]
        }
        rightMax := -1
        if i+2 <= n {
            rightMax = suff[i+2]
        }
        if leftMax >= dur || rightMax >= dur {
            cand := gaps[i] + dur + gaps[i+1]
            if cand > ans {
                ans = cand
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_free_time(event_time, start_time, end_time)
  n = start_time.length
  gaps = Array.new(n + 1, 0)
  gaps[0] = start_time[0]
  (1...n).each do |i|
    gaps[i] = start_time[i] - end_time[i - 1]
  end
  gaps[n] = event_time - end_time[n - 1]

  pref = Array.new(n + 1, 0)
  pref[0] = gaps[0]
  (1..n).each do |i|
    pref[i] = pref[i - 1] > gaps[i] ? pref[i - 1] : gaps[i]
  end

  suff = Array.new(n + 1, 0)
  suff[n] = gaps[n]
  (n - 1).downto(0) do |i|
    suff[i] = suff[i + 1] > gaps[i] ? suff[i + 1] : gaps[i]
  end

  ans = gaps.max
  n.times do |i|
    left_i = i.zero? ? 0 : end_time[i - 1]
    right_i = (i == n - 1) ? event_time : start_time[i + 1]
    dur = end_time[i] - start_time[i]

    cand2 = right_i - left_i - dur
    ans = cand2 if cand2 > ans

    left_max = i - 1 >= 0 ? pref[i - 1] : 0
    right_max = i + 2 <= n ? suff[i + 2] : 0
    if left_max >= dur || right_max >= dur
      cand1 = right_i - left_i
      ans = cand1 if cand1 > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxFreeTime(eventTime: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
        val n = startTime.length
        // gaps between meetings and edges, size n+1
        val gaps = new Array[Int](n + 1)
        gaps(0) = startTime(0)                     // from time 0 to first meeting
        var i = 1
        while (i < n) {
            gaps(i) = startTime(i) - endTime(i - 1) // between meetings
            i += 1
        }
        gaps(n) = eventTime - endTime(n - 1)       // after last meeting

        var ans = 0
        i = 0
        while (i <= n) {
            if (gaps(i) > ans) ans = gaps(i)      // existing free interval
            i += 1
        }

        // prefix max of gaps
        val pref = new Array[Int](n + 1)
        var cur = 0
        i = 0
        while (i <= n) {
            if (gaps(i) > cur) cur = gaps(i)
            pref(i) = cur
            i += 1
        }

        // suffix max of gaps
        val suff = new Array[Int](n + 1)
        cur = 0
        i = n
        while (i >= 0) {
            if (gaps(i) > cur) cur = gaps(i)
            suff(i) = cur
            i -= 1
        }

        // evaluate each meeting
        i = 0
        while (i < n) {
            val dur = endTime(i) - startTime(i)

            // case 2: merge adjacent free slots
            val adjSum = gaps(i) + gaps(i + 1)
            if (adjSum > ans) ans = adjSum

            // check for a non‑adjacent gap large enough
            var maxOther = 0
            if (i - 2 >= 0 && pref(i - 2) > maxOther) maxOther = pref(i - 2)
            if (i + 2 <= n && suff(i + 2) > maxOther) maxOther = suff(i + 2)

            if (maxOther >= dur) {
                // case 1: free the whole span around this meeting
                val total = gaps(i) + dur + gaps(i + 1)
                if (total > ans) ans = total
            }

            i += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_free_time(event_time: i32, start_time: Vec<i32>, end_time: Vec<i32>) -> i32 {
        let n = start_time.len();
        // gaps between meetings, including before first and after last
        let mut gaps = vec![0i32; n + 1];
        gaps[0] = start_time[0];
        for i in 1..n {
            gaps[i] = start_time[i] - end_time[i - 1];
        }
        gaps[n] = event_time - end_time[n - 1];

        // initial answer: longest existing free interval
        let mut ans = *gaps.iter().max().unwrap();

        // case 2: move meeting into an adjacent gap, merging the two sides
        for i in 0..n {
            let left = if i == 0 { 0 } else { end_time[i - 1] };
            let right = if i + 1 == n { event_time } else { start_time[i + 1] };
            let dur = end_time[i] - start_time[i];
            ans = ans.max(right - left - dur);
        }

        // case 1: move meeting into a non‑adjacent gap (left side)
        let mut max_left_gap = 0i32;
        for i in 0..n {
            if i >= 2 {
                max_left_gap = max_left_gap.max(gaps[i - 2]);
            }
            let dur = end_time[i] - start_time[i];
            if dur <= max_left_gap {
                let left = if i == 0 { 0 } else { end_time[i - 1] };
                let right = if i + 1 == n { event_time } else { start_time[i + 1] };
                ans = ans.max(right - left);
            }
        }

        // case 1: move meeting into a non‑adjacent gap (right side)
        let mut max_right_gap = 0i32;
        for i in (0..n).rev() {
            if i + 2 <= n {
                max_right_gap = max_right_gap.max(gaps[i + 2]);
            }
            let dur = end_time[i] - start_time[i];
            if dur <= max_right_gap {
                let left = if i == 0 { 0 } else { end_time[i - 1] };
                let right = if i + 1 == n { event_time } else { start_time[i + 1] };
                ans = ans.max(right - left);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-free-time eventTime startTime endTime)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length startTime))
         (s (list->vector startTime))
         (e (list->vector endTime)))
    (define ans 0)
    (define t1 0) ; max non‑adjacent gap on the left
    ;; left‑to‑right pass
    (let loop ((i 0))
      (when (< i n)
        (let* ((dur (- (vector-ref e i) (vector-ref s i)))
               (left-end (if (= i 0) 0 (vector-ref e (- i 1))))
               (right-start (if (= i (- n 1)) eventTime (vector-ref s (+ i 1)))))
          ;; case 2: merge adjacent free slots
          (let ((case2 (- (- right-start left-end) dur)))
            (when (> case2 ans) (set! ans case2)))
          ;; case 1 using a left non‑adjacent gap
          (when (<= dur t1)
            (let ((cand (- right-start left-end)))
              (when (> cand ans) (set! ans cand))))
          ;; update t1 with the gap immediately after this meeting
          (when (< i (- n 1))
            (let ((gap (- (vector-ref s (+ i 1)) (vector-ref e i))))
              (when (> gap t1) (set! t1 gap)))))
        (loop (+ i 1))))
    ;; right‑to‑left pass for non‑adjacent gaps on the right
    (define t2 0)
    (let loop ((i (- n 1)))
      (when (>= i 0)
        (let* ((dur (- (vector-ref e i) (vector-ref s i)))
               (left-end (if (= i 0) 0 (vector-ref e (- i 1))))
               (right-start (if (= i (- n 1)) eventTime (vector-ref s (+ i 1)))))
          ;; case 1 using a right non‑adjacent gap
          (when (<= dur t2)
            (let ((cand (- right-start left-end)))
              (when (> cand ans) (set! ans cand))))
          ;; update t2 with the gap immediately before this meeting
          (when (> i 0)
            (let ((gap (- (vector-ref s i) (vector-ref e (- i 1)))))
              (when (> gap t2) (set! t2 gap)))))
        (loop (- i 1))))
    ans))
```

## Erlang

```erlang
-spec max_free_time(EventTime :: integer(), StartTime :: [integer()], EndTime :: [integer()]) -> integer().
max_free_time(EventTime, StartTime, EndTime) ->
    % convert lists to tuples for O(1) indexing
    StT = list_to_tuple(StartTime),
    EtT = list_to_tuple(EndTime),
    N = tuple_size(StT),

    % build gaps: before first, between meetings, after last
    GapsList = build_gaps(StartTime, EndTime, EventTime),
    GapT = list_to_tuple(GapsList),
    M = tuple_size(GapT),               % M = N + 1

    % prefix max of gaps
    PrefT = build_prefix_max(GapT),
    % suffix max of gaps
    SuffT = build_suffix_max(GapT),

    % initial answer: maximum existing gap
    MaxGap = element(M, PrefT),
    Ans0 = MaxGap,

    % iterate over meetings
    Answer = loop_meetings(0, N-1, EventTime, StT, EtT, GapT, PrefT, SuffT, Ans0),
    Answer.

%% Build gaps list: before first, between each pair, after last
build_gaps([], [], _Event) -> [];
build_gaps([S|Ss], [E|Es], Event) ->
    build_gaps_helper(Ss, Es, S, E, Event, [S - 0]).

build_gaps_helper([], [], PrevStart, PrevEnd, Event, Acc) ->
    % last gap after the final meeting
    lists:reverse([Event - PrevEnd | Acc]);
build_gaps_helper([S|Ss], [E|Es], _PrevStart, PrevEnd, Event, Acc) ->
    Gap = S - PrevEnd,
    build_gaps_helper(Ss, Es, S, E, Event, [Gap | Acc]).

%% Prefix max tuple
build_prefix_max(GapT) ->
    Size = tuple_size(GapT),
    build_prefix_max(1, Size, GapT, []).

build_prefix_max(Index, Size, _GapT, Acc) when Index > Size ->
    list_to_tuple(lists:reverse(Acc));
build_prefix_max(Index, Size, GapT, Acc) ->
    Gap = element(Index, GapT),
    PrevMax = case Acc of
        [] -> 0;
        [Prev|_] -> Prev
    end,
    NewMax = erlang:max(Gap, PrevMax),
    build_prefix_max(Index + 1, Size, GapT, [NewMax | Acc]).

%% Suffix max tuple
build_suffix_max(GapT) ->
    Size = tuple_size(GapT),
    build_suffix_max(Size, GapT, []).

build_suffix_max(0, _GapT, Acc) ->
    list_to_tuple(lists:reverse(Acc));
build_suffix_max(Index, GapT, Acc) ->
    Gap = element(Index, GapT),
    PrevMax = case Acc of
        [] -> 0;
        [Prev|_] -> Prev
    end,
    NewMax = erlang:max(Gap, PrevMax),
    build_suffix_max(Index - 1, GapT, [NewMax | Acc]).

%% Main loop over meetings
loop_meetings(I, NMinusOne, _Event, _StT, _EtT, _GapT, _PrefT, _SuffT, Ans) when I > NMinusOne ->
    Ans;
loop_meetings(I, NMinusOne, Event, StT, EtT, GapT, PrefT, SuffT, Ans) ->
    % durations and neighboring times
    StartI = element(I + 1, StT),
    EndI   = element(I + 1, EtT),
    Dur    = EndI - StartI,

    PrevEnd = case I of
        0 -> 0;
        _ -> element(I, EtT)          % end of previous meeting (index I-1)
    end,
    NextStart = case I of
        NMinusOne -> Event;
        _ -> element(I + 2, StT)      % start of next meeting (index I+1)
    end,

    Span = NextStart - PrevEnd,
    Case2 = Span - Dur,
    NewAns1 = erlang:max(Ans, Case2),

    % compute max_other gap not adjacent
    M = tuple_size(GapT),
    MaxLeft = if I >= 2 -> element(I - 1, PrefT); true -> 0 end,
    MaxRight = if (I + 2) < M -> element(I + 3, SuffT); true -> 0 end,
    MaxOther = erlang:max(MaxLeft, MaxRight),

    NewAns = if MaxOther >= Dur ->
                 erlang:max(NewAns1, Span);
             true ->
                 NewAns1
             end,

    loop_meetings(I + 1, NMinusOne, Event, StT, EtT, GapT, PrefT, SuffT, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_free_time(event_time :: integer, start_time :: [integer], end_time :: [integer]) :: integer
  def max_free_time(event_time, start_time, end_time) do
    n = length(start_time)
    s = List.to_tuple(start_time)
    e = List.to_tuple(end_time)

    # build gaps array of size n+1
    gap0 = elem(s, 0)
    middle_gaps =
      for i <- 1..(n - 1) do
        elem(s, i) - elem(e, i - 1)
      end

    last_gap = event_time - elem(e, n - 1)
    gaps_list = [gap0] ++ middle_gaps ++ [last_gap]
    gaps = List.to_tuple(gaps_list)

    # initial answer: maximum existing free interval
    init_ans = Enum.max(gaps_list)

    # left-to-right pass (handles case2 and case1 using left side)
    {ans_left, _t1} =
      Enum.reduce(0..(n - 1), {init_ans, -1}, fn i, {cur_ans, t1} ->
        dur = elem(e, i) - elem(s, i)

        prev_end =
          if i == 0 do
            0
          else
            elem(e, i - 1)
          end

        next_start =
          if i == n - 1 do
            event_time
          else
            elem(s, i + 1)
          end

        # case2: merge adjacent free slots while keeping the meeting
        cur_ans = max(cur_ans, next_start - prev_end - dur)

        # case1 using a non‑adjacent left gap if possible
        cur_ans =
          if t1 >= dur do
            max(cur_ans, next_start - prev_end)
          else
            cur_ans
          end

        # update t1 with the current left gap (becomes non‑adjacent for later meetings)
        gap_i = elem(gaps, i)
        new_t1 = if gap_i > t1, do: gap_i, else: t1

        {cur_ans, new_t1}
      end)

    # right-to-left pass (handles case1 using right side)
    final_ans =
      Enum.reduce(Enum.to_list(0..(n - 1)) |> Enum.reverse, {ans_left, -1}, fn i,
                                                                            {cur_ans, t2} ->
        dur = elem(e, i) - elem(s, i)

        prev_end =
          if i == 0 do
            0
          else
            elem(e, i - 1)
          end

        next_start =
          if i == n - 1 do
            event_time
          else
            elem(s, i + 1)
          end

        # case1 using a non‑adjacent right gap if possible
        cur_ans =
          if t2 >= dur do
            max(cur_ans, next_start - prev_end)
          else
            cur_ans
          end

        # update t2 with the current right gap (becomes non‑adjacent for earlier meetings)
        gap_ip1 = elem(gaps, i + 1)
        new_t2 = if gap_ip1 > t2, do: gap_ip1, else: t2

        {cur_ans, new_t2}
      end)
      |> elem(0)

    final_ans
  end
end
```
