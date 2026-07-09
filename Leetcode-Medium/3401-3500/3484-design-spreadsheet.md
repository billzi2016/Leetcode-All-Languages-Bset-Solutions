# 3484. Design Spreadsheet

## Cpp

```cpp
class Spreadsheet {
public:
    Spreadsheet(int rows) {
        // rows count is not needed for current operations
    }
    
    void setCell(std::string cell, int value) {
        cells_[cell] = value;
    }
    
    void resetCell(std::string cell) {
        cells_.erase(cell);
    }
    
    int getValue(std::string formula) {
        // formula format: "=X+Y"
        if (formula.empty() || formula[0] != '=') return 0;
        std::size_t plusPos = formula.find('+', 1);
        std::string left = formula.substr(1, plusPos - 1);
        std::string right = formula.substr(plusPos + 1);
        return evalToken(left) + evalToken(right);
    }
    
private:
    int evalToken(const std::string& token) {
        if (token.empty()) return 0;
        if (std::isdigit(token[0])) {
            return std::stoi(token);
        } else {
            auto it = cells_.find(token);
            return it != cells_.end() ? it->second : 0;
        }
    }
    
    std::unordered_map<std::string, int> cells_;
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */
```

## Java

```java
class Spreadsheet {
    private final java.util.Map<String, Integer> cells;

    public Spreadsheet(int rows) {
        cells = new java.util.HashMap<>();
    }

    public void setCell(String cell, int value) {
        cells.put(cell, value);
    }

    public void resetCell(String cell) {
        cells.remove(cell);
    }

    public int getValue(String formula) {
        // formula format: "=X+Y"
        if (formula == null || formula.length() == 0) return 0;
        // remove leading '='
        String expr = formula.substring(1);
        int plusIdx = expr.indexOf('+');
        String left = expr.substring(0, plusIdx);
        String right = expr.substring(plusIdx + 1);
        return getOperandValue(left) + getOperandValue(right);
    }

    private int getOperandValue(String token) {
        char first = token.charAt(0);
        if (first >= 'A' && first <= 'Z') {
            // cell reference
            return cells.getOrDefault(token, 0);
        } else {
            // integer literal
            return Integer.parseInt(token);
        }
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */
```

## Python

```python
class Spreadsheet(object):
    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.cells = {}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.cells[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # formula format: "=X+Y"
        expr = formula[1:]  # remove leading '='
        left, right = expr.split('+', 1)

        def val(token):
            if token and token[0].isalpha():
                return self.cells.get(token, 0)
            else:
                return int(token) if token else 0

        return val(left) + val(right)
```

## Python3

```python
class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}  # key: cell string like "A1", value: int

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # formula format: "=X+Y"
        expr = formula[1:]  # strip leading '='
        left_str, right_str = expr.split('+', 1)

        def val(token: str) -> int:
            if token and token[0].isalpha():
                return self.cells.get(token, 0)
            else:
                return int(token)

        return val(left_str) + val(right_str)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    int rows;
    int *data; // size = 26 * rows
} Spreadsheet;

static inline int index_of(Spreadsheet *obj, const char *cell) {
    int col = cell[0] - 'A';
    int row = atoi(cell + 1) - 1; // zero‑based
    return col * obj->rows + row;
}

static inline int operand_value(Spreadsheet *obj, const char *s) {
    if (isdigit(s[0]))
        return atoi(s);
    return obj->data[index_of(obj, s)];
}

/** Initialize your data structure here. */
Spreadsheet* spreadsheetCreate(int rows) {
    Spreadsheet *obj = (Spreadsheet *)malloc(sizeof(Spreadsheet));
    obj->rows = rows;
    obj->data = (int *)calloc(26 * rows, sizeof(int));
    return obj;
}

void spreadsheetSetCell(Spreadsheet* obj, char* cell, int value) {
    int idx = index_of(obj, cell);
    obj->data[idx] = value;
}

void spreadsheetResetCell(Spreadsheet* obj, char* cell) {
    int idx = index_of(obj, cell);
    obj->data[idx] = 0;
}

/** Return the result of evaluating the formula. */
int spreadsheetGetValue(Spreadsheet* obj, char* formula) {
    const char *p = formula + 1; // skip '='
    const char *plus = strchr(p, '+');
    int left_len = (int)(plus - p);
    char left[16];
    strncpy(left, p, left_len);
    left[left_len] = '\0';
    const char *right = plus + 1;
    int v1 = operand_value(obj, left);
    int v2 = operand_value(obj, right);
    return v1 + v2;
}

void spreadsheetFree(Spreadsheet* obj) {
    if (obj) {
        free(obj->data);
        free(obj);
    }
}

/**
 * Your Spreadsheet struct will be instantiated and called as such:
 * Spreadsheet* obj = spreadsheetCreate(rows);
 * spreadsheetSetCell(obj, cell, value);
 * spreadsheetResetCell(obj, cell);
 * int param_3 = spreadsheetGetValue(obj, formula);
 * spreadsheetFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Spreadsheet {
    private readonly int _rows;
    private readonly Dictionary<string, int> _cells = new Dictionary<string, int>();

    public Spreadsheet(int rows) {
        _rows = rows;
    }

    public void SetCell(string cell, int value) {
        _cells[cell] = value;
    }

    public void ResetCell(string cell) {
        _cells.Remove(cell);
    }

    public int GetValue(string formula) {
        // Formula format: "=X+Y"
        string expr = formula.Substring(1); // remove '='
        string[] parts = expr.Split('+');
        int sum = 0;
        foreach (var part in parts) {
            if (!string.IsNullOrEmpty(part) && char.IsLetter(part[0])) {
                // cell reference
                if (_cells.TryGetValue(part, out int val)) {
                    sum += val;
                }
            } else {
                // integer literal
                sum += int.Parse(part);
            }
        }
        return sum;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * int param_3 = obj.GetValue(formula);
 */
```

## Javascript

```javascript
/**
 * @param {number} rows
 */
var Spreadsheet = function(rows) {
    this.map = new Map(); // key: cell string, value: number
};

/** 
 * @param {string} cell 
 * @param {number} value
 * @return {void}
 */
Spreadsheet.prototype.setCell = function(cell, value) {
    this.map.set(cell, value);
};

/** 
 * @param {string} cell
 * @return {void}
 */
Spreadsheet.prototype.resetCell = function(cell) {
    this.map.delete(cell); // treat as unset => default 0
};

/**
 * @param {string} formula
 * @return {number}
 */
Spreadsheet.prototype.getValue = function(formula) {
    // formula format: "=X+Y"
    const expr = formula.slice(1); // remove leading '='
    const plusIdx = expr.indexOf('+');
    const left = expr.substring(0, plusIdx);
    const right = expr.substring(plusIdx + 1);

    const getOperandValue = (op) => {
        if (/^\d+$/.test(op)) { // pure number
            return Number(op);
        }
        // cell reference
        return this.map.get(op) ?? 0;
    };

    return getOperandValue(left) + getOperandValue(right);
};

/** 
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */
```

## Typescript

```typescript
class Spreadsheet {
    private cells: Map<string, number>;

    constructor(rows: number) {
        this.cells = new Map();
    }

    setCell(cell: string, value: number): void {
        this.cells.set(cell, value);
    }

    resetCell(cell: string): void {
        this.cells.delete(cell);
    }

    getValue(formula: string): number {
        // formula format: "=X+Y"
        const expr = formula.slice(1); // remove '='
        const parts = expr.split('+');
        let sum = 0;
        for (const part of parts) {
            if (!part) continue;
            const firstChar = part.charCodeAt(0);
            if (firstChar >= 65 && firstChar <= 90) { // 'A' to 'Z'
                sum += this.cells.get(part) ?? 0;
            } else {
                sum += parseInt(part, 10);
            }
        }
        return sum;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */
```

## Php

```php
class Spreadsheet {
    private int $rows;
    private array $cells = [];

    /**
     * @param Integer $rows
     */
    function __construct($rows) {
        $this->rows = $rows;
    }

    /**
     * @param String $cell
     * @param Integer $value
     * @return NULL
     */
    function setCell($cell, $value) {
        $this->cells[$cell] = $value;
    }

    /**
     * @param String $cell
     * @return NULL
     */
    function resetCell($cell) {
        unset($this->cells[$cell]);
    }

    /**
     * @param String $formula
     * @return Integer
     */
    function getValue($formula) {
        // Formula format: "=X+Y"
        $expr = substr($formula, 1); // remove leading '='
        [$op1, $op2] = explode('+', $expr, 2);
        $sum = 0;

        foreach ([$op1, $op2] as $operand) {
            if ($operand === '') continue;
            if (ctype_digit($operand)) {
                $sum += intval($operand);
            } else {
                $sum += $this->cells[$operand] ?? 0;
            }
        }

        return $sum;
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * $obj = new Spreadsheet($rows);
 * $obj->setCell($cell, $value);
 * $obj->resetCell($cell);
 * $ret_3 = $obj->getValue($formula);
 */
```

## Swift

```swift
class Spreadsheet {
    private var cells: [String: Int] = [:]

    init(_ rows: Int) { }

    func setCell(_ cell: String, _ value: Int) {
        cells[cell] = value
    }

    func resetCell(_ cell: String) {
        cells.removeValue(forKey: cell)
    }

    func getValue(_ formula: String) -> Int {
        // Formula format: "=X+Y"
        let expr = String(formula.dropFirst())  // remove '='
        guard let plusIdx = expr.firstIndex(of: "+") else { return 0 }
        let left = String(expr[..<plusIdx])
        let right = String(expr[expr.index(after: plusIdx)...])

        func eval(_ token: String) -> Int {
            if let num = Int(token) {
                return num
            }
            return cells[token] ?? 0
        }

        return eval(left) + eval(right)
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet(rows)
 * obj.setCell(cell, value)
 * obj.resetCell(cell)
 * let ret_3: Int = obj.getValue(formula)
 */
```

## Kotlin

```kotlin
class Spreadsheet(rows: Int) {
    private val cells = HashMap<String, Int>()

    fun setCell(cell: String, value: Int) {
        cells[cell] = value
    }

    fun resetCell(cell: String) {
        cells.remove(cell)
    }

    fun getValue(formula: String): Int {
        // formula format: "=X+Y"
        val expr = formula.substring(1) // remove leading '='
        val parts = expr.split('+')
        var sum = 0
        for (part in parts) {
            if (part.isEmpty()) continue
            val c = part[0]
            sum += if (c in 'A'..'Z') {
                cells.getOrDefault(part, 0)
            } else {
                part.toInt()
            }
        }
        return sum
    }
}
```

## Dart

```dart
class Spreadsheet {
  final int rows;
  final Map<String, int> _cells = {};

  Spreadsheet(this.rows);

  void setCell(String cell, int value) {
    _cells[cell] = value;
  }

  void resetCell(String cell) {
    _cells.remove(cell);
  }

  int getValue(String formula) {
    // Formula format: "=X+Y"
    String expr = formula.substring(1); // remove '='
    int plusIdx = expr.indexOf('+');
    String left = expr.substring(0, plusIdx);
    String right = expr.substring(plusIdx + 1);
    return _parseOperand(left) + _parseOperand(right);
  }

  int _parseOperand(String s) {
    if (s.isEmpty) return 0;
    // If starts with a digit, it's a number; otherwise a cell reference.
    int first = s.codeUnitAt(0);
    if (first >= 48 && first <= 57) { // '0'..'9'
      return int.parse(s);
    }
    return _cells[s] ?? 0;
  }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param3 = obj.getValue(formula);
 */
```

## Golang

```go
type Spreadsheet struct {
	cells map[string]int
}

func Constructor(rows int) Spreadsheet {
	return Spreadsheet{cells: make(map[string]int)}
}

func (this *Spreadsheet) SetCell(cell string, value int) {
	this.cells[cell] = value
}

func (this *Spreadsheet) ResetCell(cell string) {
	delete(this.cells, cell)
}

func (this *Spreadsheet) GetValue(formula string) int {
	if len(formula) == 0 {
		return 0
	}
	if formula[0] != '=' {
		v, _ := strconv.Atoi(formula)
		return v
	}
	parts := strings.SplitN(formula[1:], "+", 2)
	sum := 0
	for _, p := range parts {
		if len(p) > 0 && p[0] >= 'A' && p[0] <= 'Z' {
			if val, ok := this.cells[p]; ok {
				sum += val
			}
		} else {
			v, _ := strconv.Atoi(p)
			sum += v
		}
	}
	return sum
}

import (
	"strconv"
	"strings"
)
```

## Ruby

```ruby
class Spreadsheet
  def initialize(rows)
    @rows = rows
    @cells = {}
  end

  def set_cell(cell, value)
    @cells[cell] = value
  end

  def reset_cell(cell)
    @cells.delete(cell)
  end

  def get_value(formula)
    expr = formula[1..-1]
    left, right = expr.split('+', 2)
    operand(left) + operand(right)
  end

  private

  def operand(str)
    if str =~ /\A[A-Z]\d+\z/
      @cells[str] || 0
    else
      str.to_i
    end
  end
end
```

## Scala

```scala
import scala.collection.mutable

class Spreadsheet(_rows: Int) {

  private val cells = mutable.Map[String, Int]()

  def setCell(cell: String, value: Int): Unit = {
    if (value == 0) cells.remove(cell)
    else cells(cell) = value
  }

  def resetCell(cell: String): Unit = {
    cells.remove(cell)
  }

  def getValue(formula: String): Int = {
    // formula format "=X+Y"
    val expr = formula.substring(1) // drop '='
    val plusIdx = expr.indexOf('+')
    val left = expr.substring(0, plusIdx)
    val right = expr.substring(plusIdx + 1)

    def tokenValue(tok: String): Int = {
      if (tok.isEmpty) 0
      else if (tok.charAt(0).isLetter) cells.getOrElse(tok, 0)
      else tok.toInt
    }

    tokenValue(left) + tokenValue(right)
  }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * val obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * val param_3 = obj.getValue(formula)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct Spreadsheet {
    _rows: i32,
    cells: RefCell<HashMap<String, i32>>,
}

impl Spreadsheet {
    fn new(rows: i32) -> Self {
        Spreadsheet {
            _rows: rows,
            cells: RefCell::new(HashMap::new()),
        }
    }

    fn set_cell(&self, cell: String, value: i32) {
        self.cells.borrow_mut().insert(cell, value);
    }

    fn reset_cell(&self, cell: String) {
        self.cells.borrow_mut().remove(&cell);
    }

    fn get_value(&self, formula: String) -> i32 {
        // Formula format: "=X+Y"
        let expr = &formula[1..]; // skip '='
        let parts: Vec<&str> = expr.split('+').collect();
        let left = parts[0];
        let right = parts[1];

        fn eval_operand(op: &str, cells: &HashMap<String, i32>) -> i32 {
            if op.as_bytes()[0].is_ascii_digit() {
                op.parse::<i32>().unwrap()
            } else {
                *cells.get(op).unwrap_or(&0)
            }
        }

        let map = self.cells.borrow();
        eval_operand(left, &map) + eval_operand(right, &map)
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * let obj = Spreadsheet::new(rows);
 * obj.set_cell(cell, value);
 * obj.reset_cell(cell);
 * let ret_3: i32 = obj.get_value(formula);
 */
```

## Racket

```racket
(define spreadsheet%
  (class object%
    (super-new)
    (init-field rows)
    (define cells (make-hash))

    (define/public (set-cell cell value)
      (hash-set! cells cell value))

    (define/public (reset-cell cell)
      (hash-remove! cells cell))

    (define/public (get-value formula)
      (let* ([expr (substring formula 1)] ; drop leading '='
             [plus-pos (string-index expr #\+)])
        (let* ([left (substring expr 0 plus-pos)]
               [right (substring expr (+ plus-pos 1))])
          (+ (parse-operand left) (parse-operand right)))))

    (define (parse-operand s)
      (let ([n (string->number s)])
        (if n
            (exact-floor n)
            (hash-ref cells s 0))))))
```

## Erlang

```erlang
-export([spreadsheet_init_/1,
         spreadsheet_set_cell/2,
         spreadsheet_reset_cell/1,
         spreadsheet_get_value/1]).

-spec spreadsheet_init_(Rows :: integer()) -> any().
spreadsheet_init_(Rows) ->
    put(spreadsheet_rows, Rows),
    put(spreadsheet_cells, #{}).

-spec spreadsheet_set_cell(Cell :: unicode:unicode_binary(), Value :: integer()) -> any().
spreadsheet_set_cell(Cell, Value) ->
    Cells = get(spreadsheet_cells),
    NewCells = Maps:put(Cell, Value, Cells),
    put(spreadsheet_cells, NewCells).

-spec spreadsheet_reset_cell(Cell :: unicode:unicode_binary()) -> any().
spreadsheet_reset_cell(Cell) ->
    Cells = get(spreadsheet_cells),
    NewCells = Maps:put(Cell, 0, Cells),
    put(spreadsheet_cells, NewCells).

-spec spreadsheet_get_value(Formula :: unicode:unicode_binary()) -> integer().
spreadsheet_get_value(Formula) ->
    %% Remove leading '='
    FormulaBody = binary:part(Formula, 1, byte_size(Formula) - 1),
    [Op1Bin, Op2Bin] = binary:split(FormulaBody, <<"+">>, [global]),
    Val1 = operand_value(Op1Bin),
    Val2 = operand_value(Op2Bin),
    Val1 + Val2.

operand_value(Bin) ->
    case binary:first(Bin) of
        C when C >= $A, C =< $Z ->
            Cells = get(spreadsheet_cells),
            maps:get(Bin, Cells, 0);
        _ ->
            binary_to_integer(Bin)
    end.
```

## Elixir

```elixir
defmodule Spreadsheet do
  @spec init_(rows :: integer) :: :ok
  def init_(_rows) do
    case Process.whereis(__MODULE__) do
      nil ->
        {:ok, _pid} = Agent.start_link(fn -> %{} end, name: __MODULE__)
        :ok

      pid when is_pid(pid) ->
        Agent.update(pid, fn _ -> %{} end)
        :ok
    end
  end

  @spec set_cell(cell :: String.t(), value :: integer) :: :ok
  def set_cell(cell, value) do
    Agent.update(__MODULE__, &Map.put(&1, cell, value))
  end

  @spec reset_cell(cell :: String.t()) :: :ok
  def reset_cell(cell) do
    Agent.update(__MODULE__, &Map.delete(&1, cell))
  end

  @spec get_value(formula :: String.t()) :: integer
  def get_value(formula) do
    expr = String.trim_leading(formula, "=")
    [left, right] = String.split(expr, "+", parts: 2)

    l = eval_operand(String.trim(left))
    r = eval_operand(String.trim(right))

    l + r
  end

  defp eval_operand(op) do
    case Integer.parse(op) do
      {num, ""} -> num
      :error ->
        Agent.get(__MODULE__, fn cells -> Map.get(cells, op, 0) end)
    end
  end
end
```
