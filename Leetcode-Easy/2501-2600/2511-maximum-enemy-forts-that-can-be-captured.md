# 2511. Maximum Enemy Forts That Can Be Captured

## Cpp

```cpp
class Solution {
public:
    int captureForts(vector<int>& forts) {
        int n = forts.size();
        int ans = 0;
        int last = -1; // index of the previous non-zero fort
        for (int i = 0; i < n; ++i) {
            if (forts[i] != 0) {
                if (last != -1 && forts[i] != forts[last]) {
                    ans = max(ans, i - last - 1);
                }
                last = i;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int captureForts(int[] forts) {
        int max = 0;
        int prevIdx = -1; // index of previous non -1 element
        for (int i = 0; i < forts.length; i++) {
            if (forts[i] == -1) continue;
            if (prevIdx != -1 && forts[prevIdx] != forts[i]) {
                int captured = i - prevIdx - 1;
                if (captured > max) max = captured;
            }
            prevIdx = i;
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def captureForts(self, forts):
        """
        :type forts: List[int]
        :rtype: int
        """
        n = len(forts)
        max_captured = 0

        for i in range(n):
            if forts[i] != 1:
                continue

            # Move to the right
            j = i + 1
            while j < n and forts[j] == -1:
                j += 1
            if j < n and forts[j] == 0:
                max_captured = max(max_captured, j - i - 1)

            # Move to the left
            j = i - 1
            while j >= 0 and forts[j] == -1:
                j -= 1
            if j >= 0 and forts[j] == 0:
                max_captured = max(max_captured, i - j - 1)

        return max_captured
```

## Python3

```python
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last = -1
        ans = 0
        for i, v in enumerate(forts):
            if v != -1:
                if last != -1 and forts[last] != v:
                    ans = max(ans, i - last - 1)
                last = i
        return ans
```

## C

```c
int captureForts(int* forts, int fortsSize) {
    int maxCaptured = 0;
    int lastIdx = -1; // index of the most recent non‑-1 fort
    
    for (int i = 0; i < fortsSize; ++i) {
        if (forts[i] == -1) continue;          // cannot be an endpoint
        if (lastIdx != -1 && forts[lastIdx] != forts[i]) {
            // both endpoints are either 0 or 1 and differ, so one is our fort and the other empty
            int captured = i - lastIdx - 1;    // number of enemy forts between them
            if (captured > maxCaptured) maxCaptured = captured;
        }
        lastIdx = i;                            // update most recent non‑-1 position
    }
    
    return maxCaptured;
}
```

## Csharp

```csharp
public class Solution {
    public int CaptureForts(int[] forts) {
        int n = forts.Length;
        int maxCapture = 0;
        int i = 0;
        while (i < n) {
            if (forts[i] == 1 || forts[i] == 0) {
                int j = i + 1;
                // skip enemy forts (-1)
                while (j < n && forts[j] == -1) {
                    j++;
                }
                // now forts[j] is not -1 or j == n
                if (j < n && ((forts[i] == 1 && forts[j] == 0) || (forts[i] == 0 && forts[j] == 1))) {
                    int captured = j - i - 1; // all between are -1
                    if (captured > maxCapture) {
                        maxCapture = captured;
                    }
                }
                i = j; // continue from the next non -1 position
            } else {
                i++;
            }
        }
        return maxCapture;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} forts
 * @return {number}
 */
var captureForts = function(forts) {
    let prev = -1;
    let maxCapture = 0;
    for (let i = 0; i < forts.length; i++) {
        if (forts[i] !== 0) {
            if (prev !== -1 && forts[i] !== forts[prev]) {
                const captured = i - prev - 1;
                if (captured > maxCapture) maxCapture = captured;
            }
            prev = i;
        }
    }
    return maxCapture;
};
```

## Typescript

```typescript
function captureForts(forts: number[]): number {
    let maxCaptured = 0;
    let lastIdx = -1;   // index of the most recent non‑zero fort
    let lastVal = 0;    // its value (1 or -1)

    for (let i = 0; i < forts.length; i++) {
        const cur = forts[i];
        if (cur !== 0) {
            if (lastIdx !== -1 && cur !== lastVal) {
                // opposite forts with only zeros in between
                const captured = i - lastIdx - 1;
                if (captured > maxCaptured) maxCaptured = captured;
            }
            lastIdx = i;
            lastVal = cur;
        }
    }

    return maxCaptured;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $forts
     * @return Integer
     */
    function captureForts($forts) {
        $n = count($forts);
        $max = 0;
        $prevIdx = -1;
        $prevVal = null;

        for ($i = 0; $i < $n; $i++) {
            if ($forts[$i] == -1) {
                continue;
            }
            // $forts[$i] is either 0 or 1
            if ($prevIdx != -1 && $forts[$i] != $prevVal) {
                $max = max($max, $i - $prevIdx - 1);
            }
            $prevIdx = $i;
            $prevVal = $forts[$i];
        }

        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func captureForts(_ forts: [Int]) -> Int {
        var lastIdx = -1
        var maxCaptured = 0
        for (i, v) in forts.enumerated() {
            if v != 0 {
                if lastIdx != -1 && forts[lastIdx] != v {
                    let captured = i - lastIdx - 1
                    if captured > maxCaptured { maxCaptured = captured }
                }
                lastIdx = i
            }
        }
        return maxCaptured
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun captureForts(forts: IntArray): Int {
        var prev = -1
        var maxCapture = 0
        for (i in forts.indices) {
            if (forts[i] != -1) {
                if (prev != -1 && forts[prev] != forts[i]) {
                    val captured = i - prev - 1
                    if (captured > maxCapture) maxCapture = captured
                }
                prev = i
            }
        }
        return maxCapture
    }
}
```

## Dart

```dart
class Solution {
  int captureForts(List<int> forts) {
    int last = -1;
    int maxCapture = 0;
    for (int i = 0; i < forts.length; ++i) {
      if (forts[i] != 0) {
        if (last != -1 && forts[i] != forts[last]) {
          int captured = i - last - 1;
          if (captured > maxCapture) {
            maxCapture = captured;
          }
        }
        last = i;
      }
    }
    return maxCapture;
  }
}
```

## Golang

```go
func captureForts(forts []int) int {
    prev := -1
    maxCapture := 0
    for i, v := range forts {
        if v == -1 {
            continue
        }
        if prev != -1 && forts[prev] != v {
            captured := i - prev - 1
            if captured > maxCapture {
                maxCapture = captured
            }
        }
        prev = i
    }
    return maxCapture
}
```

## Ruby

```ruby
def capture_forts(forts)
  max_captures = 0
  prev_index = nil

  forts.each_with_index do |val, i|
    next if val == -1

    unless prev_index.nil?
      if forts[prev_index] != val
        captures = i - prev_index - 1
        max_captures = captures if captures > max_captures
      end
    end

    prev_index = i
  end

  max_captures
end
```

## Scala

```scala
object Solution {
    def captureForts(forts: Array[Int]): Int = {
        var maxCapture = 0
        var i = 0
        val n = forts.length
        while (i < n) {
            if (forts(i) == 0) {
                i += 1
            } else {
                var j = i + 1
                while (j < n && forts(j) == -1) {
                    j += 1
                }
                if (j < n && ((forts(i) == 1 && forts(j) == 0) || (forts(i) == 0 && forts(j) == 1))) {
                    maxCapture = math.max(maxCapture, j - i - 1)
                }
                i = j
            }
        }
        maxCapture
    }
}
```

## Rust

```rust
impl Solution {
    pub fn capture_forts(forts: Vec<i32>) -> i32 {
        let mut max_captured = 0;
        let mut last_idx: i32 = -1;
        let mut last_val: i32 = 2; // sentinel different from -1,0,1
        for (i, &v) in forts.iter().enumerate() {
            if v != 0 {
                if last_idx != -1 && ((last_val == 1 && v == -1) || (last_val == -1 && v == 1)) {
                    let captured = i as i32 - last_idx - 1;
                    if captured > max_captured {
                        max_captured = captured;
                    }
                }
                last_idx = i as i32;
                last_val = v;
            }
        }
        max_captured
    }
}
```

## Racket

```racket
(define/contract (capture-forts forts)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length forts))
         (vec (list->vector forts)))
    (let loop ((i 0) (best 0))
      (if (>= i n)
          best
          (let ((v (vector-ref vec i)))
            (if (= v -1)
                (loop (+ i 1) best)
                (let inner ((j (+ i 1)) (cnt 0))
                  (cond
                    [(>= j n) (loop (+ i 1) best)]
                    [(= (vector-ref vec j) -1)
                     (inner (+ j 1) (+ cnt 1))]
                    [else
                     (if (and (not (= (vector-ref vec j) v)) (> cnt 0))
                         (let ((new-best (max best cnt)))
                           (loop (+ i 1) new-best))
                         (loop (+ i 1) best))]))))))))
```

## Erlang

```erlang
-spec capture_forts(Forts :: [integer()]) -> integer().
capture_forts(Forts) ->
    capture_forts(Forts, 0, undefined, undefined, 0).

capture_forts([], _Idx, _LastIdx, _LastVal, Max) ->
    Max;
capture_forts([H|T], Idx, LastIdx, LastVal, Max) ->
    case H of
        0 ->
            capture_forts(T, Idx + 1, LastIdx, LastVal, Max);
        _ ->
            case LastVal of
                undefined ->
                    capture_forts(T, Idx + 1, Idx, H, Max);
                _ when H =/= LastVal ->
                    Dist = Idx - LastIdx - 1,
                    NewMax = erlang:max(Max, Dist),
                    capture_forts(T, Idx + 1, Idx, H, NewMax);
                _ ->
                    capture_forts(T, Idx + 1, Idx, H, Max)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec capture_forts(forts :: [integer]) :: integer
  def capture_forts(forts) do
    {max_captures, _prev_idx, _prev_val} =
      Enum.reduce(Enum.with_index(forts), {0, nil, nil}, fn {val, idx},
                                                          {max, prev_idx, prev_val} ->
        if val == -1 do
          {max, prev_idx, prev_val}
        else
          new_max =
            if not is_nil(prev_idx) and
                 ((prev_val == 1 and val == 0) or (prev_val == 0 and val == 1)) do
              max(max, idx - prev_idx - 1)
            else
              max
            end

          {new_max, idx, val}
        end
      end)

    max_captures
  end
end
```
