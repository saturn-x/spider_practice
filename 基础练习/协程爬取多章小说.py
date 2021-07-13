#coding=utf-8
##异步的操作都需要用await 也就是阻塞声明
#拿到章节的url=http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
###协程爬取的注意事项
#1.必须创建一个任务集合 里面保存的是异步任务函数的调用 tasks['xxx()',xxx()]
#2.异步函数 必须用async声明 并且使用的使用需要用await进行阻塞
import  asyncio
import re
import requests
import aiohttp
import aiofiles
async def download_chapter(cid,cname):
    chapter_url="http://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|"+cid+"%22,%22need_bookinfo%22:1}"

    chapter_url=re.sub("%22","\"",chapter_url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=chapter_url) as result:
            dic= await result.json()
            #print(dic)
            async with aiofiles.open(f"./novel/{cname}.txt","w",encoding="utf-8") as f:
                await  f.write(dic["data"]["novel"]["content"])

async def test():
    form_url = "http://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}"
    form_url = re.sub("%22", "\"", form_url)
    result = requests.get(form_url)
    tasks=[]#这个为异步任务
    for it in result.json()["data"]["novel"]["items"]:
        tasks.append(download_chapter(it["cid"],it["title"]))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(test())




