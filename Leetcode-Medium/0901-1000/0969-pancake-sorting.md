# 0969. Pancake Sorting

## Cpp

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        int n = arr.size();
        vector<int> res;
        for (int size = n; size > 1; --size) {
            // Find index of the maximum element within first 'size' elements
            int maxIdx = 0;
            for (int i = 1; i < size; ++i) {
                if (arr[i] > arr[maxIdx]) maxIdx = i;
            }
            if (maxIdx == size - 1) continue; // already in correct position
            // Bring the maximum to front if it's not already there
            if (maxIdx != 0) {
                res.push_back(maxIdx + 1);
                reverse(arr.begin(), arr.begin() + maxIdx + 1);
            }
            // Move it to its final position
            res.push_back(size);
            reverse(arr.begin(), arr.begin() + size);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> res = new ArrayList<>();
        int n = arr.length;
        for (int size = n; size > 1; --size) {
            // find index of the maximum value (which should be 'size')
            int maxIdx = 0;
            for (int i = 1; i < size; ++i) {
                if (arr[i] > arr[maxIdx]) {
                    maxIdx = i;
                }
            }
            if (maxIdx == size - 1) {
                continue; // already in correct position
            }
            // bring it to front if not already there
            if (maxIdx != 0) {
                flip(arr, maxIdx + 1);
                res.add(maxIdx + 1);
            }
            // move it to its final place
            flip(arr, size);
            res.add(size);
        }
        return res;
    }

    private void flip(int[] a, int k) {
        for (int i = 0, j = k - 1; i < j; ++i, --j) {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
    }
}
```

## Python

```python
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(arr)
        # work from the largest value down to 1
        for size in range(n, 0, -1):
            # find index of the current target value (size)
            idx = arr.index(size)
            if idx == size - 1:
                continue  # already in correct position
            # bring it to front if it's not already there
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
            # now flip it into its final position
            res.append(size)
            arr[:size] = reversed(arr[:size])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        # Process from largest value down to 1
        for size in range(n, 0, -1):
            # Find index of the current target value (size)
            idx = arr.index(size)
            if idx == size - 1:
                continue  # already in correct position
            # If not at front, bring it to front first
            if idx != 0:
                flips.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
            # Now flip it into its final position
            flips.append(size)
            arr[:size] = reversed(arr[:size])
        return flips
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
static void flipPrefix(int* arr, int k) {
    int i = 0, j = k - 1;
    while (i < j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        ++i;
        --j;
    }
}

/**
 * Pancake Sort
 */
int* pancakeSort(int* arr, int arrSize, int* returnSize) {
    if (arrSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    int maxFlips = 2 * arrSize;                     // upper bound on flips
    int* result = (int*)malloc(maxFlips * sizeof(int));
    int cnt = 0;

    for (int curSize = arrSize; curSize > 1; --curSize) {
        /* Find index of the value that should be placed at position curSize-1 */
        int targetVal = curSize;                     // because values are 1..n
        int idx = 0;
        while (arr[idx] != targetVal) ++idx;

        if (idx == curSize - 1) {
            continue;                               // already in correct place
        }

        /* Bring it to front if not already there */
        if (idx != 0) {
            result[cnt++] = idx + 1;
            flipPrefix(arr, idx + 1);
        }

        /* Move it from front to its final position */
        result[cnt++] = curSize;
        flipPrefix(arr, curSize);
    }

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> PancakeSort(int[] arr)
    {
        var result = new List<int>();
        int n = arr.Length;
        for (int size = n; size > 1; size--)
        {
            // Find index of the maximum element within the first 'size' elements
            int maxIdx = 0;
            for (int i = 1; i < size; i++)
            {
                if (arr[i] > arr[maxIdx])
                    maxIdx = i;
            }

            // If it's already at its correct position, continue
            if (maxIdx == size - 1)
                continue;

            // Bring the maximum element to the front if it's not already there
            if (maxIdx != 0)
            {
                result.Add(maxIdx + 1);
                Array.Reverse(arr, 0, maxIdx + 1);
            }

            // Move it from the front to its final position
            result.Add(size);
            Array.Reverse(arr, 0, size);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pancakeSort = function(arr) {
    const flips = [];
    const n = arr.length;
    
    // Helper to reverse prefix [0..end]
    const flipPrefix = (end) => {
        let i = 0, j = end;
        while (i < j) {
            const tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    };
    
    for (let size = n; size > 1; --size) {
        // locate max element within the unsorted prefix [0..size-1]
        let maxIdx = 0;
        for (let i = 1; i < size; ++i) {
            if (arr[i] > arr[maxIdx]) maxIdx = i;
        }
        if (maxIdx === size - 1) continue; // already in correct position
        
        // bring max to front if it's not already there
        if (maxIdx !== 0) {
            flipPrefix(maxIdx);
            flips.push(maxIdx + 1);
        }
        // move max from front to its final position
        flipPrefix(size - 1);
        flips.push(size);
    }
    
    return flips;
};
```

## Typescript

```typescript
function pancakeSort(arr: number[]): number[] {
    const flips: number[] = [];

    const flipPrefix = (k: number): void => {
        let i = 0, j = k - 1;
        while (i < j) {
            const temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    };

    for (let size = arr.length; size > 1; size--) {
        const idx = arr.indexOf(size);
        if (idx === size - 1) continue;

        if (idx !== 0) {
            flips.push(idx + 1);
            flipPrefix(idx + 1);
        }
        flips.push(size);
        flipPrefix(size);
    }

    return flips;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function pancakeSort($arr) {
        $n = count($arr);
        $res = [];

        // Helper to flip first k elements of the array
        $flip = function (&$a, $k) {
            $prefix = array_slice($a, 0, $k);
            $prefix = array_reverse($prefix);
            for ($i = 0; $i < $k; $i++) {
                $a[$i] = $prefix[$i];
            }
        };

        // Process from largest value down to 1
        for ($size = $n; $size > 1; $size--) {
            // Find index of the current maximum (which equals $size)
            $maxIdx = -1;
            for ($i = 0; $i < $size; $i++) {
                if ($arr[$i] == $size) {
                    $maxIdx = $i;
                    break;
                }
            }

            // If it's already at its correct position, continue
            if ($maxIdx == $size - 1) {
                continue;
            }

            // Bring it to the front if not already there
            if ($maxIdx != 0) {
                $flip($arr, $maxIdx + 1);
                $res[] = $maxIdx + 1;
            }

            // Move it to its final position
            $flip($arr, $size);
            $res[] = $size;
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func pancakeSort(_ arr: [Int]) -> [Int] {
        var a = arr
        var result: [Int] = []
        let n = a.count
        for size in stride(from: n, through: 1, by: -1) {
            guard let idx = a.firstIndex(of: size) else { continue }
            if idx == size - 1 { continue }
            if idx != 0 {
                flip(&a, k: idx + 1)
                result.append(idx + 1)
            }
            flip(&a, k: size)
            result.append(size)
        }
        return result
    }
    
    private func flip(_ arr: inout [Int], k: Int) {
        var left = 0
        var right = k - 1
        while left < right {
            arr.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pancakeSort(arr: IntArray): List<Int> {
        val result = mutableListOf<Int>()
        for (size in arr.size downTo 1) {
            var idx = -1
            for (i in 0 until size) {
                if (arr[i] == size) {
                    idx = i
                    break
                }
            }
            if (idx == size - 1) continue
            if (idx != 0) {
                reversePrefix(arr, idx + 1)
                result.add(idx + 1)
            }
            reversePrefix(arr, size)
            result.add(size)
        }
        return result
    }

    private fun reversePrefix(a: IntArray, k: Int) {
        var i = 0
        var j = k - 1
        while (i < j) {
            val tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i++
            j--
        }
    }
}
```

## Dart

```dart
class Solution {
  List<int> pancakeSort(List<int> arr) {
    List<int> result = [];
    int n = arr.length;
    for (int currSize = n; currSize > 1; --currSize) {
      // Since the array is a permutation of 1..n, the value we need to place is currSize
      int maxIdx = arr.indexOf(currSize);
      if (maxIdx == currSize - 1) continue; // already in correct position
      
      if (maxIdx != 0) {
        _flip(arr, maxIdx + 1);
        result.add(maxIdx + 1);
      }
      
      _flip(arr, currSize);
      result.add(currSize);
    }
    return result;
  }

  void _flip(List<int> a, int k) {
    int i = 0, j = k - 1;
    while (i < j) {
      int tmp = a[i];
      a[i] = a[j];
      a[j] = tmp;
      i++;
      j--;
    }
  }
}
```

## Golang

```go
func pancakeSort(arr []int) []int {
	flip := func(a []int, k int) {
		for i, j := 0, k-1; i < j; i, j = i+1, j-1 {
			a[i], a[j] = a[j], a[i]
		}
	}

	n := len(arr)
	result := make([]int, 0)

	for size := n; size > 1; size-- {
		maxIdx := 0
		for i := 1; i < size; i++ {
			if arr[i] > arr[maxIdx] {
				maxIdx = i
			}
		}
		if maxIdx == size-1 {
			continue
		}
		if maxIdx != 0 {
			flip(arr, maxIdx+1)
			result = append(result, maxIdx+1)
		}
		flip(arr, size)
		result = append(result, size)
	}
	return result
}
```

## Ruby

```ruby
def pancake_sort(arr)
  result = []
  n = arr.length
  n.downto(2) do |size|
    idx = arr.index(size)
    next if idx == size - 1
    if idx != 0
      result << idx + 1
      arr[0, idx + 1] = arr[0, idx + 1].reverse
    end
    result << size
    arr[0, size] = arr[0, size].reverse
  end
  result
end
```

## Scala

```scala
object Solution {
    def pancakeSort(arr: Array[Int]): List[Int] = {
        val n = arr.length
        val res = scala.collection.mutable.ListBuffer[Int]()
        def flip(k: Int): Unit = {
            var i = 0
            var j = k - 1
            while (i < j) {
                val tmp = arr(i)
                arr(i) = arr(j)
                arr(j) = tmp
                i += 1
                j -= 1
            }
        }
        for (currSize <- n to 2 by -1) {
            var idx = 0
            while (idx < currSize && arr(idx) != currSize) idx += 1
            if (idx != currSize - 1) {
                if (idx != 0) {
                    flip(idx + 1)
                    res += (idx + 1)
                }
                flip(currSize)
                res += currSize
            }
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn pancake_sort(arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        if n <= 1 {
            return Vec::new();
        }
        let mut a = arr.clone();
        let mut res: Vec<i32> = Vec::new();

        for size in (2..=n).rev() {
            // find index of the maximum element within first `size` elements
            let mut max_idx = 0;
            for i in 1..size {
                if a[i] > a[max_idx] {
                    max_idx = i;
                }
            }

            // already at correct position
            if max_idx == size - 1 {
                continue;
            }

            // bring the maximum to front if it's not already there
            if max_idx != 0 {
                a[0..max_idx + 1].reverse();
                res.push((max_idx + 1) as i32);
            }

            // flip it into its final position
            a[0..size].reverse();
            res.push(size as i32);
        }

        res
    }
}
```

## Racket

```racket
(define/contract (pancake-sort arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length arr)]
         [v (list->vector arr)]
         [res '()])
    ;; helper: reverse first k elements of vector v in place
    (define (flip! k)
      (let loop ([i 0] [j (- k 1)])
        (when (< i j)
          (let ([tmp (vector-ref v i)])
            (vector-set! v i (vector-ref v j))
            (vector-set! v j tmp))
          (loop (+ i 1) (- j 1)))))
    ;; main algorithm: place largest values at their correct positions
    (for ([cur (in-range n 1 -1)])               ; cur = n, n-1, ..., 2
      (define target cur)
      ;; find index of target value in current vector
      (define idx
        (let loop ((i 0))
          (if (= (vector-ref v i) target)
              i
              (loop (+ i 1)))))
      (when (not (= idx (- cur 1)))               ; not already at correct place
        (when (> idx 0)                           ; bring it to front if needed
          (flip! (+ idx 1))
          (set! res (cons (+ idx 1) res)))
        ;; move it from front to its final position
        (flip! cur)
        (set! res (cons cur res))))
    (reverse res)))
```

## Erlang

```erlang
-module(solution).
-export([pancake_sort/1]).

-spec pancake_sort(Arr :: [integer()]) -> [integer()].
pancake_sort(Arr) ->
    pancake_sort(Arr, length(Arr), []).

pancake_sort(_Arr, 0, Res) -> lists:reverse(Res);
pancake_sort(_Arr, 1, Res) -> lists:reverse(Res);
pancake_sort(Arr, CurrSize, Acc) ->
    Index = find_index(CurrSize, Arr, 0),
    if
        Index == CurrSize - 1 ->
            pancake_sort(Arr, CurrSize - 1, Acc);
        true ->
            {Arr1, Acc1} =
                case Index of
                    0 -> {Arr, Acc};
                    _ ->
                        K1 = Index + 1,
                        NewArr = flip_prefix(Arr, K1),
                        {NewArr, [K1 | Acc]}
                end,
            K2 = CurrSize,
            Arr2 = flip_prefix(Arr1, K2),
            Acc2 = [K2 | Acc1],
            pancake_sort(Arr2, CurrSize - 1, Acc2)
    end.

find_index(_Val, [], _Idx) -> -1;
find_index(Val, [Val|_], Idx) -> Idx;
find_index(Val, [_|T], Idx) -> find_index(Val, T, Idx + 1).

flip_prefix(List, K) ->
    {Prefix, Rest} = lists:split(K, List),
    lists:reverse(Prefix) ++ Rest.
```

## Elixir

```elixir
defmodule Solution do
  @spec pancake_sort(arr :: [integer]) :: [integer]
  def pancake_sort(arr) do
    n = length(arr)

    {_sorted_arr, flips_rev} =
      Enum.reduce((n)..2, {arr, []}, fn cur, {a, acc} ->
        idx = Enum.find_index(a, &(&1 == cur))

        cond do
          idx == cur - 1 ->
            {a, acc}

          true ->
            # first flip to bring current max to front if needed
            {a1, acc1} =
              if idx != 0 do
                {flip(a, idx + 1), [idx + 1 | acc]}
              else
                {a, acc}
              end

            # second flip to move it to its final position
            {flip(a1, cur), [cur | acc1]}
        end
      end)

    Enum.reverse(flips_rev)
  end

  defp flip(list, k) do
    {prefix, suffix} = Enum.split(list, k)
    Enum.concat(Enum.reverse(prefix), suffix)
  end
end
```
