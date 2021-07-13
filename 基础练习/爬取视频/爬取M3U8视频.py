'''
1.Request URL: https://video.buycar5.cn/20200805/yCAPQKln/index.m3u8 通过该url获取第一层的m3u8文件
2.https://video.buycar5.cn/20200805/yCAPQKln/2000kb/hls/index.m3u8 实际的m38u文件 通过上面额进行拼接
3.key文件
'''
import aiofiles
import aiohttp
import asyncio
import requests
def download_file(url,name):
    response=requests.get(url)
    with open(f"./m3u8/{name}","w",encoding="utf-8") as f:
        f.write(response.text)
    return response.text

async def async_download_file(url,fname,session):
    async with session.get(url) as response:
        async with  aiofiles.open(f"./video/{fname}","wb") as f:
            #这里必须是await 读入的时候 各种 io 操作以及请求 操作必须加上await
            await f.write(await response.content.read())
    print(fname,"下載完畢")

async def download(fname):#传入一个真正m3u8的文件
    tasks=[] ##协程的任务集
    #异步创建一个 io文件流
    async  with aiohttp.ClientSession() as session:
        async  with  aiofiles.open(f"./m3u8/{fname}","r",encoding="utf-8") as f:
            #读文件 并同过文件进行协程下载
            async for i in f:
                if i.startswith("#"):
                    continue
                else:
                    i.strip()
                    # print("打印參數",i,i.rsplit("/")[-1])
                    task=asyncio.create_task(async_download_file(i,i.rsplit("/")[-1].strip(),session))
                    tasks.append(task)
            await asyncio.wait(tasks)
    #print(tasks)


if __name__ == '__main__':
    #下载第一层m3u8
    first_m3u8_url="https://video.buycar5.cn/20200805/yCAPQKln/index.m3u8"
    download_file("https://video.buycar5.cn/20200805/yCAPQKln/index.m3u8","first_m3u8.txt")
    #打开第一次m3u8的文件
    with open("./m3u8/first_m3u8.txt","r",encoding="utf-8") as f:
        #这里必须使用readline  如果使用read 返回的是一个str对象
        first_m3u8=f.readlines()
    for i in first_m3u8:
        if i.startswith("#"):
            continue
        else:
            i.strip()  #/20200805/yCAPQKln/2000kb/hls/index.m3u8  对链接 进行拼接
        second_m3u8_url=first_m3u8_url.split("20200805")[0]+i
    #下载第二层m3u8
    download_file(second_m3u8_url,"second_m3u8.txt")
    #通过第二层的url去异步下载文件
    asyncio.run(download("second_m3u8.txt"))
    










