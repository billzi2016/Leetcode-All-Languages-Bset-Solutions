# 1846. Maximum Element After Decreasing and Rearranging

## Cpp

```cpp
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int ans = 1;
        for (int x : arr) {
            if (x >= ans + 1) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        java.util.Arrays.sort(arr);
        int ans = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] >= ans + 1) {
                ans++;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        ans = 0
        for v in arr:
            if v > ans:
                ans += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        for v in arr:
            if v > ans:
                ans += 1
        return ans
```

## C

```c
#include <stdlib.h>

static int compare_ints(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int maximumElementAfterDecrementingAndRearranging(int* arr, int arrSize) {
    if (arrSize == 0) return 0;
    qsort(arr, (size_t)arrSize, sizeof(int), compare_ints);
    int ans = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (arr[i] > ans) {
            ++ans;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr)
    {
        System.Array.Sort(arr);
        int ans = 0;
        foreach (int v in arr)
        {
            if (v >= ans + 1)
                ans++;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr.sort((a, b) => a - b);
    let ans = 1;
    for (let i = 0; i < arr.length; ++i) {
        if (arr[i] >= ans + 1) {
            ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maximumElementAfterDecrementingAndRearranging(arr: number[]): number {
    arr.sort((a, b) => a - b);
    let ans = 1;
    for (let i = 1; i < arr.length; ++i) {
        if (arr[i] >= ans + 1) {
            ++ans;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumElementAfterDecrementingAndRearranging($arr) {
        sort($arr);
        $ans = 0;
        foreach ($arr as $v) {
            if ($v > $ans) {
                $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumElementAfterDecrementingAndRearranging(_ arr: [Int]) -> Int {
        let sorted = arr.sorted()
        var ans = 1
        for i in 1..<sorted.count {
            if sorted[i] >= ans + 1 {
                ans += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumElementAfterDecrementingAndRearranging(arr: IntArray): Int {
        arr.sort()
        var ans = 1
        for (v in arr) {
            if (v >= ans + 1) {
                ans++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumElementAfterDecrementingAndRearranging(List<int> arr) {
    arr.sort();
    int ans = 1;
    for (int i = 1; i < arr.length; ++i) {
      if (arr[i] >= ans + 1) {
        ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	sort.Ints(arr)
	ans := 1
	for i := 1; i < len(arr); i++ {
		if arr[i] >= ans+1 {
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_element_after_decrementing_and_rearranging(arr)
  arr.sort!
  ans = 1
  arr.each_with_index do |val, idx|
    next if idx == 0
    ans += 1 if val >= ans + 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maximumElementAfterDecrementingAndRearranging(arr: Array[Int]): Int = {
        java.util.Arrays.sort(arr)
        var ans = 1
        var i = 1
        while (i < arr.length) {
            if (arr(i) >= ans + 1) ans += 1
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_element_after_decrementing_and_rearranging(mut arr: Vec<i32>) -> i32 {
        arr.sort_unstable();
        let mut ans = 1;
        for &v in arr.iter().skip(1) {
            if v >= ans + 1 {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-element-after-decrementing-and-rearranging arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort arr <))
         (ans (foldl (lambda (x acc)
                       (if (>= x (+ acc 1))
                           (+ acc 1)
                           acc))
                     1
                     sorted)))
    ans))
```

## Erlang

```erlang
-spec maximum_element_after_decrementing_and_rearranging(Arr :: [integer()]) -> integer().
maximum_element_after_decrementing_and_rearranging(Arr) ->
    Sorted = lists:sort(Arr),
    lists:foldl(fun(X, Acc) ->
        case X >= Acc + 1 of
            true -> Acc + 1;
            false -> Acc
        end
    end, 0, Sorted).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_element_after_decrementing_and_rearranging(arr :: [integer]) :: integer
  def maximum_element_after_decrementing_and_rearranging(arr) do
    arr
    |> Enum.sort()
    |> Enum.reduce(0, fn x, cur ->
      if x >= cur + 1, do: cur + 1, else: cur
    end)
  end
end
```
