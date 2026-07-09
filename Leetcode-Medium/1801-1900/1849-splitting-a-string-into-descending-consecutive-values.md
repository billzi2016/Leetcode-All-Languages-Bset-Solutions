# 1849. Splitting a String Into Descending Consecutive Values

## Cpp

```cpp
class Solution {
public:
    bool splitString(string s) {
        int n = s.size();
        // try all possible lengths for the first number
        for (int len = 1; len < n; ++len) {
            __int128 first = 0;
            for (int i = 0; i < len; ++i) {
                first = first * 10 + (s[i] - '0');
            }
            if (dfs(s, len, first - 1)) return true;
        }
        return false;
    }

private:
    bool dfs(const string& s, int pos, __int128 need) {
        int n = s.size();
        if (pos == n) return true;               // successfully consumed all characters
        if (need < 0) return false;              // cannot have negative numbers

        __int128 cur = 0;
        for (int i = pos; i < n; ++i) {
            cur = cur * 10 + (s[i] - '0');
            if (cur > need) break;               // further digits will only increase
            if (cur == need) {
                if (dfs(s, i + 1, need - 1)) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
import java.math.BigInteger;

class Solution {
    public boolean splitString(String s) {
        int n = s.length();
        for (int i = 1; i < n; i++) {
            BigInteger first = new BigInteger(s.substring(0, i));
            if (dfs(s, i, first.subtract(BigInteger.ONE))) {
                return true;
            }
        }
        return false;
    }

    private boolean dfs(String s, int index, BigInteger expected) {
        if (expected.signum() < 0) {
            return false;
        }
        int n = s.length();
        if (index == n) {
            return true; // successfully matched at least two numbers
        }
        for (int end = index + 1; end <= n; end++) {
            BigInteger cur = new BigInteger(s.substring(index, end));
            int cmp = cur.compareTo(expected);
            if (cmp == 0) {
                if (dfs(s, end, expected.subtract(BigInteger.ONE))) {
                    return true;
                }
            } else if (cmp > 0) {
                // further extensions will only increase the number (or keep same with leading zeros),
                // so we can break early when cur already exceeds expected and next char isn't '0'.
                // For simplicity, continue checking longer substrings.
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos, prev):
            if pos == n:
                return True
            expected = prev - 1
            if expected < 0:
                return False
            for end in range(pos + 1, n + 1):
                val = int(s[pos:end])
                if val == expected and dfs(end, val):
                    return True
            return False

        for first_len in range(1, n):
            first_val = int(s[:first_len])
            if dfs(first_len, first_val):
                return True
        return False
```

## Python3

```python
class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        from functools import lru_cache

        @lru_cache(None)
        def dfs(idx: int, prev: int) -> bool:
            if idx == n:
                return True
            target = prev - 1
            for j in range(idx + 1, n + 1):
                cur = int(s[idx:j])
                if cur == target and dfs(j, cur):
                    return True
            return False

        for i in range(1, n):
            first = int(s[:i])
            if dfs(i, first):
                return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

static bool dfs(const char *p, unsigned __int128 prev) {
    if (*p == '\0') return true;
    int n = strlen(p);
    unsigned __int128 val = 0;
    for (int i = 0; i < n; ++i) {
        val = val * 10 + (unsigned __int128)(p[i] - '0');
        if (prev == 0) break;                     // cannot go below 0
        unsigned __int128 target = prev - 1;
        if (val > target) break;                  // further digits will only increase
        if (val == target) {
            if (dfs(p + i + 1, val)) return true;
        }
    }
    return false;
}

bool splitString(char* s) {
    int len = strlen(s);
    for (int cut = 0; cut < len - 1; ++cut) {      // first number must leave at least one char
        unsigned __int128 first = 0;
        for (int i = 0; i <= cut; ++i) {
            first = first * 10 + (unsigned __int128)(s[i] - '0');
        }
        if (dfs(s + cut + 1, first)) return true;
    }
    return false;
}
```

## Csharp

```csharp
using System.Numerics;

public class Solution {
    public bool SplitString(string s) {
        int n = s.Length;
        for (int i = 1; i < n; i++) {
            BigInteger first = BigInteger.Parse(s.Substring(0, i));
            if (DFS(s, i, first)) return true;
        }
        return false;
    }

    private bool DFS(string s, int pos, BigInteger prev) {
        if (pos == s.Length) return true;
        BigInteger target = prev - 1;
        if (target < 0) return false;

        for (int len = 1; pos + len <= s.Length; len++) {
            BigInteger cur = BigInteger.Parse(s.Substring(pos, len));
            if (cur == target) {
                if (DFS(s, pos + len, cur)) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var splitString = function(s) {
    const n = s.length;
    const memo = new Map(); // failure memoization

    function dfs(idx, prev) {
        if (idx === n) return true; // successfully consumed all characters
        const key = idx + ',' + prev.toString();
        if (memo.has(key)) return false;

        for (let end = idx + 1; end <= n; ++end) {
            const cur = BigInt(s.slice(idx, end));
            if (cur === prev - 1n) {
                if (dfs(end, cur)) return true;
            }
        }

        memo.set(key, false);
        return false;
    }

    // try every possible first number length (must leave at least one character for the next part)
    for (let i = 1; i < n; ++i) {
        const first = BigInt(s.slice(0, i));
        if (dfs(i, first)) return true;
    }
    return false;
};
```

## Typescript

```typescript
function splitString(s: string): boolean {
    const n = s.length;
    function dfs(pos: number, prev: bigint): boolean {
        if (pos === n) return true;
        const target = prev - 1n;
        for (let end = pos + 1; end <= n; ++end) {
            const curVal = BigInt(s.slice(pos, end));
            if (curVal === target) {
                if (dfs(end, curVal)) return true;
            }
        }
        return false;
    }

    for (let i = 1; i < n; ++i) {
        const firstVal = BigInt(s.slice(0, i));
        if (dfs(i, firstVal)) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function splitString($s) {
        $n = strlen($s);
        // try every possible first number (must leave at least one digit for the second part)
        for ($len = 1; $len < $n; $len++) {
            $first = substr($s, 0, $len);
            $firstVal = ltrim($first, '0');
            if ($firstVal === '') $firstVal = '0';
            if ($this->dfs(substr($s, $len), $firstVal)) {
                return true;
            }
        }
        return false;
    }

    private function dfs(string $remaining, string $prev) : bool {
        if ($remaining === '') {
            // successfully consumed all characters
            return true;
        }
        $next = $this->subOne($prev);
        if ($next === null) {
            return false;
        }
        $lenRem = strlen($remaining);
        for ($len = 1; $len <= $lenRem; $len++) {
            $part = substr($remaining, 0, $len);
            $partVal = ltrim($part, '0');
            if ($partVal === '') $partVal = '0';
            if ($partVal === $next) {
                if ($this->dfs(substr($remaining, $len), $next)) {
                    return true;
                }
            }
        }
        return false;
    }

    // returns string representation of $num - 1, or null if $num == "0"
    private function subOne(string $num) : ?string {
        if ($num === '0') {
            return null;
        }
        $i = strlen($num) - 1;
        $carry = 1;
        $res = '';
        while ($i >= 0) {
            $digit = ord($num[$i]) - 48;
            $digit -= $carry;
            if ($digit < 0) {
                $digit += 10;
                $carry = 1;
            } else {
                $carry = 0;
            }
            $res = chr($digit + 48) . $res;
            $i--;
        }
        // strip leading zeros
        $res = ltrim($res, '0');
        if ($res === '') {
            $res = '0';
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func splitString(_ s: String) -> Bool {
        let n = s.count
        if n < 2 { return false }
        
        func dfs(_ idx: Int, _ prev: Decimal, _ count: Int) -> Bool {
            if idx == n {
                return count >= 2
            }
            var endIdx = idx
            while endIdx < n {
                let start = s.index(s.startIndex, offsetBy: idx)
                let end = s.index(s.startIndex, offsetBy: endIdx + 1)
                let sub = String(s[start..<end])
                if let cur = Decimal(string: sub) {
                    if prev - Decimal(1) == cur {
                        if dfs(endIdx + 1, cur, count + 1) { return true }
                    }
                }
                endIdx += 1
            }
            return false
        }
        
        var splitPos = 0
        while splitPos < n - 1 {
            let start = s.startIndex
            let end = s.index(s.startIndex, offsetBy: splitPos + 1)
            let sub = String(s[start..<end])
            if let first = Decimal(string: sub) {
                if dfs(splitPos + 1, first, 1) { return true }
            }
            splitPos += 1
        }
        return false
    }
}
```

## Kotlin

```kotlin
import java.math.BigInteger

class Solution {
    fun splitString(s: String): Boolean {
        val n = s.length
        for (len in 1 until n) {
            val firstVal = BigInteger(s.substring(0, len))
            if (dfs(s, len, firstVal)) return true
        }
        return false
    }

    private fun dfs(s: String, index: Int, prev: BigInteger): Boolean {
        if (index == s.length) return true
        val target = prev.subtract(BigInteger.ONE)
        if (target.signum() < 0) return false
        for (len in 1..s.length - index) {
            val curVal = BigInteger(s.substring(index, index + len))
            if (curVal == target && dfs(s, index + len, curVal)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool splitString(String s) {
    int n = s.length;
    for (int i = 1; i < n; i++) {
      int firstVal = int.parse(s.substring(0, i));
      if (_dfs(s, i, firstVal)) return true;
    }
    return false;
  }

  bool _dfs(String s, int pos, int prev) {
    if (pos == s.length) return true;
    for (int len = 1; pos + len <= s.length; len++) {
      int curVal = int.parse(s.substring(pos, pos + len));
      if (curVal == prev - 1) {
        if (_dfs(s, pos + len, curVal)) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func splitString(s string) bool {
	n := len(s)

	toInt := func(sub string) int64 {
		var v int64
		for i := 0; i < len(sub); i++ {
			v = v*10 + int64(sub[i]-'0')
		}
		return v
	}

	var dfs func(pos int, prev int64, cnt int) bool
	dfs = func(pos int, prev int64, cnt int) bool {
		if pos == n {
			return cnt >= 2
		}
		target := prev - 1
		if target < 0 {
			return false
		}
		var cur int64
		for i := pos; i < n; i++ {
			cur = cur*10 + int64(s[i]-'0')
			if cur > target {
				break
			}
			if cur == target {
				if dfs(i+1, cur, cnt+1) {
					return true
				}
			}
		}
		return false
	}

	for l := 1; l <= n-1; l++ {
		firstVal := toInt(s[:l])
		if dfs(l, firstVal, 1) {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def split_string(s)
  n = s.length
  (1...n).each do |len|
    first_val = s[0, len].to_i
    return true if dfs(s, len, first_val, 1)
  end
  false
end

def dfs(s, idx, prev, cnt)
  return false if idx >= s.length
  target = prev - 1
  return false if target < 0
  max_len = s.length - idx
  (1..max_len).each do |len|
    val = s[idx, len].to_i
    next unless val == target
    new_idx = idx + len
    return true if new_idx == s.length && cnt + 1 >= 2
    return true if dfs(s, new_idx, val, cnt + 1)
  end
  false
end
```

## Scala

```scala
object Solution {
  def splitString(s: String): Boolean = {
    val n = s.length

    // depth‑first search trying to match the expected next value
    def dfs(pos: Int, prev: BigInt, count: Int): Boolean = {
      if (pos == n) return count >= 2
      var end = pos + 1
      while (end <= n) {
        val curVal = BigInt(s.substring(pos, end))
        if (prev - 1 == curVal) {
          if (dfs(end, curVal, count + 1)) return true
        }
        end += 1
      }
      false
    }

    // try every possible first number length
    var len = 1
    while (len < n) {
      val firstVal = BigInt(s.substring(0, len))
      if (dfs(len, firstVal, 1)) return true
      len += 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn split_string(s: String) -> bool {
        let n = s.len();
        for i in 1..n {
            let first_part = &s[0..i];
            if let Ok(first_val) = first_part.parse::<u128>() {
                if Self::dfs(&s[i..], first_val) {
                    return true;
                }
            }
        }
        false
    }

    fn dfs(remaining: &str, prev: u128) -> bool {
        if remaining.is_empty() {
            return true;
        }
        if prev == 0 {
            return false;
        }
        let target = prev - 1;
        for j in 1..=remaining.len() {
            let part = &remaining[0..j];
            if let Ok(val) = part.parse::<u128>() {
                if val == target && Self::dfs(&remaining[j..], val) {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (split-string s)
  (-> string? boolean?)
  (let* ((n (string-length s))
         (str s))
    (define (num-from start len)
      (string->number (substring str start (+ start len))))
    (define (dfs idx prev count)
      (cond
        [(= idx n) (>= count 2)]
        [(< prev 0) #f]
        [else
         (let loop ((len 1))
           (if (> (+ idx len) n)
               #f
               (let ((val (num-from idx len)))
                 (if (= val prev)
                     (or (dfs (+ idx len) (- prev 1) (+ count 1))
                         (loop (+ len 1)))
                     (loop (+ len 1))))))]))
    (let loop-first ((len 1))
      (if (>= len n)
          #f
          (let ((first-val (num-from 0 len)))
            (if (dfs len (- first-val 1) 1)
                #t
                (loop-first (+ len 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([split_string/1]).

-spec split_string(S :: unicode:unicode_binary()) -> boolean().
split_string(S) ->
    Len = byte_size(S),
    try_first(1, Len - 1, S).

try_first(Pos, MaxPos, _Bin) when Pos > MaxPos ->
    false;
try_first(Pos, MaxPos, Bin) ->
    Prefix = binary:part(Bin, {0, Pos}),
    Rest = binary:part(Bin, {Pos, byte_size(Bin) - Pos}),
    FirstVal = binary_to_integer(Prefix),
    case try_rest(FirstVal, Rest, 1) of
        true -> true;
        false -> try_first(Pos + 1, MaxPos, Bin)
    end.

try_rest(_Prev, <<>>, Count) ->
    Count >= 2;
try_rest(Prev, RestBin, Count) ->
    Expected = Prev - 1,
    if Expected < 0 ->
            false;
       true ->
            match_len(1, byte_size(RestBin), Expected, RestBin, Count)
    end.

match_len(Pos, MaxPos, _Expected, _RestBin, _Count) when Pos > MaxPos ->
    false;
match_len(Pos, MaxPos, Expected, RestBin, Count) ->
    Prefix = binary:part(RestBin, {0, Pos}),
    Value = binary_to_integer(Prefix),
    case Value == Expected of
        true ->
            Suffix = binary:part(RestBin, {Pos, byte_size(RestBin) - Pos}),
            case try_rest(Expected, Suffix, Count + 1) of
                true -> true;
                false -> match_len(Pos + 1, MaxPos, Expected, RestBin, Count)
            end;
        false ->
            match_len(Pos + 1, MaxPos, Expected, RestBin, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_string(s :: String.t) :: boolean
  def split_string(s) do
    len = String.length(s)

    1..(len - 1)
    |> Enum.any?(fn i ->
      {first_str, rest} = String.split_at(s, i)
      first_val = String.to_integer(first_str)
      dfs(rest, first_val - 1, 1)
    end)
  end

  defp dfs("", _expected, count), do: count >= 2
  defp dfs(_rem, expected, _count) when expected < 0, do: false

  defp dfs(rem, expected, count) do
    max = String.length(rem)

    1..max
    |> Enum.reduce_while(false, fn i, _acc ->
      {pref, rest} = String.split_at(rem, i)
      val = String.to_integer(pref)

      cond do
        val == expected ->
          if dfs(rest, expected - 1, count + 1) do
            {:halt, true}
          else
            {:cont, false}
          end

        val > expected ->
          {:halt, false}

        true ->
          {:cont, false}
      end
    end)
  end
end
```
