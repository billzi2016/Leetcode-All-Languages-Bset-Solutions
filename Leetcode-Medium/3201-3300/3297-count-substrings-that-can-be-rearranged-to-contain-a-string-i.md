# 3297. Count Substrings That Can Be Rearranged to Contain a String I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        if (m > n) return 0;
        int need[26] = {0};
        for (char c : word2) need[c - 'a']++;
        long long ans = 0;
        int cur[26] = {0};
        int missing = m;               // total characters still needed
        int r = 0;                     // exclusive right pointer

        for (int l = 0; l < n; ++l) {
            while (r < n && missing > 0) {
                int idx = word1[r] - 'a';
                if (cur[idx] < need[idx]) --missing;
                ++cur[idx];
                ++r;
            }
            if (missing == 0) {
                ans += static_cast<long long>(n - (r - 1));
            } else {
                break; // cannot satisfy for this and further l
            }
            int idxL = word1[l] - 'a';
            if (cur[idxL] <= need[idxL]) ++missing;
            --cur[idxL];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long validSubstringCount(String word1, String word2) {
        int n = word1.length();
        int[] req = new int[26];
        for (int i = 0; i < word2.length(); i++) {
            req[word2.charAt(i) - 'a']++;
        }
        int missing = 0;
        for (int v : req) missing += v;

        int[] cur = new int[26];
        long ans = 0;
        int l = 0, r = -1;

        while (l < n) {
            while (r + 1 < n && missing > 0) {
                r++;
                int idx = word1.charAt(r) - 'a';
                cur[idx]++;
                if (cur[idx] <= req[idx]) {
                    missing--;
                }
            }
            if (missing > 0) break; // cannot satisfy for this and further l
            ans += (long) (n - r);
            int idxL = word1.charAt(l) - 'a';
            if (cur[idxL] <= req[idxL]) {
                missing++;
            }
            cur[idxL]--;
            l++;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        target = [0] * 26
        for ch in word2:
            target[ord(ch) - 97] += 1

        deficit = len(word2)          # total needed characters not yet satisfied
        cur = [0] * 26                # current window frequencies
        n = len(word1)
        r = 0                         # right pointer (exclusive)
        ans = 0

        for l in range(n):
            while r < n and deficit > 0:
                idx = ord(word1[r]) - 97
                if cur[idx] < target[idx]:
                    deficit -= 1
                cur[idx] += 1
                r += 1

            if deficit == 0:
                ans += n - r + 1      # all extensions to the right are valid
            else:
                break                 # cannot satisfy any further left positions

            # slide window: remove word1[l]
            idx = ord(word1[l]) - 97
            if cur[idx] <= target[idx]:
                deficit += 1
            cur[idx] -= 1

        return ans
```

## Python3

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        # frequency of needed characters
        need = [0] * 26
        for ch in word2:
            need[ord(ch) - 97] += 1

        diff = [-need[i] for i in range(26)]   # have - need
        bad = sum(1 for v in diff if v < 0)    # count of chars not yet satisfied

        r = 0
        ans = 0
        for l in range(n):
            while r < n and bad > 0:
                idx = ord(word1[r]) - 97
                before = diff[idx]
                diff[idx] += 1
                if before < 0 <= diff[idx]:
                    bad -= 1
                r += 1

            if bad == 0:
                ans += n - r + 1   # all extensions to the right are valid
            else:
                break  # cannot satisfy for this and any further left positions

            # move left pointer forward, remove word1[l] from window
            idx = ord(word1[l]) - 97
            before = diff[idx]
            diff[idx] -= 1
            if before >= 0 > diff[idx]:
                bad += 1

        return ans
```

## C

```c
#include <string.h>

long long validSubstringCount(char* word1, char* word2) {
    int need[26] = {0};
    for (int i = 0; word2[i]; ++i) {
        need[word2[i] - 'a']++;
    }
    
    int total_needed = 0;
    for (int i = 0; i < 26; ++i) total_needed += need[i];
    
    int n = strlen(word1);
    int cnt[26] = {0};
    int missing = total_needed;
    int r = 0;
    long long ans = 0;
    
    for (int l = 0; l < n; ++l) {
        while (r < n && missing > 0) {
            int idx = word1[r] - 'a';
            if (cnt[idx] < need[idx]) missing--;
            cnt[idx]++;
            r++;
        }
        if (missing == 0) {
            ans += (long long)(n - r + 1);
        }
        if (l < r) {
            int idx = word1[l] - 'a';
            if (cnt[idx] <= need[idx]) missing++;
            cnt[idx]--;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long ValidSubstringCount(string word1, string word2) {
        int[] req = new int[26];
        foreach (char ch in word2) req[ch - 'a']++;

        int missing = 0;
        for (int i = 0; i < 26; i++) missing += req[i];

        int n = word1.Length;
        int[] cur = new int[26];
        long ans = 0;
        int left = 0, right = 0;

        while (left < n) {
            while (right < n && missing > 0) {
                int idx = word1[right] - 'a';
                if (cur[idx] < req[idx]) missing--;
                cur[idx]++;
                right++;
            }

            if (missing == 0) {
                ans += n - right + 1;
            } else {
                break;
            }

            int leftIdx = word1[left] - 'a';
            if (cur[leftIdx] <= req[leftIdx]) missing++;
            cur[leftIdx]--;
            left++;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var validSubstringCount = function(word1, word2) {
    const n = word1.length;
    const need = new Array(26).fill(0);
    for (let i = 0; i < word2.length; ++i) {
        need[word2.charCodeAt(i) - 97]++;
    }
    const have = new Array(26).fill(0);
    let right = 0;
    let ans = 0;

    const satisfied = () => {
        for (let i = 0; i < 26; ++i) {
            if (have[i] < need[i]) return false;
        }
        return true;
    };

    for (let left = 0; left < n; ++left) {
        while (right < n && !satisfied()) {
            have[word1.charCodeAt(right) - 97]++;
            right++;
        }
        if (!satisfied()) break; // cannot satisfy any further substrings
        ans += n - right + 1;
        have[word1.charCodeAt(left) - 97]--;
    }

    return ans;
};
```

## Typescript

```typescript
function validSubstringCount(word1: string, word2: string): number {
    const n = word1.length;
    const need = new Array(26).fill(0);
    for (let i = 0; i < word2.length; i++) {
        need[word2.charCodeAt(i) - 97]++;
    }

    const cnt = new Array(26).fill(0);
    let r = -1;
    let ans = 0;

    const satisfies = (): boolean => {
        for (let i = 0; i < 26; i++) {
            if (cnt[i] < need[i]) return false;
        }
        return true;
    };

    for (let l = 0; l < n; l++) {
        while (r + 1 < n && !satisfies()) {
            r++;
            cnt[word1.charCodeAt(r) - 97]++;
        }
        if (!satisfies()) break;
        ans += n - r;
        cnt[word1.charCodeAt(l) - 97]--;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function validSubstringCount($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);
        if ($n < $m) return 0;

        // frequency needed for word2
        $need = array_fill(0, 26, 0);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($word2[$i]) - 97;
            $need[$idx]++;
        }

        // count of distinct letters that actually have a requirement
        $required = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($need[$i] > 0) $required++;
        }

        $cnt = array_fill(0, 26, 0);
        $satisfied = 0; // how many required letters meet the need
        $right = 0;
        $ans = 0;

        for ($left = 0; $left < $n; $left++) {
            while ($right < $n && $satisfied < $required) {
                $idx = ord($word1[$right]) - 97;
                if ($cnt[$idx] < $need[$idx]) {
                    $cnt[$idx]++;
                    if ($cnt[$idx] == $need[$idx]) {
                        $satisfied++;
                    }
                } else {
                    $cnt[$idx]++;
                }
                $right++;
            }

            if ($satisfied < $required) {
                break; // cannot satisfy for this and further left positions
            }

            // all substrings starting at $left with end >= $right-1 are valid
            $ans += ($n - $right + 1);

            // move left pointer forward, remove its character from window
            $idxL = ord($word1[$left]) - 97;
            if ($cnt[$idxL] <= $need[$idxL]) {
                if ($cnt[$idxL] == $need[$idxL]) {
                    $satisfied--;
                }
            }
            $cnt[$idxL]--;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func validSubstringCount(_ word1: String, _ word2: String) -> Int {
        let w1 = Array(word1.utf8)
        let w2 = Array(word2.utf8)
        let n = w1.count
        if n == 0 { return 0 }
        
        var req = [Int](repeating: 0, count: 26)
        for ch in w2 {
            let idx = Int(ch - 97)
            req[idx] += 1
        }
        var cur = [Int](repeating: 0, count: 26)
        let totalReq = req.reduce(0, +)
        var deficit = totalReq
        
        var left = 0
        var right = 0
        var ans = 0
        
        while left < n {
            while right < n && deficit > 0 {
                let idx = Int(w1[right] - 97)
                if cur[idx] < req[idx] { deficit -= 1 }
                cur[idx] += 1
                right += 1
            }
            if deficit == 0 {
                ans += n - right + 1
            } else {
                break
            }
            // slide left
            let idxL = Int(w1[left] - 97)
            if cur[idxL] <= req[idxL] { deficit += 1 }
            cur[idxL] -= 1
            left += 1
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validSubstringCount(word1: String, word2: String): Long {
        val n = word1.length
        if (word2.length > n) return 0L

        val need = IntArray(26)
        for (ch in word2) {
            need[ch - 'a']++
        }
        var missing = need.sum()
        val cur = IntArray(26)

        var r = 0
        var ans = 0L
        val chars = word1.toCharArray()

        for (l in 0 until n) {
            while (r < n && missing > 0) {
                val idx = chars[r] - 'a'
                cur[idx]++
                if (cur[idx] <= need[idx]) {
                    missing--
                }
                r++
            }
            if (missing == 0) {
                ans += (n - r + 1).toLong()
            } else {
                break
            }

            val idxL = chars[l] - 'a'
            if (cur[idxL] <= need[idxL]) {
                missing++
            }
            cur[idxL]--
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int validSubstringCount(String word1, String word2) {
    int n = word1.length;
    List<int> need = List.filled(26, 0);
    for (int i = 0; i < word2.length; i++) {
      need[word2.codeUnitAt(i) - 97]++;
    }

    // Quick impossibility check
    List<int> total = List.filled(26, 0);
    for (int i = 0; i < n; i++) {
      total[word1.codeUnitAt(i) - 97]++;
    }
    for (int c = 0; c < 26; c++) {
      if (need[c] > total[c]) return 0;
    }

    List<int> cur = List.filled(26, 0);
    int left = 0, right = 0;
    int ans = 0;

    bool satisfied() {
      for (int i = 0; i < 26; i++) {
        if (cur[i] < need[i]) return false;
      }
      return true;
    }

    while (left < n) {
      while (right < n && !satisfied()) {
        cur[word1.codeUnitAt(right) - 97]++;
        right++;
      }
      if (!satisfied()) break; // cannot satisfy any further substrings
      ans += n - (right - 1);
      cur[word1.codeUnitAt(left) - 97]--;
      left++;
    }

    return ans;
  }
}
```

## Golang

```go
func validSubstringCount(word1 string, word2 string) int64 {
    n := len(word1)
    var req [26]int
    missing := 0
    for i := 0; i < len(word2); i++ {
        idx := word2[i] - 'a'
        req[idx]++
        missing++
    }

    var cnt [26]int
    right := 0
    var ans int64

    for left := 0; left < n; left++ {
        // Expand the window until it satisfies the requirement or reaches the end.
        for right < n && missing > 0 {
            idx := word1[right] - 'a'
            if cnt[idx] < req[idx] {
                missing--
            }
            cnt[idx]++
            right++
        }

        if missing == 0 {
            // All substrings extending to any position >= right-1 are valid.
            ans += int64(n - right + 1)
        } else {
            break
        }

        // Move left pointer forward, updating counts and missing accordingly.
        idx := word1[left] - 'a'
        if cnt[idx] <= req[idx] {
            missing++
        }
        cnt[idx]--
    }

    return ans
}
```

## Ruby

```ruby
def valid_substring_count(word1, word2)
  n = word1.length
  m = word2.length
  return 0 if m > n

  target = Array.new(26, 0)
  word2.each_byte { |b| target[b - 97] += 1 }

  window = Array.new(26, 0)
  need = m
  right = 0
  ans = 0
  left = 0

  while left < n
    while right < n && need > 0
      idx = word1.getbyte(right) - 97
      if window[idx] < target[idx]
        need -= 1
      end
      window[idx] += 1
      right += 1
    end

    break if need > 0   # cannot satisfy any further windows

    ans += n - right + 1

    idx_left = word1.getbyte(left) - 97
    if window[idx_left] == target[idx_left]
      need += 1
    end
    window[idx_left] -= 1
    left += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
  def validSubstringCount(word1: String, word2: String): Long = {
    val n = word1.length
    val m = word2.length
    if (m > n) return 0L

    val need = new Array[Int](26)
    var i = 0
    while (i < m) {
      need(word2.charAt(i) - 'a') += 1
      i += 1
    }

    // prefix sums: pref[pos][c] = count of char c in word1[0..pos-1]
    val pref = Array.ofDim[Int](n + 1, 26)
    var pos = 0
    while (pos < n) {
      val cur = pref(pos)
      val nxt = pref(pos + 1)
      var c = 0
      while (c < 26) {
        nxt(c) = cur(c)
        c += 1
      }
      nxt(word1.charAt(pos) - 'a') += 1
      pos += 1
    }

    def satisfies(l: Int, r: Int): Boolean = {
      var c = 0
      while (c < 26) {
        if (pref(r + 1)(c) - pref(l)(c) < need(c)) return false
        c += 1
      }
      true
    }

    var total: Long = 0L
    var left = 0
    while (left < n) {
      var lo = left + m - 1
      if (lo >= n) {
        left += 1
        // no possible substring starting at left
        continue
      }
      var hi = n - 1
      var ansR = -1
      while (lo <= hi) {
        val mid = (lo + hi) >>> 1
        if (satisfies(left, mid)) {
          ansR = mid
          hi = mid - 1
        } else {
          lo = mid + 1
        }
      }
      if (ansR != -1) total += (n - ansR).toLong
      left += 1
    }

    total
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_substring_count(word1: String, word2: String) -> i64 {
        fn enough(freq: &[i32; 26], need: &[i32; 26]) -> bool {
            for i in 0..26 {
                if freq[i] < need[i] {
                    return false;
                }
            }
            true
        }

        let w1 = word1.as_bytes();
        let n = w1.len();

        let mut need = [0i32; 26];
        for &b in word2.as_bytes() {
            need[(b - b'a') as usize] += 1;
        }

        // quick reject if word2 longer than word1
        if word2.len() > n {
            return 0;
        }

        let mut freq = [0i32; 26];
        let mut right: usize = 0;
        let mut ans: i64 = 0;

        for left in 0..n {
            while right < n && !enough(&freq, &need) {
                let idx = (w1[right] - b'a') as usize;
                freq[idx] += 1;
                right += 1;
            }

            if enough(&freq, &need) {
                ans += (n - right + 1) as i64;
            } else {
                break; // cannot satisfy for this and further left positions
            }

            let idx_left = (w1[left] - b'a') as usize;
            freq[idx_left] -= 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (valid-substring-count word1 word2)
  (-> string? string? exact-integer?)
  (let* ((n (string-length word1))
         (m (string-length word2)))
    (if (< n m)
        0
        (let ((need (make-vector 26 0))
              (have (make-vector 26 0)))
          ;; frequency of word2
          (for ([i (in-range m)])
            (let* ((ch (string-ref word2 i))
                   (idx (- (char->integer ch) (char->integer #\a))))
              (vector-set! need idx (+ 1 (vector-ref need idx)))))
          (define missing m)
          (define right 0)
          (define ans 0)

          ;; expand right pointer until condition satisfied or end reached
          (define (expand)
            (when (and (< right n) (> missing 0))
              (let* ((ch (string-ref word1 right))
                     (idx (- (char->integer ch) (char->integer #\a))))
                (when (< (vector-ref have idx) (vector-ref need idx))
                  (set! missing (- missing 1)))
                (vector-set! have idx (+ 1 (vector-ref have idx))))
              (set! right (+ right 1))
              (expand)))

          ;; main loop over left index
          (let loop ((left 0))
            (when (< left n)
              (expand)
              (if (= missing 0)
                  (set! ans (+ ans (+ (- n right) 1))) ; add n - right + 1
                  (begin
                    ;; cannot satisfy any further substrings
                    (set! left n)))
              ;; remove character at left before moving to next position
              (when (< left (- n 1))
                (let* ((ch (string-ref word1 left))
                       (idx (- (char->integer ch) (char->integer #\a))))
                  (when (<= (vector-ref have idx) (vector-ref need idx))
                    (set! missing (+ missing 1)))
                  (vector-set! have idx (- (vector-ref have idx) 1))))
              (loop (+ left 1)))))
          ans))))
```

## Erlang

```erlang
-export([valid_substring_count/2]).

-spec valid_substring_count(Word1 :: unicode:unicode_binary(),
                            Word2 :: unicode:unicode_binary()) -> integer().
valid_substring_count(Word1, Word2) ->
    Len1 = byte_size(Word1),
    Len2 = byte_size(Word2),
    if
        Len2 > Len1 -> 0;
        true ->
            Need = build_need(Word2),
            Counts0 = erlang:make_tuple(27, 0),
            loop(0, 0, Word1, Len1, Need, Counts0, 0)
    end.

%% Build frequency tuple for Word2
build_need(Bin) ->
    lists:foldl(fun(Char, Acc) -> inc(Acc, Char) end,
                erlang:make_tuple(27, 0),
                binary_to_list(Bin)).

%% Increment count of a character in the tuple (1‑based index)
inc(Tuple, Char) ->
    Idx = Char - $a + 1,
    Old = element(Idx, Tuple),
    setelement(Idx, Tuple, Old + 1).

%% Decrement count of a character in the tuple
dec(Tuple, Char) ->
    Idx = Char - $a + 1,
    Old = element(Idx, Tuple),
    setelement(Idx, Tuple, Old - 1).

%% Check if Counts dominates Need for all letters
meets(Counts, Need) -> meets_loop(1, Counts, Need).

meets_loop(I, Counts, Need) when I =< 26 ->
    case element(I, Counts) >= element(I, Need) of
        true -> meets_loop(I + 1, Counts, Need);
        false -> false
    end;
meets_loop(_, _, _) -> true.

%% Main two‑pointer loop
loop(I, R, Bin, Len, Need, Counts, Ans) when I < Len ->
    {R2, Counts2} = expand_until(R, Bin, Len, Need, Counts),
    case meets(Counts2, Need) of
        true ->
            NewAns = Ans + (Len - R2 + 1),
            CharI = binary:at(Bin, I),
            UpdatedCounts = dec(Counts2, CharI),
            loop(I + 1, R2, Bin, Len, Need, UpdatedCounts, NewAns);
        false -> Ans
    end;
loop(_, _, _, _, _, _, Ans) -> Ans.

%% Expand right pointer until condition satisfied or end reached
expand_until(R, Bin, Len, Need, Counts) ->
    case meets(Counts, Need) of
        true -> {R, Counts};
        false when R < Len ->
            Char = binary:at(Bin, R),
            NewCounts = inc(Counts, Char),
            expand_until(R + 1, Bin, Len, Need, NewCounts);
        false -> {R, Counts}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_substring_count(word1 :: String.t(), word2 :: String.t()) :: integer()
  def valid_substring_count(word1, word2) do
    n = byte_size(word1)
    need = build_need(word2)
    cur = List.to_tuple(List.duplicate(0, 26))
    loop(0, 0, n, word1, cur, need, 0)
  end

  defp build_need(word) do
    Enum.reduce(0..byte_size(word) - 1, List.to_tuple(List.duplicate(0, 26)), fn i, acc ->
      c = :binary.at(word, i) - ?a
      put_elem(acc, c, elem(acc, c) + 1)
    end)
  end

  defp satisfied?(cur, need) do
    Enum.reduce_while(0..25, true, fn idx, _acc ->
      if elem(cur, idx) >= elem(need, idx), do: {:cont, true}, else: {:halt, false}
    end)
  end

  defp expand(right, n, bin, cur, need) do
    if right < n and not satisfied?(cur, need) do
      c = :binary.at(bin, right) - ?a
      cur2 = put_elem(cur, c, elem(cur, c) + 1)
      expand(right + 1, n, bin, cur2, need)
    else
      {cur, right}
    end
  end

  defp loop(left, right, n, bin, cur, need, ans) do
    if left >= n do
      ans
    else
      {cur2, right2} = expand(right, n, bin, cur, need)

      if satisfied?(cur2, need) do
        ans2 = ans + (n - right2 + 1)
        c_left = :binary.at(bin, left) - ?a
        cur3 = put_elem(cur2, c_left, elem(cur2, c_left) - 1)
        loop(left + 1, right2, n, bin, cur3, need, ans2)
      else
        ans
      end
    end
  end
end
```
