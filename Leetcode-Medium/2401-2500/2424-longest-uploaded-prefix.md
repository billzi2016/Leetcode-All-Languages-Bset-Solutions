# 2424. Longest Uploaded Prefix

## Cpp

```cpp
class LUPrefix {
public:
    LUPrefix(int n) : uploaded(n + 2, 0), cur(0) {}
    
    void upload(int video) {
        uploaded[video] = 1;
        while (uploaded[cur + 1]) ++cur;
    }
    
    int longest() {
        return cur;
    }

private:
    std::vector<char> uploaded;
    int cur;
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix* obj = new LUPrefix(n);
 * obj->upload(video);
 * int param_2 = obj->longest();
 */
```

## Java

```java
class LUPrefix {
    private final boolean[] uploaded;
    private int longestPrefix;

    public LUPrefix(int n) {
        uploaded = new boolean[n + 2]; // extra space to avoid bound checks
        longestPrefix = 0;
    }

    public void upload(int video) {
        uploaded[video] = true;
        while (uploaded[longestPrefix + 1]) {
            longestPrefix++;
        }
    }

    public int longest() {
        return longestPrefix;
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = new LUPrefix(n);
 * obj.upload(video);
 * int param_2 = obj.longest();
 */
```

## Python

```python
class LUPrefix(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.uploaded = [False] * (n + 2)  # extra space for 1-indexing
        self.cur = 0

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.uploaded[video] = True
        while self.cur + 1 <= self.n and self.uploaded[self.cur + 1]:
            self.cur += 1

    def longest(self):
        """
        :rtype: int
        """
        return self.cur
```

## Python3

```python
class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)  # extra space for easy index
        self.cur = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.cur + 1]:
            self.cur += 1

    def longest(self) -> int:
        return self.cur
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;
    int *uploaded;
    int cur;
} LUPrefix;

LUPrefix* lUPrefixCreate(int n) {
    LUPrefix* obj = (LUPrefix*)malloc(sizeof(LUPrefix));
    if (!obj) return NULL;
    obj->n = n;
    obj->cur = 0;
    obj->uploaded = (int*)calloc(n + 2, sizeof(int)); // indices 1..n
    return obj;
}

void lUPrefixUpload(LUPrefix* obj, int video) {
    if (!obj || video < 1 || video > obj->n) return;
    obj->uploaded[video] = 1;
    while (obj->cur < obj->n && obj->uploaded[obj->cur + 1]) {
        obj->cur++;
    }
}

int lUPrefixLongest(LUPrefix* obj) {
    if (!obj) return 0;
    return obj->cur;
}

void lUPrefixFree(LUPrefix* obj) {
    if (!obj) return;
    free(obj->uploaded);
    free(obj);
}
```

## Csharp

```csharp
public class LUPrefix
{
    private readonly bool[] _uploaded;
    private int _longest;

    public LUPrefix(int n)
    {
        _uploaded = new bool[n + 2];
        _longest = 0;
    }

    public void Upload(int video)
    {
        if (!_uploaded[video])
        {
            _uploaded[video] = true;
            while (_uploaded[_longest + 1])
                _longest++;
        }
    }

    public int Longest()
    {
        return _longest;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 */
var LUPrefix = function(n) {
    this.n = n;
    this.uploaded = new Array(n + 2).fill(false);
    this.cur = 0;
};

/** 
 * @param {number} video
 * @return {void}
 */
LUPrefix.prototype.upload = function(video) {
    this.uploaded[video] = true;
    while (this.cur + 1 <= this.n && this.uploaded[this.cur + 1]) {
        this.cur++;
    }
};

/**
 * @return {number}
 */
LUPrefix.prototype.longest = function() {
    return this.cur;
};
```

## Typescript

```typescript
class LUPrefix {
    private uploaded: boolean[];
    private cur: number;

    constructor(n: number) {
        this.uploaded = new Array(n + 2).fill(false);
        this.cur = 0;
    }

    upload(video: number): void {
        this.uploaded[video] = true;
        while (this.uploaded[this.cur + 1]) {
            this.cur++;
        }
    }

    longest(): number {
        return this.cur;
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = new LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */
```

## Php

```php
class LUPrefix {
    /**
     * @param Integer $n
     */
    private $n;
    private $uploaded;
    private $cur = 0;

    function __construct($n) {
        $this->n = $n;
        // indices from 1..n, extra slot for easier check
        $this->uploaded = array_fill(0, $n + 2, false);
    }

    /**
     * @param Integer $video
     * @return NULL
     */
    function upload($video) {
        $this->uploaded[$video] = true;
        while ($this->cur < $this->n && $this->uploaded[$this->cur + 1]) {
            $this->cur++;
        }
    }

    /**
     * @return Integer
     */
    function longest() {
        return $this->cur;
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * $obj = new LUPrefix($n);
 * $obj->upload($video);
 * $ret_2 = $obj->longest();
 */
```

## Swift

```swift
class LUPrefix {
    private var uploaded: [Bool]
    private var current: Int = 0
    private let n: Int

    init(_ n: Int) {
        self.n = n
        // extra slot to avoid bounds check when accessing cur+1
        self.uploaded = Array(repeating: false, count: n + 2)
    }
    
    func upload(_ video: Int) {
        guard video >= 1 && video <= n else { return }
        if !uploaded[video] {
            uploaded[video] = true
            while uploaded[current + 1] {
                current += 1
            }
        }
    }
    
    func longest() -> Int {
        return current
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * let obj = LUPrefix(n)
 * obj.upload(video)
 * let ret_2: Int = obj.longest()
 */
```

## Kotlin

```kotlin
class LUPrefix(n: Int) {
    private val uploaded = BooleanArray(n + 2)
    private var longestPrefix = 0
    private val maxN = n

    fun upload(video: Int) {
        if (video < 1 || video > maxN) return
        uploaded[video] = true
        while (longestPrefix + 1 <= maxN && uploaded[longestPrefix + 1]) {
            longestPrefix++
        }
    }

    fun longest(): Int {
        return longestPrefix
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */
```

## Dart

```dart
class LUPrefix {
  late final List<bool> _uploaded;
  final int _n;
  int _cur = 0;

  LUPrefix(int n)
      : _n = n,
        _uploaded = List.filled(n + 2, false);

  void upload(int video) {
    if (!_uploaded[video]) {
      _uploaded[video] = true;
      while (_cur + 1 <= _n && _uploaded[_cur + 1]) {
        _cur++;
      }
    }
  }

  int longest() => _cur;
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = LUPrefix(n);
 * obj.upload(video);
 * int param2 = obj.longest();
 */
```

## Golang

```go
type LUPrefix struct {
	uploaded []bool
	cur      int
}

func Constructor(n int) LUPrefix {
	return LUPrefix{
		uploaded: make([]bool, n+2),
		cur:      0,
	}
}

func (this *LUPrefix) Upload(video int) {
	this.uploaded[video] = true
	for this.cur+1 < len(this.uploaded) && this.uploaded[this.cur+1] {
		this.cur++
	}
}

func (this *LUPrefix) Longest() int {
	return this.cur
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * obj := Constructor(n);
 * obj.Upload(video);
 * param_2 := obj.Longest();
 */
```

## Ruby

```ruby
class LUPrefix
  # Initialize the data structure with total number of videos n.
  def initialize(n)
    @uploaded = Array.new(n + 2, false) # extra space to avoid bounds check
    @cur = 0
  end

  # Mark a video as uploaded.
  def upload(video)
    @uploaded[video] = true
    while @uploaded[@cur + 1]
      @cur += 1
    end
  end

  # Return the length of the longest uploaded prefix.
  def longest
    @cur
  end
end
```

## Scala

```scala
class LUPrefix(_n: Int) {
  private val uploaded = new Array[Boolean](_n + 2)
  private var cur = 0

  def upload(video: Int): Unit = {
    if (!uploaded(video)) {
      uploaded(video) = true
      while (cur < _n && uploaded(cur + 1)) {
        cur += 1
      }
    }
  }

  def longest(): Int = cur
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * val obj = new LUPrefix(n)
 * obj.upload(video)
 * val param_2 = obj.longest()
 */
```

## Rust

```rust
use std::cell::{Cell, RefCell};

struct LUPrefix {
    uploaded: RefCell<Vec<bool>>,
    cur: Cell<usize>,
    n: usize,
}

impl LUPrefix {
    fn new(n: i32) -> Self {
        let size = n as usize + 2;
        LUPrefix {
            uploaded: RefCell::new(vec![false; size]),
            cur: Cell::new(0),
            n: n as usize,
        }
    }

    fn upload(&self, video: i32) {
        let v = video as usize;
        {
            let mut vec = self.uploaded.borrow_mut();
            vec[v] = true;
        }
        while {
            let cur = self.cur.get();
            cur + 1 <= self.n && self.uploaded.borrow()[cur + 1]
        } {
            let next = self.cur.get() + 1;
            self.cur.set(next);
        }
    }

    fn longest(&self) -> i32 {
        self.cur.get() as i32
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * let obj = LUPrefix::new(n);
 * obj.upload(video);
 * let ret_2: i32 = obj.longest();
 */
```

## Racket

```racket
(define lu-prefix%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; mutable state: current longest prefix and visited flags
    (define cur 0)
    (define visited (make-vector (+ n 1) #f))
    
    ; upload : exact-integer? -> void?
    (define/public (upload video)
      (vector-set! visited video #t)
      (let loop ()
        (when (and (< cur n) (vector-ref visited (+ cur 1)))
          (set! cur (+ cur 1))
          (loop))))
    
    ; longest : -> exact-integer?
    (define/public (longest)
      cur)))
```

## Erlang

```erlang
-module(luprefix).
-export([lu_prefix_init_/1, lu_prefix_upload/1, lu_prefix_longest/0]).

-spec lu_prefix_init_(N :: integer()) -> any().
lu_prefix_init_(N) ->
    put(n, N),
    put(uploaded, #{}),
    put(cur, 0).

-spec lu_prefix_upload(Video :: integer()) -> any().
lu_prefix_upload(Video) ->
    Uploaded = get(uploaded),
    NewUploaded = maps:put(Video, true, Uploaded),
    put(uploaded, NewUploaded),
    Cur = get(cur),
    UpdatedCur = update_cur(NewUploaded, Cur),
    put(cur, UpdatedCur).

-spec lu_prefix_longest() -> integer().
lu_prefix_longest() ->
    get(cur).

%% Helper function to advance the current longest prefix as far as possible.
update_cur(UploadedMap, Cur) ->
    case maps:is_key(Cur + 1, UploadedMap) of
        true -> update_cur(UploadedMap, Cur + 1);
        false -> Cur
    end.
```

## Elixir

```elixir
defmodule LUPrefix do
  @spec init_(n :: integer) :: any
  def init_(_n) do
    Process.put(:luprefix_state, %{ptr: 0, uploaded: MapSet.new()})
    nil
  end

  @spec upload(video :: integer) :: any
  def upload(video) do
    state = Process.get(:luprefix_state)
    uploaded = MapSet.put(state.uploaded, video)

    new_ptr =
      advance(state.ptr, uploaded)

    Process.put(:luprefix_state, %{ptr: new_ptr, uploaded: uploaded})
    nil
  end

  defp advance(ptr, uploaded) do
    if MapSet.member?(uploaded, ptr + 1) do
      advance(ptr + 1, uploaded)
    else
      ptr
    end
  end

  @spec longest() :: integer
  def longest() do
    state = Process.get(:luprefix_state)
    state.ptr
  end
end
```
