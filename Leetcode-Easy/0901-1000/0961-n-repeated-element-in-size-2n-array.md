# 0961. N-Repeated Element in Size 2N Array

## Cpp

```cpp
class Solution {
public:
    int repeatedNTimes(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) {
            if (++cnt[x] > 1) return x;
        }
        return -1; // should never reach here per problem constraints
    }
};
```

## Java

```java
class Solution {
    public int repeatedNTimes(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (i >= 1 && nums[i] == nums[i - 1]) return nums[i];
            if (i >= 2 && nums[i] == nums[i - 2]) return nums[i];
            if (i >= 3 && nums[i] == nums[i - 3]) return nums[i];
        }
        // Fallback, though problem guarantees a solution will be found earlier
        return nums[0];
    }
}
```

## Python

```python
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                return nums[i]
            if i + 2 < n and nums[i] == nums[i + 2]:
                return nums[i]
            if i + 3 < n and nums[i] == nums[i + 3]:
                return nums[i]
```

## Python3

```python
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                return nums[i]
            if i + 2 < n and nums[i] == nums[i + 2]:
                return nums[i]
            if i + 3 < n and nums[i] == nums[i + 3]:
                return nums[i]
```

## C

```c
int repeatedNTimes(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; ++i) {
        if (i + 1 < numsSize && nums[i] == nums[i + 1]) return nums[i];
        if (i + 2 < numsSize && nums[i] == nums[i + 2]) return nums[i];
        if (i + 3 < numsSize && nums[i] == nums[i + 3]) return nums[i];
    }
    return nums[0]; // fallback, should never be reached
}
```

## Csharp

```csharp
public class Solution {
    public int RepeatedNTimes(int[] nums) {
        var seen = new System.Collections.Generic.HashSet<int>();
        foreach (var num in nums) {
            if (!seen.Add(num)) return num;
        }
        return -1; // Should never happen per problem constraints
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        if (i + 1 < n && nums[i] === nums[i + 1]) return nums[i];
        if (i + 2 < n && nums[i] === nums[i + 2]) return nums[i];
        if (i + 3 < n && nums[i] === nums[i + 3]) return nums[i];
    }
    // Fallback, though problem guarantees a solution
    return nums[0];
};
```

## Typescript

```typescript
function repeatedNTimes(nums: number[]): number {
    const seen = new Set<number>();
    for (const num of nums) {
        if (seen.has(num)) return num;
        seen.add(num);
    }
    // According to problem constraints, this line is never reached.
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function repeatedNTimes($nums) {
        $seen = [];
        foreach ($nums as $num) {
            if (isset($seen[$num])) {
                return $num;
            }
            $seen[$num] = true;
        }
        // Fallback (should never reach here due to problem guarantees)
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($d = 1; $d <= 3; $d++) {
                if ($i + $d < $n && $nums[$i] === $nums[$i + $d]) {
                    return $nums[$i];
                }
            }
        }
        return null;
    }
}
```

## Swift

```swift
class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        for num in nums {
            if seen.contains(num) {
                return num
            }
            seen.insert(num)
        }
        // According to problem constraints, this line will never be reached.
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun repeatedNTimes(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (num in nums) {
            if (!seen.add(num)) return num
        }
        // According to problem constraints, this line is never reached.
        throw IllegalArgumentException("No element repeats n times")
    }
}
```

## Dart

```dart
class Solution {
  int repeatedNTimes(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      if (i >= 1 && nums[i] == nums[i - 1]) return nums[i];
      if (i >= 2 && nums[i] == nums[i - 2]) return nums[i];
      if (i >= 3 && nums[i] == nums[i - 3]) return nums[i];
    }
    // Fallback, though problem guarantees a solution.
    return nums[0];
  }
}
```

## Golang

```go
func repeatedNTimes(nums []int) int {
    seen := make(map[int]struct{})
    for _, v := range nums {
        if _, ok := seen[v]; ok {
            return v
        }
        seen[v] = struct{}{}
    }
    return -1
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def repeated_n_times(nums)
  freq = Hash.new(0)
  nums.each do |num|
    freq[num] += 1
    return num if freq[num] > 1
  end
end
```

## Scala

```scala
object Solution {
    def repeatedNTimes(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        for (x <- nums) {
            if (seen.contains(x)) return x
            seen.add(x)
        }
        // According to problem constraints, this line is never reached.
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        for i in 0..n {
            let cur = nums[i];
            if i + 1 < n && cur == nums[i + 1] {
                return cur;
            }
            if i + 2 < n && cur == nums[i + 2] {
                return cur;
            }
            if i + 3 < n && cur == nums[i + 3] {
                return cur;
            }
        }
        // According to problem constraints, this line is never reached.
        0
    }
}
```

## Racket

```racket
(define/contract (repeated-n-times nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (seen (make-hash)))
    (cond [(null? lst) (error "No repeated element")]
          [else
           (let ((x (car lst)))
             (if (hash-has-key? seen x)
                 x
                 (begin
                   (hash-set! seen x #t)
                   (loop (cdr lst) seen))))])))
```

## Erlang

```erlang
-spec repeated_n_times(Nums :: [integer()]) -> integer().
repeated_n_times(Nums) ->
    repeated_n_times(Nums, #{}).

repeated_n_times([], _) ->
    erlang:error(badarg);
repeated_n_times([X|Rest], Seen) ->
    case maps:is_key(X, Seen) of
        true -> X;
        false -> repeated_n_times(Rest, maps:put(X, true, Seen))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec repeated_n_times(nums :: [integer]) :: integer
  def repeated_n_times(nums) do
    arr = List.to_tuple(nums)
    len = tuple_size(arr)
    find_duplicate(0, len, arr)
  end

  defp find_duplicate(i, len, arr) when i < len do
    a = elem(arr, i)

    cond do
      i + 1 < len and a == elem(arr, i + 1) -> a
      i + 2 < len and a == elem(arr, i + 2) -> a
      i + 3 < len and a == elem(arr, i + 3) -> a
      true -> find_duplicate(i + 1, len, arr)
    end
  end

  defp find_duplicate(_, _, _), do: nil
end
```
