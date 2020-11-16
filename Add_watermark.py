from PIL import Image
import glob
import os

if not os.path.exists('./Image'):
    os.mkdir('./Image/')
img_path = './Image/*'
img_list = glob.glob(img_path) #获取图片路径

if not os.path.exists('./Watermark/'):
    os.mkdir('./Watermark/')
watermark_path = './Watermark/*'
watermark_list = glob.glob(watermark_path) #获取水印图片路径

if not os.path.exists('./Output/'):
    os.mkdir('./Output')

watermark = Image.open(watermark_list[0]) #提取水印
i = 1
for path in img_list:
    img = Image.open(path)
    img = img.resize((546,546),Image.ANTIALIAS) #改成546*546像素的
    img.paste(watermark,(0,0),mask=watermark) #这里一个mask很关键，不加掩盖png会不透明
    savepath = './Output/Cover'+str(i)+'.jpg'
    img.save(savepath,quality=95) #保存的时候将质量控制到95，大于95不稳定
    i = i + 1