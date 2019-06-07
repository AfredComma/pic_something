#coding:utf-8
from PIL import Image
import os
#图片压缩批处理
def compressImage(srcPath,dstPath):  #dstPath输出目录 srcPath输入目录
    for filename in os.listdir(srcPath):
        #如果不存在目的目录则创建一个，保持层级结构
        if not os.path.exists(dstPath):
                os.makedirs(dstPath)

        #拼接完整的文件或文件夹路径
        srcFile=os.path.join(srcPath,filename)
        dstFile=os.path.join(dstPath,filename).replace('png','jpg')
        print(srcFile)
        print(dstFile)

        #如果是文件就处理
        if os.path.isfile(srcFile):
            #打开原图片缩小后保存，可以用if srcFile.endswith(".jpg")或者split，splitext等函数等针对特定文件压缩
            sImg=Image.open(srcFile)
            w,h=sImg.size
            print(w,h)
            dImg=sImg.resize((int(w/1.5),int(h/1.5)),Image.ANTIALIAS)  #设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(dstFile) #也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            print(dstFile+" compressed succeeded")

        #如果是文件夹就递归
        if os.path.isdir(srcFile):
            compressImage(srcFile,dstFile)

if __name__=='__main__':
    # compressImage(u"D:/360极速浏览器下载/图片助手(ImageAssistant) 批量图片下载器/鲸准研究院：2018智能投研行业分析报告（附下载）___互联网数据资讯中心-199IT___中文互联网数据研究资讯中心-199IT",u"D:/360极速浏览器下载/图片助手(ImageAssistant) 批量图片下载器/test")
    compressImage(u"D:/360极速浏览器下载\图片助手(ImageAssistant) 批量图片下载器/艾瑞咨询：2019年中国数字音乐产业研究报告（附下载）___互联网数据资讯中心-199IT___中文互联网数据研究资讯中心-199IT",u"D:/360极速浏览器下载/图片助手(ImageAssistant) 批量图片下载器/airui_music")
    # compressImage(u"D:/360极速浏览器下载\图片助手(ImageAssistant) 批量图片下载器/5c6d0832edba2.pdf-图片",u"D:/360极速浏览器下载/图片助手(ImageAssistant) 批量图片下载器/motive")
    # compressImage(u"D:/BaiduNetdiskDownload/5c6d0832edba2.pdf-图片",u"D:/360极速浏览器下载/图片助手(ImageAssistant) 批量图片下载器/motive")
    # compressImage(u"D:/BaiduNetdiskDownload/f4285315404f1d4246f72d-images", u"D:/BaiduNetdiskDownload/f4285315404f1d4246f72d-images_small")

