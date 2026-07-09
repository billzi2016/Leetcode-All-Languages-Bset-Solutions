# 1297. Maximum Number of Occurrences of a Substring

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        unordered_map<string,int> freq;
        vector<int> cnt(26,0);
        int distinct = 0, ans = 0;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            int idxAdd = s[i] - 'a';
            if (cnt[idxAdd] == 0) ++distinct;
            ++cnt[idxAdd];
            
            if (i >= minSize) {
                int idxRemove = s[i - minSize] - 'a';
                --cnt[idxRemove];
                if (cnt[idxRemove] == 0) --distinct;
            }
            
            if (i >= minSize - 1) {
                if (distinct <= maxLetters) {
                    string sub = s.substr(i - minSize + 1, minSize);
                    int cur = ++freq[sub];
                    ans = max(ans, cur);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        Map<String, Integer> countMap = new HashMap<>();
        int[] freq = new int[26];
        int distinct = 0;
        int n = s.length();

        // Initialize the first window of size minSize
        for (int i = 0; i < minSize && i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (freq[idx] == 0) distinct++;
            freq[idx]++;
        }

        int maxOccur = 0;
        if (distinct <= maxLetters) {
            String sub = s.substring(0, minSize);
            int val = countMap.getOrDefault(sub, 0) + 1;
            countMap.put(sub, val);
            maxOccur = Math.max(maxOccur, val);
        }

        // Slide the window
        for (int i = minSize; i < n; i++) {
            // remove left character
            int outIdx = s.charAt(i - minSize) - 'a';
            freq[outIdx]--;
            if (freq[outIdx] == 0) distinct--;

            // add right character
            int inIdx = s.charAt(i) - 'a';
            if (freq[inIdx] == 0) distinct++;
            freq[inIdx]++;

            int start = i - minSize + 1;
            if (distinct <= maxLetters) {
                String sub = s.substring(start, start + minSize);
                int val = countMap.getOrDefault(sub, 0) + 1;
                countMap.put(sub, val);
                if (val > maxOccur) maxOccur = val;
            }
        }

        return maxOccur;
    }
}
```

## Python

```python
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        from collections import defaultdict

        n = len(s)
        counts = defaultdict(int)

        for i in range(n - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                counts[sub] += 1

        return max(counts.values() or [0])
```

## Python3

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        if minSize > n:
            return 0

        freq = [0] * 26
        distinct = 0
        counts = {}

        # initialize first window
        for i in range(minSize):
            idx = ord(s[i]) - 97
            if freq[idx] == 0:
                distinct += 1
            freq[idx] += 1

        if distinct <= maxLetters:
            sub = s[0:minSize]
            counts[sub] = counts.get(sub, 0) + 1

        # slide the window
        for start in range(1, n - minSize + 1):
            left_idx = ord(s[start - 1]) - 97
            freq[left_idx] -= 1
            if freq[left_idx] == 0:
                distinct -= 1

            right_idx = ord(s[start + minSize - 1]) - 97
            if freq[right_idx] == 0:
                distinct += 1
            freq[right_idx] += 1

            if distinct <= maxLetters:
                sub = s[start:start + minSize]
                counts[sub] = counts.get(sub, 0) + 1

        return max(counts.values() or [0])
```

## C

```c
#include <stdlib.h>
#include <string.h>

struct Node {
    char *key;
    int cnt;
    struct Node *next;
};

static unsigned long hash_str(const char *str, int len) {
    unsigned long h = 0;
    for (int i = 0; i < len; ++i) {
        h = h * 31 + (unsigned long)(str[i] - 'a' + 1);
    }
    return h;
}

int maxFreq(char* s, int maxLetters, int minSize, int maxSize) {
    int n = strlen(s);
    if (n < minSize) return 0;

    int len = minSize;                     // only need to consider minSize
    int freq[26] = {0};
    int distinct = 0;
    for (int i = 0; i < len; ++i) {
        int idx = s[i] - 'a';
        if (freq[idx] == 0) ++distinct;
        ++freq[idx];
    }

    const int MOD = 200003;                // prime > number of possible substrings
    struct Node **buckets = (struct Node **)calloc(MOD, sizeof(struct Node *));
    int maxCount = 0;

    for (int i = 0; i <= n - len; ++i) {
        if (distinct <= maxLetters) {
            char *sub = (char *)malloc(len + 1);
            memcpy(sub, s + i, len);
            sub[len] = '\0';

            unsigned long h = hash_str(sub, len);
            int idxb = (int)(h % MOD);
            struct Node *cur = buckets[idxb];
            while (cur) {
                if (strcmp(cur->key, sub) == 0) break;
                cur = cur->next;
            }
            if (cur) {
                ++cur->cnt;
                if (cur->cnt > maxCount) maxCount = cur->cnt;
                free(sub);
            } else {
                struct Node *node = (struct Node *)malloc(sizeof(struct Node));
                node->key = sub;
                node->cnt = 1;
                node->next = buckets[idxb];
                buckets[idxb] = node;
                if (maxCount < 1) maxCount = 1;
            }
        }

        // slide window
        if (i + len < n) {
            int outIdx = s[i] - 'a';
            --freq[outIdx];
            if (freq[outIdx] == 0) --distinct;

            int inIdx = s[i + len] - 'a';
            if (freq[inIdx] == 0) ++distinct;
            ++freq[inIdx];
        }
    }

    // clean up
    for (int i = 0; i < MOD; ++i) {
        struct Node *cur = buckets[i];
        while (cur) {
            struct Node *next = cur->next;
            free(cur->key);
            free(cur);
            cur = next;
        }
    }
    free(buckets);

    return maxCount;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxFreq(string s, int maxLetters, int minSize, int maxSize) {
        int n = s.Length;
        if (n < minSize) return 0;

        var freqMap = new Dictionary<string, int>();
        int[] charCount = new int[26];
        int distinct = 0;
        int maxFreq = 0;

        // Initialize first window
        for (int i = 0; i < minSize; i++) {
            int idx = s[i] - 'a';
            if (charCount[idx] == 0) distinct++;
            charCount[idx]++;
        }
        if (distinct <= maxLetters) {
            string sub = s.Substring(0, minSize);
            if (!freqMap.ContainsKey(sub)) freqMap[sub] = 0;
            freqMap[sub]++;
            if (freqMap[sub] > maxFreq) maxFreq = freqMap[sub];
        }

        // Slide the window
        for (int i = minSize; i < n; i++) {
            int leftIdx = s[i - minSize] - 'a';
            charCount[leftIdx]--;
            if (charCount[leftIdx] == 0) distinct--;

            int rightIdx = s[i] - 'a';
            if (charCount[rightIdx] == 0) distinct++;
            charCount[rightIdx]++;

            if (distinct <= maxLetters) {
                int start = i - minSize + 1;
                string sub = s.Substring(start, minSize);
                if (!freqMap.ContainsKey(sub)) freqMap[sub] = 0;
                freqMap[sub]++;
                if (freqMap[sub] > maxFreq) maxFreq = freqMap[sub];
            }
        }

        return maxFreq;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} maxLetters
 * @param {number} minSize
 * @param {number} maxSize
 * @return {number}
 */
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    const n = s.length;
    if (minSize > n) return 0;

    const freqMap = new Map();          // substring -> count
    const charCnt = new Array(26).fill(0);
    let unique = 0;

    // initialize first window of size minSize
    for (let i = 0; i < minSize; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (charCnt[idx] === 0) unique++;
        charCnt[idx]++;
    }
    if (unique <= maxLetters) {
        const sub = s.slice(0, minSize);
        freqMap.set(sub, (freqMap.get(sub) || 0) + 1);
    }

    // slide the window
    for (let i = minSize; i < n; ++i) {
        // remove left character
        let leftIdx = s.charCodeAt(i - minSize) - 97;
        charCnt[leftIdx]--;
        if (charCnt[leftIdx] === 0) unique--;

        // add right character
        const rightIdx = s.charCodeAt(i) - 97;
        if (charCnt[rightIdx] === 0) unique++;
        charCnt[rightIdx]++;

        if (unique <= maxLetters) {
            const sub = s.slice(i - minSize + 1, i + 1);
            freqMap.set(sub, (freqMap.get(sub) || 0) + 1);
        }
    }

    let ans = 0;
    for (const cnt of freqMap.values()) {
        if (cnt > ans) ans = cnt;
    }
    return ans;
};
```

## Typescript

```typescript
function maxFreq(s: string, maxLetters: number, minSize: number, maxSize: number): number {
    const n = s.length;
    if (n < minSize) return 0;

    const freqMap = new Map<string, number>();
    const charCnt = new Array(26).fill(0);
    let distinct = 0;
    let result = 0;

    // initialize first window of size minSize
    for (let i = 0; i < minSize; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (charCnt[idx] === 0) distinct++;
        charCnt[idx]++;
    }
    if (distinct <= maxLetters) {
        const sub = s.substring(0, minSize);
        const cnt = (freqMap.get(sub) ?? 0) + 1;
        freqMap.set(sub, cnt);
        result = Math.max(result, cnt);
    }

    // slide the window
    for (let i = 1; i + minSize - 1 < n; i++) {
        const leftIdx = s.charCodeAt(i - 1) - 97;
        charCnt[leftIdx]--;
        if (charCnt[leftIdx] === 0) distinct--;

        const rightIdx = s.charCodeAt(i + minSize - 1) - 97;
        if (charCnt[rightIdx] === 0) distinct++;
        charCnt[rightIdx]++;

        if (distinct <= maxLetters) {
            const sub = s.substring(i, i + minSize);
            const cnt = (freqMap.get(sub) ?? 0) + 1;
            freqMap.set(sub, cnt);
            result = Math.max(result, cnt);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $maxLetters
     * @param Integer $minSize
     * @param Integer $maxSize
     * @return Integer
     */
    function maxFreq($s, $maxLetters, $minSize, $maxSize) {
        $n = strlen($s);
        if ($n < $minSize) {
            return 0;
        }

        $freqMap = [];
        $charCount = array_fill(0, 26, 0);
        $unique = 0;
        $maxOccur = 0;

        // Initialize first window
        for ($i = 0; $i < $minSize; $i++) {
            $idx = ord($s[$i]) - 97;
            if ($charCount[$idx] == 0) {
                $unique++;
            }
            $charCount[$idx]++;
        }

        if ($unique <= $maxLetters) {
            $sub = substr($s, 0, $minSize);
            $freqMap[$sub] = ($freqMap[$sub] ?? 0) + 1;
            $maxOccur = max($maxOccur, $freqMap[$sub]);
        }

        // Slide the window
        for ($i = $minSize; $i < $n; $i++) {
            // Remove left character
            $leftIdx = ord($s[$i - $minSize]) - 97;
            $charCount[$leftIdx]--;
            if ($charCount[$leftIdx] == 0) {
                $unique--;
            }

            // Add right character
            $rightIdx = ord($s[$i]) - 97;
            if ($charCount[$rightIdx] == 0) {
                $unique++;
            }
            $charCount[$rightIdx]++;

            // Evaluate current window
            if ($unique <= $maxLetters) {
                $start = $i - $minSize + 1;
                $sub = substr($s, $start, $minSize);
                $freqMap[$sub] = ($freqMap[$sub] ?? 0) + 1;
                $maxOccur = max($maxOccur, $freqMap[$sub]);
            }
        }

        return $maxOccur;
    }
}
```

## Swift

```swift
class Solution {
    func maxFreq(_ s: String, _ maxLetters: Int, _ minSize: Int, _ maxSize: Int) -> Int {
        let bytes = Array(s.utf8)
        let n = bytes.count
        if n < minSize { return 0 }
        
        var charCount = [Int](repeating: 0, count: 26)
        var distinct = 0
        
        func add(_ c: UInt8) {
            let idx = Int(c - 97)
            if charCount[idx] == 0 { distinct += 1 }
            charCount[idx] += 1
        }
        
        func remove(_ c: UInt8) {
            let idx = Int(c - 97)
            charCount[idx] -= 1
            if charCount[idx] == 0 { distinct -= 1 }
        }
        
        // Initialize first window
        for i in 0..<minSize {
            add(bytes[i])
        }
        
        var freqMap = [String: Int]()
        var answer = 0
        
        if distinct <= maxLetters {
            let sub = String(decoding: bytes[0..<minSize], as: UTF8.self)
            freqMap[sub, default: 0] += 1
            answer = max(answer, freqMap[sub]!)
        }
        
        // Slide the window
        if n > minSize {
            for i in minSize..<n {
                remove(bytes[i - minSize])
                add(bytes[i])
                
                if distinct <= maxLetters {
                    let sub = String(decoding: bytes[(i - minSize + 1)...i], as: UTF8.self)
                    freqMap[sub, default: 0] += 1
                    answer = max(answer, freqMap[sub]!)
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int {
        val n = s.length
        if (n < minSize) return 0

        val freqMap = HashMap<String, Int>()
        val charCount = IntArray(26)
        var distinct = 0

        // Initialize first window of size minSize
        for (i in 0 until minSize) {
            val idx = s[i] - 'a'
            if (charCount[idx] == 0) distinct++
            charCount[idx]++
        }
        if (distinct <= maxLetters) {
            val sub = s.substring(0, minSize)
            freqMap[sub] = (freqMap[sub] ?: 0) + 1
        }

        // Slide the window
        for (i in minSize until n) {
            // remove left character
            val leftIdx = s[i - minSize] - 'a'
            charCount[leftIdx]--
            if (charCount[leftIdx] == 0) distinct--

            // add right character
            val rightIdx = s[i] - 'a'
            if (charCount[rightIdx] == 0) distinct++
            charCount[rightIdx]++

            if (distinct <= maxLetters) {
                val start = i - minSize + 1
                val sub = s.substring(start, start + minSize)
                freqMap[sub] = (freqMap[sub] ?: 0) + 1
            }
        }

        var answer = 0
        for (cnt in freqMap.values) {
            if (cnt > answer) answer = cnt
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
    final Map<String, int> freq = {};
    final int n = s.length;

    for (int i = 0; i + minSize <= n; ++i) {
      final String sub = s.substring(i, i + minSize);
      // count distinct letters in the substring
      final List<int> cnt = List.filled(26, 0);
      int distinct = 0;
      for (int j = 0; j < minSize; ++j) {
        final int idx = sub.codeUnitAt(j) - 97;
        if (cnt[idx] == 0) distinct++;
        cnt[idx]++;
      }
      if (distinct <= maxLetters) {
        freq[sub] = (freq[sub] ?? 0) + 1;
      }
    }

    int answer = 0;
    for (final v in freq.values) {
      if (v > answer) answer = v;
    }
    return answer;
  }
}
```

## Golang

```go
func maxFreq(s string, maxLetters int, minSize int, maxSize int) int {
    n := len(s)
    if n < minSize {
        return 0
    }

    freqMap := make(map[string]int)
    var cnt [26]int
    distinct := 0

    // Initialize first window of size minSize
    for i := 0; i < minSize; i++ {
        idx := int(s[i] - 'a')
        if cnt[idx] == 0 {
            distinct++
        }
        cnt[idx]++
    }
    if distinct <= maxLetters {
        sub := s[0:minSize]
        freqMap[sub]++
    }

    // Slide the window
    for i := 1; i+minSize <= n; i++ {
        leftIdx := int(s[i-1] - 'a')
        cnt[leftIdx]--
        if cnt[leftIdx] == 0 {
            distinct--
        }

        rightIdx := int(s[i+minSize-1] - 'a')
        if cnt[rightIdx] == 0 {
            distinct++
        }
        cnt[rightIdx]++

        if distinct <= maxLetters {
            sub := s[i : i+minSize]
            freqMap[sub]++
        }
    }

    // Find maximum frequency
    ans := 0
    for _, v := range freqMap {
        if v > ans {
            ans = v
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_freq(s, max_letters, min_size, max_size)
  n = s.length
  freq = Hash.new(0)
  cnt = Array.new(26, 0)
  unique = 0

  # initialize first window
  (0...min_size).each do |i|
    idx = s.getbyte(i) - 97
    unique += 1 if cnt[idx] == 0
    cnt[idx] += 1
  end
  if unique <= max_letters
    freq[s[0, min_size]] += 1
  end

  (min_size...n).each do |i|
    left_idx = s.getbyte(i - min_size) - 97
    cnt[left_idx] -= 1
    unique -= 1 if cnt[left_idx] == 0

    right_idx = s.getbyte(i) - 97
    unique += 1 if cnt[right_idx] == 0
    cnt[right_idx] += 1

    if unique <= max_letters
      start = i - min_size + 1
      freq[s[start, min_size]] += 1
    end
  end

  freq.values.max || 0
end
```

## Scala

```scala
object Solution {
    def maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int = {
        import scala.collection.mutable

        val n = s.length
        if (n < minSize) return 0

        val countMap = mutable.Map[String, Int]()
        var answer = 0

        for (i <- 0 to n - minSize) {
            val sub = s.substring(i, i + minSize)

            // Count distinct letters in the substring
            val seen = new Array[Boolean](26)
            var distinct = 0
            var j = 0
            while (j < minSize) {
                val idx = sub.charAt(j) - 'a'
                if (!seen(idx)) {
                    seen(idx) = true
                    distinct += 1
                }
                j += 1
            }

            if (distinct <= maxLetters) {
                val newCnt = countMap.getOrElse(sub, 0) + 1
                countMap.update(sub, newCnt)
                if (newCnt > answer) answer = newCnt
            }
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_freq(s: String, max_letters: i32, min_size: i32, _max_size: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k = min_size as usize;
        if k == 0 || k > n {
            return 0;
        }

        let mut cnt = [0usize; 26];
        let mut distinct = 0usize;

        for &b in &bytes[0..k] {
            let idx = (b - b'a') as usize;
            if cnt[idx] == 0 {
                distinct += 1;
            }
            cnt[idx] += 1;
        }

        use std::collections::HashMap;
        let mut map: HashMap<Vec<u8>, i32> = HashMap::new();

        if distinct <= max_letters as usize {
            *map.entry(bytes[0..k].to_vec()).or_insert(0) += 1;
        }

        for i in k..n {
            // remove left character
            let left = bytes[i - k];
            let idx_left = (left - b'a') as usize;
            cnt[idx_left] -= 1;
            if cnt[idx_left] == 0 {
                distinct -= 1;
            }
            // add right character
            let right = bytes[i];
            let idx_right = (right - b'a') as usize;
            if cnt[idx_right] == 0 {
                distinct += 1;
            }
            cnt[idx_right] += 1;

            if distinct <= max_letters as usize {
                let sub = bytes[i - k + 1..i + 1].to_vec();
                *map.entry(sub).or_insert(0) += 1;
            }
        }

        let mut ans = 0i32;
        for &v in map.values() {
            if v > ans {
                ans = v;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-freq s maxLetters minSize maxSize)
  (-> string? exact-integer? exact-integer? exact-integer? exact-integer?)
  (let ([n (string-length s)])
    (if (< n minSize)
        0
        (let* ([cnt (make-vector 26 0)]
               [distinct 0]
               [ht (make-hash)])
          ;; initial window of size minSize
          (for ([i (in-range minSize)])
            (let* ([c (string-ref s i)]
                   [idx (- (char->integer c) (char->integer #\a))])
              (when (= (vector-ref cnt idx) 0)
                (set! distinct (+ distinct 1)))
              (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
          ;; check first window
          (when (<= distinct maxLetters)
            (let ([sub (substring s 0 minSize)])
              (hash-set! ht sub (+ 1 (hash-ref ht sub 0)))))
          ;; slide the window across the string
          (for ([i (in-range minSize n)])
            ;; remove leftmost character
            (let* ([out-pos (- i minSize)]
                   [c-out (string-ref s out-pos)]
                   [idx-out (- (char->integer c-out) (char->integer #\a))])
              (vector-set! cnt idx-out (- (vector-ref cnt idx-out) 1))
              (when (= (vector-ref cnt idx-out) 0)
                (set! distinct (- distinct 1))))
            ;; add new character
            (let* ([c-in (string-ref s i)]
                   [idx-in (- (char->integer c-in) (char->integer #\a))])
              (when (= (vector-ref cnt idx-in) 0)
                (set! distinct (+ distinct 1)))
              (vector-set! cnt idx-in (+ (vector-ref cnt idx-in) 1)))
            ;; evaluate current window
            (let ([start (+ (- i minSize) 1)])
              (when (<= distinct maxLetters)
                (let ([sub (substring s start (+ start minSize))])
                  (hash-set! ht sub (+ 1 (hash-ref ht sub 0)))))))
          ;; find maximum frequency
          (let ([max 0])
            (hash-for-each ht (lambda (_ v) (when (> v max) (set! max v))))
            max)))))
```

## Erlang

```erlang
-module(solution).
-export([max_freq/4]).

-spec max_freq(S :: unicode:unicode_binary(), MaxLetters :: integer(), MinSize :: integer(), MaxSize :: integer()) -> integer().
max_freq(S, MaxLetters, MinSize, _MaxSize) ->
    L = binary_to_list(S),
    N = length(L),
    loop(0, N, MinSize, MaxLetters, L, #{}, 0).

loop(I, N, MinSize, MaxLetters, L, Map, MaxFreq) when I =< N - MinSize ->
    Sublist = lists:sublist(L, I + 1, MinSize),
    Distinct = length(lists:usort(Sublist)),
    case Distinct =< MaxLetters of
        true ->
            SubBin = list_to_binary(Sublist),
            Count0 = maps:get(SubBin, Map, 0) + 1,
            NewMap = maps:put(SubBin, Count0, Map),
            NewMax = if Count0 > MaxFreq -> Count0; true -> MaxFreq end,
            loop(I + 1, N, MinSize, MaxLetters, L, NewMap, NewMax);
        false ->
            loop(I + 1, N, MinSize, MaxLetters, L, Map, MaxFreq)
    end;
loop(_, _, _, _, _, _, MaxFreq) -> MaxFreq.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_freq(s :: String.t(), max_letters :: integer, min_size :: integer, max_size :: integer) :: integer
  def max_freq(s, max_letters, min_size, _max_size) do
    n = byte_size(s)

    if n < min_size do
      0
    else
      arr = :array.from_list(:binary.bin_to_list(s))
      counts = :erlang.make_tuple(26, 0)
      {counts, distinct} = init_counts(arr, min_size, counts, 0)

      freq_map =
        if distinct <= max_letters do
          sub = :binary.part(s, 0, min_size)
          %{sub => 1}
        else
          %{}
        end

      if n == min_size do
        max_from_map(freq_map)
      else
        {final_map, _cnts, _dist} =
          Enum.reduce(1..(n - min_size), {freq_map, counts, distinct}, fn i,
                                                                          {m, cnts, dist} ->
            out_ch = :array.get(i - 1, arr)
            in_ch = :array.get(i + min_size - 1, arr)

            # remove outgoing character
            idx_out = out_ch - ?a
            cnt_out = elem(cnts, idx_out)
            cnts = put_elem(cnts, idx_out, cnt_out - 1)
            dist = if cnt_out == 1, do: dist - 1, else: dist

            # add incoming character
            idx_in = in_ch - ?a
            cnt_in = elem(cnts, idx_in)
            cnts = put_elem(cnts, idx_in, cnt_in + 1)
            dist = if cnt_in == 0, do: dist + 1, else: dist

            sub = :binary.part(s, i, min_size)

            m =
              if dist <= max_letters do
                Map.update(m, sub, 1, &(&1 + 1))
              else
                m
              end

            {m, cnts, dist}
          end)

        max_from_map(final_map)
      end
    end
  end

  defp init_counts(arr, size, counts, distinct) do
    Enum.reduce(0..(size - 1), {counts, distinct}, fn i, {cnts, dist} ->
      ch = :array.get(i, arr)
      idx = ch - ?a
      cur = elem(cnts, idx)
      cnts = put_elem(cnts, idx, cur + 1)
      dist = if cur == 0, do: dist + 1, else: dist
      {cnts, dist}
    end)
  end

  defp max_from_map(map) do
    case map do
      %{} -> 0
      _ -> map |> Map.values() |> Enum.max()
    end
  end
end
```
