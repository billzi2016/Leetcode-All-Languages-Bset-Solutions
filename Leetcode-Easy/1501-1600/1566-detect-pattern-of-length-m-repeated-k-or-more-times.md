# 1566. Detect Pattern of Length M Repeated K or More Times

## Cpp

```cpp
class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
        int n = arr.size();
        for (int i = 0; i <= n - m; ++i) {
            int cnt = 1;
            while (i + cnt * m + m <= n) {
                bool same = true;
                for (int j = 0; j < m; ++j) {
                    if (arr[i + j] != arr[i + cnt * m + j]) {
                        same = false;
                        break;
                    }
                }
                if (!same) break;
                ++cnt;
                if (cnt >= k) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        int n = arr.length;
        for (int i = 0; i <= n - m * k; i++) {
            boolean ok = true;
            for (int j = 0; j < m && ok; j++) {
                int val = arr[i + j];
                for (int t = 1; t < k; t++) {
                    if (arr[i + j + t * m] != val) {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        n = len(arr)
        # Need at least m * k elements to have such a pattern
        if n < m * k:
            return False
        for i in range(n - m * k + 1):
            pattern = arr[i:i + m]
            match = True
            for rep in range(1, k):
                start = i + rep * m
                if arr[start:start + m] != pattern:
                    match = False
                    break
            if match:
                return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        # Need at least m * k elements to form the repeated pattern
        for start in range(n - m * k + 1):
            match = True
            # Compare each position within the pattern block
            for offset in range(m):
                base_val = arr[start + offset]
                # Check subsequent repetitions
                for rep in range(1, k):
                    if arr[start + offset + rep * m] != base_val:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
        return False
```

## C

```c
#include <stdbool.h>

bool containsPattern(int* arr, int arrSize, int m, int k) {
    if (m * k > arrSize) return false;
    for (int i = 0; i <= arrSize - m * k; ++i) {
        bool ok = true;
        for (int r = 1; r < k && ok; ++r) {
            for (int j = 0; j < m; ++j) {
                if (arr[i + r * m + j] != arr[i + j]) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool ContainsPattern(int[] arr, int m, int k) {
        int n = arr.Length;
        if (m * k > n) return false;
        for (int start = 0; start <= n - m * k; start++) {
            bool match = true;
            for (int rep = 1; rep < k && match; rep++) {
                for (int offset = 0; offset < m; offset++) {
                    if (arr[start + offset] != arr[start + rep * m + offset]) {
                        match = false;
                        break;
                    }
                }
            }
            if (match) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} m
 * @param {number} k
 * @return {boolean}
 */
var containsPattern = function(arr, m, k) {
    const n = arr.length;
    // Need at least m * k elements from start index i
    for (let i = 0; i <= n - m * k; ++i) {
        let match = true;
        // Check each repetition
        for (let rep = 1; rep < k && match; ++rep) {
            for (let j = 0; j < m; ++j) {
                if (arr[i + j] !== arr[i + rep * m + j]) {
                    match = false;
                    break;
                }
            }
        }
        if (match) return true;
    }
    return false;
};
```

## Typescript

```typescript
function containsPattern(arr: number[], m: number, k: number): boolean {
    const n = arr.length;
    for (let start = 0; start <= n - m * k; start++) {
        let valid = true;
        for (let rep = 1; rep < k && valid; rep++) {
            for (let offset = 0; offset < m; offset++) {
                if (arr[start + offset] !== arr[start + rep * m + offset]) {
                    valid = false;
                    break;
                }
            }
        }
        if (valid) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @param Integer $k
     * @return Boolean
     */
    function containsPattern($arr, $m, $k) {
        $n = count($arr);
        for ($i = 0; $i <= $n - $m * $k; $i++) {
            $ok = true;
            for ($rep = 1; $rep < $k && $ok; $rep++) {
                for ($j = 0; $j < $m; $j++) {
                    if ($arr[$i + $j] !== $arr[$i + $rep * $m + $j]) {
                        $ok = false;
                        break;
                    }
                }
            }
            if ($ok) {
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
    func containsPattern(_ arr: [Int], _ m: Int, _ k: Int) -> Bool {
        let n = arr.count
        if m * k > n { return false }
        for i in 0...(n - m * k) {
            var ok = true
            for rep in 1..<k {
                for j in 0..<m {
                    if arr[i + j] != arr[i + rep * m + j] {
                        ok = false
                        break
                    }
                }
                if !ok { break }
            }
            if ok { return true }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun containsPattern(arr: IntArray, m: Int, k: Int): Boolean {
        val n = arr.size
        if (n < m * k) return false
        for (i in 0..(n - m * k)) {
            var ok = true
            for (r in 1 until k) {
                for (j in 0 until m) {
                    if (arr[i + j] != arr[i + r * m + j]) {
                        ok = false
                        break
                    }
                }
                if (!ok) break
            }
            if (ok) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool containsPattern(List<int> arr, int m, int k) {
    int n = arr.length;
    for (int i = 0; i <= n - m * k; ++i) {
      bool ok = true;
      for (int t = 1; t < k && ok; ++t) {
        for (int j = 0; j < m; ++j) {
          if (arr[i + j] != arr[i + t * m + j]) {
            ok = false;
            break;
          }
        }
      }
      if (ok) return true;
    }
    return false;
  }
}
```

## Golang

```go
func containsPattern(arr []int, m int, k int) bool {
    n := len(arr)
    if m*k > n {
        return false
    }
    for i := 0; i <= n-m*k; i++ {
        ok := true
        for rep := 1; rep < k && ok; rep++ {
            for offset := 0; offset < m; offset++ {
                if arr[i+offset] != arr[i+rep*m+offset] {
                    ok = false
                    break
                }
            }
        }
        if ok {
            return true
        }
    }
    return false
}
```

## Ruby

```ruby
def contains_pattern(arr, m, k)
  n = arr.length
  return false if m * k > n
  (0..n - m * k).each do |i|
    ok = true
    (0...m).each do |j|
      base = arr[i + j]
      (1...k).each do |r|
        if arr[i + r * m + j] != base
          ok = false
          break
        end
      end
      break unless ok
    end
    return true if ok
  end
  false
end
```

## Scala

```scala
object Solution {
    def containsPattern(arr: Array[Int], m: Int, k: Int): Boolean = {
        val n = arr.length
        if (n < m * k) return false
        for (i <- 0 to n - m * k) {
            var good = true
            var t = 1
            while (t < k && good) {
                var j = 0
                while (j < m && good) {
                    if (arr(i + j) != arr(i + t * m + j)) good = false
                    j += 1
                }
                t += 1
            }
            if (good) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn contains_pattern(arr: Vec<i32>, m: i32, k: i32) -> bool {
        let n = arr.len();
        let m_usize = m as usize;
        let k_usize = k as usize;
        if m_usize * k_usize > n {
            return false;
        }
        for start in 0..=n - m_usize * k_usize {
            let mut ok = true;
            for rep in 1..k_usize {
                for offset in 0..m_usize {
                    if arr[start + offset] != arr[start + rep * m_usize + offset] {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
            }
            if ok {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (contains-pattern arr m k)
  (-> (listof exact-integer?) exact-integer? exact-integer? boolean?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (define (equal-block? s1 s2 len)
      (let loop ((j 0))
        (or (= j len)
            (and (= (vector-ref v (+ s1 j)) (vector-ref v (+ s2 j)))
                 (loop (+ j 1))))))
    (define (has-k-repeats? i)
      (let loop ((rep 0))
        (if (= rep k)
            #t
            (let ((start2 (+ i (* rep m))))
              (and (<= (+ start2 m) n)
                   (equal-block? i start2 m)
                   (loop (add1 rep)))))))
    (let loop ((i 0))
      (cond [(> i (- n (* m k))) #f]
            [(has-k-repeats? i) #t]
            [else (loop (+ i 1))]))))
```

## Erlang

```erlang
-spec contains_pattern(Arr :: [integer()], M :: integer(), K :: integer()) -> boolean().
contains_pattern(Arr, M, K) ->
    N = length(Arr),
    case N - M * K of
        MaxStart when MaxStart < 0 -> false;
        MaxStart ->
            T = list_to_tuple(Arr),
            check_start(0, MaxStart, M, K, T)
    end.

check_start(I, Max, _M, _K, _T) when I > Max ->
    false;
check_start(I, Max, M, K, T) ->
    case pattern_match(I, M, K, T) of
        true -> true;
        false -> check_start(I + 1, Max, M, K, T)
    end.

pattern_match(Start, M, K, T) ->
    pattern_repeat(1, K, Start, M, T).

pattern_repeat(R, K, _Start, _M, _T) when R >= K ->
    true;
pattern_repeat(R, K, Start, M, T) ->
    case blocks_equal(Start, Start + R * M, M, T) of
        true -> pattern_repeat(R + 1, K, Start, M, T);
        false -> false
    end.

blocks_equal(_A, _B, 0, _T) ->
    true;
blocks_equal(A, B, Len, T) ->
    case element(A + 1, T) =:= element(B + 1, T) of
        true -> blocks_equal(A + 1, B + 1, Len - 1, T);
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec contains_pattern(arr :: [integer], m :: integer, k :: integer) :: boolean
  def contains_pattern(arr, m, k) do
    n = length(arr)
    max_start = n - m * k

    if max_start < 0 do
      false
    else
      Enum.any?(0..max_start, fn start ->
        pattern = Enum.slice(arr, start, m)

        Enum.all?(1..(k - 1), fn rep ->
          segment = Enum.slice(arr, start + rep * m, m)
          segment == pattern
        end)
      end)
    end
  end
end
```
