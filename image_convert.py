from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=416,height=416):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("D:/XL_download/keras-yolo3-master/keras-yolo3-master/VOCdevkit/VOC2007/JPEGImages/*.jpg"):
    convertjpg(jpgfile,"D:/XL_download/keras-yolo3-master/keras-yolo3-master/VOCdevkit/VOC2007/JPEGImagess")