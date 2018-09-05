# -*- coding: UTF-8 -*-

from PIL import Image

# im_path = r'/Users/zhouwenyang/Desktop/1.jpeg'
# im = Image.open(im_path)
# width,height = im.size
# print(im.size, width, height)
#
# print(im.format, im.format_description)
# im.show()

#新建图像
# newIm = Image.new('RGB',(100,100),'blue')
newIm = Image.new('RGB',(200, 100), (255, 0, 0, 60))
newIm.save('/Users/zhouwenyang/Desktop/2.png')