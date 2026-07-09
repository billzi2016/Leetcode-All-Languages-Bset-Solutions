# 2269. Find the K-Beauty of a Number

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int divisorSubstrings(int num, int k) {
        string s = to_string(num);
        int n = s.size();
        int ans = 0;
        for (int i = 0; i + k <= n; ++i) {
            int val = stoi(s.substr(i, k));
            if (val != 0 && num % val == 0) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int divisorSubstrings(int num, int k) {
        String s = Integer.toString(num);
        int n = s.length();
        int count = 0;
        for (int i = 0; i <= n - k; i++) {
            int sub = Integer.parseInt(s.substring(i, i + k));
            if (sub != 0 && num % sub == 0) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        s = str(num)
        n = len(s)
        count = 0
        for i in range(n - k + 1):
            sub_val = int(s[i:i+k])
            if sub_val != 0 and num % sub_val == 0:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        cnt = 0
        for i in range(n - k + 1):
            sub = int(s[i:i + k])
            if sub != 0 and num % sub == 0:
                cnt += 1
        return cnt
```

## C

```c
#include <stdio.h>
#include <string.h>

int divisorSubstrings(int num, int k) {
    char s[12];
    sprintf(s, "%d", num);
    int len = strlen(s);
    int count = 0;
    for (int i = 0; i <= len - k; ++i) {
        int val = 0;
        for (int j = 0; j < k; ++j) {
            val = val * 10 + (s[i + j] - '0');
        }
        if (val != 0 && num % val == 0) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int DivisorSubstrings(int num, int k)
    {
        string s = num.ToString();
        int count = 0;
        for (int i = 0; i <= s.Length - k; i++)
        {
            int sub = int.Parse(s.Substring(i, k));
            if (sub != 0 && num % sub == 0)
                count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @param {number} k
 * @return {number}
 */
var divisorSubstrings = function(num, k) {
    const s = String(num);
    let count = 0;
    for (let i = 0; i <= s.length - k; ++i) {
        const sub = parseInt(s.substr(i, k), 10);
        if (sub !== 0 && num % sub === 0) {
            ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function divisorSubstrings(num: number, k: number): number {
    const s = num.toString();
    let count = 0;
    for (let i = 0; i <= s.length - k; ++i) {
        const sub = s.slice(i, i + k);
        const val = parseInt(sub, 10);
        if (val !== 0 && num % val === 0) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $k
     * @return Integer
     */
    function divisorSubstrings($num, $k) {
        $s = strval($num);
        $len = strlen($s);
        $count = 0;
        for ($i = 0; $i <= $len - $k; $i++) {
            $sub = substr($s, $i, $k);
            $val = intval($sub);
            if ($val != 0 && $num % $val == 0) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func divisorSubstrings(_ num: Int, _ k: Int) -> Int {
        let s = String(num)
        var count = 0
        let length = s.count
        guard k <= length else { return 0 }
        for i in 0...(length - k) {
            let start = s.index(s.startIndex, offsetBy: i)
            let end = s.index(start, offsetBy: k)
            let subStr = String(s[start..<end])
            if let val = Int(subStr), val != 0, num % val == 0 {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun divisorSubstrings(num: Int, k: Int): Int {
        val s = num.toString()
        var count = 0
        for (i in 0..s.length - k) {
            val sub = s.substring(i, i + k).toInt()
            if (sub != 0 && num % sub == 0) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int divisorSubstrings(int num, int k) {
    String s = num.toString();
    int count = 0;
    for (int i = 0; i <= s.length - k; i++) {
      int val = int.parse(s.substring(i, i + k));
      if (val != 0 && num % val == 0) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
import "strconv"

func divisorSubstrings(num int, k int) int {
	s := strconv.Itoa(num)
	n := len(s)
	count := 0
	for i := 0; i <= n-k; i++ {
		subStr := s[i : i+k]
		val, _ := strconv.Atoi(subStr)
		if val != 0 && num%val == 0 {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def divisor_substrings(num, k)
  s = num.to_s
  count = 0
  (0..s.length - k).each do |i|
    val = s[i, k].to_i
    next if val == 0
    count += 1 if num % val == 0
  end
  count
end
```

## Scala

```scala
object Solution {
    def divisorSubstrings(num: Int, k: Int): Int = {
        val s = num.toString
        var count = 0
        for (i <- 0 to s.length - k) {
            val sub = s.substring(i, i + k)
            val value = sub.toInt
            if (value != 0 && num % value == 0) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divisor_substrings(num: i32, k: i32) -> i32 {
        let s = num.to_string();
        let n = s.len();
        let k_usize = k as usize;
        let mut count = 0;
        for i in 0..=n - k_usize {
            let sub = &s[i..i + k_usize];
            if let Ok(val) = sub.parse::<i32>() {
                if val != 0 && num % val == 0 {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (divisor-substrings num k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([s   (number->string num)]
         [len (string-length s)])
    (let loop ((i 0) (cnt 0))
      (if (> i (- len k))
          cnt
          (let* ([sub (substring s i (+ i k))]
                 [val (string->number sub)])
            (loop (+ i 1)
                  (if (and (not (= val 0))
                           (= (remainder num val) 0))
                      (+ cnt 1)
                      cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([divisor_substrings/2]).

-spec divisor_substrings(integer(), integer()) -> integer().
divisor_substrings(Num, K) ->
    Str = integer_to_list(Num),
    Len = length(Str),
    count_divisors(Str, 1, K, Num, Len, 0).

count_divisors(_Str, Pos, K, _Num, Len, Acc) when Pos + K - 1 > Len ->
    Acc;
count_divisors(Str, Pos, K, Num, Len, Acc) ->
    Sub = lists:sublist(Str, Pos, K),
    Val = list_to_integer(Sub),
    NewAcc = case Val of
        0 -> Acc;
        _ when Num rem Val == 0 -> Acc + 1;
        _ -> Acc
    end,
    count_divisors(Str, Pos + 1, K, Num, Len, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec divisor_substrings(num :: integer, k :: integer) :: integer
  def divisor_substrings(num, k) do
    s = Integer.to_string(num)
    len = String.length(s)
    max_start = len - k

    0..max_start
    |> Enum.reduce(0, fn i, acc ->
      sub_str = String.slice(s, i, k)
      {sub_int, _} = Integer.parse(sub_str)

      if sub_int != 0 and rem(num, sub_int) == 0 do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
