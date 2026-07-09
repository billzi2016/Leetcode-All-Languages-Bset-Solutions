# 1170. Compare Strings by Frequency of the Smallest Character

## Cpp

```cpp
class Solution {
public:
    int freq(const string& s) {
        char mn = 'z' + 1;
        int cnt = 0;
        for (char c : s) {
            if (c < mn) {
                mn = c;
                cnt = 1;
            } else if (c == mn) {
                ++cnt;
            }
        }
        return cnt;
    }

    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        vector<int> wfreq;
        wfreq.reserve(words.size());
        for (const string& w : words) {
            wfreq.push_back(freq(w));
        }
        sort(wfreq.begin(), wfreq.end());

        vector<int> ans;
        ans.reserve(queries.size());
        int n = wfreq.size();
        for (const string& q : queries) {
            int p = freq(q);
            auto it = upper_bound(wfreq.begin(), wfreq.end(), p);
            ans.push_back(n - static_cast<int>(it - wfreq.begin()));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        int n = words.length;
        int[] wFreq = new int[n];
        for (int i = 0; i < n; i++) {
            wFreq[i] = freq(words[i]);
        }
        java.util.Arrays.sort(wFreq);
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int qFreq = freq(queries[i]);
            int idx = upperBound(wFreq, qFreq);
            ans[i] = n - idx;
        }
        return ans;
    }

    private int freq(String s) {
        char minChar = 'z' + 1;
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c < minChar) {
                minChar = c;
                count = 1;
            } else if (c == minChar) {
                count++;
            }
        }
        return count;
    }

    private int upperBound(int[] arr, int target) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (arr[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        import bisect

        def freq(s):
            m = min(s)
            return s.count(m)

        word_freqs = [freq(w) for w in words]
        word_freqs.sort()
        n = len(word_freqs)

        result = []
        for q in queries:
            p = freq(q)
            idx = bisect.bisect_right(word_freqs, p)
            result.append(n - idx)
        return result
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            smallest = min(s)
            return s.count(smallest)

        word_counts = [f(w) for w in words]
        word_counts.sort()
        n = len(word_counts)
        result = []
        for q in queries:
            p = f(q)
            idx = bisect.bisect_right(word_counts, p)
            result.append(n - idx)
        return result
```

## C

```c
#include <stdlib.h>

/* Helper: compute f(s) */
static int freq(const char *s) {
    int cnt[26] = {0};
    while (*s) {
        cnt[*s - 'a']++;
        s++;
    }
    for (int i = 0; i < 26; ++i) {
        if (cnt[i]) return cnt[i];
    }
    return 0;
}

/* qsort comparator */
static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numSmallerByFrequency(char** queries, int queriesSize,
                           char** words, int wordsSize,
                           int* returnSize) {
    /* frequencies of words */
    int *wFreq = (int *)malloc(wordsSize * sizeof(int));
    for (int i = 0; i < wordsSize; ++i) {
        wFreq[i] = freq(words[i]);
    }
    qsort(wFreq, wordsSize, sizeof(int), cmp_int);

    int *ans = (int *)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int p = freq(queries[i]);

        /* binary search first element > p */
        int l = 0, r = wordsSize;
        while (l < r) {
            int m = (l + r) >> 1;
            if (wFreq[m] <= p)
                l = m + 1;
            else
                r = m;
        }
        ans[i] = wordsSize - l;
    }

    free(wFreq);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private int FrequencyOfSmallestChar(string s)
    {
        int[] cnt = new int[26];
        foreach (char c in s)
        {
            cnt[c - 'a']++;
        }
        for (int i = 0; i < 26; i++)
        {
            if (cnt[i] > 0) return cnt[i];
        }
        return 0;
    }

    public int[] NumSmallerByFrequency(string[] queries, string[] words)
    {
        int n = words.Length;
        int[] wordFreq = new int[n];
        for (int i = 0; i < n; i++)
        {
            wordFreq[i] = FrequencyOfSmallestChar(words[i]);
        }
        Array.Sort(wordFreq);

        int q = queries.Length;
        int[] answer = new int[q];
        for (int i = 0; i < q; i++)
        {
            int p = FrequencyOfSmallestChar(queries[i]);

            // upper bound: first index with value > p
            int left = 0, right = n;
            while (left < right)
            {
                int mid = (left + right) >> 1;
                if (wordFreq[mid] <= p)
                    left = mid + 1;
                else
                    right = mid;
            }
            answer[i] = n - left;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} queries
 * @param {string[]} words
 * @return {number[]}
 */
var numSmallerByFrequency = function(queries, words) {
    const getFreq = (s) => {
        let minChar = 'z';
        for (let ch of s) {
            if (ch < minChar) minChar = ch;
        }
        let cnt = 0;
        for (let ch of s) {
            if (ch === minChar) cnt++;
        }
        return cnt;
    };
    
    const wordFreqs = words.map(getFreq).sort((a, b) => a - b);
    const n = wordFreqs.length;
    
    const upperBound = (arr, target) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo; // first index with value > target
    };
    
    const result = [];
    for (let q of queries) {
        const fq = getFreq(q);
        const idx = upperBound(wordFreqs, fq);
        result.push(n - idx);
    }
    return result;
};
```

## Typescript

```typescript
function numSmallerByFrequency(queries: string[], words: string[]): number[] {
    const getFreq = (s: string): number => {
        let minChar = 'z';
        for (const ch of s) {
            if (ch < minChar) minChar = ch;
        }
        let cnt = 0;
        for (const ch of s) {
            if (ch === minChar) cnt++;
        }
        return cnt;
    };

    const wordFreqs: number[] = words.map(getFreq);
    wordFreqs.sort((a, b) => a - b);

    const upperBound = (arr: number[], target: number): number => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    const result: number[] = [];
    for (const q of queries) {
        const p = getFreq(q);
        const idx = upperBound(wordFreqs, p);
        result.push(wordFreqs.length - idx);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String[] $words
     * @return Integer[]
     */
    function numSmallerByFrequency($queries, $words) {
        // Helper to compute f(s)
        $freq = function(string $s): int {
            $minChar = null;
            $count = 0;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $c = $s[$i];
                if ($minChar === null || $c < $minChar) {
                    $minChar = $c;
                    $count = 1;
                } elseif ($c === $minChar) {
                    $count++;
                }
            }
            return $count;
        };

        // Compute frequencies for words and sort
        $wFreqs = [];
        foreach ($words as $w) {
            $wFreqs[] = $freq($w);
        }
        sort($wFreqs, SORT_NUMERIC);

        $nWords = count($wFreqs);
        $answers = [];

        // For each query, binary search first index > p
        foreach ($queries as $q) {
            $p = $freq($q);
            $left = 0;
            $right = $nWords; // exclusive

            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($wFreqs[$mid] <= $p) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }

            $answers[] = $nWords - $left;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func numSmallerByFrequency(_ queries: [String], _ words: [String]) -> [Int] {
        func freq(_ s: String) -> Int {
            var minByte = UInt8.max
            var count = 0
            for b in s.utf8 {
                if b < minByte {
                    minByte = b
                    count = 1
                } else if b == minByte {
                    count += 1
                }
            }
            return count
        }
        
        let wordFreqs = words.map { freq($0) }.sorted()
        var result: [Int] = []
        for q in queries {
            let p = freq(q)
            // upper bound: first index with value > p
            var left = 0
            var right = wordFreqs.count
            while left < right {
                let mid = (left + right) >> 1
                if wordFreqs[mid] <= p {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            result.append(wordFreqs.count - left)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSmallerByFrequency(queries: Array<String>, words: Array<String>): IntArray {
        val wordFreq = IntArray(words.size)
        for (i in words.indices) {
            wordFreq[i] = freq(words[i])
        }
        wordFreq.sort()
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val p = freq(queries[i])
            var l = 0
            var r = wordFreq.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (wordFreq[m] <= p) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            ans[i] = wordFreq.size - l
        }
        return ans
    }

    private fun freq(s: String): Int {
        var minChar = s[0]
        var cnt = 1
        for (i in 1 until s.length) {
            val ch = s[i]
            if (ch < minChar) {
                minChar = ch
                cnt = 1
            } else if (ch == minChar) {
                cnt++
            }
        }
        return cnt
    }
}
```

## Dart

```dart
class Solution {
  List<int> numSmallerByFrequency(List<String> queries, List<String> words) {
    int _freq(String s) {
      int minChar = 123; // 'z' + 1
      for (int i = 0; i < s.length; i++) {
        int code = s.codeUnitAt(i);
        if (code < minChar) minChar = code;
      }
      int count = 0;
      for (int i = 0; i < s.length; i++) {
        if (s.codeUnitAt(i) == minChar) count++;
      }
      return count;
    }

    List<int> wordFreq = words.map(_freq).toList();
    wordFreq.sort();

    List<int> answer = [];
    for (String q in queries) {
      int p = _freq(q);
      int left = 0, right = wordFreq.length;
      while (left < right) {
        int mid = (left + right) >> 1;
        if (wordFreq[mid] <= p) {
          left = mid + 1;
        } else {
          right = mid;
        }
      }
      answer.add(wordFreq.length - left);
    }
    return answer;
  }
}
```

## Golang

```go
import "sort"

func numSmallerByFrequency(queries []string, words []string) []int {
	wf := make([]int, len(words))
	for i, w := range words {
		wf[i] = freq(w)
	}
	sort.Ints(wf)

	n := len(wf)
	ans := make([]int, len(queries))
	for i, q := range queries {
		p := freq(q)
		idx := sort.Search(n, func(j int) bool { return wf[j] > p })
		ans[i] = n - idx
	}
	return ans
}

func freq(s string) int {
	if len(s) == 0 {
		return 0
	}
	minChar := s[0]
	cnt := 1
	for i := 1; i < len(s); i++ {
		c := s[i]
		if c < minChar {
			minChar = c
			cnt = 1
		} else if c == minChar {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def f(s)
  min_c = s.each_byte.min
  cnt = 0
  s.each_byte { |b| cnt += 1 if b == min_c }
  cnt
end

# @param {String[]} queries
# @param {String[]} words
# @return {Integer[]}
def num_smaller_by_frequency(queries, words)
  word_freqs = words.map { |w| f(w) }.sort
  n = word_freqs.length
  queries.map do |q|
    p = f(q)
    idx = word_freqs.bsearch_index { |x| x > p } || n
    n - idx
  end
end
```

## Scala

```scala
object Solution {
    def numSmallerByFrequency(queries: Array[String], words: Array[String]): Array[Int] = {
        def f(s: String): Int = {
            var minChar = 'z' + 1
            var cnt = 0
            for (c <- s) {
                if (c < minChar) {
                    minChar = c
                    cnt = 1
                } else if (c == minChar) {
                    cnt += 1
                }
            }
            cnt
        }

        val wordFreqs = words.map(f).sorted
        val n = wordFreqs.length

        queries.map { q =>
            val p = f(q)
            var idx = java.util.Arrays.binarySearch(wordFreqs, p + 1)
            if (idx < 0) idx = -idx - 1
            n - idx
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_smaller_by_frequency(queries: Vec<String>, words: Vec<String>) -> Vec<i32> {
        fn freq(s: &str) -> i32 {
            let bytes = s.as_bytes();
            let mut min_c = b'{' ; // character after 'z'
            for &b in bytes {
                if b < min_c {
                    min_c = b;
                }
            }
            let mut cnt = 0;
            for &b in bytes {
                if b == min_c {
                    cnt += 1;
                }
            }
            cnt as i32
        }

        fn upper_bound(arr: &[i32], target: i32) -> usize {
            let mut lo = 0usize;
            let mut hi = arr.len();
            while lo < hi {
                let mid = (lo + hi) / 2;
                if arr[mid] <= target {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lo
        }

        let mut word_counts: Vec<i32> = words.iter().map(|w| freq(w)).collect();
        word_counts.sort_unstable();

        let total = word_counts.len();
        queries
            .iter()
            .map(|q| {
                let p = freq(q);
                let idx = upper_bound(&word_counts, p);
                (total - idx) as i32
            })
            .collect()
    }
}
```

## Racket

```racket
(define (freq s)
  (let ((len (string-length s)))
    (if (= len 0) 
        0
        (let* ((first (string-ref s 0))
               (count (let-values ([(minc cnt)
                                    (for/fold ([minc first] [cnt 1])
                                              ([i (in-range 1 len)])
                                      (let ((ch (string-ref s i)))
                                        (cond [(char<? ch minc) (values ch 1)]
                                              [(char=? ch minc) (values minc (+ cnt 1))]
                                              [else (values minc cnt)])))])
                         cnt)))
          count))))

(define/contract (num-smaller-by-frequency queries words)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  (let* ((word-freqs (map freq words))
         (sorted-vec (list->vector (sort word-freqs <))))
    (define (upper-bound v target)
      (let loop ((lo 0) (hi (vector-length v)))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (> (vector-ref v mid) target)
                  (loop lo mid)
                  (loop (add1 mid) hi))))))
    (map (lambda (q)
           (let* ((p (freq q))
                  (idx (upper-bound sorted-vec p)))
             (- (vector-length sorted-vec) idx)))
         queries)))
```

## Erlang

```erlang
-spec num_smaller_by_frequency([unicode:unicode_binary()], [unicode:unicode_binary()]) -> [integer()].
num_smaller_by_frequency(Queries, Words) ->
    WordFreqs = [freq_smallest(W) || W <- Words],
    Sorted = lists:sort(WordFreqs),
    [count_greater(Sorted, freq_smallest(Q)) || Q <- Queries].

freq_smallest(Bin) ->
    List = binary_to_list(Bin),
    MinChar = lists:min(List),
    length([C || C <- List, C == MinChar]).

count_greater(Sorted, P) ->
    Len = length(Sorted),
    FirstIdx = first_greater_idx(Sorted, P, 0, Len - 1),
    Len - FirstIdx.

first_greater_idx(_List, _P, Low, High) when Low > High ->
    Low;
first_greater_idx(List, P, Low, High) ->
    Mid = (Low + High) div 2,
    Val = lists:nth(Mid + 1, List),
    if
        Val =< P -> first_greater_idx(List, P, Mid + 1, High);
        true -> first_greater_idx(List, P, Low, Mid - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_smaller_by_frequency(queries :: [String.t()], words :: [String.t()]) :: [integer()]
  def num_smaller_by_frequency(queries, words) do
    word_freqs = Enum.map(words, &freq_of_smallest/1) |> Enum.sort()
    total = length(word_freqs)

    Enum.map(queries, fn q ->
      p = freq_of_smallest(q)
      idx = upper_bound(word_freqs, p)
      total - idx
    end)
  end

  defp freq_of_smallest(s) do
    chars = String.to_charlist(s)
    min_char = Enum.min(chars)
    Enum.count(chars, fn c -> c == min_char end)
  end

  defp upper_bound(arr, target) do
    ub(arr, target, 0, length(arr))
  end

  defp ub(_arr, _target, low, high) when low >= high, do: low

  defp ub(arr, target, low, high) do
    mid = div(low + high, 2)

    if Enum.at(arr, mid) <= target do
      ub(arr, target, mid + 1, high)
    else
      ub(arr, target, low, mid)
    end
  end
end
```
