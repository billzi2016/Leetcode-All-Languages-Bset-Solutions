# 1540. Can Convert String in K Moves

## Cpp

```cpp
class Solution {
public:
    bool canConvertString(string s, string t, int k) {
        vector<int> used(26, 0);
        for (size_t i = 0; i < s.size(); ++i) {
            int diff = (t[i] - s[i] + 26) % 26;
            if (diff == 0) continue;
            long long movesNeeded = diff + 26LL * used[diff];
            if (movesNeeded > k) return false;
            ++used[diff];
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canConvertString(String s, String t, int k) {
        if (s.length() != t.length()) return false;
        int[] used = new int[26];
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            char b = t.charAt(i);
            if (a == b) continue;
            int shift = (b - a + 26) % 26;
            // shift is in [1,25]
            int movesNeeded = shift + 26 * used[shift];
            if (movesNeeded > k) return false;
            used[shift]++;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        freq = [0] * 26  # counts for each required shift (1..25)
        for ch_s, ch_t in zip(s, t):
            diff = (ord(ch_t) - ord(ch_s)) % 26
            if diff == 0:
                continue
            need_move = diff + 26 * freq[diff]
            if need_move > k:
                return False
            freq[diff] += 1
        return True
```

## Python3

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        from collections import Counter
        diff_counts = Counter()
        for sc, tc in zip(s, t):
            d = (ord(tc) - ord(sc)) % 26
            if d != 0:
                diff_counts[d] += 1
        for d, cnt in diff_counts.items():
            # The largest move needed for this diff
            max_move = d + 26 * (cnt - 1)
            if max_move > k:
                return False
        return True
```

## C

```c
#include <string.h>
#include <stdbool.h>

bool canConvertString(char* s, char* t, int k) {
    long long cnt[26] = {0};
    size_t n = strlen(s);
    for (size_t i = 0; i < n; ++i) {
        int diff = (t[i] - s[i] + 26) % 26;
        if (diff == 0) continue;
        cnt[diff]++;
        long long needed = diff + 26LL * (cnt[diff] - 1);
        if (needed > k) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanConvertString(string s, string t, int k)
    {
        if (s.Length != t.Length) return false;

        int[] cnt = new int[26];
        for (int i = 0; i < s.Length; i++)
        {
            char a = s[i], b = t[i];
            if (a == b) continue;
            int diff = (b - a + 26) % 26;
            cnt[diff]++;
        }

        long K = k;
        for (int d = 1; d < 26; d++)
        {
            if (cnt[d] == 0) continue;
            long maxMove = d + 26L * (cnt[d] - 1);
            if (maxMove > K) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {boolean}
 */
var canConvertString = function(s, t, k) {
    const n = s.length;
    // count required shifts for each remainder 1..25
    const need = new Array(26).fill(0);
    
    for (let i = 0; i < n; ++i) {
        const a = s.charCodeAt(i) - 97;
        const b = t.charCodeAt(i) - 97;
        const diff = (b - a + 26) % 26;
        if (diff !== 0) need[diff]++;
    }
    
    for (let d = 1; d < 26; ++d) {
        if (need[d] === 0) continue;
        if (k < d) return false; // no move with this remainder exists
        const maxMoves = Math.floor((k - d) / 26) + 1;
        if (need[d] > maxMoves) return false;
    }
    
    return true;
};
```

## Typescript

```typescript
function canConvertString(s: string, t: string, k: number): boolean {
    if (s.length !== t.length) return false;
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        const a = s.charCodeAt(i) - 97;
        const b = t.charCodeAt(i) - 97;
        if (a === b) continue;
        const diff = (b - a + 26) % 26;
        cnt[diff]++;
    }
    for (let d = 1; d < 26; d++) {
        if (cnt[d] > 0) {
            const maxMove = d + 26 * (cnt[d] - 1);
            if (maxMove > k) return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Boolean
     */
    function canConvertString($s, $t, $k) {
        $n = strlen($s);
        if ($n !== strlen($t)) {
            return false;
        }
        $cnt = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $diff = (ord($t[$i]) - ord($s[$i]) + 26) % 26;
            if ($diff !== 0) {
                $cnt[$diff]++;
            }
        }
        for ($d = 1; $d < 26; $d++) {
            if ($cnt[$d] > 0) {
                $required = $d + ($cnt[$d] - 1) * 26;
                if ($required > $k) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canConvertString(_ s: String, _ t: String, _ k: Int) -> Bool {
        let sBytes = Array(s.utf8)
        let tBytes = Array(t.utf8)
        if sBytes.count != tBytes.count { return false }
        
        var freq = [Int](repeating: 0, count: 26)
        for i in 0..<sBytes.count {
            let a = Int(sBytes[i] - 97)   // 'a' ASCII is 97
            let b = Int(tBytes[i] - 97)
            if a != b {
                var diff = b - a
                if diff < 0 { diff += 26 }
                freq[diff] += 1
            }
        }
        
        for d in 1..<26 {   // diff == 0 needs no move
            let cnt = freq[d]
            if cnt == 0 { continue }
            // The largest required move for this diff is d + 26 * (cnt - 1)
            let maxMove = d + 26 * (cnt - 1)
            if maxMove > k {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canConvertString(s: String, t: String, k: Int): Boolean {
        if (s.length != t.length) return false
        val cnt = IntArray(26)
        for (i in s.indices) {
            var diff = (t[i] - 'a') - (s[i] - 'a')
            if (diff < 0) diff += 26
            if (diff != 0) cnt[diff]++
        }
        for (r in 1..25) {
            val need = cnt[r]
            if (need == 0) continue
            if (k < r) return false
            val maxPossible = (k - r) / 26 + 1
            if (need > maxPossible) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canConvertString(String s, String t, int k) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      int diff = (t.codeUnitAt(i) - s.codeUnitAt(i) + 26) % 26;
      if (diff != 0) cnt[diff]++;
    }
    for (int d = 1; d < 26; d++) {
      if (cnt[d] > 0) {
        int maxMove = d + 26 * (cnt[d] - 1);
        if (maxMove > k) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func canConvertString(s string, t string, k int) bool {
	if len(s) != len(t) {
		return false
	}
	cnt := make([]int, 26)
	for i := 0; i < len(s); i++ {
		diff := (int(t[i]-s[i]) + 26) % 26
		if diff != 0 {
			cnt[diff]++
		}
	}
	K := int64(k)
	for d := 1; d < 26; d++ {
		c := cnt[d]
		if c > 0 {
			need := int64(d) + int64(26)*(int64(c)-1)
			if need > K {
				return false
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def can_convert_string(s, t, k)
  cnt = Array.new(26, 0)
  sb = s.bytes
  tb = t.bytes
  sb.each_with_index do |b, i|
    diff = (tb[i] - b) % 26
    cnt[diff] += 1 if diff != 0
  end
  (1..25).each do |r|
    c = cnt[r]
    next if c == 0
    max_move = r + 26 * (c - 1)
    return false if max_move > k
  end
  true
end
```

## Scala

```scala
object Solution {
    def canConvertString(s: String, t: String, k: Int): Boolean = {
        if (s.length != t.length) return false
        val cnt = new Array[Int](26)
        val n = s.length
        for (i <- 0 until n) {
            val diff = ((t.charAt(i) - s.charAt(i) + 26) % 26).toInt
            if (diff != 0) cnt(diff) += 1
        }
        val K = k.toLong
        for (d <- 1 until 26) {
            val c = cnt(d)
            if (c > 0) {
                val required = d + (c - 1).toLong * 26L
                if (required > K) return false
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_convert_string(s: String, t: String, k: i32) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut need = [0usize; 26];
        let sb = s.as_bytes();
        let tb = t.as_bytes();
        for i in 0..sb.len() {
            let a = sb[i] as i32;
            let b = tb[i] as i32;
            let diff = (b - a + 26) % 26;
            if diff != 0 {
                need[diff as usize] += 1;
            }
        }

        let k64 = k as i64;
        for r in 1..=25usize {
            let cnt = need[r];
            if cnt == 0 {
                continue;
            }
            let r64 = r as i64;
            if k64 < r64 {
                return false;
            }
            // number of moves with remainder r (mod 26) up to k
            let available = ((k64 - r64) / 26 + 1) as usize;
            if cnt > available {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-convert-string s t k)
  (-> string? string? exact-integer? boolean?)
  (let* ((n (string-length s))
         (m (string-length t)))
    (if (not (= n m))
        #false
        (let ((cnt (make-vector 26 0))
              (possible #t))
          (for ([i (in-range n)])
            (when possible
              (define cs (char->integer (string-ref s i)))
              (define ct (char->integer (string-ref t i)))
              (define diff (modulo (- ct cs) 26))
              (unless (= diff 0)
                (let* ((prev (vector-ref cnt diff))
                       (new (+ prev 1))
                       (required (+ diff (* 26 (- new 1)))))
                  (vector-set! cnt diff new)
                  (when (> required k)
                    (set! possible #f)))))))
          possible)))
```

## Erlang

```erlang
-module(solution).
-export([can_convert_string/3]).

-spec can_convert_string(S :: binary(), T :: binary(), K :: integer()) -> boolean().
can_convert_string(S, T, K) ->
    Counts = diff_counts(S, T, #{}),
    check_remainders(1, 25, K, Counts).

diff_counts(<<>>, <<>>, Acc) ->
    Acc;
diff_counts(<<Sc, RestS/binary>>, <<Tc, RestT/binary>>, Acc) ->
    if
        Sc =:= Tc ->
            diff_counts(RestS, RestT, Acc);
        true ->
            D = (Tc - Sc + 26) rem 26,
            NewAcc = maps:update_with(D, fun(V) -> V + 1 end, 1, Acc),
            diff_counts(RestS, RestT, NewAcc)
    end.

check_remainders(R, MaxR, _K, _Counts) when R > MaxR ->
    true;
check_remainders(R, MaxR, K, Counts) ->
    Required = maps:get(R, Counts, 0),
    Available = if
        K >= R -> ((K - R) div 26) + 1;
        true   -> 0
    end,
    if
        Required =< Available ->
            check_remainders(R + 1, MaxR, K, Counts);
        true ->
            false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_convert_string(s :: String.t(), t :: String.t(), k :: integer) :: boolean()
  def can_convert_string(s, t, k) do
    if byte_size(s) != byte_size(t) do
      false
    else
      s_bytes = :binary.bin_to_list(s)
      t_bytes = :binary.bin_to_list(t)

      result =
        Enum.reduce_while(Enum.zip(s_bytes, t_bytes), %{}, fn {sc, tc}, acc ->
          diff = rem(tc - sc + 26, 26)

          if diff == 0 do
            {:cont, acc}
          else
            cnt = Map.get(acc, diff, 0) + 1
            required = diff + 26 * (cnt - 1)

            if required > k do
              {:halt, :error}
            else
              {:cont, Map.put(acc, diff, cnt)}
            end
          end
        end)

      result != :error
    end
  end
end
```
