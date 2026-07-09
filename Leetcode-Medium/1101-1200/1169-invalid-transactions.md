# 1169. Invalid Transactions

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Tx {
        string name;
        int time;
        int amount;
        string city;
        string raw;
    };
    
    vector<string> invalidTransactions(vector<string>& transactions) {
        int n = transactions.size();
        vector<Tx> txs;
        txs.reserve(n);
        for (const string& s : transactions) {
            size_t p1 = s.find(',');
            size_t p2 = s.find(',', p1 + 1);
            size_t p3 = s.find(',', p2 + 1);
            Tx t;
            t.name = s.substr(0, p1);
            t.time = stoi(s.substr(p1 + 1, p2 - p1 - 1));
            t.amount = stoi(s.substr(p2 + 1, p3 - p2 - 1));
            t.city = s.substr(p3 + 1);
            t.raw = s;
            txs.push_back(move(t));
        }
        
        vector<bool> invalid(n, false);
        for (int i = 0; i < n; ++i) {
            if (txs[i].amount > 1000) invalid[i] = true;
            for (int j = i + 1; j < n; ++j) {
                if (txs[i].name == txs[j].name &&
                    abs(txs[i].time - txs[j].time) <= 60 &&
                    txs[i].city != txs[j].city) {
                    invalid[i] = invalid[j] = true;
                }
            }
        }
        
        vector<string> ans;
        for (int i = 0; i < n; ++i) {
            if (invalid[i]) ans.push_back(txs[i].raw);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> invalidTransactions(String[] transactions) {
        int n = transactions.length;
        Transaction[] trans = new Transaction[n];
        for (int i = 0; i < n; i++) {
            String s = transactions[i];
            String[] parts = s.split(",");
            trans[i] = new Transaction(parts[0], Integer.parseInt(parts[1]),
                    Integer.parseInt(parts[2]), parts[3], s);
        }
        boolean[] invalid = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (trans[i].amount > 1000) {
                invalid[i] = true;
            }
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (!trans[i].name.equals(trans[j].name)) continue;
                if (Math.abs(trans[i].time - trans[j].time) <= 60 &&
                    !trans[i].city.equals(trans[j].city)) {
                    invalid[i] = true;
                    break;
                }
            }
        }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (invalid[i]) res.add(trans[i].raw);
        }
        return res;
    }

    private static class Transaction {
        String name, city, raw;
        int time, amount;
        Transaction(String name, int time, int amount, String city, String raw) {
            this.name = name;
            this.time = time;
            this.amount = amount;
            this.city = city;
            this.raw = raw;
        }
    }
}
```

## Python

```python
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed = []
        for t in transactions:
            name, time_str, amount_str, city = t.split(',')
            parsed.append((name, int(time_str), int(amount_str), city))
        n = len(transactions)
        invalid = [False] * n
        for i in range(n):
            name_i, time_i, amt_i, city_i = parsed[i]
            if amt_i > 1000:
                invalid[i] = True
            for j in range(i + 1, n):
                name_j, time_j, amt_j, city_j = parsed[j]
                if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                    invalid[i] = True
                    invalid[j] = True
        return [transactions[i] for i in range(n) if invalid[i]]
```

## Python3

```python
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parsed = []
        for i, tr in enumerate(transactions):
            name, time, amount, city = tr.split(',')
            parsed.append((name, int(time), int(amount), city, i))
        
        invalid = [False] * n
        for i in range(n):
            name_i, time_i, amt_i, city_i, idx_i = parsed[i]
            if amt_i > 1000:
                invalid[idx_i] = True
            for j in range(i + 1, n):
                name_j, time_j, amt_j, city_j, idx_j = parsed[j]
                if name_i != name_j:
                    continue
                if abs(time_i - time_j) <= 60 and city_i != city_j:
                    invalid[idx_i] = True
                    invalid[idx_j] = True
        return [transactions[i] for i in range(n) if invalid[i]]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static char *strDup(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

typedef struct {
    char *name;
    int time;
    int amount;
    char *city;
    const char *original;
} Transaction;

char** invalidTransactions(char** transactions, int transactionsSize, int* returnSize) {
    if (transactionsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    Transaction *arr = (Transaction *)malloc(sizeof(Transaction) * transactionsSize);
    for (int i = 0; i < transactionsSize; ++i) {
        char buf[128];
        strcpy(buf, transactions[i]);

        char *token = strtok(buf, ",");
        arr[i].name = strDup(token);

        token = strtok(NULL, ",");
        arr[i].time = atoi(token);

        token = strtok(NULL, ",");
        arr[i].amount = atoi(token);

        token = strtok(NULL, ",");
        arr[i].city = strDup(token);

        arr[i].original = transactions[i];
    }

    char **result = (char **)malloc(sizeof(char *) * transactionsSize);
    int cnt = 0;

    for (int i = 0; i < transactionsSize; ++i) {
        int invalid = 0;
        if (arr[i].amount > 1000) {
            invalid = 1;
        } else {
            for (int j = 0; j < transactionsSize && !invalid; ++j) {
                if (i == j) continue;
                if (strcmp(arr[i].name, arr[j].name) == 0 &&
                    abs(arr[i].time - arr[j].time) <= 60 &&
                    strcmp(arr[i].city, arr[j].city) != 0) {
                    invalid = 1;
                }
            }
        }
        if (invalid) {
            result[cnt++] = strDup(arr[i].original);
        }
    }

    // clean up
    for (int i = 0; i < transactionsSize; ++i) {
        free(arr[i].name);
        free(arr[i].city);
    }
    free(arr);

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> InvalidTransactions(string[] transactions) {
        int n = transactions.Length;
        var parsed = new Transaction[n];
        for (int i = 0; i < n; i++) {
            var parts = transactions[i].Split(',');
            parsed[i] = new Transaction {
                Name = parts[0],
                Time = int.Parse(parts[1]),
                Amount = int.Parse(parts[2]),
                City = parts[3],
                Raw = transactions[i]
            };
        }

        bool[] invalid = new bool[n];
        for (int i = 0; i < n; i++) {
            if (parsed[i].Amount > 1000) invalid[i] = true;
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (parsed[i].Name == parsed[j].Name &&
                    Math.Abs(parsed[i].Time - parsed[j].Time) <= 60 &&
                    parsed[i].City != parsed[j].City) {
                    invalid[i] = true;
                    invalid[j] = true;
                }
            }
        }

        var result = new List<string>();
        for (int i = 0; i < n; i++) {
            if (invalid[i]) result.Add(parsed[i].Raw);
        }
        return result;
    }

    private class Transaction {
        public string Name;
        public int Time;
        public int Amount;
        public string City;
        public string Raw;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} transactions
 * @return {string[]}
 */
var invalidTransactions = function(transactions) {
    const n = transactions.length;
    const parsed = transactions.map(s => {
        const [name, time, amount, city] = s.split(',');
        return { name, time: +time, amount: +amount, city, raw: s };
    });
    
    const invalidIdx = new Set();
    
    for (let i = 0; i < n; i++) {
        if (parsed[i].amount > 1000) invalidIdx.add(i);
        for (let j = i + 1; j < n; j++) {
            if (parsed[i].name === parsed[j].name &&
                Math.abs(parsed[i].time - parsed[j].time) <= 60 &&
                parsed[i].city !== parsed[j].city) {
                invalidIdx.add(i);
                invalidIdx.add(j);
            }
        }
    }
    
    const result = [];
    for (const idx of invalidIdx) {
        result.push(transactions[idx]);
    }
    return result;
};
```

## Typescript

```typescript
function invalidTransactions(transactions: string[]): string[] {
    interface Tx {
        name: string;
        time: number;
        amount: number;
        city: string;
        raw: string;
    }
    const txs: Tx[] = transactions.map(s => {
        const [name, time, amount, city] = s.split(',');
        return { name, time: +time, amount: +amount, city, raw: s };
    });
    const n = txs.length;
    const invalid = new Array<boolean>(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (txs[i].amount > 1000) invalid[i] = true;
        for (let j = i + 1; j < n; j++) {
            if (
                txs[i].name === txs[j].name &&
                Math.abs(txs[i].time - txs[j].time) <= 60 &&
                txs[i].city !== txs[j].city
            ) {
                invalid[i] = true;
                invalid[j] = true;
            }
        }
    }
    const result: string[] = [];
    for (let i = 0; i < n; i++) {
        if (invalid[i]) result.push(txs[i].raw);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $transactions
     * @return String[]
     */
    function invalidTransactions($transactions) {
        $n = count($transactions);
        $info = [];
        foreach ($transactions as $idx => $t) {
            [$name, $time, $amount, $city] = explode(',', $t);
            $info[$idx] = [
                'name'   => $name,
                'time'   => (int)$time,
                'amount' => (int)$amount,
                'city'   => $city
            ];
        }

        $invalid = array_fill(0, $n, false);

        for ($i = 0; $i < $n; $i++) {
            if ($info[$i]['amount'] > 1000) {
                $invalid[$i] = true;
            }
            for ($j = $i + 1; $j < $n; $j++) {
                if ($info[$i]['name'] === $info[$j]['name']) {
                    if (abs($info[$i]['time'] - $info[$j]['time']) <= 60 && $info[$i]['city'] !== $info[$j]['city']) {
                        $invalid[$i] = true;
                        $invalid[$j] = true;
                    }
                }
            }
        }

        $result = [];
        foreach ($transactions as $idx => $t) {
            if ($invalid[$idx]) {
                $result[] = $t;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func invalidTransactions(_ transactions: [String]) -> [String] {
        struct Tx {
            let name: String
            let time: Int
            let amount: Int
            let city: String
            let original: String
        }
        
        var parsed = [Tx]()
        for t in transactions {
            let parts = t.split(separator: ",")
            if parts.count == 4,
               let time = Int(parts[1]),
               let amount = Int(parts[2]) {
                let tx = Tx(name: String(parts[0]),
                            time: time,
                            amount: amount,
                            city: String(parts[3]),
                            original: t)
                parsed.append(tx)
            }
        }
        
        let n = parsed.count
        var invalid = [Bool](repeating: false, count: n)
        
        for i in 0..<n {
            if parsed[i].amount > 1000 {
                invalid[i] = true
            }
            for j in (i + 1)..<n {
                if parsed[i].name == parsed[j].name &&
                    abs(parsed[i].time - parsed[j].time) <= 60 &&
                    parsed[i].city != parsed[j].city {
                    invalid[i] = true
                    invalid[j] = true
                }
            }
        }
        
        var result = [String]()
        for i in 0..<n where invalid[i] {
            result.append(parsed[i].original)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    data class Tx(val name: String, val time: Int, val amount: Int, val city: String, val raw: String)

    fun invalidTransactions(transactions: Array<String>): List<String> {
        val txList = mutableListOf<Tx>()
        for (s in transactions) {
            val parts = s.split(',')
            txList.add(Tx(parts[0], parts[1].toInt(), parts[2].toInt(), parts[3], s))
        }
        val n = txList.size
        val invalid = BooleanArray(n)
        for (i in 0 until n) {
            if (txList[i].amount > 1000) invalid[i] = true
        }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (txList[i].name == txList[j].name &&
                    txList[i].city != txList[j].city &&
                    kotlin.math.abs(txList[i].time - txList[j].time) <= 60
                ) {
                    invalid[i] = true
                    invalid[j] = true
                }
            }
        }
        val result = mutableListOf<String>()
        for (i in 0 until n) {
            if (invalid[i]) result.add(txList[i].raw)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> invalidTransactions(List<String> transactions) {
    int n = transactions.length;
    var parsed = <_Transaction>[];
    for (var s in transactions) {
      var parts = s.split(',');
      parsed.add(_Transaction(
        name: parts[0],
        time: int.parse(parts[1]),
        amount: int.parse(parts[2]),
        city: parts[3],
        raw: s,
      ));
    }

    List<bool> invalid = List.filled(n, false);

    for (int i = 0; i < n; i++) {
      if (parsed[i].amount > 1000) {
        invalid[i] = true;
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (parsed[i].name == parsed[j].name &&
            (parsed[i].time - parsed[j].time).abs() <= 60 &&
            parsed[i].city != parsed[j].city) {
          invalid[i] = true;
          invalid[j] = true;
        }
      }
    }

    List<String> result = [];
    for (int i = 0; i < n; i++) {
      if (invalid[i]) {
        result.add(parsed[i].raw);
      }
    }
    return result;
  }
}

class _Transaction {
  final String name;
  final int time;
  final int amount;
  final String city;
  final String raw;

  _Transaction({
    required this.name,
    required this.time,
    required this.amount,
    required this.city,
    required this.raw,
  });
}
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

type txn struct {
	name   string
	time   int
	amount int
	city   string
	raw    string
}

func invalidTransactions(transactions []string) []string {
	n := len(transactions)
	if n == 0 {
		return nil
	}
	txns := make([]txn, n)
	for i, s := range transactions {
		parts := strings.Split(s, ",")
		t, _ := strconv.Atoi(parts[1])
		a, _ := strconv.Atoi(parts[2])
		txns[i] = txn{
			name:   parts[0],
			time:   t,
			amount: a,
			city:   parts[3],
			raw:    s,
		}
	}

	invalid := make([]bool, n)

	for i := 0; i < n; i++ {
		if txns[i].amount > 1000 {
			invalid[i] = true
		}
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if txns[i].name != txns[j].name {
				continue
			}
			diff := txns[i].time - txns[j].time
			if diff < 0 {
				diff = -diff
			}
			if diff <= 60 && txns[i].city != txns[j].city {
				invalid[i] = true
				invalid[j] = true
			}
		}
	}

	var res []string
	for i, bad := range invalid {
		if bad {
			res = append(res, txns[i].raw)
		}
	}
	return res
}
```

## Ruby

```ruby
def invalid_transactions(transactions)
  n = transactions.size
  parsed = []
  transactions.each do |t|
    name, time_str, amount_str, city = t.split(',')
    parsed << [name, time_str.to_i, amount_str.to_i, city]
  end

  invalid = Array.new(n, false)

  (0...n).each do |i|
    name_i, time_i, amt_i, city_i = parsed[i]

    invalid[i] = true if amt_i > 1000

    (0...n).each do |j|
      next if i == j
      name_j, time_j, _, city_j = parsed[j]
      if name_i == name_j && city_i != city_j && (time_i - time_j).abs <= 60
        invalid[i] = true
        break
      end
    end
  end

  result = []
  (0...n).each do |i|
    result << transactions[i] if invalid[i]
  end
  result
end
```

## Scala

```scala
object Solution {
    def invalidTransactions(transactions: Array[String]): List[String] = {
        case class Tx(name: String, time: Int, amount: Int, city: String, raw: String)
        val txs = transactions.map { s =>
            val p = s.split(",")
            Tx(p(0), p(1).toInt, p(2).toInt, p(3), s)
        }
        val invalid = scala.collection.mutable.Set[String]()
        for (i <- txs.indices) {
            val a = txs(i)
            if (a.amount > 1000) invalid += a.raw
            var j = 0
            while (j < txs.length) {
                if (i != j) {
                    val b = txs(j)
                    if (a.name == b.name && a.city != b.city && math.abs(a.time - b.time) <= 60) {
                        invalid += a.raw
                    }
                }
                j += 1
            }
        }
        invalid.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn invalid_transactions(transactions: Vec<String>) -> Vec<String> {
        #[derive(Clone)]
        struct Tx {
            name: String,
            time: i32,
            amount: i32,
            city: String,
            raw: String,
        }

        let mut txs: Vec<Tx> = Vec::with_capacity(transactions.len());
        for s in transactions.iter() {
            let parts: Vec<&str> = s.split(',').collect();
            let name = parts[0].to_string();
            let time: i32 = parts[1].parse().unwrap();
            let amount: i32 = parts[2].parse().unwrap();
            let city = parts[3].to_string();
            txs.push(Tx {
                name,
                time,
                amount,
                city,
                raw: s.clone(),
            });
        }

        let n = txs.len();
        let mut invalid = vec![false; n];

        // Rule 1: amount > 1000
        for (i, t) in txs.iter().enumerate() {
            if t.amount > 1000 {
                invalid[i] = true;
            }
        }

        // Rule 2: same name, different city, within 60 minutes
        for i in 0..n {
            for j in (i + 1)..n {
                if txs[i].name == txs[j].name
                    && txs[i].city != txs[j].city
                    && (txs[i].time - txs[j].time).abs() <= 60
                {
                    invalid[i] = true;
                    invalid[j] = true;
                }
            }
        }

        let mut result: Vec<String> = Vec::new();
        for (i, flag) in invalid.iter().enumerate() {
            if *flag {
                result.push(txs[i].raw.clone());
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)
(require racket/list)

(define/contract (invalid-transactions transactions)
  (-> (listof string?) (listof string?))
  (let* ([parsed
          (map-indexed
           (lambda (idx tr)
             (let* ([parts (string-split tr ",")]
                    [name (list-ref parts 0)]
                    [time (string->number (list-ref parts 1))]
                    [amount (string->number (list-ref parts 2))]
                    [city (list-ref parts 3)])
               (vector idx tr name time amount city)))
           transactions)]
         [n (length parsed)]
         [invalid-flags (make-vector n #f)])
    ;; Mark transactions with amount > 1000
    (for ([i (in-range n)])
      (let* ([vec (list-ref parsed i)]
             [amount (vector-ref vec 4)])
        (when (> amount 1000)
          (vector-set! invalid-flags i #t))))
    ;; Check pairwise condition: same name, different city, time diff <= 60
    (for ([i (in-range n)])
      (for ([j (in-range (+ i 1) n)])
        (let* ([vi (list-ref parsed i)]
               [vj (list-ref parsed j)]
               [name-i (vector-ref vi 2)]
               [name-j (vector-ref vj 2)])
          (when (string=? name-i name-j)
            (let* ([city-i (vector-ref vi 5)]
                   [city-j (vector-ref vj 5)]
                   [time-i (vector-ref vi 3)]
                   [time-j (vector-ref vj 3)])
              (when (and (not (string=? city-i city-j))
                         (<= (abs (- time-i time-j)) 60))
                (vector-set! invalid-flags i #t)
                (vector-set! invalid-flags j #t)))))))
    ;; Collect invalid transaction strings
    (for/list ([i (in-range n)]
               #:when (vector-ref invalid-flags i))
      (let* ([vec (list-ref parsed i)])
        (vector-ref vec 1)))))
```

## Erlang

```erlang
-spec invalid_transactions(Transactions :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
invalid_transactions(Transactions) ->
    Parsed = [parse_transaction(T) || T <- Transactions],
    Invalid = [Raw ||
        #{raw := Raw} = T <- Parsed,
        is_invalid(T, Parsed)],
    lists:usort(Invalid).

parse_transaction(Bin) ->
    [Name, TimeBin, AmountBin, City] =
        binary:split(Bin, <<",">>, [global]),
    #{name => Name,
      time => binary_to_integer(TimeBin),
      amount => binary_to_integer(AmountBin),
      city => City,
      raw => Bin}.

is_invalid(T, List) ->
    Amount = maps:get(amount, T),
    if
        Amount > 1000 -> true;
        true ->
            Name = maps:get(name, T),
            Time = maps:get(time, T),
            City = maps:get(city, T),
            lists:any(
                fun(Other) ->
                    case Other of
                        T -> false;
                        _ ->
                            maps:get(name, Other) =:= Name andalso
                            abs(Time - maps:get(time, Other)) =< 60 andalso
                            maps:get(city, Other) =/= City
                    end
                end,
                List)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec invalid_transactions(transactions :: [String.t]) :: [String.t]
  def invalid_transactions(transactions) do
    parsed =
      Enum.map(transactions, fn s ->
        [name, time_str, amount_str, city] = String.split(s, ",")
        %{
          name: name,
          time: String.to_integer(time_str),
          amount: String.to_integer(amount_str),
          city: city,
          raw: s
        }
      end)

    invalid =
      Enum.reduce(Enum.with_index(parsed), [], fn {t1, i}, acc ->
        cond do
          t1.amount > 1000 ->
            [t1.raw | acc]

          Enum.any?(Enum.with_index(parsed), fn {t2, j} ->
            i != j and
              t1.name == t2.name and
              t1.city != t2.city and
              abs(t1.time - t2.time) <= 60
          end) ->
            [t1.raw | acc]

          true ->
            acc
        end
      end)

    Enum.reverse(invalid)
  end
end
```
