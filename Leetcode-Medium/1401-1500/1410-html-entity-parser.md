# 1410. HTML Entity Parser

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string entityParser(string text) {
        unordered_map<string, string> mp = {
            {"&quot;", "\""},
            {"&apos;", "'"},
            {"&amp;", "&"},
            {"&gt;", ">"},
            {"&lt;", "<"},
            {"&frasl;", "/"}
        };
        const size_t maxLen = 7; // longest entity length
        string res;
        int n = text.size();
        for (int i = 0; i < n; ++i) {
            if (text[i] == '&') {
                size_t semi = text.find(';', i + 1);
                bool replaced = false;
                if (semi != string::npos && semi - i + 1 <= maxLen) {
                    string token = text.substr(i, semi - i + 1);
                    auto it = mp.find(token);
                    if (it != mp.end()) {
                        res += it->second;
                        i = static_cast<int>(semi); // skip the whole entity
                        replaced = true;
                    }
                }
                if (!replaced) {
                    res += '&';
                }
            } else {
                res += text[i];
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String entityParser(String text) {
        java.util.Map<String, Character> map = new java.util.HashMap<>();
        map.put("&quot;", '\"');
        map.put("&apos;", '\'');
        map.put("&amp;", '&');
        map.put("&gt;", '>');
        map.put("&lt;", '<');
        map.put("&frasl;", '/');

        StringBuilder sb = new StringBuilder();
        int n = text.length();
        for (int i = 0; i < n; i++) {
            char c = text.charAt(i);
            if (c == '&') {
                boolean matched = false;
                for (java.util.Map.Entry<String, Character> entry : map.entrySet()) {
                    String key = entry.getKey();
                    int len = key.length();
                    if (i + len <= n && text.startsWith(key, i)) {
                        sb.append(entry.getValue());
                        i += len - 1;
                        matched = true;
                        break;
                    }
                }
                if (!matched) {
                    sb.append(c);
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        mapping = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": '&',
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/',
        }
        max_len = max(len(k) for k in mapping)
        n = len(text)
        i = 0
        res = []
        while i < n:
            if text[i] == '&':
                # look ahead only up to the longest possible entity length
                end = text.find(';', i + 1, i + max_len + 1)
                if end != -1:
                    token = text[i:end + 1]
                    if token in mapping:
                        res.append(mapping[token])
                        i = end + 1
                        continue
            res.append(text[i])
            i += 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": '&',
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/',
        }
        n = len(text)
        i = 0
        res = []
        while i < n:
            if text[i] == '&':
                matched = False
                for ent, ch in entities.items():
                    l = len(ent)
                    if i + l <= n and text[i:i + l] == ent:
                        res.append(ch)
                        i += l
                        matched = True
                        break
                if not matched:
                    res.append('&')
                    i += 1
            else:
                res.append(text[i])
                i += 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* entityParser(char* text) {
    static const struct {
        const char *entity;
        char ch;
        int len;
    } map[] = {
        {"&quot;", '\"', 6},
        {"&apos;", '\'', 6},
        {"&amp;", '&', 5},
        {"&gt;", '>', 4},
        {"&lt;", '<', 4},
        {"&frasl;", '/', 8}
    };
    const int mapSize = sizeof(map) / sizeof(map[0]);

    size_t n = strlen(text);
    char *out = (char *)malloc(n + 1);
    if (!out) return NULL;

    size_t i = 0, j = 0;
    while (i < n) {
        if (text[i] == '&') {
            int matched = 0;
            for (int k = 0; k < mapSize; ++k) {
                if (i + map[k].len <= n && strncmp(text + i, map[k].entity, map[k].len) == 0) {
                    out[j++] = map[k].ch;
                    i += map[k].len;
                    matched = 1;
                    break;
                }
            }
            if (!matched) {
                out[j++] = text[i++];
            }
        } else {
            out[j++] = text[i++];
        }
    }
    out[j] = '\0';
    return out;
}
```

## Csharp

```csharp
public class Solution
{
    public string EntityParser(string text)
    {
        var map = new Dictionary<string, string>
        {
            { "&quot;", "\"" },
            { "&apos;", "'" },
            { "&amp;", "&" },
            { "&gt;", ">" },
            { "&lt;", "<" },
            { "&frasl;", "/" }
        };

        var sb = new System.Text.StringBuilder();
        int n = text.Length;
        for (int i = 0; i < n; i++)
        {
            if (text[i] == '&')
            {
                bool replaced = false;
                foreach (var kv in map)
                {
                    string key = kv.Key;
                    int len = key.Length;
                    if (i + len <= n && text.Substring(i, len) == key)
                    {
                        sb.Append(kv.Value);
                        i += len - 1; // advance past the entity
                        replaced = true;
                        break;
                    }
                }
                if (!replaced)
                {
                    sb.Append('&');
                }
            }
            else
            {
                sb.Append(text[i]);
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {string}
 */
var entityParser = function(text) {
    const map = {
        "&quot;": '"',
        "&apos;": "'",
        "&amp;" : '&',
        "&gt;"  : '>',
        "&lt;"  : '<',
        "&frasl;": '/'
    };
    
    let n = text.length;
    let i = 0;
    const res = [];
    
    while (i < n) {
        if (text[i] === '&') {
            // look for the next ';' after current position
            const semicolonIdx = text.indexOf(';', i + 1);
            if (semicolonIdx !== -1) {
                const entity = text.slice(i, semicolonIdx + 1);
                if (entity in map) {
                    res.push(map[entity]);
                    i = semicolonIdx + 1;
                    continue;
                } else {
                    // not a valid entity, copy as is
                    res.push(entity);
                    i = semicolonIdx + 1;
                    continue;
                }
            }
        }
        // regular character or '&' without following ';'
        res.push(text[i]);
        i++;
    }
    
    return res.join('');
};
```

## Typescript

```typescript
function entityParser(text: string): string {
    const entities: { [key: string]: string } = {
        "&quot;": "\"",
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
    };
    let result = "";
    const n = text.length;
    for (let i = 0; i < n;) {
        if (text[i] === '&') {
            let semicolonIdx = -1;
            // maximum entity length is 7 characters plus ';' => up to i+8
            const limit = Math.min(n, i + 8);
            for (let j = i + 1; j < limit; j++) {
                if (text[j] === ';') {
                    semicolonIdx = j;
                    break;
                }
            }
            if (semicolonIdx !== -1) {
                const candidate = text.substring(i, semicolonIdx + 1);
                if (candidate in entities) {
                    result += entities[candidate];
                    i = semicolonIdx + 1;
                    continue;
                }
            }
        }
        result += text[i];
        i++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return String
     */
    function entityParser($text) {
        $map = [
            '&quot;' => '"',
            '&apos;' => "'",
            '&amp;'  => '&',
            '&gt;'   => '>',
            '&lt;'   => '<',
            '&frasl;'=> '/',
        ];
        $n = strlen($text);
        $result = '';
        for ($i = 0; $i < $n;) {
            if ($text[$i] === '&') {
                $semiPos = strpos($text, ';', $i + 1);
                if ($semiPos !== false) {
                    $entity = substr($text, $i, $semiPos - $i + 1);
                    if (isset($map[$entity])) {
                        $result .= $map[$entity];
                        $i = $semiPos + 1;
                        continue;
                    }
                }
            }
            $result .= $text[$i];
            $i++;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func entityParser(_ text: String) -> String {
        let mapping: [String: String] = [
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;" : "&",
            "&gt;"  : ">",
            "&lt;"  : "<",
            "&frasl;": "/"
        ]
        var entities: [(pattern: [Character], value: String)] = []
        for (k, v) in mapping {
            entities.append((Array(k), v))
        }
        let chars = Array(text)
        var i = 0
        var result = ""
        while i < chars.count {
            if chars[i] == "&" {
                var matched = false
                for e in entities {
                    let len = e.pattern.count
                    if i + len <= chars.count {
                        var ok = true
                        var j = 0
                        while j < len {
                            if chars[i + j] != e.pattern[j] {
                                ok = false
                                break
                            }
                            j += 1
                        }
                        if ok {
                            result.append(e.value)
                            i += len
                            matched = true
                            break
                        }
                    }
                }
                if !matched {
                    result.append("&")
                    i += 1
                }
            } else {
                result.append(chars[i])
                i += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun entityParser(text: String): String {
        val sb = StringBuilder()
        var i = 0
        val n = text.length
        while (i < n) {
            if (text[i] == '&') {
                when {
                    i + 6 <= n && text.startsWith("&quot;", i) -> {
                        sb.append('\"')
                        i += 6
                    }
                    i + 6 <= n && text.startsWith("&apos;", i) -> {
                        sb.append('\'')
                        i += 6
                    }
                    i + 5 <= n && text.startsWith("&amp;", i) -> {
                        sb.append('&')
                        i += 5
                    }
                    i + 4 <= n && text.startsWith("&gt;", i) -> {
                        sb.append('>')
                        i += 4
                    }
                    i + 4 <= n && text.startsWith("&lt;", i) -> {
                        sb.append('<')
                        i += 4
                    }
                    i + 8 <= n && text.startsWith("&frasl;", i) -> {
                        sb.append('/')
                        i += 8
                    }
                    else -> {
                        sb.append('&')
                        i++
                    }
                }
            } else {
                sb.append(text[i])
                i++
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String entityParser(String text) {
    const Map<String, String> entities = {
      "&quot;": "\"",
      "&apos;": "'",
      "&amp;": "&",
      "&gt;": ">",
      "&lt;": "<",
      "&frasl;": "/"
    };
    final sb = StringBuffer();
    int i = 0;
    while (i < text.length) {
      if (text[i] == '&') {
        bool replaced = false;
        for (final entry in entities.entries) {
          final key = entry.key;
          if (i + key.length <= text.length && text.substring(i, i + key.length) == key) {
            sb.write(entry.value);
            i += key.length;
            replaced = true;
            break;
          }
        }
        if (!replaced) {
          sb.write('&');
          i++;
        }
      } else {
        sb.write(text[i]);
        i++;
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
func entityParser(text string) string {
	entities := map[string]string{
		"&quot;":  "\"",
		"&apos;":  "'",
		"&amp;":   "&",
		"&gt;":    ">",
		"&lt;":    "<",
		"&frasl;": "/",
	}
	var sb strings.Builder
	n := len(text)
	for i := 0; i < n; {
		if text[i] == '&' {
			end := -1
			limit := i + 10 // longest entity length is 8, give a small buffer
			if limit > n {
				limit = n
			}
			for j := i + 1; j < limit; j++ {
				if text[j] == ';' {
					end = j
					break
				}
			}
			if end != -1 {
				sub := text[i : end+1]
				if repl, ok := entities[sub]; ok {
					sb.WriteString(repl)
					i = end + 1
					continue
				}
			}
		}
		sb.WriteByte(text[i])
		i++
	}
	return sb.String()
}
```

## Ruby

```ruby
def entity_parser(text)
  mapping = {
    "&quot;" => '"',
    "&apos;" => "'",
    "&amp;" => '&',
    "&gt;" => '>',
    "&lt;" => '<',
    "&frasl;" => '/'
  }
  text.gsub(/&(quot|apos|amp|gt|lt|frasl);/) { |m| mapping[m] }
end
```

## Scala

```scala
object Solution {
    def entityParser(text: String): String = {
        val entities = Map(
            "&quot;" -> "\"",
            "&apos;" -> "'",
            "&amp;"  -> "&",
            "&gt;"   -> ">",
            "&lt;"   -> "<",
            "&frasl;"-> "/"
        )
        val sb = new StringBuilder
        var i = 0
        val n = text.length
        while (i < n) {
            if (text.charAt(i) == '&') {
                var j = i + 1
                var matched = false
                // maximum entity length is 8 ("&frasl;")
                while (j < n && j - i <= 8 && text.charAt(j) != ';') {
                    j += 1
                }
                if (j < n && text.charAt(j) == ';') {
                    val candidate = text.substring(i, j + 1)
                    entities.get(candidate) match {
                        case Some(repl) =>
                            sb.append(repl)
                            i = j + 1
                            matched = true
                        case None => // not a known entity
                    }
                }
                if (!matched) {
                    sb.append('&')
                    i += 1
                }
            } else {
                sb.append(text.charAt(i))
                i += 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn entity_parser(text: String) -> String {
        let bytes = text.as_bytes();
        let n = bytes.len();
        let mut res = String::with_capacity(n);
        let entities: [(&[u8], char); 6] = [
            (b"&quot;", '"'),
            (b"&apos;", '\''),
            (b"&amp;", '&'),
            (b"&gt;", '>'),
            (b"&lt;", '<'),
            (b"&frasl;", '/')
        ];
        let mut i = 0;
        while i < n {
            if bytes[i] == b'&' {
                let mut matched = false;
                for &(pat, ch) in &entities {
                    let len = pat.len();
                    if i + len <= n && &bytes[i..i+len] == pat {
                        res.push(ch);
                        i += len;
                        matched = true;
                        break;
                    }
                }
                if !matched {
                    res.push('&');
                    i += 1;
                }
            } else {
                res.push(bytes[i] as char);
                i += 1;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (entity-parser text)
  (-> string? string?)
  (let* ((entities (list (cons "&quot;" "\"")
                         (cons "&apos;" "'")
                         (cons "&amp;" "&")
                         (cons "&gt;" ">")
                         (cons "&lt;" "<")
                         (cons "&frasl;" "/")))
         (len (string-length text))
         (out (open-output-string)))
    (let loop ((i 0))
      (if (>= i len)
          (get-output-string out)
          (let ((pair
                 (for/or ([p entities])
                   (let* ((ent (car p))
                          (el (string-length ent)))
                     (and (<= (+ i el) len)
                          (string=? (substring text i (+ i el)) ent)
                          p)))))
            (if pair
                (begin
                  (display (cdr pair) out)
                  (loop (+ i (string-length (car pair)))))
                (begin
                  (write-char (string-ref text i) out)
                  (loop (+ i 1)))))))
    ))
```

## Erlang

```erlang
-module(solution).
-export([entity_parser/1]).

-spec entity_parser(Text :: unicode:unicode_binary()) -> unicode:unicode_binary().
entity_parser(Text) ->
    iolist_to_binary(parse(Text)).

parse(<<>>) ->
    [];
parse(<<"&quot;", Rest/binary>>) ->
    [<<"\"">>, parse(Rest)];
parse(<<"&apos;", Rest/binary>>) ->
    [<<"'">>, parse(Rest)];
parse(<<"&amp;", Rest/binary>>) ->
    [<<"&">>, parse(Rest)];
parse(<<"&gt;", Rest/binary>>) ->
    [<<">">>, parse(Rest)];
parse(<<"&lt;", Rest/binary>>) ->
    [<<"<">>, parse(Rest)];
parse(<<"&frasl;", Rest/binary>>) ->
    [<<"/">>, parse(Rest)];
parse(<<Char, Rest/binary>>) ->
    [<<Char>>, parse(Rest)].
```

## Elixir

```elixir
defmodule Solution do
  @spec entity_parser(text :: String.t()) :: String.t()
  def entity_parser(text) do
    entities = %{
      "&quot;" => "\"",
      "&apos;" => "'",
      "&amp;" => "&",
      "&gt;" => ">",
      "&lt;" => "<",
      "&frasl;" => "/"
    }

    Enum.reduce(entities, text, fn {entity, char}, acc ->
      String.replace(acc, entity, char)
    end)
  end
end
```
