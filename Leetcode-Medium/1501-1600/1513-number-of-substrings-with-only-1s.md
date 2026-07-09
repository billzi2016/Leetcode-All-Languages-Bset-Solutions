# 1513. Number of Substrings With Only 1s

## Cpp

```cpp
class Solution {
public:
    int numSub(string s) {
        const int MOD = 1000000007;
        long long ans = 0, cnt = 0;
        for (char c : s) {
            if (c == '1') {
                ++cnt;
            } else {
                if (cnt > 0) {
                    ans = (ans + cnt * (cnt + 1) / 2) % MOD;
                    cnt = 0;
                }
            }
        }
        if (cnt > 0) {
            ans = (ans + cnt * (cnt + 1) / 2) % MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numSub(String s) {
        long ans = 0;
        long cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                cnt++;
            } else {
                ans = (ans + cnt * (cnt + 1) / 2) % MOD;
                cnt = 0;
            }
        }
        ans = (ans + cnt * (cnt + 1) / 2) % MOD;
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        total = 0
        count = 0
        for ch in s:
            if ch == '1':
                count += 1
            else:
                if count:
                    total = (total + count * (count + 1) // 2) % MOD
                    count = 0
        if count:
            total = (total + count * (count + 1) // 2) % MOD
        return total
```

## Python3

```python
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        count = 0
        for ch in s:
            if ch == '1':
                count += 1
            else:
                if count:
                    total = (total + count * (count + 1) // 2) % MOD
                    count = 0
        if count:
            total = (total + count * (count + 1) // 2) % MOD
        return total
```

## C

```c
int numSub(char* s) {
    const int MOD = 1000000007;
    long long ans = 0, cnt = 0;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '1') {
            ++cnt;
        } else {
            ans = (ans + cnt * (cnt + 1) / 2) % MOD;
            cnt = 0;
        }
    }
    ans = (ans + cnt * (cnt + 1) / 2) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumSub(string s) {
        const long MOD = 1000000007L;
        long ans = 0, cnt = 0;
        foreach (char c in s) {
            if (c == '1') {
                cnt++;
            } else {
                if (cnt > 0) {
                    ans = (ans + cnt * (cnt + 1) / 2) % MOD;
                    cnt = 0;
                }
            }
        }
        if (cnt > 0) {
            ans = (ans + cnt * (cnt + 1) / 2) % MOD;
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
var numSub = function(s) {
    const MOD = 1000000007;
    let ans = 0;
    let cnt = 0;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '1') {
            cnt++;
        } else {
            if (cnt > 0) {
                ans = (ans + (cnt * (cnt + 1) / 2)) % MOD;
                cnt = 0;
            }
        }
    }
    if (cnt > 0) {
        ans = (ans + (cnt * (cnt + 1) / 2)) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function numSub(s: string): number {
    const MOD = 1_000_000_007;
    let ans = 0;
    let cnt = 0;
    for (const ch of s) {
        if (ch === '1') {
            cnt++;
        } else {
            if (cnt > 0) {
                ans = (ans + ((cnt * (cnt + 1)) >> 1) % MOD) % MOD;
                cnt = 0;
            }
        }
    }
    if (cnt > 0) {
        ans = (ans + ((cnt * (cnt + 1)) >> 1) % MOD) % MOD;
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
    function numSub($s) {
        $mod = 1000000007;
        $len = strlen($s);
        $count = 0;
        $ans = 0;
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '1') {
                $count++;
            } else {
                if ($count > 0) {
                    $add = intdiv($count * ($count + 1), 2);
                    $ans = ($ans + $add) % $mod;
                    $count = 0;
                }
            }
        }
        if ($count > 0) {
            $add = intdiv($count * ($count + 1), 2);
            $ans = ($ans + $add) % $mod;
        }
        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func numSub(_ s: String) -> Int {
        let MOD: Int64 = 1_000_000_007
        var total: Int64 = 0
        var current: Int64 = 0
        
        for ch in s {
            if ch == "1" {
                current += 1
            } else {
                if current > 0 {
                    total = (total + current * (current + 1) / 2) % MOD
                    current = 0
                }
            }
        }
        
        if current > 0 {
            total = (total + current * (current + 1) / 2) % MOD
        }
        
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSub(s: String): Int {
        val MOD = 1_000_000_007L
        var cur = 0L
        var ans = 0L
        for (ch in s) {
            if (ch == '1') {
                cur++
            } else {
                if (cur > 0) {
                    ans = (ans + cur * (cur + 1) / 2) % MOD
                    cur = 0L
                }
            }
        }
        if (cur > 0) {
            ans = (ans + cur * (cur + 1) / 2) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numSub(String s) {
    const int mod = 1000000007;
    int count = 0;
    int ans = 0;
    for (int i = 0; i < s.length; ++i) {
      if (s.codeUnitAt(i) == 49) { // '1'
        count++;
      } else {
        if (count > 0) {
          ans = (ans + (count * (count + 1) ~/ 2)) % mod;
          count = 0;
        }
      }
    }
    if (count > 0) {
      ans = (ans + (count * (count + 1) ~/ 2)) % mod;
    }
    return ans;
  }
}
```

## Golang

```go
func numSub(s string) int {
	const mod int64 = 1000000007
	var ans, cnt int64
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			cnt++
		} else {
			ans = (ans + cnt*(cnt+1)/2) % mod
			cnt = 0
		}
	}
	ans = (ans + cnt*(cnt+1)/2) % mod
	return int(ans)
}
```

## Ruby

```ruby
def num_sub(s)
  mod = 1_000_000_007
  ans = 0
  cnt = 0
  s.each_char do |ch|
    if ch == '1'
      cnt += 1
    else
      if cnt > 0
        ans = (ans + cnt * (cnt + 1) / 2) % mod
        cnt = 0
      end
    end
  end
  ans = (ans + cnt * (cnt + 1) / 2) % mod if cnt > 0
  ans
end
```

## Scala

```scala
object Solution {
    def numSub(s: String): Int = {
        val MOD = 1000000007L
        var ans = 0L
        var cnt = 0L
        for (ch <- s) {
            if (ch == '1') {
                cnt += 1
            } else {
                if (cnt > 0) {
                    ans = (ans + cnt * (cnt + 1) / 2) % MOD
                    cnt = 0
                }
            }
        }
        if (cnt > 0) {
            ans = (ans + cnt * (cnt + 1) / 2) % MOD
        }
        (ans % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cur: i64 = 0;
        let mut ans: i64 = 0;
        for &b in s.as_bytes() {
            if b == b'1' {
                cur += 1;
            } else {
                ans = (ans + cur * (cur + 1) / 2) % MOD;
                cur = 0;
            }
        }
        ans = (ans + cur * (cur + 1) / 2) % MOD;
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-sub s)
  (-> string? exact-integer?)
  (let ((len (string-length s)))
    (let loop ((i 0) (run 0) (ans 0))
      (if (= i len)
          (modulo (+ ans (if (> run 0) (/ (* run (+ run 1)) 2) 0)) MOD)
          (let ((ch (string-ref s i)))
            (if (char=? ch #\1)
                (loop (+ i 1) (+ run 1) ans)
                (let* ((add (if (> run 0) (/ (* run (+ run 1)) 2) 0))
                       (new-ans (modulo (+ ans add) MOD)))
                  (loop (+ i 1) 0 new-ans))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_sub/1]).

-spec num_sub(S :: unicode:unicode_binary()) -> integer().
num_sub(S) ->
    Mod = 1000000007,
    process(S, 0, 0, Mod).

process(<<>>, RunLen, Acc, Mod) ->
    (Acc + contribution(RunLen)) rem Mod;
process(<<$1, Rest/binary>>, RunLen, Acc, Mod) ->
    process(Rest, RunLen + 1, Acc, Mod);
process(<<$0, Rest/binary>>, RunLen, Acc, Mod) ->
    NewAcc = (Acc + contribution(RunLen)) rem Mod,
    process(Rest, 0, NewAcc, Mod).

contribution(N) when N > 0 ->
    (N * (N + 1)) div 2;
contribution(0) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    mod = 1_000_000_007

    {sum, cnt} =
      s
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn ch, {acc, cur} ->
        if ch == "1" do
          {acc, cur + 1}
        else
          added = div(cur * (cur + 1), 2)
          {(acc + added) |> rem(mod), 0}
        end
      end)

    final_sum =
      if cnt > 0 do
        added = div(cnt * (cnt + 1), 2)
        (sum + added) |> rem(mod)
      else
        sum
      end

    final_sum
  end
end
```
