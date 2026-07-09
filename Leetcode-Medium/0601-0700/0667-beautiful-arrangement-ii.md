# 0667. Beautiful Arrangement II

## Cpp

```cpp
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        vector<int> ans;
        // First part: increasing sequence up to n-k-1
        for (int i = 1; i <= n - k - 1; ++i) {
            ans.push_back(i);
        }
        // Second part: alternating low/high within the remaining range
        int low = n - k;
        int high = n;
        while (low <= high) {
            ans.push_back(low++);
            if (low <= high) {
                ans.push_back(high--);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] constructArray(int n, int k) {
        int[] ans = new int[n];
        int idx = 0;
        // First part: increasing sequence up to n - k - 1
        for (int i = 1; i <= n - k - 1; i++) {
            ans[idx++] = i;
        }
        int low = n - k;
        int high = n;
        while (low <= high) {
            ans[idx++] = low++;
            if (idx == n) break;
            ans[idx++] = high--;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        # first part: increasing sequence to create only 1 difference
        for i in range(1, n - k):
            res.append(i)
        left, right = n - k, n
        while left <= right:
            res.append(left)
            left += 1
            if left <= right:
                res.append(right)
                right -= 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [i for i in range(1, n - k)]
        low, high = n - k, n
        turn_low = True
        while low <= high:
            if turn_low:
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
            turn_low = not turn_low
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructArray(int n, int k, int* returnSize) {
    *returnSize = n;
    int* ans = (int*)malloc(n * sizeof(int));
    int idx = 0;

    // First part: increasing sequence from 1 to n-k-1
    for (int i = 1; i <= n - k - 1; ++i) {
        ans[idx++] = i;
    }

    // Remaining k+1 elements: alternating low/high to create distinct differences
    int low = n - k;
    int high = n;
    while (low <= high) {
        ans[idx++] = low++;
        if (low <= high) {
            ans[idx++] = high--;
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ConstructArray(int n, int k)
    {
        int[] ans = new int[n];
        int idx = 0;

        // First part: increasing sequence up to n - k - 1
        for (int i = 1; i <= n - k - 1; i++)
        {
            ans[idx++] = i;
        }

        // Second part: alternate low and high within the remaining range
        int low = n - k;
        int high = n;
        while (low <= high)
        {
            ans[idx++] = low++;
            if (low <= high)
            {
                ans[idx++] = high--;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var constructArray = function(n, k) {
    const ans = [];
    // first part: 1 .. n-k-1 (if any)
    for (let i = 1; i <= n - k - 1; ++i) {
        ans.push(i);
    }
    // second part: alternating low/high within the remaining k+1 numbers
    const start = n - k;
    for (let i = 0; i <= k; ++i) {
        if (i % 2 === 0) {
            ans.push(start + Math.floor(i / 2));
        } else {
            ans.push(n - Math.floor(i / 2));
        }
    }
    return ans;
};
```

## Typescript

```typescript
function constructArray(n: number, k: number): number[] {
    const res: number[] = [];
    for (let i = 1; i <= n - k - 1; ++i) {
        res.push(i);
    }
    let low = n - k;
    let high = n;
    while (low <= high) {
        res.push(low);
        low++;
        if (low > high) break;
        res.push(high);
        high--;
    }
    return res;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function constructArray($n, $k) {
        $res = [];
        // First part: 1 .. n-k-1 (if any)
        for ($i = 1; $i <= $n - $k - 1; $i++) {
            $res[] = $i;
        }
        $low = $n - $k;
        $high = $n;
        // Second part: alternating low/high to create k distinct differences
        for ($i = 0; $i <= $k; $i++) {
            if (($i & 1) == 0) {
                $val = $low + intdiv($i, 2);
            } else {
                $val = $high - intdiv($i, 2);
            }
            $res[] = $val;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func constructArray(_ n: Int, _ k: Int) -> [Int] {
        var ans = [Int]()
        let prefixCount = n - k - 1
        if prefixCount > 0 {
            for i in 1...prefixCount {
                ans.append(i)
            }
        }
        var low = n - k
        var high = n
        while low <= high {
            ans.append(low)
            low += 1
            if low <= high {
                ans.append(high)
                high -= 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructArray(n: Int, k: Int): IntArray {
        val ans = IntArray(n)
        var idx = 0
        val prefix = n - k - 1
        for (i in 1..prefix) {
            ans[idx++] = i
        }
        val lowStart = n - k
        val highEnd = n
        for (i in 0..k) {
            if (i % 2 == 0) {
                ans[idx++] = lowStart + i / 2
            } else {
                ans[idx++] = highEnd - i / 2
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> constructArray(int n, int k) {
    List<int> ans = List.filled(n, 0);
    int idx = 0;
    for (int i = 1; i <= n - k - 1; ++i) {
      ans[idx++] = i;
    }
    int low = n - k;
    int high = n;
    while (low <= high) {
      ans[idx++] = low;
      low++;
      if (low <= high) {
        ans[idx++] = high;
        high--;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func constructArray(n int, k int) []int {
    res := make([]int, n)
    idx := 0
    // First part: increasing sequence from 1 to n-k-1
    for i := 1; i <= n-k-1; i++ {
        res[idx] = i
        idx++
    }
    // Second part: alternating low/high within the remaining range
    left, right := n-k, n
    for i := 0; i <= k; i++ {
        if i%2 == 0 {
            res[idx] = left
            left++
        } else {
            res[idx] = right
            right--
        }
        idx++
    }
    return res
}
```

## Ruby

```ruby
def construct_array(n, k)
  result = []
  # Add the initial increasing sequence
  (1..(n - k - 1)).each { |i| result << i }

  low = n - k
  high = n
  (0..k).each do |i|
    if i.even?
      result << low
      low += 1
    else
      result << high
      high -= 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def constructArray(n: Int, k: Int): Array[Int] = {
        val res = new scala.collection.mutable.ArrayBuffer[Int](n)
        // First part: 1 .. n-k-1
        for (i <- 1 until n - k) {
            res += i
        }
        var left = n - k
        var right = n
        while (left <= right) {
            res += left
            left += 1
            if (left <= right) {
                res += right
                right -= 1
            }
        }
        res.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {
        let mut ans = Vec::with_capacity(n as usize);
        // First part: 1 .. n-k-1
        for v in 1..=n - k - 1 {
            ans.push(v);
        }
        // Remaining part: alternating low/high from the last k+1 numbers
        let mut low = n - k;
        let mut high = n;
        for i in 0..=k {
            if i % 2 == 0 {
                ans.push(low);
                low += 1;
            } else {
                ans.push(high);
                high -= 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (construct-array n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let* ((prefix-end (- n k 1))
         (prefix (if (> prefix-end 0)
                     (for/list ([i (in-range 1 (add1 prefix-end))]) i)
                     '()))
         (remaining (+ k 1))
         (low-start (- n k))
         (alt
          (let loop ((i 0) (low low-start) (high n) (acc '()))
            (if (= i remaining)
                (reverse acc)
                (if (even? i)
                    (loop (add1 i) (add1 low) high (cons low acc))
                    (loop (add1 i) low (sub1 high) (cons high acc)))))))
    (append prefix alt)))
```

## Erlang

```erlang
-module(solution).
-export([construct_array/2]).

-spec construct_array(N :: integer(), K :: integer()) -> [integer()].
construct_array(N, K) ->
    PrefixLen = N - K - 1,
    Prefix = case PrefixLen > 0 of
        true -> lists:seq(1, PrefixLen);
        false -> []
    end,
    Alternating = build_alternating(N, K),
    Prefix ++ Alternating.

build_alternating(N, K) ->
    build_alternating(N, K, 0, []).

build_alternating(_N, _K, I, Acc) when I > K ->
    lists:reverse(Acc);
build_alternating(N, K, I, Acc) ->
    Val = case (I rem 2) of
        0 -> N - K + I div 2;
        1 -> N - I div 2
    end,
    build_alternating(N, K, I + 1, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_array(n :: integer, k :: integer) :: [integer]
  def construct_array(n, k) do
    prefix_len = n - k - 1

    prefix =
      if prefix_len > 0 do
        Enum.to_list(1..prefix_len)
      else
        []
      end

    suffix =
      for i <- 0..k do
        if rem(i, 2) == 0 do
          (n - k) + div(i, 2)
        else
          n - div(i, 2)
        end
      end

    prefix ++ suffix
  end
end
```
