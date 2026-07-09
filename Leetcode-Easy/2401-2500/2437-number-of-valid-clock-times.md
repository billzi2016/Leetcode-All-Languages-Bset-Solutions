# 2437. Number of Valid Clock Times

## Cpp

```cpp
class Solution {
public:
    int countTime(string time) {
        int hourWays = 0, minuteWays = 0;
        for (int h = 0; h < 24; ++h) {
            char a = '0' + h / 10;
            char b = '0' + h % 10;
            if ((time[0] == '?' || time[0] == a) && (time[1] == '?' || time[1] == b))
                ++hourWays;
        }
        for (int m = 0; m < 60; ++m) {
            char c = '0' + m / 10;
            char d = '0' + m % 10;
            if ((time[3] == '?' || time[3] == c) && (time[4] == '?' || time[4] == d))
                ++minuteWays;
        }
        return hourWays * minuteWays;
    }
};
```

## Java

```java
class Solution {
    public int countTime(String time) {
        int ans = 0;
        for (int h = 0; h < 24; ++h) {
            String hh = String.format("%02d", h);
            if (!matches(time.charAt(0), hh.charAt(0)) || !matches(time.charAt(1), hh.charAt(1))) continue;
            for (int m = 0; m < 60; ++m) {
                String mm = String.format("%02d", m);
                if (matches(time.charAt(3), mm.charAt(0)) && matches(time.charAt(4), mm.charAt(1))) {
                    ans++;
                }
            }
        }
        return ans;
    }

    private boolean matches(char pattern, char digit) {
        return pattern == '?' || pattern == digit;
    }
}
```

## Python

```python
class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        cnt = 0
        for h in range(24):
            hs = f"{h:02d}"
            if (time[0] != '?' and time[0] != hs[0]) or (time[1] != '?' and time[1] != hs[1]):
                continue
            for m in range(60):
                ms = f"{m:02d}"
                if (time[3] != '?' and time[3] != ms[0]) or (time[4] != '?' and time[4] != ms[1]):
                    continue
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countTime(self, time: str) -> int:
        h1, h2 = time[0], time[1]
        m1, m2 = time[3], time[4]

        # hour possibilities
        if h1 == '?' and h2 == '?':
            hour_opts = 24
        elif h1 == '?':
            d2 = int(h2)
            if d2 <= 3:
                hour_opts = 3  # 0,1,2
            else:
                hour_opts = 2  # 0,1
        elif h2 == '?':
            d1 = int(h1)
            if d1 <= 1:
                hour_opts = 10
            elif d1 == 2:
                hour_opts = 4
            else:
                return 0
        else:
            hour = int(time[:2])
            hour_opts = 1 if 0 <= hour <= 23 else 0

        # minute possibilities
        if m1 == '?' and m2 == '?':
            minute_opts = 60
        elif m1 == '?':
            # any tens 0-5 works regardless of units digit
            minute_opts = 6
        elif m2 == '?':
            d1 = int(m1)
            if 0 <= d1 <= 5:
                minute_opts = 10
            else:
                return 0
        else:
            minute = int(time[3:])
            minute_opts = 1 if 0 <= minute <= 59 else 0

        return hour_opts * minute_opts
```

## C

```c
int countTime(char* time) {
    int ans = 0;
    for (int h = 0; h < 24; ++h) {
        char d0 = (char)(h / 10 + '0');
        char d1 = (char)(h % 10 + '0');
        if ((time[0] != '?' && time[0] != d0) ||
            (time[1] != '?' && time[1] != d1))
            continue;
        for (int m = 0; m < 60; ++m) {
            char d3 = (char)(m / 10 + '0');
            char d4 = (char)(m % 10 + '0');
            if ((time[3] != '?' && time[3] != d3) ||
                (time[4] != '?' && time[4] != d4))
                continue;
            ++ans;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountTime(string time)
    {
        int count = 0;
        for (int h = 0; h < 24; ++h)
        {
            string hs = h.ToString("D2");
            for (int m = 0; m < 60; ++m)
            {
                string ms = m.ToString("D2");
                string cur = hs + ":" + ms;
                bool ok = true;
                for (int i = 0; i < 5; ++i)
                {
                    if (time[i] != '?' && time[i] != cur[i])
                    {
                        ok = false;
                        break;
                    }
                }
                if (ok) count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} time
 * @return {number}
 */
var countTime = function(time) {
    let count = 0;
    for (let h = 0; h < 24; ++h) {
        const hs = h.toString().padStart(2, '0');
        for (let m = 0; m < 60; ++m) {
            const ms = m.toString().padStart(2, '0');
            const cur = hs + ':' + ms;
            let ok = true;
            for (let i = 0; i < 5; ++i) {
                if (time[i] !== '?' && time[i] !== cur[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function countTime(time: string): number {
    let count = 0;
    for (let h = 0; h < 24; ++h) {
        const hs = h.toString().padStart(2, '0');
        for (let m = 0; m < 60; ++m) {
            const ms = m.toString().padStart(2, '0');
            const candidate = `${hs}:${ms}`;
            let ok = true;
            for (let i = 0; i < 5; ++i) {
                if (time[i] !== '?' && time[i] !== candidate[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) ++count;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $time
     * @return Integer
     */
    function countTime($time) {
        $count = 0;
        for ($h = 0; $h < 24; $h++) {
            $hh = str_pad((string)$h, 2, '0', STR_PAD_LEFT);
            if (($time[0] !== '?' && $time[0] !== $hh[0]) ||
                ($time[1] !== '?' && $time[1] !== $hh[1])) {
                continue;
            }
            for ($m = 0; $m < 60; $m++) {
                $mm = str_pad((string)$m, 2, '0', STR_PAD_LEFT);
                if (($time[3] !== '?' && $time[3] !== $mm[0]) ||
                    ($time[4] !== '?' && $time[4] !== $mm[1])) {
                    continue;
                }
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countTime(_ time: String) -> Int {
        let t = Array(time)
        var result = 0
        for hour in 0..<24 {
            let hs = String(format: "%02d", hour)
            let hChars = Array(hs)
            if t[0] != "?" && t[0] != hChars[0] { continue }
            if t[1] != "?" && t[1] != hChars[1] { continue }
            for minute in 0..<60 {
                let ms = String(format: "%02d", minute)
                let mChars = Array(ms)
                if t[3] != "?" && t[3] != mChars[0] { continue }
                if t[4] != "?" && t[4] != mChars[1] { continue }
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
    fun countTime(time: String): Int {
        var count = 0
        for (h in 0..23) {
            val hh = if (h < 10) "0$h" else h.toString()
            for (m in 0..59) {
                val mm = if (m < 10) "0$m" else m.toString()
                val candidate = "$hh:$mm"
                var match = true
                for (i in time.indices) {
                    if (time[i] != '?' && time[i] != candidate[i]) {
                        match = false
                        break
                    }
                }
                if (match) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countTime(String time) {
    int ans = 0;
    for (int h = 0; h < 24; ++h) {
      String hs = h.toString().padLeft(2, '0');
      for (int m = 0; m < 60; ++m) {
        String ms = m.toString().padLeft(2, '0');
        bool ok = true;
        if (time[0] != '?' && time[0] != hs[0]) ok = false;
        else if (time[1] != '?' && time[1] != hs[1]) ok = false;
        else if (time[3] != '?' && time[3] != ms[0]) ok = false;
        else if (time[4] != '?' && time[4] != ms[1]) ok = false;
        if (ok) ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "fmt"

func countTime(time string) int {
	cnt := 0
	for h := 0; h < 24; h++ {
		for m := 0; m < 60; m++ {
			s := fmt.Sprintf("%02d:%02d", h, m)
			ok := true
			for i := 0; i < 5; i++ {
				if time[i] != '?' && time[i] != s[i] {
					ok = false
					break
				}
			}
			if ok {
				cnt++
			}
		}
	}
	return cnt
}
```

## Ruby

```ruby
def count_time(time)
  count = 0
  (0..23).each do |h|
    hh = format('%02d', h)
    (0..59).each do |m|
      mm = format('%02d', m)
      t = "#{hh}:#{mm}"
      match = true
      time.each_char.with_index do |c, i|
        next if c == '?'
        if c != t[i]
          match = false
          break
        end
      end
      count += 1 if match
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countTime(time: String): Int = {
        var count = 0
        for (h <- 0 until 24) {
            val hh = f"$h%02d"
            for (m <- 0 until 60) {
                val mm = f"$m%02d"
                val candidate = s"$hh:$mm"
                var ok = true
                var i = 0
                while (i < time.length && ok) {
                    if (time.charAt(i) != '?' && time.charAt(i) != candidate.charAt(i)) {
                        ok = false
                    }
                    i += 1
                }
                if (ok) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_time(time: String) -> i32 {
        let b = time.as_bytes();
        let mut hour_cnt = 0;
        for h in 0..24 {
            let d1 = ((h / 10) as u8) + b'0';
            let d2 = ((h % 10) as u8) + b'0';
            if (b[0] == b'?' || b[0] == d1) && (b[1] == b'?' || b[1] == d2) {
                hour_cnt += 1;
            }
        }
        let mut minute_cnt = 0;
        for m in 0..60 {
            let d1 = ((m / 10) as u8) + b'0';
            let d2 = ((m % 10) as u8) + b'0';
            if (b[3] == b'?' || b[3] == d1) && (b[4] == b'?' || b[4] == d2) {
                minute_cnt += 1;
            }
        }
        (hour_cnt * minute_cnt) as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define (matches? pattern s)
  (for/and ([p (in-string pattern)]
            [c (in-string s)])
    (or (char=? p #\?) (char=? p c))))

(define/contract (count-time time)
  (-> string? exact-integer?)
  (for/sum ([h (in-range 24)]
            [m (in-range 60)])
    (let* ((hs (format "~2,'0d" h))
           (ms (format "~2,'0d" m))
           (t (string-append hs ":" ms)))
      (if (matches? time t) 1 0))))
```

## Erlang

```erlang
-module(solution).
-export([count_time/1]).

-spec count_time(unicode:unicode_binary()) -> integer().
count_time(Time) ->
    Pattern = binary_to_list(Time),
    lists:foldl(fun(H, AccH) ->
        lists:foldl(fun(M, AccM) ->
            HourDigits = two_digits(H),
            MinuteDigits = two_digits(M),
            Candidate = HourDigits ++ [$:] ++ MinuteDigits,
            case match(Pattern, Candidate) of
                true -> AccM + 1;
                false -> AccM
            end
        end, AccH, lists:seq(0,59))
    end, 0, lists:seq(0,23)).

two_digits(N) when N < 10 ->
    [$0, $0 + N];
two_digits(N) ->
    [$0 + (N div 10), $0 + (N rem 10)].

match([], []) -> true;
match([C|RestP], [D|RestC]) ->
    (C =:= $?) orelse C =:= D andalso match(RestP, RestC).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_time(time :: String.t()) :: integer()
  def count_time(time) do
    [h_pat, m_pat] = String.split(time, ":")
    h1 = String.at(h_pat, 0)
    h2 = String.at(h_pat, 1)
    m1 = String.at(m_pat, 0)
    m2 = String.at(m_pat, 1)

    Enum.reduce(0..23, 0, fn hour, acc ->
      hs = pad2(hour)

      Enum.reduce(0..59, acc, fn minute, acc2 ->
        ms = pad2(minute)

        if match?(h1, String.at(hs, 0)) and
           match?(h2, String.at(hs, 1)) and
           match?(m1, String.at(ms, 0)) and
           match?(m2, String.at(ms, 1)) do
          acc2 + 1
        else
          acc2
        end
      end)
    end)
  end

  defp pad2(num) when num < 10, do: "0#{num}"
  defp pad2(num), do: Integer.to_string(num)

  defp match?("?", _), do: true
  defp match?(c, c), do: true
  defp match?(_, _), do: false
end
```
