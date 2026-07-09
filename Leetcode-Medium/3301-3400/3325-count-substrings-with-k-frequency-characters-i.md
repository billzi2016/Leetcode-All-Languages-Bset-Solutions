# 3325. Count Substrings With K-Frequency Characters I

## Cpp

```cpp
class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        int n = s.size();
        long long ans = 0;
        vector<int> cnt(26, 0);
        int good = 0;               // number of characters with frequency >= k
        int right = 0;
        for (int left = 0; left < n; ++left) {
            while (right < n && good == 0) {
                int idx = s[right] - 'a';
                ++cnt[idx];
                if (cnt[idx] == k) ++good;
                ++right;
            }
            if (good > 0) {
                ans += n - (right - 1);
            } else {
                break; // no further substrings can satisfy the condition
            }
            int idxL = s[left] - 'a';
            if (cnt[idxL] == k) --good;
            --cnt[idxL];
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numberOfSubstrings(String s, int k) {
        int n = s.length();
        long ans = 0;
        int[] cnt = new int[26];
        int right = 0;

        for (int left = 0; left < n; ++left) {
            // Expand right until condition is satisfied or we reach the end
            while (right < n && !hasAtLeastK(cnt, k)) {
                int idx = s.charAt(right) - 'a';
                cnt[idx]++;
                right++;
            }
            if (!hasAtLeastK(cnt, k)) {
                // No further substrings can satisfy the condition
                break;
            }
            // Minimal satisfying window is [left, right-1]
            ans += n - (right - 1);

            // Move left forward: remove s[left] from counts
            int idxL = s.charAt(left) - 'a';
            cnt[idxL]--;
        }

        return (int) ans;
    }

    private boolean hasAtLeastK(int[] cnt, int k) {
        for (int c : cnt) {
            if (c >= k) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        freq = [0] * 26
        cnt_ge_k = 0
        right = 0
        ans = 0

        for left in range(n):
            while right < n and cnt_ge_k == 0:
                idx = ord(s[right]) - 97
                freq[idx] += 1
                if freq[idx] == k:
                    cnt_ge_k += 1
                right += 1

            if cnt_ge_k == 0:
                break  # no further substrings can satisfy the condition

            ans += n - (right - 1)

            idx_left = ord(s[left]) - 97
            if freq[idx_left] == k:
                cnt_ge_k -= 1
            freq[idx_left] -= 1

        return ans
```

## Python3

```python
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26
        right = 0
        cnt_ge_k = 0
        ans = 0

        for left in range(n):
            while right < n and cnt_ge_k == 0:
                idx = ord(s[right]) - 97
                freq[idx] += 1
                if freq[idx] == k:
                    cnt_ge_k += 1
                right += 1

            if cnt_ge_k == 0:
                break

            ans += n - (right - 1)

            idx_left = ord(s[left]) - 97
            if freq[idx_left] == k:
                cnt_ge_k -= 1
            freq[idx_left] -= 1

        return ans
```

## C

```c
#include <string.h>

int numberOfSubstrings(char* s, int k) {
    int n = (int)strlen(s);
    if (k == 0) return 0; // not needed per constraints
    long long ans = 0;
    int cnt[26] = {0};
    int left = 0, right = 0;
    int have = 0; // number of characters with count >= k

    for (left = 0; left < n; ++left) {
        while (right < n && have == 0) {
            int idx = s[right] - 'a';
            cnt[idx]++;
            if (cnt[idx] == k) have++;
            right++;
        }
        if (have == 0) break; // no further substrings can satisfy
        ans += (long long)(n - right + 1);

        int idxL = s[left] - 'a';
        if (cnt[idxL] == k) have--;
        cnt[idxL]--;
    }

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSubstrings(string s, int k) {
        int n = s.Length;
        long ans = 0;
        for (int left = 0; left < n; ++left) {
            int[] cnt = new int[26];
            int maxFreq = 0;
            for (int right = left; right < n; ++right) {
                int idx = s[right] - 'a';
                cnt[idx]++;
                if (cnt[idx] > maxFreq) maxFreq = cnt[idx];
                if (maxFreq >= k) {
                    ans += n - right;
                    break;
                }
            }
        }
        return (int)ans;
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
var numberOfSubstrings = function(s, k) {
    const n = s.length;
    if (k === 1) return n * (n + 1) / 2;

    const cnt = new Array(26).fill(0);
    let meet = 0; // number of characters whose count >= k
    let right = -1;
    let ans = 0;

    for (let left = 0; left < n; left++) {
        while (right + 1 < n && meet === 0) {
            right++;
            const idx = s.charCodeAt(right) - 97;
            cnt[idx]++;
            if (cnt[idx] === k) meet++;
        }

        if (meet > 0) {
            ans += n - right;
        } else {
            break; // no further substrings can satisfy the condition
        }

        const idxL = s.charCodeAt(left) - 97;
        if (cnt[idxL] === k) meet--;
        cnt[idxL]--;
    }

    return ans;
};
```

## Typescript

```typescript
function numberOfSubstrings(s: string, k: number): number {
    const n = s.length;
    const cnt = new Array(26).fill(0);
    let meet = 0; // number of characters whose count >= k
    let right = 0;
    let ans = 0;

    for (let left = 0; left < n; left++) {
        while (right < n && meet === 0) {
            const idx = s.charCodeAt(right) - 97;
            cnt[idx]++;
            if (cnt[idx] === k) meet++;
            right++;
        }
        if (meet === 0) break; // no further substrings can satisfy
        ans += n - (right - 1);
        const idxL = s.charCodeAt(left) - 97;
        if (cnt[idxL] === k) meet--;
        cnt[idxL]--;
    }

    return ans;
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
    function numberOfSubstrings($s, $k) {
        $n = strlen($s);
        $counts = array_fill(0, 26, 0);
        $good = 0;          // number of characters whose count >= k
        $right = 0;
        $ans = 0;

        for ($left = 0; $left < $n; $left++) {
            while ($right < $n && $good == 0) {
                $idx = ord($s[$right]) - 97;
                $counts[$idx]++;
                if ($counts[$idx] == $k) {
                    $good++;
                }
                $right++;
            }

            if ($good > 0) {
                // minimal right index that satisfies condition is $right-1
                $ans += $n - ($right - 1);
            } else {
                break; // no further substrings can satisfy the condition
            }

            // slide left boundary forward
            $idxL = ord($s[$left]) - 97;
            if ($counts[$idxL] == $k) {
                $good--;
            }
            $counts[$idxL]--;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String, _ k: Int) -> Int {
        let bytes = Array(s.utf8)
        var arr = [Int]()
        arr.reserveCapacity(bytes.count)
        for b in bytes {
            arr.append(Int(b - 97)) // 'a' ascii is 97
        }
        let n = arr.count
        if k == 1 { // all substrings are valid
            return n * (n + 1) / 2
        }
        var cnt = [Int](repeating: 0, count: 26)
        var right = 0
        var curMax = 0
        var ans = 0
        
        for left in 0..<n {
            if right < left { right = left }
            while right < n && curMax < k {
                let idx = arr[right]
                cnt[idx] += 1
                if cnt[idx] > curMax { curMax = cnt[idx] }
                right += 1
            }
            if curMax >= k {
                ans += n - right + 1
            } else {
                break
            }
            // remove left character before next iteration
            let idxL = arr[left]
            cnt[idxL] -= 1
            // recompute curMax if needed
            if cnt[idxL] + 1 == curMax {
                var m = 0
                for v in cnt where v > m {
                    m = v
                }
                curMax = m
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String, k: Int): Int {
        val n = s.length
        val freq = IntArray(26)
        var right = 0
        var maxFreq = 0
        var ans = 0L

        for (left in 0 until n) {
            while (right < n && maxFreq < k) {
                val idx = s[right] - 'a'
                freq[idx]++
                if (freq[idx] > maxFreq) maxFreq = freq[idx]
                right++
            }
            if (maxFreq >= k) {
                ans += (n - right + 1).toLong()
            }

            // shrink window from the left
            val idxL = s[left] - 'a'
            freq[idxL]--
            if (freq[idxL] + 1 == maxFreq) {
                var newMax = 0
                for (c in 0 until 26) {
                    if (freq[c] > newMax) newMax = freq[c]
                }
                maxFreq = newMax
            }
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSubstrings(String s, int k) {
    int n = s.length;
    if (k == 1) return n * (n + 1) ~/ 2;

    List<int> cnt = List.filled(26, 0);
    int good = 0; // number of characters with frequency >= k
    int right = 0;
    int ans = 0;

    for (int left = 0; left < n; ++left) {
      while (right < n && good == 0) {
        int idx = s.codeUnitAt(right) - 97;
        cnt[idx]++;
        if (cnt[idx] == k) good++;
        right++;
      }
      if (good == 0) break; // no further valid substrings

      ans += n - (right - 1);

      int leftIdx = s.codeUnitAt(left) - 97;
      if (cnt[leftIdx] == k) good--;
      cnt[leftIdx]--;
    }

    return ans;
  }
}
```

## Golang

```go
func numberOfSubstrings(s string, k int) int {
    n := len(s)
    if k == 1 {
        return n * (n + 1) / 2
    }
    var cnt [26]int
    right := 0
    ans := 0

    hasK := func() bool {
        for _, v := range cnt {
            if v >= k {
                return true
            }
        }
        return false
    }

    for left := 0; left < n; left++ {
        for right < n && !hasK() {
            idx := int(s[right] - 'a')
            cnt[idx]++
            right++
        }
        if hasK() {
            ans += n - right + 1
        } else {
            break
        }
        idxL := int(s[left] - 'a')
        cnt[idxL]--
    }
    return ans
}
```

## Ruby

```ruby
def number_of_substrings(s, k)
  n = s.length
  counts = Array.new(26, 0)
  right = 0
  maxfreq = 0
  ans = 0
  bytes = s.bytes

  (0...n).each do |left|
    while right < n && maxfreq < k
      idx = bytes[right] - 97
      counts[idx] += 1
      maxfreq = counts[idx] if counts[idx] > maxfreq
      right += 1
    end

    ans += n - (right - 1) if maxfreq >= k

    idx_left = bytes[left] - 97
    prev = counts[idx_left]
    counts[idx_left] -= 1
    maxfreq = counts.max if prev == maxfreq
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numberOfSubstrings(s: String, k: Int): Int = {
        val n = s.length
        if (k == 1) return n * (n + 1) / 2

        val cnt = new Array[Int](26)
        var right = 0
        var maxFreq = 0
        var ans = 0L

        for (left <- 0 until n) {
            while (right < n && maxFreq < k) {
                val idx = s.charAt(right) - 'a'
                cnt(idx) += 1
                if (cnt(idx) > maxFreq) maxFreq = cnt(idx)
                right += 1
            }
            if (maxFreq >= k) {
                ans += n - right + 1
            }

            val idxL = s.charAt(left) - 'a'
            cnt(idxL) -= 1
            if (cnt(idxL) + 1 == maxFreq) {
                var mf = 0
                var i = 0
                while (i < 26) {
                    if (cnt(i) > mf) mf = cnt(i)
                    i += 1
                }
                maxFreq = mf
            }
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_substrings(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;
        let mut ans: i32 = 0;

        for left in 0..n {
            let mut cnt = [0usize; 26];
            let mut max_freq = 0usize;
            for right in left..n {
                let idx = (bytes[right] - b'a') as usize;
                cnt[idx] += 1;
                if cnt[idx] > max_freq {
                    max_freq = cnt[idx];
                }
                if max_freq >= k_usize {
                    ans += (n - right) as i32;
                    break;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-substrings s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s)))
    (if (= k 1)
        (quotient (* n (+ n 1)) 2)
        (let loop-left ((left 0) (total 0))
          (if (>= left n)
              total
              (let ((freq (make-vector 26 0)))
                (let inner ((right left))
                  (if (>= right n)
                      (loop-left (+ left 1) total)
                      (let ((idx (- (char->integer (string-ref s right))
                                    (char->integer #\a))))
                        (vector-set! freq idx (+ (vector-ref freq idx) 1))
                        (if (>= (vector-ref freq idx) k)
                            (let ((add (- n right)))
                              (loop-left (+ left 1) (+ total add)))
                            (inner (+ right 1)))))))))))))
```

## Erlang

```erlang
-spec number_of_substrings(unicode:unicode_binary(), integer()) -> integer().
number_of_substrings(S, K) ->
    CharList = binary_to_list(S),
    N = length(CharList),
    case K of
        1 -> N * (N + 1) div 2;
        _ ->
            CharT = list_to_tuple(CharList),
            outer(0, N - 1, CharT, K, 0)
    end.

outer(L, MaxIdx, _CharT, _K, Acc) when L > MaxIdx -> Acc;
outer(L, MaxIdx, CharT, K, Acc) ->
    Counts0 = erlang:make_tuple(26, 0),
    {Add, _} = find_right(L, MaxIdx, CharT, K, Counts0),
    outer(L + 1, MaxIdx, CharT, K, Acc + Add).

find_right(R, MaxIdx, _CharT, _K, Counts) when R > MaxIdx -> {0, Counts};
find_right(R, MaxIdx, CharT, K, Counts) ->
    C = element(R + 1, CharT),
    Idx = C - $a + 1,
    Old = element(Idx, Counts),
    NewCnt = Old + 1,
    NewCounts = setelement(Idx, Counts, NewCnt),
    if
        NewCnt >= K ->
            Add = (MaxIdx + 1) - R,
            {Add, NewCounts};
        true ->
            find_right(R + 1, MaxIdx, CharT, K, NewCounts)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t(), k :: integer) :: integer
  def number_of_substrings(s, k) do
    n = String.length(s)
    # initialize counts array for 26 letters with default 0
    counts = :array.new(26, default: 0)

    {_, _, _, ans} =
      Enum.reduce(0..(n - 1), {-1, counts, 0, 0}, fn left, {right, cnts, ge_k, acc} ->
        # expand right until condition satisfied or end of string
        {right, cnts, ge_k} = expand(s, n, k, right, cnts, ge_k)

        # if condition holds, add number of valid substrings starting at left
        acc =
          if ge_k > 0 do
            acc + (n - right)
          else
            acc
          end

        # remove character at position left from the window
        {cnts, ge_k} = remove_char(s, left, k, cnts, ge_k)

        {right, cnts, ge_k, acc}
      end)

    ans
  end

  defp expand(_s, n, _k, right, cnts, ge_k) when ge_k > 0 or right + 1 >= n do
    {right, cnts, ge_k}
  end

  defp expand(s, n, k, right, cnts, ge_k) do
    new_right = right + 1
    idx = :binary.at(s, new_right) - ?a
    val = :array.get(idx, cnts)
    new_val = val + 1
    cnts = :array.set(idx, new_val, cnts)
    ge_k = if new_val == k, do: ge_k + 1, else: ge_k

    expand(s, n, k, new_right, cnts, ge_k)
  end

  defp remove_char(s, pos, k, cnts, ge_k) do
    idx = :binary.at(s, pos) - ?a
    val = :array.get(idx, cnts)
    new_val = val - 1
    cnts = :array.set(idx, new_val, cnts)
    ge_k = if val == k and new_val == k - 1, do: ge_k - 1, else: ge_k
    {cnts, ge_k}
  end
end
```
