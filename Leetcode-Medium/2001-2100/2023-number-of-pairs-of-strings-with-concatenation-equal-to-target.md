# 2023. Number of Pairs of Strings With Concatenation Equal to Target

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        unordered_map<string,int> freq;
        for (const auto& s : nums) ++freq[s];
        long long ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            const string& s = nums[i];
            if (target.size() >= s.size() && target.compare(0, s.size(), s) == 0) {
                string need = target.substr(s.size());
                auto it = freq.find(need);
                if (it != freq.end()) {
                    ans += it->second;
                    if (need == s) --ans; // exclude i == j
                }
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int numOfPairs(String[] nums, String target) {
        java.util.Map<String, Integer> freq = new java.util.HashMap<>();
        for (String s : nums) {
            freq.put(s, freq.getOrDefault(s, 0) + 1);
        }
        long ans = 0;
        int tLen = target.length();
        for (int i = 1; i < tLen; i++) { // split point
            String left = target.substring(0, i);
            String right = target.substring(i);
            Integer cntLeft = freq.get(left);
            Integer cntRight = freq.get(right);
            if (cntLeft == null || cntRight == null) continue;
            if (!left.equals(right)) {
                ans += (long) cntLeft * cntRight;
            } else {
                ans += (long) cntLeft * (cntLeft - 1);
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(nums)
        ans = 0
        for s in nums:
            if target.startswith(s):
                need = target[len(s):]
                ans += cnt.get(need, 0)
                if need == s:
                    ans -= 1
        return ans
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = Counter(nums)
        ans = 0
        for s, c in cnt.items():
            if target.startswith(s):
                suffix = target[len(s):]
                if suffix in cnt:
                    ans += c * cnt[suffix]
                    if s == suffix:
                        ans -= c
        return ans
```

## C

```c
#include <string.h>

int numOfPairs(char** nums, int numsSize, char* target) {
    int count = 0;
    int tlen = strlen(target);
    for (int i = 0; i < numsSize; ++i) {
        int li = strlen(nums[i]);
        if (li >= tlen) continue;
        for (int j = 0; j < numsSize; ++j) {
            if (i == j) continue;
            int lj = strlen(nums[j]);
            if (li + lj != tlen) continue;
            if (strncmp(target, nums[i], li) == 0 && strcmp(target + li, nums[j]) == 0) {
                ++count;
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        var freq = new Dictionary<string, int>();
        foreach (var s in nums) {
            if (freq.ContainsKey(s)) freq[s]++; else freq[s] = 1;
        }
        long ans = 0;
        foreach (var s in nums) {
            if (s.Length > target.Length) continue;
            if (!target.StartsWith(s)) continue;
            string suffix = target.Substring(s.Length);
            if (freq.TryGetValue(suffix, out int cnt)) {
                if (suffix == s) cnt--; // exclude same index
                ans += cnt;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function(nums, target) {
    const freq = new Map();
    for (const s of nums) {
        freq.set(s, (freq.get(s) || 0) + 1);
    }
    let ans = 0;
    for (const a of nums) {
        if (target.startsWith(a)) {
            const b = target.slice(a.length);
            const cnt = freq.get(b) || 0;
            if (cnt > 0) {
                ans += cnt - (a === b ? 1 : 0);
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numOfPairs(nums: string[], target: string): number {
    const freq = new Map<string, number>();
    for (const s of nums) {
        freq.set(s, (freq.get(s) ?? 0) + 1);
    }
    let ans = 0;
    for (const s of nums) {
        if (target.startsWith(s)) {
            const suffix = target.substring(s.length);
            const cnt = freq.get(suffix) ?? 0;
            ans += cnt;
            if (suffix === s) {
                ans -= 1; // exclude pairing with itself
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $nums
     * @param String $target
     * @return Integer
     */
    function numOfPairs($nums, $target) {
        $freq = [];
        foreach ($nums as $s) {
            if (!isset($freq[$s])) {
                $freq[$s] = 0;
            }
            $freq[$s]++;
        }

        $len = strlen($target);
        $ans = 0;

        for ($k = 1; $k < $len; $k++) {
            $pre = substr($target, 0, $k);
            $suf = substr($target, $k);
            if (isset($freq[$pre]) && isset($freq[$suf])) {
                if ($pre === $suf) {
                    $cnt = $freq[$pre];
                    $ans += $cnt * ($cnt - 1);
                } else {
                    $ans += $freq[$pre] * $freq[$suf];
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
    func numOfPairs(_ nums: [String], _ target: String) -> Int {
        var freq = [String: Int]()
        for s in nums {
            freq[s, default: 0] += 1
        }
        var ans = 0
        for s in nums {
            if target.hasPrefix(s) {
                let startIdx = target.index(target.startIndex, offsetBy: s.count)
                let suffix = String(target[startIdx...])
                if let cnt = freq[suffix] {
                    var add = cnt
                    if suffix == s {
                        add -= 1
                    }
                    ans += add
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfPairs(nums: Array<String>, target: String): Int {
        val freq = HashMap<String, Int>()
        for (s in nums) {
            freq[s] = (freq[s] ?: 0) + 1
        }
        var ans = 0L
        for (a in nums) {
            if (target.startsWith(a)) {
                val b = target.substring(a.length)
                val cnt = freq[b] ?: 0
                var add = cnt
                if (b == a) add -= 1
                ans += add
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numOfPairs(List<String> nums, String target) {
    final Map<String, int> freq = {};
    for (var s in nums) {
      freq[s] = (freq[s] ?? 0) + 1;
    }

    int ans = 0;
    for (var s in nums) {
      if (target.length >= s.length && target.startsWith(s)) {
        final String suffix = target.substring(s.length);
        int count = freq[suffix] ?? 0;
        if (suffix == s) {
          count -= 1; // exclude the same index
        }
        ans += count;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numOfPairs(nums []string, target string) int {
    count := 0
    for i := 0; i < len(nums); i++ {
        for j := 0; j < len(nums); j++ {
            if i == j {
                continue
            }
            if nums[i]+nums[j] == target {
                count++
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def num_of_pairs(nums, target)
  freq = Hash.new(0)
  nums.each { |s| freq[s] += 1 }
  ans = 0
  nums.each do |s|
    next unless target.start_with?(s)
    suffix = target[s.length..-1]
    cnt = freq[suffix]
    cnt -= 1 if suffix == s
    ans += cnt
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numOfPairs(nums: Array[String], target: String): Int = {
        val cnt = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (s <- nums) {
            cnt(s) = cnt(s) + 1
        }
        var ans: Long = 0L
        val n = target.length
        for (k <- 1 until n) {
            val left = target.substring(0, k)
            val right = target.substring(k)
            if (cnt.contains(left) && cnt.contains(right)) {
                if (left == right) {
                    val c = cnt(left).toLong
                    ans += c * (c - 1)
                } else {
                    ans += cnt(left).toLong * cnt(right)
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
    pub fn num_of_pairs(nums: Vec<String>, target: String) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<String, i32> = HashMap::new();
        for s in &nums {
            *freq.entry(s.clone()).or_insert(0) += 1;
        }
        let t = target.as_str();
        let mut ans: i32 = 0;
        for k in 1..t.len() {
            let prefix = &t[0..k];
            let suffix = &t[k..];
            let cnt_pre = *freq.get(prefix).unwrap_or(&0);
            if cnt_pre == 0 {
                continue;
            }
            let cnt_suf = *freq.get(suffix).unwrap_or(&0);
            if cnt_suf == 0 {
                continue;
            }
            if prefix == suffix {
                ans += cnt_pre * (cnt_pre - 1);
            } else {
                ans += cnt_pre * cnt_suf;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (num-of-pairs nums target)
  (-> (listof string?) string? exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (let loop ((i 0) (cnt 0))
      (if (= i n)
          cnt
          (let inner ((j 0) (c cnt))
            (if (= j n)
                (loop (+ i 1) c)
                (if (= i j)
                    (inner (+ j 1) c)
                    (if (string=? (string-append (vector-ref vec i) (vector-ref vec j)) target)
                        (inner (+ j 1) (+ c 1))
                        (inner (+ j 1) c)))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_of_pairs/2]).

-spec num_of_pairs(Nums :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
num_of_pairs(Nums, Target) ->
    Freq = build_freq(Nums, #{}),
    count_pairs(Nums, Target, Freq, 0).

build_freq([], M) -> M;
build_freq([H|T], M) ->
    Cnt = maps:get(H, M, 0),
    build_freq(T, maps:put(H, Cnt + 1, M)).

count_pairs([], _, _, Acc) -> Acc;
count_pairs([S|Rest], Target, Freq, Acc) ->
    case string:prefix(Target, S) of
        true ->
            LenS = byte_size(S),
            LenT = byte_size(Target),
            if LenS < LenT ->
                    Suffix = binary:part(Target, {LenS, LenT - LenS}),
                    Cnt = maps:get(Suffix, Freq, 0),
                    Add = case Suffix == S of
                              true -> Cnt - 1;
                              false -> Cnt
                          end,
                    count_pairs(Rest, Target, Freq, Acc + Add);
               true ->
                    count_pairs(Rest, Target, Freq, Acc)
            end;
        false ->
            count_pairs(Rest, Target, Freq, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_of_pairs(nums :: [String.t()], target :: String.t()) :: integer()
  def num_of_pairs(nums, target) do
    freq =
      Enum.reduce(nums, %{}, fn s, acc ->
        Map.update(acc, s, 1, &(&1 + 1))
      end)

    len_target = String.length(target)

    Enum.reduce(nums, 0, fn s, acc ->
      if String.starts_with?(target, s) do
        rest_len = len_target - String.length(s)

        rest =
          if rest_len == 0 do
            ""
          else
            String.slice(target, String.length(s), rest_len)
          end

        cnt = Map.get(freq, rest, 0)

        cnt =
          if rest == s do
            cnt - 1
          else
            cnt
          end

        acc + cnt
      else
        acc
      end
    end)
  end
end
```
