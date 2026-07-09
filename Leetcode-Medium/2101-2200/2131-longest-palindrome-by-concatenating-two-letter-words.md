# 2131. Longest Palindrome by Concatenating Two Letter Words

## Cpp

```cpp
class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string,int> cnt;
        for (const string& w : words) ++cnt[w];
        
        int ans = 0;
        bool hasCenter = false;
        
        for (auto& entry : cnt) {
            const string& w = entry.first;
            int c = entry.second;
            if (c == 0) continue;
            
            if (w[0] == w[1]) { // palindrome word like "aa"
                ans += (c / 2) * 4;          // pair them
                if (c % 2 == 1) hasCenter = true; // one can be placed in the middle
            } else {
                string rev = {w[1], w[0]};
                auto itRev = cnt.find(rev);
                if (itRev != cnt.end()) {
                    int pairs = min(c, itRev->second);
                    ans += pairs * 4;
                    entry.second -= pairs;
                    itRev->second -= pairs;
                }
            }
        }
        
        if (hasCenter) ans += 2;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestPalindrome(String[] words) {
        int[][] cnt = new int[26][26];
        for (String w : words) {
            int a = w.charAt(0) - 'a';
            int b = w.charAt(1) - 'a';
            cnt[a][b]++;
        }
        int ans = 0;
        boolean hasCenter = false;
        // palindromic pairs like "aa"
        for (int i = 0; i < 26; i++) {
            int same = cnt[i][i];
            ans += (same / 2) * 4;
            if ((same & 1) == 1) {
                hasCenter = true;
            }
        }
        // non‑palindromic pairs like "ab" and "ba"
        for (int i = 0; i < 26; i++) {
            for (int j = i + 1; j < 26; j++) {
                int pairs = Math.min(cnt[i][j], cnt[j][i]);
                ans += pairs * 4;
            }
        }
        if (hasCenter) {
            ans += 2;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(words)
        ans = 0
        center_used = False

        # handle palindromic words like "aa"
        for w, c in cnt.items():
            if w[0] == w[1]:
                pairs = c // 2
                ans += pairs * 4
                if c % 2 == 1 and not center_used:
                    ans += 2
                    center_used = True

        # handle non‑palindromic pairs like "ab" with "ba"
        for w, c in cnt.items():
            if w[0] != w[1]:
                rev = w[::-1]
                if rev in cnt and w < rev:   # ensure each unordered pair counted once
                    ans += min(c, cnt[rev]) * 4

        return ans
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        middle_used = False

        for w in list(cnt.keys()):
            c = cnt[w]
            if c == 0:
                continue
            rev = w[::-1]

            if w[0] == w[1]:  # palindrome word like "aa"
                pairs = c // 2
                res += pairs * 4
                if not middle_used and c % 2 == 1:
                    middle_used = True
            else:
                if rev in cnt:
                    pairs = min(c, cnt[rev])
                    res += pairs * 4
                    cnt[w] = 0
                    cnt[rev] = 0

        if middle_used:
            res += 2
        return res
```

## C

```c
#include <stddef.h>

int longestPalindrome(char** words, int wordsSize) {
    const int N = 26 * 26;
    int cnt[N];
    for (int i = 0; i < N; ++i) cnt[i] = 0;

    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int idx = (w[0] - 'a') * 26 + (w[1] - 'a');
        ++cnt[idx];
    }

    int ans = 0;
    int has_center = 0;

    for (int i = 0; i < N; ++i) {
        int c1 = i / 26, c2 = i % 26;
        if (c1 == c2) { // palindrome word like "aa"
            ans += (cnt[i] / 2) * 4;
            if (cnt[i] % 2 == 1) has_center = 1;
        } else if (c1 < c2) { // handle each unordered pair once
            int rev = c2 * 26 + c1;
            int pairs = cnt[i] < cnt[rev] ? cnt[i] : cnt[rev];
            ans += pairs * 4;
        }
    }

    if (has_center) ans += 2;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestPalindrome(string[] words) {
        var freq = new Dictionary<string, int>();
        foreach (var w in words) {
            if (!freq.ContainsKey(w)) freq[w] = 0;
            freq[w]++;
        }

        int result = 0;
        bool hasCenter = false;

        foreach (var word in new List<string>(freq.Keys)) {
            int cnt = freq[word];
            if (cnt == 0) continue;

            if (word[0] == word[1]) { // palindrome word like "aa"
                int pairs = cnt / 2;
                result += pairs * 4; // each pair contributes 4 characters
                if (!hasCenter && cnt % 2 == 1) {
                    hasCenter = true; // one can be placed in the middle
                }
            } else {
                string rev = new string(new char[] { word[1], word[0] });
                if (freq.ContainsKey(rev)) {
                    int pairCount = Math.Min(cnt, freq[rev]);
                    result += pairCount * 4;
                    freq[word] -= pairCount;
                    freq[rev] -= pairCount;
                }
            }
        }

        if (hasCenter) result += 2;
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var longestPalindrome = function(words) {
    const freq = new Map();
    for (const w of words) {
        freq.set(w, (freq.get(w) || 0) + 1);
    }
    
    let ans = 0;
    let centerUsed = false;
    
    for (const [w, cnt] of freq.entries()) {
        if (cnt === 0) continue;
        const rev = w[1] + w[0];
        
        if (w === rev) { // palindrome word like "aa"
            const pairs = Math.floor(cnt / 2);
            ans += pairs * 4; // each pair adds two words => length 4
            if (!centerUsed && cnt % 2 === 1) {
                ans += 2;      // one unpaired word can be placed in the center
                centerUsed = true;
            }
        } else if (freq.has(rev)) {
            const revCnt = freq.get(rev);
            const pairCount = Math.min(cnt, revCnt);
            ans += pairCount * 4;
            // zero out both to avoid recounting
            freq.set(w, 0);
            freq.set(rev, 0);
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function longestPalindrome(words: string[]): number {
    const freq = new Map<string, number>();
    for (const w of words) {
        freq.set(w, (freq.get(w) || 0) + 1);
    }

    let result = 0;
    let centerUsed = false;
    const visited = new Set<string>();

    for (const [word, count] of freq.entries()) {
        if (visited.has(word)) continue;

        if (word[0] === word[1]) { // palindrome word like "aa"
            const pairs = Math.floor(count / 2);
            result += pairs * 4; // each pair contributes 4 characters
            if (!centerUsed && count % 2 === 1) {
                centerUsed = true; // one can be placed in the middle
            }
        } else {
            const rev = word[1] + word[0];
            if (freq.has(rev)) {
                const revCount = freq.get(rev)!;
                const pairs = Math.min(count, revCount);
                result += pairs * 4; // each matched pair contributes 4 characters
                visited.add(word);
                visited.add(rev);
            }
        }
    }

    if (centerUsed) result += 2; // add the central palindrome word length
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function longestPalindrome($words) {
        $cnt = [];
        foreach ($words as $w) {
            if (!isset($cnt[$w])) $cnt[$w] = 0;
            $cnt[$w]++;
        }

        $ans = 0;
        $centerUsed = false;

        foreach ($cnt as $word => $c) {
            $rev = strrev($word);
            // palindrome word like "aa"
            if ($word[0] === $word[1]) {
                $pairs = intdiv($c, 2);
                $ans += $pairs * 4; // each pair contributes two words (2+2)
                if (!$centerUsed && $c % 2 == 1) {
                    $centerUsed = true;
                }
            } elseif (isset($cnt[$rev])) {
                // process each unordered pair once
                if ($word < $rev) {
                    $pairs = min($c, $cnt[$rev]);
                    $ans += $pairs * 4; // word + its reverse
                }
            }
        }

        if ($centerUsed) {
            $ans += 2;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ words: [String]) -> Int {
        var freq = [String:Int]()
        for w in words {
            freq[w, default: 0] += 1
        }
        
        var ans = 0
        var hasCenter = false
        
        for word in Array(freq.keys) {
            guard let cnt = freq[word], cnt > 0 else { continue }
            let chars = Array(word)
            if chars[0] == chars[1] {
                ans += (cnt / 2) * 4
                if cnt % 2 == 1 {
                    hasCenter = true
                }
            } else {
                let rev = String(chars.reversed())
                if let revCnt = freq[rev], revCnt > 0 {
                    let pairs = min(cnt, revCnt)
                    ans += pairs * 4
                    freq[word] = cnt - pairs
                    freq[rev] = revCnt - pairs
                }
            }
        }
        
        if hasCenter {
            ans += 2
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(words: Array<String>): Int {
        val freq = IntArray(26 * 26)
        for (w in words) {
            val idx = (w[0] - 'a') * 26 + (w[1] - 'a')
            freq[idx]++
        }
        var ans = 0
        var centerUsed = false
        for (i in 0 until 26 * 26) {
            val a = i / 26
            val b = i % 26
            if (a == b) {
                // words like "aa"
                ans += (freq[i] / 2) * 4
                if (!centerUsed && freq[i] % 2 == 1) {
                    centerUsed = true
                    ans += 2
                }
            } else {
                val revIdx = b * 26 + a
                if (i < revIdx) { // handle each pair once
                    val pairs = kotlin.math.min(freq[i], freq[revIdx])
                    ans += pairs * 4
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int longestPalindrome(List<String> words) {
    final Map<String, int> freq = {};
    for (var w in words) {
      freq[w] = (freq[w] ?? 0) + 1;
    }

    int ans = 0;
    bool hasCenter = false;

    final List<String> keys = freq.keys.toList();
    for (final String w in keys) {
      int cnt = freq[w]!;
      if (cnt == 0) continue;

      final String rev = '${w[1]}${w[0]}';
      if (w == rev) {
        // palindrome word like "aa"
        int pairs = cnt ~/ 2;
        ans += pairs * 4; // each pair adds two words => length 4
        if (!hasCenter && cnt % 2 == 1) {
          hasCenter = true;
        }
      } else {
        if (freq.containsKey(rev)) {
          int revCnt = freq[rev]!;
          int pairCount = cnt < revCnt ? cnt : revCnt;
          ans += pairCount * 4;
          // mark both as used
          freq[w] = 0;
          freq[rev] = 0;
        }
      }
    }

    if (hasCenter) ans += 2;
    return ans;
  }
}
```

## Golang

```go
func longestPalindrome(words []string) int {
    freq := make(map[string]int, len(words))
    for _, w := range words {
        freq[w]++
    }

    ans := 0
    centerUsed := false

    // Handle palindromic words like "aa"
    for w, cnt := range freq {
        if w[0] == w[1] {
            pairs := cnt / 2
            ans += pairs * 4 // each pair contributes two words of length 2
            if cnt%2 == 1 && !centerUsed {
                ans += 2 // one word can be placed in the middle
                centerUsed = true
            }
        }
    }

    // Handle non‑palindromic words by matching with their reverse
    for w, cnt := range freq {
        if w[0] == w[1] {
            continue
        }
        rev := string([]byte{w[1], w[0]})
        if cntRev, ok := freq[rev]; ok && w < rev { // process each unordered pair once
            pairs := cnt
            if cntRev < pairs {
                pairs = cntRev
            }
            ans += pairs * 4
        }
    }

    return ans
}
```

## Ruby

```ruby
def longest_palindrome(words)
  freq = Hash.new(0)
  words.each { |w| freq[w] += 1 }

  ans = 0
  middle_used = false
  keys = freq.keys

  keys.each do |word|
    cnt = freq[word]
    next if cnt == 0

    if word[0] == word[1] # palindromic word like "aa"
      pairs = cnt / 2
      ans += pairs * 4
      middle_used ||= (cnt % 2 == 1)
    else
      rev = word.reverse
      next unless freq.key?(rev)
      # process each unordered pair only once
      if word < rev
        pairs = [cnt, freq[rev]].min
        ans += pairs * 4
        freq[word] -= pairs
        freq[rev] -= pairs
      end
    end
  end

  ans + (middle_used ? 2 : 0)
end
```

## Scala

```scala
object Solution {
  def longestPalindrome(words: Array[String]): Int = {
    import scala.collection.mutable

    val freq = mutable.Map[String, Int]().withDefaultValue(0)
    for (w <- words) {
      freq(w) += 1
    }

    var ans = 0
    var centerAdded = false

    // Process each distinct word
    for ((word, cnt) <- freq.toList) {
      if (word.charAt(0) == word.charAt(1)) { // palindrome word like "aa"
        val pairs = cnt / 2
        ans += pairs * 4               // each pair contributes 4 characters
        if (cnt % 2 == 1 && !centerAdded) {
          ans += 2                     // one unpaired can be placed in the center
          centerAdded = true
        }
      } else {
        val rev = word.reverse
        if (freq.contains(rev) && word < rev) { // handle each unordered pair once
          val minCnt = math.min(cnt, freq(rev))
          ans += minCnt * 4
        }
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        const SZ: usize = 26 * 26;
        let mut cnt = vec![0i32; SZ];
        for w in words.iter() {
            let b = w.as_bytes();
            let a_idx = (b[0] - b'a') as usize;
            let b_idx = (b[1] - b'a') as usize;
            cnt[a_idx * 26 + b_idx] += 1;
        }
        let mut ans: i32 = 0;
        let mut have_center = false;
        for i in 0..SZ {
            let a = i / 26;
            let b = i % 26;
            if a == b {
                ans += (cnt[i] / 2) * 4;
                if cnt[i] % 2 == 1 {
                    have_center = true;
                }
            } else if i < b * 26 + a {
                let rev = b * 26 + a;
                let pairs = std::cmp::min(cnt[i], cnt[rev]);
                ans += pairs * 4;
            }
        }
        if have_center {
            ans += 2;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-palindrome words)
  (-> (listof string?) exact-integer?)
  (let* ((freq (make-hash))
         (inc (lambda (w)
                (hash-set! freq w (+ (hash-ref freq w 0) 1)))))
    (for-each inc words)
    (define total 0)
    (define middle-used? #f)
    (for ([key (in-hash-keys freq)])
      (let ((cnt (hash-ref freq key)))
        (when (> cnt 0)
          (define rev (string-append (substring key 1 2) (substring key 0 1)))
          (cond
            [(string=? key rev) ; palindrome word like "aa"
             (define pairs (quotient cnt 2))
             (set! total (+ total (* pairs 4)))
             (when (and (not middle-used?) (= (remainder cnt 2) 1))
               (set! total (+ total 2))
               (set! middle-used? #t))]
            [else
             (define revcnt (hash-ref freq rev 0))
             (define pairs (min cnt revcnt))
             (when (> pairs 0)
               (set! total (+ total (* pairs 4)))
               (hash-set! freq key 0)
               (hash-set! freq rev 0))]))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([longest_palindrome/1]).

-spec longest_palindrome(Words :: [unicode:unicode_binary()]) -> integer().
longest_palindrome(Words) ->
    Freq = build_freq(Words, #{}),
    NonPalLen = nonpal_len(Freq),
    {PalLen, HasCenter} = pal_len_and_center(Freq),
    Total = NonPalLen + PalLen + (if HasCenter -> 2; true -> 0 end),
    Total.

%% Build frequency map of words
build_freq([], M) ->
    M;
build_freq([W | Rest], M) ->
    Count = maps:get(W, M, 0),
    build_freq(Rest, M#{W => Count + 1}).

%% Length contributed by non‑palindromic pairs (e.g., "ab" with "ba")
nonpal_len(Freq) ->
    maps:fold(
      fun(Key, Count, Acc) ->
          <<A, B>> = Key,
          Rev = <<B, A>>,
          case Key == Rev of
              true -> Acc;                     % skip palindromic words here
              false ->
                  case Key < Rev of
                      true ->
                          RevCount = maps:get(Rev, Freq, 0),
                          Pair = erlang:min(Count, RevCount),
                          Acc + Pair * 4;
                      false -> Acc
                  end
          end
      end,
      0,
      Freq).

%% Length from palindromic words ("aa", "bb") and whether a center word exists
pal_len_and_center(Freq) ->
    maps:fold(
      fun(Key, Count, {LenAcc, CenterAcc}) ->
          <<A, B>> = Key,
          case A == B of
              true ->
                  Pair = Count div 2,
                  NewLen = LenAcc + Pair * 4,
                  NewCenter = CenterAcc orelse (Count rem 2 == 1),
                  {NewLen, NewCenter};
              false -> {LenAcc, CenterAcc}
          end
      end,
      {0, false},
      Freq).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(words :: [String.t]) :: integer
  def longest_palindrome(words) do
    freq = Enum.frequencies(words)

    {len, has_center} =
      Enum.reduce(freq, {0, false}, fn {word, cnt}, {acc_len, acc_center} ->
        if word == String.reverse(word) do
          pairs = div(cnt, 2)
          new_len = acc_len + pairs * 4
          new_center = acc_center || rem(cnt, 2) == 1
          {new_len, new_center}
        else
          rev = String.reverse(word)

          case String.compare(word, rev) do
            :lt ->
              cnt_rev = Map.get(freq, rev, 0)
              matched = min(cnt, cnt_rev)
              {acc_len + matched * 4, acc_center}

            _ ->
              {acc_len, acc_center}
          end
        end
      end)

    if has_center do
      len + 2
    else
      len
    end
  end
end
```
