# 1534. Count Good Triplets

## Cpp

```cpp
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int n = arr.size();
        int cnt = 0;
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                if (abs(arr[i] - arr[j]) > a) continue;
                for (int k = j + 1; k < n; ++k) {
                    if (abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
                        ++cnt;
                    }
                }
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        int n = arr.length;
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (Math.abs(arr[i] - arr[j]) > a) continue;
                for (int k = j + 1; k < n; k++) {
                    if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        cnt = 0
        for i in range(n - 2):
            ai = arr[i]
            for j in range(i + 1, n - 1):
                if abs(ai - arr[j]) > a:
                    continue
                aj = arr[j]
                for k in range(j + 1, n):
                    if abs(aj - arr[k]) <= b and abs(ai - arr[k]) <= c:
                        cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
        return cnt
```

## C

```c
#include <stdlib.h>

int countGoodTriplets(int* arr, int arrSize, int a, int b, int c) {
    int count = 0;
    for (int i = 0; i < arrSize - 2; ++i) {
        for (int j = i + 1; j < arrSize - 1; ++j) {
            if (abs(arr[i] - arr[j]) > a) continue;
            for (int k = j + 1; k < arrSize; ++k) {
                if (abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
                    ++count;
                }
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountGoodTriplets(int[] arr, int a, int b, int c) {
        int n = arr.Length;
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (Math.Abs(arr[i] - arr[j]) > a) continue;
                for (int k = j + 1; k < n; k++) {
                    if (Math.Abs(arr[j] - arr[k]) <= b && Math.Abs(arr[i] - arr[k]) <= c) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    let n = arr.length;
    let count = 0;
    for (let i = 0; i < n - 2; ++i) {
        for (let j = i + 1; j < n - 1; ++j) {
            if (Math.abs(arr[i] - arr[j]) > a) continue;
            for (let k = j + 1; k < n; ++k) {
                if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                    count++;
                }
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    const n = arr.length;
    let count = 0;
    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            if (Math.abs(arr[i] - arr[j]) > a) continue;
            for (let k = j + 1; k < n; k++) {
                if (Math.abs(arr[j] - arr[k]) <= b && Math.abs(arr[i] - arr[k]) <= c) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function countGoodTriplets($arr, $a, $b, $c) {
        $n = count($arr);
        $count = 0;
        for ($i = 0; $i < $n - 2; $i++) {
            for ($j = $i + 1; $j < $n - 1; $j++) {
                if (abs($arr[$i] - $arr[$j]) > $a) continue;
                for ($k = $j + 1; $k < $n; $k++) {
                    if (abs($arr[$j] - $arr[$k]) <= $b && abs($arr[$i] - $arr[$k]) <= $c) {
                        $count++;
                    }
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countGoodTriplets(_ arr: [Int], _ a: Int, _ b: Int, _ c: Int) -> Int {
        var count = 0
        let n = arr.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                if abs(arr[i] - arr[j]) > a { continue }
                for k in (j + 1)..<n {
                    if abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c {
                        count += 1
                    }
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGoodTriplets(arr: IntArray, a: Int, b: Int, c: Int): Int {
        var count = 0
        val n = arr.size
        for (i in 0 until n - 2) {
            for (j in i + 1 until n - 1) {
                if (kotlin.math.abs(arr[i] - arr[j]) > a) continue
                for (k in j + 1 until n) {
                    if (kotlin.math.abs(arr[j] - arr[k]) <= b &&
                        kotlin.math.abs(arr[i] - arr[k]) <= c) {
                        count++
                    }
                }
            }
        }
        return count
    }
}
```

## Golang

```go
func countGoodTriplets(arr []int, a int, b int, c int) int {
    n := len(arr)
    cnt := 0
    for i := 0; i < n-2; i++ {
        for j := i + 1; j < n-1; j++ {
            if abs(arr[i]-arr[j]) > a {
                continue
            }
            for k := j + 1; k < n; k++ {
                if abs(arr[j]-arr[k]) <= b && abs(arr[i]-arr[k]) <= c {
                    cnt++
                }
            }
        }
    }
    return cnt
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

## Ruby

```ruby
def count_good_triplets(arr, a, b, c)
  n = arr.length
  count = 0
  (0...n-2).each do |i|
    ((i+1)...n-1).each do |j|
      next unless (arr[i] - arr[j]).abs <= a
      ((j+1)...n).each do |k|
        if (arr[j] - arr[k]).abs <= b && (arr[i] - arr[k]).abs <= c
          count += 1
        end
      end
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countGoodTriplets(arr: Array[Int], a: Int, b: Int, c: Int): Int = {
        var count = 0
        val n = arr.length
        var i = 0
        while (i < n - 2) {
            var j = i + 1
            while (j < n - 1) {
                if (math.abs(arr(i) - arr(j)) <= a) {
                    var k = j + 1
                    while (k < n) {
                        if (math.abs(arr(j) - arr(k)) <= b && math.abs(arr(i) - arr(k)) <= c) {
                            count += 1
                        }
                        k += 1
                    }
                }
                j += 1
            }
            i += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        let n = arr.len();
        let mut cnt: i32 = 0;
        for i in 0..n - 2 {
            for j in i + 1..n - 1 {
                if (arr[i] - arr[j]).abs() > a {
                    continue;
                }
                for k in j + 1..n {
                    if (arr[j] - arr[k]).abs() <= b && (arr[i] - arr[k]).abs() <= c {
                        cnt += 1;
                    }
                }
            }
        }
        cnt
    }
}
```
