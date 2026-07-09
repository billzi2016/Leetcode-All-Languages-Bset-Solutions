# 2502. Design Memory Allocator

## Cpp

```cpp
class Allocator {
public:
    vector<int> mem;
    int n;
    Allocator(int n) : n(n), mem(n, 0) {}
    
    int allocate(int size, int mID) {
        if (size > n) return -1;
        for (int i = 0; i + size <= n; ++i) {
            bool ok = true;
            for (int j = i; j < i + size; ++j) {
                if (mem[j] != 0) { ok = false; break; }
            }
            if (ok) {
                for (int j = i; j < i + size; ++j) mem[j] = mID;
                return i;
            }
        }
        return -1;
    }
    
    int freeMemory(int mID) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (mem[i] == mID) {
                mem[i] = 0;
                ++cnt;
            }
        }
        return cnt;
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
 */
```

## Java

```java
class Allocator {
    private final int[] memory;

    public Allocator(int n) {
        memory = new int[n];
    }

    public int allocate(int size, int mID) {
        if (size > memory.length) return -1;
        for (int i = 0; i <= memory.length - size; i++) {
            boolean free = true;
            for (int j = i; j < i + size; j++) {
                if (memory[j] != 0) {
                    free = false;
                    break;
                }
            }
            if (free) {
                for (int j = i; j < i + size; j++) {
                    memory[j] = mID;
                }
                return i;
            }
        }
        return -1;
    }

    public int freeMemory(int mID) {
        int freed = 0;
        for (int i = 0; i < memory.length; i++) {
            if (memory[i] == mID) {
                memory[i] = 0;
                freed++;
            }
        }
        return freed;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.freeMemory(mID);
 */
```

## Python

```python
class Allocator(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.mem = [0] * n

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        n = len(self.mem)
        consecutive = 0
        start = -1
        for i in range(n):
            if self.mem[i] == 0:
                if consecutive == 0:
                    start = i
                consecutive += 1
                if consecutive == size:
                    # allocate block
                    for j in range(start, start + size):
                        self.mem[j] = mID
                    return start
            else:
                consecutive = 0
        return -1

    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        count = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                count += 1
        return count

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
```

## Python3

```python
class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        start = -1
        for i, val in enumerate(self.mem):
            if val == 0:
                if cnt == 0:
                    start = i
                cnt += 1
                if cnt == size:
                    for k in range(start, start + size):
                        self.mem[k] = mID
                    return start
            else:
                cnt = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                freed += 1
        return freed
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;
    int *mem; // 0 means free, otherwise holds mID
} Allocator;

Allocator* allocatorCreate(int n) {
    Allocator *obj = (Allocator *)malloc(sizeof(Allocator));
    obj->n = n;
    obj->mem = (int *)calloc(n, sizeof(int)); // initialized to 0 (free)
    return obj;
}

int allocatorAllocate(Allocator* obj, int size, int mID) {
    if (size > obj->n) return -1;
    for (int i = 0; i <= obj->n - size; ++i) {
        int j;
        for (j = 0; j < size; ++j) {
            if (obj->mem[i + j] != 0) break;
        }
        if (j == size) { // found a block
            for (int k = 0; k < size; ++k) {
                obj->mem[i + k] = mID;
            }
            return i;
        }
    }
    return -1;
}

int allocatorFreeMemory(Allocator* obj, int mID) {
    int cnt = 0;
    for (int i = 0; i < obj->n; ++i) {
        if (obj->mem[i] == mID) {
            obj->mem[i] = 0;
            ++cnt;
        }
    }
    return cnt;
}

void allocatorFree(Allocator* obj) {
    if (!obj) return;
    free(obj->mem);
    free(obj);
}

/**
 * Your Allocator struct will be instantiated and called as such:
 * Allocator* obj = allocatorCreate(n);
 * int param_1 = allocatorAllocate(obj, size, mID);
 * int param_2 = allocatorFreeMemory(obj, mID);
 * allocatorFree(obj);
 */
```

## Csharp

```csharp
public class Allocator
{
    private readonly int[] _memory;
    private readonly int _size;

    public Allocator(int n)
    {
        _size = n;
        _memory = new int[n];
    }

    public int Allocate(int size, int mID)
    {
        if (size > _size) return -1;
        int consecutive = 0;
        for (int i = 0; i < _size; i++)
        {
            if (_memory[i] == 0)
                consecutive++;
            else
                consecutive = 0;

            if (consecutive == size)
            {
                int start = i - size + 1;
                for (int j = start; j <= i; j++)
                    _memory[j] = mID;
                return start;
            }
        }
        return -1;
    }

    public int FreeMemory(int mID)
    {
        int freed = 0;
        for (int i = 0; i < _size; i++)
        {
            if (_memory[i] == mID)
            {
                _memory[i] = 0;
                freed++;
            }
        }
        return freed;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.Allocate(size,mID);
 * int param_2 = obj.FreeMemory(mID);
 */
```

## Javascript

```javascript
/**
 * @param {number} n
 */
var Allocator = function(n) {
    this.mem = new Array(n).fill(0);
};

/** 
 * @param {number} size 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.allocate = function(size, mID) {
    const n = this.mem.length;
    if (size > n) return -1;
    for (let i = 0; i <= n - size; i++) {
        let ok = true;
        for (let j = i; j < i + size; j++) {
            if (this.mem[j] !== 0) { ok = false; break; }
        }
        if (ok) {
            for (let j = i; j < i + size; j++) this.mem[j] = mID;
            return i;
        }
    }
    return -1;
};

/** 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.freeMemory = function(mID) {
    let cnt = 0;
    for (let i = 0; i < this.mem.length; i++) {
        if (this.mem[i] === mID) {
            this.mem[i] = 0;
            cnt++;
        }
    }
    return cnt;
};
```

## Typescript

```typescript
class Allocator {
    private memory: number[];
    private n: number;

    constructor(n: number) {
        this.n = n;
        this.memory = new Array<number>(n).fill(0);
    }

    allocate(size: number, mID: number): number {
        if (size > this.n) return -1;
        for (let i = 0; i <= this.n - size; i++) {
            let ok = true;
            for (let j = i; j < i + size; j++) {
                if (this.memory[j] !== 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                for (let j = i; j < i + size; j++) {
                    this.memory[j] = mID;
                }
                return i;
            }
        }
        return -1;
    }

    freeMemory(mID: number): number {
        let freed = 0;
        for (let i = 0; i < this.n; i++) {
            if (this.memory[i] === mID) {
                this.memory[i] = 0;
                freed++;
            }
        }
        return freed;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = new Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */
```

## Php

```php
class Allocator {
    private $mem;
    private $n;

    /**
     * @param Integer $n
     */
    function __construct($n) {
        $this->n = $n;
        // Initialize memory with zeros (free)
        $this->mem = array_fill(0, $n, 0);
    }

    /**
     * @param Integer $size
     * @param Integer $mID
     * @return Integer
     */
    function allocate($size, $mID) {
        if ($size > $this->n) {
            return -1;
        }
        for ($i = 0; $i <= $this->n - $size; $i++) {
            $canAllocate = true;
            for ($j = $i; $j < $i + $size; $j++) {
                if ($this->mem[$j] !== 0) {
                    $canAllocate = false;
                    break;
                }
            }
            if ($canAllocate) {
                for ($j = $i; $j < $i + $size; $j++) {
                    $this->mem[$j] = $mID;
                }
                return $i;
            }
        }
        return -1;
    }

    /**
     * @param Integer $mID
     * @return Integer
     */
    function freeMemory($mID) {
        $freed = 0;
        for ($i = 0; $i < $this->n; $i++) {
            if ($this->mem[$i] === $mID) {
                $this->mem[$i] = 0;
                $freed++;
            }
        }
        return $freed;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * $obj = new Allocator($n);
 * $ret_1 = $obj->allocate($size, $mID);
 * $ret_2 = $obj->freeMemory($mID);
 */
```

## Swift

```swift
class Allocator {
    private var memory: [Int]

    init(_ n: Int) {
        self.memory = Array(repeating: 0, count: n)
    }

    func allocate(_ size: Int, _ mID: Int) -> Int {
        let n = memory.count
        if size > n { return -1 }
        var i = 0
        while i <= n - size {
            if memory[i] != 0 {
                i += 1
                continue
            }
            var j = i
            while j < i + size && memory[j] == 0 {
                j += 1
            }
            if j == i + size {
                for k in i..<i+size {
                    memory[k] = mID
                }
                return i
            } else {
                i = j + 1
            }
        }
        return -1
    }

    func freeMemory(_ mID: Int) -> Int {
        var count = 0
        for idx in memory.indices {
            if memory[idx] == mID {
                memory[idx] = 0
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Allocator(n: Int) {
    private val memory = IntArray(n)

    fun allocate(size: Int, mID: Int): Int {
        if (size > memory.size) return -1
        var i = 0
        while (i <= memory.size - size) {
            var j = 0
            while (j < size && memory[i + j] == 0) {
                j++
            }
            if (j == size) {
                for (k in i until i + size) {
                    memory[k] = mID
                }
                return i
            }
            // skip past the occupied cell that broke the run
            i += if (j == 0) 1 else j
        }
        return -1
    }

    fun freeMemory(mID: Int): Int {
        var freed = 0
        for (i in memory.indices) {
            if (memory[i] == mID) {
                memory[i] = 0
                freed++
            }
        }
        return freed
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */
```

## Dart

```dart
class Allocator {
  late final List<int> _mem;
  final int _n;

  Allocator(int n)
      : _n = n,
        _mem = List.filled(n, 0);

  int allocate(int size, int mID) {
    if (size > _n) return -1;
    for (int i = 0; i <= _n - size; ++i) {
      bool canPlace = true;
      for (int j = i; j < i + size; ++j) {
        if (_mem[j] != 0) {
          canPlace = false;
          break;
        }
      }
      if (canPlace) {
        for (int j = i; j < i + size; ++j) {
          _mem[j] = mID;
        }
        return i;
      }
    }
    return -1;
  }

  int freeMemory(int mID) {
    int freed = 0;
    for (int i = 0; i < _n; ++i) {
      if (_mem[i] == mID) {
        _mem[i] = 0;
        ++freed;
      }
    }
    return freed;
  }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = Allocator(n);
 * int param1 = obj.allocate(size,mID);
 * int param2 = obj.freeMemory(mID);
 */
```

## Golang

```go
type Allocator struct {
	mem []int
}

func Constructor(n int) Allocator {
	return Allocator{mem: make([]int, n)}
}

func (this *Allocator) Allocate(size int, mID int) int {
	if size > len(this.mem) {
		return -1
	}
	n := len(this.mem)
	for i := 0; i <= n-size; i++ {
		ok := true
		for j := 0; j < size; j++ {
			if this.mem[i+j] != 0 {
				ok = false
				break
			}
		}
		if ok {
			for j := 0; j < size; j++ {
				this.mem[i+j] = mID
			}
			return i
		}
	}
	return -1
}

func (this *Allocator) FreeMemory(mID int) int {
	count := 0
	for i, v := range this.mem {
		if v == mID {
			this.mem[i] = 0
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
class Allocator
  def initialize(n)
    @mem = Array.new(n, 0)
  end

  def allocate(size, m_id)
    n = @mem.length
    return -1 if size > n
    i = 0
    while i <= n - size
      j = i
      while j < i + size && @mem[j] == 0
        j += 1
      end
      if j == i + size
        (i...i + size).each { |k| @mem[k] = m_id }
        return i
      else
        i = j + 1
      end
    end
    -1
  end

  def free_memory(m_id)
    count = 0
    @mem.map! do |v|
      if v == m_id
        count += 1
        0
      else
        v
      end
    end
    count
  end
end
```

## Scala

```scala
class Allocator(_n: Int) {
  private val mem = Array.fill(_n)(0)

  def allocate(size: Int, mID: Int): Int = {
    if (size > mem.length) return -1
    var i = 0
    while (i <= mem.length - size) {
      var ok = true
      var j = 0
      while (j < size && ok) {
        if (mem(i + j) != 0) ok = false
        j += 1
      }
      if (ok) {
        var k = 0
        while (k < size) {
          mem(i + k) = mID
          k += 1
        }
        return i
      }
      i += 1
    }
    -1
  }

  def freeMemory(mID: Int): Int = {
    var cnt = 0
    var i = 0
    while (i < mem.length) {
      if (mem(i) == mID) {
        mem(i) = 0
        cnt += 1
      }
      i += 1
    }
    cnt
  }
}
```

## Rust

```rust
struct Allocator {
    mem: Vec<i32>,
}

impl Allocator {
    fn new(n: i32) -> Self {
        Allocator { mem: vec![0; n as usize] }
    }

    fn allocate(&mut self, size: i32, m_id: i32) -> i32 {
        let sz = size as usize;
        if sz == 0 || sz > self.mem.len() {
            return -1;
        }
        let mut cnt = 0usize;
        for i in 0..self.mem.len() {
            if self.mem[i] == 0 {
                cnt += 1;
            } else {
                cnt = 0;
            }
            if cnt == sz {
                let start = i + 1 - sz;
                for j in start..=i {
                    self.mem[j] = m_id;
                }
                return start as i32;
            }
        }
        -1
    }

    fn free_memory(&mut self, m_id: i32) -> i32 {
        let mut freed = 0;
        for cell in &mut self.mem {
            if *cell == m_id {
                *cell = 0;
                freed += 1;
            }
        }
        freed as i32
    }
}
```

## Racket

```racket
(define allocator%
  (class object%
    (super-new)

    ; n : exact-integer?
    (init-field
      n)

    (define memory (make-vector n 0))

    ; allocate : exact-integer? exact-integer? -> exact-integer?
    (define/public (allocate size m-id)
      (let ((len (vector-length memory)))
        (if (> size len)
            -1
            (call/cc
              (lambda (return)
                (let ((max (- len size)))
                  (for ([i (in-range 0 (+ max 1))])
                    (let loop ((j 0))
                      (cond [(= j size)
                             (for ([k (in-range size)])
                               (vector-set! memory (+ i k) m-id))
                             (return i)]
                            [else
                             (if (= (vector-ref memory (+ i j)) 0)
                                 (loop (+ j 1))
                                 (void))])))
                  -1))))))

    ; free-memory : exact-integer? -> exact-integer?
    (define/public (free-memory m-id)
      (let ((cnt 0))
        (for ([i (in-range (vector-length memory))])
          (when (= (vector-ref memory i) m-id)
            (vector-set! memory i 0)
            (set! cnt (+ cnt 1))))
        cnt))))
```

## Erlang

```erlang
-spec allocator_init_(N :: integer()) -> any().
allocator_init_(N) ->
    Memory = lists:duplicate(N, 0),
    put(memory, Memory).

-spec allocator_allocate(Size :: integer(), MID :: integer()) -> integer().
allocator_allocate(Size, MID) ->
    Mem = get(memory),
    N = length(Mem),
    Start = find_start(Mem, Size, 0, N),
    case Start of
        -1 -> -1;
        _ ->
            NewMem = set_range(Mem, Start, Size, MID),
            put(memory, NewMem),
            Start
    end.

-spec allocator_free_memory(MID :: integer()) -> integer().
allocator_free_memory(MID) ->
    Mem = get(memory),
    {NewMem, Count} = free_mem(Mem, MID, 0),
    put(memory, NewMem),
    Count.

%% helper functions

find_start(_Mem, Size, Idx, N) when Idx > N - Size -> -1;
find_start(Mem, Size, Idx, N) ->
    case all_free(Mem, Idx, Size) of
        true -> Idx;
        false -> find_start(Mem, Size, Idx + 1, N)
    end.

all_free(_Mem, _Start, 0) -> true;
all_free(Mem, Start, Size) ->
    case lists:nth(Start + 1, Mem) of
        0 -> all_free(Mem, Start + 1, Size - 1);
        _ -> false
    end.

set_range(Mem, Start, Size, MID) ->
    set_range(Mem, 0, Start, Size, MID).

set_range([], _Idx, _Start, _Size, _MID) -> [];
set_range([H|T], Idx, Start, Size, MID) ->
    if
        Idx >= Start, Idx < Start + Size ->
            [MID | set_range(T, Idx + 1, Start, Size, MID)];
        true ->
            [H   | set_range(T, Idx + 1, Start, Size, MID)]
    end.

free_mem([], _MID, Count) -> {[], Count};
free_mem([H|T], MID, Count) ->
    if
        H =:= MID ->
            {Rest, NewCount} = free_mem(T, MID, Count + 1),
            {[0 | Rest], NewCount};
        true ->
            {Rest, NewCount} = free_mem(T, MID, Count),
            {[H | Rest], NewCount}
    end.
```

## Elixir

```elixir
defmodule Allocator do
  @spec init_(n :: integer) :: any
  def init_(n) do
    Process.put(:memory, List.duplicate(0, n))
    :ok
  end

  @spec allocate(size :: integer, m_id :: integer) :: integer
  def allocate(size, m_id) do
    mem = Process.get(:memory)
    len = length(mem)

    start =
      find_start(mem, size, 0, len - size)

    if start == nil do
      -1
    else
      new_mem =
        Enum.with_index(mem)
        |> Enum.map(fn {val, idx} ->
          if idx >= start and idx < start + size, do: m_id, else: val
        end)

      Process.put(:memory, new_mem)
      start
    end
  end

  defp find_start(_mem, _size, i, max) when i > max, do: nil
  defp find_start(mem, size, i, max) do
    if Enum.slice(mem, i, size) |> Enum.all?(&(&1 == 0)) do
      i
    else
      find_start(mem, size, i + 1, max)
    end
  end

  @spec free_memory(m_id :: integer) :: integer
  def free_memory(m_id) do
    mem = Process.get(:memory)

    count = Enum.count(mem, fn x -> x == m_id end)

    if count > 0 do
      new_mem =
        Enum.map(mem, fn x ->
          if x == m_id, do: 0, else: x
        end)

      Process.put(:memory, new_mem)
    end

    count
  end
end
```
