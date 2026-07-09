# 1095. Find in Mountain Array

## Cpp

```cpp
/ **
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        // Find peak index
        int l = 1, r = n - 2;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1))
                l = mid + 1;
            else
                r = mid;
        }
        int peak = l;

        // Binary search on increasing part [0, peak]
        l = 0; r = peak;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mountainArr.get(mid) < target)
                l = mid + 1;
            else
                r = mid;
        }
        if (mountainArr.get(l) == target) return l;

        // Binary search on decreasing part [peak+1, n-1]
        l = peak + 1; r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mountainArr.get(mid) > target)
                l = mid + 1;
            else
                r = mid;
        }
        if (mountainArr.get(l) == target) return l;

        return -1;
    }
};
```

## Java

```java
/ **
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 * /
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        // Find peak index
        int lo = 1, hi = n - 2;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int peak = lo;

        // Search in increasing part
        lo = 0;
        hi = peak;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = mountainArr.get(mid);
            if (val == target) {
                return mid;
            }
            if (val < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        // Search in decreasing part
        lo = peak + 1;
        hi = n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = mountainArr.get(mid);
            if (val == target) {
                return mid;
            }
            if (val > target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountainArr: MountainArray
        :rtype: integer
        """
        def find_peak(arr):
            lo, hi = 1, arr.length() - 2
            while lo < hi:
                mid = (lo + hi) // 2
                if arr.get(mid) < arr.get(mid + 1):
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def binary_search_inc(arr, target, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                val = arr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        def binary_search_dec(arr, target, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                val = arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        peak = find_peak(mountainArr)

        idx = binary_search_inc(mountainArr, target, 0, peak)
        if idx != -1:
            return idx

        return binary_search_dec(mountainArr, target, peak + 1, mountainArr.length() - 1)
```

## Python3

```python
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # Find peak index
        lo, hi = 1, n - 2
        while lo < hi:
            mid = (lo + hi) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo
        
        # Binary search on increasing part [0, peak]
        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        # Binary search on decreasing part [peak+1, n-1]
        lo, hi = peak + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1
```

## C

```c
/*************************************************************
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 *************************************************************/

int get(MountainArray *, int index);
int length(MountainArray *);

static int findPeak(MountainArray* arr) {
    int l = 1;
    int r = length(arr) - 2;               // peak cannot be at the ends
    while (l < r) {
        int mid = l + (r - l) / 2;
        int midVal = get(arr, mid);
        int nextVal = get(arr, mid + 1);
        if (midVal < nextVal)
            l = mid + 1;                  // peak is to the right
        else
            r = mid;                      // peak is at mid or left
    }
    return l;
}

static int binarySearchInc(MountainArray* arr, int target, int l, int r) {
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = get(arr, mid);
        if (val == target)
            return mid;
        else if (val < target)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
}

static int binarySearchDec(MountainArray* arr, int target, int l, int r) {
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = get(arr, mid);
        if (val == target)
            return mid;
        else if (val > target)
            l = mid + 1;                  // move right in decreasing part
        else
            r = mid - 1;
    }
    return -1;
}

int findInMountainArray(int target, MountainArray* mountainArr) {
    int n = length(mountainArr);
    if (n < 3)
        return -1;

    int peak = findPeak(mountainArr);

    int idx = binarySearchInc(mountainArr, target, 0, peak);
    if (idx != -1)
        return idx;

    return binarySearchDec(mountainArr, target, peak + 1, n - 1);
}
```

## Csharp

```csharp
/ **
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     public int Get(int index) {}
 *     public int Length() {}
 * }
 * /
 
class Solution {
    public int FindInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.Length();
        
        // Find peak index
        int low = 1, high = n - 2;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (mountainArr.Get(mid) < mountainArr.Get(mid + 1)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int peak = low;
        
        // Binary search on increasing part [0, peak]
        int l = 0, r = peak;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int val = mountainArr.Get(mid);
            if (val == target) return mid;
            if (val < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        // Binary search on decreasing part [peak+1, n-1]
        l = peak + 1;
        r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int val = mountainArr.Get(mid);
            if (val == target) return mid;
            if (val > target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * function MountainArray() {
 *     @param {number} index
 *     @return {number}
 *     this.get = function(index) {
 *         ...
 *     };
 *
 *     @return {number}
 *     this.length = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {number} target
 * @param {MountainArray} mountainArr
 * @return {number}
 */
var findInMountainArray = function(target, mountainArr) {
    const n = mountainArr.length();

    // Find peak index
    let low = 1, high = n - 2;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        const midVal = mountainArr.get(mid);
        const nextVal = mountainArr.get(mid + 1);
        if (midVal < nextVal) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    const peak = low; // peak index

    // Binary search on increasing part [0, peak]
    let l = 0, r = peak;
    while (l <= r) {
        const m = Math.floor((l + r) / 2);
        const val = mountainArr.get(m);
        if (val === target) return m;
        if (val < target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    // Binary search on decreasing part [peak+1, n-1]
    l = peak + 1;
    r = n - 1;
    while (l <= r) {
        const m = Math.floor((l + r) / 2);
        const val = mountainArr.get(m);
        if (val === target) return m;
        if (val > target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    return -1;
};
```

## Typescript

```typescript
/ **
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     get(index: number): number {}
 *
 *     length(): number {}
 * }
 * /
function findInMountainArray(target: number, mountainArr: MountainArray): number {
    const n = mountainArr.length();

    // Find peak index
    let low = 1;
    let high = n - 2;
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    const peak = low;

    // Binary search on increasing part [0, peak]
    let l = 0;
    let r = peak;
    while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        const val = mountainArr.get(mid);
        if (val === target) return mid;
        if (val < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    // Binary search on decreasing part [peak+1, n-1]
    l = peak + 1;
    r = n - 1;
    while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        const val = mountainArr.get(mid);
        if (val === target) return mid;
        if (val > target) {
            l = mid + 1; // move right in decreasing array
        } else {
            r = mid - 1;
        }
    }

    return -1;
}
```

## Php

```php
/ **
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     function get($index) {}
 *     function length() {}
 * }
 * /
class Solution {
    /**
     * @param Integer $target
     * @param MountainArray $mountainArr
     * @return Integer
     */
    function findInMountainArray($target, $mountainArr) {
        $n = $mountainArr->length();

        // 1. Find peak index
        $low = 1;
        $high = $n - 2; // peak cannot be at the ends
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($mountainArr->get($mid) < $mountainArr->get($mid + 1)) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        $peak = $low;

        // 2. Binary search on increasing part [0, peak]
        $idx = $this->binarySearchInc($mountainArr, $target, 0, $peak);
        if ($idx != -1) {
            return $idx;
        }

        // 3. Binary search on decreasing part [peak+1, n-1]
        return $this->binarySearchDec($mountainArr, $target, $peak + 1, $n - 1);
    }

    private function binarySearchInc($mountainArr, $target, $low, $high) {
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($mountainArr->get($mid) < $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return ($mountainArr->get($low) == $target) ? $low : -1;
    }

    private function binarySearchDec($mountainArr, $target, $low, $high) {
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($mountainArr->get($mid) > $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return ($mountainArr->get($low) == $target) ? $low : -1;
    }
}
```

## Swift

```swift
/ **
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public func get(_ index: Int) -> Int {}
 *     public func length() -> Int {}
 * }
 * /
class Solution {
    func findInMountainArray(_ target: Int, _ mountainArr: MountainArray) -> Int {
        let n = mountainArr.length()
        // Find peak index
        var low = 1
        var high = n - 2
        while low < high {
            let mid = (low + high) / 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        let peak = low
        
        // Search in the increasing part [0, peak]
        var left = 0
        var right = peak
        while left <= right {
            let mid = (left + right) / 2
            let val = mountainArr.get(mid)
            if val == target {
                return mid
            } else if val < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        
        // Search in the decreasing part [peak+1, n-1]
        left = peak + 1
        right = n - 1
        while left <= right {
            let mid = (left + right) / 2
            let val = mountainArr.get(mid)
            if val == target {
                return mid
            } else if val > target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
/ **
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     fun get(index: Int): Int {}
 *     fun length(): Int {}
 * }
 */

class Solution {
    fun findInMountainArray(target: Int, mountainArr: MountainArray): Int {
        val n = mountainArr.length()
        // Find peak index
        var lo = 1
        var hi = n - 2
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        val peak = lo

        // Binary search on increasing part [0, peak]
        var left = 0
        var right = peak
        while (left <= right) {
            val mid = left + (right - left) / 2
            val value = mountainArr.get(mid)
            if (value == target) return mid
            if (value < target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        // Binary search on decreasing part [peak+1, n-1]
        left = peak + 1
        right = n - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            val value = mountainArr.get(mid)
            if (value == target) return mid
            if (value > target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        return -1
    }
}
```

## Golang

```go
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */

func findInMountainArray(target int, mountainArr *MountainArray) int {
	n := mountainArr.length()
	// 1. Find peak index
	low, high := 1, n-2
	for low < high {
		mid := (low + high) >> 1
		if mountainArr.get(mid) < mountainArr.get(mid+1) {
			low = mid + 1
		} else {
			high = mid
		}
	}
	peak := low

	// 2. Binary search on increasing part [0, peak]
	lo, hi := 0, peak
	for lo <= hi {
		mid := (lo + hi) >> 1
		val := mountainArr.get(mid)
		if val == target {
			return mid
		}
		if val < target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	// 3. Binary search on decreasing part [peak+1, n-1]
	lo, hi = peak+1, n-1
	for lo <= hi {
		mid := (lo + hi) >> 1
		val := mountainArr.get(mid)
		if val == target {
			return mid
		}
		if val > target {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	return -1
}
```

## Ruby

```ruby
def findInMountainArray(target, mountainArr)
  n = mountainArr.length

  # Find peak index
  low = 1
  high = n - 2
  while low < high
    mid = (low + high) / 2
    if mountainArr.get(mid) < mountainArr.get(mid + 1)
      low = mid + 1
    else
      high = mid
    end
  end
  peak = low

  # Search in the increasing part [0, peak]
  l = 0
  r = peak
  while l <= r
    m = (l + r) / 2
    val = mountainArr.get(m)
    if val == target
      return m
    elsif val < target
      l = m + 1
    else
      r = m - 1
    end
  end

  # Search in the decreasing part [peak+1, n-1]
  l = peak + 1
  r = n - 1
  while l <= r
    m = (l + r) / 2
    val = mountainArr.get(m)
    if val == target
      return m
    elsif val > target
      l = m + 1
    else
      r = m - 1
    end
  end

  -1
end
```

## Scala

```scala
/****
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *     def get(index: Int): Int = {}
 *     def length(): Int = {}
 * }
 */

object Solution {
  def findInMountainArray(value: Int, mountainArr: MountainArray): Int = {
    val n = mountainArr.length()
    // Find peak index
    var low = 1
    var high = n - 2
    while (low < high) {
      val mid = low + (high - low) / 2
      if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
        low = mid + 1
      } else {
        high = mid
      }
    }
    val peak = low

    // Binary search on increasing part [0, peak]
    var l = 0
    var h = peak
    while (l < h) {
      val mid = l + (h - l) / 2
      if (mountainArr.get(mid) < value) {
        l = mid + 1
      } else {
        h = mid
      }
    }
    if (mountainArr.get(l) == value) return l

    // Binary search on decreasing part [peak+1, n-1]
    var l2 = peak + 1
    var h2 = n - 1
    while (l2 < h2) {
      val mid = l2 + (h2 - l2) / 2
      if (mountainArr.get(mid) > value) {
        l2 = mid + 1
      } else {
        h2 = mid
      }
    }
    if (mountainArr.get(l2) == value) return l2

    -1
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn find_in_mountain_array(target: i32, mountain_arr: &MountainArray) -> i32 {
        let n = mountain_arr.length();

        // Find peak index
        let mut low = 1;
        let mut high = n - 2;
        while low < high {
            let mid = low + (high - low) / 2;
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        let peak = low;

        // Binary search on the increasing part [0, peak]
        let mut l = 0;
        let mut r = peak;
        while l < r {
            let mid = l + (r - l) / 2;
            if mountain_arr.get(mid) < target {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if mountain_arr.get(l) == target {
            return l;
        }

        // Binary search on the decreasing part [peak+1, n-1]
        let mut l = peak + 1;
        let mut r = n - 1;
        while l < r {
            let mid = l + (r - l) / 2;
            if mountain_arr.get(mid) > target {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if mountain_arr.get(l) == target {
            return l;
        }

        -1
    }
}
```
