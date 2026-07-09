# 1333. Filter Restaurants by Vegan-Friendly, Price and Distance

## Cpp

```cpp
class Solution {
public:
    vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        vector<pair<int,int>> filtered; // {rating, id}
        for (const auto& r : restaurants) {
            int id = r[0];
            int rating = r[1];
            int vf = r[2];
            int price = r[3];
            int distance = r[4];
            if (veganFriendly && !vf) continue;
            if (price > maxPrice || distance > maxDistance) continue;
            filtered.emplace_back(rating, id);
        }
        sort(filtered.begin(), filtered.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            if (a.first != b.first) return a.first > b.first; // higher rating first
            return a.second > b.second; // higher id first
        });
        vector<int> ans;
        ans.reserve(filtered.size());
        for (auto& p : filtered) ans.push_back(p.second);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        List<int[]> filtered = new ArrayList<>();
        for (int[] r : restaurants) {
            if (veganFriendly == 1 && r[2] == 0) continue;
            if (r[3] > maxPrice) continue;
            if (r[4] > maxDistance) continue;
            filtered.add(r);
        }
        filtered.sort((a, b) -> {
            if (b[1] != a[1]) return Integer.compare(b[1], a[1]); // rating desc
            return Integer.compare(b[0], a[0]); // id desc
        });
        List<Integer> result = new ArrayList<>(filtered.size());
        for (int[] r : filtered) {
            result.add(r[0]);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        filtered = []
        for rid, rating, vf, price, dist in restaurants:
            if veganFriendly == 1 and vf != 1:
                continue
            if price > maxPrice or dist > maxDistance:
                continue
            filtered.append((rating, rid))
        filtered.sort(key=lambda x: (-x[0], -x[1]))
        return [rid for _, rid in filtered]
```

## Python3

```python
from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = [
            r for r in restaurants
            if (veganFriendly == 0 or r[2] == 1) and r[3] <= maxPrice and r[4] <= maxDistance
        ]
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        return [r[0] for r in filtered]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int id;
    int rating;
} Rest;

static int cmpRest(const void *a, const void *b) {
    const Rest *ra = (const Rest *)a;
    const Rest *rb = (const Rest *)b;
    if (ra->rating != rb->rating)
        return (rb->rating > ra->rating) - (rb->rating < ra->rating); // descending rating
    return (rb->id > ra->id) - (rb->id < ra->id);                     // descending id
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize,
                       int veganFriendly, int maxPrice, int maxDistance, int* returnSize) {
    Rest *tmp = (Rest *)malloc(sizeof(Rest) * restaurantsSize);
    int cnt = 0;

    for (int i = 0; i < restaurantsSize; ++i) {
        int id = restaurants[i][0];
        int rating = restaurants[i][1];
        int vegan = restaurants[i][2];
        int price = restaurants[i][3];
        int distance = restaurants[i][4];

        if ((veganFriendly == 0 || vegan == 1) && price <= maxPrice && distance <= maxDistance) {
            tmp[cnt].id = id;
            tmp[cnt].rating = rating;
            ++cnt;
        }
    }

    qsort(tmp, cnt, sizeof(Rest), cmpRest);

    int *result = (int *)malloc(sizeof(int) * cnt);
    for (int i = 0; i < cnt; ++i) {
        result[i] = tmp[i].id;
    }

    free(tmp);
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FilterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        var filtered = new List<(int rating, int id)>();
        foreach (var r in restaurants) {
            int id = r[0];
            int rating = r[1];
            int vf = r[2];
            int price = r[3];
            int distance = r[4];
            if ((veganFriendly == 0 || vf == 1) && price <= maxPrice && distance <= maxDistance) {
                filtered.Add((rating, id));
            }
        }
        filtered.Sort((a, b) => {
            if (a.rating != b.rating) return b.rating.CompareTo(a.rating);
            return b.id.CompareTo(a.id);
        });
        var result = new List<int>(filtered.Count);
        foreach (var item in filtered) {
            result.Add(item.id);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} restaurants
 * @param {number} veganFriendly
 * @param {number} maxPrice
 * @param {number} maxDistance
 * @return {number[]}
 */
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    const filtered = restaurants.filter(r => 
        (veganFriendly === 0 || r[2] === 1) &&
        r[3] <= maxPrice &&
        r[4] <= maxDistance
    );
    filtered.sort((a, b) => {
        if (b[1] !== a[1]) return b[1] - a[1]; // rating descending
        return b[0] - a[0]; // id descending
    });
    return filtered.map(r => r[0]);
};
```

## Typescript

```typescript
function filterRestaurants(restaurants: number[][], veganFriendly: number, maxPrice: number, maxDistance: number): number[] {
    const candidates: [number, number][] = [];
    for (const r of restaurants) {
        if (veganFriendly === 1 && r[2] !== 1) continue;
        if (r[3] > maxPrice || r[4] > maxDistance) continue;
        candidates.push([r[0], r[1]]);
    }
    candidates.sort((a, b) => {
        if (b[1] !== a[1]) return b[1] - a[1];
        return b[0] - a[0];
    });
    return candidates.map(pair => pair[0]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $restaurants
     * @param Integer $veganFriendly
     * @param Integer $maxPrice
     * @param Integer $maxDistance
     * @return Integer[]
     */
    function filterRestaurants($restaurants, $veganFriendly, $maxPrice, $maxDistance) {
        $filtered = [];
        foreach ($restaurants as $r) {
            // r: [id, rating, veganFriendly, price, distance]
            if ($veganFriendly == 1 && $r[2] != 1) {
                continue;
            }
            if ($r[3] > $maxPrice || $r[4] > $maxDistance) {
                continue;
            }
            $filtered[] = $r;
        }

        usort($filtered, function($a, $b) {
            // rating descending
            if ($a[1] != $b[1]) {
                return $b[1] <=> $a[1];
            }
            // id descending
            return $b[0] <=> $a[0];
        });

        $result = [];
        foreach ($filtered as $r) {
            $result[] = $r[0];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func filterRestaurants(_ restaurants: [[Int]], _ veganFriendly: Int, _ maxPrice: Int, _ maxDistance: Int) -> [Int] {
        var filtered = [(id: Int, rating: Int)]()
        for r in restaurants {
            let id = r[0]
            let rating = r[1]
            let vf = r[2]
            let price = r[3]
            let distance = r[4]
            
            if veganFriendly == 1 && vf != 1 { continue }
            if price > maxPrice || distance > maxDistance { continue }
            
            filtered.append((id, rating))
        }
        
        filtered.sort {
            if $0.rating != $1.rating {
                return $0.rating > $1.rating
            } else {
                return $0.id > $1.id
            }
        }
        
        return filtered.map { $0.id }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun filterRestaurants(restaurants: Array<IntArray>, veganFriendly: Int, maxPrice: Int, maxDistance: Int): List<Int> {
        val filtered = mutableListOf<IntArray>()
        for (r in restaurants) {
            if ((veganFriendly == 0 || r[2] == 1) && r[3] <= maxPrice && r[4] <= maxDistance) {
                filtered.add(r)
            }
        }
        filtered.sortWith { a, b ->
            when {
                a[1] != b[1] -> b[1] - a[1]
                else -> b[0] - a[0]
            }
        }
        return filtered.map { it[0] }
    }
}
```

## Dart

```dart
class Solution {
  List<int> filterRestaurants(List<List<int>> restaurants, int veganFriendly, int maxPrice, int maxDistance) {
    List<List<int>> filtered = [];
    for (var r in restaurants) {
      if ((veganFriendly == 0 || r[2] == 1) && r[3] <= maxPrice && r[4] <= maxDistance) {
        filtered.add(r);
      }
    }
    filtered.sort((a, b) {
      if (b[1] != a[1]) return b[1] - a[1]; // rating descending
      return b[0] - a[0]; // id descending
    });
    List<int> result = [];
    for (var r in filtered) {
      result.add(r[0]);
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	type pair struct {
		id     int
		rating int
	}
	var filtered []pair
	for _, r := range restaurants {
		if veganFriendly == 1 && r[2] != 1 {
			continue
		}
		if r[3] > maxPrice || r[4] > maxDistance {
			continue
		}
		filtered = append(filtered, pair{id: r[0], rating: r[1]})
	}
	sort.Slice(filtered, func(i, j int) bool {
		if filtered[i].rating != filtered[j].rating {
			return filtered[i].rating > filtered[j].rating
		}
		return filtered[i].id > filtered[j].id
	})
	res := make([]int, len(filtered))
	for i, p := range filtered {
		res[i] = p.id
	}
	return res
}
```

## Ruby

```ruby
def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance)
  filtered = restaurants.select do |id, rating, vf, price, distance|
    (vegan_friendly == 0 || vf == 1) && price <= max_price && distance <= max_distance
  end
  filtered.sort_by { |id, rating, _, _, _| [-rating, -id] }.map { |id, *_| id }
end
```

## Scala

```scala
object Solution {
    def filterRestaurants(restaurants: Array[Array[Int]], veganFriendly: Int, maxPrice: Int, maxDistance: Int): List[Int] = {
        val filtered = restaurants.filter { r =>
            (veganFriendly == 0 || r(2) == 1) && r(3) <= maxPrice && r(4) <= maxDistance
        }
        val sorted = filtered.sortWith { (a, b) =>
            if (a(1) != b(1)) a(1) > b(1) else a(0) > b(0)
        }
        sorted.map(_(0)).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn filter_restaurants(
        restaurants: Vec<Vec<i32>>,
        vegan_friendly: i32,
        max_price: i32,
        max_distance: i32,
    ) -> Vec<i32> {
        let mut filtered: Vec<(i32, i32)> = Vec::new();
        for r in restaurants {
            let id = r[0];
            let rating = r[1];
            let vegan = r[2];
            let price = r[3];
            let distance = r[4];
            if (vegan_friendly == 0 || vegan == 1) && price <= max_price && distance <= max_distance {
                filtered.push((rating, id));
            }
        }
        filtered.sort_by(|&(ra, ia), &(rb, ib)| {
            if ra != rb {
                rb.cmp(&ra) // rating descending
            } else {
                ib.cmp(&ia) // id descending
            }
        });
        filtered.iter().map(|&(_, id)| id).collect()
    }
}
```

## Racket

```racket
(define/contract (filter-restaurants restaurants veganFriendly maxPrice maxDistance)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let* ([filtered
          (filter
           (lambda (r)
             (and (<= (list-ref r 3) maxPrice)               ; price
                  (<= (list-ref r 4) maxDistance)            ; distance
                  (or (= veganFriendly 0)
                      (= (list-ref r 2) 1))))                ; vegan-friendly flag
           restaurants)]
         [sorted
          (sort filtered
                (lambda (a b)
                  (let ([ra (list-ref a 1)] [rb (list-ref b 1)]
                        [ia (list-ref a 0)] [ib (list-ref b 0)])
                    (if (> ra rb) #t
                        (if (< ra rb) #f
                            (> ia ib))))))])
    (map first sorted)))
```

## Erlang

```erlang
-spec filter_restaurants(Restaurants :: [[integer()]], VeganFriendly :: integer(), MaxPrice :: integer(), MaxDistance :: integer()) -> [integer()].
filter_restaurants(Restaurants, VeganFriendly, MaxPrice, MaxDistance) ->
    Filtered = [
        {Rating, Id} ||
        [Id, Rating, Vg, Price, Distance] <- Restaurants,
        (VeganFriendly == 0 orelse Vg == 1),
        Price =< MaxPrice,
        Distance =< MaxDistance
    ],
    Sorted = lists:sort(
        fun({R1, I1}, {R2, I2}) ->
            if R1 > R2 -> true;
               R1 < R2 -> false;
               true -> I1 > I2
            end
        end,
        Filtered),
    [Id || {_Rating, Id} <- Sorted].
```

## Elixir

```elixir
defmodule Solution do
  @spec filter_restaurants(restaurants :: [[integer]], vegan_friendly :: integer, max_price :: integer, max_distance :: integer) :: [integer]
  def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance) do
    restaurants
    |> Enum.filter(fn [_id, _rating, vegan, price, distance] ->
      (vegan_friendly == 0 or vegan == 1) and price <= max_price and distance <= max_distance
    end)
    |> Enum.sort(fn [id_a, rating_a, _, _, _], [id_b, rating_b, _, _, _] ->
      if rating_a != rating_b do
        rating_a > rating_b
      else
        id_a > id_b
      end
    end)
    |> Enum.map(fn [id | _] -> id end)
  end
end
```
