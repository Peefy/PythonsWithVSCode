
import sys
from you_get import common as you_get       

directory = r'E:\xpf\Video'                       
url = 'https://www.bilibili.com/video/av11596963?from=search&seid=7224614101954159775'     
sys.argv = ['you-get','-o',directory,url]      
you_get.main()

