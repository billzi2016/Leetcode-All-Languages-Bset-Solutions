# 3131. Find the Integer Added to Array I

## Cpp

```cpp
class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        int min1 = *min_element(nums1.begin(), nums1.end());
        int min2 = *min_element(nums2.begin(), nums2.end());
        return min2 - min1;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int[] a = nums1.clone();
        int[] b = nums2.clone();
        Arrays.sort(a);
        Arrays.sort(b);
        return b[0] - a[0];
    }
}
```

## Python

```python
class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return min(nums2) - min(nums1)
```

## Python3

```python
from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
```

## C

```c
#include <stdlib.h>

static int compare_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int addedInteger(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    qsort(nums1, (size_t)nums1Size, sizeof(int), compare_int);
    qsort(nums2, (size_t)nums2Size, sizeof(int), compare_int);
    return nums2[0] - nums1[0];
}
```

## Csharp

```csharp
public class Solution {
    public int AddedInteger(int[] nums1, int[] nums2) {
        int min1 = int.MaxValue;
        foreach (int v in nums1) {
            if (v < min1) min1 = v;
        }
        int min2 = int.MaxValue;
        foreach (int v in nums2) {
            if (v < min2) min2 = v;
        }
        return min2 - min1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var addedInteger = function(nums1, nums2) {
    const a = [...nums1].sort((x, y) => x - y);
    const b = [...nums2].sort((x, y) => x - y);
    return b[0] - a[0];
};
```

## Typescript

```typescript
function addedInteger(nums1: number[], nums2: number[]): number {
    const min1 = Math.min(...nums1);
    const min2 = Math.min(...nums2);
    return min2 - min1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function addedInteger($nums1, $nums2) {
        sort($nums1);
        sort($nums2);
        return $nums2[0] - $nums1[0];
    }
}
```

## Swift

```swift
class Solution {
    func addedInteger(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let min1 = nums1.min()!
        let min2 = nums2.min()!
        return min2 - min1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addedInteger(nums1: IntArray, nums2: IntArray): Int {
        var min1 = Int.MAX_VALUE
        for (v in nums1) {
            if (v < min1) min1 = v
        }
        var min2 = Int.MAX_VALUE
        for (v in nums2) {
            if (v < min2) min2 = v
        }
        return min2 - min1
    }
}
```

## Dart

```dart
class Solution {
  int addedInteger(List<int> nums1, List<int> nums2) {
    int min1 = nums1.reduce((a, b) => a < b ? a : b);
    int min2 = nums2.reduce((a, b) => a < b ? a : b);
    return min2 - min1;
  }
}
```

## Golang

```go
import "sort"

func addedInteger(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	return nums2[0] - nums1[0]
}
```

## Ruby

```ruby
def added_integer(nums1, nums2)
  nums2.min - nums1.min
end
```

## Scala

```scala
object Solution {
    def addedInteger(nums1: Array[Int], nums2: Array[Int]): Int = {
        nums2.min - nums1.min
    }
}
```

## Rust

```rust
impl Solution {
    pub fn added_integer(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let min1 = *nums1.iter().min().unwrap();
        let min2 = *nums2.iter().min().unwrap();
        min2 - min1
    }
}
```

## Racket

```racket
(define/contract (added-integer nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (- (apply min nums2) (apply min nums1)))
```

## Erlang

```erlang
-spec added_integer([integer()], [integer()]) -> integer().
added_integer(Nums1, Nums2) ->
    lists:min(Nums2) - lists:min(Nums1).
```

## Elixir

```elixir
defmodule Solution do
  @spec added_integer(nums1 :: [integer], nums2 :: [integer]) :: integer
  def added_integer(nums1, nums2) do
    Enum.min(nums2) - Enum.min(nums1)
  end
end
```
