# -*- coding:utf-8 -*-
__author__ = 'PFENG'

import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def open_file():
    # 读取报文
    # file_name = raw_input("请输入报文路径：")
    file_name = "C:/RES_FLAT_M_20150420010000_2106371.0000004347"
    f = open(file_name)
    mobile_list = []
    line = f.readline()
    while line:
        mobile_no = line.split("|")[-2]
        print(mobile_no)
        mobile_list.append(mobile_no)
        line = f.readline()
    f.close()

    # 查询归属地
    f = open('area.txt', 'w')
    for m in mobile_list:

            api_url = "http://virtual.paipai.com/extinfo/GetMobileProductInfo?mobile="+m+"&amount=10000&callname=cb"
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            req = urllib2.Request(api_url, headers=headers)
            res = urllib2.urlopen(req)
            html = res.read()
            html = html[3:-68]
            html = html.decode('GBK').encode('utf-8')
            try:
                pattern = r'cityname:\'(.+?)\'}'
                imgre = re.compile(pattern)
                city = re.findall(imgre, html)[0]
                print(m+","+city)
                f.write(m+","+city+"\n")
            except:
                pass
    f.close()

if __name__ == '__main__':
    open_file()