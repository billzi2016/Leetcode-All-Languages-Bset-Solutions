# 0705. Design HashSet

## Cpp

```cpp
class MyHashSet {
public:
    /** Initialize your data structure here. */
    MyHashSet() : present(1000001, false) {}
    
    void add(int key) {
        present[key] = true;
    }
    
    void remove(int key) {
        present[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return present[key];
    }
private:
    std::vector<bool> present;
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
```

## Java

```java
class MyHashSet {
    private static final int MAX_KEY = 1000000;
    private final boolean[] bucket;

    public MyHashSet() {
        bucket = new boolean[MAX_KEY + 1];
    }

    public void add(int key) {
        bucket[key] = true;
    }

    public void remove(int key) {
        bucket[key] = false;
    }

    public boolean contains(int key) {
        return bucket[key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
```

## Python

```python
class MyHashSet(object):
    def __init__(self):
        self._data = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self._data[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self._data[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self._data[key]
```

## Python3

```python
class MyHashSet:
    def __init__(self):
        self.size = 10 ** 6 + 1
        self.bucket = [False] * self.size

    def add(self, key: int) -> None:
        self.bucket[key] = True

    def remove(self, key: int) -> None:
        self.bucket[key] = False

    def contains(self, key: int) -> bool:
        return self.bucket[key]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    bool *table;
} MyHashSet;

MyHashSet* myHashSetCreate() {
    MyHashSet *obj = (MyHashSet *)malloc(sizeof(MyHashSet));
    if (!obj) return NULL;
    obj->table = (bool *)calloc(1000001, sizeof(bool)); // keys 0..10^6
    return obj;
}

void myHashSetAdd(MyHashSet* obj, int key) {
    if (obj && key >= 0 && key <= 1000000)
        obj->table[key] = true;
}

void myHashSetRemove(MyHashSet* obj, int key) {
    if (obj && key >= 0 && key <= 1000000)
        obj->table[key] = false;
}

bool myHashSetContains(MyHashSet* obj, int key) {
    if (obj && key >= 0 && key <= 1000000)
        return obj->table[key];
    return false;
}

void myHashSetFree(MyHashSet* obj) {
    if (!obj) return;
    free(obj->table);
    free(obj);
}
```

## Csharp

```csharp
public class MyHashSet
{
    private const int MaxKey = 1000000;
    private readonly bool[] _present;

    public MyHashSet()
    {
        _present = new bool[MaxKey + 1];
    }

    public void Add(int key)
    {
        _present[key] = true;
    }

    public void Remove(int key)
    {
        _present[key] = false;
    }

    public bool Contains(int key)
    {
        return _present[key];
    }
}
```

## Javascript

```javascript
var MyHashSet = function() {
    this.arr = new Uint8Array(1000001);
};

MyHashSet.prototype.add = function(key) {
    this.arr[key] = 1;
};

MyHashSet.prototype.remove = function(key) {
    this.arr[key] = 0;
};

MyHashSet.prototype.contains = function(key) {
    return this.arr[key] === 1;
};
```

## Typescript

```typescript
class MyHashSet {
    private bucket: Uint8Array;

    constructor() {
        this.bucket = new Uint8Array(1000001);
    }

    add(key: number): void {
        this.bucket[key] = 1;
    }

    remove(key: number): void {
        this.bucket[key] = 0;
    }

    contains(key: number): boolean {
        return this.bucket[key] === 1;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```

## Php

```php
class MyHashSet {
    /**
     * @var array
     */
    private $bucket;

    /**
     */
    function __construct() {
        // keys are in the range [0, 10^6]
        $this->bucket = array_fill(0, 1000001, false);
    }

    /**
     * @param Integer $key
     * @return NULL
     */
    function add($key) {
        $this->bucket[$key] = true;
    }

    /**
     * @param Integer $key
     * @return NULL
     */
    function remove($key) {
        $this->bucket[$key] = false;
    }

    /**
     * @param Integer $key
     * @return Boolean
     */
    function contains($key) {
        return $this->bucket[$key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * $obj = new MyHashSet();
 * $obj->add($key);
 * $obj->remove($key);
 * $ret_3 = $obj->contains($key);
 */
```

## Swift

```swift
class MyHashSet {
    private var storage: [Bool]

    init() {
        storage = Array(repeating: false, count: 1_000_001)
    }

    func add(_ key: Int) {
        if key >= 0 && key < storage.count {
            storage[key] = true
        }
    }

    func remove(_ key: Int) {
        if key >= 0 && key < storage.count {
            storage[key] = false
        }
    }

    func contains(_ key: Int) -> Bool {
        if key >= 0 && key < storage.count {
            return storage[key]
        }
        return false
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * let ret_3: Bool = obj.contains(key)
 */
```

## Kotlin

```kotlin
class MyHashSet() {
    private val present = BooleanArray(1_000_001)

    fun add(key: Int) {
        present[key] = true
    }

    fun remove(key: Int) {
        present[key] = false
    }

    fun contains(key: Int): Boolean {
        return present[key]
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
```

## Dart

```dart
class MyHashSet {
  final List<bool> _present;

  MyHashSet() : _present = List.filled(1000001, false);

  void add(int key) {
    _present[key] = true;
  }

  void remove(int key) {
    _present[key] = false;
  }

  bool contains(int key) {
    return _present[key];
  }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * bool param3 = obj.contains(key);
 */
```

## Golang

```go
type MyHashSet struct {
	data []bool
}

func Constructor() MyHashSet {
	return MyHashSet{data: make([]bool, 1000001)}
}

func (this *MyHashSet) Add(key int) {
	this.data[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.data[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	return this.data[key]
}
```

## Ruby

```ruby
class MyHashSet
    def initialize()
        @store = Array.new(1_000_001, false)
    end

    # :type key: Integer
    # :rtype: Void
    def add(key)
        @store[key] = true
    end

    # :type key: Integer
    # :rtype: Void
    def remove(key)
        @store[key] = false
    end

    # :type key: Integer
    # :rtype: Boolean
    def contains(key)
        @store[key]
    end
end
```

## Scala

```scala
class MyHashSet() {
  private val size = 1000001
  private val bucket = new Array[Boolean](size)

  def add(key: Int): Unit = {
    bucket(key) = true
  }

  def remove(key: Int): Unit = {
    bucket(key) = false
  }

  def contains(key: Int): Boolean = {
    bucket(key)
  }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * val obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * val param_3 = obj.contains(key)
 */
```

## Rust

```rust
struct MyHashSet {
    buckets: Vec<bool>,
}

impl MyHashSet {
    fn new() -> Self {
        MyHashSet {
            buckets: vec![false; 1_000_001],
        }
    }

    fn add(&mut self, key: i32) {
        let idx = key as usize;
        self.buckets[idx] = true;
    }

    fn remove(&mut self, key: i32) {
        let idx = key as usize;
        self.buckets[idx] = false;
    }

    fn contains(&self, key: i32) -> bool {
        let idx = key as usize;
        self.buckets[idx]
    }
}
```

## Racket

```racket
(define my-hash-set%
  (class object%
    (super-new)
    (define buckets (make-vector 1000001 #f))
    (define/public (add key)
      (vector-set! buckets key #t))
    (define/public (remove key)
      (vector-set! buckets key #f))
    (define/public (contains key)
      (vector-ref buckets key))))
```

## Erlang

```erlang
-module(my_hash_set).
-export([my_hash_set_init_/0,
         my_hash_set_add/1,
         my_hash_set_remove/1,
         my_hash_set_contains/1]).

-define(TABLE, hashset).

-spec my_hash_set_init_() -> any().
my_hash_set_init_() ->
    case ets:info(?TABLE) of
        undefined -> ets:new(?TABLE, [named_table, set, public]);
        _ -> ok
    end,
    ok.

-spec my_hash_set_add(Key :: integer()) -> any().
my_hash_set_add(Key) when is_integer(Key) ->
    ets:insert(?TABLE, {Key, true}),
    ok.

-spec my_hash_set_remove(Key :: integer()) -> any().
my_hash_set_remove(Key) when is_integer(Key) ->
    ets:delete(?TABLE, Key),
    ok.

-spec my_hash_set_contains(Key :: integer()) -> boolean().
my_hash_set_contains(Key) when is_integer(Key) ->
    case ets:lookup(?TABLE, Key) of
        [] -> false;
        [_] -> true
    end.
```

## Elixir

```elixir
defmodule MyHashSet do
  @table :my_hash_set

  @spec init_() :: any
  def init_() do
    case :ets.whereis(@table) do
      :undefined -> :ok
      _pid -> :ets.delete(@table)
    end

    :ets.new(@table, [:set, :public, :named_table])
    nil
  end

  @spec add(key :: integer) :: any
  def add(key) do
    :ets.insert(@table, {key, true})
    nil
  end

  @spec remove(key :: integer) :: any
  def remove(key) do
    :ets.delete(@table, key)
    nil
  end

  @spec contains(key :: integer) :: boolean
  def contains(key) do
    case :ets.lookup(@table, key) do
      [{^key, true}] -> true
      _ -> false
    end
  end
end
```
