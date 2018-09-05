# -*- coding: UTF-8 -*-

from PIL import Image,ImageFilter

imPath = "/Users/zhouwenyang/Desktop/3.jpg"

im = Image.open(imPath)

#高斯模糊
# im.filter(ImageFilter.GaussianBlur).show()

#普通模糊
# im.filter(ImageFilter.BLUR).show()

#边缘增强
# im.filter(ImageFilter.EDGE_ENHANCE).show()

#找到边缘
# im.filter(ImageFilter.FIND_EDGES).show()

#浮雕
# im.filter(ImageFilter.EMBOSS).show()

# 轮廓
# im.filter(ImageFilter.CONTOUR).show()

# 锐化
# im.filter(ImageFilter.SHARPEN).show()

# 平滑
# im.filter(ImageFilter.SMOOTH).show()

# 细节
im.filter(ImageFilter.DETAIL).show()