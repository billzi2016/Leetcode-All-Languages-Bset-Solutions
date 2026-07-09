# 0916. Word Subsets

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        int bmax[26] = {0};
        for (const string& w : words2) {
            int cnt[26] = {0};
            for (char c : w) ++cnt[c - 'a'];
            for (int i = 0; i < 26; ++i) bmax[i] = max(bmax[i], cnt[i]);
        }
        
        vector<string> ans;
        for (const string& w : words1) {
            int cnt[26] = {0};
            for (char c : w) ++cnt[c - 'a'];
            bool ok = true;
            for (int i = 0; i < 26; ++i) {
                if (cnt[i] < bmax[i]) { ok = false; break; }
            }
            if (ok) ans.push_back(w);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] need = new int[26];
        // compute maximum required frequency for each letter from words2
        for (String b : words2) {
            int[] cnt = count(b);
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > need[i]) need[i] = cnt[i];
            }
        }

        List<String> ans = new ArrayList<>();
        // filter words1
        for (String a : words1) {
            int[] cntA = count(a);
            boolean ok = true;
            for (int i = 0; i < 26; i++) {
                if (cntA[i] < need[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) ans.add(a);
        }
        return ans;
    }

    private int[] count(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # maximum required frequency for each letter across all words in words2
        need = [0] * 26
        for b in words2:
            cnt = [0] * 26
            for ch in b:
                idx = ord(ch) - 97
                cnt[idx] += 1
            for i in range(26):
                if cnt[i] > need[i]:
                    need[i] = cnt[i]

        ans = []
        for a in words1:
            cnt_a = [0] * 26
            for ch in a:
                idx = ord(ch) - 97
                cnt_a[idx] += 1
            # check if a satisfies all needed counts
            ok = True
            for i in range(26):
                if cnt_a[i] < need[i]:
                    ok = False
                    break
            if ok:
                ans.append(a)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # maximum required frequency for each letter across all words in words2
        bmax = [0] * 26
        for b in words2:
            cnt = [0] * 26
            for ch in b:
                cnt[ord(ch) - 97] += 1
            for i in range(26):
                if cnt[i] > bmax[i]:
                    bmax[i] = cnt[i]

        ans = []
        for a in words1:
            cnt_a = [0] * 26
            for ch in a:
                cnt_a[ord(ch) - 97] += 1
            # check if a satisfies all required frequencies
            for i in range(26):
                if cnt_a[i] < bmax[i]:
                    break
            else:
                ans.append(a)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** wordSubsets(char** words1, int words1Size, char** words2, int words2Size, int* returnSize) {
    int bmax[26] = {0};
    int cnt[26];
    
    // Compute maximum required frequencies from words2
    for (int i = 0; i < words2Size; ++i) {
        memset(cnt, 0, sizeof(cnt));
        const char *s = words2[i];
        while (*s) {
            cnt[*s - 'a']++;
            s++;
        }
        for (int j = 0; j < 26; ++j) {
            if (cnt[j] > bmax[j]) bmax[j] = cnt[j];
        }
    }
    
    char **result = (char **)malloc(words1Size * sizeof(char *));
    int idx = 0;
    
    // Check each word in words1 against the required frequencies
    for (int i = 0; i < words1Size; ++i) {
        memset(cnt, 0, sizeof(cnt));
        const char *s = words1[i];
        while (*s) {
            cnt[*s - 'a']++;
            s++;
        }
        int ok = 1;
        for (int j = 0; j < 26; ++j) {
            if (cnt[j] < bmax[j]) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            result[idx++] = words1[i];
        }
    }
    
    *returnSize = idx;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private int[] GetCount(string s)
    {
        var cnt = new int[26];
        foreach (char c in s)
        {
            cnt[c - 'a']++;
        }
        return cnt;
    }

    public IList<string> WordSubsets(string[] words1, string[] words2)
    {
        var required = new int[26];
        foreach (var b in words2)
        {
            var cntB = GetCount(b);
            for (int i = 0; i < 26; i++)
            {
                if (cntB[i] > required[i])
                    required[i] = cntB[i];
            }
        }

        var result = new List<string>();
        foreach (var a in words1)
        {
            var cntA = GetCount(a);
            bool ok = true;
            for (int i = 0; i < 26; i++)
            {
                if (cntA[i] < required[i])
                {
                    ok = false;
                    break;
                }
            }
            if (ok) result.Add(a);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {string[]}
 */
var wordSubsets = function(words1, words2) {
    const need = new Array(26).fill(0);
    
    // helper to count letters in a string
    const getCount = (s) => {
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < s.length; ++i) {
            cnt[s.charCodeAt(i) - 97]++;
        }
        return cnt;
    };
    
    // compute maximum required frequency for each letter across words2
    for (const b of words2) {
        const cntB = getCount(b);
        for (let i = 0; i < 26; ++i) {
            if (cntB[i] > need[i]) need[i] = cntB[i];
        }
    }
    
    const result = [];
    // filter words1
    outer: for (const a of words1) {
        const cntA = getCount(a);
        for (let i = 0; i < 26; ++i) {
            if (cntA[i] < need[i]) continue outer;
        }
        result.push(a);
    }
    
    return result;
};
```

## Typescript

```typescript
function wordSubsets(words1: string[], words2: string[]): string[] {
    const maxFreq = new Array(26).fill(0);
    const base = 'a'.charCodeAt(0);

    for (const b of words2) {
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < b.length; ++i) {
            cnt[b.charCodeAt(i) - base]++;
        }
        for (let i = 0; i < 26; ++i) {
            if (cnt[i] > maxFreq[i]) maxFreq[i] = cnt[i];
        }
    }

    const result: string[] = [];
    outer: for (const a of words1) {
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < a.length; ++i) {
            cnt[a.charCodeAt(i) - base]++;
        }
        for (let i = 0; i < 26; ++i) {
            if (cnt[i] < maxFreq[i]) continue outer;
        }
        result.push(a);
    }

    return result;
};
```

## Php

```php
class Solution {
    /**
     * @param String[] $words1
     * @param String[] $words2
     * @return String[]
     */
    function wordSubsets($words1, $words2) {
        // maximum required frequency for each letter across all words2
        $need = array_fill(0, 26, 0);
        foreach ($words2 as $b) {
            $cnt = $this->charCount($b);
            for ($i = 0; $i < 26; ++$i) {
                if ($cnt[$i] > $need[$i]) {
                    $need[$i] = $cnt[$i];
                }
            }
        }

        $result = [];
        foreach ($words1 as $a) {
            $cntA = $this->charCount($a);
            $ok = true;
            for ($i = 0; $i < 26; ++$i) {
                if ($cntA[$i] < $need[$i]) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                $result[] = $a;
            }
        }

        return $result;
    }

    /**
     * @param string $s
     * @return int[]
     */
    private function charCount($s) {
        $cnt = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; ++$i) {
            $idx = ord($s[$i]) - ord('a');
            if ($idx >= 0 && $idx < 26) {
                $cnt[$idx]++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func wordSubsets(_ words1: [String], _ words2: [String]) -> [String] {
        var bmax = Array(repeating: 0, count: 26)
        
        for w in words2 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w.utf8 {
                let idx = Int(c - 97)
                cnt[idx] += 1
            }
            for i in 0..<26 {
                if cnt[i] > bmax[i] {
                    bmax[i] = cnt[i]
                }
            }
        }
        
        var result: [String] = []
        for w in words1 {
            var cnt = Array(repeating: 0, count: 26)
            for c in w.utf8 {
                let idx = Int(c - 97)
                cnt[idx] += 1
            }
            var ok = true
            for i in 0..<26 {
                if cnt[i] < bmax[i] {
                    ok = false
                    break
                }
            }
            if ok {
                result.append(w)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wordSubsets(words1: Array<String>, words2: Array<String>): List<String> {
        val required = IntArray(26)
        for (b in words2) {
            val cnt = IntArray(26)
            for (c in b) {
                cnt[c - 'a']++
            }
            for (i in 0 until 26) {
                if (cnt[i] > required[i]) required[i] = cnt[i]
            }
        }

        val result = mutableListOf<String>()
        outer@ for (a in words1) {
            val cnt = IntArray(26)
            for (c in a) {
                cnt[c - 'a']++
            }
            for (i in 0 until 26) {
                if (cnt[i] < required[i]) continue@outer
            }
            result.add(a)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> wordSubsets(List<String> words1, List<String> words2) {
    // Helper to count character frequencies
    List<int> _count(String s) {
      var cnt = List.filled(26, 0);
      for (int i = 0; i < s.length; i++) {
        cnt[s.codeUnitAt(i) - 97]++;
      }
      return cnt;
    }

    // Maximum required frequencies from words2
    var need = List.filled(26, 0);
    for (var b in words2) {
      var cur = _count(b);
      for (int i = 0; i < 26; i++) {
        if (cur[i] > need[i]) need[i] = cur[i];
      }
    }

    // Filter universal strings from words1
    List<String> ans = [];
    outer:
    for (var a in words1) {
      var cntA = _count(a);
      for (int i = 0; i < 26; i++) {
        if (cntA[i] < need[i]) continue outer;
      }
      ans.add(a);
    }

    return ans;
  }
}
```

## Golang

```go
func wordSubsets(words1 []string, words2 []string) []string {
	getCount := func(s string) [26]int {
		var cnt [26]int
		for i := 0; i < len(s); i++ {
			cnt[s[i]-'a']++
		}
		return cnt
	}

	var maxCnt [26]int
	for _, b := range words2 {
		c := getCount(b)
		for i := 0; i < 26; i++ {
			if c[i] > maxCnt[i] {
				maxCnt[i] = c[i]
			}
		}
	}

	var res []string
	for _, a := range words1 {
		c := getCount(a)
		ok := true
		for i := 0; i < 26; i++ {
			if c[i] < maxCnt[i] {
				ok = false
				break
			}
		}
		if ok {
			res = append(res, a)
		}
	}
	return res
}
```

## Ruby

```ruby
# @param {String[]} words1
# @param {String[]} words2
# @return {String[]}
def word_subsets(words1, words2)
  # Helper to count character frequencies in a string
  count = lambda do |s|
    freq = Array.new(26, 0)
    s.each_byte { |b| freq[b - 97] += 1 }
    freq
  end

  # Maximum required frequency for each letter across all words2
  bmax = Array.new(26, 0)
  words2.each do |w|
    cw = count.call(w)
    26.times { |i| bmax[i] = [bmax[i], cw[i]].max }
  end

  result = []
  words1.each do |w|
    cw = count.call(w)
    universal = true
    26.times do |i|
      if cw[i] < bmax[i]
        universal = false
        break
      end
    end
    result << w if universal
  end

  result
end
```

## Scala

```scala
object Solution {
    def wordSubsets(words1: Array[String], words2: Array[String]): List[String] = {
        def count(s: String): Array[Int] = {
            val cnt = new Array[Int](26)
            s.foreach(c => cnt(c - 'a') += 1)
            cnt
        }

        val bmax = new Array[Int](26)
        for (b <- words2) {
            val cnt = count(b)
            var i = 0
            while (i < 26) {
                if (cnt(i) > bmax(i)) bmax(i) = cnt(i)
                i += 1
            }
        }

        val result = scala.collection.mutable.ListBuffer[String]()
        for (a <- words1) {
            val cnt = count(a)
            var ok = true
            var i = 0
            while (i < 26 && ok) {
                if (cnt(i) < bmax(i)) ok = false
                i += 1
            }
            if (ok) result += a
        }

        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn word_subsets(words1: Vec<String>, words2: Vec<String>) -> Vec<String> {
        let mut bmax = [0u8; 26];
        for b in &words2 {
            let mut cnt = [0u8; 26];
            for &byte in b.as_bytes() {
                let idx = (byte - b'a') as usize;
                cnt[idx] += 1;
            }
            for i in 0..26 {
                if cnt[i] > bmax[i] {
                    bmax[i] = cnt[i];
                }
            }
        }

        let mut ans: Vec<String> = Vec::new();
        'outer: for a in &words1 {
            let mut cnt = [0u8; 26];
            for &byte in a.as_bytes() {
                let idx = (byte - b'a') as usize;
                cnt[idx] += 1;
            }
            for i in 0..26 {
                if cnt[i] < bmax[i] {
                    continue 'outer;
                }
            }
            ans.push(a.clone());
        }

        ans
    }
}
```

## Racket

```racket
(define (count s)
  (let ((v (make-vector 26 0)))
    (for ([c (in-string s)])
      (let* ((idx (- (char->integer c) (char->integer #\a))))
        (vector-set! v idx (+ 1 (vector-ref v idx)))))
    v))

(define/contract (word-subsets words1 words2)
  (-> (listof string?) (listof string?) (listof string?))
  (let ((bmax (make-vector 26 0)))
    ;; compute maximum required frequencies from words2
    (for ([b words2])
      (let ((cnt (count b)))
        (for ([i (in-range 26)])
          (when (> (vector-ref cnt i) (vector-ref bmax i))
            (vector-set! bmax i (vector-ref cnt i))))))
    ;; collect universal strings from words1
    (define res '())
    (define (satisfies? cnt)
      (for/and ([i (in-range 26)])
        (>= (vector-ref cnt i) (vector-ref bmax i))))
    (for ([a words1])
      (let ((cnt (count a)))
        (when (satisfies? cnt)
          (set! res (cons a res)))))
    (reverse res)))
```

## Erlang

```erlang
-module(solution).
-export([word_subsets/2]).

-spec word_subsets(Words1 :: [unicode:unicode_binary()], Words2 :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
word_subsets(Words1, Words2) ->
    Bmax = lists:foldl(fun(Word, Acc) ->
                C = count(Word),
                merge_max(Acc, C)
            end, erlang:make_tuple(26, 0), Words2),
    FilterFun = fun(Word) ->
        ACount = count(Word),
        is_universal(ACount, Bmax)
    end,
    lists:filter(FilterFun, Words1).

count(Bin) ->
    Count0 = erlang:make_tuple(26, 0),
    count_bytes(binary_to_list(Bin), Count0).

count_bytes([], C) -> C;
count_bytes([Char | Rest], C) ->
    Index = Char - $a + 1,
    Old = element(Index, C),
    NewC = setelement(Index, C, Old + 1),
    count_bytes(Rest, NewC).

merge_max(A, B) ->
    merge_max(1, A, B).

merge_max(I, A, B) when I =< 26 ->
    Max = max(element(I, A), element(I, B)),
    NewA = setelement(I, A, Max),
    merge_max(I + 1, NewA, B);
merge_max(_, A, _) -> A.

is_universal(A, B) ->
    is_universal(1, A, B).

is_universal(I, _, _) when I > 26 -> true;
is_universal(I, A, B) ->
    if element(I, A) >= element(I, B) ->
            is_universal(I + 1, A, B);
       true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec word_subsets(words1 :: [String.t()], words2 :: [String.t()]) :: [String.t()]
  def word_subsets(words1, words2) do
    bmax = Enum.reduce(words2, List.duplicate(0, 26), fn w, acc ->
      wf = freq(w)
      max_counts(acc, wf)
    end)

    Enum.filter(words1, fn w ->
      wf = freq(w)
      Enum.all?(0..25, fn i -> Enum.at(wf, i) >= Enum.at(bmax, i) end)
    end)
  end

  defp freq(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce(List.duplicate(0, 26), fn c, acc ->
      idx = c - ?a
      List.update_at(acc, idx, &(&1 + 1))
    end)
  end

  defp max_counts(a, b) do
    for {x, i} <- Enum.with_index(a) do
      y = Enum.at(b, i)

      if x > y, do: x, else: y
    end
  end
end
```
