# 2767. Partition String Into Minimum Beautiful Substrings

## Cpp

```cpp
class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        const int INF = 1e9;
        // Precompute binary strings of powers of 5 up to length 15
        vector<string> good;
        long long val = 1;
        while (true) {
            string bin;
            long long tmp = val;
            while (tmp > 0) {
                bin.push_back((tmp & 1) ? '1' : '0');
                tmp >>= 1;
            }
            reverse(bin.begin(), bin.end());
            if ((int)bin.size() > (int)s.size()) break;
            good.push_back(bin);
            val *= 5;
        }

        int n = s.size();
        vector<int> dp(n + 1, INF);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '0') continue; // cannot start with leading zero
            for (const string& p : good) {
                int len = p.size();
                if (i + len > n) continue;
                bool match = true;
                for (int k = 0; k < len; ++k) {
                    if (s[i + k] != p[k]) { match = false; break; }
                }
                if (match && dp[i + len] != INF) {
                    dp[i] = min(dp[i], 1 + dp[i + len]);
                }
            }
        }
        return dp[0] == INF ? -1 : dp[0];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumBeautifulSubstrings(String s) {
        Set<String> beautiful = new HashSet<>();
        long val = 1;
        // maximum value representable by a binary string of length up to 15
        long limit = (1L << 15);
        while (val <= limit) {
            beautiful.add(Long.toBinaryString(val));
            if (val > Long.MAX_VALUE / 5) break; // prevent overflow
            val *= 5;
        }

        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n] = 0;

        for (int i = n - 1; i >= 0; --i) {
            if (s.charAt(i) == '0') continue; // leading zero not allowed
            for (int j = i + 1; j <= n; ++j) {
                String sub = s.substring(i, j);
                if (beautiful.contains(sub) && dp[j] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[0] == Integer.MAX_VALUE ? -1 : dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minimumBeautifulSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # precompute binary strings of powers of 5 up to length n (max length 15)
        powers = set()
        val = 1
        limit = (1 << 15) - 1  # maximum value for length <=15 bits
        while val <= limit:
            b = bin(val)[2:]
            if len(b) <= n:
                powers.add(b)
            val *= 5

        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            # substrings must start with '1' (no leading zeros)
            if s[i] == '0':
                continue
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub in powers:
                    dp[j] = min(dp[j], dp[i] + 1)

        return -1 if dp[n] == INF else dp[n]
```

## Python3

```python
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        max_val = (1 << n) - 1
        beautiful = set()
        p = 1
        while p <= max_val:
            beautiful.add(bin(p)[2:])
            p *= 5

        INF = n + 1
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub in beautiful and dp[j] != INF:
                    dp[i] = min(dp[i], 1 + dp[j])

        return -1 if dp[0] == INF else dp[0]
```

## C

```c
#include <string.h>

static int isPowerOfFive(int x) {
    if (x <= 0) return 0;
    while (x % 5 == 0) x /= 5;
    return x == 1;
}

int minimumBeautifulSubstrings(char* s) {
    int n = strlen(s);
    const int INF = 100;
    int dp[16];
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[n] = 0;

    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '0') continue;          // cannot start with leading zero
        int val = 0;
        for (int j = i; j < n; ++j) {
            val = (val << 1) + (s[j] - '0');
            if (isPowerOfFive(val)) {
                if (dp[j + 1] != INF && dp[i] > 1 + dp[j + 1])
                    dp[i] = 1 + dp[j + 1];
            }
        }
    }

    return dp[0] == INF ? -1 : dp[0];
}
```

## Csharp

```csharp
public class Solution
{
    private HashSet<string> _beautiful;
    private int[] _memo;
    private string _s;

    public int MinimumBeautifulSubstrings(string s)
    {
        _s = s;
        PrecomputeBeautiful();
        int n = s.Length;
        _memo = new int[n + 1];
        for (int i = 0; i <= n; i++) _memo[i] = -2; // uncomputed
        int ans = Dp(0);
        return ans == int.MaxValue ? -1 : ans;
    }

    private void PrecomputeBeautiful()
    {
        _beautiful = new HashSet<string>();
        long val = 1;
        // maximum possible value for length <=15 bits is (1<<15)-1 = 32767
        const long limit = (1L << 15);
        while (val <= limit)
        {
            _beautiful.Add(Convert.ToString(val, 2));
            val *= 5;
        }
    }

    private int Dp(int idx)
    {
        if (idx == _s.Length) return 0;
        if (_memo[idx] != -2) return _memo[idx];
        // substrings must not start with '0'
        if (_s[idx] == '0')
        {
            _memo[idx] = int.MaxValue;
            return _memo[idx];
        }

        int best = int.MaxValue;
        for (int end = idx; end < _s.Length; ++end)
        {
            string sub = _s.Substring(idx, end - idx + 1);
            if (_beautiful.Contains(sub))
            {
                int next = Dp(end + 1);
                if (next != int.MaxValue)
                    best = Math.Min(best, 1 + next);
            }
        }

        _memo[idx] = best;
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumBeautifulSubstrings = function(s) {
    const n = s.length;
    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array(n + 1).fill(INF);
    dp[n] = 0;

    // helper to check if a binary string is beautiful
    const isBeautiful = (sub) => {
        if (sub[0] === '0') return false; // leading zero not allowed
        let val = parseInt(sub, 2);
        if (val === 0) return false;
        while (val > 1 && val % 5 === 0) {
            val /= 5;
        }
        return val === 1;
    };

    for (let i = n - 1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            const sub = s.slice(i, j + 1);
            if (isBeautiful(sub) && dp[j + 1] !== INF) {
                dp[i] = Math.min(dp[i], 1 + dp[j + 1]);
            }
        }
    }

    return dp[0] === INF ? -1 : dp[0];
};
```

## Typescript

```typescript
function minimumBeautifulSubstrings(s: string): number {
    const n = s.length;
    const INF = Number.MAX_SAFE_INTEGER;

    // Precompute all powers of 5 that fit into 15 bits
    const maxVal = (1 << n) - 1; // maximum possible value for given length
    const powerSet = new Set<number>();
    let p = 1;
    while (p <= maxVal) {
        powerSet.add(p);
        p *= 5;
    }

    const dp = new Array(n + 1).fill(INF);
    dp[n] = 0; // empty suffix needs zero substrings

    for (let i = n - 1; i >= 0; --i) {
        if (s[i] === '0') continue; // cannot start with leading zero
        let val = 0;
        for (let j = i; j < n; ++j) {
            val = (val << 1) + (s.charCodeAt(j) - 48); // build binary value
            if (powerSet.has(val)) {
                dp[i] = Math.min(dp[i], 1 + dp[j + 1]);
            }
        }
    }

    return dp[0] === INF ? -1 : dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumBeautifulSubstrings($s) {
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === PHP_INT_MAX) continue;
            for ($j = $i + 1; $j <= $n; $j++) {
                $sub = substr($s, $i, $j - $i);
                if ($this->isBeautiful($sub)) {
                    $dp[$j] = min($dp[$j], $dp[$i] + 1);
                }
            }
        }

        return $dp[$n] === PHP_INT_MAX ? -1 : $dp[$n];
    }

    private function isBeautiful(string $binary): bool {
        // must start with '1' (no leading zeros) and represent a power of 5
        if ($binary[0] !== '1') return false;
        $value = bindec($binary);
        if ($value === 0) return false;

        while ($value > 1 && $value % 5 === 0) {
            $value = intdiv($value, 5);
        }
        return $value === 1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumBeautifulSubstrings(_ s: String) -> Int {
        let n = s.count
        var powerSet = Set<String>()
        var val = 1
        while val <= (1 << n) - 1 && val > 0 {
            powerSet.insert(String(val, radix: 2))
            if Int.max / 5 < val { break }
            val *= 5
        }
        
        let chars = Array(s)
        let INF = n + 5
        var dp = Array(repeating: INF, count: n + 1)
        dp[n] = 0
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "0" { continue }
            var substr = ""
            for j in i..<n {
                substr.append(chars[j])
                if powerSet.contains(substr) {
                    dp[i] = min(dp[i], 1 + dp[j + 1])
                }
            }
        }
        
        return dp[0] >= INF ? -1 : dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumBeautifulSubstrings(s: String): Int {
        // Precompute binary representations of powers of 5 within the possible range
        val maxVal = (1 shl s.length) - 1
        val beautifulSet = mutableSetOf<String>()
        var p = 1L
        while (p <= maxVal) {
            beautifulSet.add(p.toString(2))
            p *= 5
        }

        val n = s.length
        val INF = Int.MAX_VALUE / 4
        val dp = IntArray(n + 1) { INF }
        dp[n] = 0

        for (i in n - 1 downTo 0) {
            if (s[i] == '0') continue  // substrings cannot have leading zeros
            var j = i + 1
            while (j <= n) {
                val sub = s.substring(i, j)
                if (beautifulSet.contains(sub)) {
                    dp[i] = minOf(dp[i], 1 + dp[j])
                }
                j++
            }
        }

        return if (dp[0] >= INF) -1 else dp[0]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimumBeautifulSubstrings(String s) {
    // Precompute binary representations of powers of 5 up to the length of s
    Set<String> beautiful = {};
    int val = 1;
    while (true) {
      String bin = val.toRadixString(2);
      if (bin.length > s.length) break;
      beautiful.add(bin);
      val *= 5;
    }

    int n = s.length;
    const int INF = 1 << 30;
    List<int> dp = List.filled(n + 1, INF);
    dp[n] = 0;

    for (int i = n - 1; i >= 0; --i) {
      if (s[i] == '0') continue; // substrings cannot have leading zeros
      for (int j = i; j < n; ++j) {
        String sub = s.substring(i, j + 1);
        if (beautiful.contains(sub)) {
          dp[i] = min(dp[i], dp[j + 1] + 1);
        }
      }
    }

    return dp[0] >= INF ? -1 : dp[0];
  }
}
```

## Golang

```go
func minimumBeautifulSubstrings(s string) int {
	n := len(s)
	// precompute binary representations of powers of 5 that fit in at most n bits
	maxVal := (1 << n) - 1
	beautiful := make(map[string]struct{})
	for v := 1; v <= maxVal; v *= 5 {
		bin := strconv.FormatInt(int64(v), 2)
		if len(bin) > n {
			break
		}
		beautiful[bin] = struct{}{}
		if v > maxVal/5 { // prevent overflow
			break
		}
	}

	const INF = int(1e9)
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = INF
	}
	dp[n] = 0

	for i := n - 1; i >= 0; i-- {
		if s[i] == '0' { // leading zero not allowed
			continue
		}
		for j := i + 1; j <= n; j++ {
			sub := s[i:j]
			if _, ok := beautiful[sub]; ok && dp[j] != INF {
				if 1+dp[j] < dp[i] {
					dp[i] = 1 + dp[j]
				}
			}
		}
	}

	if dp[0] == INF {
		return -1
	}
	return dp[0]
}
```

## Ruby

```ruby
def minimum_beautiful_substrings(s)
  n = s.length
  limit = (1 << n) - 1
  beautiful = {}
  val = 1
  while val <= limit
    beautiful[val.to_s(2)] = true
    val *= 5
  end

  inf = 1 << 30
  dp = Array.new(n + 1, inf)
  dp[n] = 0

  (n - 1).downto(0) do |i|
    next if s[i] == '0' # leading zero not allowed
    best = inf
    (i + 1).upto(n) do |j|
      sub = s[i...j]
      if beautiful[sub] && dp[j] != inf
        cand = 1 + dp[j]
        best = cand if cand < best
      end
    end
    dp[i] = best
  end

  ans = dp[0]
  ans == inf ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minimumBeautifulSubstrings(s: String): Int = {
        val n = s.length
        val INF = 1 << 30
        val dp = Array.fill(n + 1)(INF)
        dp(n) = 0

        def isPowerOf5(x: Long): Boolean = {
            if (x <= 0) return false
            var v = x
            while (v % 5 == 0) v /= 5
            v == 1
        }

        for (i <- n - 1 to 0 by -1) {
            if (s(i) == '1') {
                var value: Long = 0L
                for (j <- i until n) {
                    value = (value << 1) + (s(j) - '0')
                    if (isPowerOf5(value)) {
                        dp(i) = math.min(dp(i), 1 + dp(j + 1))
                    }
                }
            }
        }

        if (dp(0) >= INF) -1 else dp(0)
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn minimum_beautiful_substrings(s: String) -> i32 {
        // Precompute binary representations of powers of 5 that fit into length <=15
        let mut beautiful = HashSet::new();
        let mut val: u64 = 1;
        while val <= (1u64 << 15) {
            beautiful.insert(format!("{:b}", val));
            match val.checked_mul(5) {
                Some(next) => val = next,
                None => break,
            }
        }

        let n = s.len();
        const INF: i32 = 1_000_000;
        let mut dp = vec![INF; n + 1];
        dp[n] = 0;

        // DP from end to start
        for i in (0..n).rev() {
            if s.as_bytes()[i] == b'0' {
                continue; // substrings must not have leading zeros
            }
            for j in i + 1..=n {
                let sub = &s[i..j];
                if beautiful.contains(sub) && dp[j] != INF {
                    dp[i] = dp[i].min(dp[j] + 1);
                }
            }
        }

        if dp[0] == INF { -1 } else { dp[0] }
    }
}
```

## Racket

```racket
(define/contract (minimum-beautiful-substrings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (max-val (expt 2 n))                     ; exclusive upper bound for values
         ;; generate binary strings of powers of 5 up to max-val
         (powers (let loop ((p 1) (acc '()))
                   (if (> p max-val)
                       acc
                       (loop (* p 5) (cons (format "~b" p) acc)))))
         (power-set (let ((h (make-hash)))
                      (for ([bin powers])
                        (hash-set! h bin #t))
                      h))
         (inf 1000)                               ; larger than any possible answer
         (dp (make-vector (+ n 1) inf)))        ; dp[i] = min substrings for suffix starting at i
    (vector-set! dp n 0)
    (for ([i (in-range (sub1 n) -1 -1)])          ; iterate from n-1 down to 0
      (for ([end (in-range (+ i 1) (+ n 1))])   ; end is exclusive index of substring
        (define substr (substring s i end))
        (when (hash-has-key? power-set substr)
          (let ((cand (+ 1 (vector-ref dp end))))
            (when (< cand (vector-ref dp i))
              (vector-set! dp i cand))))))
    (let ((ans (vector-ref dp 0)))
      (if (>= ans inf) -1 ans))))
```

## Erlang

```erlang
-spec minimum_beautiful_substrings(S :: unicode:unicode_binary()) -> integer().
minimum_beautiful_substrings(S) ->
    Powers = [1,5,25,125,625,3125,15625],
    Len = byte_size(S),
    DP0 = erlang:make_tuple(Len + 1, ?INF),
    DP1 = erlang:setelement(Len + 1, DP0, 0), % dp[Len] = 0
    DPFinal = loop_i(Len - 1, Len, S, Powers, DP1),
    Answer = element(1, DPFinal),
    if Answer >= ?INF -> -1; true -> Answer end.

-define(INF, 1000).

loop_i(-1, _Len, _S, _Powers, DP) ->
    DP;
loop_i(I, Len, S, Powers, DP) ->
    Char = binary:at(S, I),
    NewDP =
        case Char of
            $0 -> erlang:setelement(I + 1, DP, ?INF);
            _ ->
                Min = loop_j(I, I + 1, Len, S, Powers, DP, ?INF),
                erlang:setelement(I + 1, DP, Min)
        end,
    loop_i(I - 1, Len, S, Powers, NewDP).

loop_j(_I, J, Len, _S, _Powers, DP, CurMin) when J > Len ->
    CurMin;
loop_j(I, J, Len, S, Powers, DP, CurMin) ->
    SubBin = binary:part(S, {I, J - I}),
    NewMin =
        case is_beautiful(SubBin, Powers) of
            true ->
                ValJ = element(J + 1, DP),
                Candidate = if ValJ >= ?INF -> ?INF; true -> 1 + ValJ end,
                erlang:min(CurMin, Candidate);
            false -> CurMin
        end,
    loop_j(I, J + 1, Len, S, Powers, DP, NewMin).

is_beautiful(SubBin, Powers) ->
    case binary:at(SubBin, 0) of
        $0 -> false;
        _ ->
            Value = bin_to_int(SubBin, 0),
            lists:member(Value, Powers)
    end.

bin_to_int(<<>>, Acc) -> Acc;
bin_to_int(<<C:8, Rest/binary>>, Acc) ->
    NewAcc = Acc * 2 + (C - $0),
    bin_to_int(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_beautiful_substrings(s :: String.t()) :: integer
  def minimum_beautiful_substrings(s) do
    n = String.length(s)

    beautiful_set =
      s
      |> generate_beautiful_binaries()
      |> MapSet.new()

    dp =
      Enum.reduce(Enum.reverse(0..(n - 1)), %{n => 0}, fn i, acc ->
        min_parts =
          Enum.reduce(i + 1..n, :infinity, fn j, cur_min ->
            sub = String.slice(s, i, j - i)

            if MapSet.member?(beautiful_set, sub) do
              case Map.get(acc, j) do
                nil -> cur_min
                val when is_integer(val) ->
                  cand = 1 + val
                  if cand < cur_min, do: cand, else: cur_min
              end
            else
              cur_min
            end
          end)

        Map.put(acc, i, min_parts)
      end)

    case Map.get(dp, 0) do
      :infinity -> -1
      val when is_integer(val) -> val
    end
  end

  defp generate_beautiful_binaries(s) do
    max_len = String.length(s)

    Enum.reduce_while(0..30, [], fn exp, acc ->
      val = :math.pow(5, exp) |> trunc()
      bin = Integer.to_string(val, 2)

      if String.length(bin) > max_len do
        {:halt, acc}
      else
        {:cont, [bin | acc]}
      end
    end)
  end
end
```
