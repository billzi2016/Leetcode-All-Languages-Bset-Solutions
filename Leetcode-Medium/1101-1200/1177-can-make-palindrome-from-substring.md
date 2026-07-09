# 1177. Can Make Palindrome from Substring

## Cpp

```cpp
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] ^ (1 << (s[i] - 'a'));
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0], r = q[1], k = q[2];
            int mask = pref[r + 1] ^ pref[l];
            int odd = __builtin_popcount(mask);
            ans.push_back(k >= odd / 2);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        int n = s.length();
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int bit = 1 << (s.charAt(i) - 'a');
            pref[i + 1] = pref[i] ^ bit;
        }
        List<Boolean> ans = new ArrayList<>(queries.length);
        for (int[] q : queries) {
            int l = q[0], r = q[1], k = q[2];
            int mask = pref[r + 1] ^ pref[l];
            int odd = Integer.bitCount(mask);
            int need = odd / 2;
            ans.add(k >= need);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] ^ (1 << (ord(ch) - ord('a')))
        res = []
        for left, right, k in queries:
            mask = pref[right + 1] ^ pref[left]
            odd = mask.bit_count() if hasattr(mask, "bit_count") else bin(mask).count("1")
            res.append((odd // 2) <= k)
        return res
```

## Python3

```python
class Solution:
    def canMakePaliQueries(self, s, queries):
        n = len(s)
        prefix = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(ch) - 97))
        res = []
        for l, r, k in queries:
            mask = prefix[r + 1] ^ prefix[l]
            odd = mask.bit_count()
            res.append((odd // 2) <= k)
        return res
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canMakePaliQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = (int)strlen(s);
    unsigned int *pref = (unsigned int *)malloc((n + 1) * sizeof(unsigned int));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] ^ (1u << (s[i] - 'a'));
    }

    bool *ans = (bool *)malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        int k = queries[i][2];
        unsigned int mask = pref[r + 1] ^ pref[l];
        int odd = __builtin_popcount(mask);
        int need = odd / 2;
        ans[i] = (k >= need);
    }

    free(pref);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<bool> CanMakePaliQueries(string s, int[][] queries) {
        int n = s.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int bit = 1 << (s[i] - 'a');
            pref[i + 1] = pref[i] ^ bit;
        }

        var result = new List<bool>(queries.Length);
        foreach (var q in queries) {
            int left = q[0];
            int right = q[1];
            int k = q[2];

            int mask = pref[right + 1] ^ pref[left];
            int odd = 0;
            while (mask != 0) {
                odd++;
                mask &= mask - 1; // remove lowest set bit
            }

            int need = Math.Max(0, (odd - 1) / 2);
            result.Add(k >= need);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canMakePaliQueries = function(s, queries) {
    const n = s.length;
    const prefix = new Uint32Array(n + 1);
    for (let i = 0; i < n; ++i) {
        const bit = 1 << (s.charCodeAt(i) - 97);
        prefix[i + 1] = prefix[i] ^ bit;
    }
    
    const popcnt = (x) => {
        x >>>= 0;
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };
    
    const ans = [];
    for (const [l, r, k] of queries) {
        const mask = prefix[r + 1] ^ prefix[l];
        const odd = popcnt(mask);
        ans.push(odd <= 2 * k + 1);
    }
    return ans;
};
```

## Typescript

```typescript
function canMakePaliQueries(s: string, queries: number[][]): boolean[] {
    const n = s.length;
    const prefix: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        const bit = 1 << (s.charCodeAt(i) - 97);
        prefix[i + 1] = prefix[i] ^ bit;
    }

    const res: boolean[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [l, r, k] = queries[i];
        let mask = prefix[r + 1] ^ prefix[l];
        let odd = 0;
        while (mask) {
            odd++;
            mask &= mask - 1;
        }
        let need = 0;
        if (odd > 1) {
            need = (odd - 1) >> 1; // floor division by 2
        }
        res[i] = k >= need;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canMakePaliQueries($s, $queries) {
        $n = strlen($s);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $pref[$i + 1] = $pref[$i] ^ (1 << $c);
        }

        $ans = [];
        foreach ($queries as $q) {
            [$l, $r, $k] = $q;
            $mask = $pref[$r + 1] ^ $pref[$l];

            // popcount of mask (number of odd frequencies)
            $odd = 0;
            while ($mask) {
                $mask &= ($mask - 1);
                $odd++;
            }

            $len = $r - $l + 1;
            $allowedOdd = $len % 2; // 0 for even length, 1 for odd length
            if ($odd <= $k * 2 + $allowedOdd) {
                $ans[] = true;
            } else {
                $ans[] = false;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func canMakePaliQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        let n = s.count
        var prefix = [Int](repeating: 0, count: n + 1)
        let chars = Array(s.utf8)   // ASCII codes of characters
        
        for i in 0..<n {
            let shift = Int(chars[i] - 97)          // 'a' is 97
            let bit = 1 << shift
            prefix[i + 1] = prefix[i] ^ bit
        }
        
        var answer = [Bool]()
        answer.reserveCapacity(queries.count)
        
        for q in queries {
            let left = q[0]
            let right = q[1]
            let k = q[2]
            
            let mask = prefix[right + 1] ^ prefix[left]
            let oddCount = mask.nonzeroBitCount
            let length = right - left + 1
            let allowedOdd = length & 1               // 1 if length is odd, else 0
            let neededChanges = max(0, (oddCount - allowedOdd) / 2)
            
            answer.append(k >= neededChanges)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakePaliQueries(s: String, queries: Array<IntArray>): List<Boolean> {
        val n = s.length
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            val bit = 1 shl (s[i] - 'a')
            pref[i + 1] = pref[i] xor bit
        }
        val res = BooleanArray(queries.size)
        for (idx in queries.indices) {
            val q = queries[idx]
            val l = q[0]
            val r = q[1]
            val k = q[2]
            val mask = pref[r + 1] xor pref[l]
            val oddCount = Integer.bitCount(mask)
            val need = oddCount / 2
            res[idx] = k >= need
        }
        return res.toList()
    }
}
```

## Dart

```dart
class Solution {
  List<bool> canMakePaliQueries(String s, List<List<int>> queries) {
    int n = s.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      int bit = 1 << (s.codeUnitAt(i) - 97);
      pref[i + 1] = pref[i] ^ bit;
    }

    List<bool> ans = List.filled(queries.length, false);
    for (int idx = 0; idx < queries.length; idx++) {
      var q = queries[idx];
      int l = q[0], r = q[1], k = q[2];
      int mask = pref[r + 1] ^ pref[l];

      int odd = 0;
      while (mask != 0) {
        odd++;
        mask &= mask - 1;
      }

      int need = odd <= 1 ? 0 : ((odd - 1) >> 1);
      ans[idx] = k >= need;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func canMakePaliQueries(s string, queries [][]int) []bool {
	n := len(s)
	pref := make([]int, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] ^ (1 << (s[i] - 'a'))
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		l, r, k := q[0], q[1], q[2]
		mask := pref[r+1] ^ pref[l]
		odd := bits.OnesCount(uint(mask))
		if odd/2 <= k {
			ans[i] = true
		} else {
			ans[i] = false
		}
	}
	return ans
}
```

## Ruby

```ruby
def can_make_pali_queries(s, queries)
  n = s.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    bit = 1 << (s.getbyte(i) - 97)
    prefix[i + 1] = prefix[i] ^ bit
  end

  result = []
  queries.each do |l, r, k|
    mask = prefix[r + 1] ^ prefix[l]
    odd = mask.to_s(2).count('1')
    needed = odd / 2
    result << (k >= needed)
  end
  result
end
```

## Scala

```scala
object Solution {
    def canMakePaliQueries(s: String, queries: Array[Array[Int]]): List[Boolean] = {
        val n = s.length
        val pref = new Array[Int](n + 1)
        for (i <- 0 until n) {
            val bit = 1 << (s.charAt(i) - 'a')
            pref(i + 1) = pref(i) ^ bit
        }
        val ans = scala.collection.mutable.ArrayBuffer[Boolean]()
        for (q <- queries) {
            val left = q(0)
            val right = q(1)
            val k = q(2)
            val mask = pref(right + 1) ^ pref(left)
            val odd = Integer.bitCount(mask)
            ans += (odd / 2 <= k)
        }
        ans.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_make_pali_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut pref = vec![0u32; n + 1];
        for i in 0..n {
            let bit = (bytes[i] - b'a') as u32;
            pref[i + 1] = pref[i] ^ (1 << bit);
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let left = q[0] as usize;
            let right = q[1] as usize;
            let k = q[2] as usize;

            let mask = pref[right + 1] ^ pref[left];
            let odd_cnt = mask.count_ones() as usize;
            let needed = odd_cnt / 2;
            ans.push(k >= needed);
        }
        ans
    }
}
```

## Racket

```racket
(define (popcnt x)
  (let loop ((v x) (c 0))
    (if (= v 0)
        c
        (loop (bitwise-and v (sub1 v)) (+ c 1)))))

(define/contract (can-make-pali-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof boolean?))
  (let* ((n (string-length s))
         (prefix (make-vector (+ n 1) 0)))
    ;; build prefix parity masks
    (for ([i (in-range n)])
      (let* ((ch (char->integer (string-ref s i)))
             (bit (- ch (char->integer #\a))))
        (vector-set! prefix (add1 i)
                     (bitwise-xor (vector-ref prefix i)
                                  (arithmetic-shift 1 bit)))))
    ;; evaluate queries
    (let loop ((qs queries) (ans '()))
      (if (null? qs)
          (reverse ans)
          (let* ((q (car qs))
                 (l (list-ref q 0))
                 (r (list-ref q 1))
                 (k (list-ref q 2))
                 (mask (bitwise-xor (vector-ref prefix (add1 r))
                                    (vector-ref prefix l)))
                 (odd (popcnt mask))
                 (need (quotient odd 2))) ; minimal replacements needed
            (loop (cdr qs) (cons (<= need k) ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([can_make_pali_queries/2]).

-spec can_make_pali_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [boolean()].
can_make_pali_queries(S, Queries) ->
    PrefixTuple = build_prefix_tuple(S),
    lists:map(
        fun([L, R, K]) ->
            MaskL = element(L + 1, PrefixTuple),
            MaskR = element(R + 2, PrefixTuple), % prefix up to R inclusive
            Odd = popcnt(MaskL bxor MaskR),
            Needed = case Odd of
                0 -> 0;
                1 -> 0;
                _ -> (Odd - 1) div 2
            end,
            K >= Needed
        end,
        Queries).

%% Build a tuple where element(Index+1) is the parity mask of first Index characters.
build_prefix_tuple(S) ->
    Bytes = binary_to_list(S),
    MasksRev = build_masks(Bytes, [0]),
    PrefixList = lists:reverse(MasksRev),
    list_to_tuple(PrefixList).

%% Accumulator holds masks in reverse order; head is most recent mask.
build_masks([], Acc) -> Acc;
build_masks([C | Rest], [PrevMask | _] = Acc) ->
    Bit = 1 bsl (C - $a),
    NewMask = PrevMask bxor Bit,
    build_masks(Rest, [NewMask | Acc]).

%% Count set bits (popcount); max 26 bits.
popcnt(0) -> 0;
popcnt(N) -> 1 + popcnt(N band (N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_pali_queries(s :: String.t(), queries :: [[integer]]) :: [boolean]
  def can_make_pali_queries(s, queries) do
    pref = build_prefix(:binary.bin_to_list(s))

    Enum.map(queries, fn [l, r, k] ->
      mask = Bitwise.bxor(elem(pref, r + 1), elem(pref, l))
      odd = bit_count(mask)
      need = div(odd, 2)
      k >= need
    end)
  end

  defp build_prefix(chars) do
    {list_rev, _} =
      Enum.reduce(chars, {[0], 0}, fn c, {acc, mask} ->
        bit = Bitwise.bsl(1, c - ?a)
        new_mask = Bitwise.bxor(mask, bit)
        {[new_mask | acc], new_mask}
      end)

    List.to_tuple(Enum.reverse(list_rev))
  end

  defp bit_count(0), do: 0
  defp bit_count(x) do
    1 + bit_count(Bitwise.band(x, x - 1))
  end
end
```
