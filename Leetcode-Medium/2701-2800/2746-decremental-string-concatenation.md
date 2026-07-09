# 2746. Decremental String Concatenation

## Cpp

```cpp
class Solution {
public:
    int minimizeConcatenatedLength(vector<string>& words) {
        const int INF = 1e9;
        vector<vector<int>> cur(26, vector<int>(26, INF));
        auto init = [&](const string& s){
            int f = s.front() - 'a';
            int l = s.back() - 'a';
            cur[f][l] = (int)s.size();
        };
        init(words[0]);
        for (size_t i = 1; i < words.size(); ++i) {
            const string& w = words[i];
            int wf = w.front() - 'a';
            int wl = w.back() - 'a';
            int wlen = (int)w.size();
            vector<vector<int>> nxt(26, vector<int>(26, INF));
            for (int f = 0; f < 26; ++f) {
                for (int l = 0; l < 26; ++l) {
                    int curLen = cur[f][l];
                    if (curLen == INF) continue;
                    // append w to the right
                    int incRight = (l == wf) ? wlen - 1 : wlen;
                    int nf = f, nl = wl;
                    nxt[nf][nl] = min(nxt[nf][nl], curLen + incRight);
                    // prepend w to the left
                    int incLeft = (wl == f) ? wlen - 1 : wlen;
                    nf = wf; nl = l;
                    nxt[nf][nl] = min(nxt[nf][nl], curLen + incLeft);
                }
            }
            cur.swap(nxt);
        }
        int ans = INF;
        for (int f = 0; f < 26; ++f)
            for (int l = 0; l < 26; ++l)
                ans = min(ans, cur[f][l]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimizeConcatenatedLength(String[] words) {
        final int INF = 1_000_000_000;
        int[][] cur = new int[26][26];
        for (int i = 0; i < 26; i++) {
            java.util.Arrays.fill(cur[i], INF);
        }
        String firstWord = words[0];
        int fIdx = firstWord.charAt(0) - 'a';
        int lIdx = firstWord.charAt(firstWord.length() - 1) - 'a';
        cur[fIdx][lIdx] = firstWord.length();

        for (int i = 1; i < words.length; i++) {
            String w = words[i];
            int wLen = w.length();
            int wFirst = w.charAt(0) - 'a';
            int wLast = w.charAt(wLen - 1) - 'a';

            int[][] nxt = new int[26][26];
            for (int a = 0; a < 26; a++) {
                java.util.Arrays.fill(nxt[a], INF);
            }

            for (int f = 0; f < 26; f++) {
                for (int l = 0; l < 26; l++) {
                    int curLen = cur[f][l];
                    if (curLen == INF) continue;

                    // Append w to the right
                    int overlapAppend = (l == wFirst) ? 1 : 0;
                    int newLenAppend = curLen + wLen - overlapAppend;
                    int nfAppend = f;
                    int nlAppend = wLast;
                    if (newLenAppend < nxt[nfAppend][nlAppend]) {
                        nxt[nfAppend][nlAppend] = newLenAppend;
                    }

                    // Prepend w to the left
                    int overlapPrepend = (wLast == f) ? 1 : 0;
                    int newLenPrepend = curLen + wLen - overlapPrepend;
                    int nfPrepend = wFirst;
                    int nlPrepend = l;
                    if (newLenPrepend < nxt[nfPrepend][nlPrepend]) {
                        nxt[nfPrepend][nlPrepend] = newLenPrepend;
                    }
                }
            }
            cur = nxt;
        }

        int answer = INF;
        for (int f = 0; f < 26; f++) {
            for (int l = 0; l < 26; l++) {
                if (cur[f][l] < answer) answer = cur[f][l];
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeConcatenatedLength(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        INF = 10**9
        # dp[first][last] = minimal length after processing current prefix
        dp = [[INF] * 26 for _ in range(26)]
        first0 = ord(words[0][0]) - 97
        last0 = ord(words[0][-1]) - 97
        dp[first0][last0] = len(words[0])

        for i in range(1, len(words)):
            w = words[i]
            wf = ord(w[0]) - 97
            wl = ord(w[-1]) - 97
            lw = len(w)
            newdp = [[INF] * 26 for _ in range(26)]
            for f in range(26):
                row = dp[f]
                for l in range(26):
                    cur_len = row[l]
                    if cur_len == INF:
                        continue
                    # option 1: current string then w
                    add1 = lw - (1 if l == wf else 0)
                    nf1, nl1 = f, wl
                    nd1 = cur_len + add1
                    if nd1 < newdp[nf1][nl1]:
                        newdp[nf1][nl1] = nd1
                    # option 2: w then current string
                    add2 = lw - (1 if wl == f else 0)
                    nf2, nl2 = wf, l
                    nd2 = cur_len + add2
                    if nd2 < newdp[nf2][nl2]:
                        newdp[nf2][nl2] = nd2
            dp = newdp

        ans = INF
        for f in range(26):
            for l in range(26):
                if dp[f][l] < ans:
                    ans = dp[f][l]
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        INF = 10 ** 9
        dp = [[INF] * 26 for _ in range(26)]
        f0 = ord(words[0][0]) - 97
        l0 = ord(words[0][-1]) - 97
        dp[f0][l0] = len(words[0])
        for w in words[1:]:
            wf = ord(w[0]) - 97
            wl = ord(w[-1]) - 97
            wlen = len(w)
            ndp = [[INF] * 26 for _ in range(26)]
            for f in range(26):
                row = dp[f]
                for l in range(26):
                    cur = row[l]
                    if cur == INF:
                        continue
                    # cur + w
                    add1 = wlen - (1 if l == wf else 0)
                    nf, nl = f, wl
                    new_len = cur + add1
                    if new_len < ndp[nf][nl]:
                        ndp[nf][nl] = new_len
                    # w + cur
                    add2 = wlen - (1 if wl == f else 0)
                    nf2, nl2 = wf, l
                    new_len2 = cur + add2
                    if new_len2 < ndp[nf2][nl2]:
                        ndp[nf2][nl2] = new_len2
            dp = ndp
        ans = INF
        for f in range(26):
            for l in range(26):
                if dp[f][l] < ans:
                    ans = dp[f][l]
        return ans
```

## C

```c
#include <string.h>
#include <limits.h>

int minimizeConcatenatedLength(char** words, int wordsSize) {
    const int INF = 1000000000;
    int dp[26][26];
    for (int i = 0; i < 26; ++i)
        for (int j = 0; j < 26; ++j)
            dp[i][j] = INF;

    // initialize with the first word
    char *w0 = words[0];
    int len0 = strlen(w0);
    int f0 = w0[0] - 'a';
    int l0 = w0[len0 - 1] - 'a';
    dp[f0][l0] = len0;

    // process remaining words
    for (int idx = 1; idx < wordsSize; ++idx) {
        char *w = words[idx];
        int L = strlen(w);
        int f = w[0] - 'a';
        int l = w[L - 1] - 'a';

        int ndp[26][26];
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                ndp[i][j] = INF;

        for (int a = 0; a < 26; ++a) {
            for (int b = 0; b < 26; ++b) {
                if (dp[a][b] == INF) continue;
                // Append w to the right
                int extra = (b == f) ? L - 1 : L;
                int newLen = dp[a][b] + extra;
                int nf = a, nl = l;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;

                // Prepend w to the left
                extra = (l == a) ? L - 1 : L;
                newLen = dp[a][b] + extra;
                nf = f; nl = b;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;
            }
        }

        // copy back
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                dp[i][j] = ndp[i][j];
    }

    int ans = INF;
    for (int a = 0; a < 26; ++a)
        for (int b = 0; b < 26; ++b)
            if (dp[a][b] < ans) ans = dp[a][b];

    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinimizeConcatenatedLength(string[] words) {
        const int ALPH = 26;
        const int INF = int.MaxValue / 2;
        int[,] dp = new int[ALPH, ALPH];
        for (int i = 0; i < ALPH; i++)
            for (int j = 0; j < ALPH; j++)
                dp[i, j] = INF;

        // initialize with first word
        string w0 = words[0];
        int f0 = w0[0] - 'a';
        int l0 = w0[w0.Length - 1] - 'a';
        dp[f0, l0] = w0.Length;

        for (int idx = 1; idx < words.Length; idx++) {
            string w = words[idx];
            int wf = w[0] - 'a';
            int wl = w[w.Length - 1] - 'a';
            int lenW = w.Length;

            int[,] ndp = new int[ALPH, ALPH];
            for (int i = 0; i < ALPH; i++)
                for (int j = 0; j < ALPH; j++)
                    ndp[i, j] = INF;

            for (int f = 0; f < ALPH; f++) {
                for (int l = 0; l < ALPH; l++) {
                    int curLen = dp[f, l];
                    if (curLen == INF) continue;

                    // Append w to the right: join(current, w)
                    int addAppend = lenW - (l == wf ? 1 : 0);
                    int newLenAppend = curLen + addAppend;
                    int nfAppend = f;
                    int nlAppend = wl;
                    if (newLenAppend < ndp[nfAppend, nlAppend])
                        ndp[nfAppend, nlAppend] = newLenAppend;

                    // Prepend w to the left: join(w, current)
                    int addPrepend = lenW - (wl == f ? 1 : 0);
                    int newLenPrepend = curLen + addPrepend;
                    int nfPrepend = wf;
                    int nlPrepend = l;
                    if (newLenPrepend < ndp[nfPrepend, nlPrepend])
                        ndp[nfPrepend, nlPrepend] = newLenPrepend;
                }
            }

            dp = ndp;
        }

        int answer = INF;
        for (int f = 0; f < ALPH; f++) {
            for (int l = 0; l < ALPH; l++) {
                if (dp[f, l] < answer) answer = dp[f, l];
            }
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var minimizeConcatenatedLength = function(words) {
    const INF = 1e9;
    const SZ = 26;
    // dp[first][last] = minimal length
    let dp = Array.from({length: SZ}, () => Array(SZ).fill(INF));
    
    const first0 = words[0].charCodeAt(0) - 97;
    const last0 = words[0].charCodeAt(words[0].length - 1) - 97;
    dp[first0][last0] = words[0].length;
    
    for (let i = 1; i < words.length; ++i) {
        const w = words[i];
        const fw = w.charCodeAt(0) - 97;
        const lw = w.charCodeAt(w.length - 1) - 97;
        const lenW = w.length;
        const ndp = Array.from({length: SZ}, () => Array(SZ).fill(INF));
        
        for (let a = 0; a < SZ; ++a) {
            for (let b = 0; b < SZ; ++b) {
                const cur = dp[a][b];
                if (cur === INF) continue;
                
                // Append w after current string
                let newLen = cur + lenW - (b === fw ? 1 : 0);
                let nf = a, nl = lw;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;
                
                // Prepend w before current string
                newLen = cur + lenW - (lw === a ? 1 : 0);
                nf = fw; nl = b;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;
            }
        }
        dp = ndp;
    }
    
    let ans = INF;
    for (let a = 0; a < SZ; ++a) {
        for (let b = 0; b < SZ; ++b) {
            if (dp[a][b] < ans) ans = dp[a][b];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimizeConcatenatedLength(words: string[]): number {
    const INF = Number.MAX_SAFE_INTEGER;
    const SZ = 26;
    let dp = Array.from({ length: SZ }, () => Array(SZ).fill(INF));
    const firstWord = words[0];
    const f0 = firstWord.charCodeAt(0) - 97;
    const l0 = firstWord.charCodeAt(firstWord.length - 1) - 97;
    dp[f0][l0] = firstWord.length;

    for (let i = 1; i < words.length; ++i) {
        const w = words[i];
        const lenW = w.length;
        const wf = w.charCodeAt(0) - 97;
        const wl = w.charCodeAt(w.length - 1) - 97;

        const ndp = Array.from({ length: SZ }, () => Array(SZ).fill(INF));

        for (let f = 0; f < SZ; ++f) {
            for (let l = 0; l < SZ; ++l) {
                const cur = dp[f][l];
                if (cur === INF) continue;

                // Append w to the right
                let newLen = cur + lenW - (l === wf ? 1 : 0);
                let nf = f;
                let nl = wl;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;

                // Prepend w to the left
                newLen = cur + lenW - (wl === f ? 1 : 0);
                nf = wf;
                nl = l;
                if (newLen < ndp[nf][nl]) ndp[nf][nl] = newLen;
            }
        }

        dp = ndp;
    }

    let ans = INF;
    for (let f = 0; f < SZ; ++f) {
        for (let l = 0; l < SZ; ++l) {
            if (dp[f][l] < ans) ans = dp[f][l];
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    public function minimizeConcatenatedLength($words) {
        $n = count($words);
        if ($n == 0) return 0;
        $INF = PHP_INT_MAX;

        // dp[index] where index = first*26 + last, stores minimal length
        $dp = array_fill(0, 26 * 26, $INF);

        $firstChar = ord($words[0][0]) - 97;
        $lastChar = ord($words[0][strlen($words[0]) - 1]) - 97;
        $len = strlen($words[0]);
        $dp[$firstChar * 26 + $lastChar] = $len;

        for ($i = 1; $i < $n; ++$i) {
            $w = $words[$i];
            $f2 = ord($w[0]) - 97;
            $l2 = ord($w[strlen($w) - 1]) - 97;
            $len2 = strlen($w);

            $ndp = array_fill(0, 26 * 26, $INF);

            for ($idx = 0; $idx < 26 * 26; ++$idx) {
                if ($dp[$idx] === $INF) continue;

                $curLen = $dp[$idx];
                $f = intdiv($idx, 26);
                $l = $idx % 26;

                // Append w to current string
                $newFirst = $f;
                $newLast = $l2;
                $add = ($l == $f2) ? 1 : 0;
                $newLen = $curLen + $len2 - $add;
                $newIdx = $newFirst * 26 + $newLast;
                if ($newLen < $ndp[$newIdx]) {
                    $ndp[$newIdx] = $newLen;
                }

                // Prepend w to current string
                $newFirst = $f2;
                $newLast = $l;
                $add = ($l2 == $f) ? 1 : 0;
                $newLen = $curLen + $len2 - $add;
                $newIdx = $newFirst * 26 + $newLast;
                if ($newLen < $ndp[$newIdx]) {
                    $ndp[$newIdx] = $newLen;
                }
            }

            $dp = $ndp;
        }

        $answer = $INF;
        foreach ($dp as $val) {
            if ($val < $answer) $answer = $val;
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeConcatenatedLength(_ words: [String]) -> Int {
        let INF = Int.max / 4
        let alphabetSize = 26
        
        func charIdx(_ ch: Character) -> Int {
            return Int(ch.unicodeScalars.first!.value - 97)
        }
        
        var dp = Array(repeating: Array(repeating: INF, count: alphabetSize), count: alphabetSize)
        
        // Initialize with the first word
        let firstWord = words[0]
        let fIdx = charIdx(firstWord.first!)
        let lIdx = charIdx(firstWord.last!)
        dp[fIdx][lIdx] = firstWord.count
        
        if words.count == 1 {
            return firstWord.count
        }
        
        // Process remaining words
        for i in 1..<words.count {
            let w = words[i]
            let wf = charIdx(w.first!)
            let wl = charIdx(w.last!)
            let m = w.count
            
            var newDP = Array(repeating: Array(repeating: INF, count: alphabetSize), count: alphabetSize)
            
            for f in 0..<alphabetSize {
                for l in 0..<alphabetSize {
                    let curLen = dp[f][l]
                    if curLen >= INF { continue }
                    
                    // Join current string on the right with w
                    var costRight = curLen + m
                    if l == wf { costRight -= 1 }
                    if costRight < newDP[f][wl] {
                        newDP[f][wl] = costRight
                    }
                    
                    // Join w on the left of current string
                    var costLeft = curLen + m
                    if wf == f { costLeft -= 1 }
                    if costLeft < newDP[wf][l] {
                        newDP[wf][l] = costLeft
                    }
                }
            }
            dp = newDP
        }
        
        var answer = INF
        for f in 0..<alphabetSize {
            for l in 0..<alphabetSize {
                if dp[f][l] < answer {
                    answer = dp[f][l]
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeConcatenatedLength(words: Array<String>): Int {
        val INF = 1_000_000_000
        var dp = Array(26) { IntArray(26) { INF } }
        val first0 = words[0][0] - 'a'
        val last0 = words[0][words[0].length - 1] - 'a'
        dp[first0][last0] = words[0].length
        for (i in 1 until words.size) {
            val w = words[i]
            val wLen = w.length
            val wf = w[0] - 'a'
            val wl = w[wLen - 1] - 'a'
            val newDp = Array(26) { IntArray(26) { INF } }
            for (f in 0 until 26) {
                for (l in 0 until 26) {
                    val cur = dp[f][l]
                    if (cur == INF) continue
                    // prev + w
                    var nLen = cur + wLen - if (l == wf) 1 else 0
                    var nf = f
                    var nl = wl
                    if (nLen < newDp[nf][nl]) newDp[nf][nl] = nLen
                    // w + prev
                    nLen = cur + wLen - if (wl == f) 1 else 0
                    nf = wf
                    nl = l
                    if (nLen < newDp[nf][nl]) newDp[nf][nl] = nLen
                }
            }
            dp = newDp
        }
        var ans = INF
        for (f in 0 until 26) {
            for (l in 0 until 26) {
                if (dp[f][l] < ans) ans = dp[f][l]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimizeConcatenatedLength(List<String> words) {
    const int INF = 1 << 30;
    List<List<int>> dp = List.generate(26, (_) => List.filled(26, INF));
    String firstWord = words[0];
    int fIdx = firstWord.codeUnitAt(0) - 97;
    int lIdx = firstWord.codeUnitAt(firstWord.length - 1) - 97;
    dp[fIdx][lIdx] = firstWord.length;

    for (int i = 1; i < words.length; ++i) {
      String w = words[i];
      int wf = w.codeUnitAt(0) - 97;
      int wl = w.codeUnitAt(w.length - 1) - 97;
      int wlen = w.length;

      List<List<int>> ndp = List.generate(26, (_) => List.filled(26, INF));

      for (int f = 0; f < 26; ++f) {
        for (int l = 0; l < 26; ++l) {
          int cur = dp[f][l];
          if (cur == INF) continue;

          // Append w to the right
          int extraAppend = wlen;
          if (l == wf) extraAppend--;
          int newLenA = cur + extraAppend;
          int nfA = f;
          int nlA = wl;
          if (newLenA < ndp[nfA][nlA]) ndp[nfA][nlA] = newLenA;

          // Prepend w to the left
          int extraPre = wlen;
          if (wl == f) extraPre--;
          int newLenP = cur + extraPre;
          int nfP = wf;
          int nlP = l;
          if (newLenP < ndp[nfP][nlP]) ndp[nfP][nlP] = newLenP;
        }
      }

      dp = ndp;
    }

    int ans = INF;
    for (int f = 0; f < 26; ++f) {
      for (int l = 0; l < 26; ++l) {
        if (dp[f][l] < ans) ans = dp[f][l];
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minimizeConcatenatedLength(words []string) int {
	const INF = int(1e9)
	var dp [26][26]int
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			dp[i][j] = INF
		}
	}
	f0 := int(words[0][0] - 'a')
	l0 := int(words[0][len(words[0])-1] - 'a')
	dp[f0][l0] = len(words[0])

	for idx := 1; idx < len(words); idx++ {
		w := words[idx]
		fw := int(w[0] - 'a')
		lw := int(w[len(w)-1] - 'a')
		wlen := len(w)

		var next [26][26]int
		for i := 0; i < 26; i++ {
			for j := 0; j < 26; j++ {
				next[i][j] = INF
			}
		}

		for f := 0; f < 26; f++ {
			for l := 0; l < 26; l++ {
				cur := dp[f][l]
				if cur == INF {
					continue
				}
				// Append w to the right
				add := wlen
				if l == fw {
					add = wlen - 1
				}
				nf, nl := f, lw
				newLen := cur + add
				if newLen < next[nf][nl] {
					next[nf][nl] = newLen
				}
				// Prepend w to the left
				add2 := wlen
				if lw == f {
					add2 = wlen - 1
				}
				nf2, nl2 := fw, l
				newLen2 := cur + add2
				if newLen2 < next[nf2][nl2] {
					next[nf2][nl2] = newLen2
				}
			}
		}
		dp = next
	}

	ans := INF
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			if dp[i][j] < ans {
				ans = dp[i][j]
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimize_concatenated_length(words)
  n = words.length
  return 0 if n == 0

  # Initialize DP with the first word
  f0 = words[0].getbyte(0) - 97
  l0 = words[0].getbyte(-1) - 97
  dp = { [f0, l0] => words[0].length }

  (1...n).each do |i|
    w = words[i]
    wf = w.getbyte(0) - 97
    wl = w.getbyte(-1) - 97
    lw = w.length

    new_dp = {}

    dp.each do |(first, last), cur_len|
      # Append w to the right
      len_append = cur_len + lw - (last == wf ? 1 : 0)
      key_append = [first, wl]
      if !new_dp.key?(key_append) || len_append < new_dp[key_append]
        new_dp[key_append] = len_append
      end

      # Prepend w to the left
      len_prepend = cur_len + lw - (wf == first ? 1 : 0)
      key_prepend = [wf, last]
      if !new_dp.key?(key_prepend) || len_prepend < new_dp[key_prepend]
        new_dp[key_prepend] = len_prepend
      end
    end

    dp = new_dp
  end

  dp.values.min
end
```

## Scala

```scala
object Solution {
  def minimizeConcatenatedLength(words: Array[String]): Int = {
    val INF = Int.MaxValue / 4
    var dp = Array.fill(26)(Array.fill(26)(INF))

    // initialize with first word
    val firstWord = words(0)
    val f0 = firstWord.head - 'a'
    val l0 = firstWord.last - 'a'
    dp(f0)(l0) = firstWord.length

    for (i <- 1 until words.length) {
      val w = words(i)
      val wf = w.head - 'a'
      val wl = w.last - 'a'
      val wlen = w.length
      val newDp = Array.fill(26)(Array.fill(26)(INF))

      var f = 0
      while (f < 26) {
        var l = 0
        while (l < 26) {
          val cur = dp(f)(l)
          if (cur < INF) {
            // Append w after current string
            val extraAppend = wlen - (if (l == wf) 1 else 0)
            val nfAppend = f
            val nlAppend = wl
            val candAppend = cur + extraAppend
            if (candAppend < newDp(nfAppend)(nlAppend)) {
              newDp(nfAppend)(nlAppend) = candAppend
            }

            // Prepend w before current string
            val extraPrepend = wlen - (if (wl == f) 1 else 0)
            val nfPrepend = wf
            val nlPrepend = l
            val candPrepend = cur + extraPrepend
            if (candPrepend < newDp(nfPrepend)(nlPrepend)) {
              newDp(nfPrepend)(nlPrepend) = candPrepend
            }
          }
          l += 1
        }
        f += 1
      }

      dp = newDp
    }

    var answer = INF
    var f = 0
    while (f < 26) {
      var l = 0
      while (l < 26) {
        if (dp(f)(l) < answer) answer = dp(f)(l)
        l += 1
      }
      f += 1
    }
    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_concatenated_length(words: Vec<String>) -> i32 {
        const INF: i32 = 1_000_000_000;
        let n = words.len();
        if n == 0 {
            return 0;
        }
        // dp[first][last] = minimal length
        let mut dp = vec![vec![INF; 26]; 26];
        let first_word = &words[0];
        let b = first_word.as_bytes();
        let f = (b[0] - b'a') as usize;
        let l = (b[b.len() - 1] - b'a') as usize;
        dp[f][l] = b.len() as i32;

        for idx in 1..n {
            let w = &words[idx];
            let wb = w.as_bytes();
            let wf = (wb[0] - b'a') as usize;
            let wl = (wb[wb.len() - 1] - b'a') as usize;
            let len_w = wb.len() as i32;

            let mut ndp = vec![vec![INF; 26]; 26];
            for fp in 0..26 {
                for lp in 0..26 {
                    let cur_len = dp[fp][lp];
                    if cur_len == INF {
                        continue;
                    }
                    // join(prev, w)
                    let mut cost1 = cur_len + len_w;
                    if lp == wf {
                        cost1 -= 1;
                    }
                    let nf1 = fp;
                    let nl1 = wl;
                    if cost1 < ndp[nf1][nl1] {
                        ndp[nf1][nl1] = cost1;
                    }

                    // join(w, prev)
                    let mut cost2 = cur_len + len_w;
                    if wl == fp {
                        cost2 -= 1;
                    }
                    let nf2 = wf;
                    let nl2 = lp;
                    if cost2 < ndp[nf2][nl2] {
                        ndp[nf2][nl2] = cost2;
                    }
                }
            }
            dp = ndp;
        }

        let mut ans = INF;
        for i in 0..26 {
            for j in 0..26 {
                if dp[i][j] < ans {
                    ans = dp[i][j];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimize-concatenated-length words)
  (-> (listof string?) exact-integer?)
  (let* ([n (length words)]
         [INF 1000000000]
         ;; helper to get char index 0-25
         [char-index (lambda (c) (- (char->integer c) (char->integer #\a)))]
         ;; initialize dp matrix 26x26 with INF
         [make-dp (lambda () (for/vector ([i 26]) (make-vector 26 INF)))]
         [dp0 (make-dp)])
    (if (= n 0)
        0
        (begin
          ;; process first word
          (let* ([w0 (list-ref words 0)]
                 [len0 (string-length w0)]
                 [f0 (char-index (string-ref w0 0))]
                 [l0 (char-index (string-ref w0 (- len0 1)))])
            (vector-set! (vector-ref dp0 f0) l0 len0))
          ;; iterate over remaining words
          (let loop ([i 1] [dp dp0])
            (if (= i n)
                ;; answer: minimum value in dp matrix
                (let min-val INF)
                  (for ([f (in-range 26)]
                        [row (in-vector dp)])
                    (for ([l (in-range 26)])
                      (let ([v (vector-ref row l)])
                        (when (< v min-val) (set! min-val v)))))
                ;; else process word i
                (let* ([w (list-ref words i)]
                       [len-w (string-length w)]
                       [f-w (char-index (string-ref w 0))]
                       [l-w (char-index (string-ref w (- len-w 1)))]
                       [dp2 (make-dp)])
                  (for ([f (in-range 26)]
                        [row (in-vector dp)])
                    (for ([l (in-range 26)])
                      (let ([cur (vector-ref row l)])
                        (when (< cur INF)
                          ;; append w on the right
                          (let* ([new-f f]
                                 [new-l l-w]
                                 [overlap? (= l f-w)]
                                 [add (- len-w (if overlap? 1 0))]
                                 [newlen (+ cur add)])
                            (let ([old (vector-ref (vector-ref dp2 new-f) new-l)])
                              (when (< newlen old)
                                (vector-set! (vector-ref dp2 new-f) new-l newlen))))
                          ;; prepend w on the left
                          (let* ([new-f f-w]
                                 [new-l l]
                                 [overlap? (= l-w f)]
                                 [add (- len-w (if overlap? 1 0))]
                                 [newlen (+ cur add)])
                            (let ([old (vector-ref (vector-ref dp2 new-f) new-l)])
                              (when (< newlen old)
                                (vector-set! (vector-ref dp2 new-f) new-l newlen))))))))
                  (loop (+ i 1) dp2)))))))))
```

## Erlang

```erlang
-spec minimize_concatenated_length([unicode:unicode_binary()]) -> integer().
minimize_concatenated_length([]) ->
    0;
minimize_concatenated_length([Word | Rest]) ->
    F = first_char(Word),
    L = last_char(Word),
    Len = byte_size(Word),
    DP0 = maps:from_list([{ {F, L}, Len }]),
    FinalDP = lists:foldl(fun(W, Acc) -> transition(Acc, W) end, DP0, Rest),
    maps:fold(
        fun(_Key, V, Min) ->
            if V < Min -> V; true -> Min end
        end,
        1 bsl 30,
        FinalDP).

first_char(W) when is_binary(W) ->
    <<F, _/binary>> = W,
    F.

last_char(W) when is_binary(W) ->
    Size = byte_size(W),
    binary:at(W, Size - 1).

transition(DPPrev, Word) ->
    Fw = first_char(Word),
    Lw = last_char(Word),
    LenW = byte_size(Word),
    maps:fold(
        fun({F, L}, CurLen, Acc) ->
            % Append word to the right
            NewFirstA = F,
            NewLastA = Lw,
            AddA = CurLen + LenW - (if L == Fw -> 1; true -> 0 end),
            Acc1 = update_min(Acc, {NewFirstA, NewLastA}, AddA),
            % Prepend word to the left
            NewFirstP = Fw,
            NewLastP = L,
            AddP = CurLen + LenW - (if Lw == F -> 1; true -> 0 end),
            update_min(Acc1, {NewFirstP, NewLastP}, AddP)
        end,
        #{},
        DPPrev).

update_min(Map, Key, Val) ->
    case maps:find(Key, Map) of
        {ok, Existing} when Existing =< Val -> Map;
        _ -> maps:put(Key, Val, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_concatenated_length(words :: [String.t()]) :: integer()
  def minimize_concatenated_length([first_word | rest_words]) do
    f0 = :binary.first(first_word) - ?a
    l0 = :binary.last(first_word) - ?a
    len0 = String.length(first_word)

    dp = %{{f0, l0} => len0}
    final_dp = process(rest_words, dp)
    final_dp |> Map.values() |> Enum.min()
  end

  defp process([], dp), do: dp

  defp process([w | rest], dp) do
    wf = :binary.first(w) - ?a
    wl = :binary.last(w) - ?a
    wlen = String.length(w)

    new_dp =
      Enum.reduce(dp, %{}, fn {{f, l}, plen}, acc ->
        # join previous string then w
        overlap1 = if l == wf, do: 1, else: 0
        nlen1 = plen + wlen - overlap1
        key1 = {f, wl}
        acc = maybe_put_min(acc, key1, nlen1)

        # join w then previous string
        overlap2 = if wl == f, do: 1, else: 0
        nlen2 = wlen + plen - overlap2
        key2 = {wf, l}
        maybe_put_min(acc, key2, nlen2)
      end)

    process(rest, new_dp)
  end

  defp maybe_put_min(map, key, val) do
    case Map.get(map, key) do
      nil -> Map.put(map, key, val)
      existing when existing <= val -> map
      _ -> Map.put(map, key, val)
    end
  end
end
```
