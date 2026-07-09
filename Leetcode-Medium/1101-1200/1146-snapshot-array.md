# 1146. Snapshot Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class SnapshotArray {
    vector<vector<pair<int,int>>> hist;
    int curSnap = 0;
public:
    SnapshotArray(int length) : hist(length) {
        for (auto &v : hist) v.emplace_back(-1, 0);
    }
    
    void set(int index, int val) {
        auto &vec = hist[index];
        if (!vec.empty() && vec.back().first == curSnap) {
            vec.back().second = val;
        } else {
            vec.emplace_back(curSnap, val);
        }
    }
    
    int snap() {
        return curSnap++;
    }
    
    int get(int index, int snap_id) {
        const auto &vec = hist[index];
        // upper_bound to find first pair with snap > snap_id
        int l = 0, r = (int)vec.size(); // [l,r)
        while (l < r) {
            int m = (l + r) >> 1;
            if (vec[m].first <= snap_id) l = m + 1;
            else r = m;
        }
        return vec[l-1].second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
```

## Java

```java
class SnapshotArray {
    private int curSnap;
    private java.util.ArrayList<int[]>[] history;

    @SuppressWarnings("unchecked")
    public SnapshotArray(int length) {
        curSnap = 0;
        history = new java.util.ArrayList[length];
        for (int i = 0; i < length; i++) {
            history[i] = new java.util.ArrayList<>();
            history[i].add(new int[]{0, 0}); // initial value
        }
    }

    public void set(int index, int val) {
        java.util.ArrayList<int[]> list = history[index];
        if (list.get(list.size() - 1)[0] == curSnap) {
            list.get(list.size() - 1)[1] = val; // overwrite same snap
        } else {
            list.add(new int[]{curSnap, val});
        }
    }

    public int snap() {
        return curSnap++;
    }

    public int get(int index, int snap_id) {
        java.util.ArrayList<int[]> list = history[index];
        int lo = 0, hi = list.size() - 1;
        while (lo < hi) {
            int mid = (lo + hi + 1) >>> 1; // upper mid
            if (list.get(mid)[0] <= snap_id) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return list.get(lo)[1];
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
```

## Python

```python
class SnapshotArray(object):
    def __init__(self, length):
        """
        :type length: int
        """
        self.current_snap = 0
        # each index stores list of (snap_id, value), initialized with snap 0 value 0
        self.history = [[(0, 0)] for _ in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        hist = self.history[index]
        if hist[-1][0] == self.current_snap:
            # overwrite the value for the current snap
            hist[-1] = (self.current_snap, val)
        else:
            hist.append((self.current_snap, val))

    def snap(self):
        """
        :rtype: int
        """
        snap_id = self.current_snap
        self.current_snap += 1
        return snap_id

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        hist = self.history[index]
        # binary search for rightmost snap_id <= target
        lo, hi = 0, len(hist) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if hist[mid][0] <= snap_id:
                lo = mid
            else:
                hi = mid - 1
        return hist[lo][1]
```

## Python3

```python
class SnapshotArray:
    def __init__(self, length: int):
        self.history = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        hist = self.history[index]
        if hist[-1][0] == self.snap_id:
            hist[-1] = (self.snap_id, val)
        else:
            hist.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        hist = self.history[index]
        lo, hi = 0, len(hist) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if hist[mid][0] <= snap_id:
                lo = mid + 1
            else:
                hi = mid - 1
        return hist[hi][1]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int snap;
    int val;
} Pair;

typedef struct {
    int length;
    int curSnap;
    Pair **history;   // per index array of pairs
    int *histSize;    // number of records per index
    int *histCap;     // capacity of each record array
} SnapshotArray;

SnapshotArray* snapshotArrayCreate(int length) {
    SnapshotArray *obj = (SnapshotArray *)malloc(sizeof(SnapshotArray));
    obj->length = length;
    obj->curSnap = 0;
    obj->history = (Pair **)malloc(length * sizeof(Pair *));
    obj->histSize = (int *)calloc(length, sizeof(int));
    obj->histCap = (int *)calloc(length, sizeof(int));

    for (int i = 0; i < length; ++i) {
        obj->histCap[i] = 1;
        obj->history[i] = (Pair *)malloc(sizeof(Pair) * obj->histCap[i]);
        obj->history[i][0].snap = 0;
        obj->history[i][0].val = 0;
        obj->histSize[i] = 1;
    }
    return obj;
}

void snapshotArraySet(SnapshotArray* obj, int index, int val) {
    int sz = obj->histSize[index];
    if (sz > 0 && obj->history[index][sz - 1].snap == obj->curSnap) {
        obj->history[index][sz - 1].val = val;
        return;
    }
    if (obj->histSize[index] == obj->histCap[index]) {
        int newCap = obj->histCap[index] * 2;
        if (newCap == 0) newCap = 2;
        obj->history[index] = (Pair *)realloc(obj->history[index], sizeof(Pair) * newCap);
        obj->histCap[index] = newCap;
    }
    obj->history[index][obj->histSize[index]].snap = obj->curSnap;
    obj->history[index][obj->histSize[index]].val = val;
    obj->histSize[index]++;
}

int snapshotArraySnap(SnapshotArray* obj) {
    return obj->curSnap++;
}

int snapshotArrayGet(SnapshotArray* obj, int index, int snap_id) {
    int lo = 0, hi = obj->histSize[index] - 1;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (obj->history[index][mid].snap <= snap_id)
            lo = mid;
        else
            hi = mid - 1;
    }
    return obj->history[index][lo].val;
}

void snapshotArrayFree(SnapshotArray* obj) {
    for (int i = 0; i < obj->length; ++i) {
        free(obj->history[i]);
    }
    free(obj->history);
    free(obj->histSize);
    free(obj->histCap);
    free(obj);
}

/**
 * Your SnapshotArray struct will be instantiated and called as such:
 * SnapshotArray* obj = snapshotArrayCreate(length);
 * snapshotArraySet(obj, index, val);
 *
 * int param_2 = snapshotArraySnap(obj);
 *
 * int param_3 = snapshotArrayGet(obj, index, snap_id);
 *
 * snapshotArrayFree(obj);
 */
```

## Csharp

```csharp
public class SnapshotArray
{
    private readonly List<(int snapId, int val)>[] _history;
    private int _currentSnap;

    public SnapshotArray(int length)
    {
        _history = new List<(int snapId, int val)>[length];
        for (int i = 0; i < length; i++)
        {
            _history[i] = new List<(int snapId, int val)>();
            _history[i].Add((0, 0));
        }
        _currentSnap = 0;
    }

    public void Set(int index, int val)
    {
        var list = _history[index];
        if (list.Count > 0 && list[list.Count - 1].snapId == _currentSnap)
        {
            list[list.Count - 1] = (_currentSnap, val);
        }
        else
        {
            list.Add((_currentSnap, val));
        }
    }

    public int Snap()
    {
        return _currentSnap++;
    }

    public int Get(int index, int snap_id)
    {
        var list = _history[index];
        int lo = 0, hi = list.Count - 1;
        while (lo < hi)
        {
            int mid = (lo + hi + 1) >> 1; // upper mid
            if (list[mid].snapId <= snap_id)
                lo = mid;
            else
                hi = mid - 1;
        }
        return list[lo].val;
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.Set(index,val);
 * int param_2 = obj.Snap();
 * int param_3 = obj.Get(index,snap_id);
 */
```

## Javascript

```javascript
/**
 * @param {number} length
 */
var SnapshotArray = function(length) {
    this.histories = new Array(length);
    for (let i = 0; i < length; i++) {
        // each entry: [snap_id, value]
        this.histories[i] = [[0, 0]];
    }
    this.curSnap = 0;
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
SnapshotArray.prototype.set = function(index, val) {
    const hist = this.histories[index];
    if (hist[hist.length - 1][0] === this.curSnap) {
        // overwrite value for the same snap_id
        hist[hist.length - 1][1] = val;
    } else {
        hist.push([this.curSnap, val]);
    }
};

/**
 * @return {number}
 */
SnapshotArray.prototype.snap = function() {
    return this.curSnap++;
};

/** 
 * @param {number} index 
 * @param {number} snap_id
 * @return {number}
 */
SnapshotArray.prototype.get = function(index, snap_id) {
    const hist = this.histories[index];
    let left = 0, right = hist.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (hist[mid][0] === snap_id) {
            return hist[mid][1];
        } else if (hist[mid][0] < snap_id) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    // right is the last index with snap_id <= target
    return hist[right][1];
};
```

## Typescript

```typescript
class SnapshotArray {
    private histories: Array<Array<[number, number]>>;
    private curSnap: number;

    constructor(length: number) {
        this.curSnap = 0;
        this.histories = new Array(length);
        for (let i = 0; i < length; i++) {
            // Initialize with a sentinel entry for snap_id -1 and value 0
            this.histories[i] = [[-1, 0]];
        }
    }

    set(index: number, val: number): void {
        const hist = this.histories[index];
        if (hist[hist.length - 1][0] === this.curSnap) {
            // Overwrite the value for the current snap if already recorded
            hist[hist.length - 1][1] = val;
        } else {
            hist.push([this.curSnap, val]);
        }
    }

    snap(): number {
        return this.curSnap++;
    }

    get(index: number, snap_id: number): number {
        const hist = this.histories[index];
        // Binary search for the rightmost entry with snap_id <= target
        let lo = 0;
        let hi = hist.length - 1;
        while (lo <= hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (hist[mid][0] <= snap_id) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        // hi now points to the desired entry
        return hist[hi][1];
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
```

## Php

```php
class SnapshotArray {
    private int $snapId;
    private array $history;

    /**
     * @param Integer $length
     */
    function __construct($length) {
        $this->snapId = 0;
        $this->history = array_fill(0, $length, null);
        for ($i = 0; $i < $length; $i++) {
            // each entry is a list of [snap_id, value] pairs
            $this->history[$i] = [[0, 0]];
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function set($index, $val) {
        $list = &$this->history[$index];
        $lastIdx = count($list) - 1;
        if ($list[$lastIdx][0] === $this->snapId) {
            // overwrite value for the same snap_id
            $list[$lastIdx][1] = $val;
        } else {
            $list[] = [$this->snapId, $val];
        }
    }

    /**
     * @return Integer
     */
    function snap() {
        $current = $this->snapId;
        $this->snapId++;
        return $current;
    }

    /**
     * @param Integer $index
     * @param Integer $snap_id
     * @return Integer
     */
    function get($index, $snap_id) {
        $list = $this->history[$index];
        $low = 0;
        $high = count($list) - 1;
        $ansIdx = 0; // default to first entry (snap_id 0)
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($list[$mid][0] <= $snap_id) {
                $ansIdx = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $list[$ansIdx][1];
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * $obj = new SnapshotArray($length);
 * $obj->set($index, $val);
 * $ret_2 = $obj->snap();
 * $ret_3 = $obj->get($index, $snap_id);
 */
```

## Swift

```swift
class SnapshotArray {
    private var snapId: Int
    private var histories: [[(Int, Int)]]

    init(_ length: Int) {
        self.snapId = 0
        self.histories = Array(repeating: [], count: length)
        for i in 0..<length {
            // Initialize with a default value at snap -1 so get works without any set.
            self.histories[i].append((-1, 0))
        }
    }

    func set(_ index: Int, _ val: Int) {
        if let last = histories[index].last, last.0 == snapId {
            // Overwrite the value for the current snapId if already set in this version.
            histories[index][histories[index].count - 1].1 = val
        } else {
            histories[index].append((snapId, val))
        }
    }

    func snap() -> Int {
        let current = snapId
        snapId += 1
        return current
    }

    func get(_ index: Int, _ snap_id: Int) -> Int {
        let arr = histories[index]
        var lo = 0
        var hi = arr.count - 1
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if arr[mid].0 <= snap_id {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return arr[lo].1
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray(length)
 * obj.set(index, val)
 * let ret_2: Int = obj.snap()
 * let ret_3: Int = obj.get(index, snap_id)
 */
```

## Kotlin

```kotlin
class SnapshotArray(length: Int) {
    private var currentSnap = 0
    private val history: Array<MutableList<Pair<Int, Int>>> =
        Array(length) { mutableListOf(Pair(0, 0)) }

    fun set(index: Int, `val`: Int) {
        val list = history[index]
        if (list.isNotEmpty() && list.last().first == currentSnap) {
            list[list.size - 1] = Pair(currentSnap, `val`)
        } else {
            list.add(Pair(currentSnap, `val`))
        }
    }

    fun snap(): Int {
        return currentSnap++
    }

    fun get(index: Int, snap_id: Int): Int {
        val list = history[index]
        var left = 0
        var right = list.size - 1
        while (left <= right) {
            val mid = (left + right) ushr 1
            if (list[mid].first <= snap_id) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return list[right].second
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = SnapshotArray(length)
 * obj.set(index,`val`)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
```

## Dart

```dart
class SnapshotArray {
  int _snapId = 0;
  late final List<List<List<int>>> _history;

  SnapshotArray(int length) {
    _history = List.generate(length, (_) => <List<int>>[[0, 0]]);
  }

  void set(int index, int val) {
    var hist = _history[index];
    if (hist.isNotEmpty && hist.last[0] == _snapId) {
      hist.last[1] = val;
    } else {
      hist.add([_snapId, val]);
    }
  }

  int snap() {
    return _snapId++;
  }

  int get(int index, int snap_id) {
    var hist = _history[index];
    int l = 0;
    int r = hist.length - 1;
    while (l <= r) {
      int m = (l + r) >> 1;
      if (hist[m][0] <= snap_id) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
    return hist[r][1];
  }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = SnapshotArray(length);
 * obj.set(index,val);
 * int param2 = obj.snap();
 * int param3 = obj.get(index,snap_id);
 */
```

## Golang

```go
package main

import "sort"

type pair struct {
	snap int
	val  int
}

type SnapshotArray struct {
	history [][]pair
	curSnap int
}

/** Initialize your data structure here. */
func Constructor(length int) SnapshotArray {
	h := make([][]pair, length)
	for i := 0; i < length; i++ {
		h[i] = []pair{{snap: 0, val: 0}}
	}
	return SnapshotArray{history: h, curSnap: 0}
}

/** Set the element at index `index` to be `val`. */
func (this *SnapshotArray) Set(index int, val int)  {
	h := this.history[index]
	if len(h) > 0 && h[len(h)-1].snap == this.curSnap {
		h[len(h)-1].val = val
	} else {
		h = append(h, pair{snap: this.curSnap, val: val})
	}
	this.history[index] = h
}

/** Take a snapshot, and return the snap_id. */
func (this *SnapshotArray) Snap() int {
	id := this.curSnap
	this.curSnap++
	return id
}

/** Get the value at index `index`, at the time we took the snapshot with id `snap_id`. */
func (this *SnapshotArray) Get(index int, snap_id int) int {
	h := this.history[index]
	// Find first entry with snap > snap_id
	pos := sort.Search(len(h), func(i int) bool { return h[i].snap > snap_id })
	if pos == 0 {
		return 0
	}
	return h[pos-1].val
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
```

## Ruby

```ruby
class SnapshotArray
  # :type length: Integer
  def initialize(length)
    @curr_snap = 0
    @history = Array.new(length) { [[-1, 0]] }
  end

  # :type index: Integer
  # :type val: Integer
  # :rtype: Void
  def set(index, val)
    hist = @history[index]
    if hist[-1][0] == @curr_snap
      hist[-1][1] = val
    else
      hist << [@curr_snap, val]
    end
  end

  # :rtype: Integer
  def snap()
    ret = @curr_snap
    @curr_snap += 1
    ret
  end

  # :type index: Integer
  # :type snap_id: Integer
  # :rtype: Integer
  def get(index, snap_id)
    hist = @history[index]
    l = 0
    r = hist.length - 1
    while l <= r
      m = (l + r) / 2
      if hist[m][0] <= snap_id
        l = m + 1
      else
        r = m - 1
      end
    end
    hist[r][1]
  end
end
```

## Scala

```scala
class SnapshotArray(_length: Int) {
  private var curSnap = 0
  private val history: Array[scala.collection.mutable.ArrayBuffer[(Int, Int)]] =
    Array.fill(_length)(scala.collection.mutable.ArrayBuffer((0, 0)))

  def set(index: Int, `val`: Int): Unit = {
    val buf = history(index)
    if (buf.last._1 == curSnap) {
      buf.update(buf.size - 1, (curSnap, `val`))
    } else {
      buf.append((curSnap, `val`))
    }
  }

  def snap(): Int = {
    val id = curSnap
    curSnap += 1
    id
  }

  def get(index: Int, snap_id: Int): Int = {
    val buf = history(index)
    var l = 0
    var r = buf.length - 1
    while (l <= r) {
      val m = (l + r) >>> 1
      if (buf(m)._1 <= snap_id) {
        l = m + 1
      } else {
        r = m - 1
      }
    }
    buf(r)._2
  }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * val obj = new SnapshotArray(length)
 * obj.set(index,`val`)
 * val param_2 = obj.snap()
 * val param_3 = obj.get(index,snap_id)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct SnapshotArray {
    cur_snap: RefCell<i32>,
    histories: Vec<RefCell<Vec<(i32, i32)>>>,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        let len = length as usize;
        let mut histories = Vec::with_capacity(len);
        for _ in 0..len {
            histories.push(RefCell::new(vec![(0, 0)]));
        }
        SnapshotArray {
            cur_snap: RefCell::new(0),
            histories,
        }
    }

    fn set(&self, index: i32, val: i32) {
        let idx = index as usize;
        let snap_id = *self.cur_snap.borrow();
        let mut hist = self.histories[idx].borrow_mut();
        if let Some(last) = hist.last_mut() {
            if last.0 == snap_id {
                last.1 = val;
                return;
            }
        }
        hist.push((snap_id, val));
    }

    fn snap(&self) -> i32 {
        let mut snap = self.cur_snap.borrow_mut();
        let ret = *snap;
        *snap += 1;
        ret
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let idx = index as usize;
        let hist = self.histories[idx].borrow();
        // binary search for first entry with snap > snap_id
        let mut lo = 0usize;
        let mut hi = hist.len();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if hist[mid].0 <= snap_id {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        // lo is the insertion point, answer at lo-1
        hist[lo - 1].1
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
```

## Racket

```racket
(define snapshot-array%
  (class object%
    (super-new)

    ; length : exact-integer?
    (init-field length)

    ; current snap id
    (define curr-snap 0)

    ; histories : vector of vectors, each inner vector stores (snap_id . value) pairs
    (define histories (make-vector length))
    ; sizes : vector storing the number of valid entries in each history vector
    (define sizes (make-vector length))

    ; initialize each index with a default record (0 . 0)
    (for ([i (in-range length)])
      (let* ((vec (make-vector 1)))
        (vector-set! vec 0 (cons 0 0))
        (vector-set! histories i vec)
        (vector-set! sizes i 1)))

    ; set : exact-integer? exact-integer? -> void?
    (define/public (set index val)
      (let* ((vec (vector-ref histories index))
             (sz (vector-ref sizes index))
             (last-pair (vector-ref vec (- sz 1))))
        (if (= (car last-pair) curr-snap)
            ; same snap id, replace value
            (vector-set! vec (- sz 1) (cons curr-snap val))
            ; append new record
            (let* ((cap (vector-length vec))
                   (new-vec (if (= sz cap)
                                (let ([nv (make-vector (* 2 cap))])
                                  (for ([j (in-range sz)])
                                    (vector-set! nv j (vector-ref vec j)))
                                  nv)
                                vec)))
              (when (not (eq? new-vec vec))
                (vector-set! histories index new-vec))
              (vector-set! new-vec sz (cons curr-snap val))
              (vector-set! sizes index (+ sz 1))))))

    ; snap : -> exact-integer?
    (define/public (snap)
      (let ((id curr-snap))
        (set! curr-snap (+ curr-snap 1))
        id))

    ; get : exact-integer? exact-integer? -> exact-integer?
    (define/public (get index snap_id)
      (let* ((vec (vector-ref histories index))
             (sz (vector-ref sizes index)))
        (let loop ([lo 0] [hi (- sz 1)] [ans -1])
          (if (> lo hi)
              (cdr (vector-ref vec ans)) ; ans is always set because snap 0 exists
              (let* ((mid (quotient (+ lo hi) 2))
                     (pair (vector-ref vec mid))
                     (sid (car pair)))
                (if (<= sid snap_id)
                    (loop (+ mid 1) hi mid)
                    (loop lo (- mid 1) ans)))))))

    ))
```

## Erlang

```erlang
-spec snapshot_array_init_(Length :: integer()) -> any().
snapshot_array_init_(Length) ->
    Empty = [{0, 0}],
    List = lists:duplicate(Length, Empty),
    Histories = list_to_tuple(List),
    State = #{histories => Histories, snap_id => 0},
    put(snapshot_state, State).

-spec snapshot_array_set(Index :: integer(), Val :: integer()) -> any().
snapshot_array_set(Index, Val) ->
    State = get(snapshot_state),
    SnapId = maps:get(snap_id, State),
    Histories = maps:get(histories, State),
    Pos = Index + 1,
    OldList = element(Pos, Histories),
    NewList = [{SnapId, Val} | OldList],
    NewHistories = setelement(Pos, Histories, NewList),
    put(snapshot_state, State#{histories => NewHistories}).

-spec snapshot_array_snap() -> integer().
snapshot_array_snap() ->
    State = get(snapshot_state),
    SnapId = maps:get(snap_id, State),
    NewState = State#{snap_id => SnapId + 1},
    put(snapshot_state, NewState),
    SnapId.

-spec snapshot_array_get(Index :: integer(), Snap_id :: integer()) -> integer().
snapshot_array_get(Index, TargetSnap) ->
    State = get(snapshot_state),
    Histories = maps:get(histories, State),
    List = element(Index + 1, Histories),
    find_value(List, TargetSnap).

find_value([{SnapId, Val} | _Rest], Target) when SnapId =< Target ->
    Val;
find_value([_ | Rest], Target) ->
    find_value(Rest, Target).
```

## Elixir

```elixir
defmodule SnapshotArray do
  @spec init_(length :: integer) :: any
  def init_(length) do
    histories =
      Enum.reduce(0..(length - 1), %{}, fn i, acc ->
        Map.put(acc, i, [{0, 0}])
      end)

    Process.put(:snapshot_state, %{snap_id: 0, histories: histories})
  end

  @spec set(index :: integer, val :: integer) :: any
  def set(index, val) do
    state = Process.get(:snapshot_state)
    snap_id = state.snap_id
    histories = state.histories
    hist = Map.get(histories, index)

    new_hist =
      case hist do
        [{sid, _} | rest] when sid == snap_id ->
          [{snap_id, val} | rest]

        _ ->
          [{snap_id, val} | hist]
      end

    new_state = %{state | histories: Map.put(histories, index, new_hist)}
    Process.put(:snapshot_state, new_state)
  end

  @spec snap() :: integer
  def snap() do
    state = Process.get(:snapshot_state)
    cur_snap = state.snap_id
    new_state = %{state | snap_id: cur_snap + 1}
    Process.put(:snapshot_state, new_state)
    cur_snap
  end

  @spec get(index :: integer, snap_id :: integer) :: integer
  def get(index, snap_id) do
    state = Process.get(:snapshot_state)
    hist = Map.get(state.histories, index)

    Enum.find_value(hist, fn {sid, val} ->
      if sid <= snap_id, do: val, else: nil
    end) || 0
  end
end
```
