# 1807. Evaluate the Bracket Pairs of a String

## Cpp

```cpp
class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> mp;
        mp.reserve(knowledge.size() * 2);
        for (const auto& kv : knowledge) {
            mp[kv[0]] = kv[1];
        }
        string res;
        res.reserve(s.size());
        int n = s.size();
        for (int i = 0; i < n; ) {
            if (s[i] == '(') {
                int j = i + 1;
                while (j < n && s[j] != ')') ++j;
                string key = s.substr(i + 1, j - i - 1);
                auto it = mp.find(key);
                if (it != mp.end()) res += it->second;
                else res.push_back('?');
                i = j + 1; // skip past ')'
            } else {
                res.push_back(s[i]);
                ++i;
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        Map<String, String> map = new HashMap<>();
        for (List<String> pair : knowledge) {
            map.put(pair.get(0), pair.get(1));
        }
        StringBuilder sb = new StringBuilder();
        int i = 0;
        int n = s.length();
        while (i < n) {
            char c = s.charAt(i);
            if (c == '(') {
                int j = i + 1;
                while (j < n && s.charAt(j) != ')') {
                    j++;
                }
                String key = s.substring(i + 1, j);
                sb.append(map.getOrDefault(key, "?"));
                i = j + 1; // move past ')'
            } else {
                sb.append(c);
                i++;
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        lookup = {k: v for k, v in knowledge}
        res = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i+1:j]
                res.append(lookup.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
```

## Python3

```python
from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kv = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i+1:j]
                res.append(kv.get(key, '?'))
                i = j + 1
            else:
                res.append(s[i])
                i += 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    const char *key;
    const char *value;
    int used;
} Entry;

static unsigned int hash_func(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)*s;
        s++;
    }
    return (unsigned int)h;
}

static Entry* create_table(int knowledgeSize) {
    int sz = 2;
    while (sz < knowledgeSize * 2) sz <<= 1;
    Entry *tbl = (Entry *)calloc(sz, sizeof(Entry));
    return tbl;
}

static void table_insert(Entry *tbl, int size, const char *key, const char *value) {
    unsigned int idx = hash_func(key) & (size - 1);
    while (tbl[idx].used) {
        if (strcmp(tbl[idx].key, key) == 0) {
            tbl[idx].value = value;
            return;
        }
        idx = (idx + 1) & (size - 1);
    }
    tbl[idx].used = 1;
    tbl[idx].key = key;
    tbl[idx].value = value;
}

static const char* table_get(Entry *tbl, int size, const char *key) {
    unsigned int idx = hash_func(key) & (size - 1);
    while (tbl[idx].used) {
        if (strcmp(tbl[idx].key, key) == 0) {
            return tbl[idx].value;
        }
        idx = (idx + 1) & (size - 1);
    }
    return NULL;
}

char* evaluate(char* s, char*** knowledge, int knowledgeSize, int* knowledgeColSize) {
    /* build hashmap */
    Entry *table = create_table(knowledgeSize);
    int tblSize = 0;
    while ((tblSize <<= 1) < knowledgeSize * 2) {} // find actual size used in create_table
    if (tblSize == 0) tblSize = 2; // fallback
    
    for (int i = 0; i < knowledgeSize; ++i) {
        const char *key = knowledge[i][0];
        const char *val = knowledge[i][1];
        table_insert(table, tblSize, key, val);
    }
    
    int n = strlen(s);
    int bufSize = n * 4 + 1;
    char *res = (char *)malloc(bufSize);
    int pos = 0;
    
    for (int i = 0; i < n;) {
        if (s[i] != '(') {
            res[pos++] = s[i++];
        } else {
            int j = i + 1;
            while (j < n && s[j] != ')') ++j;
            int keyLen = j - (i + 1);
            char keyBuf[12];
            if (keyLen >= 12) keyLen = 11; // safety, though constraints guarantee <=10
            memcpy(keyBuf, s + i + 1, keyLen);
            keyBuf[keyLen] = '\0';
            
            const char *val = table_get(table, tblSize, keyBuf);
            if (val) {
                int vlen = strlen(val);
                memcpy(res + pos, val, vlen);
                pos += vlen;
            } else {
                res[pos++] = '?';
            }
            i = j + 1; // skip ')'
        }
    }
    res[pos] = '\0';
    
    free(table);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        var dict = new Dictionary<string, string>();
        foreach (var pair in knowledge) {
            if (pair.Count == 2)
                dict[pair[0]] = pair[1];
        }

        var result = new StringBuilder();
        var keyBuilder = new StringBuilder();
        bool inside = false;

        foreach (char ch in s) {
            if (ch == '(') {
                inside = true;
                keyBuilder.Clear();
            } else if (ch == ')') {
                string key = keyBuilder.ToString();
                if (dict.TryGetValue(key, out var val))
                    result.Append(val);
                else
                    result.Append('?');
                inside = false;
            } else {
                if (inside)
                    keyBuilder.Append(ch);
                else
                    result.Append(ch);
            }
        }

        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[][]} knowledge
 * @return {string}
 */
var evaluate = function(s, knowledge) {
    const map = new Map();
    for (const [k, v] of knowledge) {
        map.set(k, v);
    }
    const res = [];
    let i = 0;
    const n = s.length;
    while (i < n) {
        if (s[i] === '(') {
            const j = s.indexOf(')', i);
            const key = s.slice(i + 1, j);
            res.push(map.has(key) ? map.get(key) : '?');
            i = j + 1;
        } else {
            res.push(s[i]);
            i++;
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function evaluate(s: string, knowledge: string[][]): string {
    const dict = new Map<string, string>();
    for (const [k, v] of knowledge) {
        dict.set(k, v);
    }
    const result: string[] = [];
    let i = 0;
    const n = s.length;
    while (i < n) {
        if (s[i] === '(') {
            let j = i + 1;
            while (j < n && s[j] !== ')') j++;
            const key = s.substring(i + 1, j);
            const val = dict.get(key);
            result.push(val !== undefined ? val : '?');
            i = j + 1; // move past ')'
        } else {
            result.push(s[i]);
            i++;
        }
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[][] $knowledge
     * @return String
     */
    function evaluate($s, $knowledge) {
        $dict = [];
        foreach ($knowledge as $pair) {
            $dict[$pair[0]] = $pair[1];
        }

        $n = strlen($s);
        $result = '';
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                $j = $i + 1;
                $key = '';
                while ($j < $n && $s[$j] !== ')') {
                    $key .= $s[$j];
                    $j++;
                }
                // $j now points to ')'
                if (array_key_exists($key, $dict)) {
                    $result .= $dict[$key];
                } else {
                    $result .= '?';
                }
                $i = $j; // skip past ')'
            } else {
                $result .= $s[$i];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        var dict = [String: String]()
        for pair in knowledge {
            if pair.count == 2 {
                dict[pair[0]] = pair[1]
            }
        }
        
        var result = ""
        var i = s.startIndex
        while i < s.endIndex {
            if s[i] == "(" {
                var j = s.index(after: i)
                while j < s.endIndex && s[j] != ")" {
                    j = s.index(after: j)
                }
                // Extract key between '(' and ')'
                let keyStart = s.index(after: i)
                let key = String(s[keyStart..<j])
                if let val = dict[key] {
                    result.append(val)
                } else {
                    result.append("?")
                }
                // Move past ')'
                i = s.index(after: j)
            } else {
                result.append(s[i])
                i = s.index(after: i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun evaluate(s: String, knowledge: List<List<String>>): String {
        val map = HashMap<String, String>()
        for (pair in knowledge) {
            map[pair[0]] = pair[1]
        }
        val sb = StringBuilder()
        var i = 0
        while (i < s.length) {
            if (s[i] == '(') {
                var j = i + 1
                while (j < s.length && s[j] != ')') {
                    j++
                }
                val key = s.substring(i + 1, j)
                sb.append(map.getOrDefault(key, "?"))
                i = j + 1
            } else {
                sb.append(s[i])
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
  String evaluate(String s, List<List<String>> knowledge) {
    final Map<String, String> dict = {};
    for (var pair in knowledge) {
      dict[pair[0]] = pair[1];
    }

    final StringBuffer sb = StringBuffer();
    int i = 0;
    while (i < s.length) {
      if (s[i] == '(') {
        int j = i + 1;
        while (j < s.length && s[j] != ')') {
          j++;
        }
        // Extract key between parentheses
        final String key = s.substring(i + 1, j);
        sb.write(dict.containsKey(key) ? dict[key]! : '?');
        i = j + 1; // Move past ')'
      } else {
        sb.write(s[i]);
        i++;
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
func evaluate(s string, knowledge [][]string) string {
	dict := make(map[string]string, len(knowledge))
	for _, kv := range knowledge {
		if len(kv) == 2 {
			dict[kv[0]] = kv[1]
		}
	}
	var sb strings.Builder
	n := len(s)
	for i := 0; i < n; {
		if s[i] == '(' {
			j := i + 1
			for j < n && s[j] != ')' {
				j++
			}
			key := s[i+1 : j]
			if val, ok := dict[key]; ok {
				sb.WriteString(val)
			} else {
				sb.WriteByte('?')
			}
			i = j + 1
		} else {
			sb.WriteByte(s[i])
			i++
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def evaluate(s, knowledge)
  dict = {}
  knowledge.each { |k, v| dict[k] = v }
  result = +""
  i = 0
  n = s.length
  while i < n
    if s[i] == '('
      j = i + 1
      j += 1 while s[j] != ')'
      key = s[(i + 1)...j]
      result << (dict[key] || '?')
      i = j + 1
    else
      result << s[i]
      i += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def evaluate(s: String, knowledge: List[List[String]]): String = {
        val dict = scala.collection.mutable.HashMap[String, String]()
        for (pair <- knowledge) {
            dict(pair(0)) = pair(1)
        }
        val sb = new StringBuilder
        var i = 0
        val n = s.length
        while (i < n) {
            if (s.charAt(i) == '(') {
                var j = i + 1
                while (j < n && s.charAt(j) != ')') {
                    j += 1
                }
                // substring between parentheses
                val key = s.substring(i + 1, j)
                sb.append(dict.getOrElse(key, "?"))
                i = j + 1 // move past ')'
            } else {
                sb.append(s.charAt(i))
                i += 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        let mut map: HashMap<&str, &str> = HashMap::with_capacity(knowledge.len());
        // Store references to strings inside the vectors to avoid extra cloning
        // Since we need &'static lifetime for hashmap keys/values, we'll clone into owned Strings later.
        // Simpler approach: store owned Strings.
        let mut map_owned: HashMap<String, String> = HashMap::with_capacity(knowledge.len());
        for pair in knowledge {
            if pair.len() == 2 {
                map_owned.insert(pair[0].clone(), pair[1].clone());
            }
        }

        let bytes = s.as_bytes();
        let mut res = String::new();
        let mut i = 0;
        while i < bytes.len() {
            if bytes[i] == b'(' {
                i += 1; // skip '('
                let start = i;
                while i < bytes.len() && bytes[i] != b')' {
                    i += 1;
                }
                // extract key between '(' and ')'
                let key = std::str::from_utf8(&bytes[start..i]).unwrap();
                if let Some(val) = map_owned.get(key) {
                    res.push_str(val);
                } else {
                    res.push('?');
                }
                i += 1; // skip ')'
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
(define/contract (evaluate s knowledge)
  (-> string? (listof (listof string?)) string?)
  (let* ([ht (make-hash)])
    (for-each (lambda (pair) (hash-set! ht (first pair) (second pair))) knowledge)
    (let ([out (open-output-string)]
          [len (string-length s)])
      (let loop ((i 0))
        (when (< i len)
          (let ((ch (string-ref s i)))
            (if (char=? ch #\()
                (let find-close ((j (+ i 1)))
                  (if (char=? (string-ref s j) #\))
                      (let* ([key (substring s (+ i 1) j)]
                             [val (if (hash-has-key? ht key)
                                      (hash-ref ht key)
                                      "?")])
                        (write-string out val)
                        (loop (+ j 1)))
                      (find-close (+ j 1))))
                (begin
                  (write-char out ch)
                  (loop (+ i 1)))))))
      (get-output-string out))))
```

## Erlang

```erlang
-module(solution).
-export([evaluate/2]).

-spec evaluate(S :: unicode:unicode_binary(), Knowledge :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
evaluate(S, Knowledge) ->
    Map = maps:from_list([{K, V} || [K, V] <- Knowledge]),
    process(S, Map, []).

process(<<>>, _Map, Acc) ->
    iolist_to_binary(lists:reverse(Acc));
process(<<$(, Rest/binary>>, Map, Acc) ->
    {KeyBin, After} = take_until_close(Rest),
    Value = case maps:get(KeyBin, Map, undefined) of
                undefined -> <<"?">>;
                V -> V
            end,
    process(After, Map, [Value | Acc]);
process(<<Char, Rest/binary>>, Map, Acc) ->
    process(Rest, Map, [<<Char>> | Acc]).

take_until_close(Bin) ->
    take_until_close(Bin, []).

take_until_close(<<$), Rest/binary>>, Acc) ->
    {list_to_binary(lists:reverse(Acc)), Rest};
take_until_close(<<Char, Rest/binary>>, Acc) ->
    take_until_close(Rest, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec evaluate(s :: String.t(), knowledge :: [[String.t()]]) :: String.t()
  def evaluate(s, knowledge) do
    map = Map.new(knowledge, fn [k, v] -> {k, v} end)
    eval_string(s, map, [])
  end

  defp eval_string(<<>>, _map, acc) do
    :erlang.iolist_to_binary(Enum.reverse(acc))
  end

  # opening bracket
  defp eval_string(<<"(", rest::binary>>, map, acc) do
    {key, after} = extract_key(rest, <<>>)
    value = Map.get(map, key, "?")
    eval_string(after, map, [value | acc])
  end

  # regular character
  defp eval_string(<<c, rest::binary>>, map, acc) do
    eval_string(rest, map, [<<c>> | acc])
  end

  defp extract_key(<<")", rest::binary>>, key), do: {key, rest}
  defp extract_key(<<c, rest::binary>>, key), do: extract_key(rest, <<key::binary, c>>)
end
```
