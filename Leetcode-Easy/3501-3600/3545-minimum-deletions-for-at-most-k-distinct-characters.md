# 3545. Minimum Deletions for At Most K Distinct Characters

## Cpp

```cpp
class Solution {
public:
    int minDeletion(string s, int k) {
        int freq[26] = {0};
        for (char c : s) freq[c - 'a']++;
        vector<int> counts;
        for (int f : freq) if (f > 0) counts.push_back(f);
        int distinct = counts.size();
        int needRemove = distinct - k;
        if (needRemove <= 0) return 0;
        sort(counts.begin(), counts.end());
        int deletions = 0;
        for (int i = 0; i < needRemove; ++i) deletions += counts[i];
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minDeletion(String s, int k) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        java.util.List<Integer> counts = new java.util.ArrayList<>();
        for (int f : freq) {
            if (f > 0) counts.add(f);
        }
        int distinct = counts.size();
        int excess = distinct - k;
        if (excess <= 0) return 0;
        java.util.Collections.sort(counts);
        int deletions = 0;
        for (int i = 0; i < excess; i++) {
            deletions += counts.get(i);
        }
        return deletions;
    }
}
```

## Python

```python
class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        counts = list(freq.values())
        distinct = len(counts)
        if distinct <= k:
            return 0
        counts.sort()
        deletions_needed = distinct - k
        return sum(counts[:deletions_needed])
```

## Python3

```python
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter
        freq = Counter(s)
        counts = list(freq.values())
        d = len(counts) - k
        if d <= 0:
            return 0
        counts.sort()
        return sum(counts[:d])
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int minDeletion(char* s, int k) {
    int freq[26] = {0};
    for (char *p = s; *p != '\0'; ++p) {
        freq[*p - 'a']++;
    }

    int counts[26];
    int m = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > 0) {
            counts[m++] = freq[i];
        }
    }

    if (m <= k) return 0;

    qsort(counts, m, sizeof(int), cmp_int);

    int deletions = 0;
    int d = m - k;
    for (int i = 0; i < d; ++i) {
        deletions += counts[i];
    }
    return deletions;
}
```

## Csharp

```csharp
public class Solution {
    public int MinDeletion(string s, int k) {
        int[] freq = new int[26];
        foreach (char c in s) {
            freq[c - 'a']++;
        }
        var counts = new List<int>();
        foreach (int f in freq) {
            if (f > 0) counts.Add(f);
        }
        int distinct = counts.Count;
        if (distinct <= k) return 0;
        counts.Sort(); // ascending
        int deletionsNeeded = distinct - k;
        int deletions = 0;
        for (int i = 0; i < deletionsNeeded; i++) {
            deletions += counts[i];
        }
        return deletions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minDeletion = function(s, k) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    const counts = [];
    for (let f of freq) if (f > 0) counts.push(f);
    const distinct = counts.length;
    const needRemove = distinct - k;
    if (needRemove <= 0) return 0;
    counts.sort((a, b) => a - b);
    let deletions = 0;
    for (let i = 0; i < needRemove; ++i) {
        deletions += counts[i];
    }
    return deletions;
};
```

## Typescript

```typescript
function minDeletion(s: string, k: number): number {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    const counts: number[] = [];
    for (const f of freq) {
        if (f > 0) counts.push(f);
    }
    const distinct = counts.length;
    if (distinct <= k) return 0;
    counts.sort((a, b) => a - b);
    let deletions = 0;
    const needRemove = distinct - k;
    for (let i = 0; i < needRemove; ++i) {
        deletions += counts[i];
    }
    return deletions;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function minDeletion($s, $k) {
        $freq = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        $counts = [];
        foreach ($freq as $c) {
            if ($c > 0) {
                $counts[] = $c;
            }
        }

        $distinct = count($counts);
        if ($distinct <= $k) {
            return 0;
        }

        sort($counts); // ascending order
        $needRemove = $distinct - $k;
        $ans = 0;
        for ($i = 0; $i < $needRemove; $i++) {
            $ans += $counts[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletion(_ s: String, _ k: Int) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97)
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        var counts = [Int]()
        for f in freq where f > 0 {
            counts.append(f)
        }
        let distinct = counts.count
        if distinct <= k { return 0 }
        counts.sort()
        var deletions = 0
        let needRemove = distinct - k
        for i in 0..<needRemove {
            deletions += counts[i]
        }
        return deletions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletion(s: String, k: Int): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val counts = mutableListOf<Int>()
        for (c in freq) if (c > 0) counts.add(c)
        var d = counts.size - k
        if (d <= 0) return 0
        counts.sort()
        var deletions = 0
        for (i in 0 until d) {
            deletions += counts[i]
        }
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minDeletion(String s, int k) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    List<int> counts = [];
    for (int f in freq) {
      if (f > 0) counts.add(f);
    }
    int distinct = counts.length;
    int d = distinct - k;
    if (d <= 0) return 0;
    counts.sort();
    int deletions = 0;
    for (int i = 0; i < d; ++i) {
      deletions += counts[i];
    }
    return deletions;
  }
}
```

## Golang

```go
package main

import "sort"

func minDeletion(s string, k int) int {
	freq := make([]int, 26)
	for _, ch := range s {
		freq[ch-'a']++
	}
	var counts []int
	for _, f := range freq {
		if f > 0 {
			counts = append(counts, f)
		}
	}
	distinct := len(counts)
	d := distinct - k
	if d <= 0 {
		return 0
	}
	sort.Ints(counts)
	deletions := 0
	for i := 0; i < d; i++ {
		deletions += counts[i]
	}
	return deletions
}
```

## Ruby

```ruby
def min_deletion(s, k)
  freq = Hash.new(0)
  s.each_char { |ch| freq[ch] += 1 }
  counts = freq.values.sort
  d = counts.size - k
  return 0 if d <= 0
  counts[0, d].sum
end
```

## Scala

```scala
object Solution {
    def minDeletion(s: String, k: Int): Int = {
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        val counts = freq.filter(_ > 0).sorted
        val distinct = counts.length
        if (distinct <= k) 0
        else {
            var deletions = 0
            val need = distinct - k
            for (i <- 0 until need) {
                deletions += counts(i)
            }
            deletions
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletion(s: String, k: i32) -> i32 {
        let mut freq = [0i32; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let mut counts: Vec<i32> = freq.iter().cloned().filter(|&x| x > 0).collect();
        let distinct = counts.len() as i32;
        let d = distinct - k;
        if d <= 0 {
            return 0;
        }
        counts.sort_unstable(); // ascending
        counts.iter().take(d as usize).sum()
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (min-deletion s k)
  (-> string? exact-integer? exact-integer?)
  (let* ([freq (make-vector 26 0)]
         [len (string-length s)])
    (for ([i (in-range len)])
      (let* ([c (string-ref s i)]
             [idx (- (char->integer c) (char->integer #\a))])
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    (define counts
      (filter positive?
              (for/list ([i (in-range 26)])
                (vector-ref freq i))))
    (define distinct (length counts))
    (if (<= distinct k)
        0
        (let* ([sorted (sort counts <)]
               [d (- distinct k)])
          (apply + (take sorted d))))))
```

## Erlang

```erlang
-module(solution).
-export([min_deletion/2]).

-spec min_deletion(S :: unicode:unicode_binary(), K :: integer()) -> integer().
min_deletion(S, K) ->
    CountsMap = build_counts(binary_to_list(S), #{}),
    Freqs = maps:values(CountsMap),
    Distinct = length(Freqs),
    case Distinct =< K of
        true -> 0;
        false ->
            D = Distinct - K,
            Sorted = lists:sort(Freqs),
            sum_first(Sorted, D)
    end.

build_counts([], Map) -> Map;
build_counts([C|Rest], Map) ->
    CharIdx = C - $a,
    Count = maps:get(CharIdx, Map, 0) + 1,
    build_counts(Rest, maps:put(CharIdx, Count, Map)).

sum_first(_, 0) -> 0;
sum_first([], _) -> 0;
sum_first([H|T], N) when N > 0 ->
    H + sum_first(T, N-1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletion(s :: String.t(), k :: integer()) :: integer()
  def min_deletion(s, k) do
    counts = s |> String.graphemes() |> Enum.frequencies() |> Map.values()
    d = length(counts) - k

    if d <= 0 do
      0
    else
      counts
      |> Enum.sort()
      |> Enum.take(d)
      |> Enum.sum()
    end
  end
end
```
