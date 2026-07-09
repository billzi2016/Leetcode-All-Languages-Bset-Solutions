# 1974. Minimum Time to Type Word Using Special Typewriter

## Cpp

```cpp
class Solution {
public:
    int minTimeToType(string word) {
        int total = 0;
        char cur = 'a';
        for (char c : word) {
            int diff = abs(c - cur);
            int steps = min(diff, 26 - diff);
            total += steps + 1; // move steps plus typing
            cur = c;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int minTimeToType(String word) {
        int time = 0;
        char current = 'a';
        for (char c : word.toCharArray()) {
            int diff = Math.abs(c - current);
            time += Math.min(diff, 26 - diff); // movement
            time += 1; // typing the character
            current = c;
        }
        return time;
    }
}
```

## Python

```python
class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        cur = ord('a')
        total = 0
        for ch in word:
            target = ord(ch)
            diff = abs(target - cur)
            steps = diff if diff <= 13 else 26 - diff
            total += steps + 1
            cur = target
        return total
```

## Python3

```python
class Solution:
    def minTimeToType(self, word: str) -> int:
        total = 0
        cur = ord('a')
        for ch in word:
            target = ord(ch)
            diff = abs(target - cur)
            steps = min(diff, 26 - diff)
            total += steps + 1  # move steps plus typing
            cur = target
        return total
```

## C

```c
int minTimeToType(char* word) {
    int total = 0;
    char cur = 'a';
    for (int i = 0; word[i] != '\0'; ++i) {
        char target = word[i];
        int diff = target - cur;
        if (diff < 0) diff = -diff;
        int steps = diff < 26 - diff ? diff : 26 - diff;
        total += steps + 1; // move steps plus typing
        cur = target;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int MinTimeToType(string word) {
        int total = 0;
        char current = 'a';
        foreach (char c in word) {
            int diff = Math.Abs(c - current);
            int move = Math.Min(diff, 26 - diff);
            total += move + 1; // move time plus typing time
            current = c;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minTimeToType = function(word) {
    let total = 0;
    let curCode = 'a'.charCodeAt(0);
    for (let i = 0; i < word.length; i++) {
        const targetCode = word.charCodeAt(i);
        const diff = Math.abs(targetCode - curCode);
        const move = Math.min(diff, 26 - diff);
        total += move + 1; // move seconds + typing second
        curCode = targetCode;
    }
    return total;
};
```

## Typescript

```typescript
function minTimeToType(word: string): number {
    let total = 0;
    let current = 'a'.charCodeAt(0);
    for (const ch of word) {
        const target = ch.charCodeAt(0);
        const diff = Math.abs(target - current);
        const move = Math.min(diff, 26 - diff);
        total += move + 1; // move time plus typing time
        current = target;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minTimeToType($word) {
        $time = 0;
        $cur = 0; // position of 'a'
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $target = ord($word[$i]) - ord('a');
            $diff = abs($target - $cur);
            $move = min($diff, 26 - $diff);
            $time += $move + 1; // move time + typing time
            $cur = $target;
        }
        return $time;
    }
}
```

## Swift

```swift
class Solution {
    func minTimeToType(_ word: String) -> Int {
        var total = 0
        var current = 0 // index for 'a'
        let aValue = UnicodeScalar("a").value
        
        for ch in word {
            guard let scalar = ch.unicodeScalars.first else { continue }
            let target = Int(scalar.value - aValue)
            let diff = abs(target - current)
            total += min(diff, 26 - diff) + 1
            current = target
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTimeToType(word: String): Int {
        var time = 0
        var current = 'a'
        for (c in word) {
            val diff = kotlin.math.abs(c.code - current.code)
            val move = kotlin.math.min(diff, 26 - diff)
            time += move + 1
            current = c
        }
        return time
    }
}
```

## Dart

```dart
class Solution {
  int minTimeToType(String word) {
    int total = 0;
    int cur = 'a'.codeUnitAt(0);
    for (int i = 0; i < word.length; i++) {
      int target = word.codeUnitAt(i);
      int diff = (target - cur).abs();
      int move = diff <= 13 ? diff : 26 - diff;
      total += move + 1;
      cur = target;
    }
    return total;
  }
}
```

## Golang

```go
func minTimeToType(word string) int {
    cur := 'a'
    total := 0
    for _, ch := range word {
        diff := int(cur - ch)
        if diff < 0 {
            diff = -diff
        }
        steps := diff
        if 26-diff < steps {
            steps = 26 - diff
        }
        total += steps + 1
        cur = ch
    }
    return total
}
```

## Ruby

```ruby
def min_time_to_type(word)
  total = 0
  current = 'a'.ord
  word.each_char do |ch|
    target = ch.ord
    diff = (target - current).abs
    move = [diff, 26 - diff].min
    total += move + 1
    current = target
  end
  total
end
```

## Scala

```scala
object Solution {
    def minTimeToType(word: String): Int = {
        var time = 0
        var cur: Char = 'a'
        for (c <- word) {
            val diff = Math.abs(c - cur)
            val steps = Math.min(diff, 26 - diff)
            time += steps + 1 // move steps plus typing
            cur = c
        }
        time
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_time_to_type(word: String) -> i32 {
        let mut cur = b'a';
        let mut total: i32 = 0;
        for ch in word.bytes() {
            let diff = if cur > ch { cur - ch } else { ch - cur };
            let steps = std::cmp::min(diff, 26 - diff);
            total += steps as i32 + 1; // move steps + type
            cur = ch;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (min-time-to-type word)
  (-> string? exact-integer?)
  (let loop ((i 0) (pos 0) (time 0))
    (if (= i (string-length word))
        time
        (let* ([c (string-ref word i)]
               [target (- (char->integer c) (char->integer #\a))]
               [diff (abs (- target pos))]
               [steps (min diff (- 26 diff))])
          (loop (+ i 1) target (+ time steps 1))))))
```

## Erlang

```erlang
-spec min_time_to_type(Word :: unicode:unicode_binary()) -> integer().
min_time_to_type(Word) ->
    min_time_to_type(Word, $a, 0).

min_time_to_type(<<>>, _Current, Acc) ->
    Acc;
min_time_to_type(<<C, Rest/binary>>, Current, Acc) ->
    Diff = erlang:abs(C - Current),
    Steps = if Diff > 13 -> 26 - Diff; true -> Diff end,
    NewAcc = Acc + Steps + 1,
    min_time_to_type(Rest, C, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time_to_type(word :: String.t) :: integer
  def min_time_to_type(word) do
    {total, _} =
      word
      |> String.to_charlist()
      |> Enum.reduce({0, ?a}, fn ch, {acc, cur} ->
        diff = abs(ch - cur)
        steps = min(diff, 26 - diff)
        {acc + steps + 1, ch}
      end)

    total
  end
end
```
