# 2901. Longest Unequal Adjacent Groups Subsequence II

## Cpp

```cpp
class Solution {
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = words.size();
        vector<int> dp(n, 1), pre(n, -1);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (groups[i] == groups[j]) continue;
                if (words[i].size() != words[j].size()) continue;
                int diff = 0;
                const string &a = words[i], &b = words[j];
                for (size_t k = 0; k < a.size(); ++k) {
                    if (a[k] != b[k]) {
                        ++diff;
                        if (diff > 1) break;
                    }
                }
                if (diff == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    pre[i] = j;
                }
            }
        }
        int bestIdx = 0;
        for (int i = 1; i < n; ++i) {
            if (dp[i] > dp[bestIdx]) bestIdx = i;
        }
        vector<string> res;
        for (int cur = bestIdx; cur != -1; cur = pre[cur]) {
            res.push_back(words[cur]);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        int[] dp = new int[n];
        int[] prev = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] == groups[j]) continue;
                if (words[i].length() != words[j].length()) continue;

                int diff = 0;
                String wi = words[i];
                String wj = words[j];
                for (int k = 0; k < wi.length(); k++) {
                    if (wi.charAt(k) != wj.charAt(k)) {
                        diff++;
                        if (diff > 1) break;
                    }
                }
                if (diff == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }

        int maxIdx = 0;
        for (int i = 1; i < n; i++) {
            if (dp[i] > dp[maxIdx]) {
                maxIdx = i;
            }
        }

        List<String> result = new ArrayList<>();
        for (int cur = maxIdx; cur != -1; cur = prev[cur]) {
            result.add(words[cur]);
        }
        Collections.reverse(result);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            wi = words[i]
            li = len(wi)
            gi = groups[i]
            for j in range(i):
                if groups[j] == gi:
                    continue
                if len(words[j]) != li:
                    continue
                # compute hamming distance, stop early if >1
                diff = 0
                wj = words[j]
                for a, b in zip(wi, wj):
                    if a != b:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # find index with maximum dp value
        max_idx = 0
        for i in range(1, n):
            if dp[i] > dp[max_idx]:
                max_idx = i

        # reconstruct sequence
        res = []
        cur = max_idx
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]
        res.reverse()
        return res
```

## Python3

```python
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            wi = words[i]
            li = len(wi)
            gi = groups[i]
            for j in range(i):
                if groups[j] == gi:
                    continue
                if len(words[j]) != li:
                    continue
                # compute hamming distance, stop early if >1
                diff = 0
                wj = words[j]
                for a, b in zip(wi, wj):
                    if a != b:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # find index with maximum dp value
        max_idx = 0
        for i in range(1, n):
            if dp[i] > dp[max_idx]:
                max_idx = i

        # reconstruct subsequence
        res = []
        cur = max_idx
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]
        res.reverse()
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getWordsInLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    int n = wordsSize;
    int *dp = (int*)malloc(sizeof(int) * n);
    int *prev = (int*)malloc(sizeof(int) * n);
    
    int maxLen = 0, maxIdx = -1;
    for (int i = 0; i < n; ++i) {
        dp[i] = 1;
        prev[i] = -1;
        int len_i = strlen(words[i]);
        for (int j = 0; j < i; ++j) {
            if (groups[i] == groups[j]) continue;
            if ((int)strlen(words[j]) != len_i) continue;
            
            // compute Hamming distance, stop early if >1
            int diff = 0;
            const char *a = words[i];
            const char *b = words[j];
            while (*a) {
                if (*a != *b) {
                    ++diff;
                    if (diff > 1) break;
                }
                ++a; ++b;
            }
            if (diff == 1 && dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > maxLen) {
            maxLen = dp[i];
            maxIdx = i;
        }
    }
    
    char **ans = (char**)malloc(sizeof(char*) * maxLen);
    int pos = maxLen - 1;
    int cur = maxIdx;
    while (cur != -1) {
        ans[pos] = words[cur];
        --pos;
        cur = prev[cur];
    }
    
    *returnSize = maxLen;
    free(dp);
    free(prev);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> GetWordsInLongestSubsequence(string[] words, int[] groups)
    {
        int n = words.Length;
        int[] dp = new int[n];
        int[] prev = new int[n];
        for (int i = 0; i < n; i++)
        {
            dp[i] = 1;
            prev[i] = -1;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (groups[i] == groups[j]) continue;
                if (words[i].Length != words[j].Length) continue;

                int diff = 0;
                string a = words[i];
                string b = words[j];
                for (int k = 0; k < a.Length && diff <= 1; k++)
                {
                    if (a[k] != b[k]) diff++;
                }
                if (diff != 1) continue;

                if (dp[j] + 1 > dp[i])
                {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }

        int maxIdx = 0;
        for (int i = 1; i < n; i++)
        {
            if (dp[i] > dp[maxIdx]) maxIdx = i;
        }

        List<string> result = new List<string>();
        int cur = maxIdx;
        while (cur != -1)
        {
            result.Add(words[cur]);
            cur = prev[cur];
        }
        result.Reverse();
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getWordsInLongestSubsequence = function(words, groups) {
    const n = words.length;
    const dp = new Array(n).fill(1);
    const prev = new Array(n).fill(-1);

    const hammingOne = (a, b) => {
        let diff = 0;
        for (let i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) {
                diff++;
                if (diff > 1) return false;
            }
        }
        return diff === 1;
    };

    for (let i = 0; i < n; i++) {
        const wi = words[i];
        const leni = wi.length;
        for (let j = 0; j < i; j++) {
            if (groups[i] === groups[j]) continue;
            if (words[j].length !== leni) continue;
            if (!hammingOne(wi, words[j])) continue;

            if (dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
    }

    // find index with maximum dp value
    let maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (dp[i] > dp[maxIdx]) maxIdx = i;
    }

    const result = [];
    let cur = maxIdx;
    while (cur !== -1) {
        result.push(words[cur]);
        cur = prev[cur];
    }
    result.reverse();
    return result;
};
```

## Typescript

```typescript
function getWordsInLongestSubsequence(words: string[], groups: number[]): string[] {
    const n = words.length;
    const dp = new Array<number>(n).fill(1);
    const prev = new Array<number>(n).fill(-1);
    const lens = words.map(w => w.length);

    function isHammingOne(a: string, b: string): boolean {
        let diff = 0;
        for (let i = 0; i < a.length && diff <= 1; i++) {
            if (a[i] !== b[i]) diff++;
        }
        return diff === 1;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (groups[i] === groups[j]) continue;
            if (lens[i] !== lens[j]) continue;
            if (!isHammingOne(words[i], words[j])) continue;
            if (dp[j] + 1 > dp[i]) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
    }

    let maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (dp[i] > dp[maxIdx]) maxIdx = i;
    }

    const result: string[] = [];
    let cur = maxIdx;
    while (cur !== -1) {
        result.push(words[cur]);
        cur = prev[cur];
    }
    result.reverse();
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer[] $groups
     * @return String[]
     */
    function getWordsInLongestSubsequence($words, $groups) {
        $n = count($words);
        if ($n == 0) return [];

        $dp = array_fill(0, $n, 1);      // length of longest subsequence ending at i
        $prev = array_fill(0, $n, -1);   // previous index in that subsequence

        $maxLen = 1;
        $maxIdx = 0;

        for ($i = 0; $i < $n; ++$i) {
            $lenI = strlen($words[$i]);
            for ($j = 0; $j < $i; ++$j) {
                if ($groups[$i] == $groups[$j]) continue;
                if (strlen($words[$j]) != $lenI) continue;

                // compute hamming distance, stop early if >1
                $diff = 0;
                for ($k = 0; $k < $lenI; ++$k) {
                    if ($words[$i][$k] !== $words[$j][$k]) {
                        ++$diff;
                        if ($diff > 1) break;
                    }
                }
                if ($diff == 1 && $dp[$j] + 1 > $dp[$i]) {
                    $dp[$i] = $dp[$j] + 1;
                    $prev[$i] = $j;
                }
            }

            if ($dp[$i] > $maxLen) {
                $maxLen = $dp[$i];
                $maxIdx = $i;
            }
        }

        // reconstruct answer
        $res = [];
        $cur = $maxIdx;
        while ($cur != -1) {
            $res[] = $words[$cur];
            $cur = $prev[$cur];
        }
        $res = array_reverse($res);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func getWordsInLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        let n = words.count
        // Precompute UTF8 byte arrays for fast character comparison
        var wordBytes = [[UInt8]]()
        wordBytes.reserveCapacity(n)
        for w in words {
            wordBytes.append(Array(w.utf8))
        }
        
        var dp = Array(repeating: 1, count: n)
        var prev = Array(repeating: -1, count: n)
        var bestIdx = 0
        
        for i in 0..<n {
            for j in 0..<i {
                if groups[i] == groups[j] { continue }
                if wordBytes[i].count != wordBytes[j].count { continue }
                
                // Compute Hamming distance, stop early if >1
                var diff = 0
                let len = wordBytes[i].count
                for k in 0..<len {
                    if wordBytes[i][k] != wordBytes[j][k] {
                        diff += 1
                        if diff > 1 { break }
                    }
                }
                
                if diff == 1 && dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1
                    prev[i] = j
                }
            }
            if dp[i] > dp[bestIdx] {
                bestIdx = i
            }
        }
        
        // Reconstruct the subsequence
        var result = [String]()
        var cur = bestIdx
        while cur != -1 {
            result.append(words[cur])
            cur = prev[cur]
        }
        return Array(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getWordsInLongestSubsequence(words: Array<String>, groups: IntArray): List<String> {
        val n = words.size
        val dp = IntArray(n) { 1 }
        val prev = IntArray(n) { -1 }
        var bestIdx = 0
        for (i in 0 until n) {
            for (j in 0 until i) {
                if (groups[i] == groups[j]) continue
                if (words[i].length != words[j].length) continue
                if (!isHammingOne(words[i], words[j])) continue
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1
                    prev[i] = j
                }
            }
            if (dp[i] > dp[bestIdx]) bestIdx = i
        }
        val result = mutableListOf<String>()
        var idx = bestIdx
        while (idx != -1) {
            result.add(words[idx])
            idx = prev[idx]
        }
        result.reverse()
        return result
    }

    private fun isHammingOne(a: String, b: String): Boolean {
        var diff = 0
        for (i in a.indices) {
            if (a[i] != b[i]) {
                diff++
                if (diff > 1) return false
            }
        }
        return diff == 1
    }
}
```

## Dart

```dart
class Solution {
  List<String> getWordsInLongestSubsequence(List<String> words, List<int> groups) {
    int n = words.length;
    List<int> dp = List.filled(n, 1);
    List<int> prev = List.filled(n, -1);

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (groups[i] == groups[j]) continue;
        if (words[i].length != words[j].length) continue;

        int diff = 0;
        String wi = words[i];
        String wj = words[j];
        for (int k = 0; k < wi.length; k++) {
          if (wi.codeUnitAt(k) != wj.codeUnitAt(k)) {
            diff++;
            if (diff > 1) break;
          }
        }
        if (diff == 1 && dp[j] + 1 > dp[i]) {
          dp[i] = dp[j] + 1;
          prev[i] = j;
        }
      }
    }

    int maxIdx = 0;
    for (int i = 1; i < n; i++) {
      if (dp[i] > dp[maxIdx]) maxIdx = i;
    }

    List<String> result = [];
    int cur = maxIdx;
    while (cur != -1) {
      result.add(words[cur]);
      cur = prev[cur];
    }
    return result.reversed.toList();
  }
}
```

## Golang

```go
func getWordsInLongestSubsequence(words []string, groups []int) []string {
	n := len(words)
	if n == 0 {
		return []string{}
	}
	dp := make([]int, n)
	prev := make([]int, n)
	for i := range dp {
		dp[i] = 1
		prev[i] = -1
	}

	hamming := func(a, b string) int {
		diff := 0
		for k := 0; k < len(a); k++ {
			if a[k] != b[k] {
				diff++
				if diff > 1 {
					return diff
				}
			}
		}
		return diff
	}

	maxLen, maxIdx := 1, 0
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if groups[i] == groups[j] {
				continue
			}
			if len(words[i]) != len(words[j]) {
				continue
			}
			if hamming(words[i], words[j]) == 1 && dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
				prev[i] = j
			}
		}
		if dp[i] > maxLen {
			maxLen = dp[i]
			maxIdx = i
		}
	}

	// reconstruct sequence
	res := make([]string, 0, maxLen)
	for cur := maxIdx; cur != -1; cur = prev[cur] {
		res = append(res, words[cur])
	}
	// reverse
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}
```

## Ruby

```ruby
# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_words_in_longest_subsequence(words, groups)
  n = words.length
  dp = Array.new(n, 1)
  prev = Array.new(n, -1)

  # helper to check if hamming distance is exactly 1
  hamming_one = lambda do |s, t|
    diff = 0
    s.length.times do |i|
      if s[i] != t[i]
        diff += 1
        return false if diff > 1
      end
    end
    diff == 1
  end

  (0...n).each do |i|
    (0...i).each do |j|
      next if groups[i] == groups[j]
      next unless words[i].length == words[j].length
      next unless hamming_one.call(words[i], words[j])
      if dp[j] + 1 > dp[i]
        dp[i] = dp[j] + 1
        prev[i] = j
      end
    end
  end

  max_len = dp.max
  idx = dp.index(max_len)

  result = []
  while idx != -1
    result << words[idx]
    idx = prev[idx]
  end
  result.reverse
end
```

## Scala

```scala
object Solution {
    def getWordsInLongestSubsequence(words: Array[String], groups: Array[Int]): List[String] = {
        val n = words.length
        val dp = Array.fill(n)(1)
        val prev = Array.fill(n)(-1)

        def hammingOne(a: String, b: String): Boolean = {
            var diff = 0
            var i = 0
            while (i < a.length && diff <= 1) {
                if (a.charAt(i) != b.charAt(i)) diff += 1
                i += 1
            }
            diff == 1
        }

        for (i <- 0 until n) {
            var j = 0
            while (j < i) {
                if (groups(i) != groups(j) &&
                    words(i).length == words(j).length &&
                    hammingOne(words(i), words(j))) {
                    val cand = dp(j) + 1
                    if (cand > dp(i)) {
                        dp(i) = cand
                        prev(i) = j
                    }
                }
                j += 1
            }
        }

        var maxIdx = 0
        for (i <- 1 until n) {
            if (dp(i) > dp(maxIdx)) maxIdx = i
        }

        val res = scala.collection.mutable.ListBuffer[String]()
        var cur = maxIdx
        while (cur != -1) {
            res += words(cur)
            cur = prev(cur)
        }
        res.reverse.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = words.len();
        if n == 0 {
            return vec![];
        }
        // dp[i]: length of longest valid subsequence ending at i
        let mut dp = vec![1usize; n];
        // prev[i]: previous index in that subsequence, None for start
        let mut prev: Vec<Option<usize>> = vec![None; n];

        // Helper to check hamming distance == 1 (lengths are equal)
        fn is_hamming_one(a: &str, b: &str) -> bool {
            let mut diff = 0;
            for (c1, c2) in a.bytes().zip(b.bytes()) {
                if c1 != c2 {
                    diff += 1;
                    if diff > 1 {
                        return false;
                    }
                }
            }
            diff == 1
        }

        for i in 0..n {
            for j in 0..i {
                if groups[i] != groups[j] && words[i].len() == words[j].len()
                    && is_hamming_one(&words[i], &words[j])
                {
                    if dp[j] + 1 > dp[i] {
                        dp[i] = dp[j] + 1;
                        prev[i] = Some(j);
                    }
                }
            }
        }

        // Find index with maximum dp value
        let mut max_idx = 0usize;
        for i in 1..n {
            if dp[i] > dp[max_idx] {
                max_idx = i;
            }
        }

        // Reconstruct the subsequence
        let mut result: Vec<String> = Vec::with_capacity(dp[max_idx]);
        let mut cur = max_idx;
        loop {
            result.push(words[cur].clone());
            if let Some(p) = prev[cur] {
                cur = p;
            } else {
                break;
            }
        }
        result.reverse();
        result
    }
}
```

## Racket

```racket
(define (hamming-one? s t)
  (let ([len (string-length s)])
    (let loop ((i 0) (diff 0))
      (cond [(> diff 1) #f]
            [(= i len) (= diff 1)]
            [else (loop (+ i 1)
                        (if (char=? (string-ref s i) (string-ref t i))
                            diff
                            (+ diff 1)))]))))

(define/contract (get-words-in-longest-subsequence words groups)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  (let* ([n (length words)]
         [wvec (list->vector words)]
         [gvec (list->vector groups)]
         [dp (make-vector n 1)]
         [prev (make-vector n -1)])
    (for ([i (in-range n)])
      (for ([j (in-range i)])
        (when (and (not (= (vector-ref gvec i) (vector-ref gvec j)))
                   (= (string-length (vector-ref wvec i))
                      (string-length (vector-ref wvec j)))
                   (hamming-one? (vector-ref wvec i) (vector-ref wvec j)))
          (let ([cand (+ (vector-ref dp j) 1)])
            (when (> cand (vector-ref dp i))
              (vector-set! dp i cand)
              (vector-set! prev i j))))))
    (define max-idx 0)
    (for ([i (in-range n)])
      (when (> (vector-ref dp i) (vector-ref dp max-idx))
        (set! max-idx i)))
    (let loop ((idx max-idx) (acc '()))
      (if (= idx -1)
          (reverse acc)
          (loop (vector-ref prev idx) (cons (vector-ref wvec idx) acc))))))
```

## Erlang

```erlang
-module(solution).
-export([get_words_in_longest_subsequence/2]).

-spec get_words_in_longest_subsequence(Words :: [unicode:unicode_binary()], Groups :: [integer()]) -> [unicode:unicode_binary()].
get_words_in_longest_subsequence(Words, Groups) ->
    N = length(Words),
    WordsT = list_to_tuple(Words),
    GroupsT = list_to_tuple(Groups),
    DP0 = erlang:make_tuple(N, 1),
    Prev0 = erlang:make_tuple(N, -1),
    {_DPFinal, PrevFinal, MaxIdx} = loop_i(0, N, WordsT, GroupsT, DP0, Prev0, 1, 0),
    build_sequence(MaxIdx, PrevFinal, WordsT).

loop_i(I, N, _WordsT, _GroupsT, DP, Prev, MaxLen, MaxIdx) when I == N ->
    {DP, Prev, MaxIdx};
loop_i(I, N, WordsT, GroupsT, DP, Prev, MaxLen, MaxIdx) ->
    Wi = element(I + 1, WordsT),
    Gi = element(I + 1, GroupsT),
    LenWi = byte_size(Wi),
    {BestLen, BestPrev} = inner_loop_j(0, I - 1, Wi, Gi, LenWi, DP, WordsT, GroupsT, 1, -1),
    DP2 = setelement(I + 1, DP, BestLen),
    Prev2 = setelement(I + 1, Prev, BestPrev),
    {NewMaxLen, NewMaxIdx} =
        if
            BestLen > MaxLen -> {BestLen, I};
            true -> {MaxLen, MaxIdx}
        end,
    loop_i(I + 1, N, WordsT, GroupsT, DP2, Prev2, NewMaxLen, NewMaxIdx).

inner_loop_j(J, EndJ, _Wi, _Gi, _LenWi, _DP, _WordsT, _GroupsT, BestLen, BestPrev) when J > EndJ ->
    {BestLen, BestPrev};
inner_loop_j(J, EndJ, Wi, Gi, LenWi, DP, WordsT, GroupsT, BestLen, BestPrev) ->
    Gj = element(J + 1, GroupsT),
    case Gj =/= Gi of
        true ->
            Wj = element(J + 1, WordsT),
            if byte_size(Wj) == LenWi,
               hamming_distance(Wi, Wj) == 1 ->
                    Dj = element(J + 1, DP),
                    Cand = Dj + 1,
                    if Cand > BestLen ->
                            inner_loop_j(J + 1, EndJ, Wi, Gi, LenWi, DP, WordsT, GroupsT, Cand, J);
                       true ->
                            inner_loop_j(J + 1, EndJ, Wi, Gi, LenWi, DP, WordsT, GroupsT, BestLen, BestPrev)
                    end;
               true ->
                    inner_loop_j(J + 1, EndJ, Wi, Gi, LenWi, DP, WordsT, GroupsT, BestLen, BestPrev)
            end;
        false ->
            inner_loop_j(J + 1, EndJ, Wi, Gi, LenWi, DP, WordsT, GroupsT, BestLen, BestPrev)
    end.

hamming_distance(Bin1, Bin2) when byte_size(Bin1) =:= byte_size(Bin2) ->
    hamming_distance(Bin1, Bin2, 0).

hamming_distance(<<C1, Rest1/binary>>, <<C2, Rest2/binary>>, Acc) ->
    NewAcc = if C1 =/= C2 -> Acc + 1; true -> Acc end,
    hamming_distance(Rest1, Rest2, NewAcc);
hamming_distance(<<>>, <<>>, Acc) -> Acc.

build_sequence(Index, PrevT, WordsT) ->
    collect(Index, PrevT, WordsT, []).

collect(-1, _PrevT, _WordsT, Acc) ->
    lists:reverse(Acc);
collect(Index, PrevT, WordsT, Acc) ->
    Word = element(Index + 1, WordsT),
    PrevIdx = element(Index + 1, PrevT),
    collect(PrevIdx, PrevT, WordsT, [Word | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_words_in_longest_subsequence(words :: [String.t()], groups :: [integer]) :: [String.t()]
  def get_words_in_longest_subsequence(words, groups) do
    n = length(words)
    words_t = List.to_tuple(words)
    groups_t = List.to_tuple(groups)

    # precompute byte lists for fast hamming distance checks
    bytes_list = Enum.map(words, &:binary.bin_to_list/1)
    bytes_t = List.to_tuple(bytes_list)

    {dp, prev, max_idx, _max_len} =
      Enum.reduce(0..(n - 1), {%{}, %{}, 0, 1}, fn i,
                                                   {dp_acc, prev_acc, cur_max_idx,
                                                    cur_max_len} ->
        wi = elem(words_t, i)
        gi = elem(groups_t, i)

        {best_len, best_prev} =
          if i == 0 do
            {1, -1}
          else
            Enum.reduce(0..(i - 1), {1, -1}, fn j,
                                             {bl, bp} ->
              gj = elem(groups_t, j)

              cond do
                gj == gi ->
                  {bl, bp}

                true ->
                  # check length equality first
                  if byte_size(wi) != byte_size(elem(words_t, j)) do
                    {bl, bp}
                  else
                    if hamming_one_bytes?(
                         elem(bytes_t, i),
                         elem(bytes_t, j)
                       ) do
                      len = Map.get(dp_acc, j) + 1

                      if len > bl do
                        {len, j}
                      else
                        {bl, bp}
                      end
                    else
                      {bl, bp}
                    end
                  end
              end
            end)
          end

        dp_new = Map.put(dp_acc, i, best_len)
        prev_new = Map.put(prev_acc, i, best_prev)

        if best_len > cur_max_len do
          {dp_new, prev_new, i, best_len}
        else
          {dp_new, prev_new, cur_max_idx, cur_max_len}
        end
      end)

    # reconstruct answer
    reconstruct(max_idx, prev, words_t, [])
  end

  defp hamming_one_bytes?(list1, list2) do
    diff =
      Enum.zip(list1, list2)
      |> Enum.reduce(0, fn {a, b}, acc ->
        if a == b, do: acc, else: acc + 1
      end)

    diff == 1
  end

  defp reconstruct(-1, _prev, _words_t, acc), do: Enum.reverse(acc)

  defp reconstruct(idx, prev, words_t, acc) do
    word = elem(words_t, idx)
    next_idx = Map.get(prev, idx, -1)
    reconstruct(next_idx, prev, words_t, [word | acc])
  end
end
```
