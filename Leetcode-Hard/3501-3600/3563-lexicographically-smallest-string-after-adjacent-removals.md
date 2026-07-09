# 3563. Lexicographically Smallest String After Adjacent Removals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string lexicographicallySmallestString(string s) {
        int n = s.size();
        auto consecutive = [&](int a, int b)->bool{
            return (a + 1) % 26 == b || (b + 1) % 26 == a;
        };
        // deletable[l][r] : can delete whole substring [l,r]
        vector<vector<char>> del(n, vector<char>(n, false));
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                for (int k = l + 1; k <= r; ++k) {
                    if (!consecutive(s[l] - 'a', s[k] - 'a')) continue;
                    bool left = (k == l + 1) || del[l + 1][k - 1];
                    bool right = (k == r) || del[k + 1][r];
                    if (left && right) {
                        del[l][r] = true;
                        break;
                    }
                }
            }
        }

        const int NONE = 26;
        vector<vector<string>> memo(n + 1, vector<string>(27, "#"));
        function<string(int,int)> dfs = [&](int pos, int prev)->string{
            if (pos == n) return "";
            string &res = memo[pos][prev];
            if (res != "#") return res;
            string best = "~"; // larger than any valid answer
            int cur = s[pos] - 'a';
            // keep current character if allowed
            if (prev == NONE || !consecutive(prev, cur)) {
                string cand = s.substr(pos,1) + dfs(pos + 1, cur);
                if (cand < best) best = cand;
            }
            // delete any deletable interval starting at pos
            for (int end = pos; end < n; ++end) {
                if (del[pos][end]) {
                    string cand = dfs(end + 1, prev);
                    if (cand < best) best = cand;
                }
            }
            res = best;
            return res;
        };

        return dfs(0, NONE);
    }
};
```

## Java

```java
class Solution {
    public String lexicographicallySmallestString(String s) {
        int n = s.length();
        char[] a = s.toCharArray();
        boolean[][] dp = new boolean[n][n];

        // helper to check consecutive letters (circular)
        java.util.function.BiPredicate<Character, Character> consecutive = (x, y) -> {
            int diff = Math.abs(x - y);
            return diff == 1 || diff == 25;
        };

        // substrings of length 2
        for (int i = 0; i + 1 < n; i++) {
            if (consecutive.test(a[i], a[i + 1])) dp[i][i + 1] = true;
        }

        // increasing lengths
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                outer:
                for (int k = i + 1; k <= j; k++) {
                    if (!consecutive.test(a[i], a[k])) continue;
                    boolean left = (i + 1 > k - 1) || dp[i + 1][k - 1];
                    if (!left) continue;
                    boolean right = (k + 1 > j) || dp[k + 1][j];
                    if (right) {
                        dp[i][j] = true;
                        break outer;
                    }
                }
            }
        }

        String[] best = new String[n + 1];
        best[n] = "";
        for (int i = n - 1; i >= 0; i--) {
            // keep current character
            String minStr = a[i] + best[i + 1];
            // try removing any removable substring starting at i
            for (int j = i; j < n; j++) {
                if (dp[i][j]) {
                    String cand = best[j + 1];
                    if (cand.compareTo(minStr) < 0) {
                        minStr = cand;
                    }
                }
            }
            best[i] = minStr;
        }
        return best[0];
    }
}
```

## Python

```python
class Solution(object):
    def lexicographicallySmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # helper to check if two chars are consecutive in circular alphabet
        def consecutive(a, b):
            x = ord(a) - 97
            y = ord(b) - 97
            return (x + 1) % 26 == y or (y + 1) % 26 == x

        # dp[l][r] = True if s[l..r] can be completely removed
        dp = [[False] * n for _ in range(n)]
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                ok = False
                k = l
                while k < r and not ok:
                    if consecutive(s[k], s[k + 1]):
                        left_ok = (k == l) or dp[l][k - 1]
                        right_ok = (k + 2 > r) or dp[k + 2][r]
                        if left_ok and right_ok:
                            ok = True
                            break
                    k += 1
                dp[l][r] = ok

        # best[i]: lexicographically smallest string obtainable from s[i:]
        best = [""] * (n + 1)
        best[n] = ""
        for i in range(n - 1, -1, -1):
            # keep current character
            cur_best = s[i] + best[i + 1]
            # try removing any removable substring starting at i
            j = i
            while j < n:
                if dp[i][j]:
                    cand = best[j + 1]
                    if cand < cur_best:
                        cur_best = cand
                j += 1
            best[i] = cur_best
        return best[0]
```

## Python3

```python
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)

        def consecutive(a: str, b: str) -> bool:
            d = abs(ord(a) - ord(b))
            return d == 1 or d == 25

        # can[i][j] = True if substring s[i..j] can be completely removed
        can = [[False] * n for _ in range(n)]

        # length 2 substrings
        for i in range(n - 1):
            if consecutive(s[i], s[i + 1]):
                can[i][i + 1] = True

        # even lengths >=4
        for length in range(4, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                # outer pair removal
                if consecutive(s[i], s[j]) and (i + 1 > j - 1 or can[i + 1][j - 1]):
                    can[i][j] = True
                    continue
                # split into two removable parts
                for k in range(i, j):
                    if ((k - i + 1) % 2) == 0:  # left part even length
                        left = (i > k) or can[i][k]
                        right = (k + 1 > j) or can[k + 1][j]
                        if left and right:
                            can[i][j] = True
                            break

        # ans[i]: lexicographically smallest string from suffix starting at i
        ans = [""] * (n + 1)
        ans[n] = ""
        for i in range(n - 1, -1, -1):
            best = None
            # option: remove whole suffix if possible
            if can[i][n - 1]:
                best = ""

            # try keeping a character at position j
            for j in range(i, n):
                if j == i or (j > i and can[i][j - 1]):
                    cand = s[j] + ans[j + 1]
                    if best is None or cand < best:
                        best = cand
            ans[i] = best

        return ans[0]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool is_consecutive(char a, char b) {
    int diff = a - b;
    if (diff == 1 || diff == -1) return true;
    if ((a == 'a' && b == 'z') || (a == 'z' && b == 'a')) return true;
    return false;
}

static char* my_strdup(const char *s) {
    size_t len = strlen(s);
    char *p = (char*)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

/* Return the lexicographically smallest string after optimal removals */
char* lexicographicallySmallestString(char* s) {
    int n = (int)strlen(s);
    static bool can[250][250];   // max length is 250

    /* DP to determine if substring [l, r] can be completely removed */
    for (int l = n - 1; l >= 0; --l) {
        for (int r = l; r < n; ++r) {
            bool removable = false;
            for (int k = l + 1; k <= r && !removable; ++k) {
                if (is_consecutive(s[l], s[k])) {
                    bool left  = (l + 1 > k - 1) ? true : can[l + 1][k - 1];
                    bool right = (k + 1 > r)     ? true : can[k + 1][r];
                    if (left && right) removable = true;
                }
            }
            can[l][r] = removable;
        }
    }

    /* DP for minimal suffix strings */
    char *dp[251];               // dp[i] = answer for suffix starting at i
    dp[n] = my_strdup("");      // empty suffix

    for (int i = n - 1; i >= 0; --i) {
        /* Option 1: keep s[i] */
        size_t len_keep = 1 + strlen(dp[i + 1]);
        char *best = (char*)malloc(len_keep + 1);
        best[0] = s[i];
        strcpy(best + 1, dp[i + 1]);

        /* Option 2: delete a removable block starting at i */
        for (int j = i + 1; j < n; ++j) {
            if (is_consecutive(s[i], s[j])) {
                bool inner = (i + 1 > j - 1) ? true : can[i + 1][j - 1];
                if (inner) {
                    char *cand = dp[j + 1];
                    if (strcmp(cand, best) < 0) {
                        free(best);
                        best = my_strdup(cand);
                    }
                }
            }
        }

        dp[i] = best;
    }

    /* Result is dp[0]; other allocated strings can be freed if desired */
    return dp[0];
}
```

## Csharp

```csharp
using System;

public class Solution {
    public string LexicographicallySmallestString(string s) {
        int n = s.Length;
        if (n == 0) return "";
        bool[,] dp = new bool[n, n];

        // Helper to check consecutive letters in circular alphabet
        bool IsConsecutive(char a, char b) {
            int diff = Math.Abs(a - b);
            return diff == 1 || diff == 25;
        }

        // DP to determine if substring [l..r] can be completely removed
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                bool removable = false;
                // try pairing s[l] with some k
                for (int k = l + 1; k <= r; ++k) {
                    if (!IsConsecutive(s[l], s[k])) continue;

                    bool leftOk = (k == l + 1) || dp[l + 1, k - 1];
                    bool rightOk = (k == r) || dp[k + 1, r];

                    if (leftOk && rightOk) {
                        removable = true;
                        break;
                    }
                }
                dp[l, r] = removable;
            }
        }

        // best[i]: smallest string achievable from suffix starting at i
        string[] best = new string[n + 1];
        best[n] = "";
        for (int i = n - 1; i >= 0; --i) {
            string cur = s[i] + best[i + 1]; // keep current character

            for (int j = i; j < n; ++j) {
                if (dp[i, j]) {
                    string cand = best[j + 1];
                    if (String.Compare(cand, cur, StringComparison.Ordinal) < 0) {
                        cur = cand;
                    }
                }
            }

            best[i] = cur;
        }

        return best[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var lexicographicallySmallestString = function(s) {
    const n = s.length;
    if (n === 0) return "";
    // helper to check circular consecutive letters
    const isConsecutive = (a, b) => {
        const diff = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
        return diff === 1 || diff === 25; // a-z are consecutive
    };
    // can[i][j] true if substring s[i..j] can be completely removed
    const can = Array.from({ length: n }, () => Array(n).fill(false));
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len - 1 < n; ++i) {
            const j = i + len - 1;
            // try to pair s[i] with some k, making the rest removable
            for (let k = i + 1; k <= j; ++k) {
                if (!isConsecutive(s[i], s[k])) continue;
                const leftRemovable = (k === i + 1) || can[i + 1][k - 1];
                const rightRemovable = (k === j) || can[k + 1][j];
                if (leftRemovable && rightRemovable) {
                    can[i][j] = true;
                    break;
                }
            }
        }
    }
    // dpAns[i]: lexicographically smallest string obtainable from suffix i..n-1
    const dpAns = Array(n + 1).fill("");
    dpAns[n] = "";
    for (let i = n - 1; i >= 0; --i) {
        let best = s[i] + dpAns[i + 1]; // keep current character
        // try deleting a removable segment starting at i
        for (let j = i + 1; j < n; ++j) {
            if (can[i][j]) {
                const candidate = dpAns[j + 1];
                if (candidate < best) best = candidate;
            }
        }
        // also possible to delete nothing (empty segment) which is already covered by keep case
        dpAns[i] = best;
    }
    return dpAns[0];
};
```

## Typescript

```typescript
function lexicographicallySmallestString(s: string): string {
    const n = s.length;
    const chars = s.split('');
    const isConsecutive = (a: string, b: string): boolean => {
        const diff = Math.abs(a.charCodeAt(0) - b.charCodeAt(0));
        return diff === 1 || diff === 25; // 'a' and 'z' are consecutive
    };

    const dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));

    for (let len = 2; len <= n; ++len) {
        for (let l = 0; l + len - 1 < n; ++l) {
            const r = l + len - 1;
            let removable = false;
            for (let m = l + 1; m <= r; ++m) {
                if (!isConsecutive(chars[l], chars[m])) continue;
                const left = l + 1 > m - 1 ? true : dp[l + 1][m - 1];
                if (!left) continue;
                const right = m + 1 > r ? true : dp[m + 1][r];
                if (right) {
                    removable = true;
                    break;
                }
            }
            dp[l][r] = removable;
        }
    }

    const ans: string[] = Array(n + 1).fill('');
    ans[n] = '';
    for (let i = n - 1; i >= 0; --i) {
        let best: string | null = null;

        if (dp[i][n - 1]) {
            best = "";
        }

        for (let j = i; j < n; ++j) {
            const removable = j === i ? true : dp[i][j - 1];
            if (!removable) continue;
            const cand = chars[j] + ans[j + 1];
            if (best === null || cand < best) {
                best = cand;
            }
        }

        ans[i] = best !== null ? best : "";
    }

    return ans[0];
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function lexicographicallySmallestString($s) {
        $n = strlen($s);
        if ($n == 0) return "";
        // dp[i][j] true if substring s[i..j] can be completely removed
        $dp = array_fill(0, $n, array_fill(0, $n, false));
        // helper closure for consecutive (circular)
        $isConsecutive = function($a, $b) {
            $oa = ord($a);
            $ob = ord($b);
            if (abs($oa - $ob) == 1) return true;
            if (($a === 'a' && $b === 'z') || ($a === 'z' && $b === 'a')) return true;
            return false;
        };
        // Build dp by increasing length
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i + $len - 1 < $n; $i++) {
                $j = $i + $len - 1;
                // direct removal of outer pair after inner removed
                if ($isConsecutive($s[$i], $s[$j])) {
                    if ($i + 1 > $j - 1 || $dp[$i + 1][$j - 1]) {
                        $dp[$i][$j] = true;
                        continue;
                    }
                }
                // split into two removable parts
                for ($k = $i; $k < $j; $k++) {
                    if ($dp[$i][$k] && $dp[$k + 1][$j]) {
                        $dp[$i][$j] = true;
                        break;
                    }
                }
            }
        }
        // best[i]: lexicographically smallest string obtainable from suffix starting at i
        $best = array_fill(0, $n + 1, "");
        $best[$n] = "";
        for ($i = $n - 1; $i >= 0; $i--) {
            $candidate = null;
            // option: delete whole suffix if removable
            if ($dp[$i][$n - 1]) {
                $candidate = "";
            }
            // try keeping a character at position j (j >= i)
            for ($j = $i; $j < $n; $j++) {
                // prefix [i, j-1] must be removable (or empty)
                if ($j == $i || $dp[$i][$j - 1]) {
                    $cur = $s[$j] . $best[$j + 1];
                    if ($candidate === null || strcmp($cur, $candidate) < 0) {
                        $candidate = $cur;
                    }
                }
            }
            // $candidate is guaranteed to be set
            $best[$i] = $candidate;
        }
        return $best[0];
    }
}
```

## Swift

```swift
class Solution {
    func lexicographicallySmallestString(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return "" }
        
        // Helper to get alphabet index 0..25
        func idx(_ c: Character) -> Int {
            return Int(c.unicodeScalars.first!.value - UnicodeScalar("a").value)
        }
        // Check if two letters are consecutive in circular alphabet
        func isConsecutive(_ a: Character, _ b: Character) -> Bool {
            let d = abs(idx(a) - idx(b))
            return d == 1 || d == 25
        }
        
        var dp = Array(repeating: Array(repeating: false, count: n), count: n)
        // DP for removable substrings
        if n >= 2 {
            for len in 1...n {
                for l in 0...(n - len) {
                    let r = l + len - 1
                    var removable = false
                    // Try to pair chars[l] with some m (l < m <= r)
                    if len >= 2 {
                        for m in (l + 1)...r where isConsecutive(chars[l], chars[m]) {
                            let leftInner = (l + 1 <= m - 1) ? dp[l + 1][m - 1] : true
                            let rightPart = (m + 1 <= r) ? dp[m + 1][r] : true
                            if leftInner && rightPart {
                                removable = true
                                break
                            }
                        }
                    }
                    // Try to split into two removable parts
                    if !removable {
                        for k in l..<r {
                            if dp[l][k] && dp[k + 1][r] {
                                removable = true
                                break
                            }
                        }
                    }
                    dp[l][r] = removable
                }
            }
        }
        
        // DP for minimal lexicographic result from position i to end
        var best = Array(repeating: "", count: n + 1)
        best[n] = ""
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                var curBest: String? = nil
                // Option: delete everything from i if removable
                if dp[i][n - 1] {
                    curBest = ""
                }
                // Try to keep a character at position j after removing prefix [i, j-1]
                for j in i..<n {
                    let prefixRemovable: Bool = (i > j - 1) ? true : dp[i][j - 1]
                    if prefixRemovable {
                        let candidate = String(chars[j]) + best[j + 1]
                        if curBest == nil || candidate < curBest! {
                            curBest = candidate
                        }
                    }
                }
                best[i] = curBest ?? ""
            }
        }
        return best[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lexicographicallySmallestString(s: String): String {
        val n = s.length
        val chars = s.toCharArray()
        // dp[l][r] true if substring [l, r] can be completely removed
        val dp = Array(n) { BooleanArray(n) }
        fun isConsecutive(a: Char, b: Char): Boolean {
            val diff = kotlin.math.abs(a - b)
            return diff == 1 || diff == 25 // 'a' and 'z' are consecutive
        }
        var len = 2
        while (len <= n) {
            var l = 0
            while (l + len <= n) {
                val r = l + len - 1
                var possible = false
                var k = l + 1
                // k must make the segment [l, k] even length => (k - l) odd
                while (k <= r && !possible) {
                    if (isConsecutive(chars[l], chars[k])) {
                        val leftOk = if (k == l + 1) true else dp[l + 1][k - 1]
                        val rightOk = if (k == r) true else dp[k + 1][r]
                        if (leftOk && rightOk) possible = true
                    }
                    k += 2 // keep (k - l) odd
                }
                dp[l][r] = possible
                l++
            }
            len += 2
        }

        val ans = Array(n + 1) { "" }
        for (i in n - 1 downTo 0) {
            var best = chars[i] + ans[i + 1]
            var j = i + 1
            while (j < n) {
                if (dp[i][j]) {
                    val cand = ans[j + 1]
                    if (cand < best) best = cand
                }
                j++
            }
            ans[i] = best
        }
        return ans[0]
    }
}
```

## Dart

```dart
class Solution {
  String lexicographicallySmallestString(String s) {
    int n = s.length;
    List<int> chars = s.codeUnits;

    bool consecutive(int a, int b) {
      if ((a - b).abs() == 1) return true;
      // 'a' (97) and 'z' (122) are consecutive in circular alphabet
      return (a == 97 && b == 122) || (a == 122 && b == 97);
    }

    // dp[l][r] = true if substring s[l..r] can be completely removed
    List<List<bool>> dp = List.generate(n, (_) => List.filled(n, false));

    for (int len = 2; len <= n; ++len) {
      for (int l = 0; l + len - 1 < n; ++l) {
        int r = l + len - 1;
        bool removable = false;

        // split into two removable parts
        for (int m = l; m < r && !removable; ++m) {
          if (dp[l][m] && dp[m + 1][r]) removable = true;
        }

        // pair first character with some k after removing interior
        if (!removable) {
          for (int k = l + 1; k <= r && !removable; ++k) {
            if (consecutive(chars[l], chars[k])) {
              bool left = (k == l + 1) ? true : dp[l + 1][k - 1];
              bool right = (k == r) ? true : dp[k + 1][r];
              if (left && right) removable = true;
            }
          }
        }

        dp[l][r] = removable;
      }
    }

    // ans[i] = lexicographically smallest string from suffix starting at i
    List<String> ans = List.filled(n + 1, '');
    ans[n] = '';
    for (int i = n - 1; i >= 0; --i) {
      String? best;

      // option: remove the whole suffix if possible
      if (dp[i][n - 1]) best = '';

      for (int j = i; j < n; ++j) {
        bool prefixRemovable = (j == i) ? true : dp[i][j - 1];
        if (!prefixRemovable) continue;
        String candidate = s[j] + ans[j + 1];
        if (best == null || candidate.compareTo(best) < 0) best = candidate;
      }

      ans[i] = best!;
    }

    return ans[0];
  }
}
```

## Golang

```go
func isConsecutive(a, b byte) bool {
	diff := (int(a) - int(b) + 26) % 26
	return diff == 1 || diff == 25
}

func lexicographicallySmallestString(s string) string {
	n := len(s)
	if n == 0 {
		return ""
	}
	b := []byte(s)

	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
	}

	for length := 2; length <= n; length++ {
		for l := 0; l+length-1 < n; l++ {
			r := l + length - 1
			found := false

			// partition into two removable parts
			for k := l; k < r && !found; k++ {
				if dp[l][k] && dp[k+1][r] {
					found = true
				}
			}
			if found {
				dp[l][r] = true
				continue
			}

			// pair first character with a later one
			for i := l + 1; i <= r; i++ {
				if isConsecutive(b[l], b[i]) {
					leftRemovable := (l+1 > i-1) || dp[l+1][i-1]
					rightRemovable := (i+1 > r) || dp[i+1][r]
					if leftRemovable && rightRemovable {
						found = true
						break
					}
				}
			}
			dp[l][r] = found
		}
	}

	ans := make([]string, n+1)
	ans[n] = ""
	for i := n - 1; i >= 0; i-- {
		best := string(b[i]) + ans[i+1]
		for j := i; j < n; j++ {
			if dp[i][j] {
				cand := ans[j+1]
				if cand < best {
					best = cand
				}
			}
		}
		ans[i] = best
	}
	return ans[0]
}
```

## Ruby

```ruby
def lexicographically_smallest_string(s)
  n = s.length
  return "" if n == 0

  # helper to check circular consecutive letters
  consecutive = lambda do |a, b|
    diff = (a.ord - b.ord).abs
    diff == 1 || diff == 25
  end

  dp = Array.new(n) { Array.new(n, false) }

  # DP for removable substrings
  (2..n).each do |len|
    (0..n - len).each do |l|
      r = l + len - 1
      (l + 1..r).each do |k|
        if consecutive.call(s[l], s[k])
          left_ok = (l + 1 > k - 1) || dp[l + 1][k - 1]
          right_ok = (k + 1 > r) || dp[k + 1][r]
          if left_ok && right_ok
            dp[l][r] = true
            break
          end
        end
      end
    end
  end

  ans = Array.new(n + 1, "")
  ans[n] = ""

  (n - 1).downto(0) do |i|
    best = nil
    # option: remove everything from i to end if possible
    best = "" if dp[i][n - 1]

    (i...n).each do |j|
      prefix_removable = (i > j - 1) || dp[i][j - 1]
      next unless prefix_removable

      candidate = s[j] + ans[j + 1]
      best = candidate if best.nil? || candidate < best
    end

    ans[i] = best
  end

  ans[0]
end
```

## Scala

```scala
object Solution {
  def lexicographicallySmallestString(s: String): String = {
    val n = s.length
    if (n == 0) return ""
    val chars = s.toCharArray

    def isConsecutive(a: Char, b: Char): Boolean = {
      val diff = Math.abs(a - b)
      diff == 1 || diff == 25 // 'a' and 'z'
    }

    // rem[l][r] true if substring s[l..r] can be completely removed
    val rem = Array.ofDim[Boolean](n, n)

    for (len <- 0 until n) {
      for (l <- 0 to n - len - 1) {
        val r = l + len
        var ok = false

        // split into two removable parts
        var k = l
        while (!ok && k < r) {
          if (rem(l)(k) && rem(k + 1)(r)) ok = true
          k += 1
        }

        // pair first character with some m
        var m = l + 1
        while (!ok && m <= r) {
          if (isConsecutive(chars(l), chars(m))) {
            val leftOk = if (m == l + 1) true else rem(l + 1)(m - 1)
            val rightOk = if (m == r) true else rem(m + 1)(r)
            if (leftOk && rightOk) ok = true
          }
          m += 1
        }

        rem(l)(r) = ok
      }
    }

    // dp[i] = lexicographically smallest string from i to end
    val dp = Array.fill[String](n + 1)("")
    dp(n) = ""

    for (i <- n - 1 to 0 by -1) {
      var best: String = null

      // option: remove entire suffix if possible
      if (rem(i)(n - 1)) best = ""

      for (j <- i until n) {
        val prefixRemovable = if (j == i) true else rem(i)(j - 1)
        if (prefixRemovable) {
          val cand = chars(j).toString + dp(j + 1)
          if (best == null || cand < best) best = cand
        }
      }

      dp(i) = if (best == null) "" else best
    }

    dp(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn lexicographically_smallest_string(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return String::new();
        }
        // dp[l][r] true if substring [l, r] can be completely removed
        let mut dp = vec![vec![false; n]; n];
        // helper to check consecutive (circular)
        fn consecutive(a: u8, b: u8) -> bool {
            (a + 1 == b) || (b + 1 == a) ||
            (a == b'Z' && b == b'A') || (a == b'A' && b == b'Z')
        }
        // Since letters are lowercase, handle wrap between 'z' and 'a'
        fn is_consecutive(a: u8, b: u8) -> bool {
            (a + 1 == b) || (b + 1 == a) ||
            (a == b'z' && b == b'a') || (a == b'a' && b == b'z')
        }
        // Compute dp for even lengths
        for len in (2..=n).step_by(2) {
            for l in 0..=n - len {
                let r = l + len - 1;
                let mut ok = false;
                for k in (l + 1)..=r {
                    if is_consecutive(bytes[l], bytes[k]) {
                        let left_ok = if k == l + 1 { true } else { dp[l + 1][k - 1] };
                        let right_ok = if k == r { true } else { dp[k + 1][r] };
                        if left_ok && right_ok {
                            ok = true;
                            break;
                        }
                    }
                }
                dp[l][r] = ok;
            }
        }

        // ans[i]: lexicographically smallest string from suffix i
        let mut ans: Vec<String> = vec![String::new(); n + 1];
        for i in (0..n).rev() {
            // option: keep current character
            let mut best = {
                let mut cur = String::new();
                cur.push(bytes[i] as char);
                cur.push_str(&ans[i + 1]);
                cur
            };
            // options: delete a removable substring starting at i
            for j in i..n {
                if dp[i][j] {
                    let cand = &ans[j + 1];
                    if cand < &best {
                        best = cand.clone();
                    }
                }
            }
            ans[i] = best;
        }
        ans[0].clone()
    }
}
```

## Racket

```racket
(define/contract (lexicographically-smallest-string s)
  (-> string? string?)
  (let* ((n (string-length s))
         ;; dp[l][r] = #t if substring s[l..r] can be completely removed
         (dp (make-vector n)))
    ;; initialize dp matrix
    (for ([i n])
      (vector-set! dp i (make-vector n #f)))
    ;; helper: are two chars consecutive in circular alphabet?
    (define (consecutive? c1 c2)
      (let ((diff (modulo (- (char->integer c1) (char->integer c2)) 26)))
        (or (= diff 1) (= diff 25))))
    ;; interval DP
    (for ([len (in-range 2 (add1 n))])
      (for ([l (in-range 0 (add1 (- n len)))])
        (let ((r (+ l len -1))
              (found #f))
          (for ([m (in-range (add1 l) (add1 r))]
                #:when (not found))
            (when (and (consecutive? (string-ref s l) (string-ref s m))
                       (let ((left  (if (= m (add1 l)) #t
                                        (vector-ref (vector-ref dp (add1 l)) (- m 1))))
                             (right (if (= m r) #t
                                        (vector-ref (vector-ref dp (add1 m)) r)))
                         )
                         (and left right)))
              (set! found #t)
              (vector-set! (vector-ref dp l) r #t))))))

    ;; ans[i] = lexicographically smallest string obtainable from suffix i..n-1
    (define ans (make-vector (add1 n) ""))
    (for ([i (in-range (sub1 n) -1 -1)])
      (let ((best #f))
        ;; whole suffix removable -> empty string candidate
        (when (and (< i n)
                   (vector-ref (vector-ref dp i) (sub1 n)))
          (set! best ""))
        ;; try keeping a character at position j after removing prefix [i, j-1]
        (for ([j (in-range i (add1 n))])
          (let ((prefix-removable
                 (if (= i j)
                     #t
                     (vector-ref (vector-ref dp i) (- j 1)))))
            (when prefix-removable
              (let* ((c (string (string-ref s j)))
                     (candidate (string-append c (vector-ref ans (add1 j)))))
                (when (or (not best) (string<? candidate best))
                  (set! best candidate))))))
        (vector-set! ans i (or best ""))))
    (vector-ref ans 0)))
```

## Erlang

```erlang
-spec lexicographically_smallest_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
lexicographically_smallest_string(S) ->
    Chars = binary_to_list(S),
    N = length(Chars),
    Rem = removable_dp(Chars, N, #{}),
    ResultList = build_ans(N, Chars, Rem, #{N => []}),
    list_to_binary(ResultList).

%% DP for deletable substrings
removable_dp(_Chars, 0, Map) -> Map;
removable_dp(Chars, N, Map0) ->
    removable_len(2, N, Chars, Map0).

removable_len(Len, MaxLen, _Chars, Map) when Len > MaxLen ->
    Map;
removable_len(Len, MaxLen, Chars, Map0) ->
    Map1 = removable_for_len(Len, length(Chars), 0, Len, Chars, Map0),
    removable_len(Len + 1, MaxLen, Chars, Map1).

removable_for_len(_Len, N, L, _LenVal, _Chars, Map) when L > N - _Len ->
    Map;
removable_for_len(Len, N, L, LenVal, Chars, Map0) ->
    R = L + Len - 1,
    Removable = removable_check(L, R, Chars, Map0),
    Map1 = case Removable of
        true -> maps:put({L,R}, true, Map0);
        false -> Map0
    end,
    removable_for_len(Len, N, L + 1, LenVal, Chars, Map1).

removable_check(L, R, Chars, Map) ->
    removable_check_k(L+1, R, L, R, Chars, Map).

removable_check_k(K, R, _L, _R, _Chars, _Map) when K > R ->
    false;
removable_check_k(K, R, L, R, Chars, Map) ->
    CharL = lists:nth(L+1, Chars),
    CharK = lists:nth(K+1, Chars),
    case consecutive(CharL, CharK) of
        true ->
            case is_rem(L+1, K-1, Map) andalso is_rem(K+1, R, Map) of
                true -> true;
                false -> removable_check_k(K+1, R, L, R, Chars, Map)
            end;
        false ->
            removable_check_k(K+1, R, L, R, Chars, Map)
    end.

consecutive(A, B) ->
    Diff = abs(A - B),
    Diff == 1 orelse Diff == 25.

is_rem(L, R, _Map) when L > R -> true;
is_rem(L, R, Map) -> maps:get({L,R}, Map, false).

%% Build answer using DP for smallest lexicographic string
build_ans(N, Chars, Rem, AnsMap) ->
    build_ans_i(N-1, N, Chars, Rem, AnsMap).

build_ans_i(-1, _N, _Chars, _Rem, AnsMap) ->
    maps:get(0, AnsMap);
build_ans_i(I, N, Chars, Rem, AnsMap) ->
    Best = find_best(I, N-1, Chars, Rem, AnsMap),
    NewMap = maps:put(I, Best, AnsMap),
    build_ans_i(I-1, N, Chars, Rem, NewMap).

find_best(I, MaxIdx, Chars, Rem, AnsMap) ->
    Initial = case is_rem(I, MaxIdx, Rem) of
        true -> [];
        false -> undefined
    end,
    find_best_loop(I, I, MaxIdx, Chars, Rem, AnsMap, Initial).

find_best_loop(_I, J, MaxIdx, _Chars, _Rem, _AnsMap, Best) when J > MaxIdx ->
    Best;
find_best_loop(I, J, MaxIdx, Chars, Rem, AnsMap, Best) ->
    PrefixRem = is_rem(I, J-1, Rem),
    NewBest = case PrefixRem of
        true ->
            CharJ = lists:nth(J+1, Chars),
            Rest = maps:get(J+1, AnsMap),
            Cand = [CharJ | Rest],
            case Best of
                undefined -> Cand;
                _ -> if less(Cand, Best) -> Cand; true -> Best end
            end;
        false ->
            Best
    end,
    find_best_loop(I, J+1, MaxIdx, Chars, Rem, AnsMap, NewBest).

less([], [_|_]) -> true;
less([_|_], []) -> false;
less([X|Xs], [Y|Ys]) ->
    if X < Y -> true;
       X > Y -> false;
       true -> less(Xs, Ys)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec lexicographically_smallest_string(s :: String.t) :: String.t
  def lexicographically_smallest_string(s) do
    chars = String.graphemes(s)
    n = length(chars)

    dp = build_removable(chars, n)
    ans_map = build_answer(chars, n, dp)

    Map.get(ans_map, 0, "")
  end

  defp build_removable(chars, n) do
    Enum.reduce(2..n, %{}, fn len, acc ->
      Enum.reduce(0..(n - len), acc, fn l, acc2 ->
        r = l + len - 1

        removable =
          Enum.any?((l + 1)..r, fn k ->
            consecutive?(Enum.at(chars, l), Enum.at(chars, k)) and
              ((l + 1 > k - 1) or Map.get(acc2, {l + 1, k - 1}, false)) and
              ((k + 1 > r) or Map.get(acc2, {k + 1, r}, false))
          end)

        if removable, do: Map.put(acc2, {l, r}, true), else: acc2
      end)
    end)
  end

  defp build_answer(chars, n, dp) do
    Enum.reduce((n - 1)..0, %{n => ""}, fn i, ans_map ->
      candidates = []

      candidates =
        if Map.get(dp, {i, n - 1}, false) do
          ["" | candidates]
        else
          candidates
        end

      candidates =
        Enum.reduce(i..(n - 1), candidates, fn j, acc ->
          prefix_removable =
            if i > j - 1,
              do: true,
              else: Map.get(dp, {i, j - 1}, false)

          if prefix_removable do
            rest = Map.fetch!(ans_map, j + 1)
            [Enum.at(chars, j) <> rest | acc]
          else
            acc
          end
        end)

      min_str =
        case candidates do
          [] -> ""
          _ -> Enum.min(candidates)
        end

      Map.put(ans_map, i, min_str)
    end)
  end

  defp consecutive?(c1, c2) do
    a = :binary.first(c1)
    b = :binary.first(c2)
    d = abs(a - b)
    d == 1 or d == 25
  end
end
```
