# 0301. Remove Invalid Parentheses

## Cpp

```cpp
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int left_rem = 0, right_rem = 0;
        for (char c : s) {
            if (c == '(') {
                ++left_rem;
            } else if (c == ')') {
                if (left_rem > 0) --left_rem;
                else ++right_rem;
            }
        }
        unordered_set<string> resultSet;
        string path;
        dfs(0, 0, 0, left_rem, right_rem, s, path, resultSet);
        return vector<string>(resultSet.begin(), resultSet.end());
    }

private:
    void dfs(int index, int left_count, int right_count,
             int left_rem, int right_rem,
             const string& s, string& path,
             unordered_set<string>& result) {
        if (index == (int)s.size()) {
            if (left_rem == 0 && right_rem == 0 && left_count == right_count) {
                result.insert(path);
            }
            return;
        }

        char c = s[index];
        if (c != '(' && c != ')') {
            path.push_back(c);
            dfs(index + 1, left_count, right_count, left_rem, right_rem, s, path, result);
            path.pop_back();
        } else if (c == '(') {
            // discard
            if (left_rem > 0) {
                dfs(index + 1, left_count, right_count, left_rem - 1, right_rem, s, path, result);
            }
            // keep
            path.push_back(c);
            dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, s, path, result);
            path.pop_back();
        } else { // c == ')'
            // discard
            if (right_rem > 0) {
                dfs(index + 1, left_count, right_count, left_rem, right_rem - 1, s, path, result);
            }
            // keep only if it won't lead to invalid prefix
            if (left_count > right_count) {
                path.push_back(c);
                dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, s, path, result);
                path.pop_back();
            }
        }
    }
};
```

## Java

```java
class Solution {
    public List<String> removeInvalidParentheses(String s) {
        int leftRem = 0, rightRem = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                leftRem++;
            } else if (c == ')') {
                if (leftRem > 0) {
                    leftRem--;
                } else {
                    rightRem++;
                }
            }
        }
        java.util.Set<String> resultSet = new java.util.HashSet<>();
        dfs(s, 0, 0, 0, leftRem, rightRem, new StringBuilder(), resultSet);
        return new java.util.ArrayList<>(resultSet);
    }

    private void dfs(String s, int index, int leftCount, int rightCount,
                     int leftRem, int rightRem, StringBuilder path,
                     java.util.Set<String> result) {
        if (index == s.length()) {
            if (leftRem == 0 && rightRem == 0) {
                result.add(path.toString());
            }
            return;
        }

        char c = s.charAt(index);
        int len = path.length();

        if (c != '(' && c != ')') {
            path.append(c);
            dfs(s, index + 1, leftCount, rightCount, leftRem, rightRem, path, result);
            path.setLength(len);
        } else {
            // Option to discard the current parenthesis
            if (c == '(' && leftRem > 0) {
                dfs(s, index + 1, leftCount, rightCount, leftRem - 1, rightRem, path, result);
            }
            if (c == ')' && rightRem > 0) {
                dfs(s, index + 1, leftCount, rightCount, leftRem, rightRem - 1, path, result);
            }

            // Option to keep the current parenthesis
            if (c == '(') {
                path.append(c);
                dfs(s, index + 1, leftCount + 1, rightCount, leftRem, rightRem, path, result);
                path.setLength(len);
            } else { // c == ')'
                if (rightCount < leftCount) {
                    path.append(c);
                    dfs(s, index + 1, leftCount, rightCount + 1, leftRem, rightRem, path, result);
                    path.setLength(len);
                }
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # First compute the number of misplaced '(' and ')' to remove
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = set()
        n = len(s)

        def dfs(index, left_count, right_count, lrem, rrem, path):
            if index == n:
                if lrem == 0 and rrem == 0:
                    res.add(''.join(path))
                return

            ch = s[index]

            # Option to discard current parenthesis
            if ch == '(' and lrem > 0:
                dfs(index + 1, left_count, right_count, lrem - 1, rrem, path)
            elif ch == ')' and rrem > 0:
                dfs(index + 1, left_count, right_count, lrem, rrem - 1, path)

            # Option to keep current character
            if ch not in ('(', ')'):
                path.append(ch)
                dfs(index + 1, left_count, right_count, lrem, rrem, path)
                path.pop()
            elif ch == '(':
                path.append(ch)
                dfs(index + 1, left_count + 1, right_count, lrem, rrem, path)
                path.pop()
            else:  # ch == ')'
                if left_count > right_count:
                    path.append(ch)
                    dfs(index + 1, left_count, right_count + 1, lrem, rrem, path)
                    path.pop()

        dfs(0, 0, 0, left_rem, right_rem, [])
        return list(res)
```

## Python3

```python
class Solution:
    def removeInvalidParentheses(self, s: str):
        from collections import deque
        # First pass to compute the number of misplaced '(' and ')'
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        res = set()
        visited = set()

        def dfs(i, path, left_cnt, right_cnt, lrem, rrem):
            state = (i, left_cnt, right_cnt, lrem, rrem)
            if state in visited:
                return
            visited.add(state)

            if i == len(s):
                if lrem == 0 and rrem == 0:
                    res.add(path)
                return

            ch = s[i]

            if ch == '(':
                # discard
                if lrem > 0:
                    dfs(i + 1, path, left_cnt, right_cnt, lrem - 1, rrem)
                # keep
                dfs(i + 1, path + ch, left_cnt + 1, right_cnt, lrem, rrem)

            elif ch == ')':
                # discard
                if rrem > 0:
                    dfs(i + 1, path, left_cnt, right_cnt, lrem, rrem - 1)
                # keep only if it can match a '('
                if left_cnt > right_cnt:
                    dfs(i + 1, path + ch, left_cnt, right_cnt + 1, lrem, rrem)

            else:
                # always keep non-parenthesis characters
                dfs(i + 1, path + ch, left_cnt, right_cnt, lrem, rrem)

        dfs(0, "", 0, 0, left_rem, right_rem)
        return list(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **arr;
    int size;
    int capacity;
} Result;

static char* strDup(const char *src) {
    size_t len = strlen(src);
    char *dst = (char *)malloc(len + 1);
    if (dst) memcpy(dst, src, len + 1);
    return dst;
}

static void addResult(Result *res, const char *str) {
    for (int i = 0; i < res->size; ++i) {
        if (strcmp(res->arr[i], str) == 0) return;
    }
    if (res->size == res->capacity) {
        int newCap = res->capacity * 2 + 1;
        char **newArr = (char **)realloc(res->arr, newCap * sizeof(char *));
        if (!newArr) return; // allocation failure, ignore
        res->arr = newArr;
        res->capacity = newCap;
    }
    res->arr[res->size++] = strDup(str);
}

static void dfs(const char *s, int n, int index,
                int leftCount, int rightCount,
                int leftRem, int rightRem,
                char *path, int pathLen,
                Result *res) {
    if (index == n) {
        if (leftRem == 0 && rightRem == 0 && leftCount == rightCount) {
            path[pathLen] = '\0';
            addResult(res, path);
        }
        return;
    }

    char c = s[index];
    if (c == '(') {
        // discard
        if (leftRem > 0)
            dfs(s, n, index + 1, leftCount, rightCount,
                leftRem - 1, rightRem, path, pathLen, res);
        // keep
        path[pathLen] = c;
        dfs(s, n, index + 1, leftCount + 1, rightCount,
            leftRem, rightRem, path, pathLen + 1, res);
    } else if (c == ')') {
        // discard
        if (rightRem > 0)
            dfs(s, n, index + 1, leftCount, rightCount,
                leftRem, rightRem - 1, path, pathLen, res);
        // keep only if it can be matched
        if (leftCount > rightCount) {
            path[pathLen] = c;
            dfs(s, n, index + 1, leftCount, rightCount + 1,
                leftRem, rightRem, path, pathLen + 1, res);
        }
    } else { // letter
        path[pathLen] = c;
        dfs(s, n, index + 1, leftCount, rightCount,
            leftRem, rightRem, path, pathLen + 1, res);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeInvalidParentheses(char* s, int* returnSize) {
    int leftRem = 0, rightRem = 0;
    for (int i = 0; s[i]; ++i) {
        if (s[i] == '(') {
            leftRem++;
        } else if (s[i] == ')') {
            if (leftRem > 0)
                leftRem--;
            else
                rightRem++;
        }
    }

    int n = strlen(s);
    char *path = (char *)malloc(n + 1);

    Result res;
    res.size = 0;
    res.capacity = 100;
    res.arr = (char **)malloc(res.capacity * sizeof(char *));

    dfs(s, n, 0, 0, 0, leftRem, rightRem, path, 0, &res);

    free(path);
    *returnSize = res.size;
    return res.arr;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

public class Solution {
    public IList<string> RemoveInvalidParentheses(string s) {
        int leftRem = 0, rightRem = 0;
        foreach (char c in s) {
            if (c == '(') {
                leftRem++;
            } else if (c == ')') {
                if (leftRem == 0) {
                    rightRem++;
                } else {
                    leftRem--;
                }
            }
        }

        var result = new HashSet<string>();
        void Dfs(int index, int leftCount, int rightCount, int lrem, int rrem, StringBuilder sb) {
            if (index == s.Length) {
                if (lrem == 0 && rrem == 0) {
                    result.Add(sb.ToString());
                }
                return;
            }

            char ch = s[index];
            if (ch == '(') {
                // discard
                if (lrem > 0) {
                    Dfs(index + 1, leftCount, rightCount, lrem - 1, rrem, sb);
                }
                // keep
                sb.Append(ch);
                Dfs(index + 1, leftCount + 1, rightCount, lrem, rrem, sb);
                sb.Length--;
            } else if (ch == ')') {
                // discard
                if (rrem > 0) {
                    Dfs(index + 1, leftCount, rightCount, lrem, rrem - 1, sb);
                }
                // keep if it forms a valid prefix
                if (leftCount > rightCount) {
                    sb.Append(ch);
                    Dfs(index + 1, leftCount, rightCount + 1, lrem, rrem, sb);
                    sb.Length--;
                }
            } else {
                sb.Append(ch);
                Dfs(index + 1, leftCount, rightCount, lrem, rrem, sb);
                sb.Length--;
            }
        }

        Dfs(0, 0, 0, leftRem, rightRem, new StringBuilder());
        return result.ToList();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    // First, determine the minimum number of '(' and ')' to remove.
    let leftRem = 0, rightRem = 0;
    for (const ch of s) {
        if (ch === '(') {
            leftRem++;
        } else if (ch === ')') {
            if (leftRem > 0) {
                leftRem--;
            } else {
                rightRem++;
            }
        }
    }

    const res = new Set();
    const visited = new Set();

    function dfs(index, expr, leftCount, rightCount, lRem, rRem) {
        const key = `${index},${leftCount},${rightCount},${lRem},${rRem}`;
        if (visited.has(key)) return;
        visited.add(key);

        if (index === s.length) {
            if (lRem === 0 && rRem === 0 && leftCount === rightCount) {
                res.add(expr);
            }
            return;
        }

        const ch = s[index];

        if (ch === '(') {
            // Option 1: delete it
            if (lRem > 0) {
                dfs(index + 1, expr, leftCount, rightCount, lRem - 1, rRem);
            }
            // Option 2: keep it
            dfs(index + 1, expr + ch, leftCount + 1, rightCount, lRem, rRem);
        } else if (ch === ')') {
            // Option 1: delete it
            if (rRem > 0) {
                dfs(index + 1, expr, leftCount, rightCount, lRem, rRem - 1);
            }
            // Option 2: keep it only if there is a matching '('
            if (leftCount > rightCount) {
                dfs(index + 1, expr + ch, leftCount, rightCount + 1, lRem, rRem);
            }
        } else {
            // Non-parenthesis characters are always kept.
            dfs(index + 1, expr + ch, leftCount, rightCount, lRem, rRem);
        }
    }

    dfs(0, "", 0, 0, leftRem, rightRem);
    return Array.from(res);
};
```

## Typescript

```typescript
function removeInvalidParentheses(s: string): string[] {
    // First, determine the minimum number of left and right parentheses to remove
    let leftRem = 0;
    let rightRem = 0;
    for (const ch of s) {
        if (ch === '(') {
            leftRem++;
        } else if (ch === ')') {
            if (leftRem > 0) {
                leftRem--;
            } else {
                rightRem++;
            }
        }
    }

    const result = new Set<string>();
    const visited = new Set<string>();

    function dfs(
        index: number,
        leftCount: number,
        rightCount: number,
        lRem: number,
        rRem: number,
        path: string
    ): void {
        if (index === s.length) {
            if (lRem === 0 && rRem === 0 && leftCount === rightCount) {
                result.add(path);
            }
            return;
        }

        const key = `${index},${leftCount},${rightCount},${lRem},${rRem}`;
        if (visited.has(key)) return;
        visited.add(key);

        const ch = s[index];

        if (ch !== '(' && ch !== ')') {
            dfs(index + 1, leftCount, rightCount, lRem, rRem, path + ch);
        } else if (ch === '(') {
            // Option 1: discard this '('
            if (lRem > 0) {
                dfs(index + 1, leftCount, rightCount, lRem - 1, rRem, path);
            }
            // Option 2: keep this '('
            dfs(index + 1, leftCount + 1, rightCount, lRem, rRem, path + ch);
        } else { // ch === ')'
            // Option 1: discard this ')'
            if (rRem > 0) {
                dfs(index + 1, leftCount, rightCount, lRem, rRem - 1, path);
            }
            // Option 2: keep this ')' only if it won't lead to invalid prefix
            if (leftCount > rightCount) {
                dfs(index + 1, leftCount, rightCount + 1, lRem, rRem, path + ch);
            }
        }
    }

    dfs(0, 0, 0, leftRem, rightRem, '');
    // If no valid strings were added (possible when input is empty), ensure at least empty string
    if (result.size === 0) result.add('');
    return Array.from(result);
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function removeInvalidParentheses($s) {
        $leftRem = 0;
        $rightRem = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === '(') {
                $leftRem++;
            } elseif ($c === ')') {
                if ($leftRem > 0) {
                    $leftRem--;
                } else {
                    $rightRem++;
                }
            }
        }

        $resultSet = [];
        $this->dfs($s, 0, 0, 0, $leftRem, $rightRem, "", $resultSet);
        return array_keys($resultSet);
    }

    private function dfs($s, $index, $leftCount, $rightCount, $leftRem, $rightRem, $path, &$set) {
        if ($index == strlen($s)) {
            if ($leftRem === 0 && $rightRem === 0) {
                $set[$path] = true;
            }
            return;
        }

        $c = $s[$index];
        if ($c === '(') {
            // discard
            if ($leftRem > 0) {
                $this->dfs($s, $index + 1, $leftCount, $rightCount, $leftRem - 1, $rightRem, $path, $set);
            }
            // keep
            $this->dfs($s, $index + 1, $leftCount + 1, $rightCount, $leftRem, $rightRem, $path . '(', $set);
        } elseif ($c === ')') {
            // discard
            if ($rightRem > 0) {
                $this->dfs($s, $index + 1, $leftCount, $rightCount, $leftRem, $rightRem - 1, $path, $set);
            }
            // keep if it forms a valid prefix
            if ($leftCount > $rightCount) {
                $this->dfs($s, $index + 1, $leftCount, $rightCount + 1, $leftRem, $rightRem, $path . ')', $set);
            }
        } else {
            // always keep non-parenthesis characters
            $this->dfs($s, $index + 1, $leftCount, $rightCount, $leftRem, $rightRem, $path . $c, $set);
        }
    }
}
```

## Swift

```swift
class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        let chars = Array(s)
        var leftRem = 0, rightRem = 0
        for ch in chars {
            if ch == "(" {
                leftRem += 1
            } else if ch == ")" {
                if leftRem > 0 {
                    leftRem -= 1
                } else {
                    rightRem += 1
                }
            }
        }
        
        var result = Set<String>()
        var path: [Character] = []
        
        func dfs(_ index: Int, _ leftCount: Int, _ rightCount: Int, _ lRem: Int, _ rRem: Int) {
            if index == chars.count {
                if lRem == 0 && rRem == 0 && leftCount == rightCount {
                    result.insert(String(path))
                }
                return
            }
            
            let ch = chars[index]
            if ch == "(" {
                // Discard '('
                if lRem > 0 {
                    dfs(index + 1, leftCount, rightCount, lRem - 1, rRem)
                }
                // Keep '('
                path.append(ch)
                dfs(index + 1, leftCount + 1, rightCount, lRem, rRem)
                path.removeLast()
            } else if ch == ")" {
                // Discard ')'
                if rRem > 0 {
                    dfs(index + 1, leftCount, rightCount, lRem, rRem - 1)
                }
                // Keep ')' only if it won't invalidate the string
                if leftCount > rightCount {
                    path.append(ch)
                    dfs(index + 1, leftCount, rightCount + 1, lRem, rRem)
                    path.removeLast()
                }
            } else {
                // Non-parenthesis character, always keep
                path.append(ch)
                dfs(index + 1, leftCount, rightCount, lRem, rRem)
                path.removeLast()
            }
        }
        
        dfs(0, 0, 0, leftRem, rightRem)
        return Array(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        var leftRem = 0
        var rightRem = 0
        for (ch in s) {
            when (ch) {
                '(' -> leftRem++
                ')' -> if (leftRem > 0) leftRem-- else rightRem++
            }
        }
        val result = HashSet<String>()
        val path = StringBuilder()
        fun dfs(index: Int, leftCount: Int, rightCount: Int, lRem: Int, rRem: Int) {
            if (index == s.length) {
                if (lRem == 0 && rRem == 0 && leftCount == rightCount) {
                    result.add(path.toString())
                }
                return
            }
            val ch = s[index]
            when (ch) {
                '(' -> {
                    // discard
                    if (lRem > 0) dfs(index + 1, leftCount, rightCount, lRem - 1, rRem)
                    // keep
                    path.append(ch)
                    dfs(index + 1, leftCount + 1, rightCount, lRem, rRem)
                    path.deleteCharAt(path.length - 1)
                }
                ')' -> {
                    // discard
                    if (rRem > 0) dfs(index + 1, leftCount, rightCount, lRem, rRem - 1)
                    // keep if it won't make the string invalid
                    if (leftCount > rightCount) {
                        path.append(ch)
                        dfs(index + 1, leftCount, rightCount + 1, lRem, rRem)
                        path.deleteCharAt(path.length - 1)
                    }
                }
                else -> {
                    path.append(ch)
                    dfs(index + 1, leftCount, rightCount, lRem, rRem)
                    path.deleteCharAt(path.length - 1)
                }
            }
        }
        dfs(0, 0, 0, leftRem, rightRem)
        return result.toList()
    }
}
```

## Dart

```dart
class Solution {
  List<String> removeInvalidParentheses(String s) {
    int leftRem = 0;
    int rightRem = 0;
    for (int i = 0; i < s.length; i++) {
      var c = s[i];
      if (c == '(') {
        leftRem++;
      } else if (c == ')') {
        if (leftRem > 0) {
          leftRem--;
        } else {
          rightRem++;
        }
      }
    }

    final Set<String> result = {};

    void dfs(int index, int leftCount, int rightCount, int lRem, int rRem,
        String path) {
      if (index == s.length) {
        if (lRem == 0 && rRem == 0 && leftCount == rightCount) {
          result.add(path);
        }
        return;
      }

      final ch = s[index];
      if (ch != '(' && ch != ')') {
        dfs(index + 1, leftCount, rightCount, lRem, rRem, path + ch);
      } else if (ch == '(') {
        // Discard this '('
        if (lRem > 0) {
          dfs(index + 1, leftCount, rightCount, lRem - 1, rRem, path);
        }
        // Keep this '('
        dfs(index + 1, leftCount + 1, rightCount, lRem, rRem, path + ch);
      } else { // ch == ')'
        // Discard this ')'
        if (rRem > 0) {
          dfs(index + 1, leftCount, rightCount, lRem, rRem - 1, path);
        }
        // Keep this ')' only if it won't lead to invalid prefix
        if (leftCount > rightCount) {
          dfs(index + 1, leftCount, rightCount + 1, lRem, rRem, path + ch);
        }
      }
    }

    dfs(0, 0, 0, leftRem, rightRem, '');
    return result.toList();
  }
}
```

## Golang

```go
func removeInvalidParentheses(s string) []string {
    // First determine the minimum number of '(' and ')' to remove.
    leftRem, rightRem := 0, 0
    for _, ch := range s {
        if ch == '(' {
            leftRem++
        } else if ch == ')' {
            if leftRem > 0 {
                leftRem--
            } else {
                rightRem++
            }
        }
    }

    results := make(map[string]struct{})
    var dfs func(idx, leftCnt, rightCnt, lrem, rrem int, path []rune)

    dfs = func(idx, leftCnt, rightCnt, lrem, rrem int, path []rune) {
        if idx == len(s) {
            if lrem == 0 && rrem == 0 && leftCnt == rightCnt {
                results[string(path)] = struct{}{}
            }
            return
        }

        c := rune(s[idx])

        if c == '(' {
            // Option 1: delete it
            if lrem > 0 {
                dfs(idx+1, leftCnt, rightCnt, lrem-1, rrem, path)
            }
            // Option 2: keep it
            path = append(path, c)
            dfs(idx+1, leftCnt+1, rightCnt, lrem, rrem, path)
            path = path[:len(path)-1]
        } else if c == ')' {
            // Option 1: delete it
            if rrem > 0 {
                dfs(idx+1, leftCnt, rightCnt, lrem, rrem-1, path)
            }
            // Option 2: keep it (only if there is a matching '(')
            if leftCnt > rightCnt {
                path = append(path, c)
                dfs(idx+1, leftCnt, rightCnt+1, lrem, rrem, path)
                path = path[:len(path)-1]
            }
        } else {
            // Non-parenthesis characters are always kept
            path = append(path, c)
            dfs(idx+1, leftCnt, rightCnt, lrem, rrem, path)
            path = path[:len(path)-1]
        }
    }

    dfs(0, 0, 0, leftRem, rightRem, []rune{})

    ans := make([]string, 0, len(results))
    for str := range results {
        ans = append(ans, str)
    }
    return ans
}
```

## Ruby

```ruby
require 'set'

def remove_invalid_parentheses(s)
  left_rem = 0
  right_rem = 0
  s.each_char do |c|
    if c == '('
      left_rem += 1
    elsif c == ')'
      if left_rem > 0
        left_rem -= 1
      else
        right_rem += 1
      end
    end
  end

  results = Set.new
  dfs(s, 0, 0, 0, left_rem, right_rem, "", results)
  results.to_a
end

def dfs(s, idx, left_cnt, right_cnt, left_rem, right_rem, path, results)
  if idx == s.length
    if left_rem == 0 && right_rem == 0 && left_cnt == right_cnt
      results.add(path)
    end
    return
  end

  ch = s[idx]

  # Option to discard the current parenthesis
  if ch == '(' && left_rem > 0
    dfs(s, idx + 1, left_cnt, right_cnt, left_rem - 1, right_rem, path, results)
  elsif ch == ')' && right_rem > 0
    dfs(s, idx + 1, left_cnt, right_cnt, left_rem, right_rem - 1, path, results)
  end

  # Option to keep the current character
  if ch != '(' && ch != ')'
    dfs(s, idx + 1, left_cnt, right_cnt, left_rem, right_rem, path + ch, results)
  elsif ch == '('
    dfs(s, idx + 1, left_cnt + 1, right_cnt, left_rem, right_rem, path + ch, results)
  else # ch == ')'
    if left_cnt > right_cnt
      dfs(s, idx + 1, left_cnt, right_cnt + 1, left_rem, right_rem, path + ch, results)
    end
  end
end
```

## Scala

```scala
object Solution {
  def removeInvalidParentheses(s: String): List[String] = {
    var leftRem = 0
    var rightRem = 0
    for (c <- s) {
      if (c == '(') leftRem += 1
      else if (c == ')') {
        if (leftRem > 0) leftRem -= 1
        else rightRem += 1
      }
    }

    val results = scala.collection.mutable.HashSet[String]()

    def dfs(i: Int, leftCount: Int, rightCount: Int,
            lRem: Int, rRem: Int, sb: StringBuilder): Unit = {
      if (i == s.length) {
        if (lRem == 0 && rRem == 0 && leftCount == rightCount) {
          results += sb.toString()
        }
        return
      }

      val ch = s.charAt(i)

      if (ch == '(') {
        // discard
        if (lRem > 0) dfs(i + 1, leftCount, rightCount, lRem - 1, rRem, sb)
        // keep
        sb.append(ch)
        dfs(i + 1, leftCount + 1, rightCount, lRem, rRem, sb)
        sb.deleteCharAt(sb.length - 1)
      } else if (ch == ')') {
        // discard
        if (rRem > 0) dfs(i + 1, leftCount, rightCount, lRem, rRem - 1, sb)
        // keep only if it can be matched
        if (leftCount > rightCount) {
          sb.append(ch)
          dfs(i + 1, leftCount, rightCount + 1, lRem, rRem, sb)
          sb.deleteCharAt(sb.length - 1)
        }
      } else {
        sb.append(ch)
        dfs(i + 1, leftCount, rightCount, lRem, rRem, sb)
        sb.deleteCharAt(sb.length - 1)
      }
    }

    dfs(0, 0, 0, leftRem, rightRem, new StringBuilder())
    results.toList
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        let chars: Vec<char> = s.chars().collect();

        // Determine the minimum number of '(' and ')' to remove
        let mut left_rem = 0i32;
        let mut right_rem = 0i32;
        for &c in &chars {
            if c == '(' {
                left_rem += 1;
            } else if c == ')' {
                if left_rem > 0 {
                    left_rem -= 1;
                } else {
                    right_rem += 1;
                }
            }
        }

        let mut result: HashSet<String> = HashSet::new();
        let mut path = String::new();
        Self::dfs(
            &chars,
            0,
            0,
            0,
            left_rem,
            right_rem,
            &mut path,
            &mut result,
        );
        result.into_iter().collect()
    }

    fn dfs(
        chars: &Vec<char>,
        index: usize,
        left_count: i32,
        right_count: i32,
        left_rem: i32,
        right_rem: i32,
        path: &mut String,
        res: &mut HashSet<String>,
    ) {
        if index == chars.len() {
            if left_rem == 0 && right_rem == 0 {
                res.insert(path.clone());
            }
            return;
        }

        let c = chars[index];
        if c == '(' {
            // Option to delete this '('
            if left_rem > 0 && !(index > 0 && chars[index - 1] == '(') {
                Self::dfs(
                    chars,
                    index + 1,
                    left_count,
                    right_count,
                    left_rem - 1,
                    right_rem,
                    path,
                    res,
                );
            }
            // Keep this '('
            path.push(c);
            Self::dfs(
                chars,
                index + 1,
                left_count + 1,
                right_count,
                left_rem,
                right_rem,
                path,
                res,
            );
            path.pop();
        } else if c == ')' {
            // Option to delete this ')'
            if right_rem > 0 && !(index > 0 && chars[index - 1] == ')') {
                Self::dfs(
                    chars,
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem - 1,
                    path,
                    res,
                );
            }
            // Keep this ')' only if it won't lead to invalid string
            if left_count > right_count {
                path.push(c);
                Self::dfs(
                    chars,
                    index + 1,
                    left_count,
                    right_count + 1,
                    left_rem,
                    right_rem,
                    path,
                    res,
                );
                path.pop();
            }
        } else {
            // Non-parenthesis characters are always kept
            path.push(c);
            Self::dfs(
                chars,
                index + 1,
                left_count,
                right_count,
                left_rem,
                right_rem,
                path,
                res,
            );
            path.pop();
        }
    }
}
```

## Racket

```racket
(define/contract (remove-invalid-parentheses s)
  (-> string? (listof string?))
  (let* ((len (string-length s))
         ;; compute minimal removals
         (calc-removals
          (let loop ((i 0) (left 0) (right-rem 0))
            (if (= i len)
                (list left right-rem)
                (let ((c (string-ref s i)))
                  (cond [(char=? c #\()
                         (loop (+ i 1) (+ left 1) right-rem)]
                        [(char=? c #\))
                         (if (> left 0)
                             (loop (+ i 1) (- left 1) right-rem)
                             (loop (+ i 1) left (+ right-rem 1)))]
                        [else
                         (loop (+ i 1) left right-rem)])))))
         (left-rem (first calc-removals))
         (right-rem (second calc-removals))
         (result (make-hash)))
    ;; depth‑first search with pruning
    (define (dfs index left-count right-count lrem rrem path)
      (cond [(= index len)
             (when (and (= lrem 0) (= rrem 0) (= left-count right-count))
               (hash-set! result path #t))]
            [else
             (let ((c (string-ref s index)))
               (cond [(char=? c #\()
                      ;; discard '(' if we still need to remove some
                      (when (> lrem 0)
                        (dfs (+ index 1) left-count right-count (- lrem 1) rrem path))
                      ;; keep '('
                      (dfs (+ index 1) (+ left-count 1) right-count lrem rrem
                           (string-append path (string c)))]
                     [(char=? c #\))
                      ;; discard ')' if we still need to remove some
                      (when (> rrem 0)
                        (dfs (+ index 1) left-count right-count lrem (- rrem 1) path))
                      ;; keep ')' only when it can match a '('
                      (when (> left-count right-count)
                        (dfs (+ index 1) left-count (+ right-count 1) lrem rrem
                             (string-append path (string c))))]
                     [else
                      ;; non‑parenthesis character, always keep
                      (dfs (+ index 1) left-count right-count lrem rrem
                           (string-append path (string c)))]))]))
    (dfs 0 0 0 left-rem right-rem "")
    ;; collect results from hash table
    (let loop ((acc '()) (pairs (hash->list result)))
      (if (null? pairs)
          (reverse acc)
          (loop (cons (caar pairs) acc) (cdr pairs)))))
```

## Erlang

```erlang
-module(solution).
-export([remove_invalid_parentheses/1]).

-spec remove_invalid_parentheses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
remove_invalid_parentheses(S) ->
    Chars = unicode:characters_to_list(S),
    {LRem, RRem} = calc_removals(Chars),
    Set = dfs(Chars, 0, 0, LRem, RRem, [], #{}),
    maps:keys(Set).

calc_removals(Chars) -> calc_removals(Chars, 0, 0).

calc_removals([], Balance, RightRem) ->
    {Balance, RightRem};
calc_removals([C|Rest], Balance, RightRem) when C == $( ->
    calc_removals(Rest, Balance + 1, RightRem);
calc_removals([C|Rest], Balance, RightRem) when C == $) ->
    if Balance > 0 ->
            calc_removals(Rest, Balance - 1, RightRem);
       true ->
            calc_removals(Rest, Balance, RightRem + 1)
    end;
calc_removals([_|Rest], Balance, RightRem) ->
    calc_removals(Rest, Balance, RightRem).

dfs([], LeftCount, RightCount, 0, 0, PathRev, Set) when LeftCount == RightCount ->
    Bin = list_to_binary(lists:reverse(PathRev)),
    maps:put(Bin, true, Set);
dfs([], _LC, _RC, _LRem, _RRem, _PathRev, Set) ->
    Set;
dfs([C|Rest], LC, RC, LRem, RRem, PathRev, Set0) ->
    % discard '(' if possible
    Set1 = case C of
        $( when LRem > 0 -> dfs(Rest, LC, RC, LRem - 1, RRem, PathRev, Set0);
        _ -> Set0
    end,
    % discard ')' if possible
    Set2 = case C of
        $) when RRem > 0 -> dfs(Rest, LC, RC, LRem, RRem - 1, PathRev, Set1);
        _ -> Set1
    end,
    % keep character
    Set3 = case C of
        $( ->
            dfs(Rest, LC + 1, RC, LRem, RRem, [C|PathRev], Set2);
        $) when RC < LC ->
            dfs(Rest, LC, RC + 1, LRem, RRem, [C|PathRev], Set2);
        _ ->
            dfs(Rest, LC, RC, Lrem, Rrem, [C|PathRev], Set2)
    end,
    Set3.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_invalid_parentheses(s :: String.t) :: [String.t]
  def remove_invalid_parentheses(s) do
    chars = String.graphemes(s)
    {left_rem, right_rem} = calculate_removals(chars)
    result_set = dfs(chars, 0, 0, left_rem, right_rem, [], MapSet.new())
    MapSet.to_list(result_set)
  end

  defp calculate_removals(chars) do
    Enum.reduce(chars, {0, 0}, fn
      "(", {l, r} -> {l + 1, r}
      ")", {l, r} ->
        if l > 0 do
          {l - 1, r}
        else
          {l, r + 1}
        end

      _, acc -> acc
    end)
  end

  defp dfs([], left_cnt, right_cnt, left_rem, right_rem, path, acc) do
    if left_rem == 0 and right_rem == 0 and left_cnt == right_cnt do
      str = Enum.reverse(path) |> Enum.join()
      MapSet.put(acc, str)
    else
      acc
    end
  end

  defp dfs([c | rest], left_cnt, right_cnt, left_rem, right_rem, path, acc) do
    case c do
      "(" ->
        # Option 1: discard this '(' if we still have left removals left
        acc1 =
          if left_rem > 0 do
            dfs(rest, left_cnt, right_cnt, left_rem - 1, right_rem, path, acc)
          else
            acc
          end

        # Option 2: keep this '('
        dfs(rest, left_cnt + 1, right_cnt, left_rem, right_rem, [c | path], acc1)

      ")" ->
        # Option 1: discard this ')' if we still have right removals left
        acc1 =
          if right_rem > 0 do
            dfs(rest, left_cnt, right_cnt, left_rem, right_rem - 1, path, acc)
          else
            acc
          end

        # Option 2: keep this ')' only if it won't make the string invalid
        if left_cnt > right_cnt do
          dfs(rest, left_cnt, right_cnt + 1, left_rem, right_rem, [c | path], acc1)
        else
          acc1
        end

      _ ->
        # Non-parenthesis characters are always kept
        dfs(rest, left_cnt, right_cnt, left_rem, right_rem, [c | path], acc)
    end
  end
end
```
