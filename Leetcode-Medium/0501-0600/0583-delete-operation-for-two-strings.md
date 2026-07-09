# 0583. Delete Operation for Two Strings

## Cpp

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        if (n == 0 || m == 0) return n + m;
        vector<int> prev(m + 1, 0), cur(m + 1, 0);
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (word1[i - 1] == word2[j - 1])
                    cur[j] = prev[j - 1] + 1;
                else
                    cur[j] = max(prev[j], cur[j - 1]);
            }
            swap(prev, cur);
        }
        int lcs = prev[m];
        return n + m - 2 * lcs;
    }
};
```

## Java

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        // dp[i][j] will hold LCS length for prefixes of lengths i and j
        int[] prev = new int[m + 1];
        int[] curr = new int[m + 1];
        for (int i = 1; i <= n; i++) {
            char c1 = word1.charAt(i - 1);
            for (int j = 1; j <= m; j++) {
                if (c1 == word2.charAt(j - 1)) {
                    curr[j] = prev[j - 1] + 1;
                } else {
                    curr[j] = Math.max(prev[j], curr[j - 1]);
                }
            }
            // swap rows
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }
        int lcs = prev[m];
        return n + m - 2 * lcs;
    }
}
```

## Python

```python
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        if n == 0 or m == 0:
            return n + m

        # DP with two rows to compute LCS length
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        for i in range(1, n + 1):
            cur[0] = 0
            w1_char = word1[i - 1]
            for j in range(1, m + 1):
                if w1_char == word2[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev, cur = cur, prev  # reuse lists

        lcs_len = prev[m]
        return n + m - 2 * lcs_len
```

## Python3

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        if n == 0 or m == 0:
            return n + m
        dp_prev = [0] * (m + 1)
        dp_cur = [0] * (m + 1)
        for i in range(1, n + 1):
            w1_char = word1[i - 1]
            for j in range(1, m + 1):
                if w1_char == word2[j - 1]:
                    dp_cur[j] = dp_prev[j - 1] + 1
                else:
                    dp_cur[j] = max(dp_prev[j], dp_cur[j - 1])
            dp_prev, dp_cur = dp_cur, dp_prev  # reuse lists
        lcs_len = dp_prev[m]
        return n + m - 2 * lcs_len
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minDistance(char* word1, char* word2) {
    int n = strlen(word1);
    int m = strlen(word2);
    
    int *prev = (int*)calloc(m + 1, sizeof(int));
    int *curr = (int*)calloc(m + 1, sizeof(int));
    if (!prev || !curr) return -1; // allocation failure guard
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (word1[i - 1] == word2[j - 1])
                curr[j] = prev[j - 1] + 1;
            else
                curr[j] = (prev[j] > curr[j - 1]) ? prev[j] : curr[j - 1];
        }
        int *tmp = prev;
        prev = curr;
        curr = tmp;
        memset(curr, 0, (m + 1) * sizeof(int));
    }
    
    int lcs = prev[m];
    free(prev);
    free(curr);
    
    return n + m - 2 * lcs;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDistance(string word1, string word2)
    {
        int n = word1.Length;
        int m = word2.Length;
        if (n == 0) return m;
        if (m == 0) return n;

        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (word1[i - 1] == word2[j - 1])
                    cur[j] = prev[j - 1] + 1;
                else
                    cur[j] = Math.Max(prev[j], cur[j - 1]);
            }
            // swap references for next iteration
            var temp = prev;
            prev = cur;
            cur = temp;
        }

        int lcs = prev[m];
        return n + m - 2 * lcs;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const n = word1.length;
    const m = word2.length;
    // Ensure we use the shorter string for inner loop to save space
    if (m === 0) return n;
    if (n === 0) return m;

    let prev = new Array(m + 1).fill(0);
    let curr = new Array(m + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        curr[0] = 0;
        const c1 = word1.charAt(i - 1);
        for (let j = 1; j <= m; j++) {
            if (c1 === word2.charAt(j - 1)) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = Math.max(prev[j], curr[j - 1]);
            }
        }
        // swap rows
        [prev, curr] = [curr, prev];
    }

    const lcs = prev[m];
    return n + m - 2 * lcs;
};
```

## Typescript

```typescript
function minDistance(word1: string, word2: string): number {
    const n = word1.length;
    const m = word2.length;
    if (n === 0) return m;
    if (m === 0) return n;

    const dp: number[] = new Array(m + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        let prev = 0; // dp[j-1] from previous row
        for (let j = 1; j <= m; j++) {
            const temp = dp[j];
            if (word1[i - 1] === word2[j - 1]) {
                dp[j] = prev + 1;
            } else {
                dp[j] = Math.max(dp[j], dp[j - 1]);
            }
            prev = temp;
        }
    }

    const lcs = dp[m];
    return n + m - 2 * lcs;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function minDistance($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        if ($n == 0) return $m;
        if ($m == 0) return $n;

        $prev = array_fill(0, $m + 1, 0);
        $curr = array_fill(0, $m + 1, 0);

        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $m; $j++) {
                if ($word1[$i - 1] === $word2[$j - 1]) {
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

        $lcs = $prev[$m];
        return $n + $m - 2 * $lcs;
    }
}
```

## Swift

```swift
class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        let a = Array(word1)
        let b = Array(word2)
        let n = a.count
        let m = b.count
        var prev = [Int](repeating: 0, count: m + 1)
        var curr = [Int](repeating: 0, count: m + 1)

        for i in 1...n {
            for j in 1...m {
                if a[i - 1] == b[j - 1] {
                    curr[j] = prev[j - 1] + 1
                } else {
                    curr[j] = max(prev[j], curr[j - 1])
                }
            }
            (prev, curr) = (curr, prev)
        }

        let lcs = prev[m]
        return n + m - 2 * lcs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDistance(word1: String, word2: String): Int {
        val n = word1.length
        val m = word2.length
        var prev = IntArray(m + 1)
        var curr = IntArray(m + 1)

        for (i in 1..n) {
            for (j in 1..m) {
                if (word1[i - 1] == word2[j - 1]) {
                    curr[j] = prev[j - 1] + 1
                } else {
                    curr[j] = maxOf(prev[j], curr[j - 1])
                }
            }
            val temp = prev
            prev = curr
            curr = temp
        }

        val lcs = prev[m]
        return n + m - 2 * lcs
    }
}
```

## Dart

```dart
class Solution {
  int minDistance(String word1, String word2) {
    int n = word1.length;
    int m = word2.length;
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        if (word1[i - 1] == word2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
        } else {
          dp[i][j] = dp[i - 1][j] > dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1];
        }
      }
    }

    int lcs = dp[n][m];
    return n + m - 2 * lcs;
  }
}
```

## Golang

```go
func minDistance(word1 string, word2 string) int {
	n, m := len(word1), len(word2)
	prev := make([]int, m+1)
	curr := make([]int, m+1)

	for i := 1; i <= n; i++ {
		curr[0] = 0
		for j := 1; j <= m; j++ {
			if word1[i-1] == word2[j-1] {
				curr[j] = prev[j-1] + 1
			} else {
				if prev[j] > curr[j-1] {
					curr[j] = prev[j]
				} else {
					curr[j] = curr[j-1]
				}
			}
		}
		prev, curr = curr, prev
	}

	lcs := prev[m]
	return n + m - 2*lcs
}
```

## Ruby

```ruby
def min_distance(word1, word2)
  n = word1.length
  m = word2.length
  prev = Array.new(m + 1, 0)
  cur = Array.new(m + 1, 0)

  (1..n).each do |i|
    cur[0] = 0
    (1..m).each do |j|
      if word1[i - 1] == word2[j - 1]
        cur[j] = prev[j - 1] + 1
      else
        cur[j] = [prev[j], cur[j - 1]].max
      end
    end
    prev, cur = cur, prev
  end

  lcs = prev[m]
  n + m - 2 * lcs
end
```

## Scala

```scala
object Solution {
    def minDistance(word1: String, word2: String): Int = {
        val n = word1.length
        val m = word2.length
        if (n == 0) return m
        if (m == 0) return n

        var dpPrev = new Array[Int](m + 1)
        var dpCurr = new Array[Int](m + 1)

        for (i <- 1 to n) {
            for (j <- 1 to m) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    dpCurr(j) = dpPrev(j - 1) + 1
                else
                    dpCurr(j) = math.max(dpPrev(j), dpCurr(j - 1))
            }
            val temp = dpPrev
            dpPrev = dpCurr
            dpCurr = temp
        }

        val lcs = dpPrev(m)
        n + m - 2 * lcs
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let bytes1 = word1.as_bytes();
        let bytes2 = word2.as_bytes();
        let n = bytes1.len();
        let m = bytes2.len();

        let mut prev = vec![0usize; m + 1];
        let mut cur = vec![0usize; m + 1];

        for i in 1..=n {
            for j in 1..=m {
                if bytes1[i - 1] == bytes2[j - 1] {
                    cur[j] = prev[j - 1] + 1;
                } else {
                    cur[j] = if prev[j] > cur[j - 1] { prev[j] } else { cur[j - 1] };
                }
            }
            std::mem::swap(&mut prev, &mut cur);
        }

        let lcs = prev[m];
        (n + m - 2 * lcs) as i32
    }
}
```

## Racket

```racket
(define/contract (min-distance word1 word2)
  (-> string? string? exact-integer?)
  (let* ((n (string-length word1))
         (m (string-length word2))
         (prev (make-vector (+ m 1) 0))
         (curr (make-vector (+ m 1) 0)))
    (for ([i (in-range 1 (add1 n))])
      (vector-set! curr 0 0)
      (let ((c1 (string-ref word1 (- i 1))))
        (for ([j (in-range 1 (add1 m))])
          (if (char=? c1 (string-ref word2 (- j 1)))
              (vector-set! curr j (+ 1 (vector-ref prev (- j 1))))
              (let ((a (vector-ref prev j))
                    (b (vector-ref curr (- j 1))))
                (vector-set! curr j (if (> a b) a b))))))
      (let ((temp prev))
        (set! prev curr)
        (set! curr temp)))
    (let ((lcs (vector-ref prev m)))
      (+ n m (* -2 lcs)))))
```

## Erlang

```erlang
-module(solution).
-export([min_distance/2]).

-spec min_distance(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
min_distance(Word1, Word2) ->
    S1 = binary_to_list(Word1),
    S2 = binary_to_list(Word2),
    LCS = lcs_len(S1, S2),
    length(S1) + length(S2) - 2 * LCS.

lcs_len(S1, S2) ->
    Len2 = length(S2),
    InitPrev = lists:duplicate(Len2 + 1, 0),
    FinalRow = dp_loop(S1, S2, InitPrev),
    lists:last(FinalRow).

dp_loop([], _S2, PrevRow) -> 
    PrevRow;
dp_loop([C|Cs], S2, PrevRow) ->
    CurrRow = process_char(C, S2, PrevRow),
    dp_loop(Cs, S2, CurrRow).

process_char(C, S2, PrevRow) ->
    [_Zero | PrevRest] = PrevRow,
    build_row(C, S2, PrevRest, 0, 0, []).

build_row(_C, [], _PrevRest, _PrevDiagPrev, _Left, Acc) ->
    lists:reverse([0 | Acc]);
build_row(C, [D|Ds], [PrevVal|PrevTail], PrevDiagPrev, Left, Acc) ->
    Curr = if C == D -> PrevDiagPrev + 1;
              true -> erlang:max(PrevVal, Left)
           end,
    build_row(C, Ds, PrevTail, PrevVal, Curr, [Curr | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_distance(word1 :: String.t(), word2 :: String.t()) :: integer()
  def min_distance(word1, word2) do
    n = byte_size(word1)
    m = byte_size(word2)

    init_prev = :array.new(m + 1, default: 0)

    final_arr =
      Enum.reduce(1..n, init_prev, fn i, prev ->
        char_i = :binary.at(word1, i - 1)

        {curr_rev, _left} =
          Enum.reduce(1..m, {[], 0}, fn j, {acc, left} ->
            if char_i == :binary.at(word2, j - 1) do
              val = :array.get(j - 1, prev) + 1
              {[val | acc], val}
            else
              up = :array.get(j, prev)
              val = if up > left, do: up, else: left
              {[val | acc], val}
            end
          end)

        curr_list = [0 | Enum.reverse(curr_rev)]
        :array.from_list(curr_list)
      end)

    lcs_len = :array.get(m, final_arr)
    n + m - 2 * lcs_len
  end
end
```
