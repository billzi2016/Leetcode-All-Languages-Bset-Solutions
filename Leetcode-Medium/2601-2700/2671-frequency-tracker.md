# 2671. Frequency Tracker

## Cpp

```cpp
class FrequencyTracker {
private:
    std::unordered_map<int, int> numFreq;
    std::unordered_map<int, int> freqCount;
public:
    FrequencyTracker() {}
    
    void add(int number) {
        int old = numFreq[number];
        int nw = old + 1;
        numFreq[number] = nw;
        if (old > 0) {
            auto it = freqCount.find(old);
            if (it != freqCount.end()) {
                if (--(it->second) == 0) freqCount.erase(it);
            }
        }
        ++freqCount[nw];
    }
    
    void deleteOne(int number) {
        auto itNum = numFreq.find(number);
        if (itNum == numFreq.end() || itNum->second == 0) return;
        int old = itNum->second;
        int nw = old - 1;
        auto itFreqOld = freqCount.find(old);
        if (itFreqOld != freqCount.end()) {
            if (--(itFreqOld->second) == 0) freqCount.erase(itFreqOld);
        }
        if (nw > 0) {
            ++freqCount[nw];
            itNum->second = nw;
        } else {
            numFreq.erase(itNum);
        }
    }
    
    bool hasFrequency(int frequency) {
        auto it = freqCount.find(frequency);
        return it != freqCount.end() && it->second > 0;
    }
};

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker* obj = new FrequencyTracker();
 * obj->add(number);
 * obj->deleteOne(number);
 * bool param_3 = obj->hasFrequency(frequency);
 */
```

## Java

```java
class FrequencyTracker {
    private static final int MAX_NUMBER = 100000;
    private static final int MAX_FREQ = 200000;
    private final int[] numFreq;
    private final int[] freqCount;

    public FrequencyTracker() {
        numFreq = new int[MAX_NUMBER + 1];
        freqCount = new int[MAX_FREQ + 2];
    }

    public void add(int number) {
        int oldFreq = numFreq[number];
        int newFreq = oldFreq + 1;
        numFreq[number] = newFreq;
        if (oldFreq > 0) {
            freqCount[oldFreq]--;
        }
        freqCount[newFreq]++;
    }

    public void deleteOne(int number) {
        int oldFreq = numFreq[number];
        if (oldFreq == 0) {
            return;
        }
        int newFreq = oldFreq - 1;
        numFreq[number] = newFreq;
        freqCount[oldFreq]--;
        if (newFreq > 0) {
            freqCount[newFreq]++;
        }
    }

    public boolean hasFrequency(int frequency) {
        if (frequency < 0 || frequency >= freqCount.length) {
            return false;
        }
        return freqCount[frequency] > 0;
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = new FrequencyTracker();
 * obj.add(number);
 * obj.deleteOne(number);
 * boolean param_3 = obj.hasFrequency(frequency);
 */
```

## Python

```python
import collections

class FrequencyTracker(object):
    def __init__(self):
        self.num_freq = {}                     # number -> its frequency
        self.freq_cnt = collections.defaultdict(int)  # frequency -> count of numbers having this frequency

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        old = self.num_freq.get(number, 0)
        new = old + 1
        self.num_freq[number] = new

        if old > 0:
            self.freq_cnt[old] -= 1
            if self.freq_cnt[old] == 0:
                del self.freq_cnt[old]
        self.freq_cnt[new] += 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        old = self.num_freq.get(number, 0)
        if old == 0:
            return

        new = old - 1
        # update frequency count for the old frequency
        self.freq_cnt[old] -= 1
        if self.freq_cnt[old] == 0:
            del self.freq_cnt[old]

        if new == 0:
            del self.num_freq[number]
        else:
            self.num_freq[number] = new
            self.freq_cnt[new] += 1

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.freq_cnt.get(frequency, 0) > 0
```

## Python3

```python
class FrequencyTracker:
    def __init__(self):
        self.num_freq = {}
        self.freq_cnt = {}

    def _inc_freq(self, f: int) -> None:
        if f <= 0:
            return
        self.freq_cnt[f] = self.freq_cnt.get(f, 0) + 1

    def _dec_freq(self, f: int) -> None:
        if f <= 0:
            return
        cnt = self.freq_cnt.get(f, 0)
        if cnt <= 1:
            self.freq_cnt.pop(f, None)
        else:
            self.freq_cnt[f] = cnt - 1

    def add(self, number: int) -> None:
        old_f = self.num_freq.get(number, 0)
        new_f = old_f + 1
        self.num_freq[number] = new_f
        self._dec_freq(old_f)
        self._inc_freq(new_f)

    def deleteOne(self, number: int) -> None:
        old_f = self.num_freq.get(number, 0)
        if old_f == 0:
            return
        new_f = old_f - 1
        if new_f == 0:
            del self.num_freq[number]
        else:
            self.num_freq[number] = new_f
        self._dec_freq(old_f)
        self._inc_freq(new_f)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_cnt.get(frequency, 0) > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *numFreq;   // frequency of each number (index by number)
    int *freqCnt;   // count of numbers having a specific frequency
} FrequencyTracker;

#define MAX_NUMBER 100000
#define MAX_FREQ   200000

FrequencyTracker* frequencyTrackerCreate() {
    FrequencyTracker *obj = (FrequencyTracker *)malloc(sizeof(FrequencyTracker));
    obj->numFreq = (int *)calloc(MAX_NUMBER + 1, sizeof(int));
    obj->freqCnt = (int *)calloc(MAX_FREQ + 2, sizeof(int)); // extra space for safety
    return obj;
}

void frequencyTrackerAdd(FrequencyTracker* obj, int number) {
    int oldFreq = obj->numFreq[number];
    int newFreq = oldFreq + 1;
    obj->numFreq[number] = newFreq;

    if (oldFreq > 0) {
        obj->freqCnt[oldFreq]--;
    }
    obj->freqCnt[newFreq]++;
}

void frequencyTrackerDeleteOne(FrequencyTracker* obj, int number) {
    int oldFreq = obj->numFreq[number];
    if (oldFreq == 0) return; // number not present

    int newFreq = oldFreq - 1;
    obj->numFreq[number] = newFreq;

    obj->freqCnt[oldFreq]--;
    if (newFreq > 0) {
        obj->freqCnt[newFreq]++;
    }
}

bool frequencyTrackerHasFrequency(FrequencyTracker* obj, int frequency) {
    if (frequency < 0 || frequency > MAX_FREQ) return false;
    return obj->freqCnt[frequency] > 0;
}

void frequencyTrackerFree(FrequencyTracker* obj) {
    if (!obj) return;
    free(obj->numFreq);
    free(obj->freqCnt);
    free(obj);
}

/**
 * Your FrequencyTracker struct will be instantiated and called as such:
 * FrequencyTracker* obj = frequencyTrackerCreate();
 * frequencyTrackerAdd(obj, number);
 *
 * frequencyTrackerDeleteOne(obj, number);
 *
 * bool param_3 = frequencyTrackerHasFrequency(obj, frequency);
 *
 * frequencyTrackerFree(obj);
 */
```

## Csharp

```csharp
public class FrequencyTracker {
    private readonly Dictionary<int, int> _numFreq = new();
    private readonly Dictionary<int, int> _freqCount = new();

    public FrequencyTracker() { }

    public void Add(int number) {
        int oldFreq = 0;
        if (_numFreq.TryGetValue(number, out var f))
            oldFreq = f;

        int newFreq = oldFreq + 1;
        _numFreq[number] = newFreq;

        if (oldFreq > 0)
            DecrementFreq(oldFreq);
        IncrementFreq(newFreq);
    }

    public void DeleteOne(int number) {
        if (!_numFreq.TryGetValue(number, out var oldFreq) || oldFreq == 0)
            return;

        int newFreq = oldFreq - 1;
        if (newFreq == 0)
            _numFreq.Remove(number);
        else
            _numFreq[number] = newFreq;

        DecrementFreq(oldFreq);
        if (newFreq > 0)
            IncrementFreq(newFreq);
    }

    public bool HasFrequency(int frequency) {
        return _freqCount.TryGetValue(frequency, out var cnt) && cnt > 0;
    }

    private void IncrementFreq(int freq) {
        if (_freqCount.ContainsKey(freq))
            _freqCount[freq]++;
        else
            _freqCount[freq] = 1;
    }

    private void DecrementFreq(int freq) {
        if (!_freqCount.TryGetValue(freq, out var cnt))
            return;
        if (cnt == 1)
            _freqCount.Remove(freq);
        else
            _freqCount[freq] = cnt - 1;
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = new FrequencyTracker();
 * obj.Add(number);
 * obj.DeleteOne(number);
 * bool param_3 = obj.HasFrequency(frequency);
 */
```

## Javascript

```javascript
var FrequencyTracker = function() {
    this.numFreq = new Map();
    this.freqCnt = new Map();
};

FrequencyTracker.prototype._updateFreqCount = function(freq, delta) {
    if (freq <= 0) return;
    let cnt = this.freqCnt.get(freq) || 0;
    cnt += delta;
    if (cnt === 0) {
        this.freqCnt.delete(freq);
    } else {
        this.freqCnt.set(freq, cnt);
    }
};

FrequencyTracker.prototype.add = function(number) {
    const oldFreq = this.numFreq.get(number) || 0;
    const newFreq = oldFreq + 1;
    this.numFreq.set(number, newFreq);
    if (oldFreq > 0) this._updateFreqCount(oldFreq, -1);
    this._updateFreqCount(newFreq, 1);
};

FrequencyTracker.prototype.deleteOne = function(number) {
    const oldFreq = this.numFreq.get(number) || 0;
    if (oldFreq === 0) return;
    const newFreq = oldFreq - 1;
    if (newFreq === 0) {
        this.numFreq.delete(number);
    } else {
        this.numFreq.set(number, newFreq);
    }
    this._updateFreqCount(oldFreq, -1);
    if (newFreq > 0) this._updateFreqCount(newFreq, 1);
};

FrequencyTracker.prototype.hasFrequency = function(frequency) {
    return (this.freqCnt.get(frequency) || 0) > 0;
};
```

## Typescript

```typescript
class FrequencyTracker {
    private numFreq: Map<number, number>;
    private freqCount: Map<number, number>;

    constructor() {
        this.numFreq = new Map();
        this.freqCount = new Map();
    }

    add(number: number): void {
        const oldFreq = this.numFreq.get(number) ?? 0;
        const newFreq = oldFreq + 1;

        // Update number's frequency
        this.numFreq.set(number, newFreq);

        // Decrease count of old frequency if applicable
        if (oldFreq > 0) {
            const oldCount = this.freqCount.get(oldFreq)! - 1;
            if (oldCount === 0) {
                this.freqCount.delete(oldFreq);
            } else {
                this.freqCount.set(oldFreq, oldCount);
            }
        }

        // Increase count of new frequency
        this.freqCount.set(newFreq, (this.freqCount.get(newFreq) ?? 0) + 1);
    }

    deleteOne(number: number): void {
        const oldFreq = this.numFreq.get(number) ?? 0;
        if (oldFreq === 0) return; // number not present

        const newFreq = oldFreq - 1;

        // Update number's frequency
        if (newFreq === 0) {
            this.numFreq.delete(number);
        } else {
            this.numFreq.set(number, newFreq);
        }

        // Decrease count of old frequency
        const oldCount = this.freqCount.get(oldFreq)! - 1;
        if (oldCount === 0) {
            this.freqCount.delete(oldFreq);
        } else {
            this.freqCount.set(oldFreq, oldCount);
        }

        // Increase count of new frequency if >0
        if (newFreq > 0) {
            this.freqCount.set(newFreq, (this.freqCount.get(newFreq) ?? 0) + 1);
        }
    }

    hasFrequency(frequency: number): boolean {
        return (this.freqCount.get(frequency) ?? 0) > 0;
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * var obj = new FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * var param_3 = obj.hasFrequency(frequency)
 */
```

## Php

```php
class FrequencyTracker {
    private $numFreq = [];
    private $freqCount = [];

    function __construct() {
        // No initialization needed beyond property defaults
    }

    /**
     * @param Integer $number
     * @return NULL
     */
    function add($number) {
        $old = $this->numFreq[$number] ?? 0;
        $new = $old + 1;
        $this->numFreq[$number] = $new;

        if ($old > 0) {
            $this->freqCount[$old]--;
            if ($this->freqCount[$old] == 0) {
                unset($this->freqCount[$old]);
            }
        }

        $this->freqCount[$new] = ($this->freqCount[$new] ?? 0) + 1;
    }

    /**
     * @param Integer $number
     * @return NULL
     */
    function deleteOne($number) {
        if (!isset($this->numFreq[$number])) {
            return;
        }
        $old = $this->numFreq[$number];
        if ($old == 0) {
            return;
        }

        $new = $old - 1;

        // Update frequency count for the old frequency
        $this->freqCount[$old]--;
        if ($this->freqCount[$old] == 0) {
            unset($this->freqCount[$old]);
        }

        if ($new > 0) {
            $this->numFreq[$number] = $new;
            $this->freqCount[$new] = ($this->freqCount[$new] ?? 0) + 1;
        } else {
            // Remove the number entirely when its frequency drops to zero
            unset($this->numFreq[$number]);
        }
    }

    /**
     * @param Integer $frequency
     * @return Boolean
     */
    function hasFrequency($frequency) {
        return isset($this->freqCount[$frequency]) && $this->freqCount[$frequency] > 0;
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * $obj = new FrequencyTracker();
 * $obj->add($number);
 * $obj->deleteOne($number);
 * $ret_3 = $obj->hasFrequency($frequency);
 */
```

## Swift

```swift
class FrequencyTracker {
    private var numToFreq: [Int: Int]
    private var freqCount: [Int: Int]

    init() {
        self.numToFreq = [:]
        self.freqCount = [:]
    }
    
    func add(_ number: Int) {
        let oldFreq = numToFreq[number] ?? 0
        let newFreq = oldFreq + 1
        numToFreq[number] = newFreq
        
        if oldFreq > 0 {
            if let cnt = freqCount[oldFreq] {
                if cnt == 1 {
                    freqCount.removeValue(forKey: oldFreq)
                } else {
                    freqCount[oldFreq] = cnt - 1
                }
            }
        }
        freqCount[newFreq, default: 0] += 1
    }
    
    func deleteOne(_ number: Int) {
        guard let oldFreq = numToFreq[number], oldFreq > 0 else { return }
        let newFreq = oldFreq - 1
        
        if oldFreq == 1 {
            numToFreq.removeValue(forKey: number)
        } else {
            numToFreq[number] = newFreq
        }
        
        if let cnt = freqCount[oldFreq] {
            if cnt == 1 {
                freqCount.removeValue(forKey: oldFreq)
            } else {
                freqCount[oldFreq] = cnt - 1
            }
        }
        
        if newFreq > 0 {
            freqCount[newFreq, default: 0] += 1
        }
    }
    
    func hasFrequency(_ frequency: Int) -> Bool {
        return (freqCount[frequency] ?? 0) > 0
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let obj = FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * let ret_3: Bool = obj.hasFrequency(frequency)
 */
```

## Kotlin

```kotlin
class FrequencyTracker() {

    private val numFreq = HashMap<Int, Int>()
    private val freqCount = HashMap<Int, Int>()

    fun add(number: Int) {
        val old = numFreq.getOrDefault(number, 0)
        val new = old + 1
        numFreq[number] = new

        if (old > 0) decrementFreq(old)
        incrementFreq(new)
    }

    fun deleteOne(number: Int) {
        val old = numFreq[number] ?: return
        val new = old - 1

        if (new == 0) {
            numFreq.remove(number)
        } else {
            numFreq[number] = new
        }

        decrementFreq(old)
        if (new > 0) incrementFreq(new)
    }

    fun hasFrequency(frequency: Int): Boolean {
        return freqCount.getOrDefault(frequency, 0) > 0
    }

    private fun incrementFreq(freq: Int) {
        freqCount[freq] = freqCount.getOrDefault(freq, 0) + 1
    }

    private fun decrementFreq(freq: Int) {
        val cnt = freqCount[freq] ?: return
        if (cnt == 1) {
            freqCount.remove(freq)
        } else {
            freqCount[freq] = cnt - 1
        }
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * var obj = FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * var param_3 = obj.hasFrequency(frequency)
 */
```

## Dart

```dart
class FrequencyTracker {
  final Map<int, int> _numFreq = {};
  final Map<int, int> _freqCount = {};

  FrequencyTracker();

  void add(int number) {
    int oldFreq = _numFreq[number] ?? 0;
    int newFreq = oldFreq + 1;
    _numFreq[number] = newFreq;

    if (oldFreq > 0) {
      int cnt = (_freqCount[oldFreq] ?? 0) - 1;
      if (cnt == 0) {
        _freqCount.remove(oldFreq);
      } else {
        _freqCount[oldFreq] = cnt;
      }
    }

    _freqCount[newFreq] = (_freqCount[newFreq] ?? 0) + 1;
  }

  void deleteOne(int number) {
    int oldFreq = _numFreq[number] ?? 0;
    if (oldFreq == 0) return;

    int newFreq = oldFreq - 1;
    if (newFreq == 0) {
      _numFreq.remove(number);
    } else {
      _numFreq[number] = newFreq;
    }

    int cntOld = (_freqCount[oldFreq] ?? 0) - 1;
    if (cntOld == 0) {
      _freqCount.remove(oldFreq);
    } else {
      _freqCount[oldFreq] = cntOld;
    }

    if (newFreq > 0) {
      _freqCount[newFreq] = (_freqCount[newFreq] ?? 0) + 1;
    }
  }

  bool hasFrequency(int frequency) {
    return (_freqCount[frequency] ?? 0) > 0;
  }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = FrequencyTracker();
 * obj.add(number);
 * obj.deleteOne(number);
 * bool param3 = obj.hasFrequency(frequency);
 */
```

## Golang

```go
type FrequencyTracker struct {
	numFreq map[int]int
	freqCnt map[int]int
}

func Constructor() FrequencyTracker {
	return FrequencyTracker{
		numFreq: make(map[int]int),
		freqCnt: make(map[int]int),
	}
}

func (this *FrequencyTracker) Add(number int) {
	oldFreq := this.numFreq[number]
	newFreq := oldFreq + 1
	this.numFreq[number] = newFreq

	if oldFreq > 0 {
		if cnt := this.freqCnt[oldFreq] - 1; cnt == 0 {
			delete(this.freqCnt, oldFreq)
		} else {
			this.freqCnt[oldFreq] = cnt
		}
	}
	this.freqCnt[newFreq]++
}

func (this *FrequencyTracker) DeleteOne(number int) {
	oldFreq := this.numFreq[number]
	if oldFreq == 0 {
		return
	}
	newFreq := oldFreq - 1

	if cnt := this.freqCnt[oldFreq] - 1; cnt == 0 {
		delete(this.freqCnt, oldFreq)
	} else {
		this.freqCnt[oldFreq] = cnt
	}

	if newFreq > 0 {
		this.freqCnt[newFreq]++
		this.numFreq[number] = newFreq
	} else {
		delete(this.numFreq, number)
	}
}

func (this *FrequencyTracker) HasFrequency(frequency int) bool {
	cnt, ok := this.freqCnt[frequency]
	return ok && cnt > 0
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * obj.DeleteOne(number);
 * param_3 := obj.HasFrequency(frequency);
 */
```

## Ruby

```ruby
class FrequencyTracker
  def initialize()
    @num_freq = Hash.new(0)
    @freq_count = Hash.new(0)
  end

=begin
    :type number: Integer
    :rtype: Void
=end
  def add(number)
    old = @num_freq[number]
    new_f = old + 1
    @num_freq[number] = new_f
    @freq_count[old] -= 1 if old > 0
    @freq_count[new_f] += 1
  end

=begin
    :type number: Integer
    :rtype: Void
=end
  def delete_one(number)
    old = @num_freq[number]
    return if old == 0
    new_f = old - 1
    @num_freq[number] = new_f
    @freq_count[old] -= 1
    if new_f > 0
      @freq_count[new_f] += 1
    else
      @num_freq.delete(number)
    end
  end

=begin
    :type frequency: Integer
    :rtype: Boolean
=end
  def has_frequency(frequency)
    @freq_count[frequency] > 0
  end
end
```

## Scala

```scala
import scala.collection.mutable.{HashMap, Map}

class FrequencyTracker() {

  private val numFreq: HashMap[Int, Int] = HashMap()
  private val freqCount: HashMap[Int, Int] = HashMap()

  def add(number: Int): Unit = {
    val oldFreq = numFreq.getOrElse(number, 0)
    val newFreq = oldFreq + 1
    numFreq.put(number, newFreq)

    if (oldFreq > 0) {
      val cntOld = freqCount(oldFreq) - 1
      if (cntOld == 0) freqCount.remove(oldFreq) else freqCount.update(oldFreq, cntOld)
    }
    freqCount.update(newFreq, freqCount.getOrElse(newFreq, 0) + 1)
  }

  def deleteOne(number: Int): Unit = {
    numFreq.get(number) match {
      case None => // do nothing
      case Some(oldFreq) =>
        val cntOld = freqCount(oldFreq) - 1
        if (cntOld == 0) freqCount.remove(oldFreq) else freqCount.update(oldFreq, cntOld)

        val newFreq = oldFreq - 1
        if (newFreq == 0) {
          numFreq.remove(number)
        } else {
          numFreq.put(number, newFreq)
          freqCount.update(newFreq, freqCount.getOrElse(newFreq, 0) + 1)
        }
    }
  }

  def hasFrequency(frequency: Int): Boolean = {
    freqCount.getOrElse(frequency, 0) > 0
  }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * val obj = new FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * val param_3 = obj.hasFrequency(frequency)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct FrequencyTracker {
    num_freq: HashMap<i32, i32>,
    freq_count: HashMap<i32, i32>,
}

impl FrequencyTracker {
    fn new() -> Self {
        FrequencyTracker {
            num_freq: HashMap::new(),
            freq_count: HashMap::new(),
        }
    }

    fn add(&mut self, number: i32) {
        let old = *self.num_freq.get(&number).unwrap_or(&0);
        let new = old + 1;
        self.num_freq.insert(number, new);

        if old > 0 {
            if let Some(cnt) = self.freq_count.get_mut(&old) {
                *cnt -= 1;
                if *cnt == 0 {
                    self.freq_count.remove(&old);
                }
            }
        }

        *self.freq_count.entry(new).or_insert(0) += 1;
    }

    fn delete_one(&mut self, number: i32) {
        let old = match self.num_freq.get(&number) {
            Some(&v) => v,
            None => return,
        };
        if old == 0 {
            return;
        }
        let new = old - 1;

        if new == 0 {
            self.num_freq.remove(&number);
        } else {
            self.num_freq.insert(number, new);
        }

        if let Some(cnt) = self.freq_count.get_mut(&old) {
            *cnt -= 1;
            if *cnt == 0 {
                self.freq_count.remove(&old);
            }
        }

        if new > 0 {
            *self.freq_count.entry(new).or_insert(0) += 1;
        }
    }

    fn has_frequency(&self, frequency: i32) -> bool {
        match self.freq_count.get(&frequency) {
            Some(&cnt) => cnt > 0,
            None => false,
        }
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let mut obj = FrequencyTracker::new();
 * obj.add(number);
 * obj.delete_one(number);
 * let ret_3: bool = obj.has_frequency(frequency);
 */
```

## Racket

```racket
(define frequency-tracker%
  (class object%
    (super-new)
    
    (field [num->freq (make-hash)])
    (field [freq-count (make-hash)])
    
    ;; add : exact-integer? -> void?
    (define/public (add number)
      (let* ([old (hash-ref num->freq number 0)]
             [new (+ old 1)])
        (hash-set! num->freq number new)
        (when (> old 0)
          (let ([cnt (hash-ref freq-count old 0)])
            (if (= cnt 1)
                (hash-remove! freq-count old)
                (hash-set! freq-count old (- cnt 1)))))
        (hash-set! freq-count new (+ 1 (hash-ref freq-count new 0)))))
    
    ;; delete-one : exact-integer? -> void?
    (define/public (delete-one number)
      (let ([old (hash-ref num->freq number 0)])
        (when (> old 0)
          (let ([new (- old 1)])
            (if (= new 0)
                (hash-remove! num->freq number)
                (hash-set! num->freq number new))
            (let ([cnt-old (hash-ref freq-count old 0)])
              (if (= cnt-old 1)
                  (hash-remove! freq-count old)
                  (hash-set! freq-count old (- cnt-old 1))))
            (when (> new 0)
              (hash-set! freq-count new (+ 1 (hash-ref freq-count new 0))))))))
    
    ;; has-frequency : exact-integer? -> boolean?
    (define/public (has-frequency frequency)
      (> (hash-ref freq-count frequency 0) 0))
    ))
```

## Erlang

```erlang
-module(solution).
-export([frequency_tracker_init_/0,
         frequency_tracker_add/1,
         frequency_tracker_delete_one/1,
         frequency_tracker_has_frequency/1]).

%% Initialize the data structures.
-spec frequency_tracker_init_() -> any().
frequency_tracker_init_() ->
    put(num_freq, #{}),
    put(freq_count, #{}).

%% Add a number to the tracker.
-spec frequency_tracker_add(Number :: integer()) -> any().
frequency_tracker_add(Number) ->
    NumFreq = get(num_freq),
    FreqCount = get(freq_count),

    OldFreq = maps:get(Number, NumFreq, 0),
    NewFreq = OldFreq + 1,

    %% Update number -> frequency map.
    NumFreq2 = maps:put(Number, NewFreq, NumFreq),

    %% Decrease count of the old frequency (if any).
    FreqCount1 =
        case OldFreq of
            0 -> FreqCount;
            _ ->
                CountOld = maps:get(OldFreq, FreqCount),
                if CountOld == 1 ->
                        maps:remove(OldFreq, FreqCount);
                   true ->
                        maps:put(OldFreq, CountOld - 1, FreqCount)
                end
        end,

    %% Increase count of the new frequency.
    CountNew = maps:get(NewFreq, FreqCount1, 0),
    FreqCount2 = maps:put(NewFreq, CountNew + 1, FreqCount1),

    put(num_freq, NumFreq2),
    put(freq_count, FreqCount2).

%% Delete one occurrence of a number from the tracker.
-spec frequency_tracker_delete_one(Number :: integer()) -> any().
frequency_tracker_delete_one(Number) ->
    NumFreq = get(num_freq),
    case maps:find(Number, NumFreq) of
        error ->
            ok;  % Number not present, nothing to do.
        {ok, OldFreq} when OldFreq > 0 ->
            NewFreq = OldFreq - 1,

            %% Update number -> frequency map.
            NumFreq2 =
                if NewFreq == 0 ->
                        maps:remove(Number, NumFreq);
                   true ->
                        maps:put(Number, NewFreq, NumFreq)
                end,

            FreqCount = get(freq_count),

            %% Decrease count of the old frequency.
            CountOld = maps:get(OldFreq, FreqCount),
            FreqCount1 =
                if CountOld == 1 ->
                        maps:remove(OldFreq, FreqCount);
                   true ->
                        maps:put(OldFreq, CountOld - 1, FreqCount)
                end,

            %% Increase count of the new frequency (if >0).
            FreqCount2 =
                case NewFreq of
                    0 -> FreqCount1;
                    _ ->
                        CountNew = maps:get(NewFreq, FreqCount1, 0),
                        maps:put(NewFreq, CountNew + 1, FreqCount1)
                end,

            put(num_freq, NumFreq2),
            put(freq_count, FreqCount2);
        {ok, _} ->
            ok
    end.

%% Check if any number has exactly the given frequency.
-spec frequency_tracker_has_frequency(Frequency :: integer()) -> boolean().
frequency_tracker_has_frequency(Frequency) ->
    FreqCount = get(freq_count),
    case maps:get(Frequency, FreqCount, 0) of
        0 -> false;
        _ -> true
    end.
```

## Elixir

```elixir
defmodule FrequencyTracker do
  @spec init_() :: :ok
  def init_() do
    case Process.whereis(__MODULE__) do
      nil ->
        Agent.start_link(fn -> %{num_to_freq: %{}, freq_count: %{}} end, name: __MODULE__)
        :ok

      _pid ->
        Agent.update(__MODULE__, fn _ -> %{num_to_freq: %{}, freq_count: %{}} end)
    end
  end

  @spec add(number :: integer) :: :ok
  def add(number) do
    Agent.update(__MODULE__, fn state ->
      num_to_freq = state.num_to_freq
      freq_count = state.freq_count

      old_freq = Map.get(num_to_freq, number, 0)
      new_freq = old_freq + 1

      num_to_freq = Map.put(num_to_freq, number, new_freq)

      freq_count =
        freq_count
        |> decrement(old_freq)
        |> increment(new_freq)

      %{num_to_freq: num_to_freq, freq_count: freq_count}
    end)
  end

  @spec delete_one(number :: integer) :: :ok
  def delete_one(number) do
    Agent.update(__MODULE__, fn state ->
      num_to_freq = state.num_to_freq
      freq_count = state.freq_count

      old_freq = Map.get(num_to_freq, number, 0)

      if old_freq == 0 do
        state
      else
        new_freq = old_freq - 1

        num_to_freq =
          if new_freq == 0 do
            Map.delete(num_to_freq, number)
          else
            Map.put(num_to_freq, number, new_freq)
          end

        freq_count =
          freq_count
          |> decrement(old_freq)
          |> increment(new_freq)

        %{num_to_freq: num_to_freq, freq_count: freq_count}
      end
    end)
  end

  @spec has_frequency(frequency :: integer) :: boolean
  def has_frequency(frequency) do
    Agent.get(__MODULE__, fn state ->
      Map.get(state.freq_count, frequency, 0) > 0
    end)
  end

  # Helper functions
  defp decrement(freq_map, 0), do: freq_map

  defp decrement(freq_map, f) do
    case Map.get(freq_map, f, 0) - 1 do
      0 -> Map.delete(freq_map, f)
      v when v > 0 -> Map.put(freq_map, f, v)
    end
  end

  defp increment(freq_map, 0), do: freq_map

  defp increment(freq_map, f) do
    Map.update(freq_map, f, 1, &(&1 + 1))
  end
end
```
