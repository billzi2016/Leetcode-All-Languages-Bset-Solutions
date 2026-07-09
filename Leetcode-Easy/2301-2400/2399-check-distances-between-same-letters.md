# 2399. Check Distances Between Same Letters

## Cpp

```cpp
class Solution {
public:
    bool checkDistances(string s, vector<int>& distance) {
        int firstPos[26];
        fill(begin(firstPos), end(firstPos), -1);
        for (int i = 0; i < (int)s.size(); ++i) {
            int idx = s[i] - 'a';
            if (firstPos[idx] == -1) {
                firstPos[idx] = i;
            } else {
                int dist = i - firstPos[idx] - 1;
                if (dist != distance[idx]) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkDistances(String s, int[] distance) {
        int[] first = new int[26];
        java.util.Arrays.fill(first, -1);
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] == -1) {
                first[idx] = i;
            } else {
                int between = i - first[idx] - 1;
                if (between != distance[idx]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        first = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            else:
                if i - first[idx] - 1 != distance[idx]:
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            else:
                if i - first[idx] - 1 != distance[idx]:
                    return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool checkDistances(char* s, int* distance, int distanceSize) {
    int first[26];
    for (int i = 0; i < 26; ++i) first[i] = -1;
    
    int len = strlen(s);
    for (int i = 0; i < len; ++i) {
        int idx = s[i] - 'a';
        if (first[idx] == -1) {
            first[idx] = i;
        } else {
            int expected = distance[idx];
            int actual = i - first[idx] - 1;
            if (actual != expected) return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckDistances(string s, int[] distance)
    {
        int[] firstPos = new int[26];
        for (int i = 0; i < 26; i++) firstPos[i] = -1;

        for (int i = 0; i < s.Length; i++)
        {
            int idx = s[i] - 'a';
            if (firstPos[idx] == -1)
            {
                firstPos[idx] = i;
            }
            else
            {
                int expected = distance[idx];
                int actual = i - firstPos[idx] - 1;
                if (actual != expected) return false;
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} distance
 * @return {boolean}
 */
var checkDistances = function(s, distance) {
    const firstPos = new Array(26).fill(-1);
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (firstPos[idx] === -1) {
            firstPos[idx] = i;
        } else {
            const between = i - firstPos[idx] - 1;
            if (between !== distance[idx]) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function checkDistances(s: string, distance: number[]): boolean {
    const firstPos = new Array(26).fill(-1);
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (firstPos[idx] === -1) {
            firstPos[idx] = i;
        } else {
            const between = i - firstPos[idx] - 1;
            if (between !== distance[idx]) return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $distance
     * @return Boolean
     */
    function checkDistances($s, $distance) {
        $first = array_fill(0, 26, -1);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            $idx = ord($c) - 97;
            if ($first[$idx] === -1) {
                $first[$idx] = $i;
            } else {
                $actual = $i - $first[$idx] - 1;
                if ($actual !== $distance[$idx]) {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkDistances(_ s: String, _ distance: [Int]) -> Bool {
        var firstPos = Array(repeating: -1, count: 26)
        for (i, ch) in s.enumerated() {
            guard let ascii = ch.asciiValue else { return false }
            let idx = Int(ascii - Character("a").asciiValue!)
            if firstPos[idx] == -1 {
                firstPos[idx] = i
            } else {
                let expected = distance[idx]
                let actual = i - firstPos[idx] - 1
                if actual != expected { return false }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkDistances(s: String, distance: IntArray): Boolean {
        val firstPos = IntArray(26) { -1 }
        for (i in s.indices) {
            val idx = s[i] - 'a'
            if (firstPos[idx] == -1) {
                firstPos[idx] = i
            } else {
                val diff = i - firstPos[idx] - 1
                if (diff != distance[idx]) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkDistances(String s, List<int> distance) {
    List<int> first = List.filled(26, -1);
    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      if (first[idx] == -1) {
        first[idx] = i;
      } else {
        int actual = i - first[idx] - 1;
        if (actual != distance[idx]) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkDistances(s string, distance []int) bool {
    first := make([]int, 26)
    for i := range first {
        first[i] = -1
    }
    for i, ch := range s {
        idx := int(ch - 'a')
        if first[idx] == -1 {
            first[idx] = i
        } else {
            if i-first[idx]-1 != distance[idx] {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def check_distances(s, distance)
  first = Array.new(26, -1)
  s.each_char.with_index do |ch, i|
    idx = ch.ord - 'a'.ord
    if first[idx] == -1
      first[idx] = i
    else
      return false unless i - first[idx] - 1 == distance[idx]
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkDistances(s: String, distance: Array[Int]): Boolean = {
        val first = Array.fill(26)(-1)
        for (i <- s.indices) {
            val idx = s(i) - 'a'
            if (first(idx) == -1) {
                first(idx) = i
            } else {
                val diff = i - first(idx) - 1
                if (diff != distance(idx)) return false
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_distances(s: String, distance: Vec<i32>) -> bool {
        let mut first = [-1i32; 26];
        for (i, &b) in s.as_bytes().iter().enumerate() {
            let idx = (b - b'a') as usize;
            if first[idx] == -1 {
                first[idx] = i as i32;
            } else {
                let actual = i as i32 - first[idx] - 1;
                if actual != distance[idx] {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-distances s distance)
  (-> string? (listof exact-integer?) boolean?)
  (let* ((n (string-length s))
         (first (make-vector 26 -1))
         (dist-vec (list->vector distance)))
    (let loop ((i 0))
      (cond
        [(= i n) #t]
        [else
         (define c (string-ref s i))
         (define idx (- (char->integer c) (char->integer #\a)))
         (define first-idx (vector-ref first idx))
         (if (= first-idx -1)
             (begin
               (vector-set! first idx i)
               (loop (+ i 1)))
             (let ((actual (- i first-idx 1))
                   (expected (vector-ref dist-vec idx)))
               (if (= actual expected)
                   (loop (+ i 1))
                   #f)))]))))
```

## Erlang

```erlang
-spec check_distances(S :: unicode:unicode_binary(), Distance :: [integer()]) -> boolean().
check_distances(S, Distance) ->
    DistTuple = list_to_tuple(Distance),
    loop(binary_to_list(S), 0, #{}, DistTuple).

loop([], _Idx, _Map, _DistTuple) -> true;
loop([C|Rest], Idx, Map, DistTuple) ->
    CharIdx = C - $a,
    case maps:get(CharIdx, Map, undefined) of
        undefined ->
            loop(Rest, Idx + 1, maps:put(CharIdx, Idx, Map), DistTuple);
        PrevIdx ->
            Expected = element(CharIdx + 1, DistTuple),
            Actual = Idx - PrevIdx - 1,
            if
                Actual =:= Expected ->
                    loop(Rest, Idx + 1, maps:remove(CharIdx, Map), DistTuple);
                true -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_distances(s :: String.t(), distance :: [integer]) :: boolean()
  def check_distances(s, distance) do
    chars = String.graphemes(s)

    result =
      Enum.reduce_while(Enum.with_index(chars), %{}, fn {ch, idx}, first_map ->
        code = :binary.first(ch) - ?a

        case Map.fetch(first_map, code) do
          {:ok, first_idx} ->
            expected = Enum.at(distance, code)

            if idx - first_idx - 1 == expected do
              {:cont, Map.delete(first_map, code)}
            else
              {:halt, false}
            end

          :error ->
            {:cont, Map.put(first_map, code, idx)}
        end
      end)

    case result do
      false -> false
      _ -> true
    end
  end
end
```
