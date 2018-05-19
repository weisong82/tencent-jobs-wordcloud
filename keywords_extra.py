# coding: utf-8

import datetime
import jieba.analyse
from os import path


now = datetime.datetime.now()
str_time=now.strftime('%Y-%m-%d-%H:%M:%S')

d = path.dirname('__file__')

stoppath= path.join(d, 'stop.txt') #停用词文件路径
seg_file= path.join(d,'output','tencentjob_seg_words.txt') #分词文件
outfile = path.join(d,'output','textrank'+str_time+'.txt') #result

lines=open('/tmp/tencentjob.csv').readlines()
#分词
jieba.analyse.set_stop_words(stoppath)
#停用词list，去除时候用
stoplist = {}.fromkeys([ line.strip('\n') for line in open(stoppath) ])

##分词文件输出
with open(seg_file, 'w') as f:
    for line in lines:
        seg_list = jieba.cut(line, cut_all=False)# 精确模式
        #消除停用词
        segs = [word for word in list(seg_list) if word not in stoplist]
        seg_line = " ".join(segs)
        f.write(''.join( seg_line ))



# Read the whole text.
text = open(seg_file).read()

textrank = jieba.analyse.textrank(text, topK=100) #list


##分词文件输出
with open(outfile, 'w') as f:
     for word in textrank:
         f.write(word + '\n')
