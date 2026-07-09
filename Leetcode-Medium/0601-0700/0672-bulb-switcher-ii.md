# 0672. Bulb Switcher II

## Cpp

```cpp
class Solution {
public:
    int flipLights(int n, int presses) {
        n = std::min(n, 3);
        if (presses == 0) return 1;
        if (presses == 1) {
            if (n == 1) return 2;
            if (n == 2) return 3;
            return 4; // n == 3
        }
        if (presses == 2) {
            if (n == 1) return 2;
            if (n == 2) return 4;
            return 7; // n == 3
        }
        // presses >= 3
        if (n == 1) return 2;
        if (n == 2) return 4;
        return 8; // n == 3
    }
};
```

## Java

```java
class Solution {
    public int flipLights(int n, int presses) {
        if (presses == 0) return 1;
        n = Math.min(n, 3);
        if (presses == 1) {
            if (n == 1) return 2;
            if (n == 2) return 3;
            return 4;
        }
        if (presses == 2) {
            if (n == 1) return 2;
            if (n == 2) return 4;
            return 7;
        }
        // presses >= 3
        if (n == 1) return 2;
        if (n == 2) return 4;
        return 8;
    }
}
```

## Python

```python
class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        # n >= 3
        if presses == 1:
            return 4
        elif presses == 2:
            return 7
        else:
            return 8
```

## Python3

```python
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)
        if presses == 0:
            return 1
        if presses == 1:
            if n == 1:
                return 2
            if n == 2:
                return 3
            return 4
        if presses == 2:
            if n == 1:
                return 2
            if n == 2:
                return 4
            return 7
        # presses >= 3
        if n == 1:
            return 2
        if n == 2:
            return 4
        return 8
```

## C

```c
int flipLights(int n, int presses) {
    if (presses == 0) return 1;
    n = n > 3 ? 3 : n; // limit to first three bulbs
    if (presses == 1) {
        if (n == 1) return 2;
        if (n == 2) return 3;
        return 4;
    }
    if (presses == 2) {
        if (n == 1) return 2;
        if (n == 2) return 4;
        return 7;
    }
    // presses >= 3
    if (n == 1) return 2;
    if (n == 2) return 4;
    return 8;
}
```

## Csharp

```csharp
public class Solution {
    public int FlipLights(int n, int presses) {
        if (presses == 0) return 1;
        n = Math.Min(n, 3);
        if (presses == 1) {
            if (n == 1) return 2;
            if (n == 2) return 3;
            return 4;
        }
        if (presses == 2) {
            if (n == 1) return 2;
            if (n == 2) return 4;
            return 7;
        }
        // presses >= 3
        if (n == 1) return 2;
        if (n == 2) return 4;
        return 8;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} presses
 * @return {number}
 */
var flipLights = function(n, presses) {
    if (presses === 0) return 1;
    n = Math.min(n, 3);
    if (n === 1) {
        // With at least one press we can toggle the single bulb on or off.
        return 2;
    }
    if (n === 2) {
        // presses == 1 gives 3 states, otherwise 4 states.
        return presses === 1 ? 3 : 4;
    }
    // n >= 3
    if (presses === 1) return 4;
    if (presses === 2) return 7;
    return 8;
};
```

## Typescript

```typescript
function flipLights(n: number, presses: number): number {
    if (presses === 0) return 1;
    n = Math.min(n, 3);
    if (presses === 1) {
        if (n === 1) return 2;
        if (n === 2) return 3;
        return 4;
    }
    if (presses === 2) {
        if (n === 1) return 2;
        if (n === 2) return 4;
        return 7;
    }
    // presses >= 3
    if (n === 1) return 2;
    if (n === 2) return 4;
    return 8;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $presses
     * @return Integer
     */
    function flipLights($n, $presses) {
        // Reduce n to at most 3 because pattern repeats every 6 lights,
        // and the first 3 lights determine all others.
        $n = min($n, 3);
        
        if ($presses == 0) {
            return 1;
        }
        
        if ($presses == 1) {
            if ($n == 1) return 2;
            if ($n == 2) return 3;
            return 4; // n == 3
        }
        
        if ($presses == 2) {
            if ($n == 1) return 2;
            if ($n == 2) return 4;
            return 7; // n == 3
        }
        
        // presses >= 3
        if ($n == 1) return 2;
        if ($n == 2) return 4;
        return 8; // n == 3
    }
}
```

## Swift

```swift
class Solution {
    func flipLights(_ n: Int, _ presses: Int) -> Int {
        let m = min(n, 3)
        if presses == 0 {
            return 1
        } else if presses == 1 {
            switch m {
            case 1:
                return 2
            case 2:
                return 3
            default:
                return 4
            }
        } else if presses == 2 {
            switch m {
            case 1:
                return 2
            case 2:
                return 4
            default:
                return 7
            }
        } else { // presses >= 3
            switch m {
            case 1:
                return 2
            case 2:
                return 4
            default:
                return 8
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun flipLights(n: Int, presses: Int): Int {
        val nn = minOf(n, 3)
        if (presses == 0) return 1
        if (presses == 1) {
            return when (nn) {
                1 -> 2
                2 -> 3
                else -> 4
            }
        }
        if (presses == 2) {
            return when (nn) {
                1 -> 2
                2 -> 4
                else -> 7
            }
        }
        // presses >= 3
        return when (nn) {
            1 -> 2
            2 -> 4
            else -> 8
        }
    }
}
```

## Dart

```dart
class Solution {
  int flipLights(int n, int presses) {
    if (presses == 0) return 1;
    n = n > 3 ? 3 : n;
    if (presses == 1) {
      if (n == 1) return 2;
      if (n == 2) return 3;
      return 4; // n == 3
    }
    if (presses == 2) {
      if (n == 1) return 2;
      if (n == 2) return 4;
      return 7; // n == 3
    }
    // presses >= 3
    if (n == 1) return 2;
    if (n == 2) return 4;
    return 8; // n == 3
  }
}
```

## Golang

```go
func flipLights(n int, presses int) int {
	if presses == 0 {
		return 1
	}
	if n == 1 {
		return 2
	}
	if n == 2 {
		if presses == 1 {
			return 3
		}
		return 4
	}
	// n >= 3
	if presses == 1 {
		return 4
	} else if presses == 2 {
		return 7
	}
	return 8
}
```

## Ruby

```ruby
def flip_lights(n, presses)
  return 1 if presses == 0
  n = [n, 3].min
  case n
  when 1
    2
  when 2
    presses == 1 ? 3 : 4
  else
    case presses
    when 1
      4
    when 2
      7
    else
      8
    end
  end
end
```

## Scala

```scala
object Solution {
  def flipLights(n: Int, presses: Int): Int = {
    val nn = math.min(n, 3)
    if (presses == 0) {
      1
    } else if (presses == 1) {
      nn match {
        case 1 => 2
        case 2 => 3
        case _ => 4
      }
    } else if (presses == 2) {
      nn match {
        case 1 => 2
        case 2 => 4
        case _ => 7
      }
    } else { // presses >= 3
      nn match {
        case 1 => 2
        case 2 => 4
        case _ => 8
      }
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn flip_lights(n: i32, presses: i32) -> i32 {
        let n = std::cmp::min(n, 3);
        match presses {
            0 => 1,
            1 => match n {
                1 => 2,
                2 => 3,
                _ => 4,
            },
            2 => match n {
                1 => 2,
                2 => 4,
                _ => 7,
            },
            _ => match n {
                1 => 2,
                2 => 4,
                _ => 8,
            },
        }
    }
}
```

## Racket

```racket
(define/contract (flip-lights n presses)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ((n (min n 3)))
    (cond
      [(zero? presses) 1]
      [(= presses 1)
       (cond [(= n 1) 2]
             [(= n 2) 3]
             [else 4])]
      [(= presses 2)
       (cond [(= n 1) 2]
             [(= n 2) 4]
             [else 7])]
      [else ; presses >= 3
       (cond [(= n 1) 2]
             [(= n 2) 4]
             [else 8])])))
```

## Erlang

```erlang
-module(solution).
-export([flip_lights/2]).
-spec flip_lights(N :: integer(), Presses :: integer()) -> integer().
flip_lights(N, Presses) ->
    N1 = erlang:min(N, 3),
    M0 = erlang:min(Presses, 3),
    case {N1, M0} of
        {_, 0} -> 1;
        {1, _} -> 2;
        {2, 1} -> 3;
        {2, _} -> 4;
        {3, 1} -> 4;
        {3, 2} -> 7;
        {3, _} -> 8
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec flip_lights(n :: integer, presses :: integer) :: integer
  def flip_lights(n, presses) do
    n = min(n, 3)

    case presses do
      0 ->
        1

      1 ->
        case n do
          1 -> 2
          2 -> 3
          _ -> 4
        end

      2 ->
        case n do
          1 -> 2
          2 -> 4
          _ -> 7
        end

      _ ->
        case n do
          1 -> 2
          2 -> 4
          _ -> 8
        end
    end
  end
end
```
