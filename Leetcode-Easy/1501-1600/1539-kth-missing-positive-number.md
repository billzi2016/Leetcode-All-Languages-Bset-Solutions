# 1539. Kth Missing Positive Number

## Cpp

```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int n = arr.size();
        auto missing = [&](int idx) { return arr[idx] - (idx + 1); };
        
        int left = 0, right = n - 1, idx = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (missing(mid) >= k) {
                idx = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        if (idx == n) {
            return arr.back() + (k - missing(n - 1));
        }
        if (idx == 0) {
            return k;
        }
        int missPrev = missing(idx - 1);
        return arr[idx - 1] + (k - missPrev);
    }
};
```

## Java

```java
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int n = arr.length;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int missing = arr[mid] - (mid + 1);
            if (missing < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        // left is the first index where missing >= k, or n if none
        if (left == n) {
            int missingLast = arr[n - 1] - n;
            return arr[n - 1] + (k - missingLast);
        } else {
            int missingAtLeft = arr[left] - (left + 1);
            return arr[left] - (missingAtLeft - k + 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        # left is the first index where missing >= k, or len(arr) if none.
        if left == 0:
            return k
        if left == len(arr):
            return arr[-1] + (k - (arr[-1] - len(arr)))
        missing_before = arr[left - 1] - left
        return arr[left - 1] + (k - missing_before)
```

## Python3

```python
from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        # left is the first index where missing >= k, or n if none.
        if left == 0:
            return k
        if left == n:
            # all missing counts are less than k
            missing_before = arr[-1] - n
            return arr[-1] + (k - missing_before)

        missing_before = arr[left - 1] - left
        return arr[left - 1] + (k - missing_before)
```

## C

```c
int findKthPositive(int* arr, int arrSize, int k) {
    int low = 0, high = arrSize - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int missing = arr[mid] - (mid + 1);
        if (missing < k)
            low = mid + 1;
        else
            high = mid - 1;
    }
    if (low == 0)
        return k;
    if (low == arrSize) {
        int missingLast = arr[arrSize - 1] - arrSize;
        return arr[arrSize - 1] + (k - missingLast);
    }
    int missingPrev = arr[low - 1] - low;
    return arr[low - 1] + (k - missingPrev);
}
```

## Csharp

```csharp
public class Solution {
    public int FindKthPositive(int[] arr, int k) {
        int n = arr.Length;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int missing = arr[mid] - (mid + 1);
            if (missing < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if (left == 0) return k;
        int missingPrev = arr[left - 1] - left;
        return arr[left - 1] + (k - missingPrev);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    const n = arr.length;
    const missingLast = arr[n - 1] - n; // total missing up to last element
    
    if (k > missingLast) {
        return arr[n - 1] + (k - missingLast);
    }
    
    let left = 0, right = n - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        const missing = arr[mid] - (mid + 1);
        if (missing < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    const missingAtLeft = arr[left] - (left + 1);
    return arr[left] - (missingAtLeft - k + 1);
};
```

## Typescript

```typescript
function findKthPositive(arr: number[], k: number): number {
    const n = arr.length;
    let left = 0, right = n - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const missing = arr[mid] - (mid + 1);
        if (missing < k) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    // left is the first index with missing >= k, or n if none
    if (left === n) {
        const missingLast = arr[n - 1] - n;
        return arr[n - 1] + (k - missingLast);
    } else {
        const missingBefore = arr[left] - (left + 1);
        return arr[left] - (missingBefore - k + 1);
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findKthPositive($arr, $k) {
        $n = count($arr);
        $left = 0;
        $right = $n - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            $missing = $arr[$mid] - ($mid + 1);
            if ($missing < $k) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        // $left is the first index where missing >= k
        if ($left == 0) {
            return $k;
        }
        $missingPrev = $arr[$left - 1] - $left; // missing count before this position
        return $arr[$left - 1] + ($k - $missingPrev);
    }
}
```

## Swift

```swift
class Solution {
    func findKthPositive(_ arr: [Int], _ k: Int) -> Int {
        var left = 0
        var right = arr.count - 1
        
        while left <= right {
            let mid = left + (right - left) / 2
            let missing = arr[mid] - (mid + 1)
            if missing < k {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        
        // left is the first index where missing >= k, or arr.count if none
        if left == 0 {
            return k
        }
        if left == arr.count {
            let missingLast = arr[arr.count - 1] - arr.count
            return arr[arr.count - 1] + (k - missingLast)
        }
        
        let missingPrev = arr[left - 1] - left
        return arr[left - 1] + (k - missingPrev)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthPositive(arr: IntArray, k: Int): Int {
        var left = 0
        var right = arr.size - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            val missing = arr[mid] - (mid + 1)
            if (missing < k) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return if (left == arr.size) {
            val missingLast = arr[arr.size - 1] - arr.size
            arr[arr.size - 1] + (k - missingLast)
        } else {
            k + left
        }
    }
}
```

## Dart

```dart
class Solution {
  int findKthPositive(List<int> arr, int k) {
    int n = arr.length;
    int missingLast = arr[n - 1] - n;
    if (k > missingLast) {
      return arr[n - 1] + (k - missingLast);
    }
    int left = 0, right = n - 1;
    while (left < right) {
      int mid = (left + right) ~/ 2;
      int missing = arr[mid] - (mid + 1);
      if (missing < k) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    int idx = left;
    int missingPrev = idx == 0 ? 0 : arr[idx - 1] - idx;
    int prevVal = idx == 0 ? 0 : arr[idx - 1];
    return prevVal + (k - missingPrev);
  }
}
```

## Golang

```go
func findKthPositive(arr []int, k int) int {
    n := len(arr)
    left, right := 0, n-1
    for left <= right {
        mid := left + (right-left)/2
        missing := arr[mid] - (mid + 1)
        if missing < k {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    // left is the first index where missing >= k, or n if none.
    if left == 0 {
        return k
    }
    if left == n {
        totalMissing := arr[n-1] - n
        return arr[n-1] + (k - totalMissing)
    }
    missingBefore := arr[left-1] - left
    return arr[left-1] + (k - missingBefore)
}
```

## Ruby

```ruby
def find_kth_positive(arr, k)
  left = 0
  right = arr.length - 1
  while left <= right
    mid = (left + right) / 2
    missing = arr[mid] - (mid + 1)
    if missing < k
      left = mid + 1
    else
      right = mid - 1
    end
  end

  if left == 0
    k
  elsif left == arr.length
    missing_last = arr[-1] - arr.length
    arr[-1] + (k - missing_last)
  else
    missing_before = arr[left - 1] - left
    arr[left - 1] + (k - missing_before)
  end
end
```

## Scala

```scala
object Solution {
    def findKthPositive(arr: Array[Int], k: Int): Int = {
        var left = 0
        var right = arr.length - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            val miss = arr(mid) - (mid + 1)
            if (miss < k) left = mid + 1 else right = mid - 1
        }
        left + k
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        // binary search for first index where missing >= k
        let mut left = 0usize;
        let mut right = n; // exclusive
        while left < right {
            let mid = (left + right) / 2;
            let missing = arr[mid] - (mid as i32 + 1);
            if missing < k {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        if left == n {
            // kth missing is after the last element
            let missing_last = arr[n - 1] - (n as i32);
            arr[n - 1] + (k - missing_last)
        } else {
            // kth missing is before arr[left]
            let missing_before = arr[left] - (left as i32 + 1);
            arr[left] - (missing_before - k + 1)
        }
    }
}
```

## Racket

```racket
(define/contract (find-kth-positive arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (let loop ((low 0) (high (- n 1)) (ans n))
      (if (> low high)
          (+ k ans)
          (let* ((mid (quotient (+ low high) 2))
                 (missing (- (vector-ref v mid) (+ mid 1))))
            (if (>= missing k)
                (loop low (- mid 1) mid)
                (loop (+ mid 1) high ans)))))))
```

## Erlang

```erlang
-spec find_kth_positive([integer()], integer()) -> integer().
find_kth_positive(Arr, K) ->
    find_kth_positive(Arr, K, 0, 0).

find_kth_positive([], K, Prev, Missing) ->
    Prev + (K - Missing);
find_kth_positive([H|T], K, Prev, Missing) ->
    Gap = H - Prev - 1,
    case Missing + Gap >= K of
        true -> Prev + (K - Missing);
        false -> find_kth_positive(T, K, H, Missing + Gap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_kth_positive(arr :: [integer], k :: integer) :: integer
  def find_kth_positive(arr, k) do
    n = length(arr)

    {low, _} = bs(arr, k, 0, n - 1)

    if low == n do
      last = List.last(arr)
      missing_last = last - n
      last + (k - missing_last)
    else
      k + low
    end
  end

  defp bs(_arr, _k, low, high) when low > high, do: {low, high}

  defp bs(arr, k, low, high) do
    mid = div(low + high, 2)
    missing = Enum.at(arr, mid) - (mid + 1)

    if missing < k do
      bs(arr, k, mid + 1, high)
    else
      bs(arr, k, low, mid - 1)
    end
  end
end
```
