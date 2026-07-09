# 0427. Construct Quad Tree

## Cpp

```cpp
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};

class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        int n = grid.size();
        return build(grid, 0, 0, n);
    }
private:
    Node* build(const vector<vector<int>>& g, int x, int y, int len) {
        bool first = g[x][y];
        bool same = true;
        for (int i = x; i < x + len && same; ++i) {
            for (int j = y; j < y + len; ++j) {
                if (g[i][j] != first) {
                    same = false;
                    break;
                }
            }
        }
        if (same) {
            return new Node(first, true);
        }
        int half = len / 2;
        Node* tl = build(g, x, y, half);
        Node* tr = build(g, x, y + half, half);
        Node* bl = build(g, x + half, y, half);
        Node* br = build(g, x + half, y + half, half);
        return new Node(true, false, tl, tr, bl, br);
    }
};
```

## Java

```java
/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}
*/

class Solution {
    public Node construct(int[][] grid) {
        int n = grid.length;
        return build(grid, 0, 0, n);
    }

    private Node build(int[][] grid, int row, int col, int size) {
        if (size == 1) {
            boolean val = grid[row][col] == 1;
            return new Node(val, true);
        }
        int half = size / 2;
        Node topLeft = build(grid, row, col, half);
        Node topRight = build(grid, row, col + half, half);
        Node bottomLeft = build(grid, row + half, col, half);
        Node bottomRight = build(grid, row + half, col + half, half);

        // If all four children are leaves and have the same value, merge them.
        if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf) {
            boolean v = topLeft.val;
            if (topRight.val == v && bottomLeft.val == v && bottomRight.val == v) {
                return new Node(v, true);
            }
        }

        // Otherwise, create an internal node.
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}
```

## Python

```python
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)

        def build(r, c, size):
            # Check if all values in the current subgrid are identical
            first = grid[r][c]
            same = True
            for i in range(r, r + size):
                if not same:
                    break
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
            if same:
                return Node(val=bool(first), isLeaf=True)
            half = size // 2
            tl = build(r, c, half)
            tr = build(r, c + half, half)
            bl = build(r + half, c, half)
            br = build(r + half, c + half, half)
            return Node(val=True, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl, bottomRight=br)

        return build(0, 0, n)
```

## Python3

```python
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(r: int, c: int, size: int) -> Node:
            if size == 1:
                v = bool(grid[r][c])
                return Node(v, True, None, None, None, None)
            half = size // 2
            tl = build(r, c, half)
            tr = build(r, c + half, half)
            bl = build(r + half, c, half)
            br = build(r + half, c + half, half)

            # If all four children are leaves and have same value, merge them.
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
                tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)
            else:
                # For internal nodes, val can be arbitrary; set to True.
                return Node(True, False, tl, tr, bl, br)

        return build(0, 0, n)
```

## Csharp

```csharp
using System;

public class Solution {
    public Node Construct(int[][] grid) {
        int n = grid.Length;
        return Build(grid, 0, 0, n);
    }
    
    private Node Build(int[][] grid, int row, int col, int size) {
        if (size == 1) {
            bool val = grid[row][col] == 1;
            return new Node(val, true);
        }
        
        bool same = true;
        int firstVal = grid[row][col];
        for (int i = row; i < row + size && same; i++) {
            for (int j = col; j < col + size; j++) {
                if (grid[i][j] != firstVal) {
                    same = false;
                    break;
                }
            }
        }
        
        if (same) {
            bool val = firstVal == 1;
            return new Node(val, true);
        }
        
        int half = size / 2;
        Node topLeft = Build(grid, row, col, half);
        Node topRight = Build(grid, row, col + half, half);
        Node bottomLeft = Build(grid, row + half, col, half);
        Node bottomRight = Build(grid, row + half, col + half, half);
        
        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }
}
```

## Javascript

```javascript
/**
 * // Definition for a QuadTree node.
 * function _Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {_Node}
 */
var construct = function(grid) {
    const n = grid.length;

    function build(x, y, size) {
        // Check if all values in the current region are the same
        let firstVal = grid[x][y];
        let uniform = true;
        for (let i = x; i < x + size && uniform; i++) {
            for (let j = y; j < y + size; j++) {
                if (grid[i][j] !== firstVal) {
                    uniform = false;
                    break;
                }
            }
        }

        if (uniform) {
            // Leaf node
            return new _Node(firstVal === 1, true, null, null, null, null);
        }

        const half = size >> 1;
        const topLeft = build(x, y, half);
        const topRight = build(x, y + half, half);
        const bottomLeft = build(x + half, y, half);
        const bottomRight = build(x + half, y + half, half);

        // Internal node; val can be arbitrary (use true)
        return new _Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
    }

    return build(0, 0, n);
};
```

## Typescript

```typescript
function construct(grid: number[][]): _Node | null {
    const n = grid.length;
    if (n === 0) return null;

    const build = (row: number, col: number, size: number): _Node => {
        const first = grid[row][col];
        let uniform = true;
        for (let i = row; i < row + size && uniform; i++) {
            for (let j = col; j < col + size; j++) {
                if (grid[i][j] !== first) {
                    uniform = false;
                    break;
                }
            }
        }
        if (uniform) {
            return new _Node(first === 1, true);
        }
        const half = size >> 1;
        const topLeft = build(row, col, half);
        const topRight = build(row, col + half, half);
        const bottomLeft = build(row + half, col, half);
        const bottomRight = build(row + half, col + half, half);
        return new _Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
    };

    return build(0, 0, n);
}
```

## Php

```php
/**
 * Definition for a QuadTree node.
 * class Node {
 *     public $val = null;
 *     public $isLeaf = null;
 *     public $topLeft = null;
 *     public $topRight = null;
 *     public $bottomLeft = null;
 *     public $bottomRight = null;
 *     function __construct($val, $isLeaf) {
 *         $this->val = $val;
 *         $this->isLeaf = $isLeaf;
 *         $this->topLeft = null;
 *         $this->topRight = null;
 *         $this->bottomLeft = null;
 *         $this->bottomRight = null;
 *     }
 * }
 */

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Node
     */
    function construct($grid) {
        $n = count($grid);
        return $this->build($grid, 0, 0, $n);
    }

    private function build(&$grid, $row, $col, $size) {
        $first = $grid[$row][$col];
        $same = true;
        for ($i = $row; $i < $row + $size && $same; $i++) {
            for ($j = $col; $j < $col + $size; $j++) {
                if ($grid[$i][$j] !== $first) {
                    $same = false;
                    break;
                }
            }
        }

        if ($same) {
            return new Node($first == 1, true);
        }

        $half = intdiv($size, 2);
        $topLeft     = $this->build($grid, $row, $col, $half);
        $topRight    = $this->build($grid, $row, $col + $half, $half);
        $bottomLeft  = $this->build($grid, $row + $half, $col, $half);
        $bottomRight = $this->build($grid, $row + $half, $col + $half, $half);

        $node = new Node(true, false); // val is arbitrary for non-leaf
        $node->topLeft = $topLeft;
        $node->topRight = $topRight;
        $node->bottomLeft = $bottomLeft;
        $node->bottomRight = $bottomRight;

        return $node;
    }
}
```

## Swift

```swift
/**
 * Definition for a QuadTree node.
 * public class Node {
 *     public var val: Bool
 *     public var isLeaf: Bool
 *     public var topLeft: Node?
 *     public var topRight: Node?
 *     public var bottomLeft: Node?
 *     public var bottomRight: Node?
 *     public init(_ val: Bool, _ isLeaf: Bool) {
 *         self.val = val
 *         self.isLeaf = isLeaf
 *         self.topLeft = nil
 *         self.topRight = nil
 *         self.bottomLeft = nil
 *         self.bottomRight = nil
 *     }
 * }
 */

class Solution {
    func construct(_ grid: [[Int]]) -> Node? {
        let n = grid.count
        guard n > 0 else { return nil }

        func build(_ r: Int, _ c: Int, _ size: Int) -> Node {
            if size == 1 {
                return Node(grid[r][c] == 1, true)
            }
            let half = size / 2
            let topLeft = build(r, c, half)
            let topRight = build(r, c + half, half)
            let bottomLeft = build(r + half, c, half)
            let bottomRight = build(r + half, c + half, half)

            if topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf &&
                topLeft.val == topRight.val && topLeft.val == bottomLeft.val && topLeft.val == bottomRight.val {
                return Node(topLeft.val, true)
            } else {
                let node = Node(false, false)
                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight
                return node
            }
        }

        return build(0, 0, n)
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a QuadTree node.
 * class Node(var `val`: Boolean, var isLeaf: Boolean) {
 *     var topLeft: Node? = null
 *     var topRight: Node? = null
 *     var bottomLeft: Node? = null
 *     var bottomRight: Node? = null
 * }
 */
class Solution {
    fun construct(grid: Array<IntArray>): Node? {
        val n = grid.size
        if (n == 0) return null

        fun build(r: Int, c: Int, size: Int): Node {
            var same = true
            val first = grid[r][c]
            outer@ for (i in r until r + size) {
                for (j in c until c + size) {
                    if (grid[i][j] != first) {
                        same = false
                        break@outer
                    }
                }
            }
            return if (same) {
                Node(first == 1, true)
            } else {
                val half = size / 2
                val topLeft = build(r, c, half)
                val topRight = build(r, c + half, half)
                val bottomLeft = build(r + half, c, half)
                val bottomRight = build(r + half, c + half, half)
                val node = Node(false, false)
                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight
                node
            }
        }

        return build(0, 0, n)
    }
}
```

## Golang

```go
/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
	var build func(x, y, size int) *Node
	build = func(x, y, size int) *Node {
		if size == 1 {
			return &Node{
				Val:    grid[x][y] == 1,
				IsLeaf: true,
			}
		}
		first := grid[x][y]
		uniform := true
		for i := x; i < x+size && uniform; i++ {
			for j := y; j < y+size; j++ {
				if grid[i][j] != first {
					uniform = false
					break
				}
			}
		}
		if uniform {
			return &Node{
				Val:    first == 1,
				IsLeaf: true,
			}
		}
		half := size / 2
		return &Node{
			IsLeaf:      false,
			TopLeft:     build(x, y, half),
			TopRight:    build(x, y+half, half),
			BottomLeft:  build(x+half, y, half),
			BottomRight: build(x+half, y+half, half),
		}
	}
	n := len(grid)
	return build(0, 0, n)
}
```

## Ruby

```ruby
# Definition for a QuadTree node.
# class Node
#     attr_accessor :val, :isLeaf, :topLeft, :topRight, :bottomLeft, :bottomRight
#     def initialize(val=false, isLeaf=false, topLeft=nil, topRight=nil, bottomLeft=nil, bottomRight=nil)
#         @val = val
#         @isLeaf = isLeaf
#         @topLeft = topLeft
#         @topRight = topRight
#         @bottomLeft = bottomLeft
#         @bottomRight = bottomRight
#     end
# end

def construct(grid)
  n = grid.length
  build = lambda do |x, y, size|
    if size == 1
      return Node.new(grid[x][y] == 1, true)
    end

    half = size / 2
    tl = build.call(x, y, half)
    tr = build.call(x, y + half, half)
    bl = build.call(x + half, y, half)
    br = build.call(x + half, y + half, half)

    if tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
       tl.val == tr.val && tl.val == bl.val && tl.val == br.val
      Node.new(tl.val, true)
    else
      Node.new(false, false, tl, tr, bl, br)
    end
  end

  build.call(0, 0, n)
end
```

## Scala

```scala
object Solution {
    def construct(grid: Array[Array[Int]]): Node = {
        val n = grid.length
        def build(r: Int, c: Int, size: Int): Node = {
            if (size == 1) {
                return new Node(grid(r)(c) == 1, true)
            }
            var same = true
            val first = grid(r)(c)
            var i = r
            while (i < r + size && same) {
                var j = c
                while (j < c + size && same) {
                    if (grid(i)(j) != first) same = false
                    j += 1
                }
                i += 1
            }
            if (same) {
                new Node(first == 1, true)
            } else {
                val half = size / 2
                val node = new Node(true, false)
                node.topLeft = build(r, c, half)
                node.topRight = build(r, c + half, half)
                node.bottomLeft = build(r + half, c, half)
                node.bottomRight = build(r + half, c + half, half)
                node
            }
        }
        build(0, 0, n)
    }
}
```
