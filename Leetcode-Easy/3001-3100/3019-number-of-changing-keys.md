# 3019. Number of Changing Keys

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countKeyChanges(string s) {
        int changes = 0;
        for (int i = 1; i < (int)s.size(); ++i) {
            if (tolower(s[i]) != tolower(s[i - 1])) {
                ++changes;
            }
        }
        return changes;
    }
};
```

## Java

```java
class Solution {
    public int countKeyChanges(String s) {
        int changes = 0;
        String lower = s.toLowerCase();
        for (int i = 1; i < lower.length(); i++) {
            if (lower.charAt(i) != lower.charAt(i - 1)) {
                changes++;
            }
        }
        return changes;
    }
}
```

## Python

```python
class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cnt = 0
        prev = s[0].lower()
        for ch in s[1:]:
            cur = ch.lower()
            if cur != prev:
                cnt += 1
            prev = cur
        return cnt
```

## Python3

```python
class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        cnt = 0
        prev = s[0].lower()
        for ch in s[1:]:
            cur = ch.lower()
            if cur != prev:
                cnt += 1
            prev = cur
        return cnt
```

## C

```c
#include <ctype.h>

int countKeyChanges(char* s) {
    if (!s || !s[0]) return 0;
    int changes = 0;
    char prev = tolower(s[0]);
    for (int i = 1; s[i] != '\0'; ++i) {
        char cur = tolower(s[i]);
        if (cur != prev) {
            ++changes;
        }
        prev = cur;
    }
    return changes;
}
```

## Csharp

```csharp
public class Solution {
    public int CountKeyChanges(string s) {
        int changes = 0;
        for (int i = 1; i < s.Length; i++) {
            if (char.ToLowerInvariant(s[i]) != char.ToLowerInvariant(s[i - 1])) {
                changes++;
            }
        }
        return changes;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countKeyChanges = function(s) {
    let cnt = 0;
    for (let i = 1; i < s.length; ++i) {
        if (s[i].toLowerCase() !== s[i - 1].toLowerCase()) cnt++;
    }
    return cnt;
};
```

## Typescript

```typescript
function countKeyChanges(s: string): number {
    let changes = 0;
    for (let i = 1; i < s.length; i++) {
        if (s[i].toLowerCase() !== s[i - 1].toLowerCase()) {
            changes++;
        }
    }
    return changes;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countKeyChanges($s) {
        $count = 0;
        $prev = null;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $curr = strtolower($s[$i]);
            if ($i > 0 && $curr !== $prev) {
                $count++;
            }
            $prev = $curr;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countKeyChanges(_ s: String) -> Int {
        var previous: Character? = nil
        var changes = 0
        for ch in s {
            let lowerChar = Character(ch.lowercased())
            if let prev = previous {
                if lowerChar != prev {
                    changes += 1
                }
            }
            previous = lowerChar
        }
        return changes
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countKeyChanges(s: String): Int {
        var changes = 0
        var prev = s[0].lowercaseChar()
        for (i in 1 until s.length) {
            val cur = s[i].lowercaseChar()
            if (cur != prev) {
                changes++
                prev = cur
            }
        }
        return changes
    }
}
```

## Dart

```dart
class Solution {
  int countKeyChanges(String s) {
    if (s.isEmpty) return 0;
    int changes = 0;
    String prev = s[0].toLowerCase();
    for (int i = 1; i < s.length; ++i) {
      String cur = s[i].toLowerCase();
      if (cur != prev) {
        changes++;
        prev = cur;
      }
    }
    return changes;
  }
}
```

## Golang

```go
func countKeyChanges(s string) int {
	if len(s) == 0 {
		return 0
	}
	cnt := 0
	prev := s[0] | 32 // convert to lowercase (ASCII)
	for i := 1; i < len(s); i++ {
		cur := s[i] | 32
		if cur != prev {
			cnt++
		}
		prev = cur
	}
	return cnt
}
```

## Ruby

```ruby
def count_key_changes(s)
  lower = s.downcase
  count = 0
  (1...lower.length).each do |i|
    count += 1 if lower[i] != lower[i - 1]
  end
  count
end
```

## Scala

```scala
object Solution {
    def countKeyChanges(s: String): Int = {
        if (s.isEmpty) return 0
        var changes = 0
        var prev = s.charAt(0).toLower
        for (i <- 1 until s.length) {
            val cur = s.charAt(i).toLower
            if (cur != prev) changes += 1
            prev = cur
        }
        changes
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_key_changes(s: String) -> i32 {
        let mut prev: Option<char> = None;
        let mut changes = 0i32;
        for ch in s.chars() {
            let cur = ch.to_ascii_lowercase();
            if let Some(p) = prev {
                if p != cur {
                    changes += 1;
                }
            }
            prev = Some(cur);
        }
        changes
    }
}
```

## Racket

```racket
(define/contract (count-key-changes s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (if (= n 0)
        0
        (let loop ((i 1)
                   (prev (char-downcase (string-ref s 0)))
                   (acc 0))
          (if (>= i n)
              acc
              (let ((curr (char-downcase (string-ref s i))))
                (loop (+ i 1) curr (if (char=? curr prev) acc (+ acc 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_key_changes/1]).

-spec count_key_changes(S :: unicode:unicode_binary()) -> integer().
count_key_changes(S) ->
    Lower = string:lowercase(S),
    Chars = unicode:characters_to_list(Lower),
    count_changes(Chars, undefined, 0).

count_changes([], _Prev, Acc) -> Acc;
count_changes([H|T], undefined, Acc) ->
    count_changes(T, H, Acc);
count_changes([H|T], Prev, Acc) when H =/= Prev ->
    count_changes(T, H, Acc + 1);
count_changes([H|T], Prev, Acc) ->
    count_changes(T, H, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_key_changes(s :: String.t()) :: integer()
  def count_key_changes(s) do
    s
    |> String.downcase()
    |> String.graphemes()
    |> Enum.reduce({0, nil}, fn ch, {cnt, prev} ->
      if prev == nil or prev == ch do
        {cnt, ch}
      else
        {cnt + 1, ch}
      end
    end)
    |> elem(0)
  end
end
```
