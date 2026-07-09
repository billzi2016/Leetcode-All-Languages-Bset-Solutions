# 0038. Count and Say

## Cpp

```cpp
class Solution {
public:
    string countAndSay(int n) {
        string cur = "1";
        for (int i = 1; i < n; ++i) {
            string nxt;
            int cnt = 1;
            for (size_t j = 1; j <= cur.size(); ++j) {
                if (j < cur.size() && cur[j] == cur[j - 1]) {
                    ++cnt;
                } else {
                    nxt += to_string(cnt);
                    nxt.push_back(cur[j - 1]);
                    cnt = 1;
                }
            }
            cur.swap(nxt);
        }
        return cur;
    }
};
```

## Java

```java
class Solution {
    public String countAndSay(int n) {
        String result = "1";
        for (int i = 1; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            int count = 1;
            char prev = result.charAt(0);
            for (int j = 1; j < result.length(); j++) {
                char cur = result.charAt(j);
                if (cur == prev) {
                    count++;
                } else {
                    sb.append(count).append(prev);
                    prev = cur;
                    count = 1;
                }
            }
            sb.append(count).append(prev);
            result = sb.toString();
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(1, n):
            nxt = []
            i = 0
            while i < len(s):
                cnt = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    cnt += 1
                nxt.append(str(cnt))
                nxt.append(s[i])
                i += 1
            s = "".join(nxt)
        return s
```

## Python3

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1, n):
            i = 0
            nxt = []
            while i < len(s):
                cnt = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    cnt += 1
                nxt.append(str(cnt))
                nxt.append(s[i])
                i += 1
            s = "".join(nxt)
        return s
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static char *next_seq(const char *s) {
    int len = strlen(s);
    int cap = len * 2 + 10;               // initial capacity
    char *res = (char *)malloc(cap);
    int pos = 0;
    for (int i = 0; i < len; ) {
        char cur = s[i];
        int cnt = 0;
        while (i < len && s[i] == cur) {
            ++cnt;
            ++i;
        }
        // ensure enough space
        if (pos + 12 >= cap) {            // worst case: count up to many digits + char
            cap *= 2;
            res = (char *)realloc(res, cap);
        }
        pos += sprintf(res + pos, "%d%c", cnt, cur);
    }
    res[pos] = '\0';
    return res;
}

char* countAndSay(int n) {
    if (n <= 1) {
        char *base = (char *)malloc(2);
        base[0] = '1';
        base[1] = '\0';
        return base;
    }
    char *cur = (char *)malloc(2);
    cur[0] = '1';
    cur[1] = '\0';
    for (int i = 2; i <= n; ++i) {
        char *next = next_seq(cur);
        free(cur);
        cur = next;
    }
    return cur;
}
```

## Csharp

```csharp
public class Solution {
    public string CountAndSay(int n) {
        string result = "1";
        for (int i = 1; i < n; i++) {
            var sb = new System.Text.StringBuilder();
            int count = 1;
            for (int j = 1; j < result.Length; j++) {
                if (result[j] == result[j - 1]) {
                    count++;
                } else {
                    sb.Append(count);
                    sb.Append(result[j - 1]);
                    count = 1;
                }
            }
            sb.Append(count);
            sb.Append(result[result.Length - 1]);
            result = sb.ToString();
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let seq = "1";
    for (let i = 1; i < n; i++) {
        let next = "";
        let count = 1;
        for (let j = 1; j < seq.length; j++) {
            if (seq[j] === seq[j - 1]) {
                count++;
            } else {
                next += count + seq[j - 1];
                count = 1;
            }
        }
        next += count + seq[seq.length - 1];
        seq = next;
    }
    return seq;
};
```

## Typescript

```typescript
function countAndSay(n: number): string {
    let current = "1";
    for (let i = 1; i < n; i++) {
        let next = "";
        let count = 1;
        for (let j = 1; j < current.length; j++) {
            if (current[j] === current[j - 1]) {
                count++;
            } else {
                next += count.toString() + current[j - 1];
                count = 1;
            }
        }
        next += count.toString() + current[current.length - 1];
        current = next;
    }
    return current;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function countAndSay($n) {
        $result = "1";
        for ($i = 1; $i < $n; $i++) {
            $prev = $result;
            $len = strlen($prev);
            $sb = "";
            $count = 1;
            for ($j = 1; $j <= $len; $j++) {
                if ($j < $len && $prev[$j] === $prev[$j - 1]) {
                    $count++;
                } else {
                    $sb .= strval($count) . $prev[$j - 1];
                    $count = 1;
                }
            }
            $result = $sb;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countAndSay(_ n: Int) -> String {
        if n == 1 { return "1" }
        var current = "1"
        for _ in 2...n {
            var nextStr = ""
            let chars = Array(current)
            var i = 0
            while i < chars.count {
                let ch = chars[i]
                var count = 0
                while i < chars.count && chars[i] == ch {
                    count += 1
                    i += 1
                }
                nextStr.append(String(count))
                nextStr.append(ch)
            }
            current = nextStr
        }
        return current
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countAndSay(n: Int): String {
        var current = "1"
        repeat(n - 1) {
            val sb = StringBuilder()
            var i = 0
            while (i < current.length) {
                val ch = current[i]
                var count = 0
                while (i < current.length && current[i] == ch) {
                    i++
                    count++
                }
                sb.append(count)
                sb.append(ch)
            }
            current = sb.toString()
        }
        return current
    }
}
```

## Dart

```dart
class Solution {
  String countAndSay(int n) {
    String result = '1';
    for (int i = 1; i < n; ++i) {
      StringBuffer sb = StringBuffer();
      int count = 1;
      for (int j = 1; j < result.length; ++j) {
        if (result[j] == result[j - 1]) {
          count++;
        } else {
          sb.write(count);
          sb.write(result[j - 1]);
          count = 1;
        }
      }
      sb.write(count);
      sb.write(result[result.length - 1]);
      result = sb.toString();
    }
    return result;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func countAndSay(n int) string {
	if n <= 0 {
		return ""
	}
	res := "1"
	for i := 2; i <= n; i++ {
		var sb strings.Builder
		count := 1
		for j := 1; j < len(res); j++ {
			if res[j] == res[j-1] {
				count++
			} else {
				sb.WriteString(strconv.Itoa(count))
				sb.WriteByte(res[j-1])
				count = 1
			}
		}
		sb.WriteString(strconv.Itoa(count))
		sb.WriteByte(res[len(res)-1])
		res = sb.String()
	}
	return res
}
```

## Ruby

```ruby
def count_and_say(n)
  result = "1"
  (2..n).each do
    prev = result
    sb = +""
    i = 0
    while i < prev.length
      count = 1
      while i + 1 < prev.length && prev[i] == prev[i + 1]
        i += 1
        count += 1
      end
      sb << count.to_s << prev[i]
      i += 1
    end
    result = sb
  end
  result
end
```

## Scala

```scala
object Solution {
    def countAndSay(n: Int): String = {
        var current = "1"
        for (_ <- 2 to n) {
            val sb = new StringBuilder
            var i = 0
            while (i < current.length) {
                var j = i
                while (j < current.length && current.charAt(j) == current.charAt(i)) {
                    j += 1
                }
                val count = j - i
                sb.append(count)
                sb.append(current.charAt(i))
                i = j
            }
            current = sb.toString()
        }
        current
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut current = String::from("1");
        for _ in 2..=n {
            let mut next = String::new();
            let chars: Vec<char> = current.chars().collect();
            let mut i = 0;
            while i < chars.len() {
                let ch = chars[i];
                let mut count = 1;
                i += 1;
                while i < chars.len() && chars[i] == ch {
                    count += 1;
                    i += 1;
                }
                next.push_str(&count.to_string());
                next.push(ch);
            }
            current = next;
        }
        current
    }
}
```

## Racket

```racket
(define/contract (count-and-say n)
  (-> exact-integer? string?)
  (letrec ((next-term
            (lambda (s)
              (let loop ((i 0) (len (string-length s)) (res ""))
                (if (= i len)
                    res
                    (let* ((ch (string-ref s i))
                           (j (let find ((k i))
                                (if (or (= k len)
                                        (not (char=? (string-ref s k) ch)))
                                    k
                                    (find (+ k 1))))))
                      (loop j len
                            (string-append res
                                           (number->string (- j i))
                                           (string ch)))))))))
    (let recur ((i 1) (cur "1"))
      (if (= i n)
          cur
          (recur (+ i 1) (next-term cur)))))
```

## Erlang

```erlang
-spec count_and_say(N :: integer()) -> unicode:unicode_binary().
count_and_say(N) when N =< 0 ->
    <<>>;
count_and_say(N) ->
    iter(N, <<"1">>).

%% iterative generation
iter(1, Bin) -> Bin;
iter(K, Bin) when K > 1 ->
    Next = next_seq(Bin),
    iter(K - 1, Next).

%% generate next term from current binary string
next_seq(Bin) ->
    List = binary:bin_to_list(Bin),
    case List of
        [] -> <<>>;
        [First | Rest] ->
            Result = process(Rest, First, 1, []),
            list_to_binary(Result)
    end.

%% process runs, building result in reverse order; final reversal restores correct order
process([], Prev, Count, Acc) ->
    Segment = integer_to_list(Count) ++ [Prev],
    RevSeg = lists:reverse(Segment),
    lists:reverse(RevSeg ++ Acc);
process([H | T], Prev, Count, Acc) when H =:= Prev ->
    process(T, Prev, Count + 1, Acc);
process([H | T], Prev, Count, Acc) ->
    Segment = integer_to_list(Count) ++ [Prev],
    RevSeg = lists:reverse(Segment),
    NewAcc = RevSeg ++ Acc,
    process(T, H, 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_and_say(integer) :: String.t()
  def count_and_say(n) when n <= 0, do: ""
  def count_and_say(1), do: "1"
  def count_and_say(n) do
    Enum.reduce(2..n, "1", fn _, acc -> next_term(acc) end)
  end

  defp next_term(s) do
    s
    |> String.graphemes()
    |> encode()
  end

  defp encode([]), do: ""
  defp encode([h | t]), do: encode(t, h, 1, "")

  defp encode([], current_char, count, acc) do
    acc <> Integer.to_string(count) <> current_char
  end

  defp encode([h | t], current_char, count, acc) when h == current_char do
    encode(t, current_char, count + 1, acc)
  end

  defp encode([h | t], current_char, count, acc) do
    new_acc = acc <> Integer.to_string(count) <> current_char
    encode(t, h, 1, new_acc)
  end
end
```
