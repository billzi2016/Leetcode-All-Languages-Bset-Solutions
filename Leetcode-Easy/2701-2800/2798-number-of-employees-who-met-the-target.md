# 2798. Number of Employees Who Met the Target

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int count = 0;
        for (int h : hours) {
            if (h >= target) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int count = 0;
        for (int h : hours) {
            if (h >= target) {
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
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for h in hours:
            if h >= target:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for h in hours:
            if h >= target:
                count += 1
        return count
```

## C

```c
int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    int count = 0;
    for (int i = 0; i < hoursSize; ++i) {
        if (hours[i] >= target) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target)
    {
        int count = 0;
        foreach (int h in hours)
        {
            if (h >= target) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    let count = 0;
    for (const h of hours) {
        if (h >= target) count++;
    }
    return count;
};
```

## Typescript

```typescript
function numberOfEmployeesWhoMetTarget(hours: number[], target: number): number {
    let count = 0;
    for (const h of hours) {
        if (h >= target) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @param Integer $target
     * @return Integer
     */
    function numberOfEmployeesWhoMetTarget($hours, $target) {
        $count = 0;
        foreach ($hours as $h) {
            if ($h >= $target) {
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
    func numberOfEmployeesWhoMetTarget(_ hours: [Int], _ target: Int) -> Int {
        var count = 0
        for h in hours {
            if h >= target {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfEmployeesWhoMetTarget(hours: IntArray, target: Int): Int {
        var count = 0
        for (h in hours) {
            if (h >= target) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfEmployeesWhoMetTarget(List<int> hours, int target) {
    int count = 0;
    for (int h in hours) {
      if (h >= target) count++;
    }
    return count;
  }
}
```

## Golang

```go
func numberOfEmployeesWhoMetTarget(hours []int, target int) int {
    count := 0
    for _, h := range hours {
        if h >= target {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def number_of_employees_who_met_target(hours, target)
  count = 0
  hours.each { |h| count += 1 if h >= target }
  count
end
```

## Scala

```scala
object Solution {
    def numberOfEmployeesWhoMetTarget(hours: Array[Int], target: Int): Int = {
        var count = 0
        for (h <- hours) {
            if (h >= target) count += 1
        }
        count
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn number_of_employees_who_met_target(hours: Vec<i32>, target: i32) -> i32 {
        hours.iter().filter(|&&h| h >= target).count() as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-employees-who-met-target hours target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (length (filter (lambda (h) (>= h target)) hours)))
```

## Erlang

```erlang
-spec number_of_employees_who_met_target(Hours :: [integer()], Target :: integer()) -> integer().
number_of_employees_who_met_target(Hours, Target) ->
    length([H || H <- Hours, H >= Target]).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_employees_who_met_target(hours :: [integer], target :: integer) :: integer
  def number_of_employees_who_met_target(hours, target) do
    Enum.count(hours, fn h -> h >= target end)
  end
end
```
