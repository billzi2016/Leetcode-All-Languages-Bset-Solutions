# 2293. Min Max Game

## Cpp

```cpp
class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        while (nums.size() > 1) {
            vector<int> nxt;
            nxt.reserve(nums.size() / 2);
            for (size_t i = 0; i < nums.size(); i += 2) {
                size_t idx = i / 2;
                if (idx % 2 == 0)
                    nxt.push_back(min(nums[i], nums[i + 1]));
                else
                    nxt.push_back(max(nums[i], nums[i + 1]));
            }
            nums.swap(nxt);
        }
        return nums[0];
    }
};
```

## Java

```java
class Solution {
    public int minMaxGame(int[] nums) {
        boolean takeMin = true;
        while (nums.length > 1) {
            int n = nums.length / 2;
            int[] next = new int[n];
            for (int i = 0; i < n; i++) {
                int a = nums[2 * i];
                int b = nums[2 * i + 1];
                next[i] = takeMin ? Math.min(a, b) : Math.max(a, b);
            }
            nums = next;
            takeMin = !takeMin;
        }
        return nums[0];
    }
}
```

## Python

```python
class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            nxt = []
            for i in range(0, len(nums), 2):
                idx = i // 2
                if idx % 2 == 0:
                    nxt.append(min(nums[i], nums[i + 1]))
                else:
                    nxt.append(max(nums[i], nums[i + 1]))
            nums = nxt
        return nums[0]
```

## Python3

```python
from typing import List

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(0, len(nums), 2):
                idx = i // 2
                if idx % 2 == 0:
                    nxt.append(min(nums[i], nums[i + 1]))
                else:
                    nxt.append(max(nums[i], nums[i + 1]))
            nums = nxt
        return nums[0]
```

## C

```c
int minMaxGame(int* nums, int numsSize) {
    while (numsSize > 1) {
        int half = numsSize / 2;
        for (int i = 0; i < half; ++i) {
            if (i % 2 == 0) {
                nums[i] = nums[2 * i] < nums[2 * i + 1] ? nums[2 * i] : nums[2 * i + 1];
            } else {
                nums[i] = nums[2 * i] > nums[2 * i + 1] ? nums[2 * i] : nums[2 * i + 1];
            }
        }
        numsSize = half;
    }
    return nums[0];
}
```

## Csharp

```csharp
public class Solution {
    public int MinMaxGame(int[] nums) {
        while (nums.Length > 1) {
            int newLen = nums.Length / 2;
            int[] next = new int[newLen];
            for (int i = 0; i < newLen; i++) {
                if ((i & 1) == 0) {
                    next[i] = Math.Min(nums[2 * i], nums[2 * i + 1]);
                } else {
                    next[i] = Math.Max(nums[2 * i], nums[2 * i + 1]);
                }
            }
            nums = next;
        }
        return nums[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minMaxGame = function(nums) {
    while (nums.length > 1) {
        const next = [];
        for (let i = 0; i < nums.length; i += 2) {
            const idx = i >> 1;
            if ((idx & 1) === 0) {
                next.push(Math.min(nums[i], nums[i + 1]));
            } else {
                next.push(Math.max(nums[i], nums[i + 1]));
            }
        }
        nums = next;
    }
    return nums[0];
};
```

## Typescript

```typescript
function minMaxGame(nums: number[]): number {
    while (nums.length > 1) {
        const n = nums.length;
        const next = new Array(n >> 1);
        for (let i = 0; i < n; i += 2) {
            const idx = i >> 1;
            if ((idx & 1) === 0) {
                next[idx] = Math.min(nums[i], nums[i + 1]);
            } else {
                next[idx] = Math.max(nums[i], nums[i + 1]);
            }
        }
        nums = next;
    }
    return nums[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minMaxGame($nums) {
        while (count($nums) > 1) {
            $new = [];
            $len = count($nums);
            for ($i = 0; $i < $len; $i += 2) {
                $pairIdx = intdiv($i, 2);
                if ($pairIdx % 2 == 0) {
                    $new[] = min($nums[$i], $nums[$i + 1]);
                } else {
                    $new[] = max($nums[$i], $nums[$i + 1]);
                }
            }
            $nums = $new;
        }
        return $nums[0];
    }
}
```

## Swift

```swift
class Solution {
    func minMaxGame(_ nums: [Int]) -> Int {
        var current = nums
        while current.count > 1 {
            var next = [Int]()
            next.reserveCapacity(current.count / 2)
            for i in stride(from: 0, to: current.count, by: 2) {
                let pairIndex = i / 2
                if pairIndex % 2 == 0 {
                    next.append(min(current[i], current[i + 1]))
                } else {
                    next.append(max(current[i], current[i + 1]))
                }
            }
            current = next
        }
        return current[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMaxGame(nums: IntArray): Int {
        var current = nums
        while (current.size > 1) {
            val n = current.size / 2
            val next = IntArray(n)
            for (i in 0 until n) {
                val a = current[2 * i]
                val b = current[2 * i + 1]
                next[i] = if (i % 2 == 0) kotlin.math.min(a, b) else kotlin.math.max(a, b)
            }
            current = next
        }
        return current[0]
    }
}
```

## Dart

```dart
class Solution {
  int minMaxGame(List<int> nums) {
    while (nums.length > 1) {
      List<int> next = [];
      for (int i = 0; i < nums.length; i += 2) {
        int idx = i ~/ 2;
        if (idx % 2 == 0) {
          next.add(nums[i] < nums[i + 1] ? nums[i] : nums[i + 1]);
        } else {
          next.add(nums[i] > nums[i + 1] ? nums[i] : nums[i + 1]);
        }
      }
      nums = next;
    }
    return nums[0];
  }
}
```

## Golang

```go
func minMaxGame(nums []int) int {
	for len(nums) > 1 {
		newLen := len(nums) / 2
		next := make([]int, newLen)
		for i := 0; i < newLen; i++ {
			a, b := nums[2*i], nums[2*i+1]
			if i%2 == 0 {
				if a < b {
					next[i] = a
				} else {
					next[i] = b
				}
			} else {
				if a > b {
					next[i] = a
				} else {
					next[i] = b
				}
			}
		}
		nums = next
	}
	return nums[0]
}
```

## Ruby

```ruby
def min_max_game(nums)
  while nums.length > 1
    next_nums = []
    nums.each_slice(2).with_index do |pair, i|
      a, b = pair
      if i.even?
        next_nums << (a < b ? a : b)
      else
        next_nums << (a > b ? a : b)
      end
    end
    nums = next_nums
  end
  nums[0]
end
```

## Scala

```scala
object Solution {
    def minMaxGame(nums: Array[Int]): Int = {
        var arr = nums
        while (arr.length > 1) {
            val n = arr.length / 2
            val next = new Array[Int](n)
            for (i <- 0 until n) {
                if ((i & 1) == 0) {
                    next(i) = math.min(arr(2 * i), arr(2 * i + 1))
                } else {
                    next(i) = math.max(arr(2 * i), arr(2 * i + 1))
                }
            }
            arr = next
        }
        arr(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_max_game(nums: Vec<i32>) -> i32 {
        let mut cur = nums;
        while cur.len() > 1 {
            let n = cur.len() / 2;
            let mut next = Vec::with_capacity(n);
            for i in 0..n {
                let a = cur[2 * i];
                let b = cur[2 * i + 1];
                if i % 2 == 0 {
                    next.push(a.min(b));
                } else {
                    next.push(a.max(b));
                }
            }
            cur = next;
        }
        cur[0]
    }
}
```

## Racket

```racket
(define/contract (min-max-game nums)
  (-> (listof exact-integer?) exact-integer?)
  (letrec
      ((next-level
        (lambda (lst)
          (let loop ((rest lst) (i 0) (acc '()))
            (if (null? rest)
                (reverse acc)
                (let* ((a (car rest))
                       (b (cadr rest))
                       (val (if (even? i) (min a b) (max a b))))
                  (loop (cddr rest) (+ i 1) (cons val acc)))))))
       (iterate
        (lambda (arr)
          (if (= (length arr) 1)
              (car arr)
              (iterate (next-level arr))))))
    (iterate nums)))
```

## Erlang

```erlang
-module(solution).
-export([min_max_game/1]).

-spec min_max_game(Nums :: [integer()]) -> integer().
min_max_game(Nums) ->
    case Nums of
        [X] -> X;
        _ -> min_max_game(process(Nums))
    end.

process(L) -> process(L, true).

process([], _) -> [];
process([A,B|Rest], true) ->
    [erlang:min(A,B) | process(Rest, false)];
process([A,B|Rest], false) ->
    [erlang:max(A,B) | process(Rest, true)].
```

## Elixir

```elixir
defmodule Solution do
  @spec min_max_game(nums :: [integer]) :: integer
  def min_max_game([single]), do: single

  def min_max_game(nums) do
    new =
      nums
      |> Enum.chunk_every(2)
      |> Enum.with_index()
      |> Enum.map(fn {[a, b], i} ->
        if rem(i, 2) == 0, do: min(a, b), else: max(a, b)
      end)

    min_max_game(new)
  end
end
```
