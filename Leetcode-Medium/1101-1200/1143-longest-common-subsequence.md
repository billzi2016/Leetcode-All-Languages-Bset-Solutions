# 1143. Longest Common Subsequence

## Cpp

```cpp
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size(), m = text2.size();
        if (n == 0 || m == 0) return 0;
        vector<int> dp(m + 1, 0), prev(m + 1, 0);
        for (int i = 1; i <= n; ++i) {
            swap(dp, prev);
            dp[0] = 0;
            for (int j = 1; j <= m; ++j) {
                if (text1[i - 1] == text2[j - 1])
                    dp[j] = prev[j - 1] + 1;
                else
                    dp[j] = max(prev[j], dp[j - 1]);
            }
        }
        return dp[m];
    }
};
```

## Java

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if (text1 == null || text2 == null) return 0;
        int m = text1.length();
        int n = text2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int prevDiag = 0;
            char c1 = text1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (c1 == text2.charAt(j - 1)) {
                    dp[j] = prevDiag + 1;
                } else {
                    dp[j] = Math.max(dp[j], dp[j - 1]);
                }
                prevDiag = temp;
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Ensure text2 is the shorter one to use less space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        n = len(text2)
        dp = [0] * (n + 1)

        for i in range(1, len(text1) + 1):
            prev = 0
            c1 = text1[i - 1]
            for j in range(1, n + 1):
                temp = dp[j]
                if c1 == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    # max of left (dp[j-1]) and up (dp[j])
                    if dp[j - 1] > dp[j]:
                        dp[j] = dp[j - 1]
                prev = temp

        return dp[n]
```

## Python3

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        if n == 0 or m == 0:
            return 0
        # Ensure we use the shorter string for DP columns to save space
        if m > n:
            text1, text2 = text2, text1
            n, m = m, n
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prev = 0
            c1 = text1[i - 1]
            for j in range(1, m + 1):
                temp = dp[j]
                if c1 == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = dp[j] if dp[j] > dp[j - 1] else dp[j - 1]
                prev = temp
        return dp[m]
```

## C

```c
int longestCommonSubsequence(char* text1, char* text2) {
    if (!text1 || !text2) return 0;
    int n = 0, m = 0;
    while (text1[n]) ++n;
    while (text2[m]) ++m;

    int rows = n + 1;
    int cols = m + 1;
    int *dp = (int *)calloc(rows * cols, sizeof(int));
    if (!dp) return 0; // allocation failure fallback

    for (int i = 1; i <= n; ++i) {
        char c1 = text1[i - 1];
        for (int j = 1; j <= m; ++j) {
            if (c1 == text2[j - 1]) {
                dp[i * cols + j] = dp[(i - 1) * cols + (j - 1)] + 1;
            } else {
                int up = dp[(i - 1) * cols + j];
                int left = dp[i * cols + (j - 1)];
                dp[i * cols + j] = up > left ? up : left;
            }
        }
    }

    int result = dp[n * cols + m];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestCommonSubsequence(string text1, string text2)
    {
        int m = text1.Length;
        int n = text2.Length;

        // Ensure we use the shorter string for DP columns to save space
        if (n > m)
        {
            var tmpStr = text1;
            text1 = text2;
            text2 = tmpStr;
            int tmpLen = m;
            m = n;
            n = tmpLen;
        }

        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++)
        {
            int prevDiag = 0; // dp[i-1][j-1]
            for (int j = 1; j <= n; j++)
            {
                int temp = dp[j]; // store old dp[j] which is dp[i-1][j]
                if (text1[i - 1] == text2[j - 1])
                {
                    dp[j] = prevDiag + 1;
                }
                else
                {
                    dp[j] = Math.Max(dp[j], dp[j - 1]);
                }
                prevDiag = temp;
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const m = text1.length;
    const n = text2.length;
    let prev = new Uint16Array(n + 1);
    let curr = new Uint16Array(n + 1);
    
    for (let i = 1; i <= m; ++i) {
        for (let j = 1; j <= n; ++j) {
            if (text1[i - 1] === text2[j - 1]) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = Math.max(prev[j], curr[j - 1]);
            }
        }
        // swap rows for next iteration
        const temp = prev;
        prev = curr;
        curr = temp;
    }
    
    return prev[n];
};
```

## Typescript

```typescript
function longestCommonSubsequence(text1: string, text2: string): number {
    const m = text1.length, n = text2.length;
    if (m === 0 || n === 0) return 0;
    let prev = new Uint16Array(n + 1);
    let cur = new Uint16Array(n + 1);
    for (let i = 1; i <= m; i++) {
        const c1 = text1.charAt(i - 1);
        for (let j = 1; j <= n; j++) {
            if (c1 === text2.charAt(j - 1)) {
                cur[j] = prev[j - 1] + 1;
            } else {
                cur[j] = Math.max(prev[j], cur[j - 1]);
            }
        }
        const temp = prev;
        prev = cur;
        cur = temp;
    }
    return prev[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $text1
     * @param String $text2
     * @return Integer
     */
    function longestCommonSubsequence($text1, $text2) {
        $n = strlen($text1);
        $m = strlen($text2);
        if ($n == 0 || $m == 0) return 0;

        // Ensure we use the smaller string for inner loop to save memory
        if ($m > $n) {
            // swap to make $m <= $n
            $tmp = $text1;
            $text1 = $text2;
            $text2 = $tmp;
            $tempLen = $n;
            $n = $m;
            $m = $tempLen;
        }

        $prev = array_fill(0, $m + 1, 0);
        $curr = array_fill(0, $m + 1, 0);

        for ($i = 1; $i <= $n; $i++) {
            for ($j = 1; $j <= $m; $j++) {
                if ($text1[$i - 1] === $text2[$j - 1]) {
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

        return $prev[$m];
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        let a = Array(text1)
        let b = Array(text2)
        let m = a.count
        let n = b.count
        if m == 0 || n == 0 { return 0 }
        var prev = [Int](repeating: 0, count: n + 1)
        var cur = [Int](repeating: 0, count: n + 1)

        for i in 1...m {
            for j in 1...n {
                if a[i - 1] == b[j - 1] {
                    cur[j] = prev[j - 1] + 1
                } else {
                    cur[j] = max(prev[j], cur[j - 1])
                }
            }
            let temp = prev
            prev = cur
            cur = temp
        }
        return prev[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestCommonSubsequence(text1: String, text2: String): Int {
        val m = text1.length
        val n = text2.length
        if (m == 0 || n == 0) return 0

        var prev = IntArray(n + 1)
        var curr = IntArray(n + 1)

        for (i in 1..m) {
            for (j in 1..n) {
                if (text1[i - 1] == text2[j - 1]) {
                    curr[j] = prev[j - 1] + 1
                } else {
                    curr[j] = kotlin.math.max(prev[j], curr[j - 1])
                }
            }
            val temp = prev
            prev = curr
            curr = temp
        }
        return prev[n]
    }
}
```

## Dart

```dart
class Solution {
  int longestCommonSubsequence(String text1, String text2) {
    int n = text1.length;
    int m = text2.length;
    List<int> prev = List.filled(m + 1, 0);
    List<int> curr = List.filled(m + 1, 0);

    for (int i = 1; i <= n; i++) {
      int c1 = text1.codeUnitAt(i - 1);
      for (int j = 1; j <= m; j++) {
        if (c1 == text2.codeUnitAt(j - 1)) {
          curr[j] = prev[j - 1] + 1;
        } else {
          curr[j] = prev[j] > curr[j - 1] ? prev[j] : curr[j - 1];
        }
      }
      List<int> temp = prev;
      prev = curr;
      curr = temp;
    }

    return prev[m];
  }
}
```

## Golang

```go
func longestCommonSubsequence(text1 string, text2 string) int {
    n, m := len(text1), len(text2)
    if n == 0 || m == 0 {
        return 0
    }
    dp := make([]int, m+1)
    for i := 1; i <= n; i++ {
        prev := 0
        for j := 1; j <= m; j++ {
            temp := dp[j]
            if text1[i-1] == text2[j-1] {
                dp[j] = prev + 1
            } else {
                if dp[j] < dp[j-1] {
                    dp[j] = dp[j-1]
                }
            }
            prev = temp
        }
    }
    return dp[m]
}
```

## Ruby

```ruby
def longest_common_subsequence(text1, text2)
  m = text1.length
  n = text2.length
  return 0 if m == 0 || n == 0

  prev = Array.new(n + 1, 0)
  curr = Array.new(n + 1, 0)

  (1..m).each do |i|
    (1..n).each do |j|
      if text1[i - 1] == text2[j - 1]
        curr[j] = prev[j - 1] + 1
      else
        a = prev[j]
        b = curr[j - 1]
        curr[j] = a > b ? a : b
      end
    end
    prev, curr = curr, prev
  end

  prev[n]
end
```

## Scala

```scala
object Solution {
  def longestCommonSubsequence(text1: String, text2: String): Int = {
    val m = text1.length
    val n = text2.length
    if (m == 0 || n == 0) return 0

    // Ensure we use the shorter string for inner loop to save space
    val (s1, s2) = if (n < m) (text2, text1) else (text1, text2)
    val len1 = s1.length
    val len2 = s2.length

    var prev = new Array[Int](len1 + 1)
    var cur = new Array[Int](len1 + 1)

    for (i <- 1 to len2) {
      for (j <- 1 to len1) {
        if (s2.charAt(i - 1) == s1.charAt(j - 1))
          cur(j) = prev(j - 1) + 1
        else
          cur(j) = math.max(prev(j), cur(j - 1))
      }
      // swap arrays for next iteration
      val temp = prev
      prev = cur
      cur = temp
    }

    prev(len1)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let a = text1.as_bytes();
        let b = text2.as_bytes();

        // Ensure we use the shorter string for DP columns to save space
        if b.len() > a.len() {
            return Self::longest_common_subsequence(text2, text1);
        }

        let n = b.len();
        let mut dp = vec![0i32; n + 1];

        for &ch_a in a.iter() {
            let mut prev = 0;
            for (j, &ch_b) in b.iter().enumerate() {
                let temp = dp[j + 1];
                if ch_a == ch_b {
                    dp[j + 1] = prev + 1;
                } else {
                    dp[j + 1] = dp[j + 1].max(dp[j]);
                }
                prev = temp;
            }
        }

        dp[n]
    }
}
```

## Racket

```racket
(define/contract (longest-common-subsequence text1 text2)
  (-> string? string? exact-integer?)
  (let* ([n (string-length text1)]
         [m (string-length text2)])
    (if (or (= n 0) (= m 0))
        0
        (let ([prev (make-vector (+ m 1) 0)]
              [cur  (make-vector (+ m 1) 0)])
          (for ([i (in-range 1 (add1 n))])
            (vector-set! cur 0 0)
            (for ([j (in-range 1 (add1 m))])
              (if (char=? (string-ref text1 (- i 1))
                          (string-ref text2 (- j 1)))
                  (vector-set! cur j (+ 1 (vector-ref prev (- j 1))))
                  (vector-set! cur j
                               (max (vector-ref prev j)
                                    (vector-ref cur (- j 1))))))
            (let ([tmp prev])
              (set! prev cur)
              (set! cur tmp)))
          (vector-ref prev m))))))
```

## Erlang

```erlang
-module(solution).
-export([longest_common_subsequence/2]).

-spec longest_common_subsequence(unicode:unicode_binary(), unicode:unicode_binary()) -> integer().
longest_common_subsequence(Text1, Text2) ->
    List1 = binary_to_list(Text1),
    List2 = binary_to_list(Text2),
    M = length(List2),
    ZeroRow = lists:duplicate(M + 1, 0),
    FinalRow = lists:foldl(fun(C1, PrevRow) ->
        compute_row(C1, List2, PrevRow)
    end, ZeroRow, List1),
    hd(lists:reverse(FinalRow)).

compute_row(_C1, [], _PrevRow) -> [0];
compute_row(C1, List2, PrevRow) ->
    PrevTail = tl(PrevRow),
    Zipped = lists:zip(List2, PrevTail),
    {RevCurr, _} = lists:foldl(fun({C2, PrevVal}, {CurAccRev, PrevDiag}) ->
        PrevLeft = case CurAccRev of [] -> 0; [L|_] -> L end,
        CurVal = if C1 == C2 -> PrevDiag + 1;
                    true -> erlang:max(PrevVal, PrevLeft)
                 end,
        {[CurVal | CurAccRev], PrevVal}
    end, {[], 0}, Zipped),
    [0 | lists:reverse(RevCurr)].
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_common_subsequence(text1 :: String.t(), text2 :: String.t()) :: integer()
  def longest_common_subsequence(text1, text2) do
    t1 = String.graphemes(text1)
    t2 = String.graphemes(text2)

    m = length(t2)

    # initial previous row filled with zeros (size m+1)
    prev_row = :array.new(m + 1, default: 0)

    final_row =
      Enum.reduce(Enum.with_index(t1, 1), prev_row, fn {ch1, _i}, prev ->
        # start a new current row
        cur_row = :array.new(m + 1, default: 0)

        cur_row =
          Enum.reduce(Enum.with_index(t2, 1), cur_row, fn {ch2, j}, cur ->
            val =
              if ch1 == ch2 do
                :array.get(j - 1, prev) + 1
              else
                up = :array.get(j, prev)
                left = :array.get(j - 1, cur)

                if up > left, do: up, else: left
              end

            :array.set(j, val, cur)
          end)

        cur_row
      end)

    :array.get(m, final_row)
  end
end
```
