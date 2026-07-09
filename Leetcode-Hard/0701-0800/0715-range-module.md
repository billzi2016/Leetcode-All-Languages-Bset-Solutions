# 0715. Range Module

## Cpp

```cpp
class RangeModule {
public:
    std::map<int, int> ranges;
    
    RangeModule() {}
    
    void addRange(int left, int right) {
        if (left >= right) return;
        auto it = ranges.lower_bound(left);
        // Merge with previous interval if overlapping or adjacent
        if (it != ranges.begin()) {
            auto prev = std::prev(it);
            if (prev->second >= left) { // overlap or touch
                left = std::min(left, prev->first);
                right = std::max(right, prev->second);
                it = ranges.erase(prev);
            }
        }
        // Merge with following intervals that intersect or touch
        while (it != ranges.end() && it->first <= right) {
            right = std::max(right, it->second);
            left = std::min(left, it->first);
            it = ranges.erase(it);
        }
        ranges[left] = right;
    }
    
    bool queryRange(int left, int right) {
        if (left >= right) return false;
        auto it = ranges.upper_bound(left);
        if (it == ranges.begin()) return false;
        --it;
        return it->second >= right;
    }
    
    void removeRange(int left, int right) {
        if (left >= right) return;
        // Handle interval that may start before 'left' and overlap
        auto it = ranges.lower_bound(left);
        if (it != ranges.begin()) {
            auto prev = std::prev(it);
            if (prev->second > left) { // overlaps
                int l = prev->first, r = prev->second;
                ranges.erase(prev);
                if (l < left) ranges[l] = left;
                if (r > right) ranges[right] = r;
            }
        }
        // Remove or trim intervals that start within [left, right)
        it = ranges.lower_bound(left);
        while (it != ranges.end() && it->first < right) {
            int l = it->first, r = it->second;
            auto nxt = std::next(it);
            ranges.erase(it);
            if (r > right) {
                ranges[right] = r;
                break; // remaining intervals start after 'right'
            }
            it = nxt;
        }
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */
```

## Java

```java
import java.util.*;

class RangeModule {
    private final TreeMap<Integer, Integer> map;

    public RangeModule() {
        map = new TreeMap<>();
    }

    public void addRange(int left, int right) {
        if (left >= right) return;
        int newLeft = left;
        int newRight = right;

        Map.Entry<Integer, Integer> entry = map.floorEntry(left);
        if (entry != null && entry.getValue() >= left) {
            newLeft = Math.min(entry.getKey(), newLeft);
            newRight = Math.max(entry.getValue(), newRight);
            map.remove(entry.getKey());
        }

        Map.Entry<Integer, Integer> cur = map.ceilingEntry(left);
        while (cur != null && cur.getKey() <= newRight) {
            newRight = Math.max(newRight, cur.getValue());
            map.remove(cur.getKey());
            cur = map.ceilingEntry(left);
        }
        map.put(newLeft, newRight);
    }

    public boolean queryRange(int left, int right) {
        if (left >= right) return true;
        Map.Entry<Integer, Integer> entry = map.floorEntry(left);
        return entry != null && entry.getValue() >= right;
    }

    public void removeRange(int left, int right) {
        if (left >= right) return;

        // Overlap on the left side
        Map.Entry<Integer, Integer> entry = map.floorEntry(left);
        if (entry != null && entry.getValue() > left) {
            int s = entry.getKey();
            int e = entry.getValue();
            if (e > right) { // split into two intervals
                if (s < left) map.put(s, left);
                else map.remove(s);
                map.put(right, e);
                return;
            } else {
                if (s < left) map.put(s, left);
                else map.remove(s);
            }
        }

        // Remove fully covered intervals
        NavigableMap<Integer, Integer> sub = map.subMap(left, true, right, false);
        List<Integer> keys = new ArrayList<>(sub.keySet());
        for (int k : keys) {
            map.remove(k);
        }

        // Overlap on the right side
        entry = map.floorEntry(right);
        if (entry != null && entry.getValue() > right) {
            int s = entry.getKey();
            int e = entry.getValue();
            map.remove(s);
            map.put(right, e);
        }
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
```

## Python

```python
import bisect

class RangeModule(object):
    def __init__(self):
        self.intervals = []  # list of [start, end), non-overlapping and sorted

    def addRange(self, left, right):
        i = bisect.bisect_left(self.intervals, [left, left])
        if i != 0 and self.intervals[i - 1][1] >= left:
            i -= 1
        while i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            del self.intervals[i]
        self.intervals.insert(i, [left, right])

    def queryRange(self, left, right):
        i = bisect.bisect_right(self.intervals, [left, float('inf')]) - 1
        if i >= 0 and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True
        return False

    def removeRange(self, left, right):
        i = bisect.bisect_left(self.intervals, [left, left])
        # handle possible overlap with previous interval
        if i != 0 and self.intervals[i - 1][1] > left:
            prev = self.intervals[i - 1]
            if prev[1] > right:
                # split into two intervals
                self.intervals[i - 1][1] = left
                self.intervals.insert(i, [right, prev[1]])
                return
            else:
                # trim the end of previous interval
                self.intervals[i - 1][1] = left

        while i < len(self.intervals) and self.intervals[i][0] < right:
            cur = self.intervals[i]
            if cur[1] <= right:
                del self.intervals[i]
            else:
                # trim the start of current interval
                self.intervals[i][0] = right
                break
```

## Python3

```python
import bisect

class RangeModule:
    def __init__(self):
        self.intervals = []  # list of [l, r), non‑overlapping and sorted by l

    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.intervals, [left, left])
        if i != 0 and self.intervals[i - 1][1] >= left:
            i -= 1
        new_l, new_r = left, right
        while i < len(self.intervals) and self.intervals[i][0] <= new_r:
            new_l = min(new_l, self.intervals[i][0])
            new_r = max(new_r, self.intervals[i][1])
            del self.intervals[i]
        self.intervals.insert(i, [new_l, new_r])

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.intervals, [left, float('inf')]) - 1
        if i >= 0 and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.intervals, [left, left])
        if i != 0 and self.intervals[i - 1][1] > left:
            i -= 1
        while i < len(self.intervals) and self.intervals[i][0] < right:
            cur_l, cur_r = self.intervals[i]
            # No overlap (shouldn't happen due to loop condition)
            if cur_r <= left:
                i += 1
                continue
            # Case: interval fully inside removal range
            if cur_l >= left and cur_r <= right:
                del self.intervals[i]
                continue
            # Case: interval covers removal range completely -> split
            if cur_l < left and cur_r > right:
                self.intervals[i][1] = left
                self.intervals.insert(i + 1, [right, cur_r])
                break
            # Trim right part
            if cur_l < left and cur_r <= right:
                self.intervals[i][1] = left
                i += 1
                continue
            # Trim left part
            if cur_l >= left and cur_r > right:
                self.intervals[i][0] = right
                break
        # done
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int left;
    int right;
} Interval;

typedef struct {
    Interval *arr;
    int size;
    int capacity;
} RangeModule;

RangeModule* rangeModuleCreate() {
    RangeModule *obj = (RangeModule *)malloc(sizeof(RangeModule));
    obj->capacity = 4;
    obj->size = 0;
    obj->arr = (Interval *)malloc(obj->capacity * sizeof(Interval));
    return obj;
}

static void ensureCapacity(RangeModule *obj, int needed) {
    if (obj->capacity >= needed) return;
    int newCap = obj->capacity * 2 + 4;
    while (newCap < needed) newCap <<= 1;
    obj->arr = (Interval *)realloc(obj->arr, newCap * sizeof(Interval));
    obj->capacity = newCap;
}

void rangeModuleAddRange(RangeModule* obj, int left, int right) {
    if (left >= right) return;
    int i = 0;
    while (i < obj->size && obj->arr[i].right < left) i++;
    int start = i;
    int newL = left, newR = right;
    while (i < obj->size && obj->arr[i].left <= right) {
        if (obj->arr[i].left < newL) newL = obj->arr[i].left;
        if (obj->arr[i].right > newR) newR = obj->arr[i].right;
        i++;
    }
    int afterCount = obj->size - i; // intervals after the merged block
    ensureCapacity(obj, start + 1 + afterCount);
    memmove(&obj->arr[start + 1], &obj->arr[i], afterCount * sizeof(Interval));
    obj->arr[start].left = newL;
    obj->arr[start].right = newR;
    obj->size = start + 1 + afterCount;
}

bool rangeModuleQueryRange(RangeModule* obj, int left, int right) {
    if (left >= right) return false;
    int lo = 0, hi = obj->size - 1, idx = -1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (obj->arr[mid].left <= left) {
            idx = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    if (idx == -1) return false;
    return obj->arr[idx].right >= right;
}

void rangeModuleRemoveRange(RangeModule* obj, int left, int right) {
    if (left >= right) return;
    int w = 0;
    for (int i = 0; i < obj->size; ++i) {
        Interval cur = obj->arr[i];
        if (cur.right <= left || cur.left >= right) {
            // No overlap
            obj->arr[w++] = cur;
        } else {
            if (cur.left < left) {
                obj->arr[w].left = cur.left;
                obj->arr[w].right = left;
                w++;
            }
            if (cur.right > right) {
                obj->arr[w].left = right;
                obj->arr[w].right = cur.right;
                w++;
            }
        }
    }
    obj->size = w;
}

void rangeModuleFree(RangeModule* obj) {
    if (!obj) return;
    free(obj->arr);
    free(obj);
}
```

## Csharp

```csharp
public class RangeModule {
    private List<int[]> intervals;

    public RangeModule() {
        intervals = new List<int[]>();
    }

    public void AddRange(int left, int right) {
        if (left >= right) return;
        int i = 0;
        while (i < intervals.Count && intervals[i][1] < left) i++;

        int start = left;
        int end = right;
        int j = i;
        while (j < intervals.Count && intervals[j][0] <= right) {
            start = Math.Min(start, intervals[j][0]);
            end = Math.Max(end, intervals[j][1]);
            j++;
        }

        if (i == j) {
            intervals.Insert(i, new int[] { start, end });
        } else {
            intervals.RemoveRange(i, j - i);
            intervals.Insert(i, new int[] { start, end });
        }
    }

    public bool QueryRange(int left, int right) {
        if (left >= right) return false;
        int lo = 0, hi = intervals.Count - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (intervals[mid][0] > left)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        if (hi >= 0 && intervals[hi][0] <= left && intervals[hi][1] >= right)
            return true;
        return false;
    }

    public void RemoveRange(int left, int right) {
        if (left >= right) return;
        int startIdx = 0;
        while (startIdx < intervals.Count && intervals[startIdx][1] <= left) startIdx++;

        int endIdx = startIdx;
        while (endIdx < intervals.Count && intervals[endIdx][0] < right) endIdx++;

        List<int[]> newInts = new List<int[]>();
        for (int k = startIdx; k < endIdx; k++) {
            int curL = intervals[k][0];
            int curR = intervals[k][1];
            if (curL < left)
                newInts.Add(new int[] { curL, Math.Min(left, curR) });
            if (curR > right)
                newInts.Add(new int[] { Math.Max(right, curL), curR });
        }

        intervals.RemoveRange(startIdx, endIdx - startIdx);
        intervals.InsertRange(startIdx, newInts);
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.AddRange(left,right);
 * bool param_2 = obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */
```

## Javascript

```javascript
var RangeModule = function() {
    this.intervals = [];
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
RangeModule.prototype.addRange = function(left, right) {
    const res = [];
    let i = 0;
    const n = this.intervals.length;
    // add intervals before the new range
    while (i < n && this.intervals[i][1] < left) {
        res.push(this.intervals[i]);
        i++;
    }
    // merge overlapping intervals
    let start = left, end = right;
    while (i < n && this.intervals[i][0] <= right) {
        start = Math.min(start, this.intervals[i][0]);
        end = Math.max(end, this.intervals[i][1]);
        i++;
    }
    res.push([start, end]);
    // add the rest
    while (i < n) {
        res.push(this.intervals[i]);
        i++;
    }
    this.intervals = res;
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {boolean}
 */
RangeModule.prototype.queryRange = function(left, right) {
    let lo = 0, hi = this.intervals.length - 1, idx = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (this.intervals[mid][0] <= left) {
            idx = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return idx !== -1 && this.intervals[idx][1] >= right;
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
RangeModule.prototype.removeRange = function(left, right) {
    const res = [];
    for (const [l, r] of this.intervals) {
        if (r <= left || l >= right) {
            // no overlap
            res.push([l, r]);
        } else {
            if (l < left) res.push([l, left]);
            if (r > right) res.push([right, r]);
        }
    }
    this.intervals = res;
};
```

## Typescript

```typescript
class RangeModule {
    private ranges: [number, number][] = [];

    constructor() {}

    private bisectLeft(target: number): number {
        let lo = 0, hi = this.ranges.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (this.ranges[mid][0] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    addRange(left: number, right: number): void {
        let i = this.bisectLeft(left);
        if (i > 0 && this.ranges[i - 1][1] >= left) i--;

        let newL = left, newR = right;
        while (i < this.ranges.length && this.ranges[i][0] <= newR) {
            newL = Math.min(newL, this.ranges[i][0]);
            newR = Math.max(newR, this.ranges[i][1]);
            this.ranges.splice(i, 1);
        }
        this.ranges.splice(i, 0, [newL, newR]);
    }

    queryRange(left: number, right: number): boolean {
        const i = this.bisectLeft(left);
        if (i === 0) return false;
        const interval = this.ranges[i - 1];
        return interval[0] <= left && interval[1] >= right;
    }

    removeRange(left: number, right: number): void {
        let i = this.bisectLeft(left);
        if (i > 0 && this.ranges[i - 1][1] > left) i--;

        while (i < this.ranges.length && this.ranges[i][0] < right) {
            const cur = this.ranges[i];
            // No overlap (shouldn't happen due to loop condition)
            if (cur[1] <= left) { i++; continue; }

            if (cur[0] >= left && cur[1] <= right) {
                // Fully covered, remove interval
                this.ranges.splice(i, 1);
                continue;
            }
            if (cur[0] < left && cur[1] > right) {
                // Split into two intervals
                const rightPart: [number, number] = [right, cur[1]];
                this.ranges[i][1] = left;
                this.ranges.splice(i + 1, 0, rightPart);
                break;
            }
            if (cur[0] < left && cur[1] > left) {
                // Trim right side
                this.ranges[i][1] = left;
                i++;
                continue;
            }
            if (cur[0] < right && cur[1] > right) {
                // Trim left side
                this.ranges[i][0] = right;
                break;
            }
            i++;
        }
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * var obj = new RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

## Php

```php
<?php
class RangeModule {
    /**
     * @var array<int, array{0:int,1:int}>
     */
    private $intervals;

    function __construct() {
        $this->intervals = [];
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function addRange($left, $right) {
        $new = [];
        $i = 0;
        $n = count($this->intervals);
        // intervals completely before the new range
        while ($i < $n && $this->intervals[$i][1] < $left) {
            $new[] = $this->intervals[$i];
            $i++;
        }
        // merge overlapping or adjacent intervals
        $mergeLeft = $left;
        $mergeRight = $right;
        while ($i < $n && $this->intervals[$i][0] <= $right) {
            $mergeLeft = min($mergeLeft, $this->intervals[$i][0]);
            $mergeRight = max($mergeRight, $this->intervals[$i][1]);
            $i++;
        }
        $new[] = [$mergeLeft, $mergeRight];
        // remaining intervals
        while ($i < $n) {
            $new[] = $this->intervals[$i];
            $i++;
        }
        $this->intervals = $new;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function queryRange($left, $right) {
        $low = 0;
        $high = count($this->intervals) - 1;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->intervals[$mid][0] > $left) {
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        $idx = $high; // interval with greatest start <= left
        if ($idx >= 0 && $this->intervals[$idx][1] >= $right) {
            return true;
        }
        return false;
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function removeRange($left, $right) {
        $new = [];
        foreach ($this->intervals as $intv) {
            // No overlap
            if ($intv[1] <= $left || $intv[0] >= $right) {
                $new[] = $intv;
                continue;
            }
            // Left part remains
            if ($intv[0] < $left) {
                $new[] = [$intv[0], $left];
            }
            // Right part remains
            if ($intv[1] > $right) {
                $new[] = [$right, $intv[1]];
            }
        }
        $this->intervals = $new;
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * $obj = new RangeModule();
 * $obj->addRange($left, $right);
 * $ret_2 = $obj->queryRange($left, $right);
 * $obj->removeRange($left, $right);
 */
?>
```

## Swift

```swift
class RangeModule {
    private var ranges: [(Int, Int)] = []
    
    init() { }
    
    func addRange(_ left: Int, _ right: Int) {
        var i = 0
        while i < ranges.count && ranges[i].1 < left {
            i += 1
        }
        var start = left
        var end = right
        var j = i
        while j < ranges.count && ranges[j].0 <= right {
            start = min(start, ranges[j].0)
            end = max(end, ranges[j].1)
            j += 1
        }
        if i == j {
            ranges.insert((start, end), at: i)
        } else {
            ranges.replaceSubrange(i..<j, with: [(start, end)])
        }
    }
    
    func queryRange(_ left: Int, _ right: Int) -> Bool {
        var lo = 0
        var hi = ranges.count - 1
        while lo <= hi {
            let mid = (lo + hi) >> 1
            if ranges[mid].0 > left {
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        if hi >= 0 && ranges[hi].1 >= right {
            return true
        }
        return false
    }
    
    func removeRange(_ left: Int, _ right: Int) {
        var newRanges: [(Int, Int)] = []
        for interval in ranges {
            let l = interval.0
            let r = interval.1
            if r <= left || l >= right {
                // No overlap
                newRanges.append(interval)
            } else {
                if l < left {
                    newRanges.append((l, left))
                }
                if r > right {
                    newRanges.append((right, r))
                }
            }
        }
        ranges = newRanges
    }
}
```

## Kotlin

```kotlin
import java.util.TreeMap

class RangeModule() {
    private val ranges = TreeMap<Int, Int>() // start -> end (exclusive)

    fun addRange(left: Int, right: Int) {
        var l = left
        var r = right

        // Merge with interval that may overlap on the left side
        val lower = ranges.floorEntry(l)
        if (lower != null && lower.value >= l) {
            l = minOf(l, lower.key)
            r = maxOf(r, lower.value)
            ranges.remove(lower.key)
        }

        // Merge all intervals that start within [l, r]
        var entry = ranges.ceilingEntry(l)
        while (entry != null && entry.key <= r) {
            r = maxOf(r, entry.value)
            val keyToRemove = entry.key
            entry = ranges.higherEntry(keyToRemove)
            ranges.remove(keyToRemove)
        }

        ranges[l] = r
    }

    fun queryRange(left: Int, right: Int): Boolean {
        val entry = ranges.floorEntry(left) ?: return false
        return entry.value >= right
    }

    fun removeRange(left: Int, right: Int) {
        if (left >= right) return

        // Handle possible overlapping interval on the left side
        var entry = ranges.floorEntry(left)
        if (entry != null && entry.value > left) {
            val start = entry.key
            val end = entry.value
            ranges.remove(start)
            if (start < left) {
                ranges[start] = left
            }
            if (end > right) {
                ranges[right] = end
            }
        }

        // Remove or trim intervals that start within [left, right)
        var cur = ranges.ceilingEntry(left)
        while (cur != null && cur.key < right) {
            val start = cur.key
            val end = cur.value
            ranges.remove(start)
            if (end > right) {
                ranges[right] = end
            }
            cur = ranges.ceilingEntry(left)
        }
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * var obj = RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

## Dart

```dart
import 'dart:math';

class RangeModule {
  List<List<int>> _ranges = [];

  RangeModule();

  void addRange(int left, int right) {
    int i = 0;
    while (i < _ranges.length && _ranges[i][1] < left) {
      i++;
    }
    int start = i;
    int newLeft = left;
    int newRight = right;
    while (i < _ranges.length && _ranges[i][0] <= right) {
      newLeft = min(newLeft, _ranges[i][0]);
      newRight = max(newRight, _ranges[i][1]);
      i++;
    }
    _ranges.removeRange(start, i);
    _ranges.insert(start, [newLeft, newRight]);
  }

  bool queryRange(int left, int right) {
    int idx = _findIdx(left);
    if (idx == -1) return false;
    return left >= _ranges[idx][0] && right <= _ranges[idx][1];
  }

  void removeRange(int left, int right) {
    int i = 0;
    while (i < _ranges.length && _ranges[i][1] <= left) {
      i++;
    }
    int start = i;
    List<List<int>> toAdd = [];
    while (i < _ranges.length && _ranges[i][0] < right) {
      int curL = _ranges[i][0];
      int curR = _ranges[i][1];
      if (curL < left) {
        toAdd.add([curL, min(left, curR)]);
      }
      if (curR > right) {
        toAdd.add([max(right, curL), curR]);
      }
      i++;
    }
    int end = i;
    _ranges.removeRange(start, end);
    _ranges.insertAll(start, toAdd);
  }

  int _findIdx(int x) {
    int lo = 0;
    int hi = _ranges.length - 1;
    while (lo <= hi) {
      int mid = (lo + hi) >> 1;
      if (_ranges[mid][0] > x) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return hi; // may be -1
  }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = RangeModule();
 * obj.addRange(left,right);
 * bool param2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
```

## Golang

```go
type Interval struct {
	l, r int
}

type RangeModule struct {
	intervals []Interval
}

/** Initialize your data structure here. */
func Constructor() RangeModule {
	return RangeModule{}
}

func (this *RangeModule) AddRange(left int, right int) {
	newL, newR := left, right
	var merged []Interval
	i, n := 0, len(this.intervals)

	// intervals completely before the new range
	for i < n && this.intervals[i].r < left {
		merged = append(merged, this.intervals[i])
		i++
	}
	// merge overlapping intervals
	for i < n && this.intervals[i].l <= right {
		if this.intervals[i].l < newL {
			newL = this.intervals[i].l
		}
		if this.intervals[i].r > newR {
			newR = this.intervals[i].r
		}
		i++
	}
	merged = append(merged, Interval{newL, newR})
	// remaining intervals after the new range
	for i < n {
		merged = append(merged, this.intervals[i])
		i++
	}
	this.intervals = merged
}

func (this *RangeModule) QueryRange(left int, right int) bool {
	// binary search for first interval with start > left
	idx := sort.Search(len(this.intervals), func(i int) bool {
		return this.intervals[i].l > left
	})
	if idx == 0 {
		return false
	}
	iv := this.intervals[idx-1]
	return iv.r >= right
}

func (this *RangeModule) RemoveRange(left int, right int) {
	var res []Interval
	for _, iv := range this.intervals {
		// no overlap
		if iv.r <= left || iv.l >= right {
			res = append(res, iv)
			continue
		}
		// left part remains
		if iv.l < left {
			res = append(res, Interval{iv.l, left})
		}
		// right part remains
		if iv.r > right {
			res = append(res, Interval{right, iv.r})
		}
	}
	this.intervals = res
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRange(left,right);
 * param_2 := obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */

import "sort"
```

## Ruby

```ruby
class RangeModule
  def initialize()
    @intervals = []
  end

=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
  def add_range(left, right)
    i = 0
    # skip intervals ending before the new range
    while i < @intervals.size && @intervals[i][1] < left
      i += 1
    end

    new_left = left
    new_right = right
    j = i
    # merge all overlapping intervals
    while j < @intervals.size && @intervals[j][0] <= right
      new_left = [new_left, @intervals[j][0]].min
      new_right = [new_right, @intervals[j][1]].max
      j += 1
    end

    # replace the covered part with the merged interval
    @intervals[i...j] = [[new_left, new_right]]
  end

=begin
    :type left: Integer
    :type right: Integer
    :rtype: Boolean
=end
  def query_range(left, right)
    lo = 0
    hi = @intervals.size - 1
    while lo <= hi
      mid = (lo + hi) / 2
      l, r = @intervals[mid]
      if left < l
        hi = mid - 1
      elsif left >= r
        lo = mid + 1
      else
        return right <= r
      end
    end
    false
  end

=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
  def remove_range(left, right)
    new_intervals = []
    @intervals.each do |l, r|
      if r <= left || l >= right
        # no overlap
        new_intervals << [l, r]
      else
        # overlap exists, possibly split
        new_intervals << [l, left] if l < left
        new_intervals << [right, r] if r > right
      end
    end
    @intervals = new_intervals
  end
end
```

## Scala

```scala
import java.util.TreeMap

class RangeModule() {

  private val map = new TreeMap[Int, Int]()

  def addRange(left: Int, right: Int): Unit = {
    var l = left
    var r = right

    // Merge with interval on the left if it overlaps or touches
    var entry = map.floorEntry(l)
    if (entry != null && entry.getValue >= l) {
      l = Math.min(l, entry.getKey)
      r = Math.max(r, entry.getValue)
      map.remove(entry.getKey)
    }

    // Merge with all following intervals that overlap or touch
    var cur = map.ceilingEntry(left)
    while (cur != null && cur.getKey <= r) {
      l = Math.min(l, cur.getKey)
      r = Math.max(r, cur.getValue)
      val next = map.higherEntry(cur.getKey)
      map.remove(cur.getKey)
      cur = next
    }

    map.put(l, r)
  }

  def queryRange(left: Int, right: Int): Boolean = {
    val entry = map.floorEntry(left)
    entry != null && entry.getValue >= right
  }

  def removeRange(left: Int, right: Int): Unit = {
    // Handle possible overlap with interval on the left side
    var entry = map.floorEntry(left)
    if (entry != null && entry.getValue > left) {
      val s = entry.getKey
      val e = entry.getValue
      map.remove(entry.getKey)
      if (s < left) map.put(s, left)
      if (e > right) map.put(right, e)
    }

    // Remove or trim intervals that start within [left, right)
    var cur = map.ceilingEntry(left)
    while (cur != null && cur.getKey < right) {
      val s = cur.getKey
      val e = cur.getValue
      val next = map.higherEntry(s)
      map.remove(s)
      if (e > right) map.put(right, e)
      cur = next
    }
  }

}

/**
 * Your RangeModule object will be instantiated and called as such:
 * val obj = new RangeModule()
 * obj.addRange(left,right)
 * val param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

## Rust

```rust
use std::collections::BTreeMap;

pub struct RangeModule {
    ranges: BTreeMap<i32, i32>,
}

impl RangeModule {
    pub fn new() -> Self {
        RangeModule {
            ranges: BTreeMap::new(),
        }
    }

    pub fn add_range(&mut self, left: i32, right: i32) {
        let mut l = left;
        let mut r = right;
        loop {
            let mut changed = false;

            // Check interval that may start before or at l
            if let Some((&s, &e)) = self.ranges.range(..=l).next_back() {
                if e >= l {
                    l = l.min(s);
                    r = r.max(e);
                    self.ranges.remove(&s);
                    changed = true;
                }
            }

            // Collect intervals whose start is within [l, r]
            let keys: Vec<i32> = self.ranges.range(l..=r).map(|(&s, _)| s).collect();
            if !keys.is_empty() {
                for s in keys {
                    if let Some(e) = self.ranges.remove(&s) {
                        l = l.min(s);
                        r = r.max(e);
                        changed = true;
                    }
                }
            }

            if !changed {
                break;
            }
        }
        self.ranges.insert(l, r);
    }

    pub fn query_range(&self, left: i32, right: i32) -> bool {
        if let Some((&_, &e)) = self.ranges.range(..=left).next_back() {
            e >= right
        } else {
            false
        }
    }

    pub fn remove_range(&mut self, left: i32, right: i32) {
        let mut to_add = Vec::new();

        // Interval that may start before left and overlap
        if let Some((&s, &e)) = self.ranges.range(..=left).next_back() {
            if e > left {
                self.ranges.remove(&s);
                if s < left {
                    to_add.push((s, left));
                }
                if e > right {
                    to_add.push((right, e));
                }
            }
        }

        // Intervals that start within [left, right)
        let keys: Vec<i32> = self.ranges.range(left..right).map(|(&s, _)| s).collect();
        for s in keys {
            if let Some(e) = self.ranges.remove(&s) {
                if e > right {
                    to_add.push((right, e));
                }
                // else fully removed
            }
        }

        for (s, e) in to_add {
            self.ranges.insert(s, e);
        }
    }
}
```

## Racket

```racket
(define range-module%
  (class object%
    (super-new)

    (define ranges '())

    ; add-range : exact-integer? exact-integer? -> void?
    (define/public (add-range left right)
      (let ((new-left left) (new-right right))
        (let loop ((lst ranges) (before '()))
          (cond
            [(null? lst)
             (set! ranges (append (reverse before) (list (cons new-left new-right))))]
            [else
              (define cur (car lst))
              (define a (car cur))
              (define b (cdr cur))
              (cond
                [(< b left)
                 (loop (cdr lst) (cons cur before))]
                [(> a right)
                 (set! ranges (append (reverse before)
                                      (list (cons new-left new-right))
                                      (cons cur (cdr lst))))]
                [else
                 (set! new-left (min new-left a))
                 (set! new-right (max new-right b))
                 (loop (cdr lst) before)]))])))

    ; query-range : exact-integer? exact-integer? -> boolean?
    (define/public (query-range left right)
      (let loop ((lst ranges))
        (cond
          [(null? lst) #f]
          [else
           (define cur (car lst))
           (define a (car cur))
           (define b (cdr cur))
           (if (and (<= a left) (>= b right))
               #t
               (if (> a left)
                   #f
                   (loop (cdr lst))))])))

    ; remove-range : exact-integer? exact-integer? -> void?
    (define/public (remove-range left right)
      (let loop ((lst ranges) (new '()))
        (if (null? lst)
            (set! ranges (reverse new))
            (let* ((cur (car lst))
                   (a (car cur))
                   (b (cdr cur)))
              (cond
                [(<= b left) ; completely before removal range
                 (loop (cdr lst) (cons cur new))]
                [(>= a right) ; completely after removal range
                 (loop (cdr lst) (cons cur new))]
                [else ; overlap
                 (when (< a left)
                   (set! new (cons (cons a left) new)))
                 (when (> b right)
                   (set! new (cons (cons right b) new)))
                 (loop (cdr lst) new)])))))))
```

## Erlang

```erlang
-module(range_module).
-export([range_module_init_/0,
         range_module_add_range/2,
         range_module_query_range/2,
         range_module_remove_range/2]).

%% Initialize the module state.
-spec range_module_init_() -> any().
range_module_init_() ->
    put(ranges, []).

%% Add a half-open interval [Left, Right).
-spec range_module_add_range(Left :: integer(), Right :: integer()) -> any().
range_module_add_range(Left, Right) ->
    Ranges = get(ranges),
    NewRanges = add_merge(Ranges, Left, Right, []),
    put(ranges, NewRanges).

%% Query whether the interval [Left, Right) is fully covered.
-spec range_module_query_range(Left :: integer(), Right :: integer()) -> boolean().
range_module_query_range(Left, Right) ->
    Ranges = get(ranges),
    query(Ranges, Left, Right).

%% Remove a half-open interval [Left, Right).
-spec range_module_remove_range(Left :: integer(), Right :: integer()) -> any().
range_module_remove_range(Left, Right) ->
    Ranges = get(ranges),
    NewRangesRev = remove_sub(Ranges, Left, Right, []),
    put(ranges, lists:reverse(NewRangesRev)).

%% Helper to merge intervals when adding.
-spec add_merge([ {integer(), integer()} ], integer(), integer(), [ {integer(), integer()} ]) -> [ {integer(), integer()} ].
add_merge([], NL, NR, Acc) ->
    lists:reverse(Acc) ++ [{NL, NR}];
add_merge([{A,B}=Int | Rest], NL, NR, Acc) ->
    if
        B < NL ->
            add_merge(Rest, NL, NR, [Int | Acc]);
        A > NR ->
            Before = lists:reverse(Acc),
            Before ++ [{NL, NR}, Int | Rest];
        true ->
            NewL = min(NL, A),
            NewR = max(NR, B),
            add_merge(Rest, NewL, NewR, Acc)
    end.

%% Helper to query coverage.
-spec query([ {integer(), integer()} ], integer(), integer()) -> boolean().
query([], _L, _R) ->
    false;
query([{A,B} | Rest], L, R) when B < L ->
    query(Rest, L, R);
query([{A,B} | _Rest], L, R) when A =< L, B >= R ->
    true;
query(_, _, _) ->
    false.

%% Helper to remove intervals.
-spec remove_sub([ {integer(), integer()} ], integer(), integer(), [ {integer(), integer()} ]) -> [ {integer(), integer()} ].
remove_sub([], _L, _R, Acc) ->
    Acc;
remove_sub([{A,B}=Int | Rest], L, R, Acc) ->
    if
        B =< L; A >= R ->
            remove_sub(Rest, L, R, [Int | Acc]);
        true ->
            Acc1 = if B > R -> [{R, B} | Acc] else Acc end,
            Acc2 = if A < L -> [{A, L} | Acc1] else Acc1 end,
            remove_sub(Rest, L, R, Acc2)
    end.
```

## Elixir

```elixir
defmodule RangeModule do
  @spec init_() :: any
  def init_() do
    Process.put(:ranges, [])
    :ok
  end

  @spec add_range(left :: integer, right :: integer) :: any
  def add_range(left, right) do
    ranges = Process.get(:ranges, [])
    {left_part, right_rest, new_l, new_r} = add_range_process(ranges, left, right, [])
    final = left_part ++ [{new_l, new_r}] ++ right_rest
    Process.put(:ranges, final)
    :ok
  end

  defp add_range_process([], l, r, left_acc) do
    {Enum.reverse(left_acc), [], l, r}
  end

  defp add_range_process([{a, b} = interval | tail], l, r, left_acc) do
    cond do
      b < l ->
        add_range_process(tail, l, r, [interval | left_acc])

      a > r ->
        {Enum.reverse(left_acc), [interval | tail], l, r}

      true ->
        new_l = min(l, a)
        new_r = max(r, b)
        add_range_process(tail, new_l, new_r, left_acc)
    end
  end

  @spec query_range(left :: integer, right :: integer) :: boolean
  def query_range(left, right) do
    ranges = Process.get(:ranges, [])
    Enum.any?(ranges, fn {a, b} -> a <= left && b >= right end)
  end

  @spec remove_range(left :: integer, right :: integer) :: any
  def remove_range(left, right) do
    ranges = Process.get(:ranges, [])
    new_ranges =
      Enum.reduce(ranges, [], fn {a, b}, acc ->
        cond do
          b <= left or a >= right ->
            [{a, b} | acc]

          true ->
            left_part = if a < left, do: [{a, left}], else: []
            right_part = if b > right, do: [{right, b}], else: []
            left_part ++ right_part ++ acc
        end
      end)
      |> Enum.reverse()

    Process.put(:ranges, new_ranges)
    :ok
  end
end
```
