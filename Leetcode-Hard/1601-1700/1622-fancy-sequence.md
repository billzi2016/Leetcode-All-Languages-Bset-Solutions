# 1622. Fancy Sequence

## Cpp

```cpp
class Fancy {
    static const long long MOD = 1000000007LL;
    std::vector<long long> base;
    long long mul = 1, add = 0;
    
    long long modpow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
public:
    Fancy() {}
    
    void append(int val) {
        long long v = val % MOD;
        long long invMul = modpow(mul, MOD - 2);
        long long b = (v - add + MOD) % MOD;
        b = b * invMul % MOD;
        base.push_back(b);
    }
    
    void addAll(int inc) {
        add = (add + inc) % MOD;
    }
    
    void multAll(int m) {
        mul = mul * m % MOD;
        add = add * m % MOD;
    }
    
    int getIndex(int idx) {
        if (idx < 0 || idx >= (int)base.size()) return -1;
        long long res = (base[idx] * mul + add) % MOD;
        return (int)res;
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */
```

## Java

```java
class Fancy {
    private static final long MOD = 1_000_000_007L;
    private long mul; // current multiplier a
    private long add; // current addition b
    private java.util.ArrayList<Long> baseVals;

    public Fancy() {
        this.mul = 1L;
        this.add = 0L;
        this.baseVals = new java.util.ArrayList<>();
    }

    public void append(int val) {
        long v = ((val - add) % MOD + MOD) % MOD;
        long invMul = modPow(mul, MOD - 2);
        long base = (v * invMul) % MOD;
        baseVals.add(base);
    }

    public void addAll(int inc) {
        add = (add + inc) % MOD;
    }

    public void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }

    public int getIndex(int idx) {
        if (idx < 0 || idx >= baseVals.size()) return -1;
        long base = baseVals.get(idx);
        long res = (mul * base + add) % MOD;
        return (int) res;
    }

    private static long modPow(long a, long e) {
        long result = 1L;
        long base = a % MOD;
        while (e > 0) {
            if ((e & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            e >>= 1;
        }
        return result;
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.append(val);
 * obj.addAll(inc);
 * obj.multAll(m);
 * int param_4 = obj.getIndex(idx);
 */
```

## Python

```python
class Fancy(object):
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.base = []          # stored values before global transformation
        self.mul = 1            # cumulative multiplier
        self.add = 0            # cumulative addition

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Adjust the incoming value to undo current global operations
        adjusted = (val - self.add) % self.MOD
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        base_val = adjusted * inv_mul % self.MOD
        self.base.append(base_val)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx < 0 or idx >= len(self.base):
            return -1
        return (self.base[idx] * self.mul + self.add) % self.MOD
```

## Python3

```python
class Fancy:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.mul = 1          # cumulative multiplier
        self.add = 0          # cumulative additive offset
        self.arr = []         # stores normalized values

    def append(self, val: int) -> None:
        # Normalize the value to the state before current transformations
        norm = (val - self.add) % self.MOD
        inv_mul = pow(self.mul, self.MOD - 2, self.MOD)
        norm = norm * inv_mul % self.MOD
        self.arr.append(norm)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.arr):
            return -1
        norm = self.arr[idx]
        return (norm * self.mul + self.add) % self.MOD
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

#define MOD 1000000007LL

typedef struct {
    long long *base;
    int size;
    int capacity;
    long long a; // cumulative multiplier
    long long b; // cumulative addition
} Fancy;

static long long modpow(long long x, long long e) {
    long long res = 1 % MOD;
    x %= MOD;
    while (e > 0) {
        if (e & 1) res = (res * x) % MOD;
        x = (x * x) % MOD;
        e >>= 1;
    }
    return res;
}

Fancy* fancyCreate() {
    Fancy* obj = (Fancy*)malloc(sizeof(Fancy));
    obj->capacity = 4;
    obj->size = 0;
    obj->base = (long long*)malloc(obj->capacity * sizeof(long long));
    obj->a = 1;
    obj->b = 0;
    return obj;
}

static void ensureCapacity(Fancy* obj) {
    if (obj->size >= obj->capacity) {
        obj->capacity <<= 1;
        obj->base = (long long*)realloc(obj->base, obj->capacity * sizeof(long long));
    }
}

void fancyAppend(Fancy* obj, int val) {
    ensureCapacity(obj);
    long long curA = obj->a;
    long long curB = obj->b;
    long long invA = modpow(curA, MOD - 2);
    long long adjusted = (val - curB) % MOD;
    if (adjusted < 0) adjusted += MOD;
    adjusted = (adjusted * invA) % MOD;
    obj->base[obj->size++] = adjusted;
}

void fancyAddAll(Fancy* obj, int inc) {
    obj->b = (obj->b + inc) % MOD;
}

void fancyMultAll(Fancy* obj, int m) {
    obj->a = (obj->a * m) % MOD;
    obj->b = (obj->b * m) % MOD;
}

int fancyGetIndex(Fancy* obj, int idx) {
    if (idx < 0 || idx >= obj->size) return -1;
    long long val = (obj->base[idx] * obj->a + obj->b) % MOD;
    return (int)val;
}

void fancyFree(Fancy* obj) {
    if (!obj) return;
    free(obj->base);
    free(obj);
}

/**
 * Your Fancy struct will be instantiated and called as such:
 * Fancy* obj = fancyCreate();
 * fancyAppend(obj, val);
 *
 * fancyAddAll(obj, inc);
 *
 * fancyMultAll(obj, m);
 *
 * int param_4 = fancyGetIndex(obj, idx);
 *
 * fancyFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Fancy {
    private const long MOD = 1000000007L;
    private List<long> baseVals;
    private long mul;
    private long add;

    public Fancy() {
        baseVals = new List<long>();
        mul = 1;
        add = 0;
    }
    
    public void Append(int val) {
        long adjusted = (val - add) % MOD;
        if (adjusted < 0) adjusted += MOD;
        adjusted = adjusted * ModInv(mul) % MOD;
        baseVals.Add(adjusted);
    }
    
    public void AddAll(int inc) {
        add = (add + inc) % MOD;
    }
    
    public void MultAll(int m) {
        mul = mul * m % MOD;
        add = add * m % MOD;
    }
    
    public int GetIndex(int idx) {
        if (idx < 0 || idx >= baseVals.Count) return -1;
        long res = (baseVals[idx] * mul % MOD + add) % MOD;
        return (int)res;
    }

    private static long ModInv(long x) {
        return ModPow(x, MOD - 2);
    }

    private static long ModPow(long a, long e) {
        long result = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) {
                result = result * a % MOD;
            }
            a = a * a % MOD;
            e >>= 1;
        }
        return result;
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * int param_4 = obj.GetIndex(idx);
 */
```

## Javascript

```javascript
var Fancy = function() {
    this.MOD = 1000000007n;
    this.arr = [];               // store base values
    this.mul = 1n;                // cumulative multiplier
    this.add = 0n;                // cumulative addition
    this.invMul = 1n;             // modular inverse of mul
};

Fancy.prototype._modPow = function(base, exp) {
    let mod = this.MOD;
    base %= mod;
    let result = 1n;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1n;
    }
    return result;
};

Fancy.prototype._modInv = function(x) {
    // MOD is prime
    return this._modPow(x, this.MOD - 2n);
};

/** 
 * @param {number} val
 * @return {void}
 */
Fancy.prototype.append = function(val) {
    const v = BigInt(val);
    const mod = this.MOD;
    // base = (v - add) * invMul mod MOD
    let base = (v - this.add) % mod;
    if (base < 0n) base += mod;
    base = (base * this.invMul) % mod;
    this.arr.push(base);
};

/** 
 * @param {number} inc
 * @return {void}
 */
Fancy.prototype.addAll = function(inc) {
    const mod = this.MOD;
    this.add = (this.add + BigInt(inc)) % mod;
};

/** 
 * @param {number} m
 * @return {void}
 */
Fancy.prototype.multAll = function(m) {
    const mod = this.MOD;
    const mm = BigInt(m);
    this.mul = (this.mul * mm) % mod;
    this.add = (this.add * mm) % mod;
    // update inverse multiplier
    const invM = this._modInv(mm);
    this.invMul = (this.invMul * invM) % mod;
};

/** 
 * @param {number} idx
 * @return {number}
 */
Fancy.prototype.getIndex = function(idx) {
    if (idx < 0 || idx >= this.arr.length) return -1;
    const mod = this.MOD;
    let val = (this.arr[idx] * this.mul + this.add) % mod;
    return Number(val);
};
```

## Typescript

```typescript
class Fancy {
    private readonly MOD = 1000000007;
    private arr: number[] = [];
    private curMul: number = 1;
    private inc: number = 0;

    constructor() {}

    append(val: number): void {
        const adjusted = ((val - this.inc + this.MOD) % this.MOD) * this.modInv(this.curMul) % this.MOD;
        this.arr.push(adjusted);
    }

    addAll(inc: number): void {
        this.inc = (this.inc + inc) % this.MOD;
    }

    multAll(m: number): void {
        this.curMul = this.curMul * m % this.MOD;
        this.inc = this.inc * m % this.MOD;
    }

    getIndex(idx: number): number {
        if (idx < 0 || idx >= this.arr.length) return -1;
        return (this.arr[idx] * this.curMul + this.inc) % this.MOD;
    }

    private modInv(x: number): number {
        let a = x, b = this.MOD - 2;
        let res = 1;
        while (b > 0) {
            if (b & 1) res = res * a % this.MOD;
            a = a * a % this.MOD;
            b >>= 1;
        }
        return res;
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * var obj = new Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */
```

## Php

```php
class Fancy {
    const MOD = 1000000007;
    private $vals = [];
    private $mul = 1;
    private $add = 0;

    function __construct() {
        
    }

    function append($val) {
        $mod = self::MOD;
        $norm = ($val - $this->add) % $mod;
        if ($norm < 0) $norm += $mod;
        $invMul = $this->modInv($this->mul);
        $norm = ($norm * $invMul) % $mod;
        $this->vals[] = $norm;
    }

    function addAll($inc) {
        $mod = self::MOD;
        $this->add = ($this->add + $inc) % $mod;
    }

    function multAll($m) {
        $mod = self::MOD;
        $this->mul = ($this->mul * $m) % $mod;
        $this->add = ($this->add * $m) % $mod;
    }

    function getIndex($idx) {
        if ($idx < 0 || $idx >= count($this->vals)) return -1;
        $mod = self::MOD;
        $norm = $this->vals[$idx];
        $res = ($norm * $this->mul + $this->add) % $mod;
        return $res;
    }

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }

    private function modInv($a) {
        return $this->modPow($a, self::MOD - 2);
    }
}
```

## Swift

```swift
class Fancy {
    private let MOD: Int64 = 1_000_000_007
    private var mul: Int64 = 1
    private var add: Int64 = 0
    private var bases: [Int64] = []
    
    init() { }
    
    func append(_ val: Int) {
        let v = ( (Int64(val) % MOD) - add + MOD ) % MOD
        let invMul = modPow(mul, MOD - 2)
        let base = (v * invMul) % MOD
        bases.append(base)
    }
    
    func addAll(_ inc: Int) {
        add = (add + Int64(inc)) % MOD
    }
    
    func multAll(_ m: Int) {
        mul = (mul * Int64(m)) % MOD
        add = (add * Int64(m)) % MOD
    }
    
    func getIndex(_ idx: Int) -> Int {
        if idx < 0 || idx >= bases.count {
            return -1
        }
        let base = bases[idx]
        let res = ( (mul * base) % MOD + add ) % MOD
        return Int(res)
    }
    
    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let obj = Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * let ret_4: Int = obj.getIndex(idx)
 */
```

## Kotlin

```kotlin
class Fancy() {
    private val MOD = 1_000_000_007L
    private var mul = 1L
    private var add = 0L
    private val stored = ArrayList<Long>()

    fun append(`val`: Int) {
        var v = `val`.toLong()
        var diff = (v - add) % MOD
        if (diff < 0) diff += MOD
        val invMul = modInv(mul)
        val base = diff * invMul % MOD
        stored.add(base)
    }

    fun addAll(inc: Int) {
        add = (add + inc) % MOD
    }

    fun multAll(m: Int) {
        mul = mul * m % MOD
        add = add * m % MOD
    }

    fun getIndex(idx: Int): Int {
        if (idx < 0 || idx >= stored.size) return -1
        val base = stored[idx]
        var res = base * mul % MOD
        res = (res + add) % MOD
        return res.toInt()
    }

    private fun modInv(x: Long): Long {
        return powMod(x, MOD - 2)
    }

    private fun powMod(a: Long, e: Long): Long {
        var base = a % MOD
        var exp = e
        var result = 1L
        while (exp > 0) {
            if ((exp and 1L) == 1L) {
                result = result * base % MOD
            }
            base = base * base % MOD
            exp = exp shr 1
        }
        return result
    }
}
```

## Dart

```dart
class Fancy {
  static const int _mod = 1000000007;
  int _aCur = 1; // cumulative multiplier
  int _bCur = 0; // cumulative addition
  final List<int> _vals = [];
  final List<int> _aSnap = [];
  final List<int> _bSnap = [];

  Fancy() {
    // initialization already done above
  }

  void append(int val) {
    _vals.add(val % _mod);
    _aSnap.add(_aCur);
    _bSnap.add(_bCur);
  }

  void addAll(int inc) {
    _bCur = (_bCur + inc) % _mod;
  }

  void multAll(int m) {
    _aCur = (_aCur * m) % _mod;
    _bCur = (_bCur * m) % _mod;
  }

  int getIndex(int idx) {
    if (idx < 0 || idx >= _vals.length) return -1;
    int v = _vals[idx];
    int aIns = _aSnap[idx];
    int bIns = _bSnap[idx];

    int invAIns = _modPow(aIns, _mod - 2);
    int aFuture = (_aCur * invAIns) % _mod;
    int bFuture = (_bCur - (aFuture * bIns) % _mod + _mod) % _mod;

    return ((aFuture * v) % _mod + bFuture) % _mod;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = Fancy();
 * obj.append(val);
 * obj.addAll(inc);
 * obj.multAll(m);
 * int param4 = obj.getIndex(idx);
 */
```

## Golang

```go
type Fancy struct {
	vals []int64
	mul  int64
	add  int64
}

const mod = 1000000007

func Constructor() Fancy {
	return Fancy{
		vals: make([]int64, 0),
		mul:  1,
		add:  0,
	}
}

func (f *Fancy) Append(val int) {
	invMul := modInv(f.mul)
	base := ((int64(val)%mod - f.add + mod) % mod) * invMul % mod
	f.vals = append(f.vals, base)
}

func (f *Fancy) AddAll(inc int) {
	f.add = (f.add + int64(inc)) % mod
}

func (f *Fancy) MultAll(m int) {
	f.mul = f.mul * int64(m) % mod
	f.add = f.add * int64(m) % mod
}

func (f *Fancy) GetIndex(idx int) int {
	if idx < 0 || idx >= len(f.vals) {
		return -1
	}
	res := (f.mul*f.vals[idx] + f.add) % mod
	return int(res)
}

func modInv(a int64) int64 {
	return powMod(a, mod-2)
}

func powMod(a, e int64) int64 {
	result := int64(1)
	base := a % mod
	for e > 0 {
		if e&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		e >>= 1
	}
	return result
}
```

## Ruby

```ruby
class Fancy
  MOD = 1_000_000_007

  def initialize()
    @arr = []
    @a = 1
    @b = 0
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def append(val)
    inv_a = mod_inv(@a)
    s = (val - @b) % MOD
    s = (s * inv_a) % MOD
    @arr << s
  end

=begin
    :type inc: Integer
    :rtype: Void
=end
  def add_all(inc)
    @b = (@b + inc) % MOD
  end

=begin
    :type m: Integer
    :rtype: Void
=end
  def mult_all(m)
    @a = (@a * m) % MOD
    @b = (@b * m) % MOD
  end

=begin
    :type idx: Integer
    :rtype: Integer
=end
  def get_index(idx)
    return -1 if idx >= @arr.length
    ((@arr[idx] * @a) % MOD + @b) % MOD
  end

  private

  def mod_pow(base, exp)
    result = 1
    b = base % MOD
    e = exp
    while e > 0
      result = (result * b) % MOD if (e & 1) == 1
      b = (b * b) % MOD
      e >>= 1
    end
    result
  end

  def mod_inv(x)
    mod_pow(x, MOD - 2)
  end
end
```

## Scala

```scala
class Fancy() {
  private val MOD = 1000000007L
  private var mul: Long = 1L
  private var add: Long = 0L
  private val base = scala.collection.mutable.ArrayBuffer[Long]()

  private def modPow(a: Long, e: Long): Long = {
    var res = 1L
    var b = a % MOD
    var exp = e
    while (exp > 0) {
      if ((exp & 1L) == 1L) res = (res * b) % MOD
      b = (b * b) % MOD
      exp >>= 1
    }
    res
  }

  private def modInv(a: Long): Long = modPow(a, MOD - 2)

  def append(`val`: Int): Unit = {
    val v = `val`.toLong
    var adjusted = (v - add) % MOD
    if (adjusted < 0) adjusted += MOD
    val invMul = modInv(mul)
    val stored = (adjusted * invMul) % MOD
    base.append(stored)
  }

  def addAll(inc: Int): Unit = {
    add = (add + inc) % MOD
  }

  def multAll(m: Int): Unit = {
    mul = (mul * m) % MOD
    add = (add * m) % MOD
  }

  def getIndex(idx: Int): Int = {
    if (idx < 0 || idx >= base.length) return -1
    val stored = base(idx)
    val value = (stored * mul + add) % MOD
    value.toInt
  }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * val obj = new Fancy()
 * obj.append(`val`)
 * obj.addAll(inc)
 * obj.multAll(m)
 * val param_4 = obj.getIndex(idx)
 */
```

## Rust

```rust
use std::vec::Vec;

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res: i64 = 1;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}

fn mod_inv(x: i64) -> i64 {
    // MOD is prime
    mod_pow(x, MOD - 2)
}

struct Fancy {
    vals: Vec<i64>,
    mul_at: Vec<i64>,
    add_at: Vec<i64>,
    cur_mul: i64,
    cur_add: i64,
}

impl Fancy {

    fn new() -> Self {
        Fancy {
            vals: Vec::new(),
            mul_at: Vec::new(),
            add_at: Vec::new(),
            cur_mul: 1,
            cur_add: 0,
        }
    }

    fn append(&mut self, val: i32) {
        let v = ((val as i64) * self.cur_mul % MOD + self.cur_add) % MOD;
        self.vals.push(v);
        self.mul_at.push(self.cur_mul);
        self.add_at.push(self.cur_add);
    }

    fn add_all(&mut self, inc: i32) {
        self.cur_add = (self.cur_add + inc as i64) % MOD;
    }

    fn mult_all(&mut self, m: i32) {
        let mm = m as i64 % MOD;
        self.cur_mul = self.cur_mul * mm % MOD;
        self.cur_add = self.cur_add * mm % MOD;
    }

    fn get_index(&self, idx: i32) -> i32 {
        let i = idx as usize;
        if i >= self.vals.len() {
            return -1;
        }
        let factor = self.cur_mul * mod_inv(self.mul_at[i]) % MOD;
        let mut res = self.vals[i] * factor % MOD;
        let add_part = (self.cur_add - self.add_at[i] * factor % MOD + MOD) % MOD;
        res = (res + add_part) % MOD;
        res as i32
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let mut obj = Fancy::new();
 * obj.append(val);
 * obj.add_all(inc);
 * obj.mult_all(m);
 * let ret_4: i32 = obj.get_index(idx);
 */
```

## Racket

```racket
(define MOD 1000000007)

(define (mod x)
  (let ((r (remainder x MOD)))
    (if (< r 0) (+ r MOD) r)))

(define (pow-mod a e)
  (let loop ((base (mod a)) (exp e) (res 1))
    (if (= exp 0)
        res
        (let ((new-res (if (odd? exp) (mod (* res base)) res)))
          (loop (mod (* base base)) (quotient exp 2) new-res)))))

(define fancy%
  (class object%
    (super-new)

    (define vals (make-vector 1))
    (define sz 0)
    (define mul 1)
    (define add 0)

    (define (ensure-capacity n)
      (when (> n (vector-length vals))
        (let ((newlen (* 2 (max n 1))))
          (let ((newvec (make-vector newlen)))
            (for ([i (in-range sz)])
              (vector-set! newvec i (vector-ref vals i)))
            (set! vals newvec)))))

    ; append : exact-integer? -> void?
    (define/public (append val)
      (let* ((inv-mul (pow-mod mul (- MOD 2)))
             (base (mod (* (mod (- val add)) inv-mul))))
        (ensure-capacity (+ sz 1))
        (vector-set! vals sz base)
        (set! sz (+ sz 1))))

    ; add-all : exact-integer? -> void?
    (define/public (add-all inc)
      (set! add (mod (+ add inc))))

    ; mult-all : exact-integer? -> void?
    (define/public (mult-all m)
      (set! mul (mod (* mul m)))
      (set! add (mod (* add m))))

    ; get-index : exact-integer? -> exact-integer?
    (define/public (get-index idx)
      (if (or (< idx 0) (>= idx sz))
          -1
          (let ((base (vector-ref vals idx)))
            (mod (+ (mod (* base mul)) add)))))
    ))
```

## Erlang

```erlang
-module(fancy).
-export([fancy_init_/0,
         fancy_append/1,
         fancy_add_all/1,
         fancy_mult_all/1,
         fancy_get_index/1]).

-define(MOD, 1000000007).

%% Initialization
fancy_init_() ->
    put(seq_array, array:new()),
    put(seq_len, 0),
    put(mul, 1),
    put(add, 0).

%% Append a value
fancy_append(Val) ->
    Mul = get(mul),
    Add = get(add),
    InvMul = mod_pow(Mul, ?MOD - 2),
    Orig = (( (Val - Add) rem ?MOD + ?MOD) rem ?MOD * InvMul) rem ?MOD,
    Len = get(seq_len),
    Arr = get(seq_array),
    NewArr = array:set(Len, Orig, Arr),
    put(seq_array, NewArr),
    put(seq_len, Len + 1).

%% Add to all elements
fancy_add_all(Inc) ->
    Add = get(add),
    NewAdd = (Add + Inc) rem ?MOD,
    put(add, NewAdd).

%% Multiply all elements
fancy_mult_all(M) ->
    Mul = get(mul),
    Add = get(add),
    NewMul = (Mul * M) rem ?MOD,
    NewAdd = (Add * M) rem ?MOD,
    put(mul, NewMul),
    put(add, NewAdd).

%% Get element at index
fancy_get_index(Idx) ->
    Len = get(seq_len),
    if Idx >= Len -> -1;
       true ->
           Arr = get(seq_array),
           Orig = array:get(Idx, Arr),
           Mul = get(mul),
           Add = get(add),
           ((Orig * Mul) rem ?MOD + Add) rem ?MOD
    end.

%% Modular exponentiation (binary exponentiation)
mod_pow(_Base, 0) -> 1;
mod_pow(Base, Exp) ->
    BaseMod = Base rem ?MOD,
    mod_pow_acc(BaseMod, Exp, 1).

mod_pow_acc(_, 0, Acc) -> Acc;
mod_pow_acc(Base, Exp, Acc) when (Exp band 1) =:= 1 ->
    NewAcc = (Acc * Base) rem ?MOD,
    mod_pow_acc((Base * Base) rem ?MOD, Exp bsr 1, NewAcc);
mod_pow_acc(Base, Exp, Acc) ->
    mod_pow_acc((Base * Base) rem ?MOD, Exp bsr 1, Acc).
```

## Elixir

```elixir
defmodule Fancy do
  @modulus 1_000_000_007

  defp mod_pow(_base, 0), do: 1

  defp mod_pow(base, exp) when exp > 0 do
    base = rem(base, @modulus)

    do_mod_pow(base, exp, 1)
  end

  defp do_mod_pow(_base, 0, acc), do: acc

  defp do_mod_pow(base, exp, acc) do
    acc = if rem(exp, 2) == 1, do: rem(acc * base, @modulus), else: acc
    base = rem(base * base, @modulus)
    exp = div(exp, 2)
    do_mod_pow(base, exp, acc)
  end

  defp mod_inv(x), do: mod_pow(x, @modulus - 2)

  @spec init_() :: any
  def init_() do
    Agent.start_link(
      fn ->
        %{
          vals: %{},
          mul_snap: %{},
          add_snap: %{},
          cur_mul: 1,
          cur_add: 0,
          size: 0
        }
      end,
      name: __MODULE__
    )

    :ok
  end

  @spec append(val :: integer) :: any
  def append(val) do
    Agent.update(__MODULE__, fn state ->
      idx = state.size

      %{
        state
        | vals: Map.put(state.vals, idx, val),
          mul_snap: Map.put(state.mul_snap, idx, state.cur_mul),
          add_snap: Map.put(state.add_snap, idx, state.cur_add),
          size: idx + 1
      }
    end)

    :ok
  end

  @spec add_all(inc :: integer) :: any
  def add_all(inc) do
    Agent.update(__MODULE__, fn state ->
      %{state | cur_add: rem(state.cur_add + inc, @modulus)}
    end)

    :ok
  end

  @spec mult_all(m :: integer) :: any
  def mult_all(m) do
    Agent.update(__MODULE__, fn state ->
      new_mul = rem(state.cur_mul * m, @modulus)
      new_add = rem(state.cur_add * m, @modulus)

      %{state | cur_mul: new_mul, cur_add: new_add}
    end)

    :ok
  end

  @spec get_index(idx :: integer) :: integer
  def get_index(idx) do
    state = Agent.get(__MODULE__, & &1)

    if idx < 0 or idx >= state.size do
      -1
    else
      val = Map.fetch!(state.vals, idx)
      mul_at = Map.fetch!(state.mul_snap, idx)
      add_at = Map.fetch!(state.add_snap, idx)

      inv_mul_at = mod_inv(mul_at)
      factor = rem(state.cur_mul * inv_mul_at, @modulus)

      part1 = rem(val * factor, @modulus)
      part2 = rem(state.cur_add - rem(add_at * factor, @modulus), @modulus)

      res = rem(part1 + part2, @modulus)
      if res < 0, do: res + @modulus, else: res
    end
  end
end
```
