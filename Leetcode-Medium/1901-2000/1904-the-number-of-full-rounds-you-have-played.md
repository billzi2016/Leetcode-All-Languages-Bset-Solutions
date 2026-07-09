# 1904. The Number of Full Rounds You Have Played

## Cpp

```cpp
class Solution {
public:
    int numberOfRounds(string loginTime, string logoutTime) {
        auto toMin = [](const string& t)->int{
            int h = stoi(t.substr(0,2));
            int m = stoi(t.substr(3,2));
            return h*60 + m;
        };
        int start = toMin(loginTime);
        int end = toMin(logoutTime);
        if (end < start) end += 24*60; // next day
        
        // first possible round start time (multiple of 15) not earlier than login
        int first = ((start + 14) / 15) * 15;
        // last possible round start time such that the round ends before or at logout
        if (end < 15) return 0; // cannot happen but safety
        int last = ((end - 15) / 15) * 15;
        
        if (last < first) return 0;
        return (last - first) / 15 + 1;
    }
};
```

## Java

```java
class Solution {
    public int numberOfRounds(String loginTime, String logoutTime) {
        int login = toMinutes(loginTime);
        int logout = toMinutes(logoutTime);
        if (logout < login) {
            logout += 24 * 60;
        }
        // earliest round start that can be fully played
        int firstStart = ((login + 14) / 15) * 15;
        // latest round start whose end is <= logout
        int lastStart = ((logout - 1) / 15) * 15;
        if (lastStart < firstStart) {
            return 0;
        }
        return (lastStart - firstStart) / 15 + 1;
    }

    private int toMinutes(String time) {
        String[] parts = time.split(":");
        int h = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        return h * 60 + m;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        def to_minutes(t):
            h, m = map(int, t.split(':'))
            return h * 60 + m

        start = to_minutes(loginTime)
        end = to_minutes(logoutTime)

        if end < start:
            end += 24 * 60  # cross midnight

        # round start up to next multiple of 15
        rounded_start = ((start + 14) // 15) * 15
        # round end down to previous multiple of 15
        rounded_end = (end // 15) * 15

        if rounded_start > rounded_end:
            return 0
        return (rounded_end - rounded_start) // 15
```

## Python3

```python
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def to_minutes(t: str) -> int:
            h, m = map(int, t.split(':'))
            return h * 60 + m

        L = to_minutes(loginTime)
        R = to_minutes(logoutTime)
        if R < L:
            R += 24 * 60

        # first possible round start (multiple of 15) not earlier than login
        start = ((L + 14) // 15) * 15
        # last possible round start such that the whole round ends before logout
        end = ((R - 15) // 15) * 15

        if start > end:
            return 0
        return (end - start) // 15 + 1
```

## C

```c
int numberOfRounds(char* loginTime, char* logoutTime) {
    // Convert hh:mm to minutes since start of day
    int login = (loginTime[0] - '0') * 10 + (loginTime[1] - '0');
    login = login * 60 + (loginTime[3] - '0') * 10 + (loginTime[4] - '0');
    
    int logout = (logoutTime[0] - '0') * 10 + (logoutTime[1] - '0');
    logout = logout * 60 + (logoutTime[3] - '0') * 10 + (logoutTime[4] - '0');
    
    // If logout is earlier, it means crossing midnight
    if (logout < login) {
        logout += 24 * 60;
    }
    
    // First possible full round start time after or at login
    int start = ((login + 14) / 15) * 15;   // ceil to next multiple of 15
    // Last possible full round end time before or at logout
    int end = (logout / 15) * 15;          // floor to previous multiple of 15
    
    if (start > end) return 0;
    return (end - start) / 15;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfRounds(string loginTime, string logoutTime) {
        int ToMinutes(string t) => int.Parse(t.Substring(0, 2)) * 60 + int.Parse(t.Substring(3, 2));

        int start = ToMinutes(loginTime);
        int end = ToMinutes(logoutTime);
        if (end < start) end += 24 * 60; // cross midnight

        // first round start time that can be fully played
        int first = ((start + 14) / 15) * 15;
        // last possible round start time
        int last = end - 15;

        if (first > last) return 0;
        return (last - first) / 15 + 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} loginTime
 * @param {string} logoutTime
 * @return {number}
 */
var numberOfRounds = function(loginTime, logoutTime) {
    const toMinutes = t => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };
    
    let start = toMinutes(loginTime);
    let end = toMinutes(logoutTime);
    if (end < start) end += 24 * 60; // cross midnight
    
    const firstStart = Math.ceil(start / 15) * 15;
    const lastStart = Math.floor((end - 15) / 15) * 15;
    
    if (firstStart > lastStart) return 0;
    return ((lastStart - firstStart) / 15) + 1;
};
```

## Typescript

```typescript
function numberOfRounds(loginTime: string, logoutTime: string): number {
    const toMinutes = (t: string): number => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };
    let start = toMinutes(loginTime);
    let end = toMinutes(logoutTime);
    if (end <= start) end += 24 * 60; // cross midnight
    const first = Math.ceil(start / 15) * 15;
    const last = Math.floor(end / 15) * 15;
    return first > last ? 0 : (last - first) / 15;
}
```

## Php

```php
class Solution {

    /**
     * @param String $loginTime
     * @param String $logoutTime
     * @return Integer
     */
    function numberOfRounds($loginTime, $logoutTime) {
        $login = $this->toMinutes($loginTime);
        $logout = $this->toMinutes($logoutTime);
        if ($logout < $login) {
            $logout += 24 * 60;
        }
        $L = 15;
        $fullRounds = intdiv($logout, $L) - (int)ceil($login / $L);
        return $fullRounds > 0 ? $fullRounds : 0;
    }

    private function toMinutes(string $time): int {
        [$h, $m] = explode(':', $time);
        return intval($h) * 60 + intval($m);
    }
}
```

## Swift

```swift
class Solution {
    func numberOfRounds(_ loginTime: String, _ logoutTime: String) -> Int {
        func toMinutes(_ s: String) -> Int {
            let parts = s.split(separator: ":")
            let h = Int(parts[0])!
            let m = Int(parts[1])!
            return h * 60 + m
        }
        var login = toMinutes(loginTime)
        var logout = toMinutes(logoutTime)
        if logout < login {
            logout += 24 * 60
        }
        let start = ((login + 14) / 15) * 15
        let end = ((logout - 15) / 15) * 15
        if start > end { return 0 }
        return (end - start) / 15 + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfRounds(loginTime: String, logoutTime: String): Int {
        fun toMinutes(t: String): Int {
            val parts = t.split(":")
            return parts[0].toInt() * 60 + parts[1].toInt()
        }
        var login = toMinutes(loginTime)
        var logout = toMinutes(logoutTime)
        if (logout < login) logout += 24 * 60
        // smallest start index (multiple of 15) >= login
        val startIdx = (login + 14) / 15
        // largest start index such that start+15 <= logout
        val endIdx = (logout - 15) / 15
        return if (endIdx < startIdx) 0 else endIdx - startIdx + 1
    }
}
```

## Dart

```dart
class Solution {
  int numberOfRounds(String loginTime, String logoutTime) {
    int toMinutes(String t) {
      var parts = t.split(':');
      return int.parse(parts[0]) * 60 + int.parse(parts[1]);
    }

    int login = toMinutes(loginTime);
    int logout = toMinutes(logoutTime);
    if (logout < login) logout += 24 * 60;

    int startIdx = (login + 14) ~/ 15; // ceil division
    int endIdx = logout ~/ 15;         // floor division

    int ans = endIdx - startIdx;
    return ans > 0 ? ans : 0;
  }
}
```

## Golang

```go
package main

import "strconv"

func numberOfRounds(loginTime string, logoutTime string) int {
	toMin := func(t string) int {
		h, _ := strconv.Atoi(t[:2])
		m, _ := strconv.Atoi(t[3:])
		return h*60 + m
	}
	login := toMin(loginTime)
	logout := toMin(logoutTime)

	if logout < login {
		logout += 24 * 60
	}

	start := ((login + 14) / 15) * 15               // first round start >= login
	end := ((logout - 15) / 15) * 15                // last round start where full round fits
	if start > end {
		return 0
	}
	return (end-start)/15 + 1
}
```

## Ruby

```ruby
def number_of_rounds(login_time, logout_time)
  h, m = login_time.split(':').map(&:to_i)
  start_min = h * 60 + m

  h, m = logout_time.split(':').map(&:to_i)
  end_min = h * 60 + m

  end_min += 24 * 60 if end_min < start_min

  first_start = ((start_min + 14) / 15) * 15
  return 0 if first_start + 15 > end_min

  last_start = ((end_min - 15) / 15) * 15
  (last_start - first_start) / 15 + 1
end
```

## Scala

```scala
object Solution {
    def numberOfRounds(loginTime: String, logoutTime: String): Int = {
        def toMinutes(t: String): Int = {
            val parts = t.split(":")
            parts(0).toInt * 60 + parts(1).toInt
        }
        var start = toMinutes(loginTime)
        var end = toMinutes(logoutTime)
        if (end < start) end += 24 * 60

        // earliest round start not before login
        val first = ((start + 14) / 15) * 15
        // latest round start that finishes before or at logout
        val last = ((end - 15) / 15) * 15

        if (first > last) 0 else ((last - first) / 15) + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_rounds(login_time: String, logout_time: String) -> i32 {
        fn to_minutes(t: &str) -> i32 {
            let mut parts = t.split(':');
            let h: i32 = parts.next().unwrap().parse().unwrap();
            let m: i32 = parts.next().unwrap().parse().unwrap();
            h * 60 + m
        }

        let mut login = to_minutes(&login_time);
        let mut logout = to_minutes(&logout_time);

        if logout < login {
            logout += 24 * 60;
        }

        // first round start not earlier than login
        let start = ((login + 14) / 15) * 15;
        // last possible round start so that the whole round ends before or at logout
        let last_possible_start = logout - 15;

        if last_possible_start < start {
            return 0;
        }

        let end = (last_possible_start / 15) * 15;
        ((end - start) / 15 + 1) as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-rounds loginTime logoutTime)
  (-> string? string? exact-integer?)
  (let* ([parse
          (lambda (s)
            (+ (* (string->number (substring s 0 2)) 60)
               (string->number (substring s 3 5))))]
         [loginM (parse loginTime)]
         [logoutM0 (parse logoutTime)]
         [logoutM (if (< logoutM0 loginM) (+ logoutM0 1440) logoutM0)])
    (let* ([start (* 15 (quotient (+ loginM 14) 15))] ; first round start >= login
           [end (- logoutM 15)])                     ; last possible round start
      (if (> start end)
          0
          (+ 1 (quotient (- end start) 15))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_rounds/2]).

-spec number_of_rounds(LoginTime :: unicode:unicode_binary(), LogoutTime :: unicode:unicode_binary()) -> integer().
number_of_rounds(LoginTime, LogoutTime) ->
    Login = parse_time(LoginTime),
    Logout0 = parse_time(LogoutTime),
    Logout = if Logout0 < Login -> Logout0 + 24*60; true -> Logout0 end,
    EndLimit = Logout - 15,
    case EndLimit >= Login of
        false -> 0;
        true ->
            FirstStart = ((Login + 14) div 15) * 15,
            if FirstStart > EndLimit -> 0;
               true -> (EndLimit - FirstStart) div 15 + 1
            end
    end.

parse_time(TimeBin) ->
    <<H1, H2, $:, M1, M2>> = TimeBin,
    Hours = (H1 - $0) * 10 + (H2 - $0),
    Minutes = (M1 - $0) * 10 + (M2 - $0),
    Hours*60 + Minutes.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_rounds(login_time :: String.t(), logout_time :: String.t()) :: integer()
  def number_of_rounds(login_time, logout_time) do
    login = to_minutes(login_time)
    logout = to_minutes(logout_time)

    logout =
      if logout < login do
        logout + 24 * 60
      else
        logout
      end

    first_start = ((login + 14) |> div(15)) * 15
    last_start = ((logout - 15) |> div(15)) * 15

    if first_start > last_start do
      0
    else
      ((last_start - first_start) |> div(15)) + 1
    end
  end

  defp to_minutes(time_str) do
    [h, m] = String.split(time_str, ":")
    String.to_integer(h) * 60 + String.to_integer(m)
  end
end
```
