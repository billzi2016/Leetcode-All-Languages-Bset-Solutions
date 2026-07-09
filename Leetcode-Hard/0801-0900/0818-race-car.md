# 0818. Race Car

## Cpp

```cpp
class Solution {
public:
    int racecar(int target) {
        unordered_map<int,int> memo;
        function<int(int)> dfs = [&](int t)->int{
            if (t == 0) return 0;
            if (memo.count(t)) return memo[t];
            // find smallest n such that (2^n - 1) >= t
            int n = 0;
            while ((1 << n) - 1 < t) ++n;
            int ans;
            if ((1 << n) - 1 == t) {
                ans = n; // just accelerate n times
            } else {
                // case 1: overshoot and reverse
                int pos = (1 << n) - 1;
                ans = n + 1 + dfs(pos - t);
                
                // case 2: stop before overshooting, reverse earlier
                for (int m = 0; m < n - 1; ++m) {
                    int forwardPos = (1 << (n - 1)) - 1;
                    int backPos = (1 << m) - 1;
                    // sequence: (n-1) A's, R, m A's, R, then solve remaining distance
                    ans = min(ans,
                              (n - 1) + 1 + m + 1 + dfs(t - forwardPos + backPos));
                }
            }
            memo[t] = ans;
            return ans;
        };
        return dfs(target);
    }
};
```

## Java

```java
class Solution {
    private int[] memo;

    public int racecar(int target) {
        memo = new int[10001];
        for (int i = 0; i < memo.length; i++) memo[i] = -1;
        return dfs(target);
    }

    private int dfs(int t) {
        if (t <= 0) return 0;
        if (memo[t] != -1) return memo[t];

        int n = 0;
        while ((1 << n) - 1 < t) n++;

        // Exact hit
        if ((1 << n) - 1 == t) {
            memo[t] = n;
            return n;
        }

        // Overshoot and reverse
        int ans = n + 1 + dfs((1 << n) - 1 - t);

        // Stop before target, reverse earlier
        for (int m = 0; m < n - 1; ++m) {
            int forwardDist = (1 << (n - 1)) - 1;
            int backwardDist = (1 << m) - 1;
            int cur = (n - 1) + 1 + m + 1 + dfs(t - forwardDist + backwardDist);
            ans = Math.min(ans, cur);
        }

        memo[t] = ans;
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(None)
        def dp(t):
            if t == 0:
                return 0
            n = t.bit_length()  # smallest n such that (1<<n)-1 >= t
            if (1 << n) - 1 == t:
                return n
            # overshoot case: go past target then reverse
            ans = n + 1 + dp((1 << n) - 1 - t)
            # try not overshooting: go forward n-1 steps, reverse, go back m steps, reverse again
            for m in range(n - 1):
                # steps: (n-1) A's, R, m A's, R, then solve remaining distance
                cur = (n - 1) + 1 + m + 1 + dp(t - ((1 << (n - 1)) - 1) + ((1 << m) - 1))
                if cur < ans:
                    ans = cur
            return ans

        return dp(target)
```

## Python3

```python
class Solution:
    def racecar(self, target: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(t: int) -> int:
            if t == 0:
                return 0
            # find smallest n such that (2^n - 1) >= t
            n = 0
            while (1 << n) - 1 < t:
                n += 1
            # exact hit
            if (1 << n) - 1 == t:
                return n

            # case 1: overshoot then reverse
            ans = n + 1 + dp((1 << n) - 1 - t)

            # case 2: stop before overshooting, turn back, go some distance forward again
            for m in range(n - 1):
                # after (n-1) accelerations we are at pos = 2^{n-1} - 1,
                # then reverse and move m steps backward (negative direction)
                # ending position:
                pos = (1 << (n - 1)) - 1 - ((1 << m) - 1)
                remaining = t - pos
                ans = min(ans, (n - 1) + 1 + m + 1 + dp(remaining))
            return ans

        return dp(target)
```

## C

```c
static int memo[10001];

int racecar(int target) {
    if (target == 0) return 0;
    if (memo[target]) return memo[target];
    
    int n = 0;
    while ((1 << n) - 1 < target) ++n;
    
    if ((1 << n) - 1 == target) {
        memo[target] = n;
        return n;
    }
    
    // Case 1: overshoot and reverse
    int ans = n + 1 + racecar((1 << n) - 1 - target);
    
    // Case 2: stop before target, reverse, go back some distance, then forward again
    for (int m = 0; m < n - 1; ++m) {
        int forward = (1 << (n - 1)) - 1;                 // position after n-1 accelerations
        int backDist = (1 << m) - 1;                     // distance moved backward after reverse
        int cur = (n - 1) + 1 + m + 1 + racecar(target - forward + backDist);
        if (cur < ans) ans = cur;
    }
    
    memo[target] = ans;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int Racecar(int target) {
        int[] dp = new int[target + 1];
        const int INF = int.MaxValue / 2;
        for (int i = 0; i <= target; i++) dp[i] = INF;
        dp[0] = 0;

        for (int t = 1; t <= target; ++t) {
            // find smallest n such that (2^n - 1) >= t
            int n = 0;
            while ((1 << n) - 1 < t) n++;

            if ((1 << n) - 1 == t) {
                dp[t] = n; // just accelerate n times
                continue;
            }

            // case 1: overshoot then reverse
            int overshootPos = (1 << n) - 1;
            dp[t] = n + 1 + dp[overshootPos - t];

            // case 2: stop before overshoot, reverse earlier
            for (int m = 0; m < n - 1; ++m) {
                int forwardPos = (1 << m) - 1;
                int candidate = m + 1 + 1 + dp[t - forwardPos];
                if (candidate < dp[t]) dp[t] = candidate;
            }
        }

        return dp[target];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} target
 * @return {number}
 */
var racecar = function(target) {
    const memo = new Map();
    const dfs = (t) => {
        if (memo.has(t)) return memo.get(t);
        let n = 0;
        while ((1 << n) - 1 < t) n++;
        // exact hit
        if ((1 << n) - 1 === t) {
            memo.set(t, n);
            return n;
        }
        // overshoot and reverse once
        let ans = n + 1 + dfs((1 << n) - 1 - t);
        // try reversing earlier
        for (let i = 0; i < n - 1; ++i) {
            const forwardPos = (1 << (n - 1)) - 1;
            const backwardDist = (1 << i) - 1;
            const curPos = forwardPos - backwardDist;
            const steps = (n - 1) + 1 + i + 1 + dfs(t - curPos);
            if (steps < ans) ans = steps;
        }
        memo.set(t, ans);
        return ans;
    };
    return dfs(target);
};
```

## Typescript

```typescript
function racecar(target: number): number {
    const limit = target * 2 + 2;
    const visited = new Set<string>();
    const queue: [number, number, number][] = [];
    queue.push([0, 1, 0]);
    visited.add('0,1');
    while (queue.length) {
        const [pos, speed, steps] = queue.shift()!;
        if (pos === target) return steps;
        // Accelerate
        let np = pos + speed;
        let ns = speed * 2;
        const keyA = `${np},${ns}`;
        if (!visited.has(keyA) && Math.abs(np) <= limit) {
            visited.add(keyA);
            queue.push([np, ns, steps + 1]);
        }
        // Reverse
        np = pos;
        ns = speed > 0 ? -1 : 1;
        const keyR = `${np},${ns}`;
        if (!visited.has(keyR) && Math.abs(np) <= limit) {
            visited.add(keyR);
            queue.push([np, ns, steps + 1]);
        }
    }
    return -1;
}
```

## Php

```php
class Solution {
    private $memo = [];

    /**
     * @param Integer $target
     * @return Integer
     */
    function racecar($target) {
        return $this->dp($target);
    }

    private function dp(int $t): int {
        if ($t == 0) {
            return 0;
        }
        if (isset($this->memo[$t])) {
            return $this->memo[$t];
        }

        // Find smallest n such that (2^n - 1) >= t
        $n = 0;
        while ((1 << $n) - 1 < $t) {
            $n++;
        }

        // Exact hit
        if ((1 << $n) - 1 == $t) {
            $this->memo[$t] = $n;
            return $n;
        }

        // Overshoot: go past target then reverse
        $ans = $n + 1 + $this->dp((1 << $n) - 1 - $t);

        // Undershoot: stop before target, reverse, and try again
        for ($m = 0; $m < $n - 1; $m++) {
            $pos = (1 << $m) - 1;                     // position after m accelerations
            $backSteps = $n - $m - 1;                 // accelerations after first reverse
            $remaining = $t - $pos + ((1 << $backSteps) - 1);
            $steps = $m + 1 + $backSteps + 1 + $this->dp($remaining);
            if ($steps < $ans) {
                $ans = $steps;
            }
        }

        $this->memo[$t] = $ans;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private var memo: [Int: Int] = [:]
    
    func racecar(_ target: Int) -> Int {
        return dfs(target)
    }
    
    private func dfs(_ t: Int) -> Int {
        if t == 0 { return 0 }
        if let cached = memo[t] { return cached }
        
        var n = 0
        while (1 << n) - 1 < t {
            n += 1
        }
        
        // Exact hit with only accelerations
        if (1 << n) - 1 == t {
            memo[t] = n
            return n
        }
        
        // Overshoot: go past target, then reverse
        var ans = n + 1 + dfs((1 << n) - 1 - t)
        
        // Undershoot: stop before target, reverse, and try again
        for i in 0..<n {
            let cur = (1 << i) - 1          // position after i accelerations
            // i accelerations, one reverse, another reverse later => i + 2 steps,
            // then solve the remaining distance
            ans = min(ans, i + 2 + dfs(t - cur - 1))
        }
        
        memo[t] = ans
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val memo = HashMap<Int, Int>()
    fun racecar(target: Int): Int {
        return dp(target)
    }

    private fun dp(t: Int): Int {
        if (t == 0) return 0
        memo[t]?.let { return it }
        var n = 0
        while ((1 shl n) - 1 < t) {
            n++
        }
        // Exact hit
        if ((1 shl n) - 1 == t) {
            memo[t] = n
            return n
        }
        // Overshoot and reverse
        var ans = n + 1 + dp((1 shl n) - 1 - t)
        // Try not overshooting: go forward (n-1) times, reverse, go back m times, reverse again
        for (m in 0 until n - 1) {
            val pos = (1 shl (n - 1)) - 1          // position after (n-1) accelerations
            val backDist = (1 shl m) - 1           // distance moved backward after m accelerations
            val cur = (n - 1) + 1 + m + 1 + dp(t - (pos - backDist))
            if (cur < ans) ans = cur
        }
        memo[t] = ans
        return ans
    }
}
```

## Dart

```dart
class Solution {
  final Map<int, int> _memo = {};

  int racecar(int target) => _dp(target);

  int _dp(int t) {
    if (t == 0) return 0;
    if (_memo.containsKey(t)) return _memo[t]!;

    // Find smallest n such that (2^n - 1) >= t
    int n = 0;
    while ((1 << n) - 1 < t) {
      n++;
    }

    // Exact hit
    if ((1 << n) - 1 == t) {
      _memo[t] = n;
      return n;
    }

    // Overshoot and reverse
    int ans = n + 1 + _dp((1 << n) - 1 - t);

    // Stop before overshooting, then adjust
    for (int m = 0; m < n - 1; ++m) {
      int forwardPos = (1 << (n - 1)) - 1;
      int backPos = (1 << m) - 1;
      int curPos = forwardPos - backPos;
      int remain = t - curPos;
      if (remain < 0) continue;
      ans = _min(ans, n + m + 2 + _dp(remain));
    }

    _memo[t] = ans;
    return ans;
  }

  int _min(int a, int b) => a < b ? a : b;
}
```

## Golang

```go
package main

func racecar(target int) int {
	if memo == nil {
		memo = make(map[int]int)
	}
	return solve(target)
}

var memo map[int]int

func solve(t int) int {
	if v, ok := memo[t]; ok {
		return v
	}
	if t == 0 {
		memo[0] = 0
		return 0
	}
	n := 0
	for (1<<n)-1 < t {
		n++
	}
	if (1<<n)-1 == t {
		memo[t] = n
		return n
	}
	// overshoot then reverse
	ans := n + 1 + solve((1<<n)-1-t)

	// try reversing earlier
	for m := 0; m < n; m++ {
		forward := (1 << m) - 1
		cur := m + 1 + (n-1-m) + 1 + solve(t-forward)
		if cur < ans {
			ans = cur
		}
	}
	memo[t] = ans
	return ans
}
```

## Ruby

```ruby
def racecar(target)
  @dp ||= {0 => 0}
  return @dp[target] if @dp.key?(target)

  n = 0
  while (1 << n) - 1 < target
    n += 1
  end

  if ((1 << n) - 1) == target
    @dp[target] = n
    return n
  end

  # Overshoot and then reverse
  ans = n + 1 + racecar((1 << n) - 1 - target)

  # Try reversing earlier
  (0...n - 1).each do |m|
    forward = (1 << (n - 1)) - 1
    back = (1 << m) - 1
    remaining = target - forward + back
    steps = n + m + 1 + racecar(remaining)
    ans = [ans, steps].min
  end

  @dp[target] = ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  private val memo: mutable.Map[Int, Int] = mutable.Map(0 -> 0)

  def racecar(target: Int): Int = dp(target)

  private def dp(t: Int): Int = {
    if (memo.contains(t)) return memo(t)

    var n = 0
    while ((1 << n) - 1 < t) n += 1
    val full = (1 << n) - 1

    val ans: Int =
      if (full == t) {
        n
      } else {
        // overshoot case
        var best = n + 1 + dp(full - t)

        // undershoot cases
        for (m <- 0 until n - 1) {
          val forward = (1 << (n - 1)) - 1
          val back = (1 << m) - 1
          val steps = (n - 1) + 1 + m + 1 + dp(t - forward + back)
          if (steps < best) best = steps
        }
        best
      }

    memo(t) = ans
    ans
  }
}
```

## Rust

```rust
use std::cmp::min;

fn dfs(t: usize, memo: &mut Vec<i32>) -> i32 {
    if memo[t] != -1 {
        return memo[t];
    }
    let target = t as i32;
    // smallest n with (2^n)-1 >= target
    let mut n = 0;
    while ((1 << n) - 1) < target {
        n += 1;
    }
    if ((1 << n) - 1) == target {
        memo[t] = n as i32;
        return memo[t];
    }

    // Option 1: overshoot and reverse
    let pos = (1 << n) - 1;
    let mut ans = n + 1 + dfs((pos - target) as usize, memo);

    // Option 2: stop before target, reverse, go back some steps, reverse again
    let pos_before = (1 << (n - 1)) - 1; // after n-1 accelerations
    for m in 0..(n - 1) {
        let back = (1 << m) - 1;
        let remaining = target - pos_before + back;
        if remaining < 0 {
            continue;
        }
        let steps = (n - 1) + 1 + m + 1 + dfs(remaining as usize, memo);
        ans = min(ans, steps);
    }

    memo[t] = ans as i32;
    ans as i32
}

impl Solution {
    pub fn racecar(target: i32) -> i32 {
        let t = target as usize;
        let mut memo = vec![-1i32; t + 1];
        dfs(t, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (racecar target)
  (-> exact-integer? exact-integer?)
  (let* ([memo (make-hash)])
    (hash-set! memo 0 0)
    (define (pow2 n) (arithmetic-shift 1 n))
    (letrec ([dp
              (lambda (t)
                (cond [(hash-has-key? memo t) (hash-ref memo t)]
                      [else
                       (let* ([n (let find ((k 0))
                                   (if (>= (- (pow2 k) 1) t)
                                       k
                                       (find (add1 k))))])
                         (define pos (- (pow2 n) 1))
                         (if (= pos t)
                             (begin (hash-set! memo t n) n)
                             (let* ([ans (+ n 1 (dp (- pos t)))])
                               (define best ans)
                               (for ([i (in-range 0 (sub1 n))])
                                 (let* ([posPrev (- (pow2 (sub1 n)) 1)]
                                        [backDist (- (pow2 i) 1)]
                                        [steps (+ (sub1 n) 1 i 1
                                                  (dp (+ (- t posPrev) backDist)))])
                                   (set! best (min best steps))))
                               (hash-set! memo t best)
                               best))))])])
      (dp target))))
```

## Erlang

```erlang
-spec racecar(Target :: integer()) -> integer().
racecar(Target) ->
    {Ans, _} = dp(Target, #{}),
    Ans.

%% internal DP with memoization
dp(0, Memo) ->
    {0, Memo};
dp(T, Memo) when T > 0 ->
    case maps:find(T, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            N = find_n(T),
            MaxPos = (1 bsl N) - 1,
            if MaxPos == T ->
                    Res = N,
                    NewMemo = maps:put(T, Res, Memo),
                    {Res, NewMemo};
               true ->
                    %% option 1 : overshoot then reverse
                    {StepsOver, Memo1} = dp(MaxPos - T, Memo),
                    Opt1 = N + 1 + StepsOver,

                    %% option 2 : turn back earlier
                    ForwardPos = (1 bsl (N-1)) - 1,
                    {Opt2, Memo2} = opt2_loop(0, N-2, T, N, ForwardPos, Memo1, Opt1, Memo1),

                    Res = min(Opt1, Opt2),
                    NewMemo = maps:put(T, Res, Memo2),
                    {Res, NewMemo}
            end
    end.

%% find smallest n such that (2^n - 1) >= T
find_n(T) -> find_n(0, T).
find_n(N, T) when ((1 bsl N) - 1) < T -> find_n(N + 1, T);
find_n(N, _) -> N.

%% iterate over possible early reversals
opt2_loop(_M, MaxM, _Target, _N, _ForwardPos, Memo, Best, BestMemo) when _M > MaxM ->
    {Best, BestMemo};
opt2_loop(M, MaxM, Target, N, ForwardPos, Memo, Best, BestMemo) ->
    BackPos = (1 bsl M) - 1,
    Rem = Target - ForwardPos + BackPos,
    if
        Rem < 0 ->
            opt2_loop(M + 1, MaxM, Target, N, ForwardPos, Memo, Best, BestMemo);
        true ->
            {StepsRem, MemoTmp} = dp(Rem, Memo),
            Candidate = (N - 1) + 1 + M + 1 + StepsRem,
            if
                Candidate < Best ->
                    opt2_loop(M + 1, MaxM, Target, N, ForwardPos, MemoTmp, Candidate, MemoTmp);
                true ->
                    opt2_loop(M + 1, MaxM, Target, N, ForwardPos, MemoTmp, Best, BestMemo)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec racecar(target :: integer) :: integer
  def racecar(target) do
    dp =
      Enum.reduce(1..target, %{}, fn t, acc ->
        n = min_n(t)

        if ((1 <<< n) - 1) == t do
          Map.put(acc, t, n)
        else
          overshoot = n + 1 + Map.get(acc, (1 <<< n) - 1 - t, 0)
          best = overshoot
          p = (1 <<< (n - 1)) - 1

          best =
            Enum.reduce(0..(n - 2), best, fn m, cur_best ->
              q = (1 <<< m) - 1
              steps = (n - 1) + 1 + m + 1 + Map.get(acc, t - p + q, 0)
              if steps < cur_best, do: steps, else: cur_best
            end)

          Map.put(acc, t, best)
        end
      end)

    dp[target]
  end

  defp min_n(t), do: min_n(t, 0)

  defp min_n(t, n) do
    if ((1 <<< n) - 1) >= t, do: n, else: min_n(t, n + 1)
  end
end
```
