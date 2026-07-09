# 2517. Maximum Tastiness of Candy Basket

## Cpp

```cpp
class Solution {
public:
    bool canAchieve(const vector<int>& a, int k, int diff) {
        int cnt = 1;
        int last = a[0];
        for (size_t i = 1; i < a.size(); ++i) {
            if (a[i] - last >= diff) {
                ++cnt;
                last = a[i];
                if (cnt >= k) return true;
            }
        }
        return cnt >= k;
    }

    int maximumTastiness(vector<int>& price, int k) {
        sort(price.begin(), price.end());
        int low = 0;
        int high = price.back() - price.front(); // maximal possible tastiness
        while (low < high) {
            int mid = low + (high - low + 1) / 2;
            if (canAchieve(price, k, mid))
                low = mid;
            else
                high = mid - 1;
        }
        return low;
    }
};
```

## Java

```java
class Solution {
    public int maximumTastiness(int[] price, int k) {
        java.util.Arrays.sort(price);
        int n = price.length;
        int low = 0;
        int high = price[n - 1] - price[0] + 1; // exclusive upper bound

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canAchieve(price, k, mid)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low - 1;
    }

    private boolean canAchieve(int[] price, int k, int minDiff) {
        int count = 1; // pick the first candy
        int lastPicked = price[0];
        for (int i = 1; i < price.length; i++) {
            if (price[i] - lastPicked >= minDiff) {
                count++;
                lastPicked = price[i];
                if (count >= k) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        
        def can(x):
            cnt = 1
            last = price[0]
            for p in price[1:]:
                if p - last >= x:
                    cnt += 1
                    last = p
                    if cnt >= k:
                        return True
            return False
        
        lo, hi = 0, price[-1] - price[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        def can(t: int) -> bool:
            cnt = 1
            last = price[0]
            for i in range(1, n):
                if price[i] - last >= t:
                    cnt += 1
                    last = price[i]
                    if cnt >= k:
                        return True
            return False

        lo, hi = 0, price[-1] - price[0] + 1  # hi is exclusive
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmp(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

static bool feasible(int *arr, int n, int k, int diff) {
    int cnt = 1;
    int last = arr[0];
    for (int i = 1; i < n; ++i) {
        if (arr[i] - last >= diff) {
            ++cnt;
            last = arr[i];
            if (cnt >= k) return true;
        }
    }
    return false;
}

int maximumTastiness(int* price, int priceSize, int k) {
    qsort(price, priceSize, sizeof(int), cmp);
    int low = 0;
    int high = price[priceSize - 1] - price[0];
    while (low < high) {
        int mid = low + (high - low + 1) / 2;
        if (feasible(price, priceSize, k, mid))
            low = mid;
        else
            high = mid - 1;
    }
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumTastiness(int[] price, int k) {
        System.Array.Sort(price);
        long low = 0;
        long high = (long)price[price.Length - 1] - price[0];
        while (low < high) {
            long mid = (low + high + 1) / 2;
            if (CanAchieve(mid, price, k)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return (int)low;
    }

    private bool CanAchieve(long diff, int[] arr, int k) {
        int count = 1;
        int last = arr[0];
        for (int i = 1; i < arr.Length; i++) {
            if ((long)arr[i] - last >= diff) {
                count++;
                last = arr[i];
                if (count >= k) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} price
 * @param {number} k
 * @return {number}
 */
var maximumTastiness = function(price, k) {
    price.sort((a, b) => a - b);
    const n = price.length;
    
    const canAchieve = (dist) => {
        let count = 1; // first candy always taken
        let last = price[0];
        for (let i = 1; i < n; i++) {
            if (price[i] - last >= dist) {
                count++;
                last = price[i];
                if (count >= k) return true;
            }
        }
        return false;
    };
    
    let low = 0;
    let high = price[n - 1] - price[0];
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (canAchieve(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
```

## Typescript

```typescript
function maximumTastiness(price: number[], k: number): number {
    price.sort((a, b) => a - b);
    const n = price.length;
    let low = 0;
    let high = price[n - 1] - price[0] + 1; // exclusive upper bound

    const can = (dist: number): boolean => {
        let count = 1;
        let last = price[0];
        for (let i = 1; i < n; i++) {
            if (price[i] - last >= dist) {
                count++;
                last = price[i];
                if (count >= k) return true;
            }
        }
        return false;
    };

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (can(mid)) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    return low - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $price
     * @param Integer $k
     * @return Integer
     */
    function maximumTastiness($price, $k) {
        sort($price);
        $n = count($price);
        $low = 0;
        $high = $price[$n - 1] - $price[0];

        // helper closure to check feasibility
        $can = function(int $diff) use ($price, $k, $n): bool {
            $cnt = 1; // pick the first candy
            $last = $price[0];
            for ($i = 1; $i < $n; ++$i) {
                if ($price[$i] - $last >= $diff) {
                    $cnt++;
                    $last = $price[$i];
                    if ($cnt >= $k) {
                        return true;
                    }
                }
            }
            return false;
        };

        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($can($mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }

        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func maximumTastiness(_ price: [Int], _ k: Int) -> Int {
        let sorted = price.sorted()
        var low = 0
        var high = (sorted.last! - sorted.first!) + 1   // exclusive upper bound
        
        func can(_ minDiff: Int) -> Bool {
            var count = 1
            var last = sorted[0]
            for i in 1..<sorted.count {
                if sorted[i] - last >= minDiff {
                    count += 1
                    last = sorted[i]
                    if count >= k { return true }
                }
            }
            return false
        }
        
        while low < high {
            let mid = (low + high) / 2
            if can(mid) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumTastiness(price: IntArray, k: Int): Int {
        val sorted = price.sorted()
        val n = sorted.size
        var low = 0
        var high = sorted[n - 1] - sorted[0] + 1 // exclusive upper bound

        while (low < high) {
            val mid = low + (high - low) / 2
            if (canAchieve(sorted, k, mid)) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low - 1
    }

    private fun canAchieve(arr: List<Int>, k: Int, diff: Int): Boolean {
        var count = 1
        var last = arr[0]
        for (i in 1 until arr.size) {
            if (arr[i] - last >= diff) {
                count++
                last = arr[i]
                if (count >= k) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int maximumTastiness(List<int> price, int k) {
    price.sort();
    int left = 0;
    int right = price.last - price.first;

    while (left < right) {
      int mid = ((left + right + 1) >> 1);
      if (_canAchieve(price, k, mid)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }

  bool _canAchieve(List<int> arr, int k, int diff) {
    int count = 1;
    int last = arr[0];
    for (int i = 1; i < arr.length; i++) {
      if (arr[i] - last >= diff) {
        count++;
        last = arr[i];
        if (count >= k) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func maximumTastiness(price []int, k int) int {
    sort.Ints(price)
    can := func(diff int) bool {
        count := 1
        last := price[0]
        for i := 1; i < len(price); i++ {
            if price[i]-last >= diff {
                count++
                last = price[i]
                if count >= k {
                    return true
                }
            }
        }
        return false
    }

    lo, hi := 0, price[len(price)-1]-price[0]
    for lo < hi {
        mid := (lo + hi + 1) / 2
        if can(mid) {
            lo = mid
        } else {
            hi = mid - 1
        }
    }
    return lo
}
```

## Ruby

```ruby
def maximum_tastiness(price, k)
  price.sort!
  low = 0
  high = price[-1] - price[0]
  while low < high
    mid = (low + high + 1) / 2
    cnt = 1
    last = price[0]
    price.each do |p|
      if p - last >= mid
        cnt += 1
        last = p
        break if cnt >= k
      end
    end
    if cnt >= k
      low = mid
    else
      high = mid - 1
    end
  end
  low
end
```

## Scala

```scala
object Solution {
    def maximumTastiness(price: Array[Int], k: Int): Int = {
        val arr = price.sorted
        val n = arr.length

        def can(diff: Int): Boolean = {
            var cnt = 1
            var last = arr(0)
            var i = 1
            while (i < n && cnt < k) {
                if (arr(i) - last >= diff) {
                    cnt += 1
                    last = arr(i)
                }
                i += 1
            }
            cnt >= k
        }

        var low = 0
        var high = arr(n - 1) - arr(0)
        while (low < high) {
            val mid = ((low.toLong + high + 1) / 2).toInt
            if (can(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_tastiness(price: Vec<i32>, k: i32) -> i32 {
        let mut arr = price;
        arr.sort_unstable();
        let n = arr.len();
        let k_usize = k as usize;
        let mut low = 0i32;
        let mut high = arr[n - 1] - arr[0];
        while low < high {
            let mid = low + (high - low + 1) / 2;
            if Self::can(&arr, k_usize, mid) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low
    }

    fn can(arr: &Vec<i32>, k: usize, diff: i32) -> bool {
        let mut count = 1usize;
        let mut last = arr[0];
        for &price in arr.iter().skip(1) {
            if price - last >= diff {
                count += 1;
                last = price;
                if count >= k {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (maximum-tastiness price k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort price <))
         (low 0)
         (high (- (last sorted) (first sorted))))
    (define (can? d lst need)
      (let loop ((cnt 1) (prev (first lst)) (rest (rest lst)))
        (cond
          [(= cnt need) #t]
          [(null? rest) #f]
          [else (let ((cur (first rest)))
                  (if (>= (- cur prev) d)
                      (loop (+ cnt 1) cur (rest rest))
                      (loop cnt prev (rest rest))))])))
    (let loop ((l low) (h high))
      (if (= l h)
          l
          (let* ((mid (quotient (+ l h 1) 2)))
            (if (can? mid sorted k)
                (loop mid h)
                (loop l (- mid 1))))))))
```

## Erlang

```erlang
-spec maximum_tastiness([integer()], integer()) -> integer().
maximum_tastiness(Price, K) ->
    Sorted = lists:sort(Price),
    Min = hd(Sorted),
    Max = lists:last(Sorted),
    MaxDiff = Max - Min,
    binary_search(0, MaxDiff + 1, Sorted, K).

binary_search(Low, High, _Sorted, _K) when High - Low =< 1 ->
    Low;
binary_search(Low, High, Sorted, K) ->
    Mid = (Low + High) div 2,
    case possible(Mid, Sorted, K) of
        true -> binary_search(Mid, High, Sorted, K);
        false -> binary_search(Low, Mid, Sorted, K)
    end.

possible(Diff, [First|Rest], K) ->
    possible_loop(Rest, First, 1, Diff, K).

possible_loop(_List, _Prev, Count, _Diff, K) when Count >= K ->
    true;
possible_loop([], _Prev, _Count, _Diff, _K) ->
    false;
possible_loop([H|T], Prev, Count, Diff, K) ->
    if H - Prev >= Diff ->
            possible_loop(T, H, Count + 1, Diff, K);
       true ->
            possible_loop(T, Prev, Count, Diff, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_tastiness(price :: [integer], k :: integer) :: integer
  def maximum_tastiness(price, k) do
    sorted = Enum.sort(price)
    min_price = hd(sorted)
    max_price = List.last(sorted)

    low = 0
    high = max_price - min_price + 1

    binary_search(sorted, k, low, high)
  end

  defp binary_search(_sorted, _k, low, high) when low >= high do
    low - 1
  end

  defp binary_search(sorted, k, low, high) do
    mid = div(low + high, 2)

    if feasible?(sorted, k, mid) do
      binary_search(sorted, k, mid + 1, high)
    else
      binary_search(sorted, k, low, mid)
    end
  end

  defp feasible?(sorted, k, dist) do
    {cnt, _last} =
      Enum.reduce_while(sorted, {1, hd(sorted)}, fn p, {cnt, last} ->
        if p - last >= dist do
          if cnt + 1 == k do
            {:halt, {k, p}}
          else
            {:cont, {cnt + 1, p}}
          end
        else
          {:cont, {cnt, last}}
        end
      end)

    cnt >= k
  end
end
```
