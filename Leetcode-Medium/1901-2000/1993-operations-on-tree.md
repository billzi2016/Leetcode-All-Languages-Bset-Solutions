# 1993. Operations on Tree

## Cpp

```cpp
class LockingTree {
public:
    LockingTree(std::vector<int>& parent) : parent(parent), lockedBy(parent.size(), -1) {
        int n = parent.size();
        children.assign(n, {});
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
    }
    
    bool lock(int num, int user) {
        if (lockedBy[num] != -1) return false;
        lockedBy[num] = user;
        return true;
    }
    
    bool unlock(int num, int user) {
        if (lockedBy[num] != user) return false;
        lockedBy[num] = -1;
        return true;
    }
    
    bool upgrade(int num, int user) {
        // check ancestors
        for (int cur = parent[num]; cur != -1; cur = parent[cur]) {
            if (lockedBy[cur] != -1) return false;
        }
        // collect locked descendants
        std::vector<int> toUnlock;
        dfsCollect(num, toUnlock);
        if (toUnlock.empty()) return false;
        // lock current node
        lockedBy[num] = user;
        // unlock all collected descendants
        for (int v : toUnlock) {
            lockedBy[v] = -1;
        }
        return true;
    }

private:
    std::vector<int> parent;
    std::vector<std::vector<int>> children;
    std::vector<int> lockedBy;
    
    void dfsCollect(int node, std::vector<int>& res) {
        for (int child : children[node]) {
            if (lockedBy[child] != -1) res.push_back(child);
            dfsCollect(child, res);
        }
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */
```

## Java

```java
class LockingTree {
    private int[] parent;
    private java.util.List<Integer>[] children;
    private int[] lockedBy;

    public LockingTree(int[] parent) {
        this.parent = parent.clone();
        int n = parent.length;
        children = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) {
            children[i] = new java.util.ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            children[parent[i]].add(i);
        }
        lockedBy = new int[n];
        java.util.Arrays.fill(lockedBy, -1);
    }

    public boolean lock(int num, int user) {
        if (lockedBy[num] != -1) return false;
        lockedBy[num] = user;
        return true;
    }

    public boolean unlock(int num, int user) {
        if (lockedBy[num] != user) return false;
        lockedBy[num] = -1;
        return true;
    }

    public boolean upgrade(int num, int user) {
        if (lockedBy[num] != -1) return false;

        // check ancestors
        int cur = parent[num];
        while (cur != -1) {
            if (lockedBy[cur] != -1) return false;
            cur = parent[cur];
        }

        java.util.List<Integer> lockedDescendants = new java.util.ArrayList<>();
        collectLocked(num, lockedDescendants);
        if (lockedDescendants.isEmpty()) return false;

        for (int node : lockedDescendants) {
            lockedBy[node] = -1;
        }
        lockedBy[num] = user;
        return true;
    }

    private void collectLocked(int node, java.util.List<Integer> list) {
        for (int child : children[node]) {
            if (lockedBy[child] != -1) {
                list.add(child);
            }
            collectLocked(child, list);
        }
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * boolean param_1 = obj.lock(num,user);
 * boolean param_2 = obj.unlock(num,user);
 * boolean param_3 = obj.upgrade(num,user);
 */
```

## Python

```python
class LockingTree(object):
    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        n = len(parent)
        self.locked = [-1] * n  # -1 means unlocked, otherwise stores user id
        self.children = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        # node must be unlocked
        if self.locked[num] != -1:
            return False
        # no locked ancestors
        cur = self.parent[num]
        while cur != -1:
            if self.locked[cur] != -1:
                return False
            cur = self.parent[cur]

        # collect locked descendants
        stack = self.children[num][:]
        locked_descendants = []
        while stack:
            node = stack.pop()
            if self.locked[node] != -1:
                locked_descendants.append(node)
            stack.extend(self.children[node])

        if not locked_descendants:
            return False

        # lock current node
        self.locked[num] = user
        # unlock all locked descendants
        for d in locked_descendants:
            self.locked[d] = -1
        return True
```

## Python3

```python
class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        n = len(parent)
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)
        self.locked_by = [-1] * n

    def lock(self, num, user):
        if self.locked_by[num] == -1:
            self.locked_by[num] = user
            return True
        return False

    def unlock(self, num, user):
        if self.locked_by[num] == user:
            self.locked_by[num] = -1
            return True
        return False

    def upgrade(self, num, user):
        # node must be unlocked
        if self.locked_by[num] != -1:
            return False
        # no locked ancestors
        cur = self.parent[num]
        while cur != -1:
            if self.locked_by[cur] != -1:
                return False
            cur = self.parent[cur]
        # collect locked descendants
        stack = [num]
        locked_descendants = []
        while stack:
            node = stack.pop()
            for child in self.children[node]:
                if self.locked_by[child] != -1:
                    locked_descendants.append(child)
                stack.append(child)
        if not locked_descendants:
            return False
        # unlock all descendants and lock current node
        for d in locked_descendants:
            self.locked_by[d] = -1
        self.locked_by[num] = user
        return True
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int n;
    int *parent;
    int **children;
    int *childCnt;
    int *lockedBy;
} LockingTree;

LockingTree* lockingTreeCreate(int* parent, int parentSize) {
    LockingTree* obj = (LockingTree*)malloc(sizeof(LockingTree));
    obj->n = parentSize;
    obj->parent = (int*)malloc(parentSize * sizeof(int));
    memcpy(obj->parent, parent, parentSize * sizeof(int));

    obj->childCnt = (int*)calloc(parentSize, sizeof(int));
    for (int i = 0; i < parentSize; ++i) {
        int p = parent[i];
        if (p != -1) obj->childCnt[p]++;
    }

    obj->children = (int**)malloc(parentSize * sizeof(int*));
    for (int i = 0; i < parentSize; ++i) {
        if (obj->childCnt[i] > 0)
            obj->children[i] = (int*)malloc(obj->childCnt[i] * sizeof(int));
        else
            obj->children[i] = NULL;
    }

    int* idx = (int*)calloc(parentSize, sizeof(int));
    for (int i = 0; i < parentSize; ++i) {
        int p = parent[i];
        if (p != -1) {
            int pos = idx[p]++;
            obj->children[p][pos] = i;
        }
    }
    free(idx);

    obj->lockedBy = (int*)calloc(parentSize, sizeof(int));
    return obj;
}

bool lockingTreeLock(LockingTree* obj, int num, int user) {
    if (obj->lockedBy[num] != 0) return false;
    obj->lockedBy[num] = user;
    return true;
}

bool lockingTreeUnlock(LockingTree* obj, int num, int user) {
    if (obj->lockedBy[num] == user) {
        obj->lockedBy[num] = 0;
        return true;
    }
    return false;
}

bool lockingTreeUpgrade(LockingTree* obj, int num, int user) {
    if (obj->lockedBy[num] != 0) return false;

    for (int cur = obj->parent[num]; cur != -1; cur = obj->parent[cur]) {
        if (obj->lockedBy[cur] != 0) return false;
    }

    int* toUnlock = (int*)malloc(obj->n * sizeof(int));
    int cnt = 0;

    int* stack = (int*)malloc(obj->n * sizeof(int));
    int top = 0;
    for (int i = 0; i < obj->childCnt[num]; ++i) {
        stack[top++] = obj->children[num][i];
    }

    while (top) {
        int u = stack[--top];
        if (obj->lockedBy[u] != 0) {
            toUnlock[cnt++] = u;
        }
        for (int i = 0; i < obj->childCnt[u]; ++i) {
            stack[top++] = obj->children[u][i];
        }
    }

    if (cnt == 0) {
        free(toUnlock);
        free(stack);
        return false;
    }

    obj->lockedBy[num] = user;
    for (int i = 0; i < cnt; ++i) {
        obj->lockedBy[toUnlock[i]] = 0;
    }

    free(toUnlock);
    free(stack);
    return true;
}

void lockingTreeFree(LockingTree* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; ++i) {
        if (obj->children[i]) free(obj->children[i]);
    }
    free(obj->children);
    free(obj->childCnt);
    free(obj->parent);
    free(obj->lockedBy);
    free(obj);
}
```

## Csharp

```csharp
public class LockingTree
{
    private readonly int[] _parent;
    private readonly List<int>[] _children;
    private readonly int[] _lockedBy; // 0 means unlocked

    public LockingTree(int[] parent)
    {
        _parent = parent;
        int n = parent.Length;
        _children = new List<int>[n];
        for (int i = 0; i < n; i++) _children[i] = new List<int>();
        for (int i = 1; i < n; i++)
        {
            int p = parent[i];
            _children[p].Add(i);
        }
        _lockedBy = new int[n]; // all zero initially
    }

    public bool Lock(int num, int user)
    {
        if (_lockedBy[num] == 0)
        {
            _lockedBy[num] = user;
            return true;
        }
        return false;
    }

    public bool Unlock(int num, int user)
    {
        if (_lockedBy[num] == user)
        {
            _lockedBy[num] = 0;
            return true;
        }
        return false;
    }

    public bool Upgrade(int num, int user)
    {
        if (_lockedBy[num] != 0) return false; // already locked

        // check ancestors
        int cur = _parent[num];
        while (cur != -1)
        {
            if (_lockedBy[cur] != 0) return false;
            cur = _parent[cur];
        }

        var lockedDescendants = new List<int>();
        CollectLocked(num, lockedDescendants);
        if (lockedDescendants.Count == 0) return false;

        foreach (int v in lockedDescendants)
        {
            _lockedBy[v] = 0;
        }
        _lockedBy[num] = user;
        return true;
    }

    private void CollectLocked(int node, List<int> list)
    {
        foreach (int child in _children[node])
        {
            if (_lockedBy[child] != 0) list.Add(child);
            CollectLocked(child, list);
        }
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = new LockingTree(parent);
 * bool param_1 = obj.Lock(num,user);
 * bool param_2 = obj.Unlock(num,user);
 * bool param_3 = obj.Upgrade(num,user);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} parent
 */
var LockingTree = function(parent) {
    this.parent = parent;
    this.n = parent.length;
    this.locked = new Array(this.n).fill(0); // 0 means unlocked, otherwise stores user id
    this.children = Array.from({ length: this.n }, () => []);
    for (let i = 1; i < this.n; i++) {
        const p = parent[i];
        this.children[p].push(i);
    }
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.lock = function(num, user) {
    if (this.locked[num] === 0) {
        this.locked[num] = user;
        return true;
    }
    return false;
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.unlock = function(num, user) {
    if (this.locked[num] === user) {
        this.locked[num] = 0;
        return true;
    }
    return false;
};

/** 
 * @param {number} num 
 * @param {number} user
 * @return {boolean}
 */
LockingTree.prototype.upgrade = function(num, user) {
    // node must be unlocked
    if (this.locked[num] !== 0) return false;

    // no locked ancestors
    let cur = this.parent[num];
    while (cur !== -1) {
        if (this.locked[cur] !== 0) return false;
        cur = this.parent[cur];
    }

    // find locked descendants
    const stack = [num];
    const toUnlock = [];
    let hasLockedDescendant = false;

    while (stack.length) {
        const node = stack.pop();
        for (const child of this.children[node]) {
            if (this.locked[child] !== 0) {
                hasLockedDescendant = true;
                toUnlock.push(child);
            }
            stack.push(child);
        }
    }

    if (!hasLockedDescendant) return false;

    // unlock all locked descendants
    for (const d of toUnlock) {
        this.locked[d] = 0;
    }

    // lock the current node
    this.locked[num] = user;
    return true;
};

/** 
 * Your LockingTree object will be instantiated and called as such:
 * var obj = new LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */
```

## Typescript

```typescript
class LockingTree {
    private parent: number[];
    private children: number[][];
    private locked: number[];

    constructor(parent: number[]) {
        this.parent = parent;
        const n = parent.length;
        this.children = Array.from({ length: n }, () => []);
        for (let i = 1; i < n; i++) {
            const p = parent[i];
            if (p !== -1) this.children[p].push(i);
        }
        this.locked = new Array(n).fill(0); // 0 means unlocked, otherwise user id
    }

    lock(num: number, user: number): boolean {
        if (this.locked[num] !== 0) return false;
        this.locked[num] = user;
        return true;
    }

    unlock(num: number, user: number): boolean {
        if (this.locked[num] !== user) return false;
        this.locked[num] = 0;
        return true;
    }

    upgrade(num: number, user: number): boolean {
        // node must be unlocked
        if (this.locked[num] !== 0) return false;

        // no ancestor locked
        let p = this.parent[num];
        while (p !== -1) {
            if (this.locked[p] !== 0) return false;
            p = this.parent[p];
        }

        // collect locked descendants
        const toUnlock: number[] = [];
        const stack: number[] = [num];
        while (stack.length) {
            const cur = stack.pop()!;
            for (const child of this.children[cur]) {
                if (this.locked[child] !== 0) {
                    toUnlock.push(child);
                }
                stack.push(child);
            }
        }

        if (toUnlock.length === 0) return false;

        // unlock all descendants
        for (const node of toUnlock) {
            this.locked[node] = 0;
        }

        // lock current node
        this.locked[num] = user;
        return true;
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * var obj = new LockingTree(parent)
 * var param_1 = obj.lock(num,user)
 * var param_2 = obj.unlock(num,user)
 * var param_3 = obj.upgrade(num,user)
 */
```

## Php

```php
class LockingTree {
    private $parent;
    private $children = [];
    private $lockedUser = [];

    /**
     * @param Integer[] $parent
     */
    function __construct($parent) {
        $this->parent = $parent;
        $n = count($parent);
        $this->lockedUser = array_fill(0, $n, -1);
        $this->children = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $p = $parent[$i];
            if ($p != -1) {
                $this->children[$p][] = $i;
            }
        }
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function lock($num, $user) {
        if ($this->lockedUser[$num] == -1) {
            $this->lockedUser[$num] = $user;
            return true;
        }
        return false;
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function unlock($num, $user) {
        if ($this->lockedUser[$num] == $user) {
            $this->lockedUser[$num] = -1;
            return true;
        }
        return false;
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function upgrade($num, $user) {
        if ($this->lockedUser[$num] != -1) {
            return false;
        }
        // check ancestors
        $p = $this->parent[$num];
        while ($p != -1) {
            if ($this->lockedUser[$p] != -1) {
                return false;
            }
            $p = $this->parent[$p];
        }
        // collect locked descendants
        $lockedDesc = [];
        $this->collectLockedDescendants($num, $lockedDesc);
        if (empty($lockedDesc)) {
            return false;
        }
        // unlock all descendants
        foreach ($lockedDesc as $node) {
            $this->lockedUser[$node] = -1;
        }
        // lock current node
        $this->lockedUser[$num] = $user;
        return true;
    }

    private function collectLockedDescendants($node, &$list) {
        foreach ($this->children[$node] as $child) {
            if ($this->lockedUser[$child] != -1) {
                $list[] = $child;
            }
            $this->collectLockedDescendants($child, $list);
        }
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * $obj = new LockingTree($parent);
 * $ret_1 = $obj->lock($num, $user);
 * $ret_2 = $obj->unlock($num, $user);
 * $ret_3 = $obj->upgrade($num, $user);
 */
```

## Swift

```swift
class LockingTree {
    private var parent: [Int]
    private var children: [[Int]]
    private var lockedBy: [Int]

    init(_ parent: [Int]) {
        self.parent = parent
        let n = parent.count
        self.children = Array(repeating: [], count: n)
        for i in 0..<n {
            let p = parent[i]
            if p != -1 {
                children[p].append(i)
            }
        }
        self.lockedBy = Array(repeating: -1, count: n)
    }

    func lock(_ num: Int, _ user: Int) -> Bool {
        if lockedBy[num] == -1 {
            lockedBy[num] = user
            return true
        }
        return false
    }

    func unlock(_ num: Int, _ user: Int) -> Bool {
        if lockedBy[num] == user {
            lockedBy[num] = -1
            return true
        }
        return false
    }

    func upgrade(_ num: Int, _ user: Int) -> Bool {
        // Node must be unlocked
        if lockedBy[num] != -1 { return false }
        // No ancestor should be locked
        var cur = parent[num]
        while cur != -1 {
            if lockedBy[cur] != -1 { return false }
            cur = parent[cur]
        }
        // Find all locked descendants
        var stack = [num]
        var lockedDescendants: [Int] = []
        while let node = stack.popLast() {
            for child in children[node] {
                if lockedBy[child] != -1 {
                    lockedDescendants.append(child)
                }
                stack.append(child)
            }
        }
        if lockedDescendants.isEmpty { return false }
        // Unlock all descendants
        for d in lockedDescendants {
            lockedBy[d] = -1
        }
        // Lock the current node
        lockedBy[num] = user
        return true
    }
}
```

## Kotlin

```kotlin
class LockingTree(parent: IntArray) {
    private val parent = parent
    private val children = Array(parent.size) { mutableListOf<Int>() }
    private val lockUser = IntArray(parent.size)

    init {
        for (i in 1 until parent.size) {
            val p = parent[i]
            children[p].add(i)
        }
    }

    fun lock(num: Int, user: Int): Boolean {
        if (lockUser[num] == 0) {
            lockUser[num] = user
            return true
        }
        return false
    }

    fun unlock(num: Int, user: Int): Boolean {
        if (lockUser[num] == user) {
            lockUser[num] = 0
            return true
        }
        return false
    }

    fun upgrade(num: Int, user: Int): Boolean {
        if (lockUser[num] != 0) return false

        var cur = parent[num]
        while (cur != -1) {
            if (lockUser[cur] != 0) return false
            cur = parent[cur]
        }

        val stack = java.util.ArrayDeque<Int>()
        stack.add(num)
        var foundLocked = false
        val toUnlock = mutableListOf<Int>()

        while (!stack.isEmpty()) {
            val node = stack.removeLast()
            for (child in children[node]) {
                if (lockUser[child] != 0) {
                    foundLocked = true
                    toUnlock.add(child)
                }
                stack.add(child)
            }
        }

        if (!foundLocked) return false

        for (d in toUnlock) {
            lockUser[d] = 0
        }
        lockUser[num] = user
        return true
    }
}
```

## Dart

```dart
class LockingTree {
  late List<int> _parent;
  late List<List<int>> _children;
  late List<int> _lockedBy;

  LockingTree(List<int> parent) {
    int n = parent.length;
    _parent = parent;
    _children = List.generate(n, (_) => []);
    for (int i = 0; i < n; i++) {
      int p = parent[i];
      if (p != -1) {
        _children[p].add(i);
      }
    }
    _lockedBy = List.filled(n, -1);
  }

  bool lock(int num, int user) {
    if (_lockedBy[num] == -1) {
      _lockedBy[num] = user;
      return true;
    }
    return false;
  }

  bool unlock(int num, int user) {
    if (_lockedBy[num] == user) {
      _lockedBy[num] = -1;
      return true;
    }
    return false;
  }

  bool upgrade(int num, int user) {
    // node must be unlocked
    if (_lockedBy[num] != -1) return false;

    // no locked ancestors
    int cur = _parent[num];
    while (cur != -1) {
      if (_lockedBy[cur] != -1) return false;
      cur = _parent[cur];
    }

    // find locked descendants
    List<int> toUnlock = [];
    bool hasLocked = false;
    List<int> stack = List.from(_children[num]);
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      if (_lockedBy[node] != -1) {
        hasLocked = true;
        toUnlock.add(node);
      }
      if (_children[node].isNotEmpty) {
        stack.addAll(_children[node]);
      }
    }

    if (!hasLocked) return false;

    // lock the current node and unlock all descendants
    _lockedBy[num] = user;
    for (int d in toUnlock) {
      _lockedBy[d] = -1;
    }
    return true;
  }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree obj = LockingTree(parent);
 * bool param1 = obj.lock(num,user);
 * bool param2 = obj.unlock(num,user);
 * bool param3 = obj.upgrade(num,user);
 */
```

## Golang

```go
type LockingTree struct {
	parent   []int
	children [][]int
	lockUser []int
}

func Constructor(parent []int) LockingTree {
	n := len(parent)
	children := make([][]int, n)
	for i, p := range parent {
		if p != -1 {
			children[p] = append(children[p], i)
		}
	}
	lockUser := make([]int, n)
	for i := 0; i < n; i++ {
		lockUser[i] = -1
	}
	return LockingTree{
		parent:   parent,
		children: children,
		lockUser: lockUser,
	}
}

func (this *LockingTree) Lock(num int, user int) bool {
	if this.lockUser[num] != -1 {
		return false
	}
	this.lockUser[num] = user
	return true
}

func (this *LockingTree) Unlock(num int, user int) bool {
	if this.lockUser[num] != user {
		return false
	}
	this.lockUser[num] = -1
	return true
}

func (this *LockingTree) Upgrade(num int, user int) bool {
	if this.lockUser[num] != -1 {
		return false
	}
	// check ancestors
	for p := this.parent[num]; p != -1; p = this.parent[p] {
		if this.lockUser[p] != -1 {
			return false
		}
	}
	// find locked descendants
	var lockedDesc []int
	stack := []int{num}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, child := range this.children[cur] {
			if this.lockUser[child] != -1 {
				lockedDesc = append(lockedDesc, child)
			}
			stack = append(stack, child)
		}
	}
	if len(lockedDesc) == 0 {
		return false
	}
	// unlock all locked descendants
	for _, node := range lockedDesc {
		this.lockUser[node] = -1
	}
	// lock current node
	this.lockUser[num] = user
	return true
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * obj := Constructor(parent);
 * param_1 := obj.Lock(num,user);
 * param_2 := obj.Unlock(num,user);
 * param_3 := obj.Upgrade(num,user);
 */
```

## Ruby

```ruby
class LockingTree
  def initialize(parent)
    @parent = parent
    n = parent.length
    @children = Array.new(n) { [] }
    (1...n).each do |i|
      p = parent[i]
      @children[p] << i
    end
    @locked_by = Array.new(n, -1)
  end

  def lock(num, user)
    if @locked_by[num] == -1
      @locked_by[num] = user
      true
    else
      false
    end
  end

  def unlock(num, user)
    if @locked_by[num] == user
      @locked_by[num] = -1
      true
    else
      false
    end
  end

  def upgrade(num, user)
    return false unless @locked_by[num] == -1

    cur = @parent[num]
    while cur != -1
      return false if @locked_by[cur] != -1
      cur = @parent[cur]
    end

    locked_descendants = []
    stack = [num]
    until stack.empty?
      node = stack.pop
      @children[node].each do |child|
        locked_descendants << child if @locked_by[child] != -1
        stack << child
      end
    end

    return false if locked_descendants.empty?

    locked_descendants.each { |d| @locked_by[d] = -1 }
    @locked_by[num] = user
    true
  end
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, Stack}

class LockingTree(_parent: Array[Int]) {

  private val n: Int = _parent.length
  private val children: Array[ArrayBuffer[Int]] = Array.fill(n)(ArrayBuffer[Int]())
  private val locked: Array[Int] = Array.ofDim[Int](n) // 0 means unlocked

  // build adjacency list of children
  for (i <- 1 until n) {
    val p = _parent(i)
    children(p).append(i)
  }

  def lock(num: Int, user: Int): Boolean = {
    if (locked(num) != 0) false
    else {
      locked(num) = user
      true
    }
  }

  def unlock(num: Int, user: Int): Boolean = {
    if (locked(num) == user) {
      locked(num) = 0
      true
    } else false
  }

  def upgrade(num: Int, user: Int): Boolean = {
    // node must be unlocked
    if (locked(num) != 0) return false

    // no ancestor should be locked
    var cur = _parent(num)
    while (cur != -1) {
      if (locked(cur) != 0) return false
      cur = _parent(cur)
    }

    // collect all locked descendants
    val toUnlock = ArrayBuffer[Int]()
    val stack = Stack[Int]()
    stack.push(num)

    while (stack.nonEmpty) {
      val node = stack.pop()
      for (child <- children(node)) {
        if (locked(child) != 0) toUnlock.append(child)
        stack.push(child)
      }
    }

    if (toUnlock.isEmpty) return false

    // unlock all descendants
    for (d <- toUnlock) locked(d) = 0

    // lock the current node
    locked(num) = user
    true
  }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * val obj = new LockingTree(parent)
 * val param_1 = obj.lock(num,user)
 * val param_2 = obj.unlock(num,user)
 * val param_3 = obj.upgrade(num,user)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct LockingTree {
    parent: Vec<i32>,
    children: Vec<Vec<usize>>,
    lock_user: RefCell<Vec<Option<i32>>>,
}

impl LockingTree {
    fn new(parent: Vec<i32>) -> Self {
        let n = parent.len();
        let mut children = vec![Vec::new(); n];
        for i in 0..n {
            let p = parent[i];
            if p != -1 {
                children[p as usize].push(i);
            }
        }
        LockingTree {
            parent,
            children,
            lock_user: RefCell::new(vec![None; n]),
        }
    }

    fn lock(&self, num: i32, user: i32) -> bool {
        let idx = num as usize;
        let mut locks = self.lock_user.borrow_mut();
        if locks[idx].is_none() {
            locks[idx] = Some(user);
            true
        } else {
            false
        }
    }

    fn unlock(&self, num: i32, user: i32) -> bool {
        let idx = num as usize;
        let mut locks = self.lock_user.borrow_mut();
        if let Some(u) = locks[idx] {
            if u == user {
                locks[idx] = None;
                return true;
            }
        }
        false
    }

    fn upgrade(&self, num: i32, user: i32) -> bool {
        let idx = num as usize;

        // Check ancestors are not locked
        let mut cur = self.parent[idx];
        while cur != -1 {
            if self.lock_user.borrow()[cur as usize].is_some() {
                return false;
            }
            cur = self.parent[cur as usize];
        }

        // Find locked descendants
        let mut stack = vec![idx];
        let mut locked_descendants = Vec::new();
        while let Some(node) = stack.pop() {
            for &child in &self.children[node] {
                if self.lock_user.borrow()[child].is_some() {
                    locked_descendants.push(child);
                }
                stack.push(child);
            }
        }

        // Must have at least one locked descendant and the node itself must be unlocked
        if locked_descendants.is_empty() || self.lock_user.borrow()[idx].is_some() {
            return false;
        }

        // Unlock all descendants and lock current node
        let mut locks = self.lock_user.borrow_mut();
        for d in locked_descendants {
            locks[d] = None;
        }
        locks[idx] = Some(user);
        true
    }
}

/**
 * Your LockingTree object will be instantiated and called as such:
 * let obj = LockingTree::new(parent);
 * let ret_1: bool = obj.lock(num, user);
 * let ret_2: bool = obj.unlock(num, user);
 * let ret_3: bool = obj.upgrade(num, user);
 */
```

## Racket

```racket
(define locking-tree%
  (class object%
    (super-new)

    (init-field parent) ; list of parents

    ;; internal data structures
    (define parent-vec (list->vector parent))
    (define n (vector-length parent-vec))
    (define lockStatus (make-vector n -1))          ; -1 means unlocked, otherwise user id
    (define children (make-vector n '()))           ; adjacency list of children

    ;; build children lists
    (for ([i (in-range n)])
      (let ([p (vector-ref parent-vec i)])
        (when (>= p 0)
          (vector-set! children p (cons i (vector-ref children p))))))

    ;; lock operation
    (define/public (lock num user)
      (if (= (vector-ref lockStatus num) -1)
          (begin
            (vector-set! lockStatus num user)
            #t)
          #f))

    ;; unlock operation
    (define/public (unlock num user)
      (if (= (vector-ref lockStatus num) user)
          (begin
            (vector-set! lockStatus num -1)
            #t)
          #f))

    ;; upgrade operation
    (define/public (upgrade num user)
      ;; node must be currently unlocked
      (if (not (= (vector-ref lockStatus num) -1))
          #f
          (let loop-anc ([cur (vector-ref parent-vec num)])
            (if (< cur 0)
                ;; no locked ancestors, now check descendants
                (let collect ((stack (vector-ref children num)) (acc '()))
                  (if (null? stack)
                      (if (null? acc)
                          #f
                          (begin
                            (for ([node acc])
                              (vector-set! lockStatus node -1))
                            (vector-set! lockStatus num user)
                            #t))
                      (let* ([node (car stack)]
                             [rest (cdr stack)])
                        (if (= (vector-ref lockStatus node) -1)
                            (collect (append (vector-ref children node) rest) acc)
                            (collect (append (vector-ref children node) rest) (cons node acc))))))
                (if (not (= (vector-ref lockStatus cur) -1))
                    #f
                    (loop-anc (vector-ref parent-vec cur))))))))
```

## Erlang

```erlang
-module(solution).
-export([locking_tree_init_/1,
         locking_tree_lock/2,
         locking_tree_unlock/2,
         locking_tree_upgrade/2]).

-spec locking_tree_init_(Parent :: [integer()]) -> any().
locking_tree_init_(Parent) ->
    N = length(Parent),
    EmptyMap = maps:from_list(lists:zip(lists:seq(0, N-1), lists:duplicate(N, []))),
    Children = build_children(Parent, EmptyMap, 0),
    Locks = #{},
    put(state, {Parent, Children, Locks}),
    ok.

-spec locking_tree_lock(Num :: integer(), User :: integer()) -> boolean().
locking_tree_lock(Num, User) ->
    State = get(state),
    Locks = element(3, State),
    case maps:is_key(Num, Locks) of
        true -> false;
        false ->
            NewLocks = maps:put(Num, User, Locks),
            put(state, setelement(3, State, NewLocks)),
            true
    end.

-spec locking_tree_unlock(Num :: integer(), User :: integer()) -> boolean().
locking_tree_unlock(Num, User) ->
    State = get(state),
    Locks = element(3, State),
    case maps:find(Num, Locks) of
        {ok, User} ->
            NewLocks = maps:remove(Num, Locks),
            put(state, setelement(3, State, NewLocks)),
            true;
        _ -> false
    end.

-spec locking_tree_upgrade(Num :: integer(), User :: integer()) -> boolean().
locking_tree_upgrade(Num, User) ->
    State = get(state),
    Parent = element(1, State),
    Children = element(2, State),
    Locks = element(3, State),

    case maps:is_key(Num, Locks) of
        true -> false;
        false ->
            case has_locked_ancestor(Num, Parent, Locks) of
                true -> false;
                false ->
                    LockedDesc = collect_locked_descendants(Num, Children, Locks),
                    case LockedDesc of
                        [] -> false;
                        _ ->
                            NewLocks0 = lists:foldl(fun(Nd, Acc) -> maps:remove(Nd, Acc) end,
                                                    Locks, LockedDesc),
                            NewLocks = maps:put(Num, User, NewLocks0),
                            put(state, setelement(3, State, NewLocks)),
                            true
                    end
            end
    end.

%% Helper to build children map
build_children([], Map, _Idx) -> Map;
build_children([P|Rest], Map, Idx) ->
    UpdatedMap = case P of
        -1 -> Map;
        _ ->
            OldChildren = maps:get(P, Map),
            maps:put(P, [Idx | OldChildren], Map)
    end,
    build_children(Rest, UpdatedMap, Idx + 1).

%% Check if any ancestor is locked
has_locked_ancestor(Num, Parent, Locks) ->
    case lists:nth(Num + 1, Parent) of
        -1 -> false;
        P ->
            case maps:is_key(P, Locks) of
                true -> true;
                false -> has_locked_ancestor(P, Parent, Locks)
            end
    end.

%% Collect all locked descendants (excluding the node itself)
collect_locked_descendants(Node, ChildrenMap, Locks) ->
    ChildList = maps:get(Node, ChildrenMap, []),
    lists:foldl(fun(Child, Acc) ->
        Acc1 = case maps:is_key(Child, Locks) of
                   true -> [Child | Acc];
                   false -> Acc
               end,
        Desc = collect_locked_descendants(Child, ChildrenMap, Locks),
        Acc1 ++ Desc
    end, [], ChildList).
```

## Elixir

```elixir
defmodule LockingTree do
  @spec init_(parent :: [integer]) :: any
  def init_(parent) do
    n = length(parent)

    children =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        p = Enum.at(parent, i)

        if p != -1 do
          Map.update(acc, p, [i], fn list -> [i | list] end)
        else
          acc
        end
      end)

    lock =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, i, 0)
      end)

    Process.put(:locking_tree_state, %{parent: parent, children: children, lock: lock})
  end

  @spec lock(num :: integer, user :: integer) :: boolean
  def lock(num, user) do
    state = Process.get(:locking_tree_state)
    lock_map = state.lock

    if Map.get(lock_map, num) == 0 do
      new_lock = Map.put(lock_map, num, user)
      Process.put(:locking_tree_state, %{state | lock: new_lock})
      true
    else
      false
    end
  end

  @spec unlock(num :: integer, user :: integer) :: boolean
  def unlock(num, user) do
    state = Process.get(:locking_tree_state)
    lock_map = state.lock

    case Map.get(lock_map, num) do
      ^user ->
        new_lock = Map.put(lock_map, num, 0)
        Process.put(:locking_tree_state, %{state | lock: new_lock})
        true

      _ ->
        false
    end
  end

  @spec upgrade(num :: integer, user :: integer) :: boolean
  def upgrade(num, user) do
    state = Process.get(:locking_tree_state)
    lock_map = state.lock

    # node must be unlocked
    if Map.get(lock_map, num) != 0 do
      false
    else
      # no locked ancestors
      if has_locked_ancestor?(num, state.parent, lock_map) do
        false
      else
        locked_descendants = collect_locked_descendants(num, state.children, lock_map, [])

        if locked_descendants == [] do
          false
        else
          new_lock =
            Enum.reduce(locked_descendants, lock_map, fn d, acc ->
              Map.put(acc, d, 0)
            end)

          new_lock = Map.put(new_lock, num, user)
          Process.put(:locking_tree_state, %{state | lock: new_lock})
          true
        end
      end
    end
  end

  defp has_locked_ancestor?(node, parent_arr, lock_map) do
    p = Enum.at(parent_arr, node)

    cond do
      p == -1 ->
        false

      Map.get(lock_map, p) != 0 ->
        true

      true ->
        has_locked_ancestor?(p, parent_arr, lock_map)
    end
  end

  defp collect_locked_descendants(node, children, lock_map, acc) do
    child_nodes = Map.get(children, node, [])

    Enum.reduce(child_nodes, acc, fn child, a ->
      a = if Map.get(lock_map, child) != 0, do: [child | a], else: a
      collect_locked_descendants(child, children, lock_map, a)
    end)
  end
end
```
