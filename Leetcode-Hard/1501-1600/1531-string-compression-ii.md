# 1531. String Compression II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int n;
    string s;
    vector<vector<int>> memo;
    
    int digitLen(int cnt) {
        if (cnt == 1) return 0;          // no number appended
        if (cnt < 10) return 1;          // 2..9
        if (cnt < 100) return 2;         // 10..99
        return 3;                        // 100..
    }
    
    int dp(int i, int k) {
        if (i == n) return 0;
        if (k < 0) return INT_MAX/2;
        int &res = memo[i][k];
        if (res != -1) return res;
        const int INF = INT_MAX/2;
        res = INF;
        
        // Option: delete current character
        if (k > 0) {
            res = min(res, dp(i + 1, k - 1));
        }
        
        char c = s[i];
        int cnt = 0;          // number of kept characters equal to c
        for (int j = i; j < n; ++j) {
            if (s[j] == c) ++cnt;
            int deletionsNeeded = (j - i + 1) - cnt;
            if (deletionsNeeded > k) continue;
            int add = 1 + digitLen(cnt);
            res = min(res, add + dp(j + 1, k - deletionsNeeded));
        }
        return res;
    }
    
    int getLengthOfOptimalCompression(string s_, int K) {
        s = std::move(s_);
        n = s.size();
        memo.assign(n + 1, vector<int>(K + 1, -1));
        return dp(0, K);
    }
};
```

## Java

```java
class Solution {
    private String str;
    private int n;
    private int[][] memo;

    public int getLengthOfOptimalCompression(String s, int k) {
        this.str = s;
        this.n = s.length();
        this.memo = new int[n + 1][k + 1];
        for (int i = 0; i <= n; i++) {
            java.util.Arrays.fill(memo[i], -1);
        }
        return dfs(0, k);
    }

    private int dfs(int idx, int k) {
        if (idx == n) return 0;
        if (memo[idx][k] != -1) return memo[idx][k];

        // Option 1: delete current character
        int best = Integer.MAX_VALUE / 2;
        if (k > 0) {
            best = Math.min(best, dfs(idx + 1, k - 1));
        }

        // Option 2: keep a group starting at idx
        int cnt = 0;          // number of kept chars equal to str[idx]
        int del = 0;          // deletions used inside the considered segment
        for (int j = idx; j < n; ++j) {
            if (str.charAt(j) == str.charAt(idx)) {
                cnt++;
            } else {
                del++;
            }
            if (del > k) break;
            int len = getLen(cnt);
            best = Math.min(best, len + dfs(j + 1, k - del));
        }

        memo[idx][k] = best;
        return best;
    }

    private int getLen(int cnt) {
        if (cnt == 1) return 1;          // just the character
        if (cnt < 10) return 2;          // char + one digit
        if (cnt < 100) return 3;         // char + two digits
        return 4;                        // char + three digits (max count is 100)
    }
}
```

## Python

```python
class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def dp(i, rem):
            if i == n:
                return 0
            # Option: delete current character
            best = float('inf')
            if rem > 0:
                best = dp(i + 1, rem - 1)

            cnt = 0          # number of kept chars equal to s[i] in the segment
            del_needed = 0   # deletions required to make the segment uniform

            for j in range(i, n):
                if s[j] == s[i]:
                    cnt += 1
                else:
                    del_needed += 1
                if del_needed > rem:
                    break

                # length contributed by this group
                if cnt == 1:
                    add = 1
                elif cnt < 10:
                    add = 2   # char + one digit
                elif cnt < 100:
                    add = 3   # char + two digits
                else:
                    add = 4   # char + three digits (max length is 100)

                best = min(best, add + dp(j + 1, rem - del_needed))
            return best

        return dp(0, k)
```

## Python3

```python
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import lru_cache

        n = len(s)

        @lru_cache(None)
        def dp(i: int, rem: int) -> int:
            # if we have processed all characters
            if i == n or n - i <= rem:
                return 0

            # option 1: delete current character
            best = float('inf')
            if rem > 0:
                best = dp(i + 1, rem - 1)

            cnt = 0          # number of s[i] kept in the current group
            del_needed = 0   # deletions used to make the group contiguous

            for j in range(i, n):
                if s[j] == s[i]:
                    cnt += 1
                else:
                    del_needed += 1

                if del_needed > rem:
                    break

                # length contributed by this group
                add = 1
                if cnt >= 2:
                    add += len(str(cnt))

                best = min(best, add + dp(j + 1, rem - del_needed))

            return best

        return dp(0, k)
```

## C

```c
#include <string.h>

static int n;
static const char *str;
static int dp[101][101];
static const int INF = 1000000;

static int digitLen(int cnt) {
    if (cnt == 1) return 0;
    if (cnt < 10) return 1;
    if (cnt < 100) return 2;
    return 3; // cnt can be up to 100
}

static int minInt(int a, int b) {
    return a < b ? a : b;
}

static int solveDP(int i, int k) {
    if (i >= n) return 0;
    if (k < 0) return INF;
    if (dp[i][k] != -1) return dp[i][k];

    int ans = INF;

    /* Option: delete current character */
    if (k > 0) {
        ans = solveDP(i + 1, k - 1);
    }

    char c = str[i];
    int cnt = 0;
    for (int j = i; j < n; ++j) {
        if (str[j] == c) ++cnt;
        int del = (j - i + 1) - cnt;
        if (del > k) continue;
        int add = 1 + digitLen(cnt);
        ans = minInt(ans, add + solveDP(j + 1, k - del));
    }

    dp[i][k] = ans;
    return ans;
}

int getLengthOfOptimalCompression(char* s, int k) {
    n = (int)strlen(s);
    str = s;
    for (int i = 0; i <= n; ++i)
        for (int j = 0; j <= k; ++j)
            dp[i][j] = -1;
    return solveDP(0, k);
}
```

## Csharp

```csharp
public class Solution
{
    private string _s;
    private int _n;
    private int[,] _memo;

    public int GetLengthOfOptimalCompression(string s, int k)
    {
        _s = s;
        _n = s.Length;
        _memo = new int[_n + 1, k + 1];
        for (int i = 0; i <= _n; i++)
            for (int j = 0; j <= k; j++)
                _memo[i, j] = -1;

        return Dp(0, k);
    }

    private int Dp(int idx, int k)
    {
        if (k < 0) return int.MaxValue / 2;
        if (idx >= _n) return 0;
        if (_memo[idx, k] != -1) return _memo[idx, k];

        // Option 1: delete current character
        int ans = Dp(idx + 1, k - 1);

        int cnt = 0, del = 0;
        for (int j = idx; j < _n; j++)
        {
            if (_s[j] == _s[idx]) cnt++;
            else del++;

            if (del > k) break;

            int addLen = 1 + Digits(cnt);
            ans = Math.Min(ans, addLen + Dp(j + 1, k - del));
        }

        _memo[idx, k] = ans;
        return ans;
    }

    private int Digits(int count)
    {
        if (count == 1) return 0;
        if (count < 10) return 1;
        if (count < 100) return 2;
        return 3; // count can be up to 100
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLengthOfOptimalCompression = function(s, k) {
    const n = s.length;
    const memo = Array.from({ length: n }, () => Array(k + 1).fill(-1));

    const digitLen = cnt => {
        if (cnt === 1) return 0;
        if (cnt < 10) return 1;
        if (cnt < 100) return 2;
        return 3; // cnt <= 100
    };

    const dfs = (i, rem) => {
        if (i === n) return 0;
        if (memo[i][rem] !== -1) return memo[i][rem];

        let ans = Infinity;

        // Option 1: delete current character
        if (rem > 0) {
            ans = Math.min(ans, dfs(i + 1, rem - 1));
        }

        // Option 2: keep a group starting at i
        let same = 0;   // number of kept chars equal to s[i]
        let del = 0;    // deletions needed inside the considered segment
        for (let j = i; j < n; ++j) {
            if (s[j] === s[i]) {
                same++;
            } else {
                del++;
            }
            if (del > rem) break;
            const cost = 1 + digitLen(same);
            ans = Math.min(ans, cost + dfs(j + 1, rem - del));
        }

        memo[i][rem] = ans;
        return ans;
    };

    return dfs(0, k);
};
```

## Typescript

```typescript
function getLengthOfOptimalCompression(s: string, k: number): number {
    const n = s.length;
    const memo = new Map<string, number>();
    const INF = Number.MAX_SAFE_INTEGER;

    function dp(i: number, remK: number): number {
        if (remK < 0) return INF;
        if (i >= n) return 0;
        const key = i + ',' + remK;
        if (memo.has(key)) return memo.get(key)!;

        // Option 1: delete current character
        let ans = dp(i + 1, remK - 1);

        // Option 2: keep a run starting at i
        let cnt = 0;   // number of kept chars equal to s[i]
        let del = 0;   // deletions needed to make the run contiguous
        for (let j = i; j < n; ++j) {
            if (s[j] === s[i]) cnt++;
            else del++;

            if (del > remK) break;

            // length contributed by this run after compression
            let add = 1; // the character itself
            if (cnt >= 2) {
                if (cnt < 10) add += 1;
                else if (cnt < 100) add += 2;
                else add += 3;
            }

            ans = Math.min(ans, add + dp(j + 1, remK - del));
        }

        memo.set(key, ans);
        return ans;
    }

    return dp(0, k);
}
```

## Php

```php
class Solution {
    private string $s;
    private int $n;
    private array $memo = [];

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function getLengthOfOptimalCompression($s, $k) {
        $this->s = $s;
        $this->n = strlen($s);
        $this->memo = array_fill(0, $this->n + 1, []);
        return $this->dfs(0, $k);
    }

    private function dfs(int $i, int $k): int {
        if ($k < 0) {
            return PHP_INT_MAX >> 1;
        }
        if ($i >= $this->n) {
            return 0;
        }
        if (isset($this->memo[$i][$k])) {
            return $this->memo[$i][$k];
        }

        // Option: delete current character
        $res = PHP_INT_MAX >> 1;
        if ($k > 0) {
            $res = min($res, $this->dfs($i + 1, $k - 1));
        }

        $c = $this->s[$i];
        $cntC = 0;
        for ($j = $i; $j < $this->n; $j++) {
            if ($this->s[$j] === $c) {
                $cntC++;
            }
            $deletions = ($j - $i + 1) - $cntC;
            if ($deletions > $k) {
                break;
            }
            $len = 1 + $this->digitLen($cntC);
            $next = $this->dfs($j + 1, $k - $deletions);
            $res = min($res, $len + $next);
        }

        $this->memo[$i][$k] = $res;
        return $res;
    }

    private function digitLen(int $cnt): int {
        if ($cnt == 1) {
            return 0;
        }
        if ($cnt < 10) {
            return 1;
        }
        if ($cnt < 100) {
            return 2;
        }
        return 3; // cnt can be at most 100 given constraints
    }
}
```

## Swift

```swift
class Solution {
    func getLengthOfOptimalCompression(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var memo = Array(repeating: Array(repeating: -1, count: k + 1), count: n + 1)

        func digitLen(_ cnt: Int) -> Int {
            if cnt == 1 { return 1 }
            else if cnt < 10 { return 2 }
            else if cnt < 100 { return 3 }
            else { return 4 } // safety for larger counts
        }

        func dfs(_ i: Int, _ kLeft: Int) -> Int {
            if i >= n { return 0 }
            if kLeft < 0 { return Int.max / 2 }
            if memo[i][kLeft] != -1 { return memo[i][kLeft] }

            var ans = Int.max / 2

            // Option: delete current character
            if kLeft > 0 {
                ans = min(ans, dfs(i + 1, kLeft - 1))
            }

            var cnt = 0
            var del = 0
            for j in i..<n {
                if chars[j] == chars[i] {
                    cnt += 1
                } else {
                    del += 1
                }
                if del > kLeft { break }
                let cost = digitLen(cnt) + dfs(j + 1, kLeft - del)
                ans = min(ans, cost)
            }

            memo[i][kLeft] = ans
            return ans
        }

        return dfs(0, k)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getLengthOfOptimalCompression(s: String, k: Int): Int {
        val n = s.length
        val memo = Array(n + 1) { IntArray(k + 1) { -1 } }
        val INF = 1_000_000

        fun digitLen(cnt: Int): Int = when {
            cnt == 1 -> 0
            cnt < 10 -> 1
            cnt < 100 -> 2
            else -> 3
        }

        fun dp(i: Int, remK: Int): Int {
            if (i >= n) return 0
            if (memo[i][remK] != -1) return memo[i][remK]

            var ans = INF

            // Option 1: delete s[i]
            if (remK > 0) {
                ans = minOf(ans, dp(i + 1, remK - 1))
            }

            val ch = s[i]
            var cnt = 0
            for (j in i until n) {
                if (s[j] == ch) cnt++
                val deletionsNeeded = (j - i + 1) - cnt
                if (deletionsNeeded > remK) continue
                val addedLen = 1 + digitLen(cnt)
                ans = minOf(ans, addedLen + dp(j + 1, remK - deletionsNeeded))
            }

            memo[i][remK] = ans
            return ans
        }

        return dp(0, k)
    }
}
```

## Dart

```dart
class Solution {
  int getLengthOfOptimalCompression(String s, int k) {
    int n = s.length;
    const int INF = 1 << 30;
    List<List<int>> memo = List.generate(n, (_) => List.filled(k + 1, -1));

    int _len(int cnt) {
      if (cnt == 1) return 1;
      if (cnt < 10) return 2;
      if (cnt < 100) return 3;
      return 4;
    }

    int dfs(int i, int kRem) {
      if (i >= n) return 0;
      if (kRem < 0) return INF;
      if (memo[i][kRem] != -1) return memo[i][kRem];

      int ans = INF;

      // Option 1: delete current character
      if (kRem > 0) {
        int val = dfs(i + 1, kRem - 1);
        if (val < ans) ans = val;
      }

      // Option 2: keep a group of s[i]
      int cnt = 0;
      int del = 0;
      for (int j = i; j < n; ++j) {
        if (s.codeUnitAt(j) == s.codeUnitAt(i)) {
          cnt++;
        } else {
          del++;
        }
        if (del > kRem) break;
        int cost = _len(cnt);
        int val = cost + dfs(j + 1, kRem - del);
        if (val < ans) ans = val;
      }

      memo[i][kRem] = ans;
      return ans;
    }

    return dfs(0, k);
  }
}
```

## Golang

```go
func getLengthOfOptimalCompression(s string, k int) int {
	n := len(s)
	const INF = 1 << 30

	// memo[i][rem] = min length for suffix starting at i with rem deletions left
	memo := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = make([]int, k+1)
		for j := 0; j <= k; j++ {
			memo[i][j] = -1
		}
	}

	var runLen func(cnt int) int
	runLen = func(cnt int) int {
		if cnt == 1 {
			return 1
		}
		if cnt < 10 {
			return 2
		}
		if cnt < 100 {
			return 3
		}
		return 4
	}

	var dp func(i, rem int) int
	dp = func(i, rem int) int {
		if i >= n || n-i <= rem { // delete all remaining characters
			return 0
		}
		if memo[i][rem] != -1 {
			return memo[i][rem]
		}
		res := INF

		// Option: delete current character directly
		if rem > 0 {
			if v := dp(i+1, rem-1); v < res {
				res = v
			}
		}

		cnt, del := 0, 0
		for j := i; j < n; j++ {
			if s[j] == s[i] {
				cnt++
			} else {
				del++
			}
			if del > rem {
				break
			}
			add := runLen(cnt)
			next := dp(j+1, rem-del)
			if add+next < res {
				res = add + next
			}
		}

		memo[i][rem] = res
		return res
	}

	return dp(0, k)
}
```

## Ruby

```ruby
def get_length_of_optimal_compression(s, k)
  n = s.length
  chars = s.bytes
  inf = 1 << 30
  dp = Array.new(n + 1) { Array.new(k + 1, inf) }
  dp[0][0] = 0

  (0...n).each do |i|
    (0..k).each do |del|
      cur = dp[i][del]
      next if cur == inf

      # delete current character
      if del < k
        dp[i + 1][del + 1] = [dp[i + 1][del + 1], cur].min
      end

      c = chars[i]
      cnt = 0
      del_needed = 0
      (i...n).each do |j|
        if chars[j] == c
          cnt += 1
        else
          del_needed += 1
        end
        break if del + del_needed > k

        add_len = 1
        if cnt >= 100
          add_len += 3
        elsif cnt >= 10
          add_len += 2
        elsif cnt >= 2
          add_len += 1
        end

        ndel = del + del_needed
        dp[j + 1][ndel] = [dp[j + 1][ndel], cur + add_len].min
      end
    end
  end

  dp[n].min
end
```

## Scala

```scala
object Solution {
    def getLengthOfOptimalCompression(s: String, k: Int): Int = {
        val n = s.length
        val INF = 1000000
        val memo = Array.ofDim[Int](n + 1, k + 1)
        for (i <- 0 to n; j <- 0 to k) memo(i)(j) = -1

        def digits(cnt: Int): Int = {
            if (cnt == 1) 0
            else if (cnt < 10) 1
            else if (cnt < 100) 2
            else 3
        }

        def dp(i: Int, rem: Int): Int = {
            if (i >= n) return 0
            if (rem < 0) return INF
            if (memo(i)(rem) != -1) return memo(i)(rem)

            var res = INF

            // Delete current character
            if (rem > 0) {
                res = Math.min(res, dp(i + 1, rem - 1))
            }

            var count = 0
            var del = 0
            var j = i
            while (j < n && del <= rem) {
                if (s.charAt(j) == s.charAt(i)) count += 1
                else del += 1

                if (del <= rem) {
                    val add = 1 + digits(count)
                    val next = dp(j + 1, rem - del)
                    res = Math.min(res, add + next)
                }
                j += 1
            }

            memo(i)(rem) = res
            res
        }

        dp(0, k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_length_of_optimal_compression(s: String, k: i32) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();
        let max_k = k as usize;
        let mut memo = vec![vec![-1i32; max_k + 1]; n + 1];

        fn dfs(
            i: usize,
            k: usize,
            n: usize,
            bytes: &[u8],
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            if i >= n {
                return 0;
            }
            if memo[i][k] != -1 {
                return memo[i][k];
            }

            // Option 1: delete current character
            let mut best = if k > 0 {
                dfs(i + 1, k - 1, n, bytes, memo)
            } else {
                i32::MAX / 2
            };

            // Option 2: keep a group starting at i
            let mut cnt = 0usize;
            for j in i..n {
                if bytes[j] == bytes[i] {
                    cnt += 1;
                }
                let deletions_needed = (j - i + 1) - cnt;
                if deletions_needed > k {
                    continue;
                }

                // length contributed by this group
                let add = 1
                    + match cnt {
                        1 => 0,
                        2..=9 => 1,
                        10..=99 => 2,
                        _ => 3, // cnt can be up to 100
                    };

                let next = dfs(j + 1, k - deletions_needed, n, bytes, memo);
                best = best.min(add as i32 + next);
            }

            memo[i][k] = best;
            best
        }

        dfs(0, max_k, n, bytes, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (get-length-of-optimal-compression s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (INF 1000000)
         (dp (make-vector n)))
    ;; initialize memo table
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector (+ k 1) -1)))
    (define (digits cnt)
      (cond [(= cnt 1) 0]
            [else (string-length (number->string cnt))]))
    (define (runlen cnt)
      (+ 1 (digits cnt))) ; character plus possible count digits
    (define (dfs i remk)
      (if (= i n)
          0
          (let* ((memo (vector-ref dp i))
                 (cached (vector-ref memo remk)))
            (if (not (= cached -1))
                cached
                (begin
                  (define best INF)
                  ;; option: delete current character
                  (when (> remk 0)
                    (set! best (min best (dfs (+ i 1) (- remk 1)))))
                  (define c (string-ref s i))
                  (define cnt 0)
                  (for ([j (in-range i n)])
                    (when (char=? (string-ref s j) c)
                      (set! cnt (+ cnt 1)))
                    (define deletions (- (+ (- j i) 1) cnt)) ; segment length - count of c
                    (when (<= deletions remk)
                      (define add (runlen cnt))
                      (set! best (min best (+ add (dfs (+ j 1) (- remk deletions)))))))
                  (vector-set! memo remk best)
                  best))))))
    (dfs 0 k)))
```

## Erlang

```erlang
-module(solution).
-export([get_length_of_optimal_compression/2]).

-define(INF, 1000000).

-spec get_length_of_optimal_compression(S :: unicode:unicode_binary(), K :: integer()) -> integer().
get_length_of_optimal_compression(S, K) ->
    List = unicode:characters_to_list(S),
    erlang:put(slist, List),
    erlang:put(sn, length(List)),
    f(0, K).

f(Pos, K) when K < 0 ->
    ?INF;
f(Pos, K) ->
    N = erlang:get(sn),
    case Pos >= N of
        true -> 0;
        false ->
            case erlang:get({Pos, K}) of
                undefined ->
                    List = erlang:get(slist),
                    Char = lists:nth(Pos + 1, List),
                    DeleteCost = f(Pos + 1, K - 1),
                    Best0 = DeleteCost,
                    Best = explore(Pos, Char, Pos, 0, K, Best0),
                    erlang:put({Pos, K}, Best),
                    Best;
                Val -> Val
            end
    end.

explore(_Pos, _Char, J, _Cnt, _K, Best) when J >= erlang:get(sn) ->
    Best;
explore(Pos, Char, J, Cnt, K, Best) ->
    List = erlang:get(slist),
    CharJ = lists:nth(J + 1, List),
    NewCnt = if CharJ == Char -> Cnt + 1; true -> Cnt end,
    DeletionsNeeded = (J - Pos + 1) - NewCnt,
    case DeletionsNeeded > K of
        true ->
            Best;
        false ->
            RunCost = 1 + digits_len(NewCnt),
            Total = RunCost + f(J + 1, K - DeletionsNeeded),
            NewBest = erlang:min(Best, Total),
            explore(Pos, Char, J + 1, NewCnt, K, NewBest)
    end.

digits_len(Cnt) when Cnt =:= 1 ->
    0;
digits_len(Cnt) when Cnt < 10 ->
    1;
digits_len(Cnt) when Cnt < 100 ->
    2;
digits_len(_Cnt) ->
    3.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_length_of_optimal_compression(s :: String.t(), k :: integer()) :: integer()
  def get_length_of_optimal_compression(s, k) do
    chars = String.to_charlist(s)
    n = length(chars)
    max_val = 1_000_000

    rows =
      :array.new(n + 1, default: nil)
      |> :array.set(n, List.duplicate(0, k + 1))

    rows =
      Enum.reduce((n - 1)..0, rows, fn i, acc_rows ->
        next_row = :array.get(i + 1, acc_rows)

        cur_row =
          for del <- 0..k do
            delete_opt = if del > 0, do: Enum.at(next_row, del - 1), else: max_val
            best = delete_opt

            {_cnt, _del_need, best2} =
              Enum.reduce_while(i..(n - 1), {0, 0, best}, fn j,
                                                            {cnt, del_need, cur_best} ->
                if Enum.at(chars, j) == Enum.at(chars, i) do
                  cnt2 = cnt + 1
                  del_need2 = del_need
                else
                  cnt2 = cnt
                  del_need2 = del_need + 1
                end

                if del_need2 > del do
                  {:halt, {cnt2, del_need2, cur_best}}
                else
                  add_len = 1 + (if cnt2 == 1, do: 0, else: digit_len(cnt2))
                  rest_row = :array.get(j + 1, acc_rows)
                  total = add_len + Enum.at(rest_row, del - del_need2)
                  new_best = if total < cur_best, do: total, else: cur_best
                  {:cont, {cnt2, del_need2, new_best}}
                end
              end)

            best2
          end

        :array.set(i, cur_row, acc_rows)
      end)

    final_row = :array.get(0, rows)
    Enum.at(final_row, k)
  end

  defp digit_len(x) when x < 10, do: 1
  defp digit_len(x) when x < 100, do: 2
  defp digit_len(_), do: 3
end
```
