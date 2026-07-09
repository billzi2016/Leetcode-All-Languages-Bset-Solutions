# 3438. Find Valid Pair of Adjacent Digits in String

## Cpp

```cpp
class Solution {
public:
    string findValidPair(string s) {
        int cnt[10] = {0};
        for (char c : s) cnt[c - '0']++;
        for (int i = 0; i + 1 < (int)s.size(); ++i) {
            int d1 = s[i] - '0';
            int d2 = s[i+1] - '0';
            if (cnt[d1] == d1 && cnt[d2] == d2) {
                return string() + s[i] + s[i+1];
            }
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String findValidPair(String s) {
        int[] freq = new int[10];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - '0']++;
        }
        for (int i = 0; i < s.length() - 1; i++) {
            char a = s.charAt(i);
            char b = s.charAt(i + 1);
            if (a == b) continue;
            int da = a - '0';
            int db = b - '0';
            if (freq[da] == da && freq[db] == db) {
                return "" + a + b;
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        n = len(s)
        for i in range(n - 1):
            a, b = s[i], s[i + 1]
            if freq[a] == int(a) and freq[b] == int(b):
                return a + b
        return ""
```

## Python3

```python
class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter
        freq = Counter(s)
        n = len(s)
        for i in range(n - 1):
            a, b = s[i], s[i + 1]
            if freq[a] == int(a) and freq[b] == int(b):
                return a + b
        return ""
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* findValidPair(char* s) {
    int cnt[10] = {0};
    size_t len = strlen(s);
    for (size_t i = 0; i < len; ++i) {
        cnt[s[i] - '0']++;
    }
    for (size_t i = 0; i + 1 < len; ++i) {
        int d1 = s[i] - '0';
        int d2 = s[i + 1] - '0';
        if (cnt[d1] == d1 && cnt[d2] == d2) {
            char* res = (char*)malloc(3);
            res[0] = s[i];
            res[1] = s[i + 1];
            res[2] = '\0';
            return res;
        }
    }
    char* empty = (char*)malloc(1);
    empty[0] = '\0';
    return empty;
}
```

## Csharp

```csharp
public class Solution
{
    public string FindValidPair(string s)
    {
        int[] freq = new int[10];
        foreach (char c in s)
            freq[c - '0']++;

        for (int i = 0; i < s.Length - 1; i++)
        {
            char a = s[i], b = s[i + 1];
            if (a == b) continue;
            int da = a - '0', db = b - '0';
            if (freq[da] == da && freq[db] == db)
                return new string(new[] { a, b });
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var findValidPair = function(s) {
    const cnt = Array(10).fill(0);
    for (const ch of s) {
        cnt[ch.charCodeAt(0) - 48]++;
    }
    for (let i = 0; i < s.length - 1; i++) {
        const a = s[i];
        const b = s[i + 1];
        if (a === b) continue;
        const da = a.charCodeAt(0) - 48;
        const db = b.charCodeAt(0) - 48;
        if (cnt[da] === da && cnt[db] === db) {
            return a + b;
        }
    }
    return "";
};
```

## Typescript

```typescript
function findValidPair(s: string): string {
    const freq = new Array(10).fill(0);
    for (const ch of s) {
        const d = ch.charCodeAt(0) - 48;
        freq[d]++;
    }
    for (let i = 0; i < s.length - 1; i++) {
        const a = s[i];
        const b = s[i + 1];
        if (a === b) continue;
        const da = a.charCodeAt(0) - 48;
        const db = b.charCodeAt(0) - 48;
        if (freq[da] === da && freq[db] === db) {
            return a + b;
        }
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function findValidPair($s) {
        $len = strlen($s);
        $freq = [];
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($freq[$c])) {
                $freq[$c] = 0;
            }
            $freq[$c]++;
        }

        for ($i = 0; $i < $len - 1; $i++) {
            $a = $s[$i];
            $b = $s[$i + 1];
            if ($a !== $b && $freq[$a] == intval($a) && $freq[$b] == intval($b)) {
                return $a . $b;
            }
        }

        return "";
    }
}
```

## Swift

```swift
class Solution {
    func findValidPair(_ s: String) -> String {
        var freq = [Int](repeating: 0, count: 10)
        for ch in s {
            if let val = ch.wholeNumberValue {
                freq[val] += 1
            }
        }
        let chars = Array(s)
        for i in 0..<(chars.count - 1) {
            let c1 = chars[i]
            let c2 = chars[i + 1]
            if c1 == c2 { continue }
            guard let v1 = c1.wholeNumberValue, let v2 = c2.wholeNumberValue else { continue }
            if freq[v1] == v1 && freq[v2] == v2 {
                return String([c1, c2])
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findValidPair(s: String): String {
        val freq = IntArray(10)
        for (ch in s) {
            freq[ch - '0']++
        }
        for (i in 0 until s.length - 1) {
            val a = s[i]
            val b = s[i + 1]
            if (a != b && freq[a - '0'] == (a - '0') && freq[b - '0'] == (b - '0')) {
                return s.substring(i, i + 2)
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String findValidPair(String s) {
    // Count frequency of each digit
    final Map<String, int> freq = {};
    for (var ch in s.split('')) {
      freq[ch] = (freq[ch] ?? 0) + 1;
    }

    // Scan adjacent pairs from left to right
    for (int i = 0; i < s.length - 1; ++i) {
      String a = s[i];
      String b = s[i + 1];
      if (a == b) continue;
      int valA = int.parse(a);
      int valB = int.parse(b);
      if ((freq[a] ?? 0) == valA && (freq[b] ?? 0) == valB) {
        return a + b;
      }
    }

    return "";
  }
}
```

## Golang

```go
func findValidPair(s string) string {
	freq := [10]int{}
	for i := 0; i < len(s); i++ {
		d := s[i] - '0'
		freq[d]++
	}
	for i := 0; i+1 < len(s); i++ {
		a, b := s[i], s[i+1]
		if a == b {
			continue
		}
		da, db := a-'0', b-'0'
		if freq[da] == int(da) && freq[db] == int(db) {
			return s[i : i+2]
		}
	}
	return ""
}
```

## Ruby

```ruby
def find_valid_pair(s)
  freq = Hash.new(0)
  s.each_char { |ch| freq[ch] += 1 }
  (0...s.length - 1).each do |i|
    a = s[i]
    b = s[i + 1]
    next if a == b
    return a + b if freq[a] == a.to_i && freq[b] == b.to_i
  end
  ""
end
```

## Scala

```scala
object Solution {
    def findValidPair(s: String): String = {
        val freq = new Array[Int](10)
        for (ch <- s) {
            freq(ch - '0') += 1
        }
        for (i <- 0 until s.length - 1) {
            val a = s.charAt(i)
            val b = s.charAt(i + 1)
            if (a != b && freq(a - '0') == (a - '0') && freq(b - '0') == (b - '0')) {
                return s.substring(i, i + 2)
            }
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_valid_pair(s: String) -> String {
        let bytes = s.as_bytes();
        let mut cnt = [0usize; 10];
        for &b in bytes {
            let d = (b - b'0') as usize;
            cnt[d] += 1;
        }
        for i in 0..bytes.len() - 1 {
            let d1 = (bytes[i] - b'0') as usize;
            let d2 = (bytes[i + 1] - b'0') as usize;
            if d1 != d2 && cnt[d1] == d1 && cnt[d2] == d2 {
                return String::from_utf8(vec![bytes[i], bytes[i + 1]]).unwrap();
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (find-valid-pair s)
  (-> string? string?)
  (let* ([len (string-length s)]
         [freq (make-vector 10 0)])
    ;; count frequencies of each digit
    (for ([i (in-range len)])
      (let* ([c (string-ref s i)]
             [d (- (char->integer c) (char->integer #\0))])
        (vector-set! freq d (+ (vector-ref freq d) 1))))
    ;; find first valid adjacent pair
    (let loop ([i 0])
      (if (>= i (- len 1))
          ""
          (let* ([c1 (string-ref s i)]
                 [c2 (string-ref s (+ i 1))]
                 [d1 (- (char->integer c1) (char->integer #\0))]
                 [d2 (- (char->integer c2) (char->integer #\0))])
            (if (and (= (vector-ref freq d1) d1)
                     (= (vector-ref freq d2) d2))
                (substring s i (+ i 2))
                (loop (+ i 1))))))))
```

## Erlang

```erlang
-spec find_valid_pair(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
find_valid_pair(S) ->
    CountMap = count_digits(S),
    find_pair(binary_to_list(S), CountMap).

count_digits(S) ->
    lists:foldl(fun(C, Acc) ->
        maps:update_with(C,
            fun(Old) -> Old + 1 end,
            1,
            Acc)
    end, #{}, binary_to_list(S)).

find_pair([_], _Map) -> <<>>;
find_pair([], _Map) -> <<>>;
find_pair([C1, C2 | Rest] = List, Map) ->
    case {valid(C1, Map), valid(C2, Map)} of
        {true, true} -> <<C1, C2>>;
        _ -> find_pair([C2 | Rest], Map)
    end.

valid(Char, Map) ->
    case maps:get(Char, Map, 0) of
        Count when Count =:= Char - $0 -> true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_valid_pair(s :: String.t()) :: String.t()
  def find_valid_pair(s) do
    counts =
      s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    graphemes = String.graphemes(s)
    len = length(graphemes)

    result =
      0..(len - 2)
      |> Enum.find_value(fn i ->
        a = Enum.at(graphemes, i)
        b = Enum.at(graphemes, i + 1)

        if a != b and
             Map.get(counts, a) == String.to_integer(a) and
             Map.get(counts, b) == String.to_integer(b) do
          a <> b
        else
          nil
        end
      end)

    result || ""
  end
end
```
