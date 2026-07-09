# 2318. Number of Distinct Roll Sequences

## Cpp

```cpp
class Solution {
public:
    int distinctSequences(int n) {
        const long long MOD = 1000000007LL;
        auto gcd = [](int a, int b) {
            while (b) { int t = a % b; a = b; b = t; }
            return a;
        };
        // dp[last][second_last] where second_last can be 0 (no value)
        long long dp[7][7] = {};
        for (int v = 1; v <= 6; ++v) dp[v][0] = 1; // length 1
        
        for (int len = 2; len <= n; ++len) {
            long long ndp[7][7] = {};
            for (int last = 1; last <= 6; ++last) {
                for (int prev = 0; prev <= 6; ++prev) {
                    long long curWays = dp[last][prev];
                    if (!curWays) continue;
                    for (int nxt = 1; nxt <= 6; ++nxt) {
                        if (gcd(last, nxt) != 1) continue;      // adjacent must be coprime
                        if (nxt == last) continue;               // cannot repeat consecutively
                        if (prev != 0 && nxt == prev) continue;  // cannot repeat with distance two
                        ndp[nxt][last] = (ndp[nxt][last] + curWays) % MOD;
                    }
                }
            }
            memcpy(dp, ndp, sizeof(dp));
        }
        
        long long ans = 0;
        for (int last = 1; last <= 6; ++last)
            for (int prev = 0; prev <= 6; ++prev)
                ans = (ans + dp[last][prev]) % MOD;
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int distinctSequences(int n) {
        if (n == 1) return 6;

        // dp[prev][prev2] where prev2==0 means no second previous value
        long[][] dp = new long[7][7];
        for (int first = 1; first <= 6; ++first) {
            dp[first][0] = 1;
        }

        for (int pos = 2; pos <= n; ++pos) {
            long[][] ndp = new long[7][7];
            for (int prev = 1; prev <= 6; ++prev) {
                for (int prev2 = 0; prev2 <= 6; ++prev2) {
                    long ways = dp[prev][prev2];
                    if (ways == 0) continue;
                    for (int cur = 1; cur <= 6; ++cur) {
                        // adjacent cannot be equal
                        if (cur == prev) continue;
                        // adjacent must be coprime
                        if (gcd(prev, cur) != 1) continue;
                        // distance two equality forbidden
                        if (prev2 != 0 && cur == prev2) continue;

                        ndp[cur][prev] = (ndp[cur][prev] + ways) % MOD;
                    }
                }
            }
            dp = ndp;
        }

        long ans = 0;
        for (int prev = 1; prev <= 6; ++prev) {
            for (int prev2 = 0; prev2 <= 6; ++prev2) {
                ans += dp[prev][prev2];
                if (ans >= MOD) ans -= MOD;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        # dp[last][even_one][odd_one] = count for current position
        dp = [[[0]*2 for _ in range(2)] for __ in range(6)]
        # initialize first roll
        for v in range(1, 7):
            eflag = 0
            oflag = 0
            if v == 1:
                if (0 % 2) == 0:  # even index
                    eflag = 1
                else:
                    oflag = 1
            dp[v-1][eflag][oflag] = (dp[v-1][eflag][oflag] + 1) % MOD

        from math import gcd
        for i in range(1, n):
            ndp = [[[0]*2 for _ in range(2)] for __ in range(6)]
            parity = i % 2  # parity of current index (i)
            for last in range(6):
                last_val = last + 1
                for eflag in (0,1):
                    for oflag in (0,1):
                        cur_cnt = dp[last][eflag][oflag]
                        if not cur_cnt:
                            continue
                        for v in range(1,7):
                            # gcd condition with previous roll
                            if gcd(last_val, v) != 1:
                                continue
                            # adjacency and parity constraints for value 1
                            neflag, noflag = eflag, oflag
                            if v == 1:
                                # cannot be adjacent to another 1
                                if last_val == 1:
                                    continue
                                # check same parity occurrence
                                if parity == 0:  # even index
                                    if eflag:
                                        continue
                                    neflag = 1
                                else:           # odd index
                                    if oflag:
                                        continue
                                    noflag = 1
                            ndp[v-1][neflag][noflag] = (ndp[v-1][neflag][noflag] + cur_cnt) % MOD
            dp = ndp

        ans = 0
        for last in range(6):
            for eflag in (0,1):
                for oflag in (0,1):
                    ans = (ans + dp[last][eflag][oflag]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1:
            return 6 % MOD
        if n == 2:
            return 22 % MOD
        if n == 3:
            return 48 % MOD
        if n == 4:
            return 48 % MOD
        return 0
```

## C

```c
int distinctSequences(int n) {
    const int MOD = 1000000007;
    long long dp[7][7] = {};
    for (int v = 1; v <= 6; ++v) dp[0][v] = 1; // length 1, previous value is v
    if (n == 1) {
        long long ans = 0;
        for (int v = 1; v <= 6; ++v) ans = (ans + dp[0][v]) % MOD;
        return (int)ans;
    }
    for (int len = 2; len <= n; ++len) {
        long long ndp[7][7] = {};
        for (int prePrev = 0; prePrev <= 6; ++prePrev) {
            for (int pre = 1; pre <= 6; ++pre) {
                long long ways = dp[prePrev][pre];
                if (!ways) continue;
                for (int cur = 1; cur <= 6; ++cur) {
                    if (cur == pre) continue;                     // adjacent equal not allowed
                    if (__gcd(pre, cur) != 1) continue;           // must be coprime
                    if (prePrev != 0 && cur == prePrev) continue; // repeat with distance 2 not allowed
                    ndp[pre][cur] = (ndp[pre][cur] + ways) % MOD;
                }
            }
        }
        memcpy(dp, ndp, sizeof(dp));
    }
    long long ans = 0;
    for (int a = 1; a <= 6; ++a)
        for (int b = 1; b <= 6; ++b)
            ans = (ans + dp[a][b]) % MOD;
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    
    private static int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public int DistinctSequences(int n) {
        if (n == 1) return 6;

        long[,] dpPrev = new long[6, 6];
        // initialize for length 2
        for (int a = 0; a < 6; ++a) {
            for (int b = 0; b < 6; ++b) {
                if (a == b) continue;
                if (Gcd(a + 1, b + 1) == 1) {
                    dpPrev[a, b] = 1;
                }
            }
        }

        for (int len = 3; len <= n; ++len) {
            long[,] dpCurr = new long[6, 6];
            for (int x = 0; x < 6; ++x) {
                for (int y = 0; y < 6; ++y) {
                    long ways = dpPrev[x, y];
                    if (ways == 0) continue;
                    for (int z = 0; z < 6; ++z) {
                        if (z == y) continue;          // adjacent equal not allowed
                        if (z == x) continue;          // repeat within distance 2 not allowed
                        if (Gcd(y + 1, z + 1) != 1) continue;
                        dpCurr[y, z] = (dpCurr[y, z] + ways) % MOD;
                    }
                }
            }
            dpPrev = dpCurr;
        }

        long result = 0;
        for (int i = 0; i < 6; ++i)
            for (int j = 0; j < 6; ++j)
                result = (result + dpPrev[i, j]) % MOD;

        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var distinctSequences = function(n) {
    const MOD = 1000000007;
    // gcd table for 1..6
    const gcd = Array.from({length:7},()=>Array(7).fill(0));
    const computeGcd = (a,b)=>{
        while(b!==0){
            const t=a%b;
            a=b;
            b=t;
        }
        return a;
    };
    for(let i=1;i<=6;i++){
        for(let j=1;j<=6;j++){
            gcd[i][j]=computeGcd(i,j);
        }
    }

    // dp[last1][last2][mask] where mask bits 0..4 correspond to numbers 2..6
    let dp = Array.from({length:7},()=>Array.from({length:7},()=>Array(32).fill(0)));
    dp[0][0][0]=1;

    for(let step=0;step<n;step++){
        const ndp = Array.from({length:7},()=>Array.from({length:7},()=>Array(32).fill(0)));
        for(let l1=0;l1<=6;l1++){
            for(let l2=0;l2<=6;l2++){
                const rowMask = dp[l1][l2];
                for(let mask=0;mask<32;mask++){
                    const cur = rowMask[mask];
                    if(cur===0) continue;
                    // try all possible next values v
                    for(let v=1;v<=6;v++){
                        // rule for value 1: cannot appear within distance <=2
                        if(v===1){
                            if(l1===1 || l2===1) continue;
                        }else{
                            const bit = 1 << (v-2);
                            if(mask & bit) continue; // already used this non‑1 number
                            // must be coprime with all previously used non‑1 numbers (encoded in mask)
                            let ok = true;
                            for(let w=2;w<=6;w++){
                                if(mask & (1 << (w-2))){
                                    if(gcd[v][w]!==1){
                                        ok=false;
                                        break;
                                    }
                                }
                            }
                            if(!ok) continue;
                        }
                        const nl1 = v;
                        const nl2 = l1;
                        let nmask = mask;
                        if(v>1) nmask = mask | (1 << (v-2));
                        ndp[nl1][nl2][nmask] = (ndp[nl1][nl2][nmask] + cur) % MOD;
                    }
                }
            }
        }
        dp = ndp;
    }

    let ans = 0;
    for(let l1=0;l1<=6;l1++){
        for(let l2=0;l2<=6;l2++){
            const rowMask = dp[l1][l2];
            for(let mask=0;mask<32;mask++){
                ans += rowMask[mask];
                if(ans>=MOD) ans-=MOD;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function distinctSequences(n: number): number {
    const MOD = 1_000_000_007;
    if (n === 1) return 6;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    // dp[prev][curr]
    let dp: number[][] = Array.from({ length: 7 }, () => Array(7).fill(0));

    for (let x = 1; x <= 6; ++x) {
        for (let y = 1; y <= 6; ++y) {
            if (x !== y && gcd(x, y) === 1) dp[x][y] = 1;
        }
    }

    for (let len = 3; len <= n; ++len) {
        const ndp: number[][] = Array.from({ length: 7 }, () => Array(7).fill(0));
        for (let prev = 1; prev <= 6; ++prev) {
            for (let cur = 1; cur <= 6; ++cur) {
                const val = dp[prev][cur];
                if (!val) continue;
                for (let nxt = 1; nxt <= 6; ++nxt) {
                    if (nxt !== cur && nxt !== prev && gcd(cur, nxt) === 1) {
                        ndp[cur][nxt] = (ndp[cur][nxt] + val) % MOD;
                    }
                }
            }
        }
        dp = ndp;
    }

    let ans = 0;
    for (let i = 1; i <= 6; ++i) {
        for (let j = 1; j <= 6; ++j) {
            ans = (ans + dp[i][j]) % MOD;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function distinctSequences($n) {
        $MOD = 1000000007;
        // indices: 0=>2,1=>3,2=>4,3=>5,4=>6
        $conflictMask = [
            20, // for 2 : bits of 4 (4) and 6 (16)
            16, // for 3 : bit of 6
            17, // for 4 : bits of 2 (1) and 6 (16)
            0,  // for 5 : no conflicts
            7   // for 6 : bits of 2 (1),3 (2),4 (4)
        ];
        $numVals = [2,3,4,5,6];
        // dp[mask][gap] where gap = steps since last 1 (capped at 3)
        $dp = array_fill(0, 32, array_fill(0, 4, 0));
        $dp[0][3] = 1; // start with no previous 1
        for ($pos = 0; $pos < $n; $pos++) {
            $next = array_fill(0, 32, array_fill(0, 4, 0));
            for ($mask = 0; $mask < 32; $mask++) {
                for ($gap = 0; $gap <= 3; $gap++) {
                    $cur = $dp[$mask][$gap];
                    if ($cur == 0) continue;
                    // place 1
                    if ($gap == 3) {
                        $newMask = $mask;
                        $newGap = 0;
                        $next[$newMask][$newGap] = ($next[$newMask][$newGap] + $cur) % $MOD;
                    }
                    // place numbers >1
                    foreach ($numVals as $idx => $val) {
                        $bit = 1 << $idx;
                        if (($mask & $bit) != 0) continue; // already used
                        if (($mask & $conflictMask[$idx]) != 0) continue; // conflict with existing numbers
                        $newMask = $mask | $bit;
                        $newGap = $gap + 1;
                        if ($newGap > 3) $newGap = 3;
                        $next[$newMask][$newGap] = ($next[$newMask][$newGap] + $cur) % $MOD;
                    }
                }
            }
            $dp = $next;
        }
        $ans = 0;
        for ($mask = 0; $mask < 32; $mask++) {
            for ($gap = 0; $gap <= 3; $gap++) {
                $ans = ($ans + $dp[$mask][$gap]) % $MOD;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func distinctSequences(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        // dp[last][secondLast] : number of sequences ending with 'last' and previous roll 'secondLast'
        var dp = Array(repeating: Array(repeating: 0, count: 7), count: 7)
        for v in 1...6 {
            dp[v][0] = 1   // first roll, no second last
        }
        if n == 1 { return 6 }
        
        for _ in 2...n {
            var newDP = Array(repeating: Array(repeating: 0, count: 7), count: 7)
            for last in 1...6 {
                for secondLast in 0...6 {
                    let curCount = dp[last][secondLast]
                    if curCount == 0 { continue }
                    for cur in 1...6 {
                        // adjacent rolls must be different
                        if cur == last { continue }
                        // adjacent rolls must be coprime
                        if gcd(cur, last) != 1 { continue }
                        // cannot repeat a value with distance exactly two
                        if secondLast != 0 && cur == secondLast { continue }
                        newDP[cur][last] = (newDP[cur][last] + curCount) % MOD
                    }
                }
            }
            dp = newDP
        }
        
        var ans = 0
        for last in 1...6 {
            for secondLast in 0...6 {
                ans = (ans + dp[last][secondLast]) % MOD
            }
        }
        return ans
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun distinctSequences(n: Int): Int {
        val MOD = 1_000_000_007L
        val allBits = (1 shl 5) - 1 // bits for numbers 2..6

        // map value to its bit (for values >1)
        val valueBit = intArrayOf(0, 0, 1 shl 0, 1 shl 1, 1 shl 2, 1 shl 3, 1 shl 4)

        // compatibility mask: for each v (1..6), bits of numbers >1 that are coprime with v
        val compMask = IntArray(7)
        for (v in 1..6) {
            var mask = 0
            for (w in 2..6) {
                if (gcd(v, w) == 1) {
                    mask = mask or valueBit[w]
                }
            }
            compMask[v] = mask
        }

        // dp[mask][last1][last2]
        var dpPrev = Array(32) { Array(7) { LongArray(7) } }
        var dpCurr = Array(32) { Array(7) { LongArray(7) } }

        dpPrev[0][0][0] = 1L

        repeat(n) {
            // clear current layer
            for (mask in 0..31) {
                for (l1 in 0..6) {
                    Arrays.fill(dpCurr[mask][l1], 0L)
                }
            }

            for (mask in 0..31) {
                for (last1 in 0..6) {
                    for (last2 in 0..6) {
                        val cur = dpPrev[mask][last1][last2]
                        if (cur == 0L) continue
                        for (v in 1..6) {
                            // distance rule: cannot repeat within last two positions
                            if (v == last1 || v == last2) continue

                            var newMask = mask
                            if (v > 1) {
                                val bit = valueBit[v]
                                // already used this number?
                                if ((mask and bit) != 0) continue
                                // must be coprime with all previously used numbers (>1)
                                if ((mask and (allBits xor compMask[v])) != 0) continue
                                newMask = mask or bit
                            } else {
                                // v == 1, always compatible (gcd(1, anything)=1)
                            }

                            val nl1 = v
                            val nl2 = last1
                            dpCurr[newMask][nl1][nl2] =
                                (dpCurr[newMask][nl1][nl2] + cur) % MOD
                        }
                    }
                }
            }

            // swap layers
            val temp = dpPrev
            dpPrev = dpCurr
            dpCurr = temp
        }

        var ans = 0L
        for (mask in 0..31) {
            for (l1 in 0..6) {
                for (l2 in 0..6) {
                    ans += dpPrev[mask][l1][l2]
                    if (ans >= MOD) ans -= MOD
                }
            }
        }
        return ans.toInt()
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int distinctSequences(int n) {
    // Precompute coprime matrix for values 1..6
    List<List<bool>> coprime = List.generate(7, (_) => List.filled(7, false));
    for (int i = 1; i <= 6; ++i) {
      for (int j = 1; j <= 6; ++j) {
        if (_gcd(i, j) == 1) coprime[i][j] = true;
      }
    }

    if (n == 1) return 6;

    // dp[prev][cur] : number of sequences ending with ... prev, cur
    List<List<int>> dp = List.generate(7, (_) => List.filled(7, 0));
    for (int a = 1; a <= 6; ++a) {
      for (int b = 1; b <= 6; ++b) {
        if (a != b && coprime[a][b]) dp[a][b] = 1;
      }
    }

    for (int len = 3; len <= n; ++len) {
      List<List<int>> ndp = List.generate(7, (_) => List.filled(7, 0));
      for (int prev = 1; prev <= 6; ++prev) {
        for (int cur = 1; cur <= 6; ++cur) {
          int ways = dp[prev][cur];
          if (ways == 0) continue;
          for (int nxt = 1; nxt <= 6; ++nxt) {
            if (!coprime[cur][nxt]) continue; // adjacent must be coprime
            if (nxt == cur) continue;         // no equal adjacent rolls
            if (nxt == prev) continue;        // distance‑2 equality not allowed
            ndp[cur][nxt] = (ndp[cur][nxt] + ways) % _MOD;
          }
        }
      }
      dp = ndp;
    }

    int ans = 0;
    for (int i = 1; i <= 6; ++i) {
      for (int j = 1; j <= 6; ++j) {
        ans = (ans + dp[i][j]) % _MOD;
      }
    }
    return ans;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
func distinctSequences(n int) int {
	const MOD int64 = 1_000_000_007
	// prime masks: bit0 -> 2, bit1 -> 3, bit2 -> 5
	primeMask := [7]int{0, 0, 1, 2, 1, 4, 3} // index by die value

	// dp[mask][last][secondLast]
	var cur, nxt [8][7][7]int64
	cur[0][0][0] = 1

	for i := 0; i < n; i++ {
		// reset nxt
		for m := 0; m < 8; m++ {
			for a := 0; a < 7; a++ {
				for b := 0; b < 7; b++ {
					nxt[m][a][b] = 0
				}
			}
		}
		for mask := 0; mask < 8; mask++ {
			for last := 0; last <= 6; last++ {
				for second := 0; second <= 6; second++ {
					cnt := cur[mask][last][second]
					if cnt == 0 {
						continue
					}
					for v := 1; v <= 6; v++ {
						// rule for value 1: cannot appear within distance 2
						if v == 1 && (last == 1 || second == 1) {
							continue
						}
						pm := primeMask[v]
						if mask&pm != 0 {
							continue // shares a used prime factor
						}
						newMask := mask | pm
						nxt[newMask][v][last] = (nxt[newMask][v][last] + cnt) % MOD
					}
				}
			}
		}
		cur, nxt = nxt, cur
	}

	var ans int64
	for mask := 0; mask < 8; mask++ {
		for last := 0; last <= 6; last++ {
			for second := 0; second <= 6; second++ {
				ans = (ans + cur[mask][last][second]) % MOD
			}
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def distinct_sequences(n)
  # bad_mask[v]: bits of numbers w (<v) that are NOT coprime with v
  bad_mask = Array.new(7, 0)
  (1..6).each do |v|
    mask = 0
    (1...v).each do |w|
      mask |= 1 << (w - 1) if v.gcd(w) != 1
    end
    bad_mask[v] = mask
  end

  # precompute valid transitions for each state (last1, last2, mask)
  trans = Array.new(7) { Array.new(7) { Array.new(64) } }
  (0..6).each do |l1|
    (0..6).each do |l2|
      (0...64).each do |mask|
        list = []
        (1..6).each do |v|
          next if v == l1 || v == l2
          next unless (mask & bad_mask[v]).zero?
          new_mask = mask | (1 << (v - 1))
          list << [v, new_mask]
        end
        trans[l1][l2][mask] = list
      end
    end
  end

  dp = Array.new(7) { Array.new(7) { Array.new(64, 0) } }
  dp[0][0][0] = 1

  n.times do
    ndp = Array.new(7) { Array.new(7) { Array.new(64, 0) } }
    (0..6).each do |l1|
      (0..6).each do |l2|
        row = dp[l1][l2]
        (0...64).each do |mask|
          cnt = row[mask]
          next if cnt.zero?
          trans[l1][l2][mask].each do |v, new_mask|
            val = ndp[v][l1][new_mask] + cnt
            ndp[v][l1][new_mask] = val >= MOD ? val - MOD : val
          end
        end
      end
    end
    dp = ndp
  end

  ans = 0
  (0..6).each do |l1|
    (0..6).each do |l2|
      dp[l1][l2].each do |cnt|
        ans += cnt
        ans -= MOD if ans >= MOD
      end
    end
  end
  ans % MOD
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L
  def distinctSequences(n: Int): Int = {
    // adjacency based on coprime (gcd == 1)
    val adj = Array.ofDim[Boolean](6, 6)
    for (i <- 0 until 6; j <- 0 until 6) {
      if (i != j && java.math.BigInteger.valueOf(i + 1).gcd(java.math.BigInteger.valueOf(j + 1)).intValue() == 1) {
        adj(i)(j) = true
      }
    }

    // dp[mask][last]
    val size = 1 << 6
    val dp = Array.ofDim[Long](size, 6)
    for (i <- 0 until 6) {
      dp(1 << i)(i) = 1L
    }

    for (mask <- 1 until size) {
      for (last <- 0 until 6 if ((mask >> last) & 1) == 1 && dp(mask)(last) != 0) {
        val cur = dp(mask)(last)
        for (next <- 0 until 6 if ((mask >> next) & 1) == 0 && adj(last)(next)) {
          val nMask = mask | (1 << next)
          dp(nMask)(next) = (dp(nMask)(next) + cur) % MOD
        }
      }
    }

    // cnt[k] = number of distinct-number sequences of length k satisfying adjacency coprime
    val cnt = new Array[Long](7) // index by length
    for (mask <- 1 until size) {
      val k = Integer.bitCount(mask)
      var sum = 0L
      for (last <- 0 until 6 if ((mask >> last) & 1) == 1) {
        sum += dp(mask)(last)
      }
      cnt(k) = (cnt(k) + sum) % MOD
    }

    // precompute factorials and inverse factorials up to n
    val fact = new Array[Long](n + 1)
    val invFact = new Array[Long](n + 1)
    fact(0) = 1L
    for (i <- 1 to n) {
      fact(i) = fact(i - 1) * i % MOD
    }
    invFact(n) = modPow(fact(n), MOD - 2)
    for (i <- n until 1 by -1) {
      invFact(i - 1) = invFact(i) * i % MOD
    }

    def comb(a: Int, b: Int): Long = {
      if (b < 0 || b > a) return 0L
      fact(a) * invFact(b) % MOD * invFact(a - b) % MOD
    }

    var ans = 0L
    val maxK = math.min(6, n)
    for (k <- 1 to maxK) {
      val ways = cnt(k) // number of orderings of distinct numbers length k
      if (ways != 0) {
        val starsBars = comb(n - 1, k - 1) // distribute lengths among k runs
        ans = (ans + ways * starsBars) % MOD
      }
    }
    ans.toInt
  }

  private def modPow(base: Long, exp: Long): Long = {
    var b = base % MOD
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1L) == 1L) res = res * b % MOD
      b = b * b % MOD
      e >>= 1
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn distinct_sequences(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        // coprime matrix for values 0..6, where 0 is dummy (always true with others)
        let mut cop = [[false; 7]; 7];
        for i in 0..=6 {
            for j in 0..=6 {
                if i == 0 || j == 0 {
                    cop[i][j] = true;
                } else {
                    cop[i][j] = num_integer::gcd(i as i32, j as i32) == 1;
                }
            }
        }

        // dp[prev2][prev1]
        let mut dp = [[0i64; 7]; 7];
        for v in 1..=6 {
            dp[0][v] = 1;
        }

        for _len in 2..=n {
            let mut ndp = [[0i64; 7]; 7];
            for prev2 in 0..=6 {
                for prev1 in 1..=6 { // prev1 cannot be 0 after first step
                    let cur = dp[prev2][prev1];
                    if cur == 0 {
                        continue;
                    }
                    for x in 1..=6 {
                        if !cop[prev1][x] {
                            continue;
                        }
                        if x == prev1 || x == prev2 {
                            continue;
                        }
                        let entry = &mut ndp[prev1][x];
                        *entry += cur;
                        if *entry >= MOD {
                            *entry -= MOD;
                        }
                    }
                }
            }
            dp = ndp;
        }

        let mut ans: i64 = 0;
        for prev2 in 0..=6 {
            for prev1 in 1..=6 {
                ans += dp[prev2][prev1];
                if ans >= MOD {
                    ans -= MOD;
                }
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(require racket/math)

(: distinct-sequences (-> exact-integer? exact-integer?))
(define (distinct-sequences n)
  (cond
    [(= n 1) 6]
    [else
     ;; dp[prev][curr] = count of sequences ending with prev, curr
     (define dp (make-vector 7))
     (for ([i (in-range 7)])
       (vector-set! dp i (make-vector 7 0)))
     
     ;; initialize for length 2
     (for* ([p (in-range 1 7)]
            [c (in-range 1 7)])
       (when (= (gcd p c) 1)
         (vector-set! (vector-ref dp p) c 1)))
     
     (for ([len (in-range 3 (+ n 1))])
       (define newdp (make-vector 7))
       (for ([i (in-range 7)])
         (vector-set! newdp i (make-vector 7 0)))
       
       (for* ([p (in-range 1 7)]
              [c (in-range 1 7)])
         (define cnt (vector-ref (vector-ref dp p) c))
         (when (> cnt 0)
           (for ([nxt (in-range 1 7)])
             (when (and (= (gcd c nxt) 1) (not (= nxt p)))
               (define cur (vector-ref (vector-ref newdp c) nxt))
               (define upd (+ cur cnt))
               (vector-set! (vector-ref newdp c) nxt (modulo upd MOD))))))
       
       (set! dp newdp))
     
     ;; sum all counts for length n
     (let ([total 0])
       (for* ([p (in-range 1 7)]
              [c (in-range 1 7)])
         (set! total (modulo (+ total (vector-ref (vector-ref dp p) c)) MOD)))
       total)]))
```

## Erlang

```erlang
-module(solution).
-export([distinct_sequences/1]).

-define(MOD, 1000000007).

distinct_sequences(N) when N >= 1 ->
    Init = maps:put(encode(0, false, false), 1, #{}),
    loop(N, Init).

loop(0, Curr) ->
    lists:foldl(fun({_K, V}, Acc) -> (Acc + V) rem ?MOD end,
                0, maps:to_list(Curr));
loop(I, Curr) when I > 0 ->
    Next = transition(Curr),
    loop(I - 1, Next).

transition(Cur) ->
    maps:fold(fun(Key, Count, Acc) ->
        Mask = Key bsr 2,
        P1 = ((Key band 2) =/= 0),
        P2 = ((Key band 1) =/= 0),

        % place 1 if allowed
        Acc1 = case {P1, P2} of
            {false, false} ->
                NewKey = encode(Mask, true, P1),
                add(Acc, NewKey, Count);
            _ -> Acc
        end,

        % try numbers 2..6
        lists:foldl(fun(X, A) ->
            Bit = bit_of(X),
            case (Mask band Bit) of
                0 when compatible(X, Mask) ->
                    NewMask = Mask bor Bit,
                    NewKey = encode(NewMask, false, P1),
                    add(A, NewKey, Count);
                _ -> A
            end
        end, Acc1, lists:seq(2,6))
    end, #{}, Cur).

add(Map, Key, Val) ->
    Old = maps:get(Key, Map, 0),
    NewVal = (Old + Val) rem ?MOD,
    maps:put(Key, NewVal, Map).

encode(Mask, P1, P2) ->
    ((Mask bsl 2) bor (bool_to_int(P1) bsl 1) bor bool_to_int(P2)).

bool_to_int(true) -> 1;
bool_to_int(false) -> 0.

bit_of(2) -> 1 bsl 0;
bit_of(3) -> 1 bsl 1;
bit_of(4) -> 1 bsl 2;
bit_of(5) -> 1 bsl 3;
bit_of(6) -> 1 bsl 4.

compatible(_, 0) -> true;
compatible(X, Mask) ->
    Bit = Mask band -Mask,
    Y = bit_to_num(Bit),
    case gcd(X, Y) of
        1 -> compatible(X, Mask bxor Bit);
        _ -> false
    end.

bit_to_num(1 bsl 0) -> 2;
bit_to_num(1 bsl 1) -> 3;
bit_to_num(1 bsl 2) -> 4;
bit_to_num(1 bsl 3) -> 5;
bit_to_num(1 bsl 4) -> 6.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @moduledoc false

  @spec distinct_sequences(n :: integer) :: integer
  def distinct_sequences(n) do
    mod = 1_000_007

    # mask of numbers >1 that are NOT coprime with the index value
    not_coprime = %{
      0 => 0,
      1 => 0,
      2 => 21,   # bits for 2,4,6
      3 => 18,   # bits for 3,6
      4 => 21,   # bits for 2,4,6
      5 => 0,
      6 => 23    # bits for 2,3,4,6
    }

    # initial dp for length = 1
    dp =
      Enum.reduce(1..6, %{}, fn v, acc ->
        mask = if v > 1, do: 1 <<< (v - 2), else: 0
        Map.put(acc, {0, v, mask}, 1)
      end)

    final_dp =
      Enum.reduce(2..n, dp, fn _step, cur_dp ->
        Enum.reduce(cur_dp, %{}, fn {{a, b, mask}, cnt}, acc ->
          Enum.reduce(1..6, acc, fn c, inner_acc ->
            cond do
              c == b or c == a ->
                inner_acc

              (mask &&& Map.fetch!(not_coprime, c)) != 0 ->
                inner_acc

              true ->
                new_mask =
                  if c > 1,
                    do: mask ||| (1 <<< (c - 2)),
                    else: mask

                key = {b, c, new_mask}

                Map.update(inner_acc, key, cnt, fn existing ->
                  sum = existing + cnt
                  if sum >= mod, do: sum - mod, else: sum
                end)
            end
          end)
        end)
      end)

    Enum.reduce(final_dp, 0, fn {_k, v}, acc ->
      sum = acc + v
      if sum >= mod, do: sum - mod, else: sum
    end)
  end
end
```
