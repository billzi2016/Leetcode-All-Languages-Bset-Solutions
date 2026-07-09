# 0151. Reverse Words in a String

## Cpp

```cpp
class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        string trimmed;
        trimmed.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (s[i] != ' ') {
                trimmed.push_back(s[i]);
            } else if (!trimmed.empty() && trimmed.back() != ' ') {
                trimmed.push_back(' ');
            }
        }
        if (!trimmed.empty() && trimmed.back() == ' ')
            trimmed.pop_back();

        reverse(trimmed.begin(), trimmed.end());

        int len = trimmed.size();
        for (int i = 0; i < len;) {
            int j = i;
            while (j < len && trimmed[j] != ' ') ++j;
            reverse(trimmed.begin() + i, trimmed.begin() + j);
            i = j + 1;
        }
        return trimmed;
    }
};
```

## Java

```java
class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        // Reverse the whole string
        reverse(arr, 0, n - 1);
        // Reverse each word in place
        int i = 0;
        while (i < n) {
            while (i < n && arr[i] == ' ') i++;
            if (i >= n) break;
            int j = i;
            while (j < n && arr[j] != ' ') j++;
            reverse(arr, i, j - 1);
            i = j;
        }
        // Build the final string with single spaces
        StringBuilder sb = new StringBuilder();
        i = 0;
        while (i < n) {
            while (i < n && arr[i] == ' ') i++;
            if (i >= n) break;
            if (sb.length() > 0) sb.append(' ');
            while (i < n && arr[i] != ' ') {
                sb.append(arr[i]);
                i++;
            }
        }
        return sb.toString();
    }

    private void reverse(char[] a, int left, int right) {
        while (left < right) {
            char tmp = a[left];
            a[left++] = a[right];
            a[right--] = tmp;
        }
    }
}
```

## Python

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
```

## Python3

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* reverseWords(char* s) {
    int n = strlen(s);
    int *starts = (int*)malloc(sizeof(int) * (n + 1));
    int *lens   = (int*)malloc(sizeof(int) * (n + 1));
    int cnt = 0;
    int i = 0;

    while (i < n) {
        while (i < n && s[i] == ' ') i++;
        if (i >= n) break;
        int st = i;
        while (i < n && s[i] != ' ') i++;
        starts[cnt] = st;
        lens[cnt]   = i - st;
        cnt++;
    }

    int total = 0;
    for (int k = 0; k < cnt; ++k) total += lens[k];
    if (cnt > 1) total += cnt - 1; // spaces between words

    char *res = (char*)malloc(total + 1);
    int pos = 0;
    for (int k = cnt - 1; k >= 0; --k) {
        memcpy(res + pos, s + starts[k], lens[k]);
        pos += lens[k];
        if (k > 0) {
            res[pos] = ' ';
            pos++;
        }
    }
    res[pos] = '\0';

    free(starts);
    free(lens);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ReverseWords(string s) {
        var words = s.Split(' ', System.StringSplitOptions.RemoveEmptyEntries);
        System.Array.Reverse(words);
        return string.Join(" ", words);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.trim().split(/\s+/).reverse().join(' ');
};
```

## Typescript

```typescript
function reverseWords(s: string): string {
    return s.trim().split(/\s+/).reverse().join(' ');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reverseWords($s) {
        $trimmed = trim($s);
        if ($trimmed === '') {
            return '';
        }
        $words = preg_split('/\s+/', $trimmed);
        $reversed = array_reverse($words);
        return implode(' ', $reversed);
    }
}
```

## Swift

```swift
class Solution {
    func reverseWords(_ s: String) -> String {
        let words = s.split(separator: " ")
        return words.reversed().joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reverseWords(s: String): String {
        val words = s.trim().split(Regex("\\s+"))
        return words.asReversed().joinToString(" ")
    }
}
```

## Dart

```dart
class Solution {
  String reverseWords(String s) {
    var words = s.trim().split(RegExp(r'\s+'));
    return words.reversed.join(' ');
  }
}
```

## Golang

```go
import "strings"

func reverseWords(s string) string {
    n := len(s)
    words := make([]string, 0)
    i := 0
    for i < n {
        // skip spaces
        for i < n && s[i] == ' ' {
            i++
        }
        if i >= n {
            break
        }
        start := i
        for i < n && s[i] != ' ' {
            i++
        }
        words = append(words, s[start:i])
    }

    var sb strings.Builder
    for j := len(words) - 1; j >= 0; j-- {
        sb.WriteString(words[j])
        if j > 0 {
            sb.WriteByte(' ')
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
# @param {String} s
# @return {String}
def reverse_words(s)
  s.split.reverse.join(' ')
end
```

## Scala

```scala
object Solution {
    def reverseWords(s: String): String = {
        s.trim.split("\\s+").reverse.mkString(" ")
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn reverse_words(s: String) -> String {
        s.split_whitespace().rev().collect::<Vec<&str>>().join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (reverse-words s)
  (-> string? string?)
  (let* ([trimmed (string-trim s)]
         [words (regexp-split #px"\\s+" trimmed)])
    (string-join (reverse words) " ")))
```

## Erlang

```erlang
-spec reverse_words(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_words(S) ->
    Words = re:split(S, <<"\\s+">>, [{return, binary}, trim]),
    RevWords = lists:reverse(Words),
    string:join(RevWords, <<" ">>).
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_words(s :: String.t) :: String.t
  def reverse_words(s) do
    s
    |> String.split(~r/\s+/, trim: true)
    |> Enum.reverse()
    |> Enum.join(" ")
  end
end
```
