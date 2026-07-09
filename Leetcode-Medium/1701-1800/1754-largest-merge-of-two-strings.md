# 1754. Largest Merge Of Two Strings

## Cpp

```cpp
class Solution {
public:
    string largestMerge(string word1, string word2) {
        string res;
        int i = 0, j = 0;
        int n1 = word1.size(), n2 = word2.size();
        while (i < n1 && j < n2) {
            if (word1[i] > word2[j]) {
                res.push_back(word1[i++]);
            } else if (word1[i] < word2[j]) {
                res.push_back(word2[j++]);
            } else {
                int cmp = word1.compare(i, string::npos, word2, j, string::npos);
                if (cmp > 0) {
                    res.push_back(word1[i++]);
                } else {
                    res.push_back(word2[j++]);
                }
            }
        }
        if (i < n1) res.append(word1.substr(i));
        if (j < n2) res.append(word2.substr(j));
        return res;
    }
};
```

## Java

```java
class Solution {
    public String largestMerge(String word1, String word2) {
        int i = 0, j = 0;
        int n1 = word1.length(), n2 = word2.length();
        StringBuilder sb = new StringBuilder(n1 + n2);
        while (i < n1 && j < n2) {
            char c1 = word1.charAt(i);
            char c2 = word2.charAt(j);
            if (c1 > c2) {
                sb.append(c1);
                i++;
            } else if (c1 < c2) {
                sb.append(c2);
                j++;
            } else { // equal, need to compare the remaining substrings
                int p = i, q = j;
                while (p < n1 && q < n2 && word1.charAt(p) == word2.charAt(q)) {
                    p++;
                    q++;
                }
                boolean takeFromWord1;
                if (q == n2) { // word2 exhausted -> word1 is larger
                    takeFromWord1 = true;
                } else if (p == n1) { // word1 exhausted -> word2 is larger
                    takeFromWord1 = false;
                } else {
                    takeFromWord1 = word1.charAt(p) > word2.charAt(q);
                }
                if (takeFromWord1) {
                    sb.append(c1);
                    i++;
                } else {
                    sb.append(c2);
                    j++;
                }
            }
        }
        while (i < n1) sb.append(word1.charAt(i++));
        while (j < n2) sb.append(word2.charAt(j++));
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = j = 0
        n, m = len(word1), len(word2)
        res = []
        while i < n and j < m:
            # Compare remaining substrings lexicographically
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        if i < n:
            res.append(word1[i:])
        if j < m:
            res.append(word2[j:])
        return ''.join(res)
```

## Python3

```python
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        n, m = len(word1), len(word2)
        res = []
        while i < n and j < m:
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        if i < n:
            res.append(word1[i:])
        if j < m:
            res.append(word2[j:])
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int suffixGreater(const char *a, const char *b) {
    while (*a && *b) {
        if (*a != *b) return *a > *b;
        ++a;
        ++b;
    }
    if (!*a && !*b) return 0;          // equal
    if (!*a) return 0;                 // a shorter -> not greater
    return 1;                          // b shorter -> a greater
}

char* largestMerge(char* word1, char* word2) {
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    int total = len1 + len2;
    char *res = (char *)malloc(total + 1);
    int i = 0, j = 0, k = 0;

    while (i < len1 && j < len2) {
        if (suffixGreater(word1 + i, word2 + j)) {
            res[k++] = word1[i++];
        } else {
            res[k++] = word2[j++];
        }
    }
    while (i < len1) res[k++] = word1[i++];
    while (j < len2) res[k++] = word2[j++];
    res[k] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestMerge(string word1, string word2) {
        int i = 0, j = 0;
        var sb = new System.Text.StringBuilder();
        int n1 = word1.Length, n2 = word2.Length;
        while (i < n1 && j < n2) {
            if (word1[i] > word2[j]) {
                sb.Append(word1[i++]);
            } else if (word1[i] < word2[j]) {
                sb.Append(word2[j++]);
            } else {
                int p = i, q = j;
                while (p < n1 && q < n2 && word1[p] == word2[q]) {
                    p++;
                    q++;
                }
                bool takeFromWord1;
                if (q == n2) { // word2 exhausted or equal
                    takeFromWord1 = true;
                } else if (p == n1) {
                    takeFromWord1 = false;
                } else {
                    takeFromWord1 = word1[p] > word2[q];
                }
                if (takeFromWord1) sb.Append(word1[i++]);
                else sb.Append(word2[j++]);
            }
        }
        if (i < n1) sb.Append(word1.Substring(i));
        if (j < n2) sb.Append(word2.Substring(j));
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var largestMerge = function(word1, word2) {
    let i = 0, j = 0;
    const n = word1.length, m = word2.length;
    const result = [];
    while (i < n && j < m) {
        if (word1.slice(i) > word2.slice(j)) {
            result.push(word1[i]);
            i++;
        } else {
            result.push(word2[j]);
            j++;
        }
    }
    if (i < n) result.push(word1.slice(i));
    if (j < m) result.push(word2.slice(j));
    return result.join('');
};
```

## Typescript

```typescript
function largestMerge(word1: string, word2: string): string {
    let i = 0, j = 0;
    const n1 = word1.length, n2 = word2.length;
    const result: string[] = [];

    while (i < n1 && j < n2) {
        if (word1[i] > word2[j]) {
            result.push(word1[i]);
            i++;
        } else if (word1[i] < word2[j]) {
            result.push(word2[j]);
            j++;
        } else {
            // characters equal, need to compare remaining substrings
            let p = i, q = j;
            while (p < n1 && q < n2 && word1[p] === word2[q]) {
                p++;
                q++;
            }
            let takeFromWord1: boolean;
            if (p === n1 && q === n2) {
                // both substrings are identical
                takeFromWord1 = true;
            } else if (p === n1) {
                // word1 exhausted, word2 is larger
                takeFromWord1 = false;
            } else if (q === n2) {
                // word2 exhausted, word1 is larger
                takeFromWord1 = true;
            } else {
                takeFromWord1 = word1[p] > word2[q];
            }

            if (takeFromWord1) {
                result.push(word1[i]);
                i++;
            } else {
                result.push(word2[j]);
                j++;
            }
        }
    }

    if (i < n1) result.push(word1.slice(i));
    if (j < n2) result.push(word2.slice(j));

    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function largestMerge($word1, $word2) {
        $i = 0;
        $j = 0;
        $n1 = strlen($word1);
        $n2 = strlen($word2);
        $result = '';

        while ($i < $n1 && $j < $n2) {
            if ($this->isFirstGreater($word1, $i, $word2, $j)) {
                $result .= $word1[$i];
                $i++;
            } else {
                $result .= $word2[$j];
                $j++;
            }
        }

        if ($i < $n1) {
            $result .= substr($word1, $i);
        }
        if ($j < $n2) {
            $result .= substr($word2, $j);
        }

        return $result;
    }

    private function isFirstGreater(string $s1, int $i, string $s2, int $j): bool {
        $len1 = strlen($s1);
        $len2 = strlen($s2);
        while ($i < $len1 && $j < $len2) {
            if ($s1[$i] !== $s2[$j]) {
                return $s1[$i] > $s2[$j];
            }
            $i++;
            $j++;
        }
        // If all compared characters are equal, the longer remaining suffix is larger.
        return $i < $len1;
    }
}
```

## Swift

```swift
class Solution {
    func largestMerge(_ word1: String, _ word2: String) -> String {
        let a = Array(word1)
        let b = Array(word2)
        var i = 0
        var j = 0
        var result: [Character] = []
        let n1 = a.count
        let n2 = b.count
        
        while i < n1 && j < n2 {
            if a[i] > b[j] {
                result.append(a[i])
                i += 1
            } else if a[i] < b[j] {
                result.append(b[j])
                j += 1
            } else {
                var ii = i
                var jj = j
                while ii < n1 && jj < n2 && a[ii] == b[jj] {
                    ii += 1
                    jj += 1
                }
                let takeFromFirst: Bool
                if ii == n1 && jj == n2 {
                    takeFromFirst = true
                } else if ii == n1 {
                    takeFromFirst = false
                } else if jj == n2 {
                    takeFromFirst = true
                } else {
                    takeFromFirst = a[ii] > b[jj]
                }
                
                if takeFromFirst {
                    result.append(a[i])
                    i += 1
                } else {
                    result.append(b[j])
                    j += 1
                }
            }
        }
        
        while i < n1 {
            result.append(a[i])
            i += 1
        }
        while j < n2 {
            result.append(b[j])
            j += 1
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestMerge(word1: String, word2: String): String {
        val sb = StringBuilder()
        var i = 0
        var j = 0
        val n1 = word1.length
        val n2 = word2.length
        while (i < n1 && j < n2) {
            if (word1.substring(i).compareTo(word2.substring(j)) > 0) {
                sb.append(word1[i])
                i++
            } else {
                sb.append(word2[j])
                j++
            }
        }
        if (i < n1) sb.append(word1.substring(i))
        if (j < n2) sb.append(word2.substring(j))
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String largestMerge(String word1, String word2) {
    int i = 0, j = 0;
    final sb = StringBuffer();
    while (i < word1.length && j < word2.length) {
      int c1 = word1.codeUnitAt(i);
      int c2 = word2.codeUnitAt(j);
      if (c1 > c2) {
        sb.writeCharCode(c1);
        i++;
      } else if (c1 < c2) {
        sb.writeCharCode(c2);
        j++;
      } else {
        int p = i, q = j;
        while (p < word1.length && q < word2.length &&
            word1.codeUnitAt(p) == word2.codeUnitAt(q)) {
          p++;
          q++;
        }
        bool takeFromWord1;
        if (q == word2.length) {
          takeFromWord1 = true; // word2 exhausted, choose from word1
        } else if (p == word1.length) {
          takeFromWord1 = false; // word1 exhausted, choose from word2
        } else {
          takeFromWord1 = word1.codeUnitAt(p) > word2.codeUnitAt(q);
        }
        if (takeFromWord1) {
          sb.writeCharCode(c1);
          i++;
        } else {
          sb.writeCharCode(c2);
          j++;
        }
      }
    }
    if (i < word1.length) sb.write(word1.substring(i));
    if (j < word2.length) sb.write(word2.substring(j));
    return sb.toString();
  }
}
```

## Golang

```go
package main

import "strings"

func larger(s1 string, i int, s2 string, j int) bool {
	n1, n2 := len(s1), len(s2)
	for i < n1 && j < n2 {
		if s1[i] != s2[j] {
			return s1[i] > s2[j]
		}
		i++
		j++
	}
	if i == n1 && j == n2 {
		return false
	}
	if i == n1 {
		return false
	}
	return true
}

func largestMerge(word1 string, word2 string) string {
	i, j := 0, 0
	n, m := len(word1), len(word2)
	var sb strings.Builder
	for i < n && j < m {
		if larger(word1, i, word2, j) {
			sb.WriteByte(word1[i])
			i++
		} else {
			sb.WriteByte(word2[j])
			j++
		}
	}
	if i < n {
		sb.WriteString(word1[i:])
	}
	if j < m {
		sb.WriteString(word2[j:])
	}
	return sb.String()
}
```

## Ruby

```ruby
def largest_merge(word1, word2)
  i = 0
  j = 0
  n1 = word1.length
  n2 = word2.length
  res = +''
  while i < n1 && j < n2
    if word1[i..-1] > word2[j..-1]
      res << word1[i]
      i += 1
    else
      res << word2[j]
      j += 1
    end
  end
  res << word1[i..-1] if i < n1
  res << word2[j..-1] if j < n2
  res
end
```

## Scala

```scala
object Solution {
  def largestMerge(word1: String, word2: String): String = {
    val n1 = word1.length
    val n2 = word2.length
    var i = 0
    var j = 0
    val sb = new StringBuilder

    def greater(i1: Int, j1: Int): Boolean = {
      var a = i1
      var b = j1
      while (a < n1 && b < n2 && word1.charAt(a) == word2.charAt(b)) {
        a += 1
        b += 1
      }
      if (a == n1 && b == n2) false
      else if (a == n1) false
      else if (b == n2) true
      else word1.charAt(a) > word2.charAt(b)
    }

    while (i < n1 && j < n2) {
      if (greater(i, j)) {
        sb.append(word1.charAt(i))
        i += 1
      } else {
        sb.append(word2.charAt(j))
        j += 1
      }
    }
    if (i < n1) sb.append(word1.substring(i))
    if (j < n2) sb.append(word2.substring(j))

    sb.toString()
  }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_merge(word1: String, word2: String) -> String {
        let mut i = 0usize;
        let mut j = 0usize;
        let n1 = word1.len();
        let n2 = word2.len();
        let bytes1 = word1.as_bytes();
        let bytes2 = word2.as_bytes();
        let mut res = String::with_capacity(n1 + n2);
        while i < n1 && j < n2 {
            if &word1[i..] > &word2[j..] {
                res.push(bytes1[i] as char);
                i += 1;
            } else {
                res.push(bytes2[j] as char);
                j += 1;
            }
        }
        if i < n1 {
            res.push_str(&word1[i..]);
        }
        if j < n2 {
            res.push_str(&word2[j..]);
        }
        res
    }
}
```

## Racket

```racket
#lang racket

(require rackunit)

;; Helper: returns #t if suffix of s1 starting at i is lexicographically greater than
;; suffix of s2 starting at j, otherwise #f.
(define (greater-suffix? s1 i s2 j)
  (let loop ((p i) (q j))
    (cond
      [(and (= p (string-length s1)) (= q (string-length s2))) #f] ; equal suffixes
      [(= p (string-length s1)) #f]                               ; s1 exhausted -> not greater
      [(= q (string-length s2)) #t]                               ; s2 exhausted -> s1 greater
      [else
       (let ((c1 (string-ref s1 p))
             (c2 (string-ref s2 q)))
         (cond
           [(char>? c1 c2) #t]
           [(char<? c1 c2) #f]
           [else (loop (+ p 1) (+ q 1))]))])))

(define/contract (largest-merge word1 word2)
  (-> string? string? string?)
  (let* ((n1 (string-length word1))
         (n2 (string-length word2)))
    (let loop ((i 0) (j 0) (rev '()))
      (cond
        [(and (= i n1) (= j n2)) (list->string (reverse rev))]
        [(= i n1)
         (loop i (+ j 1) (cons (string-ref word2 j) rev))]
        [(= j n2)
         (loop (+ i 1) j (cons (string-ref word1 i) rev))]
        [else
         (if (greater-suffix? word1 i word2 j)
             (loop (+ i 1) j (cons (string-ref word1 i) rev))
             (loop i (+ j 1) (cons (string-ref word2 j) rev)))]))))
```

## Erlang

```erlang
-module(solution).
-export([largest_merge/2]).

-spec largest_merge(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_merge(Word1, Word2) ->
    merge(Word1, Word2).

merge(<<>>, B) -> B;
merge(A, <<>>) -> A;
merge(A = <<C1/utf8, Rest1/binary>>, B = <<C2/utf8, Rest2/binary>>) ->
    case A > B of
        true  -> <<C1/utf8>> ++ merge(Rest1, B);
        false -> <<C2/utf8>> ++ merge(A, Rest2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_merge(word1 :: String.t(), word2 :: String.t()) :: String.t()
  def largest_merge(word1, word2) do
    merge(word1, word2, "")
  end

  defp merge("", "", acc), do: acc
  defp merge("", w2, acc), do: acc <> w2
  defp merge(w1, "", acc), do: acc <> w1

  defp merge(
         w1 = <<c1::binary-size(1), rest1::binary>>,
         w2 = <<c2::binary-size(1), rest2::binary>>,
         acc
       ) do
    if w1 > w2 do
      merge(rest1, w2, acc <> c1)
    else
      merge(w1, rest2, acc <> c2)
    end
  end
end
```
