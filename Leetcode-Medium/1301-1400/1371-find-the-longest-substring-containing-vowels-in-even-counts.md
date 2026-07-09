# 1371. Find the Longest Substring Containing Vowels in Even Counts

## Cpp

```cpp
class Solution {
public:
    int findTheLongestSubstring(string s) {
        // masks for vowels a, e, i, o, u
        static const int vowelMask[26] = {
            /*a*/1, 0, 0,
            /*d*/0, /*e*/2, 0,
            /*g*/0, 0, /*i*/4, 0, 0, 0,
            /*m*/0, 0, 0, /*p*/0, /*q*/0, /*r*/0,
            /*s*/0, /*t*/0, /*u*/16, 0, 0, 0, 0, 0
        };
        // Note: above initializer only fills first few entries; better compute dynamically.
        // We'll compute mask on the fly using a switch for clarity.
        
        vector<int> firstPos(32, INT_MAX);
        firstPos[0] = -1;
        int mask = 0;
        int best = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            char c = s[i];
            switch (c) {
                case 'a': mask ^= 1 << 0; break;
                case 'e': mask ^= 1 << 1; break;
                case 'i': mask ^= 1 << 2; break;
                case 'o': mask ^= 1 << 3; break;
                case 'u': mask ^= 1 << 4; break;
                default: break;
            }
            if (firstPos[mask] == INT_MAX) {
                firstPos[mask] = i;
            } else {
                best = max(best, i - firstPos[mask]);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int findTheLongestSubstring(String s) {
        int[] firstIdx = new int[32];
        java.util.Arrays.fill(firstIdx, Integer.MAX_VALUE);
        firstIdx[0] = -1; // prefix before any character
        
        int mask = 0;
        int maxLen = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case 'a': mask ^= 1; break;
                case 'e': mask ^= 2; break;
                case 'i': mask ^= 4; break;
                case 'o': mask ^= 8; break;
                case 'u': mask ^= 16; break;
                default: // consonants do not affect the mask
                    break;
            }
            if (firstIdx[mask] != Integer.MAX_VALUE) {
                maxLen = Math.max(maxLen, i - firstIdx[mask]);
            } else {
                firstIdx[mask] = i;
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mask = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        first_occurrence = [-2] * 32
        first_occurrence[0] = -1
        cur = 0
        longest = 0
        for i, ch in enumerate(s):
            cur ^= mask.get(ch, 0)
            if first_occurrence[cur] == -2:
                first_occurrence[cur] = i
            else:
                longest = max(longest, i - first_occurrence[cur])
        return longest
```

## Python3

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        first = [-2] * 32
        first[0] = -1
        vowel_mask = [0] * 26
        for ch, m in zip('aeiou', [1, 2, 4, 8, 16]):
            vowel_mask[ord(ch) - 97] = m

        res = 0
        for i, ch in enumerate(s):
            mask ^= vowel_mask[ord(ch) - 97]
            if first[mask] != -2:
                res = max(res, i - first[mask])
            else:
                first[mask] = i
        return res
```

## C

```c
#include <string.h>
#include <limits.h>

int findTheLongestSubstring(char* s) {
    int firstPos[32];
    for (int i = 0; i < 32; ++i) firstPos[i] = INT_MIN;
    firstPos[0] = -1;               // empty prefix
    int mask = 0, best = 0;

    for (int i = 0; s[i]; ++i) {
        switch (s[i]) {
            case 'a': mask ^= 1;   break;
            case 'e': mask ^= 2;   break;
            case 'i': mask ^= 4;   break;
            case 'o': mask ^= 8;   break;
            case 'u': mask ^= 16;  break;
        }
        if (firstPos[mask] != INT_MIN) {
            int len = i - firstPos[mask];
            if (len > best) best = len;
        } else {
            firstPos[mask] = i;
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindTheLongestSubstring(string s)
    {
        int[] first = new int[32];
        for (int i = 0; i < 32; i++) first[i] = -2;
        first[0] = -1;

        int mask = 0, maxLen = 0;
        for (int i = 0; i < s.Length; i++)
        {
            char c = s[i];
            switch (c)
            {
                case 'a': mask ^= 1; break;
                case 'e': mask ^= 2; break;
                case 'i': mask ^= 4; break;
                case 'o': mask ^= 8; break;
                case 'u': mask ^= 16; break;
            }

            if (first[mask] != -2)
            {
                int len = i - first[mask];
                if (len > maxLen) maxLen = len;
            }
            else
            {
                first[mask] = i;
            }
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    const maskMap = {a:1, e:2, i:4, o:8, u:16};
    const firstIdx = new Int32Array(32);
    for (let i = 0; i < 32; ++i) firstIdx[i] = -2;
    firstIdx[0] = -1; // prefix mask 0 occurs before the string starts
    let curMask = 0;
    let maxLen = 0;
    for (let i = 0; i < s.length; ++i) {
        const m = maskMap[s[i]];
        if (m !== undefined) curMask ^= m;
        if (firstIdx[curMask] === -2) {
            firstIdx[curMask] = i; // store first occurrence
        } else {
            const len = i - firstIdx[curMask];
            if (len > maxLen) maxLen = len;
        }
    }
    return maxLen;
};
```

## Typescript

```typescript
function findTheLongestSubstring(s: string): number {
    const mask: { [k: string]: number } = { a: 1, e: 2, i: 4, o: 8, u: 16 };
    const firstPos = new Array(32).fill(-2);
    firstPos[0] = -1;
    let state = 0;
    let best = 0;
    for (let i = 0; i < s.length; ++i) {
        const m = mask[s[i]];
        if (m !== undefined) state ^= m;
        if (firstPos[state] !== -2) {
            const len = i - firstPos[state];
            if (len > best) best = len;
        } else {
            firstPos[state] = i;
        }
    }
    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function findTheLongestSubstring($s) {
        $maskMap = ['a'=>1,'e'=>2,'i'=>4,'o'=>8,'u'=>16];
        $first = array_fill(0, 32, null);
        $first[0] = -1; // initial state before any character
        $state = 0;
        $maxLen = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (isset($maskMap[$c])) {
                $state ^= $maskMap[$c];
            }
            if ($first[$state] !== null) {
                $len = $i - $first[$state];
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            } else {
                $first[$state] = $i;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func findTheLongestSubstring(_ s: String) -> Int {
        var maskMap: [Character: Int] = [
            "a": 1,
            "e": 2,
            "i": 4,
            "o": 8,
            "u": 16
        ]
        var firstPos = Array(repeating: -2, count: 32)
        firstPos[0] = -1   // empty prefix
        
        var curMask = 0
        var maxLen = 0
        
        for (idx, ch) in s.enumerated() {
            if let m = maskMap[ch] {
                curMask ^= m
            }
            if firstPos[curMask] != -2 {
                let length = idx - firstPos[curMask]
                if length > maxLen { maxLen = length }
            } else {
                firstPos[curMask] = idx
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheLongestSubstring(s: String): Int {
        val first = IntArray(32) { -2 }
        first[0] = -1
        var state = 0
        var ans = 0
        for (i in s.indices) {
            when (s[i]) {
                'a' -> state = state xor 1
                'e' -> state = state xor 2
                'i' -> state = state xor 4
                'o' -> state = state xor 8
                'u' -> state = state xor 16
            }
            if (first[state] != -2) {
                ans = maxOf(ans, i - first[state])
            } else {
                first[state] = i
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findTheLongestSubstring(String s) {
    const List<int> vowelMask = [
      0, // a
      0, // b
      0, // c
      0, // d
      1, // e (actually 'e' is 101)
    ];
    // We'll use switch for clarity.
    int mask = 0;
    List<int> firstPos = List.filled(32, -2);
    firstPos[0] = -1; // empty prefix
    int maxLen = 0;

    for (int i = 0; i < s.length; i++) {
      int code = s.codeUnitAt(i);
      switch (code) {
        case 97: // 'a'
          mask ^= 1;
          break;
        case 101: // 'e'
          mask ^= 2;
          break;
        case 105: // 'i'
          mask ^= 4;
          break;
        case 111: // 'o'
          mask ^= 8;
          break;
        case 117: // 'u'
          mask ^= 16;
          break;
      }

      if (firstPos[mask] == -2) {
        firstPos[mask] = i;
      } else {
        int len = i - firstPos[mask];
        if (len > maxLen) maxLen = len;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func findTheLongestSubstring(s string) int {
    const totalStates = 32
    first := make([]int, totalStates)
    for i := 0; i < totalStates; i++ {
        first[i] = -2 // sentinel for unseen state
    }
    first[0] = -1 // empty prefix has state 0 at index -1

    mask := 0
    maxLen := 0

    for i := 0; i < len(s); i++ {
        switch s[i] {
        case 'a':
            mask ^= 1
        case 'e':
            mask ^= 2
        case 'i':
            mask ^= 4
        case 'o':
            mask ^= 8
        case 'u':
            mask ^= 16
        }
        if first[mask] != -2 {
            length := i - first[mask]
            if length > maxLen {
                maxLen = length
            }
        } else {
            first[mask] = i
        }
    }

    return maxLen
}
```

## Ruby

```ruby
def find_the_longest_substring(s)
  mask_map = Array.new(26, 0)
  mask_map['a'.ord - 97] = 1
  mask_map['e'.ord - 97] = 2
  mask_map['i'.ord - 97] = 4
  mask_map['o'.ord - 97] = 8
  mask_map['u'.ord - 97] = 16

  first_occurrence = Array.new(32)
  first_occurrence[0] = -1

  cur_mask = 0
  max_len = 0

  s.each_char.with_index do |ch, idx|
    cur_mask ^= mask_map[ch.ord - 97]
    if first_occurrence[cur_mask].nil?
      first_occurrence[cur_mask] = idx
    else
      len = idx - first_occurrence[cur_mask]
      max_len = len if len > max_len
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def findTheLongestSubstring(s: String): Int = {
        val maskMap = new Array[Int](26)
        maskMap('a' - 'a') = 1
        maskMap('e' - 'a') = 2
        maskMap('i' - 'a') = 4
        maskMap('o' - 'a') = 8
        maskMap('u' - 'a') = 16

        val firstIdx = Array.fill(32)(Int.MaxValue)
        var curMask = 0
        var maxLen = 0
        firstIdx(0) = -1

        for (i <- 0 until s.length) {
            curMask ^= maskMap(s.charAt(i) - 'a')
            if (firstIdx(curMask) != Int.MaxValue) {
                val len = i - firstIdx(curMask)
                if (len > maxLen) maxLen = len
            } else {
                firstIdx(curMask) = i
            }
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        let mut first = [-1_i32; 32];
        first[0] = 0;
        let mut mask: usize = 0;
        let mut ans: i32 = 0;
        for (i, ch) in s.chars().enumerate() {
            mask ^= match ch {
                'a' => 1,
                'e' => 2,
                'i' => 4,
                'o' => 8,
                'u' => 16,
                _ => 0,
            };
            let pos = (i + 1) as i32;
            if first[mask] == -1 {
                first[mask] = pos;
            } else {
                let len = pos - first[mask];
                if len > ans {
                    ans = len;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-the-longest-substring s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [mp (make-vector 32 -1)]   ; first occurrence of each mask, -1 means unseen
         [cur 0]
         [best 0])
    ;; mp[0] stays -1 to represent the position before the string starts
    (for ([i (in-range n)])
      (define ch (string-ref s i))
      (define mask
        (cond [(char=? ch #\a) 1]
              [(char=? ch #\e) 2]
              [(char=? ch #\i) 4]
              [(char=? ch #\o) 8]
              [(char=? ch #\u) 16]
              [else 0]))
      (set! cur (bitwise-xor cur mask))
      (define first (vector-ref mp cur))
      (if (= first -1)
          (if (= cur 0)
              (when (> (+ i 1) best) (set! best (+ i 1)))
              (vector-set! mp cur i))
          (let ([len (- i first)])
            (when (> len best) (set! best len)))))
    best))
```

## Erlang

```erlang
-spec find_the_longest_substring(S :: unicode:unicode_binary()) -> integer().
find_the_longest_substring(S) ->
    loop(S, 0, 0, #{0 => -1}, 0).

loop(<<>>, _Pos, _Xor, _Map, MaxLen) ->
    MaxLen;
loop(<<Char:8, Rest/binary>>, Pos, Xor, Map, MaxLen) ->
    Mask = case Char of
        $a -> 1;
        $e -> 2;
        $i -> 4;
        $o -> 8;
        $u -> 16;
        _   -> 0
    end,
    NewXor = Xor bxor Mask,
    case maps:get(NewXor, Map, undefined) of
        undefined ->
            NewMap = maps:put(NewXor, Pos, Map),
            loop(Rest, Pos + 1, NewXor, NewMap, MaxLen);
        FirstIdx ->
            Len = Pos - FirstIdx,
            NewMax = if Len > MaxLen -> Len; true -> MaxLen end,
            loop(Rest, Pos + 1, NewXor, Map, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_longest_substring(s :: String.t()) :: integer
  def find_the_longest_substring(s) do
    chars = :binary.bin_to_list(s)

    {_mask, _first_map, max_len} =
      Enum.reduce(Enum.with_index(chars), {0, %{0 => -1}, 0},
        fn {ch, idx}, {mask, first, max_len} ->
          mask =
            case ch do
              ?a -> mask ^ 1
              ?e -> mask ^ 2
              ?i -> mask ^ 4
              ?o -> mask ^ 8
              ?u -> mask ^ 16
              _ -> mask
            end

          {first, start_idx} =
            case Map.fetch(first, mask) do
              {:ok, sidx} -> {first, sidx}
              :error ->
                new_first = Map.put(first, mask, idx)
                {new_first, idx}
            end

          len = idx - start_idx
          max_len = if len > max_len, do: len, else: max_len
          {mask, first, max_len}
        end)

    max_len
  end
end
```
