# 0788. Rotated Digits

## Cpp

```cpp
class Solution {
public:
    int rotatedDigits(int n) {
        auto isGood = [](int x) -> bool {
            bool diff = false;
            while (x > 0) {
                int d = x % 10;
                if (d == 3 || d == 4 || d == 7) return false;
                if (d == 2 || d == 5 || d == 6 || d == 9) diff = true;
                x /= 10;
            }
            return diff;
        };
        
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            if (isGood(i)) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int rotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            int x = i;
            boolean valid = true;
            boolean diff = false;
            while (x > 0) {
                int d = x % 10;
                if (d == 3 || d == 4 || d == 7) {
                    valid = false;
                    break;
                }
                if (d == 2 || d == 5 || d == 6 || d == 9) {
                    diff = true;
                }
                x /= 10;
            }
            if (valid && diff) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        change = {'2', '5', '6', '9'}
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if all(ch in valid for ch in s) and any(ch in change for ch in s):
                count += 1
        return count
```

## Python3

```python
class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {3, 4, 7}
        change = {2, 5, 6, 9}
        cnt = 0
        for i in range(1, n + 1):
            x = i
            good = False
            while x:
                d = x % 10
                if d in invalid:
                    break
                if d in change:
                    good = True
                x //= 10
            else:
                if good:
                    cnt += 1
        return cnt
```

## C

```c
#include <stdbool.h>

int rotatedDigits(int n) {
    int count = 0;
    for (int i = 1; i <= n; ++i) {
        int x = i;
        bool good = false;
        bool valid = true;
        while (x > 0) {
            int d = x % 10;
            if (d == 3 || d == 4 || d == 7) {
                valid = false;
                break;
            }
            if (d == 2 || d == 5 || d == 6 || d == 9) {
                good = true;
            }
            x /= 10;
        }
        if (valid && good) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int RotatedDigits(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (IsGood(i)) count++;
        }
        return count;
    }

    private bool IsGood(int x) {
        bool changed = false;
        while (x > 0) {
            int d = x % 10;
            if (d == 3 || d == 4 || d == 7) return false;
            if (d == 2 || d == 5 || d == 6 || d == 9) changed = true;
            x /= 10;
        }
        return changed;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var rotatedDigits = function(n) {
    let count = 0;
    const invalid = new Set(['3', '4', '7']);
    const goodSet = new Set(['2', '5', '6', '9']);
    for (let i = 1; i <= n; ++i) {
        const s = i.toString();
        let hasInvalid = false;
        let isGood = false;
        for (const ch of s) {
            if (invalid.has(ch)) {
                hasInvalid = true;
                break;
            }
            if (goodSet.has(ch)) {
                isGood = true;
            }
        }
        if (!hasInvalid && isGood) count++;
    }
    return count;
};
```

## Typescript

```typescript
function rotatedDigits(n: number): number {
    const valid = new Set([0, 1, 2, 5, 6, 8, 9]);
    const changes = new Set([2, 5, 6, 9]);
    let ans = 0;
    for (let i = 1; i <= n; ++i) {
        let x = i;
        let ok = true;
        let changed = false;
        while (x > 0) {
            const d = x % 10;
            if (!valid.has(d)) {
                ok = false;
                break;
            }
            if (changes.has(d)) changed = true;
            x = Math.floor(x / 10);
        }
        if (ok && changed) ++ans;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function rotatedDigits($n) {
        $count = 0;
        for ($i = 1; $i <= $n; $i++) {
            $num = $i;
            $valid = true;
            $changed = false;
            while ($num > 0) {
                $digit = $num % 10;
                if ($digit == 3 || $digit == 4 || $digit == 7) {
                    $valid = false;
                    break;
                }
                if ($digit == 2 || $digit == 5 || $digit == 6 || $digit == 9) {
                    $changed = true;
                }
                $num = intdiv($num, 10);
            }
            if ($valid && $changed) {
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
    func rotatedDigits(_ n: Int) -> Int {
        var result = 0
        for i in 1...n {
            var x = i
            var hasRotatable = false
            var isValid = true
            while x > 0 {
                let digit = x % 10
                if digit == 3 || digit == 4 || digit == 7 {
                    isValid = false
                    break
                }
                if digit == 2 || digit == 5 || digit == 6 || digit == 9 {
                    hasRotatable = true
                }
                x /= 10
            }
            if isValid && hasRotatable {
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
    fun rotatedDigits(n: Int): Int {
        var count = 0
        for (i in 1..n) {
            if (isGood(i)) count++
        }
        return count
    }

    private fun isGood(x: Int): Boolean {
        var num = x
        var hasDiff = false
        while (num > 0) {
            when (num % 10) {
                3, 4, 7 -> return false
                2, 5, 6, 9 -> hasDiff = true
            }
            num /= 10
        }
        return hasDiff
    }
}
```

## Dart

```dart
class Solution {
  int rotatedDigits(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
      if (_isGood(i)) count++;
    }
    return count;
  }

  bool _isGood(int num) {
    bool changed = false;
    while (num > 0) {
      int d = num % 10;
      if (d == 3 || d == 4 || d == 7) return false;
      if (d == 2 || d == 5 || d == 6 || d == 9) changed = true;
      num ~/= 10;
    }
    return changed;
  }
}
```

## Golang

```go
func rotatedDigits(n int) int {
    count := 0
    for i := 1; i <= n; i++ {
        if isGood(i) {
            count++
        }
    }
    return count
}

func isGood(x int) bool {
    hasDiff := false
    for x > 0 {
        d := x % 10
        switch d {
        case 0, 1, 8:
            // unchanged digit
        case 2, 5, 6, 9:
            hasDiff = true
        default: // 3,4,7 are invalid
            return false
        }
        x /= 10
    }
    return hasDiff
}
```

## Ruby

```ruby
def rotated_digits(n)
  rotate = {0=>0, 1=>1, 2=>5, 5=>2, 6=>9, 8=>8, 9=>6}
  count = 0
  (1..n).each do |i|
    good = false
    valid = true
    i.to_s.each_char do |ch|
      d = ch.ord - 48
      unless rotate.key?(d)
        valid = false
        break
      end
      good ||= (rotate[d] != d)
    end
    count += 1 if valid && good
  end
  count
end
```

## Scala

```scala
object Solution {
    def rotatedDigits(n: Int): Int = {
        var count = 0
        for (i <- 1 to n) {
            if (isGood(i)) count += 1
        }
        count
    }

    private def isGood(x: Int): Boolean = {
        var num = x
        var hasDiff = false
        while (num > 0) {
            val d = num % 10
            d match {
                case 3 | 4 | 7 => return false
                case 2 | 5 | 6 | 9 => hasDiff = true
                case _ => // 0,1,8 are fine and unchanged
            }
            num /= 10
        }
        hasDiff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rotated_digits(n: i32) -> i32 {
        let mut count = 0;
        for i in 1..=n {
            let mut x = i;
            let mut valid = true;
            let mut changed = false;
            while x > 0 {
                match x % 10 {
                    0 | 1 | 8 => {}
                    2 | 5 | 6 | 9 => changed = true,
                    _ => {
                        valid = false;
                        break;
                    }
                }
                x /= 10;
            }
            if valid && changed {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (rotated-digits n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 1) (cnt 0))
    (if (> i n)
        cnt
        (loop (+ i 1) (+ cnt (if (good? i) 1 0))))))

(define (good? x)
  (let rec ((num x) (changed #f))
    (cond [(zero? num) changed]
          [else
           (let* ([d (remainder num 10)]
                  [valid? (member d '(0 1 2 5 6 8 9))]
                  [new-changed (or changed (member d '(2 5 6 9)))])
             (if (not valid?)
                 #f
                 (rec (quotient num 10) new-changed)))])))
```

## Erlang

```erlang
-module(solution).
-export([rotated_digits/1]).

-spec rotated_digits(N :: integer()) -> integer().
rotated_digits(N) when N >= 1 ->
    count_good(N, 1, 0).

count_good(N, I, Acc) when I =< N ->
    NewAcc = case is_good(I) of
        true -> Acc + 1;
        false -> Acc
    end,
    count_good(N, I + 1, NewAcc);
count_good(_, _, Acc) ->
    Acc.

is_good(Num) ->
    check_digits(Num, false).

check_digits(0, HasChanged) ->
    HasChanged;
check_digits(Num, HasChanged) ->
    Digit = Num rem 10,
    case Digit of
        3;4;7 -> false;
        _ ->
            Changed = (Digit == 2) orelse (Digit == 5) orelse (Digit == 6) orelse (Digit == 9),
            NewHasChanged = HasChanged orelse Changed,
            check_digits(Num div 10, NewHasChanged)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec rotated_digits(n :: integer) :: integer
  def rotated_digits(n) do
    rotation = %{0 => 0, 1 => 1, 2 => 5, 5 => 2, 6 => 9, 8 => 8, 9 => 6}

    Enum.reduce(1..n, 0, fn i, acc ->
      case check(i, rotation) do
        {true, true} -> acc + 1
        _ -> acc
      end
    end)
  end

  defp check(0, _map), do: {true, false}
  defp check(num, map) do
    digit = rem(num, 10)

    case Map.fetch(map, digit) do
      :error ->
        {false, false}

      {:ok, rotated} ->
        {valid_rest, changed_rest} = check(div(num, 10), map)

        if valid_rest do
          {true, changed_rest or rotated != digit}
        else
          {false, false}
        end
    end
  end
end
```
