# 2974. Minimum Number Game

## Cpp

```cpp
class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i + 1 < nums.size(); i += 2) {
            swap(nums[i], nums[i + 1]);
        }
        return nums;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i + 1 < nums.length; i += 2) {
            int temp = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = temp;
        }
        return nums;
    }
}
```

## Python

```python
class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
```

## Python3

```python
from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberGame(int* nums, int numsSize, int* returnSize) {
    int *res = (int*)malloc(numsSize * sizeof(int));
    if (!res) return NULL;
    memcpy(res, nums, numsSize * sizeof(int));

    qsort(res, numsSize, sizeof(int), cmpInt);

    for (int i = 0; i < numsSize; i += 2) {
        int tmp = res[i];
        res[i] = res[i + 1];
        res[i + 1] = tmp;
    }

    *returnSize = numsSize;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NumberGame(int[] nums) {
        System.Array.Sort(nums);
        for (int i = 0; i < nums.Length; i += 2) {
            int temp = nums[i];
            nums[i] = nums[i + 1];
            nums[i + 1] = temp;
        }
        return nums;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberGame = function(nums) {
    // Sort the numbers in non-decreasing order
    nums.sort((a, b) => a - b);
    
    // Swap each adjacent pair
    for (let i = 0; i < nums.length; i += 2) {
        const temp = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = temp;
    }
    
    return nums;
};
```

## Typescript

```typescript
function numberGame(nums: number[]): number[] {
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i += 2) {
        const temp = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = temp;
    }
    return nums;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function numberGame($nums) {
        sort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n; $i += 2) {
            $tmp = $nums[$i];
            $nums[$i] = $nums[$i + 1];
            $nums[$i + 1] = $tmp;
        }
        return $nums;
    }
}
```

## Swift

```swift
class Solution {
    func numberGame(_ nums: [Int]) -> [Int] {
        var sorted = nums.sorted()
        var i = 0
        while i + 1 < sorted.count {
            sorted.swapAt(i, i + 1)
            i += 2
        }
        return sorted
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberGame(nums: IntArray): IntArray {
        nums.sort()
        var i = 0
        while (i + 1 < nums.size) {
            val tmp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = tmp
            i += 2
        }
        return nums
    }
}
```

## Dart

```dart
class Solution {
  List<int> numberGame(List<int> nums) {
    nums.sort();
    for (int i = 0; i + 1 < nums.length; i += 2) {
      int tmp = nums[i];
      nums[i] = nums[i + 1];
      nums[i + 1] = tmp;
    }
    return nums;
  }
}
```

## Golang

```go
import "sort"

func numberGame(nums []int) []int {
	sort.Ints(nums)
	for i := 0; i+1 < len(nums); i += 2 {
		nums[i], nums[i+1] = nums[i+1], nums[i]
	}
	return nums
}
```

## Ruby

```ruby
def number_game(nums)
  nums.sort!
  (0...nums.length).step(2) do |i|
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
  end
  nums
end
```

## Scala

```scala
object Solution {
    def numberGame(nums: Array[Int]): Array[Int] = {
        val a = nums.sorted
        var i = 0
        while (i < a.length) {
            val tmp = a(i)
            a(i) = a(i + 1)
            a(i + 1) = tmp
            i += 2
        }
        a
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_game(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let n = nums.len();
        for i in (0..n).step_by(2) {
            nums.swap(i, i + 1);
        }
        nums
    }
}
```

## Racket

```racket
(define/contract (number-game nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ([sorted (sort nums <)])
    (let rec ((lst sorted))
      (if (null? lst)
          '()
          (let ((first (car lst))
                (second (cadr lst)))
            (cons second (cons first (rec (cddr lst)))))))))
```

## Erlang

```erlang
-spec number_game(Nums :: [integer()]) -> [integer()].
number_game(Nums) ->
    Sorted = lists:sort(Nums),
    swap_adjacent(Sorted).

swap_adjacent([]) -> [];
swap_adjacent([A, B | Rest]) ->
    [B, A | swap_adjacent(Rest)].
```

## Elixir

```elixir
defmodule Solution do
  @spec number_game(nums :: [integer]) :: [integer]
  def number_game(nums) do
    nums
    |> Enum.sort()
    |> Enum.chunk_every(2)
    |> Enum.flat_map(fn [a, b] -> [b, a] end)
  end
end
```
