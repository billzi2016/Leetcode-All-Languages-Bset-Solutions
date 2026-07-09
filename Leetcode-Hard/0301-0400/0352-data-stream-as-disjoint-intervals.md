# 0352. Data Stream as Disjoint Intervals

## Cpp

```cpp
class SummaryRanges {
public:
    SummaryRanges() {}
    
    void addNum(int value) {
        // Find the first interval with start > value
        auto it = intervals.lower_bound(value);
        
        // If previous interval exists and covers value, do nothing
        if (it != intervals.begin()) {
            auto prev = std::prev(it);
            if (prev->second >= value) return; // already covered
        }
        
        bool leftMerge = false, rightMerge = false;
        int newStart = value, newEnd = value;
        std::map<int,int>::iterator leftIt, rightIt;
        
        // Check left adjacency
        if (it != intervals.begin()) {
            leftIt = std::prev(it);
            if (leftIt->second + 1 == value) {
                leftMerge = true;
                newStart = leftIt->first;
            }
        }
        // Check right adjacency
        if (it != intervals.end() && it->first - 1 == value) {
            rightMerge = true;
            rightIt = it;
            newEnd = rightIt->second;
        }
        
        if (leftMerge && rightMerge) {
            // Merge three parts: left interval, value, right interval
            intervals.erase(leftIt);
            intervals.erase(rightIt);
            intervals[newStart] = newEnd;
        } else if (leftMerge) {
            // Extend left interval's end to value
            leftIt->second = value;
        } else if (rightMerge) {
            // Remove right interval and insert merged one starting at value
            intervals.erase(rightIt);
            intervals[newStart] = newEnd;
        } else {
            // New isolated interval
            intervals[value] = value;
        }
    }
    
    vector<vector<int>> getIntervals() {
        vector<vector<int>> res;
        res.reserve(intervals.size());
        for (const auto& p : intervals) {
            res.push_back({p.first, p.second});
        }
        return res;
    }
private:
    std::map<int,int> intervals; // key: start, value: end
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(value);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */
```

## Java

```java
import java.util.*;

class SummaryRanges {
    private final TreeMap<Integer, Integer> intervals;

    public SummaryRanges() {
        intervals = new TreeMap<>();
    }

    public void addNum(int value) {
        // Check if already covered by an existing interval
        Map.Entry<Integer, Integer> lower = intervals.floorEntry(value);
        if (lower != null && lower.getValue() >= value) {
            return;
        }

        int left = value;
        int right = value;

        boolean mergeLeft = false;
        boolean mergeRight = false;

        // Merge with left interval if adjacent
        if (lower != null && lower.getValue() == value - 1) {
            left = lower.getKey();
            mergeLeft = true;
        }

        // Merge with right interval if adjacent
        Map.Entry<Integer, Integer> higher = intervals.ceilingEntry(value);
        if (higher != null && higher.getKey() == value + 1) {
            right = higher.getValue();
            mergeRight = true;
        }

        // Remove old intervals that are merged
        if (mergeLeft) {
            intervals.remove(left);
        }
        if (mergeRight) {
            intervals.remove(value + 1);
        }

        // Insert the new/merged interval
        intervals.put(left, right);
    }

    public int[][] getIntervals() {
        int[][] res = new int[intervals.size()][2];
        int i = 0;
        for (Map.Entry<Integer, Integer> entry : intervals.entrySet()) {
            res[i][0] = entry.getKey();
            res[i][1] = entry.getValue();
            i++;
        }
        return res;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(value);
 * int[][] param_2 = obj.getIntervals();
 */
```

## Python

```python
class SummaryRanges(object):
    def __init__(self):
        self.nums = set()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.add(value)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        if not self.nums:
            return []
        sorted_vals = sorted(self.nums)
        intervals = []
        start = prev = sorted_vals[0]
        for v in sorted_vals[1:]:
            if v == prev + 1:
                prev = v
            else:
                intervals.append([start, prev])
                start = prev = v
        intervals.append([start, prev])
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
```

## Python3

```python
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def _find_position(self, value: int) -> int:
        lo, hi = 0, len(self.intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.intervals[mid][0] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def addNum(self, value: int) -> None:
        i = self._find_position(value)

        # Check if already covered by left interval
        if i > 0 and self.intervals[i - 1][1] >= value:
            return

        left_merge = (i > 0 and self.intervals[i - 1][1] + 1 == value)
        right_merge = (i < len(self.intervals) and self.intervals[i][0] - 1 == value)

        if left_merge and right_merge:
            # Merge both intervals
            self.intervals[i - 1][1] = self.intervals[i][1]
            del self.intervals[i]
        elif left_merge:
            self.intervals[i - 1][1] = value
        elif right_merge:
            self.intervals[i][0] = value
        else:
            self.intervals.insert(i, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return [interval[:] for interval in self.intervals]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

typedef struct {
    Interval *arr;
    int size;
    int capacity;
} SummaryRanges;

SummaryRanges* summaryRangesCreate() {
    SummaryRanges *obj = (SummaryRanges *)malloc(sizeof(SummaryRanges));
    obj->capacity = 4;
    obj->size = 0;
    obj->arr = (Interval *)malloc(obj->capacity * sizeof(Interval));
    return obj;
}

static void ensureCapacity(SummaryRanges *obj) {
    if (obj->size < obj->capacity) return;
    obj->capacity <<= 1;
    obj->arr = (Interval *)realloc(obj->arr, obj->capacity * sizeof(Interval));
}

void summaryRangesAddNum(SummaryRanges* obj, int value) {
    // binary search for first interval with start > value
    int l = 0, r = obj->size;
    while (l < r) {
        int m = (l + r) >> 1;
        if (obj->arr[m].start > value)
            r = m;
        else
            l = m + 1;
    }
    int idx = l; // insertion point

    // check if already covered by previous interval
    if (idx > 0 && obj->arr[idx - 1].end >= value) {
        return; // already present
    }

    int leftMerge = (idx > 0 && obj->arr[idx - 1].end + 1 == value);
    int rightMerge = (idx < obj->size && obj->arr[idx].start - 1 == value);

    if (leftMerge && rightMerge) {
        // merge three parts: previous interval, value, next interval
        obj->arr[idx - 1].end = obj->arr[idx].end;
        // remove idx interval
        for (int i = idx; i < obj->size - 1; ++i)
            obj->arr[i] = obj->arr[i + 1];
        obj->size--;
    } else if (leftMerge) {
        obj->arr[idx - 1].end = value;
    } else if (rightMerge) {
        obj->arr[idx].start = value;
    } else {
        // insert new interval [value, value] at idx
        ensureCapacity(obj);
        for (int i = obj->size; i > idx; --i)
            obj->arr[i] = obj->arr[i - 1];
        obj->arr[idx].start = value;
        obj->arr[idx].end = value;
        obj->size++;
    }
}

int** summaryRangesGetIntervals(SummaryRanges* obj, int* retSize, int** retColSize) {
    *retSize = obj->size;
    if (obj->size == 0) {
        *retColSize = NULL;
        return NULL;
    }

    int **res = (int **)malloc(obj->size * sizeof(int *));
    *retColSize = (int *)malloc(obj->size * sizeof(int));

    for (int i = 0; i < obj->size; ++i) {
        res[i] = (int *)malloc(2 * sizeof(int));
        res[i][0] = obj->arr[i].start;
        res[i][1] = obj->arr[i].end;
        (*retColSize)[i] = 2;
    }
    return res;
}

void summaryRangesFree(SummaryRanges* obj) {
    if (!obj) return;
    free(obj->arr);
    free(obj);
}

/**
 * Your SummaryRanges struct will be instantiated and called as such:
 * SummaryRanges* obj = summaryRangesCreate();
 * summaryRangesAddNum(obj, value);
 *
 * int** param_2 = summaryRangesGetIntervals(obj, retSize, retColSize);
 *
 * summaryRangesFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class SummaryRanges {
    private readonly SortedSet<int> _values;

    public SummaryRanges() {
        _values = new SortedSet<int>();
    }
    
    public void AddNum(int value) {
        _values.Add(value);
    }
    
    public int[][] GetIntervals() {
        var result = new List<int[]>();
        if (_values.Count == 0) return result.ToArray();

        int start = -1, prev = -2;
        foreach (int v in _values) {
            if (start == -1) {
                start = prev = v;
                continue;
            }
            if (v == prev + 1) {
                prev = v; // extend current interval
            } else {
                result.Add(new int[] { start, prev });
                start = prev = v;
            }
        }
        result.Add(new int[] { start, prev });
        return result.ToArray();
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.AddNum(value);
 * int[][] param_2 = obj.GetIntervals();
 */
```

## Javascript

```javascript
var SummaryRanges = function() {
    this.intervals = [];
};

/**
 * @param {number} value
 * @return {void}
 */
SummaryRanges.prototype.addNum = function(value) {
    const arr = this.intervals;
    let lo = 0, hi = arr.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (arr[mid][0] > value) hi = mid;
        else lo = mid + 1;
    }
    const i = lo; // first interval with start > value
    const prevIdx = i - 1;

    // If value already covered by previous interval, do nothing
    if (prevIdx >= 0 && arr[prevIdx][0] <= value && arr[prevIdx][1] >= value) {
        return;
    }

    const leftMerge = prevIdx >= 0 && arr[prevIdx][1] + 1 === value;
    const rightMerge = i < arr.length && arr[i][0] - 1 === value;

    if (leftMerge && rightMerge) {
        // Merge three parts
        arr[prevIdx][1] = arr[i][1];
        arr.splice(i, 1);
    } else if (leftMerge) {
        arr[prevIdx][1] = value;
    } else if (rightMerge) {
        arr[i][0] = value;
    } else {
        arr.splice(i, 0, [value, value]);
    }
};

/**
 * @return {number[][]}
 */
SummaryRanges.prototype.getIntervals = function() {
    // Return a shallow copy to prevent external mutation
    return this.intervals.map(pair => [pair[0], pair[1]]);
};
```

## Typescript

```typescript
class SummaryRanges {
    private intervals: number[][];

    constructor() {
        this.intervals = [];
    }

    addNum(value: number): void {
        const n = this.intervals.length;
        if (n === 0) {
            this.intervals.push([value, value]);
            return;
        }

        // binary search for the first interval with start >= value
        let lo = 0, hi = n;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (this.intervals[mid][0] < value) lo = mid + 1;
            else hi = mid;
        }
        const i = lo; // position to insert or merge

        // check left interval
        let leftIdx = i - 1;
        let rightIdx = i;

        // if value already covered by left interval
        if (leftIdx >= 0 && this.intervals[leftIdx][1] >= value) {
            return;
        }

        const leftMerge = leftIdx >= 0 && this.intervals[leftIdx][1] === value - 1;
        const rightMerge = rightIdx < n && this.intervals[rightIdx][0] === value + 1;

        if (leftMerge && rightMerge) {
            // merge three parts
            const newStart = this.intervals[leftIdx][0];
            const newEnd = this.intervals[rightIdx][1];
            // remove right interval first
            this.intervals.splice(rightIdx, 1);
            // replace left interval with merged one
            this.intervals[leftIdx] = [newStart, newEnd];
        } else if (leftMerge) {
            // extend left interval
            this.intervals[leftIdx][1] = value;
        } else if (rightMerge) {
            // extend right interval to the left
            const newEnd = this.intervals[rightIdx][1];
            this.intervals.splice(rightIdx, 1);
            this.intervals.splice(i, 0, [value, newEnd]);
        } else {
            // insert as a new interval
            this.intervals.splice(i, 0, [value, value]);
        }
    }

    getIntervals(): number[][] {
        return this.intervals.map(interval => [interval[0], interval[1]]);
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = new SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
```

## Php

```php
class SummaryRanges {
    private $intervals;

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->intervals = [];
    }

    /**
     * @param Integer $value
     * @return NULL
     */
    function addNum($value) {
        $n = count($this->intervals);
        // binary search for first interval with left >= value
        $low = 0;
        $high = $n;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->intervals[$mid][0] < $value) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        $idx = $low; // insertion point

        $mergedLeft = $value;
        $mergedRight = $value;
        $removeStart = $idx;
        $removeCount = 0;

        // check left interval
        if ($idx > 0) {
            $leftInterval = $this->intervals[$idx - 1];
            if ($leftInterval[1] >= $value) {
                return; // already covered
            }
            if ($leftInterval[1] + 1 == $value) {
                $mergedLeft = $leftInterval[0];
                $removeStart = $idx - 1;
                $removeCount++;
            }
        }

        // check right interval (original idx)
        if ($idx < $n) {
            $rightInterval = $this->intervals[$idx];
            if ($rightInterval[0] <= $value && $rightInterval[1] >= $value) {
                return; // already covered
            }
            if ($rightInterval[0] - 1 == $value) {
                $mergedRight = $rightInterval[1];
                $removeCount++;
            }
        }

        // remove intervals that will be merged
        if ($removeCount > 0) {
            array_splice($this->intervals, $removeStart, $removeCount);
        }

        // insert the new (or merged) interval
        $newInterval = [$mergedLeft, $mergedRight];
        array_splice($this->intervals, $removeStart, 0, [$newInterval]);
    }

    /**
     * @return Integer[][]
     */
    function getIntervals() {
        return $this->intervals;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * $obj = new SummaryRanges();
 * $obj->addNum($value);
 * $ret_2 = $obj->getIntervals();
 */
```

## Swift

```swift
class SummaryRanges {
    private var intervals: [[Int]] = []
    
    init() { }
    
    func addNum(_ value: Int) {
        if intervals.isEmpty {
            intervals.append([value, value])
            return
        }
        
        // binary search for first interval with start > value
        var lo = 0
        var hi = intervals.count
        while lo < hi {
            let mid = (lo + hi) >> 1
            if intervals[mid][0] <= value {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        let idx = lo               // first interval with start > value
        let leftIdx = idx - 1
        let rightIdx = idx
        
        // If value already covered by left interval, do nothing
        if leftIdx >= 0 && intervals[leftIdx][0] <= value && intervals[leftIdx][1] >= value {
            return
        }
        
        let leftMerge = leftIdx >= 0 && intervals[leftIdx][1] + 1 == value
        let rightMerge = rightIdx < intervals.count && intervals[rightIdx][0] - 1 == value
        
        if leftMerge && rightMerge {
            // Merge three parts into one interval
            let newLeft = intervals[leftIdx][0]
            let newRight = intervals[rightIdx][1]
            intervals.remove(at: rightIdx)   // remove right first
            intervals.remove(at: leftIdx)
            intervals.insert([newLeft, newRight], at: leftIdx)
        } else if leftMerge {
            intervals[leftIdx][1] = value
        } else if rightMerge {
            intervals[rightIdx][0] = value
        } else {
            intervals.insert([value, value], at: idx)
        }
    }
    
    func getIntervals() -> [[Int]] {
        return intervals
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let obj = SummaryRanges()
 * obj.addNum(value)
 * let ret_2: [[Int]] = obj.getIntervals()
 */
```

## Kotlin

```kotlin
import java.util.TreeMap

class SummaryRanges() {

    private val intervals = TreeMap<Int, Int>()

    fun addNum(value: Int) {
        var left = value
        var right = value

        // Check interval with greatest start <= value
        val lowerKey = intervals.floorKey(value)
        if (lowerKey != null) {
            val lowerEnd = intervals[lowerKey]!!
            if (value <= lowerEnd) {
                return  // already covered
            }
            if (lowerEnd + 1 == value) {
                left = lowerKey
                intervals.remove(lowerKey)
            }
        }

        // Check interval with smallest start >= value
        val higherKey = intervals.ceilingKey(value)
        if (higherKey != null && higherKey == value + 1) {
            right = intervals[higherKey]!!
            intervals.remove(higherKey)
        }

        intervals[left] = right
    }

    fun getIntervals(): Array<IntArray> {
        val result = ArrayList<IntArray>(intervals.size)
        for ((start, end) in intervals) {
            result.add(intArrayOf(start, end))
        }
        return result.toTypedArray()
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
```

## Dart

```dart
class SummaryRanges {
  List<List<int>> _intervals = [];

  SummaryRanges() {}

  void addNum(int value) {
    int n = _intervals.length;
    if (n == 0) {
      _intervals.add([value, value]);
      return;
    }

    // Find first interval with start > value using binary search
    int left = 0, right = n;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (_intervals[mid][0] <= value) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    int idx = left; // first interval with start > value

    // Check if value is already covered by previous interval
    if (idx > 0 && _intervals[idx - 1][1] >= value) {
      return;
    }

    bool mergedLeft = false;
    // Merge with previous interval if adjacent
    if (idx > 0 && _intervals[idx - 1][1] + 1 == value) {
      _intervals[idx - 1][1] = value;
      mergedLeft = true;
    }

    // Check if value is already covered by next interval
    if (idx < n && _intervals[idx][0] <= value) {
      return;
    }

    bool mergedRight = false;
    // Merge with next interval if adjacent
    if (idx < n && _intervals[idx][0] - 1 == value) {
      if (mergedLeft) {
        // merge previous and next intervals
        _intervals[idx - 1][1] = _intervals[idx][1];
        _intervals.removeAt(idx);
      } else {
        _intervals[idx][0] = value;
      }
      mergedRight = true;
    }

    if (!mergedLeft && !mergedRight) {
      _intervals.insert(idx, [value, value]);
    }
  }

  List<List<int>> getIntervals() {
    // Return a deep copy to avoid external modifications
    return _intervals.map((e) => [e[0], e[1]]).toList();
  }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = SummaryRanges();
 * obj.addNum(value);
 * List<List<int>> param2 = obj.getIntervals();
 */
```

## Golang

```go
package main

import (
	"sort"
)

type SummaryRanges struct {
	data map[int]bool
}

func Constructor() SummaryRanges {
	return SummaryRanges{data: make(map[int]bool)}
}

func (this *SummaryRanges) AddNum(value int) {
	if !this.data[value] {
		this.data[value] = true
	}
}

func (this *SummaryRanges) GetIntervals() [][]int {
	if len(this.data) == 0 {
		return [][]int{}
	}
	keys := make([]int, 0, len(this.data))
	for k := range this.data {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	var res [][]int
	start, end := keys[0], keys[0]
	for i := 1; i < len(keys); i++ {
		if keys[i] == end+1 {
			end = keys[i]
		} else {
			res = append(res, []int{start, end})
			start, end = keys[i], keys[i]
		}
	}
	res = append(res, []int{start, end})
	return res
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(value);
 * param_2 := obj.GetIntervals();
 */
```

## Ruby

```ruby
class SummaryRanges
    def initialize()
        @intervals = []
    end

=begin
    :type value: Integer
    :rtype: Void
=end
    def add_num(value)
        intervals = @intervals
        # binary search for first interval with start > value
        left = 0
        right = intervals.length
        while left < right
            mid = (left + right) / 2
            if intervals[mid][0] > value
                right = mid
            else
                left = mid + 1
            end
        end
        i = left

        # already covered by previous interval?
        if i > 0 && intervals[i-1][0] <= value && intervals[i-1][1] >= value
            return
        end

        merge_left = (i > 0 && intervals[i-1][1] + 1 == value)
        merge_right = (i < intervals.length && intervals[i][0] - 1 == value)

        if merge_left && merge_right
            new_left = intervals[i-1][0]
            new_right = intervals[i][1]
            intervals.delete_at(i)          # remove right interval
            intervals[i-1] = [new_left, new_right]  # replace left with merged
        elsif merge_left
            intervals[i-1][1] += 1
        elsif merge_right
            intervals[i][0] -= 1
        else
            intervals.insert(i, [value, value])
        end
    end

=begin
    :rtype: Integer[][]
=end
    def get_intervals()
        @intervals.map { |int| int.clone }
    end
end
```

## Scala

```scala
class SummaryRanges() {
  private val intervals = new java.util.TreeMap[Int, Int]()

  def addNum(value: Int): Unit = {
    // If the value is already covered by an existing interval, do nothing.
    val lower = intervals.floorEntry(value)
    if (lower != null && lower.getValue >= value) return

    var left = value
    var right = value

    // Merge with the interval on the left if adjacent.
    if (lower != null && lower.getValue == value - 1) {
      left = lower.getKey
      intervals.remove(lower.getKey)
    }

    // Merge with the interval on the right if adjacent.
    val higher = intervals.ceilingEntry(value + 1)
    if (higher != null && higher.getKey == value + 1) {
      right = higher.getValue
      intervals.remove(higher.getKey)
    }

    intervals.put(left, right)
  }

  def getIntervals(): Array[Array[Int]] = {
    import scala.jdk.CollectionConverters._
    val res = new scala.collection.mutable.ArrayBuffer[Array[Int]]()
    for (e <- intervals.entrySet().asScala) {
      res += Array(e.getKey, e.getValue)
    }
    res.toArray
  }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * val obj = new SummaryRanges()
 * obj.addNum(value)
 * val param_2 = obj.getIntervals()
 */
```

## Rust

```rust
use std::collections::BTreeMap;

pub struct SummaryRanges {
    intervals: BTreeMap<i32, i32>,
}

impl SummaryRanges {
    pub fn new() -> Self {
        SummaryRanges {
            intervals: BTreeMap::new(),
        }
    }

    pub fn add_num(&mut self, value: i32) {
        // If already covered, do nothing.
        if let Some((&l, &r)) = self.intervals.range(..=value).next_back() {
            if r >= value {
                return;
            }
        }

        let mut left = value;
        let mut right = value;

        // Merge with left interval if adjacent.
        if let Some((&l, &r)) = self.intervals.range(..=value).next_back() {
            if r == value - 1 {
                left = l;
                self.intervals.remove(&l);
            }
        }

        // Merge with right interval if adjacent.
        if let Some((&l2, &r2)) = self.intervals.range((value + 1)..).next() {
            if l2 == value + 1 {
                right = r2;
                self.intervals.remove(&l2);
            }
        }

        self.intervals.insert(left, right);
    }

    pub fn get_intervals(&self) -> Vec<Vec<i32>> {
        self.intervals
            .iter()
            .map(|(&l, &r)| vec![l, r])
            .collect()
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * let mut obj = SummaryRanges::new();
 * obj.add_num(value);
 * let ret_2: Vec<Vec<i32>> = obj.get_intervals();
 */
```

## Racket

```racket
(require racket/list)

(define summary-ranges%
  (class object%
    (super-new)
    (define intervals '())

    ; add-num : exact-integer? -> void?
    (define/public (add-num value)
      (let* ((n (length intervals))
             ;; find first interval whose left bound > value
             (pos (let loop ((i 0) (rest intervals))
                    (if (or (null? rest) (> (first (car rest)) value))
                        i
                        (loop (+ i 1) (cdr rest)))))
             (prev (if (> pos 0) (list-ref intervals (- pos 1)) #f))
             (next (if (< pos n) (list-ref intervals pos) #f)))
        ;; already covered?
        (cond
          [(and prev (<= (first prev) value (second prev))) (void)]
          [(and next (<= (first next) value (second next))) (void)]
          [else
           (let ((left-merge  (and prev (= (+ (second prev) 1) value)))
                 (right-merge (and next (= (- (first next) 1) value))))
             (cond
               [(and left-merge right-merge)
                ;; merge both intervals
                (set! intervals
                      (append (take intervals (- pos 1))
                              (list (list (first prev) (second next)))
                              (drop intervals (+ pos 1))))]
               [left-merge
                ;; extend previous interval
                (set! intervals
                      (append (take intervals (- pos 1))
                              (list (list (first prev) value))
                              (drop intervals pos)))]
               [right-merge
                ;; extend next interval
                (set! intervals
                      (append (take intervals pos)
                              (list (list value (second next)))
                              (drop intervals (+ pos 1))))]
               [else
                ;; insert new singleton interval
                (set! intervals
                      (append (take intervals pos)
                              (list (list value value))
                              (drop intervals pos)))])]))))

    ; get-intervals : -> (listof (listof exact-integer?))
    (define/public (get-intervals)
      intervals)))
```

## Erlang

```erlang
-module(summaryranges).
-export([summary_ranges_init_/0,
         summary_ranges_add_num/1,
         summary_ranges_get_intervals/0]).

%% Initialize the data structure.
summary_ranges_init_() ->
    put(intervals, []),
    ok.

%% Add a number to the stream.
summary_ranges_add_num(Value) when is_integer(Value) ->
    Intervals = case get(intervals) of
                   undefined -> [];
                   I -> I
               end,
    NewIntervals = insert_interval(Intervals, Value),
    put(intervals, NewIntervals),
    ok.

%% Retrieve the current list of disjoint intervals.
summary_ranges_get_intervals() ->
    Intervals = case get(intervals) of
                   undefined -> [];
                   I -> I
               end,
    lists:map(fun({L,R}) -> [L,R] end, Intervals).

%% Internal helper to insert a value into the sorted interval list.
insert_interval([], V) ->
    [{V,V}];
insert_interval([ {L,R}=I | Rest ], V) ->
    Cond =
        if
            V < L-1 ->
                %% Insert before current interval.
                [{V,V}, I | Rest];
            V == L-1 ->
                %% Extend current interval to the left.
                [{V,R} | Rest];
            V >= L, V =< R ->
                %% Value already covered.
                [I | Rest];
            V == R+1 ->
                %% Extend current interval to the right; may merge with next.
                case Rest of
                    [{L2,R2}|RestTail] when L2 == V+1 ->
                        [{L,R2} | RestTail];
                    _ ->
                        [{L,V} | Rest]
                end;
            true ->
                %% Continue searching in the rest of the list.
                [I | insert_interval(Rest, V)]
        end,
    Cond.
```

## Elixir

```elixir
defmodule SummaryRanges do
  @spec init_() :: any
  def init_() do
    Process.put(:summary_set, MapSet.new())
    :ok
  end

  @spec add_num(value :: integer) :: any
  def add_num(value) do
    set = Process.get(:summary_set, MapSet.new())
    Process.put(:summary_set, MapSet.put(set, value))
    :ok
  end

  @spec get_intervals() :: [[integer]]
  def get_intervals() do
    values =
      Process.get(:summary_set, MapSet.new())
      |> MapSet.to_list()
      |> Enum.sort()

    {rev_intervals, left, right} =
      Enum.reduce(values, {[], nil, nil}, fn v, {list, l, r} ->
        cond do
          l == nil ->
            {list, v, v}

          v == r + 1 ->
            {list, l, v}

          true ->
            {[ [l, r] | list], v, v}
        end
      end)

    intervals =
      if left != nil do
        [ [left, right] | rev_intervals ]
      else
        rev_intervals
      end

    Enum.reverse(intervals)
  end
end
```
