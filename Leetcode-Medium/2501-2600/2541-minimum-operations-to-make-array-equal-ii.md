# 2541. Minimum Operations to Make Array Equal II

## Cpp

```cpp
class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2, int k) {
        if (k == 0) {
            for (size_t i = 0; i < nums1.size(); ++i)
                if (nums1[i] != nums2[i]) return -1;
            return 0;
        }
        long long inc = 0, dec = 0;
        for (size_t i = 0; i < nums1.size(); ++i) {
            long long diff = static_cast<long long>(nums2[i]) - nums1[i];
            if (diff % k != 0) return -1;
            long long units = diff / k;
            if (units > 0) inc += units;
            else dec -= units; // units negative
        }
        return inc == dec ? inc : -1;
    }
};
```

## Java

```java
class Solution {
    public long minOperations(int[] nums1, int[] nums2, int k) {
        if (k == 0) {
            for (int i = 0; i < nums1.length; i++) {
                if (nums1[i] != nums2[i]) return -1;
            }
            return 0L;
        }
        long inc = 0, dec = 0;
        for (int i = 0; i < nums1.length; i++) {
            long diff = (long) nums2[i] - nums1[i];
            if (diff % k != 0) return -1;
            long cnt = diff / k;
            if (cnt > 0) inc += cnt;
            else dec -= cnt; // cnt is negative
        }
        if (inc != dec) return -1;
        return inc;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0 if nums1 == nums2 else -1

        total_pos = 0
        for a, b in zip(nums1, nums2):
            diff = a - b
            if diff % k != 0:
                return -1
            if diff > 0:
                total_pos += diff // k
            elif diff < 0:
                # we could also accumulate negatives to verify sum zero,
                # but checking total positive equals total negative later.
                pass

        # Verify that total surplus equals total deficit
        total_neg = 0
        for a, b in zip(nums1, nums2):
            diff = a - b
            if diff < 0:
                total_neg += (-diff) // k

        return total_pos if total_pos == total_neg else -1
```

## Python3

```python
class Solution:
    def minOperations(self, nums1, nums2, k):
        if k == 0:
            return 0 if nums1 == nums2 else -1

        inc = dec = 0
        for a, b in zip(nums1, nums2):
            diff = b - a
            if diff % k != 0:
                return -1
            d = diff // k
            if d > 0:
                inc += d
            else:
                dec -= d  # d is negative

        return inc if inc == dec else -1
```

## C

```c
long long minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    if (k == 0) {
        for (int i = 0; i < nums1Size; ++i) {
            if (nums1[i] != nums2[i]) return -1;
        }
        return 0;
    }
    
    long long pos = 0, neg = 0;
    for (int i = 0; i < nums1Size; ++i) {
        long long diff = (long long)nums2[i] - (long long)nums1[i];
        if (diff % k != 0) return -1;
        long long delta = diff / k;
        if (delta > 0) pos += delta;
        else if (delta < 0) neg -= delta; // add absolute value
    }
    
    if (pos != neg) return -1;
    return pos;
}
```

## Csharp

```csharp
public class Solution {
    public long MinOperations(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        long sum1 = 0, sum2 = 0;
        foreach (int v in nums1) sum1 += v;
        foreach (int v in nums2) sum2 += v;
        if (sum1 != sum2) return -1;
        if (k == 0) {
            for (int i = 0; i < n; i++) {
                if (nums1[i] != nums2[i]) return -1;
            }
            return 0;
        }
        long ops = 0;
        long kk = k;
        for (int i = 0; i < n; i++) {
            long diff = (long)nums1[i] - nums2[i];
            if (diff % kk != 0) return -1;
            if (diff > 0) ops += diff / kk;
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums1, nums2, k) {
    if (k === 0) {
        for (let i = 0; i < nums1.length; ++i) {
            if (nums1[i] !== nums2[i]) return -1;
        }
        return 0;
    }
    let inc = 0, dec = 0;
    for (let i = 0; i < nums1.length; ++i) {
        const diff = nums2[i] - nums1[i];
        if (diff % k !== 0) return -1;
        const units = diff / k;
        if (units > 0) inc += units;
        else if (units < 0) dec -= units; // add absolute value
    }
    return inc === dec ? inc : -1;
};
```

## Typescript

```typescript
function minOperations(nums1: number[], nums2: number[], k: number): number {
    if (k === 0) {
        for (let i = 0; i < nums1.length; ++i) {
            if (nums1[i] !== nums2[i]) return -1;
        }
        return 0;
    }
    let ops = 0;
    const n = nums1.length;
    for (let i = 0; i < n; ++i) {
        const diff = nums2[i] - nums1[i];
        if (diff % k !== 0) return -1;
        if (diff > 0) ops += diff / k;
    }
    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums1, $nums2, $k) {
        $n = count($nums1);
        if ($k == 0) {
            for ($i = 0; $i < $n; $i++) {
                if ($nums1[$i] !== $nums2[$i]) {
                    return -1;
                }
            }
            return 0;
        }

        $posSum = 0;
        $totalDiff = 0;

        for ($i = 0; $i < $n; $i++) {
            $d = $nums1[$i] - $nums2[$i];
            $totalDiff += $d;

            if ($d % $k !== 0) {
                return -1;
            }
            if ($d > 0) {
                $posSum += $d;
            }
        }

        if ($totalDiff !== 0) {
            return -1;
        }

        return intdiv($posSum, $k);
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        if k == 0 {
            return nums1.elementsEqual(nums2) ? 0 : -1
        }
        var operations = 0
        for (a, b) in zip(nums1, nums2) {
            let diff = b - a
            if diff % k != 0 { return -1 }
            if diff > 0 {
                operations += diff / k
            }
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray, k: Int): Long {
        if (k == 0) {
            for (i in nums1.indices) {
                if (nums1[i] != nums2[i]) return -1L
            }
            return 0L
        }
        val kk = k.toLong()
        var totalPos = 0L
        var sumDiff = 0L
        for (i in nums1.indices) {
            val diff = nums2[i].toLong() - nums1[i].toLong()
            if (diff % kk != 0L) return -1L
            sumDiff += diff
            if (diff > 0) totalPos += diff / kk
        }
        if (sumDiff != 0L) return -1L
        return totalPos
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums1, List<int> nums2, int k) {
    if (k == 0) {
      for (int i = 0; i < nums1.length; ++i) {
        if (nums1[i] != nums2[i]) return -1;
      }
      return 0;
    }
    int pos = 0;
    int neg = 0;
    for (int i = 0; i < nums1.length; ++i) {
      int diff = nums2[i] - nums1[i];
      if (diff % k != 0) return -1;
      int cnt = diff ~/ k;
      if (cnt > 0) {
        pos += cnt;
      } else if (cnt < 0) {
        neg -= cnt; // add absolute value
      }
    }
    return pos == neg ? pos : -1;
  }
}
```

## Golang

```go
func minOperations(nums1 []int, nums2 []int, k int) int64 {
	if k == 0 {
		for i := range nums1 {
			if nums1[i] != nums2[i] {
				return -1
			}
		}
		return 0
	}
	var totalPos int64
	var sumDiff int64
	kk := int64(k)
	for i := 0; i < len(nums1); i++ {
		diff := int64(nums2[i]) - int64(nums1[i])
		if diff%kk != 0 {
			return -1
		}
		if diff > 0 {
			totalPos += diff / kk
		}
		sumDiff += diff
	}
	if sumDiff != 0 {
		return -1
	}
	return totalPos
}
```

## Ruby

```ruby
def min_operations(nums1, nums2, k)
  return 0 if nums1 == nums2
  if k == 0
    return -1
  end

  inc = 0
  dec = 0
  n = nums1.length
  i = 0
  while i < n
    diff = nums1[i] - nums2[i]
    return -1 unless diff % k == 0
    units = diff / k
    if units > 0
      dec += units
    elsif units < 0
      inc -= units
    end
    i += 1
  end

  dec == inc ? dec : -1
end
```

## Scala

```scala
object Solution {
    def minOperations(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
        if (k == 0) {
            var i = 0
            while (i < nums1.length && nums1(i) == nums2(i)) i += 1
            return if (i == nums1.length) 0L else -1L
        }
        val kk = k.toLong
        var posSum: Long = 0L
        var negSum: Long = 0L
        var totalDiff: Long = 0L

        var i = 0
        while (i < nums1.length) {
            val diff = nums2(i).toLong - nums1(i).toLong
            if (diff % kk != 0) return -1L
            if (diff > 0) posSum += diff
            else if (diff < 0) negSum -= diff // add absolute value
            totalDiff += diff
            i += 1
        }

        if (totalDiff != 0) return -1L
        // posSum equals negSum when totalDiff == 0
        posSum / kk
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        if k == 0 {
            for (a, b) in nums1.iter().zip(nums2.iter()) {
                if a != b {
                    return -1;
                }
            }
            return 0;
        }
        let k_i64 = k as i64;
        let mut pos_sum: i64 = 0;
        let mut total_diff: i64 = 0;
        for (a, b) in nums1.iter().zip(nums2.iter()) {
            let d = *b as i64 - *a as i64;
            if d % k_i64 != 0 {
                return -1;
            }
            if d > 0 {
                pos_sum += d;
            }
            total_diff += d;
        }
        if total_diff != 0 {
            return -1;
        }
        pos_sum / k_i64
    }
}
```

## Racket

```racket
(define/contract (min-operations nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (cond
    [(zero? k) (if (equal? nums1 nums2) 0 -1)]
    [else
     (let loop ((i 0) (pos 0) (neg 0))
       (if (= i (length nums1))
           (if (= pos neg) pos -1)
           (let* ((a (list-ref nums1 i))
                  (b (list-ref nums2 i))
                  (diff (- a b)))
             (if (not (zero? (remainder diff k)))
                 -1
                 (let ((units (/ diff k)))
                   (cond [(positive? units) (loop (+ i 1) (+ pos units) neg)]
                         [(negative? units) (loop (+ i 1) pos (+ neg (- units)))]
                         [else (loop (+ i 1) pos neg)]))))))]))
```

## Erlang

```erlang
-spec min_operations(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
min_operations(Nums1, Nums2, K) when K == 0 ->
    case Nums1 =:= Nums2 of
        true -> 0;
        false -> -1
    end;
min_operations(Nums1, Nums2, K) ->
    case loop(Nums1, Nums2, 0, 0, K) of
        {Pos, Neg} when Pos == Neg -> Pos;
        _ -> -1
    end.

loop([], [], Pos, Neg, _) -> {Pos, Neg};
loop([A|As], [B|Bs], PosAcc, NegAcc, K) ->
    Diff = B - A,
    case Diff rem K of
        0 ->
            Steps = Diff div K,
            if Steps >= 0 ->
                    loop(As, Bs, PosAcc + Steps, NegAcc, K);
               true ->
                    loop(As, Bs, PosAcc, NegAcc - Steps, K)
            end;
        _ -> {error}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def min_operations(nums1, nums2, k) do
    if k == 0 do
      if nums1 == nums2, do: 0, else: -1
    else
      case Enum.reduce_while(Enum.zip(nums1, nums2), {0, 0}, fn {a, b}, {inc, dec} ->
             diff = b - a

             if rem(diff, k) != 0 do
               {:halt, :invalid}
             else
               unit = div(diff, k)

               cond do
                 unit > 0 -> {:cont, {inc + unit, dec}}
                 unit < 0 -> {:cont, {inc, dec - unit}} # subtract negative => add abs
                 true -> {:cont, {inc, dec}}
               end
             end
           end) do
        :invalid ->
          -1

        {inc, dec} ->
          if inc == dec, do: inc, else: -1
      end
    end
  end
end
```
