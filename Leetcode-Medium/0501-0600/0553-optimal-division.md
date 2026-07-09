# 0553. Optimal Division

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return "";
        if (n == 1) return to_string(nums[0]);
        if (n == 2) return to_string(nums[0]) + "/" + to_string(nums[1]);
        string res = to_string(nums[0]) + "/(";
        for (int i = 1; i < n; ++i) {
            res += to_string(nums[i]);
            if (i != n - 1) res += "/";
        }
        res += ")";
        return res;
    }
};
```

## Java

```java
class Solution {
    public String optimalDivision(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return Integer.toString(nums[0]);
        }
        if (n == 2) {
            return nums[0] + "/" + nums[1];
        }
        StringBuilder sb = new StringBuilder();
        sb.append(nums[0]).append("/(");
        for (int i = 1; i < n; i++) {
            sb.append(nums[i]);
            if (i != n - 1) {
                sb.append("/");
            }
        }
        sb.append(")");
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return "{}/{}".format(nums[0], nums[1])
        # For three or more numbers, put parentheses around everything after the first number
        middle = "/".join(str(x) for x in nums[1:])
        return "{}({})".format(nums[0] + "/", middle) if False else f"{nums[0]}/({middle})"
```

## Python3

```python
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 0:
            return ""
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f"{nums[0]}/{nums[1]}"
        middle = "/".join(str(x) for x in nums[1:])
        return f"{nums[0]}/({middle})"
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int digitCount(int x) {
    int cnt = 0;
    do {
        cnt++;
        x /= 10;
    } while (x);
    return cnt;
}

char* optimalDivision(int* nums, int numsSize) {
    if (numsSize == 0) return NULL;

    int totalLen = 0;
    if (numsSize == 1) {
        totalLen = digitCount(nums[0]);
    } else if (numsSize == 2) {
        totalLen = digitCount(nums[0]) + 1 + digitCount(nums[1]); // a/b
    } else {
        // a/(b/c/.../n)
        totalLen += digitCount(nums[0]); // first number
        totalLen += 1; // '/'
        totalLen += 1; // '('
        for (int i = 1; i < numsSize; ++i) {
            totalLen += digitCount(nums[i]);
            if (i != numsSize - 1) totalLen += 1; // '/'
        }
        totalLen += 1; // ')'
    }

    char *res = (char *)malloc(totalLen + 1);
    char *p = res;

    p += sprintf(p, "%d", nums[0]);

    if (numsSize == 1) {
        *p = '\0';
        return res;
    }

    if (numsSize == 2) {
        sprintf(p, "/%d", nums[1]);
        return res;
    }

    // numsSize >= 3
    *p++ = '/';
    *p++ = '(';
    for (int i = 1; i < numsSize; ++i) {
        p += sprintf(p, "%d", nums[i]);
        if (i != numsSize - 1) {
            *p++ = '/';
        }
    }
    *p++ = ')';
    *p = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string OptimalDivision(int[] nums)
    {
        int n = nums.Length;
        if (n == 1) return nums[0].ToString();
        if (n == 2) return $"{nums[0]}/{nums[1]}";

        var sb = new System.Text.StringBuilder();
        sb.Append(nums[0]);
        sb.Append("/(");
        for (int i = 1; i < n; i++)
        {
            sb.Append(nums[i]);
            if (i != n - 1) sb.Append('/');
        }
        sb.Append(')');
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {string}
 */
var optimalDivision = function(nums) {
    const n = nums.length;
    if (n === 1) return `${nums[0]}`;
    if (n === 2) return `${nums[0]}/${nums[1]}`;
    const inner = nums.slice(1).join('/');
    return `${nums[0]}/(${inner})`;
};
```

## Typescript

```typescript
function optimalDivision(nums: number[]): string {
    const n = nums.length;
    if (n === 0) return "";
    if (n === 1) return `${nums[0]}`;
    if (n === 2) return `${nums[0]}/${nums[1]}`;
    return `${nums[0]}/(${nums.slice(1).join('/')})`;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return String
     */
    function optimalDivision($nums) {
        $n = count($nums);
        if ($n == 0) {
            return "";
        }
        if ($n == 1) {
            return (string)$nums[0];
        }
        if ($n == 2) {
            return $nums[0] . '/' . $nums[1];
        }
        $rest = implode('/', array_slice($nums, 1));
        return $nums[0] . '/(' . $rest . ')';
    }
}
```

## Swift

```swift
class Solution {
    func optimalDivision(_ nums: [Int]) -> String {
        let n = nums.count
        if n == 1 {
            return "\(nums[0])"
        }
        if n == 2 {
            return "\(nums[0])/\(nums[1])"
        }
        var result = "\(nums[0])/("
        for i in 1..<n {
            result += "\(nums[i])"
            if i != n - 1 {
                result += "/"
            }
        }
        result += ")"
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun optimalDivision(nums: IntArray): String {
        val n = nums.size
        if (n == 1) return "${nums[0]}"
        if (n == 2) return "${nums[0]}/${nums[1]}"
        val sb = StringBuilder()
        sb.append(nums[0])
        sb.append("/(")
        for (i in 1 until n) {
            sb.append(nums[i])
            if (i != n - 1) sb.append('/')
        }
        sb.append(')')
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String optimalDivision(List<int> nums) {
    int n = nums.length;
    if (n == 0) return "";
    if (n == 1) return nums[0].toString();
    if (n == 2) return '${nums[0]}/${nums[1]}';
    StringBuffer sb = StringBuffer();
    sb.write(nums[0]);
    sb.write('/(');
    for (int i = 1; i < n; i++) {
      sb.write(nums[i]);
      if (i != n - 1) sb.write('/');
    }
    sb.write(')');
    return sb.toString();
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func optimalDivision(nums []int) string {
	n := len(nums)
	if n == 1 {
		return strconv.Itoa(nums[0])
	}
	if n == 2 {
		return strconv.Itoa(nums[0]) + "/" + strconv.Itoa(nums[1])
	}
	var sb strings.Builder
	sb.WriteString(strconv.Itoa(nums[0]))
	sb.WriteString("/(")
	for i := 1; i < n; i++ {
		if i > 1 {
			sb.WriteByte('/')
		}
		sb.WriteString(strconv.Itoa(nums[i]))
	}
	sb.WriteByte(')')
	return sb.String()
}
```

## Ruby

```ruby
def optimal_division(nums)
  case nums.length
  when 1
    nums[0].to_s
  when 2
    "#{nums[0]}/#{nums[1]}"
  else
    rest = nums[1..-1].map(&:to_s).join('/')
    "#{nums[0]}/(#{rest})"
  end
end
```

## Scala

```scala
object Solution {
    def optimalDivision(nums: Array[Int]): String = {
        val n = nums.length
        if (n == 0) ""
        else if (n == 1) nums(0).toString
        else if (n == 2) s"${nums(0)}/${nums(1)}"
        else {
            val sb = new StringBuilder()
            sb.append(nums(0)).append("/(")
            for (i <- 1 until n) {
                sb.append(nums(i))
                if (i != n - 1) sb.append("/")
            }
            sb.append(")")
            sb.toString()
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn optimal_division(nums: Vec<i32>) -> String {
        let n = nums.len();
        match n {
            0 => String::new(),
            1 => nums[0].to_string(),
            2 => format!("{}/{}", nums[0], nums[1]),
            _ => {
                let denominator = nums[1..]
                    .iter()
                    .map(|v| v.to_string())
                    .collect::<Vec<String>>()
                    .join("/");
                format!("{}/({})", nums[0], denominator)
            }
        }
    }
}
```

## Racket

```racket
(define/contract (optimal-division nums)
  (-> (listof exact-integer?) string?)
  (cond
    [(null? nums) ""]
    [(= (length nums) 1) (number->string (car nums))]
    [(= (length nums) 2) (format "~a/~a" (car nums) (cadr nums))]
    [else
     (let* ([first (car nums)]
            [rest (cdr nums)]
            [inner (string-join (map number->string rest) "/")])
       (format "~a/(~a)" first inner))]))
```

## Erlang

```erlang
-spec optimal_division(Nums :: [integer()]) -> unicode:unicode_binary().
optimal_division(Nums) ->
    case Nums of
        [] ->
            <<>>;
        [A] ->
            erlang:integer_to_binary(A);
        [A, B] ->
            << (erlang:integer_to_binary(A))/binary, $/, (erlang:integer_to_binary(B))/binary >>;
        [A | Rest] ->
            RestBins = lists:map(fun erlang:integer_to_binary/1, Rest),
            Joined = string:join(RestBins, "/"),
            << (erlang:integer_to_binary(A))/binary, $/, $(, Joined/binary, $) >>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec optimal_division(nums :: [integer]) :: String.t()
  def optimal_division(nums) do
    case nums do
      [] -> ""
      [x] -> Integer.to_string(x)
      [a, b] -> "#{a}/#{b}"
      [a | rest] ->
        inner = Enum.map_join(rest, "/", &Integer.to_string/1)
        "#{a}/(#{inner})"
    end
  end
end
```
