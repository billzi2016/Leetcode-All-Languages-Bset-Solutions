# 0424. Longest Repeating Character Replacement

## Cpp

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> cnt(26, 0);
        int left = 0, maxCount = 0, result = 0;
        for (int right = 0; right < (int)s.size(); ++right) {
            cnt[s[right] - 'A']++;
            maxCount = max(maxCount, cnt[s[right] - 'A']);
            
            while ((right - left + 1) - maxCount > k) {
                cnt[s[left] - 'A']--;
                ++left;
                // recompute maxCount could be O(26), but we can keep it as is because
                // maxCount may be stale but window size condition ensures correctness.
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int[] cnt = new int[26];
        int left = 0, maxCount = 0, result = 0;
        for (int right = 0; right < s.length(); ++right) {
            int idx = s.charAt(right) - 'A';
            cnt[idx]++;
            maxCount = Math.max(maxCount, cnt[idx]);
            while (right - left + 1 - maxCount > k) {
                cnt[s.charAt(left) - 'A']--;
                left++;
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 26
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            if count[idx] > max_freq:
                max_freq = count[idx]

            # If replacements needed exceed k, shrink window
            while (right - left + 1) - max_freq > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1
                # Recalculate max_freq could be expensive; instead keep it as is because
                # window shrink only when condition violated, and max_freq may be stale but
                # does not affect correctness since we only compare against k.
                # However to ensure correctness for future expansions, we can update:
                # (optional) recompute max_freq from count array if needed
                # Here we recompute lazily when window size changes significantly:
                # Not necessary for O(N) solution.

            result = max(result, right - left + 1)

        return result
```

## Python3

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        result = 0
        for right, ch in enumerate(s):
            idx = ord(ch) - 65
            count[idx] += 1
            if count[idx] > max_freq:
                max_freq = count[idx]
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - 65] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
```

## C

```c
#include <string.h>

int characterReplacement(char* s, int k) {
    int n = strlen(s);
    int count[26] = {0};
    int left = 0, maxCount = 0, result = 0;
    
    for (int right = 0; right < n; ++right) {
        int idx = s[right] - 'A';
        count[idx]++;
        if (count[idx] > maxCount) {
            maxCount = count[idx];
        }
        
        while ((right - left + 1) - maxCount > k) {
            int leftIdx = s[left] - 'A';
            count[leftIdx]--;
            left++;
        }
        
        int curLen = right - left + 1;
        if (curLen > result) {
            result = curLen;
        }
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int CharacterReplacement(string s, int k) {
        int[] count = new int[26];
        int left = 0, maxCount = 0, result = 0;
        for (int right = 0; right < s.Length; right++) {
            int idx = s[right] - 'A';
            count[idx]++;
            if (count[idx] > maxCount) maxCount = count[idx];
            while (right - left + 1 - maxCount > k) {
                int lIdx = s[left] - 'A';
                count[lIdx]--;
                left++;
            }
            int len = right - left + 1;
            if (len > result) result = len;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    const n = s.length;
    const cnt = new Array(26).fill(0);
    let left = 0, maxFreq = 0, ans = 0;

    for (let right = 0; right < n; ++right) {
        const idx = s.charCodeAt(right) - 65;
        cnt[idx]++;
        if (cnt[idx] > maxFreq) maxFreq = cnt[idx];

        while ((right - left + 1) - maxFreq > k) {
            const lIdx = s.charCodeAt(left) - 65;
            cnt[lIdx]--;
            left++;
        }

        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
```

## Typescript

```typescript
function characterReplacement(s: string, k: number): number {
    const count = new Array(26).fill(0);
    let left = 0;
    let maxCount = 0;
    let result = 0;

    for (let right = 0; right < s.length; ++right) {
        const idx = s.charCodeAt(right) - 65;
        count[idx]++;
        if (count[idx] > maxCount) maxCount = count[idx];

        while ((right - left + 1) - maxCount > k) {
            const lIdx = s.charCodeAt(left) - 65;
            count[lIdx]--;
            left++;
        }

        const windowLen = right - left + 1;
        if (windowLen > result) result = windowLen;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function characterReplacement($s, $k) {
        $n = strlen($s);
        if ($n == 0) return 0;

        $counts = array_fill(0, 26, 0);
        $left = 0;
        $maxCount = 0;
        $result = 0;

        for ($right = 0; $right < $n; $right++) {
            $idx = ord($s[$right]) - ord('A');
            $counts[$idx]++;
            if ($counts[$idx] > $maxCount) {
                $maxCount = $counts[$idx];
            }

            while (($right - $left + 1) - $maxCount > $k) {
                $leftIdx = ord($s[$left]) - ord('A');
                $counts[$leftIdx]--;
                $left++;
                // No need to update $maxCount here; it can stay as historical max.
            }

            $currentLen = $right - $left + 1;
            if ($currentLen > $result) {
                $result = $currentLen;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func characterReplacement(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        var count = [Int](repeating: 0, count: 26)
        let base = Int(Character("A").unicodeScalars.first!.value)
        var left = 0
        var maxFreq = 0
        var result = 0
        
        for right in 0..<chars.count {
            let idx = Int(chars[right].unicodeScalars.first!.value) - base
            count[idx] += 1
            if count[idx] > maxFreq {
                maxFreq = count[idx]
            }
            
            while (right - left + 1) - maxFreq > k {
                let leftIdx = Int(chars[left].unicodeScalars.first!.value) - base
                count[leftIdx] -= 1
                left += 1
            }
            
            let windowLen = right - left + 1
            if windowLen > result {
                result = windowLen
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        val count = IntArray(26)
        var left = 0
        var maxCount = 0
        var result = 0
        for (right in s.indices) {
            val idx = s[right] - 'A'
            count[idx]++
            if (count[idx] > maxCount) maxCount = count[idx]
            while (right - left + 1 - maxCount > k) {
                val lIdx = s[left] - 'A'
                count[lIdx]--
                left++
            }
            result = kotlin.math.max(result, right - left + 1)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int characterReplacement(String s, int k) {
    List<int> cnt = List.filled(26, 0);
    int left = 0;
    int maxCount = 0;
    int result = 0;

    for (int right = 0; right < s.length; ++right) {
      int idx = s.codeUnitAt(right) - 65;
      cnt[idx]++;
      if (cnt[idx] > maxCount) maxCount = cnt[idx];

      while ((right - left + 1) - maxCount > k) {
        int leftIdx = s.codeUnitAt(left) - 65;
        cnt[leftIdx]--;
        left++;
      }

      int windowLen = right - left + 1;
      if (windowLen > result) result = windowLen;
    }
    return result;
  }
}
```

## Golang

```go
func characterReplacement(s string, k int) int {
    var cnt [26]int
    left, maxFreq, result := 0, 0, 0

    for right := 0; right < len(s); right++ {
        idx := int(s[right] - 'A')
        cnt[idx]++
        if cnt[idx] > maxFreq {
            maxFreq = cnt[idx]
        }

        // If replacements needed exceed k, shrink window
        if (right-left+1)-maxFreq > k {
            leftIdx := int(s[left] - 'A')
            cnt[leftIdx]--
            left++
        }

        if curLen := right - left + 1; curLen > result {
            result = curLen
        }
    }
    return result
}
```

## Ruby

```ruby
def character_replacement(s, k)
  counts = Array.new(26, 0)
  left = 0
  max_count = 0
  result = 0
  s.each_char.with_index do |ch, right|
    idx = ch.ord - 65
    counts[idx] += 1
    max_count = [max_count, counts[idx]].max
    while (right - left + 1) - max_count > k
      l_idx = s[left].ord - 65
      counts[l_idx] -= 1
      left += 1
    end
    result = [result, right - left + 1].max
  end
  result
end
```

## Scala

```scala
object Solution {
    def characterReplacement(s: String, k: Int): Int = {
        val n = s.length
        if (n == 0) return 0
        val count = Array.fill(26)(0)
        var left = 0
        var maxCount = 0
        var result = 0

        for (right <- 0 until n) {
            val idx = s.charAt(right) - 'A'
            count(idx) += 1
            if (count(idx) > maxCount) maxCount = count(idx)

            while ((right - left + 1) - maxCount > k) {
                val leftIdx = s.charAt(left) - 'A'
                count(leftIdx) -= 1
                left += 1
                // Note: maxCount may be stale but it's okay; window will shrink until condition satisfied.
            }

            val windowLen = right - left + 1
            if (windowLen > result) result = windowLen
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut cnt = [0usize; 26];
        let mut left = 0usize;
        let mut max_cnt = 0usize;
        let mut ans = 0usize;
        let k_usize = k as usize;

        for right in 0..n {
            let idx = (bytes[right] - b'A') as usize;
            cnt[idx] += 1;
            if cnt[idx] > max_cnt {
                max_cnt = cnt[idx];
            }

            while right - left + 1 > max_cnt + k_usize {
                let l_idx = (bytes[left] - b'A') as usize;
                cnt[l_idx] -= 1;
                left += 1;
                // recompute current maximum frequency in the window
                max_cnt = *cnt.iter().max().unwrap();
            }

            let window_len = right - left + 1;
            if window_len > ans {
                ans = window_len;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (character-replacement s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (counts (make-vector 26 0))
         (left 0)
         (max-count 0)
         (ans 0))
    (for ([right (in-range n)])
      (define idx (- (char->integer (string-ref s right))
                     (char->integer #\A)))
      (vector-set! counts idx (+ (vector-ref counts idx) 1))
      (set! max-count (max max-count (vector-ref counts idx)))
      ;; shrink window while invalid
      (let loop ()
        (when (> (- (+ 1 (- right left)) max-count) k)
          (define lidx (- (char->integer (string-ref s left))
                          (char->integer #\A)))
          (vector-set! counts lidx (- (vector-ref counts lidx) 1))
          (set! left (+ left 1))
          (loop)))
      (set! ans (max ans (+ 1 (- right left)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([character_replacement/2]).

-spec character_replacement(S :: unicode:unicode_binary(), K :: integer()) -> integer().
character_replacement(S, K) ->
    Len = byte_size(S),
    go(0, 0, #{}, 0, 0, S, K, Len).

go(Right, Left, Counts, MaxCount, Best, _S, _K, Len) when Right == Len ->
    Best;
go(Right, Left, Counts, MaxCount, Best, S, K, Len) ->
    Char = binary:first(binary:part(S, {Right, 1})),
    Idx = Char - $A,
    Cnt = maps:get(Idx, Counts, 0) + 1,
    NewCounts = maps:put(Idx, Cnt, Counts),
    NewMaxCount = if Cnt > MaxCount -> Cnt; true -> MaxCount end,
    {NewLeft, ShrunkCounts} = shrink(Left, NewCounts, NewMaxCount, S, K, Right),
    NewBest = max(Best, Right - NewLeft + 1),
    go(Right + 1, NewLeft, ShrunkCounts, NewMaxCount, NewBest, S, K, Len).

shrink(Left, Counts, MaxCount, S, K, Right) ->
    WindowSize = Right - Left + 1,
    case WindowSize - MaxCount > K of
        true ->
            LChar = binary:first(binary:part(S, {Left, 1})),
            LIdx = LChar - $A,
            LCnt = maps:get(LIdx, Counts),
            UpdatedLCnt = LCnt - 1,
            NewCounts = if UpdatedLCnt == 0 -> maps:remove(LIdx, Counts); true -> maps:put(LIdx, UpdatedLCnt, Counts) end,
            shrink(Left + 1, NewCounts, MaxCount, S, K, Right);
        false ->
            {Left, Counts}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec character_replacement(s :: String.t(), k :: integer) :: integer
  def character_replacement(s, k) do
    chars = :binary.bin_to_list(s)

    {answer, _max_count, _counts, _win_len, _queue} =
      Enum.reduce(chars, {0, 0, make_counts_tuple(), 0, :queue.new()}, fn c,
          {ans, max_count, counts, win_len, queue} ->
        idx = c - ?A
        cnt = elem(counts, idx) + 1
        counts = put_elem(counts, idx, cnt)
        max_count = if cnt > max_count, do: cnt, else: max_count

        win_len = win_len + 1
        queue = :queue.in(c, queue)

        {win_len, counts, queue} = shrink(win_len, max_count, k, counts, queue)

        ans = if win_len > ans, do: win_len, else: ans
        {ans, max_count, counts, win_len, queue}
      end)

    answer
  end

  defp make_counts_tuple do
    :erlang.make_tuple(26, 0)
  end

  defp shrink(win_len, max_count, k, counts, queue) do
    if win_len - max_count > k do
      {{:value, left_char}, q2} = :queue.out(queue)
      idx_left = left_char - ?A
      cnt_left = elem(counts, idx_left) - 1
      counts = put_elem(counts, idx_left, cnt_left)
      shrink(win_len - 1, max_count, k, counts, q2)
    else
      {win_len, counts, queue}
    end
  end
end
```
