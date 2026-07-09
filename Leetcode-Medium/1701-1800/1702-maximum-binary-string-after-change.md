# 1702. Maximum Binary String After Change

## Cpp

```cpp
class Solution {
public:
    string maximumBinaryString(string binary) {
        int n = binary.size();
        int zeroCount = 0;
        for (char c : binary) if (c == '0') ++zeroCount;
        if (zeroCount <= 1) return binary;
        string res;
        res.append(n - zeroCount, '1');
        res.push_back('0');
        res.append(zeroCount - 1, '1');
        return res;
    }
};
```

## Java

```java
class Solution {
    public String maximumBinaryString(String binary) {
        int n = binary.length();
        int firstZero = -1;
        for (int i = 0; i < n; i++) {
            if (binary.charAt(i) == '0') {
                firstZero = i;
                break;
            }
        }
        // If there is no zero, the string is already maximal.
        if (firstZero == -1) {
            return binary;
        }

        int zeros = 0;
        for (int i = firstZero; i < n; i++) {
            if (binary.charAt(i) == '0') {
                zeros++;
            }
        }

        StringBuilder sb = new StringBuilder();
        // Keep the prefix before the first zero as all ones.
        for (int i = 0; i < firstZero; i++) {
            sb.append('1');
        }
        // Fill with (zeros - 1) ones.
        for (int i = 0; i < zeros - 1; i++) {
            sb.append('1');
        }
        // Append the final zero.
        sb.append('0');

        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        n = len(binary)
        first_zero = binary.find('0')
        last_one = binary.rfind('1')
        if first_zero == -1 or last_one == -1 or first_zero > last_one:
            return binary
        # there exists at least one "01" pattern
        return '1' * first_zero + '0' + '1' * (n - last_one - 1)
```

## Python3

```python
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        cnt0 = binary.count('0')
        if cnt0 == 0:
            return binary
        # place (cnt0-1) leading '1's, then a single '0', then the rest '1's
        return '1' * (cnt0 - 1) + '0' + '1' * (n - cnt0)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* maximumBinaryString(char* binary) {
    int n = strlen(binary);
    int firstZero = -1;
    int totalZeros = 0;
    for (int i = 0; i < n; ++i) {
        if (binary[i] == '0') {
            if (firstZero == -1) firstZero = i;
            ++totalZeros;
        }
    }

    char* ans = (char*)malloc(n + 1);
    if (!ans) return NULL;

    if (totalZeros == 0) {
        memcpy(ans, binary, n + 1);
        return ans;
    }

    int zeroPos = firstZero + totalZeros - 1;
    for (int i = 0; i < n; ++i) {
        if (i < zeroPos) ans[i] = '1';
        else if (i == zeroPos) ans[i] = '0';
        else ans[i] = '1';
    }
    ans[n] = '\0';
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public string MaximumBinaryString(string binary) {
        int n = binary.Length;
        int zeroCount = 0;
        foreach (char c in binary) {
            if (c == '0') zeroCount++;
        }
        if (zeroCount == 0) return binary;

        int firstZero = binary.IndexOf('0');
        int leadingOnes = firstZero + zeroCount - 1;
        int trailingOnes = n - firstZero - zeroCount;

        var sb = new System.Text.StringBuilder();
        if (leadingOnes > 0) sb.Append(new string('1', leadingOnes));
        sb.Append('0');
        if (trailingOnes > 0) sb.Append(new string('1', trailingOnes));

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} binary
 * @return {string}
 */
var maximumBinaryString = function(binary) {
    const n = binary.length;
    // Count zeros and find first zero index
    let zeroCount = 0;
    let firstZeroIdx = -1;
    for (let i = 0; i < n; ++i) {
        if (binary[i] === '0') {
            zeroCount++;
            if (firstZeroIdx === -1) firstZeroIdx = i;
        }
    }
    // If no zeros, already maximal
    if (zeroCount === 0) return binary;
    
    const prefixOnes = firstZeroIdx + zeroCount - 1; // number of leading '1's before the single zero
    const result =
        '1'.repeat(prefixOnes) +
        '0' +
        '1'.repeat(n - prefixOnes - 1);
    return result;
};
```

## Typescript

```typescript
function maximumBinaryString(binary: string): string {
    const n = binary.length;
    let zeroCount = 0;
    for (let i = 0; i < n; ++i) {
        if (binary[i] === '0') zeroCount++;
    }
    if (zeroCount <= 1) return binary;
    const leadingOnes = n - zeroCount;
    return '1'.repeat(leadingOnes) + '0' + '1'.repeat(zeroCount - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param String $binary
     * @return String
     */
    function maximumBinaryString($binary) {
        $n = strlen($binary);
        $zeroCount = substr_count($binary, '0');
        if ($zeroCount <= 1) {
            return $binary;
        }
        $prefixOnes = str_repeat('1', $n - $zeroCount + 1);
        $suffixOnes = str_repeat('1', $zeroCount - 2);
        return $prefixOnes . '0' . $suffixOnes;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBinaryString(_ binary: String) -> String {
        let chars = Array(binary)
        let n = chars.count
        var firstZero = -1
        var lastZero = -1
        
        for i in 0..<n {
            if chars[i] == "0" {
                if firstZero == -1 { firstZero = i }
                lastZero = i
            }
        }
        
        // No zero present, already maximal
        if firstZero == -1 {
            return binary
        }
        
        var result = [Character]()
        // Prefix of ones before the first zero
        for _ in 0..<firstZero {
            result.append("1")
        }
        // Single zero (since there is at least one zero in original)
        result.append("0")
        // Fill the rest with ones
        let remaining = n - firstZero - 1
        for _ in 0..<remaining {
            result.append("1")
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBinaryString(binary: String): String {
        val n = binary.length
        var zeroCount = 0
        for (ch in binary) if (ch == '0') zeroCount++
        if (zeroCount == 0) return binary

        var firstZero = -1
        for (i in 0 until n) {
            if (binary[i] == '0') {
                firstZero = i
                break
            }
        }

        val sb = StringBuilder(n)
        val leadingOnes = firstZero + zeroCount - 1
        repeat(leadingOnes) { sb.append('1') }
        sb.append('0')
        val trailingOnes = n - firstZero - zeroCount
        repeat(trailingOnes) { sb.append('1') }

        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String maximumBinaryString(String binary) {
    int n = binary.length;
    int firstZero = binary.indexOf('0');
    if (firstZero == -1) return binary;

    int suffixOnes = 0;
    for (int i = firstZero; i < n; ++i) {
      if (binary[i] == '1') suffixOnes++;
    }

    int leadingOnesCount = n - suffixOnes - 1;

    String repeat(String ch, int count) {
      if (count <= 0) return '';
      return List.filled(count, ch).join();
    }

    return repeat('1', leadingOnesCount) + '0' + repeat('1', suffixOnes);
  }
}
```

## Golang

```go
func maximumBinaryString(binary string) string {
	n := len(binary)
	zeroCount := 0
	firstZero := -1
	for i, ch := range binary {
		if ch == '0' {
			zeroCount++
			if firstZero == -1 {
				firstZero = i
			}
		}
	}
	if zeroCount == 0 {
		return binary
	}
	var sb strings.Builder
	sb.Grow(n)
	for i := 0; i < firstZero; i++ {
		sb.WriteByte('1')
	}
	sb.WriteByte('0')
	trailingOnes := n - firstZero - zeroCount
	for i := 0; i < trailingOnes; i++ {
		sb.WriteByte('1')
	}
	return sb.String()
}
```

## Ruby

```ruby
def maximum_binary_string(binary)
  n = binary.length
  first_zero = binary.index('0')
  return binary if first_zero.nil?
  last_zero = binary.rindex('0')
  prefix = '1' * first_zero
  suffix_len = n - last_zero - 1
  prefix + '0' + '1' * suffix_len
end
```

## Scala

```scala
object Solution {
    def maximumBinaryString(binary: String): String = {
        val n = binary.length
        var zeroCount = 0
        for (c <- binary) if (c == '0') zeroCount += 1

        if (zeroCount == 0) return binary

        val leadingOnes = n - zeroCount
        val sb = new StringBuilder(n)

        for (_ <- 0 until leadingOnes) sb.append('1')
        sb.append('0')
        for (_ <- 0 until zeroCount - 1) sb.append('1')

        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_binary_string(binary: String) -> String {
        let n = binary.len();
        let zeros = binary.bytes().filter(|&b| b == b'0').count();
        if zeros == 0 {
            return binary;
        }
        let mut res = String::with_capacity(n);
        for _ in 0..(n - zeros) {
            res.push('1');
        }
        res.push('0');
        for _ in 0..(zeros - 1) {
            res.push('1');
        }
        res
    }
}
```

## Racket

```racket
(define/contract (maximum-binary-string binary)
  (-> string? string?)
  (let* ((n (string-length binary))
         ;; count total zeros
         (zero-count
          (let loop ((i 0) (cnt 0))
            (if (>= i n)
                cnt
                (loop (+ i 1)
                      (if (char=? (string-ref binary i) #\0)
                          (+ cnt 1)
                          cnt)))))
         ;; index of first zero (valid when zero-count > 0)
         (first-zero
          (let loop ((i 0))
            (if (char=? (string-ref binary i) #\0)
                i
                (loop (+ i 1))))))
    (if (= zero-count 0)
        binary
        (let* ((prefix-ones first-zero)
               (suffix-ones (- n prefix-ones 1)))
          (string-append (make-string prefix-ones #\1)
                         "0"
                         (make-string suffix-ones #\1))))))
```

## Erlang

```erlang
-spec maximum_binary_string(Binary :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_binary_string(Binary) ->
    N = byte_size(Binary),
    case binary:match(Binary, <<"1">>) of
        nomatch ->
            %% all zeros
            case N of
                0 -> <<>>;
                1 -> <<"0">>;
                _ ->
                    Prefix = binary:copy(<<$1>>, N - 1),
                    <<Prefix/binary, $0>>
            end;
        {_Pos,_Len} ->
            case binary:match(Binary, <<"0">>) of
                nomatch -> Binary; % all ones
                _ ->
                    LeadingOnes = count_leading_ones(Binary, N),
                    RestLen = N - LeadingOnes - 1,
                    <<(binary:copy(<<$1>>, LeadingOnes))/binary,
                      $0,
                      (binary:copy(<<$1>>, RestLen))/binary>>
            end
    end.

count_leading_ones(Bin, Len) ->
    count_leading_ones(Bin, 0, Len).

count_leading_ones(_Bin, Index, Len) when Index >= Len -> Index;
count_leading_ones(Bin, Index, Len) ->
    case binary:at(Bin, Index) of
        $1 -> count_leading_ones(Bin, Index + 1, Len);
        _  -> Index
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_binary_string(binary :: String.t) :: String.t
  def maximum_binary_string(binary) do
    len = byte_size(binary)
    if len < 2 do
      binary
    else
      # Find first occurrence of "01"
      idx =
        0..(len - 2)
        |> Enum.find(fn i ->
          <<_::binary-size(i), a, b, _::binary>> = binary
          a == ?0 and b == ?1
        end)

      case idx do
        nil -> binary
        i ->
          leading = String.duplicate("1", i + 1)
          trailing_len = len - (i + 2)
          trailing = String.duplicate("1", trailing_len)
          leading <> "0" <> trailing
      end
    end
  end
end
```
