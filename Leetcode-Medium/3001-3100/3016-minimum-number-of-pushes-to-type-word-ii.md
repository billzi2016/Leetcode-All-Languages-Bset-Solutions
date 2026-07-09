# 3016. Minimum Number of Pushes to Type Word II

## Cpp

```cpp
class Solution {
public:
    int minimumPushes(string word) {
        vector<int> freq(26, 0);
        for (char c : word) ++freq[c - 'a'];
        sort(freq.begin(), freq.end(), greater<int>());
        long long total = 0;
        for (int i = 0; i < 26 && freq[i] > 0; ++i) {
            int presses = i / 8 + 1;
            total += 1LL * presses * freq[i];
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++) {
            freq[word.charAt(i) - 'a']++;
        }
        Arrays.sort(freq); // ascending
        int pushes = 0;
        int idx = 0; // position in sorted descending order
        for (int i = 25; i >= 0 && freq[i] > 0; i--) {
            pushes += freq[i] * ((idx / 8) + 1);
            idx++;
        }
        return pushes;
    }
}
```

## Python

```python
class Solution:
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        freq.sort(reverse=True)
        total = 0
        for i, f in enumerate(freq):
            if f == 0:
                break
            total += (i // 8 + 1) * f
        return total
```

## Python3

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1
        freq.sort(reverse=True)
        total = 0
        for i, f in enumerate(freq):
            if f == 0:
                break
            total += (i // 8 + 1) * f
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

int minimumPushes(char* word) {
    int freq[26] = {0};
    for (char *p = word; *p; ++p) {
        freq[*p - 'a']++;
    }

    int arr[26];
    for (int i = 0; i < 26; ++i) arr[i] = freq[i];

    qsort(arr, 26, sizeof(int), cmp_desc);

    long long total = 0;
    for (int i = 0; i < 26 && arr[i] > 0; ++i) {
        int presses = i / 8 + 1;
        total += (long long)presses * arr[i];
    }

    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPushes(string word) {
        int[] count = new int[26];
        foreach (char c in word) {
            count[c - 'a']++;
        }

        List<int> freqs = new List<int>();
        for (int i = 0; i < 26; i++) {
            if (count[i] > 0) freqs.Add(count[i]);
        }
        freqs.Sort((a, b) => b.CompareTo(a)); // descending

        int total = 0;
        for (int i = 0; i < freqs.Count; i++) {
            int presses = i / 8 + 1;
            total += presses * freqs[i];
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        freq[word.charCodeAt(i) - 97]++;
    }
    freq.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < freq.length && freq[i] > 0; i++) {
        const presses = Math.floor(i / 8) + 1;
        total += presses * freq[i];
    }
    return total;
};
```

## Typescript

```typescript
function minimumPushes(word: string): number {
    const freq = new Array(26).fill(0);
    for (const ch of word) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    freq.sort((a, b) => b - a);
    let total = 0;
    for (let i = 0; i < 26 && freq[i] > 0; i++) {
        const pushes = Math.floor(i / 8) + 1;
        total += pushes * freq[i];
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function minimumPushes($word) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($word[$i]) - 97;
            if ($idx >= 0 && $idx < 26) {
                $freq[$idx]++;
            }
        }
        rsort($freq);
        $total = 0;
        foreach ($freq as $i => $cnt) {
            if ($cnt == 0) break;
            $presses = intdiv($i, 8) + 1;
            $total += $presses * $cnt;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPushes(_ word: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for byte in word.utf8 {
            let idx = Int(byte - 97) // 'a' ASCII is 97
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        let sortedFreq = freq.sorted(by: >)
        var total = 0
        for (i, f) in sortedFreq.enumerated() where f > 0 {
            total += (i / 8 + 1) * f
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPushes(word: String): Int {
        val freq = IntArray(26)
        for (c in word) {
            freq[c - 'a']++
        }
        val list = mutableListOf<Int>()
        for (v in freq) if (v > 0) list.add(v)
        list.sortDescending()
        var total = 0L
        for (i in list.indices) {
            val presses = i / 8 + 1
            total += list[i].toLong() * presses
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumPushes(String word) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < word.length; i++) {
      int idx = word.codeUnitAt(i) - 97;
      if (idx >= 0 && idx < 26) freq[idx]++;
    }
    List<int> counts = [];
    for (int f in freq) {
      if (f > 0) counts.add(f);
    }
    counts.sort((a, b) => b.compareTo(a));
    int total = 0;
    for (int i = 0; i < counts.length; i++) {
      int pushes = (i ~/ 8) + 1;
      total += pushes * counts[i];
    }
    return total;
  }
}
```

## Golang

```go
package main

import "sort"

func minimumPushes(word string) int {
	freq := make([]int, 26)
	for _, ch := range word {
		freq[ch-'a']++
	}
	// collect non-zero frequencies
	var counts []int
	for _, v := range freq {
		if v > 0 {
			counts = append(counts, v)
		}
	}
	sort.Slice(counts, func(i, j int) bool { return counts[i] > counts[j] })
	total := 0
	for i, c := range counts {
		pushes := (i/8 + 1) * c
		total += pushes
	}
	return total
}
```

## Ruby

```ruby
def minimum_pushes(word)
  counts = Array.new(26, 0)
  word.each_byte { |b| counts[b - 97] += 1 }
  freqs = counts.sort.reverse
  total = 0
  freqs.each_with_index do |f, i|
    break if f == 0
    total += (i / 8 + 1) * f
  end
  total
end
```

## Scala

```scala
object Solution {
  def minimumPushes(word: String): Int = {
    val freq = new Array[Int](26)
    for (c <- word) {
      freq(c - 'a') += 1
    }
    java.util.Arrays.sort(freq) // ascending order
    var total: Long = 0L
    var pos = 0
    var i = 25
    while (i >= 0 && freq(i) > 0) {
      total += ((pos / 8 + 1).toLong * freq(i))
      pos += 1
      i -= 1
    }
    total.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut cnt = [0i32; 26];
        for b in word.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut freqs: Vec<i32> = cnt.iter().cloned().filter(|&x| x > 0).collect();
        freqs.sort_unstable_by(|a, b| b.cmp(a));
        let mut total: i64 = 0;
        for (i, f) in freqs.iter().enumerate() {
            let pushes = (i / 8 + 1) as i64;
            total += (*f as i64) * pushes;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-pushes word)
  (-> string? exact-integer?)
  (let* ([freqs (make-vector 26 0)]
         [len   (string-length word)])
    ;; count frequencies
    (for ([i (in-range len)])
      (let* ([c   (string-ref word i)]
             [idx (- (char->integer c) (char->integer #\a))])
        (vector-set! freqs idx (+ 1 (vector-ref freqs idx)))))
    ;; collect non‑zero frequencies
    (define freq-list
      (for/list ([i (in-range 26)]
                 #:when (> (vector-ref freqs i) 0))
        (vector-ref freqs i)))
    ;; sort descending
    (define sorted-freqs (sort freq-list >))
    ;; compute total pushes
    (let loop ((lst sorted-freqs) (idx 0) (total 0))
      (if (null? lst)
          total
          (let* ([f       (car lst)]
                 [presses (+ 1 (quotient idx 8))]
                 [add     (* f presses)])
            (loop (cdr lst) (add1 idx) (+ total add)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_pushes/1]).

-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().
minimum_pushes(Word) ->
    Freq0 = erlang:make_tuple(26, 0),
    Freq = count_freq(Word, Freq0),
    List = [element(I, Freq) || I <- lists:seq(1, 26), element(I, Freq) > 0],
    Sorted = lists:reverse(lists:sort(List)),
    {_, Total} = lists:foldl(
        fun(F, {Idx, Acc}) ->
            Pushes = (Idx div 8 + 1) * F,
            {Idx + 1, Acc + Pushes}
        end,
        {0, 0},
        Sorted),
    Total.

count_freq(<<>>, Freq) -> Freq;
count_freq(<<C, Rest/binary>>, Freq) ->
    Index = C - $a + 1,
    Count = element(Index, Freq),
    NewFreq = setelement(Index, Freq, Count + 1),
    count_freq(Rest, NewFreq).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_pushes(word :: String.t) :: integer
  def minimum_pushes(word) do
    freqs =
      word
      |> String.to_charlist()
      |> Enum.reduce(%{}, fn c, acc -> Map.update(acc, c, 1, &(&1 + 1)) end)
      |> Map.values()
      |> Enum.sort(:desc)

    {total, _} = Enum.reduce(freqs, {0, 0}, fn f, {sum, idx} ->
      pushes = div(idx, 8) + 1
      {sum + pushes * f, idx + 1}
    end)

    total
  end
end
```
