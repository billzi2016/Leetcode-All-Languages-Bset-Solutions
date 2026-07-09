# 2441. Largest Positive Integer That Exists With Its Negative

## Cpp

```cpp
class Solution {
public:
    int findMaxK(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        int ans = -1;
        for (int num : nums) {
            if (seen.count(-num)) {
                ans = std::max(ans, std::abs(num));
            }
            seen.insert(num);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findMaxK(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        int ans = -1;
        for (int num : nums) {
            if (seen.contains(-num)) {
                ans = Math.max(ans, Math.abs(num));
            }
            seen.add(num);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        ans = -1
        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            seen.add(num)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -1
        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            seen.add(num)
        return ans
```

## C

```c
#include <stdbool.h>

int findMaxK(int* nums, int numsSize) {
    bool seen[2001] = {false};
    const int offset = 1000;
    
    for (int i = 0; i < numsSize; ++i) {
        seen[nums[i] + offset] = true;
    }
    
    int ans = -1;
    for (int k = 1; k <= 1000; ++k) {
        if (seen[k + offset] && seen[-k + offset]) {
            ans = k; // larger k will overwrite previous
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMaxK(int[] nums) {
        var seen = new System.Collections.Generic.HashSet<int>();
        int ans = -1;
        foreach (int num in nums) {
            if (seen.Contains(-num)) {
                int candidate = System.Math.Abs(num);
                if (candidate > ans) ans = candidate;
            }
            seen.Add(num);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums) {
    const seen = new Set();
    let ans = -1;
    for (const num of nums) {
        if (seen.has(-num)) {
            const candidate = Math.abs(num);
            if (candidate > ans) ans = candidate;
        }
        seen.add(num);
    }
    return ans;
};
```

## Typescript

```typescript
function findMaxK(nums: number[]): number {
    const seen = new Set<number>();
    let ans = -1;
    for (const num of nums) {
        if (seen.has(-num)) {
            const k = Math.abs(num);
            if (k > ans) ans = k;
        }
        seen.add(num);
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxK($nums) {
        $seen = [];
        $ans = -1;
        foreach ($nums as $num) {
            if (isset($seen[-$num])) {
                $abs = abs($num);
                if ($abs > $ans) {
                    $ans = $abs;
                }
            }
            $seen[$num] = true;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxK(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        var ans = -1
        for num in nums {
            if seen.contains(-num) {
                let candidate = abs(num)
                if candidate > ans {
                    ans = candidate
                }
            }
            seen.insert(num)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxK(nums: IntArray): Int {
        var ans = -1
        val seen = HashSet<Int>()
        for (num in nums) {
            if (seen.contains(-num)) {
                ans = kotlin.math.max(ans, kotlin.math.abs(num))
            }
            seen.add(num)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findMaxK(List<int> nums) {
    final Set<int> seen = {};
    int ans = -1;
    for (final num in nums) {
      if (seen.contains(-num)) {
        int candidate = num.abs();
        if (candidate > ans) ans = candidate;
      }
      seen.add(num);
    }
    return ans;
  }
}
```

## Golang

```go
func findMaxK(nums []int) int {
	seen := make(map[int]struct{}, len(nums))
	ans := -1
	for _, num := range nums {
		if _, ok := seen[-num]; ok {
			if num < 0 {
				num = -num
			}
			if num > ans {
				ans = num
			}
		}
		seen[num] = struct{}{}
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

def find_max_k(nums)
  seen = Set.new
  ans = -1
  nums.each do |num|
    if seen.include?(-num)
      candidate = num.abs
      ans = candidate if candidate > ans
    end
    seen.add(num)
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findMaxK(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        var ans = -1
        for (num <- nums) {
            if (seen.contains(-num)) {
                val candidate = math.abs(num)
                if (candidate > ans) ans = candidate
            }
            seen.add(num)
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let mut seen = HashSet::new();
        let mut ans = -1;
        for &num in nums.iter() {
            if seen.contains(&-num) {
                let cand = num.abs();
                if cand > ans {
                    ans = cand;
                }
            }
            seen.insert(num);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-max-k nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((seen (make-hash))
        (best -1))
    (for ([num nums])
      (when (hash-has-key? seen (- num))
        (set! best (max best (abs num))))
      (hash-set! seen num #t))
    best))
```

## Erlang

```erlang
-spec find_max_k([integer()]) -> integer().
find_max_k(Nums) ->
    find_max_k(Nums, #{}, -1).

find_max_k([], _Seen, Ans) ->
    Ans;
find_max_k([Num | Rest], Seen, Ans) ->
    Neg = -Num,
    NewAns =
        case maps:is_key(Neg, Seen) of
            true ->
                Abs = erlang:abs(Num),
                if Abs > Ans -> Abs; true -> Ans end;
            false -> Ans
        end,
    find_max_k(Rest, maps:put(Num, true, Seen), NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_k(nums :: [integer]) :: integer
  def find_max_k(nums) do
    {ans, _} =
      Enum.reduce(nums, {-1, MapSet.new()}, fn num, {cur_ans, seen} ->
        new_ans =
          if MapSet.member?(seen, -num) do
            max(cur_ans, abs(num))
          else
            cur_ans
          end

        {new_ans, MapSet.put(seen, num)}
      end)

    ans
  end
end
```
