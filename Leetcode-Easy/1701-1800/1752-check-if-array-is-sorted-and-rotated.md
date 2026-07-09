# 1752. Check if Array Is Sorted and Rotated

## Cpp

```cpp
class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();
        int inv = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] > nums[i + 1]) ++inv;
        }
        if (nums[n - 1] > nums[0]) ++inv;
        return inv <= 1;
    }
};
```

## Java

```java
class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        int inversions = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                inversions++;
                if (inversions > 1) return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                cnt += 1
                if cnt > 1:
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        inv = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                inv += 1
        if nums[-1] > nums[0]:
            inv += 1
        return inv <= 1
```

## C

```c
#include <stdbool.h>

bool check(int* nums, int numsSize) {
    if (numsSize <= 1) return true;
    int inversions = 0;
    for (int i = 0; i < numsSize; ++i) {
        int next = (i + 1) % numsSize;
        if (nums[i] > nums[next]) {
            if (++inversions > 1) return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool Check(int[] nums) {
        int n = nums.Length;
        int inversions = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                inversions++;
                if (inversions > 1) return false;
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
var check = function(nums) {
    const n = nums.length;
    if (n <= 1) return true;
    let inversions = 0;
    for (let i = 0; i < n; i++) {
        const next = (i + 1) % n;
        if (nums[i] > nums[next]) inversions++;
        if (inversions > 1) return false;
    }
    return true;
};
```

## Typescript

```typescript
function check(nums: number[]): boolean {
    const n = nums.length;
    let inversions = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) {
            inversions++;
            if (inversions > 1) return false;
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
    function check($nums) {
        $n = count($nums);
        if ($n <= 1) {
            return true;
        }
        $inversions = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) {
                $inversions++;
            }
        }
        if ($nums[$n - 1] > $nums[0]) {
            $inversions++;
        }
        return $inversions <= 1;
    }
}
```

## Swift

```swift
class Solution {
    func check(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n <= 1 { return true }
        var inversions = 0
        for i in 0..<n {
            let next = (i + 1) % n
            if nums[i] > nums[next] {
                inversions += 1
                if inversions > 1 { return false }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun check(nums: IntArray): Boolean {
        val n = nums.size
        if (n <= 1) return true
        var inversions = 0
        for (i in 0 until n - 1) {
            if (nums[i] > nums[i + 1]) inversions++
        }
        if (nums[n - 1] > nums[0]) inversions++
        return inversions <= 1
    }
}
```

## Dart

```dart
class Solution {
  bool check(List<int> nums) {
    int n = nums.length;
    int inversions = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] > nums[(i + 1) % n]) {
        inversions++;
        if (inversions > 1) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func check(nums []int) bool {
    n := len(nums)
    if n <= 1 {
        return true
    }
    inversions := 0
    for i := 0; i < n; i++ {
        next := (i + 1) % n
        if nums[i] > nums[next] {
            inversions++
            if inversions > 1 {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def check(nums)
  n = nums.length
  inversions = 0
  (0...n-1).each do |i|
    inversions += 1 if nums[i] > nums[i + 1]
  end
  inversions += 1 if nums[-1] > nums[0]
  inversions <= 1
end
```

## Scala

```scala
object Solution {
    def check(nums: Array[Int]): Boolean = {
        val n = nums.length
        var drops = 0
        for (i <- 0 until n) {
            if (nums(i) > nums((i + 1) % n)) {
                drops += 1
                if (drops > 1) return false
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n <= 1 {
            return true;
        }
        let mut inversions = 0;
        for i in 1..n {
            if nums[i - 1] > nums[i] {
                inversions += 1;
            }
        }
        if nums[n - 1] > nums[0] {
            inversions += 1;
        }
        inversions <= 1
    }
}
```

## Racket

```racket
(define/contract (check nums)
  (-> (listof exact-integer?) boolean?)
  (let ((n (length nums)))
    (if (<= n 1)
        #t
        (let loop ((prev (car nums))
                   (rest (cdr nums))
                   (cnt 0)
                   (first (car nums))
                   (last prev))
          (if (null? rest)
              (let ((total (+ cnt (if (> last first) 1 0))))
                (<= total 1))
              (let* ((curr (car rest))
                     (new-cnt (if (> prev curr) (+ cnt 1) cnt)))
                (loop curr (cdr rest) new-cnt first curr)))))))
```

## Erlang

```erlang
-module(solution).
-export([check/1]).

-spec check(Nums :: [integer()]) -> boolean().
check([]) ->
    true;
check([_]) ->
    true;
check(Nums) ->
    First = hd(Nums),
    {Count, Last} = count_inversions(tl(Nums), First, 0),
    Total = if
        Last > First -> Count + 1;
        true -> Count
    end,
    Total =< 1.

count_inversions([], Prev, Acc) ->
    {Acc, Prev};
count_inversions([H|T], Prev, Acc) ->
    NewAcc = if Prev > H -> Acc + 1; true -> Acc end,
    count_inversions(T, H, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec check(nums :: [integer]) :: boolean
  def check(nums) do
    n = length(nums)

    cond do
      n <= 1 ->
        true

      true ->
        first = hd(nums)

        {inv, last} =
          Enum.reduce(tl(nums), {0, first}, fn val, {cnt, prev} ->
            if prev > val do
              {cnt + 1, val}
            else
              {cnt, val}
            end
          end)

        inv_total = inv + (if last > first, do: 1, else: 0)
        inv_total <= 1
    end
  end
end
```
