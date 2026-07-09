# 1286. Iterator for Combination

## Cpp

```cpp
class CombinationIterator {
public:
    CombinationIterator(string characters, int combinationLength) {
        n = characters.size();
        k = combinationLength;
        s = std::move(characters);
        generate(0, 0);
        idx = 0;
    }
    
    string next() {
        return combos[idx++];
    }
    
    bool hasNext() {
        return idx < (int)combos.size();
    }

private:
    string s;
    int n, k;
    vector<string> combos;
    int idx;

    void generate(int start, int depth) {
        if (depth == k) {
            combos.push_back(current);
            return;
        }
        for (int i = start; i <= n - (k - depth); ++i) {
            current.push_back(s[i]);
            generate(i + 1, depth + 1);
            current.pop_back();
        }
    }

    string current;
};
```

## Java

```java
class CombinationIterator {
    private final String characters;
    private final int n;
    private final int k;
    private final int[] idx;
    private boolean hasNext;

    public CombinationIterator(String characters, int combinationLength) {
        this.characters = characters;
        this.n = characters.length();
        this.k = combinationLength;
        this.idx = new int[k];
        for (int i = 0; i < k; i++) {
            idx[i] = i;
        }
        this.hasNext = k <= n;
    }

    public String next() {
        // Build current combination string
        StringBuilder sb = new StringBuilder(k);
        for (int i = 0; i < k; i++) {
            sb.append(characters.charAt(idx[i]));
        }
        // Prepare next combination
        int i = k - 1;
        while (i >= 0 && idx[i] == n - k + i) {
            i--;
        }
        if (i < 0) {
            hasNext = false;
        } else {
            idx[i]++;
            for (int j = i + 1; j < k; j++) {
                idx[j] = idx[j - 1] + 1;
            }
        }
        return sb.toString();
    }

    public boolean hasNext() {
        return hasNext;
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
```

## Python

```python
import itertools

class CombinationIterator(object):
    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.combos = [''.join(c) for c in itertools.combinations(characters, combinationLength)]
        self.idx = 0

    def next(self):
        """
        :rtype: str
        """
        result = self.combos[self.idx]
        self.idx += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.combos)
```

## Python3

```python
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        from itertools import combinations
        self._combos = [''.join(c) for c in combinations(characters, combinationLength)]
        self._index = 0

    def next(self) -> str:
        result = self._combos[self._index]
        self._index += 1
        return result

    def hasNext(self) -> bool:
        return self._index < len(self._combos)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char *characters;
    int n;
    int k;
    int *indices;
    bool has_next;
} CombinationIterator;

CombinationIterator* combinationIteratorCreate(char* characters, int combinationLength) {
    CombinationIterator* obj = (CombinationIterator*)malloc(sizeof(CombinationIterator));
    obj->n = (int)strlen(characters);
    obj->k = combinationLength;
    obj->characters = (char*)malloc(obj->n + 1);
    strcpy(obj->characters, characters);
    obj->indices = (int*)malloc(combinationLength * sizeof(int));
    for (int i = 0; i < combinationLength; ++i) {
        obj->indices[i] = i;
    }
    obj->has_next = (combinationLength <= obj->n);
    return obj;
}

char* combinationIteratorNext(CombinationIterator* obj) {
    int k = obj->k;
    char *res = (char*)malloc(k + 1);
    for (int i = 0; i < k; ++i) {
        res[i] = obj->characters[obj->indices[i]];
    }
    res[k] = '\0';

    int n = obj->n;
    int i = k - 1;
    while (i >= 0 && obj->indices[i] == i + n - k) {
        --i;
    }
    if (i < 0) {
        obj->has_next = false;
    } else {
        ++obj->indices[i];
        for (int j = i + 1; j < k; ++j) {
            obj->indices[j] = obj->indices[j - 1] + 1;
        }
    }
    return res;
}

bool combinationIteratorHasNext(CombinationIterator* obj) {
    return obj->has_next;
}

void combinationIteratorFree(CombinationIterator* obj) {
    if (!obj) return;
    free(obj->characters);
    free(obj->indices);
    free(obj);
}
```

## Csharp

```csharp
public class CombinationIterator
{
    private readonly List<string> _combinations;
    private int _index;

    public CombinationIterator(string characters, int combinationLength)
    {
        _combinations = new List<string>();
        var sb = new System.Text.StringBuilder();
        Generate(combinationLength, 0, characters, sb);
        _index = 0;
    }

    private void Generate(int targetLen, int start, string chars, System.Text.StringBuilder sb)
    {
        if (sb.Length == targetLen)
        {
            _combinations.Add(sb.ToString());
            return;
        }
        for (int i = start; i < chars.Length; i++)
        {
            sb.Append(chars[i]);
            Generate(targetLen, i + 1, chars, sb);
            sb.Length--;
        }
    }

    public string Next()
    {
        return _combinations[_index++];
    }

    public bool HasNext()
    {
        return _index < _combinations.Count;
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */
```

## Javascript

```javascript
/**
 * @param {string} characters
 * @param {number} combinationLength
 */
var CombinationIterator = function(characters, combinationLength) {
    this.combos = [];
    const n = characters.length;
    const k = combinationLength;
    const path = [];

    const backtrack = (start) => {
        if (path.length === k) {
            this.combos.push(path.join(''));
            return;
        }
        for (let i = start; i < n; ++i) {
            path.push(characters[i]);
            backtrack(i + 1);
            path.pop();
        }
    };
    backtrack(0);
    this.idx = 0;
};

/**
 * @return {string}
 */
CombinationIterator.prototype.next = function() {
    return this.combos[this.idx++];
};

/**
 * @return {boolean}
 */
CombinationIterator.prototype.hasNext = function() {
    return this.idx < this.combos.length;
};
```

## Typescript

```typescript
class CombinationIterator {
    private combos: string[];
    private index: number;

    constructor(characters: string, combinationLength: number) {
        this.combos = [];
        const n = characters.length;
        const path: string[] = [];

        const backtrack = (start: number) => {
            if (path.length === combinationLength) {
                this.combos.push(path.join(''));
                return;
            }
            for (let i = start; i < n; i++) {
                path.push(characters[i]);
                backtrack(i + 1);
                path.pop();
            }
        };

        backtrack(0);
        this.index = 0;
    }

    next(): string {
        return this.combos[this.index++];
    }

    hasNext(): boolean {
        return this.index < this.combos.length;
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * var obj = new CombinationIterator(characters, combinationLength)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
```

## Php

```php
class CombinationIterator {
    /**
     * @var array
     */
    private $combos = [];
    /**
     * @var int
     */
    private $idx = 0;

    /**
     * @param String $characters
     * @param Integer $combinationLength
     */
    function __construct($characters, $combinationLength) {
        $n = strlen($characters);
        $result = [];

        $dfs = function ($start, $path) use (&$dfs, $characters, $combinationLength, $n, &$result) {
            if (strlen($path) === $combinationLength) {
                $result[] = $path;
                return;
            }
            for ($i = $start; $i < $n; $i++) {
                $dfs($i + 1, $path . $characters[$i]);
            }
        };

        $dfs(0, "");
        $this->combos = $result;
        $this->idx = 0;
    }

    /**
     * @return String
     */
    function next() {
        return $this->combos[$this->idx++];
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->idx < count($this->combos);
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * $obj = new CombinationIterator($characters, $combinationLength);
 * $ret_1 = $obj->next();
 * $ret_2 = $obj->hasNext();
 */
```

## Swift

```swift
class CombinationIterator {
    private var combinations: [String] = []
    private var index: Int = 0

    init(_ characters: String, _ combinationLength: Int) {
        let chars = Array(characters)
        var path = [Character]()
        func dfs(_ start: Int) {
            if path.count == combinationLength {
                combinations.append(String(path))
                return
            }
            for i in start..<chars.count {
                path.append(chars[i])
                dfs(i + 1)
                path.removeLast()
            }
        }
        dfs(0)
    }

    func next() -> String {
        let result = combinations[index]
        index += 1
        return result
    }

    func hasNext() -> Bool {
        return index < combinations.count
    }
}
```

## Kotlin

```kotlin
class CombinationIterator(characters: String, private val combinationLength: Int) {

    private val combos: List<String>
    private var index = 0

    init {
        val result = mutableListOf<String>()
        fun backtrack(start: Int, sb: StringBuilder) {
            if (sb.length == combinationLength) {
                result.add(sb.toString())
                return
            }
            for (i in start until characters.length) {
                sb.append(characters[i])
                backtrack(i + 1, sb)
                sb.deleteCharAt(sb.length - 1)
            }
        }
        backtrack(0, StringBuilder())
        combos = result
    }

    fun next(): String {
        return combos[index++]
    }

    fun hasNext(): Boolean {
        return index < combos.size
    }
}
```

## Dart

```dart
class CombinationIterator {
  final List<String> _combinations = [];
  int _pos = 0;

  CombinationIterator(String characters, int combinationLength) {
    final List<String> chars = characters.split('');
    void dfs(int start, String cur) {
      if (cur.length == combinationLength) {
        _combinations.add(cur);
        return;
      }
      for (int i = start; i < chars.length; ++i) {
        dfs(i + 1, cur + chars[i]);
      }
    }

    dfs(0, '');
  }

  String next() {
    return _combination[_pos++];
  }

  bool hasNext() {
    return _pos < _combinations.length;
  }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = CombinationIterator(characters, combinationLength);
 * String param1 = obj.next();
 * bool param2 = obj.hasNext();
 */
```

## Golang

```go
type CombinationIterator struct {
	combos []string
	idx    int
}

func Constructor(characters string, combinationLength int) CombinationIterator {
	var res []string
	n := len(characters)
	var dfs func(start int, path []byte)
	dfs = func(start int, path []byte) {
		if len(path) == combinationLength {
			res = append(res, string(append([]byte{}, path...)))
			return
		}
		for i := start; i < n; i++ {
			path = append(path, characters[i])
			dfs(i+1, path)
			path = path[:len(path)-1]
		}
	}
	dfs(0, []byte{})
	return CombinationIterator{combos: res, idx: 0}
}

func (this *CombinationIterator) Next() string {
	if this.idx >= len(this.combos) {
		return ""
	}
	ans := this.combos[this.idx]
	this.idx++
	return ans
}

func (this *CombinationIterator) HasNext() bool {
	return this.idx < len(this.combos)
}
```

## Ruby

```ruby
class CombinationIterator
  # :type characters: String
  # :type combination_length: Integer
  def initialize(characters, combination_length)
    @chars = characters.chars
    @len = combination_length
    @combos = []
    dfs(0, [])
    @index = 0
  end

  # :rtype: String
  def next()
    result = @combos[@index]
    @index += 1
    result
  end

  # :rtype: Boolean
  def has_next()
    @index < @combos.size
  end

  private

  def dfs(start, path)
    if path.length == @len
      @combos << path.join
      return
    end
    (start...@chars.size).each do |i|
      path << @chars[i]
      dfs(i + 1, path)
      path.pop
    end
  end
end
```

## Scala

```scala
class CombinationIterator(_characters: String, _combinationLength: Int) {
  private val combos = scala.collection.mutable.ArrayBuffer[String]()
  private var index = 0

  private def dfs(start: Int, sb: StringBuilder): Unit = {
    if (sb.length == _combinationLength) {
      combos += sb.toString()
      return
    }
    for (i <- start until _characters.length) {
      sb.append(_characters.charAt(i))
      dfs(i + 1, sb)
      sb.deleteCharAt(sb.length - 1)
    }
  }

  dfs(0, new StringBuilder)

  def next(): String = {
    val res = combos(index)
    index += 1
    res
  }

  def hasNext(): Boolean = index < combos.length
}
```

## Rust

```rust
struct CombinationIterator {
    combinations: Vec<String>,
    index: usize,
}

impl CombinationIterator {
    fn new(characters: String, combinationLength: i32) -> Self {
        let chars: Vec<char> = characters.chars().collect();
        let k = combinationLength as usize;
        let mut combos = Vec::new();
        let mut cur = String::with_capacity(k);
        fn dfs(start: usize, k: usize, chars: &Vec<char>, cur: &mut String, res: &mut Vec<String>) {
            if cur.len() == k {
                res.push(cur.clone());
                return;
            }
            for i in start..chars.len() {
                cur.push(chars[i]);
                dfs(i + 1, k, chars, cur, res);
                cur.pop();
            }
        }
        dfs(0, k, &chars, &mut cur, &mut combos);
        CombinationIterator { combinations: combos, index: 0 }
    }

    fn next(&mut self) -> String {
        let result = self.combinations[self.index].clone();
        self.index += 1;
        result
    }

    fn has_next(&self) -> bool {
        self.index < self.combinations.len()
    }
}
```

## Racket

```racket
(define combination-iterator%
  (class object%
    (super-new)
    (init-field characters combination-length)

    ;; internal state
    (define combos '())
    (define cur 0)

    ;; pre‑compute all combinations in lexicographic order
    (begin
      (define n (string-length characters))
      (define k combination-length)
      (when (and (> n 0) (> k 0) (<= k n))
        (define idxs (make-vector k))
        (for ([i (in-range k)]) (vector-set! idxs i i))
        (define combos-rev '())
        (let loop ()
          ;; build current combination string
          (define combo
            (list->string
             (for/list ([i (in-range k)])
               (string-ref characters (vector-ref idxs i)))))
          (set! combos-rev (cons combo combos-rev))
          ;; find rightmost position that can be increased
          (define i -1)
          (for ([j (in-range (- k 1) -1 -1)])
            (when (= i -1)
              (when (< (vector-ref idxs j) (+ j (- n k)))
                (set! i j))))
          (if (= i -1)
              (void) ; all combinations generated
              (begin
                (vector-set! idxs i (+ (vector-ref idxs i) 1))
                (for ([j (in-range (+ i 1) k)])
                  (vector-set! idxs j (+ (vector-ref idxs (- j 1)) 1)))
                (loop))))
        (set! combos (reverse combos-rev))))

    (define total (length combos))

    ;; public methods
    (define/public (next)
      (define res (list-ref combos cur))
      (set! cur (+ cur 1))
      res)

    (define/public (has-next)
      (< cur total))))
```

## Erlang

```erlang
-module(solution).
-export([combination_iterator_init_/2,
         combination_iterator_next/0,
         combination_iterator_has_next/0]).

-spec combination_iterator_init_(Characters :: unicode:unicode_binary(), CombinationLength :: integer()) -> any().
combination_iterator_init_(Characters, CombinationLength) ->
    CharList = binary_to_list(Characters),
    CombList = gen_combinations(CharList, CombinationLength),
    put(comb_list, CombList),
    put(idx, 0),
    ok.

-spec combination_iterator_next() -> unicode:unicode_binary().
combination_iterator_next() ->
    Idx = get(idx),
    List = get(comb_list),
    Elem = lists:nth(Idx + 1, List),
    put(idx, Idx + 1),
    Elem.

-spec combination_iterator_has_next() -> boolean().
combination_iterator_has_next() ->
    Idx = get(idx),
    List = get(comb_list),
    Idx < length(List).

gen_combinations(_Chars, 0) ->
    [<<>>];
gen_combinations([], _K) ->
    [];
gen_combinations(Chars, K) when K > 0 ->
    case Chars of
        [] -> [];
        [H|T] ->
            With = gen_combinations(T, K - 1),
            WithPrefixed = [ <<H, Rest/binary>> || Rest <- With ],
            Without = gen_combinations(T, K),
            WithPrefixed ++ Without
    end.
```

## Elixir

```elixir
defmodule CombinationIterator do
  @spec init_(characters :: String.t(), combination_length :: integer) :: any()
  def init_(characters, combination_length) do
    combos = generate_combinations(String.graphemes(characters), combination_length)
    Process.put(:ci_combos, combos)
    Process.put(:ci_index, 0)
    :ok
  end

  @spec next() :: String.t()
  def next() do
    idx = Process.get(:ci_index, 0)
    combo = Process.get(:ci_combos) |> Enum.at(idx)
    Process.put(:ci_index, idx + 1)
    combo
  end

  @spec has_next() :: boolean()
  def has_next() do
    idx = Process.get(:ci_index, 0)
    combos = Process.get(:ci_combos, [])
    idx < length(combos)
  end

  # Helper to generate all combinations in lexicographic order
  defp generate_combinations(chars, k) do
    result = do_generate(chars, k, 0, [], [])
    Enum.reverse(result)
  end

  defp do_generate(_chars, k, _start, acc, result) when length(acc) == k do
    [Enum.join(acc) | result]
  end

  defp do_generate(chars, k, start, acc, result) do
    len = length(chars)
    needed = k - length(acc)
    Enum.reduce(start..(len - needed), result, fn i, res ->
      do_generate(chars, k, i + 1, acc ++ [Enum.at(chars, i)], res)
    end)
  end
end
```
