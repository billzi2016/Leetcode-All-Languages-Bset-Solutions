# 2516. Take K of Each Character From Left and Right

## Cpp

```cpp
class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = s.size();
        array<int,3> total{0,0,0};
        for(char c: s){
            if(c=='a') total[0]++;
            else if(c=='b') total[1]++;
            else total[2]++;
        }
        for(int cnt: total){
            if(cnt < k) return -1;
        }
        if(k==0) return 0;
        array<int,3> limit{total[0]-k, total[1]-k, total[2]-k};
        array<int,3> window{0,0,0};
        int left = 0, maxLen = 0;
        for(int right=0; right<n; ++right){
            int idx = (s[right]=='a')?0:(s[right]=='b'?1:2);
            ++window[idx];
            while(window[0] > limit[0] || window[1] > limit[1] || window[2] > limit[2]){
                int lidx = (s[left]=='a')?0:(s[left]=='b'?1:2);
                --window[lidx];
                ++left;
            }
            maxLen = max(maxLen, right - left + 1);
        }
        return n - maxLen;
    }
};
```

## Java

```java
class Solution {
    public int takeCharacters(String s, int k) {
        int n = s.length();
        if (k == 0) return 0;
        int[] total = new int[3];
        for (int i = 0; i < n; i++) {
            total[s.charAt(i) - 'a']++;
        }
        for (int cnt : total) {
            if (cnt < k) return -1;
        }

        int[] window = new int[3];
        int left = 0, maxLen = 0;

        for (int right = 0; right < n; right++) {
            window[s.charAt(right) - 'a']++;

            while (left <= right && (total[0] - window[0] < k ||
                                     total[1] - window[1] < k ||
                                     total[2] - window[2] < k)) {
                window[s.charAt(left) - 'a']--;
                left++;
            }

            // now the window [left, right] is valid
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return n - maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # total counts of each character
        total = [0, 0, 0]  # a,b,c
        for ch in s:
            total[ord(ch) - 97] += 1

        # if any character appears less than k times, impossible
        if any(cnt < k for cnt in total):
            return -1

        # maximum allowed counts inside the remaining middle window
        limit = [cnt - k for cnt in total]

        left = 0
        max_len = 0
        window = [0, 0, 0]

        for right in range(n):
            idx = ord(s[right]) - 97
            window[idx] += 1

            # shrink window while it violates limits
            while any(window[i] > limit[i] for i in range(3)):
                idx_left = ord(s[left]) - 97
                window[idx_left] -= 1
                left += 1

            # update longest valid window size
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len

        return n - max_len
```

## Python3

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        idx_map = {'a': 0, 'b': 1, 'c': 2}
        total = [0, 0, 0]
        for ch in s:
            total[idx_map[ch]] += 1
        if any(cnt < k for cnt in total):
            return -1

        limit = [cnt - k for cnt in total]  # max allowed inside removable window
        cur = [0, 0, 0]
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            i = idx_map[ch]
            cur[i] += 1
            while any(cur[j] > limit[j] for j in range(3)):
                li = idx_map[s[left]]
                cur[li] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len
```

## C

```c
#include <string.h>

int takeCharacters(char* s, int k) {
    int n = strlen(s);
    int total[3] = {0};
    for (int i = 0; i < n; ++i) {
        total[s[i] - 'a']++;
    }
    if (total[0] < k || total[1] < k || total[2] < k) return -1;

    int allowed[3];
    for (int i = 0; i < 3; ++i) allowed[i] = total[i] - k;

    int cur[3] = {0};
    int left = 0, maxLen = 0;
    for (int right = 0; right < n; ++right) {
        int idx = s[right] - 'a';
        cur[idx]++;
        while (cur[0] > allowed[0] || cur[1] > allowed[1] || cur[2] > allowed[2]) {
            int lidx = s[left] - 'a';
            cur[lidx]--;
            left++;
        }
        int len = right - left + 1;
        if (len > maxLen) maxLen = len;
    }
    return n - maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int TakeCharacters(string s, int k)
    {
        int n = s.Length;
        if (k == 0) return 0;

        int[] total = new int[3];
        foreach (char c in s)
        {
            total[c - 'a']++; // 'a','b','c' are consecutive
        }

        for (int i = 0; i < 3; i++)
        {
            if (total[i] < k) return -1;
        }

        int[] window = new int[3];
        int left = 0, maxWindow = 0;

        for (int right = 0; right < n; right++)
        {
            window[s[right] - 'a']++;

            while ((total[0] - window[0] < k) ||
                   (total[1] - window[1] < k) ||
                   (total[2] - window[2] < k))
            {
                window[s[left] - 'a']--;
                left++;
            }

            int currentLen = right - left + 1;
            if (currentLen > maxWindow) maxWindow = currentLen;
        }

        return n - maxWindow;
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
var takeCharacters = function(s, k) {
    const n = s.length;
    // total counts of a,b,c
    const total = [0, 0, 0];
    for (let i = 0; i < n; ++i) {
        total[s.charCodeAt(i) - 97]++;
    }
    // if any character appears less than k times, impossible
    if (total[0] < k || total[1] < k || total[2] < k) return -1;
    
    // maximum allowed counts inside the untouched window
    const limit = [total[0] - k, total[1] - k, total[2] - k];
    
    let left = 0;
    const win = [0, 0, 0];
    let maxLen = 0;
    
    for (let right = 0; right < n; ++right) {
        win[s.charCodeAt(right) - 97]++;
        while (win[0] > limit[0] || win[1] > limit[1] || win[2] > limit[2]) {
            win[s.charCodeAt(left) - 97]--;
            left++;
        }
        const curLen = right - left + 1;
        if (curLen > maxLen) maxLen = curLen;
    }
    
    return n - maxLen;
};
```

## Typescript

```typescript
function takeCharacters(s: string, k: number): number {
    const n = s.length;
    if (k === 0) return 0;

    const total = [0, 0, 0];
    for (let i = 0; i < n; ++i) {
        const c = s.charCodeAt(i);
        if (c === 97) total[0]++;          // 'a'
        else if (c === 98) total[1]++;     // 'b'
        else total[2]++;                   // 'c'
    }

    for (let i = 0; i < 3; ++i) {
        if (total[i] < k) return -1;
    }

    const allowed = [total[0] - k, total[1] - k, total[2] - k];
    const window = [0, 0, 0];
    let left = 0;
    let maxWindow = 0;

    for (let right = 0; right < n; ++right) {
        const rc = s.charCodeAt(right);
        if (rc === 97) window[0]++;
        else if (rc === 98) window[1]++;
        else window[2]++;

        while (window[0] > allowed[0] || window[1] > allowed[1] || window[2] > allowed[2]) {
            const lc = s.charCodeAt(left);
            if (lc === 97) window[0]--;
            else if (lc === 98) window[1]--;
            else window[2]--;
            left++;
        }

        const curLen = right - left + 1;
        if (curLen > maxWindow) maxWindow = curLen;
    }

    return n - maxWindow;
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
    function takeCharacters($s, $k) {
        $n = strlen($s);
        if ($k == 0) return 0;

        // total counts of each character
        $total = [0, 0, 0]; // a, b, c
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch === 'a') {
                $total[0]++;
            } elseif ($ch === 'b') {
                $total[1]++;
            } else { // 'c'
                $total[2]++;
            }
        }

        // impossible case
        if ($total[0] < $k || $total[1] < $k || $total[2] < $k) {
            return -1;
        }

        // maximum allowed counts inside the remaining window
        $limit = [
            $total[0] - $k,
            $total[1] - $k,
            $total[2] - $k
        ];

        $window = [0, 0, 0];
        $left = 0;
        $maxLen = 0;

        for ($right = 0; $right < $n; $right++) {
            $ch = $s[$right];
            if ($ch === 'a') {
                $window[0]++;
            } elseif ($ch === 'b') {
                $window[1]++;
            } else { // 'c'
                $window[2]++;
            }

            while ($window[0] > $limit[0] || $window[1] > $limit[1] || $window[2] > $limit[2]) {
                $chL = $s[$left];
                if ($chL === 'a') {
                    $window[0]--;
                } elseif ($chL === 'b') {
                    $window[1]--;
                } else { // 'c'
                    $window[2]--;
                }
                $left++;
            }

            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }

        return $n - $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func takeCharacters(_ s: String, _ k: Int) -> Int {
        let n = s.count
        if k == 0 { return 0 }
        var total = [0, 0, 0]   // a, b, c counts
        for ch in s {
            switch ch {
            case "a": total[0] += 1
            case "b": total[1] += 1
            default:  total[2] += 1   // 'c'
            }
        }
        for cnt in total {
            if cnt < k { return -1 }
        }
        let limit = [total[0] - k, total[1] - k, total[2] - k]
        var window = [0, 0, 0]
        var left = 0
        var maxLen = 0
        let chars = Array(s)
        for right in 0..<n {
            let idx: Int
            switch chars[right] {
            case "a": idx = 0
            case "b": idx = 1
            default:  idx = 2
            }
            window[idx] += 1
            while window[0] > limit[0] || window[1] > limit[1] || window[2] > limit[2] {
                let lIdx: Int
                switch chars[left] {
                case "a": lIdx = 0
                case "b": lIdx = 1
                default:  lIdx = 2
                }
                window[lIdx] -= 1
                left += 1
            }
            let curLen = right - left + 1
            if curLen > maxLen { maxLen = curLen }
        }
        return n - maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun takeCharacters(s: String, k: Int): Int {
        val n = s.length
        val total = IntArray(3)
        for (ch in s) {
            when (ch) {
                'a' -> total[0]++
                'b' -> total[1]++
                else -> total[2]++
            }
        }
        for (cnt in total) {
            if (cnt < k) return -1
        }
        val allowed = IntArray(3) { total[it] - k }

        var left = 0
        var maxLen = 0
        val cur = IntArray(3)

        for (right in 0 until n) {
            when (s[right]) {
                'a' -> cur[0]++
                'b' -> cur[1]++
                else -> cur[2]++
            }
            while (cur[0] > allowed[0] || cur[1] > allowed[1] || cur[2] > allowed[2]) {
                when (s[left]) {
                    'a' -> cur[0]--
                    'b' -> cur[1]--
                    else -> cur[2]--
                }
                left++
            }
            val len = right - left + 1
            if (len > maxLen) maxLen = len
        }

        return n - maxLen
    }
}
```

## Dart

```dart
class Solution {
  int takeCharacters(String s, int k) {
    int n = s.length;
    if (k == 0) return 0;

    List<int> total = [0, 0, 0];
    for (int i = 0; i < n; i++) {
      int idx = s.codeUnitAt(i) - 97; // 'a' -> 0, 'b' -> 1, 'c' -> 2
      total[idx]++;
    }

    for (int cnt in total) {
      if (cnt < k) return -1;
    }

    List<int> window = [0, 0, 0];
    int left = 0;
    int maxLen = 0;

    for (int right = 0; right < n; right++) {
      int idx = s.codeUnitAt(right) - 97;
      window[idx]++;

      while (total[0] - window[0] < k ||
          total[1] - window[1] < k ||
          total[2] - window[2] < k) {
        int leftIdx = s.codeUnitAt(left) - 97;
        window[leftIdx]--;
        left++;
      }

      int curLen = right - left + 1;
      if (curLen > maxLen) maxLen = curLen;
    }

    return n - maxLen;
  }
}
```

## Golang

```go
func takeCharacters(s string, k int) int {
    n := len(s)
    var total [3]int
    for _, ch := range s {
        switch ch {
        case 'a':
            total[0]++
        case 'b':
            total[1]++
        case 'c':
            total[2]++
        }
    }
    for i := 0; i < 3; i++ {
        if total[i] < k {
            return -1
        }
    }

    limit := [3]int{total[0] - k, total[1] - k, total[2] - k}
    var window [3]int
    left, maxLen := 0, 0

    for right := 0; right < n; right++ {
        switch s[right] {
        case 'a':
            window[0]++
        case 'b':
            window[1]++
        case 'c':
            window[2]++
        }

        for window[0] > limit[0] || window[1] > limit[1] || window[2] > limit[2] {
            switch s[left] {
            case 'a':
                window[0]--
            case 'b':
                window[1]--
            case 'c':
                window[2]--
            }
            left++
        }

        curLen := right - left + 1
        if curLen > maxLen {
            maxLen = curLen
        }
    }

    return n - maxLen
}
```

## Ruby

```ruby
def take_characters(s, k)
  n = s.length
  return 0 if k == 0

  total = [0, 0, 0]
  s.each_byte do |b|
    case b
    when 97 # 'a'
      total[0] += 1
    when 98 # 'b'
      total[1] += 1
    else     # 'c'
      total[2] += 1
    end
  end

  return -1 if total.any? { |cnt| cnt < k }

  left = 0
  max_len = 0
  window = [0, 0, 0]
  bytes = s.bytes

  (0...n).each do |right|
    case bytes[right]
    when 97
      window[0] += 1
    when 98
      window[1] += 1
    else
      window[2] += 1
    end

    while left <= right && (total[0] - window[0] < k ||
                            total[1] - window[1] < k ||
                            total[2] - window[2] < k)
      case bytes[left]
      when 97
        window[0] -= 1
      when 98
        window[1] -= 1
      else
        window[2] -= 1
      end
      left += 1
    end

    cur_len = right - left + 1
    max_len = cur_len if cur_len > max_len
  end

  n - max_len
end
```

## Scala

```scala
object Solution {
    def takeCharacters(s: String, k: Int): Int = {
        if (k == 0) return 0
        val n = s.length
        val total = new Array[Int](3)
        def idx(ch: Char): Int = ch - 'a'
        var i = 0
        while (i < n) {
            total(idx(s.charAt(i))) += 1
            i += 1
        }
        if (total(0) < k || total(1) < k || total(2) < k) return -1

        val window = new Array[Int](3)
        var left = 0
        var maxWindow = 0
        var right = 0
        while (right < n) {
            val rIdx = idx(s.charAt(right))
            window(rIdx) += 1
            while (total(0) - window(0) < k || total(1) - window(1) < k || total(2) - window(2) < k) {
                val lIdx = idx(s.charAt(left))
                window(lIdx) -= 1
                left += 1
            }
            val curLen = right - left + 1
            if (curLen > maxWindow) maxWindow = curLen
            right += 1
        }
        n - maxWindow
    }
}
```

## Rust

```rust
impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;

        // total counts of each character
        let mut total = [0usize; 3];
        for &c in bytes {
            match c {
                b'a' => total[0] += 1,
                b'b' => total[1] += 1,
                b'c' => total[2] += 1,
                _ => {}
            }
        }

        // if any character appears fewer than k times, impossible
        if total.iter().any(|&cnt| cnt < k_usize) {
            return -1;
        }

        // maximum allowed count of each character inside the kept window
        let mut allowed = [0usize; 3];
        for i in 0..3 {
            allowed[i] = total[i] - k_usize;
        }

        let mut window = [0usize; 3];
        let mut left = 0usize;
        let mut max_len = 0usize;

        for right in 0..n {
            match bytes[right] {
                b'a' => window[0] += 1,
                b'b' => window[1] += 1,
                b'c' => window[2] += 1,
                _ => {}
            }

            // shrink from left while any character exceeds its allowed count
            loop {
                let mut need_shrink = false;
                for i in 0..3 {
                    if window[i] > allowed[i] {
                        need_shrink = true;
                        break;
                    }
                }
                if !need_shrink {
                    break;
                }
                match bytes[left] {
                    b'a' => window[0] -= 1,
                    b'b' => window[1] -= 1,
                    b'c' => window[2] -= 1,
                    _ => {}
                }
                left += 1;
            }

            let cur_len = right - left + 1;
            if cur_len > max_len {
                max_len = cur_len;
            }
        }

        (n - max_len) as i32
    }
}
```

## Racket

```racket
(define (char-index ch)
  (cond [(char=? ch #\a) 0]
        [(char=? ch #\b) 1]
        [else 2]))

(define/contract (take-characters s k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length s)])
    (if (= k 0)
        0
        (let ([total (make-vector 3 0)])
          ;; count total occurrences
          (for ([i (in-range n)])
            (let ([idx (char-index (string-ref s i))])
              (vector-set! total idx (+ (vector-ref total idx) 1))))
          (if (or (< (vector-ref total 0) k)
                  (< (vector-ref total 1) k)
                  (< (vector-ref total 2) k))
              -1
              (let ([window (make-vector 3 0)]
                    [left (box 0)]
                    [max-window (box 0)])
                (for ([right (in-range n)])
                  (let* ([idx (char-index (string-ref s right))])
                    (vector-set! window idx (+ (vector-ref window idx) 1))
                    ;; shrink while condition violated
                    (let loop ()
                      (unless (and (>= (- (vector-ref total 0) (vector-ref window 0)) k)
                                   (>= (- (vector-ref total 1) (vector-ref window 1)) k)
                                   (>= (- (vector-ref total 2) (vector-ref window 2)) k))
                        (let* ([lidx (char-index (string-ref s (unbox left)))])
                          (vector-set! window lidx (- (vector-ref window lidx) 1))
                          (set-box! left (+ (unbox left) 1))
                          (loop))))
                    ;; update max-window
                    (let ([curr (+ 1 (- right (unbox left)))])
                      (when (> curr (unbox max-window))
                        (set-box! max-window curr)))))
                (- n (unbox max-window)))))))))
```

## Erlang

```erlang
-spec take_characters(S :: unicode:unicode_binary(), K :: integer()) -> integer().
take_characters(S, K) ->
    N = byte_size(S),
    case K of
        0 -> 0;
        _ ->
            {TotalA, TotalB, TotalC} = count_total(S, 0, 0, 0),
            if TotalA < K orelse TotalB < K orelse TotalC < K ->
                    -1;
               true ->
                    LimitA = TotalA - K,
                    LimitB = TotalB - K,
                    LimitC = TotalC - K,
                    MaxLen = slide(S, N, 0, 0, 0, 0, 0, LimitA, LimitB, LimitC, 0),
                    N - MaxLen
            end
    end.

%% Count total occurrences of 'a', 'b', 'c' in the binary string.
-spec count_total(binary(), integer(), integer(), integer()) -> {integer(), integer(), integer()}.
count_total(<<>>, A, B, C) ->
    {A, B, C};
count_total(<<$a, Rest/binary>>, A, B, C) ->
    count_total(Rest, A + 1, B, C);
count_total(<<$b, Rest/binary>>, A, B, C) ->
    count_total(Rest, A, B + 1, C);
count_total(<<$c, Rest/binary>>, A, B, C) ->
    count_total(Rest, A, B, C + 1).

%% Sliding window to find the longest substring whose character counts do not exceed limits.
-spec slide(binary(), integer(), integer(), integer(),
           integer(), integer(), integer(),
           integer(), integer(), integer(),
           integer()) -> integer().
slide(_Bin, N, _Left, Right, _WA, _WB, _WC,
      _LimA, _LimB, _LimC, MaxLen) when Right == N ->
    MaxLen;
slide(Bin, N, Left, Right, WA, WB, WC,
      LimA, LimB, LimC, MaxLen) ->
    Char = binary:at(Bin, Right),
    {NewWA, NewWB, NewWC} = add_char(Char, WA, WB, WC),
    {FinalLeft, FinalWA, FinalWB, FinalWC} =
        shrink(Bin, Left, NewWA, NewWB, NewWC, LimA, LimB, LimC),
    CurrLen = Right - FinalLeft + 1,
    UpdatedMax = if CurrLen > MaxLen -> CurrLen; true -> MaxLen end,
    slide(Bin, N, FinalLeft, Right + 1,
          FinalWA, FinalWB, FinalWC,
          LimA, LimB, LimC, UpdatedMax).

%% Add a character to window counts.
-spec add_char(integer(), integer(), integer(), integer()) ->
      {integer(), integer(), integer()}.
add_char($a, A, B, C) -> {A + 1, B, C};
add_char($b, A, B, C) -> {A, B + 1, C};
add_char($c, A, B, C) -> {A, B, C + 1}.

%% Remove a character from window counts.
-spec remove_char(integer(), integer(), integer(), integer()) ->
      {integer(), integer(), integer()}.
remove_char($a, A, B, C) -> {A - 1, B, C};
remove_char($b, A, B, C) -> {A, B - 1, C};
remove_char($c, A, B, C) -> {A, B, C - 1}.

%% Shrink window from the left while any count exceeds its limit.
-spec shrink(binary(), integer(),
            integer(), integer(), integer(),
            integer(), integer(), integer()) ->
      {integer(), integer(), integer(), integer()}.
shrink(_Bin, Left, WA, WB, WC, LimA, LimB, LimC) ->
    case (WA =< LimA) andalso (WB =< LimB) andalso (WC =< LimC) of
        true -> {Left, WA, WB, WC};
        false ->
            CharL = binary:at(_Bin, Left),
            {NewWA, NewWB, NewWC} = remove_char(CharL, WA, WB, WC),
            shrink(_Bin, Left + 1, NewWA, NewWB, NewWC, LimA, LimB, LimC)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec take_characters(s :: String.t(), k :: integer) :: integer
  def take_characters(s, k) do
    n = byte_size(s)

    {total_a, total_b, total_c} =
      Enum.reduce(0..(n - 1), {0, 0, 0}, fn i, {a, b, c} ->
        case :binary.at(s, i) do
          ?a -> {a + 1, b, c}
          ?b -> {a, b + 1, c}
          ?c -> {a, b, c + 1}
        end
      end)

    cond do
      k == 0 ->
        0

      total_a < k or total_b < k or total_c < k ->
        -1

      true ->
        max_window = slide(s, n, k, total_a, total_b, total_c, 0, 0, 0, 0, 0, 0)
        n - max_window
    end
  end

  # tail‑recursive sliding window
  defp slide(_s, _n, _k, _ta, _tb, _tc, right, _left, _wa, _wb, _wc, max_win) when right == _n do
    max_win
  end

  defp slide(s, n, k, ta, tb, tc, right, left, wa, wb, wc, max_win) do
    {wa1, wb1, wc1} =
      case :binary.at(s, right) do
        ?a -> {wa + 1, wb, wc}
        ?b -> {wa, wb + 1, wc}
        ?c -> {wa, wb, wc + 1}
      end

    {left2, wa2, wb2, wc2} = shrink(s, left, wa1, wb1, wc1, ta, tb, tc, k)

    cur_len = right - left2 + 1
    max_win2 = if cur_len > max_win, do: cur_len, else: max_win

    slide(s, n, k, ta, tb, tc, right + 1, left2, wa2, wb2, wc2, max_win2)
  end

  # shrink window from the left while condition not satisfied
  defp shrink(s, left, wa, wb, wc, ta, tb, tc, k) do
    if (ta - wa < k) or (tb - wb < k) or (tc - wc < k) do
      {wa1, wb1, wc1} =
        case :binary.at(s, left) do
          ?a -> {wa - 1, wb, wc}
          ?b -> {wa, wb - 1, wc}
          ?c -> {wa, wb, wc - 1}
        end

      shrink(s, left + 1, wa1, wb1, wc1, ta, tb, tc, k)
    else
      {left, wa, wb, wc}
    end
  end
end
```
