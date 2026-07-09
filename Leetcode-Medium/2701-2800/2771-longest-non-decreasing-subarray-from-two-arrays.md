# 2771. Longest Non-decreasing Subarray From Two Arrays

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxNonDecreasingLength(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        if (n == 0) return 0;
        int prev0 = 1, prev1 = 1; // dp for i-1
        int ans = 1;
        for (int i = 1; i < n; ++i) {
            int cur0 = 1, cur1 = 1;
            if (nums1[i] >= nums1[i - 1]) cur0 = max(cur0, prev0 + 1);
            if (nums1[i] >= nums2[i - 1]) cur0 = max(cur0, prev1 + 1);
            if (nums2[i] >= nums1[i - 1]) cur1 = max(cur1, prev0 + 1);
            if (nums2[i] >= nums2[i - 1]) cur1 = max(cur1, prev1 + 1);
            ans = max({ans, cur0, cur1});
            prev0 = cur0;
            prev1 = cur1;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxNonDecreasingLength(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int prev0 = 0, prev1 = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cur0, cur1;
            if (i == 0) {
                cur0 = cur1 = 1;
            } else {
                cur0 = 1;
                if (nums1[i] >= nums1[i - 1]) {
                    cur0 = Math.max(cur0, prev0 + 1);
                }
                if (nums1[i] >= nums2[i - 1]) {
                    cur0 = Math.max(cur0, prev1 + 1);
                }

                cur1 = 1;
                if (nums2[i] >= nums1[i - 1]) {
                    cur1 = Math.max(cur1, prev0 + 1);
                }
                if (nums2[i] >= nums2[i - 1]) {
                    cur1 = Math.max(cur1, prev1 + 1);
                }
            }
            ans = Math.max(ans, Math.max(cur0, cur1));
            prev0 = cur0;
            prev1 = cur1;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxNonDecreasingLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        if n == 0:
            return 0
        dp0 = dp1 = 1  # lengths ending at previous index with choice from nums1 / nums2
        ans = 1
        for i in range(1, n):
            cur0 = 1
            cur1 = 1
            v0 = nums1[i]
            v1 = nums2[i]
            if v0 >= nums1[i - 1]:
                cur0 = max(cur0, dp0 + 1)
            if v0 >= nums2[i - 1]:
                cur0 = max(cur0, dp1 + 1)
            if v1 >= nums1[i - 1]:
                cur1 = max(cur1, dp0 + 1)
            if v1 >= nums2[i - 1]:
                cur1 = max(cur1, dp1 + 1)
            dp0, dp1 = cur0, cur1
            ans = max(ans, dp0, dp1)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n == 0:
            return 0
        prev0 = prev1 = 1
        ans = 1
        for i in range(1, n):
            cur0 = cur1 = 1
            if nums1[i] >= nums1[i - 1]:
                cur0 = max(cur0, prev0 + 1)
            if nums1[i] >= nums2[i - 1]:
                cur0 = max(cur0, prev1 + 1)
            if nums2[i] >= nums1[i - 1]:
                cur1 = max(cur1, prev0 + 1)
            if nums2[i] >= nums2[i - 1]:
                cur1 = max(cur1, prev1 + 1)
            ans = max(ans, cur0, cur1)
            prev0, prev1 = cur0, cur1
        return ans
```

## C

```c
int maxNonDecreasingLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size;
    if (n == 0) return 0;
    int dp0 = 1, dp1 = 1; // lengths ending at current index using nums1[i] or nums2[i]
    int ans = 1;
    for (int i = 1; i < n; ++i) {
        int ndp0 = 1, ndp1 = 1;
        if (nums1[i] >= nums1[i - 1]) {
            int cand = dp0 + 1;
            if (cand > ndp0) ndp0 = cand;
        }
        if (nums1[i] >= nums2[i - 1]) {
            int cand = dp1 + 1;
            if (cand > ndp0) ndp0 = cand;
        }
        if (nums2[i] >= nums1[i - 1]) {
            int cand = dp0 + 1;
            if (cand > ndp1) ndp1 = cand;
        }
        if (nums2[i] >= nums2[i - 1]) {
            int cand = dp1 + 1;
            if (cand > ndp1) ndp1 = cand;
        }
        dp0 = ndp0;
        dp1 = ndp1;
        if (dp0 > ans) ans = dp0;
        if (dp1 > ans) ans = dp1;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxNonDecreasingLength(int[] nums1, int[] nums2)
    {
        int n = nums1.Length;
        if (n == 0) return 0;

        int prev0 = 1; // ending with nums1[i-1]
        int prev1 = 1; // ending with nums2[i-1]
        int answer = 1;

        for (int i = 1; i < n; i++)
        {
            int cur0 = 1;
            if (nums1[i] >= nums1[i - 1]) cur0 = Math.Max(cur0, prev0 + 1);
            if (nums1[i] >= nums2[i - 1]) cur0 = Math.Max(cur0, prev1 + 1);

            int cur1 = 1;
            if (nums2[i] >= nums1[i - 1]) cur1 = Math.Max(cur1, prev0 + 1);
            if (nums2[i] >= nums2[i - 1]) cur1 = Math.Max(cur1, prev1 + 1);

            answer = Math.Max(answer, Math.Max(cur0, cur1));

            prev0 = cur0;
            prev1 = cur1;
        }

        return answer;
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
var maxNonDecreasingLength = function(nums1, nums2) {
    const n = nums1.length;
    let prev0 = 1; // length ending at i-1 choosing nums1[i-1]
    let prev1 = 1; // length ending at i-1 choosing nums2[i-1]
    let ans = 1;

    for (let i = 1; i < n; ++i) {
        let cur0 = 1;
        if (nums1[i] >= nums1[i - 1]) cur0 = Math.max(cur0, prev0 + 1);
        if (nums1[i] >= nums2[i - 1]) cur0 = Math.max(cur0, prev1 + 1);

        let cur1 = 1;
        if (nums2[i] >= nums1[i - 1]) cur1 = Math.max(cur1, prev0 + 1);
        if (nums2[i] >= nums2[i - 1]) cur1 = Math.max(cur1, prev1 + 1);

        ans = Math.max(ans, cur0, cur1);
        prev0 = cur0;
        prev1 = cur1;
    }

    return ans;
};
```

## Typescript

```typescript
function maxNonDecreasingLength(nums1: number[], nums2: number[]): number {
    const n = nums1.length;
    if (n === 0) return 0;
    let prev0 = 1; // ending with nums1[i-1]
    let prev1 = 1; // ending with nums2[i-1]
    let ans = 1;

    for (let i = 1; i < n; i++) {
        let cur0 = 1;
        if (nums1[i] >= nums1[i - 1]) cur0 = Math.max(cur0, prev0 + 1);
        if (nums1[i] >= nums2[i - 1]) cur0 = Math.max(cur0, prev1 + 1);

        let cur1 = 1;
        if (nums2[i] >= nums1[i - 1]) cur1 = Math.max(cur1, prev0 + 1);
        if (nums2[i] >= nums2[i - 1]) cur1 = Math.max(cur1, prev1 + 1);

        ans = Math.max(ans, cur0, cur1);
        prev0 = cur0;
        prev1 = cur1;
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
    function maxNonDecreasingLength($nums1, $nums2) {
        $n = count($nums1);
        if ($n == 0) return 0;

        // dp values for the previous index
        $prev0 = 1; // ending with nums1[i-1]
        $prev1 = 1; // ending with nums2[i-1]

        $ans = 1;

        for ($i = 1; $i < $n; ++$i) {
            $cur0 = 1;
            if ($nums1[$i] >= $nums1[$i - 1]) {
                $cur0 = max($cur0, $prev0 + 1);
            }
            if ($nums1[$i] >= $nums2[$i - 1]) {
                $cur0 = max($cur0, $prev1 + 1);
            }

            $cur1 = 1;
            if ($nums2[$i] >= $nums1[$i - 1]) {
                $cur1 = max($cur1, $prev0 + 1);
            }
            if ($nums2[$i] >= $nums2[$i - 1]) {
                $cur1 = max($cur1, $prev1 + 1);
            }

            $ans = max($ans, $cur0, $cur1);

            $prev0 = $cur0;
            $prev1 = $cur1;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxNonDecreasingLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        if n == 0 { return 0 }
        var prev0 = 1   // dp ending with nums1[i-1]
        var prev1 = 1   // dp ending with nums2[i-1]
        var answer = 1
        
        for i in 1..<n {
            var cur0 = 1
            var cur1 = 1
            let a = nums1[i]
            let b = nums2[i]
            
            if a >= nums1[i - 1] {
                cur0 = max(cur0, prev0 + 1)
            }
            if a >= nums2[i - 1] {
                cur0 = max(cur0, prev1 + 1)
            }
            
            if b >= nums1[i - 1] {
                cur1 = max(cur1, prev0 + 1)
            }
            if b >= nums2[i - 1] {
                cur1 = max(cur1, prev1 + 1)
            }
            
            answer = max(answer, cur0)
            answer = max(answer, cur1)
            
            prev0 = cur0
            prev1 = cur1
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNonDecreasingLength(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        var dp0 = 1 // ending with nums1[i]
        var dp1 = 1 // ending with nums2[i]
        var answer = 1
        for (i in 1 until n) {
            var cur0 = 1
            var cur1 = 1
            if (nums1[i] >= nums1[i - 1]) cur0 = maxOf(cur0, dp0 + 1)
            if (nums1[i] >= nums2[i - 1]) cur0 = maxOf(cur0, dp1 + 1)

            if (nums2[i] >= nums1[i - 1]) cur1 = maxOf(cur1, dp0 + 1)
            if (nums2[i] >= nums2[i - 1]) cur1 = maxOf(cur1, dp1 + 1)

            dp0 = cur0
            dp1 = cur1
            answer = maxOf(answer, dp0, dp1)
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxNonDecreasingLength(List<int> nums1, List<int> nums2) {
    int n = nums1.length;
    if (n == 0) return 0;

    int prev0 = 1; // length ending at i-1 with nums1[i-1]
    int prev1 = 1; // length ending at i-1 with nums2[i-1]
    int ans = 1;

    for (int i = 1; i < n; ++i) {
      int cur0 = 1;
      if (nums1[i] >= nums1[i - 1]) {
        cur0 = max(cur0, prev0 + 1);
      }
      if (nums1[i] >= nums2[i - 1]) {
        cur0 = max(cur0, prev1 + 1);
      }

      int cur1 = 1;
      if (nums2[i] >= nums1[i - 1]) {
        cur1 = max(cur1, prev0 + 1);
      }
      if (nums2[i] >= nums2[i - 1]) {
        cur1 = max(cur1, prev1 + 1);
      }

      ans = max(ans, max(cur0, cur1));
      prev0 = cur0;
      prev1 = cur1;
    }

    return ans;
  }
}
```

## Golang

```go
func maxNonDecreasingLength(nums1 []int, nums2 []int) int {
	n := len(nums1)
	if n == 0 {
		return 0
	}
	prev0, prev1 := 1, 1
	ans := 1
	for i := 1; i < n; i++ {
		cur0 := 1
		if nums1[i] >= nums1[i-1] && prev0+1 > cur0 {
			cur0 = prev0 + 1
		}
		if nums1[i] >= nums2[i-1] && prev1+1 > cur0 {
			cur0 = prev1 + 1
		}
		cur1 := 1
		if nums2[i] >= nums1[i-1] && prev0+1 > cur1 {
			cur1 = prev0 + 1
		}
		if nums2[i] >= nums2[i-1] && prev1+1 > cur1 {
			cur1 = prev1 + 1
		}
		if cur0 > ans {
			ans = cur0
		}
		if cur1 > ans {
			ans = cur1
		}
		prev0, prev1 = cur0, cur1
	}
	return ans
}
```

## Ruby

```ruby
def max_non_decreasing_length(nums1, nums2)
  n = nums1.length
  return 0 if n == 0

  prev0 = 1
  prev1 = 1
  ans = 1

  (1...n).each do |i|
    cur0 = 1
    cur1 = 1

    if nums1[i] >= nums1[i - 1]
      cur0 = [cur0, prev0 + 1].max
    end
    if nums1[i] >= nums2[i - 1]
      cur0 = [cur0, prev1 + 1].max
    end

    if nums2[i] >= nums1[i - 1]
      cur1 = [cur1, prev0 + 1].max
    end
    if nums2[i] >= nums2[i - 1]
      cur1 = [cur1, prev1 + 1].max
    end

    ans = [ans, cur0, cur1].max
    prev0 = cur0
    prev1 = cur1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxNonDecreasingLength(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        var prev0 = 1
        var prev1 = 1
        var ans = 1
        for (i <- 1 until n) {
            var cur0 = 1
            if (nums1(i) >= nums1(i - 1)) cur0 = math.max(cur0, prev0 + 1)
            if (nums1(i) >= nums2(i - 1)) cur0 = math.max(cur0, prev1 + 1)

            var cur1 = 1
            if (nums2(i) >= nums1(i - 1)) cur1 = math.max(cur1, prev0 + 1)
            if (nums2(i) >= nums2(i - 1)) cur1 = math.max(cur1, prev1 + 1)

            ans = math.max(ans, math.max(cur0, cur1))
            prev0 = cur0
            prev1 = cur1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_non_decreasing_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        if n == 0 {
            return 0;
        }
        // dp values for the previous index
        let mut prev0: i32 = 1; // ending with nums1[i-1]
        let mut prev1: i32 = 1; // ending with nums2[i-1]
        let mut ans: i32 = 1;

        for i in 1..n {
            let mut cur0: i32 = 1;
            if nums1[i] >= nums1[i - 1] {
                cur0 = cur0.max(prev0 + 1);
            }
            if nums1[i] >= nums2[i - 1] {
                cur0 = cur0.max(prev1 + 1);
            }

            let mut cur1: i32 = 1;
            if nums2[i] >= nums1[i - 1] {
                cur1 = cur1.max(prev0 + 1);
            }
            if nums2[i] >= nums2[i - 1] {
                cur1 = cur1.max(prev1 + 1);
            }

            ans = ans.max(cur0).max(cur1);
            prev0 = cur0;
            prev1 = cur1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-non-decreasing-length nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums1))
         (v1 (list->vector nums1))
         (v2 (list->vector nums2)))
    (if (= n 0)
        0
        (let loop ((i 0) (prev0 0) (prev1 0) (best 0))
          (if (= i n)
              best
              (let* ((a (vector-ref v1 i))
                     (b (vector-ref v2 i)))
                (if (= i 0)
                    (let ((dp0 1) (dp1 1) (new-best 1))
                      (loop (add1 i) dp0 dp1 new-best))
                    (let* ((prev-a (vector-ref v1 (sub1 i)))
                           (prev-b (vector-ref v2 (sub1 i))))
                      (define dp0
                        (max 1
                             (if (>= a prev-a) (+ prev0 1) 0)
                             (if (>= a prev-b) (+ prev1 1) 0)))
                      (define dp1
                        (max 1
                             (if (>= b prev-a) (+ prev0 1) 0)
                             (if (>= b prev-b) (+ prev1 1) 0)))
                      (let ((new-best (max best dp0 dp1)))
                        (loop (add1 i) dp0 dp1 new-best))))))))))
```

## Erlang

```erlang
-spec max_non_decreasing_length([integer()], [integer()]) -> integer().
max_non_decreasing_length(Nums1, Nums2) ->
    case {Nums1, Nums2} of
        {[H1|T1], [H2|T2]} ->
            loop(T1, T2, H1, H2, 1, 1, 1);
        _ -> 0
    end.

loop([], [], _, _, DP0Prev, DP1Prev, Ans) ->
    erlang:max(Ans, erlang:max(DP0Prev, DP1Prev));
loop([X1|Rest1], [X2|Rest2], Prev1, Prev2, DP0Prev, DP1Prev, Ans) ->
    FromPrev1_0 = case X1 >= Prev1 of true -> DP0Prev + 1; false -> 0 end,
    FromPrev2_0 = case X1 >= Prev2 of true -> DP1Prev + 1; false -> 0 end,
    NewDP0 = erlang:max(1, erlang:max(FromPrev1_0, FromPrev2_0)),
    FromPrev1_1 = case X2 >= Prev1 of true -> DP0Prev + 1; false -> 0 end,
    FromPrev2_1 = case X2 >= Prev2 of true -> DP1Prev + 1; false -> 0 end,
    NewDP1 = erlang:max(1, erlang:max(FromPrev1_1, FromPrev2_1)),
    NewAns = erlang:max(Ans, erlang:max(NewDP0, NewDP1)),
    loop(Rest1, Rest2, X1, X2, NewDP0, NewDP1, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_non_decreasing_length(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_non_decreasing_length(nums1, nums2) do
    Enum.zip(nums1, nums2)
    |> Enum.reduce({nil, nil, 0, 0, 0}, fn {a, b},
          {prev_a, prev_b, prev_len1, prev_len2, ans} ->
      if prev_a == nil do
        len1 = 1
        len2 = 1
        new_ans = max(ans, 1)
        {a, b, len1, len2, new_ans}
      else
        cand1 = [1]
        cand1 = if a >= prev_a, do: [prev_len1 + 1 | cand1], else: cand1
        cand1 = if a >= prev_b, do: [prev_len2 + 1 | cand1], else: cand1
        len1 = Enum.max(cand1)

        cand2 = [1]
        cand2 = if b >= prev_a, do: [prev_len1 + 1 | cand2], else: cand2
        cand2 = if b >= prev_b, do: [prev_len2 + 1 | cand2], else: cand2
        len2 = Enum.max(cand2)

        new_ans = ans |> max(len1) |> max(len2)
        {a, b, len1, len2, new_ans}
      end
    end)
    |> elem(4)
  end
end
```
