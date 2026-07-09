# 0981. Time Based Key-Value Store

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class TimeMap {
    unordered_map<string, vector<pair<int, string>>> store;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        auto it = store.find(key);
        if (it == store.end()) return "";
        const vector<pair<int, string>>& vec = it->second;
        int l = 0, r = (int)vec.size() - 1;
        string ans = "";
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (vec[m].first <= timestamp) {
                ans = vec[m].second;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return ans;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
```

## Java

```java
import java.util.*;

class TimeMap {
    private static class Entry {
        int timestamp;
        String value;
        Entry(int t, String v) {
            this.timestamp = t;
            this.value = v;
        }
    }

    private final Map<String, List<Entry>> map;

    public TimeMap() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(timestamp, value));
    }

    public String get(String key, int timestamp) {
        List<Entry> list = map.get(key);
        if (list == null || list.isEmpty()) return "";
        int lo = 0, hi = list.size() - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (list.get(mid).timestamp <= timestamp) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans == -1 ? "" : list.get(ans).value;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
```

## Python

```python
import bisect

class TimeMap(object):
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = {'times': [], 'vals': []}
        self.store[key]['times'].append(timestamp)
        self.store[key]['vals'].append(value)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        times = self.store[key]['times']
        idx = bisect.bisect_right(times, timestamp) - 1
        if idx < 0:
            return ""
        return self.store[key]['vals'][idx]
```

## Python3

```python
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        entries = self.store[key]
        lo, hi = 0, len(entries) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            ts, val = entries[mid]
            if ts <= timestamp:
                res = val
                lo = mid + 1
            else:
                hi = mid - 1
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 131071  // a large prime number

typedef struct Entry {
    char *key;
    int *times;
    char **vals;
    int sz;
    int cap;
    struct Entry *next;
} Entry;

typedef struct {
    Entry **buckets;
    int bucketSize;
} HashMap;

typedef struct {
    HashMap *map;
} TimeMap;

/* hash function (djb2) */
static unsigned int hash_func(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)(*s);
        s++;
    }
    return (unsigned int)h;
}

/* create a new hashmap */
static HashMap* hashmapCreate(int size) {
    HashMap *hm = (HashMap*)malloc(sizeof(HashMap));
    hm->bucketSize = size;
    hm->buckets = (Entry**)calloc(size, sizeof(Entry*));
    return hm;
}

/* find entry by key */
static Entry* hashmapFind(HashMap *hm, const char *key) {
    unsigned int idx = hash_func(key) % hm->bucketSize;
    Entry *cur = hm->buckets[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0)
            return cur;
        cur = cur->next;
    }
    return NULL;
}

/* create a new entry and insert at bucket head */
static Entry* hashmapInsert(HashMap *hm, const char *key) {
    unsigned int idx = hash_func(key) % hm->bucketSize;
    Entry *e = (Entry*)malloc(sizeof(Entry));
    e->key = strdup(key);
    e->cap = 4;
    e->sz = 0;
    e->times = (int*)malloc(e->cap * sizeof(int));
    e->vals = (char**)malloc(e->cap * sizeof(char*));
    e->next = hm->buckets[idx];
    hm->buckets[idx] = e;
    return e;
}

/* ensure capacity for entry */
static void entryEnsureCap(Entry *e) {
    if (e->sz < e->cap) return;
    e->cap <<= 1;
    e->times = (int*)realloc(e->times, e->cap * sizeof(int));
    e->vals = (char**)realloc(e->vals, e->cap * sizeof(char*));
}

/* TimeMap functions */

TimeMap* timeMapCreate() {
    TimeMap *obj = (TimeMap*)malloc(sizeof(TimeMap));
    obj->map = hashmapCreate(HASH_SIZE);
    return obj;
}

void timeMapSet(TimeMap* obj, char* key, char* value, int timestamp) {
    Entry *e = hashmapFind(obj->map, key);
    if (!e) e = hashmapInsert(obj->map, key);
    entryEnsureCap(e);
    e->times[e->sz] = timestamp;
    e->vals[e->sz] = strdup(value);
    e->sz++;
}

char* timeMapGet(TimeMap* obj, char* key, int timestamp) {
    Entry *e = hashmapFind(obj->map, key);
    if (!e) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int l = 0, r = e->sz - 1, ans = -1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (e->times[m] <= timestamp) {
            ans = m;
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    if (ans == -1) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    return strdup(e->vals[ans]);
}

void timeMapFree(TimeMap* obj) {
    for (int i = 0; i < obj->map->bucketSize; ++i) {
        Entry *cur = obj->map->buckets[i];
        while (cur) {
            Entry *next = cur->next;
            free(cur->key);
            for (int j = 0; j < cur->sz; ++j)
                free(cur->vals[j]);
            free(cur->vals);
            free(cur->times);
            free(cur);
            cur = next;
        }
    }
    free(obj->map->buckets);
    free(obj->map);
    free(obj);
}

/**
 * Your TimeMap struct will be instantiated and called as such:
 * TimeMap* obj = timeMapCreate();
 * timeMapSet(obj, key, value, timestamp);
 *
 * char* param_2 = timeMapGet(obj, key, timestamp);
 *
 * timeMapFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class TimeMap {
    private readonly Dictionary<string, List<(int ts, string val)>> _store;

    public TimeMap() {
        _store = new Dictionary<string, List<(int, string)>>();
    }
    
    public void Set(string key, string value, int timestamp) {
        if (!_store.TryGetValue(key, out var list)) {
            list = new List<(int, string)>();
            _store[key] = list;
        }
        list.Add((timestamp, value));
    }
    
    public string Get(string key, int timestamp) {
        if (!_store.TryGetValue(key, out var list))
            return "";
        
        int lo = 0, hi = list.Count - 1;
        string result = "";
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            var entry = list[mid];
            if (entry.ts == timestamp)
                return entry.val;
            if (entry.ts < timestamp) {
                result = entry.val;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return result;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.Set(key,value,timestamp);
 * string param_2 = obj.Get(key,timestamp);
 */
```

## Javascript

```javascript
var TimeMap = function() {
    this.store = new Map();
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if (!this.store.has(key)) {
        this.store.set(key, []);
    }
    this.store.get(key).push([timestamp, value]);
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    const arr = this.store.get(key);
    if (!arr) return "";
    let left = 0, right = arr.length - 1, ans = -1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        if (arr[mid][0] <= timestamp) {
            ans = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans === -1 ? "" : arr[ans][1];
};
```

## Typescript

```typescript
class TimeMap {
    private store: Map<string, { times: number[]; values: string[] }>;

    constructor() {
        this.store = new Map();
    }

    set(key: string, value: string, timestamp: number): void {
        if (!this.store.has(key)) {
            this.store.set(key, { times: [], values: [] });
        }
        const entry = this.store.get(key)!;
        entry.times.push(timestamp);
        entry.values.push(value);
    }

    get(key: string, timestamp: number): string {
        const entry = this.store.get(key);
        if (!entry) return "";
        const idx = this.binarySearch(entry.times, timestamp);
        return idx === -1 ? "" : entry.values[idx];
    }

    private binarySearch(arr: number[], target: number): number {
        let left = 0;
        let right = arr.length - 1;
        let result = -1;
        while (left <= right) {
            const mid = left + ((right - left) >> 1);
            if (arr[mid] <= target) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return result;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

## Php

```php
class TimeMap {
    private $store = [];

    function __construct() {
        
    }

    /**
     * @param String $key
     * @param String $value
     * @param Integer $timestamp
     * @return NULL
     */
    function set($key, $value, $timestamp) {
        if (!isset($this->store[$key])) {
            $this->store[$key] = ['timestamps' => [], 'values' => []];
        }
        $this->store[$key]['timestamps'][] = $timestamp;
        $this->store[$key]['values'][] = $value;
    }

    /**
     * @param String $key
     * @param Integer $timestamp
     * @return String
     */
    function get($key, $timestamp) {
        if (!isset($this->store[$key])) {
            return "";
        }
        $times = $this->store[$key]['timestamps'];
        $vals  = $this->store[$key]['values'];
        $left = 0;
        $right = count($times) - 1;
        $idx = -1;
        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($times[$mid] <= $timestamp) {
                $idx = $mid;
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }
        return $idx === -1 ? "" : $vals[$idx];
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * $obj = new TimeMap();
 * $obj->set($key, $value, $timestamp);
 * $ret_2 = $obj->get($key, $timestamp);
 */
```

## Swift

```swift
class TimeMap {
    private var store: [String: [(timestamp: Int, value: String)]] = [:]

    init() {}

    func set(_ key: String, _ value: String, _ timestamp: Int) {
        store[key, default: []].append((timestamp, value))
    }

    func get(_ key: String, _ timestamp: Int) -> String {
        guard let entries = store[key] else { return "" }
        var left = 0
        var right = entries.count - 1
        var result = ""
        while left <= right {
            let mid = (left + right) >> 1
            if entries[mid].timestamp == timestamp {
                return entries[mid].value
            } else if entries[mid].timestamp < timestamp {
                result = entries[mid].value
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class TimeMap() {
    private val store = HashMap<String, MutableList<Pair<Int, String>>>()

    fun set(key: String, value: String, timestamp: Int) {
        val list = store.getOrPut(key) { mutableListOf() }
        list.add(Pair(timestamp, value))
    }

    fun get(key: String, timestamp: Int): String {
        val list = store[key] ?: return ""
        var left = 0
        var right = list.size - 1
        var result = ""
        while (left <= right) {
            val mid = (left + right) ushr 1
            if (list[mid].first <= timestamp) {
                result = list[mid].second
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return result
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

## Dart

```dart
class TimeMap {
  final Map<String, List<int>> _times = {};
  final Map<String, List<String>> _values = {};

  TimeMap();

  void set(String key, String value, int timestamp) {
    _times.putIfAbsent(key, () => []).add(timestamp);
    _values.putIfAbsent(key, () => []).add(value);
  }

  String get(String key, int timestamp) {
    if (!_times.containsKey(key)) return "";
    List<int> times = _times[key]!;
    int idx = _upperBound(times, timestamp); // first index with time > timestamp
    if (idx == 0) return "";
    return _values[key]![idx - 1];
  }

  int _upperBound(List<int> arr, int target) {
    int lo = 0, hi = arr.length;
    while (lo < hi) {
      int mid = lo + ((hi - lo) >> 1);
      if (arr[mid] <= target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo;
  }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = TimeMap();
 * obj.set(key,value,timestamp);
 * String param2 = obj.get(key,timestamp);
 */
```

## Golang

```go
type entry struct {
	ts  int
	val string
}

type TimeMap struct {
	data map[string][]entry
}

/** Initialize your data structure here. */
func Constructor() TimeMap {
	return TimeMap{data: make(map[string][]entry)}
}

/** Set the value for key at timestamp ts. */
func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.data[key] = append(this.data[key], entry{ts: timestamp, val: value})
}

/** Get the value for key at timestamp ts. */
func (this *TimeMap) Get(key string, timestamp int) string {
	entries, ok := this.data[key]
	if !ok || len(entries) == 0 {
		return ""
	}
	// binary search for greatest ts <= timestamp
	l, r := 0, len(entries)-1
	resIdx := -1
	for l <= r {
		mid := (l + r) >> 1
		if entries[mid].ts <= timestamp {
			resIdx = mid
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	if resIdx == -1 {
		return ""
	}
	return entries[resIdx].val
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
```

## Ruby

```ruby
class TimeMap
  def initialize()
    @store = Hash.new { |h, k| h[k] = [] }
  end

=begin
  :type key: String
  :type value: String
  :type timestamp: Integer
  :rtype: Void
=end
  def set(key, value, timestamp)
    @store[key] << [timestamp, value]
  end

=begin
  :type key: String
  :type timestamp: Integer
  :rtype: String
=end
  def get(key, timestamp)
    arr = @store[key]
    return "" if arr.empty?

    left = 0
    right = arr.length - 1
    result = ""

    while left <= right
      mid = (left + right) / 2
      if arr[mid][0] <= timestamp
        result = arr[mid][1]
        left = mid + 1
      else
        right = mid - 1
      end
    end

    result
  end
end
```

## Scala

```scala
import scala.collection.mutable.{HashMap, ArrayBuffer}

class TimeMap() {

  private val store = new HashMap[String, ArrayBuffer[(Int, String)]]()

  def set(key: String, value: String, timestamp: Int): Unit = {
    val list = store.getOrElseUpdate(key, ArrayBuffer.empty[(Int, String)])
    list.append((timestamp, value))
  }

  def get(key: String, timestamp: Int): String = {
    store.get(key) match {
      case None => ""
      case Some(list) =>
        var left = 0
        var right = list.length - 1
        var ans = -1
        while (left <= right) {
          val mid = (left + right) >>> 1
          if (list(mid)._1 <= timestamp) {
            ans = mid
            left = mid + 1
          } else {
            right = mid - 1
          }
        }
        if (ans == -1) "" else list(ans)._2
    }
  }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * val obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * val param_2 = obj.get(key,timestamp)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct TimeMap {
    map: RefCell<HashMap<String, Vec<(i32, String)>>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            map: RefCell::new(HashMap::new()),
        }
    }

    fn set(&self, key: String, value: String, timestamp: i32) {
        let mut m = self.map.borrow_mut();
        m.entry(key).or_insert_with(Vec::new).push((timestamp, value));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        let m = self.map.borrow();
        if let Some(vec) = m.get(&key) {
            match vec.binary_search_by(|&(ts, _)| ts.cmp(&timestamp)) {
                Ok(idx) => return vec[idx].1.clone(),
                Err(0) => return "".to_string(),
                Err(idx) => return vec[idx - 1].1.clone(),
            }
        }
        "".to_string()
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
```

## Racket

```racket
(struct time-data (entries ts-vec val-vec) #:mutable)

(define time-map%
  (class object%
    (super-new)

    (init-field [store (make-hash)])

    ; set : string? string? exact-integer? -> void?
    (define/public (set key value timestamp)
      (let ((td (hash-ref store key #f)))
        (if td
            (begin
              (set-time-data-entries! td (cons (cons timestamp value) (time-data-entries td)))
              (set-time-data-ts-vec! td #f)
              (set-time-data-val-vec! td #f))
            (let ((new-td (time-data (list (cons timestamp value)) #f #f)))
              (hash-set! store key new-td)))))

    ; get : string? exact-integer? -> string?
    (define/public (get key timestamp)
      (let ((td (hash-ref store key #f)))
        (if (not td)
            ""
            (begin
              (when (and (not (time-data-ts-vec td))
                         (not (null? (time-data-entries td))))
                (let* ((rev (reverse (time-data-entries td))) ; ascending order
                       (ts  (list->vector (map car rev)))
                       (vals (list->vector (map cdr rev))))
                  (set-time-data-ts-vec! td ts)
                  (set-time-data-val-vec! td vals)))
              (let ((tsv (time-data-ts-vec td))
                    (valv (time-data-val-vec td)))
                (if (or (not tsv) (= (vector-length tsv) 0))
                    ""
                    (let loop ((lo 0)
                               (hi (- (vector-length tsv) 1))
                               (ans -1))
                      (if (> lo hi)
                          (if (= ans -1) "" (vector-ref valv ans))
                          (let ((mid (quotient (+ lo hi) 2)))
                            (if (<= (vector-ref tsv mid) timestamp)
                                (loop (+ mid 1) hi mid)
                                (loop lo (- mid 1) ans)))))))))))))
```

## Erlang

```erlang
-spec time_map_init_() -> any().
time_map_init_() ->
    Table = time_map_table,
    case ets:info(Table) of
        undefined -> ets:new(Table, [named_table, public, ordered_set]);
        _ -> ok
    end.

-spec time_map_set(Key :: unicode:unicode_binary(), Value :: unicode:unicode_binary(), Timestamp :: integer()) -> any().
time_map_set(Key, Value, Timestamp) ->
    Table = time_map_table,
    ets:insert(Table, {{Key, Timestamp}, Value}).

-spec time_map_get(Key :: unicode:unicode_binary(), Timestamp :: integer()) -> unicode:unicode_binary().
time_map_get(Key, Timestamp) ->
    Table = time_map_table,
    case ets:lookup(Table, {Key, Timestamp}) of
        [{_, Val}] -> Val;
        [] ->
            PrevKey = ets:prev(Table, {Key, Timestamp}),
            get_prev_val(PrevKey, Key)
    end.

get_prev_val('$end_of_table', _Key) ->
    <<>>;
get_prev_val({K,_Ts}=CompKey, KeyWanted) ->
    case K of
        KeyWanted ->
            [{_, Val}] = ets:lookup(time_map_table, CompKey),
            Val;
        _Other ->
            <<>>
    end.
```

## Elixir

```elixir
defmodule TimeMap do
  @table :time_map_table

  @spec init_() :: any
  def init_() do
    # Delete existing table if present and create a new ordered set table.
    case :ets.info(@table) do
      :undefined -> :ok
      _ -> :ets.delete(@table)
    end

    :ets.new(@table, [:named_table, :public, :ordered_set, read_concurrency: true])
    :ok
  end

  @spec set(key :: String.t(), value :: String.t(), timestamp :: integer) :: any
  def set(key, value, timestamp) do
    :ets.insert(@table, {{key, timestamp}, value})
    :ok
  end

  @spec get(key :: String.t(), timestamp :: integer) :: String.t()
  def get(key, timestamp) do
    case :ets.lookup(@table, {key, timestamp}) do
      [{{^key, ^timestamp}, val}] ->
        val

      [] ->
        case :ets.prev(@table, {key, timestamp}) do
          :"$end_of_table" ->
            ""

          prev_key = {prev_k, _} ->
            if prev_k == key do
              [{^prev_key, val}] = :ets.lookup(@table, prev_key)
              val
            else
              ""
            end
        end
    end
  end
end
```
