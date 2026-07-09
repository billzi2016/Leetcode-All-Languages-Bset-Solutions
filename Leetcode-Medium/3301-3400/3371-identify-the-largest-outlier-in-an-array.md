# 3371. Identify the Largest Outlier in an Array

## Cpp

```cpp
class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        long long total = 0;
        unordered_map<int,int> cnt;
        for (int v : nums) {
            total += v;
            ++cnt[v];
        }
        int ans = INT_MIN;
        for (int x : nums) {
            long long diff = total - x;
            if ((diff & 1LL) != 0) continue; // not even
            long long yll = diff / 2;
            if (yll < INT_MIN || yll > INT_MAX) continue;
            int y = static_cast<int>(yll);
            auto it = cnt.find(y);
            if (it == cnt.end()) continue;
            if (x == y) {
                if (it->second >= 2) {
                    ans = max(ans, x);
                }
            } else {
                ans = max(ans, x);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int getLargestOutlier(int[] nums) {
        int offset = 1000;
        int[] cnt = new int[2001];
        long total = 0;
        for (int num : nums) {
            cnt[num + offset]++;
            total += num;
        }
        int maxOutlier = Integer.MIN_VALUE;
        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] == 0) continue;
            int v = i - offset;
            long oLong = total - 2L * v;
            if (oLong < -1000 || oLong > 1000) continue;
            int o = (int) oLong;
            int idxO = o + offset;
            if (idxO < 0 || idxO >= cnt.length) continue;
            if (cnt[idxO] == 0) continue;
            if (o == v) {
                if (cnt[i] >= 2) {
                    maxOutlier = Math.max(maxOutlier, o);
                }
            } else {
                maxOutlier = Math.max(maxOutlier, o);
            }
        }
        return maxOutlier;
    }
}
```

## Python

```python
class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        total = sum(nums)
        cnt = Counter(nums)
        for val in sorted(cnt.keys(), reverse=True):
            if (total - val) & 1:
                continue
            s = (total - val) // 2
            if s not in cnt:
                continue
            if val == s:
                if cnt[val] >= 2:
                    return val
            else:
                # need at least one occurrence of sum element distinct from outlier
                # cnt[s] >=1 already ensured
                return val
        # According to problem guarantees, this line should never be reached
        return None
```

## Python3

```python
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1

        ans = -10**9
        for o in nums:
            diff = total - o
            if diff & 1:  # not even
                continue
            target = diff // 2
            if target not in cnt:
                continue
            if o == target:
                if cnt[o] >= 2:
                    ans = max(ans, o)
            else:
                ans = max(ans, o)
        return ans
```

## C

```c
int getLargestOutlier(int* nums, int numsSize) {
    const int OFFSET = 1000;
    const int RANGE = 2001; // -1000 .. 1000
    int freq[RANGE] = {0};
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
        freq[nums[i] + OFFSET]++;
    }
    
    int best = INT_MIN;
    for (int v = -1000; v <= 1000; ++v) {
        if (freq[v + OFFSET] == 0) continue;
        long long outlierLL = total - 2LL * v;
        if (outlierLL < -1000 || outlierLL > 1000) continue;
        int o = (int)outlierLL;
        if (o == v) {
            if (freq[v + OFFSET] >= 2 && o > best) best = o;
        } else {
            if (freq[o + OFFSET] >= 1 && o > best) best = o;
        }
    }
    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int GetLargestOutlier(int[] nums) {
        long total = 0;
        var count = new Dictionary<int, int>();
        foreach (int x in nums) {
            total += x;
            if (count.ContainsKey(x)) count[x]++; else count[x] = 1;
        }
        int best = int.MinValue;
        foreach (int v in nums) {
            long diff = total - v;
            if ((diff & 1L) != 0) continue; // not even, cannot form sum
            long sLong = diff / 2;
            if (sLong < int.MinValue || sLong > int.MaxValue) continue;
            int s = (int)sLong;
            if (!count.ContainsKey(s)) continue;
            if (v == s) {
                if (count[v] >= 2) best = Math.Max(best, v);
            } else {
                // at least one occurrence of s exists
                best = Math.Max(best, v);
            }
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var getLargestOutlier = function(nums) {
    const freq = new Map();
    let total = 0;
    for (const v of nums) {
        total += v;
        freq.set(v, (freq.get(v) || 0) + 1);
    }
    let answer = -Infinity;
    for (const [val, cnt] of freq.entries()) {
        const sumRemaining = total - val; // remove candidate outlier
        if (sumRemaining % 2 !== 0) continue; // must be even
        const s = sumRemaining / 2; // potential sum element value
        let cntS = freq.get(s) || 0;
        if (s === val) {
            // one occurrence used as outlier, need another for the sum element
            cntS -= 1;
        }
        if (cntS >= 1) {
            if (val > answer) answer = val;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function getLargestOutlier(nums: number[]): number {
    let total = 0;
    const freq = new Map<number, number>();
    for (const v of nums) {
        total += v;
        freq.set(v, (freq.get(v) ?? 0) + 1);
    }
    let ans = -Infinity;
    for (const [x, cntX] of freq.entries()) {
        const o = total - 2 * x;
        if (!freq.has(o)) continue;
        if (o === x) {
            if (cntX >= 2 && o > ans) ans = o;
        } else {
            if (o > ans) ans = o;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function getLargestOutlier($nums) {
        $total = 0;
        $cnt = [];
        foreach ($nums as $num) {
            $total += $num;
            if (isset($cnt[$num])) {
                $cnt[$num]++;
            } else {
                $cnt[$num] = 1;
            }
        }

        $maxOutlier = null;

        foreach ($cnt as $sumVal => $freqSum) {
            $outlier = $total - 2 * $sumVal;
            if (!isset($cnt[$outlier])) {
                continue;
            }
            if ($outlier == $sumVal) {
                if ($freqSum < 2) {
                    continue;
                }
            } else {
                // need at least one occurrence of outlier, already ensured by isset
                // and at least one sumVal (guaranteed by loop)
            }

            if ($maxOutlier === null || $outlier > $maxOutlier) {
                $maxOutlier = $outlier;
            }
        }

        return $maxOutlier;
    }
}
```

## Swift

```swift
class Solution {
    func getLargestOutlier(_ nums: [Int]) -> Int {
        var freq = [Int:Int]()
        var total = 0
        for v in nums {
            total += v
            freq[v, default: 0] += 1
        }
        var answer = Int.min
        for (x, cntX) in freq {
            let o = total - 2 * x
            if let cntO = freq[o] {
                if o == x {
                    if cntX >= 2 && o > answer {
                        answer = o
                    }
                } else {
                    if o > answer {
                        answer = o
                    }
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getLargestOutlier(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        var total = 0L
        for (v in nums) {
            total += v.toLong()
            freq[v] = (freq[v] ?: 0) + 1
        }
        var answer: Int? = null
        for ((x, cntX) in freq) {
            val diff = total - x
            if ((diff and 1L) != 0L) continue  // not even, cannot form O
            val oLong = total - 2L * x
            if (oLong < Int.MIN_VALUE.toLong() || oLong > Int.MAX_VALUE.toLong()) continue
            val o = oLong.toInt()
            val cntO = freq[o] ?: 0
            if (cntO == 0) continue
            if (o == x) {
                if (cntX >= 2) {
                    answer = maxOf(answer ?: o, o)
                }
            } else {
                answer = maxOf(answer ?: o, o)
            }
        }
        return answer!!
    }
}
```

## Dart

```dart
class Solution {
  int getLargestOutlier(List<int> nums) {
    int total = 0;
    for (int v in nums) total += v;

    Map<int, int> freq = {};
    for (int v in nums) {
      freq[v] = (freq[v] ?? 0) + 1;
    }

    int maxOutlier = -9223372036854775808; // effectively negative infinity

    for (int s in freq.keys) {
      int o = total - 2 * s;
      if (!freq.containsKey(o)) continue;

      if (o == s) {
        if ((freq[s] ?? 0) >= 2 && o > maxOutlier) {
          maxOutlier = o;
        }
      } else {
        if (o > maxOutlier) {
          maxOutlier = o;
        }
      }
    }

    return maxOutlier;
  }
}
```

## Golang

```go
func getLargestOutlier(nums []int) int {
    freq := make(map[int]int)
    total := 0
    for _, v := range nums {
        total += v
        freq[v]++
    }
    maxOut := -1 << 31
    for _, v := range nums {
        rem := total - v
        if rem%2 != 0 {
            continue
        }
        s := rem / 2
        cnt := freq[s]
        if v == s {
            cnt--
        }
        if cnt > 0 && v > maxOut {
            maxOut = v
        }
    }
    return maxOut
}
```

## Ruby

```ruby
def get_largest_outlier(nums)
  total = nums.sum
  freq = Hash.new(0)
  nums.each { |v| freq[v] += 1 }
  max_outlier = nil
  freq.each_key do |x|
    o = total - 2 * x
    next unless freq.key?(o)
    if o == x
      next unless freq[x] >= 2
    end
    max_outlier = max_outlier.nil? ? o : [max_outlier, o].max
  end
  max_outlier
end
```

## Scala

```scala
object Solution {
    def getLargestOutlier(nums: Array[Int]): Int = {
        val total: Long = nums.foldLeft(0L)(_ + _)
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (v <- nums) {
            freq(v) = freq.getOrElse(v, 0) + 1
        }
        var ans = Int.MinValue
        for ((s, cntS) <- freq) {
            val oLong = total - 2L * s
            if (oLong >= Int.MinValue && oLong <= Int.MaxValue) {
                val o = oLong.toInt
                freq.get(o) match {
                    case Some(cntO) =>
                        if (s == o) {
                            if (cntS >= 2) ans = math.max(ans, o)
                        } else {
                            ans = math.max(ans, o)
                        }
                    case None => // do nothing
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn get_largest_outlier(nums: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut total: i64 = 0;
        for &v in &nums {
            *freq.entry(v).or_insert(0) += 1;
            total += v as i64;
        }

        let mut ans = i32::MIN;
        for &s in &nums {
            let outlier_i64 = total - 2 * (s as i64);
            // outlier must be an element of the array, its value fits i32 range
            let o = outlier_i64 as i32;
            if let Some(&cnt) = freq.get(&o) {
                if o == s {
                    if cnt >= 2 {
                        ans = ans.max(o);
                    }
                } else {
                    ans = ans.max(o);
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (get-largest-outlier nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((freq (make-hash))
         (total
          (foldl (lambda (x acc)
                   (hash-update! freq x add1 0)
                   (+ acc x))
                 0
                 nums)))
    (let loop ((lst nums) (best #f))
      (if (null? lst)
          best
          (let* ((o (car lst))
                 (rem (- total o)))
            (if (even? rem)
                (let ((target (/ rem 2)))
                  (define cnt-target (hash-ref freq target 0))
                  (if (and (= o target) (< cnt-target 2))
                      (loop (cdr lst) best)
                      (if (or (not (= o target)) (>= cnt-target 2))
                          (let ((new-best (if best (max best o) o)))
                            (loop (cdr lst) new-best))
                          (loop (cdr lst) best))))
                (loop (cdr lst) best)))))))
```

## Erlang

```erlang
-module(solution).
-export([get_largest_outlier/1]).
-spec get_largest_outlier(Nums :: [integer()]) -> integer().
get_largest_outlier(Nums) ->
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Nums),
    CountMap = build_count_map(Nums, #{}),
    Outliers = maps:fold(
        fun(X, Cx, Acc) ->
            O = Total - 2 * X,
            case maps:is_key(O, CountMap) of
                true ->
                    if O == X ->
                            case Cx >= 2 of
                                true -> [O | Acc];
                                false -> Acc
                            end;
                       true -> [O | Acc]
                    end;
                false -> Acc
            end
        end,
        [],
        CountMap),
    lists:max(Outliers).

build_count_map([], M) ->
    M;
build_count_map([H|T], M) ->
    NewM = maps:update_with(H, fun(C) -> C + 1 end, 1, M),
    build_count_map(T, NewM).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_largest_outlier(nums :: [integer]) :: integer
  def get_largest_outlier(nums) do
    total = Enum.sum(nums)

    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    Enum.reduce(freq, nil, fn {s, _cnt}, acc ->
      o = total - 2 * s
      needed = if s == o, do: 2, else: 1
      cnt_o = Map.get(freq, o, 0)

      if cnt_o >= needed do
        case acc do
          nil -> o
          cur when o > cur -> o
          _ -> acc
        end
      else
        acc
      end
    end)
  end
end
```
