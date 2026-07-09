# 1299. Replace Elements with Greatest Element on Right Side

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int maxSoFar = -1;
        for (int i = (int)arr.size() - 1; i >= 0; --i) {
            int current = arr[i];
            arr[i] = maxSoFar;
            if (current > maxSoFar) maxSoFar = current;
        }
        return arr;
    }
};
```

## Java

```java
class Solution {
    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        int maxSoFar = -1;
        for (int i = n - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = maxSoFar;
            if (current > maxSoFar) {
                maxSoFar = current;
            }
        }
        return arr;
    }
}
```

## Python

```python
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
                max_right = current
        return arr
```

## Python3

```python
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            if current > max_so_far:
                max_so_far = current
        return arr
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    *returnSize = arrSize;
    int* result = (int*)malloc(sizeof(int) * arrSize);
    if (!result) {
        *returnSize = 0;
        return NULL;
    }
    int maxSoFar = -1;
    for (int i = arrSize - 1; i >= 0; --i) {
        result[i] = maxSoFar;
        if (arr[i] > maxSoFar) {
            maxSoFar = arr[i];
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int maxSoFar = -1;
        for (int i = arr.Length - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = maxSoFar;
            if (current > maxSoFar) {
                maxSoFar = current;
            }
        }
        return arr;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    let maxSoFar = -1;
    for (let i = arr.length - 1; i >= 0; i--) {
        const current = arr[i];
        arr[i] = maxSoFar;
        if (current > maxSoFar) maxSoFar = current;
    }
    return arr;
};
```

## Typescript

```typescript
function replaceElements(arr: number[]): number[] {
    let maxSoFar = -1;
    for (let i = arr.length - 1; i >= 0; i--) {
        const current = arr[i];
        arr[i] = maxSoFar;
        if (current > maxSoFar) {
            maxSoFar = current;
        }
    }
    return arr;
};
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function replaceElements($arr) {
        $maxSoFar = -1;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $current = $arr[$i];
            $arr[$i] = $maxSoFar;
            if ($current > $maxSoFar) {
                $maxSoFar = $current;
            }
        }
        return $arr;
    }
}
```

## Swift

```swift
class Solution {
    func replaceElements(_ arr: [Int]) -> [Int] {
        var result = arr
        var maxSoFar = -1
        for i in stride(from: arr.count - 1, through: 0, by: -1) {
            let current = result[i]
            result[i] = maxSoFar
            if current > maxSoFar {
                maxSoFar = current
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        var maxSoFar = -1
        for (i in arr.indices.reversed()) {
            val current = arr[i]
            arr[i] = maxSoFar
            if (current > maxSoFar) {
                maxSoFar = current
            }
        }
        return arr
    }
}
```

## Dart

```dart
class Solution {
  List<int> replaceElements(List<int> arr) {
    int maxSoFar = -1;
    for (int i = arr.length - 1; i >= 0; i--) {
      int current = arr[i];
      arr[i] = maxSoFar;
      if (current > maxSoFar) {
        maxSoFar = current;
      }
    }
    return arr;
  }
}
```

## Golang

```go
func replaceElements(arr []int) []int {
    maxVal := -1
    for i := len(arr) - 1; i >= 0; i-- {
        current := arr[i]
        arr[i] = maxVal
        if current > maxVal {
            maxVal = current
        }
    }
    return arr
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def replace_elements(arr)
  max_right = -1
  (arr.length - 1).downto(0) do |i|
    current = arr[i]
    arr[i] = max_right
    max_right = current if current > max_right
  end
  arr
end
```

## Scala

```scala
object Solution {
    def replaceElements(arr: Array[Int]): Array[Int] = {
        var maxSoFar = -1
        for (i <- arr.indices.reverse) {
            val current = arr(i)
            arr(i) = maxSoFar
            if (current > maxSoFar) maxSoFar = current
        }
        arr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut res = arr;
        let mut max_right = -1;
        for i in (0..res.len()).rev() {
            let cur = res[i];
            res[i] = max_right;
            if cur > max_right {
                max_right = cur;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (replace-elements arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((xs (reverse arr))
             (max-so-far -1)
             (result '()))
    (if (null? xs)
        result
        (let* ((x (car xs))
               (new-val max-so-far)
               (new-max (max x max-so-far)))
          (loop (cdr xs) new-max (cons new-val result))))))
```

## Erlang

```erlang
-spec replace_elements(Arr :: [integer()]) -> [integer()].
replace_elements(Arr) ->
    Rev = lists:reverse(Arr),
    {_, Result} = lists:foldl(
        fun(X, {MaxSoFar, Acc}) ->
            NewAcc = [MaxSoFar | Acc],
            NewMax = erlang:max(X, MaxSoFar),
            {NewMax, NewAcc}
        end,
        {-1, []},
        Rev),
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec replace_elements(arr :: [integer]) :: [integer]
  def replace_elements(arr) do
    {result, _} =
      arr
      |> Enum.reverse()
      |> Enum.reduce({[], -1}, fn x, {acc, max_sofar} ->
        {[max_sofar | acc], max(x, max_sofar)}
      end)

    result
  end
end
```
