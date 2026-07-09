# 2981. Find Longest Special Substring That Occurs Thrice I

## Cpp

```cpp
class Solution {
public:
    int maximumLength(string s) {
        int n = s.size();
        vector<pair<char,int>> runs;
        for (int i = 0; i < n; ) {
            char c = s[i];
            int j = i;
            while (j < n && s[j] == c) ++j;
            runs.push_back({c, j - i});
            i = j;
        }
        for (int L = n; L >= 1; --L) {
            for (char ch = 'a'; ch <= 'z'; ++ch) {
                int occ = 0;
                for (auto &p : runs) {
                    if (p.first == ch && p.second >= L) {
                        occ += p.second - L + 1;
                        if (occ >= 3) return L;
                    }
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(String s) {
        int n = s.length();
        for (int len = n; len >= 1; --len) {
            for (char c = 'a'; c <= 'z'; ++c) {
                int total = 0;
                int i = 0;
                while (i < n) {
                    if (s.charAt(i) == c) {
                        int j = i;
                        while (j < n && s.charAt(j) == c) {
                            j++;
                        }
                        int run = j - i;
                        if (run >= len) {
                            total += run - len + 1;
                        }
                        i = j;
                    } else {
                        i++;
                    }
                }
                if (total >= 3) {
                    return len;
                }
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        cnt = defaultdict(int)
        n = len(s)
        for i in range(n):
            ch = s[i]
            length = 0
            for j in range(i, n):
                if s[j] == ch:
                    length += 1
                    cnt[(ch, length)] += 1
                else:
                    break
        ans = -1
        for (c, l), v in cnt.items():
            if v >= 3 and l > ans:
                ans = l
        return ans
```

## Python3

```python
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        chars = set(s)
        for L in range(n, 0, -1):
            for ch in chars:
                cnt = 0
                i = 0
                while i < n:
                    if s[i] == ch:
                        j = i
                        while j < n and s[j] == ch:
                            j += 1
                        run_len = j - i
                        if run_len >= L:
                            cnt += run_len - L + 1
                        i = j
                    else:
                        i += 1
                if cnt >= 3:
                    return L
        return -1
```

## C

```c
#include <string.h>

int maximumLength(char* s) {
    int n = strlen(s);
    int ans = -1;
    for (char ch = 'a'; ch <= 'z'; ++ch) {
        int cnt[51] = {0};
        for (int i = 0; i < n; ) {
            if (s[i] == ch) {
                int j = i;
                while (j < n && s[j] == ch) ++j;
                int L = j - i;
                for (int len = 1; len <= L; ++len) {
                    cnt[len] += L - len + 1;
                }
                i = j;
            } else {
                ++i;
            }
        }
        for (int len = n; len >= 1; --len) {
            if (cnt[len] >= 3 && len > ans) {
                ans = len;
                break; // larger lengths already checked
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaximumLength(string s) {
        int n = s.Length;
        for (int len = n; len >= 1; --len) {
            int[] cnt = new int[26];
            int i = 0;
            while (i < n) {
                char ch = s[i];
                int j = i;
                while (j < n && s[j] == ch) j++;
                int runLen = j - i;
                if (runLen >= len) {
                    cnt[ch - 'a'] += runLen - len + 1;
                }
                i = j;
            }
            foreach (int c in cnt) {
                if (c >= 3) return len;
            }
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maximumLength = function(s) {
    const n = s.length;
    // Build runs of consecutive identical characters
    const runs = [];
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        runs.push({ ch: s[i], len: j - i });
        i = j;
    }
    // Try lengths from longest to shortest
    for (let L = n; L >= 1; L--) {
        for (let code = 97; code <= 122; code++) { // 'a' to 'z'
            const c = String.fromCharCode(code);
            let occ = 0;
            for (const r of runs) {
                if (r.ch === c && r.len >= L) {
                    occ += r.len - L + 1;
                    if (occ >= 3) break;
                }
            }
            if (occ >= 3) return L;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function maximumLength(s: string): number {
    const n = s.length;
    const runs: { [key: string]: number[] } = {};

    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        const len = j - i;
        const ch = s[i];
        if (!runs[ch]) runs[ch] = [];
        runs[ch].push(len);
        i = j;
    }

    for (let L = n; L >= 1; L--) {
        for (const ch in runs) {
            let total = 0;
            for (const len of runs[ch]) {
                if (len >= L) total += len - L + 1;
                if (total >= 3) return L;
            }
        }
    }

    return -1;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maximumLength($s) {
        $n = strlen($s);
        $count = [];

        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $len = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] === $c) {
                    $len++;
                    $key = $c . '#' . $len;
                    if (isset($count[$key])) {
                        $count[$key]++;
                    } else {
                        $count[$key] = 1;
                    }
                } else {
                    break;
                }
            }
        }

        $ans = -1;
        foreach ($count as $key => $cnt) {
            if ($cnt >= 3) {
                $parts = explode('#', $key);
                $len = intval($parts[1]);
                if ($len > $ans) {
                    $ans = $len;
                }
            }
        }

        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func maximumLength(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cnt = Array(repeating: Array(repeating: 0, count: n + 1), count: 26)
        for i in 0..<n {
            let baseIdx = Int(chars[i].asciiValue! - Character("a").asciiValue!)
            var length = 0
            for j in i..<n {
                if chars[j] == chars[i] {
                    length += 1
                    cnt[baseIdx][length] += 1
                } else {
                    break
                }
            }
        }
        var ans = -1
        for idx in 0..<26 {
            for len in 1...n {
                if cnt[idx][len] >= 3 && len > ans {
                    ans = len
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(s: String): Int {
        val n = s.length
        val cnt = Array(26) { IntArray(n + 1) }
        var i = 0
        while (i < n) {
            val idx = s[i] - 'a'
            var j = i
            while (j < n && s[j] == s[i]) j++
            val runLen = j - i
            for (len in 1..runLen) {
                cnt[idx][len] += runLen - len + 1
            }
            i = j
        }
        var ans = -1
        for (c in 0 until 26) {
            for (len in n downTo 1) {
                if (cnt[c][len] >= 3 && len > ans) {
                    ans = len
                    break
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(String s) {
    int n = s.length;
    for (int len = n; len >= 1; --len) {
      for (int ci = 0; ci < 26; ++ci) {
        int target = 'a'.codeUnitAt(0) + ci;
        int occ = 0;
        int i = 0;
        while (i < n) {
          if (s.codeUnitAt(i) == target) {
            int j = i;
            while (j < n && s.codeUnitAt(j) == target) {
              ++j;
            }
            int run = j - i;
            if (run >= len) {
              occ += (run - len + 1);
            }
            i = j;
          } else {
            ++i;
          }
        }
        if (occ >= 3) return len;
      }
    }
    return -1;
  }
}
```

## Golang

```go
func maximumLength(s string) int {
	type key struct {
		c byte
		l int
	}
	cnt := make(map[key]int)
	n := len(s)

	for i := 0; i < n; i++ {
		ch := s[i]
		for j := i; j < n && s[j] == ch; j++ {
			k := key{c: ch, l: j - i + 1}
			cnt[k]++
		}
	}

	ans := -1
	for k, v := range cnt {
		if v >= 3 && k.l > ans {
			ans = k.l
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def maximum_length(s)
  n = s.length
  counts = Hash.new(0)

  (0...n).each do |i|
    c = s[i]
    len = 0
    j = i
    while j < n && s[j] == c
      len += 1
      counts[[c, len]] += 1
      j += 1
    end
  end

  ans = -1
  counts.each do |(_, l), freq|
    ans = l if freq >= 3 && l > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maximumLength(s: String): Int = {
        import scala.collection.mutable
        val n = s.length
        val cnt = mutable.Map[(Char, Int), Int]().withDefaultValue(0)
        for (i <- 0 until n) {
            var j = i
            while (j < n && s(j) == s(i)) {
                val len = j - i + 1
                cnt((s(i), len)) = cnt((s(i), len)) + 1
                j += 1
            }
        }
        var ans = -1
        for (((_, l), v) <- cnt) {
            if (v >= 3 && l > ans) ans = l
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut cnt: HashMap<(u8, usize), i32> = HashMap::new();

        for i in 0..n {
            let ch = bytes[i];
            let mut len = 0usize;
            for j in i..n {
                if bytes[j] == ch {
                    len += 1;
                    *cnt.entry((ch, len)).or_insert(0) += 1;
                } else {
                    break;
                }
            }
        }

        let mut ans: i32 = -1;
        for ((_, len), &c) in cnt.iter() {
            if c >= 3 && (*len as i32) > ans {
                ans = *len as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-length s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [h (make-hash)])
    (for ([start (in-range n)])
      (let ([c (string-ref s start)])
        (let loop ((end start) (len 0))
          (when (< end n)
            (if (char=? (string-ref s end) c)
                (let ([newlen (+ len 1)])
                  (define key (vector c newlen))
                  (hash-update! h key (lambda (v) (+ v 1)) 0)
                  (loop (+ end 1) newlen))
                (void))))))
    (let ([ans -1])
      (hash-for-each h
        (lambda (k v)
          (when (and (>= v 3)
                     (> (vector-ref k 1) ans))
            (set! ans (vector-ref k 1)))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/1]).

-spec maximum_length(S :: unicode:unicode_binary()) -> integer().
maximum_length(S) ->
    List = binary_to_list(S),
    N = length(List),
    Map = build_map(List, 0, N, #{}),
    find_max(Map).

build_map(_List, Index, N, Map) when Index >= N ->
    Map;
build_map(List, Index, N, Map) ->
    Char = lists:nth(Index + 1, List),
    UpdatedMap = extend_same(Char, Index, List, N, 0, Map),
    build_map(List, Index + 1, N, UpdatedMap).

extend_same(_Char, StartIdx, _List, N, LenSoFar, Map) when StartIdx + LenSoFar >= N ->
    Map;
extend_same(Char, StartIdx, List, N, LenSoFar, Map) ->
    Pos = StartIdx + LenSoFar,
    C = lists:nth(Pos + 1, List),
    case C == Char of
        true ->
            NewLen = LenSoFar + 1,
            Key = {Char, NewLen},
            UpdatedMap = case maps:is_key(Key, Map) of
                true -> maps:put(Key, maps:get(Key, Map) + 1, Map);
                false -> maps:put(Key, 1, Map)
            end,
            extend_same(Char, StartIdx, List, N, NewLen, UpdatedMap);
        false ->
            Map
    end.

find_max(Map) ->
    maps:fold(
        fun({_Char, Len}, Count, Acc) ->
            if Count >= 3 andalso Len > Acc -> Len;
               true -> Acc
            end
        end,
        -1,
        Map
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(s :: String.t()) :: integer
  def maximum_length(s) do
    len = byte_size(s)

    counts =
      Enum.reduce(0..len - 1, %{}, fn i, acc ->
        c = :binary.at(s, i)

        {new_acc, _} =
          Enum.reduce_while(i..len - 1, {acc, 0}, fn j, {map, cur_len} ->
            if :binary.at(s, j) == c do
              new_len = cur_len + 1
              key = {c, new_len}
              updated_map = Map.update(map, key, 1, &(&1 + 1))
              {:cont, {updated_map, new_len}}
            else
              {:halt, {map, cur_len}}
            end
          end)

        new_acc
      end)

    Enum.reduce(counts, -1, fn {{_c, l}, cnt}, best ->
      if cnt >= 3 and l > best, do: l, else: best
    end)
  end
end
```
