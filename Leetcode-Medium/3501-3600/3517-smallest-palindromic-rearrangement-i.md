# 3517. Smallest Palindromic Rearrangement I

## Cpp

```cpp
class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> cnt(26, 0);
        for (char ch : s) cnt[ch - 'a']++;
        string left;
        left.reserve(s.size() / 2);
        char mid = 0;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] % 2 == 1) mid = char('a' + i);
            left.append(cnt[i] / 2, char('a' + i));
        }
        string res = left;
        if (mid) res.push_back(mid);
        res.append(left.rbegin(), left.rend());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String smallestPalindrome(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        StringBuilder left = new StringBuilder();
        char mid = 0;
        for (int i = 0; i < 26; i++) {
            if ((cnt[i] & 1) == 1) {
                mid = (char) ('a' + i);
            }
            int half = cnt[i] / 2;
            for (int j = 0; j < half; j++) {
                left.append((char) ('a' + i));
            }
        }
        StringBuilder res = new StringBuilder();
        res.append(left);
        if (mid != 0) {
            res.append(mid);
        }
        res.append(left.reverse());
        return res.toString();
    }
}
```

## Python

```python
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        first_half = []
        mid_char = ''
        for i in range(26):
            cnt = freq[i]
            half = cnt // 2
            if half:
                first_half.append(chr(i + 97) * half)
            if cnt % 2 == 1:
                mid_char = chr(i + 97)

        left = ''.join(first_half)
        right = left[::-1]
        return left + mid_char + right
```

## Python3

```python
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        left_parts = []
        middle = ''
        for i in range(26):
            half = cnt[i] // 2
            if half:
                left_parts.append(chr(97 + i) * half)
            if cnt[i] % 2 == 1:
                middle = chr(97 + i)

        left = ''.join(left_parts)
        return left + middle + left[::-1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* smallestPalindrome(char* s) {
    size_t n = strlen(s);
    int cnt[26] = {0};
    for (size_t i = 0; i < n; ++i) {
        cnt[s[i] - 'a']++;
    }
    
    char middle = '\0';
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] % 2 == 1) {
            middle = 'a' + i;
            break; // at most one odd count in a palindrome
        }
    }
    
    size_t half_len = n / 2;
    char *half = (char *)malloc(half_len + 1);
    size_t pos = 0;
    for (int i = 0; i < 26; ++i) {
        int repeat = cnt[i] / 2;
        while (repeat--) {
            half[pos++] = 'a' + i;
        }
    }
    half[pos] = '\0';
    
    char *res = (char *)malloc(n + 1);
    size_t idx = 0;
    memcpy(res + idx, half, half_len);
    idx += half_len;
    if (middle) {
        res[idx++] = middle;
    }
    for (size_t i = half_len; i > 0; --i) {
        res[idx++] = half[i - 1];
    }
    res[idx] = '\0';
    
    free(half);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string SmallestPalindrome(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;

        var leftBuilder = new System.Text.StringBuilder();
        char middleChar = '\0';

        for (int i = 0; i < 26; i++) {
            if ((cnt[i] & 1) == 1) {
                middleChar = (char)('a' + i);
            }
            int half = cnt[i] >> 1;
            if (half > 0) leftBuilder.Append(new string((char)('a' + i), half));
        }

        string left = leftBuilder.ToString();
        var result = new System.Text.StringBuilder(left.Length * 2 + (middleChar == '\0' ? 0 : 1));

        result.Append(left);
        if (middleChar != '\0') result.Append(middleChar);
        for (int i = left.Length - 1; i >= 0; i--) {
            result.Append(left[i]);
        }

        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var smallestPalindrome = function(s) {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - 97]++;
    }
    const leftParts = [];
    let middle = '';
    for (let i = 0; i < 26; ++i) {
        const half = Math.floor(cnt[i] / 2);
        if (half > 0) {
            const ch = String.fromCharCode(97 + i);
            leftParts.push(ch.repeat(half));
        }
        if (cnt[i] % 2 === 1) {
            middle = String.fromCharCode(97 + i);
        }
    }
    const left = leftParts.join('');
    const right = leftParts.slice().reverse().join('');
    return left + middle + right;
};
```

## Typescript

```typescript
function smallestPalindrome(s: string): string {
    const cnt = new Array(26).fill(0);
    for (const ch of s) {
        cnt[ch.charCodeAt(0) - 97]++;
    }
    const leftParts: string[] = [];
    let middle = '';
    for (let i = 0; i < 26; i++) {
        const half = Math.floor(cnt[i] / 2);
        if (half > 0) {
            leftParts.push(String.fromCharCode(97 + i).repeat(half));
        }
        if (cnt[i] % 2 === 1) {
            middle = String.fromCharCode(97 + i);
        }
    }
    const left = leftParts.join('');
    const right = left.split('').reverse().join('');
    return left + middle + right;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function smallestPalindrome($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
        }

        $left = '';
        $mid = '';
        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] % 2 == 1) {
                $mid = chr($i + 97);
            }
            $half = intdiv($cnt[$i], 2);
            if ($half > 0) {
                $left .= str_repeat(chr($i + 97), $half);
            }
        }

        return $left . $mid . strrev($left);
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func smallestPalindrome(_ s: String) -> String {
        var freq = [Int](repeating: 0, count: 26)
        let aValue = Int(UnicodeScalar("a").value)
        
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value) - aValue
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        
        var leftChars = [Character]()
        leftChars.reserveCapacity(s.count / 2)
        var middleChar: Character? = nil
        
        for i in 0..<26 {
            let cnt = freq[i]
            if cnt % 2 == 1 {
                middleChar = Character(UnicodeScalar(i + aValue)!)
            }
            let half = cnt / 2
            if half > 0 {
                let ch = Character(UnicodeScalar(i + aValue)!)
                for _ in 0..<half {
                    leftChars.append(ch)
                }
            }
        }
        
        let leftString = String(leftChars)
        var result = leftString
        if let mid = middleChar {
            result.append(mid)
        }
        result += String(leftChars.reversed())
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestPalindrome(s: String): String {
        val cnt = IntArray(26)
        for (c in s) {
            cnt[c - 'a']++
        }
        val left = StringBuilder()
        var mid = ""
        for (i in 0 until 26) {
            val ch = ('a'.code + i).toChar()
            if (cnt[i] % 2 == 1) {
                mid = ch.toString()
            }
            repeat(cnt[i] / 2) { left.append(ch) }
        }
        val result = StringBuilder()
        result.append(left)
        if (mid.isNotEmpty()) result.append(mid)
        result.append(StringBuilder(left).reverse())
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String smallestPalindrome(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }

    StringBuffer left = StringBuffer();
    String middle = '';

    for (int i = 0; i < 26; i++) {
      int half = cnt[i] ~/ 2;
      for (int j = 0; j < half; j++) {
        left.writeCharCode(97 + i);
      }
      if (cnt[i] % 2 == 1) {
        middle = String.fromCharCode(97 + i);
      }
    }

    String leftStr = left.toString();
    String rev = leftStr.split('').reversed.join();

    return leftStr + middle + rev;
  }
}
```

## Golang

```go
func smallestPalindrome(s string) string {
    var freq [26]int
    for i := 0; i < len(s); i++ {
        freq[s[i]-'a']++
    }

    left := make([]byte, 0, len(s)/2)
    middle := ""

    for i := 0; i < 26; i++ {
        cnt := freq[i]
        half := cnt / 2
        if half > 0 {
            left = append(left, bytes.Repeat([]byte{byte('a' + i)}, half)...)
        }
        if cnt%2 == 1 {
            middle = string(byte('a' + i))
        }
    }

    var builder strings.Builder
    builder.Grow(len(s))
    builder.Write(left)
    if middle != "" {
        builder.WriteString(middle)
    }
    for i := len(left) - 1; i >= 0; i-- {
        builder.WriteByte(left[i])
    }
    return builder.String()
}
```

## Ruby

```ruby
def smallest_palindrome(s)
  counts = Array.new(26, 0)
  s.each_byte { |b| counts[b - 97] += 1 }

  left_parts = []
  middle = ''

  (0...26).each do |i|
    half = counts[i] / 2
    left_parts << ((97 + i).chr * half) if half > 0
    if counts[i].odd?
      middle = (97 + i).chr
    end
  end

  left = left_parts.join
  left + middle + left.reverse
end
```

## Scala

```scala
object Solution {
    def smallestPalindrome(s: String): String = {
        val freq = new Array[Int](26)
        s.foreach(ch => freq(ch - 'a') += 1)

        val leftBuilder = new StringBuilder
        var midChar = ""

        for (i <- 0 until 26) {
            val cnt = freq(i)
            if ((cnt & 1) == 1) midChar = ('a' + i).toChar.toString
            val half = cnt / 2
            for (_ <- 0 until half) leftBuilder.append(('a' + i).toChar)
        }

        val left = leftBuilder.toString()
        val right = left.reverse
        left + midChar + right
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        let mut cnt = [0usize; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }

        let mut left = String::with_capacity(s.len() / 2);
        let mut center_char: Option<char> = None;

        for i in 0..26 {
            if cnt[i] % 2 == 1 {
                center_char = Some((b'a' + i as u8) as char);
            }
            let half = cnt[i] / 2;
            for _ in 0..half {
                left.push((b'a' + i as u8) as char);
            }
        }

        let mut result = String::with_capacity(s.len());
        result.push_str(&left);
        if let Some(c) = center_char {
            result.push(c);
        }
        for ch in left.chars().rev() {
            result.push(ch);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (smallest-palindrome s)
  (-> string? string?)
  (let* ([freq (make-vector 26 0)]
         [len (string-length s)])
    ;; count frequencies
    (for ([i (in-range len)])
      (let* ([c (string-ref s i)]
             [idx (- (char->integer c) (char->integer #\a))])
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    ;; build left half and middle character
    (define left-parts '())
    (define mid "")
    (for ([i (in-range 26)])
      (let* ([cnt (vector-ref freq i)]
             [half (quotient cnt 2)]
             [odd (remainder cnt 2)]
             [ch (integer->char (+ (char->integer #\a) i))])
        (when (> half 0)
          (set! left-parts (cons (make-string half ch) left-parts)))
        (when (= odd 1)
          (set! mid (string ch)))))
    (define left-str (apply string-append (reverse left-parts)))
    (define right-str (list->string (reverse (string->list left-str))))
    (string-append left-str mid right-str)))
```

## Erlang

```erlang
-spec smallest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_palindrome(S) ->
    CountMap = count_chars(S, #{}),
    Left = build_left(CountMap),
    Middle = find_middle(CountMap),
    iolist_to_binary([Left, Middle, lists:reverse(Left)]).

count_chars(<<>>, Map) -> Map;
count_chars(<<C, Rest/binary>>, Map) ->
    NewMap = maps:update_with(C,
                               fun(V) -> V + 1 end,
                               1,
                               Map),
    count_chars(Rest, NewMap).

build_left(Map) -> build_left(lists:seq($a, $z), Map, []).

build_left([], _, Acc) -> lists:reverse(Acc);
build_left([Code | Rest], Map, Acc) ->
    Cnt = maps:get(Code, Map, 0),
    Half = Cnt div 2,
    case Half of
        0 -> build_left(Rest, Map, Acc);
        _ ->
            Bin = binary:copy(<<Code>>, Half),
            build_left(Rest, Map, [Bin | Acc])
    end.

find_middle(Map) -> find_middle(lists:seq($a, $z), Map).

find_middle([], _) -> <<>>;
find_middle([Code | Rest], Map) ->
    Cnt = maps:get(Code, Map, 0),
    if (Cnt rem 2) == 1 -> <<Code>>; true -> find_middle(Rest, Map) end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_palindrome(s :: String.t) :: String.t
  def smallest_palindrome(s) do
    counts =
      Enum.reduce(:binary.bin_to_list(s), :erlang.make_tuple(26, 0), fn c, acc ->
        idx = c - ?a + 1
        val = elem(acc, idx)
        put_elem(acc, idx, val + 1)
      end)

    left =
      for i <- 1..26 do
        cnt = elem(counts, i)
        repeat = div(cnt, 2)

        if repeat > 0,
          do: String.duplicate(<<?a + i - 1>>, repeat),
          else: ""
      end
      |> Enum.join()

    middle =
      Enum.reduce_while(1..26, "", fn i, _ ->
        cnt = elem(counts, i)

        if rem(cnt, 2) == 1 do
          {:halt, <<?a + i - 1>>}
        else
          {:cont, ""}
        end
      end)

    right = String.reverse(left)
    left <> middle <> right
  end
end
```
