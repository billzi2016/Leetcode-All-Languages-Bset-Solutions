# 3635. Earliest Finish Time for Land and Water Rides II

## Cpp

```cpp
class Solution {
public:
    struct Ride {
        int start;
        int dur;
    };
    
    long long solve(const vector<int>& startsA, const vector<int>& dursA,
                    const vector<int>& startsB, const vector<int>& dursB) {
        int n = startsA.size();
        int m = startsB.size();
        vector<Ride> A(n), B(m);
        for (int i = 0; i < n; ++i) A[i] = {startsA[i], dursA[i]};
        for (int i = 0; i < m; ++i) B[i] = {startsB[i], dursB[i]};
        
        sort(A.begin(), A.end(), [](const Ride& x, const Ride& y){ return x.start < y.start; });
        sort(B.begin(), B.end(), [](const Ride& x, const Ride& y){ return x.start < y.start; });
        
        vector<int> bStarts(m);
        for (int i = 0; i < m; ++i) bStarts[i] = B[i].start;
        
        // prefix minimum of durations in B
        vector<int> prefMinDur(m);
        for (int i = 0; i < m; ++i) {
            if (i == 0) prefMinDur[i] = B[i].dur;
            else prefMinDur[i] = min(prefMinDur[i-1], B[i].dur);
        }
        // suffix minimum of finish times in B
        const long long INF = (1LL<<60);
        vector<long long> suffMinFinish(m + 1, INF);
        for (int i = m - 1; i >= 0; --i) {
            long long fin = (long long)B[i].start + B[i].dur;
            suffMinFinish[i] = min(suffMinFinish[i+1], fin);
        }
        
        long long best = INF;
        for (const auto& a : A) {
            long long finishA = (long long)a.start + a.dur;
            int idx = upper_bound(bStarts.begin(), bStarts.end(), finishA) - bStarts.begin(); // first > finishA
            long long cur = INF;
            if (idx > 0) { // there are rides with start <= finishA
                cur = min(cur, finishA + prefMinDur[idx-1]);
            }
            // rides with start > finishA
            cur = min(cur, suffMinFinish[idx]);
            best = min(best, cur);
        }
        return best;
    }
    
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration,
                           vector<int>& waterStartTime, vector<int>& waterDuration) {
        long long ans1 = solve(landStartTime, landDuration, waterStartTime, waterDuration); // land then water
        long long ans2 = solve(waterStartTime, waterDuration, landStartTime, landDuration); // water then land
        long long ans = min(ans1, ans2);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration,
                                  int[] waterStartTime, int[] waterDuration) {
        return Math.min(
                computeMinFinish(landStartTime, landDuration, waterStartTime, waterDuration),
                computeMinFinish(waterStartTime, waterDuration, landStartTime, landDuration)
        );
    }

    private int computeMinFinish(int[] startA, int[] durA,
                                 int[] startB, int[] durB) {
        int n = startB.length;
        // sort rides of B by start time
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        java.util.Arrays.sort(idx, (i, j) -> Integer.compare(startB[i], startB[j]));

        int[] sortedStartB = new int[n];
        int[] sortedDurB = new int[n];
        for (int i = 0; i < n; i++) {
            sortedStartB[i] = startB[idx[i]];
            sortedDurB[i] = durB[idx[i]];
        }

        // prefix minimum of duration
        int[] prefMinDur = new int[n];
        prefMinDur[0] = sortedDurB[0];
        for (int i = 1; i < n; i++) {
            prefMinDur[i] = Math.min(prefMinDur[i - 1], sortedDurB[i]);
        }

        // suffix minimum of finish time (start + duration)
        int[] suffMinFinish = new int[n];
        suffMinFinish[n - 1] = sortedStartB[n - 1] + sortedDurB[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMinFinish[i] = Math.min(suffMinFinish[i + 1],
                    sortedStartB[i] + sortedDurB[i]);
        }

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < startA.length; i++) {
            int finishFirst = startA[i] + durA[i];
            int idxUpper = upperBound(sortedStartB, finishFirst); // first start > finishFirst

            int best = Integer.MAX_VALUE;
            if (idxUpper > 0) { // there are rides with start <= finishFirst
                best = Math.min(best, finishFirst + prefMinDur[idxUpper - 1]);
            }
            if (idxUpper < n) { // there are rides with start > finishFirst
                best = Math.min(best, suffMinFinish[idxUpper]);
            }
            answer = Math.min(answer, best);
        }
        return answer;
    }

    private int upperBound(int[] arr, int target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int mid = (l + r) >>> 1;
            if (arr[mid] <= target) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}
```

## Python

```python
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        import bisect

        def min_finish(first_start, first_dur, second_start, second_dur):
            # sort second rides by start time
            paired = sorted(zip(second_start, second_dur))
            starts = [p[0] for p in paired]
            durs = [p[1] for p in paired]
            n = len(starts)

            # prefix minimum of durations
            pref_min_dur = [0] * n
            cur = float('inf')
            for i in range(n):
                if durs[i] < cur:
                    cur = durs[i]
                pref_min_dur[i] = cur

            # suffix minimum of finish times (start + duration)
            suff_min_finish = [float('inf')] * (n + 1)   # extra sentinel at end
            cur = float('inf')
            for i in range(n - 1, -1, -1):
                fin = starts[i] + durs[i]
                if fin < cur:
                    cur = fin
                suff_min_finish[i] = cur

            best = float('inf')
            for s, d in zip(first_start, first_dur):
                finish_first = s + d
                # rides in second list that start <= finish_first
                idx = bisect.bisect_right(starts, finish_first) - 1
                cand = float('inf')
                if idx >= 0:
                    cand = min(cand, finish_first + pref_min_dur[idx])
                # rides that start after finish_first
                nxt = idx + 1
                if nxt < n:
                    cand = min(cand, suff_min_finish[nxt])
                if cand < best:
                    best = cand
            return best

        ans1 = min_finish(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = min_finish(waterStartTime, waterDuration, landStartTime, landDuration)
        return int(min(ans1, ans2))
```

## Python3

```python
from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        INF = 10**18

        def evaluate(firstStarts: List[int], firstDur: List[int],
                     secondStarts: List[int], secondDur: List[int]) -> int:
            # sort second rides by start time
            sec = sorted(zip(secondStarts, secondDur))
            s2 = [s for s, _ in sec]
            d2 = [d for _, d in sec]
            m = len(s2)

            # prefix minimum of durations
            pref = [INF] * m
            cur = INF
            for i, dur in enumerate(d2):
                if dur < cur:
                    cur = dur
                pref[i] = cur

            # suffix minimum of (start + duration)
            suff = [INF] * (m + 1)   # suff[m] stays INF
            cur = INF
            for i in range(m - 1, -1, -1):
                val = s2[i] + d2[i]
                if val < cur:
                    cur = val
                suff[i] = cur

            best = INF
            for s, d in zip(firstStarts, firstDur):
                t = s + d                     # finish time after first ride
                idx = bisect_right(s2, t) - 1  # last start <= t
                cand = INF
                if idx >= 0:
                    cand = min(cand, t + pref[idx])   # wait for later rides that have opened
                cand = min(cand, suff[idx + 1] if idx + 1 < m else INF)  # take a ride that starts after t
                if cand < best:
                    best = cand
            return best

        ans1 = evaluate(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = evaluate(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(ans1, ans2)
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int start;
    int dur;
} Ride;

static int cmpRide(const void *a, const void *b) {
    const Ride *ra = (const Ride *)a;
    const Ride *rb = (const Ride *)b;
    if (ra->start < rb->start) return -1;
    if (ra->start > rb->start) return 1;
    return 0;
}

static int process(const Ride *first, int fsize, const Ride *second, int ssize) {
    if (ssize == 0) return INT_MAX;
    int *prefMinDur = (int *)malloc(sizeof(int) * ssize);
    int *suffMinFinish = (int *)malloc(sizeof(int) * ssize);

    for (int i = 0; i < ssize; ++i) {
        if (i == 0) prefMinDur[i] = second[i].dur;
        else prefMinDur[i] = prefMinDur[i - 1] < second[i].dur ? prefMinDur[i - 1] : second[i].dur;
    }
    for (int i = ssize - 1; i >= 0; --i) {
        int finish = second[i].start + second[i].dur;
        if (i == ssize - 1) suffMinFinish[i] = finish;
        else suffMinFinish[i] = suffMinFinish[i + 1] < finish ? suffMinFinish[i + 1] : finish;
    }

    int best = INT_MAX;
    for (int i = 0; i < fsize; ++i) {
        int finishFirst = first[i].start + first[i].dur;

        // upper_bound: first index with start > finishFirst
        int lo = 0, hi = ssize;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (second[mid].start <= finishFirst)
                lo = mid + 1;
            else
                hi = mid;
        }
        int pos = lo; // first > finishFirst

        if (pos > 0) {
            int cand = finishFirst + prefMinDur[pos - 1];
            if (cand < best) best = cand;
        }
        if (pos < ssize) {
            int cand = suffMinFinish[pos];
            if (cand < best) best = cand;
        }
    }

    free(prefMinDur);
    free(suffMinFinish);
    return best;
}

int earliestFinishTime(int* landStartTime, int landStartTimeSize,
                       int* landDuration, int landDurationSize,
                       int* waterStartTime, int waterStartTimeSize,
                       int* waterDuration, int waterDurationSize) {
    int n = landStartTimeSize;
    int m = waterStartTimeSize;

    Ride *land = (Ride *)malloc(sizeof(Ride) * n);
    for (int i = 0; i < n; ++i) {
        land[i].start = landStartTime[i];
        land[i].dur   = landDuration[i];
    }
    qsort(land, n, sizeof(Ride), cmpRide);

    Ride *water = (Ride *)malloc(sizeof(Ride) * m);
    for (int i = 0; i < m; ++i) {
        water[i].start = waterStartTime[i];
        water[i].dur   = waterDuration[i];
    }
    qsort(water, m, sizeof(Ride), cmpRide);

    int ans1 = process(land, n, water, m);   // land then water
    int ans2 = process(water, m, land, n);   // water then land

    free(land);
    free(water);

    return ans1 < ans2 ? ans1 : ans2;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        // sort both categories by start time
        RideSort(landStartTime, landDuration, out int[] lStarts, out int[] lDur, out int[] lFin);
        RideSort(waterStartTime, waterDuration, out int[] wStarts, out int[] wDur, out int[] wFin);

        // prefix min duration and suffix min finish for each category
        BuildPrefixSuffix(wDur, wFin, out int[] wPrefDur, out int[] wSufFin);
        BuildPrefixSuffix(lDur, lFin, out int[] lPrefDur, out int[] lSufFin);

        int ans = int.MaxValue;
        // land then water
        ans = Math.Min(ans, Evaluate(lStarts, lDur, wStarts, wPrefDur, wSufFin));
        // water then land
        ans = Math.Min(ans, Evaluate(wStarts, wDur, lStarts, lPrefDur, lSufFin));

        return ans;
    }

    private static void RideSort(int[] starts, int[] durs,
                                 out int[] sSorted, out int[] dSorted, out int[] fSorted) {
        int n = starts.Length;
        var rides = new Tuple<int, int>[n];
        for (int i = 0; i < n; i++) rides[i] = Tuple.Create(starts[i], durs[i]);
        Array.Sort(rides, (a, b) => a.Item1.CompareTo(b.Item1));

        sSorted = new int[n];
        dSorted = new int[n];
        fSorted = new int[n];
        for (int i = 0; i < n; i++) {
            sSorted[i] = rides[i].Item1;
            dSorted[i] = rides[i].Item2;
            fSorted[i] = rides[i].Item1 + rides[i].Item2;
        }
    }

    private static void BuildPrefixSuffix(int[] dur, int[] fin,
                                           out int[] prefDur, out int[] sufFin) {
        int n = dur.Length;
        prefDur = new int[n];
        sufFin = new int[n];

        prefDur[0] = dur[0];
        for (int i = 1; i < n; i++) prefDur[i] = Math.Min(prefDur[i - 1], dur[i]);

        sufFin[n - 1] = fin[n - 1];
        for (int i = n - 2; i >= 0; i--) sufFin[i] = Math.Min(sufFin[i + 1], fin[i]);
    }

    private static int Evaluate(int[] firstStarts, int[] firstDurs,
                                int[] secondStarts, int[] secondPrefDur, int[] secondSufFin) {
        int best = int.MaxValue;
        int m = secondStarts.Length;

        for (int i = 0; i < firstStarts.Length; i++) {
            int finish1 = firstStarts[i] + firstDurs[i];
            int ub = UpperBound(secondStarts, finish1); // first index > finish1
            int idx = ub - 1; // last index with start <= finish1

            if (idx >= 0) {
                best = Math.Min(best, finish1 + secondPrefDur[idx]);
            }
            if (ub < m) {
                best = Math.Min(best, secondSufFin[ub]);
            }
        }

        return best;
    }

    private static int UpperBound(int[] arr, int target) {
        int lo = 0, hi = arr.Length;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    const INF = Number.MAX_SAFE_INTEGER;
    
    // helper to compute minimal finish when doing first rides then second rides
    const compute = (firstS, firstD, secondS, secondD) => {
        const m = secondS.length;
        // sort second rides by start time
        const rides = new Array(m);
        for (let i = 0; i < m; ++i) rides[i] = [secondS[i], secondD[i]];
        rides.sort((a, b) => a[0] - b[0]);
        
        const starts = new Array(m);
        const prefixMinDur = new Array(m);
        const suffixMinFinish = new Array(m);
        
        for (let i = 0; i < m; ++i) starts[i] = rides[i][0];
        prefixMinDur[0] = rides[0][1];
        for (let i = 1; i < m; ++i) {
            prefixMinDur[i] = Math.min(prefixMinDur[i - 1], rides[i][1]);
        }
        suffixMinFinish[m - 1] = rides[m - 1][0] + rides[m - 1][1];
        for (let i = m - 2; i >= 0; --i) {
            suffixMinFinish[i] = Math.min(suffixMinFinish[i + 1], rides[i][0] + rides[i][1]);
        }
        
        let best = INF;
        const n = firstS.length;
        for (let i = 0; i < n; ++i) {
            const finishFirst = firstS[i] + firstD[i];
            
            // upper bound: first index > finishFirst
            let l = 0, r = m;
            while (l < r) {
                const mid = (l + r) >> 1;
                if (starts[mid] <= finishFirst) l = mid + 1;
                else r = mid;
            }
            const idx = l - 1; // last start <= finishFirst
            
            let cand = INF;
            if (idx >= 0) {
                cand = Math.min(cand, finishFirst + prefixMinDur[idx]);
            }
            if (idx + 1 < m) {
                cand = Math.min(cand, suffixMinFinish[idx + 1]);
            }
            best = Math.min(best, cand);
        }
        return best;
    };
    
    const ans1 = compute(landStartTime, landDuration, waterStartTime, waterDuration);
    const ans2 = compute(waterStartTime, waterDuration, landStartTime, landDuration);
    return Math.min(ans1, ans2);
};
```

## Typescript

```typescript
function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    function computeMin(firstStart: number[], firstDur: number[], secondStart: number[], secondDur: number[]): number {
        const m = secondStart.length;
        const idxs = Array.from({ length: m }, (_, i) => i);
        idxs.sort((a, b) => secondStart[a] - secondStart[b]);

        const s2 = new Array<number>(m);
        const d2 = new Array<number>(m);
        const fin2 = new Array<number>(m);
        for (let i = 0; i < m; i++) {
            s2[i] = secondStart[idxs[i]];
            d2[i] = secondDur[idxs[i]];
            fin2[i] = s2[i] + d2[i];
        }

        const pref = new Array<number>(m);
        let curMin = Infinity;
        for (let i = 0; i < m; i++) {
            if (d2[i] < curMin) curMin = d2[i];
            pref[i] = curMin;
        }

        const suff = new Array<number>(m);
        curMin = Infinity;
        for (let i = m - 1; i >= 0; i--) {
            if (fin2[i] < curMin) curMin = fin2[i];
            suff[i] = curMin;
        }

        let best = Infinity;
        const n = firstStart.length;
        for (let i = 0; i < n; i++) {
            const finish1 = firstStart[i] + firstDur[i];

            // binary search last index with start <= finish1
            let l = 0, r = m - 1, pos = -1;
            while (l <= r) {
                const mid = (l + r) >> 1;
                if (s2[mid] <= finish1) {
                    pos = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }

            let cand = Infinity;
            if (pos >= 0) {
                cand = Math.min(cand, finish1 + pref[pos]);
            }
            if (pos + 1 < m) {
                cand = Math.min(cand, suff[pos + 1]);
            }
            if (cand < best) best = cand;
        }

        return best;
    }

    const ansLandThenWater = computeMin(landStartTime, landDuration, waterStartTime, waterDuration);
    const ansWaterThenLand = computeMin(waterStartTime, waterDuration, landStartTime, landDuration);
    return Math.min(ansLandThenWater, ansWaterThenLand);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $landStartTime
     * @param Integer[] $landDuration
     * @param Integer[] $waterStartTime
     * @param Integer[] $waterDuration
     * @return Integer
     */
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        // Build ride arrays [start, duration]
        $land = [];
        $n = count($landStartTime);
        for ($i = 0; $i < $n; $i++) {
            $land[] = [$landStartTime[$i], $landDuration[$i]];
        }
        $water = [];
        $m = count($waterStartTime);
        for ($i = 0; $i < $m; $i++) {
            $water[] = [$waterStartTime[$i], $waterDuration[$i]];
        }

        // Sort by start time
        usort($land, function($a, $b) { return $a[0] <=> $b[0]; });
        usort($water, function($a, $b) { return $a[0] <=> $b[0]; });

        // Preprocess water rides: prefix min duration and suffix min finish time
        $waterStarts = [];
        $prefMinDurW = [];
        $suffMinFinishW = array_fill(0, $m + 1, PHP_INT_MAX);
        $minDur = PHP_INT_MAX;
        for ($i = 0; $i < $m; $i++) {
            $start = $water[$i][0];
            $dur   = $water[$i][1];
            $waterStarts[] = $start;
            if ($dur < $minDur) $minDur = $dur;
            $prefMinDurW[$i] = $minDur;
        }
        $minFinish = PHP_INT_MAX;
        for ($i = $m - 1; $i >= 0; $i--) {
            $finish = $water[$i][0] + $water[$i][1];
            if ($finish < $minFinish) $minFinish = $finish;
            $suffMinFinishW[$i] = $minFinish;
        }

        // Preprocess land rides similarly for the opposite order
        $landStarts = [];
        $prefMinDurL = [];
        $suffMinFinishL = array_fill(0, $n + 1, PHP_INT_MAX);
        $minDur = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $start = $land[$i][0];
            $dur   = $land[$i][1];
            $landStarts[] = $start;
            if ($dur < $minDur) $minDur = $dur;
            $prefMinDurL[$i] = $minDur;
        }
        $minFinish = PHP_INT_MAX;
        for ($i = $n - 1; $i >= 0; $i--) {
            $finish = $land[$i][0] + $land[$i][1];
            if ($finish < $minFinish) $minFinish = $finish;
            $suffMinFinishL[$i] = $minFinish;
        }

        $ans = PHP_INT_MAX;

        // Land then Water
        foreach ($land as $ride) {
            $t = $ride[0] + $ride[1]; // finish time after land ride
            // binary search last water start <= t
            $l = 0; $r = $m - 1; $idx = -1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($waterStarts[$mid] <= $t) {
                    $idx = $mid;
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }
            $candidate = PHP_INT_MAX;
            if ($idx >= 0) {
                $cand1 = $t + $prefMinDurW[$idx];
                if ($cand1 < $candidate) $candidate = $cand1;
            }
            if ($idx + 1 < $m) {
                $cand2 = $suffMinFinishW[$idx + 1];
                if ($cand2 < $candidate) $candidate = $cand2;
            }
            if ($candidate < $ans) $ans = $candidate;
        }

        // Water then Land
        foreach ($water as $ride) {
            $t = $ride[0] + $ride[1]; // finish time after water ride
            // binary search last land start <= t
            $l = 0; $r = $n - 1; $idx = -1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($landStarts[$mid] <= $t) {
                    $idx = $mid;
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }
            $candidate = PHP_INT_MAX;
            if ($idx >= 0) {
                $cand1 = $t + $prefMinDurL[$idx];
                if ($cand1 < $candidate) $candidate = $cand1;
            }
            if ($idx + 1 < $n) {
                $cand2 = $suffMinFinishL[$idx + 1];
                if ($cand2 < $candidate) $candidate = $cand2;
            }
            if ($candidate < $ans) $ans = $candidate;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func earliestFinishTime(_ landStartTime: [Int], _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) -> Int {
        let n = landStartTime.count
        let m = waterStartTime.count
        
        // Water rides sorted by start time
        var waterRides = [(s: Int, d: Int)]()
        waterRides.reserveCapacity(m)
        for i in 0..<m {
            waterRides.append((s: waterStartTime[i], d: waterDuration[i]))
        }
        waterRides.sort { $0.s < $1.s }
        var wStarts = [Int]()
        var wDur = [Int]()
        wStarts.reserveCapacity(m)
        wDur.reserveCapacity(m)
        for r in waterRides {
            wStarts.append(r.s)
            wDur.append(r.d)
        }
        // Prefix minimum duration
        var wPrefMinDur = [Int](repeating: 0, count: m)
        for i in 0..<m {
            if i == 0 { wPrefMinDur[i] = wDur[i] } else { wPrefMinDur[i] = min(wPrefMinDur[i - 1], wDur[i]) }
        }
        // Suffix minimum finish time (start + duration)
        var wSuffMinFinish = [Int](repeating: 0, count: m)
        for i in stride(from: m - 1, through: 0, by: -1) {
            let fin = wStarts[i] + wDur[i]
            if i == m - 1 { wSuffMinFinish[i] = fin } else { wSuffMinFinish[i] = min(wSuffMinFinish[i + 1], fin) }
        }
        
        // Land rides sorted by start time (for reverse order)
        var landRides = [(s: Int, d: Int)]()
        landRides.reserveCapacity(n)
        for i in 0..<n {
            landRides.append((s: landStartTime[i], d: landDuration[i]))
        }
        landRides.sort { $0.s < $1.s }
        var lStarts = [Int]()
        var lDur = [Int]()
        lStarts.reserveCapacity(n)
        lDur.reserveCapacity(n)
        for r in landRides {
            lStarts.append(r.s)
            lDur.append(r.d)
        }
        var lPrefMinDur = [Int](repeating: 0, count: n)
        for i in 0..<n {
            if i == 0 { lPrefMinDur[i] = lDur[i] } else { lPrefMinDur[i] = min(lPrefMinDur[i - 1], lDur[i]) }
        }
        var lSuffMinFinish = [Int](repeating: 0, count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let fin = lStarts[i] + lDur[i]
            if i == n - 1 { lSuffMinFinish[i] = fin } else { lSuffMinFinish[i] = min(lSuffMinFinish[i + 1], fin) }
        }
        
        func upperBound(_ arr: [Int], _ target: Int) -> Int {
            var lo = 0
            var hi = arr.count
            while lo < hi {
                let mid = (lo + hi) >> 1
                if arr[mid] <= target {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }
        
        var answer = Int.max
        
        // Land then water
        for i in 0..<n {
            let finishLand = landStartTime[i] + landDuration[i]
            let idx = upperBound(wStarts, finishLand)
            var best = Int.max
            if idx > 0 {
                best = min(best, finishLand + wPrefMinDur[idx - 1])
            }
            if idx < m {
                best = min(best, wSuffMinFinish[idx])
            }
            answer = min(answer, best)
        }
        
        // Water then land
        for j in 0..<m {
            let finishWater = waterStartTime[j] + waterDuration[j]
            let idx = upperBound(lStarts, finishWater)
            var best = Int.max
            if idx > 0 {
                best = min(best, finishWater + lPrefMinDur[idx - 1])
            }
            if idx < n {
                best = min(best, lSuffMinFinish[idx])
            }
            answer = min(answer, best)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun earliestFinishTime(
        landStartTime: IntArray,
        landDuration: IntArray,
        waterStartTime: IntArray,
        waterDuration: IntArray
    ): Int {
        // helper to compute minimal finish when taking a ride from first list then second list
        fun compute(firstStart: IntArray, firstDur: IntArray,
                    secondStart: IntArray, secondDur: IntArray): Int {
            val m = secondStart.size
            // sort second rides by start time
            data class Ride(val s: Int, val d: Int)
            val rides = Array(m) { i -> Ride(secondStart[i], secondDur[i]) }
            rides.sortBy { it.s }

            val starts = IntArray(m)
            val finishes = IntArray(m)
            for (i in 0 until m) {
                starts[i] = rides[i].s
                finishes[i] = rides[i].s + rides[i].d
            }

            // prefix minimum of durations
            val prefMinDur = IntArray(m)
            var curMinDur = Int.MAX_VALUE
            for (i in 0 until m) {
                if (rides[i].d < curMinDur) curMinDur = rides[i].d
                prefMinDur[i] = curMinDur
            }

            // suffix minimum of finish times (start + duration)
            val suffMinFinish = IntArray(m)
            var curMinFin = Int.MAX_VALUE
            for (i in m - 1 downTo 0) {
                if (finishes[i] < curMinFin) curMinFin = finishes[i]
                suffMinFinish[i] = curMinFin
            }

            var bestOverall = Int.MAX_VALUE
            val n = firstStart.size
            for (i in 0 until n) {
                val finishFirst = firstStart[i] + firstDur[i]

                // binary search: first index with start > finishFirst
                var l = 0
                var r = m
                while (l < r) {
                    val mid = (l + r) ushr 1
                    if (starts[mid] <= finishFirst) {
                        l = mid + 1
                    } else {
                        r = mid
                    }
                }
                val idx = l - 1 // last ride with start <= finishFirst

                var candidate = Int.MAX_VALUE
                if (idx >= 0) {
                    // early group: can start immediately after first ride
                    val cand = finishFirst + prefMinDur[idx]
                    if (cand < candidate) candidate = cand
                }
                if (idx + 1 < m) {
                    // late group: must wait for its start time
                    val cand = suffMinFinish[idx + 1]
                    if (cand < candidate) candidate = cand
                }
                if (candidate < bestOverall) bestOverall = candidate
            }
            return bestOverall
        }

        val ansLandThenWater = compute(landStartTime, landDuration, waterStartTime, waterDuration)
        val ansWaterThenLand = compute(waterStartTime, waterDuration, landStartTime, landDuration)
        return minOf(ansLandThenWater, ansWaterThenLand)
    }
}
```

## Dart

```dart
class Solution {
  int earliestFinishTime(List<int> landStartTime, List<int> landDuration,
      List<int> waterStartTime, List<int> waterDuration) {
    // sort land rides by start time
    int n = landStartTime.length;
    var idxLand = List<int>.generate(n, (i) => i);
    idxLand.sort((a, b) => landStartTime[a].compareTo(landStartTime[b]));
    List<int> lStart = List.filled(n, 0);
    List<int> lDur = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      lStart[i] = landStartTime[idxLand[i]];
      lDur[i] = landDuration[idxLand[i]];
    }

    // sort water rides by start time
    int m = waterStartTime.length;
    var idxWater = List<int>.generate(m, (i) => i);
    idxWater.sort((a, b) => waterStartTime[a].compareTo(waterStartTime[b]));
    List<int> wStart = List.filled(m, 0);
    List<int> wDur = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      wStart[i] = waterStartTime[idxWater[i]];
      wDur[i] = waterDuration[idxWater[i]];
    }

    int ansLandThenWater = _orderMin(lStart, lDur, wStart, wDur);
    int ansWaterThenLand = _orderMin(wStart, wDur, lStart, lDur);
    return ansLandThenWater < ansWaterThenLand
        ? ansLandThenWater
        : ansWaterThenLand;
  }

  int _orderMin(List<int> firstStart, List<int> firstDur,
      List<int> secondStart, List<int> secondDur) {
    int m = secondStart.length;
    // prefix minimum of durations for early rides
    List<int> prefMinDur = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      if (i == 0) {
        prefMinDur[i] = secondDur[i];
      } else {
        prefMinDur[i] =
            prefMinDur[i - 1] < secondDur[i] ? prefMinDur[i - 1] : secondDur[i];
      }
    }

    // suffix minimum of finish times for later rides
    List<int> suffMinFinish = List.filled(m, 0);
    for (int i = m - 1; i >= 0; --i) {
      int finish = secondStart[i] + secondDur[i];
      if (i == m - 1) {
        suffMinFinish[i] = finish;
      } else {
        suffMinFinish[i] =
            suffMinFinish[i + 1] < finish ? suffMinFinish[i + 1] : finish;
      }
    }

    int best = 1 << 60; // large sentinel
    for (int i = 0; i < firstStart.length; ++i) {
      int f = firstStart[i] + firstDur[i];

      // binary search: first index with start > f
      int lo = 0, hi = m;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (secondStart[mid] <= f) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      int idx = lo - 1; // last index with start <= f

      if (idx >= 0) {
        int cand = f + prefMinDur[idx];
        if (cand < best) best = cand;
      }
      if (idx + 1 < m) {
        int cand2 = suffMinFinish[idx + 1];
        if (cand2 < best) best = cand2;
      }
    }
    return best;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

type ride struct {
	s int
	d int
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	land := make([]ride, len(landStartTime))
	for i := range landStartTime {
		land[i] = ride{s: landStartTime[i], d: landDuration[i]}
	}
	water := make([]ride, len(waterStartTime))
	for i := range waterStartTime {
		water[i] = ride{s: waterStartTime[i], d: waterDuration[i]}
	}

	sort.Slice(land, func(i, j int) bool { return land[i].s < land[j].s })
	sort.Slice(water, func(i, j int) bool { return water[i].s < water[j].s })

	minAns := computeMin(land, water)
	alt := computeMin(water, land)
	if alt < minAns {
		minAns = alt
	}
	return minAns
}

func computeMin(first []ride, second []ride) int {
	m := len(second)
	starts := make([]int, m)
	prefDur := make([]int, m)
	suffixFin := make([]int, m)

	for i := 0; i < m; i++ {
		starts[i] = second[i].s
	}
	for i := 0; i < m; i++ {
		if i == 0 || second[i].d < prefDur[i-1] {
			prefDur[i] = second[i].d
		} else {
			prefDur[i] = prefDur[i-1]
		}
	}
	for i := m - 1; i >= 0; i-- {
		fin := second[i].s + second[i].d
		if i == m-1 || fin < suffixFin[i+1] {
			suffixFin[i] = fin
		} else {
			suffixFin[i] = suffixFin[i+1]
		}
	}

	const inf = int(^uint(0) >> 1)
	ans := inf

	for _, r := range first {
		finish1 := r.s + r.d
		idx := sort.Search(m, func(i int) bool { return starts[i] > finish1 })
		best := inf
		if idx > 0 {
			cand := finish1 + prefDur[idx-1]
			if cand < best {
				best = cand
			}
		}
		if idx < m {
			cand := suffixFin[idx]
			if cand < best {
				best = cand
			}
		}
		if best < ans {
			ans = best
		}
	}
	return ans
}
```

## Ruby

```ruby
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  # Prepare sorted data for a list: starts, prefix min durations, suffix min (start+duration)
  prepare = lambda do |starts_arr, dur_arr|
    idx = (0...starts_arr.length).to_a.sort_by { |i| starts_arr[i] }
    starts = idx.map { |i| starts_arr[i] }
    durs = idx.map { |i| dur_arr[i] }
    n = starts.size
    pref_min = Array.new(n)
    cur = Float::INFINITY
    n.times do |i|
      cur = durs[i] < cur ? durs[i] : cur
      pref_min[i] = cur
    end
    suffix_min = Array.new(n)
    cur = Float::INFINITY
    (n - 1).downto(0) do |i|
      finish = starts[i] + durs[i]
      cur = finish < cur ? finish : cur
      suffix_min[i] = cur
    end
    [starts, pref_min, suffix_min]
  end

  water_starts, water_pref, water_suf = prepare.call(water_start_time, water_duration)
  land_starts, land_pref, land_suf = prepare.call(land_start_time, land_duration)

  # Compute minimal total finish when first list is taken before second list
  compute_min = lambda do |first_starts, first_durs, second_starts, second_pref, second_suf|
    best_total = Float::INFINITY
    first_starts.each_with_index do |s, i|
      t = s + first_durs[i] # finish time after first ride
      # binary search last index with start <= t
      lo = 0
      hi = second_starts.length - 1
      idx = -1
      while lo <= hi
        mid = (lo + hi) / 2
        if second_starts[mid] <= t
          idx = mid
          lo = mid + 1
        else
          hi = mid - 1
        end
      end
      cur_best = Float::INFINITY
      if idx >= 0
        cur_best = t + second_pref[idx]
      end
      if idx + 1 < second_starts.length
        cur_best = second_suf[idx + 1] if second_suf[idx + 1] < cur_best
      end
      best_total = cur_best if cur_best < best_total
    end
    best_total
  end

  ans1 = compute_min.call(land_start_time, land_duration, water_starts, water_pref, water_suf)
  ans2 = compute_min.call(water_start_time, water_duration, land_starts, land_pref, land_suf)

  [ans1, ans2].min
end
```

## Scala

```scala
object Solution {
    def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int],
                           waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {

        // sort rides by start time, return aligned arrays
        def sortRides(start: Array[Int], dur: Array[Int]): (Array[Int], Array[Int]) = {
            val n = start.length
            val idx = (0 until n).toArray.sortBy(start(_))
            val s = new Array[Int](n)
            val d = new Array[Int](n)
            var i = 0
            while (i < n) {
                s(i) = start(idx(i))
                d(i) = dur(idx(i))
                i += 1
            }
            (s, d)
        }

        // compute minimal finish time when taking a ride from first list then second list
        def solve(firstStart: Array[Int], firstDur: Array[Int],
                  secondStart: Array[Int], secondDur: Array[Int]): Int = {

            val (fs, fd) = sortRides(firstStart, firstDur)
            val (ss, sd) = sortRides(secondStart, secondDur)

            val n1 = fs.length
            val n2 = ss.length

            // prefix minimum duration for second rides
            val prefMinDur = new Array[Int](n2)
            var curMinDur = Int.MaxValue
            var i = 0
            while (i < n2) {
                if (sd(i) < curMinDur) curMinDur = sd(i)
                prefMinDur(i) = curMinDur
                i += 1
            }

            // suffix minimum finish time (start+duration) for second rides
            val suffMinFinish = new Array[Int](n2)
            var curMinFin = Int.MaxValue
            i = n2 - 1
            while (i >= 0) {
                val fin = ss(i) + sd(i)
                if (fin < curMinFin) curMinFin = fin
                suffMinFinish(i) = curMinFin
                i -= 1
            }

            var answer = Int.MaxValue

            // iterate over each ride in first list
            i = 0
            while (i < n1) {
                val finishFirst = fs(i) + fd(i)

                // binary search upper bound for start <= finishFirst
                var l = 0
                var r = n2
                while (l < r) {
                    val mid = (l + r) >>> 1
                    if (ss(mid) <= finishFirst) l = mid + 1 else r = mid
                }
                val idx = l - 1 // last index with start <= finishFirst

                var best = Int.MaxValue
                if (idx >= 0) {
                    best = finishFirst + prefMinDur(idx)
                }
                if (idx + 1 < n2) {
                    val cand = suffMinFinish(idx + 1)
                    if (cand < best) best = cand
                }
                if (best < answer) answer = best

                i += 1
            }

            answer
        }

        val ansLandThenWater = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        val ansWaterThenLand = solve(waterStartTime, waterDuration, landStartTime, landDuration)

        Math.min(ansLandThenWater, ansWaterThenLand)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn earliest_finish_time(
        land_start_time: Vec<i32>,
        land_duration: Vec<i32>,
        water_start_time: Vec<i32>,
        water_duration: Vec<i32>,
    ) -> i32 {
        fn solve(first_start: &Vec<i32>, first_dur: &Vec<i32>, second_start: &Vec<i32>, second_dur: &Vec<i32>) -> i32 {
            let n = first_start.len();
            let m = second_start.len();

            // sort second rides by start time
            let mut second: Vec<(i32, i32)> = (0..m).map(|i| (second_start[i], second_dur[i])).collect();
            second.sort_by_key(|x| x.0);
            let mut starts2 = Vec::with_capacity(m);
            let mut dur2 = Vec::with_capacity(m);
            let mut finish2 = Vec::with_capacity(m);
            for &(s, d) in &second {
                starts2.push(s);
                dur2.push(d);
                finish2.push(s + d);
            }

            // prefix minimum of durations
            let mut pref_min = Vec::with_capacity(m);
            let mut cur = i32::MAX;
            for &d in &dur2 {
                if d < cur { cur = d; }
                pref_min.push(cur);
            }

            // suffix minimum of finish times (start + duration)
            let mut suff_min = vec![i32::MAX; m];
            let mut curf = i32::MAX;
            for i in (0..m).rev() {
                if finish2[i] < curf { curf = finish2[i]; }
                suff_min[i] = curf;
            }

            // sort first rides by start time
            let mut first: Vec<(i32, i32)> = (0..n).map(|i| (first_start[i], first_dur[i])).collect();
            first.sort_by_key(|x| x.0);

            let mut best = i32::MAX;
            for &(s1, d1) in &first {
                let finish1 = s1 + d1;
                // number of rides in second list with start <= finish1
                let pos = starts2.partition_point(|&x| x <= finish1);
                if pos > 0 {
                    let cand = finish1 + pref_min[pos - 1];
                    if cand < best { best = cand; }
                }
                if pos < m {
                    let cand = suff_min[pos];
                    if cand < best { best = cand; }
                }
            }
            best
        }

        let ans1 = solve(&land_start_time, &land_duration, &water_start_time, &water_duration);
        let ans2 = solve(&water_start_time, &water_duration, &land_start_time, &land_duration);
        std::cmp::min(ans1, ans2)
    }
}
```

## Racket

```racket
(define/contract (earliest-finish-time landStartTime landDuration waterStartTime waterDuration)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((INF 1000000000000000000)
         (landS (list->vector landStartTime))
         (landD (list->vector landDuration))
         (waterS (list->vector waterStartTime))
         (waterD (list->vector waterDuration)))
    ;; sort rides of the second category and build helper vectors
    (define (prepare startsV dursV)
      (let* ((pairs (for/list ([s (in-vector startsV)] [d (in-vector dursV)]) (list s d)))
             (sorted-pairs (sort pairs < #:key (lambda (p) (first p))))
             (m (length sorted-pairs))
             (starts (make-vector m))
             (durs (make-vector m)))
        (for ([i (in-range m)] [p sorted-pairs])
          (vector-set! starts i (first p))
          (vector-set! durs i (second p)))
        (values starts durs)))
    ;; prefix minimum of durations
    (define (build-pref-min-dur dursV)
      (let* ((m (vector-length dursV))
             (pref (make-vector m))
             (best INF))
        (for ([i (in-range m)])
          (let ((d (vector-ref dursV i)))
            (when (< d best) (set! best d))
            (vector-set! pref i best)))
        pref))
    ;; suffix minimum of start+duration
    (define (build-suff-min-finish startsV dursV)
      (let* ((m (vector-length startsV))
             (suff (make-vector m))
             (best INF))
        (for ([i (in-range (- m 1) -1 -1)])
          (let ((fin (+ (vector-ref startsV i) (vector-ref dursV i))))
            (when (< fin best) (set! best fin))
            (vector-set! suff i best)))
        suff))
    ;; first index with value > val
    (define (upper-bound vec val)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (> (vector-ref vec mid) val)
                  (loop lo mid)
                  (loop (+ mid 1) hi))))))
    ;; compute minimal finish when doing first category then second
    (define (process firstS firstD secondS secondD)
      (let-values ([(secStarts secDur) (prepare secondS secondD)])
        (define pref (build-pref-min-dur secDur))
        (define suff (build-suff-min-finish secStarts secDur))
        (define best INF)
        (for ([i (in-range (vector-length firstS))])
          (let* ((finish1 (+ (vector-ref firstS i) (vector-ref firstD i)))
                 (idx (- (upper-bound secStarts finish1) 1))) ; last start <= finish1
            (when (>= idx 0)
              (define cand (+ finish1 (vector-ref pref idx)))
              (when (< cand best) (set! best cand)))
            (when (< (+ idx 1) (vector-length secStarts))
              (define cand (vector-ref suff (+ idx 1)))
              (when (< cand best) (set! best cand)))))
        best))
    (let ((ans1 (process landS landD waterS waterD))
          (ans2 (process waterS waterD landS landD)))
      (if (< ans1 ans2) ans1 ans2))))
```

## Erlang

```erlang
-spec earliest_finish_time(LandStartTime :: [integer()], LandDuration :: [integer()], WaterStartTime :: [integer()], WaterDuration :: [integer()]) -> integer().
earliest_finish_time(LandStartTime, LandDuration, WaterStartTime, WaterDuration) ->
    LandPairs = lists:zip(LandStartTime, LandDuration),
    WaterPairs = lists:zip(WaterStartTime, WaterDuration),

    WaterData = process_data(WaterPairs),
    Min1 = compute_min(LandPairs, WaterData),

    LandData = process_data(LandPairs),
    Min2 = compute_min(WaterPairs, LandData),

    min(Min1, Min2).

%% Process a list of {Start, Duration} into sorted structures
process_data(Pairs) ->
    Sorted = lists:keysort(1, Pairs),
    StartsList = [S || {S,_} <- Sorted],
    StartsTuple = list_to_tuple(StartsList),

    PrefDurList = build_pref(Sorted, undefined, []),
    PrefDurTuple = list_to_tuple(PrefDurList),

    RevSorted = lists:reverse(Sorted),
    SufFinList = build_suf(RevSorted, undefined, []),
    SufFinTuple = list_to_tuple(SufFinList),

    Len = length(StartsList),
    {StartsTuple, PrefDurTuple, SufFinTuple, Len}.

%% Build prefix minimum durations
build_pref([], _MinSoFar, Acc) ->
    lists:reverse(Acc);
build_pref([{_,D}|Rest], undefined, Acc) ->
    build_pref(Rest, D, [D|Acc]);
build_pref([{_,D}|Rest], MinSoFar, Acc) ->
    NewMin = if D < MinSoFar -> D; true -> MinSoFar end,
    build_pref(Rest, NewMin, [NewMin|Acc]).

%% Build suffix minimum finish times (start+duration)
build_suf([], _MinSoFar, Acc) ->
    lists:reverse(Acc);
build_suf([{S,D}|Rest], undefined, Acc) ->
    Finish = S + D,
    build_suf(Rest, Finish, [Finish|Acc]);
build_suf([{S,D}|Rest], MinSoFar, Acc) ->
    Finish = S + D,
    NewMin = if Finish < MinSoFar -> Finish; true -> MinSoFar end,
    build_suf(Rest, NewMin, [NewMin|Acc]).

%% Compute minimal finish time when taking a ride from FirstPairs first,
%% then one from the processed second list.
compute_min(FirstPairs, {StartsTuple, PrefDurTuple, SufFinTuple, Len}) ->
    Inf = 1 bsl 60,
    lists:foldl(fun({S,D}, MinAcc) ->
        T = S + D,
        EarlyIdx = find_last_leq(T, StartsTuple, 0, Len - 1),
        Cand1 = case EarlyIdx >= 0 of
                    true -> T + get_elem(PrefDurTuple, EarlyIdx);
                    false -> Inf
                end,
        LateIdx = EarlyIdx + 1,
        Cand2 = case LateIdx < Len of
                    true -> get_elem(SufFinTuple, LateIdx);
                    false -> Inf
                end,
        Total = if Cand1 < Cand2 -> Cand1; true -> Cand2 end,
        if Total < MinAcc -> Total; true -> MinAcc end
    end, Inf, FirstPairs).

%% Binary search: last index with start <= T, returns -1 if none.
find_last_leq(T, StartsTuple, Low, High) when Low > High ->
    High;
find_last_leq(T, StartsTuple, Low, High) ->
    Mid = (Low + High) div 2,
    Val = get_elem(StartsTuple, Mid),
    if Val =< T ->
            find_last_leq(T, StartsTuple, Mid + 1, High);
       true ->
            find_last_leq(T, StartsTuple, Low, Mid - 1)
    end.

%% Tuple element access (0‑based index)
get_elem(Tuple, Index) ->
    erlang:element(Index + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_finish_time(
          land_start_time :: [integer],
          land_duration :: [integer],
          water_start_time :: [integer],
          water_duration :: [integer]
        ) :: integer
  def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration) do
    ans1 = compute_min(land_start_time, land_duration, water_start_time, water_duration)
    ans2 = compute_min(water_start_time, water_duration, land_start_time, land_duration)
    min(ans1, ans2)
  end

  defp compute_min(first_start, first_dur, second_start, second_dur) do
    # preprocess second list (sorted by start time)
    second =
      Enum.zip(second_start, second_dur)
      |> Enum.sort_by(fn {s, _} -> s end)

    len2 = length(second)

    starts_tuple =
      second
      |> Enum.map(&elem(&1, 0))
      |> List.to_tuple()

    # prefix minimum of durations
    pref_min_dur_tuple =
      second
      |> Enum.reduce({[], :infinity}, fn {_s, d}, {acc, cur_min} ->
        new_min = if d < cur_min, do: d, else: cur_min
        {[new_min | acc], new_min}
      end)
      |> elem(0)
      |> Enum.reverse()
      |> List.to_tuple()

    # suffix minimum of finish times (start + duration)
    finishes =
      second
      |> Enum.map(fn {s, d} -> s + d end)

    suffix_min_finish_tuple =
      finishes
      |> Enum.reverse()
      |> Enum.reduce([], fn fin, acc ->
        case acc do
          [] -> [fin]
          [prev | _] ->
            min_val = if fin < prev, do: fin, else: prev
            [min_val | acc]
        end
      end)
      |> Enum.reverse()
      |> List.to_tuple()

    inf = 1 <<< 60

    # iterate over first rides to find minimal finish time
    Enum.reduce(Enum.zip(first_start, first_dur), inf, fn {s1, d1}, cur_min ->
      finish1 = s1 + d1
      idx = upper_bound(starts_tuple, finish1, 0, len2 - 1, -1)

      cand =
        cond do
          idx >= 0 and idx + 1 < len2 ->
            early = finish1 + elem(pref_min_dur_tuple, idx)
            late = elem(suffix_min_finish_tuple, idx + 1)
            min(early, late)

          idx >= 0 ->
            finish1 + elem(pref_min_dur_tuple, idx)

          idx + 1 < len2 ->
            elem(suffix_min_finish_tuple, idx + 1)

          true ->
            inf
        end

      min(cur_min, cand)
    end)
  end

  defp upper_bound(_starts, _target, low, high, best) when low > high, do: best

  defp upper_bound(starts, target, low, high, _best) do
    mid = div(low + high, 2)
    s = elem(starts, mid)

    if s <= target do
      upper_bound(starts, target, mid + 1, high, mid)
    else
      upper_bound(starts, target, low, mid - 1, -1)
    end
  end
end
```
