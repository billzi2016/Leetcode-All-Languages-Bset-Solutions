# 0665. Non-decreasing Array

## Cpp

```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt = 0;
        for (int i = 0; i + 1 < (int)nums.size(); ++i) {
            if (nums[i] > nums[i + 1]) {
                ++cnt;
                if (cnt > 1) return false;
                // decide which element to modify
                if (i == 0 || nums[i - 1] <= nums[i + 1]) {
                    // lower nums[i] to nums[i+1]
                    nums[i] = nums[i + 1];
                } else {
                    // raise nums[i+1] to nums[i]
                    nums[i + 1] = nums[i];
                }
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkPossibility(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length - 1 && count <= 1; i++) {
            if (nums[i] > nums[i + 1]) {
                count++;
                if (i == 0 || nums[i - 1] <= nums[i + 1]) {
                    // modify nums[i] down to nums[i+1]
                    // no actual change needed for checking further
                } else {
                    // modify nums[i+1] up to nums[i]
                    nums[i + 1] = nums[i];
                }
            }
        }
        return count <= 1;
    }
}
```

## Python

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                # decide which element to modify
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    # lower nums[i] to nums[i+1]
                    nums[i] = nums[i + 1]
                else:
                    # raise nums[i+1] to nums[i]
                    nums[i + 1] = nums[i]
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False
                # Decide which element to adjust
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    # Adjust nums[i] down to nums[i+1] (conceptually)
                    pass
                else:
                    # Adjust nums[i+1] up to nums[i]
                    nums[i + 1] = nums[i]
        return True
```

## C

```c
#include <stdbool.h>

bool checkPossibility(int* nums, int numsSize) {
    if (numsSize <= 2) return true;
    int violations = 0;
    for (int i = 0; i < numsSize - 1; ++i) {
        if (nums[i] > nums[i + 1]) {
            if (++violations > 1) return false;
            // Decide which element to adjust
            if (i == 0 || nums[i - 1] <= nums[i + 1]) {
                // Lower nums[i] to nums[i+1] (conceptually)
                // No actual modification needed for further checks
            } else {
                // Raise nums[i+1] to nums[i]
                nums[i + 1] = nums[i];
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckPossibility(int[] nums) {
        int violations = 0;
        for (int i = 0; i < nums.Length - 1 && violations <= 1; i++) {
            if (nums[i] > nums[i + 1]) {
                violations++;
                if (i == 0 || nums[i - 1] <= nums[i + 1]) {
                    // modify nums[i] down to nums[i+1]; no actual change needed
                } else {
                    // modify nums[i+1] up to nums[i]
                    nums[i + 1] = nums[i];
                }
            }
        }
        return violations <= 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    let modifications = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            modifications++;
            if (modifications > 1) return false;
            // Decide which element to adjust
            if (i === 0 || nums[i - 1] <= nums[i + 1]) {
                // Lower nums[i] to nums[i+1]
                nums[i] = nums[i + 1];
            } else {
                // Raise nums[i+1] to nums[i]
                nums[i + 1] = nums[i];
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkPossibility(nums: number[]): boolean {
    let modifications = 0;
    for (let i = 0; i < nums.length - 1 && modifications <= 1; i++) {
        if (nums[i] > nums[i + 1]) {
            modifications++;
            if (i === 0 || nums[i - 1] <= nums[i + 1]) {
                nums[i] = nums[i + 1];
            } else {
                nums[i + 1] = nums[i];
            }
        }
    }
    return modifications <= 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function checkPossibility($nums) {
        $n = count($nums);
        $cnt = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) {
                $cnt++;
                if ($cnt > 1) {
                    return false;
                }
                // Decide which element to adjust
                if ($i == 0 || $nums[$i - 1] <= $nums[$i + 1]) {
                    // Lower nums[i] to nums[i+1] (no need to actually change for further checks)
                } else {
                    // Raise nums[i+1] to nums[i]
                    $nums[$i + 1] = $nums[$i];
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkPossibility(_ nums: [Int]) -> Bool {
        var arr = nums
        var modifications = 0
        for i in 0..<(arr.count - 1) {
            if arr[i] > arr[i + 1] {
                modifications += 1
                if modifications > 1 { return false }
                if i == 0 || arr[i - 1] <= arr[i + 1] {
                    arr[i] = arr[i + 1]
                } else {
                    arr[i + 1] = arr[i]
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkPossibility(nums: IntArray): Boolean {
        var violations = 0
        for (i in 0 until nums.size - 1) {
            if (nums[i] > nums[i + 1]) {
                violations++
                if (violations > 1) return false
                if (i == 0 || nums[i - 1] <= nums[i + 1]) {
                    nums[i] = nums[i + 1]
                } else {
                    nums[i + 1] = nums[i]
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkPossibility(List<int> nums) {
    int count = 0;
    for (int i = 0; i < nums.length - 1 && count <= 1; ++i) {
      if (nums[i] > nums[i + 1]) {
        count++;
        if (i == 0 || nums[i - 1] <= nums[i + 1]) {
          nums[i] = nums[i + 1];
        } else {
          nums[i + 1] = nums[i];
        }
      }
    }
    return count <= 1;
  }
}
```

## Golang

```go
func checkPossibility(nums []int) bool {
    violations := 0
    for i := 0; i < len(nums)-1 && violations <= 1; i++ {
        if nums[i] > nums[i+1] {
            violations++
            if i > 0 && nums[i-1] > nums[i+1] {
                // Adjust nums[i+1] to nums[i]
                nums[i+1] = nums[i]
            } else {
                // Adjust nums[i] to nums[i+1]
                nums[i] = nums[i+1]
            }
        }
    }
    return violations <= 1
}
```

## Ruby

```ruby
def check_possibility(nums)
  count = 0
  (0...nums.length - 1).each do |i|
    if nums[i] > nums[i + 1]
      count += 1
      return false if count > 1
      if i == 0 || nums[i - 1] <= nums[i + 1]
        nums[i] = nums[i + 1]
      else
        nums[i + 1] = nums[i]
      end
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkPossibility(nums: Array[Int]): Boolean = {
        var violations = 0
        for (i <- 0 until nums.length - 1) {
            if (nums(i) > nums(i + 1)) {
                violations += 1
                if (violations > 1) return false
                if (i == 0 || nums(i - 1) <= nums(i + 1)) {
                    nums(i) = nums(i + 1)
                } else {
                    nums(i + 1) = nums(i)
                }
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_possibility(mut nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n <= 2 {
            return true;
        }
        let mut violations = 0;
        for i in 0..n - 1 {
            if nums[i] > nums[i + 1] {
                violations += 1;
                if violations > 1 {
                    return false;
                }
                if i == 0 || nums[i - 1] <= nums[i + 1] {
                    nums[i] = nums[i + 1];
                } else {
                    nums[i + 1] = nums[i];
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-possibility nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (<= n 2)
        #t
        (let loop ((i 0) (cnt 0))
          (cond [(>= i (- n 1)) #t]
                [(> cnt 1) #f]
                [(> (vector-ref v i) (vector-ref v (+ i 1)))
                 (let ([new-cnt (+ cnt 1)])
                   (if (> new-cnt 1)
                       #f
                       (begin
                         (if (and (> i 0)
                                  (> (vector-ref v (- i 1))
                                     (vector-ref v (+ i 1))))
                             (vector-set! v (+ i 1) (vector-ref v i))
                             (vector-set! v i (vector-ref v (+ i 1))))
                         (loop (+ i 1) new-cnt))))]
                [else (loop (+ i 1) cnt)]))))))
```

## Erlang

```erlang
-module(solution).
-export([check_possibility/1]).

-spec check_possibility(Nums :: [integer()]) -> boolean().
check_possibility([]) -> true;
check_possibility([_]) -> true;
check_possibility([A,B|Rest]) ->
    helper(none, A, [B|Rest], 0).

helper(_PrevPrev, _Prev, [], _Modified) -> true;
helper(PrevPrev, Prev, [Curr|Tail], Modified) ->
    if
        Prev =< Curr ->
            helper(Prev, Curr, Tail, Modified);
        true ->
            case Modified of
                1 -> false;
                0 ->
                    case PrevPrev of
                        none ->
                            % lower Prev to Curr
                            helper(none, Curr, Tail, 1);
                        _ when PrevPrev =< Curr ->
                            helper(PrevPrev, Curr, Tail, 1);
                        _ ->
                            % raise Curr to Prev
                            helper(Prev, Prev, Tail, 1)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_possibility(nums :: [integer]) :: boolean
  def check_possibility(nums) do
    t = List.to_tuple(nums)
    len = tuple_size(t)

    if len <= 2, do: true, else: loop(0, t, 0, len)
  end

  defp loop(i, _t, cnt, len) when i >= len - 1, do: true

  defp loop(i, t, cnt, len) do
    a = elem(t, i)
    b = elem(t, i + 1)

    if a <= b do
      loop(i + 1, t, cnt, len)
    else
      cnt = cnt + 1

      if cnt > 1 do
        false
      else
        t =
          cond do
            i == 0 or elem(t, i - 1) <= b ->
              put_elem(t, i, b)

            true ->
              put_elem(t, i + 1, a)
          end

        loop(i + 1, t, cnt, len)
      end
    end
  end
end
```
