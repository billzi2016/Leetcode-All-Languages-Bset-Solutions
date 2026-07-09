# 1701. Average Waiting Time

## Cpp

```cpp
class Solution {
public:
    double averageWaitingTime(std::vector<std::vector<int>>& customers) {
        long long cur = 0;
        long long total = 0;
        for (const auto& c : customers) {
            int arrive = c[0];
            int dur = c[1];
            if (cur < arrive) cur = arrive + dur;
            else cur += dur;
            total += cur - arrive;
        }
        return static_cast<double>(total) / customers.size();
    }
};
```

## Java

```java
class Solution {
    public double averageWaitingTime(int[][] customers) {
        long totalWait = 0L;
        int currentTime = 0;
        for (int[] customer : customers) {
            int arrival = customer[0];
            int prep = customer[1];
            if (currentTime < arrival) {
                currentTime = arrival;
            }
            currentTime += prep;
            totalWait += (long) (currentTime - arrival);
        }
        return (double) totalWait / customers.length;
    }
}
```

## Python

```python
class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        cur_time = 0
        total_wait = 0
        for arrive, prep in customers:
            if cur_time < arrive:
                cur_time = arrive + prep
            else:
                cur_time += prep
            total_wait += cur_time - arrive
        return total_wait / len(customers)
```

## Python3

```python
class Solution:
    def averageWaitingTime(self, customers):
        cur_time = 0
        total_wait = 0
        for arrive, prep in customers:
            if cur_time < arrive:
                cur_time = arrive
            cur_time += prep
            total_wait += cur_time - arrive
        return total_wait / len(customers)
```

## C

```c
double averageWaitingTime(int** customers, int customersSize, int* customersColSize) {
    long long totalWait = 0;
    long long currentTime = 0;
    for (int i = 0; i < customersSize; ++i) {
        int arrive = customers[i][0];
        int prep   = customers[i][1];
        if (currentTime < arrive) {
            currentTime = arrive;
        }
        currentTime += prep;
        totalWait += currentTime - arrive;
    }
    return (double)totalWait / customersSize;
}
```

## Csharp

```csharp
public class Solution
{
    public double AverageWaitingTime(int[][] customers)
    {
        long currentTime = 0;
        long totalWait = 0;

        foreach (var customer in customers)
        {
            int arrival = customer[0];
            int prep = customer[1];

            if (currentTime < arrival)
                currentTime = arrival;

            currentTime += prep;
            totalWait += currentTime - arrival;
        }

        return (double)totalWait / customers.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} customers
 * @return {number}
 */
var averageWaitingTime = function(customers) {
    let currentTime = 0;
    let totalWait = 0;
    for (const [arrival, prep] of customers) {
        if (currentTime < arrival) {
            currentTime = arrival;
        }
        currentTime += prep;
        totalWait += currentTime - arrival;
    }
    return totalWait / customers.length;
};
```

## Typescript

```typescript
function averageWaitingTime(customers: number[][]): number {
    let currentTime = 0;
    let totalWait = 0;
    for (const [arrival, prep] of customers) {
        if (currentTime < arrival) {
            currentTime = arrival + prep;
        } else {
            currentTime += prep;
        }
        totalWait += currentTime - arrival;
    }
    return totalWait / customers.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $customers
     * @return Float
     */
    function averageWaitingTime($customers) {
        $curr = 0;
        $total = 0;
        foreach ($customers as $c) {
            $arrival = $c[0];
            $time = $c[1];
            if ($curr < $arrival) {
                $curr = $arrival + $time;
            } else {
                $curr += $time;
            }
            $total += $curr - $arrival;
        }
        return $total / count($customers);
    }
}
```

## Swift

```swift
class Solution {
    func averageWaitingTime(_ customers: [[Int]]) -> Double {
        var currentTime = 0
        var totalWait: Int64 = 0
        
        for customer in customers {
            let arrival = customer[0]
            let prep = customer[1]
            
            if currentTime < arrival {
                currentTime = arrival + prep
            } else {
                currentTime += prep
            }
            totalWait += Int64(currentTime - arrival)
        }
        
        return Double(totalWait) / Double(customers.count)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun averageWaitingTime(customers: Array<IntArray>): Double {
        var currentTime = 0L
        var totalWait = 0L
        for (c in customers) {
            val arrival = c[0].toLong()
            val prep = c[1].toLong()
            if (currentTime < arrival) {
                currentTime = arrival
            }
            currentTime += prep
            totalWait += currentTime - arrival
        }
        return totalWait.toDouble() / customers.size
    }
}
```

## Dart

```dart
class Solution {
  double averageWaitingTime(List<List<int>> customers) {
    int current = 0;
    int totalWait = 0;
    for (var c in customers) {
      int arrival = c[0];
      int time = c[1];
      if (current < arrival) {
        current = arrival + time;
      } else {
        current += time;
      }
      totalWait += current - arrival;
    }
    return totalWait / customers.length;
  }
}
```

## Golang

```go
func averageWaitingTime(customers [][]int) float64 {
	var cur int64
	var total int64
	for _, c := range customers {
		arrival := int64(c[0])
		duration := int64(c[1])
		if cur < arrival {
			cur = arrival + duration
		} else {
			cur += duration
		}
		total += cur - arrival
	}
	return float64(total) / float64(len(customers))
}
```

## Ruby

```ruby
def average_waiting_time(customers)
  cur = 0
  total = 0
  customers.each do |arr, dur|
    if cur < arr
      cur = arr + dur
    else
      cur += dur
    end
    total += cur - arr
  end
  total.to_f / customers.length
end
```

## Scala

```scala
object Solution {
    def averageWaitingTime(customers: Array[Array[Int]]): Double = {
        var currentTime: Long = 0L
        var totalWait: Long = 0L
        for (c <- customers) {
            val arrival = c(0).toLong
            val prep = c(1).toLong
            if (currentTime < arrival) currentTime = arrival
            currentTime += prep
            totalWait += currentTime - arrival
        }
        totalWait.toDouble / customers.length
    }
}
```

## Rust

```rust
impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut cur_time: i64 = 0;
        let mut total_wait: i64 = 0;
        for cust in customers.iter() {
            let arrive = cust[0] as i64;
            let dur = cust[1] as i64;
            if cur_time < arrive {
                cur_time = arrive + dur;
            } else {
                cur_time += dur;
            }
            total_wait += cur_time - arrive;
        }
        total_wait as f64 / customers.len() as f64
    }
}
```

## Racket

```racket
(define/contract (average-waiting-time customers)
  (-> (listof (listof exact-integer?)) flonum?)
  (let ((n (length customers)))
    (if (= n 0)
        0.0
        (let loop ((lst customers) (curr 0) (total 0))
          (if (null? lst)
              (/ (exact->inexact total) n)
              (let* ((c (car lst))
                     (arr (list-ref c 0))
                     (prep (list-ref c 1))
                     (start (max arr curr))
                     (finish (+ start prep))
                     (wait (- finish arr)))
                (loop (cdr lst) finish (+ total wait))))))))
```

## Erlang

```erlang
-spec average_waiting_time(Customers :: [[integer()]]) -> float().
average_waiting_time(Customers) ->
    {_, Total} = lists:foldl(
        fun([Arr, Dur], {Cur, Sum}) ->
            Start = erlang:max(Arr, Cur),
            Finish = Start + Dur,
            {Finish, Sum + (Finish - Arr)}
        end,
        {0, 0},
        Customers
    ),
    Total / length(Customers).
```

## Elixir

```elixir
defmodule Solution do
  @spec average_waiting_time(customers :: [[integer]]) :: float
  def average_waiting_time(customers) do
    {total_wait, _} =
      Enum.reduce(customers, {0, 0}, fn [arrival, time], {sum, cur_time} ->
        start = if cur_time > arrival, do: cur_time, else: arrival
        finish = start + time
        wait = finish - arrival
        {sum + wait, finish}
      end)

    total_wait / length(customers)
  end
end
```
