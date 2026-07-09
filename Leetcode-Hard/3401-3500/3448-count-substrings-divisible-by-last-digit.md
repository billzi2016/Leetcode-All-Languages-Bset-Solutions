# 3448. Count Substrings Divisible By Last Digit

## Cpp

```cpp
class Solution {
public:
    long long countSubstrings(string s) {
        const int MAXD = 9;
        vector<vector<long long>> cnt(MAXD + 1);
        for (int d = 1; d <= MAXD; ++d) cnt[d] = vector<long long>(d, 0);
        long long ans = 0;
        for (char ch : s) {
            int x = ch - '0';
            if (x != 0) {
                // single character substring
                ans += 1;
                // longer substrings ending here with last digit x
                for (int r = 0; r < x; ++r) {
                    if ((r * 10) % x == 0) ans += cnt[x][r];
                }
            }
            // update dp for all possible divisors
            for (int d = 1; d <= MAXD; ++d) {
                vector<long long> nxt(d, 0);
                for (int r = 0; r < d; ++r) {
                    int nr = (r * 10 + x) % d;
                    nxt[nr] += cnt[d][r];
                }
                // start new substring consisting only of current digit
                int nr2 = x % d;
                nxt[nr2] += 1;
                cnt[d].swap(nxt);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countSubstrings(String s) {
        long[][] cnt = new long[10][];
        for (int d = 1; d <= 9; ++d) {
            cnt[d] = new long[d];
        }
        long ans = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            int x = s.charAt(i) - '0';
            long[][] next = new long[10][];
            for (int d = 1; d <= 9; ++d) {
                next[d] = new long[d];
                long[] cur = cnt[d];
                if (cur != null) {
                    for (int r = 0; r < d; ++r) {
                        long val = cur[r];
                        if (val == 0) continue;
                        int nr = (r * 10 + x) % d;
                        next[d][nr] += val;
                    }
                }
                int nr2 = x % d;
                next[d][nr2] += 1; // start new substring at i
            }
            cnt = next;
            if (x != 0) {
                ans += cnt[x][0];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # cnt[d][r] = number of substrings ending at previous position
        # with remainder r modulo d (1 <= d <= 9)
        cnt = [None] + [[0] * d for d in range(1, 10)]
        ans = 0
        for ch in s:
            x = ord(ch) - 48  # int conversion faster
            new_cnt = [None] + [[0] * d for d in range(1, 10)]
            for d in range(1, 10):
                cur = cnt[d]
                nd = new_cnt[d]
                # extend existing substrings
                for r in range(d):
                    c = cur[r]
                    if c:
                        nr = (r * 10 + x) % d
                        nd[nr] += c
                # start a new substring consisting only of current digit
                nd[x % d] += 1
            if x != 0:
                ans += new_cnt[x][0]
            cnt = new_cnt
        return ans
```

## Python3

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        # cnt[d][r] = number of substrings ending at previous position
        # with remainder r modulo d (1 <= d <= 9)
        cnt = [None] + [[0] * d for d in range(1, 10)]
        ans = 0
        for ch in s:
            x = ord(ch) - 48  # int conversion faster
            new_cnt = [None] + [[0] * d for d in range(1, 10)]
            for d in range(1, 10):
                old = cnt[d]
                cur = new_cnt[d]
                mod = d
                # propagate previous substrings
                for r in range(mod):
                    v = old[r]
                    if v:
                        nr = (r * 10 + x) % mod
                        cur[nr] += v
                # start new substring consisting of only current digit
                cur[x % mod] += 1
            cnt = new_cnt
            if x != 0:
                ans += cnt[x][0]
        return ans
```

## C

```c
#include <string.h>

long long countSubstrings(char* s) {
    int n = (int)strlen(s);
    long long cnt[10][9] = {0};
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        int x = s[i] - '0';
        for (int d = 1; d <= 9; ++d) {
            long long tmp[9] = {0};
            for (int rem = 0; rem < d; ++rem) {
                long long c = cnt[d][rem];
                if (c) {
                    int new_rem = (rem * 10 + x) % d;
                    tmp[new_rem] += c;
                }
            }
            int single_rem = x % d;
            tmp[single_rem] += 1;
            for (int rem = 0; rem < d; ++rem) {
                cnt[d][rem] = tmp[rem];
            }
        }
        if (x != 0) {
            ans += cnt[x][0];
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountSubstrings(string s) {
        var cnt = new long[10][];
        for (int d = 1; d <= 9; d++) cnt[d] = new long[d];

        long ans = 0;
        foreach (char ch in s) {
            int digit = ch - '0';
            var newCnt = new long[10][];
            for (int d = 1; d <= 9; d++) {
                int size = d;
                var prev = cnt[d];
                var cur = new long[size];

                // extend previous substrings
                for (int rem = 0; rem < size; rem++) {
                    long c = prev[rem];
                    if (c == 0) continue;
                    int newRem = (rem * 10 + digit) % d;
                    cur[newRem] += c;
                }

                // single-character substring
                int singleRem = digit % d;
                cur[singleRem] += 1;

                newCnt[d] = cur;
            }
            cnt = newCnt;

            if (digit != 0) {
                ans += cnt[digit][0];
            }
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
var countSubstrings = function(s) {
    // cnt[d][r] = number of substrings ending at previous position with remainder r modulo d
    const cnt = Array(10);
    for (let d = 1; d <= 9; d++) cnt[d] = new Array(d).fill(0);
    let ans = 0;
    
    for (const ch of s) {
        const x = ch.charCodeAt(0) - 48; // digit value
        const next = Array(10);
        
        for (let d = 1; d <= 9; d++) {
            const nd = new Array(d).fill(0);
            const prev = cnt[d];
            // extend previous substrings by current digit
            for (let r = 0; r < d; r++) {
                const c = prev[r];
                if (c !== 0) {
                    const nr = (r * 10 + x) % d;
                    nd[nr] += c;
                }
            }
            // substring consisting of only current digit
            nd[x % d] += 1;
            next[d] = nd;
        }
        
        for (let d = 1; d <= 9; d++) cnt[d] = next[d];
        
        if (x !== 0) {
            ans += cnt[x][0]; // substrings ending here divisible by their last digit
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countSubstrings(s: string): number {
    const cnt: number[][] = Array.from({ length: 10 }, (_, i) => (i === 0 ? [] : new Array(i).fill(0)));
    let ans = 0;
    for (const ch of s) {
        const x = ch.charCodeAt(0) - 48; // digit value
        const newCnt: number[][] = Array.from({ length: 10 }, (_, i) => (i === 0 ? [] : new Array(i).fill(0)));
        for (let m = 1; m <= 9; ++m) {
            const oldArr = cnt[m];
            const curArr = newCnt[m];
            // extend previous substrings
            for (let r = 0; r < m; ++r) {
                const nr = (r * 10 + x) % m;
                curArr[nr] += oldArr[r];
            }
            // single digit substring
            curArr[x % m] += 1;
        }
        if (x !== 0) {
            ans += newCnt[x][0];
        }
        for (let m = 1; m <= 9; ++m) {
            cnt[m] = newCnt[m];
        }
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
    function countSubstrings($s) {
        $n = strlen($s);
        // cnt[k][r] = number of substrings ending at previous position with remainder r modulo k
        $cnt = [];
        for ($k = 1; $k <= 9; $k++) {
            $cnt[$k] = array_fill(0, $k, 0);
        }

        $ans = 0;

        for ($i = 0; $i < $n; $i++) {
            $digit = intval($s[$i]);

            // prepare new counts for substrings ending at current position
            $newCnt = [];
            for ($k = 1; $k <= 9; $k++) {
                $newCnt[$k] = array_fill(0, $k, 0);
            }

            // extend previous substrings
            foreach ($cnt as $k => $arr) {
                $modSize = $k;
                for ($r = 0; $r < $modSize; $r++) {
                    $c = $cnt[$k][$r];
                    if ($c == 0) continue;
                    $newR = ($r * 10 + $digit) % $k;
                    $newCnt[$k][$newR] += $c;
                }
            }

            // add substrings consisting of only the current digit
            for ($k = 1; $k <= 9; $k++) {
                $newR = $digit % $k;
                $newCnt[$k][$newR] += 1;
            }

            // if last digit is non‑zero, count those with remainder 0 modulo that digit
            if ($digit != 0) {
                $ans += $newCnt[$digit][0];
            }

            // move to next position
            $cnt = $newCnt;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubstrings(_ s: String) -> Int {
        var cnt = Array(repeating: [Int64](), count: 10)
        for d in 1...9 {
            cnt[d] = Array(repeating: 0, count: d)
        }
        var answer: Int64 = 0
        for ch in s {
            let x = Int(ch.unicodeScalars.first!.value - 48)   // current digit
            var newCnt = Array(repeating: [Int64](), count: 10)
            for d in 1...9 {
                newCnt[d] = Array(repeating: 0, count: d)
                let oldArr = cnt[d]
                if !oldArr.isEmpty {
                    for r in 0..<d {
                        let val = oldArr[r]
                        if val != 0 {
                            let nr = (r * 10 + x) % d
                            newCnt[d][nr] += val
                        }
                    }
                }
                // start a new substring consisting only of current digit
                let nr2 = x % d
                newCnt[d][nr2] += 1
            }
            if x != 0 {
                answer += newCnt[x][0]
            }
            cnt = newCnt
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String): Long {
        var cnt = Array(10) { LongArray(0) }
        for (d in 1..9) cnt[d] = LongArray(d)
        var ans = 0L
        for (ch in s) {
            val x = ch - '0'
            val newCnt = Array(10) { LongArray(0) }
            for (d in 1..9) {
                val prev = cnt[d]
                val cur = LongArray(d)
                for (rem in 0 until d) {
                    val c = prev[rem]
                    if (c != 0L) {
                        val newRem = ((rem * 10 + x) % d)
                        cur[newRem] += c
                    }
                }
                if (x != 0 && d == x) {
                    cur[0] += 1L
                }
                newCnt[d] = cur
            }
            if (x != 0) {
                ans += newCnt[x][0]
            }
            cnt = newCnt
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countSubstrings(String s) {
    // counts[d] holds a list of size d, where counts[d][r] is the number
    // of substrings ending at previous index with remainder r modulo d.
    List<List<int>> counts = List.generate(10, (_) => []);
    int answer = 0;
    for (int i = 0; i < s.length; i++) {
      int digit = s.codeUnitAt(i) - 48;
      // Update DP for each possible divisor d (1..9)
      for (int d = 1; d <= 9; d++) {
        List<int> cur = counts[d];
        List<int> next = List.filled(d, 0);
        if (cur.isNotEmpty) {
          for (int r = 0; r < d; r++) {
            int cnt = cur[r];
            if (cnt != 0) {
              int nr = ((r * 10) + digit) % d;
              next[nr] += cnt;
            }
          }
        }
        // Substring consisting of only the current digit
        int singleRem = digit % d;
        next[singleRem] += 1;
        counts[d] = next;
      }
      if (digit != 0) {
        answer += counts[digit][0];
      }
    }
    return answer;
  }
}
```

## Golang

```go
func countSubstrings(s string) int64 {
    // cnt[d][r] = number of substrings ending at previous index with remainder r modulo d
    cnt := make([][]int64, 10)
    for d := 1; d <= 9; d++ {
        cnt[d] = make([]int64, d)
    }
    var ans int64

    for _, ch := range s {
        x := int(ch - '0')
        // newCnt will hold counts for substrings ending at current index
        newCnt := make([][]int64, 10)
        for d := 1; d <= 9; d++ {
            newCnt[d] = make([]int64, d)
        }

        // extend previous substrings by current digit
        for d := 1; d <= 9; d++ {
            for r := 0; r < d; r++ {
                c := cnt[d][r]
                if c == 0 {
                    continue
                }
                nr := (r*10 + x) % d
                newCnt[d][nr] += c
            }
        }

        // single‑character substring
        if x != 0 {
            newCnt[x][0]++
        }

        // count substrings ending here whose value is divisible by last digit
        if x != 0 {
            ans += newCnt[x][0]
        }

        cnt = newCnt
    }
    return ans
}
```

## Ruby

```ruby
def count_substrings(s)
  dp = Array.new(10) { [] }
  (1..9).each { |d| dp[d] = Array.new(d, 0) }

  ans = 0

  s.each_byte do |ch|
    digit = ch - 48
    new_dp = Array.new(10)

    (1..9).each do |d|
      cur = Array.new(d, 0)
      prev = dp[d]

      (0...d).each do |r|
        cnt = prev[r]
        next if cnt == 0
        nr = (r * 10 + digit) % d
        cur[nr] += cnt
      end

      cur[digit % d] += 1
      new_dp[d] = cur
    end

    ans += new_dp[digit][0] if digit != 0
    dp = new_dp
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countSubstrings(s: String): Long = {
        var cnt = Array.ofDim[Long](10, 9) // cnt(d)(r)
        var ans: Long = 0L
        var i = 0
        val n = s.length
        while (i < n) {
            val x = s.charAt(i) - '0'
            val newCnt = Array.ofDim[Long](10, 9)
            var d = 1
            while (d <= 9) {
                // substring consisting only of current character
                val rSingle = x % d
                newCnt(d)(rSingle) += 1L

                var r = 0
                while (r < d) {
                    val cur = cnt(d)(r)
                    if (cur != 0) {
                        val nr = (r * 10 + x) % d
                        newCnt(d)(nr) += cur
                    }
                    r += 1
                }
                d += 1
            }
            if (x != 0) {
                ans += newCnt(x)(0)
            }
            cnt = newCnt
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_substrings(s: String) -> i64 {
        // cnt[d][r] = number of substrings ending at previous index
        // with remainder r modulo d (1 <= d <= 9, 0 <= r < d)
        let mut cnt = [[0i64; 9]; 10];
        let mut ans: i64 = 0;
        for &ch in s.as_bytes() {
            let x = (ch - b'0') as usize;
            let mut new_cnt = [[0i64; 9]; 10];
            for d in 1..=9 {
                // extend previous substrings
                for r in 0..d {
                    let val = cnt[d][r];
                    if val != 0 {
                        let new_mod = (r * 10 + x) % d;
                        new_cnt[d][new_mod] += val;
                    }
                }
                // add the single‑character substring ending here
                let mod_single = x % d;
                new_cnt[d][mod_single] += 1;
            }
            cnt = new_cnt;
            if x != 0 {
                ans += cnt[x][0];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-substrings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         ;; previous DP vectors for remainders modulo k (1..9)
         (prev (make-vector 10 #f)))
    ;; initialize prev vectors with zeros
    (for ([k (in-range 1 10)])
      (vector-set! prev k (make-vector k 0)))
    (define ans 0)
    (for ([idx (in-range n)])
      (define x (- (char->integer (string-ref s idx))
                   (char->integer #\0))) ; current digit
      ;; current DP vectors
      (define cur (make-vector 10 #f))
      (for ([k (in-range 1 10)])
        (vector-set! cur k (make-vector k 0)))
      ;; update for each divisor k
      (for ([k (in-range 1 10)])
        (let* ((prevvec (vector-ref prev k))
               (curvec  (vector-ref cur k)))
          ;; extend previous substrings
          (for ([r (in-range k)])
            (define cnt (vector-ref prevvec r))
            (when (> cnt 0)
              (define newr (modulo (+ (* r 10) x) k))
              (vector-set! curvec newr (+ (vector-ref curvec newr) cnt))))
          ;; add substring consisting only of current digit
          (define r1 (modulo x k))
          (vector-set! curvec r1 (+ (vector-ref curvec r1) 1))))
      ;; count substrings ending at idx whose last digit is non‑zero and divisible by it
      (when (> x 0)
        (define curvec (vector-ref cur x))
        (set! ans (+ ans (vector-ref curvec 0))))
      ;; prepare for next iteration
      (set! prev cur))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_substrings/1]).

-spec count_substrings(S :: unicode:unicode_binary()) -> integer().
count_substrings(S) ->
    InitCnt = init_cnt(),
    process(S, InitCnt, 0).

init_cnt() ->
    [erlang:make_tuple(K, 0) || K <- lists:seq(1,9)].

process(<<>>, _CntList, Ans) ->
    Ans;
process(<<Char, Rest/binary>>, CntList, Ans) ->
    X = Char - $0,
    {NewCntList, Add} = update_all(CntList, X),
    process(Rest, NewCntList, Ans + Add).

update_all(CntList, X) ->
    update_k(1, CntList, X, 0, []).

update_k(K, CntList, X, AccAdd, AccNew) when K =< 9 ->
    OldTuple = lists:nth(K, CntList),
    NewTuple0 = make_new_tuple(K, OldTuple, X),
    Rsingle = X rem K,
    PrevVal = element(Rsingle + 1, NewTuple0),
    UpdatedTuple = setelement(Rsingle + 1, NewTuple0, PrevVal + 1),
    Add = case K of
        X -> element(1, UpdatedTuple);
        _ -> 0
    end,
    update_k(K + 1, CntList, X, AccAdd + Add, [UpdatedTuple | AccNew]);
update_k(_, _, _, AccAdd, AccNew) ->
    {lists:reverse(AccNew), AccAdd}.

make_new_tuple(K, OldTuple, X) ->
    make_new_tuple(0, K, OldTuple, X, erlang:make_tuple(K, 0)).

make_new_tuple(R, K, OldTuple, X, Acc) when R < K ->
    Cnt = element(R + 1, OldTuple),
    NewR = (R * 10 + X) rem K,
    Prev = element(NewR + 1, Acc),
    UpdatedAcc = setelement(NewR + 1, Acc, Prev + Cnt),
    make_new_tuple(R + 1, K, OldTuple, X, UpdatedAcc);
make_new_tuple(_, _, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t()) :: integer()
  def count_substrings(s) do
    digits = String.to_charlist(s) |> Enum.map(&(&1 - ?0))

    # initial counts: for each divisor k (1..9), a list of length k filled with zeros
    init_counts =
      for k <- 1..9, into: %{} do
        {k, List.duplicate(0, k)}
      end

    {_final_counts, answer} =
      Enum.reduce(digits, {init_counts, 0}, fn digit, {cnts, ans} ->
        new_cnts =
          Enum.reduce(1..9, %{}, fn k, acc_map ->
            old_list = Map.get(cnts, k)
            size = k
            # start with zeros list
            base = List.duplicate(0, size)

            # extend previous substrings
            extended =
              Enum.with_index(old_list)
              |> Enum.reduce(base, fn {c, r}, lst ->
                if c == 0 do
                  lst
                else
                  new_r = rem(r * 10 + digit, k)
                  List.update_at(lst, new_r, &(&1 + c))
                end
              end)

            # add the substring consisting only of current digit
            single_r = rem(digit, k)
            updated = List.update_at(extended, single_r, &(&1 + 1))

            Map.put(acc_map, k, updated)
          end)

        ans =
          if digit != 0 do
            cnt_list = Map.get(new_cnts, digit)
            Enum.at(cnt_list, 0) + ans
          else
            ans
          end

        {new_cnts, ans}
      end)

    answer
  end
end
```
