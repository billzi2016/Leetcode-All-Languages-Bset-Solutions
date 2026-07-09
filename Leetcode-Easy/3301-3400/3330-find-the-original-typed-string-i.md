# 3330. Find the Original Typed String I

## Cpp

```cpp
class Solution {
public:
    int possibleStringCount(string word) {
        int extra = 0;
        for (int i = 1; i < (int)word.size(); ++i) {
            if (word[i] == word[i - 1]) ++extra;
        }
        return extra + 1;
    }
};
```

## Java

```java
class Solution {
    public int possibleStringCount(String word) {
        int extra = 0;
        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) == word.charAt(i - 1)) {
                extra++;
            }
        }
        return extra + 1;
    }
}
```

## Python

```python
class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        cnt = 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                cnt += 1
        return cnt + 1
```

## Python3

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                ans += 1
        return ans
```

## C

```c
int possibleStringCount(char* word) {
    int ans = 1;
    for (int i = 1; word[i] != '\0'; ++i) {
        if (word[i] == word[i - 1]) {
            ++ans;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int PossibleStringCount(string word)
    {
        int count = 1; // the original string without any mistake
        for (int i = 1; i < word.Length; i++)
        {
            if (word[i] == word[i - 1])
                count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var possibleStringCount = function(word) {
    let ans = 1; // count the case with no mistake
    for (let i = 1; i < word.length; ++i) {
        if (word[i] === word[i - 1]) {
            ans += 1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function possibleStringCount(word: string): number {
    let count = 1; // original string without any mistake
    for (let i = 1; i < word.length; i++) {
        if (word[i] === word[i - 1]) {
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
     * @param String $word
     * @return Integer
     */
    function possibleStringCount($word) {
        $n = strlen($word);
        $ans = 1; // case with no mistake
        for ($i = 1; $i < $n; $i++) {
            if ($word[$i] === $word[$i - 1]) {
                $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func possibleStringCount(_ word: String) -> Int {
        let chars = Array(word)
        var result = 1
        for i in 1..<chars.count {
            if chars[i] == chars[i - 1] {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun possibleStringCount(word: String): Int {
        var count = 1
        for (i in 1 until word.length) {
            if (word[i] == word[i - 1]) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int possibleStringCount(String word) {
    int cnt = 0;
    for (int i = 1; i < word.length; ++i) {
      if (word[i] == word[i - 1]) cnt++;
    }
    return cnt + 1;
  }
}
```

## Golang

```go
func possibleStringCount(word string) int {
    ans := 1
    for i := 1; i < len(word); i++ {
        if word[i] == word[i-1] {
            ans++
        }
    }
    return ans
}
```

## Ruby

```ruby
def possible_string_count(word)
  count = 1
  (1...word.length).each do |i|
    count += 1 if word[i] == word[i - 1]
  end
  count
end
```

## Scala

```scala
object Solution {
    def possibleStringCount(word: String): Int = {
        var cnt = 1 // base string without any mistake
        for (i <- 1 until word.length) {
            if (word.charAt(i) == word.charAt(i - 1)) cnt += 1
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        let b = word.as_bytes();
        let mut ans = 1i32;
        for i in 1..b.len() {
            if b[i] == b[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (possible-string-count word)
  (-> string? exact-integer?)
  (let* ((n (string-length word))
         (cnt (let loop ((i 1) (acc 0))
                (if (>= i n)
                    acc
                    (loop (+ i 1)
                          (+ acc (if (char=? (string-ref word (- i 1))
                                         (string-ref word i))
                                      1
                                      0)))))))
    (+ cnt 1)))
```

## Erlang

```erlang
-spec possible_string_count(Word :: unicode:unicode_binary()) -> integer().
possible_string_count(Word) ->
    List = unicode:characters_to_list(Word),
    AdjacentSame = count_adjacent_same(List, 0),
    AdjacentSame + 1.

count_adjacent_same([], Acc) -> Acc;
count_adjacent_same([_], Acc) -> Acc;
count_adjacent_same([Prev, Curr | Rest], Acc) ->
    NewAcc = if Prev == Curr -> Acc + 1; true -> Acc end,
    count_adjacent_same([Curr | Rest], NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec possible_string_count(word :: String.t) :: integer
  def possible_string_count(word) do
    {cnt, _} =
      word
      |> String.graphemes()
      |> Enum.reduce({0, nil}, fn ch, {acc, prev} ->
        if ch == prev do
          {acc + 1, ch}
        else
          {acc, ch}
        end
      end)

    cnt + 1
  end
end
```
