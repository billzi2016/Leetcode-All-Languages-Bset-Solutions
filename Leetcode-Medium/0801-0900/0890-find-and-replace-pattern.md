# 0890. Find and Replace Pattern

## Cpp

```cpp
class Solution {
public:
    bool matches(const string& w, const string& p) {
        int mapP[26];
        int mapW[26];
        fill(begin(mapP), end(mapP), -1);
        fill(begin(mapW), end(mapW), -1);
        for (int i = 0; i < (int)p.size(); ++i) {
            int pi = p[i] - 'a';
            int wi = w[i] - 'a';
            if (mapP[pi] == -1 && mapW[wi] == -1) {
                mapP[pi] = wi;
                mapW[wi] = pi;
            } else {
                if (mapP[pi] != wi || mapW[wi] != pi)
                    return false;
            }
        }
        return true;
    }

    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> ans;
        for (const auto& w : words) {
            if (matches(w, pattern))
                ans.push_back(w);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (matches(word, pattern)) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean matches(String word, String pattern) {
        int[] mapPtoW = new int[26];
        int[] mapWtoP = new int[26];
        Arrays.fill(mapPtoW, -1);
        Arrays.fill(mapWtoP, -1);

        for (int i = 0; i < pattern.length(); i++) {
            int pIdx = pattern.charAt(i) - 'a';
            int wIdx = word.charAt(i) - 'a';

            if (mapPtoW[pIdx] == -1 && mapWtoP[wIdx] == -1) {
                mapPtoW[pIdx] = wIdx;
                mapWtoP[wIdx] = pIdx;
            } else {
                if (mapPtoW[pIdx] != wIdx || mapWtoP[wIdx] != pIdx) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def matches(word):
            p2w = {}
            w2p = {}
            for pc, wc in zip(pattern, word):
                if pc not in p2w:
                    p2w[pc] = wc
                elif p2w[pc] != wc:
                    return False
                if wc not in w2p:
                    w2p[wc] = pc
                elif w2p[wc] != pc:
                    return False
            return True

        return [w for w in words if matches(w])
```

## Python3

```python
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(s: str):
            m = {}
            res = []
            nxt = 0
            for ch in s:
                if ch not in m:
                    m[ch] = nxt
                    nxt += 1
                res.append(m[ch])
            return tuple(res)

        pat_enc = encode(pattern)
        return [w for w in words if encode(w) == pat_enc]
```

## C

```c
#include <stdlib.h>
#include <string.h>

char** findAndReplacePattern(char** words, int wordsSize, char* pattern, int* returnSize) {
    char **result = (char **)malloc(wordsSize * sizeof(char *));
    int count = 0;
    int patLen = strlen(pattern);
    
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int mapP[26], mapW[26];
        for (int k = 0; k < 26; ++k) {
            mapP[k] = -1;
            mapW[k] = -1;
        }
        int ok = 1;
        for (int j = 0; j < patLen; ++j) {
            int pIdx = pattern[j] - 'a';
            int wIdx = w[j] - 'a';
            if (mapP[pIdx] == -1 && mapW[wIdx] == -1) {
                mapP[pIdx] = wIdx;
                mapW[wIdx] = pIdx;
            } else {
                if (mapP[pIdx] != wIdx || mapW[wIdx] != pIdx) {
                    ok = 0;
                    break;
                }
            }
        }
        if (ok) {
            result[count++] = w;
        }
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> FindAndReplacePattern(string[] words, string pattern)
    {
        var result = new List<string>();
        foreach (var word in words)
        {
            if (IsMatch(word, pattern))
                result.Add(word);
        }
        return result;
    }

    private bool IsMatch(string word, string pattern)
    {
        int n = pattern.Length;
        int[] mapPtoW = new int[26];
        int[] mapWtoP = new int[26];
        for (int i = 0; i < 26; i++)
        {
            mapPtoW[i] = -1;
            mapWtoP[i] = -1;
        }

        for (int i = 0; i < n; i++)
        {
            int pIdx = pattern[i] - 'a';
            int wIdx = word[i] - 'a';

            if (mapPtoW[pIdx] == -1 && mapWtoP[wIdx] == -1)
            {
                mapPtoW[pIdx] = wIdx;
                mapWtoP[wIdx] = pIdx;
            }
            else
            {
                if (mapPtoW[pIdx] != wIdx || mapWtoP[wIdx] != pIdx)
                    return false;
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} pattern
 * @return {string[]}
 */
var findAndReplacePattern = function(words, pattern) {
    const matches = (word) => {
        const p2w = {};
        const w2p = {};
        for (let i = 0; i < pattern.length; i++) {
            const pChar = pattern[i];
            const wChar = word[i];
            if (p2w[pChar] === undefined && w2p[wChar] === undefined) {
                p2w[pChar] = wChar;
                w2p[wChar] = pChar;
            } else {
                if (p2w[pChar] !== wChar || w2p[wChar] !== pChar) {
                    return false;
                }
            }
        }
        return true;
    };
    
    const result = [];
    for (const w of words) {
        if (matches(w)) result.push(w);
    }
    return result;
};
```

## Typescript

```typescript
function findAndReplacePattern(words: string[], pattern: string): string[] {
    const matches: string[] = [];
    
    const isMatch = (word: string, pat: string): boolean => {
        const map = new Map<string, string>();
        const rev = new Map<string, string>();
        for (let i = 0; i < pat.length; i++) {
            const pChar = pat[i];
            const wChar = word[i];
            
            if (map.has(pChar)) {
                if (map.get(pChar) !== wChar) return false;
            } else {
                map.set(pChar, wChar);
            }
            
            if (rev.has(wChar)) {
                if (rev.get(wChar) !== pChar) return false;
            } else {
                rev.set(wChar, pChar);
            }
        }
        return true;
    };
    
    for (const w of words) {
        if (isMatch(w, pattern)) matches.push(w);
    }
    
    return matches;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $pattern
     * @return String[]
     */
    function findAndReplacePattern($words, $pattern) {
        $res = [];
        foreach ($words as $word) {
            if ($this->matches($word, $pattern)) {
                $res[] = $word;
            }
        }
        return $res;
    }

    private function matches(string $word, string $pattern): bool {
        $len = strlen($pattern);
        $p2w = [];
        $w2p = [];

        for ($i = 0; $i < $len; $i++) {
            $pc = $pattern[$i];
            $wc = $word[$i];

            if (isset($p2w[$pc])) {
                if ($p2w[$pc] !== $wc) {
                    return false;
                }
            } else {
                $p2w[$pc] = $wc;
            }

            if (isset($w2p[$wc])) {
                if ($w2p[$wc] !== $pc) {
                    return false;
                }
            } else {
                $w2p[$wc] = $pc;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func findAndReplacePattern(_ words: [String], _ pattern: String) -> [String] {
        var result = [String]()
        for word in words {
            if matches(word, pattern) {
                result.append(word)
            }
        }
        return result
    }
    
    private func matches(_ word: String, _ pattern: String) -> Bool {
        let wChars = Array(word)
        let pChars = Array(pattern)
        var forwardMap = [Character: Character]()
        var usedChars = Set<Character>()
        
        for i in 0..<pChars.count {
            let pChar = pChars[i]
            let wChar = wChars[i]
            
            if let mapped = forwardMap[pChar] {
                if mapped != wChar { return false }
            } else {
                if usedChars.contains(wChar) { return false }
                forwardMap[pChar] = wChar
                usedChars.insert(wChar)
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAndReplacePattern(words: Array<String>, pattern: String): List<String> {
        val result = mutableListOf<String>()
        for (word in words) {
            if (matches(word, pattern)) {
                result.add(word)
            }
        }
        return result
    }

    private fun matches(word: String, pattern: String): Boolean {
        val map = IntArray(26) { -1 }   // word char -> pattern char
        val rev = IntArray(26) { -1 }   // pattern char -> word char
        for (i in word.indices) {
            val w = word[i] - 'a'
            val p = pattern[i] - 'a'
            if (map[w] == -1 && rev[p] == -1) {
                map[w] = p
                rev[p] = w
            } else if (map[w] != p || rev[p] != w) {
                return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  List<String> findAndReplacePattern(List<String> words, String pattern) {
    List<String> result = [];
    for (var word in words) {
      if (_matches(word, pattern)) {
        result.add(word);
      }
    }
    return result;
  }

  bool _matches(String word, String pattern) {
    int n = word.length;
    List<int> p2w = List.filled(26, -1);
    List<int> w2p = List.filled(26, -1);
    for (int i = 0; i < n; i++) {
      int pIdx = pattern.codeUnitAt(i) - 97;
      int wIdx = word.codeUnitAt(i) - 97;
      if (p2w[pIdx] == -1 && w2p[wIdx] == -1) {
        p2w[pIdx] = wIdx;
        w2p[wIdx] = pIdx;
      } else if (p2w[pIdx] != wIdx || w2p[wIdx] != pIdx) {
        return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func findAndReplacePattern(words []string, pattern string) []string {
	matches := func(word string) bool {
		if len(word) != len(pattern) {
			return false
		}
		toWord := make(map[byte]byte)
		toPat := make(map[byte]byte)
		for i := 0; i < len(pattern); i++ {
			p := pattern[i]
			w := word[i]

			if v, ok := toWord[p]; ok {
				if v != w {
					return false
				}
			} else {
				toWord[p] = w
			}

			if v, ok := toPat[w]; ok {
				if v != p {
					return false
				}
			} else {
				toPat[w] = p
			}
		}
		return true
	}

	var res []string
	for _, w := range words {
		if matches(w) {
			res = append(res, w)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_and_replace_pattern(words, pattern)
  words.select do |w|
    map_p_to_w = {}
    map_w_to_p = {}
    match = true
    w.each_char.with_index do |c, i|
      pch = pattern[i]
      if !map_p_to_w.key?(pch) && !map_w_to_p.key?(c)
        map_p_to_w[pch] = c
        map_w_to_p[c] = pch
      elsif map_p_to_w[pch] != c || map_w_to_p[c] != pch
        match = false
        break
      end
    end
    match
  end
end
```

## Scala

```scala
object Solution {
    def findAndReplacePattern(words: Array[String], pattern: String): List[String] = {
        def matches(word: String, pat: String): Boolean = {
            val mapPW = Array.fill(26)(-1)
            val mapWP = Array.fill(26)(-1)
            var i = 0
            while (i < word.length) {
                val w = word.charAt(i) - 'a'
                val p = pat.charAt(i) - 'a'
                if (mapPW(p) == -1 && mapWP(w) == -1) {
                    mapPW(p) = w
                    mapWP(w) = p
                } else if (mapPW(p) != w || mapWP(w) != p) {
                    return false
                }
                i += 1
            }
            true
        }

        words.filter(word => matches(word, pattern)).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        fn matches(word: &str, pat: &str) -> bool {
            let mut w_to_p = [None; 26];
            let mut p_to_w = [None; 26];
            for (wc, pc) in word.chars().zip(pat.chars()) {
                let wi = (wc as u8 - b'a') as usize;
                let pi = (pc as u8 - b'a') as usize;
                match (w_to_p[wi], p_to_w[pi]) {
                    (None, None) => {
                        w_to_p[wi] = Some(pc);
                        p_to_w[pi] = Some(wc);
                    }
                    (Some(c1), Some(c2)) if c1 == pc && c2 == wc => {}
                    _ => return false,
                }
            }
            true
        }

        let mut result = Vec::new();
        for w in words.iter() {
            if matches(w, &pattern) {
                result.push(w.clone());
            }
        }
        result
    }
}
```

## Racket

```racket
(define (matches? word pat)
  (let ([len (string-length pat)])
    (if (= len (string-length word))
        (let ([p2w (make-hash)] [w2p (make-hash)])
          (let loop ((i 0) (ok #t))
            (cond [(not ok) #f]
                  [(= i len) #t]
                  [else
                   (define pch (string-ref pat i))
                   (define wch (string-ref word i))
                   (define existing-p2w (hash-ref p2w pch #f))
                   (define existing-w2p (hash-ref w2p wch #f))
                   (cond [(and existing-p2w (not (char=? existing-p2w wch))) (loop (add1 i) #f)]
                         [(and existing-w2p (not (char=? existing-w2p pch))) (loop (add1 i) #f)]
                         [else
                          (unless existing-p2w (hash-set! p2w pch wch))
                          (unless existing-w2p (hash-set! w2p wch pch))
                          (loop (add1 i) #t)]))]))
        #f)))

(define/contract (find-and-replace-pattern words pattern)
  (-> (listof string?) string? (listof string?))
  (filter (lambda (w) (matches? w pattern)) words))
```

## Erlang

```erlang
-module(solution).
-export([find_and_replace_pattern/2]).

-spec find_and_replace_pattern(Words :: [unicode:unicode_binary()], Pattern :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
find_and_replace_pattern(Words, Pattern) ->
    PatEnc = encode(unicode:characters_to_list(Pattern)),
    [Word || Word <- Words,
            encode(unicode:characters_to_list(Word)) == PatEnc].

encode(Chars) ->
    encode(Chars, #{}, 0, []).

encode([], _Map, _NextId, Acc) ->
    lists:reverse(Acc);
encode([C|Rest], Map, NextId, Acc) ->
    case maps:get(C, Map, undefined) of
        undefined ->
            NewMap = maps:put(C, NextId, Map),
            encode(Rest, NewMap, NextId + 1, [NextId | Acc]);
        Id ->
            encode(Rest, Map, NextId, [Id | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_and_replace_pattern(words :: [String.t()], pattern :: String.t()) :: [String.t()]
  def find_and_replace_pattern(words, pattern) do
    Enum.filter(words, fn word -> match?(word, pattern) end)
  end

  defp match?(word, pattern) do
    chars_w = String.graphemes(word)
    chars_p = String.graphemes(pattern)

    result =
      Enum.reduce_while(Enum.zip(chars_p, chars_w), {%{}, %{}}, fn {pc, wc}, {map_p2w, map_w2p} ->
        case {Map.get(map_p2w, pc), Map.get(map_w2p, wc)} do
          {nil, nil} ->
            {:cont, {Map.put(map_p2w, pc, wc), Map.put(map_w2p, wc, pc)}}

          {mapped_wc, mapped_pc} when mapped_wc == wc and mapped_pc == pc ->
            {:cont, {map_p2w, map_w2p}}

          _ ->
            {:halt, :mismatch}
        end
      end)

    result != :mismatch
  end
end
```
