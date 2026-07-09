# 1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits

## Cpp

```cpp
class Solution {
public:
    struct BIT {
        int n;
        vector<int> bit;
        BIT(int n): n(n), bit(n + 1, 0) {}
        void add(int idx, int val) { // idx: 0-based
            for (int i = idx + 1; i <= n; i += i & -i) bit[i] += val;
        }
        int sum(int idx) const { // prefix sum [0..idx], idx 0-based
            int res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) res += bit[i];
            return res;
        }
    };
    
    string minInteger(string num, int k) {
        int n = num.size();
        vector<queue<int>> pos(10);
        for (int i = 0; i < n; ++i) {
            pos[num[i] - '0'].push(i);
        }
        BIT bit(n);
        for (int i = 0; i < n; ++i) bit.add(i, 1); // all positions present
        
        string ans;
        ans.reserve(n);
        long long K = k;
        while ((int)ans.size() < n) {
            bool placed = false;
            for (int d = 0; d <= 9 && !placed; ++d) {
                while (!pos[d].empty()) {
                    int idx = pos[d].front();
                    long long cost = bit.sum(idx) - 1; // swaps needed
                    if (cost <= K) {
                        ans.push_back('0' + d);
                        K -= cost;
                        bit.add(idx, -1); // remove this digit
                        pos[d].pop();
                        placed = true;
                        break;
                    } else {
                        // cannot use this digit now; later same digit will be farther
                        break;
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String minInteger(String num, int k) {
        int n = num.length();
        @SuppressWarnings("unchecked")
        ArrayDeque<Integer>[] pos = new ArrayDeque[10];
        for (int d = 0; d < 10; d++) pos[d] = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            int digit = num.charAt(i) - '0';
            pos[digit].add(i);
        }

        Fenwick fenwick = new Fenwick(n);
        for (int i = 0; i < n; i++) fenwick.add(i, 1);

        StringBuilder sb = new StringBuilder();
        long remainingK = k;

        for (int placed = 0; placed < n; placed++) {
            for (int d = 0; d < 10; d++) {
                if (pos[d].isEmpty()) continue;
                int idx = pos[d].peek(); // earliest occurrence
                long before = fenwick.sum(idx); // number of remaining elements up to idx inclusive
                long swapsNeeded = before - 1;   // elements before it in the current list
                if (swapsNeeded <= remainingK) {
                    remainingK -= swapsNeeded;
                    sb.append((char) ('0' + d));
                    pos[d].poll();
                    fenwick.add(idx, -1); // remove this index from BIT
                    break;
                }
            }
        }

        return sb.toString();
    }

    private static class Fenwick {
        private final long[] tree;
        private final int n;

        Fenwick(int size) {
            n = size;
            tree = new long[n + 1];
        }

        void add(int idx, long delta) {
            for (int i = idx + 1; i <= n; i += i & -i) {
                tree[i] += delta;
            }
        }

        long sum(int idx) {
            long res = 0;
            for (int i = idx + 1; i > 0; i -= i & -i) {
                res += tree[i];
            }
            return res;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        from collections import deque

        class BIT:
            __slots__ = ('n', 'bit')
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, i, delta):
                i += 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i):
                i += 1
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s

        n = len(num)
        pos = [deque() for _ in range(10)]
        for idx, ch in enumerate(num):
            pos[ord(ch) - 48].append(idx)

        bit = BIT(n)
        for i in range(n):
            bit.add(i, 1)

        res = []
        for _ in range(n):
            for d in range(10):
                if not pos[d]:
                    continue
                idx = pos[d][0]
                swaps_needed = bit.sum(idx) - 1
                if swaps_needed <= k:
                    k -= swaps_needed
                    res.append(chr(d + 48))
                    bit.add(idx, -1)
                    pos[d].popleft()
                    break
        return ''.join(res)
```

## Python3

```python
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from collections import deque

        n = len(num)

        class Fenwick:
            __slots__ = ("n", "bit")
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def add(self, i, delta):
                i += 1
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i):
                if i < 0:
                    return 0
                i += 1
                s = 0
                while i:
                    s += self.bit[i]
                    i -= i & -i
                return s

        # queues of positions for each digit
        pos = [deque() for _ in range(10)]
        for idx, ch in enumerate(num):
            pos[int(ch)].append(idx)

        ft = Fenwick(n)
        for i in range(n):
            ft.add(i, 1)   # all positions initially present

        ans = []
        used = 0
        while used < n:
            found = False
            for d in range(10):
                if not pos[d]:
                    continue
                idx = pos[d][0]
                cost = ft.sum(idx - 1)
                if cost <= k:
                    # take this digit
                    ans.append(str(d))
                    k -= cost
                    ft.add(idx, -1)          # remove position
                    pos[d].popleft()
                    used += 1
                    found = True
                    break
            if not found:
                # cannot move any more digits; append remaining in original order
                for i in range(n):
                    if ft.sum(i) - ft.sum(i - 1):
                        ans.append(num[i])
                break

        return ''.join(ans)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int *tree;
} BIT;

static void bit_init(BIT *b, int n) {
    b->n = n;
    b->tree = (int *)calloc(n + 1, sizeof(int));
    for (int i = 1; i <= n; ++i)
        b->tree[i] = i & -i;   // all positions start with value 1
}

static int bit_sum(BIT *b, int idx) {
    int s = 0;
    while (idx > 0) {
        s += b->tree[idx];
        idx -= idx & -idx;
    }
    return s;
}

static void bit_add(BIT *b, int idx, int delta) {
    for (; idx <= b->n; idx += idx & -idx)
        b->tree[idx] += delta;
}

char* minInteger(char* num, int k) {
    int n = (int)strlen(num);
    int cnt[10] = {0};
    for (int i = 0; i < n; ++i) cnt[num[i] - '0']++;

    int *pos[10];
    int posSize[10];
    int posIdx[10] = {0};

    for (int d = 0; d <= 9; ++d) {
        posSize[d] = cnt[d];
        if (cnt[d])
            pos[d] = (int *)malloc(cnt[d] * sizeof(int));
    }

    int cur[10] = {0};
    for (int i = 0; i < n; ++i) {
        int d = num[i] - '0';
        pos[d][cur[d]++] = i;
    }

    BIT bit;
    bit_init(&bit, n);

    char *res = (char *)malloc((n + 1) * sizeof(char));
    long long K = k;

    for (int placed = 0; placed < n; ++placed) {
        int chosenDigit = -1;
        int chosenPos = -1;
        for (int d = 0; d <= 9; ++d) {
            if (posIdx[d] >= posSize[d]) continue;
            int p = pos[d][posIdx[d]];
            long long swaps = (long long)bit_sum(&bit, p + 1) - 1 - placed;
            if (swaps <= K) {
                chosenDigit = d;
                chosenPos = p;
                K -= swaps;
                break;
            }
        }
        // should always find a digit
        res[placed] = num[chosenPos];
        bit_add(&bit, chosenPos + 1, -1);
        posIdx[chosenDigit]++;
    }

    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string MinInteger(string num, int k)
    {
        int n = num.Length;
        var queues = new Queue<int>[10];
        for (int d = 0; d < 10; d++) queues[d] = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            int digit = num[i] - '0';
            queues[digit].Enqueue(i);
        }

        var bit = new BIT(n);
        for (int i = 0; i < n; i++) bit.Add(i, 1);

        var sb = new System.Text.StringBuilder();
        long remainingK = k;
        int placed = 0;

        while (placed < n)
        {
            // Find farthest index we can reach with the remaining swaps
            int low = 0, high = n - 1, best = -1;
            while (low <= high)
            {
                int mid = (low + high) >> 1;
                long movesNeeded = bit.Sum(mid) - placed;
                if (movesNeeded <= remainingK)
                {
                    best = mid;
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }

            // Choose the smallest digit whose first occurrence is within reach
            for (int d = 0; d < 10; d++)
            {
                if (queues[d].Count == 0) continue;
                int idx = queues[d].Peek();
                if (idx > best) continue;

                long movesNeeded = bit.Sum(idx) - placed;
                remainingK -= movesNeeded;

                sb.Append((char)('0' + d));
                bit.Add(idx, -1);
                queues[d].Dequeue();
                placed++;
                break;
            }
        }

        return sb.ToString();
    }

    private class BIT
    {
        private readonly int[] tree;
        private readonly int n;

        public BIT(int size)
        {
            n = size;
            tree = new int[n + 2];
        }

        // index is 0‑based
        public void Add(int index, int delta)
        {
            for (int i = index + 1; i <= n; i += i & -i)
                tree[i] += delta;
        }

        // sum of [0..index], inclusive, index is 0‑based
        public int Sum(int index)
        {
            int res = 0;
            for (int i = index + 1; i > 0; i -= i & -i)
                res += tree[i];
            return res;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var minInteger = function(num, k) {
    const n = num.length;
    // positions for each digit 0-9
    const posLists = Array.from({length: 10}, () => []);
    for (let i = 0; i < n; i++) {
        const d = num.charCodeAt(i) - 48;
        posLists[d].push(i);
    }
    const ptr = new Array(10).fill(0);

    // Fenwick Tree to track remaining characters
    class BIT {
        constructor(size) {
            this.n = size;
            this.tree = new Int32Array(size + 2);
            // initialize with 1 at each position
            for (let i = 1; i <= size; i++) {
                this.tree[i] += 1;
                const j = i + (i & -i);
                if (j <= size) this.tree[j] += this.tree[i];
            }
        }
        add(idx, delta) { // idx is 0‑based
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx) { // prefix sum [0..idx], idx 0‑based
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
    }

    const bit = new BIT(n);
    const result = [];

    for (let i = 0; i < n; i++) {
        for (let d = 0; d <= 9; d++) {
            if (ptr[d] >= posLists[d].length) continue;
            const originalIdx = posLists[d][ptr[d]];
            const swapsNeeded = bit.sum(originalIdx) - 1; // elements before it
            if (swapsNeeded <= k) {
                k -= swapsNeeded;
                result.push(String.fromCharCode(48 + d));
                bit.add(originalIdx, -1); // remove this digit
                ptr[d]++;
                break;
            }
        }
    }

    return result.join('');
};
```

## Typescript

```typescript
function minInteger(num: string, k: number): string {
    const n = num.length;
    const posLists: number[][] = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < n; i++) {
        const d = num.charCodeAt(i) - 48;
        posLists[d].push(i);
    }
    const ptr = new Array(10).fill(0);

    class BIT {
        n: number;
        tree: number[];
        constructor(n: number) {
            this.n = n;
            this.tree = new Array(n + 1).fill(0);
        }
        add(idx: number, delta: number): void {
            for (let i = idx + 1; i <= this.n; i += i & -i) {
                this.tree[i] += delta;
            }
        }
        sum(idx: number): number {
            let res = 0;
            for (let i = idx + 1; i > 0; i -= i & -i) {
                res += this.tree[i];
            }
            return res;
        }
    }

    const bit = new BIT(n);
    const result: string[] = [];
    let placed = 0;

    while (result.length < n) {
        for (let d = 0; d <= 9; d++) {
            if (ptr[d] >= posLists[d].length) continue;
            const origIdx = posLists[d][ptr[d]];
            const removedBefore = origIdx === 0 ? 0 : bit.sum(origIdx - 1);
            const effectivePos = origIdx - removedBefore;
            const swapsNeeded = effectivePos - placed;
            if (swapsNeeded <= k) {
                k -= swapsNeeded;
                result.push(String.fromCharCode(48 + d));
                ptr[d]++;
                bit.add(origIdx, 1);
                placed++;
                break;
            }
        }
    }

    return result.join('');
}
```

## Php

```php
class BIT {
    private $tree;
    private $size;

    public function __construct($n) {
        $this->size = $n + 2; // extra space
        $this->tree = array_fill(0, $this->size, 0);
    }

    public function update($idx, $delta) {
        for ($i = $idx; $i < $this->size; $i += $i & (-$i)) {
            $this->tree[$i] += $delta;
        }
    }

    // sum of [1..$idx]
    public function query($idx) {
        $sum = 0;
        for ($i = $idx; $i > 0; $i -= $i & (-$i)) {
            $sum += $this->tree[$i];
        }
        return $sum;
    }
}

class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function minInteger($num, $k) {
        $n = strlen($num);
        // positions of each digit
        $digitPos = array_fill(0, 10, []);
        for ($i = 0; $i < $n; $i++) {
            $d = ord($num[$i]) - 48;
            $digitPos[$d][] = $i;
        }
        // pointers to next unused index in each digit list
        $ptr = array_fill(0, 10, 0);
        $bit = new BIT($n);
        $result = '';

        for ($pos = 0; $pos < $n; $pos++) {
            for ($d = 0; $d <= 9; $d++) {
                if ($ptr[$d] >= count($digitPos[$d])) {
                    continue;
                }
                $idx = $digitPos[$d][$ptr[$d]];
                // number of already taken elements before idx
                $takenBefore = $bit->query($idx);
                $effectivePos = $idx - $takenBefore; // current position after removals
                $swapsNeeded = $effectivePos - $pos;
                if ($swapsNeeded <= $k) {
                    $result .= chr(48 + $d);
                    $k -= $swapsNeeded;
                    $bit->update($idx + 1, 1); // mark this index as taken
                    $ptr[$d]++; // move pointer for this digit
                    break 2; // go to next position in result
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Fenwick {
    private var tree: [Int]
    private let n: Int
    init(_ size: Int) {
        self.n = size
        self.tree = Array(repeating: 0, count: size + 2)
    }
    func add(_ index: Int, _ delta: Int) {
        var i = index + 1
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    func sum(_ index: Int) -> Int {
        var res = 0
        var i = index + 1
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
}

class Solution {
    func minInteger(_ num: String, _ k: Int) -> String {
        let chars = Array(num)
        let n = chars.count
        var queues = [[Int]](repeating: [], count: 10)
        for i in 0..<n {
            if let d = chars[i].wholeNumberValue {
                queues[d].append(i)
            }
        }
        var ptrs = [Int](repeating: 0, count: 10)
        let bit = Fenwick(n)
        for i in 0..<n { bit.add(i, 1) }
        var remainingK = k
        var result = [Character]()
        while result.count < n {
            var chosenDigit = -1
            var chosenIdx = -1
            var distance = 0
            for d in 0...9 {
                while ptrs[d] < queues[d].count {
                    let idx = queues[d][ptrs[d]]
                    let curPos = bit.sum(idx) - 1   // zero‑based position in current list
                    if curPos <= remainingK {
                        chosenDigit = d
                        chosenIdx = idx
                        distance = curPos
                        break
                    } else {
                        // this digit cannot be reached, later same digit will be farther
                        break
                    }
                }
                if chosenDigit != -1 { break }
            }
            // Append chosen digit
            let ch = Character(UnicodeScalar(chosenDigit + 48)!)
            result.append(ch)
            remainingK -= distance
            bit.add(chosenIdx, -1)
            ptrs[chosenDigit] += 1
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minInteger(num: String, k: Int): String {
        val n = num.length
        // Fenwick Tree to keep track of remaining positions
        class Fenwick(val size: Int) {
            private val bit = IntArray(size + 2)
            fun add(idx0: Int, delta: Int) {
                var i = idx0 + 1
                while (i <= size) {
                    bit[i] += delta
                    i += i and -i
                }
            }
            fun sum(idx0: Int): Int {
                var i = idx0 + 1
                var res = 0
                while (i > 0) {
                    res += bit[i]
                    i -= i and -i
                }
                return res
            }
        }

        val fenwick = Fenwick(n)
        for (i in 0 until n) fenwick.add(i, 1)

        // queues of positions for each digit
        val pos = Array(10) { java.util.ArrayDeque<Int>() }
        for (i in num.indices) {
            val d = num[i] - '0'
            pos[d].add(i)
        }

        val sb = StringBuilder()
        var remainingK = k.toLong()

        while (sb.length < n) {
            var placed = false
            for (d in 0..9) {
                val q = pos[d]
                while (!q.isEmpty()) {
                    val idx = q.peekFirst()
                    val distance = fenwick.sum(idx) - 1 // swaps needed to bring to front
                    if (distance.toLong() <= remainingK) {
                        // choose this digit
                        sb.append('0' + d)
                        remainingK -= distance
                        fenwick.add(idx, -1)
                        q.pollFirst()
                        placed = true
                        break
                    } else {
                        // cannot reach this occurrence now; later ones are farther
                        break
                    }
                }
                if (placed) break
            }
        }

        return sb.toString()
    }
}
```

## Dart

```dart
import 'dart:collection';

class Fenwick {
  final int n;
  final List<int> tree;
  Fenwick(this.n) : tree = List.filled(n + 1, 0);

  void add(int idx, int delta) {
    for (int i = idx + 1; i <= n; i += i & -i) {
      tree[i] += delta;
    }
  }

  int sum(int idx) {
    int res = 0;
    for (int i = idx + 1; i > 0; i -= i & -i) {
      res += tree[i];
    }
    return res;
  }
}

class Solution {
  String minInteger(String num, int k) {
    final n = num.length;
    // queues for each digit
    final List<Queue<int>> pos = List.generate(10, (_) => Queue<int>());
    for (int i = 0; i < n; i++) {
      int d = num.codeUnitAt(i) - 48; // '0' ascii is 48
      pos[d].addLast(i);
    }

    final bit = Fenwick(n);
    for (int i = 0; i < n; i++) {
      bit.add(i, 1); // all positions are initially present
    }

    final StringBuffer sb = StringBuffer();

    while (sb.length < n) {
      bool placed = false;
      for (int d = 0; d <= 9 && !placed; d++) {
        if (pos[d].isEmpty) continue;
        int idx = pos[d].first;
        int swapsNeeded = bit.sum(idx) - 1;
        if (swapsNeeded <= k) {
          // place this digit
          sb.writeCharCode(48 + d);
          k -= swapsNeeded;
          bit.add(idx, -1); // remove position
          pos[d].removeFirst();
          placed = true;
        }
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
type BIT struct {
	n    int
	tree []int
}

func NewBIT(n int) *BIT {
	return &BIT{
		n:    n,
		tree: make([]int, n+2),
	}
}

func (b *BIT) Add(idx, delta int) {
	for i := idx + 1; i <= b.n; i += i & -i {
		b.tree[i] += delta
	}
}

// Sum returns the sum of [0..idx]
func (b *BIT) Sum(idx int) int {
	res := 0
	for i := idx + 1; i > 0; i -= i & -i {
		res += b.tree[i]
	}
	return res
}

func minInteger(num string, k int) string {
	n := len(num)
	posLists := make([][]int, 10)
	for i, ch := range num {
		d := ch - '0'
		posLists[d] = append(posLists[d], i)
	}
	ptrs := make([]int, 10)

	bit := NewBIT(n)
	for i := 0; i < n; i++ {
		bit.Add(i, 1)
	}

	ans := make([]byte, 0, n)
	remainingK := k

	for len(ans) < n {
		selected := false
		for d := 0; d <= 9; d++ {
			if ptrs[d] >= len(posLists[d]) {
				continue
			}
			idx := posLists[d][ptrs[d]]
			curPos := bit.Sum(idx) - 1 // zero‑based position in the current remaining string
			if curPos <= remainingK {
				remainingK -= curPos
				ans = append(ans, byte('0'+d))
				bit.Add(idx, -1)
				ptrs[d]++
				selected = true
				break
			}
		}
		if !selected {
			// Fallback: take the first remaining digit (should not happen under normal constraints)
			minPos := n + 1
			selD, selIdx := -1, -1
			for d := 0; d <= 9; d++ {
				if ptrs[d] >= len(posLists[d]) {
					continue
				}
				idx := posLists[d][ptrs[d]]
				curPos := bit.Sum(idx) - 1
				if curPos < minPos {
					minPos = curPos
					selD = d
					selIdx = idx
				}
			}
			ans = append(ans, byte('0'+selD))
			bit.Add(selIdx, -1)
			ptrs[selD]++
		}
	}

	return string(ans)
}
```

## Ruby

```ruby
def min_integer(num, k)
  n = num.length
  positions = Array.new(10) { [] }
  num.each_char.with_index do |ch, i|
    positions[ch.ord - 48] << i
  end

  class BIT
    def initialize(n)
      @n = n
      @tree = Array.new(n + 1, 0)
    end
    def add(i, delta)
      i += 1
      while i <= @n
        @tree[i] += delta
        i += i & -i
      end
    end
    def sum(i)
      i += 1
      res = 0
      while i > 0
        res += @tree[i]
        i -= i & -i
      end
      res
    end
  end

  bit = BIT.new(n)
  (0...n).each { |i| bit.add(i, 1) }

  ptrs = Array.new(10, 0)
  result = []

  while result.length < n
    (0..9).each do |d|
      idx_ptr = ptrs[d]
      arr = positions[d]
      next if idx_ptr >= arr.size
      idx = arr[idx_ptr]
      swaps_needed = bit.sum(idx) - 1
      if swaps_needed <= k
        result << d.to_s
        k -= swaps_needed
        bit.add(idx, -1)
        ptrs[d] += 1
        break
      end
    end
  end

  result.join
end
```

## Scala

```scala
object Solution {
  def minInteger(num: String, k: Int): String = {
    val n = num.length
    val pos = Array.fill(10)(new scala.collection.mutable.Queue[Int]())
    for (i <- 0 until n) {
      val d = num.charAt(i) - '0'
      pos(d).enqueue(i)
    }

    class BIT(val size: Int) {
      private val tree = new Array[Int](size + 2)
      def add(idx: Int, delta: Int): Unit = {
        var i = idx + 1
        while (i <= size) {
          tree(i) += delta
          i += i & -i
        }
      }
      def sum(idx: Int): Int = {
        var res = 0
        var i = idx + 1
        while (i > 0) {
          res += tree(i)
          i -= i & -i
        }
        res
      }
    }

    val bit = new BIT(n)
    for (i <- 0 until n) bit.add(i, 1)

    var remainingK: Long = k.toLong
    val sb = new StringBuilder

    while (sb.length < n) {
      var placed = false
      var d = 0
      while (d < 10 && !placed) {
        val q = pos(d)
        if (q.nonEmpty) {
          val idx = q.front
          val before = if (idx == 0) 0 else bit.sum(idx - 1)
          if (before.toLong <= remainingK) {
            q.dequeue()
            bit.add(idx, -1)
            sb.append(('0' + d).toChar)
            remainingK -= before
            placed = true
          }
        }
        d += 1
      }
    }

    sb.toString()
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

struct Fenwick {
    tree: Vec<i32>,
    n: usize,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { tree: vec![0; n + 1], n }
    }
    fn add(&mut self, mut idx: usize, delta: i32) {
        idx += 1;
        while idx <= self.n {
            self.tree[idx] += delta;
            idx += idx & (!idx + 1);
        }
    }
    fn sum(&self, mut idx: usize) -> i32 {
        let mut res = 0;
        idx += 1;
        while idx > 0 {
            res += self.tree[idx];
            idx &= idx - 1;
        }
        res
    }
}

impl Solution {
    pub fn min_integer(num: String, k: i32) -> String {
        let n = num.len();
        let bytes = num.as_bytes();

        // queues of positions for each digit
        let mut pos_queues: Vec<VecDeque<usize>> = vec![VecDeque::new(); 10];
        for (i, &b) in bytes.iter().enumerate() {
            let d = (b - b'0') as usize;
            pos_queues[d].push_back(i);
        }

        // Fenwick tree to track remaining characters
        let mut bit = Fenwick::new(n);
        for i in 0..n {
            bit.add(i, 1);
        }

        let mut answer = String::with_capacity(n);
        let mut k_rem: i64 = k as i64;

        for _ in 0..n {
            for d in 0..10 {
                if let Some(&pos) = pos_queues[d].front() {
                    // number of remaining characters before this position
                    let swaps_needed = (bit.sum(pos) - 1) as i64;
                    if swaps_needed <= k_rem {
                        k_rem -= swaps_needed;
                        answer.push((b'0' + d as u8) as char);
                        bit.add(pos, -1);
                        pos_queues[d].pop_front();
                        break;
                    }
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
#lang racket
(provide min-integer)

(define/contract (min-integer num k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length num))
         (bit (make-vector (+ n 2) 0))

         ;; BIT add: increase position idx (1‑based) by delta
         (bit-add!
          (lambda (idx delta)
            (let loop ((i idx))
              (when (<= i n)
                (vector-set! bit i (+ (vector-ref bit i) delta))
                (loop (+ i (bitwise-and i (- i))))))))

         ;; BIT prefix sum up to idx (1‑based)
         (bit-sum
          (lambda (idx)
            (let loop ((i idx) (s 0))
              (if (= i 0)
                  s
                  (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))))

    ;; count occurrences of each digit
    (define counts (make-vector 10 0))
    (for ([idx (in-range n)])
      (let* ((ch (string-ref num idx))
             (d (- (char->integer ch) 48)))
        (vector-set! counts d (+ (vector-ref counts d) 1))))

    ;; allocate position arrays per digit
    (define pos-arrays (make-vector 10 #f))
    (for ([d (in-range 10)])
      (vector-set! pos-arrays d (make-vector (vector-ref counts d) 0)))
    (define ptrs (make-vector 10 0))

    ;; fill position arrays
    (for ([idx (in-range n)])
      (let* ((ch (string-ref num idx))
             (d (- (char->integer ch) 48))
             (arr (vector-ref pos-arrays d))
             (p (vector-ref ptrs d)))
        (vector-set! arr p idx)
        (vector-set! ptrs d (+ p 1))))
    ;; reset pointers for processing
    (for ([d (in-range 10)]) (vector-set! ptrs d 0))

    (define res (make-string n))

    (let loop-i ((i 0) (k k))
      (when (< i n)
        (let find-digit ((d 0))
          (if (= d 10)
              (void) ; should never happen
              (let* ((ptr (vector-ref ptrs d))
                     (arr (vector-ref pos-arrays d)))
                (if (< ptr (vector-length arr))
                    (let* ((pos (vector-ref arr ptr))
                           (removed (bit-sum pos))          ; removals before pos
                           (effective (- pos removed))      ; current index among remaining
                           (need (- effective i)))           ; swaps needed
                      (if (<= need k)
                          (begin
                            (string-set! res i (integer->char (+ d 48)))
                            (bit-add! (+ pos 1) 1)          ; mark position as removed
                            (vector-set! ptrs d (+ ptr 1))
                            (loop-i (+ i 1) (- k need)))
                          (find-digit (+ d 1))))
                    (find-digit (+ d 1)))))))))
    res))
```

## Erlang

```erlang
-export([min_integer/2]).
-spec min_integer(Num :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
min_integer(Num, K) ->
    DigitsList = binary:bin_to_list(Num),
    N = length(DigitsList),
    DigitsArr = array:from_list(DigitsList),          % 1‑based index
    QueuesMap0 = build_queues(DigitsList, 1, #{}),   % positions are 1‑based
    QueuesMap = maps:map(fun(_Key, L) -> lists:reverse(L) end, QueuesMap0),
    Bit0 = init_bit(N),
    process(N, K, QueuesMap, Bit0, DigitsArr, []).

%% build map Digit -> list of positions (in order)
build_queues([], _Pos, Map) -> Map;
build_queues([D|Rest], Pos, Map) ->
    Prev = maps:get(D, Map, []),
    NewMap = maps:put(D, [Pos|Prev], Map),
    build_queues(Rest, Pos + 1, NewMap).

process(N, _K, _QueuesMap, _Bit, _DigitsArr, ResRev) when length(ResRev) == N ->
    list_to_binary(lists:reverse(ResRev));
process(_N, K, QueuesMap, Bit, DigitsArr, ResRev) when K =< 0 ->
    Remaining = get_remaining(Bit, DigitsArr, 1, array:size(DigitsArr), []),
    Final = lists:reverse(ResRev) ++ Remaining,
    list_to_binary(Final);
process(N, K, QueuesMap, Bit, DigitsArr, ResRev) ->
    case select_digit(K, QueuesMap, Bit, N) of
        {ok, Digit, Pos, NewQueues, NewBit, Used} ->
            process(N, K - Used, NewQueues, NewBit, DigitsArr, [Digit|ResRev]);
        none ->
            Remaining = get_remaining(Bit, DigitsArr, 1, array:size(DigitsArr), []),
            Final = lists:reverse(ResRev) ++ Remaining,
            list_to_binary(Final)
    end.

select_digit(K, QueuesMap, Bit, N) -> select_digit($0, K, QueuesMap, Bit, N).

select_digit(Digit, _K, _QueuesMap, _Bit, _N) when Digit > $9 ->
    none;
select_digit(Digit, K, QueuesMap, Bit, N) ->
    case maps:get(Digit, QueuesMap, []) of
        [] -> select_digit(Digit + 1, K, QueuesMap, Bit, N);
        [Pos|Rest] ->
            Swaps = bit_query(Pos - 1, Bit),
            if Swaps =< K ->
                    NewBit = bit_update(Pos, -1, Bit, N),
                    NewQueues = maps:put(Digit, Rest, QueuesMap),
                    {ok, Digit, Pos, NewQueues, NewBit, Swaps};
               true ->
                    select_digit(Digit + 1, K, QueuesMap, Bit, N)
            end
    end.

%% Binary Indexed Tree (Fenwick) helpers
lsb(I) -> I band (-I).

bit_query(0, _Bit) -> 0;
bit_query(Index, Bit) when Index > 0 ->
    Val = array:get(Index, Bit),
    Val + bit_query(Index - lsb(Index), Bit).

bit_update(Index, Delta, Bit, N) when Index =< N ->
    Cur = array:get(Index, Bit),
    NewBit = array:set(Index, Cur + Delta, Bit),
    bit_update(Index + lsb(Index), Delta, NewBit, N);
bit_update(_Index, _Delta, Bit, _N) -> Bit.

init_bit(N) -> init_bit(1, N, array:new(N+1, [{default,0}])).
init_bit(I, N, Bit) when I > N -> Bit;
init_bit(I, N, Bit) ->
    Bit1 = bit_update(I, 1, Bit, N),
    init_bit(I + 1, N, Bit1).

%% Collect remaining digits in original order
get_remaining(_Bit, _DigitsArr, Pos, N, Acc) when Pos > N -> lists:reverse(Acc);
get_remaining(Bit, DigitsArr, Pos, N, Acc) ->
    Present = (bit_query(Pos, Bit) - bit_query(Pos - 1, Bit)) == 1,
    if
        Present ->
            Digit = array:get(Pos, DigitsArr),
            get_remaining(Bit, DigitsArr, Pos + 1, N, [Digit|Acc]);
        true ->
            get_remaining(Bit, DigitsArr, Pos + 1, N, Acc)
    end.
```

## Elixir

```elixir
defmodule Fenwick do
  @spec new(non_neg_integer()) :: :array.array(integer())
  def new(size) do
    :array.new(size + 1, default: 0)
  end

  @spec add(:array.array(integer()), non_neg_integer(), integer()) :: :array.array(integer())
  def add(tree, idx, delta) do
    n = :array.size(tree) - 1
    i = idx + 1
    add_loop(tree, i, delta, n)
  end

  defp add_loop(tree, i, delta, n) when i <= n do
    val = :array.get(i, tree) + delta
    tree = :array.set(i, val, tree)
    add_loop(tree, i + (i &&& -i), delta, n)
  end

  defp add_loop(tree, _i, _delta, _n), do: tree

  @spec sum(:array.array(integer()), non_neg_integer()) :: integer()
  def sum(tree, idx) do
    i = idx + 1
    sum_loop(tree, i, 0)
  end

  defp sum_loop(_tree, i, acc) when i <= 0, do: acc

  defp sum_loop(tree, i, acc) do
    val = :array.get(i, tree)
    sum_loop(tree, i - (i &&& -i), acc + val)
  end

  @spec prefix_before(:array.array(integer()), non_neg_integer()) :: integer()
  def prefix_before(_tree, 0), do: 0
  def prefix_before(tree, idx), do: sum(tree, idx - 1)
end

defmodule Solution do
  @spec min_integer(num :: String.t(), k :: integer) :: String.t()
  def min_integer(num, k) do
    chars = String.to_charlist(num)
    n = length(chars)

    # build queues of positions per digit (as lists in increasing order)
    init_queues =
      0..9
      |> Enum.map(fn _ -> [] end)
      |> List.to_tuple()

    queues_filled =
      Enum.reduce(Enum.with_index(chars), init_queues, fn {c, idx}, qs ->
        d = c - ?0
        list = elem(qs, d)
        put_elem(qs, d, [idx | list])
      end)

    # reverse each list to get ascending order
    queues =
      0..9
      |> Enum.reduce(queues_filled, fn d, acc ->
        list = elem(acc, d) |> :lists.reverse()
        put_elem(acc, d, list)
      end)

    # Fenwick tree with all ones (all positions present)
    tree = Fenwick.new(n)

    tree =
      Enum.reduce(0..(n - 1), tree, fn i, acc ->
        Fenwick.add(acc, i, 1)
      end)

    {result_rev, _tree, _queues, _k} = build(n, [], tree, queues, k)
    result_rev |> Enum.reverse() |> to_string()
  end

  defp build(0, acc, tree, queues, k), do: {acc, tree, queues, k}

  defp build(remain, acc, tree, queues, k) do
    {digit, _pos, new_tree, new_queues, new_k} = find_and_remove(0, tree, queues, k)
    # prepend character (will reverse at the end)
    acc = [digit + ?0 | acc]
    build(remain - 1, acc, new_tree, new_queues, new_k)
  end

  defp find_and_remove(digit, tree, queues, k) when digit <= 9 do
    list = elem(queues, digit)

    case list do
      [] ->
        find_and_remove(digit + 1, tree, queues, k)

      [pos | rest] ->
        cost = Fenwick.prefix_before(tree, pos)

        if cost <= k do
          new_tree = Fenwick.add(tree, pos, -1)
          new_queues = put_elem(queues, digit, rest)
          {digit, pos, new_tree, new_queues, k - cost}
        else
          # cannot use this digit now; keep its list unchanged and try larger digits
          find_and_remove(digit + 1, tree, queues, k)
        end
    end
  end

  defp find_and_remove(_, _tree, _queues, _k) do
    raise "Unexpected state: no selectable digit found"
  end
end
```
