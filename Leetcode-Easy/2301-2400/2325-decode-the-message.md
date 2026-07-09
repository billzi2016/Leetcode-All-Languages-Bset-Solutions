# 2325. Decode the Message

## Cpp

```cpp
class Solution {
public:
    string decodeMessage(string key, string message) {
        unordered_map<char, char> mp;
        char cur = 'a';
        for (char c : key) {
            if (c == ' ') continue;
            if (!mp.count(c)) {
                mp[c] = cur++;
            }
        }
        string res;
        res.reserve(message.size());
        for (char c : message) {
            if (c == ' ') res.push_back(' ');
            else res.push_back(mp[c]);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String decodeMessage(String key, String message) {
        char[] mapping = new char[26];
        boolean[] visited = new boolean[26];
        int cur = 0;
        for (char c : key.toCharArray()) {
            if (c == ' ') continue;
            int idx = c - 'a';
            if (!visited[idx]) {
                mapping[idx] = (char) ('a' + cur);
                visited[idx] = true;
                cur++;
                if (cur == 26) break;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c == ' ') {
                sb.append(' ');
            } else {
                sb.append(mapping[c - 'a']);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {}
        cur_ord = ord('a')
        for ch in key:
            if ch == ' ':
                continue
            if ch not in mapping:
                mapping[ch] = chr(cur_ord)
                cur_ord += 1
                if cur_ord > ord('z'):
                    break
        decoded = []
        for ch in message:
            if ch == ' ':
                decoded.append(' ')
            else:
                decoded.append(mapping[ch])
        return ''.join(decoded)
```

## Python3

```python
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        nxt = ord('a')
        for ch in key:
            if ch == ' ' or ch in mapping:
                continue
            mapping[ch] = chr(nxt)
            nxt += 1
            if nxt > ord('z'):
                break
        return ''.join(mapping[c] if c != ' ' else ' ' for c in message)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* decodeMessage(char* key, char* message) {
    char map[26] = {0};
    int next = 0;
    for (int i = 0; key[i]; ++i) {
        char c = key[i];
        if (c == ' ') continue;
        int idx = c - 'a';
        if (!map[idx]) {
            map[idx] = 'a' + next;
            ++next;
            if (next == 26) break;
        }
    }

    size_t len = strlen(message);
    char* res = (char*)malloc(len + 1);
    for (size_t i = 0; i < len; ++i) {
        char c = message[i];
        if (c == ' ') {
            res[i] = ' ';
        } else {
            res[i] = map[c - 'a'];
        }
    }
    res[len] = '\0';
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string DecodeMessage(string key, string message) {
        var map = new Dictionary<char, char>();
        char cur = 'a';
        foreach (char c in key) {
            if (c == ' ') continue;
            if (!map.ContainsKey(c)) {
                map[c] = cur;
                cur++;
                if (cur > 'z') break;
            }
        }

        var sb = new StringBuilder(message.Length);
        foreach (char c in message) {
            if (c == ' ') sb.Append(' ');
            else sb.Append(map[c]);
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    const mapping = new Map();
    let nextCharCode = 97; // 'a'
    for (const ch of key) {
        if (ch === ' ') continue;
        if (!mapping.has(ch)) {
            mapping.set(ch, String.fromCharCode(nextCharCode));
            nextCharCode++;
            if (nextCharCode > 122) break; // beyond 'z', safety
        }
    }
    let decoded = '';
    for (const ch of message) {
        decoded += ch === ' ' ? ' ' : mapping.get(ch);
    }
    return decoded;
};
```

## Typescript

```typescript
function decodeMessage(key: string, message: string): string {
    const map = new Map<string, string>();
    let nextCode = 97; // 'a'
    for (const ch of key) {
        if (ch === ' ') continue;
        if (!map.has(ch)) {
            map.set(ch, String.fromCharCode(nextCode));
            nextCode++;
        }
    }
    const decoded: string[] = [];
    for (const ch of message) {
        if (ch === ' ') {
            decoded.push(' ');
        } else {
            decoded.push(map.get(ch)!);
        }
    }
    return decoded.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $key
     * @param String $message
     * @return String
     */
    function decodeMessage($key, $message) {
        $map = [];
        $nextCharCode = ord('a');
        foreach (str_split($key) as $c) {
            if ($c === ' ') continue;
            if (!isset($map[$c])) {
                $map[$c] = chr($nextCharCode);
                $nextCharCode++;
                if ($nextCharCode > ord('z')) break;
            }
        }

        $decoded = '';
        foreach (str_split($message) as $ch) {
            if ($ch === ' ') {
                $decoded .= ' ';
            } else {
                $decoded .= $map[$ch];
            }
        }
        return $decoded;
    }
}
```

## Swift

```swift
class Solution {
    func decodeMessage(_ key: String, _ message: String) -> String {
        var mapping = [Character: Character]()
        var nextIdx = 0
        let aValue = Int(Character("a").unicodeScalars.first!.value)
        
        for ch in key {
            if ch == " " { continue }
            if mapping[ch] == nil {
                let mappedChar = Character(UnicodeScalar(aValue + nextIdx)!)
                mapping[ch] = mappedChar
                nextIdx += 1
                if nextIdx == 26 { break }
            }
        }
        
        var result = ""
        for ch in message {
            if ch == " " {
                result.append(" ")
            } else if let decoded = mapping[ch] {
                result.append(decoded)
            } else {
                result.append(ch) // fallback, shouldn't occur
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decodeMessage(key: String, message: String): String {
        val mapping = HashMap<Char, Char>()
        var next = 'a'
        for (c in key) {
            if (c == ' ') continue
            if (!mapping.containsKey(c)) {
                mapping[c] = next
                next++
                if (next > 'z') break
            }
        }
        val sb = StringBuilder()
        for (c in message) {
            sb.append(if (c == ' ') ' ' else mapping[c])
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String decodeMessage(String key, String message) {
    final Map<String, String> map = {};
    int nextCode = 'a'.codeUnitAt(0);
    for (int i = 0; i < key.length; i++) {
      final ch = key[i];
      if (ch != ' ' && !map.containsKey(ch)) {
        map[ch] = String.fromCharCode(nextCode);
        nextCode++;
      }
    }

    final StringBuffer sb = StringBuffer();
    for (int i = 0; i < message.length; i++) {
      final ch = message[i];
      if (ch == ' ') {
        sb.write(' ');
      } else {
        sb.write(map[ch]);
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func decodeMessage(key string, message string) string {
    var mp [256]byte
    next := byte('a')
    for i := 0; i < len(key); i++ {
        c := key[i]
        if c != ' ' && mp[c] == 0 {
            mp[c] = next
            next++
        }
    }
    res := make([]byte, len(message))
    for i := 0; i < len(message); i++ {
        c := message[i]
        if c == ' ' {
            res[i] = ' '
        } else {
            res[i] = mp[c]
        }
    }
    return string(res)
}
```

## Ruby

```ruby
def decode_message(key, message)
  mapping = {}
  next_char_code = 'a'.ord
  key.each_char do |ch|
    next if ch == ' '
    unless mapping.key?(ch)
      mapping[ch] = next_char_code.chr
      next_char_code += 1
    end
  end
  message.chars.map { |c| c == ' ' ? ' ' : mapping[c] }.join
end
```

## Scala

```scala
object Solution {
    def decodeMessage(key: String, message: String): String = {
        val map = scala.collection.mutable.Map[Char, Char]()
        var cur = 'a'
        for (ch <- key) {
            if (ch != ' ' && !map.contains(ch)) {
                map(ch) = cur
                cur = (cur + 1).toChar
            }
        }
        val sb = new StringBuilder
        for (ch <- message) {
            if (ch == ' ') sb.append(' ')
            else sb.append(map(ch))
        }
        sb.toString()
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn decode_message(key: String, message: String) -> String {
        let mut map: HashMap<char, char> = HashMap::new();
        let mut next = b'a';
        for ch in key.chars() {
            if ch == ' ' { continue; }
            if !map.contains_key(&ch) {
                map.insert(ch, next as char);
                next += 1;
                if next > b'z' { break; }
            }
        }
        let mut res = String::with_capacity(message.len());
        for ch in message.chars() {
            if ch == ' ' {
                res.push(' ');
            } else if let Some(&c) = map.get(&ch) {
                res.push(c);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (decode-message key message)
  (-> string? string? string?)
  (let ([hash (make-hash)])
    (define idx 0)
    (for ([c (in-string key)])
      (when (and (not (char=? c #\space))
                 (not (hash-has-key? hash c)))
        (hash-set! hash c (integer->char (+ (char->integer #\a) idx)))
        (set! idx (add1 idx))))
    (list->string
      (for/list ([c (in-string message)])
        (if (char=? c #\space)
            c
            (hash-ref hash c))))))
```

## Erlang

```erlang
-spec decode_message(Key :: unicode:unicode_binary(), Message :: unicode:unicode_binary()) -> unicode:unicode_binary().
decode_message(Key, Message) ->
    {Map,_} = build_map(binary_to_list(Key), #{}, $a),
    Decoded = [decode_char(C, Map) || C <- binary_to_list(Message)],
    list_to_binary(Decoded).

build_map([], Map, _Next) -> {Map, undefined};
build_map([C|Rest], Map, Next) when C == $\s ->
    build_map(Rest, Map, Next);
build_map([C|Rest], Map, Next) ->
    case maps:is_key(C, Map) of
        true  -> build_map(Rest, Map, Next);
        false -> build_map(Rest, maps:put(C, Next, Map), Next+1)
    end.

decode_char(C, _Map) when C == $\s -> $ ;
decode_char(C, Map) -> maps:get(C, Map).
```

## Elixir

```elixir
defmodule Solution do
  @spec decode_message(key :: String.t(), message :: String.t()) :: String.t()
  def decode_message(key, message) do
    {map, _} =
      key
      |> String.graphemes()
      |> Enum.reduce({%{}, ?a}, fn ch, {m, next_code} ->
        if ch == " " or Map.has_key?(m, ch) do
          {m, next_code}
        else
          {Map.put(m, ch, <<next_code>>), next_code + 1}
        end
      end)

    message
    |> String.graphemes()
    |> Enum.map(fn ch -> if ch == " ", do: " ", else Map.get(map, ch) end)
    |> Enum.join()
  end
end
```
