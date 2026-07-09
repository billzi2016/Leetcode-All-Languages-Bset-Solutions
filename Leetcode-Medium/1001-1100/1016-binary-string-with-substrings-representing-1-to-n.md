# 1016. Binary String With Substrings Representing 1 To N

## Cpp

```cpp
class Solution {
public:
    bool queryString(string s, int n) {
        unordered_set<int> present;
        int L = s.size();
        for (int i = 0; i < L; ++i) {
            if (s[i] == '0') continue; // leading zero not allowed
            long long val = 0;
            for (int len = 1; len <= 30 && i + len <= L; ++len) {
                val = (val << 1) + (s[i + len - 1] - '0');
                if (val > n) break;
                present.insert((int)val);
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (!present.count(i)) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean queryString(String s, int n) {
        int maxLen = Math.min(30, s.length());
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            int val = 0;
            for (int len = 1; len <= maxLen && i + len <= s.length(); len++) {
                char c = s.charAt(i + len - 1);
                val = (val << 1) + (c - '0');
                set.add(val);
            }
        }
        if (n > set.size()) return false;
        for (int i = 1; i <= n; i++) {
            if (!set.contains(i)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        max_len = min(30, len(s))  # binary length needed for numbers up to 1e9
        seen = set()
        L = len(s)
        for i in range(L):
            if s[i] == '0':
                continue
            val = 0
            for j in range(i, min(L, i + max_len)):
                val = (val << 1) | (s[j] == '1')
                if val > n:
                    break
                seen.add(val)
        return len(seen) == n
```

## Python3

```python
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        L = len(s)
        max_len = min(30, L)
        # Quick impossibility check
        if n > (1 << max_len) - 1:
            return False

        present = set()
        for i in range(L):
            if s[i] == '0':
                continue
            val = 0
            for l in range(max_len):
                if i + l >= L:
                    break
                val = (val << 1) | (s[i + l] == '1')
                present.add(val)

        for num in range(1, n + 1):
            if num not in present:
                return False
        return True
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

bool queryString(char* s, int n) {
    int len = strlen(s);
    int maxSub = len * 30;
    int *vals = (int *)malloc(maxSub * sizeof(int));
    if (!vals) return false; // allocation failure safety

    int cnt = 0;
    for (int i = 0; i < len; ++i) {
        if (s[i] != '1') continue;          // binary numbers start with '1'
        unsigned int val = 0;
        for (int l = 0; l < 30 && i + l < len; ++l) {
            val = (val << 1) + (unsigned int)(s[i + l] - '0');
            vals[cnt++] = (int)val;
        }
    }

    if (cnt == 0) {
        free(vals);
        return false; // no positive binary numbers present
    }

    qsort(vals, cnt, sizeof(int), cmp_int);

    int uniqCnt = 0;
    for (int i = 0; i < cnt; ++i) {
        if (i == 0 || vals[i] != vals[uniqCnt - 1]) {
            vals[uniqCnt++] = vals[i];
        }
    }

    if (n > uniqCnt) {
        free(vals);
        return false;
    }

    for (int i = 1; i <= n; ++i) {
        int key = i;
        if (!bsearch(&key, vals, uniqCnt, sizeof(int), cmp_int)) {
            free(vals);
            return false;
        }
    }

    free(vals);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool QueryString(string s, int n) {
        int L = s.Length;
        int maxLen = Math.Min(30, L);
        long limit = 1L << maxLen;
        if (n >= limit) return false;

        var substrings = new HashSet<string>();
        for (int i = 0; i < L; i++) {
            int maxPossible = Math.Min(maxLen, L - i);
            for (int len = 1; len <= maxPossible; len++) {
                substrings.Add(s.Substring(i, len));
            }
        }

        for (int i = 1; i <= n; i++) {
            string bin = Convert.ToString(i, 2);
            if (!substrings.Contains(bin)) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} n
 * @return {boolean}
 */
var queryString = function(s, n) {
    // If binary length of n exceeds s length, impossible.
    if (n.toString(2).length > s.length) return false;

    const substrSet = new Set();
    const L = s.length;
    const maxLen = Math.min(30, L); // numbers up to 1e9 need at most 30 bits

    for (let i = 0; i < L; ++i) {
        let cur = '';
        for (let len = 1; len <= maxLen && i + len <= L; ++len) {
            cur += s[i + len - 1];
            substrSet.add(cur);
        }
    }

    for (let i = 1; i <= n; ++i) {
        const bin = i.toString(2);
        if (!substrSet.has(bin)) return false;
    }
    return true;
};
```

## Typescript

```typescript
function queryString(s: string, n: number): boolean {
    const substrSet = new Set<string>();
    const maxLen = 30; // binary length of numbers up to 1e9
    for (let i = 0; i < s.length; ++i) {
        let cur = '';
        for (let j = i; j < s.length && j < i + maxLen; ++j) {
            cur += s[j];
            substrSet.add(cur);
        }
    }
    for (let num = 1; num <= n; ++num) {
        const bin = num.toString(2);
        if (!substrSet.has(bin)) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $n
     * @return Boolean
     */
    function queryString($s, $n) {
        $len = strlen($s);
        $maxBits = min(30, $len); // numbers up to 2^30 > 1e9
        $present = [];

        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '0') continue; // binary representation cannot start with 0
            $value = 0;
            for ($l = 1; $l <= $maxBits && $i + $l <= $len; $l++) {
                $bit = $s[$i + $l - 1];
                $value = ($value << 1) + ($bit === '1' ? 1 : 0);
                if ($value > $n) break; // larger numbers are irrelevant
                $present[$value] = true;
            }
        }

        // quick size check to avoid iterating huge n when impossible
        if (count($present) < $n) {
            return false;
        }

        for ($i = 1; $i <= $n; $i++) {
            if (!isset($present[$i])) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func queryString(_ s: String, _ n: Int) -> Bool {
        // If the binary length of n exceeds s's length, impossible.
        if String(n, radix: 2).count > s.count { return false }
        for i in 1...n {
            let bin = String(i, radix: 2)
            if !s.contains(bin) {
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
    fun queryString(s: String, n: Int): Boolean {
        val present = HashSet<Int>()
        val maxLen = 30 // because n <= 10^9 fits in 30 bits
        val len = s.length
        for (i in 0 until len) {
            var value = 0L
            for (j in i until minOf(len, i + maxLen)) {
                value = (value shl 1) + (s[j] - '0')
                if (value > n) break
                present.add(value.toInt())
            }
        }
        for (k in 1..n) {
            if (!present.contains(k)) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool queryString(String s, int n) {
    final Set<int> seen = {};
    int L = s.length;
    for (int i = 0; i < L; ++i) {
      int val = 0;
      for (int len = 1; len <= 30 && i + len <= L; ++len) {
        val = (val << 1) + (s.codeUnitAt(i + len - 1) - 48);
        if (val > n) break;
        if (val >= 1) seen.add(val);
      }
    }
    return seen.length == n;
  }
}
```

## Golang

```go
func queryString(s string, n int) bool {
	maxLen := 30
	if len(s) < maxLen {
		maxLen = len(s)
	}
	seen := make(map[int]struct{})
	L := len(s)
	for i := 0; i < L; i++ {
		if s[i] != '1' {
			continue
		}
		val := 0
		for l := 1; l <= maxLen && i+l <= L; l++ {
			val = (val << 1) + int(s[i+l-1]-'0')
			if val > n {
				break
			}
			seen[val] = struct{}{}
		}
	}
	return len(seen) == n
}
```

## Ruby

```ruby
def query_string(s, n)
  max_len = n.bit_length
  substr_set = {}
  l = s.length
  (0...l).each do |i|
    cur = ''
    limit = [max_len, l - i].min
    (1..limit).each do |_|
      cur << s[i + cur.length]
      substr_set[cur] = true
    end
  end
  (1..n).each do |num|
    return false unless substr_set[num.to_s(2)]
  end
  true
end
```

## Scala

```scala
object Solution {
    def queryString(s: String, n: Int): Boolean = {
        val maxLen = Math.min(30, s.length)
        val subs = scala.collection.mutable.HashSet[String]()
        for (i <- 0 until s.length) {
            var sb = new java.lang.StringBuilder()
            var l = 0
            while (l < maxLen && i + l < s.length) {
                sb.append(s.charAt(i + l))
                subs.add(sb.toString())
                l += 1
            }
        }
        for (i <- 1 to n) {
            val bin = Integer.toBinaryString(i)
            if (!subs.contains(bin)) return false
        }
        true
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn query_string(s: String, n: i32) -> bool {
        let bytes = s.as_bytes();
        let len = bytes.len();
        let max_len = std::cmp::min(30, len);
        // early impossible case: need more distinct substrings than possible
        if (n as usize) > len * max_len {
            return false;
        }

        let mut present: HashSet<i32> = HashSet::new();

        for i in 0..len {
            let mut val: i64 = 0;
            for j in i..std::cmp::min(len, i + max_len) {
                val = (val << 1) + ((bytes[j] - b'0') as i64);
                if val > 0 && val <= n as i64 {
                    present.insert(val as i32);
                }
            }
        }

        for num in 1..=n {
            if !present.contains(&num) {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (query-string s n)
  (-> string? exact-integer? boolean?)
  (let* ((len (string-length s))
         ;; Upper bound on number of substrings of length ≤30
         (max-substrings (* len 30)))
    (if (> n max-substrings)
        #false
        (let ((set (make-hash)))
          ;; collect all integers represented by substrings that start with '1'
          (for ([i (in-range len)])
            (when (char=? (string-ref s i) #\1)
              (let loop ((j i) (val 0) (cnt 0))
                (when (and (< cnt 30) (< j len))
                  (set! val (+ (arithmetic-shift val 1)
                               (if (char=? (string-ref s j) #\1) 1 0)))
                  (hash-set! set val #t)
                  (loop (+ j 1) val (+ cnt 1))))))
          ;; verify every number from 1 to n appears
          (let loop ((k 1))
            (cond [(> k n) #true]
                  [(hash-has-key? set k) (loop (+ k 1))]
                  [else #false]))))))
```

## Erlang

```erlang
-module(solution).
-export([query_string/2]).

-spec query_string(S :: unicode:unicode_binary(), N :: integer()) -> boolean().
query_string(S, N) ->
    Len = byte_size(S),
    MaxLen = min(30, Len),
    Set = build_set(S, Len, MaxLen, #{}),
    case N > maps:size(Set) of
        true -> false;
        false -> check_numbers(1, N, Set)
    end.

build_set(S, Len, MaxLen, Acc) ->
    build_start(0, S, Len, MaxLen, Acc).

build_start(Pos, _S, Len, _MaxLen, Acc) when Pos >= Len ->
    Acc;
build_start(Pos, S, Len, MaxLen, Acc) ->
    NewAcc = add_substrings(Pos, S, Len, MaxLen, Acc),
    build_start(Pos + 1, S, Len, MaxLen, NewAcc).

add_substrings(Pos, S, Len, MaxLen, Acc) ->
    add_len(1, Pos, S, Len, MaxLen, Acc).

add_len(LenSub, Pos, _S, Len, _MaxLen, Acc) when Pos + LenSub > Len ->
    Acc;
add_len(LenSub, Pos, S, Len, MaxLen, Acc) ->
    Sub = binary:part(S, Pos, LenSub),
    NewAcc = maps:put(Sub, true, Acc),
    case LenSub < MaxLen of
        true -> add_len(LenSub + 1, Pos, S, Len, MaxLen, NewAcc);
        false -> NewAcc
    end.

check_numbers(I, N, _Set) when I > N ->
    true;
check_numbers(I, N, Set) ->
    Bin = list_to_binary(io_lib:format("~b", [I])),
    case maps:is_key(Bin, Set) of
        true -> check_numbers(I + 1, N, Set);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec query_string(s :: String.t(), n :: integer) :: boolean
  def query_string(s, n) do
    s_len = String.length(s)
    max_sub_len = min(s_len, 30)

    substr_set =
      1..max_sub_len
      |> Enum.reduce(MapSet.new(), fn len, acc ->
        0..(s_len - len)
        |> Enum.reduce(acc, fn i, set_acc ->
          sub = String.slice(s, i, len)
          MapSet.put(set_acc, sub)
        end)
      end)

    1..n
    |> Enum.reduce_while(true, fn i, _ ->
      bin = Integer.to_string(i, 2)

      if MapSet.member?(substr_set, bin) do
        {:cont, true}
      else
        {:halt, false}
      end
    end)
  end
end
```
