# 3255. Find the Power of K-Size Subarrays II

## Cpp

```cpp
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res;
        res.reserve(n - k + 1);
        int cur_len = 0;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i-1] + 1) {
                ++cur_len;
            } else {
                cur_len = 1;
            }
            if (i >= k - 1) {
                if (cur_len >= k) res.push_back(nums[i]);
                else res.push_back(-1);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int dp = 0; // length of current consecutive increasing suffix
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1] + 1) {
                dp++;
            } else {
                dp = 1;
            }
            if (i >= k - 1) {
                int startIdx = i - k + 1;
                res[startIdx] = (dp >= k) ? nums[i] : -1;
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        cur_len = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                cur_len += 1
            else:
                cur_len = 1
            if i >= k - 1:
                if cur_len >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res
```

## Python3

```python
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        run = 0
        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] == 1:
                run += 1
            else:
                run = 1
            if i >= k - 1:
                if run >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int* nums, int numsSize, int k, int* returnSize){
    *returnSize = numsSize - k + 1;
    int* res = (int*)malloc((*returnSize) * sizeof(int));
    if (!res) return NULL;

    int dp = 0; // length of longest consecutive increasing subarray ending at i
    for (int i = 0; i < numsSize; ++i) {
        if (i > 0 && nums[i] == nums[i - 1] + 1)
            dp += 1;
        else
            dp = 1;

        if (i >= k - 1) {
            int idx = i - k + 1;
            res[idx] = (dp >= k) ? nums[i] : -1;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ResultsArray(int[] nums, int k) {
        int n = nums.Length;
        int[] result = new int[n - k + 1];
        int curLen = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1] + 1) {
                curLen++;
            } else {
                curLen = 1;
            }
            if (i >= k - 1) {
                result[i - k + 1] = curLen >= k ? nums[i] : -1;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var resultsArray = function(nums, k) {
    const n = nums.length;
    const res = new Array(n - k + 1);
    if (n === 0) return res;
    
    const dp = new Array(n);
    dp[0] = 1;
    for (let i = 1; i < n; ++i) {
        dp[i] = (nums[i] === nums[i - 1] + 1) ? dp[i - 1] + 1 : 1;
    }
    
    for (let i = k - 1; i < n; ++i) {
        const start = i - k + 1;
        res[start] = (dp[i] >= k) ? nums[i] : -1;
    }
    return res;
};
```

## Typescript

```typescript
function resultsArray(nums: number[], k: number): number[] {
    const n = nums.length;
    const res: number[] = [];
    let curLen = 1; // length of consecutive increasing suffix ending at current index

    for (let i = 0; i < n; ++i) {
        if (i > 0 && nums[i] === nums[i - 1] + 1) {
            curLen += 1;
        } else {
            curLen = 1;
        }

        if (i >= k - 1) {
            if (curLen >= k) {
                res.push(nums[i]);
            } else {
                res.push(-1);
            }
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function resultsArray($nums, $k) {
        $n = count($nums);
        $dp = array_fill(0, $n, 1);
        for ($i = 1; $i < $n; ++$i) {
            if ($nums[$i] == $nums[$i - 1] + 1) {
                $dp[$i] = $dp[$i - 1] + 1;
            } else {
                $dp[$i] = 1;
            }
        }

        $resSize = $n - $k + 1;
        $result = array_fill(0, $resSize, -1);
        for ($end = $k - 1; $end < $n; ++$end) {
            $start = $end - $k + 1;
            if ($dp[$end] >= $k) {
                $result[$start] = $nums[$end];
            } else {
                $result[$start] = -1;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func resultsArray(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var result = [Int]()
        var streak = 1
        
        for i in 0..<n {
            if i > 0 && nums[i] == nums[i - 1] + 1 {
                streak += 1
            } else {
                streak = 1
            }
            
            if i >= k - 1 {
                if streak >= k {
                    result.append(nums[i])
                } else {
                    result.append(-1)
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun resultsArray(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val res = IntArray(n - k + 1)
        var curLen = 0
        for (i in nums.indices) {
            if (i > 0 && nums[i] == nums[i - 1] + 1) {
                curLen += 1
            } else {
                curLen = 1
            }
            if (i >= k - 1) {
                val start = i - k + 1
                res[start] = if (curLen >= k) nums[i] else -1
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> resultsArray(List<int> nums, int k) {
    int n = nums.length;
    List<int> res = [];
    if (k == 0) return res;
    int dpPrev = 1; // length of current consecutive increasing run ending at i
    for (int i = 0; i < n; ++i) {
      if (i > 0 && nums[i] == nums[i - 1] + 1) {
        dpPrev += 1;
      } else {
        dpPrev = 1;
      }
      if (i >= k - 1) {
        res.add(dpPrev >= k ? nums[i] : -1);
      }
    }
    return res;
  }
}
```

## Golang

```go
func resultsArray(nums []int, k int) []int {
    n := len(nums)
    if n == 0 || k > n {
        return []int{}
    }
    res := make([]int, 0, n-k+1)
    cnt := 1
    for i := 0; i < n; i++ {
        if i > 0 && nums[i] == nums[i-1]+1 {
            cnt++
        } else {
            cnt = 1
        }
        if i >= k-1 {
            if cnt >= k {
                res = append(res, nums[i])
            } else {
                res = append(res, -1)
            }
        }
    }
    return res
}
```

## Ruby

```ruby
def results_array(nums, k)
  n = nums.length
  dp = Array.new(n, 1)
  (1...n).each do |i|
    if nums[i] == nums[i - 1] + 1
      dp[i] = dp[i - 1] + 1
    else
      dp[i] = 1
    end
  end

  res = []
  (0..n - k).each do |start|
    end_idx = start + k - 1
    if dp[end_idx] >= k
      res << nums[end_idx]
    else
      res << -1
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def resultsArray(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        val res = new Array[Int](n - k + 1)
        if (n == 0) return res
        val dp = new Array[Int](n)
        dp(0) = 1
        for (i <- 1 until n) {
            dp(i) = if (nums(i) == nums(i - 1) + 1) dp(i - 1) + 1 else 1
        }
        var idx = 0
        for (end <- k - 1 until n) {
            res(idx) = if (dp(end) >= k) nums(end) else -1
            idx += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        if k == 1 {
            return nums;
        }
        // diff[i] = 1 if nums[i] - nums[i-1] == 1, else 0
        let mut diff = vec![0u8; n];
        for i in 1..n {
            diff[i] = if nums[i] - nums[i - 1] == 1 { 1 } else { 0 };
        }
        // initial sum of diffs for the first window
        let mut cur: usize = 0;
        for i in 1..k {
            cur += diff[i] as usize;
        }
        let mut res = Vec::with_capacity(n - k + 1);
        for start in 0..=n - k {
            if cur == k - 1 {
                // power is the maximum element, which is the last one in an increasing consecutive subarray
                res.push(nums[start + k - 1]);
            } else {
                res.push(-1);
            }
            if start < n - k {
                cur -= diff[start + 1] as usize;
                cur += diff[start + k] as usize;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (results-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (< k 1)
        '()
        (let ([good (make-vector n 0)])
          ;; good[i] = 1 if nums[i] - nums[i-1] == 1
          (for ([i (in-range 1 n)])
            (when (= (- (vector-ref v i) (vector-ref v (- i 1))) 1)
              (vector-set! good i 1)))
          ;; initial sum of good[1..k-1]
          (define init-sum
            (let loop ((i 1) (s 0))
              (if (> i (- k 1))
                  s
                  (loop (+ i 1) (+ s (vector-ref good i))))))
          (let loop ((start 0) (curr-sum init-sum) (acc '()))
            (if (> start (- n k))
                (reverse acc)
                (let* ([power (if (= curr-sum (- k 1))
                                 (vector-ref v (+ start k -1))
                                 -1)]
                       [out (if (< (+ start 1) n)
                                (vector-ref good (+ start 1))
                                0)]
                       [in (if (< (+ start k) n)
                               (vector-ref good (+ start k))
                               0)]
                       [next-sum (- (+ curr-sum in) out)])
                  (loop (+ start 1) next-sum (cons power acc)))))))))
```

## Erlang

```erlang
-spec results_array(Nums :: [integer()], K :: integer()) -> [integer()].
results_array(Nums, K) ->
    lists:reverse(results_array_helper(Nums, K, undefined, 0, 0, [])).

results_array_helper([], _K, _Prev, _RunLen, _Idx, Acc) ->
    Acc;
results_array_helper([H|T], K, Prev, RunLen, Idx, Acc) ->
    NewRun = case Prev of
                 undefined -> 1;
                 _ when H =:= Prev + 1 -> RunLen + 1;
                 _ -> 1
             end,
    NewIdx = Idx + 1,
    if NewIdx >= K ->
            Power = if NewRun >= K -> H; true -> -1 end,
            results_array_helper(T, K, H, NewRun, NewIdx, [Power|Acc]);
       true ->
            results_array_helper(T, K, H, NewRun, NewIdx, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec results_array(nums :: [integer], k :: integer) :: [integer]
  def results_array(nums, k) do
    n = length(nums)

    if k == 1 do
      nums
    else
      arr = List.to_tuple(nums)

      diffs =
        for i <- 0..(n - 1) do
          if i == 0 do
            0
          else
            if elem(arr, i) == elem(arr, i - 1) + 1, do: 1, else: 0
          end
        end

      diff = List.to_tuple(diffs)

      init_bad =
        Enum.reduce(1..(k - 1), 0, fn j, acc ->
          if elem(diff, j) == 0, do: acc + 1, else: acc
        end)

      slide(arr, diff, n, k, 0, init_bad, [])
    end
  end

  defp slide(_arr, _diff, n, k, i, _bad, acc) when i > n - k,
    do: Enum.reverse(acc)

  defp slide(arr, diff, n, k, i, bad, acc) do
    power = if bad == 0, do: elem(arr, i + k - 1), else: -1

    {new_bad, _} =
      if i < n - k do
        left_idx = i + 1
        right_idx = i + k

        b = bad
        b = if elem(diff, left_idx) == 0, do: b - 1, else: b
        b = if elem(diff, right_idx) == 0, do: b + 1, else: b
        {b, nil}
      else
        {bad, nil}
      end

    slide(arr, diff, n, k, i + 1, new_bad, [power | acc])
  end
end
```
