# 2353. Design a Food Rating System

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class FoodRatings {
private:
    struct Comp {
        bool operator()(const pair<int,string>& a, const pair<int,string>& b) const {
            if (a.first != b.first) return a.first < b.first;          // higher rating first
            return a.second > b.second;                               // lexicographically smaller first
        }
    };
    
    unordered_map<string,int> curRating;
    unordered_map<string,string> foodCuisine;
    unordered_map<string, priority_queue<pair<int,string>, vector<pair<int,string>>, Comp>> cuisinePQ;
    
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n = foods.size();
        for (int i = 0; i < n; ++i) {
            const string& f = foods[i];
            const string& c = cuisines[i];
            int r = ratings[i];
            curRating[f] = r;
            foodCuisine[f] = c;
            cuisinePQ[c].push({r, f});
        }
    }
    
    void changeRating(string food, int newRating) {
        string c = foodCuisine[food];
        curRating[food] = newRating;
        cuisinePQ[c].push({newRating, food}); // lazy insertion
    }
    
    string highestRated(string cuisine) {
        auto& pq = cuisinePQ[cuisine];
        while (true) {
            auto top = pq.top();
            if (top.first == curRating[top.second]) {
                return top.second;
            }
            pq.pop(); // discard stale entry
        }
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
```

## Java

```java
import java.util.*;

class FoodRatings {
    private static class Food implements Comparable<Food> {
        String name;
        int rating;
        Food(String name, int rating) {
            this.name = name;
            this.rating = rating;
        }
        @Override
        public int compareTo(Food o) {
            if (this.rating != o.rating) {
                return Integer.compare(o.rating, this.rating); // higher rating first
            }
            return this.name.compareTo(o.name); // lexicographically smaller first
        }
    }

    private final Map<String, String> foodToCuisine = new HashMap<>();
    private final Map<String, Integer> foodToRating = new HashMap<>();
    private final Map<String, PriorityQueue<Food>> cuisinePQ = new HashMap<>();

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            String food = foods[i];
            String cuisine = cuisines[i];
            int rating = ratings[i];

            foodToCuisine.put(food, cuisine);
            foodToRating.put(food, rating);

            cuisinePQ.computeIfAbsent(cuisine, k -> new PriorityQueue<>())
                     .add(new Food(food, rating));
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        foodToRating.put(food, newRating);
        PriorityQueue<Food> pq = cuisinePQ.get(cuisine);
        if (pq == null) {
            pq = new PriorityQueue<>();
            cuisinePQ.put(cuisine, pq);
        }
        pq.add(new Food(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Food> pq = cuisinePQ.get(cuisine);
        while (true) {
            Food top = pq.peek();
            int currentRating = foodToRating.get(top.name);
            if (top.rating == currentRating) {
                return top.name;
            }
            pq.poll(); // discard outdated entry
        }
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */
```

## Python

```python
import heapq

class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_heap:
                self.cuisine_heap[cuisine] = []
            heapq.heappush(self.cuisine_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_heap[cuisine]
        while True:
            neg_rating, name = heap[0]
            if -neg_rating == self.food_to_rating[name]:
                return name
            heapq.heappop(heap)
```

## Python3

```python
from typing import List
import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heaps = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_heaps:
                self.cuisine_heaps[c] = []
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        c = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_heaps[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while True:
            neg_r, f = heap[0]
            if -neg_r == self.food_to_rating[f]:
                return f
            heapq.heappop(heap)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "uthash.h"

typedef struct HeapNode {
    int rating;
    char *food;
} HeapNode;

typedef struct CuisineHeap {
    char *cuisine;               // key
    HeapNode *data;
    int size;
    int capacity;
    UT_hash_handle hh;
} CuisineHeap;

typedef struct FoodInfo {
    char *food;                  // key
    int rating;
    char *cuisine;
    UT_hash_handle hh;
} FoodInfo;

struct FoodRatings {
    FoodInfo *foodMap;           // food name -> info
    CuisineHeap *cuisineMap;     // cuisine name -> heap
};

/* ---------- Heap utilities ---------- */
static void heapSwap(CuisineHeap *h, int i, int j) {
    HeapNode tmp = h->data[i];
    h->data[i] = h->data[j];
    h->data[j] = tmp;
}

static int better(const HeapNode *a, const HeapNode *b) {
    if (a->rating != b->rating) return a->rating > b->rating;
    return strcmp(a->food, b->food) < 0;   // lexicographically smaller is better
}

static void heapPush(CuisineHeap *h, int rating, char *food) {
    if (h->size == h->capacity) {
        int newCap = h->capacity ? h->capacity * 2 : 4;
        h->data = realloc(h->data, newCap * sizeof(HeapNode));
        h->capacity = newCap;
    }
    int i = h->size++;
    h->data[i].rating = rating;
    h->data[i].food = food;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (better(&h->data[i], &h->data[p])) {
            heapSwap(h, i, p);
            i = p;
        } else break;
    }
}

static void heapPop(CuisineHeap *h) {
    if (h->size == 0) return;
    h->data[0] = h->data[h->size - 1];
    h->size--;
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < h->size && better(&h->data[l], &h->data[best])) best = l;
        if (r < h->size && better(&h->data[r], &h->data[best])) best = r;
        if (best != i) {
            heapSwap(h, i, best);
            i = best;
        } else break;
    }
}

/* ---------- API implementation ---------- */
FoodRatings* foodRatingsCreate(char** foods, int foodsSize,
                               char** cuisines, int cuisinesSize,
                               int* ratings, int ratingsSize) {
    FoodRatings *obj = malloc(sizeof(FoodRatings));
    obj->foodMap = NULL;
    obj->cuisineMap = NULL;

    for (int i = 0; i < foodsSize; ++i) {
        char *foodDup = strdup(foods[i]);
        char *cuiDup  = strdup(cuisines[i]);

        FoodInfo *fi = malloc(sizeof(FoodInfo));
        fi->food = foodDup;
        fi->rating = ratings[i];
        fi->cuisine = cuiDup;
        HASH_ADD_KEYPTR(hh, obj->foodMap, fi->food, strlen(fi->food), fi);

        CuisineHeap *ch = NULL;
        HASH_FIND_STR(obj->cuisineMap, cuisines[i], ch);
        if (!ch) {
            ch = malloc(sizeof(CuisineHeap));
            ch->cuisine = strdup(cuisines[i]);
            ch->size = 0;
            ch->capacity = 4;
            ch->data = malloc(ch->capacity * sizeof(HeapNode));
            HASH_ADD_KEYPTR(hh, obj->cuisineMap, ch->cuisine,
                            strlen(ch->cuisine), ch);
        }
        heapPush(ch, ratings[i], foodDup);
    }
    return obj;
}

void foodRatingsChangeRating(FoodRatings* obj, char* food, int newRating) {
    FoodInfo *fi = NULL;
    HASH_FIND_STR(obj->foodMap, food, fi);
    if (!fi) return;   // should not happen per constraints

    fi->rating = newRating;

    CuisineHeap *ch = NULL;
    HASH_FIND_STR(obj->cuisineMap, fi->cuisine, ch);
    if (ch) {
        heapPush(ch, newRating, fi->food);
    }
}

char* foodRatingsHighestRated(FoodRatings* obj, char* cuisine) {
    CuisineHeap *ch = NULL;
    HASH_FIND_STR(obj->cuisineMap, cuisine, ch);
    while (1) {
        HeapNode *top = &ch->data[0];
        FoodInfo *fi = NULL;
        HASH_FIND_STR(obj->foodMap, top->food, fi);
        if (fi && fi->rating == top->rating) {
            return top->food;
        }
        heapPop(ch);   // discard stale entry
    }
}

void foodRatingsFree(FoodRatings* obj) {
    FoodInfo *fi, *tmpFi;
    HASH_ITER(hh, obj->foodMap, fi, tmpFi) {
        HASH_DEL(obj->foodMap, fi);
        free(fi->food);
        free(fi->cuisine);
        free(fi);
    }

    CuisineHeap *ch, *tmpCh;
    HASH_ITER(hh, obj->cuisineMap, ch, tmpCh) {
        HASH_DEL(obj->cuisineMap, ch);
        free(ch->cuisine);
        free(ch->data);
        free(ch);
    }
    free(obj);
}

/**
 * Your FoodRatings struct will be instantiated and called as such:
 * FoodRatings* obj = foodRatingsCreate(foods, foodsSize, cuisines, cuisinesSize, ratings, ratingsSize);
 * foodRatingsChangeRating(obj, food, newRating);
 *
 * char* param_2 = foodRatingsHighestRated(obj, cuisine);
 *
 * foodRatingsFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class FoodRatings
{
    private class FoodEntry
    {
        public int Rating;
        public string Name;
        public FoodEntry(int rating, string name)
        {
            Rating = rating;
            Name = name;
        }
    }

    private class FoodComparer : IComparer<FoodEntry>
    {
        public int Compare(FoodEntry x, FoodEntry y)
        {
            if (x.Rating != y.Rating)
                return y.Rating.CompareTo(x.Rating); // higher rating first
            return string.Compare(x.Name, y.Name, StringComparison.Ordinal);
        }
    }

    private readonly Dictionary<string, string> foodToCuisine = new Dictionary<string, string>();
    private readonly Dictionary<string, int> foodToRating = new Dictionary<string, int>();
    private readonly Dictionary<string, SortedSet<FoodEntry>> cuisineMap = new Dictionary<string, SortedSet<FoodEntry>>();

    public FoodRatings(string[] foods, string[] cuisines, int[] ratings)
    {
        var comparer = new FoodComparer();
        for (int i = 0; i < foods.Length; i++)
        {
            string food = foods[i];
            string cuisine = cuisines[i];
            int rating = ratings[i];

            foodToCuisine[food] = cuisine;
            foodToRating[food] = rating;

            if (!cuisineMap.TryGetValue(cuisine, out var set))
            {
                set = new SortedSet<FoodEntry>(comparer);
                cuisineMap[cuisine] = set;
            }
            set.Add(new FoodEntry(rating, food));
        }
    }

    public void ChangeRating(string food, int newRating)
    {
        int oldRating = foodToRating[food];
        string cuisine = foodToCuisine[food];

        var set = cuisineMap[cuisine];
        set.Remove(new FoodEntry(oldRating, food));
        set.Add(new FoodEntry(newRating, food));

        foodToRating[food] = newRating;
    }

    public string HighestRated(string cuisine)
    {
        var set = cuisineMap[cuisine];
        // The first element according to the comparer is the highest rated
        return set.Min.Name;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * string param_2 = obj.HighestRated(cuisine);
 */
```

## Javascript

```javascript
/**
 * @param {string[]} foods
 * @param {string[]} cuisines
 * @param {number[]} ratings
 */
var FoodRatings = function(foods, cuisines, ratings) {
    // maps food -> cuisine and current rating
    this.foodToCuisine = new Map();
    this.foodToRating = new Map();

    // map cuisine -> max-heap (array)
    this.cuisineHeaps = new Map();

    const compare = (a, b) => {
        if (a.rating !== b.rating) return a.rating > b.rating;
        return a.food < b.food; // lexicographically smaller first
    };

    const heapPush = (heap, node) => {
        heap.push(node);
        let idx = heap.length - 1;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (compare(heap[idx], heap[parent])) {
                [heap[idx], heap[parent]] = [heap[parent], heap[idx]];
                idx = parent;
            } else break;
        }
    };

    // store helper functions for later use
    this._compare = compare;
    this._heapPush = heapPush;

    for (let i = 0; i < foods.length; ++i) {
        const food = foods[i];
        const cuisine = cuisines[i];
        const rating = ratings[i];

        this.foodToCuisine.set(food, cuisine);
        this.foodToRating.set(food, rating);

        if (!this.cuisineHeaps.has(cuisine)) this.cuisineHeaps.set(cuisine, []);
        this._heapPush(this.cuisineHeaps.get(cuisine), { food, rating });
    }
};

/** 
 * @param {string} food 
 * @param {number} newRating
 * @return {void}
 */
FoodRatings.prototype.changeRating = function(food, newRating) {
    const cuisine = this.foodToCuisine.get(food);
    this.foodToRating.set(food, newRating);
    const heap = this.cuisineHeaps.get(cuisine);
    this._heapPush(heap, { food, rating: newRating });
};

/** 
 * @param {string} cuisine
 * @return {string}
 */
FoodRatings.prototype.highestRated = function(cuisine) {
    const heap = this.cuisineHeaps.get(cuisine);

    const compare = this._compare;

    const heapPop = (heap) => {
        const n = heap.length;
        if (n === 1) return heap.pop();
        const top = heap[0];
        heap[0] = heap.pop();
        let idx = 0;
        while (true) {
            const left = idx * 2 + 1;
            const right = idx * 2 + 2;
            let best = idx;
            if (left < heap.length && compare(heap[left], heap[best])) best = left;
            if (right < heap.length && compare(heap[right], heap[best])) best = right;
            if (best !== idx) {
                [heap[idx], heap[best]] = [heap[best], heap[idx]];
                idx = best;
            } else break;
        }
        return top;
    };

    while (true) {
        const top = heap[0];
        // current rating may have changed; discard stale entries
        if (this.foodToRating.get(top.food) === top.rating) {
            return top.food;
        }
        heapPop(heap);
    }
};
```

## Typescript

```typescript
class FoodRatings {
    private foodToCuisine: Map<string, string>;
    private foodToRating: Map<string, number>;
    private cuisineHeap: Map<string, MaxHeap>;

    constructor(foods: string[], cuisines: string[], ratings: number[]) {
        this.foodToCuisine = new Map();
        this.foodToRating = new Map();
        this.cuisineHeap = new Map();

        for (let i = 0; i < foods.length; i++) {
            const food = foods[i];
            const cuisine = cuisines[i];
            const rating = ratings[i];

            this.foodToCuisine.set(food, cuisine);
            this.foodToRating.set(food, rating);

            if (!this.cuisineHeap.has(cuisine)) {
                this.cuisineHeap.set(cuisine, new MaxHeap());
            }
            this.cuisineHeap.get(cuisine)!.push({ food, rating });
        }
    }

    changeRating(food: string, newRating: number): void {
        this.foodToRating.set(food, newRating);
        const cuisine = this.foodToCuisine.get(food)!;
        if (!this.cuisineHeap.has(cuisine)) {
            this.cuisineHeap.set(cuisine, new MaxHeap());
        }
        this.cuisineHeap.get(cuisine)!.push({ food, rating: newRating });
    }

    highestRated(cuisine: string): string {
        const heap = this.cuisineHeap.get(cuisine)!;
        while (true) {
            const top = heap.peek();
            if (!top) return "";
            const currentRating = this.foodToRating.get(top.food);
            if (currentRating === top.rating) {
                return top.food;
            }
            heap.pop(); // discard outdated entry
        }
    }
}

interface Entry {
    food: string;
    rating: number;
}

class MaxHeap {
    private data: Entry[] = [];

    push(item: Entry): void {
        this.data.push(item);
        this.bubbleUp(this.data.length - 1);
    }

    pop(): Entry | undefined {
        if (this.data.length === 0) return undefined;
        const top = this.data[0];
        const last = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = last;
            this.bubbleDown(0);
        }
        return top;
    }

    peek(): Entry | undefined {
        return this.data[0];
    }

    private bubbleUp(idx: number): void {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
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
            let largest = idx;

            if (left < n && this.compare(this.data[left], this.data[largest])) {
                largest = left;
            }
            if (right < n && this.compare(this.data[right], this.data[largest])) {
                largest = right;
            }

            if (largest !== idx) {
                [this.data[idx], this.data[largest]] = [this.data[largest], this.data[idx]];
                idx = largest;
            } else break;
        }
    }

    private compare(a: Entry, b: Entry): boolean {
        if (a.rating !== b.rating) return a.rating > b.rating;
        return a.food < b.food; // lexicographically smaller is higher priority
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
```

## Php

```php
class FoodPQ extends SplPriorityQueue {
    public function compare($p1, $p2): int {
        // $p1 and $p2 are arrays: [rating, foodName]
        if ($p1[0] === $p2[0]) {
            if ($p1[1] === $p2[1]) return 0;
            // lexicographically smaller name should have higher priority
            return ($p1[1] < $p2[1]) ? 1 : -1;
        }
        return ($p1[0] > $p2[0]) ? 1 : -1;
    }
}

class FoodRatings {
    private array $foodToCuisine = [];
    private array $foodToRating = [];
    /** @var array<string,FoodPQ> */
    private array $cuisinePQ = [];

    /**
     * @param String[] $foods
     * @param String[] $cuisines
     * @param Integer[] $ratings
     */
    function __construct($foods, $cuisines, $ratings) {
        $n = count($foods);
        for ($i = 0; $i < $n; ++$i) {
            $food = $foods[$i];
            $cuisine = $cuisines[$i];
            $rating = $ratings[$i];

            $this->foodToCuisine[$food] = $cuisine;
            $this->foodToRating[$food] = $rating;

            if (!isset($this->cuisinePQ[$cuisine])) {
                $pq = new FoodPQ();
                $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
                $this->cuisinePQ[$cuisine] = $pq;
            }
            $this->cuisinePQ[$cuisine]->insert([$rating, $food], [$rating, $food]);
        }
    }

    /**
     * @param String $food
     * @param Integer $newRating
     * @return NULL
     */
    function changeRating($food, $newRating) {
        $cuisine = $this->foodToCuisine[$food];
        $this->foodToRating[$food] = $newRating;
        $this->cuisinePQ[$cuisine]->insert([$newRating, $food], [$newRating, $food]);
        return null;
    }

    /**
     * @param String $cuisine
     * @return String
     */
    function highestRated($cuisine) {
        $pq = $this->cuisinePQ[$cuisine];
        while (true) {
            $top = $pq->top(); // [$rating, $food]
            $rating = $top[0];
            $food = $top[1];
            if ($rating === $this->foodToRating[$food]) {
                return $food;
            }
            $pq->extract(); // discard outdated entry
        }
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * $obj = new FoodRatings($foods, $cuisines, $ratings);
 * $obj->changeRating($food, $newRating);
 * $ret_2 = $obj->highestRated($cuisine);
 */
```

## Swift

```swift
import Foundation

struct FoodItem {
    var rating: Int
    var name: String
}

class Heap {
    private var elements: [FoodItem] = []
    private let areSorted: (FoodItem, FoodItem) -> Bool   // true if first has higher priority
    
    init(sort: @escaping (FoodItem, FoodItem) -> Bool) {
        self.areSorted = sort
    }
    
    var isEmpty: Bool { elements.isEmpty }
    
    func peek() -> FoodItem? {
        return elements.first
    }
    
    func push(_ value: FoodItem) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    @discardableResult
    func pop() -> FoodItem? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let top = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return top
        }
    }
    
    private func parent(_ index: Int) -> Int { (index - 1) / 2 }
    private func leftChild(_ index: Int) -> Int { 2 * index + 1 }
    private func rightChild(_ index: Int) -> Int { 2 * index + 2 }
    
    private func siftUp(from index: Int) {
        var child = index
        var parentIdx = parent(child)
        while child > 0 && areSorted(elements[child], elements[parentIdx]) {
            elements.swapAt(child, parentIdx)
            child = parentIdx
            parentIdx = parent(child)
        }
    }
    
    private func siftDown(from index: Int) {
        var parentIdx = index
        while true {
            let leftIdx = leftChild(parentIdx)
            let rightIdx = rightChild(parentIdx)
            var candidate = parentIdx
            
            if leftIdx < elements.count && areSorted(elements[leftIdx], elements[candidate]) {
                candidate = leftIdx
            }
            if rightIdx < elements.count && areSorted(elements[rightIdx], elements[candidate]) {
                candidate = rightIdx
            }
            if candidate == parentIdx { return }
            elements.swapAt(parentIdx, candidate)
            parentIdx = candidate
        }
    }
}

class FoodRatings {
    private var foodToCuisine: [String: String] = [:]
    private var foodToRating: [String: Int] = [:]
    private var cuisineHeaps: [String: Heap] = [:]
    
    init(_ foods: [String], _ cuisines: [String], _ ratings: [Int]) {
        for i in 0..<foods.count {
            let food = foods[i]
            let cuisine = cuisines[i]
            let rating = ratings[i]
            
            foodToCuisine[food] = cuisine
            foodToRating[food] = rating
            
            if cuisineHeaps[cuisine] == nil {
                cuisineHeaps[cuisine] = Heap { a, b in
                    if a.rating != b.rating {
                        return a.rating > b.rating          // higher rating first
                    } else {
                        return a.name < b.name              // lexicographically smaller first
                    }
                }
            }
            let item = FoodItem(rating: rating, name: food)
            cuisineHeaps[cuisine]!.push(item)
        }
    }
    
    func changeRating(_ food: String, _ newRating: Int) {
        guard let cuisine = foodToCuisine[food] else { return }
        foodToRating[food] = newRating
        let item = FoodItem(rating: newRating, name: food)
        cuisineHeaps[cuisine]?.push(item)
    }
    
    func highestRated(_ cuisine: String) -> String {
        guard let heap = cuisineHeaps[cuisine] else { return "" }
        while true {
            guard let top = heap.peek() else { return "" }
            if let current = foodToRating[top.name], current == top.rating {
                return top.name
            } else {
                _ = heap.pop()
            }
        }
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food, newRating)
 * let ret_2: String = obj.highestRated(cuisine)
 */
```

## Kotlin

```kotlin
class FoodRatings(foods: Array<String>, cuisines: Array<String>, ratings: IntArray) {
    private data class Entry(val rating: Int, val name: String)

    private val foodRating = HashMap<String, Int>()
    private val foodCuisine = HashMap<String, String>()
    private val cuisinePQ = HashMap<String, java.util.PriorityQueue<Entry>>()

    init {
        for (i in foods.indices) {
            val f = foods[i]
            val c = cuisines[i]
            val r = ratings[i]
            foodRating[f] = r
            foodCuisine[f] = c
            val pq = cuisinePQ.getOrPut(c) {
                java.util.PriorityQueue<Entry>(Comparator { a, b ->
                    if (a.rating != b.rating) b.rating - a.rating else a.name.compareTo(b.name)
                })
            }
            pq.add(Entry(r, f))
        }
    }

    fun changeRating(food: String, newRating: Int) {
        foodRating[food] = newRating
        val c = foodCuisine[food]!!
        cuisinePQ[c]!!.add(Entry(newRating, food))
    }

    fun highestRated(cuisine: String): String {
        val pq = cuisinePQ[cuisine]!!
        while (true) {
            val top = pq.peek()
            if (top != null && top.rating == foodRating[top.name]) {
                return top.name
            }
            pq.poll()
        }
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
```

## Dart

```dart
import 'dart:collection';

class _FoodEntry {
  final String name;
  final int rating;
  const _FoodEntry(this.name, this.rating);
}

class FoodRatings {
  final Map<String, String> _foodToCuisine = {};
  final Map<String, int> _foodToRating = {};
  final Map<String, SplayTreeSet<_FoodEntry>> _cuisineMap = {};

  static int _compare(_FoodEntry a, _FoodEntry b) {
    if (a.rating != b.rating) return b.rating - a.rating; // higher rating first
    return a.name.compareTo(b.name); // lexicographically smaller first
  }

  FoodRatings(List<String> foods, List<String> cuisines, List<int> ratings) {
    for (int i = 0; i < foods.length; ++i) {
      final food = foods[i];
      final cuisine = cuisines[i];
      final rating = ratings[i];

      _foodToCuisine[food] = cuisine;
      _foodToRating[food] = rating;

      _cuisineMap.putIfAbsent(
          cuisine, () => SplayTreeSet<_FoodEntry>(_compare));
      _cuisineMap[cuisine]!.add(_FoodEntry(food, rating));
    }
  }

  void changeRating(String food, int newRating) {
    final oldRating = _foodToRating[food]!;
    final cuisine = _foodToCuisine[food]!;
    final set = _cuisineMap[cuisine]!;

    set.remove(_FoodEntry(food, oldRating));
    set.add(_FoodEntry(food, newRating));

    _foodToRating[food] = newRating;
  }

  String highestRated(String cuisine) {
    return _cuisineMap[cuisine]!.first.name;
  }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param2 = obj.highestRated(cuisine);
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type Item struct {
	rating int
	name   string
}

type ItemHeap []Item

func (h ItemHeap) Len() int { return len(h) }
func (h ItemHeap) Less(i, j int) bool {
	if h[i].rating != h[j].rating {
		return h[i].rating > h[j].rating // higher rating first
	}
	return h[i].name < h[j].name // lexicographically smaller first
}
func (h ItemHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *ItemHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}

func (h *ItemHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// FoodRatings struct definition
type FoodRatings struct {
	foodToCuisine map[string]string
	foodRating    map[string]int
	cuisinePQ     map[string]*ItemHeap
}

// Constructor initializes the data structures.
func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	fr := FoodRatings{
		foodToCuisine: make(map[string]string),
		foodRating:    make(map[string]int),
		cuisinePQ:     make(map[string]*ItemHeap),
	}
	for i, food := range foods {
		cuisine := cuisines[i]
		rating := ratings[i]

		fr.foodToCuisine[food] = cuisine
		fr.foodRating[food] = rating

		if _, ok := fr.cuisinePQ[cuisine]; !ok {
			h := &ItemHeap{}
			heap.Init(h)
			fr.cuisinePQ[cuisine] = h
		}
		heap.Push(fr.cuisinePQ[cuisine], Item{rating: rating, name: food})
	}
	return fr
}

// ChangeRating updates the rating of a given food.
func (this *FoodRatings) ChangeRating(food string, newRating int) {
	this.foodRating[food] = newRating
	cuisine := this.foodToCuisine[food]
	h := this.cuisinePQ[cuisine]
	heap.Push(h, Item{rating: newRating, name: food})
}

// HighestRated returns the highest rated food for a cuisine.
func (this *FoodRatings) HighestRated(cuisine string) string {
	h := this.cuisinePQ[cuisine]
	for h.Len() > 0 {
		top := (*h)[0]
		if curRating, ok := this.foodRating[top.name]; ok && curRating == top.rating {
			return top.name
		}
		heap.Pop(h)
	}
	return ""
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
 */
```

## Ruby

```ruby
class FoodRatings
  def initialize(foods, cuisines, ratings)
    @food_rating = {}
    @food_cuisine = {}
    @cuisine_heaps = Hash.new { |h, k| h[k] = [] }
    foods.each_with_index do |food, i|
      cuisine = cuisines[i]
      rating = ratings[i]
      @food_rating[food] = rating
      @food_cuisine[food] = cuisine
      heap_push(@cuisine_heaps[cuisine], [rating, food])
    end
  end

  def change_rating(food, new_rating)
    @food_rating[food] = new_rating
    cuisine = @food_cuisine[food]
    heap_push(@cuisine_heaps[cuisine], [new_rating, food])
  end

  def highest_rated(cuisine)
    heap = @cuisine_heaps[cuisine]
    loop do
      rating, name = heap[0]
      if @food_rating[name] == rating
        return name
      else
        heap_pop(heap)
      end
    end
  end

  private

  def higher?(a, b)
    if a[0] != b[0]
      a[0] > b[0]
    else
      a[1] < b[1]
    end
  end

  def heap_push(heap, item)
    heap << item
    i = heap.size - 1
    while i > 0
      parent = (i - 1) / 2
      break unless higher?(heap[i], heap[parent])
      heap[i], heap[parent] = heap[parent], heap[i]
      i = parent
    end
  end

  def heap_pop(heap)
    return nil if heap.empty?
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      heapify_down(heap, 0)
    end
    top
  end

  def heapify_down(heap, i)
    size = heap.size
    loop do
      left = i * 2 + 1
      right = left + 1
      largest = i
      if left < size && higher?(heap[left], heap[largest])
        largest = left
      end
      if right < size && higher?(heap[right], heap[largest])
        largest = right
      end
      break if largest == i
      heap[i], heap[largest] = heap[largest], heap[i]
      i = largest
    end
  end
end
```

## Scala

```scala
import scala.collection.mutable

class FoodRatings(_foods: Array[String], _cuisines: Array[String], _ratings: Array[Int]) {

  case class Food(rating: Int, name: String)

  private implicit val foodOrdering: Ordering[Food] = new Ordering[Food] {
    override def compare(a: Food, b: Food): Int = {
      if (a.rating != b.rating) a.rating - b.rating
      else b.name.compareTo(a.name) // smaller name is considered larger for the max‑heap
    }
  }

  private val ratingMap = mutable.Map[String, Int]()
  private val cuisineMap = mutable.Map[String, String]()
  private val pqMap = mutable.Map[String, mutable.PriorityQueue[Food]]()

  // initialization
  for (i <- _foods.indices) {
    val food = _foods(i)
    val cuisine = _cuisines(i)
    val rating = _ratings(i)

    ratingMap(food) = rating
    cuisineMap(food) = cuisine

    val pq = pqMap.getOrElseUpdate(cuisine, mutable.PriorityQueue.empty[Food])
    pq.enqueue(Food(rating, food))
  }

  def changeRating(food: String, newRating: Int): Unit = {
    ratingMap(food) = newRating
    val cuisine = cuisineMap(food)
    val pq = pqMap.getOrElseUpdate(cuisine, mutable.PriorityQueue.empty[Food])
    pq.enqueue(Food(newRating, food))
  }

  def highestRated(cuisine: String): String = {
    val pq = pqMap(cuisine)
    while (pq.nonEmpty && ratingMap(pq.head.name) != pq.head.rating) {
      pq.dequeue()
    }
    pq.head.name
  }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * val obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * val param_2 = obj.highestRated(cuisine)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Clone)]
struct Item {
    rating: i32,
    food: String,
}

impl PartialEq for Item {
    fn eq(&self, other: &Self) -> bool {
        self.rating == other.rating && self.food == other.food
    }
}
impl Eq for Item {}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        match self.rating.cmp(&other.rating) {
            Ordering::Equal => other.food.cmp(&self.food), // smaller name is considered greater
            ord => ord,
        }
    }
}

struct FoodRatings {
    food_to_cuisine: RefCell<HashMap<String, String>>,
    food_to_rating: RefCell<HashMap<String, i32>>,
    cuisine_to_heap: RefCell<HashMap<String, BinaryHeap<Item>>>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut ftc = HashMap::new();
        let mut ftr = HashMap::new();
        let mut cth: HashMap<String, BinaryHeap<Item>> = HashMap::new();

        for i in 0..foods.len() {
            let food = foods[i].clone();
            let cuisine = cuisines[i].clone();
            let rating = ratings[i];

            ftc.insert(food.clone(), cuisine.clone());
            ftr.insert(food.clone(), rating);
            cth.entry(cuisine)
                .or_insert_with(BinaryHeap::new)
                .push(Item { rating, food });
        }

        FoodRatings {
            food_to_cuisine: RefCell::new(ftc),
            food_to_rating: RefCell::new(ftr),
            cuisine_to_heap: RefCell::new(cth),
        }
    }

    fn change_rating(&self, food: String, new_rating: i32) {
        // Get the cuisine of the food
        let cuisine = {
            let ftc = self.food_to_cuisine.borrow();
            ftc.get(&food).unwrap().clone()
        };

        // Update rating map
        {
            let mut ftr = self.food_to_rating.borrow_mut();
            ftr.insert(food.clone(), new_rating);
        }

        // Push new entry into the corresponding heap
        {
            let mut cth = self.cuisine_to_heap.borrow_mut();
            cth.entry(cuisine)
                .or_insert_with(BinaryHeap::new)
                .push(Item { rating: new_rating, food });
        }
    }

    fn highest_rated(&self, cuisine: String) -> String {
        let mut cth = self.cuisine_to_heap.borrow_mut();
        let heap = cth.get_mut(&cuisine).unwrap();

        loop {
            if let Some(top) = heap.peek() {
                let current_rating = {
                    let ftr = self.food_to_rating.borrow();
                    *ftr.get(&top.food).unwrap()
                };
                if top.rating == current_rating {
                    return top.food.clone();
                } else {
                    heap.pop(); // discard outdated entry
                }
            } else {
                // According to constraints, this should never happen.
                return String::new();
            }
        }
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings::new(foods, cuisines, ratings);
 * obj.change_rating(food, newRating);
 * let ret_2: String = obj.highest_rated(cuisine);
 */
```

## Racket

```racket
#lang racket
(require racket/priority-queue)

(define food-ratings%
  (class object%
    (super-new)
    (init-field foods cuisines ratings)

    ;; hash tables
    (define food-rating-hash (make-hash))
    (define food-cuisine-hash (make-hash))
    (define cuisine-pq-hash (make-hash))

    ;; comparator: higher rating first, then lexicographically smaller name
    (define (food-comp a b)
      (let ([ra (first a)] [rb (first b)]
            [na (second a)] [nb (second b)])
        (if (= ra rb)
            (string<? na nb)
            (> ra rb))))

    ;; get or create priority queue for a cuisine
    (define (get-pq cuisine)
      (let ([pq (hash-ref cuisine-pq-hash cuisine #f)])
        (if pq
            pq
            (let ((newpq (make-pq food-comp)))
              (hash-set! cuisine-pq-hash cuisine newpq)
              newpq))))

    ;; initialization
    (for ([f foods] [c cuisines] [r ratings])
      (hash-set! food-rating-hash f r)
      (hash-set! food-cuisine-hash f c)
      (define pq (get-pq c))
      (pq-push! pq (list r f)))

    ;; changeRating
    (define/public (change-rating food new-rating)
      (hash-set! food-rating-hash food new-rating)
      (define cuisine (hash-ref food-cuisine-hash food))
      (define pq (get-pq cuisine))
      (pq-push! pq (list new-rating food)))

    ;; highestRated
    (define/public (highest-rated cuisine)
      (define pq (hash-ref cuisine-pq-hash cuisine))
      (let loop ()
        (define top (pq-peek pq))
        (define cur (hash-ref food-rating-hash (second top)))
        (if (= (first top) cur)
            (second top)
            (begin
              (pq-pop! pq)
              (loop)))))))
```

## Erlang

```erlang
-module(solution).
-export([food_ratings_init_/3,
         food_ratings_change_rating/2,
         food_ratings_highest_rated/1]).

%% Initialize the system with foods, cuisines and ratings.
-spec food_ratings_init_(Foods :: [unicode:unicode_binary()],
                         Cuisines :: [unicode:unicode_binary()],
                         Ratings :: [integer()]) -> any().
food_ratings_init_(Foods, Cuisines, Ratings) ->
    {FoodInfo, CuisineMap} = build_maps(Foods, Cuisines, Ratings, #{}, #{}),
    put(food_info, FoodInfo),
    put(cuisine_map, CuisineMap).

%% Change rating of a specific food.
-spec food_ratings_change_rating(Food :: unicode:unicode_binary(),
                                 NewRating :: integer()) -> any().
food_ratings_change_rating(Food, NewRating) ->
    FoodInfo = get(food_info),
    case maps:find(Food, FoodInfo) of
        {ok, {Cuisine, OldRating}} ->
            %% Update food info map.
            UpdatedFoodInfo = maps:put(Food, {Cuisine, NewRating}, FoodInfo),
            put(food_info, UpdatedFoodInfo),

            %% Update cuisine tree.
            CuisineMap = get(cuisine_map),
            Tree0 = maps:get(Cuisine, CuisineMap),
            OldKey = {-OldRating, Food},
            Tree1 = gb_trees:delete_any(OldKey, Tree0),
            NewKey = {-NewRating, Food},
            Tree2 = gb_trees:insert(NewKey, true, Tree1),
            UpdatedCuisineMap = maps:put(Cuisine, Tree2, CuisineMap),
            put(cuisine_map, UpdatedCuisineMap);
        error ->
            ok
    end.

%% Retrieve the highest rated food for a given cuisine.
-spec food_ratings_highest_rated(Cuisine :: unicode:unicode_binary()) -> unicode:unicode_binary().
food_ratings_highest_rated(Cuisine) ->
    CuisineMap = get(cuisine_map),
    Tree = maps:get(Cuisine, CuisineMap),
    {Key, _} = gb_trees:smallest(Tree),
    {_NegRating, Food} = Key,
    Food.

%% Helper to build initial maps.
build_maps([], [], [], FoodInfoAcc, CuisineMapAcc) ->
    {FoodInfoAcc, CuisineMapAcc};
build_maps([F|Fs], [C|Cs], [R|Rs], FoodInfoAcc, CuisineMapAcc) ->
    UpdatedFoodInfo = maps:put(F, {C, R}, FoodInfoAcc),
    Tree0 = maps:get(C, CuisineMapAcc, gb_trees:empty()),
    Key = {-R, F},
    Tree1 = gb_trees:insert(Key, true, Tree0),
    UpdatedCuisineMap = maps:put(C, Tree1, CuisineMapAcc),
    build_maps(Fs, Cs, Rs, UpdatedFoodInfo, UpdatedCuisineMap).
```

## Elixir

```elixir
defmodule FoodRatings do
  @spec init_(foods :: [String.t()], cuisines :: [String.t()], ratings :: [integer]) :: any()
  def init_(foods, cuisines, ratings) do
    # Remove existing tables if they exist
    for table <- [:food_to_cuisine, :food_to_rating, :cuisine_tree] do
      case :ets.whereis(table) do
        :undefined -> :ok
        _pid -> :ets.delete(table)
      end
    end

    # Create new ETS tables
    :ets.new(:food_to_cuisine, [:named_table, :public, :set])
    :ets.new(:food_to_rating, [:named_table, :public, :set])
    :ets.new(:cuisine_tree, [:named_table, :public, :set])

    Enum.zip([foods, cuisines, ratings])
    |> Enum.each(fn {food, cuisine, rating} ->
      :ets.insert(:food_to_cuisine, {food, cuisine})
      :ets.insert(:food_to_rating, {food, rating})

      case :ets.lookup(:cuisine_tree, cuisine) do
        [] ->
          tree = :gb_trees.empty()
          new_tree = :gb_trees.insert({-rating, food}, true, tree)
          :ets.insert(:cuisine_tree, {cuisine, new_tree})

        [{^cuisine, tree}] ->
          new_tree = :gb_trees.insert({-rating, food}, true, tree)
          :ets.insert(:cuisine_tree, {cuisine, new_tree})
      end
    end)

    :ok
  end

  @spec change_rating(food :: String.t(), new_rating :: integer) :: any()
  def change_rating(food, new_rating) do
    [{^food, cuisine}] = :ets.lookup(:food_to_cuisine, food)
    [{^food, old_rating}] = :ets.lookup(:food_to_rating, food)

    # Update rating map
    :ets.insert(:food_to_rating, {food, new_rating})

    # Update the tree for the corresponding cuisine
    case :ets.lookup(:cuisine_tree, cuisine) do
      [{^cuisine, tree}] ->
        tree1 = :gb_trees.delete({-old_rating, food}, tree)
        tree2 = :gb_trees.insert({-new_rating, food}, true, tree1)
        :ets.insert(:cuisine_tree, {cuisine, tree2})

      [] ->
        :ok
    end

    :ok
  end

  @spec highest_rated(cuisine :: String.t()) :: String.t()
  def highest_rated(cuisine) do
    [{^cuisine, tree}] = :ets.lookup(:cuisine_tree, cuisine)
    {{_neg_rating, food}, _value} = :gb_trees.smallest(tree)
    food
  end
end
```
