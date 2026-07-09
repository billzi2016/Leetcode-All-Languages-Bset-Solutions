# 3471. Find the Largest Almost Missing Integer

## Cpp

```cpp
class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        const int MAXV = 51;
        vector<int> cnt(MAXV, 0);
        for (int start = 0; start <= n - k; ++start) {
            bool seen[MAXV] = {false};
            for (int i = start; i < start + k; ++i) {
                int v = nums[i];
                if (!seen[v]) {
                    seen[v] = true;
                    cnt[v]++;
                }
            }
        }
        int ans = -1;
        for (int v = 0; v < MAXV; ++v) {
            if (cnt[v] == 1) ans = max(ans, v);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        if (k == 1) {
            int[] freq = new int[51];
            for (int v : nums) freq[v]++;
            int ans = -1;
            for (int v = 0; v <= 50; v++) {
                if (freq[v] == 1 && v > ans) ans = v;
            }
            return ans;
        } else if (k == n) {
            int max = nums[0];
            for (int v : nums) if (v > max) max = v;
            return max;
        } else {
            int[] freq = new int[51];
            for (int v : nums) freq[v]++;
            int leftVal = nums[0];
            int rightVal = nums[n - 1];
            int ans = -1;
            if (freq[leftVal] == 1) ans = Math.max(ans, leftVal);
            if (freq[rightVal] == 1) ans = Math.max(ans, rightVal);
            return ans;
        }
    }
}
```

## Python

```python
class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        n = len(nums)
        if k == 1:
            freq = Counter(nums)
            ans = -1
            for num, cnt in freq.items():
                if cnt == 1 and num > ans:
                    ans = num
            return ans
        elif k == n:
            return max(nums)
        else:
            freq = Counter(nums)
            candidates = []
            if freq[nums[0]] == 1:
                candidates.append(nums[0])
            if freq[nums[-1]] == 1:
                candidates.append(nums[-1])
            return max(candidates) if candidates else -1
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            freq = Counter(nums)
            ans = -1
            for val, cnt in freq.items():
                if cnt == 1 and val > ans:
                    ans = val
            return ans
        if k == n:
            return max(nums) if nums else -1
        # 1 < k < n
        freq = Counter(nums)
        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])
        return max(candidates) if candidates else -1
```

## C

```c
int largestInteger(int* nums, int numsSize, int k) {
    int freq[51] = {0};
    for (int i = 0; i < numsSize; ++i) {
        freq[nums[i]]++;
    }
    
    if (k == 1) {
        int ans = -1;
        for (int v = 0; v <= 50; ++v) {
            if (freq[v] == 1 && v > ans) ans = v;
        }
        return ans;
    } else if (k == numsSize) {
        int maxv = nums[0];
        for (int i = 1; i < numsSize; ++i) {
            if (nums[i] > maxv) maxv = nums[i];
        }
        return maxv;
    } else {
        int firstVal = nums[0];
        int lastVal = nums[numsSize - 1];
        int firstUnique = freq[firstVal] == 1;
        int lastUnique = freq[lastVal] == 1;
        
        if (!firstUnique && !lastUnique) return -1;
        if (firstUnique && lastUnique) return firstVal > lastVal ? firstVal : lastVal;
        return firstUnique ? firstVal : lastVal;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int LargestInteger(int[] nums, int k) {
        int n = nums.Length;
        if (k == 1) {
            var freq = new Dictionary<int, int>();
            foreach (int v in nums) {
                if (!freq.ContainsKey(v)) freq[v] = 0;
                freq[v]++;
            }
            int ans = -1;
            foreach (var kvp in freq) {
                if (kvp.Value == 1 && kvp.Key > ans) ans = kvp.Key;
            }
            return ans;
        }
        if (k == n) {
            int maxVal = nums[0];
            for (int i = 1; i < n; i++) {
                if (nums[i] > maxVal) maxVal = nums[i];
            }
            return maxVal;
        }
        // 1 < k < n
        var count = new Dictionary<int, int>();
        foreach (int v in nums) {
            if (!count.ContainsKey(v)) count[v] = 0;
            count[v]++;
        }
        int first = nums[0];
        int last = nums[n - 1];
        bool firstOk = count[first] == 1;
        bool lastOk = count[last] == 1;
        if (firstOk && lastOk) return Math.Max(first, last);
        if (firstOk) return first;
        if (lastOk) return last;
        return -1;
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
var largestInteger = function(nums, k) {
    const n = nums.length;
    if (k === 1) {
        const freq = new Map();
        for (const v of nums) {
            freq.set(v, (freq.get(v) || 0) + 1);
        }
        let ans = -1;
        for (const [val, cnt] of freq.entries()) {
            if (cnt === 1 && val > ans) ans = val;
        }
        return ans;
    }
    if (k === n) {
        // only one subarray, any element appears exactly once in that subarray
        let maxVal = nums[0];
        for (let i = 1; i < n; ++i) {
            if (nums[i] > maxVal) maxVal = nums[i];
        }
        return maxVal;
    }
    // 1 < k < n
    const freq = new Map();
    for (const v of nums) {
        freq.set(v, (freq.get(v) || 0) + 1);
    }
    const first = nums[0];
    const last = nums[n - 1];
    let ans = -1;
    if (freq.get(first) === 1) ans = Math.max(ans, first);
    if (freq.get(last) === 1) ans = Math.max(ans, last);
    return ans;
};
```

## Typescript

```typescript
function largestInteger(nums: number[], k: number): number {
    const n = nums.length;
    if (k === 1) {
        const freq = new Map<number, number>();
        for (const v of nums) {
            freq.set(v, (freq.get(v) ?? 0) + 1);
        }
        let ans = -1;
        for (const [v, cnt] of freq.entries()) {
            if (cnt === 1 && v > ans) ans = v;
        }
        return ans;
    }
    if (k === n) {
        let mx = nums[0];
        for (let i = 1; i < n; ++i) {
            if (nums[i] > mx) mx = nums[i];
        }
        return mx;
    }
    // 1 < k < n
    const first = nums[0];
    const last = nums[n - 1];
    let cntFirst = 0, cntLast = 0;
    for (const v of nums) {
        if (v === first) cntFirst++;
        if (v === last) cntLast++;
    }
    const candidates: number[] = [];
    if (cntFirst === 1) candidates.push(first);
    if (cntLast === 1) candidates.push(last);
    if (candidates.length === 0) return -1;
    return Math.max(...candidates);
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
    function largestInteger($nums, $k) {
        $n = count($nums);
        if ($k == 1) {
            $freq = array_count_values($nums);
            $ans = -1;
            foreach ($freq as $val => $cnt) {
                if ($cnt == 1 && $val > $ans) {
                    $ans = $val;
                }
            }
            return $ans;
        }
        if ($k == $n) {
            return max($nums);
        }
        // 1 < k < n
        $first = $nums[0];
        $last = $nums[$n - 1];
        $freq = array_count_values($nums);
        $candidates = [];
        if (isset($freq[$first]) && $freq[$first] == 1) {
            $candidates[] = $first;
        }
        if (isset($freq[$last]) && $freq[$last] == 1) {
            $candidates[] = $last;
        }
        if (empty($candidates)) {
            return -1;
        }
        return max($candidates);
    }
}
```

## Swift

```swift
class Solution {
    func largestInteger(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if k == 1 {
            var freq = [Int:Int]()
            for v in nums {
                freq[v, default: 0] += 1
            }
            var ans = -1
            for (v, c) in freq where c == 1 {
                if v > ans { ans = v }
            }
            return ans
        } else if k == n {
            var mx = nums[0]
            for v in nums {
                if v > mx { mx = v }
            }
            return mx
        } else {
            let first = nums[0]
            let last = nums[n - 1]
            var cntFirst = 0, cntLast = 0
            for v in nums {
                if v == first { cntFirst += 1 }
                if v == last { cntLast += 1 }
            }
            var ans = -1
            if cntFirst == 1 && first > ans { ans = first }
            if cntLast == 1 && last > ans { ans = max(ans, last) }
            return ans
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestInteger(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (k == 1) {
            val freq = IntArray(51)
            for (v in nums) freq[v]++
            var ans = -1
            for (i in 0..50) {
                if (freq[i] == 1 && i > ans) ans = i
            }
            return ans
        } else if (k == n) {
            var maxVal = nums[0]
            for (v in nums) if (v > maxVal) maxVal = v
            return maxVal
        } else {
            val first = nums[0]
            val last = nums[n - 1]
            var cntFirst = 0
            var cntLast = 0
            for (v in nums) {
                if (v == first) cntFirst++
                if (v == last) cntLast++
            }
            var ans = -1
            if (cntFirst == 1) ans = maxOf(ans, first)
            if (last != first && cntLast == 1) ans = maxOf(ans, last)
            return ans
        }
    }
}
```

## Dart

```dart
class Solution {
  int largestInteger(List<int> nums, int k) {
    int n = nums.length;
    if (k == 1) {
      final Map<int, int> freq = {};
      for (int v in nums) {
        freq[v] = (freq[v] ?? 0) + 1;
      }
      int ans = -1;
      freq.forEach((key, value) {
        if (value == 1 && key > ans) ans = key;
      });
      return ans;
    } else if (k == n) {
      int maxVal = nums[0];
      for (int v in nums) {
        if (v > maxVal) maxVal = v;
      }
      return maxVal;
    } else {
      final Map<int, int> freq = {};
      for (int v in nums) {
        freq[v] = (freq[v] ?? 0) + 1;
      }
      bool firstUnique = (freq[nums[0]] ?? 0) == 1;
      bool lastUnique = (freq[nums[n - 1]] ?? 0) == 1;
      if (firstUnique && lastUnique) {
        return nums[0] > nums[n - 1] ? nums[0] : nums[n - 1];
      } else if (firstUnique) {
        return nums[0];
      } else if (lastUnique) {
        return nums[n - 1];
      } else {
        return -1;
      }
    }
  }
}
```

## Golang

```go
func largestInteger(nums []int, k int) int {
    n := len(nums)
    if k == n {
        maxVal := nums[0]
        for _, v := range nums {
            if v > maxVal {
                maxVal = v
            }
        }
        return maxVal
    }
    if k == 1 {
        cnt := make(map[int]int)
        for _, v := range nums {
            cnt[v]++
        }
        ans := -1
        for val, c := range cnt {
            if c == 1 && val > ans {
                ans = val
            }
        }
        return ans
    }
    // 1 < k < n
    first := nums[0]
    last := nums[n-1]
    countFirst, countLast := 0, 0
    for _, v := range nums {
        if v == first {
            countFirst++
        }
        if v == last {
            countLast++
        }
    }
    if countFirst > 1 && countLast > 1 {
        return -1
    }
    if countFirst == 1 && countLast == 1 {
        if first > last {
            return first
        }
        return last
    }
    if countFirst == 1 {
        return first
    }
    if countLast == 1 {
        return last
    }
    return -1
}
```

## Ruby

```ruby
def largest_integer(nums, k)
  n = nums.length
  if k == 1
    freq = Hash.new(0)
    nums.each { |x| freq[x] += 1 }
    candidates = freq.select { |_v, cnt| cnt == 1 }.keys
    return candidates.max || -1
  elsif k == n
    return nums.max
  else
    freq = Hash.new(0)
    nums.each { |x| freq[x] += 1 }
    ans = -1
    first = nums[0]
    last = nums[-1]
    ans = [ans, first].max if freq[first] == 1
    ans = [ans, last].max if freq[last] == 1
    return ans
  end
end
```

## Scala

```scala
object Solution {
    def largestInteger(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        if (k == 1) {
            val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
            for (v <- nums) freq(v) += 1
            var ans = -1
            for ((v, c) <- freq) {
                if (c == 1 && v > ans) ans = v
            }
            ans
        } else if (k == n) {
            var maxVal = nums(0)
            for (v <- nums) if (v > maxVal) maxVal = v
            maxVal
        } else { // 1 < k < n
            val first = nums(0)
            val last = nums(n - 1)
            var cntFirst = 0
            var cntLast = 0
            for (v <- nums) {
                if (v == first) cntFirst += 1
                if (v == last) cntLast += 1
            }
            var ans = -1
            if (cntFirst == 1 && first > ans) ans = first
            if (cntLast == 1 && last > ans) ans = last
            ans
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_usize = k as usize;
        // Case k == 1
        if k == 1 {
            let mut freq = [0usize; 51];
            for &v in &nums {
                freq[v as usize] += 1;
            }
            for v in (0..=50).rev() {
                if freq[v] == 1 {
                    return v as i32;
                }
            }
            return -1;
        }
        // Case k == n
        if k_usize == n {
            let mut max_val = nums[0];
            for &v in &nums[1..] {
                if v > max_val {
                    max_val = v;
                }
            }
            return max_val;
        }
        // Case 1 < k < n
        let first = nums[0];
        let last = nums[n - 1];
        let mut freq = [0usize; 51];
        for &v in &nums {
            freq[v as usize] += 1;
        }
        let mut ans = -1;
        if freq[first as usize] == 1 && first > ans {
            ans = first;
        }
        if freq[last as usize] == 1 && last > ans {
            ans = last;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (largest-integer nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [freq (let ([h (make-hash)])
                 (for-each (lambda (x) (hash-set! h x (+ 1 (hash-ref h x 0)))) nums)
                 h)])
    (cond
      [(= k 1)
       (let loop ((lst nums) (ans -1))
         (if (null? lst)
             ans
             (let* ([x (car lst)]
                    [cnt (hash-ref freq x)])
               (loop (cdr lst) (if (and (= cnt 1) (> x ans)) x ans)))))]
      [(= k n)
       (apply max nums)]
      [else
       (let* ([first-val (car nums)]
              [last-val (list-ref nums (- n 1))]
              [candidates (filter identity
                                  (list (if (= (hash-ref freq first-val) 1) first-val #f)
                                        (if (= (hash-ref freq last-val) 1) last-val #f)))])
         (if (null? candidates)
             -1
             (apply max candidates)))])))
```

## Erlang

```erlang
-spec largest_integer(Nums :: [integer()], K :: integer()) -> integer().
largest_integer(Nums, K) ->
    N = length(Nums),
    case K of
        1 ->
            FreqMap = lists:foldl(
                fun(E, Acc) ->
                    maps:update_with(E, fun(V) -> V + 1 end, 1, Acc)
                end,
                #{},
                Nums
            ),
            Candidates = [X || {X, C} <- maps:to_list(FreqMap), C == 1],
            case Candidates of
                [] -> -1;
                _  -> lists:max(Candidates)
            end;
        K when K == N ->
            lists:max(Nums);
        _ ->
            First = hd(Nums),
            Last = lists:last(Nums),
            CountFirst = length([X || X <- Nums, X == First]),
            CountLast = length([X || X <- Nums, X == Last]),
            Candidates = case {CountFirst == 1, CountLast == 1} of
                {true, true}   -> [First, Last];
                {true, false}  -> [First];
                {false, true}  -> [Last];
                _              -> []
            end,
            case Candidates of
                [] -> -1;
                _  -> lists:max(Candidates)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_integer(nums :: [integer], k :: integer) :: integer
  def largest_integer(nums, k) do
    n = length(nums)
    total_windows = n - k + 1

    counts =
      Enum.reduce(0..(total_windows - 1), %{}, fn start, acc ->
        window = Enum.slice(nums, start, k)
        uniq = MapSet.new(window)

        Enum.reduce(uniq, acc, fn x, a ->
          Map.update(a, x, 1, &(&1 + 1))
        end)
      end)

    candidates =
      counts
      |> Enum.filter(fn {_x, c} -> c == 1 end)
      |> Enum.map(fn {x, _c} -> x end)

    case candidates do
      [] -> -1
      _ -> Enum.max(candidates)
    end
  end
end
```
