# 1588. Sum of All Odd Length Subarrays

## Cpp

```cpp
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        long long total = 0;
        int n = arr.size();
        for (int i = 0; i < n; ++i) {
            int left = i + 1;
            int right = n - i;
            long long oddLeft = (left + 1) / 2;
            long long evenLeft = left / 2;
            long long oddRight = (right + 1) / 2;
            long long evenRight = right / 2;
            long long count = oddLeft * oddRight + evenLeft * evenRight;
            total += arr[i] * count;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        long total = 0;
        for (int i = 0; i < n; i++) {
            long count = ((long)(i + 1) * (n - i) + 1) / 2;
            total += arr[i] * count;
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total = 0
        for i, val in enumerate(arr):
            left = i + 1          # number of choices for the start position
            right = n - i         # number of choices for the end position
            odd_count = ((left + 1) // 2) * ((right + 1) // 2) + (left // 2) * (right // 2)
            total += val * odd_count
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i, val in enumerate(arr):
            left = i + 1
            right = n - i
            odd_left = (left + 1) // 2
            even_left = left // 2
            odd_right = (right + 1) // 2
            even_right = right // 2
            count = odd_left * odd_right + even_left * even_right
            total += val * count
        return total
```

## C

```c
int sumOddLengthSubarrays(int* arr, int arrSize) {
    long long total = 0;
    for (int i = 0; i < arrSize; ++i) {
        int left = i + 1;
        int right = arrSize - i;

        int evens_left = i / 2 + 1;
        int odds_left = left - evens_left;

        int evens_right;
        if (i % 2 == 0) {
            evens_right = (right + 1) / 2; // first index is even
        } else {
            evens_right = right / 2;       // first index is odd
        }
        int odds_right = right - evens_right;

        long long count = (long long)evens_left * evens_right +
                          (long long)odds_left * odds_right;
        total += (long long)arr[i] * count;
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        int n = arr.Length;
        long total = 0;
        for (int i = 0; i < n; i++) {
            int leftCount = i + 1;
            int rightCount = n - i;

            int oddLeft = (leftCount + 1) / 2;
            int evenLeft = leftCount / 2;
            int oddRight = (rightCount + 1) / 2;
            int evenRight = rightCount / 2;

            long occurrences = (long)oddLeft * oddRight + (long)evenLeft * evenRight;
            total += arr[i] * occurrences;
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    const n = arr.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        const left = i + 1;
        const right = n - i;
        const oddLeft = Math.ceil(left / 2);
        const evenLeft = Math.floor(left / 2);
        const oddRight = Math.ceil(right / 2);
        const evenRight = Math.floor(right / 2);
        const count = oddLeft * oddRight + evenLeft * evenRight;
        total += arr[i] * count;
    }
    return total;
};
```

## Typescript

```typescript
function sumOddLengthSubarrays(arr: number[]): number {
    const n = arr.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        const left = i + 1;
        const right = n - i;
        const oddLeft = Math.ceil(left / 2);
        const evenLeft = Math.floor(left / 2);
        const oddRight = Math.ceil(right / 2);
        const evenRight = Math.floor(right / 2);
        total += arr[i] * (oddLeft * oddRight + evenLeft * evenRight);
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumOddLengthSubarrays($arr) {
        $n = count($arr);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $left = $i + 1;
            $right = $n - $i;
            $count = intdiv($left * $right + 1, 2);
            $ans += $arr[$i] * $count;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumOddLengthSubarrays(_ arr: [Int]) -> Int {
        let n = arr.count
        var total = 0
        for i in 0..<n {
            let left = i + 1
            let right = n - i
            let oddLeft = (left + 1) / 2
            let evenLeft = left - oddLeft
            let oddRight = (right + 1) / 2
            let evenRight = right - oddRight
            total += arr[i] * (oddLeft * oddRight + evenLeft * evenRight)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOddLengthSubarrays(arr: IntArray): Int {
        val n = arr.size
        var total = 0L
        for (i in 0 until n) {
            val left = i + 1
            val right = n - i
            val oddLeft = (left + 1) / 2
            val evenLeft = left / 2
            val oddRight = (right + 1) / 2
            val evenRight = right / 2
            val count = oddLeft * oddRight + evenLeft * evenRight
            total += arr[i].toLong() * count
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumOddLengthSubarrays(List<int> arr) {
    int n = arr.length;
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
      int count = (i + 1) * (n - i);
      int oddCount = ((count) + 1) ~/ 2;
      totalSum += arr[i] * oddCount;
    }
    return totalSum;
  }
}
```

## Golang

```go
func sumOddLengthSubarrays(arr []int) int {
    n := len(arr)
    total := 0
    for i, v := range arr {
        left := i + 1
        right := n - i

        oddLeft := (left + 1) / 2
        evenLeft := left / 2
        oddRight := (right + 1) / 2
        evenRight := right / 2

        count := oddLeft*oddRight + evenLeft*evenRight
        total += v * count
    }
    return total
}
```

## Ruby

```ruby
def sum_odd_length_subarrays(arr)
  n = arr.length
  total = 0
  arr.each_with_index do |val, i|
    left = i + 1
    right = n - i
    odd_left = (left + 1) / 2
    even_left = left / 2
    odd_right = (right + 1) / 2
    even_right = right / 2
    total += val * (odd_left * odd_right + even_left * even_right)
  end
  total
end
```

## Scala

```scala
object Solution {
    def sumOddLengthSubarrays(arr: Array[Int]): Int = {
        val n = arr.length
        var total: Long = 0L
        for (i <- 0 until n) {
            val left = i + 1
            val right = n - i
            val oddLeft = (left + 1) / 2
            val evenLeft = left / 2
            val oddRight = (right + 1) / 2
            val evenRight = right / 2
            val count = oddLeft * oddRight + evenLeft * evenRight
            total += arr(i).toLong * count
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let n = arr.len() as i64;
        let mut ans: i64 = 0;
        for (i, &val) in arr.iter().enumerate() {
            let left = i as i64 + 1;
            let right = n - i as i64;
            let total = left * right;
            let odd_cnt = (total + 1) / 2;
            ans += val as i64 * odd_cnt;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (sum-odd-length-subarrays arr)
  (-> (listof exact-integer?) exact-integer?)
  (let ((n (length arr)))
    (let loop ((i 0) (lst arr) (acc 0))
      (if (null? lst)
          acc
          (let* ((val (car lst))
                 (total (* (+ i 1) (- n i)))        ; number of subarrays containing arr[i]
                 (odd-count (quotient (+ total 1) 2))) ; odd-length subarrays count
            (loop (add1 i) (cdr lst) (+ acc (* val odd-count))))))))
```

## Erlang

```erlang
-spec sum_odd_length_subarrays(Arr :: [integer()]) -> integer().
sum_odd_length_subarrays(Arr) ->
    N = length(Arr),
    {_, Sum} = lists:foldl(
        fun (Val, {Idx, Acc}) ->
            Left = Idx,
            Right = N - 1 - Idx,
            OddLeft = Left div 2 + 1,
            OddRight = Right div 2 + 1,
            EvenLeft = (Left + 1) div 2,
            EvenRight = (Right + 1) div 2,
            Count = OddLeft * OddRight + EvenLeft * EvenRight,
            {Idx + 1, Acc + Val * Count}
        end,
        {0, 0},
        Arr
    ),
    Sum.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_odd_length_subarrays(arr :: [integer]) :: integer
  def sum_odd_length_subarrays(arr) do
    n = length(arr)

    Enum.with_index(arr)
    |> Enum.reduce(0, fn {val, i}, acc ->
      left = i
      right = n - i - 1

      odd_left = div(left + 1, 2)
      even_left = div(left, 2) + 1
      odd_right = div(right + 1, 2)
      even_right = div(right, 2) + 1

      count = odd_left * odd_right + even_left * even_right
      acc + val * count
    end)
  end
end
```
