# 2496. Maximum Value of a String in an Array

## Cpp

```cpp
class Solution {
public:
    int maximumValue(vector<string>& strs) {
        int ans = 0;
        for (const string& s : strs) {
            bool allDigits = true;
            for (char c : s) {
                if (!isdigit(c)) { allDigits = false; break; }
            }
            int val;
            if (allDigits) {
                int num = 0;
                for (char c : s) {
                    num = num * 10 + (c - '0');
                }
                val = num;
            } else {
                val = static_cast<int>(s.size());
            }
            ans = max(ans, val);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumValue(String[] strs) {
        int maxVal = 0;
        for (String s : strs) {
            boolean allDigits = true;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c < '0' || c > '9') {
                    allDigits = false;
                    break;
                }
            }
            int val;
            if (allDigits) {
                // parse integer, leading zeros are handled automatically
                val = Integer.parseInt(s);
            } else {
                val = s.length();
            }
            if (val > maxVal) {
                maxVal = val;
            }
        }
        return maxVal;
    }
}
```

## Python

```python
class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_val = 0
        for s in strs:
            if s.isdigit():
                val = int(s)
            else:
                val = len(s)
            if val > max_val:
                max_val = val
        return max_val
```

## Python3

```python
from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            if s.isdigit():
                val = int(s)
            else:
                val = len(s)
            if val > max_val:
                max_val = val
        return max_val
```

## C

```c
#include <stddef.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int maximumValue(char** strs, int strsSize) {
    int maxVal = 0;
    for (int i = 0; i < strsSize; ++i) {
        char *s = strs[i];
        int allDigits = 1;
        for (char *p = s; *p != '\0'; ++p) {
            if (!isdigit((unsigned char)*p)) {
                allDigits = 0;
                break;
            }
        }
        int val;
        if (allDigits) {
            val = atoi(s);
        } else {
            val = (int)strlen(s);
        }
        if (val > maxVal) maxVal = val;
    }
    return maxVal;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumValue(string[] strs) {
        int maxVal = 0;
        foreach (var s in strs) {
            bool allDigits = true;
            foreach (char c in s) {
                if (!char.IsDigit(c)) {
                    allDigits = false;
                    break;
                }
            }
            int val;
            if (allDigits) {
                // Parse numeric value; leading zeros are handled automatically.
                // Since length <= 9, it fits into int.
                val = int.Parse(s);
            } else {
                val = s.Length;
            }
            if (val > maxVal) maxVal = val;
        }
        return maxVal;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var maximumValue = function(strs) {
    let maxVal = 0;
    for (const s of strs) {
        if (/^\d+$/.test(s)) {
            const num = parseInt(s, 10);
            if (num > maxVal) maxVal = num;
        } else {
            const len = s.length;
            if (len > maxVal) maxVal = len;
        }
    }
    return maxVal;
};
```

## Typescript

```typescript
function maximumValue(strs: string[]): number {
    let maxVal = 0;
    for (const s of strs) {
        if (/^\d+$/.test(s)) {
            const num = parseInt(s, 10);
            if (num > maxVal) maxVal = num;
        } else {
            const len = s.length;
            if (len > maxVal) maxVal = len;
        }
    }
    return maxVal;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function maximumValue($strs) {
        $max = 0;
        foreach ($strs as $s) {
            if (ctype_digit($s)) {
                $val = intval($s);
            } else {
                $val = strlen($s);
            }
            if ($val > $max) {
                $max = $val;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumValue(_ strs: [String]) -> Int {
        var result = 0
        for s in strs {
            if let num = Int(s) {
                result = max(result, num)
            } else {
                result = max(result, s.count)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumValue(strs: Array<String>): Int {
        var maxVal = 0
        for (s in strs) {
            val value = if (s.all { it.isDigit() }) s.toInt() else s.length
            if (value > maxVal) maxVal = value
        }
        return maxVal
    }
}
```

## Dart

```dart
class Solution {
  int maximumValue(List<String> strs) {
    int maxVal = 0;
    for (var s in strs) {
      bool allDigits = true;
      for (int i = 0; i < s.length; i++) {
        int code = s.codeUnitAt(i);
        if (code < 48 || code > 57) { // not '0'-'9'
          allDigits = false;
          break;
        }
      }
      int value = allDigits ? int.parse(s) : s.length;
      if (value > maxVal) {
        maxVal = value;
      }
    }
    return maxVal;
  }
}
```

## Golang

```go
package main

import "strconv"

func maximumValue(strs []string) int {
	maxVal := 0
	for _, s := range strs {
		allDigits := true
		for i := 0; i < len(s); i++ {
			if s[i] < '0' || s[i] > '9' {
				allDigits = false
				break
			}
		}
		var val int
		if allDigits {
			v, _ := strconv.Atoi(s)
			val = v
		} else {
			val = len(s)
		}
		if val > maxVal {
			maxVal = val
		}
	}
	return maxVal
}
```

## Ruby

```ruby
def maximum_value(strs)
  max_val = 0
  strs.each do |s|
    if s =~ /\A\d+\z/
      val = s.to_i
    else
      val = s.length
    end
    max_val = val if val > max_val
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def maximumValue(strs: Array[String]): Int = {
        strs.map { s =>
            if (s.forall(_.isDigit)) s.toInt else s.length
        }.max
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_value(strs: Vec<String>) -> i32 {
        let mut max_val = 0i32;
        for s in strs.iter() {
            if s.bytes().all(|b| b.is_ascii_digit()) {
                // All digits: value is the numeric interpretation
                let val: i32 = s.parse::<i32>().unwrap_or(0);
                if val > max_val {
                    max_val = val;
                }
            } else {
                // Contains letters: value is its length
                let len = s.len() as i32;
                if len > max_val {
                    max_val = len;
                }
            }
        }
        max_val
    }
}
```

## Racket

```racket
(define/contract (maximum-value strs)
  (-> (listof string?) exact-integer?)
  (let* ([values
          (map (lambda (s)
                 (if (for/and ([c (in-string s)])
                       (and (char>=? c #\0) (char<=? c #\9)))
                     (string->number s)
                     (string-length s)))
               strs)])
    (apply max values)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_value/1]).

-spec maximum_value(Strs :: [unicode:unicode_binary()]) -> integer().
maximum_value(Strs) ->
    lists:max([value(S) || S <- Strs]).

value(Bin) ->
    case is_digit_string(Bin) of
        true  -> erlang:list_to_integer(binary_to_list(Bin));
        false -> byte_size(Bin)
    end.

is_digit_string(Bin) ->
    lists:all(fun(C) -> C >= $0, C =< $9 end,
              binary_to_list(Bin)).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_value(strs :: [String.t]) :: integer
  def maximum_value(strs) do
    strs
    |> Enum.map(fn s ->
      if String.match?(s, ~r/^\d+$/) do
        String.to_integer(s)
      else
        String.length(s)
      end
    end)
    |> Enum.max()
  end
end
```
