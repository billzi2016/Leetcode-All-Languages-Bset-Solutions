# 3576. Transform Array to All Equal Elements

## Cpp

```cpp
class Solution {
public:
    bool canMakeEqual(vector<int>& nums, int k) {
        int cntNeg = 0, cntPos = 0;
        for (int x : nums) {
            if (x == -1) ++cntNeg;
            else ++cntPos;
        }
        return min(cntNeg, cntPos) <= k;
    }
};
```

## Java

```java
class Solution {
    public boolean canMakeEqual(int[] nums, int k) {
        return canTransform(nums, k, 1) || canTransform(nums, k, -1);
    }

    private boolean canTransform(int[] nums, int k, int target) {
        int n = nums.length;
        int[] diff = new int[n + 1]; // diff[i] indicates flip parity change at i
        int curFlip = 0; // current parity of flips affecting position i

        for (int i = 0; i < n; i++) {
            curFlip ^= diff[i];
            int val = nums[i];
            if ((curFlip & 1) == 1) {
                val = -val;
            }
            if (val != target) {
                // need to flip starting at i
                if (i + k > n) {
                    return false;
                }
                curFlip ^= 1;          // apply flip effect from i onward
                diff[i + k] ^= 1;      // schedule removal of this flip after window ends
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canMakeEqual(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cnt_pos = sum(1 for x in nums if x == 1)
        cnt_neg = len(nums) - cnt_pos
        return min(cnt_pos, cnt_neg) <= k
```

## Python3

```python
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        cnt_pos = sum(1 for x in nums if x == 1)
        cnt_neg = len(nums) - cnt_pos
        return min(cnt_pos, cnt_neg) <= k
```

## C

```c
bool canMakeEqual(int* nums, int numsSize, int k) {
    int cntNeg = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == -1) cntNeg++;
    }
    int cntPos = numsSize - cntNeg;
    return (cntNeg <= k) || (cntPos <= k);
}
```

## Csharp

```csharp
public class Solution {
    public bool CanMakeEqual(int[] nums, int k) {
        int neg = 0;
        foreach (int x in nums) {
            if (x == -1) neg++;
        }
        int pos = nums.Length - neg;
        return Math.Min(neg, pos) <= k;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canMakeEqual = function(nums, k) {
    let pos = 0, neg = 0;
    for (const v of nums) {
        if (v === 1) pos++;
        else neg++;
    }
    return Math.min(pos, neg) <= k;
};
```

## Typescript

```typescript
function canMakeEqual(nums: number[], k: number): boolean {
    let pos = 0;
    for (const v of nums) {
        if (v === 1) pos++;
    }
    const neg = nums.length - pos;
    return Math.min(pos, neg) <= k;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function canMakeEqual($nums, $k) {
        $n = count($nums);
        // If array has only one element, it's already equal.
        if ($n == 1) {
            return true;
        }

        foreach ([1, -1] as $target) {
            $arr = $nums;   // make a copy
            $ops = 0;
            for ($i = 0; $i < $n - 1; $i++) {
                if ($arr[$i] != $target) {
                    // flip current and next element
                    $arr[$i] = -$arr[$i];
                    $arr[$i + 1] = -$arr[$i + 1];
                    $ops++;
                    if ($ops > $k) {
                        break; // no need to continue, exceeds limit
                    }
                }
            }
            if ($ops <= $k && $arr[$n - 1] == $target) {
                return true;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canMakeEqual(_ nums: [Int], _ k: Int) -> Bool {
        var minusCount = 0
        for num in nums {
            if num == -1 { minusCount += 1 }
        }
        let plusCount = nums.count - minusCount
        return min(minusCount, plusCount) <= k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakeEqual(nums: IntArray, k: Int): Boolean {
        var negGroups = 0
        var posGroups = 0
        for (i in nums.indices) {
            if (nums[i] == -1 && (i == 0 || nums[i - 1] != -1)) {
                negGroups++
            }
            if (nums[i] == 1 && (i == 0 || nums[i - 1] != 1)) {
                posGroups++
            }
        }
        val minOps = kotlin.math.min(negGroups, posGroups)
        return minOps <= k
    }
}
```

## Dart

```dart
class Solution {
  bool canMakeEqual(List<int> nums, int k) {
    int countNeg = 0;
    for (int v in nums) {
      if (v == -1) countNeg++;
    }
    int countPos = nums.length - countNeg;
    int minFlips = countNeg < countPos ? countNeg : countPos;
    return minFlips <= k;
  }
}
```

## Golang

```go
func canMakeEqual(nums []int, k int) bool {
    pos, neg := 0, 0
    for _, v := range nums {
        if v == 1 {
            pos++
        } else {
            neg++
        }
    }
    minOps := pos
    if neg < minOps {
        minOps = neg
    }
    return minOps <= k
}
```

## Ruby

```ruby
def can_make_equal(nums, k)
  cnt_pos = 0
  nums.each { |v| cnt_pos += 1 if v == 1 }
  cnt_neg = nums.length - cnt_pos
  [cnt_pos, cnt_neg].min <= k
end
```

## Scala

```scala
object Solution {
    def canMakeEqual(nums: Array[Int], k: Int): Boolean = {
        val n = nums.length

        def minFlips(target: Int): Int = {
            val diff = new Array[Int](n)
            var curParity = 0 // 0 means even number of flips affecting current position
            var ops = 0
            var i = 0
            while (i < n) {
                if (i >= k) {
                    curParity ^= diff(i - k)
                }
                var v = nums(i)
                if ((curParity & 1) == 1) v = -v
                if (v != target) {
                    if (i + k > n) return Int.MaxValue // cannot flip a full window
                    ops += 1
                    curParity ^= 1
                    diff(i) = 1
                }
                i += 1
            }
            ops
        }

        val flipsToOne = minFlips(1)
        if (flipsToOne <= k) return true
        val flipsToMinusOne = minFlips(-1)
        flipsToMinusOne <= k
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_make_equal(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k_usize = k as usize;
        // helper closure to compute minimum flips needed to make all elements equal to target
        let min_flips = |target: i32| -> Option<usize> {
            let mut diff = vec![0u8; n + 1];
            let mut flip = 0u8;
            let mut ops = 0usize;
            for i in 0..n {
                flip ^= diff[i];
                let cur = if flip == 0 { nums[i] } else { -nums[i] };
                if cur != target {
                    if i + k_usize > n {
                        return None; // impossible
                    }
                    ops += 1;
                    flip ^= 1;
                    diff[i + k_usize] ^= 1;
                }
            }
            Some(ops)
        };

        if let Some(ops) = min_flips(1) {
            if ops <= k as usize {
                return true;
            }
        }
        if let Some(ops) = min_flips(-1) {
            if ops <= k as usize {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (can-make-equal nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ([counts
          (foldl (lambda (x acc)
                   (if (= x 1)
                       (cons (+ 1 (car acc)) (cdr acc))
                       (cons (car acc) (+ 1 (cdr acc)))))
                 (cons 0 0)
                 nums)]
         [cnt-pos (car counts)]
         [cnt-neg (cadr counts)]
         [min-ops (if (< cnt-pos cnt-neg) cnt-pos cnt-neg)])
    (<= min-ops k)))
```

## Erlang

```erlang
-spec can_make_equal(Nums :: [integer()], K :: integer()) -> boolean().
can_make_equal(Nums, K) ->
    {Pos, Neg} = count_vals(Nums, 0, 0),
    MinOps = erlang:min(Pos, Neg),
    MinOps =< K.

count_vals([], PosAcc, NegAcc) ->
    {PosAcc, NegAcc};
count_vals([H | T], PosAcc, NegAcc) when H == 1 ->
    count_vals(T, PosAcc + 1, NegAcc);
count_vals([_H | T], PosAcc, NegAcc) ->
    % Since the array contains only 1 and -1, any non‑1 is -1
    count_vals(T, PosAcc, NegAcc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_equal(nums :: [integer], k :: integer) :: boolean
  def can_make_equal(nums, k) do
    pos_count = Enum.count(nums, fn x -> x == 1 end)
    neg_count = length(nums) - pos_count
    min_flips = min(pos_count, neg_count)
    min_flips <= k
  end
end
```
