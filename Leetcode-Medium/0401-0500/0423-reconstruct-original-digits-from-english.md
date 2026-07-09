# 0423. Reconstruct Original Digits from English

## Cpp

```cpp
class Solution {
public:
    string originalDigits(string s) {
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        vector<int> out(10, 0);
        out[0] = cnt['z' - 'a'];
        out[2] = cnt['w' - 'a'];
        out[4] = cnt['u' - 'a'];
        out[6] = cnt['x' - 'a'];
        out[8] = cnt['g' - 'a'];
        out[3] = cnt['h' - 'a'] - out[8];
        out[5] = cnt['f' - 'a'] - out[4];
        out[7] = cnt['s' - 'a'] - out[6];
        out[1] = cnt['o' - 'a'] - out[0] - out[2] - out[4];
        out[9] = cnt['i' - 'a'] - out[5] - out[6] - out[8];
        string res;
        for (int d = 0; d <= 9; ++d) {
            res.append(out[d], char('0' + d));
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String originalDigits(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }
        int[] digit = new int[10];
        digit[0] = cnt['z' - 'a'];
        digit[2] = cnt['w' - 'a'];
        digit[4] = cnt['u' - 'a'];
        digit[6] = cnt['x' - 'a'];
        digit[8] = cnt['g' - 'a'];
        digit[3] = cnt['h' - 'a'] - digit[8];
        digit[5] = cnt['f' - 'a'] - digit[4];
        digit[7] = cnt['s' - 'a'] - digit[6];
        digit[1] = cnt['o' - 'a'] - digit[0] - digit[2] - digit[4];
        digit[9] = cnt['i' - 'a'] - digit[5] - digit[6] - digit[8];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= 9; i++) {
            while (digit[i]-- > 0) {
                sb.append((char) ('0' + i));
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cnt = Counter(s)
        out = [0] * 10
        out[0] = cnt['z']
        out[2] = cnt['w']
        out[4] = cnt['u']
        out[6] = cnt['x']
        out[8] = cnt['g']
        out[1] = cnt['o'] - out[0] - out[2] - out[4]
        out[3] = cnt['h'] - out[8]
        out[5] = cnt['f'] - out[4]
        out[7] = cnt['s'] - out[6]
        out[9] = cnt['i'] - out[5] - out[6] - out[8]
        res = []
        for i in range(10):
            if out[i]:
                res.append(str(i) * out[i])
        return ''.join(res)
```

## Python3

```python
class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        digit_count = [0] * 10

        # Unique identifiers
        digit_count[0] = cnt['z']   # zero
        digit_count[2] = cnt['w']   # two
        digit_count[4] = cnt['u']   # four
        digit_count[6] = cnt['x']   # six
        digit_count[8] = cnt['g']   # eight

        # Derived counts
        digit_count[3] = cnt['h'] - digit_count[8]          # three (after eight)
        digit_count[5] = cnt['f'] - digit_count[4]          # five (after four)
        digit_count[7] = cnt['s'] - digit_count[6]          # seven (after six)
        digit_count[1] = cnt['o'] - digit_count[0] - digit_count[2] - digit_count[4]  # one
        digit_count[9] = cnt['i'] - digit_count[5] - digit_count[6] - digit_count[8]  # nine

        result = []
        for d in range(10):
            if digit_count[d]:
                result.append(str(d) * digit_count[d])
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* originalDigits(char* s) {
    int cnt[26] = {0};
    for (char *p = s; *p; ++p) {
        cnt[*p - 'a']++;
    }

    int out[10] = {0};

    out[0] = cnt['z' - 'a']; // zero
    out[2] = cnt['w' - 'a']; // two
    out[4] = cnt['u' - 'a']; // four
    out[6] = cnt['x' - 'a']; // six
    out[8] = cnt['g' - 'a']; // eight

    // remove letters of identified digits
    cnt['z' - 'a'] -= out[0];
    cnt['e' - 'a'] -= out[0];
    cnt['r' - 'a'] -= out[0];
    cnt['o' - 'a'] -= out[0];

    cnt['t' - 'a'] -= out[2];
    cnt['w' - 'a'] -= out[2];
    cnt['o' - 'a'] -= out[2];

    cnt['f' - 'a'] -= out[4];
    cnt['o' - 'a'] -= out[4];
    cnt['u' - 'a'] -= out[4];
    cnt['r' - 'a'] -= out[4];

    cnt['s' - 'a'] -= out[6];
    cnt['i' - 'a'] -= out[6];
    cnt['x' - 'a'] -= out[6];

    cnt['e' - 'a'] -= out[8];
    cnt['i' - 'a'] -= out[8];
    cnt['g' - 'a'] -= out[8];
    cnt['h' - 'a'] -= out[8];
    cnt['t' - 'a'] -= out[8];

    // remaining digits
    out[3] = cnt['h' - 'a']; // three
    cnt['t' - 'a'] -= out[3];
    cnt['h' - 'a'] -= out[3];
    cnt['r' - 'a'] -= out[3];
    cnt['e' - 'a'] -= out[3] * 2;

    out[5] = cnt['f' - 'a']; // five
    cnt['f' - 'a'] -= out[5];
    cnt['i' - 'a'] -= out[5];
    cnt['v' - 'a'] -= out[5];
    cnt['e' - 'a'] -= out[5];

    out[7] = cnt['s' - 'a']; // seven
    cnt['s' - 'a'] -= out[7];
    cnt['e' - 'a'] -= out[7] * 2;
    cnt['v' - 'a'] -= out[7];
    cnt['n' - 'a'] -= out[7];

    out[1] = cnt['o' - 'a']; // one
    cnt['o' - 'a'] -= out[1];
    cnt['n' - 'a'] -= out[1];
    cnt['e' - 'a'] -= out[1];

    out[9] = cnt['i' - 'a']; // nine

    int total = 0;
    for (int i = 0; i < 10; ++i) total += out[i];

    char *res = (char *)malloc(total + 1);
    int pos = 0;
    for (int d = 0; d <= 9; ++d) {
        for (int k = 0; k < out[d]; ++k) {
            res[pos++] = '0' + d;
        }
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string OriginalDigits(string s)
    {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;

        int[] digit = new int[10];
        digit[0] = cnt['z' - 'a'];
        digit[2] = cnt['w' - 'a'];
        digit[4] = cnt['u' - 'a'];
        digit[6] = cnt['x' - 'a'];
        digit[8] = cnt['g' - 'a'];

        digit[3] = cnt['h' - 'a'] - digit[8];
        digit[5] = cnt['f' - 'a'] - digit[4];
        digit[7] = cnt['s' - 'a'] - digit[6];
        digit[1] = cnt['o' - 'a'] - digit[0] - digit[2] - digit[4];
        digit[9] = cnt['i' - 'a'] - digit[5] - digit[6] - digit[8];

        var sb = new System.Text.StringBuilder();
        for (int i = 0; i <= 9; i++)
            if (digit[i] > 0)
                sb.Append(new string((char)('0' + i), digit[i]));

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var originalDigits = function(s) {
    const cnt = new Array(26).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;

    const out = new Array(10).fill(0);
    // unique letters
    out[0] = cnt['z'.charCodeAt(0) - 97];
    out[2] = cnt['w'.charCodeAt(0) - 97];
    out[4] = cnt['u'.charCodeAt(0) - 97];
    out[6] = cnt['x'.charCodeAt(0) - 97];
    out[8] = cnt['g'.charCodeAt(0) - 97];

    // letters after removing uniques
    out[3] = cnt['h'.charCodeAt(0) - 97] - out[8];
    out[5] = cnt['f'.charCodeAt(0) - 97] - out[4];
    out[7] = cnt['s'.charCodeAt(0) - 97] - out[6];
    out[1] = cnt['o'.charCodeAt(0) - 97] - out[0] - out[2] - out[4];
    out[9] = cnt['i'.charCodeAt(0) - 97] - out[5] - out[6] - out[8];

    let result = '';
    for (let i = 0; i <= 9; ++i) {
        if (out[i] > 0) result += String(i).repeat(out[i]);
    }
    return result;
};
```

## Typescript

```typescript
function originalDigits(s: string): string {
    const cnt = new Array(26).fill(0);
    for (const ch of s) {
        cnt[ch.charCodeAt(0) - 97]++;
    }
    const idx = (c: string) => c.charCodeAt(0) - 97;
    const out = new Array(10).fill(0);
    out[0] = cnt[idx('z')];
    out[2] = cnt[idx('w')];
    out[4] = cnt[idx('u')];
    out[6] = cnt[idx('x')];
    out[8] = cnt[idx('g')];

    out[3] = cnt[idx('h')] - out[8];
    out[5] = cnt[idx('f')] - out[4];
    out[7] = cnt[idx('s')] - out[6];
    out[1] = cnt[idx('o')] - out[0] - out[2] - out[4];
    out[9] = cnt[idx('i')] - out[5] - out[6] - out[8];

    let res = '';
    for (let d = 0; d <= 9; d++) {
        if (out[d] > 0) {
            res += d.toString().repeat(out[d]);
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function originalDigits($s) {
        $cnt = array_fill(0, 26, 0);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $cnt[ord($s[$i]) - 97]++;
        }

        $digitCount = array_fill(0, 10, 0);

        // Unique letters
        $digitCount[0] = $cnt[ord('z') - 97];
        $digitCount[2] = $cnt[ord('w') - 97];
        $digitCount[4] = $cnt[ord('u') - 97];
        $digitCount[6] = $cnt[ord('x') - 97];
        $digitCount[8] = $cnt[ord('g') - 97];

        // Derived counts
        $digitCount[3] = $cnt[ord('h') - 97] - $digitCount[8];
        $digitCount[5] = $cnt[ord('f') - 97] - $digitCount[4];
        $digitCount[7] = $cnt[ord('s') - 97] - $digitCount[6];
        $digitCount[1] = $cnt[ord('o') - 97] - $digitCount[0] - $digitCount[2] - $digitCount[4];
        $digitCount[9] = $cnt[ord('i') - 97] - $digitCount[5] - $digitCount[6] - $digitCount[8];

        $result = '';
        for ($d = 0; $d <= 9; $d++) {
            if ($digitCount[$d] > 0) {
                $result .= str_repeat((string)$d, $digitCount[$d]);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func originalDigits(_ s: String) -> String {
        var cnt = [Int](repeating: 0, count: 26)
        for ch in s {
            if let v = ch.asciiValue {
                let idx = Int(v - 97)
                cnt[idx] += 1
            }
        }
        var digit = [Int](repeating: 0, count: 10)
        // unique letters
        digit[0] = cnt[Int(Character("z").asciiValue! - 97)]
        digit[2] = cnt[Int(Character("w").asciiValue! - 97)]
        digit[4] = cnt[Int(Character("u").asciiValue! - 97)]
        digit[6] = cnt[Int(Character("x").asciiValue! - 97)]
        digit[8] = cnt[Int(Character("g").asciiValue! - 97)]
        // dependent letters
        digit[3] = cnt[Int(Character("h").asciiValue! - 97)] - digit[8]
        digit[5] = cnt[Int(Character("f").asciiValue! - 97)] - digit[4]
        digit[7] = cnt[Int(Character("s").asciiValue! - 97)] - digit[6]
        digit[1] = cnt[Int(Character("o").asciiValue! - 97)] - digit[0] - digit[2] - digit[4]
        digit[9] = cnt[Int(Character("i").asciiValue! - 97)] - digit[5] - digit[6] - digit[8]
        
        var result = ""
        for i in 0...9 {
            if digit[i] > 0 {
                result += String(repeating: "\(i)", count: digit[i])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun originalDigits(s: String): String {
        val cnt = IntArray(26)
        for (ch in s) {
            cnt[ch - 'a']++
        }
        val out = IntArray(10)
        out[0] = cnt['z' - 'a']
        out[2] = cnt['w' - 'a']
        out[4] = cnt['u' - 'a']
        out[6] = cnt['x' - 'a']
        out[8] = cnt['g' - 'a']

        out[3] = cnt['h' - 'a'] - out[8]
        out[5] = cnt['f' - 'a'] - out[4]
        out[7] = cnt['s' - 'a'] - out[6]
        out[1] = cnt['o' - 'a'] - out[0] - out[2] - out[4]
        out[9] = cnt['i' - 'a'] - out[5] - out[6] - out[8]

        val sb = StringBuilder()
        for (d in 0..9) {
            repeat(out[d]) { sb.append(d) }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String originalDigits(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      cnt[s.codeUnitAt(i) - 97]++;
    }

    List<int> digitCnt = List.filled(10, 0);
    // unique letters
    digitCnt[0] = cnt['z'.codeUnitAt(0) - 97];
    digitCnt[2] = cnt['w'.codeUnitAt(0) - 97];
    digitCnt[4] = cnt['u'.codeUnitAt(0) - 97];
    digitCnt[6] = cnt['x'.codeUnitAt(0) - 97];
    digitCnt[8] = cnt['g'.codeUnitAt(0) - 97];

    // letters after removing above digits
    digitCnt[3] = cnt['h'.codeUnitAt(0) - 97] - digitCnt[8];
    digitCnt[5] = cnt['f'.codeUnitAt(0) - 97] - digitCnt[4];
    digitCnt[7] = cnt['s'.codeUnitAt(0) - 97] - digitCnt[6];
    digitCnt[1] = cnt['o'.codeUnitAt(0) - 97] -
        digitCnt[0] -
        digitCnt[2] -
        digitCnt[4];
    digitCnt[9] = cnt['i'.codeUnitAt(0) - 97] -
        digitCnt[5] -
        digitCnt[6] -
        digitCnt[8];

    StringBuffer sb = StringBuffer();
    for (int d = 0; d <= 9; ++d) {
      for (int i = 0; i < digitCnt[d]; ++i) {
        sb.write(d);
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func originalDigits(s string) string {
    cnt := [26]int{}
    for _, ch := range s {
        cnt[ch-'a']++
    }

    out := make([]int, 10)

    // helper to subtract letters of a word multiplied by times
    sub := func(word string, times int) {
        if times == 0 {
            return
        }
        for _, c := range word {
            cnt[c-'a'] -= times
        }
    }

    out[0] = cnt['z'-'a']
    sub("zero", out[0])

    out[2] = cnt['w'-'a']
    sub("two", out[2])

    out[4] = cnt['u'-'a']
    sub("four", out[4])

    out[6] = cnt['x'-'a']
    sub("six", out[6])

    out[8] = cnt['g'-'a']
    sub("eight", out[8])

    out[3] = cnt['h'-'a']
    sub("three", out[3])

    out[5] = cnt['f'-'a']
    sub("five", out[5])

    out[7] = cnt['s'-'a']
    sub("seven", out[7])

    out[1] = cnt['o'-'a']
    sub("one", out[1])

    out[9] = cnt['i'-'a']

    var sb strings.Builder
    for d := 0; d <= 9; d++ {
        for i := 0; i < out[d]; i++ {
            sb.WriteByte(byte('0' + d))
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def original_digits(s)
  cnt = Array.new(26, 0)
  s.each_byte { |b| cnt[b - 97] += 1 }

  digits = Array.new(10, 0)

  # unique letters
  digits[0] = cnt['z'.ord - 97]
  digits[2] = cnt['w'.ord - 97]
  digits[4] = cnt['u'.ord - 97]
  digits[6] = cnt['x'.ord - 97]
  digits[8] = cnt['g'.ord - 97]

  words = %w[zero one two three four five six seven eight nine]

  # subtract letters for already identified digits
  [0, 2, 4, 6, 8].each do |d|
    count = digits[d]
    next if count.zero?
    words[d].each_byte { |b| cnt[b - 97] -= count }
  end

  # remaining digits based on now-unique letters
  digits[3] = cnt['h'.ord - 97]   # three after eight removed
  digits[5] = cnt['f'.ord - 97]   # five after four removed
  digits[7] = cnt['s'.ord - 97]   # seven after six removed
  digits[1] = cnt['o'.ord - 97]   # one after zero, two, four removed
  digits[9] = cnt['i'.ord - 97]   # nine after five, six, eight removed

  # subtract letters for these digits as well (optional, not needed further)
  [3, 5, 7, 1, 9].each do |d|
    count = digits[d]
    next if count.zero?
    words[d].each_byte { |b| cnt[b - 97] -= count }
  end

  result = +''
  (0..9).each { |i| result << i.to_s * digits[i] }
  result
end
```

## Scala

```scala
object Solution {
    def originalDigits(s: String): String = {
        val cnt = new Array[Int](26)
        for (c <- s) cnt(c - 'a') += 1

        val out = new Array[Int](10)

        out(0) = cnt('z' - 'a')
        out(2) = cnt('w' - 'a')
        out(4) = cnt('u' - 'a')
        out(6) = cnt('x' - 'a')
        out(8) = cnt('g' - 'a')

        out(3) = cnt('h' - 'a') - out(8)
        out(5) = cnt('f' - 'a') - out(4)
        out(7) = cnt('s' - 'a') - out(6)
        out(1) = cnt('o' - 'a') - out(0) - out(2) - out(4)
        out(9) = cnt('i' - 'a') - out(5) - out(6) - out(8)

        val sb = new StringBuilder
        for (d <- 0 to 9) {
            var i = out(d)
            while (i > 0) {
                sb.append(('0' + d).toChar)
                i -= 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn original_digits(s: String) -> String {
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut digit_cnt = [0i32; 10];

        // Unique letters
        digit_cnt[0] = cnt[(b'z' - b'a') as usize];
        digit_cnt[2] = cnt[(b'w' - b'a') as usize];
        digit_cnt[4] = cnt[(b'u' - b'a') as usize];
        digit_cnt[6] = cnt[(b'x' - b'a') as usize];
        digit_cnt[8] = cnt[(b'g' - b'a') as usize];

        // Derived counts
        digit_cnt[3] = cnt[(b'h' - b'a') as usize] - digit_cnt[8];
        digit_cnt[5] = cnt[(b'f' - b'a') as usize] - digit_cnt[4];
        digit_cnt[7] = cnt[(b's' - b'a') as usize] - digit_cnt[6];
        digit_cnt[1] = cnt[(b'o' - b'a') as usize] - digit_cnt[0] - digit_cnt[2] - digit_cnt[4];
        digit_cnt[9] = cnt[(b'i' - b'a') as usize] - digit_cnt[5] - digit_cnt[6] - digit_cnt[8];

        let mut result = String::new();
        for d in 0..10 {
            for _ in 0..digit_cnt[d] {
                result.push((b'0' + d as u8) as char);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (original-digits s)
  (-> string? string?)
  (let* ([cnt (make-vector 26 0)]
         [char-index (lambda (ch) (- (char->integer ch) (char->integer #\a)))]
         [_ (for ([ch (in-string s)])
              (let* ([i (char-index ch)]
                     [new (+ (vector-ref cnt i) 1)])
                (vector-set! cnt i new)))])
    ;; helper to subtract letters of a word multiplied by times
    (define (subtract-word word times)
      (for ([ch (in-string word)])
        (let* ([i (char-index ch)]
               [new (- (vector-ref cnt i) times)])
          (vector-set! cnt i new))))
    (define digits (make-vector 10 0))
    ;; unique letters
    (vector-set! digits 0 (vector-ref cnt (char-index #\z)))
    (subtract-word "zero" (vector-ref digits 0))
    (vector-set! digits 2 (vector-ref cnt (char-index #\w)))
    (subtract-word "two" (vector-ref digits 2))
    (vector-set! digits 4 (vector-ref cnt (char-index #\u)))
    (subtract-word "four" (vector-ref digits 4))
    (vector-set! digits 6 (vector-ref cnt (char-index #\x)))
    (subtract-word "six" (vector-ref digits 6))
    (vector-set! digits 8 (vector-ref cnt (char-index #\g)))
    (subtract-word "eight" (vector-ref digits 8))
    ;; remaining letters
    (vector-set! digits 3 (vector-ref cnt (char-index #\h))) ; after eight removed
    (subtract-word "three" (vector-ref digits 3))
    (vector-set! digits 5 (vector-ref cnt (char-index #\f))) ; after four removed
    (subtract-word "five" (vector-ref digits 5))
    (vector-set! digits 7 (vector-ref cnt (char-index #\s))) ; after six removed
    (subtract-word "seven" (vector-ref digits 7))
    (vector-set! digits 9 (vector-ref cnt (char-index #\i))) ; after five, six, eight removed
    (subtract-word "nine" (vector-ref digits 9))
    (vector-set! digits 1 (vector-ref cnt (char-index #\o))) ; after zero, two, four removed
    ;; build result string
    (let ([out (open-output-string)])
      (for ([d (in-range 10)])
        (let ([c (vector-ref digits d)])
          (when (> c 0)
            (for (_ (in-range c))
              (write-char (integer->char (+ (char->integer #\0) d)) out)))))
      (get-output-string out))))
```

## Erlang

```erlang
-spec original_digits(unicode:unicode_binary()) -> unicode:unicode_binary().
original_digits(S) ->
    Counts = lists:foldl(
        fun(C, Acc) ->
            maps:update_with(C,
                fun(V) -> V + 1 end,
                1,
                Acc)
        end,
        #{},
        binary_to_list(S)),
    C0 = maps:get($z, Counts, 0),
    C2 = maps:get($w, Counts, 0),
    C4 = maps:get($u, Counts, 0),
    C6 = maps:get($x, Counts, 0),
    C8 = maps:get($g, Counts, 0),

    C3 = maps:get($h, Counts, 0) - C8,
    C5 = maps:get($f, Counts, 0) - C4,
    C7 = maps:get($s, Counts, 0) - C6,
    C1 = maps:get($o, Counts, 0) - C0 - C2 - C4,
    C9 = maps:get($i, Counts, 0) - C5 - C6 - C8,

    Iolist = [
        lists:duplicate(C0, $0),
        lists:duplicate(C1, $1),
        lists:duplicate(C2, $2),
        lists:duplicate(C3, $3),
        lists:duplicate(C4, $4),
        lists:duplicate(C5, $5),
        lists:duplicate(C6, $6),
        lists:duplicate(C7, $7),
        lists:duplicate(C8, $8),
        lists:duplicate(C9, $9)
    ],
    iolist_to_binary(Iolist).
```

## Elixir

```elixir
defmodule Solution do
  @spec original_digits(s :: String.t()) :: String.t()
  def original_digits(s) do
    freq =
      s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    zero = Map.get(freq, "z", 0)
    two = Map.get(freq, "w", 0)
    four = Map.get(freq, "u", 0)
    six = Map.get(freq, "x", 0)
    eight = Map.get(freq, "g", 0)

    three = Map.get(freq, "h", 0) - eight
    five = Map.get(freq, "f", 0) - four
    seven = Map.get(freq, "s", 0) - six
    nine = Map.get(freq, "i", 0) - five - six - eight
    one = Map.get(freq, "o", 0) - zero - two - four

    Enum.reduce(0..9, "", fn d, acc ->
      count =
        case d do
          0 -> zero
          1 -> one
          2 -> two
          3 -> three
          4 -> four
          5 -> five
          6 -> six
          7 -> seven
          8 -> eight
          9 -> nine
        end

      acc <> String.duplicate(Integer.to_string(d), count)
    end)
  end
end
```
