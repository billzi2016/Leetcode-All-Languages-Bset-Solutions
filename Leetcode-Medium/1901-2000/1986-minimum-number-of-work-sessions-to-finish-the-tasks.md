# 1986. Minimum Number of Work Sessions to Finish the Tasks

## Cpp

```cpp
class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        int totalMask = 1 << n;
        vector<int> subsetSum(totalMask, 0);
        for (int mask = 1; mask < totalMask; ++mask) {
            int lsb = __builtin_ctz(mask);               // index of least significant set bit
            int prev = mask ^ (1 << lsb);
            subsetSum[mask] = subsetSum[prev] + tasks[lsb];
        }
        
        const int INF = 1e9;
        vector<int> dp(totalMask, INF);
        dp[0] = 0;
        for (int mask = 1; mask < totalMask; ++mask) {
            // iterate over all non‑empty submasks of mask
            for (int sub = mask; sub; sub = (sub - 1) & mask) {
                if (subsetSum[sub] <= sessionTime) {
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + 1);
                }
            }
        }
        return dp[totalMask - 1];
    }
};
```

## Java

```java
class Solution {
    public int minSessions(int[] tasks, int sessionTime) {
        int n = tasks.length;
        int totalMask = 1 << n;
        int INF = n + 1; // maximum possible sessions
        int[] sess = new int[totalMask];
        int[] rem = new int[totalMask];
        for (int i = 0; i < totalMask; i++) {
            sess[i] = INF;
            rem[i] = 0;
        }
        sess[0] = 1; // start with one empty session
        rem[0] = 0;

        for (int mask = 0; mask < totalMask; mask++) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int newMask = mask | (1 << i);
                int candSess, candRem;
                if (rem[mask] + tasks[i] <= sessionTime) {
                    candSess = sess[mask];
                    candRem = rem[mask] + tasks[i];
                } else {
                    candSess = sess[mask] + 1;
                    candRem = tasks[i];
                }
                if (candSess < sess[newMask] || (candSess == sess[newMask] && candRem > rem[newMask])) {
                    sess[newMask] = candSess;
                    rem[newMask] = candRem;
                }
            }
        }
        return sess[totalMask - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        full = 1 << n
        INF = (float('inf'), float('inf'))
        dp = [INF] * full
        dp[0] = (1, 0)  # start with one empty session

        for mask in range(full):
            sessions, used = dp[mask]
            if sessions == float('inf'):
                continue
            for i in range(n):
                if not (mask >> i) & 1:
                    t = tasks[i]
                    if used + t <= sessionTime:
                        cand = (sessions, used + t)
                    else:
                        cand = (sessions + 1, t)
                    new_mask = mask | (1 << i)
                    cur = dp[new_mask]
                    if cand[0] < cur[0] or (cand[0] == cur[0] and cand[1] < cur[1]):
                        dp[new_mask] = cand

        return dp[full - 1][0]
```

## Python3

```python
from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        full = 1 << n
        INF = (n + 1, 0)
        dp = [INF] * full
        dp[0] = (1, sessionTime)  # start with one empty session

        for mask in range(full):
            sessions, remain = dp[mask]
            if sessions == INF[0]:
                continue
            for i in range(n):
                if not (mask >> i) & 1:
                    t = tasks[i]
                    if t <= remain:
                        cand = (sessions, remain - t)
                    else:
                        cand = (sessions + 1, sessionTime - t)
                    new_mask = mask | (1 << i)
                    cur = dp[new_mask]
                    if cand[0] < cur[0] or (cand[0] == cur[0] and cand[1] > cur[1]):
                        dp[new_mask] = cand

        return dp[full - 1][0]
```

## C

```c
#include <stdlib.h>

int minSessions(int* tasks, int tasksSize, int sessionTime) {
    int totalMasks = 1 << tasksSize;
    int *dpSess = (int *)malloc(totalMasks * sizeof(int));
    int *dpUsed = (int *)malloc(totalMasks * sizeof(int));

    const int INF_SESS = tasksSize + 5;
    const int INF_USED = sessionTime + 5;

    for (int mask = 0; mask < totalMasks; ++mask) {
        dpSess[mask] = INF_SESS;
        dpUsed[mask] = INF_USED;
    }
    dpSess[0] = 1;   // start with one empty session
    dpUsed[0] = 0;

    for (int mask = 1; mask < totalMasks; ++mask) {
        for (int i = 0; i < tasksSize; ++i) {
            if (mask & (1 << i)) {
                int prevMask = mask ^ (1 << i);
                int sess = dpSess[prevMask];
                int used = dpUsed[prevMask];
                int newSess, newUsed;

                if (used + tasks[i] <= sessionTime) {
                    newSess = sess;
                    newUsed = used + tasks[i];
                } else {
                    newSess = sess + 1;
                    newUsed = tasks[i];
                }

                if (newSess < dpSess[mask] ||
                    (newSess == dpSess[mask] && newUsed < dpUsed[mask])) {
                    dpSess[mask] = newSess;
                    dpUsed[mask] = newUsed;
                }
            }
        }
    }

    int result = dpSess[totalMasks - 1];
    free(dpSess);
    free(dpUsed);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSessions(int[] tasks, int sessionTime)
    {
        int n = tasks.Length;
        int totalMask = 1 << n;
        var dp = new (int sessions, int cur)[totalMask];
        const int INF = 1_000_000;
        for (int i = 0; i < totalMask; i++) dp[i] = (INF, INF);
        dp[0] = (1, 0); // start with one empty session

        for (int mask = 0; mask < totalMask; mask++)
        {
            var (sess, cur) = dp[mask];
            if (sess == INF) continue;

            for (int i = 0; i < n; i++)
            {
                if (((mask >> i) & 1) == 0)
                {
                    int newMask = mask | (1 << i);
                    int t = tasks[i];
                    int nsess, ncur;
                    if (cur + t <= sessionTime)
                    {
                        nsess = sess;
                        ncur = cur + t;
                    }
                    else
                    {
                        nsess = sess + 1;
                        ncur = t;
                    }

                    var (oldSess, oldCur) = dp[newMask];
                    if (nsess < oldSess || (nsess == oldSess && ncur < oldCur))
                    {
                        dp[newMask] = (nsess, ncur);
                    }
                }
            }
        }

        return dp[totalMask - 1].sessions;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tasks
 * @param {number} sessionTime
 * @return {number}
 */
var minSessions = function(tasks, sessionTime) {
    const n = tasks.length;
    const totalMask = 1 << n;
    const sum = new Array(totalMask).fill(0);
    const feasible = new Array(totalMask).fill(false);
    const pos = {};
    for (let i = 0; i < n; ++i) pos[1 << i] = i;

    for (let mask = 1; mask < totalMask; ++mask) {
        const lsb = mask & -mask;
        const idx = pos[lsb];
        sum[mask] = sum[mask ^ lsb] + tasks[idx];
        feasible[mask] = sum[mask] <= sessionTime;
    }

    const dp = new Array(totalMask).fill(n + 1);
    dp[0] = 0;

    for (let mask = 1; mask < totalMask; ++mask) {
        let sub = mask;
        while (sub) {
            if (feasible[sub]) {
                const remaining = mask ^ sub;
                dp[mask] = Math.min(dp[mask], dp[remaining] + 1);
            }
            sub = (sub - 1) & mask;
        }
    }

    return dp[totalMask - 1];
};
```

## Typescript

```typescript
function minSessions(tasks: number[], sessionTime: number): number {
    const n = tasks.length;
    const totalMask = 1 << n;
    type State = { cnt: number; rem: number };
    const INF = Number.MAX_SAFE_INTEGER;
    const dp: State[] = new Array(totalMask);
    for (let i = 0; i < totalMask; i++) {
        dp[i] = { cnt: INF, rem: 0 };
    }
    dp[0] = { cnt: 1, rem: 0 }; // start with one empty session

    for (let mask = 0; mask < totalMask; mask++) {
        const cur = dp[mask];
        if (cur.cnt === INF) continue;
        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) continue;
            const t = tasks[i];
            let next: State;
            if (t <= sessionTime - cur.rem) {
                next = { cnt: cur.cnt, rem: cur.rem + t };
            } else {
                next = { cnt: cur.cnt + 1, rem: t };
            }
            const nmask = mask | (1 << i);
            const exist = dp[nmask];
            if (
                next.cnt < exist.cnt ||
                (next.cnt === exist.cnt && next.rem > exist.rem)
            ) {
                dp[nmask] = next;
            }
        }
    }

    return dp[totalMask - 1].cnt;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @param Integer $sessionTime
     * @return Integer
     */
    function minSessions($tasks, $sessionTime) {
        $n = count($tasks);
        $fullMask = (1 << $n) - 1;
        $dp = array_fill(0, $fullMask + 1, null);
        // [sessions used, time used in current session]
        $dp[0] = [1, 0];

        for ($mask = 0; $mask <= $fullMask; $mask++) {
            if ($dp[$mask] === null) continue;
            [$sess, $used] = $dp[$mask];
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) !== 0) continue;
                $newMask = $mask | (1 << $i);
                $t = $tasks[$i];
                if ($used + $t <= $sessionTime) {
                    $cand = [$sess, $used + $t];
                } else {
                    $cand = [$sess + 1, $t];
                }
                if (
                    $dp[$newMask] === null ||
                    $cand[0] < $dp[$newMask][0] ||
                    ($cand[0] == $dp[$newMask][0] && $cand[1] < $dp[$newMask][1])
                ) {
                    $dp[$newMask] = $cand;
                }
            }
        }

        return $dp[$fullMask][0];
    }
}
```

## Swift

```swift
class Solution {
    func minSessions(_ tasks: [Int], _ sessionTime: Int) -> Int {
        let n = tasks.count
        let totalMask = 1 << n
        var dp = Array(repeating: (sessions: Int.max, remaining: 0), count: totalMask)
        dp[0] = (1, sessionTime)
        
        for mask in 0..<totalMask {
            let cur = dp[mask]
            if cur.sessions == Int.max { continue }
            for i in 0..<n where (mask & (1 << i)) == 0 {
                var nextSessions = cur.sessions
                var nextRemaining = cur.remaining
                if tasks[i] <= cur.remaining {
                    nextRemaining -= tasks[i]
                } else {
                    nextSessions += 1
                    nextRemaining = sessionTime - tasks[i]
                }
                let newMask = mask | (1 << i)
                let existing = dp[newMask]
                if nextSessions < existing.sessions || (nextSessions == existing.sessions && nextRemaining > existing.remaining) {
                    dp[newMask] = (nextSessions, nextRemaining)
                }
            }
        }
        
        return dp[totalMask - 1].sessions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSessions(tasks: IntArray, sessionTime: Int): Int {
        val n = tasks.size
        val totalMask = 1 shl n
        val sum = IntArray(totalMask)
        for (mask in 1 until totalMask) {
            val lsb = mask and -mask
            val idx = Integer.numberOfTrailingZeros(lsb)
            sum[mask] = sum[mask xor lsb] + tasks[idx]
        }
        val valid = BooleanArray(totalMask)
        for (mask in 0 until totalMask) {
            if (sum[mask] <= sessionTime) valid[mask] = true
        }
        val dp = IntArray(totalMask) { Int.MAX_VALUE / 2 }
        dp[0] = 0
        for (mask in 1 until totalMask) {
            var sub = mask
            while (sub > 0) {
                if (valid[sub]) {
                    val candidate = dp[mask xor sub] + 1
                    if (candidate < dp[mask]) dp[mask] = candidate
                }
                sub = (sub - 1) and mask
            }
        }
        return dp[totalMask - 1]
    }
}
```

## Dart

```dart
class Solution {
  int minSessions(List<int> tasks, int sessionTime) {
    int n = tasks.length;
    int totalMask = 1 << n;
    List<int> sum = List.filled(totalMask, 0);
    for (int mask = 1; mask < totalMask; ++mask) {
      int lsb = mask & -mask;
      int idx = lsb.bitLength - 1;
      sum[mask] = sum[mask ^ lsb] + tasks[idx];
    }
    List<int> dp = List.filled(totalMask, n + 1);
    dp[0] = 0;
    for (int mask = 1; mask < totalMask; ++mask) {
      int sub = mask;
      while (sub > 0) {
        if (sum[sub] <= sessionTime) {
          int candidate = dp[mask ^ sub] + 1;
          if (candidate < dp[mask]) dp[mask] = candidate;
        }
        sub = (sub - 1) & mask;
      }
    }
    return dp[totalMask - 1];
  }
}
```

## Golang

```go
func minSessions(tasks []int, sessionTime int) int {
    n := len(tasks)
    totalMask := 1 << n
    type State struct {
        sessions int
        cur      int
    }
    dp := make([]State, totalMask)
    // Initialize with large values
    for i := 0; i < totalMask; i++ {
        dp[i] = State{sessions: n + 1, cur: sessionTime}
    }
    dp[0] = State{sessions: 1, cur: 0}

    for mask := 0; mask < totalMask; mask++ {
        for i := 0; i < n; i++ {
            if mask>>i&1 == 0 {
                newMask := mask | (1 << i)
                curState := dp[mask]
                var cand State
                if curState.cur+tasks[i] <= sessionTime {
                    cand = State{sessions: curState.sessions, cur: curState.cur + tasks[i]}
                } else {
                    cand = State{sessions: curState.sessions + 1, cur: tasks[i]}
                }
                // Choose better state: fewer sessions, then smaller current time
                if cand.sessions < dp[newMask].sessions ||
                    (cand.sessions == dp[newMask].sessions && cand.cur < dp[newMask].cur) {
                    dp[newMask] = cand
                }
            }
        }
    }
    return dp[totalMask-1].sessions
}
```

## Ruby

```ruby
def min_sessions(tasks, session_time)
  n = tasks.length
  full_mask = (1 << n) - 1
  dp = Array.new(1 << n) { [Float::INFINITY, Float::INFINITY] }
  dp[0] = [1, 0]

  (0..full_mask).each do |mask|
    cur_sessions, cur_time = dp[mask]
    next if cur_sessions == Float::INFINITY

    n.times do |i|
      bit = 1 << i
      next if (mask & bit) != 0

      new_mask = mask | bit
      t = tasks[i]

      if cur_time + t <= session_time
        cand = [cur_sessions, cur_time + t]
      else
        cand = [cur_sessions + 1, t]
      end

      best = dp[new_mask]
      if cand[0] < best[0] || (cand[0] == best[0] && cand[1] < best[1])
        dp[new_mask] = cand
      end
    end
  end

  dp[full_mask][0]
end
```

## Scala

```scala
object Solution {
    def minSessions(tasks: Array[Int], sessionTime: Int): Int = {
        val n = tasks.length
        val totalMask = 1 << n
        val INF = Int.MaxValue / 2

        val dpSess = Array.fill(totalMask)(INF)
        val dpRem = Array.fill(totalMask)(0)

        dpSess(0) = 1               // start with one session having full capacity
        dpRem(0) = sessionTime

        for (mask <- 0 until totalMask) {
            val curSess = dpSess(mask)
            val curRem = dpRem(mask)
            if (curSess < INF) {
                var i = 0
                while (i < n) {
                    if ((mask & (1 << i)) == 0) {
                        val t = tasks(i)
                        var newSess = curSess
                        var newRem = curRem
                        if (t <= curRem) {
                            newRem = curRem - t
                        } else {
                            newSess += 1
                            newRem = sessionTime - t
                        }
                        val nextMask = mask | (1 << i)
                        if (newSess < dpSess(nextMask) || (newSess == dpSess(nextMask) && newRem > dpRem(nextMask))) {
                            dpSess(nextMask) = newSess
                            dpRem(nextMask) = newRem
                        }
                    }
                    i += 1
                }
            }
        }

        dpSess(totalMask - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_sessions(tasks: Vec<i32>, session_time: i32) -> i32 {
        let n = tasks.len();
        let full = 1usize << n;
        // dp[mask] = (sessions_used, remaining_time_in_last_session)
        let mut dp = vec![(i32::MAX, i32::MAX); full];
        dp[0] = (1, 0);
        for mask in 0..full {
            let (sess, rem) = dp[mask];
            if sess == i32::MAX {
                continue;
            }
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let new_mask = mask | (1 << i);
                    let t = tasks[i];
                    let (new_sess, new_rem) = if rem + t <= session_time {
                        (sess, rem + t)
                    } else {
                        (sess + 1, t)
                    };
                    let cur = dp[new_mask];
                    if new_sess < cur.0 || (new_sess == cur.0 && new_rem < cur.1) {
                        dp[new_mask] = (new_sess, new_rem);
                    }
                }
            }
        }
        dp[full - 1].0
    }
}
```

## Racket

```racket
#lang racket

(provide min-sessions)

(define/contract (min-sessions tasks sessionTime)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length tasks))
         (totalMask (arithmetic-shift 1 n))
         (sumVec (make-vector totalMask 0))
         (dpVec (make-vector totalMask 0)))
    ;; precompute sum of each subset
    (for ([mask (in-range totalMask)])
      (let ((s 0))
        (for ([i (in-range n)])
          (when (not (zero? (bitwise-and mask (arithmetic-shift 1 i))))
            (set! s (+ s (list-ref tasks i)))))
        (vector-set! sumVec mask s)))
    ;; DP over subsets
    (for ([mask (in-range 1 totalMask)])
      (let loop ((sub mask) (best n))
        (if (= sub 0)
            (vector-set! dpVec mask best)
            (let* ((subset-sum (vector-ref sumVec sub))
                   (cand (if (<= subset-sum sessionTime)
                             (+ 1 (vector-ref dpVec (bitwise-xor mask sub)))
                             best))
                   (new-best (if (< cand best) cand best)))
              (loop (bitwise-and (- sub) mask) new-best)))))
    (vector-ref dpVec (- totalMask 1))))
```

## Erlang

```erlang
-module(solution).
-export([min_sessions/2]).

-spec min_sessions(Tasks :: [integer()], SessionTime :: integer()) -> integer().
min_sessions(Tasks, SessionTime) ->
    N = length(Tasks),
    MaxMask = (1 bsl N) - 1,
    InitialDP = maps:put(0, {1, 0}, #{}),
    FinalDP = loop(0, MaxMask, Tasks, SessionTime, InitialDP),
    {Sessions, _} = maps:get(MaxMask, FinalDP),
    Sessions.

loop(Mask, MaxMask, _Tasks, _SessionTime, DP) when Mask > MaxMask ->
    DP;
loop(Mask, MaxMask, Tasks, SessionTime, DP) ->
    case maps:get(Mask, DP, undefined) of
        undefined ->
            loop(Mask + 1, MaxMask, Tasks, SessionTime, DP);
        {S, C} ->
            UpdatedDP = try_add_tasks(Mask, S, C, Tasks, SessionTime, DP),
            loop(Mask + 1, MaxMask, Tasks, SessionTime, UpdatedDP)
    end.

try_add_tasks(Mask, S, C, Tasks, SessionTime, DP) ->
    N = length(Tasks),
    try_add_task(0, N, Mask, S, C, Tasks, SessionTime, DP).

try_add_task(I, N, _Mask, _S, _C, _Tasks, _SessionTime, DP) when I >= N ->
    DP;
try_add_task(I, N, Mask, S, C, Tasks, SessionTime, DP) ->
    Bit = 1 bsl I,
    case (Mask band Bit) of
        0 ->
            TaskTime = lists:nth(I + 1, Tasks),
            {NewS, NewC} =
                if C + TaskTime =< SessionTime ->
                        {S, C + TaskTime};
                   true ->
                        {S + 1, TaskTime}
                end,
            NewMask = Mask bor Bit,
            Existing = maps:get(NewMask, DP, undefined),
            UpdatedState =
                case Existing of
                    undefined -> {NewS, NewC};
                    {ES, EC} ->
                        if NewS < ES;
                           (NewS == ES andalso NewC < EC) ->
                                {NewS, NewC};
                           true ->
                                {ES, EC}
                        end
                end,
            DP1 = maps:put(NewMask, UpdatedState, DP),
            try_add_task(I + 1, N, Mask, S, C, Tasks, SessionTime, DP1);
        _ ->
            try_add_task(I + 1, N, Mask, S, C, Tasks, SessionTime, DP)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_sessions(tasks :: [integer], session_time :: integer) :: integer
  def min_sessions(tasks, session_time) do
    import Bitwise

    n = length(tasks)
    total = 1 <<< n
    inf = 1_000_000

    dp =
      :array.new(total, default: {inf, inf})
      |> :array.set(0, {1, 0})

    dp =
      Enum.reduce(0..total - 1, dp, fn mask, acc ->
        {sessions, used} = :array.get(mask, acc)

        if sessions == inf do
          acc
        else
          Enum.with_index(tasks)
          |> Enum.reduce(acc, fn {t, i}, a2 ->
            bit = 1 <<< i

            if (mask &&& bit) != 0 do
              a2
            else
              new_mask = mask ||| bit

              cand =
                if used + t <= session_time do
                  {sessions, used + t}
                else
                  {sessions + 1, t}
                end

              {c_sess, c_used} = cand
              {o_sess, o_used} = :array.get(new_mask, a2)

              better? =
                c_sess < o_sess or (c_sess == o_sess and c_used < o_used)

              if better? do
                :array.set(new_mask, cand, a2)
              else
                a2
              end
            end
          end)
        end
      end)

    {answer, _} = :array.get(total - 1, dp)
    answer
  end
end
```
