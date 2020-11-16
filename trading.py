import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

plt.rcParams["figure.figsize"] = (5, 3)  # (w, h)
plt.rcParams["figure.dpi"] = 150

aapl = pd.read_csv("data/AAPL_2.csv", header=0, names=[
    "date", "volume", "open", "high", "low", "close", "adjclose"]).set_index('date')

aapl = aapl.iloc[::-1]

aapl.index = pd.to_datetime(aapl.index)
rets = aapl['close'].diff()[1:]

print(rets)
