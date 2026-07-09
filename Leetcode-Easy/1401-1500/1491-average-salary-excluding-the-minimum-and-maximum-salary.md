# 1491. Average Salary Excluding the Minimum and Maximum Salary

## Cpp

```cpp
class Solution {
public:
    double average(vector<int>& salary) {
        long long total = 0;
        int mn = salary[0], mx = salary[0];
        for (int s : salary) {
            total += s;
            if (s < mn) mn = s;
            if (s > mx) mx = s;
        }
        return static_cast<double>(total - mn - mx) / (salary.size() - 2);
    }
};
```

## Java

```java
class Solution {
    public double average(int[] salary) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        long sum = 0L;
        for (int s : salary) {
            sum += s;
            if (s < min) min = s;
            if (s > max) max = s;
        }
        return (double)(sum - min - max) / (salary.length - 2);
    }
}
```

## Python

```python
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary)
        mn = min(salary)
        mx = max(salary)
        return (total - mn - mx) / (len(salary) - 2)
```

## Python3

```python
from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)
        mn = min(salary)
        mx = max(salary)
        return (total - mn - mx) / (len(salary) - 2)
```

## C

```c
double average(int* salary, int salarySize) {
    long long sum = 0;
    int mn = salary[0], mx = salary[0];
    for (int i = 0; i < salarySize; ++i) {
        int val = salary[i];
        sum += val;
        if (val < mn) mn = val;
        if (val > mx) mx = val;
    }
    return ((double)(sum - mn - mx)) / (salarySize - 2);
}
```

## Csharp

```csharp
public class Solution {
    public double Average(int[] salary) {
        int min = salary[0];
        int max = salary[0];
        long sum = 0;
        foreach (int s in salary) {
            if (s < min) min = s;
            if (s > max) max = s;
            sum += s;
        }
        double result = (double)(sum - min - max) / (salary.Length - 2);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    let sum = 0, min = Infinity, max = -Infinity;
    for (const s of salary) {
        sum += s;
        if (s < min) min = s;
        if (s > max) max = s;
    }
    return (sum - min - max) / (salary.length - 2);
};
```

## Typescript

```typescript
function average(salary: number[]): number {
    let total = 0;
    let min = Number.POSITIVE_INFINITY;
    let max = Number.NEGATIVE_INFINITY;
    for (const s of salary) {
        total += s;
        if (s < min) min = s;
        if (s > max) max = s;
    }
    return (total - min - max) / (salary.length - 2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $salary
     * @return Float
     */
    function average($salary) {
        $total = array_sum($salary);
        $min = min($salary);
        $max = max($salary);
        return ($total - $min - $max) / (count($salary) - 2);
    }
}
```

## Swift

```swift
class Solution {
    func average(_ salary: [Int]) -> Double {
        var total = 0
        var minSalary = salary[0]
        var maxSalary = salary[0]
        for s in salary {
            total += s
            if s < minSalary { minSalary = s }
            if s > maxSalary { maxSalary = s }
        }
        let adjustedSum = total - minSalary - maxSalary
        return Double(adjustedSum) / Double(salary.count - 2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun average(salary: IntArray): Double {
        var sum = 0L
        var minVal = salary[0]
        var maxVal = salary[0]
        for (s in salary) {
            sum += s
            if (s < minVal) minVal = s
            if (s > maxVal) maxVal = s
        }
        val adjustedSum = sum - minVal - maxVal
        return adjustedSum.toDouble() / (salary.size - 2)
    }
}
```

## Dart

```dart
class Solution {
  double average(List<int> salary) {
    int sum = 0;
    int min = salary[0];
    int max = salary[0];
    for (int s in salary) {
      sum += s;
      if (s < min) min = s;
      if (s > max) max = s;
    }
    return (sum - min - max) / (salary.length - 2);
  }
}
```

## Golang

```go
func average(salary []int) float64 {
    sum, min, max := 0, salary[0], salary[0]
    for _, v := range salary {
        sum += v
        if v < min {
            min = v
        }
        if v > max {
            max = v
        }
    }
    return float64(sum-min-max) / float64(len(salary)-2)
}
```

## Ruby

```ruby
def average(salary)
  total = salary.sum
  min_salary = salary.min
  max_salary = salary.max
  (total - min_salary - max_salary).to_f / (salary.length - 2)
end
```

## Scala

```scala
object Solution {
    def average(salary: Array[Int]): Double = {
        val total = salary.foldLeft(0L)(_ + _)
        val minVal = salary.min
        val maxVal = salary.max
        (total - minVal - maxVal).toDouble / (salary.length - 2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let mut sum: i64 = 0;
        let mut min = i32::MAX;
        let mut max = i32::MIN;
        for &s in &salary {
            sum += s as i64;
            if s < min { min = s; }
            if s > max { max = s; }
        }
        (sum - min as i64 - max as i64) as f64 / ((salary.len() - 2) as f64)
    }
}
```

## Racket

```racket
(define/contract (average salary)
  (-> (listof exact-integer?) flonum?)
  (let* ((total (apply + salary))
         (mn (apply min salary))
         (mx (apply max salary))
         (cnt (- (length salary) 2))
         (avg (/ (- total mn mx) cnt)))
    (exact->inexact avg)))
```

## Erlang

```erlang
-spec average(Salary :: [integer()]) -> float().
average(Salary) ->
    Min = lists:min(Salary),
    Max = lists:max(Salary),
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Salary),
    Count = length(Salary) - 2,
    (Sum - Min - Max) / Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec average(salary :: [integer]) :: float
  def average(salary) do
    total = Enum.sum(salary)
    min_salary = Enum.min(salary)
    max_salary = Enum.max(salary)
    (total - min_salary - max_salary) / (length(salary) - 2)
  end
end
```
