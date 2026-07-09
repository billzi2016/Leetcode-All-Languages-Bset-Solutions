# 3463. Check If Digits Are Equal in String After Operations II

## Cpp

```cpp
class Solution {
public:
    // precomputed small binomial coefficients modulo 5
    static int comb5[5][5];
    static bool initComb5() {
        for (int n = 0; n < 5; ++n) {
            comb5[n][0] = comb5[n][n] = 1 % 5;
            for (int k = 1; k < n; ++k)
                comb5[n][k] = (comb5[n-1][k-1] + comb5[n-1][k]) % 5;
        }
        return true;
    }
    static int nCk_mod5(int n, int k) {
        if (k < 0 || k > n) return 0;
        int res = 1;
        while (n > 0 || k > 0) {
            int ni = n % 5;
            int ki = k % 5;
            if (ki > ni) return 0;
            res = (res * comb5[ni][ki]) % 5;
            n /= 5;
            k /= 5;
        }
        return res;
    }

    bool hasSameDigits(string s) {
        static bool initialized = initComb5();
        (void)initialized; // silence unused warning
        int n = (int)s.size();
        if (n == 2) return s[0] == s[1];
        vector<int> d(n);
        for (int i = 0; i < n; ++i) d[i] = s[i] - '0';
        int N = n - 2; // length of Pascal row used

        // sum modulo 2
        int sum2 = 0;
        for (int i = 0; i <= N; ++i) {
            // C(N,i) is odd iff (i & (N-i)) == 0
            if ((i & (N - i)) == 0) {
                int diffParity = (d[i] & 1) ^ (d[i + 1] & 1); // subtraction mod 2 equals xor
                sum2 ^= diffParity; // addition modulo 2 is xor
            }
        }

        // sum modulo 5
        int sum5 = 0;
        for (int i = 0; i <= N; ++i) {
            int c = nCk_mod5(N, i);
            if (c == 0) continue;
            int diff = d[i] - d[i + 1];
            diff %= 5;
            if (diff < 0) diff += 5;
            sum5 = (sum5 + c * diff) % 5;
        }

        // combine using CRT to get result modulo 10
        int combined = -1;
        for (int x = sum5; x < 10; x += 5) {
            if ((x & 1) == sum2) { // x % 2 == sum2
                combined = x;
                break;
            }
        }
        return combined == 0;
    }
};
```

## Java

```java
class Solution {
    private static final int[][] C5 = new int[5][5];
    static {
        for (int n = 0; n < 5; n++) {
            C5[n][0] = C5[n][n] = 1;
            for (int k = 1; k < n; k++) {
                C5[n][k] = (C5[n - 1][k - 1] + C5[n - 1][k]) % 5;
            }
        }
    }

    private int binomMod5(int n, int k) {
        if (k < 0 || k > n) return 0;
        int res = 1;
        while (n > 0 || k > 0) {
            int ni = n % 5;
            int ki = k % 5;
            if (ki > ni) return 0;
            res = (res * C5[ni][ki]) % 5;
            n /= 5;
            k /= 5;
        }
        return res;
    }

    private int binomMod2(int n, int k) {
        if (k < 0 || k > n) return 0;
        // Lucas for p=2: C(n,k) is odd iff (k & (n - k)) == 0
        return ((k & (n - k)) == 0) ? 1 : 0;
    }

    private int binomMod10(int n, int k) {
        if (k < 0 || k > n) return 0;
        int mod2 = binomMod2(n, k);
        int mod5 = binomMod5(n, k);
        // combine using CRT: find x in [0,9] with given residues
        int x = mod5;
        if ((x & 1) != mod2) {
            x = (mod5 + 5) % 10; // adding 5 flips parity
        }
        return x;
    }

    public boolean hasSameDigits(String s) {
        int n = s.length();
        int k = n - 2; // number of operations performed
        int sum0 = 0;
        int sum1 = 0;
        for (int i = 0; i < n; i++) {
            int digit = s.charAt(i) - '0';
            int c0 = binomMod10(k, i);
            int c1 = binomMod10(k, i - 1);
            sum0 = (sum0 + digit * c0) % 10;
            sum1 = (sum1 + digit * c1) % 10;
        }
        return sum0 == sum1;
    }
}
```

## Python

```python
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        N = n - 2  # row of binomial coefficients

        # precompute C(n,k) mod 5 for n,k in [0..4]
        small_comb_mod5 = [[0]*5 for _ in range(5)]
        for i in range(5):
            small_comb_mod5[i][0] = 1
            small_comb_mod5[i][i] = 1
            for j in range(1, i):
                small_comb_mod5[i][j] = (small_comb_mod5[i-1][j-1] + small_comb_mod5[i-1][j]) % 5

        # CRT table for modulus 2 and 5 -> modulus 10
        crt = {}
        for x in range(10):
            crt[(x % 2, x % 5)] = x

        def binom_mod5(N, K):
            res = 1
            while N > 0 or K > 0:
                ni = N % 5
                ki = K % 5
                if ki > ni:
                    return 0
                res = (res * small_comb_mod5[ni][ki]) % 5
                N //= 5
                K //= 5
            return res

        ans = 0
        for i in range(N + 1):
            diff = int(s[i]) - int(s[i + 1])
            if diff == 0:
                continue
            # binom mod 2 using Lucas (Kummer) property
            c2 = 1 if ((i & (N - i)) == 0) else 0
            c5 = binom_mod5(N, i)
            coeff = crt[(c2, c5)]  # value modulo 10
            ans = (ans + coeff * diff) % 10

        return ans % 10 == 0
```

## Python3

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n == 2:
            return s[0] == s[1]

        # precompute factorials and inverse factorials for primes 2 and 5
        fact2 = [1, 1]
        inv_fact2 = [1, 1]

        fact5 = [1] * 5
        inv_fact5 = [1] * 5
        for i in range(1, 5):
            fact5[i] = (fact5[i - 1] * i) % 5
        inv_fact5[4] = pow(fact5[4], 3, 5)  # Fermat inverse since 5 is prime
        for i in range(3, -1, -1):
            inv_fact5[i] = (inv_fact5[i + 1] * (i + 1)) % 5

        def binom_mod_prime(nn: int, kk: int, p: int, fact, inv_fact) -> int:
            if kk < 0 or kk > nn:
                return 0
            res = 1
            while nn > 0 or kk > 0:
                ni = nn % p
                ki = kk % p
                if ki > ni:
                    return 0
                # C(ni,ki) mod p using precomputed factorials
                cur = fact[ni]
                cur = (cur * inv_fact[ki]) % p
                cur = (cur * inv_fact[ni - ki]) % p
                res = (res * cur) % p
                nn //= p
                kk //= p
            return res

        def binom_mod_10(nn: int, kk: int) -> int:
            a = binom_mod_prime(nn, kk, 2, fact2, inv_fact2)
            b = binom_mod_prime(nn, kk, 5, fact5, inv_fact5)
            # combine using CRT: x ≡ a (mod 2), x ≡ b (mod 5)
            return (5 * a + 6 * b) % 10

        total = int(s[0]) % 10
        k = n - 3  # row index for binomial coefficients
        # i ranges from 1 to n-3 inclusive
        for i in range(1, n - 2):
            coeff = binom_mod_10(k, i)
            total = (total + coeff * int(s[i])) % 10

        total = (total - int(s[-1])) % 10
        return total == 0
```

## C

```c
#include <stdbool.h>
#include <string.h>

static int comb2[2][2];
static int comb5[5][5];

static void init_combinations() {
    for (int n = 0; n < 2; ++n) {
        for (int k = 0; k <= n; ++k) {
            if (k == 0 || k == n) comb2[n][k] = 1 % 2;
            else comb2[n][k] = (comb2[n-1][k-1] + comb2[n-1][k]) % 2;
        }
    }
    for (int n = 0; n < 5; ++n) {
        for (int k = 0; k <= n; ++k) {
            if (k == 0 || k == n) comb5[n][k] = 1 % 5;
            else comb5[n][k] = (comb5[n-1][k-1] + comb5[n-1][k]) % 5;
        }
    }
}

static int C_mod_prime(int N, int K, int p) {
    if (K < 0 || K > N) return 0;
    int res = 1;
    while (N > 0 || K > 0) {
        int ni = N % p;
        int ki = K % p;
        if (ki > ni) return 0;
        if (p == 2)
            res = (res * comb2[ni][ki]) % 2;
        else
            res = (res * comb5[ni][ki]) % 5;
        N /= p;
        K /= p;
    }
    return res;
}

bool hasSameDigits(char* s) {
    static bool initialized = false;
    if (!initialized) {
        init_combinations();
        initialized = true;
    }

    int n = (int)strlen(s);
    if (n == 2) return s[0] == s[1];

    int N = n - 2;               // number of reduction steps
    int total = 0;                // sum modulo 10

    for (int i = 0; i <= N; ++i) {
        int a_i   = s[i]     - '0';
        int a_nxt = s[i + 1] - '0';
        int diff = a_i - a_nxt;
        diff %= 10;
        if (diff < 0) diff += 10;

        int b2 = C_mod_prime(N, i, 2);   // C(N,i) mod 2
        int b5 = C_mod_prime(N, i, 5);   // C(N,i) mod 5

        int cmod = (5 * b2 + 6 * b5) % 10;   // CRT to get modulo 10

        total = (total + cmod * diff) % 10;
    }

    return total == 0;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private static readonly int[,] Comb5 = InitComb5();

    private static int[,] InitComb5()
    {
        var arr = new int[5, 5];
        for (int i = 0; i < 5; i++)
        {
            arr[i, 0] = 1;
            arr[i, i] = 1;
            for (int j = 1; j < i; j++)
                arr[i, j] = (arr[i - 1, j - 1] + arr[i - 1, j]) % 5;
        }
        return arr;
    }

    private static int Cmod2(int n, int k)
    {
        // C(n,k) is odd iff (k & (n-k)) == 0
        return ((k & (n - k)) == 0) ? 1 : 0;
    }

    private static int Cmod5(int n, int k)
    {
        if (k < 0 || k > n) return 0;
        int res = 1;
        while (n > 0 || k > 0)
        {
            int ni = n % 5;
            int ki = k % 5;
            if (ki > ni) return 0;
            res = (res * Comb5[ni, ki]) % 5;
            n /= 5;
            k /= 5;
        }
        return res;
    }

    private static int Cmod10(int n, int k)
    {
        int a = Cmod2(n, k); // mod 2
        int b = Cmod5(n, k); // mod 5
        // CRT: x ≡ a (mod 2), x ≡ b (mod 5) => x = (5*a + 6*b) % 10
        return (5 * a + 6 * b) % 10;
    }

    public bool HasSameDigits(string s)
    {
        int n = s.Length;
        int m = n - 2; // number of operations to reach length 2
        int[] digits = new int[n];
        for (int i = 0; i < n; i++) digits[i] = s[i] - '0';

        int diffSumMod10 = 0;
        for (int i = 0; i <= m; i++)
        {
            int diff = digits[i] - digits[i + 1];
            diff %= 10;
            if (diff < 0) diff += 10;

            int coeff = Cmod10(m, i);
            diffSumMod10 = (diffSumMod10 + diff * coeff) % 10;
        }

        return diffSumMod10 == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    const n = s.length;
    const N = n - 2; // row index for binomial coefficients
    
    // precompute C(a,b) mod 5 for a,b in [0,4]
    const comb5 = Array.from({length:5},()=>Array(5).fill(0));
    for (let i=0;i<5;i++){
        comb5[i][0]=comb5[i][i]=1%5;
        for(let j=1;j<i;j++){
            comb5[i][j]=(comb5[i-1][j-1]+comb5[i-1][j])%5;
        }
    }
    
    // binomial modulo 5 using Lucas theorem
    function binomMod5Lucas(nn, kk){
        if (kk<0 || kk>nn) return 0;
        let res = 1;
        while (nn > 0 || kk > 0) {
            const ni = nn % 5;
            const ki = kk % 5;
            if (ki > ni) return 0;
            res = (res * comb5[ni][ki]) % 5;
            nn = Math.floor(nn / 5);
            kk = Math.floor(kk / 5);
        }
        return res;
    }
    
    // binomial modulo 2: odd iff (k & (n-k)) == 0
    function binomMod2(nn, kk){
        if (kk<0 || kk>nn) return 0;
        return ((kk & (nn - kk)) === 0) ? 1 : 0;
    }
    
    // combine using CRT: x ≡ c2 (mod2), x ≡ c5 (mod5)
    function binomMod10(nn, kk){
        const c2 = binomMod2(nn, kk);
        const c5 = binomMod5Lucas(nn, kk);
        return (5 * c2 + 6 * c5) % 10;
    }
    
    let sum1 = 0; // first final digit
    let sum2 = 0; // second final digit
    
    for (let i = 0; i < n; ++i) {
        const d = s.charCodeAt(i) - 48; // digit value
        
        if (i <= N) {
            const coeff1 = binomMod10(N, i);
            sum1 = (sum1 + coeff1 * d) % 10;
        }
        if (i - 1 >= 0 && i - 1 <= N) {
            const coeff2 = binomMod10(N, i - 1);
            sum2 = (sum2 + coeff2 * d) % 10;
        }
    }
    
    return sum1 === sum2;
};
```

## Typescript

```typescript
function hasSameDigits(s: string): boolean {
    const n = s.length;
    const N = n - 2; // number of reduction steps
    const digits = Array.from(s, ch => ch.charCodeAt(0) - 48);

    // precompute C mod 5 for values 0..4
    const comb5: number[][] = Array.from({ length: 5 }, () => Array(5).fill(0));
    for (let i = 0; i < 5; ++i) {
        comb5[i][0] = comb5[i][i] = 1 % 5;
        for (let j = 1; j < i; ++j) {
            comb5[i][j] = (comb5[i - 1][j - 1] + comb5[i - 1][j]) % 5;
        }
    }

    const binomMod2 = (n: number, k: number): number => ((k & (n - k)) === 0 ? 1 : 0);

    const binomMod5 = (n: number, k: number): number => {
        let res = 1;
        while (n > 0 || k > 0) {
            const ni = n % 5;
            const ki = k % 5;
            if (ki > ni) return 0;
            res = (res * comb5[ni][ki]) % 5;
            n = Math.floor(n / 5);
            k = Math.floor(k / 5);
        }
        return res;
    };

    const binomMod10 = (n: number, k: number): number => {
        const a = binomMod2(n, k); // mod 2
        const b = binomMod5(n, k); // mod 5
        let x = b; // candidate modulo 10
        while ((x & 1) !== a) { // adjust to satisfy mod 2 condition
            x += 5;
        }
        return x % 10;
    };

    let left = 0;
    let right = 0;
    for (let i = 0; i <= N; ++i) {
        const coeff = binomMod10(N, i);
        left = (left + coeff * digits[i]) % 10;
        right = (right + coeff * digits[i + 1]) % 10;
    }
    return left === right;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function hasSameDigits($s) {
        $n = strlen($s);
        if ($n < 3) return false; // not needed per constraints

        // split digits into array of ints
        $digits = array_map('intval', str_split($s));

        $N = $n - 2; // number of operations

        // precompute small binomial tables for mod 2 and mod 5
        $smallC2 = [];
        for ($i = 0; $i < 2; $i++) {
            $smallC2[$i] = array_fill(0, $i + 1, 0);
            $smallC2[$i][0] = 1;
            $smallC2[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $smallC2[$i][$j] = ($smallC2[$i - 1][$j - 1] + $smallC2[$i - 1][$j]) % 2;
            }
        }

        $smallC5 = [];
        for ($i = 0; $i < 5; $i++) {
            $smallC5[$i] = array_fill(0, $i + 1, 0);
            $smallC5[$i][0] = 1;
            $smallC5[$i][$i] = 1;
            for ($j = 1; $j < $i; $j++) {
                $smallC5[$i][$j] = ($smallC5[$i - 1][$j - 1] + $smallC5[$i - 1][$j]) % 5;
            }
        }

        // Lucas theorem for prime p
        $lucas = function($n, $k, $p, $table) {
            $res = 1;
            while ($n > 0 || $k > 0) {
                $ni = $n % $p;
                $ki = $k % $p;
                if ($ki > $ni) return 0;
                $res = ($res * $table[$ni][$ki]) % $p;
                $n = intdiv($n, $p);
                $k = intdiv($k, $p);
            }
            return $res;
        };

        $sum1 = 0;
        $sum2 = 0;

        for ($i = 0; $i <= $N; $i++) {
            $c2 = $lucas($N, $i, 2, $smallC2);
            $c5 = $lucas($N, $i, 5, $smallC5);
            // CRT to combine modulo 2 and 5 into modulo 10
            $coeff = (5 * $c2 + 6 * $c5) % 10;

            $sum1 = ($sum1 + $coeff * $digits[$i]) % 10;
            $sum2 = ($sum2 + $coeff * $digits[$i + 1]) % 10;
        }

        return $sum1 === $sum2;
    }
}
```

## Swift

```swift
class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        let digits = s.map { Int(String($0))! }
        let n = digits.count
        if n == 2 { return digits[0] == digits[1] }
        let N = n - 2
        
        // Precompute C(a,b) mod 5 for 0 <= a,b < 5
        var comb5 = Array(repeating: Array(repeating: 0, count: 5), count: 5)
        for a in 0..<5 {
            comb5[a][0] = 1
            comb5[a][a] = 1
            if a >= 2 {
                for b in 1..<(a) {
                    comb5[a][b] = (comb5[a - 1][b - 1] + comb5[a - 1][b]) % 5
                }
            }
        }
        
        func binomMod5(_ N: Int, _ K: Int) -> Int {
            var n = N
            var k = K
            var res = 1
            while n > 0 || k > 0 {
                let nd = n % 5
                let kd = k % 5
                if kd > nd { return 0 }
                res = (res * comb5[nd][kd]) % 5
                n /= 5
                k /= 5
            }
            return res
        }
        
        var sum0 = 0
        var sum1 = 0
        
        for i in 0...N {
            // C(N,i) mod 2: odd iff (i & (N - i)) == 0
            let r2 = ((i & (N - i)) == 0) ? 1 : 0
            // C(N,i) mod 5 via Lucas theorem
            let r5 = binomMod5(N, i)
            // Combine to get modulo 10 using CRT
            let parity = r5 & 1
            var t = (r2 - parity) % 2
            if t < 0 { t += 2 }
            let coeff = (r5 + 5 * t) % 10
            
            sum0 = (sum0 + coeff * digits[i]) % 10
            sum1 = (sum1 + coeff * digits[i + 1]) % 10
        }
        
        return sum0 == sum1
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val comb2 = arrayOf(
        intArrayOf(1),
        intArrayOf(1, 1)
    )
    private val comb5 = Array(5) { IntArray(it + 1) }

    init {
        for (n in 0..4) {
            for (k in 0..n) {
                var res = 1
                for (i in 1..k) {
                    res = res * (n - i + 1) / i
                }
                comb5[n][k] = res % 5
            }
        }
    }

    private fun combModPrimeLucas(n: Long, k: Long, p: Int): Int {
        var nn = n
        var kk = k
        var res = 1
        while (nn > 0 || kk > 0) {
            val ni = (nn % p).toInt()
            val ki = (kk % p).toInt()
            if (ki > ni) return 0
            val small = if (p == 2) comb2[ni][ki] else comb5[ni][ki]
            res = (res * small) % p
            nn /= p
            kk /= p
        }
        return res
    }

    private fun combMod10(n: Long, k: Long): Int {
        val a = combModPrimeLucas(n, k, 2) // mod 2
        val b = combModPrimeLucas(n, k, 5) // mod 5
        // CRT combine: x ≡ a (mod2), x ≡ b (mod5)
        return (5 * a + 6 * b) % 10
    }

    fun hasSameDigits(s: String): Boolean {
        val n = s.length
        if (n < 3) return false
        val N = (n - 2).toLong()
        var first = 0
        for (i in 0 until n - 1) {
            val coeff = combMod10(N, i.toLong())
            first = (first + coeff * (s[i] - '0')) % 10
        }
        var second = 0
        for (i in 1 until n) {
            val coeff = combMod10(N, (i - 1).toLong())
            second = (second + coeff * (s[i] - '0')) % 10
        }
        return first == second
    }
}
```

## Dart

```dart
class Solution {
  // Precomputed binomial coefficients C(n,k) modulo 5 for 0 <= n,k < 5
  static const List<List<int>> _smallC = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 2, 1, 0, 0],
    [1, 3, 3, 1, 0],
    [1, 4, 6 % 5, 4, 1],
  ];

  int _binomMod5(int n, int k) {
    if (k < 0 || k > n) return 0;
    int res = 1;
    while (n > 0 || k > 0) {
      int ni = n % 5;
      int ki = k % 5;
      if (ki > ni) return 0;
      res = (res * _smallC[ni][ki]) % 5;
      n ~/= 5;
      k ~/= 5;
    }
    return res;
  }

  bool hasSameDigits(String s) {
    int n = s.length;
    if (n < 3) return false; // per constraints this won't happen
    List<int> digits = List<int>.generate(n, (i) => s.codeUnitAt(i) - 48);
    int t = n - 2; // number of operations performed

    int sumMod2 = 0;
    int sumMod5 = 0;

    for (int i = 0; i <= t; ++i) {
      int diff = digits[i] - digits[i + 1];
      int diffMod2 = ((diff % 2) + 2) % 2;
      int diffMod5 = ((diff % 5) + 5) % 5;

      // C(t, i) modulo 2: odd iff (i & (t - i)) == 0
      int cMod2 = ((i & (t - i)) == 0) ? 1 : 0;
      sumMod2 = (sumMod2 + cMod2 * diffMod2) % 2;

      int cMod5 = _binomMod5(t, i);
      sumMod5 = (sumMod5 + cMod5 * diffMod5) % 5;
    }

    // Combine using CRT: x ≡ sumMod2 (mod 2), x ≡ sumMod5 (mod 5)
    int combined = (5 * sumMod2 + 6 * sumMod5) % 10; // because inv(2,5)=3, 2*3=6
    return combined == 0;
  }
}
```

## Golang

```go
func hasSameDigits(s string) bool {
	n := len(s)
	if n < 3 {
		return false
	}
	N := n - 2

	// precompute C(ni,ki) mod 5 for ni,ki in [0,4]
	var comb5 [5][5]int
	fact := [5]int{1, 1, 2, 6 % 5, 24 % 5}
	invFact := [5]int{1, 1, 3, 2, 4} // modular inverses modulo 5 (since 5 is prime)
	for i := 0; i <= 4; i++ {
		for k := 0; k <= i; k++ {
			comb5[i][k] = fact[i]
			comb5[i][k] = comb5[i][k] * invFact[k] % 5
			comb5[i][k] = comb5[i][k] * invFact[i-k] % 5
		}
	}

	// helper: C(N,k) mod 2 using Lucas (property of binomial modulo 2)
	mod2 := func(N, k int) int {
		if k < 0 || k > N {
			return 0
		}
		if (k & (N - k)) == 0 {
			return 1
		}
		return 0
	}

	// helper: C(N,k) mod 5 using Lucas with precomputed comb5
	var lucasMod5 func(int, int) int
	lucasMod5 = func(N, k int) int {
		if k < 0 || k > N {
			return 0
		}
		res := 1
		for N > 0 || k > 0 {
			ni := N % 5
			ki := k % 5
			if ki > ni {
				return 0
			}
			res = res * comb5[ni][ki] % 5
			N /= 5
			k /= 5
		}
		return res
	}

	// helper: C(N,k) mod 10 using CRT from mod2 and mod5
	binomMod10 := func(N, k int) int {
		if k < 0 || k > N {
			return 0
		}
		a := mod2(N, k)          // modulo 2
		b := lucasMod5(N, k)     // modulo 5
		return (5*a + 6*b) % 10 // CRT combine: x = 5*a + 6*b (mod 10)
	}

	leftSum := 0
	rightSum := 0
	for i := 0; i < n; i++ {
		digit := int(s[i] - '0')
		if i <= N {
			c := binomMod10(N, i)
			leftSum = (leftSum + c*digit) % 10
		}
		if i >= 1 && i-1 <= N {
			c := binomMod10(N, i-1)
			rightSum = (rightSum + c*digit) % 10
		}
	}
	return leftSum == rightSum
}
```

## Ruby

```ruby
SMALL2 = [[1,0],[1,1]]

SMALL5 = Array.new(5) { Array.new(5, 0) }
(0...5).each do |n|
  (0..n).each do |k|
    if k == 0 || k == n
      SMALL5[n][k] = 1
    else
      SMALL5[n][k] = (SMALL5[n - 1][k - 1] + SMALL5[n - 1][k]) % 5
    end
  end
end

def comb_mod_prime(n, k, p, small)
  return 0 if k < 0 || k > n
  res = 1
  while n > 0 || k > 0
    ni = n % p
    ki = k % p
    return 0 if ki > ni
    res = (res * small[ni][ki]) % p
    n /= p
    k /= p
  end
  res
end

def combine_mod2_5(a, b)
  (5 * a + 6 * b) % 10
end

# @param {String} s
# @return {Boolean}
def has_same_digits(s)
  digits = s.bytes.map { |b| b - 48 }
  n = digits.length
  return false if n < 3
  nn = n - 2

  sum1 = 0
  sum2 = 0

  (0..nn).each do |i|
    c2 = comb_mod_prime(nn, i, 2, SMALL2)
    c5 = comb_mod_prime(nn, i, 5, SMALL5)
    coeff = combine_mod2_5(c2, c5)

    sum1 = (sum1 + coeff * digits[i]) % 10
    sum2 = (sum2 + coeff * digits[i + 1]) % 10
  end

  sum1 == sum2
end
```

## Scala

```scala
object Solution {
    def hasSameDigits(s: String): Boolean = {
        val n = s.length
        val N = n - 2
        val digits = s.map(c => c - '0')
        val coeff = new Array[Int](N + 1)
        var i = 0
        while (i <= N) {
            coeff(i) = binomMod10(N, i)
            i += 1
        }
        var diff = 0
        // first digit contribution
        diff = (diff + coeff(0) * digits(0)) % 10
        // middle contributions
        var idx = 1
        while (idx < n - 1) {
            val c = (coeff(idx) - coeff(idx - 1)) % 10
            val cc = if (c < 0) c + 10 else c
            diff = (diff + cc * digits(idx)) % 10
            idx += 1
        }
        // last digit subtraction
        diff = (diff - coeff(N) * digits(n - 1)) % 10
        if (diff < 0) diff += 10
        diff == 0
    }

    private def binomMod10(N: Int, K: Int): Int = {
        val a = binomMod2(N, K)
        val b = binomMod5(N, K)
        ((5 * a + 6 * b) % 10)
    }

    // C(N,K) mod 2 is 1 iff (K & (N-K)) == 0
    private def binomMod2(N: Int, K: Int): Int = {
        if ((K & (N - K)) == 0) 1 else 0
    }

    // Precomputed C(n,k) mod 5 for n,k < 5
    private val smallCombMod5: Array[Array[Int]] = Array(
        Array(1, 0, 0, 0, 0),          // n=0
        Array(1, 1, 0, 0, 0),          // n=1
        Array(1, 2, 1, 0, 0),          // n=2
        Array(1, 3, 3, 1, 0),          // n=3
        Array(1, 4, 1, 4, 1)           // n=4 (6 mod5 =1)
    )

    private def combSmallMod5(n: Int, k: Int): Int = {
        if (k < 0 || k > n) 0 else smallCombMod5(n)(k)
    }

    // Lucas theorem for modulus 5
    private def binomMod5(N: Int, K: Int): Int = {
        var n = N
        var k = K
        var res = 1
        while (n > 0 || k > 0) {
            val ni = n % 5
            val ki = k % 5
            if (ki > ni) return 0
            res = (res * combSmallMod5(ni, ki)) % 5
            n /= 5
            k /= 5
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_same_digits(s: String) -> bool {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 2 {
            return bytes[0] == bytes[1];
        }
        let k = n - 2; // binomial exponent

        // factorials modulo 2 and 5
        fn mod_pow(mut a: u32, mut e: u32, m: u32) -> u32 {
            let mut res = 1u32;
            while e > 0 {
                if e & 1 == 1 {
                    res = (res * a) % m;
                }
                a = (a * a) % m;
                e >>= 1;
            }
            res
        }

        fn prepare(p: u32) -> (Vec<u32>, Vec<u32>) {
            let mut fact = vec![0u32; p as usize];
            let mut inv_fact = vec![0u32; p as usize];
            fact[0] = 1;
            for i in 1..p as usize {
                fact[i] = (fact[i - 1] * i as u32) % p;
            }
            // Fermat inverse since p is prime
            for i in 0..p as usize {
                inv_fact[i] = mod_pow(fact[i], p - 2, p);
            }
            (fact, inv_fact)
        }

        let (fact2, inv_fact2) = prepare(2);
        let (fact5, inv_fact5) = prepare(5);

        // nCr modulo a prime using Lucas theorem
        fn ncr_mod_prime_lucas(mut n: usize, mut r: usize, p: u32,
                               fact: &Vec<u32>, inv_fact: &Vec<u32>) -> u32 {
            if r > n { return 0; }
            let mut res = 1u32;
            while n > 0 || r > 0 {
                let ni = (n % p as usize) as u32;
                let ri = (r % p as usize) as u32;
                if ri > ni {
                    return 0;
                }
                let cur = fact[ni as usize];
                let inv_r = inv_fact[ri as usize];
                let inv_nr = inv_fact[(ni - ri) as usize];
                res = (res * cur % p) * (inv_r * inv_nr % p) % p;
                n /= p as usize;
                r /= p as usize;
            }
            res
        }

        // combine modulo 2 and 5 into modulo 10 via CRT (precomputed)
        fn crt(a2: u32, a5: u32) -> u32 {
            for x in 0..10 {
                if x % 2 == a2 as usize && x % 5 == a5 as usize {
                    return x as u32;
                }
            }
            0
        }

        // helper to get C(k, i) mod 10
        let mut ncr_mod10 = |i: usize| -> u32 {
            if i > k { return 0; }
            let c2 = ncr_mod_prime_lucas(k, i, 2, &fact2, &inv_fact2);
            let c5 = ncr_mod_prime_lucas(k, i, 5, &fact5, &inv_fact5);
            crt(c2, c5)
        };

        let mut sum = 0u32;
        for i in 0..n {
            let c1 = if i <= k { ncr_mod10(i) } else { 0 };
            let c2 = if i >= 1 && i - 1 <= k { ncr_mod10(i - 1) } else { 0 };
            let diff = (c1 + 10 - c2) % 10;
            let digit = (bytes[i] - b'0') as u32;
            sum = (sum + diff * digit) % 10;
        }
        sum == 0
    }
}
```

## Racket

```racket
#lang racket

(define/contract (has-same-digits s)
  (-> string? boolean?)
  (let* ((len (string-length s))
         (k (- len 2)))
    ;; precompute small binomial tables modulo a prime p
    (define (precompute-smallC p)
      (let ((tbl (make-vector (+ p) #f)))
        (for ([n (in-range (add1 p))])
          (vector-set! tbl n (make-vector (add1 n) 0))
          (for ([r (in-range (add1 n))])
            (cond [(or (= r 0) (= r n))
                   (vector-set! (vector-ref tbl n) r 1)]
                  [else
                   (let* ((a (vector-ref (vector-ref tbl (- n 1)) r))
                          (b (vector-ref (vector-ref tbl (- n 1)) (- r 1))))
                     (vector-set! (vector-ref tbl n) r (modulo (+ a b) p)))])))
        tbl))
    (define smallC2 (precompute-smallC 2))
    (define smallC5 (precompute-smallC 5))

    ;; C(n,r) modulo prime p using Lucas theorem
    (define (comb-mod-prime n r p tbl)
      (if (or (< r 0) (> r n))
          0
          (let loop ((nn n) (rr r) (res 1))
            (if (= nn 0)
                res
                (let* ((ni (modulo nn p))
                       (ri (modulo rr p)))
                  (if (> ri ni)
                      0
                      (let ((c (vector-ref (vector-ref tbl ni) ri)))
                        (loop (quotient nn p) (quotient rr p) (modulo (* res c) p)))))))))

    ;; Chinese Remainder for mod 2 and mod 5 -> mod 10
    (define (crt a b)
      (for/first ([x (in-range 10)]
                  #:when (and (= (modulo x 2) a)
                              (= (modulo x 5) b)))
        x))

    ;; digits as vector of integers
    (define digits
      (let ((vec (make-vector len)))
        (for ([i (in-range len)])
          (vector-set! vec i (- (char->integer (string-ref s i))
                                (char->integer #\0))))
        vec))

    (let ((sum1 0) (sum2 0))
      (for ([i (in-range (add1 k))])
        (let* ((c2 (comb-mod-prime k i 2 smallC2))
               (c5 (comb-mod-prime k i 5 smallC5))
               (coeff (crt c2 c5)))
          (set! sum1 (modulo (+ sum1 (* coeff (vector-ref digits i))) 10))
          (set! sum2 (modulo (+ sum2 (* coeff (vector-ref digits (+ i 1)))) 10))))
      (= sum1 sum2))))
```

## Erlang

```erlang
-export([has_same_digits/1]).

-spec has_same_digits(S :: unicode:unicode_binary()) -> boolean().
has_same_digits(S) ->
    Digits = [C - $0 || <<C>> <= S],
    N = length(Digits) - 2,
    Diffs = diffs(Digits),
    Sum = process(Diffs, N, 0, 0),
    (Sum rem 10) == 0.

diffs([_]) -> [];
diffs([A, B | Rest]) ->
    [A - B | diffs([B | Rest])].

process([], _N, _Idx, Acc) -> Acc;
process([D | Rest], N, Idx, Acc) ->
    Coeff = binom_mod10(N, Idx),
    Dmod = ((D rem 10) + 10) rem 10,
    NewAcc = (Acc + (Coeff * Dmod) rem 10) rem 10,
    process(Rest, N, Idx + 1, NewAcc).

binom_mod10(N, K) ->
    A = binom_mod2(N, K),
    B = binom_mod5(N, K),
    ((5 * A) + (6 * B)) rem 10.

binom_mod2(N, K) when K < 0; K > N -> 0;
binom_mod2(N, K) ->
    case ((K band (N - K)) =:= 0) of
        true -> 1;
        false -> 0
    end.

binom_mod5(N, K) when K < 0; K > N -> 0;
binom_mod5(N, K) -> binom_mod5_rec(N, K).

binom_mod5_rec(0, 0) -> 1;
binom_mod5_rec(_, _) when _ =:= 0 -> 0;
binom_mod5_rec(N, K) ->
    N0 = N rem 5,
    K0 = K rem 5,
    if
        K0 > N0 -> 0;
        true ->
            Small = small_binom_mod5(N0, K0),
            Rest = binom_mod5_rec(N div 5, K div 5),
            (Small * Rest) rem 5
    end.

small_binom_mod5(0, 0) -> 1;
small_binom_mod5(1, 0) -> 1; small_binom_mod5(1, 1) -> 1;
small_binom_mod5(2, 0) -> 1; small_binom_mod5(2, 1) -> 2; small_binom_mod5(2, 2) -> 1;
small_binom_mod5(3, 0) -> 1; small_binom_mod5(3, 1) -> 3; small_binom_mod5(3, 2) -> 3; small_binom_mod5(3, 3) -> 1;
small_binom_mod5(4, 0) -> 1; small_binom_mod5(4, 1) -> 4; small_binom_mod5(4, 2) -> 1; small_binom_mod5(4, 3) -> 4; small_binom_mod5(4, 4) -> 1;
small_binom_mod5(_, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_same_digits(s :: String.t()) :: boolean()
  def has_same_digits(s) do
    digits = String.graphemes(s) |> Enum.map(&String.to_integer/1)
    n = length(digits)
    n_minus_2 = n - 2

    small2 = %{
      {0, 0} => 1,
      {1, 0} => 1,
      {1, 1} => 1
    }

    small5 =
      for ni <- 0..4, ki <- 0..ni, into: %{} do
        {{ni, ki}, comb_small(ni, ki)}
      end

    {sum2_a, sum5_a, sum2_b, sum5_b} =
      Enum.reduce(0..n_minus_2, {0, 0, 0, 0}, fn i, {s2a, s5a, s2b, s5b} ->
        bin2 = binom_mod(n_minus_2, i, 2, small2)
        bin5 = binom_mod(n_minus_2, i, 5, small5)

        d_a = Enum.at(digits, i)
        d_b = Enum.at(digits, i + 1)

        s2a = rem(s2a + d_a * bin2, 2)
        s5a = rem(s5a + d_a * bin5, 5)
        s2b = rem(s2b + d_b * bin2, 2)
        s5b = rem(s5b + d_b * bin5, 5)

        {s2a, s5a, s2b, s5b}
      end)

    digit_a = rem(5 * sum2_a + 6 * sum5_a, 10)
    digit_b = rem(5 * sum2_b + 6 * sum5_b, 10)

    digit_a == digit_b
  end

  defp comb_small(n, k) when k < 0 or k > n, do: 0
  defp comb_small(_n, 0), do: 1
  defp comb_small(n, n), do: 1
  defp comb_small(n, k) do
    comb_small(n - 1, k - 1) + comb_small(n - 1, k)
  end

  defp binom_mod(_n, _k, _p, _small) when _k < 0, do: 0
  defp binom_mod(n, k, p, small) do
    do_binom_mod(n, k, p, small, 1)
  end

  defp do_binom_mod(0, 0, _p, _small, acc), do: rem(acc, _p)

  defp do_binom_mod(n, k, p, small, acc) do
    if n == 0 and k == 0 do
      rem(acc, p)
    else
      ni = rem(n, p)
      ki = rem(k, p)

      cond do
        ki > ni ->
          0

        true ->
          new_acc = rem(acc * Map.get(small, {ni, ki}), p)
          do_binom_mod(div(n, p), div(k, p), p, small, new_acc)
      end
    end
  end
end
```
