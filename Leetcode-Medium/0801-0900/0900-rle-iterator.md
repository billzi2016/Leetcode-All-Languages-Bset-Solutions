# 0900. RLE Iterator

## Cpp

```cpp
class RLEIterator {
public:
    RLEIterator(std::vector<int>& encoding) {
        enc.reserve(encoding.size());
        for (int x : encoding) enc.push_back(x);
        pos = 0;
        advanceToNextNonZero();
        if (pos < enc.size()) {
            remaining = enc[pos];
            val = static_cast<int>(enc[pos + 1]);
        } else {
            remaining = 0;
            val = -1;
        }
    }
    
    int next(int n) {
        long long need = n;
        while (need > 0 && pos < enc.size()) {
            if (remaining > need) {
                remaining -= need;
                return val;
            } else {
                need -= remaining;
                // move to next pair
                pos += 2;
                advanceToNextNonZero();
                if (pos < enc.size()) {
                    remaining = enc[pos];
                    val = static_cast<int>(enc[pos + 1]);
                }
            }
        }
        return -1;
    }

private:
    std::vector<long long> enc;
    size_t pos;
    long long remaining;
    int val;

    void advanceToNextNonZero() {
        while (pos < enc.size() && enc[pos] == 0) {
            pos += 2;
        }
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */
```

## Java

```java
class RLEIterator {
    private final int[] encoding;
    private int idx;          // points to count element in encoding
    private long remaining;   // remaining occurrences of current value

    public RLEIterator(int[] encoding) {
        this.encoding = encoding;
        this.idx = 0;
        this.remaining = (encoding.length > 0) ? encoding[0] : 0;
    }

    public int next(int n) {
        long need = n;
        while (idx < encoding.length && need > 0) {
            if (remaining == 0) {
                idx += 2;
                if (idx < encoding.length) {
                    remaining = encoding[idx];
                }
                continue;
            }
            if (remaining >= need) {
                remaining -= need;
                return encoding[idx + 1];
            } else {
                need -= remaining;
                remaining = 0;
                // move to next pair in next iteration
            }
        }
        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.next(n);
 */
```

## Python

```python
class RLEIterator(object):
    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.encoding = encoding
        self.idx = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.idx < len(self.encoding):
            cnt = self.encoding[self.idx]
            if cnt >= n:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]
            else:
                n -= cnt
                self.idx += 2
        return -1
```

## Python3

```python
class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding):
            if self.encoding[self.idx] == 0:
                self.idx += 2
                continue
            cnt = self.encoding[self.idx]
            if cnt >= n:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx + 1]
            else:
                n -= cnt
                self.idx += 2
        return -1
```

## C

```c
typedef struct {
    int *enc;
    int size;
    int idx;          // index of current count in enc array (even index)
    long long remain; // remaining count for current value
} RLEIterator;

RLEIterator* rLEIteratorCreate(int* encoding, int encodingSize) {
    RLEIterator* obj = (RLEIterator*)malloc(sizeof(RLEIterator));
    obj->size = encodingSize;
    obj->enc = (int*)malloc(sizeof(int) * encodingSize);
    for (int i = 0; i < encodingSize; ++i) {
        obj->enc[i] = encoding[i];
    }
    obj->idx = 0;
    obj->remain = (encodingSize > 0) ? (long long)obj->enc[0] : 0;
    // skip leading zero counts
    while (obj->idx < obj->size && obj->remain == 0) {
        obj->idx += 2;
        if (obj->idx < obj->size) {
            obj->remain = (long long)obj->enc[obj->idx];
        }
    }
    return obj;
}

int rLEIteratorNext(RLEIterator* obj, int n) {
    long long need = n;
    while (need > 0 && obj->idx < obj->size) {
        if (obj->remain >= need) {
            obj->remain -= need;
            int val = obj->enc[obj->idx + 1];
            if (obj->remain == 0) {
                obj->idx += 2;
                if (obj->idx < obj->size) {
                    obj->remain = (long long)obj->enc[obj->idx];
                }
            }
            return val;
        } else {
            need -= obj->remain;
            obj->idx += 2;
            if (obj->idx >= obj->size) break;
            obj->remain = (long long)obj->enc[obj->idx];
        }
    }
    return -1;
}

void rLEIteratorFree(RLEIterator* obj) {
    if (!obj) return;
    free(obj->enc);
    free(obj);
}
```

## Csharp

```csharp
public class RLEIterator
{
    private readonly int[] _encoding;
    private int _index;          // points to count element in the pair
    private long _remaining;     // remaining occurrences of current value

    public RLEIterator(int[] encoding)
    {
        _encoding = encoding;
        _index = 0;
        if (_encoding.Length > 0)
            _remaining = _encoding[0];
    }

    public int Next(int n)
    {
        long need = n;

        while (_index < _encoding.Length && need > 0)
        {
            // Skip exhausted pairs (including initial zero counts)
            if (_remaining == 0)
            {
                _index += 2;
                if (_index >= _encoding.Length) break;
                _remaining = _encoding[_index];
                continue;
            }

            if (_remaining >= need)
            {
                _remaining -= need;
                return _encoding[_index + 1];
            }
            else
            {
                // consume all remaining of current value and move to next pair
                need -= _remaining;
                _remaining = 0; // will trigger skip in next loop iteration
            }
        }

        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.Next(n);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} encoding
 */
var RLEIterator = function(encoding) {
    this.encoding = encoding;
    this.pos = 0; // points to count of current pair
};

/** 
 * @param {number} n
 * @return {number}
 */
RLEIterator.prototype.next = function(n) {
    while (this.pos < this.encoding.length && n > 0) {
        const cnt = this.encoding[this.pos];
        if (cnt >= n) {
            // consume part of current count
            this.encoding[this.pos] -= n;
            return this.encoding[this.pos + 1];
        } else {
            // exhaust current value and move to next pair
            n -= cnt;
            this.pos += 2;
        }
    }
    return -1;
};
```

## Typescript

```typescript
class RLEIterator {
    private encoding: number[];
    private idx: number;      // points to count position (even index)
    private remaining: number;

    constructor(encoding: number[]) {
        this.encoding = encoding;
        this.idx = 0;
        this.remaining = this.encoding.length > 0 ? this.encoding[0] : 0;
    }

    next(n: number): number {
        while (n > 0 && this.idx < this.encoding.length) {
            if (this.remaining === 0) {
                this.idx += 2;
                if (this.idx >= this.encoding.length) break;
                this.remaining = this.encoding[this.idx];
                continue;
            }
            if (this.remaining >= n) {
                this.remaining -= n;
                return this.encoding[this.idx + 1];
            } else {
                n -= this.remaining;
                this.remaining = 0; // will advance in next loop iteration
            }
        }
        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = new RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
```

## Php

```php
<?php
class RLEIterator {
    private $encoding;
    private $idx = 0;

    /**
     * @param Integer[] $encoding
     */
    function __construct($encoding) {
        $this->encoding = $encoding;
        $this->idx = 0;
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function next($n) {
        $len = count($this->encoding);
        while ($this->idx < $len) {
            if ($this->encoding[$this->idx] >= $n) {
                $this->encoding[$this->idx] -= $n;
                return $this->encoding[$this->idx + 1];
            } else {
                $n -= $this->encoding[$this->idx];
                $this->idx += 2;
            }
        }
        return -1;
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * $obj = new RLEIterator($encoding);
 * $ret_1 = $obj->next($n);
 */
?>
```

## Swift

```swift
class RLEIterator {
    private var encoding: [Int]
    private var idx: Int = 0          // points to the count element
    private var remain: Int = 0       // remaining occurrences of current value

    init(_ encoding: [Int]) {
        self.encoding = encoding
        if !encoding.isEmpty {
            remain = encoding[0]
        }
    }

    func next(_ n: Int) -> Int {
        var need = n
        while idx < encoding.count {
            if remain == 0 {
                idx += 2
                if idx < encoding.count {
                    remain = encoding[idx]
                }
                continue
            }
            if need <= remain {
                remain -= need
                return encoding[idx + 1]
            } else {
                need -= remain
                remain = 0
                // loop will advance to the next pair in the next iteration
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class RLEIterator(encoding: IntArray) {
    private val enc = encoding
    private var idx = 0

    fun next(n: Int): Int {
        var need = n.toLong()
        while (idx < enc.size && need > 0) {
            if (enc[idx] == 0) {
                idx += 2
                continue
            }
            val cnt = enc[idx].toLong()
            return if (cnt >= need) {
                enc[idx] = (cnt - need).toInt()
                enc[idx + 1]
            } else {
                need -= cnt
                idx += 2
                continue
            }
        }
        return -1
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
```

## Dart

```dart
class RLEIterator {
  final List<int> _encoding;
  int _idx = 0; // points to count position
  int _remaining = 0;

  RLEIterator(List<int> encoding)
      : _encoding = encoding {
    if (_encoding.isNotEmpty) {
      _remaining = _encoding[0];
    }
  }

  int next(int n) {
    while (_idx < _encoding.length) {
      if (_remaining == 0) {
        // move to next pair
        _idx += 2;
        if (_idx >= _encoding.length) break;
        _remaining = _encoding[_idx];
        continue;
      }
      if (n <= _remaining) {
        _remaining -= n;
        return _encoding[_idx + 1];
      } else {
        n -= _remaining;
        _remaining = 0; // will advance in next loop iteration
      }
    }
    return -1;
  }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = RLEIterator(encoding);
 * int param1 = obj.next(n);
 */
```

## Golang

```go
type RLEIterator struct {
	encoding []int
	idx      int
	remain   int
}

func Constructor(encoding []int) RLEIterator {
	it := RLEIterator{
		encoding: encoding,
		idx:      0,
	}
	if len(encoding) > 0 {
		it.remain = encoding[0]
	}
	return it
}

func (it *RLEIterator) Next(n int) int {
	for n > 0 && it.idx < len(it.encoding) {
		if it.remain == 0 {
			it.idx += 2
			if it.idx >= len(it.encoding) {
				break
			}
			it.remain = it.encoding[it.idx]
		}
		if it.remain >= n {
			it.remain -= n
			return it.encoding[it.idx+1]
		}
		n -= it.remain
		it.remain = 0
	}
	return -1
}
```

## Ruby

```ruby
class RLEIterator
  # :type encoding: Integer[]
  def initialize(encoding)
    @encoding = encoding
    @idx = 0          # index of count in encoding
    @remain = @encoding.empty? ? 0 : @encoding[0]
  end

  # :type n: Integer
  # :rtype: Integer
  def next(n)
    ans = -1
    while n > 0 && @idx < @encoding.length
      if @remain == 0
        @idx += 2
        break if @idx >= @encoding.length
        @remain = @encoding[@idx]
        next
      end
      take = [n, @remain].min
      @remain -= take
      n -= take
      ans = @encoding[@idx + 1]
    end
    ans
  end
end
```

## Scala

```scala
class RLEIterator(_encoding: Array[Int]) {
  private val encoding = _encoding
  private var idx = 0               // points to count position in encoding
  private var remaining = if (encoding.isEmpty) 0 else encoding(0)

  def next(n: Int): Int = {
    var need = n
    while (idx < encoding.length && need > 0) {
      if (remaining == 0) {
        idx += 2
        if (idx < encoding.length) remaining = encoding(idx)
      } else if (remaining >= need) {
        remaining -= need
        return encoding(idx + 1)
      } else {
        need -= remaining
        remaining = 0
      }
    }
    -1
  }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * val obj = new RLEIterator(encoding)
 * val param_1 = obj.next(n)
 */
```

## Rust

```rust
struct RLEIterator {
    encoding: Vec<i32>,
    idx: usize,
    remaining: i64,
}

impl RLEIterator {
    fn new(encoding: Vec<i32>) -> Self {
        let mut it = RLEIterator {
            encoding,
            idx: 0,
            remaining: 0,
        };
        if !it.encoding.is_empty() {
            it.remaining = it.encoding[0] as i64;
        }
        it
    }

    fn next(&mut self, n: i32) -> i32 {
        let mut need = n as i64;
        while self.idx < self.encoding.len() && need > 0 {
            if self.remaining == 0 {
                self.idx += 2;
                if self.idx >= self.encoding.len() {
                    break;
                }
                self.remaining = self.encoding[self.idx] as i64;
            }
            if self.remaining >= need {
                self.remaining -= need;
                return self.encoding[self.idx + 1];
            } else {
                need -= self.remaining;
                self.remaining = 0;
            }
        }
        -1
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let mut obj = RLEIterator::new(encoding);
 * let ret_1: i32 = obj.next(n);
 */
```

## Racket

```racket
(define rle-iterator%
  (class object%
    (init-field encoding)
    (field [idx 0]          ; index in the encoding list
           [cnt 0]          ; remaining count of current value
           [val -1])        ; current value
    
    (define/public (next n)
      (let loop ()
        (cond
          [(= n 0) val]
          [(= cnt 0)
           (if (>= idx (length encoding))
               -1                                   ; no more elements
               (begin
                 (set! cnt (list-ref encoding idx))
                 (set! val (list-ref encoding (+ idx 1)))
                 (set! idx (+ idx 2))
                 (loop)))]
          [else
           (let* ([take (min n cnt)])
             (set! cnt (- cnt take))
             (set! n (- n take))
             (if (= n 0)
                 val
                 (loop)))])]))
)
```

## Erlang

```erlang
-module(rle_iterator).
-export([rle_iterator_init_/1, rle_iterator_next/1]).

%% Initialize the iterator with the run‑length encoded array.
-spec rle_iterator_init_(Encoding :: [integer()]) -> any().
rle_iterator_init_(Encoding) ->
    Pairs = build_pairs(Encoding),
    erlang:put(rle_state, {Pairs, 0}).

%% Return the last element exhausted after consuming N elements,
%% or -1 if the sequence runs out before finishing.
-spec rle_iterator_next(N :: integer()) -> integer().
rle_iterator_next(N) ->
    case erlang:get(rle_state) of
        undefined ->
            -1;
        {Pairs, Rem} ->
            {NewPairs, NewRem, Result} = consume(Pairs, Rem, N),
            erlang:put(rle_state, {NewPairs, NewRem}),
            Result
    end.

%% Convert flat encoding list to list of {Count, Value} tuples.
build_pairs([]) -> [];
build_pairs([Cnt, Val | Rest]) ->
    [{Cnt, Val} | build_pairs(Rest)].

%% Skip leading pairs with zero count.
skip_zero([]) -> [];
skip_zero([{0, _} | T]) -> skip_zero(T);
skip_zero(L) -> L.

%% Core consumption logic.
consume([], _Rem, _N) ->
    {[], 0, -1};
consume(Pairs, 0, N) ->
    case skip_zero(Pairs) of
        [] -> {[], 0, -1};
        [{Cnt, Val} | Rest] ->
            consume([{Cnt, Val} | Rest], Cnt, N)
    end;
consume(Pairs = [{_Cnt, Val} | _Tail] = List, Rem, N) when Rem > 0 ->
    case N =< Rem of
        true ->
            NewRem = Rem - N,
            {List, NewRem, Val};
        false ->
            N1 = N - Rem,
            Tail = tl(List),
            case skip_zero(Tail) of
                [] -> {[], 0, -1};
                [{Cnt2, Val2} | Rest2] ->
                    consume([{Cnt2, Val2} | Rest2], Cnt2, N1)
            end
    end.
```

## Elixir

```elixir
defmodule RLEIterator do
  @spec init_(encoding :: [integer]) :: any
  def init_(encoding) do
    :erlang.put(:rle_state, %{idx: 0, cnt: 0, val: -1, enc: encoding})
    :ok
  end

  @spec next(n :: integer) :: integer
  def next(n) do
    state = :erlang.get(:rle_state)
    enc = state.enc
    case consume(enc, state.idx, state.cnt, state.val, n, -1) do
      {:ok, new_idx, new_cnt, new_val, last} ->
        :erlang.put(:rle_state, %{idx: new_idx, cnt: new_cnt, val: new_val, enc: enc})
        last

      {:error, _} ->
        :erlang.put(:rle_state, %{idx: length(enc), cnt: 0, val: -1, enc: enc})
        -1
    end
  end

  defp consume(_enc, idx, _cnt, _val, n, _last) when n == 0 do
    {:ok, idx, 0, -1, -1}
  end

  defp consume(enc, idx, cnt, val, n, last) do
    len = length(enc)

    cond do
      idx >= len ->
        {:error, -1}

      cnt == 0 ->
        count = Enum.at(enc, idx)
        value = Enum.at(enc, idx + 1)
        consume(enc, idx + 2, count, value, n, last)

      true ->
        take = min(cnt, n)
        new_cnt = cnt - take
        new_n = n - take
        new_last = val

        if new_n == 0 do
          {:ok, idx, new_cnt, val, new_last}
        else
          # current run exhausted, move to next pair on next recursion
          consume(enc, idx, new_cnt, val, new_n, new_last)
        end
    end
  end
end
```
