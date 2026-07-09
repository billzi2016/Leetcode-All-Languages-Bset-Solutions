# 1848. Minimum Distance to the Target Element

## Cpp

```cpp
class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int ans = INT_MAX;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == target) {
                ans = min(ans, abs(i - start));
                // early exit if distance is zero
                if (ans == 0) break;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                int dist = Math.abs(i - start);
                if (dist < minDist) {
                    minDist = dist;
                }
            }
        }
        return minDist;
    }
}
```

## Python

```python
class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = len(nums)  # maximum possible distance is len-1
        for i, val in enumerate(nums):
            if val == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
                    if min_dist == 0:  # cannot get better than zero
                        break
        return min_dist
```

## Python3

```python
from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = len(nums)
        for i, val in enumerate(nums):
            if val == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
        return min_dist
```

## C

```c
int getMinDistance(int* nums, int numsSize, int target, int start) {
    int minDist = numsSize;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == target) {
            int d = i - start;
            if (d < 0) d = -d;
            if (d < minDist) minDist = d;
        }
    }
    return minDist;
}
```

## Csharp

```csharp
public class Solution {
    public int GetMinDistance(int[] nums, int target, int start) {
        int minDist = int.MaxValue;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) {
                int dist = Math.Abs(i - start);
                if (dist < minDist) {
                    minDist = dist;
                }
            }
        }
        return minDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @param {number} start
 * @return {number}
 */
var getMinDistance = function(nums, target, start) {
    let minDist = Infinity;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            const dist = Math.abs(i - start);
            if (dist < minDist) minDist = dist;
        }
    }
    return minDist;
};
```

## Typescript

```typescript
function getMinDistance(nums: number[], target: number, start: number): number {
    let minDist = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            const dist = Math.abs(i - start);
            if (dist < minDist) minDist = dist;
        }
    }
    return minDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @param Integer $start
     * @return Integer
     */
    function getMinDistance($nums, $target, $start) {
        $min = PHP_INT_MAX;
        foreach ($nums as $i => $val) {
            if ($val == $target) {
                $dist = abs($i - $start);
                if ($dist < $min) {
                    $min = $dist;
                }
                if ($min === 0) {
                    break;
                }
            }
        }
        return $min;
    }
}
```

## Swift

```swift
class Solution {
    func getMinDistance(_ nums: [Int], _ target: Int, _ start: Int) -> Int {
        var minDist = Int.max
        for i in 0..<nums.count {
            if nums[i] == target {
                let dist = abs(i - start)
                if dist < minDist {
                    minDist = dist
                }
            }
        }
        return minDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMinDistance(nums: IntArray, target: Int, start: Int): Int {
        var minDist = Int.MAX_VALUE
        for (i in nums.indices) {
            if (nums[i] == target) {
                val dist = kotlin.math.abs(i - start)
                if (dist < minDist) {
                    minDist = dist
                }
            }
        }
        return minDist
    }
}
```

## Dart

```dart
class Solution {
  int getMinDistance(List<int> nums, int target, int start) {
    int minDist = nums.length;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == target) {
        int d = (i - start).abs();
        if (d < minDist) {
          minDist = d;
        }
      }
    }
    return minDist;
  }
}
```

## Golang

```go
func getMinDistance(nums []int, target int, start int) int {
	minDist := len(nums)
	for i, v := range nums {
		if v == target {
			dist := i - start
			if dist < 0 {
				dist = -dist
			}
			if dist < minDist {
				minDist = dist
			}
		}
	}
	return minDist
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @param {Integer} start
# @return {Integer}
def get_min_distance(nums, target, start)
  min_dist = Float::INFINITY
  nums.each_with_index do |val, i|
    if val == target
      dist = (i - start).abs
      min_dist = dist if dist < min_dist
    end
  end
  min_dist.to_i
end
```

## Scala

```scala
object Solution {
    def getMinDistance(nums: Array[Int], target: Int, start: Int): Int = {
        var minDist = Int.MaxValue
        for (i <- nums.indices) {
            if (nums(i) == target) {
                val d = math.abs(i - start)
                if (d < minDist) minDist = d
            }
        }
        minDist
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut min_dist = i32::MAX;
        for (i, &val) in nums.iter().enumerate() {
            if val == target {
                let dist = (i as i32 - start).abs();
                if dist < min_dist {
                    min_dist = dist;
                }
            }
        }
        min_dist
    }
}
```

## Racket

```racket
(define/contract (get-min-distance nums target start)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let loop ((lst nums) (idx 0) (best (+ (length nums) 1)))
    (cond
      [(null? lst) best]
      [else
       (define new-best
         (if (= (car lst) target)
             (let ((dist (abs (- idx start))))
               (if (< dist best) dist best))
             best))
       (loop (cdr lst) (+ idx 1) new-best)])))
```

## Erlang

```erlang
-spec get_min_distance([integer()], integer(), integer()) -> integer().
get_min_distance(Nums, Target, Start) ->
    get_min_distance(Nums, Target, Start, 0, length(Nums)).

get_min_distance([], _, _, _, Min) ->
    Min;
get_min_distance([H|T], Target, Start, Index, Min) ->
    NewMin = case H of
        Target -> min(Min, erlang:abs(Index - Start));
        _ -> Min
    end,
    get_min_distance(T, Target, Start, Index + 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_min_distance(nums :: [integer], target :: integer, start :: integer) :: integer
  def get_min_distance(nums, target, start) do
    nums
    |> Enum.with_index()
    |> Enum.filter(fn {val, _idx} -> val == target end)
    |> Enum.map(fn {_val, idx} -> Kernel.abs(idx - start) end)
    |> Enum.min()
  end
end
```
