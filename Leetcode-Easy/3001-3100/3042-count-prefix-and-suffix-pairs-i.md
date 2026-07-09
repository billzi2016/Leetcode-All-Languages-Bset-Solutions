# 3042. Count Prefix and Suffix Pairs I

## Cpp

```cpp
class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int n = words.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            const string& a = words[i];
            int la = a.size();
            for (int j = i + 1; j < n; ++j) {
                const string& b = words[j];
                if ((int)b.size() < la) continue;
                // check prefix
                bool isPrefix = true;
                for (int k = 0; k < la; ++k) {
                    if (b[k] != a[k]) { isPrefix = false; break; }
                }
                if (!isPrefix) continue;
                // check suffix
                bool isSuffix = true;
                int offset = b.size() - la;
                for (int k = 0; k < la; ++k) {
                    if (b[offset + k] != a[k]) { isSuffix = false; break; }
                }
                if (isSuffix) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int n = words.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            String prefix = words[i];
            int len = prefix.length();
            for (int j = i + 1; j < n; j++) {
                if (words[j].length() < len) continue;
                if (words[j].startsWith(prefix) && words[j].endsWith(prefix)) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        count = 0
        for i in range(n):
            wi = words[i]
            for j in range(i + 1, n):
                wj = words[j]
                if wj.startswith(wi) and wj.endswith(wi):
                    count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            wi = words[i]
            for j in range(i + 1, n):
                wj = words[j]
                if len(wi) > len(wj):
                    continue
                if wj.startswith(wi) and wj.endswith(wi):
                    count += 1
        return count
```

## C

```c
#include <string.h>

int countPrefixSuffixPairs(char** words, int wordsSize) {
    int count = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int len_i = strlen(words[i]);
        for (int j = i + 1; j < wordsSize; ++j) {
            int len_j = strlen(words[j]);
            if (len_i > len_j) continue;
            if (strncmp(words[i], words[j], len_i) != 0) continue;
            const char *suffix = words[j] + len_j - len_i;
            if (strcmp(words[i], suffix) == 0) ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountPrefixSuffixPairs(string[] words)
    {
        int n = words.Length;
        int count = 0;
        for (int i = 0; i < n; ++i)
        {
            string prefix = words[i];
            int len = prefix.Length;
            for (int j = i + 1; j < n; ++j)
            {
                if (words[j].Length < len) continue;
                if (words[j].StartsWith(prefix) && words[j].EndsWith(prefix))
                    count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    let n = words.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const s = words[i];
        for (let j = i + 1; j < n; ++j) {
            const t = words[j];
            if (s.length > t.length) continue;
            if (t.startsWith(s) && t.endsWith(s)) ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countPrefixSuffixPairs(words: string[]): number {
    let count = 0;
    const n = words.length;
    for (let i = 0; i < n; i++) {
        const short = words[i];
        for (let j = i + 1; j < n; j++) {
            const long = words[j];
            if (short.length > long.length) continue;
            if (long.startsWith(short) && long.endsWith(short)) {
                count++;
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function countPrefixSuffixPairs($words) {
        $n = count($words);
        $count = 0;
        for ($i = 0; $i < $n; ++$i) {
            $lenI = strlen($words[$i]);
            for ($j = $i + 1; $j < $n; ++$j) {
                $lenJ = strlen($words[$j]);
                // the shorter word must be a prefix and suffix of the longer one
                if ($lenI > $lenJ) continue;
                $short = $words[$i];
                $long  = $words[$j];
                if (substr($long, 0, $lenI) === $short && substr($long, -$lenI) === $short) {
                    ++$count;
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countPrefixSuffixPairs(_ words: [String]) -> Int {
        var result = 0
        let n = words.count
        for i in 0..<n {
            let short = words[i]
            for j in (i + 1)..<n {
                let long = words[j]
                if short.count > long.count { continue }
                if long.hasPrefix(short) && long.hasSuffix(short) {
                    result += 1
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
    fun countPrefixSuffixPairs(words: Array<String>): Int {
        var count = 0
        val n = words.size
        for (i in 0 until n) {
            val w1 = words[i]
            for (j in i + 1 until n) {
                val w2 = words[j]
                if (w1.length <= w2.length && w2.startsWith(w1) && w2.endsWith(w1)) {
                    count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countPrefixSuffixPairs(List<String> words) {
    int n = words.length;
    int count = 0;
    for (int i = 0; i < n; ++i) {
      String a = words[i];
      for (int j = i + 1; j < n; ++j) {
        String b = words[j];
        if (a.length > b.length) continue;
        if (b.startsWith(a) && b.endsWith(a)) {
          count++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
import "strings"

func countPrefixSuffixPairs(words []string) int {
	cnt := 0
	for i := 0; i < len(words); i++ {
		for j := i + 1; j < len(words); j++ {
			if len(words[i]) > len(words[j]) {
				continue
			}
			if strings.HasPrefix(words[j], words[i]) && strings.HasSuffix(words[j], words[i]) {
				cnt++
			}
		}
	}
	return cnt
}
```

## Ruby

```ruby
def count_prefix_suffix_pairs(words)
  n = words.length
  count = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      wi = words[i]
      wj = words[j]
      if wj.start_with?(wi) && wj.end_with?(wi)
        count += 1
      end
    end
  end
  count
end
```

## Scala

```scala
object Solution {
  def countPrefixSuffixPairs(words: Array[String]): Int = {
    var count = 0
    val n = words.length
    for (i <- 0 until n) {
      val w1 = words(i)
      for (j <- i + 1 until n) {
        val w2 = words(j)
        if (w1.length <= w2.length && w2.startsWith(w1) && w2.endsWith(w1)) {
          count += 1
        }
      }
    }
    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut count = 0;
        for i in 0..n {
            let w1 = &words[i];
            for j in (i + 1)..n {
                let w2 = &words[j];
                if w1.len() <= w2.len()
                    && w2.starts_with(w1)
                    && w2.ends_with(w1)
                {
                    count += 1;
                }
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (count-prefix-suffix-pairs words)
  (-> (listof string?) exact-integer?)
  (let* ((n (length words))
         (vec (list->vector words)))
    (for/sum ([i (in-range n)]
              [j (in-range (+ i 1) n)])
      (if (and (string-prefix? (vector-ref vec i) (vector-ref vec j))
               (string-suffix? (vector-ref vec i) (vector-ref vec j)))
          1
          0))))
```

## Erlang

```erlang
-module(solution).
-export([count_prefix_suffix_pairs/1]).

-spec count_prefix_suffix_pairs(Words :: [unicode:unicode_binary()]) -> integer().
count_prefix_suffix_pairs(Words) ->
    Indexed = indexed(Words),
    length([1 || {A, I} <- Indexed,
                 {B, J} <- Indexed,
                 I < J,
                 is_prefix_and_suffix(A, B)]).

indexed(List) -> indexed(List, 0).
indexed([], _) -> [];
indexed([H|T], N) ->
    [{H, N}|indexed(T, N + 1)].

is_prefix_and_suffix(Pref, Str) ->
    LenPref = byte_size(Pref),
    LenStr = byte_size(Str),
    if
        LenPref > LenStr -> false;
        true ->
            case Str of
                <<Pref:LenPref/binary, _/binary>> ->
                    case Str of
                        <<_/binary, Pref:LenPref/binary>> -> true;
                        _ -> false
                    end;
                _ -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_prefix_suffix_pairs(words :: [String.t]) :: integer
  def count_prefix_suffix_pairs(words) do
    words
    |> Enum.with_index()
    |> Enum.reduce(0, fn {word_i, i}, acc ->
      rest = Enum.drop(words, i + 1)

      cnt =
        Enum.count(rest, fn word_j ->
          len_i = String.length(word_i)
          len_j = String.length(word_j)

          len_i <= len_j and
            String.starts_with?(word_j, word_i) and
            String.ends_with?(word_j, word_i)
        end)

      acc + cnt
    end)
  end
end
```
