# 1912. Design Movie Rental System

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class MovieRentingSystem {
    unordered_map<long long,int> priceMap;                 // (shop,movie) -> price
    vector< set<pair<int,int>> > avail;                    // per movie: (price, shop)
    set< tuple<int,int,int> > rented;                      // (price, shop, movie)

    static long long key(int shop,int movie){
        return (static_cast<long long>(shop) << 20) | movie;
    }
public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        int maxMovie = 0;
        for (auto &e : entries) maxMovie = max(maxMovie, e[1]);
        avail.assign(max(10001, maxMovie + 1), {});
        for (auto &e : entries){
            int shop=e[0], movie=e[1], price=e[2];
            long long k = key(shop,movie);
            priceMap[k]=price;
            avail[movie].insert({price,shop});
        }
    }

    vector<int> search(int movie) {
        vector<int> res;
        if (movie >= (int)avail.size()) return res;
        for (auto &p : avail[movie]){
            res.push_back(p.second);
            if (res.size()==5) break;
        }
        return res;
    }

    void rent(int shop, int movie) {
        long long k = key(shop,movie);
        int price = priceMap[k];
        avail[movie].erase({price,shop});
        rented.insert({price,shop,movie});
    }

    void drop(int shop, int movie) {
        long long k = key(shop,movie);
        int price = priceMap[k];
        rented.erase({price,shop,movie});
        avail[movie].insert({price,shop});
    }

    vector<vector<int>> report() {
        vector<vector<int>> res;
        for (auto it=rented.begin(); it!=rented.end() && res.size()<5; ++it){
            int price, shop, movie;
            tie(price,shop,movie)=*it;
            res.push_back({shop,movie});
        }
        return res;
    }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */
```

## Java

```java
class MovieRentingSystem {
    private static class Pair implements Comparable<Pair> {
        int price;
        int shop;
        Pair(int price, int shop) {
            this.price = price;
            this.shop = shop;
        }
        @Override
        public int compareTo(Pair o) {
            if (price != o.price) return Integer.compare(price, o.price);
            return Integer.compare(shop, o.shop);
        }
    }

    private static class Rented implements Comparable<Rented> {
        int price;
        int shop;
        int movie;
        Rented(int price, int shop, int movie) {
            this.price = price;
            this.shop = shop;
            this.movie = movie;
        }
        @Override
        public int compareTo(Rented o) {
            if (price != o.price) return Integer.compare(price, o.price);
            if (shop != o.shop) return Integer.compare(shop, o.shop);
            return Integer.compare(movie, o.movie);
        }
    }

    private final java.util.Map<Integer, java.util.TreeSet<Pair>> available;
    private final java.util.TreeSet<Rented> rentedSet;
    private final java.util.HashMap<Long, Integer> priceMap;

    public MovieRentingSystem(int n, int[][] entries) {
        available = new java.util.HashMap<>();
        rentedSet = new java.util.TreeSet<>();
        priceMap = new java.util.HashMap<>(entries.length * 2);
        for (int[] e : entries) {
            int shop = e[0];
            int movie = e[1];
            int price = e[2];
            long key = ((long) shop << 32) | (movie & 0xffffffffL);
            priceMap.put(key, price);
            available.computeIfAbsent(movie, k -> new java.util.TreeSet<>())
                     .add(new Pair(price, shop));
        }
    }

    public java.util.List<Integer> search(int movie) {
        java.util.List<Integer> res = new java.util.ArrayList<>(5);
        java.util.TreeSet<Pair> set = available.get(movie);
        if (set != null) {
            int cnt = 0;
            for (Pair p : set) {
                res.add(p.shop);
                if (++cnt == 5) break;
            }
        }
        return res;
    }

    public void rent(int shop, int movie) {
        long key = ((long) shop << 32) | (movie & 0xffffffffL);
        int price = priceMap.get(key);
        java.util.TreeSet<Pair> set = available.get(movie);
        if (set != null) {
            set.remove(new Pair(price, shop));
        }
        rentedSet.add(new Rented(price, shop, movie));
    }

    public void drop(int shop, int movie) {
        long key = ((long) shop << 32) | (movie & 0xffffffffL);
        int price = priceMap.get(key);
        rentedSet.remove(new Rented(price, shop, movie));
        available.computeIfAbsent(movie, k -> new java.util.TreeSet<>())
                 .add(new Pair(price, shop));
    }

    public java.util.List<java.util.List<Integer>> report() {
        java.util.List<java.util.List<Integer>> res = new java.util.ArrayList<>(5);
        int cnt = 0;
        for (Rented r : rentedSet) {
            java.util.List<Integer> pair = new java.util.ArrayList<>(2);
            pair.add(r.shop);
            pair.add(r.movie);
            res.add(pair);
            if (++cnt == 5) break;
        }
        return res;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * List<Integer> param_1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<Integer>> param_4 = obj.report();
 */
```

## Python

```python
import heapq

class MovieRentingSystem(object):
    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.price = {}                     # (shop,movie) -> price
        self.rented = set()                 # set of (shop,movie) currently rented
        self.movie_heap = {}                # movie -> min-heap of (price, shop)
        self.rented_heap = []               # global heap of (price, shop, movie)

        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            if movie not in self.movie_heap:
                self.movie_heap[movie] = []
            heapq.heappush(self.movie_heap[movie], (price, shop))

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        res = []
        temp = []
        heap = self.movie_heap.get(movie, [])
        while len(res) < 5 and heap:
            price, shop = heap[0]
            if (shop, movie) in self.rented:
                # unavailable, discard permanently; will be re‑added on drop
                heapq.heappop(heap)
                continue
            # available: take it for result, but keep heap intact by pop‑push
            heapq.heappop(heap)
            res.append(shop)
            temp.append((price, shop))
        for item in temp:
            heapq.heappush(heap, item)
        return res

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        self.rented.add((shop, movie))
        price = self.price[(shop, movie)]
        heapq.heappush(self.rented_heap, (price, shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        if (shop, movie) in self.rented:
            self.rented.remove((shop, movie))
        price = self.price[(shop, movie)]
        # make it available again
        heapq.heappush(self.movie_heap[movie], (price, shop))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        while len(res) < 5 and self.rented_heap:
            price, shop, movie = self.rented_heap[0]
            if (shop, movie) not in self.rented:
                heapq.heappop(self.rented_heap)
                continue
            heapq.heappop(self.rented_heap)
            res.append([shop, movie])
            temp.append((price, shop, movie))
        for item in temp:
            heapq.heappush(self.rented_heap, item)
        return res

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```

## Python3

```python
import heapq
from collections import defaultdict
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}  # (shop,movie) -> price
        self.rented = set()  # set of (shop,movie) currently rented
        self.movie_heaps = defaultdict(list)   # movie -> min-heap of (price, shop)
        self.rented_heap = []  # heap of (price, shop, movie) for all rentals

        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            heapq.heappush(self.movie_heaps[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        heap = self.movie_heaps[movie]
        res = []
        temp = []
        while len(res) < 5 and heap:
            price, shop = heap[0]
            if (shop, movie) in self.rented:
                heapq.heappop(heap)          # discard unavailable copy
                continue
            # available copy
            heapq.heappop(heap)
            res.append(shop)
            temp.append((price, shop))
        for item in temp:
            heapq.heappush(heap, item)
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))
        price = self.price[(shop, movie)]
        heapq.heappush(self.rented_heap, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.remove((shop, movie))
        price = self.price[(shop, movie)]
        heapq.heappush(self.movie_heaps[movie], (price, shop))

    def report(self) -> List[List[int]]:
        res = []
        temp = []
        while len(res) < 5 and self.rented_heap:
            price, shop, movie = heapq.heappop(self.rented_heap)
            if (shop, movie) not in self.rented:
                continue   # stale entry
            res.append([shop, movie])
            temp.append((price, shop, movie))
        for item in temp:
            heapq.heappush(self.rented_heap, item)
        return res
```

## C

```c
typedef struct {
    int price;
    int shop;
    int movie;
} Entry;

typedef struct {
    int size;
    int capacity;
    Entry *data;
} MinHeap;

static int cmpAvail(const Entry *a, const Entry *b) {
    if (a->price != b->price) return a->price - b->price;
    return a->shop - b->shop;
}
static int cmpRented(const Entry *a, const Entry *b) {
    if (a->price != b->price) return a->price - b->price;
    if (a->shop != b->shop) return a->shop - b->shop;
    return a->movie - b->movie;
}
static MinHeap* createHeap(int cap) {
    MinHeap *h = (MinHeap *)malloc(sizeof(MinHeap));
    h->size = 0;
    h->capacity = cap;
    h->data = (Entry *)malloc(cap * sizeof(Entry));
    return h;
}
static void heapSwap(Entry *a, Entry *b) {
    Entry t = *a; *a = *b; *b = t;
}
static void siftUp(MinHeap *h, int i, int (*cmp)(const Entry *, const Entry *)) {
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (cmp(&h->data[i], &h->data[p]) < 0) {
            heapSwap(&h->data[i], &h->data[p]);
            i = p;
        } else break;
    }
}
static void siftDown(MinHeap *h, int i, int (*cmp)(const Entry *, const Entry *)) {
    while (1) {
        int l = i * 2 + 1, r = l + 1, s = i;
        if (l < h->size && cmp(&h->data[l], &h->data[s]) < 0) s = l;
        if (r < h->size && cmp(&h->data[r], &h->data[s]) < 0) s = r;
        if (s != i) {
            heapSwap(&h->data[i], &h->data[s]);
            i = s;
        } else break;
    }
}
static void heapPush(MinHeap *h, Entry e, int (*cmp)(const Entry *, const Entry *)) {
    if (h->size == h->capacity) {
        h->capacity <<= 1;
        h->data = (Entry *)realloc(h->data, h->capacity * sizeof(Entry));
    }
    h->data[h->size] = e;
    siftUp(h, h->size, cmp);
    h->size++;
}
static Entry heapTop(MinHeap *h) {
    return h->data[0];
}
static Entry heapPop(MinHeap *h, int (*cmp)(const Entry *, const Entry *)) {
    Entry ret = h->data[0];
    h->size--;
    if (h->size > 0) {
        h->data[0] = h->data[h->size];
        siftDown(h, 0, cmp);
    }
    return ret;
}
static void freeHeap(MinHeap *h) {
    if (!h) return;
    free(h->data);
    free(h);
}

typedef struct {
    int n;
    int entryCnt;
    int maxMovieId;
    int *price;          // price per entry index
    char *rented;        // 0/1 per entry index
    size_t hashCap;
    long long *hashKey;
    int *hashVal;
    MinHeap **movieHeaps;   // array indexed by movie id
    MinHeap *rentedHeap;
} MovieRentingSystem;

static inline long long makeKey(int shop, int movie) {
    return ((long long)shop << 20) | (long long)movie;
}
static void hashPut(MovieRentingSystem *obj, long long key, int val) {
    size_t pos = (size_t)(key ^ (key >> 33)) & (obj->hashCap - 1);
    while (obj->hashKey[pos] != -1 && obj->hashKey[pos] != key)
        pos = (pos + 1) & (obj->hashCap - 1);
    obj->hashKey[pos] = key;
    obj->hashVal[pos] = val;
}
static int hashGet(MovieRentingSystem *obj, long long key) {
    size_t pos = (size_t)(key ^ (key >> 33)) & (obj->hashCap - 1);
    while (obj->hashKey[pos] != -1) {
        if (obj->hashKey[pos] == key) return obj->hashVal[pos];
        pos = (pos + 1) & (obj->hashCap - 1);
    }
    return -1;
}

/*------------------- API implementations -------------------*/

MovieRentingSystem* movieRentingSystemCreate(int n, int** entries, int entriesSize, int* entriesColSize){
    MovieRentingSystem *obj = (MovieRentingSystem *)malloc(sizeof(MovieRentingSystem));
    obj->n = n;
    obj->entryCnt = entriesSize;
    obj->price = (int *)malloc(entriesSize * sizeof(int));
    obj->rented = (char *)calloc(entriesSize, sizeof(char));

    int maxM = 0;
    for (int i = 0; i < entriesSize; ++i) {
        if (entries[i][1] > maxM) maxM = entries[i][1];
    }
    obj->maxMovieId = maxM;
    obj->movieHeaps = (MinHeap **)calloc(maxM + 1, sizeof(MinHeap *));
    obj->rentedHeap = createHeap(4);

    /* hashmap init */
    size_t cap = 1;
    while (cap < (size_t)entriesSize * 2) cap <<= 1;
    obj->hashCap = cap;
    obj->hashKey = (long long *)malloc(cap * sizeof(long long));
    obj->hashVal = (int *)malloc(cap * sizeof(int));
    for (size_t i = 0; i < cap; ++i) obj->hashKey[i] = -1;

    for (int i = 0; i < entriesSize; ++i) {
        int shop = entries[i][0];
        int movie = entries[i][1];
        int price = entries[i][2];
        obj->price[i] = price;
        long long key = makeKey(shop, movie);
        hashPut(obj, key, i);

        if (!obj->movieHeaps[movie]) obj->movieHeaps[movie] = createHeap(4);
        Entry e = {price, shop, movie};
        heapPush(obj->movieHeaps[movie], e, cmpAvail);
    }
    return obj;
}

int* movieRentingSystemSearch(MovieRentingSystem* obj, int movie, int* retSize){
    if (movie > obj->maxMovieId || !obj->movieHeaps[movie]) {
        *retSize = 0;
        return NULL;
    }
    MinHeap *heap = obj->movieHeaps[movie];
    Entry tmp[5];
    int cnt = 0;
    while (cnt < 5 && heap->size > 0) {
        Entry top = heapTop(heap);
        long long key = makeKey(top.shop, top.movie);
        int idx = hashGet(obj, key);
        if (idx == -1 || obj->rented[idx]) {
            heapPop(heap, cmpAvail); // discard invalid
            continue;
        }
        tmp[cnt++] = top;
        heapPop(heap, cmpAvail);   // remove to fetch next
    }
    for (int i = 0; i < cnt; ++i) heapPush(heap, tmp[i], cmpAvail);
    if (cnt == 0) {
        *retSize = 0;
        return NULL;
    }
    int *res = (int *)malloc(cnt * sizeof(int));
    for (int i = 0; i < cnt; ++i) res[i] = tmp[i].shop;
    *retSize = cnt;
    return res;
}

void movieRentingSystemRent(MovieRentingSystem* obj, int shop, int movie){
    long long key = makeKey(shop, movie);
    int idx = hashGet(obj, key);
    if (idx == -1) return; // should not happen
    obj->rented[idx] = 1;
    Entry e = {obj->price[idx], shop, movie};
    heapPush(obj->rentedHeap, e, cmpRented);
}

void movieRentingSystemDrop(MovieRentingSystem* obj, int shop, int movie){
    long long key = makeKey(shop, movie);
    int idx = hashGet(obj, key);
    if (idx == -1) return;
    obj->rented[idx] = 0;
    Entry e = {obj->price[idx], shop, movie};
    if (!obj->movieHeaps[movie]) obj->movieHeaps[movie] = createHeap(4);
    heapPush(obj->movieHeaps[movie], e, cmpAvail);
}

int** movieRentingSystemReport(MovieRentingSystem* obj, int* retSize, int** retColSize){
    MinHeap *heap = obj->rentedHeap;
    Entry tmp[5];
    int cnt = 0;
    while (cnt < 5 && heap->size > 0) {
        Entry top = heapTop(heap);
        long long key = makeKey(top.shop, top.movie);
        int idx = hashGet(obj, key);
        if (idx == -1 || !obj->rented[idx]) {
            heapPop(heap, cmpRented); // discard invalid
            continue;
        }
        tmp[cnt++] = top;
        heapPop(heap, cmpRented);
    }
    for (int i = 0; i < cnt; ++i) heapPush(heap, tmp[i], cmpRented);

    if (cnt == 0) {
        *retSize = 0;
        *retColSize = NULL;
        return NULL;
    }

    int **res = (int **)malloc(cnt * sizeof(int *));
    *retColSize = (int *)malloc(cnt * sizeof(int));
    for (int i = 0; i < cnt; ++i) {
        res[i] = (int *)malloc(2 * sizeof(int));
        res[i][0] = tmp[i].shop;
        res[i][1] = tmp[i].movie;
        (*retColSize)[i] = 2;
    }
    *retSize = cnt;
    return res;
}

void movieRentingSystemFree(MovieRentingSystem* obj){
    if (!obj) return;
    free(obj->price);
    free(obj->rented);
    for (int i = 0; i <= obj->maxMovieId; ++i)
        if (obj->movieHeaps[i]) freeHeap(obj->movieHeaps[i]);
    free(obj->movieHeaps);
    freeHeap(obj->rentedHeap);
    free(obj->hashKey);
    free(obj->hashVal);
    free(obj);
}

/*----------------------------------------------------------*/
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class MovieRentingSystem
{
    private struct AvailableItem : IComparable<AvailableItem>
    {
        public int Price;
        public int Shop;
        public int CompareTo(AvailableItem other)
        {
            int cmp = Price.CompareTo(other.Price);
            if (cmp != 0) return cmp;
            return Shop.CompareTo(other.Shop);
        }
    }

    private struct RentedItem : IComparable<RentedItem>
    {
        public int Price;
        public int Shop;
        public int Movie;
        public int CompareTo(RentedItem other)
        {
            int cmp = Price.CompareTo(other.Price);
            if (cmp != 0) return cmp;
            cmp = Shop.CompareTo(other.Shop);
            if (cmp != 0) return cmp;
            return Movie.CompareTo(other.Movie);
        }
    }

    private readonly Dictionary<long, int> priceMap = new Dictionary<long, int>();
    private readonly Dictionary<int, SortedSet<AvailableItem>> availMap = new Dictionary<int, SortedSet<AvailableItem>>();
    private readonly SortedSet<RentedItem> rentedSet = new SortedSet<RentedItem>();

    public MovieRentingSystem(int n, int[][] entries)
    {
        foreach (var e in entries)
        {
            int shop = e[0];
            int movie = e[1];
            int price = e[2];
            long key = ((long)shop << 32) | (uint)movie;
            priceMap[key] = price;

            if (!availMap.TryGetValue(movie, out var set))
            {
                set = new SortedSet<AvailableItem>();
                availMap[movie] = set;
            }
            set.Add(new AvailableItem { Price = price, Shop = shop });
        }
    }

    public IList<int> Search(int movie)
    {
        var res = new List<int>(5);
        if (availMap.TryGetValue(movie, out var set))
        {
            foreach (var item in set)
            {
                res.Add(item.Shop);
                if (res.Count == 5) break;
            }
        }
        return res;
    }

    public void Rent(int shop, int movie)
    {
        long key = ((long)shop << 32) | (uint)movie;
        int price = priceMap[key];

        // remove from available
        var availSet = availMap[movie];
        availSet.Remove(new AvailableItem { Price = price, Shop = shop });

        // add to rented
        rentedSet.Add(new RentedItem { Price = price, Shop = shop, Movie = movie });
    }

    public void Drop(int shop, int movie)
    {
        long key = ((long)shop << 32) | (uint)movie;
        int price = priceMap[key];

        // remove from rented
        rentedSet.Remove(new RentedItem { Price = price, Shop = shop, Movie = movie });

        // add back to available
        var availSet = availMap[movie];
        availSet.Add(new AvailableItem { Price = price, Shop = shop });
    }

    public IList<IList<int>> Report()
    {
        var res = new List<IList<int>>(5);
        int cnt = 0;
        foreach (var item in rentedSet)
        {
            res.Add(new List<int> { item.Shop, item.Movie });
            if (++cnt == 5) break;
        }
        return res;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * IList<int> param_1 = obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * IList<IList<int>> param_4 = obj.Report();
 */
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} entries
 */
var MovieRentingSystem = function(n, entries) {
    // map from "shop,movie" -> price
    this.priceMap = new Map();
    // set of currently rented copies identified by "shop,movie"
    this.rentedSet = new Set();
    // map movieId -> min-heap of available copies [price, shop]
    this.availHeaps = new Map();
    // global min-heap of rented copies [price, shop, movie]
    this.rentedHeap = new MinHeap((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[2] - b[2];
    });
    
    const compAvail = (a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    };
    
    for (const [shop, movie, price] of entries) {
        const key = `${shop},${movie}`;
        this.priceMap.set(key, price);
        let heap = this.availHeaps.get(movie);
        if (!heap) {
            heap = new MinHeap(compAvail);
            this.availHeaps.set(movie, heap);
        }
        heap.push([price, shop]);
    }
};

/** 
 * @param {number} movie
 * @return {number[]}
 */
MovieRentingSystem.prototype.search = function(movie) {
    const res = [];
    const heap = this.availHeaps.get(movie);
    if (!heap) return res;
    const temp = [];
    while (res.length < 5 && heap.size() > 0) {
        const top = heap.peek();
        const key = `${top[1]},${movie}`;
        if (this.rentedSet.has(key)) {
            // stale entry, discard
            heap.pop();
            continue;
        }
        // valid available copy
        res.push(top[1]); // shop id
        temp.push(heap.pop()); // remove temporarily
    }
    // push back the valid entries we popped
    for (let i = temp.length - 1; i >= 0; --i) {
        heap.push(temp[i]);
    }
    return res;
};

/** 
 * @param {number} shop 
 * @param {number} movie
 * @return {void}
 */
MovieRentingSystem.prototype.rent = function(shop, movie) {
    const key = `${shop},${movie}`;
    this.rentedSet.add(key);
    const price = this.priceMap.get(key);
    this.rentedHeap.push([price, shop, movie]);
};

/** 
 * @param {number} shop 
 * @param {number} movie
 * @return {void}
 */
MovieRentingSystem.prototype.drop = function(shop, movie) {
    const key = `${shop},${movie}`;
    if (this.rentedSet.has(key)) this.rentedSet.delete(key);
    const price = this.priceMap.get(key);
    let heap = this.availHeaps.get(movie);
    if (!heap) {
        // should not happen but guard
        heap = new MinHeap((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });
        this.availHeaps.set(movie, heap);
    }
    heap.push([price, shop]);
};

/**
 * @return {number[][]}
 */
MovieRentingSystem.prototype.report = function() {
    const res = [];
    const temp = [];
    while (res.length < 5 && this.rentedHeap.size() > 0) {
        const top = this.rentedHeap.peek();
        const key = `${top[1]},${top[2]}`;
        if (!this.rentedSet.has(key)) {
            // stale entry, discard
            this.rentedHeap.pop();
            continue;
        }
        res.push([top[1], top[2]]); // [shop, movie]
        temp.push(this.rentedHeap.pop());
    }
    // push back the valid entries we popped
    for (let i = temp.length - 1; i >= 0; --i) {
        this.rentedHeap.push(temp[i]);
    }
    return res;
};

/* Min-heap implementation */
class MinHeap {
    constructor(comp) {
        this.data = [];
        this.comp = comp;
    }
    size() {
        return this.data.length;
    }
    peek() {
        return this.data[0];
    }
    push(item) {
        const a = this.data;
        a.push(item);
        this._siftUp(a.length - 1);
    }
    pop() {
        const a = this.data;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop();
        if (a.length > 0) {
            a[0] = last;
            this._siftDown(0);
        }
        return top;
    }
    _siftUp(i) {
        const a = this.data, comp = this.comp;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (comp(a[p], a[i]) <= 0) break;
            [a[p], a[i]] = [a[i], a[p]];
            i = p;
        }
    }
    _siftDown(i) {
        const a = this.data, comp = this.comp;
        const n = a.length;
        while (true) {
            let l = i * 2 + 1;
            let r = l + 1;
            let smallest = i;
            if (l < n && comp(a[l], a[smallest]) < 0) smallest = l;
            if (r < n && comp(a[r], a[smallest]) < 0) smallest = r;
            if (smallest === i) break;
            [a[i], a[smallest]] = [a[smallest], a[i]];
            i = smallest;
        }
    }
}

/** 
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

## Typescript

```typescript
class MinHeap<T> {
    private data: T[] = [];
    private cmp: (a: T, b: T) => number;
    constructor(cmp: (a: T, b: T) => number) {
        this.cmp = cmp;
    }
    size(): number {
        return this.data.length;
    }
    peek(): T | undefined {
        return this.data[0];
    }
    push(item: T): void {
        const a = this.data;
        a.push(item);
        this.bubbleUp(a.length - 1);
    }
    pop(): T | undefined {
        const a = this.data;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop()!;
        if (a.length > 0) {
            a[0] = last;
            this.bubbleDown(0);
        }
        return top;
    }
    private bubbleUp(idx: number): void {
        const a = this.data, cmp = this.cmp;
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (cmp(a[parent], a[idx]) <= 0) break;
            [a[parent], a[idx]] = [a[idx], a[parent]];
            idx = parent;
        }
    }
    private bubbleDown(idx: number): void {
        const a = this.data, cmp = this.cmp;
        const n = a.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = left + 1;
            let smallest = idx;
            if (left < n && cmp(a[left], a[smallest]) < 0) smallest = left;
            if (right < n && cmp(a[right], a[smallest]) < 0) smallest = right;
            if (smallest === idx) break;
            [a[idx], a[smallest]] = [a[smallest], a[idx]];
            idx = smallest;
        }
    }
}

class MovieRentingSystem {
    private priceMap: Map<string, number>;
    private availableSet: Set<string>;
    private rentedSet: Set<string>;
    private movieHeaps: Map<number, MinHeap<{ price: number; shop: number }>>;
    private rentedHeap: MinHeap<{ price: number; shop: number; movie: number }>;

    constructor(n: number, entries: number[][]) {
        this.priceMap = new Map();
        this.availableSet = new Set();
        this.rentedSet = new Set();
        this.movieHeaps = new Map();
        this.rentedHeap = new MinHeap((a, b) => {
            if (a.price !== b.price) return a.price - b.price;
            if (a.shop !== b.shop) return a.shop - b.shop;
            return a.movie - b.movie;
        });

        for (const [shop, movie, price] of entries) {
            const key = `${shop}#${movie}`;
            this.priceMap.set(key, price);
            this.availableSet.add(key);

            let heap = this.movieHeaps.get(movie);
            if (!heap) {
                heap = new MinHeap((x, y) => {
                    if (x.price !== y.price) return x.price - y.price;
                    return x.shop - y.shop;
                });
                this.movieHeaps.set(movie, heap);
            }
            heap.push({ price, shop });
        }
    }

    search(movie: number): number[] {
        const heap = this.movieHeaps.get(movie);
        if (!heap) return [];

        const result: number[] = [];
        const temp: { price: number; shop: number }[] = [];

        while (result.length < 5 && heap.size() > 0) {
            const top = heap.peek()!;
            const key = `${top.shop}#${movie}`;
            if (!this.availableSet.has(key)) {
                heap.pop();
                continue;
            }
            result.push(top.shop);
            temp.push(heap.pop()!);
        }

        for (const item of temp) heap.push(item);
        return result;
    }

    rent(shop: number, movie: number): void {
        const key = `${shop}#${movie}`;
        if (!this.availableSet.has(key)) return; // per constraints shouldn't happen
        this.availableSet.delete(key);
        this.rentedSet.add(key);
        const price = this.priceMap.get(key)!;
        this.rentedHeap.push({ price, shop, movie });
    }

    drop(shop: number, movie: number): void {
        const key = `${shop}#${movie}`;
        if (!this.rentedSet.has(key)) return; // per constraints shouldn't happen
        this.rentedSet.delete(key);
        this.availableSet.add(key);
        const price = this.priceMap.get(key)!;
        let heap = this.movieHeaps.get(movie);
        if (!heap) {
            heap = new MinHeap((x, y) => {
                if (x.price !== y.price) return x.price - y.price;
                return x.shop - y.shop;
            });
            this.movieHeaps.set(movie, heap);
        }
        heap.push({ price, shop });
    }

    report(): number[][] {
        const result: number[][] = [];
        const temp: { price: number; shop: number; movie: number }[] = [];

        while (result.length < 5 && this.rentedHeap.size() > 0) {
            const top = this.rentedHeap.peek()!;
            const key = `${top.shop}#${top.movie}`;
            if (!this.rentedSet.has(key)) {
                this.rentedHeap.pop();
                continue;
            }
            result.push([top.shop, top.movie]);
            temp.push(this.rentedHeap.pop()!);
        }

        for (const item of temp) this.rentedHeap.push(item);
        return result;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

## Php

```php
class MovieRentingSystem {
    private $priceMap = [];      // [shop][movie] => price
    private $available = [];     // [shop][movie] => bool (true if available)
    private $movieHeaps = [];    // movie => SplPriorityQueue of shops
    private $rentedHeap;         // SplPriorityQueue of [shop, movie]
    private $factor;
    private $maxMoviePlus;

    /**
     * @param Integer $n
     * @param Integer[][] $entries
     */
    function __construct($n, $entries) {
        // constants for key calculation
        $maxShop = 300000;   // given constraint
        $maxMovie = 10000;   // given constraint
        $this->factor = ($maxShop + 1) * ($maxMovie + 1); // for global rented heap
        $this->maxMoviePlus = $maxMovie + 1;

        $this->rentedHeap = new SplPriorityQueue();
        $this->rentedHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        foreach ($entries as $e) {
            list($shop, $movie, $price) = $e;
            $this->priceMap[$shop][$movie] = $price;
            $this->available[$shop][$movie] = true;

            if (!isset($this->movieHeaps[$movie])) {
                $this->movieHeaps[$movie] = new SplPriorityQueue();
                $this->movieHeaps[$movie]->setExtractFlags(SplPriorityQueue::EXTR_DATA);
            }
            // key for ordering: price then shop
            $key = $price * 1000000 + $shop;   // multiplier larger than max shop id
            $priority = -$key;                 // negative for min-heap behavior
            $this->movieHeaps[$movie]->insert($shop, $priority);
        }
    }

    /**
     * @param Integer $movie
     * @return Integer[]
     */
    function search($movie) {
        $result = [];
        if (!isset($this->movieHeaps[$movie])) {
            return $result;
        }
        $heap = $this->movieHeaps[$movie];
        $temp = [];

        while (count($result) < 5 && !$heap->isEmpty()) {
            $shop = $heap->top(); // peek
            // remove it temporarily
            $heap->extract();

            if (!empty($this->available[$shop][$movie])) {
                $result[] = $shop;
            }
            // store to reinsert later (whether available or not)
            $temp[] = $shop;
        }

        // Reinsert the popped elements back into the heap
        foreach ($temp as $shop) {
            $price = $this->priceMap[$shop][$movie];
            $key = $price * 1000000 + $shop;
            $priority = -$key;
            $heap->insert($shop, $priority);
        }

        return $result;
    }

    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function rent($shop, $movie) {
        // mark as rented
        $this->available[$shop][$movie] = false;

        // add to global rented heap
        $price = $this->priceMap[$shop][$movie];
        $key = $price * $this->factor + $shop * $this->maxMoviePlus + $movie;
        $priority = -$key;
        $this->rentedHeap->insert([$shop, $movie], $priority);
    }

    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function drop($shop, $movie) {
        // mark as available again
        $this->available[$shop][$movie] = true;
        // No need to modify heaps; lazy removal will handle it.
    }

    /**
     * @return Integer[][]
     */
    function report() {
        $result = [];
        $temp = [];

        while (count($result) < 5 && !$this->rentedHeap->isEmpty()) {
            $data = $this->rentedHeap->top(); // [$shop, $movie]
            list($shop, $movie) = $data;
            // remove temporarily
            $this->rentedHeap->extract();

            if (empty($this->available[$shop][$movie])) { // still rented
                $result[] = [$shop, $movie];
                $temp[] = $data; // keep for reinsertion
            }
            // else discard silently (no longer rented)
        }

        // Reinsert the still-rented entries back into the heap
        foreach ($temp as $data) {
            list($shop, $movie) = $data;
            $price = $this->priceMap[$shop][$movie];
            $key = $price * $this->factor + $shop * $this->maxMoviePlus + $movie;
            $priority = -$key;
            $this->rentedHeap->insert($data, $priority);
        }

        return $result;
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * $obj = new MovieRentingSystem($n, $entries);
 * $ret_1 = $obj->search($movie);
 * $obj->rent($shop, $movie);
 * $obj->drop($shop, $movie);
 * $ret_4 = $obj->report();
 */
```

## Swift

```swift
import Foundation

struct Node {
    let price: Int
    let shop: Int
}

struct RentedNode {
    let price: Int
    let shop: Int
    let movie: Int
}

class Heap<T> {
    private var elements: [T] = []
    private let areSorted: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool) {
        self.areSorted = sort
    }
    
    var isEmpty: Bool { elements.isEmpty }
    
    func peek() -> T? {
        return elements.first
    }
    
    func push(_ value: T) {
        elements.append(value)
        siftUp(elements.count - 1)
    }
    
    func pop() -> T? {
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
    
    private func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && areSorted(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && areSorted(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && areSorted(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { break }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class MovieRentingSystem {
    
    private var priceMap: [Int64: Int] = [:]
    private var rentedStatus: [Int64: Bool] = [:]
    private var movieHeaps: [Int: Heap<Node>] = [:]
    private let rentedHeap = Heap<RentedNode>(sort: { a, b in
        if a.price != b.price { return a.price < b.price }
        if a.shop != b.shop { return a.shop < b.shop }
        return a.movie < b.movie
    })
    
    init(_ n: Int, _ entries: [[Int]]) {
        for e in entries {
            let shop = e[0]
            let movie = e[1]
            let price = e[2]
            let key = makeKey(shop, movie)
            priceMap[key] = price
            rentedStatus[key] = false
            if movieHeaps[movie] == nil {
                movieHeaps[movie] = Heap<Node>(sort: { a, b in
                    if a.price != b.price { return a.price < b.price }
                    return a.shop < b.shop
                })
            }
            let node = Node(price: price, shop: shop)
            movieHeaps[movie]?.push(node)
        }
    }
    
    func search(_ movie: Int) -> [Int] {
        guard let heap = movieHeaps[movie] else { return [] }
        var result: [Int] = []
        var temp: [Node] = []
        while result.count < 5, let top = heap.peek() {
            let key = makeKey(top.shop, movie)
            if rentedStatus[key] == false {
                result.append(top.shop)
                _ = heap.pop()
                temp.append(top)
            } else {
                _ = heap.pop()
            }
        }
        for node in temp { heap.push(node) }
        return result
    }
    
    func rent(_ shop: Int, _ movie: Int) {
        let key = makeKey(shop, movie)
        rentedStatus[key] = true
        if let price = priceMap[key] {
            rentedHeap.push(RentedNode(price: price, shop: shop, movie: movie))
        }
    }
    
    func drop(_ shop: Int, _ movie: Int) {
        let key = makeKey(shop, movie)
        rentedStatus[key] = false
        if let price = priceMap[key] {
            if movieHeaps[movie] == nil {
                movieHeaps[movie] = Heap<Node>(sort: { a, b in
                    if a.price != b.price { return a.price < b.price }
                    return a.shop < b.shop
                })
            }
            movieHeaps[movie]?.push(Node(price: price, shop: shop))
        }
    }
    
    func report() -> [[Int]] {
        var result: [[Int]] = []
        var temp: [RentedNode] = []
        while result.count < 5, let top = rentedHeap.peek() {
            let key = makeKey(top.shop, top.movie)
            if rentedStatus[key] == true {
                result.append([top.shop, top.movie])
                _ = rentedHeap.pop()
                temp.append(top)
            } else {
                _ = rentedHeap.pop()
            }
        }
        for node in temp { rentedHeap.push(node) }
        return result
    }
    
    private func makeKey(_ shop: Int, _ movie: Int) -> Int64 {
        return (Int64(shop) << 32) | Int64(movie)
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj = MovieRentingSystem(n, entries)
 * let ret_1: [Int] = obj.search(movie)
 * obj.rent(shop, movie)
 * obj.drop(shop, movie)
 * let ret_4: [[Int]] = obj.report()
 */
```

## Kotlin

```kotlin
import java.util.Comparator
import java.util.TreeSet

class MovieRentingSystem(n: Int, entries: Array<IntArray>) {

    private val priceMap = HashMap<Long, Int>()
    private val availMap = HashMap<Int, TreeSet<Pair<Int, Int>>>()
    private val rented = TreeSet<Node>(compareBy<Node> { it.price }
        .thenBy { it.shop }
        .thenBy { it.movie })

    init {
        for (e in entries) {
            val shop = e[0]
            val movie = e[1]
            val price = e[2]
            val key = encode(shop, movie)
            priceMap[key] = price
            val set = availMap.getOrPut(movie) { TreeSet(priceShopComparator) }
            set.add(Pair(price, shop))
        }
    }

    private fun encode(shop: Int, movie: Int): Long {
        return (shop.toLong() shl 32) or (movie.toLong() and 0xffffffffL)
    }

    companion object {
        private val priceShopComparator = Comparator<Pair<Int, Int>> { a, b ->
            if (a.first != b.first) a.first - b.first else a.second - b.second
        }
    }

    fun search(movie: Int): List<Int> {
        val res = ArrayList<Int>()
        val set = availMap[movie] ?: return res
        val it = set.iterator()
        var cnt = 0
        while (it.hasNext() && cnt < 5) {
            res.add(it.next().second)
            cnt++
        }
        return res
    }

    fun rent(shop: Int, movie: Int) {
        val key = encode(shop, movie)
        val price = priceMap[key]!!
        availMap[movie]?.remove(Pair(price, shop))
        rented.add(Node(price, shop, movie))
    }

    fun drop(shop: Int, movie: Int) {
        val key = encode(shop, movie)
        val price = priceMap[key]!!
        rented.remove(Node(price, shop, movie))
        val set = availMap.getOrPut(movie) { TreeSet(priceShopComparator) }
        set.add(Pair(price, shop))
    }

    fun report(): List<List<Int>> {
        val res = ArrayList<List<Int>>()
        val it = rented.iterator()
        var cnt = 0
        while (it.hasNext() && cnt < 5) {
            val node = it.next()
            res.add(listOf(node.shop, node.movie))
            cnt++
        }
        return res
    }

    private data class Node(val price: Int, val shop: Int, val movie: Int)
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

## Dart

```dart
import 'dart:collection';

class Item {
  final int price;
  final int shop;
  final int movie;
  Item(this.price, this.shop, this.movie);
}

int _compareAvailable(Item a, Item b) {
  if (a.price != b.price) return a.price - b.price;
  return a.shop - b.shop;
}

int _compareRented(Item a, Item b) {
  if (a.price != b.price) return a.price - b.price;
  if (a.shop != b.shop) return a.shop - b.shop;
  return a.movie - b.movie;
}

class MovieRentingSystem {
  final Map<int, SplayTreeSet<Item>> _available = {};
  final SplayTreeSet<Item> _rented = SplayTreeSet(_compareRented);
  final Map<String, Item> _itemMap = {};

  MovieRentingSystem(int n, List<List<int>> entries) {
    for (var e in entries) {
      int shop = e[0];
      int movie = e[1];
      int price = e[2];
      var it = Item(price, shop, movie);
      String key = '${shop}_$movie';
      _itemMap[key] = it;
      _available
          .putIfAbsent(movie, () => SplayTreeSet(_compareAvailable))
          .add(it);
    }
  }

  List<int> search(int movie) {
    var set = _available[movie];
    if (set == null) return [];
    List<int> res = [];
    int cnt = 0;
    for (var it in set) {
      res.add(it.shop);
      cnt++;
      if (cnt == 5) break;
    }
    return res;
  }

  void rent(int shop, int movie) {
    String key = '${shop}_$movie';
    var it = _itemMap[key]!;
    _available[movie]?.remove(it);
    _rented.add(it);
  }

  void drop(int shop, int movie) {
    String key = '${shop}_$movie';
    var it = _itemMap[key]!;
    _rented.remove(it);
    _available
        .putIfAbsent(movie, () => SplayTreeSet(_compareAvailable))
        .add(it);
  }

  List<List<int>> report() {
    List<List<int>> res = [];
    int cnt = 0;
    for (var it in _rented) {
      res.add([it.shop, it.movie]);
      cnt++;
      if (cnt == 5) break;
    }
    return res;
  }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = MovieRentingSystem(n, entries);
 * List<int> param1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<int>> param4 = obj.report();
 */
```

## Golang

```go
type Item struct {
	price int
	shop  int
	movie int
}

type MovieHeap []Item

func (h MovieHeap) Len() int { return len(h) }
func (h MovieHeap) Less(i, j int) bool {
	if h[i].price == h[j].price {
		return h[i].shop < h[j].shop
	}
	return h[i].price < h[j].price
}
func (h MovieHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MovieHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MovieHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

type RentedHeap []Item

func (h RentedHeap) Len() int { return len(h) }
func (h RentedHeap) Less(i, j int) bool {
	if h[i].price != h[j].price {
		return h[i].price < h[j].price
	}
	if h[i].shop != h[j].shop {
		return h[i].shop < h[j].shop
	}
	return h[i].movie < h[j].movie
}
func (h RentedHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *RentedHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *RentedHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

type MovieRentingSystem struct {
	available   map[int64]bool      // true if available, false if rented
	priceMap    map[int64]int       // price for each (shop,movie)
	movieHeaps  map[int]*MovieHeap  // per movie heap of all copies
	rentedHeap  *RentedHeap         // heap of rented copies
}

func encode(shop, movie int) int64 {
	return (int64(shop) << 32) | int64(movie)
}

func Constructor(n int, entries [][]int) MovieRentingSystem {
	mrs := MovieRentingSystem{
		available:  make(map[int64]bool),
		priceMap:   make(map[int64]int),
		movieHeaps: make(map[int]*MovieHeap),
		rentedHeap: &RentedHeap{},
	}
	for _, e := range entries {
		shop, movie, price := e[0], e[1], e[2]
		it := Item{price: price, shop: shop, movie: movie}
		if _, ok := mrs.movieHeaps[movie]; !ok {
			h := &MovieHeap{}
			mrs.movieHeaps[movie] = h
		}
		heap.Push(mrs.movieHeaps[movie], it)
		key := encode(shop, movie)
		mrs.available[key] = true
		mrs.priceMap[key] = price
	}
	return mrs
}

func (this *MovieRentingSystem) Search(movie int) []int {
	h, ok := this.movieHeaps[movie]
	if !ok || h.Len() == 0 {
		return []int{}
	}
	tmp := make([]Item, 0, 5)
	res := make([]int, 0, 5)

	for len(res) < 5 && h.Len() > 0 {
		it := heap.Pop(h).(Item)
		key := encode(it.shop, it.movie)
		if this.available[key] {
			res = append(res, it.shop)
		}
		tmp = append(tmp, it)
	}
	for _, it := range tmp {
		heap.Push(h, it)
	}
	return res
}

func (this *MovieRentingSystem) Rent(shop int, movie int) {
	key := encode(shop, movie)
	if !this.available[key] {
		return
	}
	this.available[key] = false
	price := this.priceMap[key]
	it := Item{price: price, shop: shop, movie: movie}
	heap.Push(this.rentedHeap, it)
}

func (this *MovieRentingSystem) Drop(shop int, movie int) {
	key := encode(shop, movie)
	if this.available[key] {
		return
	}
	this.available[key] = true
	// No need to modify heaps; lazy deletion handles it.
}

func (this *MovieRentingSystem) Report() [][]int {
	tmp := make([]Item, 0, 5)
	res := make([][]int, 0, 5)

	for len(res) < 5 && this.rentedHeap.Len() > 0 {
		it := heap.Pop(this.rentedHeap).(Item)
		key := encode(it.shop, it.movie)
		if !this.available[key] { // still rented
			res = append(res, []int{it.shop, it.movie})
		}
		tmp = append(tmp, it)
	}
	for _, it := range tmp {
		heap.Push(this.rentedHeap, it)
	}
	return res
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * obj := Constructor(n, entries);
 * param_1 := obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * param_4 := obj.Report();
 */
```

## Ruby

```ruby
require 'set'

class MovieRentingSystem
  def initialize(n, entries)
    @price = {}
    @available = Hash.new { |h, k| h[k] = SortedSet.new }
    @rented = SortedSet.new
    entries.each do |shop, movie, price|
      @price[[shop, movie]] = price
      @available[movie].add([price, shop])
    end
  end

  def search(movie)
    res = []
    set = @available[movie]
    set.each do |pair|
      res << pair[1] # shop
      break if res.size == 5
    end
    res
  end

  def rent(shop, movie)
    price = @price[[shop, movie]]
    @available[movie].delete([price, shop])
    @rented.add([price, shop, movie])
  end

  def drop(shop, movie)
    price = @price[[shop, movie]]
    @rented.delete([price, shop, movie])
    @available[movie].add([price, shop])
  end

  def report
    res = []
    @rented.each do |trip|
      res << [trip[1], trip[2]] # [shop, movie]
      break if res.size == 5
    end
    res
  end
end
```

## Scala

```scala
import java.util.{TreeSet, Comparator}
import scala.collection.mutable

class MovieRentingSystem(_n: Int, _entries: Array[Array[Int]]) {

  private case class ShopPrice(price: Int, shop: Int)
  private val compShop = new Comparator[ShopPrice] {
    override def compare(a: ShopPrice, b: ShopPrice): Int = {
      if (a.price != b.price) Integer.compare(a.price, b.price)
      else Integer.compare(a.shop, b.shop)
    }
  }

  private case class RentedEntry(price: Int, shop: Int, movie: Int)
  private val compRented = new Comparator[RentedEntry] {
    override def compare(a: RentedEntry, b: RentedEntry): Int = {
      if (a.price != b.price) Integer.compare(a.price, b.price)
      else if (a.shop != b.shop) Integer.compare(a.shop, b.shop)
      else Integer.compare(a.movie, b.movie)
    }
  }

  private val priceMap = mutable.HashMap[(Int, Int), Int]()
  private val available = mutable.HashMap[Int, TreeSet[ShopPrice]]()
  private val rented = new TreeSet[RentedEntry](compRented)

  // initialization
  for (arr <- _entries) {
    val shop = arr(0)
    val movie = arr(1)
    val price = arr(2)
    priceMap((shop, movie)) = price
    val set = available.getOrElseUpdate(movie, new TreeSet[ShopPrice](compShop))
    set.add(ShopPrice(price, shop))
  }

  def search(movie: Int): List[Int] = {
    available.get(movie) match {
      case Some(set) if !set.isEmpty =>
        val it = set.iterator()
        val buf = mutable.ListBuffer[Int]()
        var cnt = 0
        while (it.hasNext && cnt < 5) {
          buf += it.next().shop
          cnt += 1
        }
        buf.toList
      case _ => Nil
    }
  }

  def rent(shop: Int, movie: Int): Unit = {
    val price = priceMap((shop, movie))
    // remove from available set
    val set = available(movie)
    set.remove(ShopPrice(price, shop))
    // add to rented set
    rented.add(RentedEntry(price, shop, movie))
  }

  def drop(shop: Int, movie: Int): Unit = {
    val price = priceMap((shop, movie))
    // remove from rented set
    rented.remove(RentedEntry(price, shop, movie))
    // add back to available set
    val set = available.getOrElseUpdate(movie, new TreeSet[ShopPrice](compShop))
    set.add(ShopPrice(price, shop))
  }

  def report(): List[List[Int]] = {
    val it = rented.iterator()
    val buf = mutable.ListBuffer[List[Int]]()
    var cnt = 0
    while (it.hasNext && cnt < 5) {
      val e = it.next()
      buf += List(e.shop, e.movie)
      cnt += 1
    }
    buf.toList
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, HashMap};

struct MovieRentingSystem {
    price_map: HashMap<(i32, i32), i32>,
    available: HashMap<i32, BTreeSet<(i32, i32)>>, // movie -> (price, shop)
    rented: BTreeSet<(i32, i32, i32)>,            // (price, shop, movie)
}

impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut price_map = HashMap::new();
        let mut available: HashMap<i32, BTreeSet<(i32, i32)>> = HashMap::new();

        for e in entries {
            let shop = e[0];
            let movie = e[1];
            let price = e[2];
            price_map.insert((shop, movie), price);
            available
                .entry(movie)
                .or_insert_with(BTreeSet::new)
                .insert((price, shop));
        }

        MovieRentingSystem {
            price_map,
            available,
            rented: BTreeSet::new(),
        }
    }

    fn search(&self, movie: i32) -> Vec<i32> {
        let mut res = Vec::new();
        if let Some(set) = self.available.get(&movie) {
            for &(price, shop) in set.iter().take(5) {
                let _ = price; // unused, just to emphasize ordering
                res.push(shop);
            }
        }
        res
    }

    fn rent(&mut self, shop: i32, movie: i32) {
        if let Some(&price) = self.price_map.get(&(shop, movie)) {
            if let Some(set) = self.available.get_mut(&movie) {
                set.remove(&(price, shop));
            }
            self.rented.insert((price, shop, movie));
        }
    }

    fn drop(&mut self, shop: i32, movie: i32) {
        if let Some(&price) = self.price_map.get(&(shop, movie)) {
            self.rented.remove(&(price, shop, movie));
            self.available
                .entry(movie)
                .or_insert_with(BTreeSet::new)
                .insert((price, shop));
        }
    }

    fn report(&self) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        for &(price, shop, movie) in self.rented.iter().take(5) {
            let _ = price; // unused, ordering already ensured
            res.push(vec![shop, movie]);
        }
        res
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj = MovieRentingSystem::new(n, entries);
 * let ret_1: Vec<i32> = obj.search(movie);
 * obj.rent(shop, movie);
 * obj.drop(shop, movie);
 * let ret_4: Vec<Vec<i32>> = obj.report();
 */
```

## Racket

```racket
(require racket/heap)

(define movie-renting-system%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; entries : (listof (listof exact-integer?))
    (init-field
      n
      entries)
    
    ;; price of each copy, key = (list shop movie)
    (define price-hash (make-hash))
    ;; rental status, #t if rented, #f otherwise
    (define rented? (make-hash))
    ;; per‑movie available heaps: movie -> priority queue [(price shop) ...]
    (define movie-heaps (make-hash))
    ;; global rented heap: entries = (list price shop movie)
    (define rented-heap
      (make-pq
       (lambda (a b)
         (let* ([pa (first a)] [sa (second a)] [ma (third a)]
                [pb (first b)] [sb (second b)] [mb (third b)])
           (cond [(< pa pb) #t]
                 [(> pa pb) #f]
                 [(< sa sb) #t]
                 [(> sa sb) #f]
                 [(< ma mb) #t]
                 [else #f]))))))
    
    ;; initialization
    (for ([e entries])
      (define shop  (first e))
      (define movie (second e))
      (define price (third e))
      (hash-set! price-hash (list shop movie) price)
      (hash-set! rented? (list shop movie) #f)
      (define mh
        (hash-ref movie-heaps movie
                  (lambda ()
                    (let ([pq (make-pq
                               (lambda (a b)
                                 (let* ([pa (first a)] [sa (second a)]
                                        [pb (first b)] [sb (second b)])
                                   (if (< pa pb) #t
                                       (if (> pa pb) #f
                                           (< sa sb))))))])
                      (hash-set! movie-heaps movie pq)
                      pq))))
      (pq-push! mh (list price shop)))
    
    ;; search : exact-integer? -> (listof exact-integer?)
    (define/public (search movie)
      (define heap (hash-ref movie-heaps movie #f))
      (if (not heap) '()
          (let loop ((result '()) (temp '()))
            (if (or (= (length result) 5) (pq-empty? heap))
                (begin
                  (for ([e (reverse temp)]) (pq-push! heap e))
                  (reverse result))
                (let* ([entry (pq-pop! heap)]
                       [price (first entry)]
                       [shop  (second entry)]
                       [key   (list shop movie)])
                  (if (not (hash-ref rented? key #f)) ; available
                      (loop (cons shop result) (cons entry temp))
                      (loop result (cons entry temp))))))))
    
    ;; rent : exact-integer? exact-integer? -> void?
    (define/public (rent shop movie)
      (define key (list shop movie))
      (hash-set! rented? key #t)
      (define price (hash-ref price-hash key))
      (pq-push! rented-heap (list price shop movie)))
    
    ;; drop : exact-integer? exact-integer? -> void?
    (define/public (drop shop movie)
      (define key (list shop movie))
      (hash-set! rented? key #f))
    
    ;; report : -> (listof (listof exact-integer?))
    (define/public (report)
      (let loop ((result '()) (temp '()))
        (if (or (= (length result) 5) (pq-empty? rented-heap))
            (begin
              (for ([e (reverse temp)]) (pq-push! rented-heap e))
              (reverse
               (map (lambda (entry) (list (second entry) (third entry))) result)))
            (let* ([entry (pq-pop! rented-heap)]
                   [price (first entry)]
                   [shop  (second entry)]
                   [movie (third entry)]
                   [key   (list shop movie)])
              (if (hash-ref rented? key #f)
                  (loop (cons entry result) (cons entry temp))
                  (loop result (cons entry temp))))))))
    ))
```

## Erlang

```erlang
-spec movie_renting_system_init_(N :: integer(), Entries :: [[integer()]]) -> any().
movie_renting_system_init_(_N, Entries) ->
    %% clean previous tables if they exist
    (case ets:info(price_tab) of undefined -> ok; _ -> ets:delete(price_tab) end),
    (case ets:info(avail_movie) of undefined -> ok; _ -> ets:delete(avail_movie) end),
    (case ets:info(rented_tab) of undefined -> ok; _ -> ets:delete(rented_tab) end),

    %% create tables
    ets:new(price_tab, [named_table, set, public]),
    ets:new(avail_movie, [named_table, ordered_set, public]),
    ets:new(rented_tab, [named_table, ordered_set, public]),

    %% insert entries
    lists:foreach(
        fun([Shop, Movie, Price]) ->
                ets:insert(price_tab, {{Shop, Movie}, Price}),
                ets:insert(avail_movie, {{Movie, Price, Shop}, true})
        end,
        Entries),
    ok.

-spec movie_renting_system_search(Movie :: integer()) -> [integer()].
movie_renting_system_search(Movie) ->
    MatchSpec = [
        {{{Movie, '$price', '$shop'}, '_'}, [], ['$price', '$shop']}
    ],
    {Res, _} = ets:select(avail_movie, MatchSpec, 5),
    [Shop || {_Price, Shop} <- Res].

-spec movie_renting_system_rent(Shop :: integer(), Movie :: integer()) -> any().
movie_renting_system_rent(Shop, Movie) ->
    case ets:lookup(price_tab, {Shop, Movie}) of
        [{{_, _}, Price}] ->
            %% remove from available
            ets:delete(avail_movie, {Movie, Price, Shop}),
            %% add to rented
            ets:insert(rented_tab, {{Price, Shop, Movie}, true});
        [] -> ok
    end,
    ok.

-spec movie_renting_system_drop(Shop :: integer(), Movie :: integer()) -> any().
movie_renting_system_drop(Shop, Movie) ->
    case ets:lookup(price_tab, {Shop, Movie}) of
        [{{_, _}, Price}] ->
            %% remove from rented
            ets:delete(rented_tab, {Price, Shop, Movie}),
            %% add back to available
            ets:insert(avail_movie, {{Movie, Price, Shop}, true});
        [] -> ok
    end,
    ok.

-spec movie_renting_system_report() -> [[integer()]].
movie_renting_system_report() ->
    MatchSpec = [
        {{{'$price', '$shop', '$movie'}, '_'}, [], ['$shop', '$movie']}
    ],
    {Res, _} = ets:select(rented_tab, MatchSpec, 5),
    [[Shop, Movie] || [Shop, Movie] <- Res].
```

## Elixir

```elixir
defmodule MovieRentingSystem do
  @spec init_(n :: integer, entries :: [[integer]]) :: any
  def init_( _n, entries) do
    # stop previous agent if exists
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid ->
        Agent.stop(pid)
    end

    price_map = %{}
    available = %{}

    {price_map, available} =
      Enum.reduce(entries, {price_map, available}, fn [shop, movie, price], {pmap, amap} ->
        pmap = Map.put(pmap, {shop, movie}, price)

        tree = Map.get(amap, movie, :gb_trees.empty())
        tree = :gb_trees.insert({price, shop}, nil, tree)
        amap = Map.put(amap, movie, tree)

        {pmap, amap}
      end)

    state = %{
      price_map: price_map,
      available: available,
      rented: :gb_trees.empty()
    }

    Agent.start_link(fn -> state end, name: __MODULE__)
    nil
  end

  @spec search(movie :: integer) :: [integer]
  def search(movie) do
    %{available: avail} = Agent.get(__MODULE__, & &1)
    tree = Map.get(avail, movie, :gb_trees.empty())
    keys = first_k(tree, 5)
    Enum.map(keys, fn {_price, shop} -> shop end)
  end

  @spec rent(shop :: integer, movie :: integer) :: any
  def rent(shop, movie) do
    Agent.update(__MODULE__, fn state ->
      price = Map.fetch!(state.price_map, {shop, movie})

      # remove from available
      avail_tree = Map.get(state.available, movie)
      new_avail_tree = :gb_trees.delete({price, shop}, avail_tree)

      new_available =
        if :gb_trees.is_empty(new_avail_tree) do
          Map.delete(state.available, movie)
        else
          Map.put(state.available, movie, new_avail_tree)
        end

      # add to rented
      new_rented = :gb_trees.insert({price, shop, movie}, nil, state.rented)

      %{state | available: new_available, rented: new_rented}
    end)
    nil
  end

  @spec drop(shop :: integer, movie :: integer) :: any
  def drop(shop, movie) do
    Agent.update(__MODULE__, fn state ->
      price = Map.fetch!(state.price_map, {shop, movie})

      # remove from rented
      new_rented = :gb_trees.delete({price, shop, movie}, state.rented)

      # add back to available
      avail_tree = Map.get(state.available, movie, :gb_trees.empty())
      new_avail_tree = :gb_trees.insert({price, shop}, nil, avail_tree)
      new_available = Map.put(state.available, movie, new_avail_tree)

      %{state | available: new_available, rented: new_rented}
    end)
    nil
  end

  @spec report() :: [[integer]]
  def report() do
    %{rented: rented} = Agent.get(__MODULE__, & &1)
    keys = first_k(rented, 5)

    Enum.map(keys, fn {_price, shop, movie} -> [shop, movie] end)
  end

  # Helper to get first k keys from a gb_tree in order
  defp first_k(tree, k) do
    iter = :gb_trees.iterator(tree)
    collect(iter, k, [])
  end

  defp collect(_iter, 0, acc), do: Enum.reverse(acc)

  defp collect(iter, remaining, acc) do
    case :gb_trees.next(iter) do
      :none ->
        Enum.reverse(acc)

      {key, _value, next_iter} ->
        collect(next_iter, remaining - 1, [key | acc])
    end
  end
end
```
