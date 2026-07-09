# 3200. Maximum Height of a Triangle

## Cpp

```cpp
class Solution {
public:
    int maxHeightOfTriangle(int red, int blue) {
        auto simulate = [&](bool startRed) -> int {
            int r = red, b = blue;
            int height = 0;
            for (int i = 1; ; ++i) {
                bool needRed = (i % 2 == 1) ? startRed : !startRed;
                if (needRed) {
                    if (r < i) break;
                    r -= i;
                } else {
                    if (b < i) break;
                    b -= i;
                }
                ++height;
            }
            return height;
        };
        int ans1 = simulate(true);   // red on top
        int ans2 = simulate(false);  // blue on top
        return max(ans1, ans2);
    }
};
```

## Java

```java
class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        return Math.max(simulate(red, blue, true), simulate(red, blue, false));
    }
    
    private int simulate(int red, int blue, boolean startRed) {
        int level = 1;
        boolean needRed = startRed;
        while (true) {
            if (needRed) {
                if (red >= level) {
                    red -= level;
                } else {
                    break;
                }
            } else {
                if (blue >= level) {
                    blue -= level;
                } else {
                    break;
                }
            }
            needRed = !needRed;
            level++;
        }
        return level - 1;
    }
}
```

## Python

```python
class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def height(start_red):
            r, b = red, blue
            cur_is_red = start_red
            h = 0
            need = 1
            while True:
                if cur_is_red:
                    if r < need:
                        break
                    r -= need
                else:
                    if b < need:
                        break
                    b -= need
                h += 1
                need += 1
                cur_is_red = not cur_is_red
            return h

        return max(height(True), height(False))
```

## Python3

```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def simulate(start_red: bool) -> int:
            r, b = red, blue
            need = 1
            height = 0
            cur_is_red = start_red
            while True:
                if cur_is_red:
                    if r < need:
                        break
                    r -= need
                else:
                    if b < need:
                        break
                    b -= need
                height += 1
                need += 1
                cur_is_red = not cur_is_red
            return height

        return max(simulate(True), simulate(False))
```

## C

```c
int simulate(int red, int blue, int startRed) {
    int r = red, b = blue;
    int height = 0;
    int need = 1;
    int curRed = startRed; // 1 if current row should be red, 0 for blue
    while (1) {
        if (curRed) {
            if (r < need) break;
            r -= need;
        } else {
            if (b < need) break;
            b -= need;
        }
        height++;
        need++;
        curRed = !curRed;
    }
    return height;
}

int maxHeightOfTriangle(int red, int blue) {
    int h1 = simulate(red, blue, 1); // start with red
    int h2 = simulate(red, blue, 0); // start with blue
    return h1 > h2 ? h1 : h2;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxHeightOfTriangle(int red, int blue) {
        return Math.Max(Simulate(red, blue, true), Simulate(red, blue, false));
    }

    private int Simulate(int red, int blue, bool startWithRed) {
        int height = 0;
        bool needRed = startWithRed;
        for (int level = 1; ; level++) {
            if (needRed) {
                if (red < level) break;
                red -= level;
            } else {
                if (blue < level) break;
                blue -= level;
            }
            height++;
            needRed = !needRed;
        }
        return height;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} red
 * @param {number} blue
 * @return {number}
 */
var maxHeightOfTriangle = function(red, blue) {
    const heightIfStart = (startRed) => {
        let r = red, b = blue;
        let need = 1;
        let curRed = startRed;
        let h = 0;
        while (true) {
            if (curRed) {
                if (r < need) break;
                r -= need;
            } else {
                if (b < need) break;
                b -= need;
            }
            h++;
            need++;
            curRed = !curRed;
        }
        return h;
    };
    return Math.max(heightIfStart(true), heightIfStart(false));
};
```

## Typescript

```typescript
function maxHeightOfTriangle(red: number, blue: number): number {
    const simulate = (startWithRed: boolean): number => {
        let r = red, b = blue;
        let need = 1;
        let rows = 0;
        let isRed = startWithRed;
        while (true) {
            if (isRed) {
                if (r < need) break;
                r -= need;
            } else {
                if (b < need) break;
                b -= need;
            }
            rows++;
            need++;
            isRed = !isRed;
        }
        return rows;
    };
    return Math.max(simulate(true), simulate(false));
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $red
     * @param Integer $blue
     * @return Integer
     */
    function maxHeightOfTriangle($red, $blue) {
        $maxHeight = 0;
        foreach (['red', 'blue'] as $startColor) {
            $r = $red;
            $b = $blue;
            $height = 0;
            $need = 1;
            $color = $startColor;
            while (true) {
                if ($color === 'red') {
                    if ($r < $need) break;
                    $r -= $need;
                } else {
                    if ($b < $need) break;
                    $b -= $need;
                }
                $height++;
                $need++;
                $color = ($color === 'red') ? 'blue' : 'red';
            }
            if ($height > $maxHeight) {
                $maxHeight = $height;
            }
        }
        return $maxHeight;
    }
}
```

## Swift

```swift
class Solution {
    func maxHeightOfTriangle(_ red: Int, _ blue: Int) -> Int {
        func compute(startRedTop: Bool) -> Int {
            var r = red
            var b = blue
            var need = 1
            var isRed = startRedTop
            var height = 0
            while true {
                if isRed {
                    if r >= need {
                        r -= need
                    } else { break }
                } else {
                    if b >= need {
                        b -= need
                    } else { break }
                }
                height += 1
                need += 1
                isRed.toggle()
            }
            return height
        }
        let h1 = compute(startRedTop: true)
        let h2 = compute(startRedTop: false)
        return max(h1, h2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxHeightOfTriangle(red: Int, blue: Int): Int {
        fun simulate(startRed: Boolean): Int {
            var r = red
            var b = blue
            var height = 0
            var level = 1
            var needRed = startRed
            while (true) {
                if (needRed) {
                    if (r >= level) {
                        r -= level
                    } else break
                } else {
                    if (b >= level) {
                        b -= level
                    } else break
                }
                height++
                level++
                needRed = !needRed
            }
            return height
        }
        val h1 = simulate(true)
        val h2 = simulate(false)
        return maxOf(h1, h2)
    }
}
```

## Dart

```dart
class Solution {
  int maxHeightOfTriangle(int red, int blue) {
    int simulate(bool startWithRed) {
      int r = red;
      int b = blue;
      int height = 0;
      int need = 1;
      bool useRed = startWithRed;
      while (true) {
        if (useRed) {
          if (r < need) break;
          r -= need;
        } else {
          if (b < need) break;
          b -= need;
        }
        height++;
        need++;
        useRed = !useRed;
      }
      return height;
    }

    int h1 = simulate(true);
    int h2 = simulate(false);
    return h1 > h2 ? h1 : h2;
  }
}
```

## Golang

```go
func maxHeightOfTriangle(red int, blue int) int {
	calc := func(startRed bool) int {
		r, b := red, blue
		height, need := 0, 1
		curRed := startRed
		for {
			if curRed {
				if r < need {
					break
				}
				r -= need
			} else {
				if b < need {
					break
				}
				b -= need
			}
			height++
			need++
			curRed = !curRed
		}
		return height
	}
	h1 := calc(true)
	h2 := calc(false)
	if h1 > h2 {
		return h1
	}
	return h2
}
```

## Ruby

```ruby
def max_height_of_triangle(red, blue)
  max_h = 0

  # start with red on top
  r = red
  b = blue
  h = 0
  i = 1
  loop do
    need = i
    if i.odd?
      break if r < need
      r -= need
    else
      break if b < need
      b -= need
    end
    h += 1
    i += 1
  end
  max_h = h

  # start with blue on top
  r = red
  b = blue
  h = 0
  i = 1
  loop do
    need = i
    if i.odd?
      break if b < need
      b -= need
    else
      break if r < need
      r -= need
    end
    h += 1
    i += 1
  end
  max_h = [max_h, h].max

  max_h
end
```

## Scala

```scala
object Solution {
    def maxHeightOfTriangle(red: Int, blue: Int): Int = {
        def simulate(startRed: Boolean): Int = {
            var r = red
            var b = blue
            var level = 1
            var height = 0
            var curIsRed = startRed
            while (true) {
                if (curIsRed) {
                    if (r >= level) {
                        r -= level
                        height += 1
                        level += 1
                        curIsRed = !curIsRed
                    } else return height
                } else {
                    if (b >= level) {
                        b -= level
                        height += 1
                        level += 1
                        curIsRed = !curIsRed
                    } else return height
                }
            }
            height
        }
        math.max(simulate(true), simulate(false))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_height_of_triangle(red: i32, blue: i32) -> i32 {
        fn simulate(mut r: i32, mut b: i32, start_red: bool) -> i32 {
            let mut height = 0;
            let mut need = 1;
            let mut cur_is_red = start_red;
            loop {
                if cur_is_red {
                    if r < need { break; }
                    r -= need;
                } else {
                    if b < need { break; }
                    b -= need;
                }
                height += 1;
                need += 1;
                cur_is_red = !cur_is_red;
            }
            height
        }
        let h1 = simulate(red, blue, true);
        let h2 = simulate(red, blue, false);
        if h1 > h2 { h1 } else { h2 }
    }
}
```

## Racket

```racket
(define/contract (max-height-of-triangle red blue)
  (-> exact-integer? exact-integer? exact-integer?)
  (letrec ((simulate
            (lambda (start-red? r b)
              (let loop ((height 0) (need 1) (r r) (b b) (is-red start-red?))
                (if (if is-red (>= r need) (>= b need))
                    (let* ((new-r (if is-red (- r need) r))
                           (new-b (if is-red b (- b need))))
                      (loop (+ height 1) (+ need 1) new-r new-b (not is-red)))
                    height)))))
    (max (simulate #t red blue)
         (simulate #f red blue))))
```

## Erlang

```erlang
-module(solution).
-export([max_height_of_triangle/2]).

-spec max_height_of_triangle(Red :: integer(), Blue :: integer()) -> integer().
max_height_of_triangle(Red, Blue) ->
    HeightRedStart = build(Red, Blue, red),
    HeightBlueStart = build(Red, Blue, blue),
    if HeightRedStart >= HeightBlueStart -> HeightRedStart;
       true -> HeightBlueStart
    end.

build(Red, Blue, red) ->
    go(1, Red, Blue, red);
build(Red, Blue, blue) ->
    go(1, Red, Blue, blue).

go(Row, R, B, red) when R >= Row ->
    go(Row + 1, R - Row, B, blue);
go(_Row, _R, _B, red) -> 0;
go(Row, R, B, blue) when B >= Row ->
    go(Row + 1, R, B - Row, red);
go(_Row, _R, _B, blue) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_height_of_triangle(red :: integer, blue :: integer) :: integer
  def max_height_of_triangle(red, blue) do
    h_red_top = height(red, blue, 1, :red)
    h_blue_top = height(red, blue, 1, :blue)
    max(h_red_top, h_blue_top)
  end

  defp height(red, blue, row, :red) when red >= row do
    height(red - row, blue, row + 1, :blue)
  end

  defp height(_red, _blue, row, :red), do: row - 1

  defp height(red, blue, row, :blue) when blue >= row do
    height(red, blue - row, row + 1, :red)
  end

  defp height(_red, _blue, row, :blue), do: row - 1
end
```
