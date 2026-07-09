# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Cpp

```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        long long need = 1LL * k * threshold;
        long long sum = 0;
        int count = 0;
        for (int i = 0; i < (int)arr.size(); ++i) {
            sum += arr[i];
            if (i >= k) sum -= arr[i - k];
            if (i >= k - 1 && sum >= need) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        long requiredSum = (long) threshold * k;
        long windowSum = 0;
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            windowSum += arr[i];
            if (i >= k - 1) {
                if (windowSum >= requiredSum) {
                    count++;
                }
                windowSum -= arr[i - k + 1];
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= target:
                count += 1
        return count
```

## C

```c
int numOfSubarrays(int* arr, int arrSize, int k, int threshold) {
    long long need = 1LL * threshold * k;
    long long sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += arr[i];
    }
    int count = (sum >= need);
    for (int i = k; i < arrSize; ++i) {
        sum += arr[i];
        sum -= arr[i - k];
        if (sum >= need) {
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
    public int NumOfSubarrays(int[] arr, int k, int threshold)
    {
        long requiredSum = (long)k * threshold;
        long windowSum = 0;
        int count = 0;

        for (int i = 0; i < arr.Length; i++)
        {
            windowSum += arr[i];
            if (i >= k - 1)
            {
                if (windowSum >= requiredSum) count++;
                windowSum -= arr[i - k + 1];
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
var numOfSubarrays = function(arr, k, threshold) {
    const need = k * threshold;
    let sum = 0;
    for (let i = 0; i < k; ++i) sum += arr[i];
    let cnt = sum >= need ? 1 : 0;
    for (let i = k; i < arr.length; ++i) {
        sum += arr[i] - arr[i - k];
        if (sum >= need) ++cnt;
    }
    return cnt;
};
```

## Typescript

```typescript
function numOfSubarrays(arr: number[], k: number, threshold: number): number {
    const requiredSum = threshold * k;
    let sum = 0;
    for (let i = 0; i < k; ++i) {
        sum += arr[i];
    }
    let count = sum >= requiredSum ? 1 : 0;
    for (let i = k; i < arr.length; ++i) {
        sum += arr[i] - arr[i - k];
        if (sum >= requiredSum) {
            ++count;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @param Integer $threshold
     * @return Integer
     */
    function numOfSubarrays($arr, $k, $threshold) {
        $target = $threshold * $k;
        $n = count($arr);
        $sum = 0;
        for ($i = 0; $i < $k; $i++) {
            $sum += $arr[$i];
        }
        $count = ($sum >= $target) ? 1 : 0;
        for ($i = $k; $i < $n; $i++) {
            $sum += $arr[$i];
            $sum -= $arr[$i - $k];
            if ($sum >= $target) {
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
    func numOfSubarrays(_ arr: [Int], _ k: Int, _ threshold: Int) -> Int {
        let target = k * threshold
        var sum = 0
        var count = 0
        for i in 0..<arr.count {
            sum += arr[i]
            if i >= k {
                sum -= arr[i - k]
            }
            if i >= k - 1 && sum >= target {
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
    fun numOfSubarrays(arr: IntArray, k: Int, threshold: Int): Int {
        val n = arr.size
        if (k > n) return 0
        val target = threshold.toLong() * k
        var sum = 0L
        for (i in 0 until k) {
            sum += arr[i]
        }
        var count = 0
        if (sum >= target) count++
        for (i in k until n) {
            sum += arr[i].toLong()
            sum -= arr[i - k].toLong()
            if (sum >= target) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numOfSubarrays(List<int> arr, int k, int threshold) {
    int required = k * threshold;
    int sum = 0;
    for (int i = 0; i < k; i++) {
      sum += arr[i];
    }
    int count = sum >= required ? 1 : 0;
    for (int i = k; i < arr.length; i++) {
      sum += arr[i] - arr[i - k];
      if (sum >= required) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numOfSubarrays(arr []int, k int, threshold int) int {
	if len(arr) < k {
		return 0
	}
	target := threshold * k
	sum := 0
	for i := 0; i < k; i++ {
		sum += arr[i]
	}
	count := 0
	if sum >= target {
		count++
	}
	for i := k; i < len(arr); i++ {
		sum += arr[i] - arr[i-k]
		if sum >= target {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def num_of_subarrays(arr, k, threshold)
  target = k * threshold
  sum = arr[0, k].reduce(0, :+)
  count = sum >= target ? 1 : 0

  (k...arr.length).each do |i|
    sum += arr[i] - arr[i - k]
    count += 1 if sum >= target
  end

  count
end
```

## Scala

```scala
object Solution {
  def numOfSubarrays(arr: Array[Int], k: Int, threshold: Int): Int = {
    val need: Long = threshold.toLong * k
    var sum: Long = 0L
    for (i <- 0 until k) {
      sum += arr(i)
    }
    var count = if (sum >= need) 1 else 0
    var i = k
    while (i < arr.length) {
      sum += arr(i).toLong - arr(i - k).toLong
      if (sum >= need) count += 1
      i += 1
    }
    count
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        let n = arr.len();
        let k_usize = k as usize;
        let target = (threshold as i64) * (k as i64);
        let mut sum: i64 = 0;
        let mut count = 0;
        for i in 0..n {
            sum += arr[i] as i64;
            if i >= k_usize {
                sum -= arr[i - k_usize] as i64;
            }
            if i + 1 >= k_usize && sum >= target {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (num-of-subarrays arr k threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([v (list->vector arr)]
         [n (vector-length v)]
         [need (* threshold k)])
    (if (< n k)
        0
        (let* ([initial-sum (for/sum ([i (in-range k)]) (vector-ref v i))]
               [init-count (if (>= initial-sum need) 1 0)])
          (let loop ((i k) (sum initial-sum) (cnt init-count))
            (if (= i n)
                cnt
                (let* ([out-index (- i k)]
                       [new-sum (+ sum (- (vector-ref v i) (vector-ref v out-index)))])
                  (loop (+ i 1) new-sum (if (>= new-sum need) (+ cnt 1) cnt)))))))))
```

## Erlang

```erlang
-spec num_of_subarrays(Arr :: [integer()], K :: integer(), Threshold :: integer()) -> integer().
num_of_subarrays(Arr, K, Threshold) ->
    Target = K * Threshold,
    N = length(Arr),
    if
        N < K -> 0;
        true ->
            ArrT = list_to_tuple(Arr),
            Sum0 = sum_range(ArrT, 1, K),
            Count0 = if Sum0 >= Target -> 1 else 0 end,
            loop(K + 1, N, ArrT, Sum0, K, Target, Count0)
    end.

sum_range(Tuple, Start, End) ->
    sum_range(Tuple, Start, End, 0).

sum_range(_Tuple, I, End, Acc) when I > End -> Acc;
sum_range(Tuple, I, End, Acc) ->
    sum_range(Tuple, I + 1, End, Acc + erlang:element(I, Tuple)).

loop(I, N, _ArrT, _SumPrev, _K, _Target, Count) when I > N -> Count;
loop(I, N, ArrT, SumPrev, K, Target, Count) ->
    NewElem = erlang:element(I, ArrT),
    OldElem = erlang:element(I - K, ArrT),
    Sum = SumPrev - OldElem + NewElem,
    NewCount = if Sum >= Target -> Count + 1; true -> Count end,
    loop(I + 1, N, ArrT, Sum, K, Target, NewCount).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_subarrays(arr :: [integer], k :: integer, threshold :: integer) :: integer
  def num_of_subarrays(arr, k, threshold) do
    target = threshold * k
    n = length(arr)
    tup = List.to_tuple(arr)

    init_sum =
      0..(k - 1)
      |> Enum.reduce(0, fn i, acc -> acc + elem(tup, i) end)

    {count, _} =
      Enum.reduce(1..(n - k), {if(init_sum >= target, do: 1, else: 0), init_sum}, fn i, {c, s} ->
        new_s = s - elem(tup, i - 1) + elem(tup, i + k - 1)
        {if(new_s >= target, do: c + 1, else: c), new_s}
      end)

    count
  end
end
```
