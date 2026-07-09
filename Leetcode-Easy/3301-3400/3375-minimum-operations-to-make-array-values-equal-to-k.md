# 3375. Minimum Operations to Make Array Values Equal to K

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        unordered_set<int> greaterVals;
        for (int x : nums) {
            if (x < k) return -1;
            if (x > k) greaterVals.insert(x);
        }
        return (int)greaterVals.size();
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums, int k) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            if (num < k) return -1;
            if (num > k) set.add(num);
        }
        return set.size();
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                seen.add(num)
        return len(seen)
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        higher = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                higher.add(num)
        return len(higher)
```

## C

```c
int minOperations(int* nums, int numsSize, int k) {
    // Check for any element less than k
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < k) return -1;
    }
    // Boolean array to mark distinct values greater than k
    int seen[101] = {0};
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val > k && !seen[val]) {
            seen[val] = 1;
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums, int k) {
        var distinct = new System.Collections.Generic.HashSet<int>();
        foreach (var x in nums) {
            if (x < k) return -1;
            if (x > k) distinct.Add(x);
        }
        return distinct.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    const seen = new Set();
    for (const num of nums) {
        if (num < k) return -1;
        if (num > k) seen.add(num);
    }
    return seen.size;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    const distinct = new Set<number>();
    for (const num of nums) {
        if (num < k) return -1;
        if (num > k) distinct.add(num);
    }
    return distinct.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        $distinct = [];
        foreach ($nums as $val) {
            if ($val < $k) {
                return -1;
            }
            if ($val > $k) {
                $distinct[$val] = true;
            }
        }
        return count($distinct);
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var distinctGreater = Set<Int>()
        for num in nums {
            if num < k { return -1 }
            if num > k {
                distinctGreater.insert(num)
            }
        }
        return distinctGreater.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        val distinct = HashSet<Int>()
        for (v in nums) {
            if (v < k) return -1
            if (v > k) distinct.add(v)
        }
        return distinct.size
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    final Set<int> distinct = {};
    for (int num in nums) {
      if (num < k) return -1;
      if (num > k) distinct.add(num);
    }
    return distinct.length;
  }
}
```

## Golang

```go
func minOperations(nums []int, k int) int {
    seen := make(map[int]struct{})
    for _, v := range nums {
        if v < k {
            return -1
        }
        if v > k {
            seen[v] = struct{}{}
        }
    }
    return len(seen)
}
```

## Ruby

```ruby
def min_operations(nums, k)
  distinct = {}
  nums.each do |num|
    return -1 if num < k
    distinct[num] = true if num > k
  end
  distinct.size
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        val distinctGreater = scala.collection.mutable.HashSet[Int]()
        for (v <- nums) {
            if (v < k) return -1
            else if (v > k) distinctGreater += v
        }
        distinctGreater.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut distinct = std::collections::HashSet::new();
        for &v in nums.iter() {
            if v < k {
                return -1;
            }
            if v > k {
                distinct.insert(v);
            }
        }
        distinct.len() as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst nums) (seen (make-hash)))
    (cond
      [(null? lst) (hash-count seen)]
      [else
       (let ([x (car lst)])
         (if (< x k)
             -1
             (begin
               (when (> x k) (hash-set! seen x #t))
               (loop (cdr lst) seen))))])))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    case collect(Nums, K, #{}) of
        {error, _} -> -1;
        {ok, Seen} -> maps:size(Seen)
    end.

collect([], _, Seen) ->
    {ok, Seen};
collect([H|T], K, Seen) when H < K ->
    {error, none};
collect([H|T], K, Seen) ->
    NewSeen = if H > K -> maps:put(H, true, Seen); true -> Seen end,
    collect(T, K, NewSeen).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    result =
      Enum.reduce_while(nums, MapSet.new(), fn x, set ->
        cond do
          x < k -> {:halt, :error}
          x > k -> {:cont, MapSet.put(set, x)}
          true -> {:cont, set}
        end
      end)

    case result do
      :error -> -1
      set -> MapSet.size(set)
    end
  end
end
```
