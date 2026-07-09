# 2156. Find Substring With Given Hash Value

## Cpp

```cpp
class Solution {
public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        int n = s.size();
        long long cur = 0;
        long long powK = 1 % modulo;
        for (int i = 0; i < k; ++i) {
            powK = (powK * power) % modulo;
        }
        int bestIdx = -1;
        for (int i = n - 1; i >= 0; --i) {
            int val = s[i] - 'a' + 1;
            cur = (cur * power + val) % modulo;
            if (i + k < n) {
                long long outVal = s[i + k] - 'a' + 1;
                cur = (cur - outVal * powK % modulo + modulo) % modulo;
            }
            if (n - i >= k && cur == hashValue) {
                bestIdx = i; // leftmost will overwrite later
            }
        }
        return s.substr(bestIdx, k);
    }
};
```

## Java

```java
class Solution {
    public String subStrHash(String s, int power, int modulo, int k, int hashValue) {
        int n = s.length();
        long[] pow = new long[k];
        pow[0] = 1 % modulo;
        for (int i = 1; i < k; i++) {
            pow[i] = (pow[i - 1] * power) % modulo;
        }

        int start = n - k;
        long cur = 0;
        for (int j = 0; j < k; j++) {
            long val = s.charAt(start + j) - 'a' + 1;
            cur = (cur + val * pow[j]) % modulo;
        }

        int ansIdx = -1;
        if (cur == hashValue) {
            ansIdx = start;
        }

        for (int i = start - 1; i >= 0; i--) {
            long outVal = s.charAt(i + k) - 'a' + 1;
            cur = (cur - outVal * pow[k - 1]) % modulo;
            if (cur < 0) cur += modulo;

            long inVal = s.charAt(i) - 'a' + 1;
            cur = (inVal + power * cur) % modulo;
            if (cur == hashValue) {
                ansIdx = i; // earlier index overrides
            }
        }

        return s.substring(ansIdx, ansIdx + k);
    }
}
```

## Python

```python
class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        n = len(s)
        cur = 0
        ans = 0
        power_k = pow(power, k, modulo)  # power^k % modulo

        for i in range(n - 1, -1, -1):
            cur = ((ord(s[i]) - ord('a') + 1) + cur * power) % modulo
            if i + k < n:
                out_val = ord(s[i + k]) - ord('a') + 1
                cur = (cur - out_val * power_k) % modulo
            if i + k <= n and cur == hashValue:
                ans = i

        return s[ans: ans + k]
```

## Python3

```python
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        cur = 0
        ans = n  # placeholder for earliest index
        pow_k = pow(power, k, modulo)  # power^k % modulo
        cnt = 0
        for i in range(n - 1, -1, -1):
            val = ord(s[i]) - 96  # 'a' -> 1
            cur = (cur * power + val) % modulo
            cnt += 1
            if cnt > k:
                out_val = ord(s[i + k]) - 96
                cur = (cur - out_val * pow_k) % modulo
            if cnt >= k and cur == hashValue:
                ans = i
        return s[ans:ans + k]
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* subStrHash(char* s, int power, int modulo, int k, int hashValue) {
    int n = (int)strlen(s);
    
    long long pk = 1;
    for (int i = 0; i < k; ++i)
        pk = (pk * power) % modulo;          // power^k mod modulo
    
    // initial hash for the last window [n-k, n-1]
    long long cur = 0;
    long long pw = 1;
    for (int j = n - k; j < n; ++j) {
        int val = s[j] - 'a' + 1;
        cur = (cur + val * pw) % modulo;
        pw = (pw * power) % modulo;
    }
    
    int ansIdx = n - k;
    if (cur == hashValue)
        ansIdx = n - k;
    
    // slide window leftwards
    for (int i = n - k - 1; i >= 0; --i) {
        int outVal = s[i + k] - 'a' + 1;               // character leaving the window
        cur = (cur - (outVal * pk) % modulo);
        if (cur < 0) cur += modulo;
        
        cur = (cur * power) % modulo;                  // shift powers
        
        int inVal = s[i] - 'a' + 1;                     // new character entering
        cur = (cur + inVal) % modulo;
        
        if (cur == hashValue)
            ansIdx = i;                                 // earlier occurrence found
    }
    
    char* res = (char*)malloc(k + 1);
    memcpy(res, s + ansIdx, k);
    res[k] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string SubStrHash(string s, int power, int modulo, int k, int hashValue) {
        int n = s.Length;
        long[] pow = new long[k];
        pow[0] = 1 % modulo;
        for (int i = 1; i < k; i++) {
            pow[i] = (pow[i - 1] * power) % modulo;
        }

        // hash of the last window
        int start = n - k;
        long cur = 0;
        for (int j = 0; j < k; j++) {
            int val = s[start + j] - 'a' + 1;
            cur = (cur + val * pow[j]) % modulo;
        }

        int ansIdx = start;
        if (cur == hashValue) ansIdx = start;

        for (int i = start - 1; i >= 0; i--) {
            int outVal = s[i + k] - 'a' + 1;
            cur = (cur - outVal * pow[k - 1]) % modulo;
            if (cur < 0) cur += modulo;
            cur = (cur * power) % modulo;
            int inVal = s[i] - 'a' + 1;
            cur = (cur + inVal) % modulo;

            if (cur == hashValue) {
                ansIdx = i; // earlier occurrence
            }
        }

        return s.Substring(ansIdx, k);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} power
 * @param {number} modulo
 * @param {number} k
 * @param {number} hashValue
 * @return {string}
 */
var subStrHash = function(s, power, modulo, k, hashValue) {
    const n = s.length;
    const p = BigInt(power);
    const mod = BigInt(modulo);
    const target = BigInt(hashValue);

    // precompute p^(k-1) % mod
    let powKMinus1 = 1n;
    for (let i = 0; i < k - 1; ++i) {
        powKMinus1 = (powKMinus1 * p) % mod;
    }

    // compute hash of the last window [n-k, n)
    let curHash = 0n;
    let curPow = 1n;
    for (let j = 0; j < k; ++j) {
        const idx = n - k + j;
        const val = BigInt(s.charCodeAt(idx) - 96);
        curHash = (curHash + val * curPow) % mod;
        curPow = (curPow * p) % mod;
    }

    let ansIdx = n - k; // default answer
    if (curHash === target) {
        ansIdx = n - k;
    }

    // slide window leftwards
    for (let i = n - k - 1; i >= 0; --i) {
        const outVal = BigInt(s.charCodeAt(i + k) - 96);
        curHash = (curHash - outVal * powKMinus1) % mod;
        if (curHash < 0n) curHash += mod;
        curHash = (curHash * p) % mod;
        const inVal = BigInt(s.charCodeAt(i) - 96);
        curHash = (curHash + inVal) % mod;

        if (curHash === target) {
            ansIdx = i; // earlier occurrence
        }
    }

    return s.substring(ansIdx, ansIdx + k);
};
```

## Typescript

```typescript
function subStrHash(s: string, power: number, modulo: number, k: number, hashValue: number): string {
    const n = s.length;
    const p = BigInt(power);
    const mod = BigInt(modulo);
    const target = BigInt(hashValue);

    // compute power^(k-1) % mod
    let powKMinus1 = 1n;
    for (let i = 0; i < k - 1; i++) {
        powKMinus1 = (powKMinus1 * p) % mod;
    }

    // initial hash for the last possible window [n-k, n-1]
    let cur = 0n;
    let mult = 1n;
    const startIdx = n - k;
    for (let j = 0; j < k; j++) {
        const val = BigInt(s.charCodeAt(startIdx + j) - 96);
        cur = (cur + val * mult) % mod;
        mult = (mult * p) % mod;
    }

    let ansIdx = startIdx;
    if (cur === target) ansIdx = startIdx;

    // slide window leftwards
    for (let i = startIdx - 1; i >= 0; i--) {
        const leftVal = BigInt(s.charCodeAt(i) - 96);
        const rightVal = BigInt(s.charCodeAt(i + k) - 96);

        let temp = cur - (rightVal * powKMinus1) % mod;
        if (temp < 0n) temp += mod;

        cur = (leftVal + (temp * p) % mod) % mod;

        if (cur === target) {
            ansIdx = i;
        }
    }

    return s.substring(ansIdx, ansIdx + k);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $power
     * @param Integer $modulo
     * @param Integer $k
     * @param Integer $hashValue
     * @return String
     */
    function subStrHash($s, $power, $modulo, $k, $hashValue) {
        $n = strlen($s);
        // power^k % modulo
        $powK = 1;
        for ($i = 0; $i < $k; $i++) {
            $powK = ($powK * $power) % $modulo;
        }

        // initial hash for the rightmost window of length k
        $start = $n - $k;
        $cur = 0;
        $pow = 1;
        for ($i = $start; $i < $n; $i++) {
            $val = ord($s[$i]) - 96; // 'a' -> 1
            $cur = ($cur + $val * $pow) % $modulo;
            $pow = ($pow * $power) % $modulo;
        }

        $ansStart = -1;
        if ($cur == $hashValue) {
            $ansStart = $start;
        }

        // slide window to the left
        for ($i = $start - 1; $i >= 0; $i--) {
            $valOut = ord($s[$i + $k]) - 96; // character leaving the window
            $cur = ($cur * $power) % $modulo;
            $remove = ($valOut * $powK) % $modulo;
            $cur -= $remove;
            if ($cur < 0) {
                $cur += $modulo;
            }
            $valIn = ord($s[$i]) - 96; // new character entering the window
            $cur = ($cur + $valIn) % $modulo;

            if ($cur == $hashValue) {
                $ansStart = $i; // earlier occurrence
            }
        }

        return substr($s, $ansStart, $k);
    }
}
```

## Swift

```swift
class Solution {
    func subStrHash(_ s: String, _ power: Int, _ modulo: Int, _ k: Int, _ hashValue: Int) -> String {
        let n = s.count
        var vals = [Int]()
        vals.reserveCapacity(n)
        for ch in s.utf8 {
            vals.append(Int(ch) - 96) // 'a' -> 1
        }
        func modMul(_ a: Int, _ b: Int) -> Int {
            return Int((Int64(a) * Int64(b)) % Int64(modulo))
        }
        // power^(k-1) % modulo
        var pPow = 1
        if k > 1 {
            for _ in 0..<(k - 1) {
                pPow = modMul(pPow, power)
            }
        }
        // initial hash for substring starting at n-k
        var cur = 0
        var mult = 1
        let startIdx = n - k
        for idx in startIdx..<n {
            let v = vals[idx]
            cur = (cur + modMul(v, mult)) % modulo
            mult = modMul(mult, power)
        }
        var ans = startIdx
        if cur == hashValue {
            ans = startIdx
        }
        if n - k > 0 {
            for start in stride(from: n - k - 1, through: 0, by: -1) {
                let oldVal = vals[start + k]
                var temp = cur - modMul(oldVal, pPow)
                temp %= modulo
                if temp < 0 { temp += modulo }
                cur = modMul(temp, power)
                let newVal = vals[start]
                cur = (cur + newVal) % modulo
                if cur == hashValue {
                    ans = start
                }
            }
        }
        let startPos = s.index(s.startIndex, offsetBy: ans)
        let endPos = s.index(startPos, offsetBy: k)
        return String(s[startPos..<endPos])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String {
        val n = s.length
        val mod = modulo.toLong()
        val p = power.toLong()
        var cur = 0L
        var powK = 1L
        repeat(k) { powK = (powK * p) % mod } // p^k
        
        var ansIdx = -1
        for (i in n - 1 downTo 0) {
            val v = (s[i] - 'a' + 1).toLong()
            cur = (cur * p + v) % mod
            if (i + k < n) {
                val outVal = (s[i + k] - 'a' + 1).toLong()
                cur = (cur - outVal * powK % mod + mod) % mod
            }
            if (i + k <= n && cur == hashValue.toLong()) {
                ansIdx = i
            }
        }
        return s.substring(ansIdx, ansIdx + k)
    }
}
```

## Dart

```dart
class Solution {
  String subStrHash(String s, int power, int modulo, int k, int hashValue) {
    int n = s.length;
    List<int> vals = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      vals[i] = s.codeUnitAt(i) - 96; // 'a' -> 1
    }

    // power^{k-1} % modulo
    int powKMinus1 = 1;
    for (int i = 0; i < k - 1; i++) {
      powKMinus1 = (powKMinus1 * power) % modulo;
    }

    // hash of the last possible substring (starting at n-k)
    int curHash = 0;
    int mult = 1;
    for (int j = 0; j < k; j++) {
      curHash = (curHash + vals[n - k + j] * mult) % modulo;
      mult = (mult * power) % modulo;
    }

    int answerStart = -1;
    if (curHash == hashValue) answerStart = n - k;

    // slide window leftwards
    for (int i = n - k - 1; i >= 0; i--) {
      int outVal = vals[i + k];
      curHash = (curHash - (outVal * powKMinus1) % modulo);
      if (curHash < 0) curHash += modulo;
      curHash = (curHash * power) % modulo;
      curHash = (curHash + vals[i]) % modulo;

      if (curHash == hashValue) answerStart = i;
    }

    return s.substring(answerStart, answerStart + k);
  }
}
```

## Golang

```go
func subStrHash(s string, power int, modulo int, k int, hashValue int) string {
    n := len(s)
    mod := int64(modulo)
    p := int64(power)

    // Compute power^k % mod
    powK := int64(1)
    for i := 0; i < k; i++ {
        powK = (powK * p) % mod
    }

    cur := int64(0)
    ansIdx := -1

    for i := n - 1; i >= 0; i-- {
        val := int64(s[i]-'a'+1)
        cur = (cur*p + val) % mod

        if i+k < n {
            outVal := int64(s[i+k]-'a'+1)
            cur = (cur - outVal*powK%mod + mod) % mod
        }

        if i <= n-k && cur == int64(hashValue) {
            ansIdx = i
        }
    }

    return s[ansIdx : ansIdx+k]
}
```

## Ruby

```ruby
def sub_str_hash(s, power, modulo, k, hash_value)
  n = s.length
  # compute power^k % modulo
  pk = 1
  k.times { pk = (pk * power) % modulo }

  cur = 0
  ans_start = -1

  (n - 1).downto(0) do |i|
    val = s.getbyte(i) - 96 # 'a' => 1, ..., 'z' => 26
    cur = (cur * power + val) % modulo

    if n - i > k
      out_val = s.getbyte(i + k) - 96
      cur = (cur - out_val * pk) % modulo
    end

    if n - i >= k && cur == hash_value
      ans_start = i
    end
  end

  s[ans_start, k]
end
```

## Scala

```scala
object Solution {
    def subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String = {
        val n = s.length
        val vals = new Array[Int](n)
        for (i <- 0 until n) {
            vals(i) = s.charAt(i) - 'a' + 1
        }
        val modLong = modulo.toLong
        val powLong = power.toLong
        var powerK: Long = 1L
        for (_ <- 0 until k) {
            powerK = (powerK * powLong) % modLong
        }
        var cur: Long = 0L
        var ansIdx = -1
        for (i <- (n - 1) to 0 by -1) {
            cur = (cur * powLong + vals(i)) % modLong
            if (i + k < n) {
                cur = (cur - (vals(i + k).toLong * powerK) % modLong + modLong) % modLong
            }
            if (i <= n - k && cur == hashValue.toLong) {
                ansIdx = i
            }
        }
        s.substring(ansIdx, ansIdx + k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sub_str_hash(s: String, power: i32, modulo: i32, k: i32, hash_value: i32) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let p = power as i64;
        let modv = modulo as i64;
        let target = hash_value as i64;
        let k_usize = k as usize;

        // compute power^k % modulo
        let mut power_k: i64 = 1;
        for _ in 0..k {
            power_k = (power_k * p) % modv;
        }

        let mut cur: i64 = 0;
        let mut ans_start: usize = 0;

        // iterate from right to left
        for idx_rev in (0..n).rev() {
            let val = (bytes[idx_rev] - b'a' + 1) as i64;
            cur = (cur * p + val) % modv;

            if n - idx_rev > k_usize {
                // remove the character that moves out of the window
                let out_idx = idx_rev + k_usize;
                let out_val = (bytes[out_idx] - b'a' + 1) as i64;
                cur = (cur + modv - (out_val * power_k % modv)) % modv;
            }

            if n - idx_rev >= k_usize && cur == target {
                ans_start = idx_rev;
            }
        }

        s[ans_start..ans_start + k_usize].to_string()
    }
}
```

## Racket

```racket
(define/contract (sub-str-hash s power modulo k hashValue)
  (-> string? exact-integer? exact-integer? exact-integer? exact-integer? string?)
  (let* ([n (string-length s)]
         [char-val (lambda (c) (- (char->integer c) 96))]
         ;; compute power^k mod modulo
         [power-k (let loop ([exp k] [result 1])
                    (if (= exp 0)
                        result
                        (loop (quotient exp 2)
                              (if (odd? exp)
                                  (modulo (* result power) modulo)
                                  result))
                    ))]
         [cur 0]
         [ans-index 0])
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ([val-i (char-val (string-ref s i))])
        (set! cur (modulo (+ (* cur power) val_i) modulo))
        ;; if window size exceeds k, remove leftmost char contribution
        (when (> (- n i) k)
          (let* ([remove-idx (+ i k)]
                 [rem-val (char-val (string-ref s remove-idx))])
            (set! cur (modulo (- cur (modulo (* rem-val power-k) modulo))
                              modulo))))
        ;; when we have a full window, check hash
        (when (<= i (- n k))
          (when (= cur hashValue)
            (set! ans-index i)))))
    (substring s ans-index (+ ans-index k))))
```

## Erlang

```erlang
-spec sub_str_hash(S :: unicode:unicode_binary(), Power :: integer(), Modulo :: integer(), K :: integer(), HashValue :: integer()) -> unicode:unicode_binary().
sub_str_hash(S, Power, Modulo, K, HashValue) ->
    CharList = [C - $a + 1 || <<C>> <= S],
    N = length(CharList),
    CharTuple = list_to_tuple(CharList),
    PowK = mod_pow(Power rem Modulo, K, Modulo),

    % start from the end of the string
    {AnsIdx, _} = loop(N - 1, 0, 0, undefined, S, Power, Modulo, K, HashValue, PowK, CharTuple),
    binary:part(S, AnsIdx, K).

%% Recursive loop over indices from I down to 0.
loop(I, CurHash, Count, AnsIdx, _S, _Power, _Modulo, _K, _HashValue, _PowK, _CharTuple) when I < 0 ->
    {AnsIdx, CurHash};
loop(I, CurHash, Count, AnsIdx, S, Power, Modulo, K, HashValue, PowK, CharTuple) ->
    Val = element(I + 1, CharTuple),
    NewCurTmp = (Val + CurHash * Power) rem Modulo,
    NewCount0 = Count + 1,

    {NewCur, NewCount} =
        if
            NewCount0 > K ->
                OutPos = I + K,
                OutVal = element(OutPos + 1, CharTuple),
                Adjusted = (NewCurTmp - (OutVal * PowK) rem Modulo) rem Modulo,
                Cur2 = if Adjusted < 0 -> Adjusted + Modulo; true -> Adjusted end,
                {Cur2, K};
            true ->
                {NewCurTmp, NewCount0}
        end,

    NewAnsIdx =
        case NewCount of
            K when NewCur == HashValue ->
                I;
            _ ->
                AnsIdx
        end,

    loop(I - 1, NewCur, NewCount, NewAnsIdx, S, Power, Modulo, K, HashValue, PowK, CharTuple).

%% Fast modular exponentiation.
-spec mod_pow(Base :: integer(), Exp :: integer(), Mod :: integer()) -> integer().
mod_pow(_Base, 0, _Mod) ->
    1;
mod_pow(Base, Exp, Mod) when Exp rem 2 =:= 1 ->
    (Base * mod_pow((Base * Base) rem Mod, Exp div 2, Mod)) rem Mod;
mod_pow(Base, Exp, Mod) ->
    mod_pow((Base * Base) rem Mod, Exp div 2, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @spec sub_str_hash(String.t(), integer, integer, integer, integer) :: String.t()
  def sub_str_hash(s, power, modulo, k, hash_value) do
    vals = :binary.bin_to_list(s) |> Enum.map(fn b -> b - ?a + 1 end)
    tup = List.to_tuple(vals)
    n = tuple_size(tup)
    start_idx = n - k

    {init_hash, pow_k} = init_hash_and_pow(start_idx, k, tup, power, modulo)

    ans_start =
      if init_hash == hash_value do
        start_idx
      else
        nil
      end

    final_start = process(start_idx - 1, init_hash, ans_start, tup, k, power, modulo, pow_k, hash_value)
    String.slice(s, final_start, k)
  end

  defp init_hash_and_pow(start_idx, k, tup, power, modulo) do
    do_init(start_idx, 0, k, 0, 1, tup, power, modulo)
  end

  defp do_init(_pos, i, k, hash, pow, _tup, _power, _modulo) when i == k do
    {hash, pow}
  end

  defp do_init(pos, i, k, hash, pow, tup, power, modulo) do
    val = elem(tup, pos + i)
    new_hash = rem(hash + val * pow, modulo)
    new_pow = rem(pow * power, modulo)
    do_init(pos, i + 1, k, new_hash, new_pow, tup, power, modulo)
  end

  defp process(i, cur_hash, ans_start, tup, k, power, modulo, pow_k, target) when i < 0 do
    ans_start
  end

  defp process(i, cur_hash, ans_start, tup, k, power, modulo, pow_k, target) do
    val_out = elem(tup, i + k)
    val_new = elem(tup, i)

    hash1 = rem(cur_hash * power, modulo)
    subtr = rem(val_out * pow_k, modulo)
    hash2 = hash1 - subtr
    hash2 = if hash2 < 0, do: hash2 + modulo, else: hash2
    new_hash = rem(hash2 + val_new, modulo)

    new_ans =
      if new_hash == target do
        i
      else
        ans_start
      end

    process(i - 1, new_hash, new_ans, tup, k, power, modulo, pow_k, target)
  end
end
```
