import os


def merge_m3u8(m3u8,files):
    print(f"m3u8{m3u8}")
    list=[]
    for i in m3u8:
        if i.startswith("#"):
            continue
        else:
            i.strip()
            list.append(f'./{files}/tmp_{i.rsplit("/")[-1]}')
    s=" ".join(list)
    print(s)
    os.system(f"cat  {s}  > new.mp4")


if __name__ == '__main__':
    with open("./m3u8/second_m3u8.txt") as f:
        merge_m3u8(f,"video")



