# 1525. Number of Good Ways to Split a String

## Cpp

```cpp
class Solution {
public:
    int numSplits(string s) {
        int n = s.size();
        if (n < 2) return 0;
        vector<int> suffixDistinct(n);
        bool seenRight[26] = {false};
        int distinctRight = 0;
        for (int i = n - 1; i >= 0; --i) {
            int idx = s[i] - 'a';
            if (!seenRight[idx]) {
                seenRight[idx] = true;
                ++distinctRight;
            }
            suffixDistinct[i] = distinctRight;
        }
        bool seenLeft[26] = {false};
        int distinctLeft = 0;
        int ans = 0;
        for (int i = 0; i < n - 1; ++i) {
            int idx = s[i] - 'a';
            if (!seenLeft[idx]) {
                seenLeft[idx] = true;
                ++distinctLeft;
            }
            if (distinctLeft == suffixDistinct[i + 1])
                ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numSplits(String s) {
        int n = s.length();
        if (n < 2) return 0;
        int[] rightFreq = new int[26];
        for (int i = 0; i < n; i++) {
            rightFreq[s.charAt(i) - 'a']++;
        }
        int rightDistinct = 0;
        for (int cnt : rightFreq) if (cnt > 0) rightDistinct++;

        boolean[] leftSeen = new boolean[26];
        int leftDistinct = 0;
        int goodSplits = 0;

        for (int i = 0; i < n - 1; i++) {
            int idx = s.charAt(i) - 'a';
            if (!leftSeen[idx]) {
                leftSeen[idx] = true;
                leftDistinct++;
            }
            rightFreq[idx]--;
            if (rightFreq[idx] == 0) {
                rightDistinct--;
            }
            if (leftDistinct == rightDistinct) {
                goodSplits++;
            }
        }
        return goodSplits;
    }
}
```

## Python

```python
class Solution:
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        suffix = [0] * n
        mask = 0
        for i in range(n - 1, -1, -1):
            mask |= 1 << (ord(s[i]) - 97)
            suffix[i] = mask.bit_count()
        ans = 0
        left_mask = 0
        for i in range(n - 1):
            left_mask |= 1 << (ord(s[i]) - 97)
            if left_mask.bit_count() == suffix[i + 1]:
                ans += 1
        return ans
```

## Python3

```python
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # suffix distinct counts
        suffix_counts = [0] * n
        seen_right = [False] * 26
        distinct_right = 0
        for i in range(n - 1, -1, -1):
            idx = ord(s[i]) - 97
            if not seen_right[idx]:
                seen_right[idx] = True
                distinct_right += 1
            suffix_counts[i] = distinct_right

        # iterate left side
        seen_left = [False] * 26
        distinct_left = 0
        good_splits = 0
        for i in range(n - 1):  # split after i, right starts at i+1
            idx = ord(s[i]) - 97
            if not seen_left[idx]:
                seen_left[idx] = True
                distinct_left += 1
            if distinct_left == suffix_counts[i + 1]:
                good_splits += 1

        return good_splits
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

int numSplits(char* s) {
    int n = 0;
    while (s[n]) n++;
    if (n <= 1) return 0;

    int *suffix = (int*)malloc(sizeof(int) * n);
    bool seen[26] = {false};
    int cnt = 0;
    for (int i = n - 1; i >= 0; --i) {
        int idx = s[i] - 'a';
        if (!seen[idx]) {
            seen[idx] = true;
            ++cnt;
        }
        suffix[i] = cnt;
    }

    bool leftSeen[26] = {false};
    int leftCnt = 0, ans = 0;
    for (int i = 0; i < n - 1; ++i) {
        int idx = s[i] - 'a';
        if (!leftSeen[idx]) {
            leftSeen[idx] = true;
            ++leftCnt;
        }
        if (leftCnt == suffix[i + 1])
            ++ans;
    }

    free(suffix);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumSplits(string s)
    {
        int n = s.Length;
        if (n < 2) return 0;

        int[] suffixDistinct = new int[n];
        bool[] seenRight = new bool[26];
        int distinctRight = 0;
        for (int i = n - 1; i >= 0; --i)
        {
            int idx = s[i] - 'a';
            if (!seenRight[idx])
            {
                seenRight[idx] = true;
                ++distinctRight;
            }
            suffixDistinct[i] = distinctRight;
        }

        bool[] seenLeft = new bool[26];
        int distinctLeft = 0;
        int ans = 0;
        for (int i = 0; i < n - 1; ++i)
        {
            int idx = s[i] - 'a';
            if (!seenLeft[idx])
            {
                seenLeft[idx] = true;
                ++distinctLeft;
            }
            if (distinctLeft == suffixDistinct[i + 1])
                ++ans;
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
var numSplits = function(s) {
    const n = s.length;
    if (n < 2) return 0;

    const suffixDistinct = new Array(n);
    const seenRight = new Array(26).fill(false);
    let distinctRight = 0;

    for (let i = n - 1; i >= 0; --i) {
        const idx = s.charCodeAt(i) - 97;
        if (!seenRight[idx]) {
            seenRight[idx] = true;
            ++distinctRight;
        }
        suffixDistinct[i] = distinctRight;
    }

    const seenLeft = new Array(26).fill(false);
    let distinctLeft = 0;
    let ans = 0;

    for (let i = 0; i < n - 1; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (!seenLeft[idx]) {
            seenLeft[idx] = true;
            ++distinctLeft;
        }
        if (distinctLeft === suffixDistinct[i + 1]) {
            ++ans;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function numSplits(s: string): number {
    const n = s.length;
    if (n < 2) return 0;

    const suffixDistinct = new Array<number>(n);
    const seenRight = new Array<boolean>(26).fill(false);
    let distinctRight = 0;

    for (let i = n - 1; i >= 0; --i) {
        const idx = s.charCodeAt(i) - 97;
        if (!seenRight[idx]) {
            seenRight[idx] = true;
            ++distinctRight;
        }
        suffixDistinct[i] = distinctRight;
    }

    const seenLeft = new Array<boolean>(26).fill(false);
    let distinctLeft = 0;
    let goodSplits = 0;

    for (let i = 0; i < n - 1; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (!seenLeft[idx]) {
            seenLeft[idx] = true;
            ++distinctLeft;
        }
        if (distinctLeft === suffixDistinct[i + 1]) {
            ++goodSplits;
        }
    }

    return goodSplits;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSplits($s) {
        $n = strlen($s);
        if ($n < 2) return 0;

        // Count distinct letters in the whole string (right side initially)
        $rightCounts = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $rightCounts[$idx]++;
        }
        $distinctRight = 0;
        foreach ($rightCounts as $cnt) {
            if ($cnt > 0) $distinctRight++;
        }

        $leftCounts = array_fill(0, 26, 0);
        $distinctLeft = 0;
        $ans = 0;

        // Move characters one by one from right to left and compare distinct counts
        for ($i = 0; $i < $n - 1; $i++) {
            $idx = ord($s[$i]) - 97;

            // Update right side
            if ($rightCounts[$idx] == 1) {
                $distinctRight--;
            }
            $rightCounts[$idx]--;

            // Update left side
            if ($leftCounts[$idx] == 0) {
                $distinctLeft++;
            }
            $leftCounts[$idx]++;

            if ($distinctLeft === $distinctRight) {
                $ans++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numSplits(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        let n = bytes.count
        if n < 2 { return 0 }
        
        var suffixDistinct = [Int](repeating: 0, count: n)
        var rightFreq = [Int](repeating: 0, count: 26)
        var distinctRight = 0
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            let idx = Int(bytes[i] - 97)
            if rightFreq[idx] == 0 { distinctRight += 1 }
            rightFreq[idx] += 1
            suffixDistinct[i] = distinctRight
        }
        
        var leftFreq = [Int](repeating: 0, count: 26)
        var distinctLeft = 0
        var result = 0
        
        for i in 0..<(n - 1) {
            let idx = Int(bytes[i] - 97)
            if leftFreq[idx] == 0 { distinctLeft += 1 }
            leftFreq[idx] += 1
            if distinctLeft == suffixDistinct[i + 1] {
                result += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSplits(s: String): Int {
        val n = s.length
        if (n < 2) return 0

        val suffixDistinct = IntArray(n)
        val seenRight = BooleanArray(26)
        var distinctRight = 0
        for (i in n - 1 downTo 0) {
            val idx = s[i] - 'a'
            if (!seenRight[idx]) {
                seenRight[idx] = true
                distinctRight++
            }
            suffixDistinct[i] = distinctRight
        }

        val seenLeft = BooleanArray(26)
        var distinctLeft = 0
        var goodSplits = 0
        for (i in 0 until n - 1) {
            val idx = s[i] - 'a'
            if (!seenLeft[idx]) {
                seenLeft[idx] = true
                distinctLeft++
            }
            if (distinctLeft == suffixDistinct[i + 1]) {
                goodSplits++
            }
        }

        return goodSplits
    }
}
```

## Dart

```dart
class Solution {
  int numSplits(String s) {
    int n = s.length;
    List<int> suffixDistinct = List.filled(n, 0);
    List<int> rightCount = List.filled(26, 0);
    int distinctRight = 0;
    for (int i = n - 1; i >= 0; --i) {
      int idx = s.codeUnitAt(i) - 97;
      if (rightCount[idx] == 0) distinctRight++;
      rightCount[idx]++;
      suffixDistinct[i] = distinctRight;
    }
    List<int> leftCount = List.filled(26, 0);
    int distinctLeft = 0;
    int ans = 0;
    for (int i = 0; i < n - 1; ++i) {
      int idx = s.codeUnitAt(i) - 97;
      if (leftCount[idx] == 0) distinctLeft++;
      leftCount[idx]++;
      if (distinctLeft == suffixDistinct[i + 1]) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func numSplits(s string) int {
	n := len(s)
	if n <= 1 {
		return 0
	}
	suffix := make([]int, n)
	var seenRight [26]bool
	distinct := 0
	for i := n - 1; i >= 0; i-- {
		idx := s[i] - 'a'
		if !seenRight[idx] {
			seenRight[idx] = true
			distinct++
		}
		suffix[i] = distinct
	}
	ans := 0
	var seenLeft [26]bool
	leftDistinct := 0
	for i := 0; i < n-1; i++ {
		idx := s[i] - 'a'
		if !seenLeft[idx] {
			seenLeft[idx] = true
			leftDistinct++
		}
		if leftDistinct == suffix[i+1] {
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def num_splits(s)
  n = s.length
  right = Array.new(n, 0)
  seen_right = Array.new(26, false)
  distinct = 0
  (n - 1).downto(0) do |i|
    idx = s.getbyte(i) - 97
    unless seen_right[idx]
      seen_right[idx] = true
      distinct += 1
    end
    right[i] = distinct
  end

  seen_left = Array.new(26, false)
  left_distinct = 0
  ans = 0
  (0...n - 1).each do |i|
    idx = s.getbyte(i) - 97
    unless seen_left[idx]
      seen_left[idx] = true
      left_distinct += 1
    end
    ans += 1 if left_distinct == right[i + 1]
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numSplits(s: String): Int = {
        val n = s.length
        val suffixDistinct = new Array[Int](n)
        val seenRight = new Array[Boolean](26)
        var distinctRight = 0
        for (i <- (0 until n).reverse) {
            val idx = s.charAt(i) - 'a'
            if (!seenRight(idx)) {
                seenRight(idx) = true
                distinctRight += 1
            }
            suffixDistinct(i) = distinctRight
        }

        val seenLeft = new Array[Boolean](26)
        var distinctLeft = 0
        var ans = 0
        for (i <- 0 until n - 1) {
            val idx = s.charAt(i) - 'a'
            if (!seenLeft(idx)) {
                seenLeft(idx) = true
                distinctLeft += 1
            }
            if (distinctLeft == suffixDistinct(i + 1)) ans += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_splits(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n <= 1 {
            return 0;
        }
        // suffix[i] = distinct letters in s[i..]
        let mut suffix = vec![0usize; n];
        let mut seen_right = [false; 26];
        let mut cnt_right = 0usize;
        for i in (0..n).rev() {
            let idx = (bytes[i] - b'a') as usize;
            if !seen_right[idx] {
                seen_right[idx] = true;
                cnt_right += 1;
            }
            suffix[i] = cnt_right;
        }

        let mut seen_left = [false; 26];
        let mut cnt_left = 0usize;
        let mut ans = 0i32;

        for i in 0..n - 1 {
            let idx = (bytes[i] - b'a') as usize;
            if !seen_left[idx] {
                seen_left[idx] = true;
                cnt_left += 1;
            }
            if cnt_left == suffix[i + 1] {
                ans += 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (num-splits s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (suffix (make-vector n 0))
         (seenR (make-vector 26 #f))
         (cntR 0))
    ;; compute distinct counts for suffixes
    (for ([i (in-range (sub1 n) -1 -1)]) ; from n-2 down to 0
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (when (not (vector-ref seenR idx))
          (vector-set! seenR idx #t)
          (set! cntR (+ cntR 1))))
      (vector-set! suffix i cntR))
    ;; iterate left side and count good splits
    (let ((seenL (make-vector 26 #f))
          (cntL 0)
          (ans 0))
      (for ([i (in-range (- n 1))]) ; i = 0 .. n-2
        (let* ((c (string-ref s i))
               (idx (- (char->integer c) (char->integer #\a))))
          (when (not (vector-ref seenL idx))
            (vector-set! seenL idx #t)
            (set! cntL (+ cntL 1)))))
        (when (= cntL (vector-ref suffix (+ i 1)))
          (set! ans (+ ans 1))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([num_splits/1]).

-spec num_splits(S :: unicode:unicode_binary()) -> integer().
num_splits(S) ->
    L = binary_to_list(S),
    N = length(L),
    case N of
        0 -> 0;
        _ ->
            RevL = lists:reverse(L),
            SuffixCountsRev = build_suffix_counts(RevL, 0, 0, []),
            SuffixCounts = lists:reverse(SuffixCountsRev),
            SuffixTuple = list_to_tuple(SuffixCounts),
            process_splits(L, 0, 0, 0, SuffixTuple, N, 0)
    end.

build_suffix_counts([], _Mask, _Count, Acc) -> Acc;
build_suffix_counts([C|Rest], Mask, Count, Acc) ->
    Bit = 1 bsl (C - $a),
    case (Mask band Bit) of
        0 ->
            NewMask = Mask bor Bit,
            NewCount = Count + 1;
        _ ->
            NewMask = Mask,
            NewCount = Count
    end,
    build_suffix_counts(Rest, NewMask, NewCount, [NewCount | Acc]).

process_splits(_List, Idx, _LeftMask, _LeftCount, _SuffixTuple, N, Acc) when Idx >= N-1 ->
    Acc;
process_splits([C|Rest], Idx, LeftMask, LeftCount, SuffixTuple, N, Acc) ->
    Bit = 1 bsl (C - $a),
    case (LeftMask band Bit) of
        0 ->
            NewMask = LeftMask bor Bit,
            NewLC = LeftCount + 1;
        _ ->
            NewMask = LeftMask,
            NewLC = LeftCount
    end,
    RightCount = element(Idx+2, SuffixTuple),
    NewAcc = if NewLC == RightCount -> Acc + 1; true -> Acc end,
    process_splits(Rest, Idx+1, NewMask, NewLC, SuffixTuple, N, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_splits(s :: String.t()) :: integer
  def num_splits(s) do
    import Bitwise

    n = byte_size(s)
    bytes = :binary.bin_to_list(s)

    freq =
      Enum.reduce(bytes, %{}, fn b, acc ->
        c = b - ?a
        Map.update(acc, c, 1, &(&1 + 1))
      end)

    rdist = map_size(freq)
    lmask = 0
    ldist = 0
    ans = 0

    {_, _, _, _, result} =
      Enum.with_index(bytes)
      |> Enum.reduce_while({freq, lmask, ldist, rdist, ans}, fn {b, idx},
                                                             {freq, lmask, ldist, rdist, acc} ->
        c = b - ?a

        # update left side distinct count
        if (lmask &&& (1 <<< c)) == 0 do
          new_lmask = lmask ||| (1 <<< c)
          new_ldist = ldist + 1
        else
          new_lmask = lmask
          new_ldist = ldist
        end

        # update right side frequency and distinct count
        cnt = Map.get(freq, c)

        if cnt == 1 do
          new_freq = Map.delete(freq, c)
          new_rdist = rdist - 1
        else
          new_freq = Map.put(freq, c, cnt - 1)
          new_rdist = rdist
        end

        # check split after current character (if not at the last position)
        new_acc =
          if idx < n - 1 && new_ldist == new_rdist do
            acc + 1
          else
            acc
          end

        if idx == n - 1 do
          {:halt, {new_freq, new_lmask, new_ldist, new_rdist, new_acc}}
        else
          {:cont, {new_freq, new_lmask, new_ldist, new_rdist, new_acc}}
        end
      end)

    result
  end
end
```
