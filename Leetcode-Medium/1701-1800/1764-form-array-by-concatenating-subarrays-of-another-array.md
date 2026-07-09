# 1764. Form Array by Concatenating Subarrays of Another Array

## Cpp

```cpp
class Solution {
public:
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        int pos = 0;
        int n = nums.size();
        for (const auto& g : groups) {
            int m = g.size();
            bool found = false;
            while (pos + m <= n) {
                bool match = true;
                for (int i = 0; i < m; ++i) {
                    if (nums[pos + i] != g[i]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    found = true;
                    pos += m;
                    break;
                }
                ++pos;
            }
            if (!found) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canChoose(int[][] groups, int[] nums) {
        int idx = 0; // current start position in nums
        for (int[] group : groups) {
            int found = -1;
            while (idx + group.length <= nums.length) {
                boolean match = true;
                for (int j = 0; j < group.length; ++j) {
                    if (nums[idx + j] != group[j]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    found = idx;
                    break;
                }
                idx++;
            }
            if (found == -1) {
                return false;
            }
            // move index past the matched subarray for next group
            idx = found + group.length;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        i = 0  # current start index in nums
        n = len(nums)
        for g in groups:
            m = len(g)
            found = False
            while i + m <= n:
                if nums[i:i+m] == g:
                    found = True
                    i += m  # move past this subarray for next group
                    break
                i += 1
            if not found:
                return False
        return True
```

## Python3

```python
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        for g in groups:
            m = len(g)
            found = False
            while i + m <= n:
                if nums[i:i + m] == g:
                    found = True
                    i += m
                    break
                i += 1
            if not found:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool canChoose(int** groups, int groupsSize, int* groupsColSize, int* nums, int numsSize) {
    int pos = 0;
    for (int i = 0; i < groupsSize; ++i) {
        int len = groupsColSize[i];
        bool matched = false;
        while (pos + len <= numsSize) {
            int j = 0;
            for (; j < len; ++j) {
                if (nums[pos + j] != groups[i][j]) break;
            }
            if (j == len) {
                matched = true;
                pos += len;
                break;
            }
            ++pos;
        }
        if (!matched) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanChoose(int[][] groups, int[] nums) {
        int pos = 0;
        foreach (var group in groups) {
            bool found = false;
            // Try to match the current group starting from position 'pos'
            for (int i = pos; i <= nums.Length - group.Length; i++) {
                int j = 0;
                while (j < group.Length && nums[i + j] == group[j]) {
                    j++;
                }
                if (j == group.Length) {
                    // Match found
                    pos = i + group.Length; // move past this subarray
                    found = true;
                    break;
                }
            }
            if (!found) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} groups
 * @param {number[]} nums
 * @return {boolean}
 */
var canChoose = function(groups, nums) {
    let pos = 0; // current start index in nums
    for (const g of groups) {
        const m = g.length;
        let found = false;
        while (pos + m <= nums.length) {
            // try to match at current pos
            let ok = true;
            for (let i = 0; i < m; ++i) {
                if (nums[pos + i] !== g[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                found = true;
                pos += m; // move past this matched subarray
                break;
            }
            pos++; // shift start forward and try again
        }
        if (!found) return false;
    }
    return true;
};
```

## Typescript

```typescript
function canChoose(groups: number[][], nums: number[]): boolean {
    let pos = 0;
    for (const g of groups) {
        const len = g.length;
        let found = false;
        while (pos + len <= nums.length) {
            let match = true;
            for (let i = 0; i < len; ++i) {
                if (nums[pos + i] !== g[i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                found = true;
                pos += len;
                break;
            }
            pos++;
        }
        if (!found) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $groups
     * @param Integer[] $nums
     * @return Boolean
     */
    function canChoose($groups, $nums) {
        $pos = 0;
        $n = count($nums);
        foreach ($groups as $group) {
            $lenG = count($group);
            $found = false;
            for ($start = $pos; $start <= $n - $lenG; $start++) {
                $match = true;
                for ($k = 0; $k < $lenG; $k++) {
                    if ($nums[$start + $k] !== $group[$k]) {
                        $match = false;
                        break;
                    }
                }
                if ($match) {
                    $found = true;
                    $pos = $start + $lenG;
                    break;
                }
            }
            if (!$found) {
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
    func canChoose(_ groups: [[Int]], _ nums: [Int]) -> Bool {
        var start = 0
        for group in groups {
            let len = group.count
            var matched = false
            while start + len <= nums.count {
                var ok = true
                for i in 0..<len {
                    if nums[start + i] != group[i] {
                        ok = false
                        break
                    }
                }
                if ok {
                    matched = true
                    start += len
                    break
                } else {
                    start += 1
                }
            }
            if !matched { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canChoose(groups: Array<IntArray>, nums: IntArray): Boolean {
        var pos = 0
        for (group in groups) {
            var found = false
            while (pos + group.size <= nums.size) {
                var match = true
                for (i in group.indices) {
                    if (nums[pos + i] != group[i]) {
                        match = false
                        break
                    }
                }
                if (match) {
                    found = true
                    pos += group.size
                    break
                } else {
                    pos++
                }
            }
            if (!found) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canChoose(List<List<int>> groups, List<int> nums) {
    int pos = 0;
    for (var group in groups) {
      bool found = false;
      while (pos + group.length <= nums.length) {
        bool match = true;
        for (int i = 0; i < group.length; i++) {
          if (nums[pos + i] != group[i]) {
            match = false;
            break;
          }
        }
        if (match) {
          found = true;
          pos += group.length;
          break;
        }
        pos++;
      }
      if (!found) return false;
    }
    return true;
  }
}
```

## Golang

```go
func canChoose(groups [][]int, nums []int) bool {
    pos := 0
    n := len(nums)
    for _, g := range groups {
        m := len(g)
        found := false
        // try to find g starting at or after pos
        for i := pos; i <= n-m; i++ {
            match := true
            for j := 0; j < m; j++ {
                if nums[i+j] != g[j] {
                    match = false
                    break
                }
            }
            if match {
                pos = i + m
                found = true
                break
            }
        }
        if !found {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def can_choose(groups, nums)
  pos = 0
  groups.each do |g|
    found = false
    while pos + g.length <= nums.length
      if nums[pos, g.length] == g
        found = true
        pos += g.length
        break
      else
        pos += 1
      end
    end
    return false unless found
  end
  true
end
```

## Scala

```scala
object Solution {
    def canChoose(groups: Array[Array[Int]], nums: Array[Int]): Boolean = {
        var pos = 0
        for (g <- groups) {
            var matched = false
            while (!matched && pos + g.length <= nums.length) {
                var ok = true
                var k = 0
                while (k < g.length && ok) {
                    if (nums(pos + k) != g(k)) ok = false
                    k += 1
                }
                if (ok) {
                    matched = true
                    pos += g.length
                } else {
                    pos += 1
                }
            }
            if (!matched) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_choose(groups: Vec<Vec<i32>>, nums: Vec<i32>) -> bool {
        let mut pos = 0usize;
        for g in groups.iter() {
            let m = g.len();
            let mut found = false;
            let mut start = pos;
            while start + m <= nums.len() {
                if &nums[start..start + m] == g.as_slice() {
                    found = true;
                    pos = start + m; // next search starts after this subarray
                    break;
                }
                start += 1;
            }
            if !found {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-choose groups nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  (letrec
      ((match-at?
        (lambda (start g)
          (let loop ((i 0))
            (if (= i (length g))
                #t
                (and (< (+ start i) (length nums))
                     (= (list-ref nums (+ start i)) (list-ref g i))
                     (loop (+ i 1)))))))
       (find-start
        (lambda (pos g)
          (let ((n (length nums))
                (m (length g)))
            (let loop ((i pos))
              (cond [(> (+ i m) n) #f]
                    [(match-at? i g) i]
                    [else (loop (+ i 1))]))))
       (process
        (lambda (gs pos)
          (if (null? gs)
              #t
              (let* ((g (car gs))
                     (start (find-start pos g)))
                (and start
                     (process (cdr gs) (+ start (length g)))))))))
    (process groups 0)))
```

## Erlang

```erlang
-module(solution).
-export([can_choose/2]).

-spec can_choose(Groups :: [[integer()]], Nums :: [integer()]) -> boolean().
can_choose(Groups, Nums) ->
    can_choose(Groups, Nums, 0).

can_choose([], _Nums, _Pos) -> true;
can_choose([G|Rest], Nums, Pos) ->
    case find_start(G, Nums, Pos) of
        {ok, Start} ->
            NewPos = Start + length(G),
            can_choose(Rest, Nums, NewPos);
        error -> false
    end.

find_start(G, Nums, Pos) ->
    GLen = length(G),
    MaxStart = length(Nums) - GLen,
    find_start_loop(G, Nums, Pos, MaxStart).

find_start_loop(_G, _Nums, Cur, Max) when Cur > Max -> error;
find_start_loop(G, Nums, Cur, Max) ->
    case lists:sublist(Nums, Cur + 1, length(G)) == G of
        true -> {ok, Cur};
        false -> find_start_loop(G, Nums, Cur + 1, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_choose(groups :: [[integer]], nums :: [integer]) :: boolean
  def can_choose(groups, nums) do
    go(groups, nums, 0)
  end

  defp go([], _nums, _pos), do: true

  defp go([g | rest], nums, pos) do
    case find(nums, pos, g) do
      {:ok, new_pos} -> go(rest, nums, new_pos)
      :error -> false
    end
  end

  defp find(nums, start, pattern) do
    n = length(nums)
    m = length(pattern)

    max_start = n - m
    if start > max_start do
      :error
    else
      search(nums, start, max_start, pattern, m)
    end
  end

  defp search(_nums, i, max_start, _pattern, _m) when i > max_start, do: :error

  defp search(nums, i, max_start, pattern, m) do
    if Enum.slice(nums, i, m) == pattern do
      {:ok, i + m}
    else
      search(nums, i + 1, max_start, pattern, m)
    end
  end
end
```
