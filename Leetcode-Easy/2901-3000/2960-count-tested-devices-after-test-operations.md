# 2960. Count Tested Devices After Test Operations

## Cpp

```cpp
class Solution {
public:
    int countTestedDevices(vector<int>& batteryPercentages) {
        int tested = 0;
        for (int i = 0; i < (int)batteryPercentages.size(); ++i) {
            if (batteryPercentages[i] > tested) {
                ++tested;
            }
        }
        return tested;
    }
};
```

## Java

```java
class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        int tested = 0;
        for (int b : batteryPercentages) {
            if (b > tested) {
                tested++;
            }
        }
        return tested;
    }
}
```

## Python

```python
class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested = 0
        for b in batteryPercentages:
            if b > tested:
                tested += 1
        return tested
```

## Python3

```python
from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for b in batteryPercentages:
            if b > tested:
                tested += 1
        return tested
```

## C

```c
int countTestedDevices(int* batteryPercentages, int batteryPercentagesSize) {
    int tested = 0;
    for (int i = 0; i < batteryPercentagesSize; ++i) {
        if (batteryPercentages[i] > tested) {
            ++tested;
        }
    }
    return tested;
}
```

## Csharp

```csharp
public class Solution {
    public int CountTestedDevices(int[] batteryPercentages) {
        int tested = 0;
        foreach (int battery in batteryPercentages) {
            if (battery > tested) {
                tested++;
            }
        }
        return tested;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} batteryPercentages
 * @return {number}
 */
var countTestedDevices = function(batteryPercentages) {
    let tested = 0;
    for (let i = 0; i < batteryPercentages.length; i++) {
        if (batteryPercentages[i] - tested > 0) {
            tested++;
        }
    }
    return tested;
};
```

## Typescript

```typescript
function countTestedDevices(batteryPercentages: number[]): number {
    let tested = 0;
    for (const battery of batteryPercentages) {
        if (battery > tested) {
            tested++;
        }
    }
    return tested;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $batteryPercentages
     * @return Integer
     */
    function countTestedDevices($batteryPercentages) {
        $tested = 0;
        foreach ($batteryPercentages as $b) {
            if ($b > $tested) {
                $tested++;
            }
        }
        return $tested;
    }
}
```

## Swift

```swift
class Solution {
    func countTestedDevices(_ batteryPercentages: [Int]) -> Int {
        var tested = 0
        for battery in batteryPercentages {
            if battery > tested {
                tested += 1
            }
        }
        return tested
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countTestedDevices(batteryPercentages: IntArray): Int {
        var tested = 0
        for (b in batteryPercentages) {
            if (b > tested) {
                tested++
            }
        }
        return tested
    }
}
```

## Dart

```dart
class Solution {
  int countTestedDevices(List<int> batteryPercentages) {
    int tested = 0;
    for (int b in batteryPercentages) {
      if (b > tested) {
        tested++;
      }
    }
    return tested;
  }
}
```

## Golang

```go
func countTestedDevices(batteryPercentages []int) int {
    tested := 0
    for _, b := range batteryPercentages {
        if b > tested {
            tested++
        }
    }
    return tested
}
```

## Ruby

```ruby
def count_tested_devices(battery_percentages)
  tested = 0
  battery_percentages.each do |b|
    tested += 1 if b > tested
  end
  tested
end
```

## Scala

```scala
object Solution {
    def countTestedDevices(batteryPercentages: Array[Int]): Int = {
        var tested = 0
        for (b <- batteryPercentages) {
            if (b > tested) {
                tested += 1
            }
        }
        tested
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_tested_devices(battery_percentages: Vec<i32>) -> i32 {
        let mut tested = 0;
        for &b in battery_percentages.iter() {
            if b > tested {
                tested += 1;
            }
        }
        tested
    }
}
```

## Racket

```racket
(define/contract (count-tested-devices batteryPercentages)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst batteryPercentages) (cnt 0))
    (if (null? lst)
        cnt
        (let ((val (car lst)))
          (if (> val cnt)
              (loop (cdr lst) (+ cnt 1))
              (loop (cdr lst) cnt))))))
```

## Erlang

```erlang
-spec count_tested_devices([integer()]) -> integer().
count_tested_devices(BatteryPercentages) ->
    count_tested_devices(BatteryPercentages, 0).

count_tested_devices([], Count) -> Count;
count_tested_devices([H|T], Count) ->
    case H > Count of
        true -> count_tested_devices(T, Count + 1);
        false -> count_tested_devices(T, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_tested_devices(battery_percentages :: [integer]) :: integer
  def count_tested_devices(battery_percentages) do
    Enum.reduce(battery_percentages, 0, fn battery, tested ->
      if battery - tested > 0, do: tested + 1, else: tested
    end)
  end
end
```
