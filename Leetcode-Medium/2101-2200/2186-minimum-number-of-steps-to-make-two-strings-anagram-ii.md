# 2186. Minimum Number of Steps to Make Two Strings Anagram II

## Cpp

```cpp
class Solution {
public:
    int minSteps(string s, string t) {
        int cnt[26] = {0};
        for (char c : s) ++cnt[c - 'a'];
        for (char c : t) --cnt[c - 'a'];
        int ans = 0;
        for (int i = 0; i < 26; ++i) ans += abs(cnt[i]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minSteps(String s, String t) {
        int[] diff = new int[26];
        for (int i = 0; i < s.length(); i++) {
            diff[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            diff[t.charAt(i) - 'a']--;
        }
        int steps = 0;
        for (int d : diff) {
            steps += Math.abs(d);
        }
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        diff = [0] * 26
        for ch in s:
            diff[ord(ch) - 97] += 1
        for ch in t:
            diff[ord(ch) - 97] -= 1
        return sum(abs(x) for x in diff)
```

## Python3

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = [0] * 26
        for ch in s:
            diff[ord(ch) - 97] += 1
        for ch in t:
            diff[ord(ch) - 97] -= 1
        return sum(abs(x) for x in diff)
```

## C

```c
int minSteps(char* s, char* t) {
    int cnt[26] = {0};
    for (char *p = s; *p; ++p) cnt[*p - 'a']++;
    for (char *p = t; *p; ++p) cnt[*p - 'a']--;
    int ans = 0;
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] > 0) ans += cnt[i];
        else ans -= cnt[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinSteps(string s, string t) {
        int[] count = new int[26];
        foreach (char c in s) {
            count[c - 'a']++;
        }
        foreach (char c in t) {
            count[c - 'a']--;
        }
        int steps = 0;
        for (int i = 0; i < 26; i++) {
            steps += Math.Abs(count[i]);
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    const cnt = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - aCode]++;
    }
    for (let i = 0; i < t.length; ++i) {
        cnt[t.charCodeAt(i) - aCode]--;
    }
    
    let steps = 0;
    for (let i = 0; i < 26; ++i) {
        steps += Math.abs(cnt[i]);
    }
    return steps;
};
```

## Typescript

```typescript
function minSteps(s: string, t: string): number {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < t.length; ++i) {
        cnt[t.charCodeAt(i) - 97]--;
    }
    let steps = 0;
    for (let i = 0; i < 26; ++i) {
        steps += Math.abs(cnt[i]);
    }
    return steps;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minSteps($s, $t) {
        $cnt = array_fill(0, 26, 0);
        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
        }
        $lenT = strlen($t);
        for ($i = 0; $i < $lenT; $i++) {
            $idx = ord($t[$i]) - 97;
            $cnt[$idx]--;
        }
        $steps = 0;
        foreach ($cnt as $c) {
            $steps += abs($c);
        }
        return $steps;
    }
}
```

## Swift

```swift
class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        var diff = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97)
            diff[idx] += 1
        }
        for byte in t.utf8 {
            let idx = Int(byte - 97)
            diff[idx] -= 1
        }
        var result = 0
        for v in diff {
            result += abs(v)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSteps(s: String, t: String): Int {
        val count = IntArray(26)
        for (ch in s) {
            count[ch - 'a']++
        }
        for (ch in t) {
            count[ch - 'a']--
        }
        var steps = 0
        for (c in count) {
            steps += kotlin.math.abs(c)
        }
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int minSteps(String s, String t) {
    List<int> diff = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      diff[s.codeUnitAt(i) - 97]++;
    }
    for (int i = 0; i < t.length; i++) {
      diff[t.codeUnitAt(i) - 97]--;
    }
    int ans = 0;
    for (int v in diff) {
      ans += v.abs();
    }
    return ans;
  }
}
```

## Golang

```go
func minSteps(s string, t string) int {
    var cnt [26]int
    for i := 0; i < len(s); i++ {
        cnt[s[i]-'a']++
    }
    for i := 0; i < len(t); i++ {
        cnt[t[i]-'a']--
    }
    steps := 0
    for _, v := range cnt {
        if v < 0 {
            steps -= v
        } else {
            steps += v
        }
    }
    return steps
}
```

## Ruby

```ruby
def min_steps(s, t)
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }
  t.each_byte { |b| cnt[b - 97] -= 1 }
  cnt.reduce(0) { |sum, v| sum + v.abs }
end
```

## Scala

```scala
object Solution {
    def minSteps(s: String, t: String): Int = {
        val diff = new Array[Int](26)
        for (ch <- s) diff(ch - 'a') += 1
        for (ch <- t) diff(ch - 'a') -= 1
        var steps = 0
        for (i <- 0 until 26) steps += math.abs(diff(i))
        steps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut diff = [0i32; 26];
        for b in s.bytes() {
            diff[(b - b'a') as usize] += 1;
        }
        for b in t.bytes() {
            diff[(b - b'a') as usize] -= 1;
        }
        diff.iter().map(|&x| x.abs()).sum()
    }
}
```

## Racket

```racket
(define/contract (min-steps s t)
  (-> string? string? exact-integer?)
  (let* ((cnt (make-vector 26 0))
         (len-s (string-length s))
         (len-t (string-length t)))
    (for ([i (in-range len-s)])
      (let* ((ch (char->integer (string-ref s i)))
             (idx (- ch (char->integer #\a))))
        (vector-set! cnt idx (+ 1 (vector-ref cnt idx)))))
    (for ([i (in-range len-t)])
      (let* ((ch (char->integer (string-ref t i)))
             (idx (- ch (char->integer #\a))))
        (vector-set! cnt idx (- (vector-ref cnt idx) 1))))
    (let loop ((i 0) (sum 0))
      (if (= i 26)
          sum
          (loop (+ i 1) (+ sum (abs (vector-ref cnt i))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_steps/2]).

-spec min_steps(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
min_steps(S, T) ->
    Map0 = #{},
    Map1 = process_bin(S, Map0, 1),
    Map2 = process_bin(T, Map1, -1),
    maps:fold(fun(_Key, Val, Acc) -> Acc + erlang:abs(Val) end, 0, Map2).

process_bin(<<>>, Map, _Delta) ->
    Map;
process_bin(<<Char, Rest/binary>>, Map, Delta) ->
    NewMap = maps:update_with(
                Char,
                fun(V) -> V + Delta end,
                Delta,
                Map),
    process_bin(Rest, NewMap, Delta).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_steps(s :: String.t(), t :: String.t()) :: integer()
  def min_steps(s, t) do
    freq = fn str ->
      Enum.reduce(String.to_charlist(str), %{}, fn c, acc ->
        Map.update(acc, c, 1, &(&1 + 1))
      end)
    end

    fs = freq.(s)
    ft = freq.(t)

    ?a..?z
    |> Enum.reduce(0, fn code, sum ->
      a = Map.get(fs, code, 0)
      b = Map.get(ft, code, 0)
      sum + abs(a - b)
    end)
  end
end
```
