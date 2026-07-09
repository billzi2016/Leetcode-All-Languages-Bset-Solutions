# 3039. Apply Operations to Make String Empty

## Cpp

```cpp
class Solution {
public:
    string lastNonEmptyString(string s) {
        const int n = s.size();
        vector<int> cnt(26, 0), lastPos(26, -1);
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            ++cnt[idx];
            lastPos[idx] = i;
        }
        int maxFreq = 0;
        for (int c : cnt) if (c > maxFreq) maxFreq = c;
        string res;
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            if (cnt[idx] == maxFreq && lastPos[idx] == i) {
                res.push_back(s[i]);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String lastNonEmptyString(String s) {
        int n = s.length();
        int[] cnt = new int[26];
        for (int i = 0; i < n; i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        int max = 0;
        for (int c : cnt) {
            if (c > max) max = c;
        }
        boolean[] isMax = new boolean[26];
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == max) isMax[i] = true;
        }
        int[] lastIdx = new int[26];
        for (int i = 0; i < 26; i++) lastIdx[i] = -1;
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (isMax[idx]) {
                lastIdx[idx] = i;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (isMax[idx] && lastIdx[idx] == i) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        freq = Counter(s)
        max_freq = max(freq.values())
        most_frequent = {ch for ch, cnt in freq.items() if cnt == max_freq}
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        result_chars = []
        for i, ch in enumerate(s):
            if ch in most_frequent and last_index[ch] == i:
                result_chars.append(ch)
        return ''.join(result_chars)
```

## Python3

```python
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        # Count frequencies
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        max_freq = max(freq)
        most_frequent = {chr(i + 97) for i, f in enumerate(freq) if f == max_freq}

        # Record last occurrence index for each character
        last_idx = {}
        for i, ch in enumerate(s):
            if ch in most_frequent:
                last_idx[ch] = i

        # Build result keeping only the last occurrence of each most frequent char
        res_chars = []
        for i, ch in enumerate(s):
            if ch in most_frequent and last_idx.get(ch) == i:
                res_chars.append(ch)

        return ''.join(res_chars)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* lastNonEmptyString(char* s) {
    int n = strlen(s);
    int freq[26] = {0};
    int last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;
    
    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        ++freq[idx];
        last[idx] = i;
    }
    
    int maxFreq = 0;
    for (int i = 0; i < 26; ++i)
        if (freq[i] > maxFreq) maxFreq = freq[i];
    
    char* res = (char*)malloc(n + 1);
    int pos = 0;
    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        if (freq[idx] == maxFreq && last[idx] == i)
            res[pos++] = s[i];
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LastNonEmptyString(string s) {
        int[] freq = new int[26];
        foreach (char ch in s) {
            freq[ch - 'a']++;
        }

        int maxFreq = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > maxFreq) maxFreq = freq[i];
        }

        bool[] isMax = new bool[26];
        for (int i = 0; i < 26; i++) {
            if (freq[i] == maxFreq) isMax[i] = true;
        }

        bool[] taken = new bool[26];
        var rev = new System.Collections.Generic.List<char>(s.Length);
        for (int i = s.Length - 1; i >= 0; i--) {
            int idx = s[i] - 'a';
            if (isMax[idx] && !taken[idx]) {
                rev.Add(s[i]);
                taken[idx] = true;
            }
        }

        var sb = new System.Text.StringBuilder(rev.Count);
        for (int i = rev.Count - 1; i >= 0; i--) {
            sb.Append(rev[i]);
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var lastNonEmptyString = function(s) {
    const n = s.length;
    const freq = new Array(26).fill(0);
    const lastIdx = new Array(26).fill(-1);
    
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i) - 97;
        freq[ch]++;
        lastIdx[ch] = i; // update to latest index
    }
    
    let maxFreq = 0;
    for (let f of freq) if (f > maxFreq) maxFreq = f;
    
    const keep = new Array(26).fill(false);
    for (let i = 0; i < 26; ++i) {
        if (freq[i] === maxFreq) keep[i] = true;
    }
    
    const res = [];
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i) - 97;
        if (keep[ch] && lastIdx[ch] === i) {
            res.push(s[i]);
        }
    }
    
    return res.join('');
};
```

## Typescript

```typescript
function lastNonEmptyString(s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let maxFreq = 0;
    for (const f of freq) {
        if (f > maxFreq) maxFreq = f;
    }
    const most = new Set<string>();
    for (let i = 0; i < 26; i++) {
        if (freq[i] === maxFreq) {
            most.add(String.fromCharCode(97 + i));
        }
    }
    const seen = new Set<string>();
    const res: string[] = [];
    for (let i = s.length - 1; i >= 0; i--) {
        const ch = s[i];
        if (most.has(ch) && !seen.has(ch)) {
            res.push(ch);
            seen.add(ch);
        }
    }
    return res.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function lastNonEmptyString($s) {
        $len = strlen($s);
        // frequency of each character
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        // maximum frequency
        $maxFreq = max($freq);

        // characters with maximum frequency
        $most = [];
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] === $maxFreq) {
                $most[chr(97 + $i)] = true;
            }
        }

        // last occurrence index of each most frequent character
        $lastIdx = [];
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (isset($most[$c])) {
                $lastIdx[$c] = $i;
            }
        }

        // build result keeping only the last occurrence of each most frequent character
        $resultChars = [];
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (isset($most[$c]) && $lastIdx[$c] === $i) {
                $resultChars[] = $c;
            }
        }

        return implode('', $resultChars);
    }
}
```

## Swift

```swift
class Solution {
    func lastNonEmptyString(_ s: String) -> String {
        let chars = Array(s)
        var freq = [Int](repeating: 0, count: 26)
        for ch in chars {
            if let v = ch.asciiValue {
                let idx = Int(v - Character("a").asciiValue!)
                freq[idx] += 1
            }
        }
        guard let maxFreq = freq.max() else { return "" }
        var lastIdx = [Int](repeating: -1, count: 26)
        for (i, ch) in chars.enumerated() {
            if let v = ch.asciiValue {
                let idx = Int(v - Character("a").asciiValue!)
                if freq[idx] == maxFreq {
                    lastIdx[idx] = i
                }
            }
        }
        var result = ""
        for (i, ch) in chars.enumerated() {
            if let v = ch.asciiValue {
                let idx = Int(v - Character("a").asciiValue!)
                if freq[idx] == maxFreq && lastIdx[idx] == i {
                    result.append(ch)
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lastNonEmptyString(s: String): String {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var maxFreq = 0
        for (f in freq) if (f > maxFreq) maxFreq = f

        val seen = BooleanArray(26)
        val selected = mutableListOf<Char>()
        for (i in s.length - 1 downTo 0) {
            val c = s[i]
            val idx = c - 'a'
            if (freq[idx] == maxFreq && !seen[idx]) {
                seen[idx] = true
                selected.add(c)
            }
        }
        val sb = StringBuilder()
        for (i in selected.size - 1 downTo 0) {
            sb.append(selected[i])
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String lastNonEmptyString(String s) {
    // Count frequencies of each character.
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      freq[s.codeUnitAt(i) - 97]++;
    }

    // Determine the maximum frequency.
    int maxFreq = 0;
    for (int f in freq) {
      if (f > maxFreq) maxFreq = f;
    }

    // Characters that have the maximum frequency.
    Set<int> maxChars = {};
    for (int i = 0; i < 26; ++i) {
      if (freq[i] == maxFreq) maxChars.add(i);
    }

    // Keep only the last occurrence of each such character.
    Set<int> seen = {};
    List<int> kept = [];
    for (int i = s.length - 1; i >= 0; --i) {
      int code = s.codeUnitAt(i) - 97;
      if (maxChars.contains(code) && !seen.contains(code)) {
        kept.add(code);
        seen.add(code);
      }
    }

    // Build the result in correct order.
    StringBuffer sb = StringBuffer();
    for (int i = kept.length - 1; i >= 0; --i) {
      sb.writeCharCode(kept[i] + 97);
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "sort"

func lastNonEmptyString(s string) string {
	var freq [26]int
	var lastIdx [26]int
	for i := 0; i < 26; i++ {
		lastIdx[i] = -1
	}
	for i, ch := range []byte(s) {
		idx := ch - 'a'
		freq[idx]++
		lastIdx[idx] = i
	}
	maxFreq := 0
	for _, f := range freq {
		if f > maxFreq {
			maxFreq = f
		}
	}
	type pair struct {
		idx int
		ch  byte
	}
	pairs := make([]pair, 0)
	for i, f := range freq {
		if f == maxFreq && f > 0 {
			pairs = append(pairs, pair{lastIdx[i], byte('a' + i)})
		}
	}
	sort.Slice(pairs, func(i, j int) bool { return pairs[i].idx < pairs[j].idx })
	res := make([]byte, len(pairs))
	for i, p := range pairs {
		res[i] = p.ch
	}
	return string(res)
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def last_non_empty_string(s)
  freq = Array.new(26, 0)
  last_idx = Array.new(26, -1)

  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    freq[idx] += 1
    last_idx[idx] = i
  end

  max_freq = freq.max
  result = []

  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    if freq[idx] == max_freq && last_idx[idx] == i
      result << ch
    end
  end

  result.join
end
```

## Scala

```scala
object Solution {
    def lastNonEmptyString(s: String): String = {
        val n = s.length
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        var maxFreq = 0
        for (f <- freq) if (f > maxFreq) maxFreq = f

        val lastIdx = new Array[Int](26)
        java.util.Arrays.fill(lastIdx, -1)
        for (i <- 0 until n) {
            val c = s.charAt(i) - 'a'
            if (freq(c) == maxFreq) {
                lastIdx(c) = i
            }
        }

        val sb = new StringBuilder
        for (i <- 0 until n) {
            val c = s.charAt(i) - 'a'
            if (freq(c) == maxFreq && lastIdx(c) == i) {
                sb.append(s.charAt(i))
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn last_non_empty_string(s: String) -> String {
        let bytes = s.as_bytes();
        let mut freq = [0usize; 26];
        for &b in bytes {
            freq[(b - b'a') as usize] += 1;
        }
        let max_freq = *freq.iter().max().unwrap();

        let mut is_max = [false; 26];
        for i in 0..26 {
            if freq[i] == max_freq {
                is_max[i] = true;
            }
        }

        // Record last occurrence index for characters with maximal frequency
        let mut last = [usize::MAX; 26];
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if is_max[idx] {
                last[idx] = i;
            }
        }

        // Build result keeping only the last occurrence of each maximal character
        let mut res: Vec<u8> = Vec::with_capacity(s.len());
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if is_max[idx] && last[idx] == i {
                res.push(b);
            }
        }

        // SAFETY: we only pushed original ASCII lowercase letters
        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (last-non-empty-string s)
  (-> string? string?)
  (let* ([len (string-length s)]
         [freq (make-vector 26 0)])
    ;; count frequencies
    (for ([i (in-range len)])
      (let* ([ch (char->integer (string-ref s i))]
             [idx (- ch (char->integer #\a))])
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    (define max-freq
      (apply max (vector->list freq)))
    ;; remaining counts copy
    (define rem (vector-copy freq))
    (define res '())
    (for ([i (in-range len)])
      (let* ([ch (string-ref s i)]
             [idx (- (char->integer ch) (char->integer #\a))])
        (vector-set! rem idx (- (vector-ref rem idx) 1))
        (when (and (= (vector-ref freq idx) max-freq)
                   (= (vector-ref rem idx) 0))
          (set! res (cons ch res)))))
    (list->string (reverse res))))
```

## Erlang

```erlang
-spec last_non_empty_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
last_non_empty_string(S) ->
    List = binary_to_list(S),
    Freq0 = array:new(26, {default, 0}),
    Freq = freq(List, Freq0),
    MaxFreq = max_freq(Freq, 0, 0),
    LastPos0 = array:new(26, {default, -1}),
    LastPos = build_lastpos(List, Freq, MaxFreq, 0, LastPos0),
    ResRev = collect_chars(List, Freq, MaxFreq, LastPos, 0, []),
    list_to_binary(lists:reverse(ResRev)).

freq([], Arr) -> Arr;
freq([C|Rest], Arr) ->
    Index = C - $a,
    Old = array:get(Index, Arr),
    freq(Rest, array:set(Index, Old + 1, Arr)).

max_freq(_Arr, I, Max) when I >= 26 -> Max;
max_freq(Arr, I, CurMax) ->
    Val = array:get(I, Arr),
    NewMax = if Val > CurMax -> Val; true -> CurMax end,
    max_freq(Arr, I + 1, NewMax).

build_lastpos([], _Freq, _MaxFreq, _Pos, Arr) -> Arr;
build_lastpos([C|Rest], Freq, MaxFreq, Pos, Arr) ->
    Index = C - $a,
    case array:get(Index, Freq) == MaxFreq of
        true -> NewArr = array:set(Index, Pos, Arr);
        false -> NewArr = Arr
    end,
    build_lastpos(Rest, Freq, MaxFreq, Pos + 1, NewArr).

collect_chars([], _Freq, _MaxFreq, _LastPos, _Pos, Acc) -> Acc;
collect_chars([C|Rest], Freq, MaxFreq, LastPos, Pos, Acc) ->
    Index = C - $a,
    case (array:get(Index, Freq) == MaxFreq) andalso
         (array:get(Index, LastPos) == Pos) of
        true -> collect_chars(Rest, Freq, MaxFreq, LastPos, Pos + 1, [C|Acc]);
        false -> collect_chars(Rest, Freq, MaxFreq, LastPos, Pos + 1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec last_non_empty_string(s :: String.t) :: String.t
  def last_non_empty_string(s) do
    chars = String.graphemes(s)

    freq =
      Enum.reduce(chars, %{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    maxfreq = freq |> Map.values() |> Enum.max()

    most_frequent_set =
      freq
      |> Enum.filter(fn {_ch, cnt} -> cnt == maxfreq end)
      |> Enum.map(fn {ch, _cnt} -> ch end)
      |> MapSet.new()

    last_idx =
      Enum.reduce(Enum.with_index(chars), %{}, fn {ch, idx}, acc ->
        if MapSet.member?(most_frequent_set, ch) do
          Map.put(acc, ch, idx)
        else
          acc
        end
      end)

    result_rev =
      Enum.reduce(Enum.with_index(chars), [], fn {ch, idx}, acc ->
        if MapSet.member?(most_frequent_set, ch) and Map.get(last_idx, ch) == idx do
          [ch | acc]
        else
          acc
        end
      end)

    result_rev
    |> Enum.reverse()
    |> Enum.join()
  end
end
```
