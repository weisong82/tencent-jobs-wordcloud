# tencent-jobs-wordcloud

腾讯社招岗位词云提取

1.运行fetch_by_api2019-7 可以用接口抓取  截止测试日期2023.8.2有效

## 已经失效

1.scrapy爬虫，获取全部的job信息，写入文件.

   a.运行方式cd tencentjob/spiders;  scrapy crawl tencent;

   b.配置文件路径:FEED_URI="/tmp/tencentjob.csv"

## wordCloud_gen.py

2.用jieba分词做一些分词、停用词过滤
3.用WordCloud直观展示词云

 ![image](https://github.com/weisong82/tencent-jobs-wordcloud/blob/master/wc.png)
 2018.5.19更新
 ![image](output/jobs-hotwords2018.5.19.png)
 2023.8.2更新
 [image](output/jobs-hotwords2023-08-02.png)

## keywords_extra.py

直接使用jieba，在Textrank算法下提取的关键词列表，输出到textrank-${date}
