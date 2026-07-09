# 3541. Find Most Frequent Vowel and Consonant

## Cpp

```cpp
class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char,int> cnt;
        for(char c: s) cnt[c]++;
        unordered_set<char> vowels = {'a','e','i','o','u'};
        int maxVowel = 0, maxCons = 0;
        for (auto &p : cnt) {
            if (vowels.count(p.first))
                maxVowel = max(maxVowel, p.second);
            else
                maxCons = max(maxCons, p.second);
        }
        return maxVowel + maxCons;
    }
};
```

## Java

```java
class Solution {
    public int maxFreqSum(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        int maxVowel = 0, maxConsonant = 0;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue;
            char ch = (char) ('a' + i);
            if (isVowel(ch)) {
                if (cnt[i] > maxVowel) maxVowel = cnt[i];
            } else {
                if (cnt[i] > maxConsonant) maxConsonant = cnt[i];
            }
        }
        return maxVowel + maxConsonant;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel_set = set('aeiou')
        freq_vowel = 0
        freq_consonant = 0
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch, cnt in counts.items():
            if ch in vowel_set:
                if cnt > freq_vowel:
                    freq_vowel = cnt
            else:
                if cnt > freq_consonant:
                    freq_consonant = cnt
        return freq_vowel + freq_consonant
```

## Python3

```python
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        vowel_max = 0
        consonant_max = 0
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch, cnt in freq.items():
            if ch in vowels:
                if cnt > vowel_max:
                    vowel_max = cnt
            else:
                if cnt > consonant_max:
                    consonant_max = cnt
        return vowel_max + consonant_max
```

## C

```c
int maxFreqSum(char* s) {
    int freq[26] = {0};
    for (char *p = s; *p; ++p) {
        if (*p >= 'a' && *p <= 'z')
            freq[*p - 'a']++;
    }
    int isVowel[26] = {0};
    isVowel['a' - 'a'] = 1;
    isVowel['e' - 'a'] = 1;
    isVowel['i' - 'a'] = 1;
    isVowel['o' - 'a'] = 1;
    isVowel['u' - 'a'] = 1;

    int maxV = 0, maxC = 0;
    for (int i = 0; i < 26; ++i) {
        if (isVowel[i]) {
            if (freq[i] > maxV) maxV = freq[i];
        } else {
            if (freq[i] > maxC) maxC = freq[i];
        }
    }
    return maxV + maxC;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxFreqSum(string s) {
        int[] freq = new int[26];
        foreach (char c in s) {
            freq[c - 'a']++;
        }
        bool[] isVowel = new bool[26];
        isVowel['a' - 'a'] = true;
        isVowel['e' - 'a'] = true;
        isVowel['i' - 'a'] = true;
        isVowel['o' - 'a'] = true;
        isVowel['u' - 'a'] = true;

        int maxVowel = 0, maxConsonant = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) continue;
            if (isVowel[i]) {
                if (freq[i] > maxVowel) maxVowel = freq[i];
            } else {
                if (freq[i] > maxConsonant) maxConsonant = freq[i];
            }
        }
        return maxVowel + maxConsonant;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const freq = Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let maxVowel = 0, maxCons = 0;
    for (let i = 0; i < 26; i++) {
        const count = freq[i];
        if (count === 0) continue;
        const c = String.fromCharCode(i + 97);
        if (vowels.has(c)) {
            if (count > maxVowel) maxVowel = count;
        } else {
            if (count > maxCons) maxCons = count;
        }
    }
    return maxVowel + maxCons;
};
```

## Typescript

```typescript
function maxFreqSum(s: string): number {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const vowelCount = new Map<string, number>();
    const consonantCount = new Map<string, number>();

    for (const ch of s) {
        if (vowels.has(ch)) {
            vowelCount.set(ch, (vowelCount.get(ch) ?? 0) + 1);
        } else {
            consonantCount.set(ch, (consonantCount.get(ch) ?? 0) + 1);
        }
    }

    let maxVowel = 0;
    for (const cnt of vowelCount.values()) {
        if (cnt > maxVowel) maxVowel = cnt;
    }

    let maxConsonant = 0;
    for (const cnt of consonantCount.values()) {
        if (cnt > maxConsonant) maxConsonant = cnt;
    }

    return maxVowel + maxConsonant;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxFreqSum($s) {
        $vowelSet = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $freqVowel = [];
        $freqCons = [];

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (isset($vowelSet[$ch])) {
                $freqVowel[$ch] = ($freqVowel[$ch] ?? 0) + 1;
            } else {
                $freqCons[$ch] = ($freqCons[$ch] ?? 0) + 1;
            }
        }

        $maxVowel = 0;
        foreach ($freqVowel as $cnt) {
            if ($cnt > $maxVowel) $maxVowel = $cnt;
        }

        $maxConsonant = 0;
        foreach ($freqCons as $cnt) {
            if ($cnt > $maxConsonant) $maxConsonant = $cnt;
        }

        return $maxVowel + $maxConsonant;
    }
}
```

## Swift

```swift
class Solution {
    func maxFreqSum(_ s: String) -> Int {
        var counts = [Int](repeating: 0, count: 26)
        let aValue = Character("a").unicodeScalars.first!.value
        for ch in s {
            if let v = ch.unicodeScalars.first?.value {
                let idx = Int(v - aValue)
                if idx >= 0 && idx < 26 {
                    counts[idx] += 1
                }
            }
        }
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        var maxVowel = 0
        var maxConsonant = 0
        for i in 0..<26 {
            let freq = counts[i]
            if freq == 0 { continue }
            let char = Character(UnicodeScalar(aValue + UInt32(i))!)
            if vowels.contains(char) {
                if freq > maxVowel { maxVowel = freq }
            } else {
                if freq > maxConsonant { maxConsonant = freq }
            }
        }
        return maxVowel + maxConsonant
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFreqSum(s: String): Int {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var maxVowel = 0
        var maxConsonant = 0
        for (i in 0 until 26) {
            val count = freq[i]
            val ch = ('a'.code + i).toChar()
            if (vowels.contains(ch)) {
                if (count > maxVowel) maxVowel = count
            } else {
                if (count > maxConsonant) maxConsonant = count
            }
        }
        return maxVowel + maxConsonant
    }
}
```

## Dart

```dart
class Solution {
  int maxFreqSum(String s) {
    const Set<String> vowels = {'a', 'e', 'i', 'o', 'u'};
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      if (idx >= 0 && idx < 26) cnt[idx]++;
    }
    int maxVowel = 0, maxConsonant = 0;
    for (int i = 0; i < 26; i++) {
      int c = cnt[i];
      String ch = String.fromCharCode(97 + i);
      if (vowels.contains(ch)) {
        if (c > maxVowel) maxVowel = c;
      } else {
        if (c > maxConsonant) maxConsonant = c;
      }
    }
    return maxVowel + maxConsonant;
  }
}
```

## Golang

```go
func maxFreqSum(s string) int {
    var freq [26]int
    for _, ch := range s {
        if ch >= 'a' && ch <= 'z' {
            freq[ch-'a']++
        }
    }
    vowel := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
    maxV, maxC := 0, 0
    for i := 0; i < 26; i++ {
        cnt := freq[i]
        c := byte('a' + i)
        if vowel[c] {
            if cnt > maxV {
                maxV = cnt
            }
        } else {
            if cnt > maxC {
                maxC = cnt
            }
        }
    }
    return maxV + maxC
}
```

## Ruby

```ruby
def max_freq_sum(s)
  vowels = "aeiou"
  vowel_counts = Hash.new(0)
  consonant_counts = Hash.new(0)

  s.each_char do |ch|
    if vowels.include?(ch)
      vowel_counts[ch] += 1
    else
      consonant_counts[ch] += 1
    end
  end

  max_vowel = vowel_counts.empty? ? 0 : vowel_counts.values.max
  max_consonant = consonant_counts.empty? ? 0 : consonant_counts.values.max

  max_vowel + max_consonant
end
```

## Scala

```scala
object Solution {
    def maxFreqSum(s: String): Int = {
        val vowels = Set('a', 'e', 'i', 'o', 'u')
        val counts = Array.fill(26)(0)
        for (ch <- s) {
            counts(ch - 'a') += 1
        }
        var maxVowel = 0
        var maxCons = 0
        for (i <- 0 until 26) {
            val c = ('a' + i).toChar
            if (vowels.contains(c)) {
                if (counts(i) > maxVowel) maxVowel = counts(i)
            } else {
                if (counts(i) > maxCons) maxCons = counts(i)
            }
        }
        maxVowel + maxCons
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        let mut cnt = [0usize; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        // vowel indices: a e i o u
        let vowel_idx = [0, 4, 8, 14, 20]; // positions of a,e,i,o,u
        let mut max_vowel = 0usize;
        for &i in &vowel_idx {
            if cnt[i] > max_vowel {
                max_vowel = cnt[i];
            }
        }
        let mut max_consonant = 0usize;
        for i in 0..26 {
            // skip vowels
            if vowel_idx.contains(&i) {
                continue;
            }
            if cnt[i] > max_consonant {
                max_consonant = cnt[i];
            }
        }
        (max_vowel + max_consonant) as i32
    }
}
```

## Racket

```racket
(define/contract (max-freq-sum s)
  (-> string? exact-integer?)
  (let* ((vowel-hash (make-hash))
         (cons-hash (make-hash)))
    (for ([i (in-range (string-length s))])
      (let ((ch (string-ref s i)))
        (if (member ch '(#\a #\e #\i #\o #\u))
            (hash-update! vowel-hash ch add1 0)
            (hash-update! cons-hash ch add1 0))))
    (define max-vowel
      (for/fold ([m 0]) ([(k v) (in-hash vowel-hash)]) (max m v)))
    (define max-cons
      (for/fold ([m 0]) ([(k v) (in-hash cons-hash)]) (max m v)))
    (+ max-vowel max-cons)))
```

## Erlang

```erlang
-module(solution).
-export([max_freq_sum/1]).

-spec max_freq_sum(S :: unicode:unicode_binary()) -> integer().
max_freq_sum(S) ->
    Map = count_chars(S, #{}),
    VowelCounts = [Cnt || {Ch, Cnt} <- maps:to_list(Map), is_vowel(Ch)],
    ConsonantCounts = [Cnt || {Ch, Cnt} <- maps:to_list(Map), not is_vowel(Ch)],
    MaxV = case VowelCounts of [] -> 0; _ -> lists:max(VowelCounts) end,
    MaxC = case ConsonantCounts of [] -> 0; _ -> lists:max(ConsonantCounts) end,
    MaxV + MaxC.

count_chars(<<>>, Acc) ->
    Acc;
count_chars(<<Char, Rest/binary>>, Acc) ->
    NewAcc = maps:update_with(Char, fun(N) -> N + 1 end, 1, Acc),
    count_chars(Rest, NewAcc).

is_vowel($a) -> true;
is_vowel($e) -> true;
is_vowel($i) -> true;
is_vowel($o) -> true;
is_vowel($u) -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_freq_sum(s :: String.t) :: integer
  def max_freq_sum(s) do
    freq = s |> String.graphemes() |> Enum.frequencies()
    vowel_set = MapSet.new(~w(a e i o u)a)

    {max_vowel, max_consonant} =
      Enum.reduce(freq, {0, 0}, fn {ch, cnt}, {mv, mc} ->
        if MapSet.member?(vowel_set, ch) do
          {if(cnt > mv, do: cnt, else: mv), mc}
        else
          {mv, if(cnt > mc, do: cnt, else: mc)}
        end
      end)

    max_vowel + max_consonant
  end
end
```
