# 0131. Palindrome Partitioning

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.size();
        vector<vector<bool>> isPal(n, vector<bool>(n, false));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j] && (j - i < 2 || isPal[i + 1][j - 1])) {
                    isPal[i][j] = true;
                }
            }
        }
        vector<vector<string>> res;
        vector<string> cur;
        function<void(int)> dfs = [&](int start) {
            if (start == n) {
                res.push_back(cur);
                return;
            }
            for (int end = start; end < n; ++end) {
                if (isPal[start][end]) {
                    cur.emplace_back(s.substr(start, end - start + 1));
                    dfs(end + 1);
                    cur.pop_back();
                }
            }
        };
        dfs(0);
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<List<String>> partition(String s) {
        int n = s.length();
        boolean[][] isPal = new boolean[n][n];
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || isPal[i + 1][j - 1])) {
                    isPal[i][j] = true;
                }
            }
        }
        List<List<String>> result = new ArrayList<>();
        backtrack(0, s, isPal, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, String s, boolean[][] isPal,
                           List<String> path, List<List<String>> result) {
        if (start == s.length()) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int end = start; end < s.length(); ++end) {
            if (isPal[start][end]) {
                path.add(s.substring(start, end + 1));
                backtrack(end + 1, s, isPal, path, result);
                path.remove(path.size() - 1);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        # precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        res = []
        path = []

        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # Precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        res: List[List[str]] = []
        path: List[str] = []

        def backtrack(start: int) -> None:
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if pal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static char ***g_res;
static int *g_colSizes;
static int g_resCount = 0;
static int g_cap = 0;

static bool g_isPal[16][16];
static int g_pathStart[16];
static int g_pathLen[16];
static int g_depth = 0;
static const char *g_s;
static int g_n;

/* forward declaration */
static void dfs(int pos);

static void add_partition(void) {
    if (g_resCount == g_cap) {
        int newCap = g_cap == 0 ? 128 : g_cap * 2;
        g_res = realloc(g_res, newCap * sizeof(char **));
        g_colSizes = realloc(g_colSizes, newCap * sizeof(int));
        g_cap = newCap;
    }
    char **part = (char **)malloc(g_depth * sizeof(char *));
    for (int i = 0; i < g_depth; ++i) {
        int start = g_pathStart[i];
        int len = g_pathLen[i];
        char *sub = (char *)malloc(len + 1);
        memcpy(sub, g_s + start, len);
        sub[len] = '\0';
        part[i] = sub;
    }
    g_res[g_resCount] = part;
    g_colSizes[g_resCount] = g_depth;
    ++g_resCount;
}

static void dfs(int pos) {
    if (pos == g_n) {
        add_partition();
        return;
    }
    for (int end = pos; end < g_n; ++end) {
        if (g_isPal[pos][end]) {
            g_pathStart[g_depth] = pos;
            g_pathLen[g_depth] = end - pos + 1;
            ++g_depth;
            dfs(end + 1);
            --g_depth;
        }
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** partition(char* s, int* returnSize, int** returnColumnSizes) {
    g_s = s;
    g_n = (int)strlen(s);
    /* compute palindrome table */
    for (int i = g_n - 1; i >= 0; --i) {
        for (int j = i; j < g_n; ++j) {
            if (s[i] == s[j] && (j - i < 2 || g_isPal[i + 1][j - 1])) {
                g_isPal[i][j] = true;
            } else {
                g_isPal[i][j] = false;
            }
        }
    }

    g_res = NULL;
    g_colSizes = NULL;
    g_resCount = 0;
    g_cap = 0;
    g_depth = 0;

    dfs(0);

    *returnSize = g_resCount;
    *returnColumnSizes = g_colSizes;
    return g_res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> Partition(string s) {
        int n = s.Length;
        bool[,] isPal = new bool[n, n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s[i] == s[j] && (j - i < 2 || isPal[i + 1, j - 1])) {
                    isPal[i, j] = true;
                }
            }
        }

        var result = new List<IList<string>>();
        var path = new List<string>();
        Backtrack(0);
        return result;

        void Backtrack(int start) {
            if (start == n) {
                result.Add(new List<string>(path));
                return;
            }
            for (int end = start; end < n; end++) {
                if (isPal[start, end]) {
                    path.Add(s.Substring(start, end - start + 1));
                    Backtrack(end + 1);
                    path.RemoveAt(path.Count - 1);
                }
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const n = s.length;
    const dp = Array.from({ length: n }, () => Array(n).fill(false));
    
    // Precompute palindrome substrings
    for (let i = n - 1; i >= 0; i--) {
        for (let j = i; j < n; j++) {
            if (s[i] === s[j] && (j - i < 2 || dp[i + 1][j - 1])) {
                dp[i][j] = true;
            }
        }
    }
    
    const res = [];
    const path = [];
    
    function backtrack(start) {
        if (start === n) {
            res.push([...path]);
            return;
        }
        for (let end = start; end < n; end++) {
            if (dp[start][end]) {
                path.push(s.slice(start, end + 1));
                backtrack(end + 1);
                path.pop();
            }
        }
    }
    
    backtrack(0);
    return res;
};
```

## Typescript

```typescript
function partition(s: string): string[][] {
    const n = s.length;
    const isPal: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = n - 1; i >= 0; --i) {
        for (let j = i; j < n; ++j) {
            if (s[i] === s[j] && (j - i < 2 || isPal[i + 1][j - 1])) {
                isPal[i][j] = true;
            }
        }
    }
    const result: string[][] = [];
    const path: string[] = [];

    function dfs(start: number): void {
        if (start === n) {
            result.push([...path]);
            return;
        }
        for (let end = start; end < n; ++end) {
            if (isPal[start][end]) {
                path.push(s.substring(start, end + 1));
                dfs(end + 1);
                path.pop();
            }
        }
    }

    dfs(0);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[][]
     */
    function partition($s) {
        $n = strlen($s);
        // Precompute palindrome table
        $isPal = array_fill(0, $n, array_fill(0, $n, false));
        for ($i = $n - 1; $i >= 0; --$i) {
            for ($j = $i; $j < $n; ++$j) {
                if ($s[$i] === $s[$j] && ($j - $i < 2 || $isPal[$i + 1][$j - 1])) {
                    $isPal[$i][$j] = true;
                }
            }
        }

        $res = [];
        $path = [];

        $this->dfs($s, 0, $path, $res, $isPal);
        return $res;
    }

    private function dfs($s, $start, &$path, &$res, $isPal) {
        $n = strlen($s);
        if ($start == $n) {
            $res[] = $path;
            return;
        }
        for ($end = $start; $end < $n; ++$end) {
            if ($isPal[$start][$end]) {
                $substr = substr($s, $start, $end - $start + 1);
                $path[] = $substr;
                $this->dfs($s, $end + 1, $path, $res, $isPal);
                array_pop($path);
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func partition(_ s: String) -> [[String]] {
        let chars = Array(s)
        let n = chars.count
        var isPal = Array(repeating: Array(repeating: false, count: n), count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in i..<n {
                if chars[i] == chars[j] && (j - i <= 2 || isPal[i + 1][j - 1]) {
                    isPal[i][j] = true
                }
            }
        }
        var result = [[String]]()
        var path = [String]()
        func dfs(_ start: Int) {
            if start == n {
                result.append(path)
                return
            }
            for end in start..<n {
                if isPal[start][end] {
                    let substr = String(chars[start...end])
                    path.append(substr)
                    dfs(end + 1)
                    path.removeLast()
                }
            }
        }
        dfs(0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partition(s: String): List<List<String>> {
        val n = s.length
        val dp = Array(n) { BooleanArray(n) }
        for (i in n - 1 downTo 0) {
            for (j in i until n) {
                if (s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true
                }
            }
        }
        val result = mutableListOf<List<String>>()
        val path = mutableListOf<String>()
        fun dfs(start: Int) {
            if (start == n) {
                result.add(ArrayList(path))
                return
            }
            for (end in start until n) {
                if (dp[start][end]) {
                    path.add(s.substring(start, end + 1))
                    dfs(end + 1)
                    path.removeAt(path.size - 1)
                }
            }
        }
        dfs(0)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> partition(String s) {
    int n = s.length;
    // Precompute palindrome table
    List<List<bool>> isPal = List.generate(n, (_) => List.filled(n, false));
    for (int i = 0; i < n; ++i) {
      isPal[i][i] = true;
    }
    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        if (s[i] == s[j]) {
          if (len == 2) {
            isPal[i][j] = true;
          } else {
            isPal[i][j] = isPal[i + 1][j - 1];
          }
        }
      }
    }

    List<List<String>> result = [];
    List<String> path = [];

    void dfs(int start) {
      if (start == n) {
        result.add(List.from(path));
        return;
      }
      for (int end = start; end < n; ++end) {
        if (isPal[start][end]) {
          path.add(s.substring(start, end + 1));
          dfs(end + 1);
          path.removeLast();
        }
      }
    }

    dfs(0);
    return result;
  }
}
```

## Golang

```go
func partition(s string) [][]string {
	n := len(s)
	if n == 0 {
		return [][]string{}
	}
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j-i < 2 || dp[i+1][j-1]) {
				dp[i][j] = true
			}
		}
	}
	var res [][]string
	var path []string
	var dfs func(int)
	dfs = func(start int) {
		if start == n {
			tmp := make([]string, len(path))
			copy(tmp, path)
			res = append(res, tmp)
			return
		}
		for end := start; end < n; end++ {
			if dp[start][end] {
				path = append(path, s[start:end+1])
				dfs(end + 1)
				path = path[:len(path)-1]
			}
		}
	}
	dfs(0)
	return res
}
```

## Ruby

```ruby
def partition(s)
  n = s.length
  dp = Array.new(n) { Array.new(n, false) }

  (n - 1).downto(0) do |i|
    (i...n).each do |j|
      if s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1])
        dp[i][j] = true
      end
    end
  end

  res = []
  path = []

  dfs = nil
  dfs = lambda do |start|
    if start == n
      res << path.clone
      return
    end
    (start...n).each do |end_idx|
      if dp[start][end_idx]
        path << s[start..end_idx]
        dfs.call(end_idx + 1)
        path.pop
      end
    end
  end

  dfs.call(0)
  res
end
```

## Scala

```scala
object Solution {
    def partition(s: String): List[List[String]] = {
        val n = s.length
        val isPal = Array.ofDim[Boolean](n, n)
        for (i <- (0 until n).reverse) {
            for (j <- i until n) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || isPal(i + 1)(j - 1))) {
                    isPal(i)(j) = true
                }
            }
        }

        val res = collection.mutable.ListBuffer[List[String]]()

        def dfs(start: Int, path: List[String]): Unit = {
            if (start == n) {
                res += path
                return
            }
            var end = start
            while (end < n) {
                if (isPal(start)(end)) {
                    dfs(end + 1, path :+ s.substring(start, end + 1))
                }
                end += 1
            }
        }

        dfs(0, List())
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let n = s.len();
        let bytes = s.as_bytes();

        // dp[i][j] == true if s[i..=j] is a palindrome
        let mut dp = vec![vec![false; n]; n];
        for i in (0..n).rev() {
            for j in i..n {
                if bytes[i] == bytes[j] && (j - i < 2 || dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                }
            }
        }

        let mut res: Vec<Vec<String>> = Vec::new();
        let mut path: Vec<String> = Vec::new();

        fn backtrack(
            start: usize,
            s: &str,
            n: usize,
            dp: &Vec<Vec<bool>>,
            path: &mut Vec<String>,
            res: &mut Vec<Vec<String>>,
        ) {
            if start == n {
                res.push(path.clone());
                return;
            }
            for end in start..n {
                if dp[start][end] {
                    path.push(s[start..=end].to_string());
                    backtrack(end + 1, s, n, dp, path, res);
                    path.pop();
                }
            }
        }

        backtrack(0, &s, n, &dp, &mut path, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (partition s)
  (-> string? (listof (listof string?)))
  (let* ((n (string-length s))
         (is-pal?
          (lambda (i j) ; i inclusive, j exclusive
            (let loop ((l i) (r (- j 1)))
              (or (> l r)
                  (and (char=? (string-ref s l) (string-ref s r))
                       (loop (+ l 1) (- r 1))))))))
    (let rec ((i 0))
      (if (= i n)
          (list '())
          (apply append
                 (for/list ([j (in-range (+ i 1) (+ n 1))]
                            #:when (is-pal? i j))
                   (let ((sub (substring s i j)))
                     (map (lambda (rest) (cons sub rest))
                          (rec j)))))))))
```

## Erlang

```erlang
-module(solution).
-export([partition/1]).

-spec partition(S :: unicode:unicode_binary()) -> [[unicode:unicode_binary()]].
partition(S) ->
    Len = byte_size(S),
    Result = dfs(S, Len, 0, [], []),
    lists:reverse(Result).

dfs(_Bin, Len, Pos, Path, Acc) when Pos == Len ->
    [lists:reverse(Path) | Acc];
dfs(Bin, Len, Pos, Path, Acc) ->
    explore(Bin, Len, Pos, Path, Acc, Pos + 1).

explore(_Bin, Len, _Pos, _Path, Acc, End) when End > Len ->
    Acc;
explore(Bin, Len, Pos, Path, Acc, End) ->
    SubLen = End - Pos,
    case is_palindrome(Bin, Pos, SubLen) of
        true ->
            SubBin = binary:part(Bin, {Pos, SubLen}),
            NewPath = [SubBin | Path],
            Acc1 = dfs(Bin, Len, End, NewPath, Acc),
            explore(Bin, Len, Pos, Path, Acc1, End + 1);
        false ->
            explore(Bin, Len, Pos, Path, Acc, End + 1)
    end.

is_palindrome(Bin, Start, Length) ->
    Sub = binary:part(Bin, {Start, Length}),
    List = binary_to_list(Sub),
    List == lists:reverse(List).
```

## Elixir

```elixir
defmodule Solution do
  @spec partition(s :: String.t()) :: [[String.t()]]
  def partition(s) do
    n = String.length(s)
    dfs(0, [], s, n)
  end

  defp dfs(start, path, _s, n) when start == n do
    [Enum.reverse(path)]
  end

  defp dfs(start, path, s, n) do
    Enum.reduce(start..(n - 1), [], fn i, acc ->
      len = i - start + 1
      substr = String.slice(s, start, len)

      if palindrome?(substr) do
        dfs(i + 1, [substr | path], s, n) ++ acc
      else
        acc
      end
    end)
  end

  defp palindrome?(str), do: str == String.reverse(str)
end
```
