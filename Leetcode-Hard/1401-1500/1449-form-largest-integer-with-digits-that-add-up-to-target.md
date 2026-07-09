# 1449. Form Largest Integer With Digits That Add up to Target

## Cpp

```cpp
class Solution {
public:
    string largestNumber(vector<int>& cost, int target) {
        const int INF_NEG = -1000000;
        vector<int> dp(target + 1, INF_NEG);
        dp[0] = 0;
        for (int t = 1; t <= target; ++t) {
            for (int d = 1; d <= 9; ++d) {
                int c = cost[d - 1];
                if (t >= c && dp[t - c] != INF_NEG) {
                    dp[t] = max(dp[t], dp[t - c] + 1);
                }
            }
        }
        if (dp[target] <= 0) return "0";
        string ans;
        int t = target;
        while (t > 0) {
            for (int d = 9; d >= 1; --d) {
                int c = cost[d - 1];
                if (t >= c && dp[t] == dp[t - c] + 1) {
                    ans.push_back('0' + d);
                    t -= c;
                    break;
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
    public String largestNumber(int[] cost, int target) {
        int n = target;
        int INF_NEG = -10000; // sufficiently small
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = INF_NEG;
        dp[0] = 0;

        // DP: maximum number of digits achievable with total cost i
        for (int i = 1; i <= n; i++) {
            for (int d = 1; d <= 9; d++) {
                int c = cost[d - 1];
                if (i >= c && dp[i - c] != INF_NEG) {
                    dp[i] = Math.max(dp[i], dp[i - c] + 1);
                }
            }
        }

        if (dp[n] < 0) return "0";

        StringBuilder sb = new StringBuilder();
        int remaining = n;
        for (int pos = 0; pos < dp[n]; pos++) {
            // try larger digits first
            for (int d = 9; d >= 1; d--) {
                int c = cost[d - 1];
                if (remaining >= c && dp[remaining - c] == dp[remaining] - 1) {
                    sb.append(d);
                    remaining -= c;
                    break;
                }
            }
        }

        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        # dp[i] = max number of digits we can form with total cost i; -inf if impossible
        INF_NEG = -10**9
        dp = [INF_NEG] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            best = INF_NEG
            for d in range(9):
                c = cost[d]
                if t >= c and dp[t - c] != INF_NEG:
                    cand = dp[t - c] + 1
                    if cand > best:
                        best = cand
            dp[t] = best

        if dp[target] <= 0:
            return "0"

        res = []
        cur = target
        # Build the number from most significant digit to least, trying larger digits first
        while cur > 0:
            for d in range(8, -1, -1):  # digit index 8 -> digit 9 down to 0 -> digit 1
                c = cost[d]
                if cur >= c and dp[cur] == dp[cur - c] + 1:
                    res.append(str(d + 1))
                    cur -= c
                    break
        return "".join(res)
```

## Python3

```python
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[i] = max number of digits we can achieve with total cost i
        INF_NEG = -10**9
        dp = [INF_NEG] * (target + 1)
        dp[0] = 0
        for c in cost:
            for t in range(c, target + 1):
                if dp[t - c] != INF_NEG:
                    dp[t] = max(dp[t], dp[t - c] + 1)

        if dp[target] <= 0:
            return "0"

        res = []
        # Build the largest number by trying digits from 9 to 1
        for d in range(9, 0, -1):
            c = cost[d - 1]
            while target >= c and dp[target] == dp[target - c] + 1:
                res.append(str(d))
                target -= c

        return "".join(res)
```

## C

```c
#include <stdlib.h>

char* largestNumber(int* cost, int costSize, int target) {
    const int NEG_INF = -1000000;
    int *dp = (int*)malloc((target + 1) * sizeof(int));
    for (int i = 0; i <= target; ++i) dp[i] = NEG_INF;
    dp[0] = 0;

    for (int i = 1; i <= target; ++i) {
        for (int d = 1; d <= 9; ++d) {
            int c = cost[d - 1];
            if (i >= c && dp[i - c] != NEG_INF) {
                if (dp[i] < dp[i - c] + 1)
                    dp[i] = dp[i - c] + 1;
            }
        }
    }

    if (dp[target] <= 0) {
        free(dp);
        char *zero = (char*)malloc(2);
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }

    int len = dp[target];
    char *ans = (char*)malloc(len + 1);
    int pos = 0;
    int rem = target;

    while (rem > 0) {
        for (int d = 9; d >= 1; --d) {
            int c = cost[d - 1];
            if (rem >= c && dp[rem] == dp[rem - c] + 1) {
                ans[pos++] = '0' + d;
                rem -= c;
                break;
            }
        }
    }
    ans[pos] = '\0';
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public string LargestNumber(int[] cost, int target)
    {
        const int INF_NEG = -100000;
        int[] dp = new int[target + 1];
        for (int i = 1; i <= target; i++) dp[i] = INF_NEG;
        dp[0] = 0;

        // Compute maximum number of digits achievable for each total cost
        for (int t = 1; t <= target; t++)
        {
            for (int d = 1; d <= 9; d++)
            {
                int c = cost[d - 1];
                if (t >= c && dp[t - c] != INF_NEG)
                {
                    dp[t] = Math.Max(dp[t], dp[t - c] + 1);
                }
            }
        }

        if (dp[target] < 0) return "0";

        var sb = new System.Text.StringBuilder();
        int remaining = target;
        while (remaining > 0)
        {
            for (int d = 9; d >= 1; d--)
            {
                int c = cost[d - 1];
                if (remaining >= c && dp[remaining] == dp[remaining - c] + 1)
                {
                    sb.Append((char)('0' + d));
                    remaining -= c;
                    break;
                }
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cost
 * @param {number} target
 * @return {string}
 */
var largestNumber = function(cost, target) {
    const dp = new Array(target + 1).fill(-Infinity);
    dp[0] = 0;
    for (let i = 1; i <= target; i++) {
        for (let d = 0; d < 9; d++) {
            const c = cost[d];
            if (i >= c && dp[i - c] !== -Infinity) {
                dp[i] = Math.max(dp[i], dp[i - c] + 1);
            }
        }
    }
    if (dp[target] <= 0) return "0";
    let res = "";
    let t = target;
    for (let d = 8; d >= 0;) {
        const c = cost[d];
        if (t >= c && dp[t] === dp[t - c] + 1) {
            res += (d + 1).toString();
            t -= c;
        } else {
            d--;
        }
    }
    return res;
};
```

## Typescript

```typescript
function largestNumber(cost: number[], target: number): string {
    const n = target;
    const dp = new Array(n + 1).fill(Number.NEGATIVE_INFINITY);
    dp[0] = 0;

    for (let t = 1; t <= n; ++t) {
        for (let d = 0; d < 9; ++d) {
            const c = cost[d];
            if (t >= c && dp[t - c] !== Number.NEGATIVE_INFINITY) {
                dp[t] = Math.max(dp[t], dp[t - c] + 1);
            }
        }
    }

    if (dp[n] < 0) return "0";

    let res = "";
    let t = n;
    for (let d = 8; d >= 0; --d) { // digits 9 to 1
        const c = cost[d];
        while (t >= c && dp[t] === dp[t - c] + 1) {
            res += (d + 1).toString();
            t -= c;
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @param Integer $target
     * @return String
     */
    function largestNumber($cost, $target) {
        $dp = array_fill(0, $target + 1, -1);
        $dp[0] = 0;
        for ($t = 1; $t <= $target; $t++) {
            for ($i = 0; $i < 9; $i++) {
                $c = $cost[$i];
                if ($t >= $c && $dp[$t - $c] != -1) {
                    $dp[$t] = max($dp[$t], $dp[$t - $c] + 1);
                }
            }
        }
        if ($dp[$target] == -1) {
            return "0";
        }
        $res = "";
        $remaining = $target;
        while ($remaining > 0) {
            for ($d = 9; $d >= 1; $d--) {
                $c = $cost[$d - 1];
                if ($remaining >= $c && $dp[$remaining - $c] == $dp[$remaining] - 1) {
                    $res .= (string)$d;
                    $remaining -= $c;
                    break;
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func largestNumber(_ cost: [Int], _ target: Int) -> String {
        var dp = Array(repeating: -1, count: target + 1)
        dp[0] = 0
        if target > 0 {
            for t in 1...target {
                for i in 0..<9 {
                    let c = cost[i]
                    if t >= c && dp[t - c] != -1 {
                        dp[t] = max(dp[t], dp[t - c] + 1)
                    }
                }
            }
        }
        if dp[target] <= 0 {
            return "0"
        }
        var result = ""
        var remaining = target
        for digit in stride(from: 9, through: 1, by: -1) {
            let c = cost[digit - 1]
            while remaining >= c && dp[remaining] == dp[remaining - c] + 1 {
                result += String(digit)
                remaining -= c
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestNumber(cost: IntArray, target: Int): String {
        val dp = IntArray(target + 1) { -1 }
        dp[0] = 0
        for (t in 1..target) {
            var best = -1
            for (i in 0 until 9) {
                val c = cost[i]
                if (c <= t && dp[t - c] != -1) {
                    best = maxOf(best, dp[t - c] + 1)
                }
            }
            dp[t] = best
        }
        if (dp[target] <= 0) return "0"
        val sb = StringBuilder()
        var remaining = target
        for (d in 9 downTo 1) {
            val c = cost[d - 1]
            while (remaining >= c && dp[remaining] == dp[remaining - c] + 1) {
                sb.append(d)
                remaining -= c
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String largestNumber(List<int> cost, int target) {
    List<int> dp = List.filled(target + 1, -1);
    dp[0] = 0;
    for (int i = 1; i <= target; ++i) {
      for (int d = 1; d <= 9; ++d) {
        int c = cost[d - 1];
        if (i >= c && dp[i - c] != -1) {
          int cand = dp[i - c] + 1;
          if (cand > dp[i]) dp[i] = cand;
        }
      }
    }
    if (dp[target] <= 0) return "0";
    StringBuffer sb = StringBuffer();
    int curTarget = target;
    int remaining = dp[target];
    for (int pos = 0; pos < remaining; ++pos) {
      for (int d = 9; d >= 1; --d) {
        int c = cost[d - 1];
        if (curTarget >= c && dp[curTarget - c] == remaining - pos - 1) {
          sb.write(d);
          curTarget -= c;
          break;
        }
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
import "strings"

func largestNumber(cost []int, target int) string {
    dp := make([]int, target+1)
    for i := 1; i <= target; i++ {
        dp[i] = -1
    }
    dp[0] = 0

    for t := 1; t <= target; t++ {
        for d := 1; d <= 9; d++ {
            c := cost[d-1]
            if t >= c && dp[t-c] != -1 {
                if dp[t] < dp[t-c]+1 {
                    dp[t] = dp[t-c] + 1
                }
            }
        }
    }

    if dp[target] == -1 {
        return "0"
    }

    var sb strings.Builder
    rem := target
    for d := 9; d >= 1; d-- {
        c := cost[d-1]
        for rem >= c && dp[rem] == dp[rem-c]+1 {
            sb.WriteByte(byte('0' + d))
            rem -= c
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def largest_number(cost, target)
  dp = Array.new(target + 1, -1)
  dp[0] = 0
  (1..target).each do |t|
    9.times do |i|
      c = cost[i]
      if t >= c && dp[t - c] != -1
        dp[t] = [dp[t], dp[t - c] + 1].max
      end
    end
  end
  return "0" if dp[target] == -1

  result = ""
  cur = target
  while cur > 0
    9.downto(1) do |d|
      c = cost[d - 1]
      if cur >= c && dp[cur] == dp[cur - c] + 1
        result << d.to_s
        cur -= c
        break
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def largestNumber(cost: Array[Int], target: Int): String = {
    val INF = -1000000
    val dp = Array.fill(target + 1)(INF)
    dp(0) = 0
    for (i <- 1 to target) {
      var best = INF
      for (d <- 0 until 9) {
        val c = cost(d)
        if (i >= c && dp(i - c) != INF) {
          best = math.max(best, dp(i - c) + 1)
        }
      }
      dp(i) = best
    }
    if (dp(target) < 0) return "0"
    val sb = new StringBuilder
    var rem = target
    while (rem > 0) {
      var placed = false
      for (d <- 8 to 0 by -1 if !placed) {
        val c = cost(d)
        if (rem >= c && dp(rem - c) == dp(rem) - 1) {
          sb.append((d + 1).toString)
          rem -= c
          placed = true
        }
      }
    }
    sb.toString()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_number(cost: Vec<i32>, target: i32) -> String {
        let t = target as usize;
        let mut dp = vec![-1i32; t + 1];
        dp[0] = 0;
        for i in 1..=t {
            for d in 0..9 {
                let c = cost[d] as usize;
                if i >= c && dp[i - c] != -1 {
                    dp[i] = dp[i].max(dp[i - c] + 1);
                }
            }
        }
        if dp[t] <= 0 {
            return "0".to_string();
        }
        let mut res = String::new();
        let mut cur = t;
        for d in (0..9).rev() {
            let c = cost[d] as usize;
            while cur >= c && dp[cur] == dp[cur - c] + 1 {
                res.push((b'1' + d as u8) as char);
                cur -= c;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (largest-number cost target)
  (-> (listof exact-integer?) exact-integer? string?)
  (let* ((cost-vec (list->vector cost))
         (n (+ target 1))
         (INF -1000000)
         (dp (make-vector n INF)))
    (vector-set! dp 0 0)
    ;; DP: maximum number of digits for each total cost
    (for ([t (in-range 1 n)])
      (for ([d (in-range 9)])
        (let* ((c (vector-ref cost-vec d))
               (prev (- t c)))
          (when (and (>= prev 0)
                     (> (+ (vector-ref dp prev) 1) (vector-ref dp t)))
            (vector-set! dp t (+ (vector-ref dp prev) 1))))))
    (if (<= (vector-ref dp target) 0)
        "0"
        ;; Reconstruct the largest number
        (let loop ((rem target) (ans ""))
          (if (= rem 0)
              ans
              (let find-digit ((d 9))
                (cond [(< d 1) ans] ; should not happen
                      [else
                       (define idx (- d 1))
                       (define c (vector-ref cost-vec idx))
                       (if (and (<= c rem)
                                (= (vector-ref dp (- rem c))
                                   (- (vector-ref dp rem) 1)))
                           (loop (- rem c) (string-append ans (number->string d)))
                           (find-digit (- d 1)))])))))))
```

## Erlang

```erlang
-spec largest_number(Cost :: [integer()], Target :: integer()) -> unicode:unicode_binary().
largest_number(Cost, Target) ->
    DP0 = array:new(Target + 1, {default, -1}),
    DP1 = array:set(0, 0, DP0),
    DP = dp_loop(Target, Cost, 1, DP1),
    MaxDigits = array:get(Target, DP),
    case MaxDigits of
        -1 -> <<"0">>;
        _ ->
            DigitsList = build_number(Target, Cost, DP),
            list_to_binary(DigitsList)
    end.

dp_loop(Target, Cost, T, DP) when T > Target ->
    DP;
dp_loop(Target, Cost, T, DP) ->
    Max = compute_max(T, Cost, DP),
    NewDP = array:set(T, Max, DP),
    dp_loop(Target, Cost, T + 1, NewDP).

compute_max(T, Cost, DP) ->
    lists:foldl(
        fun(Digit, Acc) ->
            C = lists:nth(Digit, Cost),
            if
                T >= C ->
                    Prev = array:get(T - C, DP),
                    case Prev of
                        -1 -> Acc;
                        _ ->
                            Cand = Prev + 1,
                            if Cand > Acc -> Cand; true -> Acc end
                    end;
                true -> Acc
            end
        end,
        -1,
        lists:seq(1, 9)
    ).

build_number(Target, Cost, DP) ->
    build_number(Target, Cost, DP, []).

build_number(0, _Cost, _DP, Acc) ->
    lists:reverse(Acc);
build_number(Rem, Cost, DP, Acc) ->
    MaxDigits = array:get(Rem, DP),
    Digit = find_digit(Rem, Cost, DP, MaxDigits, 9),
    C = lists:nth(Digit, Cost),
    Char = Digit + $0,
    build_number(Rem - C, Cost, DP, [Char | Acc]).

find_digit(_Rem, _Cost, _DP, _MaxDigits, 0) ->
    0;
find_digit(Rem, Cost, DP, MaxDigits, D) when D >= 1 ->
    C = lists:nth(D, Cost),
    if
        Rem >= C,
        array:get(Rem - C, DP) == MaxDigits - 1 ->
            D;
        true ->
            find_digit(Rem, Cost, DP, MaxDigits, D - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_number(cost :: [integer], target :: integer) :: String.t
  def largest_number(cost, target) do
    inf = -1_000_000
    dp0 = :array.new(target + 1, default: inf)
    dp = :array.set(0, 0, dp0)

    dp =
      Enum.reduce(1..target, dp, fn i, acc ->
        max_val =
          Enum.reduce(0..8, inf, fn idx, cur_max ->
            c = Enum.at(cost, idx)

            if i >= c do
              prev = :array.get(i - c, acc)

              if prev != inf do
                cand = prev + 1
                if cand > cur_max, do: cand, else: cur_max
              else
                cur_max
              end
            else
              cur_max
            end
          end)

        :array.set(i, max_val, acc)
      end)

    final_len = :array.get(target, dp)

    if final_len <= 0 do
      "0"
    else
      {_, result} =
        Enum.reduce(1..final_len, {target, ""}, fn _, {rem_target, str} ->
          cur_len = :array.get(rem_target, dp)

          chosen_digit =
            Enum.find_value(9..1, fn d ->
              c = Enum.at(cost, d - 1)

              if rem_target >= c and :array.get(rem_target - c, dp) == cur_len - 1 do
                d
              else
                nil
              end
            end)

          new_rem = rem_target - Enum.at(cost, chosen_digit - 1)
          {new_rem, str <> Integer.to_string(chosen_digit)}
        end)

      result
    end
  end
end
```
