#coding:utf-8
"""
预测一个文件夹下的所有图片的,生成与图片同名的txt，文件中记录该图片的预测结果：x1,y1,x3,y3 date score
"""
import os
import argparse
from icdar_date_yolo import YOLO
from PIL import Image


def detect_img_dir(yolo,img_dir,out_dir):
    """
    遍历文件夹下的所有图片,并使用yolo v3 模型进行预测
    :param yolo:
    :param img_dir:
    :return:
    """
    img_path_list = os.listdir(img_dir)
    pic_name = []
    for file_name in img_path_list:
        # print(file_name)
        if os.path.splitext(file_name)[1] == '.txt':
            # print()
            pic_name.append(file_name.split('.')[0])

    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )

    FLAGS = parser.parse_args()

    detect_img_dir(YOLO(**vars(FLAGS)), '', '')

