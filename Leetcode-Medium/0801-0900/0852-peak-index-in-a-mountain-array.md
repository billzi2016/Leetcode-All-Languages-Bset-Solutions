# 0852. Peak Index in a Mountain Array

## Cpp

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 0, right = (int)arr.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < arr[mid + 1])
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

## Python3

```python
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

## C

```c
int peakIndexInMountainArray(int* arr, int arrSize) {
    int left = 0;
    int right = arrSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] < arr[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

## Csharp

```csharp
public class Solution {
    public int PeakIndexInMountainArray(int[] arr) {
        int left = 0;
        int right = arr.Length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] < arr[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
};
```

## Typescript

```typescript
function peakIndexInMountainArray(arr: number[]): number {
    let left = 0;
    let right = arr.length - 1;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] < arr[mid + 1]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function peakIndexInMountainArray($arr) {
        $l = 0;
        $r = count($arr) - 1;
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] < $arr[$mid + 1]) {
                $l = $mid + 1;
            } else {
                $r = $mid;
            }
        }
        return $l;
    }
}
```

## Swift

```swift
class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        var left = 0
        var right = arr.count - 1
        while left < right {
            let mid = (left + right) / 2
            if arr[mid] < arr[mid + 1] {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun peakIndexInMountainArray(arr: IntArray): Int {
        var left = 0
        var right = arr.size - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int peakIndexInMountainArray(List<int> arr) {
    int left = 0;
    int right = arr.length - 1;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid] < arr[mid + 1]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
func peakIndexInMountainArray(arr []int) int {
    left, right := 0, len(arr)-1
    for left < right {
        mid := (left + right) / 2
        if arr[mid] < arr[mid+1] {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}
```

## Ruby

```ruby
def peak_index_in_mountain_array(arr)
  left = 0
  right = arr.length - 1
  while left < right
    mid = left + (right - left) / 2
    if arr[mid] < arr[mid + 1]
      left = mid + 1
    else
      right = mid
    end
  end
  left
end
```

## Scala

```scala
object Solution {
  def peakIndexInMountainArray(arr: Array[Int]): Int = {
    var left = 0
    var right = arr.length - 1
    while (left < right) {
      val mid = left + (right - left) / 2
      if (arr(mid) < arr(mid + 1)) {
        left = mid + 1
      } else {
        right = mid
      }
    }
    left
  }
}
```

## Rust

```rust
impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut l = 0usize;
        let mut r = arr.len() - 1;
        while l < r {
            let mid = (l + r) / 2;
            if arr[mid] < arr[mid + 1] {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        l as i32
    }
}
```

## Racket

```racket
(define/contract (peak-index-in-mountain-array arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (let loop ((l 0) (r (- n 1)))
      (if (= l r)
          l
          (let ((mid (quotient (+ l r) 2)))
            (if (< (vector-ref v mid) (vector-ref v (+ mid 1)))
                (loop (+ mid 1) r)
                (loop l mid)))))))
```

## Erlang

```erlang
-spec peak_index_in_mountain_array(Arr :: [integer()]) -> integer().
peak_index_in_mountain_array(Arr) ->
    find_peak(Arr, 0).

find_peak([_], Idx) -> Idx;
find_peak([A,B|Rest], Idx) when A < B ->
    find_peak([B|Rest], Idx + 1);
find_peak(_, Idx) ->
    Idx.
```

## Elixir

```elixir
defmodule Solution do
  @spec peak_index_in_mountain_array(arr :: [integer]) :: integer
  def peak_index_in_mountain_array(arr) do
    find_peak(arr, 0)
  end

  defp find_peak([prev, curr | rest], idx) do
    if prev < curr do
      find_peak([curr | rest], idx + 1)
    else
      idx
    end
  end
end
```
