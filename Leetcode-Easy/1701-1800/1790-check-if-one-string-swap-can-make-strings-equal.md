# 1790. Check if One String Swap Can Make Strings Equal

## Cpp

```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> diff;
        for (int i = 0; i < (int)s1.size(); ++i) {
            if (s1[i] != s2[i]) {
                diff.push_back(i);
                if (diff.size() > 2) return false;
            }
        }
        if (diff.empty()) return true;
        if (diff.size() != 2) return false;
        return s1[diff[0]] == s2[diff[1]] && s1[diff[1]] == s2[diff[0]];
    }
};
```

## Java

```java
class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int n = s1.length();
        int first = -1, second = -1;
        for (int i = 0; i < n; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (first == -1) {
                    first = i;
                } else if (second == -1) {
                    second = i;
                } else {
                    return false; // more than two differences
                }
            }
        }
        if (first == -1) {
            return true; // strings are already equal
        }
        if (second == -1) {
            return false; // only one difference cannot be fixed with a single swap
        }
        return s1.charAt(first) == s2.charAt(second) && s1.charAt(second) == s2.charAt(first);
    }
}
```

## Python

```python
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        if not diffs:
            return True
        if len(diffs) != 2:
            return False
        i, j = diffs[0], diffs[1]
        return s1[i] == s2[j] and s1[j] == s2[i]
```

## Python3

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        if not diffs:
            return True
        return len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool areAlmostEqual(char* s1, char* s2) {
    int len = strlen(s1);
    int diffCount = 0;
    int first = -1, second = -1;
    for (int i = 0; i < len; ++i) {
        if (s1[i] != s2[i]) {
            if (diffCount == 0) first = i;
            else if (diffCount == 1) second = i;
            diffCount++;
            if (diffCount > 2) return false;
        }
    }
    if (diffCount == 0) return true;
    if (diffCount != 2) return false;
    return s1[first] == s2[second] && s1[second] == s2[first];
}
```

## Csharp

```csharp
public class Solution
{
    public bool AreAlmostEqual(string s1, string s2)
    {
        int first = -1, second = -1;
        for (int i = 0; i < s1.Length; i++)
        {
            if (s1[i] != s2[i])
            {
                if (first == -1)
                    first = i;
                else if (second == -1)
                    second = i;
                else
                    return false; // more than two differences
            }
        }

        if (first == -1) // strings are already equal
            return true;

        if (second != -1 && s1[first] == s2[second] && s1[second] == s2[first])
            return true;

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    const n = s1.length;
    const diffs = [];
    for (let i = 0; i < n; i++) {
        if (s1[i] !== s2[i]) {
            diffs.push(i);
            if (diffs.length > 2) return false;
        }
    }
    if (diffs.length === 0) return true;
    if (diffs.length === 2) {
        const [i, j] = diffs;
        return s1[i] === s2[j] && s1[j] === s2[i];
    }
    return false;
};
```

## Typescript

```typescript
function areAlmostEqual(s1: string, s2: string): boolean {
    if (s1 === s2) return true;
    let first = -1, second = -1;
    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[i]) {
            if (first === -1) {
                first = i;
            } else if (second === -1) {
                second = i;
            } else {
                return false;
            }
        }
    }
    if (second === -1) return false;
    return s1[first] === s2[second] && s1[second] === s2[first];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function areAlmostEqual($s1, $s2) {
        $len = strlen($s1);
        $diff = [];

        for ($i = 0; $i < $len; $i++) {
            if ($s1[$i] !== $s2[$i]) {
                $diff[] = $i;
                if (count($diff) > 2) {
                    return false;
                }
            }
        }

        $cnt = count($diff);
        if ($cnt === 0) {
            return true;
        }
        if ($cnt !== 2) {
            return false;
        }

        return $s1[$diff[0]] === $s2[$diff[1]] && $s1[$diff[1]] === $s2[$diff[0]];
    }
}
```

## Swift

```swift
class Solution {
    func areAlmostEqual(_ s1: String, _ s2: String) -> Bool {
        if s1 == s2 { return true }
        let a = Array(s1)
        let b = Array(s2)
        var diffs: [Int] = []
        for i in 0..<a.count {
            if a[i] != b[i] {
                diffs.append(i)
                if diffs.count > 2 { return false }
            }
        }
        if diffs.count != 2 { return false }
        let i = diffs[0], j = diffs[1]
        return a[i] == b[j] && a[j] == b[i]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun areAlmostEqual(s1: String, s2: String): Boolean {
        if (s1 == s2) return true
        var first = -1
        var second = -1
        for (i in s1.indices) {
            if (s1[i] != s2[i]) {
                when {
                    first == -1 -> first = i
                    second == -1 -> second = i
                    else -> return false
                }
            }
        }
        if (second == -1) return false
        return s1[first] == s2[second] && s1[second] == s2[first]
    }
}
```

## Dart

```dart
class Solution {
  bool areAlmostEqual(String s1, String s2) {
    int n = s1.length;
    int diffCount = 0;
    int first = -1;
    int second = -1;

    for (int i = 0; i < n; i++) {
      if (s1[i] != s2[i]) {
        diffCount++;
        if (diffCount == 1) {
          first = i;
        } else if (diffCount == 2) {
          second = i;
        } else {
          return false;
        }
      }
    }

    if (diffCount == 0) return true;
    if (diffCount != 2) return false;

    return s1[first] == s2[second] && s1[second] == s2[first];
  }
}
```

## Golang

```go
func areAlmostEqual(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	var diff []int
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			diff = append(diff, i)
			if len(diff) > 2 {
				return false
			}
		}
	}
	if len(diff) == 0 {
		return true
	}
	if len(diff) != 2 {
		return false
	}
	i, j := diff[0], diff[1]
	return s1[i] == s2[j] && s1[j] == s2[i]
}
```

## Ruby

```ruby
def are_almost_equal(s1, s2)
  diffs = []
  (0...s1.length).each do |i|
    if s1[i] != s2[i]
      diffs << i
      return false if diffs.size > 2
    end
  end

  return true if diffs.empty?
  return false unless diffs.size == 2

  i, j = diffs[0], diffs[1]
  s1[i] == s2[j] && s1[j] == s2[i]
end
```

## Scala

```scala
object Solution {
    def areAlmostEqual(s1: String, s2: String): Boolean = {
        var first = -1
        var second = -1
        var diff = 0
        val n = s1.length
        for (i <- 0 until n) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diff += 1
                if (diff > 2) return false
                if (first == -1) first = i else second = i
            }
        }
        if (diff == 0) true
        else if (diff == 2 && s1.charAt(first) == s2.charAt(second) && s1.charAt(second) == s2.charAt(first)) true
        else false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        if b1.len() != b2.len() {
            return false;
        }
        let mut diff_indices = Vec::with_capacity(2);
        for i in 0..b1.len() {
            if b1[i] != b2[i] {
                diff_indices.push(i);
                if diff_indices.len() > 2 {
                    return false;
                }
            }
        }
        match diff_indices.len() {
            0 => true,
            2 => {
                let i = diff_indices[0];
                let j = diff_indices[1];
                b1[i] == b2[j] && b1[j] == b2[i]
            }
            _ => false,
        }
    }
}
```

## Racket

```racket
(define/contract (are-almost-equal s1 s2)
  (-> string? string? boolean?)
  (let* ((n (string-length s1))
         (m (string-length s2)))
    (if (not (= n m))
        #f
        (let loop ((i 0) (first -1) (second -1) (cnt 0))
          (cond
            [(= i n)
             (cond
               [(= cnt 0) #t]
               [(= cnt 2)
                (and (char=? (string-ref s1 first) (string-ref s2 second))
                     (char=? (string-ref s1 second) (string-ref s2 first)))]
               [else #f])]
            [else
             (if (char=? (string-ref s1 i) (string-ref s2 i))
                 (loop (+ i 1) first second cnt)
                 (let ((new-cnt (+ cnt 1)))
                   (if (> new-cnt 2)
                       #f
                       (if (= cnt 0)
                           (loop (+ i 1) i second new-cnt)
                           (loop (+ i 1) first i new-cnt)))))])))))
```

## Erlang

```erlang
-module(solution).
-export([are_almost_equal/2]).

-spec are_almost_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
are_almost_equal(S1, S2) ->
    if byte_size(S1) =/= byte_size(S2) ->
            false;
       true ->
            L1 = unicode:characters_to_list(S1),
            L2 = unicode:characters_to_list(S2),
            check(L1, L2, [], 0)
    end.

check([], [], DiffList, Count) ->
    case Count of
        0 -> true;
        2 ->
            [{A,B},{C,D}] = lists:reverse(DiffList),
            (A =:= D) andalso (B =:= C);
        _ -> false
    end;
check([H1|T1], [H2|T2], DiffList, Count) ->
    if H1 =/= H2 ->
            NewCount = Count + 1,
            case NewCount > 2 of
                true -> false;
                false -> check(T1, T2, [{H1,H2}|DiffList], NewCount)
            end;
       true ->
            check(T1, T2, DiffList, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec are_almost_equal(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def are_almost_equal(s1, s2) do
    diffs =
      s1
      |> String.graphemes()
      |> Enum.zip(String.graphemes(s2))
      |> Enum.filter(fn {c1, c2} -> c1 != c2 end)

    case diffs do
      [] ->
        true

      [{a1, b1}, {a2, b2}] ->
        a1 == b2 and a2 == b1

      _ ->
        false
    end
  end
end
```
