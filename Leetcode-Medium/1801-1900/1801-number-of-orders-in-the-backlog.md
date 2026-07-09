# 1801. Number of Orders in the Backlog

## Cpp

```cpp
class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        const long long MOD = 1'000'000'007LL;
        // max-heap for buy orders (price descending)
        priority_queue<pair<int,long long>> buy;
        // min-heap for sell orders (price ascending)
        priority_queue<pair<int,long long>, vector<pair<int,long long>>, greater<pair<int,long long>>> sell;
        
        for (const auto& o : orders) {
            int price = o[0];
            long long amount = o[1];
            int type = o[2]; // 0 = buy, 1 = sell
            
            if (type == 0) { // buy
                while (amount > 0 && !sell.empty() && sell.top().first <= price) {
                    auto top = sell.top();
                    long long match = min(amount, top.second);
                    amount -= match;
                    top.second -= match;
                    sell.pop();
                    if (top.second > 0) sell.push(top);
                }
                if (amount > 0) buy.emplace(price, amount);
            } else { // sell
                while (amount > 0 && !buy.empty() && buy.top().first >= price) {
                    auto top = buy.top();
                    long long match = min(amount, top.second);
                    amount -= match;
                    top.second -= match;
                    buy.pop();
                    if (top.second > 0) buy.push(top);
                }
                if (amount > 0) sell.emplace(price, amount);
            }
        }
        
        long long total = 0;
        while (!buy.empty()) {
            total += buy.top().second;
            total %= MOD;
            buy.pop();
        }
        while (!sell.empty()) {
            total += sell.top().second;
            total %= MOD;
            sell.pop();
        }
        return (int)(total % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    static class Order {
        int price;
        long amount;
        Order(int p, long a) { price = p; amount = a; }
    }
    public int getNumberOfBacklogOrders(int[][] orders) {
        PriorityQueue<Order> buy = new PriorityQueue<>((a, b) -> b.price - a.price);
        PriorityQueue<Order> sell = new PriorityQueue<>(Comparator.comparingInt(a -> a.price));
        for (int[] o : orders) {
            int price = o[0];
            long amount = o[1];
            int type = o[2];
            if (type == 0) { // buy
                while (amount > 0 && !sell.isEmpty() && sell.peek().price <= price) {
                    Order s = sell.poll();
                    long matched = Math.min(amount, s.amount);
                    amount -= matched;
                    s.amount -= matched;
                    if (s.amount > 0) sell.offer(s);
                }
                if (amount > 0) buy.offer(new Order(price, amount));
            } else { // sell
                while (amount > 0 && !buy.isEmpty() && buy.peek().price >= price) {
                    Order b = buy.poll();
                    long matched = Math.min(amount, b.amount);
                    amount -= matched;
                    b.amount -= matched;
                    if (b.amount > 0) buy.offer(b);
                }
                if (amount > 0) sell.offer(new Order(price, amount));
            }
        }
        long total = 0;
        for (Order o : buy) total = (total + o.amount) % MOD;
        for (Order o : sell) total = (total + o.amount) % MOD;
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        import heapq
        MOD = 10**9 + 7

        buy_heap = []   # max-heap (store negative price)
        sell_heap = []  # min-heap (price, amount)

        for price, amount, order_type in orders:
            if order_type == 0:  # buy order
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sp, sa = heapq.heappop(sell_heap)
                    if sa > amount:
                        sa -= amount
                        amount = 0
                        heapq.heappush(sell_heap, (sp, sa))
                    else:
                        amount -= sa
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))
            else:  # sell order
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    bp, ba = heapq.heappop(buy_heap)
                    bp = -bp
                    if ba > amount:
                        ba -= amount
                        amount = 0
                        heapq.heappush(buy_heap, (-bp, ba))
                    else:
                        amount -= ba
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))

        total = 0
        for _, amt in buy_heap:
            total = (total + amt) % MOD
        for _, amt in sell_heap:
            total = (total + amt) % MOD

        return total
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        buy = []   # max-heap (store negative price)
        sell = []  # min-heap
        
        for price, amount, orderType in orders:
            if orderType == 0:  # buy
                while amount > 0 and sell and sell[0][0] <= price:
                    sp, sa = heapq.heappop(sell)
                    if sa > amount:
                        sa -= amount
                        amount = 0
                        heapq.heappush(sell, (sp, sa))
                    else:
                        amount -= sa
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:  # sell
                while amount > 0 and buy and -buy[0][0] >= price:
                    bp, ba = heapq.heappop(buy)
                    bp = -bp
                    if ba > amount:
                        ba -= amount
                        amount = 0
                        heapq.heappush(buy, (-bp, ba))
                    else:
                        amount -= ba
                if amount > 0:
                    heapq.heappush(sell, (price, amount))
        
        total = 0
        for _, a in buy:
            total = (total + a) % MOD
        for _, a in sell:
            total = (total + a) % MOD
        return total
```

## C

```c
#include <stdlib.h>

typedef long long ll;

typedef struct {
    int price;
    ll amount;
} Node;

static void swapNode(Node* a, Node* b) {
    Node t = *a;
    *a = *b;
    *b = t;
}

/* Max-heap for buy orders */
static void pushBuy(Node* heap, int* size, int price, ll amount) {
    int i = (*size)++;
    heap[i].price = price;
    heap[i].amount = amount;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].price >= heap[i].price) break;
        swapNode(&heap[p], &heap[i]);
        i = p;
    }
}
static void popBuy(Node* heap, int* size) {
    (*size)--;
    if (*size == 0) return;
    heap[0] = heap[*size];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        int r = l + 1;
        int largest = i;
        if (l < *size && heap[l].price > heap[largest].price) largest = l;
        if (r < *size && heap[r].price > heap[largest].price) largest = r;
        if (largest == i) break;
        swapNode(&heap[i], &heap[largest]);
        i = largest;
    }
}

/* Min-heap for sell orders */
static void pushSell(Node* heap, int* size, int price, ll amount) {
    int i = (*size)++;
    heap[i].price = price;
    heap[i].amount = amount;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].price <= heap[i].price) break;
        swapNode(&heap[p], &heap[i]);
        i = p;
    }
}
static void popSell(Node* heap, int* size) {
    (*size)--;
    if (*size == 0) return;
    heap[0] = heap[*size];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        int r = l + 1;
        int smallest = i;
        if (l < *size && heap[l].price < heap[smallest].price) smallest = l;
        if (r < *size && heap[r].price < heap[smallest].price) smallest = r;
        if (smallest == i) break;
        swapNode(&heap[i], &heap[smallest]);
        i = smallest;
    }
}

int getNumberOfBacklogOrders(int** orders, int ordersSize, int* ordersColSize){
    const ll MOD = 1000000007LL;
    Node* buyHeap = (Node*)malloc(sizeof(Node) * (ordersSize + 5));
    Node* sellHeap = (Node*)malloc(sizeof(Node) * (ordersSize + 5));
    int buySize = 0, sellSize = 0;

    for (int i = 0; i < ordersSize; ++i) {
        int price = orders[i][0];
        ll amount = (ll)orders[i][1];
        int type = orders[i][2]; // 0 = buy, 1 = sell

        if (type == 0) { // buy
            while (amount > 0 && sellSize > 0 && sellHeap[0].price <= price) {
                ll match = amount < sellHeap[0].amount ? amount : sellHeap[0].amount;
                amount -= match;
                sellHeap[0].amount -= match;
                if (sellHeap[0].amount == 0) popSell(sellHeap, &sellSize);
            }
            if (amount > 0) pushBuy(buyHeap, &buySize, price, amount);
        } else { // sell
            while (amount > 0 && buySize > 0 && buyHeap[0].price >= price) {
                ll match = amount < buyHeap[0].amount ? amount : buyHeap[0].amount;
                amount -= match;
                buyHeap[0].amount -= match;
                if (buyHeap[0].amount == 0) popBuy(buyHeap, &buySize);
            }
            if (amount > 0) pushSell(sellHeap, &sellSize, price, amount);
        }
    }

    ll result = 0;
    for (int i = 0; i < buySize; ++i) {
        result += buyHeap[i].amount;
        if (result >= MOD) result %= MOD;
    }
    for (int i = 0; i < sellSize; ++i) {
        result += sellHeap[i].amount;
        if (result >= MOD) result %= MOD;
    }

    free(buyHeap);
    free(sellHeap);
    return (int)(result % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int GetNumberOfBacklogOrders(int[][] orders) {
        const int MOD = 1000000007;
        var buy = new SortedDictionary<int, long>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        var sell = new SortedDictionary<int, long>();
        
        foreach (var order in orders) {
            int price = order[0];
            long amount = order[1];
            int type = order[2]; // 0 = buy, 1 = sell
            
            if (type == 0) { // buy
                while (amount > 0 && sell.Count > 0 && sell.First().Key <= price) {
                    int sp = sell.First().Key;
                    long sAmt = sell[sp];
                    long matched = Math.Min(amount, sAmt);
                    amount -= matched;
                    sAmt -= matched;
                    if (sAmt == 0) sell.Remove(sp);
                    else sell[sp] = sAmt;
                }
                if (amount > 0) {
                    if (buy.ContainsKey(price)) buy[price] += amount;
                    else buy[price] = amount;
                }
            } else { // sell
                while (amount > 0 && buy.Count > 0 && buy.First().Key >= price) {
                    int bp = buy.First().Key;
                    long bAmt = buy[bp];
                    long matched = Math.Min(amount, bAmt);
                    amount -= matched;
                    bAmt -= matched;
                    if (bAmt == 0) buy.Remove(bp);
                    else buy[bp] = bAmt;
                }
                if (amount > 0) {
                    if (sell.ContainsKey(price)) sell[price] += amount;
                    else sell[price] = amount;
                }
            }
        }
        
        long total = 0;
        foreach (var v in buy.Values) total = (total + v) % MOD;
        foreach (var v in sell.Values) total = (total + v) % MOD;
        
        return (int)(total % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} orders
 * @return {number}
 */
var getNumberOfBacklogOrders = function(orders) {
    const MOD = 1_000_000_007;

    class Heap {
        constructor(compare) {
            this.data = [];
            this.compare = compare; // returns true if a should be above b
        }
        size() { return this.data.length; }
        peek() { return this.data[0]; }
        push(item) {
            const arr = this.data;
            arr.push(item);
            let idx = arr.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.compare(arr[parent], arr[idx])) break;
                [arr[parent], arr[idx]] = [arr[idx], arr[parent]];
                idx = parent;
            }
        }
        pop() {
            const arr = this.data;
            if (arr.length === 0) return undefined;
            const top = arr[0];
            const last = arr.pop();
            if (arr.length > 0) {
                arr[0] = last;
                let idx = 0;
                const n = arr.length;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = left + 1;
                    let best = idx;

                    if (left < n && !this.compare(arr[best], arr[left])) best = left;
                    if (right < n && !this.compare(arr[best], arr[right])) best = right;

                    if (best === idx) break;
                    [arr[idx], arr[best]] = [arr[best], arr[idx]];
                    idx = best;
                }
            }
            return top;
        }
    }

    // max-heap for buys: higher price first
    const buyHeap = new Heap((a, b) => a.price > b.price);
    // min-heap for sells: lower price first
    const sellHeap = new Heap((a, b) => a.price < b.price);

    for (const [price, amountOrig, type] of orders) {
        let amount = amountOrig;
        if (type === 0) { // buy
            while (amount > 0 && sellHeap.size() > 0 && sellHeap.peek().price <= price) {
                const top = sellHeap.peek();
                if (top.amount > amount) {
                    top.amount -= amount;
                    amount = 0;
                } else {
                    amount -= top.amount;
                    sellHeap.pop();
                }
            }
            if (amount > 0) buyHeap.push({price, amount});
        } else { // sell
            while (amount > 0 && buyHeap.size() > 0 && buyHeap.peek().price >= price) {
                const top = buyHeap.peek();
                if (top.amount > amount) {
                    top.amount -= amount;
                    amount = 0;
                } else {
                    amount -= top.amount;
                    buyHeap.pop();
                }
            }
            if (amount > 0) sellHeap.push({price, amount});
        }
    }

    let result = 0;
    for (const heap of [buyHeap, sellHeap]) {
        for (const node of heap.data) {
            result = (result + node.amount) % MOD;
        }
    }
    return result;
};
```

## Typescript

```typescript
class Heap<T> {
    private data: T[] = [];
    private compare: (a: T, b: T) => boolean;

    constructor(compare: (a: T, b: T) => boolean) {
        this.compare = compare;
    }

    size(): number {
        return this.data.length;
    }

    peek(): T | undefined {
        return this.data[0];
    }

    push(item: T): void {
        this.data.push(item);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): T | undefined {
        if (this.data.length === 0) return undefined;
        const top = this.data[0];
        const end = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = end;
            this.bubbleDown(0);
        }
        return top;
    }

    getItems(): T[] {
        return this.data;
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parent = Math.floor((idx - 1) / 2);
            if (this.compare(this.data[idx], this.data[parent])) {
                [this.data[idx], this.data[parent]] = [this.data[parent], this.data[idx]];
                idx = parent;
            } else break;
        }
    }

    private bubbleDown(idx: number): void {
        const n = this.data.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = left + 1;
            let best = idx;

            if (left < n && this.compare(this.data[left], this.data[best])) best = left;
            if (right < n && this.compare(this.data[right], this.data[best])) best = right;

            if (best !== idx) {
                [this.data[idx], this.data[best]] = [this.data[best], this.data[idx]];
                idx = best;
            } else break;
        }
    }
}

function getNumberOfBacklogOrders(orders: number[][]): number {
    const MOD = 1_000_000_007;
    const buyHeap = new Heap<[number, number]>((a, b) => a[0] > b[0]); // max-heap by price
    const sellHeap = new Heap<[number, number]>((a, b) => a[0] < b[0]); // min-heap by price

    for (const [price, amtInit, type] of orders) {
        let amount = amtInit;
        if (type === 0) { // buy
            while (
                amount > 0 &&
                sellHeap.size() > 0 &&
                (sellHeap.peek()![0] <= price)
            ) {
                const top = sellHeap.peek()!;
                if (top[1] > amount) {
                    top[1] -= amount;
                    amount = 0;
                } else {
                    amount -= top[1];
                    sellHeap.pop();
                }
            }
            if (amount > 0) buyHeap.push([price, amount]);
        } else { // sell
            while (
                amount > 0 &&
                buyHeap.size() > 0 &&
                (buyHeap.peek()![0] >= price)
            ) {
                const top = buyHeap.peek()!;
                if (top[1] > amount) {
                    top[1] -= amount;
                    amount = 0;
                } else {
                    amount -= top[1];
                    buyHeap.pop();
                }
            }
            if (amount > 0) sellHeap.push([price, amount]);
        }
    }

    let total = 0;
    for (const [, a] of buyHeap.getItems()) {
        total = (total + a) % MOD;
    }
    for (const [, a] of sellHeap.getItems()) {
        total = (total + a) % MOD;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $orders
     * @return Integer
     */
    function getNumberOfBacklogOrders($orders) {
        $mod = 1000000007;

        $buyHeap = new SplPriorityQueue();   // max-heap for buy orders (price high -> priority high)
        $sellHeap = new SplPriorityQueue();  // min-heap for sell orders simulated with negative price

        $buyHeap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $sellHeap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);

        foreach ($orders as $order) {
            [$price, $amount, $type] = $order;

            if ($type == 0) { // buy order
                while ($amount > 0 && !$sellHeap->isEmpty()) {
                    $top = $sellHeap->extract();               // ['data'=>amt,'priority'=>-price]
                    $sellPrice = -$top['priority'];
                    $sellAmt   = $top['data'];

                    if ($sellPrice > $price) {                  // cannot match, put it back
                        $sellHeap->insert($sellAmt, -$sellPrice);
                        break;
                    }

                    $matched = min($amount, $sellAmt);
                    $amount  -= $matched;
                    $sellAmt -= $matched;

                    if ($sellAmt > 0) {
                        $sellHeap->insert($sellAmt, -$sellPrice);
                    }
                }

                if ($amount > 0) {
                    $buyHeap->insert($amount, $price);
                }
            } else { // sell order
                while ($amount > 0 && !$buyHeap->isEmpty()) {
                    $top = $buyHeap->extract();                 // ['data'=>amt,'priority'=>price]
                    $buyPrice = $top['priority'];
                    $buyAmt   = $top['data'];

                    if ($buyPrice < $price) {                   // cannot match, put it back
                        $buyHeap->insert($buyAmt, $buyPrice);
                        break;
                    }

                    $matched = min($amount, $buyAmt);
                    $amount  -= $matched;
                    $buyAmt  -= $matched;

                    if ($buyAmt > 0) {
                        $buyHeap->insert($buyAmt, $buyPrice);
                    }
                }

                if ($amount > 0) {
                    $sellHeap->insert($amount, -$price);
                }
            }
        }

        $result = 0;
        while (!$buyHeap->isEmpty()) {
            $node = $buyHeap->extract();
            $result = ($result + $node['data']) % $mod;
        }
        while (!$sellHeap->isEmpty()) {
            $node = $sellHeap->extract();
            $result = ($result + $node['data']) % $mod;
        }

        return $result;
    }
}
```

## Swift

```swift
import Foundation

struct Heap<T> {
    var elements: [T] = []
    let priorityFunction: (T, T) -> Bool

    init(priorityFunction: @escaping (T, T) -> Bool) {
        self.priorityFunction = priorityFunction
    }

    var isEmpty: Bool { elements.isEmpty }
    func peek() -> T? { elements.first }

    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(elements.count - 1)
    }

    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let value = elements[0]
            elements[0] = elements.removeLast()
            siftDown(0)
            return value
        }
    }

    mutating private func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && priorityFunction(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }

    mutating private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    func getNumberOfBacklogOrders(_ orders: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        struct Node { var price: Int; var amount: Int }

        var buyHeap = Heap<Node>(priorityFunction: { $0.price > $1.price })   // max-heap for buys
        var sellHeap = Heap<Node>(priorityFunction: { $0.price < $1.price })  // min-heap for sells

        for order in orders {
            let price = order[0]
            var amount = order[1]
            let type = order[2]

            if type == 0 { // buy
                while amount > 0,
                      !sellHeap.isEmpty,
                      let top = sellHeap.peek(),
                      top.price <= price {
                    var node = sellHeap.pop()!
                    if node.amount > amount {
                        node.amount -= amount
                        amount = 0
                        sellHeap.push(node)
                    } else {
                        amount -= node.amount
                    }
                }
                if amount > 0 {
                    buyHeap.push(Node(price: price, amount: amount))
                }
            } else { // sell
                while amount > 0,
                      !buyHeap.isEmpty,
                      let top = buyHeap.peek(),
                      top.price >= price {
                    var node = buyHeap.pop()!
                    if node.amount > amount {
                        node.amount -= amount
                        amount = 0
                        buyHeap.push(node)
                    } else {
                        amount -= node.amount
                    }
                }
                if amount > 0 {
                    sellHeap.push(Node(price: price, amount: amount))
                }
            }
        }

        var total: Int64 = 0
        for n in buyHeap.elements { total += Int64(n.amount) }
        for n in sellHeap.elements { total += Int64(n.amount) }

        return Int(total % Int64(MOD))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getNumberOfBacklogOrders(orders: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        data class Order(val price: Int, var amount: Long)

        val buyHeap = java.util.PriorityQueue<Order>(compareByDescending { it.price })
        val sellHeap = java.util.PriorityQueue<Order>(compareBy { it.price })

        for (ord in orders) {
            val price = ord[0]
            var amount = ord[1].toLong()
            val type = ord[2]

            if (type == 0) { // buy
                while (amount > 0 && sellHeap.isNotEmpty() && sellHeap.peek().price <= price) {
                    val top = sellHeap.peek()
                    val match = kotlin.math.min(amount, top.amount)
                    amount -= match
                    top.amount -= match
                    if (top.amount == 0L) sellHeap.poll()
                }
                if (amount > 0) {
                    buyHeap.offer(Order(price, amount))
                }
            } else { // sell
                while (amount > 0 && buyHeap.isNotEmpty() && buyHeap.peek().price >= price) {
                    val top = buyHeap.peek()
                    val match = kotlin.math.min(amount, top.amount)
                    amount -= match
                    top.amount -= match
                    if (top.amount == 0L) buyHeap.poll()
                }
                if (amount > 0) {
                    sellHeap.offer(Order(price, amount))
                }
            }
        }

        var total = 0L
        for (o in buyHeap) {
            total += o.amount
            if (total >= MOD) total %= MOD
        }
        for (o in sellHeap) {
            total += o.amount
            if (total >= MOD) total %= MOD
        }
        return (total % MOD).toInt()
    }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Order struct {
	price  int
	amount int
}

// Max-heap for buy orders (higher price first)
type BuyHeap []*Order

func (h BuyHeap) Len() int           { return len(h) }
func (h BuyHeap) Less(i, j int) bool { return h[i].price > h[j].price }
func (h BuyHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *BuyHeap) Push(x interface{}) {
	*h = append(*h, x.(*Order))
}

func (h *BuyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// Min-heap for sell orders (lower price first)
type SellHeap []*Order

func (h SellHeap) Len() int           { return len(h) }
func (h SellHeap) Less(i, j int) bool { return h[i].price < h[j].price }
func (h SellHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *SellHeap) Push(x interface{}) {
	*h = append(*h, x.(*Order))
}

func (h *SellHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func getNumberOfBacklogOrders(orders [][]int) int {
	const mod = 1000000007

	buy := &BuyHeap{}
	sell := &SellHeap{}
	heap.Init(buy)
	heap.Init(sell)

	for _, o := range orders {
		price, amount, typ := o[0], o[1], o[2]

		if typ == 0 { // buy order
			for amount > 0 && sell.Len() > 0 && (*sell)[0].price <= price {
				top := (*sell)[0]
				if top.amount > amount {
					top.amount -= amount
					amount = 0
				} else {
					amount -= top.amount
					heap.Pop(sell)
				}
			}
			if amount > 0 {
				heap.Push(buy, &Order{price: price, amount: amount})
			}
		} else { // sell order
			for amount > 0 && buy.Len() > 0 && (*buy)[0].price >= price {
				top := (*buy)[0]
				if top.amount > amount {
					top.amount -= amount
					amount = 0
				} else {
					amount -= top.amount
					heap.Pop(buy)
				}
			}
			if amount > 0 {
				heap.Push(sell, &Order{price: price, amount: amount})
			}
		}
	}

	ans := 0
	for _, o := range *buy {
		ans = (ans + o.amount) % mod
	}
	for _, o := range *sell {
		ans = (ans + o.amount) % mod
	}
	return ans
}
```

## Ruby

```ruby
def get_number_of_backlog_orders(orders)
  MOD = 1_000_000_007

  class Heap
    def initialize(&comp)
      @data = []
      @comp = comp
    end

    def push(item)
      @data << item
      sift_up(@data.size - 1)
    end

    def pop
      return nil if empty?
      top = @data[0]
      last = @data.pop
      unless empty?
        @data[0] = last
        sift_down(0)
      end
      top
    end

    def peek
      @data[0]
    end

    def empty?
      @data.empty?
    end

    private

    def sift_up(idx)
      while idx > 0
        parent = (idx - 1) / 2
        if @comp.call(@data[idx], @data[parent])
          @data[idx], @data[parent] = @data[parent], @data[idx]
          idx = parent
        else
          break
        end
      end
    end

    def sift_down(idx)
      size = @data.size
      loop do
        left = idx * 2 + 1
        right = left + 1
        best = idx
        if left < size && @comp.call(@data[left], @data[best])
          best = left
        end
        if right < size && @comp.call(@data[right], @data[best])
          best = right
        end
        break if best == idx
        @data[idx], @data[best] = @data[best], @data[idx]
        idx = best
      end
    end
  end

  sell_heap = Heap.new { |a, b| a[0] < b[0] }   # min price first
  buy_heap  = Heap.new { |a, b| a[0] > b[0] }   # max price first

  orders.each do |price, amount, type|
    if type == 0 # buy
      while amount > 0 && !sell_heap.empty? && sell_heap.peek[0] <= price
        s_price, s_amount = sell_heap.pop
        if s_amount > amount
          s_amount -= amount
          amount = 0
          sell_heap.push([s_price, s_amount])
        else
          amount -= s_amount
        end
      end
      buy_heap.push([price, amount]) if amount > 0
    else # sell
      while amount > 0 && !buy_heap.empty? && buy_heap.peek[0] >= price
        b_price, b_amount = buy_heap.pop
        if b_amount > amount
          b_amount -= amount
          amount = 0
          buy_heap.push([b_price, b_amount])
        else
          amount -= b_amount
        end
      end
      sell_heap.push([price, amount]) if amount > 0
    end
  end

  total = 0
  until buy_heap.empty?
    total = (total + buy_heap.pop[1]) % MOD
  end
  until sell_heap.empty?
    total = (total + sell_heap.pop[1]) % MOD
  end
  total
end
```

## Scala

```scala
object Solution {
    def getNumberOfBacklogOrders(orders: Array[Array[Int]]): Int = {
        import scala.collection.mutable.PriorityQueue

        val MOD = 1000000007L

        // buy orders: max-heap by price (largest price first)
        implicit val buyOrd: Ordering[(Int, Long)] = Ordering.by[(Int, Long), Int](_._1)
        // sell orders: min-heap by price (smallest price first) -> reverse ordering
        implicit val sellOrd: Ordering[(Int, Long)] = Ordering.by[(Int, Long), Int](_._1).reverse

        val buyPQ = PriorityQueue.empty[(Int, Long)]
        val sellPQ = PriorityQueue.empty[(Int, Long)]

        for (order <- orders) {
            val price = order(0)
            var amount = order(1).toLong
            val orderType = order(2)

            if (orderType == 0) { // buy
                while (amount > 0 && sellPQ.nonEmpty && sellPQ.head._1 <= price) {
                    val (sp, sa) = sellPQ.dequeue()
                    if (sa > amount) {
                        sellPQ.enqueue((sp, sa - amount))
                        amount = 0L
                    } else {
                        amount -= sa
                    }
                }
                if (amount > 0) buyPQ.enqueue((price, amount))
            } else { // sell
                while (amount > 0 && buyPQ.nonEmpty && buyPQ.head._1 >= price) {
                    val (bp, ba) = buyPQ.dequeue()
                    if (ba > amount) {
                        buyPQ.enqueue((bp, ba - amount))
                        amount = 0L
                    } else {
                        amount -= ba
                    }
                }
                if (amount > 0) sellPQ.enqueue((price, amount))
            }
        }

        var total: Long = 0L
        for ((_, a) <- buyPQ) {
            total += a
            if (total >= MOD) total %= MOD
        }
        for ((_, a) <- sellPQ) {
            total += a
            if (total >= MOD) total %= MOD
        }

        (total % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_number_of_backlog_orders(orders: Vec<Vec<i32>>) -> i32 {
        use std::collections::BinaryHeap;
        use std::cmp::Reverse;

        const MOD: i64 = 1_000_000_007;

        let mut buy: BinaryHeap<(i32, i64)> = BinaryHeap::new(); // max‑heap by price
        let mut sell: BinaryHeap<Reverse<(i32, i64)>> = BinaryHeap::new(); // min‑heap

        for order in orders {
            let price = order[0];
            let mut amount = order[1] as i64;
            let typ = order[2];

            if typ == 0 {
                // buy order
                while amount > 0 {
                    if let Some(Reverse((sell_price, sell_amount))) = sell.pop() {
                        if sell_price <= price {
                            let matched = std::cmp::min(amount, sell_amount);
                            amount -= matched;
                            let remaining_sell = sell_amount - matched;
                            if remaining_sell > 0 {
                                sell.push(Reverse((sell_price, remaining_sell)));
                            }
                        } else {
                            // cannot match, put it back
                            sell.push(Reverse((sell_price, sell_amount)));
                            break;
                        }
                    } else {
                        break;
                    }
                }
                if amount > 0 {
                    buy.push((price, amount));
                }
            } else {
                // sell order
                while amount > 0 {
                    if let Some((buy_price, buy_amount)) = buy.pop() {
                        if buy_price >= price {
                            let matched = std::cmp::min(amount, buy_amount);
                            amount -= matched;
                            let remaining_buy = buy_amount - matched;
                            if remaining_buy > 0 {
                                buy.push((buy_price, remaining_buy));
                            }
                        } else {
                            // cannot match, put it back
                            buy.push((buy_price, buy_amount));
                            break;
                        }
                    } else {
                        break;
                    }
                }
                if amount > 0 {
                    sell.push(Reverse((price, amount)));
                }
            }
        }

        let mut total: i64 = 0;
        for &(_, amt) in buy.iter() {
            total += amt;
        }
        for &Reverse((_, amt)) in sell.iter() {
            total += amt;
        }

        (total % MOD) as i32
    }
}
```

## Racket

```racket
(require data/heap
         racket/match)

(define MOD 1000000007)

(define/contract (get-number-of-backlog-orders orders)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((buy-heap (make-heap >))
         (sell-heap (make-heap <)))
    (for ([ord orders])
      (match ord
        [(list price amount type)
         (if (= type 0) ; buy order
             (let loop ((amt amount))
               (cond
                 [(zero? amt) (void)]
                 [(or (heap-empty? sell-heap)
                      (< price (first (heap-peek sell-heap))))
                  (heap-insert! buy-heap (list price amt))]
                 [else
                  (define sell-top (heap-peek sell-heap))
                  (define sell-price (first sell-top))
                  (define sell-amt (second sell-top))
                  (define trade (min amt sell-amt))
                  (heap-pop! sell-heap)
                  (when (> (- sell-amt trade) 0)
                    (heap-insert! sell-heap (list sell-price (- sell-amt trade))))
                  (loop (- amt trade))]))
             ; sell order
             (let loop ((amt amount))
               (cond
                 [(zero? amt) (void)]
                 [(or (heap-empty? buy-heap)
                      (> price (first (heap-peek buy-heap))))
                  (heap-insert! sell-heap (list price amt))]
                 [else
                  (define buy-top (heap-peek buy-heap))
                  (define buy-price (first buy-top))
                  (define buy-amt (second buy-top))
                  (define trade (min amt buy-amt))
                  (heap-pop! buy-heap)
                  (when (> (- buy-amt trade) 0)
                    (heap-insert! buy-heap (list buy-price (- buy-amt trade))))
                  (loop (- amt trade))])))]))
    (define (sum-heap h)
      (let loop ((total 0))
        (if (heap-empty? h)
            total
            (let ((top (heap-pop! h)))
              (loop (+ total (second top)))))))
    (modulo (+ (sum-heap buy-heap) (sum-heap sell-heap)) MOD)))
```
