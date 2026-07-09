# 1619. Mean of Array After Removing Some Elements

## Cpp

```cpp
class Solution {
public:
    double trimMean(std::vector<int>& arr) {
        int n = arr.size();
        std::sort(arr.begin(), arr.end());
        int k = n / 20;
        long long sum = 0;
        for (int i = k; i < n - k; ++i) {
            sum += arr[i];
        }
        return static_cast<double>(sum) / (n - 2 * k);
    }
};
```

## Java

```java
class Solution {
    public double trimMean(int[] arr) {
        int n = arr.length;
        int remove = n / 20; // 5% of elements
        java.util.Arrays.sort(arr);
        long sum = 0;
        for (int i = remove; i < n - remove; i++) {
            sum += arr[i];
        }
        return (double) sum / (n - 2 * remove);
    }
}
```

## Python

```python
class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        n = len(arr)
        k = n // 20  # 5% of elements from each end
        arr.sort()
        trimmed_sum = sum(arr[k:n - k])
        return trimmed_sum / (n - 2 * k)
```

## Python3

```python
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = n // 20
        arr.sort()
        return sum(arr[k:n - k]) / (n - 2 * k)
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

double trimMean(int* arr, int arrSize) {
    if (arr == NULL || arrSize == 0) return 0.0;
    qsort(arr, (size_t)arrSize, sizeof(int), cmp_int);
    
    int remove = arrSize / 20;               // 5% of elements
    int start = remove;
    int end   = arrSize - remove;            // exclusive upper bound
    
    long long sum = 0;
    for (int i = start; i < end; ++i) {
        sum += arr[i];
    }
    
    int count = end - start;
    return (double)sum / count;
}
```

## Csharp

```csharp
public class Solution {
    public double TrimMean(int[] arr) {
        int n = arr.Length;
        int removeCount = n / 20; // 5% of elements
        System.Array.Sort(arr);
        long sum = 0;
        for (int i = removeCount; i < n - removeCount; i++) {
            sum += arr[i];
        }
        int remaining = n - 2 * removeCount;
        return (double)sum / remaining;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(arr) {
    const n = arr.length;
    const removeCount = Math.floor(n / 20); // 5% of elements
    arr.sort((a, b) => a - b);
    let sum = 0;
    for (let i = removeCount; i < n - removeCount; ++i) {
        sum += arr[i];
    }
    return sum / (n - 2 * removeCount);
};
```

## Typescript

```typescript
function trimMean(arr: number[]): number {
    const n = arr.length;
    const removeCount = n / 20; // 5% of elements
    const sorted = arr.slice().sort((a, b) => a - b);
    let sum = 0;
    for (let i = removeCount; i < n - removeCount; i++) {
        sum += sorted[i];
    }
    return sum / (n - 2 * removeCount);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Float
     */
    function trimMean($arr) {
        sort($arr);
        $n = count($arr);
        $remove = intdiv($n, 20); // 5% of elements
        $sum = 0;
        for ($i = $remove; $i < $n - $remove; $i++) {
            $sum += $arr[$i];
        }
        return $sum / ($n - 2 * $remove);
    }
}
```

## Swift

```swift
class Solution {
    func trimMean(_ arr: [Int]) -> Double {
        let n = arr.count
        let k = n / 20
        let sortedArr = arr.sorted()
        var sum = 0
        for i in k..<(n - k) {
            sum += sortedArr[i]
        }
        return Double(sum) / Double(n - 2 * k)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun trimMean(arr: IntArray): Double {
        val sorted = arr.sorted()
        val n = sorted.size
        val remove = n / 20
        var sum = 0L
        for (i in remove until n - remove) {
            sum += sorted[i].toLong()
        }
        return sum.toDouble() / (n - 2 * remove)
    }
}
```

## Dart

```dart
class Solution {
  double trimMean(List<int> arr) {
    arr.sort();
    int n = arr.length;
    int k = n ~/ 20;
    int sum = 0;
    for (int i = k; i < n - k; ++i) {
      sum += arr[i];
    }
    return sum / (n - 2 * k);
  }
}
```

## Golang

```go
import "sort"

func trimMean(arr []int) float64 {
    sort.Ints(arr)
    n := len(arr)
    k := n / 20
    sum := 0
    for i := k; i < n-k; i++ {
        sum += arr[i]
    }
    return float64(sum) / float64(n-2*k)
}
```

## Ruby

```ruby
def trim_mean(arr)
  n = arr.length
  k = n / 20
  sorted = arr.sort
  middle = sorted[k...(n - k)]
  sum = middle.sum
  sum.to_f / middle.size
end
```

## Scala

```scala
object Solution {
    def trimMean(arr: Array[Int]): Double = {
        val n = arr.length
        val k = n / 20
        val sorted = arr.sorted
        var sum: Long = 0L
        var i = k
        while (i < n - k) {
            sum += sorted(i)
            i += 1
        }
        sum.toDouble / (n - 2 * k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        let n = arr.len();
        let k = n / 20;
        let mut v = arr.clone();
        v.sort_unstable();
        let sum: i64 = v[k..n - k].iter().map(|&x| x as i64).sum();
        sum as f64 / ((n - 2 * k) as f64)
    }
}
```

## Racket

```racket
(define/contract (trim-mean arr)
  (-> (listof exact-integer?) flonum?)
  (let* ([sorted (sort arr <)]
         [n (length sorted)]
         [k (quotient n 20)]                ; number of elements to remove from each end
         [trimmed (drop sorted k)]
         [remaining-count (- n (* 2 k))]
         [final-list (take trimmed remaining-count)]
         [sum (foldl + 0 final-list)])
    (exact->inexact (/ sum remaining-count))))
```

## Erlang

```erlang
-spec trim_mean(Arr :: [integer()]) -> float().
trim_mean(Arr) ->
    Sorted = lists:sort(Arr),
    N = length(Sorted),
    K = N div 20,
    Trimmed = lists:sublist(Sorted, K + 1, N - 2 * K),
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Trimmed),
    Count = N - 2 * K,
    Sum / Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec trim_mean(arr :: [integer]) :: float
  def trim_mean(arr) do
    n = length(arr)
    k = div(n, 20)

    sorted = Enum.sort(arr)
    middle = Enum.slice(sorted, k, n - 2 * k)

    sum = Enum.reduce(middle, 0, &+/2)
    sum / (n - 2 * k)
  end
end
```
