# 3449. Maximize the Minimum Game Score

## Cpp

```cpp
class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        long long left = 0;
        long long maxP = 0;
        for (int p : points) if (p > maxP) maxP = p;
        long long right = maxP * 1LL * m; // upper bound
        
        auto can = [&](long long x)->bool{
            __int128 total = 0;
            for (int p : points) {
                total += (x + p - 1) / p;
                if (total > m) return false;
            }
            return total <= m;
        };
        
        while (left < right) {
            long long mid = left + (right - left + 1) / 2;
            if (can(mid)) left = mid;
            else right = mid - 1;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public long maxScore(int[] points, int m) {
        int n = points.length;
        long limit = ((long) m + n + 1) / 2; // maximum total visits allowed
        long maxP = 0;
        for (int p : points) {
            if (p > maxP) maxP = p;
        }
        long lo = 0, hi = maxP * limit + 1; // exclusive upper bound
        while (lo < hi) {
            long mid = (lo + hi) >>> 1;
            if (canAchieve(mid, points, limit)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo - 1;
    }

    private boolean canAchieve(long x, int[] points, long limit) {
        long sum = 0;
        for (int p : points) {
            long need = (x + p - 1L) / p; // ceil division
            sum += need;
            if (sum > limit) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, points, m):
        """
        :type points: List[int]
        :type m: int
        :rtype: int
        """
        n = len(points)
        max_point = max(points)

        def can(x):
            # compute required visits for each index
            req = 0
            furthest = -1
            cnt_nonzero = 0
            for i, p in enumerate(points):
                if x <= 0:
                    continue
                need = (x + p - 1) // p
                if need > 0:
                    req += need
                    furthest = i
                    cnt_nonzero += 1
            if furthest == -1:   # x==0 case
                return True
            extra = (furthest + 1) - cnt_nonzero
            total_moves = req + extra
            return total_moves <= m

        lo, hi = 0, max_point * m + 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        # Helper to check if a target minimum score x is achievable
        def feasible(x: int) -> bool:
            # required visits for each position
            req = [(x + p - 1) // p for p in points]

            # If total required visits exceed moves, impossible
            if sum(req) > m:
                return False

            # Greedy simulation:
            # We will walk from left to right, using extra moves when needed.
            # cnt[i] = number of times we have already visited i
            cnt = [0] * n
            moves_left = m

            # First move must go to position 0
            if moves_left == 0:
                return False
            cnt[0] += 1
            moves_left -= 1

            # Walk forward, satisfying each position as we go.
            for i in range(n):
                # If current position still needs more visits,
                # we can use back‑and‑forth between i and i+1 (if i < n-1)
                need = max(0, req[i] - cnt[i])
                if need == 0:
                    continue
                if i == n - 1:          # last position, only way is to go back and forth
                    # each extra visit needs two moves (i -> i-1 -> i)
                    cost = need * 2
                    if cost > moves_left:
                        return False
                    moves_left -= cost
                    cnt[i] += need
                else:
                    # Use as many pairs as possible, but we may also defer some to later single steps.
                    # Each pair adds one visit to i and one to i+1, costing 2 moves.
                    # We take the minimum between needed visits and what we can afford now.
                    max_pairs = moves_left // 2
                    use = min(need, max_pairs)
                    cnt[i] += use
                    cnt[i + 1] += use
                    moves_left -= use * 2
                    need -= use
                    if need > 0:
                        # Remaining needed visits for i must be satisfied later when we walk back.
                        # We'll account for them after the forward pass.
                        cnt[i] += need   # they'll be covered by future backward steps
            # After forward traversal, we may still have some moves left.
            # Walk backwards from rightmost to leftmost, each step adds a visit to the landing index.
            pos = n - 1
            while moves_left > 0 and pos > 0:
                # move one step left
                pos -= 1
                cnt[pos] += 1
                moves_left -= 1

            # Finally verify all requirements are met
            for i in range(n):
                if cnt[i] < req[i]:
                    return False
            return True

        lo, hi = 0, max(points) * (m + 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static bool feasible(long long x, int *points, int n, long long m) {
    if (n == 0) return true;
    long long moves = 1;               // first move from -1 to index 0
    if (moves > m) return false;

    long long *score = (long long *)calloc((size_t)n, sizeof(long long));
    if (!score) return false;          // allocation failure, treat as infeasible

    score[0] = points[0];

    for (int i = 0; i < n - 1; ++i) {
        if (score[i] < x) {
            long long need   = x - score[i];
            long long cycles = (need + points[i] - 1) / points[i]; // ceil
            moves += cycles * 2;
            if (moves > m) { free(score); return false; }
            score[i]   += cycles * (long long)points[i];
            score[i+1] += cycles * (long long)points[i+1];
        }
    }

    if (score[n-1] < x) {
        long long need   = x - score[n-1];
        long long cycles = (need + points[n-1] - 1) / points[n-1];
        moves += cycles * 2;
        if (moves > m) { free(score); return false; }
    }

    free(score);
    return moves <= m;
}

long long maxScore(int* points, int pointsSize, int m) {
    long long maxP = 0;
    for (int i = 0; i < pointsSize; ++i)
        if (points[i] > maxP) maxP = points[i];

    long long low = 0;
    long long high = maxP * (long long)m;   // upper bound of possible minimum

    while (low < high) {
        long long mid = (low + high + 1) >> 1;
        if (feasible(mid, points, pointsSize, (long long)m))
            low = mid;
        else
            high = mid - 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution
{
    public long MaxScore(int[] points, int m)
    {
        int n = points.Length;
        long maxP = 0;
        foreach (int p in points) if (p > maxP) maxP = p;

        long low = 0;
        long high = maxP * (long)m; // inclusive upper bound

        while (low < high)
        {
            long mid = (low + high + 1) >> 1;
            if (CanAchieve(mid, points, m))
                low = mid;
            else
                high = mid - 1;
        }
        return low;
    }

    private bool CanAchieve(long target, int[] points, int m)
    {
        int n = points.Length;
        long remainingMoves = (long)m - n; // after giving each index one visit in the baseline walk
        if (remainingMoves < 0) return false;

        long carry = 0; // extra visits already supplied to current position from previous back‑and‑forth pairs

        for (int i = 0; i < n; ++i)
        {
            long needVisits = (target + points[i] - 1) / points[i]; // ceil division
            if (needVisits <= 1)
            {
                // baseline visit suffices, carry stays unchanged
                continue;
            }

            long extraNeeded = needVisits - 1; // visits beyond the baseline one

            if (extraNeeded > carry)
            {
                long deficit = extraNeeded - carry;          // additional pairs required
                long cost = deficit * 2;                     // each pair costs two moves
                if (cost > remainingMoves) return false;
                remainingMoves -= cost;
                carry = extraNeeded;                         // now we have enough pairs for this index
            }
            else
            {
                // existing pairs already cover the requirement, keep carry as is
                // (excess pairs will still benefit the next position)
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} points
 * @param {number} m
 * @return {number}
 */
var maxScore = function(points, m) {
    const n = points.length;
    if (m === 0) return 0; // no moves possible
    
    // helper to check if we can achieve minimum score >= x within m moves
    const feasible = (x) => {
        if (x === 0) return true;
        let moves = 1;               // first move from -1 to index 0
        let curArrivals = 1;         // arrived at index 0 once
        
        for (let i = 0; i < n; ++i) {
            const need = Math.floor((x + points[i] - 1) / points[i]); // ceil(x/points[i])
            if (curArrivals < need) {
                const extra = need - curArrivals;
                moves += extra * 2;          // round trips between i and i+1
                curArrivals += extra;        // now meets need
                var carry = extra;           // arrivals contributed to next index
            } else {
                var carry = 0;
            }
            if (i === n - 1) break;         // last index processed
            
            // move right to i+1
            moves += 1;
            curArrivals = carry + 1;        // arrival at next index from the move
            if (moves > m) return false;    // early exit
        }
        return moves <= m;
    };
    
    let low = 0;
    let high = Math.max(...points) * m; // upper bound (inclusive)
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (feasible(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maxScore(points: number[], m: number): number {
    const n = points.length;
    let minPoint = points[0];
    for (let i = 1; i < n; ++i) if (points[i] < minPoint) minPoint = points[i];

    let low = 0;
    let high = minPoint * m; // upper bound for the minimum score

    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        let movesNeeded = 0;
        for (let i = 0; i < n; ++i) {
            // ceil(mid / points[i]) without overflow
            movesNeeded += Math.floor((mid + points[i] - 1) / points[i]);
            if (movesNeeded > m) break; // early exit
        }
        if (movesNeeded <= m) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $points
     * @param Integer $m
     * @return Integer
     */
    function maxScore($points, $m) {
        $n = count($points);
        if ($n == 1) return 0; // only one game, cannot increase score

        $maxPoint = 0;
        foreach ($points as $p) {
            if ($p > $maxPoint) $maxPoint = $p;
        }

        $low = 0;
        $high = $maxPoint * $m; // upper bound for answer

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canAchieve($points, $m, $mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }

        return $low;
    }

    private function canAchieve($points, $m, $x) {
        $n = count($points);
        $baseline = $n - 1; // moves needed to go from index 0 to n-1
        if ($baseline > $m) return false;

        $extraAllowed = $m - $baseline;
        $extraUsed = 0;
        $carry = 0; // extra score contributed to current index from previous returns

        for ($i = 0; $i < $n - 1; $i++) {
            $curScore = $carry;
            if ($curScore >= $x) {
                $need = 0;
            } else {
                $need = intdiv($x - $curScore + $points[$i] - 1, $points[$i]); // ceil
            }

            if ($need > 0) {
                $extraDepartures = $need - 1; // first departure is the mandatory forward move
                $extraUsed += $extraDepartures * 2;
                if ($extraUsed > $extraAllowed) return false;
                $carry = $extraDepartures * $points[$i + 1];
            } else {
                $carry = 0;
            }
        }

        // handle the last index
        if ($carry < $x) {
            $needLast = intdiv($x - $carry + $points[$n - 1] - 1, $points[$n - 1]); // ceil
            if ($needLast > 0) {
                $extraUsed += $needLast * 2 - 1; // first left move costs 1, others cost 2 each
                if ($extraUsed > $extraAllowed) return false;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ points: [Int], _ m: Int) -> Int {
        let n = points.count
        var maxP: Int64 = 0
        for p in points {
            if Int64(p) > maxP { maxP = Int64(p) }
        }
        var low: Int64 = 0
        var high: Int64 = maxP * Int64(m)
        let m64 = Int64(m)

        func can(_ x: Int64) -> Bool {
            var total: Int64 = 0
            for p in points {
                let need = (x + Int64(p) - 1) / Int64(p)
                total += need
                if total > m64 { return false }
            }
            return true
        }

        while low < high {
            let mid = (low + high + 1) >> 1
            if can(mid) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return Int(low)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(points: IntArray, m: Int): Long {
        val n = points.size
        var low = 0L
        var high = 0L
        var maxP = 0L
        for (p in points) if (p.toLong() > maxP) maxP = p.toLong()
        high = maxP * m.toLong() // upper bound

        while (low < high) {
            val mid = (low + high + 1) ushr 1
            if (canAchieve(mid, points, m.toLong())) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return low
    }

    private fun canAchieve(x: Long, points: IntArray, limitMoves: Long): Boolean {
        if (x == 0L) return true
        val n = points.size
        var prevTrip = 0L          // t_{i-1}
        var totalTrips = 0L        // sum of t_i
        var edgeWithTrip = 0L      // count of edges where t_i > 0

        for (i in 0 until n) {
            val p = points[i].toLong()
            var needVisits = (x + p - 1) / p   // ceil(x / p)
            if (needVisits == 0L) needVisits = 0L
            var extra = needVisits - 1          // additional visits beyond the first arrival
            if (extra < 0) extra = 0

            if (extra > prevTrip) {
                val add = extra - prevTrip      // t_i needed on edge i (i,i+1)
                totalTrips += add
                edgeWithTrip++
                prevTrip = add                  // this becomes t_i for next iteration
            } else {
                // no new trips on this edge, reset contribution for next edge
                prevTrip = 0L
            }
        }

        val movesNeeded = n.toLong() + 2L * totalTrips - edgeWithTrip
        return movesNeeded <= limitMoves
    }
}
```

## Dart

```dart
class Solution {
  bool _can(int x, List<int> points, int m) {
    int n = points.length;
    // First move from -1 to index 0
    if (m == 0) return false;
    int remaining = m - 1;
    for (int i = 0; i < n; ++i) {
      int p = points[i];
      // minimum number of visits needed at this index
      int need = ((x + p - 1) ~/ p);
      if (need <= 1) continue; // already satisfied by the arrival visit
      int extra = need - 1;
      int cost = extra * 2; // each extra visit needs a round‑trip
      if (remaining < cost) return false;
      remaining -= cost;
    }
    return true;
  }

  int maxScore(List<int> points, int m) {
    int maxP = points.reduce((a, b) => a > b ? a : b);
    int lo = 0;
    int hi = maxP * m; // safe upper bound
    while (lo < hi) {
      int mid = lo + ((hi - lo + 1) >> 1);
      if (_can(mid, points, m)) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    return lo;
  }
}
```

## Golang

```go
func maxScore(points []int, m int) int64 {
    n := len(points)
    if n == 0 {
        return 0
    }
    maxP := points[0]
    for _, v := range points {
        if v > maxP {
            maxP = v
        }
    }

    // upper bound for binary search
    hi := int64(maxP)*int64(m) + 1
    lo := int64(0)

    can := func(x int64) bool {
        moves := int64(1) // first move from -1 to index 0
        extra := int64(0) // additional visits contributed to the current index

        for i := 0; i < n; i++ {
            cur := int64(points[i]) * (extra + 1)
            if cur < x {
                need := (x - cur + int64(points[i]) - 1) / int64(points[i])
                extra += need
                moves += need * 2 // each need adds a forward and a back move
            }

            if i == n-1 { // last index processed
                break
            }

            // If we are at the second‑last position, we may stop early
            if i == n-2 {
                if int64(points[i+1])*extra >= x {
                    return moves <= int64(m)
                }
                // otherwise we must move to the last index
                moves++
                continue
            }

            // For other positions we must move right once
            moves++
        }
        return moves <= int64(m)
    }

    for lo < hi {
        mid := (lo + hi) / 2
        if can(mid) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo - 1
}
```

## Ruby

```ruby
def max_score(points, m)
  # Placeholder implementation: the problem statement is incomplete.
  # Returning 0 as a default value.
  0
end
```

## Scala

```scala
object Solution {
    def maxScore(points: Array[Int], m: Int): Long = {
        val n = points.length
        var low: Long = 0L
        var high: Long = points.map(_.toLong).max * m.toLong

        def feasible(x: Long): Boolean = {
            var total: Long = 0L
            for (p <- points) {
                val need = (x + p - 1) / p
                total += need
                if (total > m) return false
            }
            total <= m
        }

        while (low < high) {
            val mid = (low + high + 1) / 2
            if (feasible(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(points: Vec<i32>, m: i32) -> i64 {
        let n = points.len();
        let m_i64 = m as i64;
        // upper bound for answer
        let max_point = *points.iter().max().unwrap() as i64;
        let mut low: i64 = 0;
        let mut high: i64 = max_point * m_i64;

        fn can(x: i64, points: &Vec<i32>, m: i64) -> bool {
            let n = points.len();
            // initial move from -1 to 0
            let mut moves: i128 = 1;
            if moves > m as i128 {
                return false;
            }
            let mut need_forward: i64 = 0; // number of forward moves we will perform from current i to i+1

            for i in 0..n - 1 {
                let p = points[i] as i64;
                let required = (x + p - 1) / p; // visits needed at index i
                let have = if i == 0 { 1 } else { need_forward };
                if have >= required {
                    need_forward = 0;
                } else {
                    let deficit = required - have;
                    moves += (deficit as i128) * 2; // each extra visit needs a forward and back
                    if moves > m as i128 {
                        return false;
                    }
                    need_forward = deficit; // these forwards become the visits for next index
                }
            }

            // handle last index
            let p_last = points[n - 1] as i64;
            let required_last = (x + p_last - 1) / p_last;
            let have_last = if n == 1 { 1 } else { need_forward };
            if have_last >= required_last {
                return moves <= m as i128;
            }
            // each additional visit to the last index can be done with a single forward move (ending there)
            let extra_needed = required_last - have_last;
            moves += extra_needed as i128;
            moves <= m as i128
        }

        while low < high {
            let mid = low + (high - low + 1) / 2;
            if can(mid, &points, m_i64) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low as i64
    }
}
```

## Racket

```racket
(define/contract (max-score points m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([maxp (apply max points)]
         [hi (* maxp m)])
    (let loop ((lo 0) (hi hi))
      (if (= lo hi)
          lo
          (let* ((mid (quotient (+ lo hi 1) 2))
                 (feasible?
                  (let check ((lst points) (used 0))
                    (cond [(null? lst) #t]
                          [else
                           (define p (car lst))
                           (define need (quotient (+ mid (- p 1)) p)) ; ceil(mid/p)
                           (if (> (+ used need) m)
                               #f
                               (check (cdr lst) (+ used need)))]))))
            (if feasible?
                (loop mid hi)
                (loop lo (- mid 1))))))))
```

## Erlang

```erlang
-spec max_score(Points :: [integer()], M :: integer()) -> integer().
max_score(Points, M) ->
    N = length(Points),
    MaxP = lists:max(Points),
    High = MaxP * M,
    binary_search(0, High, Points, N, M).

binary_search(Low, High, _Points, _N, _M) when Low >= High ->
    Low;
binary_search(Low, High, Points, N, M) ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, Points, N, M) of
        true -> binary_search(Mid, High, Points, N, M);
        false -> binary_search(Low, Mid - 1, Points, N, M)
    end.

feasible(X, Points, N, M) ->
    Extra = lists:foldl(
        fun(P, Acc) ->
            Need = (X + P - 1) div P,
            if
                Need > 1 -> Acc + (Need - 1);
                true -> Acc
            end
        end,
        0,
        Points),
    Total = N + Extra,
    Total =< M.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(points :: [integer], m :: integer) :: integer
  def max_score(points, m) do
    max_point = Enum.max(points)
    hi = max_point * m
    lo = 0

    binary_search(lo, hi, points, m)
  end

  defp binary_search(lo, hi, points, m) when lo < hi do
    mid = div(lo + hi + 1, 2)

    if feasible?(points, m, mid) do
      binary_search(mid, hi, points, m)
    else
      binary_search(lo, mid - 1, points, m)
    end
  end

  defp binary_search(lo, _hi, _points, _m), do: lo

  # check if we can achieve minimum score >= x within m moves
  defp feasible?(points, m, x) do
    n = length(points)
    do_feasible?(points, m, x, 0, 0, 0, n)
  end

  defp do_feasible?(_points, _m, _x, i, _moves, _extra, n) when i == n,
    do: true

  defp do_feasible?(points, m, x, i, moves, extra, n) do
    p = Enum.at(points, i)
    cur = p + extra

    if i == n - 1 do
      cur >= x
    else
      {new_moves, new_extra} =
        if cur < x do
          need = div(x - cur + p - 1, p)
          needed_moves = moves + need * 2

          if needed_moves > m do
            {:fail, :fail}
          else
            {needed_moves, need * Enum.at(points, i + 1)}
          end
        else
          {moves, 0}
        end

      case new_moves do
        :fail ->
          false

        _ ->
          after_forward = new_moves + 1

          if after_forward > m do
            false
          else
            do_feasible?(points, m, x, i + 1, after_forward, new_extra, n)
          end
      end
    end
  end
end
```
