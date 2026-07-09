# 2451. Odd String Difference

## Cpp

```cpp
class Solution {
public:
    string oddString(vector<string>& words) {
        auto diff = [&](const string& w) {
            vector<int> d;
            for (int i = 0; i + 1 < (int)w.size(); ++i)
                d.push_back(w[i+1] - w[i]);
            return d;
        };
        
        vector<int> d0 = diff(words[0]);
        vector<int> d1 = diff(words[1]);
        vector<int> d2 = diff(words[2]);
        vector<int> common;
        
        if (d0 == d1 || d0 == d2) {
            common = d0;
            if (d0 != d1 && d0 != d2) return words[1]; // actually unreachable
        } else {
            common = d1; // then words[0] is the odd one
            return words[0];
        }
        
        for (int i = 3; i < (int)words.size(); ++i) {
            if (diff(words[i]) != common)
                return words[i];
        }
        // If not found in later indices, it must be among first three already handled.
        // But to satisfy compiler, return empty string (should never happen).
        return "";
    }
};
```

## Java

```java
class Solution {
    public String oddString(String[] words) {
        int n = words[0].length();
        // Compute differences for first three words to determine the common pattern
        int[][] sampleDiffs = new int[3][n - 1];
        for (int i = 0; i < 3; i++) {
            sampleDiffs[i] = diffArray(words[i]);
        }
        int[] common;
        if (java.util.Arrays.equals(sampleDiffs[0], sampleDiffs[1])) {
            common = sampleDiffs[0];
        } else if (java.util.Arrays.equals(sampleDiffs[0], sampleDiffs[2])) {
            common = sampleDiffs[0];
        } else {
            common = sampleDiffs[1];
        }
        // Find and return the word whose difference array differs from the common one
        for (String w : words) {
            if (!java.util.Arrays.equals(diffArray(w), common)) {
                return w;
            }
        }
        return ""; // Fallback, problem guarantees an answer exists
    }

    private int[] diffArray(String s) {
        int len = s.length();
        int[] diff = new int[len - 1];
        for (int i = 0; i < len - 1; i++) {
            diff[i] = s.charAt(i + 1) - s.charAt(i);
        }
        return diff;
    }
}
```

## Python

```python
class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def diff(w):
            return tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1))
        
        # Determine the common difference array using first three words
        d0, d1, d2 = diff(words[0]), diff(words[1]), diff(words[2])
        if d0 == d1 or d0 == d2:
            common = d0
        else:
            common = d1  # then d1 must equal d2
        
        for w in words:
            if diff(w) != common:
                return w
        return ""  # fallback, should never reach here
```

## Python3

```python
from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(s: str):
            return tuple(ord(s[i+1]) - ord(s[i]) for i in range(len(s)-1))
        
        # Determine the common difference array using first three strings
        d0 = diff(words[0])
        d1 = diff(words[1])
        d2 = diff(words[2])
        if d0 == d1 or d0 == d2:
            common = d0
        else:
            common = d1  # then d1 == d2
        
        for w in words:
            if diff(w) != common:
                return w
        return ""  # fallback, should never happen given constraints
```

## C

```c
#include <string.h>

static void computeDiff(const char *s, int *out, int len) {
    for (int i = 0; i < len; ++i)
        out[i] = (s[i + 1] - 'a') - (s[i] - 'a');
}

static int equalDiff(const int *a, const int *b, int len) {
    for (int i = 0; i < len; ++i)
        if (a[i] != b[i]) return 0;
    return 1;
}

char* oddString(char **words, int wordsSize) {
    int n = strlen(words[0]);
    int dlen = n - 1;

    int diff0[20], diff1[20], diff2[20];
    computeDiff(words[0], diff0, dlen);
    computeDiff(words[1], diff1, dlen);

    int common[20];
    if (equalDiff(diff0, diff1, dlen)) {
        memcpy(common, diff0, dlen * sizeof(int));
    } else {
        computeDiff(words[2], diff2, dlen);
        if (equalDiff(diff0, diff2, dlen))
            memcpy(common, diff0, dlen * sizeof(int));
        else
            memcpy(common, diff1, dlen * sizeof(int));
    }

    int tmp[20];
    for (int i = 0; i < wordsSize; ++i) {
        computeDiff(words[i], tmp, dlen);
        if (!equalDiff(tmp, common, dlen))
            return words[i];
    }
    return NULL;
}
```

## Csharp

```csharp
public class Solution {
    public string OddString(string[] words) {
        var dict = new Dictionary<string, (int count, int idx)>();
        for (int i = 0; i < words.Length; i++) {
            var w = words[i];
            var sb = new System.Text.StringBuilder();
            for (int j = 0; j < w.Length - 1; j++) {
                int diff = w[j + 1] - w[j];
                sb.Append(diff).Append('#');
            }
            string key = sb.ToString();
            if (dict.ContainsKey(key)) {
                var val = dict[key];
                dict[key] = (val.count + 1, val.idx);
            } else {
                dict[key] = (1, i);
            }
        }
        foreach (var kvp in dict) {
            if (kvp.Value.count == 1) {
                return words[kvp.Value.idx];
            }
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var oddString = function(words) {
    const diffKey = (word) => {
        const diffs = [];
        for (let i = 0; i < word.length - 1; ++i) {
            diffs.push(word.charCodeAt(i + 1) - word.charCodeAt(i));
        }
        return diffs.join(',');
    };
    
    const d0 = diffKey(words[0]);
    const d1 = diffKey(words[1]);
    const d2 = diffKey(words[2]);
    
    let common;
    if (d0 === d1 || d0 === d2) {
        common = d0;
    } else {
        common = d1; // d1 must equal d2
    }
    
    for (const w of words) {
        if (diffKey(w) !== common) return w;
    }
    return ""; // should never reach here per constraints
};
```

## Typescript

```typescript
function oddString(words: string[]): string {
    const diffMap = new Map<string, { count: number; idx: number }>();
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        const diffs: number[] = [];
        for (let j = 0; j < w.length - 1; j++) {
            diffs.push(w.charCodeAt(j + 1) - w.charCodeAt(j));
        }
        const key = diffs.join(',');
        if (!diffMap.has(key)) {
            diffMap.set(key, { count: 1, idx: i });
        } else {
            diffMap.get(key)!.count++;
        }
    }
    for (const { count, idx } of diffMap.values()) {
        if (count === 1) return words[idx];
    }
    return "";
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String[] $words
     * @return String
     */
    function oddString($words) {
        $diffs = [];
        foreach ($words as $w) {
            $diffs[] = $this->getDiff($w);
        }
        if ($diffs[0] === $diffs[1] || $diffs[0] === $diffs[2]) {
            $common = $diffs[0];
        } else {
            $common = $diffs[1];
        }
        foreach ($diffs as $i => $d) {
            if ($d !== $common) {
                return $words[$i];
            }
        }
        return "";
    }

    private function getDiff($word) {
        $len = strlen($word);
        $arr = [];
        for ($i = 0; $i < $len - 1; $i++) {
            $a = ord($word[$i]) - 97;
            $b = ord($word[$i + 1]) - 97;
            $arr[] = $b - $a;
        }
        return implode(',', $arr);
    }
}
?>
```

## Swift

```swift
class Solution {
    func oddString(_ words: [String]) -> String {
        let diff0 = diff(words[0])
        let diff1 = diff(words[1])
        if diff0 == diff1 {
            for i in 2..<words.count {
                if diff(words[i]) != diff0 {
                    return words[i]
                }
            }
        } else {
            let diff2 = diff(words[2])
            if diff0 == diff2 {
                return words[1]
            } else {
                return words[0]
            }
        }
        return ""
    }
    
    private func diff(_ s: String) -> [Int] {
        let bytes = Array(s.utf8)
        var res = [Int]()
        for i in 0..<(bytes.count - 1) {
            res.append(Int(bytes[i + 1]) - Int(bytes[i]))
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun oddString(words: Array<String>): String {
        fun diff(s: String): IntArray {
            val n = s.length
            val arr = IntArray(n - 1)
            for (i in 0 until n - 1) {
                arr[i] = (s[i + 1] - 'a') - (s[i] - 'a')
            }
            return arr
        }

        val d0 = diff(words[0])
        val d1 = diff(words[1])
        val d2 = diff(words[2])

        val common: IntArray = if (d0.contentEquals(d1) || d0.contentEquals(d2)) {
            d0
        } else {
            d1 // d1 must equal d2
        }

        for (i in words.indices) {
            if (!diff(words[i]).contentEquals(common)) {
                return words[i]
            }
        }
        return "" // should never reach here
    }
}
```

## Dart

```dart
class Solution {
  String oddString(List<String> words) {
    // Helper to compute a unique key for the difference array of a word
    String diffKey(String s) {
      List<int> diffs = [];
      for (int i = 0; i < s.length - 1; i++) {
        diffs.add(s.codeUnitAt(i + 1) - s.codeUnitAt(i));
      }
      return diffs.join(',');
    }

    // Map from difference key to its occurrence count
    final Map<String, int> freq = {};

    // First pass: count frequencies of each difference pattern
    for (final w in words) {
      final key = diffKey(w);
      freq[key] = (freq[key] ?? 0) + 1;
    }

    // Second pass: find the word whose pattern occurs only once
    for (final w in words) {
      if ((freq[diffKey(w)] ?? 0) == 1) {
        return w;
      }
    }

    // According to problem constraints, this line is never reached.
    return "";
  }
}
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

func oddString(words []string) string {
	diffMap := make(map[string]int)
	keys := make([]string, len(words))

	for i, w := range words {
		var sb strings.Builder
		for j := 0; j < len(w)-1; j++ {
			if j > 0 {
				sb.WriteByte('#')
			}
			diff := int(w[j+1] - w[j])
			sb.WriteString(strconv.Itoa(diff))
		}
		key := sb.String()
		keys[i] = key
		diffMap[key]++
	}

	for i, k := range keys {
		if diffMap[k] == 1 {
			return words[i]
		}
	}
	return ""
}
```

## Ruby

```ruby
def odd_string(words)
  groups = Hash.new { |h, k| h[k] = [] }
  words.each do |w|
    diff = []
    (0...w.length - 1).each { |i| diff << w[i + 1].ord - w[i].ord }
    groups[diff] << w
  end
  groups.each_value { |arr| return arr.first if arr.size == 1 }
end
```

## Scala

```scala
object Solution {
    def oddString(words: Array[String]): String = {
        def diff(s: String): IndexedSeq[Int] = {
            val arr = new Array[Int](s.length - 1)
            var i = 0
            while (i < s.length - 1) {
                arr(i) = s.charAt(i + 1) - s.charAt(i)
                i += 1
            }
            arr.toIndexedSeq
        }

        val firstThreeDiffs = words.take(3).map(diff)
        val common = if (firstThreeDiffs(0) == firstThreeDiffs(1) || firstThreeDiffs(0) == firstThreeDiffs(2))
                        firstThreeDiffs(0)
                     else
                        firstThreeDiffs(1)

        var idx = 0
        while (idx < words.length) {
            if (diff(words(idx)) != common) return words(idx)
            idx += 1
        }
        ""
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn odd_string(words: Vec<String>) -> String {
        let mut count: HashMap<Vec<i32>, usize> = HashMap::new();
        let mut diffs: Vec<Vec<i32>> = Vec::with_capacity(words.len());

        for w in &words {
            let d = Self::diff(w);
            *count.entry(d.clone()).or_insert(0) += 1;
            diffs.push(d);
        }

        for (i, d) in diffs.iter().enumerate() {
            if count.get(d) == Some(&1usize) {
                return words[i].clone();
            }
        }
        String::new()
    }

    fn diff(s: &str) -> Vec<i32> {
        let bytes = s.as_bytes();
        let mut v = Vec::with_capacity(bytes.len() - 1);
        for i in 0..bytes.len() - 1 {
            v.push(bytes[i + 1] as i32 - bytes[i] as i32);
        }
        v
    }
}
```

## Racket

```racket
(define (diff-list s)
  (let ((len (string-length s)))
    (for/list ([i (in-range (- len 1))])
      (- (char->integer (string-ref s (+ i 1)))
         (char->integer (string-ref s i))))))

(define/contract (odd-string words)
  (-> (listof string?) string?)
  (let ((hash (make-hash))
        (pairs
          (for/list ([w words])
            (let ((d (diff-list w)))
              (hash-update! hash d (lambda (cnt) (+ cnt 1)) 0)
              (cons w d)))))
    (define odd-diff
      (for/first ([k (in-hash-keys hash)]
                  #:when (= (hash-ref hash k) 1))
        k))
    (for/first ([p pairs]
                #:when (equal? (cdr p) odd-diff))
      (car p))))
```

## Erlang

```erlang
-spec odd_string(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
odd_string(Words) ->
    [W1, W2, W3 | Rest] = Words,
    D1 = diff(W1),
    D2 = diff(W2),
    D3 = diff(W3),
    Common = case {D1 == D2, D1 == D3} of
        {true, _} -> D1;
        {false, true} -> D1;
        _ -> D2
    end,
    find_odd([W1, W2, W3 | Rest], Common).

diff(Word) ->
    Codes = binary_to_list(Word),
    diff_codes(Codes).

diff_codes([_]) -> [];
diff_codes([A, B | Tail]) ->
    [B - A | diff_codes([B | Tail])].

find_odd([], _) -> <<>>;
find_odd([Word | Rest], Common) ->
    case diff(Word) == Common of
        true -> find_odd(Rest, Common);
        false -> Word
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec odd_string(words :: [String.t]) :: String.t
  def odd_string(words) do
    diffs = Enum.map(words, fn w -> {w, diff(w)} end)
    groups = Enum.group_by(diffs, fn {_w, d} -> d end, fn {w, _d} -> w end)

    {_key, [odd_word]} =
      Enum.find(groups, fn {_k, v} -> length(v) == 1 end)

    odd_word
  end

  defp diff(word) do
    chars = String.to_charlist(word)

    Enum.zip(chars, tl(chars))
    |> Enum.map(fn {a, b} -> b - a end)
  end
end
```
