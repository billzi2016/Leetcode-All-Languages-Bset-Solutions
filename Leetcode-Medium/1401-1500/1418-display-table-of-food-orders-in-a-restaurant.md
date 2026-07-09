# 1418. Display Table of Food Orders in a Restaurant

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        set<string> foodSet;
        map<int, unordered_map<string,int>> tableMap;
        
        for (const auto& order : orders) {
            int table = stoi(order[1]);
            const string& food = order[2];
            foodSet.insert(food);
            ++tableMap[table][food];
        }
        
        vector<string> foods(foodSet.begin(), foodSet.end());
        vector<vector<string>> result;
        // Header
        vector<string> header = {"Table"};
        header.insert(header.end(), foods.begin(), foods.end());
        result.push_back(move(header));
        
        // Rows per table
        for (const auto& [tableNum, cntMap] : tableMap) {
            vector<string> row;
            row.push_back(to_string(tableNum));
            for (const string& food : foods) {
                auto it = cntMap.find(food);
                row.push_back(to_string(it != cntMap.end() ? it->second : 0));
            }
            result.push_back(move(row));
        }
        
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        Set<String> foods = new TreeSet<>();
        Map<Integer, Map<String, Integer>> tableMap = new TreeMap<>();

        for (List<String> order : orders) {
            int table = Integer.parseInt(order.get(1));
            String food = order.get(2);
            foods.add(food);
            tableMap.computeIfAbsent(table, k -> new HashMap<>())
                    .merge(food, 1, Integer::sum);
        }

        List<List<String>> result = new ArrayList<>();
        List<String> header = new ArrayList<>();
        header.add("Table");
        header.addAll(foods);
        result.add(header);

        for (Map.Entry<Integer, Map<String, Integer>> entry : tableMap.entrySet()) {
            List<String> row = new ArrayList<>();
            row.add(String.valueOf(entry.getKey()));
            Map<String, Integer> counts = entry.getValue();
            for (String food : foods) {
                row.add(String.valueOf(counts.getOrDefault(food, 0)));
            }
            result.add(row);
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        food_set = set()
        table_counts = defaultdict(lambda: defaultdict(int))

        for name, table_str, food in orders:
            table = int(table_str)
            food_set.add(food)
            table_counts[table][food] += 1

        foods = sorted(food_set)
        tables = sorted(table_counts.keys())

        header = ["Table"] + foods
        result = [header]

        for t in tables:
            row = [str(t)]
            cnts = table_counts[t]
            for f in foods:
                row.append(str(cnts.get(f, 0)))
            result.append(row)

        return result
```

## Python3

```python
class Solution:
    def displayTable(self, orders):
        from collections import defaultdict, Counter

        food_set = set()
        table_counts = defaultdict(Counter)

        for name, table_str, food in orders:
            table = int(table_str)
            food_set.add(food)
            table_counts[table][food] += 1

        foods = sorted(food_set)
        tables = sorted(table_counts.keys())

        header = ["Table"] + foods
        result = [header]

        for t in tables:
            row = [str(t)]
            cnt = table_counts[t]
            for f in foods:
                row.append(str(cnt.get(f, 0)))
            result.append(row)

        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static int cmpStr(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sa, sb);
}

static int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/* comparator for bsearch where key is a string */
static int cmpStrKey(const void *key, const void *elem) {
    const char *k = (const char *)key;
    const char *e = *(const char **)elem;
    return strcmp(k, e);
}

static char *strDup(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    memcpy(p, s, len + 1);
    return p;
}

/* binary search for food index */
static int findFoodIndex(char **arr, int size, const char *key) {
    char **res = (char **)bsearch(key, arr, size, sizeof(char *), cmpStrKey);
    if (!res) return -1;
    return (int)(res - arr);
}

char *** displayTable(char *** orders, int ordersSize, int* ordersColSize,
                      int* returnSize, int** returnColumnSizes){
    /* collect all food items */
    char **foodAll = (char **)malloc(ordersSize * sizeof(char *));
    int foodAllCnt = 0;
    for (int i = 0; i < ordersSize; ++i) {
        foodAll[foodAllCnt++] = orders[i][2];
    }
    qsort(foodAll, foodAllCnt, sizeof(char *), cmpStr);
    /* deduplicate foods */
    char **foods = (char **)malloc(ordersSize * sizeof(char *));
    int foodCount = 0;
    for (int i = 0; i < foodAllCnt; ++i) {
        if (i == 0 || strcmp(foodAll[i], foodAll[i-1]) != 0) {
            foods[foodCount++] = foodAll[i];
        }
    }
    free(foodAll);

    /* collect all table numbers */
    int *tableAll = (int *)malloc(ordersSize * sizeof(int));
    int tableAllCnt = 0;
    for (int i = 0; i < ordersSize; ++i) {
        tableAll[tableAllCnt++] = atoi(orders[i][1]);
    }
    qsort(tableAll, tableAllCnt, sizeof(int), cmpInt);
    /* deduplicate tables */
    int *tables = (int *)malloc(ordersSize * sizeof(int));
    int tableCount = 0;
    for (int i = 0; i < tableAllCnt; ++i) {
        if (i == 0 || tableAll[i] != tableAll[i-1]) {
            tables[tableCount++] = tableAll[i];
        }
    }
    free(tableAll);

    /* map table number to row index */
    int tableIdxMap[501];
    for (int i = 0; i <= 500; ++i) tableIdxMap[i] = -1;
    for (int i = 0; i < tableCount; ++i) {
        if (tables[i] >= 0 && tables[i] <= 500)
            tableIdxMap[tables[i]] = i;
    }

    /* allocate count matrix */
    int **cnt = (int **)malloc(tableCount * sizeof(int *));
    for (int i = 0; i < tableCount; ++i) {
        cnt[i] = (int *)calloc(foodCount, sizeof(int));
    }

    /* fill counts */
    for (int i = 0; i < ordersSize; ++i) {
        int tnum = atoi(orders[i][1]);
        const char *food = orders[i][2];
        int ti = tableIdxMap[tnum];
        int fi = findFoodIndex(foods, foodCount, food);
        if (ti >= 0 && fi >= 0) {
            cnt[ti][fi] += 1;
        }
    }

    /* prepare result */
    int rows = tableCount + 1;          // header + each table
    int cols = foodCount + 1;           // Table column + foods

    char ***res = (char ***)malloc(rows * sizeof(char **));
    int *colSizes = (int *)malloc(rows * sizeof(int));
    for (int i = 0; i < rows; ++i) colSizes[i] = cols;

    /* header row */
    res[0] = (char **)malloc(cols * sizeof(char *));
    res[0][0] = strDup("Table");
    for (int j = 0; j < foodCount; ++j) {
        res[0][j+1] = strDup(foods[j]);
    }

    /* data rows */
    char buf[32];
    for (int i = 0; i < tableCount; ++i) {
        res[i+1] = (char **)malloc(cols * sizeof(char *));
        snprintf(buf, sizeof(buf), "%d", tables[i]);
        res[i+1][0] = strDup(buf);
        for (int j = 0; j < foodCount; ++j) {
            snprintf(buf, sizeof(buf), "%d", cnt[i][j]);
            res[i+1][j+1] = strDup(buf);
        }
    }

    /* clean up temporary allocations */
    free(cnt[0]); // actually each row allocated separately
    for (int i = 0; i < tableCount; ++i) {
        free(cnt[i]);
    }
    free(cnt);
    free(foods);
    free(tables);

    *returnSize = rows;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> DisplayTable(IList<IList<string>> orders) {
        var foodSet = new SortedSet<string>();
        var tableSet = new SortedSet<int>();
        var countMap = new Dictionary<int, Dictionary<string, int>>();

        foreach (var order in orders) {
            int table = int.Parse(order[1]);
            string food = order[2];

            foodSet.Add(food);
            tableSet.Add(table);

            if (!countMap.TryGetValue(table, out var inner)) {
                inner = new Dictionary<string, int>();
                countMap[table] = inner;
            }
            if (!inner.ContainsKey(food)) inner[food] = 0;
            inner[food]++;
        }

        var result = new List<IList<string>>();

        var header = new List<string> { "Table" };
        foreach (var food in foodSet) {
            header.Add(food);
        }
        result.Add(header);

        foreach (int table in tableSet) {
            var row = new List<string> { table.ToString() };
            var inner = countMap[table];
            foreach (var food in foodSet) {
                if (inner.TryGetValue(food, out int cnt)) {
                    row.Add(cnt.ToString());
                } else {
                    row.Add("0");
                }
            }
            result.Add(row);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} orders
 * @return {string[][]}
 */
var displayTable = function(orders) {
    const foodSet = new Set();
    const tableMap = new Map(); // table number -> Map of food to count

    for (const [, tableStr, food] of orders) {
        const tableNum = Number(tableStr);
        foodSet.add(food);
        if (!tableMap.has(tableNum)) {
            tableMap.set(tableNum, new Map());
        }
        const foodCount = tableMap.get(tableNum);
        foodCount.set(food, (foodCount.get(food) || 0) + 1);
    }

    const foods = Array.from(foodSet).sort();
    const tables = Array.from(tableMap.keys()).sort((a, b) => a - b);

    const result = [];
    result.push(["Table", ...foods]);

    for (const t of tables) {
        const row = [String(t)];
        const counts = tableMap.get(t);
        for (const f of foods) {
            row.push(String(counts.get(f) || 0));
        }
        result.push(row);
    }

    return result;
};
```

## Typescript

```typescript
function displayTable(orders: string[][]): string[][] {
    const foodSet = new Set<string>();
    const tableMap = new Map<number, Map<string, number>>();

    for (const [_, tableStr, food] of orders) {
        const tableNum = parseInt(tableStr, 10);
        foodSet.add(food);

        if (!tableMap.has(tableNum)) {
            tableMap.set(tableNum, new Map<string, number>());
        }
        const foodCountMap = tableMap.get(tableNum)!;
        foodCountMap.set(food, (foodCountMap.get(food) ?? 0) + 1);
    }

    const foods = Array.from(foodSet).sort((a, b) => a.localeCompare(b));
    const tables = Array.from(tableMap.keys()).sort((a, b) => a - b);

    const result: string[][] = [];
    // Header
    result.push(['Table', ...foods]);

    for (const tableNum of tables) {
        const row: string[] = [tableNum.toString()];
        const foodCountMap = tableMap.get(tableNum)!;
        for (const food of foods) {
            row.push((foodCountMap.get(food) ?? 0).toString());
        }
        result.push(row);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $orders
     * @return String[][]
     */
    function displayTable($orders) {
        $foodSet = [];
        $tableMap = [];

        foreach ($orders as $order) {
            [$customer, $tableStr, $food] = $order;
            $table = intval($tableStr);
            $foodSet[$food] = true;

            if (!isset($tableMap[$table])) {
                $tableMap[$table] = [];
            }
            if (!isset($tableMap[$table][$food])) {
                $tableMap[$table][$food] = 0;
            }
            $tableMap[$table][$food]++;
        }

        // Sort food items alphabetically
        $foods = array_keys($foodSet);
        sort($foods, SORT_STRING);

        // Sort table numbers numerically
        $tables = array_keys($tableMap);
        sort($tables, SORT_NUMERIC);

        $result = [];
        $header = array_merge(["Table"], $foods);
        $result[] = $header;

        foreach ($tables as $t) {
            $row = [(string)$t];
            foreach ($foods as $f) {
                $count = $tableMap[$t][$f] ?? 0;
                $row[] = (string)$count;
            }
            $result[] = $row;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func displayTable(_ orders: [[String]]) -> [[String]] {
        var foodSet = Set<String>()
        var tableMap = [Int: [String: Int]]()
        
        for order in orders {
            let tableNumber = Int(order[1])!
            let foodItem = order[2]
            
            foodSet.insert(foodItem)
            if tableMap[tableNumber] == nil {
                tableMap[tableNumber] = [:]
            }
            tableMap[tableNumber]![foodItem, default: 0] += 1
        }
        
        let sortedFoods = foodSet.sorted()
        let sortedTables = tableMap.keys.sorted()
        
        var result = [[String]]()
        var header = ["Table"]
        header.append(contentsOf: sortedFoods)
        result.append(header)
        
        for table in sortedTables {
            var row = [String]()
            row.append(String(table))
            let foodCounts = tableMap[table]!
            for food in sortedFoods {
                let count = foodCounts[food] ?? 0
                row.append(String(count))
            }
            result.append(row)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun displayTable(orders: List<List<String>>): List<List<String>> {
        val foodSet = mutableSetOf<String>()
        val tableMap = mutableMapOf<Int, MutableMap<String, Int>>()

        for (order in orders) {
            val tableNum = order[1].toInt()
            val foodItem = order[2]
            foodSet.add(foodItem)
            val innerMap = tableMap.getOrPut(tableNum) { mutableMapOf() }
            innerMap[foodItem] = (innerMap[foodItem] ?: 0) + 1
        }

        val sortedFoods = foodSet.toList().sorted()
        val result = mutableListOf<List<String>>()

        // Header row
        val header = mutableListOf<String>()
        header.add("Table")
        header.addAll(sortedFoods)
        result.add(header)

        // Data rows sorted by table number
        for (table in tableMap.keys.sorted()) {
            val row = mutableListOf<String>()
            row.add(table.toString())
            val counts = tableMap[table]!!
            for (food in sortedFoods) {
                row.add((counts[food] ?: 0).toString())
            }
            result.add(row)
        }

        return result
    }
}
```

## Golang

```go
func displayTable(orders [][]string) [][]string {
    // maps to store counts and unique items/tables
    tableFoodCount := make(map[int]map[string]int)
    foodSet := make(map[string]struct{})
    tableSet := make(map[int]struct{})

    for _, order := range orders {
        // order = [customerName, tableNumber, foodItem]
        tableNumStr := order[1]
        foodItem := order[2]

        // convert table number to int
        tn, _ := strconv.Atoi(tableNumStr)

        if _, ok := tableFoodCount[tn]; !ok {
            tableFoodCount[tn] = make(map[string]int)
        }
        tableFoodCount[tn][foodItem]++
        foodSet[foodItem] = struct{}{}
        tableSet[tn] = struct{}{}
    }

    // collect and sort foods alphabetically
    foods := make([]string, 0, len(foodSet))
    for f := range foodSet {
        foods = append(foods, f)
    }
    sort.Strings(foods)

    // collect and sort tables numerically
    tables := make([]int, 0, len(tableSet))
    for t := range tableSet {
        tables = append(tables, t)
    }
    sort.Ints(tables)

    // build result
    res := make([][]string, 0, len(tables)+1)

    // header row
    header := make([]string, 0, len(foods)+1)
    header = append(header, "Table")
    header = append(header, foods...)
    res = append(res, header)

    // data rows
    for _, t := range tables {
        row := make([]string, 0, len(foods)+1)
        row = append(row, strconv.Itoa(t))
        counts := tableFoodCount[t]
        for _, f := range foods {
            cnt := counts[f] // zero if not present
            row = append(row, strconv.Itoa(cnt))
        }
        res = append(res, row)
    }

    return res
}
```

## Ruby

```ruby
require 'set'

# @param {String[][]} orders
# @return {String[][]}
def display_table(orders)
  foods = Set.new
  table_counts = Hash.new { |h, k| h[k] = Hash.new(0) }

  orders.each do |name, table_str, food|
    table = table_str.to_i
    foods.add(food)
    table_counts[table][food] += 1
  end

  sorted_foods = foods.to_a.sort
  header = ["Table"] + sorted_foods

  rows = table_counts.keys.sort.map do |t|
    row = [t.to_s]
    sorted_foods.each { |f| row << table_counts[t][f].to_s }
    row
  end

  [header] + rows
end
```

## Scala

```scala
object Solution {
    def displayTable(orders: List[List[String]]): List[List[String]] = {
        import scala.collection.mutable

        val foodItems = mutable.TreeSet[String]()
        val tableMap = mutable.Map[Int, mutable.Map[String, Int]]()

        for (order <- orders) {
            val tableNum = order(1).toInt
            val food = order(2)
            foodItems += food
            val inner = tableMap.getOrElseUpdate(tableNum, mutable.Map[String, Int]())
            inner(food) = inner.getOrElse(food, 0) + 1
        }

        val header: List[String] = ("Table" :: foodItems.toList).toList

        val sortedTables = tableMap.keys.toArray.sorted

        val rows: List[List[String]] = sortedTables.map { t =>
            val counts = foodItems.map(f => tableMap(t).getOrElse(f, 0).toString).toList
            (t.toString :: counts)
        }.toList

        header :: rows
    }
}
```

## Rust

```rust
impl Solution {
    pub fn display_table(orders: Vec<Vec<String>>) -> Vec<Vec<String>> {
        use std::collections::{BTreeMap, BTreeSet, HashMap};

        let mut foods = BTreeSet::<String>::new();
        let mut table_map: BTreeMap<i32, HashMap<String, i32>> = BTreeMap::new();

        for order in orders.iter() {
            // order[0] is customer name (ignored)
            let table_num: i32 = order[1].parse().unwrap();
            let food = &order[2];
            foods.insert(food.clone());

            let entry = table_map.entry(table_num).or_insert_with(HashMap::new);
            *entry.entry(food.clone()).or_insert(0) += 1;
        }

        // Build header row
        let mut result: Vec<Vec<String>> = Vec::new();
        let mut header = vec!["Table".to_string()];
        for food in foods.iter() {
            header.push(food.clone());
        }
        result.push(header);

        // Build rows for each table in numeric order
        for (table_num, counts) in table_map.iter() {
            let mut row = vec![table_num.to_string()];
            for food in foods.iter() {
                let cnt = counts.get(food).unwrap_or(&0);
                row.push(cnt.to_string());
            }
            result.push(row);
        }

        result
    }
}
```
