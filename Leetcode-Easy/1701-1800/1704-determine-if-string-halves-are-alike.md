# 1704. Determine if String Halves Are Alike

## Cpp

```cpp
class Solution {
public:
    bool halvesAreAlike(string s) {
        static const string vowels = "aeiouAEIOU";
        bool isVowel[256] = {false};
        for (char c : vowels) isVowel[(unsigned char)c] = true;
        
        int n = s.size();
        int half = n / 2;
        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < half; ++i) {
            if (isVowel[(unsigned char)s[i]]) ++cnt1;
            if (isVowel[(unsigned char)s[i + half]]) ++cnt2;
        }
        return cnt1 == cnt2;
    }
};
```

## Java

```java
class Solution {
    public boolean halvesAreAlike(String s) {
        int n = s.length();
        int half = n / 2;
        int diff = 0;
        for (int i = 0; i < half; i++) {
            if (isVowel(s.charAt(i))) diff++;
        }
        for (int i = half; i < n; i++) {
            if (isVowel(s.charAt(i))) diff--;
        }
        return diff == 0;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
```

## Python

```python
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        n = len(s) // 2
        count1 = sum(1 for ch in s[:n] if ch in vowels)
        count2 = sum(1 for ch in s[n:] if ch in vowels)
        return count1 == count2
```

## Python3

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        n = len(s) // 2
        count1 = sum(1 for ch in s[:n] if ch in vowels)
        count2 = sum(1 for ch in s[n:] if ch in vowels)
        return count1 == count2
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

static inline bool isVowel(char c) {
    char lower = (char)tolower((unsigned char)c);
    return lower == 'a' || lower == 'e' || lower == 'i' ||
           lower == 'o' || lower == 'u';
}

bool halvesAreAlike(char* s) {
    int len = strlen(s);
    int half = len / 2;
    int cnt1 = 0, cnt2 = 0;

    for (int i = 0; i < half; ++i) {
        if (isVowel(s[i])) cnt1++;
    }
    for (int i = half; i < len; ++i) {
        if (isVowel(s[i])) cnt2++;
    }

    return cnt1 == cnt2;
}
```

## Csharp

```csharp
public class Solution
{
    public bool HalvesAreAlike(string s)
    {
        int n = s.Length;
        int half = n / 2;
        int countFirst = 0, countSecond = 0;

        // Using a lookup for vowels (both lowercase and uppercase)
        var vowels = new System.Collections.Generic.HashSet<char>
        {
            'a','e','i','o','u',
            'A','E','I','O','U'
        };

        for (int i = 0; i < half; i++)
        {
            if (vowels.Contains(s[i])) countFirst++;
            if (vowels.Contains(s[i + half])) countSecond++;
        }

        return countFirst == countSecond;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    let count = 0;
    const n = s.length;
    for (let i = 0; i < n / 2; ++i) {
        if (vowels.has(s[i])) count++;
    }
    for (let i = n / 2; i < n; ++i) {
        if (vowels.has(s[i])) count--;
    }
    return count === 0;
};
```

## Typescript

```typescript
function halvesAreAlike(s: string): boolean {
    const vowels = new Set(['a','e','i','o','u','A','E','I','O','U']);
    const n = s.length >> 1;
    let diff = 0;
    for (let i = 0; i < n; ++i) {
        if (vowels.has(s[i])) diff++;
        if (vowels.has(s[i + n])) diff--;
    }
    return diff === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function halvesAreAlike($s) {
        $vowels = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $len = strlen($s);
        $mid = intdiv($len, 2);
        $balance = 0;
        for ($i = 0; $i < $mid; $i++) {
            if (isset($vowels[strtolower($s[$i])])) {
                $balance++;
            }
        }
        for ($i = $mid; $i < $len; $i++) {
            if (isset($vowels[strtolower($s[$i])])) {
                $balance--;
            }
        }
        return $balance === 0;
    }
}
```

## Swift

```swift
class Solution {
    func halvesAreAlike(_ s: String) -> Bool {
        let vowels: Set<Character> = ["a","e","i","o","u","A","E","I","O","U"]
        let chars = Array(s)
        let n = chars.count
        var countFirst = 0
        var countSecond = 0
        for i in 0..<(n/2) {
            if vowels.contains(chars[i]) { countFirst += 1 }
            if vowels.contains(chars[n - 1 - i]) { countSecond += 1 }
        }
        return countFirst == countSecond
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun halvesAreAlike(s: String): Boolean {
        val vowels = setOf('a','e','i','o','u','A','E','I','O','U')
        var count1 = 0
        var count2 = 0
        val n = s.length
        for (i in 0 until n / 2) {
            if (s[i] in vowels) count1++
            if (s[i + n / 2] in vowels) count2++
        }
        return count1 == count2
    }
}
```

## Dart

```dart
class Solution {
  bool halvesAreAlike(String s) {
    const vowels = 'aeiouAEIOU';
    int n = s.length;
    int mid = n ~/ 2;
    int countFirst = 0, countSecond = 0;

    for (int i = 0; i < mid; i++) {
      if (vowels.contains(s[i])) countFirst++;
    }
    for (int i = mid; i < n; i++) {
      if (vowels.contains(s[i])) countSecond++;
    }

    return countFirst == countSecond;
  }
}
```

## Golang

```go
func halvesAreAlike(s string) bool {
    n := len(s) / 2
    isVowel := func(c byte) bool {
        switch c {
        case 'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U':
            return true
        }
        return false
    }

    count1, count2 := 0, 0
    for i := 0; i < n; i++ {
        if isVowel(s[i]) {
            count1++
        }
        if isVowel(s[i+n]) {
            count2++
        }
    }
    return count1 == count2
}
```

## Ruby

```ruby
def halves_are_alike(s)
  mid = s.length / 2
  vowels = "aeiouAEIOU"
  s[0...mid].count(vowels) == s[mid..-1].count(vowels)
end
```

## Scala

```scala
object Solution {
    def halvesAreAlike(s: String): Boolean = {
        val vowels = Set('a','e','i','o','u','A','E','I','O','U')
        val n = s.length
        var count = 0
        for (i <- 0 until n / 2) {
            if (vowels.contains(s(i))) count += 1
            if (vowels.contains(s(i + n / 2))) count -= 1
        }
        count == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let bytes = s.as_bytes();
        let n = bytes.len() / 2;
        let mut cnt1 = 0;
        let mut cnt2 = 0;
        for i in 0..n {
            if matches!(bytes[i], b'a'|b'e'|b'i'|b'o'|b'u'|b'A'|b'E'|b'I'|b'O'|b'U') {
                cnt1 += 1;
            }
        }
        for i in n..bytes.len() {
            if matches!(bytes[i], b'a'|b'e'|b'i'|b'o'|b'u'|b'A'|b'E'|b'I'|b'O'|b'U') {
                cnt2 += 1;
            }
        }
        cnt1 == cnt2
    }
}
```

## Racket

```racket
(define/contract (halves-are-alike s)
  (-> string? boolean?)
  (let* ([len (string-length s)]
         [mid (/ len 2)])
    (define (vowel? ch)
      (member (char-downcase ch) '(#\a #\e #\i #\o #\u)))
    (define (count start end)
      (let loop ((i start) (cnt 0))
        (if (= i end)
            cnt
            (loop (add1 i)
                  (+ cnt (if (vowel? (string-ref s i)) 1 0))))))
    (= (count 0 mid) (count mid len))))
```

## Erlang

```erlang
-module(solution).
-export([halves_are_alike/1]).

-spec halves_are_alike(S :: unicode:unicode_binary()) -> boolean().
halves_are_alike(S) ->
    List = unicode:characters_to_list(S),
    N = length(List),
    Half = N div 2,
    {First, Second} = lists:split(Half, List),
    count_vowels(First) == count_vowels(Second).

count_vowels([]) -> 0;
count_vowels([H|T]) ->
    (if is_vowel(H) -> 1; true -> 0 end) + count_vowels(T).

is_vowel(C) -> lists:member(C, "aeiouAEIOU").
```

## Elixir

```elixir
defmodule Solution do
  @spec halves_are_alike(s :: String.t) :: boolean
  def halves_are_alike(s) do
    len = byte_size(s)
    half = div(len, 2)

    first = binary_part(s, 0, half)
    second = binary_part(s, half, half)

    count_vowels = fn segment ->
      segment
      |> String.downcase()
      |> String.graphemes()
      |> Enum.count(fn ch -> ch in ["a", "e", "i", "o", "u"] end)
    end

    count_vowels.(first) == count_vowels.(second)
  end
end
```
