# 2063. Vowels of All Substrings

## Cpp

```cpp
class Solution {
public:
    long long countVowels(string word) {
        const string vowels = "aeiou";
        unordered_set<char> vowSet(vowels.begin(), vowels.end());
        long long n = word.size();
        long long ans = 0;
        for (long long i = 0; i < n; ++i) {
            if (vowSet.count(word[i])) {
                ans += (i + 1) * (n - i);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countVowels(String word) {
        long total = 0;
        int n = word.length();
        for (int i = 0; i < n; i++) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                long left = i + 1L;
                long right = n - i;
                total += left * right;
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        total = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                total += (i + 1) * (n - i)
        return total
```

## Python3

```python
class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        total = 0
        for i, ch in enumerate(word):
            if ch in vowels:
                total += (i + 1) * (n - i)
        return total
```

## C

```c
#include <string.h>

static int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

long long countVowels(char* word) {
    long long total = 0;
    size_t n = strlen(word);
    for (size_t i = 0; i < n; ++i) {
        if (isVowel(word[i])) {
            total += (long long)(i + 1) * (long long)(n - i);
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public long CountVowels(string word)
    {
        long total = 0;
        int n = word.Length;
        for (int i = 0; i < n; i++)
        {
            char c = word[i];
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            {
                total += ((long)(i + 1)) * (n - i);
            }
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
var countVowels = function(word) {
    const n = word.length;
    let total = 0;
    const vowels = new Set(['a','e','i','o','u']);
    for (let i = 0; i < n; i++) {
        if (vowels.has(word[i])) {
            total += (i + 1) * (n - i);
        }
    }
    return total;
};
```

## Typescript

```typescript
function countVowels(word: string): number {
    const n = word.length;
    let total = 0;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    for (let i = 0; i < n; i++) {
        if (vowels.has(word[i])) {
            total += (i + 1) * (n - i);
        }
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
    function countVowels($word) {
        $n = strlen($word);
        $vowelSet = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $total = 0;
        for ($i = 0; $i < $n; $i++) {
            if (isset($vowelSet[$word[$i]])) {
                $total += ($i + 1) * ($n - $i);
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func countVowels(_ word: String) -> Int {
        let vowels: Set<Character> = ["a","e","i","o","u"]
        let n = word.count
        var total: Int64 = 0
        for (i, ch) in word.enumerated() {
            if vowels.contains(ch) {
                let left = Int64(i + 1)
                let right = Int64(n - i)
                total += left * right
            }
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countVowels(word: String): Long {
        val n = word.length
        var total = 0L
        for (i in word.indices) {
            when (word[i]) {
                'a', 'e', 'i', 'o', 'u' -> {
                    val left = i + 1L
                    val right = (n - i).toLong()
                    total += left * right
                }
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int countVowels(String word) {
    const vowels = {'a', 'e', 'i', 'o', 'u'};
    int n = word.length;
    int total = 0;
    for (int i = 0; i < n; i++) {
      if (vowels.contains(word[i])) {
        total += (i + 1) * (n - i);
      }
    }
    return total;
  }
}
```

## Golang

```go
func countVowels(word string) int64 {
	n := len(word)
	var total int64
	for i := 0; i < n; i++ {
		switch word[i] {
		case 'a', 'e', 'i', 'o', 'u':
			left := int64(i + 1)
			right := int64(n - i)
			total += left * right
		}
	}
	return total
}
```

## Ruby

```ruby
def count_vowels(word)
  total = 0
  n = word.length
  vowels = 'aeiou'
  word.each_char.with_index do |c, i|
    if vowels.include?(c)
      total += (i + 1) * (n - i)
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def countVowels(word: String): Long = {
        val n = word.length
        var total: Long = 0L
        for (i <- 0 until n) {
            word.charAt(i) match {
                case 'a' | 'e' | 'i' | 'o' | 'u' =>
                    total += (i + 1).toLong * (n - i).toLong
                case _ => // do nothing
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_vowels(word: String) -> i64 {
        let n = word.len() as i64;
        let mut total: i64 = 0;
        for (i, ch) in word.bytes().enumerate() {
            if matches!(ch, b'a' | b'e' | b'i' | b'o' | b'u') {
                let idx = i as i64 + 1;
                total += idx * (n - i as i64);
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (count-vowels word)
  (-> string? exact-integer?)
  (let* ((len (string-length word))
         (vowels '(#\a #\e #\i #\o #\u)))
    (let loop ((i 0) (total 0))
      (if (= i len)
          total
          (let ((ch (string-ref word i)))
            (loop (+ i 1)
                  (if (member ch vowels)
                      (+ total (* (+ i 1) (- len i)))
                      total)))))))
```

## Erlang

```erlang
-spec count_vowels(Word :: unicode:unicode_binary()) -> integer().
count_vowels(Word) ->
    N = byte_size(Word),
    count_vowels(Word, 0, N, 0).

count_vowels(<<>>, _Idx, _N, Acc) ->
    Acc;
count_vowels(<<C:8, Rest/binary>>, Idx, N, Acc) ->
    NewAcc = case is_vowel(C) of
        true -> Acc + (Idx + 1) * (N - Idx);
        false -> Acc
    end,
    count_vowels(Rest, Idx + 1, N, NewAcc).

is_vowel($a) -> true;
is_vowel($e) -> true;
is_vowel($i) -> true;
is_vowel($o) -> true;
is_vowel($u) -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_vowels(word :: String.t()) :: integer()
  def count_vowels(word) do
    n = byte_size(word)
    vowels = MapSet.new('aeiou')

    :binary.bin_to_list(word)
    |> Enum.with_index()
    |> Enum.reduce(0, fn {c, i}, acc ->
      if MapSet.member?(vowels, c) do
        acc + (i + 1) * (n - i)
      else
        acc
      end
    end)
  end
end
```
