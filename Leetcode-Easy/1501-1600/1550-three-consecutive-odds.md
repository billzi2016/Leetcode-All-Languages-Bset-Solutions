# 1550. Three Consecutive Odds

## Cpp

```cpp
class Solution {
public:
    bool threeConsecutiveOdds(std::vector<int>& arr) {
        int cnt = 0;
        for (int num : arr) {
            if (num % 2 != 0) {
                ++cnt;
                if (cnt == 3) return true;
            } else {
                cnt = 0;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int consecutive = 0;
        for (int num : arr) {
            if ((num & 1) == 1) {
                consecutive++;
                if (consecutive == 3) return true;
            } else {
                consecutive = 0;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        consecutive = 0
        for num in arr:
            if num & 1:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0
        return False
```

## Python3

```python
class Solution:
    def threeConsecutiveOdds(self, arr):
        consecutive = 0
        for num in arr:
            if num % 2 == 1:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0
        return False
```

## C

```c
#include <stdbool.h>

bool threeConsecutiveOdds(int* arr, int arrSize) {
    int consecutive = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (arr[i] & 1)
            ++consecutive;
        else
            consecutive = 0;
        if (consecutive == 3)
            return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool ThreeConsecutiveOdds(int[] arr) {
        int consecutive = 0;
        foreach (int num in arr) {
            if ((num & 1) == 1) {
                consecutive++;
                if (consecutive == 3) return true;
            } else {
                consecutive = 0;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    let consecutive = 0;
    for (const num of arr) {
        if (num % 2 !== 0) {
            consecutive++;
            if (consecutive === 3) return true;
        } else {
            consecutive = 0;
        }
    }
    return false;
};
```

## Typescript

```typescript
function threeConsecutiveOdds(arr: number[]): boolean {
    let consecutive = 0;
    for (const num of arr) {
        if (num % 2 !== 0) {
            consecutive++;
            if (consecutive === 3) return true;
        } else {
            consecutive = 0;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function threeConsecutiveOdds($arr) {
        $consecutive = 0;
        foreach ($arr as $num) {
            if ($num % 2 !== 0) {
                $consecutive++;
                if ($consecutive === 3) {
                    return true;
                }
            } else {
                $consecutive = 0;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func threeConsecutiveOdds(_ arr: [Int]) -> Bool {
        var consecutive = 0
        for num in arr {
            if num % 2 != 0 {
                consecutive += 1
                if consecutive == 3 { return true }
            } else {
                consecutive = 0
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun threeConsecutiveOdds(arr: IntArray): Boolean {
        var consecutive = 0
        for (num in arr) {
            if (num % 2 != 0) {
                consecutive++
                if (consecutive == 3) return true
            } else {
                consecutive = 0
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool threeConsecutiveOdds(List<int> arr) {
    int consecutive = 0;
    for (int num in arr) {
      if (num.isOdd) {
        consecutive++;
        if (consecutive == 3) return true;
      } else {
        consecutive = 0;
      }
    }
    return false;
  }
}
```

## Golang

```go
func threeConsecutiveOdds(arr []int) bool {
    consecutive := 0
    for _, v := range arr {
        if v%2 != 0 {
            consecutive++
            if consecutive == 3 {
                return true
            }
        } else {
            consecutive = 0
        }
    }
    return false
}
```

## Ruby

```ruby
def three_consecutive_odds(arr)
  consecutive = 0
  arr.each do |num|
    if num.odd?
      consecutive += 1
      return true if consecutive == 3
    else
      consecutive = 0
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def threeConsecutiveOdds(arr: Array[Int]): Boolean = {
        var consecutive = 0
        for (num <- arr) {
            if ((num & 1) == 1) {
                consecutive += 1
                if (consecutive >= 3) return true
            } else {
                consecutive = 0
            }
        }
        false
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        let mut consecutive = 0;
        for num in arr {
            if num & 1 == 1 {
                consecutive += 1;
                if consecutive == 3 {
                    return true;
                }
            } else {
                consecutive = 0;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (three-consecutive-odds arr)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst arr) (cnt 0))
    (cond
      [(null? lst) #f]
      [else
       (if (odd? (car lst))
           (let ((newcnt (+ cnt 1)))
             (if (= newcnt 3)
                 #t
                 (loop (cdr lst) newcnt)))
           (loop (cdr lst) 0))])))
```

## Erlang

```erlang
-spec three_consecutive_odds(Arr :: [integer()]) -> boolean().
three_consecutive_odds(Arr) ->
    three_consecutive_odds(Arr, 0).

three_consecutive_odds([], _) -> false;
three_consecutive_odds([H|T], Count) ->
    NewCount = case H rem 2 of
        1 -> Count + 1;
        _ -> 0
    end,
    if NewCount >= 3 ->
            true;
       true ->
            three_consecutive_odds(T, NewCount)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec three_consecutive_odds(arr :: [integer]) :: boolean
  def three_consecutive_odds(arr) do
    arr
    |> Enum.chunk_every(3, 1, :discard)
    |> Enum.any?(fn [a, b, c] ->
      rem(a, 2) == 1 and rem(b, 2) == 1 and rem(c, 2) == 1
    end)
  end
end
```
