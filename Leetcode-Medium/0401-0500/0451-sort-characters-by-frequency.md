# 0451. Sort Characters By Frequency

## Cpp

```cpp
class Solution {
public:
    string frequencySort(string s) {
        int cnt[256] = {0};
        for (unsigned char c : s) ++cnt[c];
        vector<pair<char,int>> v;
        v.reserve(128);
        for (int i = 0; i < 256; ++i) {
            if (cnt[i]) v.emplace_back(static_cast<char>(i), cnt[i]);
        }
        sort(v.begin(), v.end(), [](const pair<char,int>& a, const pair<char,int>& b){
            return a.second > b.second;
        });
        string res;
        res.reserve(s.size());
        for (auto& p : v) {
            res.append(p.second, p.first);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String frequencySort(String s) {
        int[] freq = new int[128];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i)]++;
        }
        int maxFreq = 0;
        for (int f : freq) {
            if (f > maxFreq) maxFreq = f;
        }
        StringBuilder[] buckets = new StringBuilder[maxFreq + 1];
        for (int c = 0; c < 128; c++) {
            int f = freq[c];
            if (f > 0) {
                if (buckets[f] == null) buckets[f] = new StringBuilder();
                for (int i = 0; i < f; i++) {
                    buckets[f].append((char) c);
                }
            }
        }
        StringBuilder result = new StringBuilder(s.length());
        for (int f = maxFreq; f > 0; f--) {
            if (buckets[f] != null) {
                result.append(buckets[f]);
            }
        }
        return result.toString();
    }
}
```

## Python

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        freq = Counter(s)
        # Sort characters by decreasing frequency
        sorted_items = sorted(freq.items(), key=lambda x: -x[1])
        return ''.join([ch * cnt for ch, cnt in sorted_items])
```

## Python3

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        return ''.join(ch * freq for ch, freq in sorted(cnt.items(), key=lambda x: -x[1]))
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char ch;
    int cnt;
} CharFreq;

static int cmpDesc(const void *a, const void *b) {
    const CharFreq *fa = (const CharFreq *)a;
    const CharFreq *fb = (const CharFreq *)b;
    return fb->cnt - fa->cnt; // descending
}

char* frequencySort(char* s) {
    if (!s) return NULL;
    int n = strlen(s);
    int freq[256] = {0};
    for (int i = 0; i < n; ++i) {
        unsigned char uc = (unsigned char)s[i];
        ++freq[uc];
    }

    CharFreq arr[256];
    int m = 0;
    for (int i = 0; i < 256; ++i) {
        if (freq[i] > 0) {
            arr[m].ch = (char)i;
            arr[m].cnt = freq[i];
            ++m;
        }
    }

    qsort(arr, m, sizeof(CharFreq), cmpDesc);

    char *res = (char *)malloc(n + 1);
    if (!res) return NULL;
    int pos = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < arr[i].cnt; ++j) {
            res[pos++] = arr[i].ch;
        }
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string FrequencySort(string s) {
        int[] freq = new int[128];
        foreach (char c in s) {
            freq[c]++;
        }

        List<char> chars = new List<char>();
        for (int i = 0; i < freq.Length; i++) {
            if (freq[i] > 0) chars.Add((char)i);
        }

        chars.Sort((a, b) => freq[b] - freq[a]);

        StringBuilder sb = new StringBuilder(s.Length);
        foreach (char c in chars) {
            int count = freq[c];
            for (int i = 0; i < count; i++) {
                sb.Append(c);
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    const freq = new Map();
    for (const ch of s) {
        freq.set(ch, (freq.get(ch) || 0) + 1);
    }
    const entries = Array.from(freq.entries());
    entries.sort((a, b) => b[1] - a[1]);
    let result = '';
    for (const [ch, count] of entries) {
        result += ch.repeat(count);
    }
    return result;
};
```

## Typescript

```typescript
function frequencySort(s: string): string {
    const freq = new Map<string, number>();
    for (const ch of s) {
        freq.set(ch, (freq.get(ch) ?? 0) + 1);
    }
    const entries = Array.from(freq.entries());
    entries.sort((a, b) => b[1] - a[1]);
    const parts: string[] = [];
    for (const [ch, count] of entries) {
        parts.push(ch.repeat(count));
    }
    return parts.join('');
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function frequencySort($s) {
        $len = strlen($s);
        $freq = [];
        $max = 0;
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($freq[$c])) {
                $freq[$c] = 1;
            } else {
                $freq[$c]++;
            }
            if ($freq[$c] > $max) {
                $max = $freq[$c];
            }
        }

        $buckets = array_fill(0, $max + 1, '');
        foreach ($freq as $char => $count) {
            $buckets[$count] .= str_repeat($char, $count);
        }

        $result = '';
        for ($i = $max; $i >= 1; $i--) {
            if ($buckets[$i] !== '') {
                $result .= $buckets[$i];
            }
        }
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func frequencySort(_ s: String) -> String {
        var freq = [Character: Int]()
        for ch in s {
            freq[ch, default: 0] += 1
        }
        let sortedChars = freq.keys.sorted { (freq[$0] ?? 0) > (freq[$1] ?? 0) }
        var result = ""
        result.reserveCapacity(s.count)
        for ch in sortedChars {
            if let count = freq[ch] {
                result += String(repeating: String(ch), count: count)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun frequencySort(s: String): String {
        val freq = HashMap<Char, Int>()
        for (c in s) {
            freq[c] = (freq[c] ?: 0) + 1
        }
        val sortedChars = freq.entries.sortedByDescending { it.value }
        val sb = StringBuilder(s.length)
        for ((ch, count) in sortedChars) {
            repeat(count) { sb.append(ch) }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String frequencySort(String s) {
    final Map<String, int> freq = {};
    for (int i = 0; i < s.length; ++i) {
      final ch = s[i];
      freq[ch] = (freq[ch] ?? 0) + 1;
    }
    final entries = freq.entries.toList()
      ..sort((a, b) => b.value.compareTo(a.value));
    final sb = StringBuffer();
    for (final e in entries) {
      for (int i = 0; i < e.value; ++i) {
        sb.write(e.key);
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func frequencySort(s string) string {
    if len(s) == 0 {
        return ""
    }
    freq := make(map[byte]int, 128)
    for i := 0; i < len(s); i++ {
        freq[s[i]]++
    }

    type pair struct {
        ch  byte
        cnt int
    }
    pairs := make([]pair, 0, len(freq))
    for ch, cnt := range freq {
        pairs = append(pairs, pair{ch, cnt})
    }

    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i].cnt > pairs[j].cnt
    })

    var sb strings.Builder
    sb.Grow(len(s))
    for _, p := range pairs {
        for i := 0; i < p.cnt; i++ {
            sb.WriteByte(p.ch)
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def frequency_sort(s)
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  freq.sort_by { |_, count| -count }.map { |char, count| char * count }.join
end
```

## Scala

```scala
object Solution {
    def frequencySort(s: String): String = {
        val freq = scala.collection.mutable.Map[Char, Int]()
        s.foreach { c =>
            freq(c) = freq.getOrElse(c, 0) + 1
        }
        val sorted = freq.toSeq.sortWith { case ((_, f1), (_, f2)) => f1 > f2 }
        val sb = new StringBuilder(s.length)
        for ((ch, count) <- sorted) {
            var i = 0
            while (i < count) {
                sb.append(ch)
                i += 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut counts = [0usize; 128];
        for &b in s.as_bytes() {
            counts[b as usize] += 1;
        }
        let n = s.len();
        let mut bucket: Vec<Vec<u8>> = vec![Vec::new(); n + 1];
        for i in 0..128 {
            let cnt = counts[i];
            if cnt > 0 {
                bucket[cnt].push(i as u8);
            }
        }
        let mut result = String::with_capacity(n);
        for freq in (1..=n).rev() {
            for &ch in &bucket[freq] {
                for _ in 0..freq {
                    result.push(ch as char);
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (frequency-sort s)
  (-> string? string?)
  (let* ([freq (make-hash)])
    (for ([ch (in-string s)])
      (hash-set! freq ch (+ 1 (hash-ref freq ch 0))))
    (define pairs (hash->list freq))
    (define sorted-pairs
      (sort pairs (lambda (a b) (> (cdr a) (cdr b)))))
    (let ([out (open-output-string)])
      (for ([pair sorted-pairs])
        (define ch (car pair))
        (define cnt (cdr pair))
        (for ([i (in-range cnt)])
          (write-char ch out)))
      (get-output-string out))))
```

## Erlang

```erlang
-module(solution).
-export([frequency_sort/1]).

-spec frequency_sort(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
frequency_sort(S) ->
    CountMap = count_chars(binary_to_list(S), #{}),
    Sorted = lists:sort(fun({_, C1}, {_, C2}) -> C1 > C2 end, maps:to_list(CountMap)),
    Iolist = build_iolist(Sorted),
    iolist_to_binary(Iolist).

count_chars([], Map) ->
    Map;
count_chars([C|Rest], Map) ->
    NewMap = maps:update_with(C,
                              fun(V) -> V + 1 end,
                              1,
                              Map),
    count_chars(Rest, NewMap).

build_iolist([]) ->
    [];
build_iolist(Pairs) ->
    lists:foldr(fun({C,N}, Acc) -> [lists:duplicate(N, C) | Acc] end, [], Pairs).
```

## Elixir

```elixir
defmodule Solution do
  @spec frequency_sort(s :: String.t) :: String.t
  def frequency_sort(s) do
    freq =
      s
      |> :binary.bin_to_list()
      |> Enum.reduce(%{}, fn c, acc ->
        Map.update(acc, c, 1, &(&1 + 1))
      end)

    sorted =
      freq
      |> Enum.to_list()
      |> Enum.sort_by(fn {_c, f} -> -f end)

    bytes = Enum.flat_map(sorted, fn {c, f} -> :lists.duplicate(f, c) end)
    :binary.list_to_bin(bytes)
  end
end
```
