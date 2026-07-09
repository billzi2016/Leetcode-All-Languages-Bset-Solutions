# 0380. Insert Delete GetRandom O(1)

## Cpp

```cpp
#include <vector>
#include <unordered_map>
#include <cstdlib>

class RandomizedSet {
public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (pos.find(val) != pos.end()) return false;
        nums.push_back(val);
        pos[val] = nums.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        auto it = pos.find(val);
        if (it == pos.end()) return false;
        int idx = it->second;
        int last = nums.back();
        nums[idx] = last;
        pos[last] = idx;
        nums.pop_back();
        pos.erase(it);
        return true;
    }
    
    int getRandom() {
        int idx = std::rand() % nums.size();
        return nums[idx];
    }

private:
    std::vector<int> nums;
    std::unordered_map<int, int> pos;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

## Java

```java
import java.util.*;

class RandomizedSet {
    private final List<Integer> list;
    private final Map<Integer, Integer> map;
    private final Random rand;

    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }
        map.put(val, list.size());
        list.add(val);
        return true;
    }

    public boolean remove(int val) {
        Integer idx = map.get(val);
        if (idx == null) {
            return false;
        }
        int lastIdx = list.size() - 1;
        int lastVal = list.get(lastIdx);
        // Move the last element to the spot of the element to delete
        list.set(idx, lastVal);
        map.put(lastVal, idx);
        // Remove last element
        list.remove(lastIdx);
        map.remove(val);
        return true;
    }

    public int getRandom() {
        int randomIndex = rand.nextInt(list.size());
        return list.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

## Python

```python
class RandomizedSet(object):
    def __init__(self):
        self.nums = []
        self.idx_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        last_val = self.nums[-1]
        # Move the last element to the spot of the element to delete
        self.nums[idx] = last_val
        self.idx_map[last_val] = idx
        # Remove last element
        self.nums.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        return random.choice(self.nums)
```

## Python3

```python
import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

## C

```c
typedef struct {
    int *arr;
    int size;
    int capacity;

    int *map_key;   // key -> value
    int *map_val;   // index in arr
    char *map_state; // 0 = empty, 1 = occupied, 2 = deleted
    int map_capacity;
} RandomizedSet;

/* hash function for integers */
static unsigned int hash_int(int x) {
    return ((unsigned int)x * 2654435761u);
}

/* ensure dynamic array has space */
static void ensure_array_capacity(RandomizedSet *obj) {
    if (obj->size < obj->capacity) return;
    int newCap = obj->capacity ? obj->capacity * 2 : 4;
    obj->arr = realloc(obj->arr, sizeof(int) * newCap);
    obj->capacity = newCap;
}

/* find index of key in hashmap; -1 if not present */
static int hashmap_find(RandomizedSet *obj, int key) {
    unsigned int h = hash_int(key);
    int mask = obj->map_capacity - 1;
    int idx = h & mask;
    while (obj->map_state[idx] != 0) { // while not empty
        if (obj->map_state[idx] == 1 && obj->map_key[idx] == key)
            return idx;
        idx = (idx + 1) & mask;
    }
    return -1;
}

/* insert key with associated array index; assumes key not present */
static void hashmap_insert(RandomizedSet *obj, int key, int arr_idx) {
    unsigned int h = hash_int(key);
    int mask = obj->map_capacity - 1;
    int idx = h & mask;
    while (obj->map_state[idx] == 1) { // occupied
        idx = (idx + 1) & mask;
    }
    obj->map_key[idx] = key;
    obj->map_val[idx] = arr_idx;
    obj->map_state[idx] = 1; // occupy
}

/* delete key from hashmap (lazy deletion) */
static void hashmap_erase(RandomizedSet *obj, int key) {
    int idx = hashmap_find(obj, key);
    if (idx != -1)
        obj->map_state[idx] = 2; // mark as deleted
}

RandomizedSet* randomizedSetCreate() {
    RandomizedSet *obj = malloc(sizeof(RandomizedSet));
    obj->capacity = 4;
    obj->size = 0;
    obj->arr = malloc(sizeof(int) * obj->capacity);

    /* hashmap size: power of two larger than expected max elements */
    obj->map_capacity = 1 << 20;               // 1048576
    obj->map_key = malloc(sizeof(int) * obj->map_capacity);
    obj->map_val = malloc(sizeof(int) * obj->map_capacity);
    obj->map_state = calloc(obj->map_capacity, sizeof(char)); // all zero (empty)

    return obj;
}

bool randomizedSetInsert(RandomizedSet* obj, int val) {
    if (hashmap_find(obj, val) != -1)
        return false;

    ensure_array_capacity(obj);
    obj->arr[obj->size] = val;
    hashmap_insert(obj, val, obj->size);
    obj->size++;
    return true;
}

bool randomizedSetRemove(RandomizedSet* obj, int val) {
    int mapIdx = hashmap_find(obj, val);
    if (mapIdx == -1)
        return false;

    int arrIdx = obj->map_val[mapIdx];
    int lastVal = obj->arr[obj->size - 1];

    /* move last element into the spot of the removed element */
    obj->arr[arrIdx] = lastVal;
    if (lastVal != val) {
        int lastMapIdx = hashmap_find(obj, lastVal);
        obj->map_val[lastMapIdx] = arrIdx;
    }

    obj->size--;
    hashmap_erase(obj, val);
    return true;
}

int randomizedSetGetRandom(RandomizedSet* obj) {
    int idx = rand() % obj->size;
    return obj->arr[idx];
}

void randomizedSetFree(RandomizedSet* obj) {
    if (!obj) return;
    free(obj->arr);
    free(obj->map_key);
    free(obj->map_val);
    free(obj->map_state);
    free(obj);
}

/**
 * Your RandomizedSet struct will be instantiated and called as such:
 * RandomizedSet* obj = randomizedSetCreate();
 * bool param_1 = randomizedSetInsert(obj, val);
 *
 * bool param_2 = randomizedSetRemove(obj, val);
 *
 * int param_3 = randomizedSetGetRandom(obj);
 *
 * randomizedSetFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class RandomizedSet {
    private List<int> nums;
    private Dictionary<int, int> idxMap;
    private Random rand;

    public RandomizedSet() {
        nums = new List<int>();
        idxMap = new Dictionary<int, int>();
        rand = new Random();
    }
    
    public bool Insert(int val) {
        if (idxMap.ContainsKey(val)) return false;
        idxMap[val] = nums.Count;
        nums.Add(val);
        return true;
    }
    
    public bool Remove(int val) {
        if (!idxMap.TryGetValue(val, out int index)) return false;
        int lastElement = nums[nums.Count - 1];
        nums[index] = lastElement;
        idxMap[lastElement] = index;
        nums.RemoveAt(nums.Count - 1);
        idxMap.Remove(val);
        return true;
    }
    
    public int GetRandom() {
        int randomIndex = rand.Next(nums.Count);
        return nums[randomIndex];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.Insert(val);
 * bool param_2 = obj.Remove(val);
 * int param_3 = obj.GetRandom();
 */
```

## Javascript

```javascript
var RandomizedSet = function() {
    this.idxMap = new Map();
    this.values = [];
};

RandomizedSet.prototype.insert = function(val) {
    if (this.idxMap.has(val)) return false;
    this.values.push(val);
    this.idxMap.set(val, this.values.length - 1);
    return true;
};

RandomizedSet.prototype.remove = function(val) {
    if (!this.idxMap.has(val)) return false;
    const idx = this.idxMap.get(val);
    const lastVal = this.values[this.values.length - 1];
    this.values[idx] = lastVal;
    this.idxMap.set(lastVal, idx);
    this.values.pop();
    this.idxMap.delete(val);
    return true;
};

RandomizedSet.prototype.getRandom = function() {
    const randIdx = Math.floor(Math.random() * this.values.length);
    return this.values[randIdx];
};
```

## Typescript

```typescript
class RandomizedSet {
    private nums: number[];
    private idxMap: Map<number, number>;

    constructor() {
        this.nums = [];
        this.idxMap = new Map();
    }

    insert(val: number): boolean {
        if (this.idxMap.has(val)) return false;
        this.idxMap.set(val, this.nums.length);
        this.nums.push(val);
        return true;
    }

    remove(val: number): boolean {
        if (!this.idxMap.has(val)) return false;
        const idx = this.idxMap.get(val)!;
        const lastVal = this.nums[this.nums.length - 1];
        this.nums[idx] = lastVal;
        this.idxMap.set(lastVal, idx);
        this.nums.pop();
        this.idxMap.delete(val);
        return true;
    }

    getRandom(): number {
        const randIdx = Math.floor(Math.random() * this.nums.length);
        return this.nums[randIdx];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

## Php

```php
class RandomizedSet {
    private $list;
    private $pos;

    function __construct() {
        $this->list = [];
        $this->pos = [];
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        if (isset($this->pos[$val])) {
            return false;
        }
        $this->list[] = $val;
        $this->pos[$val] = count($this->list) - 1;
        return true;
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        if (!isset($this->pos[$val])) {
            return false;
        }
        $idx = $this->pos[$val];
        $lastIdx = count($this->list) - 1;
        $lastVal = $this->list[$lastIdx];

        // Move the last element to the spot of the element to delete
        $this->list[$idx] = $lastVal;
        $this->pos[$lastVal] = $idx;

        // Remove the last element
        array_pop($this->list);
        unset($this->pos[$val]);

        return true;
    }

    /**
     * @return Integer
     */
    function getRandom() {
        $randIdx = mt_rand(0, count($this->list) - 1);
        return $this->list[$randIdx];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * $obj = new RandomizedSet();
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->remove($val);
 * $ret_3 = $obj->getRandom();
 */
```

## Swift

```swift
class RandomizedSet {
    private var indexMap: [Int: Int] = [:]
    private var values: [Int] = []
    
    init() { }
    
    func insert(_ val: Int) -> Bool {
        if indexMap[val] != nil { return false }
        indexMap[val] = values.count
        values.append(val)
        return true
    }
    
    func remove(_ val: Int) -> Bool {
        guard let idx = indexMap[val] else { return false }
        let lastVal = values[values.count - 1]
        values[idx] = lastVal
        indexMap[lastVal] = idx
        values.removeLast()
        indexMap.removeValue(forKey: val)
        return true
    }
    
    func getRandom() -> Int {
        let randomIdx = Int.random(in: 0..<values.count)
        return values[randomIdx]
    }
}
```

## Kotlin

```kotlin
class RandomizedSet() {

    private val list = ArrayList<Int>()
    private val map = HashMap<Int, Int>()

    fun insert(`val`: Int): Boolean {
        if (map.containsKey(`val`)) return false
        map[`val`] = list.size
        list.add(`val`)
        return true
    }

    fun remove(`val`: Int): Boolean {
        val idx = map[`val`] ?: return false
        val lastIdx = list.size - 1
        val lastVal = list[lastIdx]
        list[idx] = lastVal
        map[lastVal] = idx
        list.removeAt(lastIdx)
        map.remove(`val`)
        return true
    }

    fun getRandom(): Int {
        val randIndex = kotlin.random.Random.nextInt(list.size)
        return list[randIndex]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = RandomizedSet()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
 */
```

## Dart

```dart
import 'dart:math';

class RandomizedSet {
  final List<int> _list = [];
  final Map<int, int> _map = {};
  final Random _rand = Random();

  RandomizedSet() {}

  bool insert(int val) {
    if (_map.containsKey(val)) return false;
    _map[val] = _list.length;
    _list.add(val);
    return true;
  }

  bool remove(int val) {
    if (!_map.containsKey(val)) return false;
    int idx = _map[val]!;
    int lastVal = _list.last;
    _list[idx] = lastVal;
    _map[lastVal] = idx;
    _list.removeLast();
    _map.remove(val);
    return true;
  }

  int getRandom() {
    int idx = _rand.nextInt(_list.length);
    return _list[idx];
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = RandomizedSet();
 * bool param1 = obj.insert(val);
 * bool param2 = obj.remove(val);
 * int param3 = obj.getRandom();
 */
```

## Golang

```go
import (
	"math/rand"
)

type RandomizedSet struct {
	nums []int
	idx  map[int]int
}

func Constructor() RandomizedSet {
	return RandomizedSet{
		nums: make([]int, 0),
		idx:  make(map[int]int),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, exists := this.idx[val]; exists {
		return false
	}
	this.nums = append(this.nums, val)
	this.idx[val] = len(this.nums) - 1
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	i, exists := this.idx[val]
	if !exists {
		return false
	}
	lastIdx := len(this.nums) - 1
	lastVal := this.nums[lastIdx]

	this.nums[i] = lastVal
	this.idx[lastVal] = i

	this.nums = this.nums[:lastIdx]
	delete(this.idx, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	return this.nums[rand.Intn(len(this.nums))]
}
```

## Ruby

```ruby
class RandomizedSet
    def initialize()
        @arr = []
        @idx = {}
    end

=begin
    :type val: Integer
    :rtype: Boolean
=end
    def insert(val)
        return false if @idx.key?(val)
        @arr << val
        @idx[val] = @arr.length - 1
        true
    end

=begin
    :type val: Integer
    :rtype: Boolean
=end
    def remove(val)
        return false unless @idx.key?(val)
        i = @idx[val]
        last = @arr[-1]
        @arr[i] = last
        @idx[last] = i
        @arr.pop
        @idx.delete(val)
        true
    end

=begin
    :rtype: Integer
=end
    def get_random()
        @arr[rand(@arr.length)]
    end
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, HashMap}
import scala.util.Random

class RandomizedSet() {

  private val arr = new ArrayBuffer[Int]()
  private val idx = new HashMap[Int, Int]()

  def insert(`val`: Int): Boolean = {
    if (idx.contains(`val`)) false
    else {
      idx(`val`) = arr.length
      arr.append(`val`)
      true
    }
  }

  def remove(`val`: Int): Boolean = {
    idx.get(`val`) match {
      case None => false
      case Some(i) =>
        val lastIdx = arr.length - 1
        val lastVal = arr(lastIdx)
        arr(i) = lastVal
        idx(lastVal) = i
        arr.remove(lastIdx)
        idx -= `val`
        true
    }
  }

  def getRandom(): Int = {
    val randIdx = Random.nextInt(arr.length)
    arr(randIdx)
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * val obj = new RandomizedSet()
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.remove(`val`)
 * val param_3 = obj.getRandom()
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;
use rand::prelude::*;

struct RandomizedSet {
    nums: RefCell<Vec<i32>>,
    idx_map: RefCell<HashMap<i32, usize>>,
    rng: RefCell<ThreadRng>,
}

impl RandomizedSet {
    fn new() -> Self {
        RandomizedSet {
            nums: RefCell::new(Vec::new()),
            idx_map: RefCell::new(HashMap::new()),
            rng: RefCell::new(thread_rng()),
        }
    }

    fn insert(&self, val: i32) -> bool {
        let mut map = self.idx_map.borrow_mut();
        if map.contains_key(&val) {
            return false;
        }
        let mut nums = self.nums.borrow_mut();
        nums.push(val);
        map.insert(val, nums.len() - 1);
        true
    }

    fn remove(&self, val: i32) -> bool {
        let mut map = self.idx_map.borrow_mut();
        if let Some(&idx) = map.get(&val) {
            let mut nums = self.nums.borrow_mut();
            let last = *nums.last().unwrap();
            nums[idx] = last;
            map.insert(last, idx);
            nums.pop();
            map.remove(&val);
            true
        } else {
            false
        }
    }

    fn get_random(&self) -> i32 {
        let nums = self.nums.borrow();
        let len = nums.len();
        let mut rng = self.rng.borrow_mut();
        let idx = rng.gen_range(0..len);
        nums[idx]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
```

## Racket

```racket
(define randomized-set%
  (class object%
    (super-new)
    
    (field [vec (make-vector 4)]
           [size 0]
           [map (make-hash)])
    
    ;; insert : exact-integer? -> boolean?
    (define/public (insert val)
      (if (hash-has-key? map val)
          #f
          (begin
            (when (= size (vector-length vec))
              (define new-cap (* 2 (max 1 (vector-length vec))))
              (define new-vec (make-vector new-cap))
              (for ([i (in-range size)])
                (vector-set! new-vec i (vector-ref vec i)))
              (set! vec new-vec))
            (vector-set! vec size val)
            (hash-set! map val size)
            (set! size (+ size 1))
            #t)))
    
    ;; remove : exact-integer? -> boolean?
    (define/public (remove val)
      (if (not (hash-has-key? map val))
          #f
          (begin
            (define idx (hash-ref map val))
            (define last-index (- size 1))
            (define last-val (vector-ref vec last-index))
            (when (not (= idx last-index))
              (vector-set! vec idx last-val)
              (hash-set! map last-val idx))
            (set! size last-index)
            (hash-remove! map val)
            #t)))
    
    ;; get-random : -> exact-integer?
    (define/public (get-random)
      (define idx (random size))
      (vector-ref vec idx))))
```

## Erlang

```erlang
-module(solution).
-export([randomized_set_init_/0,
         randomized_set_insert/1,
         randomized_set_remove/1,
         randomized_set_get_random/0]).

-spec randomized_set_init_() -> any().
randomized_set_init_() ->
    case ets:info(rand_set_val_to_idx) of
        undefined -> ok;
        _ -> ets:delete(rand_set_val_to_idx)
    end,
    case ets:info(rand_set_idx_to_val) of
        undefined -> ok;
        _ -> ets:delete(rand_set_idx_to_val)
    end,
    ets:new(rand_set_val_to_idx, [named_table, public, set]),
    ets:new(rand_set_idx_to_val, [named_table, public, set]),
    put(rand_set_size, 0),
    ok.

-spec randomized_set_insert(Val :: integer()) -> boolean().
randomized_set_insert(Val) ->
    case ets:lookup(rand_set_val_to_idx, Val) of
        [] ->
            Size = get(rand_set_size),
            Idx = Size,
            ets:insert(rand_set_val_to_idx, {Val, Idx}),
            ets:insert(rand_set_idx_to_val, {Idx, Val}),
            put(rand_set_size, Size + 1),
            true;
        _ -> false
    end.

-spec randomized_set_remove(Val :: integer()) -> boolean().
randomized_set_remove(Val) ->
    case ets:lookup(rand_set_val_to_idx, Val) of
        [] -> false;
        [{Val, Idx}] ->
            Size = get(rand_set_size),
            LastIdx = Size - 1,
            [{LastIdx, LastVal}] = ets:lookup(rand_set_idx_to_val, LastIdx),
            case Idx == LastIdx of
                true -> ok;
                false ->
                    ets:insert(rand_set_val_to_idx, {LastVal, Idx}),
                    ets:insert(rand_set_idx_to_val, {Idx, LastVal})
            end,
            ets:delete(rand_set_val_to_idx, Val),
            ets:delete(rand_set_idx_to_val, LastIdx),
            put(rand_set_size, Size - 1),
            true
    end.

-spec randomized_set_get_random() -> integer().
randomized_set_get_random() ->
    Size = get(rand_set_size),
    RandIdx = rand:uniform(Size) - 1,
    [{RandIdx, Val}] = ets:lookup(rand_set_idx_to_val, RandIdx),
    Val.
```

## Elixir

```elixir
defmodule RandomizedSet do
  @spec init_() :: any
  def init_() do
    Process.put(:rand_set_state, %{map: %{}, idx: %{}, size: 0})
    :ok
  end

  @spec insert(val :: integer) :: boolean
  def insert(val) do
    state = Process.get(:rand_set_state)

    if Map.has_key?(state.idx, val) do
      false
    else
      idx = state.size
      new_map = Map.put(state.map, idx, val)
      new_idx = Map.put(state.idx, val, idx)
      new_state = %{state | map: new_map, idx: new_idx, size: idx + 1}
      Process.put(:rand_set_state, new_state)
      true
    end
  end

  @spec remove(val :: integer) :: boolean
  def remove(val) do
    state = Process.get(:rand_set_state)

    case Map.fetch(state.idx, val) do
      :error ->
        false

      {:ok, remove_idx} ->
        last_idx = state.size - 1
        {new_map, new_idx} =
          if remove_idx == last_idx do
            {
              Map.delete(state.map, last_idx),
              Map.delete(state.idx, val)
            }
          else
            last_val = Map.fetch!(state.map, last_idx)

            map_after_swap =
              state.map
              |> Map.put(remove_idx, last_val)
              |> Map.delete(last_idx)

            idx_after_swap =
              state.idx
              |> Map.put(last_val, remove_idx)
              |> Map.delete(val)

            {map_after_swap, idx_after_swap}
          end

        new_state = %{state | map: new_map, idx: new_idx, size: last_idx}
        Process.put(:rand_set_state, new_state)
        true
    end
  end

  @spec get_random() :: integer
  def get_random() do
    state = Process.get(:rand_set_state)
    size = state.size
    rand_idx = :rand.uniform(size) - 1
    Map.fetch!(state.map, rand_idx)
  end
end
```
