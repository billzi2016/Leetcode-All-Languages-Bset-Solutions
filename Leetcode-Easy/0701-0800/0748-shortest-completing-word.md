# 0748. Shortest Completing Word

## Cpp

```cpp
class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        int need[26] = {0};
        for (char ch : licensePlate) {
            if (isalpha(ch)) {
                need[tolower(ch) - 'a']++;
            }
        }
        string ans;
        int bestLen = INT_MAX;
        for (const string& w : words) {
            if ((int)w.size() >= bestLen) continue; // cannot be better
            int cnt[26] = {0};
            for (char ch : w) cnt[ch - 'a']++;
            bool ok = true;
            for (int i = 0; i < 26; ++i) {
                if (cnt[i] < need[i]) { ok = false; break; }
            }
            if (ok && (int)w.size() < bestLen) {
                bestLen = w.size();
                ans = w;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] need = new int[26];
        for (char ch : licensePlate.toCharArray()) {
            if (Character.isLetter(ch)) {
                need[Character.toLowerCase(ch) - 'a']++;
            }
        }

        String answer = null;
        for (String word : words) {
            if (answer != null && word.length() >= answer.length()) continue;

            int[] cnt = new int[26];
            for (char ch : word.toCharArray()) {
                cnt[ch - 'a']++;
            }

            boolean ok = true;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] < need[i]) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                answer = word;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter

        # Count required letters from licensePlate
        req = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        best_word = None
        best_len = float('inf')
        for w in words:
            if len(w) >= best_len:
                continue  # cannot be better than current best
            cnt = Counter(w)
            # check if all required letters are satisfied
            for c, needed in req.items():
                if cnt.get(c, 0) < needed:
                    break
            else:
                best_word = w
                best_len = len(w)

        return best_word
```

## Python3

```python
from typing import List
import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Count required letters from licensePlate
        req = collections.Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        best_word = None
        best_len = float('inf')
        for word in words:
            if len(word) >= best_len:
                continue
            wcnt = collections.Counter(word)
            # Check if word satisfies all required counts
            for c, cnt in req.items():
                if wcnt[c] < cnt:
                    break
            else:
                best_word = word
                best_len = len(word)
        return best_word
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

char* shortestCompletingWord(char* licensePlate, char** words, int wordsSize) {
    int need[26] = {0};
    for (char *p = licensePlate; *p; ++p) {
        if (isalpha(*p)) {
            need[tolower(*p) - 'a']++;
        }
    }

    char *result = NULL;
    int bestLen = INT_MAX;

    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int cnt[26] = {0};
        for (char *q = w; *q; ++q) {
            cnt[*q - 'a']++;
        }

        int ok = 1;
        for (int j = 0; j < 26; ++j) {
            if (need[j] > cnt[j]) {
                ok = 0;
                break;
            }
        }

        if (ok) {
            int len = strlen(w);
            if (len < bestLen) {
                bestLen = len;
                if (result) free(result);
                result = (char *)malloc(len + 1);
                strcpy(result, w);
            }
        }
    }

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public string ShortestCompletingWord(string licensePlate, string[] words) {
        int[] need = new int[26];
        foreach (char c in licensePlate) {
            if (char.IsLetter(c)) {
                need[char.ToLowerInvariant(c) - 'a']++;
            }
        }

        string answer = null;
        int bestLen = int.MaxValue;

        foreach (string word in words) {
            if (word.Length > bestLen) continue; // cannot be better
            int[] cnt = new int[26];
            foreach (char c in word) {
                cnt[c - 'a']++;
            }
            bool ok = true;
            for (int i = 0; i < 26; i++) {
                if (cnt[i] < need[i]) { ok = false; break; }
            }
            if (ok && word.Length < bestLen) {
                bestLen = word.Length;
                answer = word;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} licensePlate
 * @param {string[]} words
 * @return {string}
 */
var shortestCompletingWord = function(licensePlate, words) {
    const required = new Array(26).fill(0);
    for (const ch of licensePlate) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            const idx = ch.toLowerCase().charCodeAt(0) - 97;
            required[idx]++;
        }
    }

    let best = "";
    let minLen = Infinity;

    for (const w of words) {
        if (w.length > minLen) continue; // cannot beat current best
        const cnt = new Array(26).fill(0);
        for (const ch of w) {
            cnt[ch.charCodeAt(0) - 97]++;
        }
        let ok = true;
        for (let i = 0; i < 26; i++) {
            if (cnt[i] < required[i]) {
                ok = false;
                break;
            }
        }
        if (ok && w.length < minLen) {
            best = w;
            minLen = w.length;
        }
    }

    return best;
};
```

## Typescript

```typescript
function shortestCompletingWord(licensePlate: string, words: string[]): string {
    const need = new Array(26).fill(0);
    for (let i = 0; i < licensePlate.length; i++) {
        const code = licensePlate.charCodeAt(i);
        if (code >= 65 && code <= 90) { // 'A'-'Z'
            need[code - 65]++;
        } else if (code >= 97 && code <= 122) { // 'a'-'z'
            need[code - 97]++;
        }
    }

    let answer = "";
    let minLen = Infinity;

    for (const word of words) {
        if (word.length >= minLen) continue; // cannot be better
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (idx >= 0 && idx < 26) cnt[idx]++;
        }
        let ok = true;
        for (let i = 0; i < 26; i++) {
            if (cnt[i] < need[i]) { ok = false; break; }
        }
        if (ok) {
            answer = word;
            minLen = word.length;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param String $licensePlate
     * @param String[] $words
     * @return String
     */
    function shortestCompletingWord($licensePlate, $words) {
        // Count required letters from license plate
        $need = array_fill(0, 26, 0);
        $lenPlate = strlen($licensePlate);
        for ($i = 0; $i < $lenPlate; $i++) {
            $c = $licensePlate[$i];
            if (ctype_alpha($c)) {
                $idx = ord(strtolower($c)) - 97;
                $need[$idx]++;
            }
        }

        $result = "";
        $minLen = PHP_INT_MAX;

        foreach ($words as $word) {
            // Quick length check
            $lenWord = strlen($word);
            if ($lenWord >= $minLen) {
                // still need to verify because could be same length but earlier? problem wants first shortest,
                // and we only replace when strictly shorter, so skip equal lengths.
                continue;
            }

            // Count letters in the word
            $cnt = array_fill(0, 26, 0);
            for ($i = 0; $i < $lenWord; $i++) {
                $idx = ord($word[$i]) - 97;
                $cnt[$idx]++;
            }

            // Verify if word satisfies requirements
            $ok = true;
            for ($j = 0; $j < 26; $j++) {
                if ($cnt[$j] < $need[$j]) {
                    $ok = false;
                    break;
                }
            }

            if ($ok) {
                $minLen = $lenWord;
                $result = $word;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func shortestCompletingWord(_ licensePlate: String, _ words: [String]) -> String {
        var need = [Int](repeating: 0, count: 26)
        for ch in licensePlate.lowercased() {
            if let scalar = ch.unicodeScalars.first?.value,
               scalar >= 97 && scalar <= 122 {
                need[Int(scalar - 97)] += 1
            }
        }
        
        var answer = ""
        var minLen = Int.max
        
        for word in words {
            var cnt = [Int](repeating: 0, count: 26)
            for ch in word {
                let idx = Int(ch.unicodeScalars.first!.value - 97)
                cnt[idx] += 1
            }
            
            var ok = true
            for i in 0..<26 {
                if cnt[i] < need[i] {
                    ok = false
                    break
                }
            }
            
            if ok && word.count < minLen {
                minLen = word.count
                answer = word
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestCompletingWord(licensePlate: String, words: Array<String>): String {
        val need = IntArray(26)
        for (ch in licensePlate) {
            if (ch.isLetter()) {
                need[ch.lowercaseChar() - 'a']++
            }
        }

        var answer = ""
        var minLen = Int.MAX_VALUE

        wordLoop@ for (word in words) {
            if (word.length >= minLen) continue
            val have = IntArray(26)
            for (c in word) {
                have[c - 'a']++
            }
            for (i in 0 until 26) {
                if (have[i] < need[i]) continue@wordLoop
            }
            answer = word
            minLen = word.length
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  String shortestCompletingWord(String licensePlate, List<String> words) {
    // Count required letters from licensePlate
    List<int> need = List.filled(26, 0);
    for (int i = 0; i < licensePlate.length; i++) {
      var ch = licensePlate[i];
      if ((ch.codeUnitAt(0) >= 65 && ch.codeUnitAt(0) <= 90) ||
          (ch.codeUnitAt(0) >= 97 && ch.codeUnitAt(0) <= 122)) {
        int idx = ch.toLowerCase().codeUnitAt(0) - 'a'.codeUnitAt(0);
        need[idx]++;
      }
    }

    String answer = "";
    int bestLen = 1 << 30;

    for (String word in words) {
      // Quick length check
      if (word.length >= bestLen) continue;

      List<int> cnt = List.filled(26, 0);
      for (int i = 0; i < word.length; i++) {
        int idx = word.codeUnitAt(i) - 'a'.codeUnitAt(0);
        if (idx >= 0 && idx < 26) cnt[idx]++;
      }

      bool ok = true;
      for (int i = 0; i < 26; i++) {
        if (cnt[i] < need[i]) {
          ok = false;
          break;
        }
      }

      if (ok) {
        answer = word;
        bestLen = word.length;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func shortestCompletingWord(licensePlate string, words []string) string {
	need := [26]int{}
	for _, ch := range licensePlate {
		if ch >= 'a' && ch <= 'z' {
			need[ch-'a']++
		} else if ch >= 'A' && ch <= 'Z' {
			need[ch-'A']++
		}
	}

	best := ""
	minLen := int(^uint(0) >> 1) // max int

	for _, w := range words {
		if len(w) > minLen {
			continue
		}
		cnt := [26]int{}
		for i := 0; i < len(w); i++ {
			c := w[i] - 'a'
			if c <= 25 {
				cnt[c]++
			}
		}
		ok := true
		for i := 0; i < 26; i++ {
			if cnt[i] < need[i] {
				ok = false
				break
			}
		}
		if ok && len(w) < minLen {
			best = w
			minLen = len(w)
		}
	}
	return best
}
```

## Ruby

```ruby
def shortest_completing_word(license_plate, words)
  need = Array.new(26, 0)
  license_plate.each_char do |ch|
    if ch =~ /[a-zA-Z]/
      idx = ch.downcase.ord - 'a'.ord
      need[idx] += 1
    end
  end

  result = nil
  words.each do |word|
    next if result && word.length > result.length

    cnt = Array.new(26, 0)
    word.each_char { |c| cnt[c.ord - 'a'.ord] += 1 }

    ok = true
    26.times do |i|
      if need[i] > cnt[i]
        ok = false
        break
      end
    end

    if ok
      result = word if result.nil? || word.length < result.length
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def shortestCompletingWord(licensePlate: String, words: Array[String]): String = {
        val need = new Array[Int](26)
        for (ch <- licensePlate) {
            if (ch.isLetter) {
                need(ch.toLower - 'a') += 1
            }
        }

        var bestWord = ""
        var bestLen = Int.MaxValue

        for (word <- words) {
            val cnt = new Array[Int](26)
            for (c <- word) {
                cnt(c - 'a') += 1
            }
            var ok = true
            var i = 0
            while (i < 26 && ok) {
                if (cnt(i) < need(i)) ok = false
                i += 1
            }
            if (ok && word.length < bestLen) {
                bestWord = word
                bestLen = word.length
            }
        }

        bestWord
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_completing_word(license_plate: String, words: Vec<String>) -> String {
        let mut need = [0i32; 26];
        for ch in license_plate.chars() {
            if ch.is_ascii_alphabetic() {
                let idx = (ch.to_ascii_lowercase() as u8 - b'a') as usize;
                need[idx] += 1;
            }
        }

        let mut best_word = String::new();
        let mut best_len = usize::MAX;

        for w in words.iter() {
            if w.len() > best_len {
                continue;
            }
            let mut cnt = [0i32; 26];
            for ch in w.chars() {
                let idx = (ch as u8 - b'a') as usize;
                cnt[idx] += 1;
            }
            let mut ok = true;
            for i in 0..26 {
                if need[i] > cnt[i] {
                    ok = false;
                    break;
                }
            }
            if ok && w.len() < best_len {
                best_word = w.clone();
                best_len = w.len();
            }
        }

        best_word
    }
}
```

## Racket

```racket
(define/contract (shortest-completing-word licensePlate words)
  (-> string? (listof string?) string?)
  (let ([plate-freq
         (let ([v (make-vector 26 0)])
           (for ([i (in-range (string-length licensePlate))])
             (let* ([ch (string-ref licensePlate i)]
                    [lower (char-downcase ch)])
               (when (char-alphabetic? lower)
                 (define idx (- (char->integer lower) (char->integer #\a)))
                 (vector-set! v idx (+ 1 (vector-ref v idx))))))
           v)])
    (define (covers? w)
      (let ([v (make-vector 26 0)])
        (for ([i (in-range (string-length w))])
          (let* ([ch (string-ref w i)]
                 [lower (char-downcase ch)]) ; words are lowercase already
            (when (char-alphabetic? lower)
              (define idx (- (char->integer lower) (char->integer #\a)))
              (vector-set! v idx (+ 1 (vector-ref v idx))))))
        (for/and ([i (in-range 26)])
          (>= (vector-ref v i) (vector-ref plate-freq i)))))
    (let ([best-word #f])
      (for ([w words])
        (when (covers? w)
          (if (or (not best-word) (< (string-length w) (string-length best-word)))
              (set! best-word w))))
      best-word)))
```

## Erlang

```erlang
-spec shortest_completing_word(LicensePlate :: unicode:unicode_binary(),
                                 Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
shortest_completing_word(LicensePlate, Words) ->
    ReqMap = build_req(LicensePlate),
    Best = find_best(Words, ReqMap, undefined),
    Best.

%% Build a map of required letter counts from a binary string
build_req(Bin) ->
    build_req(binary_to_list(Bin), #{}).

build_req([], Map) -> Map;
build_req([C|Rest], Map) ->
    case is_letter(C) of
        true ->
            Lc = to_lower(C),
            NewMap = maps:update_with(Lc, fun(N) -> N + 1 end, 1, Map),
            build_req(Rest, NewMap);
        false ->
            build_req(Rest, Map)
    end.

is_letter(C) when $a =< C, C =< $z -> true;
is_letter(C) when $A =< C, C =< $Z -> true;
is_letter(_) -> false.

to_lower(C) when $A =< C, C =< $Z -> C + 32;
to_lower(C) -> C.

%% Find the shortest completing word
find_best([], _ReqMap, Best) ->
    Best;
find_best([Word|Rest], ReqMap, undefined) ->
    case satisfies(Word, ReqMap) of
        true -> find_best(Rest, ReqMap, Word);
        false -> find_best(Rest, ReqMap, undefined)
    end;
find_best([Word|Rest], ReqMap, Best) ->
    case satisfies(Word, ReqMap) of
        true ->
            LenW = byte_size(Word),
            LenBest = byte_size(Best),
            if LenW < LenBest ->
                    find_best(Rest, ReqMap, Word);
               true ->
                    find_best(Rest, ReqMap, Best)
            end;
        false ->
            find_best(Rest, ReqMap, Best)
    end.

%% Check if a word satisfies the required letter counts
satisfies(Word, ReqMap) ->
    WordMap = build_req(Word),
    lists:all(
      fun(Key) ->
          Need = maps:get(Key, ReqMap),
          Have = maps:get(Key, WordMap, 0),
          Have >= Need
      end,
      maps:keys(ReqMap)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_completing_word(String.t(), [String.t()]) :: String.t()
  def shortest_completing_word(license_plate, words) do
    needed =
      license_plate
      |> String.downcase()
      |> String.to_charlist()
      |> Enum.filter(&(&1 >= ?a and &1 <= ?z))
      |> Enum.frequencies()

    Enum.reduce(words, nil, fn word, best ->
      if completes?(word, needed) do
        cond do
          best == nil -> word
          String.length(word) < String.length(best) -> word
          true -> best
        end
      else
        best
      end
    end)
  end

  defp completes?(word, needed) do
    freq =
      word
      |> String.to_charlist()
      |> Enum.frequencies()

    Enum.all?(needed, fn {c, cnt} ->
      Map.get(freq, c, 0) >= cnt
    end)
  end
end
```
