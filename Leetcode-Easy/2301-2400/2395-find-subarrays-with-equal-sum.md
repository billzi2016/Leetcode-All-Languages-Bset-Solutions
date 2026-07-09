# 2395. Find Subarrays With Equal Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        unordered_set<long long> seen;
        for (int i = 0; i + 1 < (int)nums.size(); ++i) {
            long long sum = (long long)nums[i] + nums[i + 1];
            if (seen.count(sum)) return true;
            seen.insert(sum);
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean findSubarrays(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        for (int i = 0; i < nums.length - 1; i++) {
            int sum = nums[i] + nums[i + 1];
            if (!seen.add(sum)) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True
            seen.add(s)
        return False
```

## Python3

```python
from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True
            seen.add(s)
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool findSubarrays(int* nums, int numsSize) {
    if (numsSize < 2) return false;
    int subCount = numsSize - 1;
    long long *sums = (long long *)malloc(subCount * sizeof(long long));
    int seen = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        long long curSum = (long long)nums[i] + (long long)nums[i + 1];
        for (int j = 0; j < seen; ++j) {
            if (sums[j] == curSum) {
                free(sums);
                return true;
            }
        }
        sums[seen++] = curSum;
    }
    free(sums);
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool FindSubarrays(int[] nums) {
        var seen = new System.Collections.Generic.HashSet<long>();
        for (int i = 0; i < nums.Length - 1; i++) {
            long sum = (long)nums[i] + nums[i + 1];
            if (!seen.Add(sum)) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var findSubarrays = function(nums) {
    const seen = new Set();
    for (let i = 0; i < nums.length - 1; ++i) {
        const sum = nums[i] + nums[i + 1];
        if (seen.has(sum)) return true;
        seen.add(sum);
    }
    return false;
};
```

## Typescript

```typescript
function findSubarrays(nums: number[]): boolean {
    const seen = new Set<number>();
    for (let i = 0; i < nums.length - 1; i++) {
        const sum = nums[i] + nums[i + 1];
        if (seen.has(sum)) return true;
        seen.add(sum);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function findSubarrays($nums) {
        $seen = [];
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            $sum = $nums[$i] + $nums[$i + 1];
            if (isset($seen[$sum])) {
                return true;
            }
            $seen[$sum] = true;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func findSubarrays(_ nums: [Int]) -> Bool {
        var seen = Set<Int>()
        for i in 0..<(nums.count - 1) {
            let sum = nums[i] + nums[i + 1]
            if seen.contains(sum) {
                return true
            }
            seen.insert(sum)
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSubarrays(nums: IntArray): Boolean {
        val seen = HashSet<Int>()
        for (i in 0 until nums.size - 1) {
            val sum = nums[i] + nums[i + 1]
            if (!seen.add(sum)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool findSubarrays(List<int> nums) {
    final Set<int> seenSums = {};
    for (int i = 0; i < nums.length - 1; ++i) {
      int sum = nums[i] + nums[i + 1];
      if (seenSums.contains(sum)) return true;
      seenSums.add(sum);
    }
    return false;
  }
}
```

## Golang

```go
func findSubarrays(nums []int) bool {
    seen := make(map[int]struct{})
    for i := 0; i+1 < len(nums); i++ {
        sum := nums[i] + nums[i+1]
        if _, ok := seen[sum]; ok {
            return true
        }
        seen[sum] = struct{}{}
    }
    return false
}
```

## Ruby

```ruby
def find_subarrays(nums)
  seen = {}
  (0...nums.length - 1).each do |i|
    sum = nums[i] + nums[i + 1]
    return true if seen[sum]
    seen[sum] = true
  end
  false
end
```

## Scala

```scala
object Solution {
    def findSubarrays(nums: Array[Int]): Boolean = {
        val seen = scala.collection.mutable.HashSet[Int]()
        var i = 0
        while (i < nums.length - 1) {
            val sum = nums(i) + nums(i + 1)
            if (seen.contains(sum)) return true
            seen.add(sum)
            i += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_subarrays(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut seen = HashSet::new();
        for i in 0..nums.len() - 1 {
            let sum = nums[i] + nums[i + 1];
            if !seen.insert(sum) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (find-subarrays nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((prev (car nums))
             (rest (cdr nums))
             (seen (make-hash)))
    (if (null? rest)
        #f
        (let* ((curr (car rest))
               (s (+ prev curr)))
          (if (hash-has-key? seen s)
              #t
              (begin
                (hash-set! seen s #t)
                (loop curr (cdr rest) seen)))))))
```

## Erlang

```erlang
-spec find_subarrays(Nums :: [integer()]) -> boolean().
find_subarrays(Nums) ->
    find_subarrays(Nums, #{}).

find_subarrays([_], _Map) ->
    false;
find_subarrays([], _Map) ->
    false;
find_subarrays([A,B|Rest] = List, Map) ->
    Sum = A + B,
    case maps:is_key(Sum, Map) of
        true -> true;
        false -> find_subarrays([B|Rest], maps:put(Sum, true, Map))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_subarrays(nums :: [integer]) :: boolean
  def find_subarrays(nums) do
    go(nums, MapSet.new())
  end

  defp go([_], _set), do: false
  defp go([], _set), do: false

  defp go([a, b | rest], set) do
    sum = a + b

    if MapSet.member?(set, sum) do
      true
    else
      new_set = MapSet.put(set, sum)

      case rest do
        [] -> false
        [c | tail] -> go([b, c | tail], new_set)
      end
    end
  end
end
```
