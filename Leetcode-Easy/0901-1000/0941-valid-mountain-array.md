# 0941. Valid Mountain Array

## Cpp

```cpp
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return false;
        int i = 0;
        // climb up
        while (i + 1 < n && arr[i] < arr[i + 1]) ++i;
        // peak can't be first or last
        if (i == 0 || i == n - 1) return false;
        // go down
        while (i + 1 < n && arr[i] > arr[i + 1]) ++i;
        return i == n - 1;
    }
};
```

## Java

```java
class Solution {
    public boolean validMountainArray(int[] arr) {
        int n = arr.length;
        if (n < 3) return false;
        int i = 0;
        // climb up
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }
        // peak can't be first or last
        if (i == 0 || i == n - 1) return false;
        // descend down
        while (i + 1 < n && arr[i] > arr[i + 1]) {
            i++;
        }
        return i == n - 1;
    }
}
```

## Python

```python
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False

        i = 0
        # climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # descend down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
```

## Python3

```python
from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 0
        # climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False
        # go down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
```

## C

```c
#include <stdbool.h>

bool validMountainArray(int* arr, int arrSize){
    if (arrSize < 3) return false;
    
    int i = 0;
    // climb up
    while (i + 1 < arrSize && arr[i] < arr[i + 1]) {
        i++;
    }
    
    // peak can't be first or last
    if (i == 0 || i == arrSize - 1) return false;
    
    // descend down
    while (i + 1 < arrSize && arr[i] > arr[i + 1]) {
        i++;
    }
    
    return i == arrSize - 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool ValidMountainArray(int[] arr) {
        int n = arr.Length;
        if (n < 3) return false;

        int i = 0;
        while (i + 1 < n && arr[i] < arr[i + 1]) i++;

        // peak cannot be first or last element
        if (i == 0 || i == n - 1) return false;

        while (i + 1 < n && arr[i] > arr[i + 1]) i++;

        return i == n - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    const n = arr.length;
    if (n < 3) return false;

    let i = 1;
    // climb up
    while (i < n && arr[i] > arr[i - 1]) {
        i++;
    }

    // peak can't be first or last
    if (i === 1 || i === n) return false;

    // descend down
    while (i < n && arr[i] < arr[i - 1]) {
        i++;
    }

    return i === n;
};
```

## Typescript

```typescript
function validMountainArray(arr: number[]): boolean {
    const n = arr.length;
    if (n < 3) return false;

    let i = 0;
    // climb up
    while (i + 1 < n && arr[i] < arr[i + 1]) {
        i++;
    }

    // peak can't be first or last
    if (i === 0 || i === n - 1) return false;

    // descend down
    while (i + 1 < n && arr[i] > arr[i + 1]) {
        i++;
    }

    return i === n - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function validMountainArray($arr) {
        $n = count($arr);
        if ($n < 3) {
            return false;
        }

        $i = 0;

        // climb up
        while ($i + 1 < $n && $arr[$i] < $arr[$i + 1]) {
            $i++;
        }

        // peak can't be first or last
        if ($i == 0 || $i == $n - 1) {
            return false;
        }

        // climb down
        while ($i + 1 < $n && $arr[$i] > $arr[$i + 1]) {
            $i++;
        }

        return $i == $n - 1;
    }
}
```

## Swift

```swift
class Solution {
    func validMountainArray(_ arr: [Int]) -> Bool {
        let n = arr.count
        if n < 3 { return false }
        var i = 0
        while i + 1 < n && arr[i] < arr[i + 1] {
            i += 1
        }
        if i == 0 || i == n - 1 { return false }
        while i + 1 < n && arr[i] > arr[i + 1] {
            i += 1
        }
        return i == n - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validMountainArray(arr: IntArray): Boolean {
        val n = arr.size
        if (n < 3) return false
        var i = 1
        while (i < n && arr[i] > arr[i - 1]) i++
        if (i == 1 || i == n) return false
        while (i < n && arr[i] < arr[i - 1]) i++
        return i == n
    }
}
```

## Golang

```go
func validMountainArray(arr []int) bool {
    n := len(arr)
    if n < 3 {
        return false
    }
    i := 0
    for i+1 < n && arr[i] < arr[i+1] {
        i++
    }
    if i == 0 || i == n-1 {
        return false
    }
    for i+1 < n && arr[i] > arr[i+1] {
        i++
    }
    return i == n-1
}
```

## Ruby

```ruby
def valid_mountain_array(arr)
  n = arr.length
  return false if n < 3
  i = 0
  while i + 1 < n && arr[i] < arr[i + 1]
    i += 1
  end
  return false if i == 0 || i == n - 1
  while i + 1 < n && arr[i] > arr[i + 1]
    i += 1
  end
  i == n - 1
end
```

## Scala

```scala
object Solution {
    def validMountainArray(arr: Array[Int]): Boolean = {
        val n = arr.length
        if (n < 3) return false
        var i = 0
        while (i + 1 < n && arr(i) < arr(i + 1)) i += 1
        if (i == 0 || i == n - 1) return false
        while (i + 1 < n && arr(i) > arr(i + 1)) i += 1
        i == n - 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_mountain_array(arr: Vec<i32>) -> bool {
        let n = arr.len();
        if n < 3 {
            return false;
        }
        let mut i = 0;
        // ascend
        while i + 1 < n && arr[i] < arr[i + 1] {
            i += 1;
        }
        // peak can't be first or last
        if i == 0 || i == n - 1 {
            return false;
        }
        // descend
        while i + 1 < n && arr[i] > arr[i + 1] {
            i += 1;
        }
        i == n - 1
    }
}
```
