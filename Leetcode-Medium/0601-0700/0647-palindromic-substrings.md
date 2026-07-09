# 0647. Palindromic Substrings

## Cpp

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            // odd length palindromes
            for (int l = i, r = i; l >= 0 && r < n && s[l] == s[r]; --l, ++r)
                ++ans;
            // even length palindromes
            for (int l = i, r = i + 1; l >= 0 && r < n && s[l] == s[r]; --l, ++r)
                ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;
        for (int center = 0; center < n; ++center) {
            // odd length palindromes
            count += expand(s, center, center);
            // even length palindromes
            count += expand(s, center, center + 1);
        }
        return count;
    }

    private int expand(String s, int left, int right) {
        int n = s.length();
        int cnt = 0;
        while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
            ++cnt;
            --left;
            ++right;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
```

## Python3

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)

            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
```

## C

```c
int countSubstrings(char* s) {
    int n = 0;
    while (s[n]) ++n;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        // odd length palindromes
        int l = i, r = i;
        while (l >= 0 && r < n && s[l] == s[r]) {
            ++count;
            --l;
            ++r;
        }
        // even length palindromes
        l = i; r = i + 1;
        while (l >= 0 && r < n && s[l] == s[r]) {
            ++count;
            --l;
            ++r;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountSubstrings(string s)
    {
        int n = s.Length;
        int count = 0;

        for (int center = 0; center < n; center++)
        {
            // odd length palindromes
            int left = center, right = center;
            while (left >= 0 && right < n && s[left] == s[right])
            {
                count++;
                left--;
                right++;
            }

            // even length palindromes
            left = center;
            right = center + 1;
            while (left >= 0 && right < n && s[left] == s[right])
            {
                count++;
                left--;
                right++;
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        // odd length palindromes centered at i
        let l = i, r = i;
        while (l >= 0 && r < n && s[l] === s[r]) {
            ++ans;
            --l;
            ++r;
        }
        // even length palindromes centered between i and i+1
        l = i; r = i + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            ++ans;
            --l;
            ++r;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countSubstrings(s: string): number {
    const n = s.length;
    let count = 0;
    for (let center = 0; center < 2 * n - 1; ++center) {
        let left = Math.floor(center / 2);
        let right = center % 2 === 0 ? left : left + 1;
        while (left >= 0 && right < n && s[left] === s[right]) {
            ++count;
            --left;
            ++right;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countSubstrings($s) {
        $n = strlen($s);
        $count = 0;
        for ($center = 0; $center < $n; $center++) {
            // odd length palindromes
            $left = $center;
            $right = $center;
            while ($left >= 0 && $right < $n && $s[$left] === $s[$right]) {
                $count++;
                $left--;
                $right++;
            }
            // even length palindromes
            $left = $center;
            $right = $center + 1;
            while ($left >= 0 && $right < $n && $s[$left] === $s[$right]) {
                $count++;
                $left--;
                $right++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var count = 0
        
        func expand(_ left: Int, _ right: Int) {
            var l = left
            var r = right
            while l >= 0 && r < n && chars[l] == chars[r] {
                count += 1
                l -= 1
                r += 1
            }
        }
        
        for i in 0..<n {
            expand(i, i)       // odd length palindromes
            expand(i, i + 1)   // even length palindromes
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String): Int {
        val n = s.length
        var count = 0
        for (center in 0 until n) {
            // odd length palindromes
            var left = center
            var right = center
            while (left >= 0 && right < n && s[left] == s[right]) {
                count++
                left--
                right++
            }
            // even length palindromes
            left = center
            right = center + 1
            while (left >= 0 && right < n && s[left] == s[right]) {
                count++
                left--
                right++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countSubstrings(String s) {
    int n = s.length;
    int count = 0;
    for (int center = 0; center < n; ++center) {
      // odd length palindromes
      int left = center, right = center;
      while (left >= 0 && right < n && s[left] == s[right]) {
        count++;
        left--;
        right++;
      }
      // even length palindromes
      left = center;
      right = center + 1;
      while (left >= 0 && right < n && s[left] == s[right]) {
        count++;
        left--;
        right++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countSubstrings(s string) int {
    n := len(s)
    count := 0
    for i := 0; i < n; i++ {
        // odd length palindromes centered at i
        l, r := i, i
        for l >= 0 && r < n && s[l] == s[r] {
            count++
            l--
            r++
        }
        // even length palindromes centered between i and i+1
        l, r = i, i+1
        for l >= 0 && r < n && s[l] == s[r] {
            count++
            l--
            r++
        }
    }
    return count
}
```

## Ruby

```ruby
def count_substrings(s)
  n = s.length
  count = 0
  (0...n).each do |center|
    # odd length palindromes
    l = center
    r = center
    while l >= 0 && r < n && s[l] == s[r]
      count += 1
      l -= 1
      r += 1
    end
    # even length palindromes
    l = center
    r = center + 1
    while l >= 0 && r < n && s[l] == s[r]
      count += 1
      l -= 1
      r += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
  def countSubstrings(s: String): Int = {
    val n = s.length
    var cnt = 0
    for (i <- 0 until n) {
      // odd length palindromes
      var l = i
      var r = i
      while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
        cnt += 1
        l -= 1
        r += 1
      }
      // even length palindromes
      l = i
      r = i + 1
      while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
        cnt += 1
        l -= 1
        r += 1
      }
    }
    cnt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut count: i32 = 0;
        for center in 0..n {
            // odd length palindromes
            let mut left: isize = center as isize;
            let mut right: isize = center as isize;
            while left >= 0 && (right as usize) < n && bytes[left as usize] == bytes[right as usize] {
                count += 1;
                left -= 1;
                right += 1;
            }
            // even length palindromes
            let mut left: isize = center as isize;
            let mut right: isize = center as isize + 1;
            while left >= 0 && (right as usize) < n && bytes[left as usize] == bytes[right as usize] {
                count += 1;
                left -= 1;
                right += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-substrings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (let* ((odd (let expand ((l i) (r i) (c 0))
                        (if (and (>= l 0) (< r n) (char=? (string-ref s l) (string-ref s r)))
                            (expand (- l 1) (+ r 1) (+ c 1))
                            c)))
                 (even (let expand ((l i) (r (+ i 1)) (c 0))
                         (if (and (>= l 0) (< r n) (char=? (string-ref s l) (string-ref s r)))
                             (expand (- l 1) (+ r 1) (+ c 1))
                             c))))
            (loop (+ i 1) (+ total odd even)))))))
```

## Erlang

```erlang
-module(solution).
-export([count_substrings/1]).

-spec count_substrings(S :: unicode:unicode_binary()) -> integer().
count_substrings(S) ->
    List = unicode:characters_to_list(S),
    N = length(List),
    T = list_to_tuple(List),
    count_centers(N, T, 0, 0).

count_centers(N, _T, I, Acc) when I >= N ->
    Acc;
count_centers(N, T, I, Acc) ->
    Odd = expand(I, I, T, N, 0),
    Even = expand(I, I + 1, T, N, 0),
    count_centers(N, T, I + 1, Acc + Odd + Even).

-spec expand(integer(), integer(), tuple(), integer(), integer()) -> integer().
expand(L, R, _T, N, Acc) when L < 0; R >= N ->
    Acc;
expand(L, R, T, N, Acc) ->
    CharL = element(L + 1, T),
    CharR = element(R + 1, T),
    if
        CharL =:= CharR ->
            expand(L - 1, R + 1, T, N, Acc + 1);
        true ->
            Acc
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t) :: integer
  def count_substrings(s) do
    chars = s |> String.to_charlist() |> List.to_tuple()
    n = tuple_size(chars)

    0..(n - 1)
    |> Enum.reduce(0, fn i, acc ->
      acc + expand(chars, i, i, n) + expand(chars, i, i + 1, n)
    end)
  end

  defp expand(_chars, left, right, n) when left < 0 or right >= n, do: 0

  defp expand(chars, left, right, n) do
    if :erlang.element(left + 1, chars) == :erlang.element(right + 1, chars) do
      1 + expand(chars, left - 1, right + 1, n)
    else
      0
    end
  end
end
```
