# 1865. Finding Pairs With a Certain Sum

## Cpp

```cpp
class FindSumPairs {
public:
    vector<int> nums1;
    vector<int> nums2;
    unordered_map<int,int> cnt;
    
    FindSumPairs(vector<int>& nums1_, vector<int>& nums2_) {
        nums1 = nums1_;
        nums2 = nums2_;
        for (int v : nums2) {
            ++cnt[v];
        }
    }
    
    void add(int index, int val) {
        int oldVal = nums2[index];
        auto itOld = cnt.find(oldVal);
        if (itOld != cnt.end()) {
            if (--(itOld->second) == 0) cnt.erase(itOld);
        }
        int newVal = oldVal + val;
        nums2[index] = newVal;
        ++cnt[newVal];
    }
    
    int count(int tot) {
        long long ans = 0;
        for (int x : nums1) {
            int need = tot - x;
            auto it = cnt.find(need);
            if (it != cnt.end()) ans += it->second;
        }
        return (int)ans;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
```

## Java

```java
class FindSumPairs {
    private int[] nums1;
    private int[] nums2;
    private java.util.HashMap<Integer, Integer> cnt;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1.clone();
        this.nums2 = nums2.clone();
        cnt = new java.util.HashMap<>();
        for (int v : nums2) {
            cnt.put(v, cnt.getOrDefault(v, 0) + 1);
        }
    }

    public void add(int index, int val) {
        int oldVal = nums2[index];
        int newVal = oldVal + val;
        // update nums2
        nums2[index] = newVal;

        // decrement count of old value
        int oldCount = cnt.get(oldVal);
        if (oldCount == 1) {
            cnt.remove(oldVal);
        } else {
            cnt.put(oldVal, oldCount - 1);
        }

        // increment count of new value
        cnt.put(newVal, cnt.getOrDefault(newVal, 0) + 1);
    }

    public int count(int tot) {
        long res = 0;
        for (int a : nums1) {
            int need = tot - a;
            res += cnt.getOrDefault(need, 0);
        }
        return (int) res;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */
```

## Python

```python
class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = {}
        for v in nums2:
            self.cnt[v] = self.cnt.get(v, 0) + 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        # decrement count of old value
        if self.cnt[old_val] == 1:
            del self.cnt[old_val]
        else:
            self.cnt[old_val] -= 1
        # increment count of new value
        self.cnt[new_val] = self.cnt.get(new_val, 0) + 1
        # update nums2
        self.nums2[index] = new_val

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        res = 0
        get = self.cnt.get
        for x in self.nums1:
            res += get(tot - x, 0)
        return res
```

## Python3

```python
class FindSumPairs:
    def __init__(self, nums1, nums2):
        from collections import Counter
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        old = self.nums2[index]
        new = old + val
        # update frequency map
        cnt_old = self.freq[old] - 1
        if cnt_old:
            self.freq[old] = cnt_old
        else:
            del self.freq[old]
        self.freq[new] = self.freq.get(new, 0) + 1
        self.nums2[index] = new

    def count(self, tot):
        total = 0
        get = self.freq.get
        for x in self.nums1:
            total += get(tot - x, 0)
        return total
```

## C

```c
#include <stdlib.h>
#include "uthash.h"

typedef struct {
    int key;
    int val;
    UT_hash_handle hh;
} HashNode;

typedef struct {
    int *nums1;
    int n1;
    int *nums2;
    int n2;
    HashNode *freq;
} FindSumPairs;

static void inc(HashNode **map, int key) {
    HashNode *node = NULL;
    HASH_FIND_INT(*map, &key, node);
    if (node) {
        node->val++;
    } else {
        node = (HashNode *)malloc(sizeof(HashNode));
        node->key = key;
        node->val = 1;
        HASH_ADD_INT(*map, key, node);
    }
}

static void dec(HashNode **map, int key) {
    HashNode *node = NULL;
    HASH_FIND_INT(*map, &key, node);
    if (!node) return;
    if (node->val == 1) {
        HASH_DEL(*map, node);
        free(node);
    } else {
        node->val--;
    }
}

FindSumPairs* findSumPairsCreate(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    FindSumPairs *obj = (FindSumPairs *)malloc(sizeof(FindSumPairs));
    obj->n1 = nums1Size;
    obj->n2 = nums2Size;
    obj->nums1 = (int *)malloc(nums1Size * sizeof(int));
    obj->nums2 = (int *)malloc(nums2Size * sizeof(int));
    for (int i = 0; i < nums1Size; ++i) obj->nums1[i] = nums1[i];
    for (int i = 0; i < nums2Size; ++i) {
        obj->nums2[i] = nums2[i];
        inc(&obj->freq, nums2[i]);
    }
    return obj;
}

void findSumPairsAdd(FindSumPairs* obj, int index, int val) {
    int old = obj->nums2[index];
    dec(&obj->freq, old);
    int nw = old + val;
    obj->nums2[index] = nw;
    inc(&obj->freq, nw);
}

int findSumPairsCount(FindSumPairs* obj, int tot) {
    long long ans = 0;
    for (int i = 0; i < obj->n1; ++i) {
        int need = tot - obj->nums1[i];
        HashNode *node = NULL;
        HASH_FIND_INT(obj->freq, &need, node);
        if (node) ans += node->val;
    }
    return (int)ans;
}

void findSumPairsFree(FindSumPairs* obj) {
    free(obj->nums1);
    free(obj->nums2);
    HashNode *cur, *tmp;
    HASH_ITER(hh, obj->freq, cur, tmp) {
        HASH_DEL(obj->freq, cur);
        free(cur);
    }
    free(obj);
}

/**
 * Your FindSumPairs struct will be instantiated and called as such:
 * FindSumPairs* obj = findSumPairsCreate(nums1, nums1Size, nums2, nums2Size);
 * findSumPairsAdd(obj, index, val);
 * int param_2 = findSumPairsCount(obj, tot);
 * findSumPairsFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class FindSumPairs
{
    private readonly int[] _nums1;
    private readonly int[] _nums2;
    private readonly Dictionary<int, int> _cnt;

    public FindSumPairs(int[] nums1, int[] nums2)
    {
        _nums1 = nums1;
        _nums2 = nums2;
        _cnt = new Dictionary<int, int>();
        foreach (int v in nums2)
        {
            if (_cnt.ContainsKey(v))
                _cnt[v]++;
            else
                _cnt[v] = 1;
        }
    }

    public void Add(int index, int val)
    {
        int oldVal = _nums2[index];
        // decrement count of the old value
        if (_cnt[oldVal] == 1)
            _cnt.Remove(oldVal);
        else
            _cnt[oldVal]--;

        int newVal = oldVal + val;
        _nums2[index] = newVal;

        if (_cnt.ContainsKey(newVal))
            _cnt[newVal]++;
        else
            _cnt[newVal] = 1;
    }

    public int Count(int tot)
    {
        long result = 0;
        foreach (int a in _nums1)
        {
            int need = tot - a;
            if (_cnt.TryGetValue(need, out int freq))
                result += freq;
        }
        return (int)result;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.Add(index,val);
 * int param_2 = obj.Count(tot);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 */
var FindSumPairs = function(nums1, nums2) {
    this.nums1 = nums1;
    this.nums2 = nums2;
    this.cnt = new Map();
    for (const v of nums2) {
        this.cnt.set(v, (this.cnt.get(v) || 0) + 1);
    }
};

/**
 * @param {number} index
 * @param {number} val
 * @return {void}
 */
FindSumPairs.prototype.add = function(index, val) {
    const oldVal = this.nums2[index];
    const newVal = oldVal + val;
    
    // decrement count of old value
    const oldCount = this.cnt.get(oldVal);
    if (oldCount === 1) {
        this.cnt.delete(oldVal);
    } else {
        this.cnt.set(oldVal, oldCount - 1);
    }
    
    // update nums2 and increment count of new value
    this.nums2[index] = newVal;
    this.cnt.set(newVal, (this.cnt.get(newVal) || 0) + 1);
};

/**
 * @param {number} tot
 * @return {number}
 */
FindSumPairs.prototype.count = function(tot) {
    let ans = 0;
    for (const a of this.nums1) {
        const need = tot - a;
        const c = this.cnt.get(need);
        if (c !== undefined) ans += c;
    }
    return ans;
};
```

## Typescript

```typescript
class FindSumPairs {
    private nums1: number[];
    private nums2: number[];
    private cnt: Map<number, number>;

    constructor(nums1: number[], nums2: number[]) {
        this.nums1 = nums1;
        this.nums2 = nums2.slice();
        this.cnt = new Map();
        for (const v of nums2) {
            this.cnt.set(v, (this.cnt.get(v) ?? 0) + 1);
        }
    }

    add(index: number, val: number): void {
        const oldVal = this.nums2[index];
        const oldCount = this.cnt.get(oldVal)!;
        if (oldCount === 1) {
            this.cnt.delete(oldVal);
        } else {
            this.cnt.set(oldVal, oldCount - 1);
        }
        const newVal = oldVal + val;
        this.nums2[index] = newVal;
        this.cnt.set(newVal, (this.cnt.get(newVal) ?? 0) + 1);
    }

    count(tot: number): number {
        let ans = 0;
        for (const a of this.nums1) {
            const need = tot - a;
            const c = this.cnt.get(need);
            if (c !== undefined) ans += c;
        }
        return ans;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */
```

## Php

```php
class FindSumPairs {
    private $nums1;
    private $nums2;
    private $cnt;

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     */
    function __construct($nums1, $nums2) {
        $this->nums1 = $nums1;
        $this->nums2 = $nums2;
        $this->cnt = [];
        foreach ($nums2 as $v) {
            if (!isset($this->cnt[$v])) {
                $this->cnt[$v] = 0;
            }
            $this->cnt[$v]++;
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function add($index, $val) {
        $old = $this->nums2[$index];
        $this->cnt[$old]--;
        if ($this->cnt[$old] == 0) {
            unset($this->cnt[$old]);
        }
        $new = $old + $val;
        $this->nums2[$index] = $new;
        if (!isset($this->cnt[$new])) {
            $this->cnt[$new] = 0;
        }
        $this->cnt[$new]++;
    }

    /**
     * @param Integer $tot
     * @return Integer
     */
    function count($tot) {
        $res = 0;
        foreach ($this->nums1 as $num) {
            $need = $tot - $num;
            if (isset($this->cnt[$need])) {
                $res += $this->cnt[$need];
            }
        }
        return $res;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * $obj = new FindSumPairs($nums1, $nums2);
 * $obj->add($index, $val);
 * $ret_2 = $obj->count($tot);
 */
```

## Swift

```swift
class FindSumPairs {
    private var nums1: [Int]
    private var nums2: [Int]
    private var freq: [Int: Int]

    init(_ nums1: [Int], _ nums2: [Int]) {
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = [:]
        for v in nums2 {
            self.freq[v, default: 0] += 1
        }
    }

    func add(_ index: Int, _ val: Int) {
        let oldVal = nums2[index]
        if let count = freq[oldVal] {
            if count == 1 {
                freq.removeValue(forKey: oldVal)
            } else {
                freq[oldVal] = count - 1
            }
        }
        let newVal = oldVal + val
        nums2[index] = newVal
        freq[newVal, default: 0] += 1
    }

    func count(_ tot: Int) -> Int {
        var result = 0
        for a in nums1 {
            let need = tot - a
            if let c = freq[need] {
                result += c
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class FindSumPairs(nums1: IntArray, nums2: IntArray) {
    private val nums1 = nums1
    private val nums2 = nums2
    private val cnt = HashMap<Int, Int>()

    init {
        for (v in nums2) {
            cnt[v] = (cnt[v] ?: 0) + 1
        }
    }

    fun add(index: Int, `val`: Int) {
        val oldVal = nums2[index]
        val newVal = oldVal + `val`

        // decrement count of old value
        cnt[oldVal]?.let {
            if (it == 1) cnt.remove(oldVal) else cnt[oldVal] = it - 1
        }

        // increment count of new value
        cnt[newVal] = (cnt[newVal] ?: 0) + 1

        nums2[index] = newVal
    }

    fun count(tot: Int): Int {
        var result = 0L
        for (a in nums1) {
            val need = tot - a
            cnt[need]?.let { result += it }
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class FindSumPairs {
  late List<int> _nums1;
  late List<int> _nums2;
  final Map<int, int> _cnt = {};

  FindSumPairs(List<int> nums1, List<int> nums2) {
    _nums1 = nums1;
    _nums2 = nums2;
    for (var v in nums2) {
      _cnt[v] = (_cnt[v] ?? 0) + 1;
    }
  }

  void add(int index, int val) {
    int oldVal = _nums2[index];
    int oldCount = _cnt[oldVal]!;
    if (oldCount == 1) {
      _cnt.remove(oldVal);
    } else {
      _cnt[oldVal] = oldCount - 1;
    }
    int newVal = oldVal + val;
    _nums2[index] = newVal;
    _cnt[newVal] = (_cnt[newVal] ?? 0) + 1;
  }

  int count(int tot) {
    int ans = 0;
    for (var a in _nums1) {
      int need = tot - a;
      if (_cnt.containsKey(need)) {
        ans += _cnt[need]!;
      }
    }
    return ans;
  }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param2 = obj.count(tot);
 */
```

## Golang

```go
type FindSumPairs struct {
	nums1 []int
	nums2 []int
	cnt   map[int]int
}

func Constructor(nums1 []int, nums2 []int) FindSumPairs {
	cnt := make(map[int]int)
	for _, v := range nums2 {
		cnt[v]++
	}
	return FindSumPairs{
		nums1: nums1,
		nums2: nums2,
		cnt:   cnt,
	}
}

func (this *FindSumPairs) Add(index int, val int) {
	oldVal := this.nums2[index]
	if c, ok := this.cnt[oldVal]; ok {
		if c == 1 {
			delete(this.cnt, oldVal)
		} else {
			this.cnt[oldVal] = c - 1
		}
	}
	newVal := oldVal + val
	this.nums2[index] = newVal
	this.cnt[newVal]++
}

func (this *FindSumPairs) Count(tot int) int {
	res := 0
	for _, a := range this.nums1 {
		if c, ok := this.cnt[tot-a]; ok {
			res += c
		}
	}
	return res
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * obj := Constructor(nums1, nums2);
 * obj.Add(index,val);
 * param_2 := obj.Count(tot);
 */
```

## Ruby

```ruby
class FindSumPairs
  # :type nums1: Integer[]
  # :type nums2: Integer[]
  def initialize(nums1, nums2)
    @nums1 = nums1
    @nums2 = nums2
    @cnt = Hash.new(0)
    nums2.each { |v| @cnt[v] += 1 }
  end

  # :type index: Integer
  # :type val: Integer
  # :rtype: Void
  def add(index, val)
    old_val = @nums2[index]
    @cnt[old_val] -= 1
    @cnt.delete(old_val) if @cnt[old_val] == 0

    new_val = old_val + val
    @nums2[index] = new_val
    @cnt[new_val] += 1
  end

  # :type tot: Integer
  # :rtype: Integer
  def count(tot)
    total = 0
    @nums1.each do |num|
      need = tot - num
      total += @cnt[need]
    end
    total
  end
end
```

## Scala

```scala
import scala.collection.mutable

class FindSumPairs(_nums1: Array[Int], _nums2: Array[Int]) {

  private val nums1: Array[Int] = _nums1
  private val nums2: Array[Int] = _nums2.clone()
  private val cnt: mutable.HashMap[Int, Int] = mutable.HashMap()

  for (v <- nums2) {
    cnt.put(v, cnt.getOrElse(v, 0) + 1)
  }

  def add(index: Int, `val`: Int): Unit = {
    val oldVal = nums2(index)
    val newVal = oldVal + `val`

    // decrement count of old value
    cnt.get(oldVal) match {
      case Some(c) if c == 1 => cnt.remove(oldVal)
      case Some(c)           => cnt.put(oldVal, c - 1)
      case None              => // should not happen
    }

    // increment count of new value
    cnt.put(newVal, cnt.getOrElse(newVal, 0) + 1)

    nums2(index) = newVal
  }

  def count(tot: Int): Int = {
    var ans: Long = 0L
    for (a <- nums1) {
      val needLong = tot.toLong - a.toLong
      if (needLong >= Int.MinValue && needLong <= Int.MaxValue) {
        ans += cnt.getOrElse(needLong.toInt, 0)
      }
    }
    ans.toInt
  }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * val obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,`val`)
 * val param_2 = obj.count(tot)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct FindSumPairs {
    nums1: Vec<i32>,
    nums2: Vec<i32>,
    cnt: HashMap<i32, i32>,
}

impl FindSumPairs {
    fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        let mut cnt = HashMap::new();
        for &v in &nums2 {
            *cnt.entry(v).or_insert(0) += 1;
        }
        FindSumPairs { nums1, nums2, cnt }
    }

    fn add(&mut self, index: i32, val: i32) {
        let idx = index as usize;
        let old = self.nums2[idx];
        if let Some(entry) = self.cnt.get_mut(&old) {
            *entry -= 1;
            if *entry == 0 {
                self.cnt.remove(&old);
            }
        }
        let new_val = old + val;
        self.nums2[idx] = new_val;
        *self.cnt.entry(new_val).or_insert(0) += 1;
    }

    fn count(&self, tot: i32) -> i32 {
        let mut res: i64 = 0;
        for &a in &self.nums1 {
            if let Some(c) = self.cnt.get(&(tot - a)) {
                res += *c as i64;
            }
        }
        res as i32
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs::new(nums1, nums2);
 * obj.add(index, val);
 * let ret_2: i32 = obj.count(tot);
 */
```

## Racket

```racket
(define find-sum-pairs%
  (class object%
    (super-new)
    ;; constructor arguments
    (init-field nums1 nums2)   ; both are lists
    
    ;; internal mutable fields
    (field [vec2 #f]           ; vector version of nums2 for O(1) updates
           [cnt  #f])          ; hash table: value -> frequency
    
    ;; initialization code
    (begin
      (set! vec2 (list->vector nums2))
      (set! cnt (make-hash))
      (for ([v (in-vector vec2)])
        (hash-set! cnt v (+ 1 (hash-ref cnt v 0)))))
    
    ;; add operation: increment nums2[index] by val
    (define/public (add index val)
      (let* ([old (vector-ref vec2 index)]
             [new (+ old val)])
        ;; decrement count of old value
        (hash-set! cnt old (- (hash-ref cnt old) 1))
        (when (= (hash-ref cnt old) 0)
          (hash-remove! cnt old))
        ;; update nums2 vector
        (vector-set! vec2 index new)
        ;; increment count of new value
        (hash-set! cnt new (+ 1 (hash-ref cnt new 0)))))
    
    ;; count operation: number of pairs (i,j) with nums1[i] + nums2[j] == tot
    (define/public (count tot)
      (let ([total 0])
        (for ([x nums1])
          (set! total (+ total (hash-ref cnt (- tot x) 0))))
        total))))
```

## Erlang

```erlang
-spec find_sum_pairs_init_(Nums1 :: [integer()], Nums2 :: [integer()]) -> any().
find_sum_pairs_init_(Nums1, Nums2) ->
    Tuple2 = list_to_tuple(Nums2),
    CountMap = build_count_map(Nums2, #{}),
    put(nums1, Nums1),
    put(nums2, Tuple2),
    put(cnt, CountMap).

-spec find_sum_pairs_add(Index :: integer(), Val :: integer()) -> any().
find_sum_pairs_add(Index, Val) ->
    Tuple = get(nums2),
    OldVal = element(Index + 1, Tuple),
    Cnt0 = get(cnt),

    % decrement count of old value
    Cnt1 = case maps:get(OldVal, Cnt0) of
        1 -> maps:remove(OldVal, Cnt0);
        N -> maps:put(OldVal, N - 1, Cnt0)
    end,

    NewVal = OldVal + Val,
    Tuple2 = setelement(Index + 1, Tuple, NewVal),

    % increment count of new value
    Cnt2 = case maps:is_key(NewVal, Cnt1) of
        true -> maps:update_with(NewVal, fun(V) -> V + 1 end, 1, Cnt1);
        false -> maps:put(NewVal, 1, Cnt1)
    end,

    put(nums2, Tuple2),
    put(cnt, Cnt2).

-spec find_sum_pairs_count(Tot :: integer()) -> integer().
find_sum_pairs_count(Tot) ->
    Nums1 = get(nums1),
    Cnt = get(cnt),
    lists:foldl(fun(N, Acc) -> Acc + maps:get(Tot - N, Cnt, 0) end, 0, Nums1).

%% helper
build_count_map([], Map) -> Map;
build_count_map([H|T], Map) ->
    NewMap = maps:update_with(H, fun(V) -> V + 1 end, 1, Map),
    build_count_map(T, NewMap).
```

## Elixir

```elixir
defmodule FindSumPairs do
  @spec init_(nums1 :: [integer], nums2 :: [integer]) :: any
  def init_(nums1, nums2) do
    cnt =
      Enum.reduce(nums2, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    num2_map =
      nums2
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {v, i}, acc -> Map.put(acc, i, v) end)

    Process.put(:nums1, nums1)
    Process.put(:cnt, cnt)
    Process.put(:num2_map, num2_map)
    :ok
  end

  @spec add(index :: integer, val :: integer) :: any
  def add(index, val) do
    num2_map = Process.get(:num2_map)
    old_val = Map.fetch!(num2_map, index)
    new_val = old_val + val

    # update nums2 map
    Process.put(:num2_map, Map.put(num2_map, index, new_val))

    cnt = Process.get(:cnt)

    cnt =
      case Map.get(cnt, old_val) do
        nil -> cnt
        1 -> Map.delete(cnt, old_val)
        n when n > 1 -> Map.put(cnt, old_val, n - 1)
      end

    cnt = Map.update(cnt, new_val, 1, &(&1 + 1))
    Process.put(:cnt, cnt)
    :ok
  end

  @spec count(tot :: integer) :: integer
  def count(tot) do
    nums1 = Process.get(:nums1)
    cnt = Process.get(:cnt)

    Enum.reduce(nums1, 0, fn x, acc ->
      need = tot - x
      acc + Map.get(cnt, need, 0)
    end)
  end
end
```
