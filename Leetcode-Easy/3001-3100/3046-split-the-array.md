# 3046. Split the Array

## Cpp

```cpp
class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        int cnt[101] = {0};
        for (int x : nums) {
            if (++cnt[x] > 2) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        int[] freq = new int[101];
        for (int num : nums) {
            if (++freq[num] > 2) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq = Counter(nums)
        for v in freq.values():
            if v > 2:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        half = n // 2
        freq = {}
        for x in nums:
            cnt = freq.get(x, 0) + 1
            if cnt > 2:
                return False
            freq[x] = cnt
        distinct = len(freq)
        return distinct >= half
```

## C

```c
#include <stdbool.h>

bool isPossibleToSplit(int* nums, int numsSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (++freq[v] > 2) {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPossibleToSplit(int[] nums) {
        int n = nums.Length;
        int half = n / 2;
        int[] freq = new int[101];
        foreach (int num in nums) {
            if (++freq[num] > 2) return false;
        }
        int distinct = 0;
        for (int i = 1; i <= 100; i++) {
            if (freq[i] > 0) distinct++;
        }
        return distinct >= half;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossibleToSplit = function(nums) {
    const freq = new Array(101).fill(0);
    for (const v of nums) {
        freq[v]++;
        if (freq[v] > 2) return false;
    }
    let distinct = 0;
    for (let i = 1; i <= 100; i++) {
        if (freq[i] > 0) distinct++;
    }
    return distinct >= nums.length / 2;
};
```

## Typescript

```typescript
function isPossibleToSplit(nums: number[]): boolean {
    const freq = new Array(101).fill(0);
    for (const num of nums) {
        freq[num]++;
        if (freq[num] > 2) return false;
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
    function isPossibleToSplit($nums) {
        $freq = [];
        foreach ($nums as $v) {
            if (!isset($freq[$v])) {
                $freq[$v] = 0;
            }
            $freq[$v]++;
            if ($freq[$v] > 2) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isPossibleToSplit(_ nums: [Int]) -> Bool {
        var freq = [Int:Int]()
        for v in nums {
            freq[v, default: 0] += 1
            if let count = freq[v], count > 2 {
                return false
            }
        }
        return freq.count >= nums.count / 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossibleToSplit(nums: IntArray): Boolean {
        val freq = IntArray(101)
        for (v in nums) {
            freq[v]++
            if (freq[v] > 2) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isPossibleToSplit(List<int> nums) {
    List<int> freq = List.filled(101, 0);
    for (int x in nums) {
      if (++freq[x] > 2) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isPossibleToSplit(nums []int) bool {
    freq := make(map[int]int, len(nums))
    for _, v := range nums {
        freq[v]++
        if freq[v] > 2 {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def is_possible_to_split(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  return false if freq.values.any? { |c| c > 2 }
  distinct_count = freq.size
  distinct_count >= nums.length / 2
end
```

## Scala

```scala
object Solution {
    def isPossibleToSplit(nums: Array[Int]): Boolean = {
        val freq = new Array[Int](101)
        for (v <- nums) {
            freq(v) += 1
            if (freq(v) > 2) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_possible_to_split(nums: Vec<i32>) -> bool {
        let mut freq = [0u8; 101];
        for &v in &nums {
            let idx = v as usize;
            freq[idx] += 1;
            if freq[idx] > 2 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-possible-to-split nums)
  (-> (listof exact-integer?) boolean?)
  (let ([freq (make-hash)])
    (for ([x nums])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (not (for/or ([cnt (in-hash-values freq)]) (> cnt 2)))))
```

## Erlang

```erlang
-module(solution).
-export([is_possible_to_split/1]).

-spec is_possible_to_split(Nums :: [integer()]) -> boolean().
is_possible_to_split(Nums) ->
    Freq = count_freq(Nums, #{}),
    case maps:fold(fun(_K, V, Acc) -> Acc orelse V > 2 end, false, Freq) of
        true -> false;
        false -> true
    end.

count_freq([], Acc) -> Acc;
count_freq([H|T], Acc) ->
    NewAcc = maps:update_with(H,
                               fun(C) -> C + 1 end,
                               1,
                               Acc),
    count_freq(T, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible_to_split(nums :: [integer]) :: boolean
  def is_possible_to_split(nums) do
    nums
    |> Enum.reduce(%{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)
    |> Enum.any?(fn {_k, v} -> v > 2 end)
    |> Kernel.not()
  end
end
```
