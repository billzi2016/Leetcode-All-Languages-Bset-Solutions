# 0341. Flatten Nested List Iterator

## Cpp

```cpp
#include <vector>
#include <stack>

using namespace std;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
    stack<pair<vector<NestedInteger>::const_iterator,
               vector<NestedInteger>::const_iterator>> stk;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        stk.emplace(nestedList.cbegin(), nestedList.cend());
    }
    
    int next() {
        hasNext(); // ensure the top points to an integer
        int val = stk.top().first->getInteger();
        ++stk.top().first;
        return val;
    }
    
    bool hasNext() {
        while (!stk.empty()) {
            auto &top = stk.top();
            if (top.first == top.second) {
                stk.pop();
                continue;
            }
            if (top.first->isInteger())
                return true;
            const vector<NestedInteger> &lst = top.first->getList();
            ++top.first; // move past the list we are expanding
            stk.emplace(lst.cbegin(), lst.cend());
        }
        return false;
    }
};
```

## Java

```java
import java.util.Iterator;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    private Deque<Iterator<NestedInteger>> stack;
    private Integer nextInt;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new ArrayDeque<>();
        if (nestedList != null) {
            stack.push(nestedList.iterator());
        }
    }

    @Override
    public Integer next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        int result = nextInt;
        nextInt = null;
        return result;
    }

    @Override
    public boolean hasNext() {
        if (nextInt != null) {
            return true;
        }
        while (!stack.isEmpty()) {
            Iterator<NestedInteger> it = stack.peek();
            if (!it.hasNext()) {
                stack.pop();
                continue;
            }
            NestedInteger ni = it.next();
            if (ni.isInteger()) {
                nextInt = ni.getInteger();
                return true;
            } else {
                stack.push(ni.getList().iterator());
            }
        }
        return false;
    }
}
```

## Python

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Stack stores tuples of (list, current_index)
        self.stack = [(nestedList, 0)]

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise StopIteration("No more elements")
        lst, idx = self.stack[-1]
        # Retrieve integer at current position
        result = lst[idx].getInteger()
        # Move index forward for this list
        self.stack[-1] = (lst, idx + 1)
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            lst, idx = self.stack[-1]
            if idx == len(lst):
                # Finished traversing current list
                self.stack.pop()
                continue
            nested = lst[idx]
            if nested.isInteger():
                return True
            # It's a list; drill down
            self.stack[-1] = (lst, idx + 1)          # advance in the outer list
            self.stack.append((nested.getList(), 0)) # start iterating inner list
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```

## Python3

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#
#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#
#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """


class NestedIterator:
    def __init__(self, nestedList):
        self._flat = []
        self._idx = 0
        self._flatten(nestedList)

    def _flatten(self, lst):
        for ni in lst:
            if ni.isInteger():
                self._flat.append(ni.getInteger())
            else:
                self._flatten(ni.getList())

    def next(self) -> int:
        val = self._flat[self._idx]
        self._idx += 1
        return val

    def hasNext(self) -> bool:
        return self._idx < len(self._flat)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/* Interface provided by LeetCode (do not implement) */
bool NestedIntegerIsInteger(struct NestedInteger *);
int NestedIntegerGetInteger(struct NestedInteger *);
struct NestedInteger **NestedIntegerGetList(struct NestedInteger *);
int NestedIntegerGetListSize(struct NestedInteger *);

struct NestedIterator {
    int *data;
    int size;
    int pos;
    int cap;
};

static void pushInt(struct NestedIterator *it, int val) {
    if (it->size == it->cap) {
        int newCap = it->cap ? it->cap * 2 : 16;
        it->data = realloc(it->data, newCap * sizeof(int));
        it->cap = newCap;
    }
    it->data[it->size++] = val;
}

static void flatten(struct NestedInteger **list, int listSize, struct NestedIterator *it) {
    for (int i = 0; i < listSize; ++i) {
        struct NestedInteger *ni = list[i];
        if (NestedIntegerIsInteger(ni)) {
            pushInt(it, NestedIntegerGetInteger(ni));
        } else {
            struct NestedInteger **sublist = NestedIntegerGetList(ni);
            int subSize = NestedIntegerGetListSize(ni);
            flatten(sublist, subSize, it);
        }
    }
}

struct NestedIterator *nestedIterCreate(struct NestedInteger** nestedList, int nestedListSize) {
    struct NestedIterator *it = malloc(sizeof(*it));
    it->data = NULL;
    it->size = 0;
    it->pos = 0;
    it->cap = 0;
    flatten(nestedList, nestedListSize, it);
    return it;
}

bool nestedIterHasNext(struct NestedIterator *iter) {
    return iter && iter->pos < iter->size;
}

int nestedIterNext(struct NestedIterator *iter) {
    return iter->data[iter->pos++];
}

void nestedIterFree(struct NestedIterator *iter) {
    if (iter) {
        free(iter->data);
        free(iter);
    }
}
```

## Csharp

```csharp
using System.Collections.Generic;

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
public class NestedIterator {
    private readonly List<int> _flattened = new List<int>();
    private int _index = 0;

    public NestedIterator(IList<NestedInteger> nestedList) {
        Flatten(nestedList);
    }

    private void Flatten(IList<NestedInteger> list) {
        foreach (var ni in list) {
            if (ni.IsInteger()) {
                _flattened.Add(ni.GetInteger());
            } else {
                Flatten(ni.GetList());
            }
        }
    }

    public bool HasNext() {
        return _index < _flattened.Count;
    }

    public int Next() {
        return _flattened[_index++];
    }
}

/**
 * Your NestedIterator will be called like this:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.HasNext()) v[f()] = i.Next();
 */
```

## Javascript

```javascript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */

/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.stack = [];
    for (let i = nestedList.length - 1; i >= 0; --i) {
        this.stack.push(nestedList[i]);
    }
};

/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    while (this.stack.length > 0) {
        const top = this.stack[this.stack.length - 1];
        if (top.isInteger()) {
            return true;
        }
        // It's a list, unpack it
        this.stack.pop();
        const lst = top.getList();
        for (let i = lst.length - 1; i >= 0; --i) {
            this.stack.push(lst[i]);
        }
    }
    return false;
};

/**
 * @this NestedIterator
 * @returns {integer}
 */
NestedIterator.prototype.next = function() {
    if (!this.hasNext()) return null;
    const top = this.stack.pop();
    return top.getInteger();
};
```

## Typescript

```typescript
class NestedIterator {
    private flat: number[] = [];
    private idx: number = 0;

    constructor(nestedList: NestedInteger[]) {
        this.flatten(nestedList);
    }

    private flatten(list: NestedInteger[]): void {
        for (const ni of list) {
            if (ni.isInteger()) {
                const v = ni.getInteger();
                if (v !== null) {
                    this.flat.push(v);
                }
            } else {
                this.flatten(ni.getList());
            }
        }
    }

    hasNext(): boolean {
        return this.idx < this.flat.length;
    }

    next(): number {
        return this.flat[this.idx++];
    }
}
```

## Php

```php
<?php
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *
 *     // if value is not specified, initializes an empty list.
 *     // Otherwise initializes a single integer equal to value.
 *     function __construct($value = null)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     function isInteger() : bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     function getInteger()
 *
 *     // Set this NestedInteger to hold a single integer.
 *     function setInteger($i) : void
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     function add($ni) : void
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     function getList() : array
 * }
 */

class NestedIterator {
    /**
     * @var int[]
     */
    private $flat = [];

    /**
     * @var int
     */
    private $pos = 0;

    /**
     * @param NestedInteger[] $nestedList
     */
    function __construct($nestedList) {
        $this->flatten($nestedList);
    }

    /**
     * @return Integer
     */
    function next() {
        return $this->flat[$this->pos++];
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->pos < count($this->flat);
    }

    /**
     * @param NestedInteger[] $list
     */
    private function flatten($list) {
        foreach ($list as $ni) {
            if ($ni->isInteger()) {
                $this->flat[] = $ni->getInteger();
            } else {
                $this->flatten($ni->getList());
            }
        }
    }
}
?>
```

## Swift

```swift
class NestedIterator {
    private var flatList: [Int] = []
    private var index: Int = 0

    init(_ nestedList: [NestedInteger]) {
        flatten(nestedList)
    }

    private func flatten(_ list: [NestedInteger]) {
        for ni in list {
            if ni.isInteger() {
                flatList.append(ni.getInteger())
            } else {
                flatten(ni.getList())
            }
        }
    }

    func next() -> Int {
        let value = flatList[index]
        index += 1
        return value
    }

    func hasNext() -> Bool {
        return index < flatList.count
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.NoSuchElementException

class NestedIterator(nestedList: List<NestedInteger>) {
    private val stack = ArrayDeque<Iterator<NestedInteger>>()
    private var nextVal: Int? = null

    init {
        stack.addFirst(nestedList.iterator())
    }

    fun next(): Int {
        if (nextVal == null) {
            if (!hasNext()) throw NoSuchElementException()
        }
        val result = nextVal!!
        nextVal = null
        return result
    }

    fun hasNext(): Boolean {
        while (true) {
            if (stack.isEmpty()) return false
            val itr = stack.peekFirst()
            if (!itr.hasNext()) {
                stack.removeFirst()
                continue
            }
            val ni = itr.next()
            if (ni.isInteger()) {
                nextVal = ni.getInteger()!!
                return true
            } else {
                val list = ni.getList()
                if (list != null) {
                    stack.addFirst(list.iterator())
                }
            }
        }
    }
}
```

## Golang

```go
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

type NestedIterator struct {
	stack []*NestedInteger
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	it := &NestedIterator{}
	// push initial list in reverse order so we can pop from the end
	for i := len(nestedList) - 1; i >= 0; i-- {
		it.stack = append(it.stack, nestedList[i])
	}
	return it
}

func (this *NestedIterator) Next() int {
	if !this.HasNext() {
		return 0
	}
	top := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	return top.GetInteger()
}

func (this *NestedIterator) HasNext() bool {
	for len(this.stack) > 0 {
		top := this.stack[len(this.stack)-1]
		if top.IsInteger() {
			return true
		}
		// it's a list, flatten it
		this.stack = this.stack[:len(this.stack)-1]
		list := top.GetList()
		for i := len(list) - 1; i >= 0; i-- {
			this.stack = append(this.stack, list[i])
		}
	}
	return false
}
```

## Ruby

```ruby
class NestedIterator
  def initialize(nested_list)
    @flattened = []
    flatten(nested_list, @flattened)
    @index = 0
  end

  def has_next
    @index < @flattened.length
  end

  def next
    val = @flattened[@index]
    @index += 1
    val
  end

  private

  def flatten(list, result)
    list.each do |ni|
      if ni.is_integer
        result << ni.get_integer
      else
        flatten(ni.get_list, result)
      end
    end
  end
end
```

## Scala

```scala
import scala.collection.mutable.Stack

class NestedIterator(_nestedList: List[NestedInteger]) {
  private val stack = Stack[_nestedList.iterator]
  private var nextVal: Option[Int] = None

  def hasNext(): Boolean = {
    while (stack.nonEmpty) {
      if (!stack.top.hasNext) {
        stack.pop()
      } else {
        val ni = stack.top.next()
        if (ni.isInteger) {
          nextVal = Some(ni.getInteger)
          return true
        } else {
          stack.push(ni.getList.iterator)
        }
      }
    }
    false
  }

  def next(): Int = {
    if (nextVal.isEmpty && !hasNext()) {
      throw new NoSuchElementException("No more elements")
    }
    val res = nextVal.get
    nextVal = None
    res
  }
}
```

## Rust

```rust
use std::cell::Cell;

// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//     Int(i32),
//     List(Vec<NestedInteger>)
// }

struct NestedIterator {
    flat: Vec<i32>,
    pos: Cell<usize>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NestedIterator {

    fn new(nestedList: Vec<NestedInteger>) -> Self {
        let mut flat = Vec::new();
        fn dfs(list: &[NestedInteger], out: &mut Vec<i32>) {
            for ni in list {
                match ni {
                    NestedInteger::Int(v) => out.push(*v),
                    NestedInteger::List(l) => dfs(l, out),
                }
            }
        }
        dfs(&nestedList, &mut flat);
        Self { flat, pos: Cell::new(0) }
    }

    fn next(&self) -> i32 {
        let idx = self.pos.get();
        let val = self.flat[idx];
        self.pos.set(idx + 1);
        val
    }

    fn has_next(&self) -> bool {
        self.pos.get() < self.flat.len()
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * let obj = NestedIterator::new(nestedList);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */
```
