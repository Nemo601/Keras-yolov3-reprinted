# Keras-yolov3-reprinted
该项目是基于keras的yolov3实现，源模型转载自https://github.com/qqwweee/keras-yolo3
下载该项目后，可根据选择当前模型训练使用的DOTA数据集Part 1和一个可供训练的权重文件，下载地址：链接：https://pan.baidu.com/s/18QNO6e4zT9cQuP4AjFqwPw 提取码：jix9，其中JPEGImages文件夹建议直接解压至VOCdevkit\VOC2007目录中，权重文件解压至logs\000文件夹中（因为在项目中，我定义的图片和权重文件读取目录就是这两个）
较为详细的使用说明附在该工程的doc文档中。

下面是该工程的部分功能说明:

VOCdevkit/VOC2007/new.py:将Annotations中的xml数据集转化为VOC格式的练习集和验证集

yolo3/model.py:包含了yolov3的神经网络结构信息、bounding box的预测方式、IoU的计算方式等关于yolov3的模型信息

convert.py:将.weight的权重文件转化为.h5权重文件

converter.py:将DOTA数据集的labels转化为VOC数据集类型的labels

image_convert:将PNG图片批量转化为JPG图像

train.py:用来根据自己的数据集训练yolov3的模型

voc_annotation.py:将new.py生成的文件转化为训练用的数据

yolo_video.py:训练出模型后，用yolo_video来进行目标检测
