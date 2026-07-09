# 1646. Get Maximum in Generated Array

## Cpp

```cpp
class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        vector<int> nums(n + 1, 0);
        nums[0] = 0;
        nums[1] = 1;
        int maxVal = 1;
        for (int i = 1; 2 * i <= n; ++i) {
            if (2 * i <= n) {
                nums[2 * i] = nums[i];
                maxVal = max(maxVal, nums[2 * i]);
            }
            if (2 * i + 1 <= n) {
                nums[2 * i + 1] = nums[i] + nums[i + 1];
                maxVal = max(maxVal, nums[2 * i + 1]);
            }
        }
        return maxVal;
    }
};
```

## Java

```java
class Solution {
    public int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        int[] nums = new int[n + 1];
        nums[0] = 0;
        nums[1] = 1;
        int max = 1;
        for (int i = 1; 2 * i <= n; i++) {
            int evenIdx = 2 * i;
            nums[evenIdx] = nums[i];
            if (nums[evenIdx] > max) max = nums[evenIdx];
            int oddIdx = evenIdx + 1;
            if (oddIdx <= n) {
                nums[oddIdx] = nums[i] + nums[i + 1];
                if (nums[oddIdx] > max) max = nums[oddIdx];
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                half = i // 2
                nums[i] = nums[half] + nums[half + 1]
            if nums[i] > max_val:
                max_val = nums[i]
        return max_val
```

## Python3

```python
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 1
        for i in range(1, n // 2 + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
                if nums[2 * i] > max_val:
                    max_val = nums[2 * i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                if nums[2 * i + 1] > max_val:
                    max_val = nums[2 * i + 1]
        return max_val
```

## C

```c
int getMaximumGenerated(int n) {
    if (n == 0) return 0;
    int nums[101] = {0};
    nums[0] = 0;
    nums[1] = 1;
    int maxv = 1;
    for (int i = 2; i <= n; ++i) {
        if ((i & 1) == 0) {
            nums[i] = nums[i >> 1];
        } else {
            int k = i >> 1;
            nums[i] = nums[k] + nums[k + 1];
        }
        if (nums[i] > maxv) maxv = nums[i];
    }
    return maxv;
}
```

## Csharp

```csharp
public class Solution
{
    public int GetMaximumGenerated(int n)
    {
        if (n == 0) return 0;
        int[] nums = new int[n + 1];
        nums[0] = 0;
        nums[1] = 1;
        int maxVal = 1;

        for (int i = 2; i <= n; i++)
        {
            if ((i & 1) == 0)
                nums[i] = nums[i >> 1];
            else
                nums[i] = nums[i >> 1] + nums[(i >> 1) + 1];

            if (nums[i] > maxVal) maxVal = nums[i];
        }

        return maxVal;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if (n === 0) return 0;
    const nums = new Array(n + 1).fill(0);
    nums[0] = 0;
    nums[1] = 1;
    let maxVal = 1;
    for (let i = 2; i <= n; i++) {
        if ((i & 1) === 0) { // even
            nums[i] = nums[i >> 1];
        } else { // odd
            const k = i >> 1; // floor(i/2)
            nums[i] = nums[k] + nums[k + 1];
        }
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    return maxVal;
};
```

## Typescript

```typescript
function getMaximumGenerated(n: number): number {
    if (n === 0) return 0;
    const nums = new Array<number>(n + 1);
    nums[0] = 0;
    nums[1] = 1;
    let maxVal = 1;
    for (let i = 1; 2 * i <= n; i++) {
        const evenIdx = 2 * i;
        nums[evenIdx] = nums[i];
        if (nums[evenIdx] > maxVal) maxVal = nums[evenIdx];
        const oddIdx = evenIdx + 1;
        if (oddIdx <= n) {
            nums[oddIdx] = nums[i] + nums[i + 1];
            if (nums[oddIdx] > maxVal) maxVal = nums[oddIdx];
        }
    }
    return maxVal;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function getMaximumGenerated($n) {
        if ($n == 0) return 0;
        $nums = array_fill(0, $n + 1, 0);
        $nums[0] = 0;
        $nums[1] = 1;
        $maxVal = 1;
        for ($i = 1; $i * 2 <= $n; $i++) {
            $even = $i * 2;
            $nums[$even] = $nums[$i];
            if ($nums[$even] > $maxVal) $maxVal = $nums[$even];
            $odd = $even + 1;
            if ($odd <= $n) {
                $nums[$odd] = $nums[$i] + $nums[$i + 1];
                if ($nums[$odd] > $maxVal) $maxVal = $nums[$odd];
            }
        }
        return $maxVal;
    }
}
```

## Swift

```swift
class Solution {
    func getMaximumGenerated(_ n: Int) -> Int {
        if n == 0 { return 0 }
        var nums = [Int](repeating: 0, count: n + 1)
        nums[0] = 0
        nums[1] = 1
        var maxVal = 1
        var i = 1
        while i * 2 <= n {
            let evenIdx = i * 2
            nums[evenIdx] = nums[i]
            if nums[evenIdx] > maxVal { maxVal = nums[evenIdx] }
            let oddIdx = i * 2 + 1
            if oddIdx <= n {
                nums[oddIdx] = nums[i] + nums[i + 1]
                if nums[oddIdx] > maxVal { maxVal = nums[oddIdx] }
            }
            i += 1
        }
        return maxVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaximumGenerated(n: Int): Int {
        if (n == 0) return 0
        val nums = IntArray(n + 1)
        nums[0] = 0
        nums[1] = 1
        var maxVal = 1
        for (i in 1..n / 2) {
            val evenIdx = i * 2
            if (evenIdx <= n) {
                nums[evenIdx] = nums[i]
                if (nums[evenIdx] > maxVal) maxVal = nums[evenIdx]
            }
            val oddIdx = i * 2 + 1
            if (oddIdx <= n) {
                nums[oddIdx] = nums[i] + nums[i + 1]
                if (nums[oddIdx] > maxVal) maxVal = nums[oddIdx]
            }
        }
        return maxVal
    }
}
```

## Dart

```dart
class Solution {
  int getMaximumGenerated(int n) {
    if (n == 0) return 0;
    List<int> nums = List.filled(n + 1, 0);
    nums[0] = 0;
    nums[1] = 1;
    int maxVal = 1;
    for (int i = 1; i * 2 <= n; ++i) {
      int evenIdx = i * 2;
      nums[evenIdx] = nums[i];
      if (nums[evenIdx] > maxVal) maxVal = nums[evenIdx];
      int oddIdx = evenIdx + 1;
      if (oddIdx <= n) {
        nums[oddIdx] = nums[i] + nums[i + 1];
        if (nums[oddIdx] > maxVal) maxVal = nums[oddIdx];
      }
    }
    return maxVal;
  }
}
```

## Golang

```go
func getMaximumGenerated(n int) int {
	if n == 0 {
		return 0
	}
	nums := make([]int, n+1)
	nums[0] = 0
	nums[1] = 1
	maxVal := 1
	for i := 1; 2*i <= n; i++ {
		nums[2*i] = nums[i]
		if nums[2*i] > maxVal {
			maxVal = nums[2*i]
		}
		if 2*i+1 <= n {
			nums[2*i+1] = nums[i] + nums[i+1]
			if nums[2*i+1] > maxVal {
				maxVal = nums[2*i+1]
			}
		}
	}
	return maxVal
}
```

## Ruby

```ruby
def get_maximum_generated(n)
  return 0 if n == 0
  nums = Array.new(n + 1, 0)
  nums[0] = 0
  nums[1] = 1
  (2..n).each do |i|
    if i.even?
      nums[i] = nums[i / 2]
    else
      j = (i - 1) / 2
      nums[i] = nums[j] + nums[j + 1]
    end
  end
  nums.max
end
```

## Scala

```scala
object Solution {
    def getMaximumGenerated(n: Int): Int = {
        if (n == 0) return 0
        val nums = new Array[Int](n + 1)
        nums(0) = 0
        nums(1) = 1
        var maxVal = 1
        for (i <- 1 to n / 2) {
            val evenIdx = i * 2
            if (evenIdx <= n) {
                nums(evenIdx) = nums(i)
                if (nums(evenIdx) > maxVal) maxVal = nums(evenIdx)
            }
            val oddIdx = i * 2 + 1
            if (oddIdx <= n) {
                nums(oddIdx) = nums(i) + nums(i + 1)
                if (nums(oddIdx) > maxVal) maxVal = nums(oddIdx)
            }
        }
        maxVal
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let n_usize = n as usize;
        let mut nums = vec![0i32; n_usize + 1];
        nums[0] = 0;
        if n_usize >= 1 {
            nums[1] = 1;
        }
        let mut max_val = 1;
        for i in 1..=n_usize / 2 {
            let idx = i * 2;
            if idx <= n_usize {
                nums[idx] = nums[i];
                if nums[idx] > max_val {
                    max_val = nums[idx];
                }
            }
            if idx + 1 <= n_usize {
                nums[idx + 1] = nums[i] + nums[i + 1];
                if nums[idx + 1] > max_val {
                    max_val = nums[idx + 1];
                }
            }
        }
        max_val
    }
}
```

## Racket

```racket
(define/contract (get-maximum-generated n)
  (-> exact-integer? exact-integer?)
  (let* ((size (+ n 1))
         (arr (make-vector size 0)))
    (when (> size 1) (vector-set! arr 1 1))
    (for ([i (in-range 1 size)])
      (define idx (* i 2))
      (when (< idx size)
        (vector-set! arr idx (vector-ref arr i)))
      (define idx2 (+ idx 1))
      (when (< idx2 size)
        (vector-set! arr idx2
                     (+ (vector-ref arr i) (vector-ref arr (+ i 1))))))
    (let loop ((i (- size 1)) (mx 0))
      (if (< i 0)
          mx
          (loop (- i 1) (max mx (vector-ref arr i)))))))
```

## Erlang

```erlang
-module(solution).
-export([get_maximum_generated/1]).

-spec get_maximum_generated(N :: integer()) -> integer().
get_maximum_generated(N) when N >= 0 ->
    Arr0 = array:new(N + 1, {default, 0}),
    Arr1 = case N >= 1 of
               true -> array:set(1, 1, Arr0);
               false -> Arr0
           end,
    ArrFinal = fill(1, N, Arr1),
    max_val(0, N, ArrFinal, 0).

fill(I, N, Arr) when I > N ->
    Arr;
fill(I, N, Arr) ->
    case 2 * I =< N of
        true ->
            ValI = array:get(I, Arr),
            Arr1 = array:set(2 * I, ValI, Arr),
            Arr2 = if (2 * I + 1) =< N ->
                       ValIp1 = array:get(I + 1, Arr1),
                       array:set(2 * I + 1, ValI + ValIp1, Arr1)
                   else
                       Arr1
                   end,
            fill(I + 1, N, Arr2);
        false ->
            fill(I + 1, N, Arr)
    end.

max_val(Index, N, Arr, Max) when Index > N ->
    Max;
max_val(Index, N, Arr, Max) ->
    Val = array:get(Index, Arr),
    NewMax = if Val > Max -> Val; true -> Max end,
    max_val(Index + 1, N, Arr, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_maximum_generated(n :: integer) :: integer
  def get_maximum_generated(n) do
    if n == 0 do
      0
    else
      arr = :array.new(n + 1, default: 0)
      arr = :array.set(0, 0, arr)
      arr = :array.set(1, 1, arr)

      {_arr, max_val} =
        Enum.reduce(1..n, {arr, 1}, fn i, {a, cur_max} ->
          left = 2 * i

          {a, cur_max} =
            if left <= n do
              val = :array.get(i, a)
              a = :array.set(left, val, a)
              new_max = if val > cur_max, do: val, else: cur_max
              {a, new_max}
            else
              {a, cur_max}
            end

          right = left + 1

          if right <= n do
            val = :array.get(i, a) + :array.get(i + 1, a)
            a = :array.set(right, val, a)
            new_max = if val > cur_max, do: val, else: cur_max
            {a, new_max}
          else
            {a, cur_max}
          end
        end)

      max_val
    end
  end
end
```
