# 0022. Generate Parentheses

## Cpp

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur;
        dfs(res, cur, n, 0, 0);
        return res;
    }
private:
    void dfs(vector<string>& res, string& cur, int n, int open, int close) {
        if (cur.size() == n * 2) {
            res.push_back(cur);
            return;
        }
        if (open < n) {
            cur.push_back('(');
            dfs(res, cur, n, open + 1, close);
            cur.pop_back();
        }
        if (close < open) {
            cur.push_back(')');
            dfs(res, cur, n, open, close + 1);
            cur.pop_back();
        }
    }
};
```

## Java

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        if (n <= 0) return res;
        backtrack(res, new StringBuilder(), n, 0, 0);
        return res;
    }
    
    private void backtrack(List<String> res, StringBuilder cur, int max, int open, int close) {
        if (cur.length() == max * 2) {
            res.add(cur.toString());
            return;
        }
        if (open < max) {
            cur.append('(');
            backtrack(res, cur, max, open + 1, close);
            cur.deleteCharAt(cur.length() - 1);
        }
        if (close < open) {
            cur.append(')');
            backtrack(res, cur, max, open, close + 1);
            cur.deleteCharAt(cur.length() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack('', 0, 0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        def backtrack(cur: str, left: int, right: int):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if left < n:
                backtrack(cur + '(', left + 1, right)
            if right < left:
                backtrack(cur + ')', left, right + 1)
        backtrack('', 0, 0)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Helper to compute Catalan numbers up to n */
static int catalan(int n) {
    long long dp[9] = {0};
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
        long long sum = 0;
        for (int j = 0; j < i; ++j) {
            sum += dp[j] * dp[i - 1 - j];
        }
        dp[i] = sum;
    }
    return (int)dp[n];
}

/* Backtracking function */
static void backtrack(char *cur, int pos, int open, int close,
                      int n, char **res, int *idx) {
    if (pos == 2 * n) {
        cur[pos] = '\0';
        res[*idx] = (char *)malloc((2 * n + 1) * sizeof(char));
        memcpy(res[*idx], cur, 2 * n + 1);
        (*idx)++;
        return;
    }
    if (open < n) {
        cur[pos] = '(';
        backtrack(cur, pos + 1, open + 1, close, n, res, idx);
    }
    if (close < open) {
        cur[pos] = ')';
        backtrack(cur, pos + 1, open, close + 1, n, res, idx);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** generateParenthesis(int n, int* returnSize) {
    if (n <= 0) {
        *returnSize = 0;
        return NULL;
    }

    int cnt = catalan(n);
    char **ans = (char **)malloc(cnt * sizeof(char *));
    char *cur = (char *)malloc((2 * n + 1) * sizeof(char));

    int idx = 0;
    backtrack(cur, 0, 0, 0, n, ans, &idx);

    free(cur);
    *returnSize = cnt;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> GenerateParenthesis(int n)
    {
        var result = new List<string>();
        Backtrack(result, "", 0, 0, n);
        return result;
    }

    private void Backtrack(List<string> result, string current, int open, int close, int max)
    {
        if (current.Length == max * 2)
        {
            result.Add(current);
            return;
        }
        if (open < max)
        {
            Backtrack(result, current + "(", open + 1, close, max);
        }
        if (close < open)
        {
            Backtrack(result, current + ")", open, close + 1, max);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];
    const backtrack = (current, open, close) => {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        if (open < n) {
            backtrack(current + '(', open + 1, close);
        }
        if (close < open) {
            backtrack(current + ')', open, close + 1);
        }
    };
    backtrack('', 0, 0);
    return result;
};
```

## Typescript

```typescript
function generateParenthesis(n: number): string[] {
    const result: string[] = [];
    const backtrack = (current: string, open: number, close: number) => {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        if (open < n) {
            backtrack(current + '(', open + 1, close);
        }
        if (close < open) {
            backtrack(current + ')', open, close + 1);
        }
    };
    backtrack('', 0, 0);
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
    function generateParenthesis($n) {
        $result = [];
        if ($n <= 0) {
            return $result;
        }
        $backtrack = function(string $current, int $open, int $close) use (&$backtrack, &$result, $n) {
            if (strlen($current) === $n * 2) {
                $result[] = $current;
                return;
            }
            if ($open < $n) {
                $backtrack($current . '(', $open + 1, $close);
            }
            if ($close < $open) {
                $backtrack($current . ')', $open, $close + 1);
            }
        };
        $backtrack('', 0, 0);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var result = [String]()
        var current = ""
        
        func backtrack(_ open: Int, _ close: Int) {
            if current.count == 2 * n {
                result.append(current)
                return
            }
            if open < n {
                current.append("(")
                backtrack(open + 1, close)
                current.removeLast()
            }
            if close < open {
                current.append(")")
                backtrack(open, close + 1)
                current.removeLast()
            }
        }
        
        backtrack(0, 0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val result = mutableListOf<String>()
        if (n <= 0) return result
        fun backtrack(sb: StringBuilder, open: Int, close: Int) {
            if (sb.length == n * 2) {
                result.add(sb.toString())
                return
            }
            if (open < n) {
                sb.append('(')
                backtrack(sb, open + 1, close)
                sb.deleteCharAt(sb.lastIndex)
            }
            if (close < open) {
                sb.append(')')
                backtrack(sb, open, close + 1)
                sb.deleteCharAt(sb.lastIndex)
            }
        }
        backtrack(StringBuilder(), 0, 0)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> generateParenthesis(int n) {
    List<String> result = [];
    void backtrack(String current, int open, int close) {
      if (current.length == n * 2) {
        result.add(current);
        return;
      }
      if (open < n) {
        backtrack('$current(', open + 1, close);
      }
      if (close < open) {
        backtrack('$current)', open, close + 1);
      }
    }

    if (n > 0) {
      backtrack('', 0, 0);
    }
    return result;
  }
}
```

## Golang

```go
func generateParenthesis(n int) []string {
	var result []string
	var backtrack func(string, int, int)
	backtrack = func(current string, open, close int) {
		if len(current) == 2*n {
			result = append(result, current)
			return
		}
		if open < n {
			backtrack(current+"(", open+1, close)
		}
		if close < open {
			backtrack(current+")", open, close+1)
		}
	}
	backtrack("", 0, 0)
	return result
}
```

## Ruby

```ruby
def generate_parenthesis(n)
  return [] if n <= 0
  res = []
  backtrack = nil
  backtrack = ->(cur, open_cnt, close_cnt) do
    if cur.length == 2 * n
      res << cur
      next
    end
    backtrack.call(cur + '(', open_cnt + 1, close_cnt) if open_cnt < n
    backtrack.call(cur + ')', open_cnt, close_cnt + 1) if close_cnt < open_cnt
  end
  backtrack.call('', 0, 0)
  res
end
```

## Scala

```scala
object Solution {
    def generateParenthesis(n: Int): List[String] = {
        if (n == 0) return List("")
        val result = scala.collection.mutable.ListBuffer[String]()
        def backtrack(sb: StringBuilder, open: Int, close: Int): Unit = {
            if (sb.length == 2 * n) {
                result += sb.toString()
                return
            }
            if (open < n) {
                sb.append('(')
                backtrack(sb, open + 1, close)
                sb.deleteCharAt(sb.length - 1)
            }
            if (close < open) {
                sb.append(')')
                backtrack(sb, open, close + 1)
                sb.deleteCharAt(sb.length - 1)
            }
        }
        backtrack(new StringBuilder(), 0, 0)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn backtrack(res: &mut Vec<String>, cur: &mut String, open: i32, close: i32, max: i32) {
            if cur.len() == (max as usize) * 2 {
                res.push(cur.clone());
                return;
            }
            if open < max {
                cur.push('(');
                backtrack(res, cur, open + 1, close, max);
                cur.pop();
            }
            if close < open {
                cur.push(')');
                backtrack(res, cur, open, close + 1, max);
                cur.pop();
            }
        }

        let mut res = Vec::new();
        if n > 0 {
            let mut cur = String::new();
            backtrack(&mut res, &mut cur, 0, 0, n);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (generate-parenthesis n)
  (-> exact-integer? (listof string?))
  (let recur ((open n) (close n) (prefix ""))
    (cond [(zero? open)
           (list (string-append prefix (make-string close #\))))] ; only ')' left
          [else
           (let* ([add-open (recur (- open 1) close (string-append prefix "("))]
                  [add-close (if (< open close)
                                (recur open (- close 1) (string-append prefix ")"))
                                '())])
             (append add-open add-close))])))
```

## Erlang

```erlang
-module(solution).
-export([generate_parenthesis/1]).

-spec generate_parenthesis(N :: integer()) -> [unicode:unicode_binary()].
generate_parenthesis(N) when is_integer(N), N >= 0 ->
    gen(N, 0, 0, <<>>).

gen(N, Open, Close, Prefix) when Open == N, Close == N ->
    [Prefix];
gen(N, Open, Close, Prefix) ->
    L1 = case Open < N of
            true -> gen(N, Open + 1, Close, <<Prefix/binary, $(>>);
            false -> []
         end,
    L2 = case Close < Open of
            true -> gen(N, Open, Close + 1, <<Prefix/binary, $>>>);
            false -> []
         end,
    L1 ++ L2.
```

## Elixir

```elixir
defmodule Solution do
  @spec generate_parenthesis(n :: integer) :: [String.t()]
  def generate_parenthesis(n) when is_integer(n) and n >= 0 do
    backtrack("", n, n)
  end

  defp backtrack(curr, 0, 0), do: [curr]

  defp backtrack(curr, open, close) do
    opens = if open > 0, do: backtrack(curr <> "(", open - 1, close), else: []
    closes = if close > open, do: backtrack(curr <> ")", open, close - 1), else: []
    opens ++ closes
  end
end
```
