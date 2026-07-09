# 0825. Friends Of Appropriate Ages

## Cpp

```cpp
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        const int MAX_AGE = 120;
        vector<int> cnt(MAX_AGE + 1, 0);
        for (int a : ages) ++cnt[a];
        
        // prefix sums
        vector<int> pref(MAX_AGE + 1, 0);
        for (int i = 1; i <= MAX_AGE; ++i) {
            pref[i] = pref[i - 1] + cnt[i];
        }
        
        long long ans = 0;
        for (int age = 1; age <= MAX_AGE; ++age) {
            if (cnt[age] == 0) continue;
            int low = age / 2 + 7; // floor division
            if (low >= age) continue; // no valid recipients
            int total = pref[age] - pref[low]; // people with age in (low, age]
            // each person of this age can send to (total - 1) others (exclude self)
            ans += (long long)cnt[age] * (total - 1);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numFriendRequests(int[] ages) {
        int[] count = new int[121];
        for (int age : ages) {
            count[age]++;
        }
        int[] prefix = new int[121];
        for (int i = 1; i <= 120; i++) {
            prefix[i] = prefix[i - 1] + count[i];
        }
        long total = 0;
        for (int age = 15; age <= 120; age++) { // ages below 15 cannot send requests
            int cnt = count[age];
            if (cnt == 0) continue;
            int low = age / 2 + 8; // floor(0.5*age + 7) + 1 => age/2 + 7 + 1
            if (low > age) continue;
            int eligible = prefix[age] - prefix[low - 1];
            total += (long) cnt * (eligible - 1); // exclude self
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # Count frequency of each age (ages are in [1,120])
        max_age = 120
        cnt = [0] * (max_age + 1)
        for age in ages:
            cnt[age] += 1

        # Prefix sums to query number of people with age <= i quickly
        pref = [0] * (max_age + 2)
        for i in range(1, max_age + 1):
            pref[i] = pref[i - 1] + cnt[i]

        total_requests = 0
        # Ages below 15 cannot send any request because 0.5*age+7 >= age
        for a in range(15, max_age + 1):
            if cnt[a] == 0:
                continue
            lower = int(a * 0.5 + 7)
            # Number of people with acceptable ages: (lower, a]
            eligible = pref[a] - pref[lower]
            # Each person of age a can send to all eligible except themselves
            total_requests += cnt[a] * (eligible - 1)

        return total_requests
```

## Python3

```python
from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        freq = [0] * 121
        for age in ages:
            freq[age] += 1

        prefix = [0] * 121
        running = 0
        for i in range(121):
            running += freq[i]
            prefix[i] = running

        total_requests = 0
        for a in range(15, 121):
            cnt_a = freq[a]
            if cnt_a == 0:
                continue
            low = int(a * 0.5 + 7)
            min_age = low + 1
            if min_age > a:
                continue
            total_eligible = prefix[a] - (prefix[min_age - 1] if min_age > 0 else 0)
            total_requests += cnt_a * (total_eligible - 1)

        return total_requests
```

## C

```c
int numFriendRequests(int* ages, int agesSize) {
    int cnt[121] = {0};
    for (int i = 0; i < agesSize; ++i) {
        cnt[ages[i]]++;
    }
    int prefix[121];
    prefix[0] = cnt[0];
    for (int i = 1; i <= 120; ++i) {
        prefix[i] = prefix[i - 1] + cnt[i];
    }
    long long ans = 0;
    for (int a = 15; a <= 120; ++a) {
        if (cnt[a] == 0) continue;
        int low = a / 2 + 8; // floor(0.5*a + 7) + 1
        if (low > a) continue;
        int total = prefix[a] - (low > 0 ? prefix[low - 1] : 0);
        ans += (long long)cnt[a] * (total - 1);
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int NumFriendRequests(int[] ages) {
        int[] cnt = new int[121];
        foreach (int age in ages) cnt[age]++;

        int[] pref = new int[122];
        for (int i = 1; i <= 120; i++) pref[i] = pref[i - 1] + cnt[i];

        long total = 0;
        for (int a = 15; a <= 120; a++) {
            int c = cnt[a];
            if (c == 0) continue;
            int lower = a / 2 + 8; // minimum acceptable age
            if (lower > a) continue;
            int eligible = pref[a] - pref[lower - 1];
            total += (long)c * (eligible - 1);
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
var numFriendRequests = function(ages) {
    const freq = new Array(121).fill(0);
    for (const age of ages) freq[age]++;
    
    const prefix = new Array(121).fill(0);
    for (let i = 1; i <= 120; i++) {
        prefix[i] = prefix[i - 1] + freq[i];
    }
    
    let total = 0;
    for (let a = 1; a <= 120; a++) {
        const cntA = freq[a];
        if (!cntA) continue;
        const low = Math.floor(a / 2 + 7) + 1; // b > 0.5 * a + 7
        if (low > a) continue;
        const eligible = prefix[a] - prefix[low - 1]; // ages in [low, a]
        total += cntA * (eligible - 1); // exclude self
    }
    
    return total;
};
```

## Typescript

```typescript
function numFriendRequests(ages: number[]): number {
    const cnt = new Array(121).fill(0);
    for (const age of ages) {
        cnt[age]++;
    }
    let total = 0;
    for (let a = 1; a <= 120; a++) {
        if (cnt[a] === 0) continue;
        const minAge = Math.floor(a / 2 + 7) + 1;
        for (let b = minAge; b <= a; b++) {
            if (cnt[b] === 0) continue;
            if (a === b) {
                total += cnt[a] * (cnt[a] - 1);
            } else {
                total += cnt[a] * cnt[b];
            }
        }
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $ages
     * @return Integer
     */
    function numFriendRequests($ages) {
        $cnt = array_fill(0, 121, 0);
        foreach ($ages as $age) {
            $cnt[$age]++;
        }
        $ans = 0;
        for ($i = 15; $i <= 120; $i++) {
            if ($cnt[$i] == 0) continue;
            $lower = intdiv($i, 2) + 8; // age must be > 0.5 * i + 7
            for ($j = $lower; $j <= $i; $j++) {
                if ($cnt[$j] == 0) continue;
                $ans += $cnt[$i] * $cnt[$j];
            }
            $ans -= $cnt[$i]; // remove self requests
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        var count = [Int](repeating: 0, count: 121)
        for age in ages {
            count[age] += 1
        }
        var prefix = [Int](repeating: 0, count: 122)
        for i in 1...120 {
            prefix[i] = prefix[i - 1] + count[i]
        }
        var total = 0
        for a in 15...120 {
            let cnt = count[a]
            if cnt == 0 { continue }
            let lower = a / 2 + 7
            if lower >= a { continue }
            let valid = prefix[a] - prefix[lower]
            total += cnt * (valid - 1)
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numFriendRequests(ages: IntArray): Int {
        val cnt = IntArray(121)
        for (age in ages) {
            cnt[age]++
        }
        val prefix = IntArray(122)
        for (i in 1..120) {
            prefix[i] = prefix[i - 1] + cnt[i]
        }
        var total = 0L
        for (a in 15..120) {
            val countA = cnt[a]
            if (countA == 0) continue
            val low = a / 2 + 7
            if (low >= a) continue
            val eligible = prefix[a] - prefix[low] // includes people of age a
            total += countA.toLong() * (eligible - 1)
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numFriendRequests(List<int> ages) {
    List<int> freq = List.filled(121, 0);
    for (var age in ages) {
      freq[age]++;
    }
    int total = 0;
    for (int a = 15; a <= 120; ++a) {
      int cntA = freq[a];
      if (cntA == 0) continue;
      // Requests to same age
      total += cntA * (cntA - 1);
      int lower = a ~/ 2 + 7;
      for (int b = 15; b < a; ++b) {
        if (b <= lower) continue;
        int cntB = freq[b];
        if (cntB == 0) continue;
        total += cntA * cntB;
      }
    }
    return total;
  }
}
```

## Golang

```go
import "sort"

func numFriendRequests(ages []int) int {
    // Count frequency of each age
    freq := make([]int, 121)
    for _, a := range ages {
        freq[a]++
    }

    // Prefix sums to query counts in ranges quickly
    prefix := make([]int, 121)
    for i := 1; i < 121; i++ {
        prefix[i] = prefix[i-1] + freq[i]
    }

    ans := 0
    for a := 15; a <= 120; a++ { // ages below 15 cannot send requests
        if freq[a] == 0 {
            continue
        }
        low := a/2 + 7 // floor of 0.5*a + 7
        totalInRange := prefix[a] - prefix[low] // people with age > low and <= a
        // each person of age a can send to (totalInRange-1) others (exclude self)
        ans += freq[a] * (totalInRange - 1)
    }
    return ans
}
```

## Ruby

```ruby
def num_friend_requests(ages)
  cnt = Array.new(121, 0)
  ages.each { |age| cnt[age] += 1 }

  prefix = Array.new(122, 0)
  (1..120).each do |i|
    prefix[i] = prefix[i - 1] + cnt[i]
  end

  total = 0
  (15..120).each do |a|
    next if cnt[a].zero?

    low = (a / 2) + 8
    next if low > a

    in_range = prefix[a] - prefix[low - 1]
    total += cnt[a] * (in_range - 1)
  end

  total
end
```

## Scala

```scala
object Solution {
    def numFriendRequests(ages: Array[Int]): Int = {
        val maxAge = 120
        val freq = new Array[Int](maxAge + 1)
        for (age <- ages) {
            freq(age) += 1
        }
        val prefix = new Array[Int](maxAge + 1)
        var sum = 0
        var i = 0
        while (i <= maxAge) {
            sum += freq(i)
            prefix(i) = sum
            i += 1
        }
        var total: Long = 0L
        var a = 15
        while (a <= maxAge) {
            val cnt = freq(a)
            if (cnt > 0) {
                val low = a / 2 + 8
                if (low <= a) {
                    val eligible = prefix(a) - (if (low > 0) prefix(low - 1) else 0)
                    total += cnt.toLong * (eligible - 1).toLong
                }
            }
            a += 1
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_friend_requests(ages: Vec<i32>) -> i32 {
        const MAX_AGE: usize = 120;
        let mut cnt = vec![0i64; MAX_AGE + 1];
        for &age in ages.iter() {
            cnt[age as usize] += 1;
        }

        // prefix sums of counts
        let mut pref = vec![0i64; MAX_AGE + 1];
        pref[0] = cnt[0];
        for i in 1..=MAX_AGE {
            pref[i] = pref[i - 1] + cnt[i];
        }

        let mut total: i64 = 0;
        for a in 15..=MAX_AGE as i32 {
            let c = cnt[a as usize];
            if c == 0 {
                continue;
            }
            let lower = (a / 2) + 7; // ages <= lower are not allowed
            if lower >= a {
                continue;
            }
            let eligible = pref[a as usize] - pref[lower as usize];
            total += c * (eligible - 1); // exclude self
        }

        total as i32
    }
}
```

## Racket

```racket
(define/contract (num-friend-requests ages)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort ages <))
         (vec (list->vector sorted))
         (n (vector-length vec)))
    (define (lower-bound target)
      (let loop ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (val (vector-ref vec mid)))
              (if (< val target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    (let loop ((i 0) (total 0))
      (if (= i n)
          total
          (let* ((age (vector-ref vec i))
                 (min-age (+ (quotient (+ age 14) 2) 1))
                 (lb (lower-bound min-age)))
            (if (< lb i)
                (loop (+ i 1) (+ total (- i lb))) ; requests from this person
                (loop (+ i 1) total)))))))
```

## Erlang

```erlang
-spec num_friend_requests([integer()]) -> integer().
num_friend_requests(Ages) ->
    Freq = lists:foldl(
        fun(A, Acc) ->
            maps:update_with(A,
                             fun(V) -> V + 1 end,
                             1,
                             Acc)
        end,
        #{},
        Ages),
    Total = lists:foldl(
        fun(Age, Sum) ->
            CountA = maps:get(Age, Freq, 0),
            if
                CountA == 0 ->
                    Sum;
                true ->
                    MinAge = trunc(0.5 * Age + 7) + 1,
                    Recipients = sum_range(MinAge, Age, Freq),
                    if
                        Recipients > 0 ->
                            Sum + CountA * (Recipients - 1);
                        true ->
                            Sum
                    end
            end
        end,
        0,
        lists:seq(1, 120)),
    Total.

-spec sum_range(integer(), integer(), map()) -> integer().
sum_range(Min, Max, _Freq) when Min > Max ->
    0;
sum_range(Min, Max, Freq) ->
    lists:foldl(
        fun(A, Acc) ->
            Acc + maps:get(A, Freq, 0)
        end,
        0,
        lists:seq(Min, Max)).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_friend_requests(ages :: [integer]) :: integer
  def num_friend_requests(ages) do
    freq =
      Enum.reduce(ages, %{}, fn age, acc ->
        Map.update(acc, age, 1, &(&1 + 1))
      end)

    total =
      Enum.reduce(15..120, 0, fn a, acc ->
        cnt_a = Map.get(freq, a, 0)

        if cnt_a == 0 do
          acc
        else
          lower = div(a, 2) + 7 + 1

          inner =
            Enum.reduce(lower..a, 0, fn b, inner_acc ->
              cnt_b = Map.get(freq, b, 0)

              if cnt_b == 0 do
                inner_acc
              else
                inner_acc + cnt_a * cnt_b
              end
            end)

          acc + inner
        end
      end)

    self_subtract =
      Enum.reduce(15..120, 0, fn a, sub ->
        sub + Map.get(freq, a, 0)
      end)

    total - self_subtract
  end
end
```
