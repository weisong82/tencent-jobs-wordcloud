import requests

url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1690944943621&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=50&language=zh-cn&area=cn"

payload = {}
headers = {
  'authority': 'careers.tencent.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': '_ga=GA1.2.1026485821.1657590691; _qddaz=QD.610457608303412; web_uid=cd40e94d-4840-43f8-b347-aafb4f045e90; _gcl_au=1.1.1416515317.1684372067; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100014256492%22%2C%22first_id%22%3A%22181f01ab362154-064d65a09f91dfc-1c525635-2073600-181f01ab363f1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgxZjAxYWIzNjIxNTQtMDY0ZDY1YTA5ZjkxZGZjLTFjNTI1NjM1LTIwNzM2MDAtMTgxZjAxYWIzNjNmMSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEwMDAxNDI1NjQ5MiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22100014256492%22%7D%2C%22%24device_id%22%3A%22181f01ab362154-064d65a09f91dfc-1c525635-2073600-181f01ab363f1%22%7D',
  'dnt': '1',
  'referer': 'https://careers.tencent.com/search.html',
  'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json()['Data']['Count'])   ## 2574
print(response.json()['Data']['Posts'][0]) 
#{'Id': 0, 'PostId': '1622531642809655296', 'RecruitPostId': 94858, 'RecruitPostName': '魔方市场高级赛事经理', 'CountryName': '中国', 'LocationName': '深圳', 'BGName': 'IEG', 'ComName': '', 'ProductName': '', 'CategoryName': '营销与公关', 'Responsibility': '1.负责魔方射击游戏电竞赛事规划及落地，根据产品和市场特性，制定赛事目标、策略与计划，并落地执行；\r\n2.与项目研发及各版块人员保持密切协作关系，挖掘探索调优赛事模式与赛事价值，驱动呈现优质的赛事内容与赛事用户价值最大化；\r\n3.通过赛事数据、用户反馈与市场状态做持续追踪与分析，快速迭代优化电竞策略，并沉淀经验与方法；\r\n4.整合赛事策划与营销策略、赛事生态等各版块，协调各种资源达成目标，实现项目效果最大化。', 'LastUpdateTime': '2023年08月02日', 'PostURL': 'http://careers.tencent.com/jobdesc.html?postId=1622531642809655296', 'SourceID': 1, 'IsCollect': False, 'IsValid': True, 'RequireWorkYearsName': '五年以上工作经验'}