# 0845. Longest Mountain in Array

## Cpp

```cpp
class Solution {
public:
    int longestMountain(std::vector<int>& arr) {
        int n = arr.size();
        int ans = 0;
        int base = 0;
        while (base < n) {
            int end = base;
            // climb up
            while (end + 1 < n && arr[end] < arr[end + 1]) {
                ++end;
            }
            // peak must not be at the start
            if (end > base) {
                int peak = end;
                // descend down
                while (end + 1 < n && arr[end] > arr[end + 1]) {
                    ++end;
                }
                // valid mountain needs descent
                if (end > peak) {
                    ans = std::max(ans, end - base + 1);
                }
            }
            // move base to the next possible start
            base = std::max(end, base + 1);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int longestMountain(int[] arr) {
        int n = arr.length;
        int maxLen = 0;
        int i = 0;
        while (i < n) {
            int start = i;
            // climb up
            while (i + 1 < n && arr[i] < arr[i + 1]) {
                i++;
            }
            // peak must not be at the start
            if (i > start) {
                int peak = i;
                // descend down
                while (i + 1 < n && arr[i] > arr[i + 1]) {
                    i++;
                }
                if (i > peak) { // valid mountain
                    maxLen = Math.max(maxLen, i - start + 1);
                }
            }
            // move forward if no progress to avoid infinite loop
            if (i == start) {
                i++;
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        ans = 0
        i = 1
        while i < n - 1:
            # check if arr[i] is a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                ans = max(ans, right - left + 1)
                i = right + 1  # skip processed part
            else:
                i += 1
        return ans
```

## Python3

```python
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        ans = 0
        i = 1
        while i < n - 1:
            # check if current element is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                right = i + 1
                while right + 1 < n and arr[right] > arr[right + 1]:
                    right += 1
                ans = max(ans, right - left + 1)
                i = right + 1  # move past this mountain
            else:
                i += 1
        return ans
```

## C

```c
int longestMountain(int* arr, int arrSize) {
    if (arrSize < 3) return 0;
    int ans = 0;
    int i = 1;
    while (i < arrSize - 1) {
        // check if current element is a peak
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            int left = i - 1;
            while (left > 0 && arr[left] > arr[left - 1]) {
                left--;
            }
            int right = i + 1;
            while (right < arrSize - 1 && arr[right] > arr[right + 1]) {
                right++;
            }
            int len = right - left + 1;
            if (len > ans) ans = len;
            i = right; // skip processed part
        } else {
            i++;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestMountain(int[] arr) {
        int n = arr.Length;
        if (n < 3) return 0;
        int ans = 0;
        int i = 1;
        while (i < n - 1) {
            // check if current element is a peak
            if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                int left = i - 1;
                while (left > 0 && arr[left] > arr[left - 1]) {
                    left--;
                }
                int right = i + 1;
                while (right < n - 1 && arr[right] > arr[right + 1]) {
                    right++;
                }
                ans = Math.Max(ans, right - left + 1);
                i = right + 1; // skip processed part
            } else {
                i++;
            }
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
var longestMountain = function(arr) {
    const n = arr.length;
    let ans = 0;
    let i = 1; // start from second element, need left neighbor
    
    while (i < n - 1) {
        // check if current is a peak
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            // expand to the left
            let left = i - 1;
            while (left > 0 && arr[left] > arr[left - 1]) {
                left--;
            }
            // expand to the right
            let right = i + 1;
            while (right < n - 1 && arr[right] > arr[right + 1]) {
                right++;
            }
            ans = Math.max(ans, right - left + 1);
            // move i beyond this mountain to avoid rechecking interior points
            i = right + 1;
        } else {
            i++;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function longestMountain(arr: number[]): number {
    const n = arr.length;
    if (n < 3) return 0;
    let ans = 0;
    let i = 1;
    while (i < n - 1) {
        // check if arr[i] is a peak
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            let left = i - 1;
            while (left > 0 && arr[left] > arr[left - 1]) {
                left--;
            }
            let right = i + 1;
            while (right < n - 1 && arr[right] > arr[right + 1]) {
                right++;
            }
            ans = Math.max(ans, right - left + 1);
            i = right + 1; // skip processed part
        } else {
            i++;
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
    function longestMountain($arr) {
        $n = count($arr);
        $maxLen = 0;
        $i = 1;
        while ($i < $n - 1) {
            // check if current element is a peak
            if ($arr[$i] > $arr[$i - 1] && $arr[$i] > $arr[$i + 1]) {
                // expand to the left
                $left = $i - 1;
                while ($left > 0 && $arr[$left] > $arr[$left - 1]) {
                    $left--;
                }
                // expand to the right
                $right = $i + 1;
                while ($right < $n - 1 && $arr[$right] > $arr[$right + 1]) {
                    $right++;
                }
                $maxLen = max($maxLen, $right - $left + 1);
                // move i to the end of this mountain
                $i = $right;
            } else {
                $i++;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestMountain(_ arr: [Int]) -> Int {
        let n = arr.count
        var ans = 0
        var i = 0
        while i < n {
            var up = 0
            var down = 0
            // climb up
            while i + 1 < n && arr[i] < arr[i + 1] {
                i += 1
                up += 1
            }
            // climb down
            while i + 1 < n && arr[i] > arr[i + 1] && up > 0 {
                i += 1
                down += 1
            }
            if up > 0 && down > 0 {
                ans = max(ans, up + down + 1)
            }
            // skip flat parts
            while i + 1 < n && arr[i] == arr[i + 1] {
                i += 1
            }
            if up == 0 && down == 0 {
                i += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestMountain(arr: IntArray): Int {
        val n = arr.size
        var ans = 0
        var i = 1
        while (i < n - 1) {
            if (arr[i] > arr[i - 1]) { // start of an uphill
                var j = i
                // climb up
                while (j < n && arr[j] > arr[j - 1]) {
                    j++
                }
                // need a downhill after the peak
                if (j < n && arr[j] < arr[j - 1]) {
                    // descend
                    while (j < n && arr[j] < arr[j - 1]) {
                        j++
                    }
                    val len = j - (i - 1)
                    if (len >= 3) ans = maxOf(ans, len)
                }
                i = j // continue from the end of this segment
            } else {
                i++
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestMountain(List<int> arr) {
    int n = arr.length;
    if (n < 3) return 0;
    int ans = 0;
    int i = 1;
    while (i < n - 1) {
      // check for peak
      if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
        int left = i - 1;
        while (left > 0 && arr[left] > arr[left - 1]) {
          left--;
        }
        int right = i + 1;
        while (right < n - 1 && arr[right] > arr[right + 1]) {
          right++;
        }
        ans = max(ans, right - left + 1);
        i = right + 1; // skip processed part
      } else {
        i++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func longestMountain(arr []int) int {
    n := len(arr)
    if n < 3 {
        return 0
    }
    ans := 0
    i := 0
    for i < n-1 {
        // skip non‑increasing start positions
        for i+1 < n && arr[i] >= arr[i+1] {
            i++
        }
        up := i
        // climb up
        for up+1 < n && arr[up] < arr[up+1] {
            up++
        }
        if up == i { // no ascent
            i = up + 1
            continue
        }
        down := up
        // descend
        for down+1 < n && arr[down] > arr[down+1] {
            down++
        }
        if down > up { // valid mountain
            length := down - i + 1
            if length > ans {
                ans = length
            }
        }
        i = down
    }
    return ans
}
```

## Ruby

```ruby
def longest_mountain(arr)
  n = arr.length
  return 0 if n < 3
  max_len = 0
  i = 0

  while i < n - 2
    # look for the start of an ascent
    if arr[i] < arr[i + 1]
      j = i + 1
      # climb up
      while j < n && arr[j - 1] < arr[j]
        j += 1
      end

      # peak must have a descent
      if j < n && arr[j - 1] > arr[j]
        # descend down
        while j + 1 < n && arr[j] > arr[j + 1]
          j += 1
        end
        max_len = [max_len, j - i + 1].max
      end

      i = j
    else
      i += 1
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestMountain(arr: Array[Int]): Int = {
        val n = arr.length
        var ans = 0
        var i = 1
        while (i < n - 1) {
            if (arr(i) <= arr(i - 1)) {
                i += 1
            } else {
                var start = i - 1
                // climb up
                while (i < n && arr(i) > arr(i - 1)) {
                    i += 1
                }
                // need a descent to form a mountain
                if (i == n || arr(i) >= arr(i - 1)) {
                    // no valid descent, continue from current position
                } else {
                    // descend down
                    while (i < n && arr(i) < arr(i - 1)) {
                        i += 1
                    }
                    val len = i - start
                    if (len >= 3) ans = math.max(ans, len)
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_mountain(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n < 3 {
            return 0;
        }
        let mut best = 0usize;
        let mut i = 0usize;

        while i < n {
            // skip flat or descending parts to find a possible start of an ascent
            while i + 1 < n && arr[i] >= arr[i + 1] {
                i += 1;
            }
            let up_start = i;

            // climb up
            while i + 1 < n && arr[i] < arr[i + 1] {
                i += 1;
            }
            let peak = i;

            // climb down
            while i + 1 < n && arr[i] > arr[i + 1] {
                i += 1;
            }
            let down_end = i;

            if up_start < peak && peak < down_end {
                best = best.max(down_end - up_start + 1);
            }

            // If no descent was found, move forward to avoid infinite loop
            if i == peak {
                i += 1;
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (longest-mountain arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length arr))
         (v (list->vector arr)))
    (if (< n 3)
        0
        (let loop ((i 1) (maxlen 0))
          (cond [(>= i (- n 1)) maxlen]
                [else
                 (if (and (> (vector-ref v i) (vector-ref v (- i 1)))
                          (> (vector-ref v i) (vector-ref v (+ i 1))))
                     (let* ((l (let find-left ((l (- i 1)))
                                 (if (and (> l 0)
                                          (> (vector-ref v l) (vector-ref v (- l 1))))
                                     (find-left (- l 1))
                                     l)))
                            (r (let find-right ((r (+ i 1)))
                                 (if (and (< r (- n 1))
                                          (> (vector-ref v r) (vector-ref v (+ r 1))))
                                     (find-right (+ r 1))
                                     r)))
                            (len (+ (- r l) 1))
                            (new-max (if (> len maxlen) len maxlen)))
                       (loop r new-max))
                     (loop (+ i 1) maxlen))])))))
```

## Erlang

```erlang
-spec longest_mountain(Arr :: [integer()]) -> integer().
longest_mountain(Arr) ->
    case Arr of
        [] -> 0;
        _ ->
            T = list_to_tuple(Arr),
            N = tuple_size(T),
            loop(T, N, 1, 0)
    end.

%% Main scanning loop.
-spec loop(tuple(), non_neg_integer(), pos_integer(), non_neg_integer()) -> non_neg_integer().
loop(_T, N, Base, Best) when Base >= N - 1 ->
    Best;
loop(T, N, Base, Best) ->
    UpEnd = climb_up(T, N, Base),
    case UpEnd of
        Base ->
            %% No increasing part, move forward.
            loop(T, N, Base + 1, Best);
        _ ->
            Peak = UpEnd,
            DownEnd = climb_down(T, N, Peak),
            if
                DownEnd > Peak ->
                    Len = DownEnd - Base + 1,
                    NewBest = erlang:max(Best, Len),
                    %% Next possible mountain starts at DownEnd.
                    loop(T, N, DownEnd, NewBest);
                true ->
                    %% No decreasing part after the rise.
                    loop(T, N, Base + 1, Best)
            end
    end.

%% Move right while strictly increasing.
-spec climb_up(tuple(), non_neg_integer(), pos_integer()) -> pos_integer().
climb_up(_T, N, Idx) when Idx >= N ->
    Idx;
climb_up(T, N, Idx) ->
    Next = Idx + 1,
    case element(Idx, T) < element(Next, T) of
        true -> climb_up(T, N, Next);
        false -> Idx
    end.

%% Move right while strictly decreasing.
-spec climb_down(tuple(), non_neg_integer(), pos_integer()) -> pos_integer().
climb_down(_T, N, Idx) when Idx >= N ->
    Idx;
climb_down(T, N, Idx) ->
    Next = Idx + 1,
    case element(Idx, T) > element(Next, T) of
        true -> climb_down(T, N, Next);
        false -> Idx
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_mountain(arr :: [integer]) :: integer
  def longest_mountain(arr) do
    n = length(arr)

    if n < 3 do
      0
    else
      t = List.to_tuple(arr)
      loop(t, n, 1, 0)
    end
  end

  defp loop(_t, n, i, ans) when i >= n - 1, do: ans

  defp loop(t, n, i, ans) do
    if elem(t, i) > elem(t, i - 1) and elem(t, i) > elem(t, i + 1) do
      left = expand_left(t, i - 1)
      right = expand_right(t, n, i + 1)
      len = right - left + 1
      new_ans = if len > ans, do: len, else: ans
      loop(t, n, right + 1, new_ans)
    else
      loop(t, n, i + 1, ans)
    end
  end

  defp expand_left(_t, left) when left <= 0, do: left

  defp expand_left(t, left) do
    if elem(t, left) > elem(t, left - 1) do
      expand_left(t, left - 1)
    else
      left
    end
  end

  defp expand_right(_t, n, right) when right >= n - 1, do: right

  defp expand_right(t, n, right) do
    if elem(t, right) > elem(t, right + 1) do
      expand_right(t, n, right + 1)
    else
      right
    end
  end
end
```
