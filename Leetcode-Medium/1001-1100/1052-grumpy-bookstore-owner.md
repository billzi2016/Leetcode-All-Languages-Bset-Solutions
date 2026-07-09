# 1052. Grumpy Bookstore Owner

## Cpp

```cpp
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int n = customers.size();
        long long base = 0;
        for (int i = 0; i < n; ++i) {
            if (!grumpy[i]) base += customers[i];
        }
        long long cur = 0;
        for (int i = 0; i < minutes; ++i) {
            if (grumpy[i]) cur += customers[i];
        }
        long long maxExtra = cur;
        for (int i = minutes; i < n; ++i) {
            if (grumpy[i]) cur += customers[i];
            if (grumpy[i - minutes]) cur -= customers[i - minutes];
            if (cur > maxExtra) maxExtra = cur;
        }
        return static_cast<int>(base + maxExtra);
    }
};
```

## Java

```java
class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int n = customers.length;
        int baseSatisfied = 0;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) {
                baseSatisfied += customers[i];
            }
        }

        int extra = 0;
        for (int i = 0; i < minutes; i++) {
            if (grumpy[i] == 1) {
                extra += customers[i];
            }
        }
        int maxExtra = extra;

        for (int i = minutes; i < n; i++) {
            if (grumpy[i] == 1) {
                extra += customers[i];
            }
            int outIdx = i - minutes;
            if (grumpy[outIdx] == 1) {
                extra -= customers[outIdx];
            }
            if (extra > maxExtra) {
                maxExtra = extra;
            }
        }

        return baseSatisfied + maxExtra;
    }
}
```

## Python

```python
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        # Customers already satisfied without using the technique
        base_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]

        # Compute extra satisfied customers within the initial window
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        max_extra = extra

        # Slide the window across the rest of the minutes
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra += customers[i]
            j = i - minutes
            if grumpy[j] == 1:
                extra -= customers[j]
            if extra > max_extra:
                max_extra = extra

        return base_satisfied + max_extra
```

## Python3

```python
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        base = 0
        extra = [0] * len(customers)
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 0:
                base += c
            else:
                extra[i] = c

        window_sum = sum(extra[:minutes])
        max_extra = window_sum

        for i in range(minutes, len(customers)):
            window_sum += extra[i] - extra[i - minutes]
            if window_sum > max_extra:
                max_extra = window_sum

        return base + max_extra
```

## C

```c
int maxSatisfied(int* customers, int customersSize, int* grumpy, int grumpySize, int minutes) {
    long base = 0;
    for (int i = 0; i < customersSize; ++i) {
        if (!grumpy[i]) {
            base += customers[i];
        }
    }

    long cur = 0;
    for (int i = 0; i < minutes; ++i) {
        if (grumpy[i]) {
            cur += customers[i];
        }
    }
    long extra = cur;

    for (int i = minutes; i < customersSize; ++i) {
        if (grumpy[i]) {
            cur += customers[i];
        }
        if (grumpy[i - minutes]) {
            cur -= customers[i - minutes];
        }
        if (cur > extra) {
            extra = cur;
        }
    }

    return (int)(base + extra);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int n = customers.Length;
        int baseSatisfied = 0;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) baseSatisfied += customers[i];
        }

        int currentGain = 0;
        for (int i = 0; i < minutes; i++) {
            if (grumpy[i] == 1) currentGain += customers[i];
        }
        int maxGain = currentGain;

        for (int i = minutes; i < n; i++) {
            if (grumpy[i] == 1) currentGain += customers[i];
            if (grumpy[i - minutes] == 1) currentGain -= customers[i - minutes];
            if (currentGain > maxGain) maxGain = currentGain;
        }

        return baseSatisfied + maxGain;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} customers
 * @param {number[]} grumpy
 * @param {number} minutes
 * @return {number}
 */
var maxSatisfied = function(customers, grumpy, minutes) {
    const n = customers.length;
    let base = 0; // already satisfied without using technique
    for (let i = 0; i < n; ++i) {
        if (grumpy[i] === 0) base += customers[i];
    }
    
    // compute extra gain within the first window
    let windowGain = 0;
    for (let i = 0; i < minutes; ++i) {
        if (grumpy[i] === 1) windowGain += customers[i];
    }
    let maxGain = windowGain;
    
    // slide the window
    for (let i = minutes; i < n; ++i) {
        if (grumpy[i] === 1) windowGain += customers[i];
        if (grumpy[i - minutes] === 1) windowGain -= customers[i - minutes];
        if (windowGain > maxGain) maxGain = windowGain;
    }
    
    return base + maxGain;
};
```

## Typescript

```typescript
function maxSatisfied(customers: number[], grumpy: number[], minutes: number): number {
    const n = customers.length;
    let base = 0;
    for (let i = 0; i < n; i++) {
        if (grumpy[i] === 0) base += customers[i];
    }

    let extra = 0;
    for (let i = 0; i < minutes; i++) {
        if (grumpy[i] === 1) extra += customers[i];
    }
    let maxExtra = extra;

    for (let i = minutes; i < n; i++) {
        if (grumpy[i] === 1) extra += customers[i];
        const j = i - minutes;
        if (grumpy[j] === 1) extra -= customers[j];
        if (extra > maxExtra) maxExtra = extra;
    }

    return base + maxExtra;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $customers
     * @param Integer[] $grumpy
     * @param Integer $minutes
     * @return Integer
     */
    function maxSatisfied($customers, $grumpy, $minutes) {
        $n = count($customers);
        $base = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($grumpy[$i] == 0) {
                $base += $customers[$i];
            }
        }

        $extra = 0;
        for ($i = 0; $i < $minutes; $i++) {
            if ($grumpy[$i] == 1) {
                $extra += $customers[$i];
            }
        }
        $maxExtra = $extra;

        for ($i = $minutes; $i < $n; $i++) {
            if ($grumpy[$i] == 1) {
                $extra += $customers[$i];
            }
            $j = $i - $minutes;
            if ($grumpy[$j] == 1) {
                $extra -= $customers[$j];
            }
            if ($extra > $maxExtra) {
                $maxExtra = $extra;
            }
        }

        return $base + $maxExtra;
    }
}
```

## Swift

```swift
class Solution {
    func maxSatisfied(_ customers: [Int], _ grumpy: [Int], _ minutes: Int) -> Int {
        let n = customers.count
        var base = 0
        for i in 0..<n {
            if grumpy[i] == 0 {
                base += customers[i]
            }
        }
        
        var extra = 0
        for i in 0..<minutes {
            if grumpy[i] == 1 {
                extra += customers[i]
            }
        }
        var maxExtra = extra
        
        if minutes < n {
            for i in minutes..<n {
                if grumpy[i] == 1 {
                    extra += customers[i]
                }
                let j = i - minutes
                if grumpy[j] == 1 {
                    extra -= customers[j]
                }
                if extra > maxExtra {
                    maxExtra = extra
                }
            }
        }
        
        return base + maxExtra
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSatisfied(customers: IntArray, grumpy: IntArray, minutes: Int): Int {
        val n = customers.size
        var baseSatisfied = 0
        val extra = IntArray(n)
        for (i in 0 until n) {
            if (grumpy[i] == 0) {
                baseSatisfied += customers[i]
                extra[i] = 0
            } else {
                extra[i] = customers[i]
            }
        }

        var windowSum = 0
        for (i in 0 until minutes) {
            windowSum += extra[i]
        }
        var maxExtra = windowSum

        for (i in minutes until n) {
            windowSum += extra[i]
            windowSum -= extra[i - minutes]
            if (windowSum > maxExtra) {
                maxExtra = windowSum
            }
        }

        return baseSatisfied + maxExtra
    }
}
```

## Dart

```dart
class Solution {
  int maxSatisfied(List<int> customers, List<int> grumpy, int minutes) {
    int n = customers.length;
    int baseSatisfied = 0;
    for (int i = 0; i < n; i++) {
      if (grumpy[i] == 0) baseSatisfied += customers[i];
    }

    int windowGain = 0;
    for (int i = 0; i < minutes; i++) {
      if (grumpy[i] == 1) windowGain += customers[i];
    }
    int maxGain = windowGain;

    for (int i = minutes; i < n; i++) {
      if (grumpy[i] == 1) windowGain += customers[i];
      if (grumpy[i - minutes] == 1) windowGain -= customers[i - minutes];
      if (windowGain > maxGain) maxGain = windowGain;
    }

    return baseSatisfied + maxGain;
  }
}
```

## Golang

```go
func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	n := len(customers)
	base := 0
	for i := 0; i < n; i++ {
		if grumpy[i] == 0 {
			base += customers[i]
		}
	}

	extra := 0
	for i := 0; i < minutes && i < n; i++ {
		if grumpy[i] == 1 {
			extra += customers[i]
		}
	}
	maxExtra := extra

	for i := minutes; i < n; i++ {
		if grumpy[i] == 1 {
			extra += customers[i]
		}
		j := i - minutes
		if grumpy[j] == 1 {
			extra -= customers[j]
		}
		if extra > maxExtra {
			maxExtra = extra
		}
	}

	return base + maxExtra
}
```

## Ruby

```ruby
def max_satisfied(customers, grumpy, minutes)
  n = customers.length
  base = 0
  customers.each_with_index { |c, i| base += c if grumpy[i] == 0 }

  extra = 0
  (0...minutes).each { |i| extra += customers[i] if grumpy[i] == 1 }
  max_extra = extra

  (minutes...n).each do |i|
    extra += customers[i] if grumpy[i] == 1
    j = i - minutes
    extra -= customers[j] if grumpy[j] == 1
    max_extra = [max_extra, extra].max
  end

  base + max_extra
end
```

## Scala

```scala
object Solution {
    def maxSatisfied(customers: Array[Int], grumpy: Array[Int], minutes: Int): Int = {
        val n = customers.length
        var base = 0
        var i = 0
        while (i < n) {
            if (grumpy(i) == 0) base += customers(i)
            i += 1
        }

        var extra = 0
        i = 0
        while (i < minutes) {
            if (grumpy(i) == 1) extra += customers(i)
            i += 1
        }
        var maxExtra = extra

        var left = 0
        var right = minutes
        while (right < n) {
            if (grumpy(right) == 1) extra += customers(right)
            if (grumpy(left) == 1) extra -= customers(left)
            left += 1
            if (extra > maxExtra) maxExtra = extra
            right += 1
        }

        base + maxExtra
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let n = customers.len();
        let m = minutes as usize;

        // Customers already satisfied without using the technique
        let mut base = 0i32;
        for i in 0..n {
            if grumpy[i] == 0 {
                base += customers[i];
            }
        }

        // Extra customers that could become satisfied within the initial window
        let mut extra = 0i32;
        let init_end = std::cmp::min(m, n);
        for i in 0..init_end {
            if grumpy[i] == 1 {
                extra += customers[i];
            }
        }

        let mut max_extra = extra;

        // Slide the window across the rest of the minutes
        for i in m..n {
            if grumpy[i] == 1 {
                extra += customers[i];
            }
            let j = i - m;
            if grumpy[j] == 1 {
                extra -= customers[j];
            }
            if extra > max_extra {
                max_extra = extra;
            }
        }

        base + max_extra
    }
}
```

## Racket

```racket
(define/contract (max-satisfied customers grumpy minutes)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((vcust (list->vector customers))
         (vgr   (list->vector grumpy))
         (n     (vector-length vcust)))
    ;; base satisfied customers when owner is not grumpy
    (define base
      (let loop ((i 0) (sum 0))
        (if (= i n)
            sum
            (loop (+ i 1)
                  (if (= (vector-ref vgr i) 0)
                      (+ sum (vector-ref vcust i))
                      sum)))))
    ;; extra customers that could be rescued if the window covers a grumpy minute
    (define extra
      (let ((vec (make-vector n 0)))
        (let loop ((i 0))
          (when (< i n)
            (when (= (vector-ref vgr i) 1)
              (vector-set! vec i (vector-ref vcust i)))
            (loop (+ i 1))))
        vec))
    ;; sum of the first `minutes` elements in extra
    (define init-sum
      (let loop ((i 0) (sum 0))
        (if (= i minutes)
            sum
            (loop (+ i 1) (+ sum (vector-ref extra i))))))
    ;; maximum sum over any window of length `minutes`
    (define max-sum
      (if (= minutes n)
          init-sum
          (let loop ((i minutes) (cur init-sum) (maxv init-sum))
            (if (= i n)
                maxv
                (let* ((new-cur (+ cur (- (vector-ref extra (- i minutes))) (vector-ref extra i)))
                       (new-max (if (> new-cur maxv) new-cur maxv)))
                  (loop (+ i 1) new-cur new-max))))))
    (+ base max-sum)))
```

## Erlang

```erlang
-spec max_satisfied(Customers :: [integer()], Grumpy :: [integer()], Minutes :: integer()) -> integer().
max_satisfied(Customers, Grumpy, Minutes) ->
    Zipped = lists:zip(Customers, Grumpy),
    BaseSatisfied = lists:foldl(fun({C,G}, Acc) -> if G =:= 0 -> Acc + C; true -> Acc end end, 0, Zipped),
    Gains = [if G =:= 1 -> C; true -> 0 end || {C,G} <- Zipped],
    Extra = extra_gain(Gains, Minutes),
    BaseSatisfied + Extra.

extra_gain(Gains, K) ->
    N = length(Gains),
    if
        K >= N -> lists:sum(Gains);
        true ->
            Prefix = prefix_sums(Gains),
            Shifted = lists:nthtail(K, Prefix),
            case {Prefix, Shifted} of
                {[P0|Ps], [Q0|Qs]} ->
                    InitialDiff = Q0 - P0,
                    max_gain(Ps, Qs, InitialDiff)
            end
    end.

prefix_sums(List) -> prefix_sums(List, 0, [0]).
prefix_sums([], _Sum, Acc) -> lists:reverse(Acc);
prefix_sums([H|T], Sum, Acc) ->
    NewSum = Sum + H,
    prefix_sums(T, NewSum, [NewSum | Acc]).

max_gain([], [], Max) -> Max;
max_gain([P|Ps], [Q|Qs], Max) ->
    Diff = Q - P,
    NewMax = if Diff > Max -> Diff; true -> Max end,
    max_gain(Ps, Qs, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_satisfied(customers :: [integer], grumpy :: [integer], minutes :: integer) :: integer
  def max_satisfied(customers, grumpy, minutes) do
    n = length(customers)

    extra =
      Enum.zip(customers, grumpy)
      |> Enum.map(fn {c, g} -> if g == 1, do: c, else: 0 end)

    total_customers = Enum.sum(customers)
    unsatisfied_sum = Enum.sum(extra)
    base_satisfied = total_customers - unsatisfied_sum

    extra_tuple = List.to_tuple(extra)

    init_sum =
      0..(minutes - 1)
      |> Enum.reduce(0, fn i, acc -> acc + elem(extra_tuple, i) end)

    {max_extra, _} =
      Enum.reduce(minutes..(n - 1), {init_sum, init_sum}, fn i, {cur_max, cur_sum} ->
        new_sum = cur_sum + elem(extra_tuple, i) - elem(extra_tuple, i - minutes)
        max_val = if new_sum > cur_max, do: new_sum, else: cur_max
        {max_val, new_sum}
      end)

    base_satisfied + max_extra
  end
end
```
