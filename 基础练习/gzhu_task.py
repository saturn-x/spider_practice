import re
import time
from io import BytesIO
from urllib import parse

from lxml import etree
#/html/head/meta[7]
import requests
from PIL import Image, ImageEnhance
from pytesseract import pytesseract
from urllib.parse import urlparse,urlencode

def captcha_ver(img_res):
    image = Image.open(BytesIO(img_res.content))
    image = image.convert('RGB')
    enhancer = ImageEnhance.Color(image)
    enhancer = enhancer.enhance(2)
    enhancer = ImageEnhance.Brightness(enhancer)
    enhancer = enhancer.enhance(2)
    enhancer = ImageEnhance.Contrast(enhancer)
    enhancer = enhancer.enhance(7)
    enhancer = ImageEnhance.Sharpness(enhancer)
    image = enhancer.enhance(20)
    text = pytesseract.image_to_string(image, lang="eng")
    code=re.findall("\d+", text)[0]
    return code

def parse_form_data(html,code):
    html_lxml = etree.HTML(html)
    target = html_lxml.xpath('//div[@class="row btn-row"]/input/@value')
    form_data = {
        "username": "1906400018",
        "password": "Asd13612342422",
        "captcha": code,
        "warn": "true",
        "lt": target[0],
        "execution": target[1],
        "_eventId": "submit",
        "submit": "登录"
    }
    return form_data

###自动打卡
def daka(client,headers):
    url="http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start"
    res=client.get(url)
    print("请求接口",res.text)
    #拿到csrfToken
    html=etree.HTML(res.text)
    result=html.xpath("/html/head/meta[7]/@content")
    print("token",result[0])
    # tmp="idc=XNYQSB&release=&csrfToken=oGgEw9CtE2vlhhPLPpLjthhQV8YtFdAj&formData=%7B%22fieldCXY%22%3A%22%E5%85%A8%E5%9B%BD%E7%96%AB%E6%83%85%E4%B8%AD%E9%AB%98%E9%A3%8E%E9%99%A9%E5%9C%B0%E5%8C%BA%E5%90%8D%E5%8D%95%EF%BC%88%E6%88%AA%E6%AD%A22021%E5%B9%B47%E6%9C%8812%E6%97%A515%E6%97%B6%EF%BC%89%5Cn%5Cn%E9%AB%98%E9%A3%8E%E9%99%A9%E5%9C%B0%E5%8C%BA%EF%BC%9A%5Cn%E4%BA%91%E5%8D%97%E7%9C%81%E5%BE%B7%E5%AE%8F%E5%82%A3%E6%97%8F%E6%99%AF%E9%A2%87%E6%97%8F%E8%87%AA%E6%B2%BB%E5%B7%9E%E7%91%9E%E4%B8%BD%E5%B8%82%E5%A7%90%E5%91%8A%E5%9B%BD%E9%97%A8%E7%A4%BE%E5%8C%BA%5Cn%5Cn%E4%B8%AD%E9%A3%8E%E9%99%A9%E5%9C%B0%E5%8C%BA%EF%BC%9A%5Cn%E6%97%A0%22%2C%22_VAR_ACTION_REALNAME%22%3A%22%E6%B4%AA%E6%A6%95%E6%B6%9B%22%2C%22_VAR_RELEASE%22%3A%22true%22%2C%22_VAR_NOW_MONTH%22%3A%227%22%2C%22_VAR_ACTION_USERCODES%22%3A%221906400018%22%2C%22_VAR_ACTION_ACCOUNT%22%3A%221906400018%22%2C%22_VAR_ACTION_ORGANIZES_Names%22%3A%22%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22_VAR_URL_Attr%22%3A%22%7B%7D%22%2C%22_VAR_POSITIONS%22%3A%220206%3A02%3A1906400018%22%2C%22_VAR_ACTION_ORGANIZES_Codes%22%3A%220206%22%2C%22_VAR_NOW_YEAR%22%3A%222021%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Codes%22%3A%2202%22%2C%22_VAR_ACTION_ORGANIZE%22%3A%220206%22%2C%22_VAR_ACTION_INDEP_ORGANIZE%22%3A%2202%22%2C%22_VAR_ACTION_INDEP_ORGANIZE_Name%22%3A%22%E5%AD%A6%E9%99%A2%22%2C%22_VAR_ACTION_ORGANIZE_Name%22%3A%22%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ORGANIZES_Codes%22%3A%220206%22%2C%22_VAR_ADDR%22%3A%22202.192.29.74%22%2C%22_VAR_OWNER_ORGANIZES_Names%22%3A%22%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E7%BD%91%E7%BB%9C%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2%22%2C%22_VAR_URL%22%3A%22http%3A%2F%2Fyqtb.gzhu.edu.cn%2Finfoplus%2Fform%2FXNYQSB%2Fstart%22%2C%22_VAR_ACTION_INDEP_ORGANIZES_Names%22%3A%22%E5%AD%A6%E9%99%A2%22%2C%22_VAR_OWNER_ACCOUNT%22%3A%221906400018%22%2C%22_VAR_OWNER_USERCODES%22%3A%221906400018%22%2C%22_VAR_NOW_DAY%22%3A%2212%22%2C%22_VAR_OWNER_REALNAME%22%3A%22%E6%B4%AA%E6%A6%95%E6%B6%9B%22%2C%22_VAR_NOW%22%3A%221626083170%22%2C%22_VAR_ENTRY_NUMBER%22%3A%22-1%22%2C%22_VAR_ENTRY_NAME%22%3A%22%22%2C%22_VAR_ENTRY_TAGS%22%3A%22%22%7D&lang=zh"
    # dict={}
    # for i in parse.parse_qs(tmp).items():
    #     dict[i[0]]=i[1][0]
    # print(dict)
    data={'idc': 'XNYQSB', 'csrfToken': 'oGgEw9CtE2vlhhPLPpLjthhQV8YtFdAj', 'formData': '{"fieldCXY":"全国疫情中高风险地区名单（截止2021年7月12日15时）\\n\\n高风险地区：\\n云南省德宏傣族景颇族自治州瑞丽市姐告国门社区\\n\\n中风险地区：\\n无","_VAR_ACTION_REALNAME":"洪榕涛","_VAR_RELEASE":"true","_VAR_NOW_MONTH":"7","_VAR_ACTION_USERCODES":"1906400018","_VAR_ACTION_ACCOUNT":"1906400018","_VAR_ACTION_ORGANIZES_Names":"计算机科学与网络工程学院","_VAR_URL_Attr":"{}","_VAR_POSITIONS":"0206:02:1906400018","_VAR_ACTION_ORGANIZES_Codes":"0206","_VAR_NOW_YEAR":"2021","_VAR_ACTION_INDEP_ORGANIZES_Codes":"02","_VAR_ACTION_ORGANIZE":"0206","_VAR_ACTION_INDEP_ORGANIZE":"02","_VAR_ACTION_INDEP_ORGANIZE_Name":"学院","_VAR_ACTION_ORGANIZE_Name":"计算机科学与网络工程学院","_VAR_OWNER_ORGANIZES_Codes":"0206","_VAR_ADDR":"202.192.29.74","_VAR_OWNER_ORGANIZES_Names":"计算机科学与网络工程学院","_VAR_URL":"http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start","_VAR_ACTION_INDEP_ORGANIZES_Names":"学院","_VAR_OWNER_ACCOUNT":"1906400018","_VAR_OWNER_USERCODES":"1906400018","_VAR_NOW_DAY":"12","_VAR_OWNER_REALNAME":"洪榕涛","_VAR_NOW":"1626083170","_VAR_ENTRY_NUMBER":"-1","_VAR_ENTRY_NAME":"","_VAR_ENTRY_TAGS":""}', 'lang': 'zh'}
    data["csrfToken"]=result[0]
    client.headers["Referer"]="http://yqtb.gzhu.edu.cn/infoplus/form/XNYQSB/start"
    result=client.post("http://yqtb.gzhu.edu.cn/infoplus/interface/start",data=data)
    print(result.status_code)
    #拿到带有id的链接
    post_url=result.json()["entities"][0]
    print(post_url)
    print(int(time.time()))
    
    

if __name__ == '__main__':
    client=requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    url = "https://cas.gzhu.edu.cn/cas_server/login?service=http%3A%2F%2Fjwxt.gzhu.edu.cn%2Fsso%2Flyiotlogin"
    html = client.get(url, headers=headers)
    imgUrl = 'https://cas.gzhu.edu.cn/cas_server/captcha.jsp'
    img_res = client.get(imgUrl, stream=True)  # 获取验证码图片
    code = captcha_ver(img_res)
    while (len(code) != 4):
        imgUrl = 'https://cas.gzhu.edu.cn/cas_server/captcha.jsp'
        img_res = client.get(imgUrl, stream=True)  # 获取验证码图片
        code = captcha_ver(img_res)
    form_data = parse_form_data(html.text, code)
    print(form_data)
    res = client.post(url, data=form_data, headers=headers)
    if res.status_code==200:
        print("登录成功！")
    daka(client,headers)


