# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:43:27 2023

@author: ktaeh
"""

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image
import numpy as np

"""
no_use_word = ['정의', \
               '요구사항', \
               '요구', \
               '사항', \
               '대한', \
               '방안', \
               '관련', \
               '경우', \
               '단계']
"""
no_use_word = ['감리', \
               '사업', \
               '용역', \
               '구축', \
               '시스템', \
               '서비스', \
               '기반', \
               '위탁']
    
def get_noun(data):
    okt = Okt()
    noun = okt.nouns(data) #명사만 불러오기

    for i,v in enumerate(noun):
        if len(v) < 2:
            noun.pop(i)

    for search in no_use_word:
        #print('[search: ',search, ']')
        for word in noun:
            #print("[word: ", word, "]")
            if search == word:
                while search in noun:
                    #print('>>remove: '+search)
                    noun.remove(search)

    #print(noun)
    
    count = Counter(noun)
    
    noun_list = count.most_common(100)
    
    with open('C:/Users/ktaeh/Documents/wc_result.txt', 'w', encoding='utf-8') as f:
        for v in noun_list:
            f.write(" ".join(map(str,v)))
            f.write("\n")
    return noun_list

def visualize(noun_list):
    mask = np.array(Image.open('C:/Users/ktaeh/Documents/cloud.png'))
    wc = WordCloud(font_path='C:/Users/ktaeh/AppData/Local/Microsoft/Windows/Fonts/NanumGothicBold.otf', \
                   background_color="white", \
                   width=1000, \
                   height=500, \
                   max_words=100, \
                   max_font_size=300, \
                   mask=mask)

    wc.generate_from_frequencies(dict(noun_list))
    wc.to_file('C:/Users/ktaeh/Documents/wordcloud.png')    

if __name__=="__main__":
    filename = 'C:/Users/ktaeh/Documents/rfp.txt'
    f = open(filename, 'r', encoding='utf-8')
    Data = f.read()
    noun_list = get_noun(Data)
    visualize(noun_list)
