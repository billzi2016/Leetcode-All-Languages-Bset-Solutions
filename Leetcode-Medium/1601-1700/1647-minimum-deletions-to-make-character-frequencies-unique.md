# 1647. Minimum Deletions to Make Character Frequencies Unique

## Cpp

```cpp
class Solution {
public:
    int minDeletions(string s) {
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        sort(cnt.begin(), cnt.end(), greater<int>());
        int deletions = 0;
        int prev = INT_MAX;
        for (int f : cnt) {
            if (f == 0) break;
            int allowed = min(f, max(prev - 1, 0));
            deletions += f - allowed;
            prev = allowed;
        }
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minDeletions(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }
        java.util.List<Integer> freqs = new java.util.ArrayList<>();
        for (int f : cnt) {
            if (f > 0) freqs.add(f);
        }
        freqs.sort((a, b) -> b - a); // descending
        java.util.HashSet<Integer> used = new java.util.HashSet<>();
        int deletions = 0;
        for (int f : freqs) {
            while (f > 0 && used.contains(f)) {
                f--;
                deletions++;
            }
            if (f > 0) used.add(f);
        }
        return deletions;
    }
}
```

## Python

```python
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)
        used = set()
        deletions = 0

        for f in freq:
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            if f > 0:
                used.add(f)

        return deletions
```

## Python3

```python
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)
        used = set()
        deletions = 0

        for f in freq:
            while f > 0 and f in used:
                f -= 1
                deletions += 1
            if f > 0:
                used.add(f)

        return deletions
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

int minDeletions(char* s) {
    int freq[26] = {0};
    for (char *p = s; *p; ++p) {
        freq[*p - 'a']++;
    }

    int vals[26];
    int n = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > 0) {
            vals[n++] = freq[i];
        }
    }

    qsort(vals, n, sizeof(int), cmp_desc);

    int deletions = 0;
    int prev = vals[0];
    for (int i = 1; i < n; ++i) {
        if (vals[i] >= prev) {
            int target = prev > 0 ? prev - 1 : 0;
            deletions += vals[i] - target;
            vals[i] = target;
        }
        prev = vals[i];
    }

    return deletions;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDeletions(string s)
    {
        int[] freq = new int[26];
        foreach (char c in s)
            freq[c - 'a']++;

        Array.Sort(freq); // ascending

        var used = new HashSet<int>();
        int deletions = 0;

        for (int i = 25; i >= 0; i--)
        {
            int f = freq[i];
            while (f > 0 && used.Contains(f))
            {
                f--;
                deletions++;
            }
            if (f > 0)
                used.Add(f);
        }

        return deletions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function(s) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    freq.sort((a, b) => b - a); // descending
    const used = new Set();
    let deletions = 0;
    for (let f of freq) {
        while (f > 0 && used.has(f)) {
            f--;
            deletions++;
        }
        if (f > 0) used.add(f);
    }
    return deletions;
};
```

## Typescript

```typescript
function minDeletions(s: string): number {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    freq.sort((a, b) => b - a); // descending
    const used = new Set<number>();
    let deletions = 0;
    for (let f of freq) {
        while (f > 0 && used.has(f)) {
            f--;
            deletions++;
        }
        if (f > 0) used.add(f);
    }
    return deletions;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minDeletions($s) {
        $cnt = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($s[$i]) - ord('a');
            $cnt[$idx]++;
        }
        rsort($cnt); // descending order

        $deletions = 0;
        $prev = PHP_INT_MAX;

        foreach ($cnt as $f) {
            if ($f == 0) {
                break; // remaining frequencies are zero
            }
            if ($f >= $prev) {
                $newF = max(0, $prev - 1);
                $deletions += $f - $newF;
                $prev = $newF;
            } else {
                $prev = $f;
            }
        }

        return $deletions;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletions(_ s: String) -> Int {
        var counts = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97)
            if idx >= 0 && idx < 26 {
                counts[idx] += 1
            }
        }
        var frequencies = counts.filter { $0 > 0 }
        frequencies.sort(by: >)
        
        var used = Set<Int>()
        var deletions = 0
        
        for var f in frequencies {
            while f > 0 && used.contains(f) {
                f -= 1
                deletions += 1
            }
            if f > 0 {
                used.insert(f)
            }
        }
        return deletions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletions(s: String): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val list = mutableListOf<Int>()
        for (f in freq) if (f > 0) list.add(f)
        list.sortDescending()
        var deletions = 0
        var prev = Int.MAX_VALUE
        for (f in list) {
            var cur = f
            if (cur >= prev) {
                val target = if (prev > 0) prev - 1 else 0
                deletions += cur - target
                cur = target
            }
            prev = cur
        }
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minDeletions(String s) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    freq.sort((a, b) => b.compareTo(a));
    Set<int> used = {};
    int deletions = 0;
    for (int f in freq) {
      while (f > 0 && used.contains(f)) {
        f--;
        deletions++;
      }
      if (f > 0) used.add(f);
    }
    return deletions;
  }
}
```

## Golang

```go
import "sort"

func minDeletions(s string) int {
	freq := make([]int, 26)
	for _, ch := range s {
		freq[ch-'a']++
	}
	var arr []int
	for _, f := range freq {
		if f > 0 {
			arr = append(arr, f)
		}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i] > arr[j] })
	used := make(map[int]bool)
	deletions := 0
	for _, f := range arr {
		for f > 0 && used[f] {
			f--
			deletions++
		}
		if f > 0 {
			used[f] = true
		}
	}
	return deletions
}
```

## Ruby

```ruby
def min_deletions(s)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  freq.sort!.reverse!
  used = {}
  deletions = 0
  freq.each do |f|
    while f > 0 && used[f]
      f -= 1
      deletions += 1
    end
    used[f] = true if f > 0
  end
  deletions
end
```

## Scala

```scala
object Solution {
    def minDeletions(s: String): Int = {
        val counts = new Array[Int](26)
        for (c <- s) {
            counts(c - 'a') += 1
        }
        val freqs = counts.filter(_ > 0).sorted(Ordering.Int.reverse)
        var deletions = 0
        val used = scala.collection.mutable.HashSet[Int]()
        for (origFreq <- freqs) {
            var freq = origFreq
            while (freq > 0 && used.contains(freq)) {
                freq -= 1
                deletions += 1
            }
            if (freq > 0) used.add(freq)
        }
        deletions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut freqs: Vec<i32> = cnt.iter().cloned().filter(|&x| x > 0).collect();
        freqs.sort_unstable_by(|a, b| b.cmp(a)); // descending

        use std::collections::HashSet;
        let mut used = HashSet::new();
        let mut deletions = 0i32;

        for mut f in freqs {
            while f > 0 && used.contains(&f) {
                f -= 1;
                deletions += 1;
            }
            if f > 0 {
                used.insert(f);
            }
        }

        deletions
    }
}
```

## Racket

```racket
(define/contract (min-deletions s)
  (-> string? exact-integer?)
  (let* ([cnt (make-vector 26 0)])
    ;; count frequencies
    (for ([c (in-string s)])
      (let* ([idx (- (char->integer c) (char->integer #\a))])
        (vector-set! cnt idx (+ 1 (vector-ref cnt idx)))))
    (define freqs
      (filter positive? (vector->list cnt)))
    (define sorted-freqs (sort freqs >))
    (define used (make-hash))
    (define deletions 0)
    ;; ensure each frequency is unique
    (for ([f sorted-freqs])
      (let loop ((freq f))
        (cond [(= freq 0) (void)]
              [(hash-has-key? used freq)
               (set! deletions (+ deletions 1))
               (loop (- freq 1))]
              [else
               (hash-set! used freq #t)])))
    deletions)))
```

## Erlang

```erlang
-module(solution).
-export([min_deletions/1]).

-spec min_deletions(S :: unicode:unicode_binary()) -> integer().
min_deletions(S) ->
    CountsMap = count_chars(binary:bin_to_list(S), #{}),
    Freqs = maps:values(CountsMap),
    Sorted = lists:sort(fun(A, B) -> A > B end, Freqs),
    compute_deletions(Sorted, 1000000, 0).

count_chars([], Acc) ->
    Acc;
count_chars([C | Rest], Acc) ->
    Index = C - $a,
    NewAcc = maps:update_with(Index, fun(V) -> V + 1 end, 1, Acc),
    count_chars(Rest, NewAcc).

compute_deletions([], _Prev, Deletions) ->
    Deletions;
compute_deletions([F | Rest], Prev, Deletions) ->
    MaxAllowed = case Prev of
        0 -> 0;
        _ -> Prev - 1
    end,
    Allowed = if F > MaxAllowed -> MaxAllowed; true -> F end,
    NewDel = Deletions + (F - Allowed),
    compute_deletions(Rest, Allowed, NewDel).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletions(s :: String.t()) :: integer()
  def min_deletions(s) do
    counts =
      String.graphemes(s)
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    freqs = counts |> Map.values() |> Enum.sort(:desc)

    {_, deletions} =
      Enum.reduce(freqs, {MapSet.new(), 0}, fn freq, {used, del} ->
        {new_freq, added} = adjust(freq, used)
        new_used = if new_freq > 0, do: MapSet.put(used, new_freq), else: used
        {new_used, del + added}
      end)

    deletions
  end

  defp adjust(freq, used), do: adjust(freq, used, 0)

  defp adjust(0, _used, del), do: {0, del}

  defp adjust(f, used, del) do
    if MapSet.member?(used, f) do
      adjust(f - 1, used, del + 1)
    else
      {f, del}
    end
  end
end
```
