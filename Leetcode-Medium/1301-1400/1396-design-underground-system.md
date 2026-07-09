# 1396. Design Underground System

## Cpp

```cpp
class UndergroundSystem {
public:
    // id -> {startStation, startTime}
    unordered_map<int, pair<string,int>> checkInMap;
    // startStation -> (endStation -> {totalTime, tripCount})
    unordered_map<string, unordered_map<string, pair<long long,int>>> travelStats;
    
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        checkInMap[id] = {stationName, t};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto it = checkInMap.find(id);
        if (it == checkInMap.end()) return; // should not happen per problem guarantees
        const string& startStation = it->second.first;
        int startTime = it->second.second;
        long long duration = static_cast<long long>(t - startTime);
        
        auto &inner = travelStats[startStation];
        auto &stat = inner[stationName];
        stat.first += duration;   // total time
        stat.second += 1;         // count
        
        checkInMap.erase(it);
    }
    
    double getAverageTime(string startStation, string endStation) {
        const auto &inner = travelStats[startStation];
        const auto &stat = inner.at(endStation);
        return static_cast<double>(stat.first) / stat.second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
```

## Java

```java
class UndergroundSystem {
    private static class CheckInfo {
        String station;
        int time;
        CheckInfo(String station, int time) {
            this.station = station;
            this.time = time;
        }
    }

    private static class AvgInfo {
        long totalTime;
        int trips;
        AvgInfo() {
            this.totalTime = 0L;
            this.trips = 0;
        }
        void addTrip(int duration) {
            totalTime += duration;
            trips++;
        }
        double getAverage() {
            return (double) totalTime / trips;
        }
    }

    private final java.util.Map<Integer, CheckInfo> checkInMap;
    private final java.util.Map<String, AvgInfo> avgMap;

    public UndergroundSystem() {
        checkInMap = new java.util.HashMap<>();
        avgMap = new java.util.HashMap<>();
    }

    public void checkIn(int id, String stationName, int t) {
        checkInMap.put(id, new CheckInfo(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        CheckInfo info = checkInMap.remove(id);
        if (info == null) return; // safety, though problem guarantees consistency
        int duration = t - info.time;
        String key = info.station + "#" + stationName;
        AvgInfo avgInfo = avgMap.computeIfAbsent(key, k -> new AvgInfo());
        avgInfo.addTrip(duration);
    }

    public double getAverageTime(String startStation, String endStation) {
        String key = startStation + "#" + endStation;
        AvgInfo avgInfo = avgMap.get(key);
        return avgInfo.getAverage();
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
```

## Python

```python
class UndergroundSystem(object):
    def __init__(self):
        self.checkins = {}
        self.routes = {}

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        startStation, startTime = self.checkins.pop(id)
        key = (startStation, stationName)
        duration = t - startTime
        if key in self.routes:
            total, cnt = self.routes[key]
            self.routes[key] = (total + duration, cnt + 1)
        else:
            self.routes[key] = (duration, 1)

    def getAverageTime(self, startStation, endStation):
        total, cnt = self.routes[(startStation, endStation)]
        return total / float(cnt)
```

## Python3

```python
class UndergroundSystem:
    def __init__(self):
        self.checkins = {}  # id -> (station, time)
        self.travels = {}   # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins.pop(id)
        key = (startStation, stationName)
        if key not in self.travels:
            self.travels[key] = [0, 0]
        total, cnt = self.travels[key]
        self.travels[key][0] = total + (t - startTime)
        self.travels[key][1] = cnt + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.travels[(startStation, endStation)]
        return total / cnt
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAX_ID 1000005
#define TABLE_SIZE 20011   // prime number for hash table size

typedef struct CheckInInfo {
    char *station;
    int time;
} CheckInInfo;

typedef struct PairStat {
    char *key;                 // "start#end"
    long totalTime;
    int count;
    struct PairStat *next;
} PairStat;

typedef struct {
    CheckInInfo **checkins;    // array indexed by id
    PairStat **pairTable;      // hash table for station pairs
    int tableSize;
} UndergroundSystem;

/* djb2 hash function */
static unsigned long hash_str(const char *str) {
    unsigned long hash = 5381;
    int c;
    while ((c = (unsigned char)*str++))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    return hash;
}

/* create a new UndergroundSystem object */
UndergroundSystem* undergroundSystemCreate() {
    UndergroundSystem *obj = (UndergroundSystem *)malloc(sizeof(UndergroundSystem));
    obj->checkins = (CheckInInfo **)calloc(MAX_ID, sizeof(CheckInInfo *));
    obj->tableSize = TABLE_SIZE;
    obj->pairTable = (PairStat **)calloc(obj->tableSize, sizeof(PairStat *));
    return obj;
}

/* record check‑in */
void undergroundSystemCheckIn(UndergroundSystem* obj, int id, char* stationName, int t) {
    CheckInInfo *info = (CheckInInfo *)malloc(sizeof(CheckInInfo));
    info->station = strdup(stationName);
    info->time = t;
    obj->checkins[id] = info;
}

/* record check‑out and update statistics */
void undergroundSystemCheckOut(UndergroundSystem* obj, int id, char* stationName, int t) {
    CheckInInfo *info = obj->checkins[id];
    if (!info) return;  // safety, should not happen with valid input

    int duration = t - info->time;

    /* build key "start#end" */
    size_t lenStart = strlen(info->station);
    size_t lenEnd   = strlen(stationName);
    char *key = (char *)malloc(lenStart + 1 + lenEnd + 1); // start + '#' + end + '\0'
    sprintf(key, "%s#%s", info->station, stationName);

    unsigned long h = hash_str(key) % obj->tableSize;
    PairStat *node = obj->pairTable[h];
    while (node) {
        if (strcmp(node->key, key) == 0)
            break;
        node = node->next;
    }

    if (node) {
        node->totalTime += duration;
        node->count += 1;
        free(key);   // temporary key not needed
    } else {
        PairStat *newNode = (PairStat *)malloc(sizeof(PairStat));
        newNode->key = key;          // keep allocated key
        newNode->totalTime = duration;
        newNode->count = 1;
        newNode->next = obj->pairTable[h];
        obj->pairTable[h] = newNode;
    }

    /* clean up check‑in info */
    free(info->station);
    free(info);
    obj->checkins[id] = NULL;
}

/* retrieve average travel time between two stations */
double undergroundSystemGetAverageTime(UndergroundSystem* obj, char* startStation, char* endStation) {
    size_t lenStart = strlen(startStation);
    size_t lenEnd   = strlen(endStation);
    char *key = (char *)malloc(lenStart + 1 + lenEnd + 1);
    sprintf(key, "%s#%s", startStation, endStation);

    unsigned long h = hash_str(key) % obj->tableSize;
    PairStat *node = obj->pairTable[h];
    while (node) {
        if (strcmp(node->key, key) == 0)
            break;
        node = node->next;
    }
    free(key);

    if (!node) return 0.0; // should not happen with valid queries
    return ((double)node->totalTime) / node->count;
}

/* free all allocated memory */
void undergroundSystemFree(UndergroundSystem* obj) {
    if (!obj) return;

    /* free any remaining check‑in info */
    for (int i = 0; i < MAX_ID; ++i) {
        if (obj->checkins[i]) {
            free(obj->checkins[i]->station);
            free(obj->checkins[i]);
        }
    }
    free(obj->checkins);

    /* free pair statistics hash table */
    for (int i = 0; i < obj->tableSize; ++i) {
        PairStat *node = obj->pairTable[i];
        while (node) {
            PairStat *next = node->next;
            free(node->key);
            free(node);
            node = next;
        }
    }
    free(obj->pairTable);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class UndergroundSystem {
    private readonly Dictionary<int, (string station, int time)> _checkIns = new();
    private readonly Dictionary<string, (long totalTime, int count)> _travelStats = new();

    public UndergroundSystem() { }

    public void CheckIn(int id, string stationName, int t) {
        _checkIns[id] = (stationName, t);
    }

    public void CheckOut(int id, string stationName, int t) {
        var (startStation, startTime) = _checkIns[id];
        _checkIns.Remove(id);
        int travelTime = t - startTime;
        string key = startStation + "#" + stationName;

        if (_travelStats.TryGetValue(key, out var data)) {
            _travelStats[key] = (data.totalTime + travelTime, data.count + 1);
        } else {
            _travelStats[key] = (travelTime, 1);
        }
    }

    public double GetAverageTime(string startStation, string endStation) {
        string key = startStation + "#" + endStation;
        var (totalTime, count) = _travelStats[key];
        return (double)totalTime / count;
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * double param_3 = obj.GetAverageTime(startStation,endStation);
 */
```

## Javascript

```javascript
var UndergroundSystem = function() {
    this.checkIns = new Map(); // id -> {station, time}
    this.routes = new Map();   // "start|end" -> {totalTime, count}
};

UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    this.checkIns.set(id, { station: stationName, time: t });
};

UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    const checkInInfo = this.checkIns.get(id);
    if (!checkInInfo) return;
    const duration = t - checkInInfo.time;
    const key = `${checkInInfo.station}|${stationName}`;
    const routeInfo = this.routes.get(key);
    if (routeInfo) {
        routeInfo.totalTime += duration;
        routeInfo.count += 1;
    } else {
        this.routes.set(key, { totalTime: duration, count: 1 });
    }
    this.checkIns.delete(id);
};

UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    const key = `${startStation}|${endStation}`;
    const routeInfo = this.routes.get(key);
    return routeInfo.totalTime / routeInfo.count;
};
```

## Typescript

```typescript
class UndergroundSystem {
    private checkInMap: Map<number, { station: string; time: number }>;
    private tripMap: Map<string, { totalTime: number; count: number }>;

    constructor() {
        this.checkInMap = new Map();
        this.tripMap = new Map();
    }

    checkIn(id: number, stationName: string, t: number): void {
        this.checkInMap.set(id, { station: stationName, time: t });
    }

    checkOut(id: number, stationName: string, t: number): void {
        const entry = this.checkInMap.get(id);
        if (!entry) return;
        const travelTime = t - entry.time;
        const key = `${entry.station}-${stationName}`;
        const trip = this.tripMap.get(key);
        if (trip) {
            trip.totalTime += travelTime;
            trip.count += 1;
        } else {
            this.tripMap.set(key, { totalTime: travelTime, count: 1 });
        }
        this.checkInMap.delete(id);
    }

    getAverageTime(startStation: string, endStation: string): number {
        const key = `${startStation}-${endStation}`;
        const trip = this.tripMap.get(key);
        if (!trip) return 0;
        return trip.totalTime / trip.count;
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
```

## Php

```php
class UndergroundSystem {
    private $checkIns;
    private $travels;

    function __construct() {
        $this->checkIns = [];
        $this->travels = [];
    }

    /**
     * @param Integer $id
     * @param String $stationName
     * @param Integer $t
     * @return NULL
     */
    function checkIn($id, $stationName, $t) {
        $this->checkIns[$id] = [$stationName, $t];
    }

    /**
     * @param Integer $id
     * @param String $stationName
     * @param Integer $t
     * @return NULL
     */
    function checkOut($id, $stationName, $t) {
        if (!isset($this->checkIns[$id])) {
            return;
        }
        list($startStation, $startTime) = $this->checkIns[$id];
        unset($this->checkIns[$id]);

        $key = $startStation . '|' . $stationName;
        if (!isset($this->travels[$key])) {
            $this->travels[$key] = ['total' => 0, 'count' => 0];
        }
        $this->travels[$key]['total'] += ($t - $startTime);
        $this->travels[$key]['count'] += 1;
    }

    /**
     * @param String $startStation
     * @param String $endStation
     * @return Float
     */
    function getAverageTime($startStation, $endStation) {
        $key = $startStation . '|' . $endStation;
        $data = $this->travels[$key];
        return $data['total'] / $data['count'];
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * $obj = new UndergroundSystem();
 * $obj->checkIn($id, $stationName, $t);
 * $obj->checkOut($id, $stationName, $t);
 * $ret_3 = $obj->getAverageTime($startStation, $endStation);
 */
```

## Swift

```swift
class UndergroundSystem {
    
    private struct RouteKey: Hashable {
        let start: String
        let end: String
    }
    
    private var checkInMap: [Int: (station: String, time: Int)] = [:]
    private var travelMap: [RouteKey: (total: Int, count: Int)] = [:]
    
    init() { }
    
    func checkIn(_ id: Int, _ stationName: String, _ t: Int) {
        checkInMap[id] = (stationName, t)
    }
    
    func checkOut(_ id: Int, _ stationName: String, _ t: Int) {
        if let info = checkInMap[id] {
            let duration = t - info.time
            let key = RouteKey(start: info.station, end: stationName)
            var entry = travelMap[key] ?? (0, 0)
            entry.total += duration
            entry.count += 1
            travelMap[key] = entry
            checkInMap.removeValue(forKey: id)
        }
    }
    
    func getAverageTime(_ startStation: String, _ endStation: String) -> Double {
        let key = RouteKey(start: startStation, end: endStation)
        if let entry = travelMap[key] {
            return Double(entry.total) / Double(entry.count)
        }
        return 0.0
    }
}
```

## Kotlin

```kotlin
class UndergroundSystem() {
    private data class TripInfo(var total: Long = 0L, var count: Int = 0)

    private val checkInMap = HashMap<Int, Pair<String, Int>>()
    private val tripMap = HashMap<String, TripInfo>()

    fun checkIn(id: Int, stationName: String, t: Int) {
        checkInMap[id] = stationName to t
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        val (startStation, startTime) = checkInMap.remove(id) ?: return
        val duration = t - startTime
        val key = "$startStation#$stationName"
        val info = tripMap.getOrPut(key) { TripInfo() }
        info.total += duration.toLong()
        info.count++
    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        val key = "$startStation#$endStation"
        val info = tripMap[key] ?: return 0.0
        return info.total.toDouble() / info.count
    }
}
```

## Dart

```dart
class UndergroundSystem {
  final Map<int, _CheckInInfo> _checkIns = {};
  final Map<String, _RouteInfo> _routes = {};

  UndergroundSystem();

  void checkIn(int id, String stationName, int t) {
    _checkIns[id] = _CheckInInfo(stationName, t);
  }

  void checkOut(int id, String stationName, int t) {
    final info = _checkIns.remove(id);
    if (info == null) return;
    final key = '${info.station}|$stationName';
    final route = _routes.putIfAbsent(key, () => _RouteInfo());
    route.totalTime += (t - info.time);
    route.count += 1;
  }

  double getAverageTime(String startStation, String endStation) {
    final key = '$startStation|$endStation';
    final route = _routes[key];
    if (route == null || route.count == 0) return 0.0;
    return route.totalTime / route.count;
  }
}

class _CheckInInfo {
  final String station;
  final int time;
  _CheckInInfo(this.station, this.time);
}

class _RouteInfo {
  double totalTime = 0.0;
  int count = 0;
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param3 = obj.getAverageTime(startStation,endStation);
 */
```

## Golang

```go
type CheckInfo struct {
	station string
	time    int
}

type RouteInfo struct {
	total int64
	count int
}

type UndergroundSystem struct {
	checkIns map[int]CheckInfo
	routes   map[string]RouteInfo
}

/** Initialize your data structure here. */
func Constructor() UndergroundSystem {
	return UndergroundSystem{
		checkIns: make(map[int]CheckInfo),
		routes:   make(map[string]RouteInfo),
	}
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.checkIns[id] = CheckInfo{station: stationName, time: t}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	startInfo, ok := this.checkIns[id]
	if !ok {
		return
	}
	delete(this.checkIns, id)
	duration := int64(t - startInfo.time)
	key := startInfo.station + "->" + stationName
	route := this.routes[key]
	route.total += duration
	route.count++
	this.routes[key] = route
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	key := startStation + "->" + endStation
	route := this.routes[key]
	if route.count == 0 {
		return 0.0
	}
	return float64(route.total) / float64(route.count)
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
```

## Ruby

```ruby
class UndergroundSystem
  def initialize()
    @checkins = {}          # id => [station_name, time]
    @trip_stats = {}        # "start|end" => [total_time, count]
  end

=begin
    :type id: Integer
    :type station_name: String
    :type t: Integer
    :rtype: Void
=end
  def check_in(id, station_name, t)
    @checkins[id] = [station_name, t]
  end

=begin
    :type id: Integer
    :type station_name: String
    :type t: Integer
    :rtype: Void
=end
  def check_out(id, station_name, t)
    start_station, start_time = @checkins.delete(id)
    key = "#{start_station}|#{station_name}"
    total, cnt = @trip_stats[key] || [0, 0]
    travel_time = t - start_time
    @trip_stats[key] = [total + travel_time, cnt + 1]
  end

=begin
    :type start_station: String
    :type end_station: String
    :rtype: Float
=end
  def get_average_time(start_station, end_station)
    total, cnt = @trip_stats["#{start_station}|#{end_station}"]
    total.to_f / cnt
  end
end
```

## Scala

```scala
import scala.collection.mutable

class UndergroundSystem() {

  private val checkInMap = mutable.HashMap[Int, (String, Int)]()
  private val travelMap = mutable.HashMap[(String, String), (Long, Int)]()

  def checkIn(id: Int, stationName: String, t: Int): Unit = {
    checkInMap(id) = (stationName, t)
  }

  def checkOut(id: Int, stationName: String, t: Int): Unit = {
    val (startStation, startTime) = checkInMap.remove(id).get
    val key = (startStation, stationName)
    val duration = t - startTime
    travelMap.get(key) match {
      case Some((total, cnt)) => travelMap(key) = (total + duration, cnt + 1)
      case None => travelMap(key) = (duration.toLong, 1)
    }
  }

  def getAverageTime(startStation: String, endStation: String): Double = {
    val (total, cnt) = travelMap((startStation, endStation))
    total.toDouble / cnt
  }
}
```

## Rust

```rust
use std::collections::HashMap;
use std::cell::RefCell;

struct UndergroundSystem {
    checkins: RefCell<HashMap<i32, (String, i32)>>,
    trips: RefCell<HashMap<(String, String), (i64, i32)>>,
}

impl UndergroundSystem {
    fn new() -> Self {
        UndergroundSystem {
            checkins: RefCell::new(HashMap::new()),
            trips: RefCell::new(HashMap::new()),
        }
    }

    fn check_in(&self, id: i32, station_name: String, t: i32) {
        self.checkins.borrow_mut().insert(id, (station_name, t));
    }

    fn check_out(&self, id: i32, station_name: String, t: i32) {
        if let Some((start_station, start_time)) = self.checkins.borrow_mut().remove(&id) {
            let duration = (t - start_time) as i64;
            let key = (start_station, station_name);
            let mut trips = self.trips.borrow_mut();
            let entry = trips.entry(key).or_insert((0i64, 0i32));
            entry.0 += duration;
            entry.1 += 1;
        }
    }

    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        let trips = self.trips.borrow();
        if let Some(&(total, count)) = trips.get(&(start_station, end_station)) {
            total as f64 / count as f64
        } else {
            0.0
        }
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
```

## Racket

```racket
(define underground-system%
  (class object%
    (super-new)
    
    (define checkin-table (make-hash))
    (define travel-table (make-hash))
    
    ; check-in : exact-integer? string? exact-integer? -> void?
    (define/public (check-in id station-name t)
      (hash-set! checkin-table id (list station-name t)))
    
    ; check-out : exact-integer? string? exact-integer? -> void?
    (define/public (check-out id station-name t)
      (let* ([info (hash-ref checkin-table id)]
             [start-station (first info)]
             [start-time (second info)]
             [travel-time (- t start-time)]
             [key (list start-station station-name)])
        (define existing (hash-ref travel-table key #f))
        (if existing
            (let* ([total (first existing)]
                   [cnt (second existing)]
                   [new-total (+ total travel-time)]
                   [new-cnt (+ cnt 1)])
              (hash-set! travel-table key (list new-total new-cnt)))
            (hash-set! travel-table key (list travel-time 1)))
        (hash-remove! checkin-table id)))
    
    ; get-average-time : string? string? -> flonum?
    (define/public (get-average-time start-station end-station)
      (let* ([key (list start-station end-station)]
             [data (hash-ref travel-table key)])
        (exact->inexact (/ (first data) (second data)))))))
```

## Erlang

```erlang
-module(underground_system).
-export([underground_system_init_/0,
         underground_system_check_in/3,
         underground_system_check_out/3,
         underground_system_get_average_time/2]).

-spec underground_system_init_() -> any().
underground_system_init_() ->
    put(checkins, #{}),
    put(travel, #{}),
    ok.

-spec underground_system_check_in(Id :: integer(), StationName :: unicode:unicode_binary(), T :: integer()) -> any().
underground_system_check_in(Id, StationName, T) ->
    Checkins = get(checkins),
    NewCheckins = maps:put(Id, {StationName, T}, Checkins),
    put(checkins, NewCheckins),
    ok.

-spec underground_system_check_out(Id :: integer(), StationName :: unicode:unicode_binary(), T :: integer()) -> any().
underground_system_check_out(Id, EndStation, T) ->
    Checkins = get(checkins),
    {StartStation, StartTime} = maps:get(Id, Checkins),
    Duration = T - StartTime,
    % update travel statistics
    Travel = get(travel),
    Key = {StartStation, EndStation},
    UpdatedTravel =
        case maps:find(Key, Travel) of
            error ->
                maps:put(Key, {Duration, 1}, Travel);
            {ok, {Total, Count}} ->
                maps:put(Key, {Total + Duration, Count + 1}, Travel)
        end,
    put(travel, UpdatedTravel),
    % remove the check‑in record
    NewCheckins = maps:remove(Id, Checkins),
    put(checkins, NewCheckins),
    ok.

-spec underground_system_get_average_time(StartStation :: unicode:unicode_binary(), EndStation :: unicode:unicode_binary()) -> float().
underground_system_get_average_time(StartStation, EndStation) ->
    Travel = get(travel),
    {Total, Count} = maps:get({StartStation, EndStation}, Travel),
    Total / Count.
```

## Elixir

```elixir
defmodule UndergroundSystem do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} = Agent.start_link(fn -> %{checkins: %{}, trips: %{}} end, name: __MODULE__)
    :ok
  end

  @spec check_in(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_in(id, station_name, t) do
    Agent.update(__MODULE__, fn state ->
      %{state | checkins: Map.put(state.checkins, id, {station_name, t})}
    end)
  end

  @spec check_out(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_out(id, station_name, t) do
    {start_station, start_time} =
      Agent.get(__MODULE__, fn state ->
        Map.fetch!(state.checkins, id)
      end)

    duration = t - start_time
    key = {start_station, station_name}

    Agent.update(__MODULE__, fn state ->
      new_checkins = Map.delete(state.checkins, id)

      {total, cnt} = Map.get(state.trips, key, {0, 0})
      new_trips = Map.put(state.trips, key, {total + duration, cnt + 1})

      %{state | checkins: new_checkins, trips: new_trips}
    end)
  end

  @spec get_average_time(start_station :: String.t, end_station :: String.t) :: float
  def get_average_time(start_station, end_station) do
    Agent.get(__MODULE__, fn state ->
      {total, cnt} = Map.fetch!(state.trips, {start_station, end_station})
      total / cnt
    end)
  end
end
```
