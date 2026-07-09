# 1880. Check if Word Equals Summation of Two Words

## Cpp

```cpp
class Solution {
public:
    bool isSumEqual(string firstWord, string secondWord, string targetWord) {
        auto toNum = [](const string& s) {
            int val = 0;
            for (char c : s) {
                val = val * 10 + (c - 'a');
            }
            return val;
        };
        int a = toNum(firstWord);
        int b = toNum(secondWord);
        int t = toNum(targetWord);
        return a + b == t;
    }
};
```

## Java

```java
class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        return wordToInt(firstWord) + wordToInt(secondWord) == wordToInt(targetWord);
    }
    
    private int wordToInt(String word) {
        int num = 0;
        for (int i = 0; i < word.length(); i++) {
            num = num * 10 + (word.charAt(i) - 'a');
        }
        return num;
    }
}
```

## Python

```python
class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def value(word):
            return int(''.join(str(ord(c) - ord('a')) for c in word))
        return value(firstWord) + value(secondWord) == value(targetWord)
```

## Python3

```python
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def to_int(word: str) -> int:
            num = 0
            for ch in word:
                num = num * 10 + (ord(ch) - ord('a'))
            return num

        return to_int(firstWord) + to_int(secondWord) == to_int(targetWord)
```

## C

```c
#include <stdbool.h>

static long long wordValue(const char *s) {
    long long v = 0;
    while (*s) {
        v = v * 10 + (*s - 'a');
        s++;
    }
    return v;
}

bool isSumEqual(char* firstWord, char* secondWord, char* targetWord) {
    long long a = wordValue(firstWord);
    long long b = wordValue(secondWord);
    long long c = wordValue(targetWord);
    return (a + b) == c;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsSumEqual(string firstWord, string secondWord, string targetWord) {
        long a = ToNumber(firstWord);
        long b = ToNumber(secondWord);
        long c = ToNumber(targetWord);
        return a + b == c;
    }

    private long ToNumber(string s) {
        long num = 0;
        foreach (char ch in s) {
            int digit = ch - 'a';
            num = num * 10 + digit;
        }
        return num;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function(firstWord, secondWord, targetWord) {
    const toNumber = (word) => {
        let numStr = '';
        for (let i = 0; i < word.length; ++i) {
            numStr += word.charCodeAt(i) - 97;
        }
        return Number(numStr);
    };
    
    const a = toNumber(firstWord);
    const b = toNumber(secondWord);
    const c = toNumber(targetWord);
    
    return a + b === c;
};
```

## Typescript

```typescript
function isSumEqual(firstWord: string, secondWord: string, targetWord: string): boolean {
    const toNum = (w: string): number => {
        let s = '';
        for (const ch of w) {
            s += (ch.charCodeAt(0) - 97).toString();
        }
        return Number(s);
    };
    return toNum(firstWord) + toNum(secondWord) === toNum(targetWord);
}
```

## Php

```php
class Solution {

    /**
     * @param String $firstWord
     * @param String $secondWord
     * @param String $targetWord
     * @return Boolean
     */
    function isSumEqual($firstWord, $secondWord, $targetWord) {
        $toNumber = function(string $word): int {
            $num = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $digit = ord($word[$i]) - ord('a');
                $num = $num * 10 + $digit;
            }
            return $num;
        };
        
        $firstVal = $toNumber($firstWord);
        $secondVal = $toNumber($secondWord);
        $targetVal = $toNumber($targetWord);
        
        return ($firstVal + $secondVal) === $targetVal;
    }
}
```

## Swift

```swift
class Solution {
    func isSumEqual(_ firstWord: String, _ secondWord: String, _ targetWord: String) -> Bool {
        func value(of word: String) -> Int {
            var result = 0
            for scalar in word.unicodeScalars {
                let digit = Int(scalar.value - UnicodeScalar("a").value)
                result = result * 10 + digit
            }
            return result
        }
        
        let sum = value(of: firstWord) + value(of: secondWord)
        return sum == value(of: targetWord)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean {
        fun value(word: String): Int {
            var num = 0
            for (c in word) {
                num = num * 10 + (c - 'a')
            }
            return num
        }
        val sum = value(firstWord) + value(secondWord)
        return sum == value(targetWord)
    }
}
```

## Dart

```dart
class Solution {
  bool isSumEqual(String firstWord, String secondWord, String targetWord) {
    int value(String s) {
      int num = 0;
      for (int i = 0; i < s.length; i++) {
        num = num * 10 + (s.codeUnitAt(i) - 'a'.codeUnitAt(0));
      }
      return num;
    }

    return value(firstWord) + value(secondWord) == value(targetWord);
  }
}
```

## Golang

```go
func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
	convert := func(s string) int {
		num := 0
		for _, ch := range s {
			num = num*10 + int(ch-'a')
		}
		return num
	}
	return convert(firstWord)+convert(secondWord) == convert(targetWord)
}
```

## Ruby

```ruby
def is_sum_equal(first_word, second_word, target_word)
  convert = ->(w) { w.each_char.map { |c| (c.ord - 97).to_s }.join.to_i }
  convert.call(first_word) + convert.call(second_word) == convert.call(target_word)
end
```

## Scala

```scala
object Solution {
    def isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean = {
        def toNumber(s: String): Long = {
            var num = 0L
            for (c <- s) {
                num = num * 10 + (c - 'a')
            }
            num
        }
        toNumber(firstWord) + toNumber(secondWord) == toNumber(targetWord)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        fn to_number(s: &str) -> i32 {
            let mut num = 0;
            for b in s.bytes() {
                num = num * 10 + (b - b'a') as i32;
            }
            num
        }

        to_number(&first_word) + to_number(&second_word) == to_number(&target_word)
    }
}
```

## Racket

```racket
(define/contract (is-sum-equal firstWord secondWord targetWord)
  (-> string? string? string? boolean?)
  (let ([value
         (lambda (s)
           (for/fold ([acc 0]) ([ch (in-string s)])
             (+ (* acc 10) (- (char->integer ch) (char->integer #\a)))) )])
    (= (+ (value firstWord) (value secondWord)) (value targetWord))))
```

## Erlang

```erlang
-module(solution).
-export([is_sum_equal/3]).

-spec is_sum_equal(FirstWord :: unicode:unicode_binary(), SecondWord :: unicode:unicode_binary(), TargetWord :: unicode:unicode_binary()) -> boolean().
is_sum_equal(FirstWord, SecondWord, TargetWord) ->
    V1 = word_value(FirstWord),
    V2 = word_value(SecondWord),
    VT = word_value(TargetWord),
    V1 + V2 == VT.

-spec word_value(unicode:unicode_binary()) -> integer().
word_value(Bin) -> word_value(Bin, 0).

-spec word_value(unicode:unicode_binary(), integer()) -> integer().
word_value(<<>>, Acc) -> Acc;
word_value(<<C, Rest/binary>>, Acc) ->
    Digit = C - $a,
    word_value(Rest, Acc * 10 + Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_sum_equal(first_word :: String.t, second_word :: String.t, target_word :: String.t) :: boolean
  def is_sum_equal(first_word, second_word, target_word) do
    to_int = fn word ->
      word
      |> String.to_charlist()
      |> Enum.reduce(0, fn ch, acc -> acc * 10 + (ch - ?a) end)
    end

    first_val = to_int.(first_word)
    second_val = to_int.(second_word)
    target_val = to_int.(target_word)

    first_val + second_val == target_val
  end
end
```
