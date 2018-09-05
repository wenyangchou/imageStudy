# -*- coding: UTF-8 -*-

from PIL import Image

#裁剪图片
im = Image.open("/Users/zhouwenyang/Desktop/3.jpg")
cropedIm = im.crop((700, 100, 1200, 1000))
# cropedIm.save("/Users/zhouwenyang/Desktop/4.jpg")

#复制粘贴另一个图片
# im.paste(cropedIm,(100,100)) #左上
# im.show()

#调整图片大小
# width,height = im.size
# resizedIm = im.resize((width,height+1000))
# resizedIm.show()

#图片翻转
# im.rotate(90).show() #旋转
# im.transpose(Image.FLIP_LEFT_RIGHT).show() #左右镜像
im.transpose(Image.FLIP_TOP_BOTTOM).show() #上下翻转
