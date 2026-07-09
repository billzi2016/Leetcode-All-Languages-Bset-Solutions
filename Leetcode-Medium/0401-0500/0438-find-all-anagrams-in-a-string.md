# 0438. Find All Anagrams in a String

## Cpp

```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = s.size(), m = p.size();
        if (m > n) return {};
        vector<int> cntP(26, 0), cntW(26, 0);
        for (char c : p) cntP[c - 'a']++;
        for (int i = 0; i < m; ++i) cntW[s[i] - 'a']++;
        auto same = [&]() -> bool {
            for (int i = 0; i < 26; ++i)
                if (cntP[i] != cntW[i]) return false;
            return true;
        };
        vector<int> res;
        if (same()) res.push_back(0);
        for (int i = m; i < n; ++i) {
            cntW[s[i] - 'a']++;
            cntW[s[i - m] - 'a']--;
            if (same()) res.push_back(i - m + 1);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        int n = s.length(), m = p.length();
        if (n < m) return result;
        int[] need = new int[26];
        int[] window = new int[26];
        for (char c : p.toCharArray()) need[c - 'a']++;
        char[] arr = s.toCharArray();
        for (int i = 0; i < n; i++) {
            window[arr[i] - 'a']++;
            if (i >= m) {
                window[arr[i - m] - 'a']--;
            }
            if (i >= m - 1 && matches(need, window)) {
                result.add(i - m + 1);
            }
        }
        return result;
    }

    private boolean matches(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        if m > n:
            return []
        cnt = [0] * 26
        for i in range(m):
            cnt[ord(p[i]) - 97] -= 1
            cnt[ord(s[i]) - 97] += 1
        diff = sum(1 for x in cnt if x != 0)
        res = []
        if diff == 0:
            res.append(0)
        for i in range(m, n):
            out_idx = ord(s[i - m]) - 97
            in_idx = ord(s[i]) - 97

            # remove outgoing character
            if cnt[out_idx] == 0:
                diff += 1
            cnt[out_idx] -= 1
            if cnt[out_idx] == 0:
                diff -= 1

            # add incoming character
            if cnt[in_idx] == 0:
                diff += 1
            cnt[in_idx] += 1
            if cnt[in_idx] == 0:
                diff -= 1

            if diff == 0:
                res.append(i - m + 1)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        cnt = [0] * 26
        for ch in p:
            cnt[ord(ch) - 97] -= 1
        for i in range(m):
            cnt[ord(s[i]) - 97] += 1

        def all_zero() -> bool:
            for v in cnt:
                if v != 0:
                    return False
            return True

        res = []
        if all_zero():
            res.append(0)
        for i in range(m, n):
            cnt[ord(s[i]) - 97] += 1
            cnt[ord(s[i - m]) - 97] -= 1
            if all_zero():
                res.append(i - m + 1)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

int* findAnagrams(char* s, char* p, int* returnSize) {
    *returnSize = 0;
    if (!s || !p) return NULL;

    int n = (int)strlen(s);
    int m = (int)strlen(p);
    if (m > n) return NULL;

    int freqP[26] = {0};
    for (int i = 0; i < m; ++i)
        freqP[p[i] - 'a']++;

    int window[26] = {0};

    int maxRes = n - m + 1;
    int* res = (int*)malloc(sizeof(int) * maxRes);
    if (!res) return NULL;

    for (int i = 0; i < n; ++i) {
        window[s[i] - 'a']++;

        if (i >= m) {
            window[s[i - m] - 'a']--;
        }

        if (i >= m - 1) {
            int same = 1;
            for (int k = 0; k < 26; ++k) {
                if (window[k] != freqP[k]) {
                    same = 0;
                    break;
                }
            }
            if (same) {
                res[*returnSize] = i - m + 1;
                (*returnSize)++;
            }
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindAnagrams(string s, string p) {
        var result = new List<int>();
        int n = s.Length, m = p.Length;
        if (m > n) return result;

        int[] freq = new int[26];
        foreach (char c in p) freq[c - 'a']++;

        int left = 0, right = 0, need = m;
        while (right < n) {
            char rc = s[right];
            if (freq[rc - 'a'] > 0) need--;
            freq[rc - 'a']--;
            right++;

            if (need == 0) result.Add(left);

            if (right - left == m) {
                char lc = s[left];
                if (freq[lc - 'a'] >= 0) need++;
                freq[lc - 'a']++;
                left++;
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
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const result = [];
    const m = s.length, n = p.length;
    if (n > m) return result;

    const need = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        need[p.charCodeAt(i) - 97]++;
    }

    let left = 0, right = 0, count = n;
    while (right < m) {
        const idxR = s.charCodeAt(right) - 97;
        if (need[idxR] > 0) count--;
        need[idxR]--;
        right++;

        if (count === 0) result.push(left);

        if (right - left === n) {
            const idxL = s.charCodeAt(left) - 97;
            if (need[idxL] >= 0) count++;
            need[idxL]++;
            left++;
        }
    }

    return result;
};
```

## Typescript

```typescript
function findAnagrams(s: string, p: string): number[] {
    const m = s.length, n = p.length;
    if (n > m) return [];

    const diff = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        diff[p.charCodeAt(i) - 97]++;
    }

    let zero = 0;
    for (let i = 0; i < 26; i++) if (diff[i] === 0) zero++;

    const res: number[] = [];

    for (let i = 0; i < m; i++) {
        // add s[i]
        let idxAdd = s.charCodeAt(i) - 97;
        if (diff[idxAdd] === 0) zero--;
        diff[idxAdd]--;
        if (diff[idxAdd] === 0) zero++;

        // remove character leaving the window
        if (i >= n) {
            let idxRem = s.charCodeAt(i - n) - 97;
            if (diff[idxRem] === 0) zero--;
            diff[idxRem]++;
            if (diff[idxRem] === 0) zero++;
        }

        // check for anagram
        if (i >= n - 1 && zero === 26) {
            res.push(i - n + 1);
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
     * @param String $p
     * @return Integer[]
     */
    function findAnagrams($s, $p) {
        $n = strlen($s);
        $m = strlen($p);
        if ($m > $n) {
            return [];
        }

        $cntP = array_fill(0, 26, 0);
        $cntW = array_fill(0, 26, 0);
        $base = ord('a');

        for ($i = 0; $i < $m; $i++) {
            $cntP[ord($p[$i]) - $base]++;
            $cntW[ord($s[$i]) - $base]++;
        }

        $res = [];
        if ($cntP === $cntW) {
            $res[] = 0;
        }

        for ($i = $m; $i < $n; $i++) {
            $cntW[ord($s[$i]) - $base]++;               // add new char
            $cntW[ord($s[$i - $m]) - $base]--;           // remove old char
            if ($cntP === $cntW) {
                $res[] = $i - $m + 1;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        let sBytes = Array(s.utf8)
        let pBytes = Array(p.utf8)
        let n = sBytes.count
        let m = pBytes.count
        if n < m { return [] }
        
        var need = [Int](repeating: 0, count: 26)
        for b in pBytes {
            need[Int(b - 97)] += 1
        }
        
        var window = [Int](repeating: 0, count: 26)
        var result = [Int]()
        var left = 0
        var right = 0
        
        while right < n {
            let idx = Int(sBytes[right] - 97)
            window[idx] += 1
            
            if right - left + 1 == m {
                if window == need {
                    result.append(left)
                }
                let leftIdx = Int(sBytes[left] - 97)
                window[leftIdx] -= 1
                left += 1
            }
            right += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAnagrams(s: String, p: String): List<Int> {
        val result = mutableListOf<Int>()
        if (p.length > s.length) return result

        val need = IntArray(26)
        for (c in p) {
            need[c - 'a']++
        }

        val window = IntArray(26)
        val m = p.length
        for (i in s.indices) {
            val idxAdd = s[i] - 'a'
            window[idxAdd]++

            if (i >= m) {
                val idxRemove = s[i - m] - 'a'
                window[idxRemove]--
            }

            if (i >= m - 1) {
                var match = true
                for (j in 0 until 26) {
                    if (window[j] != need[j]) {
                        match = false
                        break
                    }
                }
                if (match) {
                    result.add(i - m + 1)
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findAnagrams(String s, String p) {
    int n = s.length, m = p.length;
    if (m > n) return [];

    List<int> pCount = List.filled(26, 0);
    List<int> sCount = List.filled(26, 0);

    for (int i = 0; i < m; i++) {
      pCount[p.codeUnitAt(i) - 97]++;
      sCount[s.codeUnitAt(i) - 97]++;
    }

    int matches = 0;
    for (int i = 0; i < 26; i++) {
      if (pCount[i] == sCount[i]) matches++;
    }

    List<int> result = [];
    if (matches == 26) result.add(0);

    for (int i = m; i < n; i++) {
      int addIdx = s.codeUnitAt(i) - 97;
      int removeIdx = s.codeUnitAt(i - m) - 97;

      // Add new character
      if (sCount[addIdx] == pCount[addIdx]) matches--;
      sCount[addIdx]++;
      if (sCount[addIdx] == pCount[addIdx]) matches++;

      // Remove old character
      if (sCount[removeIdx] == pCount[removeIdx]) matches--;
      sCount[removeIdx]--;
      if (sCount[removeIdx] == pCount[removeIdx]) matches++;

      if (matches == 26) result.add(i - m + 1);
    }

    return result;
  }
}
```

## Golang

```go
func findAnagrams(s string, p string) []int {
    n, m := len(s), len(p)
    if m > n {
        return []int{}
    }
    var need [26]int
    for i := 0; i < m; i++ {
        need[p[i]-'a']++
    }
    var window [26]int
    for i := 0; i < m; i++ {
        window[s[i]-'a']++
    }
    res := []int{}
    if need == window {
        res = append(res, 0)
    }
    for i := m; i < n; i++ {
        window[s[i]-'a']++
        window[s[i-m]-'a']--
        if need == window {
            res = append(res, i-m+1)
        }
    }
    return res
}
```

## Ruby

```ruby
def find_anagrams(s, p)
  n = s.length
  m = p.length
  return [] if m > n

  a_ord = 'a'.ord
  need = Array.new(26, 0)
  window = Array.new(26, 0)

  p.each_byte { |b| need[b - a_ord] += 1 }
  s_bytes = s.bytes

  (0...m).each do |i|
    window[s_bytes[i] - a_ord] += 1
  end

  diff = 0
  26.times { |i| diff += 1 if need[i] != window[i] }

  res = []
  res << 0 if diff.zero?

  (m...n).each do |i|
    out_idx = s_bytes[i - m] - a_ord
    in_idx = s_bytes[i] - a_ord

    # remove outgoing character
    diff += 1 if window[out_idx] == need[out_idx]
    window[out_idx] -= 1
    diff -= 1 if window[out_idx] == need[out_idx]

    # add incoming character
    diff += 1 if window[in_idx] == need[in_idx]
    window[in_idx] += 1
    diff -= 1 if window[in_idx] == need[in_idx]

    res << (i - m + 1) if diff.zero?
  end

  res
end
```

## Scala

```scala
object Solution {
    def findAnagrams(s: String, p: String): List[Int] = {
        val n = s.length
        val m = p.length
        if (m > n) return Nil

        val need = new Array[Int](26)
        for (c <- p) {
            need(c - 'a') += 1
        }

        val window = new Array[Int](26)
        val res = scala.collection.mutable.ListBuffer[Int]()

        var i = 0
        while (i < n) {
            val addIdx = s.charAt(i) - 'a'
            window(addIdx) += 1

            if (i >= m) {
                val removeIdx = s.charAt(i - m) - 'a'
                window(removeIdx) -= 1
            }

            if (i >= m - 1 && java.util.Arrays.equals(need, window)) {
                res += (i - m + 1)
            }
            i += 1
        }

        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let n = s_bytes.len();
        let m = p_bytes.len();
        if m > n {
            return vec![];
        }
        let mut need = [0i32; 26];
        for &b in p_bytes {
            need[(b - b'a') as usize] += 1;
        }
        let mut window = [0i32; 26];
        for i in 0..m {
            window[(s_bytes[i] - b'a') as usize] += 1;
        }
        let mut res = Vec::new();
        if window == need {
            res.push(0);
        }
        for i in m..n {
            let add_idx = (s_bytes[i] - b'a') as usize;
            window[add_idx] += 1;
            let rm_idx = (s_bytes[i - m] - b'a') as usize;
            window[rm_idx] -= 1;
            if window == need {
                res.push((i + 1 - m) as i32);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (find-anagrams s p)
  (-> string? string? (listof exact-integer?))
  (let* ((n (string-length s))
         (m (string-length p)))
    (if (> m n)
        '()
        (let ((freqP (make-vector 26 0))
              (freqW (make-vector 26 0)))
          (define (char-index ch)
            (- (char->integer ch) (char->integer #\a)))
          ;; build frequency for p
          (for ([i (in-range m)])
            (let* ((idx (char-index (string-ref p i))))
              (vector-set! freqP idx (+ 1 (vector-ref freqP idx)))))
          ;; initial window in s
          (for ([i (in-range m)])
            (let* ((idx (char-index (string-ref s i))))
              (vector-set! freqW idx (+ 1 (vector-ref freqW idx)))))
          (define (equal-freq?)
            (let loop ((i 0))
              (or (= i 26)
                  (and (= (vector-ref freqP i) (vector-ref freqW i))
                       (loop (+ i 1))))))
          (let rec ((i 0) (acc '()))
            (if (> i (- n m))
                (reverse acc)
                (let ((new-acc (if (equal-freq?) (cons i acc) acc)))
                  (when (< (+ i m) n)
                    (let* ((out-idx (char-index (string-ref s i)))
                           (in-idx  (char-index (string-ref s (+ i m)))))
                      (vector-set! freqW out-idx (- (vector-ref freqW out-idx) 1))
                      (vector-set! freqW in-idx (+ (vector-ref freqW in-idx) 1))))
                  (rec (+ i 1) new-acc)))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_anagrams/2]).
-spec find_anagrams(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> [integer()].
find_anagrams(S, P) ->
    LenS = byte_size(S),
    LenP = byte_size(P),
    if
        LenP > LenS -> [];
        true ->
            PCounts = make_counts(P, LenP, erlang:make_tuple(26, 0)),
            InitWindow = init_window(S, LenP - 1, erlang:make_tuple(26, 0)),
            slide(S, LenS, LenP, 0, InitWindow, PCounts, [])
    end.

%% Build frequency tuple for a binary of length N
make_counts(_Bin, 0, Tuple) -> Tuple;
make_counts(Bin, N, Tuple) ->
    Char = binary:at(Bin, N - 1),
    NewTuple = inc_count(Tuple, Char),
    make_counts(Bin, N - 1, NewTuple).

%% Initialize window counts for first K characters
init_window(_Bin, 0, Tuple) -> Tuple;
init_window(Bin, K, Tuple) ->
    Char = binary:at(Bin, K - 1),
    NewTuple = inc_count(Tuple, Char),
    init_window(Bin, K - 1, NewTuple).

%% Sliding window processing
slide(_S, LenS, LenP, StartIdx, _WindowCounts, _PCounts, Acc) when StartIdx > LenS - LenP ->
    lists:reverse(Acc);
slide(S, LenS, LenP, StartIdx, WindowCounts, PCounts, Acc) ->
    NewCharPos = StartIdx + LenP - 1,
    CharIn = binary:at(S, NewCharPos),
    WC1 = inc_count(WindowCounts, CharIn),

    Acc1 = case WC1 == PCounts of
               true -> [StartIdx | Acc];
               false -> Acc
           end,

    CharOut = binary:at(S, StartIdx),
    WC2 = dec_count(WC1, CharOut),

    slide(S, LenS, LenP, StartIdx + 1, WC2, PCounts, Acc1).

%% Increment count for a character in the tuple
inc_count(Tuple, Char) ->
    Index = Char - $a + 1,
    Old = element(Index, Tuple),
    setelement(Index, Tuple, Old + 1).

%% Decrement count for a character in the tuple
dec_count(Tuple, Char) ->
    Index = Char - $a + 1,
    Old = element(Index, Tuple),
    setelement(Index, Tuple, Old - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_anagrams(s :: String.t(), p :: String.t()) :: [integer()]
  def find_anagrams(s, p) do
    ls = String.length(s)
    lp = String.length(p)

    if lp > ls do
      []
    else
      s_codes = String.to_charlist(s)
      p_codes = String.to_charlist(p)

      freq_p = build_freq(p_codes)

      {_, _, res, _} =
        Enum.reduce(Enum.with_index(s_codes), {:queue.new(), :array.new(26, default: 0), [], freq_p},
          fn {code, i}, {q, win, acc_res, fp} ->
            idx = code - ?a
            cur = :array.get(idx, win)
            win = :array.set(idx, cur + 1, win)

            q = :queue.in(code, q)

            if :queue.len(q) > lp do
              {{:value, old}, q2} = :queue.out(q)
              idx_old = old - ?a
              cur_old = :array.get(idx_old, win)
              win = :array.set(idx_old, cur_old - 1, win)
              q = q2
            end

            acc_res =
              if :queue.len(q) == lp and arrays_equal?(win, fp) do
                [i - lp + 1 | acc_res]
              else
                acc_res
              end

            {q, win, acc_res, fp}
          end)

      Enum.reverse(res)
    end
  end

  defp build_freq(codes) do
    Enum.reduce(codes, :array.new(26, default: 0), fn code, arr ->
      idx = code - ?a
      cur = :array.get(idx, arr)
      :array.set(idx, cur + 1, arr)
    end)
  end

  defp arrays_equal?(arr1, arr2) do
    Enum.all?(0..25, fn i -> :array.get(i, arr1) == :array.get(i, arr2) end)
  end
end
```
