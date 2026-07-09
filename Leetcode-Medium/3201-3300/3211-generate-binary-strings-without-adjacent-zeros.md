# 3211. Generate Binary Strings Without Adjacent Zeros

## Cpp

```cpp
class Solution {
public:
    vector<string> validStrings(int n) {
        vector<string> ans;
        string cur;
        cur.reserve(n);
        function<void(int,char)> dfs = [&](int idx, char prev){
            if (idx == n) {
                ans.push_back(cur);
                return;
            }
            // try placing '1' always
            cur.push_back('1');
            dfs(idx + 1, '1');
            cur.pop_back();
            // try placing '0' only if previous is not '0'
            if (prev != '0') {
                cur.push_back('0');
                dfs(idx + 1, '0');
                cur.pop_back();
            }
        };
        // start recursion with no previous character
        dfs(0, '#'); // '#' denotes none
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> validStrings(int n) {
        List<String> result = new ArrayList<>();
        if (n <= 0) return result;
        StringBuilder sb = new StringBuilder();
        backtrack(n, sb, result);
        return result;
    }

    private void backtrack(int n, StringBuilder sb, List<String> result) {
        if (sb.length() == n) {
            result.add(sb.toString());
            return;
        }
        int len = sb.length();
        // Append '0' only if previous character is not '0'
        if (len == 0 || sb.charAt(len - 1) != '0') {
            sb.append('0');
            backtrack(n, sb, result);
            sb.deleteCharAt(sb.length() - 1);
        }
        // Append '1' always
        sb.append('1');
        backtrack(n, sb, result);
        sb.deleteCharAt(sb.length() - 1);
    }
}
```

## Python

```python
class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(curr):
            if len(curr) == n:
                res.append(''.join(curr))
                return
            if not curr or curr[-1] == '1':
                # can place 0
                curr.append('0')
                backtrack(curr)
                curr.pop()
                # can place 1
                curr.append('1')
                backtrack(curr)
                curr.pop()
            else:  # last char is '0', must place 1
                curr.append('1')
                backtrack(curr)
                curr.pop()
        backtrack([])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res: List[str] = []

        def dfs(pos: int, prev_zero: bool, cur: List[str]) -> None:
            if pos == n:
                res.append(''.join(cur))
                return
            # Append '1' always possible
            cur.append('1')
            dfs(pos + 1, False, cur)
            cur.pop()
            # Append '0' only if previous char wasn't '0'
            if not prev_zero:
                cur.append('0')
                dfs(pos + 1, True, cur)
                cur.pop()

        dfs(0, False, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
static void backtrack(int pos, int n, char *buf, char **res, int *idx) {
    if (pos == n) {
        res[*idx] = (char *)malloc((n + 1) * sizeof(char));
        memcpy(res[*idx], buf, n + 1);
        (*idx)++;
        return;
    }
    /* place '0' if previous character is not '0' */
    if (pos == 0 || buf[pos - 1] != '0') {
        buf[pos] = '0';
        backtrack(pos + 1, n, buf, res, idx);
    }
    /* always can place '1' */
    buf[pos] = '1';
    backtrack(pos + 1, n, buf, res, idx);
}

char** validStrings(int n, int* returnSize) {
    if (n <= 0) {
        *returnSize = 0;
        return NULL;
    }

    /* compute total number of valid strings: dp[i] = dp[i-1] + dp[i-2], dp[0]=1, dp[1]=2 */
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    dp[0] = 1;
    dp[1] = 2;
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    int total = dp[n];
    free(dp);

    char **result = (char **)malloc(total * sizeof(char *));
    char *buf = (char *)malloc((n + 1) * sizeof(char));
    buf[n] = '\0';

    int idx = 0;
    backtrack(0, n, buf, result, &idx);
    free(buf);

    *returnSize = total;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> ValidStrings(int n) {
        var result = new List<string>();
        if (n <= 0) return result;
        char[] cur = new char[n];
        void Dfs(int idx, char prev) {
            if (idx == n) {
                result.Add(new string(cur));
                return;
            }
            // Place '0' if not preceded by another '0'
            if (idx == 0 || prev != '0') {
                cur[idx] = '0';
                Dfs(idx + 1, '0');
            }
            // Always can place '1'
            cur[idx] = '1';
            Dfs(idx + 1, '1');
        }
        Dfs(0, '\0');
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var validStrings = function(n) {
    const result = [];
    const cur = new Array(n);
    
    const dfs = (idx, prevZero) => {
        if (idx === n) {
            result.push(cur.join(''));
            return;
        }
        // place '1'
        cur[idx] = '1';
        dfs(idx + 1, false);
        // place '0' only if previous char wasn't zero
        if (!prevZero) {
            cur[idx] = '0';
            dfs(idx + 1, true);
        }
    };
    
    dfs(0, false);
    return result;
};
```

## Typescript

```typescript
function validStrings(n: number): string[] {
    const result: string[] = [];
    const cur: string[] = new Array(n);
    
    function dfs(pos: number, lastZero: boolean) {
        if (pos === n) {
            result.push(cur.join(''));
            return;
        }
        // place '1' always allowed
        cur[pos] = '1';
        dfs(pos + 1, false);
        // place '0' only if previous char wasn't '0'
        if (!lastZero) {
            cur[pos] = '0';
            dfs(pos + 1, true);
        }
    }
    
    dfs(0, false);
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return String[]
     */
    function validStrings($n) {
        $result = [];
        $dfs = function(string $curr) use (&$dfs, &$result, $n) {
            if (strlen($curr) === $n) {
                $result[] = $curr;
                return;
            }
            // always can append '1'
            $dfs($curr . '1');
            // can append '0' only if previous char is not '0'
            if ($curr === '' || substr($curr, -1) !== '0') {
                $dfs($curr . '0');
            }
        };
        $dfs('');
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func validStrings(_ n: Int) -> [String] {
        var result = [String]()
        var current = [Character](repeating: "0", count: n)
        
        func backtrack(_ index: Int, _ prevZero: Bool) {
            if index == n {
                result.append(String(current))
                return
            }
            // place '1'
            current[index] = "1"
            backtrack(index + 1, false)
            // place '0' if previous character is not zero
            if !prevZero {
                current[index] = "0"
                backtrack(index + 1, true)
            }
        }
        
        backtrack(0, false)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validStrings(n: Int): List<String> {
        val result = mutableListOf<String>()
        val sb = StringBuilder()
        fun dfs(pos: Int, prevZero: Boolean) {
            if (pos == n) {
                result.add(sb.toString())
                return
            }
            // Append '0' if previous character is not zero
            if (!prevZero) {
                sb.append('0')
                dfs(pos + 1, true)
                sb.setLength(sb.length - 1)
            }
            // Append '1'
            sb.append('1')
            dfs(pos + 1, false)
            sb.setLength(sb.length - 1)
        }
        dfs(0, false)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> validStrings(int n) {
    List<String> result = [];
    void dfs(int idx, bool prevZero, String cur) {
      if (idx == n) {
        result.add(cur);
        return;
      }
      // Append '1' always
      dfs(idx + 1, false, cur + '1');
      // Append '0' only if previous char wasn't '0'
      if (!prevZero) {
        dfs(idx + 1, true, cur + '0');
      }
    }

    dfs(0, false, '');
    return result;
  }
}
```

## Golang

```go
func validStrings(n int) []string {
    var res []string
    if n <= 0 {
        return res
    }
    buf := make([]byte, n)
    var dfs func(idx int, prevZero bool)
    dfs = func(idx int, prevZero bool) {
        if idx == n {
            res = append(res, string(buf))
            return
        }
        // place '1'
        buf[idx] = '1'
        dfs(idx+1, false)
        // place '0' if previous wasn't zero
        if !prevZero {
            buf[idx] = '0'
            dfs(idx+1, true)
        }
    }
    dfs(0, false)
    return res
}
```

## Ruby

```ruby
def valid_strings(n)
  result = []
  backtrack = lambda do |pos, cur|
    if pos == n
      result << cur
    else
      backtrack.call(pos + 1, cur + '1')
      if pos == 0 || cur[-1] != '0'
        backtrack.call(pos + 1, cur + '0')
      end
    end
  end
  backtrack.call(0, "")
  result
end
```

## Scala

```scala
object Solution {
  def validStrings(n: Int): List[String] = {
    val result = scala.collection.mutable.ListBuffer.empty[String]
    if (n <= 0) return result.toList

    def backtrack(pos: Int, prevZero: Boolean, sb: StringBuilder): Unit = {
      if (pos == n) {
        result += sb.toString()
        return
      }
      // Append '1'
      sb.append('1')
      backtrack(pos + 1, false, sb)
      sb.setLength(sb.length - 1)

      // Append '0' only if previous char wasn't '0'
      if (!prevZero) {
        sb.append('0')
        backtrack(pos + 1, true, sb)
        sb.setLength(sb.length - 1)
      }
    }

    backtrack(0, false, new StringBuilder())
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut res = Vec::new();
        let mut cur = String::with_capacity(n);
        fn dfs(pos: usize, n: usize, last_zero: bool, cur: &mut String, res: &mut Vec<String>) {
            if pos == n {
                res.push(cur.clone());
                return;
            }
            // Append '1'
            cur.push('1');
            dfs(pos + 1, n, false, cur, res);
            cur.pop();
            // Append '0' only if previous char wasn't '0'
            if !last_zero {
                cur.push('0');
                dfs(pos + 1, n, true, cur, res);
                cur.pop();
            }
        }
        dfs(0, n, false, &mut cur, &mut res);
        res
    }
}
```

## Racket

```racket
#lang racket

(define/contract (valid-strings n)
  (-> exact-integer? (listof string?))
  (letrec ((build
            (lambda (k prev)
              (if (= k 0)
                  (list "")
                  (if (char=? prev #\0)
                      (map (lambda (s) (string-append "1" s))
                           (build (- k 1) #\1))
                      (let ((with0 (map (lambda (s) (string-append "0" s))
                                        (build (- k 1) #\0)))
                            (with1 (map (lambda (s) (string-append "1" s))
                                        (build (- k 1) #\1))))
                        (append with0 with1)))))))
    (build n #\1)))
```

## Erlang

```erlang
-spec valid_strings(N :: integer()) -> [unicode:unicode_binary()].
valid_strings(N) when N >= 0 ->
    generate(N, [], []).

generate(0, RevPrefix, Acc) ->
    Bin = list_to_binary(lists:reverse(RevPrefix)),
    [Bin | Acc];
generate(Remaining, RevPrefix, Acc) ->
    case RevPrefix of
        [] ->
            Acc1 = generate(Remaining - 1, [$0], Acc),
            generate(Remaining - 1, [$1], Acc1);
        [Prev | _] ->
            if Prev == $0 ->
                    generate(Remaining - 1, [$1 | RevPrefix], Acc);
               true ->
                    Acc1 = generate(Remaining - 1, [$0 | RevPrefix], Acc),
                    generate(Remaining - 1, [$1 | RevPrefix], Acc1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_strings(n :: integer) :: [String.t()]
  def valid_strings(n) when is_integer(n) and n >= 0 do
    dfs(0, n, nil, "", [])
    |> Enum.reverse()
  end

  defp dfs(pos, n, _prev, cur, acc) when pos == n do
    [cur | acc]
  end

  defp dfs(pos, n, prev, cur, acc) do
    # Append '1' (always allowed)
    acc = dfs(pos + 1, n, ?1, cur <> "1", acc)

    # Append '0' only if previous character is not '0'
    if prev != ?0 do
      dfs(pos + 1, n, ?0, cur <> "0", acc)
    else
      acc
    end
  end
end
```
