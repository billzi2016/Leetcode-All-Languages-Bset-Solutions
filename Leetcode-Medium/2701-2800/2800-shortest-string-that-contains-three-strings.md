# 2800. Shortest String That Contains Three Strings

## Cpp

```cpp
class Solution {
public:
    string mergeStrings(const string& x, const string& y) {
        if (x.find(y) != string::npos) return x;
        if (y.find(x) != string::npos) return y;
        int maxOverlap = 0;
        int limit = min((int)x.size(), (int)y.size());
        for (int k = limit; k >= 1; --k) {
            if (x.compare(x.size() - k, k, y, 0, k) == 0) {
                maxOverlap = k;
                break;
            }
        }
        return x + y.substr(maxOverlap);
    }

    string minimumString(string a, string b, string c) {
        vector<string> arr = {a, b, c};
        vector<int> idx = {0, 1, 2};
        string best;
        bool first = true;
        sort(idx.begin(), idx.end());
        do {
            string cur = mergeStrings(arr[idx[0]], arr[idx[1]]);
            cur = mergeStrings(cur, arr[idx[2]]);
            if (first || cur.size() < best.size() || (cur.size() == best.size() && cur < best)) {
                best = cur;
                first = false;
            }
        } while (next_permutation(idx.begin(), idx.end()));
        return best;
    }
};
```

## Java

```java
class Solution {
    public String minimumString(String a, String b, String c) {
        String[] arr = {a, b, c};
        int[][] perms = {
            {0, 1, 2},
            {0, 2, 1},
            {1, 0, 2},
            {1, 2, 0},
            {2, 0, 1},
            {2, 1, 0}
        };
        String best = null;
        for (int[] p : perms) {
            String s = merge(merge(arr[p[0]], arr[p[1]]), arr[p[2]]);
            if (best == null ||
                s.length() < best.length() ||
                (s.length() == best.length() && s.compareTo(best) < 0)) {
                best = s;
            }
        }
        return best;
    }

    private String merge(String s1, String s2) {
        if (s1.contains(s2)) {
            return s1;
        }
        int maxOverlap = 0;
        int limit = Math.min(s1.length(), s2.length());
        for (int k = limit; k > 0; k--) {
            if (s1.regionMatches(s1.length() - k, s2, 0, k)) {
                maxOverlap = k;
                break;
            }
        }
        return s1 + s2.substring(maxOverlap);
    }
}
```

## Python

```python
class Solution(object):
    def minimumString(self, a, b, c):
        """
        :type a: str
        :type b: str
        :type c: str
        :rtype: str
        """
        from itertools import permutations

        def merge(s1, s2):
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2
            max_ov = 0
            limit = min(len(s1), len(s2))
            for k in range(1, limit + 1):
                if s1[-k:] == s2[:k]:
                    max_ov = k
            return s1 + s2[max_ov:]

        best = None
        for p in permutations([a, b, c]):
            cur = merge(merge(p[0], p[1]), p[2])
            if best is None or len(cur) < len(best) or (len(cur) == len(best) and cur < best):
                best = cur
        return best
```

## Python3

```python
import itertools

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def combine(s: str, t: str) -> str:
            if t in s:
                return s
            if s in t:
                return t
            max_k = 0
            limit = min(len(s), len(t))
            for k in range(limit, 0, -1):
                if s[-k:] == t[:k]:
                    max_k = k
                    break
            return s + t[max_k:]

        best = None
        for p in itertools.permutations([a, b, c]):
            cur = p[0]
            cur = combine(cur, p[1])
            cur = combine(cur, p[2])
            if best is None or len(cur) < len(best) or (len(cur) == len(best) and cur < best):
                best = cur
        return best
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static bool contains(const string& big, const string& small) {
    return big.find(small) != string::npos;
}

static string mergeStrings(const string& cur, const string& nxt) {
    if (contains(cur, nxt)) return cur;
    int maxOverlap = 0;
    int limit = min((int)cur.size(), (int)nxt.size());
    for (int k = limit; k > 0; --k) {
        if (cur.compare(cur.size() - k, k, nxt, 0, k) == 0) {
            maxOverlap = k;
            break;
        }
    }
    return cur + nxt.substr(maxOverlap);
}

char* minimumString(char* a, char* b, char* c) {
    vector<string> s = {string(a), string(b), string(c)};
    array<int,3> perm = {0,1,2};
    string best;
    do {
        string cur = s[perm[0]];
        cur = mergeStrings(cur, s[perm[1]]);
        cur = mergeStrings(cur, s[perm[2]]);
        if (best.empty() || cur.size() < best.size() ||
            (cur.size() == best.size() && cur < best)) {
            best = cur;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    
    char* ret = (char*)malloc(best.size() + 1);
    memcpy(ret, best.c_str(), best.size() + 1);
    return ret;
}
```

## Csharp

```csharp
public class Solution {
    public string MinimumString(string a, string b, string c) {
        string[] strs = new string[] { a, b, c };
        int[][] perms = new int[][] {
            new int[]{0,1,2},
            new int[]{0,2,1},
            new int[]{1,0,2},
            new int[]{1,2,0},
            new int[]{2,0,1},
            new int[]{2,1,0}
        };
        
        string best = null;
        int bestLen = int.MaxValue;
        
        foreach (var p in perms) {
            string cur = strs[p[0]];
            cur = Merge(cur, strs[p[1]]);
            cur = Merge(cur, strs[p[2]]);
            
            if (cur.Length < bestLen || (cur.Length == bestLen && string.CompareOrdinal(cur, best) < 0)) {
                best = cur;
                bestLen = cur.Length;
            }
        }
        
        return best;
    }
    
    private string Merge(string s, string t) {
        if (s.Contains(t)) return s;
        int maxOverlap = 0;
        int limit = Math.Min(s.Length, t.Length);
        for (int k = limit; k >= 1; k--) {
            if (s.Substring(s.Length - k) == t.Substring(0, k)) {
                maxOverlap = k;
                break;
            }
        }
        return s + t.Substring(maxOverlap);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @param {string} c
 * @return {string}
 */
var minimumString = function(a, b, c) {
    const strs = [a, b, c];
    
    // merge two strings into the shortest superstring (lexicographically smallest if tie)
    const merge = (x, y) => {
        if (x.includes(y)) return x;
        if (y.includes(x)) return y;
        let maxOverlap = 0;
        const limit = Math.min(x.length, y.length);
        for (let k = limit; k > 0; --k) {
            if (x.slice(x.length - k) === y.slice(0, k)) {
                maxOverlap = k;
                break;
            }
        }
        return x + y.slice(maxOverlap);
    };
    
    let best = null;
    for (let i = 0; i < 3; ++i) {
        for (let j = 0; j < 3; ++j) if (j !== i) {
            for (let k = 0; k < 3; ++k) if (k !== i && k !== j) {
                let cur = merge(strs[i], strs[j]);
                cur = merge(cur, strs[k]);
                if (
                    best === null ||
                    cur.length < best.length ||
                    (cur.length === best.length && cur < best)
                ) {
                    best = cur;
                }
            }
        }
    }
    return best;
};
```

## Typescript

```typescript
function minimumString(a: string, b: string, c: string): string {
    const merge = (s: string, t: string): string => {
        if (s.includes(t)) return s;
        if (t.includes(s)) return t;
        let maxOverlap = 0;
        const limit = Math.min(s.length, t.length);
        for (let k = limit; k > 0; --k) {
            if (s.slice(s.length - k) === t.slice(0, k)) {
                maxOverlap = k;
                break;
            }
        }
        return s + t.slice(maxOverlap);
    };

    const perms: string[][] = [
        [a, b, c],
        [a, c, b],
        [b, a, c],
        [b, c, a],
        [c, a, b],
        [c, b, a],
    ];

    let best = "";
    for (const p of perms) {
        let cur = merge(p[0], p[1]);
        cur = merge(cur, p[2]);
        if (
            best === "" ||
            cur.length < best.length ||
            (cur.length === best.length && cur < best)
        ) {
            best = cur;
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @param String $c
     * @return String
     */
    function minimumString($a, $b, $c) {
        $perms = [
            [$a, $b, $c],
            [$a, $c, $b],
            [$b, $a, $c],
            [$b, $c, $a],
            [$c, $a, $b],
            [$c, $b, $a]
        ];
        
        $best = null;
        foreach ($perms as $p) {
            $cur = $p[0];
            for ($i = 1; $i < 3; ++$i) {
                $cur = $this->combine($cur, $p[$i]);
            }
            if ($best === null || strlen($cur) < strlen($best) ||
               (strlen($cur) == strlen($best) && strcmp($cur, $best) < 0)) {
                $best = $cur;
            }
        }
        return $best;
    }
    
    private function combine(string $s1, string $s2): string {
        // If one is substring of the other, return the longer (or containing) one
        if (strpos($s1, $s2) !== false) {
            return $s1;
        }
        if (strpos($s2, $s1) !== false) {
            return $s2;
        }
        $len1 = strlen($s1);
        $len2 = strlen($s2);
        $maxOverlap = 0;
        $limit = min($len1, $len2);
        for ($k = $limit; $k > 0; --$k) {
            if (substr($s1, $len1 - $k) === substr($s2, 0, $k)) {
                $maxOverlap = $k;
                break;
            }
        }
        return $s1 . substr($s2, $maxOverlap);
    }
}
```

## Swift

```swift
class Solution {
    func minimumString(_ a: String, _ b: String, _ c: String) -> String {
        let strs = [a, b, c]
        let perms = [
            [0, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0]
        ]
        
        func merge(_ s1: String, _ s2: String) -> String {
            if s1.contains(s2) { return s1 }
            let arr1 = Array(s1)
            let arr2 = Array(s2)
            var maxOverlap = 0
            let limit = min(arr1.count, arr2.count)
            for k in stride(from: limit, through: 1, by: -1) {
                var ok = true
                for i in 0..<k {
                    if arr1[arr1.count - k + i] != arr2[i] {
                        ok = false
                        break
                    }
                }
                if ok {
                    maxOverlap = k
                    break
                }
            }
            let suffix = String(arr2[maxOverlap...])
            return s1 + suffix
        }
        
        var best = ""
        for p in perms {
            var cur = strs[p[0]]
            cur = merge(cur, strs[p[1]])
            cur = merge(cur, strs[p[2]])
            if best.isEmpty || cur.count < best.count || (cur.count == best.count && cur < best) {
                best = cur
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumString(a: String, b: String, c: String): String {
        val arr = arrayOf(a, b, c)

        fun merge(s: String, t: String): String {
            if (s.contains(t)) return s
            var overlap = 0
            val limit = minOf(s.length, t.length)
            for (len in limit downTo 1) {
                if (s.endsWith(t.substring(0, len))) {
                    overlap = len
                    break
                }
            }
            return s + t.substring(overlap)
        }

        var best = ""
        for (i in 0..2) {
            for (j in 0..2) {
                if (j == i) continue
                for (k in 0..2) {
                    if (k == i || k == j) continue
                    var cur = arr[i]
                    cur = merge(cur, arr[j])
                    cur = merge(cur, arr[k])
                    if (best.isEmpty() ||
                        cur.length < best.length ||
                        (cur.length == best.length && cur < best)
                    ) {
                        best = cur
                    }
                }
            }
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  String minimumString(String a, String b, String c) {
    List<String> arr = [a, b, c];
    List<List<int>> perms = [
      [0, 1, 2],
      [0, 2, 1],
      [1, 0, 2],
      [1, 2, 0],
      [2, 0, 1],
      [2, 1, 0]
    ];
    String best = '';
    bool first = true;
    for (var p in perms) {
      String merged = _merge(_merge(arr[p[0]], arr[p[1]]), arr[p[2]]);
      if (first ||
          merged.length < best.length ||
          (merged.length == best.length && merged.compareTo(best) < 0)) {
        best = merged;
        first = false;
      }
    }
    return best;
  }

  String _merge(String s1, String s2) {
    if (s1.contains(s2)) return s1;
    int maxOverlap = 0;
    int limit = s1.length < s2.length ? s1.length : s2.length;
    for (int k = limit; k >= 1; --k) {
      if (s1.substring(s1.length - k) == s2.substring(0, k)) {
        maxOverlap = k;
        break;
      }
    }
    return s1 + s2.substring(maxOverlap);
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func minimumString(a string, b string, c string) string {
	merge := func(s1, s2 string) string {
		if strings.Contains(s1, s2) {
			return s1
		}
		maxOverlap := 0
		limit := len(s1)
		if len(s2) < limit {
			limit = len(s2)
		}
		for k := limit; k > 0; k-- {
			if s1[len(s1)-k:] == s2[:k] {
				maxOverlap = k
				break
			}
		}
		return s1 + s2[maxOverlap:]
	}

	strs := []string{a, b, c}
	perms := [][]int{
		{0, 1, 2},
		{0, 2, 1},
		{1, 0, 2},
		{1, 2, 0},
		{2, 0, 1},
		{2, 1, 0},
	}

	var best string
	first := true
	for _, p := range perms {
		s := merge(strs[p[0]], strs[p[1]])
		s = merge(s, strs[p[2]])
		if first || len(s) < len(best) || (len(s) == len(best) && s < best) {
			best = s
			first = false
		}
	}
	return best
}
```

## Ruby

```ruby
def merge(s1, s2)
  return s1 if s1.include?(s2)
  return s2 if s2.include?(s1)

  best = nil
  max_len = [s1.length, s2.length].min

  (max_len).downto(0) do |i|
    if i == 0 || s1[-i, i] == s2[0, i]
      cand = s1 + s2[i..-1].to_s
      best = cand
      break
    end
  end

  (max_len).downto(0) do |i|
    if i == 0 || s2[-i, i] == s1[0, i]
      cand = s2 + s1[i..-1].to_s
      if best.nil? || cand.length < best.length || (cand.length == best.length && cand < best)
        best = cand
      end
      break
    end
  end

  best
end

# @param {String} a
# @param {String} b
# @param {String} c
# @return {String}
def minimum_string(a, b, c)
  ans = nil
  [a, b, c].permutation.each do |perm|
    s = merge(perm[0], perm[1])
    s = merge(s, perm[2])
    if ans.nil? || s.length < ans.length || (s.length == ans.length && s < ans)
      ans = s
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumString(a: String, b: String, c: String): String = {
        val strs = Array(a, b, c)

        def merge(s: String, t: String): String = {
            if (s.contains(t)) return s
            var maxOverlap = 0
            val limit = Math.min(s.length, t.length)
            var k = limit
            while (k > 0) {
                if (s.endsWith(t.substring(0, k))) {
                    maxOverlap = k
                    k = 0
                } else {
                    k -= 1
                }
            }
            s + t.substring(maxOverlap)
        }

        val perms = Array(
            Array(strs(0), strs(1), strs(2)),
            Array(strs(0), strs(2), strs(1)),
            Array(strs(1), strs(0), strs(2)),
            Array(strs(1), strs(2), strs(0)),
            Array(strs(2), strs(0), strs(1)),
            Array(strs(2), strs(1), strs(0))
        )

        var best: String = null
        for (p <- perms) {
            var cur = p(0)
            cur = merge(cur, p(1))
            cur = merge(cur, p(2))
            if (best == null ||
                cur.length < best.length ||
                (cur.length == best.length && cur.compareTo(best) < 0)) {
                best = cur
            }
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_string(a: String, b: String, c: String) -> String {
        fn merge(x: &str, y: &str) -> String {
            if x.contains(y) {
                return x.to_string();
            }
            if y.contains(x) {
                return y.to_string();
            }
            let max_overlap = std::cmp::min(x.len(), y.len());
            let mut overlap = 0;
            for k in (1..=max_overlap).rev() {
                if &x[x.len() - k..] == &y[..k] {
                    overlap = k;
                    break;
                }
            }
            format!("{}{}", x, &y[overlap..])
        }

        let strs = [a, b, c];
        let perms = [
            (0usize, 1usize, 2usize),
            (0, 2, 1),
            (1, 0, 2),
            (1, 2, 0),
            (2, 0, 1),
            (2, 1, 0),
        ];
        let mut best = String::new();
        for &(i, j, k) in &perms {
            let first = &strs[i];
            let second = &strs[j];
            let third = &strs[k];
            let tmp = merge(first, second);
            let candidate = merge(&tmp, third);
            if best.is_empty()
                || candidate.len() < best.len()
                || (candidate.len() == best.len() && candidate < best)
            {
                best = candidate;
            }
        }
        best
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define (max-overlap s t)
  (let ((len-s (string-length s))
        (len-t (string-length t)))
    (let loop ((k (min len-s len-t)))
      (if (= k 0) 
          0
          (if (string=? (substring s (- len-s k)) (substring t 0 k))
              k
              (loop (- k 1)))))))

(define (merge-two s t)
  (cond [(string-contains? s t) s]
        [(string-contains? t s) t]
        [else (let ((ov (max-overlap s t)))
                (string-append s (substring t ov)))]))

(define/contract (minimum-string a b c)
  (-> string? string? string? string?)
  (let ((perms (list (list a b c)
                     (list a c b)
                     (list b a c)
                     (list b c a)
                     (list c a b)
                     (list c b a))))
    (define best #f)
    (for ([p perms])
      (define merged
        (foldl (lambda (elem acc) (merge-two acc elem))
               (first p)
               (rest p)))
      (when (or (not best)
                (< (string-length merged) (string-length best))
                (and (= (string-length merged) (string-length best))
                     (string<? merged best)))
        (set! best merged)))
    best))
```

## Erlang

```erlang
-module(solution).
-export([minimum_string/3]).

-spec minimum_string(A :: unicode:unicode_binary(),
                     B :: unicode:unicode_binary(),
                     C :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimum_string(A, B, C) ->
    Perms = [[A, B, C],
             [A, C, B],
             [B, A, C],
             [B, C, A],
             [C, A, B],
             [C, B, A]],
    lists:foldl(fun(Perm, Acc) ->
        [S1, S2, S3] = Perm,
        M12  = merge_two(S1, S2),
        M123 = merge_two(M12, S3),
        case Acc of
            undefined -> M123;
            _ ->
                LenM   = byte_size(M123),
                LenBest = byte_size(Acc),
                if LenM < LenBest ->
                        M123;
                   LenM > LenBest ->
                        Acc;
                   true ->
                        case binary:compare(M123, Acc) of
                            lt -> M123;
                            _  -> Acc
                        end
                end
        end
    end, undefined, Perms).

merge_two(B1, B2) ->
    %% If B2 is already a substring of B1, keep B1.
    case binary:match(B1, B2) of
        {_, _} -> B1;
        nomatch ->
            Len1 = byte_size(B1),
            Len2 = byte_size(B2),
            MaxK = erlang:min(Len1, Len2),
            Overlap = find_overlap(B1, B2, Len1, Len2, MaxK),
            <<B1/binary,
              (binary:part(B2, {Overlap, Len2 - Overlap}))/binary>>
    end.

find_overlap(_B1, _B2, _Len1, _Len2, 0) -> 0;
find_overlap(B1, B2, Len1, Len2, K) ->
    Suffix = binary:part(B1, {Len1 - K, K}),
    Prefix = binary:part(B2, {0, K}),
    if Suffix == Prefix ->
            K;
       true ->
            find_overlap(B1, B2, Len1, Len2, K - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_string(a :: String.t(), b :: String.t(), c :: String.t()) :: String.t()
  def minimum_string(a, b, c) do
    perms = [
      [a, b, c],
      [a, c, b],
      [b, a, c],
      [b, c, a],
      [c, a, b],
      [c, b, a]
    ]

    Enum.reduce(perms, nil, fn perm, best ->
      s = merge_two(Enum.at(perm, 0), Enum.at(perm, 1))
      s = merge_two(s, Enum.at(perm, 2))

      cond do
        best == nil -> s
        byte_size(s) < byte_size(best) -> s
        byte_size(s) > byte_size(best) -> best
        true ->
          if s <= best, do: s, else: best
      end
    end)
  end

  defp merge_two(a, b) do
    cond do
      String.contains?(a, b) -> a
      String.contains?(b, a) -> b
      true ->
        max1 = overlap_len(a, b)
        cand1 = a <> String.slice(b, max1, byte_size(b) - max1)

        max2 = overlap_len(b, a)
        cand2 = b <> String.slice(a, max2, byte_size(a) - max2)

        choose(cand1, cand2)
    end
  end

  defp choose(s1, s2) do
    l1 = byte_size(s1)
    l2 = byte_size(s2)

    cond do
      l1 < l2 -> s1
      l1 > l2 -> s2
      true ->
        if s1 <= s2, do: s1, else: s2
    end
  end

  defp overlap_len(s1, s2) do
    l1 = byte_size(s1)
    l2 = byte_size(s2)
    max = min(l1, l2)
    find_overlap(max, s1, s2, l1, l2)
  end

  defp find_overlap(0, _s1, _s2, _l1, _l2), do: 0

  defp find_overlap(k, s1, s2, l1, l2) do
    if :binary.part(s1, l1 - k, k) == :binary.part(s2, 0, k) do
      k
    else
      find_overlap(k - 1, s1, s2, l1, l2)
    end
  end
end
```
