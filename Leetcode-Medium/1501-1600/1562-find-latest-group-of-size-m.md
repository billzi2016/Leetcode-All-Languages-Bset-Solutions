# 1562. Find Latest Group of Size M

## Cpp

```cpp
class Solution {
public:
    int findLatestStep(vector<int>& arr, int m) {
        int n = arr.size();
        if (m == n) return n;
        vector<int> len(n + 2, 0);          // length of the segment for each position
        vector<int> cnt(n + 1, 0);          // count of segments of a given length
        int ans = -1;
        for (int i = 0; i < n; ++i) {
            int pos = arr[i];
            int left = len[pos - 1];
            int right = len[pos + 1];
            int total = left + right + 1;
            
            if (left > 0) cnt[left]--;
            if (right > 0) cnt[right]--;
            cnt[total]++;
            
            // update the boundary positions of the new segment
            len[pos - left] = total;
            len[pos + right] = total;
            len[pos] = total; // optional, keeps consistency
            
            if (cnt[m] > 0) ans = i + 1; // steps are 1-indexed
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findLatestStep(int[] arr, int m) {
        int n = arr.length;
        if (m == n) return n;

        int[] len = new int[n + 2]; // lengths stored at boundaries
        int[] cnt = new int[n + 1]; // count of groups of each size
        int answer = -1;

        for (int i = 0; i < n; i++) {
            int pos = arr[i];
            int left = len[pos - 1];
            int right = len[pos + 1];
            int cur = left + right + 1;

            if (left > 0) cnt[left]--;
            if (right > 0) cnt[right]--;
            cnt[cur]++;

            // update the boundaries of the new merged group
            len[pos - left] = cur;
            len[pos + right] = cur;
            len[pos] = cur; // optional, keeps internal consistency

            if (cnt[m] > 0) {
                answer = i + 1; // steps are 1-indexed
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)
        length = [0] * (n + 2)          # padding to avoid bounds checks
        cnt = {}
        ans = -1

        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]
            new_len = left + 1 + right

            # update the boundary lengths of the merged group
            length[pos - left] = new_len
            length[pos + right] = new_len

            # adjust counts for old groups
            if left:
                cnt[left] = cnt.get(left, 0) - 1
                if cnt[left] == 0:
                    del cnt[left]
            if right:
                cnt[right] = cnt.get(right, 0) - 1
                if cnt[right] == 0:
                    del cnt[right]

            # count the new merged group
            cnt[new_len] = cnt.get(new_len, 0) + 1

            if cnt.get(m, 0):
                ans = step

        return ans
```

## Python3

```python
class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        cnt = [0] * (n + 1)          # cnt[length] = number of groups with this length
        seg_len = [0] * (n + 2)      # store length at the boundaries of each group
        ans = -1

        for step, pos in enumerate(arr):
            left = seg_len[pos - 1]
            right = seg_len[pos + 1]

            if left:
                cnt[left] -= 1
            if right:
                cnt[right] -= 1

            new_len = left + 1 + right
            cnt[new_len] += 1

            # update the boundaries of the merged segment
            seg_len[pos - left] = new_len
            seg_len[pos + right] = new_len

            if cnt[m] > 0:
                ans = step + 1

        return ans
```

## C

```c
#include <stdlib.h>

int findLatestStep(int* arr, int arrSize, int m) {
    if (m == arrSize) return arrSize;
    int n = arrSize;
    int *len = (int*)calloc(n + 2, sizeof(int));
    int cntM = 0;
    int ans = -1;

    for (int i = 0; i < n; ++i) {
        int pos = arr[i];
        int leftLen = len[pos - 1];
        int rightLen = len[pos + 1];
        int newLen = leftLen + 1 + rightLen;

        if (leftLen == m) --cntM;
        if (rightLen == m) --cntM;

        len[pos - leftLen] = newLen;   // update left boundary
        len[pos + rightLen] = newLen;  // update right boundary

        if (newLen == m) ++cntM;

        if (cntM > 0) ans = i + 1;
    }

    free(len);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindLatestStep(int[] arr, int m)
    {
        int n = arr.Length;
        if (m == n) return n; // whole array will be all 1s at the last step

        int[] len = new int[n + 2]; // extra padding for easier neighbor access
        int[] count = new int[n + 1];
        int answer = -1;

        for (int i = 0; i < n; i++)
        {
            int pos = arr[i];
            int left = len[pos - 1];
            int right = len[pos + 1];
            int curLen = left + 1 + right;

            if (left > 0) count[left]--;
            if (right > 0) count[right]--;

            // update lengths at the new segment's boundaries
            len[pos] = curLen;
            len[pos - left] = curLen;   // leftmost index of the merged segment
            len[pos + right] = curLen;  // rightmost index of the merged segment

            count[curLen]++;

            if (count[m] > 0)
                answer = i + 1; // steps are 1-indexed
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} m
 * @return {number}
 */
var findLatestStep = function(arr, m) {
    const n = arr.length;
    if (m === n) return n; // whole array becomes 1 at the last step

    const len = new Array(n + 2).fill(0); // length of group at each position's boundary
    const count = new Map(); // size -> frequency
    let answer = -1;

    for (let i = 0; i < n; ++i) {
        const pos = arr[i];
        const left = len[pos - 1];
        const right = len[pos + 1];
        const total = left + right + 1;

        // update boundaries of the new merged group
        len[pos] = total;
        len[pos - left] = total;
        len[pos + right] = total;

        // adjust counts for affected groups
        if (left > 0) {
            count.set(left, (count.get(left) || 0) - 1);
        }
        if (right > 0) {
            count.set(right, (count.get(right) || 0) - 1);
        }
        count.set(total, (count.get(total) || 0) + 1);

        // check if a group of size m exists after this step
        if ((count.get(m) || 0) > 0) {
            answer = i + 1; // steps are 1-indexed
        }
    }

    return answer;
};
```

## Typescript

```typescript
function findLatestStep(arr: number[], m: number): number {
    const n = arr.length;
    if (m === n) return n;

    const size = new Array<number>(n + 2).fill(0);
    const cnt = new Map<number, number>();
    let answer = -1;

    const add = (len: number, delta: number): void => {
        if (len <= 0) return;
        const cur = (cnt.get(len) ?? 0) + delta;
        if (cur === 0) cnt.delete(len);
        else cnt.set(len, cur);
    };

    for (let i = 0; i < n; ++i) {
        const pos = arr[i];
        const left = size[pos - 1];
        const right = size[pos + 1];
        const total = left + 1 + right;

        // update boundaries of the new group
        size[pos - left] = total;
        size[pos + right] = total;

        // adjust counts for affected groups
        add(left, -1);
        add(right, -1);
        add(total, 1);

        if (cnt.has(m)) answer = i + 1;
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @return Integer
     */
    function findLatestStep($arr, $m) {
        $n = count($arr);
        // extra padding to avoid boundary checks
        $left = array_fill(0, $n + 2, 0);   // length of group ending at i (rightmost)
        $right = array_fill(0, $n + 2, 0);  // length of group starting at i (leftmost)
        $cnt = []; // map: size => number of groups with that size
        $ans = -1;

        for ($i = 0; $i < $n; $i++) {
            $pos = $arr[$i];
            $L = $left[$pos - 1];   // length of group on the left side
            $R = $right[$pos + 1];  // length of group on the right side
            $total = $L + 1 + $R;   // new merged group size

            // decrease count for old groups
            if ($L > 0) {
                $cnt[$L] = ($cnt[$L] ?? 0) - 1;
                if ($cnt[$L] == 0) unset($cnt[$L]);
            }
            if ($R > 0) {
                $cnt[$R] = ($cnt[$R] ?? 0) - 1;
                if ($cnt[$R] == 0) unset($cnt[$R]);
            }

            // increase count for the new group
            $cnt[$total] = ($cnt[$total] ?? 0) + 1;

            // update boundary lengths
            $left[$pos - $L] = $total;   // leftmost position of merged group
            $right[$pos + $R] = $total;  // rightmost position of merged group
            // optional: set current position for completeness
            $left[$pos] = $total;
            $right[$pos] = $total;

            if (isset($cnt[$m]) && $cnt[$m] > 0) {
                $ans = $i + 1; // steps are 1-indexed
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findLatestStep(_ arr: [Int], _ m: Int) -> Int {
        let n = arr.count
        var length = Array(repeating: 0, count: n + 2)
        var countMap = [Int:Int]()
        var answer = -1

        for (i, pos) in arr.enumerated() {
            let left = length[pos - 1]
            let right = length[pos + 1]
            let total = left + 1 + right

            // update lengths at the new group's boundaries
            length[pos - left] = total
            length[pos + right] = total
            length[pos] = total

            // decrement counts of old groups
            if left > 0 {
                if let cnt = countMap[left] {
                    if cnt == 1 { countMap.removeValue(forKey: left) }
                    else { countMap[left] = cnt - 1 }
                }
            }
            if right > 0 {
                if let cnt = countMap[right] {
                    if cnt == 1 { countMap.removeValue(forKey: right) }
                    else { countMap[right] = cnt - 1 }
                }
            }

            // increment count of the new group
            countMap[total, default: 0] += 1

            // check if a group of size m exists at this step
            if let cntM = countMap[m], cntM > 0 {
                answer = i + 1   // steps are 1-indexed
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLatestStep(arr: IntArray, m: Int): Int {
        val n = arr.size
        if (m == n) return n
        val left = IntArray(n + 2)
        val right = IntArray(n + 2)
        val count = IntArray(n + 1)
        var ans = -1
        for (i in arr.indices) {
            val pos = arr[i]
            val l = if (pos > 1) left[pos - 1] else 0
            val r = if (pos < n) right[pos + 1] else 0
            val cur = l + 1 + r

            if (l > 0) count[l]--
            if (r > 0) count[r]--

            count[cur]++

            left[pos] = cur
            right[pos] = cur
            val start = pos - l
            val end = pos + r
            left[end] = cur
            right[start] = cur

            if (count[m] > 0) {
                ans = i + 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findLatestStep(List<int> arr, int m) {
    int n = arr.length;
    if (m == n) return n;

    List<int> length = List.filled(n + 2, 0);
    List<int> cnt = List.filled(n + 1, 0);
    int ans = -1;

    for (int i = 0; i < n; ++i) {
      int pos = arr[i];
      int left = length[pos - 1];
      int right = length[pos + 1];
      int newLen = left + right + 1;

      if (left > 0) cnt[left]--;
      if (right > 0) cnt[right]--;
      cnt[newLen]++;

      // update the boundaries of the merged group
      length[pos - left] = newLen;
      length[pos + right] = newLen;

      if (cnt[m] > 0) ans = i + 1; // steps are 1-indexed
    }

    return ans;
  }
}
```

## Golang

```go
func findLatestStep(arr []int, m int) int {
    n := len(arr)
    left := make([]int, n+2)  // length of consecutive ones ending at i
    right := make([]int, n+2) // length of consecutive ones starting at i
    cnt := make([]int, n+1)   // count of groups of each size

    ans := -1
    for step, pos := range arr {
        l := left[pos-1]
        r := right[pos+1]
        newSize := l + 1 + r

        if l > 0 {
            cnt[l]--
        }
        if r > 0 {
            cnt[r]--
        }
        cnt[newSize]++

        // update boundaries
        left[pos] = newSize
        right[pos] = newSize
        left[pos+r] = newSize          // end of the merged segment
        right[pos-l] = newSize         // start of the merged segment

        if cnt[m] > 0 {
            ans = step + 1 // steps are 1-indexed
        }
    }
    return ans
}
```

## Ruby

```ruby
def find_latest_step(arr, m)
  n = arr.length
  return -1 if m > n

  len = Array.new(n + 2, 0)          # lengths of groups at boundaries
  count = Hash.new(0)                # how many groups of each size exist
  ans = -1

  arr.each_with_index do |pos, idx|
    left_len = len[pos - 1]
    right_len = len[pos + 1]
    total_len = left_len + 1 + right_len

    count[left_len] -= 1 if left_len > 0
    count[right_len] -= 1 if right_len > 0
    count[total_len] += 1

    # update the new group's boundaries
    len[pos - left_len] = total_len
    len[pos + right_len] = total_len
    len[pos] = total_len

    ans = idx + 1 if count[m] > 0
  end

  ans
end
```

## Scala

```scala
object Solution {
    def findLatestStep(arr: Array[Int], m: Int): Int = {
        val n = arr.length
        val size = new Array[Int](n + 2) // stores group length at boundaries
        import scala.collection.mutable.{Map => MutableMap}
        val cnt = MutableMap.empty[Int, Int].withDefaultValue(0)
        var answer = -1

        for (i <- 0 until n) {
            val pos = arr(i)
            val leftSize = size(pos - 1)
            val rightSize = size(pos + 1)
            val total = leftSize + 1 + rightSize

            if (leftSize > 0) {
                cnt(leftSize) = cnt(leftSize) - 1
                if (cnt(leftSize) == 0) cnt.remove(leftSize)
            }
            if (rightSize > 0) {
                cnt(rightSize) = cnt(rightSize) - 1
                if (cnt(rightSize) == 0) cnt.remove(rightSize)
            }

            size(pos - leftSize) = total          // update left boundary
            size(pos + rightSize) = total         // update right boundary

            cnt(total) = cnt.getOrElse(total, 0) + 1

            if (cnt.getOrElse(m, 0) > 0) answer = i + 1
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_latest_step(arr: Vec<i32>, m: i32) -> i32 {
        let n = arr.len();
        let mut len = vec![0usize; n + 2];          // lengths at group boundaries
        let mut cnt = vec![0i32; n + 1];            // count of groups of each size
        let mut ans: i32 = -1;

        for (step, &p) in arr.iter().enumerate() {
            let pos = p as usize;
            let left = len[pos - 1];
            let right = len[pos + 1];
            let total = left + 1 + right;

            if left > 0 { cnt[left] -= 1; }
            if right > 0 { cnt[right] -= 1; }
            cnt[total] += 1;

            // update the new group's boundaries
            len[pos - left] = total;
            len[pos + right] = total;

            if cnt[m as usize] > 0 {
                ans = (step + 1) as i32;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-latest-step arr m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length arr))
         (arrV (list->vector arr))
         (len (make-vector n 0))
         (cnt (make-hash))
         (ans -1))
    (define (inc! h k delta)
      (hash-set! h k (+ (hash-ref h k 0) delta)))
    (for ([i (in-range 1 (+ n 1))])
      (let* ((pos (vector-ref arrV (- i 1)))          ; position to set
             (idx (- pos 1))
             (left (if (> idx 0) (vector-ref len (- idx 1)) 0))
             (right (if (< idx (- n 1)) (vector-ref len (+ idx 1)) 0))
             (newSize (+ left 1 right)))
        (when (> left 0)
          (inc! cnt left -1))
        (when (> right 0)
          (inc! cnt right -1))
        (inc! cnt newSize 1)
        (let ((leftBound (- pos left))
              (rightBound (+ pos right)))
          (vector-set! len (- leftBound 1) newSize)
          (vector-set! len (- rightBound 1) newSize)
          (vector-set! len idx newSize))
        (when (> (hash-ref cnt m 0) 0)
          (set! ans i))))
    ans))
```

## Erlang

```erlang
-spec find_latest_step(Arr :: [integer()], M :: integer()) -> integer().
find_latest_step(Arr, M) ->
    loop(1, Arr, #{}, #{}, -1, M).

loop(_Idx, [], _LenMap, _CountMap, Ans, _M) ->
    Ans;
loop(Index, [Pos | Rest], LenMap, CountMap, Ans, M) ->
    Left = maps:get(Pos - 1, LenMap, 0),
    Right = maps:get(Pos + 1, LenMap, 0),
    NewLen = Left + Right + 1,
    CountMap1 = dec_count(CountMap, Left),
    CountMap2 = dec_count(CountMap1, Right),
    CountMap3 = inc_count(CountMap2, NewLen),

    StartPos = Pos - Left,
    EndPos = Pos + Right,
    LenMap1 = LenMap
        |> maps:put(StartPos, NewLen)
        |> maps:put(EndPos, NewLen)
        |> maps:put(Pos, NewLen),

    NewAns = case maps:is_key(M, CountMap3) of
                true -> Index;
                false -> Ans
            end,
    loop(Index + 1, Rest, LenMap1, CountMap3, NewAns, M).

dec_count(Map, 0) ->
    Map;
dec_count(Map, Size) ->
    case maps:get(Size, Map, 0) of
        1 -> maps:remove(Size, Map);
        C when C > 1 -> maps:put(Size, C - 1, Map)
    end.

inc_count(Map, Size) ->
    C = maps:get(Size, Map, 0),
    maps:put(Size, C + 1, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_latest_step(arr :: [integer], m :: integer) :: integer
  def find_latest_step(arr, m) do
    n = length(arr)

    # len array stores the size of the group at its leftmost and rightmost positions
    len = :array.new(n + 2, default: 0)
    # cnt array stores how many groups of each size currently exist
    cnt = :array.new(n + 1, default: 0)

    {answer, _len, _cnt} =
      Enum.reduce(Enum.with_index(arr, 1), {-1, len, cnt}, fn {pos, step},
                                                            {cur_ans, len_arr, cnt_arr} ->
        left_len = :array.get(pos - 1, len_arr)
        right_len = :array.get(pos + 1, len_arr)
        new_len = left_len + right_len + 1

        # decrement counts for the groups that are merged (if they exist)
        cnt_arr =
          if left_len > 0 do
            cur = :array.get(left_len, cnt_arr)
            :array.set(left_len, cur - 1, cnt_arr)
          else
            cnt_arr
          end

        cnt_arr =
          if right_len > 0 do
            cur = :array.get(right_len, cnt_arr)
            :array.set(right_len, cur - 1, cnt_arr)
          else
            cnt_arr
          end

        # increment count for the new merged group
        cur_new = :array.get(new_len, cnt_arr)
        cnt_arr = :array.set(new_len, cur_new + 1, cnt_arr)

        # update boundaries of the new group
        left_boundary = pos - left_len
        right_boundary = pos + right_len

        len_arr = :array.set(left_boundary, new_len, len_arr)
        len_arr = :array.set(right_boundary, new_len, len_arr)

        # if there is at least one group of size m, record this step as latest
        cur_ans =
          if :array.get(m, cnt_arr) > 0 do
            step
          else
            cur_ans
          end

        {cur_ans, len_arr, cnt_arr}
      end)

    answer
  end
end
```
