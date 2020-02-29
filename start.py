#!/usr/bin/python3
"""
图片差异处理程序:
    1、确定底图
    2、过滤用到的照片
    3、找出差异
    4、生成 差异图
https://blog.csdn.net/kisssfish/article/details/96480879
https://blog.csdn.net/huuinn/article/details/78430722
"""

from PIL import Image
from PIL import ImageChops 
import os

def compare_images(path_other):
    global image_base
    image_other = Image.open(path_other)
    try: 
        image_base = ImageChops.darker(image_base, image_other)    #darker、lighter、difference
    except ValueError as e:
        text = ("图片长宽不一致")
        print("【{0}】{1}".format(e,text))
        
if __name__ == '__main__':
    print("本次处理图片为本目录下以下文件：")
    files=[]
    for file in os.listdir(os.getcwd()):
        if((file.endswith("jpg")or file.endswith("JPG")) and (file.startswith("IMG") or file.startswith("img"))):
                files.append(file)
    #print(files)
    image_base=Image.open(files[0])
    for pic in files:
            print("  -->  ",pic)
            compare_images(pic)

    #结束、生成结果图：
    print("正在写入最终文件...")
    image_base.save("result.png")
    print("（已经完成，如有杂项，请删除源文件，重新执行）")
