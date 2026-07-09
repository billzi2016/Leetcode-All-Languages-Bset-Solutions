# 0565. Array Nesting

## Cpp

```cpp
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        int best = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == -1) continue;
            int cnt = 0;
            int cur = i;
            while (nums[cur] != -1) {
                int nxt = nums[cur];
                nums[cur] = -1; // mark as visited
                cur = nxt;
                ++cnt;
            }
            best = max(best, cnt);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int arrayNesting(int[] nums) {
        int n = nums.length;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                int count = 0;
                int cur = i;
                while (nums[cur] >= 0) {
                    int next = nums[cur];
                    nums[cur] = -1; // mark visited
                    cur = next;
                    count++;
                }
                if (count > maxLen) {
                    maxLen = count;
                }
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 0
        for i in range(n):
            if nums[i] < n:  # not visited yet
                cnt = 0
                cur = i
                while nums[cur] < n:
                    nxt = nums[cur]
                    nums[cur] = n  # mark as visited
                    cur = nxt
                    cnt += 1
                max_len = max(max_len, cnt)
        return max_len
```

## Python3

```python
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_len = 0
        for i in range(n):
            if not visited[i]:
                cur = i
                cnt = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = nums[cur]
                    cnt += 1
                if cnt > max_len:
                    max_len = cnt
        return max_len
```

## C

```c
int arrayNesting(int* nums, int numsSize) {
    int maxLen = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == -1) continue;
        int count = 0;
        int cur = i;
        while (nums[cur] != -1) {
            int next = nums[cur];
            nums[cur] = -1;
            cur = next;
            ++count;
        }
        if (count > maxLen) maxLen = count;
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution
{
    public int ArrayNesting(int[] nums)
    {
        int n = nums.Length;
        int maxLen = 0;

        for (int i = 0; i < n; i++)
        {
            if (nums[i] >= 0)
            {
                int count = 0;
                int cur = i;
                while (nums[cur] >= 0)
                {
                    int next = nums[cur];
                    nums[cur] = -1; // mark as visited
                    cur = next;
                    count++;
                }
                if (count > maxLen) maxLen = count;
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
var arrayNesting = function(nums) {
    let maxLen = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (nums[i] === -1) continue;
        let count = 0;
        let cur = i;
        while (nums[cur] !== -1) {
            const next = nums[cur];
            nums[cur] = -1; // mark as visited
            cur = next;
            count++;
        }
        if (count > maxLen) maxLen = count;
    }
    return maxLen;
};
```

## Typescript

```typescript
function arrayNesting(nums: number[]): number {
    let maxLen = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (nums[i] === -1) continue;
        let count = 0;
        let cur = i;
        while (nums[cur] !== -1) {
            const next = nums[cur];
            nums[cur] = -1; // mark as visited
            cur = next;
            count++;
        }
        if (count > maxLen) maxLen = count;
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
    function arrayNesting($nums) {
        $n = count($nums);
        $visited = array_fill(0, $n, false);
        $maxLen = 0;
        for ($i = 0; $i < $n; $i++) {
            if (!$visited[$i]) {
                $cnt = 0;
                $j = $i;
                while (!$visited[$j]) {
                    $visited[$j] = true;
                    $j = $nums[$j];
                    $cnt++;
                }
                if ($cnt > $maxLen) {
                    $maxLen = $cnt;
                }
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func arrayNesting(_ nums: [Int]) -> Int {
        var arr = nums
        let n = arr.count
        var maxLen = 0
        
        for i in 0..<n {
            if arr[i] == -1 { continue }
            var count = 0
            var j = i
            while arr[j] != -1 {
                let next = arr[j]
                arr[j] = -1
                j = next
                count += 1
            }
            if count > maxLen {
                maxLen = count
            }
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrayNesting(nums: IntArray): Int {
        var maxLen = 0
        val n = nums.size
        for (i in 0 until n) {
            var count = 0
            var cur = i
            while (nums[cur] >= 0) {
                val next = nums[cur]
                nums[cur] = -1
                cur = next
                count++
            }
            if (count > maxLen) maxLen = count
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int arrayNesting(List<int> nums) {
    int maxSize = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == -1) continue;
      int cur = i;
      int count = 0;
      while (nums[cur] != -1) {
        int next = nums[cur];
        nums[cur] = -1; // mark as visited
        cur = next;
        count++;
      }
      if (count > maxSize) maxSize = count;
    }
    return maxSize;
  }
}
```

## Golang

```go
func arrayNesting(nums []int) int {
    maxLen := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        if nums[i] == -1 {
            continue
        }
        cnt := 0
        cur := i
        for nums[cur] != -1 {
            next := nums[cur]
            nums[cur] = -1
            cur = next
            cnt++
        }
        if cnt > maxLen {
            maxLen = cnt
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def array_nesting(nums)
  max_len = 0
  n = nums.length
  i = 0
  while i < n
    if nums[i] >= 0
      count = 0
      j = i
      while nums[j] >= 0
        nxt = nums[j]
        nums[j] = -1
        j = nxt
        count += 1
      end
      max_len = count if count > max_len
    end
    i += 1
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def arrayNesting(nums: Array[Int]): Int = {
        val n = nums.length
        val visited = new Array[Boolean](n)
        var maxLen = 0

        for (i <- 0 until n) {
            if (!visited(i)) {
                var cur = i
                var count = 0
                while (!visited(cur)) {
                    visited(cur) = true
                    cur = nums(cur)
                    count += 1
                }
                if (count > maxLen) maxLen = count
            }
        }

        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn array_nesting(mut nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_len = 0usize;
        for i in 0..n {
            if nums[i] == -1 {
                continue;
            }
            let mut count = 0usize;
            let mut cur = i as i32;
            while nums[cur as usize] != -1 {
                let next = nums[cur as usize];
                nums[cur as usize] = -1; // mark visited
                cur = next;
                count += 1;
            }
            if count > max_len {
                max_len = count;
            }
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (array-nesting nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (visited (make-vector n #f))
         (maxlen 0))
    (for ([i (in-range n)])
      (when (not (vector-ref visited i))
        (let ((cnt 0)
              (cur i))
          (let loop ()
            (when (not (vector-ref visited cur))
              (vector-set! visited cur #t)
              (set! cnt (+ cnt 1))
              (set! cur (vector-ref vec cur))
              (loop)))
          (when (> cnt maxlen) (set! maxlen cnt)))))
    maxlen))
```

## Erlang

```erlang
-spec array_nesting(Nums :: [integer()]) -> integer().
array_nesting(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    Indices = lists:seq(0, N - 1),
    loop_indices(Indices, Tuple, #{}, 0).

loop_indices([], _Tuple, _Visited, Max) -> Max;
loop_indices([I | Rest], Tuple, Visited, Max) ->
    case maps:is_key(I, Visited) of
        true ->
            loop_indices(Rest, Tuple, Visited, Max);
        false ->
            {Cnt, NewVisited} = traverse(I, Tuple, Visited, 0),
            NewMax = if Cnt > Max -> Cnt; true -> Max end,
            loop_indices(Rest, Tuple, NewVisited, NewMax)
    end.

traverse(Cur, Tuple, Visited, Count) ->
    case maps:is_key(Cur, Visited) of
        true ->
            {Count, Visited};
        false ->
            Next = element(Cur + 1, Tuple),
            Visited1 = maps:put(Cur, true, Visited),
            traverse(Next, Tuple, Visited1, Count + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec array_nesting(nums :: [integer]) :: integer
  def array_nesting(nums) do
    n = length(nums)
    tup = List.to_tuple(nums)
    loop(0, n, tup, MapSet.new(), 0)
  end

  defp loop(i, n, _tup, visited, max_len) when i == n, do: max_len

  defp loop(i, n, tup, visited, max_len) do
    if MapSet.member?(visited, i) do
      loop(i + 1, n, tup, visited, max_len)
    else
      {len, visited2} = traverse(i, tup, visited, 0)
      new_max = if len > max_len, do: len, else: max_len
      loop(i + 1, n, tup, visited2, new_max)
    end
  end

  defp traverse(cur, tup, visited, count) do
    if MapSet.member?(visited, cur) do
      {count, visited}
    else
      visited = MapSet.put(visited, cur)
      next = elem(tup, cur)
      traverse(next, tup, visited, count + 1)
    end
  end
end
```
