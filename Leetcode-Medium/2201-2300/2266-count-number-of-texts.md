# 2266. Count Number of Texts

## Cpp

```cpp
class Solution {
public:
    int countTexts(string pressedKeys) {
        const int MOD = 1000000007;
        int n = pressedKeys.size();
        vector<int> dp3(n + 1), dp4(n + 1);
        dp3[0] = dp4[0] = 1;
        for (int i = 1; i <= n; ++i) {
            long long val3 = dp3[i - 1];
            if (i >= 2) val3 += dp3[i - 2];
            if (i >= 3) val3 += dp3[i - 3];
            dp3[i] = val3 % MOD;
            
            long long val4 = dp4[i - 1];
            if (i >= 2) val4 += dp4[i - 2];
            if (i >= 3) val4 += dp4[i - 3];
            if (i >= 4) val4 += dp4[i - 4];
            dp4[i] = val4 % MOD;
        }
        
        long long ans = 1;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && pressedKeys[j] == pressedKeys[i]) ++j;
            int len = j - i;
            char d = pressedKeys[i];
            bool four = (d == '7' || d == '9');
            ans = ans * (four ? dp4[len] : dp3[len]) % MOD;
            i = j;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countTexts(String pressedKeys) {
        final int MOD = 1_000_000_007;
        int n = pressedKeys.length();
        long[] dp3 = new long[n + 1];
        long[] dp4 = new long[n + 1];
        dp3[0] = dp4[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp3[i] = dp3[i - 1];
            if (i >= 2) dp3[i] = (dp3[i] + dp3[i - 2]) % MOD;
            if (i >= 3) dp3[i] = (dp3[i] + dp3[i - 3]) % MOD;

            dp4[i] = dp4[i - 1];
            if (i >= 2) dp4[i] = (dp4[i] + dp4[i - 2]) % MOD;
            if (i >= 3) dp4[i] = (dp4[i] + dp4[i - 3]) % MOD;
            if (i >= 4) dp4[i] = (dp4[i] + dp4[i - 4]) % MOD;
        }

        long ans = 1;
        int i = 0;
        while (i < n) {
            char c = pressedKeys.charAt(i);
            int j = i;
            while (j < n && pressedKeys.charAt(j) == c) j++;
            int len = j - i;
            if (c == '7' || c == '9') {
                ans = ans * dp4[len] % MOD;
            } else {
                ans = ans * dp3[len] % MOD;
            }
            i = j;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(pressedKeys)
        # DP for max group size 3 and 4 up to length n
        dp3 = [0] * (n + 1)
        dp4 = [0] * (n + 1)
        dp3[0] = dp4[0] = 1
        for i in range(1, n + 1):
            v3 = dp3[i - 1]
            if i >= 2:
                v3 += dp3[i - 2]
            if i >= 3:
                v3 += dp3[i - 3]
            dp3[i] = v3 % MOD

            v4 = dp4[i - 1]
            if i >= 2:
                v4 += dp4[i - 2]
            if i >= 3:
                v4 += dp4[i - 3]
            if i >= 4:
                v4 += dp4[i - 4]
            dp4[i] = v4 % MOD

        ans = 1
        i = 0
        while i < n:
            j = i
            while j < n and pressedKeys[j] == pressedKeys[i]:
                j += 1
            length = j - i
            if pressedKeys[i] in ('7', '9'):
                ways = dp4[length]
            else:
                ways = dp3[length]
            ans = (ans * ways) % MOD
            i = j
        return ans
```

## Python3

```python
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        n = len(pressedKeys)
        # precompute ways for limits 3 and 4 up to n
        ways3 = [0] * (n + 1)
        ways4 = [0] * (n + 1)
        ways3[0] = ways4[0] = 1
        for i in range(1, n + 1):
            # limit 3
            total = ways3[i - 1]
            if i >= 2:
                total += ways3[i - 2]
            if i >= 3:
                total += ways3[i - 3]
            ways3[i] = total % MOD
            # limit 4
            total = ways4[i - 1]
            if i >= 2:
                total += ways4[i - 2]
            if i >= 3:
                total += ways4[i - 3]
            if i >= 4:
                total += ways4[i - 4]
            ways4[i] = total % MOD

        ans = 1
        i = 0
        while i < n:
            j = i
            while j < n and pressedKeys[j] == pressedKeys[i]:
                j += 1
            cnt = j - i
            if pressedKeys[i] in ('7', '9'):
                ans = ans * ways4[cnt] % MOD
            else:
                ans = ans * ways3[cnt] % MOD
            i = j
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

int countTexts(char* pressedKeys) {
    const int MOD = 1000000007;
    int n = (int)strlen(pressedKeys);
    long long *dp3 = (long long*)malloc((n + 1) * sizeof(long long));
    long long *dp4 = (long long*)malloc((n + 1) * sizeof(long long));
    dp3[0] = 1;
    dp4[0] = 1;
    for (int i = 1; i <= n; ++i) {
        long long sum3 = 0, sum4 = 0;
        if (i - 1 >= 0) { sum3 += dp3[i - 1]; sum4 += dp4[i - 1]; }
        if (i - 2 >= 0) { sum3 += dp3[i - 2]; sum4 += dp4[i - 2]; }
        if (i - 3 >= 0) { sum3 += dp3[i - 3]; sum4 += dp4[i - 3]; }
        if (i - 4 >= 0) { sum4 += dp4[i - 4]; }
        dp3[i] = sum3 % MOD;
        dp4[i] = sum4 % MOD;
    }

    long long ans = 1;
    int i = 0;
    while (i < n) {
        int j = i;
        while (j < n && pressedKeys[j] == pressedKeys[i]) ++j;
        int len = j - i;
        if (pressedKeys[i] == '7' || pressedKeys[i] == '9')
            ans = ans * dp4[len] % MOD;
        else
            ans = ans * dp3[len] % MOD;
        i = j;
    }

    free(dp3);
    free(dp4);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    public int CountTexts(string pressedKeys) {
        int n = pressedKeys.Length;
        // Precompute DP for max press 3 and 4 up to length n
        long[] dp3 = new long[n + 1];
        long[] dp4 = new long[n + 1];
        dp3[0] = 1;
        dp4[0] = 1;
        for (int i = 1; i <= n; i++) {
            long sum3 = 0, sum4 = 0;
            if (i - 1 >= 0) {
                sum3 += dp3[i - 1];
                sum4 += dp4[i - 1];
            }
            if (i - 2 >= 0) {
                sum3 += dp3[i - 2];
                sum4 += dp4[i - 2];
            }
            if (i - 3 >= 0) {
                sum3 += dp3[i - 3];
                sum4 += dp4[i - 3];
            }
            if (i - 4 >= 0) {
                sum4 += dp4[i - 4];
            }
            dp3[i] = sum3 % MOD;
            dp4[i] = sum4 % MOD;
        }

        long result = 1;
        int idx = 0;
        while (idx < n) {
            char cur = pressedKeys[idx];
            int start = idx;
            while (idx < n && pressedKeys[idx] == cur) idx++;
            int len = idx - start;
            bool fourLetters = cur == '7' || cur == '9';
            long ways = fourLetters ? dp4[len] : dp3[len];
            result = (result * ways) % MOD;
        }

        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} pressedKeys
 * @return {number}
 */
var countTexts = function(pressedKeys) {
    const MOD_BIG = 1000000007n;
    const MOD_NUM = 1000000007;
    const n = pressedKeys.length;

    // Find maximum run length to size DP arrays.
    let maxRun = 0;
    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && pressedKeys[j] === pressedKeys[i]) j++;
        maxRun = Math.max(maxRun, j - i);
        i = j;
    }

    // DP for max press 3 and 4.
    const dp3 = new Array(maxRun + 1).fill(0);
    const dp4 = new Array(maxRun + 1).fill(0);
    dp3[0] = 1;
    dp4[0] = 1;
    for (let i = 1; i <= maxRun; i++) {
        let v3 = dp3[i - 1];
        if (i >= 2) v3 = (v3 + dp3[i - 2]) % MOD_NUM;
        if (i >= 3) v3 = (v3 + dp3[i - 3]) % MOD_NUM;
        dp3[i] = v3;

        let v4 = dp4[i - 1];
        if (i >= 2) v4 = (v4 + dp4[i - 2]) % MOD_NUM;
        if (i >= 3) v4 = (v4 + dp4[i - 3]) % MOD_NUM;
        if (i >= 4) v4 = (v4 + dp4[i - 4]) % MOD_NUM;
        dp4[i] = v4;
    }

    // Multiply ways for each run.
    let ans = 1n;
    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && pressedKeys[j] === pressedKeys[i]) j++;
        const len = j - i;
        const digit = pressedKeys[i];
        const ways = (digit === '7' || digit === '9') ? dp4[len] : dp3[len];
        ans = (ans * BigInt(ways)) % MOD_BIG;
        i = j;
    }

    return Number(ans);
};
```

## Typescript

```typescript
function countTexts(pressedKeys: string): number {
    const MOD = 1000000007n;
    const n = pressedKeys.length;

    const dp3: bigint[] = new Array(n + 1);
    const dp4: bigint[] = new Array(n + 1);
    dp3[0] = 1n;
    dp4[0] = 1n;

    for (let i = 1; i <= n; i++) {
        let sum3 = 0n;
        if (i - 1 >= 0) sum3 += dp3[i - 1];
        if (i - 2 >= 0) sum3 += dp3[i - 2];
        if (i - 3 >= 0) sum3 += dp3[i - 3];
        dp3[i] = sum3 % MOD;

        let sum4 = 0n;
        if (i - 1 >= 0) sum4 += dp4[i - 1];
        if (i - 2 >= 0) sum4 += dp4[i - 2];
        if (i - 3 >= 0) sum4 += dp4[i - 3];
        if (i - 4 >= 0) sum4 += dp4[i - 4];
        dp4[i] = sum4 % MOD;
    }

    let ans = 1n;
    let i = 0;
    while (i < n) {
        const ch = pressedKeys[i];
        let j = i;
        while (j < n && pressedKeys[j] === ch) j++;
        const len = j - i;
        const maxPress = (ch === '7' || ch === '9') ? 4 : 3;
        const ways = maxPress === 3 ? dp3[len] : dp4[len];
        ans = (ans * ways) % MOD;
        i = j;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param String $pressedKeys
     * @return Integer
     */
    function countTexts($pressedKeys) {
        $MOD = 1000000007;
        $n = strlen($pressedKeys);
        // precompute ways for maxPress = 3 and 4 up to n
        $ways3 = array_fill(0, $n + 1, 0);
        $ways4 = array_fill(0, $n + 1, 0);
        $ways3[0] = 1;
        $ways4[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $sum3 = $ways3[$i - 1];
            if ($i >= 2) $sum3 = ($sum3 + $ways3[$i - 2]) % $MOD;
            if ($i >= 3) $sum3 = ($sum3 + $ways3[$i - 3]) % $MOD;
            $ways3[$i] = $sum3;

            $sum4 = $ways4[$i - 1];
            if ($i >= 2) $sum4 = ($sum4 + $ways4[$i - 2]) % $MOD;
            if ($i >= 3) $sum4 = ($sum4 + $ways4[$i - 3]) % $MOD;
            if ($i >= 4) $sum4 = ($sum4 + $ways4[$i - 4]) % $MOD;
            $ways4[$i] = $sum4;
        }

        $ans = 1;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $pressedKeys[$j] === $pressedKeys[$i]) {
                $j++;
            }
            $len = $j - $i;
            $digit = $pressedKeys[$i];
            $maxPress = ($digit === '7' || $digit === '9') ? 4 : 3;
            if ($maxPress == 3) {
                $ans = ($ans * $ways3[$len]) % $MOD;
            } else {
                $ans = ($ans * $ways4[$len]) % $MOD;
            }
            $i = $j;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countTexts(_ pressedKeys: String) -> Int {
        let MOD = 1_000_000_007
        let n = pressedKeys.count
        if n == 0 { return 0 }
        
        var dp3 = [Int](repeating: 0, count: n + 1)
        var dp4 = [Int](repeating: 0, count: n + 1)
        dp3[0] = 1
        dp4[0] = 1
        
        if n >= 1 {
            for i in 1...n {
                var sum3 = 0
                for j in 1...min(3, i) {
                    sum3 += dp3[i - j]
                    if sum3 >= MOD { sum3 -= MOD }
                }
                dp3[i] = sum3 % MOD
                
                var sum4 = 0
                for j in 1...min(4, i) {
                    sum4 += dp4[i - j]
                    if sum4 >= MOD { sum4 -= MOD }
                }
                dp4[i] = sum4 % MOD
            }
        }
        
        let chars = Array(pressedKeys)
        var ans = 1
        var i = 0
        while i < n {
            let ch = chars[i]
            var j = i
            while j < n && chars[j] == ch {
                j += 1
            }
            let len = j - i
            let ways = (ch == "7" || ch == "9") ? dp4[len] : dp3[len]
            ans = Int((Int64(ans) * Int64(ways)) % Int64(MOD))
            i = j
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countTexts(pressedKeys: String): Int {
        val MOD = 1_000_000_007L
        val n = pressedKeys.length
        val dp = LongArray(n + 1)
        dp[0] = 1L
        for (i in 1..n) {
            var ways = 0L
            val curChar = pressedKeys[i - 1]
            val maxPress = if (curChar == '7' || curChar == '9') 4 else 3
            var j = i - 1
            while (j >= 0 && pressedKeys[j] == curChar) {
                val len = i - j
                if (len > maxPress) break
                ways += dp[j]
                if (ways >= MOD) ways -= MOD
                j--
            }
            dp[i] = ways
        }
        return dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countTexts(String pressedKeys) {
    int n = pressedKeys.length;
    // Precompute DP for limits 3 and 4
    List<int> dp3 = List.filled(n + 1, 0);
    List<int> dp4 = List.filled(n + 1, 0);
    dp3[0] = 1;
    dp4[0] = 1;
    for (int i = 1; i <= n; ++i) {
      int sum3 = 0;
      for (int k = 1; k <= 3 && k <= i; ++k) {
        sum3 += dp3[i - k];
        if (sum3 >= _mod) sum3 -= _mod;
      }
      dp3[i] = sum3;

      int sum4 = 0;
      for (int k = 1; k <= 4 && k <= i; ++k) {
        sum4 += dp4[i - k];
        if (sum4 >= _mod) sum4 -= _mod;
      }
      dp4[i] = sum4;
    }

    int ans = 1;
    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && pressedKeys[j] == pressedKeys[i]) {
        ++j;
      }
      int len = j - i;
      bool isFour = pressedKeys[i] == '7' || pressedKeys[i] == '9';
      int ways = isFour ? dp4[len] : dp3[len];
      ans = (ans * ways) % _mod;
      i = j;
    }
    return ans;
  }
}
```

## Golang

```go
func countTexts(pressedKeys string) int {
	const MOD int = 1000000007
	n := len(pressedKeys)

	// dp for digits with max 3 presses (2,3,4,5,6,8)
	dp3 := make([]int, n+1)
	dp3[0] = 1
	for i := 1; i <= n; i++ {
		sum := dp3[i-1]
		if i >= 2 {
			sum += dp3[i-2]
		}
		if i >= 3 {
			sum += dp3[i-3]
		}
		if sum >= MOD {
			sum %= MOD
		}
		dp3[i] = sum % MOD
	}

	// dp for digits with max 4 presses (7,9)
	dp4 := make([]int, n+1)
	dp4[0] = 1
	for i := 1; i <= n; i++ {
		sum := dp4[i-1]
		if i >= 2 {
			sum += dp4[i-2]
		}
		if i >= 3 {
			sum += dp4[i-3]
		}
		if i >= 4 {
			sum += dp4[i-4]
		}
		if sum >= MOD {
			sum %= MOD
		}
		dp4[i] = sum % MOD
	}

	ans := 1
	for i := 0; i < n; {
		j := i
		for j < n && pressedKeys[j] == pressedKeys[i] {
			j++
		}
		length := j - i
		var ways int
		if pressedKeys[i] == '7' || pressedKeys[i] == '9' {
			ways = dp4[length]
		} else {
			ways = dp3[length]
		}
		ans = int(int64(ans) * int64(ways) % MOD)
		i = j
	}
	return ans
}
```

## Ruby

```ruby
def count_texts(pressed_keys)
  mod = 1_000_000_007
  n = pressed_keys.length
  dp3 = Array.new(n + 1, 0)
  dp4 = Array.new(n + 1, 0)
  dp3[0] = dp4[0] = 1

  (1..n).each do |i|
    dp3[i] = dp3[i - 1]
    dp3[i] = (dp3[i] + dp3[i - 2]) if i >= 2
    dp3[i] = (dp3[i] + dp3[i - 3]) if i >= 3
    dp3[i] %= mod

    dp4[i] = dp4[i - 1]
    dp4[i] = (dp4[i] + dp4[i - 2]) if i >= 2
    dp4[i] = (dp4[i] + dp4[i - 3]) if i >= 3
    dp4[i] = (dp4[i] + dp4[i - 4]) if i >= 4
    dp4[i] %= mod
  end

  ans = 1
  i = 0
  while i < n
    j = i
    while j < n && pressed_keys[j] == pressed_keys[i]
      j += 1
    end
    len = j - i
    ways = if pressed_keys[i] == '7' || pressed_keys[i] == '9'
             dp4[len]
           else
             dp3[len]
           end
    ans = (ans * ways) % mod
    i = j
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countTexts(pressedKeys: String): Int = {
        val MOD = 1000000007L
        val n = pressedKeys.length

        // Precompute DP for limits 3 and 4 up to length n
        val dp3 = new Array[Long](n + 1)
        val dp4 = new Array[Long](n + 1)
        dp3(0) = 1L
        dp4(0) = 1L

        for (i <- 1 to n) {
            var sum3 = 0L
            var k = 1
            while (k <= 3 && i - k >= 0) {
                sum3 += dp3(i - k)
                k += 1
            }
            dp3(i) = sum3 % MOD

            var sum4 = 0L
            k = 1
            while (k <= 4 && i - k >= 0) {
                sum4 += dp4(i - k)
                k += 1
            }
            dp4(i) = sum4 % MOD
        }

        var ans = 1L
        var idx = 0
        while (idx < n) {
            val ch = pressedKeys.charAt(idx)
            var j = idx
            while (j < n && pressedKeys.charAt(j) == ch) {
                j += 1
            }
            val len = j - idx
            val limit = if (ch == '7' || ch == '9') 4 else 3
            val ways = if (limit == 3) dp3(len) else dp4(len)
            ans = (ans * ways) % MOD
            idx = j
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_texts(pressed_keys: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = pressed_keys.len();
        let bytes = pressed_keys.as_bytes();

        // dp for limit 3
        let mut dp3 = vec![0i64; n + 1];
        dp3[0] = 1;
        for i in 1..=n {
            let mut sum = dp3[i - 1];
            if i >= 2 {
                sum += dp3[i - 2];
            }
            if i >= 3 {
                sum += dp3[i - 3];
            }
            dp3[i] = sum % MOD;
        }

        // dp for limit 4
        let mut dp4 = vec![0i64; n + 1];
        dp4[0] = 1;
        for i in 1..=n {
            let mut sum = dp4[i - 1];
            if i >= 2 {
                sum += dp4[i - 2];
            }
            if i >= 3 {
                sum += dp4[i - 3];
            }
            if i >= 4 {
                sum += dp4[i - 4];
            }
            dp4[i] = sum % MOD;
        }

        let mut ans: i64 = 1;
        let mut i = 0usize;
        while i < n {
            let mut j = i + 1;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let len = j - i;
            let ways = if bytes[i] == b'7' || bytes[i] == b'9' {
                dp4[len]
            } else {
                dp3[len]
            };
            ans = ans * ways % MOD;
            i = j;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define (count-texts pressedKeys)
  (let* ((n (string-length pressedKeys))
         (dp3 (make-vector (+ n 1) 0))
         (dp4 (make-vector (+ n 1) 0)))
    ;; DP for digits with max 3 presses
    (vector-set! dp3 0 1)
    (for ([i (in-range 1 (+ n 1))])
      (let ((val (modulo (+ (vector-ref dp3 (- i 1))
                           (if (>= i 2) (vector-ref dp3 (- i 2)) 0)
                           (if (>= i 3) (vector-ref dp3 (- i 3)) 0))
                         MOD)))
        (vector-set! dp3 i val)))
    ;; DP for digits with max 4 presses
    (vector-set! dp4 0 1)
    (for ([i (in-range 1 (+ n 1))])
      (let ((val (modulo (+ (vector-ref dp4 (- i 1))
                           (if (>= i 2) (vector-ref dp4 (- i 2)) 0)
                           (if (>= i 3) (vector-ref dp4 (- i 3)) 0)
                           (if (>= i 4) (vector-ref dp4 (- i 4)) 0))
                         MOD)))
        (vector-set! dp4 i val)))
    ;; Process runs of identical digits
    (let loop ((i 0) (ans 1))
      (if (= i n)
          ans
          (let* ((ch (string-ref pressedKeys i))
                 (limit (if (or (char=? ch #\7) (char=? ch #\9)) 4 3)))
            (let inner ((j i))
              (if (and (< j n) (char=? (string-ref pressedKeys j) ch))
                  (inner (+ j 1))
                  (let ((len (- j i))
                        (ways (if (= limit 3)
                                  (vector-ref dp3 len)
                                  (vector-ref dp4 len))))
                    (loop j (modulo (* ans ways) MOD)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_texts/1]).

-define(MOD, 1000000007).

-spec count_texts(PressedKeys :: unicode:unicode_binary()) -> integer().
count_texts(PressedKeys) ->
    List = binary_to_list(PressedKeys),
    case List of
        [] -> 0;
        [First|Rest] ->
            process(Rest, First, 1, 1)
    end.

process([], CurrDigit, Count, Acc) ->
    Ways = ways_len(Count, max_press(CurrDigit)),
    (Acc * Ways) rem ?MOD;
process([H|T], CurrDigit, Count, Acc) when H == CurrDigit ->
    process(T, CurrDigit, Count + 1, Acc);
process([H|T], CurrDigit, Count, Acc) ->
    Ways = ways_len(Count, max_press(CurrDigit)),
    NewAcc = (Acc * Ways) rem ?MOD,
    process(T, H, 1, NewAcc).

max_press(Digit) when Digit == $7; Digit == $9 -> 4;
max_press(_)->3.

ways_len(L, K) ->
    ways_len(1, L, K, [1]).

ways_len(I, L, _K, Prev) when I > L ->
    hd(Prev);
ways_len(I, L, K, Prev) ->
    Sum = lists:foldl(fun(X, Acc) -> (Acc + X) rem ?MOD end, 0, Prev),
    NewPrev = [Sum | Prev],
    Trimmed = if length(NewPrev) > K -> lists:sublist(NewPrev, 1, K); true -> NewPrev end,
    case I of
        L -> Sum;
        _ -> ways_len(I + 1, L, K, Trimmed)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_texts(String.t()) :: integer()
  def count_texts(pressed_keys) do
    n = String.length(pressed_keys)
    dp3 = build_dp(n, 3)
    dp4 = build_dp(n, 4)

    chars = String.to_charlist(pressed_keys)
    process(chars, dp3, dp4, 1)
  end

  defp build_dp(max_len, limit) do
    Enum.reduce(0..max_len, :array.new(max_len + 1, default: 0), fn i, arr ->
      cond do
        i == 0 ->
          :array.set(0, 1, arr)

        true ->
          sum =
            Enum.reduce(1..limit, 0, fn k, s ->
              if k <= i do
                (s + :array.get(i - k, arr)) |> rem(@mod)
              else
                s
              end
            end)

          :array.set(i, sum, arr)
      end
    end)
  end

  defp process([], _dp3, _dp4, acc), do: acc

  defp process([h | t], dp3, dp4, acc) do
    {len, rest} = count_same(t, h, 1)

    limit =
      if h == ?7 or h == ?9 do
        4
      else
        3
      end

    ways =
      case limit do
        3 -> :array.get(len, dp3)
        4 -> :array.get(len, dp4)
      end

    new_acc = (acc * ways) |> rem(@mod)
    process(rest, dp3, dp4, new_acc)
  end

  defp count_same([], _target, acc), do: {acc, []}

  defp count_same([h | t], target, acc) when h == target,
    do: count_same(t, target, acc + 1)

  defp count_same(list, _target, acc), do: {acc, list}
end
```
