# 1662. Check If Two String Arrays are Equivalent

## Cpp

```cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1, s2;
        for (const auto& w : word1) s1 += w;
        for (const auto& w : word2) s2 += w;
        return s1 == s2;
    }
};
```

## Java

```java
class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder sb1 = new StringBuilder();
        for (String s : word1) {
            sb1.append(s);
        }
        StringBuilder sb2 = new StringBuilder();
        for (String s : word2) {
            sb2.append(s);
        }
        return sb1.toString().equals(sb2.toString());
    }
}
```

## Python

```python
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return "".join(word1) == "".join(word2)
```

## Python3

```python
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool arrayStringsAreEqual(char** word1, int word1Size, char** word2, int word2Size) {
    int len1 = 0;
    for (int i = 0; i < word1Size; ++i) {
        len1 += strlen(word1[i]);
    }
    int len2 = 0;
    for (int i = 0; i < word2Size; ++i) {
        len2 += strlen(word2[i]);
    }

    char *s1 = (char *)malloc(len1 + 1);
    char *s2 = (char *)malloc(len2 + 1);
    if (!s1 || !s2) {
        free(s1);
        free(s2);
        return false;
    }

    char *p = s1;
    for (int i = 0; i < word1Size; ++i) {
        size_t l = strlen(word1[i]);
        memcpy(p, word1[i], l);
        p += l;
    }
    *p = '\0';

    p = s2;
    for (int i = 0; i < word2Size; ++i) {
        size_t l = strlen(word2[i]);
        memcpy(p, word2[i], l);
        p += l;
    }
    *p = '\0';

    bool result = strcmp(s1, s2) == 0;

    free(s1);
    free(s2);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public bool ArrayStringsAreEqual(string[] word1, string[] word2) {
        var sb1 = new System.Text.StringBuilder();
        foreach (var s in word1) sb1.Append(s);
        var sb2 = new System.Text.StringBuilder();
        foreach (var s in word2) sb2.Append(s);
        return sb1.ToString() == sb2.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    return word1.join('') === word2.join('');
};
```

## Typescript

```typescript
function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    return word1.join('') === word2.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $word1
     * @param String[] $word2
     * @return Boolean
     */
    function arrayStringsAreEqual($word1, $word2) {
        $s1 = implode('', $word1);
        $s2 = implode('', $word2);
        return $s1 === $s2;
    }
}
```

## Swift

```swift
class Solution {
    func arrayStringsAreEqual(_ word1: [String], _ word2: [String]) -> Bool {
        return word1.joined() == word2.joined()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun arrayStringsAreEqual(word1: Array<String>, word2: Array<String>): Boolean {
        val sb1 = StringBuilder()
        for (s in word1) sb1.append(s)
        val sb2 = StringBuilder()
        for (s in word2) sb2.append(s)
        return sb1.toString() == sb2.toString()
    }
}
```

## Dart

```dart
class Solution {
  bool arrayStringsAreEqual(List<String> word1, List<String> word2) {
    return word1.join() == word2.join();
  }
}
```

## Golang

```go
package main

import "strings"

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	var sb1 strings.Builder
	for _, s := range word1 {
		sb1.WriteString(s)
	}
	var sb2 strings.Builder
	for _, s := range word2 {
		sb2.WriteString(s)
	}
	return sb1.String() == sb2.String()
}
```

## Ruby

```ruby
# @param {String[]} word1
# @param {String[]} word2
# @return {Boolean}
def array_strings_are_equal(word1, word2)
  word1.join == word2.join
end
```

## Scala

```scala
object Solution {
  def arrayStringsAreEqual(word1: Array[String], word2: Array[String]): Boolean = {
    val sb1 = new StringBuilder
    for (w <- word1) sb1.append(w)
    val sb2 = new StringBuilder
    for (w <- word2) sb2.append(w)
    sb1.toString == sb2.toString
  }
}
```

## Rust

```rust
impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        let mut s1 = String::new();
        for w in &word1 {
            s1.push_str(w);
        }
        let mut s2 = String::new();
        for w in &word2 {
            s2.push_str(w);
        }
        s1 == s2
    }
}
```

## Racket

```racket
#lang racket

(require rackunit)

(provide array-strings-are-equal)

(define/contract (array-strings-are-equal word1 word2)
  (-> (listof string?) (listof string?) boolean?)
  (let ([concat
         (lambda (lst)
           (if (null? lst) ""
               (apply string-append lst)))])
    (string=? (concat word1) (concat word2))))
```

## Erlang

```erlang
-spec array_strings_are_equal(Word1 :: [unicode:unicode_binary()], Word2 :: [unicode:unicode_binary()]) -> boolean().
array_strings_are_equal(Word1, Word2) ->
    iolist_to_binary(Word1) =:= iolist_to_binary(Word2).
```

## Elixir

```elixir
defmodule Solution do
  @spec array_strings_are_equal(word1 :: [String.t()], word2 :: [String.t()]) :: boolean()
  def array_strings_are_equal(word1, word2) do
    Enum.join(word1) == Enum.join(word2)
  end
end
```
