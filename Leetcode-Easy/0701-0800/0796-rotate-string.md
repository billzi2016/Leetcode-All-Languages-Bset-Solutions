# 0796. Rotate String

## Cpp

```cpp
class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.size() != goal.size()) return false;
        string doubled = s + s;
        return doubled.find(goal) != string::npos;
    }
};
```

## Java

```java
class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        return (s + s).contains(goal);
    }
}
```

## Python

```python
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        return goal in (s + s)
```

## Python3

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool rotateString(char* s, char* goal) {
    size_t n = strlen(s);
    if (n != strlen(goal)) return false;

    char *doubled = (char *)malloc(2 * n + 1);
    if (!doubled) return false;

    memcpy(doubled, s, n);
    memcpy(doubled + n, s, n);
    doubled[2 * n] = '\0';

    bool result = strstr(doubled, goal) != NULL;
    free(doubled);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool RotateString(string s, string goal)
    {
        if (s.Length != goal.Length) return false;
        return (s + s).Contains(goal);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    if (s.length !== goal.length) return false;
    return (s + s).includes(goal);
};
```

## Typescript

```typescript
function rotateString(s: string, goal: string): boolean {
    if (s.length !== goal.length) return false;
    return (s + s).includes(goal);
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function rotateString($s, $goal) {
        if (strlen($s) !== strlen($goal)) {
            return false;
        }
        return strpos($s . $s, $goal) !== false;
    }
}
?>
```

## Swift

```swift
class Solution {
    func rotateString(_ s: String, _ goal: String) -> Bool {
        guard s.count == goal.count else { return false }
        let doubled = s + s
        return doubled.contains(goal)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rotateString(s: String, goal: String): Boolean {
        if (s.length != goal.length) return false
        return (s + s).contains(goal)
    }
}
```

## Dart

```dart
class Solution {
  bool rotateString(String s, String goal) {
    if (s.length != goal.length) return false;
    return (s + s).contains(goal);
  }
}
```

## Golang

```go
package main

import "strings"

func rotateString(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	return strings.Contains(s+s, goal)
}
```

## Ruby

```ruby
# @param {String} s
# @param {String} goal
# @return {Boolean}
def rotate_string(s, goal)
  return false unless s.length == goal.length
  (s + s).include?(goal)
end
```

## Scala

```scala
object Solution {
    def rotateString(s: String, goal: String): Boolean = {
        if (s.length != goal.length) false
        else (s + s).contains(goal)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false;
        }
        let doubled = format!("{}{}", s, s);
        doubled.contains(&goal)
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract)
(require racket/string)

(define/contract (rotate-string s goal)
  (-> string? string? boolean?)
  (if (not (= (string-length s) (string-length goal)))
      #false
      (let ([double (string-append s s)])
        (string-contains? double goal))))
```

## Erlang

```erlang
-spec rotate_string(S :: unicode:unicode_binary(), Goal :: unicode:unicode_binary()) -> boolean().
rotate_string(S, Goal) ->
    case byte_size(S) =:= byte_size(Goal) of
        false -> false;
        true ->
            Double = <<S/binary, S/binary>>,
            case binary:match(Double, Goal) of
                nomatch -> false;
                _Match  -> true
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec rotate_string(s :: String.t(), goal :: String.t()) :: boolean()
  def rotate_string(s, goal) do
    if byte_size(s) != byte_size(goal) do
      false
    else
      String.contains?(s <> s, goal)
    end
  end
end
```
