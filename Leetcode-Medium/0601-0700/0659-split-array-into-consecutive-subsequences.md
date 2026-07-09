# 0659. Split Array into Consecutive Subsequences

## Cpp

```cpp
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int x : nums) ++freq[x];
        unordered_map<int, int> need; // subsequences waiting for this number
        for (int x : nums) {
            if (freq[x] == 0) continue;
            --freq[x];
            if (need[x - 1] > 0) {
                --need[x - 1];
                ++need[x];
            } else {
                if (freq[x + 1] <= 0 || freq[x + 2] <= 0) return false;
                --freq[x + 1];
                --freq[x + 2];
                ++need[x + 2];
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isPossible(int[] nums) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        for (int n : nums) {
            freq.put(n, freq.getOrDefault(n, 0) + 1);
        }
        java.util.Map<Integer, Integer> tails = new java.util.HashMap<>();
        for (int n : nums) {
            int count = freq.getOrDefault(n, 0);
            if (count == 0) continue;
            freq.put(n, count - 1);
            if (tails.getOrDefault(n - 1, 0) > 0) {
                tails.put(n - 1, tails.get(n - 1) - 1);
                tails.put(n, tails.getOrDefault(n, 0) + 1);
            } else {
                int c1 = freq.getOrDefault(n + 1, 0);
                int c2 = freq.getOrDefault(n + 2, 0);
                if (c1 > 0 && c2 > 0) {
                    freq.put(n + 1, c1 - 1);
                    freq.put(n + 2, c2 - 1);
                    tails.put(n + 2, tails.getOrDefault(n + 2, 0) + 1);
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter, defaultdict

        freq = Counter(nums)
        tails = defaultdict(int)

        for x in nums:
            if freq[x] == 0:
                continue
            freq[x] -= 1

            # try to extend a subsequence ending with x-1
            if tails[x - 1] > 0:
                tails[x - 1] -= 1
                tails[x] += 1
            else:
                # need to create new subsequence of length at least 3: x, x+1, x+2
                if freq.get(x + 1, 0) == 0 or freq.get(x + 2, 0) == 0:
                    return False
                freq[x + 1] -= 1
                freq[x + 2] -= 1
                tails[x + 2] += 1

        return True
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = {}
        for x in nums:
            if freq[x] == 0:
                continue
            freq[x] -= 1
            if need.get(x, 0) > 0:
                need[x] -= 1
                need[x + 1] = need.get(x + 1, 0) + 1
            else:
                if freq.get(x + 1, 0) > 0 and freq.get(x + 2, 0) > 0:
                    freq[x + 1] -= 1
                    freq[x + 2] -= 1
                    need[x + 3] = need.get(x + 3, 0) + 1
                else:
                    return False
        return True
```

## C

```c
#include <stdbool.h>

bool isPossible(int* nums, int numsSize) {
    const int SHIFT = 1000;
    const int RANGE = 2001; // values from -1000 to 1000 inclusive
    int cnt[RANGE] = {0};
    int tail[RANGE] = {0};

    for (int i = 0; i < numsSize; ++i) {
        cnt[nums[i] + SHIFT]++;
    }

    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int idx = x + SHIFT;
        if (cnt[idx] == 0) continue;   // already used
        cnt[idx]--;

        // Try to extend a subsequence ending with x-1
        if (x - 1 >= -1000 && tail[x - 1 + SHIFT] > 0) {
            tail[x - 1 + SHIFT]--;
            tail[idx]++;
        } else {
            // Need to start a new subsequence of length at least 3: x, x+1, x+2
            if (x + 2 > 1000) return false;
            int idx1 = x + 1 + SHIFT;
            int idx2 = x + 2 + SHIFT;
            if (cnt[idx1] > 0 && cnt[idx2] > 0) {
                cnt[idx1]--;
                cnt[idx2]--;
                tail[idx2]++;
            } else {
                return false;
            }
        }
    }

    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsPossible(int[] nums)
    {
        var freq = new Dictionary<int, int>();
        foreach (var x in nums)
        {
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }

        var need = new Dictionary<int, int>();

        foreach (var x in nums)
        {
            if (freq[x] == 0) continue;

            // use current number
            freq[x]--;

            // try to extend a subsequence that ends with x-1
            if (need.TryGetValue(x, out int cnt) && cnt > 0)
            {
                need[x] = cnt - 1;
                int nxt = x + 1;
                need[nxt] = need.ContainsKey(nxt) ? need[nxt] + 1 : 1;
            }
            else
            {
                // try to create a new subsequence of length 3: x, x+1, x+2
                if (freq.TryGetValue(x + 1, out int c1) && c1 > 0 &&
                    freq.TryGetValue(x + 2, out int c2) && c2 > 0)
                {
                    freq[x + 1] = c1 - 1;
                    freq[x + 2] = c2 - 1;
                    int nxt = x + 3;
                    need[nxt] = need.ContainsKey(nxt) ? need[nxt] + 1 : 1;
                }
                else
                {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossible = function(nums) {
    const freq = new Map();
    for (const n of nums) {
        freq.set(n, (freq.get(n) || 0) + 1);
    }
    const tails = new Map(); // subsequences ending with key
    for (const n of nums) {
        if ((freq.get(n) || 0) === 0) continue;
        freq.set(n, freq.get(n) - 1);
        if ((tails.get(n - 1) || 0) > 0) {
            tails.set(n - 1, tails.get(n - 1) - 1);
            tails.set(n, (tails.get(n) || 0) + 1);
        } else {
            const cnt1 = freq.get(n + 1) || 0;
            const cnt2 = freq.get(n + 2) || 0;
            if (cnt1 > 0 && cnt2 > 0) {
                freq.set(n + 1, cnt1 - 1);
                freq.set(n + 2, cnt2 - 1);
                tails.set(n + 2, (tails.get(n + 2) || 0) + 1);
            } else {
                return false;
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function isPossible(nums: number[]): boolean {
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }
    const tails = new Map<number, number>();
    for (const n of nums) {
        if ((freq.get(n) ?? 0) === 0) continue;
        freq.set(n, (freq.get(n) ?? 0) - 1);

        const prevTail = tails.get(n - 1) ?? 0;
        if (prevTail > 0) {
            tails.set(n - 1, prevTail - 1);
            tails.set(n, (tails.get(n) ?? 0) + 1);
        } else {
            const cnt1 = freq.get(n + 1) ?? 0;
            const cnt2 = freq.get(n + 2) ?? 0;
            if (cnt1 > 0 && cnt2 > 0) {
                freq.set(n + 1, cnt1 - 1);
                freq.set(n + 2, cnt2 - 1);
                tails.set(n + 2, (tails.get(n + 2) ?? 0) + 1);
            } else {
                return false;
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isPossible($nums) {
        $freq = [];
        foreach ($nums as $num) {
            $freq[$num] = ($freq[$num] ?? 0) + 1;
        }

        $tails = [];

        foreach ($nums as $num) {
            if (($freq[$num] ?? 0) == 0) {
                continue;
            }
            // use current number
            $freq[$num]--;

            // try to extend a subsequence ending with num-1
            if (isset($tails[$num - 1]) && $tails[$num - 1] > 0) {
                $tails[$num - 1]--;
                $tails[$num] = ($tails[$num] ?? 0) + 1;
            } else {
                // need to create a new subsequence num, num+1, num+2
                if ((($freq[$num + 1] ?? 0) > 0) && (($freq[$num + 2] ?? 0) > 0)) {
                    $freq[$num + 1]--;
                    $freq[$num + 2]--;
                    $tails[$num + 2] = ($tails[$num + 2] ?? 0) + 1;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isPossible(_ nums: [Int]) -> Bool {
        var freq = [Int:Int]()
        for n in nums {
            freq[n, default: 0] += 1
        }
        var need = [Int:Int]()
        for num in nums {
            if (freq[num] ?? 0) == 0 { continue }
            freq[num]! -= 1
            if let cnt = need[num], cnt > 0 {
                need[num]! = cnt - 1
                need[num + 1, default: 0] += 1
            } else {
                if (freq[num + 1] ?? 0) > 0 && (freq[num + 2] ?? 0) > 0 {
                    freq[num + 1]! -= 1
                    freq[num + 2]! -= 1
                    need[num + 3, default: 0] += 1
                } else {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossible(nums: IntArray): Boolean {
        val freq = HashMap<Int, Int>()
        for (num in nums) {
            freq[num] = freq.getOrDefault(num, 0) + 1
        }
        val need = HashMap<Int, Int>()
        for (num in nums) {
            if (freq.getOrDefault(num, 0) == 0) continue
            // use current number
            freq[num] = freq[num]!! - 1
            if (need.getOrDefault(num, 0) > 0) {
                // extend an existing subsequence ending with num-1
                need[num] = need[num]!! - 1
                need[num + 1] = need.getOrDefault(num + 1, 0) + 1
            } else {
                // try to create a new subsequence num, num+1, num+2
                val cnt1 = freq.getOrDefault(num + 1, 0)
                val cnt2 = freq.getOrDefault(num + 2, 0)
                if (cnt1 > 0 && cnt2 > 0) {
                    freq[num + 1] = cnt1 - 1
                    freq[num + 2] = cnt2 - 1
                    need[num + 3] = need.getOrDefault(num + 3, 0) + 1
                } else {
                    return false
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isPossible(List<int> nums) {
    final Map<int, int> freq = {};
    for (var n in nums) {
      freq[n] = (freq[n] ?? 0) + 1;
    }
    final Map<int, int> need = {};

    for (final num in nums) {
      if ((freq[num] ?? 0) == 0) continue;

      // use one occurrence of num
      freq[num] = freq[num]! - 1;

      if ((need[num] ?? 0) > 0) {
        // extend an existing subsequence ending with num-1
        need[num] = need[num]! - 1;
        need[num + 1] = (need[num + 1] ?? 0) + 1;
      } else {
        // try to create a new subsequence num, num+1, num+2
        int cnt1 = freq[num + 1] ?? 0;
        int cnt2 = freq[num + 2] ?? 0;
        if (cnt1 > 0 && cnt2 > 0) {
          freq[num + 1] = cnt1 - 1;
          freq[num + 2] = cnt2 - 1;
          need[num + 3] = (need[num + 3] ?? 0) + 1;
        } else {
          return false;
        }
      }
    }

    return true;
  }
}
```

## Golang

```go
func isPossible(nums []int) bool {
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}
	tails := make(map[int]int)

	for _, v := range nums {
		if freq[v] == 0 {
			continue
		}
		freq[v]--
		if tails[v-1] > 0 {
			tails[v-1]--
			tails[v]++
		} else {
			if freq[v+1] <= 0 || freq[v+2] <= 0 {
				return false
			}
			freq[v+1]--
			freq[v+2]--
			tails[v+2]++
		}
	}
	return true
}
```

## Ruby

```ruby
def is_possible(nums)
  count = Hash.new(0)
  nums.each { |n| count[n] += 1 }
  need = Hash.new(0)

  nums.each do |num|
    next if count[num] == 0
    count[num] -= 1

    if need[num - 1] > 0
      need[num - 1] -= 1
      need[num] += 1
    elsif count[num + 1] > 0 && count[num + 2] > 0
      count[num + 1] -= 1
      count[num + 2] -= 1
      need[num + 2] += 1
    else
      return false
    end
  end

  true
end
```

## Scala

```scala
object Solution {
  def isPossible(nums: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
    for (x <- nums) {
      freq(x) = freq(x) + 1
    }
    val need = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)

    for (num <- nums) {
      if (freq(num) == 0) {
        // already used in a subsequence
      } else {
        freq(num) = freq(num) - 1
        if (need.getOrElse(num, 0) > 0) {
          need(num) = need(num) - 1
          need(num + 1) = need.getOrElse(num + 1, 0) + 1
        } else if (freq.getOrElse(num + 1, 0) > 0 && freq.getOrElse(num + 2, 0) > 0) {
          freq(num + 1) = freq(num + 1) - 1
          freq(num + 2) = freq(num + 2) - 1
          need(num + 3) = need.getOrElse(num + 3, 0) + 1
        } else {
          return false
        }
      }
    }
    true
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn is_possible(nums: Vec<i32>) -> bool {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut tails: HashMap<i32, i32> = HashMap::new();

        for &x in &nums {
            // use current number
            if let Some(cnt) = freq.get_mut(&x) {
                if *cnt == 0 {
                    continue;
                }
                *cnt -= 1;
            }

            // try to extend a subsequence ending with x-1
            if let Some(prev_cnt) = tails.get_mut(&(x - 1)) {
                if *prev_cnt > 0 {
                    *prev_cnt -= 1;
                    *tails.entry(x).or_insert(0) += 1;
                    continue;
                }
            }

            // try to create a new subsequence x, x+1, x+2
            let cnt1 = freq.get(&(x + 1)).cloned().unwrap_or(0);
            let cnt2 = freq.get(&(x + 2)).cloned().unwrap_or(0);
            if cnt1 > 0 && cnt2 > 0 {
                *freq.get_mut(&(x + 1)).unwrap() -= 1;
                *freq.get_mut(&(x + 2)).unwrap() -= 1;
                *tails.entry(x + 2).or_insert(0) += 1;
            } else {
                return false;
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (is-possible nums)
  (-> (listof exact-integer?) boolean?)
  (call-with-current-continuation
   (lambda (return)
     (let ((freq (make-hash))
           (need (make-hash)))
       ;; count frequencies
       (for ([x nums])
         (hash-set! freq x (+ (hash-ref freq x 0) 1)))
       ;; process each number
       (for ([x nums])
         (when (> (hash-ref freq x 0) 0)
           ;; use one occurrence of x
           (hash-set! freq x (- (hash-ref freq x) 1))
           (if (> (hash-ref need x 0) 0)
               (begin
                 (hash-set! need x (- (hash-ref need x) 1))
                 (hash-set! need (+ x 1) (+ (hash-ref need (+ x 1) 0) 1)))
               (if (and (> (hash-ref freq (+ x 1) 0) 0)
                        (> (hash-ref freq (+ x 2) 0) 0))
                   (begin
                     (hash-set! freq (+ x 1) (- (hash-ref freq (+ x 1)) 1))
                     (hash-set! freq (+ x 2) (- (hash-ref freq (+ x 2)) 1))
                     (hash-set! need (+ x 3) (+ (hash-ref need (+ x 3) 0) 1)))
                   (return #f)))))
       #t))))
```

## Erlang

```erlang
-module(solution).
-export([is_possible/1]).

-spec is_possible(Nums :: [integer()]) -> boolean().
is_possible(Nums) ->
    Freq = build_freq(Nums),
    process(Nums, Freq, #{}).

build_freq(List) ->
    lists:foldl(fun(N, Acc) -> inc_key(Acc, N) end, #{}, List).

inc_key(Map, Key) ->
    maps:put(Key, maps:get(Key, Map, 0) + 1, Map).

dec_key(Map, Key) ->
    case maps:get(Key, Map, 0) of
        0 -> Map;
        1 -> maps:remove(Key, Map);
        N when N > 1 -> maps:put(Key, N - 1, Map)
    end.

process([], _Freq, _Tails) ->
    true;
process([X|Rest], Freq, Tails) ->
    case maps:get(X, Freq, 0) of
        0 ->
            process(Rest, Freq, Tails);
        _Count ->
            NewFreq1 = dec_key(Freq, X),
            case maps:get(X-1, Tails, 0) of
                C when C > 0 ->
                    NewTails1 = dec_key(Tails, X-1),
                    NewTails2 = inc_key(NewTails1, X),
                    process(Rest, NewFreq1, NewTails2);
                _ ->
                    case {maps:get(X+1, NewFreq1, 0), maps:get(X+2, NewFreq1, 0)} of
                        {C1, C2} when C1 > 0, C2 > 0 ->
                            FreqAfterX1 = dec_key(NewFreq1, X+1),
                            FreqAfterX2 = dec_key(FreqAfterX1, X+2),
                            NewTails3 = inc_key(Tails, X+2),
                            process(Rest, FreqAfterX2, NewTails3);
                        _ ->
                            false
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible(nums :: [integer]) :: boolean
  def is_possible(nums) do
    freq = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    case Enum.reduce_while(nums, {freq, %{}}, fn x, {f, need} ->
           case Map.get(f, x, 0) do
             0 ->
               {:cont, {f, need}}

             _cnt ->
               f1 = Map.update!(f, x, &(&1 - 1))

               cond do
                 Map.get(need, x, 0) > 0 ->
                   need1 = Map.update!(need, x, &(&1 - 1))
                   need2 = Map.update(need1, x + 1, 1, fn v -> v + 1 end)
                   {:cont, {f1, need2}}

                 true ->
                   if Map.get(f1, x + 1, 0) > 0 and Map.get(f1, x + 2, 0) > 0 do
                     f2 = Map.update!(f1, x + 1, &(&1 - 1))
                     f3 = Map.update!(f2, x + 2, &(&1 - 1))
                     need2 = Map.update(need, x + 3, 1, fn v -> v + 1 end)
                     {:cont, {f3, need2}}
                   else
                     {:halt, false}
                   end
               end
           end
         end) do
      false -> false
      {_final_freq, _final_need} -> true
    end
  end
end
```
