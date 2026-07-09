# 3298. Count Substrings That Can Be Rearranged to Contain a String II

## Cpp

```cpp
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        const int ALPH = 26;
        vector<int> need(ALPH, 0);
        for (char ch : word2) need[ch - 'a']++;
        int deficit = 0;
        for (int v : need) deficit += v; // total needed characters
        
        vector<int> cnt(ALPH, 0);
        long long ans = 0;
        int n = word1.size();
        int right = 0;
        
        for (int left = 0; left < n; ++left) {
            while (right < n && deficit > 0) {
                int idx = word1[right] - 'a';
                if (cnt[idx] < need[idx]) --deficit;
                ++cnt[idx];
                ++right;
            }
            if (deficit == 0) {
                ans += (long long)(n - right + 1);
            } else {
                break; // cannot satisfy for this and further left positions
            }
            int idxL = word1[left] - 'a';
            if (cnt[idxL] <= need[idxL]) ++deficit;
            --cnt[idxL];
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
        int[] need = new int[26];
        for (int i = 0; i < word2.length(); i++) {
            need[word2.charAt(i) - 'a']++;
        }
        int totalNeeded = 0;
        for (int v : need) totalNeeded += v;

        int[] cnt = new int[26];
        int missing = totalNeeded;
        long ans = 0L;
        int left = 0, right = 0; // right is exclusive

        while (left < n) {
            while (right < n && missing > 0) {
                int idx = word1.charAt(right) - 'a';
                if (cnt[idx] < need[idx]) {
                    missing--;
                }
                cnt[idx]++;
                right++;
            }

            if (missing == 0) {
                // minimal valid window ends at right-1
                ans += (long) (n - right + 1);
            } else {
                break; // cannot satisfy for this and further left positions
            }

            int idxL = word1.charAt(left) - 'a';
            cnt[idxL]--;
            if (cnt[idxL] < need[idxL]) {
                missing++;
            }
            left++;
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
        n = len(word1)
        need = [0] * 26
        for ch in word2:
            need[ord(ch) - 97] += 1

        reqKinds = sum(1 for v in need if v > 0)   # number of distinct chars needed
        cnt = [0] * 26
        met = 0                                   # how many of those chars are satisfied
        ans = 0
        r = 0

        for l in range(n):
            while r < n and met < reqKinds:
                idx = ord(word1[r]) - 97
                cnt[idx] += 1
                if need[idx] > 0 and cnt[idx] == need[idx]:
                    met += 1
                r += 1

            if met == reqKinds:
                ans += n - r + 1   # all extensions to the right are valid
            else:
                break               # cannot satisfy any further left positions

            idxl = ord(word1[l]) - 97
            if need[idxl] > 0 and cnt[idxl] == need[idxl]:
                met -= 1
            cnt[idxl] -= 1

        return ans
```

## Python3

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n = len(word1)
        req = [0] * 26
        for ch in word2:
            req[ord(ch) - 97] += 1

        cur = [0] * 26
        deficit = len(word2)          # total needed characters not yet satisfied
        r = 0
        ans = 0

        for l in range(n):
            while r < n and deficit > 0:
                idx = ord(word1[r]) - 97
                cur[idx] += 1
                if cur[idx] <= req[idx]:
                    deficit -= 1
                r += 1

            if deficit == 0:
                ans += n - r + 1      # all extensions of the minimal window are valid
            else:
                break                 # cannot satisfy for this and further left positions

            idxl = ord(word1[l]) - 97
            if cur[idxl] <= req[idxl]:
                deficit += 1
            cur[idxl] -= 1

        return ans
```

## C

```c
long long validSubstringCount(char* word1, char* word2) {
    int need[26] = {0};
    for (int i = 0; word2[i]; ++i) {
        need[word2[i] - 'a']++;
    }
    int totalNeededTypes = 0;
    for (int c = 0; c < 26; ++c) if (need[c] > 0) ++totalNeededTypes;

    // length of word1
    int n = 0;
    while (word1[n]) ++n;

    long long ans = 0;
    int have[26] = {0};
    int satisfied = 0;          // number of needed chars whose count meets requirement
    int left = 0;

    for (int right = 0; right < n; ++right) {
        int cr = word1[right] - 'a';
        have[cr]++;
        if (need[cr] > 0 && have[cr] == need[cr]) {
            ++satisfied;
        }

        // shrink left as much as possible while keeping all needed counts satisfied
        while (left <= right) {
            int cl = word1[left] - 'a';
            if (need[cl] == 0) {
                have[cl]--;
                ++left;
                continue;
            }
            if (have[cl] > need[cl]) {
                have[cl]--;
                // still satisfies requirement, satisfied unchanged
                ++left;
                continue;
            }
            break; // cannot remove further without breaking a needed count
        }

        if (satisfied == totalNeededTypes) {
            ans += (long long)(left + 1);
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long ValidSubstringCount(string word1, string word2) {
        int[] need = new int[26];
        foreach (char c in word2) need[c - 'a']++;

        int totalNeeded = 0;
        for (int i = 0; i < 26; i++) totalNeeded += need[i];

        int[] have = new int[26];
        int deficit = totalNeeded;
        long ans = 0;
        int left = 0;
        char[] arr = word1.ToCharArray();

        for (int right = 0; right < arr.Length; right++) {
            int idx = arr[right] - 'a';
            if (have[idx] < need[idx]) deficit--;
            have[idx]++;

            while (deficit == 0) {
                int lidx = arr[left] - 'a';
                if (have[lidx] - 1 >= need[lidx]) {
                    have[lidx]--;
                    left++;
                } else {
                    break;
                }
            }

            if (deficit == 0) {
                ans += (long)(left + 1);
            }
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
    let missing = 0;
    for (let v of need) missing += v;

    const cnt = new Array(26).fill(0);
    let left = 0, right = 0;
    let ans = 0;

    while (left < n) {
        // expand right until all requirements met or end reached
        while (right < n && missing > 0) {
            const idx = word1.charCodeAt(right) - 97;
            if (cnt[idx] < need[idx]) missing--;
            cnt[idx]++;
            right++;
        }
        if (missing === 0) {
            // window [left, right-1] satisfies; any longer end also works
            ans += n - right + 1;
        } else {
            break; // cannot satisfy for this left nor any later left
        }

        // move left pointer forward
        const lIdx = word1.charCodeAt(left) - 97;
        if (cnt[lIdx] <= need[lIdx]) missing++;
        cnt[lIdx]--;
        left++;
    }
    return ans;
};
```

## Typescript

```typescript
function validSubstringCount(word1: string, word2: string): number {
    const req = new Int32Array(26);
    for (let i = 0; i < word2.length; ++i) {
        req[word2.charCodeAt(i) - 97]++;
    }
    let missing = 0;
    for (let i = 0; i < 26; ++i) missing += req[i];

    const have = new Int32Array(26);
    const n = word1.length;
    let r = 0;
    let ans = 0;

    for (let l = 0; l < n; ++l) {
        while (r < n && missing > 0) {
            const idx = word1.charCodeAt(r) - 97;
            if (have[idx] < req[idx]) missing--;
            have[idx]++;
            r++;
        }
        if (missing === 0) {
            ans += n - r + 1;
        } else {
            break; // cannot satisfy any further windows
        }

        const idxL = word1.charCodeAt(l) - 97;
        if (have[idxL] <= req[idxL]) missing++;
        have[idxL]--;
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

        // frequency of characters required by word2
        $required = array_fill(0, 26, 0);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($word2[$i]) - 97;
            $required[$idx]++;
        }

        // number of distinct characters that have a positive requirement
        $needTypes = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($required[$i] > 0) $needTypes++;
        }

        $window = array_fill(0, 26, 0);
        $satisfied = 0;   // how many character types meet the required count
        $r = -1;
        $ans = 0;

        for ($l = 0; $l < $n; $l++) {
            // expand right pointer until all requirements are satisfied or end reached
            while ($r + 1 < $n && $satisfied < $needTypes) {
                $r++;
                $cIdx = ord($word1[$r]) - 97;
                $window[$cIdx]++;
                if ($required[$cIdx] > 0 && $window[$cIdx] == $required[$cIdx]) {
                    $satisfied++;
                }
            }

            // if current window satisfies, all extensions are also valid
            if ($satisfied == $needTypes) {
                $ans += $n - $r;
            } else {
                break; // cannot satisfy for this and any further left positions
            }

            // move left pointer forward, updating counts
            $cIdx = ord($word1[$l]) - 97;
            if ($required[$cIdx] > 0 && $window[$cIdx] == $required[$cIdx]) {
                $satisfied--;
            }
            $window[$cIdx]--;
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
        var need = [Int](repeating: 0, count: 26)
        for ch in w2 {
            need[Int(ch - 97)] += 1
        }
        var missing = 0
        for cnt in need where cnt > 0 {
            missing += 1
        }
        var cntArr = [Int](repeating: 0, count: 26)
        var right = 0
        var ans = 0
        for left in 0..<n {
            while right < n && missing > 0 {
                let idx = Int(w1[right] - 97)
                cntArr[idx] += 1
                if need[idx] > 0 && cntArr[idx] == need[idx] {
                    missing -= 1
                }
                right += 1
            }
            if missing == 0 {
                ans += n - (right - 1)
            } else {
                break
            }
            let idxL = Int(w1[left] - 97)
            if need[idxL] > 0 && cntArr[idxL] == need[idxL] {
                missing += 1
            }
            cntArr[idxL] -= 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validSubstringCount(word1: String, word2: String): Long {
        val need = IntArray(26)
        var typesNeeded = 0
        for (ch in word2) {
            val idx = ch - 'a'
            if (need[idx] == 0) typesNeeded++
            need[idx]++
        }
        val cur = IntArray(26)
        var satisfied = 0
        var left = 0
        var result = 0L
        val n = word1.length
        for (right in 0 until n) {
            val idxR = word1[right] - 'a'
            cur[idxR]++
            if (need[idxR] > 0 && cur[idxR] == need[idxR]) satisfied++

            while (satisfied == typesNeeded && left <= right) {
                val idxL = word1[left] - 'a'
                if (need[idxL] == 0) {
                    cur[idxL]--
                    left++
                    continue
                }
                if (cur[idxL] > need[idxL]) {
                    cur[idxL]--
                    left++
                    continue
                }
                break
            }

            if (satisfied == typesNeeded) {
                result += (left + 1).toLong()
            }
        }
        return result
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

    List<int> have = List.filled(26, 0);
    int totalMissing = word2.length;
    int r = 0;
    int ans = 0;

    for (int l = 0; l < n; l++) {
      while (r < n && totalMissing > 0) {
        int idx = word1.codeUnitAt(r) - 97;
        if (have[idx] < need[idx]) totalMissing--;
        have[idx]++;
        r++;
      }
      if (totalMissing == 0) {
        ans += (n - r + 1);
      } else {
        break;
      }

      int idxL = word1.codeUnitAt(l) - 97;
      if (have[idxL] <= need[idxL]) totalMissing++;
      have[idxL]--;
    }

    return ans;
  }
}
```

## Golang

```go
func validSubstringCount(word1 string, word2 string) int64 {
    n := len(word1)
    m := len(word2)
    if m > n {
        return 0
    }

    var req [26]int
    for i := 0; i < m; i++ {
        req[word2[i]-'a']++
    }

    var freq [26]int
    r := 0
    var ans int64

    satisfies := func() bool {
        for i := 0; i < 26; i++ {
            if freq[i] < req[i] {
                return false
            }
        }
        return true
    }

    for l := 0; l < n; l++ {
        for r < n && !satisfies() {
            idx := word1[r] - 'a'
            freq[idx]++
            r++
        }
        if satisfies() {
            ans += int64(n - r + 1)
        } else {
            break
        }
        // move left pointer forward
        idxL := word1[l] - 'a'
        freq[idxL]--
    }

    return ans
}
```

## Ruby

```ruby
def valid_substring_count(word1, word2)
  n = word1.length
  need = Array.new(26, 0)
  word2.each_byte { |b| need[b - 97] += 1 }

  have = Array.new(26, 0)
  deficit = need.sum
  ans = 0
  right = 0
  left = 0

  while left < n
    while right < n && deficit > 0
      idx = word1.getbyte(right) - 97
      have[idx] += 1
      deficit -= 1 if have[idx] <= need[idx]
      right += 1
    end

    break if deficit > 0

    ans += n - right + 1

    idx_left = word1.getbyte(left) - 97
    deficit += 1 if have[idx_left] <= need[idx_left]
    have[idx_left] -= 1

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
        val need = new Array[Int](26)
        for (ch <- word2) need(ch - 'a') += 1

        // quick impossibility check
        val total = new Array[Int](26)
        for (ch <- word1) total(ch - 'a') += 1
        var i = 0
        while (i < 26) {
            if (need(i) > total(i)) return 0L
            i += 1
        }

        def satisfied(cnt: Array[Int]): Boolean = {
            var j = 0
            while (j < 26) {
                if (cnt(j) < need(j)) return false
                j += 1
            }
            true
        }

        val cnt = new Array[Int](26)
        var left = 0
        var ans = 0L

        var right = 0
        while (right < n) {
            val idxR = word1.charAt(right) - 'a'
            cnt(idxR) += 1

            // shrink from the left as long as condition holds
            while (left <= right && satisfied(cnt)) {
                val idxL = word1.charAt(left) - 'a'
                cnt(idxL) -= 1
                left += 1
            }
            // after shrinking, all starts [0 .. left-1] are valid for this right
            ans += left
            right += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_substring_count(word1: String, word2: String) -> i64 {
        let w1 = word1.as_bytes();
        let n = w1.len();
        let mut need = [0usize; 26];
        for &b in word2.as_bytes() {
            need[(b - b'a') as usize] += 1;
        }
        let total_needed: usize = need.iter().sum();

        let mut cur = [0usize; 26];
        let mut missing = total_needed;
        let mut r = 0usize;
        let mut ans: i64 = 0;

        for l in 0..n {
            while r < n && missing > 0 {
                let idx = (w1[r] - b'a') as usize;
                cur[idx] += 1;
                if cur[idx] <= need[idx] {
                    missing -= 1;
                }
                r += 1;
            }

            if missing == 0 {
                ans += (n - r + 1) as i64; // r is exclusive, minimal satisfying ends at r-1
            } else {
                break; // cannot satisfy for this and further l
            }

            // remove left character before moving l forward
            let idx = (w1[l] - b'a') as usize;
            if cur[idx] <= need[idx] {
                missing += 1;
            }
            cur[idx] -= 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (valid-substring-count word1 word2)
  (-> string? string? exact-integer?)
  (let* ([n (string-length word1)]
         [need (make-vector 26 0)]
         [freq (make-vector 26 0)])
    ;; build need frequencies
    (for ([i (in-range (string-length word2))])
      (let* ([ch (string-ref word2 i)]
             [idx (- (char->integer ch) (char->integer #\a))])
        (vector-set! need idx (+ 1 (vector-ref need idx)))))
    ;; total missing characters initially
    (define missing
      (let loop ((i 0) (sum 0))
        (if (= i 26)
            sum
            (loop (+ i 1) (+ sum (vector-ref need i))))))
    (define left 0)
    (define right 0)
    (define ans 0)
    (define missing-var missing)

    ;; expand right pointer while we still miss needed chars
    (define (expand)
      (when (and (< right n) (> missing-var 0))
        (let* ([ch (string-ref word1 right)]
               [idx (- (char->integer ch) (char->integer #\a))])
          (define cur (vector-ref freq idx))
          (when (< cur (vector-ref need idx))
            (set! missing-var (- missing-var 1)))
          (vector-set! freq idx (+ cur 1))
          (set! right (+ right 1))
          (expand))))

    ;; main loop over left pointer
    (let loop-left ()
      (when (< left n)
        (expand)
        (if (= missing-var 0)
            (begin
              ;; all substrings starting at left with end >= right-1 are valid
              (set! ans (+ ans (- n right -1))) ; n - right + 1
              ;; remove character at left before moving left forward
              (let* ([ch (string-ref word1 left)]
                     [idx (- (char->integer ch) (char->integer #\a))])
                (define cur (vector-ref freq idx))
                (vector-set! freq idx (- cur 1))
                (when (< (vector-ref freq idx) (vector-ref need idx))
                  (set! missing-var (+ missing-var 1))))
              (set! left (+ left 1))
              (loop-left))
            ;; cannot satisfy any further substrings
            (void)))))
    ans)))
```

## Erlang

```erlang
-spec valid_substring_count(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
valid_substring_count(Word1, Word2) ->
    Req = init_counts_tuple(Word2),
    N = byte_size(Word1),
    EmptyCounts = list_to_tuple(lists:duplicate(26, 0)),
    loop(0, 0, N, Word1, Req, EmptyCounts, 0).

%% initialize required character counts from Word2
init_counts_tuple(Bin) ->
    Empty = list_to_tuple(lists:duplicate(26, 0)),
    init_counts_loop(0, byte_size(Bin), Bin, Empty).

init_counts_loop(I, Len, Bin, Tuple) when I < Len ->
    Char = binary:at(Bin, I),
    NewTuple = inc_char(Char, Tuple),
    init_counts_loop(I + 1, Len, Bin, NewTuple);
init_counts_loop(_, _, _, Tuple) -> Tuple.

%% main sliding window loop
loop(L, R, N, Word1, Req, Counts, Ans) when L < N ->
    {R2, Counts2} = expand_until_satisfied(R, N, Word1, Req, Counts),
    case satisfied(Counts2, Req) of
        true ->
            NewAns = Ans + (N - R2 + 1),
            CharL = binary:at(Word1, L),
            UpdatedCounts = dec_char(CharL, Counts2),
            loop(L + 1, R2, N, Word1, Req, UpdatedCounts, NewAns);
        false ->
            Ans
    end;
loop(_, _, _, _, _, _, Ans) -> Ans.

%% expand right pointer until window satisfies requirement or reaches end
expand_until_satisfied(R, N, _Word1, _Req, Counts) when R >= N ->
    {R, Counts};
expand_until_satisfied(R, N, Word1, Req, Counts) ->
    case satisfied(Counts, Req) of
        true -> {R, Counts};
        false ->
            Char = binary:at(Word1, R),
            NewCounts = inc_char(Char, Counts),
            expand_until_satisfied(R + 1, N, Word1, Req, NewCounts)
    end.

%% check if current counts dominate required counts
satisfied(Counts, Req) -> satisfied(0, Counts, Req).

satisfied(26, _Counts, _Req) -> true;
satisfied(I, Counts, Req) ->
    case element(I + 1, Counts) < element(I + 1, Req) of
        true -> false;
        false -> satisfied(I + 1, Counts, Req)
    end.

%% increment character count in tuple
inc_char(Char, Tuple) ->
    Idx = Char - $a,
    Val = element(Idx + 1, Tuple) + 1,
    setelement(Idx + 1, Tuple, Val).

%% decrement character count in tuple
dec_char(Char, Tuple) ->
    Idx = Char - $a,
    Val = element(Idx + 1, Tuple) - 1,
    setelement(Idx + 1, Tuple, Val).
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_substring_count(word1 :: String.t(), word2 :: String.t()) :: integer()
  def valid_substring_count(word1, word2) do
    {need_arr, total_needed} = build_need(word2)
    cur_arr = :array.new(26, default: 0)
    n = byte_size(word1)

    loop(
      0,
      0,
      cur_arr,
      total_needed,
      0,
      word1,
      n,
      need_arr
    )
  end

  defp build_need(word2) do
    Enum.reduce(:binary.bin_to_list(word2), { :array.new(26, default: 0), 0 }, fn c, {arr, total} ->
      idx = c - ?a
      cnt = :array.get(idx, arr)
      { :array.set(idx, cnt + 1, arr), total + 1 }
    end)
  end

  defp loop(l, r, cur, deficit, ans, word_bin, n, need) do
    if l >= n do
      ans
    else
      {cur2, r2, deficit2} = expand(r, cur, deficit, word_bin, n, need)

      if deficit2 > 0 do
        ans
      else
        ans2 = ans + (n - r2 + 1)
        idx_left = :binary.at(word_bin, l) - ?a
        {cur3, deficit3} = remove_char(cur2, idx_left, need, deficit2)
        loop(l + 1, r2, cur3, deficit3, ans2, word_bin, n, need)
      end
    end
  end

  defp expand(r, cur, deficit, word_bin, n, need) do
    if r < n and deficit > 0 do
      idx = :binary.at(word_bin, r) - ?a
      {cur1, deficit1} = add_char(cur, idx, need, deficit)
      expand(r + 1, cur1, deficit1, word_bin, n, need)
    else
      {cur, r, deficit}
    end
  end

  defp add_char(arr, idx, need_arr, deficit) do
    cnt = :array.get(idx, arr)
    need_cnt = :array.get(idx, need_arr)

    new_deficit =
      if cnt < need_cnt do
        deficit - 1
      else
        deficit
      end

    { :array.set(idx, cnt + 1, arr), new_deficit }
  end

  defp remove_char(arr, idx, need_arr, deficit) do
    cnt = :array.get(idx, arr)
    need_cnt = :array.get(idx, need_arr)

    new_deficit =
      if cnt <= need_cnt do
        deficit + 1
      else
        deficit
      end

    { :array.set(idx, cnt - 1, arr), new_deficit }
  end
end
```
