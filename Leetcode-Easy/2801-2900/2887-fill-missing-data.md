# 2887. Fill Missing Data

## Pythondata

```pythondata
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    if "quantity" in products.columns:
        products["quantity"] = products["quantity"].fillna(0)
    return products
```
