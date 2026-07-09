# 1668. Maximum Repeating Substring

## Cpp

```cpp
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        string repeated;
        int k = 0;
        while (true) {
            repeated += word;
            if (sequence.find(repeated) != string::npos)
                ++k;
            else
                break;
        }
        return k;
    }
};
```

## Java

```java
class Solution {
    public int maxRepeating(String sequence, String word) {
        int count = 0;
        StringBuilder sb = new StringBuilder();
        while (true) {
            sb.append(word);
            if (sequence.contains(sb.toString())) {
                count++;
            } else {
                break;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k = 0
        repeated = ""
        while True:
            repeated += word
            if repeated in sequence:
                k += 1
            else:
                break
        return k
```

## Python3

```python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated = ""
        while True:
            repeated += word
            if repeated in sequence:
                k += 1
            else:
                break
        return k
```

## C

```c
#include <string.h>

int maxRepeating(char* sequence, char* word) {
    int seqLen = strlen(sequence);
    int wlen = strlen(word);
    if (wlen == 0) return 0;

    char repeat[101] = {0}; // maximum possible length is 100 + null terminator
    int k = 0;

    while (1) {
        strcat(repeat, word);
        ++k;
        if ((int)strlen(repeat) > seqLen) break;
        if (!strstr(sequence, repeat)) {
            return k - 1;
        }
    }
    return k - 1;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxRepeating(string sequence, string word)
    {
        int count = 0;
        string repeated = "";
        while (true)
        {
            repeated += word;
            if (sequence.Contains(repeated))
                count++;
            else
                break;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sequence
 * @param {string} word
 * @return {number}
 */
var maxRepeating = function(sequence, word) {
    let k = 0;
    let repeated = '';
    while (true) {
        repeated += word;
        if (sequence.includes(repeated)) {
            k++;
        } else {
            break;
        }
    }
    return k;
};
```

## Typescript

```typescript
function maxRepeating(sequence: string, word: string): number {
    let k = 0;
    while (true) {
        const repeated = word.repeat(k + 1);
        if (sequence.includes(repeated)) {
            k++;
        } else {
            break;
        }
    }
    return k;
}
```

## Php

```php
class Solution {

    /**
     * @param String $sequence
     * @param String $word
     * @return Integer
     */
    function maxRepeating($sequence, $word) {
        $k = 0;
        $repeat = '';
        while (true) {
            $repeat .= $word; // add one more occurrence
            if (strpos($sequence, $repeat) !== false) {
                $k++;
            } else {
                break;
            }
        }
        return $k;
    }
}
```

## Swift

```swift
class Solution {
    func maxRepeating(_ sequence: String, _ word: String) -> Int {
        var k = 0
        var repeated = ""
        while true {
            repeated += word
            if sequence.contains(repeated) {
                k += 1
            } else {
                break
            }
        }
        return k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxRepeating(sequence: String, word: String): Int {
        var k = 0
        while (true) {
            val candidate = word.repeat(k + 1)
            if (sequence.contains(candidate)) {
                k++
            } else {
                break
            }
        }
        return k
    }
}
```

## Dart

```dart
class Solution {
  int maxRepeating(String sequence, String word) {
    int k = 0;
    String repeated = '';
    while (true) {
      repeated += word;
      if (sequence.contains(repeated)) {
        k++;
      } else {
        break;
      }
    }
    return k;
  }
}
```

## Golang

```go
package main

import "strings"

func maxRepeating(sequence string, word string) int {
	k := 0
	for {
		candidate := strings.Repeat(word, k+1)
		if strings.Contains(sequence, candidate) {
			k++
		} else {
			break
		}
	}
	return k
}
```

## Ruby

```ruby
def max_repeating(sequence, word)
  repeat = ''
  k = 0
  loop do
    repeat << word
    k += 1
    break unless sequence.include?(repeat)
  end
  k - 1
end
```

## Scala

```scala
object Solution {
    def maxRepeating(sequence: String, word: String): Int = {
        var k = 0
        while (sequence.contains(word * (k + 1))) {
            k += 1
        }
        k
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let mut repeated = String::new();
        let mut k = 0;
        loop {
            repeated.push_str(&word);
            if sequence.contains(&repeated) {
                k += 1;
            } else {
                break;
            }
        }
        k as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)

(define/contract (max-repeating sequence word)
  (-> string? string? exact-integer?)
  (let loop ((k 1) (best 0))
    (define repeated (apply string-append (make-list k word)))
    (if (and (> (string-length repeated) 0)
             (string-contains? sequence repeated))
        (loop (+ k 1) k)
        best)))
```

## Erlang

```erlang
-spec max_repeating(Sequence :: unicode:unicode_binary(), Word :: unicode:unicode_binary()) -> integer().
max_repeating(Sequence, Word) ->
    max_repeating_loop(Sequence, Word, 0, <<>>).

max_repeating_loop(_Seq, _Word, K, _Repeated) when K > 1000 ->
    K;
max_repeating_loop(Seq, Word, K, Repeated) ->
    Next = <<Repeated/binary, Word/binary>>,
    case binary:match(Seq, Next) of
        {_, _} -> max_repeating_loop(Seq, Word, K + 1, Next);
        nomatch -> K
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_repeating(String.t(), String.t()) :: integer()
  def max_repeating(sequence, word) do
    loop(sequence, word, 1, 0)
  end

  defp loop(seq, word, k, max) do
    repeated = String.duplicate(word, k)

    if String.contains?(seq, repeated) do
      loop(seq, word, k + 1, k)
    else
      max
    end
  end
end
```
