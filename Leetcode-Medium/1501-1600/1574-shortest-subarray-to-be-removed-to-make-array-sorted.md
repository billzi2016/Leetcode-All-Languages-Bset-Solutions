# 1574. Shortest Subarray to be Removed to Make Array Sorted

## Cpp

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(std::vector<int>& arr) {
        int n = arr.size();
        int left = 0;
        while (left + 1 < n && arr[left] <= arr[left + 1]) ++left;
        if (left == n - 1) return 0; // already non-decreasing
        
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) --right;
        
        int ans = std::min(n - left - 1, right); // remove suffix or prefix
        
        int i = 0, j = right;
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                ans = std::min(ans, j - i - 1);
                ++i;
            } else {
                ++j;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;
        int left = 0;
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++;
        }
        if (left == n - 1) return 0; // already non-decreasing

        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--;
        }

        int ans = Math.min(n - left - 1, right); // remove suffix or prefix

        for (int i = 0; i <= left; i++) {
            while (right < n && arr[i] > arr[right]) {
                right++;
            }
            ans = Math.min(ans, right - i - 1);
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # longest non-decreasing prefix
        i = 0
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        if i == n - 1:
            return 0

        # longest non-decreasing suffix
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1

        # remove either prefix after i or suffix before j
        ans = min(n - (i + 1), j)

        left, right = 0, j
        while left <= i and right < n:
            if arr[left] <= arr[right]:
                ans = min(ans, right - left - 1)
                left += 1
            else:
                right += 1

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # longest non-decreasing prefix
        left = 0
        while left + 1 < n and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0

        # longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # remove either prefix after left or suffix before right
        ans = min(n - (left + 1), right)

        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
```

## C

```c
int findLengthOfShortestSubarray(int* arr, int arrSize) {
    if (arrSize <= 1) return 0;
    
    int n = arrSize;
    int left = 0;
    while (left + 1 < n && arr[left] <= arr[left + 1]) {
        left++;
    }
    if (left == n - 1) return 0; // already non‑decreasing
    
    int right = n - 1;
    while (right > 0 && arr[right - 1] <= arr[right]) {
        right--;
    }
    
    int ans = n; // upper bound
    // remove suffix after left or prefix before right
    if (n - left - 1 < ans) ans = n - left - 1;
    if (right < ans) ans = right;
    
    int i = 0, j = right;
    while (i <= left && j < n) {
        if (arr[i] <= arr[j]) {
            int cur = j - i - 1;
            if (cur < ans) ans = cur;
            i++;
        } else {
            j++;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLengthOfShortestSubarray(int[] arr) {
        int n = arr.Length;
        int left = 0;
        while (left + 1 < n && arr[left] <= arr[left + 1]) left++;
        if (left == n - 1) return 0;

        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) right--;

        int ans = Math.Min(n - left - 1, right);
        int j = right;
        for (int i = 0; i <= left; i++) {
            while (j < n && arr[j] < arr[i]) j++;
            ans = Math.Min(ans, j - i - 1);
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findLengthOfShortestSubarray = function(arr) {
    const n = arr.length;
    // longest non-decreasing prefix
    let left = 0;
    while (left + 1 < n && arr[left] <= arr[left + 1]) {
        left++;
    }
    if (left === n - 1) return 0; // already sorted

    // longest non-decreasing suffix
    let right = n - 1;
    while (right > 0 && arr[right - 1] <= arr[right]) {
        right--;
    }

    // remove either the tail after prefix or the head before suffix
    let ans = Math.min(n - left - 1, right);

    // try to merge prefix [0..i] with suffix [right..n-1]
    for (let i = 0; i <= left; i++) {
        while (right < n && arr[i] > arr[right]) {
            right++;
        }
        ans = Math.min(ans, right - i - 1);
    }

    return ans;
};
```

## Typescript

```typescript
function findLengthOfShortestSubarray(arr: number[]): number {
    const n = arr.length;
    // Find longest non-decreasing prefix
    let left = 0;
    while (left + 1 < n && arr[left] <= arr[left + 1]) {
        left++;
    }
    // Already sorted
    if (left === n - 1) return 0;

    // Find longest non-decreasing suffix
    let right = n - 1;
    while (right > 0 && arr[right - 1] <= arr[right]) {
        right--;
    }

    // Remove either prefix after left or suffix before right
    let ans = Math.min(n - left - 1, right);

    // Try to merge prefix [0..i] with suffix [j..n-1]
    let i = 0;
    let j = right;
    while (i <= left && j < n) {
        if (arr[i] <= arr[j]) {
            ans = Math.min(ans, j - i - 1);
            i++;
        } else {
            j++;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLengthOfShortestSubarray($arr) {
        $n = count($arr);
        if ($n <= 1) return 0;

        // longest non-decreasing prefix
        $left = 0;
        while ($left + 1 < $n && $arr[$left] <= $arr[$left + 1]) {
            $left++;
        }
        if ($left == $n - 1) return 0; // already sorted

        // longest non-decreasing suffix
        $right = $n - 1;
        while ($right > 0 && $arr[$right - 1] <= $arr[$right]) {
            $right--;
        }

        // remove either prefix after left or suffix before right
        $ans = min($n - $left - 1, $right);

        $i = 0;
        $j = $right;
        while ($i <= $left && $j < $n) {
            if ($arr[$i] <= $arr[$j]) {
                // keep arr[0..i] and arr[j..end]
                $ans = min($ans, $j - $i - 1);
                $i++;
            } else {
                $j++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findLengthOfShortestSubarray(_ arr: [Int]) -> Int {
        let n = arr.count
        var left = 0
        while left + 1 < n && arr[left] <= arr[left + 1] {
            left += 1
        }
        if left == n - 1 { return 0 } // already non-decreasing
        
        var right = n - 1
        while right > 0 && arr[right - 1] <= arr[right] {
            right -= 1
        }
        
        var ans = min(n - left - 1, right) // remove suffix or prefix entirely
        
        var i = 0
        var j = right
        while i <= left && j < n {
            if arr[i] <= arr[j] {
                ans = min(ans, j - i - 1)
                i += 1
            } else {
                j += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLengthOfShortestSubarray(arr: IntArray): Int {
        val n = arr.size
        var left = 0
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++
        }
        if (left == n - 1) return 0

        var right = n - 1
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--
        }

        var ans = kotlin.math.min(right, n - left - 1)

        var i = 0
        var j = right
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                ans = kotlin.math.min(ans, j - i - 1)
                i++
            } else {
                j++
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findLengthOfShortestSubarray(List<int> arr) {
    int n = arr.length;
    int left = 0;
    while (left + 1 < n && arr[left] <= arr[left + 1]) {
      left++;
    }
    if (left == n - 1) return 0;

    int right = n - 1;
    while (right > 0 && arr[right - 1] <= arr[right]) {
      right--;
    }

    int ans = (n - (left + 1)).clamp(0, n);
    if (right < ans) ans = right;

    int j = right;
    for (int i = 0; i <= left; i++) {
      while (j < n && arr[i] > arr[j]) {
        j++;
      }
      int removedLength = j - i - 1;
      if (removedLength < ans) ans = removedLength;
    }

    return ans;
  }
}
```

## Golang

```go
func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
	if n <= 2 {
		return 0
	}
	// Find longest non-decreasing prefix
	left := 0
	for left+1 < n && arr[left] <= arr[left+1] {
		left++
	}
	if left == n-1 { // already sorted
		return 0
	}
	// Find longest non-decreasing suffix
	right := n - 1
	for right > 0 && arr[right-1] <= arr[right] {
		right--
	}
	// Remove either prefix after left or suffix before right
	ans := min(n-left-1, right)

	j := right
	for i := 0; i <= left; i++ {
		for j < n && arr[j] < arr[i] {
			j++
		}
		if j-i-1 < ans {
			ans = j - i - 1
		}
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def find_length_of_shortest_subarray(arr)
  n = arr.length
  # Find longest non‑decreasing prefix
  left = 0
  while left + 1 < n && arr[left] <= arr[left + 1]
    left += 1
  end
  return 0 if left == n - 1

  # Find longest non‑decreasing suffix start index
  right = n - 1
  while right > 0 && arr[right - 1] <= arr[right]
    right -= 1
  end

  # Remove either prefix up to right-1 or suffix after left
  ans = [right, n - left - 1].min

  i = 0
  j = right
  while i <= left && j < n
    if arr[i] <= arr[j]
      ans = [ans, j - i - 1].min
      i += 1
    else
      j += 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def findLengthOfShortestSubarray(arr: Array[Int]): Int = {
        val n = arr.length
        var left = 0
        while (left + 1 < n && arr(left) <= arr(left + 1)) {
            left += 1
        }
        if (left == n - 1) return 0

        var right = n - 1
        while (right > 0 && arr(right - 1) <= arr(right)) {
            right -= 1
        }

        var ans = Math.min(n - (left + 1), right)

        var i = 0
        var j = right
        while (i <= left && j < n) {
            if (arr(i) <= arr(j)) {
                ans = Math.min(ans, j - i - 1)
                i += 1
            } else {
                j += 1
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_length_of_shortest_subarray(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n <= 1 {
            return 0;
        }

        // longest non-decreasing prefix
        let mut left = 0usize;
        while left + 1 < n && arr[left] <= arr[left + 1] {
            left += 1;
        }
        if left == n - 1 {
            return 0; // already sorted
        }

        // longest non-decreasing suffix
        let mut right = n - 1;
        while right > 0 && arr[right - 1] <= arr[right] {
            right -= 1;
        }

        // initial answer: remove prefix after left or suffix before right
        let mut ans = std::cmp::min(n - (left + 1), right) as i32;

        // try to merge prefix [0..i] with suffix [j..n)
        let mut i = 0usize;
        let mut j = right;
        while i <= left && j < n {
            if arr[i] <= arr[j] {
                let remove_len = (j - i - 1) as i32;
                if remove_len < ans {
                    ans = remove_len;
                }
                i += 1;
            } else {
                j += 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-length-of-shortest-subarray arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector arr))
         (n   (vector-length vec)))
    (if (= n 0)
        0
        (let* ((l (let loop ((i 0))
                    (if (and (< i (- n 1))
                             (<= (vector-ref vec i)
                                 (vector-ref vec (+ i 1))))
                        (loop (+ i 1))
                        i)))
               (r (let loop ((j (- n 1)))
                    (if (and (> j 0)
                             (<= (vector-ref vec (- j 1))
                                 (vector-ref vec j)))
                        (loop (- j 1))
                        j))))
          (if (= l (- n 1))                ; already non‑decreasing
              0
              (let* ((initial-ans (min (- n (+ l 1)) r))
                     (final-ans
                      (let loop3 ((i 0) (right r) (ans initial-ans))
                        (if (> i l)
                            ans
                            (let ((new-right
                                   (let inner ((rr right))
                                     (if (and (< rr n)
                                              (> (vector-ref vec i)
                                                 (vector-ref vec rr)))
                                         (inner (+ rr 1))
                                         rr))))
                              (let ((cand (- new-right i 1))
                                    (new-ans (min ans cand)))
                                (loop3 (+ i 1) new-right new-ans)))))))
                final-ans))))))
```

## Erlang

```erlang
-spec find_length_of_shortest_subarray([integer()]) -> integer().
find_length_of_shortest_subarray(Arr) ->
    T = list_to_tuple(Arr),
    N = tuple_size(T),
    case N of
        0 -> 0;
        _ ->
            LeftEnd = left_end(T, N, 0),
            if
                LeftEnd == N - 1 ->
                    0;                                   % already sorted
                true ->
                    RightStart = right_start(T, N - 1),
                    Ans0 = erlang:min(RightStart, N - (LeftEnd + 1)),
                    loop_i(T, N, 0, LeftEnd, RightStart, Ans0)
            end
    end.

%% get element at zero‑based index
get(T, I) -> element(I + 1, T).

left_end(_T, N, Idx) when Idx >= N - 1 -> Idx;
left_end(T, N, Idx) ->
    case (Idx + 1 < N) andalso (get(T, Idx) =< get(T, Idx + 1)) of
        true -> left_end(T, N, Idx + 1);
        false -> Idx
    end.

right_start(_T, 0) -> 0;
right_start(T, Idx) ->
    case (Idx > 0) andalso (get(T, Idx - 1) =< get(T, Idx)) of
        true -> right_start(T, Idx - 1);
        false -> Idx
    end.

loop_i(_T, _N, I, LEnd, _J, Ans) when I > LEnd -> Ans;
loop_i(T, N, I, LEnd, J, Ans) ->
    NewJ = advance_j(T, N, I, J),
    Len = case NewJ > I of
              true -> NewJ - I - 1;
              false -> 0
          end,
    NewAns = erlang:min(Ans, Len),
    loop_i(T, N, I + 1, LEnd, NewJ, NewAns).

advance_j(_T, _N, _I, J) when J >= _N -> J;
advance_j(T, N, I, J) ->
    case get(T, I) =< get(T, J) of
        true -> J;
        false -> advance_j(T, N, I, J + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_length_of_shortest_subarray(arr :: [integer]) :: integer
  def find_length_of_shortest_subarray(arr) do
    n = length(arr)
    tup = List.to_tuple(arr)

    left_end = find_left(tup, n, 0)
    right_start = find_right(tup, n, n - 1)

    if left_end >= right_start do
      0
    else
      ans_initial = min(n - (left_end + 1), right_start)
      two_pointer(tup, n, left_end, right_start, ans_initial)
    end
  end

  defp find_left(_tup, n, i) when i + 1 >= n, do: i
  defp find_left(tup, n, i) do
    if elem(tup, i) <= elem(tup, i + 1) do
      find_left(tup, n, i + 1)
    else
      i
    end
  end

  defp find_right(_tup, _n, j) when j <= 0, do: j
  defp find_right(tup, n, j) do
    if elem(tup, j - 1) <= elem(tup, j) do
      find_right(tup, n, j - 1)
    else
      j
    end
  end

  defp two_pointer(tup, n, left_end, right_start, ans) do
    do_two_pointer(0, left_end, right_start, n, tup, ans)
  end

  defp do_two_pointer(i, left_end, _j, _n, _tup, ans) when i > left_end, do: ans
  defp do_two_pointer(i, left_end, j, n, tup, ans) do
    new_j = advance_j(j, n, elem(tup, i), tup)
    new_ans = min(ans, new_j - i - 1)
    do_two_pointer(i + 1, left_end, new_j, n, tup, new_ans)
  end

  defp advance_j(j, n, val_i, tup) when j < n and val_i > elem(tup, j) do
    advance_j(j + 1, n, val_i, tup)
  end
  defp advance_j(j, _n, _val_i, _tup), do: j
end
```
