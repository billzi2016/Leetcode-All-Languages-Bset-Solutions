# 2306. Naming a Company

## Cpp

```cpp
class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        unordered_map<string, int> mp;
        mp.reserve(ideas.size() * 2);
        for (const string& s : ideas) {
            string suffix = s.substr(1);
            int c = s[0] - 'a';
            mp[suffix] |= (1 << c);
        }
        vector<int> masks;
        masks.reserve(mp.size());
        for (auto &p : mp) masks.push_back(p.second);
        
        long long cnt[26][26];
        memset(cnt, 0, sizeof(cnt));
        
        for (int mask : masks) {
            // bits set
            int present = mask;
            while (present) {
                int i = __builtin_ctz(present);
                present &= (present - 1);
                // bits not set
                int absent = (~mask) & ((1 << 26) - 1);
                while (absent) {
                    int j = __builtin_ctz(absent);
                    absent &= (absent - 1);
                    cnt[i][j]++;
                }
            }
        }
        
        long long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                ans += cnt[i][j] * cnt[j][i] * 2;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long distinctNames(String[] ideas) {
        java.util.HashMap<String, Integer> suffixMask = new java.util.HashMap<>();
        for (String s : ideas) {
            String suffix = s.substring(1);
            int bit = 1 << (s.charAt(0) - 'a');
            suffixMask.merge(suffix, bit, (oldVal, newVal) -> oldVal | newVal);
        }
        int m = suffixMask.size();
        int[] masks = new int[m];
        int idx = 0;
        for (int mask : suffixMask.values()) {
            masks[idx++] = mask;
        }
        long ans = 0L;
        for (int i = 0; i < m; ++i) {
            int mi = masks[i];
            for (int j = i + 1; j < m; ++j) {
                int mj = masks[j];
                int common = mi & mj;
                int cntI = Integer.bitCount(mi ^ common);
                int cntJ = Integer.bitCount(mj ^ common);
                ans += (long) cntI * cntJ * 2;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        suffix_mask = {}
        for w in ideas:
            sfx = w[1:]
            idx = ord(w[0]) - 97
            mask = suffix_mask.get(sfx, 0)
            mask |= 1 << idx
            suffix_mask[sfx] = mask

        cnt = [[0] * 26 for _ in range(26)]

        for mask in suffix_mask.values():
            # list of present letters
            present = [i for i in range(26) if (mask >> i) & 1]
            absent = [i for i in range(26) if not ((mask >> i) & 1)]
            for a in present:
                row = cnt[a]
                for b in absent:
                    row[b] += 1

        ans = 0
        for a in range(26):
            for b in range(26):
                if a != b:
                    ans += cnt[a][b] * cnt[b][a]
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffix_mask = {}
        for w in ideas:
            s = w[1:]
            mask = suffix_mask.get(s, 0)
            mask |= 1 << (ord(w[0]) - 97)
            suffix_mask[s] = mask

        cnt = [[0] * 26 for _ in range(26)]
        all_mask = (1 << 26) - 1

        for mask in suffix_mask.values():
            present = mask
            while present:
                a_bit = present & -present
                a = a_bit.bit_length() - 1
                missing = (~mask) & all_mask
                m = missing
                while m:
                    b_bit = m & -m
                    b = b_bit.bit_length() - 1
                    cnt[a][b] += 1
                    m -= b_bit
                present -= a_bit

        ans = 0
        for i in range(26):
            for j in range(26):
                if i != j:
                    ans += cnt[i][j] * cnt[j][i]
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *suf;
    int first;
} Item;

static int cmpItem(const void *a, const void *b) {
    const Item *ia = (const Item *)a;
    const Item *ib = (const Item *)b;
    return strcmp(ia->suf, ib->suf);
}

long long distinctNames(char **ideas, int ideasSize) {
    if (ideasSize < 2) return 0;

    Item *items = (Item *)malloc(sizeof(Item) * ideasSize);
    for (int i = 0; i < ideasSize; ++i) {
        int len = strlen(ideas[i]);
        char *suf = (char *)malloc(len);               // length includes null terminator
        strcpy(suf, ideas[i] + 1);                     // copy suffix (may be empty)
        items[i].suf = suf;
        items[i].first = ideas[i][0] - 'a';
    }

    qsort(items, ideasSize, sizeof(Item), cmpItem);

    int *masks = (int *)malloc(sizeof(int) * ideasSize);
    int maskCount = 0;

    for (int i = 0; i < ideasSize;) {
        int j = i;
        int mask = 0;
        while (j < ideasSize && strcmp(items[i].suf, items[j].suf) == 0) {
            mask |= 1 << items[j].first;
            ++j;
        }
        masks[maskCount++] = mask;
        i = j;
    }

    for (int i = 0; i < ideasSize; ++i) free(items[i].suf);
    free(items);

    long long cnt[26][26];
    memset(cnt, 0, sizeof(cnt));

    for (int idx = 0; idx < maskCount; ++idx) {
        int m = masks[idx];
        for (int a = 0; a < 26; ++a) if (m & (1 << a)) {
            for (int b = 0; b < 26; ++b) if ((m & (1 << b)) == 0) {
                cnt[a][b]++;
            }
        }
    }

    free(masks);

    long long ans = 0;
    for (int a = 0; a < 26; ++a)
        for (int b = 0; b < 26; ++b)
            if (a != b)
                ans += cnt[a][b] * cnt[b][a];

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long DistinctNames(string[] ideas)
    {
        var suffixMask = new Dictionary<string, int>();
        foreach (var idea in ideas)
        {
            char first = idea[0];
            string suffix = idea.Substring(1);
            if (!suffixMask.TryGetValue(suffix, out int mask))
                mask = 0;
            mask |= 1 << (first - 'a');
            suffixMask[suffix] = mask;
        }

        long[,] cnt = new long[26, 26];
        foreach (int mask in suffixMask.Values)
        {
            for (int a = 0; a < 26; ++a)
            {
                if ((mask & (1 << a)) != 0)
                {
                    for (int b = 0; b < 26; ++b)
                    {
                        if ((mask & (1 << b)) == 0)
                            cnt[a, b]++;
                    }
                }
            }
        }

        long ans = 0;
        for (int a = 0; a < 26; ++a)
        {
            for (int b = 0; b < 26; ++b)
            {
                if (a != b)
                    ans += cnt[a, b] * cnt[b, a];
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} ideas
 * @return {number}
 */
var distinctNames = function(ideas) {
    const suffixMap = new Map(); // suffix -> bitmask of first letters
    for (const word of ideas) {
        const firstIdx = word.charCodeAt(0) - 97;
        const suffix = word.slice(1);
        const prevMask = suffixMap.get(suffix) || 0;
        suffixMap.set(suffix, prevMask | (1 << firstIdx));
    }

    // cnt[a][b]: number of suffix groups that contain letter a but not b
    const cnt = Array.from({ length: 26 }, () => Array(26).fill(0));

    for (const mask of suffixMap.values()) {
        const present = [];
        for (let i = 0; i < 26; ++i) {
            if (mask & (1 << i)) present.push(i);
        }
        for (const a of present) {
            for (let b = 0; b < 26; ++b) {
                if ((mask & (1 << b)) === 0) {
                    cnt[a][b]++;
                }
            }
        }
    }

    let ans = 0;
    for (let a = 0; a < 26; ++a) {
        for (let b = 0; b < 26; ++b) {
            if (a === b) continue;
            ans += cnt[a][b] * cnt[b][a];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function distinctNames(ideas: string[]): number {
    const suffixMap = new Map<string, number>();
    for (const w of ideas) {
        const first = w.charCodeAt(0) - 97;
        const suffix = w.slice(1);
        const prev = suffixMap.get(suffix) ?? 0;
        suffixMap.set(suffix, prev | (1 << first));
    }

    const cnt: number[][] = Array.from({ length: 26 }, () => Array(26).fill(0));

    for (const mask of suffixMap.values()) {
        const present: number[] = [];
        for (let i = 0; i < 26; i++) {
            if ((mask >> i) & 1) present.push(i);
        }
        for (const i of present) {
            for (let j = 0; j < 26; j++) {
                if (((mask >> j) & 1) === 0) cnt[i][j]++;
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < 26; i++) {
        for (let j = i + 1; j < 26; j++) {
            ans += cnt[i][j] * cnt[j][i] * 2;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $ideas
     * @return Integer
     */
    function distinctNames($ideas) {
        $suffixMasks = [];
        foreach ($ideas as $idea) {
            $first = ord($idea[0]) - 97; // 'a' => 0
            $suffix = substr($idea, 1);
            if (!isset($suffixMasks[$suffix])) {
                $suffixMasks[$suffix] = 0;
            }
            $suffixMasks[$suffix] |= (1 << $first);
        }

        // cnt[x][y]: number of suffix groups where letter x exists and y does not
        $cnt = array_fill(0, 26, array_fill(0, 26, 0));

        foreach ($suffixMasks as $mask) {
            for ($i = 0; $i < 26; ++$i) {
                if (($mask >> $i) & 1) { // letter i present
                    for ($j = 0; $j < 26; ++$j) {
                        if ($i == $j) continue;
                        if ((($mask >> $j) & 1) == 0) { // letter j absent
                            $cnt[$i][$j]++;
                        }
                    }
                }
            }
        }

        $ans = 0;
        for ($i = 0; $i < 26; ++$i) {
            for ($j = $i + 1; $j < 26; ++$j) {
                $ans += $cnt[$i][$j] * $cnt[$j][$i] * 2;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func distinctNames(_ ideas: [String]) -> Int {
        var suffixMask = [String:Int]()
        for idea in ideas {
            guard let firstChar = idea.first else { continue }
            let idx = Int(firstChar.asciiValue! - Character("a").asciiValue!)
            let mask = 1 << idx
            let suffix = String(idea.dropFirst())
            suffixMask[suffix, default: 0] |= mask
        }
        let masks = Array(suffixMask.values)
        var result = 0
        let m = masks.count
        for i in 0..<m {
            let mi = masks[i]
            for j in (i + 1)..<m {
                let mj = masks[j]
                let cntI = (mi & ~mj).nonzeroBitCount
                let cntJ = (mj & ~mi).nonzeroBitCount
                result += cntI * cntJ * 2
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distinctNames(ideas: Array<String>): Long {
        val suffixMask = HashMap<String, Int>()
        for (s in ideas) {
            val suffix = s.substring(1)
            val idx = s[0] - 'a'
            val mask = suffixMask.getOrDefault(suffix, 0) or (1 shl idx)
            suffixMask[suffix] = mask
        }
        val cnt = Array(26) { IntArray(26) }
        val ALL = (1 shl 26) - 1
        for (mask in suffixMask.values) {
            var present = mask
            while (present != 0) {
                val a = Integer.numberOfTrailingZeros(present)
                var absent = ALL xor mask
                while (absent != 0) {
                    val b = Integer.numberOfTrailingZeros(absent)
                    cnt[a][b]++
                    absent = absent and (absent - 1)
                }
                present = present and (present - 1)
            }
        }
        var ans = 0L
        for (a in 0 until 26) {
            for (b in 0 until 26) {
                if (a != b) {
                    ans += cnt[a][b].toLong() * cnt[b][a]
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int distinctNames(List<String> ideas) {
    // Map each suffix to a bitmask of first letters present.
    final Map<String, int> suffixMask = {};
    for (var idea in ideas) {
      int first = idea.codeUnitAt(0) - 97;
      String suffix = idea.length > 1 ? idea.substring(1) : '';
      suffixMask[suffix] = (suffixMask[suffix] ?? 0) | (1 << first);
    }

    // cnt[a][b]: number of ideas whose first letter is a and whose suffix
    // does NOT contain letter b.
    List<List<int>> cnt = List.generate(26, (_) => List.filled(26, 0));

    for (var idea in ideas) {
      int first = idea.codeUnitAt(0) - 97;
      String suffix = idea.length > 1 ? idea.substring(1) : '';
      int mask = suffixMask[suffix]!;
      for (int b = 0; b < 26; ++b) {
        if (b == first) continue;
        if ((mask & (1 << b)) == 0) {
          cnt[first][b]++;
        }
      }
    }

    int ans = 0;
    for (int a = 0; a < 26; ++a) {
      for (int b = 0; b < 26; ++b) {
        if (a == b) continue;
        ans += cnt[a][b] * cnt[b][a];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func distinctNames(ideas []string) int64 {
    suffixMask := make(map[string]int)
    for _, w := range ideas {
        first := w[0] - 'a'
        suffix := w[1:]
        mask := suffixMask[suffix]
        mask |= 1 << first
        suffixMask[suffix] = mask
    }
    var cnt [26][26]int
    for _, mask := range suffixMask {
        for i := 0; i < 26; i++ {
            if (mask>>i)&1 == 1 {
                for j := 0; j < 26; j++ {
                    if (mask>>j)&1 == 0 {
                        cnt[i][j]++
                    }
                }
            }
        }
    }
    var ans int64
    for i := 0; i < 26; i++ {
        for j := i + 1; j < 26; j++ {
            ans += int64(cnt[i][j]) * int64(cnt[j][i]) * 2
        }
    }
    return ans
}
```

## Ruby

```ruby
def distinct_names(ideas)
  masks = {}
  ideas.each do |s|
    first_idx = s[0].ord - 97
    suffix = s.length > 1 ? s[1..-1] : ''
    masks[suffix] ||= 0
    masks[suffix] |= (1 << first_idx)
  end

  cnt = Array.new(26) { Array.new(26, 0) }

  masks.each_value do |mask|
    present = []
    absent = []
    26.times do |i|
      if (mask & (1 << i)) != 0
        present << i
      else
        absent << i
      end
    end
    present.each do |i|
      absent.each do |j|
        cnt[i][j] += 1
      end
    end
  end

  ans = 0
  (0...26).each do |i|
    ((i + 1)...26).each do |j|
      ans += cnt[i][j] * cnt[j][i] * 2
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def distinctNames(ideas: Array[String]): Long = {
        import scala.collection.mutable

        val suffixMask = mutable.HashMap.empty[String, Int]

        for (idea <- ideas) {
            val first = idea.charAt(0) - 'a'
            val suffix = idea.substring(1)
            val updatedMask = suffixMask.getOrElse(suffix, 0) | (1 << first)
            suffixMask.update(suffix, updatedMask)
        }

        val cnt = Array.ofDim[Long](26, 26)

        for ((_, mask) <- suffixMask) {
            var a = 0
            while (a < 26) {
                if (((mask >> a) & 1) != 0) {
                    var b = 0
                    while (b < 26) {
                        if (((mask >> b) & 1) == 0) {
                            cnt(a)(b) += 1L
                        }
                        b += 1
                    }
                }
                a += 1
            }
        }

        var ans: Long = 0L
        var i = 0
        while (i < 26) {
            var j = 0
            while (j < 26) {
                if (i != j) {
                    ans += cnt(i)(j) * cnt(j)(i)
                }
                j += 1
            }
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        let mut groups: HashMap<String, u32> = HashMap::new();
        for s in ideas.iter() {
            let bytes = s.as_bytes();
            let first = (bytes[0] - b'a') as u32;
            let suffix = &s[1..];
            let entry = groups.entry(suffix.to_string()).or_insert(0);
            *entry |= 1 << first;
        }

        let mut cnt = [[0u32; 26]; 26];
        for mask in groups.values() {
            for a in 0..26 {
                if (mask >> a) & 1 == 1 {
                    for b in 0..26 {
                        if (mask >> b) & 1 == 0 {
                            cnt[a][b] += 1;
                        }
                    }
                }
            }
        }

        let mut ans: i64 = 0;
        for i in 0..26 {
            for j in 0..26 {
                if i != j {
                    ans += (cnt[i][j] as i64) * (cnt[j][i] as i64);
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (distinct-names ideas)
  (-> (listof string?) exact-integer?)
  (let* ([ht (make-hash)])
    ;; Build suffix -> mask mapping
    (for ([idea ideas])
      (let* ([first (string-ref idea 0)]
             [suffix (substring idea 1)]
             [bit (arithmetic-shift 1 (- (char->integer first) (char->integer #\a)))])
        (hash-update! ht suffix (lambda (old) (bitwise-ior old bit)) 0)))
    ;; cnt[i][j] = number of ideas whose first letter is i and whose suffix group lacks j
    (define cnt
      (for/vector #:length 26 (λ (_) (make-vector 26 0))))
    (for ([mask (in-hash-values ht)])
      (for ([i (in-range 26)])
        (when (positive? (bitwise-and mask (arithmetic-shift 1 i)))
          (for ([j (in-range 26)])
            (unless (positive? (bitwise-and mask (arithmetic-shift 1 j)))
              (let* ([row (vector-ref cnt i)]
                     [old (vector-ref row j)])
                (vector-set! row j (+ old 1))))))))
    ;; Compute answer
    (let ([ans (make-parameter 0)])
      (for ([i (in-range 26)])
        (for ([j (in-range (+ i 1) 26)])
          (let* ([a (vector-ref (vector-ref cnt i) j)]
                 [b (vector-ref (vector-ref cnt j) i)]
                 [add (* a b 2)])
            (ans (+ (ans) add)))))
      (ans))))
```

## Erlang

```erlang
-module(solution).
-export([distinct_names/1]).

%% Count set bits in an integer using Kernighan's algorithm.
popcnt(0) -> 0;
popcnt(N) -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N band (N - 1), Acc + 1).

%% Main function as required by the problem.
-spec distinct_names(Ideas :: [unicode:unicode_binary()]) -> integer().
distinct_names(Ideas) ->
    %% Build a map from suffix to bitmask of starting letters.
    SuffixMaskMap = lists:foldl(
        fun(Idea, Acc) ->
            <<First:8, Rest/binary>> = Idea,
            LetterIdx = First - $a,
            Bit = 1 bsl LetterIdx,
            case maps:get(Rest, Acc, undefined) of
                undefined -> maps:put(Rest, Bit, Acc);
                ExistingMask -> maps:put(Rest, ExistingMask bor Bit, Acc)
            end
        end,
        #{},
        Ideas),

    %% Aggregate counts for each distinct mask.
    MaskCountMap = maps:fold(
        fun(_Suffix, Mask, MAcc) ->
            case maps:get(Mask, MAcc, undefined) of
                undefined -> maps:put(Mask, 1, MAcc);
                C -> maps:put(Mask, C + 1, MAcc)
            end
        end,
        #{},
        SuffixMaskMap),

    MaskList = maps:to_list(MaskCountMap),
    compute_pairs(MaskList, 0).

%% Iterate over all unordered pairs of masks.
compute_pairs([], Acc) -> Acc;
compute_pairs([{MaskA, CountA} | Rest], Acc) ->
    NewAcc = pair_with_rest(Rest, MaskA, CountA, Acc),
    compute_pairs(Rest, NewAcc).

pair_with_rest([], _MaskA, _CountA, Acc) -> Acc;
pair_with_rest([{MaskB, CountB} | Tail], MaskA, CountA, Acc) ->
    Common = MaskA band MaskB,
    BitsA = popcnt(MaskA) - popcnt(Common),
    BitsB = popcnt(MaskB) - popcnt(Common),
    Add = 2 * BitsA * BitsB * CountA * CountB,
    pair_with_rest(Tail, MaskA, CountA, Acc + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec distinct_names(ideas :: [String.t]) :: integer
  def distinct_names(ideas) do
    import Bitwise

    # Build map from suffix to bitmask of starting letters
    suffix_map =
      Enum.reduce(ideas, %{}, fn idea, acc ->
        <<first::utf8, rest::binary>> = idea
        mask = 1 <<< (first - ?a)
        Map.update(acc, rest, mask, fn existing -> existing ||| mask end)
      end)

    # Count for each ordered pair of letters (i,j) how many suffix groups have i present and j absent
    cnt =
      Enum.reduce(suffix_map, %{}, fn {_suffix, mask}, cnt_acc ->
        present = for i <- 0..25, ((mask &&& (1 <<< i)) != 0), do: i
        absent = for j <- 0..25, ((mask &&& (1 <<< j)) == 0), do: j

        Enum.reduce(present, cnt_acc, fn i, acc2 ->
          Enum.reduce(absent, acc2, fn j, acc3 ->
            Map.update(acc3, {i, j}, 1, &(&1 + 1))
          end)
        end)
      end)

    # Compute answer using the counts
    ans =
      Enum.reduce(0..25, 0, fn i, sum_i ->
        Enum.reduce((i + 1)..25, sum_i, fn j, sum_j ->
          a = Map.get(cnt, {i, j}, 0)
          b = Map.get(cnt, {j, i}, 0)
          sum_j + a * b * 2
        end)
      end)

    ans
  end
end
```
