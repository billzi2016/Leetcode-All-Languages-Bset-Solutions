# 2154. Keep Multiplying Found Values by Two

## Cpp

```cpp
class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> s(nums.begin(), nums.end());
        while (s.count(original)) {
            original *= 2;
        }
        return original;
    }
};
```

## Java

```java
class Solution {
    public int findFinalValue(int[] nums, int original) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        while (set.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
```

## Python

```python
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        s = set(nums)
        while original in s:
            original <<= 1  # multiply by 2
        return original
```

## Python3

```python
from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original <<= 1
        return original
```

## C

```c
#include <stdbool.h>

int findFinalValue(int* nums, int numsSize, int original) {
    bool present[1001] = {false};
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] <= 1000) {
            present[nums[i]] = true;
        }
    }
    
    int cur = original;
    while (cur <= 1000 && present[cur]) {
        cur <<= 1; // multiply by 2
    }
    return cur;
}
```

## Csharp

```csharp
public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        var set = new System.Collections.Generic.HashSet<int>(nums);
        while (set.Contains(original)) {
            original <<= 1; // multiply by 2
        }
        return original;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    const set = new Set(nums);
    while (set.has(original)) {
        original *= 2;
    }
    return original;
};
```

## Typescript

```typescript
function findFinalValue(nums: number[], original: number): number {
    const numSet = new Set(nums);
    while (numSet.has(original)) {
        original *= 2;
    }
    return original;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        $set = array_flip($nums);
        while (isset($set[$original])) {
            $original *= 2;
        }
        return $original;
    }
}
```

## Swift

```swift
class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        let numSet = Set(nums)
        var value = original
        while numSet.contains(value) {
            value *= 2
        }
        return value
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        val set = nums.toHashSet()
        var cur = original
        while (set.contains(cur)) {
            cur *= 2
        }
        return cur
    }
}
```

## Dart

```dart
class Solution {
  int findFinalValue(List<int> nums, int original) {
    final Set<int> values = nums.toSet();
    while (values.contains(original)) {
      original <<= 1; // multiply by 2
    }
    return original;
  }
}
```

## Golang

```go
func findFinalValue(nums []int, original int) int {
    set := make(map[int]struct{}, len(nums))
    for _, v := range nums {
        set[v] = struct{}{}
    }
    for {
        if _, ok := set[original]; ok {
            original *= 2
        } else {
            break
        }
    }
    return original
}
```

## Ruby

```ruby
require 'set'

def find_final_value(nums, original)
  values = nums.to_set
  while values.include?(original)
    original <<= 1
  end
  original
end
```

## Scala

```scala
object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        val set = nums.toSet
        var cur = original
        while (set.contains(cur)) {
            cur *= 2
        }
        cur
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut cur = original;
        while set.contains(&cur) {
            cur *= 2;
        }
        cur
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (find-final-value nums original)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([s (list->set nums)])
    (let loop ((val original))
      (if (set-member? s val)
          (loop (* 2 val))
          val))))
```

## Erlang

```erlang
-module(solution).
-export([find_final_value/2]).

find_final_value(Nums, Original) ->
    Set = maps:from_list([{N, true} || N <- Nums]),
    loop(Set, Original).

loop(Set, Orig) ->
    case maps:is_key(Orig, Set) of
        true -> loop(Set, Orig * 2);
        false -> Orig
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_final_value(nums :: [integer], original :: integer) :: integer
  def find_final_value(nums, original) do
    set = MapSet.new(nums)
    find(set, original)
  end

  defp find(set, val) do
    if MapSet.member?(set, val) do
      find(set, val * 2)
    else
      val
    end
  end
end
```
