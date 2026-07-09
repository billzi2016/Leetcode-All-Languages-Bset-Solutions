# 2869. Minimum Operations to Collect Elements

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        vector<bool> seen(k + 1, false);
        int cnt = 0;
        int n = nums.size();
        for (int i = n - 1; i >= 0; --i) {
            int x = nums[i];
            if (x <= k && !seen[x]) {
                seen[x] = true;
                ++cnt;
                if (cnt == k) {
                    return n - i;
                }
            }
        }
        return n; // should never reach here due to problem guarantee
    }
};
```

## Java

```java
class Solution {
    public int minOperations(List<Integer> nums, int k) {
        int n = nums.size();
        boolean[] seen = new boolean[k + 1];
        int count = 0;
        for (int i = n - 1; i >= 0; --i) {
            int val = nums.get(i);
            if (val <= k && !seen[val]) {
                seen[val] = true;
                count++;
                if (count == k) {
                    return n - i;
                }
            }
        }
        return n;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = [False] * (k + 1)
        remaining = k
        ops = 0
        for num in reversed(nums):
            ops += 1
            if 1 <= num <= k and not seen[num]:
                seen[num] = True
                remaining -= 1
                if remaining == 0:
                    return ops
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = [False] * (k + 1)
        cnt = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            v = nums[i]
            if 1 <= v <= k and not seen[v]:
                seen[v] = True
                cnt += 1
                if cnt == k:
                    return n - i
        return -1
```

## C

```c
int minOperations(int* nums, int numsSize, int k) {
    int seen[51] = {0};
    int cnt = 0;
    for (int i = numsSize - 1; i >= 0; --i) {
        int val = nums[i];
        if (val <= k && !seen[val]) {
            seen[val] = 1;
            ++cnt;
            if (cnt == k) {
                return numsSize - i;
            }
        }
    }
    return numsSize;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(IList<int> nums, int k) {
        bool[] seen = new bool[k + 1];
        int collected = 0;
        int n = nums.Count;
        for (int i = n - 1; i >= 0; i--) {
            int val = nums[i];
            if (val <= k && !seen[val]) {
                seen[val] = true;
                collected++;
                if (collected == k) {
                    return n - i;
                }
            }
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    const n = nums.length;
    const seen = new Array(k + 1).fill(false);
    let collected = 0;
    
    for (let i = n - 1; i >= 0; --i) {
        const val = nums[i];
        if (val <= k && !seen[val]) {
            seen[val] = true;
            ++collected;
        }
        if (collected === k) {
            return n - i;
        }
    }
    
    // According to problem constraints, this line is never reached.
    return n;
};
```

## Typescript

```typescript
function minOperations(nums: number[], k: number): number {
    const seen = new Array(k + 1).fill(false);
    let collected = 0;
    let ops = 0;
    for (let i = nums.length - 1; i >= 0; i--) {
        ops++;
        const val = nums[i];
        if (val <= k && !seen[val]) {
            seen[val] = true;
            collected++;
            if (collected === k) return ops;
        }
    }
    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        $n = count($nums);
        $seen = array_fill(0, $k + 1, false);
        $cnt = 0;
        for ($i = $n - 1; $i >= 0; --$i) {
            $val = $nums[$i];
            if ($val <= $k && !$seen[$val]) {
                $seen[$val] = true;
                $cnt++;
                if ($cnt == $k) {
                    return $n - $i;
                }
            }
        }
        // According to problem constraints, this line is never reached.
        return $n;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var seen = Array(repeating: false, count: k + 1)
        var collected = 0
        let n = nums.count
        for i in stride(from: n - 1, through: 0, by: -1) {
            let val = nums[i]
            if val <= k && !seen[val] {
                seen[val] = true
                collected += 1
                if collected == k {
                    return n - i
                }
            }
        }
        return n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: List<Int>, k: Int): Int {
        val seen = BooleanArray(k + 1)
        var count = 0
        for (i in nums.size - 1 downTo 0) {
            val v = nums[i]
            if (v <= k && !seen[v]) {
                seen[v] = true
                count++
                if (count == k) {
                    return nums.size - i
                }
            }
        }
        return nums.size
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    List<bool> seen = List.filled(k + 1, false);
    int cnt = 0;
    int n = nums.length;
    for (int i = n - 1; i >= 0; --i) {
      int v = nums[i];
      if (v <= k && !seen[v]) {
        seen[v] = true;
        cnt++;
        if (cnt == k) return n - i;
      }
    }
    return 0;
  }
}
```

## Golang

```go
func minOperations(nums []int, k int) int {
	seen := make([]bool, k+1)
	collected := 0
	for i := len(nums) - 1; i >= 0; i-- {
		val := nums[i]
		if val <= k && !seen[val] {
			seen[val] = true
			collected++
			if collected == k {
				return len(nums) - i
			}
		}
	}
	return 0
}
```

## Ruby

```ruby
def min_operations(nums, k)
  visited = Array.new(k + 1, false)
  count = 0
  n = nums.length
  (n - 1).downto(0) do |i|
    val = nums[i]
    if val <= k && !visited[val]
      visited[val] = true
      count += 1
    end
    return n - i if count == k
  end
  n
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: List[Int], k: Int): Int = {
        val arr = nums.toArray
        val seen = new Array[Boolean](k + 1)
        var cnt = 0
        var i = arr.length - 1
        while (i >= 0) {
            val v = arr(i)
            if (v <= k && !seen(v)) {
                seen(v) = true
                cnt += 1
                if (cnt == k) return arr.length - i
            }
            i -= 1
        }
        arr.length
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        let mut seen = vec![false; k_usize + 1];
        let mut cnt = 0usize;
        for (i, &v) in nums.iter().enumerate().rev() {
            let val = v as usize;
            if val <= k_usize && !seen[val] {
                seen[val] = true;
                cnt += 1;
            }
            if cnt == k_usize {
                return (n - i) as i32;
            }
        }
        n as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (visited (make-vector (+ k 1) #f))
         (cnt 0))
    (let loop ((i (- n 1)))
      (if (< i 0)
          0
          (begin
            (define val (list-ref nums i))
            (when (and (<= val k) (not (vector-ref visited val)))
              (vector-set! visited val #t)
              (set! cnt (+ cnt 1)))
            (if (= cnt k)
                (- n i)
                (loop (- i 1)))))))
```

## Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
    Rev = lists:reverse(Nums),
    min_ops_rev(Rev, K, 0, 0, 0).

min_ops_rev([], _K, _Mask, _Count, _Steps) ->
    0;
min_ops_rev([H|T], K, Mask, Count, Steps) ->
    Bit = 1 bsl (H-1),
    IsNew = H =< K andalso (Mask band Bit) =:= 0,
    NewMask = if IsNew -> Mask bor Bit; true -> Mask end,
    NewCount = if IsNew -> Count + 1; true -> Count end,
    NewSteps = Steps + 1,
    case NewCount of
        C when C == K -> NewSteps;
        _ -> min_ops_rev(T, K, NewMask, NewCount, NewSteps)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    {ops, _} =
      Enum.reduce_while(Enum.with_index(Enum.reverse(nums)), {0, MapSet.new()}, fn {val, idx}, {_prev_ops, seen} ->
        ops = idx + 1

        new_seen =
          if val <= k and not MapSet.member?(seen, val) do
            MapSet.put(seen, val)
          else
            seen
          end

        if MapSet.size(new_seen) == k do
          {:halt, {ops, new_seen}}
        else
          {:cont, {ops, new_seen}}
        end
      end)

    ops
  end
end
```
