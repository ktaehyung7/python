from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image
import numpy as np

no_use_word = ['정의', \
               '요구사항', \
               '요구', \
               '사항', \
               '대한', \
               '방안', \
               '관련', \
               '경우', \
               '단계']

def get_noun(data):
    okt = Okt()
    noun = okt.nouns(data) #명사만 불러오기
    for i,v in enumerate(noun):
        if len(v) < 2 or (v.strip() in no_use_word):
            noun.pop(i)
            
    count = Counter(noun)
    
    noun_list = count.most_common(100)
    
    with open('C:/Users/HP DEMO HUB/Documents/wc_result.txt', 'w', encoding='utf-8') as f:
        for v in noun_list:
            f.write(" ".join(map(str,v)))
            f.write("\n")
    return noun_list

def visualize(noun_list):
    mask = np.array(Image.open('C:/Users/HP DEMO HUB/Documents/car1.png'))
    wc = WordCloud(font_path='C:/Users/HP DEMO HUB/AppData/Local/Microsoft/Windows/Fonts/NanumGothicBold.ttf', \
                   background_color="white", \
                   width=1000, \
                   height=500, \
                   max_words=100, \
                   max_font_size=300, \
                   mask=mask)

    wc.generate_from_frequencies(dict(noun_list))
    wc.to_file('C:/Users/HP DEMO HUB/Documents/wordcloud.png')    

if __name__=="__main__":
    filename = 'C:/Users/HP DEMO HUB/Documents/rfp.txt'
    f = open(filename, 'r', encoding='utf-8')
    Data = f.read()
    noun_list = get_noun(Data)
    visualize(noun_list)