# 1092. Shortest Common Supersequence

## Cpp

```cpp
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 0; i <= n; ++i) dp[i][0] = i;
        for (int j = 0; j <= m; ++j) dp[0][j] = j;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (str1[i - 1] == str2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1;
            }
        }
        string res;
        int i = n, j = m;
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                res.push_back(str1[i - 1]);
                --i; --j;
            } else if (dp[i - 1][j] < dp[i][j - 1]) {
                res.push_back(str1[i - 1]);
                --i;
            } else {
                res.push_back(str2[j - 1]);
                --j;
            }
        }
        while (i > 0) res.push_back(str1[--i]);
        while (j > 0) res.push_back(str2[--j]);
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) dp[i][0] = i;
        for (int j = 0; j <= m; j++) dp[0][j] = j;

        for (int i = 1; i <= n; i++) {
            char c1 = str1.charAt(i - 1);
            for (int j = 1; j <= m; j++) {
                char c2 = str2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        int i = n, j = m;
        while (i > 0 && j > 0) {
            char c1 = str1.charAt(i - 1);
            char c2 = str2.charAt(j - 1);
            if (c1 == c2) {
                sb.append(c1);
                i--;
                j--;
            } else if (dp[i - 1][j] < dp[i][j - 1]) {
                sb.append(c1);
                i--;
            } else {
                sb.append(c2);
                j--;
            }
        }
        while (i > 0) {
            sb.append(str1.charAt(i - 1));
            i--;
        }
        while (j > 0) {
            sb.append(str2.charAt(j - 1));
            j--;
        }

        return sb.reverse().toString();
    }
}
```

## Python

```python
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            c1 = str1[i - 1]
            row = dp[i]
            prev_row = dp[i - 1]
            for j in range(1, m + 1):
                if c1 == str2[j - 1]:
                    row[j] = prev_row[j - 1] + 1
                else:
                    row[j] = min(prev_row[j], row[j - 1]) + 1

        i, j = n, m
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1

        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return ''.join(reversed(res))
```

## Python3

```python
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = i
        for j in range(1, m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            c1 = str1[i - 1]
            row = dp[i]
            prev_row = dp[i - 1]
            for j in range(1, m + 1):
                if c1 == str2[j - 1]:
                    row[j] = prev_row[j - 1] + 1
                else:
                    row[j] = min(prev_row[j], row[j - 1]) + 1

        i, j = n, m
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1

        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return ''.join(reversed(res))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* shortestCommonSupersequence(char* str1, char* str2) {
    int n = strlen(str1);
    int m = strlen(str2);
    int rows = n + 1;
    int cols = m + 1;

    int *dp = (int *)malloc(rows * cols * sizeof(int));
    if (!dp) return NULL;

    for (int i = 0; i <= n; ++i) dp[i * cols] = i;
    for (int j = 0; j <= m; ++j) dp[j] = j;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i * cols + j] = dp[(i - 1) * cols + (j - 1)] + 1;
            } else {
                int up   = dp[(i - 1) * cols + j];
                int left = dp[i * cols + (j - 1)];
                dp[i * cols + j] = (up < left ? up : left) + 1;
            }
        }
    }

    int len = dp[n * cols + m];
    char *res = (char *)malloc((len + 1) * sizeof(char));
    if (!res) {
        free(dp);
        return NULL;
    }

    int i = n, j = m, idx = len - 1;
    while (i > 0 && j > 0) {
        if (str1[i - 1] == str2[j - 1]) {
            res[idx--] = str1[i - 1];
            --i; --j;
        } else {
            int up   = dp[(i - 1) * cols + j];
            int left = dp[i * cols + (j - 1)];
            if (up < left) {
                res[idx--] = str1[i - 1];
                --i;
            } else {
                res[idx--] = str2[j - 1];
                --j;
            }
        }
    }
    while (i > 0) {
        res[idx--] = str1[--i];
    }
    while (j > 0) {
        res[idx--] = str2[--j];
    }

    res[len] = '\0';
    free(dp);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string ShortestCommonSupersequence(string str1, string str2) {
        int n = str1.Length;
        int m = str2.Length;
        int[,] dp = new int[n + 1, m + 1];

        for (int i = 0; i <= n; i++) dp[i, 0] = i;
        for (int j = 0; j <= m; j++) dp[0, j] = j;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i, j] = dp[i - 1, j - 1] + 1;
                } else {
                    dp[i, j] = Math.Min(dp[i - 1, j], dp[i, j - 1]) + 1;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        int ii = n, jj = m;
        while (ii > 0 && jj > 0) {
            if (str1[ii - 1] == str2[jj - 1]) {
                sb.Append(str1[ii - 1]);
                ii--; jj--;
            } else if (dp[ii - 1, jj] < dp[ii, jj - 1]) {
                sb.Append(str1[ii - 1]);
                ii--;
            } else {
                sb.Append(str2[jj - 1]);
                jj--;
            }
        }

        while (ii > 0) {
            sb.Append(str1[ii - 1]);
            ii--;
        }
        while (jj > 0) {
            sb.Append(str2[jj - 1]);
            jj--;
        }

        // reverse the built string
        char[] arr = sb.ToString().ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var shortestCommonSupersequence = function(str1, str2) {
    const n = str1.length;
    const m = str2.length;
    // dp[i][j] = length of SCS for str1[0..i-1], str2[0..j-1]
    const dp = Array.from({ length: n + 1 }, () => new Uint16Array(m + 1));
    for (let i = 0; i <= n; ++i) dp[i][0] = i;
    for (let j = 0; j <= m; ++j) dp[0][j] = j;

    for (let i = 1; i <= n; ++i) {
        const c1 = str1.charAt(i - 1);
        for (let j = 1; j <= m; ++j) {
            if (c1 === str2.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
            }
        }
    }

    // Reconstruct answer
    let i = n, j = m;
    const res = [];
    while (i > 0 && j > 0) {
        if (str1.charAt(i - 1) === str2.charAt(j - 1)) {
            res.push(str1.charAt(i - 1));
            --i; --j;
        } else if (dp[i - 1][j] < dp[i][j - 1]) {
            res.push(str1.charAt(i - 1));
            --i;
        } else {
            res.push(str2.charAt(j - 1));
            --j;
        }
    }
    while (i > 0) {
        res.push(str1.charAt(--i));
    }
    while (j > 0) {
        res.push(str2.charAt(--j));
    }

    return res.reverse().join('');
};
```

## Typescript

```typescript
function shortestCommonSupersequence(str1: string, str2: string): string {
    const n = str1.length;
    const m = str2.length;

    // dp[i][j] = length of SCS for str1[0..i-1], str2[0..j-1]
    const dp: number[][] = Array.from({ length: n + 1 }, () => new Array(m + 1).fill(0));

    for (let i = 0; i <= n; i++) dp[i][0] = i;
    for (let j = 0; j <= m; j++) dp[0][j] = j;

    for (let i = 1; i <= n; i++) {
        const c1 = str1.charAt(i - 1);
        for (let j = 1; j <= m; j++) {
            const c2 = str2.charAt(j - 1);
            if (c1 === c2) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + 1;
            }
        }
    }

    // Reconstruct the SCS from dp table
    let i = n, j = m;
    const res: string[] = [];

    while (i > 0 && j > 0) {
        if (str1.charAt(i - 1) === str2.charAt(j - 1)) {
            res.push(str1.charAt(i - 1));
            i--;
            j--;
        } else if (dp[i - 1][j] < dp[i][j - 1]) {
            res.push(str1.charAt(i - 1));
            i--;
        } else {
            res.push(str2.charAt(j - 1));
            j--;
        }
    }

    while (i > 0) {
        res.push(str1.charAt(i - 1));
        i--;
    }
    while (j > 0) {
        res.push(str2.charAt(j - 1));
        j--;
    }

    return res.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function shortestCommonSupersequence($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);

        // dp[i][j] = length of SCS for str1[0..i-1], str2[0..j-1]
        $dp = array_fill(0, $n + 1, array_fill(0, $m + 1, 0));

        for ($i = 0; $i <= $n; $i++) {
            $dp[$i][0] = $i;
        }
        for ($j = 0; $j <= $m; $j++) {
            $dp[0][$j] = $j;
        }

        for ($i = 1; $i <= $n; $i++) {
            $c1 = $str1[$i - 1];
            for ($j = 1; $j <= $m; $j++) {
                $c2 = $str2[$j - 1];
                if ($c1 === $c2) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1] + 1;
                } else {
                    $dp[$i][$j] = min($dp[$i - 1][$j], $dp[$i][$j - 1]) + 1;
                }
            }
        }

        // Reconstruct SCS from dp table
        $i = $n;
        $j = $m;
        $res = '';

        while ($i > 0 && $j > 0) {
            if ($str1[$i - 1] === $str2[$j - 1]) {
                $res .= $str1[$i - 1];
                $i--;
                $j--;
            } else {
                if ($dp[$i - 1][$j] < $dp[$i][$j - 1]) {
                    $res .= $str1[$i - 1];
                    $i--;
                } else {
                    $res .= $str2[$j - 1];
                    $j--;
                }
            }
        }

        while ($i > 0) {
            $res .= $str1[$i - 1];
            $i--;
        }
        while ($j > 0) {
            $res .= $str2[$j - 1];
            $j--;
        }

        return strrev($res);
    }
}
```

## Swift

```swift
class Solution {
    func shortestCommonSupersequence(_ str1: String, _ str2: String) -> String {
        let s1 = Array(str1)
        let s2 = Array(str2)
        let m = s1.count
        let n = s2.count
        
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        
        for i in 0...m { dp[i][0] = i }
        for j in 0...n { dp[0][j] = j }
        
        if m > 0 && n > 0 {
            for i in 1...m {
                for j in 1...n {
                    if s1[i - 1] == s2[j - 1] {
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    } else {
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                    }
                }
            }
        }
        
        var i = m
        var j = n
        var result: [Character] = []
        
        while i > 0 && j > 0 {
            if s1[i - 1] == s2[j - 1] {
                result.append(s1[i - 1])
                i -= 1
                j -= 1
            } else if dp[i - 1][j] < dp[i][j - 1] {
                result.append(s1[i - 1])
                i -= 1
            } else {
                result.append(s2[j - 1])
                j -= 1
            }
        }
        
        while i > 0 {
            result.append(s1[i - 1])
            i -= 1
        }
        while j > 0 {
            result.append(s2[j - 1])
            j -= 1
        }
        
        return String(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestCommonSupersequence(str1: String, str2: String): String {
        val n = str1.length
        val m = str2.length
        val dp = Array(n + 1) { IntArray(m + 1) }

        for (i in 0..n) dp[i][0] = i
        for (j in 0..m) dp[0][j] = j

        for (i in 1..n) {
            val c1 = str1[i - 1]
            for (j in 1..m) {
                val c2 = str2[j - 1]
                dp[i][j] = if (c1 == c2) {
                    dp[i - 1][j - 1] + 1
                } else {
                    kotlin.math.min(dp[i - 1][j], dp[i][j - 1]) + 1
                }
            }
        }

        val sb = StringBuilder()
        var i = n
        var j = m
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                sb.append(str1[i - 1])
                i--
                j--
            } else if (dp[i - 1][j] < dp[i][j - 1]) {
                sb.append(str1[i - 1])
                i--
            } else {
                sb.append(str2[j - 1])
                j--
            }
        }
        while (i > 0) {
            sb.append(str1[i - 1])
            i--
        }
        while (j > 0) {
            sb.append(str2[j - 1])
            j--
        }

        return sb.reverse().toString()
    }
}
```

## Dart

```dart
class Solution {
  String shortestCommonSupersequence(String str1, String str2) {
    int n = str1.length;
    int m = str2.length;

    // dp[i][j] = length of SCS for str1[0..i-1], str2[0..j-1]
    List<List<int>> dp = List.generate(n + 1, (_) => List.filled(m + 1, 0));

    for (int i = 0; i <= n; ++i) {
      dp[i][0] = i;
    }
    for (int j = 0; j <= m; ++j) {
      dp[0][j] = j;
    }

    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j) {
        if (str1.codeUnitAt(i - 1) == str2.codeUnitAt(j - 1)) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
        } else {
          dp[i][j] = (dp[i - 1][j] < dp[i][j - 1] ? dp[i - 1][j] : dp[i][j - 1]) + 1;
        }
      }
    }

    // Reconstruct SCS from dp table
    int i = n, j = m;
    StringBuffer sb = StringBuffer();

    while (i > 0 && j > 0) {
      if (str1.codeUnitAt(i - 1) == str2.codeUnitAt(j - 1)) {
        sb.writeCharCode(str1.codeUnitAt(i - 1));
        i--;
        j--;
      } else if (dp[i - 1][j] < dp[i][j - 1]) {
        sb.writeCharCode(str1.codeUnitAt(i - 1));
        i--;
      } else {
        sb.writeCharCode(str2.codeUnitAt(j - 1));
        j--;
      }
    }

    while (i > 0) {
      sb.writeCharCode(str1.codeUnitAt(i - 1));
      i--;
    }
    while (j > 0) {
      sb.writeCharCode(str2.codeUnitAt(j - 1));
      j--;
    }

    // The string was built backwards, reverse it
    String rev = sb.toString();
    return rev.split('').reversed.join();
  }
}
```

## Golang

```go
func shortestCommonSupersequence(str1 string, str2 string) string {
	n := len(str1)
	m := len(str2)

	// dp[i][j] = length of SCS for str1[:i] and str2[:j]
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, m+1)
	}
	for i := 0; i <= n; i++ {
		dp[i][0] = i
	}
	for j := 0; j <= m; j++ {
		dp[0][j] = j
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if str1[i-1] == str2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				if dp[i-1][j] < dp[i][j-1] {
					dp[i][j] = dp[i-1][j] + 1
				} else {
					dp[i][j] = dp[i][j-1] + 1
				}
			}
		}
	}

	// Reconstruct SCS from dp table
	i, j := n, m
	res := make([]byte, 0, dp[n][m])
	for i > 0 && j > 0 {
		if str1[i-1] == str2[j-1] {
			res = append(res, str1[i-1])
			i--
			j--
		} else if dp[i-1][j] < dp[i][j-1] {
			res = append(res, str1[i-1])
			i--
		} else {
			res = append(res, str2[j-1])
			j--
		}
	}
	for i > 0 {
		res = append(res, str1[i-1])
		i--
	}
	for j > 0 {
		res = append(res, str2[j-1])
		j--
	}

	// reverse the result
	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}
	return string(res)
}
```

## Ruby

```ruby
def shortest_common_supersequence(str1, str2)
  n = str1.length
  m = str2.length
  a1 = str1.bytes
  a2 = str2.bytes

  dp = Array.new(n + 1) { Array.new(m + 1, 0) }
  (0..n).each { |i| dp[i][0] = i }
  (0..m).each { |j| dp[0][j] = j }

  (1..n).each do |i|
    (1..m).each do |j|
      if a1[i - 1] == a2[j - 1]
        dp[i][j] = dp[i - 1][j - 1] + 1
      else
        dp[i][j] = [dp[i - 1][j], dp[i][j - 1]].min + 1
      end
    end
  end

  i = n
  j = m
  res = []

  while i > 0 && j > 0
    if a1[i - 1] == a2[j - 1]
      res << a1[i - 1]
      i -= 1
      j -= 1
    else
      if dp[i - 1][j] < dp[i][j - 1]
        res << a1[i - 1]
        i -= 1
      else
        res << a2[j - 1]
        j -= 1
      end
    end
  end

  while i > 0
    res << a1[i - 1]
    i -= 1
  end

  while j > 0
    res << a2[j - 1]
    j -= 1
  end

  res.reverse.pack('C*')
end
```

## Scala

```scala
object Solution {
  def shortestCommonSupersequence(str1: String, str2: String): String = {
    val n = str1.length
    val m = str2.length
    val dp = Array.ofDim[Int](n + 1, m + 1)

    var i = 0
    while (i <= n) { dp(i)(0) = i; i += 1 }
    var j = 0
    while (j <= m) { dp(0)(j) = j; j += 1 }

    i = 1
    while (i <= n) {
      j = 1
      while (j <= m) {
        if (str1.charAt(i - 1) == str2.charAt(j - 1))
          dp(i)(j) = dp(i - 1)(j - 1) + 1
        else
          dp(i)(j) = math.min(dp(i - 1)(j), dp(i)(j - 1)) + 1
        j += 1
      }
      i += 1
    }

    val sb = new StringBuilder
    var ii = n
    var jj = m
    while (ii > 0 && jj > 0) {
      if (str1.charAt(ii - 1) == str2.charAt(jj - 1)) {
        sb.append(str1.charAt(ii - 1))
        ii -= 1
        jj -= 1
      } else if (dp(ii - 1)(jj) < dp(ii)(jj - 1)) {
        sb.append(str1.charAt(ii - 1))
        ii -= 1
      } else {
        sb.append(str2.charAt(jj - 1))
        jj -= 1
      }
    }
    while (ii > 0) { sb.append(str1.charAt(ii - 1)); ii -= 1 }
    while (jj > 0) { sb.append(str2.charAt(jj - 1)); jj -= 1 }

    sb.reverse.toString()
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn shortest_common_supersequence(str1: String, str2: String) -> String {
        let s1 = str1.as_bytes();
        let s2 = str2.as_bytes();
        let n = s1.len();
        let m = s2.len();

        // dp[i][j] = length of SCS for prefixes s1[0..i), s2[0..j)
        let mut dp = vec![vec![0usize; m + 1]; n + 1];
        for i in 0..=n {
            dp[i][0] = i;
        }
        for j in 0..=m {
            dp[0][j] = j;
        }

        for i in 1..=n {
            for j in 1..=m {
                if s1[i - 1] == s2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::cmp::min(dp[i - 1][j], dp[i][j - 1]) + 1;
                }
            }
        }

        // Reconstruct the SCS
        let mut i = n;
        let mut j = m;
        let mut res: Vec<u8> = Vec::with_capacity(dp[n][m]);

        while i > 0 && j > 0 {
            if s1[i - 1] == s2[j - 1] {
                res.push(s1[i - 1]);
                i -= 1;
                j -= 1;
            } else if dp[i - 1][j] < dp[i][j - 1] {
                res.push(s1[i - 1]);
                i -= 1;
            } else {
                res.push(s2[j - 1]);
                j -= 1;
            }
        }

        while i > 0 {
            res.push(s1[i - 1]);
            i -= 1;
        }
        while j > 0 {
            res.push(s2[j - 1]);
            j -= 1;
        }

        res.reverse();
        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (shortest-common-supersequence str1 str2)
  (-> string? string? string?)
  (let* ([n (string-length str1)]
         [m (string-length str2)]
         ;; dp table: (n+1) x (m+1) of integers
         [dp (make-vector (+ n 1))])
    ;; initialize rows
    (for ([i (in-range (+ n 1))])
      (vector-set! dp i (make-vector (+ m 1) 0)))
    ;; base cases
    (for ([i (in-range (+ n 1))])
      (vector-set! (vector-ref dp i) 0 i))
    (for ([j (in-range (+ m 1))])
      (vector-set! (vector-ref dp 0) j j))
    ;; fill DP table
    (for ([i (in-range 1 (add1 n))])
      (let* ([row (vector-ref dp i)]
             [prev-row (vector-ref dp (sub1 i))]
             [c1 (string-ref str1 (sub1 i))])
        (for ([j (in-range 1 (add1 m))])
          (let* ([c2 (string-ref str2 (sub1 j))]
                 [val (if (= c1 c2)
                          (+ 1 (vector-ref prev-row (sub1 j)))
                          (+ 1 (min (vector-ref prev-row j)
                                    (vector-ref row (sub1 j)))) )])
            (vector-set! row j val)))))
    ;; backtrack to build answer
    (let loop ([i n] [j m] [acc '()])
      (cond
        [(and (= i 0) (= j 0)) (list->string acc)]
        [(= i 0)
         (loop i (sub1 j)
               (cons (string-ref str2 (sub1 j)) acc))]
        [(= j 0)
         (loop (sub1 i) j
               (cons (string-ref str1 (sub1 i)) acc))]
        [else
         (let* ([c1 (string-ref str1 (sub1 i))]
                [c2 (string-ref str2 (sub1 j))]
                [dpij (vector-ref (vector-ref dp i) j)]
                [dpi-1j (vector-ref (vector-ref dp (sub1 i)) j)]
                [dpij-1 (vector-ref (vector-ref dp i) (sub1 j))])
           (if (= c1 c2)
               (loop (sub1 i) (sub1 j) (cons c1 acc))
               (if (< dpi-1j dpij-1)
                   (loop (sub1 i) j (cons c1 acc))
                   (loop i (sub1 j) (cons c2 acc)))))))))
```

## Erlang

```erlang
-spec shortest_common_supersequence(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
shortest_common_supersequence(Str1, Str2) ->
    S1List = binary_to_list(Str1),
    S2List = binary_to_list(Str2),
    N = length(S1List),
    M = length(S2List),
    S1Tuple = list_to_tuple(S1List),
    S2Tuple = list_to_tuple(S2List),
    DP = fill_dp(S1Tuple, S2Tuple, N, M),
    ResultList = backtrack(N, M, M, DP, S1Tuple, S2Tuple, []),
    list_to_binary(ResultList).

%% Build DP table where dp[i][j] is length of shortest common supersequence for prefixes i,j
fill_dp(S1T, S2T, N, M) ->
    Size = (N + 1) * (M + 1),
    DP0 = array:new(Size, {default, 0}),
    fill_rows(0, N, M, S1T, S2T, DP0).

fill_rows(I, N, _M, _S1T, _S2T, DP) when I > N ->
    DP;
fill_rows(I, N, M, S1T, S2T, DP) ->
    {DP2, _} = fill_cols(0, I, N, M, S1T, S2T, DP),
    fill_rows(I + 1, N, M, S1T, S2T, DP2).

fill_cols(J, I, _N, M, _S1T, _S2T, DP) when J > M ->
    {DP, ok};
fill_cols(J, I, N, M, S1T, S2T, DP) ->
    Index = I * (M + 1) + J,
    Val =
        case {I, J} of
            {0, _} -> J;
            {_, 0} -> I;
            _ ->
                Char1 = element(I, S1T),
                Char2 = element(J, S2T),
                if Char1 == Char2 ->
                        PrevIdx = (I - 1) * (M + 1) + (J - 1),
                        array:get(PrevIdx, DP) + 1;
                   true ->
                        UpIdx   = (I - 1) * (M + 1) + J,
                        LeftIdx = I * (M + 1) + (J - 1),
                        UpVal   = array:get(UpIdx, DP),
                        LeftVal = array:get(LeftIdx, DP),
                        Min = if UpVal < LeftVal -> UpVal; true -> LeftVal end,
                        Min + 1
                end
        end,
    DP2 = array:set(Index, Val, DP),
    fill_cols(J + 1, I, N, M, S1T, S2T, DP2).

%% Reconstruct one shortest common supersequence using the DP table
backtrack(I, J, M, DP, S1T, S2T, Acc) when I == 0, J == 0 ->
    lists:reverse(Acc);
backtrack(0, J, M, DP, S1T, S2T, Acc) ->
    Char = element(J, S2T),
    backtrack(0, J - 1, M, DP, S1T, S2T, [Char | Acc]);
backtrack(I, 0, M, DP, S1T, S2T, Acc) ->
    Char = element(I, S1T),
    backtrack(I - 1, 0, M, DP, S1T, S2T, [Char | Acc]);
backtrack(I, J, M, DP, S1T, S2T, Acc) ->
    Char1 = element(I, S1T),
    Char2 = element(J, S2T),
    if Char1 == Char2 ->
            backtrack(I - 1, J - 1, M, DP, S1T, S2T, [Char1 | Acc]);
       true ->
            UpIdx   = (I - 1) * (M + 1) + J,
            LeftIdx = I * (M + 1) + (J - 1),
            UpVal   = array:get(UpIdx, DP),
            LeftVal = array:get(LeftIdx, DP),
            if UpVal < LeftVal ->
                    backtrack(I - 1, J, M, DP, S1T, S2T, [Char1 | Acc]);
               true ->
                    backtrack(I, J - 1, M, DP, S1T, S2T, [Char2 | Acc])
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_common_supersequence(str1 :: String.t(), str2 :: String.t()) :: String.t()
  def shortest_common_supersequence(str1, str2) do
    n = byte_size(str1)
    m = byte_size(str2)

    rows = n + 1
    cols = m + 1
    size = rows * cols

    # Initialize DP array with zeros
    dp0 = :array.new(size, default: 0)

    # Fill first row (i = 0)
    dp1 =
      Enum.reduce(0..m, dp0, fn j, acc ->
        :array.set(j, j, acc)
      end)

    # Fill first column (j = 0)
    dp2 =
      Enum.reduce(0..n, dp1, fn i, acc ->
        :array.set(i * cols, i, acc)
      end)

    # Fill the rest of DP table
    dp_filled =
      Enum.reduce(1..n, dp2, fn i, dp_acc ->
        Enum.reduce(1..m, dp_acc, fn j, dp_inner ->
          c1 = :binary.at(str1, i - 1)
          c2 = :binary.at(str2, j - 1)

          idx = i * cols + j

          val =
            if c1 == c2 do
              :array.get((i - 1) * cols + (j - 1), dp_inner) + 1
            else
              up = :array.get((i - 1) * cols + j, dp_inner)
              left = :array.get(i * cols + (j - 1), dp_inner)
              min(up, left) + 1
            end

          :array.set(idx, val, dp_inner)
        end)
      end)

    # Backtrack to build the supersequence
    chars =
      backtrack(n, m, dp_filled, str1, str2, cols, [])

    List.to_string(chars)
  end

  defp backtrack(0, 0, _dp, _s1, _s2, _cols, acc), do: acc

  defp backtrack(i, 0, dp, s1, s2, cols, acc) when i > 0 do
    c = :binary.at(s1, i - 1)
    backtrack(i - 1, 0, dp, s1, s2, cols, [c | acc])
  end

  defp backtrack(0, j, dp, s1, s2, cols, acc) when j > 0 do
    c = :binary.at(s2, j - 1)
    backtrack(0, j - 1, dp, s1, s2, cols, [c | acc])
  end

  defp backtrack(i, j, dp, s1, s2, cols, acc) do
    c1 = :binary.at(s1, i - 1)
    c2 = :binary.at(s2, j - 1)

    if c1 == c2 do
      backtrack(i - 1, j - 1, dp, s1, s2, cols, [c1 | acc])
    else
      up = :array.get((i - 1) * cols + j, dp)
      left = :array.get(i * cols + (j - 1), dp)

      if up < left do
        backtrack(i - 1, j, dp, s1, s2, cols, [c1 | acc])
      else
        backtrack(i, j - 1, dp, s1, s2, cols, [c2 | acc])
      end
    end
  end
end
```
