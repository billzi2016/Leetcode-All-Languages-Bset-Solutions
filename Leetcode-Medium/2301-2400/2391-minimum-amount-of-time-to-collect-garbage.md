# 2391. Minimum Amount of Time to Collect Garbage

## Cpp

```cpp
class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int n = garbage.size();
        long long totalTime = 0;
        // Count all garbage units
        for (const string& s : garbage) totalTime += s.size();

        // Find last occurrence index for each type
        int lastM = -1, lastP = -1, lastG = -1;
        for (int i = 0; i < n; ++i) {
            for (char c : garbage[i]) {
                if (c == 'M') lastM = i;
                else if (c == 'P') lastP = i;
                else if (c == 'G') lastG = i;
            }
        }

        // Prefix sums of travel times
        vector<long long> pref(n, 0);
        for (int i = 1; i < n; ++i) {
            pref[i] = pref[i - 1] + travel[i - 1];
        }

        if (lastM != -1) totalTime += pref[lastM];
        if (lastP != -1) totalTime += pref[lastP];
        if (lastG != -1) totalTime += pref[lastG];

        return static_cast<int>(totalTime);
    }
};
```

## Java

```java
class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        int n = garbage.length;
        int[] prefix = new int[n];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + travel[i - 1];
        }
        long total = 0;
        int lastM = -1, lastP = -1, lastG = -1;
        for (int i = 0; i < n; i++) {
            String s = garbage[i];
            total += s.length();
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                if (c == 'M') lastM = i;
                else if (c == 'P') lastP = i;
                else if (c == 'G') lastG = i;
            }
        }
        long ans = total;
        if (lastM != -1) ans += prefix[lastM];
        if (lastP != -1) ans += prefix[lastP];
        if (lastG != -1) ans += prefix[lastG];
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        n = len(garbage)
        # cumulative travel time to reach each house from house 0
        cum = [0] * n
        for i in range(1, n):
            cum[i] = cum[i - 1] + travel[i - 1]

        last_pos = {'M': -1, 'P': -1, 'G': -1}
        total_time = 0

        for idx, g in enumerate(garbage):
            total_time += len(g)
            if 'M' in g:
                last_pos['M'] = idx
            if 'P' in g:
                last_pos['P'] = idx
            if 'G' in g:
                last_pos['G'] = idx

        for typ in ('M', 'P', 'G'):
            pos = last_pos[typ]
            if pos != -1:
                total_time += cum[pos]

        return total_time
```

## Python3

```python
from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        # cumulative travel time to reach each house from house 0
        cum = [0] * n
        for i in range(1, n):
            cum[i] = cum[i - 1] + travel[i - 1]

        total_garbage = 0
        lastM = lastP = lastG = -1

        for idx, g in enumerate(garbage):
            total_garbage += len(g)
            if 'M' in g:
                lastM = idx
            if 'P' in g:
                lastP = idx
            if 'G' in g:
                lastG = idx

        ans = total_garbage
        if lastM != -1:
            ans += cum[lastM]
        if lastP != -1:
            ans += cum[lastP]
        if lastG != -1:
            ans += cum[lastG]

        return ans
```

## C

```c
#include <stddef.h>

int garbageCollection(char** garbage, int garbageSize, int* travel, int travelSize) {
    long long ans = 0;
    int lastM = -1, lastP = -1, lastG = -1;

    for (int i = 0; i < garbageSize; ++i) {
        char *s = garbage[i];
        for (int j = 0; s[j] != '\0'; ++j) {
            ++ans;
            if (s[j] == 'M') lastM = i;
            else if (s[j] == 'P') lastP = i;
            else if (s[j] == 'G') lastG = i;
        }
    }

    for (int i = 0; i < travelSize; ++i) {
        if (i < lastM) ans += travel[i];
        if (i < lastP) ans += travel[i];
        if (i < lastG) ans += travel[i];
    }

    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int GarbageCollection(string[] garbage, int[] travel)
    {
        int n = garbage.Length;
        long[] prefix = new long[n];
        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i - 1] + travel[i - 1];
        }

        int lastM = -1, lastP = -1, lastG = -1;
        long totalPickTime = 0;

        for (int i = 0; i < n; i++)
        {
            string s = garbage[i];
            totalPickTime += s.Length;
            foreach (char c in s)
            {
                if (c == 'M') lastM = i;
                else if (c == 'P') lastP = i;
                else if (c == 'G') lastG = i;
            }
        }

        long ans = totalPickTime;
        if (lastM != -1) ans += prefix[lastM];
        if (lastP != -1) ans += prefix[lastP];
        if (lastG != -1) ans += prefix[lastG];

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
var garbageCollection = function(garbage, travel) {
    const n = garbage.length;
    // prefix[i] = total travel time to reach house i from house 0
    const prefix = new Array(n).fill(0);
    for (let i = 1; i < n; ++i) {
        prefix[i] = prefix[i - 1] + travel[i - 1];
    }

    let totalGarbageTime = 0;
    const lastPos = { 'M': -1, 'P': -1, 'G': -1 };

    for (let i = 0; i < n; ++i) {
        const s = garbage[i];
        totalGarbageTime += s.length;

        if (s.includes('M')) lastPos['M'] = i;
        if (s.includes('P')) lastPos['P'] = i;
        if (s.includes('G')) lastPos['G'] = i;
    }

    let ans = totalGarbageTime;
    if (lastPos['M'] !== -1) ans += prefix[lastPos['M']];
    if (lastPos['P'] !== -1) ans += prefix[lastPos['P']];
    if (lastPos['G'] !== -1) ans += prefix[lastPos['G']];

    return ans;
};
```

## Typescript

```typescript
function garbageCollection(garbage: string[], travel: number[]): number {
    const n = garbage.length;
    let totalTime = 0;
    let lastM = -1, lastP = -1, lastG = -1;

    for (let i = 0; i < n; ++i) {
        const s = garbage[i];
        totalTime += s.length;
        for (const ch of s) {
            if (ch === 'M') lastM = i;
            else if (ch === 'P') lastP = i;
            else if (ch === 'G') lastG = i;
        }
    }

    // prefix sum of travel: pref[i] = sum_{k=0}^{i-1} travel[k]
    const pref: number[] = new Array(n).fill(0);
    for (let i = 1; i < n; ++i) {
        pref[i] = pref[i - 1] + travel[i - 1];
    }

    if (lastM > 0) totalTime += pref[lastM];
    else if (lastM === 0) totalTime += 0;

    if (lastP > 0) totalTime += pref[lastP];
    else if (lastP === 0) totalTime += 0;

    if (lastG > 0) totalTime += pref[lastG];
    else if (lastG === 0) totalTime += 0;

    return totalTime;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $garbage
     * @param Integer[] $travel
     * @return Integer
     */
    function garbageCollection($garbage, $travel) {
        $n = count($garbage);
        // prefix distances: distance from house 0 to i
        $prefix = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $prefix[$i] = $prefix[$i - 1] + $travel[$i - 1];
        }

        $last = ['M' => -1, 'P' => -1, 'G' => -1];
        $total = 0;

        for ($i = 0; $i < $n; $i++) {
            $s = $garbage[$i];
            $len = strlen($s);
            $total += $len;
            for ($j = 0; $j < $len; $j++) {
                $c = $s[$j];
                if (isset($last[$c])) {
                    $last[$c] = $i;
                }
            }
        }

        foreach (['M', 'P', 'G'] as $c) {
            if ($last[$c] != -1) {
                $total += $prefix[$last[$c]];
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func garbageCollection(_ garbage: [String], _ travel: [Int]) -> Int {
        let n = garbage.count
        var prefix = [Int](repeating: 0, count: n)
        for i in 1..<n {
            prefix[i] = prefix[i - 1] + travel[i - 1]
        }
        
        var lastM = -1, lastP = -1, lastG = -1
        var total = 0
        
        for (i, str) in garbage.enumerated() {
            for ch in str {
                total += 1
                switch ch {
                case "M":
                    lastM = i
                case "P":
                    lastP = i
                case "G":
                    lastG = i
                default:
                    break
                }
            }
        }
        
        var ans = total
        if lastM != -1 { ans += prefix[lastM] }
        if lastP != -1 { ans += prefix[lastP] }
        if lastG != -1 { ans += prefix[lastG] }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun garbageCollection(garbage: Array<String>, travel: IntArray): Int {
        var total = 0
        val last = IntArray(3) { -1 } // M, P, G

        for (i in garbage.indices) {
            val s = garbage[i]
            total += s.length
            for (ch in s) {
                when (ch) {
                    'M' -> last[0] = i
                    'P' -> last[1] = i
                    'G' -> last[2] = i
                }
            }
        }

        val n = garbage.size
        val pref = IntArray(n)
        for (i in 1 until n) {
            pref[i] = pref[i - 1] + travel[i - 1]
        }

        for (idx in last) {
            if (idx != -1) total += pref[idx]
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int garbageCollection(List<String> garbage, List<int> travel) {
    int n = garbage.length;
    int totalTime = 0;

    // last occurrence indices for 'M', 'P', 'G'
    List<int> lastPos = List.filled(3, -1); // 0:M, 1:P, 2:G

    for (int i = 0; i < n; ++i) {
      String s = garbage[i];
      totalTime += s.length;
      if (s.contains('M')) lastPos[0] = i;
      if (s.contains('P')) lastPos[1] = i;
      if (s.contains('G')) lastPos[2] = i;
    }

    // prefix sums of travel times
    List<int> pref = List.filled(n, 0);
    for (int i = 1; i < n; ++i) {
      pref[i] = pref[i - 1] + travel[i - 1];
    }

    for (int pos in lastPos) {
      if (pos > 0) totalTime += pref[pos];
    }

    return totalTime;
  }
}
```

## Golang

```go
package main

func garbageCollection(garbage []string, travel []int) int {
	n := len(garbage)
	prefix := make([]int, n)
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] + travel[i-1]
	}
	cntM, cntP, cntG := 0, 0, 0
	lastM, lastP, lastG := -1, -1, -1

	for i, s := range garbage {
		for _, ch := range s {
			switch ch {
			case 'M':
				cntM++
				lastM = i
			case 'P':
				cntP++
				lastP = i
			case 'G':
				cntG++
				lastG = i
			}
		}
	}

	ans := cntM + cntP + cntG
	if lastM != -1 {
		ans += prefix[lastM]
	}
	if lastP != -1 {
		ans += prefix[lastP]
	}
	if lastG != -1 {
		ans += prefix[lastG]
	}
	return ans
}
```

## Ruby

```ruby
def garbage_collection(garbage, travel)
  n = garbage.length
  # prefix[i] = total travel time from house 0 to i
  prefix = Array.new(n, 0)
  (1...n).each do |i|
    prefix[i] = prefix[i - 1] + travel[i - 1]
  end

  counts = { 'M' => 0, 'P' => 0, 'G' => 0 }
  last   = { 'M' => -1, 'P' => -1, 'G' => -1 }

  garbage.each_with_index do |s, idx|
    s.each_char do |ch|
      counts[ch] += 1
      last[ch] = idx
    end
  end

  ans = counts.values.sum
  ['M', 'P', 'G'].each do |ch|
    li = last[ch]
    ans += prefix[li] if li >= 0
  end

  ans
end
```

## Scala

```scala
object Solution {
    def garbageCollection(garbage: Array[String], travel: Array[Int]): Int = {
        val n = garbage.length
        // prefix[i] = total travel time to reach house i from house 0
        val prefix = new Array[Int](n)
        for (i <- 1 until n) {
            prefix(i) = prefix(i - 1) + travel(i - 1)
        }

        var totalGarbage = 0
        val lastPos = scala.collection.mutable.Map[Char, Int]()

        for (i <- 0 until n) {
            val s = garbage(i)
            totalGarbage += s.length
            for (ch <- s) {
                lastPos(ch) = i   // keep the latest index for each type
            }
        }

        var ans = totalGarbage
        for (t <- Seq('M', 'P', 'G')) {
            if (lastPos.contains(t)) {
                ans += prefix(lastPos(t))
            }
        }
        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn garbage_collection(garbage: Vec<String>, travel: Vec<i32>) -> i32 {
        let n = garbage.len();
        // cumulative travel time to reach each house from house 0
        let mut cum = vec![0i32; n];
        for i in 1..n {
            cum[i] = cum[i - 1] + travel[i - 1];
        }

        let mut total = 0i32;
        let mut last_m: Option<usize> = None;
        let mut last_p: Option<usize> = None;
        let mut last_g: Option<usize> = None;

        for (i, s) in garbage.iter().enumerate() {
            let bytes = s.as_bytes();
            total += bytes.len() as i32;
            if bytes.contains(&b'M') { last_m = Some(i); }
            if bytes.contains(&b'P') { last_p = Some(i); }
            if bytes.contains(&b'G') { last_g = Some(i); }
        }

        let mut ans = total;
        if let Some(idx) = last_m {
            ans += cum[idx];
        }
        if let Some(idx) = last_p {
            ans += cum[idx];
        }
        if let Some(idx) = last_g {
            ans += cum[idx];
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (garbage-collection garbage travel)
  (-> (listof string?) (listof exact-integer?) exact-integer?)
  (let* ((n (length garbage))
         (travel-vec (list->vector travel))
         (pref (make-vector n 0)))
    ;; prefix sums of travel times
    (for ([i (in-range 1 n)])
      (vector-set! pref i (+ (vector-ref pref (- i 1))
                             (vector-ref travel-vec (- i 1)))))
    (define total 0)
    (define lastM -1)
    (define lastP -1)
    (define lastG -1)
    ;; scan garbage strings
    (for ([i (in-range n)]
          [s garbage])
      (let ((len (string-length s)))
        (set! total (+ total len))
        (for ([j (in-range len)])
          (case (string-ref s j)
            [(#\M) (set! lastM i)]
            [(#\P) (set! lastP i)]
            [(#\G) (set! lastG i)]))))
    ;; add required travel times
    (let ((ans total))
      (when (>= lastM 0) (set! ans (+ ans (vector-ref pref lastM))))
      (when (>= lastP 0) (set! ans (+ ans (vector-ref pref lastP))))
      (when (>= lastG 0) (set! ans (+ ans (vector-ref pref lastG))))
      ans)))
```

## Erlang

```erlang
-spec garbage_collection(Garbage :: [unicode:unicode_binary()], Travel :: [integer()]) -> integer().
garbage_collection(Garbage, Travel) ->
    % Count total units and last house index for each type
    {CountM, CountP, CountG, LastM, LastP, LastG} =
        lists:foldl(
            fun({Str, Idx},
                {CM, CP, CG, LM, LP, LG}) ->
                CM1 = CM + count_char(Str, $M),
                CP1 = CP + count_char(Str, $P),
                CG1 = CG + count_char(Str, $G),

                LM1 = case count_char(Str, $M) of
                          0 -> LM;
                          _ -> Idx
                      end,
                LP1 = case count_char(Str, $P) of
                          0 -> LP;
                          _ -> Idx
                      end,
                LG1 = case count_char(Str, $G) of
                          0 -> LG;
                          _ -> Idx
                      end,
                {CM1, CP1, CG1, LM1, LP1, LG1}
            end,
            {0, 0, 0, -1, -1, -1},
            lists:zip(Garbage, lists:seq(0, length(Garbage) - 1))
        ),

    % Prefix sums of travel times: prefix[i] = sum_{j=0}^{i-1} Travel[j]
    {RevPref, _} =
        lists:foldl(
            fun(Val, {List, Sum}) ->
                NewSum = Sum + Val,
                {[NewSum | List], NewSum}
            end,
            {[], 0},
            Travel
        ),
    Prefix = lists:reverse([0 | RevPref]),

    TravelTime = fun(Index) when Index >= 0 ->
                         lists:nth(Index + 1, Prefix);
                     (_) -> 0
                 end,

    CountM + CountP + CountG +
    TravelTime(LastM) + TravelTime(LastP) + TravelTime(LastG).

% Helper: count occurrences of Char in binary Str
count_char(Bin, Char) ->
    count_char(binary_to_list(Bin), Char, 0).

count_char([], _, Acc) -> Acc;
count_char([H | T], Char, Acc) ->
    NewAcc = if H == Char -> Acc + 1; true -> Acc end,
    count_char(T, Char, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec garbage_collection([String.t()], [integer]) :: integer
  def garbage_collection(garbage, travel) do
    # Count each type and record the last house index where it appears
    {counts, lasts} =
      Enum.reduce(Enum.with_index(garbage), {%{"M" => 0, "P" => 0, "G" => 0},
                                            %{"M" => -1, "P" => -1, "G" => -1}}, fn {s, idx}, {cnt, lst} ->
        Enum.reduce(String.graphemes(s), {cnt, lst}, fn ch, {c_acc, l_acc} ->
          c_new = Map.update!(c_acc, ch, &(&1 + 1))
          l_new = Map.put(l_acc, ch, idx)
          {c_new, l_new}
        end)
      end)

    total_pickup = counts["M"] + counts["P"] + counts["G"]

    # Cumulative travel times: cum[i] = sum of travel[0..i-1], length == length(garbage)
    cum = build_cumulative(travel)

    extra_travel =
      Enum.reduce(["M", "P", "G"], 0, fn ch, acc ->
        pos = lasts[ch]
        if pos == -1 do
          acc
        else
          acc + Enum.at(cum, pos)
        end
      end)

    total_pickup + extra_travel
  end

  defp build_cumulative(travel) do
    {list_rev, _} =
      Enum.reduce(Enum.with_index(travel), {[0], 0}, fn {t, _i}, {list, sum} ->
        new_sum = sum + t
        {[new_sum | list], new_sum}
      end)

    Enum.reverse(list_rev)
  end
end
```
