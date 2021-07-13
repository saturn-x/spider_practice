import json
import re

from requests import *


headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "cookie":"_uuid=EDCF033D-E662-7E42-B162-61F1F4014B0952595infoc; buvid3=BA3C7837-C2B1-4188-9E35-1B18A864DB30138392infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(JR|uY|u|Jm0J'uY|RJkmYkJ; LIVE_BUVID=AUTO3916091560957778; buvid_fp=BA3C7837-C2B1-4188-9E35-1B18A864DB30138392infoc; fingerprint3=d0a568c40386547c5949bc23b1a478da; fingerprint_s=2fd82e5cce7faf487cfad7142af2b69a; fingerprint=328ad87fb36b43433199b99b4c1e02d7; buvid_fp_plain=A6E9155F-C32B-405F-A85F-12EC4A41C59713437infoc; SESSDATA=ef222848,1640603098,a609d*61; bili_jct=7f40002d969f540103b2e650eb3f4c75; DedeUserID=252533270; DedeUserID__ckMd5=5567eb00295148b1; sid=jdr6n1h5; _ga=GA1.2.1981756252.1625239587; bp_video_offset_252533270=544343661175915587; CURRENT_QUALITY=80; _gid=GA1.2.1525293640.1625922145; bsource=search_baidu; bp_t_offset_252533270=546446477162171998; PVID=1; bfe_id=6f285c892d9d3c1f8f020adad8bed553",
    "referer":"https://space.bilibili.com/316568752/channel/detail?cid=171373&ctype=0"

}
#url https://api.bilibili.com/x/space/channel/video?mid=316568752&cid=171373&pn=2&ps=30&order=0&ctype=0&jsonp=jsonp&callback=__jp5
# for pn in range(1,9):
#     print(pn)
#     url="https://api.bilibili.com/x/space/channel/video?mid=316568752&cid=171373&pn="+str(pn)+"&ps=30&order=0&ctype=0&jsonp=jsonp&callback=__jp5"
#     res=get(url,headers=headers)
#     result=json.loads(re.search("__jp5\((.*)\)",res.text,flags=re.S).group(1))
#     #拿到是的每条记录
#     for i in result["data"]["list"]["archives"]:
#         print(i["title"],"BV:"+i["bvid"],"观看数:"+str(i["stat"]["view"]))
#
url="https://www.bilibili.com/video/BV1FK4y1E7m4"
res=get(url,headers=headers)
print(res.text)









