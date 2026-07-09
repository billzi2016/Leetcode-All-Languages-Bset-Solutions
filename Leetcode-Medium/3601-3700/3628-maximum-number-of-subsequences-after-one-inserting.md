# 3628. Maximum Number of Subsequences After One Inserting

## Cpp

```cpp
class Solution {
public:
    long long numOfSubsequences(string s) {
        int n = s.size();
        vector<long long> preL(n + 1, 0), preLC(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            preL[i + 1] = preL[i] + (s[i] == 'L');
            preLC[i + 1] = preLC[i] + (s[i] == 'C' ? preL[i] : 0);
        }
        vector<long long> sufT(n + 1, 0), sufCT(n + 1, 0);
        long long cntT = 0, cntCT = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == 'T') ++cntT;
            else if (s[i] == 'C') cntCT += cntT;
            sufT[i] = cntT;
            sufCT[i] = cntCT;
        }
        long long base = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'C')
                base += preL[i] * sufT[i + 1];
        }
        long long ans = base;
        for (int i = 0; i <= n; ++i) {
            // insert 'L'
            ans = max(ans, base + sufCT[i]);
            // insert 'C'
            ans = max(ans, base + preL[i] * sufT[i]);
            // insert 'T'
            ans = max(ans, base + preLC[i]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numOfSubsequences(String s) {
        int n = s.length();
        long[] preL = new long[n + 1];
        long[] preLC = new long[n + 1];
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            preL[i + 1] = preL[i];
            preLC[i + 1] = preLC[i];
            if (ch == 'L') {
                preL[i + 1]++;
            } else if (ch == 'C') {
                preLC[i + 1] += preL[i];
            }
        }

        long[] sufT = new long[n + 1];
        long[] sufCT = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            sufT[i] = sufT[i + 1];
            sufCT[i] = sufCT[i + 1];
            if (ch == 'T') {
                sufT[i]++;
            } else if (ch == 'C') {
                sufCT[i] += sufT[i + 1];
            }
        }

        long base = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'C') {
                base += preL[i] * sufT[i + 1];
            }
        }

        long maxGain = 0;
        for (int pos = 0; pos <= n; pos++) {
            long gainL = sufCT[pos];                 // insert 'L'
            long gainC = preL[pos] * sufT[pos];      // insert 'C'
            long gainT = preLC[pos];                 // insert 'T'
            long best = Math.max(gainL, Math.max(gainC, gainT));
            if (best > maxGain) {
                maxGain = best;
            }
        }

        return base + maxGain;
    }
}
```

## Python

```python
class Solution(object):
    def numOfSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        preL = [0] * (n + 1)
        preLC = [0] * (n + 1)
        cntL = 0
        cntLC = 0
        for i, ch in enumerate(s):
            if ch == 'L':
                cntL += 1
            elif ch == 'C':
                cntLC += cntL
            preL[i + 1] = cntL
            preLC[i + 1] = cntLC

        sufT = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sufT[i] = sufT[i + 1] + (1 if s[i] == 'T' else 0)

        sufCT = [0] * (n + 1)
        cntT = 0
        cntCT = 0
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == 'T':
                cntT += 1
            elif ch == 'C':
                cntCT += cntT
            sufCT[i] = cntCT

        # base count of "LCT" subsequences in original string
        base = 0
        cntL = 0
        for i, ch in enumerate(s):
            if ch == 'L':
                cntL += 1
            elif ch == 'C':
                base += cntL * sufT[i + 1]

        max_gain = 0
        for i in range(n + 1):
            # insert 'L'
            gain_L = sufCT[i]
            # insert 'C'
            gain_C = preL[i] * sufT[i]
            # insert 'T'
            gain_T = preLC[i]
            if gain_L > max_gain:
                max_gain = gain_L
            if gain_C > max_gain:
                max_gain = gain_C
            if gain_T > max_gain:
                max_gain = gain_T

        return base + max_gain
```

## Python3

```python
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        preL = [0] * (n + 1)
        preLC = [0] * (n + 1)

        cntL = 0
        cntLC = 0
        base = 0

        for i, ch in enumerate(s):
            preL[i] = cntL
            preLC[i] = cntLC
            if ch == 'L':
                cntL += 1
            elif ch == 'C':
                cntLC += cntL
            elif ch == 'T':
                base += cntLC

        preL[n] = cntL
        preLC[n] = cntLC

        sufT = [0] * (n + 1)
        sufCT = [0] * (n + 1)

        cntT = 0
        cntCT = 0
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == 'T':
                cntT += 1
            elif ch == 'C':
                cntCT += cntT
            sufT[i] = cntT
            sufCT[i] = cntCT

        ans = base
        for i in range(n + 1):
            # insert 'L'
            ans = max(ans, base + sufCT[i])
            # insert 'C'
            ans = max(ans, base + preL[i] * sufT[i])
            # insert 'T'
            ans = max(ans, base + preLC[i])

        return ans
```

## C

```c
#include <string.h>
#include <stddef.h>

long long numOfSubsequences(char* s) {
    int n = (int)strlen(s);
    // Prefix arrays
    long long *preL = (long long*)malloc((n + 1) * sizeof(long long));
    long long *preLC = (long long*)malloc((n + 1) * sizeof(long long));
    preL[0] = 0;
    preLC[0] = 0;
    for (int i = 0; i < n; ++i) {
        preL[i + 1] = preL[i] + (s[i] == 'L');
        preLC[i + 1] = preLC[i];
        if (s[i] == 'C') {
            preLC[i + 1] += preL[i];
        }
    }

    // Suffix arrays
    long long *sufT = (long long*)malloc((n + 1) * sizeof(long long));
    long long *sufCT = (long long*)malloc((n + 1) * sizeof(long long));
    sufT[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        sufT[i] = sufT[i + 1] + (s[i] == 'T');
    }
    long long cntT = 0, cntCT = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == 'C') {
            cntCT += cntT;
        }
        if (s[i] == 'T') {
            ++cntT;
        }
        sufCT[i] = cntCT;
    }

    // Base count without insertion
    long long base = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'C') {
            base += preL[i] * sufT[i + 1];
        }
    }

    // Compute maximum gain from one insertion
    long long maxGain = 0;
    for (int i = 0; i <= n; ++i) {
        // Insert 'L'
        if (sufCT[i] > maxGain) maxGain = sufCT[i];
        // Insert 'C'
        long long gainC = preL[i] * sufT[i];
        if (gainC > maxGain) maxGain = gainC;
        // Insert 'T'
        if (preLC[i] > maxGain) maxGain = preLC[i];
    }

    free(preL);
    free(preLC);
    free(sufT);
    free(sufCT);

    return base + maxGain;
}
```

## Csharp

```csharp
public class Solution {
    public long NumOfSubsequences(string s) {
        int n = s.Length;
        long[] preL = new long[n + 1];
        long[] preLC = new long[n + 1];
        for (int i = 0; i < n; i++) {
            char ch = s[i];
            preL[i + 1] = preL[i] + (ch == 'L' ? 1 : 0);
            preLC[i + 1] = preLC[i];
            if (ch == 'C') {
                preLC[i + 1] += preL[i];
            }
        }

        long[] sufT = new long[n + 1];
        long[] sufCT = new long[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            char ch = s[i];
            sufT[i] = sufT[i + 1] + (ch == 'T' ? 1 : 0);
            sufCT[i] = sufCT[i + 1];
            if (ch == 'C') {
                sufCT[i] += sufT[i + 1];
            }
        }

        long baseCount = 0;
        for (int i = 0; i <= n; i++) {
            baseCount += preLC[i] * sufT[i];
        }

        long maxGain = 0;
        for (int i = 0; i <= n; i++) {
            long gainL = sufCT[i];                     // insert 'L'
            long gainC = preL[i] * sufT[i];            // insert 'C'
            long gainT = preLC[i];                     // insert 'T'
            long localMax = gainL;
            if (gainC > localMax) localMax = gainC;
            if (gainT > localMax) localMax = gainT;
            if (localMax > maxGain) maxGain = localMax;
        }

        return baseCount + maxGain;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numOfSubsequences = function(s) {
    const n = s.length;
    const preL = new Array(n + 1).fill(0);
    const preLC = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        preL[i + 1] = preL[i] + (s[i] === 'L' ? 1 : 0);
        if (s[i] === 'C') {
            preLC[i + 1] = preLC[i] + preL[i];
        } else {
            preLC[i + 1] = preLC[i];
        }
    }

    const sufT = new Array(n + 1).fill(0);
    const sufCT = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        sufT[i] = sufT[i + 1] + (s[i] === 'T' ? 1 : 0);
        if (s[i] === 'C') {
            sufCT[i] = sufCT[i + 1] + sufT[i + 1];
        } else {
            sufCT[i] = sufCT[i + 1];
        }
    }

    // base count without insertion
    let base = 0;
    for (let i = 0; i < n; ++i) {
        if (s[i] === 'C') {
            base += preL[i] * sufT[i + 1];
        }
    }

    let maxGain = 0;
    for (let i = 0; i <= n; ++i) {
        const gainL = sufCT[i];                 // insert 'L'
        const gainC = preL[i] * sufT[i];        // insert 'C'
        const gainT = preLC[i];                 // insert 'T'
        maxGain = Math.max(maxGain, gainL, gainC, gainT);
    }

    return base + maxGain;
};
```

## Typescript

```typescript
function numOfSubsequences(s: string): number {
    const n = s.length;
    // prefix count of 'L'
    const preL = new Array<number>(n + 1);
    preL[0] = 0;
    for (let i = 0; i < n; i++) {
        preL[i + 1] = preL[i] + (s.charAt(i) === 'L' ? 1 : 0);
    }

    // suffix count of 'T'
    const sufT = new Array<number>(n + 1);
    sufT[n] = 0;
    for (let i = n - 1; i >= 0; i--) {
        sufT[i] = sufT[i + 1] + (s.charAt(i) === 'T' ? 1 : 0);
    }

    // prefix count of "LC" subsequences up to each position
    const preLCtotal = new Array<number>(n + 1);
    let cntL = 0;
    let lcCnt = 0;
    preLCtotal[0] = 0;
    for (let i = 0; i < n; i++) {
        const ch = s.charAt(i);
        if (ch === 'L') {
            cntL++;
        } else if (ch === 'C') {
            lcCnt += cntL;
        }
        preLCtotal[i + 1] = lcCnt;
    }

    // base number of "LCT" subsequences without insertion
    let base = 0;
    for (let i = 0; i < n; i++) {
        if (s.charAt(i) === 'C') {
            base += preL[i] * sufT[i + 1];
        }
    }

    // suffix count of "CT" subsequences starting at each position
    const sufCT = new Array<number>(n + 1);
    sufCT[n] = 0;
    let cntC = 0;
    let ctCnt = 0;
    for (let i = n - 1; i >= 0; i--) {
        const ch = s.charAt(i);
        if (ch === 'T') {
            ctCnt += cntC;
        } else if (ch === 'C') {
            cntC++;
        }
        sufCT[i] = ctCnt;
    }

    // evaluate best gain from inserting one character
    let maxGain = 0;
    for (let i = 0; i <= n; i++) {
        const gainL = sufCT[i];                     // insert 'L'
        if (gainL > maxGain) maxGain = gainL;

        const gainC = preL[i] * sufT[i];            // insert 'C'
        if (gainC > maxGain) maxGain = gainC;

        const gainT = preLCtotal[i];                // insert 'T'
        if (gainT > maxGain) maxGain = gainT;
    }

    return base + maxGain;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numOfSubsequences($s) {
        $n = strlen($s);
        // prefix counts
        $preL  = array_fill(0, $n + 1, 0);
        $preLC = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $ch = $s[$i];
            $preL[$i + 1]  = $preL[$i] + ($ch === 'L' ? 1 : 0);
            $preLC[$i + 1] = $preLC[$i];
            if ($ch === 'C') {
                $preLC[$i + 1] += $preL[$i]; // L before this C
            }
        }

        // suffix counts
        $sufT  = array_fill(0, $n + 1, 0);
        $sufCT = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $ch = $s[$i];
            $sufT[$i] = $sufT[$i + 1] + ($ch === 'T' ? 1 : 0);
            $sufCT[$i] = $sufCT[$i + 1];
            if ($ch === 'C') {
                $sufCT[$i] += $sufT[$i + 1]; // T after this C
            }
        }

        // base number of "LCT" subsequences in original string
        $base = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($s[$i] === 'C') {
                $base += $preL[$i] * $sufT[$i + 1];
            }
        }

        // evaluate best insertion gain
        $maxGain = 0;
        for ($i = 0; $i <= $n; ++$i) {
            $gainL = $sufCT[$i];                     // insert 'L'
            $gainC = $preL[$i] * $sufT[$i];          // insert 'C'
            $gainT = $preLC[$i];                     // insert 'T'
            $localMax = max($gainL, $gainC, $gainT);
            if ($localMax > $maxGain) {
                $maxGain = $localMax;
            }
        }

        return $base + $maxGain;
    }
}
```

## Swift

```swift
class Solution {
    func numOfSubsequences(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        
        // suffixT[i] = number of 'T' in s[i...]
        var suffixT = [Int](repeating: 0, count: n + 1)
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                suffixT[i] = suffixT[i + 1] + (chars[i] == "T" ? 1 : 0)
            }
        }
        
        // base count without insertion
        var preLCount = 0
        var base = 0
        for i in 0..<n {
            let ch = chars[i]
            if ch == "C" {
                base += preLCount * suffixT[i + 1]
            }
            if ch == "L" {
                preLCount += 1
            }
        }
        
        // preLArr[i] = number of 'L' before position i
        // preLCArr[i] = number of "LC" subsequences in prefix before i
        var preLArr = [Int](repeating: 0, count: n + 1)
        var preLCArr = [Int](repeating: 0, count: n + 1)
        var cntL = 0
        var cntLC = 0
        for i in 0..<n {
            preLArr[i] = cntL
            preLCArr[i] = cntLC
            let ch = chars[i]
            if ch == "L" {
                cntL += 1
            } else if ch == "C" {
                cntLC += cntL
            }
        }
        preLArr[n] = cntL
        preLCArr[n] = cntLC
        
        // suffixCT[i] = number of "CT" subsequences in s[i...]
        var suffixCT = [Int](repeating: 0, count: n + 1)
        var cntT = 0
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                suffixCT[i] = suffixCT[i + 1]
                if chars[i] == "C" {
                    suffixCT[i] += cntT
                }
                if chars[i] == "T" {
                    cntT += 1
                }
            }
        }
        
        var answer = base
        for i in 0...n {
            let gainL = suffixCT[i]                     // insert 'L'
            let gainC = preLArr[i] * suffixT[i]         // insert 'C'
            let gainT = preLCArr[i]                     // insert 'T'
            let bestGain = max(gainL, max(gainC, gainT))
            if base + bestGain > answer {
                answer = base + bestGain
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfSubsequences(s: String): Long {
        val n = s.length
        val preL = LongArray(n + 1)
        val preLC = LongArray(n + 1)
        var cntL = 0L
        var cntLC = 0L
        for (i in 0 until n) {
            when (s[i]) {
                'L' -> cntL++
                'C' -> cntLC += cntL
            }
            preL[i + 1] = cntL
            preLC[i + 1] = cntLC
        }

        val sufT = LongArray(n + 1)
        val sufCT = LongArray(n + 1)
        var cntT = 0L
        var cntCT = 0L
        for (i in n - 1 downTo 0) {
            when (s[i]) {
                'T' -> cntT++
                'C' -> cntCT += cntT
            }
            sufT[i] = cntT
            sufCT[i] = cntCT
        }

        var base = 0L
        for (i in 0 until n) {
            if (s[i] == 'T') {
                base += preLC[i]
            }
        }

        var maxGain = 0L
        for (i in 0..n) {
            val gainL = sufCT[i]
            if (gainL > maxGain) maxGain = gainL

            val gainC = preL[i] * sufT[i]
            if (gainC > maxGain) maxGain = gainC

            val gainT = preLC[i]
            if (gainT > maxGain) maxGain = gainT
        }

        return base + maxGain
    }
}
```

## Dart

```dart
class Solution {
  int numOfSubsequences(String s) {
    int n = s.length;
    List<int> preL = List.filled(n + 1, 0);
    List<int> preLC = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      int ch = s.codeUnitAt(i);
      preL[i + 1] = preL[i] + (ch == 76 ? 1 : 0); // 'L'
      if (ch == 67) { // 'C'
        preLC[i + 1] = preLC[i] + preL[i];
      } else {
        preLC[i + 1] = preLC[i];
      }
    }

    List<int> sufT = List.filled(n + 1, 0);
    List<int> sufCT = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
      int ch = s.codeUnitAt(i);
      sufT[i] = sufT[i + 1] + (ch == 84 ? 1 : 0); // 'T'
      if (ch == 67) { // 'C'
        sufCT[i] = sufCT[i + 1] + sufT[i + 1];
      } else {
        sufCT[i] = sufCT[i + 1];
      }
    }

    int base = 0;
    for (int i = 0; i < n; i++) {
      if (s.codeUnitAt(i) == 67) { // 'C'
        base += preL[i] * sufT[i + 1];
      }
    }

    int maxGain = 0;
    for (int i = 0; i <= n; i++) {
      int gainL = sufCT[i]; // insert 'L' before position i
      if (gainL > maxGain) maxGain = gainL;

      int gainC = preL[i] * sufT[i]; // insert 'C'
      if (gainC > maxGain) maxGain = gainC;

      int gainT = preLC[i]; // insert 'T'
      if (gainT > maxGain) maxGain = gainT;
    }

    return base + maxGain;
  }
}
```

## Golang

```go
func numOfSubsequences(s string) int64 {
    n := len(s)
    preL := make([]int64, n+1)
    preLC := make([]int64, n+1)

    var cntL, cntLC int64
    for i := 0; i < n; i++ {
        preL[i] = cntL
        preLC[i] = cntLC
        if s[i] == 'L' {
            cntL++
        } else if s[i] == 'C' {
            cntLC += cntL
        }
    }
    preL[n] = cntL
    preLC[n] = cntLC

    sufT := make([]int64, n+1)
    sufCT := make([]int64, n+1)

    var cntT, cntCT int64
    for i := n - 1; i >= 0; i-- {
        sufT[i] = cntT
        sufCT[i] = cntCT
        if s[i] == 'T' {
            cntT++
        } else if s[i] == 'C' {
            cntCT += cntT
        }
    }
    // sufT[n] and sufCT[n] are already zero

    var base int64
    for i := 0; i < n; i++ {
        if s[i] == 'C' {
            base += preL[i] * sufT[i+1]
        }
    }

    var maxGain int64
    for i := 0; i <= n; i++ {
        // Insert 'L'
        if g := sufCT[i]; g > maxGain {
            maxGain = g
        }
        // Insert 'C'
        if g := preL[i] * sufT[i]; g > maxGain {
            maxGain = g
        }
        // Insert 'T'
        if g := preLC[i]; g > maxGain {
            maxGain = g
        }
    }

    return base + maxGain
}
```

## Ruby

```ruby
def num_of_subsequences(s)
  n = s.length
  preL = Array.new(n + 1, 0)
  preLC = Array.new(n + 1, 0)

  (0...n).each do |i|
    ch = s[i]
    preL[i + 1] = preL[i] + (ch == 'L' ? 1 : 0)
    preLC[i + 1] = preLC[i]
    preLC[i + 1] += preL[i] if ch == 'C'
  end

  sufT = Array.new(n + 1, 0)
  sufCT = Array.new(n + 1, 0)

  (n - 1).downto(0) do |i|
    ch = s[i]
    sufT[i] = sufT[i + 1] + (ch == 'T' ? 1 : 0)
    sufCT[i] = sufCT[i + 1]
    sufCT[i] += sufT[i + 1] if ch == 'C'
  end

  base = 0
  (0...n).each { |i| base += preLC[i] if s[i] == 'T' }

  max_val = base
  (0..n).each do |i|
    gain_l = sufCT[i]
    gain_c = preL[i] * sufT[i]
    gain_t = preLC[i]

    cur = base + gain_l
    max_val = cur if cur > max_val

    cur = base + gain_c
    max_val = cur if cur > max_val

    cur = base + gain_t
    max_val = cur if cur > max_val
  end

  max_val
end
```

## Scala

```scala
object Solution {
    def numOfSubsequences(s: String): Long = {
        val n = s.length
        val preL = new Array[Long](n + 1)
        val preLC = new Array[Long](n + 1)

        var i = 0
        while (i < n) {
            val ch = s.charAt(i)
            preL(i + 1) = preL(i) + (if (ch == 'L') 1 else 0)
            preLC(i + 1) = preLC(i) + (if (ch == 'C') preL(i) else 0)
            i += 1
        }

        val sufT = new Array[Long](n + 1)
        val sufCT = new Array[Long](n + 1)

        i = n - 1
        while (i >= 0) {
            val ch = s.charAt(i)
            sufT(i) = sufT(i + 1) + (if (ch == 'T') 1 else 0)
            sufCT(i) = sufCT(i + 1) + (if (ch == 'C') sufT(i + 1) else 0)
            i -= 1
        }

        var base: Long = 0L
        i = 0
        while (i < n) {
            if (s.charAt(i) == 'C')
                base += preL(i) * sufT(i + 1)
            i += 1
        }

        var maxGain: Long = 0L
        var pos = 0
        while (pos <= n) {
            val gainL = sufCT(pos)
            val gainC = preL(pos) * sufT(pos)
            val gainT = preLC(pos)

            var best = gainL
            if (gainC > best) best = gainC
            if (gainT > best) best = gainT
            if (best > maxGain) maxGain = best

            pos += 1
        }

        base + maxGain
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_subsequences(s: String) -> i64 {
        let bytes = s.as_bytes();
        let n = bytes.len();

        // Prefix counts
        let mut pre_l = vec![0i64; n + 1];
        let mut pre_lc = vec![0i64; n + 1];
        for i in 0..n {
            pre_l[i + 1] = pre_l[i] + if bytes[i] == b'L' { 1 } else { 0 };
            pre_lc[i + 1] = pre_lc[i];
            if bytes[i] == b'C' {
                pre_lc[i + 1] += pre_l[i];
            }
        }

        // Suffix counts of T
        let mut suf_t = vec![0i64; n + 1];
        for i in (0..n).rev() {
            suf_t[i] = suf_t[i + 1] + if bytes[i] == b'T' { 1 } else { 0 };
        }

        // Suffix counts of CT subsequences
        let mut suf_ct = vec![0i64; n + 1];
        let mut cnt_t = 0i64;
        let mut ct = 0i64;
        for i in (0..n).rev() {
            if bytes[i] == b'T' {
                cnt_t += 1;
            } else if bytes[i] == b'C' {
                ct += cnt_t;
            }
            suf_ct[i] = ct;
        }

        // Base number of LCT subsequences without insertion
        let mut base: i64 = 0;
        for i in 0..n {
            if bytes[i] == b'C' {
                base += pre_l[i] * suf_t[i + 1];
            }
        }

        // Compute maximum gain from a single insertion
        let mut max_gain: i64 = 0;
        for i in 0..=n {
            // Insert 'L'
            max_gain = max_gain.max(suf_ct[i]);
            // Insert 'C'
            max_gain = max_gain.max(pre_l[i] * suf_t[i]);
            // Insert 'T'
            max_gain = max_gain.max(pre_lc[i]);
        }

        base + max_gain
    }
}
```

## Racket

```racket
(define/contract (num-of-subsequences s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [preL (make-vector (+ n 1) 0)]
         [preLC (make-vector (+ n 1) 0)])
    ;; Prefix counts
    (for ([i (in-range n)])
      (let ([ch (string-ref s i)])
        (vector-set! preL (+ i 1)
                     (+ (vector-ref preL i)
                        (if (char=? ch #\L) 1 0)))
        (vector-set! preLC (+ i 1)
                     (+ (vector-ref preLC i)
                        (if (char=? ch #\C) (vector-ref preL i) 0)))))
    ;; Suffix counts
    (let* ([sufT (make-vector (+ n 1) 0)]
           [sufCT (make-vector (+ n 1) 0)])
      (for ([i (in-range (- n 1) -1 -1)])
        (let ([ch (string-ref s i)])
          (vector-set! sufT i
                       (+ (vector-ref sufT (+ i 1))
                          (if (char=? ch #\T) 1 0)))
          (vector-set! sufCT i
                       (+ (vector-ref sufCT (+ i 1))
                          (if (char=? ch #\C)
                              (vector-ref sufT (+ i 1))
                              0)))))
      ;; Compute base and maximal gain
      (let loop ([i 0] [base 0] [max-gain 0])
        (if (> i n)
            (+ base max-gain)
            (let* ([preLC-i (vector-ref preLC i)]
                   [sufT-i (vector-ref sufT i)]
                   [gainL (vector-ref sufCT i)]
                   [gainC (* (vector-ref preL i) sufT-i)]
                   [gainT preLC-i]
                   [new-base (+ base (* preLC-i sufT-i))]
                   [new-max (max max-gain gainL gainC gainT)])
              (loop (+ i 1) new-base new-max)))))))
```

## Erlang

```erlang
-spec num_of_subsequences(S :: unicode:unicode_binary()) -> integer().
num_of_subsequences(S) ->
    Chars = binary_to_list(S),
    {SufTList, SufCTList} = build_suffix(Chars),
    SufTTuple = list_to_tuple(SufTList),
    SufCTTuple = list_to_tuple(SufCTList),
    {Base, MaxGain} = forward(Chars, 0, 0, 0, 0, 0, SufTTuple, SufCTTuple),
    Base + MaxGain.

build_suffix(Chars) ->
    Rev = lists:reverse(Chars),
    build_rev(Rev, 0, [0], [0]).

build_rev([], _CntT, SufTAcc, SufCTAcc) ->
    {lists:reverse(SufTAcc), lists:reverse(SufCTAcc)};
build_rev([Char|Rest], CntT, SufTAcc, SufCTAcc) ->
    SufTi = CntT,
    AddCT = case Char of $C -> CntT; _ -> 0 end,
    PrevSufCT = hd(SufCTAcc),
    SufCTi = PrevSufCT + AddCT,
    NewSufTAcc = [SufTi | SufTAcc],
    NewSufCTAcc = [SufCTi | SufCTAcc],
    NewCntT = case Char of $T -> CntT + 1; _ -> CntT end,
    build_rev(Rest, NewCntT, NewSufTAcc, NewSufCTAcc).

forward([], Index, PreL, PreLC, BaseAcc, MaxGain, SufTTuple, SufCTTuple) ->
    GainL = element(Index + 1, SufCTTuple),
    GainC = PreL * element(Index + 1, SufTTuple),
    GainT = PreLC,
    NewMaxGain = max(MaxGain, max(GainL, max(GainC, GainT))),
    {BaseAcc, NewMaxGain};
forward([Char|Rest], Index, PreL, PreLC, BaseAcc, MaxGain, SufTTuple, SufCTTuple) ->
    GainL = element(Index + 1, SufCTTuple),
    GainC = PreL * element(Index + 1, SufTTuple),
    GainT = PreLC,
    NewMaxGain0 = max(MaxGain, max(GainL, max(GainC, GainT))),
    BaseAcc1 = case Char of
        $C -> BaseAcc + PreL * element(Index + 2, SufTTuple);
        _   -> BaseAcc
    end,
    PreL1 = case Char of $L -> PreL + 1; _ -> PreL end,
    PreLC1 = case Char of $C -> PreLC + PreL; _ -> PreLC end,
    forward(Rest, Index + 1, PreL1, PreLC1, BaseAcc1, NewMaxGain0, SufTTuple, SufCTTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_subsequences(s :: String.t) :: integer
  def num_of_subsequences(s) do
    chars = :binary.bin_to_list(s)
    n = length(chars)

    # Prefix counts: preL[i] = number of 'L' in first i characters, preLC[i] = number of "LC" subsequences in first i characters
    {preL_rev, preLC_rev, _, _} =
      Enum.reduce(chars, {[], [], 0, 0}, fn c, {l_acc, lc_acc, l_cnt, lc_cnt} ->
        {new_l, new_lc} = case c do
          ?L -> {l_cnt + 1, lc_cnt}
          ?C -> {l_cnt, lc_cnt + l_cnt}
          _   -> {l_cnt, lc_cnt}
        end
        {[new_l | l_acc], [new_lc | lc_acc], new_l, new_lc}
      end)

    preL = [0 | Enum.reverse(preL_rev)]
    preLC = [0 | Enum.reverse(preLC_rev)]

    # Suffix counts: sufT[i] = number of 'T' from i to end-1, sufCT[i] = number of "CT" subsequences from i to end-1
    {sufT_rev, sufCT_rev, _, _} =
      Enum.reduce(Enum.reverse(chars), {[], [], 0, 0}, fn c, {t_acc, ct_acc, t_cnt, ct_cnt} ->
        {new_t, new_ct} = case c do
          ?T -> {t_cnt + 1, ct_cnt}
          ?C -> {t_cnt, ct_cnt + t_cnt}
          _   -> {t_cnt, ct_cnt}
        end
        {[new_t | t_acc], [new_ct | ct_acc], new_t, new_ct}
      end)

    sufT = sufT_rev ++ [0]
    sufCT = sufCT_rev ++ [0]

    preL_t = List.to_tuple(preL)
    preLC_t = List.to_tuple(preLC)
    sufT_t = List.to_tuple(sufT)
    sufCT_t = List.to_tuple(sufCT)

    # Base count without insertion
    base =
      Enum.reduce(Enum.with_index(chars), 0, fn {c, i}, acc ->
        if c == ?C do
          l_before = elem(preL_t, i)
          t_after = elem(sufT_t, i + 1)
          acc + l_before * t_after
        else
          acc
        end
      end)

    # Maximum gain from a single insertion
    max_gain =
      Enum.reduce(0..n, 0, fn pos, best_sofar ->
        gL = elem(sufCT_t, pos)
        gC = elem(preL_t, pos) * elem(sufT_t, pos)
        gT = elem(preLC_t, pos)
        cur_best = max(gL, max(gC, gT))
        if cur_best > best_sofar, do: cur_best, else: best_sofar
      end)

    base + max_gain
  end
end
```
