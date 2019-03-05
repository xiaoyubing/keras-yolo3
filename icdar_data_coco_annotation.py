#coding:utf-8
"""
转换标注文本
"""
import os


data_path = './data/sroie_data_new_train/'
out_data_path = '/mnt/sda/icdar/keras-yolo3/data/sroie_data_new_train_out/'

path_list = os.listdir(data_path)
txt_names = []

train_f = open('train.txt', 'w')

for file_name in path_list:
    # print(file_name)
    if os.path.splitext(file_name)[1] == '.txt':
        txt_name = file_name.split('.')[0]
        txt_path = os.path.join(data_path, file_name)
        with open(txt_path, 'r') as f:
            labels = f.readlines()
            for label in labels:  # ｌａｂｅｌｓ的格式为（左上角两位坐标，右上角两位坐标，右下角两位坐标，左下角两位坐标，文本内容）
                splited_label = label.split(',')
                print(len(splited_label))
                l_u = tuple((int(splited_label[0]), int(splited_label[1])))  # 左上角坐标
                r_u = tuple((int(splited_label[2]), int(splited_label[3])))  # 右上角坐标
                r_d = tuple((int(splited_label[4]), int(splited_label[5])))  # 右下角坐标
                l_d = tuple((int(splited_label[6]), int(splited_label[7])))  # 左下角坐标

                result = "%s %d,%d,%d,%d,%d" % (data_path + txt_name + '.jpg', int(splited_label[0]),
                                                 int(splited_label[1]), int(splited_label[4]), int(splited_label[5]), 0)
                train_f.write(result)
                train_f.write('\n')

train_f.close()