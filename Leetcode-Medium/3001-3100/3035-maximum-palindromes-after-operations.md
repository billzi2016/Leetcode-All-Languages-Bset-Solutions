# 3035. Maximum Palindromes After Operations

## Cpp

```cpp
class Solution {
public:
    int maxPalindromesAfterOperations(vector<string>& words) {
        long long freq[26] = {0};
        for (const string& w : words) {
            for (char c : w) freq[c - 'a']++;
        }
        long long totalPairs = 0;
        for (int i = 0; i < 26; ++i) totalPairs += freq[i] / 2;
        
        vector<int> lens;
        lens.reserve(words.size());
        for (const string& w : words) lens.push_back((int)w.size());
        sort(lens.begin(), lens.end());
        
        int ans = 0;
        for (int len : lens) {
            long long need = len / 2; // number of pairs required
            if (totalPairs >= need) {
                totalPairs -= need;
                ++ans;
            } else break;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxPalindromesAfterOperations(String[] words) {
        int[] freq = new int[26];
        for (String w : words) {
            for (int i = 0; i < w.length(); ++i) {
                freq[w.charAt(i) - 'a']++;
            }
        }
        long totalPairs = 0;
        for (int f : freq) {
            totalPairs += f / 2;
        }
        int n = words.length;
        int[] lens = new int[n];
        for (int i = 0; i < n; ++i) {
            lens[i] = words[i].length();
        }
        java.util.Arrays.sort(lens);
        int ans = 0;
        for (int len : lens) {
            long need = len / 2;
            if (totalPairs >= need) {
                ans++;
                totalPairs -= need;
            } else {
                break;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxPalindromesAfterOperations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter
        freq = Counter()
        for w in words:
            freq.update(w)
        total_pairs = sum(v // 2 for v in freq.values())
        lengths = sorted(len(w) for w in words)
        ans = 0
        for L in lengths:
            need = L // 2
            if total_pairs >= need:
                total_pairs -= need
                ans += 1
            else:
                break
        return ans
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        freq = Counter()
        for w in words:
            freq.update(w)
        total_pairs = sum(v // 2 for v in freq.values())
        lengths = sorted(len(w) for w in words)
        ans = 0
        for L in lengths:
            need = L // 2
            if total_pairs >= need:
                total_pairs -= need
                ans += 1
            else:
                break
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int maxPalindromesAfterOperations(char** words, int wordsSize) {
    int freq[26] = {0};
    int *lens = (int *)malloc(wordsSize * sizeof(int));
    if (!lens) return 0;
    
    for (int i = 0; i < wordsSize; ++i) {
        const char *s = words[i];
        int len = 0;
        while (s[len]) {
            freq[s[len] - 'a']++;
            len++;
        }
        lens[i] = len;
    }
    
    long long totalPairs = 0;
    for (int i = 0; i < 26; ++i) {
        totalPairs += freq[i] / 2;
    }
    
    qsort(lens, wordsSize, sizeof(int), cmp_int);
    
    int ans = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int need = lens[i] / 2;
        if (totalPairs >= need) {
            totalPairs -= need;
            ans++;
        } else {
            break;
        }
    }
    
    free(lens);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxPalindromesAfterOperations(string[] words) {
        int[] freq = new int[26];
        foreach (var w in words) {
            foreach (char c in w) {
                freq[c - 'a']++;
            }
        }

        long totalPairs = 0;
        foreach (int f in freq) {
            totalPairs += f / 2;
        }

        List<int> needs = new List<int>();
        foreach (var w in words) {
            needs.Add(w.Length / 2);
        }
        needs.Sort();

        int count = 0;
        foreach (int need in needs) {
            if (totalPairs >= need) {
                totalPairs -= need;
                count++;
            } else {
                break;
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
var maxPalindromesAfterOperations = function(words) {
    const freq = new Array(26).fill(0);
    for (const w of words) {
        for (let i = 0; i < w.length; i++) {
            freq[w.charCodeAt(i) - 97]++;
        }
    }
    let totalPairs = 0;
    for (let i = 0; i < 26; i++) {
        totalPairs += Math.floor(freq[i] / 2);
    }
    const lengths = words.map(w => w.length).sort((a, b) => a - b);
    let ans = 0;
    for (const len of lengths) {
        const need = Math.floor(len / 2);
        if (totalPairs >= need) {
            totalPairs -= need;
            ans++;
        } else break;
    }
    return ans;
};
```

## Typescript

```typescript
function maxPalindromesAfterOperations(words: string[]): number {
    const freq = new Array(26).fill(0);
    for (const w of words) {
        for (let i = 0; i < w.length; ++i) {
            freq[w.charCodeAt(i) - 97]++;
        }
    }
    let totalPairs = 0;
    for (let c = 0; c < 26; ++c) {
        totalPairs += Math.floor(freq[c] / 2);
    }
    const lens = words.map(w => w.length).sort((a, b) => a - b);
    let ans = 0;
    for (const len of lens) {
        const need = Math.floor(len / 2);
        if (totalPairs >= need) {
            totalPairs -= need;
            ++ans;
        } else break;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maxPalindromesAfterOperations($words) {
        // Count frequency of each letter across all words
        $freq = array_fill(0, 26, 0);
        foreach ($words as $w) {
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $idx = ord($w[$i]) - 97;
                if ($idx >= 0 && $idx < 26) {
                    $freq[$idx]++;
                }
            }
        }

        // Total number of available matching pairs
        $totalPairs = 0;
        foreach ($freq as $f) {
            $totalPairs += intdiv($f, 2);
        }

        // Required pairs for each word to become a palindrome
        $needs = [];
        foreach ($words as $w) {
            $needs[] = intdiv(strlen($w), 2);
        }
        sort($needs);

        $ans = 0;
        foreach ($needs as $need) {
            if ($totalPairs >= $need) {
                $totalPairs -= $need;
                $ans++;
            } else {
                break;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxPalindromesAfterOperations(_ words: [String]) -> Int {
        var freq = Array(repeating: 0, count: 26)
        var lengths = [Int]()
        
        for w in words {
            lengths.append(w.count)
            for b in w.utf8 {
                let idx = Int(b) - 97
                if idx >= 0 && idx < 26 {
                    freq[idx] += 1
                }
            }
        }
        
        var totalPairs = 0
        for cnt in freq {
            totalPairs += cnt / 2
        }
        
        lengths.sort()
        var result = 0
        
        for len in lengths {
            let need = len / 2
            if totalPairs >= need {
                totalPairs -= need
                result += 1
            } else {
                break
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPalindromesAfterOperations(words: Array<String>): Int {
        val freq = IntArray(26)
        for (w in words) {
            for (c in w) {
                freq[c - 'a']++
            }
        }
        var totalPairs = 0
        for (cnt in freq) {
            totalPairs += cnt / 2
        }
        val lengths = IntArray(words.size) { i -> words[i].length }
        lengths.sort()
        var ans = 0
        for (len in lengths) {
            val need = len / 2
            if (totalPairs >= need) {
                ans++
                totalPairs -= need
            } else break
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxPalindromesAfterOperations(List<String> words) {
    List<int> freq = List.filled(26, 0);
    for (var w in words) {
      for (int i = 0; i < w.length; i++) {
        freq[w.codeUnitAt(i) - 97]++;
      }
    }
    int pairs = 0;
    for (int f in freq) {
      pairs += f ~/ 2;
    }

    List<int> lengths = words.map((w) => w.length).toList();
    lengths.sort();

    int count = 0;
    for (int len in lengths) {
      int need = len ~/ 2;
      if (pairs >= need) {
        pairs -= need;
        count++;
      } else {
        break;
      }
    }
    return count;
  }
}
```

## Golang

```go
func maxPalindromesAfterOperations(words []string) int {
    var freq [26]int
    lengths := make([]int, len(words))
    for i, w := range words {
        lengths[i] = len(w)
        for _, c := range w {
            freq[c-'a']++
        }
    }
    totalPairs := 0
    for _, f := range freq {
        totalPairs += f / 2
    }
    sort.Ints(lengths)
    ans := 0
    for _, l := range lengths {
        need := l / 2
        if totalPairs >= need {
            totalPairs -= need
            ans++
        } else {
            break
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_palindromes_after_operations(words)
  freq = Array.new(26, 0)
  words.each do |w|
    w.each_byte { |b| freq[b - 97] += 1 }
  end

  total_pairs = freq.reduce(0) { |sum, cnt| sum + cnt / 2 }

  lengths = words.map(&:length).sort
  count = 0

  lengths.each do |len|
    need = len / 2
    break if total_pairs < need
    total_pairs -= need
    count += 1
  end

  count
end
```

## Scala

```scala
object Solution {
    def maxPalindromesAfterOperations(words: Array[String]): Int = {
        val freq = new Array[Int](26)
        for (w <- words) {
            for (ch <- w) {
                freq(ch - 'a') += 1
            }
        }
        var totalPairs = 0
        for (c <- freq) totalPairs += c / 2

        val lengths = words.map(_.length).sorted
        var count = 0
        var pairs = totalPairs

        for (len <- lengths) {
            val need = len / 2
            if (pairs >= need) {
                pairs -= need
                count += 1
            } else {
                return count
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_palindromes_after_operations(words: Vec<String>) -> i32 {
        let mut freq = [0i32; 26];
        for w in &words {
            for &b in w.as_bytes() {
                freq[(b - b'a') as usize] += 1;
            }
        }
        let total_pairs: i32 = freq.iter().map(|&c| c / 2).sum();

        let mut needs: Vec<i32> = words.iter().map(|w| (w.len() / 2) as i32).collect();
        needs.sort_unstable();

        let mut used = 0i32;
        let mut ans = 0i32;
        for &p in &needs {
            if used + p <= total_pairs {
                used += p;
                ans += 1;
            } else {
                break;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-palindromes-after-operations words)
  (-> (listof string?) exact-integer?)
  (let* ([freq (make-vector 26 0)]
         [add-char
          (lambda (c)
            (let* ([idx (- (char->integer c) (char->integer #\a))])
              (vector-set! freq idx (+ 1 (vector-ref freq idx)))))]
         [_ (for-each
             (lambda (s)
               (for ([i (in-range (string-length s))])
                 (add-char (string-ref s i))))
             words)]
         [total-pairs
          (let loop ((i 0) (sum 0))
            (if (= i 26)
                sum
                (loop (+ i 1) (+ sum (quotient (vector-ref freq i) 2)))))]
         [sorted-lens (sort (map string-length words) <)])
    (let loop ((ls sorted-lens) (pairs total-pairs) (cnt 0))
      (if (null? ls)
          cnt
          (let* ([len (car ls)]
                 [need (quotient len 2)])
            (if (>= pairs need)
                (loop (cdr ls) (- pairs need) (+ cnt 1))
                cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([max_palindromes_after_operations/1]).

-spec max_palindromes_after_operations(Words :: [unicode:unicode_binary()]) -> integer().
max_palindromes_after_operations(Words) ->
    %% Count frequencies of each letter a-z
    EmptyFreq = lists:duplicate(26, 0),
    Freq = lists:foldl(
        fun(Bin, Acc) ->
            lists:foldl(
                fun(Char, A) ->
                    Index = Char - $a,
                    Old = element(Index + 1, A),
                    setelement(Index + 1, A, Old + 1)
                end,
                Acc,
                binary_to_list(Bin))
        end,
        EmptyFreq,
        Words),

    %% Total number of available pairs
    TotalPairs = lists:foldl(
        fun(N, Sum) -> Sum + N div 2 end,
        0,
        tuple_to_list(list_to_tuple(Freq))),

    %% Sort word lengths ascending
    Lengths = [byte_size(W) || W <- Words],
    SortedLengths = lists:sort(Lengths),

    %% Greedily form palindromes using available pairs
    make_palindromes(SortedLengths, TotalPairs, 0).

make_palindromes([], _Pairs, Count) ->
    Count;
make_palindromes([L | Rest], Pairs, Count) ->
    Need = L div 2,
    if
        Pairs >= Need ->
            make_palindromes(Rest, Pairs - Need, Count + 1);
        true ->
            Count
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_palindromes_after_operations(words :: [String.t]) :: integer
  def max_palindromes_after_operations(words) do
    freq =
      Enum.reduce(words, %{}, fn word, acc ->
        String.graphemes(word)
        |> Enum.reduce(acc, fn ch, map -> Map.update(map, ch, 1, &(&1 + 1)) end)
      end)

    total_pairs = Enum.reduce(freq, 0, fn {_ch, cnt}, sum -> sum + div(cnt, 2) end)

    sorted_lengths =
      words
      |> Enum.map(&String.length/1)
      |> Enum.sort()

    {ans, _} =
      Enum.reduce_while(sorted_lengths, {0, total_pairs}, fn len, {cnt, pairs_left} ->
        need = div(len, 2)

        if pairs_left >= need do
          {:cont, {cnt + 1, pairs_left - need}}
        else
          {:halt, {cnt, pairs_left}}
        end
      end)

    ans
  end
end
```
