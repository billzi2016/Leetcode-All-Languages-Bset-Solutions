# 2484. Count Palindromic Subsequences

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPalindromes(string s) {
        const long long MOD = 1000000007LL;
        int n = s.size();
        if (n < 5) return 0;
        // rightMat[k][a*10+b] = sum_{m>k, s[m]=a} cnt_b_between(k,m)
        vector<array<long long,100>> rightMat(n);
        array<long long,10> rightCnt{};
        array<long long,100> rightSum{};
        rightCnt.fill(0);
        rightSum.fill(0);
        for (int k = n - 1; k >= 0; --k) {
            // snapshot for center k
            rightMat[k] = rightSum;
            int d = s[k] - '0';
            // update rightSum: each existing a gains cnt of b==d equal to rightCnt[a]
            for (int a = 0; a < 10; ++a) {
                long long add = rightCnt[a];
                if (add) rightSum[a*10 + d] += add;
            }
            // add current digit to rightCnt
            rightCnt[d]++;
        }

        array<long long,10> leftCnt{};
        array<long long,100> leftSum{};
        leftCnt.fill(0);
        leftSum.fill(0);
        long long ans = 0;

        for (int k = 0; k < n; ++k) {
            // combine leftSum and rightMat[k]
            const auto &r = rightMat[k];
            for (int idx = 0; idx < 100; ++idx) {
                if (leftSum[idx]==0 || r[idx]==0) continue;
                ans += (leftSum[idx] % MOD) * (r[idx] % MOD);
                if (ans >= (1LL<<62)) ans %= MOD; // prevent overflow
            }
            ans %= MOD;

            int d = s[k] - '0';
            // update leftSum for future centers: interior element at k contributes to b==d
            for (int a = 0; a < 10; ++a) {
                long long add = leftCnt[a];
                if (add) leftSum[a*10 + d] += add;
            }
            // add current digit to leftCnt
            leftCnt[d]++;
        }

        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;

    public int countPalindromes(String s) {
        int n = s.length();
        char[] ch = s.toCharArray();

        // suffixPairs[k][b][a] = number of pairs (l,m) with l>k, m>l, s[l]=b, s[m]=a
        int[][][] suffixPairs = new int[n][10][10];
        int[] cntRight = new int[10];
        int[][] pairsRight = new int[10][10];

        for (int idx = n - 1; idx >= 0; --idx) {
            // store current pairsRight as suffix for position idx
            for (int i = 0; i < 10; ++i) {
                System.arraycopy(pairsRight[i], 0, suffixPairs[idx][i], 0, 10);
            }
            int d = ch[idx] - '0';
            // update pairsRight with new pairs where current idx is the left element (l)
            for (int a = 0; a < 10; ++a) {
                if (cntRight[a] != 0) {
                    long val = pairsRight[d][a] + (long) cntRight[a];
                    pairsRight[d][a] = (int) (val % MOD);
                }
            }
            cntRight[d]++;
        }

        long ans = 0;
        int[] cntLeft = new int[10];
        int[][] leftPairs = new int[10][10];

        for (int k = 0; k < n; ++k) {
            // combine left pairs and right pairs using current character as center
            for (int a = 0; a < 10; ++a) {
                for (int b = 0; b < 10; ++b) {
                    int left = leftPairs[a][b];
                    if (left == 0) continue;
                    int right = suffixPairs[k][b][a];
                    if (right == 0) continue;
                    ans += (long) left * right % MOD;
                    if (ans >= MOD) ans -= MOD;
                }
            }

            int d = ch[k] - '0';
            // update leftPairs with new pairs where current k is the right element (j)
            for (int a = 0; a < 10; ++a) {
                if (cntLeft[a] != 0) {
                    long val = leftPairs[a][d] + (long) cntLeft[a];
                    leftPairs[a][d] = (int) (val % MOD);
                }
            }
            cntLeft[d]++;
        }

        return (int) (ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        if n < 5:
            return 0

        digits = [ord(c) - 48 for c in s]  # convert to ints 0-9

        # suffix_pairs[i][a*10+b] = number of ordered pairs (l,m) with l>=i, m>l,
        # s[l]=a, s[m]=b
        suffix_pairs = [[0] * 100 for _ in range(n + 1)]
        cnt_suffix = [0] * 10

        for i in range(n - 1, -1, -1):
            cur = digits[i]
            row = suffix_pairs[i]
            nxt = suffix_pairs[i + 1]
            # copy next row
            row[:] = nxt[:]
            # add pairs where first digit is cur and second digit is a
            base = cur * 10
            for a in range(10):
                row[base + a] += cnt_suffix[a]
            cnt_suffix[cur] += 1

        prefix_counts = [0] * 10
        prefix_pair = [0] * 100
        ans = 0

        for k in range(n):
            # contributions with center at position k
            right = suffix_pairs[k + 1]  # pairs strictly after k
            total = 0
            for idx in range(100):
                if prefix_pair[idx] and right[idx]:
                    total += (prefix_pair[idx] * right[idx]) % MOD
            ans = (ans + total) % MOD

            # update prefix structures with current character s[k]
            cur = digits[k]
            base_cur = cur
            for a in range(10):
                idx = a * 10 + base_cur
                prefix_pair[idx] += prefix_counts[a]
            prefix_counts[cur] += 1

        return ans % MOD
```

## Python3

```python
class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        if n < 5:
            return 0

        # prefix pair counts up to each index
        pref = [[0] * 100 for _ in range(n)]
        freq = [0] * 10
        cur = [[0] * 10 for _ in range(10)]
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            for a in range(10):
                cnt = freq[a]
                if cnt:
                    cur[a][d] += cnt
            freq[d] += 1
            flat = []
            for a in range(10):
                flat.extend(cur[a])
            pref[i] = flat

        # suffix pair counts from each index to end
        suff = [[0] * 100 for _ in range(n)]
        freq = [0] * 10
        cur = [[0] * 10 for _ in range(10)]
        for i in range(n - 1, -1, -1):
            d = ord(s[i]) - 48
            for a in range(10):
                cnt = freq[a]
                if cnt:
                    cur[d][a] += cnt
            freq[d] += 1
            flat = []
            for a in range(10):
                flat.extend(cur[a])
            suff[i] = flat

        ans = 0
        zero = [0] * 100
        for k in range(n):
            # left side pairs must end before k, right side pairs start after k
            L = pref[k - 1] if k >= 1 else zero
            R = suff[k + 1] if k + 1 < n else zero
            total = 0
            for a in range(10):
                base_a = a * 10
                for b in range(10):
                    left = L[base_a + b]
                    if left:
                        right = R[b * 10 + a]
                        if right:
                            total = (total + left * right) % MOD
            ans = (ans + total) % MOD

        return ans % MOD
```

## C

```c
#include <string.h>
#include <stdlib.h>

#define MOD 1000000007

int countPalindromes(char* s) {
    int n = strlen(s);
    if (n < 5) return 0;

    // rightPairs[i][a*10+b] = number of ordered pairs (l,m) with l>i, m>l,
    // where s[l]=a and s[m]=b
    int *rightPairs = (int*)calloc((size_t)n * 100, sizeof(int));
    if (!rightPairs) return 0; // allocation failure fallback

    long long cnt[10] = {0};
    long long pairCnt[10][10] = {{0}};

    for (int i = n - 1; i >= 0; --i) {
        int base = i * 100;
        for (int a = 0; a < 10; ++a)
            for (int b = 0; b < 10; ++b)
                rightPairs[base + a * 10 + b] = (int)pairCnt[a][b];

        int d = s[i] - '0';
        for (int x = 0; x < 10; ++x) {
            pairCnt[d][x] += cnt[x];
            if (pairCnt[d][x] >= MOD) pairCnt[d][x] %= MOD;
        }
        cnt[d] += 1;
        if (cnt[d] >= MOD) cnt[d] %= MOD;
    }

    long long leftCnt[10] = {0};
    long long leftPair[10][10] = {{0}};
    long long ans = 0;

    for (int k = 0; k < n; ++k) {
        int *rp = rightPairs + k * 100;
        for (int a = 0; a < 10; ++a) {
            for (int b = 0; b < 10; ++b) {
                long long term = leftPair[a][b] * rp[b * 10 + a];
                ans += term % MOD;
                if (ans >= MOD) ans %= MOD;
            }
        }

        int d = s[k] - '0';
        for (int x = 0; x < 10; ++x) {
            leftPair[x][d] += leftCnt[x];
            if (leftPair[x][d] >= MOD) leftPair[x][d] %= MOD;
        }
        leftCnt[d] += 1;
        if (leftCnt[d] >= MOD) leftCnt[d] %= MOD;
    }

    free(rightPairs);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int CountPalindromes(string s) {
        int n = s.Length;
        // suffixPairs[k][a*10+b] = number of pairs (l,m) with l>k, m>l, s[l]=a, s[m]=b
        int[][] suffixPairs = new int[n][];
        int[] cnt = new int[10];
        int[,] pair = new int[10, 10];

        for (int idx = n - 1; idx >= 0; idx--) {
            // store current pair counts for center at idx
            int[] arr = new int[100];
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    arr[a * 10 + b] = pair[a, b];
                }
            }
            suffixPairs[idx] = arr;

            int d = s[idx] - '0';
            // add pairs where current idx is the first element
            for (int y = 0; y < 10; y++) {
                if (cnt[y] != 0) {
                    pair[d, y] = (pair[d, y] + cnt[y]) % MOD;
                }
            }
            cnt[d]++;
        }

        int[] leftCnt = new int[10];
        int[,] leftPair = new int[10, 10];
        long ans = 0;

        for (int k = 0; k < n; k++) {
            int[] rightArr = suffixPairs[k];
            // combine left pairs and right pairs
            for (int a = 0; a < 10; a++) {
                for (int b = 0; b < 10; b++) {
                    int leftVal = leftPair[a, b];
                    if (leftVal == 0) continue;
                    int rightVal = rightArr[b * 10 + a];
                    if (rightVal == 0) continue;
                    ans += ((long)leftVal * rightVal) % MOD;
                    if (ans >= MOD) ans -= MOD;
                }
            }

            // update left structures with current character as second element of pair
            int d = s[k] - '0';
            for (int x = 0; x < 10; x++) {
                if (leftCnt[x] != 0) {
                    leftPair[x, d] = (leftPair[x, d] + leftCnt[x]) % MOD;
                }
            }
            leftCnt[d]++;
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromes = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    if (n < 5) return 0;

    // convert to digit array for fast access
    const digits = new Uint8Array(n);
    for (let i = 0; i < n; ++i) digits[i] = s.charCodeAt(i) - 48;

    // suffixPairs[pos][a*10+b] = number of ordered pairs (first=a, second=b)
    // with both indices >= pos
    const suffixPairs = new Array(n + 1);
    const zeroArr = new Uint32Array(100);
    suffixPairs[n] = zeroArr; // all zeros for empty suffix

    const suffixCounts = new Uint32Array(10);
    let curPairs = new Uint32Array(100); // mutable, will be copied each step
    for (let i = n - 1; i >= 0; --i) {
        const d = digits[i];
        for (let a = 0; a < 10; ++a) {
            const idx = d * 10 + a;
            curPairs[idx] += suffixCounts[a];
        }
        suffixCounts[d]++;
        // store snapshot for position i
        suffixPairs[i] = curPairs.slice();
    }

    const prefixCounts = new Uint32Array(10);
    let leftPairs = new Uint32Array(100); // ordered pairs in the prefix

    let ans = 0;

    for (let k = 0; k < n; ++k) {
        const rightPairs = suffixPairs[k + 1];

        // accumulate contributions: sum_{a,b} left[a][b] * right[b][a]
        for (let idx = 0; idx < 100; ++idx) {
            const leftVal = leftPairs[idx];
            if (!leftVal) continue;
            const a = (idx / 10) | 0;
            const b = idx % 10;
            const rightVal = rightPairs[b * 10 + a];
            if (!rightVal) continue;
            ans = (ans + (leftVal * rightVal) % MOD) % MOD;
        }

        // update leftPairs to include current digit as second element of future pairs
        const cur = digits[k];
        for (let a = 0; a < 10; ++a) {
            const idx = a * 10 + cur;
            leftPairs[idx] += prefixCounts[a];
            if (leftPairs[idx] >= MOD) leftPairs[idx] %= MOD;
        }
        // update prefix digit counts
        prefixCounts[cur]++;
    }

    return ans % MOD;
};
```

## Typescript

```typescript
function countPalindromes(s: string): number {
    const MOD = 1_000_000_007;
    const n = s.length;
    const digits = new Uint8Array(n);
    for (let i = 0; i < n; ++i) digits[i] = s.charCodeAt(i) - 48;

    // left side data
    const leftCnt = new Array(10).fill(0);
    const leftPairs: number[][] = Array.from({ length: 10 }, () => new Array(10).fill(0));

    // right side data
    const rightCnt = new Array(10).fill(0);
    for (let d of digits) rightCnt[d]++;

    const rightPairs: number[][] = Array.from({ length: 10 }, () => new Array(10).fill(0));
    const seenTmp = new Array(10).fill(0);
    for (let idx = 0; idx < n; ++idx) {
        const d = digits[idx];
        for (let a = 0; a < 10; ++a) {
            rightPairs[a][d] += seenTmp[a];
        }
        seenTmp[d]++;
    }

    let ans = 0;

    for (let k = 0; k < n; ++k) {
        const d = digits[k];

        // remove position k from the right side
        rightCnt[d]--;
        for (let a = 0; a < 10; ++a) {
            if (rightPairs[d][a]) {
                rightPairs[d][a] -= rightCnt[a];
            }
        }
        for (let a = 0; a < 10; ++a) {
            if (rightPairs[a][d]) {
                rightPairs[a][d] -= leftCnt[a];
            }
        }

        // contribution with current center
        let add = 0;
        for (let a = 0; a < 10; ++a) {
            const rowL = leftPairs[a];
            for (let b = 0; b < 10; ++b) {
                const lv = rowL[b];
                if (!lv) continue;
                const rv = rightPairs[b][a];
                if (!rv) continue;
                add = (add + (lv * rv) % MOD) % MOD;
            }
        }
        ans = (ans + add) % MOD;

        // update left side with current position
        for (let a = 0; a < 10; ++a) {
            if (leftCnt[a]) {
                leftPairs[a][d] += leftCnt[a];
            }
        }
        leftCnt[d]++;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromes($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $digits = [];
        for ($i = 0; $i < $n; $i++) {
            $digits[$i] = ord($s[$i]) - 48;
        }

        // Right side counts and pair matrix (total pairs in whole string)
        $cntRight = array_fill(0, 10, 0);
        $pairRight = array_fill(0, 100, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $d = $digits[$i];
            $base = $d * 10;
            for ($a = 0; $a < 10; $a++) {
                $pairRight[$base + $a] += $cntRight[$a];
            }
            $cntRight[$d]++;
        }

        // Left side structures
        $cntLeft = array_fill(0, 10, 0);
        $pairLeft = array_fill(0, 100, 0);
        $ans = 0;

        for ($k = 0; $k < $n; $k++) {
            $center = $digits[$k];

            // Remove current digit from right side
            $cntRight[$center]--;
            $base = $center * 10;
            for ($a = 0; $a < 10; $a++) {
                $pairRight[$base + $a] -= $cntRight[$a];
            }

            // Count palindromes with this center
            for ($a = 0; $a < 10; $a++) {
                $aBase = $a * 10;
                for ($b = 0; $b < 10; $b++) {
                    $leftVal = $pairLeft[$aBase + $b];
                    if ($leftVal == 0) continue;
                    $rightIdx = $b * 10 + $a;
                    $rightVal = $pairRight[$rightIdx];
                    if ($rightVal == 0) continue;
                    $ans = ($ans + ($leftVal % $mod) * ($rightVal % $mod)) % $mod;
                }
            }

            // Update left structures with current digit as second element of pairs
            for ($a = 0; $a < 10; $a++) {
                $pairIdx = $a * 10 + $center;
                $pairLeft[$pairIdx] += $cntLeft[$a];
            }
            $cntLeft[$center]++;
        }

        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countPalindromes(_ s: String) -> Int {
        let MOD: Int64 = 1_000_000_007
        let n = s.count
        if n < 5 { return 0 }
        
        // Convert string to digit array
        var digits = [Int]()
        digits.reserveCapacity(n)
        for scalar in s.unicodeScalars {
            digits.append(Int(scalar.value - 48))
        }
        
        // suffixPairs[pos][b][a] = number of pairs (l,m) with l >= pos, s[l]=b, s[m]=a, l < m
        var suffixPairs = Array(repeating: Int64(0), count: (n + 1) * 100)
        var cntR = Array(repeating: Int64(0), count: 10)
        var pairR = Array(repeating: Array(repeating: Int64(0), count: 10), count: 10)
        
        // Build suffix pairs from right to left
        for i in stride(from: n - 1, through: 0, by: -1) {
            let b = digits[i]
            for a in 0..<10 {
                pairR[b][a] += cntR[a]
            }
            var base = i * 100
            for x in 0..<10 {
                for y in 0..<10 {
                    suffixPairs[base] = pairR[x][y]
                    base += 1
                }
            }
            cntR[b] += 1
        }
        
        // Prefix structures for left side pairs
        var cntL = Array(repeating: Int64(0), count: 10)
        var pairL = Array(repeating: Array(repeating: Int64(0), count: 10), count: 10)
        
        var ans: Int64 = 0
        
        // Iterate each position as the center of palindrome
        for k in 0..<n {
            let baseIdx = (k + 1) * 100
            for a in 0..<10 {
                for b in 0..<10 {
                    let leftCount = pairL[a][b]
                    if leftCount != 0 {
                        let rightCount = suffixPairs[baseIdx + b * 10 + a] // (b,a)
                        ans += (leftCount % MOD) * (rightCount % MOD)
                        if ans >= MOD { ans %= MOD }
                    }
                }
            }
            
            // Update prefix pairs with current digit as the later element
            let cur = digits[k]
            for a in 0..<10 {
                pairL[a][cur] += cntL[a]
            }
            cntL[cur] += 1
        }
        
        return Int(ans % MOD)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun countPalindromes(s: String): Int {
        val MOD = 1_000_000_007L
        val n = s.length
        if (n < 5) return 0
        val digits = IntArray(n) { s[it] - '0' }

        // suffix counts of single digits
        val suffCount = Array(n + 1) { IntArray(10) }
        for (i in n - 1 downTo 0) {
            for (d in 0..9) {
                suffCount[i][d] = suffCount[i + 1][d]
            }
            suffCount[i][digits[i]]++
        }

        // rightPairAfter[i][y][x]: number of ordered pairs (d,e) with d<e, both >= i,
        // s[d]=y, s[e]=x   (mod MOD)
        val rightPair = Array(n + 1) { Array(10) { LongArray(10) } }
        for (i in n - 1 downTo 0) {
            // copy from i+1
            for (y in 0..9) {
                for (x in 0..9) {
                    rightPair[i][y][x] = rightPair[i + 1][y][x]
                }
            }
            val cur = digits[i]
            for (x in 0..9) {
                val cntX = suffCount[i + 1][x].toLong()
                if (cntX != 0L) {
                    var v = rightPair[i][cur][x] + cntX
                    if (v >= MOD) v %= MOD
                    rightPair[i][cur][x] = v
                }
            }
        }

        val prefCount = LongArray(10)
        val leftPair = Array(10) { LongArray(10) }
        var ans = 0L

        for (k in 0 until n) {
            // contributions with center at k
            val rp = rightPair[k + 1]
            for (x in 0..9) {
                for (y in 0..9) {
                    val left = leftPair[x][y]
                    if (left == 0L) continue
                    val right = rp[y][x]
                    if (right == 0L) continue
                    ans += (left * right) % MOD
                    if (ans >= MOD) ans %= MOD
                }
            }

            // update left structures with position k
            val cur = digits[k]
            for (x in 0..9) {
                val cnt = prefCount[x]
                if (cnt != 0L) {
                    var v = leftPair[x][cur] + cnt
                    if (v >= MOD) v %= MOD
                    leftPair[x][cur] = v
                }
            }
            prefCount[cur] = (prefCount[cur] + 1) % MOD
        }

        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countPalindromes(String s) {
    int n = s.length;
    List<int> digits = List<int>.generate(n, (i) => s.codeUnitAt(i) - 48);

    // suffixPairs[i][a*10+b] = number of pairs (p,q) with p<q and p>=i,
    // where s[p]=a and s[q]=b.
    List<List<int>> suffixPairs = List.generate(n + 1, (_) => List.filled(100, 0));
    List<int> cnt = List.filled(10, 0);
    List<int> pairCount = List.filled(100, 0);

    for (int i = n - 1; i >= 0; --i) {
      int d = digits[i];
      for (int d2 = 0; d2 < 10; ++d2) {
        int idx = d * 10 + d2;
        pairCount[idx] += cnt[d2];
        // counts stay within reasonable range, no need to mod here
      }
      cnt[d]++;

      // copy current pairCount into suffixPairs[i]
      List<int> dest = suffixPairs[i];
      for (int idx = 0; idx < 100; ++idx) {
        dest[idx] = pairCount[idx];
      }
    }

    List<int> leftCnt = List.filled(10, 0);
    List<int> leftPair = List.filled(100, 0);
    int ans = 0;

    for (int k = 0; k < n; ++k) {
      List<int> rightPair = suffixPairs[k + 1];
      for (int a = 0; a < 10; ++a) {
        int baseA = a * 10;
        for (int b = 0; b < 10; ++b) {
          int leftVal = leftPair[baseA + b];
          if (leftVal == 0) continue;
          int rightVal = rightPair[b * 10 + a];
          if (rightVal == 0) continue;
          ans = (ans + (leftVal * rightVal) % _MOD) % _MOD;
        }
      }

      // update left structures with current digit as the later element of pairs
      int d = digits[k];
      for (int prev = 0; prev < 10; ++prev) {
        int idx = prev * 10 + d;
        leftPair[idx] += leftCnt[prev];
        if (leftPair[idx] >= _MOD) leftPair[idx] -= _MOD;
      }
      leftCnt[d]++;
      if (leftCnt[d] >= _MOD) leftCnt[d] -= _MOD;
    }

    return ans % _MOD;
  }
}
```

## Golang

```go
package main

import (
	"bufio"
	"os"
)

const MOD int64 = 1000000007

func countPalindromes(s string) int {
	n := len(s)
	if n < 5 {
		return 0
	}

	// pref[i] = counts of digits in s[0..i-1]
	pref := make([][10]int, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i]
		d := s[i] - '0'
		pref[i+1][d]++
	}

	// suff[i] = counts of digits in s[i+1..n-1]
	suff := make([][10]int, n)
	cnt := [10]int{}
	for i := n - 1; i >= 0; i-- {
		suff[i] = cnt
		d := s[i] - '0'
		cnt[d]++
	}

	// rightSumByDigit[b][a] = sum_{pos where digit==b} suff[pos][a]
	rightSum := make([][10]int, 10)
	for i := 0; i < n; i++ {
		b := s[i] - '0'
		for a := 0; a < 10; a++ {
			rightSum[b][a] += suff[i][a]
		}
	}

	leftSum := make([][10]int, 10)
	var ans int64 = 0

	for k := 0; k < n; k++ {
		// remove current position from right side (l must be > k)
		bk := s[k] - '0'
		for a := 0; a < 10; a++ {
			rightSum[bk][a] -= suff[k][a]
		}

		// compute contributions for center k
		for b := 0; b < 10; b++ {
			var contrib int64 = 0
			for a := 0; a < 10; a++ {
				contrib += int64(leftSum[b][a]) * int64(rightSum[b][a])
			}
			ans += contrib
			if ans >= MOD {
				ans %= MOD
			}
		}

		// add current position to left side for future centers
		for a := 0; a < 10; a++ {
			leftSum[bk][a] += pref[k][a]
		}
	}

	return int(ans % MOD)
}

// The following is only needed to make the file compile on LeetCode.
func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	if _, err := fmt.Fscan(in, &s); err == nil {
		fmt.Println(countPalindromes(s))
	}
}
```

## Ruby

```ruby
def count_palindromes(s)
  mod = 1_000_000_007
  n = s.length
  return 0 if n < 5

  digits = s.bytes.map { |b| b - 48 }

  # suffix_pairs[i] stores counts of ordered pairs (b,a) with indices > i
  suffix_digit_counts = Array.new(10, 0)
  suffix_pair_cur = Array.new(100, 0)
  suffix_pairs = Array.new(n) { Array.new(100, 0) }

  (n - 1).downto(0) do |i|
    suffix_pairs[i] = suffix_pair_cur.dup
    d = digits[i]
    10.times do |a|
      idx = d * 10 + a
      suffix_pair_cur[idx] += suffix_digit_counts[a]
    end
    suffix_digit_counts[d] += 1
  end

  prefix_digit_counts = Array.new(10, 0)
  prefix_pair = Array.new(100, 0)

  ans = 0

  n.times do |k|
    right_arr = suffix_pairs[k]

    100.times do |idx|
      left = prefix_pair[idx]
      next if left == 0
      a = idx / 10
      b = idx % 10
      right = right_arr[b * 10 + a]
      next if right == 0
      ans = (ans + left * right) % mod
    end

    c = digits[k]
    10.times do |a|
      idx = a * 10 + c
      prefix_pair[idx] += prefix_digit_counts[a]
    end
    prefix_digit_counts[c] += 1
  end

  ans % mod
end
```

## Scala

```scala
object Solution {
    def countPalindromes(s: String): Int = {
        val MOD = 1000000007L
        val n = s.length
        // suffixPairs[i][y][x] = number of pairs (d,e) with d >= i, e > d, s[d]=y, s[e]=x
        val suffixPairs = Array.ofDim[Long](n + 2, 10, 10)
        val digitCnt = new Array[Long](10)

        var i = n - 1
        while (i >= 0) {
            // copy from i+1
            var a = 0
            while (a < 10) {
                var b = 0
                while (b < 10) {
                    suffixPairs(i)(a)(b) = suffixPairs(i + 1)(a)(b)
                    b += 1
                }
                a += 1
            }
            val c = s.charAt(i) - '0'
            var x = 0
            while (x < 10) {
                suffixPairs(i)(c)(x) += digitCnt(x)
                x += 1
            }
            digitCnt(c) += 1
            i -= 1
        }

        val leftDigitCnt = new Array[Long](10)
        val leftPair = Array.ofDim[Long](10, 10)

        var ans = 0L
        var k = 0
        while (k < n) {
            // use current leftPair and right side suffixPairs[k+1]
            var x = 0
            while (x < 10) {
                var y = 0
                while (y < 10) {
                    val left = leftPair(x)(y)
                    if (left != 0) {
                        val right = suffixPairs(k + 1)(y)(x)
                        if (right != 0) {
                            ans += (left % MOD) * (right % MOD)
                            ans %= MOD
                        }
                    }
                    y += 1
                }
                x += 1
            }

            // update left structures with s[k] for future centers
            val c = s.charAt(k) - '0'
            var d = 0
            while (d < 10) {
                leftPair(d)(c) += leftDigitCnt(d)
                d += 1
            }
            leftDigitCnt(c) += 1

            k += 1
        }

        ((ans % MOD).toInt)
    }
}
```

## Rust

```rust
use std::cmp::min;

impl Solution {
    pub fn count_palindromes(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n < 5 {
            return 0;
        }
        // convert to digits 0..9
        let digits: Vec<usize> = bytes.iter().map(|&b| (b - b'0') as usize).collect();

        // suffix pair counts for each position
        let mut suffix_pairs: Vec<[[i64; 10]; 10]> = vec![[[0i64; 10]; 10]; n];
        let mut cur = [[0i64; 10]; 10];
        let mut cnt_right = [0i64; 10];

        for i in (0..n).rev() {
            suffix_pairs[i] = cur;
            let d = digits[i];
            for a in 0..10 {
                if cnt_right[a] != 0 {
                    cur[d][a] += cnt_right[a];
                }
            }
            cnt_right[d] += 1;
        }

        // iterate centers from left to right
        let mut left_pair = [[0i64; 10]; 10];
        let mut cnt_left = [0i64; 10];
        let mut ans: i64 = 0;

        for c in 0..n {
            let right = &suffix_pairs[c];
            for a in 0..10 {
                for b in 0..10 {
                    let lp = left_pair[a][b];
                    let rp = right[b][a];
                    if lp != 0 && rp != 0 {
                        let add = (lp as i128 * rp as i128) % MOD as i128;
                        ans += add as i64;
                        if ans >= MOD {
                            ans -= MOD;
                        }
                    }
                }
            }

            // update left structures with current character
            let d = digits[c];
            for a in 0..10 {
                if cnt_left[a] != 0 {
                    left_pair[a][d] += cnt_left[a];
                }
            }
            cnt_left[d] += 1;
        }

        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-palindromes s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (digits (make-vector n)))
    ;; convert characters to digits
    (for ([i (in-range n)])
      (vector-set! digits i
                   (- (char->integer (string-ref s i))
                      (char->integer #\0))))
    (if (< n 5)
        0
        (let ((suffix-pairs (make-vector n)))
          ;; compute suffix pair counts for each position
          (let ((cnt (make-vector 10 0))
                (pair-counts (make-vector 100 0)))
            (for ([i (in-range (sub1 n) -1 -1)])
              (vector-set! suffix-pairs i (vector-copy pair-counts))
              (define cur (vector-ref digits i))
              (for ([b (in-range 10)])
                (let* ((idx (+ (* cur 10) b))
                       (inc (vector-ref cnt b)))
                  (vector-set! pair-counts idx
                               (+ (vector-ref pair-counts idx) inc))))
              (vector-set! cnt cur (+ (vector-ref cnt cur) 1))))
          ;; forward pass accumulating answer
          (let ((left-digit (make-vector 10 0))
                (left-pair (make-vector 100 0))
                (result 0))
            (for ([k (in-range n)])
              (define right-pair (vector-ref suffix-pairs k))
              ;; contribution of current center
              (for ([a (in-range 10)]
                    [b (in-range 10)])
                (let* ((left-val (vector-ref left-pair (+ (* a 10) b)))
                       (right-val (vector-ref right-pair (+ (* b 10) a))))
                  (when (and (> left-val 0) (> right-val 0))
                    (set! result
                          (modulo (+ result
                                     (modulo (* left-val right-val) MOD))
                                  MOD)))))
              ;; update left structures with current position
              (define cur (vector-ref digits k))
              (for ([a (in-range 10)])
                (let* ((idx (+ (* a 10) cur))
                       (inc (vector-ref left-digit a)))
                  (vector-set! left-pair idx
                               (+ (vector-ref left-pair idx) inc))))
              (vector-set! left-digit cur
                           (+ (vector-ref left-digit cur) 1)))
            result)))))
```

## Erlang

```erlang
-module(solution).
-compile([export_all]).
-define(MOD, 1000000007).

-spec count_palindromes(S :: unicode:unicode_binary()) -> integer().
count_palindromes(S) ->
    Digits = [C - $0 || C <- binary_to_list(S)],
    N = length(Digits),
    case N < 5 of
        true -> 0;
        false ->
            Zero10 = {0,0,0,0,0,0,0,0,0,0},
            % suffix counts tuple: element(Pos+1) is a 10‑tuple of digit frequencies from Pos to end
            SuffixCounts = build_suffix_counts(Digits, Zero10),
            TotalCount = element(1, SuffixCounts),

            % initial right pairs (all ordered pairs i<j)
            {RightPairs0, _Seen} = build_right_pairs(Digits, Zero10),

            loop(0, Digits, Zero10, zero_matrix(), TotalCount, RightPairs0,
                 SuffixCounts, 0).

%% Build suffix counts tuple
build_suffix_counts(Digits, Zero) ->
    Rev = lists:reverse(Digits),
    {List,_} = lists:foldl(
        fun(Digit,{AccList,Prev}) ->
                New = inc_tuple(Prev, Digit, 1),
                {[New|AccList], New}
        end,
        {[Zero], Zero},
        Rev),
    list_to_tuple(List).

%% Build initial right pairs matrix
build_right_pairs([], _Zero) -> {zero_matrix(), zero_tuple()};
build_right_pairs([Cur|Rest], Zero) ->
    build_right_pairs(Rest, Cur, Zero, zero_matrix(), zero_tuple()).

build_right_pairs([], _Cur, _Zero, RP, Seen) -> {RP, Seen};
build_right_pairs([Cur|Rest], PrevCur, Zero, RP, Seen) ->
    RP1 = add_counts_for_cur(RP, Seen, PrevCur),
    Seen1 = inc_tuple(Seen, PrevCur, 1),
    build_right_pairs(Rest, Cur, Zero, RP1, Seen1).

add_counts_for_cur(RP, Seen, Cur) ->
    lists:foldl(
        fun(A, AccRP) ->
                Cnt = element(A+1, Seen),
                if Cnt =:= 0 -> AccRP;
                   true -> add_to_matrix(AccRP, A, Cur, Cnt)
                end
        end,
        RP,
        lists:seq(0,9)).

%% Main loop over positions
loop(_Idx, [], _LeftCount, _LeftPairs, _RightCount, _RightPairs, _SuffixCounts, Ans) ->
    Ans rem ?MOD;
loop(Idx, [Cur|Rest], LeftCount, LeftPairs, RightCount, RightPairs,
     SuffixCounts, Ans) ->

    % remove current digit from right side
    RightCount1 = dec_tuple(RightCount, Cur, 1),

    LaterRow = element(Idx+2, SuffixCounts),   % counts after position Idx
    RP1 = subtract_first_cur(RightPairs, Cur, LaterRow),
    RP2 = subtract_second_cur(RP1, Cur, LeftCount),

    Contribution = compute_contrib(LeftPairs, RP2),
    Ans1 = (Ans + Contribution) rem ?MOD,

    % update left side with current digit
    LeftPairs1 = add_left_pairs(LeftPairs, Cur, LeftCount),
    LeftCount1 = inc_tuple(LeftCount, Cur, 1),

    loop(Idx+1, Rest, LeftCount1, LeftPairs1, RightCount1, RP2,
         SuffixCounts, Ans1).

subtract_first_cur(RP, Cur, LaterRow) ->
    lists:foldl(
        fun(B, AccRP) ->
                Cnt = element(B+1, LaterRow),
                if Cnt =:= 0 -> AccRP;
                   true -> add_to_matrix(AccRP, Cur, B, -Cnt)
                end
        end,
        RP,
        lists:seq(0,9)).

subtract_second_cur(RP, Cur, LeftCount) ->
    lists:foldl(
        fun(A, AccRP) ->
                Cnt = element(A+1, LeftCount),
                if Cnt =:= 0 -> AccRP;
                   true -> add_to_matrix(AccRP, A, Cur, -Cnt)
                end
        end,
        RP,
        lists:seq(0,9)).

add_left_pairs(LP, Cur, LeftCount) ->
    lists:foldl(
        fun(A, AccLP) ->
                Cnt = element(A+1, LeftCount),
                if Cnt =:= 0 -> AccLP;
                   true -> add_to_matrix(AccLP, A, Cur, Cnt)
                end
        end,
        LP,
        lists:seq(0,9)).

compute_contrib(LeftPairs, RightPairs) ->
    lists:foldl(
        fun(A, SumA) ->
                RowL = element(A+1, LeftPairs),
                lists:foldl(
                    fun(B, SumB) ->
                            Lcnt = element(B+1, RowL),
                            if Lcnt =:= 0 -> SumB;
                               true ->
                                   Rcnt = get_matrix(RightPairs, B, A),
                                   (SumB + (Lcnt * Rcnt) rem ?MOD) rem ?MOD
                            end
                    end,
                    SumA,
                    lists:seq(0,9))
        end,
        0,
        lists:seq(0,9)).

%% Matrix utilities
zero_matrix() ->
    list_to_tuple([{0,0,0,0,0,0,0,0,0,0} || _ <- lists:seq(1,10)]).

add_to_matrix(Matrix, RowIdx, ColIdx, Delta) ->
    Row = element(RowIdx+1, Matrix),
    Old = element(ColIdx+1, Row),
    NewRow = setelement(ColIdx+1, Row, Old + Delta),
    setelement(RowIdx+1, Matrix, NewRow).

get_matrix(Matrix, RowIdx, ColIdx) ->
    Row = element(RowIdx+1, Matrix),
    element(ColIdx+1, Row).

%% Tuple count utilities
inc_tuple(Tuple, Index, Delta) ->
    Old = element(Index+1, Tuple),
    setelement(Index+1, Tuple, Old + Delta).

dec_tuple(Tuple, Index, Delta) ->
    inc_tuple(Tuple, Index, -Delta).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec count_palindromes(s :: String.t()) :: integer
  def count_palindromes(s) do
    mod = 1_000_000_007

    # convert string to list of digit integers
    digits =
      for <<c <- s>>, do: c - ?0

    n = length(digits)

    empty_matrix = fn -> List.duplicate(List.duplicate(0, 10), 10) end

    # ---------- build right pair matrices ----------
    {_, _, right_list} =
      Enum.reduce(Enum.reverse(0..(n - 1)), {empty_matrix.(), List.duplicate(0, 10), []},
        fn i,
           {pair_mat, suffix_cnts, acc} ->
          # store copy for region > i
          new_acc = [Enum.map(pair_mat, & &1) | acc]

          digit = Enum.at(digits, i)

          # update pair matrix with contributions where current digit is the earlier element
          updated_pair_mat =
            Enum.reduce(0..9, pair_mat, fn a, pm ->
              cnt = Enum.at(suffix_cnts, a)

              if cnt == 0 do
                pm
              else
                row = Enum.at(pm, digit)
                new_row = List.replace_at(row, a, Enum.at(row, a) + cnt)
                List.replace_at(pm, digit, new_row)
              end
            end)

          updated_suffix_cnts = List.update_at(suffix_cnts, digit, &(&1 + 1))
          {updated_pair_mat, updated_suffix_cnts, new_acc}
        end)

    # right_list now has matrices for indices 0..n-1 (region > index)
    # ---------- iterate centers ----------
    {_, _, answer} =
      Enum.reduce(0..(n - 1), {List.duplicate(0, 10), empty_matrix.(), 0},
        fn k,
           {left_cnts, left_mat, acc_ans} ->
          right_mat = Enum.at(right_list, k)

          # compute contribution for this center
          contrib =
            Enum.reduce(0..9, 0, fn a, sum_a ->
              row_left = Enum.at(left_mat, a)

              sum_b =
                Enum.reduce(0..9, 0, fn b, sum_b_inner ->
                  left_val = Enum.at(row_left, b)

                  if left_val == 0 do
                    sum_b_inner
                  else
                    right_row = Enum.at(right_mat, b)
                    right_val = Enum.at(right_row, a)
                    rem(sum_b_inner + left_val * right_val, mod)
                  end
                end)

              rem(sum_a + sum_b, mod)
            end)

          new_acc = rem(acc_ans + contrib, mod)

          # update left structures with current digit for future centers
          digit = Enum.at(digits, k)

          updated_left_mat =
            Enum.reduce(0..9, left_mat, fn a, mat_acc ->
              cnt_a = Enum.at(left_cnts, a)

              if cnt_a == 0 do
                mat_acc
              else
                row = Enum.at(mat_acc, a)
                new_row = List.replace_at(row, digit, Enum.at(row, digit) + cnt_a)
                List.replace_at(mat_acc, a, new_row)
              end
            end)

          updated_left_cnts = List.update_at(left_cnts, digit, &(&1 + 1))
          {updated_left_cnts, updated_left_mat, new_acc}
        end)

    answer
  end
end
```
