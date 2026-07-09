# 0923. 3Sum With Multiplicity

## Cpp

```cpp
class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        const int MOD = 1'000'000'007;
        long long cnt[101] = {0};
        for (int x : arr) ++cnt[x];
        long long ans = 0;
        for (int i = 0; i <= 100; ++i) {
            if (cnt[i] == 0) continue;
            for (int j = i; j <= 100; ++j) {
                if (cnt[j] == 0) continue;
                int k = target - i - j;
                if (k < j || k > 100) continue;
                if (cnt[k] == 0) continue;
                if (i == j && j == k) {
                    // C(cnt[i], 3)
                    long long c = cnt[i];
                    ans += c * (c - 1) % MOD * (c - 2) % MOD * 166666668 % MOD; // multiply by modular inverse of 6
                } else if (i == j && j != k) {
                    // C(cnt[i], 2) * cnt[k]
                    long long c = cnt[i];
                    ans += c * (c - 1) / 2 % MOD * cnt[k] % MOD;
                } else if (i < j && j == k) {
                    // cnt[i] * C(cnt[j], 2)
                    long long c = cnt[j];
                    ans += cnt[i] % MOD * (c * (c - 1) / 2 % MOD) % MOD;
                } else { // all distinct
                    ans += cnt[i] % MOD * (cnt[j] % MOD) % MOD * (cnt[k] % MOD) % MOD;
                }
                ans %= MOD;
            }
        }
        return (int)(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int threeSumMulti(int[] arr, int target) {
        int[] freq = new int[101];
        for (int num : arr) {
            freq[num]++;
        }
        
        long ans = 0;
        for (int i = 0; i <= 100; i++) {
            if (freq[i] == 0) continue;
            for (int j = i; j <= 100; j++) {
                if (freq[j] == 0) continue;
                int k = target - i - j;
                if (k < j || k > 100) continue;
                if (freq[k] == 0) continue;
                
                long cnt = 0;
                if (i == j && j == k) {
                    if (freq[i] >= 3) {
                        cnt = ((long) freq[i] * (freq[i] - 1) * (freq[i] - 2)) / 6; // C(freq[i],3)
                    }
                } else if (i == j && j != k) {
                    if (freq[i] >= 2) {
                        cnt = ((long) freq[i] * (freq[i] - 1) / 2) * freq[k]; // C(freq[i],2) * freq[k]
                    }
                } else if (i < j && j == k) {
                    if (freq[j] >= 2) {
                        cnt = ((long) freq[j] * (freq[j] - 1) / 2) * freq[i]; // freq[i] * C(freq[j],2)
                    }
                } else { // all distinct
                    cnt = (long) freq[i] * freq[j] * freq[k];
                }
                
                ans = (ans + cnt) % MOD;
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        cnt = [0] * 101
        for v in arr:
            cnt[v] += 1

        ans = 0
        for i in range(101):
            if cnt[i] == 0:
                continue
            for j in range(i, 101):
                if cnt[j] == 0:
                    continue
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                if k < j:   # maintain i <= j <= k
                    continue
                if cnt[k] == 0:
                    continue

                ci, cj, ck = cnt[i], cnt[j], cnt[k]

                if i == j == k:
                    if ci >= 3:
                        ans += ci * (ci - 1) * (ci - 2) // 6
                elif i == j and j != k:
                    if ci >= 2:
                        ans += (ci * (ci - 1) // 2) * ck
                elif i < j and j == k:
                    if cj >= 2:
                        ans += ci * (cj * (cj - 1) // 2)
                else:  # i < j < k
                    ans += ci * cj * ck

                ans %= MOD

        return ans % MOD
```

## Python3

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 101
        for v in arr:
            freq[v] += 1

        ans = 0
        for a in range(101):
            if freq[a] == 0:
                continue
            for b in range(a, 101):
                if freq[b] == 0:
                    continue
                c = target - a - b
                if c < b or c > 100:
                    continue
                if freq[c] == 0:
                    continue

                if a == b == c:
                    cnt = freq[a]
                    ans += cnt * (cnt - 1) * (cnt - 2) // 6
                elif a == b != c:
                    cnt_a = freq[a]
                    cnt_c = freq[c]
                    ans += cnt_a * (cnt_a - 1) // 2 * cnt_c
                elif a < b and b == c:
                    cnt_b = freq[b]
                    cnt_a = freq[a]
                    ans += cnt_a * cnt_b * (cnt_b - 1) // 2
                else:  # all distinct
                    ans += freq[a] * freq[b] * freq[c]

        return ans % MOD
```

## C

```c
int threeSumMulti(int* arr, int arrSize, int target) {
    const int MOD = 1000000007;
    long long freq[101] = {0};
    for (int i = 0; i < arrSize; ++i) {
        freq[arr[i]]++;
    }
    long long ans = 0;
    for (int a = 0; a <= 100; ++a) {
        if (!freq[a]) continue;
        for (int b = a; b <= 100; ++b) {
            if (!freq[b]) continue;
            int c = target - a - b;
            if (c < b || c > 100) continue;
            if (!freq[c]) continue;
            long long ways = 0;
            if (a == b && b == c) {
                if (freq[a] >= 3) {
                    ways = freq[a] * (freq[a] - 1) * (freq[a] - 2) / 6;
                }
            } else if (a == b && b != c) {
                if (freq[a] >= 2) {
                    ways = (freq[a] * (freq[a] - 1) / 2) * freq[c];
                }
            } else if (a < b && b == c) {
                if (freq[b] >= 2) {
                    ways = freq[a] * (freq[b] * (freq[b] - 1) / 2);
                }
            } else { // all distinct
                ways = freq[a] * freq[b] * freq[c];
            }
            ans = (ans + ways) % MOD;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int ThreeSumMulti(int[] arr, int target) {
        const int MOD = 1_000_000_007;
        long ans = 0;
        int[] cnt = new int[101];
        foreach (int v in arr) cnt[v]++;

        for (int i = 0; i <= 100; i++) {
            if (cnt[i] == 0) continue;
            for (int j = i; j <= 100; j++) {
                if (cnt[j] == 0) continue;
                int k = target - i - j;
                if (k < j || k > 100) continue;
                if (cnt[k] == 0) continue;

                long ways;
                if (i == j && j == k) {
                    // C(cnt[i], 3)
                    ways = (long)cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) / 6;
                } else if (i == j && j != k) {
                    // C(cnt[i], 2) * cnt[k]
                    ways = (long)cnt[i] * (cnt[i] - 1) / 2 * cnt[k];
                } else if (i < j && j == k) {
                    // cnt[i] * C(cnt[j], 2)
                    ways = (long)cnt[i] * cnt[j] * (cnt[j] - 1) / 2;
                } else { // i < j < k
                    ways = (long)cnt[i] * cnt[j] * cnt[k];
                }

                ans = (ans + ways) % MOD;
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var threeSumMulti = function(arr, target) {
    const MOD = 1000000007;
    const cnt = new Array(101).fill(0);
    for (const num of arr) cnt[num]++;

    let ans = 0;
    for (let i = 0; i <= 100; i++) {
        if (cnt[i] === 0) continue;
        for (let j = i; j <= 100; j++) {
            if (cnt[j] === 0) continue;
            const k = target - i - j;
            if (k < j || k > 100) continue;
            if (cnt[k] === 0) continue;

            let ways = 0;
            if (i === j && j === k) {
                // C(cnt[i], 3)
                if (cnt[i] >= 3) {
                    ways = cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) / 6;
                }
            } else if (i === j && j !== k) {
                // C(cnt[i], 2) * cnt[k]
                if (cnt[i] >= 2) {
                    ways = cnt[i] * (cnt[i] - 1) / 2 * cnt[k];
                }
            } else if (i < j && j === k) {
                // cnt[i] * C(cnt[j], 2)
                if (cnt[j] >= 2) {
                    ways = cnt[i] * cnt[j] * (cnt[j] - 1) / 2;
                }
            } else { // i < j < k
                ways = cnt[i] * cnt[j] * cnt[k];
            }

            ans = (ans + ways) % MOD;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function threeSumMulti(arr: number[], target: number): number {
    const MOD = 1_000_000_007;
    const cnt = new Array(101).fill(0);
    for (const v of arr) cnt[v]++;

    let ans = 0;

    for (let i = 0; i <= 100; i++) {
        if (cnt[i] === 0) continue;
        for (let j = i; j <= 100; j++) {
            if (cnt[j] === 0) continue;
            const k = target - i - j;
            if (k < j || k > 100) continue;
            if (cnt[k] === 0) continue;

            let add = 0;
            if (i === j && j === k) {
                const c = cnt[i];
                if (c >= 3) {
                    add = Math.floor(c * (c - 1) * (c - 2) / 6) % MOD;
                }
            } else if (i === j && j !== k) {
                const c = cnt[i];
                if (c >= 2) {
                    add = (Math.floor(c * (c - 1) / 2) % MOD) * cnt[k] % MOD;
                }
            } else if (i < j && j === k) {
                const c = cnt[j];
                if (c >= 2) {
                    add = (Math.floor(c * (c - 1) / 2) % MOD) * cnt[i] % MOD;
                }
            } else { // all distinct
                add = ((cnt[i] * cnt[j]) % MOD) * cnt[k] % MOD;
            }

            ans = (ans + add) % MOD;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function threeSumMulti($arr, $target) {
        $mod = 1000000007;
        $freq = array_fill(0, 101, 0);
        foreach ($arr as $v) {
            $freq[$v]++;
        }
        $ans = 0;
        for ($i = 0; $i <= 100; $i++) {
            if ($freq[$i] == 0) continue;
            for ($j = $i; $j <= 100; $j++) {
                if ($freq[$j] == 0) continue;
                $k = $target - $i - $j;
                if ($k < $j || $k > 100) continue;
                if ($freq[$k] == 0) continue;

                $ci = $freq[$i];
                $cj = $freq[$j];
                $ck = $freq[$k];

                if ($i == $j && $j == $k) {
                    if ($ci >= 3) {
                        $add = intdiv($ci * ($ci - 1) * ($ci - 2), 6);
                        $ans = ($ans + $add) % $mod;
                    }
                } elseif ($i == $j && $j != $k) {
                    if ($ci >= 2) {
                        $add = intdiv($ci * ($ci - 1), 2) * $ck;
                        $ans = ($ans + $add) % $mod;
                    }
                } elseif ($i != $j && $j == $k) {
                    if ($cj >= 2) {
                        $add = $ci * intdiv($cj * ($cj - 1), 2);
                        $ans = ($ans + $add) % $mod;
                    }
                } else { // all distinct
                    $add = $ci * $cj * $ck;
                    $ans = ($ans + $add) % $mod;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func threeSumMulti(_ arr: [Int], _ target: Int) -> Int {
        let MOD = 1_000_000_007
        var cnt = Array(repeating: 0, count: 101)
        for v in arr {
            cnt[v] += 1
        }
        var ans: Int64 = 0
        for i in 0...100 {
            if cnt[i] == 0 { continue }
            for j in i...100 {
                if cnt[j] == 0 { continue }
                let k = target - i - j
                if k < j || k > 100 { continue }
                if cnt[k] == 0 { continue }
                
                var ways: Int64 = 0
                if i == j && j == k {
                    let c = cnt[i]
                    if c >= 3 {
                        ways = (Int64(c) * Int64(c - 1) * Int64(c - 2)) / 6
                    }
                } else if i == j && j != k {
                    let ci = cnt[i]
                    let ck = cnt[k]
                    if ci >= 2 {
                        ways = (Int64(ci) * Int64(ci - 1) / 2) * Int64(ck)
                    }
                } else if i < j && j == k {
                    let ci = cnt[i]
                    let cj = cnt[j]
                    if cj >= 2 {
                        ways = Int64(ci) * (Int64(cj) * Int64(cj - 1) / 2)
                    }
                } else { // i < j && j < k
                    ways = Int64(cnt[i]) * Int64(cnt[j]) * Int64(cnt[k])
                }
                
                ans = (ans + ways) % Int64(MOD)
            }
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun threeSumMulti(arr: IntArray, target: Int): Int {
        val MOD = 1_000_000_007L
        val freq = IntArray(101)
        for (v in arr) {
            freq[v]++
        }
        var ans = 0L
        for (i in 0..100) {
            if (freq[i] == 0) continue
            for (j in i..100) {
                if (freq[j] == 0) continue
                val k = target - i - j
                if (k < j || k > 100) continue
                if (freq[k] == 0) continue

                val ci = freq[i].toLong()
                val cj = freq[j].toLong()
                val ck = freq[k].toLong()
                var add = 0L

                when {
                    i == j && j == k -> {
                        if (ci >= 3) {
                            add = ci * (ci - 1) * (ci - 2) / 6
                        }
                    }
                    i == j && j != k -> {
                        if (ci >= 2) {
                            add = ci * (ci - 1) / 2 * ck
                        }
                    }
                    i < j && j == k -> {
                        if (cj >= 2) {
                            add = ci * cj * (cj - 1) / 2
                        }
                    }
                    else -> { // i < j < k
                        add = ci * cj * ck
                    }
                }

                ans = (ans + add) % MOD
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int threeSumMulti(List<int> arr, int target) {
    List<int> cnt = List.filled(101, 0);
    for (var v in arr) {
      cnt[v]++;
    }
    int res = 0;
    for (int i = 0; i <= 100; i++) {
      if (cnt[i] == 0) continue;
      for (int j = i; j <= 100; j++) {
        if (cnt[j] == 0) continue;
        int k = target - i - j;
        if (k < j || k > 100) continue;
        if (cnt[k] == 0) continue;

        int ci = cnt[i], cj = cnt[j], ck = cnt[k];
        int add = 0;
        if (i == j && j == k) {
          if (ci >= 3) {
            add = (ci * (ci - 1) * (ci - 2) ~/ 6) % _MOD;
          }
        } else if (i == j && j != k) {
          if (ci >= 2) {
            int comb = ci * (ci - 1) ~/ 2;
            add = (comb % _MOD) * ck % _MOD;
          }
        } else if (i < j && j == k) {
          if (cj >= 2) {
            int comb = cj * (cj - 1) ~/ 2;
            add = ci * (comb % _MOD) % _MOD;
          }
        } else { // all distinct
          add = ((ci * cj) % _MOD) * ck % _MOD;
        }

        res = (res + add) % _MOD;
      }
    }
    return res;
  }
}
```

## Golang

```go
func threeSumMulti(arr []int, target int) int {
	const MOD int64 = 1000000007
	freq := make([]int64, 101)
	for _, v := range arr {
		freq[v]++
	}
	var ans int64
	for a := 0; a <= 100; a++ {
		if freq[a] == 0 {
			continue
		}
		for b := a; b <= 100; b++ {
			if freq[b] == 0 {
				continue
			}
			c := target - a - b
			if c < b || c > 100 {
				continue
			}
			if freq[c] == 0 {
				continue
			}
			var add int64
			if a == b && b == c {
				if freq[a] >= 3 {
					add = freq[a] * (freq[a] - 1) * (freq[a] - 2) / 6
				}
			} else if a == b && b != c {
				if freq[a] >= 2 {
					add = (freq[a] * (freq[a] - 1) / 2) * freq[c]
				}
			} else if a < b && b == c {
				if freq[b] >= 2 {
					add = freq[a] * (freq[b] * (freq[b] - 1) / 2)
				}
			} else { // a < b < c
				add = freq[a] * freq[b] * freq[c]
			}
			ans = (ans + add) % MOD
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
def three_sum_multi(arr, target)
  mod = 1_000_000_007
  freq = Array.new(101, 0)
  arr.each { |v| freq[v] += 1 }

  ans = 0
  (0..100).each do |i|
    next if freq[i].zero?
    (i..100).each do |j|
      next if freq[j].zero?
      k = target - i - j
      break if k < j
      next if k > 100 || k < j
      next if freq[k].zero?

      cnt =
        if i == j && j == k
          freq[i] * (freq[i] - 1) * (freq[i] - 2) / 6
        elsif i == j && j != k
          freq[i] * (freq[i] - 1) / 2 * freq[k]
        elsif i < j && j == k
          freq[i] * freq[j] * (freq[j] - 1) / 2
        else # i < j < k
          freq[i] * freq[j] * freq[k]
        end

      ans = (ans + cnt) % mod
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def threeSumMulti(arr: Array[Int], target: Int): Int = {
        val MOD = 1000000007L
        val maxVal = 100
        val cnt = new Array[Long](maxVal + 1)
        for (v <- arr) cnt(v) += 1

        var ans = 0L
        for (a <- 0 to maxVal if cnt(a) > 0) {
            for (b <- a to maxVal if cnt(b) > 0) {
                val c = target - a - b
                if (c < b || c > maxVal) {
                    // skip invalid c
                } else if (cnt(c) == 0) {
                    // no such element
                } else {
                    var add = 0L
                    if (a == b && b == c) {
                        if (cnt(a) >= 3)
                            add = cnt(a) * (cnt(a) - 1) * (cnt(a) - 2) / 6
                    } else if (a == b && b != c) {
                        if (cnt(a) >= 2)
                            add = cnt(a) * (cnt(a) - 1) / 2 * cnt(c)
                    } else if (a < b && b == c) {
                        if (cnt(b) >= 2)
                            add = cnt(b) * (cnt(b) - 1) / 2 * cnt(a)
                    } else { // all distinct
                        add = cnt(a) * cnt(b) * cnt(c)
                    }
                    ans = (ans + add) % MOD
                }
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn three_sum_multi(arr: Vec<i32>, target: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i64; 101];
        for &v in &arr {
            cnt[v as usize] += 1;
        }
        let mut ans: i64 = 0;
        for a in 0..=100 {
            if cnt[a] == 0 { continue; }
            for b in a..=100 {
                if cnt[b] == 0 { continue; }
                let sum_ab = a as i32 + b as i32;
                let c_val = target - sum_ab;
                if c_val < 0 || c_val > 100 { continue; }
                let c = c_val as usize;
                if c < b { continue; } // maintain order a <= b <= c
                if cnt[c] == 0 { continue; }

                let ways: i64 = if a == b && b == c {
                    if cnt[a] >= 3 {
                        cnt[a] * (cnt[a] - 1) * (cnt[a] - 2) / 6
                    } else {
                        0
                    }
                } else if a == b && b != c {
                    if cnt[a] >= 2 {
                        cnt[a] * (cnt[a] - 1) / 2 * cnt[c]
                    } else {
                        0
                    }
                } else if a < b && b == c {
                    if cnt[b] >= 2 {
                        cnt[a] * cnt[b] * (cnt[b] - 1) / 2
                    } else {
                        0
                    }
                } else {
                    cnt[a] * cnt[b] * cnt[c]
                };

                ans = (ans + ways) % MOD;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (three-sum-multi arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((freq (make-vector 101 0)))
    ;; count frequencies
    (for ([v arr])
      (vector-set! freq v (+ 1 (vector-ref freq v))))
    (let ((ans 0))
      (for ([a (in-range 0 101)])
        (define fa (vector-ref freq a))
        (when (> fa 0)
          (for ([b (in-range a 101)])
            (define fb (vector-ref freq b))
            (when (> fb 0)
              (define c (- target a b))
              (when (and (>= c b) (<= c 100))
                (define fc (vector-ref freq c))
                (when (> fc 0)
                  (cond
                    [(and (= a b) (= b c)) ; all equal
                     (when (>= fa 3)
                       (define term (quotient (* fa (- fa 1) (- fa 2)) 6))
                       (set! ans (modulo (+ ans term) MOD)))]
                    [(= a b)                ; a == b < c
                     (when (>= fa 2)
                       (define comb (quotient (* fa (- fa 1)) 2))
                       (define term (modulo (* comb fc) MOD))
                       (set! ans (modulo (+ ans term) MOD)))]
                    [(= b c)                ; a < b == c
                     (when (>= fb 2)
                       (define comb (quotient (* fb (- fb 1)) 2))
                       (define term (modulo (* fa comb) MOD))
                       (set! ans (modulo (+ ans term) MOD)))]
                    [else                   ; all distinct
                     (define term (modulo (* fa fb fc) MOD))
                     (set! ans (modulo (+ ans term) MOD))])))))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([three_sum_multi/2]).
-define(MOD, 1000000007).

-spec three_sum_multi(Arr :: [integer()], Target :: integer()) -> integer().
three_sum_multi(Arr, Target) ->
    FreqMap = lists:foldl(fun(X, Acc) ->
        maps:update_with(X, fun(C) -> C + 1 end, 1, Acc)
    end, #{}, Arr),
    loop_a(0, FreqMap, Target, 0).

loop_a(A, _FreqMap, _Target, Acc) when A > 100 ->
    Acc;
loop_a(A, FreqMap, Target, Acc) ->
    FA = maps:get(A, FreqMap, 0),
    Acc1 = if FA == 0 -> Acc; true -> loop_b(A, FA, A, FreqMap, Target, Acc) end,
    loop_a(A + 1, FreqMap, Target, Acc1).

loop_b(_A, _FA, B, _FreqMap, _Target, Acc) when B > 100 ->
    Acc;
loop_b(A, FA, B, FreqMap, Target, Acc) ->
    FB = maps:get(B, FreqMap, 0),
    Acc2 = if FB == 0 -> Acc; true ->
        C = Target - A - B,
        case (C >= B andalso C =< 100) of
            true ->
                FC = maps:get(C, FreqMap, 0),
                if FC == 0 -> Acc;
                   true ->
                       Count = compute(FA, FB, FC, A, B, C),
                       (Acc + Count) rem ?MOD
                end;
            false -> Acc
        end
    end,
    loop_b(A, FA, B + 1, FreqMap, Target, Acc2).

compute(FA, FB, FC, A, B, C) ->
    case {A =:= B, B =:= C} of
        {true, true} -> nCr3(FA);
        {true, false} -> (nCr2(FA) * FC) rem ?MOD;
        {false, true} -> (FA * nCr2(FB)) rem ?MOD;
        {false, false} -> ((FA * FB) rem ?MOD * FC) rem ?MOD
    end.

nCr2(N) when N >= 2 ->
    (N * (N - 1)) div 2;
nCr2(_) -> 0.

nCr3(N) when N >= 3 ->
    (N * (N - 1) * (N - 2)) div 6;
nCr3(_) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec three_sum_multi(arr :: [integer], target :: integer) :: integer
  def three_sum_multi(arr, target) do
    mod = 1_000_000_007

    freq =
      Enum.reduce(arr, :array.new(101, {default, 0}), fn x, a ->
        current = :array.get(x, a)
        :array.set(x, current + 1, a)
      end)

    max_val = 100

    result =
      for a <- 0..max_val,
          b <- a..max_val do
        c = target - a - b

        if c < b or c > max_val do
          0
        else
          ca = :array.get(a, freq)
          cb = :array.get(b, freq)
          cc = :array.get(c, freq)

          cond do
            a == b and b == c ->
              comb3(ca)

            a == b and b != c ->
              comb2(ca) * cc

            a != b and b == c ->
              ca * comb2(cb)

            true ->
              ca * cb * cc
          end
        end
      end
      |> Enum.reduce(0, fn x, acc -> rem(acc + x, mod) end)

    result
  end

  defp comb2(n) when n >= 2, do: div(n * (n - 1), 2)
  defp comb2(_), do: 0

  defp comb3(n) when n >= 3, do: div(n * (n - 1) * (n - 2), 6)
  defp comb3(_), do: 0
end
```
