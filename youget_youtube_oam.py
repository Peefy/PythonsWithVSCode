
import sys
from you_get import common as you_get       

directory = r''                       
url = 'https://www.youtube.com/watch?v=D40gKUWwx7A'     
sys.argv = ['you-get','-o',directory,url]      
you_get.main()

