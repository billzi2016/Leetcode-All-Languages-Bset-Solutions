# 1860. Incremental Memory Leak

## Cpp

```cpp
class Solution {
public:
    vector<int> memLeak(int memory1, int memory2) {
        int i = 1;
        while (true) {
            if (max(memory1, memory2) < i) break;
            if (memory1 >= memory2) {
                memory1 -= i;
            } else {
                memory2 -= i;
            }
            ++i;
        }
        return {i, memory1, memory2};
    }
};
```

## Java

```java
class Solution {
    public int[] memLeak(int memory1, int memory2) {
        int i = 1;
        while (true) {
            if (Math.max(memory1, memory2) < i) break;
            if (memory1 >= memory2) {
                memory1 -= i;
            } else {
                memory2 -= i;
            }
            i++;
        }
        return new int[]{i, memory1, memory2};
    }
}
```

## Python

```python
class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        i = 1
        while True:
            # check if any stick can accommodate i bits
            if max(memory1, memory2) < i:
                return [i, memory1, memory2]
            # allocate to the stick with more available memory,
            # or to memory1 if they are equal
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
```

## Python3

```python
from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while True:
            if max(memory1, memory2) < i:
                break
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* memLeak(int memory1, int memory2, int* returnSize) {
    long long i = 1;
    while (1) {
        if (memory1 >= memory2) {
            if ((long long)memory1 < i) break;
            memory1 -= (int)i;
        } else {
            if ((long long)memory2 < i) break;
            memory2 -= (int)i;
        }
        ++i;
    }
    int* res = (int*)malloc(3 * sizeof(int));
    res[0] = (int)i;          // crash time
    res[1] = memory1;
    res[2] = memory2;
    *returnSize = 3;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MemLeak(int memory1, int memory2) {
        int time = 1;
        while (true) {
            if (memory1 < time && memory2 < time) break;
            if (memory1 >= memory2) {
                memory1 -= time;
            } else {
                memory2 -= time;
            }
            time++;
        }
        return new int[] { time, memory1, memory2 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} memory1
 * @param {number} memory2
 * @return {number[]}
 */
var memLeak = function(memory1, memory2) {
    let t = 1;
    while (true) {
        if (memory1 >= memory2) {
            if (memory1 < t) break;
            memory1 -= t;
        } else {
            if (memory2 < t) break;
            memory2 -= t;
        }
        t++;
    }
    return [t, memory1, memory2];
};
```

## Typescript

```typescript
function memLeak(memory1: number, memory2: number): number[] {
    let time = 1;
    while (true) {
        if (memory1 >= memory2) {
            if (memory1 < time) break;
            memory1 -= time;
        } else {
            if (memory2 < time) break;
            memory2 -= time;
        }
        time++;
    }
    return [time, memory1, memory2];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $memory1
     * @param Integer $memory2
     * @return Integer[]
     */
    function memLeak($memory1, $memory2) {
        $i = 1;
        while (true) {
            if ($memory1 >= $memory2) { // tie goes to memory1
                if ($memory1 < $i) break;
                $memory1 -= $i;
            } else {
                if ($memory2 < $i) break;
                $memory2 -= $i;
            }
            $i++;
        }
        return [$i, $memory1, $memory2];
    }
}
```

## Swift

```swift
class Solution {
    func memLeak(_ memory1: Int, _ memory2: Int) -> [Int] {
        var m1 = memory1
        var m2 = memory2
        var time = 1
        while true {
            if max(m1, m2) < time {
                return [time, m1, m2]
            }
            if m1 >= m2 {
                m1 -= time
            } else {
                m2 -= time
            }
            time += 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun memLeak(memory1: Int, memory2: Int): IntArray {
        var m1 = memory1
        var m2 = memory2
        var i = 1
        while (true) {
            if (m1 >= m2) {
                if (m1 < i) break
                m1 -= i
            } else {
                if (m2 < i) break
                m2 -= i
            }
            i++
        }
        return intArrayOf(i, m1, m2)
    }
}
```

## Dart

```dart
class Solution {
  List<int> memLeak(int memory1, int memory2) {
    int i = 1;
    while (true) {
      if (memory1 < i && memory2 < i) break;
      if (memory1 >= memory2) {
        memory1 -= i;
      } else {
        memory2 -= i;
      }
      i++;
    }
    return [i, memory1, memory2];
  }
}
```

## Golang

```go
func memLeak(memory1 int, memory2 int) []int {
    m1, m2 := memory1, memory2
    for i := 1; ; i++ {
        // decide which stick to allocate to
        if m1 >= m2 { // choose first when equal or greater
            if m1 < i {
                return []int{i, m1, m2}
            }
            m1 -= i
        } else {
            if m2 < i {
                return []int{i, m1, m2}
            }
            m2 -= i
        }
    }
}
```

## Ruby

```ruby
def mem_leak(memory1, memory2)
  i = 1
  loop do
    if memory1 >= memory2
      return [i, memory1, memory2] if memory1 < i
      memory1 -= i
    else
      return [i, memory1, memory2] if memory2 < i
      memory2 -= i
    end
    i += 1
  end
end
```

## Scala

```scala
object Solution {
    def memLeak(memory1: Int, memory2: Int): Array[Int] = {
        var m1 = memory1.toLong
        var m2 = memory2.toLong
        var t = 0L
        while (true) {
            t += 1
            if (m1 >= m2) {
                if (m1 < t) return Array(t.toInt, m1.toInt, m2.toInt)
                m1 -= t
            } else {
                if (m2 < t) return Array(t.toInt, m1.toInt, m2.toInt)
                m2 -= t
            }
        }
        Array()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn mem_leak(memory1: i32, memory2: i32) -> Vec<i32> {
        let mut m1 = memory1 as i64;
        let mut m2 = memory2 as i64;
        let mut t: i64 = 1;
        loop {
            if m1 >= m2 {
                if m1 < t { break; }
                m1 -= t;
            } else {
                if m2 < t { break; }
                m2 -= t;
            }
            t += 1;
        }
        vec![t as i32, m1 as i32, m2 as i32]
    }
}
```

## Racket

```racket
(define/contract (mem-leak memory1 memory2)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let loop ((m1 memory1) (m2 memory2) (i 1))
    (if (< (max m1 m2) i)
        (list i m1 m2)
        (if (>= m1 m2)
            (loop (- m1 i) m2 (+ i 1))
            (loop m1 (- m2 i) (+ i 1))))))
```

## Erlang

```erlang
-module(solution).
-export([mem_leak/2]).

-spec mem_leak(Memory1 :: integer(), Memory2 :: integer()) -> [integer()].
mem_leak(Memory1, Memory2) ->
    loop(1, Memory1, Memory2).

loop(I, M1, M2) when M1 >= M2 ->
    case M1 < I of
        true -> [I, M1, M2];
        false -> loop(I + 1, M1 - I, M2)
    end;
loop(I, M1, M2) ->
    case M2 < I of
        true -> [I, M1, M2];
        false -> loop(I + 1, M1, M2 - I)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec mem_leak(memory1 :: integer, memory2 :: integer) :: [integer]
  def mem_leak(memory1, memory2) do
    leak(memory1, memory2, 1)
  end

  defp leak(m1, m2, i) do
    cond do
      m1 >= m2 ->
        if m1 < i do
          [i, m1, m2]
        else
          leak(m1 - i, m2, i + 1)
        end

      true ->
        if m2 < i do
          [i, m1, m2]
        else
          leak(m1, m2 - i, i + 1)
        end
    end
  end
end
```
