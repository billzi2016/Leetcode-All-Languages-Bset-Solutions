# 1312. Minimum Insertion Steps to Make a String Palindrome

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minInsertions(string s) {
        int n = s.size();
        string rev(s.rbegin(), s.rend());
        vector<int> dp(n + 1, 0), prev(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == rev[j - 1])
                    dp[j] = prev[j - 1] + 1;
                else
                    dp[j] = max(prev[j], dp[j - 1]);
            }
            swap(dp, prev);
        }
        int lcs = prev[n];
        return n - lcs;
    }
};
```

## Java

```java
class Solution {
    public int minInsertions(String s) {
        String t = new StringBuilder(s).reverse().toString();
        int n = s.length();
        int[] prev = new int[n + 1];
        int[] cur = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    cur[j] = 1 + prev[j - 1];
                } else {
                    cur[j] = Math.max(prev[j], cur[j - 1]);
                }
            }
            int[] temp = prev;
            prev = cur;
            cur = temp; // reuse the array for next iteration
        }

        int lcs = prev[n];
        return n - lcs;
    }
}
```

## Python

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev = s[::-1]
        n = len(s)
        dp_prev = [0] * (n + 1)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[j] = dp_prev[j - 1] + 1
                else:
                    dp[j] = dp_prev[j] if dp_prev[j] > dp[j - 1] else dp[j - 1]
            dp_prev, dp = dp, [0] * (n + 1)

        lps = dp_prev[n]
        return n - lps
```

## Python3

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            si = s[i - 1]
            for j in range(1, n + 1):
                if si == rev[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        lcs_len = prev[n]
        return n - lcs_len
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minInsertions(char* s) {
    int n = strlen(s);
    char *rev = (char *)malloc(n + 1);
    rev[n] = '\0';
    for (int i = 0; i < n; ++i) rev[i] = s[n - 1 - i];

    int *prev = (int *)calloc(n + 1, sizeof(int));
    int *curr = (int *)calloc(n + 1, sizeof(int));

    for (int i = 1; i <= n; ++i) {
        curr[0] = 0;
        for (int j = 1; j <= n; ++j) {
            if (s[i - 1] == rev[j - 1])
                curr[j] = prev[j - 1] + 1;
            else
                curr[j] = (prev[j] > curr[j - 1]) ? prev[j] : curr[j - 1];
        }
        int *tmp = prev;
        prev = curr;
        curr = tmp;
    }

    int lcs = prev[n];
    free(rev);
    free(prev);
    free(curr);
    return n - lcs;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinInsertions(string s)
    {
        int n = s.Length;
        if (n == 0) return 0;

        char[] revArr = new char[n];
        for (int i = 0; i < n; i++) revArr[i] = s[n - 1 - i];
        string rev = new string(revArr);

        int[] dpPrev = new int[n + 1];
        int[] dp = new int[n + 1];

        for (int i = 1; i <= n; i++)
        {
            dp[0] = 0;
            char c1 = s[i - 1];
            for (int j = 1; j <= n; j++)
            {
                if (c1 == rev[j - 1])
                    dp[j] = dpPrev[j - 1] + 1;
                else
                    dp[j] = Math.Max(dpPrev[j], dp[j - 1]);
            }
            // swap references for next iteration
            var temp = dpPrev;
            dpPrev = dp;
            dp = temp;
        }

        int lps = dpPrev[n];
        return n - lps;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    const n = s.length;
    if (n <= 1) return 0;
    const t = s.split('').reverse().join('');
    let dpPrev = new Array(n + 1).fill(0);
    let dp = new Array(n + 1).fill(0);
    
    for (let i = 1; i <= n; i++) {
        dp[0] = 0;
        const chS = s[i - 1];
        for (let j = 1; j <= n; j++) {
            if (chS === t[j - 1]) {
                dp[j] = dpPrev[j - 1] + 1;
            } else {
                dp[j] = Math.max(dpPrev[j], dp[j - 1]);
            }
        }
        // swap references for next iteration
        const temp = dpPrev;
        dpPrev = dp;
        dp = temp;
    }
    
    const lcs = dpPrev[n];
    return n - lcs;
};
```

## Typescript

```typescript
function minInsertions(s: string): number {
    const n = s.length;
    if (n <= 1) return 0;
    const t = s.split('').reverse().join('');
    let prev = new Array(n + 1).fill(0);
    let curr = new Array(n + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= n; j++) {
            if (s[i - 1] === t[j - 1]) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = Math.max(prev[j], curr[j - 1]);
            }
        }
        const temp = prev;
        prev = curr;
        curr = temp;
    }

    const lcs = prev[n];
    return n - lcs;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minInsertions($s) {
        $n = strlen($s);
        if ($n <= 1) return 0;
        $t = strrev($s);

        $prev = array_fill(0, $n + 1, 0);
        $curr = array_fill(0, $n + 1, 0);

        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s[$i - 1] === $t[$j - 1]) {
                    $curr[$j] = $prev[$j - 1] + 1;
                } else {
                    $curr[$j] = max($prev[$j], $curr[$j - 1]);
                }
            }
            // swap rows for next iteration
            $temp = $prev;
            $prev = $curr;
            $curr = $temp;
        }

        $lps = $prev[$n];
        return $n - $lps;
    }
}
```

## Swift

```swift
class Solution {
    func minInsertions(_ s: String) -> Int {
        let chars = Array(s)
        let rev = Array(chars.reversed())
        let n = chars.count
        var prev = [Int](repeating: 0, count: n + 1)
        var cur = [Int](repeating: 0, count: n + 1)
        
        for i in 1...n {
            cur[0] = 0
            for j in 1...n {
                if chars[i - 1] == rev[j - 1] {
                    cur[j] = prev[j - 1] + 1
                } else {
                    cur[j] = max(prev[j], cur[j - 1])
                }
            }
            swap(&prev, &cur)
        }
        
        let lcsLength = prev[n]
        return n - lcsLength
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minInsertions(s: String): Int {
        val n = s.length
        val rev = s.reversed()
        var dpPrev = IntArray(n + 1)
        var dpCurr = IntArray(n + 1)

        for (i in 1..n) {
            dpCurr[0] = 0
            for (j in 1..n) {
                if (s[i - 1] == rev[j - 1]) {
                    dpCurr[j] = dpPrev[j - 1] + 1
                } else {
                    dpCurr[j] = kotlin.math.max(dpPrev[j], dpCurr[j - 1])
                }
            }
            // swap references for next iteration
            val temp = dpPrev
            dpPrev = dpCurr
            dpCurr = temp
        }

        val lps = dpPrev[n]
        return n - lps
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minInsertions(String s) {
    int n = s.length;
    String rev = s.split('').reversed.join();
    List<int> prev = List.filled(n + 1, 0);
    List<int> cur = List.filled(n + 1, 0);

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        if (s.codeUnitAt(i - 1) == rev.codeUnitAt(j - 1)) {
          cur[j] = prev[j - 1] + 1;
        } else {
          cur[j] = max(prev[j], cur[j - 1]);
        }
      }
      // swap rows for next iteration
      List<int> temp = prev;
      prev = cur;
      cur = temp;
    }

    int lps = prev[n];
    return n - lps;
  }
}
```

## Golang

```go
func minInsertions(s string) int {
	n := len(s)
	rev := make([]byte, n)
	for i := 0; i < n; i++ {
		rev[i] = s[n-1-i]
	}
	dpPrev := make([]int, n+1)
	dp := make([]int, n+1)

	for i := 1; i <= n; i++ {
		dp[0] = 0
		for j := 1; j <= n; j++ {
			if s[i-1] == rev[j-1] {
				dp[j] = dpPrev[j-1] + 1
			} else {
				if dpPrev[j] > dp[j-1] {
					dp[j] = dpPrev[j]
				} else {
					dp[j] = dp[j-1]
				}
			}
		}
		copy(dpPrev, dp)
	}

	lcs := dpPrev[n]
	return n - lcs
}
```

## Ruby

```ruby
def min_insertions(s)
  n = s.length
  rev = s.reverse
  prev = Array.new(n + 1, 0)
  cur = Array.new(n + 1, 0)

  (1..n).each do |i|
    (1..n).each do |j|
      if s[i - 1] == rev[j - 1]
        cur[j] = prev[j - 1] + 1
      else
        a = prev[j]
        b = cur[j - 1]
        cur[j] = a > b ? a : b
      end
    end
    prev, cur = cur, prev
    cur.fill(0)
  end

  lcs = prev[n]
  n - lcs
end
```

## Scala

```scala
object Solution {
  def minInsertions(s: String): Int = {
    val n = s.length
    if (n <= 1) return 0
    val rev = s.reverse
    val dpPrev = new Array[Int](n + 1)
    val dp = new Array[Int](n + 1)

    var i = 1
    while (i <= n) {
      var j = 1
      while (j <= n) {
        if (s.charAt(i - 1) == rev.charAt(j - 1)) {
          dp(j) = 1 + dpPrev(j - 1)
        } else {
          val a = dpPrev(j)
          val b = dp(j - 1)
          dp(j) = if (a > b) a else b
        }
        j += 1
      }
      var k = 0
      while (k <= n) {
        dpPrev(k) = dp(k)
        k += 1
      }
      i += 1
    }

    val lps = dpPrev(n)
    n - lps
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let rev: Vec<u8> = bytes.iter().rev().cloned().collect();

        let mut dp_prev = vec![0usize; n + 1];
        let mut dp = vec![0usize; n + 1];

        for i in 1..=n {
            for j in 1..=n {
                if bytes[i - 1] == rev[j - 1] {
                    dp[j] = dp_prev[j - 1] + 1;
                } else {
                    dp[j] = std::cmp::max(dp_prev[j], dp[j - 1]);
                }
            }
            std::mem::swap(&mut dp, &mut dp_prev);
        }

        let lcs_len = dp_prev[n];
        (n - lcs_len) as i32
    }
}
```

## Racket

```racket
(define/contract (min-insertions s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (rev (list->string (reverse (string->list s))))
         (prev (make-vector (+ n 1) 0))
         (curr (make-vector (+ n 1) 0)))
    (let loop-i ((i 1) (prev prev) (curr curr))
      (if (> i n)
          (let ((lps (vector-ref prev n)))
            (- n lps))
          (begin
            (vector-set! curr 0 0)
            (let loop-j ((j 1))
              (if (> j n)
                  (loop-i (+ i 1) curr prev)
                  (let* ((c1 (string-ref s (- i 1)))
                         (c2 (string-ref rev (- j 1))))
                    (if (char=? c1 c2)
                        (vector-set! curr j (+ 1 (vector-ref prev (- j 1))))
                        (let ((a (vector-ref prev j))
                              (b (vector-ref curr (- j 1))))
                          (vector-set! curr j (max a b))))
                    (loop-j (+ j 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_insertions/1]).

-spec min_insertions(S :: unicode:unicode_binary()) -> integer().
min_insertions(S) ->
    Str = binary_to_list(S),
    RevStr = lists:reverse(Str),
    N = length(Str),
    SeqT = list_to_tuple(Str),
    RevT = list_to_tuple(RevStr),
    LPS = lcs(SeqT, RevT, N),
    N - LPS.

lcs(_SeqT, _RevT, 0) -> 0;
lcs(SeqT, RevT, N) ->
    Prev0 = array:new(N + 1, {default, 0}),
    lcs_i(1, N, SeqT, RevT, Prev0).

lcs_i(I, N, _SeqT, _RevT, Prev) when I > N ->
    array:get(N, Prev);
lcs_i(I, N, SeqT, RevT, Prev) ->
    Curr = array:new(N + 1, {default, 0}),
    Curr1 = lcs_j(1, N, I, SeqT, RevT, Prev, Curr),
    lcs_i(I + 1, N, SeqT, RevT, Curr1).

lcs_j(J, N, _I, _SeqT, _RevT, _Prev, Curr) when J > N ->
    Curr;
lcs_j(J, N, I, SeqT, RevT, Prev, Curr) ->
    CharI = element(I, SeqT),
    CharJ = element(J, RevT),
    Val =
        if CharI == CharJ ->
                1 + array:get(J - 1, Prev);
           true ->
                MaxPrev = array:get(J, Prev),
                MaxCurrLeft = array:get(J - 1, Curr),
                if MaxPrev >= MaxCurrLeft -> MaxPrev; true -> MaxCurrLeft end
        end,
    Curr1 = array:set(J, Val, Curr),
    lcs_j(J + 1, N, I, SeqT, RevT, Prev, Curr1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_insertions(s :: String.t()) :: integer
  def min_insertions(s) do
    a = String.to_charlist(s)
    b = String.to_charlist(String.reverse(s))
    n = length(a)

    a_tuple = List.to_tuple(a)
    b_tuple = List.to_tuple(b)

    dp_prev = :array.new(n + 1, default: 0)

    {dp_final, _} =
      Enum.reduce(1..n, {dp_prev, nil}, fn i, {prev, _} ->
        dp_curr = :array.new(n + 1, default: 0)

        dp_curr =
          Enum.reduce(1..n, dp_curr, fn j, cur_arr ->
            if elem(a_tuple, i - 1) == elem(b_tuple, j - 1) do
              val = 1 + :array.get(j - 1, prev)
              :array.set(j, val, cur_arr)
            else
              val = max(:array.get(j, prev), :array.get(j - 1, cur_arr))
              :array.set(j, val, cur_arr)
            end
          end)

        {dp_curr, nil}
      end)

    lcs_len = :array.get(n, dp_final)
    n - lcs_len
  end
end
```
