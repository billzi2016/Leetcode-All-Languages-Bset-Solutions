# 1238. Circular Permutation in Binary Representation

## Cpp

```cpp
class Solution {
public:
    vector<int> circularPermutation(int n, int start) {
        int total = 1 << n;
        vector<int> gray(total);
        for (int i = 0; i < total; ++i) {
            gray[i] = i ^ (i >> 1);
        }
        int pos = 0;
        while (pos < total && gray[pos] != start) ++pos;
        vector<int> ans;
        ans.reserve(total);
        for (int i = 0; i < total; ++i) {
            ans.push_back(gray[(pos + i) % total]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> circularPermutation(int n, int start) {
        int total = 1 << n;
        int[] gray = new int[total];
        for (int i = 0; i < total; i++) {
            gray[i] = i ^ (i >> 1);
        }
        int idx = 0;
        while (gray[idx] != start) {
            idx++;
        }
        List<Integer> result = new ArrayList<>(total);
        for (int i = 0; i < total; i++) {
            result.add(gray[(idx + i) % total]);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        total = 1 << n
        gray = [i ^ (i >> 1) for i in range(total)]
        idx = gray.index(start)
        return gray[idx:] + gray[:idx]
```

## Python3

```python
from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        m = 1 << n
        gray = [i ^ (i >> 1) for i in range(m)]
        idx = gray.index(start)
        return gray[idx:] + gray[:idx]
```

## C

```c
#include <stdlib.h>

int* circularPermutation(int n, int start, int* returnSize) {
    int size = 1 << n;
    int *gray = (int *)malloc(sizeof(int) * size);
    if (!gray) return NULL;

    for (int i = 0; i < size; ++i) {
        gray[i] = i ^ (i >> 1);
    }

    int idx = 0;
    while (idx < size && gray[idx] != start) {
        ++idx;
    }

    int *ans = (int *)malloc(sizeof(int) * size);
    if (!ans) {
        free(gray);
        return NULL;
    }

    for (int i = 0; i < size; ++i) {
        ans[i] = gray[(idx + i) % size];
    }

    free(gray);
    *returnSize = size;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> CircularPermutation(int n, int start) {
        int total = 1 << n;
        int[] gray = new int[total];
        for (int i = 0; i < total; i++) {
            gray[i] = i ^ (i >> 1);
        }
        int idx = System.Array.IndexOf(gray, start);
        var result = new List<int>(total);
        for (int i = 0; i < total; i++) {
            result.Add(gray[(idx + i) % total]);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} start
 * @return {number[]}
 */
var circularPermutation = function(n, start) {
    const total = 1 << n;
    const gray = new Array(total);
    for (let i = 0; i < total; i++) {
        gray[i] = i ^ (i >> 1);
    }
    let idx = 0;
    while (gray[idx] !== start) idx++;
    const result = new Array(total);
    for (let i = 0; i < total; i++) {
        result[i] = gray[(idx + i) % total];
    }
    return result;
};
```

## Typescript

```typescript
function circularPermutation(n: number, start: number): number[] {
    const total = 1 << n;
    const gray: number[] = new Array(total);
    for (let i = 0; i < total; i++) {
        gray[i] = i ^ (i >> 1);
    }
    let idx = 0;
    while (idx < total && gray[idx] !== start) idx++;
    const result: number[] = [];
    for (let i = 0; i < total; i++) {
        result.push(gray[(idx + i) % total]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer[]
     */
    function circularPermutation($n, $start) {
        $size = 1 << $n;
        $gray = [];
        for ($i = 0; $i < $size; $i++) {
            $gray[] = $i ^ ($i >> 1);
        }
        $idx = array_search($start, $gray);
        if ($idx === false) {
            $idx = 0;
        }
        $result = array_merge(array_slice($gray, $idx), array_slice($gray, 0, $idx));
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func circularPermutation(_ n: Int, _ start: Int) -> [Int] {
        let total = 1 << n
        var gray = [Int]()
        gray.reserveCapacity(total)
        for i in 0..<total {
            gray.append(i ^ (i >> 1))
        }
        guard let idx = gray.firstIndex(of: start) else { return [] }
        var result = [Int]()
        result.reserveCapacity(total)
        for i in 0..<total {
            result.append(gray[(idx + i) % total])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun circularPermutation(n: Int, start: Int): List<Int> {
        val total = 1 shl n
        val gray = IntArray(total)
        for (i in 0 until total) {
            gray[i] = i xor (i shr 1)
        }
        var idx = 0
        while (idx < total && gray[idx] != start) idx++
        val result = ArrayList<Int>(total)
        for (k in 0 until total) {
            result.add(gray[(idx + k) % total])
        }
        return result
    }
}
```

## Golang

```go
func circularPermutation(n int, start int) []int {
    m := 1 << n
    gray := make([]int, m)
    for i := 0; i < m; i++ {
        gray[i] = i ^ (i >> 1)
    }
    idx := 0
    for ; idx < m; idx++ {
        if gray[idx] == start {
            break
        }
    }
    ans := make([]int, m)
    copy(ans, gray[idx:])
    copy(ans[m-idx:], gray[:idx])
    return ans
}
```

## Ruby

```ruby
def circular_permutation(n, start)
  total = 1 << n
  gray = Array.new(total) { |i| i ^ (i >> 1) }
  idx = gray.index(start)
  gray[idx..-1] + gray[0...idx]
end
```

## Scala

```scala
object Solution {
    def circularPermutation(n: Int, start: Int): List[Int] = {
        val total = 1 << n
        val gray = new Array[Int](total)
        var i = 0
        while (i < total) {
            gray(i) = i ^ (i >> 1)
            i += 1
        }
        var startIdx = 0
        while (startIdx < total && gray(startIdx) != start) {
            startIdx += 1
        }
        val res = new Array[Int](total)
        i = 0
        while (i < total) {
            res(i) = gray((startIdx + i) % total)
            i += 1
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn circular_permutation(n: i32, start: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let total = 1usize << n_usize;
        let mut gray_codes = Vec::with_capacity(total);
        for i in 0..total {
            gray_codes.push((i ^ (i >> 1)) as i32);
        }
        let start_pos = gray_codes.iter().position(|&x| x == start).unwrap();
        let mut result = Vec::with_capacity(total);
        for i in 0..total {
            result.push(gray_codes[(start_pos + i) % total]);
        }
        result
    }
}
```
