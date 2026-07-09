# 2211. Count Collisions on a Road

## Cpp

```cpp
class Solution {
public:
    int countCollisions(string directions) {
        int n = directions.size();
        int i = 0, j = n - 1;
        while (i < n && directions[i] == 'L') ++i;
        while (j >= 0 && directions[j] == 'R') --j;
        if (i > j) return 0;
        int ans = 0;
        for (int k = i; k <= j; ++k) {
            if (directions[k] != 'S') ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countCollisions(String directions) {
        int n = directions.length();
        int i = 0;
        while (i < n && directions.charAt(i) == 'L') {
            i++;
        }
        int j = n - 1;
        while (j >= 0 && directions.charAt(j) == 'R') {
            j--;
        }
        if (i > j) {
            return 0;
        }
        int collisions = 0;
        for (int k = i; k <= j; k++) {
            if (directions.charAt(k) != 'S') {
                collisions++;
            }
        }
        return collisions;
    }
}
```

## Python

```python
class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        n = len(directions)
        left = 0
        while left < n and directions[left] == 'L':
            left += 1
        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        if left > right:
            return 0
        cnt = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left = 0
        while left < n and directions[left] == 'L':
            left += 1
        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1
        if left > right:
            return 0
        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1
        return collisions
```

## C

```c
#include <string.h>

int countCollisions(char* directions) {
    int n = strlen(directions);
    int i = 0;
    while (i < n && directions[i] == 'L') ++i;
    int leftSafe = i;

    int j = n - 1;
    while (j >= 0 && directions[j] == 'R') --j;
    int rightSafe = n - 1 - j;

    int movingCount = 0;
    for (int k = 0; k < n; ++k) {
        if (directions[k] != 'S')
            ++movingCount;
    }

    return movingCount - leftSafe - rightSafe;
}
```

## Csharp

```csharp
public class Solution {
    public int CountCollisions(string directions) {
        int n = directions.Length;
        int left = 0;
        while (left < n && directions[left] == 'L') left++;
        int right = n - 1;
        while (right >= 0 && directions[right] == 'R') right--;
        int collisions = 0;
        for (int i = left; i <= right; i++) {
            if (directions[i] != 'S')
                collisions++;
        }
        return collisions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} directions
 * @return {number}
 */
var countCollisions = function(directions) {
    const n = directions.length;
    let left = 0;
    while (left < n && directions[left] === 'L') left++;
    
    let rightIdx = n - 1;
    while (rightIdx >= 0 && directions[rightIdx] === 'R') rightIdx--;
    const right = n - 1 - rightIdx; // number of trailing 'R's
    
    if (left + right >= n) return 0; // no cars that can collide
    
    let collisions = 0;
    for (let i = left; i <= rightIdx; i++) {
        if (directions[i] !== 'S') collisions++;
    }
    return collisions;
};
```

## Typescript

```typescript
function countCollisions(directions: string): number {
    const n = directions.length;
    let left = 0;
    while (left < n && directions[left] === 'L') left++;
    let right = n - 1;
    while (right >= 0 && directions[right] === 'R') right--;
    if (left > right) return 0;
    let collisions = 0;
    for (let i = left; i <= right; i++) {
        if (directions[i] !== 'S') collisions++;
    }
    return collisions;
}
```

## Php

```php
class Solution {

    /**
     * @param String $directions
     * @return Integer
     */
    function countCollisions($directions) {
        $n = strlen($directions);
        $left = 0;
        while ($left < $n && $directions[$left] === 'L') {
            $left++;
        }
        $right = $n - 1;
        while ($right >= 0 && $directions[$right] === 'R') {
            $right--;
        }
        if ($left > $right) {
            return 0;
        }
        $collisions = 0;
        for ($i = $left; $i <= $right; $i++) {
            if ($directions[$i] !== 'S') {
                $collisions++;
            }
        }
        return $collisions;
    }
}
```

## Swift

```swift
class Solution {
    func countCollisions(_ directions: String) -> Int {
        let cars = Array(directions)
        var left = 0
        while left < cars.count && cars[left] == "L" {
            left += 1
        }
        var right = cars.count - 1
        while right >= 0 && cars[right] == "R" {
            right -= 1
        }
        if left > right { return 0 }
        var collisions = 0
        for i in left...right {
            if cars[i] != "S" {
                collisions += 1
            }
        }
        return collisions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCollisions(directions: String): Int {
        val n = directions.length
        var left = 0
        while (left < n && directions[left] == 'L') left++
        var right = n - 1
        while (right >= 0 && directions[right] == 'R') right--
        if (left > right) return 0
        var collisions = 0
        for (i in left..right) {
            if (directions[i] != 'S') collisions++
        }
        return collisions
    }
}
```

## Dart

```dart
class Solution {
  int countCollisions(String directions) {
    int n = directions.length;
    int i = 0;
    while (i < n && directions[i] == 'L') {
      i++;
    }
    int j = n - 1;
    while (j >= i && directions[j] == 'R') {
      j--;
    }
    int collisions = 0;
    for (int k = i; k <= j; k++) {
      if (directions[k] != 'S') {
        collisions++;
      }
    }
    return collisions;
  }
}
```

## Golang

```go
func countCollisions(directions string) int {
	n := len(directions)
	left := 0
	for left < n && directions[left] == 'L' {
		left++
	}
	right := n - 1
	for right >= 0 && directions[right] == 'R' {
		right--
	}
	if left > right {
		return 0
	}
	collisions := 0
	for i := left; i <= right; i++ {
		if directions[i] != 'S' {
			collisions++
		}
	}
	return collisions
}
```

## Ruby

```ruby
def count_collisions(directions)
  n = directions.length
  left = 0
  while left < n && directions[left] == 'L'
    left += 1
  end
  right = n - 1
  while right >= 0 && directions[right] == 'R'
    right -= 1
  end
  return 0 if left > right

  collisions = 0
  (left..right).each do |i|
    collisions += 1 unless directions[i] == 'S'
  end
  collisions
end
```

## Scala

```scala
object Solution {
    def countCollisions(directions: String): Int = {
        val n = directions.length
        var left = 0
        while (left < n && directions(left) == 'L') left += 1
        var right = n - 1
        while (right >= 0 && directions(right) == 'R') right -= 1
        if (left > right) return 0
        var collisions = 0
        var i = left
        while (i <= right) {
            if (directions(i) != 'S') collisions += 1
            i += 1
        }
        collisions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let bytes = directions.as_bytes();
        let n = bytes.len();

        // Trim leading 'L's
        let mut left = 0;
        while left < n && bytes[left] == b'L' {
            left += 1;
        }
        if left == n {
            return 0;
        }

        // Trim trailing 'R's (right is exclusive)
        let mut right = n;
        while right > left && bytes[right - 1] == b'R' {
            right -= 1;
        }

        if left >= right {
            return 0;
        }

        let mut collisions = 0;
        for i in left..right {
            if bytes[i] != b'S' {
                collisions += 1;
            }
        }
        collisions as i32
    }
}
```

## Racket

```racket
(define/contract (count-collisions directions)
  (-> string? exact-integer?)
  (let* ((n (string-length directions))
         (start
          (let loop ((i 0))
            (if (and (< i n) (char=? (string-ref directions i) #\L))
                (loop (+ i 1))
                i)))
         (end
          (let loop ((i (- n 1)))
            (if (and (>= i 0) (char=? (string-ref directions i) #\R))
                (loop (- i 1))
                i))))
    (if (> start end)
        0
        (let loop ((idx start) (cnt 0))
          (if (> idx end)
              cnt
              (let ((c (string-ref directions idx)))
                (loop (+ idx 1) (if (char=? c #\S) cnt (+ cnt 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_collisions/1]).

-spec count_collisions(Directions :: unicode:unicode_binary()) -> integer().
count_collisions(Directions) ->
    Str = binary_to_list(Directions),
    Len = length(Str),
    LeadingL = count_leading_L(Str, 0),
    Rev = lists:reverse(Str),
    TrailingR = count_trailing_R(Rev, 0),
    MiddleLen = Len - LeadingL - TrailingR,
    if
        MiddleLen =< 0 -> 0;
        true ->
            Rest = lists:nthtail(LeadingL, Str),
            MiddleList = lists:sublist(Rest, MiddleLen),
            count_non_S(MiddleList, 0)
    end.

count_leading_L([], Acc) -> Acc;
count_leading_L([H|T], Acc) when H =:= $L ->
    count_leading_L(T, Acc + 1);
count_leading_L(_, Acc) -> Acc.

count_trailing_R([], Acc) -> Acc;
count_trailing_R([H|T], Acc) when H =:= $R ->
    count_trailing_R(T, Acc + 1);
count_trailing_R(_, Acc) -> Acc.

count_non_S([], Acc) -> Acc;
count_non_S([H|T], Acc) when H =/= $S ->
    count_non_S(T, Acc + 1);
count_non_S([_|T], Acc) ->
    count_non_S(T, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_collisions(directions :: String.t()) :: integer()
  def count_collisions(directions) do
    chars = String.to_charlist(directions)
    len = length(chars)

    lead =
      Enum.take_while(chars, fn c -> c == ?L end)
      |> length()

    trail =
      chars
      |> Enum.reverse()
      |> Enum.take_while(fn c -> c == ?R end)
      |> length()

    middle_len = len - lead - trail

    mid_s =
      if middle_len > 0 do
        Enum.slice(chars, lead, middle_len)
        |> Enum.count(fn c -> c == ?S end)
      else
        0
      end

    len - lead - trail - mid_s
  end
end
```
