# 1432. Max Difference You Can Get From Changing an Integer

## Cpp

```cpp
class Solution {
public:
    int maxDiff(int num) {
        string s = to_string(num);
        // compute maximum
        string maxStr = s;
        for (char d = '0'; d <= '9'; ++d) {
            if (d == '9') continue;
            size_t pos = s.find(d);
            if (pos != string::npos) {
                string t = s;
                for (char &c : t) if (c == d) c = '9';
                maxStr = t;
                break;
            }
        }
        // compute minimum
        string minStr = s;
        if (s[0] != '1') {
            char d = s[0];
            string t = s;
            for (char &c : t) if (c == d) c = '1';
            minStr = t;
        } else {
            bool replaced = false;
            for (size_t i = 1; i < s.size(); ++i) {
                if (s[i] != '0') {
                    char d = s[i];
                    string t = s;
                    for (char &c : t) if (c == d) c = '0';
                    minStr = t;
                    replaced = true;
                    break;
                }
            }
            // if no replacement possible, minStr stays as original
        }
        int a = stoi(maxStr);
        int b = stoi(minStr);
        return a - b;
    }
};
```

## Java

```java
class Solution {
    public int maxDiff(int num) {
        String s = Integer.toString(num);
        char[] chars = s.toCharArray();
        // Compute maximum
        String maxStr = s;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] != '9') {
                char target = chars[i];
                StringBuilder sb = new StringBuilder();
                for (char c : chars) {
                    sb.append(c == target ? '9' : c);
                }
                maxStr = sb.toString();
                break;
            }
        }
        int maxVal = Integer.parseInt(maxStr);
        // Compute minimum
        String minStr = s;
        if (chars[0] != '1') {
            char target = chars[0];
            StringBuilder sb = new StringBuilder();
            for (char c : chars) {
                sb.append(c == target ? '1' : c);
            }
            minStr = sb.toString();
        } else {
            int idx = -1;
            for (int i = 1; i < chars.length; i++) {
                if (chars[i] != chars[0] && chars[i] != '0') {
                    idx = i;
                    break;
                }
            }
            if (idx != -1) {
                char target = chars[idx];
                StringBuilder sb = new StringBuilder();
                for (char c : chars) {
                    sb.append(c == target ? '0' : c);
                }
                minStr = sb.toString();
            }
        }
        int minVal = Integer.parseInt(minStr);
        return maxVal - minVal;
    }
}
```

## Python

```python
class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        # compute maximum possible number
        max_s = s
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break

        # compute minimum possible number
        min_s = s
        first = s[0]
        if first != '1':
            min_s = s.replace(first, '1')
        else:
            for ch in s[1:]:
                if ch != first:
                    min_s = s.replace(ch, '0')
                    break

        return int(max_s) - int(min_s)
```

## Python3

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # compute maximum
        max_s = s
        for ch in s:
            if ch != '9':
                max_s = s.replace(ch, '9')
                break

        # compute minimum
        min_s = s
        if s[0] != '1':
            # replace leading digit with 1
            min_s = s.replace(s[0], '1')
        else:
            target = None
            for ch in s[1:]:
                if ch != '0' and ch != s[0]:
                    target = ch
                    break
            if target is not None:
                min_s = s.replace(target, '0')

        return int(max_s) - int(min_s)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxDiff(int num) {
    char s[12];
    sprintf(s, "%d", num);
    int len = strlen(s);

    // Compute maximum value
    char maxStr[12];
    strcpy(maxStr, s);
    char replaceMax = 0;
    for (int i = 0; i < len; ++i) {
        if (s[i] != '9') {
            replaceMax = s[i];
            break;
        }
    }
    if (replaceMax) {
        for (int i = 0; i < len; ++i) {
            if (maxStr[i] == replaceMax)
                maxStr[i] = '9';
        }
    }

    // Compute minimum value
    char minStr[12];
    strcpy(minStr, s);
    char replaceMin = 0;
    if (s[0] != '1') {
        replaceMin = s[0];
        for (int i = 0; i < len; ++i) {
            if (minStr[i] == replaceMin)
                minStr[i] = '1';
        }
    } else {
        for (int i = 1; i < len; ++i) {
            if (s[i] != '0' && s[i] != s[0]) {
                replaceMin = s[i];
                break;
            }
        }
        if (replaceMin) {
            for (int i = 0; i < len; ++i) {
                if (minStr[i] == replaceMin)
                    minStr[i] = '0';
            }
        }
    }

    int maxVal = atoi(maxStr);
    int minVal = atoi(minStr);
    return maxVal - minVal;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDiff(int num) {
        string s = num.ToString();
        int maxVal = int.MinValue;
        int minVal = int.MaxValue;
        for (int x = 0; x <= 9; x++) {
            for (int y = 0; y <= 9; y++) {
                char cx = (char)('0' + x);
                char cy = (char)('0' + y);
                var sb = new System.Text.StringBuilder();
                foreach (char c in s) {
                    sb.Append(c == cx ? cy : c);
                }
                string t = sb.ToString();
                if (t[0] == '0') continue; // leading zero not allowed
                int val = int.Parse(t);
                if (val > maxVal) maxVal = val;
                if (val < minVal) minVal = val;
            }
        }
        return maxVal - minVal;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var maxDiff = function(num) {
    const s = String(num);
    
    // Helper to replace all occurrences of a character
    const replaceAll = (str, target, repl) => str.split(target).join(repl);
    
    // Compute maximum value
    let maxStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '9') {
            maxStr = replaceAll(s, s[i], '9');
            break;
        }
    }
    
    // Compute minimum value
    let minStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '1') {
            const target = s[i];
            if (i === 0) {
                // most significant digit cannot become 0
                minStr = replaceAll(s, target, '1');
            } else {
                minStr = replaceAll(s, target, '0');
            }
            break;
        }
    }
    
    return Number(maxStr) - Number(minStr);
};
```

## Typescript

```typescript
function maxDiff(num: number): number {
    const s = num.toString();

    // Compute maximum possible value
    let maxStr = s;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== '9') {
            const target = s[i];
            maxStr = s.split('').map(ch => ch === target ? '9' : ch).join('');
            break;
        }
    }

    // Compute minimum possible value
    let minStr = s;
    if (s[0] !== '1') {
        const target = s[0];
        minStr = s.split('').map(ch => ch === target ? '1' : ch).join('');
    } else {
        for (let i = 1; i < s.length; i++) {
            if (s[i] !== '0') {
                const target = s[i];
                minStr = s.split('').map(ch => ch === target ? '0' : ch).join('');
                break;
            }
        }
    }

    return parseInt(maxStr, 10) - parseInt(minStr, 10);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function maxDiff($num) {
        $s = strval($num);
        $len = strlen($s);
        
        // Compute maximum possible number
        $maxStr = $s;
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] !== '9') {
                $maxStr = str_replace($s[$i], '9', $s);
                break;
            }
        }
        
        // Compute minimum possible number
        $minStr = $s;
        if ($s[0] !== '1') {
            $minStr = str_replace($s[0], '1', $s);
        } else {
            for ($i = 1; $i < $len; $i++) {
                if ($s[$i] !== '0') {
                    $minStr = str_replace($s[$i], '0', $s);
                    break;
                }
            }
        }
        
        return intval($maxStr) - intval($minStr);
    }
}
```

## Swift

```swift
class Solution {
    func maxDiff(_ num: Int) -> Int {
        let s = String(num)
        let chars = Array(s)
        
        // Helper to replace all occurrences of a target character with another character
        func replacedString(_ original: String, target: Character, replacement: Character) -> String {
            var result = ""
            for ch in original {
                result.append(ch == target ? replacement : ch)
            }
            return result
        }
        
        // Compute maximum possible number
        var maxStr = s
        for ch in chars {
            if ch != "9" {
                maxStr = replacedString(s, target: ch, replacement: "9")
                break
            }
        }
        
        // Compute minimum possible number
        var minStr = s
        if chars[0] != "1" {
            // Replace the most significant digit with '1'
            let target = chars[0]
            minStr = replacedString(s, target: target, replacement: "1")
        } else {
            var found = false
            for i in 1..<chars.count {
                if chars[i] != "0" && chars[i] != chars[0] {
                    let target = chars[i]
                    minStr = replacedString(s, target: target, replacement: "0")
                    found = true
                    break
                }
            }
            // If no suitable digit found, minStr remains unchanged
            if !found {
                // No change needed; already minimal
            }
        }
        
        let maxVal = Int(maxStr)!
        let minVal = Int(minStr)!
        return maxVal - minVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDiff(num: Int): Int {
        val original = num.toString()
        var minVal = Int.MAX_VALUE
        var maxVal = Int.MIN_VALUE
        for (x in '0'..'9') {
            for (y in '0'..'9') {
                val sb = StringBuilder()
                for (c in original) {
                    sb.append(if (c == x) y else c)
                }
                if (sb[0] == '0') continue
                val v = sb.toString().toInt()
                if (v < minVal) minVal = v
                if (v > maxVal) maxVal = v
            }
        }
        return maxVal - minVal
    }
}
```

## Dart

```dart
class Solution {
  int maxDiff(int num) {
    String s = num.toString();

    // Compute maximum value
    String maxStr = s;
    for (int i = 0; i < s.length; i++) {
      if (s[i] != '9') {
        String target = s[i];
        maxStr = s.replaceAll(target, '9');
        break;
      }
    }

    // Compute minimum value
    String minStr = s;
    if (s[0] != '1') {
      String target = s[0];
      minStr = s.replaceAll(target, '1');
    } else {
      bool replaced = false;
      for (int i = 1; i < s.length; i++) {
        if (s[i] != '0' && s[i] != s[0]) {
          String target = s[i];
          minStr = s.replaceAll(target, '0');
          replaced = true;
          break;
        }
      }
      // If no replacement possible, minStr remains original
    }

    int maxVal = int.parse(maxStr);
    int minVal = int.parse(minStr);
    return maxVal - minVal;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func maxDiff(num int) int {
	s := strconv.Itoa(num)

	// Compute maximum value
	maxStr := s
	for i := 0; i < len(s); i++ {
		if s[i] != '9' {
			target := s[i]
			var b strings.Builder
			b.Grow(len(s))
			for j := 0; j < len(s); j++ {
				if s[j] == target {
					b.WriteByte('9')
				} else {
					b.WriteByte(s[j])
				}
			}
			maxStr = b.String()
			break
		}
	}

	// Compute minimum value
	minStr := s
	if s[0] != '1' {
		target := s[0]
		var b strings.Builder
		b.Grow(len(s))
		for i := 0; i < len(s); i++ {
			if s[i] == target {
				b.WriteByte('1')
			} else {
				b.WriteByte(s[i])
			}
		}
		minStr = b.String()
	} else {
		found := false
		var target byte
		for i := 1; i < len(s); i++ {
			if s[i] != '1' {
				target = s[i]
				found = true
				break
			}
		}
		if found {
			var b strings.Builder
			b.Grow(len(s))
			for i := 0; i < len(s); i++ {
				if s[i] == target {
					b.WriteByte('0')
				} else {
					b.WriteByte(s[i])
				}
			}
			minStr = b.String()
		}
	}

	maxVal, _ := strconv.Atoi(maxStr)
	minVal, _ := strconv.Atoi(minStr)

	return maxVal - minVal
}
```

## Ruby

```ruby
def max_diff(num)
  s = num.to_s

  # Compute maximum value
  max_s = s.dup
  replace_max = nil
  s.each_char do |ch|
    if ch != '9'
      replace_max = ch
      break
    end
  end
  max_s.tr!(replace_max, '9') if replace_max

  # Compute minimum value
  min_s = s.dup
  first_char = s[0]
  if first_char != '1'
    # Replace leading digit with 1
    min_s.tr!(first_char, '1')
  else
    replace_min = nil
    s.each_char.with_index do |ch, idx|
      next if idx == 0
      if ch != first_char
        replace_min = ch
        break
      end
    end
    min_s.tr!(replace_min, '0') if replace_min
  end

  max_s.to_i - min_s.to_i
end
```

## Scala

```scala
object Solution {
    def maxDiff(num: Int): Int = {
        val s = num.toString
        val n = s.length
        // Compute maximum value
        var maxChars = s.toCharArray
        var i = 0
        while (i < n && maxChars(i) == '9') i += 1
        if (i < n) {
            val target = maxChars(i)
            for (j <- 0 until n) {
                if (maxChars(j) == target) maxChars(j) = '9'
            }
        }
        val maxVal = new String(maxChars).toInt

        // Compute minimum value
        var minChars = s.toCharArray
        if (minChars(0) != '1') {
            val target = minChars(0)
            for (j <- 0 until n) {
                if (minChars(j) == target) minChars(j) = '1'
            }
        } else {
            var found = false
            var k = 1
            while (k < n && !found) {
                val cur = minChars(k)
                if (cur != '0' && cur != minChars(0)) {
                    val target = cur
                    for (j <- 0 until n) {
                        if (minChars(j) == target) minChars(j) = '0'
                    }
                    found = true
                }
                k += 1
            }
        }
        val minVal = new String(minChars).toInt

        maxVal - minVal
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_diff(num: i32) -> i32 {
        let s = num.to_string();

        // Compute maximum possible number
        let mut max_s = s.clone();
        if let Some(first_non9) = s.chars().find(|&c| c != '9') {
            let target = first_non9;
            max_s = s
                .chars()
                .map(|c| if c == target { '9' } else { c })
                .collect();
        }

        // Compute minimum possible number
        let mut min_s = s.clone();
        let chars: Vec<char> = s.chars().collect();
        let first = chars[0];
        if first != '1' {
            let target = first;
            min_s = s
                .chars()
                .map(|c| if c == target { '1' } else { c })
                .collect();
        } else {
            // Find a digit (not the leading one) that can be turned into 0
            for &c in chars.iter().skip(1) {
                if c != first && c != '0' {
                    let target = c;
                    min_s = s
                        .chars()
                        .map(|ch| if ch == target { '0' } else { ch })
                        .collect();
                    break;
                }
            }
        }

        let max_val: i32 = max_s.parse().unwrap();
        let min_val: i32 = min_s.parse().unwrap();

        max_val - min_val
    }
}
```

## Racket

```racket
(define/contract (max-diff num)
  (-> exact-integer? exact-integer?)
  (letrec
      ((replace-all
        (lambda (s old new)
          (list->string
           (map (lambda (ch) (if (char=? ch old) new ch))
                (string->list s)))))
       
       (max-str
        (lambda (s)
          (let loop ((i 0) (len (string-length s)))
            (if (= i len)
                s
                (let ((ch (string-ref s i)))
                  (if (char=? ch #\9)
                      (loop (+ i 1) len)
                      (replace-all s ch #\9)))))))
       
       (min-str
        (lambda (s)
          (let ((first (string-ref s 0)))
            (if (not (char=? first #\1))
                (replace-all s first #\1)
                (let loop ((i 1) (len (string-length s)) (found #f))
                  (cond
                    [(= i len) s]
                    [else
                     (let ((ch (string-ref s i)))
                       (if (and (not (char=? ch first))
                                (not (char=? ch #\0)))
                           (replace-all s ch #\0)
                           (loop (+ i 1) len found)))])))))))
    (let* ((s (number->string num))
           (a (string->number (max-str s)))
           (b (string->number (min-str s))))
      (- a b))))
```

## Erlang

```erlang
-module(solution).
-export([max_diff/1]).

-spec max_diff(Num :: integer()) -> integer().
max_diff(Num) ->
    Str = integer_to_list(Num),
    MaxStr = max_transform(Str),
    MinStr = min_transform(Str),
    list_to_integer(MaxStr) - list_to_integer(MinStr).

%% Find the maximum possible number by replacing first non-9 digit with 9
max_transform(Str) ->
    case first_not_digit(Str, $9) of
        undefined -> Str;
        Digit -> replace_all(Str, Digit, $9)
    end.

%% Find the minimum possible number respecting leading-zero rule
min_transform([First|Rest] = Str) ->
    if First =/= $1 ->
            replace_all(Str, First, $1);
       true ->
            case first_not_digit(Rest, $0) of
                undefined -> Str;
                Digit -> replace_all(Str, Digit, $0)
            end
    end.

%% Return the first digit in List that is not Target, or 'undefined' if none.
first_not_digit([], _Target) ->
    undefined;
first_not_digit([H|T], Target) when H =/= Target ->
    H;
first_not_digit([_|T], Target) ->
    first_not_digit(T, Target).

%% Replace all occurrences of From with To in the list of characters.
replace_all(List, From, To) ->
    [if C == From -> To; true -> C end || C <- List].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_diff(num :: integer) :: integer
  def max_diff(num) do
    s = Integer.to_string(num)

    # Compute maximum possible number
    max_num =
      case String.graphemes(s) |> Enum.find(fn c -> c != "9" end) do
        nil ->
          num

        ch ->
          String.replace(s, ch, "9")
          |> String.to_integer()
      end

    # Compute minimum possible number
    first = String.at(s, 0)

    min_num =
      if first != "1" do
        String.replace(s, first, "1")
        |> String.to_integer()
      else
        idx =
          1..(String.length(s) - 1)
          |> Enum.find(fn i ->
            c = String.at(s, i)
            c != "0" and c != first
          end)

        case idx do
          nil ->
            num

          i ->
            ch = String.at(s, i)

            String.replace(s, ch, "0")
            |> String.to_integer()
        end
      end

    max_num - min_num
  end
end
```
