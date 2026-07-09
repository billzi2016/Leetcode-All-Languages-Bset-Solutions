# 1683. Invalid Tweets

## Mysql

```mysql
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
```

## Mssql

```mssql
SELECT tweet_id
FROM Tweets
WHERE LEN(content) > 15;
```

## Oraclesql

```oraclesql
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```

## Pythondata

```pythondata
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets["content"].astype(str).str.len() > 15
    return tweets.loc[mask, ["tweet_id"]].reset_index(drop=True)
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
```
