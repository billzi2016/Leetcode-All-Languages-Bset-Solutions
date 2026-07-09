# 2357. Make Array Zero by Subtracting Equal Amounts

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> uniq;
        for (int x : nums) {
            if (x != 0) uniq.insert(x);
        }
        return uniq.size();
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        java.util.HashSet<Integer> unique = new java.util.HashSet<>();
        for (int num : nums) {
            if (num != 0) {
                unique.add(num);
            }
        }
        return unique.size();
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len({num for num in nums if num > 0})
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num != 0})
```

## C

```c
#include <stddef.h>

int minimumOperations(int* nums, int numsSize) {
    int seen[101] = {0};
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (v > 0 && !seen[v]) {
            seen[v] = 1;
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(int[] nums) {
        var set = new HashSet<int>();
        foreach (int num in nums) {
            if (num != 0) {
                set.Add(num);
            }
        }
        return set.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const unique = new Set();
    for (const num of nums) {
        if (num !== 0) {
            unique.add(num);
        }
    }
    return unique.size;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[]): number {
    const seen = new Set<number>();
    for (const num of nums) {
        if (num !== 0) {
            seen.add(num);
        }
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $unique = [];
        foreach ($nums as $num) {
            if ($num != 0) {
                $unique[$num] = true;
            }
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var uniqueValues = Set<Int>()
        for num in nums where num != 0 {
            uniqueValues.insert(num)
        }
        return uniqueValues.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (num in nums) {
            if (num != 0) {
                seen.add(num)
            }
        }
        return seen.size
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    final unique = <int>{};
    for (final num in nums) {
      if (num != 0) unique.add(num);
    }
    return unique.length;
  }
}
```

## Golang

```go
func minimumOperations(nums []int) int {
	unique := make(map[int]struct{})
	for _, v := range nums {
		if v != 0 {
			unique[v] = struct{}{}
		}
	}
	return len(unique)
}
```

## Ruby

```ruby
def minimum_operations(nums)
  nums.reject { |v| v == 0 }.uniq.size
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        for (num <- nums) {
            if (num != 0) seen += num
        }
        seen.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut uniq = std::collections::HashSet::new();
        for v in nums {
            if v != 0 {
                uniq.insert(v);
            }
        }
        uniq.len() as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((unique
         (remove-duplicates
          (filter (lambda (x) (> x 0)) nums))))
    (length unique)))
```

## Erlang

```erlang
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    Unique = lists:usort([N || N <- Nums, N =/= 0]),
    length(Unique).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    nums
    |> Enum.filter(&(&1 != 0))
    |> MapSet.new()
    |> MapSet.size()
  end
end
```
