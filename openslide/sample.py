import os
import sys
import argparse
from openslide import OpenSlide, open_slide

from DigiPathUtils import decompose_file, save_img

parser = argparse.ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

decompose_file(
    filename=args.file, 
    delta=256, 
    begin=[30000,20000], 
    n=[5,5],
    out_dir='img/',
    #size=[256,256],
    #JPEG=True
    )