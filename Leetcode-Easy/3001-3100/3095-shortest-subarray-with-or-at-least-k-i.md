# 3095. Shortest Subarray With OR at Least K I

## Cpp

```cpp
class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        if (k == 0) return 1;
        const int n = nums.size();
        int best = n + 1;
        for (int i = 0; i < n; ++i) {
            int cur = 0;
            for (int j = i; j < n; ++j) {
                cur |= nums[j];
                if (cur >= k) {
                    best = min(best, j - i + 1);
                    break; // longer subarrays from i will be larger
                }
            }
        }
        return best == n + 1 ? -1 : best;
    }
};
```

## Java

```java
class Solution {
    public int minimumSubarrayLength(int[] nums, int k) {
        if (k == 0) return 1;
        int n = nums.length;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i; j < n; j++) {
                cur |= nums[j];
                if (cur >= k) {
                    ans = Math.min(ans, j - i + 1);
                    break;
                }
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 0:
            return 1
        best = n + 1
        for i in range(n):
            cur_or = 0
            for j in range(i, n):
                cur_or |= nums[j]
                if cur_or >= k:
                    length = j - i + 1
                    if length < best:
                        best = length
                    break
        return best if best <= n else -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 1
        ans = float('inf')
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur |= nums[j]
                if cur >= k:
                    ans = min(ans, j - i + 1)
                    break
        return -1 if ans == float('inf') else ans
```

## C

```c
int minimumSubarrayLength(int* nums, int numsSize, int k) {
    int best = numsSize + 1;
    for (int i = 0; i < numsSize; ++i) {
        long long cur = 0;
        for (int j = i; j < numsSize; ++j) {
            cur |= (long long)nums[j];
            if (cur >= k) {
                int len = j - i + 1;
                if (len < best) best = len;
                break; // longer subarrays from this start are not shorter
            }
        }
    }
    return (best == numsSize + 1) ? -1 : best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSubarrayLength(int[] nums, int k) {
        if (k == 0) return 1;
        int n = nums.Length;
        int best = int.MaxValue;
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i; j < n; j++) {
                cur |= nums[j];
                if (cur >= k) {
                    best = Math.Min(best, j - i + 1);
                    break;
                }
            }
        }
        return best == int.MaxValue ? -1 : best;
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
var minimumSubarrayLength = function(nums, k) {
    const n = nums.length;
    let best = Infinity;
    for (let i = 0; i < n; ++i) {
        let curOr = 0;
        for (let j = i; j < n; ++j) {
            curOr |= nums[j];
            if (curOr >= k) {
                const len = j - i + 1;
                if (len < best) best = len;
                break; // longer subarrays starting at i are not shorter
            }
        }
    }
    return best === Infinity ? -1 : best;
};
```

## Typescript

```typescript
function minimumSubarrayLength(nums: number[], k: number): number {
    const n = nums.length;
    let best = Infinity;

    for (let i = 0; i < n; i++) {
        let curOr = 0;
        for (let j = i; j < n; j++) {
            curOr |= nums[j];
            if (curOr >= k) {
                const len = j - i + 1;
                if (len < best) best = len;
                break; // longer subarrays from this start are not shorter
            }
        }
    }

    return best === Infinity ? -1 : best;
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
    function minimumSubarrayLength($nums, $k) {
        if ($k == 0) {
            return 1;
        }
        $n = count($nums);
        $best = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $or = 0;
            for ($j = $i; $j < $n; $j++) {
                $or |= $nums[$j];
                if ($or >= $k) {
                    $len = $j - $i + 1;
                    if ($len < $best) {
                        $best = $len;
                    }
                    break; // longer subarrays starting at i will be larger
                }
            }
        }
        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 0 { return 1 }
        var best = Int.max
        for i in 0..<n {
            var cur = 0
            for j in i..<n {
                cur |= nums[j]
                if cur >= k {
                    let len = j - i + 1
                    if len < best { best = len }
                    break
                }
            }
        }
        return best == Int.max ? -1 : best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSubarrayLength(nums: IntArray, k: Int): Int {
        if (k == 0) return 1
        var best = Int.MAX_VALUE
        val n = nums.size
        for (i in 0 until n) {
            var cur = 0
            for (j in i until n) {
                cur = cur or nums[j]
                if (cur >= k) {
                    val len = j - i + 1
                    if (len < best) best = len
                    break
                }
            }
        }
        return if (best == Int.MAX_VALUE) -1 else best
    }
}
```

## Dart

```dart
class Solution {
  int minimumSubarrayLength(List<int> nums, int k) {
    int n = nums.length;
    const int INF = 1 << 30;
    int ans = INF;

    for (int i = 0; i < n; ++i) {
      int cur = 0;
      for (int j = i; j < n; ++j) {
        cur |= nums[j];
        if (cur >= k) {
          ans = ans < (j - i + 1) ? ans : (j - i + 1);
          break; // longer subarrays starting at i will be larger
        }
      }
    }

    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minimumSubarrayLength(nums []int, k int) int {
	n := len(nums)
	const inf = int(^uint(0) >> 1) // max int
	best := inf

	for i := 0; i < n; i++ {
		cur := 0
		for j := i; j < n; j++ {
			cur |= nums[j]
			if cur >= k {
				if length := j - i + 1; length < best {
					best = length
				}
				break
			}
		}
	}

	if best == inf {
		return -1
	}
	return best
}
```

## Ruby

```ruby
def minimum_subarray_length(nums, k)
  n = nums.length
  best = Float::INFINITY
  (0...n).each do |i|
    cur = 0
    (i...n).each do |j|
      cur |= nums[j]
      if cur >= k
        len = j - i + 1
        best = len if len < best
        break
      end
    end
  end
  best == Float::INFINITY ? -1 : best
end
```

## Scala

```scala
object Solution {
    def minimumSubarrayLength(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        var best = Int.MaxValue
        for (i <- 0 until n) {
            var cur = 0
            for (j <- i until n) {
                cur |= nums(j)
                if (cur >= k) {
                    val len = j - i + 1
                    if (len < best) best = len
                }
            }
        }
        if (best == Int.MaxValue) -1 else best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if k == 0 {
            return 1;
        }
        let mut best = usize::MAX;
        for i in 0..n {
            let mut cur: u64 = 0;
            for j in i..n {
                cur |= nums[j] as u64;
                if cur >= k as u64 {
                    best = best.min(j - i + 1);
                    break; // longer subarrays from this start are not needed
                }
            }
        }
        if best == usize::MAX { -1 } else { best as i32 }
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (minimum-subarray-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [vec (list->vector nums)])
    (if (= k 0)
        (if (> n 0) 1 -1)
        (let loop-i ((i 0) (best (+ n 1)))
          (if (>= i n)
              (if (> best n) -1 best)
              (let loop-j ((j i) (cur-or 0) (best-inner best))
                (if (>= j n)
                    (loop-i (+ i 1) best-inner)
                    (let* ([new-or (bitwise-ior cur-or (vector-ref vec j))]
                           [len (+ 1 (- j i))]
                           [new-best (if (and (>= new-or k) (< len best-inner))
                                         len
                                         best-inner)])
                      (loop-j (+ j 1) new-or new-best)))))))))
```

## Erlang

```erlang
-spec minimum_subarray_length(Nums :: [integer()], K :: integer()) -> integer().
minimum_subarray_length(Nums, K) ->
    case K of
        0 -> 1;
        _ ->
            N = length(Nums),
            Min = find_min(Nums, K, 1, N + 1, N),
            if Min =:= N + 1 -> -1; true -> Min end
    end.

find_min(_Nums, _K, I, Min, N) when I > N ->
    Min;
find_min(Nums, K, I, Min, N) ->
    Rest = lists:sublist(Nums, I),
    NewMin = inner(Rest, K, Min),
    find_min(Nums, K, I + 1, NewMin, N).

inner(List, K, Min) ->
    inner2(List, K, 0, 0, Min).

inner2([], _K, _Acc, _Len, Min) ->
    Min;
inner2([H|T], K, Acc, Len, Min) ->
    NewAcc = Acc bor H,
    NewLen = Len + 1,
    if
        NewAcc >= K ->
            case NewLen < Min of
                true -> NewLen;
                false -> Min
            end;
        true ->
            inner2(T, K, NewAcc, NewLen, Min)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec minimum_subarray_length(nums :: [integer], k :: integer) :: integer
  def minimum_subarray_length(nums, k) do
    n = length(nums)

    if k == 0 do
      1
    else
      best = find_min(nums, k, 0, n, n + 1)
      if best == n + 1, do: -1, else: best
    end
  end

  defp find_min(_nums, _k, i, n, best) when i >= n, do: best

  defp find_min(nums, k, i, n, best) do
    new_best = find_min_j(i, i, nums, k, n, best, 0)

    if new_best == 1 do
      1
    else
      find_min(nums, k, i + 1, n, new_best)
    end
  end

  defp find_min_j(_start, j, _nums, _k, _n, best, _cur_or) when j >= _n, do: best

  defp find_min_j(start, j, nums, k, n, best, cur_or) do
    cur_or = cur_or ||| Enum.at(nums, j)

    if cur_or >= k do
      len = j - start + 1
      min(best, len)
    else
      find_min_j(start, j + 1, nums, k, n, best, cur_or)
    end
  end
end
```
