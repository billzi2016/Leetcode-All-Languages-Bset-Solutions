# 1640. Check Array Formation Through Concatenation

## Cpp

```cpp
class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, const vector<int>*> mp;
        for (const auto& p : pieces) {
            if (!p.empty())
                mp[p[0]] = &p;
        }
        int i = 0, n = arr.size();
        while (i < n) {
            auto it = mp.find(arr[i]);
            if (it == mp.end()) return false;
            const vector<int>* piece = it->second;
            for (int val : *piece) {
                if (i >= n || arr[i] != val) return false;
                ++i;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        java.util.Map<Integer, int[]> map = new java.util.HashMap<>();
        for (int[] p : pieces) {
            if (p.length > 0) {
                map.put(p[0], p);
            }
        }
        int i = 0;
        while (i < arr.length) {
            int[] piece = map.get(arr[i]);
            if (piece == null) return false;
            for (int val : piece) {
                if (i >= arr.length || arr[i] != val) return false;
                i++;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        first_map = {p[0]: p for p in pieces}
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] not in first_map:
                return False
            piece = first_map[arr[i]]
            for val in piece:
                if i >= n or arr[i] != val:
                    return False
                i += 1
        return True
```

## Python3

```python
class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        first_to_piece = {p[0]: p for p in pieces}
        i = 0
        n = len(arr)
        while i < n:
            val = arr[i]
            if val not in first_to_piece:
                return False
            piece = first_to_piece[val]
            for x in piece:
                if i >= n or arr[i] != x:
                    return False
                i += 1
        return True
```

## C

```c
#include <stdbool.h>

bool canFormArray(int* arr, int arrSize, int** pieces, int piecesSize, int* piecesColSize){
    int i = 0;
    while (i < arrSize) {
        bool matched = false;
        for (int p = 0; p < piecesSize; ++p) {
            if (pieces[p][0] == arr[i]) {
                int len = piecesColSize[p];
                for (int k = 0; k < len; ++k) {
                    if (i + k >= arrSize || arr[i + k] != pieces[p][k])
                        return false;
                }
                i += len;
                matched = true;
                break;
            }
        }
        if (!matched) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanFormArray(int[] arr, int[][] pieces) {
        var map = new Dictionary<int, int[]>();
        foreach (var p in pieces) {
            if (p.Length > 0) {
                map[p[0]] = p;
            }
        }

        int i = 0;
        while (i < arr.Length) {
            if (!map.TryGetValue(arr[i], out var piece)) return false;
            for (int j = 0; j < piece.Length; j++) {
                if (i + j >= arr.Length || arr[i + j] != piece[j]) return false;
            }
            i += piece.Length;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} pieces
 * @return {boolean}
 */
var canFormArray = function(arr, pieces) {
    const map = new Map();
    for (const p of pieces) {
        map.set(p[0], p);
    }
    let i = 0;
    while (i < arr.length) {
        const piece = map.get(arr[i]);
        if (!piece) return false;
        for (let j = 0; j < piece.length; ++j) {
            if (arr[i + j] !== piece[j]) return false;
        }
        i += piece.length;
    }
    return true;
};
```

## Typescript

```typescript
function canFormArray(arr: number[], pieces: number[][]): boolean {
    const pieceMap = new Map<number, number[]>();
    for (const p of pieces) {
        if (p.length > 0) {
            pieceMap.set(p[0], p);
        }
    }

    let i = 0;
    while (i < arr.length) {
        const piece = pieceMap.get(arr[i]);
        if (!piece) return false;
        for (let j = 0; j < piece.length; ++j) {
            if (arr[i + j] !== piece[j]) return false;
        }
        i += piece.length;
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $pieces
     * @return Boolean
     */
    function canFormArray($arr, $pieces) {
        $map = [];
        foreach ($pieces as $p) {
            if (!empty($p)) {
                $map[$p[0]] = $p;
            }
        }

        $i = 0;
        $n = count($arr);
        while ($i < $n) {
            $val = $arr[$i];
            if (!isset($map[$val])) {
                return false;
            }
            foreach ($map[$val] as $num) {
                if ($i >= $n || $arr[$i] != $num) {
                    return false;
                }
                $i++;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canFormArray(_ arr: [Int], _ pieces: [[Int]]) -> Bool {
        var pieceMap = [Int: [Int]]()
        for p in pieces {
            if let first = p.first {
                pieceMap[first] = p
            }
        }
        var i = 0
        while i < arr.count {
            guard let piece = pieceMap[arr[i]] else { return false }
            for val in piece {
                if i >= arr.count || arr[i] != val {
                    return false
                }
                i += 1
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canFormArray(arr: IntArray, pieces: Array<IntArray>): Boolean {
        val map = HashMap<Int, IntArray>()
        for (p in pieces) {
            if (p.isNotEmpty()) {
                map[p[0]] = p
            }
        }
        var i = 0
        while (i < arr.size) {
            val piece = map[arr[i]] ?: return false
            for (v in piece) {
                if (i >= arr.size || arr[i] != v) return false
                i++
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canFormArray(List<int> arr, List<List<int>> pieces) {
    final Map<int, List<int>> firstToPiece = {};
    for (var p in pieces) {
      if (p.isNotEmpty) {
        firstToPiece[p[0]] = p;
      }
    }

    int i = 0;
    while (i < arr.length) {
      if (!firstToPiece.containsKey(arr[i])) return false;
      final piece = firstToPiece[arr[i]]!;
      for (int j = 0; j < piece.length; ++j) {
        if (i + j >= arr.length || arr[i + j] != piece[j]) return false;
      }
      i += piece.length;
    }

    return true;
  }
}
```

## Golang

```go
func canFormArray(arr []int, pieces [][]int) bool {
	m := make(map[int][]int)
	for _, p := range pieces {
		if len(p) > 0 {
			m[p[0]] = p
		}
	}
	i := 0
	for i < len(arr) {
		piece, ok := m[arr[i]]
		if !ok {
			return false
		}
		for _, v := range piece {
			if i >= len(arr) || arr[i] != v {
				return false
			}
			i++
		}
	}
	return true
}
```

## Ruby

```ruby
def can_form_array(arr, pieces)
  piece_map = {}
  pieces.each { |p| piece_map[p[0]] = p }

  i = 0
  while i < arr.length
    piece = piece_map[arr[i]]
    return false unless piece

    piece.each do |val|
      return false if arr[i] != val
      i += 1
    end
  end

  true
end
```

## Scala

```scala
object Solution {
    def canFormArray(arr: Array[Int], pieces: Array[Array[Int]]): Boolean = {
        val firstToPiece = scala.collection.mutable.Map[Int, Array[Int]]()
        for (p <- pieces) {
            if (p.nonEmpty) firstToPiece(p(0)) = p
        }
        var i = 0
        while (i < arr.length) {
            firstToPiece.get(arr(i)) match {
                case None => return false
                case Some(piece) =>
                    for (j <- piece.indices) {
                        if (i + j >= arr.length || arr(i + j) != piece(j)) return false
                    }
                    i += piece.length
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_form_array(arr: Vec<i32>, pieces: Vec<Vec<i32>>) -> bool {
        use std::collections::HashMap;
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();
        for piece in pieces {
            if let Some(&first) = piece.first() {
                map.insert(first, piece);
            }
        }
        let mut i = 0usize;
        while i < arr.len() {
            match map.get(&arr[i]) {
                Some(piece) => {
                    for &val in piece.iter() {
                        if i >= arr.len() || arr[i] != val {
                            return false;
                        }
                        i += 1;
                    }
                }
                None => return false,
            }
        }
        true
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (can-form-array arr pieces)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) boolean?)
  (let ([first->piece (make-hash)])
    (for ([p pieces])
      (hash-set! first->piece (first p) p))
    (let loop ((i 0) (n (length arr)))
      (if (= i n)
          #t
          (let* ([val (list-ref arr i)]
                 [piece (hash-ref first->piece val #f)])
            (if (not piece)
                #f
                (let ([len (length piece)])
                  (if (and (<= (+ i len) n)
                           (equal? (take (drop arr i) len) piece))
                      (loop (+ i len) n)
                      #f))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_form_array/2]).

-spec can_form_array(Arr :: [integer()], Pieces :: [[integer()]]) -> boolean().
can_form_array(Arr, Pieces) ->
    Map = build_map(Pieces, #{}),
    check_arr(Arr, Map).

build_map([], M) -> M;
build_map([Piece|Rest], M) ->
    [First|_] = Piece,
    build_map(Rest, maps:put(First, Piece, M)).

check_arr([], _Map) -> true;
check_arr([H|_]=Arr, Map) ->
    case maps:get(H, Map, undefined) of
        undefined -> false;
        Piece ->
            case match_piece(Piece, Arr) of
                {ok, RestArr} -> check_arr(RestArr, Map);
                false -> false
            end
    end.

match_piece([], Rest) -> {ok, Rest};
match_piece([H|T], [H|Rest]) -> match_piece(T, Rest);
match_piece(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_form_array(arr :: [integer], pieces :: [[integer]]) :: boolean
  def can_form_array(arr, pieces) do
    piece_map =
      Enum.reduce(pieces, %{}, fn [head | _] = piece, acc ->
        Map.put(acc, head, piece)
      end)

    check(arr, piece_map)
  end

  defp check([], _), do: true

  defp check([h | _] = remaining, map) do
    case Map.get(map, h) do
      nil -> false
      piece ->
        len = length(piece)
        {prefix, rest} = Enum.split(remaining, len)

        if prefix == piece do
          check(rest, map)
        else
          false
        end
    end
  end
end
```
