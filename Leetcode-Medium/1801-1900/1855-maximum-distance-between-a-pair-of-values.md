# 1855. Maximum Distance Between a Pair of Values

## Cpp

```cpp
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        int ans = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            if (j < i) j = i;
            while (j + 1 < m && nums1[i] <= nums2[j + 1]) {
                ++j;
            }
            if (nums1[i] <= nums2[j]) {
                ans = max(ans, j - i);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int ans = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i) j = i;
            while (j < m && nums1[i] <= nums2[j]) {
                ans = Math.max(ans, j - i);
                j++;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        ans = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                # valid pair, try to extend j for larger distance
                ans = max(ans, j - i)
                j += 1
            else:
                # nums1[i] too large, move i forward
                i += 1
                if i > j:
                    j = i
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        j = 0
        ans = 0
        for i in range(n1):
            if j < i:
                j = i
            while j + 1 < n2 and nums2[j + 1] >= nums1[i]:
                j += 1
            if j < n2 and nums2[j] >= nums1[i]:
                ans = max(ans, j - i)
        return ans
```

## C

```c
int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0, ans = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] <= nums2[j]) {
            if (j - i > ans) ans = j - i;
            ++j;
        } else {
            ++i;
            if (i > j) j = i;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDistance(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        int m = nums2.Length;
        int i = 0, j = 0, maxDist = 0;
        while (i < n && j < m) {
            if (nums1[i] <= nums2[j]) {
                maxDist = Math.Max(maxDist, j - i);
                j++;
            } else {
                i++;
                if (i > j) j = i;
            }
        }
        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDistance = function(nums1, nums2) {
    let maxDist = 0;
    let j = 0;
    const n2 = nums2.length;
    for (let i = 0; i < nums1.length; ++i) {
        if (j < i) j = i;
        while (j + 1 < n2 && nums2[j + 1] >= nums1[i]) {
            ++j;
        }
        if (nums2[j] >= nums1[i]) {
            maxDist = Math.max(maxDist, j - i);
        }
    }
    return maxDist;
};
```

## Typescript

```typescript
function maxDistance(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    const m = nums2.length;
    let ans = 0;
    let j = 0;
    for (let i = 0; i < n; i++) {
        if (j < i) j = i;
        while (j < m && nums1[i] <= nums2[j]) {
            const dist = j - i;
            if (dist > ans) ans = dist;
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
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxDistance($nums1, $nums2) {
        $n = count($nums1);
        $m = count($nums2);
        $ans = 0;
        $j = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($j < $i) {
                $j = $i;
            }
            while ($j + 1 < $m && $nums2[$j + 1] >= $nums1[$i]) {
                $j++;
            }
            if ($j < $m && $nums2[$j] >= $nums1[$i]) {
                $ans = max($ans, $j - $i);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0
        var j = 0
        let n1 = nums1.count
        let n2 = nums2.count
        var ans = 0
        
        while i < n1 && j < n2 {
            if nums1[i] <= nums2[j] {
                // valid pair, update answer
                ans = max(ans, j - i)
                j += 1
            } else {
                // need a smaller value in nums1, move i forward
                i += 1
                if i > j { j = i }
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(nums1: IntArray, nums2: IntArray): Int {
        var i = 0
        var j = 0
        var ans = 0
        val n1 = nums1.size
        val n2 = nums2.size
        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                ans = kotlin.math.max(ans, j - i)
                j++
            } else {
                i++
                if (i > j) j = i
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(List<int> nums1, List<int> nums2) {
    int n1 = nums1.length;
    int n2 = nums2.length;
    int i = 0, j = 0, ans = 0;
    while (i < n1 && j < n2) {
      if (nums1[i] <= nums2[j]) {
        int dist = j - i;
        if (dist > ans) ans = dist;
        j++;
      } else {
        i++;
        if (i > j) j = i;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxDistance(nums1 []int, nums2 []int) int {
    n1, n2 := len(nums1), len(nums2)
    ans := 0
    j := 0
    for i := 0; i < n1; i++ {
        if j < i {
            j = i
        }
        for j+1 < n2 && nums1[i] <= nums2[j+1] {
            j++
        }
        if j < n2 && nums1[i] <= nums2[j] {
            if d := j - i; d > ans {
                ans = d
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_distance(nums1, nums2)
  i = 0
  j = 0
  ans = 0
  n1 = nums1.length
  n2 = nums2.length

  while i < n1 && j < n2
    if nums1[i] <= nums2[j]
      ans = [ans, j - i].max
      j += 1
    else
      i += 1
      j = i if j < i
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxDistance(nums1: Array[Int], nums2: Array[Int]): Int = {
        var i = 0
        var j = 0
        val n1 = nums1.length
        val n2 = nums2.length
        var ans = 0
        while (i < n1 && j < n2) {
            if (nums1(i) <= nums2(j)) {
                ans = math.max(ans, j - i)
                j += 1
            } else {
                i += 1
                if (i > j) j = i
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n1 = nums1.len();
        let n2 = nums2.len();
        let mut i = 0usize;
        let mut j = 0usize;
        let mut ans = 0i32;
        while i < n1 && j < n2 {
            if nums1[i] <= nums2[j] {
                let dist = (j - i) as i32;
                if dist > ans {
                    ans = dist;
                }
                j += 1;
            } else {
                i += 1;
                if i > j {
                    j = i;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-distance nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (n1 (vector-length v1))
         (n2 (vector-length v2)))
    (let loop ((i 0) (j 0) (maxd 0))
      (if (= i n1)
          maxd
          (let* ((j (if (< j i) i j))
                 (val1 (vector-ref v1 i))
                 (j (let inner ((jj j))
                      (if (and (< jj n2) (>= (vector-ref v2 jj) val1))
                          (inner (+ jj 1))
                          jj)))
                 (dist (- j 1 i))
                 (newmax (if (> dist maxd) dist maxd)))
            (loop (+ i 1) j newmax))))))
```

## Erlang

```erlang
-spec max_distance([integer()], [integer()]) -> integer().
max_distance(Nums1, Nums2) ->
    T1 = list_to_tuple(Nums1),
    T2 = list_to_tuple(Nums2),
    Len1 = tuple_size(T1),
    Len2 = tuple_size(T2),
    loop(0, 0, 0, T1, T2, Len1, Len2).

loop(I, J, Max, _T1, _T2, Len1, _Len2) when I >= Len1 ->
    Max;
loop(I, J, Max, T1, T2, Len1, Len2) ->
    J0 = if J < I -> I; true -> J end,
    {NewJ, _} = advance(I, J0, T1, T2, Len2),
    Dist = case NewJ - 1 >= I of
               true -> NewJ - 1 - I;
               false -> 0
           end,
    Max1 = if Dist > Max -> Dist; true -> Max end,
    loop(I + 1, NewJ, Max1, T1, T2, Len1, Len2).

advance(I, J, T1, T2, Len2) when J < Len2,
      element(I + 1, T1) =< element(J + 1, T2) ->
    advance(I, J + 1, T1, T2, Len2);
advance(_, J, _, _, _) ->
    {J, ok}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_distance(nums1, nums2) do
    t1 = List.to_tuple(nums1)
    t2 = List.to_tuple(nums2)

    len1 = tuple_size(t1)
    len2 = tuple_size(t2)

    loop(0, len1, t1, len2, t2, 0, 0)
  end

  defp loop(i, len1, _t1, _len2, _t2, _j, ans) when i >= len1, do: ans

  defp loop(i, len1, t1, len2, t2, j, ans) do
    j = if j < i, do: i, else: j
    {new_j, new_ans} = advance(i, t1, len2, t2, j, ans)
    loop(i + 1, len1, t1, len2, t2, new_j, new_ans)
  end

  defp advance(_i, _t1, len2, _t2, j, ans) when j >= len2, do: {j, ans}

  defp advance(i, t1, len2, t2, j, ans) do
    if :erlang.element(i + 1, t1) <= :erlang.element(j + 1, t2) do
      new_ans = if j - i > ans, do: j - i, else: ans
      advance(i, t1, len2, t2, j + 1, new_ans)
    else
      {j, ans}
    end
  end
end
```
