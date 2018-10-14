#########################
#########################
#########################
from __future__ import (absolute_import ,division ,
                         print_function ,unicode_literals)

try:
    #Python 2.x
    from urllib2 import urlopen

except ImportError:
    #Python 3.x
    from urllib.request import urlopen

import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
#读取数据
req = response.read()
#将数据写入文件
file_name = 'btc_close_2017.json'
with open(file_name ,'wb') as f_obj:
    f_obj.write(req)

file_urllib = json.loads(req)
print(file_urllib)
