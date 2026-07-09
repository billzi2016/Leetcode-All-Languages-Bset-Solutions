# 3456. Find Special Substring of Length K

## Cpp

```cpp
class Solution {
public:
    bool hasSpecialSubstring(string s, int k) {
        int n = s.size();
        if (k == 0) return false;
        int cnt = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] == s[i-1]) {
                ++cnt;
            } else {
                cnt = 1;
            }
            if (cnt >= k) return true;
        }
        // check first character case when n==1 or run at start
        return k <= 1; // for single-character strings, k==1 is true otherwise false handled above
    }
};
```

## Java

```java
class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        if (k == 0) return true;
        int count = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1;
            }
            if (count >= k) return true;
        }
        // Check the case when k == 1 or the first character alone satisfies
        return k <= 1 && !s.isEmpty();
    }
}
```

## Python

```python
class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        cnt = 0
        prev = ''
        for ch in s:
            if ch == prev:
                cnt += 1
            else:
                cnt = 1
                prev = ch
            if cnt >= k:
                return True
        return False
```

## Python3

```python
class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        if k == 1:
            return True
        cnt = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1
                if cnt >= k:
                    return True
            else:
                cnt = 1
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool hasSpecialSubstring(char* s, int k) {
    if (!s || k <= 0) return false;
    if (k == 1) return true;          // any single character forms a valid substring
    int count = 1;
    for (int i = 1; s[i] != '\0'; ++i) {
        if (s[i] == s[i - 1]) {
            ++count;
            if (count >= k) return true;
        } else {
            count = 1;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasSpecialSubstring(string s, int k) {
        int count = 0;
        char prev = '\0';
        foreach (char c in s) {
            if (c == prev) {
                count++;
            } else {
                prev = c;
                count = 1;
            }
            if (count >= k) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasSpecialSubstring = function(s, k) {
    if (k === 1) return true;
    let count = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            count++;
            if (count >= k) return true;
        } else {
            count = 1;
        }
    }
    return false;
};
```

## Typescript

```typescript
function hasSpecialSubstring(s: string, k: number): boolean {
    if (k === 1) return true;
    let count = 1;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            count++;
            if (count >= k) return true;
        } else {
            count = 1;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function hasSpecialSubstring($s, $k) {
        if ($k <= 1) {
            return true;
        }
        $n = strlen($s);
        $cnt = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) {
                $cnt++;
                if ($cnt >= $k) {
                    return true;
                }
            } else {
                $cnt = 1;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func hasSpecialSubstring(_ s: String, _ k: Int) -> Bool {
        if k == 1 { return !s.isEmpty }
        let chars = Array(s)
        var count = 1
        for i in 1..<chars.count {
            if chars[i] == chars[i - 1] {
                count += 1
                if count >= k { return true }
            } else {
                count = 1
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasSpecialSubstring(s: String, k: Int): Boolean {
        if (k == 1) return true
        var count = 1
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1]) {
                count++
                if (count >= k) return true
            } else {
                count = 1
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool hasSpecialSubstring(String s, int k) {
    if (k == 1) return true;
    int count = 1;
    for (int i = 1; i < s.length; i++) {
      if (s[i] == s[i - 1]) {
        count++;
        if (count >= k) return true;
      } else {
        count = 1;
      }
    }
    return false;
  }
}
```

## Golang

```go
func hasSpecialSubstring(s string, k int) bool {
	if k > len(s) {
		return false
	}
	count := 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			count++
		} else {
			if count >= k {
				return true
			}
			count = 1
		}
	}
	return count >= k
}
```

## Ruby

```ruby
def has_special_substring(s, k)
  count = 1
  (1...s.length).each do |i|
    if s[i] == s[i - 1]
      count += 1
    else
      return true if count >= k
      count = 1
    end
  end
  count >= k
end
```

## Scala

```scala
object Solution {
    def hasSpecialSubstring(s: String, k: Int): Boolean = {
        if (k <= 1) return true
        var count = 1
        for (i <- 1 until s.length) {
            if (s(i) == s(i - 1)) {
                count += 1
                if (count >= k) return true
            } else {
                count = 1
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_special_substring(s: String, k: i32) -> bool {
        let k = k as usize;
        if k == 0 {
            return true;
        }
        let mut prev = 0u8;
        let mut cnt = 0usize;
        for &b in s.as_bytes() {
            if b == prev {
                cnt += 1;
            } else {
                prev = b;
                cnt = 1;
            }
            if cnt >= k {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (has-special-substring s k)
  (-> string? exact-integer? boolean?)
  (let ((n (string-length s)))
    (if (< n k)
        #f
        (let loop ((i 0) (cnt 1) (prev (string-ref s 0)))
          (cond
            [(>= cnt k) #t]
            [(= i (- n 1)) #f]
            [else
             (define next-char (string-ref s (+ i 1)))
             (if (char=? next-char prev)
                 (loop (+ i 1) (+ cnt 1) prev)
                 (loop (+ i 1) 1 next-char))])))))
```

## Erlang

```erlang
-spec has_special_substring(unicode:unicode_binary(), integer()) -> boolean().
has_special_substring(S, K) ->
    scan(binary_to_list(S), undefined, 0, K).

scan(_List, _Prev, RunLen, K) when RunLen >= K ->
    true;
scan([], _Prev, RunLen, K) ->
    RunLen >= K;
scan([H|T], Prev, RunLen, K) ->
    case Prev of
        undefined ->
            scan(T, H, 1, K);
        _ ->
            if
                H =:= Prev ->
                    scan(T, Prev, RunLen + 1, K);
                true ->
                    scan(T, H, 1, K)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_special_substring(s :: String.t(), k :: integer) :: boolean()
  def has_special_substring(s, k) do
    s
    |> String.to_charlist()
    |> check(k, 0, nil)
  end

  defp check([], _k, _cnt, _prev), do: false

  defp check([h | t], k, cnt, prev) do
    new_cnt = if h == prev, do: cnt + 1, else: 1

    if new_cnt >= k do
      true
    else
      check(t, k, new_cnt, h)
    end
  end
end
```
