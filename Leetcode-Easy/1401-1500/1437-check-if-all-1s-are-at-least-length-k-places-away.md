# 1437. Check If All 1's Are at Least Length K Places Away

## Cpp

```cpp
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int last = -k - 1; // ensures first 1 passes the check
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) {
                if (i - last - 1 < k) return false;
                last = i;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int lastOne = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (lastOne != -1 && i - lastOne - 1 < k) {
                    return false;
                }
                lastOne = i;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_one = -1  # position of previous 1; -1 indicates none seen yet
        for i, val in enumerate(nums):
            if val == 1:
                if last_one != -1 and i - last_one <= k:
                    return False
                last_one = i
        return True
```

## Python3

```python
from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one = -k - 1  # ensures first 1 passes check
        for i, val in enumerate(nums):
            if val == 1:
                if i - last_one - 1 < k:
                    return False
                last_one = i
        return True
```

## C

```c
#include <stdbool.h>

bool kLengthApart(int* nums, int numsSize, int k) {
    int last = -k - 1; // position before start ensures first 1 passes
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (i - last - 1 < k) {
                return false;
            }
            last = i;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int lastOne = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (lastOne != -1 && i - lastOne - 1 < k) {
                    return false;
                }
                lastOne = i;
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
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let lastOne = -k - 1; // position far enough left of start
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (i - lastOne - 1 < k) return false;
            lastOne = i;
        }
    }
    return true;
};
```

## Typescript

```typescript
function kLengthApart(nums: number[], k: number): boolean {
    let lastOne = -k - 1; // ensures first 1 always passes
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (i - lastOne <= k) return false;
            lastOne = i;
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
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $prev = -$k - 1;
        foreach ($nums as $i => $val) {
            if ($val == 1) {
                if ($i - $prev - 1 < $k) {
                    return false;
                }
                $prev = $i;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var prev = -k - 1
        for (i, val) in nums.enumerated() {
            if val == 1 {
                if i - prev <= k { return false }
                prev = i
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var prev = -k - 1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (i - prev - 1 < k) return false
                prev = i
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    int prev = -(k + 1);
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        if (i - prev - 1 < k) return false;
        prev = i;
      }
    }
    return true;
  }
}
```

## Golang

```go
func kLengthApart(nums []int, k int) bool {
    last := -k - 1 // ensures first 1 always passes
    for i, v := range nums {
        if v == 1 {
            if i-last-1 < k {
                return false
            }
            last = i
        }
    }
    return true
}
```

## Ruby

```ruby
def k_length_apart(nums, k)
  prev = -(k + 1)
  nums.each_with_index do |val, idx|
    if val == 1
      return false if idx - prev <= k
      prev = idx
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var last = -k - 1
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                if (i - last <= k) return false
                last = i
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut last_one: Option<usize> = None;
        for (i, &v) in nums.iter().enumerate() {
            if v == 1 {
                if let Some(prev) = last_one {
                    // distance between indices must be greater than k
                    if (i - prev) as i32 <= k {
                        return false;
                    }
                }
                last_one = Some(i);
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (k-length-apart nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let loop ((lst nums) (i 0) (last (- (+ k 1)))) ; last initialized to -(k+1)
    (cond
      [(null? lst) #t]
      [else
       (define val (car lst))
       (if (= val 1)
           (if (and (>= last 0) (<= (- i last) k))
               #f
               (loop (cdr lst) (+ i 1) i))
           (loop (cdr lst) (+ i 1) last))])))
```

## Erlang

```erlang
-spec k_length_apart(Nums :: [integer()], K :: integer()) -> boolean().
k_length_apart(Nums, K) ->
    k_length_apart(Nums, K, 0, none).

k_length_apart([], _K, _Idx, _Last) ->
    true;
k_length_apart([H|T], K, Idx, Last) when H =:= 1 ->
    case Last of
        none ->
            k_length_apart(T, K, Idx + 1, Idx);
        L when (Idx - L - 1) < K ->
            false;
        _ ->
            k_length_apart(T, K, Idx + 1, Idx)
    end;
k_length_apart([_|T], K, Idx, Last) ->
    k_length_apart(T, K, Idx + 1, Last).
```

## Elixir

```elixir
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    result =
      Enum.reduce_while(Enum.with_index(nums), -1, fn {val, idx}, last_one ->
        if val == 1 do
          if last_one != -1 and idx - last_one - 1 < k do
            {:halt, false}
          else
            {:cont, idx}
          end
        else
          {:cont, last_one}
        end
      end)

    result != false
  end
end
```
