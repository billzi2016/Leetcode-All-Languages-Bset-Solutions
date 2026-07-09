# 2546. Apply Bitwise Operations to Make Strings Equal

## Cpp

```cpp
class Solution {
public:
    bool makeStringsEqual(string s, string target) {
        bool hasOneS = false, hasOneT = false;
        for (char c : s) if (c == '1') { hasOneS = true; break; }
        for (char c : target) if (c == '1') { hasOneT = true; break; }
        return hasOneS == hasOneT;
    }
};
```

## Java

```java
class Solution {
    public boolean makeStringsEqual(String s, String target) {
        boolean sHasOne = s.indexOf('1') != -1;
        boolean tHasOne = target.indexOf('1') != -1;
        return sHasOne == tHasOne;
    }
}
```

## Python

```python
class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        return ('1' in s) == ('1' in target)
```

## Python3

```python
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return ('1' in s) == ('1' in target)
```

## C

```c
#include <stdbool.h>

bool makeStringsEqual(char* s, char* target) {
    bool hasS = false, hasT = false;
    for (int i = 0; s[i] != '\0'; ++i) {
        if (s[i] == '1') {
            hasS = true;
            break;
        }
    }
    for (int i = 0; target[i] != '\0'; ++i) {
        if (target[i] == '1') {
            hasT = true;
            break;
        }
    }
    return hasS == hasT;
}
```

## Csharp

```csharp
public class Solution
{
    public bool MakeStringsEqual(string s, string target)
    {
        bool sHasOne = s.IndexOf('1') >= 0;
        bool tHasOne = target.IndexOf('1') >= 0;
        return sHasOne == tHasOne;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} target
 * @return {boolean}
 */
var makeStringsEqual = function(s, target) {
    const hasOneS = s.includes('1');
    const hasOneT = target.includes('1');
    return (hasOneS && hasOneT) || (!hasOneS && !hasOneT);
};
```

## Typescript

```typescript
function makeStringsEqual(s: string, target: string): boolean {
    const sHasOne = s.includes('1');
    const tHasOne = target.includes('1');
    return sHasOne === tHasOne;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $target
     * @return Boolean
     */
    function makeStringsEqual($s, $target) {
        $hasOneS = strpos($s, '1') !== false;
        $hasOneT = strpos($target, '1') !== false;
        return $hasOneS === $hasOneT;
    }
}
```

## Swift

```swift
class Solution {
    func makeStringsEqual(_ s: String, _ target: String) -> Bool {
        let hasOneS = s.contains("1")
        let hasOneT = target.contains("1")
        return hasOneS == hasOneT
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeStringsEqual(s: String, target: String): Boolean {
        val sHasOne = s.indexOf('1') >= 0
        val tHasOne = target.indexOf('1') >= 0
        return sHasOne == tHasOne
    }
}
```

## Dart

```dart
class Solution {
  bool makeStringsEqual(String s, String target) {
    bool hasOneS = s.contains('1');
    bool hasOneT = target.contains('1');
    return hasOneS == hasOneT;
  }
}
```

## Golang

```go
func makeStringsEqual(s string, target string) bool {
    hasOneS := false
    for i := 0; i < len(s); i++ {
        if s[i] == '1' {
            hasOneS = true
            break
        }
    }
    hasOneT := false
    for i := 0; i < len(target); i++ {
        if target[i] == '1' {
            hasOneT = true
            break
        }
    }
    return hasOneS == hasOneT
}
```

## Ruby

```ruby
def make_strings_equal(s, target)
  has_one_s = s.include?('1')
  has_one_t = target.include?('1')
  has_one_s == has_one_t
end
```

## Scala

```scala
object Solution {
    def makeStringsEqual(s: String, target: String): Boolean = {
        val hasOneS = s.contains('1')
        val hasOneT = target.contains('1')
        hasOneS == hasOneT
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_strings_equal(s: String, target: String) -> bool {
        let s_has_one = s.as_bytes().iter().any(|&c| c == b'1');
        let t_has_one = target.as_bytes().iter().any(|&c| c == b'1');
        s_has_one == t_has_one
    }
}
```

## Racket

```racket
(define/contract (make-strings-equal s target)
  (-> string? string? boolean?)
  (let ((s-one
         (let loop ((i 0) (n (string-length s)))
           (if (= i n)
               #f
               (if (char=? (string-ref s i) #\1)
                   #t
                   (loop (+ i 1) n)))))
        (t-one
         (let loop ((i 0) (n (string-length target)))
           (if (= i n)
               #f
               (if (char=? (string-ref target i) #\1)
                   #t
                   (loop (+ i 1) n))))))
    (equal? s-one t-one)))
```

## Erlang

```erlang
-spec make_strings_equal(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> boolean().
make_strings_equal(S, Target) ->
    HasS = has_one(S),
    HasT = has_one(Target),
    HasS == HasT.

has_one(Bin) ->
    case binary:match(Bin, <<"1">>) of
        {_, _} -> true;
        nomatch -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec make_strings_equal(s :: String.t(), target :: String.t()) :: boolean()
  def make_strings_equal(s, target) do
    String.contains?(s, "1") == String.contains?(target, "1")
  end
end
```
