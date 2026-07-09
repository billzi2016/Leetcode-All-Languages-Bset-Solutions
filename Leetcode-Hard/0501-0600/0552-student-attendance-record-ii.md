# 0552. Student Attendance Record II

## Cpp

```cpp
class Solution {
public:
    int checkRecord(int n) {
        const int MOD = 1000000007;
        long long cur[2][3] = {{0}};
        long long nxt[2][3];
        cur[0][0] = 1;
        for (int i = 0; i < n; ++i) {
            // reset next
            for (int a = 0; a < 2; ++a)
                for (int l = 0; l < 3; ++l)
                    nxt[a][l] = 0;
            for (int a = 0; a <= 1; ++a) {
                for (int l = 0; l <= 2; ++l) {
                    long long val = cur[a][l];
                    if (!val) continue;
                    // add 'P'
                    nxt[a][0] = (nxt[a][0] + val) % MOD;
                    // add 'A' if no A yet
                    if (a == 0) {
                        nxt[1][0] = (nxt[1][0] + val) % MOD;
                    }
                    // add 'L' if less than two consecutive L's
                    if (l < 2) {
                        nxt[a][l+1] = (nxt[a][l+1] + val) % MOD;
                    }
                }
            }
            // copy nxt to cur
            for (int a = 0; a < 2; ++a)
                for (int l = 0; l < 3; ++l)
                    cur[a][l] = nxt[a][l];
        }
        long long ans = 0;
        for (int a = 0; a <= 1; ++a)
            for (int l = 0; l <= 2; ++l)
                ans = (ans + cur[a][l]) % MOD;
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int checkRecord(int n) {
        long[][] curr = new long[2][3];
        long[][] next = new long[2][3];
        curr[0][0] = 1;
        for (int i = 0; i < n; i++) {
            // reset next
            for (int a = 0; a < 2; a++) {
                for (int l = 0; l < 3; l++) {
                    next[a][l] = 0;
                }
            }
            for (int a = 0; a <= 1; a++) {
                for (int l = 0; l <= 2; l++) {
                    long val = curr[a][l];
                    if (val == 0) continue;
                    // add 'P'
                    next[a][0] = (next[a][0] + val) % MOD;
                    // add 'A' if allowed
                    if (a < 1) {
                        next[a + 1][0] = (next[a + 1][0] + val) % MOD;
                    }
                    // add 'L' if allowed
                    if (l < 2) {
                        next[a][l + 1] = (next[a][l + 1] + val) % MOD;
                    }
                }
            }
            // swap curr and next
            long[][] temp = curr;
            curr = next;
            next = temp;
        }
        long result = 0;
        for (int a = 0; a <= 1; a++) {
            for (int l = 0; l <= 2; l++) {
                result += curr[a][l];
            }
        }
        return (int)(result % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 1000000007
        # dp[a][l] where a = number of A's (0 or 1), l = consecutive L's at the end (0..2)
        dp_curr = [[0] * 3 for _ in range(2)]
        dp_curr[0][0] = 1

        for _ in range(n):
            dp_next = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    val = dp_curr[a][l]
                    if not val:
                        continue
                    # Add 'P'
                    dp_next[a][0] = (dp_next[a][0] + val) % MOD
                    # Add 'A' if we haven't used an A yet
                    if a == 0:
                        dp_next[1][0] = (dp_next[1][0] + val) % MOD
                    # Add 'L' if we have less than two consecutive L's
                    if l < 2:
                        dp_next[a][l + 1] = (dp_next[a][l + 1] + val) % MOD
            dp_curr = dp_next

        result = 0
        for a in range(2):
            for l in range(3):
                result = (result + dp_curr[a][l]) % MOD
        return result
```

## Python3

```python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        for _ in range(n):
            ndp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                row = dp[a]
                for l in range(3):
                    val = row[l]
                    if not val:
                        continue
                    # Add 'P'
                    ndp[a][0] = (ndp[a][0] + val) % MOD
                    # Add 'A' if no previous absence
                    if a == 0:
                        ndp[1][0] = (ndp[1][0] + val) % MOD
                    # Add 'L' if less than two consecutive lates
                    if l < 2:
                        ndp[a][l + 1] = (ndp[a][l + 1] + val) % MOD
            dp = ndp
        return sum(dp[a][l] for a in range(2) for l in range(3)) % MOD
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int checkRecord(int n) {
        const long long MOD = 1000000007LL;
        long long cur[2][3] = {{0}};
        long long nxt[2][3];
        cur[0][0] = 1; // length 0, no A, no trailing L
        
        for (int i = 0; i < n; ++i) {
            memset(nxt, 0, sizeof(nxt));
            for (int a = 0; a <= 1; ++a) {
                for (int l = 0; l <= 2; ++l) {
                    long long val = cur[a][l];
                    if (!val) continue;
                    // Add 'P'
                    nxt[a][0] = (nxt[a][0] + val) % MOD;
                    // Add 'A' if no A used yet
                    if (a == 0) {
                        nxt[1][0] = (nxt[1][0] + val) % MOD;
                    }
                    // Add 'L' if less than two consecutive L's
                    if (l < 2) {
                        nxt[a][l+1] = (nxt[a][l+1] + val) % MOD;
                    }
                }
            }
            memcpy(cur, nxt, sizeof(cur));
        }
        
        long long ans = 0;
        for (int a = 0; a <= 1; ++a)
            for (int l = 0; l <= 2; ++l)
                ans = (ans + cur[a][l]) % MOD;
        return (int)ans;
    }
};
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int CheckRecord(int n)
    {
        long[,] cur = new long[2, 3];
        cur[0, 0] = 1;

        for (int i = 0; i < n; i++)
        {
            long[,] nxt = new long[2, 3];
            for (int a = 0; a <= 1; a++)
            {
                for (int l = 0; l <= 2; l++)
                {
                    long val = cur[a, l];
                    if (val == 0) continue;

                    // Add 'P'
                    nxt[a, 0] = (nxt[a, 0] + val) % MOD;

                    // Add 'A' if no previous absence
                    if (a == 0)
                        nxt[1, 0] = (nxt[1, 0] + val) % MOD;

                    // Add 'L' if less than two consecutive L's
                    if (l < 2)
                        nxt[a, l + 1] = (nxt[a, l + 1] + val) % MOD;
                }
            }
            cur = nxt;
        }

        long result = 0;
        for (int a = 0; a <= 1; a++)
            for (int l = 0; l <= 2; l++)
                result = (result + cur[a, l]) % MOD;

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
var checkRecord = function(n) {
    const MOD = 1000000007;
    let cur = [
        [1, 0, 0], // 0 absences, ending with 0,1,2 L's
        [0, 0, 0]  // 1 absence, ending with 0,1,2 L's
    ];
    
    for (let i = 0; i < n; ++i) {
        const next = [
            [0, 0, 0],
            [0, 0, 0]
        ];
        for (let a = 0; a <= 1; ++a) {
            for (let l = 0; l <= 2; ++l) {
                const val = cur[a][l];
                if (!val) continue;
                
                // Add 'P': reset consecutive L's
                next[a][0] = (next[a][0] + val) % MOD;
                
                // Add 'A' if no previous absence
                if (a === 0) {
                    next[1][0] = (next[1][0] + val) % MOD;
                }
                
                // Add 'L' if less than two consecutive L's so far
                if (l < 2) {
                    next[a][l + 1] = (next[a][l + 1] + val) % MOD;
                }
            }
        }
        cur = next;
    }
    
    let ans = 0;
    for (let a = 0; a <= 1; ++a) {
        for (let l = 0; l <= 2; ++l) {
            ans = (ans + cur[a][l]) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function checkRecord(n: number): number {
    const MOD = 1000000007;
    let cur: number[][] = Array.from({ length: 2 }, () => Array(3).fill(0));
    cur[0][0] = 1;

    for (let i = 0; i < n; i++) {
        const nxt: number[][] = Array.from({ length: 2 }, () => Array(3).fill(0));
        for (let a = 0; a <= 1; a++) {
            for (let l = 0; l <= 2; l++) {
                const val = cur[a][l];
                if (!val) continue;
                // Add 'P'
                nxt[a][0] = (nxt[a][0] + val) % MOD;
                // Add 'A' if we haven't used one yet
                if (a < 1) {
                    nxt[a + 1][0] = (nxt[a + 1][0] + val) % MOD;
                }
                // Add 'L' if consecutive L's are less than 2
                if (l < 2) {
                    nxt[a][l + 1] = (nxt[a][l + 1] + val) % MOD;
                }
            }
        }
        cur = nxt;
    }

    let ans = 0;
    for (let a = 0; a <= 1; a++) {
        for (let l = 0; l <= 2; l++) {
            ans = (ans + cur[a][l]) % MOD;
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
    function checkRecord($n) {
        $MOD = 1000000007;
        // dp[absences][consecutiveLates]
        $dp = [[0, 0, 0], [0, 0, 0]];
        $dp[0][0] = 1;

        for ($i = 0; $i < $n; $i++) {
            $next = [[0, 0, 0], [0, 0, 0]];
            for ($a = 0; $a < 2; $a++) {
                for ($l = 0; $l < 3; $l++) {
                    $val = $dp[$a][$l];
                    if ($val == 0) continue;

                    // Add 'P'
                    $next[$a][0] = ($next[$a][0] + $val) % $MOD;

                    // Add 'A' if we have less than 1 absence so far
                    if ($a + 1 < 2) {
                        $next[$a + 1][0] = ($next[$a + 1][0] + $val) % $MOD;
                    }

                    // Add 'L' if consecutive lates are less than 2
                    if ($l + 1 < 3) {
                        $next[$a][$l + 1] = ($next[$a][$l + 1] + $val) % $MOD;
                    }
                }
            }
            $dp = $next;
        }

        $result = 0;
        for ($a = 0; $a < 2; $a++) {
            for ($l = 0; $l < 3; $l++) {
                $result = ($result + $dp[$a][$l]) % $MOD;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func checkRecord(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var curr = Array(repeating: Array(repeating: 0, count: 3), count: 2)
        curr[0][0] = 1
        
        for _ in 0..<n {
            var next = Array(repeating: Array(repeating: 0, count: 3), count: 2)
            for a in 0...1 {
                for l in 0...2 {
                    let val = curr[a][l]
                    if val == 0 { continue }
                    
                    // Append 'P'
                    var tmp = next[a][0] + val
                    if tmp >= MOD { tmp -= MOD }
                    next[a][0] = tmp
                    
                    // Append 'A' if no previous 'A'
                    if a == 0 {
                        tmp = next[1][0] + val
                        if tmp >= MOD { tmp -= MOD }
                        next[1][0] = tmp
                    }
                    
                    // Append 'L' if less than two consecutive L's
                    if l < 2 {
                        tmp = next[a][l + 1] + val
                        if tmp >= MOD { tmp -= MOD }
                        next[a][l + 1] = tmp
                    }
                }
            }
            curr = next
        }
        
        var result = 0
        for a in 0...1 {
            for l in 0...2 {
                result += curr[a][l]
                if result >= MOD { result -= MOD }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkRecord(n: Int): Int {
        val MOD = 1_000_000_007L
        var curr = Array(2) { LongArray(3) }
        var next = Array(2) { LongArray(3) }
        curr[0][0] = 1L
        for (i in 0 until n) {
            for (a in 0..1) java.util.Arrays.fill(next[a], 0L)
            for (a in 0..1) {
                for (l in 0..2) {
                    val v = curr[a][l]
                    if (v == 0L) continue
                    // Add 'P'
                    next[a][0] = (next[a][0] + v) % MOD
                    // Add 'A' if allowed
                    if (a < 1) {
                        next[a + 1][0] = (next[a + 1][0] + v) % MOD
                    }
                    // Add 'L' if allowed
                    if (l < 2) {
                        next[a][l + 1] = (next[a][l + 1] + v) % MOD
                    }
                }
            }
            val temp = curr
            curr = next
            next = temp
        }
        var ans = 0L
        for (a in 0..1) {
            for (l in 0..2) {
                ans = (ans + curr[a][l]) % MOD
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int checkRecord(int n) {
    List<List<int>> dpCurr = List.generate(2, (_) => List.filled(3, 0));
    dpCurr[0][0] = 1;

    for (int i = 0; i < n; ++i) {
      List<List<int>> next = List.generate(2, (_) => List.filled(3, 0));
      for (int a = 0; a < 2; ++a) {
        for (int l = 0; l < 3; ++l) {
          int val = dpCurr[a][l];
          if (val == 0) continue;
          // Add 'P'
          next[a][0] = (next[a][0] + val) % _mod;
          // Add 'A' if no previous absence
          if (a == 0) {
            next[1][0] = (next[1][0] + val) % _mod;
          }
          // Add 'L' if less than two consecutive L's
          if (l < 2) {
            next[a][l + 1] = (next[a][l + 1] + val) % _mod;
          }
        }
      }
      dpCurr = next;
    }

    int result = 0;
    for (int a = 0; a < 2; ++a) {
      for (int l = 0; l < 3; ++l) {
        result = (result + dpCurr[a][l]) % _mod;
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD int64 = 1000000007

func checkRecord(n int) int {
	var cur [2][3]int64
	cur[0][0] = 1
	for i := 0; i < n; i++ {
		var nxt [2][3]int64
		for a := 0; a < 2; a++ {
			for l := 0; l < 3; l++ {
				v := cur[a][l]
				if v == 0 {
					continue
				}
				// Add 'P'
				nxt[a][0] = (nxt[a][0] + v) % MOD
				// Add 'A' if no previous absence
				if a == 0 {
					nxt[1][0] = (nxt[1][0] + v) % MOD
				}
				// Add 'L' if less than two consecutive lates
				if l < 2 {
					nxt[a][l+1] = (nxt[a][l+1] + v) % MOD
				}
			}
		}
		cur = nxt
	}
	var ans int64
	for a := 0; a < 2; a++ {
		for l := 0; l < 3; l++ {
			ans = (ans + cur[a][l]) % MOD
		}
	}
	return int(ans)
}

// The following main function is only for local testing and will be ignored by LeetCode.
func main() {
	fmt.Println(checkRecord(2))    // Expected: 8
	fmt.Println(checkRecord(1))    // Expected: 3
	fmt.Println(checkRecord(10101)) // Expected: 183236316
}
```

## Ruby

```ruby
def check_record(n)
  mod = 1_000_000_007
  dp = Array.new(2) { Array.new(3, 0) }
  dp[0][0] = 1

  n.times do
    next_dp = Array.new(2) { Array.new(3, 0) }
    (0..1).each do |a|
      (0..2).each do |l|
        val = dp[a][l]
        next if val == 0
        # Add 'P'
        next_dp[a][0] = (next_dp[a][0] + val) % mod
        # Add 'A' if we haven't used an absence yet
        if a < 1
          next_dp[a + 1][0] = (next_dp[a + 1][0] + val) % mod
        end
        # Add 'L' if we have less than two consecutive lates
        if l < 2
          next_dp[a][l + 1] = (next_dp[a][l + 1] + val) % mod
        end
      end
    end
    dp = next_dp
  end

  ans = 0
  (0..1).each do |a|
    (0..2).each do |l|
      ans = (ans + dp[a][l]) % mod
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def checkRecord(n: Int): Int = {
        val MOD = 1000000007L
        var cur = Array.ofDim[Long](2, 3)
        cur(0)(0) = 1L

        for (_ <- 0 until n) {
            val next = Array.ofDim[Long](2, 3)
            var a = 0
            while (a < 2) {
                var l = 0
                while (l < 3) {
                    val v = cur(a)(l)
                    if (v != 0L) {
                        // Add 'P'
                        next(a)(0) = (next(a)(0) + v) % MOD
                        // Add 'A' if no previous absence
                        if (a == 0) {
                            next(1)(0) = (next(1)(0) + v) % MOD
                        }
                        // Add 'L' if less than two consecutive L's
                        if (l < 2) {
                            next(a)(l + 1) = (next(a)(l + 1) + v) % MOD
                        }
                    }
                    l += 1
                }
                a += 1
            }
            cur = next
        }

        var ans = 0L
        var a = 0
        while (a < 2) {
            var l = 0
            while (l < 3) {
                ans = (ans + cur(a)(l)) % MOD
                l += 1
            }
            a += 1
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_record(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cur = [[0i64; 3]; 2];
        cur[0][0] = 1;
        for _ in 0..n as usize {
            let mut nxt = [[0i64; 3]; 2];
            for a in 0..2 {
                for l in 0..3 {
                    let val = cur[a][l];
                    if val == 0 {
                        continue;
                    }
                    // Add 'P'
                    nxt[a][0] = (nxt[a][0] + val) % MOD;
                    // Add 'A' if we haven't used an absence yet
                    if a < 1 {
                        nxt[a + 1][0] = (nxt[a + 1][0] + val) % MOD;
                    }
                    // Add 'L' if we have less than two consecutive lates
                    if l < 2 {
                        nxt[a][l + 1] = (nxt[a][l + 1] + val) % MOD;
                    }
                }
            }
            cur = nxt;
        }
        let mut ans: i64 = 0;
        for a in 0..2 {
            for l in 0..3 {
                ans = (ans + cur[a][l]) % MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (check-record n)
  (-> exact-integer? exact-integer?)
  (let* ((size 6)
         (dp (make-vector size 0))
         (ndp (make-vector size 0)))
    (vector-set! dp 0 1) ; a=0, l=0
    (for ([i (in-range n)])
      ;; clear ndp
      (for ([j (in-range size)]) (vector-set! ndp j 0))
      ;; transition
      (for ([idx (in-range size)])
        (let ((cur (vector-ref dp idx)))
          (when (> cur 0)
            (define a (quotient idx 3))
            (define l (remainder idx 3))
            ;; add 'P'
            (let ((dest (+ (* a 3) 0)))
              (vector-set! ndp dest
                           (mod (+ (vector-ref ndp dest) cur) MOD)))
            ;; add 'A' if no previous absence
            (when (= a 0)
              (let ((dest (+ (* 1 3) 0))) ; a becomes 1
                (vector-set! ndp dest
                             (mod (+ (vector-ref ndp dest) cur) MOD))))
            ;; add 'L' if less than two consecutive lates
            (when (< l 2)
              (let ((dest (+ (* a 3) (+ l 1))))
                (vector-set! ndp dest
                             (mod (+ (vector-ref ndp dest) cur) MOD)))))))
      ;; swap dp and ndp for next iteration
      (let ((tmp dp))
        (set! dp ndp)
        (set! ndp tmp)))
    ;; sum all valid states
    (let ((ans 0))
      (for ([idx (in-range size)])
        (set! ans (mod (+ ans (vector-ref dp idx)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([check_record/1]).

-define(MOD, 1000000007).

check_record(N) ->
    Initial = [[1,0,0],[0,0,0]],
    Final = iter(N, Initial),
    [[A0L0, A0L1, A0L2], [A1L0, A1L1, A1L2]] = Final,
    ((A0L0 + A0L1 + A0L2 + A1L0 + A1L1 + A1L2) rem ?MOD).

iter(0, Curr) -> Curr;
iter(N, Curr) when N > 0 ->
    Next = step(Curr),
    iter(N-1, Next).

step([[A0L0, A0L1, A0L2], [A1L0, A1L1, A1L2]]) ->
    SumA0 = (A0L0 + A0L1 + A0L2) rem ?MOD,
    SumA1 = (A1L0 + A1L1 + A1L2) rem ?MOD,
    NewA0L0 = SumA0,
    NewA0L1 = A0L0,
    NewA0L2 = A0L1,
    NewA1L0 = (SumA1 + SumA0) rem ?MOD,
    NewA1L1 = A1L0,
    NewA1L2 = A1L1,
    [[NewA0L0, NewA0L1, NewA0L2], [NewA1L0, NewA1L1, NewA1L2]].
```

## Elixir

```elixir
defmodule Solution do
  @spec check_record(n :: integer) :: integer
  def check_record(n) do
    mod = 1_000_000_007

    dp0 = %{
      {0, 0} => 1,
      {0, 1} => 0,
      {0, 2} => 0,
      {1, 0} => 0,
      {1, 1} => 0,
      {1, 2} => 0
    }

    dp =
      Enum.reduce(1..n, dp0, fn _, dp_acc ->
        Enum.reduce(dp_acc, %{}, fn {{a, l}, val}, acc ->
          if val == 0 do
            acc
          else
            # Append 'P'
            acc = Map.update(acc, {a, 0}, val, fn existing -> rem(existing + val, mod) end)

            # Append 'A' if no previous absence
            acc =
              if a == 0 do
                Map.update(acc, {1, 0}, val, fn existing -> rem(existing + val, mod) end)
              else
                acc
              end

            # Append 'L' if less than two consecutive lates
            acc =
              if l < 2 do
                Map.update(acc, {a, l + 1}, val, fn existing -> rem(existing + val, mod) end)
              else
                acc
              end

            acc
          end
        end)
      end)

    Enum.reduce(dp, 0, fn {_k, v}, sum -> rem(sum + v, mod) end)
  end
end
```
