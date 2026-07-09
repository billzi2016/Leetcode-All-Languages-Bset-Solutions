# 3335. Total Characters in String After Transformations I

## Cpp

```cpp
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        const int MOD = 1000000007;
        vector<long long> cnt(26, 0), nxt(26, 0);
        for (char ch : s) cnt[ch - 'a']++;
        for (int step = 0; step < t; ++step) {
            nxt[0] = cnt[25] % MOD;                                   // a <- z
            nxt[1] = (cnt[25] + cnt[0]) % MOD;                         // b <- z + a
            for (int i = 2; i < 26; ++i) {
                nxt[i] = cnt[i - 1] % MOD;                             // others <- previous char
            }
            cnt.swap(nxt);
        }
        long long ans = 0;
        for (long long v : cnt) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return static_cast<int>(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int lengthAfterTransformations(String s, int t) {
        long[] cnt = new long[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        long[] nxt = new long[26];
        for (int step = 0; step < t; step++) {
            nxt[0] = cnt[25] % MOD;
            nxt[1] = (cnt[25] + cnt[0]) % MOD;
            for (int c = 2; c < 26; c++) {
                nxt[c] = cnt[c - 1] % MOD;
            }
            // swap references
            long[] temp = cnt;
            cnt = nxt;
            nxt = temp;
        }
        long ans = 0;
        for (long v : cnt) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for _ in range(t):
            nxt = [0] * 26
            # 'a' comes from previous 'z'
            nxt[0] = cnt[25] % MOD
            # 'b' comes from previous 'a' and 'z'
            nxt[1] = (cnt[0] + cnt[25]) % MOD
            # other letters shift from previous character
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = [x % MOD for x in nxt]

        return sum(cnt) % MOD
```

## Python3

```python
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        for _ in range(t):
            nxt = [0] * 26
            # a comes from previous z
            nxt[0] = cnt[25] % MOD
            # b comes from previous z and a
            nxt[1] = (cnt[25] + cnt[0]) % MOD
            # other letters shift from previous character
            for c in range(2, 26):
                nxt[c] = cnt[c - 1]
            cnt = nxt

        return sum(cnt) % MOD
```

## C

```c
int lengthAfterTransformations(char* s, int t) {
    const long long MOD = 1000000007LL;
    long long cnt[26] = {0}, nxt[26];
    for (char *p = s; *p; ++p) {
        cnt[*p - 'a']++;
    }
    while (t--) {
        nxt[0] = cnt[25] % MOD;
        nxt[1] = (cnt[25] + cnt[0]) % MOD;
        for (int c = 2; c < 26; ++c) {
            nxt[c] = cnt[c - 1];
        }
        for (int c = 0; c < 26; ++c) {
            cnt[c] = nxt[c] % MOD;
        }
    }
    long long ans = 0;
    for (int c = 0; c < 26; ++c) {
        ans += cnt[c];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int LengthAfterTransformations(string s, int t)
    {
        long[] cnt = new long[26];
        foreach (char ch in s)
            cnt[ch - 'a']++;

        long[] nxt = new long[26];

        for (int step = 0; step < t; ++step)
        {
            Array.Clear(nxt, 0, 26);

            // contributions from 'z'
            long zcnt = cnt[25] % MOD;
            if (zcnt != 0)
            {
                nxt[0] = (nxt[0] + zcnt) % MOD; // to 'a'
                nxt[1] = (nxt[1] + zcnt) % MOD; // to 'b'
            }

            // contributions from other letters
            for (int c = 0; c < 25; ++c)
            {
                long val = cnt[c] % MOD;
                if (val != 0)
                {
                    int idx = c + 1;
                    nxt[idx] = (nxt[idx] + val) % MOD;
                }
            }

            // swap arrays for next iteration
            var temp = cnt;
            cnt = nxt;
            nxt = temp;
        }

        long ans = 0;
        foreach (long v in cnt)
        {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} t
 * @return {number}
 */
var lengthAfterTransformations = function(s, t) {
    const MOD = 1000000007n;
    // count of each character a..z as BigInt
    let cnt = new Array(26).fill(0n);
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - 97] += 1n;
    }
    if (t === 0) {
        let sum = 0n;
        for (let v of cnt) sum = (sum + v) % MOD;
        return Number(sum);
    }
    for (let step = 0; step < t; ++step) {
        const nxt = new Array(26).fill(0n);
        // 'a' comes from previous 'z'
        nxt[0] = cnt[25];
        // 'b' comes from previous 'a' and previous 'z'
        nxt[1] = (cnt[0] + cnt[25]) % MOD;
        // other letters shift from previous character
        for (let c = 2; c < 26; ++c) {
            nxt[c] = cnt[c - 1];
        }
        // ensure modulo for all entries
        for (let c = 0; c < 26; ++c) {
            nxt[c] %= MOD;
        }
        cnt = nxt;
    }
    let ans = 0n;
    for (let v of cnt) {
        ans = (ans + v) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function lengthAfterTransformations(s: string, t: number): number {
    const MOD = 1000000007;
    let cur = new Array(26).fill(0);
    for (const ch of s) {
        cur[ch.charCodeAt(0) - 97] = (cur[ch.charCodeAt(0) - 97] + 1) % MOD;
    }
    for (let step = 0; step < t; ++step) {
        const nxt = new Array(26).fill(0);
        // 'a' comes from previous 'z'
        nxt[0] = cur[25];
        // 'b' comes from previous 'z' and 'a'
        nxt[1] = (cur[25] + cur[0]) % MOD;
        for (let c = 2; c < 26; ++c) {
            nxt[c] = cur[c - 1];
        }
        cur = nxt;
    }
    let ans = 0;
    for (const v of cur) {
        ans = (ans + v) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $t
     * @return Integer
     */
    function lengthAfterTransformations($s, $t) {
        $mod = 1000000007;
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97; // 'a' ASCII is 97
            $cnt[$idx] = ($cnt[$idx] + 1) % $mod;
        }
        for ($step = 0; $step < $t; $step++) {
            $nxt = array_fill(0, 26, 0);
            // 'a' comes from previous 'z'
            $nxt[0] = $cnt[25];
            // 'b' comes from previous 'a' and 'z'
            $nxt[1] = ($cnt[0] + $cnt[25]) % $mod;
            // other letters shift
            for ($c = 2; $c < 26; $c++) {
                $nxt[$c] = $cnt[$c - 1];
            }
            $cnt = $nxt;
        }
        $ans = 0;
        foreach ($cnt as $v) {
            $ans = ($ans + $v) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int) -> Int {
        let MOD = 1_000_000_007
        var cnt = [Int](repeating: 0, count: 26)
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value - 97)
            if idx >= 0 && idx < 26 {
                cnt[idx] += 1
                if cnt[idx] >= MOD { cnt[idx] -= MOD }
            }
        }
        var cur = cnt.map { $0 % MOD }
        for _ in 0..<t {
            var nxt = [Int](repeating: 0, count: 26)
            let z = cur[25]
            nxt[0] = z
            nxt[1] = (z + cur[0]) % MOD
            if 2 < 26 {
                for i in 2..<26 {
                    nxt[i] = cur[i - 1]
                }
            }
            cur = nxt
        }
        var total = 0
        for v in cur {
            total += v
            if total >= MOD { total -= MOD }
        }
        return total % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthAfterTransformations(s: String, t: Int): Int {
        val MOD = 1_000_000_007L
        var cur = LongArray(26)
        for (ch in s) {
            cur[ch - 'a'] = (cur[ch - 'a'] + 1) % MOD
        }
        repeat(t) {
            val nxt = LongArray(26)
            nxt[0] = cur[25] % MOD
            nxt[1] = (cur[25] + cur[0]) % MOD
            for (c in 2 until 26) {
                nxt[c] = cur[c - 1]
            }
            cur = nxt
        }
        var ans = 0L
        for (v in cur) {
            ans += v
            if (ans >= MOD) ans -= MOD
        }
        ans %= MOD
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int lengthAfterTransformations(String s, int t) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      int idx = s.codeUnitAt(i) - 97;
      cnt[idx] = (cnt[idx] + 1) % _mod;
    }

    for (int step = 0; step < t; ++step) {
      List<int> nxt = List.filled(26, 0);
      // 'a' comes only from previous 'z'
      nxt[0] = cnt[25];
      // 'b' comes from previous 'a' and 'z'
      nxt[1] = (cnt[0] + cnt[25]) % _mod;
      for (int c = 2; c < 26; ++c) {
        nxt[c] = cnt[c - 1];
      }
      cnt = nxt;
    }

    int ans = 0;
    for (int v in cnt) {
      ans += v;
      if (ans >= _mod) ans -= _mod;
    }
    return ans % _mod;
  }
}
```

## Golang

```go
func lengthAfterTransformations(s string, t int) int {
	const MOD int64 = 1000000007
	cnt := make([]int64, 26)
	for _, ch := range s {
		cnt[ch-'a']++
	}
	for i := 0; i < t; i++ {
		nxt := make([]int64, 26)
		nxt[0] = cnt[25] % MOD
		nxt[1] = (cnt[25] + cnt[0]) % MOD
		for c := 2; c < 26; c++ {
			nxt[c] = cnt[c-1] % MOD
		}
		cnt = nxt
	}
	var ans int64
	for _, v := range cnt {
		ans = (ans + v) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def length_after_transformations(s, t)
  mod = 1_000_000_007
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }

  t.times do
    nxt = Array.new(26, 0)
    nxt[0] = cnt[25] % mod
    nxt[1] = (cnt[25] + cnt[0]) % mod
    i = 2
    while i < 26
      nxt[i] = cnt[i - 1] % mod
      i += 1
    end
    cnt = nxt
  end

  cnt.reduce(0) { |sum, v| (sum + v) % mod }
end
```

## Scala

```scala
object Solution {
    def lengthAfterTransformations(s: String, t: Int): Int = {
        val MOD = 1000000007L
        var cur = new Array[Long](26)
        for (ch <- s) {
            cur(ch - 'a') = (cur(ch - 'a') + 1) % MOD
        }
        var nxt = new Array[Long](26)

        var i = 0
        while (i < t) {
            nxt(0) = cur(25)
            nxt(1) = (cur(25) + cur(0)) % MOD
            var c = 2
            while (c < 26) {
                nxt(c) = cur(c - 1)
                c += 1
            }
            // swap references for next iteration
            val temp = cur
            cur = nxt
            nxt = temp
            i += 1
        }

        var sum = 0L
        var idx = 0
        while (idx < 26) {
            sum += cur(idx)
            if (sum >= MOD) sum -= MOD
            idx += 1
        }
        (sum % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i64; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        for _ in 0..t as usize {
            let mut nxt = [0i64; 26];
            // 'a' comes from previous 'z'
            nxt[0] = cnt[25] % MOD;
            // 'b' comes from previous 'z' and previous 'a'
            nxt[1] = (cnt[25] + cnt[0]) % MOD;
            // other letters shift from the previous one
            for i in 2..26 {
                nxt[i] = cnt[i - 1] % MOD;
            }
            cnt = nxt;
        }
        let mut ans: i64 = 0;
        for &v in cnt.iter() {
            ans += v;
            if ans >= MOD {
                ans -= MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define MOD 1000000007)

(define/contract (length-after-transformations s t)
  (-> string? exact-integer? exact-integer?)
  (let ((cnt (make-vector 26 0)))
    ;; initial frequencies
    (for ([i (in-range (string-length s))])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    ;; apply t transformations
    (for ([step (in-range t)])
      (let ((nxt (make-vector 26 0)))
        (vector-set! nxt 0 (modulo (vector-ref cnt 25) MOD))
        (vector-set! nxt 1 (modulo (+ (vector-ref cnt 25) (vector-ref cnt 0)) MOD))
        (for ([c (in-range 2 26)])
          (vector-set! nxt c (modulo (vector-ref cnt (- c 1)) MOD)))
        (set! cnt nxt)))
    ;; sum counts
    (let ((ans 0))
      (for ([i (in-range 26)])
        (set! ans (modulo (+ ans (vector-ref cnt i)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([length_after_transformations/2]).

-define(MOD, 1000000007).

length_after_transformations(S, T) ->
    ZeroList = lists:duplicate(26, 0),
    InitCnt = list_to_tuple(ZeroList),
    Chars = unicode:characters_to_list(S),
    Cnt0 = build_counts(Chars, InitCnt),
    loop(T, Cnt0).

build_counts([], Cnt) -> Cnt;
build_counts([Char | Rest], Cnt) ->
    Idx = Char - $a,
    Pos = Idx + 1,
    Old = element(Pos, Cnt),
    NewCnt = setelement(Pos, Cnt, (Old + 1) rem ?MOD),
    build_counts(Rest, NewCnt).

step({A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}) ->
    {Z, (Z + A) rem ?MOD, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y}.

loop(0, Cnt) ->
    sum_tuple(Cnt);
loop(T, Cnt) when T > 0 ->
    NewCnt = step(Cnt),
    loop(T - 1, NewCnt).

sum_tuple(Cnt) ->
    lists:foldl(fun(X, Acc) -> (X + Acc) rem ?MOD end, 0, tuple_to_list(Cnt)).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec length_after_transformations(s :: String.t(), t :: integer) :: integer
  def length_after_transformations(s, t) do
    # initial character frequencies
    cnt =
      s
      |> :binary.bin_to_list()
      |> Enum.reduce(List.duplicate(0, 26), fn code, acc ->
        idx = code - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    final_cnt =
      1..t
      |> Enum.reduce(cnt, fn _, cur ->
        a = Enum.at(cur, 25) |> rem(@mod)
        b = (Enum.at(cur, 25) + Enum.at(cur, 0)) |> rem(@mod)

        shifted =
          for i <- 2..25 do
            Enum.at(cur, i - 1) |> rem(@mod)
          end

        [a, b] ++ shifted
      end)

    final_cnt
    |> Enum.reduce(0, fn x, acc -> (acc + x) rem @mod end)
  end
end
```
