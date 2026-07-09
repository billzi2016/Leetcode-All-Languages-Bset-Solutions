# 0995. Minimum Number of K Consecutive Bit Flips

## Cpp

```cpp
class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        int curFlip = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            if (i >= k && nums[i - k] == 2) {
                --curFlip;
            }
            if ( ((nums[i] + curFlip) & 1) == 0 ) {
                if (i + k > n) return -1;
                ++ans;
                ++curFlip;
                nums[i] = 2; // mark start of a flip
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int flips = 0;
        int curFlip = 0; // number of active flips affecting current position
        for (int i = 0; i < n; i++) {
            if (i >= k && nums[i - k] >= 2) { // a flip started k steps ago ends here
                curFlip--;
            }
            // effective value after current flips: (original + curFlip) % 2
            if ((nums[i] + curFlip) % 2 == 0) { // need to flip at i
                if (i + k > n) {
                    return -1;
                }
                flips++;
                curFlip++;
                nums[i] += 2; // mark that a flip starts here
            }
        }
        return flips;
    }
}
```

## Python

```python
class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cur_flips = 0   # number of active flips affecting current position
        ans = 0
        for i in range(n):
            if i >= k and nums[i - k] == 2:
                cur_flips -= 1
            # effective value after current flips
            if (nums[i] ^ (cur_flips & 1)) == 0:
                if i + k > n:
                    return -1
                ans += 1
                cur_flips += 1
                nums[i] = 2   # mark start of a new flip
        return ans
```

## Python3

```python
class Solution:
    def minKBitFlips(self, nums, k):
        n = len(nums)
        cur_flip = 0
        ans = 0
        for i in range(n):
            if i >= k and nums[i - k] == 2:
                cur_flip -= 1
            # effective bit after current flips: nums[i] ^ (cur_flip & 1)
            # need to flip when this effective bit is 0
            if (nums[i] ^ (cur_flip & 1)) == 0:
                if i + k > n:
                    return -1
                ans += 1
                cur_flip += 1
                nums[i] = 2  # mark that a flip starts here
        return ans
```

## C

```c
int minKBitFlips(int* nums, int numsSize, int k) {
    int curFlip = 0;
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i >= k && nums[i - k] == 2) {
            curFlip--;
        }
        if ((curFlip % 2) == nums[i]) {
            if (i + k > numsSize) return -1;
            ans++;
            curFlip++;
            nums[i] = 2; // mark the start of a flip
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinKBitFlips(int[] nums, int k) {
        int n = nums.Length;
        int curFlip = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i >= k && nums[i - k] >= 2) {
                curFlip--;
            }
            if ((nums[i] + curFlip) % 2 == 0) {
                if (i + k > n) return -1;
                ans++;
                curFlip++;
                nums[i] += 2; // mark start of a flip
            }
        }
        return ans;
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
var minKBitFlips = function(nums, k) {
    const n = nums.length;
    let curFlip = 0; // number of active flips affecting current index
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (i >= k && nums[i - k] === 2) {
            curFlip--;
        }
        // effective value after current flips: (nums[i] + curFlip) % 2
        if ((nums[i] + curFlip) % 2 === 0) { // need to flip
            if (i + k > n) return -1;
            ans++;
            curFlip++;
            nums[i] = 2; // mark start of a new flip
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minKBitFlips(nums: number[], k: number): number {
    const n = nums.length;
    const diff = new Array(n).fill(0); // marks where a flip effect ends
    let curFlip = 0; // parity of flips affecting current position
    let ans = 0;

    for (let i = 0; i < n; i++) {
        if (i >= k) {
            curFlip ^= diff[i - k];
        }
        // effective value after previous flips
        const val = nums[i] ^ curFlip;
        if (val === 0) { // need to flip starting at i
            if (i + k > n) return -1;
            ans++;
            curFlip ^= 1;      // this flip affects upcoming positions
            diff[i] = 1;       // will be removed when window slides past i+k-1
        }
    }
    return ans;
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
    function minKBitFlips($nums, $k) {
        $n = count($nums);
        $flip = 0; // number of active flips affecting current position
        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i >= $k && $nums[$i - $k] == 2) {
                $flip--;
            }
            // If parity of flips equals the original bit, we need to flip here
            if (($flip % 2) == $nums[$i]) {
                if ($i + $k > $n) {
                    return -1;
                }
                $res++;
                $flip++;
                $nums[$i] = 2; // mark start of a new flip
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func minKBitFlips(_ nums: [Int], _ k: Int) -> Int {
        var arr = nums
        let n = arr.count
        var curFlip = 0          // number of active flips affecting current index
        var flipCount = 0
        
        for i in 0..<n {
            if i >= k && arr[i - k] == 2 {
                curFlip -= 1
            }
            // effective bit after considering current flips' parity
            if (arr[i] ^ (curFlip & 1)) == 0 {
                if i + k > n { return -1 }
                arr[i] = 2               // mark start of a new flip
                curFlip += 1
                flipCount += 1
            }
        }
        return flipCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minKBitFlips(nums: IntArray, k: Int): Int {
        val n = nums.size
        var flip = 0          // number of active flips affecting current index
        var ans = 0
        for (i in 0 until n) {
            if (i >= k && nums[i - k] == 2) {
                flip--
            }
            // effective value after applying previous flips
            if ((nums[i] + flip) % 2 == 0) {   // need to be 1, currently 0
                if (i + k > n) return -1
                ans++
                flip++
                nums[i] = 2    // mark the start of a new flip
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minKBitFlips(List<int> nums, int k) {
    int n = nums.length;
    int curFlip = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (i >= k && nums[i - k] == 2) {
        curFlip--;
      }
      if ((curFlip % 2) == nums[i]) {
        if (i + k > n) {
          return -1;
        }
        ans++;
        curFlip++;
        nums[i] = 2;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minKBitFlips(nums []int, k int) int {
	n := len(nums)
	flipCnt := 0   // number of flips affecting current position
	ans := 0

	for i := 0; i < n; i++ {
		if i >= k && nums[i-k] == 2 { // a flip that started k steps ago ends here
			flipCnt--
		}
		// effective value after current flips: nums[i] XOR (flipCnt%2)
		// need it to be 1, so if it's 0 we must flip now
		if nums[i] == (flipCnt & 1) {
			if i+k > n {
				return -1
			}
			ans++
			flipCnt++
			nums[i] = 2 // mark start of a new flip
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_k_bit_flips(nums, k)
  n = nums.length
  cur_flips = 0
  total = 0
  i = 0
  while i < n
    if i >= k && nums[i - k] == 2
      cur_flips -= 1
    end

    # If current effective bit is 0, we need to flip starting here
    if (cur_flips % 2) == nums[i]
      return -1 if i + k > n
      total += 1
      cur_flips += 1
      nums[i] = 2   # mark the start of a flip
    end

    i += 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def minKBitFlips(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        var curFlip = 0          // number of active flips affecting current position
        var ans = 0
        for (i <- 0 until n) {
            if (i >= k && nums(i - k) == 2) {
                curFlip -= 1      // the flip that started at i-k ends here
            }
            // If after applying current flips, the bit is 0, we need to flip starting at i
            if ((curFlip & 1) == nums(i)) {
                if (i + k > n) return -1
                ans += 1
                curFlip += 1
                nums(i) = 2        // mark start of a new flip
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_k_bit_flips(mut nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut flip = 0i32; // current parity of flips affecting position i
        let mut ans = 0i32;

        for i in 0..n {
            if i >= k && nums[i - k] == 2 {
                // a flip that started at i-k ends before i, toggle parity back
                flip ^= 1;
            }
            // effective value after current flips
            if (nums[i] ^ flip) == 0 {
                // need to start a new flip here
                if i + k > n {
                    return -1;
                }
                ans += 1;
                flip ^= 1;          // this flip now affects subsequent positions
                nums[i] = 2;        // mark the start of a flip
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-k-bit-flips nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (flip (make-vector n 0)))
    (let loop ((i 0) (cur 0) (ans 0))
      (cond
        [(= i n) ans]
        [else
         (when (>= i k)
           (set! cur (bitwise-xor cur (vector-ref flip (- i k)))))
         (define effective (bitwise-xor (vector-ref arr i) cur))
         (if (= effective 0)
             (if (> (+ i k) n)
                 -1
                 (begin
                   (vector-set! flip i 1)
                   (set! cur (bitwise-xor cur 1))
                   (loop (+ i 1) cur (+ ans 1))))
             (loop (+ i 1) cur ans))]))))
```

## Erlang

```erlang
-module(solution).
-export([min_k_bit_flips/2]).

-spec min_k_bit_flips(Nums :: [integer()], K :: integer()) -> integer().
min_k_bit_flips(Nums, K) ->
    N = length(Nums),
    Queue = queue:new(),
    process(Nums, 0, 0, Queue, 0, K, N).

process([], _Idx, _CurFlip, _Queue, TotalFlips, _K, _N) ->
    TotalFlips;
process([Num|Rest], Idx, CurFlip0, Queue0, TotalFlips0, K, N) ->
    {Queue1, CurFlip} = expire(Idx, Queue0, CurFlip0),
    Effective = Num bxor CurFlip,
    case Effective of
        0 ->
            if Idx + K > N ->
                    -1;
               true ->
                    NewQueue = queue:in(Idx + K, Queue1),
                    process(Rest, Idx+1, 1 - CurFlip, NewQueue, TotalFlips0+1, K, N)
            end;
        _ ->
            process(Rest, Idx+1, CurFlip, Queue1, TotalFlips0, K, N)
    end.

expire(Index, Queue, CurFlip) ->
    case queue:peek(Queue) of
        {ExpPos, _} when ExpPos =:= Index ->
            {_Val, NewQueue} = queue:out(Queue),
            expire(Index, NewQueue, 1 - CurFlip);
        empty ->
            {Queue, CurFlip};
        _ ->
            {Queue, CurFlip}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_k_bit_flips(nums :: [integer], k :: integer) :: integer
  def min_k_bit_flips(nums, k) do
    n = length(nums)
    q = :queue.new()
    process(Enum.with_index(nums), k, n, q, 0, 0)
  end

  defp process([], _k, _n, _q, _cur_flip, ans), do: ans

  defp process([{num, i} | rest], k, n, q, cur_flip, ans) do
    {q1, cur_flip1} = expire(q, i, cur_flip)

    effective =
      if rem(cur_flip1, 2) == 0 do
        num
      else
        1 - num
      end

    cond do
      effective == 0 ->
        if i + k > n do
          -1
        else
          q2 = :queue.in(i + k, q1)
          process(rest, k, n, q2, cur_flip1 + 1, ans + 1)
        end

      true ->
        process(rest, k, n, q1, cur_flip1, ans)
    end
  end

  defp expire(q, i, cur_flip) do
    case :queue.peek(q) do
      {:value, exp} when exp == i ->
        {{:value, _}, q_rest} = :queue.out(q)
        expire(q_rest, i, cur_flip - 1)

      _ ->
        {q, cur_flip}
    end
  end
end
```
