# 1930. Unique Length-3 Palindromic Subsequences

## Cpp

```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        const int ALPH = 26;
        vector<int> first(ALPH, -1), last(ALPH, -1);
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            if (first[idx] == -1) first[idx] = i;
            last[idx] = i;
        }
        int ans = 0;
        for (int c = 0; c < ALPH; ++c) {
            if (first[c] == -1 || last[c] <= first[c] + 1) continue;
            bool seen[ALPH] = {false};
            for (int i = first[c] + 1; i < last[c]; ++i) {
                seen[s[i] - 'a'] = true;
            }
            for (int k = 0; k < ALPH; ++k) if (seen[k]) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        java.util.Arrays.fill(first, -1);
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] == -1) first[idx] = i;
            last[idx] = i;
        }
        int ans = 0;
        for (int c = 0; c < 26; c++) {
            int l = first[c];
            int r = last[c];
            if (l == -1 || l >= r) continue;
            int mask = 0;
            for (int i = l + 1; i < r; i++) {
                mask |= 1 << (s.charAt(i) - 'a');
            }
            ans += Integer.bitCount(mask);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = [-1] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for c in range(26):
            if first[c] != -1 and first[c] < last[c]:
                middle_chars = set()
                for k in range(first[c] + 1, last[c]):
                    middle_chars.add(s[k])
                ans += len(middle_chars)
        return ans
```

## Python3

```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for c in range(26):
            l = first[c]
            r = last[c]
            if l == -1 or l >= r:
                continue
            middle_chars = set()
            for k in range(l + 1, r):
                middle_chars.add(s[k])
            ans += len(middle_chars)

        return ans
```

## C

```c
int countPalindromicSubsequence(char* s) {
    if (!s) return 0;
    int n = 0;
    while (s[n] != '\0') ++n;

    int first[26];
    int last[26];
    for (int i = 0; i < 26; ++i) {
        first[i] = -1;
        last[i] = -1;
    }

    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        if (first[idx] == -1) first[idx] = i;
        last[idx] = i;
    }

    int ans = 0;
    for (int c = 0; c < 26; ++c) {
        if (first[c] == -1 || first[c] >= last[c]) continue; // need at least two occurrences with a gap
        bool seen[26] = {false};
        for (int k = first[c] + 1; k < last[c]; ++k) {
            int mid = s[k] - 'a';
            seen[mid] = true;
        }
        for (int d = 0; d < 26; ++d) {
            if (seen[d]) ++ans;
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountPalindromicSubsequence(string s)
    {
        int n = s.Length;
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) first[i] = -1;

        for (int i = 0; i < n; i++)
        {
            int idx = s[i] - 'a';
            if (first[idx] == -1) first[idx] = i;
            last[idx] = i;
        }

        int ans = 0;
        bool[] seen = new bool[26];

        for (int c = 0; c < 26; c++)
        {
            int left = first[c];
            int right = last[c];
            if (left == -1 || left == right) continue;

            Array.Clear(seen, 0, 26);
            for (int iPos = left + 1; iPos < right; iPos++)
                seen[s[iPos] - 'a'] = true;

            for (int k = 0; k < 26; k++)
                if (seen[k]) ans++;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const n = s.length;
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);
    
    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (first[idx] === -1) first[idx] = i;
        last[idx] = i;
    }
    
    let ans = 0;
    const seen = new Array(26);
    
    for (let c = 0; c < 26; ++c) {
        const l = first[c];
        const r = last[c];
        if (l === -1 || l === r) continue; // no room for a middle character
        
        // reset seen array
        for (let i = 0; i < 26; ++i) seen[i] = false;
        
        for (let k = l + 1; k < r; ++k) {
            const midIdx = s.charCodeAt(k) - 97;
            seen[midIdx] = true;
        }
        
        for (let i = 0; i < 26; ++i) {
            if (seen[i]) ++ans;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countPalindromicSubsequence(s: string): number {
    const n = s.length;
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);

    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (first[idx] === -1) first[idx] = i;
        last[idx] = i;
    }

    let ans = 0;
    const seen = new Array(26).fill(false);

    for (let c = 0; c < 26; ++c) {
        const left = first[c];
        const right = last[c];
        if (left === -1 || left >= right) continue;

        // reset seen array
        seen.fill(false);
        for (let i = left + 1; i < right; ++i) {
            const midIdx = s.charCodeAt(i) - 97;
            seen[midIdx] = true;
        }
        for (let k = 0; k < 26; ++k) {
            if (seen[k]) ans++;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        $n = strlen($s);
        $first = array_fill(0, 26, -1);
        $last  = array_fill(0, 26, -1);

        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97; // 'a' ASCII is 97
            if ($first[$idx] === -1) {
                $first[$idx] = $i;
            }
            $last[$idx] = $i;
        }

        $ans = 0;

        for ($c = 0; $c < 26; $c++) {
            $l = $first[$c];
            $r = $last[$c];

            if ($l === -1 || $r - $l <= 1) {
                continue; // no room for a middle character
            }

            $present = array_fill(0, 26, false);
            for ($k = $l + 1; $k < $r; $k++) {
                $midIdx = ord($s[$k]) - 97;
                $present[$midIdx] = true;
            }

            foreach ($present as $has) {
                if ($has) {
                    $ans++;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        let n = s.count
        var chars = [Int]()
        chars.reserveCapacity(n)
        for byte in s.utf8 {
            chars.append(Int(byte - 97)) // 'a' ascii is 97
        }
        
        var first = [Int](repeating: -1, count: 26)
        var last = [Int](repeating: -1, count: 26)
        
        for i in 0..<n {
            let c = chars[i]
            if first[c] == -1 { first[c] = i }
            last[c] = i
        }
        
        var ans = 0
        for idx in 0..<26 {
            let f = first[idx]
            let l = last[idx]
            if f == -1 || l <= f + 1 { continue } // no room for middle character
            var mask = 0
            for k in (f + 1)..<l {
                mask |= 1 << chars[k]
            }
            ans += mask.nonzeroBitCount
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        val n = s.length
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }

        for (i in 0 until n) {
            val idx = s[i] - 'a'
            if (first[idx] == -1) first[idx] = i
            last[idx] = i
        }

        var ans = 0
        for (c in 0 until 26) {
            val start = first[c]
            val end = last[c]
            if (start == -1 || start >= end) continue

            val seen = BooleanArray(26)
            for (j in start + 1 until end) {
                seen[s[j] - 'a'] = true
            }
            var cnt = 0
            for (b in seen) if (b) cnt++
            ans += cnt
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countPalindromicSubsequence(String s) {
    int n = s.length;
    List<int> first = List.filled(26, -1);
    List<int> last = List.filled(26, -1);

    for (int i = 0; i < n; i++) {
      int idx = s.codeUnitAt(i) - 97;
      if (first[idx] == -1) first[idx] = i;
      last[idx] = i;
    }

    int ans = 0;

    for (int c = 0; c < 26; c++) {
      int start = first[c];
      int end = last[c];
      if (start == -1 || start >= end) continue;

      List<bool> seen = List.filled(26, false);
      for (int i = start + 1; i < end; i++) {
        int mid = s.codeUnitAt(i) - 97;
        seen[mid] = true;
      }

      for (bool b in seen) {
        if (b) ans++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countPalindromicSubsequence(s string) int {
    first := make([]int, 26)
    last := make([]int, 26)
    for i := 0; i < 26; i++ {
        first[i] = -1
    }
    for idx := 0; idx < len(s); idx++ {
        c := int(s[idx] - 'a')
        if first[c] == -1 {
            first[c] = idx
        }
        last[c] = idx
    }

    ans := 0
    for c := 0; c < 26; c++ {
        if first[c] == -1 || first[c] >= last[c] {
            continue
        }
        var seen [26]bool
        for i := first[c] + 1; i < last[c]; i++ {
            seen[int(s[i]-'a')] = true
        }
        cnt := 0
        for _, v := range seen {
            if v {
                cnt++
            }
        }
        ans += cnt
    }
    return ans
}
```

## Ruby

```ruby
def count_palindromic_subsequence(s)
  first = Array.new(26, -1)
  last = Array.new(26, -1)

  s.each_byte.with_index do |b, i|
    idx = b - 97
    first[idx] = i if first[idx] == -1
    last[idx] = i
  end

  ans = 0
  26.times do |c|
    f = first[c]
    l = last[c]
    next if f == -1 || f + 1 >= l

    seen = Array.new(26, false)
    (f + 1...l).each do |j|
      mid_idx = s.getbyte(j) - 97
      seen[mid_idx] = true
    end
    ans += seen.count(true)
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countPalindromicSubsequence(s: String): Int = {
        val n = s.length
        val first = Array.fill(26)(-1)
        val last = Array.fill(26)(-1)

        var i = 0
        while (i < n) {
            val idx = s.charAt(i) - 'a'
            if (first(idx) == -1) first(idx) = i
            last(idx) = i
            i += 1
        }

        var ans = 0
        var c = 0
        while (c < 26) {
            val f = first(c)
            val l = last(c)
            if (f != -1 && f < l) {
                var mask = 0
                var j = f + 1
                while (j < l) {
                    val midIdx = s.charAt(j) - 'a'
                    mask |= (1 << midIdx)
                    j += 1
                }
                ans += Integer.bitCount(mask)
            }
            c += 1
        }

        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut first = [-1i32; 26];
        let mut last = [-1i32; 26];

        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if first[idx] == -1 {
                first[idx] = i as i32;
            }
            last[idx] = i as i32;
        }

        let mut ans: i32 = 0;

        for c in 0..26 {
            if first[c] == -1 {
                continue;
            }
            let left = (first[c] + 1) as usize;
            let right = last[c] as usize; // exclusive upper bound
            if left >= right {
                continue;
            }

            let mut mask: u32 = 0;
            for k in left..right {
                let mid_idx = (bytes[k] - b'a') as usize;
                mask |= 1 << mid_idx;
            }
            ans += mask.count_ones() as i32;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-palindromic-subsequence s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (first (make-vector 26 -1))
         (last (make-vector 26 -1)))
    ;; Record first and last occurrence of each character
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (when (= (vector-ref first idx) -1)
          (vector-set! first idx i))
        (vector-set! last idx i)))
    ;; Count unique palindromic subsequences of length 3
    (define ans 0)
    (for ([ch (in-range 26)])
      (let ((fi (vector-ref first ch))
            (la (vector-ref last ch)))
        (when (and (not (= fi -1)) (< fi la))
          (define present (make-vector 26 #f))
          (define cnt 0)
          (for ([j (in-range (+ fi 1) la)])
            (let* ((midc (string-ref s j))
                   (midIdx (- (char->integer midc) (char->integer #\a))))
              (unless (vector-ref present midIdx)
                (vector-set! present midIdx #t)
                (set! cnt (+ cnt 1)))))
          (set! ans (+ ans cnt)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_palindromic_subsequence/1]).

-spec count_palindromic_subsequence(S :: unicode:unicode_binary()) -> integer().
count_palindromic_subsequence(S) ->
    Chars = binary_to_list(S),
    Tuple = list_to_tuple(Chars),
    {FirstMap, LastMap} = build_maps(Chars, 0, #{}, #{}),
    maps:fold(fun(Key, FirstIdx, Acc) ->
        LastIdx = maps:get(Key, LastMap),
        case LastIdx - FirstIdx > 1 of
            true ->
                Mask = count_between(FirstIdx + 1, LastIdx - 1, Tuple, 0),
                Acc + popcnt(Mask);
            false -> Acc
        end
    end, 0, FirstMap).

build_maps([], _Idx, First, Last) -> {First, Last};
build_maps([C|Rest], Idx, First, Last) ->
    Offset = C - $a,
    NewFirst = case maps:is_key(Offset, First) of
        true -> First;
        false -> maps:put(Offset, Idx, First)
    end,
    NewLast = maps:put(Offset, Idx, Last),
    build_maps(Rest, Idx + 1, NewFirst, NewLast).

count_between(From, To, Tuple, Mask) when From > To ->
    Mask;
count_between(From, To, Tuple, Mask) ->
    Char = element(From + 1, Tuple),
    Offset = Char - $a,
    NewMask = Mask bor (1 bsl Offset),
    count_between(From + 1, To, Tuple, NewMask).

popcnt(N) -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N band (N - 1), Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    require Bitwise

    len = byte_size(s)

    first =
      List.duplicate(-1, 26)
      |> List.to_tuple()

    last =
      List.duplicate(-1, 26)
      |> List.to_tuple()

    {first, last} =
      0..(len - 1)
      |> Enum.reduce({first, last}, fn idx, {f_acc, l_acc} ->
        c = :binary.at(s, idx) - ?a

        f_new =
          if elem(f_acc, c) == -1 do
            put_elem(f_acc, c, idx)
          else
            f_acc
          end

        l_new = put_elem(l_acc, c, idx)
        {f_new, l_new}
      end)

    0..25
    |> Enum.reduce(0, fn ch, acc ->
      f = elem(first, ch)
      l = elem(last, ch)

      if f != -1 and l > f + 1 do
        mask =
          (f + 1)..(l - 1)
          |> Enum.reduce(0, fn idx, m ->
            mid_c = :binary.at(s, idx) - ?a
            Bitwise.bor(m, Bitwise.shift_left(1, mid_c))
          end)

        acc + popcount(mask)
      else
        acc
      end
    end)
  end

  defp popcount(x), do: popcount(x, 0)

  defp popcount(0, acc), do: acc

  defp popcount(x, acc) do
    popcount(Bitwise.bsr(x, 1), acc + Bitwise.band(x, 1))
  end
end
```
