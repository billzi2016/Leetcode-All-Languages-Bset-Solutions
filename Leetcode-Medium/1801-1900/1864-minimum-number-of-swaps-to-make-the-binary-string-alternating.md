# 1864. Minimum Number of Swaps to Make the Binary String Alternating

## Cpp

```cpp
class Solution {
public:
    int minSwaps(string s) {
        int n = s.size();
        int cnt0 = 0;
        for (char c : s) if (c == '0') ++cnt0;
        int ans = INT_MAX;
        // pattern starting with '0'
        int needZero0 = (n + 1) / 2; // ceil(n/2)
        if (cnt0 == needZero0) {
            int diff = 0;
            for (int i = 0; i < n; ++i) {
                char expected = (i % 2 == 0) ? '0' : '1';
                if (s[i] != expected) ++diff;
            }
            ans = min(ans, diff / 2);
        }
        // pattern starting with '1'
        int needZero1 = n / 2; // floor(n/2)
        if (cnt0 == needZero1) {
            int diff = 0;
            for (int i = 0; i < n; ++i) {
                char expected = (i % 2 == 0) ? '1' : '0';
                if (s[i] != expected) ++diff;
            }
            ans = min(ans, diff / 2);
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(String s) {
        int n = s.length();
        int cnt0 = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') cnt0++;
        }
        int cnt1 = n - cnt0;

        // Even length: both patterns possible only if counts are equal
        if ((n & 1) == 0) {
            if (cnt0 != cnt1) return -1;
            int swaps0 = computeSwaps(s, true);   // pattern starts with '0'
            int swaps1 = computeSwaps(s, false);  // pattern starts with '1'
            return Math.min(swaps0, swaps1);
        } else {
            int half = n / 2;          // floor
            int ceil = half + 1;       // ceil
            int ans = Integer.MAX_VALUE;
            if (cnt0 == ceil && cnt1 == half) {
                ans = Math.min(ans, computeSwaps(s, true));
            }
            if (cnt1 == ceil && cnt0 == half) {
                ans = Math.min(ans, computeSwaps(s, false));
            }
            return ans == Integer.MAX_VALUE ? -1 : ans;
        }
    }

    private int computeSwaps(String s, boolean startWithZero) {
        int type01 = 0; // have '0' but need '1'
        int type10 = 0; // have '1' but need '0'
        for (int i = 0; i < s.length(); i++) {
            char expected;
            if ((i & 1) == 0) {
                expected = startWithZero ? '0' : '1';
            } else {
                expected = startWithZero ? '1' : '0';
            }
            char actual = s.charAt(i);
            if (actual != expected) {
                if (actual == '0') {
                    type01++;
                } else {
                    type10++;
                }
            }
        }
        return Math.max(type01, type10);
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = n - cnt0

        # If the difference is more than 1, impossible
        if abs(cnt0 - cnt1) > 1:
            return -1

        def mismatches(start_char):
            mis = 0
            expected = start_char
            for ch in s:
                if ch != expected:
                    mis += 1
                # flip expected between '0' and '1'
                expected = '1' if expected == '0' else '0'
            return mis

        if n % 2 == 0:
            # both patterns possible, choose minimal swaps
            mis0 = mismatches('0')
            mis1 = mismatches('1')
            return min(mis0, mis1) // 2
        else:
            # only one pattern is feasible: majority character starts first
            if cnt0 > cnt1:
                mis = mismatches('0')
            else:
                mis = mismatches('1')
            return mis // 2
```

## Python3

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        ans = float('inf')

        # pattern starting with '0' -> "0101..."
        zeros_needed = (n + 1) // 2
        if cnt0 == zeros_needed:
            mism01 = 0  # positions where we have '0' but need '1'
            for i, ch in enumerate(s):
                expected = '0' if i % 2 == 0 else '1'
                if ch != expected and ch == '0':
                    mism01 += 1
            ans = min(ans, mism01)

        # pattern starting with '1' -> "1010..."
        zeros_needed = n // 2
        if cnt0 == zeros_needed:
            mism01 = 0
            for i, ch in enumerate(s):
                expected = '1' if i % 2 == 0 else '0'
                if ch != expected and ch == '0':
                    mism01 += 1
            ans = min(ans, mism01)

        return -1 if ans == float('inf') else ans
```

## C

```c
#include <string.h>
#include <limits.h>

int minSwaps(char* s) {
    int n = (int)strlen(s);
    int cnt0 = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') cnt0++;
    }
    int ans = INT_MAX;

    // Pattern starting with '0'
    if ((n % 2 == 0 && cnt0 == n / 2) ||
        (n % 2 == 1 && cnt0 == (n + 1) / 2)) {
        int mis01 = 0; // positions where we have '0' but need '1'
        for (int i = 0; i < n; ++i) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s[i] != expected && s[i] == '0') mis01++;
        }
        ans = mis01;
    }

    // Pattern starting with '1'
    if ((n % 2 == 0 && cnt0 == n / 2) ||
        (n % 2 == 1 && cnt0 == n / 2)) {
        int mis01 = 0; // positions where we have '0' but need '1' for this pattern
        for (int i = 0; i < n; ++i) {
            char expected = (i % 2 == 0) ? '1' : '0';
            if (s[i] != expected && s[i] == '0') mis01++;
        }
        if (mis01 < ans) ans = mis01;
    }

    return (ans == INT_MAX) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSwaps(string s) {
        int n = s.Length;
        int zeros = 0;
        foreach (char c in s) if (c == '0') zeros++;

        if (n % 2 == 0) {
            if (zeros != n / 2) return -1;

            int mism0 = 0; // pattern "0101..."
            int mism1 = 0; // pattern "1010..."

            for (int i = 0; i < n; i++) {
                char expected0 = (i % 2 == 0) ? '0' : '1';
                if (s[i] != expected0) mism0++;

                char expected1 = (i % 2 == 0) ? '1' : '0';
                if (s[i] != expected1) mism1++;
            }

            return Math.Min(mism0 / 2, mism1 / 2);
        } else {
            int ans = int.MaxValue;

            // pattern starting with '0'
            int zerosNeeded0 = (n + 1) / 2;
            if (zeros == zerosNeeded0) {
                int mism = 0;
                for (int i = 0; i < n; i++) {
                    char expected = (i % 2 == 0) ? '0' : '1';
                    if (s[i] != expected) mism++;
                }
                ans = Math.Min(ans, mism / 2);
            }

            // pattern starting with '1'
            int zerosNeeded1 = n / 2;
            if (zeros == zerosNeeded1) {
                int mism = 0;
                for (int i = 0; i < n; i++) {
                    char expected = (i % 2 == 0) ? '1' : '0';
                    if (s[i] != expected) mism++;
                }
                ans = Math.Min(ans, mism / 2);
            }

            return ans == int.MaxValue ? -1 : ans;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {
    const n = s.length;
    let cnt0 = 0;
    for (const ch of s) if (ch === '0') cnt0++;
    const cnt1 = n - cnt0;

    let ans = Infinity;

    // Pattern starting with '0' -> "0101..."
    const need0_start0 = Math.ceil(n / 2);
    const need1_start0 = Math.floor(n / 2);
    if (cnt0 === need0_start0 && cnt1 === need1_start0) {
        let mismatches = 0;
        for (let i = 0; i < n; ++i) {
            const expected = (i % 2 === 0) ? '0' : '1';
            if (s[i] !== expected) mismatches++;
        }
        ans = Math.min(ans, mismatches / 2);
    }

    // Pattern starting with '1' -> "1010..."
    const need0_start1 = Math.floor(n / 2);
    const need1_start1 = Math.ceil(n / 2);
    if (cnt0 === need0_start1 && cnt1 === need1_start1) {
        let mismatches = 0;
        for (let i = 0; i < n; ++i) {
            const expected = (i % 2 === 0) ? '1' : '0';
            if (s[i] !== expected) mismatches++;
        }
        ans = Math.min(ans, mismatches / 2);
    }

    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minSwaps(s: string): number {
    const n = s.length;
    let best = Number.MAX_SAFE_INTEGER;

    // Pattern starting with '0' : 0101...
    let zeroMis = 0, oneMis = 0;
    for (let i = 0; i < n; i++) {
        const expected = (i % 2 === 0) ? '0' : '1';
        if (s[i] !== expected) {
            if (s[i] === '0') zeroMis++;
            else oneMis++;
        }
    }
    if (zeroMis === oneMis) best = Math.min(best, zeroMis);

    // Pattern starting with '1' : 1010...
    zeroMis = 0;
    oneMis = 0;
    for (let i = 0; i < n; i++) {
        const expected = (i % 2 === 0) ? '1' : '0';
        if (s[i] !== expected) {
            if (s[i] === '0') zeroMis++;
            else oneMis++;
        }
    }
    if (zeroMis === oneMis) best = Math.min(best, zeroMis);

    return best === Number.MAX_SAFE_INTEGER ? -1 : best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minSwaps($s) {
        $n = strlen($s);
        $cnt0 = substr_count($s, '0');
        $ans = PHP_INT_MAX;

        // Pattern starting with '0' -> zeros needed = ceil(n/2)
        $needZeroStart0 = intdiv($n + 1, 2);
        if ($cnt0 == $needZeroStart0) {
            $mis01 = 0; // s[i]=='0' but should be '1'
            $mis10 = 0; // s[i]=='1' but should be '0'
            for ($i = 0; $i < $n; $i++) {
                $expected = ($i % 2 == 0) ? '0' : '1';
                if ($s[$i] !== $expected) {
                    if ($s[$i] === '0') {
                        $mis01++;
                    } else {
                        $mis10++;
                    }
                }
            }
            // swaps needed equals number of mismatched zeros (or ones)
            $ans = min($ans, $mis01);
        }

        // Pattern starting with '1' -> zeros needed = floor(n/2)
        $needZeroStart1 = intdiv($n, 2);
        if ($cnt0 == $needZeroStart1) {
            $mis01 = 0;
            $mis10 = 0;
            for ($i = 0; $i < $n; $i++) {
                $expected = ($i % 2 == 0) ? '1' : '0';
                if ($s[$i] !== $expected) {
                    if ($s[$i] === '0') {
                        $mis01++;
                    } else {
                        $mis10++;
                    }
                }
            }
            $ans = min($ans, $mis01);
        }

        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ s: String) -> Int {
        let chars = Array(s)
        var mismatch01_0 = 0   // expected '1', got '0' (pattern starts with '0')
        var mismatch10_0 = 0   // expected '0', got '1'
        var mismatch01_1 = 0   // expected '1', got '0' (pattern starts with '1')
        var mismatch10_1 = 0   // expected '0', got '1'
        
        for i in 0..<chars.count {
            let c = chars[i]
            
            // Pattern "0101..."
            let exp0: Character = (i % 2 == 0) ? "0" : "1"
            if c != exp0 {
                if c == "0" {
                    mismatch01_0 += 1
                } else {
                    mismatch10_0 += 1
                }
            }
            
            // Pattern "1010..."
            let exp1: Character = (i % 2 == 0) ? "1" : "0"
            if c != exp1 {
                if c == "0" {
                    mismatch01_1 += 1
                } else {
                    mismatch10_1 += 1
                }
            }
        }
        
        var ans = Int.max
        if mismatch01_0 == mismatch10_0 {
            ans = min(ans, mismatch01_0)
        }
        if mismatch01_1 == mismatch10_1 {
            ans = min(ans, mismatch01_1)
        }
        return ans == Int.max ? -1 : ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(s: String): Int {
        val n = s.length
        var zeroCount = 0
        for (c in s) if (c == '0') zeroCount++

        var answer = Int.MAX_VALUE

        // Pattern starting with '0' -> expected zeros = ceil(n/2)
        val zerosPattern0 = (n + 1) / 2
        if (zeroCount == zerosPattern0) {
            var mismatches = 0
            for (i in 0 until n) {
                val expected = if (i % 2 == 0) '0' else '1'
                if (s[i] != expected) mismatches++
            }
            answer = minOf(answer, mismatches / 2)
        }

        // Pattern starting with '1' -> expected zeros = floor(n/2)
        val zerosPattern1 = n / 2
        if (zeroCount == zerosPattern1) {
            var mismatches = 0
            for (i in 0 until n) {
                val expected = if (i % 2 == 0) '1' else '0'
                if (s[i] != expected) mismatches++
            }
            answer = minOf(answer, mismatches / 2)
        }

        return if (answer == Int.MAX_VALUE) -1 else answer
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(String s) {
    int n = s.length;
    int zeroCount = 0;
    for (int i = 0; i < n; i++) {
      if (s.codeUnitAt(i) == 48) zeroCount++; // '0'
    }
    int oneCount = n - zeroCount;
    const int INF = 1 << 30;
    int ans = INF;

    for (String start in ['0', '1']) {
      int reqZero, reqOne;
      if (n % 2 == 0) {
        reqZero = n ~/ 2;
        reqOne = n ~/ 2;
      } else {
        if (start == '0') {
          reqZero = n ~/ 2 + 1;
          reqOne = n - reqZero;
        } else {
          reqOne = n ~/ 2 + 1;
          reqZero = n - reqOne;
        }
      }

      if (zeroCount != reqZero || oneCount != reqOne) continue;

      int cnt0 = 0, cnt1 = 0; // cnt0: have '0' need '1', cnt1: have '1' need '0'
      for (int i = 0; i < n; i++) {
        bool expectZero = ((i % 2) == 0) ? (start == '0') : (start != '0');
        int ch = s.codeUnitAt(i);
        if (expectZero) {
          if (ch != 48) cnt1++; // have '1', need '0'
        } else {
          if (ch != 49) cnt0++; // have '0', need '1'
        }
      }

      int swaps = cnt0 > cnt1 ? cnt0 : cnt1;
      if (swaps < ans) ans = swaps;
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minSwaps(s string) int {
	n := len(s)
	zeroCnt := 0
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			zeroCnt++
		}
	}

	calc := func(start byte) (int, bool) {
		cnt01, cnt10 := 0, 0 // 0->1 mismatches and 1->0 mismatches
		exp := start
		for i := 0; i < n; i++ {
			if s[i] != exp {
				if s[i] == '0' {
					cnt01++
				} else {
					cnt10++
				}
			}
			// flip expected for next position
			if exp == '0' {
				exp = '1'
			} else {
				exp = '0'
			}
		}
		if cnt01 != cnt10 {
			return 0, false
		}
		return cnt01, true
	}

	ans := -1
	if swaps, ok := calc('0'); ok && (ans == -1 || swaps < ans) {
		ans = swaps
	}
	if swaps, ok := calc('1'); ok && (ans == -1 || swaps < ans) {
		ans = swaps
	}
	return ans
}
```

## Ruby

```ruby
def min_swaps(s)
  mis0_start0 = 0
  mis1_start0 = 0
  mis0_start1 = 0
  mis1_start1 = 0

  s.each_char.with_index do |ch, i|
    if i.even?
      # pattern starting with '0' expects '0', pattern starting with '1' expects '1'
      mis1_start0 += 1 if ch == '1'   # should be 0 but is 1
      mis0_start1 += 1 if ch == '0'   # should be 1 but is 0
    else
      # pattern starting with '0' expects '1', pattern starting with '1' expects '0'
      mis0_start0 += 1 if ch == '0'   # should be 1 but is 0
      mis1_start1 += 1 if ch == '1'   # should be 0 but is 1
    end
  end

  ans = Float::INFINITY
  ans = [ans, mis0_start0].min if mis0_start0 == mis1_start0
  ans = [ans, mis0_start1].min if mis0_start1 == mis1_start1

  ans == Float::INFINITY ? -1 : ans
end
```

## Scala

```scala
object Solution {
    def minSwaps(s: String): Int = {
        val n = s.length
        val zeroCnt = s.count(_ == '0')
        var ans = Int.MaxValue

        // Pattern starting with '0'
        val expectedZeros0 = (n + 1) / 2
        if (zeroCnt == expectedZeros0) {
            var misZero = 0
            var misOne = 0
            for (i <- 0 until n) {
                val expected = if ((i & 1) == 0) '0' else '1'
                if (s(i) != expected) {
                    if (s(i) == '0') misZero += 1 else misOne += 1
                }
            }
            ans = math.min(ans, Math.max(misZero, misOne))
        }

        // Pattern starting with '1'
        val expectedZeros1 = n / 2
        if (zeroCnt == expectedZeros1) {
            var misZero = 0
            var misOne = 0
            for (i <- 0 until n) {
                val expected = if ((i & 1) == 0) '1' else '0'
                if (s(i) != expected) {
                    if (s(i) == '0') misZero += 1 else misOne += 1
                }
            }
            ans = math.min(ans, Math.max(misZero, misOne))
        }

        if (ans == Int.MaxValue) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let cnt0 = bytes.iter().filter(|&&c| c == b'0').count();

        let mut ans = usize::MAX;

        // Pattern starting with '0'
        let required_zeros_start0 = (n + 1) / 2;
        if cnt0 == required_zeros_start0 {
            let mut cnt01 = 0; // zeros that should be ones
            for i in 0..n {
                let expected = if i % 2 == 0 { b'0' } else { b'1' };
                if bytes[i] != expected && bytes[i] == b'0' {
                    cnt01 += 1;
                }
            }
            ans = ans.min(cnt01);
        }

        // Pattern starting with '1'
        let required_zeros_start1 = n / 2;
        if cnt0 == required_zeros_start1 {
            let mut cnt01 = 0; // zeros that should be ones
            for i in 0..n {
                let expected = if i % 2 == 0 { b'1' } else { b'0' };
                if bytes[i] != expected && bytes[i] == b'0' {
                    cnt01 += 1;
                }
            }
            ans = ans.min(cnt01);
        }

        if ans == usize::MAX {
            -1
        } else {
            ans as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-swaps s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         ;; count total zeros in the string
         (total-zeros
          (let loop ((i 0) (cnt 0))
            (if (= i n)
                cnt
                (loop (+ i 1)
                      (if (char=? (string-ref s i) #\0)
                          (+ cnt 1)
                          cnt)))))
         ;; helper to compute swaps for a given starting character
         (calc-swaps
          (lambda (start-char)
            (let* ((required-zeros
                    (if (char=? start-char #\0)
                        (quotient (+ n 1) 2)   ; positions 0,2,... need zeros
                        (quotient n 2)))       ; positions 1,3,... need zeros
              (if (not (= total-zeros required-zeros))
                  #f
                  (let loop ((i 0) (mis01 0) (mis10 0))
                    (if (= i n)
                        (if (= mis01 mis10) mis01 #f) ; should be equal when possible
                        (let* ((expected
                                (if (even? i)
                                    start-char
                                    (if (char=? start-char #\0) #\1 #\0)))
                               (actual (string-ref s i)))
                          (cond [(and (char=? expected #\0) (char=? actual #\1))
                                 (loop (+ i 1) (+ mis01 1) mis10)]
                                [(and (char=? expected #\1) (char=? actual #\0))
                                 (loop (+ i 1) mis01 (+ mis10 1))]
                                [else
                                 (loop (+ i 1) mis01 mis10)])))))))))
         (swaps-start-0 (calc-swaps #\0))
         (swaps-start-1 (calc-swaps #\1)))
    (cond [(and swaps-start-0 swaps-start-1)
           (min swaps-start-0 swaps-start-1)]
          [swaps-start-0 swaps-start-0]
          [swaps-start-1 swaps-start-1]
          [else -1])))
```

## Erlang

```erlang
-spec min_swaps(S :: unicode:unicode_binary()) -> integer().
min_swaps(S) ->
    List = binary_to_list(S),
    N = length(List),
    ZeroCount = count_zeros(List),
    Starts = [$0, $1],
    Result = lists:foldl(fun(Start, Acc) ->
        ExpectedZeros = expected_zeros(N, Start),
        if
            ZeroCount =/= ExpectedZeros -> Acc;
            true ->
                {C01, C10} = calc_swaps(List, Start, 0, 0, 0),
                Swaps = max(C01, C10),
                case Acc of
                    -1 -> Swaps;
                    _ when Swaps < Acc -> Swaps;
                    _ -> Acc
                end
        end
    end, -1, Starts),
    Result.

count_zeros(List) ->
    lists:foldl(fun(C, Acc) -> if C == $0 -> Acc + 1; true -> Acc end end, 0, List).

expected_zeros(N, $0) ->
    case N rem 2 of
        0 -> N div 2;
        _ -> (N + 1) div 2
    end;
expected_zeros(N, $1) ->
    case N rem 2 of
        0 -> N div 2;
        _ -> (N - 1) div 2
    end.

calc_swaps([], _Start, _Idx, C01, C10) ->
    {C01, C10};
calc_swaps([H|T], Start, Idx, C01, C10) ->
    Expected = case Idx rem 2 of
        0 -> Start;
        1 -> opposite(Start)
    end,
    NewC01 = if H == $0 andalso Expected == $1 -> C01 + 1; true -> C01 end,
    NewC10 = if H == $1 andalso Expected == $0 -> C10 + 1; true -> C10 end,
    calc_swaps(T, Start, Idx + 1, NewC01, NewC10).

opposite($0) -> $1;
opposite($1) -> $0.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(s :: String.t()) :: integer
  def min_swaps(s) do
    n = String.length(s)

    zeros =
      s
      |> String.graphemes()
      |> Enum.count(&(&1 == "0"))

    {mismatch0, mismatch1} =
      s
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({0, 0}, fn {ch, idx}, {c0, c1} ->
        expected0 = if rem(idx, 2) == 0, do: "0", else: "1"
        expected1 = if rem(idx, 2) == 0, do: "1", else: "0"

        c0 = if ch != expected0, do: c0 + 1, else: c0
        c1 = if ch != expected1, do: c1 + 1, else: c1

        {c0, c1}
      end)

    cond do
      rem(n, 2) == 0 ->
        # even length: both patterns need n/2 zeros and ones
        if zeros != div(n, 2), do: -1,
          else: min(div(mismatch0, 2), div(mismatch1, 2))

      true ->
        half = div(n, 2)

        cond do
          zeros == half + 1 -> div(mismatch0, 2)   # pattern starting with '0' possible
          zeros == half     -> div(mismatch1, 2)   # pattern starting with '1' possible
          true              -> -1
        end
    end
  end
end
```
