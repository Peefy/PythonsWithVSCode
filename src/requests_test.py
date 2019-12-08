
import requests

zhuanlanHost = "https://news-at.zhihu.com/api/4/news/latest"
githuburl = 'https://github.com/Peefy/WebMagicSharp/tree/master/WebMagicSharp'

r = requests.get(githuburl)
print(r.text)

r = requests.get(zhuanlanHost)
print(r.text)
