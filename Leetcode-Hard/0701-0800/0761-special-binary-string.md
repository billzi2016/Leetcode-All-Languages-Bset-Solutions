# 0761. Special Binary String

## Cpp

```cpp
class Solution {
public:
    string makeLargestSpecial(string s) {
        vector<string> parts;
        int count = 0, start = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            count += (s[i] == '1' ? 1 : -1);
            if (count == 0) {
                // s[start..i] is a special substring
                string inner = s.substr(start + 1, i - start - 1);
                string processed = makeLargestSpecial(inner);
                parts.push_back("1" + processed + "0");
                start = i + 1;
            }
        }
        sort(parts.begin(), parts.end(), greater<string>());
        string res;
        for (auto &p : parts) res += p;
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String makeLargestSpecial(String s) {
        List<String> parts = new ArrayList<>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') balance++;
            else balance--;
            if (balance == 0) {
                String inner = s.substring(start + 1, i);
                parts.add("1" + makeLargestSpecial(inner) + "0");
                start = i + 1;
            }
        }
        Collections.sort(parts, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (String part : parts) sb.append(part);
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        parts = []
        balance = 0
        last = 0
        for i, ch in enumerate(s):
            balance += 1 if ch == '1' else -1
            if balance == 0:
                # s[last:i+1] is a special substring
                inner = s[last + 1:i]
                parts.append('1' + self.makeLargestSpecial(inner) + '0')
                last = i + 1
        parts.sort(reverse=True)
        return ''.join(parts)
```

## Python3

```python
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        bal = 0
        last = 0
        for i, ch in enumerate(s):
            bal += 1 if ch == '1' else -1
            if bal == 0:
                inner = s[last + 1:i]
                parts.append('1' + self.makeLargestSpecial(inner) + '0')
                last = i + 1
        parts.sort(reverse=True)
        return ''.join(parts)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_desc(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sb, sa);  // descending order
}

char* makeLargestSpecial(char* s) {
    if (!s || *s == '\0') {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int n = strlen(s);
    char *parts[55];
    int cnt = 0, bal = 0, start = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '1') bal++;
        else bal--;
        if (bal == 0) {
            int inner_len = i - start - 1;
            char *inner = (char *)malloc(inner_len + 2);
            memcpy(inner, s + start + 1, inner_len);
            inner[inner_len] = '\0';
            char *processed_inner = makeLargestSpecial(inner);
            free(inner);

            int pi_len = strlen(processed_inner);
            char *part = (char *)malloc(pi_len + 3);
            part[0] = '1';
            memcpy(part + 1, processed_inner, pi_len);
            part[pi_len + 1] = '0';
            part[pi_len + 2] = '\0';
            free(processed_inner);

            parts[cnt++] = part;
            start = i + 1;
        }
    }

    qsort(parts, cnt, sizeof(char *), cmp_desc);

    int total_len = 0;
    for (int i = 0; i < cnt; ++i) total_len += strlen(parts[i]);

    char *res = (char *)malloc(total_len + 1);
    int pos = 0;
    for (int i = 0; i < cnt; ++i) {
        int l = strlen(parts[i]);
        memcpy(res + pos, parts[i], l);
        pos += l;
        free(parts[i]);
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public string MakeLargestSpecial(string s) {
        List<string> parts = new List<string>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.Length; i++) {
            balance += s[i] == '1' ? 1 : -1;
            if (balance == 0) {
                // substring from start to i inclusive is a special string
                string inner = s.Substring(start + 1, i - start - 1);
                string processedInner = MakeLargestSpecial(inner);
                parts.Add("1" + processedInner + "0");
                start = i + 1;
            }
        }
        parts.Sort((a, b) => b.CompareTo(a)); // descending lexicographic
        return string.Concat(parts);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeLargestSpecial = function(s) {
    const parts = [];
    let count = 0, start = 0;
    for (let i = 0; i < s.length; i++) {
        count += s[i] === '1' ? 1 : -1;
        if (count === 0) {
            // substring from start to i inclusive is special
            const inner = s.substring(start + 1, i);
            parts.push('1' + makeLargestSpecial(inner) + '0');
            start = i + 1;
        }
    }
    parts.sort((a, b) => b.localeCompare(a));
    return parts.join('');
};
```

## Typescript

```typescript
function makeLargestSpecial(s: string): string {
    const parts: string[] = [];
    let balance = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') balance++;
        else balance--;
        if (balance === 0) {
            const inner = s.substring(start + 1, i);
            parts.push('1' + makeLargestSpecial(inner) + '0');
            start = i + 1;
        }
    }
    parts.sort((a, b) => b.localeCompare(a));
    return parts.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeLargestSpecial($s) {
        $n = strlen($s);
        if ($n == 0) return "";
        $balance = 0;
        $start = 0;
        $parts = [];
        for ($i = 0; $i < $n; $i++) {
            $balance += ($s[$i] === '1') ? 1 : -1;
            if ($balance == 0) {
                // substring from $start to $i inclusive is a special string
                $inner = substr($s, $start + 1, $i - $start - 1);
                $processedInner = $this->makeLargestSpecial($inner);
                $parts[] = '1' . $processedInner . '0';
                $start = $i + 1;
            }
        }
        rsort($parts, SORT_STRING);
        return implode('', $parts);
    }
}
```

## Swift

```swift
class Solution {
    func makeLargestSpecial(_ s: String) -> String {
        let chars = Array(s)
        var count = 0
        var i = 0
        var parts = [String]()
        for j in 0..<chars.count {
            if chars[j] == "1" {
                count += 1
            } else {
                count -= 1
            }
            if count == 0 {
                let inner = String(chars[(i + 1)..<j])
                let processedInner = makeLargestSpecial(inner)
                parts.append("1" + processedInner + "0")
                i = j + 1
            }
        }
        parts.sort(by: >)
        return parts.joined()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeLargestSpecial(s: String): String {
        if (s.length <= 2) return s
        val parts = mutableListOf<String>()
        var count = 0
        var start = 0
        for (i in s.indices) {
            if (s[i] == '1') count++ else count--
            if (count == 0) {
                val inner = makeLargestSpecial(s.substring(start + 1, i))
                parts.add("1$inner0")
                start = i + 1
            }
        }
        parts.sortDescending()
        return parts.joinToString("")
    }
}
```

## Dart

```dart
class Solution {
  String makeLargestSpecial(String s) {
    if (s.length <= 2) return s;
    List<String> parts = [];
    int count = 0;
    int start = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        count++;
      } else {
        count--;
      }
      if (count == 0) {
        String inner = makeLargestSpecial(s.substring(start + 1, i));
        parts.add('1' + inner + '0');
        start = i + 1;
      }
    }
    parts.sort((a, b) => b.compareTo(a));
    return parts.join();
  }
}
```

## Golang

```go
import "sort"

func makeLargestSpecial(s string) string {
	if len(s) <= 2 {
		return s
	}
	var parts []string
	count, start := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			count++
		} else {
			count--
		}
		if count == 0 {
			inner := makeLargestSpecial(s[start+1 : i])
			part := "1" + inner + "0"
			parts = append(parts, part)
			start = i + 1
		}
	}
	sort.Slice(parts, func(i, j int) bool {
		return parts[i] > parts[j]
	})
	res := ""
	for _, p := range parts {
		res += p
	}
	return res
}
```

## Ruby

```ruby
def make_largest_special(s)
  return "" if s.empty?
  parts = []
  balance = 0
  start = 0
  s.each_char.with_index do |ch, i|
    balance += (ch == '1' ? 1 : -1)
    if balance == 0
      inner = s[(start + 1)...i]
      parts << "1" + make_largest_special(inner) + "0"
      start = i + 1
    end
  end
  parts.sort! { |a, b| b <=> a }
  parts.join
end
```

## Scala

```scala
object Solution {
    def makeLargestSpecial(s: String): String = {
        val parts = scala.collection.mutable.ListBuffer[String]()
        var balance = 0
        var start = 0
        for (i <- s.indices) {
            if (s(i) == '1') balance += 1 else balance -= 1
            if (balance == 0) {
                val inner = s.substring(start + 1, i)
                val processedInner = makeLargestSpecial(inner)
                parts += ("1" + processedInner + "0")
                start = i + 1
            }
        }
        parts.sortWith(_ > _).mkString("")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_largest_special(s: String) -> String {
        fn helper(sub: &str) -> String {
            let mut parts: Vec<String> = Vec::new();
            let mut count = 0i32;
            let mut start = 0usize;
            let bytes = sub.as_bytes();
            for (i, &b) in bytes.iter().enumerate() {
                if b == b'1' {
                    count += 1;
                } else {
                    count -= 1;
                }
                if count == 0 {
                    // inner part without the outermost '1' and '0'
                    let inner = &sub[start + 1..i];
                    let processed_inner = helper(inner);
                    let part = format!("1{}0", processed_inner);
                    parts.push(part);
                    start = i + 1;
                }
            }
            parts.sort_by(|a, b| b.cmp(a)); // descending lexicographic
            parts.concat()
        }

        helper(&s)
    }
}
```

## Racket

```racket
(define/contract (make-largest-special s)
  (-> string? string?)
  (letrec ((process
            (lambda (str)
              (if (= (string-length str) 0)
                  ""
                  (let loop ((i 0) (bal 0) (start 0) (parts '()))
                    (if (= i (string-length str))
                        (apply string-append (sort parts string>?))
                        (let* ((ch (string-ref str i))
                               (new-bal (if (char=? ch #\1) (+ bal 1) (- bal 1))))
                          (if (= new_bal 0)
                              (let* ((inner (substring str (+ start 1) i))
                                     (inner-processed (process inner))
                                     (piece (string-append "1" inner-processed "0")))
                                (loop (+ i 1) 0 (+ i 1) (cons piece parts)))
                              (loop (+ i 1) new_bal start parts)))))))))
    (process s)))
```

## Erlang

```erlang
-module(solution).
-export([make_largest_special/1]).

-spec make_largest_special(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_largest_special(S) ->
    Str = binary_to_list(S),
    ResultList = largest(Str),
    list_to_binary(ResultList).

largest([]) -> [];
largest(Str) ->
    Components = split_components(Str, [], [], 0),
    Processed = [wrap(Comp) || Comp <- Components],
    Sorted = lists:reverse(lists:sort(Processed)),
    lists:flatten(Sorted).

split_components([], _Curr, Acc, _Bal) ->
    lists:reverse(Acc);
split_components([C|Rest], Curr, Acc, Bal) ->
    NewBal = case C of
                $1 -> Bal + 1;
                $0 -> Bal - 1
            end,
    NewCurr = [C|Curr],
    if NewBal == 0 ->
        ComponentRev = lists:reverse(NewCurr),
        split_components(Rest, [], [ComponentRev | Acc], 0);
       true ->
        split_components(Rest, NewCurr, Acc, NewBal)
    end.

wrap(Component) ->
    Len = length(Component),
    Inner = case Len > 2 of
                true -> lists:sublist(Component, 2, Len - 2);
                false -> []
            end,
    ProcessedInner = largest(Inner),
    [$1] ++ ProcessedInner ++ [$0].
```

## Elixir

```elixir
defmodule Solution do
  @spec make_largest_special(s :: String.t) :: String.t
  def make_largest_special(s) do
    do_make(s)
  end

  defp do_make(s) when byte_size(s) <= 2, do: s

  defp do_make(s) do
    chars = String.graphemes(s)

    {pieces, _} =
      Enum.with_index(chars)
      |> Enum.reduce({[], {0, 0}}, fn {ch, idx}, {list, {balance, start}} ->
        new_balance = if ch == "1", do: balance + 1, else: balance - 1

        if new_balance == 0 do
          inner =
            chars
            |> Enum.slice(start + 1, idx - start - 1)
            |> Enum.join()

          piece = "1" <> do_make(inner) <> "0"
          {[piece | list], {new_balance, idx + 1}}
        else
          {list, {new_balance, start}}
        end
      end)

    pieces
    |> Enum.sort(&>=/2)
    |> Enum.join()
  end
end
```
