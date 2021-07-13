import aiofiles
import aiohttp
import asyncio
import requests
import re
import os
##根据上面下的ts文件进行解密合并
from Crypto.Cipher import AES


async def dec_file(file,key):
    aes=AES.new(key=key.encode("utf8"),IV=b"0000000000000000",mode=AES.MODE_CBC)
    #异步读文件
    async with  aiofiles.open(file,"rb") as fr,aiofiles.open(f'./video/tmp_{file.split("/")[-1]}',"wb") as fw :
        content= await fr.read()
        await  fw.write(aes.decrypt(content))
    print(f'tmp_{file.split("/")[-1]}解密完成！')

##进行解密的io异步函数
async def dec_key(files_name,key):
    tasks = []
    for root,dirs,files  in os.walk(files_name):
        for i in files:
            file_path=files_name+"/"+i #。/video/xxx.ts
            #将任务创建进去
            task=asyncio.create_task(dec_file(file_path,key))
            tasks.append(task)
        await asyncio.wait(tasks)




if __name__ == '__main__':
    #url re
    obj=re.compile(r"URI")
    key_url=""
    with open("./m3u8/second_m3u8.txt") as f :
        for i in f:
            if obj.search(i):
                key_url=re.search(r"URI=\"(?P<url>.*?)\"", i).group("url")
        res=requests.get(key_url)
        key=res.text
        asyncio.run(dec_key("./video",key))

















