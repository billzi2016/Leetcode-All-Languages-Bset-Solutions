# 2103. Rings and Rods

## Cpp

```cpp
class Solution {
public:
    int countPoints(string rings) {
        int mask[10] = {0};
        for (int i = 0; i < (int)rings.size(); i += 2) {
            char color = rings[i];
            int rod = rings[i + 1] - '0';
            if (color == 'R') mask[rod] |= 1;
            else if (color == 'G') mask[rod] |= 2;
            else if (color == 'B') mask[rod] |= 4;
        }
        int ans = 0;
        for (int i = 0; i < 10; ++i) {
            if (mask[i] == 7) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPoints(String rings) {
        int[] mask = new int[10];
        for (int i = 0; i < rings.length(); i += 2) {
            char color = rings.charAt(i);
            int rod = rings.charAt(i + 1) - '0';
            switch (color) {
                case 'R' -> mask[rod] |= 1;
                case 'G' -> mask[rod] |= 2;
                case 'B' -> mask[rod] |= 4;
            }
        }
        int count = 0;
        for (int m : mask) {
            if (m == 7) count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        masks = [0] * 10  # bitmask for each rod
        color_bit = {'R': 1, 'G': 2, 'B': 4}
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = int(rings[i + 1])
            masks[r] |= color_bit[c]
        return sum(1 for m in masks if m == 7)
```

## Python3

```python
class Solution:
    def countPoints(self, rings: str) -> int:
        masks = [0] * 10
        color_bit = {'R': 1, 'G': 2, 'B': 4}
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = ord(rings[i + 1]) - ord('0')
            masks[r] |= color_bit[c]
        return sum(1 for m in masks if m == 7)
```

## C

```c
int countPoints(char* rings) {
    int mask[10] = {0};
    for (int i = 0; rings[i] && rings[i + 1]; i += 2) {
        char c = rings[i];
        int rod = rings[i + 1] - '0';
        if (c == 'R') mask[rod] |= 1;
        else if (c == 'G') mask[rod] |= 2;
        else if (c == 'B') mask[rod] |= 4;
    }
    int cnt = 0;
    for (int i = 0; i < 10; ++i) {
        if (mask[i] == 7) ++cnt;
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPoints(string rings) {
        int[] masks = new int[10];
        for (int i = 0; i < rings.Length; i += 2) {
            char color = rings[i];
            int rod = rings[i + 1] - '0';
            switch (color) {
                case 'R':
                    masks[rod] |= 1;
                    break;
                case 'G':
                    masks[rod] |= 2;
                    break;
                case 'B':
                    masks[rod] |= 4;
                    break;
            }
        }
        int count = 0;
        foreach (int mask in masks) {
            if (mask == 7) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} rings
 * @return {number}
 */
var countPoints = function(rings) {
    const masks = new Array(10).fill(0);
    for (let i = 0; i < rings.length; i += 2) {
        const color = rings[i];
        const rod = rings.charCodeAt(i + 1) - 48; // '0' -> 0
        let bit = 0;
        if (color === 'R') bit = 1;
        else if (color === 'G') bit = 2;
        else if (color === 'B') bit = 4;
        masks[rod] |= bit;
    }
    let count = 0;
    for (let i = 0; i < 10; ++i) {
        if (masks[i] === 7) count++;
    }
    return count;
};
```

## Typescript

```typescript
function countPoints(rings: string): number {
    const masks = new Array(10).fill(0);
    for (let i = 0; i < rings.length; i += 2) {
        const color = rings[i];
        const rod = rings.charCodeAt(i + 1) - 48;
        let bit = 0;
        if (color === 'R') bit = 1;
        else if (color === 'G') bit = 2;
        else if (color === 'B') bit = 4;
        masks[rod] |= bit;
    }
    let count = 0;
    for (const m of masks) {
        if (m === 7) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param string $rings
     * @return int
     */
    function countPoints($rings) {
        $mask = array_fill(0, 10, 0);
        $len = strlen($rings);
        for ($i = 0; $i < $len; $i += 2) {
            $color = $rings[$i];
            $rod = intval($rings[$i + 1]);
            switch ($color) {
                case 'R':
                    $mask[$rod] |= 1;
                    break;
                case 'G':
                    $mask[$rod] |= 2;
                    break;
                case 'B':
                    $mask[$rod] |= 4;
                    break;
            }
        }
        $count = 0;
        foreach ($mask as $m) {
            if ($m === 7) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countPoints(_ rings: String) -> Int {
        var masks = Array(repeating: 0, count: 10)
        let chars = Array(rings)
        var i = 0
        while i < chars.count {
            let colorChar = chars[i]
            let rodChar = chars[i + 1]
            guard let rod = Int(String(rodChar)) else { i += 2; continue }
            var bit = 0
            switch colorChar {
            case "R": bit = 1
            case "G": bit = 2
            case "B": bit = 4
            default: break
            }
            masks[rod] |= bit
            i += 2
        }
        var result = 0
        for mask in masks where mask == 7 {
            result += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPoints(rings: String): Int {
        val masks = IntArray(10)
        var i = 0
        while (i < rings.length) {
            val color = rings[i]
            val rod = rings[i + 1] - '0'
            when (color) {
                'R' -> masks[rod] = masks[rod] or 1
                'G' -> masks[rod] = masks[rod] or 2
                'B' -> masks[rod] = masks[rod] or 4
            }
            i += 2
        }
        var count = 0
        for (mask in masks) {
            if (mask == 7) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countPoints(String rings) {
    List<int> masks = List.filled(10, 0);
    for (int i = 0; i < rings.length; i += 2) {
      String color = rings[i];
      int rod = rings.codeUnitAt(i + 1) - 48; // '0' ASCII is 48
      int bit;
      if (color == 'R') {
        bit = 1;
      } else if (color == 'G') {
        bit = 2;
      } else { // 'B'
        bit = 4;
      }
      masks[rod] |= bit;
    }
    int count = 0;
    for (int mask in masks) {
      if (mask == 7) count++;
    }
    return count;
  }
}
```

## Golang

```go
func countPoints(rings string) int {
	var rods [10]int
	for i := 0; i < len(rings); i += 2 {
		c := rings[i]
		idx := rings[i+1] - '0'
		mask := 0
		switch c {
		case 'R':
			mask = 1
		case 'G':
			mask = 2
		case 'B':
			mask = 4
		}
		rods[idx] |= mask
	}
	count := 0
	for _, m := range rods {
		if m == 7 {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_points(rings)
  masks = Array.new(10, 0)
  i = 0
  while i < rings.length
    color = rings[i]
    rod = rings.getbyte(i + 1) - 48
    case color
    when 'R'
      masks[rod] |= 1
    when 'G'
      masks[rod] |= 2
    else # 'B'
      masks[rod] |= 4
    end
    i += 2
  end
  masks.count(7)
end
```

## Scala

```scala
object Solution {
    def countPoints(rings: String): Int = {
        val masks = Array.fill(10)(0)
        var i = 0
        while (i < rings.length) {
            val color = rings.charAt(i)
            val rod = rings.charAt(i + 1) - '0'
            val bit = color match {
                case 'R' => 1
                case 'G' => 2
                case 'B' => 4
                case _   => 0
            }
            masks(rod) |= bit
            i += 2
        }
        var count = 0
        for (mask <- masks) {
            if (mask == 7) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut masks = [0u8; 10];
        let bytes = rings.as_bytes();
        let mut i = 0;
        while i < bytes.len() {
            let bit = match bytes[i] as char {
                'R' => 1,
                'G' => 2,
                'B' => 4,
                _ => 0,
            };
            let rod = (bytes[i + 1] - b'0') as usize;
            masks[rod] |= bit;
            i += 2;
        }
        masks.iter().filter(|&&m| m == 7).count() as i32
    }
}
```

## Racket

```racket
(define/contract (count-points rings)
  (-> string? exact-integer?)
  (let* ([len (string-length rings)]
         [masks (make-vector 10 0)])
    (for ([i (in-range 0 len 2)])
      (let* ([c (string-ref rings i)]
             [rod-char (string-ref rings (+ i 1))]
             [rod (- (char->integer rod-char) (char->integer #\0))]
             [bit (cond [(char=? c #\R) 1]
                        [(char=? c #\G) 2]
                        [else 4])])
        (vector-set! masks rod (bitwise-ior (vector-ref masks rod) bit))))
    (for/sum ([mask (in-vector masks)])
      (if (= mask 7) 1 0))))
```

## Erlang

```erlang
-module(solution).
-export([count_points/1]).

-spec count_points(Rings :: unicode:unicode_binary()) -> integer().
count_points(Rings) ->
    List = binary_to_list(Rings),
    FinalMap = process(List, #{}),
    maps:fold(fun(_Rod, Mask, Acc) ->
        case Mask band 7 of
            7 -> Acc + 1;
            _ -> Acc
        end
    end, 0, FinalMap).

process([], Map) -> Map;
process([Color, RodChar | Rest], Map) ->
    Bit = case Color of
        $R -> 1;
        $G -> 2;
        $B -> 4
    end,
    Rod = RodChar - $0,
    Prev = maps:get(Rod, Map, 0),
    NewMap = maps:put(Rod, Prev bor Bit, Map),
    process(Rest, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_points(rings :: String.t()) :: integer()
  def count_points(rings) do
    parse(rings, %{})
  end

  defp parse(<<>>, acc) do
    acc
    |> Map.values()
    |> Enum.count(fn mask -> mask == 0b111 end)
  end

  defp parse(<<color, rod_char, rest::binary>>, acc) do
    rod = rod_char - ?0
    new_mask = (Map.get(acc, rod, 0)) ||| color_bit(color)
    parse(rest, Map.put(acc, rod, new_mask))
  end

  defp color_bit(?R), do: 1 <<< 0
  defp color_bit(?G), do: 1 <<< 1
  defp color_bit(?B), do: 1 <<< 2
end
```
