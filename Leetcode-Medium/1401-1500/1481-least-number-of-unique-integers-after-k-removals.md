# 1481. Least Number of Unique Integers after K Removals

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        unordered_map<int,int> cnt;
        for (int x : arr) ++cnt[x];
        vector<int> freqs;
        freqs.reserve(cnt.size());
        for (auto &p : cnt) freqs.push_back(p.second);
        sort(freqs.begin(), freqs.end());
        int i = 0;
        while (i < (int)freqs.size() && k >= freqs[i]) {
            k -= freqs[i];
            ++i;
        }
        return freqs.size() - i;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : arr) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        int[] frequencies = new int[freqMap.size()];
        int idx = 0;
        for (int count : freqMap.values()) {
            frequencies[idx++] = count;
        }
        Arrays.sort(frequencies);

        int i = 0;
        while (i < frequencies.length && k >= frequencies[i]) {
            k -= frequencies[i];
            i++;
        }
        return frequencies.length - i;
    }
}
```

## Python

```python
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        counts = sorted(Counter(arr).values())
        i = 0
        n = len(counts)
        while i < n and k >= counts[i]:
            k -= counts[i]
            i += 1
        return n - i
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        counts = sorted(freq.values())
        i = 0
        while i < len(counts) and k >= counts[i]:
            k -= counts[i]
            i += 1
        return len(counts) - i
```

## C

```c
#include <stdlib.h>

static int int_cmp(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int findLeastNumOfUniqueInts(int* arr, int arrSize, int k) {
    if (arrSize == 0) return 0;
    if (k >= arrSize) return 0;

    qsort(arr, (size_t)arrSize, sizeof(int), int_cmp);

    int *freq = (int *)malloc((size_t)arrSize * sizeof(int));
    int uniqCount = 0;
    int i = 0;
    while (i < arrSize) {
        int val = arr[i];
        int cnt = 0;
        while (i < arrSize && arr[i] == val) {
            ++cnt;
            ++i;
        }
        freq[uniqCount++] = cnt;
    }

    qsort(freq, (size_t)uniqCount, sizeof(int), int_cmp);

    int idx = 0;
    while (idx < uniqCount && k >= freq[idx]) {
        k -= freq[idx];
        ++idx;
    }

    free(freq);
    return uniqCount - idx;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLeastNumOfUniqueInts(int[] arr, int k) {
        var freq = new System.Collections.Generic.Dictionary<int, int>();
        foreach (var num in arr) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        var counts = new System.Collections.Generic.List<int>(freq.Values);
        counts.Sort();

        int remainingUnique = counts.Count;
        foreach (int cnt in counts) {
            if (k >= cnt) {
                k -= cnt;
                remainingUnique--;
            } else {
                break;
            }
        }

        return remainingUnique;
    }
}
```

## Javascript

```javascript
var findLeastNumOfUniqueInts = function(arr, k) {
    const freqMap = new Map();
    for (const num of arr) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    const frequencies = Array.from(freqMap.values());
    frequencies.sort((a, b) => a - b);
    let removedUnique = 0;
    while (removedUnique < frequencies.length && k >= frequencies[removedUnique]) {
        k -= frequencies[removedUnique];
        removedUnique++;
    }
    return frequencies.length - removedUnique;
};
```

## Typescript

```typescript
function findLeastNumOfUniqueInts(arr: number[], k: number): number {
    const freq = new Map<number, number>();
    for (const num of arr) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    const counts = Array.from(freq.values()).sort((a, b) => a - b);
    let remaining = counts.length;
    for (const c of counts) {
        if (k >= c) {
            k -= c;
            remaining--;
        } else {
            break;
        }
    }
    return remaining;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findLeastNumOfUniqueInts($arr, $k) {
        $freq = [];
        foreach ($arr as $v) {
            if (!isset($freq[$v])) {
                $freq[$v] = 0;
            }
            $freq[$v]++;
        }

        $counts = array_values($freq);
        sort($counts); // ascending order

        $removedUnique = 0;
        foreach ($counts as $c) {
            if ($k >= $c) {
                $k -= $c;
                $removedUnique++;
            } else {
                break;
            }
        }

        return count($counts) - $removedUnique;
    }
}
```

## Swift

```swift
class Solution {
    func findLeastNumOfUniqueInts(_ arr: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        for num in arr {
            freq[num, default: 0] += 1
        }
        var frequencies = Array(freq.values)
        frequencies.sort()
        var remainingK = k
        var removedUnique = 0
        for f in frequencies {
            if remainingK >= f {
                remainingK -= f
                removedUnique += 1
            } else {
                break
            }
        }
        return frequencies.count - removedUnique
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLeastNumOfUniqueInts(arr: IntArray, k: Int): Int {
        val freq = HashMap<Int, Int>()
        for (num in arr) {
            freq[num] = (freq[num] ?: 0) + 1
        }
        val counts = freq.values.toIntArray()
        java.util.Arrays.sort(counts)
        var remaining = k
        var removed = 0
        for (c in counts) {
            if (remaining >= c) {
                remaining -= c
                removed++
            } else break
        }
        return freq.size - removed
    }
}
```

## Golang

```go
import "sort"

func findLeastNumOfUniqueInts(arr []int, k int) int {
    freq := make(map[int]int)
    for _, v := range arr {
        freq[v]++
    }
    freqs := make([]int, 0, len(freq))
    for _, cnt := range freq {
        freqs = append(freqs, cnt)
    }
    sort.Ints(freqs)

    i := 0
    for i < len(freqs) && k >= freqs[i] {
        k -= freqs[i]
        i++
    }
    return len(freqs) - i
}
```

## Ruby

```ruby
def find_least_num_of_unique_ints(arr, k)
  freq = Hash.new(0)
  arr.each { |num| freq[num] += 1 }
  counts = freq.values.sort
  i = 0
  while i < counts.size && k >= counts[i]
    k -= counts[i]
    i += 1
  end
  counts.size - i
end
```

## Scala

```scala
object Solution {
    def findLeastNumOfUniqueInts(arr: Array[Int], k: Int): Int = {
        import scala.collection.mutable

        val freq = mutable.HashMap[Int, Int]()
        arr.foreach { x =>
            freq.put(x, freq.getOrElse(x, 0) + 1)
        }

        val frequencies = freq.values.toArray.sorted
        var remainingK = k
        var idx = 0
        while (idx < frequencies.length && remainingK >= frequencies(idx)) {
            remainingK -= frequencies(idx)
            idx += 1
        }
        frequencies.length - idx
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for num in arr {
            *freq.entry(num).or_insert(0) += 1;
        }
        let mut counts: Vec<i32> = freq.values().cloned().collect();
        counts.sort_unstable();

        let mut remaining = counts.len() as i32;
        let mut k_left = k;
        for cnt in counts {
            if k_left >= cnt {
                k_left -= cnt;
                remaining -= 1;
            } else {
                break;
            }
        }
        remaining
    }
}
```
