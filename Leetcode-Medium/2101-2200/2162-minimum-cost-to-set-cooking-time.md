# 2162. Minimum Cost to Set Cooking Time

## Cpp

```cpp
class Solution {
public:
    int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        long long best = LLONG_MAX;
        for (int mm = 0; mm <= 99; ++mm) {
            int ss = targetSeconds - mm * 60;
            if (ss < 0 || ss > 99) continue;
            int d[4];
            d[0] = mm / 10;
            d[1] = mm % 10;
            d[2] = ss / 10;
            d[3] = ss % 10;
            for (int len = 1; len <= 4; ++len) {
                long long cost = 0;
                int cur = startAt;
                for (int i = 4 - len; i < 4; ++i) {
                    if (cur != d[i]) {
                        cost += moveCost;
                        cur = d[i];
                    }
                    cost += pushCost;
                }
                best = min(best, cost);
            }
        }
        return (int)best;
    }
};
```

## Java

```java
class Solution {
    public int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        int best = Integer.MAX_VALUE;
        for (int mm = 0; mm <= 99; ++mm) {
            int ss = targetSeconds - mm * 60;
            if (ss < 0 || ss > 99) continue;
            int[] d = new int[4];
            d[0] = mm / 10;
            d[1] = mm % 10;
            d[2] = ss / 10;
            d[3] = ss % 10;

            int idx = 0;
            while (idx < 4 && d[idx] == 0) idx++; // skip leading zeros
            if (idx == 4) continue; // should not happen for targetSeconds > 0

            int cur = startAt;
            int cost = 0;
            for (int i = idx; i < 4; ++i) {
                if (cur != d[i]) {
                    cost += moveCost;
                    cur = d[i];
                }
                cost += pushCost;
            }
            best = Math.min(best, cost);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        INF = 10**18
        best = INF

        def cost(seq):
            cur = startAt
            total = 0
            for ch in seq:
                d = ord(ch) - 48
                if cur != d:
                    total += moveCost
                    cur = d
                total += pushCost
            return total

        for mm in range(100):
            ss = targetSeconds - mm * 60
            if 0 <= ss <= 99:
                s = "{:02d}{:02d}".format(mm, ss)  # four digits string
                # find first non-zero index (or length if all zeros)
                first_non_zero = 0
                while first_non_zero < 4 and s[first_non_zero] == '0':
                    first_non_zero += 1
                # we can omit any leading zeros, i.e., start at any i <= first_non_zero
                for i in range(first_non_zero + 1):
                    seq = s[i:]
                    best = min(best, cost(seq))

        return best
```

## Python3

```python
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        INF = 10**18
        best = INF

        for mm in range(100):
            ss = targetSeconds - mm * 60
            if 0 <= ss <= 99:
                s = f"{mm:02d}{ss:02d}"  # four‑digit representation
                # consider all suffixes of length 1..4
                for k in range(1, 5):
                    seq = s[4 - k:]  # last k characters
                    cur = startAt
                    cost = 0
                    for ch in seq:
                        d = ord(ch) - 48  # faster int conversion
                        if cur != d:
                            cost += moveCost
                            cur = d
                        cost += pushCost
                    if cost < best:
                        best = cost

        return best
```

## C

```c
#include <limits.h>

int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
    int ans = INT_MAX;
    for (int mm = 0; mm <= 99; ++mm) {
        int ss = targetSeconds - mm * 60;
        if (ss < 0 || ss > 99) continue;
        int d[4];
        d[0] = mm / 10;
        d[1] = mm % 10;
        d[2] = ss / 10;
        d[3] = ss % 10;

        int firstNZ = 0;
        while (firstNZ < 4 && d[firstNZ] == 0) ++firstNZ;

        for (int i = 0; i <= firstNZ; ++i) {
            int cost = 0;
            int cur = startAt;
            for (int j = i; j < 4; ++j) {
                if (cur != d[j]) {
                    cost += moveCost;
                    cur = d[j];
                }
                cost += pushCost;
            }
            if (cost < ans) ans = cost;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds)
    {
        int best = int.MaxValue;
        for (int mm = 0; mm <= 99; ++mm)
        {
            int ss = targetSeconds - mm * 60;
            if (ss < 0 || ss > 99) continue;

            string fourDigits = $"{mm:D2}{ss:D2}";
            int idx = 0;
            while (idx < fourDigits.Length - 1 && fourDigits[idx] == '0')
                idx++;
            string seq = fourDigits.Substring(idx);

            int cost = ComputeCost(seq, startAt, moveCost, pushCost);
            if (cost < best) best = cost;
        }
        return best;
    }

    private int ComputeCost(string seq, int startAt, int moveCost, int pushCost)
    {
        int cur = startAt;
        int total = 0;
        foreach (char ch in seq)
        {
            int d = ch - '0';
            if (cur != d)
            {
                total += moveCost;
                cur = d;
            }
            total += pushCost;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} startAt
 * @param {number} moveCost
 * @param {number} pushCost
 * @param {number} targetSeconds
 * @return {number}
 */
var minCostSetTime = function(startAt, moveCost, pushCost, targetSeconds) {
    let best = Number.MAX_SAFE_INTEGER;
    for (let mm = 0; mm <= 99; ++mm) {
        const ss = targetSeconds - mm * 60;
        if (ss < 0 || ss > 99) continue;

        const m1 = Math.floor(mm / 10);
        const m2 = mm % 10;
        const s1 = Math.floor(ss / 10);
        const s2 = ss % 10;
        const str = '' + m1 + m2 + s1 + s2; // exactly 4 digits

        for (let i = 0; i < 4; ++i) {
            const suffix = str.slice(i);
            if (!suffix.length) continue;

            let cur = startAt;
            let cost = 0;
            for (let ch of suffix) {
                const d = ch.charCodeAt(0) - 48; // digit value
                if (d !== cur) {
                    cost += moveCost;
                    cur = d;
                }
                cost += pushCost;
            }
            if (cost < best) best = cost;
        }
    }
    return best;
};
```

## Typescript

```typescript
function minCostSetTime(startAt: number, moveCost: number, pushCost: number, targetSeconds: number): number {
    let best = Number.MAX_SAFE_INTEGER;

    for (let mm = 0; mm <= 99; ++mm) {
        const ss = targetSeconds - mm * 60;
        if (ss < 0 || ss > 99) continue;

        const mmStr = mm.toString().padStart(2, '0');
        const ssStr = ss.toString().padStart(2, '0');
        const s = mmStr + ssStr; // length 4

        for (let p = 0; p < 4; ++p) {
            let ok = true;
            for (let k = 0; k < p; ++k) {
                if (s[k] !== '0') { ok = false; break; }
            }
            if (!ok) continue;

            const seq = s.slice(p);
            let cur = startAt;
            let cost = 0;
            for (const ch of seq) {
                const d = ch.charCodeAt(0) - 48; // faster than Number(ch)
                if (cur !== d) {
                    cost += moveCost;
                    cur = d;
                }
                cost += pushCost;
            }
            if (cost < best) best = cost;
        }
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $startAt
     * @param Integer $moveCost
     * @param Integer $pushCost
     * @param Integer $targetSeconds
     * @return Integer
     */
    function minCostSetTime($startAt, $moveCost, $pushCost, $targetSeconds) {
        $best = PHP_INT_MAX;
        for ($mm = 0; $mm <= 99; $mm++) {
            $ss = $targetSeconds - $mm * 60;
            if ($ss < 0 || $ss > 99) continue;

            // four‑digit representation mmss with leading zeros
            $s = sprintf("%02d%02d", $mm, $ss);

            // count leading zeros that can be omitted
            $firstNonZero = 0;
            while ($firstNonZero < 4 && $s[$firstNonZero] === '0') {
                $firstNonZero++;
            }

            // try removing 0..$firstNonZero leading zeros
            for ($i = 0; $i <= $firstNonZero; $i++) {
                $sub = substr($s, $i);
                if ($sub === '') continue;

                $cost = 0;
                $cur = $startAt;
                $len = strlen($sub);
                for ($j = 0; $j < $len; $j++) {
                    $d = intval($sub[$j]);
                    if ($cur !== $d) {
                        $cost += $moveCost;
                        $cur = $d;
                    }
                    $cost += $pushCost;
                }
                if ($cost < $best) $best = $cost;
            }
        }
        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func minCostSetTime(_ startAt: Int, _ moveCost: Int, _ pushCost: Int, _ targetSeconds: Int) -> Int {
        var answer = Int.max
        for minutes in 0...99 {
            let seconds = targetSeconds - minutes * 60
            if seconds < 0 || seconds > 99 { continue }
            
            // digits: MMSS as four separate digits
            let d0 = minutes / 10
            let d1 = minutes % 10
            let d2 = seconds / 10
            let d3 = seconds % 10
            let digits = [d0, d1, d2, d3]
            
            // find first non‑zero digit (if all zero, skip)
            var firstNZ = 0
            while firstNZ < 4 && digits[firstNZ] == 0 {
                firstNZ += 1
            }
            if firstNZ == 4 { continue }   // not possible for targetSeconds >= 1
            
            // we may omit any number of leading zeros (including none)
            for startIdx in 0...firstNZ {
                var cur = startAt
                var cost = 0
                for i in startIdx..<4 {
                    let d = digits[i]
                    if cur != d {
                        cost += moveCost
                        cur = d
                    }
                    cost += pushCost
                }
                answer = min(answer, cost)
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int {
        var answer = Int.MAX_VALUE
        for (mm in 0..99) {
            val ss = targetSeconds - mm * 60
            if (ss < 0 || ss > 99) continue
            val digits = intArrayOf(mm / 10, mm % 10, ss / 10, ss % 10)
            for (startIdx in 0..3) {
                var cost = 0
                var cur = startAt
                for (j in startIdx..3) {
                    if (cur != digits[j]) {
                        cost += moveCost
                        cur = digits[j]
                    }
                    cost += pushCost
                }
                answer = kotlin.math.min(answer, cost)
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
    const int INF = 1 << 60;
    int answer = INF;

    for (int mm = 0; mm <= 99; ++mm) {
      int ss = targetSeconds - mm * 60;
      if (ss < 0 || ss > 99) continue;

      List<int> digits = [
        mm ~/ 10,
        mm % 10,
        ss ~/ 10,
        ss % 10
      ];

      int idx = 0;
      while (idx < 4 && digits[idx] == 0) idx++;
      if (idx == 4) continue; // should not happen for targetSeconds >= 1

      int cur = startAt;
      int cost = 0;

      for (int i = idx; i < 4; ++i) {
        int d = digits[i];
        if (d != cur) {
          cost += moveCost;
          cur = d;
        }
        cost += pushCost;
      }

      if (cost < answer) answer = cost;
    }

    return answer;
  }
}
```

## Golang

```go
func minCostSetTime(startAt int, moveCost int, pushCost int, targetSeconds int) int {
    const INF = int(^uint(0) >> 1)
    ans := INF
    for mm := 0; mm <= 99; mm++ {
        ss := targetSeconds - mm*60
        if ss < 0 || ss > 99 {
            continue
        }
        digits := []int{mm / 10, mm % 10, ss / 10, ss % 10}
        // try dropping leading zeros (0 to 3 digits)
        for i := 0; i < 4; i++ {
            ok := true
            for j := 0; j < i; j++ {
                if digits[j] != 0 {
                    ok = false
                    break
                }
            }
            if !ok {
                break // cannot drop further non‑zero digit
            }
            cur := startAt
            cost := 0
            for _, d := range digits[i:] {
                if cur != d {
                    cost += moveCost
                    cur = d
                }
                cost += pushCost
            }
            if cost < ans {
                ans = cost
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_cost_set_time(start_at, move_cost, push_cost, target_seconds)
  min_cost = Float::INFINITY

  (0..99).each do |mm|
    ss = target_seconds - mm * 60
    next if ss < 0 || ss > 99

    s = format('%02d%02d', mm, ss) # four‑digit string

    (1..4).each do |k|
      seq = s[-k, k]               # suffix of length k
      cur = start_at
      cost = 0

      seq.each_char do |ch|
        d = ch.ord - 48
        if cur != d
          cost += move_cost
          cur = d
        end
        cost += push_cost
      end

      min_cost = cost if cost < min_cost
    end
  end

  min_cost.to_i
end
```

## Scala

```scala
object Solution {
  def minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int = {
    var answer = Int.MaxValue

    // helper to compute cost of pressing a sequence of digits (as string)
    def calcCost(seq: String): Int = {
      var total = 0
      var cur = startAt
      for (ch <- seq) {
        val d = ch - '0'
        if (cur != d) total += moveCost
        total += pushCost
        cur = d
      }
      total
    }

    for (mm <- 0 to 99) {
      val ss = targetSeconds - mm * 60
      if (ss >= 0 && ss <= 99) {
        // build the four‑digit representation
        val s = f"${mm}%02d${ss}%02d"
        // remove leading zeros (they are not pressed)
        var idx = 0
        while (idx < s.length && s.charAt(idx) == '0') idx += 1
        val seq = if (idx == s.length) "0" else s.substring(idx)
        val cost = calcCost(seq)
        if (cost < answer) answer = cost
      }
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost_set_time(start_at: i32, move_cost: i32, push_cost: i32, target_seconds: i32) -> i32 {
        let mut answer = i32::MAX;

        // Helper to compute cost of pressing a sequence of digits
        let calc_cost = |digits: &[i32]| -> i32 {
            let mut total = 0;
            let mut cur = start_at;
            for &d in digits {
                if cur != d {
                    total += move_cost;
                }
                total += push_cost;
                cur = d;
            }
            total
        };

        for mm in 0..=99 {
            let ss = target_seconds - mm * 60;
            if ss < 0 || ss > 99 {
                continue;
            }
            // Build the 4‑digit representation "MMSS"
            let s = format!("{:02}{:02}", mm, ss);
            let digits: Vec<i32> = s.chars()
                                   .map(|c| c.to_digit(10).unwrap() as i32)
                                   .collect();
            // Consider all non‑empty suffixes (pressing 1 to 4 digits)
            for k in 1..=4 {
                let start_idx = 4 - k;
                let cost = calc_cost(&digits[start_idx..]);
                if cost < answer {
                    answer = cost;
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (min-cost-set-time startAt moveCost pushCost targetSeconds)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let ((best (expt 2 60))) ; large initial value
    (define (cost-for-seq seq)
      (let loop ((pos startAt) (lst seq) (acc 0))
        (if (null? lst)
            acc
            (let* ((d (car lst))
                   (move (if (= pos d) 0 moveCost))
                   (new-acc (+ acc move pushCost)))
              (loop d (cdr lst) new-acc)))))
    (for ([mm (in-range 0 100)])
      (let* ((ss (- targetSeconds (* mm 60))))
        (when (and (>= ss 0) (<= ss 99))
          (define d1 (quotient mm 10))
          (define d2 (remainder mm 10))
          (define d3 (quotient ss 10))
          (define d4 (remainder ss 10))
          (define full (list d1 d2 d3 d4))
          (for ([k (in-range 1 5)]) ; suffix length from 1 to 4
            (let* ((seq (drop full (- 4 k)))
                   (c (cost-for-seq seq)))
              (when (< c best) (set! best c)))))))
    best))
```

## Erlang

```erlang
-define(INF, 1 bsl 60).

-spec min_cost_set_time(StartAt :: integer(), MoveCost :: integer(), PushCost :: integer(), TargetSeconds :: integer()) -> integer().
min_cost_set_time(StartAt, MoveCost, PushCost, TargetSeconds) ->
    Inf = ?INF,
    lists:foldl(
        fun(Mm, Best) ->
            Ss = TargetSeconds - Mm * 60,
            if
                Ss >= 0, Ss =< 99 ->
                    Digits = [Mm div 10, Mm rem 10, Ss div 10, Ss rem 10],
                    Cost = min_cost_seq(Digits, StartAt, MoveCost, PushCost),
                    case Cost < Best of
                        true -> Cost;
                        false -> Best
                    end;
                true ->
                    Best
            end
        end,
        Inf,
        lists:seq(0, 99)
    ).

min_cost_seq(Digits, StartAt, MoveCost, PushCost) ->
    LeadZeros = count_leading_zeros(Digits),
    min_cost_seq_k(0, LeadZeros, Digits, StartAt, MoveCost, PushCost, ?INF).

min_cost_seq_k(K, MaxK, Digits, StartAt, MoveCost, PushCost, Best) when K =< MaxK ->
    Seq = lists:nthtail(K, Digits),
    Cost = compute_seq_cost(Seq, StartAt, MoveCost, PushCost),
    NewBest = if Cost < Best -> Cost; true -> Best end,
    min_cost_seq_k(K + 1, MaxK, Digits, StartAt, MoveCost, PushCost, NewBest);
min_cost_seq_k(_, _, _, _, _, _, Best) ->
    Best.

count_leading_zeros([0 | Rest]) ->
    1 + count_leading_zeros(Rest);
count_leading_zeros(_) ->
    0;
count_leading_zeros([]) ->
    0.

compute_seq_cost(Seq, StartAt, MoveCost, PushCost) ->
    compute_seq_cost(Seq, StartAt, MoveCost, PushCost, 0).

compute_seq_cost([], _Curr, _MoveCost, _PushCost, Acc) ->
    Acc;
compute_seq_cost([D | Rest], Curr, MoveCost, PushCost, Acc) ->
    if
        Curr =:= D ->
            NewAcc = Acc + PushCost,
            compute_seq_cost(Rest, Curr, MoveCost, PushCost, NewAcc);
        true ->
            NewAcc = Acc + MoveCost + PushCost,
            compute_seq_cost(Rest, D, MoveCost, PushCost, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost_set_time(start_at :: integer, move_cost :: integer, push_cost :: integer, target_seconds :: integer) :: integer
  def min_cost_set_time(start_at, move_cost, push_cost, target_seconds) do
    costs =
      Enum.flat_map(0..99, fn mm ->
        ss = target_seconds - mm * 60

        if ss >= 0 and ss <= 99 do
          digits = [
            div(mm, 10),
            rem(mm, 10),
            div(ss, 10),
            rem(ss, 10)
          ]

          leading_zeros =
            digits
            |> Enum.take_while(fn d -> d == 0 end)
            |> length()

          Enum.map(0..leading_zeros, fn i ->
            seq = Enum.slice(digits, i, 4 - i)

            compute_cost(seq, start_at, move_cost, push_cost)
          end)
        else
          []
        end
      end)

    Enum.min(costs)
  end

  defp compute_cost(seq, start_at, move_cost, push_cost) do
    {total, _} =
      Enum.reduce(seq, {0, start_at}, fn d, {cost, cur} ->
        cost = if cur != d, do: cost + move_cost, else: cost
        {cost + push_cost, d}
      end)

    total
  end
end
```
