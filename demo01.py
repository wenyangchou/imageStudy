# -*- coding: UTF-8 -*-

from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open("/Users/zhouwenyang/Desktop/1.jpeg"),lang='chi_sim')
print(text)