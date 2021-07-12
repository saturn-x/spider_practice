#coding=utf-8
from time import sleep

import  requests
import  re
import csv
##这里是练习一下正则表达式
from numpy.random import rand

if __name__ == '__main__':
    f=open("maoyantop100.csv","w",encoding='utf_8_sig')
    csw_write=csv.writer(f)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie":"__mta=221691815.1625978889745.1626069127134.1626069321989.36; uuid_n_v=v1; _lxsdk_cuid=17a94a21148c8-0c70681c0e0b9b-6373264-144600-17a94a21148c8; _lxsdk=30908910E20311EB82B96B700774E9B877F32FBC15B746F6A55DC08C93953FC2; __mta=221691815.1625978889745.1625991287161.1626066527506.12; uuid=691DB950E2D111EBAD8677F166774E1CC89DD3AA512C42C697E188E315E07829; _csrf=837b7f9d9ccadaa8326260110996a92b7777373b70b1deea76aaf112efe9600d; lt=okRqed3NCdTvLAFRalqwamoD0KcAAAAACw4AACUx_lDVip6njmisPRmEOvpUVEFQOHXbAZBjlzcc30tqpvilQ1U25WzKW3mHFT3PSg; lt.sig=XbXOsGAkrZzQ7hceQ9S0E59kdBw; uid=774720282; uid.sig=LwTumzNUqYBWmKU3GH2qxCgBFiA; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1626067497,1626067498,1626067498,1626067499; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1626069322"
    }
    for offset in range(0,10):
        res=requests.get("https://maoyan.com/board/4?offset="+str(offset*10),headers=headers)
        content=res.text
        print(res.status_code)
        obj=re.compile(r'<i class="board-index board-index.*?>(?P<rank>.*?)</i.*?<p class="name"><a.*?>(?P<film_name>.*?)</'
                       r'.*?p class="star">(?P<start>.*?)</p>.*?<p class="releasetime">(?P<film_time>.*?)<',re.S)
        #result是提个迭代器
        result=obj.finditer(content)
        for i in result:
            dict=i.groupdict()
            print(dict)
            dict["start"]=dict["start"].strip()
            csw_write.writerow(dict.values())
            sleep(rand()%2)
    sleep(rand()%2)

