# 2905. Find Indices With Index and Value Difference II

## Cpp

```cpp
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        int n = nums.size();
        if (valueDifference == 0) return {0, 0};
        long long minVal = LLONG_MAX;
        int minIdx = -1;
        long long maxVal = LLONG_MIN;
        int maxIdx = -1;
        for (int i = 0; i < n; ++i) {
            int addPos = i - indexDifference;
            if (addPos >= 0) {
                long long v = nums[addPos];
                if (v < minVal) { minVal = v; minIdx = addPos; }
                if (v > maxVal) { maxVal = v; maxIdx = addPos; }
            }
            if (minIdx != -1) {
                if (llabs((long long)nums[i] - minVal) >= valueDifference) return {i, minIdx};
                if (llabs((long long)nums[i] - maxVal) >= valueDifference) return {i, maxIdx};
            }
        }
        return {-1, -1};
    }
};
```

## Java

```java
class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.length;
        int[] prefMinIdx = new int[n];
        int[] prefMaxIdx = new int[n];
        int minVal = nums[0];
        int maxVal = nums[0];
        prefMinIdx[0] = 0;
        prefMaxIdx[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < minVal) {
                minVal = nums[i];
                prefMinIdx[i] = i;
            } else {
                prefMinIdx[i] = prefMinIdx[i - 1];
            }
            if (nums[i] > maxVal) {
                maxVal = nums[i];
                prefMaxIdx[i] = i;
            } else {
                prefMaxIdx[i] = prefMaxIdx[i - 1];
            }
        }

        for (int i = 0; i < n; i++) {
            int limit = i - indexDifference;
            if (limit < 0) continue;

            int jMin = prefMinIdx[limit];
            if (Math.abs(nums[i] - nums[jMin]) >= valueDifference) {
                return new int[]{i, jMin};
            }

            int jMax = prefMaxIdx[limit];
            if (Math.abs(nums[i] - nums[jMax]) >= valueDifference) {
                return new int[]{i, jMax};
            }
        }
        return new int[]{-1, -1};
    }
}
```

## Python

```python
class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        n = len(nums)
        pref_min_val = 10**18
        pref_max_val = -1
        pref_min_idx = -1
        pref_max_idx = -1
        p = 0  # next index to add into prefix structures

        for i in range(n):
            # Add all indices that become eligible as left side candidates
            while p <= i - indexDifference:
                val = nums[p]
                if val < pref_min_val:
                    pref_min_val = val
                    pref_min_idx = p
                if val > pref_max_val:
                    pref_max_val = val
                    pref_max_idx = p
                p += 1

            # If there is at least one candidate, check the conditions
            if i - indexDifference >= 0:
                if abs(nums[i] - pref_min_val) >= valueDifference:
                    return [i, pref_min_idx]
                if abs(nums[i] - pref_max_val) >= valueDifference:
                    return [i, pref_max_idx]

        return [-1, -1]
```

## Python3

```python
from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        # Special handling when valueDifference is 0
        if valueDifference == 0:
            if indexDifference == 0:
                return [0, 0]
            if indexDifference <= n - 1:
                return [0, indexDifference]
            return [-1, -1]

        min_val = None
        max_val = None
        min_idx = -1
        max_idx = -1

        for i in range(n):
            j = i - indexDifference
            if j >= 0:
                v = nums[j]
                if min_val is None or v < min_val:
                    min_val = v
                    min_idx = j
                if max_val is None or v > max_val:
                    max_val = v
                    max_idx = j

            if min_val is not None:
                if abs(nums[i] - min_val) >= valueDifference:
                    return [i, min_idx]
                if abs(nums[i] - max_val) >= valueDifference:
                    return [i, max_idx]

        return [-1, -1]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    int *ans = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    if (numsSize == 0) {
        ans[0] = -1; ans[1] = -1;
        return ans;
    }
    
    // Prefix min and max indices
    int *prefMinIdx = (int*)malloc(numsSize * sizeof(int));
    int *prefMaxIdx = (int*)malloc(numsSize * sizeof(int));
    
    prefMinIdx[0] = 0;
    prefMaxIdx[0] = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < nums[prefMinIdx[i-1]]) prefMinIdx[i] = i;
        else prefMinIdx[i] = prefMinIdx[i-1];
        
        if (nums[i] > nums[prefMaxIdx[i-1]]) prefMaxIdx[i] = i;
        else prefMaxIdx[i] = prefMaxIdx[i-1];
    }
    
    for (int i = indexDifference; i < numsSize; ++i) {
        int leftPos = i - indexDifference;
        if (leftPos < 0) continue; // shouldn't happen due to loop start
        
        int minIdx = prefMinIdx[leftPos];
        int maxIdx = prefMaxIdx[leftPos];
        
        long long diff1 = nums[i] - nums[minIdx];
        if (diff1 < 0) diff1 = -diff1;
        if (diff1 >= valueDifference) {
            ans[0] = minIdx;
            ans[1] = i;
            free(prefMinIdx);
            free(prefMaxIdx);
            return ans;
        }
        
        long long diff2 = nums[i] - nums[maxIdx];
        if (diff2 < 0) diff2 = -diff2;
        if (diff2 >= valueDifference) {
            ans[0] = maxIdx;
            ans[1] = i;
            free(prefMinIdx);
            free(prefMaxIdx);
            return ans;
        }
    }
    
    // No pair found
    ans[0] = -1;
    ans[1] = -1;
    free(prefMinIdx);
    free(prefMaxIdx);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindIndices(int[] nums, int indexDifference, int valueDifference) {
        int n = nums.Length;
        int prefMinVal = int.MaxValue;
        int prefMinIdx = -1;
        int prefMaxVal = int.MinValue;
        int prefMaxIdx = -1;

        for (int i = 0; i < n; i++) {
            int newIdx = i - indexDifference;
            if (newIdx >= 0) {
                int val = nums[newIdx];
                if (val < prefMinVal) {
                    prefMinVal = val;
                    prefMinIdx = newIdx;
                }
                if (val > prefMaxVal) {
                    prefMaxVal = val;
                    prefMaxIdx = newIdx;
                }
            }

            if (prefMinIdx != -1) {
                long diffMin = Math.Abs((long)nums[i] - prefMinVal);
                if (diffMin >= valueDifference) {
                    return new int[] { i, prefMinIdx };
                }
                long diffMax = Math.Abs((long)nums[i] - prefMaxVal);
                if (diffMax >= valueDifference) {
                    return new int[] { i, prefMaxIdx };
                }
            }
        }

        return new int[] { -1, -1 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} indexDifference
 * @param {number} valueDifference
 * @return {number[]}
 */
var findIndices = function(nums, indexDifference, valueDifference) {
    const n = nums.length;
    // If valueDifference is 0, any single index works.
    if (valueDifference === 0) return [0, 0];

    // Prefix minimum values and their indices
    const prefMinVal = new Array(n);
    const prefMinIdx = new Array(n);
    // Prefix maximum values and their indices
    const prefMaxVal = new Array(n);
    const prefMaxIdx = new Array(n);

    prefMinVal[0] = nums[0];
    prefMinIdx[0] = 0;
    prefMaxVal[0] = nums[0];
    prefMaxIdx[0] = 0;

    for (let i = 1; i < n; ++i) {
        if (nums[i] < prefMinVal[i - 1]) {
            prefMinVal[i] = nums[i];
            prefMinIdx[i] = i;
        } else {
            prefMinVal[i] = prefMinVal[i - 1];
            prefMinIdx[i] = prefMinIdx[i - 1];
        }

        if (nums[i] > prefMaxVal[i - 1]) {
            prefMaxVal[i] = nums[i];
            prefMaxIdx[i] = i;
        } else {
            prefMaxVal[i] = prefMaxVal[i - 1];
            prefMaxIdx[i] = prefMaxIdx[i - 1];
        }
    }

    for (let i = indexDifference; i < n; ++i) {
        const j = i - indexDifference; // farthest allowed earlier index
        const minV = prefMinVal[j];
        const minI = prefMinIdx[j];
        if (Math.abs(nums[i] - minV) >= valueDifference) {
            return [i, minI];
        }
        const maxV = prefMaxVal[j];
        const maxI = prefMaxIdx[j];
        if (Math.abs(nums[i] - maxV) >= valueDifference) {
            return [i, maxI];
        }
    }

    return [-1, -1];
};
```

## Typescript

```typescript
function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    const n = nums.length;
    if (n === 0) return [-1, -1];

    const prefMinVal = new Array<number>(n);
    const prefMinIdx = new Array<number>(n);
    const prefMaxVal = new Array<number>(n);
    const prefMaxIdx = new Array<number>(n);

    for (let i = 0; i < n; i++) {
        if (i === 0) {
            prefMinVal[i] = nums[i];
            prefMinIdx[i] = i;
            prefMaxVal[i] = nums[i];
            prefMaxIdx[i] = i;
        } else {
            if (nums[i] < prefMinVal[i - 1]) {
                prefMinVal[i] = nums[i];
                prefMinIdx[i] = i;
            } else {
                prefMinVal[i] = prefMinVal[i - 1];
                prefMinIdx[i] = prefMinIdx[i - 1];
            }

            if (nums[i] > prefMaxVal[i - 1]) {
                prefMaxVal[i] = nums[i];
                prefMaxIdx[i] = i;
            } else {
                prefMaxVal[i] = prefMaxVal[i - 1];
                prefMaxIdx[i] = prefMaxIdx[i - 1];
            }
        }
    }

    for (let i = 0; i < n; i++) {
        const j = i - indexDifference;
        if (j < 0) continue;

        const minVal = prefMinVal[j];
        const minIdx = prefMinIdx[j];
        if (Math.abs(nums[i] - minVal) >= valueDifference) {
            return [i, minIdx];
        }

        const maxVal = prefMaxVal[j];
        const maxIdx = prefMaxIdx[j];
        if (Math.abs(nums[i] - maxVal) >= valueDifference) {
            return [i, maxIdx];
        }
    }

    return [-1, -1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $indexDifference
     * @param Integer $valueDifference
     * @return Integer[]
     */
    function findIndices($nums, $indexDifference, $valueDifference) {
        $n = count($nums);
        // Quick check when both differences are zero: any index works.
        if ($indexDifference == 0 && $valueDifference == 0) {
            return [0, 0];
        }

        // Prefix minimum values and their indices
        $prefMinVal = [];
        $prefMinIdx = [];
        // Prefix maximum values and their indices
        $prefMaxVal = [];
        $prefMaxIdx = [];

        for ($i = 0; $i < $n; ++$i) {
            if ($i == 0) {
                $prefMinVal[$i] = $nums[$i];
                $prefMinIdx[$i] = $i;
                $prefMaxVal[$i] = $nums[$i];
                $prefMaxIdx[$i] = $i;
            } else {
                // Minimum
                if ($nums[$i] < $prefMinVal[$i - 1]) {
                    $prefMinVal[$i] = $nums[$i];
                    $prefMinIdx[$i] = $i;
                } else {
                    $prefMinVal[$i] = $prefMinVal[$i - 1];
                    $prefMinIdx[$i] = $prefMinIdx[$i - 1];
                }
                // Maximum
                if ($nums[$i] > $prefMaxVal[$i - 1]) {
                    $prefMaxVal[$i] = $nums[$i];
                    $prefMaxIdx[$i] = $i;
                } else {
                    $prefMaxVal[$i] = $prefMaxVal[$i - 1];
                    $prefMaxIdx[$i] = $prefMaxIdx[$i - 1];
                }
            }
        }

        for ($i = 0; $i < $n; ++$i) {
            $left = $i - $indexDifference;
            if ($left >= 0) {
                // Check against prefix minimum
                $minVal = $prefMinVal[$left];
                $minIdx = $prefMinIdx[$left];
                if (abs($nums[$i] - $minVal) >= $valueDifference) {
                    return [$i, $minIdx];
                }
                // Check against prefix maximum
                $maxVal = $prefMaxVal[$left];
                $maxIdx = $prefMaxIdx[$left];
                if (abs($nums[$i] - $maxVal) >= $valueDifference) {
                    return [$i, $maxIdx];
                }
            }
        }

        return [-1, -1];
    }
}
```

## Swift

```swift
class Solution {
    func findIndices(_ nums: [Int], _ indexDifference: Int, _ valueDifference: Int) -> [Int] {
        let n = nums.count
        if n == 0 { return [-1, -1] }
        
        var prefMinIdx = Array(repeating: 0, count: n)
        var prefMaxIdx = Array(repeating: 0, count: n)
        var prefMinVal = Array(repeating: 0, count: n)
        var prefMaxVal = Array(repeating: 0, count: n)
        
        prefMinIdx[0] = 0
        prefMaxIdx[0] = 0
        prefMinVal[0] = nums[0]
        prefMaxVal[0] = nums[0]
        
        if n > 1 {
            for i in 1..<n {
                if nums[i] < prefMinVal[i - 1] {
                    prefMinVal[i] = nums[i]
                    prefMinIdx[i] = i
                } else {
                    prefMinVal[i] = prefMinVal[i - 1]
                    prefMinIdx[i] = prefMinIdx[i - 1]
                }
                
                if nums[i] > prefMaxVal[i - 1] {
                    prefMaxVal[i] = nums[i]
                    prefMaxIdx[i] = i
                } else {
                    prefMaxVal[i] = prefMaxVal[i - 1]
                    prefMaxIdx[i] = prefMaxIdx[i - 1]
                }
            }
        }
        
        for i in 0..<n {
            let left = i - indexDifference
            if left >= 0 {
                let minIdx = prefMinIdx[left]
                if abs(nums[i] - nums[minIdx]) >= valueDifference {
                    return [i, minIdx]
                }
                let maxIdx = prefMaxIdx[left]
                if abs(nums[i] - nums[maxIdx]) >= valueDifference {
                    return [i, maxIdx]
                }
            }
        }
        
        return [-1, -1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findIndices(nums: IntArray, indexDifference: Int, valueDifference: Int): IntArray {
        val n = nums.size
        if (n == 0) return intArrayOf(-1, -1)

        val prefMinVal = IntArray(n)
        val prefMinIdx = IntArray(n)
        val prefMaxVal = IntArray(n)
        val prefMaxIdx = IntArray(n)

        for (i in 0 until n) {
            if (i == 0) {
                prefMinVal[i] = nums[i]
                prefMinIdx[i] = i
                prefMaxVal[i] = nums[i]
                prefMaxIdx[i] = i
            } else {
                if (nums[i] < prefMinVal[i - 1]) {
                    prefMinVal[i] = nums[i]
                    prefMinIdx[i] = i
                } else {
                    prefMinVal[i] = prefMinVal[i - 1]
                    prefMinIdx[i] = prefMinIdx[i - 1]
                }
                if (nums[i] > prefMaxVal[i - 1]) {
                    prefMaxVal[i] = nums[i]
                    prefMaxIdx[i] = i
                } else {
                    prefMaxVal[i] = prefMaxVal[i - 1]
                    prefMaxIdx[i] = prefMaxIdx[i - 1]
                }
            }
        }

        for (i in 0 until n) {
            val left = i - indexDifference
            if (left < 0) continue

            val minVal = prefMinVal[left]
            val idxMin = prefMinIdx[left]
            if (kotlin.math.abs(nums[i] - minVal) >= valueDifference) {
                return intArrayOf(idxMin, i)
            }

            val maxVal = prefMaxVal[left]
            val idxMax = prefMaxIdx[left]
            if (kotlin.math.abs(nums[i] - maxVal) >= valueDifference) {
                return intArrayOf(idxMax, i)
            }
        }

        return intArrayOf(-1, -1)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findIndices(List<int> nums, int indexDifference, int valueDifference) {
    int n = nums.length;

    // If valueDifference is zero, any pair with sufficient index distance works.
    if (valueDifference == 0) {
      if (indexDifference <= n - 1) {
        return [0, indexDifference];
      }
      return [-1, -1];
    }

    // Prefix minimums and maximums with their indices.
    List<int> prefMinVal = List.filled(n, 0);
    List<int> prefMinIdx = List.filled(n, 0);
    List<int> prefMaxVal = List.filled(n, 0);
    List<int> prefMaxIdx = List.filled(n, 0);

    int curMinVal = nums[0];
    int curMinIdx = 0;
    int curMaxVal = nums[0];
    int curMaxIdx = 0;

    for (int i = 0; i < n; ++i) {
      if (nums[i] < curMinVal) {
        curMinVal = nums[i];
        curMinIdx = i;
      }
      if (nums[i] > curMaxVal) {
        curMaxVal = nums[i];
        curMaxIdx = i;
      }
      prefMinVal[i] = curMinVal;
      prefMinIdx[i] = curMinIdx;
      prefMaxVal[i] = curMaxVal;
      prefMaxIdx[i] = curMaxIdx;
    }

    for (int i = 0; i < n; ++i) {
      int bound = i - indexDifference;
      if (bound < 0) continue;

      int minVal = prefMinVal[bound];
      int minIdx = prefMinIdx[bound];
      int maxVal = prefMaxVal[bound];
      int maxIdx = prefMaxIdx[bound];

      if ((nums[i] - minVal).abs() >= valueDifference) {
        return [i, minIdx];
      }
      if ((nums[i] - maxVal).abs() >= valueDifference) {
        return [i, maxIdx];
      }
    }

    return [-1, -1];
  }
}
```

## Golang

```go
func findIndices(nums []int, indexDifference int, valueDifference int) []int {
    n := len(nums)
    const INF = int(^uint(0) >> 1)

    minVal, minIdx := INF, -1
    maxVal, maxIdx := -INF, -1

    for i := 0; i < n; i++ {
        if i-indexDifference >= 0 {
            pos := i - indexDifference
            v := nums[pos]
            if v < minVal {
                minVal = v
                minIdx = pos
            }
            if v > maxVal {
                maxVal = v
                maxIdx = pos
            }
        }

        if minIdx != -1 {
            diff := nums[i] - minVal
            if diff < 0 {
                diff = -diff
            }
            if diff >= valueDifference {
                return []int{i, minIdx}
            }
            diff2 := nums[i] - maxVal
            if diff2 < 0 {
                diff2 = -diff2
            }
            if diff2 >= valueDifference {
                return []int{i, maxIdx}
            }
        }
    }
    return []int{-1, -1}
}
```

## Ruby

```ruby
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  return [0, 0] if index_difference == 0 && value_difference == 0

  min_val = nil
  max_val = nil
  min_idx = -1
  max_idx = -1

  (0...n).each do |i|
    j = i - index_difference
    if j >= 0
      val = nums[j]
      if min_val.nil? || val < min_val
        min_val = val
        min_idx = j
      end
      if max_val.nil? || val > max_val
        max_val = val
        max_idx = j
      end
    end

    unless min_val.nil?
      return [i, min_idx] if (nums[i] - min_val).abs >= value_difference
      return [i, max_idx] if (nums[i] - max_val).abs >= value_difference
    end
  end

  [-1, -1]
end
```

## Scala

```scala
object Solution {
    def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
        val n = nums.length
        var minVal = Int.MaxValue
        var minIdx = -1
        var maxVal = Int.MinValue
        var maxIdx = -1

        for (i <- 0 until n) {
            if (i - indexDifference >= 0) {
                val j = i - indexDifference
                val v = nums(j)
                if (v < minVal) { minVal = v; minIdx = j }
                if (v > maxVal) { maxVal = v; maxIdx = j }
            }

            if (minIdx != -1) {
                val diffMin = Math.abs(nums(i).toLong - minVal.toLong)
                if (diffMin >= valueDifference) return Array(minIdx, i)

                val diffMax = Math.abs(nums(i).toLong - maxVal.toLong)
                if (diffMax >= valueDifference) return Array(maxIdx, i)
            }
        }

        Array(-1, -1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        // If the required index distance is larger than any possible distance, impossible.
        if (index_difference as usize) > n.saturating_sub(1) {
            return vec![-1, -1];
        }
        // When value difference is zero and index condition can be satisfied, any single index works.
        if value_difference == 0 {
            return vec![0, 0];
        }

        let idx_diff = index_difference as usize;
        let val_diff = value_difference as i64;

        let mut min_val: i64 = i64::MAX;
        let mut min_idx: usize = 0;
        let mut max_val: i64 = i64::MIN;
        let mut max_idx: usize = 0;

        for i in 0..n {
            if i >= idx_diff {
                // Add the new candidate at position k into prefix statistics.
                let k = i - idx_diff;
                let v = nums[k] as i64;
                if v < min_val {
                    min_val = v;
                    min_idx = k;
                }
                if v > max_val {
                    max_val = v;
                    max_idx = k;
                }

                let cur = nums[i] as i64;
                if (cur - min_val).abs() >= val_diff {
                    return vec![i as i32, min_idx as i32];
                }
                if (cur - max_val).abs() >= val_diff {
                    return vec![i as i32, max_idx as i32];
                }
            } else if idx_diff == 0 {
                // For idx_diff == 0 we also need to consider the current element itself.
                let cur = nums[i] as i64;
                // Update min/max with the current element before checking.
                if cur < min_val {
                    min_val = cur;
                    min_idx = i;
                }
                if cur > max_val {
                    max_val = cur;
                    max_idx = i;
                }
                if (cur - min_val).abs() >= val_diff {
                    return vec![i as i32, min_idx as i32];
                }
                if (cur - max_val).abs() >= val_diff {
                    return vec![i as i32, max_idx as i32];
                }
            }
        }

        vec![-1, -1]
    }
}
```

## Racket

```racket
(define/contract (find-indices nums indexDifference valueDifference)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ([vec (list->vector nums)]
         [n   (vector-length vec)])
    (let loop ((i 0) (min-val (expt 2 60)) (max-val -1) (min-idx -1) (max-idx -1))
      (if (= i n)
          (list -1 -1)
          (let* ([k        (- i indexDifference)]
                 [has-new? (>= k 0)]
                 [val      (if has-new? (vector-ref vec k) 0)]
                 [new-min-val (if (and has-new? (< val min-val)) val min-val)]
                 [new-min-idx (if (and has-new? (< val min-val)) k   min-idx)]
                 [new-max-val (if (and has-new? (> val max-val)) val max-val)]
                 [new-max-idx (if (and has-new? (> val max-val)) k   max-idx)]
                 [cur        (vector-ref vec i)])
            (cond
              [(and (>= new-min-idx 0)
                    (>= (abs (- cur new-min-val)) valueDifference))
               (list i new-min-idx)]
              [(and (>= new-max-idx 0)
                    (>= (abs (- cur new-max-val)) valueDifference))
               (list i new-max-idx)]
              [else
               (loop (+ i 1) new-min-val new-max-val new-min-idx new-max-idx)]))))))
```

## Erlang

```erlang
-module(solution).
-export([find_indices/3]).

-spec find_indices(Nums :: [integer()], IndexDifference :: integer(), ValueDifference :: integer()) -> [integer()].
find_indices(Nums, IndexDiff, ValueDiff) ->
    NumTuple = list_to_tuple(Nums),
    N = tuple_size(NumTuple),
    loop(0, N, IndexDiff, ValueDiff, NumTuple, undefined, -1, undefined, -1).

loop(I, N, _IdxDiff, _ValDiff, _Tuple, _PrefMinVal, _PrefMinIdx, _PrefMaxVal, _PrefMaxIdx) when I >= N ->
    [-1, -1];
loop(I, N, IdxDiff, ValDiff, Tuple, PrefMinVal, PrefMinIdx, PrefMaxVal, PrefMaxIdx) ->
    % Add new eligible index to prefix if any
    {NewMinVal, NewMinIdx, NewMaxVal, NewMaxIdx} =
        case I - IdxDiff of
            K when K >= 0 ->
                ValK = element(K + 1, Tuple),
                {TmpMinVal, TmpMinIdx} =
                    case PrefMinVal of
                        undefined -> {ValK, K};
                        _ when ValK < PrefMinVal -> {ValK, K};
                        _ -> {PrefMinVal, PrefMinIdx}
                    end,
                {TmpMaxVal, TmpMaxIdx} =
                    case PrefMaxVal of
                        undefined -> {ValK, K};
                        _ when ValK > PrefMaxVal -> {ValK, K};
                        _ -> {PrefMaxVal, PrefMaxIdx}
                    end,
                {TmpMinVal, TmpMinIdx, TmpMaxVal, TmpMaxIdx};
            _ ->
                {PrefMinVal, PrefMinIdx, PrefMaxVal, PrefMaxIdx}
        end,
    CurrVal = element(I + 1, Tuple),
    case (NewMinIdx =/= -1) andalso (erlang:abs(CurrVal - NewMinVal) >= ValDiff) of
        true ->
            [I, NewMinIdx];
        false ->
            case (NewMaxIdx =/= -1) andalso (erlang:abs(CurrVal - NewMaxVal) >= ValDiff) of
                true -> [I, NewMaxIdx];
                false -> loop(I + 1, N, IdxDiff, ValDiff, Tuple,
                              NewMinVal, NewMinIdx, NewMaxVal, NewMaxIdx)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_indices(nums :: [integer], index_difference :: integer, value_difference :: integer) :: [integer]
  def find_indices(nums, index_difference, value_difference) do
    n = length(nums)
    arr = List.to_tuple(nums)

    init_acc = {nil, -1, nil, -1}

    result =
      Enum.reduce_while(0..(n - 1), init_acc, fn i,
                                                {pminv, pmini, pmaxv, pmaxi} ->
        if i - index_difference >= 0 do
          j = i - index_difference
          val = elem(arr, j)

          {new_min_v, new_min_i} =
            case pminv do
              nil -> {val, j}
              _ when val < pminv -> {val, j}
              _ -> {pminv, pmini}
            end

          {new_max_v, new_max_i} =
            case pmaxv do
              nil -> {val, j}
              _ when val > pmaxv -> {val, j}
              _ -> {pmaxv, pmaxi}
            end

          cur = elem(arr, i)

          if abs(cur - new_min_v) >= value_difference do
            {:halt, [new_min_i, i]}
          else
            if abs(cur - new_max_v) >= value_difference do
              {:halt, [new_max_i, i]}
            else
              {:cont, {new_min_v, new_min_i, new_max_v, new_max_i}}
            end
          end
        else
          {:cont, {pminv, pmini, pmaxv, pmaxi}}
        end
      end)

    case result do
      [i, j] -> [i, j]
      _ -> [-1, -1]
    end
  end
end
```
