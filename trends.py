import pandas as pd                        
from pytrends.request import TrendReq
from collections import Counter
import time

pt = TrendReq()
def tr(key_w):
    kw_list=[key_w]
    print (key_w)
    pt.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='', gprop='')
