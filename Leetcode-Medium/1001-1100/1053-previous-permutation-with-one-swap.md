# 1053. Previous Permutation With One Swap

## Cpp

```cpp
class Solution {
public:
    vector<int> prevPermOpt1(vector<int>& arr) {
        int n = arr.size();
        // Find the first index from right where arr[i] > arr[i+1]
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) --i;
        if (i < 0) return arr; // already smallest permutation
        
        // Find the largest value less than arr[i] in suffix
        int maxLess = -1;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[i] && arr[j] > maxLess) {
                maxLess = arr[j];
            }
        }
        // Find the leftmost occurrence of maxLess in suffix and swap
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] == maxLess) {
                swap(arr[i], arr[j]);
                break;
            }
        }
        return arr;
    }
};
```

## Java

```java
class Solution {
    public int[] prevPermOpt1(int[] arr) {
        int n = arr.length;
        // Find the first index from the right where arr[i] > arr[i + 1]
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            i--;
        }
        if (i < 0) {
            return arr; // already smallest permutation
        }

        // Find the largest value less than arr[i] in the suffix
        int maxLess = -1;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[i] && arr[j] > maxLess) {
                maxLess = arr[j];
            }
        }

        // Find the rightmost occurrence of that value
        int idx = -1;
        for (int j = n - 1; j > i; --j) {
            if (arr[j] == maxLess) {
                idx = j;
                break;
            }
        }

        // Swap and return
        int tmp = arr[i];
        arr[i] = arr[idx];
        arr[idx] = tmp;
        return arr;
    }
}
```

## Python

```python
class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        # Find the first index i from right where arr[i] > arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr

        # Find the largest value less than arr[i] in suffix
        max_less = -1
        for j in range(i + 1, n):
            if arr[j] < arr[i] and arr[j] > max_less:
                max_less = arr[j]

        # Find the leftmost index j where arr[j] == max_less
        for j in range(i + 1, n):
            if arr[j] == max_less:
                arr[i], arr[j] = arr[j], arr[i]
                break

        return arr
```

## Python3

```python
from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 1
        while i > 0 and arr[i - 1] <= arr[i]:
            i -= 1
        if i == 0:
            return arr
        pivot = i - 1

        max_less = -1
        candidate = -1
        for j in range(i, n):
            if arr[j] < arr[pivot]:
                if arr[j] > max_less:
                    max_less = arr[j]
                    candidate = j
                elif arr[j] == max_less:
                    candidate = j  # take rightmost occurrence

        arr[pivot], arr[candidate] = arr[candidate], arr[pivot]
        return arr
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prevPermOpt1(int* arr, int arrSize, int* returnSize) {
    int* res = (int*)malloc(sizeof(int) * arrSize);
    for (int i = 0; i < arrSize; ++i) {
        res[i] = arr[i];
    }
    *returnSize = arrSize;

    // Find the first index from the right where res[i] > res[i+1]
    int i = arrSize - 2;
    while (i >= 0 && res[i] <= res[i + 1]) {
        --i;
    }
    if (i < 0) {               // Already the smallest permutation
        return res;
    }

    // Find the largest value less than res[i] to its right
    int maxLess = -1;
    for (int k = i + 1; k < arrSize; ++k) {
        if (res[k] < res[i] && res[k] > maxLess) {
            maxLess = res[k];
        }
    }

    // Among those with value == maxLess, pick the leftmost occurrence
    int j = -1;
    for (int k = i + 1; k < arrSize; ++k) {
        if (res[k] == maxLess) {
            j = k;
            break;
        }
    }

    // Perform the swap
    int tmp = res[i];
    res[i] = res[j];
    res[j] = tmp;

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] PrevPermOpt1(int[] arr) {
        int n = arr.Length;
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            i--;
        }
        if (i < 0) return arr;

        int j = n - 1;
        while (j > i && (arr[j] >= arr[i] || (j > 0 && arr[j] == arr[j - 1]))) {
            j--;
        }

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        return arr;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var prevPermOpt1 = function(arr) {
    const n = arr.length;
    let i = n - 2;
    while (i >= 0 && arr[i] <= arr[i + 1]) {
        i--;
    }
    if (i < 0) return arr; // already smallest
    
    let maxLess = -Infinity;
    let j = -1;
    for (let k = i + 1; k < n; ++k) {
        if (arr[k] < arr[i]) {
            if (arr[k] > maxLess) {
                maxLess = arr[k];
                j = k;
            }
            // if equal to current maxLess, keep earlier index (leftmost), so do nothing
        }
    }
    
    // swap i and j
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    
    return arr;
};
```

## Typescript

```typescript
function prevPermOpt1(arr: number[]): number[] {
    const n = arr.length;
    let i = n - 1;
    while (i > 0 && arr[i - 1] <= arr[i]) {
        i--;
    }
    if (i === 0) return arr; // already smallest permutation

    const leftIdx = i - 1;

    // Find index of the largest element less than arr[leftIdx]
    let candIdx = -1;
    for (let j = i; j < n; ++j) {
        if (arr[j] < arr[leftIdx]) {
            if (candIdx === -1 || arr[j] > arr[candIdx]) {
                candIdx = j;
            }
        }
    }

    // Among duplicates of the chosen value, pick the leftmost occurrence
    const targetVal = arr[candIdx];
    for (let j = i; j < candIdx; ++j) {
        if (arr[j] === targetVal) {
            candIdx = j;
            break;
        }
    }

    // Swap and return
    [arr[leftIdx], arr[candIdx]] = [arr[candIdx], arr[leftIdx]];
    return arr;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function prevPermOpt1($arr) {
        $n = count($arr);
        // Find the first index from right where arr[i] > arr[i+1]
        $i = $n - 2;
        while ($i >= 0 && $arr[$i] <= $arr[$i + 1]) {
            $i--;
        }
        if ($i < 0) {
            return $arr; // already the smallest permutation
        }

        // Find the largest element smaller than arr[i] to its right
        $j = $i + 1;
        for ($k = $i + 1; $k < $n; $k++) {
            if ($arr[$k] < $arr[$i] && $arr[$k] > $arr[$j]) {
                $j = $k;
            }
        }

        // If there are duplicates of the chosen value, pick the leftmost one
        while ($j > $i + 1 && $arr[$j] == $arr[$j - 1]) {
            $j--;
        }

        // Swap arr[i] and arr[j]
        $temp = $arr[$i];
        $arr[$i] = $arr[$j];
        $arr[$j] = $temp;

        return $arr;
    }
}
```

## Swift

```swift
class Solution {
    func prevPermOpt1(_ arr: [Int]) -> [Int] {
        var a = arr
        let n = a.count
        if n < 2 { return a }
        
        var i = n - 1
        while i > 0 && a[i - 1] <= a[i] {
            i -= 1
        }
        if i == 0 { return a } // already the smallest permutation
        
        var maxLess = -1
        var idx = -1
        for j in i..<n {
            if a[j] < a[i - 1] && a[j] > maxLess {
                maxLess = a[j]
                idx = j
            }
        }
        
        // Perform the swap
        a.swapAt(i - 1, idx)
        return a
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun prevPermOpt1(arr: IntArray): IntArray {
        val n = arr.size
        var i = n - 2
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            i--
        }
        if (i < 0) return arr

        var maxLess = -1
        for (j in i + 1 until n) {
            if (arr[j] < arr[i] && arr[j] > maxLess) {
                maxLess = arr[j]
            }
        }

        var idx = -1
        for (j in i + 1 until n) {
            if (arr[j] == maxLess) {
                idx = j
                break
            }
        }

        val tmp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = tmp
        return arr
    }
}
```

## Dart

```dart
class Solution {
  List<int> prevPermOpt1(List<int> arr) {
    int n = arr.length;
    int i = n - 2;
    while (i >= 0 && arr[i] <= arr[i + 1]) {
      i--;
    }
    if (i < 0) return arr;

    int maxLess = -1;
    for (int k = i + 1; k < n; k++) {
      if (arr[k] < arr[i] && arr[k] > maxLess) {
        maxLess = arr[k];
      }
    }

    int j = -1;
    for (int k = i + 1; k < n; k++) {
      if (arr[k] == maxLess) {
        j = k;
        break;
      }
    }

    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;

    return arr;
  }
}
```

## Golang

```go
func prevPermOpt1(arr []int) []int {
	n := len(arr)
	// Find the first index from the right where arr[i] > arr[i+1]
	i := n - 2
	for i >= 0 && arr[i] <= arr[i+1] {
		i--
	}
	if i < 0 {
		return arr
	}

	// Find the largest value less than arr[i] in the suffix
	maxLess := -1
	j := i + 1
	for k := i + 1; k < n; k++ {
		if arr[k] < arr[i] && arr[k] > maxLess {
			maxLess = arr[k]
			j = k
		}
	}
	// If there are duplicates of the chosen value, pick the leftmost one
	for j-1 > i && arr[j-1] == arr[j] {
		j--
	}

	// Swap
	arr[i], arr[j] = arr[j], arr[i]
	return arr
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def prev_perm_opt1(arr)
  n = arr.length
  i = n - 2
  while i >= 0 && arr[i] <= arr[i + 1]
    i -= 1
  end
  return arr if i < 0

  best_val = -1
  best_idx = -1
  (i + 1...n).each do |j|
    if arr[j] < arr[i] && arr[j] > best_val
      best_val = arr[j]
      best_idx = j
    end
  end

  if best_idx != -1
    # ensure leftmost occurrence of best_val after i
    (i + 1...n).each do |j|
      if arr[j] == best_val
        best_idx = j
        break
      end
    end
    arr[i], arr[best_idx] = arr[best_idx], arr[i]
  end

  arr
end
```

## Scala

```scala
object Solution {
    def prevPermOpt1(arr: Array[Int]): Array[Int] = {
        val n = arr.length
        var i = n - 1
        while (i > 0 && arr(i - 1) <= arr(i)) {
            i -= 1
        }
        if (i == 0) return arr

        val idx = i - 1
        var maxLess = -1
        var jIdx = -1
        var j = idx + 1
        while (j < n) {
            if (arr(j) < arr(idx)) {
                if (arr(j) > maxLess) {
                    maxLess = arr(j)
                    jIdx = j
                }
            }
            j += 1
        }

        val tmp = arr(idx)
        arr(idx) = arr(jIdx)
        arr(jIdx) = tmp
        arr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn prev_perm_opt1(mut arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        if n < 2 {
            return arr;
        }
        // Find the first index i from the right where arr[i] > arr[i+1]
        let mut i_opt = None;
        for i in (0..n - 1).rev() {
            if arr[i] > arr[i + 1] {
                i_opt = Some(i);
                break;
            }
        }
        if let Some(i) = i_opt {
            // Find the largest value less than arr[i] in the suffix,
            // and among equal values choose the leftmost index.
            let mut best_j: Option<usize> = None;
            let mut best_val = std::i32::MIN;
            for j in i + 1..n {
                if arr[j] < arr[i] && arr[j] > best_val {
                    best_val = arr[j];
                    best_j = Some(j);
                }
            }
            if let Some(j) = best_j {
                arr.swap(i, j);
            }
        }
        arr
    }
}
```

## Racket

```racket
(define/contract (prev-perm-opt1 arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length arr))
         (vec (list->vector arr)))
    (let loop-i ((i (- n 2)))
      (if (< i 0)
          (vector->list vec) ; no decreasing point, return original
          (if (> (vector-ref vec i) (vector-ref vec (+ i 1)))
              (let* ((target (vector-ref vec i))
                     (candidate-index -1)
                     (candidate-value -1))
                (for ([j (in-range (+ i 1) n)])
                  (let ((val (vector-ref vec j)))
                    (when (< val target)
                      (cond [(> val candidate-value)
                             (set! candidate-value val)
                             (set! candidate-index j)]
                            [(= val candidate-value)
                             ;; keep earlier index (leftmost), do nothing
                             ]))))
                (if (= candidate-index -1)
                    (vector->list vec) ; should not happen
                    (begin
                      (let ((temp (vector-ref vec i)))
                        (vector-set! vec i (vector-ref vec candidate-index))
                        (vector-set! vec candidate-index temp))
                      (vector->list vec))))
              (loop-i (- i 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([prev_perm_opt1/1]).

-spec prev_perm_opt1(Arr :: [integer()]) -> [integer()].
prev_perm_opt1(Arr) ->
    Tuple = list_to_tuple(Arr),
    N = tuple_size(Tuple),
    I = find_i(N - 1, Tuple),
    case I of
        0 -> Arr;
        _ ->
            Ai = element(I, Tuple),
            {J, _} = find_j(I + 1, N, Ai, Tuple, -1, 0),
            NewTuple = swap(Tuple, I, J),
            tuple_to_list(NewTuple)
    end.

find_i(Index, Tuple) when Index >= 1 ->
    if element(Index, Tuple) > element(Index + 1, Tuple) ->
            Index;
       true ->
            find_i(Index - 1, Tuple)
    end;
find_i(_, _) -> 0.

find_j(K, N, Ai, Tuple, MaxVal, JIdx) when K =< N ->
    Val = element(K, Tuple),
    if Val < Ai andalso Val > MaxVal ->
            find_j(K + 1, N, Ai, Tuple, Val, K);
       true ->
            find_j(K + 1, N, Ai, Tuple, MaxVal, JIdx)
    end;
find_j(_, _, _, _, MaxVal, JIdx) -> {JIdx, MaxVal}.

swap(Tuple, I, J) ->
    Vi = element(I, Tuple),
    Vj = element(J, Tuple),
    Temp = setelement(I, Tuple, Vj),
    setelement(J, Temp, Vi).
```

## Elixir

```elixir
defmodule Solution do
  @spec prev_perm_opt1(arr :: [integer]) :: [integer]
  def prev_perm_opt1(arr) do
    tup = List.to_tuple(arr)
    n = tuple_size(tup)

    # Find the first index i from the right where arr[i] > arr[i+1]
    i =
      Enum.reduce_while(Enum.to_list(0..max(n - 2, 0)) |> Enum.reverse(), -1, fn idx, _acc ->
        if elem(tup, idx) > elem(tup, idx + 1) do
          {:halt, idx}
        else
          {:cont, -1}
        end
      end)

    if i == -1 do
      arr
    else
      # Find the index j (> i) with the largest value less than arr[i]
      {best_val, best_idx} =
        Enum.reduce((i + 1)..(n - 1), {-1, -1}, fn idx, {bval, bidx} ->
          val = elem(tup, idx)

          if val < elem(tup, i) and val > bval do
            {val, idx}
          else
            {bval, bidx}
          end
        end)

      # Perform the swap
      val_i = elem(tup, i)
      val_j = elem(tup, best_idx)

      new_tup =
        tup
        |> put_elem(i, val_j)
        |> put_elem(best_idx, val_i)

      Tuple.to_list(new_tup)
    end
  end
end
```
