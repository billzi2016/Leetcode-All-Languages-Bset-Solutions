# 1476. Subrectangle Queries

## Cpp

```cpp
class SubrectangleQueries {
public:
    std::vector<std::vector<int>> rect;
    
    SubrectangleQueries(std::vector<std::vector<int>>& rectangle) {
        rect = rectangle;
    }
    
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int i = row1; i <= row2; ++i) {
            for (int j = col1; j <= col2; ++j) {
                rect[i][j] = newValue;
            }
        }
    }
    
    int getValue(int row, int col) {
        return rect[row][col];
    }
};

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);
 * obj->updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj->getValue(row,col);
 */
```

## Java

```java
class SubrectangleQueries {
    private final int[][] rectangle;

    public SubrectangleQueries(int[][] rectangle) {
        this.rectangle = rectangle;
    }

    public void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int i = row1; i <= row2; i++) {
            for (int j = col1; j <= col2; j++) {
                rectangle[i][j] = newValue;
            }
        }
    }

    public int getValue(int row, int col) {
        return rectangle[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.getValue(row,col);
 */
```

## Python

```python
class SubrectangleQueries(object):
    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        # Store a reference to the mutable rectangle
        self.rect = [row[:] for row in rectangle]

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for r in range(row1, row2 + 1):
            self.rect[r][col1:col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rect[row][col]
```

## Python3

```python
from typing import List

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rect = [row[:] for row in rectangle]

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            self.rect[r][col1:col2 + 1] = [newValue] * (col2 - col1 + 1)

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int rows;
    int cols;
    int **data;
} SubrectangleQueries;

SubrectangleQueries* subrectangleQueriesCreate(int** rectangle, int rectangleSize, int* rectangleColSize) {
    SubrectangleQueries *obj = (SubrectangleQueries *)malloc(sizeof(SubrectangleQueries));
    obj->rows = rectangleSize;
    obj->cols = rectangleColSize[0];
    obj->data = (int **)malloc(obj->rows * sizeof(int *));
    for (int i = 0; i < obj->rows; ++i) {
        obj->data[i] = (int *)malloc(obj->cols * sizeof(int));
        for (int j = 0; j < obj->cols; ++j) {
            obj->data[i][j] = rectangle[i][j];
        }
    }
    return obj;
}

void subrectangleQueriesUpdateSubrectangle(SubrectangleQueries* obj, int row1, int col1, int row2, int col2, int newValue) {
    for (int i = row1; i <= row2; ++i) {
        for (int j = col1; j <= col2; ++j) {
            obj->data[i][j] = newValue;
        }
    }
}

int subrectangleQueriesGetValue(SubrectangleQueries* obj, int row, int col) {
    return obj->data[row][col];
}

void subrectangleQueriesFree(SubrectangleQueries* obj) {
    for (int i = 0; i < obj->rows; ++i) {
        free(obj->data[i]);
    }
    free(obj->data);
    free(obj);
}
```

## Csharp

```csharp
public class SubrectangleQueries
{
    private readonly int[][] _rect;

    public SubrectangleQueries(int[][] rectangle)
    {
        int rows = rectangle.Length;
        _rect = new int[rows][];
        for (int i = 0; i < rows; i++)
        {
            int cols = rectangle[i].Length;
            _rect[i] = new int[cols];
            System.Array.Copy(rectangle[i], _rect[i], cols);
        }
    }

    public void UpdateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
    {
        for (int r = row1; r <= row2; r++)
        {
            for (int c = col1; c <= col2; c++)
            {
                _rect[r][c] = newValue;
            }
        }
    }

    public int GetValue(int row, int col)
    {
        return _rect[row][col];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangle
 */
var SubrectangleQueries = function(rectangle) {
    // Deep copy to avoid external modifications
    this.rect = rectangle.map(row => row.slice());
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2 
 * @param {number} newValue
 * @return {void}
 */
SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {
    for (let i = row1; i <= row2; i++) {
        for (let j = col1; j <= col2; j++) {
            this.rect[i][j] = newValue;
        }
    }
};

/** 
 * @param {number} row 
 * @param {number} col
 * @return {number}
 */
SubrectangleQueries.prototype.getValue = function(row, col) {
    return this.rect[row][col];
};
```

## Typescript

```typescript
class SubrectangleQueries {
    private rect: number[][];

    constructor(rectangle: number[][]) {
        // Deep copy to avoid external modifications
        this.rect = rectangle.map(row => row.slice());
    }

    updateSubrectangle(row1: number, col1: number, row2: number, col2: number, newValue: number): void {
        for (let r = row1; r <= row2; r++) {
            const row = this.rect[r];
            for (let c = col1; c <= col2; c++) {
                row[c] = newValue;
            }
        }
    }

    getValue(row: number, col: number): number {
        return this.rect[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

## Php

```php
class SubrectangleQueries {
    private $rect;

    public function __construct($rectangle) {
        $this->rect = $rectangle;
    }

    public function updateSubrectangle($row1, $col1, $row2, $col2, $newValue) {
        for ($i = $row1; $i <= $row2; $i++) {
            for ($j = $col1; $j <= $col2; $j++) {
                $this->rect[$i][$j] = $newValue;
            }
        }
    }

    public function getValue($row, $col) {
        return $this->rect[$row][$col];
    }
}
```

## Swift

```swift
class SubrectangleQueries {
    private var rectangle: [[Int]]
    
    init(_ rectangle: [[Int]]) {
        self.rectangle = rectangle
    }
    
    func updateSubrectangle(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int, _ newValue: Int) {
        for r in row1...row2 {
            for c in col1...col2 {
                rectangle[r][c] = newValue
            }
        }
    }
    
    func getValue(_ row: Int, _ col: Int) -> Int {
        return rectangle[row][col]
    }
}
```

## Kotlin

```kotlin
class SubrectangleQueries(rectangle: Array<IntArray>) {

    private val rect = rectangle

    fun updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int) {
        for (i in row1..row2) {
            val rowArr = rect[i]
            for (j in col1..col2) {
                rowArr[j] = newValue
            }
        }
    }

    fun getValue(row: Int, col: Int): Int {
        return rect[row][col]
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

## Golang

```go
type SubrectangleQueries struct {
	rect [][]int
}

func Constructor(rectangle [][]int) SubrectangleQueries {
	// Deep copy to avoid external modifications
	copied := make([][]int, len(rectangle))
	for i := range rectangle {
		row := make([]int, len(rectangle[i]))
		copy(row, rectangle[i])
		copied[i] = row
	}
	return SubrectangleQueries{rect: copied}
}

func (this *SubrectangleQueries) UpdateSubrectangle(row1 int, col1 int, row2 int, col2 int, newValue int) {
	for r := row1; r <= row2; r++ {
		for c := col1; c <= col2; c++ {
			this.rect[r][c] = newValue
		}
	}
}

func (this *SubrectangleQueries) GetValue(row int, col int) int {
	return this.rect[row][col]
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * obj := Constructor(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * param_2 := obj.GetValue(row,col);
 */
```

## Ruby

```ruby
class SubrectangleQueries
  # :type rectangle: Integer[][]
  def initialize(rectangle)
    @rect = rectangle.map { |row| row.dup }
  end

  # :type row1: Integer
  # :type col1: Integer
  # :type row2: Integer
  # :type col2: Integer
  # :type new_value: Integer
  # :rtype: Void
  def update_subrectangle(row1, col1, row2, col2, new_value)
    (row1..row2).each do |r|
      (col1..col2).each do |c|
        @rect[r][c] = new_value
      end
    end
  end

  # :type row: Integer
  # :type col: Integer
  # :rtype: Integer
  def get_value(row, col)
    @rect[row][col]
  end
end
```

## Scala

```scala
class SubrectangleQueries(_rectangle: Array[Array[Int]]) {
  private val rectangle = _rectangle.map(_.clone)

  def updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int): Unit = {
    var i = row1
    while (i <= row2) {
      var j = col1
      while (j <= col2) {
        rectangle(i)(j) = newValue
        j += 1
      }
      i += 1
    }
  }

  def getValue(row: Int, col: Int): Int = {
    rectangle(row)(col)
  }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

## Rust

```rust
struct SubrectangleQueries {
    rect: Vec<Vec<i32>>,
}

impl SubrectangleQueries {
    fn new(rectangle: Vec<Vec<i32>>) -> Self {
        Self { rect: rectangle }
    }

    fn update_subrectangle(&mut self, row1: i32, col1: i32, row2: i32, col2: i32, new_value: i32) {
        let r1 = row1 as usize;
        let c1 = col1 as usize;
        let r2 = row2 as usize;
        let c2 = col2 as usize;
        for i in r1..=r2 {
            for j in c1..=c2 {
                self.rect[i][j] = new_value;
            }
        }
    }

    fn get_value(&self, row: i32, col: i32) -> i32 {
        self.rect[row as usize][col as usize]
    }
}
```

## Racket

```racket
(define subrectangle-queries%
  (class object%
    (init-field rectangle)
    (super-new)

    ;; internal mutable representation as vector of vectors
    (define rect (list->vector (map list->vector rectangle)))

    (define/public (update-subrectangle row1 col1 row2 col2 newValue)
      (for ([r (in-range row1 (+ row2 1))])
        (let ([rowvec (vector-ref rect r)])
          (for ([c (in-range col1 (+ col2 1))])
            (vector-set! rowvec c newValue)))))

    (define/public (get-value row col)
      (vector-ref (vector-ref rect row) col))))
```
