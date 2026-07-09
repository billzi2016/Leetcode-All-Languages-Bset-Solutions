# 0841. Keys and Rooms

## Cpp

```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> visited(n, false);
        stack<int> st;
        st.push(0);
        visited[0] = true;
        while (!st.empty()) {
            int cur = st.top();
            st.pop();
            for (int key : rooms[cur]) {
                if (!visited[key]) {
                    visited[key] = true;
                    st.push(key);
                }
            }
        }
        for (bool v : visited) {
            if (!v) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        boolean[] visited = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        visited[0] = true;
        while (!stack.isEmpty()) {
            int room = stack.pop();
            for (int key : rooms.get(room)) {
                if (!visited[key]) {
                    visited[key] = true;
                    stack.push(key);
                }
            }
        }
        for (boolean v : visited) {
            if (!v) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        stack = [0]
        visited[0] = True
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        return all(visited)
```

## Python3

```python
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        stack = [0]
        visited[0] = True
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)
        return all(visited)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize) {
    if (roomsSize == 0) return true;
    
    bool *visited = (bool *)calloc(roomsSize, sizeof(bool));
    int *stack = (int *)malloc(roomsSize * sizeof(int));
    int top = 0;
    
    // start from room 0
    visited[0] = true;
    stack[top++] = 0;
    
    while (top > 0) {
        int cur = stack[--top];
        int keysCount = roomsColSize[cur];
        for (int i = 0; i < keysCount; ++i) {
            int key = rooms[cur][i];
            if (!visited[key]) {
                visited[key] = true;
                stack[top++] = key;
            }
        }
    }
    
    bool allVisited = true;
    for (int i = 0; i < roomsSize; ++i) {
        if (!visited[i]) {
            allVisited = false;
            break;
        }
    }
    
    free(visited);
    free(stack);
    return allVisited;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool CanVisitAllRooms(IList<IList<int>> rooms) {
        int n = rooms.Count;
        var visited = new bool[n];
        var stack = new Stack<int>();
        stack.Push(0);
        visited[0] = true;
        
        while (stack.Count > 0) {
            int room = stack.Pop();
            foreach (int key in rooms[room]) {
                if (!visited[key]) {
                    visited[key] = true;
                    stack.Push(key);
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    const n = rooms.length;
    const visited = new Array(n).fill(false);
    const stack = [0];
    visited[0] = true;
    
    while (stack.length) {
        const room = stack.pop();
        for (const key of rooms[room]) {
            if (!visited[key]) {
                visited[key] = true;
                stack.push(key);
            }
        }
    }
    
    return visited.every(v => v);
};
```

## Typescript

```typescript
function canVisitAllRooms(rooms: number[][]): boolean {
    const n = rooms.length;
    const visited = new Array<boolean>(n).fill(false);
    const stack: number[] = [0];
    visited[0] = true;

    while (stack.length) {
        const room = stack.pop()!;
        for (const key of rooms[room]) {
            if (!visited[key]) {
                visited[key] = true;
                stack.push(key);
            }
        }
    }

    return visited.every(v => v);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rooms
     * @return Boolean
     */
    function canVisitAllRooms($rooms) {
        $n = count($rooms);
        $visited = array_fill(0, $n, false);
        $stack = [0];
        $visited[0] = true;

        while (!empty($stack)) {
            $room = array_pop($stack);
            foreach ($rooms[$room] as $key) {
                if (!$visited[$key]) {
                    $visited[$key] = true;
                    $stack[] = $key;
                }
            }
        }

        foreach ($visited as $v) {
            if (!$v) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        let n = rooms.count
        var visited = Array(repeating: false, count: n)
        var stack = [Int]()
        
        visited[0] = true
        stack.append(0)
        
        while let room = stack.popLast() {
            for key in rooms[room] {
                if !visited[key] {
                    visited[key] = true
                    stack.append(key)
                }
            }
        }
        
        return visited.allSatisfy { $0 }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canVisitAllRooms(rooms: List<List<Int>>): Boolean {
        val n = rooms.size
        val visited = BooleanArray(n)
        val stack = ArrayDeque<Int>()
        visited[0] = true
        stack.addLast(0)

        while (stack.isNotEmpty()) {
            val room = stack.removeLast()
            for (key in rooms[room]) {
                if (!visited[key]) {
                    visited[key] = true
                    stack.addLast(key)
                }
            }
        }

        for (v in visited) {
            if (!v) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canVisitAllRooms(List<List<int>> rooms) {
    int n = rooms.length;
    List<bool> visited = List.filled(n, false);
    List<int> stack = [0];
    visited[0] = true;

    while (stack.isNotEmpty) {
      int room = stack.removeLast();
      for (int key in rooms[room]) {
        if (!visited[key]) {
          visited[key] = true;
          stack.add(key);
        }
      }
    }

    for (bool v in visited) {
      if (!v) return false;
    }
    return true;
  }
}
```

## Golang

```go
func canVisitAllRooms(rooms [][]int) bool {
    n := len(rooms)
    visited := make([]bool, n)
    stack := []int{0}
    visited[0] = true

    for len(stack) > 0 {
        cur := stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        for _, key := range rooms[cur] {
            if !visited[key] {
                visited[key] = true
                stack = append(stack, key)
            }
        }
    }

    for i := 0; i < n; i++ {
        if !visited[i] {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def can_visit_all_rooms(rooms)
  n = rooms.size
  visited = Array.new(n, false)
  stack = [0]
  visited[0] = true

  until stack.empty?
    room = stack.pop
    rooms[room].each do |key|
      next if visited[key]
      visited[key] = true
      stack << key
    end
  end

  visited.all?
end
```

## Scala

```scala
object Solution {
    def canVisitAllRooms(rooms: List[List[Int]]): Boolean = {
        val n = rooms.length
        val visited = new Array[Boolean](n)
        val stack = scala.collection.mutable.Stack[Int]()
        visited(0) = true
        stack.push(0)

        while (stack.nonEmpty) {
            val room = stack.pop()
            for (key <- rooms(room)) {
                if (!visited(key)) {
                    visited(key) = true
                    stack.push(key)
                }
            }
        }

        visited.forall(_ == true)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let n = rooms.len();
        let mut visited = vec![false; n];
        let mut stack = Vec::new();

        visited[0] = true;
        stack.push(0usize);

        while let Some(room) = stack.pop() {
            for &key in &rooms[room] {
                let k = key as usize;
                if !visited[k] {
                    visited[k] = true;
                    stack.push(k);
                }
            }
        }

        visited.iter().all(|&v| v)
    }
}
```

## Racket

```racket
(define/contract (can-visit-all-rooms rooms)
  (-> (listof (listof exact-integer?)) boolean?)
  (let* ((n (length rooms))
         (visited (make-vector n #f)))
    (vector-set! visited 0 #t)
    (let loop ((stack '(0)))
      (if (null? stack)
          (for/and ([i (in-range n)])
            (vector-ref visited i))
          (let* ((room (car stack))
                 (rest (cdr stack))
                 (keys (list-ref rooms room))
                 (new-stack
                  (foldl (lambda (key acc)
                           (if (not (vector-ref visited key))
                               (begin
                                 (vector-set! visited key #t)
                                 (cons key acc))
                               acc))
                         rest
                         keys)))
            (loop new-stack))))))
```

## Erlang

```erlang
-spec can_visit_all_rooms(Rooms :: [[integer()]]) -> boolean().
can_visit_all_rooms(Rooms) ->
    N = length(Rooms),
    Seen0 = #{0 => true},
    dfs([0], Seen0, Rooms, N).

dfs([], Seen, _Rooms, N) ->
    map_size(Seen) == N;
dfs([Room | RestStack], Seen, Rooms, N) ->
    Keys = lists:nth(Room + 1, Rooms),
    NewKeys = [K || K <- Keys, not maps:is_key(K, Seen)],
    NewSeen = lists:foldl(fun(K, Acc) -> maps:put(K, true, Acc) end, Seen, NewKeys),
    dfs(NewKeys ++ RestStack, NewSeen, Rooms, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_visit_all_rooms(rooms :: [[integer]]) :: boolean
  def can_visit_all_rooms(rooms) do
    n = length(rooms)
    visited = dfs([0], MapSet.new([0]), rooms)
    MapSet.size(visited) == n
  end

  defp dfs([], visited, _rooms), do: visited

  defp dfs([room | rest], visited, rooms) do
    keys = Enum.at(rooms, room)

    {new_visited, new_stack} =
      Enum.reduce(keys, {visited, rest}, fn key, {vis, stk} ->
        if MapSet.member?(vis, key) do
          {vis, stk}
        else
          {MapSet.put(vis, key), [key | stk]}
        end
      end)

    dfs(new_stack, new_visited, rooms)
  end
end
```
