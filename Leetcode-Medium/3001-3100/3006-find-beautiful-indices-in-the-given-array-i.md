# 3006. Find Beautiful Indices in the Given Array I

## Cpp

```cpp
class Solution {
public:
    vector<int> beautifulIndices(string s, string a, string b, int k) {
        int n = s.size();
        int la = a.size(), lb = b.size();
        vector<int> posA, posB;
        for (int i = 0; i + la <= n; ++i) {
            if (s.compare(i, la, a) == 0) posA.push_back(i);
        }
        for (int i = 0; i + lb <= n; ++i) {
            if (s.compare(i, lb, b) == 0) posB.push_back(i);
        }
        vector<int> ans;
        for (int i : posA) {
            int left = i - k;
            auto it = lower_bound(posB.begin(), posB.end(), left);
            if (it != posB.end() && abs(*it - i) <= k) {
                ans.push_back(i);
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
    public List<Integer> beautifulIndices(String s, String a, String b, int k) {
        int n = s.length();
        int lenA = a.length();
        int lenB = b.length();

        List<Integer> aPos = new ArrayList<>();
        List<Integer> bPos = new ArrayList<>();

        for (int i = 0; i + lenA <= n; ++i) {
            if (s.regionMatches(i, a, 0, lenA)) {
                aPos.add(i);
            }
        }

        for (int i = 0; i + lenB <= n; ++i) {
            if (s.regionMatches(i, b, 0, lenB)) {
                bPos.add(i);
            }
        }

        List<Integer> result = new ArrayList<>();
        if (bPos.isEmpty()) return result;

        for (int i : aPos) {
            int left = i - k;
            int right = i + k;
            int idx = lowerBound(bPos, left);
            if (idx < bPos.size() && bPos.get(idx) <= right) {
                result.add(i);
            }
        }

        return result;
    }

    private int lowerBound(List<Integer> list, int target) {
        int lo = 0, hi = list.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid) < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        n = len(s)
        la, lb = len(a), len(b)
        pos_a = []
        pos_b = []
        for i in range(n - la + 1):
            if s[i:i+la] == a:
                pos_a.append(i)
        for i in range(n - lb + 1):
            if s[i:i+lb] == b:
                pos_b.append(i)
        import bisect
        res = []
        for i in pos_a:
            idx = bisect.bisect_left(pos_b, i)
            ok = False
            if idx < len(pos_b) and abs(pos_b[idx] - i) <= k:
                ok = True
            elif idx > 0 and abs(pos_b[idx-1] - i) <= k:
                ok = True
            if ok:
                res.append(i)
        return res
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        la, lb = len(a), len(b)

        occ_a = []
        for i in range(n - la + 1):
            if s[i:i+la] == a:
                occ_a.append(i)

        occ_b = []
        for i in range(n - lb + 1):
            if s[i:i+lb] == b:
                occ_b.append(i)

        res = []
        for i in occ_a:
            pos = bisect.bisect_left(occ_b, i)
            ok = False
            if pos < len(occ_b) and abs(occ_b[pos] - i) <= k:
                ok = True
            if pos > 0 and abs(occ_b[pos-1] - i) <= k:
                ok = True
            if ok:
                res.append(i)

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* beautifulIndices(char* s, char* a, char* b, int k, int* returnSize) {
    int n = (int)strlen(s);
    int la = (int)strlen(a);
    int lb = (int)strlen(b);

    int *posA = (int*)malloc(n * sizeof(int));
    int cntA = 0;
    for (int i = 0; i + la <= n; ++i) {
        if (strncmp(s + i, a, la) == 0) {
            posA[cntA++] = i;
        }
    }

    int *posB = (int*)malloc(n * sizeof(int));
    int cntB = 0;
    for (int i = 0; i + lb <= n; ++i) {
        if (strncmp(s + i, b, lb) == 0) {
            posB[cntB++] = i;
        }
    }

    int *res = (int*)malloc(cntA * sizeof(int));
    int resCnt = 0;
    int idxB = 0;

    for (int ai = 0; ai < cntA; ++ai) {
        int iPos = posA[ai];
        while (idxB < cntB && posB[idxB] < iPos - k) {
            ++idxB;
        }
        if (idxB < cntB && posB[idxB] <= iPos + k) {
            res[resCnt++] = iPos;
        }
    }

    free(posA);
    free(posB);

    *returnSize = resCnt;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> BeautifulIndices(string s, string a, string b, int k) {
        int n = s.Length;
        int lenA = a.Length;
        int lenB = b.Length;
        
        List<int> aPos = new List<int>();
        for (int i = 0; i + lenA <= n; ++i) {
            bool match = true;
            for (int j = 0; j < lenA; ++j) {
                if (s[i + j] != a[j]) { match = false; break; }
            }
            if (match) aPos.Add(i);
        }
        
        List<int> bPos = new List<int>();
        for (int i = 0; i + lenB <= n; ++i) {
            bool match = true;
            for (int j = 0; j < lenB; ++j) {
                if (s[i + j] != b[j]) { match = false; break; }
            }
            if (match) bPos.Add(i);
        }
        
        List<int> result = new List<int>();
        foreach (int i in aPos) {
            int left = i - k;
            int right = i + k;
            int idx = bPos.BinarySearch(left);
            if (idx < 0) idx = ~idx;
            if (idx < bPos.Count && bPos[idx] <= right) {
                result.Add(i);
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
 * @param {string} a
 * @param {string} b
 * @param {number} k
 * @return {number[]}
 */
var beautifulIndices = function(s, a, b, k) {
    const n = s.length;
    const lenA = a.length;
    const lenB = b.length;
    const aPos = [];
    for (let i = 0; i <= n - lenA; ++i) {
        if (s.slice(i, i + lenA) === a) aPos.push(i);
    }
    const bPos = [];
    for (let i = 0; i <= n - lenB; ++i) {
        if (s.slice(i, i + lenB) === b) bPos.push(i);
    }
    const res = [];
    if (bPos.length === 0) return res;
    for (const i of aPos) {
        const left = i - k;
        const right = i + k;
        // binary search first bPos >= left
        let lo = 0, hi = bPos.length - 1, idx = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (bPos[mid] >= left) {
                idx = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        if (idx !== -1 && bPos[idx] <= right) res.push(i);
    }
    return res;
};
```

## Typescript

```typescript
function beautifulIndices(s: string, a: string, b: string, k: number): number[] {
    const n = s.length;
    const la = a.length;
    const lb = b.length;
    const aPos: number[] = [];
    const bPos: number[] = [];

    for (let i = 0; i + la <= n; i++) {
        if (s.substr(i, la) === a) aPos.push(i);
    }
    for (let i = 0; i + lb <= n; i++) {
        if (s.substr(i, lb) === b) bPos.push(i);
    }

    const res: number[] = [];
    let left = 0;
    for (const i of aPos) {
        while (left < bPos.length && bPos[left] < i - k) left++;
        if (left < bPos.length && bPos[left] <= i + k) {
            res.push(i);
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $a
     * @param String $b
     * @param Integer $k
     * @return Integer[]
     */
    function beautifulIndices($s, $a, $b, $k) {
        $n = strlen($s);
        $lenA = strlen($a);
        $lenB = strlen($b);

        $aPos = [];
        for ($i = 0; $i + $lenA <= $n; $i++) {
            if (substr($s, $i, $lenA) === $a) {
                $aPos[] = $i;
            }
        }

        $bPos = [];
        for ($i = 0; $i + $lenB <= $n; $i++) {
            if (substr($s, $i, $lenB) === $b) {
                $bPos[] = $i;
            }
        }

        $res = [];
        if (empty($bPos)) {
            return $res;
        }

        $bCount = count($bPos);
        foreach ($aPos as $idx) {
            // binary search for first bPos >= idx
            $l = 0;
            $r = $bCount - 1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($bPos[$mid] < $idx) {
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }

            $ok = false;
            if ($l < $bCount && abs($bPos[$l] - $idx) <= $k) {
                $ok = true;
            }
            if ($l - 1 >= 0 && abs($bPos[$l - 1] - $idx) <= $k) {
                $ok = true;
            }

            if ($ok) {
                $res[] = $idx;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulIndices(_ s: String, _ a: String, _ b: String, _ k: Int) -> [Int] {
        let sBytes = Array(s.utf8)
        let aBytes = Array(a.utf8)
        let bBytes = Array(b.utf8)
        let n = sBytes.count
        let la = aBytes.count
        let lb = bBytes.count
        
        var aPos = [Int]()
        if la <= n {
            for i in 0...(n - la) {
                var match = true
                for t in 0..<la where match {
                    if sBytes[i + t] != aBytes[t] { match = false }
                }
                if match { aPos.append(i) }
            }
        }
        
        var bPos = [Int]()
        if lb <= n {
            for i in 0...(n - lb) {
                var match = true
                for t in 0..<lb where match {
                    if sBytes[i + t] != bBytes[t] { match = false }
                }
                if match { bPos.append(i) }
            }
        }
        
        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }
        
        var result = [Int]()
        for i in aPos {
            // need any b position within [i - k, i + k]
            let left = i - k
            let idx = lowerBound(bPos, left)
            var beautiful = false
            if idx < bPos.count && abs(bPos[idx] - i) <= k {
                beautiful = true
            } else if idx > 0 && abs(bPos[idx - 1] - i) <= k {
                beautiful = true
            }
            if beautiful { result.append(i) }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulIndices(s: String, a: String, b: String, k: Int): List<Int> {
        val n = s.length
        val lenA = a.length
        val lenB = b.length

        val isA = BooleanArray(n)
        for (i in 0..n - lenA) {
            if (s.regionMatches(i, a, 0, lenA)) {
                isA[i] = true
            }
        }

        val isB = BooleanArray(n)
        for (i in 0..n - lenB) {
            if (s.regionMatches(i, b, 0, lenB)) {
                isB[i] = true
            }
        }

        val pref = IntArray(n)
        var sum = 0
        for (i in 0 until n) {
            if (isB[i]) sum++
            pref[i] = sum
        }

        val result = mutableListOf<Int>()
        for (i in 0..n - lenA) {
            if (!isA[i]) continue
            var left = i - k
            if (left < 0) left = 0
            var right = i + k
            if (right >= n) right = n - 1

            val count = pref[right] - if (left > 0) pref[left - 1] else 0
            if (count > 0) {
                result.add(i)
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> beautifulIndices(String s, String a, String b, int k) {
    int n = s.length;
    int lenA = a.length;
    int lenB = b.length;
    List<int> posA = [];
    List<int> posB = [];

    for (int i = 0; i <= n - lenA; ++i) {
      if (s.startsWith(a, i)) posA.add(i);
    }
    for (int i = 0; i <= n - lenB; ++i) {
      if (s.startsWith(b, i)) posB.add(i);
    }

    List<int> res = [];
    if (posB.isEmpty) return res;

    for (int i in posA) {
      int low = i - k;
      int l = 0, r = posB.length;
      while (l < r) {
        int mid = (l + r) >> 1;
        if (posB[mid] < low) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      if (l < posB.length && posB[l] <= i + k) {
        res.add(i);
      }
    }

    return res;
  }
}
```

## Golang

```go
func beautifulIndices(s string, a string, b string, k int) []int {
    n := len(s)
    la, lb := len(a), len(b)

    var posA []int
    for i := 0; i+la <= n; i++ {
        if s[i:i+la] == a {
            posA = append(posA, i)
        }
    }

    var posB []int
    for i := 0; i+lb <= n; i++ {
        if s[i:i+lb] == b {
            posB = append(posB, i)
        }
    }

    res := make([]int, 0)
    for _, i := range posA {
        lo, hi := 0, len(posB)
        for lo < hi {
            mid := (lo + hi) / 2
            if posB[mid] < i {
                lo = mid + 1
            } else {
                hi = mid
            }
        }

        ok := false
        if lo < len(posB) && abs(posB[lo]-i) <= k {
            ok = true
        }
        if lo-1 >= 0 && abs(posB[lo-1]-i) <= k {
            ok = true
        }
        if ok {
            res = append(res, i)
        }
    }

    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

## Ruby

```ruby
def beautiful_indices(s, a, b, k)
  n = s.length
  la = a.length
  lb = b.length

  pos_a = []
  if la <= n
    (0..n - la).each do |i|
      pos_a << i if s[i, la] == a
    end
  end

  pos_b = []
  if lb <= n
    (0..n - lb).each do |i|
      pos_b << i if s[i, lb] == b
    end
  end

  res = []
  j = 0
  m = pos_b.length

  pos_a.each do |i|
    while j < m && pos_b[j] < i - k
      j += 1
    end
    if j < m && (pos_b[j] - i).abs <= k
      res << i
    end
  end

  res
end
```

## Scala

```scala
object Solution {
    def beautifulIndices(s: String, a: String, b: String, k: Int): List[Int] = {
        val n = s.length
        val la = a.length
        val lb = b.length

        val listA = scala.collection.mutable.ArrayBuffer[Int]()
        val listB = scala.collection.mutable.ArrayBuffer[Int]()

        // find all occurrences of a
        for (i <- 0 to n - la) {
            if (s.regionMatches(i, a, 0, la)) listA += i
        }
        // find all occurrences of b
        for (i <- 0 to n - lb) {
            if (s.regionMatches(i, b, 0, lb)) listB += i
        }

        val res = scala.collection.mutable.ArrayBuffer[Int]()
        var j = 0
        val m = listB.length

        for (iIdx <- listA) {
            while (j < m && listB(j) < iIdx - k) {
                j += 1
            }
            if (j < m && listB(j) <= iIdx + k) {
                res += iIdx
            }
        }

        res.toList
    }
}
```

## Rust

```rust
use std::cmp;

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        let s_bytes = s.as_bytes();
        let a_bytes = a.as_bytes();
        let b_bytes = b.as_bytes();
        let n = s_bytes.len();
        let la = a_bytes.len();
        let lb = b_bytes.len();

        let mut a_pos: Vec<usize> = Vec::new();
        if la <= n {
            for i in 0..=n - la {
                if &s_bytes[i..i + la] == a_bytes {
                    a_pos.push(i);
                }
            }
        }

        let mut b_pos: Vec<usize> = Vec::new();
        if lb <= n {
            for i in 0..=n - lb {
                if &s_bytes[i..i + lb] == b_bytes {
                    b_pos.push(i);
                }
            }
        }

        let mut res: Vec<i32> = Vec::new();
        if b_pos.is_empty() {
            return res;
        }
        let k_usize = k as usize;

        for &i in a_pos.iter() {
            let left = if i >= k_usize { i - k_usize } else { 0 };
            match b_pos.binary_search(&left) {
                Ok(_) => res.push(i as i32),
                Err(idx) => {
                    if idx < b_pos.len() && b_pos[idx] <= i + k_usize {
                        res.push(i as i32);
                    }
                }
            }
        }

        res
    }
}
```

## Racket

```racket
(define (find-positions str pat)
  (let* ((n (string-length str))
         (m (string-length pat)))
    (if (> m n)
        '()
        (let loop ((i 0) (acc '()))
          (if (> i (- n m))
              (reverse acc)
              (if (string=? (substring str i (+ i m)) pat)
                  (loop (+ i 1) (cons i acc))
                  (loop (+ i 1) acc)))))))

(define/contract (beautiful-indices s a b k)
  (-> string? string? string? exact-integer? (listof exact-integer?))
  (let* ((posA (find-positions s a))
         (posB-list (find-positions s b))
         (posB (list->vector posB-list)))
    (if (or (null? posA) (= (vector-length posB) 0))
        '()
        (let loop ((as posA) (idx 0) (lenB (vector-length posB)) (res '()))
          (if (null? as)
              (reverse res)
              (let* ((i (car as))
                     (new-idx
                      (let advance ((j idx))
                        (if (and (< j lenB)
                                 (< (vector-ref posB j) (- i k)))
                            (advance (+ j 1))
                            j))))
                (if (and (< new-idx lenB)
                         (<= (vector-ref posB new-idx) (+ i k)))
                    (loop (cdr as) new-idx lenB (cons i res))
                    (loop (cdr as) new-idx lenB res))))))))
```

## Erlang

```erlang
-spec beautiful_indices(S :: unicode:unicode_binary(), A :: unicode:unicode_binary(), B :: unicode:unicode_binary(), K :: integer()) -> [integer()].
beautiful_indices(S, A, B, K) ->
    APos = positions(S, A),
    BPosList = positions(S, B),
    case BPosList of
        [] -> [];
        _  ->
            BTup = list_to_tuple(BPosList),
            BSize = tuple_size(BTup),
            process(APos, BTup, BSize, K, [])
    end.

positions(Str, Sub) ->
    LenStr = byte_size(Str),
    LenSub = byte_size(Sub),
    MaxStart = LenStr - LenSub,
    if
        MaxStart < 0 -> [];
        true -> positions_loop(0, MaxStart, Str, Sub, [], LenSub)
    end.

positions_loop(I, Max, Str, Sub, Acc, LenSub) when I > Max ->
    lists:reverse(Acc);
positions_loop(I, Max, Str, Sub, Acc, LenSub) ->
    case binary:part(Str, {I, LenSub}) of
        Sub -> positions_loop(I + 1, Max, Str, Sub, [I | Acc], LenSub);
        _   -> positions_loop(I + 1, Max, Str, Sub, Acc, LenSub)
    end.

process([], _BTup, _BSize, _K, Res) ->
    lists:reverse(Res);
process([I | Rest], BTup, BSize, K, Res) ->
    Lower = I - K,
    Upper = I + K,
    Idx = lower_bound(BTup, BSize, Lower),
    if
        Idx < BSize ->
            Val = element(Idx + 1, BTup),
            if Val =< Upper ->
                    process(Rest, BTup, BSize, K, [I | Res]);
               true ->
                    process(Rest, BTup, BSize, K, Res)
            end;
        true ->
            process(Rest, BTup, BSize, K, Res)
    end.

lower_bound(Tup, Size, Target) ->
    lower_bound(0, Size, Tup, Target).

lower_bound(Low, High, _Tup, _Target) when Low >= High ->
    Low;
lower_bound(Low, High, Tup, Target) ->
    Mid = (Low + High) div 2,
    Val = element(Mid + 1, Tup),
    if
        Val < Target -> lower_bound(Mid + 1, High, Tup, Target);
        true         -> lower_bound(Low, Mid, Tup, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_indices(String.t(), String.t(), String.t(), integer()) :: [integer()]
  def beautiful_indices(s, a, b, k) do
    a_pos = :binary.matches(s, a) |> Enum.map(&elem(&1, 0))
    b_pos = :binary.matches(s, b) |> Enum.map(&elem(&1, 0))

    {res_rev, _} =
      Enum.reduce(a_pos, {[], b_pos}, fn i, {acc, b_list} ->
        b_remaining = drop_while(b_list, fn j -> j < i - k end)

        case b_remaining do
          [] ->
            {acc, []}

          [head | _] = bl when head <= i + k ->
            {[i | acc], bl}

          [_head | _] = bl ->
            {acc, bl}
        end
      end)

    Enum.reverse(res_rev)
  end

  defp drop_while([h | t], fun) when is_function(fun, 1) do
    if fun.(h), do: drop_while(t, fun), else: [h | t]
  end

  defp drop_while([], _fun), do: []
end
```
