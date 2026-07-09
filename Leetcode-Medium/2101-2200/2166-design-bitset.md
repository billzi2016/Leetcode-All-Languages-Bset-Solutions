# 2166. Design Bitset

## Cpp

```cpp
class Bitset {
public:
    Bitset(int size) : n(size), flipped(false), cntOnes(0), bits(size, 0) {}
    
    void fix(int idx) {
        char desiredStored = flipped ? 0 : 1;
        if (bits[idx] != desiredStored) {
            // previous logical value
            int prevLogical = bits[idx] ^ flipped;
            // new logical is 1
            cntOnes += (prevLogical == 0);
            bits[idx] = desiredStored;
        }
    }
    
    void unfix(int idx) {
        char desiredStored = flipped ? 1 : 0;
        if (bits[idx] != desiredStored) {
            int prevLogical = bits[idx] ^ flipped;
            // new logical is 0
            cntOnes -= (prevLogical == 1);
            bits[idx] = desiredStored;
        }
    }
    
    void flip() {
        flipped = !flipped;
        cntOnes = n - cntOnes;
    }
    
    bool all() {
        return cntOnes == n;
    }
    
    bool one() {
        return cntOnes > 0;
    }
    
    int count() {
        return cntOnes;
    }
    
    std::string toString() {
        std::string res;
        res.reserve(n);
        for (int i = 0; i < n; ++i) {
            res.push_back((bits[i] ^ flipped) ? '1' : '0');
        }
        return res;
    }
private:
    int n;
    bool flipped;
    int cntOnes;
    std::vector<char> bits;
};

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset* obj = new Bitset(size);
 * obj->fix(idx);
 * obj->unfix(idx);
 * obj->flip();
 * bool param_4 = obj->all();
 * bool param_5 = obj->one();
 * int param_6 = obj->count();
 * string param_7 = obj->toString();
 */
```

## Java

```java
class Bitset {
    private final int n;
    private final boolean[] bits; // stored values without global flip
    private boolean flipped;
    private int cnt; // number of 1s in the current logical view

    public Bitset(int size) {
        this.n = size;
        this.bits = new boolean[n];
        this.flipped = false;
        this.cnt = 0;
    }

    public void fix(int idx) {
        // If current logical value is 0, change it to 1
        if ((bits[idx] ^ flipped) == false) {
            bits[idx] = !flipped; // set stored value so that after XOR it's 1
            cnt++;
        }
    }

    public void unfix(int idx) {
        // If current logical value is 1, change it to 0
        if ((bits[idx] ^ flipped) == true) {
            bits[idx] = flipped; // set stored value so that after XOR it's 0
            cnt--;
        }
    }

    public void flip() {
        flipped = !flipped;
        cnt = n - cnt;
    }

    public boolean all() {
        return cnt == n;
    }

    public boolean one() {
        return cnt > 0;
    }

    public int count() {
        return cnt;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            sb.append((bits[i] ^ flipped) ? '1' : '0');
        }
        return sb.toString();
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = new Bitset(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * boolean param_4 = obj.all();
 * boolean param_5 = obj.one();
 * int param_6 = obj.count();
 * String param_7 = obj.toString();
 */
```

## Python

```python
class Bitset(object):
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.bits = [0] * size  # stored bits
        self.flipped = False    # logical inversion flag
        self.cnt = 0            # count of logical 1s

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if (self.bits[idx] ^ self.flipped) == 0:
            self.bits[idx] = 1 ^ self.flipped
            self.cnt += 1

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if (self.bits[idx] ^ self.flipped) == 1:
            self.bits[idx] = 0 ^ self.flipped
            self.cnt -= 1

    def flip(self):
        """
        :rtype: None
        """
        self.flipped = not self.flipped
        self.cnt = self.size - self.cnt

    def all(self):
        """
        :rtype: bool
        """
        return self.cnt == self.size

    def one(self):
        """
        :rtype: bool
        """
        return self.cnt > 0

    def count(self):
        """
        :rtype: int
        """
        return self.cnt

    def toString(self):
        """
        :rtype: str
        """
        if not self.flipped:
            return ''.join(str(b) for b in self.bits)
        else:
            # flipped, invert each bit logically
            return ''.join('1' if b == 0 else '0' for b in self.bits)
```

## Python3

```python
class Bitset:
    def __init__(self, size: int):
        self.n = size
        self.bits = [0] * size          # stored bits
        self.flipped = False            # whether view is flipped
        self.cnt = 0                    # number of logical 1s

    def fix(self, idx: int) -> None:
        if (self.bits[idx] ^ self.flipped) == 1:
            return
        self.bits[idx] = 1 ^ self.flipped
        self.cnt += 1

    def unfix(self, idx: int) -> None:
        if (self.bits[idx] ^ self.flipped) == 0:
            return
        self.bits[idx] = 0 ^ self.flipped
        self.cnt -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.cnt = self.n - self.cnt

    def all(self) -> bool:
        return self.cnt == self.n

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return ''.join('1' if (b ^ self.flipped) else '0' for b in self.bits)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int size;
    char *bits;      // stored bits (0 or 1)
    bool flipped;   // logical flip flag
    int cntOnes;     // number of logical 1s
} Bitset;

Bitset* bitsetCreate(int size) {
    Bitset* obj = (Bitset*)malloc(sizeof(Bitset));
    obj->size = size;
    obj->bits = (char*)calloc(size, sizeof(char)); // initialized to 0
    obj->flipped = false;
    obj->cntOnes = 0;
    return obj;
}

static inline bool logicalBit(Bitset* obj, int idx) {
    return (obj->bits[idx] ^ obj->flipped);
}

void bitsetFix(Bitset* obj, int idx) {
    if (!logicalBit(obj, idx)) {               // currently 0
        obj->bits[idx] = obj->flipped ? 0 : 1; // set stored so logical becomes 1
        obj->cntOnes++;
    }
}

void bitsetUnfix(Bitset* obj, int idx) {
    if (logicalBit(obj, idx)) {                // currently 1
        obj->bits[idx] = obj->flipped ? 1 : 0; // set stored so logical becomes 0
        obj->cntOnes--;
    }
}

void bitsetFlip(Bitset* obj) {
    obj->flipped = !obj->flipped;
    obj->cntOnes = obj->size - obj->cntOnes;
}

bool bitsetAll(Bitset* obj) {
    return obj->cntOnes == obj->size;
}

bool bitsetOne(Bitset* obj) {
    return obj->cntOnes > 0;
}

int bitsetCount(Bitset* obj) {
    return obj->cntOnes;
}

char* bitsetToString(Bitset* obj) {
    char *res = (char*)malloc((obj->size + 1) * sizeof(char));
    for (int i = 0; i < obj->size; ++i) {
        res[i] = (obj->bits[i] ^ obj->flipped) ? '1' : '0';
    }
    res[obj->size] = '\0';
    return res;
}

void bitsetFree(Bitset* obj) {
    if (!obj) return;
    free(obj->bits);
    free(obj);
}
```

## Csharp

```csharp
public class Bitset
{
    private readonly bool[] _bits;
    private readonly int _size;
    private int _onesCount;
    private bool _flipped;

    public Bitset(int size)
    {
        _size = size;
        _bits = new bool[size];
        _onesCount = 0;
        _flipped = false;
    }

    public void Fix(int idx)
    {
        if (!_flipped)
        {
            if (!_bits[idx])
            {
                _bits[idx] = true;
                _onesCount++;
            }
        }
        else
        {
            // actual value is !_bits[idx]; need it to be 1 => store false
            if (_bits[idx])
            {
                _bits[idx] = false;
                _onesCount++;
            }
        }
    }

    public void Unfix(int idx)
    {
        if (!_flipped)
        {
            if (_bits[idx])
            {
                _bits[idx] = false;
                _onesCount--;
            }
        }
        else
        {
            // actual value is !_bits[idx]; need it to be 0 => store true
            if (!_bits[idx])
            {
                _bits[idx] = true;
                _onesCount--;
            }
        }
    }

    public void Flip()
    {
        _flipped = !_flipped;
        _onesCount = _size - _onesCount;
    }

    public bool All()
    {
        return _onesCount == _size;
    }

    public bool One()
    {
        return _onesCount > 0;
    }

    public int Count()
    {
        return _onsCount;
    }

    public string ToString()
    {
        char[] result = new char[_size];
        if (!_flipped)
        {
            for (int i = 0; i < _size; i++)
                result[i] = _bits[i] ? '1' : '0';
        }
        else
        {
            for (int i = 0; i < _size; i++)
                result[i] = _bits[i] ? '0' : '1';
        }
        return new string(result);
    }

    private int _onsCount => _onesCount;
}
```

## Javascript

```javascript
var Bitset = function(size) {
    this.size = size;
    this.bits = new Uint8Array(size);
    this.flipped = false;
    this.cnt = 0;
};

Bitset.prototype.fix = function(idx) {
    if (!this.flipped) {
        if (this.bits[idx] === 0) {
            this.bits[idx] = 1;
            this.cnt++;
        }
    } else {
        if (this.bits[idx] === 1) {
            this.bits[idx] = 0;
            this.cnt++;
        }
    }
};

Bitset.prototype.unfix = function(idx) {
    if (!this.flipped) {
        if (this.bits[idx] === 1) {
            this.bits[idx] = 0;
            this.cnt--;
        }
    } else {
        if (this.bits[idx] === 0) {
            this.bits[idx] = 1;
            this.cnt--;
        }
    }
};

Bitset.prototype.flip = function() {
    this.flipped = !this.flipped;
    this.cnt = this.size - this.cnt;
};

Bitset.prototype.all = function() {
    return this.cnt === this.size;
};

Bitset.prototype.one = function() {
    return this.cnt > 0;
};

Bitset.prototype.count = function() {
    return this.cnt;
};

Bitset.prototype.toString = function() {
    const res = new Array(this.size);
    if (!this.flipped) {
        for (let i = 0; i < this.size; i++) {
            res[i] = this.bits[i] ? '1' : '0';
        }
    } else {
        for (let i = 0; i < this.size; i++) {
            res[i] = this.bits[i] ? '0' : '1';
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
class Bitset {
    private n: number;
    private bits: Uint8Array;
    private flipped: boolean;
    private cntOnes: number;

    constructor(size: number) {
        this.n = size;
        this.bits = new Uint8Array(size); // all zeros
        this.flipped = false;
        this.cntOnes = 0;
    }

    fix(idx: number): void {
        const actual = this.bits[idx] ^ (this.flipped ? 1 : 0);
        if (actual === 0) {
            this.bits[idx] = this.flipped ? 0 : 1;
            this.cntOnes++;
        }
    }

    unfix(idx: number): void {
        const actual = this.bits[idx] ^ (this.flipped ? 1 : 0);
        if (actual === 1) {
            this.bits[idx] = this.flipped ? 1 : 0;
            this.cntOnes--;
        }
    }

    flip(): void {
        this.flipped = !this.flipped;
        this.cntOnes = this.n - this.cntOnes;
    }

    all(): boolean {
        return this.cntOnes === this.n;
    }

    one(): boolean {
        return this.cntOnes > 0;
    }

    count(): number {
        return this.cntOnes;
    }

    toString(): string {
        const result: string[] = new Array(this.n);
        const flipVal = this.flipped ? 1 : 0;
        for (let i = 0; i < this.n; i++) {
            const val = this.bits[i] ^ flipVal;
            result[i] = val ? '1' : '0';
        }
        return result.join('');
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * var obj = new Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * var param_4 = obj.all()
 * var param_5 = obj.one()
 * var param_6 = obj.count()
 * var param_7 = obj.toString()
 */
```

## Php

```php
class Bitset {
    private int $size;
    private array $bits;
    private int $cnt = 0;
    private bool $flipped = false;

    /**
     * @param Integer $size
     */
    function __construct($size) {
        $this->size = $size;
        $this->bits = array_fill(0, $size, 0);
        $this->cnt = 0;
        $this->flipped = false;
    }

    /**
     * @param Integer $idx
     * @return NULL
     */
    function fix($idx) {
        $flipBit = $this->flipped ? 1 : 0;
        $current = $this->bits[$idx] ^ $flipBit;
        if ($current === 0) {
            // set stored bit so that logical becomes 1
            $this->bits[$idx] = $this->flipped ? 0 : 1;
            $this->cnt++;
        }
    }

    /**
     * @param Integer $idx
     * @return NULL
     */
    function unfix($idx) {
        $flipBit = $this->flipped ? 1 : 0;
        $current = $this->bits[$idx] ^ $flipBit;
        if ($current === 1) {
            // set stored bit so that logical becomes 0
            $this->bits[$idx] = $this->flipped ? 1 : 0;
            $this->cnt--;
        }
    }

    /**
     * @return NULL
     */
    function flip() {
        $this->flipped = !$this->flipped;
        $this->cnt = $this->size - $this->cnt;
    }

    /**
     * @return Boolean
     */
    function all() {
        return $this->cnt === $this->size;
    }

    /**
     * @return Boolean
     */
    function one() {
        return $this->cnt > 0;
    }

    /**
     * @return Integer
     */
    function count() {
        return $this->cnt;
    }

    /**
     * @return String
     */
    function toString() {
        $flipBit = $this->flipped ? 1 : 0;
        $result = '';
        for ($i = 0; $i < $this->size; $i++) {
            $bit = $this->bits[$i] ^ $flipBit;
            $result .= $bit ? '1' : '0';
        }
        return $result;
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * $obj = new Bitset($size);
 * $obj->fix($idx);
 * $obj->unfix($idx);
 * $obj->flip();
 * $ret_4 = $obj->all();
 * $ret_5 = $obj->one();
 * $ret_6 = $obj->count();
 * $ret_7 = $obj->toString();
 */
```

## Swift

```swift
class Bitset {
    private var bits: [Bool]
    private var flipped: Bool
    private var onesCount: Int

    init(_ size: Int) {
        self.bits = Array(repeating: false, count: size)
        self.flipped = false
        self.onesCount = 0
    }
    
    func fix(_ idx: Int) {
        if !flipped {
            if !bits[idx] {
                bits[idx] = true
                onesCount += 1
            }
        } else {
            // logical value is opposite of stored; need logical 1 => store false
            if bits[idx] {
                bits[idx] = false
                onesCount += 1
            }
        }
    }
    
    func unfix(_ idx: Int) {
        if !flipped {
            if bits[idx] {
                bits[idx] = false
                onesCount -= 1
            }
        } else {
            // logical value is opposite of stored; need logical 0 => store true
            if !bits[idx] {
                bits[idx] = true
                onesCount -= 1
            }
        }
    }
    
    func flip() {
        flipped.toggle()
        onesCount = bits.count - onesCount
    }
    
    func all() -> Bool {
        return onesCount == bits.count
    }
    
    func one() -> Bool {
        return onesCount > 0
    }
    
    func count() -> Int {
        return onesCount
    }
    
    func toString() -> String {
        var chars = [Character]()
        chars.reserveCapacity(bits.count)
        if flipped {
            for b in bits {
                chars.append(b ? "0" : "1")
            }
        } else {
            for b in bits {
                chars.append(b ? "1" : "0")
            }
        }
        return String(chars)
    }
}
```

## Kotlin

```kotlin
class Bitset(size: Int) {
    private val n = size
    private val bits = BooleanArray(n)
    private var flipped = false
    private var onesCount = 0

    fun fix(idx: Int) {
        val actual = if (flipped) !bits[idx] else bits[idx]
        if (!actual) {
            if (flipped) {
                bits[idx] = false
            } else {
                bits[idx] = true
            }
            onesCount++
        }
    }

    fun unfix(idx: Int) {
        val actual = if (flipped) !bits[idx] else bits[idx]
        if (actual) {
            if (flipped) {
                bits[idx] = true
            } else {
                bits[idx] = false
            }
            onesCount--
        }
    }

    fun flip() {
        flipped = !flipped
        onesCount = n - onesCount
    }

    fun all(): Boolean {
        return onesCount == n
    }

    fun one(): Boolean {
        return onesCount > 0
    }

    fun count(): Int {
        return onesCount
    }

    override fun toString(): String {
        val sb = StringBuilder(n)
        for (i in 0 until n) {
            val actual = if (flipped) !bits[i] else bits[i]
            sb.append(if (actual) '1' else '0')
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Bitset {
  late List<int> _bits;
  final int _size;
  bool _flipped = false;
  int _cnt = 0;

  Bitset(int size)
      : _size = size,
        _bits = List.filled(size, 0);

  void fix(int idx) {
    if (!_flipped) {
      if (_bits[idx] == 0) {
        _bits[idx] = 1;
        _cnt++;
      }
    } else {
      // actual value is 1 - _bits[idx]
      if (_bits[idx] == 1) {
        _bits[idx] = 0;
        _cnt++;
      }
    }
  }

  void unfix(int idx) {
    if (!_flipped) {
      if (_bits[idx] == 1) {
        _bits[idx] = 0;
        _cnt--;
      }
    } else {
      // actual value is 1 - _bits[idx]
      if (_bits[idx] == 0) {
        _bits[idx] = 1;
        _cnt--;
      }
    }
  }

  void flip() {
    _flipped = !_flipped;
    _cnt = _size - _cnt;
  }

  bool all() => _cnt == _size;

  bool one() => _cnt > 0;

  int count() => _cnt;

  @override
  String toString() {
    final sb = StringBuffer();
    if (!_flipped) {
      for (var b in _bits) {
        sb.write(b);
      }
    } else {
      for (var b in _bits) {
        sb.write(1 - b);
      }
    }
    return sb.toString();
  }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = Bitset(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * bool param4 = obj.all();
 * bool param5 = obj.one();
 * int param6 = obj.count();
 * String param7 = obj.toString();
 */
```

## Golang

```go
package main

import (
	"strings"
)

type Bitset struct {
	bits    []bool
	flipped bool
	cnt     int
	size    int
}

func Constructor(size int) Bitset {
	return Bitset{
		bits: make([]bool, size),
		size: size,
	}
}

func (this *Bitset) Fix(idx int) {
	if this.flipped {
		if this.bits[idx] { // logical 0, need to become 1
			this.bits[idx] = false
			this.cnt++
		}
	} else {
		if !this.bits[idx] { // logical 0, need to become 1
			this.bits[idx] = true
			this.cnt++
		}
	}
}

func (this *Bitset) Unfix(idx int) {
	if this.flipped {
		if !this.bits[idx] { // logical 1, need to become 0
			this.bits[idx] = true
			this.cnt--
		}
	} else {
		if this.bits[idx] { // logical 1, need to become 0
			this.bits[idx] = false
			this.cnt--
		}
	}
}

func (this *Bitset) Flip() {
	this.flipped = !this.flipped
	this.cnt = this.size - this.cnt
}

func (this *Bitset) All() bool {
	return this.cnt == this.size
}

func (this *Bitset) One() bool {
	return this.cnt > 0
}

func (this *Bitset) Count() int {
	return this.cnt
}

func (this *Bitset) ToString() string {
	var sb strings.Builder
	sb.Grow(this.size)
	if this.flipped {
		for _, b := range this.bits {
			if !b {
				sb.WriteByte('1')
			} else {
				sb.WriteByte('0')
			}
		}
	} else {
		for _, b := range this.bits {
			if b {
				sb.WriteByte('1')
			} else {
				sb.WriteByte('0')
			}
		}
	}
	return sb.String()
}

/**
 * Your Bitset object will be instantiated and called as such:
 * obj := Constructor(size);
 * obj.Fix(idx);
 * obj.Unfix(idx);
 * obj.Flip();
 * param_4 := obj.All();
 * param_5 := obj.One();
 * param_6 := obj.Count();
 * param_7 := obj.ToString();
 */
```

## Ruby

```ruby
class Bitset
  def initialize(size)
    @size = size
    @bits = Array.new(size, 0)
    @flip = false
    @cnt = 0
  end

  def fix(idx)
    cur = @bits[idx] ^ (@flip ? 1 : 0)
    if cur == 0
      @bits[idx] = @flip ? 0 : 1
      @cnt += 1
    end
  end

  def unfix(idx)
    cur = @bits[idx] ^ (@flip ? 1 : 0)
    if cur == 1
      @bits[idx] = @flip ? 1 : 0
      @cnt -= 1
    end
  end

  def flip()
    @flip = !@flip
    @cnt = @size - @cnt
  end

  def all()
    @cnt == @size
  end

  def one()
    @cnt > 0
  end

  def count()
    @cnt
  end

  def to_string()
    if @flip
      @bits.map { |b| (b ^ 1).to_s }.join
    else
      @bits.map { |b| b.to_s }.join
    end
  end
end
```

## Scala

```scala
class Bitset(_size: Int) {
  private val n = _size
  private val bits = new Array[Boolean](n)
  private var flipped = false
  private var onesCount = 0

  def fix(idx: Int): Unit = {
    val logical = if (flipped) !bits(idx) else bits(idx)
    if (!logical) {
      if (flipped) bits(idx) = false else bits(idx) = true
      onesCount += 1
    }
  }

  def unfix(idx: Int): Unit = {
    val logical = if (flipped) !bits(idx) else bits(idx)
    if (logical) {
      if (flipped) bits(idx) = true else bits(idx) = false
      onesCount -= 1
    }
  }

  def flip(): Unit = {
    flipped = !flipped
    onesCount = n - onesCount
  }

  def all(): Boolean = {
    onesCount == n
  }

  def one(): Boolean = {
    onesCount > 0
  }

  def count(): Int = {
    onesCount
  }

  override def toString(): String = {
    val sb = new java.lang.StringBuilder(n)
    var i = 0
    while (i < n) {
      val bit = if (flipped) !bits(i) else bits(i)
      sb.append(if (bit) '1' else '0')
      i += 1
    }
    sb.toString()
  }
}
```

## Rust

```rust
struct Bitset {
    bits: Vec<u8>,
    flipped: bool,
    cnt_one: usize,
    size: usize,
}

impl Bitset {
    fn new(size: i32) -> Self {
        let n = size as usize;
        Bitset {
            bits: vec![0; n],
            flipped: false,
            cnt_one: 0,
            size: n,
        }
    }

    fn fix(&mut self, idx: i32) {
        let i = idx as usize;
        let cur = if self.flipped { self.bits[i] ^ 1 } else { self.bits[i] };
        if cur == 0 {
            if self.flipped {
                self.bits[i] = 0; // logical 1 => stored 0 when flipped
            } else {
                self.bits[i] = 1;
            }
            self.cnt_one += 1;
        }
    }

    fn unfix(&mut self, idx: i32) {
        let i = idx as usize;
        let cur = if self.flipped { self.bits[i] ^ 1 } else { self.bits[i] };
        if cur == 1 {
            if self.flipped {
                self.bits[i] = 1; // logical 0 => stored 1 when flipped
            } else {
                self.bits[i] = 0;
            }
            self.cnt_one -= 1;
        }
    }

    fn flip(&mut self) {
        self.flipped = !self.flipped;
        self.cnt_one = self.size - self.cnt_one;
    }

    fn all(&self) -> bool {
        self.cnt_one == self.size
    }

    fn one(&self) -> bool {
        self.cnt_one > 0
    }

    fn count(&self) -> i32 {
        self.cnt_one as i32
    }

    fn to_string(&self) -> String {
        let mut s = String::with_capacity(self.size);
        for &b in &self.bits {
            let val = if self.flipped { b ^ 1 } else { b };
            s.push(if val == 1 { '1' } else { '0' });
        }
        s
    }
}
```

## Racket

```racket
(define bitset%
  (class object%
    (super-new)
    
    ; size : exact-integer?
    (init-field
      size)
    
    (define arr (make-vector size 0))   ; stored bits (0/1)
    (define flip-flag #f)               ; whether logical view is flipped
    (define cnt 0)                      ; number of logical 1s
    
    ; fix : exact-integer? -> void?
    (define/public (fix idx)
      (let* ((stored (vector-ref arr idx))
             (logical (if flip-flag (= stored 0) (= stored 1))))
        (unless logical
          (vector-set! arr idx (if flip-flag 0 1))
          (set! cnt (+ cnt 1)))))
    
    ; unfix : exact-integer? -> void?
    (define/public (unfix idx)
      (let* ((stored (vector-ref arr idx))
             (logical (if flip-flag (= stored 0) (= stored 1))))
        (when logical
          (vector-set! arr idx (if flip-flag 1 0))
          (set! cnt (- cnt 1)))))
    
    ; flip : -> void?
    (define/public (flip)
      (set! flip-flag (not flip-flag))
      (set! cnt (- size cnt)))
    
    ; all : -> boolean?
    (define/public (all)
      (= cnt size))
    
    ; one : -> boolean?
    (define/public (one)
      (> cnt 0))
    
    ; count : -> exact-integer?
    (define/public (count)
      cnt)
    
    ; to-string : -> string?
    (define/public (to-string)
      (let ((s (make-string size)))
        (for ([i (in-range size)])
          (let* ((stored (vector-ref arr i))
                 (logical (if flip-flag (= stored 0) (= stored 1))))
            (string-set! s i (if logical #\1 #\0))))
        s))))
```

## Erlang

```erlang
-module(solution).
-export([bitset_init_/1,
         bitset_fix/1,
         bitset_unfix/1,
         bitset_flip/0,
         bitset_all/0,
         bitset_one/0,
         bitset_count/0,
         bitset_to_string/0]).

%% Initialize the Bitset with given size.
-spec bitset_init_(Size :: integer()) -> any().
bitset_init_(Size) ->
    put(bitset_size, Size),
    put(bitset_flipped, false),
    put(bitset_set, #{}),
    put(bitset_count, 0).

%% Set bit at index Idx to 1.
-spec bitset_fix(Idx :: integer()) -> any().
bitset_fix(Idx) ->
    Flipped = get(bitset_flipped),
    Set = get(bitset_set),
    Count = get(bitset_count),

    DefaultBit = if Flipped -> 1; true -> 0 end,
    InSet = maps:is_key(Idx, Set),

    Real = case {DefaultBit, InSet} of
               {1, false} -> 1;
               {1, true}  -> 0;
               {0, false} -> 0;
               {0, true}  -> 1
           end,

    if Real == 1 ->
            ok; % already 1
       true ->
            NewSet = case InSet of
                         true -> maps:remove(Idx, Set);
                         false -> Set#{Idx => true}
                     end,
            put(bitset_set, NewSet),
            put(bitset_count, Count + 1)
    end.

%% Set bit at index Idx to 0.
-spec bitset_unfix(Idx :: integer()) -> any().
bitset_unfix(Idx) ->
    Flipped = get(bitset_flipped),
    Set = get(bitset_set),
    Count = get(bitset_count),

    DefaultBit = if Flipped -> 1; true -> 0 end,
    InSet = maps:is_key(Idx, Set),

    Real = case {DefaultBit, InSet} of
               {1, false} -> 1;
               {1, true}  -> 0;
               {0, false} -> 0;
               {0, true}  -> 1
           end,

    if Real == 0 ->
            ok; % already 0
       true ->
            NewSet = case InSet of
                         true -> maps:remove(Idx, Set);
                         false -> Set#{Idx => true}
                     end,
            put(bitset_set, NewSet),
            put(bitset_count, Count - 1)
    end.

%% Flip all bits.
-spec bitset_flip() -> any().
bitset_flip() ->
    Size = get(bitset_size),
    Flipped = get(bitset_flipped),
    Count = get(bitset_count),

    put(bitset_flipped, not Flipped),
    put(bitset_count, Size - Count).

%% Return true if all bits are 1.
-spec bitset_all() -> boolean().
bitset_all() ->
    get(bitset_count) == get(bitset_size).

%% Return true if at least one bit is 1.
-spec bitset_one() -> boolean().
bitset_one() ->
    get(bitset_count) > 0.

%% Return the number of bits set to 1.
-spec bitset_count() -> integer().
bitset_count() ->
    get(bitset_count).

%% Return string representation of the Bitset.
-spec bitset_to_string() -> unicode:unicode_binary().
bitset_to_string() ->
    Size = get(bitset_size),
    Flipped = get(bitset_flipped),
    Set = get(bitset_set),

    DefaultBit = if Flipped -> 1; true -> 0 end,

    Bits = [ case maps:is_key(I, Set) of
                 true ->
                     if DefaultBit == 1 -> $0; true -> $1 end;
                 false ->
                     if DefaultBit == 1 -> $1; true -> $0 end
             end || I <- lists:seq(0, Size - 1)],

    list_to_binary(Bits).
```

## Elixir

```elixir
defmodule Bitset do
  @spec init_(size :: integer) :: :ok
  def init_(size) do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} =
      Agent.start_link(
        fn ->
          %{
            size: size,
            ones: MapSet.new(),
            flipped: false
          }
        end,
        name: __MODULE__
      )

    :ok
  end

  @spec fix(idx :: integer) :: :ok
  def fix(idx) do
    Agent.update(__MODULE__, fn state ->
      cond do
        # flipped == false, need stored bit = 1
        not state.flipped and MapSet.member?(state.ones, idx) ->
          state

        not state.flipped ->
          %{state | ones: MapSet.put(state.ones, idx)}

        # flipped == true, need stored bit = 0 (i.e., remove if present)
        state.flipped and not MapSet.member?(state.ones, idx) ->
          state

        state.flipped ->
          %{state | ones: MapSet.delete(state.ones, idx)}
      end
    end)

    :ok
  end

  @spec unfix(idx :: integer) :: :ok
  def unfix(idx) do
    Agent.update(__MODULE__, fn state ->
      cond do
        # flipped == false, need stored bit = 0 (remove if present)
        not state.flipped and not MapSet.member?(state.ones, idx) ->
          state

        not state.flipped ->
          %{state | ones: MapSet.delete(state.ones, idx)}

        # flipped == true, need stored bit = 1 (add if absent)
        state.flipped and MapSet.member?(state.ones, idx) ->
          state

        state.flipped ->
          %{state | ones: MapSet.put(state.ones, idx)}
      end
    end)

    :ok
  end

  @spec flip() :: :ok
  def flip() do
    Agent.update(__MODULE__, fn state -> %{state | flipped: not state.flipped} end)
    :ok
  end

  @spec all() :: boolean
  def all() do
    {size, ones_set, flipped} = Agent.get(__MODULE__, fn s -> {s.size, s.ones, s.flipped} end)

    logical_one_count =
      if flipped, do: size - MapSet.size(ones_set), else: MapSet.size(ones_set)

    logical_one_count == size
  end

  @spec one() :: boolean
  def one() do
    {size, ones_set, flipped} = Agent.get(__MODULE__, fn s -> {s.size, s.ones, s.flipped} end)

    logical_one_count =
      if flipped, do: size - MapSet.size(ones_set), else: MapSet.size(ones_set)

    logical_one_count > 0
  end

  @spec count() :: integer
  def count() do
    {size, ones_set, flipped} = Agent.get(__MODULE__, fn s -> {s.size, s.ones, s.flipped} end)

    if flipped, do: size - MapSet.size(ones_set), else: MapSet.size(ones_set)
  end

  @spec to_string() :: String.t()
  def to_string() do
    state = Agent.get(__MODULE__, fn s -> s end)

    Enum.map_join(0..state.size - 1, fn idx ->
      stored_one = MapSet.member?(state.ones, idx)
      logical_one = if state.flipped, do: not stored_one, else: stored_one

      if logical_one, do: "1", else: "0"
    end)
  end
end
```
