# 0139. Word Break

## Cpp

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int maxLen = 0;
        for (const string& w : wordDict) maxLen = max(maxLen, (int)w.size());

        int n = s.size();
        vector<bool> dp(n + 1, false);
        dp[0] = true;

        for (int i = 1; i <= n; ++i) {
            int start = max(0, i - maxLen);
            for (int j = start; j < i; ++j) {
                if (!dp[j]) continue;
                if (dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        int maxLen = 0;
        for (String w : wordDict) {
            if (w.length() > maxLen) {
                maxLen = w.length();
            }
        }
        for (int i = 0; i < n; i++) {
            if (!dp[i]) continue;
            int limit = Math.min(maxLen, n - i);
            for (int l = 1; l <= limit; l++) {
                if (dict.contains(s.substring(i, i + l))) {
                    dp[i + l] = true;
                }
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # only need to check substrings up to max_len
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

## Python3

```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            # only need to check substrings up to max_len
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool wordBreak(char* s, char** wordDict, int wordDictSize) {
    int n = strlen(s);
    bool *dp = (bool *)calloc(n + 1, sizeof(bool));
    dp[0] = true;
    for (int i = 1; i <= n; ++i) {
        for (int w = 0; w < wordDictSize; ++w) {
            int len = strlen(wordDict[w]);
            if (len <= i && dp[i - len]) {
                if (strncmp(s + i - len, wordDict[w], len) == 0) {
                    dp[i] = true;
                    break;
                }
            }
        }
    }
    bool result = dp[n];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool WordBreak(string s, IList<string> wordDict)
    {
        var dict = new HashSet<string>(wordDict);
        int maxLen = 0;
        foreach (var w in dict)
            if (w.Length > maxLen) maxLen = w.Length;

        int n = s.Length;
        var dp = new bool[n + 1];
        dp[0] = true;

        for (int i = 1; i <= n; ++i)
        {
            for (int len = 1; len <= maxLen && len <= i; ++len)
            {
                if (!dp[i - len]) continue;
                if (dict.Contains(s.Substring(i - len, len)))
                {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    const dict = new Set(wordDict);
    let maxLen = 0;
    for (const w of wordDict) {
        if (w.length > maxLen) maxLen = w.length;
    }
    const n = s.length;
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 0; i < n; i++) {
        if (!dp[i]) continue;
        for (let len = 1; len <= maxLen && i + len <= n; len++) {
            if (dict.has(s.substring(i, i + len))) {
                dp[i + len] = true;
            }
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet = new Set(wordDict);
    const n = s.length;
    const dp: boolean[] = Array(n + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $wordDict
     * @return Boolean
     */
    function wordBreak($s, $wordDict) {
        $n = strlen($s);
        if ($n == 0) return true;

        // Build set for O(1) lookups and find max word length
        $wordSet = [];
        $maxLen = 0;
        foreach ($wordDict as $w) {
            $wordSet[$w] = true;
            $len = strlen($w);
            if ($len > $maxLen) $maxLen = $len;
        }

        // dp[i] means s[0..i-1] can be segmented
        $dp = array_fill(0, $n + 1, false);
        $dp[0] = true;

        for ($i = 1; $i <= $n; $i++) {
            $limit = min($i, $maxLen);
            for ($len = 1; $len <= $limit; $len++) {
                $j = $i - $len;
                if (!$dp[$j]) continue;
                $sub = substr($s, $j, $len);
                if (isset($wordSet[$sub])) {
                    $dp[$i] = true;
                    break;
                }
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
        let n = s.count
        var dp = Array(repeating: false, count: n + 1)
        dp[0] = true
        let chars = Array(s)
        let words = wordDict.map { Array($0) }
        
        for i in 0..<n {
            if !dp[i] { continue }
            for w in words {
                let len = w.count
                if i + len > n { continue }
                var match = true
                for j in 0..<len {
                    if chars[i + j] != w[j] {
                        match = false
                        break
                    }
                }
                if match {
                    dp[i + len] = true
                }
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val dict = HashSet(wordDict)
        val n = s.length
        val dp = BooleanArray(n + 1)
        dp[0] = true
        for (i in 1..n) {
            for (j in 0 until i) {
                if (dp[j] && dict.contains(s.substring(j, i))) {
                    dp[i] = true
                    break
                }
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  bool wordBreak(String s, List<String> wordDict) {
    final Set<String> dict = Set.from(wordDict);
    final int n = s.length;
    final List<bool> dp = List.filled(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; i++) {
      for (int j = 0; j < i; j++) {
        if (dp[j] && dict.contains(s.substring(j, i))) {
          dp[i] = true;
          break;
        }
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func wordBreak(s string, wordDict []string) bool {
	dict := make(map[string]struct{}, len(wordDict))
	maxLen := 0
	for _, w := range wordDict {
		dict[w] = struct{}{}
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		start := i - maxLen
		if start < 0 {
			start = 0
		}
		for j := start; j < i; j++ {
			if !dp[j] {
				continue
			}
			if _, ok := dict[s[j:i]]; ok {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def word_break(s, word_dict)
  word_set = {}
  word_dict.each { |w| word_set[w] = true }
  n = s.length
  dp = Array.new(n + 1, false)
  dp[0] = true

  (1..n).each do |i|
    (0...i).each do |j|
      if dp[j] && word_set.key?(s[j, i - j])
        dp[i] = true
        break
      end
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
  def wordBreak(s: String, wordDict: List[String]): Boolean = {
    val dict = wordDict.toSet
    if (dict.isEmpty) return false
    val maxLen = wordDict.map(_.length).max
    val n = s.length
    val dp = new Array[Boolean](n + 1)
    dp(0) = true
    var i = 1
    while (i <= n) {
      var j = math.max(0, i - maxLen)
      var found = false
      while (j < i && !found) {
        if (dp(j) && dict.contains(s.substring(j, i))) {
          dp(i) = true
          found = true
        }
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let word_set: HashSet<String> = word_dict.into_iter().collect();
        let n = s.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for i in 1..=n {
            for j in 0..i {
                if dp[j] && word_set.contains(&s[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        dp[n]
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (word-break s wordDict)
  (-> string? (listof string?) boolean?)
  (let* ([n (string-length s)]
         [dict (list->set wordDict)]
         [dp (make-vector (add1 n) #f)])
    (vector-set! dp 0 #t)
    (for ([i (in-range 1 (add1 n))])
      (let loop ((j 0))
        (when (and (not (vector-ref dp i)) (< j i))
          (if (and (vector-ref dp j)
                   (set-member? dict (substring s j i)))
              (vector-set! dp i #t)
              (loop (add1 j))))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([word_break/2]).
-spec word_break(S :: unicode:unicode_binary(), WordDict :: [unicode:unicode_binary()]) -> boolean().
word_break(S, WordDict) ->
    Dict = maps:from_list([{W,true} || W <- WordDict]),
    Len = byte_size(S),
    DP0 = #{0 => true},
    ResultDP = word_break_loop(1, Len, S, Dict, DP0),
    maps:get(Len, ResultDP, false).

word_break_loop(I, Len, _S, _Dict, DP) when I > Len ->
    DP;
word_break_loop(I, Len, S, Dict, DP) ->
    case can_reach(I, S, Dict, DP) of
        true  -> word_break_loop(I + 1, Len, S, Dict, DP#{I => true});
        false -> word_break_loop(I + 1, Len, S, Dict, DP)
    end.

can_reach(I, S, Dict, DP) ->
    can_reach_j(0, I, S, Dict, DP).

can_reach_j(J, I, _S, _Dict, _DP) when J >= I ->
    false;
can_reach_j(J, I, S, Dict, DP) ->
    case maps:get(J, DP, false) of
        true ->
            Len = I - J,
            Sub = binary:part(S, {J, Len}),
            case maps:is_key(Sub, Dict) of
                true -> true;
                false -> can_reach_j(J + 1, I, S, Dict, DP)
            end;
        false ->
            can_reach_j(J + 1, I, S, Dict, DP)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec word_break(s :: String.t(), word_dict :: [String.t()]) :: boolean()
  def word_break(s, word_dict) do
    words = MapSet.new(word_dict)

    max_len =
      case word_dict do
        [] -> 0
        _ ->
          word_dict
          |> Enum.map(&String.length/1)
          |> Enum.max()
      end

    n = String.length(s)

    dp = :array.new(n + 1, default: false)
    dp = :array.set(0, true, dp)

    final_dp =
      Enum.reduce(0..(n - 1), dp, fn i, acc_dp ->
        if :array.get(i, acc_dp) do
          Enum.reduce(1..max_len, acc_dp, fn l, inner_acc ->
            j = i + l

            if j <= n do
              sub = String.slice(s, i, l)

              if MapSet.member?(words, sub) do
                :array.set(j, true, inner_acc)
              else
                inner_acc
              end
            else
              inner_acc
            end
          end)
        else
          acc_dp
        end
      end)

    :array.get(n, final_dp)
  end
end
```
