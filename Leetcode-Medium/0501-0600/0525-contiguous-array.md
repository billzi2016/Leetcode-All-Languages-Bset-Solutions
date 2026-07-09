# 0525. Contiguous Array

## Cpp

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> first;
        first.reserve(nums.size() * 2);
        first[0] = -1;
        int count = 0, maxLen = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            count += nums[i] == 1 ? 1 : -1;
            auto it = first.find(count);
            if (it != first.end()) {
                maxLen = max(maxLen, i - it->second);
            } else {
                first[count] = i;
            }
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int findMaxLength(int[] nums) {
        java.util.HashMap<Integer, Integer> firstIndex = new java.util.HashMap<>();
        firstIndex.put(0, -1);
        int maxLen = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            count += (nums[i] == 1) ? 1 : -1;
            if (firstIndex.containsKey(count)) {
                int len = i - firstIndex.get(count);
                if (len > maxLen) {
                    maxLen = len;
                }
            } else {
                firstIndex.put(count, i);
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_index = {0: -1}
        count = 0
        max_len = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in first_index:
                max_len = max(max_len, i - first_index[count])
            else:
                first_index[count] = i
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_to_index = {0: -1}
        max_len = 0
        count = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_to_index:
                max_len = max(max_len, i - count_to_index[count])
            else:
                count_to_index[count] = i
        return max_len
```

## C

```c
int findMaxLength(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int offset = numsSize; // to shift count range [-n, n] to [0, 2n]
    int mapSize = 2 * numsSize + 1;
    int *firstSeen = (int *)malloc(mapSize * sizeof(int));
    if (!firstSeen) return 0; // allocation failure fallback
    for (int i = 0; i < mapSize; ++i) {
        firstSeen[i] = -2; // sentinel for unseen
    }
    int maxLen = 0;
    int count = 0;
    firstSeen[offset] = -1; // count 0 seen at index -1
    
    for (int i = 0; i < numsSize; ++i) {
        count += (nums[i] == 1) ? 1 : -1;
        int idx = count + offset;
        if (firstSeen[idx] != -2) {
            int len = i - firstSeen[idx];
            if (len > maxLen) maxLen = len;
        } else {
            firstSeen[idx] = i;
        }
    }
    
    free(firstSeen);
    return maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMaxLength(int[] nums) {
        var firstIndex = new Dictionary<int, int>();
        firstIndex[0] = -1; // count zero at position before start
        int maxLen = 0;
        int count = 0;
        for (int i = 0; i < nums.Length; i++) {
            count += nums[i] == 1 ? 1 : -1;
            if (firstIndex.TryGetValue(count, out int prevIdx)) {
                int len = i - prevIdx;
                if (len > maxLen) maxLen = len;
            } else {
                firstIndex[count] = i;
            }
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {
    const firstSeen = new Map();
    // sum 0 is seen at index -1 (before array starts)
    firstSeen.set(0, -1);
    let maxLen = 0;
    let count = 0; // treat 1 as +1, 0 as -1
    
    for (let i = 0; i < nums.length; i++) {
        count += nums[i] === 1 ? 1 : -1;
        if (firstSeen.has(count)) {
            const prevIdx = firstSeen.get(count);
            const len = i - prevIdx;
            if (len > maxLen) maxLen = len;
        } else {
            firstSeen.set(count, i);
        }
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function findMaxLength(nums: number[]): number {
    const firstIndex = new Map<number, number>();
    firstIndex.set(0, -1);
    let maxLen = 0;
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i] === 1 ? 1 : -1;
        if (firstIndex.has(count)) {
            const prev = firstIndex.get(count)!;
            const len = i - prev;
            if (len > maxLen) maxLen = len;
        } else {
            firstIndex.set(count, i);
        }
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxLength($nums) {
        $map = [0 => -1];
        $count = 0;
        $maxLen = 0;
        foreach ($nums as $i => $num) {
            $count += ($num == 1) ? 1 : -1;
            if (isset($map[$count])) {
                $len = $i - $map[$count];
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            } else {
                $map[$count] = $i;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func findMaxLength(_ nums: [Int]) -> Int {
        var firstSeen = [Int: Int]()
        firstSeen[0] = -1
        var count = 0
        var maxLen = 0
        
        for (i, num) in nums.enumerated() {
            count += (num == 1) ? 1 : -1
            if let prevIndex = firstSeen[count] {
                let length = i - prevIndex
                if length > maxLen { maxLen = length }
            } else {
                firstSeen[count] = i
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaxLength(nums: IntArray): Int {
        val firstIdx = HashMap<Int, Int>()
        var count = 0
        var maxLen = 0
        firstIdx[0] = -1
        for (i in nums.indices) {
            count += if (nums[i] == 1) 1 else -1
            val prev = firstIdx[count]
            if (prev != null) {
                val len = i - prev
                if (len > maxLen) maxLen = len
            } else {
                firstIdx[count] = i
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int findMaxLength(List<int> nums) {
    final Map<int, int> firstIndex = {0: -1};
    int count = 0;
    int maxLen = 0;

    for (int i = 0; i < nums.length; i++) {
      count += nums[i] == 1 ? 1 : -1;
      if (firstIndex.containsKey(count)) {
        final len = i - firstIndex[count]!;
        if (len > maxLen) maxLen = len;
      } else {
        firstIndex[count] = i;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func findMaxLength(nums []int) int {
    firstIdx := make(map[int]int)
    firstIdx[0] = -1
    count, maxLen := 0, 0
    for i, v := range nums {
        if v == 1 {
            count++
        } else {
            count--
        }
        if idx, ok := firstIdx[count]; ok {
            if length := i - idx; length > maxLen {
                maxLen = length
            }
        } else {
            firstIdx[count] = i
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def find_max_length(nums)
  count_to_index = {0 => -1}
  max_len = 0
  count = 0

  nums.each_with_index do |num, i|
    count += (num == 1 ? 1 : -1)

    if count_to_index.key?(count)
      length = i - count_to_index[count]
      max_len = length if length > max_len
    else
      count_to_index[count] = i
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def findMaxLength(nums: Array[Int]): Int = {
        import scala.collection.mutable

        val firstIndex = mutable.Map[Int, Int]()
        var count = 0
        var maxLen = 0
        firstIndex(0) = -1

        for (i <- nums.indices) {
            if (nums(i) == 1) count += 1 else count -= 1
            firstIndex.get(count) match {
                case Some(prevIdx) =>
                    val len = i - prevIdx
                    if (len > maxLen) maxLen = len
                case None =>
                    firstIndex(count) = i
            }
        }

        maxLen
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let mut first_occurrence: HashMap<i32, usize> = HashMap::new();
        let mut count: i32 = 0;
        let mut max_len: usize = 0;

        for (i, &num) in nums.iter().enumerate() {
            if num == 1 {
                count += 1;
            } else {
                count -= 1;
            }

            if count == 0 {
                max_len = i + 1;
            } else if let Some(&prev_idx) = first_occurrence.get(&count) {
                let len = i - prev_idx;
                if len > max_len {
                    max_len = len;
                }
            } else {
                first_occurrence.insert(count, i);
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (find-max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((first-index-hash (make-hash)))
    ;; map count -> earliest index where this count occurs
    (hash-set! first-index-hash 0 -1) ; count 0 before start at index -1
    (let loop ((i 0)
               (cnt 0)
               (maxlen 0)
               (rest nums))
      (if (null? rest)
          maxlen
          (let* ((val (car rest))
                 (new-cnt (+ cnt (if (= val 1) 1 -1)))
                 (existing (hash-ref first-index-hash new-cnt #f)))
            (when (not existing)
              (hash-set! first-index-hash new-cnt i))
            (define earliest (hash-ref first-index-hash new-cnt))
            (define curlen (- i earliest))
            (loop (+ i 1) new-cnt (max maxlen curlen) (cdr rest)))))))
```

## Erlang

```erlang
-spec find_max_length(Nums :: [integer()]) -> integer().
find_max_length(Nums) ->
    loop(Nums, 0, 0, #{0 => -1}, 0).

loop([], _Idx, _Count, _Map, Max) ->
    Max;
loop([H|T], Idx, Count, Map, Max) ->
    NewCount = case H of
        1 -> Count + 1;
        0 -> Count - 1
    end,
    case maps:find(NewCount, Map) of
        {ok, FirstIdx} ->
            Len = Idx - FirstIdx,
            NewMax = if Len > Max -> Len; true -> Max end,
            loop(T, Idx + 1, NewCount, Map, NewMax);
        error ->
            NewMap = maps:put(NewCount, Idx, Map),
            loop(T, Idx + 1, NewCount, NewMap, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_max_length(nums :: [integer]) :: integer
  def find_max_length(nums) do
    {_count, _map, max_len} =
      Enum.with_index(nums)
      |> Enum.reduce({0, %{0 => -1}, 0}, fn {num, idx}, {cnt, map, max_len} ->
        cnt = cnt + if num == 1, do: 1, else: -1

        case Map.fetch(map, cnt) do
          {:ok, first_idx} ->
            len = idx - first_idx
            new_max = if len > max_len, do: len, else: max_len
            {cnt, map, new_max}

          :error ->
            {cnt, Map.put(map, cnt, idx), max_len}
        end
      end)

    max_len
  end
end
```
