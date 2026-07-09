# 3457. Eat Pizzas!

## Cpp

```cpp
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end());
        int n = pizzas.size();
        int totalDays = n / 4;
        int oddCount = (totalDays + 1) / 2;   // ceil
        int evenCount = totalDays / 2;        // floor
        
        long long ans = 0;
        int left = 0;
        int right = n - 1;
        
        // Process odd-numbered days: take largest, discard three smallest
        for (int i = 0; i < oddCount; ++i) {
            ans += pizzas[right];
            --right;
            left += 3;
        }
        
        // Process even-numbered days: take second largest, discard two smallest
        for (int i = 0; i < evenCount; ++i) {
            // right now points to the largest remaining element
            // second largest is at right-1
            ans += pizzas[right - 1];
            right -= 2;   // remove both largest and second largest
            left += 2;    // discard two smallest
        }
        
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maxWeight(int[] pizzas) {
        java.util.Arrays.sort(pizzas);
        int n = pizzas.length;
        int days = n / 4;
        int oddDays = (days + 1) / 2; // ceil(days/2)
        int evenDays = days / 2;      // floor(days/2)

        long ans = 0L;
        int left = 0, right = n - 1;

        for (int i = 0; i < oddDays; i++) {
            ans += pizzas[right];
            right--;
            left += 3; // consume three smallest
        }

        for (int i = 0; i < evenDays; i++) {
            ans += pizzas[right - 1]; // second largest among the four
            right -= 2;               // remove two largest
            left += 2;                // remove two smallest
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        pizzas.sort()
        n = len(pizzas)
        groups = n // 4
        left = 0
        right = n - 1
        total = 0
        for day in range(1, groups + 1):
            if day % 2 == 1:  # odd day
                total += pizzas[right]
                left += 3
                right -= 1
            else:  # even day
                # take two largest, gain the smaller one (second largest)
                total += pizzas[right - 1]
                left += 2
                right -= 2
        return total
```

## Python3

```python
class Solution:
    def maxWeight(self, pizzas):
        pizzas.sort()
        n = len(pizzas)
        days = n // 4
        low = 0
        high = n - 1
        ans = 0
        for d in range(days):
            if d % 2 == 0:  # odd-numbered day (1-indexed)
                ans += pizzas[high]
                high -= 1
                low += 3
            else:           # even-numbered day
                ans += pizzas[high - 1]
                high -= 2
                low += 2
        return ans
```

## C

```c
long long maxWeight(int* pizzas, int pizzasSize) {
    qsort(pizzas, pizzasSize, sizeof(int), 
          (int (*)(const void*, const void*))[](const void *a, const void *b)->int{
              int ai = *(const int*)a;
              int bi = *(const int*)b;
              return (ai > bi) - (ai < bi);
          });
    
    int totalDays = pizzasSize / 4;
    int oddDays = (totalDays + 1) / 2;   // ceil(totalDays/2)
    int evenDays = totalDays - oddDays;
    
    long long ans = 0;
    int idx = pizzasSize - 1; // points to the current largest remaining pizza
    
    // Process odd-numbered days: take three smallest and one largest (gain the largest)
    for (int i = 0; i < oddDays; ++i) {
        ans += pizzas[idx];
        --idx; // remove that largest pizza
    }
    
    // Process even-numbered days: take two smallest and two largest,
    // gain the second largest among the two largest.
    for (int i = 0; i < evenDays; ++i) {
        --idx;               // discard the largest (no gain)
        ans += pizzas[idx];  // gain the second largest
        --idx;               // discard the other pizza of this day
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxWeight(int[] pizzas) {
        int n = pizzas.Length;
        System.Array.Sort(pizzas);
        int groups = n / 4;
        int oddDays = (groups + 1) / 2; // ceil
        int evenDays = groups / 2;

        long ans = 0;
        for (int i = n - oddDays; i < n; ++i) {
            ans += pizzas[i];
        }

        int idx = n - oddDays - 2;
        for (int k = 0; k < evenDays; ++k) {
            ans += pizzas[idx - 2 * k];
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} pizzas
 * @return {number}
 */
var maxWeight = function(pizzas) {
    pizzas.sort((a, b) => a - b);
    let left = 0;
    let right = pizzas.length - 1;
    let total = 0;
    while (left <= right) {
        // odd-numbered day: take the largest as gain
        total += pizzas[right];
        right--;
        left += 3; // use three smallest as fillers
        if (left > right) break;
        // even-numbered day: take the second largest as gain,
        // the largest becomes a filler
        total += pizzas[right - 1];
        right -= 2; // consume both large pizzas
        left += 2;  // use two smallest as fillers
    }
    return total;
};
```

## Typescript

```typescript
function maxWeight(pizzas: number[]): number {
    pizzas.sort((a, b) => a - b);
    let left = 0;
    let right = pizzas.length - 1;
    const days = pizzas.length / 4;
    let ans = 0;

    for (let day = 1; day <= days; day++) {
        if (day % 2 === 1) { // odd-numbered day
            ans += pizzas[right];
            right--;
            left += 3;
        } else { // even-numbered day
            ans += pizzas[right - 1];
            right -= 2;   // discard the largest and use second largest as gain
            left += 2;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $pizzas
     * @return Integer
     */
    function maxWeight($pizzas) {
        $n = count($pizzas);
        sort($pizzas); // ascending order

        $skip = intdiv($n, 4); // number of groups / days
        $ans = 0;
        $cnt = 0;
        for ($i = $n - 1; $cnt < $skip; $i -= 2, $cnt++) {
            $ans += $pizzas[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxWeight(_ pizzas: [Int]) -> Int {
        let sorted = pizzas.sorted()
        var left = 0
        var right = sorted.count - 1
        var total = 0
        let days = sorted.count / 4
        
        for day in 1...days {
            if day % 2 == 1 { // odd-numbered day
                total += sorted[right]
                right -= 1
                left += 3
            } else { // even-numbered day
                total += sorted[right - 1]
                right -= 2
                left += 2
            }
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxWeight(pizzas: IntArray): Long {
        pizzas.sort()
        var ans = 0L
        var idx = pizzas.size - 1
        val groups = pizzas.size / 4
        repeat(groups) {
            ans += pizzas[idx].toLong()
            idx -= 2
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxWeight(List<int> pizzas) {
    pizzas.sort(); // ascending order
    int n = pizzas.length;
    int days = n ~/ 4;
    int oddDays = (days + 1) ~/ 2; // ceil(days / 2)
    int left = 0;
    int right = n - 1;
    int total = 0;

    for (int i = 0; i < oddDays; i++) {
      total += pizzas[right];
      right--;
      left += 3;
    }

    int evenDays = days - oddDays;
    for (int i = 0; i < evenDays; i++) {
      // second largest among the four selected
      total += pizzas[right - 1];
      left += 2;
      right -= 2;
    }

    return total;
  }
}
```

## Golang

```go
func maxWeight(pizzas []int) int64 {
    n := len(pizzas)
    if n == 0 {
        return 0
    }
    sort.Ints(pizzas)
    groups := n / 4
    var sum int64
    cnt := 0
    for i := n - 1; i >= 0 && cnt < groups; i -= 2 {
        sum += int64(pizzas[i])
        cnt++
    }
    return sum
}
```

## Ruby

```ruby
def max_weight(pizzas)
  pizzas.sort!
  i = 0
  j = pizzas.length - 1
  total = 0

  while i < j
    # odd-numbered day: take the largest pizza as gain
    total += pizzas[j]
    j -= 1
    i += 3
    break if i > j

    # even-numbered day: take the second largest among the remaining four
    total += pizzas[j - 1]
    j -= 2
    i += 2
  end

  total
end
```

## Scala

```scala
object Solution {
    def maxWeight(pizzas: Array[Int]): Long = {
        val arr = pizzas.sorted
        var left = 0
        var right = arr.length - 1
        val days = arr.length / 4
        var total: Long = 0L
        var i = 0
        while (i < days) {
            if ((i & 1) == 0) { // odd-numbered day (1-indexed)
                total += arr(right).toLong
                right -= 1
                left += 3
            } else { // even-numbered day
                total += arr(right - 1).toLong
                right -= 2
                left += 2
            }
            i += 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_weight(pizzas: Vec<i32>) -> i64 {
        let mut a = pizzas;
        a.sort(); // ascending
        let n = a.len();
        let groups = n / 4;               // total days
        let odd_days = (groups + 1) / 2;   // ceil(groups/2)
        let even_days = groups / 2;        // floor(groups/2)

        let mut left: usize = 0;
        let mut right: usize = n - 1;
        let mut ans: i64 = 0;

        for _ in 0..odd_days {
            ans += a[right] as i64; // largest pizza of the day
            if right == 0 { break; }
            right -= 1;            // consume it
            left += 3;             // three smallest pizzas are eaten but give no weight
        }

        for _ in 0..even_days {
            // two smallest and two largest remain, we gain the smaller of the two largest
            ans += a[right - 1] as i64;
            if right < 2 { break; }
            right -= 2;            // consume both largest pizzas
            left += 2;             // consume two smallest pizzas
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-weight pizzas)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort pizzas <))
         (v (list->vector sorted))
         (n (vector-length v))
         (groups (quotient n 4))
         (odd-days (quotient (+ groups 1) 2)) ; ceil(groups/2)
         (even-days (- groups odd-days)))
    (let loop-odd ((i 0) (left 0) (right (sub1 n)) (total 0))
      (if (= i odd-days)
          (let loop-even ((j 0) (l left) (r right) (tot total))
            (if (= j even-days)
                tot
                (loop-even (+ j 1)
                           (+ l 2)
                           (- r 2)
                           (+ tot (vector-ref v (- r 1))))))
          (loop-odd (+ i 1)
                     (+ left 3)
                     (- right 1)
                     (+ total (vector-ref v right)))))))
```

## Erlang

```erlang
-spec max_weight([integer()]) -> integer().
max_weight(Pizzas) ->
    Sorted = lists:sort(Pizzas),
    T = list_to_tuple(Sorted),
    N = tuple_size(T),
    loop(1, N, 1, T).

loop(L, R, _Day, _T) when L > R ->
    0;
loop(L, R, Day, T) ->
    case Day rem 2 of
        1 -> % odd day: take three smallest and the largest (gain largest)
            Gain = element(R, T),
            NewL = L + 3,
            NewR = R - 1,
            Gain + loop(NewL, NewR, Day + 1, T);
        0 -> % even day: take two smallest and two largest (gain second largest)
            Gain = element(R - 1, T),
            NewL = L + 2,
            NewR = R - 2,
            Gain + loop(NewL, NewR, Day + 1, T)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_weight(pizzas :: [integer]) :: integer
  def max_weight(pizzas) do
    sorted = Enum.sort(pizzas)
    tup = List.to_tuple(sorted)
    n = tuple_size(tup)

    loop(tup, 0, n - 1, true, 0)
  end

  defp loop(_tup, left, right, _odd?, acc) when left > right, do: acc

  # odd-numbered day: take three smallest and one largest (gain the largest)
  defp loop(tup, left, right, true, acc) do
    gain = elem(tup, right)
    loop(tup, left + 3, right - 1, false, acc + gain)
  end

  # even-numbered day: take two smallest and two largest (gain the second largest)
  defp loop(tup, left, right, false, acc) do
    gain = elem(tup, right - 1)
    loop(tup, left + 2, right - 2, true, acc + gain)
  end
end
```
