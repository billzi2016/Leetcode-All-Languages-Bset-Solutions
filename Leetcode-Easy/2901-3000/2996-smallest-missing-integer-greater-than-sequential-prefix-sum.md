# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

## Cpp

```cpp
class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int n = nums.size();
        long long sum = 0;
        int i = 0;
        // longest sequential prefix
        while (i < n) {
            sum += nums[i];
            if (i + 1 < n && nums[i + 1] == nums[i] + 1) {
                ++i;
            } else {
                break;
            }
        }
        unordered_set<int> present(nums.begin(), nums.end());
        int x = static_cast<int>(sum);
        while (present.count(x)) ++x;
        return x;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int missingInteger(int[] nums) {
        int n = nums.length;
        int sum = nums[0];
        int i = 1;
        while (i < n && nums[i] == nums[i - 1] + 1) {
            sum += nums[i];
            i++;
        }
        Set<Integer> set = new HashSet<>();
        for (int v : nums) {
            set.add(v);
        }
        int x = sum;
        while (set.contains(x)) {
            x++;
        }
        return x;
    }
}
```

## Python

```python
class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find longest sequential prefix and its sum
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        present = set(nums)
        x = total
        while x in present:
            x += 1
        return x
```

## Python3

```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix
        n = len(nums)
        prefix_len = 1  # at least first element
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix_len += 1
            else:
                break
        sum_prefix = sum(nums[:prefix_len])
        
        present = set(nums)
        x = sum_prefix
        while x in present:
            x += 1
        return x
```

## C

```c
int missingInteger(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int prefixEnd = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] == nums[i - 1] + 1)
            prefixEnd = i;
        else
            break;
    }
    long sum = 0;
    for (int i = 0; i <= prefixEnd; ++i) {
        sum += nums[i];
    }
    int x = (int)sum;
    while (1) {
        int found = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] == x) {
                found = 1;
                break;
            }
        }
        if (!found) return x;
        ++x;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int MissingInteger(int[] nums) {
        // Compute sum of the longest sequential prefix
        int n = nums.Length;
        int sum = nums[0];
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                sum += nums[i];
            } else {
                break;
            }
        }

        // Store all numbers in a hash set for O(1) look‑up
        var present = new HashSet<int>(nums);

        // Find the smallest missing integer >= sum
        int candidate = sum;
        while (present.Contains(candidate)) {
            candidate++;
        }
        return candidate;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingInteger = function(nums) {
    const present = new Set(nums);
    
    // Compute sum of the longest sequential prefix
    let sum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            sum += nums[i];
        } else {
            break;
        }
    }
    
    // Find the smallest missing integer >= sum
    let x = sum;
    while (present.has(x)) {
        x++;
    }
    return x;
};
```

## Typescript

```typescript
function missingInteger(nums: number[]): number {
    const n = nums.length;
    let prefixEnd = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] === nums[i - 1] + 1) {
            prefixEnd = i;
        } else {
            break;
        }
    }
    let sum = 0;
    for (let i = 0; i <= prefixEnd; i++) {
        sum += nums[i];
    }

    const present = new Set(nums);
    let x = sum;
    while (present.has(x)) {
        x++;
    }
    return x;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingInteger($nums) {
        $n = count($nums);
        // longest sequential prefix sum
        $sum = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] == $nums[$i - 1] + 1) {
                $sum += $nums[$i];
            } else {
                break;
            }
        }

        // build set of existing numbers
        $present = array_flip($nums);

        // find smallest missing integer >= sum
        $x = $sum;
        while (isset($present[$x])) {
            $x++;
        }
        return $x;
    }
}
```

## Swift

```swift
class Solution {
    func missingInteger(_ nums: [Int]) -> Int {
        var i = 1
        while i < nums.count && nums[i] == nums[i - 1] + 1 {
            i += 1
        }
        let prefixEnd = i - 1
        var sum = 0
        for idx in 0...prefixEnd {
            sum += nums[idx]
        }
        let numSet = Set(nums)
        var x = sum
        while numSet.contains(x) {
            x += 1
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun missingInteger(nums: IntArray): Int {
        var prefixLen = 1
        for (i in 1 until nums.size) {
            if (nums[i] == nums[i - 1] + 1) {
                prefixLen++
            } else break
        }
        var sum = 0
        for (i in 0 until prefixLen) {
            sum += nums[i]
        }
        val present = HashSet<Int>()
        for (v in nums) present.add(v)
        var x = sum
        while (present.contains(x)) {
            x++
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int missingInteger(List<int> nums) {
    int n = nums.length;
    int i = 1;
    while (i < n && nums[i] == nums[i - 1] + 1) {
      i++;
    }
    int sum = 0;
    for (int j = 0; j < i; j++) {
      sum += nums[j];
    }
    Set<int> present = nums.toSet();
    int x = sum;
    while (present.contains(x)) {
      x++;
    }
    return x;
  }
}
```

## Golang

```go
func missingInteger(nums []int) int {
	n := len(nums)
	end := 1
	for i := 1; i < n; i++ {
		if nums[i] == nums[i-1]+1 {
			end++
		} else {
			break
		}
	}
	sum := 0
	for i := 0; i < end; i++ {
		sum += nums[i]
	}
	exist := make(map[int]struct{}, n)
	for _, v := range nums {
		exist[v] = struct{}{}
	}
	x := sum
	for {
		if _, ok := exist[x]; !ok {
			return x
		}
		x++
	}
}
```

## Ruby

```ruby
def missing_integer(nums)
  idx = 0
  while idx + 1 < nums.length && nums[idx + 1] == nums[idx] + 1
    idx += 1
  end
  prefix_sum = nums[0..idx].sum
  present = {}
  nums.each { |v| present[v] = true }
  x = prefix_sum
  x += 1 while present.key?(x)
  x
end
```

## Scala

```scala
object Solution {
    def missingInteger(nums: Array[Int]): Int = {
        val n = nums.length
        var end = 0
        while (end + 1 < n && nums(end + 1) == nums(end) + 1) {
            end += 1
        }
        var sum = 0
        var i = 0
        while (i <= end) {
            sum += nums(i)
            i += 1
        }
        val present = nums.toSet
        var x = sum
        while (present.contains(x)) {
            x += 1
        }
        x
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        // Compute sum of the longest sequential prefix
        let mut sum = nums[0];
        for i in 1..nums.len() {
            if nums[i] == nums[i - 1] + 1 {
                sum += nums[i];
            } else {
                break;
            }
        }

        // Store all numbers for O(1) existence checks
        let set: HashSet<i32> = nums.into_iter().collect();

        // Find the smallest missing integer >= sum
        let mut x = sum;
        while set.contains(&x) {
            x += 1;
        }
        x
    }
}
```

## Racket

```racket
(define/contract (missing-integer nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((num-set
          (let ((h (make-hash)))
            (for-each (lambda (n) (hash-set! h n #t)) nums)
            h))
         (sum-prefix
          (if (null? nums)
              0
              (let loop ((rest (cdr nums))
                         (prev (car nums))
                         (acc (car nums)))
                (if (or (null? rest) (not (= (car rest) (+ prev 1))))
                    acc
                    (loop (cdr rest) (car rest) (+ acc (car rest))))))))
    (let loop ((x sum-prefix))
      (if (hash-has-key? num-set x)
          (loop (+ x 1))
          x))))
```

## Erlang

```erlang
-spec missing_integer(Nums :: [integer()]) -> integer().
missing_integer(Nums) ->
    PrefixSum = prefix_sum_seq(Nums),
    Set = sets:from_list(Nums),
    find_missing(PrefixSum, Set).

prefix_sum_seq([]) -> 0;
prefix_sum_seq([H|T]) ->
    prefix_sum_seq(T, H, H).

prefix_sum_seq([], _Prev, Acc) -> Acc;
prefix_sum_seq([X|Rest], Prev, Acc) ->
    if X =:= Prev + 1 ->
            prefix_sum_seq(Rest, X, Acc + X);
       true ->
            Acc
    end.

find_missing(Curr, Set) ->
    case sets:is_element(Curr, Set) of
        true -> find_missing(Curr+1, Set);
        false -> Curr
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec missing_integer(nums :: [integer]) :: integer
  def missing_integer([first | rest] = nums) do
    {prefix_sum, _} =
      Enum.reduce_while(rest, {first, first}, fn cur, {sum, prev} ->
        if cur == prev + 1 do
          {:cont, {sum + cur, cur}}
        else
          {:halt, {sum, prev}}
        end
      end)

    set = MapSet.new(nums)
    find_missing(prefix_sum, set)
  end

  defp find_missing(x, set) do
    if MapSet.member?(set, x), do: find_missing(x + 1, set), else: x
  end
end
```
