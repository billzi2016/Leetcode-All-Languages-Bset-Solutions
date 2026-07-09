# 1287. Element Appearing More Than 25% In Sorted Array

## Cpp

```cpp
class Solution {
public:
    int findSpecialInteger(std::vector<int>& arr) {
        int n = arr.size();
        int k = n / 4;
        for (int i = 0; i + k < n; ++i) {
            if (arr[i] == arr[i + k]) return arr[i];
        }
        return -1; // guaranteed to never reach here
    }
};
```

## Java

```java
class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int size = n / 4;
        for (int i = 0; i + size < n; i++) {
            if (arr[i] == arr[i + size]) {
                return arr[i];
            }
        }
        // Should never reach here as per problem guarantee
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        step = n // 4
        for i in range(n - step):
            if arr[i] == arr[i + step]:
                return arr[i]
```

## Python3

```python
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        size = n // 4
        for i in range(n - size):
            if arr[i] == arr[i + size]:
                return arr[i]
        # Guaranteed to have an answer; fallback (should never reach here)
        return arr[0]
```

## C

```c
int findSpecialInteger(int* arr, int arrSize) {
    int size = arrSize / 4;
    for (int i = 0; i + size < arrSize; ++i) {
        if (arr[i] == arr[i + size]) {
            return arr[i];
        }
    }
    return arr[0]; // guaranteed to exist
}
```

## Csharp

```csharp
public class Solution {
    public int FindSpecialInteger(int[] arr) {
        int n = arr.Length;
        int size = n / 4; // floor division
        for (int i = 0; i + size < n; i++) {
            if (arr[i] == arr[i + size]) {
                return arr[i];
            }
        }
        // Fallback, though problem guarantees a solution exists
        return arr[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    const n = arr.length;
    const k = Math.floor(n / 4);
    for (let i = 0; i + k < n; ++i) {
        if (arr[i] === arr[i + k]) {
            return arr[i];
        }
    }
    // Should never reach here as per problem guarantee
    return -1;
};
```

## Typescript

```typescript
function findSpecialInteger(arr: number[]): number {
    const n = arr.length;
    const k = Math.floor(n / 4);
    for (let i = 0; i + k < n; i++) {
        if (arr[i] === arr[i + k]) {
            return arr[i];
        }
    }
    return -1; // guaranteed to never reach here
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findSpecialInteger($arr) {
        $n = count($arr);
        $size = intdiv($n, 4); // floor division
        
        for ($i = 0; $i + $size < $n; $i++) {
            if ($arr[$i] === $arr[$i + $size]) {
                return $arr[$i];
            }
        }
        
        // Fallback (should never be reached due to problem guarantees)
        return $arr[0];
    }
}
```

## Swift

```swift
class Solution {
    func findSpecialInteger(_ arr: [Int]) -> Int {
        let n = arr.count
        let k = n / 4
        for i in 0..<(n - k) {
            if arr[i] == arr[i + k] {
                return arr[i]
            }
        }
        // Guaranteed to have an answer; fallback
        return arr[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSpecialInteger(arr: IntArray): Int {
        val n = arr.size
        val k = n / 4
        for (i in 0..n - k - 1) {
            if (arr[i] == arr[i + k]) return arr[i]
        }
        return -1 // guaranteed to never reach here
    }
}
```

## Dart

```dart
class Solution {
  int findSpecialInteger(List<int> arr) {
    int n = arr.length;
    int k = n ~/ 4; // floor division
    for (int i = 0; i + k < n; ++i) {
      if (arr[i] == arr[i + k]) {
        return arr[i];
      }
    }
    return -1; // guaranteed to find an answer before this point
  }
}
```

## Golang

```go
func findSpecialInteger(arr []int) int {
    n := len(arr)
    k := n / 4
    for i := 0; i+k < n; i++ {
        if arr[i] == arr[i+k] {
            return arr[i]
        }
    }
    return -1
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def find_special_integer(arr)
  n = arr.length
  k = n / 4
  (0..n - k - 1).each do |i|
    return arr[i] if arr[i] == arr[i + k]
  end
end
```

## Scala

```scala
object Solution {
    def findSpecialInteger(arr: Array[Int]): Int = {
        val n = arr.length
        val k = n / 4
        for (i <- 0 until n - k) {
            if (arr(i) == arr(i + k)) return arr(i)
        }
        // Fallback, though problem guarantees a solution exists
        arr(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let size = n / 4;
        for i in 0..n - size {
            if arr[i] == arr[i + size] {
                return arr[i];
            }
        }
        // Guaranteed to have an answer
        arr[0]
    }
}
```

## Racket

```racket
(define/contract (find-special-integer arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector arr))
         (n   (vector-length vec))
         (size (quotient n 4))) ; floor division
    (let loop ((i 0))
      (if (>= i (- n size))
          (error "No element found, but problem guarantees existence.")
          (if (= (vector-ref vec i)
                 (vector-ref vec (+ i size)))
              (vector-ref vec i)
              (loop (+ i 1)))))))
```

## Erlang

```erlang
-spec find_special_integer([integer()]) -> integer().
find_special_integer(Arr) ->
    Len = length(Arr),
    Size = Len div 4,
    T = list_to_tuple(Arr),
    loop(T, Len, Size, 0).

loop(_T, Len, Size, I) when I > Len - Size - 1 ->
    %% This case should never be reached because a solution is guaranteed.
    0;
loop(T, Len, Size, I) ->
    A = element(I + 1, T),
    B = element(I + Size + 1, T),
    case A == B of
        true -> A;
        false -> loop(T, Len, Size, I + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_special_integer(arr :: [integer]) :: integer
  def find_special_integer(arr) do
    tup = List.to_tuple(arr)
    len = tuple_size(tup)
    size = div(len, 4)

    Enum.reduce_while(0..(len - size - 1), nil, fn i, _acc ->
      if :erlang.element(i + 1, tup) == :erlang.element(i + size + 1, tup) do
        {:halt, :erlang.element(i + 1, tup)}
      else
        {:cont, nil}
      end
    end)
  end
end
```
