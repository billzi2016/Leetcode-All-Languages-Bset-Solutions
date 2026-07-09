# 0860. Lemonade Change

## Cpp

```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for (int bill : bills) {
            if (bill == 5) {
                ++five;
            } else if (bill == 10) {
                if (five == 0) return false;
                --five;
                ++ten;
            } else { // bill == 20
                if (ten > 0 && five > 0) {
                    --ten;
                    --five;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int bill : bills) {
            if (bill == 5) {
                five++;
            } else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else { // bill == 20
                if (ten > 0 && five > 0) {
                    ten--;
                    five--;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```

## Python3

```python
class Solution:
    def lemonadeChange(self, bills):
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:  # b == 20
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```

## C

```c
#include <stdbool.h>

bool lemonadeChange(int* bills, int billsSize) {
    int five = 0, ten = 0;
    for (int i = 0; i < billsSize; ++i) {
        if (bills[i] == 5) {
            five++;
        } else if (bills[i] == 10) {
            if (five == 0) return false;
            five--;
            ten++;
        } else { // bill is 20
            if (ten > 0 && five > 0) {
                ten--;
                five--;
            } else if (five >= 3) {
                five -= 3;
            } else {
                return false;
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool LemonadeChange(int[] bills)
    {
        int five = 0, ten = 0;
        foreach (int bill in bills)
        {
            if (bill == 5)
            {
                five++;
            }
            else if (bill == 10)
            {
                if (five == 0) return false;
                five--;
                ten++;
            }
            else // bill == 20
            {
                if (ten > 0 && five > 0)
                {
                    ten--;
                    five--;
                }
                else if (five >= 3)
                {
                    five -= 3;
                }
                else
                {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
var lemonadeChange = function(bills) {
    let five = 0, ten = 0;
    for (const bill of bills) {
        if (bill === 5) {
            five++;
        } else if (bill === 10) {
            if (five === 0) return false;
            five--;
            ten++;
        } else { // bill === 20
            if (ten > 0 && five > 0) {
                ten--;
                five--;
            } else if (five >= 3) {
                five -= 3;
            } else {
                return false;
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function lemonadeChange(bills: number[]): boolean {
    let five = 0, ten = 0;
    for (const bill of bills) {
        if (bill === 5) {
            five++;
        } else if (bill === 10) {
            if (five === 0) return false;
            five--;
            ten++;
        } else { // bill === 20
            if (ten > 0 && five > 0) {
                ten--;
                five--;
            } else if (five >= 3) {
                five -= 3;
            } else {
                return false;
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $bills
     * @return Boolean
     */
    function lemonadeChange($bills) {
        $five = 0;
        $ten = 0;
        foreach ($bills as $bill) {
            if ($bill == 5) {
                $five++;
            } elseif ($bill == 10) {
                if ($five == 0) {
                    return false;
                }
                $five--;
                $ten++;
            } else { // bill == 20
                if ($ten > 0 && $five > 0) {
                    $ten--;
                    $five--;
                } elseif ($five >= 3) {
                    $five -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func lemonadeChange(_ bills: [Int]) -> Bool {
        var five = 0
        var ten = 0
        for bill in bills {
            if bill == 5 {
                five += 1
            } else if bill == 10 {
                if five == 0 { return false }
                five -= 1
                ten += 1
            } else { // bill == 20
                if ten > 0 && five > 0 {
                    ten -= 1
                    five -= 1
                } else if five >= 3 {
                    five -= 3
                } else {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lemonadeChange(bills: IntArray): Boolean {
        var five = 0
        var ten = 0
        for (bill in bills) {
            when (bill) {
                5 -> five++
                10 -> {
                    if (five == 0) return false
                    five--
                    ten++
                }
                20 -> {
                    if (ten > 0 && five > 0) {
                        ten--
                        five--
                    } else if (five >= 3) {
                        five -= 3
                    } else {
                        return false
                    }
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool lemonadeChange(List<int> bills) {
    int five = 0;
    int ten = 0;
    for (int bill in bills) {
      if (bill == 5) {
        five++;
      } else if (bill == 10) {
        if (five == 0) return false;
        five--;
        ten++;
      } else { // bill == 20
        if (ten > 0 && five > 0) {
          ten--;
          five--;
        } else if (five >= 3) {
          five -= 3;
        } else {
          return false;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
func lemonadeChange(bills []int) bool {
    five, ten := 0, 0
    for _, b := range bills {
        switch b {
        case 5:
            five++
        case 10:
            if five == 0 {
                return false
            }
            five--
            ten++
        case 20:
            if ten > 0 && five > 0 {
                ten--
                five--
            } else if five >= 3 {
                five -= 3
            } else {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def lemonade_change(bills)
  five = 0
  ten = 0
  bills.each do |bill|
    case bill
    when 5
      five += 1
    when 10
      return false if five == 0
      five -= 1
      ten += 1
    when 20
      if ten > 0 && five > 0
        ten -= 1
        five -= 1
      elsif five >= 3
        five -= 3
      else
        return false
      end
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def lemonadeChange(bills: Array[Int]): Boolean = {
        var five = 0
        var ten = 0
        for (b <- bills) {
            b match {
                case 5 => five += 1
                case 10 =>
                    if (five == 0) return false
                    five -= 1
                    ten += 1
                case 20 =>
                    if (ten > 0 && five > 0) {
                        ten -= 1
                        five -= 1
                    } else if (five >= 3) {
                        five -= 3
                    } else {
                        return false
                    }
                case _ => // do nothing, input guaranteed to be 5,10,20
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut five = 0;
        let mut ten = 0;
        for bill in bills {
            match bill {
                5 => five += 1,
                10 => {
                    if five == 0 {
                        return false;
                    }
                    five -= 1;
                    ten += 1;
                }
                20 => {
                    if ten > 0 && five > 0 {
                        ten -= 1;
                        five -= 1;
                    } else if five >= 3 {
                        five -= 3;
                    } else {
                        return false;
                    }
                }
                _ => {}
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (lemonade-change bills)
  (-> (listof exact-integer?) boolean?)
  (let loop ((bs bills) (five 0) (ten 0))
    (cond
      [(null? bs) #t]
      [else
       (let ((bill (car bs)))
         (cond
           [(= bill 5)
            (loop (cdr bs) (+ five 1) ten)]
           [(= bill 10)
            (if (>= five 1)
                (loop (cdr bs) (- five 1) (+ ten 1))
                #f)]
           [(= bill 20)
            (cond
              [(and (>= ten 1) (>= five 1))
               (loop (cdr bs) (- five 1) (- ten 1))]
              [(>= five 3)
               (loop (cdr bs) (- five 3) ten)]
              [else #f])]
           [else #f]))])))
```

## Erlang

```erlang
-module(solution).
-export([lemonade_change/1]).

-spec lemonade_change(Bills :: [integer()]) -> boolean().
lemonade_change(Bills) ->
    lemonade_change(Bills, 0, 0).

lemonade_change([], _Five, _Ten) ->
    true;
lemonade_change([5|Rest], Five, Ten) ->
    lemonade_change(Rest, Five + 1, Ten);
lemonade_change([10|Rest], Five, Ten) ->
    case Five >= 1 of
        true -> lemonade_change(Rest, Five - 1, Ten + 1);
        false -> false
    end;
lemonade_change([20|Rest], Five, Ten) ->
    if
        Ten >= 1 andalso Five >= 1 ->
            lemonade_change(Rest, Five - 1, Ten - 1);
        Five >= 3 ->
            lemonade_change(Rest, Five - 3, Ten);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec lemonade_change(bills :: [integer]) :: boolean
  def lemonade_change(bills), do: process(bills, 0, 0)

  defp process([], _five, _ten), do: true

  defp process([bill | rest], five, ten) do
    case bill do
      5 ->
        process(rest, five + 1, ten)

      10 ->
        if five >= 1 do
          process(rest, five - 1, ten + 1)
        else
          false
        end

      20 ->
        cond do
          ten >= 1 and five >= 1 ->
            process(rest, five - 1, ten - 1)

          five >= 3 ->
            process(rest, five - 3, ten)

          true ->
            false
        end
    end
  end
end
```
