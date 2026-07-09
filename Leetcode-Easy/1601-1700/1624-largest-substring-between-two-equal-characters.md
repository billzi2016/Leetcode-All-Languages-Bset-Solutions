# 1624. Largest Substring Between Two Equal Characters

## Cpp

```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        vector<int> first(26, -1);
        int ans = -1;
        for (int i = 0; i < (int)s.size(); ++i) {
            int idx = s[i] - 'a';
            if (first[idx] != -1) {
                ans = max(ans, i - first[idx] - 1);
            } else {
                first[idx] = i;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int[] first = new int[26];
        java.util.Arrays.fill(first, -1);
        int ans = -1;
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] != -1) {
                ans = Math.max(ans, i - first[idx] - 1);
            } else {
                first[idx] = i;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in first:
                ans = max(ans, i - first[ch] - 1)
            else:
                first[ch] = i
        return ans
```

## Python3

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_idx = {}
        ans = -1
        for i, ch in enumerate(s):
            if ch in first_idx:
                ans = max(ans, i - first_idx[ch] - 1)
            else:
                first_idx[ch] = i
        return ans
```

## C

```c
int maxLengthBetweenEqualCharacters(char* s) {
    int first[26];
    for (int i = 0; i < 26; ++i) first[i] = -1;
    int ans = -1;
    for (int i = 0; s[i]; ++i) {
        int idx = s[i] - 'a';
        if (first[idx] != -1) {
            int len = i - first[idx] - 1;
            if (len > ans) ans = len;
        } else {
            first[idx] = i;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxLengthBetweenEqualCharacters(string s)
    {
        int[] first = new int[26];
        for (int i = 0; i < 26; i++) first[i] = -1;
        int ans = -1;
        for (int i = 0; i < s.Length; i++)
        {
            int idx = s[i] - 'a';
            if (first[idx] != -1)
                ans = Math.Max(ans, i - first[idx] - 1);
            else
                first[idx] = i;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxLengthBetweenEqualCharacters = function(s) {
    const firstIdx = new Array(26).fill(-1);
    let ans = -1;
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97; // 'a' = 97
        if (firstIdx[idx] === -1) {
            firstIdx[idx] = i;
        } else {
            const len = i - firstIdx[idx] - 1;
            if (len > ans) ans = len;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxLengthBetweenEqualCharacters(s: string): number {
    const first = new Map<string, number>();
    let ans = -1;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (first.has(ch)) {
            const len = i - first.get(ch)! - 1;
            if (len > ans) ans = len;
        } else {
            first.set(ch, i);
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxLengthBetweenEqualCharacters($s) {
        $first = [];
        $ans = -1;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (array_key_exists($c, $first)) {
                $dist = $i - $first[$c] - 1;
                if ($dist > $ans) {
                    $ans = $dist;
                }
            } else {
                $first[$c] = $i;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxLengthBetweenEqualCharacters(_ s: String) -> Int {
        let chars = Array(s)
        var firstPos = Array(repeating: -1, count: 26)
        var answer = -1
        for i in 0..<chars.count {
            guard let ascii = chars[i].asciiValue else { continue }
            let idx = Int(ascii - Character("a").asciiValue!)
            if firstPos[idx] != -1 {
                answer = max(answer, i - firstPos[idx] - 1)
            } else {
                firstPos[idx] = i
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxLengthBetweenEqualCharacters(s: String): Int {
        val first = IntArray(26) { -1 }
        var ans = -1
        for (i in s.indices) {
            val idx = s[i] - 'a'
            if (first[idx] != -1) {
                ans = kotlin.math.max(ans, i - first[idx] - 1)
            } else {
                first[idx] = i
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxLengthBetweenEqualCharacters(String s) {
    Map<String, int> firstIndex = {};
    int ans = -1;
    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (firstIndex.containsKey(ch)) {
        ans = max(ans, i - firstIndex[ch]! - 1);
      } else {
        firstIndex[ch] = i;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxLengthBetweenEqualCharacters(s string) int {
    firstIdx := [26]int{}
    for i := 0; i < 26; i++ {
        firstIdx[i] = -1
    }
    ans := -1
    for i, ch := range s {
        idx := ch - 'a'
        if firstIdx[idx] == -1 {
            firstIdx[idx] = i
        } else {
            length := i - firstIdx[idx] - 1
            if length > ans {
                ans = length
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_length_between_equal_characters(s)
  first_index = Array.new(26)
  ans = -1
  base = 'a'.ord
  s.each_char.with_index do |ch, i|
    idx = ch.ord - base
    if first_index[idx].nil?
      first_index[idx] = i
    else
      length = i - first_index[idx] - 1
      ans = length if length > ans
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxLengthBetweenEqualCharacters(s: String): Int = {
        val first = Array.fill(26)(-1)
        var ans = -1
        for (i <- s.indices) {
            val idx = s.charAt(i) - 'a'
            if (first(idx) != -1) {
                val len = i - first(idx) - 1
                if (len > ans) ans = len
            } else {
                first(idx) = i
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut first = [-1i32; 26];
        let mut ans = -1i32;
        for (i, &b) in s.as_bytes().iter().enumerate() {
            let idx = (b - b'a') as usize;
            if first[idx] != -1 {
                let len = i as i32 - first[idx] - 1;
                if len > ans {
                    ans = len;
                }
            } else {
                first[idx] = i as i32;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-length-between-equal-characters s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (first (make-vector 26 -1))
         (ans -1))
    (let loop ((i 0) (best ans))
      (if (= i n)
          best
          (let* ((ch (char->integer (string-ref s i)))
                 (idx (- ch (char->integer #\a))))
            (cond
              [(= (vector-ref first idx) -1)
               (vector-set! first idx i)
               (loop (+ i 1) best)]
              [else
               (let ((len (- i (vector-ref first idx) 1)))
                 (loop (+ i 1) (max best len)))]))))))
```

## Erlang

```erlang
-module(solution).
-export([max_length_between_equal_characters/1]).

-spec max_length_between_equal_characters(S :: unicode:unicode_binary()) -> integer().
max_length_between_equal_characters(S) ->
    List = binary_to_list(S),
    max_len(List, 0, #{}, -1).

max_len([], _Idx, _Map, Ans) ->
    Ans;
max_len([C|Rest], Idx, Map, Ans) ->
    CharKey = C - $a,
    case maps:is_key(CharKey, Map) of
        true ->
            FirstIdx = maps:get(CharKey, Map),
            NewAns = erlang:max(Ans, Idx - FirstIdx - 1),
            max_len(Rest, Idx + 1, Map, NewAns);
        false ->
            NewMap = maps:put(CharKey, Idx, Map),
            max_len(Rest, Idx + 1, NewMap, Ans)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_length_between_equal_characters(s :: String.t) :: integer
  def max_length_between_equal_characters(s) do
    chars = String.graphemes(s)

    {ans, _} =
      Enum.reduce(Enum.with_index(chars), {-1, %{}}, fn {c, i}, {max_len, map} ->
        case Map.fetch(map, c) do
          {:ok, first_idx} ->
            len = i - first_idx - 1
            new_max = if len > max_len, do: len, else: max_len
            {new_max, map}

          :error ->
            {max_len, Map.put(map, c, i)}
        end
      end)

    ans
  end
end
```
