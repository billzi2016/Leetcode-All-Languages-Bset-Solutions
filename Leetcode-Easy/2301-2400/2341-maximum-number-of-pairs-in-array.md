# 2341. Maximum Number of Pairs in Array

## Cpp

```cpp
class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        int cnt[101] = {0};
        for (int x : nums) ++cnt[x];
        int pairs = 0, leftovers = 0;
        for (int f : cnt) {
            pairs += f / 2;
            leftovers += f % 2;
        }
        return {pairs, leftovers};
    }
};
```

## Java

```java
class Solution {
    public int[] numberOfPairs(int[] nums) {
        int[] cnt = new int[101];
        for (int num : nums) {
            cnt[num]++;
        }
        int pairs = 0;
        for (int c : cnt) {
            pairs += c / 2;
        }
        int leftover = nums.length - pairs * 2;
        return new int[]{pairs, leftover};
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        pairs = 0
        leftovers = 0
        for cnt in freq.values():
            pairs += cnt // 2
            leftovers += cnt % 2
        return [pairs, leftovers]
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pairs = sum(v // 2 for v in freq.values())
        leftovers = sum(v % 2 for v in freq.values())
        return [pairs, leftovers]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfPairs(int* nums, int numsSize, int* returnSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]]++;
    }
    
    int pairs = 0, leftovers = 0;
    for (int i = 0; i <= 100; ++i) {
        pairs += freq[i] / 2;
        leftovers += freq[i] % 2;
    }
    
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = pairs;
    result[1] = leftovers;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] NumberOfPairs(int[] nums) {
        int[] freq = new int[101];
        foreach (int num in nums) {
            freq[num]++;
        }
        int pairs = 0;
        int leftover = 0;
        foreach (int count in freq) {
            pairs += count / 2;
            leftover += count % 2;
        }
        return new int[] { pairs, leftover };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    const freq = new Map();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    let pairs = 0;
    for (const count of freq.values()) {
        pairs += Math.floor(count / 2);
    }
    const leftovers = nums.length - pairs * 2;
    return [pairs, leftovers];
};
```

## Typescript

```typescript
function numberOfPairs(nums: number[]): number[] {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    let pairs = 0;
    for (const count of freq.values()) {
        pairs += Math.floor(count / 2);
    }
    const leftovers = nums.length - pairs * 2;
    return [pairs, leftovers];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function numberOfPairs($nums) {
        $freq = array_count_values($nums);
        $pairs = 0;
        foreach ($freq as $count) {
            $pairs += intdiv($count, 2);
        }
        $leftover = count($nums) - $pairs * 2;
        return [$pairs, $leftover];
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ nums: [Int]) -> [Int] {
        var freq = [Int: Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        var pairs = 0
        for count in freq.values {
            pairs += count / 2
        }
        let leftover = nums.count - pairs * 2
        return [pairs, leftover]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums: IntArray): IntArray {
        val freq = IntArray(101)
        for (num in nums) {
            freq[num]++
        }
        var pairs = 0
        var leftover = 0
        for (c in freq) {
            pairs += c / 2
            leftover += c % 2
        }
        return intArrayOf(pairs, leftover)
    }
}
```

## Dart

```dart
class Solution {
  List<int> numberOfPairs(List<int> nums) {
    final freq = <int, int>{};
    for (var num in nums) {
      freq[num] = (freq[num] ?? 0) + 1;
    }
    int pairs = 0;
    for (var count in freq.values) {
      pairs += count ~/ 2;
    }
    int leftovers = nums.length - pairs * 2;
    return [pairs, leftovers];
  }
}
```

## Golang

```go
func numberOfPairs(nums []int) []int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }
    pairs, leftovers := 0, 0
    for _, cnt := range freq {
        pairs += cnt / 2
        leftovers += cnt % 2
    }
    return []int{pairs, leftovers}
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def number_of_pairs(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  pairs = 0
  leftovers = 0
  freq.each_value do |count|
    pairs += count / 2
    leftovers += count % 2
  end
  [pairs, leftovers]
end
```

## Scala

```scala
object Solution {
    def numberOfPairs(nums: Array[Int]): Array[Int] = {
        val freq = new Array[Int](101)
        for (v <- nums) {
            freq(v) += 1
        }
        var pairs = 0
        var leftovers = 0
        for (cnt <- freq) {
            pairs += cnt / 2
            leftovers += cnt % 2
        }
        Array(pairs, leftovers)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums: Vec<i32>) -> Vec<i32> {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &num in nums.iter() {
            *freq.entry(num).or_insert(0) += 1;
        }
        let mut pairs = 0;
        let mut leftover = 0;
        for &count in freq.values() {
            pairs += count / 2;
            leftover += count % 2;
        }
        vec![pairs, leftover]
    }
}
```

## Racket

```racket
(define/contract (number-of-pairs nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ((freq (make-hash)))
    (for-each (lambda (x) (hash-update! freq x add1 0)) nums)
    (define pair-count 0)
    (define leftover 0)
    (hash-for-each freq
      (lambda (_ v)
        (set! pair-count (+ pair-count (quotient v 2)))
        (set! leftover   (+ leftover   (remainder v 2)))))
    (list pair-count leftover)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_pairs/1]).

-spec number_of_pairs(Nums :: [integer()]) -> [integer()].
number_of_pairs(Nums) ->
    FreqMap = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    {Pairs, Leftover} = maps:fold(
        fun(_Key, Count, {P, L}) ->
            {P + Count div 2, L + Count rem 2}
        end,
        {0, 0},
        FreqMap
    ),
    [Pairs, Leftover].
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums :: [integer]) :: [integer]
  def number_of_pairs(nums) do
    freqs = Enum.reduce(nums, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)

    {pairs, leftovers} =
      Enum.reduce(freqs, {0, 0}, fn {_val, count}, {p, l} ->
        {p + div(count, 2), l + rem(count, 2)}
      end)

    [pairs, leftovers]
  end
end
```
