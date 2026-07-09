# 0868. Binary Gap

## Cpp

```cpp
class Solution {
public:
    int binaryGap(int n) {
        int last = -1;
        int maxDist = 0;
        for (int i = 0; n > 0; ++i) {
            if (n & 1) {
                if (last != -1) {
                    maxDist = std::max(maxDist, i - last);
                }
                last = i;
            }
            n >>= 1;
        }
        return maxDist;
    }
};
```

## Java

```java
class Solution {
    public int binaryGap(int n) {
        int last = -1;
        int maxDist = 0;
        int index = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if (last != -1) {
                    maxDist = Math.max(maxDist, index - last);
                }
                last = index;
            }
            n >>= 1;
            index++;
        }
        return maxDist;
    }
}
```

## Python

```python
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = -1
        max_dist = 0
        i = 0
        while n:
            if n & 1:
                if last != -1:
                    max_dist = max(max_dist, i - last)
                last = i
            n >>= 1
            i += 1
        return max_dist
```

## Python3

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        max_dist = 0
        i = 0
        while n:
            if n & 1:
                if last != -1:
                    max_dist = max(max_dist, i - last)
                last = i
            n >>= 1
            i += 1
        return max_dist
```

## C

```c
int binaryGap(int n) {
    int lastPos = -1;
    int maxDist = 0;
    int pos = 0;
    while (n > 0) {
        if (n & 1) {
            if (lastPos != -1) {
                int dist = pos - lastPos;
                if (dist > maxDist) maxDist = dist;
            }
            lastPos = pos;
        }
        n >>= 1;
        ++pos;
    }
    return maxDist;
}
```

## Csharp

```csharp
public class Solution {
    public int BinaryGap(int n) {
        int maxDist = 0;
        int lastPos = -1;
        int position = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if (lastPos != -1) {
                    int dist = position - lastPos;
                    if (dist > maxDist) maxDist = dist;
                }
                lastPos = position;
            }
            n >>= 1;
            position++;
        }
        return maxDist;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    let last = -1;
    let maxDist = 0;
    let pos = 0;
    while (n > 0) {
        if ((n & 1) === 1) {
            if (last !== -1) {
                const dist = pos - last;
                if (dist > maxDist) maxDist = dist;
            }
            last = pos;
        }
        n >>= 1;
        pos++;
    }
    return maxDist;
};
```

## Typescript

```typescript
function binaryGap(n: number): number {
    let last = -1;
    let maxDist = 0;
    let pos = 0;
    while (n > 0) {
        if ((n & 1) === 1) {
            if (last !== -1) {
                const dist = pos - last;
                if (dist > maxDist) maxDist = dist;
            }
            last = pos;
        }
        n >>= 1;
        pos++;
    }
    return maxDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function binaryGap($n) {
        $last = -1;
        $maxDist = 0;
        $pos = 0;
        while ($n > 0) {
            if ($n & 1) {
                if ($last != -1) {
                    $dist = $pos - $last;
                    if ($dist > $maxDist) {
                        $maxDist = $dist;
                    }
                }
                $last = $pos;
            }
            $n >>= 1;
            $pos++;
        }
        return $maxDist;
    }
}
```

## Swift

```swift
class Solution {
    func binaryGap(_ n: Int) -> Int {
        var num = n
        var position = 0
        var lastOnePos = -1
        var maxDist = 0
        
        while num > 0 {
            if (num & 1) == 1 {
                if lastOnePos != -1 {
                    let dist = position - lastOnePos
                    if dist > maxDist {
                        maxDist = dist
                    }
                }
                lastOnePos = position
            }
            position += 1
            num >>= 1
        }
        
        return maxDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun binaryGap(n: Int): Int {
        var num = n
        var pos = 0
        var last = -1
        var maxDist = 0
        while (num > 0) {
            if ((num and 1) == 1) {
                if (last != -1) {
                    val dist = pos - last
                    if (dist > maxDist) maxDist = dist
                }
                last = pos
            }
            pos++
            num = num shr 1
        }
        return maxDist
    }
}
```

## Dart

```dart
class Solution {
  int binaryGap(int n) {
    int last = -1;
    int maxDist = 0;
    int pos = 0;
    while (n > 0) {
      if ((n & 1) == 1) {
        if (last != -1) {
          int dist = pos - last;
          if (dist > maxDist) maxDist = dist;
        }
        last = pos;
      }
      n >>= 1;
      pos++;
    }
    return maxDist;
  }
}
```

## Golang

```go
func binaryGap(n int) int {
    lastPos := -1
    maxDist := 0
    pos := 0
    for n > 0 {
        if n&1 == 1 {
            if lastPos != -1 {
                if d := pos - lastPos; d > maxDist {
                    maxDist = d
                }
            }
            lastPos = pos
        }
        n >>= 1
        pos++
    }
    return maxDist
}
```

## Ruby

```ruby
def binary_gap(n)
  last = nil
  max_dist = 0
  pos = 0
  while n > 0
    if (n & 1) == 1
      unless last.nil?
        dist = pos - last
        max_dist = dist if dist > max_dist
      end
      last = pos
    end
    n >>= 1
    pos += 1
  end
  max_dist
end
```

## Scala

```scala
object Solution {
    def binaryGap(n: Int): Int = {
        var last = -1
        var maxDist = 0
        var pos = 0
        var num = n
        while (num > 0) {
            if ((num & 1) == 1) {
                if (last != -1) {
                    val dist = pos - last
                    if (dist > maxDist) maxDist = dist
                }
                last = pos
            }
            pos += 1
            num >>= 1
        }
        maxDist
    }
}
```

## Rust

```rust
impl Solution {
    pub fn binary_gap(n: i32) -> i32 {
        let mut num = n as u32;
        let mut last: Option<i32> = None;
        let mut max_gap = 0;
        let mut pos: i32 = 0;
        while num > 0 {
            if (num & 1) == 1 {
                if let Some(prev) = last {
                    let gap = pos - prev;
                    if gap > max_gap {
                        max_gap = gap;
                    }
                }
                last = Some(pos);
            }
            num >>= 1;
            pos += 1;
        }
        max_gap
    }
}
```

## Racket

```racket
(define/contract (binary-gap n)
  (-> exact-integer? exact-integer?)
  (let loop ((i 0) (x n) (last -1) (best 0))
    (if (= x 0)
        best
        (let ((bit (bitwise-and x 1)))
          (if (= bit 1)
              (if (>= last 0)
                  (let ((dist (- i last)))
                    (loop (+ i 1) (arithmetic-shift x -1) i (max best dist)))
                  (loop (+ i 1) (arithmetic-shift x -1) i best))
              (loop (+ i 1) (arithmetic-shift x -1) last best))))))
```

## Erlang

```erlang
-spec binary_gap(N :: integer()) -> integer().
binary_gap(N) when N > 0 ->
    binary_gap(N, 0, -1, 0).

binary_gap(0, _Idx, _Last, Max) ->
    Max;
binary_gap(Rem, Idx, Last, Max) ->
    case Rem band 1 of
        1 ->
            NewMax = if Last >= 0 -> erlang:max(Max, Idx - Last); true -> Max end,
            binary_gap(Rem bsr 1, Idx + 1, Idx, NewMax);
        0 ->
            binary_gap(Rem bsr 1, Idx + 1, Last, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec binary_gap(n :: integer) :: integer
  def binary_gap(n) do
    do_binary_gap(n, 0, nil, 0)
  end

  defp do_binary_gap(0, _pos, _last, max), do: max

  defp do_binary_gap(num, pos, last, max) do
    if (num &&& 1) == 1 do
      case last do
        nil ->
          do_binary_gap(num >>> 1, pos + 1, pos, max)

        prev ->
          gap = pos - prev
          new_max = if gap > max, do: gap, else: max
          do_binary_gap(num >>> 1, pos + 1, pos, new_max)
      end
    else
      do_binary_gap(num >>> 1, pos + 1, last, max)
    end
  end
end
```
