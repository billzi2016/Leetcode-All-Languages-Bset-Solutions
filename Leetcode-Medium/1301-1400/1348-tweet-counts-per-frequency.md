# 1348. Tweet Counts Per Frequency

## Cpp

```cpp
class TweetCounts {
public:
    TweetCounts() {}
    
    void recordTweet(std::string tweetName, int time) {
        tweets[tweetName].push_back(time);
    }
    
    std::vector<int> getTweetCountsPerFrequency(std::string freq, std::string tweetName, int startTime, int endTime) {
        int interval = 0;
        if (freq == "minute") interval = 60;
        else if (freq == "hour") interval = 3600;
        else if (freq == "day") interval = 86400;
        
        int buckets = (endTime - startTime) / interval + 1;
        std::vector<int> result(buckets, 0);
        
        auto it = tweets.find(tweetName);
        if (it != tweets.end()) {
            for (int t : it->second) {
                if (t < startTime || t > endTime) continue;
                int idx = (t - startTime) / interval;
                result[idx]++;
            }
        }
        return result;
    }
    
private:
    std::unordered_map<std::string, std::vector<int>> tweets;
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

## Java

```java
import java.util.*;

class TweetCounts {
    private final Map<String, List<Integer>> tweetMap;

    public TweetCounts() {
        tweetMap = new HashMap<>();
    }

    public void recordTweet(String tweetName, int time) {
        tweetMap.computeIfAbsent(tweetName, k -> new ArrayList<>()).add(time);
    }

    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        int interval;
        switch (freq) {
            case "minute":
                interval = 60;
                break;
            case "hour":
                interval = 3600;
                break;
            case "day":
                interval = 86400;
                break;
            default:
                throw new IllegalArgumentException("Invalid frequency");
        }

        int bucketCount = (endTime - startTime) / interval + 1;
        int[] counts = new int[bucketCount];

        List<Integer> times = tweetMap.getOrDefault(tweetName, Collections.emptyList());
        for (int t : times) {
            if (t < startTime || t > endTime) continue;
            int idx = (t - startTime) / interval;
            counts[idx]++;
        }

        List<Integer> result = new ArrayList<>(bucketCount);
        for (int c : counts) {
            result.add(c);
        }
        return result;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

## Python

```python
class TweetCounts(object):
    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        delta = {'minute': 60, 'hour': 3600, 'day': 86400}[freq]
        chunks = (endTime - startTime) // delta + 1
        result = [0] * chunks
        times = self.tweets.get(tweetName, [])
        for t in times:
            if startTime <= t <= endTime:
                idx = (t - startTime) // delta
                result[idx] += 1
        return result
```

## Python3

```python
class TweetCounts:
    def __init__(self):
        from collections import defaultdict
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # Insert while keeping the list sorted
        import bisect
        lst = self.tweets[tweetName]
        bisect.insort(lst, time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        interval = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        total_chunks = (endTime - startTime) // interval + 1
        res = [0] * total_chunks

        import bisect
        times = self.tweets.get(tweetName, [])
        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)

        for t in times[left:right]:
            idx = (t - startTime) // interval
            res[idx] += 1

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TimeArray {
    int *arr;
    int size;
    int cap;
} TimeArray;

typedef struct Node {
    char *key;
    TimeArray times;
    struct Node *next;
} Node;

typedef struct {
    Node **table;
    int capacity;
} TweetCounts;

/* hash function (djb2) */
static unsigned int hash_func(const char *s, int mod) {
    unsigned long hash = 5381;
    int c;
    while ((c = *s++))
        hash = ((hash << 5) + hash) + (unsigned long)c; /* hash * 33 + c */
    return (unsigned int)(hash % (unsigned long)mod);
}

/* find node, create if needed */
static Node* get_node(TweetCounts *obj, const char *key, int create) {
    unsigned int idx = hash_func(key, obj->capacity);
    Node *cur = obj->table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0)
            return cur;
        cur = cur->next;
    }
    if (!create) return NULL;
    /* create new node */
    Node *node = (Node *)malloc(sizeof(Node));
    node->key = strdup(key);
    node->times.arr = (int *)malloc(4 * sizeof(int));
    node->times.size = 0;
    node->times.cap = 4;
    node->next = obj->table[idx];
    obj->table[idx] = node;
    return node;
}

/* TweetCounts API */
TweetCounts* tweetCountsCreate() {
    TweetCounts *obj = (TweetCounts *)malloc(sizeof(TweetCounts));
    obj->capacity = 10007; /* prime number */
    obj->table = (Node **)calloc(obj->capacity, sizeof(Node *));
    return obj;
}

void tweetCountsRecordTweet(TweetCounts* obj, char* tweetName, int time) {
    Node *node = get_node(obj, tweetName, 1);
    if (node->times.size == node->times.cap) {
        node->times.cap <<= 1;
        node->times.arr = (int *)realloc(node->times.arr, node->times.cap * sizeof(int));
    }
    node->times.arr[node->times.size++] = time;
}

int* tweetCountsGetTweetCountsPerFrequency(TweetCounts* obj, char* freq, char* tweetName,
                                           int startTime, int endTime, int* retSize) {
    int interval;
    if (strcmp(freq, "minute") == 0)
        interval = 60;
    else if (strcmp(freq, "hour") == 0)
        interval = 3600;
    else
        interval = 86400; /* day */

    int buckets = (endTime - startTime) / interval + 1;
    *retSize = buckets;
    int *res = (int *)malloc(buckets * sizeof(int));
    for (int i = 0; i < buckets; ++i) res[i] = 0;

    Node *node = get_node(obj, tweetName, 0);
    if (!node) return res;

    for (int i = 0; i < node->times.size; ++i) {
        int t = node->times.arr[i];
        if (t < startTime || t > endTime) continue;
        int idx = (t - startTime) / interval;
        res[idx]++;
    }
    return res;
}

void tweetCountsFree(TweetCounts* obj) {
    for (int i = 0; i < obj->capacity; ++i) {
        Node *cur = obj->table[i];
        while (cur) {
            Node *next = cur->next;
            free(cur->key);
            free(cur->times.arr);
            free(cur);
            cur = next;
        }
    }
    free(obj->table);
    free(obj);
}

/**
 * Your TweetCounts struct will be instantiated and called as such:
 * TweetCounts* obj = tweetCountsCreate();
 * tweetCountsRecordTweet(obj, tweetName, time);
 *
 * int* param_2 = tweetCountsGetTweetCountsPerFrequency(obj, freq, tweetName,
 *                                                     startTime, endTime, retSize);
 *
 * tweetCountsFree(obj);
 */
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class TweetCounts {
    private readonly Dictionary<string, List<int>> _tweets;
    
    public TweetCounts() {
        _tweets = new Dictionary<string, List<int>>();
    }
    
    public void RecordTweet(string tweetName, int time) {
        if (!_tweets.ContainsKey(tweetName)) {
            _tweets[tweetName] = new List<int>();
        }
        _tweets[tweetName].Add(time);
    }
    
    public IList<int> GetTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        int interval = freq switch {
            "minute" => 60,
            "hour"   => 3600,
            "day"    => 86400,
            _ => throw new ArgumentException("Invalid frequency")
        };
        
        int bucketCount = (endTime - startTime) / interval + 1;
        int[] counts = new int[bucketCount];
        
        if (_tweets.TryGetValue(tweetName, out var times)) {
            foreach (int t in times) {
                if (t < startTime || t > endTime) continue;
                int idx = (t - startTime) / interval;
                counts[idx]++;
            }
        }
        
        List<int> result = new List<int>(bucketCount);
        for (int i = 0; i < bucketCount; i++) {
            result.Add(counts[i]);
        }
        return result;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.RecordTweet(tweetName,time);
 * IList<int> param_2 = obj.GetTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

## Javascript

```javascript
var TweetCounts = function() {
    this.map = new Map(); // tweetName => {times: [], sorted: bool}
};

/** 
 * @param {string} tweetName 
 * @param {number} time
 * @return {void}
 */
TweetCounts.prototype.recordTweet = function(tweetName, time) {
    if (!this.map.has(tweetName)) {
        this.map.set(tweetName, {times: [], sorted: true});
    }
    const entry = this.map.get(tweetName);
    entry.times.push(time);
    entry.sorted = false;
};

/**
 * binary search lower bound
 */
function lowerBound(arr, target) {
    let left = 0, right = arr.length;
    while (left < right) {
        const mid = (left + right) >> 1;
        if (arr[mid] < target) left = mid + 1;
        else right = mid;
    }
    return left;
}

/** 
 * @param {string} freq 
 * @param {string} tweetName 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number[]}
 */
TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    const intervalMap = {minute: 60, hour: 3600, day: 86400};
    const interval = intervalMap[freq];
    const bucketCount = Math.floor((endTime - startTime) / interval) + 1;
    const result = new Array(bucketCount).fill(0);
    
    if (!this.map.has(tweetName)) return result;
    const entry = this.map.get(tweetName);
    if (!entry.sorted) {
        entry.times.sort((a, b) => a - b);
        entry.sorted = true;
    }
    const times = entry.times;
    let idx = lowerBound(times, startTime);
    while (idx < times.length && times[idx] <= endTime) {
        const bucket = Math.floor((times[idx] - startTime) / interval);
        result[bucket]++;
        idx++;
    }
    return result;
};
```

## Typescript

```typescript
class TweetCounts {
    private tweetMap: Map<string, number[]>;

    constructor() {
        this.tweetMap = new Map();
    }

    recordTweet(tweetName: string, time: number): void {
        if (!this.tweetMap.has(tweetName)) {
            this.ttweetMap.set(tweetName, []);
        }
        this.tweetMap.get(tweetName)!.push(time);
    }

    getTweetCountsPerFrequency(freq: string, tweetName: string, startTime: number, endTime: number): number[] {
        const interval = freq === "minute" ? 60 : freq === "hour" ? 3600 : 86400;
        const bucketCount = Math.floor((endTime - startTime) / interval) + 1;
        const result = new Array(bucketCount).fill(0);
        const times = this.tweetMap.get(tweetName);
        if (!times) return result;

        times.sort((a, b) => a - b);
        let i = this.lowerBound(times, startTime);
        while (i < times.length && times[i] <= endTime) {
            const idx = Math.floor((times[i] - startTime) / interval);
            result[idx]++;
            i++;
        }
        return result;
    }

    private lowerBound(arr: number[], target: number): number {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

## Php

```php
class TweetCounts {
    private $tweets;

    public function __construct() {
        $this->tweets = [];
    }

    /**
     * @param String $tweetName
     * @param Integer $time
     * @return NULL
     */
    public function recordTweet($tweetName, $time) {
        if (!isset($this->tweets[$tweetName])) {
            $this->tweets[$tweetName] = [];
        }
        $this->tweets[$tweetName][] = $time;
    }

    /**
     * @param String $freq
     * @param String $tweetName
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Integer[]
     */
    public function getTweetCountsPerFrequency($freq, $tweetName, $startTime, $endTime) {
        $deltaMap = [
            'minute' => 60,
            'hour'   => 3600,
            'day'    => 86400
        ];
        $delta = $deltaMap[$freq];
        $bucketCount = intdiv($endTime - $startTime, $delta) + 1;
        $result = array_fill(0, $bucketCount, 0);

        if (!isset($this->tweets[$tweetName])) {
            return $result;
        }

        foreach ($this->tweets[$tweetName] as $t) {
            if ($t < $startTime || $t > $endTime) {
                continue;
            }
            $idx = intdiv($t - $startTime, $delta);
            $result[$idx]++;
        }

        return $result;
    }
}
```

## Swift

```swift
class TweetCounts {
    private var tweets = [String: [Int]]()
    private var sortedNames = Set<String>()
    
    init() {}
    
    func recordTweet(_ tweetName: String, _ time: Int) {
        tweets[tweetName, default: []].append(time)
        sortedNames.remove(tweetName)
    }
    
    func getTweetCountsPerFrequency(_ freq: String, _ tweetName: String, _ startTime: Int, _ endTime: Int) -> [Int] {
        let interval: Int
        switch freq {
        case "minute": interval = 60
        case "hour":   interval = 3600
        case "day":    interval = 86400
        default:       interval = 60
        }
        
        let chunkCount = (endTime - startTime) / interval + 1
        var result = Array(repeating: 0, count: chunkCount)
        
        guard var times = tweets[tweetName] else {
            return result
        }
        
        if !sortedNames.contains(tweetName) {
            times.sort()
            tweets[tweetName] = times
            sortedNames.insert(tweetName)
        } else {
            // retrieve the possibly updated sorted array
            times = tweets[tweetName]!
        }
        
        let lo = lowerBound(times, startTime)
        let hi = upperBound(times, endTime)
        if lo < hi {
            for i in lo..<hi {
                let idx = (times[i] - startTime) / interval
                result[idx] += 1
            }
        }
        return result
    }
    
    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var left = 0, right = arr.count
        while left < right {
            let mid = (left + right) >> 1
            if arr[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
    
    private func upperBound(_ arr: [Int], _ target: Int) -> Int {
        var left = 0, right = arr.count
        while left < right {
            let mid = (left + right) >> 1
            if arr[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class TweetCounts() {

    private val tweetMap = HashMap<String, MutableList<Int>>()

    fun recordTweet(tweetName: String, time: Int) {
        tweetMap.getOrPut(tweetName) { mutableListOf() }.add(time)
    }

    fun getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int, endTime: Int): List<Int> {
        val interval = when (freq) {
            "minute" -> 60
            "hour" -> 3600
            else -> 86400 // day
        }
        val bucketCount = ((endTime - startTime) / interval) + 1
        val result = IntArray(bucketCount)
        val times = tweetMap[tweetName] ?: return result.toList()
        for (t in times) {
            if (t in startTime..endTime) {
                val idx = (t - startTime) / interval
                result[idx]++
            }
        }
        return result.toList()
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

## Dart

```dart
class TweetCounts {
  final Map<String, List<int>> _tweets = {};

  TweetCounts();

  void recordTweet(String tweetName, int time) {
    _tweets.putIfAbsent(tweetName, () => []).add(time);
  }

  List<int> getTweetCountsPerFrequency(
      String freq, String tweetName, int startTime, int endTime) {
    int interval;
    if (freq == 'minute') {
      interval = 60;
    } else if (freq == 'hour') {
      interval = 3600;
    } else {
      interval = 86400; // day
    }

    int bucketCount = ((endTime - startTime) ~/ interval) + 1;
    List<int> result = List.filled(bucketCount, 0);
    var times = _tweets[tweetName];
    if (times == null) return result;

    for (int t in times) {
      if (t < startTime || t > endTime) continue;
      int idx = ((t - startTime) ~/ interval);
      result[idx]++;
    }
    return result;
  }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<int> param2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

## Golang

```go
type TweetCounts struct {
	tweets map[string][]int
}

func Constructor() TweetCounts {
	return TweetCounts{tweets: make(map[string][]int)}
}

func (this *TweetCounts) RecordTweet(tweetName string, time int) {
	this.tweets[tweetName] = append(this.tweets[tweetName], time)
}

func (this *TweetCounts) GetTweetCountsPerFrequency(freq string, tweetName string, startTime int, endTime int) []int {
	interval := 0
	switch freq {
	case "minute":
		interval = 60
	case "hour":
		interval = 3600
	case "day":
		interval = 86400
	}
	buckets := (endTime-startTime)/interval + 1
	res := make([]int, buckets)

	times, ok := this.tweets[tweetName]
	if !ok || len(times) == 0 {
		return res
	}

	// sort a copy to avoid mutating original order for future inserts
	sorted := append([]int(nil), times...)
	sort.Ints(sorted)

	for _, t := range sorted {
		if t < startTime {
			continue
		}
		if t > endTime {
			break
		}
		idx := (t - startTime) / interval
		res[idx]++
	}
	return res
}
```

## Ruby

```ruby
class TweetCounts
  def initialize()
    @tweets = Hash.new { |h, k| h[k] = [] }
  end

=begin
  :type tweet_name: String
  :type time: Integer
  :rtype: Void
=end
  def record_tweet(tweet_name, time)
    @tweets[tweet_name] << time
  end

=begin
  :type freq: String
  :type tweet_name: String
  :type start_time: Integer
  :type end_time: Integer
  :rtype: Integer[]
=end
  def get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time)
    interval = case freq
               when "minute" then 60
               when "hour"   then 3600
               when "day"    then 86400
               else 1
               end

    bucket_count = ((end_time - start_time) / interval) + 1
    result = Array.new(bucket_count, 0)

    return result unless @tweets.key?(tweet_name)

    @tweets[tweet_name].each do |t|
      next if t < start_time || t > end_time
      idx = (t - start_time) / interval
      result[idx] += 1
    end

    result
  end
end
```

## Scala

```scala
class TweetCounts() {
  private val tweets = scala.collection.mutable.HashMap[String, scala.collection.mutable.ArrayBuffer[Int]]()

  def recordTweet(tweetName: String, time: Int): Unit = {
    val buf = tweets.getOrElseUpdate(tweetName, scala.collection.mutable.ArrayBuffer[Int]())
    buf += time
  }

  def getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int, endTime: Int): List[Int] = {
    val interval = freq match {
      case "minute" => 60
      case "hour"   => 3600
      case "day"    => 86400
    }
    val size = ((endTime - startTime) / interval) + 1
    val counts = new Array[Int](size)

    tweets.get(tweetName).foreach { times =>
      var i = 0
      while (i < times.length) {
        val t = times(i)
        if (t >= startTime && t <= endTime) {
          val idx = (t - startTime) / interval
          counts(idx) += 1
        }
        i += 1
      }
    }

    counts.toList
  }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * val obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * val param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

## Rust

```rust
use std::collections::HashMap;
use std::cell::RefCell;

struct TweetCounts {
    data: RefCell<HashMap<String, Vec<i32>>>,
}

impl TweetCounts {
    fn new() -> Self {
        TweetCounts { data: RefCell::new(HashMap::new()) }
    }

    fn record_tweet(&self, tweet_name: String, time: i32) {
        self.data
            .borrow_mut()
            .entry(tweet_name)
            .or_insert_with(Vec::new)
            .push(time);
    }

    fn get_tweet_counts_per_frequency(
        &self,
        freq: String,
        tweet_name: String,
        start_time: i32,
        end_time: i32,
    ) -> Vec<i32> {
        let interval = match freq.as_str() {
            "minute" => 60,
            "hour" => 3600,
            "day" => 86400,
            _ => 1,
        };
        let chunks = ((end_time - start_time) / interval + 1) as usize;
        let mut result = vec![0; chunks];
        if let Some(times) = self.data.borrow().get(&tweet_name) {
            for &t in times.iter() {
                if t >= start_time && t <= end_time {
                    let idx = ((t - start_time) / interval) as usize;
                    result[idx] += 1;
                }
            }
        }
        result
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * let obj = TweetCounts::new();
 * obj.record_tweet(tweetName, time);
 * let ret_2: Vec<i32> = obj.get_tweet_counts_per_frequency(freq, tweetName, startTime, endTime);
 */
```

## Racket

```racket
(define tweet-counts%
  (class object%
    (super-new)
    (define data (make-hash))
    
    ; record-tweet : string? exact-integer? -> void?
    (define/public (record-tweet tweet-name time)
      (hash-set! data tweet-name
                 (cons time (hash-ref data tweet-name '()))))
    
    ; get-tweet-counts-per-frequency : string? string? exact-integer? exact-integer? -> (listof exact-integer?)
    (define/public (get-tweet-counts-per-frequency freq tweet-name start-time end-time)
      (define interval
        (cond [(string=? freq "minute") 60]
              [(string=? freq "hour")   3600]
              [(string=? freq "day")    86400]))
      (define total-chunks (+ 1 (quotient (- end-time start-time) interval)))
      (define counts (make-vector total-chunks 0))
      (for ([t (in-list (hash-ref data tweet-name '()))])
        (when (and (>= t start-time) (<= t end-time))
          (let* ([idx (quotient (- t start-time) interval)])
            (vector-set! counts idx (+ 1 (vector-ref counts idx))))))
      (for/list ([i (in-range total-chunks)]) (vector-ref counts i)))))
```

## Erlang

```erlang
-define(TABLE, tweet_counts_table).

-spec tweet_counts_init_() -> any().
tweet_counts_init_() ->
    case ets:info(?TABLE) of
        undefined -> ok;
        _ -> ets:delete(?TABLE)
    end,
    ets:new(?TABLE, [named_table, public, set, {keypos, 1}]).

-spec tweet_counts_record_tweet(TweetName :: unicode:unicode_binary(), Time :: integer()) -> any().
tweet_counts_record_tweet(TweetName, Time) ->
    case ets:lookup(?TABLE, TweetName) of
        [] ->
            ets:insert(?TABLE, {TweetName, [Time]});
        [{_, Times}] ->
            ets:insert(?TABLE, {TweetName, [Time | Times]})
    end.

-spec tweet_counts_get_tweet_counts_per_frequency(Freq :: unicode:unicode_binary(),
                                                  TweetName :: unicode:unicode_binary(),
                                                  StartTime :: integer(),
                                                  EndTime :: integer()) -> [integer()].
tweet_counts_get_tweet_counts_per_frequency(Freq, TweetName, StartTime, EndTime) ->
    Interval = case Freq of
        <<"minute">> -> 60;
        <<"hour">>   -> 3600;
        <<"day">>    -> 86400
    end,
    NumBuckets = ((EndTime - StartTime) div Interval) + 1,
    Arr0 = array:new(NumBuckets, {default, 0}),
    Times = case ets:lookup(?TABLE, TweetName) of
        [] -> [];
        [{_, L}] -> L
    end,
    CountsArr = lists:foldl(
        fun(Time, Arr) ->
            if Time < StartTime orelse Time > EndTime ->
                    Arr;
               true ->
                    Index = (Time - StartTime) div Interval,
                    Old = array:get(Index, Arr),
                    array:set(Index, Old + 1, Arr)
            end
        end,
        Arr0,
        Times),
    array:to_list(CountsArr).
```

## Elixir

```elixir
defmodule TweetCounts do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} = Agent.start_link(fn -> %{} end, name: __MODULE__)
    :ok
  end

  @spec record_tweet(tweet_name :: String.t(), time :: integer) :: any
  def record_tweet(tweet_name, time) do
    Agent.update(__MODULE__, fn state ->
      Map.update(state, tweet_name, [time], fn list -> [time | list] end)
    end)

    :ok
  end

  @spec get_tweet_counts_per_frequency(
          freq :: String.t(),
          tweet_name :: String.t(),
          start_time :: integer,
          end_time :: integer
        ) :: [integer]
  def get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time) do
    bucket =
      case freq do
        "minute" -> 60
        "hour" -> 3600
        "day" -> 86_400
      end

    times = Agent.get(__MODULE__, fn state -> Map.get(state, tweet_name, []) end)

    bucket_counts =
      Enum.reduce(times, %{}, fn t, acc ->
        if t >= start_time and t <= end_time do
          idx = div(t - start_time, bucket)
          Map.update(acc, idx, 1, &(&1 + 1))
        else
          acc
        end
      end)

    num_buckets = div(end_time - start_time, bucket) + 1

    Enum.map(0..(num_buckets - 1), fn i -> Map.get(bucket_counts, i, 0) end)
  end
end
```
