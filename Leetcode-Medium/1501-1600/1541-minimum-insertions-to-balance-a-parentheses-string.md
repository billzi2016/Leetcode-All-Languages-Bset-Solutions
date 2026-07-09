# 1541. Minimum Insertions to Balance a Parentheses String

## Cpp

```cpp
class Solution {
public:
    int minInsertions(string s) {
        int ans = 0;
        int need = 0; // number of ')' needed
        for (char c : s) {
            if (c == '(') {
                need += 2;
                if (need % 2) { // odd, we have a single ')'
                    ++ans;      // insert one ')'
                    --need;     // now need is even
                }
            } else { // c == ')'
                --need;
                if (need < 0) {
                    ++ans;   // insert '(' before this ')'
                    need = 1; // this ')' counts as first of a pair, need one more ')'
                }
            }
        }
        return ans + need;
    }
};
```

## Java

```java
class Solution {
    public int minInsertions(String s) {
        int insertions = 0;
        int need = 0; // number of ')' needed
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (c == '(') {
                if ((need & 1) == 1) { // odd need, fix a missing ')'
                    insertions++;
                    need--;
                }
                need += 2;
            } else { // ')'
                need--;
                if (need < 0) {
                    insertions++; // insert '(' before this ')'
                    need = 1;    // this ')' counts as first of a pair
                }
            }
        }
        insertions += need / 2;
        return insertions;
    }
}
```

## Python

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0          # insertions performed so far
        need = 0         # number of ')' needed to balance current '('
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                need += 2
                # if we have an odd need, insert one ')'
                if need % 2 == 1:
                    ans += 1
                    need -= 1
                i += 1
            else:  # ')'
                need -= 1
                if need < 0:
                    # need a '(' before this ')'
                    ans += 1
                    need = 1   # after inserting '(', we still need one more ')'
                i += 1
        return ans + need
```

## Python3

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0
        for c in s:
            if c == '(':
                if need % 2 == 1:
                    ans += 1
                    need -= 1
                need += 2
            else:  # ')'
                need -= 1
                if need < 0:
                    ans += 1
                    need = 1
        return ans + need
```

## C

```c
int minInsertions(char* s) {
    int ans = 0;
    int need = 0; // number of ')' required
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '(') {
            need += 2;
            if (need % 2 == 1) { // odd, insert one ')'
                ans++;
                need--;
            }
        } else { // ')'
            need--;
            if (need == -1) {
                ans++;      // insert '('
                need = 1;   // after using current ')', we still need one more ')'
            }
        }
    }
    ans += need;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinInsertions(string s) {
        int insertions = 0;
        int need = 0; // number of ')' needed
        
        foreach (char c in s) {
            if (c == '(') {
                need += 2;
                if ((need & 1) == 1) { // odd, we have a single pending ')'
                    insertions++;
                    need--; // add one ')' to make it even
                }
            } else { // c == ')'
                need--;
                if (need < 0) {
                    insertions++; // insert '(' before this ')'
                    need = 1;    // this ')' counts as the first of a pair
                }
            }
        }
        
        return insertions + need;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    let insertions = 0;
    let need = 0; // number of ')' needed to balance current '('
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '(') {
            if (need % 2 === 1) {
                // previous '(' had one unmatched ')', insert another ')'
                insertions += 1;
                need -= 1;
            }
            need += 2; // each '(' expects two ')'
        } else { // s[i] === ')'
            need -= 1;
            if (need < 0) {
                // no matching '(', insert one
                insertions += 1;
                // after inserting '(', we have used this ')' as the first of its pair
                need = 1;
            }
        }
    }
    return insertions + need;
};
```

## Typescript

```typescript
function minInsertions(s: string): number {
    let ans = 0;
    let need = 0; // number of ')' needed
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '(') {
            need += 2;
            if (need % 2 === 1) {
                ans++;      // insert one ')'
                need--;     // now need is even
            }
        } else { // ')'
            need--;
            if (need < 0) {
                ans++;      // insert '(' before this ')'
                need = 1;   // after insertion, we still need one more ')'
            }
        }
    }
    return ans + need;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minInsertions($s) {
        $need = 0; // number of ')' needed to balance current '('
        $ans = 0;  // insertions performed
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === '(') {
                $need += 2;
                // if need is odd, we have a stray ')', insert one ')' to make it even
                if ($need % 2 == 1) {
                    $ans++;
                    $need--;
                }
            } else { // ')'
                $need--;
                if ($need < 0) {
                    // need an extra '(' before this ')'
                    $ans++;
                    // current ')' counts as first of a pair, so we still need one more ')'
                    $need = 1;
                }
            }
        }
        return $ans + $need;
    }
}
```

## Swift

```swift
class Solution {
    func minInsertions(_ s: String) -> Int {
        var insertions = 0
        var need = 0   // number of ')' needed to balance
        
        for ch in s {
            if ch == "(" {
                need += 2
                if need % 2 == 1 {
                    // we have an odd need, insert one ')'
                    insertions += 1
                    need -= 1
                }
            } else { // ch == ")"
                need -= 1
                if need < 0 {
                    // need a '(' before this ')'
                    insertions += 1
                    need = 1   // current ')' counts as first of a pair
                }
            }
        }
        
        return insertions + need
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minInsertions(s: String): Int {
        var insertions = 0
        var neededClosings = 0
        for (ch in s) {
            if (ch == '(') {
                neededClosings += 2
                if (neededClosings % 2 == 1) {
                    // Insert one ')' to balance the previous unmatched ')'
                    insertions++
                    neededClosings--
                }
            } else { // ch == ')'
                neededClosings--
                if (neededClosings < 0) {
                    // Need an extra '(' before this ')'
                    insertions++
                    neededClosings = 1
                }
            }
        }
        return insertions + neededClosings
    }
}
```

## Dart

```dart
class Solution {
  int minInsertions(String s) {
    int insertions = 0;
    int need = 0; // number of ')' needed
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        need += 2;
        if (need % 2 == 1) {
          insertions++;
          need--;
        }
      } else { // ')'
        need--;
        if (need < 0) {
          insertions++;
          need = 1; // this ')' counts as the first of a needed pair
        }
      }
    }
    return insertions + need;
  }
}
```

## Golang

```go
func minInsertions(s string) int {
	need, ans := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			need += 2
			if need%2 == 1 {
				ans++
				need--
			}
		} else { // ')'
			need--
			if need < 0 {
				ans++
				need = 1
			}
		}
	}
	return ans + need
}
```

## Ruby

```ruby
def min_insertions(s)
  ans = 0
  need = 0
  s.each_char do |c|
    if c == '('
      need += 2
      if need.odd?
        ans += 1
        need -= 1
      end
    else
      need -= 1
      if need < 0
        ans += 1
        need = 1
      end
    end
  end
  ans + need
end
```

## Scala

```scala
object Solution {
    def minInsertions(s: String): Int = {
        var insertions = 0
        var need = 0 // number of ')' needed to balance current '('

        var i = 0
        while (i < s.length) {
            val c = s.charAt(i)
            if (c == '(') {
                need += 2
                if (need % 2 == 1) { // odd need means we have an extra ')'
                    insertions += 1   // insert one ')'
                    need -= 1         // that ')' satisfies part of the need
                }
            } else { // c == ')'
                need -= 1
                if (need < 0) {
                    insertions += 1   // insert a '(' before this ')'
                    need = 1          // after insertion, we still need one more ')'
                }
            }
            i += 1
        }

        insertions + need
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let mut need: i32 = 0;
        let mut ans: i32 = 0;
        for ch in s.chars() {
            if ch == '(' {
                if need % 2 == 1 {
                    ans += 1;
                    need -= 1;
                }
                need += 2;
            } else { // ')'
                need -= 1;
                if need < 0 {
                    ans += 1;
                    need = 1;
                }
            }
        }
        ans + need
    }
}
```

## Racket

```racket
(define/contract (min-insertions s)
  (-> string? exact-integer?)
  (let ([ans 0]
        [need 0])
    (for ([i (in-range (string-length s))])
      (define c (string-ref s i))
      (cond
        [(char=? c #\()
         (when (odd? need)
           (set! ans (+ ans 1))
           (set! need (- need 1))) ; fix the dangling single ')'
         (set! need (+ need 2))]
        [(char=? c #\))
         (set! need (- need 1))
         (when (< need 0)
           (set! ans (+ ans 1))   ; insert a '('
           (set! need 1))]))      ; now we need one more ')'
    (+ ans need)))
```

## Erlang

```erlang
-module(solution).
-export([min_insertions/1]).

-spec min_insertions(S :: unicode:unicode_binary()) -> integer().
min_insertions(S) ->
    {Ans, Need} = loop(S, 0, 0),
    Ans + Need.

loop(<<>>, Ans, Need) ->
    {Ans, Need};
loop(<<$(, Rest/binary>>, Ans, Need) ->
    NewNeed = Need + 2,
    case NewNeed rem 2 of
        1 -> loop(Rest, Ans + 1, NewNeed - 1);
        _ -> loop(Rest, Ans, NewNeed)
    end;
loop(<<$), Rest/binary>>, Ans, Need) ->
    NewNeed = Need - 1,
    if
        NewNeed < 0 ->
            loop(Rest, Ans + 1, 1);
        true ->
            loop(Rest, Ans, NewNeed)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_insertions(String.t()) :: integer()
  def min_insertions(s) do
    {ans, need} =
      String.graphemes(s)
      |> Enum.reduce({0, 0}, fn ch, {ans, need} ->
        case ch do
          "(" ->
            new_need = need + 2

            if rem(new_need, 2) == 1 do
              # Insert one ')' to make the needed count even
              {ans + 1, new_need - 1}
            else
              {ans, new_need}
            end

          ")" ->
            new_need = need - 1

            if new_need < 0 do
              # Insert a '(' before this ')'
              {ans + 1, 1}
            else
              {ans, new_need}
            end
        end
      end)

    ans + need
  end
end
```
