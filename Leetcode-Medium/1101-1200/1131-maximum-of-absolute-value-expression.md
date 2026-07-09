# 1131. Maximum of Absolute Value Expression

## Cpp

```cpp
class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        long long answer = 0;
        // Case 1: +arr1 +arr2 +i
        long long mx = LLONG_MIN, mn = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            long long val = (long long)arr1[i] + arr2[i] + i;
            mx = max(mx, val);
            mn = min(mn, val);
        }
        answer = max(answer, mx - mn);
        // Case 2: +arr1 +arr2 -i
        mx = LLONG_MIN; mn = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            long long val = (long long)arr1[i] + arr2[i] - i;
            mx = max(mx, val);
            mn = min(mn, val);
        }
        answer = max(answer, mx - mn);
        // Case 3: +arr1 -arr2 +i
        mx = LLONG_MIN; mn = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            long long val = (long long)arr1[i] - arr2[i] + i;
            mx = max(mx, val);
            mn = min(mn, val);
        }
        answer = max(answer, mx - mn);
        // Case 4: +arr1 -arr2 -i
        mx = LLONG_MIN; mn = LLONG_MAX;
        for (int i = 0; i < n; ++i) {
            long long val = (long long)arr1[i] - arr2[i] - i;
            mx = max(mx, val);
            mn = min(mn, val);
        }
        answer = max(answer, mx - mn);
        return (int)answer;
    }
};
```

## Java

```java
class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        int n = arr1.length;
        long max1 = Long.MIN_VALUE, min1 = Long.MAX_VALUE;
        long max2 = Long.MIN_VALUE, min2 = Long.MAX_VALUE;
        long max3 = Long.MIN_VALUE, min3 = Long.MAX_VALUE;
        long max4 = Long.MIN_VALUE, min4 = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            long a = arr1[i];
            long b = arr2[i];

            long v1 = a + b + i;
            long v2 = a + b - i;
            long v3 = a - b + i;
            long v4 = a - b - i;

            if (v1 > max1) max1 = v1;
            if (v1 < min1) min1 = v1;
            if (v2 > max2) max2 = v2;
            if (v2 < min2) min2 = v2;
            if (v3 > max3) max3 = v3;
            if (v3 < min3) min3 = v3;
            if (v4 > max4) max4 = v4;
            if (v4 < min4) min4 = v4;
        }

        long ans = Math.max(Math.max(max1 - min1, max2 - min2), Math.max(max3 - min3, max4 - min4));
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        min_f = max_f = None
        min_g = max_g = None
        min_h = max_h = None
        min_k = max_k = None

        for i, (a, b) in enumerate(zip(arr1, arr2)):
            f = a + b + i
            g = a + b - i
            h = a - b + i
            k = a - b - i

            if min_f is None:
                min_f = max_f = f
                min_g = max_g = g
                min_h = max_h = h
                min_k = max_k = k
            else:
                if f < min_f: min_f = f
                if f > max_f: max_f = f

                if g < min_g: min_g = g
                if g > max_g: max_g = g

                if h < min_h: min_h = h
                if h > max_h: max_h = h

                if k < min_k: min_k = k
                if k > max_k: max_k = k

        return max(max_f - min_f, max_g - min_g, max_h - min_h, max_k - min_k)
```

## Python3

```python
from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        # Initialize min and max for each of the four forms
        min_vals = [float('inf')] * 4
        max_vals = [float('-inf')] * 4

        for i in range(n):
            a, b = arr1[i], arr2[i]
            vals = [
                a + b + i,
                a + b - i,
                a - b + i,
                a - b - i
            ]
            for k in range(4):
                v = vals[k]
                if v < min_vals[k]:
                    min_vals[k] = v
                if v > max_vals[k]:
                    max_vals[k] = v

        ans = 0
        for k in range(4):
            diff = max_vals[k] - min_vals[k]
            if diff > ans:
                ans = diff
        return ans
```

## C

```c
int maxAbsValExpr(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    long long min1 = LLONG_MAX, max1 = LLONG_MIN;
    long long min2 = LLONG_MAX, max2 = LLONG_MIN;
    long long min3 = LLONG_MAX, max3 = LLONG_MIN;
    long long min4 = LLONG_MAX, max4 = LLONG_MIN;

    for (int i = 0; i < arr1Size; ++i) {
        long long a = arr1[i];
        long long b = arr2[i];
        long long v1 = a + b + i;
        long long v2 = a + b - i;
        long long v3 = a - b + i;
        long long v4 = a - b - i;

        if (v1 < min1) min1 = v1;
        if (v1 > max1) max1 = v1;
        if (v2 < min2) min2 = v2;
        if (v2 > max2) max2 = v2;
        if (v3 < min3) min3 = v3;
        if (v3 > max3) max3 = v3;
        if (v4 < min4) min4 = v4;
        if (v4 > max4) max4 = v4;
    }

    long long ans1 = max1 - min1;
    long long ans2 = max2 - min2;
    long long ans3 = max3 - min3;
    long long ans4 = max4 - min4;

    long long result = ans1;
    if (ans2 > result) result = ans2;
    if (ans3 > result) result = ans3;
    if (ans4 > result) result = ans4;

    return (int)result;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxAbsValExpr(int[] arr1, int[] arr2) {
        int n = arr1.Length;
        int max1 = int.MinValue, min1 = int.MaxValue;
        int max2 = int.MinValue, min2 = int.MaxValue;
        int max3 = int.MinValue, min3 = int.MaxValue;
        int max4 = int.MinValue, min4 = int.MaxValue;

        for (int i = 0; i < n; i++) {
            int a = arr1[i];
            int b = arr2[i];

            int v1 = a + b + i;
            int v2 = a + b - i;
            int v3 = a - b + i;
            int v4 = a - b - i;

            if (v1 > max1) max1 = v1;
            if (v1 < min1) min1 = v1;
            if (v2 > max2) max2 = v2;
            if (v2 < min2) min2 = v2;
            if (v3 > max3) max3 = v3;
            if (v3 < min3) min3 = v3;
            if (v4 > max4) max4 = v4;
            if (v4 < min4) min4 = v4;
        }

        int ans1 = max1 - min1;
        int ans2 = max2 - min2;
        int ans3 = max3 - min3;
        int ans4 = max4 - min4;

        return Math.Max(Math.Max(ans1, ans2), Math.Max(ans3, ans4));
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var maxAbsValExpr = function(arr1, arr2) {
    let max1 = -Infinity, min1 = Infinity;
    let max2 = -Infinity, min2 = Infinity;
    let max3 = -Infinity, min3 = Infinity;
    let max4 = -Infinity, min4 = Infinity;

    for (let i = 0; i < arr1.length; ++i) {
        const a = arr1[i];
        const b = arr2[i];

        const v1 =  a + b + i;
        const v2 =  a - b + i;
        const v3 = -a + b + i;
        const v4 = -a - b + i;

        if (v1 > max1) max1 = v1;
        if (v1 < min1) min1 = v1;

        if (v2 > max2) max2 = v2;
        if (v2 < min2) min2 = v2;

        if (v3 > max3) max3 = v3;
        if (v3 < min3) min3 = v3;

        if (v4 > max4) max4 = v4;
        if (v4 < min4) min4 = v4;
    }

    return Math.max(
        max1 - min1,
        max2 - min2,
        max3 - min3,
        max4 - min4
    );
};
```

## Typescript

```typescript
function maxAbsValExpr(arr1: number[], arr2: number[]): number {
    const n = arr1.length;
    let answer = 0;
    const combos: [number, number][] = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]
    ];
    for (const [s1, s2] of combos) {
        let maxVal = -Infinity;
        let minVal = Infinity;
        for (let i = 0; i < n; i++) {
            const cur = s1 * arr1[i] + s2 * arr2[i] + i;
            if (cur > maxVal) maxVal = cur;
            if (cur < minVal) minVal = cur;
        }
        answer = Math.max(answer, maxVal - minVal);
    }
    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function maxAbsValExpr($arr1, $arr2) {
        $n = count($arr1);
        $max1 = PHP_INT_MIN; $min1 = PHP_INT_MAX;
        $max2 = PHP_INT_MIN; $min2 = PHP_INT_MAX;
        $max3 = PHP_INT_MIN; $min3 = PHP_INT_MAX;
        $max4 = PHP_INT_MIN; $min4 = PHP_INT_MAX;

        for ($i = 0; $i < $n; $i++) {
            $a = $arr1[$i];
            $b = $arr2[$i];

            $v1 = $a + $b + $i;
            $v2 = $a + $b - $i;
            $v3 = $a - $b + $i;
            $v4 = $a - $b - $i;

            if ($v1 > $max1) $max1 = $v1;
            if ($v1 < $min1) $min1 = $v1;

            if ($v2 > $max2) $max2 = $v2;
            if ($v2 < $min2) $min2 = $v2;

            if ($v3 > $max3) $max3 = $v3;
            if ($v3 < $min3) $min3 = $v3;

            if ($v4 > $max4) $max4 = $v4;
            if ($v4 < $min4) $min4 = $v4;
        }

        $ans1 = $max1 - $min1;
        $ans2 = $max2 - $min2;
        $ans3 = $max3 - $min3;
        $ans4 = $max4 - $min4;

        return max($ans1, $ans2, $ans3, $ans4);
    }
}
```

## Swift

```swift
class Solution {
    func maxAbsValExpr(_ arr1: [Int], _ arr2: [Int]) -> Int {
        let n = arr1.count
        var max0 = Int.min, min0 = Int.max
        var max1 = Int.min, min1 = Int.max
        var max2 = Int.min, min2 = Int.max
        var max3 = Int.min, min3 = Int.max
        
        for i in 0..<n {
            let a = arr1[i]
            let b = arr2[i]
            
            let v0 = a + b + i
            if v0 > max0 { max0 = v0 }
            if v0 < min0 { min0 = v0 }
            
            let v1 = a + b - i
            if v1 > max1 { max1 = v1 }
            if v1 < min1 { min1 = v1 }
            
            let v2 = a - b + i
            if v2 > max2 { max2 = v2 }
            if v2 < min2 { min2 = v2 }
            
            let v3 = a - b - i
            if v3 > max3 { max3 = v3 }
            if v3 < min3 { min3 = v3 }
        }
        
        var ans = 0
        ans = max(ans, max0 - min0)
        ans = max(ans, max1 - min1)
        ans = max(ans, max2 - min2)
        ans = max(ans, max3 - min3)
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAbsValExpr(arr1: IntArray, arr2: IntArray): Int {
        var max1 = Int.MIN_VALUE
        var min1 = Int.MAX_VALUE
        var max2 = Int.MIN_VALUE
        var min2 = Int.MAX_VALUE
        var max3 = Int.MIN_VALUE
        var min3 = Int.MAX_VALUE
        var max4 = Int.MIN_VALUE
        var min4 = Int.MAX_VALUE

        for (i in arr1.indices) {
            val a = arr1[i]
            val b = arr2[i]

            val v1 = a + b + i
            if (v1 > max1) max1 = v1
            if (v1 < min1) min1 = v1

            val v2 = a + b - i
            if (v2 > max2) max2 = v2
            if (v2 < min2) min2 = v2

            val v3 = a - b + i
            if (v3 > max3) max3 = v3
            if (v3 < min3) min3 = v3

            val v4 = a - b - i
            if (v4 > max4) max4 = v4
            if (v4 < min4) min4 = v4
        }

        var ans = max1 - min1
        val diff2 = max2 - min2
        if (diff2 > ans) ans = diff2
        val diff3 = max3 - min3
        if (diff3 > ans) ans = diff3
        val diff4 = max4 - min4
        if (diff4 > ans) ans = diff4

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxAbsValExpr(List<int> arr1, List<int> arr2) {
    int n = arr1.length;
    int v1 = arr1[0] + arr2[0];
    int v2 = v1;
    int v3 = arr1[0] - arr2[0];
    int v4 = v3;

    int max1 = v1, min1 = v1;
    int max2 = v2, min2 = v2;
    int max3 = v3, min3 = v3;
    int max4 = v4, min4 = v4;

    for (int i = 0; i < n; ++i) {
      int a = arr1[i];
      int b = arr2[i];

      int val1 = a + b + i;
      int val2 = a + b - i;
      int val3 = a - b + i;
      int val4 = a - b - i;

      if (val1 > max1) max1 = val1;
      if (val1 < min1) min1 = val1;

      if (val2 > max2) max2 = val2;
      if (val2 < min2) min2 = val2;

      if (val3 > max3) max3 = val3;
      if (val3 < min3) min3 = val3;

      if (val4 > max4) max4 = val4;
      if (val4 < min4) min4 = val4;
    }

    int ans1 = max1 - min1;
    int ans2 = max2 - min2;
    int ans3 = max3 - min3;
    int ans4 = max4 - min4;

    int result = ans1;
    if (ans2 > result) result = ans2;
    if (ans3 > result) result = ans3;
    if (ans4 > result) result = ans4;
    return result;
  }
}
```

## Golang

```go
func maxAbsValExpr(arr1 []int, arr2 []int) int {
	n := len(arr1)
	max1, min1 := arr1[0]+arr2[0], arr1[0]+arr2[0]
	max2, min2 := arr1[0]+arr2[0], arr1[0]+arr2[0]
	max3, min3 := arr1[0]-arr2[0], arr1[0]-arr2[0]
	max4, min4 := arr1[0]-arr2[0], arr1[0]-arr2[0]

	for i := 0; i < n; i++ {
		v1 := arr1[i] + arr2[i] + i
		if v1 > max1 {
			max1 = v1
		}
		if v1 < min1 {
			min1 = v1
		}

		v2 := arr1[i] + arr2[i] - i
		if v2 > max2 {
			max2 = v2
		}
		if v2 < min2 {
			min2 = v2
		}

		v3 := arr1[i] - arr2[i] + i
		if v3 > max3 {
			max3 = v3
		}
		if v3 < min3 {
			min3 = v3
		}

		v4 := arr1[i] - arr2[i] - i
		if v4 > max4 {
			max4 = v4
		}
		if v4 < min4 {
			min4 = v4
		}
	}

	ans := max1 - min1
	if d := max2 - min2; d > ans {
		ans = d
	}
	if d := max3 - min3; d > ans {
		ans = d
	}
	if d := max4 - min4; d > ans {
		ans = d
	}
	return ans
}
```

## Ruby

```ruby
def max_abs_val_expr(arr1, arr2)
  n = arr1.length
  max1 = -Float::INFINITY
  min1 = Float::INFINITY
  max2 = -Float::INFINITY
  min2 = Float::INFINITY
  max3 = -Float::INFINITY
  min3 = Float::INFINITY
  max4 = -Float::INFINITY
  min4 = Float::INFINITY

  (0...n).each do |i|
    a = arr1[i]
    b = arr2[i]
    v1 = a + b + i
    v2 = a + b - i
    v3 = a - b + i
    v4 = a - b - i

    max1 = v1 if v1 > max1
    min1 = v1 if v1 < min1
    max2 = v2 if v2 > max2
    min2 = v2 if v2 < min2
    max3 = v3 if v3 > max3
    min3 = v3 if v3 < min3
    max4 = v4 if v4 > max4
    min4 = v4 if v4 < min4
  end

  diff1 = max1 - min1
  diff2 = max2 - min2
  diff3 = max3 - min3
  diff4 = max4 - min4

  [diff1, diff2, diff3, diff4].max
end
```

## Scala

```scala
object Solution {
  def maxAbsValExpr(arr1: Array[Int], arr2: Array[Int]): Int = {
    var max1, min1 = Long.MinValue
    var max2, min2 = Long.MaxValue
    var max3, min3 = Long.MinValue
    var max4, min4 = Long.MaxValue

    // Initialize mins and maxes properly
    max1 = Long.MinValue; min1 = Long.MaxValue
    max2 = Long.MinValue; min2 = Long.MaxValue
    max3 = Long.MinValue; min3 = Long.MaxValue
    max4 = Long.MinValue; min4 = Long.MaxValue

    for (i <- arr1.indices) {
      val a = arr1(i).toLong
      val b = arr2(i).toLong
      val idx = i.toLong

      val v1 = a + b + idx
      val v2 = a + b - idx
      val v3 = a - b + idx
      val v4 = a - b - idx

      if (v1 > max1) max1 = v1
      if (v1 < min1) min1 = v1

      if (v2 > max2) max2 = v2
      if (v2 < min2) min2 = v2

      if (v3 > max3) max3 = v3
      if (v3 < min3) min3 = v3

      if (v4 > max4) max4 = v4
      if (v4 < min4) min4 = v4
    }

    var ans = Long.MinValue
    ans = math.max(ans, max1 - min1)
    ans = math.max(ans, max2 - min2)
    ans = math.max(ans, max3 - min3)
    ans = math.max(ans, max4 - min4)

    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_abs_val_expr(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let n = arr1.len();
        let mut answer = i32::MIN;
        // Four sign combinations with the index term always positive
        for combo in 0..4 {
            let mut max_val = i32::MIN;
            let mut min_val = i32::MAX;
            for i in 0..n {
                let a = arr1[i];
                let b = arr2[i];
                let val = match combo {
                    0 => a + b + i as i32,          // +a +b +i
                    1 => a - b + i as i32,          // +a -b +i
                    2 => -a + b + i as i32,         // -a +b +i
                    _ => -a - b + i as i32,         // -a -b +i
                };
                if val > max_val { max_val = val; }
                if val < min_val { min_val = val; }
            }
            let diff = max_val - min_val;
            if diff > answer { answer = diff; }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (max-abs-val-expr arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((vec1 (list->vector arr1))
         (vec2 (list->vector arr2))
         (n    (vector-length vec1)))
    (if (= n 0)
        0
        (let* ((a0 (vector-ref vec1 0))
               (b0 (vector-ref vec2 0))
               (v1-0 (+ a0 b0 0))
               (v2-0 (+ a0 b0 (- 0)))
               (v3-0 (+ a0 (- b0) 0))
               (v4-0 (+ a0 (- b0) (- 0))))
          (let-values ([(min1 max1 min2 max2 min3 max3 min4 max4)
                        (for/fold ([m1 v1-0] [M1 v1-0]
                                   [m2 v2-0] [M2 v2-0]
                                   [m3 v3-0] [M3 v3-0]
                                   [m4 v4-0] [M4 v4-0])
                                  ([i (in-range 1 n)])
                          (define a (vector-ref vec1 i))
                          (define b (vector-ref vec2 i))
                          (define val1 (+ a b i))
                          (define val2 (+ a b (- i)))
                          (define val3 (+ a (- b) i))
                          (define val4 (+ a (- b) (- i)))
                          (values (min m1 val1) (max M1 val1)
                                  (min m2 val2) (max M2 val2)
                                  (min m3 val3) (max M3 val3)
                                  (min m4 val4) (max M4 val4)))])
            (let ([d1 (- max1 min1)]
                  [d2 (- max2 min2)]
                  [d3 (- max3 min3)]
                  [d4 (- max4 min4)])
              (apply max (list d1 d2 d3 d4))))))))
```

## Erlang

```erlang
-spec max_abs_val_expr(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
max_abs_val_expr(Arr1, Arr2) ->
    Large = 1000000000,
    loop(Arr1, Arr2, 0, Large, -Large, Large, -Large, Large, -Large, Large, -Large).

loop([], [], _I, Min1, Max1, Min2, Max2, Min3, Max3, Min4, Max4) ->
    D1 = Max1 - Min1,
    D2 = Max2 - Min2,
    D3 = Max3 - Min3,
    D4 = Max4 - Min4,
    max_of_four(D1, D2, D3, D4);
loop([A|As], [B|Bs], I, Min1, Max1, Min2, Max2, Min3, Max3, Min4, Max4) ->
    V1 = A + B + I,
    V2 = A + B - I,
    V3 = A - B + I,
    V4 = A - B - I,
    NewMin1 = erlang:min(Min1, V1),
    NewMax1 = erlang:max(Max1, V1),
    NewMin2 = erlang:min(Min2, V2),
    NewMax2 = erlang:max(Max2, V2),
    NewMin3 = erlang:min(Min3, V3),
    NewMax3 = erlang:max(Max3, V3),
    NewMin4 = erlang:min(Min4, V4),
    NewMax4 = erlang:max(Max4, V4),
    loop(As, Bs, I + 1,
         NewMin1, NewMax1,
         NewMin2, NewMax2,
         NewMin3, NewMax3,
         NewMin4, NewMax4).

max_of_two(A, B) when A >= B -> A;
max_of_two(_, B) -> B.

max_of_four(A, B, C, D) ->
    max_of_two(max_of_two(A, B), max_of_two(C, D)).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_abs_val_expr(arr1 :: [integer], arr2 :: [integer]) :: integer
  def max_abs_val_expr(arr1, arr2) do
    init = {
      -1_000_000_000, 1_000_000_000,
      -1_000_000_000, 1_000_000_000,
      -1_000_000_000, 1_000_000_000,
      -1_000_000_000, 1_000_000_000
    }

    {max1, min1, max2, min2, max3, min3, max4, min4} =
      Enum.reduce(Enum.with_index(Enum.zip(arr1, arr2)), init, fn {{a1, a2}, i},
                                                                {mx1, mn1, mx2, mn2,
                                                                 mx3, mn3, mx4, mn4} ->
        p1 = a1 + a2 + i
        p2 = a1 + a2 - i
        p3 = a1 - a2 + i
        p4 = a1 - a2 - i

        {
          max(p1, mx1), min(p1, mn1),
          max(p2, mx2), min(p2, mn2),
          max(p3, mx3), min(p3, mn3),
          max(p4, mx4), min(p4, mn4)
        }
      end)

    diff1 = max1 - min1
    diff2 = max2 - min2
    diff3 = max3 - min3
    diff4 = max4 - min4

    Enum.max([diff1, diff2, diff3, diff4])
  end
end
```
