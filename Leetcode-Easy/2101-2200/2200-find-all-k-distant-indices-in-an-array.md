# 2200. Find All K-Distant Indices in an Array

## Cpp

```cpp
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n = nums.size();
        vector<int> res;
        int r = 0; // smallest index not yet added
        for (int j = 0; j < n; ++j) {
            if (nums[j] == key) {
                int left = max(0, j - k);
                int right = min(n - 1, j + k);
                int start = max(r, left);
                for (int i = start; i <= right; ++i) {
                    res.push_back(i);
                }
                r = right + 1;
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        int next = 0; // smallest index not yet added
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int left = Math.max(0, i - k);
                int right = Math.min(n - 1, i + k);
                int start = Math.max(left, next);
                for (int idx = start; idx <= right; idx++) {
                    result.add(idx);
                }
                next = Math.max(next, right + 1);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        nxt = 0  # smallest index not yet added
        for i, val in enumerate(nums):
            if val == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)
                start = max(nxt, left)
                for idx in range(start, right + 1):
                    res.append(idx)
                nxt = right + 1
        return res
```

## Python3

```python
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = set()
        for i, val in enumerate(nums):
            if val == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)
                for j in range(left, right + 1):
                    result.add(j)
        return sorted(result)
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findKDistantIndices(int* nums, int numsSize, int key, int k, int* returnSize) {
    int* res = (int*)malloc(numsSize * sizeof(int));
    int idx = 0;
    int nextStart = 0; // smallest index not yet added

    for (int j = 0; j < numsSize; ++j) {
        if (nums[j] == key) {
            int left = j - k;
            if (left < 0) left = 0;
            int right = j + k;
            if (right >= numsSize) right = numsSize - 1;

            int start = nextStart > left ? nextStart : left;
            for (int i = start; i <= right; ++i) {
                res[idx++] = i;
            }
            nextStart = right + 1;
        }
    }

    *returnSize = idx;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindKDistantIndices(int[] nums, int key, int k) {
        int n = nums.Length;
        var result = new List<int>();
        int next = 0; // smallest index not yet added
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                int left = Math.Max(0, i - k);
                int right = Math.Min(n - 1, i + k);
                int start = Math.Max(left, next);
                for (int idx = start; idx <= right; idx++) {
                    result.Add(idx);
                }
                next = Math.Max(next, right + 1);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function(nums, key, k) {
    const n = nums.length;
    const res = [];
    let next = 0; // smallest index not yet added
    for (let i = 0; i < n; ++i) {
        if (nums[i] === key) {
            const left = Math.max(0, i - k);
            const right = Math.min(n - 1, i + k);
            let start = Math.max(next, left);
            for (let idx = start; idx <= right; ++idx) {
                res.push(idx);
            }
            next = right + 1;
        }
    }
    return res;
};
```

## Typescript

```typescript
function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    const n = nums.length;
    const result: number[] = [];
    let nextIdx = 0; // smallest index not yet added

    for (let j = 0; j < n; ++j) {
        if (nums[j] !== key) continue;

        const left = Math.max(0, j - k);
        const right = Math.min(n - 1, j + k);

        const start = Math.max(left, nextIdx);
        for (let i = start; i <= right; ++i) {
            result.push(i);
        }
        nextIdx = Math.max(nextIdx, right + 1);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $key
     * @param Integer $k
     * @return Integer[]
     */
    function findKDistantIndices($nums, $key, $k) {
        $n = count($nums);
        $res = [];
        $next = 0; // smallest index not yet added
        for ($j = 0; $j < $n; $j++) {
            if ($nums[$j] == $key) {
                $l = max(0, $j - $k);
                $r = min($n - 1, $j + $k);
                $start = max($next, $l);
                for ($i = $start; $i <= $r; $i++) {
                    $res[] = $i;
                }
                $next = $r + 1;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func findKDistantIndices(_ nums: [Int], _ key: Int, _ k: Int) -> [Int] {
        var result = [Int]()
        let n = nums.count
        var next = 0
        for (j, value) in nums.enumerated() {
            if value == key {
                let left = max(0, j - k)
                let right = min(n - 1, j + k)
                var start = max(left, next)
                while start <= right {
                    result.append(start)
                    start += 1
                }
                next = right + 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKDistantIndices(nums: IntArray, key: Int, k: Int): List<Int> {
        val n = nums.size
        val result = mutableListOf<Int>()
        var next = 0
        for (j in 0 until n) {
            if (nums[j] == key) {
                val left = kotlin.math.max(0, j - k)
                val right = kotlin.math.min(n - 1, j + k)
                var start = kotlin.math.max(left, next)
                while (start <= right) {
                    result.add(start)
                    start++
                }
                next = kotlin.math.max(next, right + 1)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findKDistantIndices(List<int> nums, int key, int k) {
    int n = nums.length;
    List<int> res = [];
    int nextIdx = 0;
    for (int j = 0; j < n; ++j) {
      if (nums[j] == key) {
        int left = j - k;
        if (left < 0) left = 0;
        int right = j + k;
        if (right >= n) right = n - 1;
        int start = nextIdx > left ? nextIdx : left;
        for (int i = start; i <= right; ++i) {
          res.add(i);
        }
        nextIdx = right + 1;
      }
    }
    return res;
  }
}
```

## Golang

```go
func findKDistantIndices(nums []int, key int, k int) []int {
	n := len(nums)
	res := make([]int, 0)
	next := 0
	for i, v := range nums {
		if v == key {
			left := i - k
			if left < 0 {
				left = 0
			}
			right := i + k
			if right >= n {
				right = n - 1
			}
			start := left
			if next > start {
				start = next
			}
			for j := start; j <= right; j++ {
				res = append(res, j)
			}
			next = right + 1
		}
	}
	return res
}
```

## Ruby

```ruby
def find_k_distant_indices(nums, key, k)
  n = nums.length
  result = []
  next_idx = 0

  nums.each_with_index do |val, j|
    next unless val == key

    left = [j - k, 0].max
    right = [j + k, n - 1].min

    start = [left, next_idx].max
    if start <= right
      (start..right).each { |i| result << i }
      next_idx = right + 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def findKDistantIndices(nums: Array[Int], key: Int, k: Int): List[Int] = {
        val n = nums.length
        val result = scala.collection.mutable.ListBuffer[Int]()
        var nextIdx = 0
        for (j <- 0 until n) {
            if (nums(j) == key) {
                val left = math.max(0, j - k)
                val right = math.min(n - 1, j + k)
                var i = math.max(left, nextIdx)
                while (i <= right) {
                    result += i
                    i += 1
                }
                if (right + 1 > nextIdx) nextIdx = right + 1
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let n = nums.len();
        let mut res: Vec<i32> = Vec::new();
        let mut next_start: usize = 0;
        let kk = k as usize;

        for (j, &val) in nums.iter().enumerate() {
            if val == key {
                let left = if j >= kk { j - kk } else { 0 };
                let right = std::cmp::min(n - 1, j + kk);
                let start = std::cmp::max(next_start, left);
                if start <= right {
                    for idx in start..=right {
                        res.push(idx as i32);
                    }
                    next_start = right + 1;
                }
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (find-k-distant-indices nums key k)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ((n (length nums)))
    (let loop ((i 0) (r 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (let ((val (list-ref nums i)))
            (if (= val key)
                (let* ((left (max 0 (- i k)))
                       (right (min (- n 1) (+ i k)))
                       (start (max left r))
                       (new-acc
                        (let loop2 ((j right) (a acc))
                          (if (< j start) a
                              (loop2 (- j 1) (cons j a)))))
                       (new-r (max r (+ right 1))))
                  (loop (+ i 1) new-r new-acc))
                (loop (+ i 1) r acc)))))))
```

## Erlang

```erlang
-spec find_k_distant_indices(Nums :: [integer()], Key :: integer(), K :: integer()) -> [integer()].
find_k_distant_indices(Nums, Key, K) ->
    Len = length(Nums),
    loop(0, Nums, Len, Key, K, -1, []).

loop(_Idx, [], _Len, _Key, _K, _CurEnd, Acc) ->
    lists:reverse(Acc);
loop(Idx, [H|T], Len, Key, K, CurEnd, Acc) ->
    if H =:= Key ->
            L = erlang:max(0, Idx - K),
            R = erlang:min(Len-1, Idx + K),
            NewStart = erlang:max(L, CurEnd+1),
            case NewStart =< R of
                true ->
                    Range = lists:seq(NewStart, R),
                    RevRange = lists:reverse(Range),
                    loop(Idx+1, T, Len, Key, K, R, RevRange ++ Acc);
                false ->
                    loop(Idx+1, T, Len, Key, K, CurEnd, Acc)
            end;
       true ->
            loop(Idx+1, T, Len, Key, K, CurEnd, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_k_distant_indices(nums :: [integer], key :: integer, k :: integer) :: [integer]
  def find_k_distant_indices(nums, key, k) do
    n = length(nums)

    {res_rev, _} =
      Enum.reduce(Enum.with_index(nums), {[], 0}, fn {val, i}, {acc, r} ->
        if val == key do
          left = max(0, i - k)
          right = min(n - 1, i + k)
          start = max(r, left)

          new_acc =
            if start <= right do
              Enum.reduce(start..right, acc, fn idx, a -> [idx | a] end)
            else
              acc
            end

          {new_acc, right + 1}
        else
          {acc, r}
        end
      end)

    Enum.reverse(res_rev)
  end
end
```
