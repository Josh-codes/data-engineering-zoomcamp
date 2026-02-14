import sys

import pandas as pd
print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "passenger": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_tripdata_{month:02d}.parquet")

print(f"Running pipeline for month {month}")
