# 1816. Truncate Sentence

## Cpp

```cpp
class Solution {
public:
    string truncateSentence(string s, int k) {
        int spaces = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] == ' ') {
                ++spaces;
                if (spaces == k) {
                    return s.substr(0, i);
                }
            }
        }
        return s;
    }
};
```

## Java

```java
class Solution {
    public String truncateSentence(String s, int k) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < k; i++) {
            if (i > 0) sb.append(' ');
            sb.append(words[i]);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ' '.join(s.split()[:k])
```

## Python3

```python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* truncateSentence(char* s, int k) {
    int len = strlen(s);
    char *res = (char *)malloc(len + 1);
    if (!res) return NULL;
    
    int wordCount = 0;
    int i = 0;
    for (; i < len; ++i) {
        if (s[i] == ' ') {
            ++wordCount;
            if (wordCount == k) break;
        }
        res[i] = s[i];
    }
    res[i] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string TruncateSentence(string s, int k)
    {
        int spaceCount = 0;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == ' ')
            {
                spaceCount++;
                if (spaceCount == k)
                {
                    return s.Substring(0, i);
                }
            }
        }
        return s;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    return s.split(' ').slice(0, k).join(' ');
};
```

## Typescript

```typescript
function truncateSentence(s: string, k: number): string {
    return s.split(' ').slice(0, k).join(' ');
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function truncateSentence($s, $k) {
        $words = explode(' ', $s);
        return implode(' ', array_slice($words, 0, $k));
    }
}
```

## Swift

```swift
class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        let words = s.split(separator: " ")
        return words.prefix(k).joined(separator: " ")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun truncateSentence(s: String, k: Int): String {
        return s.split(' ').take(k).joinToString(" ")
    }
}
```

## Dart

```dart
class Solution {
  String truncateSentence(String s, int k) {
    return s.split(' ').sublist(0, k).join(' ');
  }
}
```

## Golang

```go
package main

import "strings"

func truncateSentence(s string, k int) string {
	parts := strings.SplitN(s, " ", k)
	return strings.Join(parts, " ")
}
```

## Ruby

```ruby
def truncate_sentence(s, k)
  s.split(' ')[0, k].join(' ')
end
```

## Scala

```scala
object Solution {
    def truncateSentence(s: String, k: Int): String = {
        s.split(" ").take(k).mkString(" ")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        s.split(' ').take(k as usize).collect::<Vec<&str>>().join(" ")
    }
}
```

## Racket

```racket
(require racket/string)
(require racket/list)

(define/contract (truncate-sentence s k)
  (-> string? exact-integer? string?)
  (string-join (take (string-split s " ") k) " "))
```

## Erlang

```erlang
-module(solution).
-export([truncate_sentence/2]).

-spec truncate_sentence(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
truncate_sentence(S, K) ->
    Words = binary:split(S, <<" ">>, [global]),
    FirstK = lists:sublist(Words, K),
    binary:join(FirstK, <<" ">>).
```

## Elixir

```elixir
defmodule Solution do
  @spec truncate_sentence(s :: String.t(), k :: integer()) :: String.t()
  def truncate_sentence(s, k) do
    s
    |> String.split(" ")
    |> Enum.take(k)
    |> Enum.join(" ")
  end
end
```
