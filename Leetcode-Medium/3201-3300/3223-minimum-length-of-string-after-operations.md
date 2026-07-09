# 3223. Minimum Length of String After Operations

## Cpp

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int cnt[26] = {0};
        for (char ch : s) cnt[ch - 'a']++;
        int ans = 0;
        for (int f : cnt) {
            if (f % 2 == 0) ans += min(f, 2);
            else ans += 1;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumLength(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        int result = 0;
        for (int f : freq) {
            if (f == 0) continue;
            result += (f & 1) == 0 ? 2 : 1;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = 0
        for cnt in freq:
            if cnt == 0:
                continue
            ans += 1 if cnt % 2 else 2
        return ans
```

## Python3

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = 0
        for f in cnt:
            if f == 0:
                continue
            if f <= 2:
                ans += f
            else:
                ans += 2 if f % 2 == 0 else 1
        return ans
```

## C

```c
#include <stddef.h>

int minimumLength(char* s) {
    int freq[26] = {0};
    for (char *p = s; *p != '\0'; ++p) {
        freq[*p - 'a']++;
    }
    int ans = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] == 0) continue;
        ans += (freq[i] % 2 == 1) ? 1 : 2;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumLength(string s) {
        int[] freq = new int[26];
        foreach (char ch in s) {
            freq[ch - 'a']++;
        }
        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) continue;
            result += (freq[i] & 1) == 1 ? 1 : 2;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    let result = 0;
    for (const cnt of freq) {
        if (cnt === 0) continue;
        result += (cnt % 2 === 0) ? 2 : 1;
    }
    return result;
};
```

## Typescript

```typescript
function minimumLength(s: string): number {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    let ans = 0;
    for (const f of freq) {
        if (f === 0) continue;
        ans += (f & 1) ? 1 : 2;
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
    function minimumLength($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97; // ord('a') == 97
            $freq[$idx]++;
        }
        $result = 0;
        foreach ($freq as $cnt) {
            if ($cnt === 0) continue;
            $result += ($cnt % 2 === 1) ? 1 : 2;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minimumLength(_ s: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte) - 97 // 'a' ASCII is 97
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        var result = 0
        for f in freq {
            if f == 0 { continue }
            if f % 2 == 0 {
                result += 2
            } else {
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
    fun minimumLength(s: String): Int {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var result = 0
        for (cnt in freq) {
            if (cnt > 0) {
                result += if (cnt % 2 == 0) 2 else 1
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int minimumLength(String s) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    int result = 0;
    for (int f in freq) {
      if (f == 0) continue;
      result += (f % 2 == 1) ? 1 : 2;
    }
    return result;
  }
}
```

## Golang

```go
func minimumLength(s string) int {
    var cnt [26]int
    for i := 0; i < len(s); i++ {
        cnt[s[i]-'a']++
    }
    res := 0
    for _, c := range cnt[:] {
        if c == 0 {
            continue
        }
        if c%2 == 1 {
            res += 1
        } else {
            // even count, at least 2 remain (or 0 if c==0 which is handled)
            res += 2
        }
    }
    return res
}
```

## Ruby

```ruby
def minimum_length(s)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  ans = 0
  freq.each do |c|
    next if c == 0
    ans += c.odd? ? 1 : 2
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumLength(s: String): Int = {
        val freq = new Array[Int](26)
        for (c <- s) {
            freq(c - 'a') += 1
        }
        var result = 0
        for (cnt <- freq) {
            if (cnt > 0) {
                result += (if ((cnt & 1) == 1) 1 else 2)
            }
        }
        result
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let mut freq = [0usize; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let mut ans = 0i32;
        for &f in freq.iter() {
            if f == 0 {
                continue;
            }
            if f % 2 == 1 {
                ans += 1;
            } else {
                ans += 2;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-length s)
  (-> string? exact-integer?)
  (let* ((freq (make-vector 26 0))
         (n (string-length s)))
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    (let loop ((i 0) (ans 0))
      (if (= i 26)
          ans
          (let* ((c (vector-ref freq i))
                 (add (cond [(< c 3) c]
                            [(even? c) 2]
                            [else 1])))
            (loop (+ i 1) (+ ans add)))))))
```

## Erlang

```erlang
-spec minimum_length(S :: unicode:unicode_binary()) -> integer().
minimum_length(S) ->
    FreqMap = count_freq(S, #{}),
    maps:fold(
        fun(_Char, Count, Acc) ->
            case Count rem 2 of
                0 -> Acc + 2;
                _ -> Acc + 1
            end
        end,
        0,
        FreqMap).

count_freq(<<>>, Map) -> Map;
count_freq(<<C, Rest/binary>>, Map) ->
    NewMap = maps:update_with(C, fun(N) -> N + 1 end, 1, Map),
    count_freq(Rest, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_length(s :: String.t()) :: integer()
  def minimum_length(s) do
    freq =
      :binary.bin_to_list(s)
      |> Enum.reduce(%{}, fn byte, acc ->
        idx = byte - ?a
        Map.update(acc, idx, 1, &(&1 + 1))
      end)

    Enum.reduce(freq, 0, fn {_idx, cnt}, sum ->
      if rem(cnt, 2) == 1 do
        sum + 1
      else
        sum + 2
      end
    end)
  end
end
```
