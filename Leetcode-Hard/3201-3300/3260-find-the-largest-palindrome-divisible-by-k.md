# 3260. Find the Largest Palindrome Divisible by K

## Cpp

```cpp
class Solution {
public:
    string largestPalindrome(int n, int k) {
        if (k == 1) return string(n, '9'); // any number works
        
        int m = (n + 1) / 2;                     // positions to decide
        vector<int> pow10(n);
        pow10[0] = 1 % k;
        for (int i = 1; i < n; ++i) {
            pow10[i] = (pow10[i - 1] * 10) % k;
        }
        // coefficient for each position in the first half
        vector<int> coeff(m);
        for (int idx = 0; idx < m; ++idx) {
            int leftExp = n - 1 - idx;   // exponent of the leftmost digit
            int rightExp = idx;          // exponent of its mirror
            int c = pow10[leftExp];
            if (leftExp != rightExp) c = (c + pow10[rightExp]) % k;
            coeff[idx] = c % k;
        }
        // dp[pos][rem] : using positions pos..m-1 we can obtain remainder rem
        vector<vector<char>> dp(m + 1, vector<char>(k, 0));
        dp[m][0] = 1;
        for (int pos = m - 1; pos >= 0; --pos) {
            for (int remNext = 0; remNext < k; ++remNext) if (dp[pos + 1][remNext]) {
                for (int d = 0; d <= 9; ++d) {
                    if (pos == 0 && d == 0) continue; // no leading zero
                    int newRem = (d * coeff[pos] + remNext) % k;
                    dp[pos][newRem] = 1;
                }
            }
        }
        // construct the answer greedily
        string left(m, '0');
        int need = 0; // remainder we still need to achieve with remaining positions
        for (int pos = 0; pos < m; ++pos) {
            for (int d = 9; d >= (pos == 0 ? 1 : 0); --d) {
                int contrib = (d * coeff[pos]) % k;
                int remNext = need - contrib;
                remNext %= k;
                if (remNext < 0) remNext += k;
                if (dp[pos + 1][remNext]) {
                    left[pos] = char('0' + d);
                    need = remNext;
                    break;
                }
            }
        }
        // build full palindrome
        string ans(n, ' ');
        for (int i = 0; i < m; ++i) ans[i] = left[i];
        for (int i = m; i < n; ++i) ans[i] = ans[n - 1 - i];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String largestPalindrome(int n, int k) {
        if (k == 1) {
            char[] allNine = new char[n];
            java.util.Arrays.fill(allNine, '9');
            return new String(allNine);
        }
        int m = (n + 1) / 2;
        int[] pow = new int[n];
        pow[0] = 1 % k;
        for (int i = 1; i < n; i++) {
            pow[i] = (pow[i - 1] * 10) % k;
        }
        int[] coeff = new int[m];
        for (int i = 0; i < m; i++) {
            if (i == n - 1 - i) {
                coeff[i] = pow[n - 1 - i] % k;
            } else {
                coeff[i] = (pow[n - 1 - i] + pow[i]) % k;
            }
        }

        boolean[][] dp = new boolean[m + 1][k];
        dp[m][0] = true;
        for (int pos = m - 1; pos >= 0; pos--) {
            for (int rem = 0; rem < k; rem++) {
                if (!dp[pos + 1][rem]) continue;
                int startDigit = (pos == 0) ? 1 : 0;
                for (int d = startDigit; d <= 9; d++) {
                    int newRem = (d * coeff[pos] + rem) % k;
                    dp[pos][newRem] = true;
                }
            }
        }

        StringBuilder left = new StringBuilder();
        int curRem = 0;
        for (int pos = 0; pos < m; pos++) {
            int startDigit = (pos == 0) ? 1 : 0;
            for (int d = 9; d >= startDigit; d--) {
                int newRem = (curRem + d * coeff[pos]) % k;
                int need = (k - newRem) % k;
                if (dp[pos + 1][need]) {
                    left.append((char) ('0' + d));
                    curRem = newRem;
                    break;
                }
            }
        }

        StringBuilder res = new StringBuilder();
        res.append(left);
        if ((n & 1) == 1) {
            res.append(new StringBuilder(left.substring(0, left.length() - 1)).reverse());
        } else {
            res.append(new StringBuilder(left).reverse());
        }
        return res.toString();
    }
}
```

## Python

```python
class Solution(object):
    def largestPalindrome(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # precompute 10^i mod k for i = 0 .. n-1
        pow_mod = [1 % k]
        for _ in range(1, n):
            pow_mod.append((pow_mod[-1] * 10) % k)

        m = (n + 1) // 2  # number of free positions (first half)
        weights = []
        for p in range(m):
            i = p
            j = n - 1 - p
            if i == j:
                w = pow_mod[i]
            else:
                w = (pow_mod[i] + pow_mod[n - 1 - i]) % k
            weights.append(w)

        # dp[pos][rem] = can achieve remainder rem using positions pos..m-1
        dp = [bytearray(k) for _ in range(m + 1)]
        dp[m][0] = 1

        for pos in range(m - 1, -1, -1):
            w = weights[pos]
            nxt = dp[pos + 1]
            cur = dp[pos]
            for rem_next in range(k):
                if not nxt[rem_next]:
                    continue
                # try all digits 0..9 (pos==0 later handled in construction)
                for d in range(10):
                    total = (d * w + rem_next) % k
                    cur[total] = 1

        # construct the answer greedily
        res_half = []
        pref_mod = 0
        for pos in range(m):
            w = weights[pos]
            for d in range(9, -1, -1):
                if pos == 0 and d == 0:
                    continue
                new_pref = (pref_mod + d * w) % k
                need_suffix = (-new_pref) % k
                if dp[pos + 1][need_suffix]:
                    res_half.append(str(d))
                    pref_mod = new_pref
                    break

        left = ''.join(res_half)
        if n % 2 == 0:
            palindrome = left + left[::-1]
        else:
            palindrome = left + left[-2::-1]  # skip the middle character when mirroring
        return palindrome
```

## Python3

```python
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        m = (n + 1) // 2  # independent positions
        # precompute powers of 10 modulo k
        pow_mod = [1 % k]
        for _ in range(1, n):
            pow_mod.append((pow_mod[-1] * 10) % k)
        # compute weight for each independent position
        weights = []
        for i in range(m):
            j = n - 1 - i
            if i == j:
                w = pow_mod[i] % k
            else:
                w = (pow_mod[i] + pow_mod[j]) % k
            weights.append(w)
        full_mask = (1 << k) - 1
        # dp_masks[pos] = bitmask of remainders achievable from pos to end
        dp_masks = [0] * (m + 1)
        dp_masks[m] = 1 << 0  # only remainder 0 with no positions left
        for idx in range(m - 1, -1, -1):
            mask_next = dp_masks[idx + 1]
            cur_mask = 0
            digit_range = range(1, 10) if idx == 0 else range(0, 10)
            w = weights[idx]
            for d in digit_range:
                contrib = (d * w) % k
                if contrib == 0:
                    shifted = mask_next
                else:
                    # rotate left by contrib bits within k bits
                    shifted = ((mask_next << contrib) | (mask_next >> (k - contrib))) & full_mask
                cur_mask |= shifted
            dp_masks[idx] = cur_mask
        # construct answer greedily
        res = [''] * n
        cur_rem = 0
        for i in range(m):
            w = weights[i]
            digit_range = range(9, 0, -1) if i == 0 else range(9, -1, -1)
            for d in digit_range:
                new_rem = (cur_rem + d * w) % k
                needed = (-new_rem) % k
                if dp_masks[i + 1] >> needed & 1:
                    res[i] = str(d)
                    res[n - 1 - i] = str(d)
                    cur_rem = new_rem
                    break
        return ''.join(res)
```

## C

```c
#include <stdlib.h>

char* largestPalindrome(int n, int k) {
    // precompute powers of 10 modulo k
    int *pow10 = (int*)malloc(n * sizeof(int));
    pow10[0] = 1 % k;
    for (int i = 1; i < n; ++i) {
        pow10[i] = (pow10[i - 1] * 10) % k;
    }

    int half = (n + 1) / 2;                     // number of independent positions
    int *factor = (int*)malloc(half * sizeof(int));
    for (int pos = 0; pos < half; ++pos) {
        int leftIdx = n - 1 - pos;              // exponent for the left digit
        if (pos == n - 1 - pos) {               // middle position in odd length
            factor[pos] = pow10[leftIdx] % k;
        } else {
            factor[pos] = (pow10[leftIdx] + pow10[pos]) % k;
        }
    }

    // dp[pos][rem] : can we achieve remainder rem using positions pos..half-1 ?
    char *dp = (char*)calloc((half + 1) * k, sizeof(char));
    dp[half * k + 0] = 1;                       // base case

    for (int pos = half - 1; pos >= 0; --pos) {
        for (int remPrev = 0; remPrev < k; ++remPrev) {
            if (!dp[(pos + 1) * k + remPrev]) continue;
            int dStart = (pos == 0 ? 1 : 0);
            for (int d = dStart; d <= 9; ++d) {
                int newRem = (d * factor[pos] + remPrev) % k;
                dp[pos * k + newRem] = 1;
            }
        }
    }

    // construct the answer greedily
    char *ans = (char*)malloc((n + 1) * sizeof(char));
    int curRem = 0;
    for (int pos = 0; pos < half; ++pos) {
        int dStart = (pos == 0 ? 1 : 0);
        for (int d = 9; d >= dStart; --d) {
            int newRem = (curRem + d * factor[pos]) % k;
            int need = (k - newRem) % k;
            if (dp[(pos + 1) * k + need]) {
                ans[pos] = '0' + d;
                curRem = newRem;
                break;
            }
        }
    }

    // mirror to complete the palindrome
    for (int i = half; i < n; ++i) {
        ans[i] = ans[n - 1 - i];
    }
    ans[n] = '\0';

    free(pow10);
    free(factor);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestPalindrome(int n, int k) {
        // Precompute powers of 10 modulo k
        int[] pow = new int[n];
        if (k == 1) {
            // All numbers are divisible by 1, answer is all '9's
            return new string('9', n);
        }
        pow[0] = 1 % k;
        for (int i = 1; i < n; i++) {
            pow[i] = (pow[i - 1] * 10) % k;
        }

        int halfLen = n / 2;
        bool hasCenter = (n % 2 == 1);
        int totalVars = halfLen + (hasCenter ? 1 : 0);
        int[] weights = new int[totalVars];

        // Weights for the mirrored positions
        for (int i = 0; i < halfLen; i++) {
            int w = (pow[n - 1 - i] + pow[i]) % k;
            weights[i] = w;
        }
        if (hasCenter) {
            int mid = halfLen; // index of center
            weights[mid] = pow[halfLen] % k;
        }

        // suffixMask[pos] : bitmask of remainders achievable from pos to end
        int[] suffixMask = new int[totalVars + 1];
        suffixMask[totalVars] = 1 << 0; // empty suffix gives remainder 0

        for (int pos = totalVars - 1; pos >= 0; pos--) {
            int w = weights[pos];
            int mask = 0;
            for (int d = 0; d <= 9; d++) {
                int add = (d * w) % k;
                int prev = suffixMask[pos + 1];
                // combine each reachable remainder from the suffix
                for (int r = 0; r < k; r++) {
                    if ((prev & (1 << r)) != 0) {
                        int nr = (r + add) % k;
                        mask |= 1 << nr;
                    }
                }
            }
            suffixMask[pos] = mask;
        }

        // Greedy construction of digits
        int[] chosen = new int[totalVars];
        int curRem = 0;
        for (int pos = 0; pos < totalVars; pos++) {
            int startDigit = 9;
            int minDigit = (pos == 0) ? 1 : 0;
            for (int d = startDigit; d >= minDigit; d--) {
                int newRem = (curRem + d * weights[pos]) % k;
                int need = (k - newRem) % k;
                if ((suffixMask[pos + 1] & (1 << need)) != 0) {
                    chosen[pos] = d;
                    curRem = newRem;
                    break;
                }
            }
        }

        // Build the palindrome string
        char[] res = new char[n];
        for (int i = 0; i < halfLen; i++) {
            char c = (char)('0' + chosen[i]);
            res[i] = c;
            res[n - 1 - i] = c;
        }
        if (hasCenter) {
            res[halfLen] = (char)('0' + chosen[totalVars - 1]);
        }

        return new string(res);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var largestPalindrome = function(n, k) {
    // precompute powers of 10 modulo k
    const pow = new Array(n);
    pow[0] = 1 % k;
    for (let i = 1; i < n; ++i) {
        pow[i] = (pow[i - 1] * 10) % k;
    }

    const m = Math.ceil(n / 2); // independent positions
    const w = new Array(m);
    for (let i = 0; i < m; ++i) {
        if (i === n - 1 - i) { // middle of odd length
            w[i] = pow[i];
        } else {
            w[i] = (pow[n - 1 - i] + pow[i]) % k;
        }
    }

    const fullMask = 1 << k; // not used directly, just for size reference
    const dp = new Array(m + 1);
    dp[m] = 1 << 0; // only remainder 0 achievable after all positions

    // build DP from right to left
    for (let pos = m - 1; pos >= 0; --pos) {
        let curMask = 0;
        const weight = w[pos];
        const nextMask = dp[pos + 1];
        for (let d = 0; d <= 9; ++d) {
            const contrib = (d * weight) % k;
            // combine with all remainders reachable from suffix
            for (let r = 0; r < k; ++r) {
                if ((nextMask >> r) & 1) {
                    const nr = (contrib + r) % k;
                    curMask |= 1 << nr;
                }
            }
        }
        dp[pos] = curMask;
    }

    // construct the largest palindrome
    const digits = new Array(n);
    let needRem = 0; // we want total remainder 0 at the end

    for (let pos = 0; pos < m; ++pos) {
        const weight = w[pos];
        const startDigit = (pos === 0) ? 9 : 9;
        const minDigit = (pos === 0) ? 1 : 0;
        let chosen = -1;
        for (let d = startDigit; d >= minDigit; --d) {
            const contrib = (d * weight) % k;
            const requiredPrev = (needRem - contrib) % k;
            const need = requiredPrev < 0 ? requiredPrev + k : requiredPrev;
            if ((dp[pos + 1] >> need) & 1) {
                chosen = d;
                needRem = need; // update needed remainder for the suffix
                break;
            }
        }
        // chosen must exist per problem guarantee
        digits[pos] = chosen;
        digits[n - 1 - pos] = chosen;
    }

    return digits.join('');
};
```

## Typescript

```typescript
function largestPalindrome(n: number, k: number): string {
    const m = Math.ceil(n / 2);
    // precompute 10^i mod k for i=0..n-1
    const powMod: number[] = new Array(n);
    if (k === 1) {
        // all powers are 0 modulo 1, but we keep as 0 to avoid NaN
        powMod.fill(0);
    } else {
        powMod[0] = 1 % k;
        for (let i = 1; i < n; ++i) {
            powMod[i] = (powMod[i - 1] * 10) % k;
        }
    }

    // compute weight for each position in the first half
    const weights: number[] = new Array(m);
    for (let i = 0; i < m; ++i) {
        const leftPow = powMod[n - 1 - i];
        const rightPow = powMod[i];
        if (i === n - 1 - i) {
            weights[i] = leftPow % k;
        } else {
            weights[i] = (leftPow + rightPow) % k;
        }
    }

    // dp[i] : bitmask of remainders achievable using positions i..m-1
    const dp: Uint32Array = new Uint32Array(m + 1);
    dp[m] = 1 << 0; // only remainder 0

    for (let i = m - 1; i >= 0; --i) {
        let mask = 0;
        const w = weights[i];
        const startDigit = i === 0 ? 1 : 0;
        for (let d = startDigit; d <= 9; ++d) {
            const contrib = (d * w) % k;
            const suffixMask = dp[i + 1];
            // iterate over possible remainders in suffixMask
            for (let r = 0; r < k; ++r) {
                if ((suffixMask & (1 << r)) !== 0) {
                    const newRem = (contrib + r) % k;
                    mask |= 1 << newRem;
                }
            }
        }
        dp[i] = mask;
    }

    // construct the largest palindrome greedily
    let curTarget = 0; // we need total remainder 0 for suffix i..end
    const halfDigits: number[] = new Array(m);
    for (let i = 0; i < m; ++i) {
        const w = weights[i];
        const minDigit = i === 0 ? 1 : 0;
        let chosen = -1;
        for (let d = 9; d >= minDigit; --d) {
            const contrib = (d * w) % k;
            let needed = curTarget - contrib;
            needed %= k;
            if (needed < 0) needed += k;
            if ((dp[i + 1] & (1 << needed)) !== 0) {
                chosen = d;
                curTarget = needed; // new target for the remaining suffix
                break;
            }
        }
        halfDigits[i] = chosen; // guaranteed to find a digit
    }

    // build full palindrome string
    const chars: string[] = new Array(n);
    for (let i = 0; i < m; ++i) {
        const ch = String(halfDigits[i]);
        chars[i] = ch;
        chars[n - 1 - i] = ch;
    }
    return chars.join('');
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function largestPalindrome($n, $k) {
        // precompute 10^i mod k
        $pow = [];
        $pow[0] = 1 % $k;
        for ($i = 1; $i < $n; $i++) {
            $pow[$i] = ($pow[$i - 1] * 10) % $k;
        }

        $pairCount = intdiv($n, 2);
        $m = $pairCount + ($n % 2); // total independent positions
        $weights = [];

        for ($i = 0; $i < $pairCount; $i++) {
            $w = ($pow[$n - 1 - $i] + $pow[$i]) % $k;
            $weights[] = $w;
        }
        if ($n % 2 == 1) {
            $midIdx = $pairCount;
            $weights[] = $pow[$midIdx] % $k;
        }

        // DP suffix: dp[pos][rem] => can we achieve remainder rem from pos..end
        $dp = array_fill(0, $m + 1, array_fill(0, $k, false));
        $dp[$m][0] = true;

        for ($pos = $m - 1; $pos >= 0; $pos--) {
            $w = $weights[$pos];
            for ($rem = 0; $rem < $k; $rem++) {
                $ok = false;
                for ($d = 0; $d <= 9; $d++) {
                    $target = ($rem - ($d * $w) % $k + $k) % $k;
                    if ($dp[$pos + 1][$target]) {
                        $ok = true;
                        break;
                    }
                }
                $dp[$pos][$rem] = $ok;
            }
        }

        // Greedy construction
        $cur = 0;
        $chosen = [];
        for ($pos = 0; $pos < $m; $pos++) {
            $w = $weights[$pos];
            $start = 9;
            $end = 0;
            if ($pos == 0) $end = 1; // leading digit cannot be zero
            for ($d = $start; $d >= $end; $d--) {
                $newCur = ($cur + ($d * $w) % $k) % $k;
                $need = ($k - $newCur) % $k;
                if ($dp[$pos + 1][$need]) {
                    $chosen[] = $d;
                    $cur = $newCur;
                    break;
                }
            }
        }

        // Build palindrome string
        if ($n % 2 == 0) {
            $firstHalf = $chosen; // length pairCount
            $secondHalf = array_reverse($firstHalf);
            $digits = array_merge($firstHalf, $secondHalf);
        } else {
            $firstHalf = array_slice($chosen, 0, $pairCount);
            $midDigit = $chosen[$pairCount];
            $secondHalf = array_reverse($firstHalf);
            $digits = array_merge($firstHalf, [$midDigit], $secondHalf);
        }

        return implode('', $digits);
    }
}
```

## Swift

```swift
class Solution {
    func largestPalindrome(_ n: Int, _ k: Int) -> String {
        if n == 0 { return "" }
        // Precompute powers of 10 modulo k
        var powMod = [Int](repeating: 0, count: n)
        powMod[0] = 1 % k
        if n > 1 {
            for i in 1..<n {
                powMod[i] = (powMod[i - 1] * 10) % k
            }
        }
        let leftLen = (n + 1) / 2
        var weight = [Int](repeating: 0, count: leftLen)
        for i in 0..<leftLen {
            if n % 2 == 1 && i == leftLen - 1 { // middle digit for odd length
                weight[i] = powMod[n - 1 - i] % k
            } else {
                let a = powMod[n - 1 - i]
                let b = powMod[i]
                weight[i] = (a + b) % k
            }
        }
        // suffix DP: mask of achievable remainders from position idx to end
        var suffixMask = [UInt16](repeating: 0, count: leftLen + 1)
        suffixMask[leftLen] = 1 << 0   // only remainder 0 is possible with no digits
        if k == 1 {
            // all remainders are 0, masks stay as only bit 0 set
            for idx in stride(from: leftLen - 1, through: 0, by: -1) {
                suffixMask[idx] = 1 << 0
            }
        } else {
            for idx in stride(from: leftLen - 1, through: 0, by: -1) {
                var curMask: UInt16 = 0
                let w = weight[idx]
                let digitStart = (idx == 0) ? 1 : 0
                for d in digitStart...9 {
                    let add = (d * w) % k
                    let nextMask = suffixMask[idx + 1]
                    for r in 0..<k {
                        if ((nextMask >> r) & 1) == 1 {
                            let newR = (r + add) % k
                            curMask |= UInt16(1 << newR)
                        }
                    }
                }
                suffixMask[idx] = curMask
            }
        }
        // Greedy construction of left half
        var chosenDigits = [Int]()
        var curRem = 0
        for idx in 0..<leftLen {
            let w = weight[idx]
            var selected = -1
            let digitRange: StrideThrough<Int> = (idx == 0) ? stride(from: 9, through: 1, by: -1) : stride(from: 9, through: 0, by: -1)
            for d in digitRange {
                let newRem = (curRem + d * w) % k
                let need = (k - newRem) % k
                if ((suffixMask[idx + 1] >> need) & 1) == 1 {
                    selected = d
                    curRem = newRem
                    break
                }
            }
            // solution always exists, so selected will be set
            chosenDigits.append(selected)
        }
        // Build full palindrome string
        var chars = [Character]()
        for d in chosenDigits {
            chars.append(Character(UnicodeScalar(48 + d)!))
        }
        let revStart = (n % 2 == 0) ? leftLen - 1 : leftLen - 2
        if revStart >= 0 {
            for i in stride(from: revStart, through: 0, by: -1) {
                let d = chosenDigits[i]
                chars.append(Character(UnicodeScalar(48 + d)!))
            }
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPalindrome(n: Int, k: Int): String {
        val mod = k
        // Precompute powers of 10 modulo k
        val pow = IntArray(n)
        var cur = 1 % mod
        for (i in 0 until n) {
            pow[i] = cur
            cur = (cur * 10) % mod
        }
        val pairs = n / 2
        val steps = pairs + if (n % 2 == 1) 1 else 0
        val w = IntArray(steps)
        for (i in 0 until pairs) {
            w[i] = (pow[n - 1 - i] + pow[i]) % mod
        }
        if (n % 2 == 1) {
            w[steps - 1] = pow[pairs] % mod
        }

        // suffixPossible[pos][rem] = can we achieve remainder rem using positions pos..end-1
        val suffix = Array(steps + 1) { BooleanArray(mod) }
        suffix[steps][0] = true
        for (i in steps - 1 downTo 0) {
            for (rem in 0 until mod) if (suffix[i + 1][rem]) {
                for (d in 0..9) {
                    val added = (d * w[i]) % mod
                    val newRem = (added + rem) % mod
                    suffix[i][newRem] = true
                }
            }
        }

        val res = CharArray(n)
        var prefixRem = 0
        for (i in 0 until steps) {
            val leftIdx = i
            val rightIdx = n - 1 - i
            var chosen = -1
            for (d in 9 downTo 0) {
                if (i == 0 && d == 0) continue // no leading zero
                val added = (d * w[i]) % mod
                val newRem = (prefixRem + added) % mod
                val need = (mod - newRem) % mod
                if (suffix[i + 1][need]) {
                    chosen = d
                    prefixRem = newRem
                    res[leftIdx] = ('0'.code + d).toChar()
                    if (leftIdx != rightIdx) {
                        res[rightIdx] = ('0'.code + d).toChar()
                    }
                    break
                }
            }
            // solution always exists per problem statement
        }
        return String(res)
    }
}
```

## Dart

```dart
class Solution {
  String largestPalindrome(int n, int k) {
    // Precompute powers of 10 modulo k
    List<int> pow10 = List.filled(n + 1, 0);
    pow10[0] = 1 % k;
    for (int i = 1; i <= n; ++i) {
      pow10[i] = (pow10[i - 1] * 10) % k;
    }

    int m = (n + 1) >> 1; // number of independent positions
    List<int> weight = List.filled(m, 0);
    for (int i = 0; i < m; ++i) {
      if (i == n - 1 - i) {
        weight[i] = pow10[i];
      } else {
        weight[i] = (pow10[n - 1 - i] + pow10[i]) % k;
      }
    }

    // suffix[pos][rem] = can we achieve remainder rem using positions pos..m-1
    List<List<int>> suffix = List.generate(m + 1, (_) => List.filled(k, 0));
    suffix[m][0] = 1;

    for (int pos = m - 1; pos >= 0; --pos) {
      for (int rem = 0; rem < k; ++rem) {
        bool ok = false;
        for (int d = 0; d <= 9; ++d) {
          if (pos == 0 && d == 0) continue; // no leading zero
          int prev = rem - d * weight[pos];
          prev %= k;
          if (prev < 0) prev += k;
          if (suffix[pos + 1][prev] == 1) {
            ok = true;
            break;
          }
        }
        suffix[pos][rem] = ok ? 1 : 0;
      }
    }

    // Build the largest palindrome greedily
    StringBuffer firstHalf = StringBuffer();
    int need = 0; // remainder we still need to achieve
    for (int pos = 0; pos < m; ++pos) {
      for (int d = 9; d >= 0; --d) {
        if (pos == 0 && d == 0) continue;
        int prev = need - d * weight[pos];
        prev %= k;
        if (prev < 0) prev += k;
        if (suffix[pos + 1][prev] == 1) {
          firstHalf.write(d);
          need = prev;
          break;
        }
      }
    }

    String left = firstHalf.toString();
    List<int> revCodes = left.codeUnits.reversed.toList();
    String right = String.fromCharCodes(revCodes);
    if (n % 2 == 0) {
      return left + right;
    } else {
      // remove the duplicated middle character
      return left + right.substring(1);
    }
  }
}
```

## Golang

```go
func largestPalindrome(n int, k int) string {
	if k == 1 {
		ans := make([]byte, n)
		for i := range ans {
			ans[i] = '9'
		}
		return string(ans)
	}

	// pow[i] = 10^i % k
	pow := make([]int, n)
	pow[0] = 1 % k
	for i := 1; i < n; i++ {
		pow[i] = (pow[i-1] * 10) % k
	}

	half := (n + 1) / 2
	coeff := make([]int, half)
	for idx := 0; idx < half; idx++ {
		leftPos := idx
		rightPos := n - 1 - idx
		if leftPos == rightPos { // center of odd length
			exp := n - 1 - leftPos
			coeff[idx] = pow[exp]
		} else {
			expLeft := n - 1 - leftPos
			expRight := n - 1 - rightPos // equals leftPos
			coeff[idx] = (pow[expLeft] + pow[expRight]) % k
		}
	}

	// dp[pos][rem] = can achieve remainder rem using positions pos..half-1
	dp := make([][]bool, half+1)
	for i := 0; i <= half; i++ {
		dp[i] = make([]bool, k)
	}
	dp[half][0] = true

	for pos := half - 1; pos >= 0; pos-- {
		cur := dp[pos]
		next := dp[pos+1]
		c := coeff[pos] % k
		for rPrev := 0; rPrev < k; rPrev++ {
			if !next[rPrev] {
				continue
			}
			for d := 0; d <= 9; d++ {
				if pos == 0 && d == 0 {
					continue
				}
				newRem := (c*d + rPrev) % k
				cur[newRem] = true
			}
		}
	}

	// Greedy construction of the first half
	resHalf := make([]byte, half)
	needRem := 0
	for pos := 0; pos < half; pos++ {
		c := coeff[pos] % k
		chosen := -1
		for d := 9; d >= 0; d-- {
			if pos == 0 && d == 0 {
				continue
			}
			contrib := (c * d) % k
			suffixNeed := (needRem - contrib) % k
			if suffixNeed < 0 {
				suffixNeed += k
			}
			if dp[pos+1][suffixNeed] {
				chosen = d
				needRem = suffixNeed
				break
			}
		}
		if chosen == -1 { // should never happen
			chosen = 0
		}
		resHalf[pos] = byte('0' + chosen)
	}

	// Build full palindrome
	ans := make([]byte, n)
	for i := 0; i < half; i++ {
		ans[i] = resHalf[i]
		ans[n-1-i] = resHalf[i]
	}
	return string(ans)
}
```

## Ruby

```ruby
def largest_palindrome(n, k)
  # precompute 10^{position} mod k for each position from left to right
  pow = Array.new(n)
  cur = 1 % k
  i = n - 1
  while i >= 0
    pow[i] = cur
    cur = (cur * 10) % k
    i -= 1
  end

  mid = (n + 1) / 2
  coeff = Array.new(mid)
  i = 0
  while i < mid
    j = n - 1 - i
    if i == j
      coeff[i] = pow[i] % k
    else
      coeff[i] = (pow[i] + pow[j]) % k
    end
    i += 1
  end

  # masks[pos] : bitmask of remainders achievable from pos..mid-1
  masks = Array.new(mid + 1, 0)
  masks[mid] = 1 << 0

  i = mid - 1
  while i >= 0
    mask = 0
    digits = (i == 0 ? (1..9) : (0..9))
    digits.each do |d|
      add = (coeff[i] * d) % k
      next_mask = masks[i + 1]
      r = 0
      while r < k
        if (next_mask & (1 << r)) != 0
          new_rem = (add + r) % k
          mask |= 1 << new_rem
        end
        r += 1
      end
    end
    masks[i] = mask
    i -= 1
  end

  # greedy construction of the first half
  cur = 0
  first_half = []
  i = 0
  while i < mid
    chosen = nil
    d_range = (i == 0 ? (9).downto(1) : (9).downto(0))
    d_range.each do |d|
      add = (coeff[i] * d) % k
      need = (k - (cur + add) % k) % k
      if (masks[i + 1] & (1 << need)) != 0
        chosen = d
        cur = (cur + add) % k
        first_half << d
        break
      end
    end
    i += 1
  end

  # build full palindrome string
  if n.even?
    pal_digits = first_half + first_half.reverse
  else
    pal_digits = first_half + first_half[0...-1].reverse
  end
  pal_digits.map(&:to_s).join
end
```

## Scala

```scala
object Solution {
    def largestPalindrome(n: Int, k: Int): String = {
        // precompute 10^exp % k for exp = 0 .. n-1
        val powMod = new Array[Int](n)
        if (k != 0) {
            powMod(0) = 1 % k
            var i = 1
            while (i < n) {
                powMod(i) = (powMod(i - 1) * 10) % k
                i += 1
            }
        }

        val m = (n + 1) / 2                     // number of independent positions
        val coeff = new Array[Int](m)

        var idx = 0
        while (idx < m) {
            val j = n - 1 - idx
            if (idx == j) {                     // middle position when n is odd
                coeff(idx) = powMod(idx) % k
            } else {
                coeff(idx) = (powMod(idx) + powMod(j)) % k
            }
            idx += 1
        }

        // suffix DP using bitmask of reachable remainders
        val suffixMask = new Array[Int](m + 1)
        suffixMask(m) = 1 << 0                     // only remainder 0 is possible with no digits

        var i = m - 1
        while (i >= 0) {
            var mask = 0
            val c = coeff(i)
            val nextMask = suffixMask(i + 1)
            var rem = 0
            while (rem < k) {
                if ((nextMask >> rem) & 1 == 1) {
                    var d = 0
                    while (d <= 9) {
                        val newRem = (rem + d * c) % k
                        mask |= 1 << newRem
                        d += 1
                    }
                }
                rem += 1
            }
            suffixMask(i) = mask
            i -= 1
        }

        // greedy construction of the largest palindrome
        val chosen = new Array[Int](m)
        var curRem = 0
        i = 0
        while (i < m) {
            val minDigit = if (i == 0) 1 else 0
            var d = 9
            var placed = false
            while (d >= minDigit && !placed) {
                val newRem = (curRem + d * coeff(i)) % k
                val need = (k - newRem) % k
                if ((suffixMask(i + 1) >> need) & 1 == 1) {
                    chosen(i) = d
                    curRem = newRem
                    placed = true
                }
                d -= 1
            }
            i += 1
        }

        // build the final palindrome string
        val chars = new Array[Char](n)
        i = 0
        while (i < m) {
            val ch = (chosen(i) + '0').toChar
            chars(i) = ch
            chars(n - 1 - i) = ch
            i += 1
        }
        new String(chars)
    }
}
```

## Rust

```rust
use std::iter::FromIterator;

impl Solution {
    pub fn largest_palindrome(n: i32, k: i32) -> String {
        let n_us = n as usize;
        let k_us = k as usize;
        // precompute 10^i mod k
        let mut pow = vec![0usize; n_us];
        if n_us > 0 {
            pow[0] = 1 % k_us;
            for i in 1..n_us {
                pow[i] = (pow[i - 1] * 10) % k_us;
            }
        }

        let m = (n_us + 1) / 2; // number of independent positions
        let mut coeffs = vec![0usize; m];
        for idx in 0..m {
            let left = idx;
            let right = n_us - 1 - idx;
            if left < right {
                coeffs[idx] = (pow[left] + pow[right]) % k_us;
            } else {
                // center of odd length
                coeffs[idx] = pow[left] % k_us;
            }
        }

        // dp[pos][rem] = can we achieve remainder rem using positions pos..m-1
        let mut dp = vec![vec![false; k_us]; m + 1];
        dp[m][0] = true;
        for pos in (0..m).rev() {
            let c = coeffs[pos];
            for d in 0..=9 {
                if pos == 0 && d == 0 {
                    continue; // leading zero not allowed
                }
                let delta = (c * d) % k_us;
                for rem_next in 0..k_us {
                    if dp[pos + 1][rem_next] {
                        let rem = (delta + rem_next) % k_us;
                        dp[pos][rem] = true;
                    }
                }
            }
        }

        // construct the largest palindrome
        let mut half = vec![0u8; m];
        let mut need = 0usize; // remainder we still need to achieve
        for pos in 0..m {
            let c = coeffs[pos];
            for d in (0..=9).rev() {
                if pos == 0 && d == 0 {
                    continue;
                }
                let delta = (c * d) % k_us;
                let needed_suffix = (need + k_us - delta) % k_us;
                if dp[pos + 1][needed_suffix] {
                    half[pos] = d as u8;
                    need = needed_suffix;
                    break;
                }
            }
        }

        // build full palindrome string
        let mut chars = vec!['0'; n_us];
        for i in 0..m {
            let ch = (b'0' + half[i]) as char;
            chars[i] = ch;
            chars[n_us - 1 - i] = ch;
        }
        String::from_iter(chars)
    }
}
```

## Racket

```racket
(define/contract (largest-palindrome n k)
  (-> exact-integer? exact-integer? string?)
  (let* ([modk k]
         [pow (let loop ([i 0] [vec (make-vector n)])
                (if (= i n)
                    vec
                    (begin
                      (vector-set! vec i (if (= i 0) (modulo 1 modk)
                                            (modulo (* (vector-ref vec (- i 1)) 10) modk)))
                      (loop (+ i 1) vec))))] ; pow[i] = 10^i % k
         [m (quotient (+ n 1) 2)] ; number of independent positions
         ;; compute weights for each independent position (from most significant side)
         [weights (let loop ([i 0] [vec (make-vector m)])
                    (if (= i m)
                        vec
                        (let* ([L (- n 1 i)]
                               [R i]
                               [w (if (= L R)
                                      (vector-ref pow L)
                                      (modulo (+ (vector-ref pow L) (vector-ref pow R)) modk))])
                          (vector-set! vec i w)
                          (loop (+ i 1) vec))))]

    ;; DP suffix masks: dp[i] = bitmask of reachable remainders using positions i..m-1
    (let loop-dp ([i (- m 1)] [next-mask 1] ; only remainder 0 reachable after end
                  [dp (make-vector (+ m 1) 0)])
      (vector-set! dp (+ i 1) next-mask) ; store for position i+1
      (if (< i 0)
          (let* ([digits (let build ([pos 0] [cur-mod 0] [out '()])
                           (if (= pos m)
                               (reverse out)
                               (let* ([w (vector-ref weights pos)]
                                      [digit-range (if (= pos 0) (range 9 -1 -1) (range 9 -1 -1))])
                                 (define chosen
                                   (for/first ([d digit-range]
                                               #:when (not (and (= pos 0) (= d 0)))
                                               #:let ([new-mod (modulo (+ cur-mod (* d w)) modk)]
                                                      [need (modulo (- new-mod) modk)])
                                               (if (bitwise-bit-set? (vector-ref dp (+ pos 1)) need)
                                                   d
                                                   #f)))
                                 (build (+ pos 1) (modulo (+ cur-mod (* chosen w)) modk) (cons chosen out))))))

                 ;; build final string
                 [result-str
                  (let* ([char-list (map (lambda (d) (integer->char (+ d 48))) digits)])
                    (if (even? n)
                        (list->string (append char-list (reverse char-list)))
                        (let* ([left (take char-list (- m 1))]
                               [mid (list-ref char-list (- m 1))])
                          (list->string (append left (list mid) (reverse left)))))))]

            result-str)
          (let* ([w (vector-ref weights i)]
                 [mask 0])
            (for ([r (in-range modk)])
              (when (bitwise-bit-set? next-mask r)
                (for ([d (in-range 10)])
                  (define nr (modulo (+ (* d w) r) modk))
                  (set! mask (bitwise-ior mask (arithmetic-shift 1 nr))))))
            (loop-dp (- i 1) mask dp))))))
```

## Erlang

```erlang
-spec largest_palindrome(N :: integer(), K :: integer()) -> unicode:unicode_binary().
largest_palindrome(N, K) ->
    PowTuple = list_to_tuple(pow_list(N, K)),
    M = (N + 1) div 2,
    Weights = weights(N, M, K, PowTuple),
    Masks = masks_build(Weights, K),                     % size M+1
    DigitsRev = build_digits(Weights, tl(Masks), K),    % digits collected reversed
    FirstHalf = lists:reverse(DigitsRev),
    SecondHalf =
        case N rem 2 of
            0 -> lists:reverse(FirstHalf);
            1 -> lists:reverse(tl(FirstHalf))
        end,
    FullDigits = FirstHalf ++ SecondHalf,
    list_to_binary([ $0 + D || D <- FullDigits ]).

%% generate list of powers 10^i mod K for i=0..N-1
pow_list(N, K) -> pow_list(N, K, [], 1 rem K).
pow_list(0, _K, Acc, _Cur) -> lists:reverse(Acc);
pow_list(N, K, Acc, Cur) ->
    pow_list(N - 1, K, [Cur | Acc], (Cur * 10) rem K).

%% compute weight for each position i (0‑based) of the first half
weights(N, M, K, PowTuple) -> weights(0, N, M, K, PowTuple, []).
weights(I, _N, M, _K, _PowTuple, Acc) when I =:= M ->
    lists:reverse(Acc);
weights(I, N, M, K, PowTuple, Acc) ->
    LeftExp  = N - 1 - I,
    RightExp = I,
    LeftVal  = element(LeftExp + 1, PowTuple),
    W =
        case I * 2 == N - 1 of
            true -> LeftVal rem K;                     % middle digit (odd length)
            false ->
                RightVal = element(RightExp + 1, PowTuple),
                (LeftVal + RightVal) rem K
        end,
    weights(I + 1, N, M, K, PowTuple, [W | Acc]).

%% build suffix masks: mask[i] = set of remainders reachable from position i
masks_build(Weights, K) ->
    InitialMask = 1 bsl 0,
    {MasksRev, _} = masks_rev(lists:reverse(Weights), K, InitialMask, []),
    lists:reverse(MasksRev) ++ [InitialMask].

masks_rev([], _K, MaskNext, Acc) -> {Acc, MaskNext};
masks_rev([W | Rest], K, MaskNext, Acc) ->
    MaskI = compute_mask(W, K, MaskNext),
    masks_rev(Rest, K, MaskI, [MaskI | Acc]).

compute_mask(W, K, MaskNext) ->
    compute_mask_digits(0, W, K, MaskNext, 0).

compute_mask_digits(D, _W, _K, _MaskNext, AccMask) when D > 9 -> AccMask;
compute_mask_digits(D, W, K, MaskNext, AccMask) ->
    Add = (D * W) rem K,
    NewMask = add_remainders(Add, K, MaskNext, AccMask),
    compute_mask_digits(D + 1, W, K, MaskNext, NewMask).

add_remainders(_Add, _K, 0, AccMask) -> AccMask;   % no bits set
add_remainders(Add, K, MaskNext, AccMask) ->
    add_remainders(0, Add, K, MaskNext, AccMask).

add_remainders(R, Add, K, MaskNext, AccMask) when R >= K -> AccMask;
add_remainders(R, Add, K, MaskNext, AccMask) ->
    case (MaskNext band (1 bsl R)) of
        0 ->
            add_remainders(R + 1, Add, K, MaskNext, AccMask);
        _ ->
            NewR = (Add + R) rem K,
            Updated = AccMask bor (1 bsl NewR),
            add_remainders(R + 1, Add, K, MaskNext, Updated)
    end.

%% construct the largest palindrome digits (first half), returned reversed
build_digits(Weights, MasksTail, K) ->
    build_digits(Weights, MasksTail, K, 0, [], true).

build_digits([], [], _K, _CurMod, Acc, _First) -> Acc;
build_digits([W | Ws], [NextMask | RestMasks], K, CurMod, Acc, First) ->
    DigitsRange = if First -> lists:seq(9,1,-1); true -> lists:seq(9,0,-1) end,
    Needed = (K - CurMod) rem K,
    D = choose_digit(DigitsRange, W, K, Needed, NextMask),
    Add = (D * W) rem K,
    NewCur = (CurMod + Add) rem K,
    build_digits(Ws, RestMasks, K, NewCur, [D | Acc], false).

choose_digit([], _W, _K, _Needed, _NextMask) -> 0;
choose_digit([D | Ds], W, K, Needed, NextMask) ->
    Add = (D * W) rem K,
    Target0 = Needed - Add,
    Target = if Target0 < 0 -> Target0 + K; true -> Target0 end,
    case (NextMask band (1 bsl Target)) of
        0 -> choose_digit(Ds, W, K, Needed, NextMask);
        _ -> D
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_palindrome(n :: integer, k :: integer) :: String.t
  def largest_palindrome(n, k) do
    require Integer
    import Bitwise

    # precompute 10^i mod k
    pow = :array.new(n + 1)
    pow = :array.set(0, Integer.mod(1, k), pow)

    pow =
      Enum.reduce(1..n, pow, fn i, acc ->
        prev = :array.get(i - 1, acc)
        val = Integer.mod(prev * 10, k)
        :array.set(i, val, acc)
      end)

    pairs = div(n, 2)
    total_units = pairs + rem(n, 2)

    # contribution function
    contrib_fun = fn u, d ->
      if u < pairs do
        i = u
        left_pow = :array.get(n - 1 - i, pow)
        right_pow = :array.get(i, pow)
        Integer.mod((left_pow + right_pow) * d, k)
      else
        mid_pow = :array.get(pairs, pow)
        Integer.mod(mid_pow * d, k)
      end
    end

    # DP masks: dp[u] is bitmask of reachable remainders from unit u to end
    dp = :array.new(total_units + 1)
    dp = :array.set(total_units, 1 <<< 0, dp)

    dp =
      Enum.reduce((total_units - 1)..0, dp, fn u, acc_dp ->
        prev_mask = :array.get(u + 1, acc_dp)

        new_mask =
          Enum.reduce(0..(k - 1), 0, fn r, mask_acc ->
            if (prev_mask &&& (1 <<< r)) != 0 do
              Enum.reduce(0..9, mask_acc, fn d, inner_acc ->
                c = contrib_fun.(u, d)
                nr = Integer.mod(r + c, k)
                inner_acc ||| (1 <<< nr)
              end)
            else
              mask_acc
            end
          end)

        :array.set(u, new_mask, acc_dp)
      end)

    # construct answer
    ans = :array.new(n)
    rem_needed = 0

    {ans_final, _} =
      Enum.reduce(0..(total_units - 1), {ans, rem_needed}, fn u, {cur_ans, cur_rem} ->
        digit_list = Enum.reverse(0..9)

        chosen_digit =
          Enum.reduce_while(digit_list, nil, fn d, _acc ->
            if u == 0 and d == 0 do
              {:cont, nil}
            else
              c = contrib_fun.(u, d)
              next_rem = Integer.mod(cur_rem - c, k)
              next_mask = :array.get(u + 1, dp)

              if (next_mask &&& (1 <<< next_rem)) != 0 do
                {:halt, d}
              else
                {:cont, nil}
              end
            end
          end) || 0

        updated_ans =
          if u < pairs do
            left_pos = u
            right_pos = n - 1 - u
            ch = ?0 + chosen_digit

            cur_ans
            |> :array.set(left_pos, ch)
            |> :array.set(right_pos, ch)
          else
            mid_pos = pairs
            ch = ?0 + chosen_digit
            :array.set(cur_ans, mid_pos, ch)
          end

        next_rem = Integer.mod(cur_rem - contrib_fun.(u, chosen_digit), k)
        {updated_ans, next_rem}
      end)

    chars =
      for i <- 0..(n - 1) do
        :array.get(i, ans_final)
      end

    List.to_string(chars)
  end
end
```
