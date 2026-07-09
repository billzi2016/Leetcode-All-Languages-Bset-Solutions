# 1357. Apply Discount Every n Orders

## Cpp

```cpp
class Cashier {
public:
    Cashier(int n, int discount, std::vector<int>& products, std::vector<int>& prices) {
        this->n = n;
        this->discount = discount;
        for (size_t i = 0; i < products.size(); ++i) {
            priceMap[products[i]] = prices[i];
        }
        customerCount = 0;
    }
    
    double getBill(std::vector<int> product, std::vector<int> amount) {
        ++customerCount;
        double total = 0.0;
        for (size_t i = 0; i < product.size(); ++i) {
            total += static_cast<double>(amount[i]) * priceMap[product[i]];
        }
        if (customerCount % n == 0) {
            total = total * (100 - discount) / 100.0;
        }
        return total;
    }
private:
    int n;
    int discount;
    int customerCount;
    std::unordered_map<int, int> priceMap;
};
```

## Java

```java
class Cashier {
    private final int n;
    private final int discount;
    private final int[] priceMap; // index by product id
    private int customerCount;

    public Cashier(int n, int discount, int[] products, int[] prices) {
        this.n = n;
        this.discount = discount;
        this.priceMap = new int[201]; // product ids are <=200
        for (int i = 0; i < products.length; i++) {
            priceMap[products[i]] = prices[i];
        }
        this.customerCount = 0;
    }

    public double getBill(int[] product, int[] amount) {
        customerCount++;
        double total = 0.0;
        for (int i = 0; i < product.length; i++) {
            total += priceMap[product[i]] * (double) amount[i];
        }
        if (customerCount % n == 0) {
            total = total * (100 - discount) / 100.0;
        }
        return total;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.getBill(product,amount);
 */
```

## Python

```python
class Cashier(object):
    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.price_map = dict(zip(products, prices))
        self.cnt = 0

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        total = 0
        for p, a in zip(product, amount):
            total += self.price_map[p] * a
        self.cnt += 1
        if self.cnt % self.n == 0:
            total = total * (100 - self.discount) / 100.0
        return float(total)
```

## Python3

```python
class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.price_map = {p: pr for p, pr in zip(products, prices)}
        self.cnt = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        total = 0
        for pid, qty in zip(product, amount):
            total += self.price_map[pid] * qty
        self.cnt += 1
        if self.cnt % self.n == 0:
            total *= (100 - self.discount) / 100.0
        return float(total)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;
    int discount;
    int cnt;
    double priceMap[201];
} Cashier;

Cashier* cashierCreate(int n, int discount, int* products, int productsSize, int* prices, int pricesSize) {
    Cashier *obj = (Cashier*)malloc(sizeof(Cashier));
    obj->n = n;
    obj->discount = discount;
    obj->cnt = 0;
    for (int i = 0; i <= 200; ++i) obj->priceMap[i] = 0.0;
    for (int i = 0; i < productsSize; ++i) {
        int id = products[i];
        obj->priceMap[id] = (double)prices[i];
    }
    return obj;
}

double cashierGetBill(Cashier* obj, int* product, int productSize, int* amount, int amountSize) {
    double total = 0.0;
    for (int i = 0; i < productSize; ++i) {
        int id = product[i];
        total += (double)amount[i] * obj->priceMap[id];
    }
    obj->cnt++;
    if (obj->cnt % obj->n == 0) {
        total = total * (100 - obj->discount) / 100.0;
    }
    return total;
}

void cashierFree(Cashier* obj) {
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Cashier {
    private readonly int _n;
    private readonly int _discount;
    private readonly Dictionary<int, int> _priceMap;
    private int _customerCount;

    public Cashier(int n, int discount, int[] products, int[] prices) {
        _n = n;
        _discount = discount;
        _priceMap = new Dictionary<int, int>(products.Length);
        for (int i = 0; i < products.Length; i++) {
            _priceMap[products[i]] = prices[i];
        }
        _customerCount = 0;
    }

    public double GetBill(int[] product, int[] amount) {
        double total = 0;
        for (int i = 0; i < product.Length; i++) {
            total += amount[i] * _priceMap[product[i]];
        }
        _customerCount++;
        if (_customerCount % _n == 0) {
            total = total * (100 - _discount) / 100.0;
        }
        return total;
    }
}
```

## Javascript

```javascript
var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discount = discount;
    this.priceMap = new Map();
    for (let i = 0; i < products.length; i++) {
        this.priceMap.set(products[i], prices[i]);
    }
    this.customerCount = 0;
};

Cashier.prototype.getBill = function(product, amount) {
    let total = 0;
    for (let i = 0; i < product.length; i++) {
        total += amount[i] * this.priceMap.get(product[i]);
    }
    this.customerCount++;
    if (this.customerCount % this.n === 0) {
        total = total * (100 - this.discount) / 100;
    }
    return total;
};
```

## Typescript

```typescript
class Cashier {
    private n: number;
    private discount: number;
    private priceMap: Map<number, number>;
    private customerCount: number;

    constructor(n: number, discount: number, products: number[], prices: number[]) {
        this.n = n;
        this.discount = discount;
        this.priceMap = new Map();
        for (let i = 0; i < products.length; i++) {
            this.priceMap.set(products[i], prices[i]);
        }
        this.customerCount = 0;
    }

    getBill(product: number[], amount: number[]): number {
        let total = 0;
        for (let i = 0; i < product.length; i++) {
            const price = this.priceMap.get(product[i]) ?? 0;
            total += price * amount[i];
        }
        this.customerCount++;
        if (this.customerCount % this.n === 0) {
            total = total * (100 - this.discount) / 100;
        }
        return total;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * var obj = new Cashier(n, discount, products, prices)
 * var param_1 = obj.getBill(product,amount)
 */
```

## Php

```php
class Cashier {
    private int $n;
    private int $discount;
    private array $priceMap = [];
    private int $cnt = 0;

    /**
     * @param Integer $n
     * @param Integer $discount
     * @param Integer[] $products
     * @param Integer[] $prices
     */
    function __construct($n, $discount, $products, $prices) {
        $this->n = $n;
        $this->discount = $discount;
        $len = count($products);
        for ($i = 0; $i < $len; $i++) {
            $this->priceMap[$products[$i]] = $prices[$i];
        }
    }

    /**
     * @param Integer[] $product
     * @param Integer[] $amount
     * @return Float
     */
    function getBill($product, $amount) {
        $total = 0;
        $len = count($product);
        for ($i = 0; $i < $len; $i++) {
            $pid = $product[$i];
            $amt = $amount[$i];
            $price = $this->priceMap[$pid] ?? 0;
            $total += $price * $amt;
        }
        $this->cnt++;
        if ($this->cnt % $this->n == 0) {
            $total = $total * (100 - $this->discount) / 100.0;
        }
        return $total;
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * $obj = new Cashier($n, $discount, $products, $prices);
 * $ret_1 = $obj->getBill($product, $amount);
 */
```

## Swift

```swift
class Cashier {
    private let n: Int
    private let discount: Int
    private var priceMap: [Int: Int] = [:]
    private var customerCount: Int = 0

    init(_ n: Int, _ discount: Int, _ products: [Int], _ prices: [Int]) {
        self.n = n
        self.discount = discount
        for (p, pr) in zip(products, prices) {
            priceMap[p] = pr
        }
    }

    func getBill(_ product: [Int], _ amount: [Int]) -> Double {
        var total: Double = 0.0
        for i in 0..<product.count {
            if let price = priceMap[product[i]] {
                total += Double(price * amount[i])
            }
        }
        customerCount += 1
        if customerCount % n == 0 {
            total *= Double(100 - discount) / 100.0
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Cashier(private val n: Int, private val discount: Int, products: IntArray, prices: IntArray) {
    private val priceMap = HashMap<Int, Int>()
    private var count = 0

    init {
        for (i in products.indices) {
            priceMap[products[i]] = prices[i]
        }
    }

    fun getBill(product: IntArray, amount: IntArray): Double {
        var total = 0.0
        for (i in product.indices) {
            val price = priceMap[product[i]] ?: 0
            total += amount[i] * price.toDouble()
        }
        count++
        if (count % n == 0) {
            total = total * (100 - discount) / 100.0
        }
        return total
    }
}
```

## Dart

```dart
class Cashier {
  final int _n;
  final int _discount;
  final Map<int, int> _priceMap = {};
  int _cnt = 0;

  Cashier(int n, int discount, List<int> products, List<int> prices)
      : _n = n,
        _discount = discount {
    for (int i = 0; i < products.length; i++) {
      _priceMap[products[i]] = prices[i];
    }
  }

  double getBill(List<int> product, List<int> amount) {
    double total = 0;
    for (int i = 0; i < product.length; i++) {
      int price = _priceMap[product[i]]!;
      total += price * amount[i];
    }
    _cnt++;
    if (_cnt % _n == 0) {
      total = total * (100 - _discount) / 100;
    }
    return total;
  }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = Cashier(n, discount, products, prices);
 * double param1 = obj.getBill(product,amount);
 */
```

## Golang

```go
type Cashier struct {
	n        int
	discount int
	priceMap map[int]int
	cnt      int
}

func Constructor(n int, discount int, products []int, prices []int) Cashier {
	m := make(map[int]int, len(products))
	for i, p := range products {
		m[p] = prices[i]
	}
	return Cashier{
		n:        n,
		discount: discount,
		priceMap: m,
		cnt:      0,
	}
}

func (this *Cashier) GetBill(product []int, amount []int) float64 {
	total := 0
	for i, pid := range product {
		total += amount[i] * this.priceMap[pid]
	}
	this.cnt++
	if this.cnt%this.n == 0 {
		return float64(total) * float64(100-this.discount) / 100.0
	}
	return float64(total)
}
```

## Ruby

```ruby
class Cashier
  def initialize(n, discount, products, prices)
    @n = n
    @discount = discount
    @price_map = {}
    products.each_with_index { |p, i| @price_map[p] = prices[i] }
    @cnt = 0
  end

  def get_bill(product, amount)
    total = 0.0
    product.each_with_index do |pid, idx|
      total += amount[idx] * @price_map[pid]
    end
    @cnt += 1
    if @cnt % @n == 0
      total *= (100 - @discount) / 100.0
    end
    total
  end
end
```

## Scala

```scala
class Cashier(_n: Int, _discount: Int, _products: Array[Int], _prices: Array[Int]) {
    private val n = _n
    private val discount = _discount
    private val priceMap: Map[Int, Int] = (_products zip _prices).toMap
    private var count = 0

    def getBill(product: Array[Int], amount: Array[Int]): Double = {
        count += 1
        var total = 0.0
        var i = 0
        while (i < product.length) {
            total += priceMap(product(i)).toDouble * amount(i)
            i += 1
        }
        if (count % n == 0) {
            total = total * (100 - discount) / 100.0
        }
        total
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * val obj = new Cashier(n, discount, products, prices)
 * val param_1 = obj.getBill(product,amount)
 */
```

## Rust

```rust
use std::collections::HashMap;
use std::cell::Cell;

struct Cashier {
    n: i32,
    discount: i32,
    price_map: HashMap<i32, i32>,
    cnt: Cell<i32>,
}

impl Cashier {
    fn new(n: i32, discount: i32, products: Vec<i32>, prices: Vec<i32>) -> Self {
        let mut map = HashMap::new();
        for (p, pr) in products.into_iter().zip(prices.into_iter()) {
            map.insert(p, pr);
        }
        Cashier {
            n,
            discount,
            price_map: map,
            cnt: Cell::new(0),
        }
    }

    fn get_bill(&self, product: Vec<i32>, amount: Vec<i32>) -> f64 {
        let mut sum: i64 = 0;
        for (p, a) in product.iter().zip(amount.iter()) {
            if let Some(price) = self.price_map.get(p) {
                sum += (*price as i64) * (*a as i64);
            }
        }
        let cur = self.cnt.get() + 1;
        self.cnt.set(cur);
        let mut total = sum as f64;
        if cur % self.n == 0 {
            total = total * (100 - self.discount) as f64 / 100.0;
        }
        total
    }
}
```

## Racket

```racket
(define cashier%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; discount : exact-integer?
    ; products : (listof exact-integer?)
    ; prices : (listof exact-integer?)
    (init-field
      n
      discount
      products
      prices)
    
    ; private mutable counter
    (define cnt 0)
    
    ; map product id -> price
    (define price-hash (make-hash))
    (for ([p products] [pr prices])
      (hash-set! price-hash p pr))
    
    ; get-bill : (listof exact-integer?) (listof exact-integer?) -> flonum?
    (define/public (get-bill product amount)
      (set! cnt (+ cnt 1))
      (define total
        (let loop ((ps product) (as amount) (sum 0))
          (if (null? ps)
              sum
              (let* ([pid (car ps)]
                     [amt (car as)]
                     [price (hash-ref price-hash pid)])
                (loop (cdr ps) (cdr as) (+ sum (* amt price)))))))
      (define factor (/ (- 100 discount) 100.0))
      (if (= (remainder cnt n) 0)
          (* total factor)
          (exact->inexact total)))))
```

## Erlang

```erlang
-spec cashier_init_(N :: integer(), Discount :: integer(), Products :: [integer()], Prices :: [integer()]) -> any().
cashier_init_(N, Discount, Products, Prices) ->
    PriceMap = maps:from_list(lists:zip(Products, Prices)),
    State = #{n => N, discount => Discount, price_map => PriceMap, count => 0},
    put(cashier_state, State).

-spec cashier_get_bill(Product :: [integer()], Amount :: [integer()]) -> float().
cashier_get_bill(Product, Amount) ->
    State = get(cashier_state),
    PriceMap = maps:get(price_map, State),
    Subtotal = lists:foldl(
        fun({P, A}, Acc) ->
            Price = maps:get(P, PriceMap),
            Acc + Price * A
        end,
        0,
        lists:zip(Product, Amount)
    ),
    Count1 = maps:get(count, State) + 1,
    N = maps:get(n, State),
    Discount = maps:get(discount, State),
    Bill =
        if
            Count1 rem N == 0 ->
                Subtotal * (100 - Discount) / 100.0;
            true ->
                Subtotal * 1.0
        end,
    NewState = State#{count => Count1},
    put(cashier_state, NewState),
    Bill.
```

## Elixir

```elixir
defmodule Cashier do
  @spec init_(n :: integer, discount :: integer, products :: [integer], prices :: [integer]) :: any
  def init_(n, discount, products, prices) do
    price_map = Enum.zip(products, prices) |> Map.new()
    Process.put(:cashier_state, %{n: n, discount: discount, map: price_map, cnt: 0})
  end

  @spec get_bill(product :: [integer], amount :: [integer]) :: float
  def get_bill(product, amount) do
    state = Process.get(:cashier_state)

    subtotal =
      Enum.zip(product, amount)
      |> Enum.reduce(0, fn {p, a}, acc ->
        price = Map.fetch!(state.map, p)
        acc + price * a
      end)

    cnt = state.cnt + 1

    total =
      if rem(cnt, state.n) == 0 do
        subtotal * (100 - state.discount) / 100.0
      else
        subtotal * 1.0
      end

    Process.put(:cashier_state, %{state | cnt: cnt})
    total
  end
end
```
