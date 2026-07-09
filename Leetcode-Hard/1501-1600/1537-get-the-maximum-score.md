# 1537. Get the Maximum Score

## Cpp

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        const long long MOD = 1000000007LL;
        long long sum1 = 0, sum2 = 0, ans = 0;
        size_t i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] == nums2[j]) {
                ans = (ans + max(sum1, sum2) + nums1[i]) % MOD;
                sum1 = sum2 = 0;
                ++i; ++j;
            } else if (nums1[i] < nums2[j]) {
                sum1 += nums1[i++];
            } else {
                sum2 += nums2[j++];
            }
        }
        while (i < nums1.size()) sum1 += nums1[i++];
        while (j < nums2.size()) sum2 += nums2[j++];
        ans = (ans + max(sum1, sum2)) % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int maxSum(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        long sum1 = 0, sum2 = 0, result = 0;
        int n = nums1.length, m = nums2.length;
        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                sum1 += nums1[i++];
            } else if (nums1[i] > nums2[j]) {
                sum2 += nums2[j++];
            } else { // common element
                long maxPrev = Math.max(sum1, sum2);
                result = (result + maxPrev + nums1[i]) % MOD;
                i++;
                j++;
                sum1 = 0;
                sum2 = 0;
            }
        }
        while (i < n) {
            sum1 += nums1[i++];
        }
        while (j < m) {
            sum2 += nums2[j++];
        }
        result = (result + Math.max(sum1, sum2)) % MOD;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        i = j = 0
        sum1 = sum2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 = (sum1 + nums1[i]) % MOD
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 = (sum2 + nums2[j]) % MOD
                j += 1
            else:
                # common element, choose the better path up to here
                best = max(sum1, sum2) + nums1[i]
                best %= MOD
                sum1 = sum2 = best
                i += 1
                j += 1
        while i < n1:
            sum1 = (sum1 + nums1[i]) % MOD
            i += 1
        while j < n2:
            sum2 = (sum2 + nums2[j]) % MOD
            j += 1
        return max(sum1, sum2) % MOD
```

## Python3

```python
from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i = j = 0
        sum1 = sum2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # common element, choose the better path
                best = max(sum1, sum2) + nums1[i]
                sum1 = sum2 = best
                i += 1
                j += 1
        while i < n1:
            sum1 += nums1[i]
            i += 1
        while j < n2:
            sum2 += nums2[j]
            j += 1
        return max(sum1, sum2) % MOD
```

## C

```c
int maxSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    const long long MOD = 1000000007LL;
    long long sum1 = 0, sum2 = 0, ans = 0;
    int i = 0, j = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) {
            sum1 += nums1[i++];
        } else if (nums1[i] > nums2[j]) {
            sum2 += nums2[j++];
        } else {
            long long best = sum1 > sum2 ? sum1 : sum2;
            ans = (ans + best + nums1[i]) % MOD;
            sum1 = 0;
            sum2 = 0;
            i++; j++;
        }
    }
    while (i < nums1Size) {
        sum1 += nums1[i++];
    }
    while (j < nums2Size) {
        sum2 += nums2[j++];
    }
    ans = (ans + (sum1 > sum2 ? sum1 : sum2)) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int MaxSum(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        long sum1 = 0, sum2 = 0, result = 0;
        while (i < nums1.Length && j < nums2.Length) {
            if (nums1[i] < nums2[j]) {
                sum1 += nums1[i];
                i++;
            } else if (nums1[i] > nums2[j]) {
                sum2 += nums2[j];
                j++;
            } else {
                long maxPrev = sum1 > sum2 ? sum1 : sum2;
                result = (result + maxPrev + nums1[i]) % MOD;
                i++; j++;
                sum1 = 0;
                sum2 = 0;
            }
        }
        while (i < nums1.Length) {
            sum1 += nums1[i];
            i++;
        }
        while (j < nums2.Length) {
            sum2 += nums2[j];
            j++;
        }
        result = (result + (sum1 > sum2 ? sum1 : sum2)) % MOD;
        return (int)result;
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
var maxSum = function(nums1, nums2) {
    const MOD = 1000000007;
    let i = 0, j = 0;
    let sum1 = 0, sum2 = 0;
    const n1 = nums1.length, n2 = nums2.length;
    
    while (i < n1 && j < n2) {
        if (nums1[i] < nums2[j]) {
            sum1 += nums1[i];
            i++;
        } else if (nums1[i] > nums2[j]) {
            sum2 += nums2[j];
            j++;
        } else { // equal element, can switch paths
            const best = Math.max(sum1, sum2) + nums1[i];
            sum1 = sum2 = best;
            i++;
            j++;
        }
    }
    
    while (i < n1) {
        sum1 += nums1[i++];
    }
    while (j < n2) {
        sum2 += nums2[j++];
    }
    
    const result = Math.max(sum1, sum2) % MOD;
    return result;
};
```

## Typescript

```typescript
function maxSum(nums1: number[], nums2: number[]): number {
    const MOD = 1000000007;
    let i = 0, j = 0;
    let sum1 = 0, sum2 = 0;

    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            sum1 += nums1[i];
            i++;
        } else if (nums1[i] > nums2[j]) {
            sum2 += nums2[j];
            j++;
        } else {
            const best = Math.max(sum1, sum2) + nums1[i];
            sum1 = sum2 = best;
            i++;
            j++;
        }
    }

    while (i < nums1.length) {
        sum1 += nums1[i];
        i++;
    }
    while (j < nums2.length) {
        sum2 += nums2[j];
        j++;
    }

    return Math.max(sum1, sum2) % MOD;
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
    function maxSum($nums1, $nums2) {
        $mod = 1000000007;
        $i = 0;
        $j = 0;
        $sum1 = 0;
        $sum2 = 0;
        $res = 0;
        $n = count($nums1);
        $m = count($nums2);

        while ($i < $n && $j < $m) {
            if ($nums1[$i] < $nums2[$j]) {
                $sum1 += $nums1[$i];
                $i++;
            } elseif ($nums1[$i] > $nums2[$j]) {
                $sum2 += $nums2[$j];
                $j++;
            } else {
                // common element
                $val = $nums1[$i]; // same as $nums2[$j]
                $res = ($res + max($sum1, $sum2) + $val) % $mod;
                $sum1 = 0;
                $sum2 = 0;
                $i++;
                $j++;
            }
        }

        while ($i < $n) {
            $sum1 += $nums1[$i];
            $i++;
        }

        while ($j < $m) {
            $sum2 += $nums2[$j];
            $j++;
        }

        $res = ($res + max($sum1, $sum2)) % $mod;
        return (int)$res;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let MOD = 1_000_000_007
        var i = 0, j = 0
        var sum1: Int64 = 0
        var sum2: Int64 = 0
        var result: Int64 = 0
        
        while i < nums1.count && j < nums2.count {
            let a = nums1[i]
            let b = nums2[j]
            if a < b {
                sum1 += Int64(a)
                i += 1
            } else if a > b {
                sum2 += Int64(b)
                j += 1
            } else {
                // common element
                let maxPrev = max(sum1, sum2)
                result = (result + maxPrev + Int64(a)) % Int64(MOD)
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
            }
        }
        
        while i < nums1.count {
            sum1 += Int64(nums1[i])
            i += 1
        }
        while j < nums2.count {
            sum2 += Int64(nums2[j])
            j += 1
        }
        
        result = (result + max(sum1, sum2)) % Int64(MOD)
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums1: IntArray, nums2: IntArray): Int {
        val MOD = 1_000_000_007L
        var i = 0
        var j = 0
        var sum1 = 0L
        var sum2 = 0L
        var result = 0L

        while (i < nums1.size && j < nums2.size) {
            val a = nums1[i]
            val b = nums2[j]
            when {
                a < b -> {
                    sum1 += a
                    i++
                }
                a > b -> {
                    sum2 += b
                    j++
                }
                else -> { // a == b, common element
                    result = (result + maxOf(sum1, sum2) + a) % MOD
                    i++; j++
                    sum1 = 0L
                    sum2 = 0L
                }
            }
        }

        while (i < nums1.size) {
            sum1 += nums1[i]
            i++
        }
        while (j < nums2.size) {
            sum2 += nums2[j]
            j++
        }

        result = (result + maxOf(sum1, sum2)) % MOD
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<int> nums1, List<int> nums2) {
    const int MOD = 1000000007;
    int i = 0, j = 0;
    int n = nums1.length, m = nums2.length;
    int sum1 = 0, sum2 = 0;

    while (i < n && j < m) {
      if (nums1[i] < nums2[j]) {
        sum1 += nums1[i];
        i++;
      } else if (nums1[i] > nums2[j]) {
        sum2 += nums2[j];
        j++;
      } else {
        int maxPrev = sum1 > sum2 ? sum1 : sum2;
        int cur = (maxPrev + nums1[i]) % MOD;
        sum1 = sum2 = cur;
        i++;
        j++;
      }
    }

    while (i < n) {
      sum1 += nums1[i];
      i++;
    }
    while (j < m) {
      sum2 += nums2[j];
      j++;
    }

    return ((sum1 > sum2 ? sum1 : sum2) % MOD);
  }
}
```

## Golang

```go
func maxSum(nums1 []int, nums2 []int) int {
	const MOD int64 = 1000000007
	i, j := 0, 0
	var sum1, sum2 int64

	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			sum1 += int64(nums1[i])
			i++
		} else if nums1[i] > nums2[j] {
			sum2 += int64(nums2[j])
			j++
		} else { // equal element, can switch paths
			val := int64(nums1[i])
			if sum2 > sum1 {
				sum1 = sum2
			}
			sum1 += val
			sum2 = sum1
			i++
			j++
		}
	}

	for i < len(nums1) {
		sum1 += int64(nums1[i])
		i++
	}
	for j < len(nums2) {
		sum2 += int64(nums2[j])
		j++
	}

	if sum2 > sum1 {
		sum1 = sum2
	}
	return int(sum1 % MOD)
}
```

## Ruby

```ruby
def max_sum(nums1, nums2)
  i = j = 0
  sum1 = sum2 = 0
  n = nums1.length
  m = nums2.length
  while i < n && j < m
    if nums1[i] < nums2[j]
      sum1 += nums1[i]
      i += 1
    elsif nums1[i] > nums2[j]
      sum2 += nums2[j]
      j += 1
    else
      cur = [sum1, sum2].max + nums1[i]
      sum1 = sum2 = cur
      i += 1
      j += 1
    end
  end
  while i < n
    sum1 += nums1[i]
    i += 1
  end
  while j < m
    sum2 += nums2[j]
    j += 1
  end
  [sum1, sum2].max % 1_000_000_007
end
```

## Scala

```scala
object Solution {
    def maxSum(nums1: Array[Int], nums2: Array[Int]): Int = {
        val MOD = 1000000007L
        var i = 0
        var j = 0
        var sum1 = 0L
        var sum2 = 0L
        var result = 0L

        while (i < nums1.length && j < nums2.length) {
            if (nums1(i) < nums2(j)) {
                sum1 += nums1(i)
                i += 1
            } else if (nums1(i) > nums2(j)) {
                sum2 += nums2(j)
                j += 1
            } else {
                val common = nums1(i).toLong
                result = (result + math.max(sum1, sum2) + common) % MOD
                sum1 = 0L
                sum2 = 0L
                i += 1
                j += 1
            }
        }

        while (i < nums1.length) {
            sum1 += nums1(i)
            i += 1
        }
        while (j < nums2.length) {
            sum2 += nums2(j)
            j += 1
        }

        result = (result + math.max(sum1, sum2)) % MOD
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let (mut i, mut j) = (0usize, 0usize);
        let (n, m) = (nums1.len(), nums2.len());
        let mut sum1: i64 = 0;
        let mut sum2: i64 = 0;
        let mut result: i64 = 0;

        while i < n && j < m {
            if nums1[i] < nums2[j] {
                sum1 += nums1[i] as i64;
                i += 1;
            } else if nums1[i] > nums2[j] {
                sum2 += nums2[j] as i64;
                j += 1;
            } else {
                let val = nums1[i] as i64;
                result = (result + std::cmp::max(sum1, sum2) + val) % MOD;
                sum1 = 0;
                sum2 = 0;
                i += 1;
                j += 1;
            }
        }

        while i < n {
            sum1 += nums1[i] as i64;
            i += 1;
        }
        while j < m {
            sum2 += nums2[j] as i64;
            j += 1;
        }

        result = (result + std::cmp::max(sum1, sum2)) % MOD;
        result as i32
    }
}
```

## Racket

```racket
(define/contract (max-sum nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (n (vector-length v1))
         (m (vector-length v2))
         (MOD 1000000007))
    (let loop ((i 0) (j 0) (sum1 0) (sum2 0) (ans 0))
      (cond
        [(and (< i n) (< j m))
         (let ((a (vector-ref v1 i))
               (b (vector-ref v2 j)))
           (cond
             [(< a b)
              (loop (+ i 1) j (+ sum1 a) sum2 ans)]
             [(> a b)
              (loop i (+ j 1) sum1 (+ sum2 b) ans)]
             [else ; a == b, common element
              (let ((new-ans (modulo (+ ans (max sum1 sum2) a) MOD)))
                (loop (+ i 1) (+ j 1) 0 0 new-ans))]))]
        [(< i n)
         ;; nums1 has remaining elements
         (let ((rem-sum (let sum-loop ((k i) (s sum1))
                          (if (< k n)
                              (sum-loop (+ k 1) (+ s (vector-ref v1 k)))
                              s))))
           (modulo (+ ans (max rem-sum sum2)) MOD))]
        [(< j m)
         ;; nums2 has remaining elements
         (let ((rem-sum (let sum-loop ((k j) (s sum2))
                          (if (< k m)
                              (sum-loop (+ k 1) (+ s (vector-ref v2 k)))
                              s))))
           (modulo (+ ans (max sum1 rem-sum)) MOD))]
        [else
         ;; both exhausted
         (modulo (+ ans (max sum1 sum2)) MOD)]))))
```

## Erlang

```erlang
-module(solution).
-export([max_sum/2]).

-spec max_sum([integer()], [integer()]) -> integer().
max_sum(Nums1, Nums2) ->
    MOD = 1000000007,
    Total = process(Nums1, Nums2, 0, 0, 0),
    Total rem MOD.

process([], [], Sum1, Sum2, Total) ->
    Total + max(Sum1, Sum2);
process([H|T], [], Sum1, Sum2, Total) ->
    process(T, [], Sum1 + H, Sum2, Total);
process([], [H|T], Sum1, Sum2, Total) ->
    process([], T, Sum1, Sum2 + H, Total);
process([H1|T1]=L1, [H2|T2]=L2, Sum1, Sum2, Total) when H1 == H2 ->
    NewTotal = Total + max(Sum1, Sum2) + H1,
    process(T1, T2, 0, 0, NewTotal);
process([H1|T1]=L1, [H2|_]=L2, Sum1, Sum2, Total) when H1 < H2 ->
    process(T1, L2, Sum1 + H1, Sum2, Total);
process(L1, [H2|T2], Sum1, Sum2, Total) ->
    process(L1, T2, Sum1, Sum2 + H2, Total).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec max_sum(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_sum(nums1, nums2) do
    helper(nums1, nums2, 0, 0, 0)
  end

  defp helper([], [], sum1, sum2, acc) do
    (acc + max(sum1, sum2)) |> rem(@mod)
  end

  defp helper([], [h | t], sum1, sum2, acc) do
    helper([], t, sum1, sum2 + h, acc)
  end

  defp helper([h | t], [], sum1, sum2, acc) do
    helper(t, [], sum1 + h, sum2, acc)
  end

  defp helper([h1 | t1] = l1, [h2 | t2] = l2, sum1, sum2, acc) do
    cond do
      h1 == h2 ->
        new_acc = (acc + max(sum1, sum2) + h1) |> rem(@mod)
        helper(t1, t2, 0, 0, new_acc)

      h1 < h2 ->
        helper(t1, l2, sum1 + h1, sum2, acc)

      true ->
        helper(l1, t2, sum1, sum2 + h2, acc)
    end
  end
end
```
