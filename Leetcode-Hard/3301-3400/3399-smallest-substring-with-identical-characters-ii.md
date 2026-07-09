# 3399. Smallest Substring With Identical Characters II

## Cpp

```cpp
class Solution {
public:
    bool feasible(const string& s, int numOps, int L) {
        int n = s.size();
        const int INF = n + 5;
        vector<int> pref0(n + 1, 0), pref1(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            pref0[i] = pref0[i - 1] + (s[i - 1] == '0');
            pref1[i] = i - pref0[i];
        }
        vector<int> dp0(n + 1, INF), dp1(n + 1, INF);
        dp0[0] = dp1[0] = 0;
        deque<pair<int,int>> dq0, dq1; // (index, value)
        dq0.emplace_back(0, dp1[0] - 0 + pref0[0]); // for building blocks of '0'
        dq1.emplace_back(0, dp0[0] - 0 + pref1[0]); // for building blocks of '1'

        for (int i = 1; i <= n; ++i) {
            while (!dq0.empty() && dq0.front().first < i - L) dq0.pop_front();
            while (!dq1.empty() && dq1.front().first < i - L) dq1.pop_front();

            int const0 = i - pref0[i]; // ones in prefix [1..i]
            int const1 = i - pref1[i]; // zeros in prefix [1..i]

            int best0 = INF, best1 = INF;
            if (!dq0.empty()) best0 = const0 + dq0.front().second;
            if (!dq1.empty()) best1 = const1 + dq1.front().second;

            dp0[i] = best0;
            dp1[i] = best1;

            int val0 = dp1[i] - i + pref0[i];
            while (!dq0.empty() && dq0.back().second >= val0) dq0.pop_back();
            dq0.emplace_back(i, val0);

            int val1 = dp0[i] - i + pref1[i];
            while (!dq1.empty() && dq1.back().second >= val1) dq1.pop_back();
            dq1.emplace_back(i, val1);
        }
        return std::min(dp0[n], dp1[n]) <= numOps;
    }

    int minLength(string s, int numOps) {
        int n = s.size();
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(s, numOps, mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int low = 1, high = n;
        while (low < high) {
            int mid = (low + high) >>> 1; // candidate max length
            long opsNeeded = 0;
            int count = 1;
            for (int i = 1; i < n; i++) {
                if (s.charAt(i) == s.charAt(i - 1)) {
                    count++;
                } else {
                    opsNeeded += count / (mid + 1);
                    if (opsNeeded > numOps) break;
                    count = 1;
                }
            }
            opsNeeded += count / (mid + 1);
            if (opsNeeded <= numOps) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
}
```

## Python

```python
class Solution(object):
    def minLength(self, s, numOps):
        """
        :type s: str
        :type numOps: int
        :rtype: int
        """
        n = len(s)

        # prefix sums of ones and zeros
        prefOnes = [0] * (n + 1)
        prefZeros = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            prefOnes[i] = prefOnes[i - 1] + (ch == '1')
            prefZeros[i] = prefZeros[i - 1] + (ch == '0')

        from collections import deque

        def feasible(L):
            dq0 = deque()   # stores (index k, dp[k][1] - prefOnes[k])
            dq1 = deque()   # stores (index k, dp[k][0] - prefZeros[k])

            # base case: k = 0, dp[0][0] = dp[0][1] = 0
            dq0.append((0, 0 - prefOnes[0]))
            dq1.append((0, 0 - prefZeros[0]))

            dp0_i = dp1_i = 0

            for i in range(1, n + 1):
                # keep only candidates with k >= i-L
                while dq0 and dq0[0][0] < i - L:
                    dq0.popleft()
                while dq1 and dq1[0][0] < i - L:
                    dq1.popleft()

                min_val0 = dq0[0][1]
                dp0_i = prefOnes[i] + min_val0

                min_val1 = dq1[0][1]
                dp1_i = prefZeros[i] + min_val1

                # add candidate for future positions (k = i)
                val_for_dq0 = dp1_i - prefOnes[i]
                while dq0 and dq0[-1][1] >= val_for_dq0:
                    dq0.pop()
                dq0.append((i, val_for_dq0))

                val_for_dq1 = dp0_i - prefZeros[i]
                while dq1 and dq1[-1][1] >= val_for_dq1:
                    dq1.pop()
                dq1.append((i, val_for_dq1))

            return min(dp0_i, dp1_i) <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append(j - i)
            i = j

        low, high = 1, n
        while low < high:
            mid = (low + high) // 2
            ops_needed = 0
            limit = mid + 1
            for length in runs:
                ops_needed += length // limit
                if ops_needed > numOps:
                    break
            if ops_needed <= numOps:
                high = mid
            else:
                low = mid + 1
        return low
```

## C

```c
#include <string.h>

int minLength(char* s, int numOps) {
    int n = strlen(s);
    int left = 1, right = n;
    while (left < right) {
        int mid = left + (right - left) / 2; // candidate maximum length
        long long need = 0;
        for (int i = 0; i < n;) {
            char c = s[i];
            int j = i;
            while (j < n && s[j] == c) ++j;
            int len = j - i;
            need += len / (mid + 1);
            if (need > numOps) break;
            i = j;
        }
        if (need <= numOps)
            right = mid;
        else
            left = mid + 1;
    }
    return left;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinLength(string s, int numOps) {
        int n = s.Length;
        int[] pref0 = new int[n + 1];
        int[] pref1 = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pref0[i + 1] = pref0[i] + (s[i] == '0' ? 1 : 0);
            pref1[i + 1] = pref1[i] + (s[i] == '1' ? 1 : 0);
        }

        bool Can(int L) {
            const int INF = int.MaxValue / 2;
            int[] dp0 = new int[n + 1];
            int[] dp1 = new int[n + 1];
            for (int i = 0; i <= n; i++) {
                dp0[i] = dp1[i] = INF;
            }
            dp0[0] = dp1[0] = 0;

            int[] deq0 = new int[n + 2]; // stores indices for computing dp0 (uses dp1)
            int[] deq1 = new int[n + 2]; // stores indices for computing dp1 (uses dp0)
            int f0 = 0, b0 = 0;
            int f1 = 0, b1 = 0;

            // initial index 0
            deq0[b0++] = 0;
            deq1[b1++] = 0;

            for (int i = 1; i <= n; i++) {
                while (f0 < b0 && deq0[f0] < i - L) f0++;
                while (f1 < b1 && deq1[f1] < i - L) f1++;

                if (f0 < b0) {
                    int j = deq0[f0];
                    int best = dp1[j] + pref0[j] - j;
                    dp0[i] = i - pref0[i] + best;
                }

                if (f1 < b1) {
                    int j = deq1[f1];
                    int best = dp0[j] + pref1[j] - j;
                    dp1[i] = i - pref1[i] + best;
                }

                // add current index to deques
                int valForDeq0 = dp1[i] + pref0[i] - i;
                while (f0 < b0) {
                    int idx = deq0[b0 - 1];
                    int curVal = dp1[idx] + pref0[idx] - idx;
                    if (curVal <= valForDeq0) break;
                    b0--;
                }
                deq0[b0++] = i;

                int valForDeq1 = dp0[i] + pref1[i] - i;
                while (f1 < b1) {
                    int idx = deq1[b1 - 1];
                    int curVal = dp0[idx] + pref1[idx] - idx;
                    if (curVal <= valForDeq1) break;
                    b1--;
                }
                deq1[b1++] = i;
            }

            int minFlips = Math.Min(dp0[n], dp1[n]);
            return minFlips <= numOps;
        }

        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} numOps
 * @return {number}
 */
var minLength = function(s, numOps) {
    const n = s.length;
    let low = 1, high = n;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        let ops = 0;
        for (let i = 0; i < n;) {
            let j = i;
            while (j < n && s[j] === s[i]) j++;
            const len = j - i;
            ops += Math.floor(len / (mid + 1));
            if (ops > numOps) break;
            i = j;
        }
        if (ops <= numOps) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function minLength(s: string, numOps: number): number {
    const n = s.length;
    const runs: number[] = [];
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        runs.push(j - i);
        i = j;
    }

    const feasible = (L: number): boolean => {
        const block = L + 1;
        let ops = 0;
        for (const len of runs) {
            ops += Math.floor(len / block);
            if (ops > numOps) return false;
        }
        return ops <= numOps;
    };

    let lo = 1, hi = n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (feasible(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $numOps
     * @return Integer
     */
    function minLength($s, $numOps) {
        $n = strlen($s);
        $low = 1;
        $high = $n;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canAchieve($s, $numOps, $mid)) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }

    private function canAchieve(string $s, int $k, int $L): bool {
        $n = strlen($s);
        $need = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i + 1;
            while ($j < $n && $s[$j] === $s[$i]) {
                $j++;
            }
            $len = $j - $i;
            $need += intdiv($len, $L + 1);
            if ($need > $k) {
                return false;
            }
            $i = $j;
        }
        return $need <= $k;
    }
}
```

## Swift

```swift
class Solution {
    func minLength(_ s: String, _ numOps: Int) -> Int {
        let chars = Array(s)
        var runs = [Int]()
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] {
                j += 1
            }
            runs.append(j - i)
            i = j
        }
        
        var low = 1
        var high = chars.count
        while low < high {
            let mid = (low + high) / 2
            var opsNeeded = 0
            for len in runs {
                opsNeeded += len / (mid + 1)
                if opsNeeded > numOps { break }
            }
            if opsNeeded <= numOps {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minLength(s: String, numOps: Int): Int {
        val runs = mutableListOf<Int>()
        var i = 0
        while (i < s.length) {
            var j = i
            while (j < s.length && s[j] == s[i]) j++
            runs.add(j - i)
            i = j
        }
        var low = 1
        var high = s.length
        while (low < high) {
            val mid = (low + high) / 2
            if (canAchieve(mid, runs, numOps)) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }

    private fun canAchieve(L: Int, runs: List<Int>, k: Int): Boolean {
        var opsNeeded = 0L
        val divisor = L + 1
        for (len in runs) {
            opsNeeded += len / divisor
            if (opsNeeded > k) return false
        }
        return opsNeeded <= k
    }
}
```

## Dart

```dart
class Solution {
  int minLength(String s, int numOps) {
    bool can(int L) {
      int flips = 0;
      String prevChar = '';
      int cnt = 0;
      for (int i = 0; i < s.length; i++) {
        String c = s[i];
        if (i == 0) {
          prevChar = c;
          cnt = 1;
        } else {
          if (c == prevChar) {
            cnt++;
            if (cnt > L) {
              flips++;
              // flip current character
              prevChar = (prevChar == '0') ? '1' : '0';
              cnt = 1;
            }
          } else {
            prevChar = c;
            cnt = 1;
          }
        }
        if (flips > numOps) return false;
      }
      return flips <= numOps;
    }

    int low = 1, high = s.length;
    while (low < high) {
      int mid = (low + high) >> 1;
      if (can(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func minLength(s string, numOps int) int {
    n := len(s)
    low, high := 1, n
    for low < high {
        mid := (low + high) / 2
        opsNeeded := 0
        cnt := 1
        for i := 1; i < n; i++ {
            if s[i] == s[i-1] {
                cnt++
            } else {
                opsNeeded += cnt / (mid + 1)
                cnt = 1
            }
        }
        opsNeeded += cnt / (mid + 1)

        if opsNeeded <= numOps {
            high = mid
        } else {
            low = mid + 1
        }
    }
    return low
}
```

## Ruby

```ruby
def min_length(s, num_ops)
  n = s.length
  runs = []
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && s.getbyte(j) == s.getbyte(i)
    runs << (j - i)
    i = j
  end

  low = 1
  high = n
  while low < high
    mid = (low + high) / 2
    needed = 0
    runs.each do |len|
      needed += len / (mid + 1)
      break if needed > num_ops
    end
    if needed <= num_ops
      high = mid
    else
      low = mid + 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def minLength(s: String, numOps: Int): Int = {
        val n = s.length
        val runs = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && s.charAt(j) == s.charAt(i)) j += 1
            runs += (j - i)
            i = j
        }

        def feasible(L: Int): Boolean = {
            val block = L + 1
            var need: Long = 0L
            var idx = 0
            while (idx < runs.length) {
                need += runs(idx) / block
                if (need > numOps) return false
                idx += 1
            }
            need <= numOps
        }

        var lo = 1
        var hi = n
        while (lo < hi) {
            val mid = (lo + hi) >>> 1
            if (feasible(mid)) hi = mid else lo = mid + 1
        }
        lo
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_length(s: String, num_ops: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut low: usize = 1;
        let mut high: usize = n;
        while low < high {
            let mid = (low + high) / 2;
            if Self::required_ops(&bytes, mid) <= num_ops as i64 {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        low as i32
    }

    fn required_ops(bytes: &[u8], max_len: usize) -> i64 {
        let mut ops: i64 = 0;
        let mut i = 0;
        while i < bytes.len() {
            let cur = bytes[i];
            let mut j = i + 1;
            while j < bytes.len() && bytes[j] == cur {
                j += 1;
            }
            let run_len = j - i;
            ops += (run_len / (max_len + 1)) as i64;
            i = j;
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (min-length s numOps)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length s)])
    (let loop ((lo 1) (hi n))
      (if (= lo hi)
          lo
          (let* ([mid (quotient (+ lo hi) 2)]
                 [block-size (+ mid 1)]
                 [need
                  (let ([need 0] [cnt 0] [prev #\space])
                    (for ([i (in-range n)])
                      (let ([c (string-ref s i)])
                        (if (char=? c prev)
                            (set! cnt (+ cnt 1))
                            (begin
                              (when (> cnt 0)
                                (set! need (+ need (quotient cnt block-size))))
                              (set! cnt 1)
                              (set! prev c)))))
                    (when (> cnt 0)
                      (set! need (+ need (quotient cnt block-size))))
                    need)])
            (if (<= need numOps)
                (loop lo mid)
                (loop (+ mid 1) hi))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_length/2]).

-spec min_length(S :: unicode:unicode_binary(), NumOps :: integer()) -> integer().
min_length(S, NumOps) ->
    N = byte_size(S),
    Runs = get_runs(S, [], 0, undefined),
    binary_search(1, N, Runs, NumOps).

%% Build list of run lengths from the binary string.
-spec get_runs(binary(), [integer()], integer(), maybe_improper_list()) -> [integer()].
get_runs(<<>>, Acc, 0, _) ->
    lists:reverse(Acc);
get_runs(<<>>, Acc, CurLen, _) ->
    lists:reverse([CurLen | Acc]);
get_runs(<<C, Rest/binary>>, Acc, CurLen, undefined) ->
    get_runs(Rest, Acc, 1, C);
get_runs(<<C, Rest/binary>>, Acc, CurLen, Prev) when C =:= Prev ->
    get_runs(Rest, Acc, CurLen + 1, Prev);
get_runs(<<C, Rest/binary>>, Acc, CurLen, _Prev) ->
    get_runs(Rest, [CurLen | Acc], 1, C).

%% Binary search for minimal feasible length.
-spec binary_search(integer(), integer(), [integer()], integer()) -> integer().
binary_search(Low, High, Runs, K) when Low >= High ->
    Low;
binary_search(Low, High, Runs, K) ->
    Mid = (Low + High) div 2,
    case feasible(Runs, Mid, K) of
        true -> binary_search(Low, Mid, Runs, K);
        false -> binary_search(Mid + 1, High, Runs, K)
    end.

%% Check if we can achieve max run length <= L with at most K flips.
-spec feasible([integer()], integer(), integer()) -> boolean().
feasible(Runs, L, K) ->
    Needed = needed_flips(Runs, L),
    Needed =< K.

%% Total flips required for given maximum allowed run length L.
-spec needed_flips([integer()], integer()) -> integer().
needed_flips(Runs, L) ->
    lists:foldl(fun(Len, Sum) -> Sum + (Len - 1) div L end, 0, Runs).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_length(s :: String.t(), num_ops :: integer) :: integer
  def min_length(s, num_ops) do
    n = String.length(s)
    chars = String.to_charlist(s)

    binary_search(1, n, chars, num_ops)
  end

  defp binary_search(low, high, chars, k) when low < high do
    mid = div(low + high, 2)
    limit = mid + 1
    needed = flips_needed(chars, limit)

    if needed <= k do
      binary_search(low, mid, chars, k)
    else
      binary_search(mid + 1, high, chars, k)
    end
  end

  defp binary_search(low, _high, _chars, _k), do: low

  defp flips_needed(chars, limit) do
    {_, last_len, total_before} =
      Enum.reduce(chars, {nil, 0, 0}, fn ch, {prev, len, acc} ->
        cond do
          prev == nil ->
            {ch, 1, acc}

          ch == prev ->
            {prev, len + 1, acc}

          true ->
            new_acc = acc + div(len, limit)
            {ch, 1, new_acc}
        end
      end)

    total_before + div(last_len, limit)
  end
end
```
