# 3258. Count Substrings That Satisfy K-Constraint I

## Cpp

```cpp
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int cnt0 = 0, cnt1 = 0;
            for (int j = i; j < n; ++j) {
                if (s[j] == '0') ++cnt0;
                else ++cnt1;
                if (cnt0 > k && cnt1 > k) break;
                ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int zeros = 0, ones = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '0') {
                    zeros++;
                } else {
                    ones++;
                }
                if (zeros <= k || ones <= k) {
                    ans++;
                } else {
                    break;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            cnt0 = cnt1 = 0
            for j in range(i, n):
                if s[j] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
                if cnt0 <= k or cnt1 <= k:
                    ans += 1
                else:
                    break
        return ans
```

## Python3

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt0 = cnt1 = 0
            for j in range(i, n):
                if s[j] == '0':
                    cnt0 += 1
                else:
                    cnt1 += 1
                if cnt0 <= k or cnt1 <= k:
                    ans += 1
        return ans
```

## C

```c
#include <string.h>

int countKConstraintSubstrings(char* s, int k) {
    int n = strlen(s);
    int total = 0;
    for (int i = 0; i < n; ++i) {
        int cnt0 = 0, cnt1 = 0;
        for (int j = i; j < n; ++j) {
            if (s[j] == '0')
                ++cnt0;
            else
                ++cnt1;
            if (cnt0 <= k || cnt1 <= k)
                ++total;
            else
                break;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int CountKConstraintSubstrings(string s, int k) {
        int n = s.Length;
        int result = 0;
        for (int i = 0; i < n; i++) {
            int zeros = 0, ones = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '0') zeros++;
                else ones++;
                if (zeros <= k || ones <= k) result++;
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
 * @param {number} k
 * @return {number}
 */
var countKConstraintSubstrings = function(s, k) {
    const n = s.length;
    const total = n * (n + 1) / 2;
    let bad = 0;
    let zeroCnt = 0, oneCnt = 0;
    let r = 0;
    for (let l = 0; l < n; ++l) {
        while (r < n && (zeroCnt <= k || oneCnt <= k)) {
            if (s[r] === '0') zeroCnt++;
            else oneCnt++;
            r++;
        }
        if (zeroCnt > k && oneCnt > k) {
            bad += n - r + 1;
        }
        // move left pointer
        if (s[l] === '0') zeroCnt--;
        else oneCnt--;
    }
    return total - bad;
};
```

## Typescript

```typescript
function countKConstraintSubstrings(s: string, k: number): number {
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        let cnt0 = 0, cnt1 = 0;
        for (let j = i; j < n; ++j) {
            if (s[j] === '0') cnt0++;
            else cnt1++;
            if (cnt0 > k && cnt1 > k) break;
            ans++;
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
     * @param Integer $k
     * @return Integer
     */
    function countKConstraintSubstrings($s, $k) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            $cnt0 = 0;
            $cnt1 = 0;
            for ($j = $i; $j < $n; ++$j) {
                if ($s[$j] === '0') {
                    $cnt0++;
                } else {
                    $cnt1++;
                }
                if (min($cnt0, $cnt1) <= $k) {
                    $ans++;
                } else {
                    break;
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
    func countKConstraintSubstrings(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            var cnt0 = 0
            var cnt1 = 0
            for j in i..<n {
                if chars[j] == "0" {
                    cnt0 += 1
                } else {
                    cnt1 += 1
                }
                if cnt0 <= k || cnt1 <= k {
                    ans += 1
                } else {
                    break
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countKConstraintSubstrings(s: String, k: Int): Int {
        val n = s.length
        val prefZero = IntArray(n + 1)
        for (i in 0 until n) {
            prefZero[i + 1] = prefZero[i] + if (s[i] == '0') 1 else 0
        }
        var ans = 0
        for (l in 0 until n) {
            for (r in l + 1..n) {
                val zeros = prefZero[r] - prefZero[l]
                val len = r - l
                val ones = len - zeros
                if (zeros <= k || ones <= k) ans++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countKConstraintSubstrings(String s, int k) {
    int n = s.length;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int cnt0 = 0, cnt1 = 0;
      for (int j = i; j < n; j++) {
        if (s.codeUnitAt(j) == 48) {
          cnt0++;
        } else {
          cnt1++;
        }
        if (cnt0 <= k || cnt1 <= k) {
          ans++;
        } else {
          break;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countKConstraintSubstrings(s string, k int) int {
    n := len(s)
    ans := 0
    for i := 0; i < n; i++ {
        zeros, ones := 0, 0
        for j := i; j < n; j++ {
            if s[j] == '0' {
                zeros++
            } else {
                ones++
            }
            if zeros <= k || ones <= k {
                ans++
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_k_constraint_substrings(s, k)
  n = s.length
  ans = 0
  n.times do |i|
    zeros = 0
    ones = 0
    (i...n).each do |j|
      if s[j] == '0'
        zeros += 1
      else
        ones += 1
      end
      break if zeros > k && ones > k
      ans += 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countKConstraintSubstrings(s: String, k: Int): Int = {
        import scala.util.control.Breaks.{break, breakable}
        val n = s.length
        var ans = 0
        for (i <- 0 until n) {
            var zeros = 0
            var ones = 0
            breakable {
                for (j <- i until n) {
                    if (s.charAt(j) == '0') zeros += 1 else ones += 1
                    if (zeros <= k || ones <= k) ans += 1
                    else break
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans: i32 = 0;
        for i in 0..n {
            let mut cnt0 = 0;
            let mut cnt1 = 0;
            for j in i..n {
                if bytes[j] == b'0' {
                    cnt0 += 1;
                } else {
                    cnt1 += 1;
                }
                if cnt0 <= k as usize || cnt1 <= k as usize {
                    ans += 1;
                } else {
                    // both counts exceed k, further extension will also fail
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
(define/contract (count-k-constraint-substrings s k)
  (-> string? exact-integer? exact-integer?)
  (let ((n (string-length s)))
    (let loop-i ((i 0) (total 0))
      (if (= i n)
          total
          (let loop-j ((j i) (cnt0 0) (cnt1 0) (cur-total total))
            (if (= j n)
                (loop-i (+ i 1) cur-total)
                (let* ((ch (string-ref s j))
                       (new-cnt0 (if (char=? ch #\0) (+ cnt0 1) cnt0))
                       (new-cnt1 (if (char=? ch #\1) (+ cnt1 1) cnt1))
                       (new-total (if (or (<= new-cnt0 k) (<= new-cnt1 k))
                                      (+ cur-total 1)
                                      cur-total)))
                  (loop-j (+ j 1) new-cnt0 new-cnt1 new-total))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_k_constraint_substrings/2]).

-spec count_k_constraint_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
count_k_constraint_substrings(S, K) ->
    Len = byte_size(S),
    count_all(0, Len, S, K).

count_all(I, Len, _S, _K) when I >= Len -> 0;
count_all(I, Len, S, K) ->
    CountFromI = count_from(I, Len, S, K, 0, 0),
    CountFromI + count_all(I + 1, Len, S, K).

count_from(J, Len, _S, _K, _Z, _O) when J >= Len -> 0;
count_from(J, Len, S, K, Z, O) ->
    Char = binary:at(S, J),
    {NZ, NO} = case Char of
        $0 -> {Z + 1, O};
        $1 -> {Z, O + 1}
    end,
    if erlang:min(NZ, NO) =< K ->
            1 + count_from(J + 1, Len, S, K, NZ, NO);
       true ->
            0
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_k_constraint_substrings(s :: String.t(), k :: integer) :: integer
  def count_k_constraint_substrings(s, k) do
    chars = String.graphemes(s)
    n = length(chars)

    # prefix sum of zeros; pref[i] = number of '0' in s[0..i-1]
    pref =
      Enum.reduce(chars, [0], fn ch, acc ->
        zeros = hd(acc) + if ch == "0", do: 1, else: 0
        [zeros | acc]
      end)
      |> Enum.reverse()

    0..(n - 1)
    |> Enum.reduce(0, fn i, ans ->
      i..(n - 1)
      |> Enum.reduce(ans, fn j, acc ->
        zeros = Enum.at(pref, j + 1) - Enum.at(pref, i)
        len = j - i + 1
        ones = len - zeros

        if zeros <= k or ones <= k do
          acc + 1
        else
          acc
        end
      end)
    end)
  end
end
```
