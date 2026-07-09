# 3083. Existence of a Substring in a String and Its Reverse

## Cpp

```cpp
class Solution {
public:
    bool isSubstringPresent(string s) {
        int n = s.size();
        if (n < 2) return false;
        unordered_set<string> subs;
        for (int i = 0; i + 1 < n; ++i) {
            subs.insert(s.substr(i, 2));
        }
        string rev = s;
        reverse(rev.begin(), rev.end());
        for (int i = 0; i + 1 < n; ++i) {
            if (subs.count(rev.substr(i, 2))) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isSubstringPresent(String s) {
        int n = s.length();
        if (n < 2) return false;
        String rev = new StringBuilder(s).reverse().toString();
        for (int i = 0; i < n - 1; i++) {
            String sub = s.substring(i, i + 2);
            if (rev.contains(sub)) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2:
            return False
        rev = s[::-1]
        rev_subs = set()
        for i in range(n - 1):
            rev_subs.add(rev[i:i+2])
        for i in range(n - 1):
            if s[i:i+2] in rev_subs:
                return True
        return False
```

## Python3

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False
        rev = s[::-1]
        subs = {s[i:i+2] for i in range(n - 1)}
        rev_subs = {rev[i:i+2] for i in range(n - 1)}
        return not subs.isdisjoint(rev_subs)
```

## C

```c
#include <stdbool.h>

bool isSubstringPresent(char* s) {
    int n = 0;
    while (s[n]) n++;
    if (n < 2) return false;

    char rev[101];
    for (int i = 0; i < n; ++i) {
        rev[i] = s[n - 1 - i];
    }
    rev[n] = '\0';

    for (int i = 0; i < n - 1; ++i) {
        char a = s[i], b = s[i + 1];
        for (int j = 0; j < n - 1; ++j) {
            if (a == rev[j] && b == rev[j + 1]) {
                return true;
            }
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsSubstringPresent(string s) {
        int n = s.Length;
        if (n < 2) return false;

        var substrings = new HashSet<string>();
        for (int i = 0; i < n - 1; i++) {
            substrings.Add(s.Substring(i, 2));
        }

        char[] arr = s.ToCharArray();
        Array.Reverse(arr);
        string rev = new string(arr);

        for (int i = 0; i < rev.Length - 1; i++) {
            if (substrings.Contains(rev.Substring(i, 2))) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isSubstringPresent = function(s) {
    const n = s.length;
    if (n < 2) return false;
    
    const rev = s.split('').reverse().join('');
    const revSubs = new Set();
    for (let i = 0; i < n - 1; ++i) {
        revSubs.add(rev.substring(i, i + 2));
    }
    
    for (let i = 0; i < n - 1; ++i) {
        if (revSubs.has(s.substring(i, i + 2))) return true;
    }
    return false;
};
```

## Typescript

```typescript
function isSubstringPresent(s: string): boolean {
    const n = s.length;
    if (n < 2) return false;

    const rev = s.split('').reverse().join('');
    const substrSet = new Set<string>();

    for (let i = 0; i + 1 < rev.length; i++) {
        substrSet.add(rev.substring(i, i + 2));
    }

    for (let i = 0; i + 1 < n; i++) {
        if (substrSet.has(s.substring(i, i + 2))) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isSubstringPresent($s) {
        $n = strlen($s);
        if ($n < 2) {
            return false;
        }
        $subs = [];
        for ($i = 0; $i < $n - 1; $i++) {
            $sub = $s[$i] . $s[$i + 1];
            $subs[$sub] = true;
        }
        $rev = strrev($s);
        $m = strlen($rev);
        for ($i = 0; $i < $m - 1; $i++) {
            $sub = $rev[$i] . $rev[$i + 1];
            if (isset($subs[$sub])) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isSubstringPresent(_ s: String) -> Bool {
        let n = s.count
        if n < 2 { return false }
        let chars = Array(s)
        let revChars = Array(String(s.reversed()))
        for i in 0..<(n - 1) {
            for j in 0..<(n - 1) {
                if chars[i] == revChars[j] && chars[i + 1] == revChars[j + 1] {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSubstringPresent(s: String): Boolean {
        if (s.length < 2) return false
        val rev = s.reversed()
        val substrings = HashSet<String>()
        for (i in 0 until s.length - 1) {
            substrings.add(s.substring(i, i + 2))
        }
        for (i in 0 until rev.length - 1) {
            if (substrings.contains(rev.substring(i, i + 2))) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isSubstringPresent(String s) {
    int n = s.length;
    if (n < 2) return false;
    final Set<String> subs = {};
    for (int i = 0; i < n - 1; ++i) {
      subs.add(s.substring(i, i + 2));
    }
    String rev = s.split('').reversed.join();
    for (int i = 0; i < rev.length - 1; ++i) {
      if (subs.contains(rev.substring(i, i + 2))) return true;
    }
    return false;
  }
}
```

## Golang

```go
func isSubstringPresent(s string) bool {
    n := len(s)
    if n < 2 {
        return false
    }
    // Build reversed string
    rev := make([]byte, n)
    for i := 0; i < n; i++ {
        rev[i] = s[n-1-i]
    }

    substrSet := make(map[string]struct{})
    for i := 0; i+1 < n; i++ {
        substrSet[s[i:i+2]] = struct{}{}
    }
    for i := 0; i+1 < n; i++ {
        sub := string(rev[i : i+2])
        if _, ok := substrSet[sub]; ok {
            return true
        }
    }
    return false
}
```

## Ruby

```ruby
def is_substring_present(s)
  return false if s.length < 2
  rev = s.reverse
  (0..s.length - 2).each do |i|
    sub = s[i, 2]
    return true if rev.include?(sub)
  end
  false
end
```

## Scala

```scala
object Solution {
    def isSubstringPresent(s: String): Boolean = {
        if (s.length < 2) return false
        val rev = s.reverse
        val substrings = scala.collection.mutable.HashSet[String]()
        for (i <- 0 until s.length - 1) {
            substrings.add(s.substring(i, i + 2))
        }
        for (j <- 0 until rev.length - 1) {
            if (substrings.contains(rev.substring(j, j + 2))) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_substring_present(s: String) -> bool {
        let n = s.len();
        if n < 2 {
            return false;
        }
        let mut set = std::collections::HashSet::new();
        for i in 0..n - 1 {
            let sub = &s[i..i + 2];
            set.insert(sub.to_string());
        }
        let rev: String = s.chars().rev().collect();
        for i in 0..n - 1 {
            let sub = &rev[i..i + 2];
            if set.contains(sub) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (is-substring-present s)
  (-> string? boolean?)
  (let* ([n (string-length s)]
         [rev (string-reverse s)])
    (let loop ((i 0))
      (if (> i (- n 2))
          #f
          (let ([sub (substring s i (+ i 2))])
            (if (string-contains? rev sub)
                #t
                (loop (add1 i))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_substring_present/1]).

-spec is_substring_present(S :: unicode:unicode_binary()) -> boolean().
is_substring_present(S) ->
    Len = byte_size(S),
    case Len < 2 of
        true -> false;
        false ->
            Rev = list_to_binary(lists:reverse(binary_to_list(S))),
            has_common_substring(0, Len - 1, S, Rev)
    end.

-spec has_common_substring(integer(), integer(), binary(), binary()) -> boolean().
has_common_substring(I, Max, _S, _Rev) when I >= Max ->
    false;
has_common_substring(I, Max, S, Rev) ->
    Sub = binary:part(S, {I, 2}),
    case binary:match(Rev, Sub) of
        nomatch -> has_common_substring(I + 1, Max, S, Rev);
        _Match   -> true
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_substring_present(s :: String.t()) :: boolean()
  def is_substring_present(s) do
    len = String.length(s)

    if len < 2 do
      false
    else
      rev = String.reverse(s)

      rev_set =
        0..(String.length(rev) - 2)
        |> Enum.map(fn i -> binary_part(rev, i, 2) end)
        |> MapSet.new()

      0..(len - 2)
      |> Enum.any?(fn i ->
        sub = binary_part(s, i, 2)
        MapSet.member?(rev_set, sub)
      end)
    end
  end
end
```
