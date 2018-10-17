import os
import sys
import argparse
from openslide import OpenSlide, open_slide

parser = argparse.ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()

print("OpenSlide vendor:", OpenSlide.detect_format(args.file))
#print("PIL format:", ImageSlide.detect_format(args.file))
with open_slide(args.file) as slide:
    print("Dimensions:", slide.dimensions)
    print("Levels:", slide.level_count)
    print("Level dimensions:", slide.level_dimensions)
    print("Level downsamples:", slide.level_downsamples)
    #print("Properties:", slide.properties)
    #print("Associated images:", slide.associated_images)

    dim = slide.dimensions
    lvls = slide.level_count
    lvl_dim = slide.level_dimensions
    lvl_down = slide.level_downsamples

    print(type(slide))
    img = slide.read_region((0,0), 1, (100, 100))
    img = img.convert('RGB')
    img.save('tmp.jpg')
