# 3433. Count Mentions Per User

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        struct Event{
            string type;
            int time;
            string data;
        };
        vector<Event> evs;
        evs.reserve(events.size());
        for (auto &e : events) {
            evs.push_back({e[0], stoi(e[1]), e[2]});
        }
        sort(evs.begin(), evs.end(), [](const Event& a, const Event& b){
            if (a.time != b.time) return a.time < b.time;
            int pa = (a.type == "MESSAGE") ? 1 : 0;
            int pb = (b.type == "MESSAGE") ? 1 : 0;
            return pa < pb; // status changes before messages
        });
        
        vector<int> mentions(numberOfUsers, 0);
        vector<bool> online(numberOfUsers, true);
        
        for (const auto& ev : evs) {
            if (ev.type == "OFFLINE") {
                int uid = stoi(ev.data);
                online[uid] = false;
            } else if (ev.type == "ONLINE") {
                int uid = stoi(ev.data);
                online[uid] = true;
            } else if (ev.type == "MESSAGE") {
                const string& content = ev.data;
                if (content == "ALL") {
                    for (int i = 0; i < numberOfUsers; ++i) mentions[i]++;
                } else {
                    bool hasIdMention = false;
                    string token;
                    stringstream ss(content);
                    while (ss >> token) {
                        if (token.rfind("id", 0) == 0 && token.size() > 2) {
                            int uid = stoi(token.substr(2));
                            if (uid >= 0 && uid < numberOfUsers && online[uid])
                                mentions[uid]++;
                            hasIdMention = true;
                        }
                    }
                    if (!hasIdMention) {
                        for (int i = 0; i < numberOfUsers; ++i)
                            if (online[i]) mentions[i]++;
                    }
                }
            }
        }
        return mentions;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        class Event {
            String type;
            int time;
            String data;
            Event(String t, int ti, String d) { type = t; time = ti; data = d; }
        }

        List<Event> evList = new ArrayList<>();
        for (List<String> e : events) {
            String type = e.get(0);
            int time = Integer.parseInt(e.get(1));
            String data = e.get(2);
            evList.add(new Event(type, time, data));
        }

        evList.sort((a, b) -> {
            if (a.time != b.time) return Integer.compare(a.time, b.time);
            // status changes before messages
            boolean aMsg = a.type.equals("MESSAGE");
            boolean bMsg = b.type.equals("MESSAGE");
            if (aMsg == bMsg) return 0;
            return aMsg ? 1 : -1;
        });

        boolean[] online = new boolean[numberOfUsers];
        Arrays.fill(online, true);
        int[] mentions = new int[numberOfUsers];

        for (Event ev : evList) {
            switch (ev.type) {
                case "OFFLINE":
                    int offId = Integer.parseInt(ev.data);
                    online[offId] = false;
                    break;
                case "ONLINE":
                    int onId = Integer.parseInt(ev.data);
                    online[onId] = true;
                    break;
                case "MESSAGE":
                    String msg = ev.data;
                    if (msg.equals("ALL")) {
                        for (int i = 0; i < numberOfUsers; i++) mentions[i]++;
                    } else {
                        String[] parts = msg.split("\\s+");
                        for (String part : parts) {
                            if (part.startsWith("id")) {
                                try {
                                    int uid = Integer.parseInt(part.substring(2));
                                    if (uid >= 0 && uid < numberOfUsers && online[uid]) {
                                        mentions[uid]++;
                                    }
                                } catch (NumberFormatException ignored) {}
                            }
                        }
                    }
                    break;
                default:
                    // ignore unknown types
            }
        }

        return mentions;
    }
}
```

## Python

```python
class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        # sort by timestamp, with status changes before messages at same time
        def sort_key(e):
            ts = int(e[1])
            priority = 0 if e[0] != "MESSAGE" else 1
            return (ts, priority)
        events.sort(key=sort_key)

        online = set(range(numberOfUsers))
        mentions = [0] * numberOfUsers

        for typ, _, data in events:
            if typ == "OFFLINE":
                uid = int(data)
                online.discard(uid)
            elif typ == "ONLINE":
                uid = int(data)
                online.add(uid)
            else:  # MESSAGE
                tokens = data.split()
                if len(tokens) == 1 and tokens[0] == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif any(tok.startswith("id") for tok in tokens):
                    for tok in tokens:
                        if tok.startswith("id"):
                            uid = int(tok[2:])
                            mentions[uid] += 1
                else:
                    for uid in online:
                        mentions[uid] += 1

        return mentions
```

## Python3

```python
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Prepare events sorted by timestamp, with status changes before messages at same time
        processed = []
        for idx, ev in enumerate(events):
            typ, ts_str, data = ev
            ts = int(ts_str)
            priority = 0 if typ != "MESSAGE" else 1   # status change first
            processed.append((ts, priority, idx, typ, data))
        processed.sort()
        
        online = set(range(numberOfUsers))
        mentions = [0] * numberOfUsers
        
        for _, _, _, typ, data in processed:
            if typ == "OFFLINE":
                uid = int(data)
                online.discard(uid)
            elif typ == "ONLINE":
                uid = int(data)
                online.add(uid)
            else:  # MESSAGE
                tokens = data.split()
                for token in tokens:
                    if token == "ALL":
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                    elif token.startswith("id"):
                        uid = int(token[2:])
                        mentions[uid] += 1
                    else:
                        for uid in online:
                            mentions[uid] += 1
        return mentions
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countMentions(int numberOfUsers, char*** events, int eventsSize, int* eventsColSize, int* returnSize) {
    // Helper struct for sorting
    typedef struct {
        int idx;
        int timestamp;
        bool isMessage;
    } EventInfo;

    EventInfo *info = (EventInfo*)malloc(eventsSize * sizeof(EventInfo));
    for (int i = 0; i < eventsSize; ++i) {
        info[i].idx = i;
        info[i].timestamp = atoi(events[i][1]);
        info[i].isMessage = strcmp(events[i][0], "MESSAGE") == 0;
    }

    int cmp(const void *a, const void *b) {
        const EventInfo *ea = (const EventInfo *)a;
        const EventInfo *eb = (const EventInfo *)b;
        if (ea->timestamp != eb->timestamp)
            return ea->timestamp - eb->timestamp;
        // status events before message events at same timestamp
        if (ea->isMessage == eb->isMessage) return 0;
        return ea->isMessage ? 1 : -1;
    }

    qsort(info, eventsSize, sizeof(EventInfo), cmp);

    int *mentions = (int*)calloc(numberOfUsers, sizeof(int));
    bool *online = (bool*)malloc(numberOfUsers * sizeof(bool));
    for (int i = 0; i < numberOfUsers; ++i) online[i] = true;

    for (int k = 0; k < eventsSize; ++k) {
        int i = info[k].idx;
        char *typeStr = events[i][0];
        if (strcmp(typeStr, "MESSAGE") == 0) {
            char *content = events[i][2];
            if (strcmp(content, "ALL") == 0) {
                for (int u = 0; u < numberOfUsers; ++u)
                    mentions[u]++;
            } else {
                // split content
                char *copy = strdup(content);
                char *token = strtok(copy, " ");
                bool anyId = false;
                while (token) {
                    if (strncmp(token, "id", 2) == 0) {
                        int uid = atoi(token + 2);
                        if (uid >= 0 && uid < numberOfUsers && online[uid])
                            mentions[uid]++;
                        anyId = true;
                    }
                    token = strtok(NULL, " ");
                }
                free(copy);
                if (!anyId) {
                    for (int u = 0; u < numberOfUsers; ++u)
                        if (online[u]) mentions[u]++;
                }
            }
        } else { // OFFLINE or ONLINE
            int uid = atoi(events[i][2]);
            if (strcmp(typeStr, "OFFLINE") == 0)
                online[uid] = false;
            else
                online[uid] = true; // treat any non‑MESSAGE as ONLINE
        }
    }

    free(info);
    free(online);
    *returnSize = numberOfUsers;
    return mentions;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CountMentions(int numberOfUsers, IList<IList<string>> events) {
        var sorted = new List<(int time, int priority, string type, string data)>();
        foreach (var ev in events) {
            string type = ev[0];
            int t = int.Parse(ev[1]);
            string data = ev[2];
            int pri = type == "MESSAGE" ? 1 : 0; // status changes before messages at same timestamp
            sorted.Add((t, pri, type, data));
        }
        sorted.Sort((a, b) => {
            int cmp = a.time.CompareTo(b.time);
            if (cmp != 0) return cmp;
            return a.priority.CompareTo(b.priority);
        });

        bool[] online = new bool[numberOfUsers];
        for (int i = 0; i < numberOfUsers; i++) online[i] = true;

        int[] mentions = new int[numberOfUsers];

        foreach (var e in sorted) {
            if (e.type == "OFFLINE") {
                int uid = int.Parse(e.data);
                online[uid] = false;
            } else if (e.type == "ONLINE") {
                int uid = int.Parse(e.data);
                online[uid] = true;
            } else if (e.type == "MESSAGE") {
                string content = e.data;
                if (content == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) mentions[i]++;
                } else {
                    var parts = content.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                    foreach (var part in parts) {
                        if (part.StartsWith("id")) {
                            int uid = int.Parse(part.Substring(2));
                            if (uid >= 0 && uid < numberOfUsers && online[uid]) {
                                mentions[uid]++;
                            }
                        }
                    }
                }
            }
        }

        return mentions;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numberOfUsers
 * @param {string[][]} events
 * @return {number[]}
 */
var countMentions = function(numberOfUsers, events) {
    // Parse and sort events by timestamp.
    const parsed = events.map(e => ({
        type: e[0],
        time: Number(e[1]),
        data: e[2]
    }));
    parsed.sort((a, b) => {
        if (a.time !== b.time) return a.time - b.time;
        // status changes before messages at same timestamp
        const order = (type) => type === "MESSAGE" ? 1 : 0;
        return order(a.type) - order(b.type);
    });

    const online = new Array(numberOfUsers).fill(true);
    const mentions = new Array(numberOfUsers).fill(0);

    for (const ev of parsed) {
        if (ev.type === "OFFLINE") {
            const id = Number(ev.data);
            online[id] = false;
        } else if (ev.type === "ONLINE") {
            const id = Number(ev.data);
            online[id] = true;
        } else if (ev.type === "MESSAGE") {
            const txt = ev.data;
            if (txt === "ALL") {
                for (let i = 0; i < numberOfUsers; ++i) {
                    mentions[i] += 1;
                }
            } else {
                const parts = txt.split(' ');
                for (const part of parts) {
                    // expect format id<number>
                    if (!part.startsWith("id")) continue;
                    const uid = Number(part.slice(2));
                    if (online[uid]) {
                        mentions[uid] += 1;
                    }
                }
            }
        }
    }

    return mentions;
};
```

## Typescript

```typescript
function countMentions(numberOfUsers: number, events: string[][]): number[] {
    const mentions = new Array(numberOfUsers).fill(0);
    const online = new Array(numberOfUsers).fill(true); // all users start online

    const sorted = events.slice().sort((a, b) => {
        const tA = Number(a[1]);
        const tB = Number(b[1]);
        if (tA !== tB) return tA - tB;
        const rankA = a[0] === "MESSAGE" ? 1 : 0; // status changes before messages
        const rankB = b[0] === "MESSAGE" ? 1 : 0;
        return rankA - rankB;
    });

    for (const ev of sorted) {
        const type = ev[0];
        if (type === "OFFLINE") {
            const uid = Number(ev[2]);
            online[uid] = false;
        } else if (type === "ONLINE") {
            const uid = Number(ev[2]);
            online[uid] = true;
        } else { // MESSAGE
            const content = ev[2];
            if (content === "ALL") {
                for (let i = 0; i < numberOfUsers; ++i) mentions[i]++;
            } else {
                const parts = content.split(' ');
                for (const part of parts) {
                    if (!part) continue;
                    // expected format: id<number>
                    const uid = Number(part.slice(2));
                    if (online[uid]) mentions[uid]++;
                }
            }
        }
    }

    return mentions;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numberOfUsers
     * @param String[][] $events
     * @return Integer[]
     */
    function countMentions($numberOfUsers, $events) {
        // Sort events by timestamp; status changes before messages at same time
        usort($events, function($a, $b) {
            $t1 = intval($a[1]);
            $t2 = intval($b[1]);
            if ($t1 === $t2) {
                $p1 = ($a[0] === 'MESSAGE') ? 1 : 0;
                $p2 = ($b[0] === 'MESSAGE') ? 1 : 0;
                return $p1 <=> $p2; // non‑message first
            }
            return $t1 <=> $t2;
        });

        // online status: true means online
        $online = array_fill(0, $numberOfUsers, true);
        // mentions count
        $mentions = array_fill(0, $numberOfUsers, 0);

        foreach ($events as $ev) {
            $type = $ev[0];
            $content = $ev[2];

            if ($type === 'OFFLINE') {
                $uid = intval($content);
                $online[$uid] = false;
            } elseif ($type === 'ONLINE') { // handle possible ONLINE events
                $uid = intval($content);
                $online[$uid] = true;
            } elseif ($type === 'MESSAGE') {
                $tokens = preg_split('/\s+/', trim($content));
                $hasId = false;

                foreach ($tokens as $tok) {
                    if (strlen($tok) > 2 && substr($tok, 0, 2) === 'id' && ctype_digit(substr($tok, 2))) {
                        $uid = intval(substr($tok, 2));
                        $hasId = true;
                        if ($online[$uid]) {
                            $mentions[$uid] += 1;
                        }
                    }
                }

                if (!$hasId) {
                    // No explicit ids in the message
                    if (trim($content) === 'ALL') {
                        for ($i = 0; $i < $numberOfUsers; ++$i) {
                            $mentions[$i] += 1;
                        }
                    } else {
                        // Mention all currently online users
                        for ($i = 0; $i < $numberOfUsers; ++$i) {
                            if ($online[$i]) {
                                $mentions[$i] += 1;
                            }
                        }
                    }
                }
            }
        }

        return $mentions;
    }
}
```

## Swift

```swift
class Solution {
    func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int] {
        var parsed: [(type: String, time: Int, data: String)] = []
        for e in events {
            let type = e[0]
            let time = Int(e[1])!
            let data = e[2]
            parsed.append((type, time, data))
        }
        parsed.sort { $0.time < $1.time }
        
        var online = Array(repeating: true, count: numberOfUsers)
        var mentions = Array(repeating: 0, count: numberOfUsers)
        
        var idx = 0
        while idx < parsed.count {
            let curTime = parsed[idx].time
            var statusEvents: [(String, String)] = []
            var messageContents: [String] = []
            
            var j = idx
            while j < parsed.count && parsed[j].time == curTime {
                let ev = parsed[j]
                if ev.type == "MESSAGE" {
                    messageContents.append(ev.data)
                } else { // OFFLINE or ONLINE
                    statusEvents.append((ev.type, ev.data))
                }
                j += 1
            }
            
            // Apply status changes first
            for (type, data) in statusEvents {
                if type == "OFFLINE" {
                    let uid = Int(data)!
                    online[uid] = false
                } else if type == "ONLINE" {
                    let uid = Int(data)!
                    online[uid] = true
                }
            }
            
            // Process messages
            for content in messageContents {
                if content == "ALL" {
                    for u in 0..<numberOfUsers {
                        mentions[u] += 1
                    }
                } else {
                    let parts = content.split(separator: " ")
                    var hasId = false
                    for part in parts {
                        if part.hasPrefix("id") {
                            let numStr = part.dropFirst(2)
                            if let uid = Int(numStr) {
                                mentions[uid] += 1
                                hasId = true
                            }
                        }
                    }
                    if !hasId {
                        for u in 0..<numberOfUsers where online[u] {
                            mentions[u] += 1
                        }
                    }
                }
            }
            
            idx = j
        }
        
        return mentions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countMentions(numberOfUsers: Int, events: List<List<String>>): IntArray {
        data class Event(val type: String, val time: Int, val data: String)

        // Parse and sort events by timestamp
        val sorted = events.map { Event(it[0], it[1].toInt(), it[2]) }
            .sortedBy { it.time }

        val online = BooleanArray(numberOfUsers) { true }   // all users start online
        val mentions = IntArray(numberOfUsers)

        var idx = 0
        while (idx < sorted.size) {
            val curTime = sorted[idx].time

            // Process status changes first (any non-MESSAGE event)
            var j = idx
            while (j < sorted.size && sorted[j].time == curTime && sorted[j].type != "MESSAGE") {
                when (sorted[j].type) {
                    "OFFLINE" -> {
                        val uid = sorted[j].data.toInt()
                        online[uid] = false
                    }
                    "ONLINE" -> {
                        val uid = sorted[j].data.toInt()
                        online[uid] = true
                    }
                }
                j++
            }

            // Process MESSAGE events at the same timestamp
            var k = j
            while (k < sorted.size && sorted[k].time == curTime && sorted[k].type == "MESSAGE") {
                val content = sorted[k].data
                val tokens = content.split(' ')
                if ("ALL" in tokens) {
                    // Mention every user regardless of status
                    for (u in 0 until numberOfUsers) mentions[u]++
                } else {
                    var hasId = false
                    for (tok in tokens) {
                        if (tok.startsWith("id")) {
                            hasId = true
                            val uid = tok.substring(2).toInt()
                            if (online[uid]) mentions[uid]++
                        }
                    }
                    if (!hasId) {
                        // Generic message: mention all currently online users
                        for (u in 0 until numberOfUsers) {
                            if (online[u]) mentions[u]++
                        }
                    }
                }
                k++
            }

            idx = k
        }

        return mentions
    }
}
```

## Dart

```dart
class Solution {
  List<int> countMentions(int numberOfUsers, List<List<String>> events) {
    // Sort by timestamp, and ensure status changes come before messages at same time
    events.sort((a, b) {
      int t1 = int.parse(a[1]);
      int t2 = int.parse(b[1]);
      if (t1 != t2) return t1.compareTo(t2);
      bool isMsg1 = a[0] == "MESSAGE";
      bool isMsg2 = b[0] == "MESSAGE";
      if (isMsg1 == isMsg2) return 0;
      // non-MESSAGE first
      return isMsg1 ? 1 : -1;
    });

    List<bool> online = List.filled(numberOfUsers, true);
    List<int> mentions = List.filled(numberOfUsers, 0);

    for (var ev in events) {
      String type = ev[0];
      if (type == "OFFLINE") {
        int uid = int.parse(ev[2]);
        online[uid] = false;
      } else if (type == "ONLINE") {
        int uid = int.parse(ev[2]);
        online[uid] = true;
      } else if (type == "MESSAGE") {
        String content = ev[2];
        if (content == "ALL") {
          for (int i = 0; i < numberOfUsers; ++i) {
            mentions[i]++;
          }
        } else {
          List<String> tokens = content.split(' ');
          bool anyId = false;
          for (String token in tokens) {
            if (token.startsWith("id")) {
              String numStr = token.substring(2);
              if (numStr.isNotEmpty) {
                int uid = int.parse(numStr);
                mentions[uid]++;
                anyId = true;
              }
            }
          }
          if (!anyId) {
            for (int i = 0; i < numberOfUsers; ++i) {
              if (online[i]) mentions[i]++;
            }
          }
        }
      }
    }

    return mentions;
  }
}
```

## Golang

```go
func countMentions(numberOfUsers int, events [][]string) []int {
	type ev struct {
		typ  string
		ts   int
		data string
	}
	evs := make([]ev, len(events))
	for i, e := range events {
		// e[0]=type, e[1]=timestamp, e[2]=data
		ts := 0
		for _, c := range e[1] {
			ts = ts*10 + int(c-'0')
		}
		evs[i] = ev{typ: e[0], ts: ts, data: e[2]}
	}

	// sort by timestamp, and for same timestamp process non‑MESSAGE before MESSAGE
	sort.Slice(evs, func(i, j int) bool {
		if evs[i].ts != evs[j].ts {
			return evs[i].ts < evs[j].ts
		}
		if evs[i].typ == "MESSAGE" && evs[j].typ != "MESSAGE" {
			return false
		}
		if evs[i].typ != "MESSAGE" && evs[j].typ == "MESSAGE" {
			return true
		}
		return i < j
	})

	online := make([]bool, numberOfUsers)
	for i := range online {
		online[i] = true
	}
	mentions := make([]int, numberOfUsers)

	for _, e := range evs {
		switch e.typ {
		case "OFFLINE":
			id := 0
			for _, c := range e.data {
				id = id*10 + int(c-'0')
			}
			if id >= 0 && id < numberOfUsers {
				online[id] = false
			}
		case "ONLINE":
			id := 0
			for _, c := range e.data {
				id = id*10 + int(c-'0')
			}
			if id >= 0 && id < numberOfUsers {
				online[id] = true
			}
		case "MESSAGE":
			content := e.data
			if content == "ALL" {
				for i := 0; i < numberOfUsers; i++ {
					mentions[i]++
				}
			} else if strings.HasPrefix(content, "id") {
				fields := strings.Fields(content)
				for _, token := range fields {
					if strings.HasPrefix(token, "id") {
						idStr := token[2:]
						id := 0
						for _, c := range idStr {
							id = id*10 + int(c-'0')
						}
						if id >= 0 && id < numberOfUsers && online[id] {
							mentions[id]++
						}
					}
				}
			} else { // generic message mentions all currently online users
				for i := 0; i < numberOfUsers; i++ {
					if online[i] {
						mentions[i]++
					}
				}
			}
		}
	}
	return mentions
}

import (
	"sort"
	"strings"
)
```

## Ruby

```ruby
def count_mentions(number_of_users, events)
  sorted = events.map { |type, ts_str, data| [type, ts_str.to_i, data] }
                 .sort_by { |type, ts, _| [ts, type == "MESSAGE" ? 1 : 0] }

  online = Array.new(number_of_users, true)
  mentions = Array.new(number_of_users, 0)

  sorted.each do |type, _, data|
    case type
    when "OFFLINE"
      uid = data.to_i
      online[uid] = false
    when "ONLINE"
      uid = data.to_i
      online[uid] = true
    when "MESSAGE"
      if data == "ALL"
        (0...number_of_users).each { |i| mentions[i] += 1 }
      elsif data == "HERE"
        (0...number_of_users).each { |i| mentions[i] += 1 if online[i] }
      else
        data.split(' ').each do |token|
          next unless token.start_with?('id')
          uid = token[2..].to_i
          mentions[uid] += 1
        end
      end
    end
  end

  mentions
end
```

## Scala

```scala
object Solution {
    def countMentions(numberOfUsers: Int, events: List[List[String]]): Array[Int] = {
        case class Ev(tpe: String, ts: Int, data: String)

        val evs = events.map(e => Ev(e(0), e(1).toInt, e(2)))
        val sorted = evs.sortWith { (a, b) =>
            if (a.ts != b.ts) a.ts < b.ts
            else {
                val orderA = if (a.tpe == "MESSAGE") 1 else 0
                val orderB = if (b.tpe == "MESSAGE") 1 else 0
                orderA < orderB
            }
        }

        val online = Array.fill(numberOfUsers)(true)
        val mentions = Array.fill(numberOfUsers)(0)

        for (ev <- sorted) {
            ev.tpe match {
                case "OFFLINE" =>
                    val id = ev.data.toInt
                    online(id) = false
                case "ONLINE" =>
                    val id = ev.data.toInt
                    online(id) = true
                case "MESSAGE" =>
                    if (ev.data == "ALL") {
                        var i = 0
                        while (i < numberOfUsers) {
                            mentions(i) += 1
                            i += 1
                        }
                    } else {
                        val parts = ev.data.split(" ")
                        var hasId = false
                        for (p <- parts) {
                            if (p.startsWith("id")) {
                                hasId = true
                                val idStr = p.substring(2)
                                if (idStr.nonEmpty) {
                                    val id = idStr.toInt
                                    if (online(id)) mentions(id) += 1
                                }
                            }
                        }
                        if (!hasId) {
                            var i = 0
                            while (i < numberOfUsers) {
                                if (online(i)) mentions(i) += 1
                                i += 1
                            }
                        }
                    }
                case _ => // ignore unknown types
            }
        }

        mentions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_mentions(number_of_users: i32, events: Vec<Vec<String>>) -> Vec<i32> {
        let n = number_of_users as usize;
        // Build a list of (timestamp, order, type, data)
        let mut evs: Vec<(i32, i32, String, String)> = events
            .into_iter()
            .map(|e| {
                let typ = e[0].clone();
                let ts: i32 = e[1].parse().unwrap();
                // order: status changes before messages at same timestamp
                let order = if typ == "MESSAGE" { 1 } else { 0 };
                (ts, order, typ, e[2].clone())
            })
            .collect();

        evs.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });

        let mut online = vec![true; n];
        let mut mentions = vec![0i32; n];

        for (_, _, typ, data) in evs {
            match typ.as_str() {
                "OFFLINE" => {
                    let id: usize = data.parse().unwrap();
                    online[id] = false;
                }
                "ONLINE" => {
                    let id: usize = data.parse().unwrap();
                    online[id] = true;
                }
                "MESSAGE" => {
                    if data == "ALL" {
                        for i in 0..n {
                            mentions[i] += 1;
                        }
                    } else {
                        // Count generic tokens (not starting with "id")
                        let mut generic_cnt = 0i32;
                        for token in data.split_whitespace() {
                            if token.starts_with("id") && token.len() > 2 {
                                // id mention
                                if let Ok(id) = token[2..].parse::<usize>() {
                                    if id < n && online[id] {
                                        mentions[id] += 1;
                                    }
                                }
                            } else {
                                generic_cnt += 1;
                            }
                        }
                        if generic_cnt > 0 {
                            for i in 0..n {
                                if online[i] {
                                    mentions[i] += generic_cnt;
                                }
                            }
                        }
                    }
                }
                _ => {}
            }
        }

        mentions
    }
}
```

## Racket

```racket
(define/contract (count-mentions numberOfUsers events)
  (-> exact-integer? (listof (listof string?)) (listof exact-integer?))
  (let* ((sorted-events
          (sort events
                (lambda (e1 e2)
                  (let* ((t1 (string->number (list-ref e1 1)))
                         (t2 (string->number (list-ref e2 1)))
                         (type1 (list-ref e1 0))
                         (type2 (list-ref e2 0))
                         (rank1 (if (string=? type1 "MESSAGE") 1 0))
                         (rank2 (if (string=? type2 "MESSAGE") 1 0)))
                    (cond [(< t1 t2) #t]
                          [(> t1 t2) #f]
                          [else (< rank1 rank2)])))))
         (mentions (make-vector numberOfUsers 0))
         (online   (make-vector numberOfUsers #t)))
    (for ([ev sorted-events])
      (define type (list-ref ev 0))
      (define data (list-ref ev 2))
      (cond [(string=? type "OFFLINE")
             (define idx (string->number data))
             (vector-set! online idx #f)]
            [(string=? type "ONLINE")
             (define idx (string->number data))
             (vector-set! online idx #t)]
            [(string=? type "MESSAGE")
             (if (string=? data "ALL")
                 (for ([i (in-range numberOfUsers)])
                   (vector-set! mentions i (+ 1 (vector-ref mentions i))))
                 (let ((tokens (string-split data)))
                   (for ([tok tokens])
                     (define idx (string->number (substring tok 2)))
                     (when (vector-ref online idx)
                       (vector-set! mentions idx (+ 1 (vector-ref mentions idx)))))))]))
    (let loop ((i 0) (acc '()))
      (if (= i numberOfUsers)
          (reverse acc)
          (loop (+ i 1) (cons (vector-ref mentions i) acc))))))
```

## Erlang

```erlang
-spec count_mentions(NumberOfUsers :: integer(), Events :: [[unicode:unicode_binary()]]) -> [integer()].
count_mentions(NumberOfUsers, Events) ->
    %% Build list of {Timestamp, Priority, Index, Type, Data}
    EventTuples = lists:foldl(
        fun(Event, Acc) ->
            [TypeBin, TimeBin, DataBin] = Event,
            Timestamp = erlang:binary_to_integer(TimeBin),
            Priority = case TypeBin of
                <<"MESSAGE">> -> 1;
                _ -> 0   %% OFFLINE / ONLINE etc.
            end,
            Index = length(Acc), % preserve original order for stability if needed
            [{Timestamp, Priority, Index, TypeBin, DataBin} | Acc]
        end,
        [],
        Events),
    SortedEvents = lists:sort(
        fun({Ta, Pa, _, _, _}, {Tb, Pb, _, _, _}) ->
            case Ta <=> Tb of
                lt -> true;
                gt -> false;
                eq -> Pa =< Pb
            end
        end,
        EventTuples),

    %% Initialize online map (all true) and counts map (all 0)
    OnlineInit = maps:from_list(
        [{I, true} || I <- lists:seq(0, NumberOfUsers - 1)]),
    CountsInit = maps:from_list(
        [{I, 0} || I <- lists:seq(0, NumberOfUsers - 1)]),

    {FinalCountsMap, _FinalOnline} =
        process_events(SortedEvents, OnlineInit, CountsInit),

    %% Produce result list ordered by user id
    [maps:get(I, FinalCountsMap) || I <- lists:seq(0, NumberOfUsers - 1)].

process_events([], OnlineMap, CountsMap) ->
    {CountsMap, OnlineMap};
process_events([{_, _, _, TypeBin, DataBin} | Rest], OnlineMap, CountsMap) ->
    case TypeBin of
        <<"OFFLINE">> ->
            UserId = erlang:binary_to_integer(DataBin),
            NewOnline = maps:put(UserId, false, OnlineMap),
            process_events(Rest, NewOnline, CountsMap);
        <<"ONLINE">> ->
            UserId = erlang:binary_to_integer(DataBin),
            NewOnline = maps:put(UserId, true, OnlineMap),
            process_events(Rest, NewOnline, CountsMap);
        <<"MESSAGE">> ->
            Tokens = binary:split(DataBin, <<" ">>, [global]),
            {NewCounts, NewOnline} = handle_message(Tokens, OnlineMap, CountsMap),
            process_events(Rest, NewOnline, NewCounts)
    end.

handle_message([], OnlineMap, CountsMap) ->
    {CountsMap, OnlineMap};
handle_message([Token | Rest], OnlineMap, CountsMap) ->
    case Token of
        <<"ALL">> ->
            UpdatedCounts = increment_all(CountsMap),
            handle_message(Rest, OnlineMap, UpdatedCounts);
        <<"HERE">> ->
            UpdatedCounts = increment_here(OnlineMap, CountsMap),
            handle_message(Rest, OnlineMap, UpdatedCounts);
        << "id", RestId/binary >> ->
            UserId = erlang:binary_to_integer(RestId),
            UpdatedCounts = maps:update_with(UserId,
                fun(V) -> V + 1 end,
                1,
                CountsMap),
            handle_message(Rest, OnlineMap, UpdatedCounts);
        _Other ->
            %% Unknown token, ignore
            handle_message(Rest, OnlineMap, CountsMap)
    end.

increment_all(CountsMap) ->
    maps:fold(
        fun(UserId, Count, Acc) ->
            maps:put(UserId, Count + 1, Acc)
        end,
        #{},
        CountsMap).

increment_here(OnlineMap, CountsMap) ->
    maps:fold(
        fun(UserId, IsOnline, AccCounts) ->
            case IsOnline of
                true ->
                    NewCount = maps:get(UserId, AccCounts) + 1,
                    maps:put(UserId, NewCount, AccCounts);
                false ->
                    AccCounts
            end
        end,
        CountsMap,
        OnlineMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_mentions(number_of_users :: integer, events :: [[String.t]]) :: [integer]
  def count_mentions(number_of_users, events) do
    # Sort events by timestamp, status changes before messages at same time
    sorted_events =
      Enum.sort_by(events, fn [type, ts_str, _data] ->
        {String.to_integer(ts_str), if type == "MESSAGE", do: 1, else: 0}
      end)

    initial_online = MapSet.new(0..number_of_users - 1)
    initial_mentions = for _ <- 0..number_of_users - 1, do: 0

    {_final_online, final_mentions} =
      Enum.reduce(sorted_events, {initial_online, initial_mentions}, fn [type, _ts_str, data],
                                                                      {online_set,
                                                                       mentions_list} ->
        case type do
          "OFFLINE" ->
            user = String.to_integer(data)
            {MapSet.delete(online_set, user), mentions_list}

          "ONLINE" ->
            user = String.to_integer(data)
            {MapSet.put(online_set, user), mentions_list}

          "MESSAGE" ->
            tokens = String.split(data, " ", trim: true)

            new_mentions =
              Enum.reduce(tokens, mentions_list, fn token, acc_mentions ->
                cond do
                  token == "ALL" ->
                    Enum.map(acc_mentions, &(&1 + 1))

                  String.starts_with?(token, "id") ->
                    uid = token |> String.slice(2..-1) |> String.to_integer()
                    List.update_at(acc_mentions, uid, &(&1 + 1))

                  true ->
                    # generic mention to currently online users
                    Enum.reduce(online_set, acc_mentions, fn uid, inner_acc ->
                      List.update_at(inner_acc, uid, &(&1 + 1))
                    end)
                end
              end)

            {online_set, new_mentions}
        end
      end)

    final_mentions
  end
end
```
