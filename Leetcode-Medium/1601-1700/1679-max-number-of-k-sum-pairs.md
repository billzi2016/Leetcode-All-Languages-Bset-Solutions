# 1679. Max Number of K-Sum Pairs

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        int ans = 0;
        for (int x : nums) {
            int need = k - x;
            auto it = cnt.find(need);
            if (it != cnt.end() && it->second > 0) {
                ++ans;
                --it->second;
            } else {
                ++cnt[x];
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxOperations(int[] nums, int k) {
        java.util.HashMap<Integer, Integer> count = new java.util.HashMap<>();
        int operations = 0;
        for (int num : nums) {
            int need = k - num;
            Integer have = count.get(need);
            if (have != null && have > 0) {
                operations++;
                if (have == 1) {
                    count.remove(need);
                } else {
                    count.put(need, have - 1);
                }
            } else {
                count.put(num, count.getOrDefault(num, 0) + 1);
            }
        }
        return operations;
    }
}
```

## Python

```python
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {}
        ops = 0
        for num in nums:
            complement = k - num
            if counts.get(complement, 0) > 0:
                ops += 1
                counts[complement] -= 1
            else:
                counts[num] = counts.get(num, 0) + 1
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        ops = 0
        for num in nums:
            complement = k - num
            if freq.get(complement, 0):
                ops += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        return ops
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int maxOperations(int* nums, int numsSize, int k) {
    if (numsSize < 2) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    int left = 0, right = numsSize - 1, ops = 0;
    while (left < right) {
        long sum = (long)nums[left] + nums[right];
        if (sum == k) {
            ++ops;
            ++left;
            --right;
        } else if (sum < k) {
            ++left;
        } else {
            --right;
        }
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxOperations(int[] nums, int k) {
        var count = new Dictionary<int, int>();
        int operations = 0;
        foreach (int num in nums) {
            int complement = k - num;
            if (count.TryGetValue(complement, out int c) && c > 0) {
                operations++;
                if (c == 1)
                    count.Remove(complement);
                else
                    count[complement] = c - 1;
            } else {
                if (count.ContainsKey(num))
                    count[num]++;
                else
                    count[num] = 1;
            }
        }
        return operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    const freq = new Map();
    let ops = 0;
    for (const num of nums) {
        const need = k - num;
        const cntNeed = freq.get(need);
        if (cntNeed > 0) {
            ops++;
            freq.set(need, cntNeed - 1);
        } else {
            freq.set(num, (freq.get(num) || 0) + 1);
        }
    }
    return ops;
};
```

## Typescript

```typescript
function maxOperations(nums: number[], k: number): number {
    const count = new Map<number, number>();
    let operations = 0;
    for (const num of nums) {
        const complement = k - num;
        const compCount = count.get(complement);
        if (compCount !== undefined && compCount > 0) {
            operations++;
            count.set(complement, compCount - 1);
        } else {
            count.set(num, (count.get(num) ?? 0) + 1);
        }
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maxOperations($nums, $k) {
        $cnt = [];
        $ops = 0;
        foreach ($nums as $num) {
            $comp = $k - $num;
            if (isset($cnt[$comp]) && $cnt[$comp] > 0) {
                $cnt[$comp]--;
                $ops++;
            } else {
                if (!isset($cnt[$num])) {
                    $cnt[$num] = 0;
                }
                $cnt[$num]++;
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func maxOperations(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        var operations = 0
        for num in nums {
            let complement = k - num
            if let count = freq[complement], count > 0 {
                operations += 1
                freq[complement] = count - 1
            } else {
                freq[num, default: 0] += 1
            }
        }
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxOperations(nums: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        var operations = 0
        for (num in nums) {
            val need = k - num
            val cntNeed = freq[need] ?: 0
            if (cntNeed > 0) {
                operations++
                if (cntNeed == 1) {
                    freq.remove(need)
                } else {
                    freq[need] = cntNeed - 1
                }
            } else {
                freq[num] = (freq[num] ?: 0) + 1
            }
        }
        return operations
    }
}
```

## Golang

```go
func maxOperations(nums []int, k int) int {
    freq := make(map[int]int)
    ops := 0
    for _, v := range nums {
        need := k - v
        if cnt, ok := freq[need]; ok && cnt > 0 {
            ops++
            freq[need] = cnt - 1
        } else {
            freq[v]++
        }
    }
    return ops
}
```

## Ruby

```ruby
def max_operations(nums, k)
  freq = Hash.new(0)
  ops = 0
  nums.each do |num|
    need = k - num
    if freq[need] > 0
      ops += 1
      freq[need] -= 1
    else
      freq[num] += 1
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def maxOperations(nums: Array[Int], k: Int): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        var ops = 0
        for (num <- nums) {
            val need = k - num
            freq.get(need) match {
                case Some(cnt) if cnt > 0 =>
                    ops += 1
                    if (cnt == 1) freq -= need else freq.update(need, cnt - 1)
                case _ =>
                    freq.update(num, freq.getOrElse(num, 0) + 1)
            }
        }
        ops
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut ops = 0;
        for &num in nums.iter() {
            let need = k - num;
            if let Some(cnt) = freq.get_mut(&need) {
                if *cnt > 0 {
                    *cnt -= 1;
                    ops += 1;
                    continue;
                }
            }
            *freq.entry(num).or_insert(0) += 1;
        }
        ops
    }
}
```
