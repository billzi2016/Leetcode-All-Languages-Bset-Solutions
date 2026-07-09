# 0567. Permutation in String

## Cpp

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size(), m = s2.size();
        if (n > m) return false;
        vector<int> cnt1(26, 0), cnt2(26, 0);
        for (char c : s1) cnt1[c - 'a']++;
        for (int i = 0; i < n; ++i) cnt2[s2[i] - 'a']++;
        if (cnt1 == cnt2) return true;
        for (int i = n; i < m; ++i) {
            cnt2[s2[i] - 'a']++;
            cnt2[s2[i - n] - 'a']--;
            if (cnt1 == cnt2) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        if (n > m) return false;
        int[] diffArr = new int[26];
        for (int i = 0; i < n; i++) {
            diffArr[s1.charAt(i) - 'a']++;
            diffArr[s2.charAt(i) - 'a']--;
        }
        int nonZero = 0;
        for (int v : diffArr) if (v != 0) nonZero++;
        if (nonZero == 0) return true;
        for (int i = n; i < m; i++) {
            int inIdx = s2.charAt(i) - 'a';
            int outIdx = s2.charAt(i - n) - 'a';
            // add incoming character
            if (diffArr[inIdx] == 0) nonZero++;
            diffArr[inIdx]--;
            if (diffArr[inIdx] == 0) nonZero--;
            // remove outgoing character
            if (diffArr[outIdx] == 0) nonZero++;
            diffArr[outIdx]++;
            if (diffArr[outIdx] == 0) nonZero--;
            if (nonZero == 0) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n > m:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26
        a_ord = ord('a')

        for i in range(n):
            freq1[ord(s1[i]) - a_ord] += 1
            freq2[ord(s2[i]) - a_ord] += 1

        matches = sum(1 for i in range(26) if freq1[i] == freq2[i])
        if matches == 26:
            return True

        for i in range(n, m):
            idx_in = ord(s2[i]) - a_ord
            idx_out = ord(s2[i - n]) - a_ord

            # add new character
            if freq2[idx_in] == freq1[idx_in]:
                matches -= 1
            freq2[idx_in] += 1
            if freq2[idx_in] == freq1[idx_in]:
                matches += 1

            # remove old character
            if freq2[idx_out] == freq1[idx_out]:
                matches -= 1
            freq2[idx_out] -= 1
            if freq2[idx_out] == freq1[idx_out]:
                matches += 1

            if matches == 26:
                return True

        return False
```

## Python3

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - 97] += 1
            cnt2[ord(s2[i]) - 97] += 1
        matches = sum(1 for i in range(26) if cnt1[i] == cnt2[i])
        if matches == 26:
            return True
        for i in range(n, m):
            idx_in = ord(s2[i]) - 97
            idx_out = ord(s2[i - n]) - 97

            cnt2[idx_in] += 1
            if cnt2[idx_in] == cnt1[idx_in]:
                matches += 1
            elif cnt2[idx_in] - 1 == cnt1[idx_in]:
                matches -= 1

            cnt2[idx_out] -= 1
            if cnt2[idx_out] == cnt1[idx_out]:
                matches += 1
            elif cnt2[idx_out] + 1 == cnt1[idx_out]:
                matches -= 1

            if matches == 26:
                return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool checkInclusion(char* s1, char* s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);
    if (len1 > len2) return false;

    int diff[26] = {0};
    for (int i = 0; i < len1; ++i) {
        diff[s1[i] - 'a']++;
        diff[s2[i] - 'a']--;
    }

    int matches = 0;
    for (int i = 0; i < 26; ++i)
        if (diff[i] == 0) ++matches;

    if (matches == 26) return true;

    for (int i = len1; i < len2; ++i) {
        int addIdx = s2[i] - 'a';
        int remIdx = s2[i - len1] - 'a';

        if (diff[addIdx] == 0) --matches;
        diff[addIdx]++;
        if (diff[addIdx] == 0) ++matches;

        if (diff[remIdx] == 0) --matches;
        diff[remIdx]--;
        if (diff[remIdx] == 0) ++matches;

        if (matches == 26) return true;
    }

    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckInclusion(string s1, string s2)
    {
        int n = s1.Length;
        int m = s2.Length;
        if (n > m) return false;

        int[] need = new int[26];
        int[] window = new int[26];

        foreach (char c in s1)
            need[c - 'a']++;

        for (int i = 0; i < n; i++)
            window[s2[i] - 'a']++;

        int matches = 0;
        for (int i = 0; i < 26; i++)
            if (need[i] == window[i]) matches++;

        if (matches == 26) return true;

        for (int i = n; i < m; i++)
        {
            int addIdx = s2[i] - 'a';
            int removeIdx = s2[i - n] - 'a';

            // Add new character
            if (window[addIdx] == need[addIdx]) matches--;
            window[addIdx]++;
            if (window[addIdx] == need[addIdx]) matches++;

            // Remove old character
            if (window[removeIdx] == need[removeIdx]) matches--;
            window[removeIdx]--;
            if (window[removeIdx] == need[removeIdx]) matches++;

            if (matches == 26) return true;
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const n = s1.length, m = s2.length;
    if (n > m) return false;

    const need = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        need[s1.charCodeAt(i) - 97]++;
    }

    const win = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        win[s2.charCodeAt(i) - 97]++;
    }

    let matches = 0;
    for (let i = 0; i < 26; ++i) {
        if (need[i] === win[i]) matches++;
    }
    if (matches === 26) return true;

    for (let i = n; i < m; ++i) {
        const addIdx = s2.charCodeAt(i) - 97;
        const remIdx = s2.charCodeAt(i - n) - 97;

        // add new character
        win[addIdx]++;
        if (win[addIdx] === need[addIdx]) {
            matches++;
        } else if (win[addIdx] === need[addIdx] + 1) {
            matches--;
        }

        // remove old character
        win[remIdx]--;
        if (win[remIdx] === need[remIdx]) {
            matches++;
        } else if (win[remIdx] === need[remIdx] - 1) {
            matches--;
        }

        if (matches === 26) return true;
    }
    return false;
};
```

## Typescript

```typescript
function checkInclusion(s1: string, s2: string): boolean {
    const n = s1.length;
    const m = s2.length;
    if (n > m) return false;

    const cnt1 = new Array(26).fill(0);
    const cnt2 = new Array(26).fill(0);

    for (let i = 0; i < n; i++) {
        cnt1[s1.charCodeAt(i) - 97]++;
        cnt2[s2.charCodeAt(i) - 97]++;
    }

    let matches = 0;
    for (let i = 0; i < 26; i++) {
        if (cnt1[i] === cnt2[i]) matches++;
    }
    if (matches === 26) return true;

    const update = (idx: number, delta: number) => {
        const before = cnt2[idx];
        if (before === cnt1[idx]) matches--;
        const after = before + delta;
        cnt2[idx] = after;
        if (after === cnt1[idx]) matches++;
    };

    for (let i = n; i < m; i++) {
        const addIdx = s2.charCodeAt(i) - 97;
        const removeIdx = s2.charCodeAt(i - n) - 97;
        update(addIdx, 1);
        update(removeIdx, -1);
        if (matches === 26) return true;
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkInclusion($s1, $s2) {
        $len1 = strlen($s1);
        $len2 = strlen($s2);
        if ($len1 > $len2) {
            return false;
        }

        $cnt1 = array_fill(0, 26, 0);
        $cnt2 = array_fill(0, 26, 0);

        for ($i = 0; $i < $len1; $i++) {
            $cnt1[ord($s1[$i]) - ord('a')]++;
            $cnt2[ord($s2[$i]) - ord('a')]++;
        }

        if ($cnt1 === $cnt2) {
            return true;
        }

        for ($i = $len1; $i < $len2; $i++) {
            $addIdx = ord($s2[$i]) - ord('a');
            $removeIdx = ord($s2[$i - $len1]) - ord('a');

            $cnt2[$addIdx]++;
            $cnt2[$removeIdx]--;

            if ($cnt1 === $cnt2) {
                return true;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkInclusion(_ s1: String, _ s2: String) -> Bool {
        let n = s1.count
        let m = s2.count
        if n > m { return false }
        
        var need = [Int](repeating: 0, count: 26)
        var window = [Int](repeating: 0, count: 26)
        
        let arr1 = Array(s1.utf8)
        let arr2 = Array(s2.utf8)
        
        for ch in arr1 {
            need[Int(ch - 97)] += 1
        }
        for i in 0..<n {
            window[Int(arr2[i] - 97)] += 1
        }
        
        var matches = 0
        for i in 0..<26 {
            if need[i] == window[i] { matches += 1 }
        }
        if matches == 26 { return true }
        
        var left = 0
        for right in n..<m {
            let addIdx = Int(arr2[right] - 97)
            let removeIdx = Int(arr2[left] - 97)
            left += 1
            
            // add character at right
            window[addIdx] += 1
            if window[addIdx] == need[addIdx] {
                matches += 1
            } else if window[addIdx] == need[addIdx] + 1 {
                matches -= 1
            }
            
            // remove character at left-1
            window[removeIdx] -= 1
            if window[removeIdx] == need[removeIdx] {
                matches += 1
            } else if window[removeIdx] == need[removeIdx] - 1 {
                matches -= 1
            }
            
            if matches == 26 { return true }
        }
        
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {
        val n = s1.length
        val m = s2.length
        if (n > m) return false

        val freq = IntArray(26)
        for (c in s1) {
            freq[c - 'a']++
        }

        val window = IntArray(26)
        for (i in 0 until n) {
            val c = s2[i]
            window[c - 'a']++
        }

        var matches = 0
        for (i in 0..25) {
            if (freq[i] == window[i]) matches++
        }
        if (matches == 26) return true

        for (i in n until m) {
            val addIdx = s2[i] - 'a'
            val removeIdx = s2[i - n] - 'a'

            // Add new character
            if (freq[addIdx] == window[addIdx]) matches--
            window[addIdx]++
            if (freq[addIdx] == window[addIdx]) matches++

            // Remove old character
            if (freq[removeIdx] == window[removeIdx]) matches--
            window[removeIdx]--
            if (freq[removeIdx] == window[removeIdx]) matches++

            if (matches == 26) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool checkInclusion(String s1, String s2) {
    int n = s1.length;
    int m = s2.length;
    if (n > m) return false;

    List<int> cnt1 = List.filled(26, 0);
    List<int> cnt2 = List.filled(26, 0);

    for (int i = 0; i < n; i++) {
      cnt1[s1.codeUnitAt(i) - 97]++;
      cnt2[s2.codeUnitAt(i) - 97]++;
    }

    int matches = 0;
    for (int i = 0; i < 26; i++) {
      if (cnt1[i] == cnt2[i]) matches++;
    }
    if (matches == 26) return true;

    for (int i = n; i < m; i++) {
      int addIdx = s2.codeUnitAt(i) - 97;
      int removeIdx = s2.codeUnitAt(i - n) - 97;

      // add new character
      if (cnt1[addIdx] == cnt2[addIdx]) matches--;
      cnt2[addIdx]++;
      if (cnt1[addIdx] == cnt2[addIdx]) matches++;

      // remove old character
      if (cnt1[removeIdx] == cnt2[removeIdx]) matches--;
      cnt2[removeIdx]--;
      if (cnt1[removeIdx] == cnt2[removeIdx]) matches++;

      if (matches == 26) return true;
    }

    return false;
  }
}
```

## Golang

```go
func checkInclusion(s1 string, s2 string) bool {
    n, m := len(s1), len(s2)
    if n > m {
        return false
    }
    var need [26]int
    for i := 0; i < n; i++ {
        need[int(s1[i]-'a')]++
    }
    var window [26]int
    for i := 0; i < n; i++ {
        window[int(s2[i]-'a')]++
    }
    matches := 0
    for i := 0; i < 26; i++ {
        if need[i] == window[i] {
            matches++
        }
    }
    if matches == 26 {
        return true
    }
    for i := n; i < m; i++ {
        r := int(s2[i] - 'a')
        l := int(s2[i-n] - 'a')

        // add right character
        if window[r] == need[r] {
            matches--
        }
        window[r]++
        if window[r] == need[r] {
            matches++
        }

        // remove left character
        if window[l] == need[l] {
            matches--
        }
        window[l]--
        if window[l] == need[l] {
            matches++
        }

        if matches == 26 {
            return true
        }
    }
    return false
}
```

## Ruby

```ruby
def check_inclusion(s1, s2)
  n = s1.length
  m = s2.length
  return false if n > m

  cnt1 = Array.new(26, 0)
  cnt2 = Array.new(26, 0)

  s1.each_char { |c| cnt1[c.ord - 97] += 1 }
  s2[0...n].each_char { |c| cnt2[c.ord - 97] += 1 }

  matches = 0
  26.times { |i| matches += 1 if cnt1[i] == cnt2[i] }
  return true if matches == 26

  (n...m).each do |i|
    add_idx = s2[i].ord - 97
    rem_idx = s2[i - n].ord - 97

    # add new character
    matches -= 1 if cnt2[add_idx] == cnt1[add_idx]
    cnt2[add_idx] += 1
    matches += 1 if cnt2[add_idx] == cnt1[add_idx]

    # remove old character
    matches -= 1 if cnt2[rem_idx] == cnt1[rem_idx]
    cnt2[rem_idx] -= 1
    matches += 1 if cnt2[rem_idx] == cnt1[rem_idx]

    return true if matches == 26
  end

  false
end
```

## Scala

```scala
object Solution {
    def checkInclusion(s1: String, s2: String): Boolean = {
        val n = s1.length
        val m = s2.length
        if (n > m) return false

        val freq1 = new Array[Int](26)
        val window = new Array[Int](26)

        for (c <- s1) {
            freq1(c - 'a') += 1
        }
        for (i <- 0 until n) {
            val c = s2(i)
            window(c - 'a') += 1
        }

        var matches = 0
        for (i <- 0 until 26) {
            if (freq1(i) == window(i)) matches += 1
        }
        if (matches == 26) return true

        for (i <- n until m) {
            val inIdx = s2(i) - 'a'
            val outIdx = s2(i - n) - 'a'

            // add incoming character
            if (freq1(inIdx) == window(inIdx)) matches -= 1
            window(inIdx) += 1
            if (freq1(inIdx) == window(inIdx)) matches += 1

            // remove outgoing character
            if (freq1(outIdx) == window(outIdx)) matches -= 1
            window(outIdx) -= 1
            if (freq1(outIdx) == window(outIdx)) matches += 1

            if (matches == 26) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let n1 = s1.len();
        let n2 = s2.len();
        if n1 > n2 {
            return false;
        }
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();

        let mut need = [0i32; 26];
        for &c in b1 {
            need[(c - b'a') as usize] += 1;
        }

        let mut have = [0i32; 26];
        for i in 0..n1 {
            have[(b2[i] - b'a') as usize] += 1;
        }

        let mut matches = 0usize;
        for i in 0..26 {
            if need[i] == have[i] {
                matches += 1;
            }
        }
        if matches == 26 {
            return true;
        }

        for i in n1..n2 {
            let idx_new = (b2[i] - b'a') as usize;
            let idx_old = (b2[i - n1] - b'a') as usize;

            // add new character
            if have[idx_new] == need[idx_new] {
                matches -= 1;
            }
            have[idx_new] += 1;
            if have[idx_new] == need[idx_new] {
                matches += 1;
            }

            // remove old character
            if have[idx_old] == need[idx_old] {
                matches -= 1;
            }
            have[idx_old] -= 1;
            if have[idx_old] == need[idx_old] {
                matches += 1;
            }

            if matches == 26 {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (check-inclusion s1 s2)
  (-> string? string? boolean?)
  (let* ((len1 (string-length s1))
         (len2 (string-length s2)))
    (if (> len1 len2)
        #false
        (let ((cnt1 (make-vector 26 0))
              (cnt2 (make-vector 26 0)))
          ;; count characters in s1
          (for ([i (in-range len1)])
            (let* ((c (string-ref s1 i))
                   (idx (- (char->integer c) (char->integer #\a))))
              (vector-set! cnt1 idx (+ 1 (vector-ref cnt1 idx)))))
          ;; count characters in the first window of s2
          (for ([i (in-range len1)])
            (let* ((c (string-ref s2 i))
                   (idx (- (char->integer c) (char->integer #\a))))
              (vector-set! cnt2 idx (+ 1 (vector-ref cnt2 idx)))))
          ;; helper to compare the two count vectors
          (define (matches?)
            (let loop ((i 0))
              (if (= i 26)
                  #true
                  (if (= (vector-ref cnt1 i) (vector-ref cnt2 i))
                      (loop (+ i 1))
                      #false))))
          (if (matches?) 
              #true
              (let loop ((start 0))
                (if (>= start (- len2 len1))
                    #false
                    (begin
                      (let* ((out-char (string-ref s2 start))
                             (in-char (string-ref s2 (+ start len1)))
                             (out-idx (- (char->integer out-char) (char->integer #\a)))
                             (in-idx  (- (char->integer in-char)  (char->integer #\a))))
                        (vector-set! cnt2 out-idx (- (vector-ref cnt2 out-idx) 1))
                        (vector-set! cnt2 in-idx (+ (vector-ref cnt2 in-idx) 1)))
                      (if (matches?) 
                          #true
                          (loop (+ start 1)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([check_inclusion/2]).

-spec check_inclusion(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_inclusion(S1, S2) ->
    Len1 = byte_size(S1),
    Len2 = byte_size(S2),
    if
        Len1 > Len2 ->
            false;
        true ->
            Diff0 = erlang:make_tuple(26, 0),
            Diff1 = fold_inc(S1, Len1, Diff0),
            Diff2 = fold_dec(S2, Len1, Diff1),
            Matches = zero_count(Diff2, 26),
            if
                Matches == 26 ->
                    true;
                true ->
                    slide(Len1, Len1, Len2, S2, Diff2, Matches)
            end
    end.

fold_inc(_S, 0, Diff) -> Diff;
fold_inc(S, L, Diff) ->
    lists:foldl(
        fun(I, D) ->
            Char = binary:at(S, I),
            Idx = Char - $a + 1,
            setelement(Idx, D, element(Idx, D) + 1)
        end,
        Diff,
        lists:seq(0, L - 1)
    ).

fold_dec(_S, 0, Diff) -> Diff;
fold_dec(S, L, Diff) ->
    lists:foldl(
        fun(I, D) ->
            Char = binary:at(S, I),
            Idx = Char - $a + 1,
            setelement(Idx, D, element(Idx, D) - 1)
        end,
        Diff,
        lists:seq(0, L - 1)
    ).

zero_count(Tuple, N) -> zero_count(Tuple, N, 0).
zero_count(_Tuple, 0, Acc) -> Acc;
zero_count(Tuple, I, Acc) ->
    Val = element(I, Tuple),
    NewAcc = if Val == 0 -> Acc + 1; true -> Acc end,
    zero_count(Tuple, I - 1, NewAcc).

slide(_Len1, Pos, Len2, _S2, _Diff, _Matches) when Pos >= Len2 ->
    false;
slide(Len1, Pos, Len2, S2, Diff, Matches) ->
    OutIdx = Pos - Len1,
    OutChar = binary:at(S2, OutIdx),
    InChar = binary:at(S2, Pos),

    IdxOut = OutChar - $a + 1,
    OldValOut = element(IdxOut, Diff),
    NewValOut = OldValOut + 1,
    Matches1 = case OldValOut of
        0 -> Matches - 1;
        _ -> Matches
    end,
    Matches2 = case NewValOut of
        0 -> Matches1 + 1;
        _ -> Matches1
    end,
    Diff1 = setelement(IdxOut, Diff, NewValOut),

    IdxIn = InChar - $a + 1,
    OldValIn = element(IdxIn, Diff1),
    NewValIn = OldValIn - 1,
    Matches3 = case OldValIn of
        0 -> Matches2 - 1;
        _ -> Matches2
    end,
    Matches4 = case NewValIn of
        0 -> Matches3 + 1;
        _ -> Matches3
    end,
    Diff2 = setelement(IdxIn, Diff1, NewValIn),

    if
        Matches4 == 26 ->
            true;
        true ->
            slide(Len1, Pos + 1, Len2, S2, Diff2, Matches4)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_inclusion(s1 :: String.t, s2 :: String.t) :: boolean
  def check_inclusion(s1, s2) do
    len1 = String.length(s1)
    len2 = String.length(s2)

    if len1 > len2 do
      false
    else
      s1_chars = String.to_charlist(s1)
      s2_chars = String.to_charlist(s2)

      freq0 = List.duplicate(0, 26)

      freq =
        Enum.reduce(0..(len1 - 1), freq0, fn i, f ->
          idx1 = Enum.at(s1_chars, i) - ?a
          f = List.update_at(f, idx1, &(&1 + 1))
          idx2 = Enum.at(s2_chars, i) - ?a
          List.update_at(f, idx2, &(&1 - 1))
        end)

      if Enum.all?(freq, fn x -> x == 0 end) do
        true
      else
        if len1 == len2 do
          false
        else
          result =
            Enum.reduce_while(len1..(len2 - 1), freq, fn i, f ->
              out_idx = Enum.at(s2_chars, i - len1) - ?a
              f = List.update_at(f, out_idx, &(&1 + 1))
              in_idx = Enum.at(s2_chars, i) - ?a
              f = List.update_at(f, in_idx, &(&1 - 1))

              if Enum.all?(f, fn x -> x == 0 end) do
                {:halt, true}
              else
                {:cont, f}
              end
            end)

          result === true
        end
      end
    end
  end
end
```
