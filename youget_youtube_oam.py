
import sys
from you_get import common as you_get       

directory = r'./video/'                       
url = 'https://www.youtube.com/watch?v=QHYJ4VpqAvs'     
sys.argv = ['you-get','-o',directory,url]      
you_get.main()

