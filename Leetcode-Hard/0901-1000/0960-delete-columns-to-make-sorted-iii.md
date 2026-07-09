# 0960. Delete Columns to Make Sorted III

## Cpp

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        if (n == 0) return 0;
        int m = strs[0].size();
        vector<int> dp(m, 1);
        int best = 1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < i; ++j) {
                bool ok = true;
                for (int r = 0; r < n; ++r) {
                    if (strs[r][j] > strs[r][i]) { ok = false; break; }
                }
                if (ok) dp[i] = max(dp[i], dp[j] + 1);
            }
            best = max(best, dp[i]);
        }
        return m - best;
    }
};
```

## Java

```java
class Solution {
    public int minDeletionSize(String[] strs) {
        int nRows = strs.length;
        int cols = strs[0].length();
        int[] dp = new int[cols];
        int maxKeep = 0;
        for (int i = 0; i < cols; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                boolean ok = true;
                for (int r = 0; r < nRows; r++) {
                    if (strs[r].charAt(j) > strs[r].charAt(i)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxKeep = Math.max(maxKeep, dp[i]);
        }
        return cols - maxKeep;
    }
}
```

## Python

```python
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        w = len(strs[0])
        dp = [1] * w  # longest keepable subsequence ending at column i
        for i in range(w):
            for j in range(i):
                ok = True
                for r in range(n):
                    if strs[r][j] > strs[r][i]:
                        ok = False
                        break
                if ok:
                    dp[i] = max(dp[i], dp[j] + 1)
        longest = max(dp) if w else 0
        return w - longest
```

## Python3

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        w = len(strs[0])
        dp = [1] * w
        for i in range(w):
            for j in range(i):
                ok = True
                for r in range(n):
                    if strs[r][j] > strs[r][i]:
                        ok = False
                        break
                if ok:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        max_keep = max(dp) if dp else 0
        return w - max_keep
```

## C

```c
int minDeletionSize(char** strs, int strsSize) {
    if (strsSize == 0) return 0;
    int n = strsSize;
    int m = strlen(strs[0]);
    int *dp = (int *)malloc(m * sizeof(int));
    int maxkeep = 0;
    for (int j = 0; j < m; ++j) {
        dp[j] = 1;
        for (int i = 0; i < j; ++i) {
            int ok = 1;
            for (int r = 0; r < n; ++r) {
                if (strs[r][i] > strs[r][j]) { ok = 0; break; }
            }
            if (ok && dp[i] + 1 > dp[j]) dp[j] = dp[i] + 1;
        }
        if (dp[j] > maxkeep) maxkeep = dp[j];
    }
    free(dp);
    return m - maxkeep;
}
```

## Csharp

```csharp
public class Solution {
    public int MinDeletionSize(string[] strs) {
        int n = strs.Length;
        int w = strs[0].Length;
        int[] dp = new int[w];
        int maxKeep = 0;

        for (int j = 0; j < w; j++) {
            dp[j] = 1; // keep only column j
            for (int i = 0; i < j; i++) {
                bool ok = true;
                for (int r = 0; r < n; r++) {
                    if (strs[r][i] > strs[r][j]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    dp[j] = Math.Max(dp[j], dp[i] + 1);
                }
            }
            maxKeep = Math.Max(maxKeep, dp[j]);
        }

        return w - maxKeep;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const n = strs.length;
    const m = strs[0].length;
    const dp = new Array(m).fill(1);
    let maxKeep = 1;

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < i; ++j) {
            let ok = true;
            for (let r = 0; r < n; ++r) {
                if (strs[r][j] > strs[r][i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        maxKeep = Math.max(maxKeep, dp[i]);
    }

    return m - maxKeep;
};
```

## Typescript

```typescript
function minDeletionSize(strs: string[]): number {
    const n = strs.length;
    const m = strs[0].length;
    const dp = new Array(m).fill(1);
    let maxKeep = 1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < i; j++) {
            let ok = true;
            for (let r = 0; r < n; r++) {
                if (strs[r].charCodeAt(j) > strs[r].charCodeAt(i)) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        maxKeep = Math.max(maxKeep, dp[i]);
    }

    return m - maxKeep;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        $n = count($strs);
        if ($n == 0) return 0;
        $m = strlen($strs[0]);
        $dp = array_fill(0, $m, 1);
        $maxKeep = 0;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $i; $j++) {
                $ok = true;
                for ($r = 0; $r < $n; $r++) {
                    if ($strs[$r][$j] > $strs[$r][$i]) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) {
                    $dp[$i] = max($dp[$i], $dp[$j] + 1);
                }
            }
            $maxKeep = max($maxKeep, $dp[$i]);
        }

        return $m - $maxKeep;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let n = strs.count
        guard let first = strs.first else { return 0 }
        let m = first.count
        var cols = [[UInt8]](repeating: [UInt8](repeating: 0, count: m), count: n)
        for i in 0..<n {
            let bytes = Array(strs[i].utf8)
            for j in 0..<m {
                cols[i][j] = bytes[j]
            }
        }
        var dp = [Int](repeating: 1, count: m)
        var maxKeep = 1
        if m == 0 { return 0 }
        for i in 0..<m {
            var best = 1
            if i > 0 {
                for j in 0..<i {
                    var ok = true
                    for r in 0..<n {
                        if cols[r][j] > cols[r][i] {
                            ok = false
                            break
                        }
                    }
                    if ok && dp[j] + 1 > best {
                        best = dp[j] + 1
                    }
                }
            }
            dp[i] = best
            if best > maxKeep { maxKeep = best }
        }
        return m - maxKeep
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        val n = strs.size
        val w = strs[0].length
        val dp = IntArray(w) { 1 }
        var best = 1
        for (j in 0 until w) {
            for (i in 0 until j) {
                var ok = true
                for (r in 0 until n) {
                    if (strs[r][i] > strs[r][j]) {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    dp[j] = maxOf(dp[j], dp[i] + 1)
                }
            }
            best = maxOf(best, dp[j])
        }
        return w - best
    }
}
```

## Dart

```dart
class Solution {
  int minDeletionSize(List<String> strs) {
    int n = strs.length;
    int m = strs[0].length;
    List<int> dp = List.filled(m, 1);
    int maxKeep = 1;

    for (int j = 0; j < m; ++j) {
      for (int i = 0; i < j; ++i) {
        bool ok = true;
        for (int r = 0; r < n; ++r) {
          if (strs[r].codeUnitAt(i) > strs[r].codeUnitAt(j)) {
            ok = false;
            break;
          }
        }
        if (ok && dp[i] + 1 > dp[j]) {
          dp[j] = dp[i] + 1;
        }
      }
      if (dp[j] > maxKeep) maxKeep = dp[j];
    }

    return m - maxKeep;
  }
}
```

## Golang

```go
func minDeletionSize(strs []string) int {
    n := len(strs)
    w := len(strs[0])
    dp := make([]int, w)
    maxKeep := 0
    for i := 0; i < w; i++ {
        dp[i] = 1
        for j := 0; j < i; j++ {
            ok := true
            for r := 0; r < n; r++ {
                if strs[r][j] > strs[r][i] {
                    ok = false
                    break
                }
            }
            if ok && dp[j]+1 > dp[i] {
                dp[i] = dp[j] + 1
            }
        }
        if dp[i] > maxKeep {
            maxKeep = dp[i]
        }
    }
    return w - maxKeep
}
```

## Ruby

```ruby
def min_deletion_size(strs)
  n = strs.size
  w = strs[0].size
  dp = Array.new(w, 1)
  max_len = 1

  (0...w).each do |i|
    (0...i).each do |j|
      ok = true
      (0...n).each do |r|
        if strs[r][j] > strs[r][i]
          ok = false
          break
        end
      end
      dp[i] = dp[j] + 1 if ok && dp[j] + 1 > dp[i]
    end
    max_len = dp[i] if dp[i] > max_len
  end

  w - max_len
end
```

## Scala

```scala
object Solution {
  def minDeletionSize(strs: Array[String]): Int = {
    val n = strs.length
    val w = strs(0).length
    val dp = new Array[Int](w)
    var maxKeep = 0

    def can(j: Int, i: Int): Boolean = {
      var r = 0
      while (r < n) {
        if (strs(r)(j) > strs(r)(i)) return false
        r += 1
      }
      true
    }

    for (i <- 0 until w) {
      dp(i) = 1
      var j = 0
      while (j < i) {
        if (can(j, i) && dp(j) + 1 > dp(i)) {
          dp(i) = dp(j) + 1
        }
        j += 1
      }
      if (dp(i) > maxKeep) maxKeep = dp(i)
    }

    w - maxKeep
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let n = strs.len();
        if n == 0 {
            return 0;
        }
        let m = strs[0].len();
        // Convert each string to a vector of bytes for fast indexing
        let cols: Vec<Vec<u8>> = strs.iter().map(|s| s.as_bytes().to_vec()).collect();

        let mut dp = vec![1usize; m];
        let mut best = 0usize;

        for i in 0..m {
            for j in 0..i {
                // check if column j can precede column i
                let mut ok = true;
                for r in 0..n {
                    if cols[r][j] > cols[r][i] {
                        ok = false;
                        break;
                    }
                }
                if ok && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                }
            }
            if dp[i] > best {
                best = dp[i];
            }
        }

        (m - best) as i32
    }
}
```

## Racket

```racket
(define/contract (min-deletion-size strs)
  (-> (listof string?) exact-integer?)
  (let* ((n (length strs))
         (m (if (= n 0) 0 (string-length (car strs))))
         (svec (list->vector strs))
         (dp (make-vector m 1)))
    (define (col-le? j i)
      (let loop ((row 0))
        (or (= row n)
            (let ((cj (string-ref (vector-ref svec row) j))
                  (ci (string-ref (vector-ref svec row) i)))
              (and (char<=? cj ci) (loop (+ row 1)))))))
    (for ([i (in-range m)])
      (vector-set! dp i 1)
      (for ([j (in-range i)])
        (when (col-le? j i)
          (let ((cand (+ (vector-ref dp j) 1))
                (curr (vector-ref dp i)))
            (when (> cand curr)
              (vector-set! dp i cand))))))
    (let ((maxlen (if (= m 0) 0
                     (apply max (vector->list dp)))))
      (- m maxlen))))
```

## Erlang

```erlang
-export([min_deletion_size/1]).
-spec min_deletion_size(Strs :: [unicode:unicode_binary()]) -> integer().
min_deletion_size(Strs) ->
    Rows = [binary_to_list(S) || S <- Strs],
    case Rows of
        [] -> 0;
        _ ->
            W = length(hd(Rows)),
            DP = build_dp(W, Rows),
            Longest = lists:max(DP),
            W - Longest
    end.

build_dp(W, Rows) ->
    lists:foldl(fun(I, AccDP) ->
        MaxPrev = max_prev(I, Rows, AccDP),
        AccDP ++ [MaxPrev + 1]
    end, [], lists:seq(0, W - 1)).

max_prev(Index, Rows, DP) ->
    max_prev(Index, 0, 0, Rows, DP).

max_prev(Index, J, Max, _Rows, _DP) when J >= Index -> Max;
max_prev(Index, J, Max, Rows, DP) ->
    case can(J, Index, Rows) of
        true ->
            Val = lists:nth(J + 1, DP),
            NewMax = if Val > Max -> Val; true -> Max end,
            max_prev(Index, J + 1, NewMax, Rows, DP);
        false ->
            max_prev(Index, J + 1, Max, Rows, DP)
    end.

can(I, J, Rows) ->
    lists:all(fun(Row) ->
        CharI = lists:nth(I + 1, Row),
        CharJ = lists:nth(J + 1, Row),
        CharI =< CharJ
    end, Rows).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t]) :: integer
  def min_deletion_size(strs) do
    rows = Enum.map(strs, &String.to_charlist/1)
    m = String.length(List.first(strs))

    columns =
      for i <- 0..(m - 1) do
        Enum.map(rows, fn r -> Enum.at(r, i) end)
      end

    dp = :array.new(m, default: 0)

    dp =
      Enum.reduce(0..(m - 1), dp, fn i, acc ->
        best = 1

        best =
          Enum.reduce(0..(i - 1), best, fn j, cur_best ->
            col_j = Enum.at(columns, j)
            col_i = Enum.at(columns, i)

            if Enum.all?(Enum.zip(col_j, col_i), fn {c1, c2} -> c1 <= c2 end) do
              prev = :array.get(j, acc)
              max(cur_best, prev + 1)
            else
              cur_best
            end
          end)

        :array.set(i, best, acc)
      end)

    max_keep =
      Enum.reduce(0..(m - 1), 0, fn i, cur -> max(cur, :array.get(i, dp)) end)

    m - max_keep
  end
end
```
