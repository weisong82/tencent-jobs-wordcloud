# coding: utf-8
#tencent hr jobs  wordcloud

from os import path
import matplotlib.pyplot as plt
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS
import  datetime

###define var 
jobs_file = 'jobs-2023.8.2.csv'
##########

now = datetime.datetime.now()
str_time=now.strftime('%Y-%m-%d')

d = path.dirname('__file__')

stoppath= path.join(d, 'stop.txt') #停用词文件路径
seg_file= path.join(d,'output','tencentjob_seg_words.txt') #分词文件
outfile = path.join(d,'output','jobs-hotwords'+str_time+'.png') #result

lines=open(jobs_file, encoding='utf-8').readlines()
#分词
jieba.analyse.set_stop_words(stoppath)
#停用词list，去除时候用
stoplist = {}.fromkeys([ line.strip('\n') for line in open(stoppath, encoding='utf-8') ])

##分词文件输出
with open(seg_file, 'w', encoding='utf-8') as f:
    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)# 精确模式
        #消除停用词
        segs = [word.strip() for word in list(seg_list) if word not in stoplist]
        seg_line = " ".join(segs)
        f.write(''.join(seg_line))



#word cloud


# Read the whole text.
text = open(seg_file, encoding='utf-8').read()

stopwords = set(STOPWORDS)
#可以加一些过滤词

#中文字体要单独弄
wc = WordCloud(font_path='simhei.ttf',
               width=700, height=500,
               background_color="black", max_words=100,min_font_size=10,max_font_size=40,stopwords=stopwords)
# generate word cloud
wc.generate(text)


wc.to_file(outfile)

# # show
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.figure()
# plt.axis("off")
# plt.show()

