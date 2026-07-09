# 1234. Replace the Substring for Balanced String

## Cpp

```cpp
class Solution {
public:
    int balancedString(string s) {
        int n = s.size();
        int target = n / 4;
        array<int, 4> cnt{};
        for (char c : s) {
            if (c == 'Q') cnt[0]++;
            else if (c == 'W') cnt[1]++;
            else if (c == 'E') cnt[2]++;
            else cnt[3]++; // 'R'
        }
        auto enough = [&](const array<int,4>& a)->bool{
            return a[0] <= target && a[1] <= target && a[2] <= target && a[3] <= target;
        };
        if (enough(cnt)) return 0;
        int left = 0, ans = n;
        for (int right = 0; right < n; ++right) {
            // remove s[right] from consideration
            if (s[right] == 'Q') cnt[0]--;
            else if (s[right] == 'W') cnt[1]--;
            else if (s[right] == 'E') cnt[2]--;
            else cnt[3]--;
            while (left <= right && enough(cnt)) {
                ans = min(ans, right - left + 1);
                // add back s[left] as we move left forward
                if (s[left] == 'Q') cnt[0]++;
                else if (s[left] == 'W') cnt[1]++;
                else if (s[left] == 'E') cnt[2]++;
                else cnt[3]++;
                ++left;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int idx(char c) {
        if (c == 'Q') return 0;
        if (c == 'W') return 1;
        if (c == 'E') return 2;
        return 3; // 'R'
    }

    public int balancedString(String s) {
        int n = s.length();
        int target = n / 4;
        int[] cnt = new int[4];
        char[] arr = s.toCharArray();

        for (char c : arr) {
            cnt[idx(c)]++;
        }

        boolean alreadyBalanced = true;
        for (int v : cnt) {
            if (v != target) {
                alreadyBalanced = false;
                break;
            }
        }
        if (alreadyBalanced) return 0;

        int minLen = n;
        int left = 0;

        for (int right = 0; right < n; right++) {
            cnt[idx(arr[right])]--;

            while (left <= right &&
                   cnt[0] <= target && cnt[1] <= target &&
                   cnt[2] <= target && cnt[3] <= target) {
                minLen = Math.min(minLen, right - left + 1);
                cnt[idx(arr[left])]++; // move left out of window
                left++;
            }
        }

        return minLen;
    }
}
```

## Python

```python
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        n = len(s)
        target = n // 4
        cnt = Counter(s)

        # If already balanced
        if all(cnt[ch] <= target for ch in "QWER"):
            return 0

        left = 0
        min_len = n
        for right, ch in enumerate(s):
            cnt[ch] -= 1  # include s[right] into the window (remove from outside)

            # Try to shrink the window while the remaining string is balanced
            while left <= right and all(cnt[c] <= target for c in "QWER"):
                min_len = min(min_len, right - left + 1)
                cnt[s[left]] += 1  # move left out of window (add back to outside)
                left += 1

        return min_len
```

## Python3

```python
class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter
        n = len(s)
        target = n // 4
        cnt = Counter(s)
        if all(v <= target for v in cnt.values()):
            return 0
        left = 0
        ans = n
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while left <= right and all(cnt[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans
```

## C

```c
#include <string.h>

int balancedString(char* s) {
    int n = strlen(s);
    int target = n / 4;
    int total[4] = {0}; // Q, W, E, R

    for (int i = 0; i < n; ++i) {
        char c = s[i];
        if (c == 'Q') total[0]++;
        else if (c == 'W') total[1]++;
        else if (c == 'E') total[2]++;
        else if (c == 'R') total[3]++;
    }

    int already = 1;
    for (int i = 0; i < 4; ++i) {
        if (total[i] != target) { already = 0; break; }
    }
    if (already) return 0;

    int win[4] = {0};
    int left = 0;
    int min_len = n;

    for (int right = 0; right < n; ++right) {
        char c = s[right];
        if (c == 'Q') win[0]++;
        else if (c == 'W') win[1]++;
        else if (c == 'E') win[2]++;
        else if (c == 'R') win[3]++;

        while (left <= right) {
            int ok = 1;
            for (int i = 0; i < 4; ++i) {
                if (total[i] - win[i] > target) { ok = 0; break; }
            }
            if (!ok) break;

            int cur_len = right - left + 1;
            if (cur_len < min_len) min_len = cur_len;

            char cl = s[left];
            if (cl == 'Q') win[0]--;
            else if (cl == 'W') win[1]--;
            else if (cl == 'E') win[2]--;
            else if (cl == 'R') win[3]--;
            ++left;
        }
    }

    return min_len;
}
```

## Csharp

```csharp
public class Solution
{
    public int BalancedString(string s)
    {
        int n = s.Length;
        int target = n / 4;
        int[] total = new int[4];
        foreach (char c in s)
        {
            total[Idx(c)]++;
        }

        bool alreadyBalanced = true;
        for (int i = 0; i < 4; i++)
        {
            if (total[i] > target)
            {
                alreadyBalanced = false;
                break;
            }
        }
        if (alreadyBalanced) return 0;

        int[] window = new int[4];
        int left = 0;
        int minLen = n;

        for (int right = 0; right < n; right++)
        {
            window[Idx(s[right])]++;

            while (left <= right && IsValid(total, window, target))
            {
                minLen = Math.Min(minLen, right - left + 1);
                window[Idx(s[left])]--;
                left++;
            }
        }

        return minLen;
    }

    private static bool IsValid(int[] total, int[] window, int target)
    {
        for (int i = 0; i < 4; i++)
        {
            if (total[i] - window[i] > target) return false;
        }
        return true;
    }

    private static int Idx(char c)
    {
        // Map 'Q','W','E','R' to 0..3
        switch (c)
        {
            case 'Q': return 0;
            case 'W': return 1;
            case 'E': return 2;
            case 'R': return 3;
            default: return -1;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var balancedString = function(s) {
    const n = s.length;
    const target = n / 4;
    const total = {Q:0, W:0, E:0, R:0};
    for (const ch of s) total[ch]++;

    const need = {
        Q: Math.max(0, total.Q - target),
        W: Math.max(0, total.W - target),
        E: Math.max(0, total.E - target),
        R: Math.max(0, total.R - target)
    };
    
    if (need.Q === 0 && need.W === 0 && need.E === 0 && need.R === 0) return 0;
    
    const win = {Q:0, W:0, E:0, R:0};
    let left = 0;
    let minLen = n;
    
    const satisfies = () => (
        win.Q >= need.Q &&
        win.W >= need.W &&
        win.E >= need.E &&
        win.R >= need.R
    );
    
    for (let right = 0; right < n; ++right) {
        win[s[right]]++;
        while (satisfies()) {
            minLen = Math.min(minLen, right - left + 1);
            win[s[left]]--;
            left++;
        }
    }
    
    return minLen;
};
```

## Typescript

```typescript
function balancedString(s: string): number {
    const n = s.length;
    const target = n / 4;
    const idxMap: { [key: string]: number } = { Q: 0, W: 1, E: 2, R: 3 };
    const total = [0, 0, 0, 0];
    for (const ch of s) {
        total[idxMap[ch]]++;
    }
    if (total.every(cnt => cnt <= target)) return 0;

    const outside = total.slice(); // counts of characters outside the current window
    let left = 0;
    let minLen = n;

    for (let right = 0; right < n; right++) {
        const rIdx = idxMap[s[right]];
        outside[rIdx]--;

        while (
            left <= right &&
            outside[0] <= target &&
            outside[1] <= target &&
            outside[2] <= target &&
            outside[3] <= target
        ) {
            minLen = Math.min(minLen, right - left + 1);
            const lIdx = idxMap[s[left]];
            outside[lIdx]++;
            left++;
        }
    }

    return minLen;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function balancedString($s) {
        $n = strlen($s);
        $target = intdiv($n, 4);
        $cnt = ['Q'=>0,'W'=>0,'E'=>0,'R'=>0];
        for ($i = 0; $i < $n; $i++) {
            $cnt[$s[$i]]++;
        }
        $need = [];
        foreach (['Q','W','E','R'] as $c) {
            $excess = $cnt[$c] - $target;
            $need[$c] = $excess > 0 ? $excess : 0;
        }
        if ($need['Q']==0 && $need['W']==0 && $need['E']==0 && $need['R']==0) {
            return 0;
        }
        $win = ['Q'=>0,'W'=>0,'E'=>0,'R'=>0];
        $left = 0;
        $minLen = $n;
        for ($right = 0; $right < $n; $right++) {
            $ch = $s[$right];
            $win[$ch]++;
            while ($this->covers($win, $need)) {
                $currLen = $right - $left + 1;
                if ($currLen < $minLen) {
                    $minLen = $currLen;
                }
                $win[$s[$left]]--;
                $left++;
            }
        }
        return $minLen;
    }

    private function covers($win, $need) {
        foreach (['Q','W','E','R'] as $c) {
            if ($win[$c] < $need[$c]) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func balancedString(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        let target = n / 4
        
        var total = [Int](repeating: 0, count: 4)
        for ch in chars {
            let i = idx(ch)
            if i >= 0 { total[i] += 1 }
        }
        
        var need = [Int](repeating: 0, count: 4)
        var required = 0
        for i in 0..<4 {
            let excess = total[i] - target
            if excess > 0 {
                need[i] = excess
                required += excess
            }
        }
        if required == 0 { return 0 }
        
        var left = 0
        var minLen = n
        var window = [Int](repeating: 0, count: 4)
        
        for right in 0..<n {
            let rIdx = idx(chars[right])
            window[rIdx] += 1
            
            while left <= right && isValid(window, need) {
                minLen = min(minLen, right - left + 1)
                let lIdx = idx(chars[left])
                window[lIdx] -= 1
                left += 1
            }
        }
        return minLen
    }
    
    private func idx(_ ch: Character) -> Int {
        switch ch {
        case "Q": return 0
        case "W": return 1
        case "E": return 2
        case "R": return 3
        default: return -1
        }
    }
    
    private func isValid(_ window: [Int], _ need: [Int]) -> Bool {
        for i in 0..<4 {
            if window[i] < need[i] { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun balancedString(s: String): Int {
        val n = s.length
        val target = n / 4
        fun idx(c: Char): Int = when (c) {
            'Q' -> 0
            'W' -> 1
            'E' -> 2
            else -> 3 // 'R'
        }
        val total = IntArray(4)
        for (ch in s) {
            total[idx(ch)]++
        }
        val need = IntArray(4)
        var allZero = true
        for (i in 0..3) {
            need[i] = if (total[i] > target) total[i] - target else 0
            if (need[i] != 0) allZero = false
        }
        if (allZero) return 0

        val window = IntArray(4)
        var left = 0
        var ans = n
        fun satisfied(): Boolean {
            for (i in 0..3) {
                if (window[i] < need[i]) return false
            }
            return true
        }

        for (right in 0 until n) {
            val rIdx = idx(s[right])
            window[rIdx]++
            while (satisfied()) {
                ans = kotlin.math.min(ans, right - left + 1)
                val lIdx = idx(s[left])
                window[lIdx]--
                left++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int balancedString(String s) {
    int n = s.length;
    int target = n ~/ 4;
    Map<String, int> cnt = {'Q': 0, 'W': 0, 'E': 0, 'R': 0};

    for (int i = 0; i < n; i++) {
      String ch = s[i];
      cnt[ch] = cnt[ch]! + 1;
    }

    bool alreadyBalanced = true;
    for (var v in cnt.values) {
      if (v != target) {
        alreadyBalanced = false;
        break;
      }
    }
    if (alreadyBalanced) return 0;

    int left = 0;
    int minLen = n;
    List<String> chars = s.split('');

    for (int right = 0; right < n; right++) {
      String ch = chars[right];
      cnt[ch] = cnt[ch]! - 1;

      while (left <= right &&
          cnt['Q']! <= target &&
          cnt['W']! <= target &&
          cnt['E']! <= target &&
          cnt['R']! <= target) {
        int windowLen = right - left + 1;
        if (windowLen < minLen) minLen = windowLen;

        String lch = chars[left];
        cnt[lch] = cnt[lch]! + 1;
        left++;
      }
    }

    return minLen;
  }
}
```

## Golang

```go
func balancedString(s string) int {
	n := len(s)
	target := n / 4
	total := [4]int{}
	idx := func(b byte) int {
		switch b {
		case 'Q':
			return 0
		case 'W':
			return 1
		case 'E':
			return 2
		default: // 'R'
			return 3
		}
	}
	for i := 0; i < n; i++ {
		total[idx(s[i])]++
	}

	need := [4]int{}
	for i := 0; i < 4; i++ {
		if total[i] > target {
			need[i] = total[i] - target
		}
	}
	if need[0] == 0 && need[1] == 0 && need[2] == 0 && need[3] == 0 {
		return 0
	}

	minLen := n
	window := [4]int{}
	left := 0
	for right := 0; right < n; right++ {
		window[idx(s[right])]++
		for left <= right && satisfies(window, need) {
			cur := right - left + 1
			if cur < minLen {
				minLen = cur
			}
			window[idx(s[left])]--
			left++
		}
	}
	return minLen
}

func satisfies(win [4]int, need [4]int) bool {
	for i := 0; i < 4; i++ {
		if win[i] < need[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def balanced_string(s)
  n = s.length
  target = n / 4
  idx = { 'Q' => 0, 'W' => 1, 'E' => 2, 'R' => 3 }
  cnt = [0, 0, 0, 0]
  s.each_char { |c| cnt[idx[c]] += 1 }

  return 0 if cnt.all? { |v| v <= target }

  left = 0
  min_len = n
  chars = s.chars

  (0...n).each do |right|
    cnt[idx[chars[right]]] -= 1

    while left <= right && cnt.all? { |v| v <= target }
      cur_len = right - left + 1
      min_len = cur_len if cur_len < min_len
      cnt[idx[chars[left]]] += 1
      left += 1
    end
  end

  min_len
end
```

## Scala

```scala
object Solution {
  def balancedString(s: String): Int = {
    val n = s.length
    val need = n / 4
    val total = new Array[Int](4)
    for (c <- s) total(idx(c)) += 1

    var alreadyBalanced = true
    var i = 0
    while (i < 4) {
      if (total(i) > need) { alreadyBalanced = false; }
      i += 1
    }
    if (alreadyBalanced) return 0

    val window = new Array[Int](4)
    var left = 0
    var minLen = n
    for (right <- 0 until n) {
      window(idx(s.charAt(right))) += 1
      while (left <= right && isValid(total, window, need)) {
        val curLen = right - left + 1
        if (curLen < minLen) minLen = curLen
        window(idx(s.charAt(left))) -= 1
        left += 1
      }
    }
    minLen
  }

  private def idx(c: Char): Int = c match {
    case 'Q' => 0
    case 'W' => 1
    case 'E' => 2
    case 'R' => 3
  }

  private def isValid(total: Array[Int], window: Array[Int], need: Int): Boolean = {
    var i = 0
    while (i < 4) {
      if (total(i) - window(i) > need) return false
      i += 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn balanced_string(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let target = n / 4;
        // total counts
        let mut cnt = [0usize; 4];
        for &b in bytes {
            let idx = match b {
                b'Q' => 0,
                b'W' => 1,
                b'E' => 2,
                b'R' => 3,
                _ => unreachable!(),
            };
            cnt[idx] += 1;
        }
        if cnt.iter().all(|&c| c <= target) {
            return 0;
        }

        let mut cur = cnt.clone(); // counts outside current window
        let mut left = 0usize;
        let mut min_len = n;

        for right in 0..n {
            let idx_r = match bytes[right] {
                b'Q' => 0,
                b'W' => 1,
                b'E' => 2,
                b'R' => 3,
                _ => unreachable!(),
            };
            cur[idx_r] -= 1;

            while left <= right && cur.iter().all(|&c| c <= target) {
                let window_len = right - left + 1;
                if window_len < min_len {
                    min_len = window_len;
                }
                // shrink from left
                let idx_l = match bytes[left] {
                    b'Q' => 0,
                    b'W' => 1,
                    b'E' => 2,
                    b'R' => 3,
                    _ => unreachable!(),
                };
                cur[idx_l] += 1;
                left += 1;
            }
        }

        min_len as i32
    }
}
```

## Racket

```racket
(define/contract (balanced-string s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [target (/ n 4)]
         [char-index
          (lambda (ch)
            (cond [(char=? ch #\Q) 0]
                  [(char=? ch #\W) 1]
                  [(char=? ch #\E) 2]
                  [(char=? ch #\R) 3]))])
    (define total (make-vector 4 0))
    (for ([i (in-range n)])
      (let* ([ch (string-ref s i)]
             [idx (char-index ch)])
        (vector-set! total idx (+ (vector-ref total idx) 1))))
    (define need (make-vector 4 0))
    (for ([i (in-range 4)])
      (let* ([excess (- (vector-ref total i) target)])
        (when (> excess 0)
          (vector-set! need i excess))))
    (if (for/and ([i (in-range 4)]) (= (vector-ref need i) 0))
        0
        (let* ([window (make-vector 4 0)]
               [left 0]
               [min-len n])
          (define (enough?)
            (for/and ([i (in-range 4)])
              (>= (vector-ref window i) (vector-ref need i))))
          (for ([right (in-range n)])
            (let* ([ch (string-ref s right)]
                   [idx (char-index ch)])
              (vector-set! window idx (+ (vector-ref window idx) 1)))
            (let loop ()
              (when (enough?)
                (set! min-len (min min-len (- (+ right 1) left)))
                (let* ([ch-left (string-ref s left)]
                       [idx-left (char-index ch-left)])
                  (vector-set! window idx-left (- (vector-ref window idx-left) 1))
                  (set! left (+ left 1))
                  (loop)))))
          min-len))))
```

## Erlang

```erlang
-module(solution).
-export([balanced_string/1]).

-spec balanced_string(unicode:unicode_binary()) -> integer().
balanced_string(S) ->
    N = byte_size(S),
    Target = N div 4,
    Total = total_counts(S, N, {0,0,0,0}, 0),
    Need = need_tuple(Total, Target),
    case need_all_zero(Need) of
        true -> 0;
        false ->
            sliding_window(S, N, Need, {0,0,0,0}, 0, 0, N)
    end.

%% Count total frequencies in the whole string.
total_counts(_S, N, Counts, Index) when Index == N ->
    Counts;
total_counts(S, N, Counts, Index) ->
    Char = binary:at(S, Index),
    NewCounts = inc_counts(Counts, Char),
    total_counts(S, N, NewCounts, Index + 1).

%% Build need tuple: how many of each char must be removed (i.e., appear in the window).
need_tuple({Q,W,E,R}, Target) ->
    {max(Q - Target, 0), max(W - Target, 0), max(E - Target, 0), max(R - Target, 0)}.

need_all_zero({A,B,C,D}) ->
    A =:= 0 andalso B =:= 0 andalso C =:= 0 andalso D =:= 0.

%% Sliding window to find minimal length covering the need.
sliding_window(_S, N, _Need, _WinCounts, Left, Right, MinLen) when Right == N ->
    MinLen;
sliding_window(S, N, Need, WinCounts, Left, Right, MinLen) ->
    CharR = binary:at(S, Right),
    NewWin = inc_counts(WinCounts, CharR),
    {NewLeft, ShrunkWin, UpdatedMin} = shrink_left(S, Need, NewWin, Left, Right, MinLen),
    sliding_window(S, N, Need, ShrunkWin, NewLeft, Right + 1, UpdatedMin).

%% Move left pointer while window satisfies need.
shrink_left(_S, Need, WinCounts, Left, Right, MinLen) ->
    case window_satisfies(WinCounts, Need) of
        true ->
            CurrLen = Right - Left + 1,
            NewMin = if CurrLen < MinLen -> CurrLen; true -> MinLen end,
            CharL = binary:at(_S, Left),
            NewWin = dec_counts(WinCounts, CharL),
            shrink_left(_S, Need, NewWin, Left + 1, Right, NewMin);
        false ->
            {Left, WinCounts, MinLen}
    end.

%% Check if window counts meet or exceed need for all characters.
window_satisfies(Win, Need) ->
    element(1, Win) >= element(1, Need) andalso
    element(2, Win) >= element(2, Need) andalso
    element(3, Win) >= element(3, Need) andalso
    element(4, Win) >= element(4, Need).

%% Increment count for a character.
inc_counts(Counts, Char) ->
    Index = char_index(Char),
    Old = element(Index, Counts),
    setelement(Index, Counts, Old + 1).

%% Decrement count for a character.
dec_counts(Counts, Char) ->
    Index = char_index(Char),
    Old = element(Index, Counts),
    setelement(Index, Counts, Old - 1).

%% Map character to tuple position.
char_index($Q) -> 1;
char_index($W) -> 2;
char_index($E) -> 3;
char_index($R) -> 4.
```

## Elixir

```elixir
defmodule Solution do
  @spec balanced_string(s :: String.t()) :: integer
  def balanced_string(s) do
    n = byte_size(s)
    target = div(n, 4)

    init_counts = %{?Q => 0, ?W => 0, ?E => 0, ?R => 0}

    total =
      Enum.reduce(String.to_charlist(s), init_counts, fn c, acc ->
        Map.update!(acc, c, &(&1 + 1))
      end)

    excess = %{
      ?Q => max(0, total[?Q] - target),
      ?W => max(0, total[?W] - target),
      ?E => max(0, total[?E] - target),
      ?R => max(0, total[?R] - target)
    }

    if Enum.all?(excess, fn {_k, v} -> v == 0 end) do
      0
    else
      {_, _, ans} =
        Enum.reduce(0..(n - 1), {0, init_counts, n}, fn right, {left, window, min_len} ->
          c = :binary.at(s, right)
          window = Map.update!(window, c, &(&1 + 1))
          {new_left, new_window, new_min} = shrink(s, left, right, window, excess, min_len)
          {new_left, new_window, new_min}
        end)

      ans
    end
  end

  defp shrink(s, left, right, window, excess, min_len) do
    if satisfied?(window, excess) do
      cur_len = right - left + 1
      new_min = if cur_len < min_len, do: cur_len, else: min_len
      cl = :binary.at(s, left)
      new_window = Map.update!(window, cl, &(&1 - 1))
      shrink(s, left + 1, right, new_window, excess, new_min)
    else
      {left, window, min_len}
    end
  end

  defp satisfied?(window, excess) do
    Enum.all?([?Q, ?W, ?E, ?R], fn k -> window[k] >= excess[k] end)
  end
end
```
