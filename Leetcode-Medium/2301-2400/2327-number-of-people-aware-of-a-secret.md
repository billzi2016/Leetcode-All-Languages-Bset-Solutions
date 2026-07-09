# 2327. Number of People Aware of a Secret

## Cpp

```cpp
class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        const int MOD = 1'000'000'007;
        vector<long long> dp(n + 1, 0), pref(n + 1, 0);
        dp[1] = 1;
        pref[1] = 1;
        for (int i = 2; i <= n; ++i) {
            int L = i - forget + 1;
            if (L < 1) L = 1;
            int R = i - delay;
            long long val = 0;
            if (R >= 1 && L <= R) {
                val = (pref[R] - pref[L - 1]) % MOD;
                if (val < 0) val += MOD;
            }
            dp[i] = val;
            pref[i] = (pref[i - 1] + dp[i]) % MOD;
        }
        int startIdx = n - forget + 1;
        if (startIdx < 1) startIdx = 1;
        long long ans = (pref[n] - pref[startIdx - 1]) % MOD;
        if (ans < 0) ans += MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        final int MOD = 1_000_000_007;
        long[] dp = new long[n + 1];
        dp[1] = 1;
        long active = 0;
        for (int day = 2; day <= n; day++) {
            if (day - delay >= 1) {
                active = (active + dp[day - delay]) % MOD;
            }
            if (day - forget >= 1) {
                active = (active - dp[day - forget] + MOD) % MOD;
            }
            dp[day] = active;
        }
        long ans = 0;
        int start = n - forget + 1;
        if (start < 1) start = 1;
        for (int i = start; i <= n; i++) {
            ans += dp[i];
            if (ans >= MOD) ans -= MOD;
        }
        return (int) (ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # new[i]: number of people who learn the secret on day i (1-indexed)
        new = [0] * (n + 2)
        new[1] = 1

        share_sum = 0          # sum of people eligible to share today
        total = 1              # total people aware at current day

        for day in range(2, n + 1):
            # people become eligible to share after 'delay' days
            if day - delay >= 1:
                share_sum = (share_sum + new[day - delay]) % MOD
            # people stop sharing (and forget) after 'forget' days
            if day - forget >= 1:
                share_sum = (share_sum - new[day - forget]) % MOD

            new[day] = share_sum
            total = (total + new[day]) % MOD

            # remove those who forget today from the total count
            if day - forget >= 1:
                total = (total - new[day - forget]) % MOD

        return total % MOD
```

## Python3

```python
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        new = [0] * (n + 2)      # new[i]: people who learn the secret on day i
        pref = [0] * (n + 2)     # prefix sums of new
        
        new[1] = 1
        pref[1] = 1
        
        for day in range(2, n + 1):
            start = max(1, day - forget + 1)
            end = day - delay
            if end >= start:
                sharers = (pref[end] - pref[start - 1]) % MOD
            else:
                sharers = 0
            new[day] = sharers
            pref[day] = (pref[day - 1] + new[day]) % MOD
        
        ans_start = max(1, n - forget + 1)
        answer = (pref[n] - pref[ans_start - 1]) % MOD
        return answer
```

## C

```c
#include <stdlib.h>

int peopleAwareOfSecret(int n, int delay, int forget) {
    const int MOD = 1000000007;
    long long *newP = (long long *)calloc(n + 2, sizeof(long long));
    if (!newP) return 0;
    newP[1] = 1;                     // day 1 discovery
    long long shareSum = 0;          // people who can share today

    for (int i = 2; i <= n; ++i) {
        int addIdx = i - delay;
        if (addIdx >= 1) {
            shareSum += newP[addIdx];
            if (shareSum >= MOD) shareSum -= MOD;
        }
        int subIdx = i - forget;
        if (subIdx >= 1) {
            shareSum -= newP[subIdx];
            if (shareSum < 0) shareSum += MOD;
        }
        newP[i] = shareSum;
    }

    long long ans = 0;
    int start = n - forget + 1;
    if (start < 1) start = 1;
    for (int i = start; i <= n; ++i) {
        ans += newP[i];
        if (ans >= MOD) ans -= MOD;
    }

    free(newP);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int PeopleAwareOfSecret(int n, int delay, int forget) {
        const int MOD = 1000000007;
        long[] dp = new long[n + 1];
        // arrays sized enough to avoid index out of range for future events
        long[] inc = new long[n + forget + 2];
        long[] dec = new long[n + forget + 2];

        dp[1] = 1;
        if (1 + delay <= n) inc[1 + delay] = (inc[1 + delay] + 1) % MOD;
        if (1 + forget <= n) dec[1 + forget] = (dec[1 + forget] + 1) % MOD;

        long shareable = 0;
        for (int day = 2; day <= n; day++) {
            shareable = (shareable + inc[day]) % MOD;
            shareable = (shareable - dec[day] + MOD) % MOD;
            dp[day] = shareable;

            if (day + delay <= n) {
                inc[day + delay] = (inc[day + delay] + dp[day]) % MOD;
            }
            if (day + forget <= n) {
                dec[day + forget] = (dec[day + forget] + dp[day]) % MOD;
            }
        }

        long ans = 0;
        for (int i = 1; i <= n; i++) {
            if (i + forget > n) {
                ans = (ans + dp[i]) % MOD;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
var peopleAwareOfSecret = function(n, delay, forget) {
    const MOD = 1000000007;
    const dp = new Array(n + 1).fill(0);
    dp[1] = 1;
    let share = 0;
    for (let i = 2; i <= n; ++i) {
        if (i - delay >= 1) {
            share += dp[i - delay];
            if (share >= MOD) share -= MOD;
        }
        if (i - forget >= 1) {
            share -= dp[i - forget];
            if (share < 0) share += MOD;
        }
        dp[i] = share;
    }
    let ans = 0;
    const start = Math.max(1, n - forget + 1);
    for (let i = start; i <= n; ++i) {
        ans += dp[i];
        if (ans >= MOD) ans -= MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    const MOD = 1_000_000_007;
    const dp: number[] = new Array(n + 2).fill(0);
    dp[1] = 1;
    let shareSum = 0;

    for (let day = 2; day <= n; day++) {
        if (day - delay >= 1) {
            shareSum = (shareSum + dp[day - delay]) % MOD;
        }
        if (day - forget >= 1) {
            shareSum = (shareSum - dp[day - forget] + MOD) % MOD;
        }
        dp[day] = shareSum;
    }

    let ans = 0;
    const start = Math.max(1, n - forget + 1);
    for (let i = start; i <= n; i++) {
        ans = (ans + dp[i]) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $delay
     * @param Integer $forget
     * @return Integer
     */
    function peopleAwareOfSecret($n, $delay, $forget) {
        $MOD = 1000000007;
        $new = array_fill(0, $n + 2, 0);
        $new[1] = 1;
        $sum = 0;
        for ($i = 2; $i <= $n; $i++) {
            if ($i - $delay >= 1) {
                $sum = ($sum + $new[$i - $delay]) % $MOD;
            }
            if ($i - $forget >= 1) {
                $sum = ($sum - $new[$i - $forget] + $MOD) % $MOD;
            }
            $new[$i] = $sum;
        }
        $ans = 0;
        $start = max(1, $n - $forget + 1);
        for ($i = $start; $i <= $n; $i++) {
            $ans = ($ans + $new[$i]) % $MOD;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func peopleAwareOfSecret(_ n: Int, _ delay: Int, _ forget: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: 0, count: n + 2)
        dp[1] = 1
        var active = 0
        
        if n >= 2 {
            for day in 2...n {
                let addIdx = day - delay
                if addIdx >= 1 {
                    active += dp[addIdx]
                    if active >= MOD { active -= MOD }
                }
                let subIdx = day - forget
                if subIdx >= 1 {
                    active -= dp[subIdx]
                    if active < 0 { active += MOD }
                }
                dp[day] = active
            }
        }
        
        var result = 0
        for i in 1...n where i + forget > n {
            result += dp[i]
            if result >= MOD { result -= MOD }
        }
        return result % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int {
        val MOD = 1_000_000_007L
        val newArr = LongArray(n + 2)
        val prefix = LongArray(n + 2)

        newArr[1] = 1L
        prefix[1] = 1L

        for (i in 2..n) {
            val r = i - delay
            if (r >= 1) {
                var l = i - forget + 1
                if (l < 1) l = 1
                var sum = (prefix[r] - prefix[l - 1]) % MOD
                if (sum < 0) sum += MOD
                newArr[i] = sum
            } else {
                newArr[i] = 0L
            }
            prefix[i] = (prefix[i - 1] + newArr[i]) % MOD
        }

        var ans = 0L
        val start = n - forget + 1
        for (i in maxOf(1, start)..n) {
            ans += newArr[i]
        }
        ans %= MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int peopleAwareOfSecret(int n, int delay, int forget) {
    List<int> dp = List.filled(n + 1, 0);
    dp[1] = 1;
    int shareable = 0; // number of people who can share today

    for (int day = 2; day <= n; ++day) {
      if (day - delay >= 1) {
        shareable = (shareable + dp[day - delay]) % _mod;
      }
      if (day - forget >= 1) {
        shareable = (shareable - dp[day - forget]) % _mod;
        if (shareable < 0) shareable += _mod;
      }
      dp[day] = shareable;
    }

    int ans = 0;
    for (int i = n - forget + 1; i <= n; ++i) {
      if (i >= 1) {
        ans = (ans + dp[i]) % _mod;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func peopleAwareOfSecret(n int, delay int, forget int) int {
	const MOD = 1000000007
	dp := make([]int, n+1)
	dp[1] = 1
	share := 0
	for i := 2; i <= n; i++ {
		if i-delay >= 1 {
			share += dp[i-delay]
			if share >= MOD {
				share -= MOD
			}
		}
		if i-forget >= 1 {
			share -= dp[i-forget]
			if share < 0 {
				share += MOD
			}
		}
		dp[i] = share
	}
	ans := 0
	start := n - forget + 1
	if start < 1 {
		start = 1
	}
	for i := start; i <= n; i++ {
		ans += dp[i]
		if ans >= MOD {
			ans -= MOD
		}
	}
	return ans
}
```

## Ruby

```ruby
def people_aware_of_secret(n, delay, forget)
  mod = 1_000_000_007
  return 1 if n == 1
  dp = Array.new(n + 1, 0)
  dp[1] = 1
  share_sum = 0
  total = 1
  (2..n).each do |day|
    if day - delay >= 1
      share_sum += dp[day - delay]
      share_sum %= mod
    end
    if day - forget >= 1
      share_sum -= dp[day - forget]
      share_sum %= mod
      total -= dp[day - forget]
      total %= mod
    end
    dp[day] = share_sum % mod
    total += dp[day]
    total %= mod
  end
  total % mod
end
```

## Scala

```scala
object Solution {
    def peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int = {
        val MOD = 1000000007L
        val learn = new Array[Long](n + 2)
        learn(1) = 1L
        var share: Long = 0L

        for (day <- 2 to n) {
            if (day - delay >= 1) {
                share = (share + learn(day - delay)) % MOD
            }
            if (day - forget >= 1) {
                share = (share - learn(day - forget) + MOD) % MOD
            }
            learn(day) = share
        }

        var ans: Long = 0L
        val start = math.max(1, n - forget + 1)
        for (i <- start to n) {
            ans = (ans + learn(i)) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        let n = n as usize;
        let delay = delay as usize;
        let forget = forget as usize;
        const MOD: i64 = 1_000_000_007;

        // dp[i] = number of people who learned the secret on day i
        let mut dp = vec![0i64; n + 2];
        dp[1] = 1;

        let mut share_sum: i64 = 0; // sum of active sharers for current day
        let mut total: i64 = 1;     // people who currently know the secret

        for day in 2..=n {
            // People become eligible to share after 'delay' days
            if day >= delay + 1 {
                share_sum += dp[day - delay];
                if share_sum >= MOD { share_sum -= MOD; }
            }
            // People forget after 'forget' days and stop sharing
            if day >= forget + 1 {
                let val = dp[day - forget];
                share_sum -= val;
                if share_sum < 0 { share_sum += MOD; }

                total -= val;
                if total < 0 { total += MOD; }
            }

            // New people learned the secret today
            let new_people = share_sum % MOD;
            dp[day] = new_people;

            total += new_people;
            if total >= MOD { total -= MOD; }
        }

        (total % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (people-aware-of-secret n delay forget)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([new-vec (make-vector (+ n 2) 0)])
    (vector-set! new-vec 1 1) ; day 1
    (let ([active 0])
      (for ([i (in-range 2 (+ n 1))])
        ;; add people who become able to share today
        (when (>= (- i delay) 1)
          (set! active (modulo (+ active (vector-ref new-vec (- i delay))) MOD)))
        ;; remove people who forget today
        (when (>= (- i forget) 1)
          (set! active (modulo (- active (vector-ref new-vec (- i forget))) MOD)))
        (vector-set! new-vec i active))
      ;; sum of people still knowing the secret at day n
      (let* ([start (max 1 (+ (- n forget) 1))])
        (for/fold ([sum 0]) ([j (in-range start (+ n 1))])
          (modulo (+ sum (vector-ref new-vec j)) MOD))))))
```

## Erlang

```erlang
-spec people_aware_of_secret(N :: integer(), Delay :: integer(), Forget :: integer()) -> integer().
people_aware_of_secret(N, Delay, Forget) ->
    Mod = 1000000007,
    DP0 = maps:put(1, 1, #{}),
    {DPMap,_} = lists:foldl(
        fun(I, {DPAcc, ShareAcc}) ->
            RightIdx = I - Delay,
            Share1 = if
                RightIdx >= 1 -> (ShareAcc + maps:get(RightIdx, DPAcc)) rem Mod;
                true -> ShareAcc
            end,
            LeftIdx = I - Forget,
            Share2 = if
                LeftIdx >= 1 ->
                    (Share1 - maps:get(LeftIdx, DPAcc) + Mod) rem Mod;
                true -> Share1
            end,
            NewVal = Share2,
            {maps:put(I, NewVal, DPAcc), Share2}
        end,
        {DP0, 0},
        lists:seq(2, N)
    ),
    Start = erlang:max(1, N - Forget + 1),
    Answer = lists:foldl(
        fun(J, Acc) ->
            (Acc + maps:get(J, DPMap)) rem Mod
        end,
        0,
        lists:seq(Start, N)
    ),
    Answer.
```

## Elixir

```elixir
defmodule Solution do
  @spec people_aware_of_secret(n :: integer, delay :: integer, forget :: integer) :: integer
  def people_aware_of_secret(n, delay, forget) do
    mod = 1_000_000_007

    # pref[0] = 0, pref[1] = 1 (day 1)
    pref = [0, 1]

    {pref_final, _} =
      Enum.reduce(2..n, {pref, 1}, fn i, {pref_acc, _prev_dp} ->
        l = i - forget + 1
        r = i - delay

        new =
          if r >= 1 and l <= r do
            l_adj = max(l, 1)
            sum_r = Enum.at(pref_acc, r)
            sum_l_1 = Enum.at(pref_acc, l_adj - 1)

            diff = sum_r - sum_l_1
            if diff < 0, do: diff + mod, else: diff
          else
            0
          end

        pref_i = (Enum.at(pref_acc, i - 1) + new) |> rem(mod)
        {pref_acc ++ [pref_i], new}
      end)

    start_idx = max(0, n - forget)
    total = Enum.at(pref_final, n) - Enum.at(pref_final, start_idx)
    if total < 0, do: total + mod, else: total
  end
end
```
