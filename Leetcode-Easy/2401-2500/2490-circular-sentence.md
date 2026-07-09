# 2490. Circular Sentence

## Cpp

```cpp
class Solution {
public:
    bool isCircularSentence(std::string sentence) {
        int n = sentence.size();
        for (int i = 0; i < n - 1; ++i) {
            if (sentence[i] == ' ') {
                // character before space and after space must match
                if (sentence[i - 1] != sentence[i + 1]) return false;
            }
        }
        // first and last characters must match
        return sentence.front() == sentence.back();
    }
};
```

## Java

```java
class Solution {
    public boolean isCircularSentence(String sentence) {
        int n = sentence.length();
        for (int i = 0; i < n; i++) {
            if (sentence.charAt(i) == ' ') {
                // character before space should match character after space
                if (sentence.charAt(i - 1) != sentence.charAt(i + 1)) {
                    return false;
                }
            }
        }
        // first and last characters must be the same
        return sentence.charAt(0) == sentence.charAt(n - 1);
    }
}
```

## Python

```python
class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        n = len(sentence)
        for i in range(n):
            if sentence[i] == ' ':
                # characters before and after the space must match
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        # first and last character of the whole sentence must match
        return sentence[0] == sentence[-1]
```

## Python3

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, ch in enumerate(sentence):
            if ch == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return sentence[0] == sentence[-1]
```

## C

```c
#include <stdbool.h>

bool isCircularSentence(char* sentence) {
    if (!sentence) return false;
    int len = 0;
    while (sentence[len] != '\0') ++len;
    for (int i = 0; i < len; ++i) {
        if (sentence[i] == ' ') {
            if (sentence[i - 1] != sentence[i + 1]) return false;
        }
    }
    return sentence[0] == sentence[len - 1];
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsCircularSentence(string sentence)
    {
        int n = sentence.Length;
        for (int i = 0; i < n; i++)
        {
            if (sentence[i] == ' ')
            {
                // character before space is last of previous word,
                // character after space is first of next word
                if (sentence[i - 1] != sentence[i + 1])
                    return false;
            }
        }
        // check circular condition between last and first characters
        return sentence[0] == sentence[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    const n = sentence.length;
    for (let i = 0; i < n; i++) {
        if (sentence[i] === ' ') {
            if (sentence[i - 1] !== sentence[i + 1]) return false;
        }
    }
    return sentence[0] === sentence[n - 1];
};
```

## Typescript

```typescript
function isCircularSentence(sentence: string): boolean {
    const n = sentence.length;
    for (let i = 0; i < n; i++) {
        if (sentence[i] === ' ') {
            if (sentence[i - 1] !== sentence[i + 1]) return false;
        }
    }
    return sentence[0] === sentence[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $sentence
     * @return Boolean
     */
    function isCircularSentence($sentence) {
        $len = strlen($sentence);
        for ($i = 0; $i < $len; $i++) {
            if ($sentence[$i] === ' ') {
                // previous character and next character must match
                if ($sentence[$i - 1] !== $sentence[$i + 1]) {
                    return false;
                }
            }
        }
        // first and last characters must match
        return $sentence[0] === $sentence[$len - 1];
    }
}
```

## Swift

```swift
class Solution {
    func isCircularSentence(_ sentence: String) -> Bool {
        let chars = Array(sentence)
        for i in 0..<chars.count {
            if chars[i] == " " {
                // Since there are no leading/trailing spaces, i-1 and i+1 are valid indices
                if chars[i - 1] != chars[i + 1] {
                    return false
                }
            }
        }
        return chars.first == chars.last
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isCircularSentence(sentence: String): Boolean {
        val n = sentence.length
        for (i in 0 until n) {
            if (sentence[i] == ' ') {
                if (sentence[i - 1] != sentence[i + 1]) return false
            }
        }
        return sentence[0] == sentence[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  bool isCircularSentence(String sentence) {
    int n = sentence.length;
    for (int i = 0; i < n; ++i) {
      if (sentence[i] == ' ') {
        if (sentence[i - 1] != sentence[i + 1]) return false;
      }
    }
    return sentence[0] == sentence[n - 1];
  }
}
```

## Golang

```go
func isCircularSentence(sentence string) bool {
	n := len(sentence)
	for i := 0; i < n; i++ {
		if sentence[i] == ' ' {
			if sentence[i-1] != sentence[i+1] {
				return false
			}
		}
	}
	return sentence[0] == sentence[n-1]
}
```

## Ruby

```ruby
# @param {String} sentence
# @return {Boolean}
def is_circular_sentence(sentence)
  (0...sentence.length).each do |i|
    if sentence[i] == ' '
      return false unless sentence[i - 1] == sentence[i + 1]
    end
  end
  sentence[0] == sentence[-1]
end
```

## Scala

```scala
object Solution {
    def isCircularSentence(sentence: String): Boolean = {
        val n = sentence.length
        for (i <- 0 until n) {
            if (sentence(i) == ' ') {
                if (sentence(i - 1) != sentence(i + 1)) return false
            }
        }
        sentence(0) == sentence(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let bytes = sentence.as_bytes();
        for i in 0..bytes.len() {
            if bytes[i] == b' ' {
                // Since there are no leading/trailing spaces and words are separated by a single space,
                // it's safe to access i-1 and i+1.
                if bytes[i - 1] != bytes[i + 1] {
                    return false;
                }
            }
        }
        bytes[0] == *bytes.last().unwrap()
    }
}
```

## Racket

```racket
(define/contract (is-circular-sentence sentence)
  (-> string? boolean?)
  (let* ((n (string-length sentence))
         (first (string-ref sentence 0))
         (last (string-ref sentence (- n 1))))
    (if (not (char=? first last))
        #f
        (let loop ((i 0))
          (cond
            [(>= i n) #t]
            [(char=? (string-ref sentence i) #\space)
             (if (char=? (string-ref sentence (- i 1))
                         (string-ref sentence (+ i 1)))
                 (loop (+ i 1))
                 #f)]
            [else (loop (+ i 1))])))))
```

## Erlang

```erlang
-module(solution).
-export([is_circular_sentence/1]).

-spec is_circular_sentence(Sentence :: unicode:unicode_binary()) -> boolean().
is_circular_sentence(Sentence) ->
    List = binary_to_list(Sentence),
    case List of
        [] -> false;
        _ ->
            First = hd(List),
            Last  = lists:last(List),
            if First =/= Last ->
                    false;
               true ->
                    check_spaces(List)
            end
    end.

check_spaces([Prev, $ , Next | Rest]) when Prev =:= Next ->
    check_spaces([Next | Rest]);
check_spaces([_Prev, $ , _Next | _Rest]) ->
    false;
check_spaces([_ | Rest]) ->
    check_spaces(Rest);
check_spaces([]) ->
    true.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_circular_sentence(sentence :: String.t()) :: boolean()
  def is_circular_sentence(sentence) do
    words = String.split(sentence, " ")
    [first_word | rest] = words

    init_last = String.slice(first_word, -1..-1)

    result =
      Enum.reduce_while(rest, init_last, fn word, prev_last ->
        first_char = String.first(word)

        if first_char == prev_last do
          {:cont, String.slice(word, -1..-1)}
        else
          {:halt, :error}
        end
      end)

    case result do
      :error -> false
      final_last -> final_last == String.first(first_word)
    end
  end
end
```
