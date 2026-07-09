# 2303. Calculate Amount Paid in Taxes

## Cpp

```cpp
class Solution {
public:
    double calculateTax(vector<vector<int>>& brackets, int income) {
        double tax = 0.0;
        int prev = 0;
        for (const auto& b : brackets) {
            int upper = b[0];
            int percent = b[1];
            if (income <= prev) break;
            int taxable = min(income, upper) - prev;
            tax += taxable * percent / 100.0;
            prev = upper;
        }
        return tax;
    }
};
```

## Java

```java
class Solution {
    public double calculateTax(int[][] brackets, int income) {
        double tax = 0.0;
        int prevUpper = 0;
        for (int[] bracket : brackets) {
            int upper = bracket[0];
            int percent = bracket[1];
            if (income <= prevUpper) {
                break;
            }
            int taxable = Math.min(income, upper) - prevUpper;
            tax += taxable * percent / 100.0;
            prevUpper = upper;
        }
        return tax;
    }
}
```

## Python

```python
class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = min(income, upper) - prev
            tax += taxable * percent / 100.0
            prev = upper
        return tax
```

## Python3

```python
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev = 0
        for upper, percent in brackets:
            if income <= prev:
                break
            taxable = min(income, upper) - prev
            tax += taxable * percent / 100.0
            prev = upper
        return tax
```

## C

```c
double calculateTax(int** brackets, int bracketsSize, int* bracketsColSize, int income) {
    double tax = 0.0;
    int prev = 0;
    for (int i = 0; i < bracketsSize && income > prev; ++i) {
        int upper = brackets[i][0];
        int percent = brackets[i][1];
        int taxable = (income < upper ? income : upper) - prev;
        if (taxable > 0) {
            tax += taxable * (percent / 100.0);
        }
        prev = upper;
    }
    return tax;
}
```

## Csharp

```csharp
public class Solution {
    public double CalculateTax(int[][] brackets, int income) {
        double tax = 0.0;
        int prev = 0;
        foreach (var bracket in brackets) {
            int upper = bracket[0];
            int percent = bracket[1];
            if (income <= prev) break;
            int taxable = Math.Min(income, upper) - prev;
            tax += taxable * percent / 100.0;
            prev = upper;
        }
        return tax;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
var calculateTax = function(brackets, income) {
    let prev = 0;
    let tax = 0;
    for (const [upper, percent] of brackets) {
        if (income <= prev) break;
        const taxable = Math.min(income, upper) - prev;
        tax += taxable * percent / 100;
        prev = upper;
    }
    return tax;
};
```

## Typescript

```typescript
function calculateTax(brackets: number[][], income: number): number {
    let tax = 0;
    let prev = 0;
    for (const [upper, percent] of brackets) {
        if (income <= prev) break;
        const taxable = Math.min(income, upper) - prev;
        tax += taxable * (percent / 100);
        prev = upper;
        if (income <= upper) break;
    }
    return tax;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $brackets
     * @param Integer $income
     * @return Float
     */
    function calculateTax($brackets, $income) {
        $prev = 0;
        $tax = 0.0;
        foreach ($brackets as $b) {
            $upper = $b[0];
            $percent = $b[1];
            if ($income <= $prev) {
                break;
            }
            $taxable = min($income, $upper) - $prev;
            if ($taxable > 0) {
                $tax += $taxable * $percent / 100.0;
            }
            $prev = $upper;
        }
        return $tax;
    }
}
```

## Swift

```swift
class Solution {
    func calculateTax(_ brackets: [[Int]], _ income: Int) -> Double {
        var prev = 0
        var tax: Double = 0.0
        for bracket in brackets {
            let upper = bracket[0]
            let percent = bracket[1]
            if income <= prev { break }
            let taxable = min(income, upper) - prev
            tax += Double(taxable) * Double(percent) / 100.0
            prev = upper
        }
        return tax
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculateTax(brackets: Array<IntArray>, income: Int): Double {
        var tax = 0.0
        var prev = 0
        for (bracket in brackets) {
            val upper = bracket[0]
            val percent = bracket[1]
            if (income <= prev) break
            val taxable = minOf(income, upper) - prev
            tax += taxable * percent / 100.0
            prev = upper
        }
        return tax
    }
}
```

## Dart

```dart
class Solution {
  double calculateTax(List<List<int>> brackets, int income) {
    double tax = 0.0;
    int prev = 0;
    for (var bracket in brackets) {
      if (income <= prev) break;
      int upper = bracket[0];
      int percent = bracket[1];
      int taxable = (income < upper ? income : upper) - prev;
      tax += taxable * percent / 100.0;
      prev = upper;
    }
    return tax;
  }
}
```

## Golang

```go
func calculateTax(brackets [][]int, income int) float64 {
	prev := 0
	tax := 0.0
	for _, b := range brackets {
		if income <= prev {
			break
		}
		upper, percent := b[0], b[1]
		amt := min(income, upper) - prev
		tax += float64(amt) * float64(percent) / 100.0
		prev = upper
	}
	return tax
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def calculate_tax(brackets, income)
  tax = 0.0
  prev = 0
  brackets.each do |upper, percent|
    break if income <= prev
    taxable = [income, upper].min - prev
    tax += taxable * percent / 100.0
    prev = upper
  end
  tax
end
```

## Scala

```scala
object Solution {
    def calculateTax(brackets: Array[Array[Int]], income: Int): Double = {
        var tax = 0.0
        var prev = 0
        for (b <- brackets) {
            val upper = b(0)
            val percent = b(1)
            if (income > prev) {
                val taxable = math.min(income, upper) - prev
                tax += taxable * percent / 100.0
                prev = upper
            }
        }
        tax
    }
}
```

## Rust

```rust
impl Solution {
    pub fn calculate_tax(brackets: Vec<Vec<i32>>, income: i32) -> f64 {
        let mut tax = 0f64;
        let mut prev = 0i32;
        for b in brackets.iter() {
            if income <= prev {
                break;
            }
            let upper = b[0];
            let percent = b[1];
            let taxable = (std::cmp::min(income, upper) - prev).max(0);
            tax += taxable as f64 * percent as f64 / 100.0;
            prev = upper;
        }
        tax
    }
}
```

## Racket

```racket
(define/contract (calculate-tax brackets income)
  (-> (listof (listof exact-integer?)) exact-integer? flonum?)
  (let loop ((remaining brackets) (prev 0) (tax 0.0))
    (if (null? remaining)
        tax
        (let* ((pair (first remaining))
               (upper (first pair))
               (percent (second pair))
               (amount (max 0 (- (min income upper) prev))))
          (if (= amount 0)
              tax
              (loop (rest remaining)
                    upper
                    (+ tax (* (/ percent 100.0) amount))))))))
```

## Erlang

```erlang
-module(solution).
-export([calculate_tax/2]).

-spec calculate_tax(Brackets :: [[integer()]], Income :: integer()) -> float().
calculate_tax(Brackets, Income) ->
    calc(Brackets, Income, 0, 0.0).

calc([], _Income, _Prev, Tax) -> 
    Tax;
calc([[Upper, Percent]|Rest], Income, Prev, Tax) when Income =< Prev ->
    Tax;
calc([[Upper, Percent]|Rest], Income, Prev, Tax) ->
    Taxable = min(Income, Upper) - Prev,
    NewTax = Tax + (Taxable * Percent) / 100.0,
    calc(Rest, Income, Upper, NewTax).
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate_tax(brackets :: [[integer]], income :: integer) :: float
  def calculate_tax(brackets, income) do
    {_last_upper, tax} =
      Enum.reduce_while(brackets, {0, 0.0}, fn [upper, percent], {prev, acc} ->
        if income <= prev do
          {:halt, {prev, acc}}
        else
          taxable = min(income, upper) - prev
          added = taxable * percent / 100.0
          new_acc = acc + added

          if income <= upper do
            {:halt, {upper, new_acc}}
          else
            {:cont, {upper, new_acc}}
          end
        end
      end)

    tax
  end
end
```
