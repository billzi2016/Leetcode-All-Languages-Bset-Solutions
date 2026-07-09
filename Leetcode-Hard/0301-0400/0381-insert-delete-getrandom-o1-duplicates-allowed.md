# 0381. Insert Delete GetRandom O(1) - Duplicates allowed

## Cpp

```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <random>

class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() : gen(rd()) {}

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool notPresent = (idx.find(val) == idx.end()) || idx[val].empty();
        nums.push_back(val);
        idx[val].insert(nums.size() - 1);
        return notPresent;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        auto it = idx.find(val);
        if (it == idx.end() || it->second.empty()) return false;

        // Get an arbitrary index of the element to remove
        int removeIdx = *it->second.begin();

        int lastVal = nums.back();
        int lastIdx = nums.size() - 1;

        // Move last element into the spot of the element to delete, if not the same
        nums[removeIdx] = lastVal;
        // Update the indices set for lastVal
        idx[lastVal].erase(lastIdx);
        if (removeIdx != lastIdx) {
            idx[lastVal].insert(removeIdx);
        }

        // Remove the index from val's set
        it->second.erase(removeIdx);
        if (it->second.empty()) {
            idx.erase(it);
        }

        nums.pop_back();
        return true;
    }

    /** Get a random element from the collection. */
    int getRandom() {
        std::uniform_int_distribution<int> dist(0, static_cast<int>(nums.size()) - 1);
        return nums[dist(gen)];
    }

private:
    std::vector<int> nums;
    std::unordered_map<int, std::unordered_set<int>> idx;
    std::random_device rd;
    std::mt19937 gen;
};
```

## Java

```java
import java.util.*;

class RandomizedCollection {
    private List<Integer> nums;
    private Map<Integer, Set<Integer>> idxMap;
    private Random rand;

    public RandomizedCollection() {
        nums = new ArrayList<>();
        idxMap = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        boolean notPresent = !idxMap.containsKey(val);
        idxMap.computeIfAbsent(val, k -> new HashSet<>()).add(nums.size());
        nums.add(val);
        return notPresent;
    }

    public boolean remove(int val) {
        Set<Integer> set = idxMap.get(val);
        if (set == null || set.isEmpty()) {
            return false;
        }
        int idxToRemove = set.iterator().next();
        set.remove(idxToRemove);

        int lastIdx = nums.size() - 1;
        int lastVal = nums.get(lastIdx);

        if (idxToRemove != lastIdx) {
            nums.set(idxToRemove, lastVal);
            Set<Integer> lastSet = idxMap.get(lastVal);
            lastSet.remove(lastIdx);
            lastSet.add(idxToRemove);
        }

        nums.remove(lastIdx);

        if (set.isEmpty()) {
            idxMap.remove(val);
        }
        return true;
    }

    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

## Python

```python
import random
from collections import defaultdict

class RandomizedCollection(object):
    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.idx[val].add(len(self.nums) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not self.idx.get(val):
            return False
        # Index of element to remove
        remove_idx = self.idx[val].pop()
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        if remove_idx != last_idx:
            # Move the last element into the spot vacated by remove_idx
            self.nums[remove_idx] = last_val
            # Update the indices set for the moved element
            self.idx[last_val].remove(last_idx)
            self.idx[last_val].add(remove_idx)

        # Remove the last element from list
        self.nums.pop()
        if not self.idx[val]:
            del self.idx[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)
```

## Python3

```python
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.idx[val].add(len(self.nums) - 1)
        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx.get(val):
            return False
        remove_idx = self.idx[val].pop()
        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1
        if remove_idx != last_idx:
            self.nums[remove_idx] = last_val
            self.idx[last_val].remove(last_idx)
            self.idx[last_val].add(remove_idx)
        self.nums.pop()
        if not self.idx[val]:
            del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include "uthash.h"

typedef struct {
    int *indices;          // dynamic array of global indices
    int size;
    int capacity;
    int key;               // the value itself (hash key)
    UT_hash_handle hh;     // hash handle for uthash
} ValueIndices;

typedef struct {
    int val;       // value at this position
    int idxPos;    // position of this index inside its ValueIndices->indices array
} ElemInfo;

typedef struct {
    int *vals;               // dynamic array of values
    ElemInfo *infos;         // parallel array storing metadata for each index
    int size;
    int capacity;
    ValueIndices *map;       // hash table from value to its indices list
} RandomizedCollection;

/* Helper: ensure the main arrays have enough capacity */
static void ensureCapacity(RandomizedCollection *obj) {
    if (obj->size >= obj->capacity) {
        int newCap = obj->capacity ? obj->capacity * 2 : 4;
        obj->vals = realloc(obj->vals, newCap * sizeof(int));
        obj->infos = realloc(obj->infos, newCap * sizeof(ElemInfo));
        obj->capacity = newCap;
    }
}

/* Helper: ensure a ValueIndices structure has enough capacity for its indices array */
static void ensureViCapacity(ValueIndices *vi) {
    if (vi->size >= vi->capacity) {
        int newCap = vi->capacity ? vi->capacity * 2 : 4;
        vi->indices = realloc(vi->indices, newCap * sizeof(int));
        vi->capacity = newCap;
    }
}

/* Create a new RandomizedCollection */
RandomizedCollection* randomizedCollectionCreate() {
    RandomizedCollection *obj = malloc(sizeof(RandomizedCollection));
    obj->vals = NULL;
    obj->infos = NULL;
    obj->size = 0;
    obj->capacity = 0;
    obj->map = NULL;
    return obj;
}

/* Insert a value. Returns true if the collection did not already contain the specified element. */
bool randomizedCollectionInsert(RandomizedCollection* obj, int val) {
    ensureCapacity(obj);
    int idx = obj->size;

    // Append value
    obj->vals[idx] = val;

    // Find or create ValueIndices for this value
    ValueIndices *vi = NULL;
    HASH_FIND_INT(obj->map, &val, vi);
    bool firstInsert = false;
    if (!vi) {
        vi = (ValueIndices *)malloc(sizeof(ValueIndices));
        vi->key = val;
        vi->size = 0;
        vi->capacity = 0;
        vi->indices = NULL;
        HASH_ADD_INT(obj->map, key, vi);
        firstInsert = true;
    }

    // Add index to the value's indices list
    ensureViCapacity(vi);
    int posInVi = vi->size;
    vi->indices[posInVi] = idx;
    vi->size++;

    // Store metadata for this position
    obj->infos[idx].val = val;
    obj->infos[idx].idxPos = posInVi;

    obj->size++;
    return firstInsert;
}

/* Remove a value. Returns true if the collection contained the specified element. */
bool randomizedCollectionRemove(RandomizedCollection* obj, int val) {
    ValueIndices *vi = NULL;
    HASH_FIND_INT(obj->map, &val, vi);
    if (!vi || vi->size == 0) return false;

    // Index to remove: take last index from the value's list
    int idxToRemove = vi->indices[vi->size - 1];
    vi->size--;

    // If after removal the list becomes empty, delete it from hashmap
    if (vi->size == 0) {
        HASH_DEL(obj->map, vi);
        free(vi->indices);
        free(vi);
    }

    int lastIdx = obj->size - 1;
    int lastVal = obj->vals[lastIdx];

    if (idxToRemove != lastIdx) {
        // Move the last element into idxToRemove
        obj->vals[idxToRemove] = lastVal;

        // Update metadata for moved element
        ElemInfo *infoMoved = &obj->infos[lastIdx];
        int posInViLast = infoMoved->idxPos;

        ValueIndices *viLast = NULL;
        HASH_FIND_INT(obj->map, &lastVal, viLast);
        // Replace the old index with idxToRemove in its indices list
        viLast->indices[posInViLast] = idxToRemove;

        // Update infos at new position
        obj->infos[idxToRemove].val = lastVal;
        obj->infos[idxToRemove].idxPos = posInViLast;
    }

    // Reduce overall size
    obj->size--;
    return true;
}

/* Get a random element from the collection. */
int randomizedCollectionGetRandom(RandomizedCollection* obj) {
    int idx = rand() % obj->size;
    return obj->vals[idx];
}

/* Free all allocated memory. */
void randomizedCollectionFree(RandomizedCollection* obj) {
    // Free hashmap entries
    ValueIndices *vi, *tmp;
    HASH_ITER(hh, obj->map, vi, tmp) {
        HASH_DEL(obj->map, vi);
        free(vi->indices);
        free(vi);
    }
    // Free main arrays
    free(obj->vals);
    free(obj->infos);
    free(obj);
}
```

## Csharp

```csharp
public class RandomizedCollection
{
    private readonly List<int> _list;
    private readonly Dictionary<int, HashSet<int>> _dict;
    private readonly Random _rand;

    public RandomizedCollection()
    {
        _list = new List<int>();
        _dict = new Dictionary<int, HashSet<int>>();
        _rand = new Random();
    }

    public bool Insert(int val)
    {
        bool notContains = !_dict.ContainsKey(val);
        if (!_dict.TryGetValue(val, out var set))
        {
            set = new HashSet<int>();
            _dict[val] = set;
        }
        set.Add(_list.Count);
        _list.Add(val);
        return notContains;
    }

    public bool Remove(int val)
    {
        if (!_dict.ContainsKey(val) || _dict[val].Count == 0)
            return false;

        // Get an arbitrary index of the element to remove
        var idxSet = _dict[val];
        int removeIdx = -1;
        foreach (var i in idxSet)
        {
            removeIdx = i;
            break;
        }

        // Remove this index from the set
        idxSet.Remove(removeIdx);
        if (idxSet.Count == 0)
            _dict.Remove(val);

        int lastIndex = _list.Count - 1;
        int lastVal = _list[lastIndex];

        // Move the last element into the spot of the removed element if not the same spot
        if (removeIdx != lastIndex)
        {
            _list[removeIdx] = lastVal;

            var lastSet = _dict[lastVal];
            lastSet.Remove(lastIndex);
            lastSet.Add(removeIdx);
        }

        // Remove the last element from list
        _list.RemoveAt(lastIndex);

        return true;
    }

    public int GetRandom()
    {
        int idx = _rand.Next(_list.Count);
        return _list[idx];
    }
}
```

## Javascript

```javascript
var RandomizedCollection = function() {
    this.nums = [];
    this.idxMap = new Map(); // value -> Set of indices
};

RandomizedCollection.prototype.insert = function(val) {
    const idx = this.nums.length;
    this.nums.push(val);
    if (!this.idxMap.has(val)) {
        this.idxMap.set(val, new Set());
    }
    const set = this.idxMap.get(val);
    const alreadyExists = set.size > 0;
    set.add(idx);
    return !alreadyExists;
};

RandomizedCollection.prototype.remove = function(val) {
    if (!this.idxMap.has(val)) return false;
    const set = this.idxMap.get(val);
    if (set.size === 0) return false;

    // Get an arbitrary index of the element to remove
    const idxToRemove = set.values().next().value;
    set.delete(idxToRemove);

    const lastIdx = this.nums.length - 1;
    const lastVal = this.nums[lastIdx];

    if (idxToRemove !== lastIdx) {
        // Move the last element into the spot of the removed element
        this.nums[idxToRemove] = lastVal;

        // Update the index set for the moved value
        const lastSet = this.idxMap.get(lastVal);
        lastSet.delete(lastIdx);
        lastSet.add(idxToRemove);
    }

    this.nums.pop();

    if (set.size === 0) {
        this.idxMap.delete(val);
    }
    return true;
};

RandomizedCollection.prototype.getRandom = function() {
    const randIdx = Math.floor(Math.random() * this.nums.length);
    return this.nums[randIdx];
};
```

## Typescript

```typescript
class RandomizedCollection {
    private nums: number[];
    private idxMap: Map<number, Set<number>>;

    constructor() {
        this.nums = [];
        this.idxMap = new Map();
    }

    insert(val: number): boolean {
        const idx = this.nums.length;
        this.nums.push(val);
        let set = this.idxMap.get(val);
        const isNew = !set;
        if (!set) {
            set = new Set<number>();
            this.idxMap.set(val, set);
        }
        set.add(idx);
        return isNew;
    }

    remove(val: number): boolean {
        const set = this.idxMap.get(val);
        if (!set || set.size === 0) return false;

        // Get an arbitrary index of the value to remove
        const it = set.values();
        const idxToRemove = it.next().value;

        // Remove this index from the set
        set.delete(idxToRemove);

        const lastIdx = this.nums.length - 1;
        const lastVal = this.nums[lastIdx];

        if (idxToRemove !== lastIdx) {
            // Move the last element to the spot of the removed element
            this.nums[idxToRemove] = lastVal;

            // Update the index set for the moved value
            const lastSet = this.idxMap.get(lastVal)!;
            lastSet.delete(lastIdx);
            lastSet.add(idxToRemove);
        }

        // Remove the last element from the array
        this.nums.pop();

        if (set.size === 0) {
            this.idxMap.delete(val);
        }
        return true;
    }

    getRandom(): number {
        const randIdx = Math.floor(Math.random() * this.nums.length);
        return this.nums[randIdx];
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * var obj = new RandomizedCollection()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
```

## Php

```php
<?php
class RandomizedCollection {
    /**
     * @var array
     */
    private $list;
    /**
     * @var array map value => set of indices (as associative array)
     */
    private $indices;

    function __construct() {
        $this->list = [];
        $this->indices = [];
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        $isNew = !isset($this->indices[$val]) || empty($this->indices[$val]);
        $this->list[] = $val;
        $idx = count($this->list) - 1;
        if (!isset($this->indices[$val])) {
            $this->indices[$val] = [];
        }
        $this->indices[$val][$idx] = true;
        return $isNew;
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        if (!isset($this->indices[$val]) || empty($this->indices[$val])) {
            return false;
        }
        // get an arbitrary index of the value to remove
        foreach ($this->indices[$val] as $removeIdx => $_) {
            break;
        }

        $lastIdx = count($this->list) - 1;
        $lastVal = $this->list[$lastIdx];

        // Remove the index from val's set
        unset($this->indices[$val][$removeIdx]);

        if ($removeIdx != $lastIdx) {
            // Move last element to the place of removed element
            $this->list[$removeIdx] = $lastVal;

            // Update indices for lastVal
            unset($this->indices[$lastVal][$lastIdx]);
            $this->indices[$lastVal][$removeIdx] = true;
        }

        // Remove last element from list
        array_pop($this->list);

        if (empty($this->indices[$val])) {
            unset($this->indices[$val]);
        }

        return true;
    }

    /**
     * @return Integer
     */
    function getRandom() {
        $randIdx = array_rand($this->list);
        return $this->list[$randIdx];
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * $obj = new RandomizedCollection();
 * $ret_1 = $obj->insert($val);
 * $ret_2 = $obj->remove($val);
 * $ret_3 = $obj->getRandom();
 */
?>
```

## Swift

```swift
class RandomizedCollection {
    private var nums: [Int]
    private var idxMap: [Int: Set<Int>]

    init() {
        nums = []
        idxMap = [:]
    }

    func insert(_ val: Int) -> Bool {
        let isNew = idxMap[val] == nil
        nums.append(val)
        let index = nums.count - 1
        if var set = idxMap[val] {
            set.insert(index)
            idxMap[val] = set
        } else {
            idxMap[val] = Set([index])
        }
        return isNew
    }

    func remove(_ val: Int) -> Bool {
        guard let indices = idxMap[val], !indices.isEmpty else {
            return false
        }
        let idxToRemove = indices.first!
        var newSet = indices
        newSet.remove(idxToRemove)
        if newSet.isEmpty {
            idxMap.removeValue(forKey: val)
        } else {
            idxMap[val] = newSet
        }

        let lastIdx = nums.count - 1
        let lastVal = nums[lastIdx]

        if idxToRemove != lastIdx {
            nums[idxToRemove] = lastVal
            if var lastSet = idxMap[lastVal] {
                lastSet.remove(lastIdx)
                lastSet.insert(idxToRemove)
                idxMap[lastVal] = lastSet
            }
        }

        nums.removeLast()
        return true
    }

    func getRandom() -> Int {
        let randomIndex = Int.random(in: 0..<nums.count)
        return nums[randomIndex]
    }
}
```

## Kotlin

```kotlin
class RandomizedCollection() {
    private val nums = mutableListOf<Int>()
    private val idxMap = HashMap<Int, MutableSet<Int>>()
    private val rand = java.util.Random()

    fun insert(`val`: Int): Boolean {
        val isNew = !idxMap.containsKey(`val`)
        nums.add(`val`)
        val set = idxMap.getOrPut(`val`) { HashSet() }
        set.add(nums.size - 1)
        return isNew
    }

    fun remove(`val`: Int): Boolean {
        val set = idxMap[`val`] ?: return false
        // Get an arbitrary index of the value to remove
        val it = set.iterator()
        val removeIdx = it.next()
        it.remove() // remove this index from the set

        val lastIdx = nums.size - 1
        if (removeIdx != lastIdx) {
            val lastVal = nums[lastIdx]
            nums[removeIdx] = lastVal

            // Update the indices set for the last value
            val lastSet = idxMap[lastVal]!!
            lastSet.remove(lastIdx)
            lastSet.add(removeIdx)
        }
        nums.removeAt(lastIdx)

        if (set.isEmpty()) {
            idxMap.remove(`val`)
        }
        return true
    }

    fun getRandom(): Int {
        val randomIndex = rand.nextInt(nums.size)
        return nums[randomIndex]
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * var obj = RandomizedCollection()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
 */
```

## Dart

```dart
import 'dart:math';

class RandomizedCollection {
  final List<int> _vals = [];
  final Map<int, Set<int>> _idxMap = {};
  final Random _rand = Random();

  RandomizedCollection();

  bool insert(int val) {
    bool notExists = !(_idxMap.containsKey(val) && _idxMap[val]!.isNotEmpty);
    _vals.add(val);
    int idx = _vals.length - 1;
    _idxMap.putIfAbsent(val, () => <int>{});
    _idxMap[val]!.add(idx);
    return notExists;
  }

  bool remove(int val) {
    if (!_idxMap.containsKey(val) || _idxMap[val]!.isEmpty) {
      return false;
    }
    // Get an arbitrary index of the value to remove
    int removeIdx = _idxMap[val]!.first;
    _idxMap[val]!.remove(removeIdx);

    int lastIdx = _vals.length - 1;
    int lastVal = _vals[lastIdx];

    if (removeIdx != lastIdx) {
      // Move the last element to the place of the element to delete
      _vals[removeIdx] = lastVal;

      // Update the index set for the moved value
      _idxMap[lastVal]!.remove(lastIdx);
      _idxMap[lastVal]!.add(removeIdx);
    }

    _vals.removeLast();

    if (_idxMap[val]!.isEmpty) {
      _idxMap.remove(val);
    }
    return true;
  }

  int getRandom() {
    int randomIndex = _rand.nextInt(_vals.length);
    return _vals[randomIndex];
  }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = RandomizedCollection();
 * bool param1 = obj.insert(val);
 * bool param2 = obj.remove(val);
 * int param3 = obj.getRandom();
 */
```

## Golang

```go
import (
	"math/rand"
	"time"
)

type RandomizedCollection struct {
	nums []int
	idx  map[int]map[int]struct{}
}

func Constructor() RandomizedCollection {
	rand.Seed(time.Now().UnixNano())
	return RandomizedCollection{
		nums: []int{},
		idx:  make(map[int]map[int]struct{}),
	}
}

func (this *RandomizedCollection) Insert(val int) bool {
	this.nums = append(this.nums, val)
	pos := len(this.nums) - 1
	if _, ok := this.idx[val]; !ok {
		this.idx[val] = make(map[int]struct{})
	}
	set := this.idx[val]
	set[pos] = struct{}{}
	return len(set) == 1
}

func (this *RandomizedCollection) Remove(val int) bool {
	set, ok := this.idx[val]
	if !ok || len(set) == 0 {
		return false
	}
	var removeIdx int
	for i := range set {
		removeIdx = i
		break
	}
	lastIdx := len(this.nums) - 1
	lastVal := this.nums[lastIdx]

	// Move last element to the place of the element to delete
	this.nums[removeIdx] = lastVal

	// Update index map for the moved element
	lastSet := this.idx[lastVal]
	delete(lastSet, lastIdx)
	if removeIdx != lastIdx {
		lastSet[removeIdx] = struct{}{}
	}

	// Remove the index from the set of val
	delete(set, removeIdx)

	// Trim the slice
	this.nums = this.nums[:lastIdx]

	if len(set) == 0 {
		delete(this.idx, val)
	}
	return true
}

func (this *RandomizedCollection) GetRandom() int {
	return this.nums[rand.Intn(len(this.nums))]
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
```

## Ruby

```ruby
require 'set'

class RandomizedCollection
  def initialize()
    @list = []
    @idx_map = Hash.new { |h, k| h[k] = Set.new }
  end

  # :type val: Integer
  # :rtype: Boolean
  def insert(val)
    @list << val
    idx = @list.length - 1
    @idx_map[val] << idx
    @idx_map[val].size == 1
  end

  # :type val: Integer
  # :rtype: Boolean
  def remove(val)
    return false unless @idx_map.key?(val) && !@idx_map[val].empty?

    idx_to_remove = @idx_map[val].first
    @idx_map[val].delete(idx_to_remove)

    last_idx = @list.length - 1
    if idx_to_remove != last_idx
      last_val = @list[last_idx]
      @list[idx_to_remove] = last_val

      @idx_map[last_val].delete(last_idx)
      @idx_map[last_val] << idx_to_remove
    end

    @list.pop
    @idx_map.delete(val) if @idx_map[val].empty?
    true
  end

  # :rtype: Integer
  def get_random()
    @list[rand(@list.length)]
  end
end
```

## Scala

```scala
class RandomizedCollection() {
  private val nums = new scala.collection.mutable.ArrayBuffer[Int]()
  private val idxMap = new scala.collection.mutable.HashMap[Int, scala.collection.mutable.Set[Int]]()

  def insert(`val`: Int): Boolean = {
    val index = nums.length
    nums.append(`val`)
    val set = idxMap.getOrElseUpdate(`val`, scala.collection.mutable.Set[Int]())
    val existed = set.nonEmpty
    set.add(index)
    !existed
  }

  def remove(`val`: Int): Boolean = {
    idxMap.get(`val`) match {
      case None => false
      case Some(set) if set.isEmpty => false
      case Some(set) =>
        val removeIdx = set.head
        set.remove(removeIdx)

        val lastIdx = nums.length - 1
        val lastVal = nums(lastIdx)

        if (removeIdx != lastIdx) {
          nums(removeIdx) = lastVal
          val lastSet = idxMap(lastVal)
          lastSet.remove(lastIdx)
          lastSet.add(removeIdx)
        }

        nums.remove(lastIdx)

        if (set.isEmpty) {
          idxMap.remove(`val`)
        }
        true
    }
  }

  def getRandom(): Int = {
    val randIdx = scala.util.Random.nextInt(nums.length)
    nums(randIdx)
  }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * val obj = new RandomizedCollection()
 * val param_1 = obj.insert(`val`)
 * val param_2 = obj.remove(`val`)
 * val param_3 = obj.getRandom()
 */
```

## Rust

```rust
use std::collections::{HashMap, HashSet};
use rand::prelude::*;

struct RandomizedCollection {
    nums: Vec<i32>,
    idx_map: HashMap<i32, HashSet<usize>>,
}

impl RandomizedCollection {
    fn new() -> Self {
        RandomizedCollection { nums: Vec::new(), idx_map: HashMap::new() }
    }

    fn insert(&mut self, val: i32) -> bool {
        let contains = self.idx_map.get(&val).map_or(false, |s| !s.is_empty());
        self.nums.push(val);
        let idx = self.nums.len() - 1;
        self.idx_map.entry(val).or_insert_with(HashSet::new).insert(idx);
        !contains
    }

    fn remove(&mut self, val: i32) -> bool {
        // Find an index of the value to remove
        let remove_idx_opt = self.idx_map.get(&val).and_then(|s| s.iter().next().cloned());
        if remove_idx_opt.is_none() {
            return false;
        }
        let remove_idx = remove_idx_opt.unwrap();

        // Remove this index from the value's set
        let mut need_cleanup = false;
        if let Some(set) = self.idx_map.get_mut(&val) {
            set.remove(&remove_idx);
            if set.is_empty() {
                need_cleanup = true;
            }
        }
        if need_cleanup {
            self.idx_map.remove(&val);
        }

        let last_idx = self.nums.len() - 1;
        let last_val = self.nums[last_idx];

        if remove_idx != last_idx {
            // Move the last element to the place of the removed element
            self.nums[remove_idx] = last_val;

            // Update the index set for the moved value
            if let Some(set) = self.idx_map.get_mut(&last_val) {
                set.remove(&last_idx);
                set.insert(remove_idx);
            }
        }

        self.nums.pop();
        true
    }

    fn get_random(&self) -> i32 {
        let mut rng = thread_rng();
        let idx = rng.gen_range(0..self.nums.len());
        self.nums[idx]
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * let obj = RandomizedCollection::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
```

## Racket

```racket
(require racket/list)

(define randomized-collection%
  (class object%
    (super-new)
    
    ; internal storage
    (define arr (make-vector 4))
    (define sz 0)
    (define idxMap (make-hash)) ; val -> mutable hash of indices
    
    ;; ensure capacity for insertion
    (define (ensure-capacity)
      (when (>= sz (vector-length arr))
        (let* ((new-cap (* 2 (max 1 (vector-length arr))))
               (new-arr (make-vector new-cap)))
          (for ([i (in-range sz)])
            (vector-set! new-arr i (vector-ref arr i)))
          (set! arr new-arr))))
    
    ; insert : exact-integer? -> boolean?
    (define/public (insert val)
      (ensure-capacity)
      (let* ((inner (hash-ref idxMap val
                              (lambda ()
                                (let ((h (make-hash)))
                                  (hash-set! idxMap val h)
                                  h))))
             (was-empty (hash-empty? inner))
             (i sz))
        (vector-set! arr i val)
        (set! sz (+ sz 1))
        (hash-set! inner i #t)
        was-empty))
    
    ; remove : exact-integer? -> boolean?
    (define/public (remove val)
      (let ((inner (hash-ref idxMap val #f)))
        (if (or (not inner) (hash-empty? inner))
            #false
            (begin
              (define rem-idx (car (hash-keys inner))) ; any index of val
              (define last-idx (- sz 1))
              (define last-val (vector-ref arr last-idx))
              
              ;; move last element into the spot to delete
              (vector-set! arr rem-idx last-val)
              
              ;; update mapping for the moved element
              (let ((inner-last (hash-ref idxMap last-val)))
                (hash-remove! inner-last last-idx)
                (hash-set! inner-last rem-idx #t))
              
              ;; remove the index of val from its set
              (hash-remove! inner rem-idx)
              
              (set! sz (- sz 1))
              
              ;; clean up if no more occurrences
              (when (hash-empty? inner)
                (hash-remove! idxMap val))
              
              #true))))
    
    ; get-random : -> exact-integer?
    (define/public (get-random)
      (let ((i (random sz)))
        (vector-ref arr i)))))
```

## Erlang

```erlang
-module(solution).
-export([randomized_collection_init_/0,
         randomized_collection_insert/1,
         randomized_collection_remove/1,
         randomized_collection_get_random/0]).

randomized_collection_init_() ->
    put(state, #{idx_to_val => #{}, val_to_indices => #{}, size => 0}).

randomized_collection_insert(Val) when is_integer(Val) ->
    State = get(state),
    Size = maps:get(size, State),
    IdxMap = maps:get(idx_to_val, State),
    ValIdxMap = maps:get(val_to_indices, State),

    NewIdx = Size,
    NewIdxMap = maps:put(NewIdx, Val, IdxMap),

    PrevList = maps:get(Val, ValIdxMap, []),
    NewList = [NewIdx | PrevList],
    NewValIdxMap = maps:put(Val, NewList, ValIdxMap),

    NewState = State#{idx_to_val => NewIdxMap,
                      val_to_indices => NewValIdxMap,
                      size => Size + 1},
    put(state, NewState),
    (PrevList == []).

randomized_collection_remove(Val) when is_integer(Val) ->
    State = get(state),
    ValIdxMap0 = maps:get(val_to_indices, State, #{}),

    case maps:find(Val, ValIdxMap0) of
        error -> false;
        {ok, List} when List == [] -> false;
        {ok, [IdxToRemove | RestIndices]} ->
            Size = maps:get(size, State),
            LastIdx = Size - 1,
            IdxMap0 = maps:get(idx_to_val, State),

            {NewIdxMap, ValIdxMap1} =
                if IdxToRemove == LastIdx ->
                        {maps:remove(LastIdx, IdxMap0), ValIdxMap0}
                   true ->
                        LastVal = maps:get(LastIdx, IdxMap0),
                        TempIdxMap = maps:put(IdxToRemove, LastVal, IdxMap0),
                        NewIdxMapTmp = maps:remove(LastIdx, TempIdxMap),

                        LastValList = maps:get(LastVal, ValIdxMap0),
                        UpdatedLastValList = replace_index(LastValList, LastIdx, IdxToRemove),
                        ValIdxMapTmp = maps:put(LastVal, UpdatedLastValList, ValIdxMap0),

                        {NewIdxMapTmp, ValIdxMapTmp}
                end,

            NewValIdxMap =
                case RestIndices of
                    [] -> maps:remove(Val, ValIdxMap1);
                    _  -> maps:put(Val, RestIndices, ValIdxMap1)
                end,

            NewState = State#{idx_to_val => NewIdxMap,
                              val_to_indices => NewValIdxMap,
                              size => Size - 1},
            put(state, NewState),
            true
    end.

randomized_collection_get_random() ->
    State = get(state),
    Size = maps:get(size, State),
    RandIdx = rand:uniform(Size) - 1,
    IdxMap = maps:get(idx_to_val, State),
    maps:get(RandIdx, IdxMap).

replace_index([H|T], Old, New) when H == Old ->
    [New | T];
replace_index([H|T], Old, New) ->
    [H | replace_index(T, Old, New)];
replace_index([], _Old, _New) -> [].
```

## Elixir

```elixir
defmodule RandomizedCollection do
  @spec init_() :: :ok
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} =
      Agent.start_link(
        fn ->
          %{idx_to_val: %{}, val_to_idxs: %{}, size: 0}
        end,
        name: __MODULE__
      )

    :ok
  end

  @spec insert(val :: integer) :: boolean
  def insert(val) do
    Agent.get_and_update(__MODULE__, fn state ->
      idx = state.size

      idx_to_val =
        Map.put(state.idx_to_val, idx, val)

      val_set =
        Map.get(state.val_to_idxs, val, MapSet.new())
        |> MapSet.put(idx)

      val_to_idxs =
        Map.put(state.val_to_idxs, val, val_set)

      new_state = %{state | idx_to_val: idx_to_val, val_to_idxs: val_to_idxs, size: idx + 1}
      {MapSet.size(val_set) == 1, new_state}
    end)
  end

  @spec remove(val :: integer) :: boolean
  def remove(val) do
    Agent.get_and_update(__MODULE__, fn state ->
      case Map.get(state.val_to_idxs, val) do
        nil -> {false, state}
        idx_set when MapSet.size(idx_set) == 0 -> {false, state}
        _ ->
          [remove_idx | _] = MapSet.to_list(idx_set)
          last_idx = state.size - 1
          last_val = Map.get(state.idx_to_val, last_idx)

          idx_to_val = state.idx_to_val
          val_to_idxs = state.val_to_idxs

          {idx_to_val, val_to_idxs} =
            if remove_idx != last_idx do
              # move last_val to the position of remove_idx
              idx_to_val1 = Map.put(idx_to_val, remove_idx, last_val)

              # update indices set for last_val
              last_set = Map.get(val_to_idxs, last_val)
              last_set =
                last_set
                |> MapSet.delete(last_idx)
                |> MapSet.put(remove_idx)

              val_to_idxs1 = Map.put(val_to_idxs, last_val, last_set)
              {idx_to_val1, val_to_idxs1}
            else
              {idx_to_val, val_to_idxs}
            end

          # remove the now-last element
          idx_to_val = Map.delete(idx_to_val, last_idx)

          # update set for removed value
          val_set =
            Map.get(val_to_idxs, val)
            |> MapSet.delete(remove_idx)

          val_to_idxs =
            if MapSet.size(val_set) == 0 do
              Map.delete(val_to_idxs, val)
            else
              Map.put(val_to_idxs, val, val_set)
            end

          new_state = %{state | idx_to_val: idx_to_val, val_to_idxs: val_to_idxs, size: state.size - 1}
          {true, new_state}
      end
    end)
  end

  @spec get_random() :: integer
  def get_random() do
    Agent.get(__MODULE__, fn state ->
      idx = :rand.uniform(state.size) - 1
      Map.fetch!(state.idx_to_val, idx)
    end)
  end
end
```
