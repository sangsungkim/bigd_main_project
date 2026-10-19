import pandas as pd
import matplotlib.pyplot as plt

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code" : str}) 
print(watchlist_df["code"].tolist())

# [005930, 000660, 005380] 
# dtype={"code" : str} 추가 없으면 [5930, 660, 5380] 으로 자동 형변환 