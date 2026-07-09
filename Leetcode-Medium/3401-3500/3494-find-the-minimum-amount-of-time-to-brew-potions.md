# 3494. Find the Minimum Amount of Time to Brew Potions

## Cpp

```cpp
class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size();
        vector<long long> freeTime(n, 0);
        for (int x : mana) {
            long long prevFinish = 0;
            for (int i = 0; i < n; ++i) {
                long long start = max(freeTime[i], prevFinish);
                long long finish = start + (long long)skill[i] * x;
                freeTime[i] = finish;
                prevFinish = finish;
            }
        }
        return freeTime.empty() ? 0 : freeTime.back();
    }
};
```

## Java

```java
class Solution {
    public long minTime(int[] skill, int[] mana) {
        int n = skill.length;
        long[] f = new long[n];
        for (int x : mana) {
            long now = f[0];
            for (int i = 1; i < n; i++) {
                now = Math.max(now + (long) skill[i - 1] * x, f[i]);
            }
            long finish = now + (long) skill[n - 1] * x;
            f[n - 1] = finish;
            for (int i = n - 2; i >= 0; i--) {
                f[i] = f[i + 1] - (long) skill[i + 1] * x;
            }
        }
        return f[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n = len(skill)
        f = [0] * n  # completion time of each wizard after previous potion
        for x in mana:
            new_f = [0] * n
            # first wizard
            cur = f[0] + skill[0] * x
            new_f[0] = cur
            # remaining wizards
            for i in range(1, n):
                cur = max(f[i], cur) + skill[i] * x
                new_f[i] = cur
            f = new_f
        return f[-1]
```

## Python3

```python
from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        f = [0] * n  # earliest free time for each wizard
        for x in mana:
            now = f[0]
            for i in range(1, n):
                now = max(now + skill[i - 1] * x, f[i])
            f[-1] = now + skill[-1] * x
            # update earlier wizards' free times backwards
            for i in range(n - 2, -1, -1):
                f[i] = f[i + 1] - skill[i + 1] * x
        return f[-1]
```

## C

```c
#include <stddef.h>

long long minTime(int* skill, int skillSize, int* mana, int manaSize) {
    if (skillSize == 0 || manaSize == 0) return 0;
    long long *finish = (long long *)malloc(sizeof(long long) * skillSize);
    for (int i = 0; i < skillSize; ++i) finish[i] = 0;

    for (int j = 0; j < manaSize; ++j) {
        long long t = finish[0];
        finish[0] = t + (long long)skill[0] * mana[j];
        for (int i = 1; i < skillSize; ++i) {
            long long start = finish[i];
            if (start < finish[i - 1]) start = finish[i - 1];
            finish[i] = start + (long long)skill[i] * mana[j];
        }
    }

    long long result = finish[skillSize - 1];
    free(finish);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long MinTime(int[] skill, int[] mana) {
        int n = skill.Length;
        long[] finish = new long[n];
        foreach (int m in mana) {
            // First wizard
            finish[0] += (long)skill[0] * m;
            for (int i = 1; i < n; ++i) {
                long start = Math.Max(finish[i - 1], finish[i]);
                finish[i] = start + (long)skill[i] * m;
            }
        }
        return finish[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} skill
 * @param {number[]} mana
 * @return {number}
 */
var minTime = function(skill, mana) {
    const n = skill.length;
    const f = new Array(n).fill(0);
    for (let idx = 0; idx < mana.length; ++idx) {
        const x = mana[idx];
        let now = f[0];
        for (let i = 1; i < n; ++i) {
            now = Math.max(now + skill[i - 1] * x, f[i]);
        }
        f[n - 1] = now + skill[n - 1] * x;
        for (let i = n - 2; i >= 0; --i) {
            f[i] = f[i + 1] - skill[i + 1] * x;
        }
    }
    return f[n - 1];
};
```

## Typescript

```typescript
function minTime(skill: number[], mana: number[]): number {
    const n = skill.length;
    const f = new Array<number>(n).fill(0);
    for (let j = 0; j < mana.length; ++j) {
        const x = mana[j];
        let now = f[0];
        for (let i = 1; i < n; ++i) {
            now = Math.max(now + skill[i - 1] * x, f[i]);
        }
        f[n - 1] = now + skill[n - 1] * x;
        for (let i = n - 2; i >= 0; --i) {
            f[i] = f[i + 1] - skill[i + 1] * x;
        }
    }
    return f[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $skill
     * @param Integer[] $mana
     * @return Integer
     */
    function minTime($skill, $mana) {
        $n = count($skill);
        $dp = array_fill(0, $n, 0); // finish time of each wizard
        
        foreach ($mana as $x) {
            $prevFinish = 0; // finish time of previous wizard for current potion
            for ($i = 0; $i < $n; ++$i) {
                $start = max($dp[$i], $prevFinish);
                $finish = $start + $skill[$i] * $x;
                $dp[$i] = $finish;
                $prevFinish = $finish;
            }
        }
        
        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func minTime(_ skill: [Int], _ mana: [Int]) -> Int {
        let n = skill.count
        var f = Array(repeating: Int64(0), count: n)
        for m in mana {
            let x = Int64(m)
            var now = f[0]
            if n > 1 {
                for i in 1..<n {
                    let finishPrev = now + Int64(skill[i - 1]) * x
                    now = max(finishPrev, f[i])
                }
            }
            f[n - 1] = now + Int64(skill[n - 1]) * x
            if n > 1 {
                for i in stride(from: n - 2, through: 0, by: -1) {
                    f[i] = f[i + 1] - Int64(skill[i + 1]) * x
                }
            }
        }
        return Int(f[n - 1])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTime(skill: IntArray, mana: IntArray): Long {
        val n = skill.size
        val finish = LongArray(n)
        for (mInt in mana) {
            val m = mInt.toLong()
            var cur = finish[0] + skill[0].toLong() * m
            finish[0] = cur
            for (i in 1 until n) {
                val arrival = cur
                val ready = finish[i]
                cur = kotlin.math.max(arrival, ready) + skill[i].toLong() * m
                finish[i] = cur
            }
        }
        return finish[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int minTime(List<int> skill, List<int> mana) {
    int n = skill.length;
    List<int> f = List.filled(n, 0);
    for (int x in mana) {
      int now = f[0];
      for (int i = 1; i < n; ++i) {
        int finishPrev = now + skill[i - 1] * x;
        now = finishPrev < f[i] ? f[i] : finishPrev;
      }
      int finalFinish = now + skill[n - 1] * x;
      f[n - 1] = finalFinish;
      for (int i = n - 2; i >= 0; --i) {
        f[i] = f[i + 1] - skill[i + 1] * x;
      }
    }
    return f[n - 1];
  }
}
```

## Golang

```go
func minTime(skill []int, mana []int) int64 {
    n := len(skill)
    // f[i] stores the time when wizard i becomes free
    f := make([]int64, n)

    for _, x := range mana {
        var prevFinish int64 = 0
        mul := int64(x)
        for i := 0; i < n; i++ {
            start := f[i]
            if prevFinish > start {
                start = prevFinish
            }
            finish := start + int64(skill[i])*mul
            f[i] = finish
            prevFinish = finish
        }
    }
    return f[n-1]
}
```

## Ruby

```ruby
def min_time(skill, mana)
  n = skill.length
  f = Array.new(n, 0)

  mana.each do |x|
    now = f[0]
    (1...n).each do |i|
      now = [now + skill[i - 1] * x, f[i]].max
    end
    f[n - 1] = now + skill[n - 1] * x

    (n - 2).downto(0) do |i|
      f[i] = f[i + 1] - skill[i + 1] * x
    end
  end

  f[-1]
end
```

## Scala

```scala
object Solution {
    def minTime(skill: Array[Int], mana: Array[Int]): Long = {
        val n = skill.length
        val f = new Array[Long](n) // earliest free time for each wizard
        var idx = 0
        while (idx < mana.length) {
            val x = mana(idx).toLong
            var now = f(0)
            var i = 1
            while (i < n) {
                val finishPrev = now + skill(i - 1).toLong * x
                if (finishPrev > f(i)) now = finishPrev else now = f(i)
                i += 1
            }
            f(n - 1) = now + skill(n - 1).toLong * x
            var j = n - 2
            while (j >= 0) {
                f(j) = f(j + 1) - skill(j + 1).toLong * x
                j -= 1
            }
            idx += 1
        }
        f(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_time(skill: Vec<i32>, mana: Vec<i32>) -> i64 {
        let n = skill.len();
        let mut f = vec![0i64; n];
        let skill_i64: Vec<i64> = skill.iter().map(|&v| v as i64).collect();

        for &m in mana.iter() {
            let x = m as i64;
            // forward pass to compute the finish time of the last wizard
            let mut now = f[0];
            for i in 1..n {
                now = std::cmp::max(now + skill_i64[i - 1] * x, f[i]);
            }
            f[n - 1] = now + skill_i64[n - 1] * x;
            // backward pass to align earlier wizards' free times
            for i in (0..n - 1).rev() {
                f[i] = f[i + 1] - skill_i64[i + 1] * x;
            }
        }

        f[n - 1]
    }
}
```

## Racket

```racket
(define/contract (min-time skill mana)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length skill))
         (f (make-vector n 0))
         (skill-vec (list->vector skill)))
    (for ([x (in-list mana)])
      (define now (vector-ref f 0))
      (for ([i (in-range 1 n)])
        (set! now
              (max (+ now (* (vector-ref skill-vec (- i 1)) x))
                   (vector-ref f i))))
      (define finish (+ now (* (vector-ref skill-vec (- n 1)) x)))
      (vector-set! f (- n 1) finish)
      (for ([i (in-range (- n 2) -1 -1)])
        (vector-set! f i
                     (- (vector-ref f (+ i 1))
                        (* (vector-ref skill-vec (+ i 1)) x)))))
    (vector-ref f (- n 1))))
```

## Erlang

```erlang
-spec min_time([integer()], [integer()]) -> integer().
min_time(Skill, Mana) ->
    SkillT = list_to_tuple(Skill),
    N = tuple_size(SkillT),
    ZeroList = lists:duplicate(N, 0),
    F0 = list_to_tuple(ZeroList),
    process(Mana, SkillT, N, F0).

process([], _SkillT, N, F) ->
    element(N, F);
process([X|Rest], SkillT, N, F) ->
    Now0 = element(1, F),
    Now = forward_pass(2, N, X, SkillT, F, Now0),
    LastFinish = Now + element(N, SkillT) * X,
    RevList = build_rev(N - 1, X, SkillT, LastFinish, []),
    NewFList = lists:reverse([LastFinish | RevList]),
    NewF = list_to_tuple(NewFList),
    process(Rest, SkillT, N, NewF).

forward_pass(I, N, _X, _SkillT, _F, Now) when I > N ->
    Now;
forward_pass(I, N, X, SkillT, F, Now) ->
    PrevSkill = element(I - 1, SkillT),
    Fi = element(I, F),
    NewNow = max(Now + PrevSkill * X, Fi),
    forward_pass(I + 1, N, X, SkillT, F, NewNow).

build_rev(0, _X, _SkillT, _Prev, Acc) ->
    Acc;
build_rev(I, X, SkillT, Prev, Acc) when I >= 1 ->
    SkillNext = element(I + 1, SkillT),
    Fi = Prev - SkillNext * X,
    build_rev(I - 1, X, SkillT, Fi, [Fi | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(skill :: [integer], mana :: [integer]) :: integer
  def min_time(skill, mana) do
    n = length(skill)

    skill_arr = :array.from_list(skill)
    # initialize free times array with zeros
    arr = :array.new(n, default: 0)

    final_arr =
      Enum.reduce(mana, arr, fn x, acc_arr ->
        {new_arr, _prev_finish} =
          Enum.reduce(0..(n - 1), {acc_arr, 0}, fn i, {a, prev_finish} ->
            free = :array.get(i, a)
            start = if free > prev_finish, do: free, else: prev_finish
            finish = start + (:array.get(i, skill_arr) * x)
            {:array.set(i, finish, a), finish}
          end)

        new_arr
      end)

    :array.get(n - 1, final_arr)
  end
end
```
