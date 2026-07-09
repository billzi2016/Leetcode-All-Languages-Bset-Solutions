# 0804. Unique Morse Code Words

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        static const vector<string> morse = {
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        };
        unordered_set<string> seen;
        for (const string& w : words) {
            string code;
            code.reserve(w.size() * 4); // average length
            for (char c : w) {
                code += morse[c - 'a'];
            }
            seen.insert(move(code));
        }
        return static_cast<int>(seen.size());
    }
};
```

## Java

```java
class Solution {
    private static final String[] MORSE = {
        ".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.",
        "---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    };
    
    public int uniqueMorseRepresentations(String[] words) {
        java.util.HashSet<String> set = new java.util.HashSet<>();
        for (String word : words) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < word.length(); i++) {
                sb.append(MORSE[word.charAt(i) - 'a']);
            }
            set.add(sb.toString());
        }
        return set.size();
    }
}
```

## Python

```python
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        seen = set()
        for w in words:
            code = ''.join(morse[ord(c) - 97] for c in w)
            seen.add(code)
        return len(seen)
```

## Python3

```python
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.", "....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
                 "-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            transformation = ''.join(morse[ord(c) - ord('a')] for c in word)
            seen.add(transformation)
        return len(seen)
```

## C

```c
#include <string.h>
#include <stdbool.h>

int uniqueMorseRepresentations(char** words, int wordsSize) {
    const char *morse[26] = {
        ".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.",
        "---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    };
    
    char unique[100][50]; // max 100 words, each transformation <= 48 chars + '\0'
    int uniqueCount = 0;
    
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        char buf[50] = {0};
        char *p = buf;
        while (*w) {
            const char *code = morse[*w - 'a'];
            while (*code) {
                *p++ = *code++;
            }
            ++w;
        }
        *p = '\0';
        
        bool found = false;
        for (int j = 0; j < uniqueCount; ++j) {
            if (strcmp(unique[j], buf) == 0) {
                found = true;
                break;
            }
        }
        if (!found) {
            strcpy(unique[uniqueCount], buf);
            ++uniqueCount;
        }
    }
    
    return uniqueCount;
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly string[] Morse = new[]
    {
        ".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.",
        "---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    };

    public int UniqueMorseRepresentations(string[] words)
    {
        var set = new HashSet<string>();
        foreach (var word in words)
        {
            var sb = new System.Text.StringBuilder();
            foreach (char c in word)
            {
                sb.Append(Morse[c - 'a']);
            }
            set.Add(sb.ToString());
        }
        return set.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const morse = [".-","-...","-.-.","-..",".","..-.","--.", "....","..",".---","-.-",".-..",
                  "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
                  "-.--","--.."];
    const seen = new Set();
    for (const w of words) {
        let code = '';
        for (let i = 0; i < w.length; i++) {
            code += morse[w.charCodeAt(i) - 97];
        }
        seen.add(code);
    }
    return seen.size;
};
```

## Typescript

```typescript
function uniqueMorseRepresentations(words: string[]): number {
    const morse = [
        ".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.",
        "---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    ];
    const seen = new Set<string>();
    for (const word of words) {
        let code = "";
        for (let i = 0; i < word.length; i++) {
            code += morse[word.charCodeAt(i) - 97];
        }
        seen.add(code);
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function uniqueMorseRepresentations($words) {
        $morse = [".-","-...","-.-.","-..",".","..-.","--.", "....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        $unique = [];
        foreach ($words as $word) {
            $code = '';
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $idx = ord($word[$i]) - 97;
                $code .= $morse[$idx];
            }
            $unique[$code] = true;
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        let morse = [
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        ]
        var unique = Set<String>()
        for word in words {
            var code = ""
            for ch in word.unicodeScalars {
                let index = Int(ch.value - 97) // 'a' ascii is 97
                code += morse[index]
            }
            unique.insert(code)
        }
        return unique.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniqueMorseRepresentations(words: Array<String>): Int {
        val morse = arrayOf(
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        )
        val seen = HashSet<String>()
        for (word in words) {
            val sb = StringBuilder()
            for (ch in word) {
                sb.append(morse[ch - 'a'])
            }
            seen.add(sb.toString())
        }
        return seen.size
    }
}
```

## Dart

```dart
class Solution {
  int uniqueMorseRepresentations(List<String> words) {
    const List<String> morse = [
      ".-","-...","-.-.","-..",".","..-.","--.",
      "....","..",".---","-.-",".-..","--","-.",
      "---",".--.","--.-",".-.","...","-","..-",
      "...-",".--","-..-","-.--","--.."
    ];
    final Set<String> seen = {};
    for (final word in words) {
      final StringBuffer sb = StringBuffer();
      for (int i = 0; i < word.length; i++) {
        int idx = word.codeUnitAt(i) - 97; // 'a' ascii
        sb.write(morse[idx]);
      }
      seen.add(sb.toString());
    }
    return seen.length;
  }
}
```

## Golang

```go
func uniqueMorseRepresentations(words []string) int {
	morse := []string{
		".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
		"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
		"--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
		"-.--", "--..",
	}
	unique := make(map[string]struct{})
	for _, w := range words {
		var sb []byte
		for i := 0; i < len(w); i++ {
			sb = append(sb, morse[w[i]-'a']...)
		}
		unique[string(sb)] = struct{}{}
	}
	return len(unique)
}
```

## Ruby

```ruby
require 'set'

# @param {String[]} words
# @return {Integer}
def unique_morse_representations(words)
  morse = [".-","-...","-.-.","-..",".","..-.","--.", "....","..",".---",
           "-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
           "-","..-","...-",".--","-..-","-.--","--.."]
  seen = Set.new
  words.each do |word|
    code = word.each_char.map { |c| morse[c.ord - 97] }.join
    seen.add(code)
  end
  seen.size
end
```

## Scala

```scala
object Solution {
    def uniqueMorseRepresentations(words: Array[String]): Int = {
        val morse = Array(
            ".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.",
            "---",".--.","--.-",".-.","...","-","..-",
            "...-",".--","-..-","-.--","--.."
        )
        val seen = scala.collection.mutable.HashSet[String]()
        for (w <- words) {
            val sb = new StringBuilder
            for (c <- w) {
                sb.append(morse(c - 'a'))
            }
            seen += sb.toString()
        }
        seen.size
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        let morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--..",
        ];
        let mut set = HashSet::new();
        for w in words {
            let mut code = String::new();
            for b in w.bytes() {
                let idx = (b - b'a') as usize;
                code.push_str(morse[idx]);
            }
            set.insert(code);
        }
        set.len() as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/set)

(define MORSE
  (vector ".-" "-..." "-.-." "-.." "." "..-." "--." "...." ".."
          ".---" "-.-" ".-.." "--" "-." "---" ".--." "--.-" ".-."
          "..." "-" "..-" "...-" ".--" "-..-" "-.--" "--.."))

(define/contract (unique-morse-representations words)
  (-> (listof string?) exact-integer?)
  (let loop ((ws words) (s empty))
    (if (null? ws)
        (set-count s)
        (let* ([w (car ws)]
               [code (apply string-append
                            (for/list ([c (in-string w)])
                              (vector-ref MORSE (- (char->integer c)
                                                   (char->integer #\a)))) )])
          (loop (cdr ws) (set-add s code))))))
```

## Erlang

```erlang
-spec unique_morse_representations(Words :: [unicode:unicode_binary()]) -> integer().
unique_morse_representations(Words) ->
    Morse = [
        <<".-">>,   % a
        <<"-...">>, % b
        <<"-.-.">>, % c
        <<"-..">>,  % d
        <<".">>,    % e
        <<"..-.">>, % f
        <<"--.">>,  % g
        <<"....">>, % h
        <<"..">>,   % i
        <<".---">>, % j
        <<"-.-">>,  % k
        <<".-..">>, % l
        <<"--">>,   % m
        <<"-.">>,   % n
        <<"---">>,  % o
        <<".--.">>, % p
        <<"--.-">>, % q
        <<".-.">>,  % r
        <<"...">>,  % s
        <<"-">>,    % t
        <<"..-">>,  % u
        <<"...-">>, % v
        <<".--">>,  % w
        <<"-..-">>, % x
        <<"-.--">>, % y
        <<"--..">>  % z
    ],
    Transform = fun(Word) ->
        Chars = binary_to_list(Word),
        lists:foldl(
            fun(C, Acc) ->
                Index = C - $a,
                MorseCode = lists:nth(Index + 1, Morse),
                <<Acc/binary, MorseCode/binary>>
            end,
            <<>>,
            Chars
        )
    end,
    SetMap = lists:foldl(
        fun(W, Map) ->
            Trans = Transform(W),
            maps:put(Trans, true, Map)
        end,
        #{},
        Words
    ),
    maps:size(SetMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_morse_representations(words :: [String.t]) :: integer
  def unique_morse_representations(words) do
    morse = [
      ".-","-...","-.-.","-..",".","..-.","--.",
      "....","..",".---","-.-",".-..","--","-.",
      "---",".--.","--.-",".-.","...","-","..-",
      "...-",".--","-..-","-.--","--.."
    ]

    words
    |> Enum.reduce(MapSet.new(), fn word, set ->
      code =
        word
        |> String.to_charlist()
        |> Enum.map(fn c -> Enum.at(morse, c - ?a) end)
        |> Enum.join()

      MapSet.put(set, code)
    end)
    |> MapSet.size()
  end
end
```
