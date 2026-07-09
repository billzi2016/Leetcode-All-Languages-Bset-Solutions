# 3045. Count Prefix and Suffix Pairs II

## Cpp

```cpp
class Solution {
public:
    long long countPrefixSuffixPairs(std::vector<std::string>& words) {
        const unsigned long long BASE = 1315423911ULL;
        std::unordered_map<unsigned long long, long long> cnt;
        cnt.reserve(words.size() * 2);
        long long ans = 0;
        for (const std::string& w : words) {
            int m = w.size();
            // prefix function
            std::vector<int> pi(m);
            for (int i = 1; i < m; ++i) {
                int j = pi[i - 1];
                while (j > 0 && w[i] != w[j]) j = pi[j - 1];
                if (w[i] == w[j]) ++j;
                pi[i] = j;
            }
            // rolling hash prefix
            std::vector<unsigned long long> pref(m + 1, 0);
            for (int i = 0; i < m; ++i) {
                pref[i + 1] = pref[i] * BASE + static_cast<unsigned long long>(w[i] - 'a' + 1);
            }
            unsigned long long fullHash = pref[m];
            // count identical previous words
            auto itFull = cnt.find(fullHash);
            if (itFull != cnt.end()) ans += itFull->second;
            // count borders
            int l = pi.empty() ? 0 : pi[m - 1];
            while (l > 0) {
                unsigned long long h = pref[l];
                auto it = cnt.find(h);
                if (it != cnt.end()) ans += it->second;
                l = pi[l - 1];
            }
            // insert current word
            ++cnt[fullHash];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countPrefixSuffixPairs(String[] words) {
        Node root = new Node();
        long ans = 0;
        for (String w : words) {
            Node cur = root;
            int l = 0, r = w.length() - 1;
            while (l <= r) {
                int key = (w.charAt(l) - 'a') * 26 + (w.charAt(r) - 'a');
                if (cur.next == null) {
                    cur.next = new java.util.HashMap<>();
                }
                Node nxt = cur.next.get(key);
                if (nxt == null) {
                    nxt = new Node();
                    cur.next.put(key, nxt);
                }
                ans += nxt.cnt;
                cur = nxt;
                l++;
                r--;
            }
            cur.cnt++;
        }
        return ans;
    }

    private static class Node {
        int cnt = 0;
        java.util.Map<Integer, Node> next = null;
    }
}
```

## Python

```python
class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict

        def border_lengths(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            res = []
            l = n
            while l:
                res.append(l)
                l = pi[l - 1]
            return res

        cnt = defaultdict(int)
        ans = 0
        for w in words:
            for L in border_lengths(w):
                prefix = w[:L]
                ans += cnt[prefix]
            cnt[w] += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        base = 91138233
        MASK = (1 << 64) - 1
        cnt = {}
        ans = 0

        for w in words:
            n = len(w)
            # KMP prefix function
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and w[i] != w[j]:
                    j = pi[j - 1]
                if w[i] == w[j]:
                    j += 1
                pi[i] = j

            # rolling hash for prefixes
            pref = [0] * n
            h = 0
            for i, ch in enumerate(w):
                h = ((h * base) + (ord(ch) - 96)) & MASK
                pref[i] = h

            L = n
            while L > 0:
                hash_val = pref[L - 1]
                ans += cnt.get(hash_val, 0)
                L = pi[L - 1]

            full_hash = pref[-1]
            cnt[full_hash] = cnt.get(full_hash, 0) + 1

        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct {
    unsigned long long key;
    int used;
    long long cnt;
} Entry;

static inline void hashmap_inc(Entry *table, size_t mask, unsigned long long key) {
    size_t idx = (size_t)(key & mask);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) & mask;
    }
    if (!table[idx].used) {
        table[idx].used = 1;
        table[idx].key = key;
        table[idx].cnt = 1;
    } else {
        table[idx].cnt++;
    }
}

static inline long long hashmap_get(Entry *table, size_t mask, unsigned long long key) {
    size_t idx = (size_t)(key & mask);
    while (table[idx].used && table[idx].key != key) {
        idx = (idx + 1) & mask;
    }
    if (!table[idx].used) return 0;
    return table[idx].cnt;
}

long long countPrefixSuffixPairs(char** words, int wordsSize) {
    const unsigned long long BASE = 1315423911ULL;

    // find maximum word length
    int maxLen = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int l = strlen(words[i]);
        if (l > maxLen) maxLen = l;
    }

    // precompute powers of BASE up to maxLen
    unsigned long long *powBase = (unsigned long long *)malloc((maxLen + 1) * sizeof(unsigned long long));
    powBase[0] = 1ULL;
    for (int i = 1; i <= maxLen; ++i) {
        powBase[i] = powBase[i - 1] * BASE;
    }

    // hash table size: power of two > 2*wordsSize
    size_t cap = 1;
    while (cap < (size_t)wordsSize * 2) cap <<= 1;
    size_t mask = cap - 1;
    Entry *table = (Entry *)calloc(cap, sizeof(Entry));

    long long answer = 0;

    for (int idxWord = 0; idxWord < wordsSize; ++idxWord) {
        char *s = words[idxWord];
        int n = strlen(s);

        // prefix hashes
        unsigned long long *h = (unsigned long long *)malloc((n + 1) * sizeof(unsigned long long));
        h[0] = 0ULL;
        for (int i = 0; i < n; ++i) {
            h[i + 1] = h[i] * BASE + (unsigned long long)(s[i] - 'a' + 1);
        }

        // KMP prefix function
        int *pi = (int *)malloc(n * sizeof(int));
        pi[0] = 0;
        for (int i = 1; i < n; ++i) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) ++j;
            pi[i] = j;
        }

        // collect all border lengths (including full length)
        int len = n;
        while (len > 0) {
            unsigned long long prefHash = h[len]; // hash of prefix length len
            answer += hashmap_get(table, mask, prefHash);
            len = pi[len - 1];
        }

        // insert current word's full hash into map
        hashmap_inc(table, mask, h[n]);

        free(h);
        free(pi);
    }

    free(powBase);
    free(table);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long CountPrefixSuffixPairs(string[] words) {
        const ulong BASE = 127UL;
        var countMap = new Dictionary<ulong, int>();
        long result = 0;

        foreach (var word in words) {
            int n = word.Length;
            // Prefix hashes
            ulong[] pref = new ulong[n + 1];
            for (int i = 0; i < n; i++) {
                pref[i + 1] = pref[i] * BASE + (ulong)(word[i] - 'a' + 1);
            }

            // KMP prefix function
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                int j = pi[i - 1];
                while (j > 0 && word[i] != word[j]) j = pi[j - 1];
                if (word[i] == word[j]) j++;
                pi[i] = j;
            }

            // Iterate over all border lengths including full length
            int len = n;
            while (len > 0) {
                ulong key = pref[len];
                if (countMap.TryGetValue(key, out int cnt)) result += cnt;

                if (len == n) len = pi[n - 1];
                else len = pi[len - 1];
            }

            // Register current word
            ulong fullKey = pref[n];
            countMap[fullKey] = countMap.TryGetValue(fullKey, out int cur) ? cur + 1 : 1;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var countPrefixSuffixPairs = function(words) {
    class Node {
        constructor() {
            this.next = new Map(); // key -> Node
            this.cnt = 0; // number of previous words ending here
        }
    }

    const root = new Node();
    let ans = 0;

    for (const w of words) {
        let node = root;
        const n = w.length;
        for (let i = 0; i < n; ++i) {
            const a = w.charCodeAt(i) - 97;               // front character
            const b = w.charCodeAt(n - 1 - i) - 97;       // corresponding back character
            const key = (a << 5) | b;                     // encode pair into a number (0..1023)
            let child = node.next.get(key);
            if (!child) {
                child = new Node();
                node.next.set(key, child);
            }
            node = child;
            ans += node.cnt; // add all previous words that end at this depth
        }
        node.cnt += 1; // current word ends here
    }

    return ans;
};
```

## Typescript

```typescript
function countPrefixSuffixPairs(words: string[]): number {
    const MOD1 = 1000000007n;
    const MOD2 = 1000000009n;
    const BASE = 91138233n;

    const seen = new Map<string, number>();
    let answer = 0n;

    for (const w of words) {
        const n = w.length;
        // KMP prefix function
        const pi = new Int32Array(n);
        for (let i = 1; i < n; i++) {
            let j = pi[i - 1];
            while (j > 0 && w.charCodeAt(i) !== w.charCodeAt(j)) {
                j = pi[j - 1];
            }
            if (w.charCodeAt(i) === w.charCodeAt(j)) ++j;
            pi[i] = j;
        }

        // rolling hashes for all prefixes
        const pref1: bigint[] = new Array(n);
        const pref2: bigint[] = new Array(n);
        let h1 = 0n, h2 = 0n;
        for (let i = 0; i < n; i++) {
            const code = BigInt(w.charCodeAt(i) - 96); // 'a' -> 1
            h1 = (h1 * BASE + code) % MOD1;
            h2 = (h2 * BASE + code) % MOD2;
            pref1[i] = h1;
            pref2[i] = h2;
        }

        // iterate over all border lengths (including full length)
        let len = n;
        while (len > 0) {
            const idx = len - 1;
            const key = `${pref1[idx]}_${pref2[idx]}`;
            const cnt = seen.get(key);
            if (cnt !== undefined) answer += BigInt(cnt);
            len = pi[len - 1];
        }

        // store current word
        const fullKey = `${pref1[n - 1]}_${pref2[n - 1]}`;
        seen.set(fullKey, (seen.get(fullKey) ?? 0) + 1);
    }

    return Number(answer);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function countPrefixSuffixPairs($words) {
        $mod1 = 1000000007;
        $mod2 = 1000000009;
        $base = 91138233;

        // find maximum length to precompute powers (not strictly needed for prefix hash only)
        $maxLen = 0;
        foreach ($words as $w) {
            $len = strlen($w);
            if ($len > $maxLen) $maxLen = $len;
        }

        // precompute powers (optional, not used directly but kept for completeness)
        $pow1 = [1];
        $pow2 = [1];
        for ($i = 1; $i <= $maxLen; $i++) {
            $pow1[$i] = (int)(($pow1[$i - 1] * $base) % $mod1);
            $pow2[$i] = (int)(($pow2[$i - 1] * $base) % $mod2);
        }

        $cnt = []; // hash => occurrences seen so far
        $ans = 0;

        foreach ($words as $s) {
            $n = strlen($s);

            // KMP prefix function
            $pi = array_fill(0, $n, 0);
            for ($i = 1; $i < $n; $i++) {
                $j = $pi[$i - 1];
                while ($j > 0 && $s[$i] !== $s[$j]) {
                    $j = $pi[$j - 1];
                }
                if ($s[$i] === $s[$j]) {
                    $j++;
                }
                $pi[$i] = $j;
            }

            // rolling hashes for prefixes
            $h1 = [0];
            $h2 = [0];
            for ($i = 0; $i < $n; $i++) {
                $c = ord($s[$i]) - 96; // 'a' -> 1, ..., 'z' -> 26
                $h1[$i + 1] = (int)((($h1[$i] * $base) % $mod1 + $c) % $mod1);
                $h2[$i + 1] = (int)((($h2[$i] * $base) % $mod2 + $c) % $mod2);
            }

            // iterate over all border lengths (including full length)
            $len = $n;
            while ($len > 0) {
                $key = $h1[$len] . ':' . $h2[$len];
                if (isset($cnt[$key])) {
                    $ans += $cnt[$key];
                }
                $len = $pi[$len - 1];
            }

            // store current word for future comparisons
            $fullKey = $h1[$n] . ':' . $h2[$n];
            if (!isset($cnt[$fullKey])) {
                $cnt[$fullKey] = 0;
            }
            $cnt[$fullKey]++;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    struct HashPair: Hashable {
        let h1: UInt64
        let h2: UInt64
    }
    
    func countPrefixSuffixPairs(_ words: [String]) -> Int {
        let base1: UInt64 = 91138233
        let base2: UInt64 = 97266353
        
        var counter = [HashPair: Int]()
        var result: Int64 = 0
        
        for word in words {
            let bytes = Array(word.utf8)
            let n = bytes.count
            if n == 0 { continue }
            
            // Prefix hashes
            var pref1 = [UInt64](repeating: 0, count: n + 1)
            var pref2 = [UInt64](repeating: 0, count: n + 1)
            for i in 0..<n {
                pref1[i + 1] = pref1[i] &* base1 &+ UInt64(bytes[i])
                pref2[i + 1] = pref2[i] &* base2 &+ UInt64(bytes[i])
            }
            
            // KMP prefix function
            var pi = [Int](repeating: 0, count: n)
            if n > 1 {
                for i in 1..<n {
                    var j = pi[i - 1]
                    while j > 0 && bytes[i] != bytes[j] {
                        j = pi[j - 1]
                    }
                    if bytes[i] == bytes[j] { j += 1 }
                    pi[i] = j
                }
            }
            
            // Count matches for full length (identical previous words)
            let fullKey = HashPair(h1: pref1[n], h2: pref2[n])
            if let cnt = counter[fullKey] {
                result += Int64(cnt)
            }
            
            // Count matches for all proper borders
            var k = n > 0 ? pi[n - 1] : 0
            while k > 0 {
                let key = HashPair(h1: pref1[k], h2: pref2[k])
                if let cnt = counter[key] {
                    result += Int64(cnt)
                }
                k = pi[k - 1]
            }
            
            // Record current word
            counter[fullKey, default: 0] += 1
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Node {
        val next = IntArray(26) { -1 }
        var endCount: Long = 0L
    }

    fun countPrefixSuffixPairs(words: Array<String>): Long {
        val nodes = mutableListOf(Node()) // root at index 0
        var result = 0L

        for (word in words) {
            val m = word.length
            // KMP prefix function
            val pi = IntArray(m)
            for (i in 1 until m) {
                var j = pi[i - 1]
                while (j > 0 && word[i] != word[j]) {
                    j = pi[j - 1]
                }
                if (word[i] == word[j]) j++
                pi[i] = j
            }

            // mark border lengths (including full length)
            val isBorder = BooleanArray(m + 1)
            var len = m
            while (len > 0) {
                isBorder[len] = true
                len = pi[len - 1]
            }

            // traverse trie to count previous words that are borders
            var nodeIdx = 0
            for (i in 0 until m) {
                val c = word[i] - 'a'
                val nextIdx = nodes[nodeIdx].next[c]
                if (nextIdx == -1) break
                nodeIdx = nextIdx
                val prefLen = i + 1
                if (isBorder[prefLen]) {
                    result += nodes[nodeIdx].endCount
                }
            }

            // insert current word into trie
            var cur = 0
            for (ch in word) {
                val idx = ch - 'a'
                var nxt = nodes[cur].next[idx]
                if (nxt == -1) {
                    nxt = nodes.size
                    nodes.add(Node())
                    nodes[cur].next[idx] = nxt
                }
                cur = nxt
            }
            nodes[cur].endCount += 1L
        }

        return result
    }
}
```

## Dart

```dart
class _Node {
  final List<int> next = List.filled(26, -1);
  int end = 0;
}

class Solution {
  int countPrefixSuffixPairs(List<String> words) {
    final List<_Node> nodes = [_Node()]; // root at index 0
    int ans = 0;

    for (final String w in words) {
      final int n = w.length;
      // KMP prefix function
      final List<int> pi = List.filled(n, 0);
      for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && w.codeUnitAt(i) != w.codeUnitAt(j)) {
          j = pi[j - 1];
        }
        if (w.codeUnitAt(i) == w.codeUnitAt(j)) ++j;
        pi[i] = j;
      }

      // mark border lengths (including full length)
      final List<bool> isBorder = List.filled(n + 1, false);
      int l = n > 0 ? pi[n - 1] : 0;
      while (l > 0) {
        isBorder[l] = true;
        l = pi[l - 1];
      }
      isBorder[n] = true;

      // traverse/insert into trie, counting matches
      int cur = 0;
      for (int idx = 0; idx < n; ++idx) {
        final int c = w.codeUnitAt(idx) - 97;
        if (nodes[cur].next[c] == -1) {
          nodes.add(_Node());
          nodes[cur].next[c] = nodes.length - 1;
        }
        cur = nodes[cur].next[c];
        final int len = idx + 1;
        if (isBorder[len]) {
          ans += nodes[cur].end;
        }
      }
      // record this word
      nodes[cur].end++;
    }

    return ans;
  }
}
```

## Golang

```go
func countPrefixSuffixPairs(words []string) int64 {
    cnt := make(map[string]int64)
    var ans int64

    for _, w := range words {
        n := len(w)
        // compute prefix function (KMP failure array)
        pi := make([]int, n)
        for i := 1; i < n; i++ {
            j := pi[i-1]
            for j > 0 && w[i] != w[j] {
                j = pi[j-1]
            }
            if w[i] == w[j] {
                j++
            }
            pi[i] = j
        }

        // iterate over all border lengths (including full length)
        l := n
        for l > 0 {
            prefix := w[:l]
            if c, ok := cnt[prefix]; ok {
                ans += c
            }
            l = pi[l-1]
        }

        // store current word for future matches
        cnt[w]++
    }

    return ans
}
```

## Ruby

```ruby
def count_prefix_suffix_pairs(words)
  base = 91138233
  mask = (1 << 64) - 1

  max_len = words.map(&:length).max || 0
  pow = Array.new(max_len + 1, 0)
  pow[0] = 1
  (1..max_len).each { |i| pow[i] = (pow[i - 1] * base) & mask }

  cnt = Hash.new(0)
  ans = 0

  words.each do |w|
    m = w.length
    bytes = w.bytes
    pref = Array.new(m + 1, 0)
    (0...m).each do |i|
      pref[i + 1] = ((pref[i] * base) + (bytes[i] - 96)) & mask
    end

    pi = Array.new(m, 0)
    (1...m).each do |i|
      j = pi[i - 1]
      while j > 0 && bytes[i] != bytes[j]
        j = pi[j - 1]
      end
      j += 1 if bytes[i] == bytes[j]
      pi[i] = j
    end

    l = m
    while l > 0
      h = pref[l]
      ans += cnt[[h, l]]
      l = pi[l - 1]
    end

    full_hash = pref[m]
    cnt[[full_hash, m]] += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countPrefixSuffixPairs(words: Array[String]): Long = {
    val cnt = scala.collection.mutable.HashMap[String, Long]()
    var result: Long = 0L

    for (w <- words) {
      val n = w.length
      // compute prefix function (KMP)
      val pi = new Array[Int](n)
      var j = 0
      var i = 1
      while (i < n) {
        while (j > 0 && w.charAt(i) != w.charAt(j)) {
          j = pi(j - 1)
        }
        if (w.charAt(i) == w.charAt(j)) {
          j += 1
        }
        pi(i) = j
        i += 1
      }

      var len = n
      while (len > 0) {
        val sub = w.substring(0, len)
        result += cnt.getOrElse(sub, 0L)
        if (len == n) {
          len = if (n == 0) 0 else pi(n - 1)
        } else {
          len = pi(len - 1)
        }
      }

      cnt.update(w, cnt.getOrElse(w, 0L) + 1)
    }

    result
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i64 {
        let mut cnt: HashMap<String, i64> = HashMap::new();
        let mut ans: i64 = 0;
        for w in words.iter() {
            let bytes = w.as_bytes();
            let n = bytes.len();

            // KMP prefix function
            let mut pi = vec![0usize; n];
            for i in 1..n {
                let mut j = pi[i - 1];
                while j > 0 && bytes[i] != bytes[j] {
                    j = pi[j - 1];
                }
                if bytes[i] == bytes[j] {
                    j += 1;
                }
                pi[i] = j;
            }

            // iterate over all border lengths (including full length)
            let mut len = n;
            loop {
                let sub = &w[..len];
                if let Some(c) = cnt.get(sub) {
                    ans += *c;
                }
                let next = pi[len - 1];
                if next == 0 {
                    break;
                }
                len = next;
            }

            // record current word
            *cnt.entry(w.clone()).or_insert(0) += 1;
        }
        ans
    }
}
```

## Racket

```racket
(struct node (children cnt) #:mutable)

(define/contract (count-prefix-suffix-pairs words)
  (-> (listof string?) exact-integer?)
  (let ([root (node (make-hash) 0)])
    (define (query w)
      (let ([n (string-length w)])
        (let recur ((i 0) (cur root) (sum 0))
          (if (>= i n)
              sum
              (let* ([ch (string-ref w i)]
                     [ch2 (string-ref w (- n i 1))])
                (if (char=? ch ch2)
                    (let ([child (hash-ref (node-children cur) ch #f)])
                      (if child
                          (recur (+ i 1) child (+ sum (node-cnt child)))
                          sum))
                    sum))))))
    (define (insert w)
      (let loop ((i 0) (cur root))
        (if (= i (string-length w))
            (set-node-cnt! cur (+ (node-cnt cur) 1))
            (let* ([ch (string-ref w i)]
                   [children (node-children cur)])
              (define child (hash-ref children ch #f))
              (unless child
                (set! child (node (make-hash) 0))
                (hash-set! children ch child))
              (loop (+ i 1) child)))))
    (let ([ans 0])
      (for ([w words])
        (set! ans (+ ans (query w)))
        (insert w))
      ans)))
```

## Erlang

```erlang
-spec count_prefix_suffix_pairs(Words :: [unicode:unicode_binary()]) -> integer().
count_prefix_suffix_pairs(Words) ->
    process(Words, #{}, 0).

process([], _Map, Acc) ->
    Acc;
process([W | Rest], Map, Acc) ->
    N = byte_size(W),
    Chars = binary:bin_to_list(W),
    CharTup = list_to_tuple(Chars),
    PiArr = build_pi(CharTup, N),
    Add = sum_borders(W, N, PiArr, Map),
    NewAcc = Acc + Add,
    NewMap = maps:update_with(W, fun(C) -> C + 1 end, 1, Map),
    process(Rest, NewMap, NewAcc).

build_pi(_CharTup, 0) ->
    array:new(0, {default, 0});
build_pi(CharTup, N) when N > 0 ->
    Indexes = lists:seq(1, N - 1),
    Pi0 = array:new(N, {default, 0}),
    {PiArr, _} =
        lists:foldl(
            fun(I, {Arr, _PrevJ}) ->
                CharI = element(I + 1, CharTup),
                J0 = array:get(I - 1, Arr),
                J = shrink(J0, CharI, CharTup, Arr),
                J1 =
                    if
                        CharI == element(J + 1, CharTup) -> J + 1;
                        true -> J
                    end,
                {array:set(I, J1, Arr), J1}
            end,
            {Pi0, 0},
            Indexes),
    PiArr.

shrink(0, _CharI, _CharTup, _Arr) ->
    0;
shrink(J, CharI, CharTup, Arr) ->
    CharJ = element(J + 1, CharTup),
    if
        CharI == CharJ -> J;
        true -> shrink(array:get(J - 1, Arr), CharI, CharTup, Arr)
    end.

sum_borders(_Word, 0, _PiArr, _Map) ->
    0;
sum_borders(Word, Len, PiArr, Map) ->
    Prefix = binary:part(Word, 0, Len),
    Count = maps:get(Prefix, Map, 0),
    NextLen = array:get(Len - 1, PiArr),
    Count + sum_borders(Word, NextLen, PiArr, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_prefix_suffix_pairs(words :: [String.t()]) :: integer()
  def count_prefix_suffix_pairs(words) do
    {ans, _} =
      Enum.reduce(words, {0, %{}}, fn word, {total, cnt_map} ->
        pi = build_pi(word)
        # contribution from identical previous words
        contrib = Map.get(cnt_map, word, 0)

        n = byte_size(word)
        k = if n == 0, do: 0, else: :array.get(n - 1, pi)

        contrib = sum_borders(k, word, pi, cnt_map, contrib)

        new_total = total + contrib
        new_cnt_map = Map.update(cnt_map, word, 1, &(&1 + 1))
        {new_total, new_cnt_map}
      end)

    ans
  end

  # Build prefix function (KMP) for a binary string, returned as an :array
  defp build_pi(bin) do
    n = byte_size(bin)
    pi = :array.new(n, default: 0)
    do_build(1, 0, bin, pi, n)
  end

  defp do_build(i, _k, _bin, pi, n) when i >= n, do: pi

  defp do_build(i, k, bin, pi, n) do
    b_i = :binary.at(bin, i)

    {k1, pi1} =
      if k > 0 and b_i != :binary.at(bin, k) do
        fallback(k, b_i, bin, pi)
      else
        {k, pi}
      end

    k2 =
      if b_i == :binary.at(bin, k1) do
        k1 + 1
      else
        k1
      end

    pi2 = :array.set(i, k2, pi1)
    do_build(i + 1, k2, bin, pi2, n)
  end

  # Recursive fallback using previously computed pi values
  defp fallback(0, _b_i, _bin, pi), do: {0, pi}

  defp fallback(k, b_i, bin, pi) do
    if b_i == :binary.at(bin, k) do
      {k, pi}
    else
      new_k = :array.get(k - 1, pi)
      fallback(new_k, b_i, bin, pi)
    end
  end

  # Sum contributions of all proper border prefixes
  defp sum_borders(0, _bin, _pi, _cnt_map, acc), do: acc

  defp sum_borders(k, bin, pi, cnt_map, acc) do
    prefix = :binary.part(bin, 0, k)
    new_acc = acc + Map.get(cnt_map, prefix, 0)

    next_k =
      if k == 0 do
        0
      else
        :array.get(k - 1, pi)
      end

    sum_borders(next_k, bin, pi, cnt_map, new_acc)
  end
end
```
