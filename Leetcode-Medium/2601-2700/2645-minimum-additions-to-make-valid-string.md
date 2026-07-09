# 2645. Minimum Additions to Make Valid String

## Cpp

```cpp
class Solution {
public:
    int addMinimum(string word) {
        const string pat = "abc";
        int idx = 0, ans = 0;
        for (char c : word) {
            while (pat[idx] != c) {
                ++ans;
                idx = (idx + 1) % 3;
            }
            idx = (idx + 1) % 3;
        }
        while (idx != 0) {
            ++ans;
            idx = (idx + 1) % 3;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int addMinimum(String word) {
        char[] pattern = {'a', 'b', 'c'};
        int idx = 0; // expected character index in pattern
        int insertions = 0;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            while (ch != pattern[idx]) {
                insertions++;
                idx = (idx + 1) % 3;
            }
            // matched current character
            idx = (idx + 1) % 3;
        }
        // complete the last incomplete "abc" block if any
        while (idx != 0) {
            insertions++;
            idx = (idx + 1) % 3;
        }
        return insertions;
    }
}
```

## Python

```python
class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        pattern = "abc"
        j = 0
        ans = 0
        for ch in word:
            while ch != pattern[j]:
                ans += 1
                j = (j + 1) % 3
            j = (j + 1) % 3
        if j != 0:
            ans += 3 - j
        return ans
```

## Python3

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        pattern = "abc"
        i = 0
        ans = 0
        for ch in word:
            while ch != pattern[i]:
                ans += 1
                i = (i + 1) % 3
            i = (i + 1) % 3
        ans += (3 - i) % 3
        return ans
```

## C

```c
int addMinimum(char* word) {
    const char pattern[3] = {'a', 'b', 'c'};
    int i = 0, j = 0;
    int ans = 0;
    while (word[i] != '\0') {
        if (word[i] == pattern[j]) {
            i++;
            j = (j + 1) % 3;
        } else {
            ans++;
            j = (j + 1) % 3;
        }
    }
    ans += (3 - j) % 3;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int AddMinimum(string word) {
        string pattern = "abc";
        int insertions = 0;
        int j = 0; // index in pattern
        
        foreach (char ch in word) {
            while (ch != pattern[j]) {
                insertions++;
                j = (j + 1) % 3;
            }
            // matched current character
            j = (j + 1) % 3;
        }
        
        insertions += (3 - j) % 3; // complete the last "abc" block if needed
        return insertions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var addMinimum = function(word) {
    const pattern = ['a', 'b', 'c'];
    let insertions = 0;
    let j = 0; // index in pattern
    
    let i = 0;
    while (i < word.length) {
        if (word[i] === pattern[j]) {
            i++;
            j = (j + 1) % 3;
        } else {
            insertions++;
            j = (j + 1) % 3;
        }
    }
    
    // Complete the last incomplete "abc" block, if any
    insertions += (3 - j) % 3;
    return insertions;
};
```

## Typescript

```typescript
function addMinimum(word: string): number {
    let insertions = 0;
    const pattern = ['a', 'b', 'c'];
    let pIdx = 0; // index in pattern

    for (let i = 0; i < word.length; i++) {
        while (word[i] !== pattern[pIdx]) {
            insertions++;
            pIdx = (pIdx + 1) % 3;
        }
        // matched current character
        pIdx = (pIdx + 1) % 3;
    }

    if (pIdx !== 0) {
        insertions += 3 - pIdx;
    }

    return insertions;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function addMinimum($word) {
        $pattern = ['a', 'b', 'c'];
        $i = 0;
        $j = 0;
        $ans = 0;
        $n = strlen($word);
        while ($i < $n) {
            if ($word[$i] === $pattern[$j]) {
                $i++;
                $j = ($j + 1) % 3;
            } else {
                $ans++;
                $j = ($j + 1) % 3;
            }
        }
        $ans += (3 - $j) % 3;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func addMinimum(_ word: String) -> Int {
        let pattern: [Character] = ["a", "b", "c"]
        var p = 0
        var ans = 0
        for ch in word {
            while ch != pattern[p] {
                ans += 1
                p = (p + 1) % 3
            }
            p = (p + 1) % 3
        }
        ans += (3 - p) % 3
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addMinimum(word: String): Int {
        val pattern = charArrayOf('a', 'b', 'c')
        var insertions = 0
        var idx = 0 // index in pattern
        for (ch in word) {
            while (ch != pattern[idx]) {
                insertions++
                idx = (idx + 1) % 3
            }
            idx = (idx + 1) % 3
        }
        if (idx != 0) {
            insertions += 3 - idx
        }
        return insertions
    }
}
```

## Dart

```dart
class Solution {
  int addMinimum(String word) {
    const pattern = 'abc';
    int ans = 0;
    int j = 0;
    for (int i = 0; i < word.length; i++) {
      while (word[i] != pattern[j]) {
        ans++;
        j = (j + 1) % 3;
      }
      j = (j + 1) % 3;
    }
    ans += (3 - j) % 3;
    return ans;
  }
}
```

## Golang

```go
func addMinimum(word string) int {
	pattern := []byte{'a', 'b', 'c'}
	ans, idx := 0, 0
	for i := 0; i < len(word); i++ {
		ch := word[i]
		for ch != pattern[idx] {
			ans++
			idx = (idx + 1) % 3
		}
		idx = (idx + 1) % 3
	}
	ans += (3 - idx) % 3
	return ans
}
```

## Ruby

```ruby
def add_minimum(word)
  pattern = ['a', 'b', 'c']
  j = 0
  ans = 0
  i = 0
  while i < word.length
    if word[i] == pattern[j]
      i += 1
      j = (j + 1) % 3
    else
      ans += 1
      j = (j + 1) % 3
    end
  end
  ans + ((3 - j) % 3)
end
```

## Scala

```scala
object Solution {
    def addMinimum(word: String): Int = {
        val pattern = Array('a', 'b', 'c')
        var i = 0
        var j = 0
        var ans = 0
        val n = word.length
        while (i < n) {
            if (word.charAt(i) == pattern(j)) {
                i += 1
                j = (j + 1) % 3
            } else {
                ans += 1
                j = (j + 1) % 3
            }
        }
        ans + ((3 - j) % 3)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_minimum(word: String) -> i32 {
        let pattern = ['a', 'b', 'c'];
        let mut idx = 0usize;
        let mut ans = 0i32;
        for ch in word.chars() {
            while ch != pattern[idx] {
                ans += 1;
                idx = (idx + 1) % 3;
            }
            idx = (idx + 1) % 3;
        }
        ans + ((3 - idx) % 3) as i32
    }
}
```

## Racket

```racket
(define/contract (add-minimum word)
  (-> string? exact-integer?)
  (let* ([pattern "abc"]
         [n (string-length word)])
    (let loop ((i 0) (j 0) (ans 0))
      (if (= i n)
          (+ ans (if (= j 0) 0 (- 3 j)))
          (let ((c (string-ref word i))
                (p (string-ref pattern j)))
            (if (char=? c p)
                (loop (+ i 1) (modulo (+ j 1) 3) ans)
                (loop i (modulo (+ j 1) 3) (+ ans 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([add_minimum/1]).

-spec add_minimum(Word :: unicode:unicode_binary()) -> integer().
add_minimum(Word) ->
    List = binary_to_list(Word),
    helper(List, 0, 0).

helper([], Idx, Acc) ->
    Rem = case Idx of
        0 -> 0;
        1 -> 2;
        2 -> 1
    end,
    Acc + Rem;
helper([C|Rest], Idx, Acc) ->
    PatternChar = pattern_char(Idx),
    if C == PatternChar ->
            NewIdx = (Idx + 1) rem 3,
            helper(Rest, NewIdx, Acc);
       true ->
            NewAcc = Acc + 1,
            NewIdx = (Idx + 1) rem 3,
            helper([C|Rest], NewIdx, NewAcc)
    end.

pattern_char(0) -> $a;
pattern_char(1) -> $b;
pattern_char(2) -> $c.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_minimum(word :: String.t()) :: integer()
  def add_minimum(word) do
    chars = String.graphemes(word)
    {j, ans} = process(chars, 0, 0)
    ans + rem(3 - j, 3)
  end

  @pattern ["a", "b", "c"]

  defp process([], j, ans), do: {j, ans}

  defp process([h | t], j, ans) do
    {new_j, new_ans} = match_char(h, j, ans)
    process(t, new_j, new_ans)
  end

  defp match_char(ch, j, ans) do
    if ch == Enum.at(@pattern, j) do
      {rem(j + 1, 3), ans}
    else
      new_j = rem(j + 1, 3)
      match_char(ch, new_j, ans + 1)
    end
  end
end
```
