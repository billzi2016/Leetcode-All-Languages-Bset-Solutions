# 0978. Longest Turbulent Subarray

## Cpp

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        int n = arr.size();
        if (n < 2) return n;
        int ans = 1, cur = 1;
        for (int i = 1; i < n; ++i) {
            if (arr[i] == arr[i-1]) {
                cur = 1;
            } else if (i == 1 ||
                       (arr[i-2] < arr[i-1] && arr[i-1] > arr[i]) ||
                       (arr[i-2] > arr[i-1] && arr[i-1] < arr[i])) {
                ++cur;
            } else {
                cur = 2; // start new window with arr[i-1], arr[i]
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int n = arr.length;
        if (n < 2) return n;
        int ans = 1;
        int start = 0;
        int prevCmp = 0; // comparison of previous adjacent pair

        for (int i = 1; i < n; i++) {
            int curCmp;
            if (arr[i - 1] < arr[i]) {
                curCmp = -1;
            } else if (arr[i - 1] > arr[i]) {
                curCmp = 1;
            } else {
                curCmp = 0;
            }

            if (curCmp == 0) {
                start = i;
                prevCmp = 0;
            } else {
                if (prevCmp != 0 && curCmp * prevCmp != -1) {
                    // not alternating, restart from previous element
                    start = i - 1;
                }
                ans = Math.max(ans, i - start + 1);
                prevCmp = curCmp;
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 2:
            return n
        ans = inc = dec = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
        ans = 1
        cur = 1
        prev = 0  # previous comparison sign
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff > 0:
                cmp = 1
            elif diff < 0:
                cmp = -1
            else:
                cmp = 0
            if cmp == 0:
                cur = 1
            else:
                if prev * cmp == -1:
                    cur += 1
                else:
                    cur = 2
            ans = max(ans, cur)
            prev = cmp
        return ans
```

## C

```c
int max(int a, int b) {
    return a > b ? a : b;
}

int maxTurbulenceSize(int* arr, int arrSize) {
    if (arrSize == 0) return 0;
    if (arrSize == 1) return 1;

    int inc = 1; // length ending with '>'
    int dec = 1; // length ending with '<'
    int ans = 1;

    for (int i = 1; i < arrSize; ++i) {
        if (arr[i] > arr[i - 1]) {
            inc = dec + 1;
            dec = 1;
        } else if (arr[i] < arr[i - 1]) {
            dec = inc + 1;
            inc = 1;
        } else {
            inc = dec = 1;
        }
        ans = max(ans, max(inc, dec));
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxTurbulenceSize(int[] arr) {
        int n = arr.Length;
        if (n == 1) return 1;

        int maxLen = 1;
        int curLen = 1;
        int prevCmp = 0; // comparison between arr[i-2] and arr[i-1]

        for (int i = 1; i < n; i++) {
            int cmp;
            if (arr[i - 1] < arr[i]) cmp = -1;
            else if (arr[i - 1] > arr[i]) cmp = 1;
            else cmp = 0;

            if (cmp == 0) {
                curLen = 1;
            } else if (prevCmp == 0 || cmp * prevCmp == -1) {
                curLen += 1;
            } else {
                curLen = 2; // start new subarray with previous element and current
            }

            maxLen = Math.Max(maxLen, curLen);
            prevCmp = cmp;
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
    const n = arr.length;
    if (n < 2) return n;

    const cmp = (a, b) => (a < b ? -1 : a > b ? 1 : 0);

    let ans = 1;
    let left = 0; // start index of current turbulent window

    for (let i = 1; i < n; ++i) {
        const cur = cmp(arr[i - 1], arr[i]);

        if (cur === 0) {
            left = i;
        } else if (i > 1) {
            const prev = cmp(arr[i - 2], arr[i - 1]);
            // If not alternating, reset window start to previous element
            if (prev * cur !== -1) {
                left = i - 1;
            }
        }

        ans = Math.max(ans, i - left + 1);
    }

    return ans;
};
```

## Typescript

```typescript
function maxTurbulenceSize(arr: number[]): number {
    const n = arr.length;
    if (n < 2) return n;
    let up = 1, down = 1, ans = 1;
    for (let i = 1; i < n; ++i) {
        if (arr[i] > arr[i - 1]) {
            up = down + 1;
            down = 1;
        } else if (arr[i] < arr[i - 1]) {
            down = up + 1;
            up = 1;
        } else {
            up = down = 1;
        }
        ans = Math.max(ans, up, down);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maxTurbulenceSize($arr) {
        $n = count($arr);
        if ($n < 2) return $n;
        $maxLen = 1;
        $anchor = 0; // start index of current turbulent window

        for ($i = 1; $i < $n; ++$i) {
            $c = $arr[$i - 1] <=> $arr[$i]; // -1, 0, or 1
            if ($c == 0) {
                $anchor = $i;
            } else {
                if ($i > 1) {
                    $prevC = $arr[$i - 2] <=> $arr[$i - 1];
                    if ($c * $prevC != -1) { // not alternating
                        $anchor = $i - 1;
                    }
                }
            }
            $maxLen = max($maxLen, $i - $anchor + 1);
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maxTurbulenceSize(_ arr: [Int]) -> Int {
        let n = arr.count
        if n < 2 { return n }
        var maxLen = 1
        var start = 0
        var prevCmp = 0
        
        for i in 1..<n {
            let curCmp: Int
            if arr[i] > arr[i - 1] {
                curCmp = 1
            } else if arr[i] < arr[i - 1] {
                curCmp = -1
            } else {
                curCmp = 0
            }
            
            if curCmp == 0 {
                start = i
                prevCmp = 0
            } else {
                if prevCmp == 0 || curCmp * prevCmp != -1 {
                    start = i - 1
                }
                let len = i - start + 1
                if len > maxLen { maxLen = len }
                prevCmp = curCmp
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTurbulenceSize(arr: IntArray): Int {
        val n = arr.size
        if (n < 2) return n
        var ans = 1
        var cur = 1
        var prevCmp = 0
        for (i in 1 until n) {
            val cmp = when {
                arr[i - 1] < arr[i] -> 1
                arr[i - 1] > arr[i] -> -1
                else -> 0
            }
            if (cmp == 0) {
                cur = 1
            } else if (prevCmp * cmp == -1) {
                cur += 1
            } else {
                cur = 2
            }
            ans = kotlin.math.max(ans, cur)
            prevCmp = cmp
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxTurbulenceSize(List<int> arr) {
    int n = arr.length;
    if (n < 2) return n;

    int ans = 1;
    int start = 0;
    int prevCmp = 0; // sign of previous comparison

    for (int i = 1; i < n; i++) {
      int curCmp;
      if (arr[i] > arr[i - 1]) {
        curCmp = 1;
      } else if (arr[i] < arr[i - 1]) {
        curCmp = -1;
      } else {
        curCmp = 0;
      }

      if (curCmp == 0) {
        start = i;
        prevCmp = 0;
      } else {
        if (prevCmp != 0 && prevCmp * curCmp != -1) {
          start = i - 1;
        }
        int len = i - start + 1;
        if (len > ans) ans = len;
        prevCmp = curCmp;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxTurbulenceSize(arr []int) int {
    n := len(arr)
    if n < 2 {
        return n
    }
    maxLen, cur, prevCmp := 1, 1, 0
    for i := 1; i < n; i++ {
        var cmp int
        if arr[i] > arr[i-1] {
            cmp = 1
        } else if arr[i] < arr[i-1] {
            cmp = -1
        } else {
            cmp = 0
        }
        if cmp == 0 {
            cur = 1
        } else if prevCmp == 0 || cmp*prevCmp == -1 {
            cur++
        } else {
            cur = 2
        }
        if cur > maxLen {
            maxLen = cur
        }
        prevCmp = cmp
    }
    return maxLen
}
```

## Ruby

```ruby
def max_turbulence_size(arr)
  n = arr.length
  return 1 if n == 1

  inc = dec = 1
  ans = 1

  (1...n).each do |i|
    if arr[i] > arr[i - 1]
      inc = dec + 1
      dec = 1
    elsif arr[i] < arr[i - 1]
      dec = inc + 1
      inc = 1
    else
      inc = dec = 1
    end
    ans = [ans, inc, dec].max
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxTurbulenceSize(arr: Array[Int]): Int = {
        val n = arr.length
        if (n < 2) return n
        var maxLen = 1
        var curLen = 1
        var prevCmp = 0 // -1, 0, or 1

        for (i <- 1 until n) {
            val cmp = 
                if (arr(i) > arr(i - 1)) 1
                else if (arr(i) < arr(i - 1)) -1
                else 0

            if (cmp == 0) {
                curLen = 1
            } else if (prevCmp * cmp == -1) {
                curLen += 1
            } else {
                curLen = 2 // start new subarray from i-1 to i
            }

            maxLen = math.max(maxLen, curLen)
            prevCmp = cmp
        }
        maxLen
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n < 2 {
            return n as i32;
        }
        let mut max_len = 1usize;
        let mut cur_len = 1usize;
        let mut prev_cmp: i8 = 0;
        for i in 1..n {
            let cmp: i8 = if arr[i] > arr[i - 1] {
                1
            } else if arr[i] < arr[i - 1] {
                -1
            } else {
                0
            };
            if cmp == 0 {
                cur_len = 1;
            } else if prev_cmp * cmp == -1 {
                cur_len += 1;
            } else {
                cur_len = 2;
            }
            if cur_len > max_len {
                max_len = cur_len;
            }
            prev_cmp = cmp;
        }
        max_len as i32
    }
}
```

## Racket

```racket
(define (sign x)
  (cond [(> x 0) 1]
        [(< x 0) -1]
        [else 0]))

(define/contract (max-turbulence-size arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length arr))
         (v (list->vector arr)))
    (cond
      [(= n 0) 0]
      [(= n 1) 1]
      [else
       (let loop ((i 1)          ; current index
                  (start 0)      ; start of current turbulent window
                  (prev-cmp 0)   ; comparison between v[i-1] and v[i-2]
                  (max-len 1))   ; best length found so far
         (if (>= i n)
             max-len
             (let* ((cur (- (vector-ref v i) (vector-ref v (- i 1))))
                    (cmp (sign cur)))
               (cond
                 [(= cmp 0)
                  ;; equal breaks turbulence completely
                  (loop (+ i 1) (+ i 1) 0 (max max-len 1))]
                 [(= prev-cmp 0)
                  ;; first non‑zero comparison in a new segment
                  (let ((new-start (- i 1)))
                    (loop (+ i 1) new-start cmp (max max-len 2)))]
                 [else
                  (if (= (* cmp prev-cmp) -1)
                      ;; alternating sign – extend window
                      (loop (+ i 1) start cmp (max max-len (+ (- i start) 1)))
                      ;; same sign – restart from previous element
                      (let ((new-start (- i 1)))
                        (loop (+ i 1) new-start cmp (max max-len 2))))])))))])))
```

## Erlang

```erlang
-spec max_turbulence_size(Arr :: [integer()]) -> integer().
max_turbulence_size(Arr) ->
    case Arr of
        [] -> 0;
        [_] -> 1;
        [First, Second | Tail] ->
            Cmp = cmp(Second, First),
            CurLen = if Cmp == 0 -> 1; true -> 2 end,
            Max0 = CurLen,
            helper(Second, Tail, CurLen, Cmp, Max0)
    end.

-spec helper(prev :: integer(), rest :: [integer()], cur_len :: integer(),
             prev_cmp :: integer(), max_len :: integer()) -> integer().
helper(_Prev, [], _CurLen, _PrevCmp, Max) ->
    Max;
helper(Prev, [Curr | Rest], CurLen, PrevCmp, Max) ->
    Cmp = cmp(Curr, Prev),
    case Cmp of
        0 ->
            NewCur = 1,
            NewPrevCmp = 0,
            NewMax = erlang:max(Max, NewCur);
        _ ->
            case PrevCmp of
                0 ->
                    NewCur = 2,
                    NewPrevCmp = Cmp,
                    NewMax = erlang:max(Max, NewCur);
                _ when Cmp * PrevCmp == -1 ->
                    NewCur = CurLen + 1,
                    NewPrevCmp = Cmp,
                    NewMax = erlang:max(Max, NewCur);
                _ ->
                    NewCur = 2,
                    NewPrevCmp = Cmp,
                    NewMax = erlang:max(Max, NewCur)
            end
    end,
    helper(Curr, Rest, NewCur, NewPrevCmp, NewMax).

-spec cmp(A :: integer(), B :: integer()) -> integer().
cmp(A, B) when A > B -> 1;
cmp(A, B) when A < B -> -1;
cmp(_, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_turbulence_size(arr :: [integer]) :: integer
  def max_turbulence_size(arr) do
    case arr do
      [] -> 0
      [_] -> 1
      _ ->
        {ans, _, _} =
          Enum.zip(arr, tl(arr))
          |> Enum.reduce({1, 1, 1}, fn {a, b}, {ans, inc, dec} ->
            cond do
              a < b ->
                new_inc = dec + 1
                new_dec = 1
                {max(ans, max(new_inc, new_dec)), new_inc, new_dec}
              a > b ->
                new_dec = inc + 1
                new_inc = 1
                {max(ans, max(new_inc, new_dec)), new_inc, new_dec}
              true ->
                {max(ans, 1), 1, 1}
            end
          end)

        ans
    end
  end
end
```
