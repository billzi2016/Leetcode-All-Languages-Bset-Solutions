# 3114. Latest Time You Can Obtain After Replacing Characters

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string findLatestTime(string s) {
        string best = "";
        int bestVal = -1;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                char buf[6];
                sprintf(buf, "%02d:%02d", h, m);
                string cand(buf);
                bool ok = true;
                for (int i = 0; i < 5; ++i) {
                    if (s[i] != '?' && s[i] != cand[i]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    int val = h * 60 + m;
                    if (val > bestVal) {
                        bestVal = val;
                        best = cand;
                    }
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String findLatestTime(String s) {
        int best = -1;
        String bestStr = "";
        for (int h = 0; h <= 11; h++) {
            for (int m = 0; m < 60; m++) {
                String cand = String.format("%02d:%02d", h, m);
                boolean ok = true;
                for (int i = 0; i < 5; i++) {
                    char sc = s.charAt(i);
                    if (sc != '?' && sc != cand.charAt(i)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) {
                    int val = h * 60 + m;
                    if (val > best) {
                        best = val;
                        bestStr = cand;
                    }
                }
            }
        }
        return bestStr;
    }
}
```

## Python

```python
class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = -1
        best_time = ""
        for h in range(12):  # 0 to 11 inclusive
            for m in range(60):  # 0 to 59 inclusive
                cur = "{:02d}:{:02d}".format(h, m)
                match = True
                for i in range(5):
                    if s[i] != '?' and s[i] != cur[i]:
                        match = False
                        break
                if match:
                    total = h * 60 + m
                    if total > best:
                        best = total
                        best_time = cur
        return best_time
```

## Python3

```python
class Solution:
    def findLatestTime(self, s: str) -> str:
        chars = list(s)
        # Hour tens
        if chars[0] == '?':
            if chars[1] == '?':
                chars[0] = '1'
            else:
                chars[0] = '1' if chars[1] <= '1' else '0'
        # Hour units
        if chars[1] == '?':
            chars[1] = '1' if chars[0] == '1' else '9'
        # Minute tens
        if chars[3] == '?':
            chars[3] = '5'
        # Minute units
        if chars[4] == '?':
            chars[4] = '9'
        return ''.join(chars)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* findLatestTime(char* s) {
    int best = -1;
    char bestStr[6];
    for (int h = 0; h <= 11; ++h) {
        for (int m = 0; m < 60; ++m) {
            char cand[6];
            cand[0] = '0' + h / 10;
            cand[1] = '0' + h % 10;
            cand[2] = ':';
            cand[3] = '0' + m / 10;
            cand[4] = '0' + m % 10;
            cand[5] = '\0';
            int ok = 1;
            for (int i = 0; i < 5; ++i) {
                if (s[i] != '?' && s[i] != cand[i]) {
                    ok = 0;
                    break;
                }
            }
            if (ok) {
                int total = h * 60 + m;
                if (total > best) {
                    best = total;
                    memcpy(bestStr, cand, 6);
                }
            }
        }
    }
    char* res = (char*)malloc(6 * sizeof(char));
    strcpy(res, bestStr);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string FindLatestTime(string s) {
        for (int h = 11; h >= 0; h--) {
            for (int m = 59; m >= 0; m--) {
                string t = $"{h:D2}:{m:D2}";
                bool ok = true;
                for (int i = 0; i < 5; i++) {
                    if (s[i] != '?' && s[i] != t[i]) {
                        ok = false;
                        break;
                    }
                }
                if (ok) return t;
            }
        }
        return ""; // guaranteed to find a valid time
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var findLatestTime = function(s) {
    for (let h = 11; h >= 0; h--) {
        const hh = h.toString().padStart(2, '0');
        for (let m = 59; m >= 0; m--) {
            const mm = m.toString().padStart(2, '0');
            const t = `${hh}:${mm}`;
            let ok = true;
            for (let i = 0; i < 5; i++) {
                if (s[i] !== '?' && s[i] !== t[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) return t;
        }
    }
    return ""; // guaranteed to find a valid time per constraints
};
```

## Typescript

```typescript
function findLatestTime(s: string): string {
    let best = "";
    for (let h = 0; h < 12; h++) {
        const hh = h.toString().padStart(2, '0');
        for (let m = 0; m < 60; m++) {
            const mm = m.toString().padStart(2, '0');
            const t = `${hh}:${mm}`;
            let ok = true;
            for (let i = 0; i < 5; i++) {
                if (s[i] !== '?' && s[i] !== t[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok && (best === "" || t > best)) {
                best = t;
            }
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function findLatestTime($s) {
        for ($h = 11; $h >= 0; $h--) {
            for ($m = 59; $m >= 0; $m--) {
                $time = sprintf("%02d:%02d", $h, $m);
                $match = true;
                for ($i = 0; $i < 5; $i++) {
                    if ($s[$i] !== '?' && $s[$i] !== $time[$i]) {
                        $match = false;
                        break;
                    }
                }
                if ($match) {
                    return $time;
                }
            }
        }
        // According to constraints, this line should never be reached.
        return "";
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func findLatestTime(_ s: String) -> String {
        var best = ""
        var bestVal = -1
        let patternChars = Array(s)
        
        for hour in 0...11 {
            for minute in 0...59 {
                let hh = String(format: "%02d", hour)
                let mm = String(format: "%02d", minute)
                let candidate = "\(hh):\(mm)"
                if isMatch(candidate, patternChars) {
                    let value = hour * 60 + minute
                    if value > bestVal {
                        bestVal = value
                        best = candidate
                    }
                }
            }
        }
        return best
    }
    
    private func isMatch(_ time: String, _ pattern: [Character]) -> Bool {
        let tChars = Array(time)
        for i in 0..<tChars.count {
            if pattern[i] != "?" && pattern[i] != tChars[i] {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLatestTime(s: String): String {
        var bestHour = 0
        var bestMin = 0
        for (h in 0..11) {
            val hh = if (h < 10) "0$h" else "$h"
            for (m in 0..59) {
                val mm = if (m < 10) "0$m" else "$m"
                val candidate = "$hh:$mm"
                var ok = true
                for (i in s.indices) {
                    if (s[i] != '?' && s[i] != candidate[i]) {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    if (h > bestHour || (h == bestHour && m > bestMin)) {
                        bestHour = h
                        bestMin = m
                    }
                }
            }
        }
        val resH = if (bestHour < 10) "0$bestHour" else "$bestHour"
        val resM = if (bestMin < 10) "0$bestMin" else "$bestMin"
        return "$resH:$resM"
    }
}
```

## Dart

```dart
class Solution {
  String findLatestTime(String s) {
    int best = -1;
    String bestStr = "";
    for (int h = 0; h < 12; ++h) {
      for (int m = 0; m < 60; ++m) {
        String hh = h.toString().padLeft(2, '0');
        String mm = m.toString().padLeft(2, '0');
        String cand = "$hh:$mm";
        bool ok = true;
        for (int i = 0; i < s.length; ++i) {
          if (s[i] != '?' && s[i] != cand[i]) {
            ok = false;
            break;
          }
        }
        if (ok) {
          int total = h * 60 + m;
          if (total > best) {
            best = total;
            bestStr = cand;
          }
        }
      }
    }
    return bestStr;
  }
}
```

## Golang

```go
package main

import "fmt"

func findLatestTime(s string) string {
	best := ""
	maxVal := -1
	for h := 0; h < 12; h++ {
		for m := 0; m < 60; m++ {
			t := fmt.Sprintf("%02d:%02d", h, m)
			ok := true
			for i := 0; i < 5; i++ {
				if s[i] != '?' && s[i] != t[i] {
					ok = false
					break
				}
			}
			if ok {
				val := h*60 + m
				if val > maxVal {
					maxVal = val
					best = t
				}
			}
		}
	}
	return best
}
```

## Ruby

```ruby
def find_latest_time(s)
  (0..11).to_a.reverse.each do |h|
    (0..59).to_a.reverse.each do |m|
      hh = format('%02d', h)
      mm = format('%02d', m)
      t = "#{hh}:#{mm}"
      match = true
      s.chars.each_with_index do |c, i|
        next if c == '?'
        if c != t[i]
          match = false
          break
        end
      end
      return t if match
    end
  end
end
```

## Scala

```scala
object Solution {
    def findLatestTime(s: String): String = {
        for (h <- 11 to 0 by -1) {
            val hh = f"$h%02d"
            for (m <- 59 to 0 by -1) {
                val mm = f"$m%02d"
                val cand = s"${hh}:${mm}"
                var ok = true
                var i = 0
                while (i < 5 && ok) {
                    if (s(i) != '?' && s(i) != cand(i)) ok = false
                    i += 1
                }
                if (ok) return cand
            }
        }
        "" // guaranteed to never reach here
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_latest_time(s: String) -> String {
        let bytes = s.as_bytes();
        for h in (0..=11).rev() {
            let hour_str = format!("{:02}", h);
            let hb = hour_str.as_bytes();
            if !(bytes[0] == b'?' || bytes[0] == hb[0]) { continue; }
            if !(bytes[1] == b'?' || bytes[1] == hb[1]) { continue; }
            for m in (0..=59).rev() {
                let minute_str = format!("{:02}", m);
                let mb = minute_str.as_bytes();
                if !(bytes[3] == b'?' || bytes[3] == mb[0]) { continue; }
                if !(bytes[4] == b'?' || bytes[4] == mb[1]) { continue; }
                return format!("{}:{}", hour_str, minute_str);
            }
        }
        String::new() // guaranteed never to reach
    }
}
```

## Racket

```racket
(define/contract (find-latest-time s)
  (-> string? string?)
  (define (matches? pat cand)
    (let loop ((i 0) (len (string-length pat)))
      (if (= i len)
          #t
          (let ((pc (string-ref pat i))
                (cc (string-ref cand i)))
            (if (char=? pc #\?)
                (loop (+ i 1) len)
                (and (char=? pc cc) (loop (+ i 1) len)))))))
  (define max-min -1)
  (define ans "")
  (for ([h (in-range 0 12)])
    (for ([m (in-range 0 60)])
      (let* ((cand (format "~2,'0d:~2,'0d" h m))
             (total (+ (* h 60) m)))
        (when (and (matches? s cand) (> total max-min))
          (set! max-min total)
          (set! ans cand)))))
  ans)
```

## Erlang

```erlang
-spec find_latest_time(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
find_latest_time(S) ->
    Pattern = binary_to_list(S),
    {_, BestBin} =
        lists:foldl(
            fun(Hour, AccHour) ->
                lists:foldl(
                    fun(Minute, {CurBestTime, CurBestBin}) ->
                        CandidateBin = iolist_to_binary(io_lib:format("~2..0B:~2..0B", [Hour, Minute])),
                        CandList = binary_to_list(CandidateBin),
                        case matches(Pattern, CandList) of
                            true ->
                                TimeVal = Hour * 60 + Minute,
                                if TimeVal > CurBestTime ->
                                        {TimeVal, CandidateBin};
                                   true ->
                                        {CurBestTime, CurBestBin}
                                end;
                            false ->
                                {CurBestTime, CurBestBin}
                        end
                    end,
                    AccHour,
                    lists:seq(0, 59)
                )
            end,
            {-1, <<>>},
            lists:seq(0, 11)
        ),
    BestBin.

matches([], []) -> true;
matches([P|Ps], [C|Cs]) ->
    (P =:= $?) orelse (P =:= C) andalso matches(Ps, Cs).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_latest_time(s :: String.t()) :: String.t()
  def find_latest_time(s) do
    pattern = String.to_charlist(s)

    {best_h, best_m} =
      Enum.reduce(0..11, {-1, -1}, fn h, acc ->
        Enum.reduce(0..59, acc, fn m, {bh, bm} = _acc2 ->
          time_str = :io_lib.format("~2..0B:~2..0B", [h, m]) |> List.to_string()

          if matches?(time_str, pattern) do
            if h * 60 + m > bh * 60 + bm do
              {h, m}
            else
              {bh, bm}
            end
          else
            {bh, bm}
          end
        end)
      end)

    :io_lib.format("~2..0B:~2..0B", [best_h, best_m]) |> List.to_string()
  end

  defp matches?(time_str, pattern) do
    time_chars = String.to_charlist(time_str)

    Enum.zip(time_chars, pattern)
    |> Enum.all?(fn {c, p} -> p == ?? || p == c end)
  end
end
```
