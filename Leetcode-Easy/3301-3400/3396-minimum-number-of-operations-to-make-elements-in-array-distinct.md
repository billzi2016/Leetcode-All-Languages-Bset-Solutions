# 3396. Minimum Number of Operations to Make Elements in Array Distinct

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        unordered_set<int> seen;
        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            if (seen.count(nums[i])) {
                return i / 3 + 1;
            }
            seen.insert(nums[i]);
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (seen.contains(nums[i])) {
                return i / 3 + 1;
            }
            seen.add(nums[i]);
        }
        return 0;
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
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0
```

## Python3

```python
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0
```

## C

```c
#include <stdbool.h>

int minimumOperations(int* nums, int numsSize) {
    bool seen[101] = {false};
    for (int i = numsSize - 1; i >= 0; --i) {
        if (seen[nums[i]]) {
            return i / 3 + 1;
        }
        seen[nums[i]] = true;
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(int[] nums) {
        var seen = new HashSet<int>();
        for (int i = nums.Length - 1; i >= 0; i--) {
            if (seen.Contains(nums[i])) {
                return i / 3 + 1;
            }
            seen.Add(nums[i]);
        }
        return 0;
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
    const seen = new Set();
    for (let i = nums.length - 1; i >= 0; i--) {
        if (seen.has(nums[i])) {
            return Math.floor(i / 3) + 1;
        }
        seen.add(nums[i]);
    }
    return 0;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[]): number {
    const seen = new Set<number>();
    for (let i = nums.length - 1; i >= 0; --i) {
        if (seen.has(nums[i])) {
            return Math.floor(i / 3) + 1;
        }
        seen.add(nums[i]);
    }
    return 0;
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
        $seen = [];
        $n = count($nums);
        for ($i = $n - 1; $i >= 0; $i--) {
            $val = $nums[$i];
            if (isset($seen[$val])) {
                return intdiv($i, 3) + 1;
            }
            $seen[$val] = true;
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            let val = nums[i]
            if seen.contains(val) {
                return i / 3 + 1
            }
            seen.insert(val)
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (i in nums.indices.reversed()) {
            if (!seen.add(nums[i])) {
                return i / 3 + 1
            }
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    Set<int> seen = {};
    for (int i = nums.length - 1; i >= 0; i--) {
      if (seen.contains(nums[i])) {
        return i ~/ 3 + 1;
      }
      seen.add(nums[i]);
    }
    return 0;
  }
}
```

## Golang

```go
func minimumOperations(nums []int) int {
    seen := make(map[int]struct{})
    for i := len(nums) - 1; i >= 0; i-- {
        if _, ok := seen[nums[i]]; ok {
            return i/3 + 1
        }
        seen[nums[i]] = struct{}{}
    }
    return 0
}
```

## Ruby

```ruby
def minimum_operations(nums)
  seen = {}
  (nums.length - 1).downto(0) do |i|
    val = nums[i]
    if seen.key?(val)
      return i / 3 + 1
    else
      seen[val] = true
    end
  end
  0
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        var i = nums.length - 1
        while (i >= 0) {
            if (seen.contains(nums(i))) return i / 3 + 1
            seen.add(nums(i))
            i -= 1
        }
        0
    }
}
```

## Rust

```rust
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        for i in (0..nums.len()).rev() {
            if seen.contains(&nums[i]) {
                return (i as i32) / 3 + 1;
            }
            seen.insert(nums[i]);
        }
        0
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i (- n 1)) (seen (make-hash)))
      (if (< i 0)
          0
          (let ((val (vector-ref v i)))
            (if (hash-has-key? seen val)
                (+ (quotient i 3) 1)
                (begin
                  (hash-set! seen val #t)
                  (loop (- i 1) seen))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    Rev = lists:reverse(Nums),
    go(Rev, 0, sets:new(), length(Nums)).

go([], _C, _Seen, _N) ->
    0;
go([X|Rest], C, Seen, N) ->
    case sets:is_element(X, Seen) of
        true ->
            I = N - 1 - C,
            (I div 3) + 1;
        false ->
            go(Rest, C + 1, sets:add_element(X, Seen), N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    nums
    |> Enum.with_index()
    |> Enum.reverse()
    |> go(MapSet.new())
  end

  defp go([], _set), do: 0

  defp go([{val, idx} | rest], set) do
    if MapSet.member?(set, val) do
      div(idx, 3) + 1
    else
      go(rest, MapSet.put(set, val))
    end
  end
end
```
