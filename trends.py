import pandas as pd                        
from pytrends.request import TrendReq
from collections import Counter
import time

pt = TrendReq()
def tr(key_w):
    kw_list=[key_w]
    print (key_w)
    pt.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='', gprop='')
    df=pt.related_queries()
    stop=[
    'i',
    'me',
    'my',
    'myself',
    'we',
    'our',
    'ours',
    'ourselves',
    'you',
    'your',
    'yours',
    'yourself',
    'yourselves',
    'he',
    'him',
    'his',
    'himself',
    'she',
    'her',
    'hers',
    'herself',
    'it',
    'its',
    'itself',
    'they',
    'them',
    'their',
    'theirs',
    'themselves',
    'what',
    'which',
    'who',
    'whom',
    'this',
    'that',
    'these',
    'those',
    'am',
    'is',
    'are',
    'was',
    'were',
    'be',
    'been',
    'being',
    'have',
    'has',
    'had',
    'having',
    'do',
    'does',
    'did',
    'doing',
    'a',
    'an',
    'the',
    'and',
    'but',
    'if',
    'or',
    'because',
    'as',
    'until',
    'while',
    'of',
    'at',
    'by',
    'for',
    'with',
    'about',
    'against',
    'between',
    'into',
    'through',
    'during',
    'before',
    'after',
    'above',
    'below',
    'to',
    'from',
    'up',
    'down',
    'in',
    'out',
    'on',
    'off',
    'over',
    'under',
    'again',
    'further',
    'then',
    'once',
    'here',
    'there',
    'when',
    'where',
    'why',
    'how',
    'all',
    'any',
    'both',
    'each',
    'few',
    'more',
    'most',
    'other',
    'some',
    'such',
    'no',
    'nor',
    'not',
    'only',
    'own',
    'same',
    'so',
    'than',
    'too',
    'very',
    's',
    't',
    'can',
    'will',
    'just',
    'don',
    'should',
    'now'
    ]
    key=[]
    for i in df[key_w]['rising']['query']:
        for p in i.split():
            if p.lower()!= key_w:
                if p.lower() not in stop:
                    key.append(p)
                
    c = Counter(key)
    print (c.most_common(2))
    final=[]            

    for k in df[key_w]['rising']['query']:
        for i in c.most_common(2):
            if i[0] in k:
                    if k not in final:
                        print (k)
                        final.append(k)
    print ('_________________')

ll=[]#your topic list
for i in ll:
        tr(i)
