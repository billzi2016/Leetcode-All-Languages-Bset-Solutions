# 1224. Maximum Equal Frequency

## Cpp

```cpp
class Solution {
public:
    int maxEqualFreq(vector<int>& nums) {
        int n = nums.size();
        const int MAXV = 100000;
        vector<int> cnt(MAXV + 1, 0);
        vector<int> freqCount(n + 2, 0); // frequency -> how many numbers have this frequency
        int maxFreq = 0;
        int distinct = 0;
        int answer = 0;

        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            if (cnt[x] == 0) ++distinct;

            int prev = cnt[x];
            if (prev > 0) --freqCount[prev];

            ++cnt[x];
            int cur = cnt[x];
            ++freqCount[cur];
            maxFreq = max(maxFreq, cur);

            int len = i + 1;
            bool ok = false;

            if (maxFreq == 1) {
                // all numbers appear once
                ok = true;
            } else if (distinct == 1) {
                // only one distinct number
                ok = true;
            } else {
                // case: one number appears once, others have frequency maxFreq
                if (freqCount[1] == 1 && maxFreq * freqCount[maxFreq] == len - 1)
                    ok = true;

                // case: one number has frequency maxFreq, others have maxFreq-1
                if (maxFreq > 1 && freqCount[maxFreq] == 1 &&
                    (maxFreq - 1) * (freqCount[maxFreq - 1] + 1) == len - 1)
                    ok = true;
            }

            if (ok) answer = len;
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int maxEqualFreq(int[] nums) {
        int n = nums.length;
        int maxVal = 100000; // as per constraints
        int[] cnt = new int[maxVal + 1];
        int[] freqCnt = new int[n + 2]; // frequency can go up to n
        int distinct = 0;
        int maxFreq = 0;
        int answer = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (cnt[x] == 0) {
                distinct++;
            }
            // decrease count of previous frequency
            if (cnt[x] > 0) {
                freqCnt[cnt[x]]--;
            }
            cnt[x]++;
            maxFreq = Math.max(maxFreq, cnt[x]);
            freqCnt[cnt[x]]++;

            int len = i + 1;
            boolean ok = false;

            // case 1: all frequencies are 1
            if (maxFreq == 1) {
                ok = true;
            }
            // case 2: one number has frequency maxFreq, others have maxFreq-1
            else if (freqCnt[maxFreq] == 1 && (maxFreq - 1) * (distinct - 1) + maxFreq == len) {
                ok = true;
            }
            // case 3: one number occurs once, others have frequency maxFreq
            else if (freqCnt[1] == 1 && maxFreq * (distinct - 1) + 1 == len) {
                ok = true;
            }

            if (ok) {
                answer = len;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        cnt = defaultdict(int)          # number -> frequency
        freqCnt = defaultdict(int)      # frequency -> how many numbers have this frequency
        distinct = 0                     # number of distinct values seen so far
        maxFreq = 0
        ans = 0

        for i, x in enumerate(nums):
            prev = cnt[x]
            if prev:
                freqCnt[prev] -= 1
                if freqCnt[prev] == 0:
                    del freqCnt[prev]
            else:
                distinct += 1

            cur = prev + 1
            cnt[x] = cur
            freqCnt[cur] += 1
            if cur > maxFreq:
                maxFreq = cur

            n = i + 1  # current prefix length

            # condition 1: all frequencies are 1
            if maxFreq == 1:
                ans = n
            # condition 2: one number has frequency maxFreq, others have maxFreq-1
            elif freqCnt.get(maxFreq, 0) == 1 and (maxFreq - 1) * (distinct - 1) + maxFreq == n:
                ans = n
            # condition 3: one number appears once, others have frequency maxFreq
            elif freqCnt.get(1, 0) == 1 and maxFreq * (distinct - 1) + 1 == n:
                ans = n

        return ans
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt = defaultdict(int)          # number -> its count
        freq = defaultdict(int)         # frequency -> how many numbers have this frequency
        maxF = 0
        ans = 0

        for i, x in enumerate(nums):
            old = cnt[x]
            if old > 0:
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]

            cnt[x] = old + 1
            new = old + 1
            freq[new] += 1

            maxF = max(maxF, new)
            n = i + 1

            ok = False
            if maxF == 1:
                ok = True
            elif freq.get(1, 0) == 1 and maxF * freq[maxF] == n - 1:
                ok = True
            elif freq.get(maxF, 0) == 1 and (maxF - 1) * freq.get(maxF - 1, 0) + maxF == n:
                ok = True

            if ok:
                ans = n

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int maxEqualFreq(int* nums, int numsSize) {
    const int MAX_VAL = 100000;
    static int freq[MAX_VAL + 5];
    memset(freq, 0, sizeof(freq));

    int *freqCount = (int*)calloc(numsSize + 2, sizeof(int));
    if (!freqCount) return 0;

    int maxFreq = 0;
    int distinct = 0;
    int answer = 0;

    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        int old = freq[val];

        if (old > 0) {
            freqCount[old]--;
        } else {
            distinct++;
        }

        freq[val]++;
        int cur = freq[val];
        freqCount[cur]++;

        if (cur > maxFreq) maxFreq = cur;

        int n = i + 1;
        bool ok = false;

        if (maxFreq == 1) {
            ok = true;                                   // all frequencies are 1
        } else {
            // one number has frequency maxFreq, others have maxFreq-1
            if (freqCount[maxFreq] == 1 &&
                (maxFreq - 1) * (distinct - 1) + maxFreq == n) {
                ok = true;
            }
            // one number has frequency 1, others have maxFreq
            else if (freqCount[1] == 1 &&
                     maxFreq * (distinct - 1) + 1 == n) {
                ok = true;
            }
        }

        if (ok) answer = n;
    }

    free(freqCount);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxEqualFreq(int[] nums) {
        int n = nums.Length;
        int[] cnt = new int[100001];
        int[] freqCount = new int[n + 2]; // frequency can be at most n
        int maxFreq = 0;
        int result = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int prev = cnt[x];
            if (prev > 0) {
                freqCount[prev]--;
            }
            cnt[x]++;
            int cur = cnt[x];
            freqCount[cur]++;
            if (cur > maxFreq) maxFreq = cur;

            int len = i + 1;
            bool ok = false;

            if (maxFreq == 1) {
                ok = true; // all frequencies are 1
            } else {
                int countMax = freqCount[maxFreq];
                int countMaxMinusOne = maxFreq > 1 ? freqCount[maxFreq - 1] : 0;
                int countOne = freqCount[1];

                // case: one number has frequency maxFreq, others have maxFreq-1
                if (countMax == 1 && countMaxMinusOne * (maxFreq - 1) + maxFreq == len) {
                    ok = true;
                }
                // case: one number has frequency 1, others have maxFreq
                else if (countOne == 1 && countMax * maxFreq + 1 == len) {
                    ok = true;
                }
            }

            if (ok) result = len;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxEqualFreq = function(nums) {
    const n = nums.length;
    const cnt = new Map();                 // number -> its count
    const freq = new Array(n + 2).fill(0); // frequency -> how many numbers have this frequency
    let maxF = 0;                          // current maximum frequency
    let ans = 0;

    for (let i = 0; i < n; ++i) {
        const x = nums[i];
        const oldCnt = cnt.get(x) || 0;
        const newCnt = oldCnt + 1;
        cnt.set(x, newCnt);

        if (oldCnt > 0) freq[oldCnt]--;
        freq[newCnt]++;

        if (newCnt > maxF) maxF = newCnt;

        const total = i + 1; // length of current prefix

        // Case 1: all frequencies are 1
        if (maxF === 1) {
            ans = total;
            continue;
        }

        // Case 2: one number has frequency maxF, others have maxF-1
        if (
            freq[maxF] === 1 &&
            freq[maxF] * maxF + freq[maxF - 1] * (maxF - 1) === total
        ) {
            ans = total;
            continue;
        }

        // Case 3: one number occurs once, others have frequency maxF
        if (
            freq[1] === 1 &&
            freq[maxF] * maxF + 1 === total
        ) {
            ans = total;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxEqualFreq(nums: number[]): number {
    const n = nums.length;
    const cnt = new Array(100001).fill(0);
    const freqCnt = new Array(n + 2).fill(0);
    let maxF = 0;
    let ans = 0;

    for (let i = 0; i < n; ++i) {
        const x = nums[i];
        const prev = cnt[x];
        if (prev > 0) freqCnt[prev]--;
        cnt[x]++;
        const cur = cnt[x];
        freqCnt[cur]++;
        if (cur > maxF) maxF = cur;

        const total = i + 1;
        let ok = false;

        if (maxF === 1) {
            ok = true;
        } else if (
            freqCnt[maxF] * maxF + freqCnt[maxF - 1] * (maxF - 1) === total &&
            freqCnt[maxF] === 1
        ) {
            ok = true;
        } else if (
            freqCnt[1] === 1 &&
            maxF * freqCnt[maxF] === total - 1
        ) {
            ok = true;
        }

        if (ok) ans = total;
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
    function maxEqualFreq($nums) {
        $n = count($nums);
        $cnt = [];          // value => frequency
        $freqCnt = [];      // frequency => how many values have this frequency
        $maxFreq = 0;       // current maximum frequency
        $distinct = 0;      // number of distinct values seen so far
        $ans = 0;

        for ($i = 0; $i < $n; ++$i) {
            $v = $nums[$i];
            $old = $cnt[$v] ?? 0;
            if ($old > 0) {
                $freqCnt[$old] = ($freqCnt[$old] ?? 0) - 1;
            } else {
                // first occurrence of this value
                ++$distinct;
            }

            $new = $old + 1;
            $cnt[$v] = $new;
            $freqCnt[$new] = ($freqCnt[$new] ?? 0) + 1;

            if ($new > $maxFreq) {
                $maxFreq = $new;
            }

            $total = $i + 1; // length of current prefix

            // Case 1: all frequencies are 1
            if ($maxFreq == 1) {
                $ans = $total;
                continue;
            }

            $cntMax = $freqCnt[$maxFreq] ?? 0;
            $cntOne = $freqCnt[1] ?? 0;

            // Case 2: one number has frequency maxFreq, others have maxFreq-1
            if ($cntMax == 1 && ($maxFreq - 1) * $distinct + 1 == $total) {
                $ans = $total;
                continue;
            }

            // Case 3: one number occurs once, others have frequency maxFreq
            if ($cntOne == 1 && $maxFreq * ($distinct - 1) + 1 == $total) {
                $ans = $total;
                continue;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxEqualFreq(_ nums: [Int]) -> Int {
        var count = [Int:Int]()          // number -> its frequency
        var freqCount = [Int:Int]()      // frequency -> how many numbers have this frequency
        var maxFreq = 0
        var answer = 0

        for (i, num) in nums.enumerated() {
            let prev = count[num] ?? 0
            if prev > 0 {
                if let cur = freqCount[prev] {
                    if cur == 1 {
                        freqCount.removeValue(forKey: prev)
                    } else {
                        freqCount[prev] = cur - 1
                    }
                }
            }

            let newFreq = prev + 1
            count[num] = newFreq
            freqCount[newFreq, default: 0] += 1
            if newFreq > maxFreq { maxFreq = newFreq }

            let total = i + 1
            let cntMax = freqCount[maxFreq] ?? 0
            let cntMaxMinusOne = freqCount[maxFreq - 1] ?? 0
            let cntOne = freqCount[1] ?? 0

            var valid = false
            if maxFreq == 1 {
                valid = true
            } else if cntMax == 1 && (maxFreq * cntMax + (maxFreq - 1) * cntMaxMinusOne == total) {
                valid = true
            } else if cntOne == 1 && (maxFreq * cntMax + 1 == total) {
                valid = true
            }

            if valid { answer = total }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxEqualFreq(nums: IntArray): Int {
        val n = nums.size
        val cnt = IntArray(100001)
        val freqCount = IntArray(n + 2)
        var maxFreq = 0
        var ans = 0
        for (i in 0 until n) {
            val x = nums[i]
            val old = cnt[x]
            if (old > 0) {
                freqCount[old]--
            }
            val newc = old + 1
            cnt[x] = newc
            freqCount[newc]++
            if (newc > maxFreq) maxFreq = newc

            val len = i + 1
            if (maxFreq == 1) {
                ans = len
            } else {
                val cntMax = freqCount[maxFreq]
                // one number occurs once, others have frequency maxFreq
                if (cntMax * maxFreq == len - 1 && freqCount[1] == 1) {
                    ans = len
                }
                // one number has frequency maxFreq, others have maxFreq-1
                if (freqCount[maxFreq - 1] * (maxFreq - 1) + maxFreq == len && cntMax == 1) {
                    ans = len
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxEqualFreq(List<int> nums) {
    int n = nums.length;
    const int MAX_VAL = 100000;
    List<int> cnt = List.filled(MAX_VAL + 1, 0);
    List<int> freqCnt = List.filled(n + 2, 0);
    int distinct = 0;
    int maxFreq = 0;
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      int prev = cnt[x];
      if (prev > 0) {
        freqCnt[prev]--;
      } else {
        distinct++;
      }
      cnt[x] = prev + 1;
      int curFreq = cnt[x];
      freqCnt[curFreq]++;
      if (curFreq > maxFreq) maxFreq = curFreq;

      int len = i + 1;
      bool ok = false;
      if (maxFreq == 1) {
        ok = true;
      } else if (freqCnt[1] == 1 && maxFreq * (distinct - 1) + 1 == len) {
        ok = true;
      } else if (freqCnt[maxFreq] == 1 &&
          (maxFreq - 1) * (distinct - 1) + maxFreq == len) {
        ok = true;
      }

      if (ok) ans = len;
    }
    return ans;
  }
}
```

## Golang

```go
func maxEqualFreq(nums []int) int {
    n := len(nums)
    // constraints: nums[i] <= 100000
    cnt := make([]int, 100001)
    freqCount := make([]int, n+2) // frequencies up to n
    maxFreq := 0
    ans := 0

    for i, x := range nums {
        prev := cnt[x]
        if prev > 0 {
            freqCount[prev]--
        }
        cnt[x] = prev + 1
        cur := cnt[x]
        freqCount[cur]++
        if cur > maxFreq {
            maxFreq = cur
        }

        total := i + 1

        if maxFreq == 1 {
            ans = total
        } else {
            // case: one number has frequency maxFreq, others have maxFreq-1
            if freqCount[maxFreq] == 1 && (freqCount[maxFreq-1]*(maxFreq-1)+maxFreq) == total {
                ans = total
            }
            // case: one number appears once, others have frequency maxFreq
            if freqCount[1] == 1 && freqCount[maxFreq]*maxFreq == total-1 {
                ans = total
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_equal_freq(nums)
  cnt = Hash.new(0)
  freq = Hash.new(0)
  max_freq = 0
  ans = 0

  nums.each_with_index do |x, i|
    prev = cnt[x]
    cnt[x] = prev + 1
    freq[prev] -= 1 if prev > 0
    freq[prev + 1] += 1
    max_freq = [max_freq, prev + 1].max

    total = i + 1

    if max_freq == 1
      ans = total
    elsif freq[max_freq] * max_freq == total - 1 && freq[1] == 1
      ans = total
    elsif freq[max_freq] == 1 && (max_freq - 1) * (freq[max_freq - 1] + 1) == total
      ans = total
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxEqualFreq(nums: Array[Int]): Int = {
        val n = nums.length
        val maxVal = 100000
        val cnt = new Array[Int](maxVal + 1)
        val freqCount = new Array[Int](n + 2) // frequencies up to n
        var maxFreq = 0
        var distinct = 0
        var ans = 0

        for (i <- nums.indices) {
            val x = nums(i)
            val prev = cnt(x)
            if (prev > 0) freqCount(prev) -= 1 else distinct += 1
            cnt(x) = prev + 1
            val cur = cnt(x)
            freqCount(cur) += 1
            if (cur > maxFreq) maxFreq = cur

            val total = i + 1
            var ok = false
            if (maxFreq == 1) {
                ok = true
            } else {
                // one number has frequency maxFreq, others have maxFreq-1
                if (freqCount(maxFreq) == 1 && (maxFreq - 1) * (distinct - 1) + maxFreq == total) {
                    ok = true
                }
                // one number appears once, others have frequency maxFreq
                else if (freqCount(1) == 1 && maxFreq * (distinct - 1) == total - 1) {
                    ok = true
                }
            }

            if (ok) ans = total
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_equal_freq(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        // constraints: 1 <= nums[i] <= 100000
        let mut cnt = vec![0usize; 100_001];
        let mut freq = vec![0usize; n + 2]; // frequency -> how many numbers have this frequency
        let mut maxf = 0usize;
        let mut ans = 0i32;

        for (i, &num) in nums.iter().enumerate() {
            let x = num as usize;
            if cnt[x] > 0 {
                freq[cnt[x]] -= 1;
            }
            cnt[x] += 1;
            let c = cnt[x];
            freq[c] += 1;
            if c > maxf {
                maxf = c;
            }

            let len = i + 1;

            // case 1: all frequencies are 1
            if maxf == 1 {
                ans = len as i32;
            }
            // case 2: one number has frequency maxf, others have maxf-1
            else if freq[maxf] * maxf + freq[maxf - 1] * (maxf - 1) == len && freq[maxf] == 1 {
                ans = len as i32;
            }
            // case 3: one number has frequency 1, others have maxf
            else if freq[1] == 1 && freq[maxf] * maxf == len - 1 {
                ans = len as i32;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-equal-freq nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((cnt (make-hash))
         (freqCnt (make-hash))
         (maxFreq 0)
         (distinct 0)
         (ans 0))
    (for ([x nums] [i (in-naturals)])
      (define old (hash-ref cnt x 0))
      (when (= old 0) (set! distinct (+ distinct 1)))
      (define new (+ old 1))
      (hash-set! cnt x new)
      ;; update frequency of counts
      (when (> old 0)
        (define prev (hash-ref freqCnt old 0))
        (hash-set! freqCnt old (- prev 1)))
      (define cur (hash-ref freqCnt new 0))
      (hash-set! freqCnt new (+ cur 1))
      ;; update max frequency
      (when (> new maxFreq) (set! maxFreq new))
      (define total (+ i 1))
      (define cfmax (hash-ref freqCnt maxFreq 0))
      (define cfmaxMinus (if (> maxFreq 1)
                             (hash-ref freqCnt (- maxFreq 1) 0)
                             0))
      (define cf1 (hash-ref freqCnt 1 0))
      (when (or (= maxFreq 1)
                (and (= cfmax 1)
                     (= (+ (* cfmax maxFreq)
                           (* cfmaxMinus (- maxFreq 1)))
                        total))
                (and (= cf1 1)
                     (= (+ (* cfmax maxFreq)
                           (* (- distinct cfmax) (- maxFreq 1)))
                        total)))
        (set! ans total)))
    ans))
```

## Erlang

```erlang
-spec max_equal_freq(Nums :: [integer()]) -> integer().
max_equal_freq(Nums) ->
    helper(Nums, #{}, #{}, 0, 0, 0, 0).

helper([], _CntMap, _FreqCount, _MaxFreq, _Distinct, _Pos, Ans) ->
    Ans;
helper([Num | Rest], CntMap, FreqCount, MaxFreq, Distinct, Pos, Ans) ->
    NewPos = Pos + 1,
    PrevFreq = maps:get(Num, CntMap, 0),
    NewFreq = PrevFreq + 1,
    CntMap2 = maps:put(Num, NewFreq, CntMap),

    %% Decrease count of previous frequency if it existed
    FreqCount1 =
        case PrevFreq of
            0 -> FreqCount;
            _ ->
                CountPrev = maps:get(PrevFreq, FreqCount),
                NewCountPrev = CountPrev - 1,
                if
                    NewCountPrev == 0 ->
                        maps:remove(PrevFreq, FreqCount);
                    true ->
                        maps:put(PrevFreq, NewCountPrev, FreqCount)
                end
        end,

    %% Increase count of new frequency
    CountNew = maps:get(NewFreq, FreqCount1, 0),
    FreqCount2 = maps:put(NewFreq, CountNew + 1, FreqCount1),

    NewMaxFreq = if NewFreq > MaxFreq -> NewFreq; true -> MaxFreq end,
    NewDistinct = if PrevFreq == 0 -> Distinct + 1; true -> Distinct end,

    %% Retrieve needed counts
    CountMax = maps:get(NewMaxFreq, FreqCount2),
    CountOne = maps:get(1, FreqCount2, 0),

    Cond1 = (NewMaxFreq == 1),
    Cond2 = (CountMax == 1) andalso ((NewMaxFreq - 1) * (NewDistinct - 1) + NewMaxFreq == NewPos),
    Cond3 = (CountOne == 1) andalso (NewMaxFreq * (NewDistinct - 1) == NewPos - 1),

    NewAns = if Cond1 orelse Cond2 orelse Cond3 -> NewPos; true -> Ans end,

    helper(Rest, CntMap2, FreqCount2, NewMaxFreq, NewDistinct, NewPos, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_equal_freq(nums :: [integer]) :: integer
  def max_equal_freq(nums) do
    {_cnt, _freq, _maxf, ans} =
      Enum.reduce(Enum.with_index(nums, 1), {%{}, %{}, 0, 0}, fn {num, i},
          {cnt_map, freq_map, max_f, best} ->
        prev = Map.get(cnt_map, num, 0)
        new = prev + 1

        cnt_map2 = Map.put(cnt_map, num, new)

        # decrement previous frequency count
        freq_map1 =
          if prev > 0 do
            case Map.get(freq_map, prev) do
              1 -> Map.delete(freq_map, prev)
              v -> Map.put(freq_map, prev, v - 1)
            end
          else
            freq_map
          end

        # increment new frequency count
        freq_map2 = Map.update(freq_map1, new, 1, &(&1 + 1))

        max_f2 = if new > max_f, do: new, else: max_f

        distinct = map_size(cnt_map2)
        total = i
        cnt_max = Map.get(freq_map2, max_f2, 0)
        freq_one_cnt = Map.get(freq_map2, 1, 0)

        valid =
          cond do
            max_f2 == 1 -> true
            cnt_max == 1 and (max_f2 - 1) * distinct == total - 1 -> true
            freq_one_cnt == 1 and max_f2 * (distinct - 1) == total - 1 -> true
            true -> false
          end

        best2 = if valid, do: i, else: best

        {cnt_map2, freq_map2, max_f2, best2}
      end)

    ans
  end
end
```
