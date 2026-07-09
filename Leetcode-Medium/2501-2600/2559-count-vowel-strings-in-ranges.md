# 2559. Count Vowel Strings in Ranges

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        int n = words.size();
        vector<int> pref(n);
        auto isVowel = [&](char c)->bool{
            return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        };
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            const string& w = words[i];
            if (!w.empty() && isVowel(w.front()) && isVowel(w.back())) ++cnt;
            pref[i] = cnt;
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            int res = pref[r] - (l ? pref[l-1] : 0);
            ans.push_back(res);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int n = words.length;
        boolean[] isVowelString = new boolean[n];
        for (int i = 0; i < n; i++) {
            String w = words[i];
            char first = w.charAt(0);
            char last = w.charAt(w.length() - 1);
            if (isVowel(first) && isVowel(last)) {
                isVowelString[i] = true;
            }
        }

        int[] prefix = new int[n];
        for (int i = 0; i < n; i++) {
            prefix[i] = (i > 0 ? prefix[i - 1] : 0) + (isVowelString[i] ? 1 : 0);
        }

        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            ans[i] = prefix[r] - (l > 0 ? prefix[l - 1] : 0);
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = set('aeiou')
        n = len(words)
        pref = [0] * n
        cnt = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                cnt += 1
            pref[i] = cnt

        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(pref[r])
            else:
                ans.append(pref[r] - pref[l - 1])
        return ans
```

## Python3

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)
        prefix = [0] * n
        cnt = 0
        for i, w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                cnt += 1
            prefix[i] = cnt

        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] - prefix[l - 1])
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int isVowelChar(char c) {
    return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* vowelStrings(char** words, int wordsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize; // unused, each query has 2 columns
    
    int *pref = (int*)malloc(wordsSize * sizeof(int));
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        int len = strlen(w);
        int add = 0;
        if (len > 0 && isVowelChar(w[0]) && isVowelChar(w[len-1]))
            add = 1;
        pref[i] = (i ? pref[i-1] : 0) + add;
    }
    
    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        int cnt = pref[r] - (l > 0 ? pref[l-1] : 0);
        ans[i] = cnt;
    }
    
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] VowelStrings(string[] words, int[][] queries) {
        int n = words.Length;
        int[] prefix = new int[n];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            string w = words[i];
            if (IsVowel(w[0]) && IsVowel(w[w.Length - 1])) cnt++;
            prefix[i] = cnt;
        }

        int q = queries.Length;
        int[] ans = new int[q];
        for (int i = 0; i < q; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            ans[i] = prefix[r] - (l > 0 ? prefix[l - 1] : 0);
        }
        return ans;
    }

    private bool IsVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function(words, queries) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const n = words.length;
    const prefix = new Array(n);
    let cnt = 0;
    for (let i = 0; i < n; ++i) {
        const w = words[i];
        if (vowels.has(w[0]) && vowels.has(w[w.length - 1])) {
            ++cnt;
        }
        prefix[i] = cnt;
    }

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [l, r] = queries[i];
        if (l === 0) {
            ans[i] = prefix[r];
        } else {
            ans[i] = prefix[r] - prefix[l - 1];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function vowelStrings(words: string[], queries: number[][]): number[] {
    const n = words.length;
    const pref = new Array<number>(n);
    let cnt = 0;
    const isVowel = (ch: string) => ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    for (let i = 0; i < n; i++) {
        const w = words[i];
        if (isVowel(w[0]) && isVowel(w[w.length - 1])) cnt++;
        pref[i] = cnt;
    }
    const ans = new Array<number>(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [l, r] = queries[i];
        ans[i] = pref[r] - (l > 0 ? pref[l - 1] : 0);
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function vowelStrings($words, $queries) {
        $vowels = ['a'=>1,'e'=>1,'i'=>1,'o'=>1,'u'=>1];
        $n = count($words);
        $prefix = [];
        $cnt = 0;
        for ($i = 0; $i < $n; $i++) {
            $w = $words[$i];
            $first = $w[0];
            $last = $w[strlen($w) - 1];
            if (isset($vowels[$first]) && isset($vowels[$last])) {
                $cnt++;
            }
            $prefix[$i] = $cnt;
        }
        $ans = [];
        foreach ($queries as $q) {
            [$l, $r] = $q;
            if ($l == 0) {
                $ans[] = $prefix[$r];
            } else {
                $ans[] = $prefix[$r] - $prefix[$l - 1];
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func vowelStrings(_ words: [String], _ queries: [[Int]]) -> [Int] {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        var prefix = [Int](repeating: 0, count: words.count)
        var cnt = 0
        for i in 0..<words.count {
            let w = words[i]
            if let first = w.first, let last = w.last,
               vowels.contains(first) && vowels.contains(last) {
                cnt += 1
            }
            prefix[i] = cnt
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let l = q[0]
            let r = q[1]
            if l == 0 {
                result.append(prefix[r])
            } else {
                result.append(prefix[r] - prefix[l - 1])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun vowelStrings(words: Array<String>, queries: Array<IntArray>): IntArray {
        val n = words.size
        val prefix = IntArray(n)
        var count = 0
        for (i in 0 until n) {
            val w = words[i]
            if (isVowel(w.first()) && isVowel(w.last())) {
                count++
            }
            prefix[i] = count
        }
        val q = queries.size
        val ans = IntArray(q)
        for (i in 0 until q) {
            val l = queries[i][0]
            val r = queries[i][1]
            ans[i] = if (l == 0) prefix[r] else prefix[r] - prefix[l - 1]
        }
        return ans
    }

    private fun isVowel(c: Char): Boolean {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }
}
```

## Dart

```dart
class Solution {
  List<int> vowelStrings(List<String> words, List<List<int>> queries) {
    int n = words.length;
    List<int> prefix = List.filled(n, 0);
    int count = 0;

    bool isVowel(int c) {
      return c == 97 || c == 101 || c == 105 || c == 111 || c == 117; // a e i o u
    }

    for (int i = 0; i < n; i++) {
      String w = words[i];
      if (w.isNotEmpty) {
        int first = w.codeUnitAt(0);
        int last = w.codeUnitAt(w.length - 1);
        if (isVowel(first) && isVowel(last)) {
          count++;
        }
      }
      prefix[i] = count;
    }

    List<int> ans = [];
    for (var q in queries) {
      int l = q[0];
      int r = q[1];
      int total = prefix[r] - (l > 0 ? prefix[l - 1] : 0);
      ans.add(total);
    }
    return ans;
  }
}
```

## Golang

```go
func vowelStrings(words []string, queries [][]int) []int {
	isVowel := func(c byte) bool {
		switch c {
		case 'a', 'e', 'i', 'o', 'u':
			return true
		}
		return false
	}

	n := len(words)
	prefix := make([]int, n)
	count := 0
	for i, w := range words {
		if len(w) > 0 && isVowel(w[0]) && isVowel(w[len(w)-1]) {
			count++
		}
		prefix[i] = count
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		if l == 0 {
			ans[i] = prefix[r]
		} else {
			ans[i] = prefix[r] - prefix[l-1]
		}
	}
	return ans
}
```

## Ruby

```ruby
def vowel_strings(words, queries)
  vowels = "aeiou"
  n = words.length
  prefix = Array.new(n, 0)
  count = 0
  words.each_with_index do |w, i|
    if vowels.include?(w[0]) && vowels.include?(w[-1])
      count += 1
    end
    prefix[i] = count
  end

  result = []
  queries.each do |l, r|
    if l == 0
      result << prefix[r]
    else
      result << prefix[r] - prefix[l - 1]
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def vowelStrings(words: Array[String], queries: Array[Array[Int]]): Array[Int] = {
        val n = words.length
        val prefix = new Array[Int](n)
        var cnt = 0
        for (i <- 0 until n) {
            val w = words(i)
            if (isVowel(w.head) && isVowel(w.last)) cnt += 1
            prefix(i) = cnt
        }
        val m = queries.length
        val ans = new Array[Int](m)
        for (i <- 0 until m) {
            val l = queries(i)(0)
            val r = queries(i)(1)
            ans(i) = if (l == 0) prefix(r) else prefix(r) - prefix(l - 1)
        }
        ans
    }

    private def isVowel(c: Char): Boolean = {
        c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }
}
```

## Rust

```rust
impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        fn is_vowel(b: u8) -> bool {
            matches!(b, b'a' | b'e' | b'i' | b'o' | b'u')
        }

        let n = words.len();
        let mut prefix = vec![0i32; n];
        let mut cnt = 0i32;
        for (i, w) in words.iter().enumerate() {
            let bytes = w.as_bytes();
            if is_vowel(bytes[0]) && is_vowel(*bytes.last().unwrap()) {
                cnt += 1;
            }
            prefix[i] = cnt;
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let res = if l == 0 { prefix[r] } else { prefix[r] - prefix[l - 1] };
            ans.push(res);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (vowel-strings words queries)
  (-> (listof string?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length words)]
         [pref (make-vector n)])
    (let loop ((i 0) (sum 0))
      (if (= i n)
          (void)
          (let* ([s (list-ref words i)]
                 [len (string-length s)]
                 [first (and (> len 0) (string-ref s 0))]
                 [last (and (> len 0) (string-ref s (- len 1)))]
                 [is-vowel (and first last
                                (or (char=? first #\a) (char=? first #\e) (char=? first #\i) (char=? first #\o) (char=? first #\u))
                                (or (char=? last #\a) (char=? last #\e) (char=? last #\i) (char=? last #\o) (char=? last #\u)))])
            (let ((new-sum (+ sum (if is-vowel 1 0))))
              (vector-set! pref i new-sum)
              (loop (+ i 1) new-sum)))))
    (map (lambda (qr)
           (let* ([l (first qr)]
                  [r (second qr)])
             (if (= l 0)
                 (vector-ref pref r)
                 (- (vector-ref pref r) (vector-ref pref (- l 1))))))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([vowel_strings/2]).

-spec vowel_strings(Words :: [unicode:unicode_binary()], Queries :: [[integer()]]) -> [integer()].
vowel_strings(Words, Queries) ->
    {_, RevPrefix} = lists:foldl(
        fun(Word, {Sum, Acc}) ->
            IsVowel = is_vowel_word(Word),
            NewSum = Sum + (if IsVowel -> 1; true -> 0 end),
            {NewSum, [NewSum | Acc]}
        end,
        {0, []},
        Words
    ),
    PrefixList = lists:reverse(RevPrefix),
    PrefixTuple = list_to_tuple(PrefixList),
    [ answer(L, R, PrefixTuple) || [L, R] <- Queries ].

answer(L, R, PrefixTuple) ->
    RVal = element(R + 1, PrefixTuple),
    LMinus1Val = case L of
        0 -> 0;
        _ -> element(L, PrefixTuple)
    end,
    RVal - LMinus1Val.

is_vowel_word(Word) ->
    Size = byte_size(Word),
    if
        Size == 0 -> false;
        true ->
            First = binary:at(Word, 0),
            Last = binary:at(Word, Size - 1),
            is_vowel(First) andalso is_vowel(Last)
    end.

is_vowel(C) when C == $a; C == $e; C == $i; C == $o; C == $u -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec vowel_strings(words :: [String.t()], queries :: [[integer]]) :: [integer]
  def vowel_strings(words, queries) do
    prefix = build_prefix(words)

    Enum.map(queries, fn [l, r] ->
      right = :erlang.element(r + 1, prefix)
      left = if l == 0, do: 0, else: :erlang.element(l, prefix)
      right - left
    end)
  end

  defp build_prefix(words) do
    {_, list} =
      Enum.reduce(words, {0, []}, fn w, {sum, acc} ->
        new_sum = if vowel_word?(w), do: sum + 1, else: sum
        {new_sum, [new_sum | acc]}
      end)

    list
    |> Enum.reverse()
    |> List.to_tuple()
  end

  defp vowel_word?(word) do
    first = :binary.first(word)
    last = :binary.last(word)
    is_vowel(first) and is_vowel(last)
  end

  defp is_vowel(c) when c in [?a, ?e, ?i, ?o, ?u], do: true
  defp is_vowel(_), do: false
end
```
