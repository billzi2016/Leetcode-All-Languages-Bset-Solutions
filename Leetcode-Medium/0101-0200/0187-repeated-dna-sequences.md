# 0187. Repeated DNA Sequences

## Cpp

```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        const int L = 10;
        int n = s.size();
        if (n < L) return {};
        
        // map nucleotides to two-bit numbers
        static int mp[256];
        static bool init = [](){
            mp['A'] = 0;
            mp['C'] = 1;
            mp['G'] = 2;
            mp['T'] = 3;
            return true;
        }();
        (void)init; // silence unused warning
        
        const int mask = (1 << (2 * L)) - 1; // keep only last 20 bits
        unordered_map<int, int> cnt;
        vector<string> ans;
        
        int hash = 0;
        for (int i = 0; i < L; ++i) {
            hash = (hash << 2) | mp[(unsigned char)s[i]];
        }
        cnt[hash] = 1;
        
        for (int i = L; i < n; ++i) {
            hash = ((hash << 2) & mask) | mp[(unsigned char)s[i]];
            int c = ++cnt[hash];
            if (c == 2) {
                ans.push_back(s.substr(i - L + 1, L));
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int n = s.length();
        List<String> result = new ArrayList<>();
        if (n < 10) return result;

        // Map each character to 2-bit representation
        int[] map = new int[128];
        map['A'] = 0;
        map['C'] = 1;
        map['G'] = 2;
        map['T'] = 3;

        int mask = (1 << 20) - 1; // keep only last 20 bits (10 chars * 2 bits)
        int hash = 0;
        for (int i = 0; i < 10; ++i) {
            hash = (hash << 2) | map[s.charAt(i)];
        }

        HashMap<Integer, Integer> count = new HashMap<>();
        count.put(hash, 1);

        for (int i = 10; i < n; ++i) {
            // slide window: shift left 2 bits, add new char, keep last 20 bits
            hash = ((hash << 2) & mask) | map[s.charAt(i)];
            int c = count.getOrDefault(hash, 0);
            if (c == 1) { // appears exactly twice now
                result.add(s.substring(i - 9, i + 1));
            }
            count.put(hash, c + 1);
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        mask = (1 << 20) - 1  # keep only last 20 bits (10 chars * 2 bits)
        hash_val = 0
        seen = set()
        added = set()
        res = []
        for i, ch in enumerate(s):
            hash_val = ((hash_val << 2) | mapping[ch]) & mask
            if i >= 9:
                if hash_val in seen:
                    if hash_val not in added:
                        res.append(s[i - 9:i + 1])
                        added.add(hash_val)
                else:
                    seen.add(hash_val)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        # map nucleotides to two-bit numbers
        mp = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        mask = (1 << 20) - 1  # keep only last 20 bits (10 chars * 2 bits)

        # compute hash for the first window
        h = 0
        for i in range(10):
            h = (h << 2) | mp[s[i]]
        seen = {h: 0}
        repeated = set()

        # slide the window
        for start in range(1, n - 9):
            h = ((h << 2) & mask) | mp[s[start + 9]]
            if h in seen:
                repeated.add(s[start:start + 10])
            else:
                seen[h] = start

        return list(repeated)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static inline int bits(char c) {
    return (c == 'A') ? 0 : (c == 'C') ? 1 : (c == 'G') ? 2 : 3;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRepeatedDnaSequences(char* s, int* returnSize) {
    *returnSize = 0;
    if (!s) return NULL;

    int n = (int)strlen(s);
    if (n < 10) return NULL;

    const int mask = (1 << 20) - 1;               // keep only last 20 bits
    int *cnt = (int *)calloc(1 << 20, sizeof(int));
    if (!cnt) return NULL;

    int key = 0;
    for (int i = 0; i < n; ++i) {
        key = ((key << 2) & mask) | bits(s[i]);
        if (i >= 9) {
            cnt[key]++;
        }
    }

    char **res = (char **)malloc(n * sizeof(char *));
    if (!res) {
        free(cnt);
        return NULL;
    }
    int idx = 0;

    key = 0;
    for (int i = 0; i < n; ++i) {
        key = ((key << 2) & mask) | bits(s[i]);
        if (i >= 9 && cnt[key] > 1) {
            char *sub = (char *)malloc(11);
            memcpy(sub, s + i - 9, 10);
            sub[10] = '\0';
            res[idx++] = sub;
            cnt[key] = 0; // ensure each sequence added only once
        }
    }

    free(cnt);

    if (idx == 0) {
        free(res);
        return NULL;
    }

    *returnSize = idx;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        var result = new List<string>();
        if (s == null || s.Length < 10) return result;

        int[] map = new int[128];
        map['A'] = 0;
        map['C'] = 1;
        map['G'] = 2;
        map['T'] = 3;

        var counts = new Dictionary<int, int>();
        int val = 0;
        for (int i = 0; i < 9; ++i) {
            val = (val << 2) | map[s[i]];
        }

        int mask = (1 << 20) - 1; // keep only last 20 bits (10 chars * 2 bits)

        for (int i = 9; i < s.Length; ++i) {
            val = ((val << 2) & mask) | map[s[i]];
            if (!counts.TryGetValue(val, out int c)) {
                counts[val] = 1;
            } else {
                if (c == 1) {
                    result.Add(s.Substring(i - 9, 10));
                }
                counts[val] = c + 1;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    const L = 10;
    if (s.length < L) return [];
    
    // map nucleotides to 2-bit numbers
    const charToBits = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    };
    
    let hash = 0;
    for (let i = 0; i < L; ++i) {
        hash = (hash << 2) | charToBits[s[i]];
    }
    
    const mask = (1 << (2 * L)) - 1; // keep only last 20 bits
    const seen = new Map();
    seen.set(hash, 1);
    const result = [];
    
    for (let i = L; i < s.length; ++i) {
        // slide window: remove leftmost char and add new char
        hash = ((hash << 2) & mask) | charToBits[s[i]];
        const cnt = seen.get(hash) || 0;
        if (cnt === 1) { // second occurrence
            result.push(s.substring(i - L + 1, i + 1));
        }
        seen.set(hash, cnt + 1);
    }
    
    return result;
};
```

## Typescript

```typescript
function findRepeatedDnaSequences(s: string): string[] {
    const L = 10;
    if (s.length < L) return [];

    const charToVal: { [k: string]: number } = { A: 0, C: 1, G: 2, T: 3 };
    const mask = (1 << (L * 2)) - 1; // keep only last 20 bits

    let hash = 0;
    for (let i = 0; i < L; i++) {
        hash = (hash << 2) | charToVal[s[i]];
    }

    const seen = new Set<number>();
    const repeated = new Set<string>();
    seen.add(hash);

    for (let i = L; i < s.length; i++) {
        // slide window: shift left, add new char, and mask to keep 20 bits
        hash = ((hash << 2) & mask) | charToVal[s[i]];
        if (seen.has(hash)) {
            repeated.add(s.substring(i - L + 1, i + 1));
        } else {
            seen.add(hash);
        }
    }

    return Array.from(repeated);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function findRepeatedDnaSequences($s) {
        $len = strlen($s);
        if ($len < 10) {
            return [];
        }
        $counts = [];
        for ($i = 0; $i <= $len - 10; $i++) {
            $sub = substr($s, $i, 10);
            if (isset($counts[$sub])) {
                $counts[$sub]++;
            } else {
                $counts[$sub] = 1;
            }
        }
        $result = [];
        foreach ($counts as $sub => $cnt) {
            if ($cnt > 1) {
                $result[] = $sub;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findRepeatedDnaSequences(_ s: String) -> [String] {
        let n = s.count
        if n < 10 { return [] }
        var result = [String]()
        var seen = Set<Int>()
        var repeated = Set<Int>()
        var hash = 0
        let mask = (1 << 20) - 1   // keep last 10 characters (2 bits each)
        
        let bytes = Array(s.utf8)
        for i in 0..<bytes.count {
            let val: Int
            switch bytes[i] {
            case 65: // 'A'
                val = 0
            case 67: // 'C'
                val = 1
            case 71: // 'G'
                val = 2
            default: // 'T' (84)
                val = 3
            }
            hash = ((hash << 2) | val) & mask
            if i >= 9 {
                if seen.contains(hash) {
                    repeated.insert(hash)
                } else {
                    seen.insert(hash)
                }
            }
        }
        
        for h in repeated {
            result.append(intToString(h))
        }
        return result
    }
    
    private func intToString(_ hash: Int) -> String {
        var chars = [Character](repeating: "A", count: 10)
        var v = hash
        for i in stride(from: 9, through: 0, by: -1) {
            let bits = v & 3
            switch bits {
            case 0:
                chars[i] = "A"
            case 1:
                chars[i] = "C"
            case 2:
                chars[i] = "G"
            default:
                chars[i] = "T"
            }
            v >>= 2
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findRepeatedDnaSequences(s: String): List<String> {
        val n = s.length
        if (n < 10) return emptyList()
        val seen = HashMap<Int, Int>()
        val result = ArrayList<String>()
        var hash = 0
        val mask = (1 shl 20) - 1 // keep last 20 bits (10 chars * 2 bits)
        for (i in 0 until n) {
            val v = when (s[i]) {
                'A' -> 0
                'C' -> 1
                'G' -> 2
                else -> 3 // 'T'
            }
            hash = ((hash shl 2) or v) and mask
            if (i >= 9) {
                val cnt = seen.getOrDefault(hash, 0)
                if (cnt == 1) {
                    result.add(s.substring(i - 9, i + 1))
                }
                seen[hash] = cnt + 1
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> findRepeatedDnaSequences(String s) {
    const int L = 10;
    final int n = s.length;
    if (n < L) return [];
    const int mask = (1 << (L * 2)) - 1; // keep last 20 bits
    final Map<int, int> count = {};
    final Set<String> res = {};

    int hash = 0;
    for (int i = 0; i < L; ++i) {
      hash = (hash << 2) | _charToBits(s.codeUnitAt(i));
    }
    count[hash] = 1;

    for (int i = L; i < n; ++i) {
      hash = ((hash << 2) & mask) | _charToBits(s.codeUnitAt(i));
      int c = count[hash] ?? 0;
      if (c == 1) {
        res.add(s.substring(i - L + 1, i + 1));
      }
      count[hash] = c + 1;
    }

    return res.toList();
  }

  int _charToBits(int code) {
    // 'A' =65, 'C'=67,'G'=71,'T'=84
    if (code == 65) return 0; // A
    if (code == 67) return 1; // C
    if (code == 71) return 2; // G
    return 3; // T
  }
}
```

## Golang

```go
func findRepeatedDnaSequences(s string) []string {
    n := len(s)
    if n < 10 {
        return []string{}
    }
    const mask = (1 << 20) - 1
    counts := make(map[int]int)
    var hash int

    for i := 0; i < 10; i++ {
        hash = (hash << 2) | charToBits(s[i])
    }
    counts[hash] = 1
    res := []string{}

    for i := 10; i < n; i++ {
        hash = ((hash << 2) & mask) | charToBits(s[i])
        if cnt, ok := counts[hash]; ok {
            if cnt == 1 {
                res = append(res, s[i-9:i+1])
            }
            counts[hash] = cnt + 1
        } else {
            counts[hash] = 1
        }
    }

    return res
}

func charToBits(b byte) int {
    switch b {
    case 'A':
        return 0
    case 'C':
        return 1
    case 'G':
        return 2
    default: // 'T'
        return 3
    }
}
```

## Ruby

```ruby
def find_repeated_dna_sequences(s)
  return [] if s.length < 10
  counts = Hash.new(0)
  result = []
  (0..s.length - 10).each do |i|
    sub = s[i, 10]
    counts[sub] += 1
    result << sub if counts[sub] == 2
  end
  result
end
```

## Scala

```scala
object Solution {
    def findRepeatedDnaSequences(s: String): List[String] = {
        val n = s.length
        if (n < 10) return Nil

        // encode characters to two bits
        val enc = new Array[Int](128)
        enc('A') = 0
        enc('C') = 1
        enc('G') = 2
        enc('T') = 3

        var hash = 0
        val mask = (1 << 20) - 1 // keep only last 20 bits (10 chars * 2 bits)

        val firstSeen = scala.collection.mutable.HashSet[Int]()
        val added = scala.collection.mutable.HashSet[Int]()
        val result = scala.collection.mutable.ListBuffer[String]()

        for (i <- 0 until n) {
            hash = ((hash << 2) | enc(s.charAt(i))) & mask
            if (i >= 9) { // window of length 10 is ready
                if (firstSeen.contains(hash)) {
                    if (!added.contains(hash)) {
                        result += s.substring(i - 9, i + 1)
                        added.add(hash)
                    }
                } else {
                    firstSeen.add(hash)
                }
            }
        }

        result.toList
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        const LEN: usize = 10;
        if s.len() < LEN {
            return Vec::new();
        }
        let bytes = s.as_bytes();
        // map A,C,G,T to 2-bit values
        #[inline]
        fn val(b: u8) -> u32 {
            match b {
                b'A' => 0,
                b'C' => 1,
                b'G' => 2,
                b'T' => 3,
                _ => 0, // unreachable for valid input
            }
        }

        let mask: u32 = (1 << (LEN * 2)) - 1; // keep only last 20 bits
        let mut code: u32 = 0;
        let mut seen: HashSet<u32> = HashSet::new();
        let mut repeated: HashSet<String> = HashSet::new();

        for i in 0..bytes.len() {
            code = ((code << 2) & mask) | val(bytes[i]);
            if i + 1 >= LEN {
                let start = i + 1 - LEN;
                if !seen.insert(code) {
                    // already seen before
                    repeated.insert(s[start..start + LEN].to_string());
                }
            }
        }

        repeated.into_iter().collect()
    }
}
```

## Racket

```racket
#lang racket

(provide find-repeated-dna-sequences)

(define/contract (find-repeated-dna-sequences s)
  (-> string? (listof string?))
  (let* ((n (string-length s))
         (mask (sub1 (arithmetic-shift 1 20))) ; keep last 20 bits (10 chars * 2 bits)
         (counts (make-hash)))
    (define (code ch)
      (cond [(char=? ch #\A) 0]
            [(char=? ch #\C) 1]
            [(char=? ch #\G) 2]
            [else 3])) ; T

    ;; rolling hash over the string
    (let loop ((i 0) (h 0))
      (if (= i n)
          (void)
          (let* ((c (code (string-ref s i)))
                 (new-h (bitwise-ior (bitwise-and (arithmetic-shift h 2) mask) c)))
            (when (>= i 9)
              (hash-set! counts new-h (+ 1 (hash-ref counts new-h 0))))
            (loop (+ i 1) new-h))))

    ;; convert integer representation back to DNA string
    (define (int->dna val)
      (let ((vec (make-vector 10)))
        (let rec ((idx 9) (v val))
          (when (>= idx 0)
            (define cd (bitwise-and v 3))
            (vector-set! vec idx
                         (case cd
                           [(0) #\A]
                           [(1) #\C]
                           [(2) #\G]
                           [else #\T]))
            (rec (- idx 1) (arithmetic-shift v -2))))
        (list->string (vector->list vec))))

    ;; collect sequences that appear more than once
    (let ((res '()))
      (hash-for-each counts
        (lambda (k v)
          (when (> v 1)
            (set! res (cons (int->dna k) res)))))
      (reverse res))))
```

## Erlang

```erlang
-module(solution).
-export([find_repeated_dna_sequences/1]).
-spec find_repeated_dna_sequences(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
find_repeated_dna_sequences(S) ->
    Len = byte_size(S),
    if
        Len < 10 ->
            [];
        true ->
            Bytes = binary_to_list(S),
            {FirstTen, Rest} = lists:split(10, Bytes),
            Code0 = build_code(FirstTen, 0),
            Mask = (1 bsl 20) - 1,
            Seen0 = maps:put(Code0, true, #{}),
            Repeated0 = #{},
            Result0 = [],
            Result = process(Rest, Code0, Mask, Seen0, Repeated0, Result0),
            lists:reverse(Result)
    end.

build_code([], Acc) -> Acc;
build_code([Char|Tail], Acc) ->
    Val = char_to_val(Char),
    NewAcc = (Acc bsl 2) bor Val,
    build_code(Tail, NewAcc).

char_to_val($A) -> 0;
char_to_val($C) -> 1;
char_to_val($G) -> 2;
char_to_val($T) -> 3.

val_to_char(0) -> $A;
val_to_char(1) -> $C;
val_to_char(2) -> $G;
val_to_char(3) -> $T.

int_to_seq(Code) ->
    Chars = [val_to_char((Code bsr (2*I)) band 3) || I <- lists:seq(9,0,-1)],
    list_to_binary(Chars).

process([], _PrevCode, _Mask, _Seen, _Repeated, AccResult) ->
    AccResult;
process([Char|Tail], PrevCode, Mask, Seen, Repeated, AccResult) ->
    Val = char_to_val(Char),
    Code = ((PrevCode bsl 2) band Mask) bor Val,
    case maps:is_key(Code, Seen) of
        false ->
            NewSeen = maps:put(Code, true, Seen),
            process(Tail, Code, Mask, NewSeen, Repeated, AccResult);
        true ->
            case maps:is_key(Code, Repeated) of
                false ->
                    SeqBin = int_to_seq(Code),
                    NewRepeated = maps:put(Code, true, Repeated),
                    process(Tail, Code, Mask, Seen, NewRepeated, [SeqBin|AccResult]);
                true ->
                    process(Tail, Code, Mask, Seen, Repeated, AccResult)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec find_repeated_dna_sequences(s :: String.t) :: [String.t]
  def find_repeated_dna_sequences(s) do
    len = byte_size(s)

    if len < 10 do
      []
    else
      mask = (1 <<< 20) - 1

      {_, _, result_set} =
        Enum.reduce(0..(len - 1), {0, MapSet.new(), MapSet.new()}, fn i,
                                                                   {hash, seen, res} ->
          val = encode(:binary.at(s, i))
          hash = ((hash <<< 2) ||| val) &&& mask

          if i >= 9 do
            if MapSet.member?(seen, hash) do
              sub = :binary.part(s, i - 9, 10)
              {hash, seen, MapSet.put(res, sub)}
            else
              {hash, MapSet.put(seen, hash), res}
            end
          else
            {hash, seen, res}
          end
        end)

      MapSet.to_list(result_set)
    end
  end

  defp encode(?A), do: 0
  defp encode(?C), do: 1
  defp encode(?G), do: 2
  defp encode(?T), do: 3
end
```
