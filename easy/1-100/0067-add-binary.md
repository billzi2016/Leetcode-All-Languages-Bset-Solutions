# 0067. Add Binary

## Cpp

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;
        string result;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            result.push_back('0' + (sum & 1));
            carry = sum >> 1;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

## Java

```java
class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        StringBuilder sb = new StringBuilder();
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            sb.append((char) ('0' + (sum & 1)));
            carry = sum >> 1;
        }
        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                total += ord(b[j]) - 48
                j -= 1
            res.append(chr((total & 1) + 48))
            carry = total >> 1
        return ''.join(reversed(res))
```

## Python3

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                total += ord(b[j]) - 48
                j -= 1
            res.append('1' if total % 2 else '0')
            carry = total // 2
        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* addBinary(char* a, char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    int maxLen = lenA > lenB ? lenA : lenB;
    
    // Temporary buffer: max length + possible carry + null terminator
    char *tmp = (char*)malloc(maxLen + 2);
    if (!tmp) return NULL;
    tmp[maxLen + 1] = '\0';
    
    int i = lenA - 1, j = lenB - 1;
    int pos = maxLen;          // position to fill in tmp
    int carry = 0;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        tmp[pos--] = (sum % 2) + '0';
        carry = sum / 2;
    }
    
    int start = pos + 1;               // first valid digit in tmp
    int resultLen = maxLen - pos;      // number of digits
    
    char *result = (char*)malloc(resultLen + 1);
    if (!result) {
        free(tmp);
        return NULL;
    }
    memcpy(result, tmp + start, resultLen);
    result[resultLen] = '\0';
    
    free(tmp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public string AddBinary(string a, string b) {
        int i = a.Length - 1;
        int j = b.Length - 1;
        int carry = 0;
        var sb = new System.Text.StringBuilder();
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            sb.Append((char)('0' + (sum & 1)));
            carry = sum >> 1;
        }
        var arr = sb.ToString().ToCharArray();
        System.Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let i = a.length - 1;
    let j = b.length - 1;
    let carry = 0;
    const res = [];
    while (i >= 0 || j >= 0 || carry) {
        const sum = (i >= 0 ? a.charCodeAt(i) - 48 : 0) +
                    (j >= 0 ? b.charCodeAt(j) - 48 : 0) + 
                    carry;
        res.push((sum % 2).toString());
        carry = sum >> 1; // same as Math.floor(sum / 2)
        i--;
        j--;
    }
    return res.reverse().join('');
};
```

## Typescript

```typescript
function addBinary(a: string, b: string): string {
    let i = a.length - 1;
    let j = b.length - 1;
    let carry = 0;
    const res: string[] = [];
    while (i >= 0 || j >= 0 || carry) {
        const sum =
            (i >= 0 ? (a.charCodeAt(i) - 48) : 0) +
            (j >= 0 ? (b.charCodeAt(j) - 48) : 0) +
            carry;
        res.push((sum % 2).toString());
        carry = sum > 1 ? 1 : 0;
        i--;
        j--;
    }
    return res.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return String
     */
    function addBinary($a, $b) {
        $i = strlen($a) - 1;
        $j = strlen($b) - 1;
        $carry = 0;
        $result = '';
        while ($i >= 0 || $j >= 0 || $carry > 0) {
            $sum = $carry;
            if ($i >= 0) {
                $sum += ($a[$i] === '1') ? 1 : 0;
                $i--;
            }
            if ($j >= 0) {
                $sum += ($b[$j] === '1') ? 1 : 0;
                $j--;
            }
            $result = ($sum % 2) . $result;
            $carry = intdiv($sum, 2);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        let aArr = Array(a)
        let bArr = Array(b)
        var i = aArr.count - 1
        var j = bArr.count - 1
        var carry = 0
        var res = [Character]()
        while i >= 0 || j >= 0 || carry > 0 {
            var sum = carry
            if i >= 0 {
                sum += aArr[i] == "1" ? 1 : 0
                i -= 1
            }
            if j >= 0 {
                sum += bArr[j] == "1" ? 1 : 0
                j -= 1
            }
            res.append((sum % 2) == 1 ? "1" : "0")
            carry = sum / 2
        }
        return String(res.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addBinary(a: String, b: String): String {
        val sb = StringBuilder()
        var i = a.length - 1
        var j = b.length - 1
        var carry = 0
        while (i >= 0 || j >= 0 || carry > 0) {
            var sum = carry
            if (i >= 0) {
                sum += a[i] - '0'
                i--
            }
            if (j >= 0) {
                sum += b[j] - '0'
                j--
            }
            sb.append((sum % 2))
            carry = sum / 2
        }
        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String addBinary(String a, String b) {
    int i = a.length - 1;
    int j = b.length - 1;
    int carry = 0;
    List<int> result = [];

    while (i >= 0 || j >= 0 || carry > 0) {
      int sum = carry;
      if (i >= 0) {
        sum += a.codeUnitAt(i) - 48;
        i--;
      }
      if (j >= 0) {
        sum += b.codeUnitAt(j) - 48;
        j--;
      }
      result.add((sum & 1) + 48);
      carry = sum >> 1;
    }

    return String.fromCharCodes(result.reversed);
  }
}
```

## Golang

```go
func addBinary(a string, b string) string {
    i, j := len(a)-1, len(b)-1
    carry := 0
    var res []byte
    for i >= 0 || j >= 0 || carry > 0 {
        sum := carry
        if i >= 0 {
            sum += int(a[i] - '0')
            i--
        }
        if j >= 0 {
            sum += int(b[j] - '0')
            j--
        }
        res = append(res, byte('0'+(sum%2)))
        carry = sum / 2
    }
    // reverse the result
    for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
        res[l], res[r] = res[r], res[l]
    }
    return string(res)
}
```

## Ruby

```ruby
def add_binary(a, b)
  i = a.length - 1
  j = b.length - 1
  carry = 0
  result = []
  while i >= 0 || j >= 0 || carry > 0
    sum = carry
    if i >= 0
      sum += a.getbyte(i) - 48
      i -= 1
    end
    if j >= 0
      sum += b.getbyte(j) - 48
      j -= 1
    end
    result << (sum & 1).to_s
    carry = sum >> 1
  end
  result.reverse.join
end
```

## Scala

```scala
object Solution {
    def addBinary(a: String, b: String): String = {
        val sb = new StringBuilder
        var i = a.length - 1
        var j = b.length - 1
        var carry = 0
        while (i >= 0 || j >= 0 || carry > 0) {
            var sum = carry
            if (i >= 0) {
                sum += a.charAt(i) - '0'
                i -= 1
            }
            if (j >= 0) {
                sum += b.charAt(j) - '0'
                j -= 1
            }
            sb.append((sum & 1).toString)
            carry = sum >> 1
        }
        sb.reverse.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a_bytes = a.as_bytes();
        let b_bytes = b.as_bytes();
        let mut i: i32 = a_bytes.len() as i32 - 1;
        let mut j: i32 = b_bytes.len() as i32 - 1;
        let mut carry = 0;
        let mut result: Vec<char> = Vec::new();

        while i >= 0 || j >= 0 || carry > 0 {
            let mut sum = carry;
            if i >= 0 {
                sum += (a_bytes[i as usize] - b'0') as i32;
                i -= 1;
            }
            if j >= 0 {
                sum += (b_bytes[j as usize] - b'0') as i32;
                j -= 1;
            }
            result.push(((sum % 2) as u8 + b'0') as char);
            carry = sum / 2;
        }

        result.iter().rev().collect()
    }
}
```

## Racket

```racket
(define/contract (add-binary a b)
  (-> string? string? string?)
  (let* ((len-a (string-length a))
         (len-b (string-length b)))
    (let loop ((i (sub1 len-a))
               (j (sub1 len-b))
               (carry 0)
               (acc '()))
      (if (and (< i 0) (< j 0) (= carry 0))
          (list->string (reverse acc))
          (let* ((da (if (>= i 0)
                         (- (char->integer (string-ref a i)) (char->integer #\0))
                         0))
                 (db (if (>= j 0)
                         (- (char->integer (string-ref b j)) (char->integer #\0))
                         0))
                 (sum (+ da db carry))
                 (digit (modulo sum 2))
                 (new-carry (quotient sum 2))
                 (next-acc (cons (integer->char (+ digit (char->integer #\0))) acc)))
            (loop (if (>= i 0) (sub1 i) i)
                  (if (>= j 0) (sub1 j) j)
                  new-carry
                  next-acc))))))
```

## Erlang

```erlang
-spec add_binary(unicode:unicode_binary(), unicode:unicode_binary()) -> unicode:unicode_binary().
add_binary(A, B) ->
    add_binary(lists:reverse(binary_to_list(A)),
               lists:reverse(binary_to_list(B)), 0, []).

add_binary([], [], 0, Acc) ->
    list_to_binary(lists:reverse(Acc));
add_binary([], [], Carry, Acc) when Carry > 0 ->
    list_to_binary(lists:reverse([ $1 | Acc ]));
add_binary(L1, L2, Carry, Acc) ->
    {D1, Rest1} = case L1 of
        [] -> {0, []};
        [H|T] -> {H - $0, T}
    end,
    {D2, Rest2} = case L2 of
        [] -> {0, []};
        [H|T] -> {H - $0, T}
    end,
    Sum = D1 + D2 + Carry,
    NewCarry = Sum div 2,
    Bit = (Sum rem 2) + $0,
    add_binary(Rest1, Rest2, NewCarry, [Bit | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec add_binary(a :: String.t(), b :: String.t()) :: String.t()
  def add_binary(a, b) do
    a_rev = :binary.bin_to_list(a) |> Enum.reverse()
    b_rev = :binary.bin_to_list(b) |> Enum.reverse()
    {res, carry} = add_lists(a_rev, b_rev, 0, [])
    final = if carry == 1, do: [?1 | res], else: res
    List.to_string(final)
  end

  defp add_lists([], [], carry, acc), do: {acc, carry}

  defp add_lists([ha | ta], [hb | tb], carry, acc) do
    sum = (ha - ?0) + (hb - ?0) + carry
    bit = rem(sum, 2)
    new_carry = div(sum, 2)
    add_lists(ta, tb, new_carry, [bit + ?0 | acc])
  end

  defp add_lists([ha | ta], [], carry, acc) do
    sum = (ha - ?0) + carry
    bit = rem(sum, 2)
    new_carry = div(sum, 2)
    add_lists(ta, [], new_carry, [bit + ?0 | acc])
  end

  defp add_lists([], [hb | tb], carry, acc) do
    sum = (hb - ?0) + carry
    bit = rem(sum, 2)
    new_carry = div(sum, 2)
    add_lists([], tb, new_carry, [bit + ?0 | acc])
  end
end
```
