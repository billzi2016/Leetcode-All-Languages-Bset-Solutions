# 2469. Convert the Temperature

## Cpp

```cpp
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
        return {kelvin, fahrenheit};
    }
};
```

## Java

```java
class Solution {
    public double[] convertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
        return new double[]{kelvin, fahrenheit};
    }
}
```

## Python

```python
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 9.0 / 5.0 + 32.0
        return [kelvin, fahrenheit]
```

## Python3

```python
from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 9 / 5 + 32
        return [kelvin, fahrenheit]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    double* ans = (double*)malloc(2 * sizeof(double));
    if (!ans) {
        *returnSize = 0;
        return NULL;
    }
    ans[0] = celsius + 273.15;               // Kelvin
    ans[1] = celsius * 9.0 / 5.0 + 32.0;      // Fahrenheit
    *returnSize = 2;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public double[] ConvertTemperature(double celsius) {
        double kelvin = celsius + 273.15;
        double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
        return new double[] { kelvin, fahrenheit };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
    const kelvin = celsius + 273.15;
    const fahrenheit = celsius * 9 / 5 + 32;
    return [kelvin, fahrenheit];
};
```

## Typescript

```typescript
function convertTemperature(celsius: number): number[] {
    const kelvin = celsius + 273.15;
    const fahrenheit = celsius * 9 / 5 + 32;
    return [kelvin, fahrenheit];
}
```

## Php

```php
class Solution {

    /**
     * @param Float $celsius
     * @return Float[]
     */
    function convertTemperature($celsius) {
        $kelvin = $celsius + 273.15;
        $fahrenheit = $celsius * 9 / 5 + 32;
        return [$kelvin, $fahrenheit];
    }
}
```

## Swift

```swift
class Solution {
    func convertTemperature(_ celsius: Double) -> [Double] {
        let kelvin = celsius + 273.15
        let fahrenheit = celsius * 9.0 / 5.0 + 32.0
        return [kelvin, fahrenheit]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun convertTemperature(celsius: Double): DoubleArray {
        val kelvin = celsius + 273.15
        val fahrenheit = celsius * 9.0 / 5.0 + 32.0
        return doubleArrayOf(kelvin, fahrenheit)
    }
}
```

## Dart

```dart
class Solution {
  List<double> convertTemperature(double celsius) {
    double kelvin = celsius + 273.15;
    double fahrenheit = celsius * 9 / 5 + 32;
    return [kelvin, fahrenheit];
  }
}
```

## Golang

```go
func convertTemperature(celsius float64) []float64 {
	kelvin := celsius + 273.15
	fahrenheit := celsius*9/5 + 32
	return []float64{kelvin, fahrenheit}
}
```

## Ruby

```ruby
# @param {Float} celsius
# @return {Float[]}
def convert_temperature(celsius)
  kelvin = celsius + 273.15
  fahrenheit = celsius * 9.0 / 5.0 + 32.0
  [kelvin, fahrenheit]
end
```

## Scala

```scala
object Solution {
    def convertTemperature(celsius: Double): Array[Double] = {
        val kelvin = celsius + 273.15
        val fahrenheit = celsius * 9.0 / 5.0 + 32.0
        Array(kelvin, fahrenheit)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let kelvin = celsius + 273.15;
        let fahrenheit = celsius * 9.0 / 5.0 + 32.0;
        vec![kelvin, fahrenheit]
    }
}
```

## Racket

```racket
(define/contract (convert-temperature celsius)
  (-> flonum? (listof flonum?))
  (let* ([kelvin (+ celsius 273.15)]
         [fahrenheit (+ (* celsius (/ 9.0 5.0)) 32.0)])
    (list kelvin fahrenheit)))
```

## Erlang

```erlang
-module(solution).
-export([convert_temperature/1]).

-spec convert_temperature(Celsius :: float()) -> [float()].
convert_temperature(Celsius) ->
    Kelvin = Celsius + 273.15,
    Fahrenheit = Celsius * 9.0 / 5.0 + 32.0,
    [Kelvin, Fahrenheit].
```

## Elixir

```elixir
defmodule Solution do
  @spec convert_temperature(celsius :: float) :: [float]
  def convert_temperature(celsius) do
    kelvin = celsius + 273.15
    fahrenheit = celsius * 9.0 / 5.0 + 32.0
    [kelvin, fahrenheit]
  end
end
```
