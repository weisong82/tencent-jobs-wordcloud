
# coding: utf-8

# In[1]:


###tencent hr jobs wc

import jieba
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS


# In[2]:


lines=open('../tencentjob.csv').readlines() 
#分词
jieba.analyse.set_stop_words("../jieba/stop.txt")
#停用词list，去除时候用
stoplist = {}.fromkeys([ line.strip() for line in open("../jieba/stop.txt") ])  


# In[3]:


##分词文件输出
with open('tencentjob_seg_words.txt', 'w') as f:
    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)# 精确模式
        #消除停用词
        segs = [word for word in list(seg_list) if word not in stoplist]  
        seg_line = " ".join(segs)  
        f.write(''.join( seg_line ))


# In[4]:


#关键词抽取
content = open('../tencentjob.csv', 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=100)
print(",".join(tags))


# In[14]:


#word cloud
d = path.dirname('__file__')

# Read the whole text.
text = open(path.join(d, 'tencentjob_seg_words.txt')).read()

stopwords = set(STOPWORDS)
#可以加一些过滤词

#中文字体要单独弄
wc = WordCloud(font_path='/usr/share/fonts//simhei.ttf',               width=700, height=500,               background_color="black", max_words=100,min_font_size=10,max_font_size=40,stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "jobs-hotwords.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.axis("off")
plt.show()

