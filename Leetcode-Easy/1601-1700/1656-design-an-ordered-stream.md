# 1656. Design an Ordered Stream

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class OrderedStream {
public:
    OrderedStream(int n) : ptr(1), stream(n + 1, "") {}
    
    vector<string> insert(int idKey, string value) {
        stream[idKey] = move(value);
        vector<string> res;
        while (ptr < (int)stream.size() && !stream[ptr].empty()) {
            res.push_back(stream[ptr]);
            ++ptr;
        }
        return res;
    }

private:
    int ptr;
    vector<string> stream;
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */
```

## Java

```java
class OrderedStream {
    private final String[] stream;
    private int ptr;

    public OrderedStream(int n) {
        stream = new String[n + 1]; // 1-indexed
        ptr = 1;
    }

    public java.util.List<String> insert(int idKey, String value) {
        stream[idKey] = value;
        java.util.List<String> result = new java.util.ArrayList<>();
        while (ptr < stream.length && stream[ptr] != null) {
            result.add(stream[ptr]);
            ptr++;
        }
        return result;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */
```

## Python

```python
class OrderedStream(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.stream = [None] * (n + 1)  # 1-indexed
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey] = value
        res = []
        while self.ptr <= self.n and self.stream[self.ptr] is not None:
            res.append(self.stream[self.ptr])
            self.ptr += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```

## Python3

```python
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [""] * (n + 1)  # 1-indexed
        self.ptr = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []
        while self.ptr <= self.n and self.stream[self.ptr]:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **arr;   // 1-indexed array of stored strings
    int n;        // total size
    int ptr;      // next id to output
} OrderedStream;

OrderedStream* orderedStreamCreate(int n) {
    OrderedStream *obj = (OrderedStream*)malloc(sizeof(OrderedStream));
    obj->n = n;
    obj->ptr = 1;
    obj->arr = (char**)calloc(n + 1, sizeof(char*)); // index 0 unused
    return obj;
}

static char* my_strdup(const char *s) {
    size_t len = strlen(s);
    char *p = (char*)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

char** orderedStreamInsert(OrderedStream* obj, int idKey, char* value, int* retSize) {
    // store the value
    if (obj->arr[idKey] == NULL) {
        obj->arr[idKey] = my_strdup(value);
    }

    // collect consecutive values starting from ptr
    char **res = (char**)malloc(sizeof(char*) * obj->n); // maximum possible size
    int cnt = 0;
    while (obj->ptr <= obj->n && obj->arr[obj->ptr]) {
        res[cnt++] = obj->arr[obj->ptr];
        obj->ptr++;
    }
    *retSize = cnt;
    return res;
}

void orderedStreamFree(OrderedStream* obj) {
    if (!obj) return;
    for (int i = 1; i <= obj->n; ++i) {
        free(obj->arr[i]);
    }
    free(obj->arr);
    free(obj);
}

/**
 * Your OrderedStream struct will be instantiated and called as such:
 * OrderedStream* obj = orderedStreamCreate(n);
 * char** param_1 = orderedStreamInsert(obj, idKey, value, retSize);
 *
 * orderedStreamFree(obj);
 */
```

## Csharp

```csharp
public class OrderedStream
{
    private readonly string[] _stream;
    private int _ptr;

    public OrderedStream(int n)
    {
        _stream = new string[n + 1]; // 1-indexed
        _ptr = 1;
    }

    public IList<string> Insert(int idKey, string value)
    {
        _stream[idKey] = value;
        var result = new List<string>();

        while (_ptr < _stream.Length && _stream[_ptr] != null)
        {
            result.Add(_stream[_ptr]);
            _ptr++;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.n = n;
    this.stream = new Array(n + 1); // 1-indexed
    this.ptr = 1; // next id to output
};

/** 
 * @param {number} idKey 
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(idKey, value) {
    this.stream[idKey] = value;
    const result = [];
    while (this.ptr <= this.n && this.stream[this.ptr] !== undefined) {
        result.push(this.stream[this.ptr]);
        this.ptr++;
    }
    return result;
};
```

## Typescript

```typescript
class OrderedStream {
    private stream: (string | undefined)[];
    private ptr: number;
    private size: number;

    constructor(n: number) {
        this.stream = new Array(n + 1);
        this.ptr = 1;
        this.size = n;
    }

    insert(idKey: number, value: string): string[] {
        this.stream[idKey] = value;
        const result: string[] = [];
        while (this.ptr <= this.size && this.stream[this.ptr] !== undefined) {
            result.push(this.stream[this.ptr]!);
            this.ptr++;
        }
        return result;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
```

## Php

```php
<?php
class OrderedStream {
    private $stream;
    private $ptr;
    private $n;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->n = $n;
        $this->stream = array_fill(0, $n + 1, null);
        $this->ptr = 1;
    }

    /**
     * @param Integer $idKey
     * @param String $value
     * @return String[]
     */
    function insert($idKey, $value) {
        $this->stream[$idKey] = $value;
        $result = [];
        while ($this->ptr <= $this->n && $this->stream[$this->ptr] !== null) {
            $result[] = $this->stream[$this->ptr];
            $this->ptr++;
        }
        return $result;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * $obj = new OrderedStream($n);
 * $ret_1 = $obj->insert($idKey, $value);
 */
?>
```

## Swift

```swift
class OrderedStream {
    private var stream: [String?]
    private var ptr: Int

    init(_ n: Int) {
        self.stream = Array(repeating: nil, count: n + 1)
        self.ptr = 1
    }

    func insert(_ idKey: Int, _ value: String) -> [String] {
        stream[idKey] = value
        var result = [String]()
        while ptr < stream.count, let val = stream[ptr] {
            result.append(val)
            ptr += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class OrderedStream(n: Int) {
    private val stream = arrayOfNulls<String>(n + 1)
    private var ptr = 1
    fun insert(idKey: Int, value: String): List<String> {
        stream[idKey] = value
        val result = mutableListOf<String>()
        while (ptr < stream.size && stream[ptr] != null) {
            result.add(stream[ptr]!!)
            ptr++
        }
        return result
    }
}
```

## Dart

```dart
class OrderedStream {
  final List<String?> _stream;
  int _ptr = 1;

  OrderedStream(int n) : _stream = List.filled(n + 1, null);

  List<String> insert(int idKey, String value) {
    _stream[idKey] = value;
    List<String> result = [];
    while (_ptr < _stream.length && _stream[_ptr] != null) {
      result.add(_stream[_ptr]!);
      _ptr++;
    }
    return result;
  }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = OrderedStream(n);
 * List<String> param1 = obj.insert(idKey,value);
 */
```

## Golang

```go
type OrderedStream struct {
	stream []string
	ptr    int
}

func Constructor(n int) OrderedStream {
	return OrderedStream{
		stream: make([]string, n+1), // 1-indexed
		ptr:    1,
	}
}

func (this *OrderedStream) Insert(idKey int, value string) []string {
	this.stream[idKey] = value
	var res []string
	for this.ptr < len(this.stream) && this.stream[this.ptr] != "" {
		res = append(res, this.stream[this.ptr])
		this.ptr++
	}
	return res
}
```

## Ruby

```ruby
class OrderedStream
  def initialize(n)
    @stream = Array.new(n + 1)
    @ptr = 1
  end

  def insert(id_key, value)
    @stream[id_key] = value
    result = []
    while @ptr < @stream.length && !@stream[@ptr].nil?
      result << @stream[@ptr]
      @ptr += 1
    end
    result
  end
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer

class OrderedStream(_n: Int) {
  private val data = new Array[String](_n + 1)
  private var ptr = 1

  def insert(idKey: Int, value: String): List[String] = {
    data(idKey) = value
    val result = ListBuffer[String]()
    while (ptr <= _n && data(ptr) != null) {
      result += data(ptr)
      ptr += 1
    }
    result.toList
  }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * val obj = new OrderedStream(n)
 * val param_1 = obj.insert(idKey,value)
 */
```

## Rust

```rust
struct OrderedStream {
    stream: Vec<Option<String>>,
    ptr: usize,
}

impl OrderedStream {
    fn new(n: i32) -> Self {
        let size = n as usize + 1; // 1-indexed, ignore index 0
        OrderedStream {
            stream: vec![None; size],
            ptr: 1,
        }
    }

    fn insert(&mut self, id_key: i32, value: String) -> Vec<String> {
        let idx = id_key as usize;
        self.stream[idx] = Some(value);
        let mut result = Vec::new();
        while self.ptr < self.stream.len() {
            if let Some(v) = self.stream[self.ptr].take() {
                result.push(v);
                self.ptr += 1;
            } else {
                break;
            }
        }
        result
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * let mut obj = OrderedStream::new(n);
 * let ret_1: Vec<String> = obj.insert(idKey, value);
 */
```

## Racket

```racket
(define ordered-stream%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field n)
    
    ; internal storage and pointer
    (field [arr (make-vector (+ n 1) #f)]
           [ptr 1])
    
    ; insert : exact-integer? string? -> (listof string?)
    (define/public (insert id-key value)
      (vector-set! arr id-key value)
      (let loop ((out '()))
        (if (and (<= ptr n) (not (eq? (vector-ref arr ptr) #f)))
            (begin
              (set! out (cons (vector-ref arr ptr) out))
              (set! ptr (+ ptr 1))
              (loop out))
            (reverse out))))))
```

## Erlang

```erlang
-spec ordered_stream_init_(N :: integer()) -> any().
ordered_stream_init_(N) ->
    put(stream_map, #{}),
    put(ptr, 1),
    ok.

-spec ordered_stream_insert(IdKey :: integer(), Value :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
ordered_stream_insert(IdKey, Value) ->
    Map = get(stream_map),
    NewMap = maps:put(IdKey, Value, Map),
    put(stream_map, NewMap),
    Ptr = get(ptr),
    fetch(Ptr, NewMap, []).

fetch(Ptr, Map, Acc) when maps:is_key(Ptr, Map) ->
    Val = maps:get(Ptr, Map),
    fetch(Ptr + 1, Map, [Val | Acc]);
fetch(Ptr, _Map, Acc) ->
    put(ptr, Ptr),
    lists:reverse(Acc).
```

## Elixir

```elixir
defmodule OrderedStream do
  @spec init_(n :: integer) :: :ok
  def init_(n) do
    state = %{n: n, data: %{}, ptr: 1}
    Process.put(:ordered_stream_state, state)
    :ok
  end

  @spec insert(id_key :: integer, value :: String.t()) :: [String.t()]
  def insert(id_key, value) do
    state = Process.get(:ordered_stream_state)

    data = Map.put(state.data, id_key, value)

    {output, new_ptr} = collect(data, state.ptr)

    new_state = %{state | data: data, ptr: new_ptr}
    Process.put(:ordered_stream_state, new_state)

    output
  end

  defp collect(data, ptr) do
    case Map.fetch(data, ptr) do
      {:ok, v} ->
        {rest, next_ptr} = collect(data, ptr + 1)
        {[v | rest], next_ptr}

      :error ->
        {[], ptr}
    end
  end
end
```
