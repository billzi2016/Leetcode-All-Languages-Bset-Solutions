# 1946. Largest Number After Mutating Substring

## Cpp

```cpp
class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        bool started = false;
        for (int i = 0; i < (int)num.size(); ++i) {
            int orig = num[i] - '0';
            int mapped = change[orig];
            if (!started) {
                if (mapped > orig) {
                    started = true;
                    num[i] = char('0' + mapped);
                }
            } else {
                if (mapped >= orig) {
                    num[i] = char('0' + mapped);
                } else {
                    break;
                }
            }
        }
        return num;
    }
};
```

## Java

```java
class Solution {
    public String maximumNumber(String num, int[] change) {
        char[] chars = num.toCharArray();
        boolean started = false;
        for (int i = 0; i < chars.length; i++) {
            int orig = chars[i] - '0';
            int mapped = change[orig];
            if (!started) {
                if (mapped > orig) {
                    started = true;
                    chars[i] = (char) ('0' + mapped);
                }
            } else {
                if (mapped >= orig) {
                    chars[i] = (char) ('0' + mapped);
                } else {
                    break;
                }
            }
        }
        return new String(chars);
    }
}
```

## Python

```python
class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        n = list(num)
        started = False
        for i, ch in enumerate(n):
            d = ord(ch) - 48  # int conversion faster
            nd = change[d]
            if not started:
                if nd > d:
                    started = True
                    n[i] = str(nd)
            else:
                if nd >= d:
                    n[i] = str(nd)
                else:
                    break
        return "".join(n)
```

## Python3

```python
from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        chars = list(num)
        started = False
        for i, ch in enumerate(chars):
            d = ord(ch) - 48  # int conversion faster
            new_d = change[d]
            if not started:
                if new_d > d:
                    started = True
                    chars[i] = str(new_d)
            else:
                if new_d >= d:
                    chars[i] = str(new_d)
                else:
                    break
        return ''.join(chars)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* maximumNumber(char* num, int* change, int changeSize) {
    size_t n = strlen(num);
    char *res = (char*)malloc(n + 1);
    if (!res) return NULL;
    
    int started = 0;
    for (size_t i = 0; i < n; ++i) {
        int d = num[i] - '0';
        int nd = change[d];
        if (!started) {
            if (nd > d) {
                started = 1;
                res[i] = (char)(nd + '0');
            } else {
                res[i] = num[i];
            }
        } else {
            if (nd >= d) {
                res[i] = (char)(nd + '0');
            } else {
                // stop mutation, copy the rest unchanged
                res[i] = num[i];
                for (size_t j = i + 1; j < n; ++j)
                    res[j] = num[j];
                res[n] = '\0';
                return res;
            }
        }
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string MaximumNumber(string num, int[] change)
    {
        char[] arr = num.ToCharArray();
        bool started = false;
        for (int i = 0; i < arr.Length; i++)
        {
            int orig = arr[i] - '0';
            int mapped = change[orig];
            if (!started)
            {
                if (mapped > orig)
                {
                    started = true;
                    arr[i] = (char)('0' + mapped);
                }
            }
            else
            {
                if (mapped >= orig)
                {
                    arr[i] = (char)('0' + mapped);
                }
                else
                {
                    break;
                }
            }
        }
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number[]} change
 * @return {string}
 */
var maximumNumber = function(num, change) {
    const n = num.length;
    const res = [];
    let started = false;
    for (let i = 0; i < n; i++) {
        const d = num.charCodeAt(i) - 48; // digit value
        const mapped = change[d];
        if (!started) {
            if (mapped > d) {
                started = true;
                res.push(String(mapped));
            } else {
                res.push(num[i]);
            }
        } else {
            if (mapped >= d) {
                res.push(String(mapped));
            } else {
                // stop mutation, copy the rest unchanged
                res.push(...num.slice(i));
                break;
            }
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function maximumNumber(num: string, change: number[]): string {
    const n = num.length;
    const result: string[] = [];
    let started = false;

    for (let i = 0; i < n; ++i) {
        const digit = num.charCodeAt(i) - 48; // original digit
        const mapped = change[digit];          // changed digit

        if (!started) {
            if (mapped > digit) {
                started = true;
                result.push(String.fromCharCode(mapped + 48));
            } else {
                result.push(num[i]);
            }
        } else {
            if (mapped >= digit) {
                result.push(String.fromCharCode(mapped + 48));
            } else {
                // stop mutating, copy the rest unchanged
                result.push(...num.slice(i).split(''));
                break;
            }
        }
    }

    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @param Integer[] $change
     * @return String
     */
    function maximumNumber($num, $change) {
        $len = strlen($num);
        $res = '';
        $started = false;
        for ($i = 0; $i < $len; $i++) {
            $orig = intval($num[$i]);
            $new = $change[$orig];
            if (!$started) {
                if ($new > $orig) {
                    $started = true;
                    $res .= (string)$new;
                } else {
                    $res .= $num[$i];
                }
            } else {
                if ($new >= $orig) {
                    $res .= (string)$new;
                } else {
                    $res .= substr($num, $i);
                    break;
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func maximumNumber(_ num: String, _ change: [Int]) -> String {
        var chars = Array(num)
        let n = chars.count
        var i = 0
        
        // Find the first position where mutation increases the digit
        while i < n {
            if let d = chars[i].wholeNumberValue, change[d] > d {
                break
            }
            i += 1
        }
        
        // If no such position exists, return original number
        if i == n { return num }
        
        // Mutate the substring while it does not decrease any digit
        while i < n {
            if let d = chars[i].wholeNumberValue, change[d] >= d {
                chars[i] = Character(String(change[d]))
                i += 1
            } else {
                break
            }
        }
        
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumNumber(num: String, change: IntArray): String {
        val chars = num.toCharArray()
        var started = false
        for (i in chars.indices) {
            val orig = chars[i] - '0'
            val newDigit = change[orig]
            if (!started) {
                if (newDigit > orig) {
                    started = true
                    chars[i] = ('0'.code + newDigit).toChar()
                }
            } else {
                if (newDigit >= orig) {
                    chars[i] = ('0'.code + newDigit).toChar()
                } else {
                    break
                }
            }
        }
        return String(chars)
    }
}
```

## Dart

```dart
class Solution {
  String maximumNumber(String num, List<int> change) {
    List<String> chars = num.split('');
    int state = 0; // 0: not started, 1: mutating, 2: finished
    for (int i = 0; i < chars.length; i++) {
      int orig = chars[i].codeUnitAt(0) - 48;
      int newDigit = change[orig];
      if (state == 0) {
        if (newDigit > orig) {
          state = 1;
          chars[i] = newDigit.toString();
        }
      } else if (state == 1) {
        if (newDigit >= orig) {
          chars[i] = newDigit.toString();
        } else {
          state = 2;
        }
      }
    }
    return chars.join('');
  }
}
```

## Golang

```go
func maximumNumber(num string, change []int) string {
    b := []byte(num)
    started := false
    for i := 0; i < len(b); i++ {
        orig := int(b[i] - '0')
        newVal := change[orig]
        if !started {
            if newVal > orig {
                started = true
                b[i] = byte('0' + newVal)
            }
        } else {
            if newVal >= orig {
                b[i] = byte('0' + newVal)
            } else {
                break
            }
        }
    }
    return string(b)
}
```

## Ruby

```ruby
def maximum_number(num, change)
  chars = num.chars
  n = chars.length
  i = 0
  # Find the start of the segment where mutation is beneficial
  while i < n && change[chars[i].ord - 48] <= (chars[i].ord - 48)
    i += 1
  end
  return num if i == n

  # Mutate while it does not make the digit smaller
  while i < n && change[chars[i].ord - 48] >= (chars[i].ord - 48)
    chars[i] = change[chars[i].ord - 48].to_s
    i += 1
  end

  chars.join
end
```

## Scala

```scala
object Solution {
    def maximumNumber(num: String, change: Array[Int]): String = {
        val n = num.length
        val sb = new StringBuilder(n)
        var started = false
        var ended = false
        for (i <- 0 until n) {
            val origChar = num.charAt(i)
            val orig = origChar - '0'
            val mapped = change(orig)
            if (!started) {
                if (mapped > orig) {
                    started = true
                    sb.append(mapped)
                } else {
                    sb.append(origChar)
                }
            } else if (!ended) {
                if (mapped >= orig) {
                    sb.append(mapped)
                } else {
                    ended = true
                    sb.append(origChar)
                }
            } else {
                sb.append(origChar)
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_number(num: String, change: Vec<i32>) -> String {
        let bytes = num.as_bytes();
        let n = bytes.len();
        let mut res: Vec<u8> = Vec::with_capacity(n);
        let mut i = 0;
        let mut started = false;

        while i < n {
            let d = (bytes[i] - b'0') as usize;
            let mapped = change[d] as u8;
            if !started {
                if mapped > d as u8 {
                    started = true;
                    res.push(b'0' + mapped);
                } else {
                    res.push(bytes[i]);
                }
                i += 1;
            } else {
                if mapped >= d as u8 {
                    res.push(b'0' + mapped);
                    i += 1;
                } else {
                    // stop mutation, copy the rest unchanged
                    while i < n {
                        res.push(bytes[i]);
                        i += 1;
                    }
                }
            }
        }

        String::from_utf8(res).unwrap()
    }
}
```

## Racket

```racket
(define/contract (maximum-number num change)
  (-> string? (listof exact-integer?) string?)
  (let* ((len (string-length num))
         (zero-char (char->integer #\0)))
    (let loop ((i 0) (started #f) (ended #f) (acc '()))
      (if (= i len)
          (list->string (reverse acc))
          (let* ((ch (string-ref num i))
                 (d (- (char->integer ch) zero-char))
                 (newd (list-ref change d)))
            (cond
              [(and (not started) (> newd d))
               (loop (+ i 1) #t #f
                     (cons (integer->char (+ newd zero-char)) acc))]
              [started
               (if (and (not ended) (>= newd d))
                   (loop (+ i 1) #t #f
                         (cons (integer->char (+ newd zero-char)) acc))
                   (loop (+ i 1) started #t
                         (cons ch acc)))]
              [else
               (loop (+ i 1) started ended
                     (cons ch acc))]))))))
```

## Erlang

```erlang
-spec maximum_number(Num :: unicode:unicode_binary(), Change :: [integer()]) -> unicode:unicode_binary().
maximum_number(Num, Change) ->
    Digits = binary_to_list(Num),
    ChangeTuple = list_to_tuple(Change),
    {ResRev, _Started, _Done} = mutate(Digits, ChangeTuple, [], false, false),
    list_to_binary(lists:reverse(ResRev)).

mutate([], _, Acc, Started, Done) ->
    {Acc, Started, Done};
mutate([C | Rest], ChangeTuple, Acc, Started, Done) ->
    D = C - $0,
    NewDInt = element(D + 1, ChangeTuple),
    case {Started, Done} of
        {false, _} ->
            if NewDInt > D ->
                    mutate(Rest, ChangeTuple, [NewDInt + $0 | Acc], true, false);
               true ->
                    mutate(Rest, ChangeTuple, [C | Acc], false, false)
            end;
        {true, false} ->
            if NewDInt >= D ->
                    mutate(Rest, ChangeTuple, [NewDInt + $0 | Acc], true, false);
               true ->
                    mutate(Rest, ChangeTuple, [C | Acc], true, true)
            end;
        {true, true} ->
            mutate(Rest, ChangeTuple, [C | Acc], true, true)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_number(num :: String.t(), change :: [integer]) :: String.t()
  def maximum_number(num, change) do
    digits = String.graphemes(num)

    {result_rev, _started, _done} =
      Enum.reduce(digits, {[], false, false}, fn ch, {acc, started, done} ->
        if done do
          {[ch | acc], started, true}
        else
          d = String.to_integer(ch)
          mapped = Enum.at(change, d)

          cond do
            not started and mapped > d ->
              {[Integer.to_string(mapped) | acc], true, false}

            started and mapped >= d ->
              {[Integer.to_string(mapped) | acc], true, false}

            started and mapped < d ->
              {[ch | acc], started, true}

            true ->
              {[ch | acc], started, false}
          end
        end
      end)

    result_rev |> Enum.reverse() |> Enum.join()
  end
end
```
