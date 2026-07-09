# 1573. Number of Ways to Split a String

## Cpp

```cpp
class Solution {
public:
    int numWays(string s) {
        const long long MOD = 1000000007LL;
        int n = s.size();
        vector<int> pos;
        pos.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') pos.push_back(i);
        }
        long long totalOnes = pos.size();
        if (totalOnes == 0) {
            long long ways = (long long)(n - 1) * (n - 2) / 2 % MOD;
            return (int)ways;
        }
        if (totalOnes % 3 != 0) return 0;
        int k = totalOnes / 3; // each part must contain k ones
        long long leftZeros = pos[k] - pos[k - 1] - 1;
        long long rightZeros = pos[2 * k] - pos[2 * k - 1] - 1;
        long long ans = ((leftZeros + 1) % MOD) * ((rightZeros + 1) % MOD) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numWays(String s) {
        int n = s.length();
        long totalOnes = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') totalOnes++;
        }
        if (totalOnes % 3 != 0) return 0;
        if (totalOnes == 0) {
            long ways = ((long) (n - 1) * (n - 2) / 2) % MOD;
            return (int) ways;
        }
        long target = totalOnes / 3;
        long cntFirst = 0, cntSecond = 0;
        long onesSeen = 0;
        for (int i = 0; i < n - 1; i++) { // split positions must leave at least one char for the third part
            if (s.charAt(i) == '1') onesSeen++;
            if (onesSeen == target) {
                cntFirst++;
            } else if (onesSeen == 2 * target) {
                cntSecond++;
            }
        }
        long ans = (cntFirst % MOD) * (cntSecond % MOD) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        total_ones = s.count('1')
        if total_ones % 3 != 0:
            return 0
        target = total_ones // 3
        cnt_first = 0
        ans = 0
        ones_sofar = 0
        # iterate up to second last character to ensure third part non‑empty
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones_sofar += 1
            if ones_sofar == 2 * target:
                ans = (ans + cnt_first) % MOD
            if ones_sofar == target:
                cnt_first += 1
        return ans % MOD
```

## Python3

```python
class Solution:
    def numWays(self, s: str) -> int:
        total_ones = s.count('1')
        n = len(s)
        if total_ones == 0:
            # choose any two split points among n-1 gaps
            return (n - 1) * (n - 2) // 2
        if total_ones % 3 != 0:
            return 0

        target = total_ones // 3
        first_cut_options = 0
        ways = 0
        ones_so_far = 0

        for i, ch in enumerate(s):
            if ch == '1':
                ones_so_far += 1
            if ones_so_far == target:
                # possible place to cut after position i (i < n-1)
                first_cut_options += 1
            elif ones_so_far == 2 * target:
                # possible second cut after position i, add all first cut options before it
                ways += first_cut_options

        return ways
```

## C

```c
#include <string.h>
#define MOD 1000000007LL

int numWays(char* s) {
    int n = strlen(s);
    long long totalOnes = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') totalOnes++;
    }
    
    if (totalOnes == 0) {
        long long ways = ((long long)(n - 1) * (n - 2) / 2) % MOD;
        return (int)ways;
    }
    
    if (totalOnes % 3 != 0) return 0;
    
    long long target = totalOnes / 3;
    long long cnt = 0;
    int first = -1, second = -1, third = -1, fourth = -1;
    
    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') {
            cnt++;
            if (cnt == target) first = i;
            if (cnt == target + 1) second = i;
            if (cnt == 2 * target) third = i;
            if (cnt == 2 * target + 1) fourth = i;
        }
    }
    
    long long zerosBetweenFirst = second - first - 1;
    long long zerosBetweenSecond = fourth - third - 1;
    
    long long ans = ((zerosBetweenFirst + 1) % MOD) * ((zerosBetweenSecond + 1) % MOD) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumWays(string s) {
        const long MOD = 1000000007L;
        int n = s.Length;
        long totalOnes = 0;
        foreach (char c in s) if (c == '1') totalOnes++;
        if (totalOnes == 0) {
            long ways = ((long)(n - 1) * (n - 2) / 2) % MOD;
            return (int)ways;
        }
        if (totalOnes % 3 != 0) return 0;
        long k = totalOnes / 3;
        long cntFirst = 0, ans = 0, prefix = 0;
        foreach (char c in s) {
            if (c == '1') prefix++;
            if (prefix == k) {
                cntFirst = (cntFirst + 1) % MOD;
            } else if (prefix == 2 * k) {
                ans = (ans + cntFirst) % MOD;
            }
        }
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numWays = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    let totalOnes = 0;
    for (let ch of s) if (ch === '1') totalOnes++;
    if (totalOnes % 3 !== 0) return 0;
    if (totalOnes === 0) {
        // choose any two cut positions among n-1 gaps
        const ways = ((n - 1) * (n - 2) / 2) % MOD;
        return ways;
    }
    const target = totalOnes / 3;
    let cum = 0, cntFirst = 0, cntSecond = 0;
    for (let i = 0; i < n - 1; ++i) {
        if (s[i] === '1') cum++;
        if (cum === target) cntFirst++;
        else if (cum === 2 * target) cntSecond++;
    }
    return (cntFirst * cntSecond) % MOD;
};
```

## Typescript

```typescript
function numWays(s: string): number {
    const n = s.length;
    let totalOnes = 0;
    for (const ch of s) if (ch === '1') totalOnes++;

    // All zeros case
    if (totalOnes === 0) {
        return ((n - 1) * (n - 2)) / 2;
    }

    if (totalOnes % 3 !== 0) return 0;

    const target = totalOnes / 3;
    let cntFirst = 0, cntSecond = 0;
    let onesSeen = 0;

    for (let i = 0; i < n; i++) {
        if (s[i] === '1') ++onesSeen;

        if (onesSeen === target) {
            // count zeros after this position
            let zeroCnt = 0;
            let j = i + 1;
            while (j < n && s[j] === '0') {
                ++zeroCnt;
                ++j;
            }
            cntFirst = zeroCnt + 1; // include cut right after the target-th '1'
        }

        if (onesSeen === 2 * target) {
            let zeroCnt = 0;
            let j = i + 1;
            while (j < n && s[j] === '0') {
                ++zeroCnt;
                ++j;
            }
            cntSecond = zeroCnt + 1; // include cut right after the 2*target-th '1'
        }
    }

    return cntFirst * cntSecond;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numWays($s) {
        $MOD = 1000000007;
        $n = strlen($s);
        $totalOnes = substr_count($s, '1');
        if ($totalOnes % 3 !== 0) {
            return 0;
        }
        if ($totalOnes === 0) {
            // Choose any two cut positions among (n-1) gaps
            $ways = (($n - 1) * ($n - 2) / 2) % $MOD;
            return (int)$ways;
        }
        $target = intdiv($totalOnes, 3);
        $cum = 0;
        $cntFirst = 0;
        $ans = 0;
        // iterate up to n-2 inclusive; last position cannot be a cut for the second part
        for ($i = 0; $i < $n - 1; $i++) {
            if ($s[$i] === '1') {
                $cum++;
            }
            if ($cum == $target) {
                $cntFirst++;
            } elseif ($cum == 2 * $target) {
                $ans = ($ans + $cntFirst) % $MOD;
            }
        }
        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func numWays(_ s: String) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var onesPos = [Int]()
        onesPos.reserveCapacity(n)
        for i in 0..<n {
            if chars[i] == "1" {
                onesPos.append(i)
            }
        }
        let totalOnes = onesPos.count
        if totalOnes % 3 != 0 {
            return 0
        }
        if totalOnes == 0 {
            let ways = Int64(n - 1) * Int64(n - 2) / 2
            return Int(ways % Int64(MOD))
        }
        let k = totalOnes / 3
        let leftWays = onesPos[k] - onesPos[k - 1]
        let rightWays = onesPos[2 * k] - onesPos[2 * k - 1]
        let ans = (Int64(leftWays) * Int64(rightWays)) % Int64(MOD)
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numWays(s: String): Int {
        val MOD = 1_000_000_007L
        val n = s.length
        var totalOnes = 0
        for (ch in s) if (ch == '1') totalOnes++
        if (totalOnes % 3 != 0) return 0
        if (totalOnes == 0) {
            val ways = ((n - 1).toLong() * (n - 2) / 2) % MOD
            return ways.toInt()
        }
        val target = totalOnes / 3
        var prefixOnes = 0
        var cntFirst = 0L
        var ans = 0L
        for (i in 0 until n - 1) {
            if (s[i] == '1') prefixOnes++
            when (prefixOnes) {
                target -> cntFirst = (cntFirst + 1) % MOD
                2 * target -> ans = (ans + cntFirst) % MOD
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numWays(String s) {
    int n = s.length;
    int totalOnes = 0;
    for (int i = 0; i < n; ++i) {
      if (s.codeUnitAt(i) == 49) totalOnes++; // '1'
    }

    if (totalOnes == 0) {
      // Choose any two cut positions among n-1 possible gaps
      int ways = ((n - 1) * (n - 2) ~/ 2) % _mod;
      return ways;
    }

    if (totalOnes % 3 != 0) return 0;

    int target = totalOnes ~/ 3;
    int twoTarget = target * 2;

    int cur = 0;
    int firstCuts = 0;
    int answer = 0;

    // iterate up to n-2 (i < n-1) so that each cut leaves at least one character after it
    for (int i = 0; i < n - 1; ++i) {
      if (s.codeUnitAt(i) == 49) cur++;

      if (cur == target) {
        firstCuts++;
        if (firstCuts >= _mod) firstCuts -= _mod;
      } else if (cur == twoTarget) {
        answer += firstCuts;
        if (answer >= _mod) answer %= _mod;
      }
    }

    return answer % _mod;
  }
}
```

## Golang

```go
func numWays(s string) int {
	const MOD int64 = 1000000007
	n := len(s)
	totalOnes := 0
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			totalOnes++
		}
	}
	if totalOnes == 0 {
		ways := int64(n-1) * int64(n-2) / 2 % MOD
		return int(ways)
	}
	if totalOnes%3 != 0 {
		return 0
	}
	k := totalOnes / 3
	onesSeen := 0
	var firstZeros, secondZeros int64
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			onesSeen++
		} else {
			if onesSeen == k {
				firstZeros++
			} else if onesSeen == 2*k {
				secondZeros++
			}
		}
	}
	ways := ((firstZeros + 1) % MOD) * ((secondZeros + 1) % MOD) % MOD
	return int(ways)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def num_ways(s)
  n = s.length
  ones = []
  s.each_char.with_index { |ch, i| ones << i if ch == '1' }
  total = ones.size
  return ((n - 1) * (n - 2) / 2) % MOD if total == 0
  return 0 unless total % 3 == 0

  k = total / 3
  first_cut_options = ones[k] - ones[k - 1]
  second_cut_options = ones[2 * k] - ones[2 * k - 1]

  (first_cut_options * second_cut_options) % MOD
end
```

## Scala

```scala
object Solution {
    def numWays(s: String): Int = {
        val MOD = 1000000007L
        val n = s.length
        var totalOnes = 0
        for (c <- s) if (c == '1') totalOnes += 1

        if (totalOnes == 0) {
            val ways = ((n - 1).toLong * (n - 2) / 2) % MOD
            return ways.toInt
        }
        if (totalOnes % 3 != 0) return 0

        val target = totalOnes / 3
        var cum = 0
        var cntFirst: Long = 0
        var cntSecond: Long = 0

        for (i <- 0 until n - 1) {
            if (s.charAt(i) == '1') cum += 1
            if (cum == target) cntFirst += 1
            else if (cum == 2 * target) cntSecond += 1
        }

        val ans = (cntFirst % MOD) * (cntSecond % MOD) % MOD
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_ways(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len() as i64;
        let total_ones = s.as_bytes().iter().filter(|&&b| b == b'1').count() as i64;

        if total_ones == 0 {
            // choose any two cut positions among (n-1) gaps
            let ways = ((n - 1) * (n - 2) / 2) % MOD;
            return ways as i32;
        }

        if total_ones % 3 != 0 {
            return 0;
        }

        let target = total_ones / 3;
        let mut cnt = 0i64;
        let mut left = 0i64;
        let mut ans = 0i64;

        for &b in s.as_bytes() {
            if b == b'1' {
                cnt += 1;
            }
            if cnt == target {
                left += 1;
            } else if cnt == 2 * target {
                ans = (ans + left) % MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-ways s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         ;; count total number of '1's
         (total
          (let loop ((i 0) (cnt 0))
            (if (= i n)
                cnt
                (loop (+ i 1)
                      (if (char=? (string-ref s i) #\1)
                          (+ cnt 1)
                          cnt))))))
    (cond
      [(not (= (remainder total 3) 0)) 0]               ; cannot split evenly
      [(= total 0)                                      ; all zeros
       (let* ((a (- n 1))
              (b (- n 2))
              (ways (/ (* a b) 2)))                     ; C(n-1,2)
         (modulo ways MOD))]
      [else
       (let* ((target (/ total 3))
              (left 0)
              (right 0)
              (cum 0))
         (for ([i (in-range n)])
           (when (char=? (string-ref s i) #\1)
             (set! cum (+ cum 1)))
           (cond
             [(= cum target)   (set! left (+ left 1))]
             [(= cum (* 2 target)) (set! right (+ right 1))]))
         (modulo (* left right) MOD))])))
```

## Erlang

```erlang
-spec num_ways(S :: unicode:unicode_binary()) -> integer().
num_ways(S) ->
    Mod = 1000000007,
    Len = byte_size(S),
    TotalOnes = count_ones(S, 0),
    case TotalOnes of
        0 ->
            N1 = Len - 1,
            ((N1 * (N1 - 1) div 2) rem Mod);
        _ when TotalOnes rem 3 =/= 0 ->
            0;
        _ ->
            Target = TotalOnes div 3,
            loop(S, Target, 0, 0, 0, Mod)
    end.

count_ones(<<>>, Acc) -> Acc;
count_ones(<<$1, Rest/binary>>, Acc) -> count_ones(Rest, Acc + 1);
count_ones(<<_, Rest/binary>>, Acc) -> count_ones(Rest, Acc).

loop(<<>>, _Target, _PrefixCnt, _OnesSoFar, Acc, _Mod) ->
    Acc;
loop(<<C, Rest/binary>>, Target, PrefixCnt, OnesSoFar, Acc, Mod) ->
    NewOnes = OnesSoFar + (if C == $1 -> 1; true -> 0 end),
    case NewOnes of
        T when T == Target ->
            loop(Rest, Target, PrefixCnt + 1, NewOnes, Acc, Mod);
        TT when TT == 2 * Target ->
            NewAcc = (Acc + PrefixCnt) rem Mod,
            loop(Rest, Target, PrefixCnt, NewOnes, NewAcc, Mod);
        _ ->
            loop(Rest, Target, PrefixCnt, NewOnes, Acc, Mod)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec num_ways(s :: String.t()) :: integer()
  def num_ways(s) do
    chars = :binary.bin_to_list(s)
    total = Enum.count(chars, fn c -> c == ?1 end)
    n = length(chars)

    cond do
      total == 0 ->
        ((n - 1) * (n - 2) div 2) |> rem(@mod)

      rem(total, 3) != 0 ->
        0

      true ->
        k = div(total, 3)

        {cnt1, cnt2, _} =
          Enum.reduce(chars, {0, 0, 0}, fn c, {c1, c2, sum} ->
            sum = sum + if c == ?1, do: 1, else: 0
            c1 = if sum == k, do: c1 + 1, else: c1
            c2 = if sum == 2 * k, do: c2 + 1, else: c2
            {c1, c2, sum}
          end)

        rem(cnt1 * cnt2, @mod)
    end
  end
end
```
