# 3403. Find the Lexicographically Largest String From the Box I

## Cpp

```cpp
class Solution {
public:
    string answerString(string word, int numFriends) {
        int n = word.size();
        int limit = n - numFriends + 1; // maximum possible length of a piece
        string best = "";
        for (int i = 0; i < n; ++i) {
            int len = min(limit, n - i);
            string cand = word.substr(i, len);
            if (cand > best) best = cand;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String answerString(String word, int numFriends) {
        int n = word.length();
        int maxLen = n - numFriends + 1; // guaranteed >= 1
        if (numFriends == 1) {
            return word;
        }
        int i = 0, j = 1, k = 0;
        while (i < n && j < n && k < n) {
            char a = word.charAt(i + k);
            char b = word.charAt(j + k);
            if (a == b) {
                k++;
                continue;
            }
            if (a > b) {
                // suffix starting at i is larger, skip j
                j = j + k + 1;
            } else {
                // suffix starting at j is larger, skip i
                i = i + k + 1;
            }
            if (i == j) {
                i++;
            }
            k = 0;
        }
        int start = Math.min(i, j);
        int end = Math.min(start + maxLen, n);
        return word.substring(start, end);
    }
}
```

## Python

```python
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        n = len(word)
        max_len = n - numFriends + 1  # maximum allowed length
        best = ""
        for i in range(n):
            cand = word[i:i + max_len]
            if cand > best:
                best = cand
        return best
```

## Python3

```python
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        L = n - numFriends + 1
        i, j, k = 0, 1, 0
        while j + k < n:
            if word[i + k] == word[j + k]:
                k += 1
                continue
            if word[i + k] > word[j + k]:
                j = j + k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        start = i
        return word[start:start + L]
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* answerString(char* word, int numFriends) {
    int n = strlen(word);
    if (numFriends == 1) {
        char *res = (char*)malloc(n + 1);
        strcpy(res, word);
        return res;
    }
    int limit = n - numFriends + 1;   // maximum allowed length

    // Find the start index of the lexicographically largest suffix
    int i = 0, j = 1, k = 0;
    while (j + k < n && i + k < n) {
        if (word[i + k] == word[j + k]) {
            ++k;
            continue;
        }
        if (word[i + k] > word[j + k]) {
            j = j + k + 1;          // suffix at i is larger, skip j
        } else {
            i = (i + k + 1 > j) ? i + k + 1 : j;
            j = i + 1;              // suffix at j is larger, move i forward
        }
        k = 0;
    }
    int start = i;

    int maxLen = n - start;
    int ansLen = (maxLen < limit) ? maxLen : limit;

    char *ans = (char*)malloc(ansLen + 1);
    memcpy(ans, word + start, ansLen);
    ans[ansLen] = '\0';
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public string AnswerString(string word, int numFriends) {
        int n = word.Length;
        if (numFriends == 1) return word;
        int maxLen = n - numFriends + 1;
        string best = "";
        for (int i = 0; i < n; ++i) {
            int len = Math.Min(maxLen, n - i);
            string cand = word.Substring(i, len);
            if (string.Compare(cand, best) > 0) {
                best = cand;
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} numFriends
 * @return {string}
 */
var answerString = function(word, numFriends) {
    const n = word.length;
    if (numFriends === 1) return word; // must take the whole string

    const maxLen = n - numFriends + 1;

    // Find start index of lexicographically largest suffix
    let i = 0, j = 1, k = 0;
    while (j < n) {
        const a = word.charCodeAt(i + k);
        const b = word.charCodeAt(j + k);
        if (a === b) {
            k++;
            // If we reached the end of either suffix, break
            if (i + k >= n || j + k >= n) break;
            continue;
        }
        if (a > b) {
            // suffix at i is larger, skip over j's candidate
            j = j + k + 1;
        } else {
            // suffix at j is larger, move i forward
            i = Math.max(i + k + 1, j);
            j = i + 1;
        }
        k = 0;
    }

    const start = i;
    return word.substring(start, Math.min(n, start + maxLen));
};
```

## Typescript

```typescript
function answerString(word: string, numFriends: number): string {
    if (numFriends === 1) return word;
    const n = word.length;
    const maxLen = n - numFriends + 1;

    // Find the starting index of the lexicographically largest suffix
    let i = 0, j = 1, k = 0;
    while (j + k < n) {
        const a = word.charCodeAt(i + k);
        const b = word.charCodeAt(j + k);
        if (a === b) {
            k++;
        } else if (a > b) {
            j = j + k + 1;
            k = 0;
        } else {
            i = Math.max(i + k + 1, j);
            j = i + 1;
            k = 0;
        }
    }
    const start = Math.min(i, j);
    const len = Math.min(maxLen, n - start);
    return word.substring(start, start + len);
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $numFriends
     * @return String
     */
    function answerString($word, $numFriends) {
        $n = strlen($word);
        if ($numFriends == 1) {
            return $word;
        }

        // Find the start index of the lexicographically largest suffix
        $i = 0;      // candidate start
        $j = 1;      // next start to compare
        $k = 0;      // offset for comparison

        while ($j + $k < $n) {
            $a = $word[$i + $k];
            $b = $word[$j + $k];
            if ($a === $b) {
                $k++;
                continue;
            }
            if ($a > $b) {
                // suffix at j is smaller, skip it
                $j = $j + $k + 1;
            } else {
                // suffix at i is smaller, move i to j
                $i = max($i + $k + 1, $j);
                $j = $i + 1;
            }
            $k = 0;
        }

        $start = $i;
        $maxLen = $n - $numFriends + 1; // maximum allowed length
        $takeLen = min($maxLen, $n - $start);

        return substr($word, $start, $takeLen);
    }
}
```

## Swift

```swift
class Solution {
    func answerString(_ word: String, _ numFriends: Int) -> String {
        let n = word.count
        if numFriends == 1 { return word }
        let maxLen = n - numFriends + 1
        let chars = Array(word)
        var i = 0
        var j = 1
        while j < n {
            var k = 0
            while i + k < n && j + k < n && chars[i + k] == chars[j + k] {
                k += 1
            }
            if j + k == n { break }
            if i + k == n {
                i = j
                j = i + 1
                continue
            }
            if chars[i + k] < chars[j + k] {
                i = j
                j = i + 1
            } else {
                j = j + k + 1
            }
        }
        let endIdx = min(i + maxLen, n)
        return String(chars[i..<endIdx])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun answerString(word: String, numFriends: Int): String {
        val n = word.length
        if (numFriends == 1) return word
        val maxLen = n - numFriends + 1

        var i = 0
        var j = 1
        var k = 0
        while (j + k < n) {
            val a = word[i + k]
            val b = word[j + k]
            if (a == b) {
                k++
            } else if (a < b) {
                i = maxOf(i + k + 1, j)
                j = i + 1
                k = 0
            } else { // a > b
                j = j + k + 1
                k = 0
            }
        }

        val start = i
        val end = minOf(start + maxLen, n)
        return word.substring(start, end)
    }
}
```

## Dart

```dart
class Solution {
  String answerString(String word, int numFriends) {
    int n = word.length;
    int maxLen = n - numFriends + 1;
    // Find the start index of the lexicographically largest suffix
    int i = 0, j = 1, k = 0;
    while (j < n) {
      while (i + k < n && j + k < n &&
          word.codeUnitAt(i + k) == word.codeUnitAt(j + k)) {
        k++;
      }
      if (j + k >= n) break;
      if (word.codeUnitAt(i + k) > word.codeUnitAt(j + k)) {
        // suffix at i is larger, skip j
        j = j + k + 1;
      } else {
        // suffix at j is larger, move i forward
        i = i + k + 1;
        if (i >= j) i = j;
        j = i + 1;
      }
      k = 0;
    }
    int start = i;
    int end = start + maxLen;
    if (end > n) end = n;
    return word.substring(start, end);
  }
}
```

## Golang

```go
func answerString(word string, numFriends int) string {
    n := len(word)
    if numFriends == 1 {
        return word
    }
    maxLen := n - numFriends + 1

    // Find the starting index of the lexicographically largest suffix.
    i, j, k := 0, 1, 0
    for j < n && i < n {
        if i+k >= n || j+k >= n {
            break
        }
        a := word[i+k]
        b := word[j+k]
        if a == b {
            k++
            continue
        }
        if a < b {
            // suffix starting at j is larger
            i = i + k + 1
            if i <= j {
                i = j + 1
            }
            j = i + 1
        } else { // a > b
            // suffix starting at i is larger
            j = j + k + 1
        }
        k = 0
    }

    start := i
    if start >= n {
        start = n - 1
    }
    end := start + maxLen
    if end > n {
        end = n
    }
    return word[start:end]
}
```

## Ruby

```ruby
def answer_string(word, num_friends)
  return word if num_friends == 1
  n = word.length
  max_len = n - num_friends + 1
  best = ""
  (0...n).each do |i|
    len = [max_len, n - i].min
    substr = word[i, len]
    best = substr if substr > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def answerString(word: String, numFriends: Int): String = {
        val n = word.length
        if (numFriends == 1) return word

        var i = 0          // candidate start index of best suffix
        var j = 1          // next start to compare
        var k = 0          // offset for comparison

        while (j < n && i + k < n) {
            val a = word.charAt(i + k)
            val b = word.charAt(j + k)
            if (a == b) {
                k += 1
            } else if (a > b) {
                j = j + k + 1
                k = 0
            } else { // a < b
                i = Math.max(i + k + 1, j)
                j = i + 1
                k = 0
            }
        }

        val start = i
        val maxLen = n - numFriends + 1
        val end = Math.min(n, start + maxLen)
        word.substring(start, end)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let max_len = n - (num_friends as usize) + 1;

        // start index of the best substring
        let mut best_start = 0usize;
        for i in 0..n {
            let cur_len = std::cmp::min(max_len, n - i);
            let best_len = std::cmp::min(max_len, n - best_start);
            if bytes[i..i + cur_len] > bytes[best_start..best_start + best_len] {
                best_start = i;
            }
        }

        let best_len = std::cmp::min(max_len, n - best_start);
        String::from_utf8(bytes[best_start..best_start + best_len].to_vec()).unwrap()
    }
}
```

## Racket

```racket
(define/contract (answer-string word numFriends)
  (-> string? exact-integer? string?)
  (define n (string-length word))
  (define maxlen (+ (- n numFriends) 1)) ; maximum allowed length
  ;; Find start index of lexicographically largest suffix
  (define (find-start s)
    (let ((len (string-length s)))
      (let recur ((i 0) (j 1) (k 0))
        (if (or (>= j len)
                (>= (+ i k) len)
                (>= (+ j k) len))
            i
            (let ((ci (string-ref s (+ i k)))
                  (cj (string-ref s (+ j k))))
              (cond [(char=? ci cj) (recur i j (+ k 1))]
                    [(char>? ci cj) (recur i (+ j k 1) 0)]
                    [else
                     (let ((newi (max (+ i k 1) j)))
                       (recur newi (+ newi 1) 0))]))))))
  (if (= numFriends 1)
      word
      (let* ((start (find-start word))
             (len   (min maxlen (- n start))))
        (substring word start (+ start len)))))
```

## Erlang

```erlang
-spec answer_string(Word :: unicode:unicode_binary(), NumFriends :: integer()) -> unicode:unicode_binary().
answer_string(Word, NumFriends) ->
    N = byte_size(Word),
    MaxLen = N - NumFriends + 1,
    find_best(Word, N, MaxLen, 0, <<>>).

find_best(_Word, _N, _MaxLen, Start, Best) when Start >= _N ->
    Best;
find_best(Word, N, MaxLen, Start, Best) ->
    Len = erlang:min(MaxLen, N - Start),
    Sub = binary:part(Word, Start, Len),
    NewBest = if Sub > Best -> Sub; true -> Best end,
    find_best(Word, N, MaxLen, Start + 1, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec answer_string(word :: String.t(), num_friends :: integer) :: String.t()
  def answer_string(word, num_friends) do
    n = byte_size(word)
    max_len_allowed = n - num_friends + 1

    start = find_start(word, n, 0, 1, 0)

    len = min(max_len_allowed, n - start)
    :binary.part(word, start, len)
  end

  defp find_start(_word, n, i, _j, _k) when i >= n, do: i
  defp find_start(word, n, i, j, k) do
    if j + k >= n do
      i
    else
      a = :binary.at(word, i + k)
      b = :binary.at(word, j + k)

      cond do
        a == b ->
          find_start(word, n, i, j, k + 1)

        a > b ->
          # suffix at i is larger; skip the block starting at j
          new_j = j + k + 1
          find_start(word, n, i, new_j, 0)

        true ->
          # suffix at j is larger; move i forward
          new_i = max(i + k + 1, j)
          new_j = new_i + 1
          find_start(word, n, new_i, new_j, 0)
      end
    end
  end
end
```
