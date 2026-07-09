# 0402. Remove K Digits

## Cpp

```cpp
class Solution {
public:
    string removeKdigits(string num, int k) {
        string stk;
        for (char c : num) {
            while (!stk.empty() && k > 0 && stk.back() > c) {
                stk.pop_back();
                --k;
            }
            stk.push_back(c);
        }
        while (k > 0 && !stk.empty()) {
            stk.pop_back();
            --k;
        }
        int i = 0;
        while (i < (int)stk.size() && stk[i] == '0') ++i;
        string ans = stk.substr(i);
        return ans.empty() ? "0" : ans;
    }
};
```

## Java

```java
class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        if (k >= n) return "0";
        char[] stack = new char[n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            char c = num.charAt(i);
            while (top > 0 && k > 0 && stack[top - 1] > c) {
                top--;
                k--;
            }
            stack[top++] = c;
        }
        top -= k; // remove remaining digits from the end if any
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < top && stack[i] == '0') i++; // skip leading zeros
        for (; i < top; i++) {
            sb.append(stack[i]);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # If still need to remove digits, remove from the end
        if k:
            stack = stack[:-k]
        # Strip leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
```

## Python3

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:-k]
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* removeKdigits(char* num, int k) {
    int n = strlen(num);
    char *stack = (char*)malloc(n);
    int top = 0;

    for (int i = 0; i < n; ++i) {
        char c = num[i];
        while (top > 0 && k > 0 && stack[top - 1] > c) {
            --top;
            --k;
        }
        stack[top++] = c;
    }

    if (k > 0) {
        top -= k;
        if (top < 0) top = 0;
    }

    int start = 0;
    while (start < top && stack[start] == '0') {
        ++start;
    }

    int newLen = top - start;
    char *res;
    if (newLen <= 0) {
        res = (char*)malloc(2);
        res[0] = '0';
        res[1] = '\0';
    } else {
        res = (char*)malloc(newLen + 1);
        memcpy(res, stack + start, newLen);
        res[newLen] = '\0';
    }

    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RemoveKdigits(string num, int k)
    {
        var stack = new System.Text.StringBuilder();

        foreach (char c in num)
        {
            while (k > 0 && stack.Length > 0 && stack[stack.Length - 1] > c)
            {
                stack.Length--;
                k--;
            }
            stack.Append(c);
        }

        while (k > 0 && stack.Length > 0)
        {
            stack.Length--;
            k--;
        }

        int i = 0;
        while (i < stack.Length && stack[i] == '0')
            i++;

        if (i == stack.Length)
            return "0";

        return stack.ToString(i, stack.Length - i);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    const stack = [];
    for (const ch of num) {
        while (k > 0 && stack.length && stack[stack.length - 1] > ch) {
            stack.pop();
            k--;
        }
        stack.push(ch);
    }
    // If deletions remain, remove from the end
    while (k > 0) {
        stack.pop();
        k--;
    }
    let result = stack.join('').replace(/^0+/, '');
    return result === '' ? '0' : result;
};
```

## Typescript

```typescript
function removeKdigits(num: string, k: number): string {
    const stack: string[] = [];
    for (const ch of num) {
        while (k > 0 && stack.length && stack[stack.length - 1] > ch) {
            stack.pop();
            k--;
        }
        stack.push(ch);
    }
    while (k > 0 && stack.length) {
        stack.pop();
        k--;
    }
    let result = stack.join('').replace(/^0+/, '');
    return result === '' ? '0' : result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function removeKdigits($num, $k) {
        $len = strlen($num);
        if ($k >= $len) return "0";
        $stack = [];
        for ($i = 0; $i < $len; $i++) {
            $c = $num[$i];
            while ($k > 0 && !empty($stack) && end($stack) > $c) {
                array_pop($stack);
                $k--;
            }
            $stack[] = $c;
        }
        while ($k > 0) {
            array_pop($stack);
            $k--;
        }
        $result = implode('', $stack);
        $result = ltrim($result, '0');
        return $result === '' ? "0" : $result;
    }
}
```

## Swift

```swift
class Solution {
    func removeKdigits(_ num: String, _ k: Int) -> String {
        var stack = [Character]()
        var remaining = k
        for ch in num {
            while remaining > 0 && !stack.isEmpty && stack.last! > ch {
                stack.removeLast()
                remaining -= 1
            }
            stack.append(ch)
        }
        if remaining > 0 {
            stack.removeLast(remaining)
        }
        let result = String(stack)
        let trimmed = result.drop(while: { $0 == "0" })
        return trimmed.isEmpty ? "0" : String(trimmed)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeKdigits(num: String, k: Int): String {
        var remain = k
        val stack = CharArray(num.length)
        var top = 0

        for (c in num) {
            while (remain > 0 && top > 0 && stack[top - 1] > c) {
                top--
                remain--
            }
            stack[top++] = c
        }

        // If still need to remove digits, truncate from the end
        top -= remain

        var idx = 0
        while (idx < top && stack[idx] == '0') idx++

        val sb = StringBuilder()
        for (i in idx until top) {
            sb.append(stack[i])
        }

        return if (sb.isEmpty()) "0" else sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String removeKdigits(String num, int k) {
    List<String> stack = [];
    for (int i = 0; i < num.length; i++) {
      String c = num[i];
      while (k > 0 && stack.isNotEmpty && stack.last.compareTo(c) > 0) {
        stack.removeLast();
        k--;
      }
      stack.add(c);
    }
    while (k > 0 && stack.isNotEmpty) {
      stack.removeLast();
      k--;
    }
    String result = stack.join('');
    int idx = 0;
    while (idx < result.length && result[idx] == '0') {
      idx++;
    }
    result = result.substring(idx);
    return result.isEmpty ? "0" : result;
  }
}
```

## Golang

```go
func removeKdigits(num string, k int) string {
	n := len(num)
	if k >= n {
		return "0"
	}
	stack := make([]byte, 0, n)
	for i := 0; i < n; i++ {
		c := num[i]
		for k > 0 && len(stack) > 0 && stack[len(stack)-1] > c {
			stack = stack[:len(stack)-1]
			k--
		}
		stack = append(stack, c)
	}
	if k > 0 {
		stack = stack[:len(stack)-k]
	}
	idx := 0
	for idx < len(stack) && stack[idx] == '0' {
		idx++
	}
	res := string(stack[idx:])
	if res == "" {
		return "0"
	}
	return res
}
```

## Ruby

```ruby
def remove_kdigits(num, k)
  stack = []
  num.each_char do |c|
    while k > 0 && !stack.empty? && stack[-1] > c
      stack.pop
      k -= 1
    end
    stack << c
  end
  while k > 0
    stack.pop
    k -= 1
  end
  result = stack.join.sub(/^0+/, '')
  result.empty? ? "0" : result
end
```

## Scala

```scala
object Solution {
  def removeKdigits(num: String, k: Int): String = {
    var toRemove = k
    val stack = new java.util.ArrayDeque[Char]()
    for (c <- num) {
      while (toRemove > 0 && !stack.isEmpty && stack.peekLast() > c) {
        stack.pollLast()
        toRemove -= 1
      }
      stack.addLast(c)
    }
    while (toRemove > 0 && !stack.isEmpty) {
      stack.pollLast()
      toRemove -= 1
    }

    val sb = new StringBuilder()
    var leadingZero = true
    import scala.jdk.CollectionConverters._
    for (c <- stack.asScala) {
      if (leadingZero && c == '0') {
        // skip leading zeros
      } else {
        leadingZero = false
        sb.append(c)
      }
    }

    val result = sb.toString()
    if (result.isEmpty) "0" else result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let mut k = k as usize;
        let mut stack: Vec<char> = Vec::with_capacity(num.len());
        for ch in num.chars() {
            while k > 0 && !stack.is_empty() && *stack.last().unwrap() > ch {
                stack.pop();
                k -= 1;
            }
            stack.push(ch);
        }
        while k > 0 && !stack.is_empty() {
            stack.pop();
            k -= 1;
        }
        let mut result = String::with_capacity(stack.len());
        let mut leading = true;
        for &c in &stack {
            if leading && c == '0' {
                continue;
            }
            leading = false;
            result.push(c);
        }
        if result.is_empty() { "0".to_string() } else { result }
    }
}
```

## Racket

```racket
(define/contract (remove-kdigits num k)
  (-> string? exact-integer? string?)
  (let* ((chars (string->list num))
         (remaining k)
         (stack '()))
    (for ([c chars])
      (let loop ()
        (when (and (> remaining 0) (not (null? stack)) (char>? (car stack) c))
          (set! stack (cdr stack))
          (set! remaining (- remaining 1))
          (loop)))
      (set! stack (cons c stack)))
    (when (> remaining 0)
      (set! stack (list-tail stack remaining))) ; remove from the rightmost side
    (let ((result (list->string (reverse stack))))
      (let loop ((i 0) (len (string-length result)))
        (cond [(= i len) "0"]
              [(char=? (string-ref result i) #\0) (loop (+ i 1) len)]
              [else (substring result i)])))))
```

## Erlang

```erlang
-spec remove_kdigits(Num :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
remove_kdigits(Num, K) ->
    Digits = binary_to_list(Num),
    {Stack0, RemK} = process(Digits, K, []),
    Stack1 = case RemK of
                0 -> Stack0;
                _ -> lists:nthtail(RemK, Stack0)
            end,
    ResultList = lists:reverse(Stack1),
    Trimmed = trim_zeros(ResultList),
    case Trimmed of
        [] -> <<"0">>;
        _ -> list_to_binary(Trimmed)
    end.

process([], K, Stack) ->
    {Stack, K};
process([D|Rest], K, Stack) when K > 0, Stack =/= [], hd(Stack) > D ->
    process([D|Rest], K-1, tl(Stack));
process([D|Rest], K, Stack) ->
    process(Rest, K, [D|Stack]).

trim_zeros([]) -> [];
trim_zeros([$0 | Rest]) -> trim_zeros(Rest);
trim_zeros(L) -> L.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_kdigits(num :: String.t(), k :: integer()) :: String.t()
  def remove_kdigits(num, k) do
    {stack, remaining_k} =
      num
      |> String.graphemes()
      |> Enum.reduce({[], k}, fn digit, {stk, kk} ->
        {new_stk, new_kk} = pop_until(stk, kk, digit)
        {[digit | new_stk], new_kk}
      end)

    final_stack =
      if remaining_k > 0 do
        Enum.drop(stack, remaining_k)
      else
        stack
      end

    result = final_stack |> Enum.reverse() |> Enum.join()
    trimmed = String.trim_leading(result, "0")
    if trimmed == "" do "0" else trimmed end
  end

  defp pop_until([], kk, _digit), do: {[], kk}
  defp pop_until([h | t] = stk, kk, digit) when kk > 0 and h > digit do
    pop_until(t, kk - 1, digit)
  end
  defp pop_until(stk, kk, _digit), do: {stk, kk}
end
```
