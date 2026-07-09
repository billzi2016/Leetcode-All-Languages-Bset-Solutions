# 0284. Peeking Iterator

## Cpp

```cpp
class PeekingIterator : public Iterator {
    mutable bool hasPeeked;
    mutable int peekVal;
public:
    PeekingIterator(const std::vector<int>& nums) : Iterator(nums), hasPeeked(false), peekVal(0) {}
    
    int peek() {
        if (!hasPeeked) {
            peekVal = Iterator::next();
            hasPeeked = true;
        }
        return peekVal;
    }
    
    int next() {
        if (hasPeeked) {
            hasPeeked = false;
            return peekVal;
        }
        return Iterator::next();
    }
    
    bool hasNext() const {
        return hasPeeked || Iterator::hasNext();
    }
};
```

## Java

```java
import java.util.Iterator;

class PeekingIterator implements Iterator<Integer> {
    private final Iterator<Integer> iterator;
    private Integer nextElement;
    
    public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        if (iterator.hasNext()) {
            nextElement = iterator.next();
        } else {
            nextElement = null;
        }
    }
    
    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        return nextElement;
    }
    
    @Override
    public Integer next() {
        Integer current = nextElement;
        if (iterator.hasNext()) {
            nextElement = iterator.next();
        } else {
            nextElement = null;
        }
        return current;
    }
    
    @Override
    public boolean hasNext() {
        return nextElement != null;
    }
}
```

## Python

```python
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self._has_peeked = False
        self._peek_val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._has_peeked:
            self._peek_val = self._iter.next()
            self._has_peeked = True
        return self._peek_val

    def next(self):
        """
        :rtype: int
        """
        if self._has_peeked:
            val = self._peek_val
            self._has_peeked = False
            self._peek_val = None
            return val
        else:
            return self._iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._has_peeked or self._iter.hasNext()
```

## Python3

```python
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next = iterator.next() if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/* Iterator definition provided by LeetCode */
struct Iterator {
    bool (*hasNext)();
    int  (*next)();
};

/* PeekingIterator structure */
struct PeekingIterator {
    struct Iterator *iterator;
    bool hasPeeked;
    int peekedElement;
};

/* Constructor */
struct PeekingIterator* Constructor(struct Iterator* iter) {
    struct PeekingIterator* piter = (struct PeekingIterator*)malloc(sizeof(struct PeekingIterator));
    piter->iterator   = iter;
    piter->hasPeeked  = false;
    return piter;
}

/* Peek the next element without advancing */
int peek(struct PeekingIterator* obj) {
    if (!obj->hasPeeked) {
        obj->peekedElement = obj->iterator->next();
        obj->hasPeeked = true;
    }
    return obj->peekedElement;
}

/* Return the next element and advance */
int next(struct PeekingIterator* obj) {
    if (obj->hasPeeked) {
        obj->hasPeeked = false;
        return obj->peekedElement;
    }
    return obj->iterator->next();
}

/* Check if there are more elements */
bool hasNext(struct PeekingIterator* obj) {
    if (obj->hasPeeked) return true;
    return obj->iterator->hasNext();
}

/* Optional: free the iterator */
void peekingIteratorFree(struct PeekingIterator* obj) {
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class PeekingIterator {
    private readonly IEnumerator<int> _iterator;
    private int _next;
    private bool _hasNext;

    public PeekingIterator(IEnumerator<int> iterator) {
        _iterator = iterator;
        _hasNext = _iterator.MoveNext();
        if (_hasNext) {
            _next = _iterator.Current;
        }
    }

    // Returns the next element in the iteration without advancing the iterator.
    public int Peek() {
        return _next;
    }

    // Returns the next element in the iteration and advances the iterator.
    public int Next() {
        int current = _next;
        _hasNext = _iterator.MoveNext();
        if (_hasNext) {
            _next = _iterator.Current;
        }
        return current;
    }

    // Returns false if the iterator is referring to the end of the array or true otherwise.
    public bool HasNext() {
        return _hasNext;
    }
}
```

## Javascript

```javascript
/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    }; 
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/**
 * @param {Iterator} iterator
 */
var PeekingIterator = function(iterator) {
    this.iterator = iterator;
    this._hasPeeked = false;
    this._peekedElement = null;
    if (this.iterator.hasNext()) {
        this._peekedElement = this.iterator.next();
        this._hasPeeked = true;
    }
};

/**
 * @return {number}
 */
PeekingIterator.prototype.peek = function() {
    return this._peekedElement;
};

/**
 * @return {number}
 */
PeekingIterator.prototype.next = function() {
    var result;
    if (this._hasPeeked) {
        result = this._peekedElement;
    } else {
        result = this.iterator.next();
    }
    // Refresh the cache for the next element
    if (this.iterator.hasNext()) {
        this._peekedElement = this.iterator.next();
        this._hasPeeked = true;
    } else {
        this._peekedElement = null;
        this._hasPeeked = false;
    }
    return result;
};

/**
 * @return {boolean}
 */
PeekingIterator.prototype.hasNext = function() {
    return this._hasPeeked || this.iterator.hasNext();
};
```

## Typescript

```typescript
/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Iterator {
 *      hasNext(): boolean {}
 *
 *      next(): number {}
 * }
 */

class PeekingIterator {
    private iterator: Iterator;
    private peekedValue: number | null = null;
    private hasPeeked: boolean = false;

    constructor(iterator: Iterator) {
        this.iterator = iterator;
    }

    peek(): number {
        if (!this.hasPeeked) {
            this.peekedValue = this.iterator.next();
            this.hasPeeked = true;
        }
        // Non-null assertion because calls are guaranteed to be valid
        return this.peekedValue!;
    }

    next(): number {
        if (this.hasPeeked) {
            const result = this.peekedValue!;
            this.peekedValue = null;
            this.hasPeeked = false;
            return result;
        }
        return this.iterator.next();
    }

    hasNext(): boolean {
        return this.hasPeeked || this.iterator.hasNext();
    }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = new PeekingIterator(iterator)
 * var param_1 = obj.peek()
 * var param_2 = obj.next()
 * var param_3 = obj.hasNext()
 */
```

## Php

```php
class PeekingIterator {
    private $iter;
    private $hasPeeked = false;
    private $peekVal;

    /**
     * @param ArrayIterator $arr
     */
    function __construct($arr) {
        $this->iter = $arr;
    }

    /**
     * @return Integer
     */
    function next() {
        if ($this->hasPeeked) {
            $result = $this->peekVal;
            $this->hasPeeked = false;
            $this->peekVal = null;
            // move underlying iterator forward since we consumed the cached value
            $this->iter->next();
            return $result;
        } else {
            $result = $this->iter->current();
            $this->iter->next();
            return $result;
        }
    }

    /**
     * @return Integer
     */
    function peek() {
        if (!$this->hasPeeked) {
            $this->peekVal = $this->iter->current();
            $this->hasPeeked = true;
        }
        return $this->peekVal;
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        if ($this->hasPeeked) {
            return true;
        }
        return $this->iter->valid();
    }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * $obj = new PeekingIterator($arr);
 * $ret_1 = $obj->next();
 * $ret_2 = $obj->peek();
 * $ret_3 = $obj->hasNext();
 */
```

## Swift

```swift
class PeetingIterator {
    private var iterator: IndexingIterator<[Int]>
    private var nextElement: Int?
    
    init(_ arr: IndexingIterator<Array<Int>>) {
        self.iterator = arr
        self.nextElement = iterator.next()
    }
    
    func next() -> Int {
        let current = nextElement!
        nextElement = iterator.next()
        return current
    }
    
    func peek() -> Int {
        return nextElement!
    }
    
    func hasNext() -> Bool {
        return nextElement != nil
    }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * let obj = PeetingIterator(arr)
 * let ret_1: Int = obj.next()
 * let ret_2: Int = obj.peek()
 * let ret_3: Bool = obj.hasNext()
 */
```

## Kotlin

```kotlin
class PeekingIterator(iterator: Iterator<Int>) : Iterator<Int> {
    private val iter = iterator
    private var hasPeeked = false
    private var peekedElem = 0

    fun peek(): Int {
        if (!hasPeeked) {
            if (!iter.hasNext()) throw NoSuchElementException()
            peekedElem = iter.next()
            hasPeeked = true
        }
        return peekedElem
    }

    override fun next(): Int {
        if (hasPeeked) {
            hasPeeked = false
            return peekedElem
        }
        if (!iter.hasNext()) throw NoSuchElementException()
        return iter.next()
    }

    override fun hasNext(): Boolean {
        return hasPeeked || iter.hasNext()
    }
}
```

## Golang

```go
type PeekingIterator struct {
	iter      *Iterator
	cache     int
	hasCache  bool
}

func Constructor(iter *Iterator) *PeekingIterator {
	pi := &PeekingIterator{iter: iter}
	if iter.hasNext() {
		pi.cache = iter.next()
		pi.hasCache = true
	}
	return pi
}

func (this *PeekingIterator) hasNext() bool {
	return this.hasCache || this.iter.hasNext()
}

func (this *PeekingIterator) next() int {
	if this.hasCache {
		val := this.cache
		this.hasCache = false
		return val
	}
	return this.iter.next()
}

func (this *PeekingIterator) peek() int {
	if !this.hasCache {
		this.cache = this.iter.next()
		this.hasCache = true
	}
	return this.cache
}
```

## Ruby

```ruby
class PeekingIterator
  def initialize(iter)
    @iter = iter
    @has_peeked = false
    @peek_val = nil
  end

  def peek
    unless @has_peeked
      @peek_val = @iter.next
      @has_peeked = true
    end
    @peek_val
  end

  def next
    if @has_peeked
      val = @peek_val
      @has_peeked = false
      @peek_val = nil
      val
    else
      @iter.next
    end
  end

  def hasNext
    @has_peeked || @iter.hasNext
  end
end
```

## Scala

```scala
class PeekingIterator(_iterator: Iterator[Int]) {
  private var cache: Option[Int] = None

  def peek(): Int = {
    if (cache.isEmpty && _iterator.hasNext) {
      cache = Some(_iterator.next())
    }
    cache.get
  }

  def next(): Int = {
    if (cache.nonEmpty) {
      val v = cache.get
      cache = None
      v
    } else {
      _iterator.next()
    }
  }

  def hasNext(): Boolean = {
    cache.isDefined || _iterator.hasNext
  }
}
```
