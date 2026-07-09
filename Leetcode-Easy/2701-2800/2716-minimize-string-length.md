# 2716. Minimize String Length

## Cpp

```cpp
class Solution {
public:
    int minimizedStringLength(string s) {
        vector<bool> seen(26, false);
        for (char c : s) seen[c - 'a'] = true;
        int cnt = 0;
        for (bool b : seen) if (b) ++cnt;
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int minimizedStringLength(String s) {
        boolean[] seen = new boolean[26];
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (!seen[idx]) {
                seen[idx] = true;
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))
```

## Python3

```python
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
```

## C

```c
#include <stdbool.h>

int minimizedStringLength(char* s) {
    bool seen[26] = {false};
    int cnt = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int idx = s[i] - 'a';
        if (!seen[idx]) {
            seen[idx] = true;
            ++cnt;
        }
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimizedStringLength(string s)
    {
        var uniqueChars = new System.Collections.Generic.HashSet<char>();
        foreach (char c in s)
        {
            uniqueChars.Add(c);
        }
        return uniqueChars.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimizedStringLength = function(s) {
    return new Set(s).size;
};
```

## Typescript

```typescript
function minimizedStringLength(s: string): number {
    const uniq = new Set<string>();
    for (const ch of s) {
        uniq.add(ch);
    }
    return uniq.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimizedStringLength($s) {
        $unique = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $unique[$s[$i]] = true;
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func minimizedStringLength(_ s: String) -> Int {
        var uniqueChars = Set<Character>()
        for ch in s {
            uniqueChars.insert(ch)
        }
        return uniqueChars.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizedStringLength(s: String): Int {
        val seen = BooleanArray(26)
        var count = 0
        for (c in s) {
            val idx = c - 'a'
            if (!seen[idx]) {
                seen[idx] = true
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int minimizedStringLength(String s) {
    final Set<int> distinct = {};
    for (final int ch in s.codeUnits) {
      distinct.add(ch);
    }
    return distinct.length;
  }
}
```

## Golang

```go
func minimizedStringLength(s string) int {
	seen := [26]bool{}
	count := 0
	for i := 0; i < len(s); i++ {
		idx := s[i] - 'a'
		if !seen[idx] {
			seen[idx] = true
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def minimized_string_length(s)
  s.chars.uniq.size
end
```

## Scala

```scala
object Solution {
    def minimizedStringLength(s: String): Int = {
        s.toSet.size
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn minimized_string_length(s: String) -> i32 {
        let mut uniq = HashSet::new();
        for ch in s.chars() {
            uniq.insert(ch);
        }
        uniq.len() as i32
    }
}
```

## Racket

```racket
(define/contract (minimized-string-length s)
  (-> string? exact-integer?)
  (let* ((len (string-length s))
         (seen (make-vector 26 #f))
         (count 0))
    (for ([i (in-range len)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (when (not (vector-ref seen idx))
          (vector-set! seen idx #t)
          (set! count (+ count 1)))))
    count))
```

## Erlang

```erlang
-module(solution).
-export([minimized_string_length/1]).

-spec minimized_string_length(S :: unicode:unicode_binary()) -> integer().
minimized_string_length(S) ->
    length(lists:usort(binary:bin_to_list(S))).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimized_string_length(s :: String.t) :: integer
  def minimized_string_length(s) do
    s
    |> String.graphemes()
    |> MapSet.new()
    |> MapSet.size()
  end
end
```
