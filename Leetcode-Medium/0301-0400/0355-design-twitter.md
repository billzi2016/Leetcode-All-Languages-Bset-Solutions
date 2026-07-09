# 0355. Design Twitter

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Twitter {
    struct TweetInfo {
        int time;
        int id;
    };
    struct HeapNode {
        int time;
        int tweetId;
        int userId;
        int idx; // index in user's tweet list
        bool operator<(const HeapNode& other) const {
            return time < other.time; // max-heap based on time
        }
    };
    
    int timestamp;
    unordered_map<int, vector<TweetInfo>> userTweets;          // userId -> list of tweets (chronological)
    unordered_map<int, unordered_set<int>> followeesMap;      // followerId -> set of followeeIds
    
public:
    Twitter() : timestamp(0) {}
    
    void postTweet(int userId, int tweetId) {
        userTweets[userId].push_back({timestamp++, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<int> result;
        unordered_set<int> candidates;
        candidates.insert(userId);
        if (followeesMap.count(userId)) {
            for (int f : followeesMap[userId]) candidates.insert(f);
        }
        
        priority_queue<HeapNode> pq;
        for (int uid : candidates) {
            const auto& vec = userTweets[uid];
            if (!vec.empty()) {
                int idx = static_cast<int>(vec.size()) - 1;
                const auto& tw = vec[idx];
                pq.push({tw.time, tw.id, uid, idx});
            }
        }
        
        while (!pq.empty() && result.size() < 10) {
            HeapNode cur = pq.top(); pq.pop();
            result.push_back(cur.tweetId);
            if (cur.idx > 0) {
                int newIdx = cur.idx - 1;
                const auto& tw = userTweets[cur.userId][newIdx];
                pq.push({tw.time, tw.id, cur.userId, newIdx});
            }
        }
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        followeesMap[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        auto it = followeesMap.find(followerId);
        if (it != followeesMap.end()) {
            it->second.erase(followeeId);
            if (it->second.empty()) followeesMap.erase(it);
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
```

## Java

```java
class Twitter {
    private static class Tweet {
        int id;
        int time;
        Tweet(int id, int time) {
            this.id = id;
            this.time = time;
        }
    }

    private int timestamp = 0;
    private final Map<Integer, Set<Integer>> followMap = new HashMap<>();
    private final Map<Integer, List<Tweet>> tweetMap = new HashMap<>();

    public Twitter() { }

    public void postTweet(int userId, int tweetId) {
        tweetMap.computeIfAbsent(userId, k -> new ArrayList<>()).add(0, new Tweet(tweetId, timestamp++));
    }

    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> followees = followMap.getOrDefault(userId, Collections.emptySet());
        PriorityQueue<Tweet> heap = new PriorityQueue<>((a, b) -> Integer.compare(b.time, a.time));

        // include user's own tweets
        addTweetsToHeap(userId, heap);
        for (int fid : followees) {
            if (fid == userId) continue;
            addTweetsToHeap(fid, heap);
        }

        List<Integer> res = new ArrayList<>(10);
        int count = 0;
        while (!heap.isEmpty() && count < 10) {
            res.add(heap.poll().id);
            count++;
        }
        return res;
    }

    private void addTweetsToHeap(int uid, PriorityQueue<Tweet> heap) {
        List<Tweet> list = tweetMap.get(uid);
        if (list == null) return;
        int limit = Math.min(10, list.size());
        for (int i = 0; i < limit; i++) {
            heap.offer(list.get(i));
        }
    }

    public void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        followMap.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        Set<Integer> set = followMap.get(followerId);
        if (set != null) {
            set.remove(followeeId);
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
```

## Python

```python
import collections
import heapq

class Twitter(object):
    def __init__(self):
        self.time = 0
        self.tweets = collections.defaultdict(list)   # userId -> list of (time, tweetId)
        self.followees = collections.defaultdict(set) # followerId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        users = set()
        users.add(userId)
        users.update(self.followees.get(userId, []))
        heap = []
        for uid in users:
            tweet_list = self.tweets.get(uid)
            if tweet_list:
                idx = len(tweet_list) - 1
                t, tid = tweet_list[idx]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))
        res = []
        while heap and len(res) < 10:
            _, tid, uid, next_idx = heapq.heappop(heap)
            res.append(tid)
            if next_idx >= 0:
                t, nid = self.tweets[uid][next_idx]
                heapq.heappush(heap, (-t, nid, uid, next_idx - 1))
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)
```

## Python3

```python
import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)          # userId -> list of (timestamp, tweetId)
        self.followees = defaultdict(set)        # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = set(self.followees.get(userId, set()))
        users.add(userId)
        for uid in users:
            tws = self.tweets.get(uid, [])
            # take up to 10 most recent tweets from this user
            for ts, tid in reversed(tws[-10:]):
                heapq.heappush(heap, (-ts, tid))
        result = []
        while heap and len(result) < 10:
            _, tid = heapq.heappop(heap)
            result.append(tid)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)
```

## C

```c
typedef struct TweetNode {
    int tweetId;
    int time;
    struct TweetNode* next;
} TweetNode;

typedef struct HeapNode {
    int tweetId;
    int time;
    TweetNode* nodePtr;
} HeapNode;

typedef struct {
    int timestamp;
    TweetNode* tweets[501];          // heads of tweet lists per user
    char follow[501][501];           // follow matrix, 1 if follower follows followee
} Twitter;

/* Max-heap functions */
static void heapSwap(HeapNode* a, HeapNode* b) {
    HeapNode tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(HeapNode* heap, int* size, HeapNode val) {
    int i = (*size)++;
    heap[i] = val;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].time >= heap[i].time) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static HeapNode heapPop(HeapNode* heap, int* size) {
    HeapNode top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= *size) break;
        int largest = l;
        if (r < *size && heap[r].time > heap[l].time) largest = r;
        if (heap[i].time >= heap[largest].time) break;
        heapSwap(&heap[i], &heap[largest]);
        i = largest;
    }
    return top;
}

/* Twitter API */
Twitter* twitterCreate() {
    Twitter* obj = (Twitter*)calloc(1, sizeof(Twitter));
    for (int i = 1; i <= 500; ++i) {
        obj->follow[i][i] = 1;   // each user follows themselves
    }
    return obj;
}

void twitterPostTweet(Twitter* obj, int userId, int tweetId) {
    TweetNode* node = (TweetNode*)malloc(sizeof(TweetNode));
    node->tweetId = tweetId;
    node->time = ++obj->timestamp;
    node->next = obj->tweets[userId];
    obj->tweets[userId] = node;
}

int* twitterGetNewsFeed(Twitter* obj, int userId, int* retSize) {
    HeapNode heap[501];
    int hsize = 0;

    for (int uid = 1; uid <= 500; ++uid) {
        if (obj->follow[userId][uid] && obj->tweets[uid]) {
            TweetNode* tn = obj->tweets[uid];
            HeapNode hn;
            hn.tweetId = tn->tweetId;
            hn.time = tn->time;
            hn.nodePtr = tn;
            heapPush(heap, &hsize, hn);
        }
    }

    int maxCount = 10;
    int* res = (int*)malloc(maxCount * sizeof(int));
    int cnt = 0;

    while (hsize > 0 && cnt < maxCount) {
        HeapNode top = heapPop(heap, &hsize);
        res[cnt++] = top.tweetId;
        if (top.nodePtr->next) {
            TweetNode* nxt = top.nodePtr->next;
            HeapNode hn;
            hn.tweetId = nxt->tweetId;
            hn.time = nxt->time;
            hn.nodePtr = nxt;
            heapPush(heap, &hsize, hn);
        }
    }

    *retSize = cnt;
    return res;
}

void twitterFollow(Twitter* obj, int followerId, int followeeId) {
    if (followerId == followeeId) return;
    obj->follow[followerId][followeeId] = 1;
}

void twitterUnfollow(Twitter* obj, int followerId, int followeeId) {
    if (followerId == followeeId) return;
    obj->follow[followerId][followeeId] = 0;
}

void twitterFree(Twitter* obj) {
    for (int i = 1; i <= 500; ++i) {
        TweetNode* cur = obj->tweets[i];
        while (cur) {
            TweetNode* nxt = cur->next;
            free(cur);
            cur = nxt;
        }
    }
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Twitter
{
    private int _timestamp;
    private readonly Dictionary<int, List<(int time, int tweetId)>> _userTweets;
    private readonly Dictionary<int, HashSet<int>> _followees;

    public Twitter()
    {
        _timestamp = 0;
        _userTweets = new Dictionary<int, List<(int, int)>>();
        _followees = new Dictionary<int, HashSet<int>>();
    }

    public void PostTweet(int userId, int tweetId)
    {
        if (!_userTweets.ContainsKey(userId))
            _userTweets[userId] = new List<(int, int)>();
        _userTweets[userId].Add((_timestamp++, tweetId));
    }

    public IList<int> GetNewsFeed(int userId)
    {
        var result = new List<int>();

        if (!_followees.ContainsKey(userId))
            _followees[userId] = new HashSet<int>();

        var users = new HashSet<int>(_followees[userId]) { userId };

        var heap = new PriorityQueue<Node, int>();
        foreach (var uid in users)
        {
            if (_userTweets.TryGetValue(uid, out var list) && list.Count > 0)
            {
                int idx = list.Count - 1;
                var t = list[idx];
                heap.Enqueue(new Node { Time = t.time, TweetId = t.tweetId, UserId = uid, Index = idx }, -t.time);
            }
        }

        while (heap.Count > 0 && result.Count < 10)
        {
            var node = heap.Dequeue();
            result.Add(node.TweetId);

            if (node.Index > 0)
            {
                int newIdx = node.Index - 1;
                var t2 = _userTweets[node.UserId][newIdx];
                heap.Enqueue(new Node { Time = t2.time, TweetId = t2.tweetId, UserId = node.UserId, Index = newIdx }, -t2.time);
            }
        }

        return result;
    }

    public void Follow(int followerId, int followeeId)
    {
        if (followerId == followeeId) return;

        if (!_followees.ContainsKey(followerId))
            _followees[followerId] = new HashSet<int>();
        _followees[followerId].Add(followeeId);
    }

    public void Unfollow(int followerId, int followeeId)
    {
        if (followerId == followeeId) return;

        if (_followees.TryGetValue(followerId, out var set))
            set.Remove(followeeId);
    }

    private class Node
    {
        public int Time;
        public int TweetId;
        public int UserId;
        public int Index;
    }
}
```

## Javascript

```javascript
var Twitter = function() {
    this.time = 0;
    this.tweets = new Map(); // userId -> array of {time, id}
    this.followMap = new Map(); // followerId -> Set of followeeIds
};

/** 
 * @param {number} userId 
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function(userId, tweetId) {
    if (!this.tweets.has(userId)) this.tweets.set(userId, []);
    this.time++;
    this.tweets.get(userId).push({ time: this.time, id: tweetId });
};

/** 
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function(userId) {
    const candidates = [];
    const followees = this.followMap.get(userId);
    if (followees) {
        for (const uid of followees) {
            const arr = this.tweets.get(uid);
            if (arr) {
                for (let i = arr.length - 1, cnt = 0; i >= 0 && cnt < 10; i--, cnt++) {
                    candidates.push(arr[i]);
                }
            }
        }
    }
    const selfArr = this.tweets.get(userId);
    if (selfArr) {
        for (let i = selfArr.length - 1, cnt = 0; i >= 0 && cnt < 10; i--, cnt++) {
            candidates.push(selfArr[i]);
        }
    }
    candidates.sort((a, b) => b.time - a.time);
    const res = [];
    for (let i = 0; i < Math.min(10, candidates.length); i++) {
        res.push(candidates[i].id);
    }
    return res;
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function(followerId, followeeId) {
    if (followerId === followeeId) return;
    let set = this.followMap.get(followerId);
    if (!set) {
        set = new Set();
        this.followMap.set(followerId, set);
    }
    set.add(followeeId);
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function(followerId, followeeId) {
    const set = this.followMap.get(followerId);
    if (set) {
        set.delete(followeeId);
    }
};
```

## Typescript

```typescript
class Twitter {
    private time: number;
    private tweets: Map<number, { id: number; time: number }[]>;
    private followees: Map<number, Set<number>>;

    constructor() {
        this.time = 0;
        this.tweets = new Map();
        this.followees = new Map();
    }

    postTweet(userId: number, tweetId: number): void {
        if (!this.tweets.has(userId)) {
            this.tweets.set(userId, []);
        }
        this.time++;
        this.tweets.get(userId)!.push({ id: tweetId, time: this.time });
    }

    getNewsFeed(userId: number): number[] {
        const result: number[] = [];
        const heap = new MaxHeap();

        // ensure the user follows themselves implicitly
        const followSet = new Set<number>();
        followSet.add(userId);
        const set = this.followees.get(userId);
        if (set) {
            for (const fid of set) followSet.add(fid);
        }

        for (const uid of followSet) {
            const userTweets = this.tweets.get(uid);
            if (userTweets && userTweets.length > 0) {
                const idx = userTweets.length - 1; // most recent tweet index
                const tw = userTweets[idx];
                heap.push({ time: tw.time, tweetId: tw.id, userId: uid, idx });
            }
        }

        while (result.length < 10 && heap.size() > 0) {
            const top = heap.pop();
            result.push(top.tweetId);
            if (top.idx > 0) {
                const newIdx = top.idx - 1;
                const tw = this.tweets.get(top.userId)![newIdx];
                heap.push({ time: tw.time, tweetId: tw.id, userId: top.userId, idx: newIdx });
            }
        }

        return result;
    }

    follow(followerId: number, followeeId: number): void {
        if (followerId === followeeId) return;
        if (!this.followees.has(followerId)) {
            this.followees.set(followerId, new Set());
        }
        this.followees.get(followerId)!.add(followeeId);
    }

    unfollow(followerId: number, followeeId: number): void {
        if (followerId === followeeId) return;
        const set = this.followees.get(followerId);
        if (set) {
            set.delete(followeeId);
        }
    }
}

interface HeapNode {
    time: number;
    tweetId: number;
    userId: number;
    idx: number;
}

class MaxHeap {
    private heap: HeapNode[] = [];

    push(node: HeapNode): void {
        this.heap.push(node);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): HeapNode {
        const top = this.heap[0];
        const last = this.heap.pop()!;
        if (this.heap.length > 0) {
            this.heap[0] = last;
            this.bubbleDown(0);
        }
        return top;
    }

    size(): number {
        return this.heap.length;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parent = (index - 1) >> 1;
            if (this.heap[parent].time >= this.heap[index].time) break;
            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
            index = parent;
        }
    }

    private bubbleDown(index: number): void {
        const n = this.heap.length;
        while (true) {
            let largest = index;
            const left = index * 2 + 1;
            const right = left + 1;
            if (left < n && this.heap[left].time > this.heap[largest].time) largest = left;
            if (right < n && this.heap[right].time > this.heap[largest].time) largest = right;
            if (largest === index) break;
            [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]];
            index = largest;
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
```

## Php

```php
class Twitter {
    private int $timestamp = 0;
    /** @var array<int, array<int, array{int,int}>> */
    private array $tweets = []; // userId => list of [timestamp, tweetId]
    /** @var array<int, array<int,bool>> */
    private array $follows = []; // followerId => set of followeeIds

    function __construct() {
        // initialization handled by property defaults
    }

    /**
     * @param Integer $userId
     * @param Integer $tweetId
     * @return NULL
     */
    function postTweet($userId, $tweetId) {
        $this->timestamp++;
        if (!isset($this->tweets[$userId])) {
            $this->tweets[$userId] = [];
        }
        // prepend for faster recent access (optional)
        $this->tweets[$userId][] = [$this->timestamp, $tweetId];
    }

    /**
     * @param Integer $userId
     * @return Integer[]
     */
    function getNewsFeed($userId) {
        $candidates = [];

        // own tweets
        if (isset($this->tweets[$userId])) {
            $candidates = array_merge($candidates, $this->tweets[$userId]);
        }

        // followees' tweets
        if (isset($this->follows[$userId])) {
            foreach ($this->follows[$userId] as $followeeId => $_) {
                if (isset($this->tweets[$followeeId])) {
                    $candidates = array_merge($candidates, $this->tweets[$followeeId]);
                }
            }
        }

        // sort by timestamp descending
        usort($candidates, function ($a, $b) {
            return $b[0] <=> $a[0];
        });

        $result = [];
        $limit = min(10, count($candidates));
        for ($i = 0; $i < $limit; $i++) {
            $result[] = $candidates[$i][1];
        }
        return $result;
    }

    /**
     * @param Integer $followerId
     * @param Integer $followeeId
     * @return NULL
     */
    function follow($followerId, $followeeId) {
        if ($followerId == $followeeId) {
            return;
        }
        if (!isset($this->follows[$followerId])) {
            $this->follows[$followerId] = [];
        }
        $this->follows[$followerId][$followeeId] = true;
    }

    /**
     * @param Integer $followerId
     * @param Integer $followeeId
     * @return NULL
     */
    function unfollow($followerId, $followeeId) {
        if ($followerId == $followeeId) {
            return;
        }
        if (isset($this->follows[$followerId][$followeeId])) {
            unset($this->follows[$followerId][$followeeId]);
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * $obj = new Twitter();
 * $obj->postTweet($userId, $tweetId);
 * $ret_2 = $obj->getNewsFeed($userId);
 * $obj->follow($followerId, $followeeId);
 * $obj->unfollow($followerId, $followeeId);
 */
```

## Swift

```swift
class Twitter {
    private var timestamp = 0
    private var tweets = [Int: [(time: Int, id: Int)]]()
    private var follows = [Int: Set<Int>]()
    
    init() {}
    
    func postTweet(_ userId: Int, _ tweetId: Int) {
        timestamp += 1
        if tweets[userId] != nil {
            tweets[userId]?.append((time: timestamp, id: tweetId))
        } else {
            tweets[userId] = [(time: timestamp, id: tweetId)]
        }
    }
    
    func getNewsFeed(_ userId: Int) -> [Int] {
        var candidates = [(time: Int, id: Int)]()
        var followees = follows[userId] ?? Set<Int>()
        followees.insert(userId)
        for uid in followees {
            if let list = tweets[uid], !list.isEmpty {
                let start = max(0, list.count - 10)
                for i in stride(from: list.count - 1, through: start, by: -1) {
                    candidates.append(list[i])
                }
            }
        }
        candidates.sort { $0.time > $1.time }
        var result = [Int]()
        let limit = min(10, candidates.count)
        for i in 0..<limit {
            result.append(candidates[i].id)
        }
        return result
    }
    
    func follow(_ followerId: Int, _ followeeId: Int) {
        if followerId == followeeId { return }
        if follows[followerId] != nil {
            follows[followerId]?.insert(followeeId)
        } else {
            follows[followerId] = Set([followeeId])
        }
    }
    
    func unfollow(_ followerId: Int, _ followeeId: Int) {
        if followerId == followeeId { return }
        follows[followerId]?.remove(followeeId)
    }
}
```

## Kotlin

```kotlin
class Twitter() {
    private var timestamp = 0
    private val tweets = HashMap<Int, MutableList<Pair<Int, Int>>>()
    private val follows = HashMap<Int, MutableSet<Int>>()

    fun postTweet(userId: Int, tweetId: Int) {
        tweets.getOrPut(userId) { mutableListOf() }.add(Pair(tweetId, timestamp++))
    }

    fun getNewsFeed(userId: Int): List<Int> {
        val heap = java.util.PriorityQueue<Pair<Int, Int>>(compareBy { it.second })
        fun addRecent(uid: Int) {
            val list = tweets[uid] ?: return
            var count = 0
            var i = list.size - 1
            while (i >= 0 && count < 10) {
                heap.offer(list[i])
                if (heap.size > 10) heap.poll()
                count++
                i--
            }
        }

        addRecent(userId)
        follows[userId]?.forEach { fid ->
            if (fid != userId) addRecent(fid)
        }

        val result = mutableListOf<Int>()
        while (!heap.isEmpty()) {
            result.add(heap.poll().first)
        }
        result.reverse()
        return result
    }

    fun follow(followerId: Int, followeeId: Int) {
        if (followerId == followeeId) return
        follows.getOrPut(followerId) { mutableSetOf() }.add(followeeId)
    }

    fun unfollow(followerId: Int, followeeId: Int) {
        if (followerId == followeeId) return
        follows[followerId]?.remove(followeeId)
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * var obj = Twitter()
 * obj.postTweet(userId,tweetId)
 * var param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
```

## Dart

```dart
import 'dart:collection';

class Tweet {
  final int time;
  final int id;
  Tweet(this.time, this.id);
}

class _HeapNode {
  final int time;
  final int tweetId;
  final int userId;
  final int idx; // index in the user's tweet list
  _HeapNode(this.time, this.tweetId, this.userId, this.idx);
}

class Twitter {
  int _timestamp = 0;
  final Map<int, List<Tweet>> _userTweets = {};
  final Map<int, Set<int>> _followees = {};

  Twitter() {}

  void postTweet(int userId, int tweetId) {
    _timestamp++;
    _userTweets.putIfAbsent(userId, () => []).add(Tweet(_timestamp, tweetId));
  }

  List<int> getNewsFeed(int userId) {
    final Set<int> followSet = _followees[userId] ?? {};
    // Ensure the user's own tweets are considered
    final Set<int> usersToCheck = {...followSet, userId};

    final PriorityQueue<_HeapNode> heap = PriorityQueue<_HeapNode>(
        (a, b) => b.time.compareTo(a.time)); // max-heap by time

    for (final uid in usersToCheck) {
      final tweets = _userTweets[uid];
      if (tweets != null && tweets.isNotEmpty) {
        final int idx = tweets.length - 1;
        final Tweet lastTweet = tweets[idx];
        heap.add(_HeapNode(lastTweet.time, lastTweet.id, uid, idx));
      }
    }

    final List<int> result = [];
    while (result.length < 10 && heap.isNotEmpty) {
      final node = heap.removeFirst();
      result.add(node.tweetId);
      if (node.idx > 0) {
        final prevIdx = node.idx - 1;
        final Tweet prevTweet = _userTweets[node.userId]![prevIdx];
        heap.add(_HeapNode(prevTweet.time, prevTweet.id, node.userId, prevIdx));
      }
    }

    return result;
  }

  void follow(int followerId, int followeeId) {
    if (followerId == followeeId) return;
    _followees.putIfAbsent(followerId, () => <int>{}).add(followeeId);
  }

  void unfollow(int followerId, int followeeId) {
    if (followerId == followeeId) return;
    final set = _followees[followerId];
    set?.remove(followeeId);
    if (set != null && set.isEmpty) {
      _followees.remove(followerId);
    }
  }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = Twitter();
 * obj.postTweet(userId,tweetId);
 * List<int> param2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type Tweet struct {
	id   int
	time int
}

type Item struct {
	time    int
	tweetId int
	userId  int
	idx     int // index in the user's tweet slice
}

// MaxHeap implements a max-heap based on tweet time.
type MaxHeap []Item

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	return h[i].time > h[j].time // larger time = higher priority
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// Twitter is the main struct.
type Twitter struct {
	timestamp  int
	userTweets map[int][]Tweet          // userId -> list of tweets (chronological)
	follows    map[int]map[int]struct{} // followerId -> set of followeeIds
}

/** Initialize your data structure here. */
func Constructor() Twitter {
	return Twitter{
		timestamp:  0,
		userTweets: make(map[int][]Tweet),
		follows:    make(map[int]map[int]struct{}),
	}
}

/** Compose a new tweet. */
func (this *Twitter) PostTweet(userId int, tweetId int) {
	this.userTweets[userId] = append(this.userTweets[userId], Tweet{id: tweetId, time: this.timestamp})
	this.timestamp++
}

/** Retrieve the 10 most recent tweet ids in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user herself.
Tweets must be ordered from most recent to least recent. */
func (this *Twitter) GetNewsFeed(userId int) []int {
	// collect all relevant users: self + followees
	users := make(map[int]struct{})
	if set, ok := this.follows[userId]; ok {
		for uid := range set {
			users[uid] = struct{}{}
		}
	}
	users[userId] = struct{}{}

	h := &MaxHeap{}
	heap.Init(h)

	// push the most recent tweet of each user into heap
	for uid := range users {
		tweets := this.userTweets[uid]
		if len(tweets) == 0 {
			continue
		}
		idx := len(tweets) - 1
		t := tweets[idx]
		heap.Push(h, Item{time: t.time, tweetId: t.id, userId: uid, idx: idx})
	}

	result := []int{}
	for h.Len() > 0 && len(result) < 10 {
		it := heap.Pop(h).(Item)
		result = append(result, it.tweetId)

		if it.idx > 0 {
			newIdx := it.idx - 1
			t := this.userTweets[it.userId][newIdx]
			heap.Push(h, Item{time: t.time, tweetId: t.id, userId: it.userId, idx: newIdx})
		}
	}
	return result
}

/** Follower follows a followee. */
func (this *Twitter) Follow(followerId int, followeeId int) {
	if followerId == followeeId {
		return
	}
	if _, ok := this.follows[followerId]; !ok {
		this.follows[followerId] = make(map[int]struct{})
	}
	this.follows[followerId][followeeId] = struct{}{}
}

/** Follower unfollows a followee. */
func (this *Twitter) Unfollow(followerId int, followeeId int) {
	if followerId == followeeId {
		return
	}
	if set, ok := this.follows[followerId]; ok {
		delete(set, followeeId)
	}
}
```

## Ruby

```ruby
require 'set'

class Twitter
  def initialize()
    @timestamp = 0
    @tweets = Hash.new { |h, k| h[k] = [] }          # user_id => array of [time, tweet_id]
    @followees = Hash.new { |h, k| h[k] = Set.new([k]) } # follower_id => set of followee_ids (includes self)
  end

=begin
    :type user_id: Integer
    :type tweet_id: Integer
    :rtype: Void
=end
  def post_tweet(user_id, tweet_id)
    @timestamp += 1
    @tweets[user_id] << [@timestamp, tweet_id]
  end

=begin
    :type user_id: Integer
    :rtype: Integer[]
=end
  def get_news_feed(user_id)
    follow_set = @followees[user_id] || Set.new([user_id])
    candidates = []

    follow_set.each do |fid|
      tweets = @tweets[fid]
      next if tweets.empty?
      # take up to last 10 tweets from this user
      limit = [10, tweets.size].min
      (1..limit).each do |i|
        candidates << tweets[-i]   # [-1] newest, [-2] second newest, etc.
      end
    end

    candidates.sort_by! { |t| -t[0] }  # sort descending by timestamp
    candidates.first(10).map { |t| t[1] }
  end

=begin
    :type follower_id: Integer
    :type followee_id: Integer
    :rtype: Void
=end
  def follow(follower_id, followee_id)
    return if follower_id == followee_id
    @followees[follower_id].add(followee_id)
  end

=begin
    :type follower_id: Integer
    :type followee_id: Integer
    :rtype: Void
=end
  def unfollow(follower_id, followee_id)
    return if follower_id == followee_id
    @followees[follower_id].delete(followee_id) if @followees.key?(follower_id)
  end
end
```

## Scala

```scala
import scala.collection.mutable.{Map, Set, ListBuffer, ArrayBuffer}

class Twitter() {

  private case class Tweet(time: Int, id: Int)

  private var timestamp: Int = 0
  private val userTweets: Map[Int, ListBuffer[Tweet]] = Map()
  private val followees: Map[Int, Set[Int]] = Map()

  def postTweet(userId: Int, tweetId: Int): Unit = {
    timestamp += 1
    val list = userTweets.getOrElseUpdate(userId, ListBuffer())
    list.prepend(Tweet(timestamp, tweetId))
  }

  def getNewsFeed(userId: Int): List[Int] = {
    val users = Set[Int]()
    followees.get(userId).foreach(users ++= _)
    users += userId

    val candidates = ArrayBuffer[Tweet]()
    for (uid <- users) {
      userTweets.get(uid).foreach { tweets =>
        var i = 0
        while (i < tweets.size && i < 10) {
          candidates += tweets(i)
          i += 1
        }
      }
    }

    candidates.sortInPlaceBy(t => -t.time)
    candidates.take(10).map(_.id).toList
  }

  def follow(followerId: Int, followeeId: Int): Unit = {
    if (followerId != followeeId) {
      val set = followees.getOrElseUpdate(followerId, Set())
      set += followeeId
    }
  }

  def unfollow(followerId: Int, followeeId: Int): Unit = {
    if (followerId != followeeId) {
      followees.get(followerId).foreach(_ -= followeeId)
    }
  }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * val obj = new Twitter()
 * obj.postTweet(userId,tweetId)
 * val param_2 = obj.getNewsFeed(userId)
 * obj.follow(followerId,followeeId)
 * obj.unfollow(followerId,followeeId)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::{BinaryHeap, HashMap, HashSet};

type Tweet = (i64, i32); // (timestamp, tweet_id)

#[derive(Eq)]
struct HeapItem {
    timestamp: i64,
    tweet_id: i32,
    user_id: i32,
    idx: usize,
}

impl Ord for HeapItem {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.timestamp.cmp(&other.timestamp)
            .then_with(|| self.tweet_id.cmp(&other.tweet_id))
    }
}
impl PartialOrd for HeapItem {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}
impl PartialEq for HeapItem {
    fn eq(&self, other: &Self) -> bool {
        self.timestamp == other.timestamp && self.tweet_id == other.tweet_id
    }
}

struct Twitter {
    time: RefCell<i64>,
    tweets: RefCell<HashMap<i32, Vec<Tweet>>>,
    follows: RefCell<HashMap<i32, HashSet<i32>>>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Twitter {
    fn new() -> Self {
        Twitter {
            time: RefCell::new(0),
            tweets: RefCell::new(HashMap::new()),
            follows: RefCell::new(HashMap::new()),
        }
    }

    fn post_tweet(&self, user_id: i32, tweet_id: i32) {
        let mut t = self.time.borrow_mut();
        *t += 1;
        let ts = *t;

        let mut tweets_map = self.tweets.borrow_mut();
        tweets_map
            .entry(user_id)
            .or_insert_with(Vec::new)
            .push((ts, tweet_id));
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<i32> {
        let follows_map = self.follows.borrow();
        let mut users = Vec::new();
        users.push(user_id);
        if let Some(set) = follows_map.get(&user_id) {
            for &uid in set.iter() {
                users.push(uid);
            }
        }

        let tweets_map = self.tweets.borrow();

        let mut heap = BinaryHeap::new();

        for uid in users {
            if let Some(vec) = tweets_map.get(&uid) {
                if !vec.is_empty() {
                    let idx = vec.len() - 1;
                    let (ts, tid) = vec[idx];
                    heap.push(HeapItem {
                        timestamp: ts,
                        tweet_id: tid,
                        user_id: uid,
                        idx,
                    });
                }
            }
        }

        let mut result = Vec::new();
        while result.len() < 10 {
            if let Some(item) = heap.pop() {
                result.push(item.tweet_id);
                if item.idx > 0 {
                    let new_idx = item.idx - 1;
                    let vec = tweets_map.get(&item.user_id).unwrap();
                    let (ts, tid) = vec[new_idx];
                    heap.push(HeapItem {
                        timestamp: ts,
                        tweet_id: tid,
                        user_id: item.user_id,
                        idx: new_idx,
                    });
                }
            } else {
                break;
            }
        }

        result
    }

    fn follow(&self, follower_id: i32, followee_id: i32) {
        if follower_id == followee_id {
            return;
        }
        let mut follows_map = self.follows.borrow_mut();
        follows_map
            .entry(follower_id)
            .or_insert_with(HashSet::new)
            .insert(followee_id);
    }

    fn unfollow(&self, follower_id: i32, followee_id: i32) {
        if follower_id == followee_id {
            return;
        }
        let mut follows_map = self.follows.borrow_mut();
        if let Some(set) = follows_map.get_mut(&follower_id) {
            set.remove(&followee_id);
        }
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * let obj = Twitter::new();
 * obj.post_tweet(userId, tweetId);
 * let ret_2: Vec<i32> = obj.get_news_feed(userId);
 * obj.follow(followerId, followeeId);
 * obj.unfollow(followerId, followeeId);
 */
```

## Racket

```racket
#lang racket
(require racket/set)
(require racket/list)

(define twitter%
  (class object%
    (super-new)

    ;; private data structures
    (define tweet-counter 0)                ; global timestamp
    (define tweets (make-hash))             ; user-id -> list of (list timestamp tweet-id)
    (define follows (make-hash))            ; follower-id -> set of followee ids

    ;; post-tweet : exact-integer? exact-integer? -> void?
    (define/public (post-tweet user-id tweet-id)
      (set! tweet-counter (+ tweet-counter 1))
      (define lst (hash-ref tweets user-id '()))
      (hash-set! tweets user-id (cons (list tweet-counter tweet-id) lst)))

    ;; get-news-feed : exact-integer? -> (listof exact-integer?)
    (define/public (get-news-feed user-id)
      (define followees
        (let ((s (hash-ref follows user-id (set))))
          (set-add s user-id))) ; include self
      (define all '())
      (for ([fid (in-set followees)])
        (define tl (hash-ref tweets fid '()))
        (set! all (append all tl)))
      (define sorted
        (sort all > #:key (lambda (pair) (first pair))))
      (map second (take sorted 10)))

    ;; follow : exact-integer? exact-integer? -> void?
    (define/public (follow follower-id followee-id)
      (when (not (= follower-id followee-id))
        (define s (hash-ref follows follower-id (set)))
        (hash-set! follows follower-id (set-add s followee-id))))

    ;; unfollow : exact-integer? exact-integer? -> void?
    (define/public (unfollow follower-id followee-id)
      (when (not (= follower-id followee-id))
        (define s (hash-ref follows follower-id (set)))
        (hash-set! follows follower-id (set-remove s followee-id))))
    )) ; close class and define
```

## Erlang

```erlang
-module(solution).
-export([twitter_init_/0,
         twitter_post_tweet/2,
         twitter_get_news_feed/1,
         twitter_follow/2,
         twitter_unfollow/2]).

-include_lib("kernel/include/logger.hrl").

%% Initialize ETS tables
-spec twitter_init_() -> any().
twitter_init_() ->
    case ets:info(tweets) of
        undefined -> ok;
        _ -> ets:delete(tweets)
    end,
    case ets:info(follows) of
        undefined -> ok;
        _ -> ets:delete(follows)
    end,
    ets:new(tweets, [named_table, public, set]),
    ets:new(follows, [named_table, public, set]),
    ok.

%% Post a tweet
-spec twitter_post_tweet(UserId :: integer(), TweetId :: integer()) -> any().
twitter_post_tweet(UserId, TweetId) ->
    Timestamp = erlang:unique_integer([monotonic, positive]),
    case ets:lookup(tweets, UserId) of
        [] -> ets:insert(tweets, {UserId, [{Timestamp, TweetId}]});
        [{UserId, List}] ->
            ets:insert(tweets, {UserId, [{Timestamp, TweetId} | List]})
    end,
    ensure_self_follow(UserId),
    ok.

%% Get news feed (most recent 10 tweet ids)
-spec twitter_get_news_feed(UserId :: integer()) -> [integer()].
twitter_get_news_feed(UserId) ->
    FollowSet = get_follow_set(UserId),
    TweetsLists =
        [lists:sublist(get_user_tweets(Followee), 10) || Followee <- gb_sets:to_list(FollowSet)],
    AllTweets = lists:flatten(TweetsLists),
    SortedDesc = lists:reverse(lists:keysort(1, AllTweets)),
    TopTen = lists:sublist(SortedDesc, 10),
    [TweetId || {_Ts, TweetId} <- TopTen].

%% Follow operation
-spec twitter_follow(FollowerId :: integer(), FolloweeId :: integer()) -> any().
twitter_follow(FollowerId, FolloweeId) ->
    ensure_self_follow(FollowerId),
    ensure_self_follow(FolloweeId),
    Set = case ets:lookup(follows, FollowerId) of
              [] -> gb_sets:new();
              [{_, S}] -> S
          end,
    NewSet = gb_sets:add_element(FolloweeId, Set),
    ets:insert(follows, {FollowerId, NewSet}),
    ok.

%% Unfollow operation
-spec twitter_unfollow(FollowerId :: integer(), FolloweeId :: integer()) -> any().
twitter_unfollow(FollowerId, FolloweeId) ->
    case FollowerId =:= FolloweeId of
        true -> ok; % cannot unfollow oneself
        false ->
            Set = case ets:lookup(follows, FollowerId) of
                      [] -> gb_sets:new();
                      [{_, S}] -> S
                  end,
            NewSet = gb_sets:del_element(FolloweeId, Set),
            ets:insert(follows, {FollowerId, NewSet}),
            ok
    end.

%% Helper to ensure a user follows themselves
ensure_self_follow(UserId) ->
    case ets:lookup(follows, UserId) of
        [] ->
            ets:insert(follows, {UserId, gb_sets:add_element(UserId, gb_sets:new())});
        [{_, Set}] ->
            case gb_sets:is_member(UserId, Set) of
                true -> ok;
                false ->
                    NewSet = gb_sets:add_element(UserId, Set),
                    ets:insert(follows, {UserId, NewSet})
            end
    end.

%% Retrieve the follow set for a user (includes self)
get_follow_set(UserId) ->
    case ets:lookup(follows, UserId) of
        [] -> gb_sets:add_element(UserId, gb_sets:new());
        [{_, Set}] -> Set
    end.

%% Get stored tweets list for a user (most recent first)
get_user_tweets(UserId) ->
    case ets:lookup(tweets, UserId) of
        [] -> [];
        [{_, List}] -> List
    end.
```

## Elixir

```elixir
defmodule Twitter do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil ->
        Agent.start_link(fn -> %{tweets: %{}, follows: %{}, timestamp: 0} end, name: __MODULE__)

      pid ->
        Agent.stop(pid)
        Agent.start_link(fn -> %{tweets: %{}, follows: %{}, timestamp: 0} end, name: __MODULE__)
    end

    :ok
  end

  @spec post_tweet(user_id :: integer, tweet_id :: integer) :: any
  def post_tweet(user_id, tweet_id) do
    Agent.update(__MODULE__, fn state ->
      ts = state.timestamp + 1

      tweets =
        Map.update(state.tweets, user_id, [{ts, tweet_id}], fn list ->
          [{ts, tweet_id} | list]
        end)

      %{state | tweets: tweets, timestamp: ts}
    end)

    :ok
  end

  @spec get_news_feed(user_id :: integer) :: [integer]
  def get_news_feed(user_id) do
    Agent.get(__MODULE__, fn state ->
      followees =
        state.follows
        |> Map.get(user_id, MapSet.new())
        |> MapSet.put(user_id)

      tweets =
        followees
        |> Enum.map(fn uid -> Map.get(state.tweets, uid, []) end)
        |> List.flatten()

      tweets
      |> Enum.sort_by(fn {ts, _} -> -ts end)
      |> Enum.take(10)
      |> Enum.map(fn {_ts, tid} -> tid end)
    end)
  end

  @spec follow(follower_id :: integer, followee_id :: integer) :: any
  def follow(follower_id, followee_id) do
    if follower_id == followee_id do
      :ok
    else
      Agent.update(__MODULE__, fn state ->
        follows =
          Map.update(state.follows, follower_id, MapSet.new([followee_id]), fn set ->
            MapSet.put(set, followee_id)
          end)

        %{state | follows: follows}
      end)
    end
  end

  @spec unfollow(follower_id :: integer, followee_id :: integer) :: any
  def unfollow(follower_id, followee_id) do
    Agent.update(__MODULE__, fn state ->
      case Map.get(state.follows, follower_id) do
        nil ->
          state

        set ->
          new_set = MapSet.delete(set, followee_id)

          follows =
            if MapSet.size(new_set) == 0 do
              Map.delete(state.follows, follower_id)
            else
              Map.put(state.follows, follower_id, new_set)
            end

          %{state | follows: follows}
      end
    end)
  end
end
```
