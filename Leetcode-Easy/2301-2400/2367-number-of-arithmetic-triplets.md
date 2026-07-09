# 2367. Number of Arithmetic Triplets

## Cpp

```cpp
class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        unordered_set<int> s(nums.begin(), nums.end());
        int cnt = 0;
        for (int x : nums) {
            if (s.count(x - diff) && s.count(x + diff)) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        int count = 0;
        for (int num : nums) {
            if (seen.contains(num - diff) && seen.contains(num - 2 * diff)) {
                count++;
            }
            seen.add(num);
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        s = set(nums)
        count = 0
        for x in nums:
            if (x - diff) in s and (x + diff) in s:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        cnt = 0
        for x in nums:
            if x + diff in s and x + 2 * diff in s:
                cnt += 1
        return cnt
```

## C

```c
int arithmeticTriplets(int* nums, int numsSize, int diff) {
    // Since nums[i] is in range [0,200], we can use a fixed-size lookup table.
    int present[201] = {0};
    for (int i = 0; i < numsSize; ++i) {
        present[nums[i]] = 1;
    }
    
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val - diff >= 0 && val + diff <= 200 &&
            present[val - diff] && present[val + diff]) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int ArithmeticTriplets(int[] nums, int diff) {
        var set = new HashSet<int>(nums);
        int count = 0;
        foreach (int x in nums) {
            if (set.Contains(x - diff) && set.Contains(x - 2 * diff)) {
                count++;
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
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    const numSet = new Set(nums);
    let count = 0;
    for (const x of nums) {
        if (numSet.has(x - diff) && numSet.has(x + diff)) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function arithmeticTriplets(nums: number[], diff: number): number {
    const numSet = new Set(nums);
    let count = 0;
    for (const x of nums) {
        if (numSet.has(x + diff) && numSet.has(x + 2 * diff)) {
            count++;
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
     * @param Integer $diff
     * @return Integer
     */
    function arithmeticTriplets($nums, $diff) {
        $set = array_flip($nums);
        $count = 0;
        foreach ($nums as $num) {
            if (isset($set[$num + $diff]) && isset($set[$num + 2 * $diff])) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func arithmeticTriplets(_ nums: [Int], _ diff: Int) -> Int {
        let numSet = Set(nums)
        var count = 0
        for num in nums {
            if numSet.contains(num + diff) && numSet.contains(num + 2 * diff) {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arithmeticTriplets(nums: IntArray, diff: Int): Int {
        val numSet = nums.toHashSet()
        var count = 0
        for (x in nums) {
            if (numSet.contains(x - diff) && numSet.contains(x + diff)) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int arithmeticTriplets(List<int> nums, int diff) {
    final numSet = nums.toSet();
    int count = 0;
    for (var x in nums) {
      if (numSet.contains(x - diff) && numSet.contains(x + diff)) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func arithmeticTriplets(nums []int, diff int) int {
    s := make(map[int]struct{}, len(nums))
    for _, v := range nums {
        s[v] = struct{}{}
    }
    count := 0
    for _, v := range nums {
        if _, ok1 := s[v-diff]; ok1 {
            if _, ok2 := s[v+diff]; ok2 {
                count++
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def arithmetic_triplets(nums, diff)
  present = {}
  nums.each { |v| present[v] = true }
  count = 0
  nums.each do |v|
    count += 1 if present[v + diff] && present[v + 2 * diff]
  end
  count
end
```

## Scala

```scala
object Solution {
    def arithmeticTriplets(nums: Array[Int], diff: Int): Int = {
        val setNums = nums.toSet
        var count = 0
        for (x <- nums) {
            if (setNums.contains(x + diff) && setNums.contains(x + 2 * diff)) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashSet;

pub struct Solution;

impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        let set: HashSet<i32> = nums.iter().cloned().collect();
        let mut count = 0;
        for &x in &nums {
            if set.contains(&(x - diff)) && set.contains(&(x + diff)) {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (arithmetic-triplets nums diff)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((set (let ((h (make-hash)))
                (for ([x nums]) (hash-set! h x #t))
                h))
         (cnt (for/sum ([x nums])
                (if (and (hash-has-key? set (+ x diff))
                         (hash-has-key? set (+ x (* 2 diff))))
                    1
                    0))))
    cnt))
```

## Erlang

```erlang
-spec arithmetic_triplets(Nums :: [integer()], Diff :: integer()) -> integer().
arithmetic_triplets(Nums, Diff) ->
    Set = maps:from_list([{N, true} || N <- Nums]),
    lists:foldl(
        fun(N, Acc) ->
            case {maps:is_key(N + Diff, Set), maps:is_key(N + 2 * Diff, Set)} of
                {true, true} -> Acc + 1;
                _ -> Acc
            end
        end,
        0,
        Nums
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec arithmetic_triplets(nums :: [integer], diff :: integer) :: integer
  def arithmetic_triplets(nums, diff) do
    set = MapSet.new(nums)

    Enum.reduce(nums, 0, fn x, acc ->
      if MapSet.member?(set, x - diff) and MapSet.member?(set, x + diff) do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
