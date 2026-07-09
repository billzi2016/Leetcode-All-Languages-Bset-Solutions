# 0658. Find K Closest Elements

## Cpp

```cpp
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int left = 0, right = n - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // If the element at mid is farther from x than the element at mid+k, move window right
            if (x - arr[mid] > arr[mid + k] - x)
                left = mid + 1;
            else
                right = mid;
        }
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int n = arr.length;
        int left = 0;
        int right = n - k; // inclusive start index bound
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            long distLeft = Math.abs((long)x - arr[mid]);
            long distRight = Math.abs((long)arr[mid + k] - x);
            if (distLeft > distRight) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        List<Integer> result = new ArrayList<>(k);
        for (int i = left; i < left + k; i++) {
            result.add(arr[i]);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import bisect
        n = len(arr)
        # Find the insertion point for x
        idx = bisect.bisect_left(arr, x)

        left = max(0, idx - k - 1)
        right = min(n - 1, idx + k)

        # Shrink window to size k
        while right - left + 1 > k:
            if left < 0:
                left += 1
                continue
            if right >= n:
                right -= 1
                continue
            if abs(arr[left] - x) <= abs(arr[right] - x):
                # left element is closer or equal, discard right
                right -= 1
            else:
                # right element is closer, discard left
                left += 1

        return arr[left:left + k]
```

## Python3

```python
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if abs(x - arr[mid]) > abs(arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
```

## C

```c
#include <stdlib.h>

int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize) {
    int low = 0;
    int high = arrSize - k;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (x - arr[mid] > arr[mid + k] - x)
            low = mid + 1;
        else
            high = mid;
    }
    *returnSize = k;
    int* res = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i) {
        res[i] = arr[low + i];
    }
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> FindClosestElements(int[] arr, int k, int x) {
        int left = 0;
        int right = arr.Length - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            // Compare distances between x and the two potential window edges
            if (x - arr[mid] > arr[mid + k] - x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        List<int> result = new List<int>(k);
        for (int i = left; i < left + k; i++) {
            result.Add(arr[i]);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    let left = 0;
    let right = arr.length - k;
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (Math.abs(x - arr[mid]) > Math.abs(arr[mid + k] - x)) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    return arr.slice(left, left + k);
};
```

## Typescript

```typescript
function findClosestElements(arr: number[], k: number, x: number): number[] {
    let left = 0;
    let right = arr.length - k;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (x - arr[mid] > arr[mid + k] - x) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return arr.slice(left, left + k);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findClosestElements($arr, $k, $x) {
        $n = count($arr);
        $left = 0;
        $right = $n - $k;
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if (abs($x - $arr[$mid]) > abs($arr[$mid + $k] - $x)) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return array_slice($arr, $left, $k);
    }
}
```

## Swift

```swift
class Solution {
    func findClosestElements(_ arr: [Int], _ k: Int, _ x: Int) -> [Int] {
        var left = 0
        var right = arr.count - k
        while left < right {
            let mid = (left + right) / 2
            if x - arr[mid] > arr[mid + k] - x {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return Array(arr[left..<(left + k)])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        var left = 0
        var right = arr.size - k
        while (left < right) {
            val mid = (left + right) ushr 1
            val diffLeft = kotlin.math.abs(arr[mid] - x)
            val diffRight = kotlin.math.abs(arr[mid + k] - x)
            if (diffLeft > diffRight) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        val result = ArrayList<Int>(k)
        for (i in left until left + k) {
            result.add(arr[i])
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findClosestElements(List<int> arr, int k, int x) {
    int n = arr.length;
    int left = 0;
    int right = n - k;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (x - arr[mid] > arr[mid + k] - x) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return arr.sublist(left, left + k);
  }
}
```

## Golang

```go
func findClosestElements(arr []int, k int, x int) []int {
	n := len(arr)
	left, right := 0, n-k
	for left < right {
		mid := (left + right) / 2
		if x-arr[mid] > arr[mid+k]-x {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return arr[left : left+k]
}
```

## Ruby

```ruby
def find_closest_elements(arr, k, x)
  left = 0
  right = arr.length - k
  while left < right
    mid = (left + right) / 2
    if x - arr[mid] > arr[mid + k] - x
      left = mid + 1
    else
      right = mid
    end
  end
  arr[left, k]
end
```

## Scala

```scala
object Solution {
    def findClosestElements(arr: Array[Int], k: Int, x: Int): List[Int] = {
        var left = 0
        var right = arr.length - k
        while (left < right) {
            val mid = left + (right - left) / 2
            val leftDist = x.toLong - arr(mid).toLong
            val rightDist = arr(mid + k).toLong - x.toLong
            if (leftDist > rightDist) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        arr.slice(left, left + k).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let n = arr.len();
        let k_usize = k as usize;
        if k_usize == 0 {
            return vec![];
        }
        let mut left = 0usize;
        let mut right = n - k_usize; // inclusive upper bound for start index
        while left < right {
            let mid = (left + right) / 2;
            let dist_left = (x as i64 - arr[mid] as i64).abs();
            let dist_right = (arr[mid + k_usize] as i64 - x as i64).abs();
            if dist_left > dist_right {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        arr[left..left + k_usize].to_vec()
    }
}
```

## Racket

```racket
(define/contract (find-closest-elements arr k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (let loop ((low 0) (high (- n k)))
      (if (< low high)
          (let* ((mid (quotient (+ low high) 2))
                 (left (vector-ref v mid))
                 (right (vector-ref v (+ mid k)))
                 (diff-left (- x left))
                 (diff-right (- right x)))
            (if (> diff-left diff-right)
                (loop (+ mid 1) high)
                (loop low mid)))
          (let ((start low))
            (for/list ((i (in-range start (+ start k))))
              (vector-ref v i))))))
```

## Erlang

```erlang
-spec find_closest_elements(Arr :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_closest_elements(Arr, K, X) ->
    Pairs = [{erlang:abs(V - X), V} || V <- Arr],
    SortedPairs = lists:sort(Pairs),
    FirstK = lists:sublist(SortedPairs, K),
    Values = [V || {_D, V} <- FirstK],
    lists:sort(Values).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_closest_elements(arr :: [integer], k :: integer, x :: integer) :: [integer]
  def find_closest_elements(arr, k, x) do
    tup = List.to_tuple(arr)
    n = tuple_size(tup)

    left = binary_search(tup, x, k, 0, n - k)

    for i <- left..(left + k - 1), do: elem(tup, i)
  end

  defp binary_search(_tup, _x, _k, low, high) when low >= high, do: low

  defp binary_search(tup, x, k, low, high) do
    mid = div(low + high, 2)

    left_val = elem(tup, mid)
    right_val = elem(tup, mid + k)

    if abs(x - left_val) > abs(right_val - x) do
      binary_search(tup, x, k, mid + 1, high)
    else
      binary_search(tup, x, k, low, mid)
    end
  end
end
```
