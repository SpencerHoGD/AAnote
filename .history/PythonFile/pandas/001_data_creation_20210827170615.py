import numpy as np
import pandas as pd


# s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20210820", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))



# print(s)
# print(dates)
print(df)
print()
print()
print()
print()
print()