# 1813. Sentence Similarity III

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        auto split = [](const string& s) {
            vector<string> v;
            istringstream iss(s);
            string w;
            while (iss >> w) v.push_back(w);
            return v;
        };
        
        vector<string> a = split(sentence1);
        vector<string> b = split(sentence2);
        if (a.size() > b.size()) swap(a, b); // ensure a is not longer
        
        int n = a.size(), m = b.size();
        int i = 0;
        while (i < n && a[i] == b[i]) ++i;
        
        int pa = n - 1, pb = m - 1;
        while (pa >= i && pb >= i && a[pa] == b[pb]) {
            --pa;
            --pb;
        }
        return pa < i;
    }
};
```

## Java

```java
class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] w1 = sentence1.split(" ");
        String[] w2 = sentence2.split(" ");
        if (w1.length > w2.length) {
            return areSentencesSimilar(sentence2, sentence1);
        }
        int i = 0;
        while (i < w1.length && i < w2.length && w1[i].equals(w2[i])) {
            i++;
        }
        int j1 = w1.length - 1;
        int j2 = w2.length - 1;
        while (j1 >= i && j2 >= i && w1[j1].equals(w2[j2])) {
            j1--;
            j2--;
        }
        return j1 < i;
    }
}
```

## Python

```python
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        words1 = sentence1.split()
        words2 = sentence2.split()
        # Ensure words1 is the shorter (or equal) list
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        i = 0
        n1, n2 = len(words1), len(words2)
        while i < n1 and words1[i] == words2[i]:
            i += 1

        j1 = n1 - 1
        j2 = n2 - 1
        while j1 >= i and j2 >= i and words1[j1] == words2[j2]:
            j1 -= 1
            j2 -= 1

        return j1 < i
```

## Python3

```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()
        # Ensure w1 is the shorter (or equal)
        if len(w1) > len(w2):
            w1, w2 = w2, w1
        i = 0
        n1, n2 = len(w1), len(w2)
        while i < n1 and w1[i] == w2[i]:
            i += 1
        j1, j2 = n1 - 1, n2 - 1
        while j1 >= i and w1[j1] == w2[j2]:
            j1 -= 1
            j2 -= 1
        return j1 < i
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static char* dupstr(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

bool areSentencesSimilar(char* sentence1, char* sentence2) {
    // Duplicate strings because strtok modifies them
    char *s1 = dupstr(sentence1);
    char *s2 = dupstr(sentence2);
    if (!s1 || !s2) {
        free(s1);
        free(s2);
        return false;
    }

    // Maximum possible words is length/2+1, allocate enough space
    const int MAX_WORDS = 200; // safe upper bound for given constraints
    char *w1[MAX_WORDS];
    char *w2[MAX_WORDS];
    int n1 = 0, n2 = 0;

    // Split sentence1 into words
    char *token = strtok(s1, " ");
    while (token) {
        w1[n1++] = token;
        token = strtok(NULL, " ");
    }

    // Split sentence2 into words
    token = strtok(s2, " ");
    while (token) {
        w2[n2++] = token;
        token = strtok(NULL, " ");
    }

    // Ensure w1 is the shorter (or equal) array
    if (n1 > n2) {
        // swap pointers and lengths
        char **tmpW = w1; int tmpN = n1;
        w1[0] = NULL; // dummy to avoid compiler warning about unused variable
        // Actually we need to swap the content arrays, easier: use separate variables
    }

    // To simplify swapping without moving actual arrays, use pointers to arrays
    char **shortWords = w1;
    int shortLen = n1;
    char **longWords = w2;
    int longLen = n2;

    if (n1 > n2) {
        shortWords = w2;
        shortLen = n2;
        longWords = w1;
        longLen = n1;
    }

    // Compare prefix
    int left = 0;
    while (left < shortLen && strcmp(shortWords[left], longWords[left]) == 0) {
        left++;
    }

    // Compare suffix
    int i = shortLen - 1;
    int j = longLen - 1;
    while (i >= left && j >= left && strcmp(shortWords[i], longWords[j]) == 0) {
        i--;
        j--;
    }

    bool result = (i < left);

    free(s1);
    free(s2);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool AreSentencesSimilar(string sentence1, string sentence2)
    {
        var words1 = sentence1.Split(' ');
        var words2 = sentence2.Split(' ');

        // Ensure words1 is the shorter (or equal) array
        if (words1.Length > words2.Length)
        {
            var temp = words1;
            words1 = words2;
            words2 = temp;
        }

        int i = 0;
        while (i < words1.Length && words1[i] == words2[i])
        {
            i++;
        }

        int j1 = words1.Length - 1;
        int j2 = words2.Length - 1;
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2])
        {
            j1--;
            j2--;
        }

        return j1 < i;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    const words1 = sentence1.split(' ');
    const words2 = sentence2.split(' ');
    
    // Ensure words1 is the shorter (or equal) array
    if (words1.length > words2.length) return areSentencesSimilar(sentence2, sentence1);
    
    let i = 0;
    while (i < words1.length && i < words2.length && words1[i] === words2[i]) {
        i++;
    }
    
    let j1 = words1.length - 1;
    let j2 = words2.length - 1;
    while (j1 >= i && j2 >= i && words1[j1] === words2[j2]) {
        j1--;
        j2--;
    }
    
    return j1 < i;
};
```

## Typescript

```typescript
function areSentencesSimilar(sentence1: string, sentence2: string): boolean {
    const words1 = sentence1.split(' ');
    const words2 = sentence2.split(' ');
    if (words1.length > words2.length) return areSentencesSimilar(sentence2, sentence1);
    let i = 0;
    while (i < words1.length && i < words2.length && words1[i] === words2[i]) i++;
    let j1 = words1.length - 1;
    let j2 = words2.length - 1;
    while (j1 >= i && j2 >= i && words1[j1] === words2[j2]) {
        j1--;
        j2--;
    }
    return j1 < i;
}
```

## Php

```php
class Solution {
    /**
     * @param String $sentence1
     * @param String $sentence2
     * @return Boolean
     */
    function areSentencesSimilar($sentence1, $sentence2) {
        $words1 = explode(' ', $sentence1);
        $words2 = explode(' ', $sentence2);
        if (count($words1) > count($words2)) {
            $tmp = $words1;
            $words1 = $words2;
            $words2 = $tmp;
        }
        $n1 = count($words1);
        $n2 = count($words2);
        $i = 0;
        while ($i < $n1 && $words1[$i] === $words2[$i]) {
            $i++;
        }
        $j1 = $n1 - 1;
        $j2 = $n2 - 1;
        while ($j1 >= $i && $j2 >= $i && $words1[$j1] === $words2[$j2]) {
            $j1--;
            $j2--;
        }
        return $j1 < $i;
    }
}
```

## Swift

```swift
class Solution {
    func areSentencesSimilar(_ sentence1: String, _ sentence2: String) -> Bool {
        let words1 = sentence1.split(separator: " ").map(String.init)
        let words2 = sentence2.split(separator: " ").map(String.init)
        
        // Ensure words1 is the shorter (or equal) array
        if words1.count > words2.count {
            return areSentencesSimilar(sentence2, sentence1)
        }
        
        var i = 0
        while i < words1.count && words1[i] == words2[i] {
            i += 1
        }
        
        var j1 = words1.count - 1
        var j2 = words2.count - 1
        while j1 >= i && words1[j1] == words2[j2] {
            j1 -= 1
            j2 -= 1
        }
        
        return j1 < i
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areSentencesSimilar(sentence1: String, sentence2: String): Boolean {
        var words1 = sentence1.split(' ')
        var words2 = sentence2.split(' ')
        // Ensure words1 is the shorter (or equal) array
        if (words1.size > words2.size) {
            val temp = words1
            words1 = words2
            words2 = temp
        }
        var i = 0
        while (i < words1.size && i < words2.size && words1[i] == words2[i]) {
            i++
        }
        var j1 = words1.lastIndex
        var j2 = words2.lastIndex
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2]) {
            j1--
            j2--
        }
        return j1 < i
    }
}
```

## Dart

```dart
class Solution {
  bool areSentencesSimilar(String sentence1, String sentence2) {
    List<String> w1 = sentence1.split(' ');
    List<String> w2 = sentence2.split(' ');
    if (w1.length > w2.length) {
      var tmp = w1;
      w1 = w2;
      w2 = tmp;
    }
    int i = 0;
    while (i < w1.length && i < w2.length && w1[i] == w2[i]) {
      i++;
    }
    int j1 = w1.length - 1;
    int j2 = w2.length - 1;
    while (j1 >= i && j2 >= i && w1[j1] == w2[j2]) {
      j1--;
      j2--;
    }
    return j1 < i;
  }
}
```

## Golang

```go
package main

import "strings"

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	words1 := strings.Split(sentence1, " ")
	words2 := strings.Split(sentence2, " ")

	if len(words1) > len(words2) {
		return areSentencesSimilar(sentence2, sentence1)
	}

	i := 0
	for i < len(words1) && i < len(words2) && words1[i] == words2[i] {
		i++
	}
	j1 := len(words1) - 1
	j2 := len(words2) - 1
	for j1 >= i && j2 >= i && words1[j1] == words2[j2] {
		j1--
		j2--
	}
	return j1 < i
}
```

## Ruby

```ruby
def are_sentences_similar(sentence1, sentence2)
  w1 = sentence1.split(' ')
  w2 = sentence2.split(' ')
  if w1.length > w2.length
    w1, w2 = w2, w1
  end

  i = 0
  while i < w1.length && i < w2.length && w1[i] == w2[i]
    i += 1
  end

  j1 = w1.length - 1
  j2 = w2.length - 1
  while j1 >= i && j2 >= i && w1[j1] == w2[j2]
    j1 -= 1
    j2 -= 1
  end

  j1 < i
end
```

## Scala

```scala
object Solution {
    def areSentencesSimilar(sentence1: String, sentence2: String): Boolean = {
        val w1 = sentence1.split(" ")
        val w2 = sentence2.split(" ")
        if (w1.length > w2.length) return areSentencesSimilar(sentence2, sentence1)

        var i = 0
        while (i < w1.length && w1(i) == w2(i)) {
            i += 1
        }

        var j = w1.length - 1
        var k = w2.length - 1
        while (j >= i && w1(j) == w2(k)) {
            j -= 1
            k -= 1
        }

        i > j
    }
}
```

## Rust

```rust
impl Solution {
    pub fn are_sentences_similar(sentence1: String, sentence2: String) -> bool {
        let w1: Vec<&str> = sentence1.split_whitespace().collect();
        let w2: Vec<&str> = sentence2.split_whitespace().collect();

        // Ensure `short` is the smaller (or equal) list of words
        let (short, long) = if w1.len() <= w2.len() { (&w1, &w2) } else { (&w2, &w1) };

        // Match common prefix
        let mut i = 0;
        while i < short.len()
            && i < long.len()
            && short[i] == long[i]
        {
            i += 1;
        }

        // Match common suffix
        let mut s_idx = short.len();
        let mut l_idx = long.len();
        while s_idx > i
            && l_idx > i
            && short[s_idx - 1] == long[l_idx - 1]
        {
            s_idx -= 1;
            l_idx -= 1;
        }

        // If all words of the shorter sentence are matched, they are similar
        s_idx == i
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (are-sentences-similar sentence1 sentence2)
  (-> string? string? boolean?)
  (let loop ((s1 sentence1) (s2 sentence2))
    (let* ([w1 (string-split s1)]
           [w2 (string-split s2)]
           [len1 (length w1)]
           [len2 (length w2)])
      (if (> len1 len2)
          (loop s2 s1) ; ensure w1 is the shorter or equal list
          (let prefix ((i 0))
            (if (and (< i len1)
                     (< i len2)
                     (string=? (list-ref w1 i) (list-ref w2 i)))
                (prefix (+ i 1))
                (let suffix ((i-end (- len1 1))
                             (j-end (- len2 1))
                             (start i))
                  (if (and (>= i-end start)
                           (>= j-end start)
                           (string=? (list-ref w1 i-end) (list-ref w2 j-end)))
                      (suffix (- i-end 1) (- j-end 1) start)
                      (= start len1)))))))))
```

## Erlang

```erlang
-spec are_sentences_similar(Sentence1 :: unicode:unicode_binary(), Sentence2 :: unicode:unicode_binary()) -> boolean().
are_sentences_similar(Sentence1, Sentence2) ->
    Words1 = binary:split(Sentence1, <<" ">>, [global]),
    Words2 = binary:split(Sentence2, <<" ">>, [global]),
    case length(Words1) > length(Words2) of
        true -> are_sentences_similar(Sentence2, Sentence1);
        false ->
            {Rest1, Rest2} = drop_common_prefix(Words1, Words2),
            Rev1 = lists:reverse(Rest1),
            Rev2 = lists:reverse(Rest2),
            {Final1, Final2} = drop_common_prefix(Rev1, Rev2),
            (Final1 == [] orelse Final2 == [])
    end.

drop_common_prefix([H|T1], [H|T2]) ->
    drop_common_prefix(T1, T2);
drop_common_prefix(L1, L2) ->
    {L1, L2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec are_sentences_similar(sentence1 :: String.t(), sentence2 :: String.t()) :: boolean()
  def are_sentences_similar(sentence1, sentence2) do
    w1 = String.split(sentence1, " ")
    w2 = String.split(sentence2, " ")

    {short, long} =
      if length(w1) <= length(w2), do: {w1, w2}, else: {w2, w1}

    len_s = length(short)

    start = prefix_match(short, long, 0)

    if start == len_s do
      true
    else
      i = len_s - 1
      j = length(long) - 1
      remaining_i = suffix_match(short, long, i, j, start)
      remaining_i < start
    end
  end

  defp prefix_match(short, long, idx) do
    if idx < length(short) && Enum.at(short, idx) == Enum.at(long, idx) do
      prefix_match(short, long, idx + 1)
    else
      idx
    end
  end

  defp suffix_match(_short, _long, i, _j, start_idx) when i < start_idx, do: i

  defp suffix_match(short, long, i, j, start_idx) do
    if Enum.at(short, i) == Enum.at(long, j) do
      suffix_match(short, long, i - 1, j - 1, start_idx)
    else
      i
    end
  end
end
```
