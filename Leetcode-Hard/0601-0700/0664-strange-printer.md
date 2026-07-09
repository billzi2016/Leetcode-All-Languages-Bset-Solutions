# 0664. Strange Printer

## Cpp

```cpp
class Solution {
public:
    int strangePrinter(string s) {
        string t;
        for (char c : s) {
            if (t.empty() || t.back() != c) t.push_back(c);
        }
        int n = t.size();
        if (n == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(n, -1));
        function<int(int,int)> solve = [&](int l, int r) -> int {
            if (l > r) return 0;
            int &res = dp[l][r];
            if (res != -1) return res;
            res = 1 + solve(l + 1, r);
            for (int k = l + 1; k <= r; ++k) {
                if (t[k] == t[l]) {
                    res = min(res, solve(l, k - 1) + solve(k + 1, r));
                }
            }
            return res;
        };
        return solve(0, n - 1);
    }
};
```

## Java

```java
class Solution {
    public int strangePrinter(String s) {
        // Remove consecutive duplicate characters
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (i == 0 || s.charAt(i) != s.charAt(i - 1)) {
                sb.append(s.charAt(i));
            }
        }
        char[] chars = sb.toString().toCharArray();
        int n = chars.length;
        if (n == 0) return 0;

        int[][] memo = new int[n][n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(memo[i], -1);
        }
        return dfs(0, n - 1, chars, memo);
    }

    private int dfs(int l, int r, char[] s, int[][] memo) {
        if (l > r) return 0;
        if (memo[l][r] != -1) return memo[l][r];

        // Print s[l] alone then the rest
        int ans = 1 + dfs(l + 1, r, s, memo);

        for (int k = l + 1; k <= r; k++) {
            if (s[k] == s[l]) {
                int combined = dfs(l, k - 1, s, memo) + dfs(k + 1, r, s, memo);
                ans = Math.min(ans, combined);
            }
        }

        memo[l][r] = ans;
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove consecutive duplicates to reduce problem size
        compressed = []
        for ch in s:
            if not compressed or compressed[-1] != ch:
                compressed.append(ch)
        s = ''.join(compressed)
        n = len(s)
        if n == 0:
            return 0

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            # Print s[i] alone then solve the rest
            ans = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    # Merge printing of s[i] with s[k]
                    ans = min(ans, dp(i + 1, k - 1) + dp(k, j))
            return ans

        return dp(0, n - 1)
```

## Python3

```python
class Solution:
    def strangePrinter(self, s: str) -> int:
        # Remove consecutive duplicates to reduce problem size
        filtered = []
        for ch in s:
            if not filtered or filtered[-1] != ch:
                filtered.append(ch)
        s = ''.join(filtered)
        n = len(s)
        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Print s[i] separately then the rest
                dp[i][j] = dp[i + 1][j] + 1
                # Try to merge prints where characters match
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        left = dp[i + 1][k - 1] if k - 1 >= i + 1 else 0
                        val = left + dp[k][j]
                        if val < dp[i][j]:
                            dp[i][j] = val

        return dp[0][n - 1]
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int strangePrinter(char* s) {
    if (!s) return 0;
    int orig_len = strlen(s);
    if (orig_len == 0) return 0;

    // Remove consecutive duplicates
    char proc[105];
    int n = 0;
    for (int i = 0; i < orig_len; ++i) {
        if (i == 0 || s[i] != s[i - 1]) {
            proc[n++] = s[i];
        }
    }
    proc[n] = '\0';
    if (n == 0) return 0;

    // DP table
    int dp[105][105] = {0};

    for (int i = 0; i < n; ++i)
        dp[i][i] = 1;

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len - 1 < n; ++i) {
            int j = i + len - 1;
            // worst case: print s[j] separately
            dp[i][j] = dp[i][j - 1] + 1;
            for (int k = i; k < j; ++k) {
                if (proc[k] == proc[j]) {
                    int left = dp[i][k];
                    int right = (k + 1 <= j - 1) ? dp[k + 1][j - 1] : 0;
                    if (left + right < dp[i][j])
                        dp[i][j] = left + right;
                }
            }
        }
    }

    return dp[0][n - 1];
}
```

## Csharp

```csharp
public class Solution
{
    public int StrangePrinter(string s)
    {
        if (string.IsNullOrEmpty(s)) return 0;

        // Remove consecutive duplicate characters
        var sb = new System.Text.StringBuilder();
        foreach (char c in s)
        {
            if (sb.Length == 0 || sb[sb.Length - 1] != c)
                sb.Append(c);
        }
        string t = sb.ToString();
        int n = t.Length;
        int[,] memo = new int[n, n];

        int Dfs(int i, int j)
        {
            if (i > j) return 0;
            if (memo[i, j] != 0) return memo[i, j];

            int ans = 1 + Dfs(i + 1, j);
            for (int k = i + 1; k <= j; k++)
            {
                if (t[k] == t[i])
                {
                    int temp = Dfs(i, k - 1) + Dfs(k + 1, j);
                    if (temp < ans) ans = temp;
                }
            }

            memo[i, j] = ans;
            return ans;
        }

        return Dfs(0, n - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var strangePrinter = function(s) {
    // Remove consecutive duplicates to reduce problem size
    let filtered = '';
    for (let i = 0; i < s.length; ++i) {
        if (i === 0 || s[i] !== s[i - 1]) filtered += s[i];
    }
    const n = filtered.length;
    if (n === 0) return 0;

    // memo[l][r] stores answer for substring [l, r]
    const memo = Array.from({ length: n }, () => Array(n).fill(-1));

    function dp(l, r) {
        if (l > r) return 0;
        if (memo[l][r] !== -1) return memo[l][r];

        // Print filtered[l] alone, then solve the rest
        let ans = 1 + dp(l + 1, r);

        // Try to merge prints when same character appears later
        for (let k = l + 1; k <= r; ++k) {
            if (filtered[k] === filtered[l]) {
                const merged = dp(l + 1, k - 1) + dp(k, r);
                if (merged < ans) ans = merged;
            }
        }

        memo[l][r] = ans;
        return ans;
    }

    return dp(0, n - 1);
};
```

## Typescript

```typescript
function strangePrinter(s: string): number {
    // Remove consecutive duplicate characters to reduce problem size
    let filtered = "";
    for (let i = 0; i < s.length; i++) {
        if (i === 0 || s[i] !== s[i - 1]) {
            filtered += s[i];
        }
    }

    const n = filtered.length;
    if (n === 0) return 0;

    // dp[l][r]: minimum turns to print substring filtered[l..r]
    const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    for (let l = n - 1; l >= 0; l--) {
        dp[l][l] = 1;
        for (let r = l + 1; r < n; r++) {
            // Print filtered[l] separately, then the rest
            dp[l][r] = dp[l + 1][r] + 1;

            // Try to merge prints when characters match
            for (let k = l + 1; k <= r; k++) {
                if (filtered[k] === filtered[l]) {
                    const left = k === l + 1 ? 0 : dp[l + 1][k - 1];
                    const right = dp[k][r];
                    dp[l][r] = Math.min(dp[l][r], left + right);
                }
            }
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function strangePrinter($s) {
        // Remove consecutive duplicates
        $len = strlen($s);
        if ($len == 0) return 0;
        $filtered = '';
        for ($i = 0; $i < $len; $i++) {
            if ($i == 0 || $s[$i] !== $s[$i - 1]) {
                $filtered .= $s[$i];
            }
        }
        $s = $filtered;
        $n = strlen($s);
        if ($n == 0) return 0;

        // dp[i][j] = minimum turns to print s[i..j]
        $dp = array_fill(0, $n, array_fill(0, $n, 0));

        $dfs = function($i, $j) use (&$s, &$dp, &$dfs) {
            if ($i > $j) return 0;
            if ($dp[$i][$j] != 0) return $dp[$i][$j];

            // Print s[i] alone then the rest
            $res = 1 + $dfs($i + 1, $j);

            for ($k = $i + 1; $k <= $j; $k++) {
                if ($s[$k] === $s[$i]) {
                    $temp = $dfs($i, $k - 1) + $dfs($k + 1, $j);
                    if ($temp < $res) $res = $temp;
                }
            }

            $dp[$i][$j] = $res;
            return $res;
        };

        return $dfs(0, $n - 1);
    }
}
```

## Swift

```swift
class Solution {
    func strangePrinter(_ s: String) -> Int {
        // Remove consecutive duplicate characters
        var filtered = [Character]()
        for ch in s {
            if filtered.isEmpty || filtered.last! != ch {
                filtered.append(ch)
            }
        }
        let n = filtered.count
        if n == 0 { return 0 }
        
        var dp = Array(repeating: Array(repeating: -1, count: n), count: n)
        
        func helper(_ i: Int, _ j: Int) -> Int {
            if i > j { return 0 }
            if dp[i][j] != -1 { return dp[i][j] }
            
            var ans = 1 + helper(i + 1, j) // print filtered[i] alone
            if i + 1 <= j {
                for k in (i + 1)...j where filtered[k] == filtered[i] {
                    let temp = helper(i, k - 1) + helper(k + 1, j)
                    if temp < ans { ans = temp }
                }
            }
            dp[i][j] = ans
            return ans
        }
        
        return helper(0, n - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun strangePrinter(s: String): Int {
        if (s.isEmpty()) return 0
        val sb = StringBuilder()
        var prev = '#'
        for (c in s) {
            if (c != prev) {
                sb.append(c)
                prev = c
            }
        }
        val str = sb.toString()
        val n = str.length
        val memo = Array(n) { IntArray(n) { -1 } }

        fun dfs(l: Int, r: Int): Int {
            if (l > r) return 0
            if (memo[l][r] != -1) return memo[l][r]
            var res = 1 + dfs(l + 1, r)
            for (k in l + 1..r) {
                if (str[k] == str[l]) {
                    val candidate = dfs(l, k - 1) + dfs(k + 1, r)
                    if (candidate < res) res = candidate
                }
            }
            memo[l][r] = res
            return res
        }

        return dfs(0, n - 1)
    }
}
```

## Dart

```dart
class Solution {
  int strangePrinter(String s) {
    // Remove consecutive duplicate characters
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      if (i == 0 || s[i] != s[i - 1]) {
        sb.write(s[i]);
      }
    }
    String str = sb.toString();
    int n = str.length;
    if (n == 0) return 0;

    List<List<int>> memo = List.generate(n, (_) => List.filled(n, 0));

    int dfs(int i, int j) {
      if (i > j) return 0;
      if (memo[i][j] != 0) return memo[i][j];
      // Print str[i] alone then the rest
      int res = 1 + dfs(i + 1, j);
      for (int k = i + 1; k <= j; k++) {
        if (str[k] == str[i]) {
          int temp = dfs(i, k - 1) + dfs(k + 1, j);
          if (temp < res) res = temp;
        }
      }
      memo[i][j] = res;
      return res;
    }

    return dfs(0, n - 1);
  }
}
```

## Golang

```go
func strangePrinter(s string) int {
	// Remove consecutive duplicate characters
	if len(s) == 0 {
		return 0
	}
	var t []byte
	for i := 0; i < len(s); i++ {
		if i == 0 || s[i] != s[i-1] {
			t = append(t, s[i])
		}
	}
	str := string(t)
	n := len(str)
	if n == 0 {
		return 0
	}

	// dp[l][r] = minimum turns to print str[l..r]
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = -1
		}
	}

	var dfs func(l, r int) int
	dfs = func(l, r int) int {
		if l > r {
			return 0
		}
		if dp[l][r] != -1 {
			return dp[l][r]
		}
		// Print str[l] alone, then the rest
		best := 1 + dfs(l+1, r)
		for k := l + 1; k <= r; k++ {
			if str[k] == str[l] {
				// Merge printing of str[l] with str[k]
				cost := dfs(l, k-1) + dfs(k+1, r)
				if cost < best {
					best = cost
				}
			}
		}
		dp[l][r] = best
		return best
	}

	return dfs(0, n-1)
}
```

## Ruby

```ruby
def strange_printer(s)
  # Remove consecutive duplicate characters
  t = ''
  s.each_char { |c| t << c if t.empty? || t[-1] != c }
  n = t.length
  return 0 if n == 0

  memo = Array.new(n) { Array.new(n, -1) }

  dfs = nil
  dfs = lambda do |l, r|
    return 0 if l > r
    return 1 if l == r
    cached = memo[l][r]
    return cached unless cached == -1

    # Print t[l] alone first
    best = 1 + dfs.call(l + 1, r)

    (l + 1).upto(r) do |k|
      if t[k] == t[l]
        cost = dfs.call(l, k - 1) + dfs.call(k + 1, r)
        best = [best, cost].min
      end
    end

    memo[l][r] = best
  end

  dfs.call(0, n - 1)
end
```

## Scala

```scala
object Solution {
    def strangePrinter(s: String): Int = {
        // Remove consecutive duplicate characters
        val sb = new StringBuilder
        for (c <- s) {
            if (sb.isEmpty || sb.last != c) sb.append(c)
        }
        val str = sb.toString()
        val n = str.length
        if (n == 0) return 0

        val dp = Array.ofDim[Int](n, n)

        def dfs(l: Int, r: Int): Int = {
            if (l > r) return 0
            if (dp(l)(r) != 0) return dp(l)(r)
            var res = 1 + dfs(l + 1, r) // print str(l) alone
            var k = l + 1
            while (k <= r) {
                if (str.charAt(k) == str.charAt(l)) {
                    val temp = dfs(l, k - 1) + dfs(k + 1, r)
                    if (temp < res) res = temp
                }
                k += 1
            }
            dp(l)(r) = res
            res
        }

        dfs(0, n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn strange_printer(s: String) -> i32 {
        // Remove consecutive duplicate characters
        let mut filtered: Vec<char> = Vec::new();
        for ch in s.chars() {
            if filtered.last() != Some(&ch) {
                filtered.push(ch);
            }
        }

        let n = filtered.len();
        if n == 0 {
            return 0;
        }

        // dp[l][r] = minimum turns to print substring filtered[l..=r]
        let mut dp = vec![vec![0usize; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }

        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                // worst case: print filtered[r] separately
                let mut best = dp[l][r - 1] + 1;

                // try to merge printing of filtered[r] with a previous same character
                for k in l..r {
                    if filtered[k] == filtered[r] {
                        let val = if k + 1 <= r - 1 {
                            dp[l][k] + dp[k + 1][r - 1]
                        } else {
                            dp[l][k]
                        };
                        if val < best {
                            best = val;
                        }
                    }
                }

                dp[l][r] = best;
            }
        }

        dp[0][n - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (strange-printer s)
  (-> string? exact-integer?)
  (let* ((remove-consecutive
          (lambda (str)
            (let ((len (string-length str)))
              (let loop ((i 0) (res ""))
                (if (= i len)
                    res
                    (let* ((c (string-ref str i))
                           (last-char (if (> (string-length res) 0)
                                          (string-ref res (- (string-length res) 1))
                                          #\null))
                           (new-res (if (and (not (char=? last-char #\null))
                                            (char=? c last-char))
                                        res
                                        (string-append res (string c)))))
                      (loop (+ i 1) new-res)))))))
         (t (remove-consecutive s))
         (n (string-length t))
         (chars (string->list t))
         (memo (let ((m (make-vector n)))
                 (do ((i 0 (+ i 1))) ((= i n))
                   (vector-set! m i (make-vector n -1)))
                 m))
         (dp
          (letrec ((f (lambda (l r)
                        (cond [(> l r) 0]
                              [else
                               (let ((cached (vector-ref (vector-ref memo l) r)))
                                 (if (not (= cached -1))
                                     cached
                                     (begin
                                       (define ans (+ 1 (f (+ l 1) r)))
                                       (do ((k (+ l 1) (+ k 1))) ((> k r))
                                         (when (char=? (list-ref chars l) (list-ref chars k))
                                           (let ((cand (+ (f l (- k 1)) (f (+ k 1) r))))
                                             (set! ans (if (< cand ans) cand ans)))))
                                       (vector-set! (vector-ref memo l) r ans)
                                       ans)))))))
            f)))
    (if (= n 0) 0 (dp 0 (- n 1)))))
```

## Erlang

```erlang
-module(solution).
-export([strange_printer/1]).

-spec strange_printer(S :: unicode:unicode_binary()) -> integer().
strange_printer(S) ->
    Chars = binary_to_list(S),
    Unique = remove_duplicates(Chars),
    N = length(Unique),
    case N of
        0 -> 0;
        _ ->
            Tuple = list_to_tuple(Unique),
            {Ans, _} = min_turns(1, N, Tuple, #{}),
            Ans
    end.

remove_duplicates([]) -> [];
remove_duplicates([H|T]) -> remove_dup(T, H, [H]).

remove_dup([], _, Acc) ->
    lists:reverse(Acc);
remove_dup([H|T], Prev, Acc) ->
    if H =:= Prev ->
            remove_dup(T, Prev, Acc);
       true ->
            remove_dup(T, H, [H|Acc])
    end.

min_turns(I, J, _Tuple, Memo) when I > J ->
    {0, Memo};
min_turns(I, J, Tuple, Memo) ->
    Key = {I, J},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            {NextVal, Memo1} = min_turns(I + 1, J, Tuple, Memo),
            Base = 1 + NextVal,
            CharI = element(I, Tuple),
            {Best, Memo2} = loop_k(I, I + 1, J, CharI, Base, Tuple, Memo1),
            NewMemo = maps:put(Key, Best, Memo2),
            {Best, NewMemo}
    end.

loop_k(_I, K, _J, _CharI, MinAcc, _Tuple, Memo) when K > _J ->
    {MinAcc, Memo};
loop_k(I, K, J, CharI, MinAcc, Tuple, Memo) ->
    CharK = element(K, Tuple),
    if CharK == CharI ->
            {Left, MemoL} = min_turns(I, K - 1, Tuple, Memo),
            {Right, MemoR} = min_turns(K + 1, J, Tuple, MemoL),
            Cand = Left + Right,
            NewMin = if Cand < MinAcc -> Cand; true -> MinAcc end,
            loop_k(I, K + 1, J, CharI, NewMin, Tuple, MemoR);
       true ->
            loop_k(I, K + 1, J, CharI, MinAcc, Tuple, Memo)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec strange_printer(s :: String.t()) :: integer
  def strange_printer(s) do
    compressed = compress(s)
    n = String.length(compressed)

    if n == 0 do
      0
    else
      chars = compressed |> String.graphemes() |> List.to_tuple()
      {result, _} = dfs(chars, 0, n - 1, %{})
      result
    end
  end

  defp compress(s) do
    s
    |> String.graphemes()
    |> Enum.chunk_by(& &1)
    |> Enum.map(&hd/1)
    |> Enum.join()
  end

  defp dfs(chars, i, j, memo) when i > j do
    {0, memo}
  end

  defp dfs(chars, i, j, memo) do
    key = {i, j}

    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        # Print chars[i] separately then solve the rest
        {next_val, memo1} = dfs(chars, i + 1, j, memo)
        best = next_val + 1

        {best_final, memo2} =
          Enum.reduce((i + 1)..j, {best, memo1}, fn k, {cur_best, mem_acc} ->
            if elem(chars, k) == elem(chars, i) do
              {left, mem_left} = dfs(chars, i, k - 1, mem_acc)
              {right, mem_right} = dfs(chars, k + 1, j, mem_left)
              total = left + right

              new_best = if total < cur_best, do: total, else: cur_best
              {new_best, mem_right}
            else
              {cur_best, mem_acc}
            end
          end)

        memo_updated = Map.put(memo2, key, best_final)
        {best_final, memo_updated}
    end
  end
end
```
