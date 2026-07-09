# 1639. Number of Ways to Form a Target String Given a Dictionary

## Cpp

```cpp
class Solution {
public:
    int numWays(vector<string>& words, string target) {
        const int MOD = 1000000007;
        int m = words[0].size();
        int n = target.size();
        vector<array<int,26>> freq(m);
        for (int i = 0; i < m; ++i) freq[i].fill(0);
        for (const string& w : words) {
            for (int i = 0; i < m; ++i) {
                ++freq[i][w[i] - 'a'];
            }
        }
        vector<long long> dp(n + 1, 0);
        dp[0] = 1;
        for (int col = 0; col < m; ++col) {
            for (int t = n; t >= 1; --t) {
                int ch = target[t - 1] - 'a';
                if (freq[col][ch]) {
                    dp[t] = (dp[t] + freq[col][ch] * dp[t - 1]) % MOD;
                }
            }
        }
        return (int)dp[n];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int numWays(String[] words, String target) {
        int m = words[0].length();          // length of each word (columns)
        int n = target.length();            // length of target
        
        if (m < n) return 0;                // not enough columns to form target
        
        // frequency[col][char] = count of char at position col across all words
        int[][] freq = new int[m][26];
        for (String w : words) {
            for (int i = 0; i < m; ++i) {
                freq[i][w.charAt(i) - 'a']++;
            }
        }
        
        // dp[t] = ways to form first t characters of target using processed columns so far
        int[] dp = new int[n + 1];
        dp[0] = 1;
        
        for (int col = 0; col < m; ++col) {
            // update dp in reverse to avoid overwriting needed values
            for (int t = n; t >= 1; --t) {
                int chIdx = target.charAt(t - 1) - 'a';
                long add = (long) freq[col][chIdx] * dp[t - 1];
                dp[t] = (int) ((dp[t] + add) % MOD);
            }
        }
        
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)
        # frequency of each character at every column
        freq = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                freq[i][ord(ch) - 97] += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for col in range(m):
            # only need to consider target lengths up to columns processed so far
            upper = min(col + 1, n)
            for t in range(upper, 0, -1):
                c_idx = ord(target[t - 1]) - 97
                cnt = freq[col][c_idx]
                if cnt:
                    dp[t] = (dp[t] + cnt * dp[t - 1]) % MOD
        return dp[n]
```

## Python3

```python
import sys
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)
        
        # frequency of each character at each column
        freq = [[0] * 26 for _ in range(m)]
        for w in words:
            for i, ch in enumerate(w):
                freq[i][ord(ch) - 97] += 1
        
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to form empty target
        
        for col in range(m):
            t_char_idx = ord(target[0]) - 97  # placeholder, will be used inside loop
            # update dp backwards to avoid using updated values within same column
            for j in range(min(col + 1, n), 0, -1):
                char_idx = ord(target[j - 1]) - 97
                if freq[col][char_idx]:
                    dp[j] = (dp[j] + freq[col][char_idx] * dp[j - 1]) % MOD
        
        return dp[n]
```

## C

```c
#include <string.h>
#include <stdlib.h>

#define MOD 1000000007

int numWays(char** words, int wordsSize, char* target) {
    int m = strlen(words[0]);
    int n = strlen(target);
    
    // frequency matrix: freq[col][char]
    int **freq = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; ++i) {
        freq[i] = (int*)calloc(26, sizeof(int));
    }
    for (int w = 0; w < wordsSize; ++w) {
        char *s = words[w];
        for (int i = 0; i < m; ++i) {
            freq[i][s[i] - 'a']++;
        }
    }
    
    int *dp = (int*)calloc(n + 1, sizeof(int));
    dp[0] = 1;
    
    for (int col = 0; col < m; ++col) {
        for (int t = n - 1; t >= 0; --t) {
            int cnt = freq[col][target[t] - 'a'];
            if (cnt) {
                long long add = (long long)cnt * dp[t] % MOD;
                dp[t + 1] += (int)add;
                if (dp[t + 1] >= MOD) dp[t + 1] -= MOD;
            }
        }
    }
    
    int ans = dp[n];
    
    for (int i = 0; i < m; ++i) free(freq[i]);
    free(freq);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    public int NumWays(string[] words, string target)
    {
        int m = words[0].Length;
        int n = target.Length;

        // frequency of each character at every column
        int[][] freq = new int[m][];
        for (int i = 0; i < m; i++) freq[i] = new int[26];

        foreach (var w in words)
        {
            for (int i = 0; i < m; i++)
            {
                freq[i][w[i] - 'a']++;
            }
        }

        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int col = 0; col < m; col++)
        {
            // update dp in reverse to use previous column values
            for (int t = n; t >= 1; t--)
            {
                int cnt = freq[col][target[t - 1] - 'a'];
                if (cnt == 0) continue;
                long add = ((long)dp[t - 1] * cnt) % MOD;
                dp[t] = (int)((dp[t] + add) % MOD);
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var numWays = function(words, target) {
    const MOD = 1000000007;
    const m = words[0].length;
    const n = target.length;

    // frequency of each character at each column
    const freq = Array.from({ length: m }, () => new Uint32Array(26));
    for (const w of words) {
        for (let i = 0; i < m; ++i) {
            const c = w.charCodeAt(i) - 97;
            freq[i][c] += 1;
        }
    }

    // dp[t]: ways to form first t characters of target using processed columns
    const dp = new Uint32Array(n + 1);
    dp[0] = 1;

    for (let col = 0; col < m; ++col) {
        // iterate backwards to use previous column values
        for (let t = n; t >= 1; --t) {
            const cIdx = target.charCodeAt(t - 1) - 97;
            const cnt = freq[col][cIdx];
            if (cnt === 0) continue;
            const add = (cnt * dp[t - 1]) % MOD;
            dp[t] = (dp[t] + add) % MOD;
        }
    }

    return Number(dp[n]);
};
```

## Typescript

```typescript
function numWays(words: string[], target: string): number {
    const MOD = 1_000_000_007;
    const m = words[0].length;
    const n = target.length;

    // frequency of each character at each column
    const freq: number[][] = Array.from({ length: m }, () => new Array(26).fill(0));
    for (const w of words) {
        for (let i = 0; i < m; ++i) {
            const idx = w.charCodeAt(i) - 97;
            freq[i][idx]++;
        }
    }

    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let col = 0; col < m; ++col) {
        const fcol = freq[col];
        for (let t = n; t >= 1; --t) {
            const chIdx = target.charCodeAt(t - 1) - 97;
            const cnt = fcol[chIdx];
            if (cnt > 0) {
                dp[t] = (dp[t] + cnt * dp[t - 1]) % MOD;
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
     * @param String[] $words
     * @param String $target
     * @return Integer
     */
    function numWays($words, $target) {
        $MOD = 1000000007;
        $m = strlen($words[0]);
        $n = strlen($target);
        
        // frequency of each character at each column
        $freq = array_fill(0, $m, array_fill(0, 26, 0));
        foreach ($words as $w) {
            for ($i = 0; $i < $m; $i++) {
                $cIdx = ord($w[$i]) - 97;
                $freq[$i][$cIdx]++;
            }
        }
        
        // dp[t] = ways to form first t characters of target
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        
        for ($col = 0; $col < $m; $col++) {
            // update dp in reverse to use each column at most once
            for ($t = $n; $t >= 1; $t--) {
                $charIdx = ord($target[$t - 1]) - 97;
                $cnt = $freq[$col][$charIdx];
                if ($cnt > 0) {
                    $dp[$t] = ($dp[$t] + $dp[$t - 1] * $cnt) % $MOD;
                }
            }
        }
        
        return $dp[$n];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func numWays(_ words: [String], _ target: String) -> Int {
        guard let firstWord = words.first else { return 0 }
        let m = firstWord.count
        let n = target.count
        if m < n { return 0 }
        
        // Frequency matrix: m columns x 26 letters
        var freq = Array(repeating: Array(repeating: 0, count: 26), count: m)
        for w in words {
            let chars = Array(w.utf8)
            for i in 0..<m {
                let idx = Int(chars[i] - 97) // 'a' ascii is 97
                freq[i][idx] += 1
            }
        }
        
        // Convert target to indices 0..25
        let tChars = Array(target.utf8)
        var targetIdx = [Int]()
        targetIdx.reserveCapacity(n)
        for ch in tChars {
            targetIdx.append(Int(ch - 97))
        }
        
        var dp = Array(repeating: Int64(0), count: n + 1)
        dp[0] = 1
        
        for col in 0..<m {
            // Update dp backwards to use previous column values
            if n == 0 { break }
            for t in stride(from: n, through: 1, by: -1) {
                let cIdx = targetIdx[t - 1]
                let ways = freq[col][cIdx]
                if ways > 0 {
                    dp[t] = (dp[t] + dp[t - 1] * Int64(ways)) % Int64(MOD)
                }
            }
        }
        
        return Int(dp[n])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numWays(words: Array<String>, target: String): Int {
        val MOD = 1_000_000_007L
        val m = words[0].length
        val n = target.length

        // frequency of each character at each column
        val freq = Array(m) { IntArray(26) }
        for (w in words) {
            for (i in w.indices) {
                val chIdx = w[i] - 'a'
                freq[i][chIdx]++
            }
        }

        val dp = LongArray(n + 1)
        dp[0] = 1L

        for (col in 0 until m) {
            val f = freq[col]
            var t = n
            while (t >= 1) {
                val idx = target[t - 1] - 'a'
                val cnt = f[idx]
                if (cnt != 0) {
                    dp[t] = (dp[t] + cnt * dp[t - 1]) % MOD
                }
                t--
            }
        }

        return dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numWays(List<String> words, String target) {
    if (words.isEmpty) return 0;
    int m = words[0].length;
    int n = target.length;
    // Frequency of each character at each column
    List<List<int>> freq = List.generate(m, (_) => List.filled(26, 0));
    for (var w in words) {
      for (int i = 0; i < m; ++i) {
        int idx = w.codeUnitAt(i) - 97;
        freq[i][idx]++;
      }
    }

    // dp[j] = ways to form first j characters of target
    List<int> dp = List.filled(n + 1, 0);
    dp[0] = 1;

    for (int col = 0; col < m; ++col) {
      // iterate backwards to avoid using updated values in the same column
      for (int j = n; j >= 1; --j) {
        int charIdx = target.codeUnitAt(j - 1) - 97;
        int cnt = freq[col][charIdx];
        if (cnt == 0) continue;
        dp[j] = (dp[j] + (cnt * dp[j - 1]) % _mod) % _mod;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
package main

import "fmt"

const mod int64 = 1000000007

func numWays(words []string, target string) int {
	m := len(words[0])
	n := len(target)

	// frequency of each character at each column
	freq := make([][26]int, m)
	for _, w := range words {
		for i, ch := range w {
			freq[i][ch-'a']++
		}
	}

	dp := make([]int64, n+1)
	dp[0] = 1

	for col := 0; col < m; col++ {
		// update dp backwards to use previous column values
		for t := n; t >= 1; t-- {
			cIdx := target[t-1] - 'a'
			if cnt := freq[col][cIdx]; cnt > 0 {
				dp[t] = (dp[t] + int64(cnt)*dp[t-1]) % mod
			}
		}
	}

	return int(dp[n])
}

// The following main function is only for local testing and will be ignored by LeetCode.
func main() {
	fmt.Println(numWays([]string{"acca", "bbbb", "caca"}, "aba")) // expected 6
	fmt.Println(numWays([]string{"abba", "baab"}, "bab"))       // expected 4
}
```

## Ruby

```ruby
def num_ways(words, target)
  mod = 1_000_000_007
  m = words[0].length
  n = target.length

  freq = Array.new(m) { Array.new(26, 0) }
  words.each do |w|
    w.each_char.with_index do |ch, i|
      freq[i][ch.ord - 97] += 1
    end
  end

  dp = Array.new(n + 1, 0)
  dp[0] = 1

  (0...m).each do |col|
    n.downto(1) do |t|
      idx = target[t - 1].ord - 97
      cnt = freq[col][idx]
      next if cnt == 0
      dp[t] = (dp[t] + cnt * dp[t - 1]) % mod
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L
  def numWays(words: Array[String], target: String): Int = {
    val m = words(0).length
    val n = target.length
    val freq = Array.ofDim[Int](m, 26)
    var wIdx = 0
    while (wIdx < words.length) {
      val w = words(wIdx)
      var i = 0
      while (i < m) {
        val c = w.charAt(i) - 'a'
        freq(i)(c) += 1
        i += 1
      }
      wIdx += 1
    }

    val dp = new Array[Long](n + 1)
    dp(0) = 1L

    var col = 0
    while (col < m) {
      var t = n - 1
      while (t >= 0) {
        val chIdx = target.charAt(t) - 'a'
        val cnt = freq(col)(chIdx)
        if (cnt != 0) {
          dp(t + 1) = (dp(t + 1) + dp(t) * cnt) % MOD
        }
        t -= 1
      }
      col += 1
    }

    dp(n).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_ways(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = words[0].len();
        let n = target.len();
        // frequency of each character at each column
        let mut freq = vec![[0i64; 26]; m];
        for w in &words {
            let bytes = w.as_bytes();
            for (j, &b) in bytes.iter().enumerate() {
                freq[j][(b - b'a') as usize] += 1;
            }
        }

        let target_bytes = target.as_bytes();
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;

        for col in 0..m {
            let col_freq = &freq[col];
            // iterate backwards to avoid using updated values in the same column
            for t in (1..=n).rev() {
                let idx = (target_bytes[t - 1] - b'a') as usize;
                let cnt = col_freq[idx];
                if cnt != 0 {
                    dp[t] = (dp[t] + cnt * dp[t - 1]) % MOD;
                }
            }
        }

        dp[n] as i32
    }
}
```

## Racket

```racket
#lang racket
(provide num-ways)

(define MOD 1000000007)

(define/contract (num-ways words target)
  (-> (listof string?) string? exact-integer?)
  (let* ([m (string-length (first words))]
         [n (string-length target)])
    ;; frequency matrix: m columns, each a vector of 26 counts
    (define freq (make-vector m))
    (for ([i (in-range m)])
      (vector-set! freq i (make-vector 26 0)))
    ;; fill frequencies
    (for ([w words])
      (for ([i (in-range m)])
        (let* ([c (string-ref w i)]
               [idx (- (char->integer c) (char->integer #\a))]
               [col (vector-ref freq i)])
          (vector-set! col idx (+ (vector-ref col idx) 1)))))
    ;; dp array, size n+1
    (define dp (make-vector (+ n 1) 0))
    (vector-set! dp 0 1)
    ;; iterate over each column position
    (for ([pos (in-range m)])
      (let ([col (vector-ref freq pos)])
        (for ([t (in-range n 0 -1)]) ; t = n .. 1
          (when (> t 0)
            (let* ([char-idx (- (char->integer (string-ref target (- t 1)))
                                (char->integer #\a))]
                   [cnt (vector-ref col char-idx)])
              (when (> cnt 0)
                (define prev (vector-ref dp (- t 1)))
                (define cur (vector-ref dp t))
                (define new (+ cur (* cnt prev)))
                (vector-set! dp t (modulo new MOD))))))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-module(solution).
-export([num_ways/2]).
-define(MOD, 1000000007).

num_ways(Words, Target) ->
    WordLen = byte_size(hd(Words)),
    TargetLen = byte_size(Target),
    FreqArray = build_freq(Words, WordLen),
    TargetIdxTuple = build_target_idx(Target, TargetLen),
    DP0 = array:set(0, 1, array:new(TargetLen + 1)),
    DPFinal = dp_loop(WordLen, 0, FreqArray, DP0, TargetIdxTuple, TargetLen),
    array:get(TargetLen, DPFinal).

build_freq(Words, WordLen) ->
    build_freq(Words, WordLen, array:new(WordLen)).

build_freq([], _, Acc) -> Acc;
build_freq([W|Rest], WordLen, Acc) ->
    Acc1 = update_word(W, WordLen, 0, Acc),
    build_freq(Rest, WordLen, Acc1).

update_word(_Word, WordLen, Pos, Acc) when Pos >= WordLen -> Acc;
update_word(Word, WordLen, Pos, Acc) ->
    CharCode = binary:at(Word, Pos) - $a,
    CharIdx = CharCode + 1,
    Tuple0 = case array:get(Pos, Acc) of
                undefined -> erlang:make_tuple(27, 0);
                T -> T
            end,
    Count = element(CharIdx, Tuple0),
    NewTuple = setelement(CharIdx, Tuple0, Count + 1),
    Acc1 = array:set(Pos, NewTuple, Acc),
    update_word(Word, WordLen, Pos + 1, Acc1).

build_target_idx(TargetBin, Len) ->
    build_target_idx(TargetBin, Len, erlang:make_tuple(Len, 0), 0).

build_target_idx(_Bin, Len, Tuple, Pos) when Pos >= Len -> Tuple;
build_target_idx(Bin, Len, Tuple, Pos) ->
    CharCode = binary:at(Bin, Pos) - $a,
    CharIdx = CharCode + 1,
    NewTuple = setelement(Pos + 1, Tuple, CharIdx),
    build_target_idx(Bin, Len, NewTuple, Pos + 1).

dp_loop(WordLen, I, _FreqArray, DP, _TargetIdxTuple, _TargetLen) when I >= WordLen ->
    DP;
dp_loop(WordLen, I, FreqArray, DP, TargetIdxTuple, TargetLen) ->
    Tuple = array:get(I, FreqArray),
    MaxJ = erlang:min(I + 1, TargetLen),
    DP1 = dp_update(MaxJ, DP, Tuple, TargetIdxTuple),
    dp_loop(WordLen, I + 1, FreqArray, DP1, TargetIdxTuple, TargetLen).

dp_update(J, DP, _Tuple, _TargetIdxTuple) when J =< 0 ->
    DP;
dp_update(J, DP, Tuple, TargetIdxTuple) ->
    Prev = array:get(J - 1, DP),
    Cur = array:get(J, DP),
    CharIdx = element(J, TargetIdxTuple),
    CountChar = element(CharIdx, Tuple),
    Add = (CountChar * Prev) rem ?MOD,
    NewCur = (Cur + Add) rem ?MOD,
    DP2 = array:set(J, NewCur, DP),
    dp_update(J - 1, DP2, Tuple, TargetIdxTuple).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec num_ways(words :: [String.t()], target :: String.t()) :: integer()
  def num_ways(words, target) do
    l = String.length(List.first(words))
    n = String.length(target)

    if n > l do
      0
    else
      freq =
        Enum.reduce(words, %{}, fn word, acc ->
          chars = String.to_charlist(word)

          Enum.with_index(chars)
          |> Enum.reduce(acc, fn {ch, idx}, a ->
            c = ch - ?a
            Map.update(a, {idx, c}, 1, &(&1 + 1))
          end)
        end)

      mod = 1_000_000_007

      dp0 = :array.new(n + 1, default: 0) |> :array.set(0, 1)

      dp_final =
        Enum.reduce(0..(l - 1), dp0, fn i, dp_acc ->
          Enum.reduce(Enum.reverse(0..(n - 1)), dp_acc, fn j, dp_inner ->
            c_target = :binary.at(target, j)
            count = Map.get(freq, {i, c_target - ?a}, 0)

            if count == 0 do
              dp_inner
            else
              prev = :array.get(j, dp_inner)
              cur = :array.get(j + 1, dp_inner)
              new_val = rem(cur + prev * count, mod)
              :array.set(j + 1, new_val, dp_inner)
            end
          end)
        end)

      :array.get(n, dp_final)
    end
  end
end
```
