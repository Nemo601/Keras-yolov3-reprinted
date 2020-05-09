import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["plane", "ship", "storage-tank", "baseball-diamond", "tennis-court", "swimming-pool", "ground-track-field",
           "harbor", "bridge", "large-vehicle", "small-vehicle", "helicopter", "roundabout", "soccer-ball-field",
           "basketball-court"]


def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult)==1:
        #     continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        x_all = (int(xmlbox.find('x1').text), int(xmlbox.find('x2').text), int(xmlbox.find('x3').text), int(xmlbox.find('x4').text))
        y_all = (int(xmlbox.find('y1').text), int(xmlbox.find('y2').text), int(xmlbox.find('y3').text),
                 int(xmlbox.find('y4').text))
        x_min = min(x_all)
        x_max = max(x_all)
        y_min = min(y_all)
        y_max = max(y_all)
        # b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        b = (x_min, y_min, x_max, y_max)
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

