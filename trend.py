import pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl="en-US", tz=360)
kw_list = ["NFT's"]
kw_list = ["oil"]
kw_list = ["ukraine"]
pytrends.build_payload(kw_list=kw_list)
#pytrend.build_payload(kw_list, timeframe='today 1-m')

historicaldf = pytrend.get_historical_interest(
  kw_list, 
  year_start=2020, month_start=10, day_start=1, hour_start=0, 
  year_end=2022, month_end=2, day_end=21, hour_end=15, cat=0, geo='', gprop='', sleep=0)

historicaldf.plot(figsize=(20, 12))
historicaldf.plot(subplots=True, figsize=(20, 12))

df = pytrends.interest_over_time()

adf = df[df.index > '2020-01-01']

df.plot(figsize=(20,7), color='purple', linewidth=7, label=kw_list)
adf["NFT's"].plot(figsize=(20,7), color='purple', linewidth=7)
adf["oil"].plot(figsize=(20,7), color='purple', linewidth=7)
adf["ukraine"].plot(figsize=(20,7), color='purple', linewidth=7)

