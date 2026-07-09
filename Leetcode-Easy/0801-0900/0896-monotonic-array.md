# 0896. Monotonic Array

## Cpp

```cpp
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool inc = false, dec = false;
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] > nums[i - 1]) inc = true;
            else if (nums[i] < nums[i - 1]) dec = true;
            if (inc && dec) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean increasing = true;
        boolean decreasing = true;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                decreasing = false;
            }
            if (nums[i] < nums[i - 1]) {
                increasing = false;
            }
        }
        return increasing || decreasing;
    }
}
```

## Python

```python
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            elif nums[i] < nums[i - 1]:
                inc = False
            if not inc and not dec:
                return False
        return inc or dec
```

## Python3

```python
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            elif nums[i] < nums[i - 1]:
                inc = False
            if not inc and not dec:
                return False
        return inc or dec
```

## C

```c
#include <stdbool.h>

bool isMonotonic(int* nums, int numsSize) {
    if (numsSize <= 2) return true;
    
    bool increasing = true;
    bool decreasing = true;
    
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] > nums[i - 1]) decreasing = false;
        if (nums[i] < nums[i - 1]) increasing = false;
        if (!increasing && !decreasing) return false;
    }
    
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsMonotonic(int[] nums) {
        bool increasing = false;
        bool decreasing = false;
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                increasing = true;
            } else if (nums[i] > nums[i + 1]) {
                decreasing = true;
            }
            if (increasing && decreasing) {
                return false;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    let increasing = true;
    let decreasing = true;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) decreasing = false;
        if (nums[i] < nums[i - 1]) increasing = false;
        if (!increasing && !decreasing) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isMonotonic(nums: number[]): boolean {
    const n = nums.length;
    if (n <= 2) return true;

    let i = 1;
    while (i < n && nums[i] === nums[i - 1]) i++;
    if (i === n) return true; // all elements equal

    const increasing = nums[i] > nums[i - 1];
    for (; i < n; i++) {
        if (increasing) {
            if (nums[i] < nums[i - 1]) return false;
        } else {
            if (nums[i] > nums[i - 1]) return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isMonotonic($nums) {
        $increasing = true;
        $decreasing = true;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $decreasing = false;
            }
            if ($nums[$i] < $nums[$i - 1]) {
                $increasing = false;
            }
        }
        return $increasing || $decreasing;
    }
}
```

## Swift

```swift
class Solution {
    func isMonotonic(_ nums: [Int]) -> Bool {
        var increasing = true
        var decreasing = true
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                decreasing = false
            } else if nums[i] < nums[i - 1] {
                increasing = false
            }
        }
        return increasing || decreasing
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isMonotonic(nums: IntArray): Boolean {
        var increasing = true
        var decreasing = true
        for (i in 1 until nums.size) {
            if (nums[i] > nums[i - 1]) decreasing = false
            if (nums[i] < nums[i - 1]) increasing = false
        }
        return increasing || decreasing
    }
}
```

## Dart

```dart
class Solution {
  bool isMonotonic(List<int> nums) {
    if (nums.length <= 2) return true;
    bool increasing = true;
    bool decreasing = true;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) decreasing = false;
      if (nums[i] < nums[i - 1]) increasing = false;
      if (!increasing && !decreasing) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isMonotonic(nums []int) bool {
	n := len(nums)
	if n <= 2 {
		return true
	}
	i := 1
	for i < n && nums[i] == nums[i-1] {
		i++
	}
	if i == n {
		return true
	}
	inc := nums[i] > nums[i-1]
	for ; i < n; i++ {
		if inc && nums[i] < nums[i-1] {
			return false
		}
		if !inc && nums[i] > nums[i-1] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_monotonic(nums)
  increasing = true
  decreasing = true
  (0...nums.length - 1).each do |i|
    if nums[i] < nums[i + 1]
      decreasing = false
    elsif nums[i] > nums[i + 1]
      increasing = false
    end
  end
  increasing || decreasing
end
```

## Scala

```scala
object Solution {
    def isMonotonic(nums: Array[Int]): Boolean = {
        var increasing = true
        var decreasing = true
        for (i <- 1 until nums.length) {
            if (nums(i) > nums(i - 1)) decreasing = false
            if (nums(i) < nums(i - 1)) increasing = false
        }
        increasing || decreasing
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_monotonic(nums: Vec<i32>) -> bool {
        if nums.len() <= 2 {
            return true;
        }
        let mut inc = true;
        let mut dec = true;
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                dec = false;
            }
            if nums[i] < nums[i - 1] {
                inc = false;
            }
        }
        inc || dec
    }
}
```

## Racket

```racket
(define/contract (is-monotonic nums)
  (-> (listof exact-integer?) boolean?)
  (if (or (null? nums) (null? (cdr nums)))
      #t
      (let loop ((prev (car nums))
                 (rest (cdr nums))
                 (inc #t)
                 (dec #t))
        (if (null? rest)
            (or inc dec)
            (let* ((curr (car rest))
                   (new-inc (and inc (<= prev curr)))
                   (new-dec (and dec (>= prev curr))))
              (loop curr (cdr rest) new-inc new-dec))))))
```

## Erlang

```erlang
-module(solution).
-export([is_monotonic/1]).

-spec is_monotonic(Nums :: [integer()]) -> boolean().
is_monotonic([]) ->
    true;
is_monotonic([_]) ->
    true;
is_monotonic([H|T]) ->
    is_monotonic(T, H, true, true).

%% Helper: process remaining list with previous element and flags.
-spec is_monotonic([integer()], integer(), boolean(), boolean()) -> boolean().
is_monotonic([], _Prev, Inc, Dec) ->
    Inc orelse Dec;
is_monotonic([Curr|Rest], Prev, Inc, Dec) ->
    NewInc = Inc andalso (Prev =< Curr),
    NewDec = Dec andalso (Prev >= Curr),
    case NewInc orelse NewDec of
        true -> is_monotonic(Rest, Curr, NewInc, NewDec);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_monotonic(nums :: [integer]) :: boolean
  def is_monotonic([]), do: true
  def is_monotonic([_]), do: true

  def is_monotonic(nums) do
    {inc, dec} =
      Enum.reduce(Enum.chunk_every(nums, 2, 1, []), {true, true}, fn [a, b], {inc, dec} ->
        {
          inc && a <= b,
          dec && a >= b
        }
      end)

    inc or dec
  end
end
```
