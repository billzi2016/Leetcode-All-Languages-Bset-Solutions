# 3076. Shortest Uncommon Substring in an Array

## Cpp

```cpp
class Solution {
public:
    vector<string> shortestSubstrings(vector<string>& arr) {
        int n = arr.size();
        unordered_map<string, int> cnt;
        vector<unordered_set<string>> subs_per_string(n);
        
        // Count each distinct substring per string
        for (int i = 0; i < n; ++i) {
            const string& s = arr[i];
            unordered_set<string>& local = subs_per_string[i];
            int L = s.size();
            for (int l = 0; l < L; ++l) {
                string cur;
                cur.reserve(L - l);
                for (int r = l; r < L; ++r) {
                    cur.push_back(s[r]);
                    if (local.insert(cur).second) {
                        ++cnt[cur];
                    }
                }
            }
        }
        
        vector<string> ans(n);
        // Find answer for each string
        for (int i = 0; i < n; ++i) {
            const string& s = arr[i];
            int L = s.size();
            string best = "";
            bool found = false;
            for (int len = 1; len <= L && !found; ++len) {
                vector<string> candidates;
                unordered_set<string> seen;
                for (int start = 0; start + len <= L; ++start) {
                    string sub = s.substr(start, len);
                    if (!seen.insert(sub).second) continue;
                    if (cnt[sub] == 1) {
                        candidates.push_back(sub);
                    }
                }
                if (!candidates.empty()) {
                    sort(candidates.begin(), candidates.end());
                    best = candidates[0];
                    found = true;
                }
            }
            ans[i] = best; // empty string if not found
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String[] shortestSubstrings(String[] arr) {
        int n = arr.length;
        java.util.Map<String, Integer> cnt = new java.util.HashMap<>();
        // Count substrings per distinct string
        for (String s : arr) {
            java.util.Set<String> set = new java.util.HashSet<>();
            int L = s.length();
            for (int i = 0; i < L; i++) {
                for (int j = i + 1; j <= L; j++) {
                    set.add(s.substring(i, j));
                }
            }
            for (String sub : set) {
                cnt.put(sub, cnt.getOrDefault(sub, 0) + 1);
            }
        }

        String[] ans = new String[n];
        for (int idx = 0; idx < n; idx++) {
            String s = arr[idx];
            int L = s.length();
            String result = null;
            for (int len = 1; len <= L; len++) {
                String best = null;
                for (int start = 0; start + len <= L; start++) {
                    String sub = s.substring(start, start + len);
                    if (cnt.getOrDefault(sub, 0) == 1) {
                        if (best == null || sub.compareTo(best) < 0) {
                            best = sub;
                        }
                    }
                }
                if (best != null) {
                    result = best;
                    break;
                }
            }
            ans[idx] = result == null ? "" : result;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        sub_count = {}
        # Count each distinct substring per string
        for s in arr:
            seen = set()
            L = len(s)
            for i in range(L):
                for j in range(i + 1, L + 1):
                    sub = s[i:j]
                    if sub not in seen:
                        seen.add(sub)
                        sub_count[sub] = sub_count.get(sub, 0) + 1

        result = []
        # Find shortest uncommon substring for each string
        for s in arr:
            ans = ""
            L = len(s)
            found = False
            for length in range(1, L + 1):
                candidates = []
                for i in range(L - length + 1):
                    sub = s[i:i + length]
                    if sub_count.get(sub, 0) == 1:
                        candidates.append(sub)
                if candidates:
                    ans = min(candidates)
                    found = True
                    break
            result.append(ans)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        sub_to_set = {}
        substrings_per_idx = [set() for _ in range(n)]

        # collect unique substrings per string and map to the set of indices where they appear
        for i, s in enumerate(arr):
            seen = set()
            L = len(s)
            for start in range(L):
                for end in range(start + 1, L + 1):
                    sub = s[start:end]
                    if sub in seen:
                        continue
                    seen.add(sub)
                    substrings_per_idx[i].add(sub)
                    if sub in sub_to_set:
                        sub_to_set[sub].add(i)
                    else:
                        sub_to_set[sub] = {i}

        answer = []
        for i, s in enumerate(arr):
            L = len(s)
            found = False
            # try lengths from 1 upwards
            for length in range(1, L + 1):
                candidates = []
                for start in range(L - length + 1):
                    sub = s[start:start + length]
                    occ = sub_to_set.get(sub, set())
                    if len(occ) == 1 and i in occ:
                        candidates.append(sub)
                if candidates:
                    answer.append(min(candidates))
                    found = True
                    break
            if not found:
                answer.append("")
        return answer
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

char** shortestSubstrings(char** arr, int arrSize, int* returnSize) {
    char **ans = (char **)malloc(arrSize * sizeof(char *));
    for (int i = 0; i < arrSize; ++i) {
        const char *s = arr[i];
        int L = strlen(s);
        char best[21];          // max substring length is 20
        int foundLen = -1;      // length of best substring, -1 means not found yet

        for (int len = 1; len <= L; ++len) {
            int haveCandidate = 0;
            // iterate all substrings of current length
            for (int start = 0; start + len <= L; ++start) {
                char sub[21];
                memcpy(sub, s + start, len);
                sub[len] = '\0';

                // check if sub appears in any other string
                int unique = 1;
                for (int j = 0; j < arrSize; ++j) {
                    if (j == i) continue;
                    if (strstr(arr[j], sub) != NULL) {
                        unique = 0;
                        break;
                    }
                }
                if (!unique) continue;

                // this substring is unique to string i
                if (!haveCandidate || strcmp(sub, best) < 0) {
                    strcpy(best, sub);
                }
                haveCandidate = 1;
            }
            if (haveCandidate) {
                foundLen = len;   // shortest length found
                break;            // no need to check longer lengths
            }
        }

        if (foundLen == -1) {
            ans[i] = (char *)malloc(1);
            ans[i][0] = '\0';
        } else {
            int blen = strlen(best);
            ans[i] = (char *)malloc(blen + 1);
            strcpy(ans[i], best);
        }
    }
    *returnSize = arrSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public string[] ShortestSubstrings(string[] arr)
    {
        int n = arr.Length;
        var occ = new Dictionary<string, int>();

        // Count in how many different strings each substring appears
        for (int i = 0; i < n; i++)
        {
            var s = arr[i];
            var seenInThis = new HashSet<string>();
            int len = s.Length;
            for (int start = 0; start < len; start++)
            {
                for (int l = 1; start + l <= len; l++)
                {
                    string sub = s.Substring(start, l);
                    if (seenInThis.Add(sub))
                    {
                        if (occ.ContainsKey(sub))
                            occ[sub]++;
                        else
                            occ[sub] = 1;
                    }
                }
            }
        }

        var answer = new string[n];

        // Find shortest unique substring for each string
        for (int i = 0; i < n; i++)
        {
            var s = arr[i];
            var seen = new HashSet<string>();
            int bestLen = int.MaxValue;
            string bestStr = "";
            int len = s.Length;

            for (int start = 0; start < len; start++)
            {
                for (int l = 1; start + l <= len; l++)
                {
                    string sub = s.Substring(start, l);
                    if (!seen.Add(sub)) continue; // avoid duplicates within same string

                    if (occ[sub] == 1)
                    {
                        if (l < bestLen || (l == bestLen && string.CompareOrdinal(sub, bestStr) < 0))
                        {
                            bestLen = l;
                            bestStr = sub;
                        }
                    }
                }
            }

            answer[i] = bestStr; // empty if none found
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} arr
 * @return {string[]}
 */
var shortestSubstrings = function(arr) {
    const n = arr.length;
    const globalCount = new Map(); // substring -> number of distinct strings containing it

    // First pass: count each unique substring per string
    for (let i = 0; i < n; i++) {
        const s = arr[i];
        const seen = new Set();
        const L = s.length;
        for (let start = 0; start < L; start++) {
            let sub = '';
            for (let end = start; end < L; end++) {
                sub += s[end];
                seen.add(sub);
            }
        }
        for (const sub of seen) {
            globalCount.set(sub, (globalCount.get(sub) || 0) + 1);
        }
    }

    const result = new Array(n).fill('');

    // Second pass: find shortest uncommon substring per string
    for (let i = 0; i < n; i++) {
        const s = arr[i];
        const L = s.length;
        let found = false;

        for (let len = 1; len <= L && !found; len++) {
            const candidates = [];
            for (let start = 0; start + len <= L; start++) {
                const sub = s.substring(start, start + len);
                if (globalCount.get(sub) === 1) {
                    candidates.push(sub);
                }
            }
            if (candidates.length > 0) {
                candidates.sort(); // lexicographic order
                result[i] = candidates[0];
                found = true;
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function shortestSubstrings(arr: string[]): string[] {
    const substrCount = new Map<string, number>();

    // Count each distinct substring per string
    for (const s of arr) {
        const seen = new Set<string>();
        const n = s.length;
        for (let i = 0; i < n; i++) {
            let cur = '';
            for (let j = i; j < n; j++) {
                cur += s[j];
                if (!seen.has(cur)) {
                    seen.add(cur);
                    substrCount.set(cur, (substrCount.get(cur) ?? 0) + 1);
                }
            }
        }
    }

    const ans: string[] = [];

    // Find shortest unique substring for each string
    for (const s of arr) {
        let best = '';
        const n = s.length;
        outer: for (let len = 1; len <= n; len++) {
            const candidates: string[] = [];
            for (let i = 0; i + len <= n; i++) {
                const sub = s.substring(i, i + len);
                if ((substrCount.get(sub) ?? 0) === 1) {
                    candidates.push(sub);
                }
            }
            if (candidates.length > 0) {
                candidates.sort(); // lexicographically smallest first
                best = candidates[0];
                break outer;
            }
        }
        ans.push(best);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $arr
     * @return String[]
     */
    function shortestSubstrings($arr) {
        $n = count($arr);
        $subMap = [];

        // First pass: count in how many different strings each substring appears
        for ($i = 0; $i < $n; $i++) {
            $s = $arr[$i];
            $len = strlen($s);
            $seen = [];
            for ($start = 0; $start < $len; $start++) {
                for ($l = 1; $l <= $len - $start; $l++) {
                    $sub = substr($s, $start, $l);
                    if (!isset($seen[$sub])) {
                        $seen[$sub] = true;
                        if (isset($subMap[$sub])) {
                            $subMap[$sub]++;
                        } else {
                            $subMap[$sub] = 1;
                        }
                    }
                }
            }
        }

        $answer = array_fill(0, $n, "");

        // Second pass: for each string find its shortest unique substring
        for ($i = 0; $i < $n; $i++) {
            $s = $arr[$i];
            $len = strlen($s);
            $best = null;
            $bestLen = PHP_INT_MAX;
            $seen = [];
            for ($start = 0; $start < $len; $start++) {
                for ($l = 1; $l <= $len - $start; $l++) {
                    $sub = substr($s, $start, $l);
                    if (isset($seen[$sub])) continue;
                    $seen[$sub] = true;
                    if ($subMap[$sub] === 1) { // unique to this string
                        if ($l < $bestLen) {
                            $bestLen = $l;
                            $best = $sub;
                        } elseif ($l == $bestLen && strcmp($sub, $best) < 0) {
                            $best = $sub;
                        }
                    }
                }
            }
            $answer[$i] = $best === null ? "" : $best;
        }

        return $answer;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func shortestSubstrings(_ arr: [String]) -> [String] {
        var globalCount = [String:Int]()
        
        // First pass: count each distinct substring per string
        for s in arr {
            let chars = Array(s)
            let n = chars.count
            var seen = Set<String>()
            for i in 0..<n {
                var subChars = [Character]()
                for j in i..<n {
                    subChars.append(chars[j])
                    let sub = String(subChars)
                    if !seen.contains(sub) {
                        seen.insert(sub)
                        globalCount[sub, default: 0] += 1
                    }
                }
            }
        }
        
        var result = [String]()
        
        // Second pass: find shortest unique substring for each string
        for s in arr {
            let chars = Array(s)
            let n = chars.count
            var answer = ""
            var found = false
            
            for length in 1...n where !found {
                var bestCandidate: String? = nil
                if n - length < 0 { continue }
                for start in 0...(n - length) {
                    let sub = String(chars[start..<(start + length)])
                    if globalCount[sub] == 1 {
                        if bestCandidate == nil || sub < bestCandidate! {
                            bestCandidate = sub
                        }
                    }
                }
                if let cand = bestCandidate {
                    answer = cand
                    found = true
                }
            }
            
            result.append(answer)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestSubstrings(arr: Array<String>): Array<String> {
        val freq = HashMap<String, Int>()
        // Count each distinct substring per string
        for (s in arr) {
            val seen = HashSet<String>()
            val n = s.length
            for (i in 0 until n) {
                var sb = StringBuilder()
                for (j in i until n) {
                    sb.append(s[j])
                    val sub = sb.toString()
                    if (seen.add(sub)) {
                        freq[sub] = (freq[sub] ?: 0) + 1
                    }
                }
            }
        }

        val result = Array(arr.size) { "" }
        for ((idx, s) in arr.withIndex()) {
            var answer: String? = null
            outer@ for (len in 1..s.length) {
                val candidates = mutableListOf<String>()
                for (i in 0..s.length - len) {
                    val sub = s.substring(i, i + len)
                    if (freq[sub] == 1) {
                        candidates.add(sub)
                    }
                }
                if (candidates.isNotEmpty()) {
                    candidates.sort()
                    answer = candidates[0]
                    break@outer
                }
            }
            result[idx] = answer ?: ""
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> shortestSubstrings(List<String> arr) {
    final Map<String, int> freq = {};

    // Count substrings per string (unique within each string)
    for (final s in arr) {
      final Set<String> seen = {};
      final int len = s.length;
      for (int i = 0; i < len; ++i) {
        for (int j = i + 1; j <= len; ++j) {
          final sub = s.substring(i, j);
          if (!seen.contains(sub)) {
            seen.add(sub);
            freq[sub] = (freq[sub] ?? 0) + 1;
          }
        }
      }
    }

    final List<String> answer = List.filled(arr.length, '');
    for (int idx = 0; idx < arr.length; ++idx) {
      final s = arr[idx];
      final int len = s.length;
      String? best;

      // Try lengths from shortest to longest
      outer:
      for (int l = 1; l <= len; ++l) {
        String? candidate;
        for (int i = 0; i + l <= len; ++i) {
          final sub = s.substring(i, i + l);
          if ((freq[sub] ?? 0) == 1) {
            if (candidate == null || sub.compareTo(candidate) < 0) {
              candidate = sub;
            }
          }
        }
        if (candidate != null) {
          best = candidate;
          break outer;
        }
      }

      answer[idx] = best ?? '';
    }

    return answer;
  }
}
```

## Golang

```go
func shortestSubstrings(arr []string) []string {
    cnt := make(map[string]int)

    // Count each distinct substring per string
    for _, s := range arr {
        seen := make(map[string]struct{})
        l := len(s)
        for i := 0; i < l; i++ {
            for j := i + 1; j <= l; j++ {
                sub := s[i:j]
                if _, ok := seen[sub]; !ok {
                    seen[sub] = struct{}{}
                    cnt[sub]++
                }
            }
        }
    }

    ans := make([]string, len(arr))
    for idx, s := range arr {
        found := ""
        l := len(s)
        // search by increasing length
        for length := 1; length <= l; length++ {
            minSub := ""
            for start := 0; start+length <= l; start++ {
                sub := s[start : start+length]
                if cnt[sub] == 1 {
                    if minSub == "" || sub < minSub {
                        minSub = sub
                    }
                }
            }
            if minSub != "" {
                found = minSub
                break
            }
        }
        ans[idx] = found
    }

    return ans
}
```

## Ruby

```ruby
def shortest_substrings(arr)
  global_counts = Hash.new(0)

  arr.each do |s|
    seen = {}
    l = s.length
    (0...l).each do |st|
      (st + 1..l).each do |en|
        sub = s[st...en]
        unless seen[sub]
          seen[sub] = true
          global_counts[sub] += 1
        end
      end
    end
  end

  arr.map do |s|
    best = nil
    l = s.length
    (0...l).each do |st|
      (st + 1..l).each do |en|
        sub = s[st...en]
        next unless global_counts[sub] == 1
        if best.nil? || sub.length < best.length || (sub.length == best.length && sub < best)
          best = sub
        end
      end
    end
    best ? best : ""
  end
end
```

## Scala

```scala
object Solution {
    def shortestSubstrings(arr: Array[String]): Array[String] = {
        import scala.collection.mutable.{Map => MutableMap, Set => MutableSet}
        val n = arr.length
        // map substring -> number of distinct strings containing it
        val cnt = MutableMap.empty[String, Int]

        // First pass: count substrings per string (unique within a string)
        for (s <- arr) {
            val seen = MutableSet.empty[String]
            val len = s.length
            var i = 0
            while (i < len) {
                var j = i + 1
                while (j <= len) {
                    seen += s.substring(i, j)
                    j += 1
                }
                i += 1
            }
            for (sub <- seen) {
                cnt.update(sub, cnt.getOrElse(sub, 0) + 1)
            }
        }

        // Second pass: find shortest unique substring per string
        val ans = new Array[String](n)
        var idx = 0
        while (idx < n) {
            val s = arr(idx)
            var bestLen = Int.MaxValue
            var bestStr = ""
            val len = s.length
            var i = 0
            while (i < len) {
                var j = i + 1
                while (j <= len) {
                    val sub = s.substring(i, j)
                    if (cnt.getOrElse(sub, 0) == 1) {
                        val l = sub.length
                        if (l < bestLen || (l == bestLen && sub < bestStr)) {
                            bestLen = l
                            bestStr = sub
                        }
                    }
                    j += 1
                }
                i += 1
            }
            ans(idx) = if (bestLen == Int.MaxValue) "" else bestStr
            idx += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_substrings(arr: Vec<String>) -> Vec<String> {
        use std::collections::{HashMap, HashSet};

        let n = arr.len();
        // substring -> number of distinct strings containing it
        let mut cnt: HashMap<String, usize> = HashMap::new();
        // store unique substrings for each string
        let mut subs_per_str: Vec<Vec<String>> = Vec::with_capacity(n);

        for s in &arr {
            let chars: Vec<char> = s.chars().collect();
            let len = chars.len();
            let mut seen: HashSet<String> = HashSet::new();

            for i in 0..len {
                let mut cur = String::new();
                for j in i..len {
                    cur.push(chars[j]);
                    if seen.insert(cur.clone()) {
                        *cnt.entry(cur.clone()).or_insert(0) += 1;
                    }
                }
            }

            subs_per_str.push(seen.into_iter().collect());
        }

        let mut answer: Vec<String> = Vec::with_capacity(n);
        for (idx, _) in arr.iter().enumerate() {
            let mut best_len = usize::MAX;
            let mut best_sub = String::new();

            for sub in &subs_per_str[idx] {
                if cnt.get(sub).copied().unwrap_or(0) == 1 {
                    let l = sub.len();
                    if l < best_len || (l == best_len && sub < &best_sub) {
                        best_len = l;
                        best_sub = sub.clone();
                    }
                }
            }

            if best_len == usize::MAX {
                answer.push(String::new());
            } else {
                answer.push(best_sub);
            }
        }

        answer
    }
}
```

## Racket

```racket
#lang racket

(define/contract (shortest-substrings arr)
  (-> (listof string?) (listof string?))
  (let ((global (make-hash)))
    ;; First pass: count each distinct substring per string
    (for ([s arr])
      (let ((local (make-hash)))
        (let ((len (string-length s)))
          (for ([i (in-range len)])
            (for ([j (in-range (+ i 1) (+ len 1))])
              (define sub (substring s i j))
              (unless (hash-has-key? local sub)
                (hash-set! local sub #t)
                (if (hash-has-key? global sub)
                    (hash-set! global sub (+ 1 (hash-ref global sub)))
                    (hash-set! global sub 1))))))))
    ;; Second pass: find shortest unique substring for each string
    (let ((answers '()))
      (for ([s arr])
        (define best "")
        (define bestlen 1000) ; larger than any possible substring length
        (let ((len (string-length s)))
          (for ([i (in-range len)])
            (for ([j (in-range (+ i 1) (+ len 1))])
              (define sub (substring s i j))
              (when (= (hash-ref global sub) 1)
                (define slen (- j i))
                (cond
                  [(< slen bestlen)
                   (set! best sub)
                   (set! bestlen slen)]
                  [(and (= slen bestlen) (string<? sub best))
                   (set! best sub)])))))
        (set! answers (cons best answers)))
      (reverse answers))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_substrings/1]).

-spec shortest_substrings(Arr :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
shortest_substrings(Arr) ->
    CountMap = build_counts(Arr, #{}),
    lists:map(fun(S) -> find_unique(S, CountMap) end, Arr).

build_counts([], Map) -> Map;
build_counts([S|Rest], Map) ->
    Unique = substrings_set(S),
    NewMap = maps:fold(
        fun(Sub, _Val, Acc) ->
            Prev = maps:get(Sub, Acc, 0),
            maps:put(Sub, Prev + 1, Acc)
        end,
        Map,
        Unique),
    build_counts(Rest, NewMap).

substrings_set(S) ->
    LenS = byte_size(S),
    lists:foldl(
        fun(Start, Acc) ->
            MaxLen = LenS - Start,
            lists:foldl(
                fun(Len, A2) ->
                    Sub = binary:part(S, {Start, Len}),
                    maps:put(Sub, true, A2)
                end,
                Acc,
                lists:seq(1, MaxLen))
        end,
        #{},
        lists:seq(0, LenS - 1)).

find_unique(S, CountMap) ->
    Unique = substrings_set(S),
    Candidates = maps:fold(
        fun(Sub, _Val, Acc) ->
            case maps:get(Sub, CountMap) of
                1 -> [Sub|Acc];
                _ -> Acc
            end
        end,
        [],
        Unique),
    select_best(Candidates).

select_best([]) -> <<>>;
select_best([First|Rest]) ->
    Best = {byte_size(First), First},
    {_, Result} = lists:foldl(
        fun(Sub, {BestLen, BestSub}) ->
            Len = byte_size(Sub),
            case Len < BestLen of
                true -> {Len, Sub};
                false when Len == BestLen ->
                    if Sub < BestSub -> {Len, Sub}; true -> {Len, BestSub} end;
                false -> {BestLen, BestSub}
            end
        end,
        Best,
        Rest),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_substrings(arr :: [String.t]) :: [String.t]
  def shortest_substrings(arr) do
    occ =
      Enum.reduce(Enum.with_index(arr), %{}, fn {s, _idx}, acc ->
        subs = substrings_set(s)

        Enum.reduce(subs, acc, fn sub, a ->
          Map.update(a, sub, 1, &(&1 + 1))
        end)
      end)

    Enum.map(arr, fn s ->
      subs = substrings_set(s)

      unique_subs =
        Enum.filter(subs, fn sub -> Map.get(occ, sub) == 1 end)

      case unique_subs do
        [] ->
          ""

        _ ->
          min_len =
            unique_subs
            |> Enum.map(&String.length/1)
            |> Enum.min()

          unique_subs
          |> Enum.filter(fn sub -> String.length(sub) == min_len end)
          |> Enum.min()
      end
    end)
  end

  defp substrings_set(s) do
    len = String.length(s)

    Enum.reduce(0..(len - 1), MapSet.new(), fn i, set ->
      Enum.reduce(1..(len - i), set, fn l, sset ->
        sub = String.slice(s, i, l)
        MapSet.put(sset, sub)
      end)
    end)
  end
end
```
