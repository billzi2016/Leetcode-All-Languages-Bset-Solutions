# 2653. Sliding Subarray Beauty

## Cpp

```cpp
class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        const int OFFSET = 50; // values from -1 to -50 map to 1..50
        int freq[51] = {0}; // index i corresponds to value -i
        
        auto add = [&](int val){
            if (val < 0) freq[-val]++;
        };
        auto remove = [&](int val){
            if (val < 0) freq[-val]--;
        };
        auto beauty = [&]()->int{
            int cnt = 0;
            for (int i = OFFSET; i >= 1; --i) {
                cnt += freq[i];
                if (cnt >= x) return -i;
            }
            return 0;
        };
        
        // initial window
        for (int i = 0; i < k; ++i) add(nums[i]);
        vector<int> res;
        res.reserve(nums.size() - k + 1);
        res.push_back(beauty());
        
        // slide the window
        for (int i = k; i < (int)nums.size(); ++i) {
            remove(nums[i - k]);
            add(nums[i]);
            res.push_back(beauty());
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int n = nums.length;
        int[] result = new int[n - k + 1];
        // cnt[i] stores frequency of value (i - 50), i ranges from 0 to 49 for negatives -50..-1
        int[] cnt = new int[51];
        int totalNeg = 0;

        // initialize first window
        for (int i = 0; i < k; i++) {
            if (nums[i] < 0) {
                cnt[nums[i] + 50]++;
                totalNeg++;
            }
        }

        int idx = 0;
        result[idx++] = (totalNeg >= x) ? kthSmallestNegative(cnt, x) : 0;

        // slide the window
        for (int i = k; i < n; i++) {
            int out = nums[i - k];
            if (out < 0) {
                cnt[out + 50]--;
                totalNeg--;
            }
            int in = nums[i];
            if (in < 0) {
                cnt[in + 50]++;
                totalNeg++;
            }
            result[idx++] = (totalNeg >= x) ? kthSmallestNegative(cnt, x) : 0;
        }

        return result;
    }

    private int kthSmallestNegative(int[] cnt, int k) {
        int sum = 0;
        for (int i = 0; i < 50; i++) { // indices 0..49 correspond to -50..-1
            sum += cnt[i];
            if (sum >= k) {
                return i - 50;
            }
        }
        return 0; // should not reach here when called correctly
    }
}
```

## Python

```python
class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # frequency array for values -50 .. -1
        offset = 50
        freq = [0] * 51  # index i corresponds to value i - offset
        
        def add(val, delta):
            if val < 0:
                freq[val + offset] += delta

        # initialize first window
        for i in range(k):
            add(nums[i], 1)

        def beauty():
            cnt = 0
            for v in range(-50, 0):  # -50 .. -1
                cnt += freq[v + offset]
                if cnt >= x:
                    return v
            return 0

        res = [beauty()]
        n = len(nums)
        for i in range(k, n):
            add(nums[i - k], -1)   # remove leftmost
            add(nums[i], 1)        # add new rightmost
            res.append(beauty())
        return res
```

## Python3

```python
from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # frequency of negative numbers; index i corresponds to value -i (i from 1..50)
        freq = [0] * 51
        n = len(nums)

        # initialize first window
        for i in range(k):
            v = nums[i]
            if v < 0:
                freq[-v] += 1

        def kth_negative():
            cnt = 0
            for idx in range(50, 0, -1):   # -50 .. -1
                cnt += freq[idx]
                if cnt >= x:
                    return -idx
            return 0

        res = [kth_negative()]

        # slide the window
        for i in range(k, n):
            out_val = nums[i - k]
            if out_val < 0:
                freq[-out_val] -= 1
            in_val = nums[i]
            if in_val < 0:
                freq[-in_val] += 1
            res.append(kth_negative())

        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSubarrayBeauty(int* nums, int numsSize, int k, int x, int* returnSize) {
    *returnSize = numsSize - k + 1;
    int* res = (int*)malloc((*returnSize) * sizeof(int));
    
    // frequency of negatives: index 0 for -1, ..., 49 for -50
    int freq[50] = {0};
    int totalNeg = 0;
    
    // initial window
    for (int i = 0; i < k; ++i) {
        if (nums[i] < 0) {
            int idx = -nums[i] - 1;   // map -1..-50 to 0..49
            freq[idx]++;
            totalNeg++;
        }
    }
    
    for (int i = 0; i < *returnSize; ++i) {
        if (i > 0) { // slide window
            int outVal = nums[i - 1];
            if (outVal < 0) {
                int idx = -outVal - 1;
                freq[idx]--;
                totalNeg--;
            }
            int inVal = nums[i + k - 1];
            if (inVal < 0) {
                int idx = -inVal - 1;
                freq[idx]++;
                totalNeg++;
            }
        }
        
        if (totalNeg < x) {
            res[i] = 0;
        } else {
            int cnt = 0;
            int ans = 0;
            for (int idx = 49; idx >= 0; --idx) { // from -50 up to -1
                cnt += freq[idx];
                if (cnt >= x) {
                    ans = -(idx + 1);
                    break;
                }
            }
            res[i] = ans;
        }
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] GetSubarrayBeauty(int[] nums, int k, int x)
    {
        int n = nums.Length;
        int[] result = new int[n - k + 1];
        // freq[idx] where idx = -value (1..50) for negative numbers
        int[] freq = new int[51];
        int negCount = 0;

        // initialize first window
        for (int i = 0; i < k; i++)
        {
            if (nums[i] < 0)
            {
                freq[-nums[i]]++;
                negCount++;
            }
        }

        for (int start = 0; start <= n - k; start++)
        {
            // compute beauty for current window
            if (negCount < x)
            {
                result[start] = 0;
            }
            else
            {
                int cum = 0;
                for (int idx = 50; idx >= 1; idx--)
                {
                    cum += freq[idx];
                    if (cum >= x)
                    {
                        result[start] = -idx;
                        break;
                    }
                }
            }

            // slide window
            if (start + k < n)
            {
                int outNum = nums[start];
                if (outNum < 0)
                {
                    freq[-outNum]--;
                    negCount--;
                }

                int inNum = nums[start + k];
                if (inNum < 0)
                {
                    freq[-inNum]++;
                    negCount++;
                }
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
 * @param {number} x
 * @return {number[]}
 */
var getSubarrayBeauty = function(nums, k, x) {
    const n = nums.length;
    const freq = new Array(51).fill(0); // index i corresponds to value -i
    
    for (let i = 0; i < k; ++i) {
        if (nums[i] < 0) freq[-nums[i]]++;
    }
    
    const getBeauty = () => {
        let cnt = 0;
        for (let v = -50; v <= -1; ++v) {
            cnt += freq[-v];
            if (cnt >= x) return v;
        }
        return 0;
    };
    
    const res = [];
    res.push(getBeauty());
    
    for (let i = k; i < n; ++i) {
        const outVal = nums[i - k];
        if (outVal < 0) freq[-outVal]--;
        const inVal = nums[i];
        if (inVal < 0) freq[-inVal]++;
        res.push(getBeauty());
    }
    
    return res;
};
```

## Typescript

```typescript
function getSubarrayBeauty(nums: number[], k: number, x: number): number[] {
    const n = nums.length;
    const freq = new Array(51).fill(0); // index i corresponds to value -i (1..50)
    for (let i = 0; i < k; i++) {
        if (nums[i] < 0) freq[-nums[i]]++;
    }
    const res: number[] = [];
    for (let start = 0; start <= n - k; start++) {
        let cnt = 0;
        let beauty = 0;
        for (let idx = 50; idx >= 1; idx--) {
            cnt += freq[idx];
            if (cnt >= x) {
                beauty = -idx;
                break;
            }
        }
        res.push(beauty);
        if (start + k < n) {
            const outVal = nums[start];
            if (outVal < 0) freq[-outVal]--;
            const inVal = nums[start + k];
            if (inVal < 0) freq[-inVal]++;
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
     * @param Integer $x
     * @return Integer[]
     */
    function getSubarrayBeauty($nums, $k, $x) {
        $n = count($nums);
        // frequency for values -50 .. 0 (we only use -50..-1)
        $freq = array_fill(0, 51, 0); // index = value + 50
        // initial window
        for ($i = 0; $i < $k; $i++) {
            $v = $nums[$i];
            if ($v < 0) {
                $freq[$v + 50]++;
            }
        }

        $result = [];
        $windows = $n - $k + 1;
        for ($start = 0; $start < $windows; $start++) {
            // find x-th smallest negative
            $cntNeg = 0;
            $beauty = 0;
            for ($idx = 0; $idx < 50; $idx++) { // -50 to -1
                $cntNeg += $freq[$idx];
                if ($cntNeg >= $x) {
                    $beauty = $idx - 50; // convert index back to value
                    break;
                }
            }
            if ($cntNeg < $x) {
                $beauty = 0;
            }
            $result[] = $beauty;

            // slide window
            if ($start + $k < $n) {
                $out = $nums[$start];
                if ($out < 0) {
                    $freq[$out + 50]--;
                }
                $in = $nums[$start + $k];
                if ($in < 0) {
                    $freq[$in + 50]++;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getSubarrayBeauty(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var freq = Array(repeating: 0, count: 50) // indices 0 (-1) to 49 (-50)
        
        for i in 0..<k {
            let v = nums[i]
            if v < 0 {
                freq[-v - 1] += 1
            }
        }
        
        var result = [Int]()
        result.append(kthSmallestNegative(freq, x))
        
        if n == k { return result }
        
        for i in k..<n {
            let outVal = nums[i - k]
            if outVal < 0 {
                freq[-outVal - 1] -= 1
            }
            let inVal = nums[i]
            if inVal < 0 {
                freq[-inVal - 1] += 1
            }
            result.append(kthSmallestNegative(freq, x))
        }
        
        return result
    }
    
    private func kthSmallestNegative(_ freq: [Int], _ x: Int) -> Int {
        var count = 0
        for idx in 0..<freq.count { // -1 to -50
            count += freq[idx]
            if count >= x {
                return -(idx + 1)
            }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSubarrayBeauty(nums: IntArray, k: Int, x: Int): IntArray {
        val n = nums.size
        val res = IntArray(n - k + 1)
        val offset = 50               // maps -50..-1 to 0..49
        val freq = IntArray(offset)   // frequency of negative numbers in current window

        fun add(num: Int) {
            if (num < 0) {
                freq[num + offset]++
            }
        }

        fun remove(num: Int) {
            if (num < 0) {
                freq[num + offset]--
            }
        }

        fun beauty(): Int {
            var cnt = 0
            for (i in 0 until offset) {          // iterate from -50 up to -1
                cnt += freq[i]
                if (cnt >= x) {
                    return i - offset             // convert index back to value
                }
            }
            return 0                               // not enough negatives
        }

        // initial window
        for (i in 0 until k) add(nums[i])
        res[0] = beauty()

        var pos = 1
        for (right in k until n) {
            val left = nums[right - k]
            remove(left)
            add(nums[right])
            res[pos++] = beauty()
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> getSubarrayBeauty(List<int> nums, int k, int x) {
    int n = nums.length;
    // freq[i] stores count of negative number -i (1 <= i <= 50)
    List<int> freq = List.filled(51, 0);
    int negCount = 0;

    for (int i = 0; i < k; i++) {
      if (nums[i] < 0) {
        int idx = -nums[i];
        freq[idx]++;
        negCount++;
      }
    }

    int getBeauty() {
      if (negCount < x) return 0;
      int cum = 0;
      for (int i = 50; i >= 1; i--) {
        cum += freq[i];
        if (cum >= x) return -i;
      }
      return 0;
    }

    List<int> ans = [];
    ans.add(getBeauty());

    for (int start = 0; start < n - k; start++) {
      int outVal = nums[start];
      if (outVal < 0) {
        int idx = -outVal;
        freq[idx]--;
        negCount--;
      }
      int inVal = nums[start + k];
      if (inVal < 0) {
        int idx = -inVal;
        freq[idx]++;
        negCount++;
      }
      ans.add(getBeauty());
    }

    return ans;
  }
}
```

## Golang

```go
func getSubarrayBeauty(nums []int, k int, x int) []int {
	n := len(nums)
	if n == 0 || k == 0 {
		return []int{}
	}
	freq := make([]int, 50) // indices 0..49 correspond to -1 .. -50
	totalNeg := 0

	// initialize first window
	for i := 0; i < k; i++ {
		if nums[i] < 0 {
			idx := -nums[i] - 1
			freq[idx]++
			totalNeg++
		}
	}

	getBeauty := func() int {
		if totalNeg < x {
			return 0
		}
		cnt := 0
		for idx := 0; idx < 50; idx++ {
			cnt += freq[idx]
			if cnt >= x {
				return -(idx + 1)
			}
		}
		return 0
	}

	res := make([]int, 0, n-k+1)
	res = append(res, getBeauty())

	// slide window
	for i := k; i < n; i++ {
		outVal := nums[i-k]
		if outVal < 0 {
			idx := -outVal - 1
			freq[idx]--
			totalNeg--
		}
		inVal := nums[i]
		if inVal < 0 {
			idx := -inVal - 1
			freq[idx]++
			totalNeg++
		}
		res = append(res, getBeauty())
	}

	return res
}
```

## Ruby

```ruby
def get_subarray_beauty(nums, k, x)
  n = nums.length
  freq = Array.new(51, 0) # indices 0..50 correspond to values -50..0 (0 unused for non‑negative)

  # initialize first window
  (0...k).each do |i|
    v = nums[i]
    if v < 0
      freq[v + 50] += 1
    end
  end

  result = []

  (0..n - k).each do |start|
    # find x‑th smallest negative in current window
    cnt = 0
    beauty = 0
    (0...51).each do |idx|
      cnt += freq[idx]
      if cnt >= x
        beauty = idx - 50
        break
      end
    end
    result << beauty

    # slide the window
    if start + k < n
      out_val = nums[start]
      if out_val < 0
        freq[out_val + 50] -= 1
      end
      in_val = nums[start + k]
      if in_val < 0
        freq[in_val + 50] += 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def getSubarrayBeauty(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        val freq = new Array[Int](51) // indices 1..50 correspond to -1 .. -50 (stored by absolute value)
        val n = nums.length

        var i = 0
        while (i < k) {
            val v = nums(i)
            if (v < 0) freq(-v) += 1
            i += 1
        }

        val res = scala.collection.mutable.ArrayBuffer[Int]()

        def beauty(): Int = {
            var cnt = 0
            var idx = 50 // corresponds to -50, the smallest possible negative
            while (idx >= 1) {
                cnt += freq(idx)
                if (cnt >= x) return -idx
                idx -= 1
            }
            0
        }

        res += beauty()

        var start = 0
        var end = k
        while (end < n) {
            val outVal = nums(start)
            if (outVal < 0) freq(-outVal) -= 1

            val inVal = nums(end)
            if (inVal < 0) freq(-inVal) += 1

            start += 1
            end += 1

            res += beauty()
        }

        res.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_subarray_beauty(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let n = nums.len();
        let k_usize = k as usize;
        let x_usize = x as usize;

        // frequencies for values -50..0 (we only use negatives)
        let mut freq = [0i32; 51];
        let mut total_neg: usize = 0;

        // initialize first window
        for i in 0..k_usize {
            let v = nums[i];
            if v < 0 {
                let idx = (v + 50) as usize;
                freq[idx] += 1;
                total_neg += 1;
            }
        }

        fn beauty(freq: &[i32; 51], total_neg: usize, x: usize) -> i32 {
            if total_neg < x {
                return 0;
            }
            let mut cnt = 0usize;
            for idx in 0..51 {
                cnt += freq[idx] as usize;
                if cnt >= x {
                    return (idx as i32) - 50;
                }
            }
            0
        }

        let mut res = Vec::with_capacity(n - k_usize + 1);
        res.push(beauty(&freq, total_neg, x_usize));

        // slide the window
        for i in k_usize..n {
            // remove outgoing element
            let out = nums[i - k_usize];
            if out < 0 {
                let idx = (out + 50) as usize;
                freq[idx] -= 1;
                total_neg -= 1;
            }
            // add incoming element
            let inn = nums[i];
            if inn < 0 {
                let idx = (inn + 50) as usize;
                freq[idx] += 1;
                total_neg += 1;
            }

            res.push(beauty(&freq, total_neg, x_usize));
        }

        res
    }
}
```

## Racket

```racket
(define/contract (get-subarray-beauty nums k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ((arr (list->vector nums))
         (n (vector-length arr))
         (freq (make-vector 51 0))
         (negCount 0))
    ;; initialize first window
    (for ([i (in-range k)])
      (let ((val (vector-ref arr i)))
        (when (< val 0)
          (define idx (- val))
          (vector-set! freq idx (+ 1 (vector-ref freq idx)))
          (set! negCount (+ negCount 1)))))
    ;; helper to compute beauty of current window
    (define (beauty)
      (if (< negCount x)
          0
          (let loop ((i 50) (cnt 0))
            (if (< i 1)
                0
                (let ((newcnt (+ cnt (vector-ref freq i))))
                  (if (>= newcnt x)
                      (- i)
                      (loop (- i 1) newcnt)))))))
    (define result (make-vector (+ 1 (- n k)) 0))
    ;; first window beauty
    (vector-set! result 0 (beauty))
    ;; slide the window
    (for ([i (in-range k n)])
      (let ((out (vector-ref arr (- i k)))
            (in (vector-ref arr i)))
        (when (< out 0)
          (define idx (- out))
          (vector-set! freq idx (- (vector-ref freq idx) 1))
          (set! negCount (- negCount 1)))
        (when (< in 0)
          (define idx (- in))
          (vector-set! freq idx (+ 1 (vector-ref freq idx)))
          (set! negCount (+ negCount 1)))
        (let ((pos (- i k + 1)))
          (vector-set! result pos (beauty)))))
    (vector->list result)))
```

## Erlang

```erlang
-export([get_subarray_beauty/3]).

-spec get_subarray_beauty(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
get_subarray_beauty(Nums, K, X) ->
    InitCounts = lists:foldl(fun(V, Acc) -> update_counts(Acc, V, 1) end,
                             erlang:make_tuple(51, 0),
                             lists:sublist(Nums, K)),
    FirstBeauty = get_beauty(InitCounts, X),
    Rest = lists:nthtail(K, Nums), % elements entering the window
    RevRes = slide(Nums, Rest, InitCounts, X, [FirstBeauty]),
    lists:reverse(RevRes).

%% Update frequency tuple for a value (only negatives) by Delta (+1 or -1)
-spec update_counts(tuple(), integer(), integer()) -> tuple().
update_counts(Cnts, Val, Delta) when Val < 0 ->
    Idx = Val + 51,                     % -50 -> 1, -1 -> 50
    Old = element(Idx, Cnts),
    setelement(Idx, Cnts, Old + Delta);
update_counts(Cnts, _Val, _Delta) ->
    Cnts.

%% Retrieve the x‑th smallest negative number; 0 if not enough negatives
-spec get_beauty(tuple(), integer()) -> integer().
get_beauty(Cnts, X) -> find_beauty(1, 0, Cnts, X).

-spec find_beauty(integer(), integer(), tuple(), integer()) -> integer().
find_beauty(Id, Cum, Cnts, X) when Id =< 50 ->
    C = element(Id, Cnts),
    NewCum = Cum + C,
    if
        NewCum >= X -> Id - 51;          % convert index back to value
        true       -> find_beauty(Id + 1, NewCum, Cnts, X)
    end;
find_beauty(_, _, _, _) ->
    0.

%% Slide the window across the array
-spec slide([integer()], [integer()], tuple(), integer(), [integer()]) -> [integer()].
slide(_OutList, [], _Cnts, _X, Acc) ->
    Acc;
slide(OutList, [InVal|RestIn], Cnts, X, Acc) ->
    OutVal = hd(OutList),
    C1 = update_counts(Cnts, OutVal, -1),
    C2 = update_counts(C1, InVal, 1),
    Beauty = get_beauty(C2, X),
    slide(tl(OutList), RestIn, C2, X, [Beauty|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_subarray_beauty(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def get_subarray_beauty(nums, k, x) do
    n = length(nums)
    arr = :array.from_list(nums)

    init_freq =
      Enum.reduce(0..(k - 1), %{}, fn i, acc ->
        v = :array.get(i, arr)

        if v < 0,
          do: Map.update(acc, v, 1, &(&1 + 1)),
          else: acc
      end)

    beauties_rev = [get_beauty(init_freq, x)]

    {beauties_rev, _} =
      Enum.reduce(k..(n - 1), {beauties_rev, init_freq}, fn i, {list_acc, freq} ->
        out_val = :array.get(i - k, arr)

        freq =
          if out_val < 0 do
            cnt = Map.get(freq, out_val)
            if cnt == 1, do: Map.delete(freq, out_val), else: Map.put(freq, out_val, cnt - 1)
          else
            freq
          end

        in_val = :array.get(i, arr)

        freq =
          if in_val < 0,
            do: Map.update(freq, in_val, 1, &(&1 + 1)),
            else: freq

        beauty = get_beauty(freq, x)
        {[beauty | list_acc], freq}
      end)

    Enum.reverse(beauties_rev)
  end

  defp get_beauty(freq, x) do
    case Enum.reduce_while(-50..-1, 0, fn v, acc ->
           cnt = Map.get(freq, v, 0)
           new_acc = acc + cnt

           if new_acc >= x,
             do: {:halt, v},
             else: {:cont, new_acc}
         end) do
      nil -> 0
      val -> val
    end
  end
end
```
