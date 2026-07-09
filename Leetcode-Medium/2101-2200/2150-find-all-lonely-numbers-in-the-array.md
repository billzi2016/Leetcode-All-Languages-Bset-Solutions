# 2150. Find All Lonely Numbers in the Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findLonely(vector<int>& nums) {
        unordered_map<int,int> freq;
        freq.reserve(nums.size()*2);
        for (int x : nums) ++freq[x];
        vector<int> ans;
        ans.reserve(freq.size());
        for (const auto& kv : freq) {
            if (kv.second == 1 &&
                freq.find(kv.first - 1) == freq.end() &&
                freq.find(kv.first + 1) == freq.end()) {
                ans.push_back(kv.first);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findLonely(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : nums) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        Set<Integer> present = freq.keySet();
        List<Integer> result = new ArrayList<>();
        for (int v : nums) {
            if (freq.get(v) == 1 && !present.contains(v - 1) && !present.contains(v + 1)) {
                result.add(v);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        result = []
        present = set(freq.keys())
        for x, cnt in freq.items():
            if cnt == 1 and (x - 1) not in present and (x + 1) not in present:
                result.append(x)
        return result
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        present = set(cnt.keys())
        lonely = []
        for x, c in cnt.items():
            if c == 1 and (x - 1) not in present and (x + 1) not in present:
                lonely.append(x)
        return lonely
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findLonely(int* nums, int numsSize, int* returnSize) {
    const int MAX_VAL = 1000000;
    int *cnt = (int*)calloc(MAX_VAL + 2, sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        cnt[nums[i]]++;
    }
    
    int *res = (int*)malloc(numsSize * sizeof(int));
    int idx = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        if (cnt[x] == 1 &&
            (x == 0 || cnt[x - 1] == 0) &&
            (x == MAX_VAL || cnt[x + 1] == 0)) {
            res[idx++] = x;
        }
    }
    
    *returnSize = idx;
    free(cnt);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindLonely(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var x in nums) {
            if (freq.ContainsKey(x)) freq[x]++;
            else freq[x] = 1;
        }
        var present = new HashSet<int>(freq.Keys);
        var result = new List<int>();
        foreach (var kvp in freq) {
            int x = kvp.Key;
            if (kvp.Value == 1 && !present.Contains(x - 1) && !present.Contains(x + 1)) {
                result.Add(x);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
var findLonely = function(nums) {
    const freq = new Map();
    for (const x of nums) {
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    const result = [];
    for (const [x, count] of freq.entries()) {
        if (count === 1 && !freq.has(x - 1) && !freq.has(x + 1)) {
            result.push(x);
        }
    }
    return result;
};
```

## Typescript

```typescript
function findLonely(nums: number[]): number[] {
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }
    const result: number[] = [];
    for (const [val, count] of freq.entries()) {
        if (count === 1 && !freq.has(val - 1) && !freq.has(val + 1)) {
            result.push(val);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findLonely($nums) {
        $cnt = [];
        foreach ($nums as $v) {
            if (isset($cnt[$v])) {
                $cnt[$v]++;
            } else {
                $cnt[$v] = 1;
            }
        }

        $res = [];
        foreach ($cnt as $num => $c) {
            if ($c === 1 && !isset($cnt[$num - 1]) && !isset($cnt[$num + 1])) {
                $res[] = (int)$num;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func findLonely(_ nums: [Int]) -> [Int] {
        var freq = [Int:Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        var result = [Int]()
        for (num, count) in freq {
            if count == 1 && freq[num - 1] == nil && freq[num + 1] == nil {
                result.append(num)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLonely(nums: IntArray): List<Int> {
        val freq = HashMap<Int, Int>()
        for (v in nums) {
            freq[v] = (freq[v] ?: 0) + 1
        }
        val result = ArrayList<Int>()
        for ((num, count) in freq) {
            if (count == 1 && !freq.containsKey(num - 1) && !freq.containsKey(num + 1)) {
                result.add(num)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findLonely(List<int> nums) {
    final Map<int, int> freq = {};
    for (var v in nums) {
      freq[v] = (freq[v] ?? 0) + 1;
    }
    final List<int> result = [];
    for (var entry in freq.entries) {
      if (entry.value == 1 &&
          !freq.containsKey(entry.key - 1) &&
          !freq.containsKey(entry.key + 1)) {
        result.add(entry.key);
      }
    }
    return result;
  }
}
```

## Golang

```go
func findLonely(nums []int) []int {
	cnt := make(map[int]int)
	for _, v := range nums {
		cnt[v]++
	}
	res := []int{}
	for _, v := range nums {
		if cnt[v] == 1 && cnt[v-1] == 0 && cnt[v+1] == 0 {
			res = append(res, v)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_lonely(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  result = []
  freq.each do |num, cnt|
    next unless cnt == 1
    unless freq.key?(num - 1) || freq.key?(num + 1)
      result << num
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def findLonely(nums: Array[Int]): List[Int] = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    for (x <- nums) {
      freq.update(x, freq.getOrElse(x, 0) + 1)
    }
    val res = scala.collection.mutable.ListBuffer[Int]()
    for ((x, cnt) <- freq) {
      if (cnt == 1 && !freq.contains(x - 1) && !freq.contains(x + 1)) {
        res += x
      }
    }
    res.toList
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_lonely(nums: Vec<i32>) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for &v in nums.iter() {
            *freq.entry(v).or_insert(0) += 1;
        }
        let mut result = Vec::new();
        for (&x, &cnt) in freq.iter() {
            if cnt == 1 && !freq.contains_key(&(x - 1)) && !freq.contains_key(&(x + 1)) {
                result.push(x);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-lonely nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((freq (make-hash)))
    ;; count frequencies
    (for-each (lambda (x)
                (hash-set! freq x (+ 1 (hash-ref freq x 0))))
              nums)
    ;; collect lonely numbers
    (define result '())
    (for ([pair (in-hash freq)])
      (define x (car pair))
      (define cnt (cdr pair))
      (when (and (= cnt 1)
                 (zero? (hash-ref freq (- x 1) 0))
                 (zero? (hash-ref freq (+ x 1) 0)))
        (set! result (cons x result))))
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([find_lonely/1]).

-spec find_lonely(Nums :: [integer()]) -> [integer()].
find_lonely(Nums) ->
    CountMap = count_map(Nums, #{}),
    Keys = maps:keys(CountMap),
    [K || K <- Keys,
          1 =:= maps:get(K, CountMap),
          not maps:is_key(K-1, CountMap),
          not maps:is_key(K+1, CountMap)].

count_map([], Acc) -> Acc;
count_map([H|T], Acc) ->
    NewAcc = case maps:find(H, Acc) of
        {ok, C} -> maps:put(H, C + 1, Acc);
        error   -> maps:put(H, 1, Acc)
    end,
    count_map(T, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lonely(nums :: [integer]) :: [integer]
  def find_lonely(nums) do
    freq = Enum.frequencies(nums)

    freq
    |> Map.keys()
    |> Enum.filter(fn x ->
      freq[x] == 1 and not Map.has_key?(freq, x - 1) and not Map.has_key?(freq, x + 1)
    end)
  end
end
```
