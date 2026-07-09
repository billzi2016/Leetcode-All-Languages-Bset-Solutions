# 2115. Find All Possible Recipes from Given Supplies

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_set<string> available(supplies.begin(), supplies.end());
        int n = recipes.size();
        unordered_map<string,int> idx;
        for (int i = 0; i < n; ++i) idx[recipes[i]] = i;
        
        vector<int> indegree(n, 0);
        unordered_map<string, vector<int>> graph; // ingredient -> list of recipes needing it
        
        for (int i = 0; i < n; ++i) {
            for (const string& ing : ingredients[i]) {
                if (!available.count(ing)) {
                    graph[ing].push_back(i);
                    ++indegree[i];
                }
            }
        }
        
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) q.push(i);
        }
        
        vector<string> result;
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            const string& made = recipes[cur];
            result.push_back(made);
            // this recipe can now serve as an ingredient
            if (graph.count(made)) {
                for (int nxt : graph[made]) {
                    if (--indegree[nxt] == 0) q.push(nxt);
                }
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        Set<String> available = new HashSet<>(Arrays.asList(supplies));
        int n = recipes.length;
        Map<String, Integer> recipeIndex = new HashMap<>();
        for (int i = 0; i < n; i++) {
            recipeIndex.put(recipes[i], i);
        }

        int[] indegree = new int[n];
        Map<String, List<Integer>> graph = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (String ing : ingredients.get(i)) {
                if (!available.contains(ing)) {
                    indegree[i]++;
                    graph.computeIfAbsent(ing, k -> new ArrayList<>()).add(i);
                }
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        List<String> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            String recipeName = recipes[cur];
            result.add(recipeName);
            List<Integer> dependents = graph.get(recipeName);
            if (dependents != null) {
                for (int nxt : dependents) {
                    indegree[nxt]--;
                    if (indegree[nxt] == 0) {
                        queue.offer(nxt);
                    }
                }
            }
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        from collections import deque, defaultdict

        supply_set = set(supplies)
        n = len(recipes)

        indegree = [0] * n
        graph = defaultdict(list)  # ingredient -> list of recipe indices that need it

        for i in range(n):
            for ing in ingredients[i]:
                if ing not in supply_set:
                    indegree[i] += 1
                    graph[ing].append(i)

        q = deque([i for i in range(n) if indegree[i] == 0])
        result = []

        while q:
            idx = q.popleft()
            recipe_name = recipes[idx]
            result.append(recipe_name)
            # this newly created recipe becomes an available ingredient
            for dependent in graph.get(recipe_name, []):
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)

        return result
```

## Python3

```python
from typing import List
from collections import deque, defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipe_index = {r: i for i, r in enumerate(recipes)}
        indegree = [0] * len(recipes)
        graph = defaultdict(list)  # ingredient -> list of recipes that need it

        for i, ing_list in enumerate(ingredients):
            for ing in ing_list:
                if ing not in supply_set:
                    indegree[i] += 1
                    graph[ing].append(i)

        q = deque([i for i, deg in enumerate(indegree) if deg == 0])
        result = []

        while q:
            idx = q.popleft()
            recipe_name = recipes[idx]
            result.append(recipe_name)
            # this newly made recipe can serve as an ingredient
            for nxt in graph.get(recipe_name, []):
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findAllRecipes(char** recipes, int recipesSize,
                      char*** ingredients, int ingredientsSize,
                      int* ingredientsColSize,
                      char** supplies, int suppliesSize,
                      int* returnSize) {
    // indegree for each recipe
    int *indeg = (int *)calloc(recipesSize, sizeof(int));
    bool *made = (bool *)calloc(recipesSize, sizeof(bool));
    bool *inQueue = (bool *)calloc(recipesSize, sizeof(bool));

    // compute initial indegrees based on supplies only
    for (int i = 0; i < recipesSize; ++i) {
        int cnt = 0;
        for (int j = 0; j < ingredientsColSize[i]; ++j) {
            char *ing = ingredients[i][j];
            bool found = false;
            for (int s = 0; s < suppliesSize; ++s) {
                if (strcmp(ing, supplies[s]) == 0) {
                    found = true;
                    break;
                }
            }
            if (!found) cnt++;
        }
        indeg[i] = cnt;
    }

    // queue for recipes ready to make
    int *queue = (int *)malloc(recipesSize * sizeof(int));
    int qhead = 0, qtail = 0;

    for (int i = 0; i < recipesSize; ++i) {
        if (indeg[i] == 0) {
            queue[qtail++] = i;
            inQueue[i] = true;
        }
    }

    char **result = (char **)malloc(recipesSize * sizeof(char *));
    int resCount = 0;

    while (qhead < qtail) {
        int idx = queue[qhead++];
        made[idx] = true;
        result[resCount++] = recipes[idx];

        // this recipe becomes an available ingredient
        const char *newIng = recipes[idx];

        for (int j = 0; j < recipesSize; ++j) {
            if (made[j]) continue; // already completed
            // check if recipe j needs newIng
            bool decreased = false;
            for (int k = 0; k < ingredientsColSize[j]; ++k) {
                if (strcmp(ingredients[j][k], newIng) == 0) {
                    indeg[j]--;
                    decreased = true;
                    break; // each ingredient appears at most once per recipe
                }
            }
            if (decreased && indeg[j] == 0 && !inQueue[j]) {
                queue[qtail++] = j;
                inQueue[j] = true;
            }
        }
    }

    *returnSize = resCount;

    free(indeg);
    free(made);
    free(inQueue);
    free(queue);

    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> FindAllRecipes(string[] recipes, IList<IList<string>> ingredients, string[] supplies) {
        var supplySet = new HashSet<string>(supplies);
        int n = recipes.Length;
        var recipeIndex = new Dictionary<string, int>();
        for (int i = 0; i < n; i++) {
            recipeIndex[recipes[i]] = i;
        }

        var indegree = new int[n];
        var graph = new Dictionary<string, List<int>>();

        for (int i = 0; i < n; i++) {
            foreach (var ing in ingredients[i]) {
                if (!supplySet.Contains(ing)) {
                    indegree[i]++;
                    if (!graph.TryGetValue(ing, out var list)) {
                        list = new List<int>();
                        graph[ing] = list;
                    }
                    list.Add(i);
                }
            }
        }

        var queue = new Queue<int>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.Enqueue(i);
            }
        }

        var result = new List<string>();
        while (queue.Count > 0) {
            int idx = queue.Dequeue();
            string recipe = recipes[idx];
            result.Add(recipe);

            if (graph.TryGetValue(recipe, out var dependents)) {
                foreach (int nxt in dependents) {
                    indegree[nxt]--;
                    if (indegree[nxt] == 0) {
                        queue.Enqueue(nxt);
                    }
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function(recipes, ingredients, supplies) {
    const available = new Set(supplies);
    const graph = new Map(); // ingredient -> list of recipe indices that need it
    const indegree = new Array(recipes.length).fill(0);

    for (let i = 0; i < recipes.length; ++i) {
        for (const ing of ingredients[i]) {
            if (!available.has(ing)) {
                indegree[i] += 1;
                if (!graph.has(ing)) graph.set(ing, []);
                graph.get(ing).push(i);
            }
        }
    }

    const queue = [];
    for (let i = 0; i < recipes.length; ++i) {
        if (indegree[i] === 0) queue.push(i);
    }

    const result = [];
    let qIdx = 0;
    while (qIdx < queue.length) {
        const idx = queue[qIdx++];
        const rec = recipes[idx];
        result.push(rec);
        available.add(rec);

        if (!graph.has(rec)) continue;
        for (const nxt of graph.get(rec)) {
            indegree[nxt] -= 1;
            if (indegree[nxt] === 0) queue.push(nxt);
        }
    }

    return result;
};
```

## Typescript

```typescript
function findAllRecipes(recipes: string[], ingredients: string[][], supplies: string[]): string[] {
    const supplySet = new Set<string>(supplies);
    const graph = new Map<string, number[]>(); // ingredient -> list of recipe indices that need it
    const indegree = new Array(recipes.length).fill(0);

    for (let i = 0; i < recipes.length; i++) {
        for (const ing of ingredients[i]) {
            if (!supplySet.has(ing)) {
                indegree[i]++;
                if (!graph.has(ing)) graph.set(ing, []);
                graph.get(ing)!.push(i);
            }
        }
    }

    const queue: number[] = [];
    for (let i = 0; i < recipes.length; i++) {
        if (indegree[i] === 0) queue.push(i);
    }

    const result: string[] = [];

    while (queue.length) {
        const idx = queue.shift()!;
        const recipeName = recipes[idx];
        result.push(recipeName);

        // The newly created recipe becomes an available ingredient
        if (!graph.has(recipeName)) continue;
        for (const dependentIdx of graph.get(recipeName)!) {
            indegree[dependentIdx]--;
            if (indegree[dependentIdx] === 0) queue.push(dependentIdx);
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $recipes
     * @param String[][] $ingredients
     * @param String[] $supplies
     * @return String[]
     */
    function findAllRecipes($recipes, $ingredients, $supplies) {
        $available = array_flip($supplies); // set of current supplies

        $n = count($recipes);
        $recipeToIdx = [];
        for ($i = 0; $i < $n; $i++) {
            $recipeToIdx[$recipes[$i]] = $i;
        }

        $inDegree = array_fill(0, $n, 0);
        $graph = []; // ingredient => list of recipe indices that need it

        for ($i = 0; $i < $n; $i++) {
            foreach ($ingredients[$i] as $ing) {
                if (!isset($available[$ing])) {
                    $inDegree[$i]++;
                    if (!isset($graph[$ing])) {
                        $graph[$ing] = [];
                    }
                    $graph[$ing][] = $i;
                }
            }
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($inDegree[$i] === 0) {
                $queue->enqueue($i);
            }
        }

        $result = [];
        while (!$queue->isEmpty()) {
            $idx = $queue->dequeue();
            $recipeName = $recipes[$idx];
            $result[] = $recipeName;

            // this recipe becomes an available ingredient
            if (isset($graph[$recipeName])) {
                foreach ($graph[$recipeName] as $nextIdx) {
                    $inDegree[$nextIdx]--;
                    if ($inDegree[$nextIdx] === 0) {
                        $queue->enqueue($nextIdx);
                    }
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findAllRecipes(_ recipes: [String], _ ingredients: [[String]], _ supplies: [String]) -> [String] {
        let n = recipes.count
        var supplySet = Set<String>(supplies)
        var recipeIndex = [String: Int]()
        for i in 0..<n {
            recipeIndex[recipes[i]] = i
        }
        
        var graph = [String: [Int]]()
        var indegree = Array(repeating: 0, count: n)
        
        for i in 0..<n {
            for ing in ingredients[i] {
                if !supplySet.contains(ing) {
                    indegree[i] += 1
                    graph[ing, default: []].append(i)
                }
            }
        }
        
        var queue = [Int]()
        var head = 0
        for i in 0..<n where indegree[i] == 0 {
            queue.append(i)
        }
        
        var result = [String]()
        while head < queue.count {
            let idx = queue[head]
            head += 1
            let recipeName = recipes[idx]
            result.append(recipeName)
            if let dependents = graph[recipeName] {
                for nextIdx in dependents {
                    indegree[nextIdx] -= 1
                    if indegree[nextIdx] == 0 {
                        queue.append(nextIdx)
                    }
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findAllRecipes(recipes: Array<String>, ingredients: List<List<String>>, supplies: Array<String>): List<String> {
        val supplySet = HashSet<String>()
        for (s in supplies) supplySet.add(s)

        val n = recipes.size
        val indegree = IntArray(n)
        val adj = HashMap<String, MutableList<Int>>()

        for (i in 0 until n) {
            for (ing in ingredients[i]) {
                if (!supplySet.contains(ing)) {
                    indegree[i]++
                    adj.getOrPut(ing) { mutableListOf() }.add(i)
                }
            }
        }

        val queue: ArrayDeque<Int> = ArrayDeque()
        for (i in 0 until n) {
            if (indegree[i] == 0) queue.add(i)
        }

        val result = mutableListOf<String>()
        while (queue.isNotEmpty()) {
            val idx = queue.removeFirst()
            val name = recipes[idx]
            result.add(name)

            val dependents = adj[name] ?: continue
            for (nextIdx in dependents) {
                indegree[nextIdx]--
                if (indegree[nextIdx] == 0) {
                    queue.add(nextIdx)
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<String> findAllRecipes(
      List<String> recipes, List<List<String>> ingredients, List<String> supplies) {
    int n = recipes.length;
    Map<String, int> recipeIndex = {};
    for (int i = 0; i < n; i++) {
      recipeIndex[recipes[i]] = i;
    }

    Set<String> available = supplies.toSet();

    // adjacency: ingredient -> list of recipes that need it
    Map<String, List<int>> graph = {};

    List<int> indegree = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      for (String ing in ingredients[i]) {
        if (!available.contains(ing)) {
          indegree[i]++;
          graph.putIfAbsent(ing, () => []).add(i);
        }
      }
    }

    Queue<int> q = ListQueue<int>();
    for (int i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        q.addLast(i);
      }
    }

    List<String> result = [];

    while (q.isNotEmpty) {
      int idx = q.removeFirst();
      String madeRecipe = recipes[idx];
      result.add(madeRecipe);
      // this recipe becomes an available ingredient
      if (graph.containsKey(madeRecipe)) {
        for (int nxt in graph[madeRecipe]!) {
          indegree[nxt]--;
          if (indegree[nxt] == 0) {
            q.addLast(nxt);
          }
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	supplySet := make(map[string]bool)
	for _, s := range supplies {
		supplySet[s] = true
	}
	n := len(recipes)
	indegree := make([]int, n)
	graph := make(map[string][]int)

	for i, ingList := range ingredients {
		for _, ing := range ingList {
			if !supplySet[ing] {
				indegree[i]++
				graph[ing] = append(graph[ing], i)
			}
		}
	}

	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if indegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	res := make([]string, 0)
	for len(queue) > 0 {
		idx := queue[0]
		queue = queue[1:]
		res = append(res, recipes[idx])
		name := recipes[idx]
		if deps, ok := graph[name]; ok {
			for _, depIdx := range deps {
				indegree[depIdx]--
				if indegree[depIdx] == 0 {
					queue = append(queue, depIdx)
				}
			}
		}
	}

	return res
}
```

## Ruby

```ruby
require 'set'

# @param {String[]} recipes
# @param {String[][]} ingredients
# @param {String[]} supplies
# @return {String[]}
def find_all_recipes(recipes, ingredients, supplies)
  supply_set = Set.new(supplies)

  n = recipes.length
  indegree = Array.new(n, 0)
  graph = Hash.new { |h, k| h[k] = [] }

  recipe_index = {}
  recipes.each_with_index { |r, i| recipe_index[r] = i }

  recipes.each_with_index do |recipe, idx|
    ingredients[idx].each do |ing|
      next if supply_set.include?(ing)
      indegree[idx] += 1
      graph[ing] << idx
    end
  end

  queue = []
  n.times { |i| queue << i if indegree[i] == 0 }

  result = []

  until queue.empty?
    cur = queue.shift
    result << recipes[cur]

    # the newly created recipe can serve as an ingredient
    graph[recipes[cur]].each do |nbr|
      indegree[nbr] -= 1
      queue << nbr if indegree[nbr] == 0
    end if graph.key?(recipes[cur])
  end

  result
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def findAllRecipes(recipes: Array[String], ingredients: List[List[String]], supplies: Array[String]): List[String] = {
        val n = recipes.length
        val indegree = new Array[Int](n)
        val adj = mutable.Map[String, mutable.ArrayBuffer[Int]]()
        val supplySet = mutable.HashSet[String]()
        supplies.foreach(supplySet.add)

        // Map recipe name to its index (optional for this solution)
        // Build graph and indegrees
        for (i <- recipes.indices) {
            for (ing <- ingredients(i)) {
                if (!supplySet.contains(ing)) {
                    indegree(i) += 1
                    adj.getOrElseUpdate(ing, mutable.ArrayBuffer[Int]()).append(i)
                }
            }
        }

        val queue = mutable.Queue[Int]()
        for (i <- recipes.indices) {
            if (indegree(i) == 0) queue.enqueue(i)
        }

        val result = mutable.ListBuffer[String]()

        while (queue.nonEmpty) {
            val curIdx = queue.dequeue()
            val curName = recipes(curIdx)
            result += curName

            // This recipe becomes an available ingredient
            if (adj.contains(curName)) {
                for (nextIdx <- adj(curName)) {
                    indegree(nextIdx) -= 1
                    if (indegree(nextIdx) == 0) queue.enqueue(nextIdx)
                }
            }
        }

        result.toList
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn find_all_recipes(
        recipes: Vec<String>,
        ingredients: Vec<Vec<String>>,
        supplies: Vec<String>,
    ) -> Vec<String> {
        let n = recipes.len();
        // Map recipe name to its index
        let mut recipe_idx: HashMap<&str, usize> = HashMap::new();
        for (i, r) in recipes.iter().enumerate() {
            recipe_idx.insert(r.as_str(), i);
        }

        // Set of initial supplies for quick lookup
        let supply_set: HashSet<&str> = supplies.iter().map(|s| s.as_str()).collect();

        // indegree count for each recipe
        let mut indeg = vec![0usize; n];
        // adjacency list: ingredient -> list of recipes that need it
        let mut graph: HashMap<String, Vec<usize>> = HashMap::new();

        for (i, ing_list) in ingredients.iter().enumerate() {
            for ing in ing_list {
                if supply_set.contains(ing.as_str()) {
                    // already available, no edge needed
                    continue;
                }
                // Edge from ingredient to recipe i
                graph.entry(ing.clone()).or_default().push(i);
                indeg[i] += 1;
            }
        }

        let mut q: VecDeque<usize> = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }

        let mut result: Vec<String> = Vec::new();

        while let Some(idx) = q.pop_front() {
            // we can make this recipe
            result.push(recipes[idx].clone());

            // treat the newly made recipe as an available ingredient
            if let Some(dependents) = graph.get(&recipes[idx]) {
                for &next in dependents {
                    indeg[next] -= 1;
                    if indeg[next] == 0 {
                        q.push_back(next);
                    }
                }
            }
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(require racket/queue)

(define/contract (find-all-recipes recipes ingredients supplies)
  (-> (listof string?) (listof (listof string?)) (listof string?) (listof string?))
  (let* ((n (length recipes))
         (supplies-set (make-hash))
         (adj (make-hash))
         (indegree (make-vector n 0)))
    ;; record initial supplies
    (for ([s (in-list supplies)])
      (hash-set! supplies-set s #t))
    ;; build graph and indegree counts
    (for ([i (in-range n)])
      (let ((ings (list-ref ingredients i)))
        (for ([ing (in-list ings)])
          (unless (hash-has-key? supplies-set ing)
            (vector-set! indegree i (+ 1 (vector-ref indegree i)))
            (hash-set! adj ing (cons i (hash-ref adj ing '())))))))
    ;; queue of recipes ready to make
    (define q (make-queue))
    (for ([i (in-range n)])
      (when (= (vector-ref indegree i) 0)
        (enqueue! q i)))
    ;; process queue
    (let loop ((result '()))
      (if (queue-empty? q)
          (reverse result)
          (let* ((idx (dequeue! q))
                 (rec-name (list-ref recipes idx))
                 (new-result (cons rec-name result)))
            (for ([dep (in-list (hash-ref adj rec-name '()))])
              (vector-set! indegree dep (- (vector-ref indegree dep) 1))
              (when (= (vector-ref indegree dep) 0)
                (enqueue! q dep)))
            (loop new-result))))))
```

## Erlang

```erlang
-spec find_all_recipes(Recipes :: [unicode:unicode_binary()], Ingredients :: [[unicode:unicode_binary()]], Supplies :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_all_recipes(Recipes, Ingredients, Supplies) ->
    SupplySet = lists:foldl(fun(S, Acc) -> maps:put(S, true, Acc) end, #{}, Supplies),
    RecipeIdxMap = maps:from_list(lists:zip(Recipes, lists:seq(0, length(Recipes) - 1))),
    {Graph, InDeg} = build_graph(Recipes, Ingredients, SupplySet, RecipeIdxMap),
    Queue0 = [Idx || {Idx, Deg} <- maps:to_list(InDeg), Deg == 0],
    Result = bfs(Queue0, Graph, InDeg, Recipes, []),
    lists:reverse(Result).

-spec build_graph([unicode:unicode_binary()], [[unicode:unicode_binary()]], map(), map()) -> {map(), map()}.
build_graph(Recipes, Ingredients, SupplySet, RecipeIdxMap) ->
    EmptyGraph = #{},
    InitInDeg = maps:from_list(lists:map(fun(I) -> {I, 0} end, lists:seq(0, length(Recipes) - 1))),
    build_graph_loop(Recipes, Ingredients, SupplySet, RecipeIdxMap, EmptyGraph, InitInDeg).

-spec build_graph_loop([unicode:unicode_binary()], [[unicode:unicode_binary()]], map(), map(), map(), map()) -> {map(), map()}.
build_graph_loop([], [], _SupplySet, _RecipeIdxMap, Graph, InDeg) ->
    {Graph, InDeg};
build_graph_loop([R | RestR], [IngList | RestI], SupplySet, RecipeIdxMap, GraphAcc, InDegAcc) ->
    Idx = maps:get(R, RecipeIdxMap),
    {NewGraph, NewInDeg} =
        lists:foldl(
            fun(Ing, {G, D}) ->
                case maps:is_key(Ing, SupplySet) of
                    true -> {G, D};
                    false ->
                        G1 = maps:update_with(
                                Ing,
                                fun(L) -> [Idx | L] end,
                                [Idx],
                                G),
                        CurrDeg = maps:get(Idx, D),
                        D1 = maps:put(Idx, CurrDeg + 1, D),
                        {G1, D1}
                end
            end,
            {GraphAcc, InDegAcc},
            IngList),
    build_graph_loop(RestR, RestI, SupplySet, RecipeIdxMap, NewGraph, NewInDeg).

-spec bfs([non_neg_integer()], map(), map(), [unicode:unicode_binary()], [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
bfs([], _Graph, _InDeg, _Recipes, Acc) ->
    Acc;
bfs([Idx | Queue], Graph, InDeg, Recipes, Acc) ->
    RecipeName = lists:nth(Idx + 1, Recipes),
    Dependents = maps:get(RecipeName, Graph, []),
    {UpdatedInDeg, UpdatedQueue} =
        lists:foldl(
            fun(DIdx, {DegMap, Q}) ->
                Curr = maps:get(DIdx, DegMap),
                NewVal = Curr - 1,
                DegMap2 = maps:put(DIdx, NewVal, DegMap),
                if
                    NewVal == 0 -> {DegMap2, Q ++ [DIdx]};
                    true -> {DegMap2, Q}
                end
            end,
            {InDeg, Queue},
            Dependents),
    bfs(UpdatedQueue, Graph, UpdatedInDeg, Recipes, [RecipeName | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_all_recipes(recipes :: [String.t()], ingredients :: [[String.t()]], supplies :: [String.t()]) :: [String.t()]
  def find_all_recipes(recipes, ingredients, supplies) do
    supply_set = MapSet.new(supplies)
    n = length(recipes)

    {graph, indegree} =
      Enum.reduce(0..(n - 1), {%{}, %{}}, fn i, {g, indeg} ->
        ing_list = Enum.at(ingredients, i)

        indeg_i =
          Enum.count(ing_list, fn ing -> not MapSet.member?(supply_set, ing) end)

        indeg = Map.put(indeg, i, indeg_i)

        g =
          Enum.reduce(ing_list, g, fn ing, acc ->
            if MapSet.member?(supply_set, ing) do
              acc
            else
              Map.update(acc, ing, [i], fn lst -> [i | lst] end)
            end
          end)

        {g, indeg}
      end)

    queue =
      Enum.reduce(0..(n - 1), :queue.new(), fn i, q ->
        if Map.get(indegree, i) == 0 do
          :queue.in(i, q)
        else
          q
        end
      end)

    result_rev = bfs(queue, graph, indegree, [], recipes)
    Enum.reverse(result_rev)
  end

  defp bfs(queue, graph, indegree, acc, recipes) do
    case :queue.out(queue) do
      {:empty, _} ->
        acc

      {{:value, idx}, q_rest} ->
        recipe_name = Enum.at(recipes, idx)
        acc2 = [recipe_name | acc]

        dependents = Map.get(graph, recipe_name, [])

        {indeg_updated, q_new} =
          Enum.reduce(dependents, {indegree, q_rest}, fn dep_idx, {map_acc, q_acc} ->
            new_val = Map.get(map_acc, dep_idx) - 1
            map_acc2 = Map.put(map_acc, dep_idx, new_val)

            if new_val == 0 do
              {map_acc2, :queue.in(dep_idx, q_acc)}
            else
              {map_acc2, q_acc}
            end
          end)

        bfs(q_new, graph, indeg_updated, acc2, recipes)
    end
  end
end
```
