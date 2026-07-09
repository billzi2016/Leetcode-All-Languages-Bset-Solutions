# 3208. Alternating Groups II

## Cpp

```cpp
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        if (n == 0) return 0;
        long long result = 0;          // use long long to avoid overflow in intermediate sum
        int cnt = 1;                   // length of current alternating segment
        int last = colors[0];
        int total = n + k - 1;         // length of the virtual extended array

        for (int i = 1; i < total; ++i) {
            int idx = i % n;
            if (colors[idx] == last) {
                cnt = 1;               // reset when two adjacent colors are equal
            } else {
                ++cnt;                 // extend the alternating segment
                if (cnt >= k) ++result;
            }
            last = colors[idx];
        }
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        int n = colors.length;
        int result = 0;
        int cnt = 1; // length of current alternating segment
        int last = colors[0];
        for (int i = 1; i < n + k - 1; i++) {
            int cur = colors[i % n];
            if (cur == last) {
                cnt = 1;
            } else {
                cnt++;
                if (cnt >= k) {
                    result++;
                }
            }
            last = cur;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        # count of consecutive alternating tiles ending at current position
        cnt = 1
        last = colors[0]
        result = 0

        # iterate over the array plus first (k-1) elements to handle wrap‑around
        for i in range(1, n + k - 1):
            cur = colors[i % n]
            if cur == last:
                cnt = 1          # pattern breaks, start new sequence from current tile
            else:
                cnt += 1
                if cnt >= k:
                    result += 1   # a valid alternating group of length k ends here
            last = cur

        return result
```

## Python3

```python
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if n == 0 or k > n:
            return 0

        res = 0
        cnt = 1  # length of current alternating segment
        last = colors[0]

        # iterate over the next (n + k - 2) elements after the first one
        for i in range(1, n + k - 1):
            idx = i % n
            if colors[idx] == last:
                cnt = 1
            else:
                cnt += 1
                if cnt >= k:
                    res += 1
            last = colors[idx]

        return res
```

## C

```c
int numberOfAlternatingGroups(int* colors, int colorsSize, int k) {
    int n = colorsSize;
    if (n == 0) return 0;

    int totalIter = n + k - 1;          // iterate over extended circular array
    int result = 0;
    int run = 1;                        // length of current alternating segment
    int last = colors[0];

    for (int i = 1; i < totalIter; ++i) {
        int cur = colors[i % n];
        if (cur == last) {
            run = 1;                    // reset when pattern breaks
        } else {
            ++run;
            if (run >= k) {
                ++result;               // each time we have a window of size k ending here
            }
        }
        last = cur;
    }

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfAlternatingGroups(int[] colors, int k) {
        int n = colors.Length;
        // Since k >= 3 per constraints, no need to handle k == 1 or 2 separately.
        int result = 0;
        int cnt = 1;                     // length of current alternating segment
        int last = colors[0];
        
        // Process the array plus the first (k-1) elements to account for wrap‑around windows
        for (int i = 1; i < n + k - 1; i++) {
            int cur = colors[i % n];
            if (cur == last) {
                cnt = 1;                 // start new segment from current tile
            } else {
                cnt++;
                if (cnt >= k) result++; // each additional tile creates a new valid group
            }
            last = cur;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} colors
 * @param {number} k
 * @return {number}
 */
var numberOfAlternatingGroups = function(colors, k) {
    const n = colors.length;
    let result = 0;
    let cnt = 1; // length of current alternating segment
    let last = colors[0];
    
    // iterate through the array plus first (k-1) elements to handle wrap‑around
    for (let i = 1; i < n + k - 1; ++i) {
        const idx = i % n;
        if (colors[idx] === last) {
            cnt = 1; // reset when pattern breaks
        } else {
            cnt++;
            if (cnt >= k) result++;
        }
        last = colors[idx];
    }
    
    return result;
};
```

## Typescript

```typescript
function numberOfAlternatingGroups(colors: number[], k: number): number {
    const n = colors.length;
    let result = 0;
    let cnt = 1; // length of current alternating segment
    let last = colors[0];
    // iterate through the array plus first (k-1) elements to handle wrap‑around windows
    for (let i = 1; i < n + k - 1; ++i) {
        const cur = colors[i % n];
        if (cur === last) {
            cnt = 1;
        } else {
            cnt++;
            if (cnt >= k) result++;
        }
        last = cur;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @param Integer $k
     * @return Integer
     */
    function numberOfAlternatingGroups($colors, $k) {
        $n = count($colors);
        if ($n == 0) return 0;

        $result = 0;
        $cnt = 1; // length of current alternating segment
        $last = $colors[0];

        // iterate through the array plus first k-1 elements to handle wrap‑around
        for ($i = 1; $i < $n + $k - 1; $i++) {
            $idx = $i % $n;
            if ($colors[$idx] == $last) {
                $cnt = 1; // reset count when pattern breaks
            } else {
                $cnt++;
                if ($cnt >= $k) {
                    $result++;
                }
            }
            $last = $colors[$idx];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ k: Int) -> Int {
        let n = colors.count
        if n == 0 { return 0 }
        var result = 0
        var count = 1               // length of current alternating segment
        var last = colors[0]
        let total = n + k - 1       // iterate enough to cover wrap‑around windows
        
        for i in 1..<total {
            let idx = i % n
            let cur = colors[idx]
            if cur == last {
                count = 1           // start new segment from current tile
            } else {
                count += 1
            }
            if count >= k {
                result += 1
            }
            last = cur
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        val n = colors.size
        var result = 0
        var cnt = 1
        var last = colors[0]
        val total = n + k - 1
        for (i in 1 until total) {
            val idx = i % n
            if (colors[idx] == last) {
                cnt = 1
            } else {
                cnt++
                if (cnt >= k) result++
            }
            last = colors[idx]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int numberOfAlternatingGroups(List<int> colors, int k) {
    int n = colors.length;
    int result = 0;
    int cnt = 1;
    int last = colors[0];
    int total = n + k - 1; // iterate enough to cover all circular windows
    for (int i = 1; i < total; ++i) {
      int cur = colors[i % n];
      if (cur == last) {
        cnt = 1;
      } else {
        cnt += 1;
        if (cnt >= k) result++;
      }
      last = cur;
    }
    return result;
  }
}
```

## Golang

```go
func numberOfAlternatingGroups(colors []int, k int) int {
	n := len(colors)
	if n == 0 || k > n {
		return 0
	}
	result := 0
	cnt := 1
	last := colors[0]

	for i := 1; i < n+k-1; i++ {
		idx := i % n
		if colors[idx] == last {
			cnt = 1
		} else {
			cnt++
			if cnt >= k {
				result++
			}
		}
		last = colors[idx]
	}
	return result
}
```

## Ruby

```ruby
def number_of_alternating_groups(colors, k)
  n = colors.length
  return 0 if n < k

  result = 0
  cnt = 1
  last = colors[0]

  total_steps = n + k - 2
  (1..total_steps).each do |i|
    cur = colors[i % n]
    if cur == last
      cnt = 1
    else
      cnt += 1
      result += 1 if cnt >= k
    end
    last = cur
  end

  result
end
```

## Scala

```scala
object Solution {
    def numberOfAlternatingGroups(colors: Array[Int], k: Int): Int = {
        val n = colors.length
        var result = 0
        var cnt = 1
        var last = colors(0)
        // iterate over the extended sequence to handle circular wrap
        for (i <- 1 to n + k - 2) {
            val idx = i % n
            if (colors(idx) == last) {
                cnt = 1
                last = colors(idx)
            } else {
                cnt += 1
                if (cnt >= k) result += 1
                last = colors(idx)
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let n = colors.len();
        if n == 0 {
            return 0;
        }
        let k_usize = k as usize;
        // count alternating runs
        let mut ans: i32 = 0;
        let mut cnt: usize = 1; // length of current alternating segment
        let mut last = colors[0];
        // iterate over the array plus first (k-1) elements to handle wrap‑around
        for i in 1..(n + k_usize - 1) {
            let idx = i % n;
            if colors[idx] == last {
                cnt = 1;
            } else {
                cnt += 1;
            }
            if cnt >= k_usize {
                ans += 1;
            }
            last = colors[idx];
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-alternating-groups colors k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length colors))
         (vec (list->vector colors)))
    (if (< n k)
        0
        (let loop ((i 1)               ; current step index
                   (cnt 1)             ; length of current alternating run
                   (last (vector-ref vec 0)) ; previous color
                   (res 0))            ; result count
          (if (> i (- (+ n k) 2))
              res
              (let* ((idx (modulo i n))
                     (cur (vector-ref vec idx)))
                (if (= cur last)
                    (loop (+ i 1) 1 cur res)
                    (let ((newcnt (+ cnt 1))
                          (newres (if (>= newcnt k) (+ res 1) res)))
                      (loop (+ i 1) newcnt cur newres)))))))))
```

## Erlang

```erlang
-spec number_of_alternating_groups([integer()], integer()) -> integer().
number_of_alternating_groups(Colors, K) ->
    Tuple = list_to_tuple(Colors),
    N = tuple_size(Tuple),
    case N of
        0 -> 0;
        _ ->
            First = element(1, Tuple),
            loop(1, N, K, Tuple, First, 1, 0)
    end.

loop(I, N, K, Tuple, Last, Count, Res) when I =< N + K - 1 ->
    Index = ((I - 1) rem N) + 1,
    Cur = element(Index, Tuple),
    NewCount = if Cur == Last -> 1; true -> Count + 1 end,
    NewRes = if NewCount >= K -> Res + 1; true -> Res end,
    loop(I + 1, N, K, Tuple, Cur, NewCount, NewRes);
loop(_, _, _, _, _, _, Res) ->
    Res.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer], k :: integer) :: integer
  def number_of_alternating_groups(colors, k) do
    extended = colors ++ Enum.take(colors, k - 1)

    case extended do
      [] -> 0
      [first | rest] ->
        {result, _, _} =
          Enum.reduce(rest, {0, 1, first}, fn cur, {res, cnt, prev} ->
            if cur == prev do
              {res, 1, cur}
            else
              new_cnt = cnt + 1
              new_res = if new_cnt >= k, do: res + 1, else: res
              {new_res, new_cnt, cur}
            end
          end)

        result
    end
  end
end
```
