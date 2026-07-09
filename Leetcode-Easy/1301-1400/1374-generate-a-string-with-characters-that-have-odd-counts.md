# 1374. Generate a String With Characters That Have Odd Counts

## Cpp

```cpp
class Solution {
public:
    std::string generateTheString(int n) {
        if (n % 2 == 1) {
            return std::string(n, 'a');
        } else {
            return std::string(n - 1, 'a') + 'b';
        }
    }
};
```

## Java

```java
class Solution {
    public String generateTheString(int n) {
        StringBuilder sb = new StringBuilder(n);
        if (n % 2 == 1) {
            for (int i = 0; i < n; i++) {
                sb.append('a');
            }
        } else {
            for (int i = 0; i < n - 1; i++) {
                sb.append('a');
            }
            sb.append('b');
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'
```

## Python3

```python
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'
```

## C

```c
#include <stdlib.h>

char* generateTheString(int n) {
    char *s = (char*)malloc(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        s[i] = 'a';
    }
    if (n % 2 == 0) {
        s[n - 1] = 'b';
    } else {
        s[n - 1] = 'a';
    }
    s[n] = '\0';
    return s;
}
```

## Csharp

```csharp
public class Solution {
    public string GenerateTheString(int n) {
        if (n % 2 == 1) {
            return new string('a', n);
        } else {
            return new string('a', n - 1) + 'b';
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var generateTheString = function(n) {
    if (n % 2 === 1) {
        return 'a'.repeat(n);
    } else {
        return 'a'.repeat(n - 1) + 'b';
    }
};
```

## Typescript

```typescript
function generateTheString(n: number): string {
    if (n % 2 === 1) {
        return 'a'.repeat(n);
    } else {
        return 'a'.repeat(n - 1) + 'b';
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function generateTheString($n) {
        if ($n % 2 == 1) {
            return str_repeat('a', $n);
        } else {
            return str_repeat('a', $n - 1) . 'b';
        }
    }
}
```

## Swift

```swift
class Solution {
    func generateTheString(_ n: Int) -> String {
        if n % 2 == 1 {
            return String(repeating: "a", count: n)
        } else {
            var result = String(repeating: "a", count: n - 1)
            result.append("b")
            return result
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generateTheString(n: Int): String {
        val sb = StringBuilder()
        if (n % 2 == 1) {
            repeat(n) { sb.append('a') }
        } else {
            repeat(n - 1) { sb.append('a') }
            sb.append('b')
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String generateTheString(int n) {
    if (n % 2 == 1) {
      return List.filled(n, 'a').join();
    } else {
      return List.filled(n - 1, 'a').join() + 'b';
    }
  }
}
```

## Golang

```go
package main

import "strings"

func generateTheString(n int) string {
	if n%2 == 1 {
		return strings.Repeat("a", n)
	}
	var sb strings.Builder
	sb.Grow(n)
	sb.WriteString(strings.Repeat("a", n-1))
	sb.WriteByte('b')
	return sb.String()
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {String}
def generate_the_string(n)
  if n.odd?
    'a' * n
  else
    'a' * (n - 1) + 'b'
  end
end
```

## Scala

```scala
object Solution {
    def generateTheString(n: Int): String = {
        if (n % 2 == 1) "a" * n
        else "a" * (n - 1) + "b"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn generate_the_string(n: i32) -> String {
        let n = n as usize;
        if n % 2 == 1 {
            "a".repeat(n)
        } else {
            let mut s = "a".repeat(n - 1);
            s.push('b');
            s
        }
    }
}
```

## Racket

```racket
(define/contract (generate-the-string n)
  (-> exact-integer? string?)
  (if (odd? n)
      (make-string n #\a)
      (string-append (make-string (- n 1) #\a) "b")))
```

## Erlang

```erlang
-module(solution).
-export([generate_the_string/1]).

-spec generate_the_string(N :: integer()) -> unicode:unicode_binary().
generate_the_string(N) when N > 0 ->
    case N rem 2 of
        1 -> list_to_binary(lists:duplicate(N, $a));
        0 -> list_to_binary(lists:duplicate(N-1, $a) ++ [$b])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_the_string(n :: integer) :: String.t()
  def generate_the_string(n) do
    if rem(n, 2) == 1 do
      String.duplicate("a", n)
    else
      String.duplicate("a", n - 1) <> "b"
    end
  end
end
```
