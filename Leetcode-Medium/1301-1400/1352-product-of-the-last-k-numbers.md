# 1352. Product of the Last K Numbers

## Cpp

```cpp
class ProductOfNumbers {
public:
    std::vector<long long> pref;
    ProductOfNumbers() {
        pref.push_back(1); // initial dummy product
    }
    
    void add(int num) {
        if (num == 0) {
            pref.clear();
            pref.push_back(1);
        } else {
            pref.push_back(pref.back() * num);
        }
    }
    
    int getProduct(int k) {
        if (k >= (int)pref.size()) return 0;
        long long res = pref.back() / pref[pref.size() - 1 - k];
        return (int)res;
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
```

## Java

```java
class ProductOfNumbers {
    private java.util.ArrayList<Long> prefixProducts;

    public ProductOfNumbers() {
        prefixProducts = new java.util.ArrayList<>();
        prefixProducts.add(1L); // sentinel
    }

    public void add(int num) {
        if (num == 0) {
            prefixProducts.clear();
            prefixProducts.add(1L);
        } else {
            long last = prefixProducts.get(prefixProducts.size() - 1);
            prefixProducts.add(last * num);
        }
    }

    public int getProduct(int k) {
        int size = prefixProducts.size() - 1; // number of elements after last zero
        if (k > size) {
            return 0;
        }
        long total = prefixProducts.get(size);
        long prev = prefixProducts.get(size - k);
        return (int)(total / prev);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
```

## Python

```python
class ProductOfNumbers(object):
    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k-1]
```

## Python3

```python
class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]
```

## C

```c
typedef <stddef.h>
#include <stdlib.h>

typedef struct {
    long long *pref;
    int cnt;   // number of elements after the last zero
    int cap;   // capacity of pref array
} ProductOfNumbers;

ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj = (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));
    if (!obj) return NULL;
    obj->cap = 128;
    obj->pref = (long long*)malloc(obj->cap * sizeof(long long));
    obj->pref[0] = 1LL;
    obj->cnt = 0;
    return obj;
}

static void ensureCapacity(ProductOfNumbers* obj, int needed) {
    if (needed <= obj->cap) return;
    while (obj->cap < needed) obj->cap <<= 1;
    obj->pref = (long long*)realloc(obj->pref, obj->cap * sizeof(long long));
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (num == 0) {
        obj->cnt = 0;
        obj->pref[0] = 1LL;
        return;
    }
    ensureCapacity(obj, obj->cnt + 2);
    obj->pref[obj->cnt + 1] = obj->pref[obj->cnt] * (long long)num;
    obj->cnt += 1;
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    if (k > obj->cnt) return 0;
    long long res = obj->pref[obj->cnt] / obj->pref[obj->cnt - k];
    return (int)res;
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    if (!obj) return;
    free(obj->pref);
    free(obj);
}
```

## Csharp

```csharp
public class ProductOfNumbers {
    private readonly System.Collections.Generic.List<long> _prefix;

    public ProductOfNumbers() {
        _prefix = new System.Collections.Generic.List<long>();
        _prefix.Add(1); // sentinel for easier calculations
    }
    
    public void Add(int num) {
        if (num == 0) {
            _prefix.Clear();
            _prefix.Add(1);
        } else {
            long last = _prefix[_prefix.Count - 1];
            _prefix.Add(last * num);
        }
    }
    
    public int GetProduct(int k) {
        int size = _prefix.Count - 1; // number of elements after the last zero
        if (k > size) return 0;
        long result = _prefix[size] / _prefix[size - k];
        return (int)result;
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.Add(num);
 * int param_2 = obj.GetProduct(k);
 */
```

## Javascript

```javascript
var ProductOfNumbers = function() {
    this.prefix = [1];
};

ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) {
        this.prefix = [1];
    } else {
        const last = this.prefix[this.prefix.length - 1];
        this.prefix.push(last * num);
    }
};

ProductOfNumbers.prototype.getProduct = function(k) {
    if (k >= this.prefix.length) return 0;
    const n = this.prefix.length - 1;
    return this.prefix[n] / this.prefix[n - k];
};
```

## Typescript

```typescript
class ProductOfNumbers {
    private prefix: number[];

    constructor() {
        this.prefix = [1];
    }

    add(num: number): void {
        if (num === 0) {
            this.prefix = [1];
        } else {
            const last = this.prefix[this.prefix.length - 1];
            this.prefix.push(last * num);
        }
    }

    getProduct(k: number): number {
        const n = this.prefix.length;
        if (k >= n) return 0;
        const total = this.prefix[n - 1];
        const prev = this.prefix[n - k - 1];
        return Math.trunc(total / prev);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
```

## Php

```php
class ProductOfNumbers {
    /**
     * @var array<int>
     */
    private $prefix;

    public function __construct() {
        // Initialize with 1 to simplify product calculations
        $this->prefix = [1];
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    public function add($num) {
        if ($num == 0) {
            // Reset on zero
            $this->prefix = [1];
        } else {
            $last = end($this->prefix);
            $this->prefix[] = $last * $num;
        }
    }

    /**
     * @param Integer $k
     * @return Integer
     */
    public function getProduct($k) {
        $size = count($this->prefix) - 1; // exclude the initial 1
        if ($k > $size) {
            return 0;
        }
        $last = $this->prefix[$size];
        $prev = $this->prefix[$size - $k];
        return (int)($last / $prev);
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * $obj = new ProductOfNumbers();
 * $obj->add($num);
 * $ret_2 = $obj->getProduct($k);
 */
```

## Swift

```swift
class ProductOfNumbers {
    private var prefix: [Int] = [1]

    init() { }

    func add(_ num: Int) {
        if num == 0 {
            prefix = [1]
        } else {
            let last = prefix.last!
            prefix.append(last * num)
        }
    }

    func getProduct(_ k: Int) -> Int {
        if k >= prefix.count {
            return 0
        }
        let n = prefix.count - 1
        return prefix[n] / prefix[n - k]
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers()
 * obj.add(num)
 * let ret_2: Int = obj.getProduct(k)
 */
```

## Kotlin

```kotlin
class ProductOfNumbers() {
    private val prefix = mutableListOf<Long>(1L)

    fun add(num: Int) {
        if (num == 0) {
            prefix.clear()
            prefix.add(1L)
        } else {
            prefix.add(prefix.last() * num)
        }
    }

    fun getProduct(k: Int): Int {
        if (k >= prefix.size) return 0
        val result = prefix[prefix.size - 1] / prefix[prefix.size - 1 - k]
        return result.toInt()
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
```

## Dart

```dart
class ProductOfNumbers {
  List<int> _prefix;

  ProductOfNumbers() : _prefix = [1];

  void add(int num) {
    if (num == 0) {
      _prefix = [1];
    } else {
      _prefix.add(_prefix.last * num);
    }
  }

  int getProduct(int k) {
    if (k >= _prefix.length) return 0;
    return _prefix.last ~/ _prefix[_prefix.length - 1 - k];
  }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = ProductOfNumbers();
 * obj.add(num);
 * int param2 = obj.getProduct(k);
 */
```

## Golang

```go
type ProductOfNumbers struct {
	pref []int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{pref: []int{1}}
}

func (this *ProductOfNumbers) Add(num int) {
	if num == 0 {
		this.pref = []int{1}
	} else {
		last := this.pref[len(this.pref)-1]
		this.pref = append(this.pref, last*num)
	}
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	size := len(this.pref) - 1
	if k > size {
		return 0
	}
	return this.pref[size] / this.pref[size-k]
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */
```

## Ruby

```ruby
class ProductOfNumbers
  def initialize()
    @prefix = [1]
  end

=begin
  :type num: Integer
  :rtype: Void
=end
  def add(num)
    if num == 0
      @prefix = [1]
    else
      @prefix << @prefix[-1] * num
    end
  end

=begin
  :type k: Integer
  :rtype: Integer
=end
  def get_product(k)
    return 0 if k >= @prefix.length
    @prefix[-1] / @prefix[-k-1]
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

class ProductOfNumbers() {
  private val prefix = ArrayBuffer[Long](1L)

  def add(num: Int): Unit = {
    if (num == 0) {
      prefix.clear()
      prefix += 1L
    } else {
      prefix += prefix.last * num.toLong
    }
  }

  def getProduct(k: Int): Int = {
    if (k >= prefix.size) 0
    else {
      val prod = prefix(prefix.size - 1) / prefix(prefix.size - 1 - k)
      prod.toInt
    }
  }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * val obj = new ProductOfNumbers()
 * obj.add(num)
 * val param_2 = obj.getProduct(k)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct ProductOfNumbers {
    prefix: RefCell<Vec<i64>>,
}

impl ProductOfNumbers {
    fn new() -> Self {
        Self {
            prefix: RefCell::new(vec![1]),
        }
    }

    fn add(&self, num: i32) {
        if num == 0 {
            *self.prefix.borrow_mut() = vec![1];
        } else {
            let mut pref = self.prefix.borrow_mut();
            let last = *pref.last().unwrap();
            pref.push(last * num as i64);
        }
    }

    fn get_product(&self, k: i32) -> i32 {
        let pref = self.prefix.borrow();
        let total = pref.len() - 1; // exclude the initial dummy 1
        if (k as usize) > total {
            0
        } else {
            let res = pref[total] / pref[total - k as usize];
            res as i32
        }
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */
```

## Racket

```racket
(define product-of-numbers%
  (class object%
    (super-new)
    (init-field)

    (define max-capacity 40005)
    (define prefix (make-vector max-capacity 1))
    (define size 0)

    (define/public (add num)
      (if (= num 0)
          (set! size 0)
          (let ([new (* (vector-ref prefix size) num)])
            (set! size (+ size 1))
            (vector-set! prefix size new))))

    (define/public (get-product k)
      (if (> k size)
          0
          (let* ([numerator (vector-ref prefix size)]
                 [denominator (vector-ref prefix (- size k))])
            (quotient numerator denominator))))))
```

## Erlang

```erlang
-module(product_of_numbers).
-export([product_of_numbers_init_/0,
         product_of_numbers_add/1,
         product_of_numbers_get_product/1]).

%% Initialize the data structures.
product_of_numbers_init_() ->
    case ets:info(product_of_numbers_table) of
        undefined -> ok;
        _ -> ets:delete(product_of_numbers_table)
    end,
    Table = ets:new(product_of_numbers_table, [named_table, public]),
    put(product_of_numbers_state, {Table, 0}),
    ok.

%% Add a number to the stream.
product_of_numbers_add(Num) ->
    {Table, Size} = get(product_of_numbers_state),
    case Num of
        0 ->
            ets:delete_all_objects(Table),
            put(product_of_numbers_state, {Table, 0});
        _ ->
            PrevProd =
                case Size of
                    0 -> 1;
                    _ ->
                        [{_, P}] = ets:lookup(Table, Size),
                        P
                end,
            NewProd = PrevProd * Num,
            NewSize = Size + 1,
            ets:insert(Table, {NewSize, NewProd}),
            put(product_of_numbers_state, {Table, NewSize})
    end.

%% Get the product of the last K numbers.
product_of_numbers_get_product(K) ->
    {Table, Size} = get(product_of_numbers_state),
    if
        K > Size -> 0;
        true ->
            [{_, ProdSize}] = ets:lookup(Table, Size),
            Index = Size - K,
            ProdPrev =
                case Index of
                    0 -> 1;
                    _ ->
                        [{_, P}] = ets:lookup(Table, Index),
                        P
                end,
            ProdSize div ProdPrev
    end.
```

## Elixir

```elixir
defmodule ProductOfNumbers do
  @spec init_() :: any
  def init_() do
    Process.put(:prefix, %{0 => 1})
    Process.put(:size, 0)
  end

  @spec add(num :: integer) :: any
  def add(num) do
    if num == 0 do
      Process.put(:prefix, %{0 => 1})
      Process.put(:size, 0)
    else
      size = Process.get(:size)
      prefix = Process.get(:prefix)
      prev_prod = Map.fetch!(prefix, size)
      new_prod = prev_prod * num
      Process.put(:prefix, Map.put(prefix, size + 1, new_prod))
      Process.put(:size, size + 1)
    end
  end

  @spec get_product(k :: integer) :: integer
  def get_product(k) do
    size = Process.get(:size)
    if k > size do
      0
    else
      prefix = Process.get(:prefix)
      prod = Map.fetch!(prefix, size)
      prev = Map.fetch!(prefix, size - k)
      div(prod, prev)
    end
  end
end
```
