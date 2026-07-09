# 0828. Count Unique Characters of All Substrings of a Given String

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniqueLetterString(string s) {
        int n = s.size();
        vector<int> prev(n), nxt(n);
        vector<int> last(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'A';
            prev[i] = last[c];
            last[c] = i;
        }
        fill(last.begin(), last.end(), n);
        for (int i = n - 1; i >= 0; --i) {
            int c = s[i] - 'A';
            nxt[i] = last[c];
            last[c] = i;
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long left = i - prev[i];
            long long right = nxt[i] - i;
            ans += left * right;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int uniqueLetterString(String s) {
        int n = s.length();
        int[] last = new int[26];
        int[] prev = new int[26];
        Arrays.fill(last, -1);
        Arrays.fill(prev, -1);
        long result = 0;
        for (int i = 0; i < n; ++i) {
            int idx = s.charAt(i) - 'A';
            if (last[idx] != -1) {
                result += (long)(last[idx] - prev[idx]) * (i - last[idx]);
            }
            prev[idx] = last[idx];
            last[idx] = i;
        }
        for (int idx = 0; idx < 26; ++idx) {
            if (last[idx] != -1) {
                result += (long)(last[idx] - prev[idx]) * (n - last[idx]);
            }
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # positions for each uppercase letter
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - 65].append(i)

        total = 0
        for lst in pos:
            if not lst:
                continue
            prev = -1
            for j, idx in enumerate(lst):
                next_idx = lst[j + 1] if j + 1 < len(lst) else n
                total += (idx - prev) * (next_idx - idx)
                prev = idx
        return total
```

## Python3

```python
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        from collections import defaultdict
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            pos[ch].append(i)

        n = len(s)
        ans = 0
        for lst in pos.values():
            lst = [-1] + lst + [n]
            for k in range(1, len(lst) - 1):
                ans += (lst[k] - lst[k - 1]) * (lst[k + 1] - lst[k])
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int uniqueLetterString(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return 0;
    
    int *prev = (int*)malloc(n * sizeof(int));
    int *next = (int*)malloc(n * sizeof(int));
    
    int last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;
    for (int i = 0; i < n; ++i) {
        int c = s[i] - 'A';
        prev[i] = last[c];
        last[c] = i;
    }
    
    int nxt[26];
    for (int i = 0; i < 26; ++i) nxt[i] = n;
    for (int i = n - 1; i >= 0; --i) {
        int c = s[i] - 'A';
        next[i] = nxt[c];
        nxt[c] = i;
    }
    
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long left = i - prev[i];
        long long right = next[i] - i;
        ans += left * right;
    }
    
    free(prev);
    free(next);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int UniqueLetterString(string s) {
        int n = s.Length;
        int[] prev = new int[n];
        int[] next = new int[n];
        int[] lastPos = new int[26];
        for (int i = 0; i < 26; i++) lastPos[i] = -1;
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'A';
            prev[i] = lastPos[c];
            lastPos[c] = i;
        }
        for (int i = 0; i < 26; i++) lastPos[i] = n;
        for (int i = n - 1; i >= 0; i--) {
            int c = s[i] - 'A';
            next[i] = lastPos[c];
            lastPos[c] = i;
        }
        long result = 0;
        for (int i = 0; i < n; i++) {
            long left = i - prev[i];
            long right = next[i] - i;
            result += left * right;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var uniqueLetterString = function(s) {
    const n = s.length;
    const positions = Array.from({ length: 26 }, () => [-1]); // sentinel start
    
    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 65; // 'A' -> 0
        positions[idx].push(i);
    }
    
    let result = 0;
    for (const arr of positions) {
        arr.push(n); // sentinel end
        for (let j = 1; j < arr.length - 1; j++) {
            const prev = arr[j - 1];
            const cur = arr[j];
            const next = arr[j + 1];
            result += (cur - prev) * (next - cur);
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function uniqueLetterString(s: string): number {
    const n = s.length;
    const prev = new Array<number>(n);
    const next = new Array<number>(n);
    const lastPos = new Array<number>(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 65;
        prev[i] = lastPos[idx];
        lastPos[idx] = i;
    }
    const nextPos = new Array<number>(26).fill(n);
    for (let i = n - 1; i >= 0; i--) {
        const idx = s.charCodeAt(i) - 65;
        next[i] = nextPos[idx];
        nextPos[idx] = i;
    }
    let result = 0;
    for (let i = 0; i < n; i++) {
        const left = i - prev[i];
        const right = next[i] - i;
        result += left * right;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function uniqueLetterString($s) {
        $n = strlen($s);
        // positions for each uppercase letter
        $pos = array_fill(0, 26, []);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 65; // 'A' ASCII is 65
            $pos[$idx][] = $i;
        }

        $total = 0;
        for ($c = 0; $c < 26; $c++) {
            if (empty($pos[$c])) continue;

            // add sentinel values at both ends
            array_unshift($pos[$c], -1);
            $pos[$c][] = $n;

            $len = count($pos[$c]);
            for ($j = 1; $j < $len - 1; $j++) {
                $prev = $pos[$c][$j - 1];
                $curr = $pos[$c][$j];
                $next = $pos[$c][$j + 1];
                $total += ($curr - $prev) * ($next - $curr);
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func uniqueLetterString(_ s: String) -> Int {
        let n = s.count
        var positions = [[Int]](repeating: [], count: 26)
        var idx = 0
        for scalar in s.unicodeScalars {
            let charIndex = Int(scalar.value - UnicodeScalar("A").value)
            positions[charIndex].append(idx)
            idx += 1
        }
        var result = 0
        for list in positions {
            let m = list.count
            if m == 0 { continue }
            for i in 0..<m {
                let cur = list[i]
                let prev = i > 0 ? list[i - 1] : -1
                let next = i + 1 < m ? list[i + 1] : n
                result += (cur - prev) * (next - cur)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniqueLetterString(s: String): Int {
        val n = s.length
        val prev = IntArray(n)
        val next = IntArray(n) { n }
        val lastPosPrev = IntArray(26) { -1 }
        for (i in 0 until n) {
            val idx = s[i] - 'A'
            prev[i] = lastPosPrev[idx]
            lastPosPrev[idx] = i
        }
        val lastPosNext = IntArray(26) { n }
        for (i in n - 1 downTo 0) {
            val idx = s[i] - 'A'
            next[i] = lastPosNext[idx]
            lastPosNext[idx] = i
        }
        var result = 0L
        for (i in 0 until n) {
            val left = i - prev[i]
            val right = next[i] - i
            result += left.toLong() * right.toLong()
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int uniqueLetterString(String s) {
    int n = s.length;
    List<List<int>> positions = List.generate(26, (_) => []);
    for (int i = 0; i < n; i++) {
      int idx = s.codeUnitAt(i) - 65; // 'A' ASCII code is 65
      positions[idx].add(i);
    }
    int result = 0;
    for (var list in positions) {
      if (list.isEmpty) continue;
      for (int k = 0; k < list.length; k++) {
        int prev = k == 0 ? -1 : list[k - 1];
        int next = k == list.length - 1 ? n : list[k + 1];
        result += (list[k] - prev) * (next - list[k]);
      }
    }
    return result;
  }
}
```

## Golang

```go
func uniqueLetterString(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	prev := make([]int, n)
	lastPos := [26]int{}
	for i := 0; i < 26; i++ {
		lastPos[i] = -1
	}
	for i := 0; i < n; i++ {
		c := s[i] - 'A'
		prev[i] = lastPos[c]
		lastPos[c] = i
	}

	next := make([]int, n)
	nextPos := [26]int{}
	for i := 0; i < 26; i++ {
		nextPos[i] = n
	}
	for i := n - 1; i >= 0; i-- {
		c := s[i] - 'A'
		next[i] = nextPos[c]
		nextPos[c] = i
	}

	var ans int64
	for i := 0; i < n; i++ {
		left := i - prev[i]
		right := next[i] - i
		ans += int64(left * right)
	}
	return int(ans)
}
```

## Ruby

```ruby
def unique_letter_string(s)
  n = s.length
  positions = Hash.new { |h, k| h[k] = [] }
  s.each_char.with_index { |ch, i| positions[ch] << i }

  total = 0
  positions.each_value do |arr|
    arr.unshift(-1)
    arr.push(n)
    (1...arr.length - 1).each do |i|
      left = arr[i] - arr[i - 1]
      right = arr[i + 1] - arr[i]
      total += left * right
    end
  end

  total
end
```

## Scala

```scala
object Solution {
  def uniqueLetterString(s: String): Int = {
    val n = s.length
    val last = Array.fill(26)(-1)
    val prev = Array.fill(26)(-1)
    var result: Long = 0L

    for (i <- 0 until n) {
      val idx = s.charAt(i) - 'A'
      if (last(idx) != -1) {
        result += (last(idx) - prev(idx)).toLong * (i - last(idx))
      }
      prev(idx) = last(idx)
      last(idx) = i
    }

    for (idx <- 0 until 26) {
      if (last(idx) != -1) {
        result += (last(idx) - prev(idx)).toLong * (n - last(idx))
      }
    }

    result.toInt
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn unique_letter_string(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut prev = vec![-1i32; n];
        let mut next = vec![n as i32; n];

        // previous occurrence
        let mut last: HashMap<u8, i32> = HashMap::new();
        for i in 0..n {
            let c = bytes[i];
            if let Some(&p) = last.get(&c) {
                prev[i] = p;
            }
            last.insert(c, i as i32);
        }

        // next occurrence
        last.clear();
        for i_rev in (0..n).rev() {
            let c = bytes[i_rev];
            if let Some(&p) = last.get(&c) {
                next[i_rev] = p;
            }
            last.insert(c, i_rev as i32);
        }

        let mut total: i64 = 0;
        for i in 0..n {
            let left = (i as i32 - prev[i]) as i64;
            let right = (next[i] - i as i32) as i64;
            total += left * right;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (unique-letter-string s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [prev (make-vector n -1)]
         [next (make-vector n n)])
    ;; previous occurrence
    (let ([last (make-vector 26 -1)])
      (for ([i (in-range n)])
        (let* ([ch (string-ref s i)]
               [idx (- (char->integer ch) (char->integer #\A))])
          (vector-set! prev i (vector-ref last idx))
          (vector-set! last idx i))))
    ;; next occurrence
    (let ([last (make-vector 26 n)])
      (for ([i (in-range (sub1 n) -1 -1)])
        (let* ([ch (string-ref s i)]
               [idx (- (char->integer ch) (char->integer #\A))])
          (vector-set! next i (vector-ref last idx))
          (vector-set! last idx i))))
    ;; sum contributions
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (let* ([left (- i (vector-ref prev i))]
                 [right (- (vector-ref next i) i)]
                 [contrib (* left right)])
            (loop (add1 i) (+ total contrib)))))))
```

## Erlang

```erlang
-spec unique_letter_string(S :: unicode:unicode_binary()) -> integer().
unique_letter_string(S) ->
    Bytes = binary_to_list(S),
    N = length(Bytes),
    CharMap = build_map(Bytes, 0, #{}),
    maps:fold(
        fun(_Char, PosRev, Acc) ->
            Acc + calc_contrib(PosRev, N)
        end,
        0,
        CharMap
    ).

%% Build a map from character code to list of positions (in reverse order).
-spec build_map([integer()], integer(), map()) -> map().
build_map([], _Idx, Map) ->
    Map;
build_map([C | Rest], Idx, Map) ->
    UpdatedMap =
        case maps:find(C, Map) of
            {ok, L} -> maps:put(C, [Idx | L], Map);
            error   -> maps:put(C, [Idx], Map)
        end,
    build_map(Rest, Idx + 1, UpdatedMap).

%% Calculate contribution for a character given its reversed position list.
-spec calc_contrib([integer()], integer()) -> integer().
calc_contrib(PosRev, N) ->
    Pos = lists:reverse(PosRev),
    calc_contrib(Pos, N, -1, 0).

-spec calc_contrib([integer()], integer(), integer(), integer()) -> integer().
calc_contrib([], _N, _Prev, Acc) ->
    Acc;
calc_contrib([Cur | Rest], N, Prev, Acc) ->
    Next = case Rest of
        []      -> N;
        [NextPos | _] -> NextPos
    end,
    NewAcc = Acc + (Cur - Prev) * (Next - Cur),
    calc_contrib(Rest, N, Cur, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_letter_string(s :: String.t()) :: integer()
  def unique_letter_string(s) do
    n = byte_size(s)

    positions =
      s
      |> :binary.bin_to_list()
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {c, i}, acc ->
        Map.update(acc, c, [i], &[i | &1])
      end)

    positions
    |> Enum.reduce(0, fn {_char, rev_list}, sum ->
      list = Enum.reverse(rev_list)
      full = [-1] ++ list ++ [n]
      sum + contribution(full, 0)
    end)
  end

  defp contribution([prev, cur, nxt | rest], acc) do
    new_acc = acc + (cur - prev) * (nxt - cur)
    contribution([cur, nxt | rest], new_acc)
  end

  defp contribution(_, acc), do: acc
end
```
