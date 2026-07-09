# 0915. Partition Array into Disjoint Intervals

## Cpp

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int n = nums.size();
        int left_max = nums[0];      // max that must be in left part
        int cur_max = nums[0];       // max seen so far (could be in left)
        int ans = 1;                 // length of left part
        
        for (int i = 1; i < n; ++i) {
            if (nums[i] < left_max) {
                // need to extend left part up to i
                ans = i + 1;
                left_max = cur_max;
            } else {
                cur_max = max(cur_max, nums[i]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int partitionDisjoint(int[] nums) {
        int n = nums.length;
        int currMax = nums[0];      // max that must be in left
        int possibleMax = nums[0];  // overall max seen so far
        int leftLen = 1;            // length of left part
        
        for (int i = 1; i < n; i++) {
            if (nums[i] < currMax) {
                // need to include this element in left
                leftLen = i + 1;
                currMax = possibleMax;
            } else {
                // update overall max seen so far
                if (nums[i] > possibleMax) {
                    possibleMax = nums[i];
                }
            }
        }
        return leftLen;
    }
}
```

## Python

```python
class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = possible_max = nums[0]
        left_len = 1
        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                left_len = i + 1
                curr_max = possible_max
            else:
                if nums[i] > possible_max:
                    possible_max = nums[i]
        return left_len
```

## Python3

```python
from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = possible_max = nums[0]
        left_len = 1
        for i in range(1, len(nums)):
            if nums[i] < curr_max:
                left_len = i + 1
                curr_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])
        return left_len
```

## C

```c
int partitionDisjoint(int* nums, int numsSize) {
    int curr_max = nums[0];
    int possible_max = nums[0];
    int ans = 1;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < curr_max) {
            ans = i + 1;
            curr_max = possible_max;
        } else {
            if (nums[i] > possible_max) possible_max = nums[i];
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int PartitionDisjoint(int[] nums)
    {
        int currMax = nums[0];
        int possibleMax = nums[0];
        int leftLength = 1;

        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] < currMax)
            {
                leftLength = i + 1;
                currMax = possibleMax;
            }
            else
            {
                if (nums[i] > possibleMax)
                    possibleMax = nums[i];
            }
        }

        return leftLength;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var partitionDisjoint = function(nums) {
    let currMax = nums[0];
    let possibleMax = nums[0];
    let leftLen = 1;
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < currMax) {
            // Need to extend the left partition up to i
            leftLen = i + 1;
            currMax = possibleMax;
        } else {
            // Update the maximum seen so far in the traversed part
            if (nums[i] > possibleMax) possibleMax = nums[i];
        }
    }
    
    return leftLen;
};
```

## Typescript

```typescript
function partitionDisjoint(nums: number[]): number {
    let currMax = nums[0];
    let possibleMax = nums[0];
    let leftLen = 1;
    for (let i = 1; i < nums.length; i++) {
        const val = nums[i];
        if (val < currMax) {
            leftLen = i + 1;
            currMax = possibleMax;
        } else {
            if (val > possibleMax) possibleMax = val;
        }
    }
    return leftLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function partitionDisjoint($nums) {
        $n = count($nums);
        $currMax = $nums[0];
        $possibleMax = $nums[0];
        $len = 1; // length of left part

        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] < $currMax) {
                // need to extend left partition up to i
                $len = $i + 1;
                $currMax = $possibleMax;
            } else {
                if ($nums[$i] > $possibleMax) {
                    $possibleMax = $nums[$i];
                }
            }
        }

        return $len;
    }
}
```

## Swift

```swift
class Solution {
    func partitionDisjoint(_ nums: [Int]) -> Int {
        var currMax = nums[0]
        var possibleMax = nums[0]
        var leftLen = 1
        for i in 1..<nums.count {
            let val = nums[i]
            if val < currMax {
                leftLen = i + 1
                currMax = possibleMax
            }
            if val > possibleMax {
                possibleMax = val
            }
        }
        return leftLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partitionDisjoint(nums: IntArray): Int {
        var currMax = nums[0]
        var possibleMax = nums[0]
        var leftSize = 1
        for (i in 1 until nums.size) {
            val v = nums[i]
            if (v < currMax) {
                leftSize = i + 1
                currMax = possibleMax
            } else {
                if (v > possibleMax) possibleMax = v
            }
        }
        return leftSize
    }
}
```

## Dart

```dart
class Solution {
  int partitionDisjoint(List<int> nums) {
    int n = nums.length;
    int currMax = nums[0];
    int possibleMax = nums[0];
    int leftLen = 1;

    for (int i = 1; i < n; ++i) {
      if (nums[i] < currMax) {
        leftLen = i + 1;
        currMax = possibleMax;
      }
      if (nums[i] > possibleMax) {
        possibleMax = nums[i];
      }
    }

    return leftLen;
  }
}
```

## Golang

```go
func partitionDisjoint(nums []int) int {
    currMax := nums[0]
    possibleMax := nums[0]
    leftLen := 1
    for i := 1; i < len(nums); i++ {
        if nums[i] < currMax {
            leftLen = i + 1
            currMax = possibleMax
        } else if nums[i] > possibleMax {
            possibleMax = nums[i]
        }
    }
    return leftLen
}
```

## Ruby

```ruby
def partition_disjoint(nums)
  curr_max = nums[0]
  possible_max = nums[0]
  left_len = 1

  (1...nums.length).each do |i|
    x = nums[i]
    if x < curr_max
      left_len = i + 1
      curr_max = possible_max
    end
    possible_max = x if x > possible_max
  end

  left_len
end
```

## Scala

```scala
object Solution {
  def partitionDisjoint(nums: Array[Int]): Int = {
    var currMax = nums(0)
    var possibleMax = nums(0)
    var leftLen = 1
    var i = 1
    while (i < nums.length) {
      val v = nums(i)
      if (v < currMax) {
        leftLen = i + 1
        currMax = possibleMax
      } else {
        if (v > possibleMax) possibleMax = v
      }
      i += 1
    }
    leftLen
  }
}
```

## Rust

```rust
impl Solution {
    pub fn partition_disjoint(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut curr_max = nums[0];
        let mut possible_max = nums[0];
        let mut left_len = 1usize;
        for i in 1..n {
            let x = nums[i];
            if x < curr_max {
                left_len = i + 1;
                curr_max = possible_max;
            }
            if x > possible_max {
                possible_max = x;
            }
        }
        left_len as i32
    }
}
```

## Racket

```racket
(define/contract (partition-disjoint nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((first (car nums))
         (rest (cdr nums)))
    (let loop ((i 1)                ; current index
               (lst rest)           ; remaining elements
               (curr-max first)     ; max that must stay in left
               (possible-max first) ; overall max seen so far
               (len 1))              ; length of left partition
      (if (null? lst)
          len
          (let ((num (car lst)))
            (if (< num curr-max)
                ;; need to extend left up to this index
                (loop (+ i 1) (cdr lst) possible-max possible-max (+ i 1))
                ;; otherwise just update possible max
                (let ((new-possible (max possible-max num)))
                  (loop (+ i 1) (cdr lst) curr-max new-possible len))))))))
```

## Erlang

```erlang
-module(solution).
-export([partition_disjoint/1]).

-spec partition_disjoint(Nums :: [integer()]) -> integer().
partition_disjoint([H|T]) ->
    loop(T, H, H, 1, 2).

loop([], _CurrMax, _PossibleMax, Len, _Idx) ->
    Len;
loop([X|Rest], CurrMax, PossibleMax, Len, Idx) ->
    case X < CurrMax of
        true ->
            NewLen = Idx,
            NewCurrMax = PossibleMax,
            NewPossibleMax = erlang:max(PossibleMax, X),
            loop(Rest, NewCurrMax, NewPossibleMax, NewLen, Idx + 1);
        false ->
            NewPossibleMax = erlang:max(PossibleMax, X),
            loop(Rest, CurrMax, NewPossibleMax, Len, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec partition_disjoint(nums :: [integer]) :: integer
  def partition_disjoint([first | rest]) do
    {_curr_max, _possible_max, left_len} =
      Enum.reduce(Enum.with_index(rest, 1), {first, first, 1}, fn {h, idx},
                                                                {curr_max, possible_max,
                                                                 left_len} ->
        if h < curr_max do
          new_len = idx + 1
          new_curr = max(possible_max, h)
          {new_curr, new_curr, new_len}
        else
          new_possible = max(possible_max, h)
          {curr_max, new_possible, left_len}
        end
      end)

    left_len
  end
end
```
