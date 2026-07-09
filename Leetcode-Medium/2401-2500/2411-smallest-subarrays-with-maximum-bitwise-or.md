# 2411. Smallest Subarrays With Maximum Bitwise OR

## Cpp

```cpp
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        const int B = 31; // bits for numbers up to 1e9
        int n = nums.size();
        vector<int> pos(B, -1);
        vector<int> ans(n);
        for (int i = n - 1; i >= 0; --i) {
            int far = i;
            for (int b = 0; b < B; ++b) {
                if ((nums[i] >> b) & 1) continue;
                if (pos[b] != -1) far = max(far, pos[b]);
            }
            ans[i] = far - i + 1;
            for (int b = 0; b < B; ++b) {
                if ((nums[i] >> b) & 1) pos[b] = i;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] smallestSubarrays(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        int[] nextPos = new int[31];
        for (int b = 0; b < 31; b++) nextPos[b] = -1;

        for (int i = n - 1; i >= 0; i--) {
            int maxPos = -1;
            int val = nums[i];
            for (int b = 0; b < 31; b++) {
                if ((val & (1 << b)) == 0) {
                    if (nextPos[b] != -1 && nextPos[b] > maxPos) {
                        maxPos = nextPos[b];
                    }
                }
            }
            ans[i] = (maxPos == -1) ? 1 : (maxPos - i + 1);
            // update positions for bits that are set in nums[i]
            for (int b = 0; b < 31; b++) {
                if ((val & (1 << b)) != 0) {
                    nextPos[b] = i;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # positions of next occurrence of each bit set to 1
        pos = [-1] * 31
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            max_pos = i
            val = nums[i]
            # check bits that are 0 in current value
            missing = (~val) & ((1 << 31) - 1)
            b = 0
            while missing:
                if missing & 1:
                    p = pos[b]
                    if p != -1 and p > max_pos:
                        max_pos = p
                missing >>= 1
                b += 1
            # also need to consider bits where val has 0 but we didn't iterate because higher bits beyond 30 are irrelevant (they're always zero)
            ans[i] = max_pos - i + 1

            # update positions for bits that are 1 in current value
            v = val
            b = 0
            while v:
                if v & 1:
                    pos[b] = i
                v >>= 1
                b += 1

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # positions of the most recent occurrence (to the right) of each bit set to 1
        pos = [-1] * 31  # bits 0..30 sufficient for nums[i] <= 1e9
        
        for i in range(n - 1, -1, -1):
            far = i
            x = nums[i]
            # determine the furthest needed index to cover all missing bits
            for b in range(31):
                if (x >> b) & 1:
                    continue
                p = pos[b]
                if p != -1 and p > far:
                    far = p
            ans[i] = far - i + 1
            # update positions for bits present at current index
            for b in range(31):
                if (x >> b) & 1:
                    pos[b] = i
        return ans
```

## C

```c
#include <stdlib.h>

int* smallestSubarrays(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* ans = (int*)malloc(numsSize * sizeof(int));
    if (!ans) return NULL;

    const int BITS = 31; // enough for numbers up to 1e9
    int pos[BITS];
    for (int b = 0; b < BITS; ++b) pos[b] = -1;

    for (int i = numsSize - 1; i >= 0; --i) {
        int right = i;
        int val = nums[i];

        // Determine farthest needed position
        for (int b = 0; b < BITS; ++b) {
            if ((val >> b) & 1) continue;          // bit already set
            if (pos[b] != -1 && pos[b] > right) {
                right = pos[b];
            }
        }

        ans[i] = right - i + 1;

        // Update positions of bits that are set in current number
        for (int b = 0; b < BITS; ++b) {
            if ((val >> b) & 1) {
                pos[b] = i;
            }
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SmallestSubarrays(int[] nums) {
        int n = nums.Length;
        int[] answer = new int[n];
        const int BITS = 31; // since nums[i] <= 1e9 < 2^30
        int[] nextPos = new int[BITS];
        for (int b = 0; b < BITS; ++b) nextPos[b] = -1;

        for (int i = n - 1; i >= 0; --i) {
            int farthest = i;
            int val = nums[i];
            // Determine the farthest needed position for bits not set in current value
            for (int b = 0; b < BITS; ++b) {
                if (((val >> b) & 1) == 0 && nextPos[b] != -1) {
                    if (nextPos[b] > farthest) farthest = nextPos[b];
                }
            }
            answer[i] = farthest - i + 1;

            // Update positions for bits that are set in current value
            for (int b = 0; b < BITS; ++b) {
                if (((val >> b) & 1) == 1) {
                    nextPos[b] = i;
                }
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestSubarrays = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    const nextPos = new Array(31).fill(-1); // positions of next 1 for each bit
    
    for (let i = n - 1; i >= 0; --i) {
        let far = i;
        const val = nums[i];
        // Determine the farthest needed position based on bits that are 0 here
        for (let b = 0; b < 31; ++b) {
            if (((val >>> b) & 1) === 0) {
                const pos = nextPos[b];
                if (pos !== -1 && pos > far) far = pos;
            }
        }
        ans[i] = far - i + 1;
        // Update positions for bits that are 1 at current index
        for (let b = 0; b < 31; ++b) {
            if (((val >>> b) & 1) === 1) {
                nextPos[b] = i;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function smallestSubarrays(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array<number>(n);
    const pos = new Array<number>(31).fill(-1);
    for (let i = n - 1; i >= 0; --i) {
        let maxPos = i;
        const v = nums[i];
        for (let b = 0; b < 31; ++b) {
            if (((v >>> b) & 1) === 0) {
                const p = pos[b];
                if (p !== -1 && p > maxPos) maxPos = p;
            }
        }
        ans[i] = maxPos - i + 1;
        for (let b = 0; b < 31; ++b) {
            if (((v >>> b) & 1) === 1) {
                pos[b] = i;
            }
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
     * @return Integer[]
     */
    function smallestSubarrays($nums) {
        $n = count($nums);
        $pos = array_fill(0, 31, -1);
        $ans = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $right = $i;
            $val = $nums[$i];
            // Determine farthest needed position for bits not set in current value
            for ($b = 0; $b < 31; ++$b) {
                if ((($val >> $b) & 1) == 0 && $pos[$b] != -1) {
                    if ($pos[$b] > $right) {
                        $right = $pos[$b];
                    }
                }
            }
            $ans[$i] = $right - $i + 1;
            // Update latest positions for bits that are set
            for ($b = 0; $b < 31; ++$b) {
                if ((($val >> $b) & 1) == 1) {
                    $pos[$b] = $i;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func smallestSubarrays(_ nums: [Int]) -> [Int] {
        let n = nums.count
        let B = 31   // enough for numbers up to 1e9
        var pos = Array(repeating: -1, count: B)
        var ans = Array(repeating: 0, count: n)
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            let val = nums[i]
            var maxPos = i
            // Determine farthest needed index for bits that are currently 0
            for b in 0..<B {
                if ((val >> b) & 1) == 0 {
                    let p = pos[b]
                    if p != -1 && p > maxPos {
                        maxPos = p
                    }
                }
            }
            ans[i] = maxPos - i + 1
            // Update positions for bits that are 1 at current index
            for b in 0..<B {
                if ((val >> b) & 1) == 1 {
                    pos[b] = i
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestSubarrays(nums: IntArray): IntArray {
        val n = nums.size
        val answer = IntArray(n)
        val nextPos = IntArray(31) { -1 }
        for (i in n - 1 downTo 0) {
            var far = i
            val value = nums[i]
            for (b in 0..30) {
                if (((value shr b) and 1) == 0) {
                    val p = nextPos[b]
                    if (p != -1 && p > far) far = p
                }
            }
            answer[i] = far - i + 1
            for (b in 0..30) {
                if (((value shr b) and 1) == 1) {
                    nextPos[b] = i
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> smallestSubarrays(List<int> nums) {
    const int BITS = 31;
    int n = nums.length;
    List<int> pos = List.filled(BITS, -1);
    List<int> ans = List.filled(n, 0);
    for (int i = n - 1; i >= 0; --i) {
      int far = i;
      int val = nums[i];
      for (int b = 0; b < BITS; ++b) {
        if ((val & (1 << b)) == 0 && pos[b] != -1) {
          if (pos[b] > far) far = pos[b];
        }
      }
      ans[i] = far - i + 1;
      for (int b = 0; b < BITS; ++b) {
        if ((val & (1 << b)) != 0) {
          pos[b] = i;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func smallestSubarrays(nums []int) []int {
    n := len(nums)
    ans := make([]int, n)
    const B = 31
    pos := make([]int, B)
    for i := 0; i < B; i++ {
        pos[i] = -1
    }
    for i := n - 1; i >= 0; i-- {
        maxPos := i
        x := nums[i]
        for b := 0; b < B; b++ {
            if (x>>b)&1 == 0 && pos[b] != -1 && pos[b] > maxPos {
                maxPos = pos[b]
            }
        }
        ans[i] = maxPos - i + 1
        for b := 0; b < B; b++ {
            if (x>>b)&1 == 1 {
                pos[b] = i
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def smallest_subarrays(nums)
  n = nums.length
  pos = Array.new(31, -1)
  ans = Array.new(n, 1)

  (n - 1).downto(0) do |i|
    right = i
    val = nums[i]

    0.upto(30) do |b|
      if ((val >> b) & 1) == 0 && pos[b] != -1
        right = pos[b] if pos[b] > right
      end
    end

    ans[i] = right - i + 1

    0.upto(30) do |b|
      pos[b] = i if ((val >> b) & 1) == 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def smallestSubarrays(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val ans = new Array[Int](n)
        val lastPos = Array.fill(31)(-1) // positions of most recent 1 for each bit
        var i = n - 1
        while (i >= 0) {
            var maxIdx = i
            val x = nums(i)
            var b = 0
            while (b < 31) {
                if ((x & (1 << b)) == 0) {
                    val p = lastPos(b)
                    if (p != -1 && p > maxIdx) maxIdx = p
                }
                b += 1
            }
            ans(i) = maxIdx - i + 1
            b = 0
            while (b < 31) {
                if ((x & (1 << b)) != 0) {
                    lastPos(b) = i
                }
                b += 1
            }
            i -= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_subarrays(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut answer = vec![0i32; n];
        // positions of the most recent occurrence (to the right) of each bit set to 1
        let mut pos = [-1i32; 31]; // bits 0..30

        for i in (0..n).rev() {
            let val = nums[i];
            let mut far = i as i32;

            // Determine the furthest needed position for bits that are 0 at current index
            for b in 0..31 {
                if ((val >> b) & 1) == 0 {
                    let p = pos[b];
                    if p != -1 && p > far {
                        far = p;
                    }
                }
            }

            answer[i] = far - i as i32 + 1;

            // Update positions for bits that are 1 at current index
            for b in 0..31 {
                if ((val >> b) & 1) == 1 {
                    pos[b] = i as i32;
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (smallest-subarrays nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([v (list->vector nums)]
         [n (vector-length v)]
         [pos (make-vector 31 -1)]
         [ans (make-vector n)])
    (for ([i (in-range (sub1 n) -1 -1)]) ; i from n-1 down to 0
      (define num (vector-ref v i))
      (define need i)
      ;; determine farthest needed position for bits that are 0 in num
      (for ([bit (in-range 31)])
        (when (= (bitwise-and (arithmetic-shift num (- bit)) 1) 0)
          (let ([p (vector-ref pos bit)])
            (when (>= p 0)
              (set! need (max need p))))))
      ;; store answer length
      (vector-set! ans i (+ (- need i) 1))
      ;; update positions for bits that are 1 in num
      (for ([bit (in-range 31)])
        (when (= (bitwise-and (arithmetic-shift num (- bit)) 1) 1)
          (vector-set! pos bit i))))
    (vector->list ans)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_subarrays/1]).

-spec smallest_subarrays(Nums :: [integer()]) -> [integer()].
smallest_subarrays(Nums) ->
    N = length(Nums),
    NumArr = list_to_tuple(Nums),
    PosInit = list_to_tuple(lists:duplicate(31, -1)),
    AnswersRev = loop(N-1, PosInit, [], NumArr),
    lists:reverse(AnswersRev).

loop(I, _Pos, Acc, _NumArr) when I < 0 ->
    Acc;
loop(I, Pos, Acc, NumArr) ->
    Num = element(I+1, NumArr),
    NeedPos = compute_need(Num, Pos, I),
    Len = NeedPos - I + 1,
    NewAcc = [Len | Acc],
    UpdatedPos = update_pos(Num, Pos, I),
    loop(I-1, UpdatedPos, NewAcc, NumArr).

compute_need(Num, PosTuple, I) ->
    compute_need_bit(0, Num, PosTuple, I, I).

compute_need_bit(31, _Num, _PosTuple, MaxPos, _I) ->
    MaxPos;
compute_need_bit(Bit, Num, PosTuple, I, MaxPos) ->
    Mask = 1 bsl Bit,
    case (Num band Mask) of
        0 ->
            Pos = element(Bit+1, PosTuple),
            NewMax = if Pos =/= -1, Pos > MaxPos -> Pos; true -> MaxPos end,
            compute_need_bit(Bit+1, Num, PosTuple, I, NewMax);
        _ ->
            compute_need_bit(Bit+1, Num, PosTuple, I, MaxPos)
    end.

update_pos(Num, PosTuple, I) ->
    update_pos_bit(0, Num, PosTuple, I).

update_pos_bit(31, _Num, PosTuple, _I) ->
    PosTuple;
update_pos_bit(Bit, Num, PosTuple, I) ->
    Mask = 1 bsl Bit,
    case (Num band Mask) of
        0 ->
            update_pos_bit(Bit+1, Num, PosTuple, I);
        _ ->
            NewPosTuple = setelement(Bit+1, PosTuple, I),
            update_pos_bit(Bit+1, Num, NewPosTuple, I)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_subarrays(nums :: [integer]) :: [integer]
  def smallest_subarrays(nums) do
    import Bitwise

    n = length(nums)
    init_pos = for _ <- 0..30, do: -1

    {_pos, answers_rev} =
      nums
      |> Enum.reverse()
      |> Enum.with_index()
      |> Enum.reduce({init_pos, []}, fn {val, rev_idx}, {pos, ans_rev} ->
        i = n - 1 - rev_idx

        max_pos =
          Enum.reduce(0..30, i, fn b, acc ->
            if ((val >>> b) &&& 1) == 0 do
              p = Enum.at(pos, b)

              if p != -1 and p > acc do
                p
              else
                acc
              end
            else
              acc
            end
          end)

        len = max_pos - i + 1

        new_pos =
          Enum.map(0..30, fn b ->
            if ((val >>> b) &&& 1) == 1, do: i, else: Enum.at(pos, b)
          end)

        {new_pos, [len | ans_rev]}
      end)

    Enum.reverse(answers_rev)
  end
end
```
