# 2540. Minimum Common Value

## Cpp

```cpp
class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        size_t i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) return nums1[i];
            if (nums1[i] < nums2[j]) ++i;
            else ++j;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            a, b = nums1[i], nums2[j]
            if a == b:
                return a
            if a < b:
                i += 1
            else:
                j += 1
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
```

## C

```c
int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] == nums2[j]) return nums1[i];
        if (nums1[i] < nums2[j]) ++i;
        else ++j;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int GetCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.Length && j < nums2.Length) {
            if (nums1[i] == nums2[j]) return nums1[i];
            if (nums1[i] < nums2[j]) i++;
            else j++;
        }
        return -1;
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
var getCommon = function(nums1, nums2) {
    let i = 0, j = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] === nums2[j]) return nums1[i];
        if (nums1[i] < nums2[j]) i++;
        else j++;
    }
    return -1;
};
```

## Typescript

```typescript
function getCommon(nums1: number[], nums2: number[]): number {
    let i = 0, j = 0;
    const n = nums1.length, m = nums2.length;
    while (i < n && j < m) {
        if (nums1[i] === nums2[j]) return nums1[i];
        if (nums1[i] < nums2[j]) i++;
        else j++;
    }
    return -1;
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
    function getCommon($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $n = count($nums1);
        $m = count($nums2);
        while ($i < $n && $j < $m) {
            if ($nums1[$i] == $nums2[$j]) {
                return $nums1[$i];
            } elseif ($nums1[$i] < $nums2[$j]) {
                $i++;
            } else {
                $j++;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func getCommon(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0
        var j = 0
        while i < nums1.count && j < nums2.count {
            let a = nums1[i]
            let b = nums2[j]
            if a == b {
                return a
            } else if a < b {
                i += 1
            } else {
                j += 1
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getCommon(nums1: IntArray, nums2: IntArray): Int {
        var i = 0
        var j = 0
        while (i < nums1.size && j < nums2.size) {
            val a = nums1[i]
            val b = nums2[j]
            if (a == b) return a
            if (a < b) {
                i++
            } else {
                j++
            }
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int getCommon(List<int> nums1, List<int> nums2) {
    int i = 0, j = 0;
    while (i < nums1.length && j < nums2.length) {
      if (nums1[i] == nums2[j]) return nums1[i];
      if (nums1[i] < nums2[j]) {
        i++;
      } else {
        j++;
      }
    }
    return -1;
  }
}
```

## Golang

```go
func getCommon(nums1 []int, nums2 []int) int {
    i, j := 0, 0
    for i < len(nums1) && j < len(nums2) {
        if nums1[i] == nums2[j] {
            return nums1[i]
        }
        if nums1[i] < nums2[j] {
            i++
        } else {
            j++
        }
    }
    return -1
}
```

## Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def get_common(nums1, nums2)
  i = 0
  j = 0
  n1 = nums1.length
  n2 = nums2.length

  while i < n1 && j < n2
    if nums1[i] == nums2[j]
      return nums1[i]
    elsif nums1[i] < nums2[j]
      i += 1
    else
      j += 1
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def getCommon(nums1: Array[Int], nums2: Array[Int]): Int = {
        var i = 0
        var j = 0
        val n = nums1.length
        val m = nums2.length
        while (i < n && j < m) {
            if (nums1(i) == nums2(j)) return nums1(i)
            else if (nums1(i) < nums2(j)) i += 1
            else j += 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i = 0usize;
        let mut j = 0usize;
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                return nums1[i];
            } else if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (get-common nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let loop ((l1 nums1) (l2 nums2))
    (cond
      [(or (null? l1) (null? l2)) -1]
      [else
       (let ((a (car l1)) (b (car l2)))
         (cond
           [(= a b) a]
           [(< a b) (loop (cdr l1) l2)]
           [else   (loop l1 (cdr l2))]))])))
```

## Erlang

```erlang
-module(solution).
-export([get_common/2]).

-spec get_common(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
get_common([], _) -> -1;
get_common(_, []) -> -1;
get_common([H1|T1]=L1, [H2|T2]=L2) ->
    if
        H1 =:= H2 -> H1;
        H1 < H2  -> get_common(T1, L2);
        true     -> get_common(L1, T2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_common(nums1 :: [integer], nums2 :: [integer]) :: integer
  def get_common(nums1, nums2) do
    go(nums1, nums2)
  end

  defp go([], _), do: -1
  defp go(_, []), do: -1
  defp go([h1 | t1] = l1, [h2 | t2] = l2) do
    cond do
      h1 == h2 -> h1
      h1 < h2 -> go(t1, l2)
      true -> go(l1, t2)
    end
  end
end
```
