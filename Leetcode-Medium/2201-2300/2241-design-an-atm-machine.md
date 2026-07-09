# 2241. Design an ATM Machine

## Cpp

```cpp
class ATM {
public:
    ATM() {
        counts = vector<long long>(5, 0);
        denoms = {20, 50, 100, 200, 500};
    }
    
    void deposit(vector<int> banknotesCount) {
        for (int i = 0; i < 5; ++i) {
            counts[i] += banknotesCount[i];
        }
    }
    
    vector<int> withdraw(int amount) {
        long long amt = amount;
        vector<long long> used(5, 0);
        // Greedy from largest to smallest
        for (int i = 4; i >= 0; --i) {
            long long take = min(counts[i], amt / denoms[i]);
            used[i] = take;
            amt -= take * denoms[i];
        }
        if (amt != 0) {
            return vector<int>{-1};
        }
        // Apply withdrawal
        for (int i = 0; i < 5; ++i) {
            counts[i] -= used[i];
        }
        vector<int> result(5);
        for (int i = 0; i < 5; ++i) result[i] = static_cast<int>(used[i]);
        return result;
    }

private:
    vector<long long> counts;
    const vector<int> denoms;
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
 */
```

## Java

```java
class ATM {
    private final long[] notes = new long[5];
    private static final int[] VALUES = {20, 50, 100, 200, 500};

    public ATM() {
    }

    public void deposit(int[] banknotesCount) {
        for (int i = 0; i < 5; i++) {
            notes[i] += banknotesCount[i];
        }
    }

    public int[] withdraw(int amount) {
        long remaining = amount;
        long[] used = new long[5];

        for (int i = 4; i >= 0; i--) {
            if (remaining <= 0) break;
            long canUse = Math.min(notes[i], remaining / VALUES[i]);
            used[i] = canUse;
            remaining -= canUse * VALUES[i];
        }

        if (remaining != 0) {
            return new int[]{-1};
        }

        // successful withdrawal, update notes and prepare result
        int[] result = new int[5];
        for (int i = 0; i < 5; i++) {
            notes[i] -= used[i];
            result[i] = (int) used[i];
        }
        return result;
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */
```

## Python

```python
class ATM(object):
    def __init__(self):
        self.denoms = [20, 50, 100, 200, 500]
        self.cnt = [0] * 5

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for i in range(5):
            self.cnt[i] += banknotesCount[i]

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        used = [0] * 5
        remaining = amount
        # Greedy from largest to smallest denomination
        for i in range(4, -1, -1):
            if remaining <= 0:
                break
            take = min(self.cnt[i], remaining // self.denoms[i])
            used[i] = take
            remaining -= take * self.denoms[i]
        if remaining != 0:
            return [-1]
        # Successful withdrawal: update counts
        for i in range(5):
            self.cnt[i] -= used[i]
        return used
```

## Python3

```python
class ATM:
    def __init__(self):
        self.cnt = [0] * 5
        self.vals = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.cnt[i] += banknotesCount[i]

    def withdraw(self, amount):
        # attempt greedy for first three denominations
        used = [0] * 5
        remaining = amount

        for i in range(3):  # 500,200,100
            take = min(self.cnt[i], remaining // self.vals[i])
            used[i] = take
            remaining -= take * self.vals[i]

        # handle 50 and 20 with backtracking on number of 50s
        max_fifty = min(self.cnt[3], remaining // 50)
        for f in range(max_fifty, -1, -1):
            rem_after_fifty = remaining - f * 50
            if rem_after_fifty % 20 != 0:
                continue
            tw = rem_after_fifty // 20
            if tw <= self.cnt[4]:
                used[3] = f
                used[4] = tw
                # update counts
                for i in range(5):
                    self.cnt[i] -= used[i]
                return used

        return [-1]
```

## C

```c
typedef struct {
    long long cnt[5];
} ATM;

static const int DENOMS[5] = {20, 50, 100, 200, 500};

ATM* aTMCreate() {
    ATM* obj = (ATM*)malloc(sizeof(ATM));
    for (int i = 0; i < 5; ++i) obj->cnt[i] = 0;
    return obj;
}

void aTMDeposit(ATM* obj, int* banknotesCount, int banknotesCountSize) {
    for (int i = 0; i < 5 && i < banknotesCountSize; ++i) {
        obj->cnt[i] += (long long)banknotesCount[i];
    }
}

int* aTMWithdraw(ATM* obj, int amount, int* retSize) {
    long long need = amount;
    long long used[5] = {0};
    
    for (int i = 4; i >= 0; --i) {
        long long take = need / DENOMS[i];
        if (take > obj->cnt[i]) take = obj->cnt[i];
        used[i] = take;
        need -= take * DENOMS[i];
    }
    
    int* res = (int*)malloc(sizeof(int) * 5);
    if (need != 0) {
        *retSize = 1;
        res[0] = -1;
        return res;
    }
    
    for (int i = 0; i < 5; ++i) {
        obj->cnt[i] -= used[i];
        res[i] = (int)used[i];
    }
    *retSize = 5;
    return res;
}

void aTMFree(ATM* obj) {
    free(obj);
}
```

## Csharp

```csharp
public class ATM
{
    private readonly long[] _counts = new long[5];
    private static readonly int[] Denominations = { 20, 50, 100, 200, 500 };

    public ATM()
    {
    }

    public void Deposit(int[] banknotesCount)
    {
        for (int i = 0; i < 5; i++)
        {
            _counts[i] += banknotesCount[i];
        }
    }

    public int[] Withdraw(int amount)
    {
        long remaining = amount;
        int[] used = new int[5];

        for (int i = 4; i >= 0; i--)
        {
            if (remaining == 0) break;
            long need = remaining / Denominations[i];
            long take = Math.Min(_counts[i], need);
            used[i] = (int)take;
            remaining -= take * Denominations[i];
        }

        if (remaining != 0)
        {
            return new int[] { -1 };
        }

        for (int i = 0; i < 5; i++)
        {
            _counts[i] -= used[i];
        }

        return used;
    }
}
```

## Javascript

```javascript
var ATM = function() {
    this.denoms = [20, 50, 100, 200, 500];
    this.count = [0, 0, 0, 0, 0];
};

/**
 * @param {number[]} banknotesCount
 * @return {void}
 */
ATM.prototype.deposit = function(banknotesCount) {
    for (let i = 0; i < 5; i++) {
        this.count[i] += banknotesCount[i];
    }
};

/**
 * @param {number} amount
 * @return {number[]}
 */
ATM.prototype.withdraw = function(amount) {
    const used = new Array(5).fill(0);
    let remaining = amount;
    for (let i = 4; i >= 0; i--) {
        const denom = this.denoms[i];
        const take = Math.min(this.count[i], Math.floor(remaining / denom));
        used[i] = take;
        remaining -= take * denom;
    }
    if (remaining === 0) {
        for (let i = 0; i < 5; i++) {
            this.count[i] -= used[i];
        }
        return used;
    } else {
        return [-1];
    }
};
```

## Typescript

```typescript
class ATM {
    private readonly denominations: number[] = [20, 50, 100, 200, 500];
    private bank: number[];

    constructor() {
        this.bank = new Array(5).fill(0);
    }

    deposit(banknotesCount: number[]): void {
        for (let i = 0; i < 5; i++) {
            this.bank[i] += banknotesCount[i];
        }
    }

    withdraw(amount: number): number[] {
        const used = new Array(5).fill(0);
        let remaining = amount;

        for (let i = 4; i >= 0; i--) {
            const canUse = Math.min(this.bank[i], Math.floor(remaining / this.denominations[i]));
            used[i] = canUse;
            remaining -= canUse * this.denominations[i];
        }

        if (remaining === 0) {
            for (let i = 0; i < 5; i++) {
                this.bank[i] -= used[i];
            }
            return used;
        } else {
            return [-1];
        }
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
```

## Php

```php
class ATM {
    private $cnt;
    private $denoms;

    function __construct() {
        $this->cnt = array_fill(0, 5, 0);
        $this->denoms = [20, 50, 100, 200, 500];
    }

    /**
     * @param Integer[] $banknotesCount
     * @return NULL
     */
    function deposit($banknotesCount) {
        for ($i = 0; $i < 5; $i++) {
            $this->cnt[$i] += $banknotesCount[$i];
        }
    }

    /**
     * @param Integer $amount
     * @return Integer[]
     */
    function withdraw($amount) {
        $used = array_fill(0, 5, 0);
        $remaining = $amount;
        for ($i = 4; $i >= 0; $i--) {
            $maxNotes = intdiv($remaining, $this->denoms[$i]);
            $use = min($maxNotes, $this->cnt[$i]);
            $used[$i] = $use;
            $remaining -= $use * $this->denoms[$i];
        }
        if ($remaining === 0) {
            for ($i = 0; $i < 5; $i++) {
                $this->cnt[$i] -= $used[$i];
            }
            return $used;
        } else {
            return [-1];
        }
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * $obj = new ATM();
 * $obj->deposit($banknotesCount);
 * $ret_2 = $obj->withdraw($amount);
 */
```

## Swift

```swift
class ATM {
    private let denominations = [20, 50, 100, 200, 500]
    private var counts = [Int](repeating: 0, count: 5)
    
    init() {}
    
    func deposit(_ banknotesCount: [Int]) {
        for i in 0..<5 {
            counts[i] += banknotesCount[i]
        }
    }
    
    func withdraw(_ amount: Int) -> [Int] {
        var remaining = amount
        var used = [Int](repeating: 0, count: 5)
        
        for i in stride(from: 4, through: 0, by: -1) {
            let denom = denominations[i]
            if remaining >= denom && counts[i] > 0 {
                let need = remaining / denom
                let take = min(counts[i], need)
                used[i] = take
                remaining -= take * denom
            }
        }
        
        if remaining == 0 {
            for i in 0..<5 {
                counts[i] -= used[i]
            }
            return used
        } else {
            return [-1]
        }
    }
}
```

## Kotlin

```kotlin
class ATM() {
    private val denominations = intArrayOf(20, 50, 100, 200, 500)
    private val counts = LongArray(5)

    fun deposit(banknotesCount: IntArray) {
        for (i in 0..4) {
            counts[i] += banknotesCount[i].toLong()
        }
    }

    fun withdraw(amount: Int): IntArray {
        var remaining = amount.toLong()
        val used = LongArray(5)

        for (i in 4 downTo 0) {
            if (remaining == 0L) break
            val canUse = minOf(counts[i], remaining / denominations[i])
            if (canUse > 0) {
                used[i] = canUse
                remaining -= canUse * denominations[i]
            }
        }

        return if (remaining == 0L) {
            for (i in 0..4) {
                counts[i] -= used[i]
            }
            IntArray(5) { used[it].toInt() }
        } else {
            intArrayOf(-1)
        }
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
```

## Dart

```dart
class ATM {
  static const List<int> _values = [20, 50, 100, 200, 500];
  final List<int> _notes = List.filled(5, 0);

  ATM();

  void deposit(List<int> banknotesCount) {
    for (int i = 0; i < 5; ++i) {
      _notes[i] += banknotesCount[i];
    }
  }

  List<int> withdraw(int amount) {
    List<int> used = List.filled(5, 0);
    int remaining = amount;

    for (int i = 4; i >= 0; --i) {
      if (remaining <= 0) break;
      int need = remaining ~/ _values[i];
      if (need > 0) {
        int take = need <= _notes[i] ? need : _notes[i];
        used[i] = take;
        remaining -= take * _values[i];
      }
    }

    if (remaining != 0) {
      return [-1];
    }

    for (int i = 0; i < 5; ++i) {
      _notes[i] -= used[i];
    }
    return used;
  }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = ATM();
 * obj.deposit(banknotesCount);
 * List<int> param2 = obj.withdraw(amount);
 */
```

## Golang

```go
type ATM struct {
	cnt [5]int64
}

func Constructor() ATM {
	return ATM{}
}

func (this *ATM) Deposit(banknotesCount []int) {
	for i := 0; i < 5; i++ {
		this.cnt[i] += int64(banknotesCount[i])
	}
}

func (this *ATM) Withdraw(amount int) []int {
	denoms := []int64{20, 50, 100, 200, 500}
	need := make([]int64, 5)
	rem := int64(amount)

	for i := 4; i >= 0; i-- {
		if rem <= 0 {
			break
		}
		maxUse := rem / denoms[i]
		if maxUse > this.cnt[i] {
			maxUse = this.cnt[i]
		}
		need[i] = maxUse
		rem -= maxUse * denoms[i]
	}

	if rem != 0 {
		return []int{-1}
	}

	// successful withdrawal, update counts and prepare result slice
	res := make([]int, 5)
	for i := 0; i < 5; i++ {
		this.cnt[i] -= need[i]
		res[i] = int(need[i])
	}
	return res
}

/**
 * Your ATM object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Deposit(banknotesCount);
 * param_2 := obj.Withdraw(amount);
 */
```

## Ruby

```ruby
class ATM
  def initialize()
    @cnt = [0, 0, 0, 0, 0]
    @denoms = [20, 50, 100, 200, 500]
  end

=begin
    :type banknotes_count: Integer[]
    :rtype: Void
=end
  def deposit(banknotes_count)
    5.times do |i|
      @cnt[i] += banknotes_count[i]
    end
  end

=begin
    :type amount: Integer
    :rtype: Integer[]
=end
  def withdraw(amount)
    used = Array.new(5, 0)
    remaining = amount
    4.downto(0) do |i|
      d = @denoms[i]
      take = [remaining / d, @cnt[i]].min
      used[i] = take
      remaining -= take * d
    end
    if remaining == 0
      5.times { |i| @cnt[i] -= used[i] }
      used
    else
      [-1]
    end
  end
end
```

## Scala

```scala
class ATM() {
  private val denominations = Array(20, 50, 100, 200, 500)
  private val notes = new Array[Long](5)

  def deposit(banknotesCount: Array[Int]): Unit = {
    var i = 0
    while (i < 5) {
      notes(i) += banknotesCount(i).toLong
      i += 1
    }
  }

  def withdraw(amount: Int): Array[Int] = {
    val used = new Array[Long](5)
    var remaining = amount.toLong
    var i = 4
    while (i >= 0) {
      if (remaining > 0) {
        val need = remaining / denominations(i)
        val take = math.min(need, notes(i))
        used(i) = take
        remaining -= take * denominations(i)
      }
      i -= 1
    }
    if (remaining == 0) {
      var j = 0
      while (j < 5) {
        notes(j) -= used(j)
        j += 1
      }
      used.map(_.toInt)
    } else {
      Array(-1)
    }
  }
}

/**
 * Your ATM object will be instantiated and called as such:
 * val obj = new ATM()
 * obj.deposit(banknotesCount)
 * val param_2 = obj.withdraw(amount)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct ATM {
    notes: RefCell<Vec<i64>>,
}

impl ATM {
    fn new() -> Self {
        ATM {
            notes: RefCell::new(vec![0; 5]),
        }
    }

    fn deposit(&self, banknotes_count: Vec<i32>) {
        let mut notes = self.notes.borrow_mut();
        for i in 0..5 {
            notes[i] += banknotes_count[i] as i64;
        }
    }

    fn withdraw(&self, amount: i32) -> Vec<i32> {
        const DENOM: [i64; 5] = [20, 50, 100, 200, 500];
        let mut need = amount as i64;
        let mut notes = self.notes.borrow_mut();
        let mut used = vec![0i64; 5];

        for i in (0..5).rev() {
            let take = std::cmp::min(notes[i], need / DENOM[i]);
            used[i] = take;
            need -= take * DENOM[i];
        }

        if need != 0 {
            return vec![-1];
        }

        for i in 0..5 {
            notes[i] -= used[i];
        }
        used.iter().map(|&x| x as i32).collect()
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * let obj = ATM::new();
 * obj.deposit(banknotesCount);
 * let ret_2: Vec<i32> = obj.withdraw(amount);
 */
```

## Racket

```racket
(define atm%
  (class object%
    (super-new)
    (define banknotes (make-vector 5 0))
    (define denominations (vector 20 50 100 200 500))
    
    ; deposit : (listof exact-integer?) -> void?
    (define/public (deposit banknotes-count)
      (for ([i (in-range 5)])
        (vector-set! banknotes i
                     (+ (vector-ref banknotes i) (list-ref banknotes-count i)))))
    
    ; withdraw : exact-integer? -> (listof exact-integer?)
    (define/public (withdraw amount)
      (let* ([used (make-vector 5 0)]
             [remaining amount])
        (for ([i (in-range 4 -1 -1)])
          (define d (vector-ref denominations i))
          (define have (vector-ref banknotes i))
          (define use (min have (quotient remaining d)))
          (when (> use 0)
            (vector-set! used i use)
            (set! remaining (- remaining (* use d)))))
        (if (= remaining 0)
            (begin
              (for ([i (in-range 5)])
                (vector-set! banknotes i
                             (- (vector-ref banknotes i) (vector-ref used i))))
              (vector->list used))
            (list -1)))))
```

## Erlang

```erlang
-define(DENOMS_TUPLE, {20,50,100,200,500}).

-spec atm_init_() -> any().
atm_init_() ->
    erlang:put(atm_state, [0,0,0,0,0]).

-spec atm_deposit(BanknotesCount :: [integer()]) -> any().
atm_deposit(BanknotesCount) ->
    State = erlang:get(atm_state),
    NewState = lists:zipwith(fun(A,B) -> A + B end, State, BanknotesCount),
    erlang:put(atm_state, NewState).

-spec atm_withdraw(Amount :: integer()) -> [integer()].
atm_withdraw(Amount) ->
    StateList = erlang:get(atm_state),
    StateT = list_to_tuple(StateList),
    UsedT0 = erlang:make_tuple(5, 0),

    {RemAmt, UsedT} = withdraw_loop(5, Amount, StateT, UsedT0),

    case RemAmt of
        0 ->
            %% successful withdrawal, update state
            NewStateT = update_state(StateT, UsedT),
            erlang:put(atm_state, tuple_to_list(NewStateT)),
            tuple_to_list(UsedT);
        _ ->
            [-1]
    end.

%% Greedy loop from high denomination index down to 1
withdraw_loop(Idx, AmtLeft, StateT, UsedT) when Idx >= 1 ->
    Denom = element(Idx, ?DENOMS_TUPLE),
    Avail = element(Idx, StateT),
    Use = erlang:min(Avail, AmtLeft div Denom),
    NewAmt = AmtLeft - Use * Denom,
    NewUsedT = setelement(Idx, UsedT, Use),
    withdraw_loop(Idx - 1, NewAmt, StateT, NewUsedT);
withdraw_loop(0, AmtLeft, _StateT, UsedT) ->
    {AmtLeft, UsedT}.

%% Subtract used notes from current state
update_state(StateT, UsedT) ->
    update_state_iter(5, StateT, UsedT).

update_state_iter(Idx, StateAcc, UsedT) when Idx >= 1 ->
    Old = element(Idx, StateAcc),
    Use = element(Idx, UsedT),
    NewStateAcc = setelement(Idx, StateAcc, Old - Use),
    update_state_iter(Idx - 1, NewStateAcc, UsedT);
update_state_iter(0, StateAcc, _UsedT) ->
    StateAcc.
```

## Elixir

```elixir
defmodule ATM do
  @spec init_() :: any
  def init_() do
    Process.put(:atm_counts, [0, 0, 0, 0, 0])
    :ok
  end

  @spec deposit(banknotes_count :: [integer]) :: any
  def deposit(banknotes_count) do
    current = Process.get(:atm_counts, [0, 0, 0, 0, 0])

    new_counts =
      Enum.zip(current, banknotes_count)
      |> Enum.map(fn {a, b} -> a + b end)

    Process.put(:atm_counts, new_counts)
    :ok
  end

  @spec withdraw(amount :: integer) :: [integer]
  def withdraw(amount) do
    counts = Process.get(:atm_counts, [0, 0, 0, 0, 0])
    indices = [4, 3, 2, 1, 0]          # correspond to denominations 500,200,100,50,20
    denoms = [500, 200, 100, 50, 20]

    {used_desc, remaining, new_counts_desc} =
      Enum.reduce(Enum.zip(indices, denoms), {[], amount, []}, fn {i, d},
                                                                {used_acc, amt, new_acc} ->
        cnt = Enum.at(counts, i)
        take = min(cnt, div(amt, d))
        {
          [take | used_acc],
          amt - take * d,
          [cnt - take | new_acc]
        }
      end)

    if remaining == 0 do
      used = Enum.reverse(used_desc)          # order: 20,50,100,200,500
      new_counts = Enum.reverse(new_counts_desc)
      Process.put(:atm_counts, new_counts)
      used
    else
      [-1]
    end
  end
end
```
