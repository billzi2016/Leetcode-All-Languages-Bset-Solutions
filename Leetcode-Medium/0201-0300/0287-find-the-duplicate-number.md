# 0287. Find the Duplicate Number

## Cpp

```cpp
class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        int ptr1 = nums[0];
        int ptr2 = slow;
        while (ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        return ptr1;
    }
};
```

## Java

```java
class Solution {
    public int findDuplicate(int[] nums) {
        // Phase 1: Find intersection point of two runners.
        int slow = nums[0];
        int fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        // Phase 2: Find the entrance to the cycle.
        slow = nums[0];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
```

## Python

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Phase 1: Find intersection point of two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
```

## Python3

```python
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point of two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
```

## C

```c
int findDuplicate(int* nums, int numsSize) {
    int tortoise = nums[0];
    int hare = nums[0];
    
    // Phase 1: Find intersection point of two runners.
    do {
        tortoise = nums[tortoise];
        hare = nums[nums[hare]];
    } while (tortoise != hare);
    
    // Phase 2: Find the entrance to the cycle.
    int ptr1 = nums[0];
    int ptr2 = tortoise;
    while (ptr1 != ptr2) {
        ptr1 = nums[ptr1];
        ptr2 = nums[ptr2];
    }
    
    return ptr1;
}
```

## Csharp

```csharp
public class Solution {
    public int FindDuplicate(int[] nums) {
        // Phase 1: Finding the intersection point of two runners.
        int tortoise = nums[0];
        int hare = nums[0];
        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);
        
        // Phase 2: Find the entrance to the cycle.
        int ptr1 = nums[0];
        int ptr2 = tortoise;
        while (ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        return ptr1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let slow = nums[0];
    let fast = nums[0];
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow !== fast);
    
    let finder = nums[0];
    while (finder !== slow) {
        finder = nums[finder];
        slow = nums[slow];
    }
    return finder;
};
```

## Typescript

```typescript
function findDuplicate(nums: number[]): number {
    let tortoise = nums[0];
    let hare = nums[0];

    // Phase 1: Find intersection point of two runners.
    do {
        tortoise = nums[tortoise];
        hare = nums[nums[hare]];
    } while (tortoise !== hare);

    // Phase 2: Find entrance to the cycle.
    let ptr1 = nums[0];
    let ptr2 = tortoise;
    while (ptr1 !== ptr2) {
        ptr1 = nums[ptr1];
        ptr2 = nums[ptr2];
    }
    return ptr1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findDuplicate($nums) {
        // Phase 1: Find intersection point of two runners.
        $slow = $nums[0];
        $fast = $nums[$nums[0]];
        while ($slow !== $fast) {
            $slow = $nums[$slow];
            $fast = $nums[$nums[$fast]];
        }

        // Phase 2: Find the entrance to the cycle.
        $slow = $nums[0];
        while ($slow !== $fast) {
            $slow = $nums[$slow];
            $fast = $nums[$fast];
        }
        return $slow;
    }
}
```

## Swift

```swift
class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        var slow = nums[0]
        var fast = nums[0]
        
        repeat {
            slow = nums[slow]
            fast = nums[nums[fast]]
        } while slow != fast
        
        var finder = nums[0]
        while finder != slow {
            finder = nums[finder]
            slow = nums[slow]
        }
        return finder
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDuplicate(nums: IntArray): Int {
        var slow = nums[0]
        var fast = nums[0]

        // Phase 1: Find intersection point of two runners.
        do {
            slow = nums[slow]
            fast = nums[nums[fast]]
        } while (slow != fast)

        // Phase 2: Find the entrance to the cycle.
        slow = nums[0]
        while (slow != fast) {
            slow = nums[slow]
            fast = nums[fast]
        }
        return slow
    }
}
```

## Dart

```dart
class Solution {
  int findDuplicate(List<int> nums) {
    int tortoise = nums[0];
    int hare = nums[0];
    do {
      tortoise = nums[tortoise];
      hare = nums[nums[hare]];
    } while (tortoise != hare);
    tortoise = nums[0];
    while (tortoise != hare) {
      tortoise = nums[tortoise];
      hare = nums[hare];
    }
    return hare;
  }
}
```

## Golang

```go
func findDuplicate(nums []int) int {
    // Phase 1: Find intersection point of two runners.
    tortoise := nums[0]
    hare := nums[0]
    for {
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare {
            break
        }
    }

    // Phase 2: Find the entrance to the cycle.
    ptr1 := nums[0]
    ptr2 := tortoise
    for ptr1 != ptr2 {
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    }
    return ptr1
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
  # Phase 1: Find intersection point of two runners.
  tortoise = nums[0]
  hare = nums[nums[0]]
  while tortoise != hare
    tortoise = nums[tortoise]
    hare = nums[nums[hare]]
  end

  # Phase 2: Find the entrance to the cycle.
  ptr1 = 0
  ptr2 = tortoise
  while ptr1 != ptr2
    ptr1 = nums[ptr1]
    ptr2 = nums[ptr2]
  end
  ptr1
end
```

## Scala

```scala
object Solution {
    def findDuplicate(nums: Array[Int]): Int = {
        var slow = nums(0)
        var fast = nums(0)

        do {
            slow = nums(slow)
            fast = nums(nums(fast))
        } while (slow != fast)

        slow = nums(0)
        while (slow != fast) {
            slow = nums(slow)
            fast = nums(fast)
        }
        slow
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        // Phase 1: Find intersection point of two runners.
        let mut tortoise = nums[0] as usize;
        let mut hare = nums[tortoise] as usize;
        while tortoise != hare {
            tortoise = nums[tortoise] as usize;
            hare = nums[nums[hare] as usize] as usize;
        }

        // Phase 2: Find the entrance to the cycle.
        let mut ptr1 = 0usize;
        let mut ptr2 = tortoise;
        while ptr1 != ptr2 {
            ptr1 = nums[ptr1] as usize;
            ptr2 = nums[ptr2] as usize;
        }
        ptr1 as i32
    }
}
```

## Racket

```racket
(define/contract (find-duplicate nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (f (lambda (i) (vector-ref v i))))
    ;; Phase 1: find meeting point
    (let loop ((tortoise (f 0))
               (hare (f (f 0))))
      (if (= tortoise hare)
          ;; Phase 2: find entrance to cycle
          (let find-entrance ((ptr1 0) (ptr2 tortoise))
            (if (= ptr1 ptr2)
                ptr1
                (find-entrance (f ptr1) (f ptr2))))
          (loop (f tortoise) (f (f hare)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_duplicate/1]).

-spec find_duplicate(Nums :: [integer()]) -> integer().
find_duplicate(Nums) ->
    Tuple = list_to_tuple(Nums),
    % Phase 1: Find intersection point of two runners.
    Tortoise0 = get_val(Tuple, get_val(Tuple, 0)),
    Hare0 = get_val(Tuple, get_val(Tuple, get_val(Tuple, 0))),
    {Tortoise, _Hare} = find_meeting_point(Tuple, Tortoise0, Hare0),
    % Phase 2: Find entrance to the cycle.
    Start = get_val(Tuple, 0),
    find_entrance(Tuple, Start, Tortoise).

% Recursive search for meeting point.
find_meeting_point(_Tuple, Tortoise, Hare) when Tortoise =:= Hare ->
    {Tortoise, Hare};
find_meeting_point(Tuple, Tortoise, Hare) ->
    NewTortoise = get_val(Tuple, Tortoise),
    NewHare = get_val(Tuple, get_val(Tuple, Hare)),
    find_meeting_point(Tuple, NewTortoise, NewHare).

% Recursive search for cycle entrance.
find_entrance(_Tuple, Ptr1, Ptr2) when Ptr1 =:= Ptr2 ->
    Ptr1;
find_entrance(Tuple, Ptr1, Ptr2) ->
    NewPtr1 = get_val(Tuple, Ptr1),
    NewPtr2 = get_val(Tuple, Ptr2),
    find_entrance(Tuple, NewPtr1, NewPtr2).

% Helper to fetch value at zero‑based index.
get_val(Tuple, Index) ->
    element(Index + 1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_duplicate(nums :: [integer]) :: integer
  def find_duplicate(nums) do
    arr = List.to_tuple(nums)

    # Phase 1: Find the intersection point of the two runners.
    tortoise = elem(arr, 0)
    hare = elem(arr, tortoise)
    meeting = find_meeting_point(arr, tortoise, hare)

    # Phase 2: Find the entrance to the cycle.
    start = elem(arr, 0)
    find_entrance(arr, start, meeting)
  end

  defp find_meeting_point(arr, tortoise, hare) do
    if tortoise == hare do
      tortoise
    else
      next_tortoise = elem(arr, tortoise)
      next_hare = elem(arr, elem(arr, hare))
      find_meeting_point(arr, next_tortoise, next_hare)
    end
  end

  defp find_entrance(arr, ptr1, ptr2) do
    if ptr1 == ptr2 do
      ptr1
    else
      find_entrance(arr, elem(arr, ptr1), elem(arr, ptr2))
    end
  end
end
```
