# 2564. Substring XOR Queries

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> substringXorQueries(string s, vector<vector<int>>& queries) {
        int n = s.size();
        unordered_map<int, pair<int,int>> best;
        best.reserve(n * 30);
        
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                auto it = best.find(0);
                if (it == best.end() || (1 < (it->second.second - it->second.first + 1)) ||
                    (1 == (it->second.second - it->second.first + 1) && i < it->second.first)) {
                    best[0] = {i, i};
                }
            } else {
                int val = 0;
                for (int j = i; j < n && j < i + 30; ++j) {
                    val = (val << 1) + (s[j] - '0');
                    int len = j - i + 1;
                    auto it = best.find(val);
                    if (it == best.end() || len < (it->second.second - it->second.first + 1) ||
                        (len == (it->second.second - it->second.first + 1) && i < it->second.first)) {
                        best[val] = {i, j};
                    }
                }
            }
        }
        
        vector<vector<int>> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int target = q[0] ^ q[1];
            auto it = best.find(target);
            if (it != best.end()) {
                ans.push_back({it->second.first, it->second.second});
            } else {
                ans.push_back({-1, -1});
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
    public int[][] substringXorQueries(String s, int[][] queries) {
        int n = s.length();
        char[] ch = s.toCharArray();
        HashMap<Integer, int[]> best = new HashMap<>(n * 30);
        for (int i = 0; i < n; i++) {
            int val = 0;
            for (int j = i; j < n && j < i + 30; j++) {
                val = (val << 1) | (ch[j] - '0');
                int[] existing = best.get(val);
                if (existing == null) {
                    best.put(val, new int[]{i, j});
                } else {
                    int curLen = j - i + 1;
                    int existLen = existing[1] - existing[0] + 1;
                    if (curLen < existLen || (curLen == existLen && i < existing[0])) {
                        best.put(val, new int[]{i, j});
                    }
                }
            }
        }

        int q = queries.length;
        int[][] ans = new int[q][2];
        for (int i = 0; i < q; i++) {
            int target = queries[i][0] ^ queries[i][1];
            int[] pair = best.get(target);
            if (pair != null) {
                ans[i][0] = pair[0];
                ans[i][1] = pair[1];
            } else {
                ans[i][0] = -1;
                ans[i][1] = -1;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution:
    def substringXorQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(s)
        MAX_VAL = (1 << 30) - 1  # maximum value representable with <=30 bits
        best = {}  # val -> (left, right)

        for i in range(n):
            val = 0
            # consider substrings of length up to 30
            for j in range(i, min(n, i + 30)):
                val = (val << 1) + (s[j] == '1')
                if val > MAX_VAL:
                    break
                cur_len = j - i + 1
                if val not in best:
                    best[val] = (i, j)
                else:
                    li, ri = best[val]
                    best_len = ri - li + 1
                    if cur_len < best_len or (cur_len == best_len and i < li):
                        best[val] = (i, j)

        ans = []
        for first, second in queries:
            target = first ^ second
            if target in best:
                l, r = best[target]
                ans.append([l, r])
            else:
                ans.append([-1, -1])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        LIMIT = (1 << 30) - 1  # maximum possible value for xor result
        best = {}  # val -> (length, left, right)

        for i in range(n):
            val = 0
            for j in range(i, min(n, i + 30)):
                val = (val << 1) | (s[j] == '1')
                if val > LIMIT:
                    break
                cur_len = j - i + 1
                if val not in best or cur_len < best[val][0] or (cur_len == best[val][0] and i < best[val][1]):
                    best[val] = (cur_len, i, j)

        ans = []
        for first, second in queries:
            target = first ^ second
            if target in best:
                _, l, r = best[target]
                ans.append([l, r])
            else:
                ans.append([-1, -1])
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int** substringXorQueries(char* s, int** queries, int queriesSize, int* queriesColSize,
                          int* returnSize, int** returnColumnSizes) {
    int n = (int)strlen(s);
    const int MAXLEN = 30;
    const int HSIZE = 1 << 20;               // hash table size (power of two)

    struct Node {
        unsigned int key;
        int left;
        int right;
        char used;
    };

    struct Node* ht = (struct Node*)calloc(HSIZE, sizeof(struct Node));

    /* Build map of substring values to best (left,right) */
    for (int i = 0; i < n; ++i) {
        unsigned int val = 0;
        for (int j = i; j < n && j < i + MAXLEN; ++j) {
            val = (val << 1) | (unsigned int)(s[j] - '0');
            unsigned int idx = (val * 2654435761u) & (HSIZE - 1);
            while (ht[idx].used && ht[idx].key != val) {
                idx = (idx + 1) & (HSIZE - 1);
            }
            if (!ht[idx].used) {
                ht[idx].used = 1;
                ht[idx].key = val;
                ht[idx].left = i;
                ht[idx].right = j;
            } else {
                int curLen = ht[idx].right - ht[idx].left + 1;
                int newLen = j - i + 1;
                if (newLen < curLen || (newLen == curLen && i < ht[idx].left)) {
                    ht[idx].left = i;
                    ht[idx].right = j;
                }
            }
        }
    }

    *returnSize = queriesSize;
    int** ans = (int**)malloc(queriesSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc(queriesSize * sizeof(int));

    for (int q = 0; q < queriesSize; ++q) {
        (*returnColumnSizes)[q] = 2;
        ans[q] = (int*)malloc(2 * sizeof(int));

        unsigned int first = (unsigned int)queries[q][0];
        unsigned int second = (unsigned int)queries[q][1];
        unsigned int target = first ^ second;

        unsigned int idx = (target * 2654435761u) & (HSIZE - 1);
        while (ht[idx].used && ht[idx].key != target) {
            idx = (idx + 1) & (HSIZE - 1);
        }
        if (ht[idx].used && ht[idx].key == target) {
            ans[q][0] = ht[idx].left;
            ans[q][1] = ht[idx].right;
        } else {
            ans[q][0] = -1;
            ans[q][1] = -1;
        }
    }

    free(ht);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] SubstringXorQueries(string s, int[][] queries) {
        int n = s.Length;
        var dict = new Dictionary<int, int[]>();
        int maxVal = (1 << 30) - 1; // maximum value needed (<= 10^9)

        for (int i = 0; i < n; i++) {
            long val = 0;
            for (int j = i; j < n && j < i + 30; j++) {
                val = (val << 1) + (s[j] - '0');
                if (val > maxVal) break;

                int v = (int)val;
                int len = j - i + 1;

                if (!dict.TryGetValue(v, out var existing) ||
                    len < (existing[1] - existing[0] + 1) ||
                    (len == (existing[1] - existing[0] + 1) && i < existing[0])) {
                    dict[v] = new int[] { i, j };
                }
            }
        }

        int m = queries.Length;
        int[][] ans = new int[m][];
        for (int idx = 0; idx < m; idx++) {
            int first = queries[idx][0];
            int second = queries[idx][1];
            int target = first ^ second;

            if (dict.TryGetValue(target, out var pos)) {
                ans[idx] = new int[] { pos[0], pos[1] };
            } else {
                ans[idx] = new int[] { -1, -1 };
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[][]}
 */
var substringXorQueries = function(s, queries) {
    const n = s.length;
    const best = new Map(); // value -> [left, right]

    for (let i = 0; i < n; ++i) {
        let val = 0;
        for (let j = i; j < n && j < i + 30; ++j) {
            val = (val << 1) + (s.charCodeAt(j) - 48);
            const len = j - i + 1;
            if (!best.has(val)) {
                best.set(val, [i, j]);
            } else {
                const prev = best.get(val);
                const prevLen = prev[1] - prev[0] + 1;
                if (len < prevLen || (len === prevLen && i < prev[0])) {
                    best.set(val, [i, j]);
                }
            }
        }
    }

    const ans = new Array(queries.length);
    for (let k = 0; k < queries.length; ++k) {
        const [first, second] = queries[k];
        const target = first ^ second;
        if (best.has(target)) {
            ans[k] = best.get(target).slice(); // copy to avoid mutation
        } else {
            ans[k] = [-1, -1];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function substringXorQueries(s: string, queries: number[][]): number[][] {
    const n = s.length;
    const best = new Map<number, [number, number]>();
    for (let i = 0; i < n; i++) {
        let val = 0;
        for (let j = i; j < Math.min(n, i + 30); j++) {
            val = (val << 1) + (s.charCodeAt(j) - 48);
            const existing = best.get(val);
            if (!existing) {
                best.set(val, [i, j]);
            } else {
                const lenExisting = existing[1] - existing[0];
                const lenCurr = j - i;
                if (lenCurr < lenExisting || (lenCurr === lenExisting && i < existing[0])) {
                    best.set(val, [i, j]);
                }
            }
        }
    }

    const ans: number[][] = [];
    for (const q of queries) {
        const target = q[0] ^ q[1];
        const res = best.get(target);
        if (res) ans.push([res[0], res[1]]);
        else ans.push([-1, -1]);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[][]
     */
    function substringXorQueries($s, $queries) {
        $n = strlen($s);
        $map = [];

        for ($i = 0; $i < $n; $i++) {
            $val = 0;
            // only need substrings up to length 30
            $maxJ = min($n, $i + 30);
            for ($j = $i; $j < $maxJ; $j++) {
                $val = ($val << 1) + ($s[$j] === '1' ? 1 : 0);
                $len = $j - $i + 1;
                if (!isset($map[$val]) || $len < $map[$val][2] || ($len == $map[$val][2] && $i < $map[$val][0])) {
                    // store left, right, length
                    $map[$val] = [$i, $j, $len];
                }
            }
        }

        $ans = [];
        foreach ($queries as $q) {
            $first = $q[0];
            $second = $q[1];
            $target = $first ^ $second;
            if (isset($map[$target])) {
                $ans[] = [$map[$target][0], $map[$target][1]];
            } else {
                $ans[] = [-1, -1];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func substringXorQueries(_ s: String, _ queries: [[Int]]) -> [[Int]] {
        let n = s.count
        let bytes = Array(s.utf8)   // '0' = 48, '1' = 49
        var best = [Int:(Int,Int)]()   // value -> (left,right)
        
        for i in 0..<n {
            var val = 0
            var j = i
            var length = 0
            while j < n && length < 30 {
                val = (val << 1) + (bytes[j] == 49 ? 1 : 0)
                let curLen = length + 1
                if let existing = best[val] {
                    let existLen = existing.1 - existing.0 + 1
                    if curLen < existLen || (curLen == existLen && i < existing.0) {
                        best[val] = (i, j)
                    }
                } else {
                    best[val] = (i, j)
                }
                length += 1
                j += 1
            }
        }
        
        var answer = [[Int]]()
        answer.reserveCapacity(queries.count)
        for q in queries {
            let target = q[0] ^ q[1]
            if let pair = best[target] {
                answer.append([pair.0, pair.1])
            } else {
                answer.append([-1, -1])
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun substringXorQueries(s: String, queries: Array<IntArray>): Array<IntArray> {
        val n = s.length
        val best = HashMap<Int, IntArray>()
        for (i in 0 until n) {
            var value = 0
            for (j in i until minOf(n, i + 30)) {
                value = (value shl 1) or (s[j] - '0')
                val len = j - i + 1
                val existing = best[value]
                if (existing == null ||
                    len < existing[1] - existing[0] + 1 ||
                    (len == existing[1] - existing[0] + 1 && i < existing[0])
                ) {
                    best[value] = intArrayOf(i, j)
                }
            }
        }

        val ans = Array(queries.size) { IntArray(2) }
        for (idx in queries.indices) {
            val first = queries[idx][0]
            val second = queries[idx][1]
            val target = first xor second
            val res = best[target]
            if (res != null) {
                ans[idx][0] = res[0]
                ans[idx][1] = res[1]
            } else {
                ans[idx][0] = -1
                ans[idx][1] = -1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> substringXorQueries(String s, List<List<int>> queries) {
    const int maxLen = 30;
    const int limit = 1000000000; // 1e9
    final Map<int, List<int>> best = {};

    for (int i = 0; i < s.length; i++) {
      int val = 0;
      for (int j = i; j < s.length && j < i + maxLen; j++) {
        val = (val << 1) + (s.codeUnitAt(j) - 48);
        if (val > limit) break;
        final int len = j - i + 1;
        if (!best.containsKey(val)) {
          best[val] = [i, j];
        } else {
          final List<int> cur = best[val]!;
          final int curLen = cur[1] - cur[0] + 1;
          if (len < curLen || (len == curLen && i < cur[0])) {
            best[val] = [i, j];
          }
        }
      }
    }

    final List<List<int>> ans = [];
    for (final q in queries) {
      final int target = q[0] ^ q[1];
      if (best.containsKey(target)) {
        ans.add(best[target]!);
      } else {
        ans.add([-1, -1]);
      }
    }
    return ans;
  }
}
```

## Golang

```go
func substringXorQueries(s string, queries [][]int) [][]int {
	n := len(s)
	type pair struct{ l, r int }
	best := make(map[int]pair)
	bestLen := make(map[int]int)

	for i := 0; i < n; i++ {
		val := 0
		for j := i; j < n && j-i+1 <= 30; j++ {
			val = (val << 1) + int(s[j]-'0')
			curLen := j - i + 1
			if prevLen, ok := bestLen[val]; !ok || curLen < prevLen || (curLen == prevLen && i < best[val].l) {
				bestLen[val] = curLen
				best[val] = pair{i, j}
			}
		}
	}

	ans := make([][]int, len(queries))
	for idx, q := range queries {
		target := q[0] ^ q[1]
		if p, ok := best[target]; ok {
			ans[idx] = []int{p.l, p.r}
		} else {
			ans[idx] = []int{-1, -1}
		}
	}
	return ans
}
```

## Ruby

```ruby
def substring_xor_queries(s, queries)
  n = s.length
  max_len = 30
  best = {}

  (0...n).each do |i|
    val = 0
    limit = [i + max_len, n].min
    j = i
    while j < limit
      val = (val << 1) + (s.getbyte(j) - 48)
      if !best.key?(val)
        best[val] = [i, j]
      else
        cur = best[val]
        if (j - i) < (cur[1] - cur[0]) || ((j - i) == (cur[1] - cur[0]) && i < cur[0])
          best[val] = [i, j]
        end
      end
      j += 1
    end
  end

  res = []
  queries.each do |first, second|
    target = first ^ second
    if best.key?(target)
      res << best[target]
    else
      res << [-1, -1]
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def substringXorQueries(s: String, queries: Array[Array[Int]]): Array[Array[Int]] = {
        val n = s.length
        import scala.collection.mutable
        val best = mutable.Map[Int, (Int, Int)]()
        for (i <- 0 until n) {
            var value = 0
            var len = 0
            while (len < 30 && i + len < n) {
                value = (value << 1) | (s.charAt(i + len) - '0')
                len += 1
                best.get(value) match {
                    case None =>
                        best(value) = (i, i + len - 1)
                    case Some((l, r)) =>
                        val oldLen = r - l + 1
                        if (len < oldLen || (len == oldLen && i < l)) {
                            best(value) = (i, i + len - 1)
                        }
                }
            }
        }

        val ans = new Array[Array[Int]](queries.length)
        for (idx <- queries.indices) {
            val first = queries(idx)(0)
            val second = queries(idx)(1)
            val target = first ^ second
            best.get(target) match {
                case Some((l, r)) => ans(idx) = Array(l, r)
                case None         => ans(idx) = Array(-1, -1)
            }
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn substring_xor_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut map: HashMap<u32, (usize, usize)> = HashMap::new();

        for i in 0..n {
            let mut val: u32 = 0;
            // consider substrings up to length 30
            for j in i..std::cmp::min(n, i + 30) {
                val = (val << 1) | ((bytes[j] - b'0') as u32);
                let len = j - i + 1;
                match map.get(&val) {
                    Some(&(l, r)) => {
                        let cur_len = r - l + 1;
                        if len < cur_len || (len == cur_len && i < l) {
                            map.insert(val, (i, j));
                        }
                    }
                    None => {
                        map.insert(val, (i, j));
                    }
                };
            }
        }

        let mut ans: Vec<Vec<i32>> = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let first = q[0] as u32;
            let second = q[1] as u32;
            let target = first ^ second;
            if let Some(&(l, r)) = map.get(&target) {
                ans.push(vec![l as i32, r as i32]);
            } else {
                ans.push(vec![-1, -1]);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (substring-xor-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((n (string-length s))
         (best (make-hash))) ; value -> list left right
    ;; Preprocess all substrings of length up to 30
    (for ([i (in-range n)])
      (let ((val 0))
        (for ([len (in-range 1 31)])          ; len = 1..30
          (define j (+ i len -1))
          (when (< j n)
            (set! val (bitwise-ior (arithmetic-shift val 1)
                                   (if (char=? (string-ref s j) #\1) 1 0)))
            (let ((existing (hash-ref best val #f)))
              (if existing
                  (let* ((old-left (list-ref existing 0))
                         (old-right (list-ref existing 1))
                         (old-len (+ (- old-right old-left) 1)))
                    (cond [(< len old-len)
                           (hash-set! best val (list i j))]
                          [(and (= len old-len) (< i old-left))
                           (hash-set! best val (list i j))]))
                  (hash-set! best val (list i j))))))))
    ;; Answer queries
    (map (lambda (q)
           (define target (bitwise-xor (list-ref q 0) (list-ref q 1)))
           (let ((ans (hash-ref best target #f)))
             (if ans ans (list -1 -1))))
         queries)))
```

## Erlang

```erlang
-spec substring_xor_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [[integer()]].
substring_xor_queries(S, Queries) ->
    Len = byte_size(S),
    BitsList = [C - $0 || C <- binary_to_list(S)],
    BitsTuple = list_to_tuple(BitsList),
    Map = build_map(0, Len, BitsTuple, #{}),
    [ case maps:find(T, Map) of
          {ok, {_Len, L, R}} -> [L,R];
          error -> [-1,-1]
      end
      || [First,Second] <- Queries,
         T = First bxor Second ].

build_map(I, Len, BitsTuple, Map) when I < Len ->
    MaxLen = min(30, Len - I),
    NewMap = process_sub(I, 0, 0, MaxLen, BitsTuple, Map),
    build_map(I+1, Len, BitsTuple, NewMap);
build_map(_, _, _, Map) -> Map.

process_sub(Start, Offset, Val, MaxLen, BitsTuple, Map) when Offset < MaxLen ->
    Idx = Start + Offset,
    Bit = element(Idx+1, BitsTuple),
    NewVal = (Val bsl 1) bor Bit,
    LenSub = Offset + 1,
    UpdatedMap =
        case maps:find(NewVal, Map) of
            error -> maps:put(NewVal, {LenSub, Start, Idx}, Map);
            {ok, {OldLen, OldStart, _}} ->
                if LenSub < OldLen orelse (LenSub == OldLen andalso Start < OldStart) ->
                        maps:put(NewVal, {LenSub, Start, Idx}, Map);
                   true -> Map
                end
        end,
    process_sub(Start, Offset+1, NewVal, MaxLen, BitsTuple, UpdatedMap);
process_sub(_, _, _, _, _, Map) -> Map.
```

## Elixir

```elixir
defmodule Solution do
  @spec substring_xor_queries(s :: String.t(), queries :: [[integer]]) :: [[integer]]
  def substring_xor_queries(s, queries) do
    bits = s |> String.to_charlist() |> Enum.map(&(&1 - ?0))
    n = length(bits)
    max_val = 1_000_000_000

    map = build_map(bits, n, max_val)

    Enum.map(queries, fn [first, second] ->
      target = Bitwise.bxor(first, second)

      case Map.get(map, target) do
        nil -> [-1, -1]
        {_len, left, right} -> [left, right]
      end
    end)
  end

  defp build_map(bits, n, max_val) do
    Enum.reduce(0..(n - 1), %{}, fn i, acc ->
      process_start(i, bits, n, max_val, acc)
    end)
  end

  defp process_start(start, bits, n, max_val, map) do
    do_process_start(start, start, 0, bits, n, max_val, map)
  end

  defp do_process_start(start, pos, cur, bits, n, max_val, map) do
    if pos - start >= 30 or pos >= n do
      map
    else
      bit = Enum.at(bits, pos)
      new_cur = (cur <<< 1) ||| bit

      if new_cur > max_val do
        map
      else
        len = pos - start + 1

        updated_map =
          case Map.get(map, new_cur) do
            nil ->
              Map.put(map, new_cur, {len, start, pos})

            {old_len, old_start, _} ->
              if len < old_len or (len == old_len and start < old_start) do
                Map.put(map, new_cur, {len, start, pos})
              else
                map
              end
          end

        do_process_start(start, pos + 1, new_cur, bits, n, max_val, updated_map)
      end
    end
  end
end
```
