# 2785. Sort Vowels in a String

## Cpp

```cpp
class Solution {
public:
    string sortVowels(string s) {
        const string order = "AEIOUaeiou";
        int cnt[128] = {0};
        bool isVowel[128] = {false};
        for (char c : order) isVowel[(int)c] = true;
        for (char c : s) if (isVowel[(int)c]) ++cnt[(int)c];
        string ans;
        ans.reserve(s.size());
        int idx = 0;
        while (idx < 10 && cnt[(int)order[idx]] == 0) ++idx;
        for (char c : s) {
            if (isVowel[(int)c]) {
                while (idx < 10 && cnt[(int)order[idx]] == 0) ++idx;
                ans.push_back(order[idx]);
                --cnt[(int)order[idx]];
            } else {
                ans.push_back(c);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String sortVowels(String s) {
        int[] cnt = new int[128];
        String vowelOrder = "AEIOUaeiou";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (isVowel(c)) {
                cnt[c]++;
            }
        }
        StringBuilder sb = new StringBuilder(s.length());
        int idx = 0;
        // advance to first available vowel
        while (idx < 10 && cnt[vowelOrder.charAt(idx)] == 0) {
            idx++;
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (isVowel(c)) {
                while (idx < 10 && cnt[vowelOrder.charAt(idx)] == 0) {
                    idx++;
                }
                char replace = vowelOrder.charAt(idx);
                sb.append(replace);
                cnt[replace]--;
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
```

## Python

```python
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = set('AEIOUaeiou')
        order = 'AEIOUaeiou'
        cnt = {}
        for ch in s:
            if ch in vowels_set:
                cnt[ch] = cnt.get(ch, 0) + 1

        res = []
        idx = 0
        # advance to first available vowel
        while idx < len(order) and cnt.get(order[idx], 0) == 0:
            idx += 1

        for ch in s:
            if ch not in vowels_set:
                res.append(ch)
            else:
                while idx < len(order) and cnt.get(order[idx], 0) == 0:
                    idx += 1
                v = order[idx]
                res.append(v)
                cnt[v] -= 1

        return ''.join(res)
```

## Python3

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_order = "AEIOUaeiou"
        counts = {c: 0 for c in vowel_order}
        vowel_set = set(vowel_order)

        for ch in s:
            if ch in vowel_set:
                counts[ch] += 1

        idx = 0
        res = []
        for ch in s:
            if ch in vowel_set:
                while idx < len(vowel_order) and counts[vowel_order[idx]] == 0:
                    idx += 1
                v = vowel_order[idx]
                res.append(v)
                counts[v] -= 1
            else:
                res.append(ch)

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int vowelIndex(char c) {
    switch (c) {
        case 'A': return 0;
        case 'E': return 1;
        case 'I': return 2;
        case 'O': return 3;
        case 'U': return 4;
        case 'a': return 5;
        case 'e': return 6;
        case 'i': return 7;
        case 'o': return 8;
        case 'u': return 9;
        default:  return -1;
    }
}

char* sortVowels(char* s) {
    if (!s) return NULL;

    int freq[10] = {0};
    for (int i = 0; s[i]; ++i) {
        int idx = vowelIndex(s[i]);
        if (idx != -1) freq[idx]++;
    }

    size_t n = strlen(s);
    char *res = (char *)malloc(n + 1);
    if (!res) return NULL;

    const char *order = "AEIOUaeiou";
    int cur = 0;
    for (size_t i = 0; i < n; ++i) {
        int idx = vowelIndex(s[i]);
        if (idx == -1) {
            res[i] = s[i];
        } else {
            while (cur < 10 && freq[cur] == 0) cur++;
            res[i] = order[cur];
            freq[cur]--;
        }
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string SortVowels(string s)
    {
        char[] order = new char[] { 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' };
        int[] cnt = new int[10];

        foreach (char c in s)
        {
            int idx = GetVowelIndex(c);
            if (idx != -1) cnt[idx]++;
        }

        var sb = new System.Text.StringBuilder(s.Length);
        int p = 0;
        foreach (char c in s)
        {
            int idx = GetVowelIndex(c);
            if (idx == -1)
            {
                sb.Append(c);
            }
            else
            {
                while (p < 10 && cnt[p] == 0) p++;
                sb.Append(order[p]);
                cnt[p]--;
            }
        }

        return sb.ToString();
    }

    private int GetVowelIndex(char c)
    {
        switch (c)
        {
            case 'A': return 0;
            case 'E': return 1;
            case 'I': return 2;
            case 'O': return 3;
            case 'U': return 4;
            case 'a': return 5;
            case 'e': return 6;
            case 'i': return 7;
            case 'o': return 8;
            case 'u': return 9;
            default: return -1;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {
    const isVowel = (ch) => {
        return ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u' ||
               ch === 'A' || ch === 'E' || ch === 'I' || ch === 'O' || ch === 'U';
    };
    
    const order = ['A','E','I','O','U','a','e','i','o','u']; // ASCII ascending
    const cnt = {
        'A':0,'E':0,'I':0,'O':0,'U':0,
        'a':0,'e':0,'i':0,'o':0,'u':0
    };
    
    for (let ch of s) {
        if (isVowel(ch)) cnt[ch]++;
    }
    
    const res = [];
    let ptr = 0;
    for (let ch of s) {
        if (!isVowel(ch)) {
            res.push(ch);
        } else {
            while (ptr < order.length && cnt[order[ptr]] === 0) ptr++;
            const v = order[ptr];
            res.push(v);
            cnt[v]--;
        }
    }
    
    return res.join('');
};
```

## Typescript

```typescript
function sortVowels(s: string): string {
    const vowelOrder = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'];
    const idxMap: { [k: string]: number } = {
        A: 0, E: 1, I: 2, O: 3, U: 4,
        a: 5, e: 6, i: 7, o: 8, u: 9
    };
    const cnt = new Array(10).fill(0);
    for (let i = 0; i < s.length; ++i) {
        const ch = s[i];
        if (idxMap.hasOwnProperty(ch)) cnt[idxMap[ch]]++;
    }
    let ptr = 0;
    while (ptr < 10 && cnt[ptr] === 0) ++ptr;
    const res: string[] = [];
    for (let i = 0; i < s.length; ++i) {
        const ch = s[i];
        if (idxMap.hasOwnProperty(ch)) {
            while (ptr < 10 && cnt[ptr] === 0) ++ptr;
            res.push(vowelOrder[ptr]);
            cnt[ptr]--;
        } else {
            res.push(ch);
        }
    }
    return res.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortVowels($s) {
        $vowelOrder = ['A','E','I','O','U','a','e','i','o','u'];
        // Initialize counts for each vowel
        $counts = array_fill_keys($vowelOrder, 0);
        
        $len = strlen($s);
        // Count frequencies of vowels in the string
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (isset($counts[$ch])) {
                $counts[$ch]++;
            }
        }
        
        $result = '';
        $idx = 0; // pointer in vowelOrder
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (!isset($counts[$ch])) {
                $result .= $ch;
            } else {
                while ($idx < 10 && $counts[$vowelOrder[$idx]] == 0) {
                    $idx++;
                }
                $chosen = $vowelOrder[$idx];
                $result .= $chosen;
                $counts[$chosen]--;
            }
        }
        
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sortVowels(_ s: String) -> String {
        func isVowel(_ c: Character) -> Bool {
            switch c {
            case "a","e","i","o","u","A","E","I","O","U":
                return true
            default:
                return false
            }
        }
        
        // Count frequencies of each vowel (ASCII range fits in 128)
        var cnt = [Int](repeating: 0, count: 128)
        for ch in s {
            if isVowel(ch) {
                let ascii = Int(ch.unicodeScalars.first!.value)
                cnt[ascii] += 1
            }
        }
        
        // Vowels sorted by ASCII order
        let sortedVowels: [Character] = Array("AEIOUaeiou")
        var idx = 0
        
        var result = [Character]()
        result.reserveCapacity(s.count)
        
        for ch in s {
            if isVowel(ch) {
                // Find next available vowel in sorted order
                while idx < sortedVowels.count &&
                        cnt[Int(sortedVowels[idx].unicodeScalars.first!.value)] == 0 {
                    idx += 1
                }
                let v = sortedVowels[idx]
                result.append(v)
                cnt[Int(v.unicodeScalars.first!.value)] -= 1
            } else {
                result.append(ch)
            }
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortVowels(s: String): String {
        val vowelsOrder = "AEIOUaeiou"
        val cnt = IntArray(128)
        for (ch in s) {
            if (isVowel(ch)) cnt[ch.code]++
        }
        val sb = StringBuilder(s.length)
        var idx = 0
        while (idx < vowelsOrder.length && cnt[vowelsOrder[idx].code] == 0) idx++
        for (ch in s) {
            if (!isVowel(ch)) {
                sb.append(ch)
            } else {
                while (idx < vowelsOrder.length && cnt[vowelsOrder[idx].code] == 0) idx++
                val v = vowelsOrder[idx]
                sb.append(v)
                cnt[v.code]--
            }
        }
        return sb.toString()
    }

    private fun isVowel(c: Char): Boolean {
        return when (c) {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U' -> true
            else -> false
        }
    }
}
```

## Dart

```dart
class Solution {
  String sortVowels(String s) {
    const String vowelOrder = 'AEIOUaeiou';
    const Map<String, int> idxMap = {
      'A': 0,
      'E': 1,
      'I': 2,
      'O': 3,
      'U': 4,
      'a': 5,
      'e': 6,
      'i': 7,
      'o': 8,
      'u': 9,
    };

    List<int> cnt = List.filled(10, 0);
    for (int i = 0; i < s.length; ++i) {
      final String ch = s[i];
      final int? idx = idxMap[ch];
      if (idx != null) cnt[idx]++;
    }

    int curIdx = 0;
    while (curIdx < 10 && cnt[curIdx] == 0) curIdx++;

    final StringBuffer sb = StringBuffer();
    for (int i = 0; i < s.length; ++i) {
      final String ch = s[i];
      if (!idxMap.containsKey(ch)) {
        sb.write(ch);
      } else {
        while (curIdx < 10 && cnt[curIdx] == 0) curIdx++;
        sb.write(vowelOrder[curIdx]);
        cnt[curIdx]--;
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
func sortVowels(s string) string {
	isVowel := func(c byte) bool {
		switch c {
		case 'a', 'e', 'i', 'o', 'u',
			'A', 'E', 'I', 'O', 'U':
			return true
		}
		return false
	}

	counts := make([]int, 128)
	for i := 0; i < len(s); i++ {
		c := s[i]
		if isVowel(c) {
			counts[c]++
		}
	}

	order := []byte{'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
	idx := 0
	for idx < len(order) && counts[order[idx]] == 0 {
		idx++
	}

	res := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if isVowel(c) {
			for idx < len(order) && counts[order[idx]] == 0 {
				idx++
			}
			res[i] = order[idx]
			counts[order[idx]]--
		} else {
			res[i] = c
		}
	}

	return string(res)
}
```

## Ruby

```ruby
def sort_vowels(s)
  vowels = "AEIOUaeiou"
  freq = Hash.new(0)
  s.each_char { |ch| freq[ch] += 1 if vowels.include?(ch) }

  idx = 0
  result = +""
  s.each_char do |ch|
    if vowels.include?(ch)
      idx += 1 while idx < vowels.length && freq[vowels[idx]] == 0
      result << vowels[idx]
      freq[vowels[idx]] -= 1
    else
      result << ch
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  private val vowelSet = Set('a','e','i','o','u','A','E','I','O','U')
  def sortVowels(s: String): String = {
    val cnt = new Array[Int](128)
    for (c <- s) if (vowelSet(c)) cnt(c) += 1

    val order = "AEIOUaeiou"
    var idx = 0
    val sb = new StringBuilder(s.length)

    for (c <- s) {
      if (vowelSet(c)) {
        while (idx < order.length && cnt(order.charAt(idx)) == 0) idx += 1
        val v = order.charAt(idx)
        sb.append(v)
        cnt(v) -= 1
      } else {
        sb.append(c)
      }
    }
    sb.toString()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_vowels(s: String) -> String {
        // Vowel order according to ASCII values
        const VOWELS: [char; 10] = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'];
        
        fn vowel_index(c: char) -> Option<usize> {
            match c {
                'A' => Some(0),
                'E' => Some(1),
                'I' => Some(2),
                'O' => Some(3),
                'U' => Some(4),
                'a' => Some(5),
                'e' => Some(6),
                'i' => Some(7),
                'o' => Some(8),
                'u' => Some(9),
                _ => None,
            }
        }

        // Count frequencies of each vowel
        let mut cnt = [0usize; 10];
        for ch in s.chars() {
            if let Some(idx) = vowel_index(ch) {
                cnt[idx] += 1;
            }
        }

        // Build the resulting string, placing vowels in sorted order
        let mut result = String::with_capacity(s.len());
        let mut cur = 0usize; // points to smallest remaining vowel
        for ch in s.chars() {
            if vowel_index(ch).is_some() {
                while cur < 10 && cnt[cur] == 0 {
                    cur += 1;
                }
                // cur is guaranteed to be valid because we have a matching count
                result.push(VOWELS[cur]);
                cnt[cur] -= 1;
            } else {
                result.push(ch);
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (sort-vowels s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [counts (make-vector 10 0)]
         [sorted-vowels (vector #\A #\E #\I #\O #\U #\a #\e #\i #\o #\u)])
    ;; Count vowels
    (let loop ((i 0))
      (when (< i n)
        (let* ([c (string-ref s i)]
               [idx (cond [(char=? c #\A) 0]
                          [(char=? c #\E) 1]
                          [(char=? c #\I) 2]
                          [(char=? c #\O) 3]
                          [(char=? c #\U) 4]
                          [(char=? c #\a) 5]
                          [(char=? c #\e) 6]
                          [(char=? c #\i) 7]
                          [(char=? c #\o) 8]
                          [(char=? c #\u) 9]
                          [else -1])])
          (when (>= idx 0)
            (vector-set! counts idx (+ (vector-ref counts idx) 1))))
        (loop (+ i 1))))
    ;; Build result string
    (let ([res (make-string n)])
      (let loop2 ((i 0) (cur 0))
        (when (< i n)
          (let* ([c (string-ref s i)]
                 [idx (cond [(char=? c #\A) 0]
                            [(char=? c #\E) 1]
                            [(char=? c #\I) 2]
                            [(char=? c #\O) 3]
                            [(char=? c #\U) 4]
                            [(char=? c #\a) 5]
                            [(char=? c #\e) 6]
                            [(char=? c #\i) 7]
                            [(char=? c #\o) 8]
                            [(char=? c #\u) 9]
                            [else -1])])
            (if (>= idx 0)
                ;; replace with next sorted vowel
                (let loop3 ((j cur))
                  (if (> (vector-ref counts j) 0)
                      (begin
                        (string-set! res i (vector-ref sorted-vowels j))
                        (vector-set! counts j (- (vector-ref counts j) 1))
                        (loop2 (+ i 1) j))
                      (loop3 (+ j 1))))
                ;; consonant, keep as is
                (begin
                  (string-set! res i c)
                  (loop2 (+ i 1) cur))))))
      res)))
```

## Erlang

```erlang
-module(solution).
-export([sort_vowels/1]).
-define(VOWELS, [$A,$E,$I,$O,$U,$a,$e,$i,$o,$u]).

-spec sort_vowels(unicode:unicode_binary()) -> unicode:unicode_binary().
sort_vowels(S) ->
    Counts0 = #{ $A=>0, $E=>0, $I=>0, $O=>0, $U=>0,
                $a=>0, $e=>0, $i=>0, $o=>0, $u=>0 },
    Counts = count_vowels(S, Counts0),
    ResultList = rebuild(S, Counts, 0),
    iolist_to_binary(ResultList).

%% Count vowels in the binary
-spec count_vowels(binary(), map()) -> map().
count_vowels(<<>>, Map) ->
    Map;
count_vowels(<<C, Rest/binary>>, Map) ->
    case is_vowel(C) of
        true ->
            Count = maps:get(C, Map),
            NewMap = maps:put(C, Count + 1, Map),
            count_vowels(Rest, NewMap);
        false ->
            count_vowels(Rest, Map)
    end.

%% Rebuild the string with sorted vowels
-spec rebuild(binary(), map(), non_neg_integer()) -> iolist().
rebuild(<<>>, _Counts, _Idx) ->
    [];
rebuild(<<C, Rest/binary>>, Counts, Idx) ->
    if is_vowel(C) ->
            {VChar, NewCounts, NewIdx} = next_vowel(Idx, ?VOWELS, Counts),
            [VChar | rebuild(Rest, NewCounts, NewIdx)];
       true ->
            [C | rebuild(Rest, Counts, Idx)]
    end.

%% Find the next vowel with remaining count
-spec next_vowel(non_neg_integer(), list(integer()), map()) -> {integer(), map(), non_neg_integer()}.
next_vowel(Idx, Vowels, Counts) when Idx < length(Vowels) ->
    Char = lists:nth(Idx + 1, Vowels),
    case maps:get(Char, Counts) of
        Cnt when Cnt > 0 ->
            NewCounts = maps:put(Char, Cnt - 1, Counts),
            {Char, NewCounts, Idx};
        _ ->
            next_vowel(Idx + 1, Vowels, Counts)
    end.

%% Check if a character is a vowel
-spec is_vowel(integer()) -> boolean().
is_vowel(C) ->
    case C of
        $a; $e; $i; $o; $u;
        $A; $E; $I; $O; $U -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_vowels(s :: String.t()) :: String.t()
  def sort_vowels(s) do
    chars = String.to_charlist(s)
    vowel_order = 'AEIOUaeiou'
    vowel_set = MapSet.new(vowel_order)

    counts =
      Enum.reduce(chars, %{}, fn c, acc ->
        if MapSet.member?(vowel_set, c) do
          Map.update(acc, c, 1, &(&1 + 1))
        else
          acc
        end
      end)

    {result_rev, _final_counts, _} =
      Enum.reduce(chars, {[], counts, 0}, fn c, {res, cnts, idx} ->
        if MapSet.member?(vowel_set, c) do
          {idx2, cnts2} = advance_idx(vowel_order, cnts, idx)
          v_char = Enum.at(vowel_order, idx2)
          updated_cnts = Map.update!(cnts2, v_char, &(&1 - 1))
          {[v_char | res], updated_cnts, idx2}
        else
          {[c | res], cnts, idx}
        end
      end)

    result_rev |> Enum.reverse() |> List.to_string()
  end

  defp advance_idx(vowel_order, counts, idx) do
    len = length(vowel_order)

    if idx < len && Map.get(counts, Enum.at(vowel_order, idx), 0) == 0 do
      advance_idx(vowel_order, counts, idx + 1)
    else
      {idx, counts}
    end
  end
end
```
