# 2446. Determine if Two Events Have Conflict

## Cpp

```cpp
class Solution {
public:
    bool haveConflict(vector<string>& event1, vector<string>& event2) {
        auto toMinutes = [](const string& t)->int{
            int h = (t[0]-'0')*10 + (t[1]-'0');
            int m = (t[3]-'0')*10 + (t[4]-'0');
            return h*60 + m;
        };
        int s1 = toMinutes(event1[0]);
        int e1 = toMinutes(event1[1]);
        int s2 = toMinutes(event2[0]);
        int e2 = toMinutes(event2[1]);
        return max(s1, s2) <= min(e1, e2);
    }
};
```

## Java

```java
class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        int s1 = toMinutes(event1[0]);
        int e1 = toMinutes(event1[1]);
        int s2 = toMinutes(event2[0]);
        int e2 = toMinutes(event2[1]);
        return Math.max(s1, s2) <= Math.min(e1, e2);
    }
    
    private int toMinutes(String time) {
        int hour = (time.charAt(0) - '0') * 10 + (time.charAt(1) - '0');
        int minute = (time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
        return hour * 60 + minute;
    }
}
```

## Python

```python
class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        def to_minutes(t):
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        
        s1, e1 = map(to_minutes, event1)
        s2, e2 = map(to_minutes, event2)
        return not (e1 < s2 or e2 < s1)
```

## Python3

```python
from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def to_minutes(t: str) -> int:
            h, m = t.split(':')
            return int(h) * 60 + int(m)
        
        s1, e1 = map(to_minutes, event1)
        s2, e2 = map(to_minutes, event2)
        return max(s1, s2) <= min(e1, e2)
```

## C

```c
#include <stdbool.h>

static int timeToMinutes(const char *t) {
    int hour = (t[0] - '0') * 10 + (t[1] - '0');
    int minute = (t[3] - '0') * 10 + (t[4] - '0');
    return hour * 60 + minute;
}

bool haveConflict(char **event1, int event1Size, char **event2, int event2Size) {
    int start1 = timeToMinutes(event1[0]);
    int end1   = timeToMinutes(event1[1]);
    int start2 = timeToMinutes(event2[0]);
    int end2   = timeToMinutes(event2[1]);

    return (start1 <= end2 && start2 <= end1);
}
```

## Csharp

```csharp
public class Solution
{
    public bool HaveConflict(string[] event1, string[] event2)
    {
        int s1 = Parse(event1[0]);
        int e1 = Parse(event1[1]);
        int s2 = Parse(event2[0]);
        int e2 = Parse(event2[1]);

        return Math.Max(s1, s2) <= Math.Min(e1, e2);
    }

    private int Parse(string time)
    {
        // time format "HH:MM"
        int hours = (time[0] - '0') * 10 + (time[1] - '0');
        int minutes = (time[3] - '0') * 10 + (time[4] - '0');
        return hours * 60 + minutes;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} event1
 * @param {string[]} event2
 * @return {boolean}
 */
var haveConflict = function(event1, event2) {
    const toMinutes = (t) => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };
    
    const start1 = toMinutes(event1[0]);
    const end1   = toMinutes(event1[1]);
    const start2 = toMinutes(event2[0]);
    const end2   = toMinutes(event2[1]);
    
    // intervals are inclusive, so they overlap if they intersect at any point
    return !(end1 < start2 || end2 < start1);
};
```

## Typescript

```typescript
function haveConflict(event1: string[], event2: string[]): boolean {
    const toMinutes = (time: string): number => {
        const [h, m] = time.split(':').map(Number);
        return h * 60 + m;
    };
    
    const s1 = toMinutes(event1[0]);
    const e1 = toMinutes(event1[1]);
    const s2 = toMinutes(event2[0]);
    const e2 = toMinutes(event2[1]);
    
    return Math.max(s1, s2) <= Math.min(e1, e2);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $event1
     * @param String[] $event2
     * @return Boolean
     */
    function haveConflict($event1, $event2) {
        $s1 = $this->toMinutes($event1[0]);
        $e1 = $this->toMinutes($event1[1]);
        $s2 = $this->toMinutes($event2[0]);
        $e2 = $this->toMinutes($event2[1]);

        return ($s1 <= $e2 && $s2 <= $e1);
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
    func haveConflict(_ event1: [String], _ event2: [String]) -> Bool {
        func toMinutes(_ time: String) -> Int {
            let parts = time.split(separator: ":")
            let hour = Int(parts[0])!
            let minute = Int(parts[1])!
            return hour * 60 + minute
        }
        let start1 = toMinutes(event1[0])
        let end1 = toMinutes(event1[1])
        let start2 = toMinutes(event2[0])
        let end2 = toMinutes(event2[1])
        return !(end1 < start2 || end2 < start1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun haveConflict(event1: Array<String>, event2: Array<String>): Boolean {
        val s1 = toMinutes(event1[0])
        val e1 = toMinutes(event1[1])
        val s2 = toMinutes(event2[0])
        val e2 = toMinutes(event2[1])
        return maxOf(s1, s2) <= minOf(e1, e2)
    }

    private fun toMinutes(time: String): Int {
        val parts = time.split(":")
        return parts[0].toInt() * 60 + parts[1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  bool haveConflict(List<String> event1, List<String> event2) {
    int toMinutes(String time) {
      final parts = time.split(':');
      return int.parse(parts[0]) * 60 + int.parse(parts[1]);
    }

    int s1 = toMinutes(event1[0]);
    int e1 = toMinutes(event1[1]);
    int s2 = toMinutes(event2[0]);
    int e2 = toMinutes(event2[1]);

    return (s1 <= e2) && (s2 <= e1);
  }
}
```

## Golang

```go
func haveConflict(event1 []string, event2 []string) bool {
    parse := func(t string) int {
        // t format "HH:MM"
        hour := (int(t[0]-'0')*10 + int(t[1]-'0')) * 60
        minute := int(t[3]-'0')*10 + int(t[4]-'0')
        return hour + minute
    }
    s1, e1 := parse(event1[0]), parse(event1[1])
    s2, e2 := parse(event2[0]), parse(event2[1])
    if s1 > e2 || s2 > e1 {
        return false
    }
    return true
}
```

## Ruby

```ruby
def have_conflict(event1, event2)
  parse = ->(t) { t[0..1].to_i * 60 + t[3..4].to_i }
  s1 = parse.call(event1[0])
  e1 = parse.call(event1[1])
  s2 = parse.call(event2[0])
  e2 = parse.call(event2[1])
  [s1, s2].max <= [e1, e2].min
end
```

## Scala

```scala
object Solution {
    def haveConflict(event1: Array[String], event2: Array[String]): Boolean = {
        def toMinutes(t: String): Int = {
            val parts = t.split(":")
            parts(0).toInt * 60 + parts(1).toInt
        }
        val start1 = toMinutes(event1(0))
        val end1   = toMinutes(event1(1))
        val start2 = toMinutes(event2(0))
        val end2   = toMinutes(event2(1))

        math.max(start1, start2) <= math.min(end1, end2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn have_conflict(event1: Vec<String>, event2: Vec<String>) -> bool {
        fn parse(time: &str) -> i32 {
            let mut parts = time.split(':');
            let h: i32 = parts.next().unwrap().parse().unwrap();
            let m: i32 = parts.next().unwrap().parse().unwrap();
            h * 60 + m
        }

        let s1 = parse(&event1[0]);
        let e1 = parse(&event1[1]);
        let s2 = parse(&event2[0]);
        let e2 = parse(&event2[1]);

        std::cmp::max(s1, s2) <= std::cmp::min(e1, e2)
    }
}
```

## Racket

```racket
(define/contract (have-conflict event1 event2)
  (-> (listof string?) (listof string?) boolean?)
  (let* ([start1 (parse-time (first event1))]
         [end1   (parse-time (second event1))]
         [start2 (parse-time (first event2))]
         [end2   (parse-time (second event2))])
    (<= (max start1 start2) (min end1 end2))))

(define (parse-time s)
  (let* ([hour (string->number (substring s 0 2))]
         [minute (string->number (substring s 3 5))])
    (+ (* hour 60) minute)))
```

## Erlang

```erlang
-module(solution).
-export([have_conflict/2]).

-spec have_conflict(Event1 :: [unicode:unicode_binary()], Event2 :: [unicode:unicode_binary()]) -> boolean().
have_conflict(Event1, Event2) ->
    [Start1Str, End1Str] = Event1,
    [Start2Str, End2Str] = Event2,
    S1 = parse_time(Start1Str),
    E1 = parse_time(End1Str),
    S2 = parse_time(Start2Str),
    E2 = parse_time(End2Str),
    max(S1, S2) =< min(E1, E2).

parse_time(TimeBin) ->
    [H, M] = binary:split(TimeBin, <<":">>, [global]),
    binary_to_integer(H) * 60 + binary_to_integer(M).
```

## Elixir

```elixir
defmodule Solution do
  @spec have_conflict(event1 :: [String.t()], event2 :: [String.t()]) :: boolean()
  def have_conflict(event1, event2) do
    s1 = to_minutes(Enum.at(event1, 0))
    e1 = to_minutes(Enum.at(event1, 1))
    s2 = to_minutes(Enum.at(event2, 0))
    e2 = to_minutes(Enum.at(event2, 1))

    max(s1, s2) <= min(e1, e2)
  end

  defp to_minutes(time) do
    [h, m] = String.split(time, ":")
    String.to_integer(h) * 60 + String.to_integer(m)
  end
end
```
