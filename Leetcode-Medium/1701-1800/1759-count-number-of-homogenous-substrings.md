# 1759. Count Number of Homogenous Substrings

## Cpp

```cpp
class Solution {
public:
    int countHomogenous(string s) {
        const int MOD = 1000000007;
        long long ans = 0, streak = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (i > 0 && s[i] == s[i - 1]) {
                ++streak;
            } else {
                streak = 1;
            }
            ans += streak;
            if (ans >= MOD) ans %= MOD;
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int countHomogenous(String s) {
        long ans = 0;
        long cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {
                cur++;
            } else {
                cur = 1;
            }
            ans += cur;
            if (ans >= MOD) ans %= MOD;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        streak = 0
        prev = ''
        for ch in s:
            if ch == prev:
                streak += 1
            else:
                streak = 1
                prev = ch
            ans += streak
            if ans >= MOD:
                ans -= MOD
        return ans % MOD
```

## Python3

```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        streak = 0
        prev = ''
        for ch in s:
            if ch == prev:
                streak += 1
            else:
                streak = 1
                prev = ch
            ans = (ans + streak) % MOD
        return ans
```

## C

```c
int countHomogenous(char* s) {
    const int MOD = 1000000007;
    long long ans = 0, streak = 0;
    char prev = 0;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == prev) {
            ++streak;
        } else {
            streak = 1;
            prev = s[i];
        }
        ans += streak;
        if (ans >= MOD) ans %= MOD;
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    public int CountHomogenous(string s)
    {
        const int MOD = 1000000007;
        long ans = 0;
        int streak = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if (i > 0 && s[i] == s[i - 1])
                streak++;
            else
                streak = 1;

            ans += streak;
            if (ans >= MOD) ans -= MOD;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {
    const MOD = 1000000007;
    let ans = 0;
    let streak = 0;
    for (let i = 0; i < s.length; ++i) {
        if (i > 0 && s[i] === s[i - 1]) {
            streak += 1;
        } else {
            streak = 1;
        }
        ans += streak;
        if (ans >= MOD) ans %= MOD;
    }
    return ans % MOD;
};
```

## Typescript

```typescript
function countHomogenous(s: string): number {
    const MOD = 1_000_000_007;
    let ans = 0;
    let streak = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && s[i] === s[i - 1]) {
            streak++;
        } else {
            streak = 1;
        }
        ans = (ans + streak) % MOD;
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
    function countHomogenous($s) {
        $mod = 1000000007;
        $ans = 0;
        $curr = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $s[$i] === $s[$i - 1]) {
                $curr++;
            } else {
                $curr = 1;
            }
            $ans += $curr;
            if ($ans >= $mod) {
                $ans %= $mod;
            }
        }
        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countHomogenous(_ s: String) -> Int {
        let MOD = 1_000_000_007
        var ans: Int64 = 0
        var streak: Int64 = 0
        var prev: UInt8 = 0
        
        for ch in s.utf8 {
            if ch == prev {
                streak += 1
            } else {
                streak = 1
                prev = ch
            }
            ans += streak
        }
        
        return Int(ans % Int64(MOD))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countHomogenous(s: String): Int {
        val mod = 1_000_000_007L
        var ans = 0L
        var streak = 0L
        for (i in s.indices) {
            if (i > 0 && s[i] == s[i - 1]) {
                streak += 1
            } else {
                streak = 1
            }
            ans += streak
            if (ans >= mod) ans %= mod
        }
        return (ans % mod).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countHomogenous(String s) {
    const int MOD = 1000000007;
    int ans = 0;
    int streak = 0;
    for (int i = 0; i < s.length; ++i) {
      if (i > 0 && s[i] == s[i - 1]) {
        streak += 1;
      } else {
        streak = 1;
      }
      ans += streak;
      if (ans >= MOD) ans %= MOD;
    }
    return ans % MOD;
  }
}
```

## Golang

```go
func countHomogenous(s string) int {
	const MOD int64 = 1000000007
	var ans int64
	var streak int64
	var prev byte

	for i := 0; i < len(s); i++ {
		if i == 0 || s[i] == prev {
			streak++
		} else {
			streak = 1
		}
		ans += streak
		if ans >= MOD {
			ans %= MOD
		}
		prev = s[i]
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
def count_homogenous(s)
  mod = 1_000_000_007
  ans = 0
  streak = 0
  prev = nil

  s.each_char do |c|
    if c == prev
      streak += 1
    else
      streak = 1
      prev = c
    end
    ans = (ans + streak) % mod
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countHomogenous(s: String): Int = {
        val MOD = 1000000007L
        var ans = 0L
        var streak = 0L
        var prev: Char = 0.toChar
        for (c <- s) {
            if (c == prev) {
                streak += 1
            } else {
                streak = 1
                prev = c
            }
            ans = (ans + streak) % MOD
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let mut ans: i64 = 0;
        let mut streak: i64 = 0;
        for i in 0..bytes.len() {
            if i > 0 && bytes[i] == bytes[i - 1] {
                streak += 1;
            } else {
                streak = 1;
            }
            ans += streak;
            if ans >= MOD {
                ans %= MOD;
            }
        }
        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-homogenous s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (ans 0)
         (curr 0))
    (for ([i (in-range len)])
      (if (or (= i 0)
              (char=? (string-ref s i) (string-ref s (- i 1))))
          (set! curr (+ curr 1))
          (set! curr 1))
      (set! ans (modulo (+ ans curr) MOD)))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_homogenous/1]).

-define(MOD, 1000000007).

-spec count_homogenous(S :: unicode:unicode_binary()) -> integer().
count_homogenous(<<>>) ->
    0;
count_homogenous(<<First:8, Rest/binary>>) ->
    loop(Rest, First, 1, 1).

loop(<<>>, _Prev, _Streak, Acc) ->
    Acc rem ?MOD;
loop(<<C:8, Rest/binary>>, Prev, Streak, Acc) ->
    NewStreak = if C == Prev -> Streak + 1; true -> 1 end,
    NewAcc = (Acc + NewStreak) rem ?MOD,
    loop(Rest, C, NewStreak, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_homogenous(s :: String.t()) :: integer()
  def count_homogeneous(s) do
    mod = 1_000_000_007

    {ans, _streak, _prev} =
      s
      |> String.to_charlist()
      |> Enum.reduce({0, 0, nil}, fn ch, {acc, streak, prev} ->
        if prev == ch do
          new_streak = streak + 1
          {(acc + new_streak) rem mod, new_streak, ch}
        else
          new_streak = 1
          {(acc + new_streak) rem mod, new_streak, ch}
        end
      end)

    ans
  end
end
```
