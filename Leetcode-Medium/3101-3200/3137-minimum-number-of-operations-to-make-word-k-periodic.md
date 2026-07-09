# 3137. Minimum Number of Operations to Make Word K-Periodic

## Cpp

```cpp
class Solution {
public:
    int minimumOperationsToMakeKPeriodic(string word, int k) {
        int n = word.size();
        int blocks = n / k;
        unordered_map<string, int> freq;
        int maxFreq = 0;
        for (int i = 0; i < n; i += k) {
            string sub = word.substr(i, k);
            int cnt = ++freq[sub];
            if (cnt > maxFreq) maxFreq = cnt;
        }
        return blocks - maxFreq;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        int n = word.length();
        int blocks = n / k;
        java.util.HashMap<String, Integer> freq = new java.util.HashMap<>();
        int maxFreq = 0;
        for (int i = 0; i < n; i += k) {
            String sub = word.substring(i, i + k);
            int cnt = freq.getOrDefault(sub, 0) + 1;
            freq.put(sub, cnt);
            if (cnt > maxFreq) {
                maxFreq = cnt;
            }
        }
        return blocks - maxFreq;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperationsToMakeKPeriodic(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        blocks = n // k
        freq = {}
        max_cnt = 0
        for b in range(blocks):
            sub = word[b*k:(b+1)*k]
            cnt = freq.get(sub, 0) + 1
            freq[sub] = cnt
            if cnt > max_cnt:
                max_cnt = cnt
        return blocks - max_cnt
```

## Python3

```python
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        from collections import Counter
        n = len(word)
        blocks = (word[i:i + k] for i in range(0, n, k))
        freq = Counter(blocks)
        max_freq = max(freq.values())
        total_blocks = n // k
        return total_blocks - max_freq
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int g_k;

static int cmp_substr(const void *a, const void *b) {
    const char *pa = *(const char **)a;
    const char *pb = *(const char **)b;
    return memcmp(pa, pb, (size_t)g_k);
}

int minimumOperationsToMakeKPeriodic(char* word, int k) {
    int n = (int)strlen(word);
    int blocks = n / k;
    const char **arr = (const char **)malloc(blocks * sizeof(const char *));
    for (int i = 0; i < blocks; ++i) {
        arr[i] = word + i * k;
    }
    g_k = k;
    qsort(arr, (size_t)blocks, sizeof(const char *), cmp_substr);
    
    int maxCnt = 1, curCnt = 1;
    for (int i = 1; i < blocks; ++i) {
        if (memcmp(arr[i], arr[i - 1], (size_t)k) == 0) {
            ++curCnt;
        } else {
            if (curCnt > maxCnt) maxCnt = curCnt;
            curCnt = 1;
        }
    }
    if (curCnt > maxCnt) maxCnt = curCnt;
    
    free(arr);
    return blocks - maxCnt;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperationsToMakeKPeriodic(string word, int k) {
        int n = word.Length;
        int blocks = n / k;
        var freq = new Dictionary<string, int>();
        int maxFreq = 0;
        for (int i = 0; i < n; i += k) {
            string sub = word.Substring(i, k);
            if (freq.TryGetValue(sub, out int cnt)) {
                cnt++;
                freq[sub] = cnt;
            } else {
                cnt = 1;
                freq[sub] = 1;
            }
            if (cnt > maxFreq) maxFreq = cnt;
        }
        return blocks - maxFreq;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumOperationsToMakeKPeriodic = function(word, k) {
    const n = word.length;
    const totalBlocks = n / k;
    const freqMap = new Map();
    let maxFreq = 0;
    for (let i = 0; i < n; i += k) {
        const sub = word.substring(i, i + k);
        const cnt = (freqMap.get(sub) || 0) + 1;
        freqMap.set(sub, cnt);
        if (cnt > maxFreq) maxFreq = cnt;
    }
    return totalBlocks - maxFreq;
};
```

## Typescript

```typescript
function minimumOperationsToMakeKPeriodic(word: string, k: number): number {
    const n = word.length;
    const totalBlocks = n / k;
    const freqMap = new Map<string, number>();
    let maxFreq = 0;

    for (let i = 0; i < n; i += k) {
        const block = word.substring(i, i + k);
        const count = (freqMap.get(block) ?? 0) + 1;
        freqMap.set(block, count);
        if (count > maxFreq) maxFreq = count;
    }

    return totalBlocks - maxFreq;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function minimumOperationsToMakeKPeriodic($word, $k) {
        $n = strlen($word);
        $totalBlocks = intdiv($n, $k);
        $freq = [];
        $maxFreq = 0;
        for ($i = 0; $i < $n; $i += $k) {
            $sub = substr($word, $i, $k);
            if (!isset($freq[$sub])) {
                $freq[$sub] = 0;
            }
            $freq[$sub]++;
            if ($freq[$sub] > $maxFreq) {
                $maxFreq = $freq[$sub];
            }
        }
        return $totalBlocks - $maxFreq;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minimumOperationsToMakeKPeriodic(_ word: String, _ k: Int) -> Int {
        let chars = Array(word)
        let n = chars.count
        var freq = [String: Int]()
        var maxCount = 0
        var i = 0
        while i < n {
            let subStr = String(chars[i..<i + k])
            let cnt = (freq[subStr] ?? 0) + 1
            freq[subStr] = cnt
            if cnt > maxCount { maxCount = cnt }
            i += k
        }
        let totalBlocks = n / k
        return totalBlocks - maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperationsToMakeKPeriodic(word: String, k: Int): Int {
        val n = word.length
        val blocks = n / k
        val freq = HashMap<String, Int>()
        var maxFreq = 0
        var i = 0
        while (i < n) {
            val sub = word.substring(i, i + k)
            val cnt = (freq[sub] ?: 0) + 1
            freq[sub] = cnt
            if (cnt > maxFreq) maxFreq = cnt
            i += k
        }
        return blocks - maxFreq
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperationsToMakeKPeriodic(String word, int k) {
    int n = word.length;
    int blocks = n ~/ k;
    Map<String, int> freq = {};
    for (int b = 0; b < blocks; ++b) {
      int start = b * k;
      String sub = word.substring(start, start + k);
      freq[sub] = (freq[sub] ?? 0) + 1;
    }
    int maxFreq = 0;
    for (var count in freq.values) {
      if (count > maxFreq) maxFreq = count;
    }
    return blocks - maxFreq;
  }
}
```

## Golang

```go
func minimumOperationsToMakeKPeriodic(word string, k int) int {
    n := len(word)
    blockCount := n / k
    freq := make(map[string]int, blockCount)

    maxFreq := 0
    for i := 0; i < n; i += k {
        sub := word[i : i+k]
        cnt := freq[sub] + 1
        freq[sub] = cnt
        if cnt > maxFreq {
            maxFreq = cnt
        }
    }

    return blockCount - maxFreq
}
```

## Ruby

```ruby
def minimum_operations_to_make_k_periodic(word, k)
  n = word.length
  total_blocks = n / k
  freq = Hash.new(0)
  i = 0
  while i < n
    block = word[i, k]
    freq[block] += 1
    i += k
  end
  max_freq = freq.values.max || 0
  total_blocks - max_freq
end
```

## Scala

```scala
object Solution {
    def minimumOperationsToMakeKPeriodic(word: String, k: Int): Int = {
        val n = word.length
        val totalBlocks = n / k
        val freq = scala.collection.mutable.Map[String, Int]()
        var maxFreq = 0
        var i = 0
        while (i < n) {
            val block = word.substring(i, i + k)
            val cnt = freq.getOrElse(block, 0) + 1
            freq.update(block, cnt)
            if (cnt > maxFreq) maxFreq = cnt
            i += k
        }
        totalBlocks - maxFreq
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations_to_make_k_periodic(word: String, k: i32) -> i32 {
        let k = k as usize;
        let n = word.len();
        use std::collections::HashMap;
        let mut count: HashMap<String, usize> = HashMap::new();

        for start in (0..n).step_by(k) {
            let sub = &word[start..start + k];
            *count.entry(sub.to_string()).or_insert(0) += 1;
        }

        let total_blocks = n / k;
        let max_freq = count.values().cloned().max().unwrap_or(0);
        (total_blocks - max_freq) as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-operations-to-make-k-periodic word k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length word))
         (total-blocks (quotient n k))
         (freq (make-hash)))
    (for ([i (in-range 0 n k)])
      (define sub (substring word i (+ i k)))
      (hash-set! freq sub (add1 (hash-ref freq sub 0))))
    (define max-freq
      (let loop ((keys (hash-keys freq)) (mx 0))
        (if (null? keys)
            mx
            (let* ((key (car keys))
                   (cnt (hash-ref freq key)))
              (loop (cdr keys) (max mx cnt))))))
    (- total-blocks max-freq)))
```

## Erlang

```erlang
-spec minimum_operations_to_make_k_periodic(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_operations_to_make_k_periodic(Word, K) ->
    N = byte_size(Word),
    Blocks = N div K,
    FreqMap = count_blocks(Word, K, 0, #{}, Blocks),
    MaxFreq = max_freq(FreqMap, 0),
    Blocks - MaxFreq.

count_blocks(_Word, _K, _Idx, Map, 0) ->
    Map;
count_blocks(Word, K, Idx, Map, Remaining) ->
    Sub = binary:part(Word, Idx, K),
    UpdatedMap = maps:update_with(Sub,
        fun(C) -> C + 1 end,
        1,
        Map),
    count_blocks(Word, K, Idx + K, UpdatedMap, Remaining - 1).

max_freq(Map, Acc) ->
    lists:foldl(fun({_Key, Val}, Max) ->
                        if Val > Max -> Val; true -> Max end
                end,
                Acc,
                maps:to_list(Map)).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations_to_make_k_periodic(String.t(), integer()) :: integer()
  def minimum_operations_to_make_k_periodic(word, k) do
    n = byte_size(word)
    total_blocks = div(n, k)

    freq_map =
      Enum.reduce(0..total_blocks - 1, %{}, fn i, acc ->
        start = i * k
        sub = :binary.part(word, start, k)
        Map.update(acc, sub, 1, &(&1 + 1))
      end)

    max_freq =
      freq_map
      |> Enum.map(fn {_sub, cnt} -> cnt end)
      |> Enum.max(fn -> 0 end)

    total_blocks - max_freq
  end
end
```
