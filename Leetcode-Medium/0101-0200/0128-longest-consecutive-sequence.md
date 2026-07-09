# 0128. Longest Consecutive Sequence

## Cpp

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int best = 0;
        for (int x : s) {
            if (!s.count(x - 1)) { // start of a sequence
                int cur = x;
                int len = 0;
                while (s.count(cur)) {
                    ++len;
                    ++cur;
                }
                best = max(best, len);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int longest = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) { // start of a sequence
                int current = num;
                int length = 1;
                while (set.contains(current + 1)) {
                    current++;
                    length++;
                }
                if (length > longest) {
                    longest = length;
                }
            }
        }
        return longest;
    }
}
```

## Python

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:  # start of a sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
```

## Python3

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n - 1 not in num_set:  # start of a sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int longestConsecutive(int* nums, int numsSize) {
    if (numsSize == 0) return 0;

    qsort(nums, numsSize, sizeof(int), cmp_int);

    int maxLen = 1, curLen = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] == nums[i - 1]) {
            continue;               // skip duplicates
        } else if (nums[i] == nums[i - 1] + 1) {
            curLen++;
        } else {
            if (curLen > maxLen) maxLen = curLen;
            curLen = 1;
        }
    }
    if (curLen > maxLen) maxLen = curLen;
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;

        var set = new HashSet<int>(nums);
        int longest = 0;

        foreach (int num in set)
        {
            // Only start counting if 'num' is the beginning of a sequence
            if (!set.Contains(num - 1))
            {
                int current = num;
                int length = 1;

                while (set.Contains(current + 1))
                {
                    current++;
                    length++;
                }

                if (length > longest) longest = length;
            }
        }

        return longest;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let maxLen = 0;
    
    for (const n of numSet) {
        // only start counting if n is the beginning of a sequence
        if (!numSet.has(n - 1)) {
            let current = n;
            let length = 1;
            
            while (numSet.has(current + 1)) {
                current += 1;
                length += 1;
            }
            
            if (length > maxLen) maxLen = length;
        }
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function longestConsecutive(nums: number[]): number {
    const numSet = new Set<number>(nums);
    let maxLen = 0;

    for (const n of numSet) {
        if (!numSet.has(n - 1)) { // start of a sequence
            let current = n;
            let length = 1;
            while (numSet.has(current + 1)) {
                current += 1;
                length++;
            }
            if (length > maxLen) maxLen = length;
        }
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestConsecutive($nums) {
        if (empty($nums)) {
            return 0;
        }
        $set = [];
        foreach ($nums as $num) {
            $set[$num] = true;
        }

        $longest = 0;
        foreach ($set as $num => $_) {
            if (!isset($set[$num - 1])) { // start of a sequence
                $current = $num;
                $streak = 1;
                while (isset($set[$current + 1])) {
                    $current++;
                    $streak++;
                }
                if ($streak > $longest) {
                    $longest = $streak;
                }
            }
        }

        return $longest;
    }
}
```

## Swift

```swift
class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let numSet = Set(nums)
        var longest = 0
        for num in numSet {
            if !numSet.contains(num - 1) {
                var current = num
                var streak = 1
                while numSet.contains(current + 1) {
                    current += 1
                    streak += 1
                }
                longest = max(longest, streak)
            }
        }
        return longest
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        val set = HashSet<Int>(nums.size)
        for (num in nums) {
            set.add(num)
        }
        var maxLen = 0
        for (num in set) {
            if (!set.contains(num - 1)) { // start of a sequence
                var current = num
                var length = 1
                while (set.contains(current + 1)) {
                    current += 1
                    length++
                }
                if (length > maxLen) maxLen = length
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int longestConsecutive(List<int> nums) {
    final Set<int> numSet = nums.toSet();
    int longest = 0;

    for (int n in numSet) {
      if (!numSet.contains(n - 1)) {
        int current = n;
        int streak = 1;
        while (numSet.contains(current + 1)) {
          current += 1;
          streak++;
        }
        if (streak > longest) longest = streak;
      }
    }

    return longest;
  }
}
```

## Golang

```go
func longestConsecutive(nums []int) int {
	set := make(map[int]struct{}, len(nums))
	for _, v := range nums {
		set[v] = struct{}{}
	}
	maxLen := 0
	for _, v := range nums {
		if _, exists := set[v-1]; !exists {
			cur := v
			length := 0
			for {
				if _, ok := set[cur]; ok {
					length++
					cur++
				} else {
					break
				}
			}
			if length > maxLen {
				maxLen = length
			}
		}
	}
	return maxLen
}
```

## Ruby

```ruby
require 'set'

def longest_consecutive(nums)
  set = nums.to_set
  max_len = 0
  set.each do |num|
    next if set.include?(num - 1)
    current = num
    length = 1
    while set.include?(current + 1)
      current += 1
      length += 1
    end
    max_len = length if length > max_len
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def longestConsecutive(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        val numSet = nums.toSet
        var maxLen = 0

        for (num <- numSet) {
            if (!numSet.contains(num - 1)) {
                var current = num
                var length = 1
                while (numSet.contains(current + 1)) {
                    current += 1
                    length += 1
                }
                if (length > maxLen) maxLen = length
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let set: HashSet<i32> = nums.iter().cloned().collect();
        let mut max_len = 0;
        for &num in &set {
            if !set.contains(&(num - 1)) {
                let mut current = num;
                let mut length = 1;
                while set.contains(&(current + 1)) {
                    current += 1;
                    length += 1;
                }
                if length > max_len {
                    max_len = length;
                }
            }
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (longest-consecutive nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((set (make-hash)))
    (for-each (lambda (x) (hash-set! set x #t)) nums)
    (let loop ((remaining nums) (best 0))
      (if (null? remaining)
          best
          (let* ((num (car remaining))
                 (prev (- num 1)))
            (if (hash-has-key? set prev)
                (loop (cdr remaining) best)
                (let inner ((cur num) (len 0))
                  (if (hash-has-key? set cur)
                      (inner (+ cur 1) (+ len 1))
                      (let ((new-best (if (> len best) len best)))
                        (loop (cdr remaining) new-best)))))))))
```

## Erlang

```erlang
-spec longest_consecutive([integer()]) -> integer().
longest_consecutive(Nums) ->
    Set = maps:from_list([{N, true} || N <- Nums]),
    longest_consecutive_loop(Set, Nums, 0).

%% iterate over the original list, keeping track of the maximum length found
-spec longest_consecutive_loop(map(), [integer()], integer()) -> integer().
longest_consecutive_loop(_, [], Max) ->
    Max;
longest_consecutive_loop(Set, [H|T], Max) ->
    case maps:is_key(H-1, Set) of
        true ->
            %% not the start of a sequence
            longest_consecutive_loop(Set, T, Max);
        false ->
            Len = count_forward(H, Set, 1),
            NewMax = if Len > Max -> Len; true -> Max end,
            longest_consecutive_loop(Set, T, NewMax)
    end.

%% count consecutive numbers forward from Current
-spec count_forward(integer(), map(), integer()) -> integer().
count_forward(Current, Set, Len) ->
    case maps:is_key(Current+1, Set) of
        true -> count_forward(Current+1, Set, Len+1);
        false -> Len
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_consecutive(nums :: [integer]) :: integer
  def longest_consecutive(nums) do
    set = MapSet.new(nums)

    Enum.reduce(set, 0, fn num, max_len ->
      if MapSet.member?(set, num - 1) do
        max_len
      else
        len = count_seq(set, num + 1, 1)
        if len > max_len, do: len, else: max_len
      end
    end)
  end

  defp count_seq(set, next_num, cur_len) do
    if MapSet.member?(set, next_num) do
      count_seq(set, next_num + 1, cur_len + 1)
    else
      cur_len
    end
  end
end
```
