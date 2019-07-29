import pickle
import argparse
import glob
import cv2
import os
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-r',help = "generate training images data from raw data",action="store_true")
parser.add_argument('-t',help = "generate testing images data from raw data",action="store_true")
parser.add_argument('-d',help = "raw data dir contain raw_data file such as data_batch_1 and so on")

args = parser.parse_args()


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def flat2img(flat_data):

    img_R = flat_data[0:1024].reshape((32, 32))
    img_G = flat_data[1024:2048].reshape((32, 32))
    img_B = flat_data[2048:3072].reshape((32, 32))
    img = np.dstack((img_R, img_G, img_B))
    return img

def generate_train_data(raw_data_dir):
    train_dir = raw_data_dir+'/train'
    if os.path.exists(train_dir):
        pass
    else:
        os.mkdir(train_dir)
# raw_data_dir should contain raw_data file such as "data_batch_1" and so on
    pattern = "*_batch_*"
    labels = {}
    for fname in glob.glob(raw_data_dir+'/'+pattern):
        diction = unpickle(fname)
        for i in tqdm(range(10000)):
            flat_data = diction[b'data'][i]
            filename = diction[b"filenames"][i]
            label = diction[b"labels"][i]

            filename = filename.decode()

            img = flat2img(flat_data)
            cv2.imwrite(raw_data_dir+'/train/'+filename,img)
            labels[filename] = label

    with open(train_dir+"/labels.txt", "w") as f:
        for (filename, label) in labels.items():
            f.write("{0} {1}\n".format(filename, label))

def generate_test_data(raw_data_dir):
    test_dir = raw_data_dir+'/test'
    if os.path.exists(test_dir):
        pass
    else:
        os.mkdir(test_dir)
    pattern = "*_batch"
    labels = {}
    for fname in glob.glob(raw_data_dir+'/'+pattern):
        diction = unpickle(fname)
        for i in tqdm(range(10000)):
            flat_data = diction[b'data'][i]
            filename = diction[b"filenames"][i]
            label = diction[b"labels"][i]

            filename = filename.decode()

            img = flat2img(flat_data)
            cv2.imwrite(raw_data_dir+'/test/'+filename,img)
            labels[filename] = label

    with open(test_dir+"/labels.txt", "w") as f:
        for (filename, label) in labels.items():
            f.write("{0} {1}\n".format(filename, label))
if args.r:
    generate_train_data(args.d)
if args.t:
    generate_test_data(args.d)
