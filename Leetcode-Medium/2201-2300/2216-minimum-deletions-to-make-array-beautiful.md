# 2216. Minimum Deletions to Make Array Beautiful

## Cpp

```cpp
class Solution {
public:
    int minDeletion(vector<int>& nums) {
        int deletions = 0;
        vector<int> kept;
        for (int x : nums) {
            if (kept.size() % 2 == 0) {
                // start of a new pair
                kept.push_back(x);
            } else {
                // need a different element from the previous one
                if (kept.back() == x) {
                    ++deletions; // delete current element
                } else {
                    kept.push_back(x);
                }
            }
        }
        if (kept.size() % 2 == 1) {
            ++deletions; // make length even by deleting last element
        }
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minDeletion(int[] nums) {
        int deletions = 0;
        int length = 0; // length of the constructed beautiful array
        int first = -1; // holds the element at an odd index (first of a pair)
        for (int num : nums) {
            if ((length & 1) == 0) { // need to start a new pair
                first = num;
                length++;
            } else { // we have one element waiting for a partner
                if (num == first) {
                    deletions++; // skip this element
                } else {
                    length++;
                }
            }
        }
        if ((length & 1) == 1) {
            deletions++; // make the final length even
        }
        return deletions;
    }
}
```

## Python

```python
class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        deletions = 0
        kept_len = 0
        last = None  # value of the most recently kept element
        
        for x in nums:
            if kept_len % 2 == 0:
                # start a new pair
                last = x
                kept_len += 1
            else:
                # need a different element to complete the pair
                if x != last:
                    last = x
                    kept_len += 1
                else:
                    deletions += 1
        
        # If we ended with an odd length, remove the last element
        if kept_len % 2 == 1:
            deletions += 1
        
        return deletions
```

## Python3

```python
from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        kept = []
        for x in nums:
            if len(kept) % 2 == 0:
                kept.append(x)
            else:
                if kept[-1] != x:
                    kept.append(x)
        if len(kept) % 2 == 1:
            kept.pop()
        return len(nums) - len(kept)
```

## C

```c
int minDeletion(int* nums, int numsSize) {
    int deletions = 0;
    int curLen = 0;
    int last = -1; // stores the first element of the current pair
    for (int i = 0; i < numsSize; ++i) {
        if (curLen % 2 == 0) {
            // start a new pair with this element
            last = nums[i];
            ++curLen;
        } else {
            // need an element different from 'last' to complete the pair
            if (nums[i] == last) {
                ++deletions; // delete current element
            } else {
                ++curLen; // keep it as second of the pair
            }
        }
    }
    // If we ended with a dangling first element, remove it
    if (curLen % 2 == 1) {
        ++deletions;
    }
    return deletions;
}
```

## Csharp

```csharp
public class Solution {
    public int MinDeletion(int[] nums) {
        var keep = new System.Collections.Generic.List<int>();
        foreach (int x in nums) {
            if (keep.Count % 2 == 0) {
                keep.Add(x);
            } else {
                if (keep[keep.Count - 1] != x) {
                    keep.Add(x);
                }
            }
        }
        if (keep.Count % 2 == 1) {
            keep.RemoveAt(keep.Count - 1);
        }
        return nums.Length - keep.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minDeletion = function(nums) {
    let deletions = 0;
    const res = [];
    for (const x of nums) {
        if (res.length % 2 === 0) {
            // start a new pair
            res.push(x);
        } else {
            // need to ensure the current element differs from the previous one in the pair
            if (res[res.length - 1] !== x) {
                res.push(x);
            } else {
                deletions++;
            }
        }
    }
    // If we end up with an odd length, remove the last element
    if (res.length % 2 === 1) {
        deletions++;
    }
    return deletions;
};
```

## Typescript

```typescript
function minDeletion(nums: number[]): number {
    const originalLength = nums.length;
    const kept: number[] = [];
    for (const x of nums) {
        if (kept.length % 2 === 1 && kept[kept.length - 1] === x) {
            continue; // delete this element
        }
        kept.push(x);
    }
    if (kept.length % 2 === 1) {
        kept.pop(); // make length even
    }
    return originalLength - kept.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDeletion($nums) {
        $deletions = 0;
        $resLen = 0;
        $first = null;
        foreach ($nums as $num) {
            if ($resLen % 2 == 1 && $first === $num) {
                $deletions++;
                continue;
            }
            $first = $num;
            $resLen++;
        }
        if ($resLen % 2 == 1) {
            $deletions++;
        }
        return $deletions;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletion(_ nums: [Int]) -> Int {
        var kept = 0
        var prev = -1
        for num in nums {
            if kept % 2 == 0 {
                // start of a new pair
                prev = num
                kept += 1
            } else {
                // need a different element from the previous one
                if num != prev {
                    kept += 1
                }
                // else skip (delete) this element
            }
        }
        if kept % 2 == 1 {
            kept -= 1
        }
        return nums.count - kept
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletion(nums: IntArray): Int {
        var deletions = 0
        var kept = 0
        var prev = -1
        for (x in nums) {
            if (kept % 2 == 0) {
                prev = x
                kept++
            } else {
                if (x != prev) {
                    kept++
                } else {
                    deletions++
                }
            }
        }
        if (kept % 2 == 1) deletions++
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minDeletion(List<int> nums) {
    int deletions = 0;
    bool expectFirst = true; // true means we are at even index of the resulting array
    int prev = -1;

    for (int x in nums) {
      if (expectFirst) {
        // take this element as the first of a pair
        prev = x;
        expectFirst = false;
      } else {
        // need a second element different from prev
        if (x == prev) {
          deletions++;
          // keep waiting for a suitable second element
        } else {
          // pair completed
          expectFirst = true;
        }
      }
    }

    // If we end with an unmatched first element, delete it
    if (!expectFirst) {
      deletions++;
    }

    return deletions;
  }
}
```

## Golang

```go
func minDeletion(nums []int) int {
    deletions := 0
    resLen := 0
    var prev int
    for _, v := range nums {
        if resLen%2 == 0 {
            prev = v
            resLen++
        } else {
            if v == prev {
                deletions++
            } else {
                resLen++
            }
        }
    }
    if resLen%2 == 1 {
        deletions++
    }
    return deletions
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_deletion(nums)
  res = []
  nums.each do |x|
    if res.size.odd?
      next if res[-1] == x
    end
    res << x
  end
  res.pop if res.size.odd?
  nums.length - res.length
end
```

## Scala

```scala
object Solution {
    def minDeletion(nums: Array[Int]): Int = {
        var deletions = 0
        var keptLen = 0
        var prev = 0
        for (num <- nums) {
            if (keptLen % 2 == 0) {
                prev = num
                keptLen += 1
            } else {
                if (num == prev) {
                    deletions += 1
                } else {
                    prev = num
                    keptLen += 1
                }
            }
        }
        if (keptLen % 2 == 1) deletions + 1 else deletions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletion(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut kept_len = 0usize;
        let mut last_even = 0i32;
        for &x in nums.iter() {
            if kept_len % 2 == 0 {
                // even position in the resulting array, always keep
                last_even = x;
                kept_len += 1;
            } else {
                // odd position: must differ from previous (even) element
                if x != last_even {
                    kept_len += 1;
                }
                // otherwise skip this element
            }
        }
        if kept_len % 2 == 1 {
            kept_len -= 1; // delete the last unpaired element
        }
        (n - kept_len) as i32
    }
}
```

## Racket

```racket
(define/contract (min-deletion nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (len
          (let loop ((lst nums) (res '()) (len 0))
            (if (null? lst)
                len
                (let ((x (car lst)))
                  (if (odd? len)
                      (if (equal? x (car res))
                          (loop (cdr lst) res len)               ; skip duplicate in pair
                          (loop (cdr lst) (cons x res) (+ len 1))) ; add as second of pair
                      (loop (cdr lst) (cons x res) (+ len 1))))))))
    (let ((final-len (if (odd? len) (- len 1) len)))
      (- n final-len))))
```

## Erlang

```erlang
-spec min_deletion([integer()]) -> integer().
min_deletion(Nums) ->
    N = length(Nums),
    {_, KeepLen} = lists:foldl(
        fun(Num, {ResRev, Len}) ->
            case Len rem 2 of
                0 ->
                    {[Num | ResRev], Len + 1};
                1 ->
                    Prev = hd(ResRev),
                    if Num == Prev ->
                        {ResRev, Len};
                       true ->
                        {[Num | ResRev], Len + 1}
                    end
            end
        end,
        {[], 0},
        Nums
    ),
    FinalLen = case KeepLen rem 2 of
        0 -> KeepLen;
        1 -> KeepLen - 1
    end,
    N - FinalLen.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletion(nums :: [integer]) :: integer
  def min_deletion(nums) do
    {len, del, _} =
      Enum.reduce(nums, {0, 0, nil}, fn x, {len, del, prev} ->
        if rem(len, 2) == 0 do
          {len + 1, del, x}
        else
          if x != prev do
            {len + 1, del, x}
          else
            {len, del + 1, prev}
          end
        end
      end)

    del + rem(len, 2)
  end
end
```
