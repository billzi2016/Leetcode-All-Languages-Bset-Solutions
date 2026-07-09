# 1018. Binary Prefix Divisible By 5

## Cpp

```cpp
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> ans;
        ans.reserve(nums.size());
        int cur = 0;
        for (int bit : nums) {
            cur = ((cur << 1) + bit) % 5;
            ans.push_back(cur == 0);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Boolean> prefixesDivBy5(int[] nums) {
        java.util.List<Boolean> result = new java.util.ArrayList<>(nums.length);
        int mod = 0;
        for (int bit : nums) {
            mod = ((mod << 1) + bit) % 5;
            result.add(mod == 0);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = []
        cur = 0
        for bit in nums:
            cur = (cur * 2 + bit) % 5
            res.append(cur == 0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for bit in nums:
            cur = (cur * 2 + bit) % 5
            res.append(cur == 0)
        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    bool* ans = (bool*)malloc(numsSize * sizeof(bool));
    int cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        cur = ((cur << 1) + nums[i]) % 5;
        ans[i] = (cur == 0);
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        var result = new List<bool>(nums.Length);
        int mod = 0;
        foreach (int bit in nums) {
            mod = ((mod << 1) + bit) % 5;
            result.Add(mod == 0);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    const result = new Array(nums.length);
    let mod = 0;
    for (let i = 0; i < nums.length; i++) {
        mod = ((mod << 1) + nums[i]) % 5;
        result[i] = mod === 0;
    }
    return result;
};
```

## Typescript

```typescript
function prefixesDivBy5(nums: number[]): boolean[] {
    const result: boolean[] = new Array(nums.length);
    let remainder = 0;
    for (let i = 0; i < nums.length; i++) {
        remainder = ((remainder << 1) + nums[i]) % 5;
        result[i] = remainder === 0;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean[]
     */
    function prefixesDivBy5($nums) {
        $result = [];
        $mod = 0;
        foreach ($nums as $bit) {
            $mod = ($mod * 2 + $bit) % 5;
            $result[] = $mod === 0;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        var result = [Bool]()
        result.reserveCapacity(nums.count)
        var current = 0
        for bit in nums {
            current = (current * 2 + bit) % 5
            result.append(current == 0)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun prefixesDivBy5(nums: IntArray): List<Boolean> {
        val result = ArrayList<Boolean>(nums.size)
        var current = 0
        for (bit in nums) {
            current = ((current shl 1) + bit) % 5
            result.add(current == 0)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> prefixesDivBy5(List<int> nums) {
    List<bool> answer = [];
    int mod = 0;
    for (int bit in nums) {
      mod = ((mod << 1) + bit) % 5;
      answer.add(mod == 0);
    }
    return answer;
  }
}
```

## Golang

```go
func prefixesDivBy5(nums []int) []bool {
    result := make([]bool, len(nums))
    mod := 0
    for i, bit := range nums {
        mod = ((mod << 1) + bit) % 5
        if mod == 0 {
            result[i] = true
        }
    }
    return result
}
```

## Ruby

```ruby
def prefixes_div_by5(nums)
  result = []
  cur = 0
  nums.each do |bit|
    cur = ((cur << 1) + bit) % 5
    result << (cur == 0)
  end
  result
end
```

## Scala

```scala
object Solution {
    def prefixesDivBy5(nums: Array[Int]): List[Boolean] = {
        var mod = 0
        val res = scala.collection.mutable.ListBuffer.empty[Boolean]
        for (bit <- nums) {
            mod = ((mod << 1) + bit) % 5
            res += (mod == 0)
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut result = Vec::with_capacity(nums.len());
        let mut rem: i32 = 0;
        for &bit in nums.iter() {
            rem = (rem * 2 + bit) % 5;
            result.push(rem == 0);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (prefixes-div-by5 nums)
  (-> (listof exact-integer?) (listof boolean?))
  (let loop ((lst nums) (mod 0) (acc '()))
    (if (null? lst)
        (reverse acc)
        (let* ((b (car lst))
               (new-mod (modulo (+ (* mod 2) b) 5))
               (new-acc (cons (= new-mod 0) acc)))
          (loop (cdr lst) new-mod new-acc)))))
```

## Erlang

```erlang
-module(solution).
-export([prefixes_div_by5/1]).

-spec prefixes_div_by5(Nums :: [integer()]) -> [boolean()].
prefixes_div_by5(Nums) ->
    prefixes_div_by5(Nums, 0, []).

prefixes_div_by5([], _Rem, Acc) ->
    lists:reverse(Acc);
prefixes_div_by5([Bit|Rest], Rem, Acc) ->
    NewRem = (Rem * 2 + Bit) rem 5,
    Bool = (NewRem == 0),
    prefixes_div_by5(Rest, NewRem, [Bool | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec prefixes_div_by5(nums :: [integer]) :: [boolean]
  def prefixes_div_by5(nums) do
    {_last_rem, rev} =
      Enum.reduce(nums, {0, []}, fn bit, {rem, acc} ->
        new_rem = :erlang.rem(rem * 2 + bit, 5)
        {new_rem, [new_rem == 0 | acc]}
      end)

    Enum.reverse(rev)
  end
end
```
