import pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl="en-US", tz=360)
pytrends.build_payload(kw_list=["NFT's"])
df = pytrends.interest_over_time()
df["NFT's"].plot(figsize=(20,7), color='purple', linewidth=7)
