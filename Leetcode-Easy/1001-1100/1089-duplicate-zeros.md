# 1089. Duplicate Zeros

## Cpp

```cpp
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int possibleDups = 0;

        // Count zeros that can be duplicated within the array bounds
        for (int left = 0; left < n - possibleDups; ++left) {
            if (arr[left] == 0) {
                // Edge case: zero at the boundary where its duplicate would exceed length
                if (left == n - possibleDups - 1) {
                    arr[n - 1] = 0;
                    n -= 1;               // effective length reduced, no more duplication
                    break;
                }
                ++possibleDups;
            }
        }

        int last = n - possibleDups - 1;

        // Move elements backwards, duplicating zeros as needed
        for (int i = last; i >= 0; --i) {
            if (arr[i] == 0) {
                arr[i + possibleDups] = 0;
                --possibleDups;
                arr[i + possibleDups] = 0;
            } else {
                arr[i + possibleDups] = arr[i];
            }
        }
    }
};
```

## Java

```java
class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length;
        int possibleDups = 0;
        int length = n - 1;

        // Count zeros to be duplicated
        for (int left = 0; left <= length - possibleDups; left++) {
            if (arr[left] == 0) {
                // Edge case: zero at the boundary with no space for its duplicate
                if (left == length - possibleDups) {
                    arr[length] = 0;
                    length -= 1;
                    break;
                }
                possibleDups++;
            }
        }

        // Shift and duplicate from the end
        for (int i = length - possibleDups; i >= 0; i--) {
            if (arr[i] == 0) {
                arr[i + possibleDups] = 0;
                possibleDups--;
                arr[i + possibleDups] = 0;
            } else {
                arr[i + possibleDups] = arr[i];
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        possible_dups = 0
        length = n - 1

        left = 0
        while left <= length - possible_dups:
            if arr[left] == 0:
                # Edge case: zero at the boundary that can't be duplicated fully
                if left == length - possible_dups:
                    arr[length] = 0
                    length -= 1
                    break
                possible_dups += 1
            left += 1

        last = length - possible_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
```

## Python3

```python
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        possible_dups = 0
        left = 0

        # Count zeros that can be duplicated within the array bounds
        while left + possible_dups < n:
            if arr[left] == 0:
                # Edge case: zero at the boundary where its duplicate would exceed length
                if left + possible_dups == n - 1:
                    # Place a single zero at the end and reduce effective length
                    arr[-1] = 0
                    n -= 1
                    break
                possible_dups += 1
            left += 1

        # Start from the last element that will be part of the final array
        i = left - 1          # index in original portion
        j = n - 1             # write pointer at the end of the array

        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
                arr[j] = 0
                j -= 1
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1
```

## C

```c
void duplicateZeros(int* arr, int arrSize) {
    int possibleDups = 0;
    int n = arrSize;

    // First pass: count zeros that can be duplicated
    for (int left = 0; left < n - possibleDups; ++left) {
        if (arr[left] == 0) {
            // Edge case: zero at the boundary which can't be fully duplicated
            if (left == n - 1 - possibleDups) {
                arr[n - 1] = 0;
                n -= 1;               // reduce effective length
                break;
            }
            ++possibleDups;
        }
    }

    // Second pass: copy from the end, duplicating zeros
    int last = n - 1 - possibleDups;   // index of last element to consider
    for (int i = last; i >= 0; --i) {
        if (arr[i] == 0) {
            arr[n - 1] = 0;
            --n;
            arr[n - 1] = 0;
            --n;
        } else {
            arr[n - 1] = arr[i];
            --n;
        }
    }
}
```

## Csharp

```csharp
public class Solution
{
    public void DuplicateZeros(int[] arr)
    {
        int length = arr.Length;
        int possibleDups = 0;

        // Find the number of zeros to be duplicated.
        for (int left = 0; left < length - possibleDups; left++)
        {
            if (arr[left] == 0)
            {
                // Edge case: zero at the boundary which can't be fully duplicated.
                if (left == length - possibleDups - 1)
                {
                    // Copy this zero once at the end and reduce effective length.
                    arr[length - 1] = 0;
                    length -= 1; // Exclude the last element from further processing.
                    break;
                }
                possibleDups++;
            }
        }

        int last = length - possibleDups - 1; // Index of last element to process.

        // Shift and duplicate zeros starting from the end.
        for (int i = last; i >= 0; i--)
        {
            if (arr[i] == 0)
            {
                arr[i + possibleDups] = 0;
                possibleDups--;
                arr[i + possibleDups] = 0;
            }
            else
            {
                arr[i + possibleDups] = arr[i];
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    let n = arr.length;
    let possibleDups = 0;

    // First pass: count zeros that can be duplicated within the array bounds
    for (let left = 0; left < n - possibleDups; left++) {
        if (arr[left] === 0) {
            // Edge case: zero at the boundary which can't be fully duplicated
            if (left === n - possibleDups - 1) {
                // Place a single zero at the end and shrink effective length
                arr[n - 1] = 0;
                n -= 1; // reduce the considered array size
                break;
            }
            possibleDups++;
        }
    }

    // Second pass: work backwards, copying elements to their new positions
    let last = n - possibleDups - 1;
    for (let i = last; i >= 0; i--) {
        if (arr[i] === 0) {
            arr[i + possibleDups] = 0;
            possibleDups--;
            arr[i + possibleDups] = 0;
        } else {
            arr[i + possibleDups] = arr[i];
        }
    }
};
```

## Typescript

```typescript
function duplicateZeros(arr: number[]): void {
    let possibleDups = 0;
    let length = arr.length - 1;

    // First pass: count zeros that can be duplicated
    for (let left = 0; left <= length - possibleDups; left++) {
        if (arr[left] === 0) {
            // Edge case: zero at the boundary which can't be fully duplicated
            if (left === length - possibleDups) {
                arr[length] = 0;
                length -= 1;
                break;
            }
            possibleDups++;
        }
    }

    // Second pass: copy elements from the end, duplicating zeros
    for (let i = length - possibleDups; i >= 0; i--) {
        if (arr[i] === 0) {
            arr[i + possibleDups] = 0;
            possibleDups--;
            arr[i + possibleDups] = 0;
        } else {
            arr[i + possibleDups] = arr[i];
        }
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return NULL
     */
    function duplicateZeros(&$arr) {
        $n = count($arr);
        $possibleDups = 0;

        // First pass: find how many zeros can be duplicated within the array bounds
        for ($left = 0; $left < $n - $possibleDups; $left++) {
            if ($arr[$left] == 0) {
                // Edge case: zero at the boundary where its duplicate would exceed length
                if ($left == $n - $possibleDups - 1) {
                    // Place a single zero at the last position and shrink effective length
                    $arr[$n - 1] = 0;
                    $n = $n - 1;
                    break;
                }
                $possibleDups++;
            }
        }

        // Second pass: work backwards, copying elements to their new positions
        $last = $n - $possibleDups - 1; // index of last element to process

        for ($i = $last; $i >= 0; $i--) {
            if ($arr[$i] == 0) {
                $arr[$i + $possibleDups] = 0;
                $possibleDups--;
                $arr[$i + $possibleDups] = 0;
            } else {
                $arr[$i + $possibleDups] = $arr[$i];
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func duplicateZeros(_ arr: inout [Int]) {
        var n = arr.count
        var possibleDups = 0
        var left = 0

        // First pass: count zeros that can be duplicated within the array bounds
        while left + possibleDups < n {
            if arr[left] == 0 {
                // Edge case: zero at the boundary where its duplicate would exceed length
                if left + possibleDups == n - 1 {
                    // Place this zero at the end and shrink effective length
                    arr[n - 1] = 0
                    n -= 1
                    break
                }
                possibleDups += 1
            }
            left += 1
        }

        var i = n - 1 - possibleDups          // Index of last element to consider
        var j = arr.count - 1                 // Position to write into

        // Second pass: copy elements backwards, duplicating zeros
        while i >= 0 {
            if arr[i] == 0 {
                arr[j] = 0
                j -= 1
                arr[j] = 0
                j -= 1
            } else {
                arr[j] = arr[i]
                j -= 1
            }
            i -= 1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun duplicateZeros(arr: IntArray): Unit {
        val n = arr.size
        var zeros = 0
        for (i in 0 until n) {
            if (arr[i] == 0) zeros++
        }
        var i = n - 1
        var j = n + zeros - 1
        while (i >= 0) {
            if (j < n && j >= 0) {
                arr[j] = arr[i]
            }
            if (arr[i] == 0) {
                j--
                if (j < n && j >= 0) {
                    arr[j] = 0
                }
            }
            i--
            j--
        }
    }
}
```

## Dart

```dart
class Solution {
  void duplicateZeros(List<int> arr) {
    int length = arr.length - 1;
    int possibleDups = 0;

    // Find the number of zeros to be duplicated
    for (int left = 0; left <= length - possibleDups; left++) {
      if (arr[left] == 0) {
        // Edge case: zero at the boundary which can't be duplicated fully
        if (left == length - possibleDups) {
          arr[length] = 0;
          length -= 1;
          break;
        }
        possibleDups++;
      }
    }

    int i = length - possibleDups;
    int j = length;

    while (i >= 0) {
      if (arr[i] == 0) {
        arr[j] = 0;
        j--;
        arr[j] = 0;
        j--;
      } else {
        arr[j] = arr[i];
        j--;
      }
      i--;
    }
  }
}
```

## Golang

```go
func duplicateZeros(arr []int) {
    n := len(arr)
    possibleDups := 0

    // Find the number of zeros to be duplicated
    for i := 0; i < n-possibleDups; i++ {
        if arr[i] == 0 {
            // Edge case: zero at the boundary where its duplicate would exceed array length
            if i == n-possibleDups-1 {
                // Copy this zero once at the end and reduce effective length
                arr[n-1] = 0
                n--
                break
            }
            possibleDups++
        }
    }

    // Start from the last index that will be part of the final array
    last := n - possibleDups - 1
    for i := last; i >= 0; i-- {
        if arr[i] == 0 {
            arr[i+possibleDups] = 0
            possibleDups--
            arr[i+possibleDups] = 0
        } else {
            arr[i+possibleDups] = arr[i]
        }
    }
}
```

## Ruby

```ruby
def duplicate_zeros(arr)
  n = arr.length
  possible_dups = 0
  i = 0

  while i + possible_dups < n
    if arr[i] == 0
      if i + possible_dups == n - 1
        arr[n - 1] = 0
        n -= 1
        break
      end
      possible_dups += 1
    end
    i += 1
  end

  last = n - 1
  i = n - 1 - possible_dups

  while i >= 0
    if arr[i] == 0
      arr[last] = 0
      last -= 1
      arr[last] = 0
      last -= 1
    else
      arr[last] = arr[i]
      last -= 1
    end
    i -= 1
  end
end
```

## Scala

```scala
object Solution {
  def duplicateZeros(arr: Array[Int]): Unit = {
    val n = arr.length
    var zeros = 0
    var i = 0
    while (i < n) {
      if (arr(i) == 0) zeros += 1
      i += 1
    }

    var j = n + zeros - 1
    i = n - 1
    while (i >= 0 && j >= 0) {
      if (arr(i) != 0) {
        if (j < n) arr(j) = arr(i)
      } else {
        // write first zero
        if (j < n) arr(j) = 0
        j -= 1
        // write second zero
        if (j >= 0 && j < n) arr(j) = 0
      }
      i -= 1
      j -= 1
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn duplicate_zeros(arr: &mut Vec<i32>) {
        let n = arr.len();
        if n == 0 {
            return;
        }
        let mut zeros = 0usize;
        let mut i = 0usize;

        // First pass: count zeros that can be duplicated within bounds
        while i + zeros < n {
            if arr[i] == 0 {
                // Edge case: zero at the boundary where its duplicate would exceed array length
                if i + zeros == n - 1 {
                    // Place a single zero at the end and copy remaining elements
                    arr[n - 1] = 0;
                    let mut left = i as isize - 1;
                    let mut right = (n as isize) - 2;
                    while left >= 0 {
                        arr[right as usize] = arr[left as usize];
                        if arr[left as usize] == 0 {
                            right -= 1;
                            arr[right as usize] = 0;
                        }
                        left -= 1;
                        right -= 1;
                    }
                    return;
                }
                zeros += 1;
            }
            i += 1;
        }

        // Second pass: copy from the end, duplicating zeros
        let mut left = (i as isize) - 1;
        let mut right = (n as isize) - 1;
        while left >= 0 {
            arr[right as usize] = arr[left as usize];
            if arr[left as usize] == 0 {
                right -= 1;
                arr[right as usize] = 0;
            }
            left -= 1;
            right -= 1;
        }
    }
}
```
