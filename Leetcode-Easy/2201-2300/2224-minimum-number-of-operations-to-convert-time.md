# 2224. Minimum Number of Operations to Convert Time

## Cpp

```cpp
class Solution {
public:
    int convertTime(string current, string correct) {
        auto toMinutes = [](const string& t) {
            int h = (t[0] - '0') * 10 + (t[1] - '0');
            int m = (t[3] - '0') * 10 + (t[4] - '0');
            return h * 60 + m;
        };
        int diff = toMinutes(correct) - toMinutes(current);
        int ops = 0;
        const int vals[4] = {60, 15, 5, 1};
        for (int v : vals) {
            ops += diff / v;
            diff %= v;
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int convertTime(String current, String correct) {
        int cur = toMinutes(current);
        int cor = toMinutes(correct);
        int diff = cor - cur;
        int ops = 0;
        int[] vals = {60, 15, 5, 1};
        for (int v : vals) {
            ops += diff / v;
            diff %= v;
        }
        return ops;
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
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))
        diff = (h2 * 60 + m2) - (h1 * 60 + m1)
        ops = 0
        for d in (60, 15, 5, 1):
            ops += diff // d
            diff %= d
        return ops
```

## Python3

```python
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))
        diff = (h2 * 60 + m2) - (h1 * 60 + m1)
        ops = 0
        for d in (60, 15, 5, 1):
            ops += diff // d
            diff %= d
        return ops
```

## C

```c
#include <stdio.h>

int convertTime(char* current, char* correct) {
    int h1, m1, h2, m2;
    sscanf(current, "%d:%d", &h1, &m1);
    sscanf(correct, "%d:%d", &h2, &m2);
    
    int diff = (h2 * 60 + m2) - (h1 * 60 + m1);
    int ops = 0;
    
    ops += diff / 60;
    diff %= 60;
    
    ops += diff / 15;
    diff %= 15;
    
    ops += diff / 5;
    diff %= 5;
    
    ops += diff; // remaining minutes (1-minute operations)
    
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int ConvertTime(string current, string correct) {
        int cur = ToMinutes(current);
        int cor = ToMinutes(correct);
        int diff = cor - cur;
        int ops = 0;
        int[] vals = {60, 15, 5, 1};
        foreach (int v in vals) {
            ops += diff / v;
            diff %= v;
        }
        return ops;
    }

    private int ToMinutes(string time) {
        int hours = int.Parse(time.Substring(0, 2));
        int minutes = int.Parse(time.Substring(3, 2));
        return hours * 60 + minutes;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} current
 * @param {string} correct
 * @return {number}
 */
var convertTime = function(current, correct) {
    const toMinutes = t => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };
    
    let diff = toMinutes(correct) - toMinutes(current);
    const ops = [60, 15, 5, 1];
    let count = 0;
    
    for (const op of ops) {
        if (diff === 0) break;
        count += Math.floor(diff / op);
        diff %= op;
    }
    
    return count;
};
```

## Typescript

```typescript
function convertTime(current: string, correct: string): number {
    const toMinutes = (t: string): number => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };
    let diff = toMinutes(correct) - toMinutes(current);
    const ops = [60, 15, 5, 1];
    let count = 0;
    for (const op of ops) {
        count += Math.floor(diff / op);
        diff %= op;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $current
     * @param String $correct
     * @return Integer
     */
    function convertTime($current, $correct) {
        // Convert HH:MM to total minutes
        list($ch, $cm) = array_map('intval', explode(':', $current));
        list($rh, $rm) = array_map('intval', explode(':', $correct));
        $start = $ch * 60 + $cm;
        $end   = $rh * 60 + $rm;

        $diff = $end - $start; // guaranteed non‑negative

        $ops = 0;
        foreach ([60, 15, 5, 1] as $step) {
            if ($diff == 0) break;
            $cnt = intdiv($diff, $step);
            $ops += $cnt;
            $diff -= $cnt * $step;
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func convertTime(_ current: String, _ correct: String) -> Int {
        func minutes(from time: String) -> Int {
            let parts = time.split(separator: ":")
            let hour = Int(parts[0])!
            let minute = Int(parts[1])!
            return hour * 60 + minute
        }
        
        var diff = minutes(from: correct) - minutes(from: current)
        let ops = [60, 15, 5, 1]
        var count = 0
        
        for op in ops {
            if diff == 0 { break }
            count += diff / op
            diff %= op
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun convertTime(current: String, correct: String): Int {
        val curMinutes = current.substring(0, 2).toInt() * 60 + current.substring(3).toInt()
        val corrMinutes = correct.substring(0, 2).toInt() * 60 + correct.substring(3).toInt()
        var diff = corrMinutes - curMinutes
        var ops = 0
        val denominations = intArrayOf(60, 15, 5, 1)
        for (d in denominations) {
            ops += diff / d
            diff %= d
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int convertTime(String current, String correct) {
    int toMinutes(String s) {
      var parts = s.split(':');
      return int.parse(parts[0]) * 60 + int.parse(parts[1]);
    }

    int diff = toMinutes(correct) - toMinutes(current);
    const ops = [60, 15, 5, 1];
    int count = 0;
    for (var op in ops) {
      count += diff ~/ op;
      diff %= op;
    }
    return count;
  }
}
```

## Golang

```go
import "strconv"

func convertTime(current string, correct string) int {
	h1, _ := strconv.Atoi(current[:2])
	m1, _ := strconv.Atoi(current[3:])
	h2, _ := strconv.Atoi(correct[:2])
	m2, _ := strconv.Atoi(correct[3:])

	diff := (h2*60 + m2) - (h1*60 + m1)

	ops := diff / 60
	diff %= 60
	ops += diff / 15
	diff %= 15
	ops += diff / 5
	diff %= 5
	ops += diff

	return ops
}
```

## Ruby

```ruby
def convert_time(current, correct)
  cur_h, cur_m = current.split(':').map(&:to_i)
  cor_h, cor_m = correct.split(':').map(&:to_i)
  diff = (cor_h * 60 + cor_m) - (cur_h * 60 + cur_m)

  ops = 0
  [60, 15, 5, 1].each do |step|
    ops += diff / step
    diff %= step
  end
  ops
end
```

## Scala

```scala
object Solution {
    def convertTime(current: String, correct: String): Int = {
        def toMinutes(t: String): Int = {
            val parts = t.split(":")
            val h = parts(0).toInt
            val m = parts(1).toInt
            h * 60 + m
        }
        var diff = toMinutes(correct) - toMinutes(current)
        var ops = 0
        val denominations = Array(60, 15, 5, 1)
        for (d <- denominations) {
            ops += diff / d
            diff %= d
        }
        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn convert_time(current: String, correct: String) -> i32 {
        fn to_minutes(s: &str) -> i32 {
            let mut parts = s.split(':');
            let h: i32 = parts.next().unwrap().parse().unwrap();
            let m: i32 = parts.next().unwrap().parse().unwrap();
            h * 60 + m
        }
        let mut diff = to_minutes(&correct) - to_minutes(&current);
        let mut ops = 0;
        for &step in &[60, 15, 5, 1] {
            ops += diff / step;
            diff %= step;
        }
        ops
    }
}
```

## Racket

```racket
(define/contract (convert-time current correct)
  (-> string? string? exact-integer?)
  (let* ((time-to-mins
          (lambda (s)
            (+ (* (string->number (substring s 0 2)) 60)
               (string->number (substring s 3 5)))))
         (diff (- (time-to-mins correct) (time-to-mins current))))
    (let loop ((ops (list 60 15 5 1))
               (remaining diff)
               (cnt 0))
      (if (null? ops)
          cnt
          (let* ((op (car ops))
                 (q (quotient remaining op))
                 (r (remainder remaining op)))
            (loop (cdr ops) r (+ cnt q)))))))
```

## Erlang

```erlang
-module(solution).
-export([convert_time/2]).

-spec convert_time(Current :: unicode:unicode_binary(), Correct :: unicode:unicode_binary()) -> integer().
convert_time(Current, Correct) ->
    Curr = time_to_minutes(Current),
    Corr = time_to_minutes(Correct),
    Diff = Corr - Curr,
    Ops60 = Diff div 60,
    Rem1 = Diff rem 60,
    Ops15 = Rem1 div 15,
    Rem2 = Rem1 rem 15,
    Ops5 = Rem2 div 5,
    Rem3 = Rem2 rem 5,
    Ops60 + Ops15 + Ops5 + Rem3.

time_to_minutes(<<H1, H2, $:, M1, M2>>) ->
    ((H1 - $0) * 10 + (H2 - $0)) * 60 +
    ((M1 - $0) * 10 + (M2 - $0)).
```

## Elixir

```elixir
defmodule Solution do
  @spec convert_time(current :: String.t(), correct :: String.t()) :: integer()
  def convert_time(current, correct) do
    diff = to_minutes(correct) - to_minutes(current)

    {count, _} =
      Enum.reduce([60, 15, 5, 1], {0, diff}, fn coin, {cnt, rem} ->
        add = div(rem, coin)
        {cnt + add, rem - add * coin}
      end)

    count
  end

  defp to_minutes(time) do
    [h, m] = String.split(time, ":")
    String.to_integer(h) * 60 + String.to_integer(m)
  end
end
```
