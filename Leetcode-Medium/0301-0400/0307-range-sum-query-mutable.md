# 0307. Range Sum Query - Mutable

## Cpp

```cpp
class NumArray {
public:
    NumArray(vector<int>& nums) : n(nums.size()), bit(n + 1, 0), data(nums) {
        for (int i = 0; i < n; ++i) add(i, data[i]);
    }
    
    void update(int index, int val) {
        int diff = val - data[index];
        data[index] = val;
        add(index, diff);
    }
    
    int sumRange(int left, int right) {
        return query(right) - (left > 0 ? query(left - 1) : 0);
    }

private:
    int n;
    vector<int> bit;
    vector<int> data;
    
    inline int lowbit(int x) { return x & (-x); }
    
    void add(int idx, int delta) {
        for (int i = idx + 1; i <= n; i += lowbit(i))
            bit[i] += delta;
    }
    
    int query(int idx) const {
        int sum = 0;
        for (int i = idx + 1; i > 0; i -= lowbit(i))
            sum += bit[i];
        return sum;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
```

## Java

```java
class NumArray {
    private final int[] bit;
    private final int[] nums;
    private final int n;

    public NumArray(int[] nums) {
        this.n = nums.length;
        this.nums = new int[n];
        this.bit = new int[n + 1];
        for (int i = 0; i < n; i++) {
            updateBIT(i, nums[i]);
            this.nums[i] = nums[i];
        }
    }

    private void updateBIT(int index, int delta) {
        index++; // convert to 1‑based
        while (index <= n) {
            bit[index] += delta;
            index += index & -index;
        }
    }

    public void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        updateBIT(index, delta);
    }

    private int prefixSum(int index) {
        int sum = 0;
        index++; // convert to 1‑based
        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }
        return sum;
    }

    public int sumRange(int left, int right) {
        return prefixSum(right) - (left == 0 ? 0 : prefixSum(left - 1));
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
```

## Python

```python
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = list(nums)
        self.bit = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self._add(i, val)

    def _add(self, idx, delta):
        i = idx + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _prefix_sum(self, idx):
        if idx < 0:
            return 0
        res = 0
        i = idx + 1
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        if delta:
            self.nums[index] = val
            self._add(index, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._prefix_sum(right) - self._prefix_sum(left - 1)
```

## Python3

```python
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)
        for i, val in enumerate(nums):
            self._add(i + 1, val)

    def _add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def _prefix_sum(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        if delta:
            self.nums[index] = val
            self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *bit;   // 1-indexed BIT
    int *nums;  // original array values
    int n;
} NumArray;

static void bitAdd(NumArray *obj, int index, int delta) {
    for (int i = index + 1; i <= obj->n; i += i & -i)
        obj->bit[i] += delta;
}

static int prefixSum(NumArray *obj, int index) {
    int sum = 0;
    for (int i = index + 1; i > 0; i -= i & -i)
        sum += obj->bit[i];
    return sum;
}

/** Initialize your data structure here. */
NumArray* numArrayCreate(int* nums, int numsSize) {
    NumArray *obj = (NumArray *)malloc(sizeof(NumArray));
    if (!obj) return NULL;
    obj->n = numsSize;
    obj->bit = (int *)calloc(numsSize + 1, sizeof(int));
    obj->nums = (int *)malloc(numsSize * sizeof(int));
    if (!obj->bit || !obj->nums) {
        free(obj->bit);
        free(obj->nums);
        free(obj);
        return NULL;
    }
    memcpy(obj->nums, nums, numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i)
        bitAdd(obj, i, obj->nums[i]);
    return obj;
}

/** Update the value of nums[index] to val. */
void numArrayUpdate(NumArray* obj, int index, int val) {
    int delta = val - obj->nums[index];
    if (delta != 0) {
        obj->nums[index] = val;
        bitAdd(obj, index, delta);
    }
}

/** Return the sum of the elements of nums between indices left and right inclusive. */
int numArraySumRange(NumArray* obj, int left, int right) {
    if (left == 0)
        return prefixSum(obj, right);
    else
        return prefixSum(obj, right) - prefixSum(obj, left - 1);
}

/** Deallocate memory */
void numArrayFree(NumArray* obj) {
    if (!obj) return;
    free(obj->bit);
    free(obj->nums);
    free(obj);
}
```

## Csharp

```csharp
public class NumArray
{
    private readonly int[] _tree;
    private readonly int[] _nums;
    private readonly int _n;

    public NumArray(int[] nums)
    {
        _n = nums.Length;
        _tree = new int[_n + 1];
        _nums = new int[_n];
        for (int i = 0; i < _n; i++)
        {
            UpdateInternal(i, nums[i]);
            _nums[i] = nums[i];
        }
    }

    public void Update(int index, int val)
    {
        int diff = val - _nums[index];
        if (diff != 0)
        {
            _nums[index] = val;
            Add(index + 1, diff);
        }
    }

    public int SumRange(int left, int right)
    {
        return PrefixSum(right + 1) - PrefixSum(left);
    }

    private void UpdateInternal(int index, int val)
    {
        // Used only in constructor to build the BIT.
        Add(index + 1, val);
    }

    private void Add(int i, int delta)
    {
        while (i <= _n)
        {
            _tree[i] += delta;
            i += i & -i;
        }
    }

    private int PrefixSum(int i)
    {
        int sum = 0;
        while (i > 0)
        {
            sum += _tree[i];
            i -= i & -i;
        }
        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.Update(index,val);
 * int param_2 = obj.SumRange(left,right);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.n = nums.length;
    this.tree = new Array(this.n + 1).fill(0);
    this.nums = nums.slice();
    for (let i = 0; i < this.n; i++) {
        this._add(i + 1, this.nums[i]);
    }
};

NumArray.prototype._add = function(index, delta) {
    while (index <= this.n) {
        this.tree[index] += delta;
        index += index & -index;
    }
};

NumArray.prototype._prefixSum = function(index) {
    let sum = 0;
    while (index > 0) {
        sum += this.tree[index];
        index -= index & -index;
    }
    return sum;
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(index, val) {
    const diff = val - this.nums[index];
    if (diff !== 0) {
        this.nums[index] = val;
        this._add(index + 1, diff);
    }
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    return this._prefixSum(right + 1) - this._prefixSum(left);
};
```

## Typescript

```typescript
class NumArray {
    private nums: number[];
    private bit: number[];
    private n: number;

    constructor(nums: number[]) {
        this.n = nums.length;
        this.nums = nums.slice();
        this.bit = new Array(this.n + 1).fill(0);
        for (let i = 0; i < this.n; i++) {
            this.add(i, this.nums[i]);
        }
    }

    private add(index: number, delta: number): void {
        let i = index + 1;
        while (i <= this.n) {
            this.bit[i] += delta;
            i += i & -i;
        }
    }

    private prefixSum(index: number): number {
        let res = 0;
        let i = index + 1;
        while (i > 0) {
            res += this.bit[i];
            i -= i & -i;
        }
        return res;
    }

    update(index: number, val: number): void {
        const diff = val - this.nums[index];
        this.nums[index] = val;
        this.add(index, diff);
    }

    sumRange(left: number, right: number): number {
        if (left === 0) return this.prefixSum(right);
        return this.prefixSum(right) - this.prefixSum(left - 1);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */
```

## Php

```php
class NumArray {
    private $tree = [];
    private $nums = [];
    private $n = 0;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->n = count($nums);
        $this->tree = array_fill(0, $this->n + 1, 0);
        $this->nums = $nums;
        for ($i = 0; $i < $this->n; $i++) {
            $this->add($i + 1, $nums[$i]);
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function update($index, $val) {
        $diff = $val - $this->nums[$index];
        if ($diff != 0) {
            $this->nums[$index] = $val;
            $this->add($index + 1, $diff);
        }
    }

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function sumRange($left, $right) {
        return $this->prefixSum($right + 1) - $this->prefixSum($left);
    }

    private function add($i, $delta) {
        while ($i <= $this->n) {
            $this->tree[$i] += $delta;
            $i += $i & (-$i);
        }
    }

    private function prefixSum($i) {
        $sum = 0;
        while ($i > 0) {
            $sum += $this->tree[$i];
            $i -= $i & (-$i);
        }
        return $sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * $obj = new NumArray($nums);
 * $obj->update($index, $val);
 * $ret_2 = $obj->sumRange($left, $right);
 */
```

## Swift

```swift
class NumArray {
    private var nums: [Int]
    private var tree: [Int]
    private let n: Int

    init(_ nums: [Int]) {
        self.n = nums.count
        self.nums = nums
        self.tree = Array(repeating: 0, count: n + 1)
        if n > 0 {
            for i in 0..<n {
                add(i + 1, nums[i])
            }
        }
    }

    private func lowbit(_ x: Int) -> Int {
        return x & -x
    }

    private func add(_ index: Int, _ delta: Int) {
        var i = index
        while i <= n {
            tree[i] += delta
            i += lowbit(i)
        }
    }

    private func prefixSum(_ index: Int) -> Int {
        var i = index
        var sum = 0
        while i > 0 {
            sum += tree[i]
            i -= lowbit(i)
        }
        return sum
    }

    func update(_ index: Int, _ val: Int) {
        let diff = val - nums[index]
        nums[index] = val
        add(index + 1, diff)
    }

    func sumRange(_ left: Int, _ right: Int) -> Int {
        return prefixSum(right + 1) - prefixSum(left)
    }
}
```

## Kotlin

```kotlin
class NumArray(nums: IntArray) {
    private val n = nums.size
    private val bit = IntArray(n + 1)
    private val arr = IntArray(n)

    init {
        for (i in nums.indices) {
            arr[i] = nums[i]
            var idx = i + 1
            while (idx <= n) {
                bit[idx] += nums[i]
                idx += idx and -idx
            }
        }
    }

    private fun add(index: Int, delta: Int) {
        var idx = index + 1
        while (idx <= n) {
            bit[idx] += delta
            idx += idx and -idx
        }
    }

    private fun prefixSum(index: Int): Int {
        var idx = index + 1
        var sum = 0
        while (idx > 0) {
            sum += bit[idx]
            idx -= idx and -idx
        }
        return sum
    }

    fun update(index: Int, `val`: Int) {
        val diff = `val` - arr[index]
        if (diff != 0) {
            arr[index] = `val`
            add(index, diff)
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        return prefixSum(right) - if (left > 0) prefixSum(left - 1) else 0
    }
}
```

## Dart

```dart
class NumArray {
  late final List<int> _tree;
  late final List<int> _nums;
  late final int _n;

  NumArray(List<int> nums) {
    _n = nums.length;
    _nums = List.from(nums);
    _tree = List.filled(_n + 1, 0);
    for (int i = 0; i < _n; i++) {
      _add(i + 1, _nums[i]);
    }
  }

  void _add(int index, int delta) {
    while (index <= _n) {
      _tree[index] += delta;
      index += index & -index;
    }
  }

  int _prefixSum(int index) {
    int sum = 0;
    while (index > 0) {
      sum += _tree[index];
      index -= index & -index;
    }
    return sum;
  }

  void update(int index, int val) {
    int delta = val - _nums[index];
    if (delta != 0) {
      _nums[index] = val;
      _add(index + 1, delta);
    }
  }

  int sumRange(int left, int right) {
    return _prefixSum(right + 1) - _prefixSum(left);
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = NumArray(nums);
 * obj.update(index,val);
 * int param2 = obj.sumRange(left,right);
 */
```

## Golang

```go
type NumArray struct {
	tree []int
	nums []int
	n    int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	tree := make([]int, n+1)
	na := NumArray{
		tree: tree,
		nums: make([]int, n),
		n:    n,
	}
	copy(na.nums, nums)
	for i, v := range nums {
		na.add(i+1, v)
	}
	return na
}

func (this *NumArray) Update(index int, val int) {
	if index < 0 || index >= this.n {
		return
	}
	delta := val - this.nums[index]
	this.nums[index] = val
	this.add(index+1, delta)
}

func (this *NumArray) SumRange(left int, right int) int {
	if left < 0 {
		left = 0
	}
	if right >= this.n {
		right = this.n - 1
	}
	return this.prefixSum(right+1) - this.prefixSum(left)
}

func (this *NumArray) add(idx int, delta int) {
	for idx <= this.n {
		this.tree[idx] += delta
		idx += idx & -idx
	}
}

func (this *NumArray) prefixSum(idx int) int {
	sum := 0
	for idx > 0 {
		sum += this.tree[idx]
		idx -= idx & -idx
	}
	return sum
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
```

## Ruby

```ruby
class NumArray
  # :type nums: Integer[]
  def initialize(nums)
    @n = nums.length
    @tree = Array.new(@n + 1, 0)
    @nums = nums.clone
    (1..@n).each do |i|
      add(i, @nums[i - 1])
    end
  end

  # :type index: Integer
  # :type val: Integer
  # :rtype: Void
  def update(index, val)
    diff = val - @nums[index]
    @nums[index] = val
    add(index + 1, diff)
  end

  # :type left: Integer
  # :type right: Integer
  # :rtype: Integer
  def sum_range(left, right)
    prefix_sum(right + 1) - prefix_sum(left)
  end

  private

  def add(i, delta)
    while i <= @n
      @tree[i] += delta
      i += i & -i
    end
  end

  def prefix_sum(i)
    sum = 0
    while i > 0
      sum += @tree[i]
      i -= i & -i
    end
    sum
  end
end
```

## Scala

```scala
class NumArray(_nums: Array[Int]) {
  private val n = _nums.length
  private val bit = new Array[Long](n + 1)
  private val nums = new Array[Long](n)

  private def add(idx: Int, delta: Long): Unit = {
    var i = idx + 1
    while (i <= n) {
      bit(i) += delta
      i += i & -i
    }
  }

  private def prefixSum(idx: Int): Long = {
    var res = 0L
    var i = idx + 1
    while (i > 0) {
      res += bit(i)
      i -= i & -i
    }
    res
  }

  // Build BIT
  {
    var i = 0
    while (i < n) {
      val v = _nums(i).toLong
      nums(i) = v
      add(i, v)
      i += 1
    }
  }

  def update(index: Int, `val`: Int): Unit = {
    val newVal = `val`.toLong
    val delta = newVal - nums(index)
    if (delta != 0) {
      nums(index) = newVal
      add(index, delta)
    }
  }

  def sumRange(left: Int, right: Int): Int = {
    val sumRight = prefixSum(right)
    val sumLeft = if (left > 0) prefixSum(left - 1) else 0L
    (sumRight - sumLeft).toInt
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * val obj = new NumArray(nums)
 * obj.update(index,`val`)
 * val param_2 = obj.sumRange(left,right)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct NumArray {
    n: usize,
    tree: RefCell<Vec<i32>>,
    nums: RefCell<Vec<i32>>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        let n = nums.len();
        let mut tree = vec![0; n + 1];
        for (i, &val) in nums.iter().enumerate() {
            let mut idx = i + 1;
            while idx <= n {
                tree[idx] += val;
                idx += idx & (!idx + 1);
            }
        }
        NumArray {
            n,
            tree: RefCell::new(tree),
            nums: RefCell::new(nums),
        }
    }

    fn update(&self, index: i32, val: i32) {
        let idx = index as usize;
        let mut nums_ref = self.nums.borrow_mut();
        let delta = val - nums_ref[idx];
        if delta != 0 {
            nums_ref[idx] = val;
            drop(nums_ref);
            let mut i = idx + 1;
            let n = self.n;
            let mut tree_ref = self.tree.borrow_mut();
            while i <= n {
                tree_ref[i] += delta;
                i += i & (!i + 1);
            }
        }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let l = left as usize;
        let r = right as usize;
        self.prefix_sum(r + 1) - self.prefix_sum(l)
    }

    fn prefix_sum(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        let tree_ref = self.tree.borrow();
        while idx > 0 {
            res += tree_ref[idx];
            idx -= idx & (!idx + 1);
        }
        res
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * obj.update(index, val);
 * let ret_2: i32 = obj.sum_range(left, right);
 */
```

## Racket

```racket
(define num-array%
  (class object%
    (super-new)
    
    ; nums : (listof exact-integer?)
    (init-field
      nums)
    
    ; internal BIT vector
    (define n (length nums))
    (define bit (make-vector (+ n 1) 0))
    
    (define (lowbit x)
      (bitwise-and x (- x)))
    
    (define (bit-add! i delta)
      (let loop ((i i))
        (when (< i (vector-length bit))
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (lowbit i))))))
    
    (define (prefix-sum i)
      (let loop ((i i) (s 0))
        (if (= i 0)
            s
            (loop (- i (lowbit i)) (+ s (vector-ref bit i))))))
    
    ; build BIT from initial nums
    (for ([idx (in-range n)])
      (bit-add! (+ idx 1) (list-ref nums idx)))
    
    ; update : exact-integer? exact-integer? -> void?
    (define/public (update index val)
      (let* ((old (list-ref nums index))
             (delta (- val old)))
        (set! nums (list-set nums index val))
        (bit-add! (+ index 1) delta)))
    
    ; sum-range : exact-integer? exact-integer? -> exact-integer?
    (define/public (sum-range left right)
      (- (prefix-sum (+ right 1)) (prefix-sum left)))) )
```

## Erlang

```erlang
-module(num_array).
-export([num_array_init_/1,
         num_array_update/2,
         num_array_sum_range/2]).

%% Initialize the data structure with the given list of numbers.
-spec num_array_init_(Nums :: [integer()]) -> any().
num_array_init_(Nums) ->
    N = length(Nums),
    Tree0 = array:new(N + 1, {default, 0}),
    Tree = init_tree(Tree0, Nums, 1, N),
    NumArr = array:from_list([0 | Nums]),   % 1‑based indexing
    put(numarray_state, #{tree => Tree, nums => NumArr, n => N}).

%% Update the value at index Index to Val.
-spec num_array_update(Index :: integer(), Val :: integer()) -> any().
num_array_update(Index, Val) ->
    State = get(numarray_state),
    N = maps:get(n, State),
    Tree = maps:get(tree, State),
    NumArr = maps:get(nums, State),
    I = Index + 1,
    OldVal = array:get(I, NumArr),
    Diff = Val - OldVal,
    NewNumArr = array:set(I, Val, NumArr),
    NewTree = update_bit(Tree, I, Diff, N),
    put(numarray_state, State#{tree => NewTree, nums => NewNumArr}).

%% Return the sum of elements between left and right (inclusive).
-spec num_array_sum_range(Left :: integer(), Right :: integer()) -> integer().
num_array_sum_range(Left, Right) ->
    State = get(numarray_state),
    Tree = maps:get(tree, State),
    L = Left + 1,
    R = Right + 1,
    prefix(R, Tree) - prefix(L - 1, Tree).

%% ---------- Helper functions ----------
init_tree(Tree, [], _, _) -> Tree;
init_tree(Tree, [H | T], Index, N) ->
    NewTree = update_bit(Tree, Index, H, N),
    init_tree(NewTree, T, Index + 1, N).

update_bit(Tree, Index, Delta, N) when Index =< N ->
    Old = array:get(Index, Tree),
    Updated = array:set(Index, Old + Delta, Tree),
    NextIdx = Index + (Index band -Index),
    update_bit(Updated, NextIdx, Delta, N);
update_bit(Tree, _, _) -> Tree.

prefix(Idx, Tree) when Idx > 0 ->
    prefix_loop(Idx, Tree, 0);
prefix(_, _) -> 0.

prefix_loop(0, _, Acc) -> Acc;
prefix_loop(I, Tree, Acc) ->
    Val = array:get(I, Tree),
    NewAcc = Acc + Val,
    NextI = I band (I - 1),
    prefix_loop(NextI, Tree, NewAcc).
```

## Elixir

```elixir
defmodule NumArray do
  require Bitwise

  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    n = length(nums)
    Process.put(:numarray_n, n)

    nums_arr = :array.from_list(nums)
    Process.put(:numarray_nums, nums_arr)

    bit = build_bit(nums, n)
    Process.put(:numarray_bit, bit)

    :ok
  end

  @spec update(index :: integer, val :: integer) :: any
  def update(index, val) do
    n = Process.get(:numarray_n)

    nums = Process.get(:numarray_nums)
    old_val = :array.get(index, nums)
    diff = val - old_val

    new_nums = :array.set(index, val, nums)
    Process.put(:numarray_nums, new_nums)

    bit = Process.get(:numarray_bit)
    new_bit = update_bit(bit, index + 1, diff, n)
    Process.put(:numarray_bit, new_bit)

    :ok
  end

  @spec sum_range(left :: integer, right :: integer) :: integer
  def sum_range(left, right) do
    bit = Process.get(:numarray_bit)
    prefix_right = query(bit, right + 1)
    prefix_left = query(bit, left)
    prefix_right - prefix_left
  end

  # Helper to build BIT from initial array
  defp build_bit(nums, n) do
    bit = :array.new(n + 1, default: 0)

    Enum.with_index(nums)
    |> Enum.reduce(bit, fn {val, i}, acc ->
      update_bit(acc, i + 1, val, n)
    end)
  end

  # Update BIT at position idx with delta
  defp update_bit(bit, idx, delta, n) when idx <= n do
    cur = :array.get(idx, bit)
    new_bit = :array.set(idx, cur + delta, bit)
    next_idx = idx + (idx &&& -idx)
    update_bit(new_bit, next_idx, delta, n)
  end

  defp update_bit(bit, idx, _delta, n) when idx > n, do: bit

  # Prefix sum query up to idx (inclusive)
  defp query(_bit, 0), do: 0

  defp query(bit, idx) do
    cur = :array.get(idx, bit)
    prev_idx = idx - (idx &&& -idx)
    cur + query(bit, prev_idx)
  end
end
```
