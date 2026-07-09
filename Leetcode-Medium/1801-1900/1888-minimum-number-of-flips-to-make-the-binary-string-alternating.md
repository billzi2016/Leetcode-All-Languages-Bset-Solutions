# 1888. Minimum Number of Flips to Make the Binary String Alternating

## Cpp

```cpp
class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        string t = s + s;
        int m = 2 * n;
        vector<int> diff0(m), diff1(m);
        for (int i = 0; i < m; ++i) {
            char exp0 = (i % 2 == 0) ? '0' : '1';
            char exp1 = (i % 2 == 0) ? '1' : '0';
            diff0[i] = (t[i] != exp0);
            diff1[i] = (t[i] != exp1);
        }
        int ans = n; // maximum possible flips
        int sum0 = 0, sum1 = 0;
        for (int i = 0; i < m; ++i) {
            sum0 += diff0[i];
            sum1 += diff1[i];
            if (i >= n) {
                sum0 -= diff0[i - n];
                sum1 -= diff1[i - n];
            }
            if (i >= n - 1) {
                ans = min(ans, min(sum0, sum1));
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minFlips(String s) {
        int n = s.length();
        String t = s + s;
        int m = t.length(); // 2 * n
        int[] diff0 = new int[m];
        int[] diff1 = new int[m];
        for (int i = 0; i < m; i++) {
            char c = t.charAt(i);
            char exp0 = (i % 2 == 0) ? '0' : '1';
            char exp1 = (i % 2 == 0) ? '1' : '0';
            diff0[i] = (c != exp0) ? 1 : 0;
            diff1[i] = (c != exp1) ? 1 : 0;
        }
        int ans = Integer.MAX_VALUE;
        int sum0 = 0, sum1 = 0;
        for (int i = 0; i < m; i++) {
            sum0 += diff0[i];
            sum1 += diff1[i];
            if (i >= n) {
                sum0 -= diff0[i - n];
                sum1 -= diff1[i - n];
            }
            if (i >= n - 1) {
                ans = Math.min(ans, Math.min(sum0, sum1));
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ss = s + s  # duplicate for cyclic shifts
        
        # patterns for alternating strings starting with '0' and '1'
        pat0 = ['0' if i % 2 == 0 else '1' for i in range(2 * n)]
        pat1 = ['1' if i % 2 == 0 else '0' for i in range(2 * n)]
        
        # mismatches with each pattern
        diff0 = [0] * (2 * n)
        diff1 = [0] * (2 * n)
        for i, ch in enumerate(ss):
            if ch != pat0[i]:
                diff0[i] = 1
            if ch != pat1[i]:
                diff1[i] = 1
        
        # sliding window to find minimal mismatches over all rotations
        cur0 = sum(diff0[:n])
        cur1 = sum(diff1[:n])
        best0, best1 = cur0, cur1
        
        for i in range(1, n):
            cur0 += diff0[i + n - 1] - diff0[i - 1]
            cur1 += diff1[i + n - 1] - diff1[i - 1]
            if cur0 < best0:
                best0 = cur0
            if cur1 < best1:
                best1 = cur1
        
        return min(best0, best1)
```

## Python3

```python
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        m0 = [0] * (2 * n)
        m1 = [0] * (2 * n)
        for i, ch in enumerate(ss):
            # pattern starting with '0'
            if (i & 1) == 0:
                expected0 = '0'
                expected1 = '1'
            else:
                expected0 = '1'
                expected1 = '0'
            m0[i] = ch != expected0
            m1[i] = ch != expected1

        cur0 = sum(m0[:n])
        cur1 = sum(m1[:n])
        ans = min(cur0, cur1)

        for i in range(n, 2 * n):
            cur0 += m0[i] - m0[i - n]
            cur1 += m1[i] - m1[i - n]
            if cur0 < ans:
                ans = cur0
            if cur1 < ans:
                ans = cur1

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int minFlips(char* s) {
    int n = 0;
    while (s[n]) ++n;
    if (n <= 1) return 0;

    int len2 = 2 * n;
    char *t = (char *)malloc(len2 + 1);
    for (int i = 0; i < n; ++i) t[i] = s[i];
    for (int i = 0; i < n; ++i) t[n + i] = s[i];
    t[len2] = '\0';

    int cnt0 = 0, cnt1 = 0;
    for (int i = 0; i < n; ++i) {
        char exp0 = (i % 2 == 0) ? '0' : '1';
        if (t[i] != exp0) ++cnt0;
        char exp1 = (i % 2 == 0) ? '1' : '0';
        if (t[i] != exp1) ++cnt1;
    }
    int ans = cnt0 < cnt1 ? cnt0 : cnt1;

    for (int i = n; i < len2; ++i) {
        int outIdx = i - n;
        char exp0_out = (outIdx % 2 == 0) ? '0' : '1';
        if (t[outIdx] != exp0_out) --cnt0;
        char exp1_out = (outIdx % 2 == 0) ? '1' : '0';
        if (t[outIdx] != exp1_out) --cnt1;

        char exp0_in = (i % 2 == 0) ? '0' : '1';
        if (t[i] != exp0_in) ++cnt0;
        char exp1_in = (i % 2 == 0) ? '1' : '0';
        if (t[i] != exp1_in) ++cnt1;

        int cur = cnt0 < cnt1 ? cnt0 : cnt1;
        if (cur < ans) ans = cur;
    }

    free(t);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinFlips(string s) {
        int n = s.Length;
        string ss = s + s;
        int len = 2 * n;
        int[] diff0 = new int[len];
        int[] diff1 = new int[len];
        for (int i = 0; i < len; i++) {
            char expected0 = (i % 2 == 0) ? '0' : '1';
            char expected1 = (i % 2 == 0) ? '1' : '0';
            diff0[i] = ss[i] == expected0 ? 0 : 1;
            diff1[i] = ss[i] == expected1 ? 0 : 1;
        }

        int window0 = 0, window1 = 0;
        for (int i = 0; i < n; i++) {
            window0 += diff0[i];
            window1 += diff1[i];
        }
        int ans = Math.Min(window0, window1);

        for (int i = n; i < len; i++) {
            window0 += diff0[i] - diff0[i - n];
            window1 += diff1[i] - diff1[i - n];
            ans = Math.Min(ans, Math.Min(window0, window1));
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minFlips = function(s) {
    const n = s.length;
    const ss = s + s;
    const m = ss.length;
    const diff0 = new Array(m);
    const diff1 = new Array(m);
    
    for (let i = 0; i < m; ++i) {
        const ch = ss[i];
        // pattern starting with '0': 0101...
        const exp0 = (i % 2 === 0) ? '0' : '1';
        diff0[i] = ch === exp0 ? 0 : 1;
        // pattern starting with '1': 1010...
        const exp1 = (i % 2 === 0) ? '1' : '0';
        diff1[i] = ch === exp1 ? 0 : 1;
    }
    
    let sum0 = 0, sum1 = 0;
    let ans = n; // maximum possible flips
    
    for (let i = 0; i < m; ++i) {
        sum0 += diff0[i];
        sum1 += diff1[i];
        
        if (i >= n) {
            sum0 -= diff0[i - n];
            sum1 -= diff1[i - n];
        }
        if (i >= n - 1) {
            const cur = Math.min(sum0, sum1);
            if (cur < ans) ans = cur;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function minFlips(s: string): number {
    const n = s.length;
    const t = s + s;
    const m = t.length;

    const mismatch0: number[] = new Array(m);
    const mismatch1: number[] = new Array(m);

    for (let i = 0; i < m; ++i) {
        const ch = t.charAt(i);
        const exp0 = (i & 1) === 0 ? '0' : '1';
        const exp1 = (i & 1) === 0 ? '1' : '0';
        mismatch0[i] = ch === exp0 ? 0 : 1;
        mismatch1[i] = ch === exp1 ? 0 : 1;
    }

    let sum0 = 0, sum1 = 0;
    for (let i = 0; i < n; ++i) {
        sum0 += mismatch0[i];
        sum1 += mismatch1[i];
    }
    let ans = Math.min(sum0, sum1);

    for (let i = n; i < m; ++i) {
        sum0 += mismatch0[i] - mismatch0[i - n];
        sum1 += mismatch1[i] - mismatch1[i - n];
        const cur = Math.min(sum0, sum1);
        if (cur < ans) ans = cur;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minFlips($s) {
        $n = strlen($s);
        $cntStart0 = 0;
        $cntStart1 = 0;
        for ($i = 0; $i < $n; $i++) {
            // pattern starting with '0': 0101...
            $expected0 = ($i % 2 == 0) ? '0' : '1';
            if ($s[$i] !== $expected0) {
                $cntStart0++;
            }
            // pattern starting with '1': 1010...
            $expected1 = ($i % 2 == 0) ? '1' : '0';
            if ($s[$i] !== $expected1) {
                $cntStart1++;
            }
        }
        return min($cntStart0, $cntStart1);
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        
        // duplicate the string to handle circular rotations
        var extended = [Character]()
        extended.reserveCapacity(2 * n)
        extended.append(contentsOf: chars)
        extended.append(contentsOf: chars)
        
        let zero: Character = "0"
        let one: Character = "1"
        
        var mism0 = 0   // mismatches with pattern starting with '0' (global index parity)
        var mism1 = 0   // mismatches with pattern starting with '1'
        
        // initial window [0, n)
        for i in 0..<n {
            let c = extended[i]
            if c != ((i % 2 == 0) ? zero : one) { mism0 += 1 }
            if c != ((i % 2 == 0) ? one : zero) { mism1 += 1 }
        }
        
        var answer = min(mism0, mism1)
        
        // slide the window over the duplicated part
        for i in n..<2 * n {
            let outIdx = i - n
            let outChar = extended[outIdx]
            if outChar != ((outIdx % 2 == 0) ? zero : one) { mism0 -= 1 }
            if outChar != ((outIdx % 2 == 0) ? one : zero) { mism1 -= 1 }
            
            let inChar = extended[i]
            if inChar != ((i % 2 == 0) ? zero : one) { mism0 += 1 }
            if inChar != ((i % 2 == 0) ? one : zero) { mism1 += 1 }
            
            answer = min(answer, min(mism0, mism1))
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlips(s: String): Int {
        val n = s.length
        if (n == 0) return 0
        val t = s + s
        var sum0 = 0 // mismatches with pattern starting '0' at index 0 globally
        var sum1 = 0 // mismatches with pattern starting '1' at index 0 globally

        for (i in 0 until n) {
            val c = t[i]
            if ((i % 2 == 0 && c != '0') || (i % 2 == 1 && c != '1')) sum0++
            if ((i % 2 == 0 && c != '1') || (i % 2 == 1 && c != '0')) sum1++
        }

        var ans = kotlin.math.min(sum0, sum1)

        for (start in 1 until n) {
            val outIdx = start - 1
            val outChar = t[outIdx]
            if ((outIdx % 2 == 0 && outChar != '0') || (outIdx % 2 == 1 && outChar != '1')) sum0--
            if ((outIdx % 2 == 0 && outChar != '1') || (outIdx % 2 == 1 && outChar != '0')) sum1--

            val inIdx = start + n - 1
            val inChar = t[inIdx]
            if ((inIdx % 2 == 0 && inChar != '0') || (inIdx % 2 == 1 && inChar != '1')) sum0++
            if ((inIdx % 2 == 0 && inChar != '1') || (inIdx % 2 == 1 && inChar != '0')) sum1++

            ans = kotlin.math.min(ans, kotlin.math.min(sum0, sum1))
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minFlips(String s) {
    int n = s.length;
    // Duplicate the string virtually by using modulo indexing.
    List<int> mismatch0 = List.filled(2 * n, 0);
    List<int> mismatch1 = List.filled(2 * n, 0);

    for (int i = 0; i < 2 * n; ++i) {
      int idx = i % n;
      int ch = s.codeUnitAt(idx);
      int exp0 = (i & 1) == 0 ? 48 : 49; // pattern starting with '0'
      int exp1 = (i & 1) == 0 ? 49 : 48; // pattern starting with '1'
      mismatch0[i] = ch == exp0 ? 0 : 1;
      mismatch1[i] = ch == exp1 ? 0 : 1;
    }

    int sum0 = 0, sum1 = 0;
    for (int i = 0; i < n; ++i) {
      sum0 += mismatch0[i];
      sum1 += mismatch1[i];
    }
    int ans = sum0 < sum1 ? sum0 : sum1;

    for (int i = n; i < 2 * n; ++i) {
      sum0 += mismatch0[i] - mismatch0[i - n];
      sum1 += mismatch1[i] - mismatch1[i - n];
      int cur = sum0 < sum1 ? sum0 : sum1;
      if (cur < ans) ans = cur;
    }

    return ans;
  }
}
```

## Golang

```go
func minFlips(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	s2 := s + s
	m0 := make([]int, 2*n)
	m1 := make([]int, 2*n)

	for i := 0; i < 2*n; i++ {
		ch := s2[i]
		// pattern starting with '0'
		exp0 := byte('0')
		if i%2 == 1 {
			exp0 = '1'
		}
		if ch != exp0 {
			m0[i] = 1
		}
		// pattern starting with '1'
		exp1 := byte('1')
		if i%2 == 1 {
			exp1 = '0'
		}
		if ch != exp1 {
			m1[i] = 1
		}
	}

	sum0, sum1 := 0, 0
	for i := 0; i < n; i++ {
		sum0 += m0[i]
		sum1 += m1[i]
	}
	ans := sum0
	if sum1 < ans {
		ans = sum1
	}

	for start := 1; start < n; start++ {
		endIdx := start + n - 1
		sum0 = sum0 - m0[start-1] + m0[endIdx]
		sum1 = sum1 - m1[start-1] + m1[endIdx]
		if sum0 < ans {
			ans = sum0
		}
		if sum1 < ans {
			ans = sum1
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_flips(s)
  n = s.length
  return 0 if n <= 1

  ss = s + s
  mism0 = 0
  mism1 = 0
  ans = Float::INFINITY

  (0...(2 * n)).each do |i|
    c = ss[i]
    expected0 = (i.even?) ? '0' : '1'
    expected1 = (i.even?) ? '1' : '0'

    mism0 += 1 if c != expected0
    mism1 += 1 if c != expected1

    if i >= n
      left_c = ss[i - n]
      left_expected0 = ((i - n).even?) ? '0' : '1'
      left_expected1 = ((i - n).even?) ? '1' : '0'

      mism0 -= 1 if left_c != left_expected0
      mism1 -= 1 if left_c != left_expected1
    end

    if i >= n - 1
      ans = [ans, mism0, mism1].min
    end
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minFlips(s: String): Int = {
        val n = s.length
        if (n == 0) return 0
        val ss = s + s
        val diff0 = new Array[Int](2 * n)
        val diff1 = new Array[Int](2 * n)

        var i = 0
        while (i < 2 * n) {
            val c = ss.charAt(i)
            // pattern starting with '0'
            val expected0 = if ((i & 1) == 0) '0' else '1'
            diff0(i) = if (c != expected0) 1 else 0
            // pattern starting with '1'
            val expected1 = if ((i & 1) == 0) '1' else '0'
            diff1(i) = if (c != expected1) 1 else 0
            i += 1
        }

        var cur0 = 0
        var cur1 = 0
        i = 0
        while (i < n) {
            cur0 += diff0(i)
            cur1 += diff1(i)
            i += 1
        }
        var ans = Math.min(cur0, cur1)

        var start = 1
        while (start < n) {
            cur0 = cur0 - diff0(start - 1) + diff0(start + n - 1)
            cur1 = cur1 - diff1(start - 1) + diff1(start + n - 1)
            ans = Math.min(ans, Math.min(cur0, cur1))
            start += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let bytes = s.as_bytes();
        // duplicate the string to handle cyclic shifts
        let mut dup = Vec::with_capacity(2 * n);
        dup.extend_from_slice(bytes);
        dup.extend_from_slice(bytes);

        // mismatches with two alternating patterns: starting with '0' and with '1'
        let mut mis0 = vec![0i32; 2 * n];
        let mut mis1 = vec![0i32; 2 * n];
        for i in 0..2 * n {
            let expected0 = if i % 2 == 0 { b'0' } else { b'1' };
            let expected1 = if i % 2 == 0 { b'1' } else { b'0' };
            mis0[i] = (dup[i] != expected0) as i32;
            mis1[i] = (dup[i] != expected1) as i32;
        }

        // initial window of size n
        let mut sum0: i32 = mis0[0..n].iter().sum();
        let mut sum1: i32 = mis1[0..n].iter().sum();
        let mut ans = std::cmp::min(sum0, sum1);

        // slide the window over the duplicated array
        for i in n..2 * n {
            sum0 += mis0[i];
            sum1 += mis1[i];
            sum0 -= mis0[i - n];
            sum1 -= mis1[i - n];
            ans = std::cmp::min(ans, std::cmp::min(sum0, sum1));
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (min-flips s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (t (string-append s s))
         (len (* 2 n)))
    (if (= n 0)
        0
        (begin
          (define mism0 (make-vector len 0))
          (define mism1 (make-vector len 0))
          (for ([i (in-range len)])
            (let* ((c (string-ref t i))
                   (expected0 (if (even? i) #\0 #\1))
                   (expected1 (if (even? i) #\1 #\0)))
              (vector-set! mism0 i (if (char=? c expected0) 0 1))
              (vector-set! mism1 i (if (char=? c expected1) 0 1))))
          (define first-sum0
            (for/sum ([i (in-range n)]) (vector-ref mism0 i)))
          (define first-sum1
            (for/sum ([i (in-range n)]) (vector-ref mism1 i)))
          (let loop ((start 1)
                     (sum0 first-sum0)
                     (sum1 first-sum1)
                     (best (min first-sum0 first-sum1)))
            (if (= start n)
                best
                (let* ((out-idx (- start 1))
                       (in-idx (+ start n -1))
                       (new-sum0 (+ (- sum0 (vector-ref mism0 out-idx))
                                    (vector-ref mism0 in-idx)))
                       (new-sum1 (+ (- sum1 (vector-ref mism1 out-idx))
                                    (vector-ref mism1 in-idx)))
                       (cur (min new-sum0 new-sum1)))
                  (loop (+ start 1) new-sum0 new-sum1
                        (if (< cur best) cur best)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_flips/1]).

-spec min_flips(S :: unicode:unicode_binary()) -> integer().
min_flips(S) ->
    SList = binary_to_list(S),
    N = length(SList),
    DoubleList = SList ++ SList,
    M0Rev = build_mismatch(DoubleList, 0, []),
    M0 = lists:reverse(M0Rev),
    PrefixTuple = list_to_tuple(build_prefix(M0)),
    MaxAns = N,
    Range = lists:seq(0, N - 1),
    lists:foldl(
        fun(L, Acc) ->
            Sum0 = element(L + N + 1, PrefixTuple) - element(L + 1, PrefixTuple),
            FlipsStart0 = if (L rem 2) == 0 -> Sum0; true -> N - Sum0 end,
            FlipsStart1 = N - FlipsStart0,
            WindowMin = if FlipsStart0 < FlipsStart1 -> FlipsStart0; true -> FlipsStart1 end,
            case WindowMin < Acc of
                true -> WindowMin;
                false -> Acc
            end
        end,
        MaxAns,
        Range).

% Build mismatch list (0/1) assuming global pattern starts with '0'.
build_mismatch([], _Idx, Acc) ->
    Acc;
build_mismatch([Char | Rest], Idx, Acc) ->
    Expected = if (Idx rem 2) == 0 -> $0; true -> $1 end,
    Mismatch = if Char =:= Expected -> 0; true -> 1 end,
    build_mismatch(Rest, Idx + 1, [Mismatch | Acc]).

% Build prefix sums list from mismatch list.
build_prefix(MList) ->
    build_prefix(MList, 0, [0]).
build_prefix([], _Sum, Acc) ->
    lists:reverse(Acc);
build_prefix([M | Rest], Sum, Acc) ->
    NewSum = Sum + M,
    build_prefix(Rest, NewSum, [NewSum | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_flips(s :: String.t()) :: integer()
  def min_flips(s) do
    chars = String.to_charlist(s)
    n = length(chars)

    double = chars ++ chars

    {diff0_list, diff1_list} =
      Enum.with_index(double)
      |> Enum.reduce({[], []}, fn {ch, idx}, {acc0, acc1} ->
        exp0 = if rem(idx, 2) == 0, do: ?0, else: ?1
        exp1 = if rem(idx, 2) == 0, do: ?1, else: ?0

        d0 = if ch != exp0, do: 1, else: 0
        d1 = if ch != exp1, do: 1, else: 0

        {[d0 | acc0], [d1 | acc1]}
      end)

    diff0 = List.to_tuple(Enum.reverse(diff0_list))
    diff1 = List.to_tuple(Enum.reverse(diff1_list))

    sum0 = init_sum(diff0, n)
    sum1 = init_sum(diff1, n)

    initial_min = min(sum0, sum1)

    {_final_s0, _final_s1, answer} =
      1..(n - 1)
      |> Enum.reduce({sum0, sum1, initial_min}, fn start, {s0, s1, cur_min} ->
        out_idx = start - 1
        in_idx = start + n - 1

        ns0 = s0 - elem(diff0, out_idx) + elem(diff0, in_idx)
        ns1 = s1 - elem(diff1, out_idx) + elem(diff1, in_idx)

        new_min = min(cur_min, min(ns0, ns1))
        {ns0, ns1, new_min}
      end)

    answer
  end

  defp init_sum(tuple, n) do
    0..(n - 1)
    |> Enum.reduce(0, fn i, acc -> acc + elem(tuple, i) end)
  end
end
```
