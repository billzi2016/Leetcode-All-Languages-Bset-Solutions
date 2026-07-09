# 2483. Minimum Penalty for a Shop

## Cpp

```cpp
class Solution {
public:
    int bestClosingTime(string customers) {
        int curPenalty = 0;
        int minPenalty = 0;
        int bestHour = 0;
        for (int i = 0; i < (int)customers.size(); ++i) {
            if (customers[i] == 'Y')
                --curPenalty;
            else
                ++curPenalty;
            if (curPenalty < minPenalty) {
                minPenalty = curPenalty;
                bestHour = i + 1;
            }
        }
        return bestHour;
    }
};
```

## Java

```java
class Solution {
    public int bestClosingTime(String customers) {
        int curPenalty = 0;
        int minPenalty = 0;
        int bestHour = 0;
        for (int i = 0; i < customers.length(); i++) {
            char c = customers.charAt(i);
            if (c == 'Y') {
                curPenalty--;
            } else { // 'N'
                curPenalty++;
            }
            if (curPenalty < minPenalty) {
                minPenalty = curPenalty;
                bestHour = i + 1;
            }
        }
        return bestHour;
    }
}
```

## Python

```python
class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        cur = 0
        min_penalty = 0
        ans = 0
        for i, c in enumerate(customers):
            if c == 'Y':
                cur -= 1
            else:
                cur += 1
            if cur < min_penalty:
                min_penalty = cur
                ans = i + 1
        return ans
```

## Python3

```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur = 0
        min_penalty = 0
        earliest = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                cur -= 1
            else:
                cur += 1
            if cur < min_penalty:
                min_penalty = cur
                earliest = i + 1
        return earliest
```

## C

```c
#include <string.h>

int bestClosingTime(char* customers) {
    int curPenalty = 0;
    int minPenalty = 0;
    int earliestHour = 0;
    int n = strlen(customers);
    for (int i = 0; i < n; ++i) {
        if (customers[i] == 'Y')
            curPenalty--;
        else
            curPenalty++;
        if (curPenalty < minPenalty) {
            minPenalty = curPenalty;
            earliestHour = i + 1;
        }
    }
    return earliestHour;
}
```

## Csharp

```csharp
public class Solution
{
    public int BestClosingTime(string customers)
    {
        int curPenalty = 0;
        int minPenalty = 0;
        int bestHour = 0;

        for (int i = 0; i < customers.Length; i++)
        {
            if (customers[i] == 'Y')
                curPenalty--;
            else // 'N'
                curPenalty++;

            if (curPenalty < minPenalty)
            {
                minPenalty = curPenalty;
                bestHour = i + 1;
            }
        }

        return bestHour;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function(customers) {
    let curPenalty = 0;
    let minPenalty = 0;
    let earliestHour = 0;
    
    for (let i = 0; i < customers.length; i++) {
        if (customers[i] === 'Y') {
            curPenalty -= 1;
        } else { // 'N'
            curPenalty += 1;
        }
        if (curPenalty < minPenalty) {
            minPenalty = curPenalty;
            earliestHour = i + 1;
        }
    }
    
    return earliestHour;
};
```

## Typescript

```typescript
function bestClosingTime(customers: string): number {
    let curPenalty = 0;
    let minPenalty = 0;
    let earliestHour = 0;
    for (let i = 0; i < customers.length; i++) {
        if (customers[i] === 'Y') {
            curPenalty--;
        } else {
            curPenalty++;
        }
        if (curPenalty < minPenalty) {
            minPenalty = curPenalty;
            earliestHour = i + 1;
        }
    }
    return earliestHour;
}
```

## Php

```php
class Solution {

    /**
     * @param String $customers
     * @return Integer
     */
    function bestClosingTime($customers) {
        $curPenalty = 0;
        $minPenalty = 0;
        $bestHour = 0;
        $n = strlen($customers);
        for ($i = 0; $i < $n; $i++) {
            if ($customers[$i] === 'Y') {
                $curPenalty--;
            } else { // 'N'
                $curPenalty++;
            }
            if ($curPenalty < $minPenalty) {
                $minPenalty = $curPenalty;
                $bestHour = $i + 1;
            }
        }
        return $bestHour;
    }
}
```

## Swift

```swift
class Solution {
    func bestClosingTime(_ customers: String) -> Int {
        var curPenalty = 0
        var minPenalty = 0
        var earliestHour = 0
        
        for (i, ch) in customers.enumerated() {
            if ch == "Y" {
                curPenalty -= 1
            } else { // 'N'
                curPenalty += 1
            }
            if curPenalty < minPenalty {
                minPenalty = curPenalty
                earliestHour = i + 1
            }
        }
        return earliestHour
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bestClosingTime(customers: String): Int {
        var curPenalty = 0
        var minPenalty = 0
        var earliestHour = 0
        for (i in customers.indices) {
            if (customers[i] == 'Y') {
                curPenalty--
            } else {
                curPenalty++
            }
            if (curPenalty < minPenalty) {
                minPenalty = curPenalty
                earliestHour = i + 1
            }
        }
        return earliestHour
    }
}
```

## Dart

```dart
class Solution {
  int bestClosingTime(String customers) {
    int curPenalty = 0;
    int minPenalty = 0;
    int earliestHour = 0;
    for (int i = 0; i < customers.length; i++) {
      if (customers.codeUnitAt(i) == 89) { // 'Y'
        curPenalty--;
      } else { // 'N'
        curPenalty++;
      }
      if (curPenalty < minPenalty) {
        minPenalty = curPenalty;
        earliestHour = i + 1;
      }
    }
    return earliestHour;
  }
}
```

## Golang

```go
func bestClosingTime(customers string) int {
    curPenalty, minPenalty := 0, 0
    bestHour := 0
    for i, c := range customers {
        if c == 'Y' {
            curPenalty--
        } else { // c == 'N'
            curPenalty++
        }
        if curPenalty < minPenalty {
            minPenalty = curPenalty
            bestHour = i + 1
        }
    }
    return bestHour
}
```

## Ruby

```ruby
def best_closing_time(customers)
  cur_penalty = 0
  min_penalty = 0
  earliest_hour = 0

  customers.each_char.with_index do |ch, i|
    if ch == 'Y'
      cur_penalty -= 1
    else
      cur_penalty += 1
    end

    if cur_penalty < min_penalty
      min_penalty = cur_penalty
      earliest_hour = i + 1
    end
  end

  earliest_hour
end
```

## Scala

```scala
object Solution {
    def bestClosingTime(customers: String): Int = {
        var curPenalty = 0
        var minPenalty = 0
        var earliestHour = 0
        var i = 0
        val n = customers.length
        while (i < n) {
            if (customers.charAt(i) == 'Y') curPenalty -= 1 else curPenalty += 1
            if (curPenalty < minPenalty) {
                minPenalty = curPenalty
                earliestHour = i + 1
            }
            i += 1
        }
        earliestHour
    }
}
```

## Rust

```rust
impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let mut cur = 0i32;
        let mut min_penalty = 0i32;
        let mut earliest = 0i32;

        for (i, ch) in customers.bytes().enumerate() {
            if ch == b'Y' {
                cur -= 1;
            } else { // 'N'
                cur += 1;
            }
            if cur < min_penalty {
                min_penalty = cur;
                earliest = i as i32 + 1;
            }
        }

        earliest
    }
}
```

## Racket

```racket
(define/contract (best-closing-time customers)
  (-> string? exact-integer?)
  (let ((n (string-length customers)))
    (let loop ((i 0) (cur 0) (min-pen 0) (ans 0))
      (if (= i n)
          ans
          (let* ((c (string-ref customers i))
                 (new-cur (if (char=? c #\Y) (- cur 1) (+ cur 1))))
            (if (< new-cur min-pen)
                (loop (+ i 1) new-cur new-cur (+ i 1))
                (loop (+ i 1) new-cur min-pen ans)))))))
```

## Erlang

```erlang
-spec best_closing_time(Customers :: unicode:unicode_binary()) -> integer().
best_closing_time(Customers) ->
    loop(Customers, 0, 0, 0, 0).

loop(<<>>, _Idx, _Cur, _Min, Ans) ->
    Ans;
loop(<<C, Rest/binary>>, Idx, Cur, Min, Ans) ->
    NewCur = case C of
        $Y -> Cur - 1;
        $N -> Cur + 1
    end,
    {NewMin, NewAns} =
        if NewCur < Min ->
                {NewCur, Idx + 1};
           true ->
                {Min, Ans}
        end,
    loop(Rest, Idx + 1, NewCur, NewMin, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec best_closing_time(customers :: String.t()) :: integer()
  def best_closing_time(customers) do
    chars = String.to_charlist(customers)

    {best_hour, _cur, _min} =
      Enum.reduce(Enum.with_index(chars), {0, 0, 0}, fn {ch, idx},
                                                    {best, cur, min} ->
        new_cur = if ch == ?Y, do: cur - 1, else: cur + 1

        if new_cur < min do
          {idx + 1, new_cur, new_cur}
        else
          {best, new_cur, min}
        end
      end)

    best_hour
  end
end
```
