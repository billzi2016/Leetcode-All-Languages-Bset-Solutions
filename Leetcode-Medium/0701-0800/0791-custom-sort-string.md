# 0791. Custom Sort String

## Cpp

```cpp
class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> freq(26, 0);
        for (char c : s) ++freq[c - 'a'];
        string result;
        result.reserve(s.size());
        for (char c : order) {
            int idx = c - 'a';
            while (freq[idx]--) result.push_back(c);
        }
        for (int i = 0; i < 26; ++i) {
            while (freq[i]--) result.push_back('a' + i);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String customSortString(String order, String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        for (char c : order.toCharArray()) {
            int idx = c - 'a';
            while (freq[idx] > 0) {
                sb.append(c);
                freq[idx]--;
            }
        }
        for (int i = 0; i < 26; i++) {
            while (freq[i] > 0) {
                sb.append((char) ('a' + i));
                freq[i]--;
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        res = []
        for ch in order:
            idx = ord(ch) - 97
            if cnt[idx]:
                res.append(ch * cnt[idx])
                cnt[idx] = 0

        for i in range(26):
            if cnt[i]:
                res.append(chr(i + 97) * cnt[i])

        return ''.join(res)
```

## Python3

```python
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        result_parts = []
        for ch in order:
            idx = ord(ch) - 97
            if freq[idx]:
                result_parts.append(ch * freq[idx])
                freq[idx] = 0

        for i in range(26):
            if freq[i]:
                result_parts.append(chr(i + 97) * freq[i])

        return ''.join(result_parts)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* customSortString(char* order, char* s) {
    int freq[26] = {0};
    for (char *p = s; *p; ++p) {
        freq[*p - 'a']++;
    }

    size_t len = strlen(s);
    char *res = (char *)malloc(len + 1);
    if (!res) return NULL;

    size_t pos = 0;
    for (char *p = order; *p; ++p) {
        int idx = *p - 'a';
        while (freq[idx]-- > 0) {
            res[pos++] = *p;
        }
    }

    for (int i = 0; i < 26; ++i) {
        while (freq[i]-- > 0) {
            res[pos++] = (char)('a' + i);
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
    public string CustomSortString(string order, string s)
    {
        int[] freq = new int[26];
        foreach (char c in s)
            freq[c - 'a']++;

        var sb = new System.Text.StringBuilder();

        foreach (char c in order)
        {
            int idx = c - 'a';
            while (freq[idx] > 0)
            {
                sb.Append(c);
                freq[idx]--;
            }
        }

        for (int i = 0; i < 26; i++)
        {
            while (freq[i] > 0)
            {
                sb.Append((char)('a' + i));
                freq[i]--;
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} order
 * @param {string} s
 * @return {string}
 */
var customSortString = function(order, s) {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    
    const result = [];
    for (const ch of order) {
        const idx = ch.charCodeAt(0) - 97;
        while (freq[idx] > 0) {
            result.push(ch);
            freq[idx]--;
        }
    }
    
    for (let i = 0; i < 26; i++) {
        while (freq[i] > 0) {
            result.push(String.fromCharCode(i + 97));
            freq[i]--;
        }
    }
    
    return result.join('');
};
```

## Typescript

```typescript
function customSortString(order: string, s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let result = '';
    for (const ch of order) {
        const idx = ch.charCodeAt(0) - 97;
        if (freq[idx] > 0) {
            result += ch.repeat(freq[idx]);
            freq[idx] = 0;
        }
    }
    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            const ch = String.fromCharCode(i + 97);
            result += ch.repeat(freq[i]);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $order
     * @param String $s
     * @return String
     */
    function customSortString($order, $s) {
        // Frequency array for letters a-z
        $freq = array_fill(0, 26, 0);
        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        // Build result following the custom order
        $result = '';
        $lenO = strlen($order);
        for ($i = 0; $i < $lenO; $i++) {
            $c = $order[$i];
            $idx = ord($c) - 97;
            while ($freq[$idx] > 0) {
                $result .= $c;
                $freq[$idx]--;
            }
        }

        // Append remaining characters not in order
        for ($i = 0; $i < 26; $i++) {
            while ($freq[$i] > 0) {
                $result .= chr($i + 97);
                $freq[$i]--;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        var freq = [Int](repeating: 0, count: 26)
        for ch in s {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            freq[idx] += 1
        }
        var result = ""
        for ch in order {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            while freq[idx] > 0 {
                result.append(ch)
                freq[idx] -= 1
            }
        }
        for i in 0..<26 {
            while freq[i] > 0 {
                let ch = Character(UnicodeScalar(i + 97)!)
                result.append(ch)
                freq[i] -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun customSortString(order: String, s: String): String {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        val sb = StringBuilder()
        for (ch in order) {
            val idx = ch - 'a'
            repeat(freq[idx]) { sb.append(ch) }
            freq[idx] = 0
        }
        for (i in 0 until 26) {
            repeat(freq[i]) { sb.append(('a'.code + i).toChar()) }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String customSortString(String order, String s) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      freq[idx]++;
    }

    StringBuffer sb = StringBuffer();

    for (int i = 0; i < order.length; i++) {
      int idx = order.codeUnitAt(i) - 97;
      while (freq[idx] > 0) {
        sb.writeCharCode(order.codeUnitAt(i));
        freq[idx]--;
      }
    }

    for (int i = 0; i < 26; i++) {
      while (freq[i] > 0) {
        sb.writeCharCode(i + 97);
        freq[i]--;
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

func customSortString(order string, s string) string {
	cnt := [26]int{}
	for _, ch := range s {
		cnt[ch-'a']++
	}
	var b strings.Builder
	b.Grow(len(s))
	for _, ch := range order {
		idx := ch - 'a'
		for cnt[idx] > 0 {
			b.WriteByte(byte(ch))
			cnt[idx]--
		}
	}
	for i := 0; i < 26; i++ {
		for cnt[i] > 0 {
			b.WriteByte('a' + byte(i))
			cnt[i]--
		}
	}
	return b.String()
}
```

## Ruby

```ruby
# @param {String} order
# @param {String} s
# @return {String}
def custom_sort_string(order, s)
  count = Array.new(26, 0)
  s.each_byte { |b| count[b - 97] += 1 }

  result = +""
  order.each_byte do |b|
    idx = b - 97
    cnt = count[idx]
    if cnt > 0
      result << (b.chr * cnt)
      count[idx] = 0
    end
  end

  26.times do |i|
    cnt = count[i]
    result << ((i + 97).chr * cnt) if cnt > 0
  end

  result
end
```

## Scala

```scala
object Solution {
    def customSortString(order: String, s: String): String = {
        val freq = new Array[Int](26)
        for (c <- s) {
            freq(c - 'a') += 1
        }
        val sb = new java.lang.StringBuilder()
        for (c <- order) {
            var idx = c - 'a'
            while (freq(idx) > 0) {
                sb.append(c)
                freq(idx) -= 1
            }
        }
        for (i <- 0 until 26) {
            var count = freq(i)
            val ch = ('a' + i).toChar
            while (count > 0) {
                sb.append(ch)
                count -= 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut freq = [0usize; 26];
        for ch in s.bytes() {
            freq[(ch - b'a') as usize] += 1;
        }

        let mut result = String::with_capacity(s.len());

        for ch in order.bytes() {
            let idx = (ch - b'a') as usize;
            while freq[idx] > 0 {
                result.push(ch as char);
                freq[idx] -= 1;
            }
        }

        for i in 0..26 {
            while freq[i] > 0 {
                result.push((b'a' + i as u8) as char);
                freq[i] -= 1;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (custom-sort-string order s)
  (-> string? string? string?)
  (let* ([freq (make-vector 26 0)])
    ;; Count frequencies in s
    (for ([c (in-string s)])
      (let* ([idx (- (char->integer c) (char->integer #\a))]
             [old (vector-ref freq idx)])
        (vector-set! freq idx (+ old 1))))
    ;; Build result list according to order
    (define result '())
    (for ([c (in-string order)])
      (let* ([idx (- (char->integer c) (char->integer #\a))]
             [cnt (vector-ref freq idx)])
        (when (> cnt 0)
          (for (_ (in-range cnt))
            (set! result (cons c result))))
        (vector-set! freq idx 0)))
    ;; Append remaining characters not in order
    (for ([i (in-range 26)])
      (let* ([cnt (vector-ref freq i)]
             [ch (integer->char (+ (char->integer #\a) i))])
        (when (> cnt 0)
          (for (_ (in-range cnt))
            (set! result (cons ch result))))))
    ;; Convert list of chars to string
    (list->string (reverse result))))
```

## Erlang

```erlang
-module(solution).
-export([custom_sort_string/2]).

-spec custom_sort_string(Order :: unicode:unicode_binary(), S :: unicode:unicode_binary()) -> unicode:unicode_binary().
custom_sort_string(Order, S) ->
    OrderList = binary:bin_to_list(Order),
    SList = binary:bin_to_list(S),
    FreqMap0 = build_freq_map(SList, #{}),
    {PartialList, FreqMap1} = add_order_chars(OrderList, FreqMap0, []),
    FinalList = add_remaining(PartialList, FreqMap1),
    list_to_binary(FinalList).

build_freq_map([], Map) -> Map;
build_freq_map([C|Rest], Map) ->
    Index = C - $a,
    Count = maps:get(Index, Map, 0),
    NewMap = maps:put(Index, Count + 1, Map),
    build_freq_map(Rest, NewMap).

add_order_chars([], Map, Acc) -> {Acc, Map};
add_order_chars([C|Rest], Map, Acc) ->
    Index = C - $a,
    Count = maps:get(Index, Map, 0),
    NewAcc = case Count of
        0 -> Acc;
        _ -> Acc ++ lists:duplicate(Count, C)
    end,
    UpdatedMap = maps:put(Index, 0, Map),
    add_order_chars(Rest, UpdatedMap, NewAcc).

add_remaining(Acc, Map) ->
    maps:fold(fun(Index, Count, A) ->
        case Count of
            0 -> A;
            _ ->
                Char = $a + Index,
                A ++ lists:duplicate(Count, Char)
        end
    end, Acc, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec custom_sort_string(order :: String.t(), s :: String.t()) :: String.t()
  def custom_sort_string(order, s) do
    freq =
      :binary.bin_to_list(s)
      |> Enum.reduce(%{}, fn c, acc ->
        ch = <<c>>
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    order_chars = String.graphemes(order)

    ordered_parts =
      Enum.map(order_chars, fn ch ->
        cnt = Map.get(freq, ch, 0)
        if cnt > 0, do: String.duplicate(ch, cnt), else: ""
      end)

    leftover_parts =
      freq
      |> Enum.reject(fn {ch, _cnt} -> ch in order_chars end)
      |> Enum.map(fn {ch, cnt} -> String.duplicate(ch, cnt) end)

    (ordered_parts ++ leftover_parts) |> Enum.join()
  end
end
```
