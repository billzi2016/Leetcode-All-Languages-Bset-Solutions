# 2592. Maximize Greatness of an Array

## Cpp

```cpp
class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        int n = nums.size();
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());   // original values sorted
        sort(nums.begin(), nums.end());               // perm candidates sorted
        
        int i = 0, j = 0, greatness = 0;
        while (i < n && j < n) {
            if (nums[j] > sortedNums[i]) {
                ++greatness;
                ++i;
                ++j;
            } else {
                ++j;
            }
        }
        return greatness;
    }
};
```

## Java

```java
class Solution {
    public int maximizeGreatness(int[] nums) {
        int n = nums.length;
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        int i = 0, j = 0, count = 0;
        while (i < n && j < n) {
            if (sorted[j] > sorted[i]) {
                count++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i = j = 0
        greatness = 0
        while i < n and j < n:
            if nums[j] > nums[i]:
                greatness += 1
                i += 1
                j += 1
            else:
                j += 1
        return greatness
```

## Python3

```python
from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = j = 0
        greatness = 0
        while i < n and j < n:
            if nums[j] > nums[i]:
                greatness += 1
                i += 1
                j += 1
            else:
                j += 1
        return greatness
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int maximizeGreatness(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int i = 0, j = 0, count = 0;
    while (i < numsSize && j < numsSize) {
        if (nums[j] > nums[i]) {
            ++count;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximizeGreatness(int[] nums) {
        int n = nums.Length;
        int[] sorted = (int[])nums.Clone();
        System.Array.Sort(sorted);
        int i = 0, j = 0, count = 0;
        while (i < n && j < n) {
            if (sorted[j] > sorted[i]) {
                count++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximizeGreatness = function(nums) {
    nums.sort((a, b) => a - b);
    let i = 0, count = 0;
    for (let j = 0; j < nums.length && i < nums.length; ++j) {
        if (nums[j] > nums[i]) {
            count++;
            i++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function maximizeGreatness(nums: number[]): number {
    const sorted = nums.slice().sort((a, b) => a - b);
    let i = 0, j = 0, count = 0;
    const n = sorted.length;
    while (i < n && j < n) {
        if (sorted[j] > sorted[i]) {
            count++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximizeGreatness($nums) {
        sort($nums);
        $n = count($nums);
        $i = 0;
        $j = 0;
        $greatness = 0;
        while ($i < $n && $j < $n) {
            if ($nums[$j] > $nums[$i]) {
                $greatness++;
                $i++;
                $j++;
            } else {
                $j++;
            }
        }
        return $greatness;
    }
}
```

## Swift

```swift
class Solution {
    func maximizeGreatness(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        var i = 0
        var j = 0
        var count = 0
        let n = sorted.count
        while i < n && j < n {
            if sorted[j] > sorted[i] {
                count += 1
                i += 1
                j += 1
            } else {
                j += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximizeGreatness(nums: IntArray): Int {
        val sorted = nums.clone()
        sorted.sort()
        var i = 0
        var j = 0
        var greatness = 0
        val n = sorted.size
        while (i < n && j < n) {
            if (sorted[j] > sorted[i]) {
                greatness++
                i++
                j++
            } else {
                j++
            }
        }
        return greatness
    }
}
```

## Dart

```dart
class Solution {
  int maximizeGreatness(List<int> nums) {
    List<int> sorted = List.from(nums);
    sorted.sort();
    int n = sorted.length;
    int i = 0, j = 0, count = 0;
    while (i < n && j < n) {
      if (sorted[j] > sorted[i]) {
        count++;
        i++;
        j++;
      } else {
        j++;
      }
    }
    return count;
  }
}
```

## Golang

```go
package main

import "sort"

func maximizeGreatness(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	i, j, cnt := 0, 0, 0
	for i < n && j < n {
		if nums[j] > nums[i] {
			cnt++
			i++
			j++
		} else {
			j++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def maximize_greatness(nums)
  a = nums.sort
  n = a.length
  i = 0
  j = 0
  count = 0
  while i < n && j < n
    if a[j] > a[i]
      count += 1
      i += 1
      j += 1
    else
      j += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
  def maximizeGreatness(nums: Array[Int]): Int = {
    val a = nums.sorted
    var i = 0
    var j = 0
    var cnt = 0
    val n = a.length
    while (i < n && j < n) {
      if (a(j) > a(i)) {
        cnt += 1
        i += 1
        j += 1
      } else {
        j += 1
      }
    }
    cnt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn maximize_greatness(nums: Vec<i32>) -> i32 {
        let mut sorted = nums.clone();
        sorted.sort_unstable();
        let n = sorted.len();
        let (mut i, mut j) = (0usize, 0usize);
        let mut count = 0i32;
        while i < n && j < n {
            if sorted[j] > sorted[i] {
                count += 1;
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (maximize-greatness nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [v (list->vector sorted)])
    (let loop ((i 0) (j 0) (cnt 0))
      (cond
        [(or (= i (vector-length v)) (= j (vector-length v))) cnt]
        [(> (vector-ref v j) (vector-ref v i))
         (loop (+ i 1) (+ j 1) (+ cnt 1))]
        [else
         (loop i (+ j 1) cnt)]))))
```

## Erlang

```erlang
-module(solution).
-export([maximize_greatness/1]).

-spec maximize_greatness(Nums :: [integer()]) -> integer().
maximize_greatness(Nums) ->
    Sorted = lists:sort(Nums),
    count_greater(Sorted, Sorted, 0).

count_greater([], _, Acc) -> Acc;
count_greater(_, [], Acc) -> Acc;
count_greater([O|Os], [C|Cs], Acc) when C > O ->
    count_greater(Os, Cs, Acc + 1);
count_greater(Olist, [_C|Cs], Acc) ->
    count_greater(Olist, Cs, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximize_greatness(nums :: [integer]) :: integer
  def maximize_greatness(nums) do
    sorted = Enum.sort(nums)
    count_greatness(sorted, sorted, 0)
  end

  defp count_greatness([], _candidates, acc), do: acc
  defp count_greatness(_targets, [], acc), do: acc
  defp count_greatness([t | t_rest] = targets, [c | c_rest], acc) do
    if c > t do
      count_greatness(t_rest, c_rest, acc + 1)
    else
      count_greatness(targets, c_rest, acc)
    end
  end
end
```
