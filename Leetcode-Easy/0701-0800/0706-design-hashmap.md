# 0706. Design HashMap

## Cpp

```cpp
class MyHashMap {
    static const int SIZE = 1000001;
    std::vector<int> table;
public:
    MyHashMap() : table(SIZE, -1) {}
    
    void put(int key, int value) {
        table[key] = value;
    }
    
    int get(int key) {
        return table[key];
    }
    
    void remove(int key) {
        table[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
```

## Java

```java
class MyHashMap {
    private static final int SIZE = 1000001;
    private final int[] values;
    private final boolean[] occupied;

    public MyHashMap() {
        values = new int[SIZE];
        occupied = new boolean[SIZE];
    }

    public void put(int key, int value) {
        values[key] = value;
        occupied[key] = true;
    }

    public int get(int key) {
        return occupied[key] ? values[key] : -1;
    }

    public void remove(int key) {
        occupied[key] = false;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

## Python

```python
class MyHashMap(object):
    def __init__(self):
        self.size = 1000001
        self.table = [None] * self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.table[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.table[key]
        return -1 if val is None else val

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.table[key] = None
```

## Python3

```python
class MyHashMap:
    def __init__(self):
        self._size = 1009  # a prime number for better distribution
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key: int) -> int:
        return key % self._size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *vals;
    char *used;
} MyHashMap;

#define HASH_SIZE 1000001

MyHashMap* myHashMapCreate() {
    MyHashMap* obj = (MyHashMap*)malloc(sizeof(MyHashMap));
    if (!obj) return NULL;
    obj->vals = (int*)malloc(HASH_SIZE * sizeof(int));
    obj->used = (char*)malloc(HASH_SIZE * sizeof(char));
    if (!obj->vals || !obj->used) {
        free(obj->vals);
        free(obj->used);
        free(obj);
        return NULL;
    }
    memset(obj->used, 0, HASH_SIZE * sizeof(char));
    return obj;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    if (!obj || key < 0 || key >= HASH_SIZE) return;
    obj->vals[key] = value;
    obj->used[key] = 1;
}

int myHashMapGet(MyHashMap* obj, int key) {
    if (!obj || key < 0 || key >= HASH_SIZE) return -1;
    return obj->used[key] ? obj->vals[key] : -1;
}

void myHashMapRemove(MyHashMap* obj, int key) {
    if (!obj || key < 0 || key >= HASH_SIZE) return;
    obj->used[key] = 0;
}

void myHashMapFree(MyHashMap* obj) {
    if (!obj) return;
    free(obj->vals);
    free(obj->used);
    free(obj);
}
```

## Csharp

```csharp
public class MyHashMap
{
    private const int BucketSize = 1009; // a prime number for better distribution
    private readonly System.Collections.Generic.List<System.Collections.Generic.KeyValuePair<int, int>>[] _buckets;

    public MyHashMap()
    {
        _buckets = new System.Collections.Generic.List<System.Collections.Generic.KeyValuePair<int, int>>[BucketSize];
        for (int i = 0; i < BucketSize; i++)
            _buckets[i] = new System.Collections.Generic.List<System.Collections.Generic.KeyValuePair<int, int>>();
    }

    private int GetIndex(int key)
    {
        return key % BucketSize;
    }

    public void Put(int key, int value)
    {
        var bucket = _buckets[GetIndex(key)];
        for (int i = 0; i < bucket.Count; i++)
        {
            if (bucket[i].Key == key)
            {
                bucket[i] = new System.Collections.Generic.KeyValuePair<int, int>(key, value);
                return;
            }
        }
        bucket.Add(new System.Collections.Generic.KeyValuePair<int, int>(key, value));
    }

    public int Get(int key)
    {
        var bucket = _buckets[GetIndex(key)];
        foreach (var kv in bucket)
        {
            if (kv.Key == key)
                return kv.Value;
        }
        return -1;
    }

    public void Remove(int key)
    {
        var bucket = _buckets[GetIndex(key)];
        for (int i = 0; i < bucket.Count; i++)
        {
            if (bucket[i].Key == key)
            {
                bucket.RemoveAt(i);
                return;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.Put(key,value);
 * int param_2 = obj.Get(key);
 * obj.Remove(key);
 */
```

## Javascript

```javascript
var MyHashMap = function() {
    this.map = new Array(1000001).fill(-1);
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    this.map[key] = value;
};

/** 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    return this.map[key];
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    this.map[key] = -1;
};
```

## Typescript

```typescript
class MyHashMap {
    private readonly size = 1000;
    private buckets: Array<Array<[number, number]>>;

    constructor() {
        this.buckets = new Array(this.size);
        for (let i = 0; i < this.size; i++) {
            this.buckets[i] = [];
        }
    }

    private hash(key: number): number {
        return key % this.size;
    }

    put(key: number, value: number): void {
        const idx = this.hash(key);
        const bucket = this.buckets[idx];
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                bucket[i][1] = value;
                return;
            }
        }
        bucket.push([key, value]);
    }

    get(key: number): number {
        const idx = this.hash(key);
        const bucket = this.buckets[idx];
        for (const [k, v] of bucket) {
            if (k === key) {
                return v;
            }
        }
        return -1;
    }

    remove(key: number): void {
        const idx = this.hash(key);
        const bucket = this.buckets[idx];
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                bucket.splice(i, 1);
                break;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
```

## Php

```php
class MyHashMap {
    private $size = 1000;
    private $buckets;

    function __construct() {
        $this->buckets = array_fill(0, $this->size, []);
    }

    /**
     * @param Integer $key
     * @param Integer $value
     * @return NULL
     */
    function put($key, $value) {
        $idx = $key % $this->size;
        foreach ($this->buckets[$idx] as &$pair) {
            if ($pair[0] === $key) {
                $pair[1] = $value;
                return;
            }
        }
        $this->buckets[$idx][] = [$key, $value];
    }

    /**
     * @param Integer $key
     * @return Integer
     */
    function get($key) {
        $idx = $key % $this->size;
        foreach ($this->buckets[$idx] as $pair) {
            if ($pair[0] === $key) {
                return $pair[1];
            }
        }
        return -1;
    }

    /**
     * @param Integer $key
     * @return NULL
     */
    function remove($key) {
        $idx = $key % $this->size;
        $bucket =& $this->buckets[$idx];
        $len = count($bucket);
        for ($i = 0; $i < $len; $i++) {
            if ($bucket[$i][0] === $key) {
                array_splice($bucket, $i, 1);
                break;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * $obj = new MyHashMap();
 * $obj->put($key, $value);
 * $ret_2 = $obj->get($key);
 * $obj->remove($key);
 */
```

## Swift

```swift
class MyHashMap {
    private var values: [Int]
    private var exists: [Bool]

    init() {
        let size = 1_000_001
        values = Array(repeating: -1, count: size)
        exists = Array(repeating: false, count: size)
    }
    
    func put(_ key: Int, _ value: Int) {
        values[key] = value
        exists[key] = true
    }
    
    func get(_ key: Int) -> Int {
        return exists[key] ? values[key] : -1
    }
    
    func remove(_ key: Int) {
        exists[key] = false
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap()
 * obj.put(key, value)
 * let ret_2: Int = obj.get(key)
 * obj.remove(key)
 */
```

## Kotlin

```kotlin
class MyHashMap() {

    private val data = IntArray(1_000_001) { -1 }

    fun put(key: Int, value: Int) {
        data[key] = value
    }

    fun get(key: Int): Int {
        return data[key]
    }

    fun remove(key: Int) {
        data[key] = -1
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
```

## Dart

```dart
class MyHashMap {
  static const int _bucketSize = 1009; // a prime number for hashing
  final List<List<_Entry>> _buckets;

  MyHashMap() : _buckets = List.generate(_bucketSize, (_) => []);

  void put(int key, int value) {
    int idx = key % _bucketSize;
    var bucket = _buckets[idx];
    for (var entry in bucket) {
      if (entry.key == key) {
        entry.value = value;
        return;
      }
    }
    bucket.add(_Entry(key, value));
  }

  int get(int key) {
    int idx = key % _bucketSize;
    var bucket = _buckets[idx];
    for (var entry in bucket) {
      if (entry.key == key) {
        return entry.value;
      }
    }
    return -1;
  }

  void remove(int key) {
    int idx = key % _bucketSize;
    var bucket = _buckets[idx];
    for (int i = 0; i < bucket.length; i++) {
      if (bucket[i].key == key) {
        bucket.removeAt(i);
        return;
      }
    }
  }
}

class _Entry {
  int key;
  int value;
  _Entry(this.key, this.value);
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = MyHashMap();
 * obj.put(key,value);
 * int param2 = obj.get(key);
 * obj.remove(key);
 */
```

## Golang

```go
type MyHashMap struct {
	data []int
}

func Constructor() MyHashMap {
	const size = 1000001
	d := make([]int, size)
	for i := range d {
		d[i] = -1
	}
	return MyHashMap{data: d}
}

func (this *MyHashMap) Put(key int, value int) {
	this.data[key] = value
}

func (this *MyHashMap) Get(key int) int {
	return this.data[key]
}

func (this *MyHashMap) Remove(key int) {
	this.data[key] = -1
}
```

## Ruby

```ruby
class MyHashMap
  def initialize()
    @store = Array.new(1_000_001, -1)
  end

=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
  def put(key, value)
    @store[key] = value
  end

=begin
    :type key: Integer
    :rtype: Integer
=end
  def get(key)
    @store[key]
  end

=begin
    :type key: Integer
    :rtype: Void
=end
  def remove(key)
    @store[key] = -1
  end
end
```

## Scala

```scala
class MyHashMap() {

  private val size = 1000001
  private val map = Array.fill(size)(-1)

  def put(key: Int, value: Int): Unit = {
    map(key) = value
  }

  def get(key: Int): Int = {
    map(key)
  }

  def remove(key: Int): Unit = {
    map(key) = -1
  }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * val obj = new MyHashMap()
 * obj.put(key,value)
 * val param_2 = obj.get(key)
 * obj.remove(key)
 */
```

## Rust

```rust
struct MyHashMap {
    data: Vec<i32>,
}

impl MyHashMap {
    fn new() -> Self {
        // Use -1 to denote empty slot since values are non‑negative.
        MyHashMap { data: vec![-1; 1_000_001] }
    }

    fn put(&mut self, key: i32, value: i32) {
        let idx = key as usize;
        self.data[idx] = value;
    }

    fn get(&self, key: i32) -> i32 {
        let idx = key as usize;
        self.data[idx]
    }

    fn remove(&mut self, key: i32) {
        let idx = key as usize;
        self.data[idx] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let mut obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */
```

## Racket

```racket
(define my-hash-map%
  (class object%
    (super-new)
    
    (init-field) ; no external init fields
    
    (field [store (make-vector 1000001 -1)])
    
    ;; put : exact-integer? exact-integer? -> void?
    (define/public (put key value)
      (vector-set! store key value))
    
    ;; get : exact-integer? -> exact-integer?
    (define/public (get key)
      (vector-ref store key))
    
    ;; remove : exact-integer? -> void?
    (define/public (remove key)
      (vector-set! store key -1))))
```

## Erlang

```erlang
-module(my_hash_map).
-export([my_hash_map_init_/0,
         my_hash_map_put/2,
         my_hash_map_get/1,
         my_hash_map_remove/1]).

-spec my_hash_map_init_() -> any().
my_hash_map_init_() ->
    case erlang:get(hashmap_table) of
        undefined -> ok;
        Tid when is_reference(Tid) -> ets:delete(Tid)
    end,
    Tid = ets:new(hashmap_table, [set, private]),
    erlang:put(hashmap_table, Tid),
    ok.

-spec my_hash_map_put(Key :: integer(), Value :: integer()) -> any().
my_hash_map_put(Key, Value) ->
    case erlang:get(hashmap_table) of
        undefined -> ok;
        Tid when is_reference(Tid) -> ets:insert(Tid, {Key, Value})
    end,
    ok.

-spec my_hash_map_get(Key :: integer()) -> integer().
my_hash_map_get(Key) ->
    case erlang:get(hashmap_table) of
        undefined -> -1;
        Tid when is_reference(Tid) ->
            case ets:lookup(Tid, Key) of
                [{_, V}] -> V;
                [] -> -1
            end
    end.

-spec my_hash_map_remove(Key :: integer()) -> any().
my_hash_map_remove(Key) ->
    case erlang:get(hashmap_table) of
        undefined -> ok;
        Tid when is_reference(Tid) -> ets:delete(Tid, Key)
    end,
    ok.
```

## Elixir

```elixir
defmodule MyHashMap do
  @spec init_() :: any
  def init_() do
    Process.put(:my_hashmap, %{})
  end

  @spec put(key :: integer, value :: integer) :: any
  def put(key, value) do
    map = Process.get(:my_hashmap, %{})
    Process.put(:my_hashmap, Map.put(map, key, value))
  end

  @spec get(key :: integer) :: integer
  def get(key) do
    map = Process.get(:my_hashmap, %{})
    case Map.fetch(map, key) do
      {:ok, v} -> v
      :error -> -1
    end
  end

  @spec remove(key :: integer) :: any
  def remove(key) do
    map = Process.get(:my_hashmap, %{})
    Process.put(:my_hashmap, Map.delete(map, key))
  end
end
```
