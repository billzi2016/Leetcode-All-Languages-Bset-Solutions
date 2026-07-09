# 3206. Alternating Groups I

## Cpp

```cpp
class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors) {
        int n = colors.size();
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            int left = (i - 1 + n) % n;
            int right = (i + 1) % n;
            if (colors[left] == colors[right] && colors[i] != colors[left]) {
                ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int numberOfAlternatingGroups(int[] colors) {
        int n = colors.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int left = colors[(i - 1 + n) % n];
            int right = colors[(i + 1) % n];
            if (colors[i] != left && colors[i] != right) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        cnt = 0
        for i in range(n):
            left = colors[(i - 1) % n]
            right = colors[(i + 1) % n]
            if colors[i] != left and colors[i] != right:
                cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        for i in range(n):
            if colors[i] != colors[(i - 1) % n] and colors[i] != colors[(i + 1) % n]:
                count += 1
        return count
```

## C

```c
int numberOfAlternatingGroups(int* colors, int colorsSize) {
    int n = colorsSize;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        int left = (i - 1 + n) % n;
        int right = (i + 1) % n;
        if (colors[i] != colors[left] && colors[i] != colors[right]) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfAlternatingGroups(int[] colors) {
        int n = colors.Length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int left = colors[(i - 1 + n) % n];
            int right = colors[(i + 1) % n];
            if (colors[i] != left && colors[i] != right) {
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} colors
 * @return {number}
 */
var numberOfAlternatingGroups = function(colors) {
    const n = colors.length;
    let count = 0;
    for (let i = 0; i < n; i++) {
        const left = (i - 1 + n) % n;
        const right = (i + 1) % n;
        if (colors[left] !== colors[i] && colors[right] !== colors[i]) {
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function numberOfAlternatingGroups(colors: number[]): number {
    const n = colors.length;
    let count = 0;
    for (let i = 0; i < n; i++) {
        const prev = colors[(i - 1 + n) % n];
        const next = colors[(i + 1) % n];
        if (colors[i] !== prev && colors[i] !== next) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function numberOfAlternatingGroups($colors) {
        $n = count($colors);
        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            $prev = $colors[($i - 1 + $n) % $n];
            $next = $colors[($i + 1) % $n];
            if ($colors[$i] != $prev && $colors[$i] != $next) {
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
    func numberOfAlternatingGroups(_ colors: [Int]) -> Int {
        let n = colors.count
        var count = 0
        for i in 0..<n {
            let left = (i - 1 + n) % n
            let right = (i + 1) % n
            if colors[i] != colors[left] && colors[i] != colors[right] {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfAlternatingGroups(colors: IntArray): Int {
        val n = colors.size
        var count = 0
        for (i in 0 until n) {
            val left = colors[(i - 1 + n) % n]
            val mid = colors[i]
            val right = colors[(i + 1) % n]
            if (mid != left && mid != right) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfAlternatingGroups(List<int> colors) {
    int n = colors.length;
    int count = 0;
    for (int i = 0; i < n; ++i) {
      int left = colors[(i - 1 + n) % n];
      int right = colors[(i + 1) % n];
      if (left == right && colors[i] != left) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numberOfAlternatingGroups(colors []int) int {
	n := len(colors)
	count := 0
	for i := 0; i < n; i++ {
		left := colors[(i-1+n)%n]
		right := colors[(i+1)%n]
		if colors[i] != left && colors[i] != right {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def number_of_alternating_groups(colors)
  n = colors.length
  cnt = 0
  (0...n).each do |i|
    left = colors[(i - 1) % n]
    right = colors[(i + 1) % n]
    cnt += 1 if left == right && colors[i] != left
  end
  cnt
end
```

## Scala

```scala
object Solution {
    def numberOfAlternatingGroups(colors: Array[Int]): Int = {
        val n = colors.length
        var cnt = 0
        for (i <- 0 until n) {
            val left = colors((i - 1 + n) % n)
            val right = colors((i + 1) % n)
            if (left == right && colors(i) != left) cnt += 1
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>) -> i32 {
        let n = colors.len();
        if n < 3 {
            return 0;
        }
        let mut count = 0;
        for i in 0..n {
            let left = (i + n - 1) % n;
            let right = (i + 1) % n;
            if colors[i] != colors[left] && colors[i] != colors[right] {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-alternating-groups colors)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length colors))
         (mod (lambda (i) (modulo i n))))
    (for/sum ([i (in-range n)])
      (let ((prev (list-ref colors (mod (- i 1))))
            (curr (list-ref colors i))
            (next (list-ref colors (mod (+ i 1)))))
        (if (and (not (= prev curr)) (not (= next curr))) 1 0)))))
```

## Erlang

```erlang
-spec number_of_alternating_groups(Colors :: [integer()]) -> integer().
number_of_alternating_groups(Colors) ->
    N = length(Colors),
    Tuple = list_to_tuple(Colors),
    count(Tuple, N, 0, 0).

count(_Tuple, N, Index, Acc) when Index >= N -> Acc;
count(Tuple, N, Index, Acc) ->
    LeftIdx = ((Index - 1 + N) rem N) + 1,
    MidIdx = Index + 1,
    RightIdx = ((Index + 1) rem N) + 1,
    Left = element(LeftIdx, Tuple),
    Mid = element(MidIdx, Tuple),
    Right = element(RightIdx, Tuple),
    NewAcc = if Mid =/= Left andalso Mid =/= Right -> Acc + 1; true -> Acc end,
    count(Tuple, N, Index + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer]) :: integer
  def number_of_alternating_groups(colors) do
    n = length(colors)
    tup = List.to_tuple(colors)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      c = elem(tup, i)
      left = elem(tup, rem(i - 1 + n, n))
      right = elem(tup, rem(i + 1, n))

      if c != left and c != right do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
