# 1711. Count Good Meals

## Cpp

```cpp
class Solution {
public:
    int countPairs(vector<int>& deliciousness) {
        const int MOD = 1000000007;
        if (deliciousness.empty()) return 0;
        int maxVal = *max_element(deliciousness.begin(), deliciousness.end());
        int maxSum = maxVal * 2;
        vector<int> powers;
        for (int p = 1; p <= maxSum; p <<= 1) {
            powers.push_back(p);
        }
        unordered_map<int, long long> freq;
        freq.reserve(deliciousness.size() * 2);
        long long ans = 0;
        for (int x : deliciousness) {
            for (int p : powers) {
                int need = p - x;
                auto it = freq.find(need);
                if (it != freq.end()) {
                    ans += it->second;
                    if (ans >= MOD) ans %= MOD;
                }
            }
            ++freq[x];
        }
        return static_cast<int>(ans % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countPairs(int[] deliciousness) {
        // Precompute powers of two up to 2^21
        int[] powers = new int[22];
        for (int i = 0; i <= 21; i++) {
            powers[i] = 1 << i;
        }
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        long ans = 0L;
        for (int val : deliciousness) {
            for (int p : powers) {
                int need = p - val;
                Integer cnt = freq.get(need);
                if (cnt != null) {
                    ans += cnt;
                    if (ans >= MOD) ans -= MOD; // keep within range
                }
            }
            freq.put(val, freq.getOrDefault(val, 0) + 1);
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        cnt = {}
        powers = [1 << i for i in range(22)]  # up to 2^21 inclusive
        ans = 0
        for v in deliciousness:
            for p in powers:
                need = p - v
                if need in cnt:
                    ans += cnt[need]
            ans %= MOD
            cnt[v] = cnt.get(v, 0) + 1
        return ans % MOD
```

## Python3

```python
class Solution:
    def countPairs(self, deliciousness):
        from collections import defaultdict
        MOD = 10**9 + 7
        cnt = defaultdict(int)
        powers = [1 << i for i in range(22)]  # up to 2^21 > max possible sum (2*2^20)
        ans = 0
        for x in deliciousness:
            for p in powers:
                need = p - x
                if need in cnt:
                    ans += cnt[need]
            cnt[x] += 1
        return ans % MOD
```

## C

```c
#include <stdlib.h>

int countPairs(int* deliciousness, int deliciousnessSize) {
    const int MOD = 1000000007;
    const int MAX_VAL = 1 << 20; // 1048576
    int *freq = (int *)calloc(MAX_VAL + 1, sizeof(int));
    long long ans = 0;

    for (int i = 0; i < deliciousnessSize; ++i) {
        int x = deliciousness[i];
        for (int k = 0; k <= 21; ++k) { // powers of two up to 2^21
            long long target = 1LL << k;
            long long y = target - x;
            if (y < 0 || y > MAX_VAL) continue;
            ans += freq[(int)y];
            if (ans >= MOD) ans %= MOD;
        }
        ++freq[x];
    }

    free(freq);
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int CountPairs(int[] deliciousness) {
        const int MOD = 1000000007;
        var freq = new Dictionary<int, long>();
        long ans = 0;
        
        // Precompute powers of two up to 2^21 (since max sum <= 2 * 2^20)
        int[] powers = new int[22];
        for (int i = 0; i <= 21; i++) {
            powers[i] = 1 << i;
        }
        
        foreach (int val in deliciousness) {
            foreach (int p in powers) {
                int need = p - val;
                if (freq.TryGetValue(need, out long cnt)) {
                    ans += cnt;
                    if (ans >= MOD) ans %= MOD;
                }
            }
            
            if (freq.ContainsKey(val))
                freq[val] += 1;
            else
                freq[val] = 1;
        }
        
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} deliciousness
 * @return {number}
 */
var countPairs = function(deliciousness) {
    const MOD = 1000000007;
    // precompute powers of two up to 2^21 (since max sum <= 2*2^20)
    const powers = [];
    for (let i = 0; i <= 21; i++) {
        powers.push(1 << i);
    }
    
    const freq = new Map();
    let ans = 0;
    
    for (const val of deliciousness) {
        for (const p of powers) {
            const need = p - val;
            if (freq.has(need)) {
                ans += freq.get(need);
                if (ans >= MOD) ans -= MOD;
            }
        }
        freq.set(val, (freq.get(val) || 0) + 1);
    }
    
    return ans % MOD;
};
```

## Typescript

```typescript
function countPairs(deliciousness: number[]): number {
    const MOD = 1_000_000_007;
    let maxVal = 0;
    for (const v of deliciousness) if (v > maxVal) maxVal = v;
    const maxSum = maxVal * 2;
    const powers: number[] = [];
    let p = 1;
    while (p <= maxSum) {
        powers.push(p);
        p <<= 1;
    }
    const cnt = new Map<number, number>();
    let ans = 0;
    for (const x of deliciousness) {
        for (const target of powers) {
            const need = target - x;
            if (need < 0) continue;
            const c = cnt.get(need);
            if (c !== undefined) {
                ans += c;
                if (ans >= MOD) ans -= MOD;
            }
        }
        cnt.set(x, (cnt.get(x) ?? 0) + 1);
    }
    return ans % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $deliciousness
     * @return Integer
     */
    function countPairs($deliciousness) {
        $mod = 1000000007;
        $powers = [];
        for ($i = 0; $i <= 21; $i++) {
            $powers[] = 1 << $i;
        }
        $cnt = [];
        $ans = 0;
        foreach ($deliciousness as $x) {
            foreach ($powers as $p) {
                $need = $p - $x;
                if (isset($cnt[$need])) {
                    $ans += $cnt[$need];
                    if ($ans >= $mod) {
                        $ans -= $mod;
                    }
                }
            }
            if (!isset($cnt[$x])) {
                $cnt[$x] = 0;
            }
            $cnt[$x]++;
        }
        return $ans % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ deliciousness: [Int]) -> Int {
        let MOD = 1_000_000_007
        var powers = [Int]()
        for i in 0...21 {
            powers.append(1 << i)
        }
        var freq = [Int: Int]()
        var ans = 0
        for val in deliciousness {
            for p in powers {
                let need = p - val
                if let cnt = freq[need] {
                    ans = (ans + cnt) % MOD
                }
            }
            freq[val, default: 0] += 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(deliciousness: IntArray): Int {
        val MOD = 1_000_000_007L
        val cnt = HashMap<Int, Int>()
        var ans = 0L

        // Powers of two up to 2^22 (covers maximum possible sum)
        val powers = mutableListOf<Int>()
        var p = 1
        while (p <= (1 shl 22)) {
            powers.add(p)
            p = p shl 1
        }

        for (v in deliciousness) {
            for (pow in powers) {
                val need = pow - v
                cnt[need]?.let { ans += it.toLong() }
            }
            cnt[v] = cnt.getOrDefault(v, 0) + 1
        }

        return (ans % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countPairs(List<int> deliciousness) {
    final Map<int, int> freq = {};
    final List<int> powers = List.generate(22, (i) => 1 << i);
    int ans = 0;
    for (final val in deliciousness) {
      for (final p in powers) {
        final need = p - val;
        if (freq.containsKey(need)) {
          ans = (ans + freq[need]!) % _mod;
        }
      }
      freq[val] = (freq[val] ?? 0) + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func countPairs(deliciousness []int) int {
	const MOD = 1_000_000_007
	maxVal := 0
	for _, v := range deliciousness {
		if v > maxVal {
			maxVal = v
		}
	}
	limit := maxVal * 2
	powers := make([]int, 0)
	for p := 1; p <= limit; p <<= 1 {
		powers = append(powers, p)
	}
	cnt := make(map[int]int64)
	var ans int64
	for _, x := range deliciousness {
		for _, target := range powers {
			need := target - x
			if c, ok := cnt[need]; ok {
				ans += c
				if ans >= MOD {
					ans %= MOD
				}
			}
		}
		cnt[x]++
	}
	return int(ans % MOD)
}
```

## Ruby

```ruby
def count_pairs(deliciousness)
  mod = 1_000_000_007
  max_val = deliciousness.max || 0
  max_sum = max_val * 2
  powers = []
  p = 1
  while p <= max_sum
    powers << p
    p <<= 1
  end

  freq = Hash.new(0)
  ans = 0

  deliciousness.each do |x|
    powers.each do |pwr|
      y = pwr - x
      cnt = freq[y]
      ans += cnt
      ans -= mod if ans >= mod
    end
    freq[x] += 1
  end

  ans % mod
end
```

## Scala

```scala
object Solution {
    def countPairs(deliciousness: Array[Int]): Int = {
        val MOD = 1000000007L
        if (deliciousness.isEmpty) return 0

        // maximum possible sum
        var maxVal = deliciousness.max
        var maxSum = maxVal * 2
        // generate powers of two up to a value larger than any possible sum
        val powers = scala.collection.mutable.ArrayBuffer[Long]()
        var p = 1L
        while (p <= (maxSum << 1)) {
            powers += p
            p <<= 1
        }

        import scala.collection.mutable
        val freq = mutable.Map[Int, Long]().withDefaultValue(0L)
        var ans = 0L

        for (x <- deliciousness) {
            for (pow <- powers) {
                val need = pow - x
                if (need >= 0 && need <= Int.MaxValue) {
                    ans += freq.getOrElse(need.toInt, 0L)
                }
            }
            freq(x) = freq(x) + 1L
        }

        ((ans % MOD).toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(deliciousness: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt: std::collections::HashMap<i32, i64> = std::collections::HashMap::new();
        // powers of two up to 2^21 (max possible sum)
        let powers: Vec<i32> = (0..=21).map(|i| 1_i32 << i).collect();

        let mut ans: i64 = 0;
        for &x in deliciousness.iter() {
            for &p in powers.iter() {
                let need = p - x;
                if need < 0 {
                    continue;
                }
                if let Some(&c) = cnt.get(&need) {
                    ans += c;
                    if ans >= MOD {
                        ans %= MOD;
                    }
                }
            }
            *cnt.entry(x).or_insert(0) += 1;
        }
        (ans % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-pairs deliciousness)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((freq (make-hash))
         ;; pre‑compute powers of two up to 2^21
         (powers (let loop ((i 0) (acc '()))
                   (if (> i 21)
                       (reverse acc)
                       (loop (+ i 1) (cons (arithmetic-shift 1 i) acc)))))
         (ans 0))
    (for ([x deliciousness])
      (for ([p powers])
        (let ((need (- p x)))
          (when (>= need 0)
            (let ((cnt (hash-ref freq need 0)))
              (when (> cnt 0)
                (set! ans (modulo (+ ans cnt) MOD)))))))
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    ans))
```

## Erlang

```erlang
-spec count_pairs(Deliciousness :: [integer()]) -> integer().
count_pairs(Deliciousness) ->
    Mod = 1000000007,
    Powers = [1 bsl K || K <- lists:seq(0,21)],
    loop(Deliciousness, #{}, 0, Mod, Powers).

loop([], _Map, Ans, _Mod, _Powers) -> Ans rem _Mod;
loop([X|Rest], Map, Ans, Mod, Powers) ->
    Contribution = contrib(Powers, X, Map, 0),
    NewAns = (Ans + Contribution) rem Mod,
    NewMap = maps:update_with(X, fun(C) -> C+1 end, 1, Map),
    loop(Rest, NewMap, NewAns, Mod, Powers).

contrib([], _X, _Map, Acc) -> Acc;
contrib([P|Ps], X, Map, Acc) ->
    Target = P - X,
    case maps:get(Target, Map, undefined) of
        undefined -> contrib(Ps, X, Map, Acc);
        Count -> contrib(Ps, X, Map, Acc + Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(deliciousness :: [integer]) :: integer
  def count_pairs(deliciousness) do
    mod = 1_000_000_007
    powers = for i <- 0..21, do: 1 <<< i

    {_freq_map, result} =
      Enum.reduce(deliciousness, {%{}, 0}, fn x, {freq, ans} ->
        add =
          Enum.reduce(powers, 0, fn p, acc ->
            y = p - x
            cnt = Map.get(freq, y, 0)
            (acc + cnt) |> rem(mod)
          end)

        new_ans = (ans + add) |> rem(mod)
        new_freq = Map.update(freq, x, 1, &(&1 + 1))
        {new_freq, new_ans}
      end)

    result
  end
end
```
