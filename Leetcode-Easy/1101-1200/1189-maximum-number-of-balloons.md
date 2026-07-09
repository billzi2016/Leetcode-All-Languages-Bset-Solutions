# 1189. Maximum Number of Balloons

## Cpp

```cpp
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        array<int, 26> cnt{};
        for (char c : text) cnt[c - 'a']++;
        int b = cnt['b' - 'a'];
        int a = cnt['a' - 'a'];
        int l = cnt['l' - 'a'] / 2;
        int o = cnt['o' - 'a'] / 2;
        int n = cnt['n' - 'a'];
        return min({b, a, l, o, n});
    }
};
```

## Java

```java
class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] cnt = new int[26];
        for (char c : text.toCharArray()) {
            cnt[c - 'a']++;
        }
        int b = cnt['b' - 'a'];
        int a = cnt['a' - 'a'];
        int l = cnt['l' - 'a'] / 2;
        int o = cnt['o' - 'a'] / 2;
        int n = cnt['n' - 'a'];
        return Math.min(Math.min(b, a), Math.min(l, Math.min(o, n)));
    }
}
```

## Python

```python
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1
        b = freq.get('b', 0)
        a = freq.get('a', 0)
        l = freq.get('l', 0) // 2
        o = freq.get('o', 0) // 2
        n = freq.get('n', 0)
        return min(b, a, l, o, n)
```

## Python3

```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        need = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        return min(cnt[ch] // need[ch] for ch in need)
```

## C

```c
int maxNumberOfBalloons(char* text) {
    int freq[26] = {0};
    for (char *p = text; *p; ++p) {
        freq[*p - 'a']++;
    }
    int b = freq['b' - 'a'];
    int a = freq['a' - 'a'];
    int l = freq['l' - 'a'] / 2;
    int o = freq['o' - 'a'] / 2;
    int n = freq['n' - 'a'];
    
    int min = b;
    if (a < min) min = a;
    if (l < min) min = l;
    if (o < min) min = o;
    if (n < min) min = n;
    return min;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNumberOfBalloons(string text) {
        int[] cnt = new int[26];
        foreach (char c in text) cnt[c - 'a']++;
        int b = cnt['b' - 'a'];
        int a = cnt['a' - 'a'];
        int l = cnt['l' - 'a'] / 2;
        int o = cnt['o' - 'a'] / 2;
        int n = cnt['n' - 'a'];
        int min = b;
        if (a < min) min = a;
        if (l < min) min = l;
        if (o < min) min = o;
        if (n < min) min = n;
        return min;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    const freq = {};
    for (const ch of text) {
        freq[ch] = (freq[ch] || 0) + 1;
    }
    const b = freq['b'] || 0;
    const a = freq['a'] || 0;
    const l = Math.floor((freq['l'] || 0) / 2);
    const o = Math.floor((freq['o'] || 0) / 2);
    const n = freq['n'] || 0;
    return Math.min(b, a, l, o, n);
};
```

## Typescript

```typescript
function maxNumberOfBalloons(text: string): number {
    const freq = new Map<string, number>();
    for (const ch of text) {
        freq.set(ch, (freq.get(ch) ?? 0) + 1);
    }
    const b = freq.get('b') ?? 0;
    const a = freq.get('a') ?? 0;
    const l = Math.floor((freq.get('l') ?? 0) / 2);
    const o = Math.floor((freq.get('o') ?? 0) / 2);
    const n = freq.get('n') ?? 0;
    return Math.min(b, a, l, o, n);
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function maxNumberOfBalloons($text) {
        $freq = array_fill_keys(['b','a','l','o','n'], 0);
        $len = strlen($text);
        for ($i = 0; $i < $len; $i++) {
            $ch = $text[$i];
            if (isset($freq[$ch])) {
                $freq[$ch]++;
            }
        }
        // 'l' and 'o' are needed twice
        $freq['l'] = intdiv($freq['l'], 2);
        $freq['o'] = intdiv($freq['o'], 2);
        return min($freq);
    }
}
```

## Swift

```swift
class Solution {
    func maxNumberOfBalloons(_ text: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        let aScalar = UnicodeScalar("a").value
        for scalar in text.unicodeScalars {
            let idx = Int(scalar.value - aScalar)
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        func count(_ ch: Character) -> Int {
            return freq[Int(UnicodeScalar(String(ch))!.value - aScalar)]
        }
        let b = count("b")
        let a = count("a")
        let l = count("l") / 2
        let o = count("o") / 2
        let n = count("n")
        
        var result = b
        result = min(result, a)
        result = min(result, l)
        result = min(result, o)
        result = min(result, n)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        val cnt = IntArray(26)
        for (ch in text) {
            cnt[ch - 'a']++
        }
        val b = cnt['b' - 'a']
        val a = cnt['a' - 'a']
        val l = cnt['l' - 'a'] / 2
        val o = cnt['o' - 'a'] / 2
        val n = cnt['n' - 'a']
        return minOf(b, a, l, o, n)
    }
}
```

## Dart

```dart
class Solution {
  int maxNumberOfBalloons(String text) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < text.length; ++i) {
      cnt[text.codeUnitAt(i) - 97]++;
    }
    int b = cnt['b'.codeUnitAt(0) - 97];
    int a = cnt['a'.codeUnitAt(0) - 97];
    int l = cnt['l'.codeUnitAt(0) - 97] ~/ 2;
    int o = cnt['o'.codeUnitAt(0) - 97] ~/ 2;
    int n = cnt['n'.codeUnitAt(0) - 97];
    return [b, a, l, o, n].reduce((value, element) => value < element ? value : element);
  }
}
```

## Golang

```go
func maxNumberOfBalloons(text string) int {
    var cnt [26]int
    for _, ch := range text {
        cnt[ch-'a']++
    }
    b := cnt['b'-'a']
    a := cnt['a'-'a']
    l := cnt['l'-'a'] / 2
    o := cnt['o'-'a'] / 2
    n := cnt['n'-'a']

    // find minimum among the required counts
    min := b
    if a < min {
        min = a
    }
    if l < min {
        min = l
    }
    if o < min {
        min = o
    }
    if n < min {
        min = n
    }
    return min
}
```

## Ruby

```ruby
def max_number_of_balloons(text)
  freq = Hash.new(0)
  text.each_char { |c| freq[c] += 1 }
  [
    freq['b'],
    freq['a'],
    freq['l'] / 2,
    freq['o'] / 2,
    freq['n']
  ].min
end
```

## Scala

```scala
object Solution {
    def maxNumberOfBalloons(text: String): Int = {
        val freq = new Array[Int](26)
        for (c <- text) {
            freq(c - 'a') += 1
        }
        val b = freq('b' - 'a')
        val a = freq('a' - 'a')
        val l = freq('l' - 'a') / 2
        val o = freq('o' - 'a') / 2
        val n = freq('n' - 'a')
        Seq(b, a, l, o, n).min
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut cnt = [0usize; 26];
        for ch in text.bytes() {
            cnt[(ch - b'a') as usize] += 1;
        }
        let b = cnt[(b'b' - b'a') as usize];
        let a = cnt[(b'a' - b'a') as usize];
        let l = cnt[(b'l' - b'a') as usize] / 2;
        let o = cnt[(b'o' - b'a') as usize] / 2;
        let n = cnt[(b'n' - b'a') as usize];
        let ans = *[b, a, l, o, n].iter().min().unwrap();
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-number-of-balloons text)
  (-> string? exact-integer?)
  (let* ([freq (make-vector 26 0)]
         [len (string-length text)])
    (for ([i (in-range len)])
      (let* ([ch (string-ref text i)]
             [idx (- (char->integer ch) (char->integer #\a))])
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    (define b (vector-ref freq (- (char->integer #\b) (char->integer #\a))))
    (define a (vector-ref freq (- (char->integer #\a) (char->integer #\a))))
    (define l (vector-ref freq (- (char->integer #\l) (char->integer #\a))))
    (define o (vector-ref freq (- (char->integer #\o) (char->integer #\a))))
    (define n (vector-ref freq (- (char->integer #\n) (char->integer #\a))))
    (let ([candidates (list b a (quotient l 2) (quotient o 2) n)])
      (apply min candidates))))
```

## Erlang

```erlang
-spec max_number_of_balloons(Text :: unicode:unicode_binary()) -> integer().
max_number_of_balloons(Text) ->
    List = unicode:characters_to_list(Text),
    Counts = lists:foldl(fun(Char, Acc) ->
        case Char of
            $b -> maps:update_with(b, fun(V) -> V + 1 end, 1, Acc);
            $a -> maps:update_with(a, fun(V) -> V + 1 end, 1, Acc);
            $l -> maps:update_with(l, fun(V) -> V + 1 end, 1, Acc);
            $o -> maps:update_with(o, fun(V) -> V + 1 end, 1, Acc);
            $n -> maps:update_with(n, fun(V) -> V + 1 end, 1, Acc);
            _   -> Acc
        end
    end, #{b => 0, a => 0, l => 0, o => 0, n => 0}, List),
    B = maps:get(b, Counts),
    A = maps:get(a, Counts),
    L = maps:get(l, Counts) div 2,
    O = maps:get(o, Counts) div 2,
    N = maps:get(n, Counts),
    lists:min([B, A, L, O, N]).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_number_of_balloons(text :: String.t) :: integer
  def max_number_of_balloons(text) do
    freq =
      text
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    b = Map.get(freq, "b", 0)
    a = Map.get(freq, "a", 0)
    l = Map.get(freq, "l", 0) |> div(2)
    o = Map.get(freq, "o", 0) |> div(2)
    n = Map.get(freq, "n", 0)

    Enum.min([b, a, l, o, n])
  end
end
```
